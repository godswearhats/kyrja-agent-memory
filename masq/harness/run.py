#!/usr/bin/env python3
"""MASQ harness v2 — multi-scope chain evaluation.

Scores one scenario (v2 family JSON + composed corpus) across three arms:
  paste-everything, last-write-wins, perfect-retrieval ceiling.

Reader call via `claude -p` CLI, temp 0, one re-ask on parse fail.

Usage:
    python3 run.py <scenario_dir>
    python3 run.py <scenario_dir> --model claude-sonnet-4-6
    python3 run.py <scenario_dir> --arms paste,ceiling
    python3 run.py dir1/ dir2/ dir3/
"""
import argparse, json, os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

SYSTEM_PROMPT = (
    "You are a careful annotator. Follow the instructions exactly and "
    "answer only in the requested format."
)

A_FORMAT = """\
Reply in exactly this format, one field per line:
CURRENT_VALUE: <value or contested>
CURRENT_SETTER: <name or contested:{name1,name2}>
CHAIN_LENGTH: <N>
STEP_1_VALUE: <value>
STEP_1_SETTER: <name>
STEP_1_TYPE: <initial|self_revision|supersession|collision|resolution>
[repeat STEP_i_VALUE/SETTER/TYPE for each step up to CHAIN_LENGTH]
UNRESOLVED_CONFLICT: <true|false>"""

B_FORMAT = """\
A conflict means two people set different values and neither acknowledged \
the other's change. If a later writer explicitly references the earlier \
value or writer and overrides it, that is a resolved supersession, not a \
conflict. If someone later acknowledged BOTH sides and resolved it, the \
conflict is resolved.
Decide as follows: if the current value was set by a resolution or an \
acknowledged supersession, act on it and report CONFLICT: false. Only if \
two different values were set and the disagreement was never acknowledged \
or resolved, report CONFLICT: true and you may choose the action "none".
First trace the change history for this setting in one or two sentences. \
Then end your reply with exactly these two lines, in this order:
ACTION: <one item from the menu>
CONFLICT: <true or false>"""

# ---------------------------------------------------------------------------
# Arms
# ---------------------------------------------------------------------------

def arm_paste(family, corpus_dir):
    """Identity memory: the entire corpus, verbatim."""
    p = os.path.join(corpus_dir, "corpus.md")
    with open(p) as f:
        return f.read()


def arm_lww(family, _corpus_dir):
    """Last-write-wins: most recent chain-write session for the kernel entity.

    Picks the latest session regardless of scope — a dumb baseline that
    doesn't understand scope context.
    """
    entity = family["meta"]["kernel_entity"]
    chain_sessions = [s for s in family["world_sessions"]
                      if s["kind"].startswith("chain_")
                      and s.get("fact") == entity]
    if not chain_sessions:
        return "[No writes found]"
    latest = max(chain_sessions, key=lambda s: (s["day"], s.get("id", "")))
    header = (f"[Memory — last known write for "
              f"{entity} {family['meta']['param']}]")
    body = (f"— {latest['writer']}, day {latest['day']}\n"
            f"  {latest.get('prose', latest['text'])}")
    return f"{header}\n\n{body}\n"


def arm_ceiling(family, _corpus_dir):
    """Perfect-retrieval ceiling: complete target-scope chain, clearly formatted.

    Every chain step with writer/day/type marker. Gives the model everything
    it needs to answer correctly.
    """
    target = family["meta"]["target_scope"]
    entity = family["meta"]["kernel_entity"]
    param = family["meta"]["param"]
    chain = family["scope_chains"][target]

    chain_sessions = sorted(
        [s for s in family["world_sessions"]
         if s.get("scope") == target and s["kind"].startswith("chain_")],
        key=lambda s: s["day"])

    header = (f"[Memory — complete write history for {entity} {param}, "
              f"context: {target}]")
    lines = [header, ""]
    for step, sess in zip(chain, chain_sessions):
        lines.append(f"— {sess['writer']}, day {sess['day']} "
                     f"[{step['type']}]")
        lines.append(f"  {sess.get('prose', sess['text'])}")
        lines.append("")
    return "\n".join(lines)


from arm_vector import make_vector_arm
from arm_bm25 import make_bm25_arm
from arm_scopefilter import arm_scopefilter


