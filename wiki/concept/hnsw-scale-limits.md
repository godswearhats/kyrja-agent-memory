---
type: concept
name: HNSW Scale Limits
status: timeless
last_ingested: 2026-05-13
sources: [../source/hnsw-real-time-updates-2407.md, ../source/uber-opensearch-billion-scale.md]
epistemic_tags: [measured, asserted]
tags: [hnsw, recall-cascade, scale-thesis, mode-1, mode-3, mode-4]
---

## Definition

The **HNSW scale limits** are the four ways HNSW (Hierarchical Navigable Small World) degrades as the index grows past the million-vector regime: recall, memory, latency/build-time, and update-induced unreachability. Three of the four modes (recall degradation, hub distortion, unreachable points) are direct ingredients of the [cascading-failures product](./cascading-failures.md).

## Recall degradation

`[ASSERTED]` (vendor benchmarks and survey literature — see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md) and [memory-surveys-2026](../source/memory-surveys-2026.md); construct-validity note: benchmarks use varied configurations and datasets, so the figures are directional, not commensurable):

| Scale | Recall (same configuration) |
|---|---|
| 10K vectors | ~99% |
| 10M vectors | ~85% |
| 100K pages, real corpus | measurable 12% performance hit |

Retrieval quality degrades **silently** as the database grows; latency can stay flat while recall slides.

**Mechanisms:**

- **Hubness problem.** Some vectors become "hubs" appearing as neighbors to a disproportionate number of points. At scale, hubs dominate search paths — queries are pulled toward heavily-connected nodes regardless of true similarity. This is **mode 3** of the [cascading-failures product](./cascading-failures.md).
- **Graph fragmentation.** Frequent insertions/deletions degrade the "small world" property of the navigation graph. Disconnected islands emerge.
- **Intrinsic dimensionality.** Higher intrinsic dimensionality of the corpus → worse recall at any scale.

## Memory requirements

Formula: `num_vectors × (dimensions × 4 bytes + M × 2 × 4 bytes + overhead)`. With M=16, float32:

| Dimensions | 100M vectors | 1B vectors |
|---|---|---|
| 768 | ~45 GB | ~450 GB |
| 1536 | ~77 GB | ~770 GB |
| 3072 | ~141 GB | ~1.4 TB |

`[MEASURED]` via vendor calculators (Lantern, Zilliz; see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md)). Construct-validity note: these are RAM-resident-index estimates assuming float32 vectors at standard M=16 graph degree; quantization or RaBitQ-class compression (see [RaBitQ source](../source/rabitq-2024.md)) collapses these numbers ~10-30×.

At 1B vectors / 1536d: typically >$10K/month on cloud instances. **Cost, not feasibility, is the binding constraint at this scale.**

## Query latency

| Scale | HNSW latency |
|---|---|
| 1M | 2-10 ms (SIFT1M: ~95% recall@10 in 1-2 ms) |
| 1-10M | 10-30 ms (jumps to 100s of ms at memory constraints) |
| 100M | <5 ms in-memory; requires ~500 GB RAM |
| 1B (hybrid) | ~50 ms (order-of-magnitude higher than pure in-memory) |

`[MEASURED]` (vendor and ANN-Benchmarks data; see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md)). Latency stays acceptable across scales *when memory is provisioned*; the latency cliff appears when the index spills out of RAM. *Construct-validity:* figures are from ANN-Benchmarks synthetic corpora (SIFT/GIST/GloVe) and vendor lab configurations; agentic-memory workloads with homogeneous-code embeddings and continuous writes may behave differently.

## Index build time

| Configuration | Build time |
|---|---|
| 100M vectors, CPU | ~1.5 hours |
| 160M vectors, CPU | 3-6 hours |
| 1B vectors, CPU | 10+ hours to days |
| 1B vectors, GPU (CAGRA) | ~2 hours |

`[MEASURED]` (see [vendor production-scaling claims](../source/vendor-production-scaling-claims.md) for CAGRA / cuVS numbers). CPU-only billion-scale builds are operationally painful; GPU-native indexes (CAGRA via cuVS) are the practical path.

## Update degradation

`[MEASURED]` ([source: MN-RU paper](../source/hnsw-real-time-updates-2407.md); construct-validity note: figures are from controlled benchmark configurations, not production agentic-memory workloads):

- After ~200 update iterations, **3-4% of points become permanently unreachable** from the graph entry point.
- In pgvector: insertion rate drops to **~3 rows/second** at millions of rows.
- HNSW index causes degradation even on UPDATE statements that don't touch the vector columns.
- Redis (specialized infrastructure): 66K vector insertions/second sustainable at billion scale.

This is **mode 4** of the [cascading-failures product](./cascading-failures.md). Critical for agentic memory specifically, which writes continuously.

## HNSW vs alternatives at billion scale

| Metric | HNSW | DiskANN | IVF-PQ |
|---|---|---|---|
| Memory (1B, 768d) | ~500 GB+ RAM | ~32 GB RAM + SSD | Low (compressed) |
| Latency | <5 ms (in-memory) | 5-20 ms (NVMe) | 10-50 ms |
| Recall@90% QPS | ~2,165 | ~2,597 | Lower |
| Build time | Hours to days | Hours | Faster than HNSW |
| Dynamic updates | Supported (with degradation) | Supported | Requires rebuild |
| Cost at 1B | >$10K/month | Fraction of HNSW | Lowest |

`[ASSERTED]` (synthesis of [DiskANN + SPFresh source](../source/diskann-spfresh.md), [vendor production-scaling claims](../source/vendor-production-scaling-claims.md), and the cited HNSW papers). Construct-validity note: numbers are cross-vendor synthesis; not all rows are commensurable. The directional ordering (HNSW most expensive at 1B, DiskANN/IVF-PQ cheaper) is robust across sources, but the per-row magnitudes are vendor-published and not third-party-replicated.

## Production billion-scale evidence

[Uber's OpenSearch deployment](../source/uber-opensearch-billion-scale.md) operates 1.5B items at ~400-dim with P99 <120ms and 4TB index — proving billion-scale HNSW is *technically achievable* at low dimensionality with significant engineering investment. The deployment is **not** in the agentic-memory regime (high d, continuous updates, instruction-conditioned queries), and so does not refute the cascading-failures claim for that regime.

## Role in Kyrja thesis

- Source for **modes 1, 3, and 4** of the [cascading-failures product](./cascading-failures.md).
- Frames the integration gap: every [incumbent](../incumbent/cognee.md) delegates to HNSW under the hood and inherits these limits.
- Motivates the "beyond HNSW" portion of [seven-layer stack](./seven-layer-stack.md) tiered-storage and admission-control layers — concept page pending (F-deep-3).

## Related

- [Cascading-failures product](./cascading-failures.md) — the synthesis that makes these limits load-bearing.
- [Embedding collapse](./embedding-collapse.md) — the orthogonal recall-degradation mode (mode 2) operating in the embedding space.
- All five incumbent pages: [cognee](../incumbent/cognee.md), [mem0](../incumbent/mem0.md), [zep](../incumbent/zep.md), [lightmem](../incumbent/lightmem.md), [letta](../incumbent/letta.md) — all inherit these limits via their chosen HNSW backend.

## Source archive

Concept synthesized from deep-dive §5 (agentic-memory-scaling-deep-dive.md, lines 375-456).
