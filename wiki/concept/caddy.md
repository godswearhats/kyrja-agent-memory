---
type: concept
name: Caddy — co-trained memory module with separate state, learned policies, and activation-injection interface
status: living
last_ingested: 2026-06-12
sources: [../source/wayne-2018-merlin.md, ../source/borgeaud-2022-retro.md, ../source/josselyn-tonegawa-2020-engrams.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/dong-2025-norman-episodic.md, ../source/hassabis-2026-memory-bottleneck.md, ../source/redondo-morris-2011-stc.md, ../source/buzsaki-2015-spw-r.md, ../source/wu-2022-memorizing-transformer.md, ../source/fountas-2024-em-llm.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, memory-architecture, path-decision, discrete-unit-family, aj-originated]
---

## Definition

`[ASSERTED]` The **caddy** is the within-[discrete-unit memory architecture family](./discrete-unit-memory-architecture.md) member characterised by *a separately-trainable memory module with its own internal latent state, learned consolidation and retrieval policies, and an activation-injection interface to a primary LLM consumer*. It is the within-family alternative to bolt-on memory.

The caddy is **design vocabulary, not a product name.** It is a primitive in the Kyrja architectural lexicon — alongside "bolt-on memory," "substrate," and "consolidation channel" — and is expected to inform multiple future product decisions without naming any of them. Any eventual Kyrja product implementing the caddy concept will have its own name decided separately at product time.

The label "caddy" is grounded in a load-bearing analogy: a professional golf caddy is a separately-employed expert who carries the player's yardage book and mental model of the course, holds memory of past plays, communicates via a developed shorthand, has silent internal capacity (knows more than they say), and was apprenticed in caddying before being specialised to this golfer. The mapping to the architectural commitments is precise — see [The caddy/golfer analogy](#the-caddygolfer-analogy) below.

## Why this concept exists as its own page

`[ASSERTED]` The caddy concept previously lived as scattered material in [open-question/memory-caddy](../open-question/memory-caddy.md), [discrete-unit-memory-architecture](./discrete-unit-memory-architecture.md), [cognitive-maps-and-conjunctive-coding](./cognitive-maps-and-conjunctive-coding.md), [consolidation-channel](./consolidation-channel.md), [memory-consumer-axis](./memory-consumer-axis.md), and several source pages. The 2026-05-15 naming-decision session (caddy/golfer analogy) ratified "caddy" as the canonical term for what had been called "third-path memory model." This page consolidates the architectural definition in one place so other pages can cite it without re-defining.

Anti-sprawl satisfied on both clauses: the concept will be referenced by ≥5 existing pages once propagation lands, and it has its own status lifecycle (the empirical question of whether the caddy survives ablation against bolt-on baselines is still open — see [open-question/memory-caddy](../open-question/memory-caddy.md)).

## The five architectural commitments

`[ASSERTED]` A system qualifies as a caddy if it commits to all five of the following. Each commitment is independently checkable against an implementation.

