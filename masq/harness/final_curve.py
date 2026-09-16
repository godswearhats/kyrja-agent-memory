#!/usr/bin/env python3
"""Assemble the full 5-point degradation curve from the cleaned harness.

A (all sizes): re-graded from stored a_raw (A_FORMAT unchanged, fix-1 grading).
B cheap sizes (6k/25k/60k): from brerun JSON (fixed B_FORMAT).
B big sizes (150k/400k): from per-scenario results-*.json (fixed harness).
"""
import glob, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from run import parse_a, grade_a

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                       else os.path.join(HERE, "../generator/sweep-v2"))
CHEAP = {"6k", "25k", "60k"}

# --- A: re-grade all stored results ---
A = defaultdict(list)   # (size, arm) -> [score]
for f in glob.glob(os.path.join(root, "*/*/*/results-*.json")):
    fam_dir = os.path.dirname(f)
    fam = [x for x in os.listdir(fam_dir)
           if x.startswith("family-") and x.endswith(".json")]
    if not fam:
        continue
    gt = json.load(open(os.path.join(fam_dir, fam[0])))["ground_truth"]
    size = os.path.basename(fam_dir)
    for r in json.load(open(f))["results"]:
        s = grade_a(parse_a(r.get("a_raw", "") or ""), gt)["score"]
        A[(size, r["arm_key"])].append(s)

# --- B cheap: from brerun ---
B = defaultdict(list)   # (size, arm) -> [pass(bool)]
brer = os.path.join(root, "brerun-claude-opus-4-8.json")
if os.path.exists(brer):
    for r in json.load(open(brer))["results"]:
        if r["size"] in CHEAP:
            B[(r["size"], r["arm_key"])].append(r["b_grade"]["pass"])

# --- B big: from results files ---
for f in glob.glob(os.path.join(root, "*/*/*/results-*.json")):
    size = os.path.basename(os.path.dirname(f))
    if size in CHEAP:
        continue
    for r in json.load(open(f))["results"]:
        B[(size, r["arm_key"])].append(r["b_grade"]["pass"])

order = ["6k", "25k", "60k", "150k", "400k"]
def pct(xs):
    return f"{100*sum(xs)/len(xs):.0f}%" if xs else "  -"

print("MASQ v2 — full degradation curve (cleaned harness, opus-4-8)\n")
print(f"{'size':<7}{'paste A':>9}{'ceil A':>8}{'paste B':>9}{'ceil B':>8}{'n/arm':>7}")
print("-" * 48)
for s in order:
    pa, ca = A.get((s, "paste"), []), A.get((s, "ceiling"), [])
    pb, cb = B.get((s, "paste"), []), B.get((s, "ceiling"), [])
    n = len(pb) or len(pa)
    print(f"{s:<7}{pct(pa):>9}{pct(ca):>8}{pct(pb):>9}{pct(cb):>8}{n:>7}")

# headline: paste B (= % scenarios solved) and ceiling sanity across sizes
allcb = [x for s in order for x in B.get((s, "ceiling"), [])]
allca = [x for s in order for x in A.get((s, "ceiling"), [])]
print("\nSANITY (must hold all sizes): ceiling B "
      f"{pct(allcb)}  ceiling A {pct(allca)}  [gate >=90%]")
print("HEADLINE: paste-everything B-pass (= scenarios solved) by size above.")
