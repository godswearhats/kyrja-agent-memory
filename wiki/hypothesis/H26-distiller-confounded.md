---
type: hypothesis
name: H-DISTILLER-CONFOUNDED — Exp 1 win was an Opus 4.7 distillation artefact
status: REJECTED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [encoding, confounder, distiller]
---

## Claim

Exp 1's slot-format (variant C) cost-reduction win was an artefact of Opus 4.7 distillation — C wins only because the distiller was strong enough to produce well-formed slots, and the win would disappear with a weaker distiller.

## What would falsify it

An experiment where slot-format (C) memory is distilled by a weaker model (Opus 4.6 or lower) and still wins on cost vs prose (A) distilled by the same weaker model.

## Evidence for

None. The hypothesis was not supported.

## Evidence against

- Exp 2 (Task 3, C-replication) used **Opus 4.6 distillation for both A and C**. C still wins: $0.805 vs $1.105, −27%, 95% CIs disjoint. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* same cost metric, same task class, controlled distiller — direct test of the confound. Slot-format effect persists when distiller version is held constant at the weaker level.

## Open sub-questions

- Does the slot-format win hold under **progressively weaker distillers** (e.g., Haiku, smaller Sonnet)? Production design assumes Haiku-class distillation for cost reasons.
- Is there a distiller-quality threshold below which the slot structure degrades into noise and the win disappears?
- Does the answer depend on the **complexity of the source session** (a Haiku distiller might handle simple sessions fine but fail on multi-step debugging)?

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — evidence anchor.
- [H25-replicate](./H25-replicate.md) — the experiment that closed this confound.
- [H23-util](./H23-util.md) — parent claim about memory utility.
