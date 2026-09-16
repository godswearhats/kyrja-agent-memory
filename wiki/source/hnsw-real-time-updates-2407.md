---
type: source
name: "Real-Time HNSW Updates and MN-RU (arxiv 2407.07871)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [hnsw, update-degradation, recall-cascade]
---

## Citation

*MN-RU: Mitigating Neighbor Removal-induced Unreachable Points in Real-Time HNSW Updates.* arXiv:2407.07871. v2.

## Location

- arXiv: https://arxiv.org/html/2407.07871v2

## Key claims (with our restatements)

### The unreachable-points failure mode

**Paper:** Under sustained insertion/deletion cycles, HNSW's incremental rebalancing leaves a measurable fraction of indexed points **structurally unreachable** from the graph entry point. After ~200 update iterations in standard configurations, **3-4% of points are permanently unreachable** — they remain in storage but no query can find them.

**Our restatement:** This is mode 4 of the [cascading-failures product](../concept/cascading-failures.md). Distinct from recall degradation due to embedding crowding or hub distortion — these points are lost to the index itself, not to the embedding. The failure compounds with corpus age, not corpus size.

### Mitigation (MN-RU)

The paper proposes a Neighbor Removal-induced Unreachable points mitigation strategy that re-attaches orphaned neighborhoods on a continuous schedule.

**Our restatement:** This is a *mitigation*, not an elimination — it reduces the unreachable fraction but does not zero it. And the mitigation runs at additional cost, which production deployments (pgvector, vendor backends) generally do not enable by default.

### Supporting production evidence

The paper aligns with [pgvector issue #875](https://github.com/pgvector/pgvector/issues/875) (degradation under updates) and [pgvector issue #810](https://github.com/pgvector/pgvector/issues/810) (insertion rate dropping to ~3 rows/second at millions of rows).

## Relevance to Kyrja

- Anchors the **mode-4 (unreachable-points)** term of the [cascading-failures product](../concept/cascading-failures.md).
- Anchors the "Update Degradation" subsection of [HNSW scale limits](../concept/hnsw-scale-limits.md).
- For agentic memory specifically: agentic systems write *continuously* (every session adds memories) and delete/update (consolidation, dedup). This is the literal worst-case operating regime for HNSW's update-degradation mode.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify the 3-4% number against the specific configuration tested.
