---
type: open-question
name: Right balance between vector, graph, and structured (SQL) storage
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [storage, architecture, hot-store]
---

## The question

**What's the right balance between vector, graph, and structured (SQL) storage for agent memory?**

Google's "no vectors, just text" approach (Always-On Memory agent) works at small scale and ditches vector databases entirely. Does that hold at 10M+ memories? What if the LLM itself is a better "index" than any vector search for causally-structured data — i.e. just let the LLM read summaries and decide what to load? Conversely, [Zep](../incumbent/zep.md) leans heavily on graph; [Mem0](../incumbent/mem0.md) on vector; the current Kyrja wedge architecture uses structured-filter-first with vector as re-rank — three different bets, no consensus.

## Why it matters

- **Architecture decision the wedge already made.** [structured-filter-first](../decision/structured-filter-first.md) commits to SQL-as-primary, vector-as-re-rank. This open question keeps the alternatives visible — the decision is reversible.
- **The seven-layer stack** ([seven-layer-stack](../concept/seven-layer-stack.md)) folds graph, vector, and tiered into separate layers. The *balance* between them at the hot-store level is unresolved across the field.
- **LLM-as-index is genuinely new.** The Google Always-On Memory approach treats the LLM's in-context reasoning as the retrieval layer. If that scales, the entire vector-DB industry is partly obsoleted; if it doesn't, the LLM-as-index claim is a small-scale artifact.

## What evidence would resolve it

- **Workload-conditional benchmarks** — separate (a) NL Q&A workloads, (b) compositional/code workloads, (c) causally-structured reasoning traces. Likely none of the three storage types dominates across all three workload classes. Pairs with [query-type-axis](./query-type-axis.md).
- **LLM-as-index scaling curve.** Google's approach at 10M memories: does it hold? If summaries themselves are the index, what's the summary-to-memory ratio at scale?
- **Three-way head-to-head on a homogeneous-code MTP** corpus. Reuse [MTP](../decision/tool-chain-wedge-as-adoption-path.md) data when available; cross-evaluate against vector-only and graph-only baselines.

## Related

- [structured-filter-first](../decision/structured-filter-first.md) — the wedge's current bet
- [seven-layer-stack](../concept/seven-layer-stack.md) — how vector/graph/SQL appear as separate layers
- [graph-memory-approaches](../concept/graph-memory-approaches.md) — the graph alternative
- [multi-vector-retrieval](../concept/multi-vector-retrieval.md) — vector-side escape from the single-vector ceiling
- [query-type-axis](./query-type-axis.md) — the workload conditioning that likely shapes the answer
- Deep-dive §11 Q3 origin: agentic-memory-scaling-deep-dive.md
