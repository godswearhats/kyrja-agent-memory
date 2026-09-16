#!/usr/bin/env python3
"""Sweep harness runner v2 — batch-run across sweep directories.

Finds all (domain, seed, size) directories under the sweep root, runs
the harness, collects results into a single JSON for analysis.

Usage:
    python3 sweep_run.py ../generator/sweep --model claude-opus-4-8
    python3 sweep_run.py ../generator/sweep --sizes 6k,25k --dry-run
    python3 sweep_run.py ../generator/sweep --resume
"""
import argparse, json, os, sys, time
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from run import run_scenario, ARMS


def find_sweep_dirs(root, domains=None, seeds=None, sizes=None):
    dirs = []
    for domain in sorted(os.listdir(root)):
        dpath = os.path.join(root, domain)
        if not os.path.isdir(dpath):
            continue
        if domains and domain not in domains:
            continue
        for sdir in sorted(os.listdir(dpath)):
            spath = os.path.join(dpath, sdir)
            if not os.path.isdir(spath) or not sdir.startswith("s"):
                continue
            seed = sdir[1:]
            if seeds and seed not in seeds:
                continue
            for size in sorted(os.listdir(spath)):
                szpath = os.path.join(spath, size)
                if not os.path.isdir(szpath):
                    continue
                if sizes and size not in sizes:
                    continue
                if size.endswith("-raw"):
                    continue
                fams = [f for f in os.listdir(szpath)
                        if f.startswith("family-") and f.endswith(".json")]
                if fams:
                    dirs.append(dict(path=szpath, domain=domain,
                                     seed=seed, size=size))
    return dirs


def has_results(d, model):
    return any(f.startswith("results-") and model in f
               for f in os.listdir(d["path"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="sweep root directory")
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--arms", default="paste,ceiling",
                    help="comma-separated arm keys")
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--domains", default=None)
    ap.add_argument("--seeds", default=None)
    ap.add_argument("--sizes", default=None)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    arm_keys = [k.strip() for k in a.arms.split(",")]
    domains = a.domains.split(",") if a.domains else None
    seeds = a.seeds.split(",") if a.seeds else None
    sizes = a.sizes.split(",") if a.sizes else None

    root = os.path.abspath(a.root)
    dirs = find_sweep_dirs(root, domains, seeds, sizes)

    if a.resume:
        todo = [d for d in dirs if not has_results(d, a.model)]
        skip = len(dirs) - len(todo)
        if skip:
            print(f"Resuming: {skip} already done, {len(todo)} remaining")
        dirs = todo

    calls = len(dirs) * len(arm_keys) * 2
    print(f"Sweep: {len(dirs)} scenarios × {len(arm_keys)} arms × "
          f"2 queries = {calls} reader calls")
    print(f"  model: {a.model}")
    print(f"  arms:  {arm_keys}")

    if a.dry_run:
        for d in dirs:
            print(f"  {d['domain']}/s{d['seed']}/{d['size']}")
        print(f"\n(dry run — {calls} calls would be made)")
        return

    all_results = []
    t0 = time.time()
    for i, d in enumerate(dirs):
        print(f"\n{'='*60}")
        print(f"[{i+1}/{len(dirs)}] {d['domain']}/s{d['seed']}/{d['size']}")
        print(f"{'='*60}")
        try:
            results = run_scenario(d["path"], a.model, arm_keys, a.concurrency)
            for r in results:
                r["sweep_domain"] = d["domain"]
                r["sweep_seed"] = d["seed"]
                r["sweep_size"] = d["size"]
            all_results.extend(results)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            continue

    elapsed = time.time() - t0
    print(f"\n{'='*60}")
    print(f"SWEEP COMPLETE — {len(all_results)} evaluations in {elapsed:.0f}s")
    print(f"{'='*60}")

    # Aggregate by size × arm
    by_size_arm = defaultdict(list)
    for r in all_results:
        by_size_arm[(r["sweep_size"], r["arm_key"])].append(r)

    size_order = ["6k", "25k", "60k", "150k", "400k"]
    print(f"\n{'size':<6}  {'arm':<22}  {'B-pass':>7}  {'A-mean':>7}  {'n':>4}")
    print(f"{'----':<6}  {'----':<22}  {'------':>7}  {'------':>7}  {'--':>4}")
    for size in size_order:
        for ak in arm_keys:
            rs = by_size_arm.get((size, ak), [])
            if not rs:
                continue
            b_rate = sum(1 for r in rs if r["b_grade"]["pass"]) / len(rs)
            a_mean = sum(r["a_score"] for r in rs) / len(rs)
            arm_name = ARMS[ak][0][:20]
            print(f"{size:<6}  {arm_name:<22}  {b_rate:>7.0%}  "
                  f"{a_mean:>7.0%}  {len(rs):>4}")

    # Escalation gate: paste-everything B ≥ 85%?
    print(f"\nESCALATION GATE:")
    for size in size_order:
        rs = by_size_arm.get((size, "paste"), [])
        if not rs:
            continue
        b_rate = sum(1 for r in rs if r["b_grade"]["pass"]) / len(rs)
        status = "ESCALATE" if b_rate >= 0.85 else "OK"
        print(f"  {size}: paste B-rate = {b_rate:.0%}  [{status}]")

    out_path = a.out or os.path.join(root,
                                      f"sweep-results-{a.model}.json")
    out_data = {
        "meta": {
            "model": a.model,
            "arms": arm_keys,
            "n_scenarios": len(dirs),
            "n_evaluations": len(all_results),
            "elapsed_s": round(elapsed, 1),
        },
        "results": all_results,
    }
    with open(out_path, "w") as f:
        json.dump(out_data, f, indent=2, default=str)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
