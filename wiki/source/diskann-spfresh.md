---
type: source
name: "DiskANN (NeurIPS 2019) and SPFresh (SOSP 2023)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [beyond-hnsw, billion-scale, tiered-storage]
---

## Citation

Two complementary works underpinning the beyond-HNSW transition for billion-scale indexes:

1. *DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node.* NeurIPS 2019.
2. *SPFresh: Incremental In-Place Update for Billion-Scale Vector Search.* SOSP 2023.

## Location

- DiskANN paper PDF: https://suhasjs.github.io/files/diskann_neurips19.pdf
- DiskANN MSR project: https://www.microsoft.com/en-us/research/project/project-akupara-approximate-nearest-neighbor-search-for-large-scale-semantic-search/
- SPFresh (ACM): https://dl.acm.org/doi/10.1145/3600006.3613166
- SQL Server 2025 DiskANN GA: https://devblogs.microsoft.com/azure-sql/sql-server-2025-ctp-2-1-diskann-improvements/
- Independent comparison: https://www.tigerdata.com/learn/hnsw-vs-diskann

## Key claims (with our restatements)

### DiskANN

**Paper:** Billion-scale ANN on a single node. Indexes up to 1B vectors at ~95% recall with ~5ms latency, using **5-10× more points per machine than HNSW** by keeping the graph on SSD and only the entry/navigation nodes in memory.

**Our restatement:** DiskANN is the canonical "beyond HNSW" approach: the graph structure stays, but storage decouples from RAM. Memory drops 10-30× at modest latency cost. Production-validated: integrated into SQL Server 2025 / Azure SQL public preview as a first-class index type.

**Construct-validity note:** 95% recall and 5ms latency are benchmark numbers on standardized billion-scale ANN benchmarks (SIFT1B, DEEP1B). Real corpora at higher d (1536+) and with continuous updates have not been replicated to the same recall/latency point in published work.

### SPFresh

**Paper:** Adds **LIRE (Lightweight Incremental REbalancing)** to enable in-place updates on DiskANN-class indexes. Achieves billion-scale freshness with **~1% DRAM and <10% CPU** vs full rebuilds.

**Our restatement:** Solves the "DiskANN can't handle continuous writes" gap that initially limited its applicability to memory systems. SPFresh is the foundation underneath TurboPuffer's clustered-index design — production-validated at 3.5T+ documents.

**Construct-validity note:** SPFresh published numbers are for adversarial benchmarks; production deployments report similar order-of-magnitude wins but exact numbers are vendor-internal.

### What DiskANN/SPFresh do *not* solve

- **Single-node by default.** Billion-scale on one node, yes — but trillion-scale requires sharding or hybrid architectures on top (SPANN, TurboPuffer's clustered design).
- **Embedding-side limits.** The LIMIT bound and embedding collapse still apply — DiskANN improves index efficiency, not representational capacity.

## Relevance to Kyrja

- Anchors the **tiered-storage layer** of [seven-layer stack](../concept/seven-layer-stack.md) (Warm-tier candidate; DiskANN on NVMe).
- Sources [beyond-HNSW approaches](../concept/beyond-hnsw-approaches.md) and the "every layer exists in production or research" argument of the integration-gap leg.
- DiskANN+SPFresh demonstrate that the engineering exists; the gap is integration, not invention.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv / ACM to verify specific configuration numbers.
