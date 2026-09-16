---
type: concept
name: Cascading-Failures Product
status: timeless
last_ingested: 2026-05-13
sources: [../source/weller-2025-limit.md, ../source/hnsw-real-time-updates-2407.md, ../source/semantic-collapse-2025.md]
epistemic_tags: [speculated, measured]
tags: [scale-thesis, retrieval, recall-cascade]
---

## Definition

The **cascading-failures product** describes how four independent recall-degradation modes compound to produce ~30-50% effective recall at billion scale for a single-vector dense memory system over homogeneous code corpora.

The four modes:

1. **HNSW recall degradation at scale** — `[SPECULATED]` (specific magnitude). The *existence* of degradation is well-documented in [HNSW real-time-updates paper](../source/hnsw-real-time-updates-2407.md) and vendor benchmarks (see [HNSW scale limits](./hnsw-scale-limits.md)); the *composite ~85% at 10M → lower at scale* figure is a Kyrja synthesis of cross-vendor data and is uncalibrated for our target corpus.
2. **Embedding crowding in homogeneous code** — `[SPECULATED]` (specific magnitude). The mechanism is sourced from [Weller 2025 LIMIT](../source/weller-2025-limit.md) (architectural ceiling) and [Denham 2025](../source/semantic-collapse-2025.md) (formalization). The *~60-70% effective recall on homogeneous code* figure is a Kyrja composite estimate, not measured on production agentic-memory code corpora. See [embedding collapse](./embedding-collapse.md) for the three lenses.
3. **Hub distortion** — queries pulled toward heavily-connected nodes in the HNSW graph, away from true nearest neighbors. See [HNSW scale limits — hubness](./hnsw-scale-limits.md#recall-degradation). Documented in HNSW literature; magnitude not quantified for our corpus.
4. **Unreachable points from constant updates** — `[MEASURED]` 3-4% lost after ~200 update cycles ([MN-RU paper](../source/hnsw-real-time-updates-2407.md); construct-validity note: figures from controlled benchmark configurations, not production agentic-memory workloads). See [HNSW scale limits — update degradation](./hnsw-scale-limits.md#update-degradation).

## The product (deep-dive §6.5)

```
Degraded HNSW recall at scale (85% → ?)
  × Embedding crowding in homogeneous code (~60-70% effective recall)
    × Hub distortion pulling queries to wrong neighbors
      × Unreachable points from constant updates (3-4% lost)
        = Effective recall: potentially 30-50% at billion scale
```

## Role in Kyrja thesis

This product is **the load-bearing claim of the recall leg** of our scale thesis. If true, agentic memory systems built on single-vector dense retrieval over homogeneous code corpora at billion scale degrade into a failure mode where the agent re-solves solved problems, contradicts prior decisions, and generates duplicates (because dedup search also has degraded recall) — a degenerative spiral.

## Epistemic status of the product itself

`[SPECULATED]` whether the four modes **compound multiplicatively or overlap.** Each individual mode is sourced from literature; the *product* is our synthesis. The highest-priority empirical gap in the current thesis is calibrating multiplicativity vs overlap: the observed 49% recall figure on LongMemEval (Mem0 independent re-run) may already be the floor set by the worst single mode, not the product of all four.

See [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md).

## Why this matters for the wedge

The wedge product's [precision over recall](../decision/precision-over-recall.md) decision is partially a response to this concept: rather than fight the recall ceiling, design the read path so that returning nothing is preferable to returning a low-confidence wrong memory. This avoids the dedup-recall spiral by ensuring write-side dedup doesn't depend on perfect recall either. Coupled with [structured-filter-first](../decision/structured-filter-first.md), the wedge sidesteps the embedding-crowding term (mode 2) entirely on the read path.

## Falsifiability

The cascading-failures thesis is falsified by any of:

1. **A single escape path achieves >90% recall on third-party-replicated agentic-memory benchmarks at billion scale on homogeneous (e.g. all-Java, all-TypeScript) corpora.** This would show the failure modes do *not* compound — the worst single mode is escapable in isolation, contradicting the multiplicative framing. *Status:* not yet observed; no benchmark probes 1B-scale homogeneous code. See [billion-scale-benchmark-gap](../open-question/billion-scale-benchmark-gap.md).
2. **Independent benchmark replications converge on incumbent scores >85%** as evaluation methodology stabilises. Would suggest current 49-65% scores are methodology artefacts, not architectural floor. *Status:* not yet observed; the [benchmark-replication-gap](./benchmark-replication-gap.md) is currently widening across vendors, not narrowing.
3. **An incumbent ships the integrated [seven-layer stack](./seven-layer-stack.md)** before Kyrja or any new entrant can. Would close the integration gap and preempt the moat. *Status:* not yet observed; the per-layer rollup shows no integrator with more than ~2.5 of 7 layers.

These criteria are pre-registered (recorded 2026-04-30, re-anchored from the prior single-wall framing). Two further pre-registered falsifiability tests exist on the volume leg specifically — see [scale-crossings](./scale-crossings.md) and [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md).

## Related

- [HNSW scale limits](./hnsw-scale-limits.md) — modes 1, 3, 4 of the cascade as a single page.
- [Embedding collapse](./embedding-collapse.md) — mode 2 with the three formal lenses; supersedes the prior pending `embedding-anisotropy` and `limit-bound` references.
- [Seven-layer stack](./seven-layer-stack.md) — the architecture that, if integrated, addresses each layer of the cascade.
- [Benchmark replication gap](./benchmark-replication-gap.md) — the today-anchor evidence; small-scale 49-65% projects downward on the cascade hypothesis.
- [Cost leg — affordable substrate](./cost-leg-affordable-substrate.md) — what cascading-failures is *not*: the recall thesis is orthogonal to storage cost.

## Source archive

Concept synthesized from deep-dive §6.5 (agentic-memory-scaling-deep-dive.md, lines 522-554).
