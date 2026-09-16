#!/usr/bin/env python3
"""Analyze write-quality-variance trial results.

Loads data/trials.json, groups by variant, reports:
  - mean cost, mean output tokens, pass rate
  - bootstrap 95% CI on cost
  - pairwise comparisons A vs each of B, C, D
  - decision-rule outcomes per the spec

Usage:
    analyze.py
"""

import json
import random
from pathlib import Path
from statistics import mean, stdev

EXP_DIR = Path(__file__).parent.parent
TRIALS_PATH = EXP_DIR / "data" / "trials.json"

PHASE2_COLD_MEAN = 0.41   # n=2: $0.40, $0.42
PHASE2_LEVEL_D_MEAN = 0.27  # n=2: $0.25, $0.29
PHASE2_LEVEL_D_RANGE = (0.22, 0.32)  # ±20% reproduction band


def bootstrap_ci(values, n_resamples=10000, ci=0.95):
    """Return (lower, upper) bootstrap CI on the mean."""
    if not values:
        return (None, None)
    n = len(values)
    means = []
    for _ in range(n_resamples):
        sample = [random.choice(values) for _ in range(n)]
        means.append(mean(sample))
    means.sort()
    lower = means[int((1 - ci) / 2 * n_resamples)]
    upper = means[int((1 + ci) / 2 * n_resamples)]
    return (lower, upper)


