---
type: open-question
name: F2 orchestration-depth bimodality is n=1
status: OPEN
last_ingested: 2026-05-13
sources: [../experiment/2026-04-30-aj-session-audit/README.md]
epistemic_tags: [measured]
tags: [scale-model, F2, replication, pre-registration]
---

## The question

The scale-model parameter F2 (orchestration depth — average sub-tasks per top-level session) was audit-corrected on 2026-04-30 against empirical data from **1,964 sessions over 44 active days from a single user (AJ)**. The audit found a bimodal distribution by work type and re-anchored SWE scenarios to F2 ∈ {8, 10, 12}. See [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md).

**The audit's n=1 is its weakness.** Pre-registration discipline says: confirm bimodality with a second user before treating it as established. Until then, F2 is empirically anchored to *one engineer's working pattern*, not a general property of agent workloads.

## Why it matters

- **F2 is a top-4 sensitivity driver** in the scale model. A wrong central propagates into all six [scale-crossings](../concept/scale-crossings.md) scenarios.
- **Bimodality is a structural claim.** If the bimodal distribution is real (work-type-dependent: short sessions on bug-fixes, long sessions on feature work), F2 needs to be a *distribution*, not a scalar. If the bimodality is an AJ-specific artifact, the audit's single-central is the safer choice.
- **The honest read is the audit strengthened the model** by replacing a literature estimate with measured data — but a generalization claim from n=1 has known weakness, and the scale model rests on it.

## What evidence would resolve it

- **A second-user F2 measurement.** Another engineer's session data, broken out by work type, run through the same audit methodology. Bimodality replicates → claim survives. Bimodality doesn't replicate → revert to a single distribution or flag as user-dependent.
- **A team-wide F2 measurement.** Aggregated session telemetry across multiple engineers (10+) would substantially close this gap. Currently no such data is collected.
- **Synthetic-task validation.** Run a fixed task set against multiple engineers and measure F2 distribution. Controls for task-mix-confound that single-user data can't.

## What would close this

Promotion to a hypothesis (`H-F2-BIMODALITY`) with falsifiable form, conditional on a second-user data source. Until then, the F2 central in the audit-corrected scale model is `[MEASURED]` for AJ specifically and `[SPECULATED]` as a general property. *Construct-validity:* the AJ measurement operationalizes "orchestration depth" as the count of distinct sub-task invocations per top-level Claude Code conversation under AJ's own work-type categorization rules (see [session-audit experiment](../experiment/2026-04-30-aj-session-audit/README.md)); the n=1 caveat is intrinsic and the generalization claim is exactly what this open question disputes.

## Related

- [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md) — where the n=1 audit lives
- [scale-crossings](../concept/scale-crossings.md) — propagates F2 into Y5 vector counts and QPS projections
- [f5-production-data](./f5-production-data.md) — adjacent scale-model parameter gap
- [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) — the MTP can collect F2 data as a side-product
- THESIS.md Q3 origin: [scale-model/THESIS.md](../../../research/scale-model/THESIS.md)
