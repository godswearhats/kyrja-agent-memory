---
type: source
name: "Khandelwal et al. 2020 — Generalization through Memorization: Nearest Neighbor Language Models (kNN-LM)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, retrieval-augmentation, knn, p2]
---

## Citation

Khandelwal, U., Levy, O., Jurafsky, D., Zettlemoyer, L. & Lewis, M. (2020). *Generalization through Memorization: Nearest Neighbor Language Models.* ICLR 2020. arXiv:1911.00172. Stanford / Facebook AI Research.

## Location

- arXiv: https://arxiv.org/abs/1911.00172
- Rubric note: [substrate-survey/notes/khandelwal-2020-knnlm.md](../../../research/library/substrate-survey/notes/khandelwal-2020-knnlm.md)

## Key claims (with our restatements)

### Frozen-LM kNN interpolation

**Paper (§2):** Pretrained Transformer LM with frozen weights. Run one forward pass over the training corpus; for each token, store `(f(c_i), w_i)` where `f` is an intermediate layer activation (best: FFN input after layer norm, last layer; 1024-dim) and `w_i` is the target token. At inference, embed the test context with the same `f`, query the datastore via FAISS for `k=1024` nearest neighbours under squared L2, compute `p_kNN(y|x) ∝ Σ_N 1_{y=v_i} exp(−d(k_i, f(x)))`, then interpolate: `p(y|x) = λ·p_kNN(y|x) + (1−λ)·p_LM(y|x)`. No training.

**Our restatement:** `[ASSERTED]` — minimum viable [P2 substrate-as-module](../concept/substrate-paradigms.md). External memory, frozen LM, no training. Architecturally identical in shape to the agentic-memory products' approach but with a *learned* interpolation weight instead of prompt concatenation.

### Retrieval substitutes for training

**Paper (§4.2 / Table 3):** Model trained on Wiki-100M (100M tokens) with a Wiki-3B (3B-token) datastore reaches 13.73 test perplexity — better than the same architecture trained on all 3B tokens directly (15.17 ppl). Paper: *"Retrieving nearest neighbors from the corpus outperforms training on it ... rather than training language models on ever larger datasets, we can use smaller datasets to learn representations and augment them with kNN-LM over a large corpus."*

**Our restatement:** `[ASSERTED]` — structural claim that *representations* benefit from training while *memorization* is better handled by retrieval. The same conceptual move underlying agent memory: don't pour episodes into model weights; keep the LM lean and put episodes in retrievable form.

### λ scales with datastore size

**Paper (Figure 2b):** With a 100M datastore, optimal `λ ≈ 0.25`. With a 3B datastore, optimal `λ ≈ 0.55`.

**Our restatement:** `[ASSERTED]` — quantitative scaling: the model defers more to retrieval as the retrieval surface gets richer. For agent memory: a per-domain trust dial that should grow with the corpus.

### Free improvement at constant training data

**Paper (Table 1):** WikiText-103 base LM → kNN-LM with WikiText-103 as the datastore drops perplexity from 18.65 to 16.12 with zero new training data and zero new training. Paper: *"the prediction problem is more challenging than previously appreciated; learning similarity is easier than predicting the next word."*

**Our restatement:** `[ASSERTED]` — the model already *knows* useful things its softmax cannot express; kNN unlocks them. Implication for agents: retrieval over their own intermediate activations may unlock latent knowledge without any training.

## Important caveats

- **No write side.** Datastore is built once via a forward pass over training data. No online accumulation, no learned write decision.
- **No learned integration.** `λ` is a fixed scalar tuned on validation. No per-token or per-context adaptive weighting.
- **No structural retrieval.** Just nearest neighbours by L2 distance. No "find the memory adjacent to the one we just retrieved" capability ([NTM](./graves-2014-ntm.md) has this).
- **No simulation / forward modeling.**
- **No cog-sci grounding.** Paper cites no memory psychology; engineering-driven.
- **Cross-session continuity not addressed** `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the minimum viable P2 substrate-as-module — the 2020 baseline that current agentic-memory products are still operating at, often worse.
- Anchors the claim in [substrate-as-memory](../concept/substrate-as-memory.md) that the agentic-memory field is operating at kNN-LM-2020 level while LM research moved to RETRO-2022 and Titans-2024.
- Reusable for Kyrja: pretrained-LM embeddings as a free retrieval surface (the LM's own intermediate FFN-input activations); token-level memory primitive (finer-grained than chunk-level); `λ`-interpolation as a learned trust dial; datastore-size scaling pushes against active-forgetting design.
- Direct architectural anchor for [Mem0](../incumbent/mem0.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Cognee](../incumbent/cognee.md), [LightMem](../incumbent/lightmem.md) — they implement kNN-LM-shaped retrieval but with prompt-concat replacing `λ`-interpolation.

## Audit history

- 2026-05-13 — verbatim read, pp.1-6 (core sections §1-§4), rubric note written.

## Archive location

arXiv:1911.00172. Not in `library/papers/`. Fetch from arXiv for re-verification.
