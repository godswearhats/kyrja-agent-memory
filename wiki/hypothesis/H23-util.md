---
type: hypothesis
name: H-UTIL — memory reduces cost on causally-related tasks
status: SUPPORTED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [wedge, encoding, cost-axis]
---

## Claim

Memory of prior tool-chain sessions, injected at session start, reduces agent-completion token cost on a causally-related task relative to a cold agent.

## What would falsify it

Across multiple tasks and distillers, memory-equipped agents show no significant cost reduction vs cold (CIs overlap), or memory-equipped agents cost more than cold on the same task.

## Evidence for

- Exp 1 (Task 2, `where_keep_attrs_scalar`): slot-format memory mean cost $0.142 vs cold $0.295 (n=4 each). **−52% cost**, 95% CIs disjoint. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* cost is agent-completion token spend, the wedge's promised benefit — direct measure of the hypothesis, not a proxy.
- Exp 2 (Task 3, `where_keep_attrs_coord`): slot-format memory mean cost $0.805 vs cold $1.334 (n=4 each). **−40% cost**, 95% CIs disjoint. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* same as above.
- Direction is stable across two tasks in the same family (xarray.where), two distiller versions (Opus 4.7 and 4.6), and the same agent model (Opus 4.6).

## Evidence against

- Magnitudes are **not portable**. −52% on Task 2 vs −40% on Task 3 — adjacent tasks, materially different effect sizes. Quote direction, not magnitudes, when generalizing.
- **Memory was partly redundant with the prompt** in Exp 2. The Task 3 issue's "Hints" section already contained Task 2's fix in prose, so the comparison was really "structured memory + prose hints" vs "prose hints alone," not "memory vs no memory." `[ASSERTED]` from [experiment side findings](../experiment/2026-05-11-write-quality-variance/README.md). A `cold-no-hints` arm would bound this.
- Pass-rate showed no memory effect in either run. That metric (SWE-bench gold) was found misaligned with the wedge hypothesis and retracted (see [experiment construct-validity note](../experiment/2026-05-11-write-quality-variance/README.md)) — so pass-rate is **not** evidence against this hypothesis, but the absence of supporting pass-rate evidence is a notable gap.

## Open sub-questions

- What is the marginal value of structured memory **beyond prose hints already in the prompt**? Cold-no-hints arm needed.
- Does the effect hold across **task families** beyond xarray.where? Single family is high variance risk.
- Does cost-reduction magnitude scale predictably with task complexity, agent-model version, or distiller quality?
- Is there a regime where memory **increases** cost (e.g., misleading prior on a divergent task)? Not observed; not tested.

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — primary evidence anchor.
- [H25-replicate](./H25-replicate.md) — the replication leg.
- [H26-distiller-confounded](./H26-distiller-confounded.md) — alternative explanation, rejected.
- [precision-over-recall](../decision/precision-over-recall.md) — read-path discipline this hypothesis's cost asymmetry argues for.
