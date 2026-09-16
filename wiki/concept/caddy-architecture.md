---
type: concept
name: Caddy architecture — six-component sketch with thirty operations, tier-labeled
status: living
last_ingested: 2026-05-25
sources: [../source/wu-2022-memorizing-transformer.md, ../source/fountas-2024-em-llm.md, ../source/dong-2025-norman-episodic.md, ../source/borgeaud-2022-retro.md, ../source/wayne-2018-merlin.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, architecture, design-specification, research-program]
---

## Definition

`[ASSERTED]` The **caddy architecture** is the first detailed architectural specification of the [caddy](./caddy.md) concept — a six-component decomposition (encoder, store, consolidator, retriever, integration interface, golfer) plus three cross-cutting concerns (training loop, lifecycle layer, salience signal). Each component decomposes into discrete operations; each operation is tier-labeled by implementation feasibility (T1 proven at LLM scale → T4 speculative); and the research-prototype subset identifies what's needed to demonstrate the architectural pattern and beat EM-LLM's 2.5/5 Norman-rubric ceiling.

Post-reconciliation total: 30 operations, with **two active load-bearing T4 research targets**: T_A1b (auxiliary world-model loss on memory representations) and K2+T_A3 (schema-fit-modulated consolidation with continuous drift). Per [caddy-as-research-program](../decision/caddy-as-research-program.md) (2026-05-20), the caddy is a research program; both T4s are active load-bearing targets, ordered into a stack-ranked research backlog rather than partitioned into "MVP-critical-path" vs "v2-deferred." Ordering is set by the stack-rank exercise (forthcoming) using scientific leverage, tractability, dependencies, and frontier-pacing as criteria — anchored to "moves us toward demonstrating tier 3-4 retrieval via the caddy." **Flag (2026-05-25):** whether tier 3 is a capability distinct from tier-2 semantic retrieval is under review after the [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) (bag-of-words decodes the arc patterns at 82%); see [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md).

This page exists because the architecture is referenced by [caddy](./caddy.md), [memory-caddy open question](../open-question/memory-caddy.md), [consolidation-channel](./consolidation-channel.md), and [discrete-unit-memory-architecture](./discrete-unit-memory-architecture.md). It has its own status lifecycle — the architecture is empirically falsifiable independently of the caddy concept's broader validity.

Companion pages: [caddy-interface-doors](./caddy-interface-doors.md) (D/U/Q door framework for integration), [caddy-memory-representation-spectrum](./caddy-memory-representation-spectrum.md) (deferred decision: preconfigured vocab vs learned reps), [caddy-tier-semantics](./caddy-tier-semantics.md) (deferred decision: N-tier mapping to silicon).

## The six-component sketch

```
                  ┌──────────────────────────────────┐
                  │  EXPERIENCE STREAM               │
                  │  conversation turns, tool I/O,   │
                  │  observed events, results        │
                  └──────────────┬───────────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────────┐
                  │  GOLFER (LLM, ~70B-class)        │
                  │  forward pass, reasoning,        │
                  │  output generation               │
                  └─────┬──────────────────────┬─────┘
                        │                      ▲
                  [write path]            [read path]
                        │                      │
                        ▼                      │
   ┌────────────────────────────────────────────────────────┐
   │  CADDY (sidecar)                                       │
   │                                                        │
   │  ┌─────────────┐    ┌─────────────┐    ┌────────────┐  │
   │  │ (1) ENCODER │───▶│ (2) STORE   │───▶│(4)RETRIEVER│  │
   │  │ select +    │    │ memory      │    │ cue-       │  │
   │  │ represent   │    │ state       │    │ completion │  │
   │  └─────────────┘    │ N tiers     │    └─────┬──────┘  │
   │                     │ (N≥2)       │          │         │
   │                     └──────┬──────┘          │         │
   │                            │                 │         │
   │                            ▼                 │         │
   │                   ┌──────────────────┐       │         │
   │                   │(3) CONSOLIDATOR  │       │         │
   │                   │ offline: schema  │       │         │
   │                   │ fit, rehearsal,  │       │         │
   │                   │ forgetting,      │       │         │
   │                   │ composition      │       │         │
   │                   └──────────────────┘       │         │
   └───────────────────────────────────────────────┼────────┘
                                                  │
                                                  ▼
                  ┌──────────────────────────────────┐
                  │  (5) INTEGRATION INTERFACE       │
                  │  how caddy output reaches golfer │
                  │  forward pass: tokens? cross-    │
                  │  attn? activations? weights?     │
                  └──────────────────────────────────┘

   CROSS-CUTTING:
   (A) TRAINING LOOP   — co-training regime, loss surfaces, frozen vs
                         updatable, auxiliary objectives
   (B) LIFECYCLE LAYER — per-user, versioning, hot-swap, multi-tenancy,
                         privacy boundary (prototype-dropped; production concern)
   (C) SALIENCE SIGNAL — learned scalar/vector function s(item, context,
                         history) consumed by encoder, consolidator,
                         and retriever ops
```

