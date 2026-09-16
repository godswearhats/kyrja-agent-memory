"""Repair the cap-contaminated Supermemory store (2026-07-22 outage).

340/626 documents were marked 'done' with zero extracted memories after the
subscription cap killed every `claude -p` call from 23:38:07Z onward. This
supervisor re-extracts them on the subscription, cap-safely:

- chronological batches (deployment-shaped: later sessions extract into a
  store already holding earlier memories, as a sequential ingest would have)
- health-gated: no new batch is submitted while `claude -p` is cap-stalled
- verified: per-batch yield check; a final full census must show every
  document with >=1 memory, else verification FAILS
- boundary pass: docs processed within +/-120s of any proxy error/stall are
  conservatively re-extracted even if they show partial yield

Usage: python3 audit_repair.py <scenario_dir> [--reader] [--batch N]
--reader: on verification PASS, re-run the MASQ reader for the supermemory
arm (run.py merge-on-write protects all other arms' results).
"""
import argparse, datetime, json, os, subprocess, sys, time

import arm_supermemory as arm

HARNESS = os.path.dirname(os.path.abspath(__file__))
PROXY_LOG = os.path.join(HARNESS, "proxy-log.jsonl")
POLL_S = 15
BATCH_DONE_TIMEOUT_S = 4 * 3600     # throttled worst case ~34 calls/batch
CAP_SLEEP_S = 900
MAX_ROUNDS = 60


def log(msg):
    print(f"[{datetime.datetime.now():%H:%M:%S}] {msg}", flush=True)


def claude_healthy():
    from clean_contaminated import ERROR_SIGNATURES
    try:
        r = subprocess.run(
            ["claude", "-p", "--model", "claude-opus-4-8", "Reply: OK"],
            capture_output=True, text=True, timeout=120)
        out = r.stdout.strip()
        return (r.returncode == 0 and out != ""
                and not any(s in out.lower() for s in ERROR_SIGNATURES))
    except Exception:
        return False


def load_family(scenario_dir):
    fam_path = [os.path.join(scenario_dir, f) for f in os.listdir(scenario_dir)
                if f.startswith("family-")][0]
    return json.load(open(fam_path))


def batch_wait(tag, custom_ids):
    t0 = time.time()
    while time.time() - t0 < BATCH_DONE_TIMEOUT_S:
        _, docs = arm._existing_custom_ids(tag)
        mine = [d for d in docs if d.custom_id in custom_ids]
        if len(mine) == len(custom_ids) and all(
                d.status in ("done", "failed") for d in mine):
            return mine
        time.sleep(POLL_S)
    raise TimeoutError(f"batch not done after {BATCH_DONE_TIMEOUT_S}s")


