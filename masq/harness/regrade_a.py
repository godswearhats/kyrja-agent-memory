#!/usr/bin/env python3
"""Re-grade the A-layer on stored a_raw with the current grading logic.

A_FORMAT and the A-query are unchanged, so stored reader outputs are valid;
this re-scores them for free (no reader calls) to test the value-matching
fix. Reports per-arm A-score, old vs new, split by domain.
"""
import glob, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from run import parse_a, grade_a

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "../generator/sweep-v2")
root = os.path.abspath(root)

agg = defaultdict(lambda: {"old": [], "new": []})  # (domain,arm) -> scores
flips = []
for f in sorted(glob.glob(os.path.join(root, "*/*/*/results-*-claude-opus-4-8.json"))):
    fam_dir = os.path.dirname(f)
    fam = [x for x in os.listdir(fam_dir) if x.startswith("family-") and x.endswith(".json")]
    if not fam:
        continue
    family = json.load(open(os.path.join(fam_dir, fam[0])))
    gt = family["ground_truth"]
    d = json.load(open(f))
    domain = os.path.relpath(f, root).split("/")[0]
    size = os.path.basename(fam_dir)
    for r in d["results"]:
        old = r["a_score"]
        new = grade_a(parse_a(r.get("a_raw", "") or ""), gt)["score"]
        key = (domain, r["arm_key"])
        agg[key]["old"].append(old)
        agg[key]["new"].append(new)
        if abs(new - old) > 0.15:
            flips.append((domain, size, r["arm_key"], old, new))

print(f"Re-graded A on stored outputs under {os.path.relpath(root)}\n")
print(f"{'domain':<13}{'arm':<10}{'A old':>7}{'A new':>7}{'n':>4}")
print("-" * 41)
for (dom, arm) in sorted(agg):
    v = agg[(dom, arm)]
    om = sum(v["old"]) / len(v["old"])
    nm = sum(v["new"]) / len(v["new"])
    print(f"{dom:<13}{arm:<10}{om:>6.0%}{nm:>7.0%}{len(v['old']):>4}")

# overall ceiling
cv = {"old": [], "new": []}
for (dom, arm), v in agg.items():
    if arm == "ceiling":
        cv["old"] += v["old"]; cv["new"] += v["new"]
if cv["old"]:
    print(f"\nCEILING overall A: {sum(cv['old'])/len(cv['old']):.0%} -> "
          f"{sum(cv['new'])/len(cv['new']):.0%}  (n={len(cv['old'])})")
print(f"\nScenarios with |Δ|>15pp: {len(flips)}")
for dom, size, arm, o, n in flips[:20]:
    print(f"  {dom}/{size} {arm}: {o:.0%} -> {n:.0%}")
