---
type: source
name: "Zep / Graphiti — Temporal Knowledge Graph for Agent Memory (arxiv 2501.13956)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [incumbent-anchor, integration-gap, temporal-memory]
---

## Citation

Zep team. *Zep: A Temporal Knowledge Graph Architecture for Agent Memory.* arXiv:2501.13956, Jan 2025. Plus Graphiti open-source engine and Neo4j integration material.

## Location

- arXiv: https://arxiv.org/abs/2501.13956
- Concepts: https://help.getzep.com/concepts
- Graphiti GitHub: https://github.com/getzep/graphiti
- Neo4j integration write-up: https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/
- Neo4j vector index docs: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- Configuration: https://help.getzep.com/graphiti/configuration/neo-4-j-configuration
- Comparative (Atlan): https://atlan.com/know/zep-vs-mem0/

## Key claims (with our restatements)

### Architecture

**Paper/vendor:** Neo4j (v5.26+) for both knowledge graph and vector indexing. 1024-dim float32 vectors, cosine similarity, HNSW via Apache Lucene. BM25 full-text indexes alongside. Triple hybrid retrieval (cosine + BM25 + breadth-first graph traversal) with no LLM calls during retrieval. Three-layer knowledge graph: Episodic (raw events) → Semantic Entity → Community subgraph. Explicit event time + ingestion time with validity windows for facts.

**Our restatement:** Zep is the most temporal-aware incumbent. The "no LLM at retrieval" property is a real differentiator — predictable latency, no per-query cost. Storage is still HNSW at the leaves; the temporal/graph layers sit on top. Neo4j is a single-storage-tier commitment.

### Vendor benchmarks

**Paper/vendor:** 94.8% DMR accuracy (vs 93.4% MemGPT). P95 retrieval latency 300ms (90% reduction vs vector-only). Up to 18.5% accuracy improvement over baselines.

**Our restatement:** `[ASSERTED]`. DMR (Deep Memory Retrieval) is Zep's own benchmark; comparison to MemGPT on a vendor benchmark inherits the construct-validity concern that lights up most incumbent claims.

### Acknowledged limitations

**Paper/vendor:** Neo4j does not allow pre-filtering on vector indexes. Memory footprint exceeds 600,000 tokens per conversation (vs ~1,764 for Mem0). Immediate post-ingestion retrieval often fails; correct answers appear hours later after background graph processing. Self-hosting requires provisioning multiple systems. Community Edition was deprecated Apr 2025.

**Our restatement:** The 300x memory-footprint multiple vs Mem0 is the cost of the temporal/graph layers. The "post-ingestion retrieval lag" is a write-path bottleneck — temporal-graph extraction is expensive enough to be deferred. Both are billion-scale red flags.

### Adoption signal

~14,000 GitHub stars in 8 months for Graphiti; 25,000 weekly PyPI downloads. Production in CRM, compliance, healthcare.

## Relevance to Kyrja

- Anchors [Zep incumbent page](../incumbent/zep.md).
- Zep occupies the **multi-graph memory + retrieval layers** of [seven-layer stack](../concept/seven-layer-stack.md) most fully of any incumbent — but only one of the four graphs (temporal). Does not address admission control, multi-vector embedding, or tiered storage.
- The post-ingestion retrieval lag is direct empirical support for the consolidation-layer claim: graph extraction is expensive and asynchronous in practice.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify any specific claim.
