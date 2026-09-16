---
type: incumbent
name: Milvus
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: []
tags: [incumbent, vector-db, substrate, tiered-storage]
---

## What it does

**Open-source + managed vector database** from Zilliz. Milvus 2.6 added tiered storage with on-demand hot/cold loading, reporting 80% vector-search cost reduction. Strong on hybrid retrieval (dense + sparse + scalar filtering) and GPU acceleration (cuVS integration via NVIDIA).

## What it doesn't

- **Not an agent-memory product.** Substrate with strong vector-DB ergonomics.
- **No memory-system semantics** (admission control, consolidation policy, governance).
- **No graph layer** — Milvus pairs with external graph stores rather than embedding them.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

Covers **1.5 layers** — tiered storage (with explicit hot/cold tiering as a Milvus 2.6 feature) plus hybrid retrieval. Milvus is the most-tier-aware of the major vector-DB incumbents.

## Where it fails

- **At memory-system layers.** Like Pinecone/Qdrant/Turbopuffer, Milvus stops at the substrate boundary; admission, consolidation, governance are user-implemented.
- **At single-substrate optimization vs vertical specialization.** Milvus is broad — many index types, many storage modes — which can outcompete narrower substrates on flexibility but lose on per-feature performance.

## Role in Kyrja thesis

Milvus's 2.6 tiered storage is the substrate evidence that **multi-tier hot/cold is becoming default**, supporting the [beyond-hnsw-approaches](../concept/beyond-hnsw-approaches.md) thesis that the field has converged on multi-tier as a baseline. It's a reasonable substrate option for the wedge, though less aligned with the SQL-first slot-format approach than [pgvector](./pgvector.md).

## Related

- [beyond-hnsw-approaches](../concept/beyond-hnsw-approaches.md) — Milvus is a tier-aware example
- [seven-layer-stack](../concept/seven-layer-stack.md) — 1.5-of-7 coverage
- [DiskANN + SPFresh](../source/diskann-spfresh.md) — Milvus implements DiskANN, anchoring its beyond-HNSW story
