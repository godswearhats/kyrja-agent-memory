---
type: source
name: "Stability of Modern Vector Retrieval / Breaking the Curse of Dimensionality (arxiv 2512.12458)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [curse-of-dimensionality, embedding-collapse, stability]
---

## Citation

*Breaking the Curse of Dimensionality: A Stability-Theoretic Analysis of Modern Vector Retrieval.* arXiv:2512.12458, December 2025.

## Location

- arXiv: https://arxiv.org/abs/2512.12458

## Key claims (with our restatements)

### Reframing curse-of-dimensionality through stability

**Paper:** Classical theory predicts retrieval should suffer from the curse of dimensionality (distances compress, NN search becomes meaningless). This paper examines retrieval through the lens of **stability**: whether small query perturbations radically alter the nearest-neighbor result. Extends stability theory to multi-vector search, filtered vector search, and sparse vector search.

**Our restatement:** This is the **theoretical counter-anchor** to the simple "curse of dimensionality kills high-d retrieval" framing. Retrieval can be high-d and *stable* (works reliably for queries near indexed points) without being able to handle adversarial or out-of-distribution queries. Sharpens what failure modes are actually expected at scale.

### Multi-vector and sparse-vector stability

The paper's extension to multi-vector (ColBERT/MUVERA-class) and sparse-vector (SPLADE-class) retrieval is the formal underpinning for why these architectures are recommended escapes from the single-vector ceiling.

**Our restatement:** Strengthens the case for the [seven-layer stack](../concept/seven-layer-stack.md)'s embedding layer including multi-vector and sparse vectors in parallel.

## Relevance to Kyrja

- Sources [embedding collapse](../concept/embedding-collapse.md) concept page's "curse of dimensionality" section.
- Provides theoretical justification for the multi-vector / sparse-vector recommendations across the wedge stack.
- Complementary to [Weller 2025 LIMIT](./weller-2025-limit.md) (representability bound) and [semantic-collapse](./semantic-collapse-2025.md) (entropy-based collapse): three different formal lenses on "high-dimensional embedding retrieval has structural limits."

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify specific claims.
