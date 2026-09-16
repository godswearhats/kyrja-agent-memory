---
type: concept
name: Beyond-HNSW Approaches
status: timeless
last_ingested: 2026-05-13
sources: [../source/diskann-spfresh.md, ../source/rabitq-2024.md, ../source/uber-opensearch-billion-scale.md]
epistemic_tags: [asserted, measured]
tags: [tiered-storage, quantization, billion-scale, beyond-hnsw]
---

## Definition

The **beyond-HNSW approaches** are the five families of vector-index architectures that the field has converged on as the post-HNSW direction. None is a drop-in HNSW replacement; each addresses a specific binding constraint that HNSW hits at billion scale ([HNSW scale limits](./hnsw-scale-limits.md)).

The Jan 2026 *Vector Search for the Future* survey (arXiv:2601.01937) traces the evolution: **all-in-memory → heterogeneous memory-SSD → memory-SSD-object-storage cloud-native**.

## The five approaches

### 1. Clustered / partition-based

**Idea:** Avoid random memory access by clustering vectors and routing queries to relevant clusters first. Examples: TurboPuffer (SPFresh-based, S3-first, SSD cache), SPANN (Microsoft), Databricks Storage Optimized (distributed K-means + PQ, 64× compression).

**Evidence:** TurboPuffer powers Cursor and Notion at 3.5T+ documents with 8-10ms cached latency. Databricks Storage Optimized achieves 1B+ vectors in <8h build time at 7× lower cost than RAM-resident HNSW. `[ASSERTED]` from [vendor production-scaling claims](../source/vendor-production-scaling-claims.md); construct-validity caveats on that page apply.

### 2. GPU-native graph indexes (CAGRA / cuVS)

**Idea:** Build the graph for GPU parallelism from the start, not as a port. **CAGRA** (NVIDIA): fixed-degree flat graph built from k-NN graph via IVF-PQ or NN-DESCENT.

**Evidence:** Build 12.3× faster; search 4.7× faster (Deep100M); throughput 18× for images, 8× for text. Integrated into Faiss v1.10.0, OpenSearch 3.0, Weaviate, Elasticsearch, Milvus. AWS OpenSearch with cuVS: **billion-scale in under an hour at 3.75× lower cost**. `[MEASURED]` (vendor-published; see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md)). *Construct-validity:* comparisons are vendor-published GPU-vs-CPU; standardized benchmarks generally confirm the directional ordering, but the agentic-memory write profile is not the test workload.

### 3. Hybrid (HNSW-IF, SPANN, B+ANN)

**Idea:** Use HNSW only for the small high-memory "centroid" set; route to disk-resident inverted files or B+ trees for the rest. Examples: Vespa HNSW-IF, Microsoft SPANN, B+ANN (Nov 2025, supports dissimilarity queries which HNSW cannot).

**Evidence:** Vespa achieves order-of-magnitude memory reduction vs pure HNSW at billion scale.

### 4. RaBitQ-powered (extreme compression, provably bounded)

**Idea:** Compress vectors at the bit-level with formal error bounds, then run any index on top. See [RaBitQ source page](../source/rabitq-2024.md).

**Evidence:** Elasticsearch BBQ: 95% memory reduction, 20-30× less quantization time. **VectorChord: 1B+ vectors on a single 128GB-RAM PostgreSQL machine.** The latter is the load-bearing evidence that quantization has structurally shifted billion-scale economics.

### 5. Object-storage-first

**Idea:** Treat S3 / object storage as the primary tier; RAM and SSD are caches. Examples: TurboPuffer (3.5T+ docs, 100× cost reduction), Amazon S3 Vectors (40B+ ingested, 90% cost reduction GA in 2025), LanceDB-on-S3 (1B+ reference architecture).

**Production scaling table** (all `[ASSERTED]` vendor-reported; see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md). Construct-validity: cost-reduction percentages are vs prior-generation vendor offerings, not vs a uniform baseline):

