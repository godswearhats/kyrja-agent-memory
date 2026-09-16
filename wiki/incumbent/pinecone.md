---
type: incumbent
name: Pinecone
status_current_as_of: 2026-05-12
last_ingested: 2026-05-13
sources: []
tags: [incumbent, vector-db, substrate, serverless]
---

## What it does

**Managed vector database** with a serverless tier (Pinecone Serverless) and a pod-based tier. Headline features: filtered search (ICML 2025 paper on accurate metadata filtering in serverless), slab architecture for tier scaling, cascading multi-vector retrieval support.

## What it doesn't

- **Not an agent-memory product.** Substrate only. No admission control, consolidation, graph layer, or governance.
- **Cost transparency at scale.** Pinecone Serverless pricing applied to large [scale-crossings](../concept/scale-crossings.md) scenarios projects to $280M/yr at 2.7B vectors and $1.17B/yr at 8.5B vectors (vendor-pricing probe at `incumbent-pricing-2026-04-30.md`). This is vendor-choice pricing, not a market-wide constraint — see [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) for the contrasting Turbopuffer numbers.
- **Object-storage-first architecture.** Pinecone's slab/serverless architecture is its own design, not the S3-class pattern that Turbopuffer and LanceDB use.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

Covers **1 layer** — tiered storage / index. Pinecone Filtered Search adds limited structural-filter support, but the core product is single-vector dense + metadata filter.

## Where it fails

- **At cost.** For the high-scale scenarios in the scale model, Pinecone Serverless pricing dominates. The product is a fit for moderate-scale workloads, not 1B+ vector deployments.
- **Filtered-search pathology.** Pinecone's own ICML paper acknowledges that filter+vector queries are fast when the partition aligns with the filter selectivity, and catastrophically slow otherwise. This is the [partition-strategy](../open-question/partition-strategy.md) hazard generalized.

## Role in Kyrja thesis

Pinecone is the "price-like-cost-is-a-wall" data point in [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md). It demonstrates that vendor choice — not field-wide economics — determines whether a substrate makes billion-scale memory affordable. The wedge does not bet on Pinecone.

## Related

- [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) — contrast against object-storage-first incumbents
- [partition-strategy](../open-question/partition-strategy.md) — Pinecone Filtered Search illustrates the partition pathology
- [Turbopuffer](./turbopuffer.md), [LanceDB source](../source/lancedb.md) — object-storage-first contrast
- [seven-layer-stack](../concept/seven-layer-stack.md) — 1-of-7 coverage
