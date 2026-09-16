#!/usr/bin/env python3
"""Headline world generator — pinned difficulty core, context-length axis.

Locked design (calibration 2026-06-26):
  - PINNED CORE (identical every scenario): 5 scopes, 4 near-misses,
    20-sibling bed (n_collisions=2). ~7k tokens. The sibling-bed calibration
    showed difficulty is FLAT across bed size 10->150, so we pin lean at the
    cheapest safe size (K=20 = 2 collisions, margin over the K=10 floor).
  - SIZE AXIS (vary chatter only): 25k / 60k / 150k / 400k. Same needle,
    progressively deeper haystack. 6k dropped (can't host 5 scopes + bed).

Chatter sizing anchored to the calibration: at the pinned core, n_chatter=588
yielded ~62k, i.e. ~93.5 composed tokens per chatter session over a ~7k core.

Coverage: 3 domains x 5 seeds = 15/size x 4 sizes = 60 worlds.
Output: generator/headline/<domain>/s<seed>/<size>/
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sweep  # reuse tested generate_one (embed -> compose -> verify)

CORE_TOK = 7000        # pinned-core token weight (5 scopes + 4 nm + 20 sib)
TOK_PER_CHAT = 93.5    # composed tokens per chatter session (calibration-anchored)

SIZE_TARGETS = {"25k": 25000, "60k": 60000, "150k": 150000, "400k": 400000}
DAYS = {"25k": 90, "60k": 180, "150k": 365, "400k": 730}

DOMAINS = ["rate-limit", "ownership", "merge-policy"]
SEEDS = [4001, 4002, 4003, 4004, 4005]   # fresh; distinct from sweep-v2 / calib

SIZES = {}
for key, target in SIZE_TARGETS.items():
    n_chatter = max(40, round((target - CORE_TOK) / TOK_PER_CHAT))
    SIZES[key] = dict(
        n_siblings=20, n_chatter=n_chatter, n_collisions=2,
        n_scopes=5, n_near_misses=4, days=DAYS[key],
    )

sweep.SIZES = SIZES
OUT = os.path.join(HERE, "headline")


def main():
    only = sys.argv[1:] or list(SIZE_TARGETS)   # optional size filter for smoke tests
    print("=== headline generator: pinned core, size axis ===")
    print(f"{'size':<6}{'target':>8}{'n_chat':>8}{'n_sib':>6}"
          f"{'n_coll':>7}{'scopes':>7}{'nm':>4}{'days':>6}")
    for k in SIZE_TARGETS:
        c = SIZES[k]
        print(f"{k:<6}{SIZE_TARGETS[k]:>8}{c['n_chatter']:>8}{c['n_siblings']:>6}"
              f"{c['n_collisions']:>7}{c['n_scopes']:>7}{c['n_near_misses']:>4}"
              f"{c['days']:>6}")
    sizes = [s for s in SIZE_TARGETS if s in only]
    total = len(DOMAINS) * len(SEEDS) * len(sizes)
    print(f"\n{total} worlds -> {OUT}\n")

    done = 0
    for domain in DOMAINS:
        for seed in SEEDS:
            for size in sizes:
                ok = sweep.generate_one(domain, seed, size, OUT)
                done += ok
                if not ok:
                    print(f"\nABORTED at {domain}/s{seed}/{size}")
                    sys.exit(1)
    print(f"\nHeadline generation complete: {done}/{total} worlds.")


if __name__ == "__main__":
    main()
