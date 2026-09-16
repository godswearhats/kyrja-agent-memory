#!/usr/bin/env python3
"""Sibling-bed calibration generator.

Question: how big a sibling confusability bed is needed to hold the
scope-disambiguation task at full difficulty? That size pins the fixed
difficulty core and thus the floor of the v2 size axis.

Design (isolate bed from haystack volume):
  - HOLD CONSTANT: 5 scopes, 4 near-misses, total corpus ~60k tokens.
  - VARY: sibling bed K in {0,20,40,80,150}, back-filling chatter so the
    total stays ~60k. A bigger bed REPLACES haystack rather than adding
    size, so any difficulty change is the bed's doing, not corpus growth.

Held-constant total is anchored to the real 60k world (n_chatter=520 at
n_siblings=60 ~= 60k tokens). One sibling ~= 1.7 chatter sessions in token
terms (measured: 259 sibling sessions for 150 siblings, ~uniform session
size), so we trade 1.7 chatter sessions per sibling to hold size flat.
Collisions are drawn from the sibling pool (embedding.py:194), so we scale
n_collisions ~= 10% of K to preserve the existing worlds' bed composition.

Output: generator/calib/<domain>/s<seed>/K<k>/
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep  # reuse the tested generate_one (embed -> compose -> verify)

ANCHOR_CHAT = 520      # n_chatter that yields ~60k at the anchor bed size
ANCHOR_K = 60          # anchor sibling count (the real 60k world)
SIB_TO_CHAT = 1.7      # measured chatter-sessions per sibling (token-equiv)

# K=0 (no bed) and K=5 (n_collisions rounds to 0) FAIL verify by construction:
# invariants I2/I3/I8 require >=1 collision and the param recurring in noise.
# So the generator enforces a minimum confusability bed; K=10 is the floor.
BED_SIZES = [10, 20, 40, 80, 150]
DOMAINS = ["rate-limit", "ownership", "merge-policy"]
SEEDS = [3001, 3002]   # fresh seeds, distinct from sweep-v2 (2001-2004)

CALIB = {}
for K in BED_SIZES:
    n_chatter = ANCHOR_CHAT + round(SIB_TO_CHAT * (ANCHOR_K - K))
    n_collisions = round(0.10 * K)
    CALIB[f"K{K}"] = dict(
        n_siblings=K, n_chatter=n_chatter, n_collisions=n_collisions,
        n_scopes=5, n_near_misses=4, days=180,
    )

# swap the size table so generate_one reads our per-bed config
sweep.SIZES = CALIB

OUT = os.path.join(HERE, "calib")


def main():
    print("=== sibling-bed calibration: planned configs ===")
    print(f"{'key':<6}{'n_sib':>6}{'n_chat':>8}{'n_coll':>7}"
          f"{'scopes':>7}{'nm':>4}")
    for K in BED_SIZES:
        c = CALIB[f"K{K}"]
        print(f"{'K'+str(K):<6}{c['n_siblings']:>6}{c['n_chatter']:>8}"
              f"{c['n_collisions']:>7}{c['n_scopes']:>7}{c['n_near_misses']:>4}")
    total = len(DOMAINS) * len(SEEDS) * len(BED_SIZES)
    print(f"\n{total} worlds -> {OUT}\n")

    done = failed = 0
    for domain in DOMAINS:
        for seed in SEEDS:
            for K in BED_SIZES:
                ok = sweep.generate_one(domain, seed, f"K{K}", OUT)
                done += ok
                failed += (not ok)
                if not ok:
                    print(f"\nABORTED at {domain}/s{seed}/K{K}")
                    sys.exit(1)
    print(f"\nCalibration generation complete: {done}/{total} worlds.")


if __name__ == "__main__":
    main()
