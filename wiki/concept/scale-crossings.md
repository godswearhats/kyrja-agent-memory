---
type: concept
name: Scale Crossings
status: timeless
last_ingested: 2026-05-12
sources: [../source/weller-2025-limit.md]
epistemic_tags: [measured, asserted]
tags: [scale-thesis, volume-leg, tornado-sensitivity]
---

## Definition

**Scale crossings** are the dates at which a modelled agentic-memory deployment exceeds each of six architectural-wall thresholds, under the [scale model](../../../research/scale-model/THESIS.md)'s stock-and-flow ODE. The headline finding: **all six bracketing scenarios cross the LIMIT-1536d ceiling inside the 5-year planning horizon**, with the most conservative case crossing at year 1.46 and the most aggressive at year 0.01.

This concept exists because the headline finding is referenced widely across the wiki and is the volume leg of the scale thesis. Defining it once, here, lets other pages cite the result without re-stating the table.

## The thresholds

| Threshold | Vectors | Source |
|---|---|---|
| LIMIT-1536d ceiling | ~13M (interpolated, bracket 8M–20M) | [Weller 2025 LIMIT](../source/weller-2025-limit.md) — d=1536 not a paper datapoint |
| HNSW recall degradation | 10M | HNSW behaviour under continuous writes `[ASSERTED]` |
| HNSW memory non-trivial | 50M | ~400 GB at 1536d `[ASSERTED]` |
| HNSW uneconomical | 100M | Cost analysis without quantization `[ASSERTED]` |
| LIMIT-4096d ceiling | 250M | [Weller 2025 LIMIT](../source/weller-2025-limit.md) — paper-empirical at d=4096 |
| Architectural rebuild forced | 1B | Industry case studies `[ASSERTED]` |

**Construct-validity caveat for [MEASURED] outputs below:** the thresholds are *flattened proxies* for the [cascading-failures product](./cascading-failures.md). Crossing a threshold does not imply effective recall collapse; it means one of several mechanisms enters the regime where it could materially contribute. "Y5 vectors" and "year-of-crossing" are scale-model outputs (model-internal measurements with documented parameters); they are not field-measured recall values.

## The crossings (audit-corrected centrals, 2026-04-30)

| Scenario | Y5 vectors | Peak QPS | Walls crossed | LIMIT-1536d crossed at |
|---|---|---|---|---|
| A: SWE-200 conservative | 55M | 33 | 3 | y1.46 |
| B: SWE-200 moderate | 166M | 108 | 4 | y0.60 |
| C: SWE-200 aggressive | 997M | 551 | 5 | y0.11 |
| D: Enterprise-5000 conservative | 65M | 49 | 3 | y1.75 |
| E: Enterprise-5000 aggressive | 2.7B | 1,719 | 6 | y0.06 |
| F: Frontier-1000 (2030) | 8.5B | 4,032 | 6 | y0.01 |

`[MEASURED]` from the scale model under audit-corrected centrals. *Construct-validity:* outputs are deterministic functions of the parameter set; the empirical strength of the claim is the strength of the parameter calibration, not the model itself.

## Top-4 tornado drivers

Sensitivity analysis on Scenario B identifies the same top-4 drivers for both volume and throughput `[MEASURED]`:

1. `orchestration_depth`
2. `memories_per_session` (F5)
3. `sessions_per_user_day`
4. `tool_chain_amplifier`

**All four are per-session multipliers.** "How heavy each user gets" dominates over "how many users adopt." Adoption-rate uncertainty (F6, F7) sits at the bottom of the tornado because logistic saturation flattens the swing within 5 years.

*Construct-validity for the ranking:* sensitivity is measured by ±50% variation around the scenario-central, not by parameter-bound variation (which collapses to zero when a scenario overrides a parameter at its bound — a known cosmetic bug in the tornado plot). The top-4 ranking is robust under either method; the magnitude bars are not.

## Why this matters

- **Volume leg of the scale thesis is supported.** Every bracketing scenario, including the conservative ones, enters LIMIT-territory inside ordinary enterprise planning horizons. The thesis-binding claim that "incumbents hit walls inside customer planning horizons" rests on this leg.
- **Per-session-multiplier dominance shapes the wedge.** Because the top-4 drivers are all about how each user behaves (not how many users adopt), the wedge product can be load-bearing on volume even with slow adoption. This licenses the [tool-chain wedge as adoption path](../decision/repo-bounded-scope.md) — single-user data still matters.
- **Calibration gap is concentrated in F5.** F5 is the only top-4 driver with **no production-data anchor**; the central was nudged 9 → 12 in audit on the strength of EMem (a synthetic benchmark). The volume leg's biggest residual uncertainty lives in this one parameter. See [f5-production-data](../open-question/f5-production-data.md).
- **Threshold-as-proxy framing matters for honest reading.** A crossing is necessary but not sufficient for the recall collapse predicted by cascading-failures. Pairing this concept with [cascading-failures](./cascading-failures.md) and [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md) is how the volume and recall legs interlock.

## Scope limits

- **No query-type axis.** The model treats all stored stock as if every query draws from the LIMIT-bound combinatorial regime. Natural-language-dominated workloads (Glean-shape Q&A) likely never bite this leg; reasoning/instruction-following workloads are the exposed regime. Per [Weller 2025 LIMIT](../source/weller-2025-limit.md) Theorem 1, the bound is on *representability* of compositional queries, not smooth recall. See [query-type-axis](../open-question/query-type-axis.md) — flagged as the next structural change to the scale model.
- **F12 retention not wired.** Regulated-enterprise scenarios (HIPAA/SOX/EU AI Act-bound) are currently optimistic — see [f12-retention-wiring](../open-question/f12-retention-wiring.md). Direction of the bug: crossings should arrive *sooner* in regulated scenarios than currently shown.
- **F2 bimodality is n=1.** Anchored on a single user's data; not yet replicated.
- **The crossing date is not a forecast.** "Year T" is the date by which one bracketing scenario reaches the threshold; not a prediction that any specific customer reaches it on that date.

## Related

- [cascading-failures](./cascading-failures.md) — the recall-leg framing this concept pairs with.
- [Weller 2025 LIMIT](../source/weller-2025-limit.md) — anchors the LIMIT-1536d and LIMIT-4096d thresholds.
- [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md) — the highest-priority gap in the recall leg.
- [f5-production-data](../open-question/f5-production-data.md) — the largest unanchored top-4 driver.
- [f12-retention-wiring](../open-question/f12-retention-wiring.md) — known model bug; regulated-scenario direction-of-error.
- [BIG-PICTURE (2026-05-14 archive)](../archive/BIG-PICTURE-2026-05-14.md) — three-legs-of-evidence summary cites this concept for the volume leg.

## Source archive

Concept synthesized from [scale-model THESIS.md](../../../research/scale-model/THESIS.md) §"Volume leg — what the scale model shows" and §"Audit summary". Audit-corrected centrals dated 2026-04-30 (Nils/indigo with three parallel sub-agent passes on F1/F5/F8 and F2/F4).
