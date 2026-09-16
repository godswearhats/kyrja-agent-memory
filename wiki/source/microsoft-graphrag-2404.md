---
type: source
name: "Microsoft GraphRAG (arxiv 2404.16130) and Leiden-community summarization"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [graph-memory, graphrag, leiden-community, hierarchical-summarization, pending-verbatim-read]
---

## Citation

*From Local to Global: A Graph RAG Approach to Query-Focused Summarization.* Edge et al., Microsoft Research. arXiv:2404.16130, April 2024.

## Location

- arXiv: https://arxiv.org/abs/2404.16130
- Microsoft Research blog: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
- Reference implementation: https://github.com/microsoft/graphrag

## Key claims (with our restatements)

### The GraphRAG pipeline

**Paper:** Three stages:
1. **Entity-relationship extraction** from source documents via LLM.
2. **Leiden community detection** over the resulting entity graph — clusters entities into hierarchical communities.
3. **Hierarchical summarization** — generates summaries at multiple community levels; queries hit summaries at the level matching scope.

**Our restatement:** The pipeline operationalizes a specific bet: that structured-entity context + community hierarchy outperforms flat retrieval on narrative-scoped questions. The Leiden-community-summarization pattern is what [Cognee](../incumbent/cognee.md) partially imitates.

### Headline empirical claim

**Paper:** On annual-report analysis benchmarks, knowledge-graph augmentation moved "correct" answers from ~50% to ~80%; on certain question types precision reached ~99%.

**Our restatement:** `[ASSERTED]` (vendor-published numbers; not yet read verbatim per [feedback_load_bearing_sources]). Construct-validity caveats:
- **Annual-report analysis ≠ agentic-memory recall on code.** The benchmark is narrative document Q&A; agentic memory at billion scale on homogeneous code corpora is a different regime.
- **The 50→80% delta is *suggestive* but not directly applicable** to the [cascading-failures product](../concept/cascading-failures.md) prediction. The pipeline addresses a different failure mode (semantic-flat retrieval) than the four modes in the cascade.
- **Microsoft is the vendor.** Independent third-party replication on the GraphRAG benchmark suite would close [benchmark-replication-gap](../concept/benchmark-replication-gap.md)-style concerns.

### Relationship to multi-graph memory

**Our restatement:** GraphRAG is a **single-graph** system (entities + relationships, community-clustered). It is not the four-graph structure on the [seven-layer stack](../concept/seven-layer-stack.md), but it is the most concrete production-scale demonstration that graph-augmented retrieval beats flat retrieval on at least one well-defined benchmark family.

## Construct-validity caveats

- **Not read verbatim.** This stub paraphrases the paper from its abstract, the Microsoft blog post, and the deep-dive's framing. Numbers are not verified to-the-decimal.
- **Benchmark scope.** Annual-report analysis is the headline; broader applicability to code/agentic workloads is an open question.

## Relevance to Kyrja

- Sources the GraphRAG citation in [graph-memory-approaches](../concept/graph-memory-approaches.md).
- Anchors the Leiden-community-summarization pattern referenced for [Cognee](../incumbent/cognee.md).
- Counter-anchor to the "context windows will solve it" objection: structured graph retrieval beat flat retrieval on a documented benchmark.

## Archive location

Not in `library/papers/`. Fetch from arXiv before any claim on this page is upgraded from `[ASSERTED]` paraphrase to `[ASSERTED]` verbatim with construct-validity hardened.
