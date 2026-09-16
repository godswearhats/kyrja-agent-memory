---
type: concept
name: Active-Stages Framework for Agent Memory
status: timeless
last_ingested: 2026-06-10
# bumped 2026-05-14 evening — added inbound links from new cog-sci source pages (McClelland 1995, Yang 2024, Josselyn 2020, Tse 2007, Nader 2000)
sources: [../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/yang-et-al-2024-selection-of-experience.md, ../source/josselyn-tonegawa-2020-engrams.md, ../source/tse-et-al-2007-schemas.md, ../source/nader-schafe-ledoux-2000-reconsolidation.md, ../source/howard-kahana-2002-tcm.md]
epistemic_tags: [speculated]
tags: [substrate-memory, active-stages, training-signal, framework, wedge-relevant]
---

## Definition

The **active-stages framework** decomposes agent memory into five pipeline stages — `creating → retaining → finding → recalling → using` — and classifies each as either **passive** (mechanical, content-independent operations) or **active** (operations requiring agency, judgment, or decision-making over time).

The passive/active distinction:

- **Passive stages**: mechanical operations driven by deterministic rules or learned representations (vector lookup, attention, softmax). Current LLMs handle these well.
- **Active stages**: operations requiring temporal credit assignment, content-aware judgment, or agency over what to keep / merge / discard / supersede. **Structurally absent from the current substrate.** `[SPECULATED]`

The four active stages, named explicitly:

| active stage | what it does | distinct because |
|---|---|---|
| **Selection (curation)** | Decide what's worth storing at write time | Requires "will this be useful later?" judgment — no gradient from next-token loss |
| **Consolidation** | Merge near-duplicate memories into one abstracted entry | Requires comparison signal across the memory store |
| **Controlled forgetting** | Evict by content/relevance, not just age | Requires relevance modeling over time. **M17 reweighting (2026-05-17):** the [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) walk repositioned this stage — biology's "encode promiscuously, forget intelligently" architecture suggests this may be *the* place intelligence belongs, not one stage among four equally-weighted. The RLVR-for-curation recommendation may apply more strongly to *this* stage than to curation. See [H34](../hypothesis/H34-forgetting-scores.md) and [pattern-separation](./pattern-separation.md) for the architectural-prerequisite framing. |
| **Updating** | Detect and resolve conflict between new and old | Requires conflict detection + supersession semantics |

`[ASSERTED]` (2026-06-10) **Supersession spans two stages, and conflating them is a failure mode.** Handling a fact that changed ("vegetarian" → "pescatarian") decomposes as **detection** (an *updating*-stage job: recognise the new fact contradicts the old, and distinguish supersede vs refine vs coordinate multi-value) → **disposal** (a *forgetting*-stage job: silence the loser, per [silent-engrams](./silent-engrams.md)). The forgetting machinery ([H34](../hypothesis/H34-forgetting-scores.md)) supplies only the disposal half; the detector is the unsolved *updating*-stage piece. See [fact-supersession](./fact-supersession.md).

## Why the framework matters

`[SPECULATED]` (own observation during 2026-05-12 grading exercise on kNN-LM / Memorizing Transformers / RETRO — Kyrja-internal diagnostic claim, not externally validated). The active/passive split is **diagnostic**: applied to existing substrate-memory architectures, it shows a clean pattern — they differ in *how cleverly they retrieve from a passive store*, not in *whether the store is actively curated*. None of them is.

The deeper claim from this diagnosis: **the active stages aren't engineering oversights; they're absent because next-token cross-entropy (the dominant training signal) can't produce them.** `[SPECULATED]` Curation requires temporal credit assignment; consolidation requires a comparison signal across the store; forgetting requires relevance modeling. None of these naturally fall out of pretraining or even RLHF.

Convergence with cog-sci (encoding → storage/consolidation → retrieval/reconstruction → application) and DB/IR engineering (ingestion → persistence → indexing → query → materialization) is structural — analogical evidence the decomposition is correct, not direct empirical validation. `[SPECULATED]`

## Per-stage training-signal taxonomy

For each active stage, the candidate training-signal flavor differs:

| stage | training-signal flavor | reason |
|---|---|---|
| Curation | **RLVR with delayed reward** (future-retrieval success as verifier) | Reality is the judge, eventually — same trick as RLVR for reasoning models, applied on a longer time horizon |
| Consolidation | **Self-supervised contrastive** (same-fact pairs should merge) | "These two memories are about the same thing" is a comparison signal, not a reward signal — no RL needed |
| Controlled forgetting | **RLVR with negative-retrieval signal**, or LRU / usage heuristic | Could be non-RL — the heuristic baseline may be good enough |
| Updating | **Self-supervised conflict detection + RL for resolution** | Hybrid — detection is symmetric to consolidation; resolution requires judgment |

