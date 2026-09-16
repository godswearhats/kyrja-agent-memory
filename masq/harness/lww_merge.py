#!/usr/bin/env python3
"""Merge lww results back into per-scenario files and summarise.

After `sweep_run.py --arms lww` overwrites each results-*.json with ONLY the
lww arm, this restores paste+ceiling from the .pc.bak snapshot and merges the
three arms into one file. Then prints lww B-pass and A-mean by size, plus a
contamination check (lww has no ceiling canary, so we look for empty raw
outputs / rate-limit signatures recorded in the results).
"""
import json, glob, os, re, collections

ROOT = os.path.join(os.path.dirname(__file__), "../generator/sweep-v2")
ROOT = os.path.abspath(ROOT)
RL = re.compile(r"rate.?limit|overload|session limit|usage limit|429|503|"
                r"too many requests|resets \d", re.I)

def size_of(path):
    return os.path.basename(os.path.dirname(path))

by_size = collections.defaultdict(lambda: {"b_pass":0,"b_n":0,"a_sum":0.0,
                                           "a_n":0,"empty":0,"rl":0,"merged":0})

for f in sorted(glob.glob(f"{ROOT}/*/*/*/results-*-claude-opus-4-8.json")):
    bak = f + ".pc.bak"
    cur = json.load(open(f))
    cur_arms = {r["arm"]: r for r in cur["results"]}
    lww = cur_arms.get("last-write-wins")
    if lww is None:
        # not yet run for this scenario; skip
        continue
    s = size_of(f)
    # restore paste+ceiling from backup, add lww
    merged = {}
    if os.path.exists(bak):
        for r in json.load(open(bak))["results"]:
            merged[r["arm"]] = r
    merged["last-write-wins"] = lww
    cur["results"] = list(merged.values())
    json.dump(cur, open(f, "w"), indent=2, default=str)
    by_size[s]["merged"] += 1
    # summarise lww
    rec = by_size[s]
    rec["b_n"] += 1
    if lww["b_grade"]["pass"]:
        rec["b_pass"] += 1
    rec["a_sum"] += lww["a_score"]; rec["a_n"] += 1
    raw = (str(lww.get("a_raw","")) + str(lww.get("b_raw","")))
    if not raw.strip():
        rec["empty"] += 1
    if RL.search(raw):
        rec["rl"] += 1

order = ["6k","25k","60k","150k","400k"]
print("=== LWW MERGE + SUMMARY ===")
print(f"{'size':<6}{'merged':>7}{'lww B-pass':>13}{'lww A-mean':>12}"
      f"{'empty':>7}{'rl-sig':>8}")
tot_bp=tot_bn=0
for s in order:
    if s not in by_size: continue
    r = by_size[s]
    tot_bp += r["b_pass"]; tot_bn += r["b_n"]
    bp = f"{r['b_pass']}/{r['b_n']}"
    am = f"{r['a_sum']/r['a_n']:.0%}" if r["a_n"] else "-"
    print(f"{s:<6}{r['merged']:>7}{bp:>13}{am:>12}{r['empty']:>7}{r['rl']:>8}")
print(f"\npooled lww B: {tot_bp}/{tot_bn} = {tot_bp/tot_bn:.0%}" if tot_bn else "no data")
print("\nReference (clean): ceiling B 60/60=100%  |  paste B 23/60=38%")
print("Expectation: lww should land BETWEEN. empty/rl-sig must be ~0 (clean).")
