---
type: hypothesis
name: H43 — Soft-composition caddy with co-training exhibits emergent constructive memory
status: PROPOSED
last_ingested: 2026-05-19
sources: [../source/schacter-addis-buckner-2007-prospective-brain.md, ../source/buzsaki-2015-spw-r.md]
epistemic_tags: [speculated]
tags: [caddy, soft-composition, hard-selection, constructive-memory, co-training, m16-anchored, h37-adjacent]
---

## Claim

A caddy architecture with a **soft-composition output interface** (attention-style: a weighted blend of value vectors injected into the golfer's hidden state) and **co-trained end-to-end with the golfer** will exhibit *emergent constructive memory* in the [M16](../concept/mechanism-gap-matrix.md) sense — its outputs will be composed/recombined representations that are distinguishable from any single stored item — *without* requiring an explicitly engineered constructive operator. A caddy with a **hard-selection output interface** (top-K stored items returned verbatim) is structurally incapable of exhibiting this property regardless of training, because the interface forbids it.

## What would falsify it

`[SPECULATED]` The hypothesis is **rejected** if either of the following holds:

1. **Construction does not emerge** from soft-composition + co-training, as measured by a *composition score* (defined below) on the caddy's outputs falling within the noise band of the hard-selection baseline's composition score across a held-out task set.
2. **Construction emerges but does not help.** Composition score is high but downstream task performance (per the operationalisation in [Norman rubric § 5 properties](../concept/norman-rubric.md)) is no better than the hard-selection baseline, indicating the constructions are arbitrary recombinations rather than task-useful ones.

The hypothesis is **supported** if both (a) the soft-composition caddy's composition score is reliably higher than the hard-selection caddy's, AND (b) task performance is correspondingly higher, across multiple workloads (long-form generation, multi-document QA, agent-task-completion).

## Evidence for

- **`[SPECULATED]` Theoretical: every attention computation is by definition a weighted sum of value vectors.** An attention layer with K > 1 effective heads always produces a composed output, not a literal retrieval. This is a structural property of attention, not an empirical claim. Memorizing Transformer's attention over a long-term cache produces composed outputs by construction.
- **`[ASSERTED]` Biological precedent ([M14 Buzsáki SPW-Rs](../source/buzsaki-2015-spw-r.md) + [M16 Schacter et al. prospective brain](../source/schacter-addis-buckner-2007-prospective-brain.md)).** The hippocampus does not have a top-down "constructive operator" — no engineered subroutine that says "now compose fragments." SPW-Rs are reactivations of cell ensembles; joint replays happen because shared ensembles co-fire. Construction is emergent from substrate dynamics. Biology established the proof-of-concept for emergent construction from a substrate with the right wiring.
- **`[SPECULATED]` Hard selection structurally forbids emergence.** No gradient signal can rewrite "return K records verbatim" into "return one composed thing." The interface constrains the function space. This is an architectural argument, not an empirical one — but it follows from the basic ML observation that gradient descent operates within the function class the architecture admits.
- **`[ASSERTED]` Memorizing Transformer (Wu 2022)** — partial empirical precedent: soft-composition kNN attention over a long-term cache trained jointly with the LM improves perplexity on long-context modelling. Construction is not explicitly measured but is implicit in the output mechanism. See [retrieval-granularity](../concept/retrieval-granularity.md "pending").

## Evidence against

- **`[SPECULATED]` Co-training backprop-through-retrieval is famously hard.** [REALM](../source/realm-paper.md "pending"), [ColBERT](../source/colbert-paper.md "pending"), and other differentiable-retrieval architectures wrestled with gradient propagation through discrete retrieval operations. Memorizing Transformer dodged this — its long-term cache is filled *post-hoc*, no gradient through the cache. If true co-training of a writable caddy turns out to be unstable, the hypothesis's premise (co-training + soft composition) may not be reliably trainable, separately from whether emergence would occur in principle.
- **`[SPECULATED]` Pure selection may be sufficient for many tasks.** For short-horizon agent tasks dominated by 2-3 highly relevant memories ("the user prefers Python", "we're using Postgres"), the marginal value of composition over selection may be empirically small. Emergence could occur and still not provide a measurable downstream benefit.
- **`[CONTESTED]` Composition score may be ill-defined.** Distinguishing "composed output" from "weighted retrieval that happens to blend a few items" is a construct-validity question that the falsification criterion has not yet settled. See *Open sub-questions* below.

## Open sub-questions

- **How to define a composition score?** Candidate operationalisations: (i) cosine distance between the caddy's output and the nearest stored item exceeds a threshold τ; (ii) the output requires content from N ≥ 2 stored items to reconstruct (sparse-recovery test); (iii) human-judgment evaluation on whether the caddy's output asserts content present in any single stored item. Each has construct-validity issues — needs careful selection before running the falsification experiment.
- **What's the right co-training curriculum?** Co-training from scratch risks the golfer over-relying on a still-untrained caddy; pretrain-golfer-first-then-add-caddy risks the caddy underfitting because the golfer has already learned to do without it. The optimal curriculum is unknown and probably workload-dependent.
- **What's the right golfer:caddy size ratio?** Two scaling laws. The optimal ratio for emergence is unknown and likely depends on workload diversity (more diverse → larger caddy needed?).
- **Does the [pattern-separation](../concept/pattern-separation.md) requirement (from H34) interact with composition?** A caddy with enforced pattern separation may have *harder* time composing because separated representations are explicitly designed not to overlap. Or it may have an *easier* time because the composition has cleaner basis vectors to work with. Unknown.
- **Does construction belong on the caddy side or the golfer side?** Even with emergent online construction, M14's *off-line* SPW-R regime suggests there's value in pre-building constructed artifacts during quiet periods. The hypothesis as stated covers online construction only; an extension would test whether off-line construction via a [consolidation-channel](../concept/consolidation-channel.md) is additive or redundant.
- **How does this interact with [H37 (pluggable substrate)](../hypothesis/H37-pluggable-substrate.md "pending")?** A multi-point soft-composition architecture (different layers attend to different memory pools) would presumably exhibit emergence at each pool — but does the emergence compose across pools, or stay layer-local?

## Related

- [matrix row M16](../concept/mechanism-gap-matrix.md) — constructive memory / prospective brain; this hypothesis tests the *strong reading* of M16 (construction-as-implementation, not just construction-as-purpose)
- [schacter-addis-buckner-2007-prospective-brain](../source/schacter-addis-buckner-2007-prospective-brain.md) — primary source for the constructive episodic simulation hypothesis
- [matrix row M14](../concept/mechanism-gap-matrix.md) — Buzsáki SPW-Rs; the physiological substrate where biology achieves emergent construction
- [caddy](../concept/caddy.md) — the architectural commitments; the soft-vs-hard interface fork is the design choice this hypothesis tests
- [memory-caddy](../open-question/memory-caddy.md) — broader open question; this hypothesis is one falsifiable instantiation
- [retrieval-granularity](../concept/retrieval-granularity.md) — granularity choice interacts with composition (per-token attention enables learned-when-to-compose; per-turn retrieval forecloses it)
- [H42 — learned salience function](./H42-learned-salience-function.md) — companion hypothesis on the salience side; both H42 and H43 share the "learned through co-training rather than engineered explicitly" architectural bet
- [H34 — forgetting scores](./H34-forgetting-scores.md) — H34 + H43 together form the caddy's training programme: emergent forgetting (H34) + emergent construction (H43), both from co-training
- [pattern-separation](../concept/pattern-separation.md) — possible interaction with composition; needs investigation
- [consolidation-channel](../concept/consolidation-channel.md) — the off-line surface that may be additive to emergent online construction
- [discrete-unit-memory-architecture](../concept/discrete-unit-memory-architecture.md) — the broader family; hard-selection caddies are members, soft-composition caddies are at the boundary