The six components map approximately to: **encoder** (write-path admission and representation), **store** (persistent state across N tiers), **consolidator** (offline transformation and composition), **retriever** (read-path cue-matching), **integration interface** (how caddy output reaches the golfer's forward pass), **golfer** (the LLM consumer).

`[ASSERTED]` AJ confirmed the box-level decomposition 2026-05-17 after architectural interrogation: every question raised was answerable inside one of these six boxes plus three cross-cutting concerns, confirming the decomposition captures the architectural surface.

## The M17 architectural inversion (the wedge claim)

`[ASSERTED]` Current memory systems (Mem0, Letta, Zep, Cognee, LightMem) concentrate intelligence at the admission gate: heavy salience computation runs at write-time, with light or absent forgetting downstream. M17 ([active forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md)) inverts this: biology admits liberally during attended events, then concentrates intelligence at offline forgetting policy. The caddy commits to the M17 inversion.

**The hypothesis this commits to.** The plausible reason no published memory system scores ≥3/5 on the [Norman rubric](./norman-rubric.md) is that they all gate at write-time and don't forget intelligently. The post-Norman gap (eleven months, no system above 2.5/5) may be the cumulative consequence of this inversion not being in the design space. The caddy's wedge is committing to it.

**Three architectural consequences:**

1. **The encoder lightens to admit-all-discrete-events.** The heavy salience computation that selective gating would do online is deferred to consolidator-side ops where context is richer. Surprise-based event segmentation remains the only filter; *within* an event, admission is permissive by default.

2. **The consolidator gains salience-modulated decay.** Decay rate becomes a function of a named salience-signal primitive, not "did this get replayed." This is where intelligent forgetting actually lives.

3. **Hot and cold storage tiers do structurally different jobs, and the consolidator becomes the most architecturally load-bearing component.** Hot is the promiscuous-admit tier (transient, large, mostly destined to be forgotten). Cold is the consolidated tier (small, schema-fit, persistent). The consolidator decides what graduates — making consolidation primary, not auxiliary.

**Storage profile.** The shift from "selective-encode + dumb-forget" (small steady-state) to "promiscuous-encode + smart-forget" (growing-then-pruning) requires the consolidator's pruning rate to keep up with the encoder's admission rate. If it does, the store stabilises at a bounded equilibrium; if not, it grows unbounded.

This is a constraint we share with biology — disk/RAM costs map onto biology's metabolic costs — so biology's solution-shape (intelligent decay) is mechanism-relevant, not just inspirational. Per the [[feedback_inspiration_not_blueprint]] shared-constraint clause: when biology's constraint maps onto ours, biology's solution-shape transfers.

**Why the salience signal becomes load-bearing here.** Both intelligent decay and schema-fit consolidation depend on the same upstream input: a learned function quantifying memory value. The inversion makes the named primitive structurally essential, not merely a tidiness improvement. Without it, the consolidator has nothing to be smart with, and the inversion collapses.

**Doc-stage scope impact (per [[feedback_mvp_doc_not_mvp]]).** The inversion doesn't meaningfully change *what we build*. Same components, same ops. What changes is which ops carry the intelligence, and which load-bearing primitive the system routes through. Cheap to do at doc stage, expensive to retrofit after building.

The op-level instantiation of this inversion (E2 light admission, K5 salience-modulated decay, C salience signal cross-cutting primitive) is laid out in the operations tables below.

## Thirty operations, tier-labeled

`[ASSERTED]` Each component decomposes into discrete operations. Each operation is tier-labeled:

- **T1** — Proven at LLM scale (shipped in a paper or product)
- **T2** — Demonstrated at small/adjacent scale (works in toy regimes or related domains)
- **T3** — Principled but untested in this configuration (building blocks exist; not composed this way)
- **T4** — Speculative (believed on theory/biology; no engineering corroboration)

### (1) Encoder

| Op | Description | Tier | Anchor |
|---|---|---|---|
| E1 | Surprise-based event boundary detection | T2 | [EM-LLM](../source/fountas-2024-em-llm.md); Norman N2 |
| E2 | Light admission within E1-segmented events (default: admit all; selectivity TBD) — heavy salience computation deferred to K-side | T2 | M17 "encode promiscuously" inversion |
| E3 | Conjunctive representation (what×where×when×salience×context) | T3 | M11 cog-maps |
| E4 | Commit representation with temporal-context binding | T3 | TCM; Norman N4 |

### (2) Store

| Op | Description | Tier | Anchor |
|---|---|---|---|
| S1 | Discrete addressable units across N tiers (N≥2; prototype N=2; tier semantics deferred — see [[caddy-tier-semantics]]). Each unit is **multi-field**: `event_rep` + `raw_content` + `trajectory_state` per [multi-field-memory-unit decision](../decision/multi-field-memory-unit.md) | T1 | Vector DBs, KV stores — production |
| S2 | Silent state larger than read interface | T2 | MERLIN, Hopfield; C1 silent-engram |
| S3 | Incremental addition without catastrophic interference | T2 | [MEGa](../source/pan-2025-mega.md) at Llama-3.1-8B |
| S4 | Modification post-write (reconsolidation) | T3 | ROME/MEMIT for in-weights; Norman N1 |
| S5 | Drifting temporal context vector across writes | T3 | TCM / successor representation |
| S6 | Explicit consolidation success/failure signal | T1 | Family precondition; eBay patent precedent |

### (3) Consolidator (offline)

| Op | Description | Tier | Anchor |
|---|---|---|---|
| K1 | Sample hot-store items as training distribution for cold store | T3 | M11 reframing #1 (hot-store-as-training-data) |
| K2 | Tier promotion: schema-fit-modulated (any tier → next-warmer); cold-promotion is the load-bearing case. **Active load-bearing T4 research target** alongside T_A1b — see [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md). Ordering vs. T_A1b set by stack-rank | T4 | Tse 2007 schema in biology; no engineering analog |
| K3 | Reverse-replay on salience for credit assignment | T3 | RL credit-assignment + M11 reverse-replay reframing |
| K4 | Non-iid trajectory-shaped curriculum | T2 | M11 reframing #2; offline RL primitives |
| K5 | Tier demotion: salience-modulated decay (any tier → next-colder; rate = f(C); specific f TBD) — intelligent forgetting per M17. Learned-policy form is part of the K2+T_A3 research target; if K2+T_A3 is dequeued behind T_A1b, the prototype can run K5 with an engineered baseline (FIFO/LRU/TTL or frozen-predictor novelty scoring) without blocking T_A1b work | T3 | M17 active forgetting; H34 reweighted; H42 learned salience function |
| K6 | Offline composition: generate composite fragments from existing memories during consolidation; admit by salience; persist for reuse across sessions. Implementation style deferred (speculative caching / materialized views / Sketch C / reservoir-recombination) | T4 | M14 SPW-R off-line regime; M16 prospective brain; H43 write-side complement; [reservoir-computing](../open-question/reservoir-computing.md); [LoRA as M14-shape](./lora.md) |

### (4) Retriever

| Op | Description | Tier | Anchor |
|---|---|---|---|
| R1 | Cue from context + drifting temporal context | T3 | Norman N4 |
| R2 | Pattern-completion (modern-Hopfield / MERLIN-shape) | T2 | [RETRO](../source/borgeaud-2022-retro.md), [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) |
| R3 | Selectivity via prediction failure / schema gap. **Refinement 2026-05-19**: the prediction error is a vector (ẑ - z'), not just a magnitude — its *direction* (expected event-of-kind-A but got event-of-kind-B) carries retrieval-relevant signal. Retrieval cue uses the full error vector, not just |error| | T3 | FLARE; Norman N3 read-side |
| R4 | Top-k retrieval (configurable k; k=1 honors Norman WTA spirit) | T2 | Engineering-standard with WTA softening |

`[ASSERTED]` R5 (read-as-write reconsolidation at zero latency) was originally a load-bearing T4. It was **demoted** 2026-05-17 under the [[inspiration-not-blueprint]] principle: biology has read-as-write because there's no engineering separation between read and write pathways at the synaptic level — a constraint, not an insight. See [caddy § Five commitments and R5 demotion](./caddy.md) for the full development.

### (5) Integration interface

| Op | Description | Tier | Anchor |
|---|---|---|---|
| I1 | Activation injection via cross-attention (D2 in [[caddy-interface-doors]]); text-injection disallowed — the soft-composition commitment that makes M16 construction emergent under co-training (H43). Other D-doors (D1 embedding, D4 adapter/LoRA, D5 logit) have distinct capability profiles; see doors page | T1 | [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md), RETRO; caddy C4; [H43](../hypothesis/H43-soft-composition-emergent-construction.md) |
| I2 | End-to-end gradient flow through injection | T1 | Same precedents |
| I3 | Co-training stability — don't break golfer | T2 | Memorizing Transformer Section 4.5 |

### (6) Golfer

| Op | Description | Tier |
|---|---|---|
| G1 | Standard LLM forward pass + decoding | T1 |
| G2 | Provide gradient surface for caddy co-training | T1 |
| G3 | Tolerate activation injection without degradation | T2 |

### (A) Training loop

| Op | Description | Tier | Anchor |
|---|---|---|---|
| **T_A1** | **Joint loss: task + auxiliary world-model-style loss on memory reps (MBP-was-dropped).** Falsifiable form: [H44 — T_A1b cross-domain transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md), de-risked by [2026-05-18 isolation experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) with binary verdict methodology in [2026-05-20 probe-2 test set design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md) | **T4** | ICAE precedent at context-compression scale only |
| T_A2 | Co-training schedule (frozen-vs-trainable per stage) | T3 | Memorizing Transformer Section 4.5 (4% finetune) |

`[ASSERTED]` T_A3 (continuous online schema drift, no retraining boundaries) is structurally entangled with K2 — they are the same bet viewed at different scales. K2 is the per-write decision; T_A3 is the system property that emerges from K2 firing continuously over time. Treated as one combined T4: **K2+T_A3**.

**`[ASSERTED]` Status (2026-05-20):** K2+T_A3 is an **active load-bearing T4 research target**, distinct from T_A1b on both timescale (slow / cortical-analog) and mechanism (consolidation policy vs. representation learning). The hypothesis ([H40](../hypothesis/H40-schema-fit-modulated-consolidation.md)) is falsifiable; the [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md) confirmed its scientific distinctness from T_A1b's EMA-target mechanism. The 2026-05-19 deferral to v2 was MVP-product-shaped (tier 3-4 wedge demonstration didn't require it for first-product scope) and was REVERSED 2026-05-20 per [caddy-as-research-program](../decision/caddy-as-research-program.md). Ordering vs. T_A1b is decided by the stack-rank exercise.

### (B) Lifecycle layer

`[ASSERTED]` Dropped for the research prototype. Production concerns (per-user instantiation, versioning, hot-swap, multi-tenancy routing, deletion-on-request) are downstream of "does the architecture work." Research prototype is single-user, single-instance. For the (eventual) team-memory extension, see § Team memory extension below.

### (C) Salience signal

| Op | Description | Tier | Anchor |
|---|---|---|---|
| C | Learned salience function (signature TBD: scalar vs vector, single function vs family) — consumed by E2, K2, K5, R3 | T3 | M15 load-bearing reframe; [salience-signal open question](../open-question/salience-signal.md); H42 |

`[ASSERTED]` Cross-cutting primitive promoted 2026-05-17 during M14-M17 reconciliation. M03, M04, M05, M15, M17 all depend on the same upstream input. Five matrix rows route through it; multiple caddy ops consume it.

**Architectural commitment, not signature commitment.** The doc commits only to *all four consumers routing through C, not through hand-coded heuristics.* The shape of C (scalar vs low-dim vector; one function vs family; query-conditional vs not) is deferred per [[feedback_mvp_doc_not_mvp]]. Logical-type commitment (a `RANK_SCORE`-shaped primitive), not physical-type commitment.

**Training relationship.** C is structurally a sub-output of the T_A1 auxiliary loss — the same training signal that shapes memory representations also shapes the salience head that reads them. Not a third load-bearing T4; a downstream consequence of T_A1.

## Research prototype specification + load-bearing T4 research targets

`[ASSERTED]` Spec total (post M14-M17 reconciliation, 2026-05-17): **6 T1, 9 T2, 11 T3, 4 T4 across 30 ops** (counting C and K6 added during reconciliation; counting R5 in its demoted state).

**Load-bearing T4 research targets (per [caddy-as-research-program](../decision/caddy-as-research-program.md), 2026-05-20): two.**

- **T_A1b** — auxiliary world-model loss on memory representations. Falsifiable form: [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md). Falsifier: [2026-05-18 isolation experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md), with probe-2 binary-verdict methodology pre-registered in [2026-05-20 probe-2 test set design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md).
- **K2+T_A3** — schema-fit-modulated consolidation with continuous online drift. Falsifiable form: [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md). Falsifier: the Version A / Version B isolation experiment design preserved inside H40.

Both are active research targets on distinct timescales and distinct mechanisms — see [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md). Ordering between them is set by the forthcoming stack-rank exercise; one is dequeued first per the "one active research thread at a time" constraint. Sanity-prediction (2026-05-20): T_A1b first (more foundational, pre-registered protocol exists, single-GPU tractable, frontier-pacing pressure from V-JEPA), K2+T_A3 second. The ranking is the work, not this prediction.

The two T4s that are **not** active load-bearing:
- **R5** (read-as-write reconsolidation) — demoted 2026-05-17 to "interesting variant to test" under [[feedback_inspiration_not_blueprint]] (biological constraint, not insight).
- **K6** (offline composition) — deferred from active queue, in spec. Valuable capability; non-trivial to get right; deferred until simpler bets are decided.

### Research prototype scope

The caddy prototype distilled to ~17 operations across the six components, anchored to existing-precedent architecture where possible. The prototype is the smallest implementation that lets us run the load-bearing experiments end-to-end — it is *not* a product target and is not scoped against time-to-market.

```
ARCHITECTURE (from Memorizing Transformer):
  - Pretrained LLM, briefly finetuned (~4% of pretraining cost; MemTx §4.5)
  - Single mid-layer kNN-attention augmentation (~70% depth)
  - Dedicated memory query head W_Q_mem (not repurposing existing Q heads)
  - Memory and local attention combined via learned per-head sigmoid gate
  - Content-conditional gating (not unconditional bias) — refines MemTx's design

ENCODER (from EM-LLM):
  - Surprise-based event boundaries using the base LLM's own NLL
  - Adaptive threshold: rolling mean + γ·std
  - Graph-theoretic refinement via modularity on attention key similarity
  - Handles Norman N2 (event segmentation)

NEW vs the two papers (the actual research):
  - Memory stores LEARNED REPRESENTATIONS (not raw KV pairs)
       — provisional per [[caddy-memory-representation-spectrum]]
  - Memory persists CROSS-SESSION (not within-document only)
  - Learned representations trained with AUXILIARY LOSS (T_A1b; load-bearing)
  - Temporal-context binding at write time (Norman N4)
  - Multi-field memory units (event_rep + raw_content + trajectory_state)
       per [[multi-field-memory-unit]]
  - Schema-fit-modulated consolidation with continuous drift (K2+T_A3;
       load-bearing — second in queue per stack-rank, [[H40]])

PROTOTYPE-DROPPED (per inspiration-not-blueprint and mvp-doc-not-mvp):
  - E3 conjunctive representation as architectural commitment (constraint)
  - S2 silent state as separate op (just a property of S1)
  - S6 explicit consolidation signal (use loss-curve convergence)
  - K3 reverse-replay (engineering has explicit logging)
  - K6 offline composition (valuable capability, non-trivial to get right;
        deferred behind simpler load-bearing bets — AJ 2026-05-17)
  - R5 read-as-write reconsolidation (distributed-systems separation wins)
  - L1-L5 entire lifecycle layer

ENGINEERED FALLBACK (used when a load-bearing target is queued behind):
  - If K2+T_A3 is queued behind T_A1b, the prototype can run K5 with
       FIFO/LRU/TTL or frozen-predictor novelty scoring as a placeholder
       so T_A1b work isn't blocked. This is a sequencing choice, not a
       claim that the learned policy is unneeded.
```

**Research prototype target:** 3.5-4/5 on the [Norman rubric](./norman-rubric.md). The R4 softening (top-k with k>1 default) deliberately costs Norman-rubric points in exchange for engineering pragmatism. EM-LLM's 2.5/5 ceiling is decisively beaten regardless.

## Architectural decomposition that survived AJ pushback

`[ASSERTED]` Six design decisions arrived at via the 2026-05-17 design session and reconciliation pass survived adversarial pressure:

1. **Six-component decomposition** — confirmed sufficient when AJ confirmed every question fits inside one of the six boxes (plus three cross-cutting concerns).
2. **Two load-bearing T4s, not four** — emerged from the adversarial "you don't need any of this" pass. See [[feedback_inspiration_not_blueprint]] for the discipline that drove R5's demotion.
3. **Single query head at ~70% depth for the research prototype** — chosen over multi-layer integration. See § Query head mechanics below.
4. **Dedicated W_Q_mem head, not repurposed Q vectors** — Option B over Option A. See § Query head mechanics below.
5. **R4 softening to top-k** — k=1 as config default honors Norman WTA spirit; k>1 enables engineering pragmatism.
6. **M17 encode-promiscuously / forget-intelligently inversion** — added 2026-05-17 during M14-M17 reconciliation. See § The M17 architectural inversion above.

## Query head mechanics

### Depth at ~70% of the transformer stack

`[ASSERTED]` The memory-augmented layer sits at ~70% depth of the transformer stack. For a 32-layer model (e.g. Llama-3-8B), this is around layers 20-24. For 80 layers (Llama-3-70B), around layers 50-60.

**Too early is wrong.** At early layers, representations are still primarily syntactic/lexical. Queries from that depth would be shaped like "what's the next syntactic structure," not "what do I remember about Marie Curie." The concept the query would ask for hasn't yet been crystallized in the residual stream.

**Too late is wrong.** At late layers, the model has committed to a specific output trajectory. A query head here can only nudge the final answer, not influence the reasoning that produced it. You'd retrieve memory just in time to flavour a sentence, not in time to shape what gets said.

**Empirical anchor:** [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) tested layers 3/6/9/12 in a 12-layer model; layers 6 and 9 (50% and 75% depth) gave best perplexity. Their default was layer 9 (75%).

### Dedicated vs repurposed query head

`[ASSERTED]` Two options for producing memory queries from the augmented layer:

**Option A — Repurpose existing heads (Memorizing Transformer's choice).** The layer's existing Q projections produce vectors that probe both local context AND memory. No new parameters; one mechanism, two purposes. Simple but the same query has to serve both jobs.

**Option B — Dedicated memory query head.** A new small set of parameters at that layer produces query vectors aimed specifically at memory. The query can be optimised for memory-utility separately from local-attention-utility. More parameters, more expressive.

**Current choice: Option B.** Co-training under the auxiliary loss (T_A1) is shaping memory representations; a dedicated query head lets the LLM's "way of asking" be co-trained with the caddy's "way of representing." The shared language they learn together — the geometric alignment between Q_mem and K_mem — is, mechanically, the query-key matching at this dedicated head.

### Co-training and geometric alignment

`[ASSERTED]` "Speaking the same language" between caddy and golfer is a mechanically-measurable property: the dot product between Q_mem (golfer's memory query vector) and K_mem (caddy's stored key vector) on relevant memories goes up over training. That's literally the success signal of co-training.

Three ways to achieve alignment:

1. Train the caddy's representations to live in the LLM's existing layer-N space (constrains the caddy)
2. Add a projection layer between them (extra parameters, slight semantic mismatch)
3. **Co-train both** — caddy learns its representation space, golfer learns to produce queries that match (the caddy-metaphor-faithful choice)

Option 3 is what the caddy concept commits to. The "shorthand the caddy and golfer develop together" *is* this geometric alignment.

## Memory-representation spectrum (deferred)

`[ASSERTED]` The caddy's memory items live on a spectrum between **preconfigured vocabulary + binding policy** (LoRA-style, reservoir-computing-style) and **learned representations** (T_A1-trained encoder produces codes). The current architectural commitment is a **hybrid leaning learned-rep** position: frozen base LLM + light learned encoder + learned codes in the encoder's output space.

The position is held provisionally per [[feedback_mvp_doc_not_mvp]]. Both load-bearing T4 research targets (T_A1b, K2+T_A3) are *shape-dependent* on it — a future decision to slide toward preconfigured would require revisiting both T4 specifications. Full treatment of the spectrum, the tradeoffs, and the conditions for revisiting: [caddy-memory-representation-spectrum](./caddy-memory-representation-spectrum.md).

## Tier semantics (deferred)

`[ASSERTED]` Storage is committed to be N-tier with N≥2 (S1), with promotion (K2) and demotion (K5) ops between adjacent tiers. The research prototype starts at N=2 (effectively hot/cold from the M17 inversion); a production system would likely run N=3 or N=4 matching the physical memory hierarchy (HBM/RAM/NVMe). Specific N, per-tier semantics, and the lifecycle-axis-vs-hardware-axis question are deferred. Full treatment of the multi-tier commitment, the silicon-mapping rationale, and the deferred specifics: [caddy-tier-semantics](./caddy-tier-semantics.md).

## Team memory extension

`[ASSERTED]` Out of scope for the research prototype. The architectural property that enables team memory: **once Q/K alignment is established for the golfer, the storage infrastructure underneath is pluggable.** Any caddy whose K_mem vectors live in the golfer's known Q-space can be queried by that golfer.

Natural partition:
- **Hot stores stay personal** — recent ephemeral interactions, individual context, privacy by default
- **Cold stores can partition** — personal cold store + team cold store (potentially multiple teams)
- **Consolidator routes** — decides what graduates from personal hot to team cold (explicit user tagging, channel inference, multi-user confirmation, or schema-fit detection)
- **Encoder is the shared protocol** — same encoder weights across users produce K_mem in the same geometric space

For Kyrja's specific situation (team of agents communicating via `/team-share/` and MCP), the team-caddy would integrate with the wiki: the wiki becomes the text-level shadow of the team cold store; the team caddy adds representation-level access. v3+ work.

## What this architecture inherits and what it adds

`[ASSERTED]` Three of four architectural ingredients have LLM-scale precedents:

| Ingredient | Source | Tier |
|---|---|---|
| Single mid-layer cross-attention to external memory + learned gate | [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) | T1 |
| Surprise + modularity-graph event segmentation | [EM-LLM](../source/fountas-2024-em-llm.md) | T2 |
| Light finetune of pretrained base to add memory (4% of pretraining cost) | Memorizing Transformer §4.5 | T2 |
| **Auxiliary world-model loss on learned memory representations** | **None at experiential-memory scale** | **T4 — the bet** |

The caddy is, structurally, **Memorizing Transformer with EM-LLM's segmentation, extended with learned representations trained under auxiliary loss, persisted cross-session, and consolidated by schema fit.**

**M14-M17 reconciliation (2026-05-17) added:** salience signal as cross-cutting primitive (C), the M17 encode-promiscuously / forget-intelligently inversion, the multi-tier storage generalisation (N≥2; specifics deferred to silicon mapping), the memory-representation spectrum (held provisionally between preconfigured-vocab and learned-rep endpoints), and K6 offline-composition as a deferred capability. The reconciliation kept two load-bearing T4 research targets: T_A1 (later sharpened to T_A1b) and K2+T_A3.

**2026-05-20 framing shift:** per [caddy-as-research-program](../decision/caddy-as-research-program.md), the caddy is a research program (commercial track decoupled to Eira's bolt-on). The 2026-05-19 K2+T_A3 demotion to v2 — which was MVP-product-shaped — is REVERSED. Both T4s (T_A1b, K2+T_A3) are active load-bearing research targets, ordered by a stack-rank exercise (forthcoming) using scientific leverage, tractability, dependencies, and frontier-pacing as criteria.

## Why this matters

- **Names the design space concretely.** Future architectural decisions can be located on this surface (which component, which op) rather than relitigated abstractly.
- **Tier-labels distinguish engineering risk from research risk.** Two load-bearing T4 research targets (T_A1b and K2+T_A3) define the experimental program; H44 and H40 are their respective falsifiable forms. Everything T3 and below is engineering risk — hard, often expensive, but plannable.
- **The op-level decomposition identifies the smallest demonstrable system.** ~17 ops, not 30. Research-team-shippable, not venture-scale-only — but optimized for "can we run the load-bearing experiments end-to-end," not for time-to-market.
- **Constrains the experimental program.** Two falsifiable bets (T_A1b via H44; K2+T_A3 via H40) ordered by stack-rank. The stack-rank decides which experiment runs first; both decide the architecture's scientific footing.

## Scope limits

- **Architecture, not implementation.** Specific hyperparameters (γ in surprise threshold, k in retrieval, loss weighting in T_A1) are downstream of this page.
- **Research program, not product.** Architecture supports the [caddy](./caddy.md) concept as a research target; commercial vehicle is Eira's bolt-on track per [caddy-as-research-program](../decision/caddy-as-research-program.md).
- **Prototype-scoped.** Team memory, lifecycle, governance — all out of scope for the research prototype. Captured for future reference.
- **Held loosely on T_A1 specifics.** Which auxiliary objective (autoencoder? JEPA? world-model?) is itself a research question; this page commits to *having* an auxiliary objective, not to a specific one.
- **Pattern separation as architectural commitment: declined.** M17 graded decay requires non-colliding storage *units*, which the caddy's discrete addressable storage (S1 row IDs) satisfies by construction. Biology's pattern-separation mechanism is a constraint biology faces (no explicit addressing), not an insight the caddy needs to import. See [[pattern-separation]] for why this matters for substrate paths but not for sidecar architectures.
- **Retrieval cadence is sub-turn at D2/Q4 (single mid-layer cross-attention + dedicated W_Q_mem head).** This puts the caddy on a finer position on the [retrieval-granularity](./retrieval-granularity.md) spectrum than current incumbents' per-turn default. Multi-layer (D3), agentic multi-hop (Q2/Q3), and metacognitive/workspace (Q5/Q6) doors are deferred to v2+ as architecturally distinct finer-or-richer variants — see [[caddy-interface-doors]].

## Related

- [[caddy]] — the canonical architectural definition; this page is its detailed specification.
- [[caddy-interface-doors]] — the D/U/Q door framework; mechanically how integration happens.
- [[caddy-memory-representation-spectrum]] — deferred decision: preconfigured vs learned reps.
- [[caddy-tier-semantics]] — deferred decision: N-tier mapping to silicon.
- [[memory-caddy]] — the live open question; this architecture is the current best-guess answer.
- [[consolidation-channel]] — Kyrja's primary wedge concept; K2+T_A3 in this architecture *is* the channel.
- [[norman-rubric]] — the external evaluation framework; research prototype target is 3.5-4/5.
- [[discrete-unit-memory-architecture]] — the family this architecture instantiates.
- [[feedback_inspiration_not_blueprint]] — discipline that drove R5 demotion and the M14-M17 test-case resolutions.
- [[feedback_capabilities_not_policies]] — discipline that drove the multi-tier-as-capability commitment.
- [[feedback_mvp_doc_not_mvp]] — discipline behind the deferred decisions held in this doc.
- [memory-retrieval-tiers](./memory-retrieval-tiers.md) — capability taxonomy; the architecture's wedge targets tier 3-4.
- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — the wedge-target decision.
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — the multi-field commitment for S1 entries.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the falsifiable form of T_A1.
- [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) — RESOLVED 2026-05-19: K2 stays scientifically distinct from T_A1b's EMA-target mechanism.
- [caddy-as-research-program](../decision/caddy-as-research-program.md) — 2026-05-20 decision: caddy is a research program; commercial track decoupled to Eira's bolt-on; K2+T_A3 returns to active load-bearing research alongside T_A1b.
- [k2-ta3-deferred-to-v2](../decision/k2-ta3-deferred-to-v2.md) — REVERSED 2026-05-20. Historical record of the 2026-05-19 MVP-product-shaped deferral, now undone.
- [H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the falsifiable form of K2+T_A3.

## Source archive

- 2026-05-17 main design session (Nils side-window) — architectural sketch, 25-op decomposition, tier-labeling, op pruning to prototype scope, layer-depth specification, T_A1 first-principles walk, integration-interface deep dive
- 2026-05-17 M14-M17 reconciliation (Nils main-window) — salience signal (C) promoted as cross-cutting primitive; M17 architectural inversion landed as wedge claim; K6 added as deferred op; multi-tier storage generalisation committed; memory-representation spectrum held provisionally
- 2026-05-17 readability restructure — reordered for motivation→mechanism→rationale arc; extracted [[caddy-memory-representation-spectrum]] and [[caddy-tier-semantics]] as separate concept pages with independent lifecycles
- [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) verbatim read (2026-05-17)
- [EM-LLM](../source/fountas-2024-em-llm.md) verbatim read (2026-05-17)
