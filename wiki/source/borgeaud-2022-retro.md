---
type: source
name: "Borgeaud et al. 2022 — RETRO: Improving language models by retrieving from trillions of tokens"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, retrieval-augmentation, cross-attention, p2]
---

## Citation

Borgeaud, S., Mensch, A., Hoffmann, J. et al. (2022). *Improving language models by retrieving from trillions of tokens.* arXiv:2112.04426. DeepMind.

## Location

- arXiv: https://arxiv.org/abs/2112.04426
- Rubric note: [substrate-survey/notes/borgeaud-2022-retro.md](../../../research/library/substrate-survey/notes/borgeaud-2022-retro.md)

## Key claims (with our restatements)

### Chunked cross-attention to trillion-token store

**Paper (§2-§3):** Split input into chunks of 64 tokens. For each chunk, retrieve `k` nearest neighbours from a 2T-token key-value database via cosine distance on frozen BERT embeddings. Each retrieved neighbour contains the matching chunk plus its continuation in the original document. Encode neighbours via a bidirectional Transformer (the retrieval encoder). Interleave RETRO blocks (which include chunked cross-attention to encoded neighbours) with standard Transformer blocks. Cross-attention attends from chunk `u`'s last token onwards to neighbours of the *previous* chunk `u-1` (preserves autoregressivity). Database is constructed once, frozen, queried at `O(log T)` via SCaNN.

**Our restatement:** `[ASSERTED]` — RETRO is the P2-substrate-as-module frontier. Differentiable cross-attention is the load-bearing piece — the model *learns* when to attend to retrieved content vs its own parametric knowledge.

### 25× parameter savings via retrieval

**Paper (§4):** 7.5B-parameter RETRO matches GPT-3 (175B) and Jurassic-1 (178B) on Pile while using ~25× fewer parameters.

**Our restatement:** `[ASSERTED]` — paper-reported magnitudes. External memory can substitute for parameters as a scaling path. For agent memory: agents accumulate interactions over months/years; you cannot keep adding parameters but you can keep adding retrievable data.

### Retrofit-able into existing models

**Paper (§4.2):** RETRO can be retrofitted onto any pretrained Transformer by training only cross-attention and retrieval-encoder weights — ~10% of parameters on ~3% of pretraining data.

**Our restatement:** `[ASSERTED]` — closest existing pattern to "add learned memory to an existing LLM" without full fine-tuning. Reusable engineering primitive for Kyrja.

### Copy-vs-generalize observability

**Paper (§4.4):** Model behaviour around retrieved content is inspectable — can determine whether a generated token is a copy of retrieved content or a generalization.

**Our restatement:** `[ASSERTED]` — paper-supported. Useful for memory-quality audits in agent contexts: when did the agent recall verbatim vs generalize from memory.

## Important caveats

- **Database is static.** No online accumulation or pruning; database grows monotonically `[ASSERTED]`.
- **Retriever is frozen.** BERT-kNN is not learned end-to-end with the main model.
- **No constructive reconstruction.** Memory is verbatim text chunks; the model attends to them but does not recombine fragments into novel outputs.
- **No surprise-driven encoding.** All training data indexed; nothing preferentially weighted.
- **No simulation primitive.** Predicts next token from past context + retrieved chunks.
- **Sequence-scoped.** No cross-session persistence story `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P2-substrate-as-module frontier — "philosophy-2 done well" with differentiable integration.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md): agentic-memory products inherit the static-store half of RETRO but drop the learned cross-attention half (the part that does the work).
- Reusable for Kyrja: chunked cross-attention to retrieved content as a learned memory-use mechanism; frozen-retriever-plus-learned-encoder split as a clean architectural seam; retrofit pattern for adding learned memory to a frozen LLM.
- Direct comparison anchor for [Mem0](../incumbent/mem0.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Cognee](../incumbent/cognee.md), [LightMem](../incumbent/lightmem.md) — they implement degenerate-P2 with prompt-concat replacing cross-attention.
- **Architectural ancestor: [MERLIN (Wayne et al. 2018)](./wayne-2018-merlin.md)**. RETRO's chunked cross-attention to encoded neighbours is structurally the LLM-era port of MERLIN's content-addressed read head with learned keys. The distinctive piece RETRO did **not** inherit is MERLIN's **MBP** — the auxiliary world-model loss that shaped memory representations independently of the LM's own loss. This dropped element is the core of the [MBP-was-dropped hypothesis](../open-question/memory-caddy.md) surfaced 2026-05-15: whether adding back an MBP-style auxiliary objective on the memory module improves over the existing co-trained-memory baseline is, as far as we have surveyed, an unmeasured ablation.

## Audit history

- 2026-05-13 — verbatim read, pp.1-15 (core sections §1-§4), rubric note written.

## Archive location

arXiv:2112.04426. Not in `library/papers/`. Fetch from arXiv for re-verification.
