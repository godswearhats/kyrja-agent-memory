---
type: source
name: "Vendor production-scaling claims (TurboPuffer, Databricks, CAGRA, S3 Vectors, etc.)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [vendor-claims, beyond-hnsw, billion-scale, pending-verbatim-read]
---

## Purpose

This page aggregates **vendor-reported production-scaling claims** that the [beyond-HNSW approaches](../concept/beyond-hnsw-approaches.md) concept page draws on. Each claim is sourced from vendor blog posts, press releases, or product docs — not from independent third-party benchmarks. Treat as `[ASSERTED]` vendor-published with construct-validity caveats below.

This page exists because the deep-dive synthesized these into a single production-scaling table; per evidence-anchoring discipline we now atomize the underlying vendor anchors.

## Citations and locations

### TurboPuffer (S3-first, SSD-cached clustered architecture)

- Vendor site: https://turbopuffer.com
- Architecture blog posts (vendor-published).
- **Claim:** powers Cursor and Notion at 3.5T+ documents with 8-10ms cached latency; ~100× cost reduction vs RAM-resident HNSW.

### Databricks Storage Optimized (distributed K-means + PQ)

- Databricks vector-search docs and engineering blog (vendor-published).
- **Claim:** 1B+ vectors in <8h build time at 7× lower cost than RAM-resident HNSW; 64× compression.

### NVIDIA CAGRA / cuVS (GPU-native graph index)

- NVIDIA blog and cuVS docs.
- AWS OpenSearch integration: vendor co-published with NVIDIA.
- **Claim:** build 12.3× faster; search 4.7× faster on Deep100M; throughput 18× for images, 8× for text. AWS OpenSearch + cuVS: billion-scale build in under an hour at 3.75× lower cost.

### Amazon S3 Vectors (native vectors in object storage)

- AWS announcement (2025 GA).
- **Claim:** 40B+ vectors ingested; ~90% cost reduction vs prior pattern.

### Milvus 2.6 tiered storage

- Zilliz/Milvus 2.6 release blog (vendor-published).
- **Claim:** 4.3× more data on same hardware via RAM → SSD → object-storage tiering; ~80% cost reduction.

### LanceDB on S3

- LanceDB docs (vendor-published).
- **Claim:** 1B+ vectors reference architecture on S3.

### Google Vertex AI 2.0 (ScaNN)

- Google Cloud blog (vendor-published).
- **Claim:** 1B vectors at 9.6ms P95.

### IBM CAS (custom GPU-accelerated)

- IBM research blog (vendor-published).
- **Claim:** 100B-vector prototype; 13-day build time.

## Construct-validity caveats (apply to all of the above)

1. **Vendor-published, not third-party-replicated.** Each magnitude is the vendor's own measurement on their own infrastructure with their own workload. Independent replication exists for very few; cross-vendor comparisons (cost-reduction "vs prior-generation") are vs each vendor's own prior offering, not against a uniform baseline.
2. **Workload mismatch.** Most demonstrations are write-once or batched-update (e.g. Cursor's code indexing). **Continuous-write agentic-memory workloads have not been replicated** on any of these architectures at billion scale.
3. **Recall not always reported.** Latency and cost numbers are headline; recall at the configured operating point is sometimes implicit or missing. The construct-validity note on the [HNSW scale limits](../concept/hnsw-scale-limits.md) page applies here: latency stays acceptable *when memory is provisioned*; recall stays acceptable *for the benchmark's distribution*.
4. **Not read verbatim.** Per [feedback_load_bearing_sources], specific magnitudes on this page are paraphrased from vendor blog posts and the deep-dive's framing; primary sources have not been audited line-by-line.

## Relevance to Kyrja

- Sources [beyond-HNSW approaches](../concept/beyond-hnsw-approaches.md) production-scaling claims (lines 23, 47).
- Anchors the [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) page's vendor pricing claims.
- Direct evidence that the storage cost of billion-scale vector retrieval has structurally shifted in 2024-2025 — but **not** evidence about the recall leg or the agentic-memory continuous-write regime.

## Promotion path

If any specific vendor claim becomes load-bearing for a Kyrja decision (e.g., the wedge product chooses Databricks SO or TurboPuffer as the substrate), split that vendor's claims into a dedicated `source/<vendor>-2026.md` page with verbatim quotes and accessed-on dates.

## Archive location

Vendor blog posts and product docs — not in `library/papers/`. URLs above; fetch live for verbatim verification before any production decision.