`[SPECULATED]` These are design recommendations from the 2026-05-12 design session, not empirically validated assignments. The flavors map cleanly onto the existing post-training taxonomy (RLVR / RLHF / self-supervised), but the per-stage application is novel synthesis.

## Temporal credit assignment — the central technical risk

The active stages share one structural challenge that RLVR did **not** have in reasoning models: **the verifier fires on a delayed horizon.** `[SPECULATED]` Re-tagged 2026-05-13: the underlying delayed-reward credit-assignment difficulty is textbook RL knowledge, but applying it to a multi-week memory-curation horizon is Kyrja-internal extrapolation, not externally anchored.

- **o1-style RLVR**: solve the math problem, check answer, immediate reward within one generation. Fast credit assignment.
- **Memory curation**: store X today, X turns out useful at retrieval next week or month. Reward signal delayed by orders of magnitude.

Standard PPO machinery struggles with multi-week credit assignment. This is the load-bearing technical risk in any substrate-aware memory architecture that uses RL-style training. `[SPECULATED]` Mitigations worth investigating:

- **Counterfactual rewards**: would the query have succeeded *without* this memory? Cheaper than waiting for natural retrieval.
- **Offline batch training**: rebuild curator periodically from logged retrieval outcomes (sidesteps online credit assignment).
- **Synthetic future queries**: generate plausible future queries at write time, score retrievability against them immediately.

## Role in Kyrja design

The framework is the conceptual lens for Kyrja's substrate-aware-memory thesis. Three implications:

1. **Diagnostic.** The [seven-layer integration stack](./seven-layer-stack.md) maps onto the passive stages well; [admission-control](./admission-control.md) is the only layer targeting an active stage directly (curation). The framework explains *why* the seven-layer integration matters and where the architectural depth needs to land.

2. **Design grid.** Each active stage needs three answers: **mechanism, training signal, unit of memory.** The per-stage taxonomy above answers the training-signal column; the seven-layer stack answers parts of mechanism; unit-of-memory varies by stage (token / vector / chunk / structured record / graph node).

3. **Substrate vs RAG++ split.** RAG++ approaches structurally avoid the active stages because they keep the LM frozen and rely on LLM-mediated heuristics ("ask the model: is this worth keeping?"). Substrate-aware approaches introduce explicit loss signals for the active stages. This framework names the gap RAG++ is choosing to ignore.

## Connection to existing wiki

- [substrate-as-memory](./substrate-as-memory.md) — paradigm-level framing in which the active stages live. Active stages are the operations RAG++ avoids and substrate-as-memory addresses.
- [substrate-paradigms](./substrate-paradigms.md) — P1/P2/P3 architectures each implement the active stages differently: P1 ([Mamba](../source/gu-dao-2023-mamba.md), [Titans](../source/behrouz-2024-titans.md), [TTT](../source/sun-2024-ttt.md)) embeds selection/forgetting in state-update dynamics; P2 ([NTM](../source/graves-2014-ntm.md), [RETRO](../source/borgeaud-2022-retro.md)) makes them differentiable read/write ops; P3 ([DreamerV3](../source/hafner-2023-dreamerv3.md), [LeCun 2022](../source/lecun-2022-autonomous-mi.md)) embeds them in world-model training.
- [consolidation-channel](./consolidation-channel.md) — formalises *consolidation* as a paradigm-level operator (CLS-grounded; cf. [Xu et al. 2026](../source/xu-2026-agentic-memo.md)). The "consolidation" active stage here and the consolidation-channel concept are the same operation viewed from inside the Kyrja stack vs from the paradigm level. [EvoSC](../source/yu-2026-evosc.md) is the empirically-built instance at the soft-prompt-tuning depth (frozen base LLM); the active-stages framework predicts substrate-aware loss signals are required for true neocortical consolidation, which EvoSC does not provide. [Behrouz et al. 2026 (Nested Learning / Hope)](../source/behrouz-2026-nested-learning.md) reaches deeper rungs of the substrate-depth ladder via a frequency-stratified MLP chain and introduces the **optimisers-as-associative-memory** reframing (every gradient-based optimiser is a learned compressor of gradients) — this strengthens the active-stages claim that consolidation is structurally *a learned compressor*. Hope addresses **consolidation, forgetting, and updating** but **does not address curation** (no analogue of CLS replay-selection at write time); curation remains the framework's unaddressed active stage.
- [admission-control](./admission-control.md) — operationalises the *curation* stage; the four candidate training signals listed there overlap with this framework's RLVR-for-curation recommendation.
- [seven-layer integration stack](./seven-layer-stack.md) — six layers target the passive stages; admission-control is the lone active-stage layer.
- [H29 — edge-substrate-memory](../hypothesis/H29-edge-substrate-memory.md) — predicts where substrate-aware (and therefore active-stage-aware) memory first lands. Uses this framework as its operationalisation of "substrate memory."
- [H38 — rationale-trace-memory](../hypothesis/H38-rationale-trace-memory.md) — loop-level (depth 0-1) candidate mechanism for the *selection (curation)* and *consolidation* active stages. Asks whether summarised rationale traces transfer across tasks without weight updates. Sits explicitly inside the theorem-bounded regime ([Xu et al. 2026 CSC](../source/xu-2026-agentic-memo.md)) that substrate-aware approaches escape.

