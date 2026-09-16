---
type: source
name: "SPLADE (sparse-dense retrieval) and the open question for code memory"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [sparse-retrieval, splade, embedding-layer, code-memory, pending-verbatim-read]
---

## Citation

- *SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking.* Formal et al., SIGIR 2021. arXiv:2107.05720.
- *SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval.* Formal et al., 2021. arXiv:2109.10086.
- Follow-up: *SPLADEv3* and SPLADE variants (industrial deployment generation).

## Location

- SPLADE arXiv: https://arxiv.org/abs/2107.05720
- SPLADE v2 arXiv: https://arxiv.org/abs/2109.10086
- Pinecone analysis: https://www.pinecone.io/learn/splade/

## Key claims (with our restatements)

### What SPLADE is

**Paper:** SPLADE is a *learned* sparse retrieval model. It produces high-dimensional sparse vectors (one weight per BERT vocabulary token) that operate in the same algebra as BM25 but learned end-to-end. Combines lexical-style sparsity with neural query/document expansion.

**Our restatement:** SPLADE is the sparse-side complement to dense embeddings. It sidesteps the dense-embedding *distance-compression* mode of [embedding collapse](../concept/embedding-collapse.md) because sparse spaces are effectively unbounded-dimensional and don't collapse the same way. The [vector-stability paper](./vector-stability-2512.md) extends stability theory to sparse retrieval specifically.

### Hybrid retrieval and the stability lens

**Paper:** SPLADE benchmarks competitively with dense retrievers on MS-MARCO and BEIR, and the *combination* (dense + SPLADE-sparse, often called hybrid retrieval) routinely beats either alone.

**Our restatement:** Sparse-dense hybrid is one of the Weller-LIMIT-recommended escape paths from the [single-vector representability ceiling](./weller-2025-limit.md). For Kyrja, SPLADE is the candidate sparse-side of the [seven-layer-stack embedding layer](../concept/seven-layer-stack.md) (alongside dense + multi-vector ColBERT/MUVERA-class).

### The code-specific open question (load-bearing)

The deep-dive raised a specific open question (§11 Q9, paraphrased; not externally cited): **is SPLADE underexplored for code memory specifically?** Code corpora are homogeneous, keyword-dense, and pattern-rich — superficially the kind of regime where learned-sparse should excel. But:

- SPLADE's training data is general-domain text (MS-MARCO, Wikipedia, news), not code.
- Code-specific sparse retrieval has been explored mainly via BM25 + AST-features, not via learned sparse models.
- No published benchmark cleanly compares SPLADE-trained-on-code against dense + multi-vector on agentic-memory recall.

**Our restatement:** `[SPECULATED]` — the hypothesis that SPLADE-trained-on-code beats dense-trained-on-code on homogeneous code corpora is a Kyrja-internal extrapolation from general-domain SPLADE results and the embedding-collapse framing. No external empirical study addresses this directly. Promotion to a hypothesis or experiment is on the [F-deep-4 open-question shortlist](../archive/BIG-PICTURE-2026-05-14.md) (archived 2026-05-14).

## Construct-validity caveats

- **Not read verbatim.** Per [feedback_load_bearing_sources], this stub is paraphrased from general SPLADE literature and the deep-dive's framing, not from a verbatim read of the SPLADE papers. Numbers (e.g. specific MS-MARCO/BEIR scores) are intentionally omitted until that read happens.
- **No code-domain empirical data.** Every claim about SPLADE-for-code in this page is extrapolation, not measurement.

## Relevance to Kyrja

- Sources the SPLADE term in [multi-vector retrieval](../concept/multi-vector-retrieval.md).
- Anchors the sparse-side of the [seven-layer stack](../concept/seven-layer-stack.md) embedding layer.
- Open question: code-specific SPLADE — on the [F-deep-4 shortlist](../archive/BIG-PICTURE-2026-05-14.md) (archived 2026-05-14).

## Archive location

Not in `library/papers/`. Fetch from arXiv (papers above) for verbatim reading before any claim on this page is upgraded from *SPECULATED* to *ASSERTED* or *MEASURED*.
