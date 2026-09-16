#!/usr/bin/env python3
"""Sibling-bed calibration summary.

Reads per-scenario results under generator/calib/<domain>/s<seed>/K<k>/ and
reports, per bed size K (pooled across domains+seeds, n=6/cell):
  - paste B-pass rate   (primary difficulty signal)
  - paste A-mean        (secondary, continuous, less noisy)
  - ceiling B-pass rate (sanity canary: must be ~100% at every K)
  - empty / rate-limit signatures (contamination check)

Then applies the pre-registered decision rule to pin the bed:
  * paste-B flat & low across K            -> bed not load-bearing, pin small
  * paste-B declines then plateaus         -> pin at the knee
  * paste-B still declining at K=150       -> bed strongly load-bearing
"""
import json, glob, os, re, collections, math

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../generator/calib"))
RL = re.compile(r"rate.?limit|overload|usage limit|429|503|too many requests|"
                r"service unavailable|resets \d", re.I)
PASTE, CEIL = "paste-everything", "perfect-retrieval"


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return ((c-h)/d, (c+h)/d)


def knum(s):
    return int(s.lstrip("K"))


agg = collections.defaultdict(lambda: {"pb": 0, "pn": 0, "pa": [], "cb": 0,
                                       "cn": 0, "empty": 0, "rl": 0})

for f in sorted(glob.glob(f"{ROOT}/*/*/K*/results-*-claude-opus-4-8.json")):
    K = os.path.basename(os.path.dirname(f))
    arms = {r["arm"]: r for r in json.load(open(f))["results"]}
    a = agg[K]
    if PASTE in arms:
        r = arms[PASTE]
        a["pn"] += 1
        a["pb"] += bool(r["b_grade"]["pass"])
        a["pa"].append(r["a_score"])
        raw = str(r.get("a_raw", "")) + str(r.get("b_raw", ""))
        if not raw.strip():
            a["empty"] += 1
        if RL.search(raw):
            a["rl"] += 1
    if CEIL in arms:
        r = arms[CEIL]
        a["cn"] += 1
        a["cb"] += bool(r["b_grade"]["pass"])

order = sorted(agg, key=knum)
print("=== SIBLING-BED CALIBRATION (all ~63k tokens, 5 scopes, 4 near-misses) ===\n")
print(f"{'K':>4}{'n':>4}{'paste B':>14}{'paste A':>10}"
      f"{'ceil B':>9}{'empty':>7}{'rl':>4}")
prev = None
trend = []
for K in order:
    a = agg[K]
    lo, hi = wilson(a["pb"], a["pn"])
    pb = f"{a['pb']}/{a['pn']}={a['pb']/a['pn']:.0%}" if a["pn"] else "-"
    ci = f"[{lo:.0%}-{hi:.0%}]"
    pa = f"{sum(a['pa'])/len(a['pa']):.0%}" if a["pa"] else "-"
    cb = f"{a['cb']}/{a['cn']}={a['cb']/a['cn']:.0%}" if a["cn"] else "-"
    print(f"{K:>4}{a['pn']:>4}{pb:>9}{ci:>11}{pa:>10}{cb:>9}"
          f"{a['empty']:>7}{a['rl']:>4}")
    trend.append((knum(K), a["pb"]/a["pn"] if a["pn"] else None))

# ceiling sanity
bad_ceil = [K for K in order if agg[K]["cn"] and agg[K]["cb"] < agg[K]["cn"]]
print("\n--- sanity ---")
print(f"ceiling 100% at every K: {'YES' if not bad_ceil else 'NO ' + str(bad_ceil)}")
tot_empty = sum(agg[K]["empty"] for K in order)
tot_rl = sum(agg[K]["rl"] for K in order)
print(f"contamination: empty={tot_empty}  rl-sig={tot_rl} "
      f"(rl-sig may be false positives from the rate-limit domain's prose)")

# crude trend read
vals = [v for _, v in trend if v is not None]
if vals:
    lo_k, hi_k = trend[0][1], trend[-1][1]
    print("\n--- trend (paste B, low->high bed) ---")
    print("  " + "  ".join(f"K{k}:{v:.0%}" for k, v in trend))
    if hi_k is not None and lo_k is not None:
        drop = lo_k - hi_k
        print(f"  K10 -> K150 change in paste-B: {drop:+.0%} "
              f"(negative = bigger bed is harder)")