def repair(scenario_dir, batch_size, max_docs=None):
    fam = load_family(scenario_dir)
    tag = arm._tag(fam, scenario_dir)
    sess_order = {s["id"]: i for i, s in enumerate(fam["world_sessions"])}
    sess_by_id = {s["id"]: s for s in fam["world_sessions"]}
    t_start = time.time()

    attempts, given_up = {}, []
    rounds = [0]

    def drain(queue, label):
        """Repair every doc in `queue` through verified batches."""
        queue.sort(key=lambda d: sess_order.get(
            (d.custom_id or "").split(":")[-1], 1 << 30))
        while queue and rounds[0] < MAX_ROUNDS:
            rounds[0] += 1
            batch, queue[:] = queue[:batch_size], queue[batch_size:]
            log(f"{label} round {rounds[0]}: repairing {len(batch)} "
                f"(queue {len(queue)}, given up {len(given_up)})")

            while not claude_healthy():
                log(f"claude -p unhealthy (cap window?) — sleeping "
                    f"{CAP_SLEEP_S}s before submitting")
                time.sleep(CAP_SLEEP_S)

            ids = set()
            for d in batch:
                sid = d.custom_id.split(":")[-1]
                s = sess_by_id[sid]
                attempts[d.custom_id] = attempts.get(d.custom_id, 0) + 1
                arm._cl().documents.delete(d.id)
                content = (f"— {s['writer']}, day {s['day']}\n"
                           f"{s.get('prose') or s['text']}")
                arm._cl().documents.add(content=content, container_tag=tag,
                                        custom_id=d.custom_id)
                ids.add(d.custom_id)
            done = batch_wait(tag, ids)
            n_ok = 0
            for d in done:
                g = arm._cl().documents.get(d.id).model_dump()
                if [m for m in (g.get("memories") or [])
                        if (m.get("memory") or m.get("content") or "").strip()]:
                    n_ok += 1
                elif attempts[d.custom_id] >= 3:
                    given_up.append(d.custom_id)
                else:
                    queue.append(d)
            log(f"{label} round {rounds[0]}: batch yield {n_ok}/{len(batch)}")
        if queue:
            log(f"MAX_ROUNDS ({MAX_ROUNDS}) exhausted with "
                f"{len(queue)} docs left")

    log("full census (one-time)...")
    queue = arm._zero_yield_docs(tag)
    log(f"{len(queue)} zero-yield docs to repair")
    if max_docs is not None:
        queue.sort(key=lambda d: sess_order.get(
            (d.custom_id or "").split(":")[-1], 1 << 30))
        queue = queue[:max_docs]
        log(f"smoke mode: limiting to {len(queue)} doc(s)")
    drain(queue, "main")

    if max_docs is not None:
        ok = not given_up
        log(f"smoke mode: done ({'OK' if ok else 'PROBLEMS'}); skipping "
            f"boundary pass + verification gate")
        return ok

    # Boundary passes: any doc whose processing window touches a proxy
    # error/stall may be PARTIALLY extracted (some calls landed, some died) —
    # yield alone cannot detect that, so re-extract conservatively, through
    # the same verified drain loop (the 2026-07-25 one-shot version left 22
    # docs empty when resets hit during the pass itself). Iterate until a
    # pass generates no new events, so events during a pass are themselves
    # boundary-checked by the next one.
    def events_since(ts):
        out = []
        for line in open(PROXY_LOG):
            rec = json.loads(line)
            if ("error" in rec or rec.get("stalled")) and rec["ts"] >= ts:
                out.append(rec["ts"])
        return out

    handled_cutoff = t_start
    for bp in range(3):
        sus_ts = events_since(handled_cutoff)
        if not sus_ts:
            break
        handled_cutoff = max(sus_ts) + 1
        _, docs = arm._existing_custom_ids(tag)
        redo = []
        for d in docs:
            try:
                u = datetime.datetime.fromisoformat(
                    str(d.updated_at).replace("Z", "+00:00")).timestamp()
            except Exception:
                continue
            if any(abs(u - t) <= 120 for t in sus_ts):
                redo.append(d)
        log(f"boundary pass {bp + 1}: {len(sus_ts)} error/stall events; "
            f"re-extracting {len(redo)} boundary docs")
        for d in redo:
            attempts.pop(d.custom_id, None)
        drain(redo, f"boundary{bp + 1}")

    # Final verification census. Events after the boundary-pass cutoff are
    # reported separately: docs touched by those could be partially extracted
    # and no later pass re-checked them — surface it, don't hide it.
    all_events = events_since(t_start)
    late_events = events_since(handled_cutoff)
    empty = arm._zero_yield_docs(tag)
    have, docs = arm._existing_custom_ids(tag)
    n_sessions = len(arm._sessions(fam))
    ok = not empty and len(have) >= n_sessions and not late_events
    verdict = {
        "tag": tag, "ts": time.time(),
        "n_sessions": n_sessions, "n_docs": len(have),
        "n_zero_yield": len(empty),
        "zero_yield_docs": [d.custom_id for d in empty],
        "error_stall_events_during_repair": len(all_events),
        "events_after_boundary_cutoff": len(late_events),
        "pass": ok,
    }
    path = os.path.join(scenario_dir, f"repair-verification-{tag}.json")
    json.dump(verdict, open(path, "w"), indent=1)
    log(f"VERIFICATION {'PASS' if ok else 'FAIL'} — {path}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario_dir")
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--reader", action="store_true")
    ap.add_argument("--max-docs", type=int, default=None,
                    help="smoke mode: repair at most N docs, report batch "
                         "yield, skip the pass/fail verification gate")
    args = ap.parse_args()

    ok = repair(args.scenario_dir, args.batch, args.max_docs)
    if not ok:
        sys.exit(1)
    if args.reader:
        log("verification PASS — re-running reader (supermemory arm only)")
        r = subprocess.run(
            [sys.executable, os.path.join(HARNESS, "run.py"),
             args.scenario_dir, "--arms", "supermemory"],
            cwd=HARNESS)
        sys.exit(r.returncode)


if __name__ == "__main__":
    main()
