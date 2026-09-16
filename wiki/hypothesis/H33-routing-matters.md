---
type: hypothesis
name: H-ROUTING-MATTERS — query-intent routing beats any single retrieval method
status: PROPOSED
last_ingested: 2026-06-30
sources: [../source/magma-paper-2601.md]
epistemic_tags: [asserted]
tags: [retrieval, routing, v2]
---

## Claim

Classifying query intent (temporal, causal, entity-based, factual) and routing to the appropriate retrieval strategy produces larger downstream-quality gains than improving any single retrieval method. The routing policy is worth more than any index it routes to.

## What would falsify it

- Enterprise queries cluster into 1-2 intent types (e.g. nearly all "what happened with X?"), making routing unnecessary.
- Heuristic routing (pattern matching) achieves ≥90% of trained routing performance, making the trained-router investment marginal.
- The retrieval-method-doesn't-matter-much finding from Thread 5 (BM25 ≈ semantic ≈ hybrid) extends to routing — if all methods produce similar results, routing between them doesn't help.

## Evidence for

- **MAGMA paper** (arxiv 2601.03236, see [MAGMA source](../source/magma-paper-2601.md)) — ablation showed removing the adaptive routing policy dropped LOCOMO performance from 0.700 to 0.637, a larger drop than removing any single graph type. `[ASSERTED]` from paper.
- **Intuitive argument.** "What happened last Tuesday?" wants temporal filtering. "Why did we choose Postgres?" wants causal graph traversal. "Tell me about the auth service" wants entity search. One retrieval method can't serve all of these well.

## Evidence against

- MAGMA's result is on LOCOMO (single-agent, short-term, chatbot-style). Enterprise query intent distributions may be different.
- Thread 5 (from tool-chain-wedge-goals-2026-05-11.md) found retrieval-method differences within 1.5% on tool-call-chain memories. If that finding generalizes, the routing margin shrinks.
- The current wedge uses [structured-filter-first](../decision/structured-filter-first.md) static priority (file/entity > task type > semantic), not learned routing. The wedge gets value from the priority order even without intent classification.
- **MASQ replicates the method-equivalence that powers falsifier #3** `[MEASURED]` (construct-validity / scope at bullet end): bm25 ≈ vector (8 vs 6 of 15, CIs overlap) on the confusable-scope task ([MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md)). If the ranking methods a router would choose between are themselves equivalent, routing *between them* is low-leverage; the leverage was filter-vs-rank (structured exclusion), which is a priority-order/index choice, not an intent-routing choice. *Construct-validity / scope:* synthetic, confusable-by-construction; CI-overlap equivalence at n=15; bounds what this says about natural enterprise query mixes.

## Open sub-questions

- What's the enterprise query intent distribution on a real codebase? Currently unknown.
- Is heuristic routing on file/entity/task-type cues enough, or does the gain require learned intent classification?
- Where does routing pay off — at MTP scale, mid-product, or only past the [scaling-crossover](./H30-scaling-crossover-point.md)?

## Related

- [structured-filter-first](../decision/structured-filter-first.md) — the static-priority predecessor the learned-routing version would upgrade
- [H30-scaling-crossover-point](./H30-scaling-crossover-point.md) — adjacent scale-conditional retrieval hypothesis
- Shelved predecessor: H18 in _archive