| System | Architecture | Scale | Cost claim |
|---|---|---|---|
| TurboPuffer | S3-first, SSD cache, clustered | 3.5T+ docs (Cursor, Notion) | 100× reduction |
| Amazon S3 Vectors | Native vectors in object storage | 40B+ ingested | 90% reduction |
| Milvus 2.6 | RAM → SSD → Object Storage | 4.3× more data, same HW | 80% reduction |
| Databricks SO | Object storage + PQ | 1B+ in <8h | 7× reduction |
| LanceDB on S3 | Lance format on S3 | 1B+ reference architecture | S3 pricing |
| Google Vertex AI 2.0 | ScaNN, managed | 1B at 9.6ms P95 | Managed |
| IBM CAS | Custom, GPU-accelerated | 100B prototype | 13 days build |

## The DiskANN-and-successors family

See [DiskANN + SPFresh source page](../source/diskann-spfresh.md). DiskANN indexes 1B vectors at ~95% recall with ~5ms latency on a single node; SPFresh adds incremental updates at 1% DRAM / <10% CPU. DiskANN is now first-class in **SQL Server 2025 / Azure SQL** (Enterprise GA), making "beyond HNSW" available as a commodity database feature, not just research.

## What these approaches do *not* solve

- **Embedding-side limits.** RaBitQ compresses storage; it does not raise the [LIMIT bound](../source/weller-2025-limit.md) representational ceiling or fix [embedding collapse](./embedding-collapse.md).
- **The agentic-memory write profile.** Most production billion-scale deployments (Uber, TurboPuffer-on-Cursor) are predominantly write-once or batched-update workloads. Continuous-write agentic memory has not been replicated at billion scale on any of these architectures.

## Role in Kyrja thesis

- Anchors **the tiered storage layer** of [seven-layer stack](./seven-layer-stack.md) (Hot HNSW+RaBitQ / Warm DiskANN / Cold S3-Vectors).
- Anchors **the GPU-indexing aside** of the same stack (CAGRA for bulk ingestion).
- Closes the deep-dive's "every component exists in production or research" claim on the storage/indexing side. The remaining gap is integration, not invention.

## Filtered vector search (sub-topic worth surfacing)

`[ASSERTED]` (see [Pinecone filtered vector source](../source/pinecone-filtered-vector-icml-2025.md)). Three strategies: pre-filtering, post-filtering, integrated/in-algorithm filtering. **Pinecone (ICML 2025)** achieved mean recall@10 of 0.989 across all selectivity ranges on YFCC via immutable vector slabs in LSM-tree on object storage. Reddit (340M+ vectors): metadata filtering was the **primary bottleneck**, P99 latency jumping 10× when crossing between vector graph and relational metadata store.

This matters for our [structured filter-first decision](../decision/structured-filter-first.md) — filtering is the layer most likely to break in naive implementations and the layer Pinecone has invested most in.

## Multi-vector retrieval

See [multi-vector retrieval](./multi-vector-retrieval.md) for the ColBERT/MUVERA/SPLADE family. Conceptually adjacent to the beyond-HNSW approaches but distinct: multi-vector changes the *representation*, beyond-HNSW changes the *index*.

## Related

- [HNSW scale limits](./hnsw-scale-limits.md) — the problem these approaches address.
- [Embedding collapse](./embedding-collapse.md) — the orthogonal problem; not addressed by beyond-HNSW.
- [Multi-vector retrieval](./multi-vector-retrieval.md) — the representation-side escape.
- [Seven-layer stack](./seven-layer-stack.md) — the integrated architecture incorporating these approaches.
- All [incumbents](../incumbent/cognee.md) — each delegates to a single HNSW-class backend, foregoing this family.

## Source archive

Concept synthesized from deep-dive §7 (agentic-memory-scaling-deep-dive.md, lines 557-727).