1. **Separately-addressable model state.** The memory module has its own internal latent space, distinct from the primary LLM's parameters or KV cache. The internal state can be *larger than what is communicated at the read interface* — the [silent-engrams](./silent-engrams.md) property (M06 of the [mechanism-gap-matrix](./mechanism-gap-matrix.md)).
2. **Learned consolidation policies.** Write-side decisions — what to admit, how to aggregate, when to mark a memory consolidated — are produced by trained policies, not hand-coded thresholds or LLM-call heuristics over an unlearned store.
3. **Cue-completion retrieval.** Read-side primitive is pattern completion over learned representations (modern-Hopfield / [MERLIN](../source/wayne-2018-merlin.md)-shaped attention with learned keys and temperatures), not exact-key lookup or similarity search over frozen embeddings.
4. **Co-training via activation injection.** The memory module's output reaches the primary LLM via an internal forward-pass interface — enumerated and capability-distinguished in [[caddy-interface-doors]] as D-doors (embedding-level injection, cross-attention, adapter/LoRA modulation, logit-level interpolation). Text injection into the prompt collapses the architecture back into bolt-on — that interface is *not* sufficient for caddy status. The caddy and the consumer are co-trained.
5. **Auxiliary objective beyond the consumer's task loss.** The memory module is trained under at least one non-task objective on its own representations (MERLIN's MBP-style world-model reconstruction, JEPA-style embedding-space prediction, contrastive matching, or equivalent). This is the live empirical commitment: see [MBP-was-dropped](#the-mbp-was-dropped-empirical-question) below.

Commitments 1-4 are architectural and binary. Commitment 5 is the architecturally-distinctive bet that is still empirically untested in the LLM era.

## The caddy/golfer analogy

`[ASSERTED]` The analogy is not decorative — each axis maps precisely onto an architectural commitment, and the mapping is what makes the term sticky.

| Caddy property | Architectural translation |
|---|---|
| Separately-employed person with own training | Separately-trained model with own parameters |
| Carries yardage book and course mental model | Internal latent space dedicated to memory representations (commitment 1) |
| Holds memory of past plays for this golfer | Learned consolidation policies admitting and storing experiences (commitment 2) |
| Knows more than they say ("silent capacity") | Internal state larger than read interface (commitment 1, silent engrams) |
| Communicates via developed shorthand | Activation-injection interface, co-trained with consumer (commitment 4) |
| Apprenticed as a caddy first, then specialised | Pre-trained on a generic memory objective (commitment 5), then specialised to the consumer via co-training |
| Doesn't make the swings; player is still the agent | The primary LLM remains the reasoning agent; the caddy supports retrieval + compression, not generation |
| Replaceable but expensively | Co-training builds shared shorthand not recoverable from the underlying skill alone — strategic moat and strategic commitment simultaneously |

The analogy also captures what the caddy is **not**:

- Not a tool that the player picks up and uses (that's a bolt-on database).
- Not a part of the player's own mind that gets specialised (that's substrate).
- Not the player themselves doing both jobs (that's the LLM-only baseline).

`[SPECULATED]` The analogy may transfer further than the mapping above suggests. Open questions worth exploring: what is the caddy-analogue of "reading the green" (real-time environmental inference)? Of "between-shot conversation" (mid-task scratchpad)? Of "the caddy's bag" (multi-tier internal storage)?

## Within-family axes (M11 refinement)

`[ASSERTED]` The 2026-05-15 M11 walkthrough refined the original "shared architecture, learned-vs-unlearned policy split" framing twice. The caddy and bolt-on are not capability-distinct within the discrete-unit family — they are differentiated along three axes:

| Axis | Bolt-on flavour | Caddy flavour |
|---|---|---|
| **Policy learnedness** | Can be learned, often hand-coded | Naturally learned |
| **Architectural coupling** | Read and write are separable | Read and write can be one operation ([M10 reconsolidation](./mechanism-gap-matrix.md)) |
| **Integration depth** | Decomposed sub-systems with handoffs | End-to-end trained model |

`[ASSERTED]` The cross-examination during the M11 walkthrough produced this refinement honestly. The initial reading — "bolt-on commits to a storage representation upfront and therefore cannot do schema induction" — did not survive. A bolt-on system can induce schemas via at least four buildable sub-systems (learned embedding space, learned field structure, learned salience, learned retrieval policy). The real distinguisher is the **integration depth** of those sub-systems — how much information is lost across the boundaries between them — not a capability break. See [discrete-unit-memory-architecture § Refinement (M11 walkthrough)](./discrete-unit-memory-architecture.md#refinement-m11-walkthrough-2026-05-15-integration-depth-not-capability-binary) for the full development.

## Genuinely caddy-only properties (post-cross-examination)

`[SPECULATED]` After the M11 cross-examination, three properties were proposed as caddy-distinctive. The 2026-05-17 architecture-design session demoted one and absorbed another. Current status:

1. **End-to-end gradient flow through memory.** Bolt-on storage is non-differentiable; sub-systems can be trained individually but downstream-task-success gradient cannot propagate through the storage layer to the encoder. The caddy can. This matters when the only available training signal is sparse and distal — *"did the final answer help"* rather than per-step retrieval-success signals. **Status: kept.**

2. **Read-as-write coupling at zero latency** (R5). Biological [reconsolidation (M10)](./mechanism-gap-matrix.md) works because retrieval and update are *the same operation*. Bolt-on can chain them with millisecond gaps but they remain physically separable; the caddy could in principle collapse them into one forward pass. **Status: demoted 2026-05-17.** Per [[feedback_inspiration_not_blueprint]], R5 is a **biological constraint, not a structural insight** — biology has read-as-write because there is no engineering separation between read and write pathways at the synaptic level. Distributed-systems engineering's read-write separation is genuinely *better* for digital memory (auditable, debuggable, replayable). Periodic background re-encoding based on retrieval logs approximates the functional benefits without breaking distributed-systems invariants. Demoted from "load-bearing T4" to "interesting variant to test."

3. **Continuous online schema drift** (T_A3). Bolt-on sub-systems update on explicit retraining boundaries; the caddy can drift continuously. **Status: active load-bearing T4 research target as of 2026-05-20.** Absorbed into K2 (schema-fit-modulated consolidation) as the same bet viewed at different scales; K2 is the per-write decision; T_A3 is the system property that emerges from K2 firing continuously over time. Combined **K2+T_A3** is one of two active load-bearing T4 research targets (alongside T_A1b) per [caddy-as-research-program](../decision/caddy-as-research-program.md). The 2026-05-19 demotion to v2 was MVP-product-shaped (tier 3-4 wedge demonstration didn't require it for first-product scope) and was REVERSED 2026-05-20 once the caddy was reframed as a research program. Falsifiable form: [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md). Distinct mechanism from T_A1b per [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md) — CLS theory: distinct timescales, distinct jobs.

`[ASSERTED]` Net pattern: the caddy is **a refined bolt-on with tighter integration on the surviving axes (end-to-end gradient flow + continuous schema-fit consolidation), not a genuinely separate paradigm.** This is more honest than the earlier "third path is special" framing and is the operational reading the rest of the wiki should converge on.

## Candidate commitment 6 — tagged-intermediate-tier with capacity-bounded resource gating (under cross-examination 2026-05-17)

`[SPECULATED]` The M15 walkthrough (Redondo & Morris 2011 synaptic tagging and capture) surfaced a sixth candidate architectural commitment that no current memory system has:

> **C6 (candidate).** The caddy maintains a *transient intermediate tier* between "encoded" and "committed-to-persistence" states. Encoding sets a tag at low cost; persistence requires the tag to capture a resource from a *capacity-bounded global pool* during a bounded window; tags that fail to capture expire without commit.

Architecturally this is the [STC mechanism](../source/redondo-morris-2011-stc.md) ported to software: token-bucket persistence with shared budget, no coordinator, automatic forgetting via tag expiry. It gives the caddy *cheap-write semantics with deferred and context-modulated commit*.

**Why this is loaded as "candidate" rather than ratified:** the M15 walk also surfaced that **the load-bearing variable is the salience signal that gates pool emission, not the architectural shape itself.** See [salience-signal open question](../open-question/salience-signal.md) and [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md). Both STC-shape (C6) and hot-store-with-promotion (the [consolidation-channel](./consolidation-channel.md) framing) stall on the same upstream problem. C6 is worth adopting if and only if the salience-signal problem is solved well enough to make the deferred-commit mechanism reliably better than write-time admission. Until then, C6 remains an architectural option, not a binding commitment.

## Interface fork — soft composition vs hard selection (2026-05-17)

`[ASSERTED]` The M16 walk surfaced a design fork in the caddy's output interface that is logically distinct from the five commitments above but interacts with all of them.

| Interface | What the caddy hands the golfer | Composition path |
|---|---|---|
| **Hard selection** | K stored items returned verbatim, concatenated into context | None — interface forbids composition |
| **Soft composition** | Attention-style weighted blend of value vectors injected into golfer's hidden state | Emergent — every attention computation is by construction a weighted sum |

`[ASSERTED]` The fork is load-bearing for whether [M16 (constructive memory / prospective brain)](./mechanism-gap-matrix.md)'s *strong reading* — flexible recombination of fragments into novel composed outputs — is achievable through training without an explicitly engineered constructive operator. Hard selection structurally forecloses this; soft composition makes it the default behaviour. See [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) for the falsifiable claim.

`[ASSERTED]` Naming distinction worth preserving (AJ-originated, 2026-05-17): **the caddy's job is *anticipation*, not *prediction*.** Prediction is the golfer's job — taking the swing, choosing the next token. The caddy's job is preparing material in a form useful for the golfer's prediction. Real-world golf caddies anticipate (walk the course, note the wind, pre-club for conditions) without taking shots. Soft composition is the architectural shape that lets emergent anticipation cover the construction work biology does in SPW-Rs.

`[ASSERTED]` The fork interacts with [retrieval-granularity](./retrieval-granularity.md) — soft composition is *natural and cheap* at fine granularity (attention is the soft-composition primitive) and *expensive and unnatural* at per-turn granularity (you'd have to construct composed contexts via a separate process before generation begins). The current agent-memory product space defaults to per-turn + hard-selection; the caddy's interesting design space is fine granularity + soft composition.

`[ASSERTED]` The fork also interacts with [pattern-separation](./pattern-separation.md). Soft composition over densely-overlapping memory keys may compose *too easily* (returning blurry averages); soft composition over pattern-separated keys may compose *cleaner basis vectors*. The interaction is empirically open — H43's open sub-questions name it explicitly.

**Query head as the natural locus for the salience signal.** A dedicated query head in the golfer (a separate attention head whose sole job is producing memory queries) is the explicit *ask-the-caddy* operator. Its output is "what does the golfer need to know right now" — which is a salience computation by another name. [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md) becomes "the query head *is* the learned salience function on the read side." This is the online complement to the off-line salience signal that drives consolidation and forgetting; both are downstream of the same upstream computation, applied at different surfaces.

## The MBP-was-dropped empirical question

`[SPECULATED]` Commitment 5 (auxiliary objective beyond task loss) is the empirically live question. The MERLIN-RETRO/Memorizing-Transformer lineage demonstrates that the LLM-era retrieval-augmented language models *inherited MERLIN's learned read head but dropped MERLIN's MBP* — the auxiliary world-model loss that shaped memory representations independently of the consumer's task loss. See [open-question/memory-caddy § Sharpest research hypothesis](../open-question/memory-caddy.md) for the full development.

The 2026-05-15 literature pass surveyed:

- **[Memory³](https://arxiv.org/abs/2407.01178)** (Yang et al. 2024) — co-trained memory + activation injection at 2.4B scale, two-stage pretraining (warmup then continual-train with explicit memory), **next-token loss only at both stages.** Memory is the LLM's own sparsified attention KVs cached externally. Substrate-flavoured caddy-adjacent system, but not commitment-5-satisfying. Acts as a near-perfect natural baseline for the MBP-was-dropped ablation.
- **[ICAE](https://arxiv.org/abs/2307.06945)** (Ge et al. 2023) — LoRA-encoder + frozen LLM decoder, **dual pretraining objective** (autoencoding reconstruction + LM continuation). **Same-class-different-shape precedent for commitment 5 — see [ge-2024-icae](../source/ge-2024-icae.md) verbatim read.** Both objectives are *token-space* next-token CE losses computed at the frozen decoder's output (§2.2.1, §2.2.2); the memory slots are intermediate hidden states with no direct loss in representation space. Anti-collapse mechanism is "frozen decoder must reconstruct text," not the BYOL triad (no stop-grad, no EMA). Table 5's headline is GPT-4 pairwise win-rate on downstream instruction-following: pretraining-at-all wins **6.4×** over no-pretraining; the AE+LM mix vs either-alone lift is a smaller **1.3-1.4×**. **What ICAE supports for the caddy:** the gradient path through a memory bottleneck attached to an LLM can be trained successfully at LLM scale. **What ICAE does *not* support:** that representation-space (V-JEPA-style) auxiliary loss in particular works at LLM scale — that's a different loss family and is H44's load-bearing extrapolation. Per-context-compression scope (not experiential-memory across deployments) is a separate scope-mismatch.
- **[LLM-JEPA](https://arxiv.org/abs/2509.14252)** (Huang, LeCun, Balestriero 2025) — JEPA-style auxiliary loss on LLM training; **no memory module.** Their gap statement is independent confirmation: *"The lack of JEPA-style LLM is a testimony of the challenge in designing such objectives for language."*
- **Memory Decoder / MLP Memory** (Cao et al. 2025) — separate memory modules trained to imitate a kNN retriever; auxiliary objective is retrieval-distillation, not world-modelling.

`[ASSERTED]` The exact combination — *separately-stateful memory module + activation-injection interface + auxiliary world-model-style loss on the memory representations* — is unoccupied in the published literature as of 2026-05-15. The cleanest open empirical question in the caddy space is whether commitment 5 adds signal over commitments 1-4 alone.

## External validation (2026-05-16 update)

`[ASSERTED]` Two independent external sources converge on the caddy wedge:

**The [Norman rubric](./norman-rubric.md) (Dong, Lu, Norman & Michelmann 2025, Trends in Cognitive Sciences):** The Princeton/NYU Norman lab — the leading academic group on hippocampal-CLS modelling — explicitly endorses the caddy architectural pattern by name. Verbatim, page 3: *"a memory system that rapidly stores information in a latent and lasting form (like the hippocampus in humans) and is separate from both the context window (which can be limited in size, like working memory in humans) and the weights of the main LLM (which are updated incrementally, like neocortex in humans)."* They further endorse storing internal representations over verbatim text (commitment 4). The paper specifies five evaluable properties (dynamic memory updating, event segmentation, selective encoding/retrieval, temporal contiguity, competition at retrieval) — see [norman-rubric](./norman-rubric.md) for the full scoring framework.

**Hassabis on context windows as "badly approximated hippocampus"** (post-Gemini-3 interview, see [hassabis-2026-memory-bottleneck](../source/hassabis-2026-memory-bottleneck.md)): The DeepMind CEO publicly diagnoses the same failure mode the caddy is proposed to solve, using the same hippocampal framing. Pitch-relevant: *"a badly approximated hippocampus... kind of brute force — you're remembering everything when in fact most tokens are irrelevant."*

The combination — top-tier academic validation in a peer-reviewed journal plus public commercial CEO endorsement — is the strongest possible external validation for the caddy wedge. The differentiation pitch is no longer "novel architectural pattern" but rather "the first system to satisfy the [norman-rubric](./norman-rubric.md) on a sidecar architecture that matches Norman's explicit recommendation."

### Norman-rubric alignment of the five commitments

| Caddy commitment | Norman rubric property | Alignment |
|---|---|---|
| C1 separately-addressable state | Architectural prerequisite (Norman endorses separate-from-context-and-weights) | ✓ |
| C2 learned consolidation policies | Property 3 (selective encoding) | ✓ + extends to admission |
| C3 cue-completion retrieval | Property 5 (competition at retrieval) | ✓ — pattern-completion is winner-take-all-shaped |
| C4 activation injection | Architectural prerequisite (Norman endorses internal-representations over verbatim) | ✓ |
| C5 auxiliary objective | Not directly in rubric; closest is dynamic memory updating + consolidation | partial — Norman's Outstanding Question 2 ("EM updates semantic memory through consolidation") names this as the missing piece |

**Additional Norman properties the caddy must implement beyond C1-C5:**

- **Event segmentation** (property 2): the caddy's encoder must do surprise-based boundary detection, not fixed-size chunking. This is a *new commitment* beyond C1-C5 that the Norman rubric forces us to adopt.
- **Temporal contiguity** (property 4): scale-invariant context-drift in the retrieval mechanism (TCM-style, per [howard-kahana-2002-tcm](../source/howard-kahana-2002-tcm.md)). Another new commitment.

These additional properties are now load-bearing for the pitch and should be incorporated into Kyrja's experimental programme.

## Research prototype architecture and the two load-bearing T4s (2026-05-20)

`[ASSERTED]` The 2026-05-17 architecture-design session produced the first detailed architectural specification — see [caddy-architecture](./caddy-architecture.md) for the full treatment (six-component sketch, 25 operations, tier labels, prototype scoping). Headline findings (refined 2026-05-20 under the research-program framing):

**Two active load-bearing T4 research targets: T_A1b and K2+T_A3.**

Per [caddy-as-research-program](../decision/caddy-as-research-program.md), the caddy is a research program (commercial vehicle is Eira's bolt-on track; decoupled). Both T4s are active load-bearing — distinct mechanisms on distinct timescales per [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md). Ordering between them is set by a stack-rank exercise (forthcoming) using scientific leverage, tractability, dependencies, and frontier-pacing as criteria — all anchored to "moves us toward demonstrating tier 3-4 retrieval via the caddy."

```
T_A1b (auxiliary world-model loss on memory representations; "MBP-was-dropped")
  ↑ representation-level bet (JEPA family); V-JEPA is same-shape smaller-scope precedent
  ↑ ICAE is same-class different-shape precedent (token-space loss, not representation-space)
  ↑ falsifiable form: H44 (cross-domain analogical retrieval ≥10pp over baseline)
  ↑ falsifier: 2026-05-18 isolation experiment (pre-registered thresholds)

K2+T_A3 (schema-fit-modulated consolidation with continuous online drift)
  ↑ consolidation-policy bet; CLS-theory-informed; slow-timescale cortical-analog
  ↑ falsifiable form: H40
  ↑ falsifier: Version A static-reference vs Version B dynamic-reference design
    preserved inside H40

NOT ACTIVE LOAD-BEARING:
  R5 (read-as-write reconsolidation) — demoted 2026-05-17; biological constraint, not insight
  K6 (offline composition) — deferred from active queue; valuable but non-trivial
```

**2026-05-18 sharpening.** T_A1 reformulated as **T_A1b** (JEPA-style predictive loss on event-segmented memory reps) per [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md). Tier 1-2 capability preserved as side-effect via [multi-field-memory-unit](../decision/multi-field-memory-unit.md). Tier framing in [memory-retrieval-tiers](./memory-retrieval-tiers.md).

**Sequencing fallback for retention policy.** If K2+T_A3 is queued behind T_A1b per the stack-rank, the prototype can run K5 with an engineered baseline (FIFO/LRU/TTL or frozen-predictor novelty scoring + periodic batch re-curation) as a placeholder so T_A1b work isn't blocked. This is sequencing, not a claim that the learned policy is unneeded.

**Research prototype inherits known LLM-scale primitives:**
- Single mid-layer cross-attention at ~70% depth ([Memorizing Transformer](../source/wu-2022-memorizing-transformer.md))
- Dedicated W_Q_mem query head, co-trained for geometric alignment with caddy's K-space
- Surprise-based event boundaries with modularity-graph refinement ([EM-LLM](../source/fountas-2024-em-llm.md))
- Light finetune of pretrained base at ~4% of pretraining cost (MemTx §4.5)
- Auxiliary world-model loss on learned representations (T_A1b; load-bearing) — no LLM-scale precedent
- Schema-fit-modulated consolidation with continuous drift (K2+T_A3; load-bearing) — no LLM-scale precedent

See [caddy-architecture § Research prototype specification](./caddy-architecture.md#research-prototype-specification--load-bearing-t4-research-targets) for the full distillation to ~17 ops.

**Integration mechanics** are detailed in [caddy-interface-doors](./caddy-interface-doors.md) — D-doors (caddy → golfer), U-doors (golfer → caddy), and Q-doors (golfer actively probing caddy). The current commitments are:
- Out-door: D2 (single mid-layer cross-attention)
- In-doors: U1 (raw input) + U4 (surprise signal)
- Query-doors: Q1 (cross-attention) + Q4 (dedicated W_Q_mem head)

Q4 (the dedicated W_Q_mem head) is also the **online complement to the M16 interface fork** discussed above — soft-composition (D2's attention-weighted blend) on the out-door side, and dedicated salience-shaped queries (Q4) on the in-door side. The two together give the caddy a clean read/query/integrate cycle.

## Post-Norman gap finding (2026-05-16)

`[ASSERTED]` The Norman rubric was published June 2025 in Trends in Cognitive Sciences. **Eleven months later (as of 2026-05-16), no system in the published literature scores ≥3/5 on the rubric.** EM-LLM (Fountas 2024, ICLR 2025) at ~2.5/5 is the current ceiling.

Post-Norman publications surveyed:

- **[Hope / Nested Learning](../source/behrouz-2026-nested-learning.md)** (Dec 2025, 6 mo after Norman): 1.5/5
- **NextMem** (Feb 2026, 8 mo after): no rubric engagement in abstract
- **GradMem** (Mar 2026, 9 mo after): no rubric engagement in abstract
- **Anthropic Auto Dream** (Mar 2026, 9 mo after): 1 of 5 properties (consolidation only)
- **[AMI Labs](../incumbent/ami-labs.md)** (Mar 2026, 9 mo after): no rubric engagement in public framing
- **[Engramme](../incumbent/engramme.md)** (Mar 2026 stealth exit, 9 mo after): 0/5
- **[NeoCognition](../incumbent/neocognition.md)** (Apr 2026, 10 mo after): stealth, unknown
- **[MEGa](../source/pan-2025-mega.md)** (Apr 2025, predates Norman): 1.5/5

`[ASSERTED]` The empirical-implementation gap is real and persistent. Most plausible interpretation: integrating all five properties in one system is research-program-scale work that doesn't fit the "ship a paper a quarter" cadence the field optimises for. The cell remains open despite the rubric being publicly specified by the most-credentialed possible source.

This is the strongest evidence-shape for the venture's wedge being defensible: not "no one has thought of this" but "no one has built this, eleven months after the standards-setting paper said they should."

## 2026-05-30 — the frozen co-trained RL-controller framing + open challenges

`[SPECULATED]` (Nils/AJ strategy session. **Exploratory — threads to pressure-test, not a verdict for or against the caddy.** AJ flagged not to overindex.) AJ sharpened the caddy as a concrete bet: an **RL-trained controller, co-trained with the LLM and then *frozen* (like the LLM)** — reads activations at an intermediate layer (~16), decides what to retrieve and injects at a later layer (~24), and decides what (if anything) to **store**. The store itself grows at runtime (cheap append to a non-parametric store); the *policies* are frozen. The point: the expensive learning (both LLM and controller) happens **once, at training time**; runtime is cheap. This fits commitments 2/4 and the "anticipation not prediction" framing — RL supplies the *consolidation signal* (credit assignment = what's worth storing), reframing consolidation as credit-assignment, not compression.

**Open challenges (rocks thrown this session — recorded as risks, not refutations):**

1. **Relocates the cheap-vs-compositional trade-off to *training time*, doesn't break it.** Freeze controller + LLM and the *grammar of composition is fixed forever at training*. Runtime can add new **operands** (new facts/entities) but not new **grammar** (new composition operators/skills) — modulo the frozen model's *steerable* range (function/task vectors push the bound past the literal training set, but it stays a bound you can't grow at runtime). See the [operand-vs-grammar / wedge-sizing question](../open-question/thinks-with-wedge-sizing.md). Whether this bound is acceptable depends on whether the target memory is "new operands" (✓) or "new grammar from experience" (✗ — the bounded caddy structurally can't).
2. **The irony.** It invokes RL but *freezes away* RL's headline superpower — continual skill acquisition. It keeps RL's training-time strength (learn a good controller) and forfeits runtime learning. May be the right *bounded* bet, but eyes open.
3. **The write policy may not train (historical rock — now partly CONTESTED, see below).** NTM/DNC/[MERLIN](../source/wayne-2018-merlin.md) found that a *discrete "decide what to store"* controller is brutal to train (sparse, long-horizon, huge action space) — the field retreated to **differentiable** read/write or **auxiliary** losses (MERLIN's MBP). A pure-reward store-decision in session 1 paying off in session 2 is the highest-variance credit-assignment regime; convergence is not guaranteed. (This is exactly the [commitment-5 / MBP-was-dropped](#the-mbp-was-dropped-empirical-question) live question, seen from the RL side.)

   `[CONTESTED]` (2026-06-10; **ALL FOUR cluster papers verified on full read 2026-06-12**) A 2025–2026 wave of papers reports discrete memory-op controllers trained by reward that *do* converge: [Memory-R1](../source/yan-2025-memory-r1.md) (ADD/UPDATE/DELETE/NOOP via PPO/GRPO, 152 QA pairs — verified, but its manager trains as a **per-turn bandit** on turn-attributed rewards with GPT-4o-mini-built bank snapshots, so it never enters the long-horizon regime the rock is about; see [§ Rock-3 reading](../source/yan-2025-memory-r1.md)), [Mem-α](../source/wang-2025-mem-alpha.md) (structured core/episodic/semantic store, GRPO — verified: trajectory-level training converges only with **per-action LM-judge process rewards**; dropping them is their own "catastrophic" ablation), [AgeMem](../source/yu-2026-agemem.md) (verified: the advertised "step-wise GRPO for sparse and discontinuous rewards" deflates to **uniform terminal-advantage broadcast plus ground-truth-informed reward shaping** at the cluster's shortest horizon; notably the only member training a single unified policy with no frozen counterpart), and [Memory-R2](../source/yan-2026-memory-r2.md) (LoGo-GRPO; names and fixes the exact unfair-credit-assignment pathology our supersession trace narrated). **The objection therefore splits.** At the **text-store / tool-call level** the "doesn't train" rock is contested — and the Memory-R2 full read both *confirms the claim* (INSERT/UPDATE/DELETE policy converges, beats baselines, transfers OOD from 2 training conversations) and *vindicates the rock's mechanism*: without their machinery, direct 32-session training collapses (F1 0.47→0.27, M-Fail >70%). Convergence is purchased by horizon curriculum (the dominant ablation, −25.55 F1 when removed), local rerollouts from cached memory states (~3 F1), session-attributed rewards (privileged evidence-location supervision), and a heavily prompt-scaffolded action space — see [yan-2026-memory-r2 § Rock-3 verdict](../source/yan-2026-memory-r2.md). At the **latent-store / activation-injection level** (the caddy's commitment 4) it stands *unproven either way* — none of these papers trains a controller over a latent store injected via cross-attention; the R2 read narrows the latent-port question to session-attributable probe rewards (state checkpointing is cheap). **Cluster read COMPLETE (4/4 verified per [[feedback_load_bearing_sources]]).** The pattern holds across all four: convergence is purchased with **reward densification** — turn-attributed QA (R1), curriculum + cached-state rerollouts + session-attributed QA (R2), per-action LM-judge validity (Mem-α), ground-truth-informed terminal shaping at short horizon (AgeMem) — never by the discrete-write regime being benign. Nobody trains on sparse end-of-trajectory reward alone at long horizon; AgeMem's outcome-only ablation converging *at short horizon* and R2's direct-32-session collapse are the same horizon story from opposite ends. The portable question for the latent variant: which densifier survives a store an LM judge cannot read? (Mem-α's judge reward doesn't port unless the probe/decoder makes slots legible — which loops back to commitment 5.)

   `[ASSERTED]` **The portable question now has a replicated candidate answer (2026-06-12, three follow-up full reads).** [Mem-T](../source/yue-2026-mem-t.md) and [TreeMem](../source/mao-2026-treemem.md) — independent groups, different decomposition axes (retrieval steps within one policy vs pipeline stages across policies) — both train memory policies with **structural credit assignment**: branch the computation, average leaf outcomes downstream, credit the node. The signals consume only leaf outcomes, branching topology, and provenance/length metadata — **never store contents** — so they port in principle to a store an LM judge cannot read (leaf judges, which read final *answers*, survive; store-reading judges don't). TreeMem's controlled comparison (its Table 3) shows structural credit beating both uniform terminal broadcast and hand-engineered intermediate rewards. Three limits keep the rock standing: (1) both exercise the mechanism only at **short effective horizons** (≤6 retrieval steps / 3 pipeline stages), each escaping the long write horizon differently — Mem-T retreats to hindsight-filtered SFT for construction, TreeMem collapses construction to a single shot on evidence-located (privileged-curation) sessions; (2) branch-and-average cost explodes with horizon (TreeMem's own limitation note); (3) Mem-T's SFT optimizer doesn't port to continuous latent writes — only the credit *score* does. Meanwhile [ElasticMem](../source/feng-2026-elasticmem.md) — the field's first "RL + latent memory" paper — confirms the **latent write cell is empty**: its bank is batch-built offline from prompted text extraction and frozen; RL trains read-side only (retrieval state, per-memory soft-token budget, projector — all on content-free metadata features, converging cleanly). **Net Rock-3 status: candidate densifier family exists, replicated, content-free; demonstrated text-only and short-horizon; a learned streaming write policy over a latent store remains unoccupied in the literature as of 2026-06** ([[feedback_capability_vs_resource]]: read absence as tractability-seeking, not technical verdict).
4. **Frozen-policy OOD.** A frozen retrieval/store policy generalises only as far as its training distribution — "you can only remember things you were *trained to know how to* remember." The generalisation burden moves from the write to the controller's OOD robustness; it doesn't vanish.

`[SPECULATED]` **Freeze topology is an OPEN axis, not a commitment (2026-06-12).** The "everything parametric frozen at deployment" picture above is one point in a per-component design space (always-frozen / scheduled thaws / runtime-plastic); AJ explicitly flagged we lack empirical grounds to commit, and RL natively favours *some* component staying unfrozen. See [open-question/freeze-topology](../open-question/freeze-topology.md) — including the sharpest sub-question: whether a weights-resident schema choice would silently foreclose K2+T_A3.

### Rock-3 mitigations — how you'd actually train the discrete policies

`[SPECULATED]` (Provenance: 2026-06-08 Web-Claude transcript, interrogated by Nils 2026-06-10 per [[feedback_external_claude_conversations]]; design proposals, not measured.) If Rock 3 is to be answered at the latent level, three mechanisms are the candidate toolkit:

- **Counterfactual-margin reward.** Reward the caddy's *marginal* contribution, not raw performance: `reward = loss(golfer alone) − loss(golfer + retrieved memory)`. Because the golfer is frozen, the "alone" baseline is a second forward pass with the injection gates masked — cheap. This cancels the text-difficulty variance that otherwise dominates (easy vs hard text inflates/deflates raw loss regardless of the caddy), and concentrates *all* learning pressure where memory is non-redundant — the caddy earns nothing for storing what the golfer already knew. It builds the advantage baseline into the reward itself, cutting variance before the critic engages — a direct attack on Rock 3's "highest-variance regime."
- **Multi-horizon critics.** Retrieval decisions have near-immediate consequences (short effective horizon); write decisions pay off sessions later (near-1 horizon). A single discount factor forces one horizon onto both. Use separate critics with separate γ (short for retrieval, near-1 for writes), or an ensemble of γ-heads on a shared body (hyperbolic-style discounting — heavy weight on the immediate, steep drop, fat tail for the distant future, which matches the actual utility distribution of memories: useful soon or much later, rarely in between).
- **The two design lemmas ("failures indict design, not weights").** A policy *cannot learn a distinction its state representation cannot observe*, and *cannot take an action its action space does not contain*. The supersession failure ([fact-supersession](./fact-supersession.md)) is caused by both: the retrieval policy can't see staleness (so it can't avoid stale facts) and the write policy has no supersede/silence action (so it can't reconcile). No reward tuning fixes either — they are state-vector and action-space design problems. This reframes "the policy didn't learn" as "we under-specified what it could see or do."

`[SPECULATED]` These mechanisms are *why* the text-level papers above may be converging where the 2018-era controllers did not, and they are the things to port ([[feedback_borrow_not_adopt]]) if the caddy attempts the latent variant.

## Scope limits

- **Concept, not product.** The caddy is design vocabulary; the eventual product will have a different name and is decided at product time. Do not use "caddy" as a customer-facing label.
- **Within the discrete-unit family only.** The caddy is one member of the [discrete-unit memory architecture family](./discrete-unit-memory-architecture.md), not a separate family. Continuous-update substrate (Hope-shape) is outside the family entirely.
- **Open empirically.** Commitment 5 is the live empirical bet. It is held loosely pending an ablation that has not been run in the published literature.
- **Does not commit to a specific implementation.** The caddy concept admits multiple instantiations differing in architectural choices (which auxiliary objective; which sub-architecture for the encoder; how aggressive the silent-state subspace is). Implementation choices are downstream of the concept.
- **Not the same as MERLIN.** MERLIN is a 2018 RL agent template; the caddy is its conceptual descendant ported to the LLM-era / agent-memory setting. The differences (within-episode vs cross-deployment, RL policy vs LLM consumer, MBP's specific multi-modality vs an LLM-era analogue) are architecturally significant.

## Related

- [[caddy-architecture]] — detailed architectural specification (six components, 25 operations, tier labels, prototype scoping). The first concrete answer to "what does the caddy actually look like."
- [[caddy-interface-doors]] — D/U/Q door framework for how data flows between caddy and golfer at integration time. The mechanical specification of the read/write/query paths.
- [Memorizing Transformer (Wu et al. 2022)](../source/wu-2022-memorizing-transformer.md) — architectural template for the caddy's read path; §4.5 validates bolt-on viability at ~4% of pretraining cost.
- [EM-LLM (Fountas et al. 2024)](../source/fountas-2024-em-llm.md) — current Norman-rubric ceiling (~2.5/5); architectural template for E1 event segmentation; NOT a sidecar (per-layer per-head KV-cache management).
- [[discrete-unit-memory-architecture]] — the family the caddy belongs to. The caddy is one of three named members (the other two being bolt-on memory and biological CLS).
- [[memory-consumer-axis]] — orthogonal axis. The caddy occupies the *outside-LLM × memory-for-the-model* cell, currently empty in deployed systems.
- [[catastrophic-interference]] — the architectural problem the caddy must take a position on; current commitments 1-5 are silent on which solution-shape (M11 / M14 / RC / LoRA) the caddy adopts.
- [[lora]] — one of the explicitly-named consumer interface options in commitment 4; also the LLM-era M14-shape stumble-into.
- [[reservoir-computing]] — candidate concrete implementation of M14's preconfigured-vocabulary framing for the caddy substrate. **Updated 2026-05-17:** the literature-review pass closed Sketch A (pure-RC-as-caddy-substrate) as empirically dead — both Pascanu/Jaeger 2011 and Sussillo/Abbott 2009 extended the architecture for hard tasks. Sketch B (S4-shape: structured + trained substrate) and Sketch C (reservoir + writable buffer + off-line consolidation) remain alive. The cerebellar biological precedent is feedforward, not recurrent, weakening the hippocampus analogy.
- [[salience-signal]] — load-bearing input variable that gates commitment 2 (learned consolidation policies) and candidate commitment 6.
- [[consolidation-channel]] — Kyrja's primary wedge concept. The caddy's commitments 2 and 5 instantiate the channel.
- [[cognitive-maps-and-conjunctive-coding]] — the biological mechanism set documenting what architectural priors a caddy would need to bake in (M11-derivative; 2026-05-15).
- [[silent-engrams]] — M06 of the matrix; the silent-state property is commitment 1's biological precedent.
- [[verbatim-vs-latent-tiers]] — the fact/schema *format* split, read-mechanics, and the two learning channels behind commitments 3/4.
- [[fact-supersession]] — the change-over-time failure of the fact tier; the Rock-3 design lemmas govern its fix.
- [[pattern-separation]] — architectural prerequisite for graded decay; interacts with interface fork (soft composition over separated keys vs over overlapping keys).
- [[retrieval-granularity]] — granularity spectrum; the soft-composition + fine-granularity choice is the caddy's interesting design space.
- [[H43-soft-composition-emergent-construction]] — falsifiable claim that the soft-composition interface produces emergent M16 strong-reading construction through co-training, without explicit constructive operator.
- [[mechanism-gap-matrix]] — the catalogue the caddy is being designed to instantiate.
- [open-question/memory-caddy](../open-question/memory-caddy.md) — the live design question. Falsifiability hooks, MBP-was-dropped specification, three-interface decomposition, state-as-of-pause.
- [[substrate-as-memory]] — the substrate path's framing; the caddy is *not* substrate (no modification of the primary LLM's parameters); contrast useful for keeping the concept tight.
- [[substrate-paradigms]] — P2 substrate-as-module taxonomy; the caddy is a descendant of P2 with stronger commitments.

## Source archive

- AJ-ratified naming decision, 2026-05-15 side-window session. Caddy/golfer analogy session was the load-bearing moment.
- Conceptual content draws from: MERLIN verbatim read (2026-05-15), matrix walk M03-M11 (2026-05-15, main window), cross-examination on schema induction (2026-05-15, main window mid-M11), 2026-05-15 literature pass surveying co-trained-memory-with-auxiliary-objective space.