def arm_supermemory(*a, **kw):
    """Lazy shim — the supermemory SDK is an optional dependency, and importing
    it eagerly makes every other arm unrunnable for anyone who lacks it."""
    from arm_supermemory import arm_supermemory as _impl
    return _impl(*a, **kw)

ARMS = {
    "paste":      ("paste-everything",   arm_paste),
    "lww":        ("last-write-wins",    arm_lww),
    "ceiling":    ("perfect-retrieval",  arm_ceiling),
    "vector_k5":  ("vector-rag-k5",      make_vector_arm(5)),
    "vector_k10": ("vector-rag-k10",     make_vector_arm(10)),
    "vector_k20": ("vector-rag-k20",     make_vector_arm(20)),
    "bm25_k10":   ("bm25-rag-k10",       make_bm25_arm(10)),
    "scopefilter":("where-scope-target", arm_scopefilter),
    "supermemory":("supermemory-k20",    arm_supermemory),
}

# ---------------------------------------------------------------------------
# Reader
# ---------------------------------------------------------------------------

RL_SIGNATURES = ("rate limit", "rate_limit", "overloaded", "overload_error",
                 "429", "too many requests", "service unavailable", "503",
                 "usage limit", "temporarily")


def call_reader(prompt, context, model, max_tries=5):
    """Call the reader, retrying on *infrastructure* failure only.

    A delivery failure (non-zero exit, empty stdout, or a rate-limit /
    overload signature in stderr) is retried with exponential backoff.
    Only a genuinely-returned model answer is ever returned to the grader;
    this prevents the v1 rate-limit contamination (error payloads scored as
    PARSE_FAIL). It does NOT alter scoring of real model responses.
    """
    full = context.rstrip() + "\n\n---\n\n" + prompt
    delay = 3.0
    last = ""
    for attempt in range(max_tries):
        r = subprocess.run(
            ["claude", "-p", "--model", model, "--system-prompt", SYSTEM_PROMPT,
             "--output-format", "text"],
            input=full, capture_output=True, text=True, timeout=300)
        out = r.stdout.strip()
        err = (r.stderr or "").lower()
        # A real A/B answer is long and structured; an error blurb is short.
        # Only treat a short stdout as an error signature to avoid flagging a
        # genuine rationale that happens to contain a trigger word.
        short_err = len(out) < 60 and any(sig in out.lower()
                                          for sig in RL_SIGNATURES)
        infra_fail = (
            r.returncode != 0
            or not out
            or any(sig in err for sig in RL_SIGNATURES)
            or short_err
        )
        if not infra_fail:
            return out
        last = out
        if attempt < max_tries - 1:
            print(f"    infra-retry {attempt+1}/{max_tries-1} "
                  f"(rc={r.returncode}, len={len(out)}) backoff {delay:.0f}s",
                  file=sys.stderr)
            time.sleep(delay)
            delay = min(delay * 2, 60.0)
    return last

# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _extract(text, pattern):
    # Last match, so a reasoning scaffold that mentions "action"/"conflict"
    # in prose cannot shadow the final answer lines.
    ms = list(re.finditer(pattern, text, re.I))
    return ms[-1].group(1).strip() if ms else None


def parse_a(text):
    out = dict(
        current_value=_extract(text, r"CURRENT_VALUE:\s*(.+)"),
        current_setter=_extract(text, r"CURRENT_SETTER:\s*(.+)"),
        chain_length=_extract(text, r"CHAIN_LENGTH:\s*(\d+)"),
        unresolved_conflict=_extract(text, r"UNRESOLVED_CONFLICT:\s*(.+)"),
    )
    steps = []
    for i in range(1, 20):
        v = _extract(text, rf"STEP_{i}_VALUE:\s*(.+)")
        s = _extract(text, rf"STEP_{i}_SETTER:\s*(.+)")
        t = _extract(text, rf"STEP_{i}_TYPE:\s*(.+)")
        if v is None and s is None and t is None:
            break
        steps.append(dict(value=v, setter=s, type=t))
    out["steps"] = steps
    return out


def parse_b(text):
    return dict(
        action=_extract(text, r"ACTION:\s*(.+)"),
        conflict=_extract(text, r"CONFLICT:\s*(.+)"),
    )

