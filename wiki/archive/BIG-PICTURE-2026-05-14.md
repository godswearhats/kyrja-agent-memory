---
name: Kyrja Big Picture
status: living
last_ingested: 2026-05-14
sources: []
---

# Kyrja Big Picture

*The "you are here" map for Kyrja research. Drill from here into wiki pages for detail. This document is intentionally short — depth lives in the wiki.*

---

## Thesis (one paragraph)

Agentic memory systems built on commodity-database stitching (Cognee, Mem0, Letta, Zep all delegate to HNSW under the hood) inherit those backends' scale limits and degrade into a **cascading-failures regime** at billion scale on homogeneous code corpora. The wedge is **integration discipline across a seven-layer stack** — every component exists in research or production, no incumbent integrates more than one or two layers. We earn the right to take on the integration by leading with a **tool-chain token-savings wedge** — a deliberately narrow product that proves itself before the broader architecture is built.

---

## Architecture

See [seven-layer integration stack](./concept/seven-layer-stack.md) for the full architecture (with diagram).

The wedge product touches **2-3 layers** initially: admission control, embedding, retrieval. Remaining layers come on with subsequent product iterations.

---

## Three legs of evidence

1. **Volume.** All six bracketing scenarios cross the LIMIT-1536d ceiling within 5 years — even the conservative ones. See [scale-crossings](./concept/scale-crossings.md). Upstream rate-of-generation in [agent data generation](./concept/agent-data-generation.md) (100K-500K ephemeral tokens per 100 persisted lines). Anchored on [Weller 2025 LIMIT](./source/weller-2025-limit.md).

