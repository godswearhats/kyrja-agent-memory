#!/usr/bin/env python3
"""Analyze Exp 2 (C-replication on Task 3) results.

Loads exp2/data/trials.json, groups by variant {cold, A, C}, reports:
  - mean cost, mean output tokens, pass rate
  - bootstrap 95% CI on cost
  - pairwise CI overlap (A vs C, A vs cold, C vs cold)
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

# Exp 1 reference numbers for context (where_keep_attrs_scalar)
EXP1_COLD_MEAN = 0.295   # n=4 bootstrap mean
EXP1_A_MEAN = 0.247      # n=4 (Opus 4.7-distilled)
EXP1_C_MEAN = 0.142      # n=4 (Opus 4.7-distilled)

# Halt rule thresholds (from spec.md)
COLD_LOW = 0.15
COLD_HIGH = 0.50


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


def ci_overlap(ci1, ci2):
    return not (ci1[1] < ci2[0] or ci2[1] < ci1[0])


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

    print("=" * 76)
    print("Exp 2 — C-Replication on Task 3 (where_keep_attrs_coord, pydata__xarray-7229)")
    print("Source: Task 2 transcript | Distiller: Opus 4.6 | Agent: Opus 4.6")
    print("=" * 76)

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
            "passes": passes,
            "pass_rate": f"{passes}/{n}",
        }

    fmt = "{:8s}  {:>3s}  {:>8s}  {:>8s}  {:>17s}  {:>10s}  {:>7s}  {:>6s}"
    print(fmt.format("variant", "n", "mean_$", "std_$", "95% CI ($)", "out_tok", "turns", "pass"))
    print("-" * 80)
    order = ["cold", "A", "C"]
    for variant in [v for v in order if v in summary]:
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
    print("Exp 1 reference (where_keep_attrs_scalar, n=4 each):")
    print(f"  cold:  ${EXP1_COLD_MEAN:.3f}")
    print(f"  A:     ${EXP1_A_MEAN:.3f}")
    print(f"  C:     ${EXP1_C_MEAN:.3f}")
    print()

    print("Individual trial costs:")
    for variant in [v for v in order if v in summary]:
        costs = summary[variant]["cost_individual"]
        cost_str = ", ".join(f"${c:.3f}" for c in costs)
        print(f"  {variant}: {cost_str}")
    print()

    print("=" * 76)
    print("Pre-registered decision rules (spec.md)")
    print("=" * 76)

    if "cold" in summary:
        cold = summary["cold"]
        cold_mean = cold["cost_mean"]
        cold_pass = cold["passes"]
        cold_n = cold["n"]
        print(f"\n[Halt rule 5] Cold baseline cost band")
        print(f"  Cold mean: ${cold_mean:.3f}")
        print(f"  Expected band: ${COLD_LOW:.2f}–${COLD_HIGH:.2f}")
        if cold_mean < COLD_LOW or cold_mean > COLD_HIGH:
            print(f"  HALT: Task 3 baseline outside expected band; effect sizes incomparable to Task 2")
        else:
            print(f"  OK: within band, proceed with interpretation")
        print(f"\n[Halt rule 6] Cold pass rate")
        print(f"  Pass rate: {cold_pass}/{cold_n}")
        if cold_pass < 3:
            print(f"  HALT: <3/4 cold passes — task too hard or noisy for clean cost comparison")
        else:
            print(f"  OK: cold pass rate sufficient")

    if "A" in summary and "C" in summary and "cold" in summary:
        a = summary["A"]
        c = summary["C"]
        cold = summary["cold"]
        a_ci = a["cost_ci"]
        c_ci = c["cost_ci"]
        cold_ci = cold["cost_ci"]

        ac_overlap = ci_overlap(a_ci, c_ci)
        a_cold_overlap = ci_overlap(a_ci, cold_ci)
        c_cold_overlap = ci_overlap(c_ci, cold_ci)

        print(f"\n[Co-primary 1] Pass rate (memory effect on hard-task solvability)")
        print(f"  cold: {cold['pass_rate']}")
        print(f"  A:    {a['pass_rate']}")
        print(f"  C:    {c['pass_rate']}")
        if cold['passes'] <= 1 and (a['passes'] >= 3 or c['passes'] >= 3):
            print(f"  Result: STRONG pass-rate effect — memory enables solvability on this hard task.")
        elif a['passes'] > cold['passes'] or c['passes'] > cold['passes']:
            print(f"  Result: Pass-rate trends up with memory (cold {cold['pass_rate']} → A {a['pass_rate']}, C {c['pass_rate']}).")
        else:
            print(f"  Result: No pass-rate effect from memory.")

        # Cost on passing runs only (cold has so few passes that mean-on-all is misleading)
        print(f"\n[Co-primary 2] Cost on passing runs only")
        for variant in ["cold", "A", "C"]:
            runs = by_variant.get(variant, [])
            pass_costs = [r["agent"]["total_cost_usd"] for r in runs if r["evaluation"].get("success") is True]
            if pass_costs:
                m = mean(pass_costs)
                lo, hi = bootstrap_ci(pass_costs) if len(pass_costs) >= 2 else (m, m)
                print(f"  {variant}: ${m:.3f}  CI [${lo:.3f}, ${hi:.3f}]  (n_pass={len(pass_costs)})")
            else:
                print(f"  {variant}: no passing runs")

        print(f"\n[Co-primary 3] H-REPLICATE on cost (C < A < cold, disjoint CIs)")
        print(f"  C  CI: [${c_ci[0]:.3f}, ${c_ci[1]:.3f}]  mean ${c['cost_mean']:.3f}")
        print(f"  A  CI: [${a_ci[0]:.3f}, ${a_ci[1]:.3f}]  mean ${a['cost_mean']:.3f}")
        print(f"  cold CI: [${cold_ci[0]:.3f}, ${cold_ci[1]:.3f}]  mean ${cold['cost_mean']:.3f}")
        print(f"  A vs C overlap: {ac_overlap}")
        print(f"  A vs cold overlap: {a_cold_overlap}")
        print(f"  C vs cold overlap: {c_cold_overlap}")

        c_below_a = c["cost_mean"] < a["cost_mean"]
        a_below_cold = a["cost_mean"] < cold["cost_mean"]
        c_below_cold = c["cost_mean"] < cold["cost_mean"]

        if c_below_a and a_below_cold and not ac_overlap and not a_cold_overlap:
            print(f"  Result: H-REPLICATE SUPPORTED — slot format wins on Task 3 too. Architectural.")
        elif (c_below_a and c_below_cold and a_below_cold and not c_cold_overlap and ac_overlap):
            print(f"  Result: H-FORMAT-TASK-SPECIFIC — memory helps (both A and C < cold), but A vs C overlaps. Slot win is Task-2-specific.")
        elif not c_cold_overlap and not a_cold_overlap and not ac_overlap and c["cost_mean"] > a["cost_mean"]:
            print(f"  Result: STRUCTURE HURTS on Task 3 — surprising direction. Halt and diagnose.")
        elif a_cold_overlap and c_cold_overlap:
            print(f"  Result: H-MEMORY-NO-TRANSFER — Task 2 memory doesn't help Task 3. Relevance ceiling.")
        else:
            print(f"  Result: Mixed signal. See pairwise overlaps above and interpret manually.")

    print()
    print("=" * 76)
    print("Cost reduction vs cold (point estimates)")
    print("=" * 76)
    if "cold" in summary:
        cold_mean = summary["cold"]["cost_mean"]
        for variant in ["A", "C"]:
            if variant in summary:
                v_mean = summary[variant]["cost_mean"]
                pct = (v_mean - cold_mean) / cold_mean * 100
                sign = "−" if pct < 0 else "+"
                print(f"  {variant} vs cold: {sign}{abs(pct):.1f}%  (${v_mean:.3f} vs ${cold_mean:.3f})")

    print()
    print("Output token comparison:")
    for variant in [v for v in order if v in summary]:
        s = summary[variant]
        print(f"  {variant}: {s['out_tok_mean']:.0f} avg, {s['turns_mean']:.1f} turns avg")


if __name__ == "__main__":
    main()
