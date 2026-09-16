---
type: incumbent
name: Zep / Graphiti
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: [source/zep-graphiti-2501.md]
tags: [incumbent, integration-gap, temporal-memory]
---

## What it does

Temporal-knowledge-graph memory system. Neo4j (v5.26+) is the single backend for both knowledge graph and vector indexing (HNSW via Apache Lucene, 1024-dim float32). Three-layer knowledge graph: Episodic (raw events) → Semantic Entity → Community (clusters with summaries). Triple hybrid retrieval (cosine + Okapi BM25 + breadth-first graph traversal) with **no LLM calls during retrieval** — all index-based. Reranking stack: RRF, MMR, graph-episode/node-distance rerankers, cross-encoder LLMs only at final scoring. Explicit event time + ingestion time + validity windows; conflict detection/resolution baked in. Graphiti is the open-source engine.

See [Zep / Graphiti paper + vendor source](../source/zep-graphiti-2501.md) for the underlying material.

## What it doesn't

- **Multi-tier storage.** Single Neo4j cluster; no hot/warm/cold tiers, no object-storage fallback.
- **Multi-vector embedding.** Single-vector dense (1024-dim).
- **Other graph types.** Temporal graph is excellent; semantic-entity and community subgraphs exist, but the *causal* and *structural-code* graphs from [seven-layer stack](../concept/seven-layer-stack.md) are not built.
- **Synchronous post-ingest retrieval.** Vendor-acknowledged: "immediate post-ingestion retrieval often fails; correct answers appear hours later after background graph processing." Graph extraction is expensive and asynchronous.
- **Pre-filter on vector indexes.** Neo4j does not allow this — a structural limitation of the chosen backend.
- **Low memory footprint.** Reported >600,000 tokens per conversation vs ~1,764 for Mem0 — ~300× multiple, the cost of the temporal/graph layers.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ✗ |
| Embedding | ◐ — single-vector dense (1024-dim, cosine) |
| Multi-Graph Memory | ◑ — episodic + semantic-entity + community + temporal; ~1.5 of the 4 graphs (temporal is the differentiator) |
| Tiered Storage | ✗ |
| Retrieval | ✓ — triple hybrid is genuinely strong; no-LLM-at-retrieval is a real architectural property |
| Consolidation | ◐ — community-clustering + asynchronous graph processing is consolidation-adjacent |
| Governance | ✗ |

**Net: ~2.5 of 7 layers materially covered.** The most layer-covering incumbent in the set, primarily because of the graph layer.

## Where it fails

- **Write-path latency.** Post-ingest retrieval lag is direct empirical support for the consolidation-layer claim (graph extraction is expensive enough to be deferred in practice).
- **Memory footprint.** 300× Mem0 is a billion-scale red flag — temporal graph + community clustering does not have a clear path to 1B vectors on commodity hardware.
- **Backend lock-in.** Neo4j-only commitment forecloses tiered storage and multi-vector escapes.
- **Community Edition deprecated Apr 2025.** Self-hosting requires provisioning multiple systems; the open-path is narrowing.

## Adoption signal

~14,000 GitHub stars in 8 months on Graphiti. 25,000 weekly PyPI downloads. Production in CRM, compliance, healthcare.

## Related

- [Zep / Graphiti source](../source/zep-graphiti-2501.md).
- [Mem0](./mem0.md) — the system Zep markets against.
- [Seven-layer stack](../concept/seven-layer-stack.md).
- [Cascading-failures product](../concept/cascading-failures.md).
