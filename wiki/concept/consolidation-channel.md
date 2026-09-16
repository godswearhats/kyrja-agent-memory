---
type: concept
name: Consolidation channel
status: timeless
last_ingested: 2026-05-30
sources: [../source/xu-2026-agentic-memo.md, ../source/behrouz-2024-titans.md, ../source/hafner-2023-dreamerv3.md, ../source/lecun-2022-autonomous-mi.md, ../source/yu-2026-evosc.md, ../source/behrouz-2026-nested-learning.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/yang-et-al-2024-selection-of-experience.md, ../source/tse-et-al-2007-schemas.md, ../source/josselyn-tonegawa-2020-engrams.md, ../source/nader-schafe-ledoux-2000-reconsolidation.md, ../source/howard-kahana-2002-tcm.md, ../source/wayne-2018-merlin.md, ../source/redondo-morris-2011-stc.md, ../source/buzsaki-2015-spw-r.md]
epistemic_tags: [asserted, speculated]
tags: [substrate-memory, consolidation, cls, substrate-depth]
program: kerros
---

> **Program: [Kerros](./kerros.md) (assigned 2026-05-25).** This page is part of the substrate-memory research program. It is dense with product-era "wedge" / "Phase-3" / "Kyrja" language from 2026-05-13 → 05-20, preserved as chronicle. Read "wedge" as *research contribution* and "Phase-3 design" as *open research design question*. The consolidation channel is a candidate Kerros mechanism, not a commercial moat; its value is judged by the [integration gate](./kerros.md), not by market defensibility.

> **Status note (updated 2026-05-20):** The 2026-05-18 wedge sharpening reframed Kyrja's research target from "the consolidation channel as wedge" to **tier 3-4 retrieval as wedge** per [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — analogical and predictive retrieval. The consolidation channel's caddy instantiation is now precisely K2+T_A3 in [caddy-architecture](./caddy-architecture.md), formalized as falsifiable hypothesis [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md). Per [caddy-as-research-program](../decision/caddy-as-research-program.md) (2026-05-20), K2+T_A3 is an **active load-bearing T4 research target** alongside T_A1b (the representation pathway). The "Kyrja's named wedge as of 2026-05-13" language below is preserved for historical context; the consolidation channel is no longer *the* wedge, but it is one of two load-bearing pathways inside the caddy that deliver toward the tier 3-4 wedge.

> **Load-bearing input variable (added 2026-05-17):** The consolidation channel's policy operates on a **salience signal** that the field does not yet reliably compute. See [salience-signal](../open-question/salience-signal.md) for the upstream open question. The channel's architectural shape is largely a downstream choice from how salience gets computed — both STC-shape (token-bucket persistence with shared budget) and hot-store-with-promotion (explicit per-memory scoring at promotion time) stall on the same salience-computation bottleneck. See [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md) for the first falsifiable claim.

> **Off-line vs online surface distinction (added 2026-05-17, M16 walk):** The consolidation channel is the **off-line surface**. There is a complementary **online surface** — the runtime memory consultation that happens during generation, at whatever [retrieval-granularity](./retrieval-granularity.md) the caddy adopts. Biology operates both surfaces simultaneously (theta-mode during active behaviour for the online surface; SPW-R during sleep / quiet wakefulness for the off-line surface). The two are not in competition — they compose, doing different jobs. The consolidation channel pre-builds artifacts (consolidated representations, recombined fragments, abstracted gist); the online surface consumes them per-step during generation. AJ's framing: the choice of communication interface between caddy and golfer (online surface) shapes what work the caddy needs to do off-line (consolidation channel). See [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) for how the soft-composition interface choice on the online surface interacts with what the consolidation channel needs to materialise.

## Definition

