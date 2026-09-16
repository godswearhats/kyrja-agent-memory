---
type: source
name: "Uber — Powering Billion-Scale Vector Search with OpenSearch"
status: timeless
last_ingested: 2026-05-12
sources: []
tags: [hnsw, production-evidence, billion-scale]
---

## Citation

Uber Engineering. *Powering Billion-Scale Vector Search with OpenSearch.* Blog post, late 2025.

## Location

- Uber blog: https://www.uber.com/us/en/blog/powering-billion-scale-vector-search-with-opensearch/
- InfoQ summary: https://www.infoq.com/news/2025/12/uber-opensearch-vector-semantic/

## Key claims (with our restatements)

### Concrete production billion-scale anchor

**Vendor:** 1.5B items at ~400-dim vectors on OpenSearch. P99 at 2K QPS reduced from ~250ms to <120ms (52% improvement). Index size reduced from 11TB to 4TB by disabling `_source` and `doc_values`. Ingestion time reduced from 12h to 2.5h via optimized bulk indexing. Blue/green deployment for zero-downtime refresh. gRPC Bulk API yielded 20-35% runtime reduction.

**Our restatement:** This is the **most detailed public billion-scale HNSW production deployment** the deep-dive identifies — better documented than Pinecone customer references or Reddit's 340M case. It establishes that 1.5B is achievable, at low dimensionality (400d, not 1536d), with massive engineering investment. Construct-validity for our argument: Uber operates at 400d which sits *below* the LIMIT-bound regime, and uses OpenSearch HNSW with significant operational discipline.

### What the deployment does *not* prove

- **Dimensionality:** 400d is well below the d=1536 regime our scale thesis targets. The [LIMIT bound](./weller-2025-limit.md) at 400d is generous; at 1536d the per-dimension capacity headroom is much smaller relative to corpus size.
- **Update profile:** Uber's vectors are largely write-once at index build time; agentic memory's continuous write/update load is structurally different (see [HNSW real-time updates](./hnsw-real-time-updates-2407.md)).
- **Query distribution:** Uber's queries are likely natural-language Q&A; the LIMIT-bound exposure is concentrated on instruction-conditioned and predicate-composition queries.

## Relevance to Kyrja

- Anchors the "billion-scale is technically achievable, but the engineering cost is enormous, and the regime is not the agentic-memory regime" position in [HNSW scale limits](../concept/hnsw-scale-limits.md).
- Acts as a load-bearing **counter-anchor**: when our thesis says "HNSW breaks at billion scale," Uber's deployment proves the claim is regime-dependent, not absolute. Sharpens our claim from "HNSW breaks at 1B" to "HNSW breaks at 1B under the agentic-memory regime (high d, continuous updates, instruction-conditioned queries)."

## Archive location

Blog post, fetch live for current state. The InfoQ summary version is stable.
