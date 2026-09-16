---
type: open-question
name: Z-curve as algebraic alternative to graph traversal for multi-dim retrieval
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [retrieval, multi-dimensional, architecture, post-wedge]
---

## The question

The z-order curve (a space-filling curve via bit interleaving) provides multi-dimensional compound range queries that are architecturally equivalent to weighted graph traversal for queries of the shape "find memories simultaneously X along dimension A, Y along dimension B, Z along dimension C."

**Is this a core architectural advantage to build toward, or a deferred optimization?**

The 2026-04-20 reframing of shelved H12 distinguished these. The original framing was "z-curve correctly deferred for MVP." The reframing — driven by Zep competitive analysis — was that z-curve is a *structural differentiator* that gives Kyrja graph-like multi-dimensional retrieval without graph-extraction cost.

## Why it matters

- **Competitive positioning vs Zep.** [Zep](../incumbent/zep.md) uses graph traversal for multi-dimensional proximity (recent + relevant + connected). Graph traversal requires expensive LLM-driven entity extraction at ingest and bounded-depth traversal at query. Z-curve achieves the same compound-range-query class algebraically on continuous dimensions.
- **Predictable latency.** Z-curve range scans on B-tree indexes have standard-database latency guarantees. Graph traversal is bounded by depth limits to meet latency targets.
- **Cost asymmetry.** Z-curve indexing is compute-cheap (bit interleaving). Graph extraction requires LLM calls per episode.
- **Dependency chain.** If [rl-encoding-upgrade](./rl-encoding-upgrade.md) produces a continuous utility dimension, the natural retrieval-side expression of that learning loop is z-curve indexing of (time, forgetting score, utility). The two questions interlock.

## Candidate continuous dimensions

1. **Time** (already present)
2. **Forgetting score** ([H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md))
3. **Access recency/frequency** — usage-weighted importance
4. **Confidence score** — extraction certainty
5. **RL-derived utility score** ([rl-encoding-upgrade](./rl-encoding-upgrade.md))

With three or more continuous dimensions, z-curve compound range queries become measurably more efficient than independent WHERE clauses, and reproduce graph-style "multi-dimensional proximity."

## What evidence would resolve it

- **Benchmark comparison.** Same query set against (a) independent WHERE clauses, (b) z-curve range scan, (c) lightweight graph traversal. Measure precision, recall, latency at multiple corpus sizes.
- **Query-pattern logs from a real codebase MTP** ([tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md)) — which queries actually need multi-dimensional continuous range filtering? If the distribution is dominated by 1- or 2-dimension queries, z-curve is over-engineering.
- **Postgres support gap.** Postgres has no native z-curve indexing; PostGIS space-filling curves are the nearest. Whether a custom index is justified depends on the benchmark above.

## What would close this

Promotion to a hypothesis with falsifiable form, conditional on either MTP query-pattern evidence or a benchmark result. Likely shape:

> *Z-curve range queries beat independent-WHERE-clause filtering on (precision, recall, latency) jointly when the query mixes ≥3 continuous dimensions, at corpus sizes above N memories.*

## Evidence against z-curve as differentiator

- Z-curve only handles continuous / ordinal dimensions. Categorical relationships (entity A is-related-to entity B) still need explicit modelling.
- True multi-hop reasoning ("friend of a friend") isn't reducible to range queries — graph traversal genuinely wins for that class.
- No production memory system uses z-curve indexing today; the absence may itself be evidence (or just unfamiliarity).

## Related

- [structured-filter-first](../decision/structured-filter-first.md) — the static-priority predecessor; z-curve is the continuous-dim extension
- [rl-encoding-upgrade](./rl-encoding-upgrade.md) — dependency: RL utility score is one of the candidate continuous dimensions
- [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) — another candidate continuous dimension
- [Zep incumbent](../incumbent/zep.md) — the graph-traversal competitor whose architecture this question contrasts with
- Shelved predecessor: H12 in _archive
