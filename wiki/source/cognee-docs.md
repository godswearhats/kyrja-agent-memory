---
type: source
name: "Cognee — vendor documentation and project material"
status: timeless
last_ingested: 2026-05-12
sources: []
tags: [incumbent-anchor, integration-gap, graph-rag]
---

## Citation

Vendor-published documentation, blog posts, and case studies. Not a single paper; a roll-up of project material as of mid-2026.

## Location

- GitHub: https://github.com/topoteretes/cognee
- Docs: https://docs.cognee.ai/core-concepts/overview
- Architecture write-up: https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory
- Benchmarks: https://www.cognee.ai/blog/deep-dives/ai-memory-evals-0825
- Research results: https://www.cognee.ai/research-and-evaluation-results
- LanceDB case study: https://www.lancedb.com/blog/case-study-cognee
- Qdrant integration: https://qdrant.tech/documentation/frameworks/cognee/
- FalkorDB integration: https://docs.falkordb.com/agentic-memory/cognee.html

## Key claims (with our restatements)

### Architecture

**Vendor:** Pluggable vector backends (LanceDB default, Qdrant, PGVector, Weaviate, Redis, DuckDB, Pinecone, ChromaDB, FalkorDB). Pluggable graph backends (Neo4j, FalkorDB, Kuzu, NetworkX). Hybrid GraphRAG retrieval with five modes (CHUNKS, SUMMARIES, INSIGHTS, GRAPH_COMPLETION, RAG_COMPLETION).

**Our restatement:** Cognee delegates indexing entirely to chosen backends — all of which use HNSW. The "graph" layer is the differentiator, not the storage primitive. This puts Cognee at the cascading-failures regime of whichever HNSW backend it sits on.

### Scale claims

**Vendor:** ~1 GB processed in ~40 minutes using 100+ containers. 1M+ pipelines/month across 70+ companies (Bayer, University of Wyoming named). Known gap acknowledged: scaling to terabyte datasets.

**Our restatement:** `[ASSERTED]` — vendor-reported, not independently verified. Scale claim is in pipelines/month, not vectors-stored or query latency. The terabyte-gap acknowledgement is unusually candid for an incumbent.

### Benchmark claims

**Vendor:** +25% Human-like Correctness, +314% DeepEval F1 (with CoT optimization); outperforms LightRAG, Graphiti, Mem0 on default settings.

**Our restatement:** `[ASSERTED]`. Construct-validity unknown — vendor-published benchmarks are systematically optimistic ("benchmark chaos" — vendors run on different datasets, honest comparison nearly impossible). Use as a directional signal, not a ground truth.

## Relevance to Kyrja

- Anchors [Cognee incumbent page](../incumbent/cognee.md).
- Cognee occupies the **graph-memory + retrieval layers** of [seven-layer stack](../concept/seven-layer-stack.md); it does not address admission control, tiered storage, multi-vector embedding, or consolidation as a billion-scale problem.
- The pluggable-backend posture means Cognee inherits the cascading-failures regime of HNSW at scale; it does not solve it.

## Archive location

Not a single artifact; rolling vendor material. To verify a specific quantitative claim, fetch from the linked URL above (claims are volatile).
