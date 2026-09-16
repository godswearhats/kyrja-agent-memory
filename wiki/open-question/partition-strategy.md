---
type: open-question
name: Right partition strategy for agent memory
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [storage, partitioning, multi-agent]
---

## The question

**What's the right partition strategy for agent memory at scale?** Per-service? Per-team? Per-language? Per-repo? Per-agent-session? Per-customer-org?

The choice of partition key determines whether filtered search is fast or catastrophically slow. Different incumbents have made different bets implicitly; no formal analysis of partition choice across realistic enterprise workloads exists.

## Why it matters

- **Determines structured-filter performance.** [structured-filter-first](../decision/structured-filter-first.md) commits to filter-then-vector retrieval. The partition key is the *most selective* filter; if it doesn't align with the query distribution, the post-filter candidate set is too large and the wedge advantage shrinks.
- **The wedge already picks `(org_id, repo_id)`.** [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) commits to a two-level partition: org-wide storage with repo-scoped queries. This question keeps the alternatives visible — the partition could go finer (per-agent, per-language) or coarser (org-only).
- **Pinecone Filtered Search (ICML 2025)** demonstrates that naive metadata filtering on poorly-chosen partition keys breaks vector-DB query plans at scale. Whether the wedge's `(org_id, repo_id)` choice avoids that pathology is unverified.

## What evidence would resolve it

- **Empirical query-mix data** from a real deployment, broken out by candidate partition key. Which key has the highest selectivity-to-cost ratio?
- **Crossover analysis.** At what corpus size does a finer partition (per-language under per-repo) start paying off vs the simpler two-level wedge?
- **Pathological-case analysis.** Pinecone Filtered Search shows that *some* partition+filter combinations are catastrophic. Is `(org_id, repo_id)` in the safe regime? Verifying this is a small experiment that should land before the MTP scales.

## Related

- [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) — the wedge's current partition choice
- [structured-filter-first](../decision/structured-filter-first.md) — what depends on a good partition
- [H30-scaling-crossover-point](../hypothesis/H30-scaling-crossover-point.md) — scaling behavior of the structured-filter approach; partition strategy is one variable
- Deep-dive §11 Q14 origin: agentic-memory-scaling-deep-dive.md