def main():
    random.seed(42)

    with open(TRIALS_PATH) as f:
        trials = json.load(f)

    by_variant = {}
    for t in trials:
        v = t.get("variant")
        if v is None:
            continue
        by_variant.setdefault(v, []).append(t)

    print("=" * 72)
    print("Write-Quality Variance — Phase 2 follow-up, single-task pilot")
    print("Task: where_keep_attrs_scalar (xarray-6461)")
    print("=" * 72)

    summary = {}
    for variant in sorted(by_variant.keys()):
        runs = by_variant[variant]
        costs = [r["agent"]["total_cost_usd"] for r in runs]
        out_toks = [r["agent"]["output_tokens"] for r in runs]
        turns = [r["agent"]["num_turns"] for r in runs]
        passes = sum(1 for r in runs if r["evaluation"].get("success") is True)
        n = len(runs)
        cost_lo, cost_hi = bootstrap_ci(costs)
        summary[variant] = {
            "n": n,
            "cost_mean": mean(costs),
            "cost_std": stdev(costs) if n > 1 else 0,
            "cost_ci": (cost_lo, cost_hi),
            "cost_individual": costs,
            "out_tok_mean": mean(out_toks),
            "turns_mean": mean(turns),
            "pass_rate": f"{passes}/{n}",
        }

    fmt = "{:8s}  {:>3s}  {:>8s}  {:>8s}  {:>17s}  {:>10s}  {:>7s}  {:>6s}"
    print(fmt.format("variant", "n", "mean_$", "std_$", "95% CI ($)", "out_tok", "turns", "pass"))
    print("-" * 80)
    for variant in sorted(summary.keys()):
        s = summary[variant]
        ci_str = f"[{s['cost_ci'][0]:.3f},{s['cost_ci'][1]:.3f}]"
        print(fmt.format(
            variant, str(s["n"]),
            f"{s['cost_mean']:.3f}",
            f"{s['cost_std']:.3f}",
            ci_str,
            f"{s['out_tok_mean']:.0f}",
            f"{s['turns_mean']:.1f}",
            s["pass_rate"],
        ))

    print()
    print("Reference baselines (Phase 2 pilot, n=2 each):")
    print(f"  cold:    ${PHASE2_COLD_MEAN:.2f}")
    print(f"  Level D: ${PHASE2_LEVEL_D_MEAN:.2f} (range ${PHASE2_LEVEL_D_RANGE[0]:.2f}-${PHASE2_LEVEL_D_RANGE[1]:.2f})")
    print()

    # Individual costs per variant
    print("Individual trial costs:")
    for variant in sorted(summary.keys()):
        costs = summary[variant]["cost_individual"]
        cost_str = ", ".join(f"${c:.3f}" for c in costs)
        print(f"  {variant}: {cost_str}")
    print()

    # Decision rules
    print("=" * 72)
    print("Pre-registered decision rules")
    print("=" * 72)

    if "A" in summary:
        a_mean = summary["A"]["cost_mean"]
        in_band = PHASE2_LEVEL_D_RANGE[0] <= a_mean <= PHASE2_LEVEL_D_RANGE[1]
        print(f"\n[Rule 1/2] A reproduction check")
        print(f"  A mean: ${a_mean:.3f}")
        print(f"  Phase 2 Level D band: ${PHASE2_LEVEL_D_RANGE[0]:.2f}-${PHASE2_LEVEL_D_RANGE[1]:.2f}")
        print(f"  Result: {'WITHIN band — harness trustworthy' if in_band else 'OUTSIDE band — investigate before drawing conclusions'}")

    if "A" in summary and "D" in summary:
        a_mean = summary["A"]["cost_mean"]
        d_mean = summary["D"]["cost_mean"]
        a_ci = summary["A"]["cost_ci"]
        d_ci = summary["D"]["cost_ci"]
        d_above_cold = d_mean >= PHASE2_COLD_MEAN
        print(f"\n[Rule 3/4] H-QUAL-FLOOR (D vs cold)")
        print(f"  D mean: ${d_mean:.3f}  CI: [${d_ci[0]:.3f}, ${d_ci[1]:.3f}]")
        print(f"  Phase 2 cold: ${PHASE2_COLD_MEAN:.2f}")
        if d_above_cold:
            print(f"  Result: D ≥ cold — H-QUAL-FLOOR SUPPORTED — write-side gate MANDATORY")
        elif d_mean > a_mean and not (a_ci[1] < d_ci[0] or d_ci[1] < a_ci[0]):
            print(f"  Result: D between A and cold (CIs overlap) — write-side gate helpful but not critical")
        elif d_mean > a_mean:
            print(f"  Result: D > A (CIs disjoint) — write-side gate helpful but not critical")
        else:
            print(f"  Result: D ≈ A or D < A — bad sources do NOT degrade utility — write-quality variance is not binding")

    if "A" in summary and "B" in summary and "C" in summary:
        a = summary["A"]
        b = summary["B"]
        c = summary["C"]
        a_ci = a["cost_ci"]
        b_ci = b["cost_ci"]
        c_ci = c["cost_ci"]
        ab_overlap = not (a_ci[1] < b_ci[0] or b_ci[1] < a_ci[0])
        ac_overlap = not (a_ci[1] < c_ci[0] or c_ci[1] < a_ci[0])
        bc_overlap = not (b_ci[1] < c_ci[0] or c_ci[1] < b_ci[0])
        all_overlap = ab_overlap and ac_overlap and bc_overlap
        print(f"\n[Rule 5/6] H-QUAL-FRAMING and H-QUAL-STRUCTURE (A vs B vs C)")
        print(f"  A vs B CIs overlap: {ab_overlap}")
        print(f"  A vs C CIs overlap: {ac_overlap}")
        print(f"  B vs C CIs overlap: {bc_overlap}")
        if all_overlap:
            print(f"  Result: A ≈ B ≈ C — prompt phrasing and structure are SECOND-ORDER. Defer prompt iteration; focus on schema/keys.")
        else:
            print(f"  Result: At least one variant differs — prompt design matters; inspect pairwise.")
            if not ab_overlap:
                direction = "A < B" if a["cost_mean"] < b["cost_mean"] else "A > B"
                print(f"    A vs B: {direction} (briefing vs summary framing matters)")
            if not ac_overlap:
                direction = "A < C" if a["cost_mean"] < c["cost_mean"] else "A > C"
                print(f"    A vs C: {direction} (prose vs slots matters)")

    print()
    print("=" * 72)
    print("Output token comparison (lower = less agent exploration)")
    print("=" * 72)
    for variant in sorted(summary.keys()):
        s = summary[variant]
        print(f"  {variant}: {s['out_tok_mean']:.0f} avg")


if __name__ == "__main__":
    main()
