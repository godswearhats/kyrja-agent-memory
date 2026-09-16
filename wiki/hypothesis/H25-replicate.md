---
type: hypothesis
name: H-REPLICATE — slot-format win replicates on a second task
status: SUPPORTED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [wedge, encoding, slot-format, replication]
---

## Claim

The slot-format encoding's cost-reduction win observed in Exp 1 (Task 2) replicates on a second task (Task 3) with disjoint confidence intervals.

## What would falsify it

Exp 2 Task 3 shows slot-format (C) **not significantly better than prose (A)** on cost (CIs overlap), or C costs more than cold.

## Evidence for

- Exp 2 (Task 3, `where_keep_attrs_coord`): C $0.805 vs A $1.105 (−27%, 95% CIs disjoint); C vs cold $1.334 (−40%, CIs disjoint). `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* cost is the metric Exp 1's original win was claimed on — direct apples-to-apples replication.
- **Distiller controlled.** Exp 2 used Opus 4.6 distillation for both A and C, closing the distiller-version confound Exp 1 left open (see [H26-distiller-confounded](./H26-distiller-confounded.md)).

## Evidence against

- **Adjacent task, not independent task.** Task 2 (scalar) and Task 3 (coord) are both `where_keep_attrs` parameterizations in xarray. Direction stable on adjacent tasks may not predict an unrelated task. A third task in a different repo family would strengthen the replication.
- **Magnitude shrank** from −42% (Exp 1) to −27% (Exp 2). Direction stable; magnitude not portable.
- **A-vs-cold CIs overlap** in Exp 2 ($1.105 vs $1.334, n=4) — A's marginal effect over cold is weaker than in Exp 1. Constrains how much "prose memory" alone helps.

## Open sub-questions

- Does the win replicate on a **non-xarray task family**? Single repo family is the biggest external-validity risk.
- Does the magnitude shrink monotonically with task difficulty, or is the relationship non-monotonic?
- Is the Exp 2 "memory + prose hints" confound (the Task 3 issue's "Hints" section already contained Task 2's fix) causing the C win to be a structure-vs-prose-in-prompt comparison, not a pure memory comparison?

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — both runs.
- [H23-util](./H23-util.md) — the parent hypothesis this replicates a leg of.
- [H26-distiller-confounded](./H26-distiller-confounded.md) — controlled-for by Exp 2 design.
- [H27-qual-structure](./H27-qual-structure.md) — the format-direction question this replicates.
