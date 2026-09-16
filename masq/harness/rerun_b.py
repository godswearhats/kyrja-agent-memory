#!/usr/bin/env python3
"""Re-run the B-query only, with the current B_FORMAT, across the sweep.

A-layer is unchanged and already re-graded for free; this re-spends only on
the decision query to test whether the format-contradiction + scaffold fix
clears the ceiling escalation bias on resolved chains.

Usage:
    python3 rerun_b.py ../generator/sweep-v2 --sizes 6k,25k,60k
"""
import argparse, glob, json, os, sys, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from run import ARMS, B_FORMAT, call_reader, parse_b, grade_b
from sweep_run import find_sweep_dirs


def rerun_one(family, arm_key, corpus_dir, model):
    name, fn = ARMS[arm_key]
    context = fn(family, corpus_dir)
    prompt = family["b_query"] + "\n\n" + B_FORMAT
    raw = call_reader(prompt, context, model)
    parsed = parse_b(raw)
    if parsed.get("action") is None or parsed.get("conflict") is None:
        raw = call_reader(prompt + "\n\n(Your previous answer could not be "
                          "parsed. Use the exact format above.)", context, model)
        parsed = parse_b(raw)
    g = grade_b(parsed, family["ground_truth"])
    return dict(domain=family["meta"]["domain"], arm_key=arm_key,
                b_raw=raw, b_parsed=parsed, b_grade=g,
                conflict_flag_gt=family["ground_truth"]["conflict_flag"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--arms", default="paste,ceiling")
    ap.add_argument("--sizes", default=None)
    ap.add_argument("--concurrency", type=int, default=2)
    a = ap.parse_args()
    arms = [x.strip() for x in a.arms.split(",")]
    sizes = a.sizes.split(",") if a.sizes else None
    root = os.path.abspath(a.root)
    dirs = find_sweep_dirs(root, None, None, sizes)

    jobs = []
    for d in dirs:
        fam = [x for x in os.listdir(d["path"])
               if x.startswith("family-") and x.endswith(".json")][0]
        family = json.load(open(os.path.join(d["path"], fam)))
        for ak in arms:
            jobs.append((family, ak, d))
    print(f"B re-run: {len(jobs)} calls ({len(dirs)} scenarios x {len(arms)} arms)")

    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.concurrency) as ex:
        futs = {ex.submit(rerun_one, fam, ak, d["path"], a.model):
                (d, ak) for fam, ak, d in jobs}
        done = 0
        for fut in as_completed(futs):
            d, ak = futs[fut]
            r = fut.result()
            r.update(size=d["size"], seed=d["seed"])
            results.append(r)
            done += 1
            sym = "PASS" if r["b_grade"]["pass"] else "FAIL"
            if not r["b_grade"]["pass"]:
                print(f"  [{done}/{len(jobs)}] {d['domain']}/s{d['seed']}/"
                      f"{d['size']} {ak}: {sym} ({r['b_grade']['reason']})")
    print(f"\nDone in {time.time()-t0:.0f}s\n")

    # B-pass by size x arm
    bsa = defaultdict(list)
    for r in results:
        bsa[(r["size"], r["arm_key"])].append(r)
    order = ["6k", "25k", "60k", "150k", "400k"]
    print(f"{'size':<6}{'arm':<10}{'B-pass':>8}{'n':>4}")
    print("-" * 28)
    for s in order:
        for ak in arms:
            rs = bsa.get((s, ak), [])
            if not rs:
                continue
            bp = sum(1 for r in rs if r["b_grade"]["pass"]) / len(rs)
            print(f"{s:<6}{ak:<10}{bp:>7.0%}{len(rs):>4}")

    # ceiling gate + resolved-chain split
    cz = [r for r in results if r["arm_key"] == "ceiling"]
    if cz:
        cp = sum(1 for r in cz if r["b_grade"]["pass"]) / len(cz)
        res = [r for r in cz if not r["conflict_flag_gt"]]
        unr = [r for r in cz if r["conflict_flag_gt"]]
        print(f"\nCEILING B-pass overall: {cp:.0%} (n={len(cz)})  "
              f"[gate >=90%]")
        if res:
            print(f"  on RESOLVED chains:   "
                  f"{sum(1 for r in res if r['b_grade']['pass'])/len(res):.0%} "
                  f"(n={len(res)})")
        if unr:
            print(f"  on UNRESOLVED chains: "
                  f"{sum(1 for r in unr if r['b_grade']['pass'])/len(unr):.0%} "
                  f"(n={len(unr)})")

    out = os.path.join(root, f"brerun-{a.model}.json")
    json.dump({"results": results}, open(out, "w"), indent=2, default=str)
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
