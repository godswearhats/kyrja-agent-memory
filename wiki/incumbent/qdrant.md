---
type: incumbent
name: Qdrant
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: []
tags: [incumbent, vector-db, substrate, hybrid-search]
---

## What it does

**Open-source + managed vector database** in Rust. Headline features: hybrid dense+sparse search, payload-based filtering, MUVERA-style multi-vector support (per their 2026 blog), and a Series B funding announcement positioning it as a primary substrate competitor to Pinecone.

## What it doesn't

- **Not an agent-memory product.** Substrate only; no admission control, consolidation, graph, governance.
- **No object-storage-first architecture.** Full-precision Qdrant deployments price like Pinecone at high scale.
- **No memory-specific semantics** (provenance, temporal modeling, identity).

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

Covers **1.5 layers** — vector index + hybrid retrieval. The dense+sparse hybrid is part of layer 5 (retrieval) of the seven-layer stack; not just substrate.

## Where it fails

- **At cost at scale.** Full-precision Qdrant on the high-end [scale-crossings](../concept/scale-crossings.md) scenarios projects to similar pricing pathologies as Pinecone. Quantization (RaBitQ-style) is supported but not default.
- **Hybrid-on-the-substrate isn't memory-system-hybrid.** Qdrant hybrid is dense+sparse co-retrieval at the index level. The seven-layer-stack's hybrid retrieval also incorporates BM25, cross-encoder rerank, and graph signals — none of which Qdrant provides.

## Role in Kyrja thesis

Qdrant is a substrate option for the wedge's [structured-filter-first](../decision/structured-filter-first.md) read path. It's not the architectural differentiator — the differentiator is the integration above it. Its hybrid-search capability is well-targeted for the wedge's read-path needs without forcing a graph layer.

## Related

- [beyond-hnsw-approaches](../concept/beyond-hnsw-approaches.md) — Qdrant is referenced under the hybrid family
- [multi-vector-retrieval](../concept/multi-vector-retrieval.md) — Qdrant's MUVERA support is a small-scale plus
- [seven-layer-stack](../concept/seven-layer-stack.md) — 1.5-of-7 coverage
