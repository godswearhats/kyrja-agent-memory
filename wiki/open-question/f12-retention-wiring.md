---
type: open-question
name: F12 — retention floor wired into simulate()
status: OPEN
last_ingested: 2026-05-13
sources: [../source/compliance-retention-regimes.md]
epistemic_tags: [asserted]
tags: [scale-model, model-bug, regulated-enterprise]
---

## The question

The scale model defines `retention_floor_years` (F12) but **does not wire it into `simulate()`**. Compliance retention regimes (HIPAA ~6 yr, SOX ~7 yr, EU AI Act 6 mo – 10 yr `[ASSERTED]` — see [compliance-retention-regimes](../source/compliance-retention-regimes.md)) should bound the consolidation rate from below — a regulated tenant cannot forget memory faster than its retention floor. Currently the model lets consolidation run unconstrained regardless of regime.

## Why it matters

- **Regulated-enterprise scenarios are not honest** until F12 is wired. Healthcare, finance, and EU AI Act-bound deployments are the most commercially load-bearing scale segments per Eira's commercial framing ([coral](coral "pending")); claiming scale projections for them while ignoring the retention floor overstates how aggressively consolidation can reduce volume.
- **Direction of the bug is known.** Adding F12 can only *raise* projected memory volume in regulated scenarios (consolidation gets a floor, not a ceiling). So the current model is **optimistic** for regulated tenants — wall-crossings in regulated scenarios should arrive sooner than currently shown, not later.
- **Magnitude unknown.** Whether the correction matters at the year-scale resolution of the model depends on the gap between the natural consolidation rate and the retention floor. If retention floor << natural consolidation, the wiring is a no-op in those scenarios. If retention floor >> natural consolidation, the wiring becomes the binding constraint and scenarios change qualitatively.

## What evidence would resolve it

1. **Wire F12 into `simulate()` and re-run.** Cheap. The F12 parameter, regime values, and scenarios already exist. Implementation is a clamp on the consolidation term per scenario's compliance regime.
2. **Compare delta against tornado sensitivities.** If post-wiring F12 enters the top sensitivity drivers, it becomes a load-bearing model parameter requiring independent calibration. If it stays low-sensitivity, the bug is real but minor.
3. **Validate retention regime numbers.** HIPAA/SOX/EU AI Act values were sourced casually; legal/compliance literature should confirm. EU AI Act in particular has a wide stated range (6 mo – 10 yr) that may collapse under closer reading.

**Adequate signal**: rerun with F12 wired, look at whether regulated-scenario wall-crossing dates shift more than ~6 months. That's the threshold below which the bug is honesty-without-impact and above which it's model-shaping.

## Sub-questions

- Should retention be a hard floor on stock, or a hard floor on age-of-oldest-memory? They differ when stock grows: a 6-yr age floor with continuing ingest can still allow aggressive consolidation of *new* memories.
- Are there partial-retention regimes (e.g. metadata retained, content tombstoned)? The model currently treats memory as monolithic; a metadata-only floor would be much cheaper.
- Does the F12 wiring interact with [F5](./f5-production-data.md)? If F5 is high and F12 is binding, regulated tenants accumulate fastest — possibly a separate scale story.

## Related

- [scale-crossings](../concept/scale-crossings.md) — the projections F12 should constrain.
- [f5-production-data](./f5-production-data.md) — F12 interaction with the largest unanchored per-session multiplier.
- Bug flagged 2026-04-29 in `project_kyrja_active.md` ("Known bugs / open issues in the model" section). Container-local; pending full atomization into wiki.
