---
type: source
name: "Pinecone filtered vector search (ICML 2025) + the Reddit metadata-filter bottleneck"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [filtered-search, metadata-filter, pinecone, structured-retrieval, pending-verbatim-read]
---

## Citations

1. Pinecone, ICML 2025: paper on filtered vector search with immutable vector slabs stored as LSM-tree segments on object storage. Specific title and arXiv ID to be confirmed on verbatim read.
2. Reddit engineering blog (2024-2025): vector + metadata-filter scaling experience at ~340M vectors.

## Location

- Pinecone research page: https://www.pinecone.io/learn/
- ICML 2025 proceedings: https://icml.cc/Conferences/2025
- Reddit engineering blog: https://www.redditinc.com/blog (specific post to be located on verbatim read)

## Key claims (with our restatements)

### Pinecone ICML 2025: filtered vector recall

**Paper:** Immutable vector slabs organized as LSM-tree segments on object storage; integrated/in-algorithm filtering rather than pre- or post-filter. Reports **mean recall@10 of 0.989 across all selectivity ranges** on YFCC100M.

**Our restatement:** `[ASSERTED]` (vendor-published; not yet read verbatim per [feedback_load_bearing_sources]). The headline is **invariance to selectivity** — most filtering implementations degrade sharply at extreme selectivity (very high or very low), and Pinecone is claiming an architecture where that degradation is bounded. Direct evidence that the integrated-filtering pattern works at production scale for at least one well-studied benchmark.

**Construct-validity:**
- **YFCC100M is image+metadata**, not agentic-memory code. Generalization to code-corpus filtering is plausible but not measured.
- **Vendor-published**, not third-party-replicated.
- **Selectivity-range claim** is more important than the 0.989 headline — the variance across selectivity, not the mean, is what matters for production agentic memory.

### Reddit: metadata-filter as bottleneck

**Engineering report:** at ~340M vectors, metadata filtering was the **primary latency bottleneck**, with P99 latency jumping 10× when queries crossed between the vector graph and a separate relational metadata store.

**Our restatement:** `[ASSERTED]` (vendor-reported anecdote). Direct evidence that **the filter layer, not the vector layer, is where production agentic memory breaks** at hundred-million scale on heterogeneous workloads. Reinforces the [structured filter-first decision](../decision/structured-filter-first.md) — filter before similarity rather than after.

## Construct-validity caveats

- **Not read verbatim.** Paper title, exact arXiv ID, and Reddit blog URL all need verification.
- **Headline-only numbers.** Recall@10=0.989 is the mean; the variance across selectivity ranges is the load-bearing detail and is not yet recorded here.
- **Selectivity-range edge cases unverified.** Pinecone's invariance claim is what makes the architecture interesting; until edge cases (selectivity ≈ 0.001 and selectivity ≈ 0.999) are verified, treat the headline as directional.

## Relevance to Kyrja

- Sources [beyond-HNSW filtered vector search](../concept/beyond-hnsw-approaches.md) section.
- Supports [structured filter-first decision](../decision/structured-filter-first.md) — direct evidence that filter-layer engineering matters at scale.
- Adjacent to [federation-access-patterns](../concept/federation-access-patterns.md) — identity-aware filtering at query time is the same architectural primitive applied to multi-tenant memory.

## Archive location

Not in `library/papers/`. ICML 2025 paper to be fetched from arxiv on verbatim read. Reddit blog URL to be located.
