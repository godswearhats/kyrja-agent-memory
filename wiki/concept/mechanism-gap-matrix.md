---
type: concept
name: Mechanism-gap matrix — biological memory primitives × AI implementation status
status: living
last_ingested: 2026-05-26
sources: [../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/yang-et-al-2024-selection-of-experience.md, ../source/josselyn-tonegawa-2020-engrams.md, ../source/tse-et-al-2007-schemas.md, ../source/nader-schafe-ledoux-2000-reconsolidation.md, ../source/howard-kahana-2002-tcm.md, ../source/buzsaki-2015-spw-r.md, ../source/redondo-morris-2011-stc.md, ../source/schacter-addis-buckner-2007-prospective-brain.md, ../source/hardt-nader-nadel-2013-active-forgetting.md]
epistemic_tags: [asserted, speculated]
tags: [mechanism-gap, ai-translation, path-decision, foundational, living-document]
---

## Definition

The **mechanism-gap matrix** is a living catalogue of biological memory mechanisms and their AI implementation status. Each row names a mechanism, anchors it to a primary source, and records whether current RAG-based and substrate-level agent-memory systems implement it. The matrix is the empirical anchor for Kyrja's path-decision diligence: it makes "which gaps exist" a question of cataloguing, not vibes.

The matrix exists as its own page because it (a) is referenced by `consolidation-channel`, `active-stages-framework`, `admission-control`, `complementary-learning-systems`, both H39 and H40, and any future hypothesis or open-question that derives from a specific biological mechanism (≥6 inbound, anti-sprawl rule 1 satisfied via the inbound count), and (b) has its own update lifecycle (new rows added when new biological mechanisms are sourced; existing rows updated when AI implementations close or partially close a gap).

## The matrix

Status legend:
- ✅ — implemented in this AI class
- ⚠ — partially implemented, or implemented for a different purpose
- ❌ — no implementation in this AI class
- N/A — not applicable to this AI class

