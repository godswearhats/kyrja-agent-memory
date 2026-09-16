---
type: concept
name: Caddy tier semantics — multi-tier storage with semantics deferred to silicon mapping
status: living
last_ingested: 2026-06-10
sources: [../source/wu-2022-memorizing-transformer.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, architecture, deferred-decision, storage, hardware]
---

## Definition

`[ASSERTED]` **Tier semantics deferred to silicon** is the architectural commitment that the [caddy](./caddy.md) has an **N-tier storage architecture with capacity-bounded tiers and salience-modulated promotion/demotion between adjacent tiers**, with the specific N and per-tier semantics deferred to hardware mapping. The research prototype starts at N=2 (effectively hot/cold from the M17 inversion); a production system would likely run at N=3 or N=4 matching physical memory hierarchies.

This page exists because the architectural commitment (N-tier with promotion ops) and the deferred specifics (what N is, what each tier means) have separate lifecycles — the commitment is settled, the specifics are open. Referenced by [caddy-architecture](./caddy-architecture.md) as the multi-tier generalisation of S1, K2, K5.

## Why generalise from two tiers

`[ASSERTED]` Modern LLM serving has a 3-4 tier physical memory hierarchy whether the caddy spec acknowledges it or not:

| Tier | Bandwidth | Latency | Capacity | Cost |
|---|---|---|---|---|
| GPU HBM | ~3 TB/s | ~ns | 80-192 GB | very expensive |
| System RAM | ~50 GB/s | ~100 ns | 256 GB - 2 TB | moderate |
| NVMe | ~7 GB/s | ~100 μs | 10s of TB | cheap |
| Network/blob | ~1 GB/s | ~10 ms | unbounded | cheapest |

The caddy *must* decide where each item lives at any given moment. Two-tier specs collapse the hardware's natural tiers, creating impedance mismatch at implementation time. Three- or four-tier specs that name silicon tiers directly over-commit before learning happens.

The right level: commit to the **capability** (multi-tier with promotion/demotion ops), defer the count and the per-tier semantics.

## Lifecycle tiers vs hardware tiers are orthogonal axes

`[ASSERTED]` A single item has both a *lifecycle state* (just-admitted / under-evaluation / consolidated) and a *hardware location* (HBM / RAM / NVMe). The mapping is not 1:1:

- A just-admitted item might be in HBM if currently being inferred over, or in RAM if admitted-but-quiet
- A consolidated item might be in HBM if hot in retrieval, or in NVMe if cold in retrieval

Whether the research prototype merges these axes into a single tier index or keeps them as separate orthogonal axes per item is itself a deferred design decision.

## A third orthogonal axis: storage format (2026-06-10)

`[ASSERTED]` Beyond *lifecycle state* and *hardware location*, an item also has a **storage format**: latent (a learned vector) vs verbatim (raw bytes with a vector only as retrieval key). This is a genuinely separate axis — a verbatim fact and a latent schema can share a hardware tier and a lifecycle state yet differ in format, and the format dictates the read mechanics (re-encode-on-read vs direct vector injection) and the learning channel (policy-trained vs gradient-trained). The full development — including the "key indexes, never reconstructs" principle and the LSM-compaction maintenance frame — is in [verbatim-vs-latent-tiers](./verbatim-vs-latent-tiers.md). The hardware/lifecycle commitments on this page are unchanged by it; format is simply the axis this page did not previously name.

## Why explicit tiers survive silicon scrutiny

Three reinforcements emerged from the 2026-05-17 silicon attack on the multi-tier commitment:

1. **Queue-bounded consolidation is a hard physical requirement, not an optimisation.** Under the M17 inversion, the hot store will exceed GPU HBM capacity. K2 evaluating the entire hot store means streaming items GPU↔CPU per pass — bandwidth-bound, CPU-bound, and fundamentally wrong for the most architecturally load-bearing component. A bounded inner tier that fits in GPU HBM lets K2 run on accelerated hardware.

2. **Bottom-up rescue maps to cache eviction.** Biology's shared-budget rescue mechanism (M15 STC) is structurally identical to LRU cache eviction competing for cache lines — one of the best-understood operations in systems engineering (CPUs, OS page caches, DB buffer pools, CDN edges). The biology validates the pattern; the engineering is already mature.

3. **Tier-promotion ops match hardware memory-movement primitives.** GPU↔RAM↔NVMe transfers are operations hardware vendors already optimise (NVLink, CXL, DirectStorage). Naming tier promotion in the caddy architecture aligns the abstractions with the silicon's primitives. Two-tier abstraction forces either "everything in HBM" (capacity-bound, impossible at scale) or ad-hoc paging (harder to optimise than tier-aware abstractions).

## What's committed

- **Discrete addressable units (S1)** span N tiers, N≥2
- **K2** generalises to "tier promotion (any tier → next-warmer)"; cold-promotion remains the load-bearing case
- **K5** generalises to "tier demotion (any tier → next-colder)"; rate = f(C)
- **Salience signal (C)** consumed by promotion and demotion ops uniformly across tiers
- **Capacity-bounded tiers** enforce shared-budget competition (M15 insight, hardware-natural)

## What's deferred

- **Specific N** — research prototype starts at N=2; a production system would likely run N=3 or N=4 matching hardware tiers
- **Whether lifecycle tiers and hardware tiers share an index** or stay as orthogonal axes
- **Per-tier capacity budgets** — set per hardware mapping
- **Promotion/demotion policy specifics** — LRU? salience-weighted? hybrid?
- **Which tier the bounded competition for promotion** (M15 PRP rescue analogue) lives in

## Doc-stage scope-impact assessment

Per [[feedback_mvp_doc_not_mvp]]: the multi-tier generalisation doesn't meaningfully change what we build. The research prototype can still be N=2 (effectively hot/cold). What changes is that the *architectural commitment* supports N≥2 without refactor, so scaling to match hardware tiers is configuration rather than redesign. Cheap to commit at doc stage; expensive to retrofit if we'd over-committed to N=2.

## When this gets revisited

The deferred specifics become load-bearing when:
- The prototype hits HBM capacity limits and needs explicit tier management to scale
- Deployment requires multi-node distributed caddy (introduces network-tier semantics)
- Multi-tenancy in lifecycle layer (currently B-section dropped) requires per-tenant tier budgeting

## Related

- [[verbatim-vs-latent-tiers]] — the third (format) axis: latent schemas vs verbatim-byte facts, with read-mechanics and the LSM-compaction frame
- [[caddy-architecture]] — the architecture this is a part of; references this page as deferred decision
- [[caddy]] — the architectural concept
- [[memory-caddy]] — the open question
- [[feedback_capabilities_not_policies]] — the discipline that justifies N-tier-as-capability over N-tier-as-count
- [[feedback_inspiration_not_blueprint]] — the discipline for borrowing biology's shared-budget pattern

## Source archive

- 2026-05-17 — promoted to its own page during caddy-architecture readability restructure; content originated in the M14-M17 reconciliation pass (extracted from caddy-architecture.md Tier semantics section to manage parent-doc length while preserving the multi-tier commitment + silicon attack reasoning)
