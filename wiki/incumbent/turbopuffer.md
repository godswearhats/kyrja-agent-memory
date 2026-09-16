---
type: incumbent
name: Turbopuffer
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: []
tags: [incumbent, vector-db, substrate, object-storage-first]
---

## What it does

**Object-storage-first vector database** with attached compute. Built on the principle that vector indexes are read-heavy and bursty, so storing them on S3-class object storage (with compute attached on demand) collapses the cost-at-scale problem. Pricing: ~$1/M-vec/month + $4/M-queries.

Production references: powers Cursor and Notion at 3.5T+ documents combined. See vendor docs at turbopuffer.com/docs/architecture.

## What it doesn't

- **Memory-system semantics.** Turbopuffer is a substrate, not an agent-memory product. No admission control, no consolidation, no graph layer, no governance — just vector storage and search.
- **Multi-vector retrieval as a first-class feature.** Single-vector dense + filter is the canonical pattern.
- **Strong consistency.** Object-storage-first architecture inherits S3-class eventual consistency on the write side.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

Covers **1 layer** — tiered storage. Specifically the *cold* tier (object storage) with hot-tier compute attached on demand. The substrate is excellent; the layers above it (admission, embedding strategy, graph, consolidation, governance) are entirely user responsibility.

## Where it fails

- **Not a memory system.** Treating Turbopuffer as agentic memory means re-implementing the other six layers on top, which is exactly the integration-gap problem.
- **Latency tail.** Cold-start queries against object storage have a latency floor. For interactive agent workloads, this needs caching that lives outside Turbopuffer.

## Role in Kyrja thesis

Turbopuffer is the canonical reference for [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md): "Storage cost is no longer the binding constraint at billion scale." It is the substrate side of the affordability claim; whether the *layered system above it* is also affordable is the open question at [cost-curve-at-scale](../open-question/cost-curve-at-scale.md).

## Related

- [beyond-hnsw-approaches](../concept/beyond-hnsw-approaches.md) — Turbopuffer is the canonical object-storage-first example
- [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) — the framing this incumbent anchors
- [seven-layer-stack](../concept/seven-layer-stack.md) — 1-of-7 coverage