| ID | Biological mechanism | Primary source | RAG-based (Mem0, Letta, Zep, Cognee, LightMem) | Substrate-level (Hope, EvoSC, Skill-SD, Cartridges) | Caddy (sidecar, [caddy-architecture](./caddy-architecture.md)) | Kyrja-relevant? | Last reviewed |
|---|---|---|---|---|---|---|---|
| M01 | Fast hippocampal-analog store (rapid one-shot encoding) | [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) | ✅ Vector DB / context window | ✅ Pretrained weights serve as slow side; episodic stores plug in for fast side | ✅ S1 + E1/E2 (one-shot via promiscuous admission per M17 inversion) | Core | 2026-05-17 |
| M02 | Slow neocortical-analog store (gradual structural learning) | [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) | ✅ Frozen pretrained LLM | ✅ Pretrained weights | ✅ (misleading — same caveat: frozen LLM as slow store; G1) | Core | 2026-05-17 |
| M03 | Replay-mediated consolidation operator (fast → slow transfer) | [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) + [Yang 2024](../source/yang-et-al-2024-selection-of-experience.md) | ❌ No consolidation | ⚠ [Hope](../source/behrouz-2026-nested-learning.md) (online only, stage-1); Skill-SD (offline distillation, no selectivity); [EvoSC](../source/yu-2026-evosc.md) (depth-2 soft prompt) | ✅ K1 + **K2** (load-bearing T4) + K4 — architecturally first-class; THE consolidation channel | **Named wedge** ([consolidation-channel](./consolidation-channel.md)) | 2026-05-17 |
| M04 | Selective experience replay (salience/surprise/novelty-prioritized) | [Yang 2024](../source/yang-et-al-2024-selection-of-experience.md) | ❌ | ❌ (PER in RL literature has the *mechanism* but not applied to LLM agent memory) | ✅ K1 + K2 + **(C)** salience signal — learned selection per H42 | High — direct curation analogue; Schaul 2016 PER is the ML bridge | 2026-05-17 |
| M05 | Schema-fit rate modulation (faster consolidation for compatible info) | [Tse 2007](../source/tse-et-al-2007-schemas.md) | ❌ Fixed (no rate) | ❌ Fixed (per implementation) | ✅ **K2** — direct commitment; **active load-bearing T4 research target per [[caddy-as-research-program]] (2026-05-20)**; falsifiable form [[H40]] | **High** — [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md) | 2026-05-20 |
| M06 | Silent engrams (storage ≠ retrieval-handle availability) | [Josselyn 2020](../source/josselyn-tonegawa-2020-engrams.md) | ❌ | ❌ | ⚠ S2 in full spec, prototype-dropped per inspiration-not-blueprint; H39 | **High but speculative** — [H39](../hypothesis/H39-silent-state-primitives.md), [silent-engrams concept](./silent-engrams.md) | 2026-05-17 |
| M07 | Engram migration over time (hippocampus → cortex visualized at cell-ensemble resolution) | [Josselyn 2020](../source/josselyn-tonegawa-2020-engrams.md) (Kitamura 2017 cited) | ❌ | ⚠ Hope's frequency-stratified CMS gestures at multi-timescale storage but doesn't migrate per memory | ✅ K2 + multi-tier (S1 N≥2) — per-memory tier promotion | Medium | 2026-05-17 |
| M08 | Temporal coallocation (~6h linking window) | [Josselyn 2020](../source/josselyn-tonegawa-2020-engrams.md) (Cai 2016 cited) | ❌ | ❌ | ⚠ K2 batch-window parameter absorbs M08+M15 unification; specific window deferred | Medium-high — concrete, time-bounded, AI-translatable | 2026-05-17 |
| M09 | Sparse competitive allocation (excitability-mediated, Darwinian) | [Josselyn 2020](../source/josselyn-tonegawa-2020-engrams.md) | ❌ | ⚠ MoE routing is load-balancing, not memory-allocation; same shape, different objective | ✅ Multi-tier bounded capacity + (C) — Darwinian competition emerges from shared budget | Medium | 2026-05-17 |
| M10 | Reconsolidation (retrieval-triggered update window) | [Nader 2000](../source/nader-schafe-ledoux-2000-reconsolidation.md) | ❌ Pure read | ⚠ MEMIT/ROME edit but not retrieval-triggered; no labile-window semantics | ⚠ S4 enables post-write modification; R5 read-as-write deliberately declined as biological constraint | **OUT OF SCOPE for Kerros (2026-05-26)** — per-memory malleability is a feature for biology, a bug for software (drift, evil² amplification, lost inspectability). Consolidation ≠ reconsolidation; see [integration-gate § Exclusions](./integration-gate.md) | 2026-05-26 |
| M11 | Catastrophic interference avoidance via interleaved learning | [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) | N/A (no FT) | ⚠ Implicit in continual-learning literature; not explicit in agent products | ✅ External S1 storage avoids in-weights interference by construction; K4 + T_A2 handle caddy training | Medium — constraint on any consolidation channel design | 2026-05-17 |
| M12 | Quasi-regular handling (episodic specifics + structural regularity simultaneously) | [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) | ❌ Episodes only (no abstraction) | ❌ Structure only (no episode preservation) | ✅ Multi-tier preserves episodes; K2 induces structure; H43 emerges composition | **Foundational** — both sides needed | 2026-05-17 |
| M13 | Temporal context as retrieval primitive (maintained drifting vector, updated by retrieved content, asymmetric via preexp/newly-learned split) | [Howard & Kahana 2002](../source/howard-kahana-2002-tcm.md) | ⚠ KV cache is implicit within-session; recency weighting is a scalar boost — neither is a persistent vector updated by retrieval | ❌ No substrate-level system maintains a persistent context vector that updates on retrieval | ⚠ S5 + R1 committed at T3; specific TCM mechanism deferred per H41 | **High** — [H41](../hypothesis/H41-temporal-context-retrieval.md); read-side complement to consolidation channel | 2026-05-17 |
| M14 | Sharp-wave ripple physiology + prospective/constructive/vicarious off-line computation (preplay of unvisited routes, joint replays stitching novel trajectories, chained "what if" search, preconfigured-vocabulary alternative to interleaved learning) | [Buzsáki 2015](../source/buzsaki-2015-spw-r.md) | ❌ No mechanism for preplay, joint-replay recombination, or vicarious off-line search; replay broadly absent | ❌ Hope's stage-1 online updates do none of M14's three distinctive functional roles (preplay, joint-replay, vicarious search); re-graded ⚠→❌ 2026-05-17 | ⚠ K6 offline composition in full spec, prototype-dropped; [reservoir-computing](../open-question/reservoir-computing.md) + [LoRA](./lora.md) as sibling architectures | **High** — adds a new functional axis (off-line generative computation, beyond retrieval); sibling to M16 | 2026-05-17 |
| M15 | Synaptic tagging and capture (transient intermediate state ~90 min, gated by global PRP pool; behavioural tagging extends to schema-fit / cross-event rescue at memory level) | [Redondo & Morris 2011](../source/redondo-morris-2011-stc.md) (substitute anchor — Frey & Morris 1997 unavailable) | ❌ No analog of synapse-specific transient state with global-resource gating; encoding either commits or fails | ❌ No equivalent of "potential but uncommitted" intermediate state in pretrained LLM | ⚠ M15 insights absorbed into K2 (batch window, shared budget) + (C) + S1 row-state; no dedicated tagged tier | **Foundational** — molecular substrate underlying M05, M09, M10; tagged-intermediate-tier as architectural primitive | 2026-05-17 |
| M16 | Constructive memory / prospective brain (memory's primary function is forward simulation; shared neural machinery for remembering past and imagining future; flexible recombination of fragments) | [Schacter, Addis & Buckner 2007](../source/schacter-addis-buckner-2007-prospective-brain.md) | ❌ Retrieval-as-lookup; no constructive recombination of fragments into novel scenarios | ❌ No simulation-engine mode; LLM forward pass generates from context but not from stored fragments via memory mechanism | ✅ I1 soft composition (H43) at retrieval; K6 write-side construction deferred | **High** — cognitive characterisation of what M14 describes physiologically; reframes memory's purpose | 2026-05-17 |
| M17 | Active forgetting (regulated decay-via-AMPA-internalisation during sleep; promiscuous encoding + selective forgetting architecture; gist-formation via specifics-decay) | [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) | ⚠ Capacity heuristics (LRU, cutoffs) exist; learned graded forgetting policy modulated by salience signals is absent | ❌ Weights persist forever (frozen) or full retraining; no graded metaplastically-modulated forgetting primitive | ✅ **M17 inversion is the architectural wedge**: K5 salience-modulated decay + (C); H34 reweighted | **Foundational** — first inverse mechanism in the matrix; partner operator to M03 consolidation; possibly same mechanism viewed from opposite angle | 2026-05-17 |

**Tally as of 2026-05-17 (post caddy-column addition + M14 substrate re-grade):**

| Class | ✅ | ⚠ | ❌ | N/A | Notes |
|---|---|---|---|---|---|
| RAG-based | 2 | 2 | 13 | 0 | M01 + M02 (M02 misleading); ⚠ on M13 (KV cache as implicit context) + M17 (LRU heuristics); 13 hard ❌ |
| Substrate-level | 2 | 5 | 10 | 0 | M14 re-graded ⚠→❌ 2026-05-17 (Hope's stage-1 implements none of preplay/joint-replay/vicarious-search); 10 hard ❌ supports AJ's M11 substrate-antagonism intuition |
| Caddy (sidecar) | 11 | 6 | 0 | 0 | M01-M05, M07, M09, M11-M12, M16-M17 are full architectural commitments; M06, M08, M10, M13-M15 are partial (prototype-deferred, parameterised, or insight-absorbed-into-other-ops); zero hard ❌ |

**Caddy column reading:** every matrix row is at least partially addressed by the caddy architecture — no hard ❌ exists. The ⚠ entries fall in three categories:
- **Prototype-deferred but in full spec** (M06 silent engrams via S2; M14 vicarious search via K6) — explicit "keep in spec, build later" decisions per [[feedback_mvp_doc_not_mvp]]
- **Insight-absorbed rather than dedicated op** (M08 temporal coallocation via K2 batch-window; M15 STC via K2+C+S1 row-state) — biology's specific mechanism not imported per [[feedback_inspiration_not_blueprint]], the structural insight lands as parameterisation
- **Architectural commitment with implementation deferred** (M10 reconsolidation via S4 minus declined R5; M13 temporal context via S5+R1 at T3) — committed but not yet load-bearing

The caddy column is the empirical anchor for the post-Norman gap claim: 11 of 17 mechanisms are full architectural commitments in a single system, where every published incumbent scores ≤2 ✅ (counting EM-LLM/MEGa at the high end).

## How to update this matrix

`[ASSERTED]` Update procedure (additive — never delete a row, only mark it superseded):

- **Adding a new row** (new biological mechanism surfaced from primary literature):
  - Assign the next M## ID.
  - Anchor to a `source/*` page (the source page must exist; do not add rows for mechanisms cited only transitively).
  - Fill the RAG and substrate columns based on the *current state of the field*, not aspirational. ⚠ status requires a one-line rationale.
  - Set `Last reviewed` to today.
  - Bump `last_ingested:` on this page.
  - Add inbound links from any concept/hypothesis pages the new mechanism affects.

- **Updating an existing row** (AI implementation status changes, or new evidence shifts the assessment):
  - Update the status column in-place (✅/⚠/❌/N/A).
  - Update `Last reviewed`.
  - Append a one-line entry to "Update history" below.
  - If the change supersedes a hypothesis's evidence base (e.g., a system now implements M06, so [H39](../hypothesis/H39-silent-state-primitives.md) needs re-evaluation), flag the affected hypothesis page.

- **Marking superseded** (rare — the mechanism turns out to be wrong, or two mechanisms merge):
  - Add a "SUPERSEDED" marker in the mechanism column.
  - Add a note in "Update history" explaining the supersession.
  - Don't delete the row.

## Candidate rows pending future reads

`[ASSERTED]` All four candidate rows from the 2026-05-14 list have been promoted to numbered rows during the 2026-05-16 ingest pass. New candidate rows will be added here as future primary reads land.

The candidate list is not exhaustive — additional mechanisms named in the cog-sci literature may surface during future Kyrja work. Specific gaps currently flagged for potential future ingest (from the M14-M17 reads):

- **Modern Hopfield pattern-completion-as-retrieval** (Ramsauer 2020, Krotov 2020) — candidate read-side primitive complementing M13 temporal-context retrieval.
- **Adult hippocampal neurogenesis as pattern-separation capacity** (Nakashiba et al. 2012, McHugh et al. 2007) — mechanism by which capacity can grow rather than being architecturally fixed.
- **Successor representation** (Stachenfeld et al. 2017) — algorithmic crossover for M13 temporal-context primitive; RL literature on multi-timescale SR may transfer to caddy implementations.
- **PKMζ / atypical PKC isoform mechanism for memory maintenance** (Sacktor et al. line) — molecular substrate for the maintenance side of M15 STC, possibly a deeper sub-row.

## Update history

- **2026-05-14** — Matrix created with M01-M12 from the cog-sci primary-source sweep (5 P0 reads). Initial assessment: 7 of 12 mechanisms unimplemented.
- **2026-05-14 (evening)** — Promoted Howard & Kahana 2002 TCM from candidate to M13 after full verbatim read. Net effect: 8 of 13 mechanisms unimplemented in either AI class. Spawned [H41](../hypothesis/H41-temporal-context-retrieval.md). The retrieval-cue primitive that M13 names is architecturally distinct from M01-M12 (which are all storage/consolidation/selection); M13 is the first read-side primitive in the matrix.
- **2026-05-16** — Promoted all four queued candidate rows (M14-M17) to numbered rows during the substrate-path digest ingest pass. Verbatim reads completed for Buzsáki 2015 SPW-Rs (M14), Redondo & Morris 2011 STC (M15 substitute for paywalled Frey & Morris 1997), Schacter, Addis & Buckner 2007 prospective-brain (M16, replacing the originally-listed Schacter & Addis 2007 with the canonical NRN co-authored anchor), Hardt/Nader/Nadel 2013 active forgetting (M17). Net effect: matrix grows from 13 to 17 rows; 11 of 17 hard ❌ in both AI classes. Three substantive novel observations surfaced during the reads: (a) M14 is NOT subsumed by M11 — it adds a new functional axis (off-line generative computation: preplay, joint replays, vicarious "what if" search, preconfigured-vocabulary alternative to interleaved learning); (b) M15 surfaces a tagged-intermediate-tier as candidate architectural primitive underlying M05, M09, M10 simultaneously; (c) M17 is the first inverse mechanism in the matrix — active forgetting as constructive function, with hippocampal-trace decay as the biology's automatic abstraction mechanism. The walk also surfaced a **fourth unification observation** (M03 + M17 may be the same sleep-based selection mechanism viewed from opposite angles), strengthening the speculation that the matrix rows may be observable consequences of a smaller primitive set. M14 + M16 + M17 together reframe memory's primary function as **constructive simulation, not faithful retrieval** — a structural reorientation that no current AI memory architecture has adopted.
- **2026-05-17 (caddy-column addition + M14 substrate re-grade)** — Caddy (sidecar) column added to the matrix, populated against the [caddy-architecture](./caddy-architecture.md) post-M14-M17 reconciliation state. Each row anchored to specific caddy ops (E#/S#/K#/R#/I#/T_A#/C) where applicable. Substrate column M14 re-graded ⚠→❌ on grounds flagged twice during the M14 and M16/M17 walks: Hope's stage-1 online updates implement none of M14's three distinctive functional roles (preplay, joint replays stitching novel trajectories, vicarious off-line search). The caddy column shows 11 ✅ / 6 ⚠ / 0 ❌ — every matrix row at least partially addressed; zero hard ❌. The ⚠ entries are deliberate (prototype-deferred-but-in-spec, insight-absorbed-into-parameterisation, or T3-committed-with-specifics-deferred). The 11 ✅ count is the empirical anchor for the post-Norman gap claim: no published incumbent system scores above ~2 ✅ on the same matrix.
- **2026-05-17 (M16 + M17 walks)** — Walkthrough of rows M16 and M17 completed; matrix walk M01-M17 now complete.
  - M16 walk: produced (1) anticipate-vs-predict naming distinction — caddy's job is anticipation (preparing material for the golfer's prediction), not prediction itself; (2) selection-vs-construction dichotomy — M16 strong reading requires construction (returning composed fragments that don't exist as any single stored item), weak reading allows selection (returning the right literal items); (3) strong vs weak reading of M16: weak (teleological — memory exists for future action, implementation can still be selection-based) vs strong (architectural — caddy must construct novel fragments); (4) construction-as-emergence question — if caddy uses soft-composition interface (attention-style output) + co-training, construction emerges essentially for free; if caddy uses hard-selection interface (top-K verbatim), construction is structurally foreclosed regardless of training. Promoted to [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md). (5) Two surfaces, not one: online surface (theta-mode, per-token-per-layer) + off-line surface (SPW-R regime) compose, doing different jobs. Promoted to [retrieval-granularity](./retrieval-granularity.md) as a five-position spectrum with current agent-memory product space all defaulting to per-turn without testing finer alternatives.
  - M17 walk: produced (1) first inverse mechanism in the matrix — forgetting is a first-class memory function, not a failure mode; (2) "encode promiscuously, forget intelligently" architectural inversion — biology puts intelligence at forgetting policy, current AI systems put it at admission gate. The MOOM-style scoring of [H34](../hypothesis/H34-forgetting-scores.md) is one operational implementation of the inverted-architecture bet. (3) **Two forgetting mechanisms, not one** — interference (overlap-driven, during active processing) vs decay (off-line, salience-modulated). Maps cleanly to two AI problems: interference → catastrophic forgetting (known); decay → graded learned forgetting policy (absent). (4) **Pattern separation as architectural prerequisite for graded decay** — promoted to [pattern-separation concept](./pattern-separation.md). Without orthogonal coding, similar memories collide and interference dominates; per-memory decay rates have no meaningful referent. DB analogy: per-key TTLs require non-colliding keys. (5) **Fourth unification observation: M03 + M17 may be the same mechanism** — sleep-window replay strengthens what gets replayed; non-replay produces decay; same salience-driven selection, opposite outcomes. (6) Salience signal is now the **fifth** matrix row dependency (M03, M04, M05, M15, M17) — reinforces the salience-signal-as-load-bearing-variable observation from the M15 walk.
  - Substrate-antagonism re-grade for M14 still flagged as deferred — to be addressed during the caddy column update.
- **2026-05-17 (M14 + M15 walks)** — Walkthrough of rows M14 and M15 completed.
  - M14 walk: produced (1) Sketch C architectural reading — recombination as a write-side operation on the caddy's store performed during off-line passes, derived from biology's SPW-R-state-vs-theta-state mutual exclusion; (2) math-level bridge to LLM attention via Modern Hopfield equivalence (Ramsauer 2020), with the critical disanalogy that attention operates over the context window while M14's mechanism operates over long-term storage; (3) [reservoir-computing](../open-question/reservoir-computing.md) opened as candidate concrete implementation of preconfigured-vocabulary framing; (4) [LoRA](./lora.md) reframed as an M14-shaped solution the LLM toolchain stumbled into without invoking the biological framing; (5) the [catastrophic-interference](./catastrophic-interference.md) concept formalised with M11/M14/RC/LoRA as the four-and-a-half known solution shapes. Substrate-antagonism reading for M14 candidate re-grade: the current ⚠ may be too generous given Hope's stage-1 online updates implement none of M14's three distinctive functional roles (preplay, joint-replay, vicarious search). Flagged for re-assessment during the caddy-column update.
  - M15 walk: produced (1) AJ-originated WAL-plus-credit-pool-plus-rescue restatement of STC mechanism — tags are free/automatic, PRPs are the scarce shared resource, the rescue mechanism is bottom-up (passive capture from shared budget) not top-down (no coordinator); (2) token-bucket-rate-limiting analog ("token-bucket persistence") and GC-tenuring-with-competitive-promotion analog landed; (3) **fifth unification observation: M08 + M15** — temporal coallocation (~6h, population-level) and synaptic tagging (~90 min, synapse-level) likely the same mechanism observed at different scales, with M15 adding salience-mediated rescue beyond M08's pure-temporal binding; (4) **load-bearing reframe: salience signal computation is the variable downstream of architecture, invariant across M03 / M04 / M05 / M15 / M17 implementations**, promoted to [salience-signal open question](../open-question/salience-signal.md) and the first falsifiable claim derived from it as [H42](../hypothesis/H42-learned-salience-function.md). The salience-signal finding refines the matrix's character: many rows depend on the same unresolved input, suggesting the matrix's catalogue is observing *consequences of an upstream computational problem* in addition to the architectural-primitive set already speculated.

- **2026-05-26 (integration-gate re-grade)** — Re-graded M01–M17 by the [integration gate](./integration-gate.md) (boltable-in-principle / scaling-separation). The 17 rows collapse onto one Kerros bet (non-frozen weights); M10 marked out-of-scope-for-Kerros; the M03/M17 unification splits under the gate. See the "Re-graded through the integration gate" section. No row's AI-implementation status changed — this is a Kerros-scope overlay, not a status update.

## Synthesis: M01-M17 walk complete

`[ASSERTED]` Promoted 2026-05-17 after walkthrough of all 17 rows and the caddy-architecture reconciliation pass. Four findings consolidate the matrix walk into load-bearing claims:

### 1. The caddy column is the empirical anchor for the wedge claim

11 ✅ / 6 ⚠ / 0 ❌ across the caddy column versus 2 ✅ / 2-5 ⚠ / 10-13 ❌ for the published incumbent classes. No system in the [Norman rubric](./norman-rubric.md) literature scores comparably. The matrix is the per-mechanism breakdown of what the post-Norman gap actually consists of, and the caddy is the architectural commitment that closes it.

### 2. Primitive-set decomposition: the 17 rows may be consequences of a smaller primitive set

Five unification candidates surfaced during the walk, each suggesting two or more rows share an underlying mechanism observed at different scales or angles:

| Unification | Reading | Implication |
|---|---|---|
| **M10/M11** | Reconsolidation and interleaved-learning may be the same online-update mechanism viewed at different timescales | If true, one consolidation operator (K2-shape) handles both |
| **M11/M12** | Catastrophic-interference avoidance and quasi-regular handling may be the same architectural commitment (separate stores for episodes vs structure) seen from two angles | Multi-tier storage (S1 N≥2) addresses both |
| **M05/M10/M15** | Schema-fit modulation, reconsolidation, and synaptic tagging may all be facets of the same gated-promotion machinery | (C) salience signal + K2 covers the family |
| **M03/M17** | Replay-based consolidation and active forgetting may be the same sleep-window mechanism: replayed → strengthened, non-replayed → decayed; same salience signal, opposite outcomes | K2 promotion and K5 demotion share the salience-signal input — confirmed by the M17 inversion architectural commitment |
| **M08/M15** | Temporal coallocation (~6h population-level) and synaptic tagging (~90 min synapse-level) likely the same mechanism observed at different scales | K2 batch-window parameter covers both |

The matrix may be a catalogue of *observable consequences* of perhaps 4-6 underlying architectural primitives, not 17 independent mechanisms. This refines the gap-filling strategy: closing several rows with one architectural commitment is structurally possible.

### 3. Salience signal computation is the load-bearing upstream variable

Five matrix rows (M03, M04, M05, M15, M17) depend on the same upstream input: a learned scalar-or-low-dim-vector function quantifying a memory's value to the system. The architectural choice (consolidator op shape, tagged-intermediate-tier vs not, decay rule) is largely implementation detail downstream of the salience signal. The signal itself is invariant across architectures and not yet solved by the current field.

Promoted to [salience-signal open question](../open-question/salience-signal.md). First falsifiable claim derived: [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md). The caddy commits to it as cross-cutting primitive (C) per [caddy-architecture § (C) Salience signal](./caddy-architecture.md#c-salience-signal).

### 4. M14-M17 cluster joint reframing: memory's primary function

The M14-M17 cluster jointly reframes memory's primary function as **constructive simulation supported by active forgetting, tagged-intermediate persistence, and preconfigured vocabulary** — not faithful retrieval:

- **M14 (SPW-R / preplay)** — off-line generative recombination, vicarious search, joint replays. Memory generates novel trajectories from stored fragments.
- **M15 (STC / tagged intermediates)** — encoding is not commitment; tagged items compete for shared-budget rescue. Memory is a competition for persistence, not an absolute admission.
- **M16 (constructive memory / prospective brain)** — memory exists for forward simulation; shared neural machinery for remembering past and imagining future.
- **M17 (active forgetting)** — forgetting is a first-class memory function, not a failure mode. "Encode promiscuously, forget intelligently" inverts current AI practice.

Together, these four rows commit the architecture to *anticipation* (caddy's job) rather than retrieval — the M16 reframing that AJ named during the M16 walk. The caddy's I1 + H43 soft-composition commitment captures the retrieval-side construction; K6 (deferred behind simpler load-bearing bets) captures the write-side construction; K5 + M17 inversion captures the active-forgetting commitment.

No published memory system has adopted this reframing as architectural posture. The 11-month post-Norman gap is plausibly the cumulative consequence of every existing system being designed around retrieval, not anticipation.

### 5. Family-level framing status: discrete-unit-memory-architecture survived

The [discrete-unit-memory-architecture](./discrete-unit-memory-architecture.md) frame (continuous-update substrate vs discrete-unit family) survived M01-M17 unchanged. Within the family, the [caddy](./caddy.md) is the active architectural member. The three-axis within-family space (policy-learnedness × coupling-depth × integration-depth) calibrated in the M10/M11 walk also survived M12-M17.

Substrate-as-Kyrja-product-path remains de-facto closed (AJ explicit 2026-05-15). Bolt-on remains the de-facto crowded space. The caddy is the active question's answer.

## Re-graded through the integration gate (2026-05-26)

`[ASSERTED]` The matrix's columns ask *is a mechanism implemented*. The [integration gate](./integration-gate.md) asks a different question — *is the capability boltable in principle, or does a bolt-on's imitation cost diverge with complexity?* Re-grading M01–M17 by that test sorts the rows onto one axis and collapses them to a single Kerros bet (**non-frozen weights**). The pivot is the [memory-consumer-axis](./memory-consumer-axis.md): integration ↔ memory-for-the-model; persistence ↔ memory-for-the-agent.

- **Integration (Kerros) — compositional / constructive generalization:** M12, M14, M16. Bolt-on imitation cost *diverges* (combinatorial / Xu `k²/d`). The provable separation.
- **Integration (Kerros) — consolidation into the slow store:** M03, M05, M07. Cost grows (text-replay scales with the knowledge base).
- **Persistence (product) — boltable:** M01, M04, M08, M09, M13, M15, M17. Storage / selection / decay a software loop does fine; the inert store is a *feature* (reliability, inspectability, anti-poisoning).
- **Inverted cost (constraint, not capability):** M11. The bolt-on *wins* — inert records never collide; integration risks collision. CLS pays it down.
- **Excluded:** M10 (per-memory reconsolidation) — out of scope; a feature for biology, a bug for software. See the M10 row and [integration-gate § Exclusions](./integration-gate.md).

The sort straddles the matrix's own unifications: M03/M17 were flagged as the same mechanism, but under the gate they **split** — consolidation's fast→slow *transfer* is integration (M03), while forgetting-as-eviction is boltable (M17). Same biology, opposite sides of the gate. This re-grade supersedes the wedge-anchored [research-backlog stack-rank](../decision/research-backlog-stack-rank.md). Full treatment + cost ledger + experiment shape: [integration-gate](./integration-gate.md).

## Why this matters

## Scope limits

- The matrix tracks **mechanisms**, not architectures. A single architecture (e.g., Hope) may partially implement multiple mechanisms (M03, M07); the matrix records that, but doesn't decompose architectures.
- **AI implementation status** is a coarse summary, not a benchmark. ⚠ entries hide considerable variation across systems within the class.
- The matrix does NOT prescribe priority. The "Kyrja-relevant?" column is editorial commentary, not a forced ranking.
- The matrix is **deliberately additive**. Rows are added when new sources land; the AI columns are updated when the field moves. Rows are not removed even when superseded — the supersession event is preserved in the update history.

## Related

- [consolidation-channel](./consolidation-channel.md) — the operator M03 names; Kyrja's primary wedge.
- [complementary-learning-systems](./complementary-learning-systems.md) — the cog-sci foundation; sources M01, M02, M03, M11, M12.
- [silent-engrams](./silent-engrams.md) — concept page for M06.
- [active-stages-framework](./active-stages-framework.md) — Kyrja's per-stage decomposition; multiple matrix rows source biological precedents for the four active stages.
- [admission-control](./admission-control.md) — M05 (schema-fit) is the biological precedent for an admission-rate signal.
- [substrate-as-memory](./substrate-as-memory.md) — the broader paradigm; the matrix is the gap-list inside it.
- [catastrophic-interference](./catastrophic-interference.md) — the architectural problem M11 and M14 supply different solutions to.
- [H39 — silent-state primitives](../hypothesis/H39-silent-state-primitives.md) — falsifiable claim derived from M06.
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — falsifiable claim derived from M05.
- [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md) — falsifiable claim derived from M13.
- [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md) — falsifiable claim derived from the salience-signal open question.
- [salience-signal](../open-question/salience-signal.md) — load-bearing input variable across M03, M04, M05, M15, M17.
- [reservoir-computing](../open-question/reservoir-computing.md) — candidate concrete implementation of M14's preconfigured-vocabulary framing. **2026-05-17 update:** literature-review pass closed pure-RC ("Sketch A") as empirically dead — the architectural commitment was abandoned by RC's own engineering descendants. The cerebellar biological precedent is feedforward; the hippocampus-as-recurrent-RC analogy is weaker than initially framed. Sketch C (reservoir + writable buffer + off-line consolidation) maps onto the M14 SPW-R off-line regime and remains the architecturally most interesting candidate.
- [pattern-separation](./pattern-separation.md) — architectural prerequisite for graded decay (M17); orthogonal/sparse coding as the precondition for per-memory decay rates.
- [retrieval-granularity](./retrieval-granularity.md) — five-position spectrum of when memory is surfaced during generation; current incumbents all default to per-turn without testing finer alternatives.
- [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) — falsifiable claim that soft-composition interface + co-training produces emergent M16 constructive memory.
- [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md) — M03 design fork.
- [cross-session-continuity](../open-question/cross-session-continuity.md) — M13 is a candidate addressing-mechanism.

## Source archive

The matrix was constructed during the 2026-05-14 cog-sci primary-source sweep. See [log.md](../log.md) under that date for the sweep's full ingest record. Each row anchors to a primary source page; the sources frontmatter lists those anchors.