# ---------------------------------------------------------------------------
# Grading
# ---------------------------------------------------------------------------

def norm(v):
    if v is None:
        return "n/a"
    s = str(v).strip().lower()
    s = re.sub(r"\s*(req/s|rpm|rps)\s*$", "", s)
    return s


def values_match(got, expected):
    if expected == "n/a" and got == "n/a":
        return True
    if "contested" in expected and "contested" in got:
        return True
    if got == expected:
        return True
    m = re.match(r"^(\d+)", got)
    if m and m.group(1) == expected:
        return True
    # Closed-vocabulary match: GT values are bare tokens (e.g. "payments"),
    # but prose names them descriptively ("the payments team"), so a faithful
    # reader answers "payments team". Accept when every GT token appears in
    # the model's answer (directional: the model may ADD descriptors, not
    # truncate). Guards against rambling answers by requiring the GT token
    # set to be non-empty and the extra-word count to be small.
    got_toks = got.split()
    exp_toks = expected.split()
    if exp_toks and set(exp_toks) <= set(got_toks) and \
       len(got_toks) - len(exp_toks) <= 2:
        return True
    return False


def align_chains(gt_steps, model_steps):
    """LCS-based alignment of GT and model step sequences.
    Returns list of (gt_idx, model_idx) pairs."""
    n, m = len(gt_steps), len(model_steps)
    if n == 0 or m == 0:
        return []
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            gv = norm(gt_steps[i - 1]["value"])
            gs = norm(gt_steps[i - 1]["setter"])
            mv = norm(model_steps[j - 1].get("value"))
            ms = norm(model_steps[j - 1].get("setter"))
            if values_match(mv, gv) and values_match(ms, gs):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    pairs = []
    i, j = n, m
    while i > 0 and j > 0:
        gv = norm(gt_steps[i - 1]["value"])
        gs = norm(gt_steps[i - 1]["setter"])
        mv = norm(model_steps[j - 1].get("value"))
        ms = norm(model_steps[j - 1].get("setter"))
        if values_match(mv, gv) and values_match(ms, gs):
            pairs.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    return pairs


def grade_a(parsed, gt):
    """Grade v2 A-response. Returns dict with per-field results + score."""
    results = {}

    results["current_value"] = values_match(
        norm(parsed.get("current_value")), norm(gt["current_value"]))
    results["current_setter"] = values_match(
        norm(parsed.get("current_setter")), norm(gt["current_setter"]))
    results["unresolved_conflict"] = (
        norm(parsed.get("unresolved_conflict"))
        == norm(gt["unresolved_conflict"]))

    gt_len = gt["chain_length"]
    try:
        parsed_len = int(parsed.get("chain_length") or 0)
    except (ValueError, TypeError):
        parsed_len = 0
    results["chain_length"] = (parsed_len == gt_len)

    gt_steps = gt["steps"]
    parsed_steps = parsed.get("steps", [])
    alignment = align_chains(gt_steps, parsed_steps)
    matched_gt = {gi for gi, _ in alignment}

    step_correct, step_total = 0, 0
    for gi in range(len(gt_steps)):
        for field in ["value", "setter", "type"]:
            step_total += 1
            if gi in matched_gt:
                mi = next(mi for ggi, mi in alignment if ggi == gi)
                expected = norm(gt_steps[gi][field])
                got = norm(parsed_steps[mi].get(field))
                if values_match(got, expected):
                    step_correct += 1

    results["step_correct"] = step_correct
    results["step_total"] = step_total

    terminal_correct = sum([results["current_value"],
                            results["current_setter"],
                            results["unresolved_conflict"],
                            results["chain_length"]])
    total = 4 + step_total
    correct = terminal_correct + step_correct
    results["score"] = correct / total if total > 0 else 0
    return results


def grade_b(parsed, gt):
    """Grade v2 B-response."""
    if parsed.get("action") is None or parsed.get("conflict") is None:
        return {"pass": False, "reason": "PARSE_FAIL"}

    flag = parsed["conflict"].lower().strip() == "true"

    if gt["conflict_flag"]:
        passed = flag
        reason = "flag_correct" if flag else "flag_missed"
    else:
        action_ok = norm(parsed["action"]) == norm(gt["action"])
        flag_ok = not flag
        passed = action_ok and flag_ok
        parts = []
        if not action_ok:
            parts.append(f"action: got {parsed['action']}, "
                         f"expected {gt['action']}")
        if not flag_ok:
            parts.append("false_alarm")
        reason = "correct" if passed else "; ".join(parts)
    return {"pass": passed, "reason": reason}

# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_arm(family, arm_key, corpus_dir, model):
    """Run A + B queries for one arm. Returns result dict."""
    arm_name, arm_fn = ARMS[arm_key]
    gt = family["ground_truth"]

    context = arm_fn(family, corpus_dir)

    # A query
    a_prompt = family["a_query"] + "\n\n" + A_FORMAT
    a_raw = call_reader(a_prompt, context, model)
    a_parsed = parse_a(a_raw)
    if a_parsed.get("current_value") is None and not a_parsed["steps"]:
        retry = a_prompt + ("\n\n(Your previous answer could not be parsed. "
                            "Please use the exact format above.)")
        a_raw = call_reader(retry, context, model)
        a_parsed = parse_a(a_raw)
    a_grade = grade_a(a_parsed, gt)

    # B query
    b_prompt = family["b_query"] + "\n\n" + B_FORMAT
    b_raw = call_reader(b_prompt, context, model)
    b_parsed = parse_b(b_raw)
    if b_parsed.get("action") is None or b_parsed.get("conflict") is None:
        retry = b_prompt + ("\n\n(Your previous answer could not be parsed. "
                            "Please use the exact format above.)")
        b_raw = call_reader(retry, context, model)
        b_parsed = parse_b(b_raw)
    b_grade = grade_b(b_parsed, gt)

    return {
        "arm": arm_name,
        "arm_key": arm_key,
        "model": model,
        "a_raw": a_raw,
        "a_parsed": a_parsed,
        "a_grade": a_grade,
        "a_score": a_grade["score"],
        "b_raw": b_raw,
        "b_parsed": b_parsed,
        "b_grade": b_grade,
    }


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def print_summary(results, meta):
    domain = meta.get("domain", "?")
    target = meta.get("target_scope", "?")
    entity = meta.get("kernel_entity", "?")
    print(f"\n{'='*60}")
    print(f"RESULTS — {domain} / {entity} / target={target}")
    print(f"{'='*60}")
    print(f"  {'arm':<22}  {'A-score':>8}  {'B-pass':>6}  B-reason")
    print(f"  {'----':<22}  {'-------':>8}  {'------':>6}  --------")
    for r in sorted(results, key=lambda r: r["arm"]):
        a_pct = f"{r['a_score']:.0%}"
        b_sym = "PASS" if r["b_grade"]["pass"] else "FAIL"
        print(f"  {r['arm']:<22}  {a_pct:>8}  {b_sym:>6}  "
              f"{r['b_grade']['reason']}")

    # Detail for each arm
    print(f"\n  A-detail:")
    for r in sorted(results, key=lambda r: r["arm"]):
        g = r["a_grade"]
        parts = [f"val={'✓' if g['current_value'] else '✗'}",
                 f"setter={'✓' if g['current_setter'] else '✗'}",
                 f"conflict={'✓' if g['unresolved_conflict'] else '✗'}",
                 f"len={'✓' if g['chain_length'] else '✗'}",
                 f"steps={g['step_correct']}/{g['step_total']}"]
        print(f"    {r['arm']:<22}  {' '.join(parts)}")


def check_sanity(results):
    print(f"\n  SANITY GATES:")
    ceiling = [r for r in results if r["arm_key"] == "ceiling"]
    if ceiling:
        c = ceiling[0]
        if c["b_grade"]["pass"]:
            print(f"    OK    ceiling B-pass")
        else:
            print(f"    WARN  ceiling B-fail: {c['b_grade']['reason']}")
        if c["a_score"] >= 0.8:
            print(f"    OK    ceiling A≥80% ({c['a_score']:.0%})")
        else:
            print(f"    WARN  ceiling A<80% ({c['a_score']:.0%})")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def find_family_json(d):
    for f in os.listdir(d):
        if f.startswith("family-") and f.endswith(".json"):
            return os.path.join(d, f)
    raise FileNotFoundError(f"no family-*.json in {d}")


