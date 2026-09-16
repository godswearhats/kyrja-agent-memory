---
type: concept
name: Graph-Memory Approaches (GraphRAG, MAGMA, GAM, A-MEM)
status: timeless
last_ingested: 2026-05-13
sources: [../source/memory-surveys-2026.md, ../source/zep-graphiti-2501.md]
epistemic_tags: [asserted]
tags: [graph-memory, multi-graph, integration-gap, temporal-memory]
---

## Definition

**Graph-memory approaches** treat agent memory as one or more knowledge graphs over which retrieval is graph traversal augmented by vector similarity at the leaves. The family splits roughly:

- **Single-graph variants** (Microsoft GraphRAG, Zep/Graphiti) — one knowledge graph; entity-relationship structure with optional temporal facets.
- **Multi-graph variants** (MAGMA, GAM) — multiple orthogonal graphs (semantic, temporal, causal, structural) traversed in parallel.
- **Zettelkasten-inspired** (A-MEM) — dynamic linking; new memories trigger updates to historical representations.

This is the **Multi-Graph Memory layer** of [seven-layer stack](./seven-layer-stack.md).

## The four canonical graph types (seven-layer-stack synthesis)

1. **Semantic graph** — entity relationships. The most common; what GraphRAG and Cognee build.
2. **Temporal graph** — fact validity windows; "this was true between t1 and t2." [Zep's differentiator](../incumbent/zep.md).
3. **Causal graph** — what caused what. Underexplored in production; mentioned in deep-dive §10's hypothetical stack.
4. **Structural graph** — code dependencies, imports, call graphs. Underexplored for memory; structural code information is generally treated as auxiliary, not as a first-class memory graph.

**No incumbent integrates more than two of these four graphs.** Zep is closest (semantic + temporal). The integration gap on this layer is concrete and demonstrable.

## Specific approaches

### Microsoft GraphRAG (arxiv 2404.16130)

Entity-relationship extraction → Leiden community detection → hierarchical summarization. Knowledge graphs boosted precision to 99% in some benchmarks; "correct" answers went 50% → 80% on annual-report analysis tasks.

**Our restatement:** `[ASSERTED]` (vendor-published; see [Microsoft GraphRAG source](../source/microsoft-graphrag-2404.md)). Construct-validity note: annual-report analysis ≠ agentic-memory recall on code; the 50→80% delta is suggestive but not directly applicable. The Leiden-community-summarization pattern is structurally interesting and is what Cognee partially imitates.

### GAM — Hierarchical Graph-based Agentic Memory (Apr 2026, arxiv 2604.12285)

**Decouples encoding from consolidation.** Event Progression Graph (active dialogue) integrates into Topic Associative Network only on semantic shifts.

**Our restatement:** Aligns with the LightMem-style "sensory → short-term → long-term" staging, but graph-shaped instead of summary-shaped. The decoupling pattern is right; the question is whether the topic-associative-network primitive scales.

### MAGMA — Multi-Graph Agentic Memory (Jan 2026, arxiv 2601.03236)

**Orthogonal semantic, temporal, causal, and entity graphs** with policy-guided traversal. Reports outperforming SOTA on LoCoMo and LongMemEval.

**Our restatement:** This is the **first paper to operationalize the four-graph structure** the seven-layer stack proposes. Direct architectural reference for the multi-graph memory layer. Construct-validity note: LoCoMo/LongMemEval are conversational benchmarks; replication on agent-memory regimes (code, reasoning traces) is missing.

### A-MEM — Zettelkasten-inspired (NeurIPS 2025, arxiv 2502.12110)

**Dynamic indexing and linking** — new memories trigger updates to historical representations. Interconnected knowledge networks rather than fixed graph at write time.

**Our restatement:** A-MEM's update-on-write pattern is the natural opposite of admission control: admission rejects low-value memories *before* writing; A-MEM modifies the existing graph *during* write. The two are complementary, not competing.

## The "long context is not memory" thesis

`[ASSERTED]` ([9-challenges survey](../source/memory-surveys-2026.md)). 200K-token windows underperform purpose-built memory systems on selective retrieval. This is the single most important defense of graph-memory (and memory architectures generally) against the "context windows will solve it" objection.

## Graph-memory failure modes (worth knowing)

- **Write-path latency.** Zep's documented post-ingestion lag is direct evidence: graph extraction is expensive. Async by default.
- **Pre-filter problems.** Neo4j (Zep's backend) does not allow pre-filtering on vector indexes. Graph databases are structurally not designed for the filtered-vector-search pattern.
- **Memory footprint.** Zep reports ~600,000 tokens per conversation vs ~1,764 for Mem0 — ~300× cost of the temporal/graph layers.

These are real billion-scale red flags; they don't invalidate the architecture but bound where it can live.

## What multi-graph buys you vs single-graph

`[SPECULATED]` (deep-dive §10 hypothesis). The four orthogonal graphs are claimed to provide **complementary** failure modes — when one graph fails to retrieve (e.g., semantic similarity misses), another might succeed (e.g., causal-link traversal). This is the same logic as hybrid dense+sparse retrieval, applied at the graph layer.

We have no empirical evidence at billion scale; MAGMA's LoCoMo results are at conversational scale.

## Role in Kyrja thesis

- Anchors the **Multi-Graph Memory layer** of [seven-layer stack](./seven-layer-stack.md).
- Frames why [Zep](../incumbent/zep.md) is the closest incumbent (~2.5 layers covered) on the integration-gap front.
- The four-graph structure is `[SPECULATED]` — Kyrja synthesis of the [MAGMA paper](https://arxiv.org/abs/2601.03236) (which operationalizes four orthogonal graphs but at conversational scale) plus the deep-dive's §10 hypothetical. **Not yet load-bearing for the wedge product** — the MTP touches admission + embedding + retrieval, not multi-graph memory. Multi-graph memory is post-wedge.

## Related

- [Zep incumbent page](../incumbent/zep.md) — single-graph (semantic + temporal) production analog.
- [Cognee incumbent page](../incumbent/cognee.md) — partial GraphRAG implementation.
- [Seven-layer stack](./seven-layer-stack.md) — context for the four-graph structure.
- [Cascading-failures product](./cascading-failures.md) — graph memory does not eliminate the cascade; it offers an orthogonal retrieval path.

## Source archive

Concept synthesized from deep-dive §8 (graph-based systems) + §10 (multi-graph memory layer). See agentic-memory-scaling-deep-dive.md, lines 747-757 and 994-1001.