## Open questions

- **Operationalisation of "useful"** in the curation reward function: task success of downstream agent, answer quality, reduced re-derivation cost, reduced token count? Multiple candidates, each operationalises differently.
- **Temporal benchmark gap**: the MASQ benchmark is currently a *static corpus* (given query Q, which retriever wins?). Production has temporal dynamics (store at t1, query at t2 > t1+N). Benchmark needs extension before temporal credit-assignment policies can be trained against it.
- **Whether consolidation is genuinely self-supervised contrastive** at production scale, or whether the "same-fact" comparison signal degenerates to LLM-mediated judgment in practice.

## Source archive

Synthesized during the 2026-05-12 LLM curriculum + Kyrja design session. Grounded in:

- 2026-04-28 / 2026-05-11 LLM curriculum sessions covering retrieval-augmented architectures (kNN-LM, Memorizing Transformers, RETRO) and reasoning models / RLVR.
- AJ's own decomposition (memory pipeline + passive/active split) developed during the 2026-05-12 SSM/Mamba session.
- The grading exercise applying this framework to the three hybrid-frontier architectures (`project_llm_fundamentals.md` in project memory holds the working notes).

Not yet sourced to external literature — this is internal synthesis. Closest external precedent: Atkinson-Shiffrin three-stage memory model (encoding/storage/retrieval) as used in [LightMem](../incumbent/lightmem.md), though Atkinson-Shiffrin does not separate passive from active.

**2026-05-14 update: biological precedents now atomized for each active stage.** External grounding (added during cog-sci primary-source sweep):

- **Selection (curation)** ↔ [Yang et al. 2024 — selective replay](../source/yang-et-al-2024-selection-of-experience.md). Awake sharp-wave ripples are the neurophysiological tagging mechanism that selects experiences for sleep consolidation. The selection function itself remains under-specified.
- **Consolidation** ↔ [McClelland, McNaughton & O'Reilly 1995 — CLS](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) (mechanism) + [Tse et al. 2007 — schemas](../source/tse-et-al-2007-schemas.md) (rate-modulation by schema fit). The CLS framework supplies the *why* (catastrophic interference forces dual-system + interleaved learning); Tse 2007 supplies a 50-100× rate modulation when schemas are present. See [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) for the AI-translation hypothesis (per-candidate rate modulation).
- **Controlled forgetting / engram silencing** ↔ [Josselyn & Tonegawa 2020 — engrams](../source/josselyn-tonegawa-2020-engrams.md). The silent-engram concept (storage ≠ retrieval-handle availability) is the biological mechanism — engrams can be made retrieval-inaccessible without being deleted. No current AI system implements this. See [silent-engrams concept](./silent-engrams.md) and [H39 — silent-state primitives](../hypothesis/H39-silent-state-primitives.md) for the AI-translation hypothesis.
- **Updating** ↔ [Nader, Schafe & LeDoux 2000 — reconsolidation](../source/nader-schafe-ledoux-2000-reconsolidation.md). Memory retrieval creates a labile window during which the memory can be modified, strengthened, or silenced. The biological mechanism is the database-transaction analogue (retrieve = BEGIN TRANSACTION; commit = re-encode; rollback = silence).

**Retrieval-side primitive (not an active stage but adjacent):** [Howard & Kahana 2002 — TCM](../source/howard-kahana-2002-tcm.md) supplies a cog-sci anchor for *retrieval-cue construction* — a primitive distinct from the four active stages above but compositional with them. The framework's `finding` and `recalling` stages have been treated as passive (vector lookup, attention); TCM argues that the cue itself is a maintained, drifting, retrieval-updated vector. See [H41](../hypothesis/H41-temporal-context-retrieval.md) for the AI-translation hypothesis. Whether retrieval-cue construction should be promoted to a fifth active stage is open.

These atomizations move the framework's per-stage claims from internal synthesis to externally anchored. The training-signal taxonomy and temporal-credit-assignment story remain Kyrja-internal extrapolation.

The matrix of biological mechanisms × AI implementation status (covering 12 rows including the four active-stage precedents above) lives at [mechanism-gap-matrix](./mechanism-gap-matrix.md) and is the empirical anchor for path-decision diligence.