2. **Recall.** The [cascading-failures product](./concept/cascading-failures.md) predicts 30-50% effective recall at billion scale. Modes 1, 3, 4 anchored in [HNSW scale limits](./concept/hnsw-scale-limits.md); mode 2 anchored in [embedding collapse](./concept/embedding-collapse.md). `[ASSERTED]` at the product level; today-anchor evidence at small scale lives in [benchmark-replication-gap](./concept/benchmark-replication-gap.md) (incumbents at 49-65% on third-party replications, before any wall bites). [multiplicativity-vs-overlap](./open-question/multiplicativity-vs-overlap.md) is the highest-priority empirical gap. Three pre-registered falsification criteria are in [cascading-failures § Falsifiability](./concept/cascading-failures.md#falsifiability).

3. **Integration gap.** [Seven-layer stack](./concept/seven-layer-stack.md) maps research-vs-incumbent layer by layer. No incumbent integrates more than ~2.5 of 7 layers; governance is uncovered across the entire set. See [incumbents — index](./incumbent/index.md) for the catalog and [seven-layer-stack § Incumbent mapping](./concept/seven-layer-stack.md#incumbent-mapping) for the per-layer rollup table.

---

## Substrate paradigm framing (added 2026-05-13)

Kyrja's plain-English thesis — "AI agent memory should be the substrate the agent thinks WITH, not the database the agent thinks ABOUT" — sits inside the [substrate-as-memory](./concept/substrate-as-memory.md) paradigm. The 2026-05-13 substrate survey (10 papers, comparison-grid + temperature-checks) anchored three architectural sub-paradigms ([substrate-paradigms](./concept/substrate-paradigms.md)): P1 substrate-as-state ([Mamba](./source/gu-dao-2023-mamba.md), [Titans](./source/behrouz-2024-titans.md), [TTT](./source/sun-2024-ttt.md)); P2 substrate-as-module ([NTM](./source/graves-2014-ntm.md), [kNN-LM](./source/khandelwal-2020-knn-lm.md), [RETRO](./source/borgeaud-2022-retro.md)); P3 substrate-as-simulator ([World Models](./source/ha-schmidhuber-2018-world-models.md), [DreamerV3](./source/hafner-2023-dreamerv3.md), [LeCun 2022](./source/lecun-2022-autonomous-mi.md)). [Xu et al. 2026](./source/xu-2026-agentic-memo.md) provides a Theorem 1 sample-complexity separation `Ω(k²/d)` between retrieval and parametric memory and names the field's missing piece as the **consolidation channel** — Kyrja's defensible wedge. The Phase 2 read of [EvoSC (Yu et al. 2026)](./source/yu-2026-evosc.md) on 2026-05-14 added the **substrate-depth ladder** to the design space: consolidation can be realised at varying depths (text retrieval → text summarisation → soft prompt tuning → adapter → weight edit → full FT), and EvoSC's published gains sit at the soft-prompt-tuning depth atop a frozen base — empirical proof that consolidation-shaped operations work even at low substrate depth, while leaving the deeper rungs open. The same-day read of [Nested Learning / Hope (Behrouz et al. 2026)](./source/behrouz-2026-nested-learning.md) added a second axis: depth is not one-dimensional — Hope's frequency-stratified MLP chain occupies multiple ladder rungs simultaneously, making the design space `(depth, frequency)`-valued. Hope also names a load-bearing fork the consolidation channel must commit to: **online (stage-1) vs offline (stage-2) consolidation** — Hope addresses only the former. See [online-vs-offline-consolidation](./open-question/online-vs-offline-consolidation.md). The substrate-memory work and the seven-layer wedge work do not compete; they are complementary architectural levels. See [consolidation-channel](./concept/consolidation-channel.md) and [cross-session-continuity](./open-question/cross-session-continuity.md).

---

## Three framing updates from the deep-dive (2026-05-12)

Surfaced during Phase F deep-dive atomization; each changes how a downstream argument should be made.

1. **Storage cost is no longer the binding constraint at billion scale.** VectorChord runs 1B+ vectors on a single 128GB-RAM PostgreSQL machine via [RaBitQ](./source/rabitq-2024.md). Binding constraints shift to recall (the [LIMIT bound](./source/weller-2025-limit.md)) and consolidation. Implication: the tiered-storage layer of the [seven-layer stack](./concept/seven-layer-stack.md) is *necessary but no longer the load-bearing differentiator* — the embedding layer and admission layer carry more weight than the deep-dive originally implied. Full cost-leg framing at [cost-leg — affordable substrate](./concept/cost-leg-affordable-substrate.md).

2. **"Long context is not memory" is the empirical defense against the context-windows objection.** The [9-challenges survey (Mar 2026)](./source/memory-surveys-2026.md) demonstrates that 200K+ token windows underperform purpose-built memory systems on selective retrieval. As 1M+ context windows ship, the natural counter-question to memory work is "why build memory at all?" This survey is the citable answer — passive context underperforms purpose-built memory on the workloads that matter.

3. **Admission control is the only causal layer.** Six of seven layers in the stack ([embedding](./concept/multi-vector-retrieval.md), [graph memory](./concept/graph-memory-approaches.md), [tiered storage](./concept/beyond-hnsw-approaches.md), retrieval, consolidation, governance) fight *symptoms* of corpus growth. Only [admission control](./concept/admission-control.md) reduces corpus size *at the source*. If 80% of agent memories are redundant or low-value, preventing their creation is orders of magnitude cheaper than storing and searching them. This reframes the priority ordering of the stack — admission control is not just "first in the dataflow," it's "highest leverage on the binding constraint." Wedge implication: the MTP should ship a simple admission heuristic (LSH dedup + length floor + importance score from the distiller) and log decisions for a future learned gate.

---

## Key decisions

| Decision | Status | Page |
|---|---|---|
| Repo-bounded scope | ACTIVE | [repo-bounded-scope](./decision/repo-bounded-scope.md) |
| Precision over recall | ACTIVE | [precision-over-recall](./decision/precision-over-recall.md) |
| Structured filter first, semantic last | ACTIVE | [structured-filter-first](./decision/structured-filter-first.md) |
| Org-wide store, repo-scoped queries | ACTIVE | [org-wide-store-repo-scoped-queries](./decision/org-wide-store-repo-scoped-queries.md) |
| Write-side quality gate deferrable | ACTIVE | [write-side-quality-gate-deferrable](./decision/write-side-quality-gate-deferrable.md) |
| Tool-chain wedge as adoption path | ACTIVE | [tool-chain-wedge-as-adoption-path](./decision/tool-chain-wedge-as-adoption-path.md) |
| Slot-format encoding for memory | ACTIVE | [slot-format-encoding](./decision/slot-format-encoding.md) |
| Re-anchor thesis on cascading-failures product (methodology) | ACTIVE | [cascading-failures-reanchor](./decision/cascading-failures-reanchor.md) |
| Scale-model audit corrections (methodology) | ACTIVE | [scale-model-audit-corrections](./decision/scale-model-audit-corrections.md) |

---

## What we've measured vs asserted vs untested

| Claim | Status | Anchor |
|---|---|---|
| Slot-format encoding beats prose on cost | `[MEASURED]` | [Exp 1 + Exp 2](experiment/2026-05-11-write-quality-variance/README.md) |
| Cost-asymmetry: relevant memory −50%, irrelevant +50% | `[MEASURED]` (Phase 2; magnitudes drift) | same |
| Pass-rate effect of memory on agent task completion | **retracted** — metric was misaligned (SWE-bench gold ≠ wedge hypothesis) | same |
| H-QUAL-FLOOR (bad source = harmful memory) | REJECTED for mild degradation; UNTESTED for worst case | same |
| Cascading-failures product at billion scale | `[ASSERTED]` | [cascading-failures](./concept/cascading-failures.md) |
| Multiplicativity vs overlap of the four cascade modes | `[SPECULATED]` — highest-priority empirical gap | same |
| Seven-layer integration outperforms 1-2-layer incumbents | `[ASSERTED]` | Goal 5 MTP is first evidence step |

---

## Open experiments by leverage

1. **Goal 5: MTP build.** Smallest end-to-end loop on AJ's real work. Surfaces encoding-quality ceiling and provides real quality signal (which SWE-bench can't). Highest leverage.
2. **Multiplicativity-vs-overlap on cascading-failures.** Calibrate whether the four recall modes compound multiplicatively or overlap. See [multiplicativity-vs-overlap](./open-question/multiplicativity-vs-overlap.md).
3. **Worst-case source experiment.** Closes H-QUAL-FLOOR at the limit.
4. **F5 (memories/session) production data.** Biggest data gap in scale model; no vendor publishes.
5. **F12 retention wiring.** Compliance retention (HIPAA, SOX, EU AI Act) doesn't currently bound consolidation rate in the model.

---

## Wiki scope (clarified 2026-05-12)

The wiki captures **all of our thinking about agent memory**, not just what is in scope for the current wedge. The wedge will evolve as we learn; hypotheses we pursue will change. The inclusion test for a wiki page is "is this a real research idea worth tracking," not "is this load-bearing for the wedge right now." Anti-sprawl rules (3+ inbound refs OR own status lifecycle) remain the gate against duplication, not against ambition.

This framing was made explicit on 2026-05-12 after a wedge-centric triage pass produced an over-pruning bias. Triage now defaults to *promote unless clearly subsumed or commercial*.

## Cross-agent work (referenced, not duplicated)

- **Eira's commercial framing** — lives in .
- **Kerman's MASQ benchmark work** — lives in . See [kerman-10x-test-design](./open-question/kerman-10x-test-design.md) for what the benchmark would need to measure.

---

## Navigation

- [SCHEMA.md](./SCHEMA.md) — conventions for the wiki itself (v0.4).
- [index.md](./index.md) — full catalog of pages by type.
- [incumbent/index.md](./incumbent/index.md) — catalog of memory-system and vector-DB substrate incumbents.
- [log.md](./log.md) — ingest history and schema-change record.

---

*Last updated 2026-05-14 by Nils (indigo). Wiki schema v0.4. Phase F (atomization of monolithic docs into the wiki) complete; substrate-survey Phase 1 ingested 2026-05-13; EvoSC + Nested Learning ingested 2026-05-14. Phase 2 reading continues (McClelland 1995, ParamMem, Experience Compression Spectrum) before Phase 3 design.*