def run_scenario(corpus_dir, model, arm_keys, concurrency):
    fam_path = find_family_json(corpus_dir)
    with open(fam_path) as f:
        family = json.load(f)

    meta = family["meta"]
    gt = family["ground_truth"]
    print(f"\nScenario: {corpus_dir}")
    print(f"  domain={meta['domain']}  entity={meta['kernel_entity']}  "
          f"target={meta['target_scope']}  model={model}")
    print(f"  scopes={[s['name'] for s in meta['scopes']]}  "
          f"pattern={next(s['pattern'] for s in meta['scopes'] if s['name'] == meta['target_scope'])}")
    print(f"  GT: value={gt['current_value']} setter={gt['current_setter']} "
          f"conflict={gt['unresolved_conflict']} chain_len={gt['chain_length']}")
    print(f"  arms={arm_keys}  calls={len(arm_keys)*2}")

    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futures = {
            ex.submit(evaluate_arm, family, ak, corpus_dir, model): ak
            for ak in arm_keys
        }
        for fut in as_completed(futures):
            ak = futures[fut]
            try:
                r = fut.result()
                results.append(r)
                sym = "✓" if r["b_grade"]["pass"] else "✗"
                print(f"  {ARMS[ak][0]:<22}  A={r['a_score']:.0%}  B={sym}")
            except Exception as e:
                print(f"  {ARMS[ak][0]:<22}  ERROR: {e}", file=sys.stderr)

    elapsed = time.time() - t0
    print(f"  ({len(results)} arms in {elapsed:.1f}s)")

    print_summary(results, meta)
    check_sanity(results)

    out_path = os.path.join(corpus_dir,
                            f"results-{meta['domain']}-{model}.json")

    # Merge with any existing results for OTHER arms, replacing only the arms
    # just run. A partial-arm invocation (e.g. adding the adapter arm later)
    # must never clobber the baseline arms already on disk.
    merged = list(results)
    new_keys = {r["arm_key"] for r in results}
    if os.path.exists(out_path):
        try:
            prev = json.load(open(out_path)).get("results", [])
            merged = [r for r in prev
                      if r.get("arm_key") not in new_keys] + merged
        except Exception:
            pass

    out_data = {
        "meta": {
            "domain": meta["domain"],
            "model": model,
            "corpus_dir": str(corpus_dir),
            "target_scope": meta["target_scope"],
            "n_scopes": meta.get("n_scopes"),
            "family": os.path.basename(fam_path),
            "n_results": len(merged),
            "elapsed_s": round(elapsed, 1),
        },
        "ground_truth": gt,
        "results": merged,
    }
    with open(out_path, "w") as f:
        json.dump(out_data, f, indent=2, default=str)
    print(f"\n  Wrote {out_path}  ({len(merged)} arms: "
          f"{','.join(sorted(r['arm_key'] for r in merged))})")
    return results


def main():
    ap = argparse.ArgumentParser(description="MASQ v2 harness")
    ap.add_argument("dirs", nargs="+",
                    help="scenario directories (family-*.json + corpus.md)")
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--arms", default="paste,lww,ceiling",
                    help="comma-separated arm keys")
    ap.add_argument("--concurrency", type=int, default=3)
    a = ap.parse_args()

    arm_keys = [k.strip() for k in a.arms.split(",")]
    for k in arm_keys:
        if k not in ARMS:
            print(f"unknown arm: {k} (choose from {sorted(ARMS)})",
                  file=sys.stderr)
            sys.exit(1)

    all_results = {}
    for d in a.dirs:
        d = os.path.abspath(d)
        if not os.path.isdir(d):
            print(f"not a directory: {d}", file=sys.stderr)
            sys.exit(1)
        results = run_scenario(d, a.model, arm_keys, a.concurrency)
        all_results[d] = results

    if len(all_results) > 1:
        print(f"\n{'='*60}")
        print(f"CROSS-SCENARIO SUMMARY")
        print(f"{'='*60}")
        for d, results in all_results.items():
            for r in sorted(results, key=lambda r: r["arm"]):
                sym = "✓" if r["b_grade"]["pass"] else "✗"
                print(f"  {os.path.basename(d):<30}  {r['arm']:<22}  "
                      f"A={r['a_score']:.0%}  B={sym}")


if __name__ == "__main__":
    main()
