#!/usr/bin/env python3
"""Bootstrap significance analysis for ceiling effect experiment."""

import json
import os
import sys

import numpy as np

SCRIPT_DIR = os.path.dirname(__file__)
DEFAULT_RESULTS = os.path.join(SCRIPT_DIR, "ceiling_results_full.json")
RESULTS_PATH = DEFAULT_RESULTS if os.path.exists(DEFAULT_RESULTS) else os.path.join(SCRIPT_DIR, "ceiling_results.json")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "ceiling_analysis_full.json") if os.path.exists(DEFAULT_RESULTS) else os.path.join(SCRIPT_DIR, "ceiling_analysis.json")
N_BOOTSTRAP = 10_000
SEED = 42


def bootstrap_ci(values, n_boot=N_BOOTSTRAP, ci=0.95):
    rng = np.random.RandomState(SEED)
    vals = np.array(values)
    means = np.array([rng.choice(vals, size=len(vals), replace=True).mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return {
        "mean": round(float(vals.mean()), 4),
        "ci_low": round(float(np.percentile(means, 100 * alpha)), 4),
        "ci_high": round(float(np.percentile(means, 100 * (1 - alpha))), 4),
        "std": round(float(vals.std()), 4),
    }


def pairwise_test(vals_a, vals_b, n_boot=N_BOOTSTRAP):
    """P(A > B) via paired bootstrap."""
    rng = np.random.RandomState(SEED)
    a, b = np.array(vals_a), np.array(vals_b)
    n = len(a)
    a_wins = 0
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        if a[idx].mean() > b[idx].mean():
            a_wins += 1
    return {
        "mean_diff": round(float(a.mean() - b.mean()), 4),
        "p_a_better": round(a_wins / n_boot, 4),
    }


def main():
    with open(RESULTS_PATH) as f:
        data = json.load(f)

    results = data["results"]
    tiers = ["T0_no_memory", "T1_bm25", "T2_semantic", "T3_hybrid"]

    # Group F1 scores by tier, preserving query order
    tier_f1s = {}
    for tier in tiers:
        tier_f1s[tier] = [r["f1"] for r in results if r["tier"] == tier]

    # Bootstrap CIs
    print("Bootstrap confidence intervals (95%, n=10,000):", file=sys.stderr)
    ci_results = {}
    for tier in tiers:
        ci = bootstrap_ci(tier_f1s[tier])
        ci_results[tier] = ci
        print(f"  {tier:15s}  mean={ci['mean']:.4f}  [{ci['ci_low']:.4f}, {ci['ci_high']:.4f}]", file=sys.stderr)

    # Pairwise comparisons (each tier vs every other)
    print("\nPairwise significance tests:", file=sys.stderr)
    pairwise = {}
    for i, tier_a in enumerate(tiers):
        for tier_b in tiers[i+1:]:
            key = f"{tier_b}_vs_{tier_a}"
            test = pairwise_test(tier_f1s[tier_b], tier_f1s[tier_a])
            pairwise[key] = test
            direction = ">" if test["mean_diff"] > 0 else "<"
            print(
                f"  {tier_b} vs {tier_a}: diff={test['mean_diff']:+.4f}  "
                f"P({tier_b.split('_')[0]} better)={test['p_a_better']:.3f}",
                file=sys.stderr,
            )

    # Adjacent tier improvements (the monotonic trend we're looking for)
    print("\nAdjacent tier improvements:", file=sys.stderr)
    for i in range(len(tiers) - 1):
        key = f"{tiers[i+1]}_vs_{tiers[i]}"
        if key in pairwise:
            test = pairwise[key]
            print(f"  {tiers[i]} → {tiers[i+1]}: {test['mean_diff']:+.4f} (p={test['p_a_better']:.3f})", file=sys.stderr)

    output = {
        "confidence_intervals": ci_results,
        "pairwise_tests": pairwise,
        "n_bootstrap": N_BOOTSTRAP,
        "n_queries": len(tier_f1s[tiers[0]]),
    }
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote analysis to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