The **consolidation channel** is the operator that moves information from a fast, episodic, exemplar-based store into slow, parametric, generalized representations — and back, when relevant context is needed. It is the bridge between the **database paradigm** (where memory lives in an external store the model queries) and the **substrate paradigm** (where memory lives in the model's weights, state, or generative dynamics).

The concept is grounded in **Complementary Learning Systems** ([McClelland, McNaughton & O'Reilly 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md), atomized 2026-05-14): biological memory uses a fast hippocampal exemplar store plus a slow neocortical rule-extracting consolidator. Either alone is broken. The agentic-memory field has implemented only the fast side; the consolidation channel is the missing piece. See [complementary-learning-systems](./complementary-learning-systems.md) for the cognitive-science grounding.

## Why this concept exists as its own page

The consolidation channel is **Kyrja's named wedge** as of 2026-05-13. The substrate-survey identified that:

1. Every paradigm-level paper assumes consolidation happens but does not specify *how* it happens for a personal-assistant context `[ASSERTED]` ([source](../source/xu-2026-agentic-memo.md)).
2. No agentic-memory *product* implements a true neocortical-side consolidation channel — they all operate at the [kNN-LM](../source/khandelwal-2020-knn-lm.md) 2020 baseline or worse `[ASSERTED]`. A research prototype, [EvoSC](../source/yu-2026-evosc.md), implements the dual-store architectural pattern but at the *soft-prompt-tuning depth* — base LLM weights remain frozen.
3. The closest published mechanism that touches weights is **Skill-SD** (Wang 2026, cited by [Xu et al.](../source/xu-2026-agentic-memo.md)) which compresses trajectories into natural-language skills and distils into student weights — but it requires a privileged-teacher oracle that doesn't exist in personal-assistant deployment `[ASSERTED]`.

The page exists because the concept is referenced by the substrate-paradigm sources, by [H29](../hypothesis/H29-edge-substrate-memory.md) and [H37](../hypothesis/H37-pluggable-substrate.md), and anchors a core Kerros research direction.

## The operator shape

At minimum the consolidation channel takes:

- **Input.** Episodic traces (interaction logs, retrieved memories, or in-context observations).
- **Process.** Compression into a representation suitable for parametric storage — natural-language skill summary (Skill-SD), latent state ([world models](../source/ha-schmidhuber-2018-world-models.md)), or gradient update ([Titans](../source/behrouz-2024-titans.md), [TTT](../source/sun-2024-ttt.md)).
- **Output.** A parametric update — weight delta, persistent latent, or distilled student model.

The differentiator across implementations is *when* consolidation happens (offline batch vs online during inference) and *what* triggers it (loss surprise as in Titans, scheduled as in Skill-SD, dream-driven as in DreamerV3's imagination).

> **Lens to explore (2026-05-30, `[SPECULATED]`, exploratory — don't overindex):** frame consolidation as **credit assignment, not compression**. The hard part of the write isn't shrinking episodes — it's the *signal* for *which* structure deserves to change `θ` (the toy task had labels; real session memory doesn't). That signal is what RL supplies (reward / surprise → what's worth writing), which is why the weight-integration-from-experience work lives in the RL community. Connects the *what-triggers* axis to [Titans](../source/behrouz-2024-titans.md)' surprise-gating and [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md)'s schema-fit. The cost of this write side is what the [incremental-integration-cost](../open-question/incremental-integration-cost.md) trade-off prices.

## Substrate-depth ladder

Beyond *when* and *what triggers*, a third design axis is **how deeply into the substrate** the consolidation channel modifies the model. This axis is novel synthesis from the 2026-05-14 read of [EvoSC](../source/yu-2026-evosc.md) and is `[SPECULATED]` as a Kyrja-internal framework — not externally proposed in those terms.

The ladder, from shallowest to deepest:

| Depth | What changes | Frozen `θ`? | Example | Strictness under [Xu's CSC theorem](../source/xu-2026-agentic-memo.md) |
|---|---|---|---|---|
| 0 — Text retrieval | Stored exemplars + retrieval policy | Yes | [kNN-LM](../source/khandelwal-2020-knn-lm.md), HippoRAG | Theorem bites with full force; `ᾱ < 1` applies |
| 1 — Text summarisation | Stored *abstractions* of exemplars | Yes | A-MEM, AWM, TER | Theorem still applies; smarter prompts, same frozen LLM |
| 2 — Soft prompt tuning | Learned continuous prefix (small) | Yes | [EvoSC](../source/yu-2026-evosc.md) `P_θ` (20 tokens) | Theorem still applies in principle; soft prompts route inputs differently but don't change `θ` |
| 3 — Adapter / LoRA | Small low-rank `θ` delta on attention layers | Partially (small delta) | LoRA-based fine-tuning, [Titans](../source/behrouz-2024-titans.md)'s internal-state updates | Theorem partially escaped; gap narrows |
| 4 — Targeted weight edit | Surgical knowledge insertion (e.g., MEMIT, ROME) | Partially (targeted) | MEMIT, ROME, knowledge editing | Theorem escaped for edited concepts; locality varies |
| 5 — Full fine-tune / distillation | Whole-model `θ` update from trajectory data | No (modified) | Skill-SD distillation, full FT | Theorem fully escaped; full neocortical consolidation |

`[SPECULATED]` Two implications follow from this ladder:

- **Most "agentic memory" innovation lives at depths 0-1.** A-MEM, HippoRAG, Mem0, Zep, LightMem all sit here. The empirical leaderboard for "agentic memory benchmarks" measures who's best within depths 0-1.
- **The Kyrja wedge proposes moving up the ladder.** The interesting open question is not *whether* deeper consolidation works (Xu's theorem says it must for compositional novelty) but *what depth is cost-effective* for personal-assistant dialogue. The empirical question Phase 3 should pose: how much of the compositional gap closes per ladder rung?

The substrate-depth choice interacts with the trigger choice and the representation choice — not all combinations are coherent. (Soft prompts can't easily encode "a single new fact"; targeted weight edits can't easily encode "an entire trajectory style.")

### First empirical data on the per-rung question (2026-05-28)

`[MEASURED]` The ladder's load-bearing open question — *"how much of the compositional gap closes per ladder rung?"* — got its first data point from the factored-operator [Gate-2 write experiment](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md). It also exposes a rung the ladder above omits: an **embedding-row-only write** (freeze the whole transformer, train only the new symbol's input-embedding row) sits *below* LoRA — call it **rung ~2.5: input-representation edit**, the shallowest possible parametric write.

The result: this shallowest write **fails to consolidate cheaply.** Adding new symbols to a model already competent at the operator, it fit the training examples perfectly (loss→0) but did **not** generalise to held-out pairs (few-shot stuck at chance), with retention exact. Diagnosis: **underdetermined in parameter space** — the data was information-sufficient, but an 896-d embedding row of which only ~4 directions matter has too many free directions to recover the true factor vector without a low-rank prior. `[SPECULATED]` Implication for the channel's write side: a cheap consolidation write likely needs to target a **learned low-rank write-subspace** (a "write head" derived once from the base), not naive full-dimension SGD on the new representation. This is the in-weights analogue of MEGa's (line below) gated-LoRA-distillation direction, approached from the cheapest rung up. Whether the low-rank write recovers few-shot generalisation is the pending decider in [incremental-integration-cost](../open-question/incremental-integration-cost.md) — the question of whether deep consolidation is cheap enough to count as *memory* rather than *training*.

## Frequency axis — depth is not one-dimensional

The substrate-depth ladder above treats depth as a single design choice per architecture. The 2026-05-14 read of [Behrouz et al. 2026 (Nested Learning / Hope)](../source/behrouz-2026-nested-learning.md) revealed this framing is incomplete: Hope occupies *multiple rungs simultaneously* at different update frequencies. `[SPECULATED]` Kyrja-internal synthesis.

Specifically (verbatim §7.1 of Behrouz et al.): *"the parameters of ℓ-th MLP block, i.e., θ^(f_ℓ), are updated every C^(ℓ) steps"* — Hope's Continuum Memory System is a chain of MLP blocks each operating at a different frequency. A high-frequency block is effectively at rung 2-3 (transient parametric update), a low-frequency block at rung 5 (full fine-tune at training time). The Transformer is the special case `k=1, frequency=0`.

This makes the design space **two-dimensional**: `(depth, frequency)`. The same architectural shape that exists in CLS biology (fast hippocampal write + slow neocortical consolidation) is not a binary tier but a continuum of (depth, frequency) pairs.

| Architecture | Depth | Frequency | Notes |
|---|---|---|---|
| [kNN-LM](../source/khandelwal-2020-knn-lm.md) | 0 | N/A (no parametric write) | Database-paradigm; theorem bites |
| [EvoSC](../source/yu-2026-evosc.md) `P_θ` | 2 | per-domain (low) | Frozen base; depth-2 / batched |
| [Titans](../source/behrouz-2024-titans.md) test-time updates | 3 | per-token (high) | Substrate-depth ladder rung 3 at high frequency |
| MEMIT-style edits | 4 | per-edit (sparse) | Surgical, low-frequency persistent |
| Skill-SD distillation | 5 | per-batch (low, offline) | Full FT at scheduled cadence |
| Hope inner (self-mod Titans) | 2-3 *transient* | per-token (high) | Writes don't persist past context |
| Hope outer (CMS) | 5 | multi-frequency continuum | The frequency-stratified design space |

`[SPECULATED]` Implication: Kyrja's consolidation-channel design should specify *both* coordinates, not just depth. A single (depth=5, frequency=monthly) channel may be wrong if the right answer is a chain of (depth=2, frequency=per-session) + (depth=5, frequency=quarterly). Phase 3 should sketch the frequency-spectrum explicitly.

## Hot store as training-data source for the cold store (M11 reframing)

`[ASSERTED]` AJ surfaced (2026-05-15, mid-M11 walkthrough) a tighter framing for what the consolidation channel actually does: the hot store is the **training-data source** for the cold store, not just a temporary buffer.

McClelland's 1995 framing said cortex learns from hippocampal replay. AJ's restating says the same thing more sharply: cold storage's structure is *determined entirely by what gets replayed, in what order, at what rate.* The hot store isn't a way-station; it's the generator of the training distribution. Three observable consequences follow.

### Non-standard training data properties

`[ASSERTED]` Biological replay violates every assumption standard ML training rests on:

| Standard ML assumption | Biological replay reality |
|---|---|
| Fixed dataset, defined at training start | Open-world; new experiences arrive continuously |
| i.i.d. sampling within the dataset | Non-i.i.d.; replay is structured by hot-store contents, salience ([M04](./mechanism-gap-matrix.md)), schema-fit ([M05](./mechanism-gap-matrix.md)), reverse-replay |
| Determinism given seed + data + architecture | Non-reproducible; replay selection is stochastic, hot-store contents drift continuously |
| Closed-world (the dataset is complete) | Trajectory-shaped; cortex's state is the result of a *path* through replay sessions, not optimisation over a corpus |

`[SPECULATED]` Three implications for a caddy:

1. **The model is genuinely non-reproducible.** Each instance evolves uniquely along its trajectory. Feature for personalisation; bug for debugging/auditing. Standard ML eval methodology breaks against systems whose state drifts continuously with usage.
2. **Training/inference distinction collapses.** Every retrieval is potentially a learning event (cross-link [reconsolidation / M10](./mechanism-gap-matrix.md)). The clean ML separation of "training time" and "inference time" doesn't exist in biology and may not exist for a biology-faithful memory model.
3. **The "frozen snapshot" deployment model is the alien thing, not biology.** ML's standard practice — train once, deploy forever — is the unusual choice when compared against any system that has to live in a changing world.

### Temporal compression as an engineering target

`[ASSERTED]` Sharp-wave ripple replay achieves ~100× temporal compression — a ~10-second trajectory replays in ~100ms during a ripple. AJ's observation: **this is tractable in an agentic setting.** Activities take place over hours during agent operation; the hot store accumulates them; during downtime (e.g. overnight) the system fires them all through the cold-store training pipeline at processing speed. The 100× ratio drops out of the throughput difference between waking-experience pace and offline-processing pace.

`[SPECULATED]` Caveat noted by AJ: the *exact shape and format* of the replay batch is the novel research area, and it may turn out to be unreachable. Specifically: what does the cold store consume? Token sequences? Compressed event representations? Cognitive-map coordinates (see [[cognitive-maps-and-conjunctive-coding]])? The compression itself is the easy part; the *representation* of what gets compressed is the open design problem.

### Reverse replay as automatic credit assignment

`[ASSERTED]` Foster & Wilson 2006 (Nature 440:680-683) showed reverse replay specifically follows salient events (most prominently reward). The replay runs *from the outcome backwards* through the immediately preceding trajectory. Cog-sci interpretation: this is credit assignment — propagate the value of the outcome back to the actions that produced it. The biological analogue of temporal-difference learning's eligibility traces (Sutton 1988).

`[SPECULATED]` Engineering re-framing (AJ's, 2026-05-15): **reverse replay = automatic distributed tracing on the memory store.** When something salient happens (positive or negative outcome), replay the preceding state sequence in reverse to construct a causal trace. Engineering teams do this manually with logs and traces; biology has it built into the consolidation channel.

The consequence for a caddy: if reverse-replay-on-salience is implemented as a write-path primitive, the module emits **causal traces as a structural property of the architecture** — outcomes get automatically linked to their precursors during consolidation, no hand-coded annotation pass required. No current bolt-on memory product does this. The information (which earlier events led to this outcome) is information no current system produces, generated by a mechanism biology has been refining for ~hundreds of millions of years.

### M10 / M11 as possibly the same mechanism

`[SPECULATED]` Working observation from the M11 walkthrough (2026-05-15): [reconsolidation (M10)](./mechanism-gap-matrix.md) and the interleaved consolidation of M11 may be the same underlying mechanism operating at different timescales. Both involve labile-then-stable transitions; both depend on the same replay/ripple substrate; both are triggered by retrieval or replay-event onset.

If they unify, "consolidation" isn't a discrete event but a **continuous re-stabilisation process** that fires every time a memory is retrieved (M10 micro-scale) or every time the hot store is offline-replayed (M11 macro-scale). Sleep would just be the high-bandwidth batched version of what reconsolidation does at sub-second scale during use.

AJ noted from a distributed-systems angle: this unification has software analogues (transaction-with-lease semantics where the lease can be of varying length depending on whether you're in interactive operation vs offline batch). The exact-same-mechanism reading is consistent with this.

Status: working observation, not load-bearing for any current design decision. Flagged for development in subsequent matrix walk passes. If the unification holds, several of the matrix's row-by-row separations collapse into a single architectural primitive.

**Update 2026-05-26 (integration-gate decision):** this unification is *not* imported into the channel's design. Per [integration-gate § Exclusions](./integration-gate.md), **M10 (reconsolidation) is out of scope for Kerros** — per-memory rewrite-on-retrieval is a feature for biology, a bug for software (drift, evil² amplification, lost inspectability). The consolidation channel writes *structure into θ* (**consolidation**); it does **not** rewrite episodes on retrieval (**reconsolidation**). This explicitly declines the refinement the [Nader source](../source/nader-schafe-ledoux-2000-reconsolidation.md) suggested (folding a retrieval-triggered update window into the channel), and the *"every retrieval is a learning event"* / transaction-lease framing above is preserved as chronicle, not adopted as a design commitment. **Consolidation ≠ reconsolidation.**

### M11 / M12 as possibly the same architectural commitment, viewed two ways

`[SPECULATED]` Parallel observation surfaced during the 2026-05-16 M12 walkthrough. [Catastrophic-interference avoidance via interleaved learning (M11)](./mechanism-gap-matrix.md) and [quasi-regular handling (M12)](./mechanism-gap-matrix.md) are catalogued as separate mechanisms but may be **two observational windows on the same architectural commitment**: maintaining two systems with different learning rates with a consolidation operator between them. M11 names *why the architecture is forced* (interference avoidance under joint pressure for generalisation and exemplar fidelity); M12 names *what the architecture enables* (handling quasi-regular domains where rules and exceptions must coexist).

Combined with the M10/M11 unification observation above, the matrix walk has produced two hints that the 13 rows are not independent: M10/M11 may be one mechanism at different timescales, and M11/M12 may be the same architectural commitment seen from two angles. If a third unification surfaces in the M14-M17 reads, the catalogue framing of the matrix may need supplementing with a primitive-set page: a smaller set of architectural primitives whose interactions produce the observable matrix rows.

Candidate primitive set from the walk so far: discrete addressable units (M01-M02-M06 substrate); separate fast/slow representations with different learning rates (M01-M02-M03-M11-M12 thread); salience-modulated plasticity (M04-M05-M09 thread); consolidation operator moving information between tiers (M03-M07-M10 thread). Status: not load-bearing now; flagged for development if a third unification surfaces in M14-M17 or if a Kyrja design decision turns on the primitive-set framing.

### M13 as the read-side complement to the consolidation channel

`[ASSERTED]` The 2026-05-16 M13 walkthrough confirmed that M13 ([temporal context as retrieval primitive](./mechanism-gap-matrix.md)) is the first explicitly *read-side* primitive in the matrix. Everything M01-M12 is write-side or storage-side: encoding, consolidation, allocation, interference avoidance, reconsolidation, quasi-regular handling. M13 is the first row about *how memories are cued at retrieval time*, with a maintained context vector that updates on retrieval and biases subsequent retrieval.

The consolidation channel is write-side; H41's drifting context vector is read-side; they compose. The context vector at retrieval time could itself be a consolidation signal (which traces co-activated in current context get consolidated together) — possible coupling between the read-side and write-side primitives that has not been specified in current TCM-flavoured proposals. Open design question for Phase 3 if the caddy investigation crystalises into a recipe.

Open question for the matrix as a whole: **are there other read-side primitives the matrix is missing?** M13 was promoted from a candidate row 2026-05-14; the prior 12 rows were all write/storage-side. Candidate read-side mechanisms to screen for in future ingest passes: pattern-completion-as-retrieval (Modern Hopfield, Krotov 2020); cue-driven activation of silent engrams ([M06](./mechanism-gap-matrix.md), differs from M13 in being storage-side awakening rather than read-side cuing); reconstructive retrieval (the Schacter & Addis 2007 candidate row M16, currently abstract-scanned).

## Why the consolidation channel needs both stores (the integration argument)

| Property | Episodic-only (RAG++) | Parametric-only (fine-tune) | Consolidation channel |
|---|---|---|---|
| Novel exemplar recall | Strong | Weak | Strong (via episodic side) |
| Compositional transfer | Weak `[ASSERTED]` ([source](../source/xu-2026-agentic-memo.md)) | Strong | Strong (via parametric side) |
| Online updateability | Strong | Weak | Strong |
| Cost per query | Low (lookup) | Zero (no retrieval) | Mixed (hot/cold tiering) |
| Cross-session continuity | Limited (store grows unboundedly) | Limited (catastrophic forgetting) | Targeted (compress + forget per channel) |

A personal-assistant agent that talks to one user over months needs *both* sides. Episodic exemplars for "what did I say last Tuesday" recall; parametric consolidation for "what kind of person is this user, how do they like to be communicated with" generalization. The consolidation channel is the operator that makes the dual-store architecture work `[SPECULATED]`.

## Open design questions

These are the load-bearing design questions for the Kerros consolidation mechanism:

- **Online vs offline regime.** Gradient-coupled online ([Hope](../source/behrouz-2026-nested-learning.md) shape, stage-1-only), batched offline distillation (Skill-SD shape), or selective-replay (biological / [Yang et al. 2024](../source/yang-et-al-2024-selection-of-experience.md) shape, no existing implementation)? Load-bearing design fork; see [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md).
- **Trigger.** Surprise-driven ([Titans](../source/behrouz-2024-titans.md)-style gradient-as-loss), schedule-driven (daily/weekly batch), or capacity-driven (when episodic store crosses a threshold)? See [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md).
- **Representation.** Natural-language skill (Skill-SD), structured slot ([slot-format-encoding](../decision/slot-format-encoding.md)), latent vector ([V-JEPA-style](../source/lecun-2022-autonomous-mi.md)), or gradient ([Titans](../source/behrouz-2024-titans.md))?
- **Substrate locus / depth + frequency.** Where does the consolidated representation land on the [substrate-depth ladder](#substrate-depth-ladder) — soft prompt prefix (depth 2, [EvoSC](../source/yu-2026-evosc.md)), sidecar adapter (depth 3), targeted weight edit (depth 4, MEMIT-style), or full fine-tune (depth 5, Skill-SD-style)? *And at what frequency* — per-token, per-session, scheduled cadence? Each `(depth, frequency)` pair has different cost, locality, persistence, and reversibility properties. See [Frequency axis](#frequency-axis--depth-is-not-one-dimensional) above and [Hope's CMS](../source/behrouz-2026-nested-learning.md) for the continuum framing.
- **Forgetting.** What does the channel evict from the episodic store after consolidation, and what does it preserve? See [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md).
- **Reward signal.** How does the channel know it consolidated well? See [rl-target-encoding-vs-consolidation](../open-question/rl-target-encoding-vs-consolidation.md) for the narrower "where do we spend RL budget" framing of this question.

## Scope limits

- The consolidation channel is *one operator* in the substrate paradigm, not the whole paradigm. It does not subsume selection, retrieval, or active-stage updating. See [active-stages-framework](./active-stages-framework.md).
- "Consolidation" in this concept page refers to the **CLS-grounded operator** that moves information between storage tiers. The narrower sense — merging redundant exemplars within a single vector store — is the [LightMem](../incumbent/lightmem.md)-style operation and is covered separately by [rl-target-encoding-vs-consolidation](../open-question/rl-target-encoding-vs-consolidation.md).
- The concept does not commit Kerros to any specific consolidation recipe. The recipe is an open research design question.

## Related

- [substrate-as-memory](./substrate-as-memory.md) — paradigm in which the consolidation channel lives
- [substrate-paradigms](./substrate-paradigms.md) — P1/P2/P3 architectures the channel can be built across
- [active-stages-framework](./active-stages-framework.md) — consolidation is one of four active stages
- [mechanism-gap-matrix](./mechanism-gap-matrix.md) — row M03 names the consolidation channel as Kyrja's primary wedge; the matrix is the broader catalogue of biological mechanisms × AI implementation status
- [silent-engrams](./silent-engrams.md) — silent-state transitions are the mechanism by which the hippocampal trace persists during cortical migration; refines the McClelland 1995 "trace decays" assumption
- [cognitive-maps-and-conjunctive-coding](./cognitive-maps-and-conjunctive-coding.md) — what biological replay carries: cognitive-map coordinates with conjunctive binding, not just raw event sequences. Refines the "what does the consolidation channel transport" question; surfaced from the M11 walkthrough 2026-05-15.
- [H39 — silent-state primitives](../hypothesis/H39-silent-state-primitives.md) — three-state memory architecture (available/silent/absent) as a Kyrja design alternative
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — per-candidate rate modulation as a Kyrja design alternative; extends the (depth, frequency) design space
- [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md) — read-side complement to the (write-side) consolidation channel: a maintained context vector updated by retrieval, distinct from but compositional with the channel's write-side operator
- [Howard & Kahana 2002 (TCM)](../source/howard-kahana-2002-tcm.md) — cog-sci anchor for the retrieval-cue primitive that complements the consolidation operator
- [Yu et al. 2026 (EvoSC)](../source/yu-2026-evosc.md) — most directly comparable prior art; soft-prompt-tuning depth (ladder rung 2)
- [Wayne et al. 2018 (MERLIN)](../source/wayne-2018-merlin.md) — worked precedent for the channel's write-side objective being shaped by a **non-task auxiliary loss** (the MBP / variational world-model objective) rather than by the consumer's task loss. The LLM-era retrieval-augmented descendants ([RETRO](../source/borgeaud-2022-retro.md), [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md)) inherited MERLIN's read head but dropped the MBP — the [MBP-was-dropped hypothesis](../open-question/memory-caddy.md) flagged as the sharpest open question in the caddy space.
- [caddy-architecture](./caddy-architecture.md) — detailed architectural specification (2026-05-17); the channel's K1-K5 ops (sampling, schema-fit modulation, reverse-replay, trajectory curriculum, decay) are decomposed there as the consolidator's operations. K2+T_A3 is an active load-bearing T4 research target alongside T_A1b per [caddy-as-research-program](../decision/caddy-as-research-program.md).
- [caddy-as-research-program](../decision/caddy-as-research-program.md) — 2026-05-20 decision: caddy is a research program; K2+T_A3 is load-bearing.
- [k2-ta3-deferred-to-v2](../decision/k2-ta3-deferred-to-v2.md) — REVERSED 2026-05-20. Historical record of the 2026-05-19 MVP-product-scope deferral.
- [H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the channel's falsifiable form.
- [Behrouz et al. 2026 (Nested Learning / Hope)](../source/behrouz-2026-nested-learning.md) — implements *stage-1-only* online consolidation via frequency-stratified MLP chain; reveals the (depth, frequency) 2D design space
- [Xu et al. 2026](../source/xu-2026-agentic-memo.md) — names the consolidation channel architecturally; provides CSC theorem motivation
- [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md) — load-bearing design fork surfaced by Hope's stage-1-only framing
- [rl-target-encoding-vs-consolidation](../open-question/rl-target-encoding-vs-consolidation.md) — narrower question about RL budget allocation for the consolidation operator
- [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md) — ordering hypothesis for the consolidation operation
- [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) — forgetting half of the consolidation channel
- [procedural-memory-alternative](../open-question/procedural-memory-alternative.md) — procedural skill ≈ consolidated behavioural trace
- [H38 — rationale-trace-memory](../hypothesis/H38-rationale-trace-memory.md) — loop-level (depth 0-1) consolidation alternative: summarise `Thought` tokens from agent trajectories as cross-task memory without weight updates. Sits inside the theorem-bounded regime; named here as the non-substrate counterpart to deeper-ladder consolidation paths.
- [norman-rubric](./norman-rubric.md) — externally-defined evaluation framework (Dong/Lu/Norman/Michelmann 2025, TiCS); Norman's Outstanding Question 2 explicitly names the consolidation channel as the missing piece in current MA-LLMs (*"EM is used to train semantic memory through a process of consolidation"*); the channel is what Norman et al. say MA-LLMs need.
- [Spens & Burgess 2024](../source/spens-2024-hippocampal-rag.md) — closest existing published implementation of replay-driven consolidation at academic scale; Mistral-7B as neocortex trained on replayed hippocampal traces. Bolt-on/substrate hybrid, not caddy, but derisks the cog-sci-to-neural-memory transfer.
- [MEGa (Pan et al. 2025)](../source/pan-2025-mega.md) — in-weights CLS-grounded variant; their stated future work (rehearsal-driven distillation of gated LoRA into base weights) is exactly the consolidation channel operator design, from the in-weights side.

## Source archive

Substrate survey: `xu-2026-agentic-memo.md` (CLS framing, Theorem 1, Skill-SD reference).
