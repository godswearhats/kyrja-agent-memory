---
type: decision
name: Structured Filter First, Semantic Last
status: ACTIVE
last_ingested: 2026-06-30
sources: [../source/weller-2025-limit.md, ../experiment/2026-06-30-masq-retrieval-arms.md]
tags: [wedge, retrieval, anisotropy]
---

## Decision

Retrieval order for a coding agent's memory:

1. **File/entity overlap** (touched-file Z, called-function F) — sharpest categorical signal
2. **Task type** (T)
3. **Semantic similarity** (embedding cosine)
4. **Tool-call prefix** (e.g. "edited then ran tests")

Structured filters narrow the candidate set to ~50-200 items; semantic embeddings act as a **re-ranker** within that set, not as the primary index.

## Motivation

- **Sidesteps embedding-anisotropy / cone-collapse on homogeneous code.** All-Python or all-TypeScript codebases produce embeddings that collapse toward shared keywords. Two semantically distinct functions in the same idiomatic style produce near-identical embeddings. See [cascading-failures](../concept/cascading-failures.md) (embedding-crowding term, mode 2).
- **Categorical signals don't suffer dimensionality compression.** File-overlap is a binary check; task-type is a discrete category. Both are immune to the recall-ceiling proven in [Weller 2025 LIMIT](../source/weller-2025-limit.md).
- **Thread 5 empirical anchor:** at small scale, BM25 (48.3% hit rate), semantic (45.2%), and hybrid (52.4%) are roughly equivalent `[MEASURED]` ([Thread 5 retrieval comparison](../experiment/2026-04-17-thread5-retrieval-comparison/README.md)). Retrieval method barely matters when the structured filter dominates. Encoding quality is the binding constraint, not retrieval method. *Construct-validity:* small-scale archive experiment; "hit rate" is top-k retrieval accuracy against a held-out query set, which approximates but does not equal end-to-end retrieval utility for the wedge. Source archive: _archive/kyrja-shelved-2026-04-21/; experiment not yet promoted to wiki.
- **MASQ controlled anchor (construct-limited):** on a synthetic confusable-scope benchmark, a structured scope filter (`WHERE scope=target`) reached oracle decision accuracy (15/15) while every similarity-ranking arm floored at or below paste — vector 6/15, bm25 8/15, paste 9/15; scope-filter beats all three with zero paired losses (p≤0.03, n=15) `[MEASURED]` *(construct-validity-limited — scope caveat at bullet end)* ([MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md)). It **replicates** Thread 5's method-equivalence (bm25≈vector) and **extends** it: not only does method barely matter, all ranking loses to the filter, and the binding constraint is *exclusion of confusable siblings*, not recall (retrievers recall the target ~2.8/3 but cannot drop the siblings). *Construct-validity / scope:* MASQ **constructs** the confusability and uses an **oracle** scope tag; this is a clean demonstration of the failure mode this decision routes around, **not** independent validation of the production architecture, which still lacks real-corpus retrieval evidence. See [H45](../hypothesis/H45-exclusion-over-recall.md).

## Commitments

- Semantic embeddings exist in the retrieval pipeline but are explicitly **not** the primary index.
- Compound key index design (per [repo-bounded-scope](./repo-bounded-scope.md)) is load-bearing.
- The store architecture must support structured filtering as the first-class query primitive; vector search is auxiliary.
- Don't lead with a vector-DB-first architecture (e.g. Pinecone, Weaviate). Structured filter on Postgres + pgvector (or SQLite + sqlite-vec at MTP scale).

## Reversibility

**Moderate.** The order of operations could be reversed (semantic first, filter later) without rebuilding the store, but doing so re-exposes the system to embedding-anisotropy on homogeneous code corpora. Reversal would require demonstrating that anisotropy is solvable at our corpus scale before being responsible.

## Related

- [repo-bounded-scope](./repo-bounded-scope.md) — defines the primary scope key
- [precision-over-recall](./precision-over-recall.md) — the threshold the semantic re-ranker is tuned against
- [cascading-failures](../concept/cascading-failures.md) — the embedding-crowding term this decision mitigates
- [Weller 2025 LIMIT](../source/weller-2025-limit.md) — the recall-ceiling result this decision routes around
- [MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md) / [H45](../hypothesis/H45-exclusion-over-recall.md) — controlled, construct-limited demonstration of the filter-beats-ranking failure mode
