---
type: source
name: "Wu, Rabe, Hutchins & Szegedy 2022 — Memorizing Transformers (ICLR 2022)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [memorizing-transformer, knn-attention, external-memory, caddy-architectural-template, iclr-2022, google-research, mbp-was-dropped]
---

## Citation

Wu, Y., Rabe, M. N., Hutchins, D., & Szegedy, C. (2022). *Memorizing Transformers.* Published as a conference paper at ICLR 2022. arXiv:2203.08913.

Affiliations: Google Research (`{yuhuai,mrabe,delesley,szegedy}@google.com`).

## Location

- arXiv: https://arxiv.org/abs/2203.08913
- ICLR 2022 OpenReview entry (search by title)
- Local verbatim text extract: `toolu_01CyFEDSQ7a3KDFKMoWmztfJ.json` (full paper as JSON-wrapped text, ~58KB)

## Key claims (with our restatements)

### Architecture: single mid-layer kNN-augmented attention

**Paper (§3, §4):** *"Unless specified otherwise, we use the 9th layer as the kNN augmented attention layer."* Architecture: 12-layer decoder-only transformer with embedding size 1024, 8 attention heads of dimension 128, FFN hidden size 4096. The kNN-augmented layer runs standard dense self-attention AND approximate kNN attention over external memory in parallel; outputs combined via learned per-head sigmoid gate.

Layer depth ablation (Table 14, paper): layers 3/6/9/12 give perplexities 2.40 / 2.36 / 2.37 / 2.43 on arXiv. Layer 6 marginally best; layer 9 within noise.

Rationale verbatim: *"adding memory to the middle of the layer stack will obtain the best result, whereas adding memory to layers either too close to the input or to the output obtained less gains."*

**Our restatement:** `[ASSERTED]` The empirical anchor for the caddy's **single-mid-layer integration door (D2)**. The "70% depth" heuristic in [caddy-architecture](../concept/caddy-architecture.md) traces directly to MemTx's layer-9-of-12 finding. The "too early / too late is wrong" architectural intuition is grounded in this paper's ablation.

### Combination via learned per-head sigmoid gate

**Paper (§3.1):** *"The same queries are used for both the local context, and for the external memory."* Combination: `V_a = V_m ⊙ σ(g) + V_c ⊙ (1 − σ(g))` where `bg` is *"a learned per-head scalar parameter."* Gate is **content-unconditional** — one bias per head, not a function of token content.

Empirical observation: *"In our experiments, the value of the gate g does not depend on the content of the token at each position... We did observe that over time, most heads learned to attend almost exclusively to external memory."*

**Our restatement:** `[ASSERTED]` Two findings the caddy design inherits and refines:
- Combination-via-learned-gate is a well-understood, training-time-learnable primitive (T1)
- MemTx's **content-unconditional gate** is a known limitation. The caddy [architecture](../concept/caddy-architecture.md) refines to **content-conditional gating** so the model can learn *when* to use memory vs. local, rather than averaging it as a fixed bias. This is a known-good architectural pattern in modern variants (e.g., MoE routing).

The "heads learn to attend almost exclusively to external memory" finding is **emergent, not designed**: the gate is unconditional, the training objective is just LM loss, the heads found their niche by becoming long-range specialists at the one layer where memory was available. Useful precedent for *expecting* memory-specialization to emerge under co-training, but cautionary about over-reliance under unconditional gates.

### Bolt-on viability: finetune-to-add-memory at 4% of pretraining cost

**Paper (§4.5), verbatim:** *"We took a pre-trained 1B vanilla Transformer model, and fine-tuned it to use external memory... Within 20K steps (4% of the pre-training time) the fine-tuned model has already closed 85% of the gap... after 100k steps it has closed the gap entirely."*

**Our restatement:** `[ASSERTED]` The **load-bearing precedent** for the caddy's "lightly-finetune base LLM to add memory" architectural commitment. This shows that a pretrained vanilla transformer can be *retrofitted* with external memory by finetuning, recovering 100% of the gap to a from-scratch trained memorizing transformer in 4% of pretraining cost.

**Caveat:** they finetune the *whole* base model, not just the new gate parameter. They did NOT demonstrate "freeze base entirely, train only the adapter." So the cost isn't free — but it's tiny compared to from-scratch training. The "frozen-base + bolt-on" claim should be softened to "lightly-finetuned base + bolt-on" — which is what the caddy commits to.

### Non-differentiable external memory store

**Paper (§3.1):** *"after each training step, the (key, value) pairs in the local context are appended to the end of the external memory."* Memory contents are the (K, V) pairs computed at the kNN-augmented layer itself. Memory is **frozen-after-write** per entry; only the model parameters that produced them change over time (the staleness problem).

Approximate kNN: *"We use a simple approximation of kNN for TPUs, which has a recall of about 90%."* Default k=32 (ablation shows k=128 gives 0.01 ppl improvement; diminishing returns past k=32).

Maximum memory size tested: 262K. Table 5 shows monotonic gains: 8K → 65K → 131K → 262K all improve perplexity.

**Our restatement:** `[ASSERTED]` Memory contents being **non-differentiable** is a fundamental design property — the kNN is purely retrieval; gradients do NOT flow into stored memory entries. The trainable components are: the gate parameters, the host layer's projections (W_Q, W_K, W_V), and any base-model finetune. This shape carries forward to the caddy, where the *representations* are produced by learned encoder parameters (which DO get gradients during co-training), but the *stored content* is frozen-at-write.

### Per-document FIFO; no cross-session memory

**Paper (§3.1, Ethics section):** *"Each subsequence in the batch comes from a different document, and thus requires a separate external memory, which is cleared at the start of each new document."*

**Our restatement:** `[ASSERTED]` **The biggest dis-analogy with the caddy concept.** MemTx memory is per-document scratch with FIFO eviction; never tested for cross-session retention; never demonstrated for persistent memory across deployments. The caddy explicitly addresses the gap MemTx leaves open — cross-session persistent memory with learned consolidation policies.

### MBP-was-dropped: no auxiliary loss

**Paper:** Trained with LM loss only. No auxiliary objective on the memory representations themselves. No reconstruction loss, no JEPA-style predictive loss, no contrastive loss on memory content.

**Our restatement:** `[ASSERTED]` MemTx is the canonical example of the **MBP-was-dropped** lineage. MERLIN (Wayne 2018) had MBP (Memory-Based Predictor, an auxiliary world-model loss on memory representations); MemTx inherited MERLIN's architectural shape but dropped the auxiliary loss. This is the central empirical gap the caddy's T_A1 commitment proposes to fill. See [open-question/memory-caddy](../open-question/memory-caddy.md) and [caddy § The MBP-was-dropped empirical question](../concept/caddy.md).

## Important caveats

- **Memory contents are layer-9-K/V vectors tied to specific model weights.** Swapping the base model invalidates the store. Not model-agnostic.
- **Memory is per-document, not persistent.** All "long context" results are within one document. No claim about cross-session retention is made or supported.
- **Distributional shift / staleness** (Sec 3.2): *"The model parameters that produce the queries change over time, and will thus have shifted since the keys and values were stored. For very large memories, older records may become 'stale.'"* Mitigated by key/query normalization but not eliminated.
- **Sparse benefit:** *"the benefit of external memory is somewhat sparse. The improvement in perplexity seems to be mainly driven by a small percentage of tokens"* — rare names, citations, function names. Memorization helps with the long tail, not with average prediction.
- **No catastrophic-forgetting test on the base.** The finetune-to-add-memory result (§4.5) updates the whole model. Whether base knowledge degrades is not measured.
- **No "frozen base, train only gate" ablation.** The strictest sidecar claim (no base updates at all) is NOT demonstrated.

## Relevance to Kyrja

- **Architectural template for the caddy's read path.** Single mid-layer cross-attention + learned gate. See [caddy-architecture § Research prototype specification](../concept/caddy-architecture.md#research-prototype-specification--load-bearing-t4-research-targets).
- **Bolt-on viability proof.** §4.5 is the strongest existing evidence that a pretrained LLM can be retrofitted with external memory at modest cost. The caddy inherits this finding.
- **Demarcates what the caddy adds beyond MemTx.** MemTx provides architecture; the caddy adds cross-session persistence, learned representations (not raw K/V), auxiliary loss (T_A1), and schema-fit-modulated consolidation.
- **Cited by:** [caddy](../concept/caddy.md), [caddy-architecture](../concept/caddy-architecture.md), [caddy-interface-doors](../concept/caddy-interface-doors.md), [open-question/memory-caddy](../open-question/memory-caddy.md), [substrate-paradigms](../concept/substrate-paradigms.md), [memory-consumer-axis](../concept/memory-consumer-axis.md).

## Audit history

- 2026-05-17 — Verbatim read via arXiv full-text extraction. Subagent extraction with structured prompts; key quotes verified against the paper text. Replaces prior `[pending]` link. Conducted by Nils (indigo).

## Archive location

- arXiv source: https://arxiv.org/abs/2203.08913 (PDF: https://arxiv.org/pdf/2203.08913.pdf)
- Local verbatim text extract (full paper, JSON-wrapped): `toolu_01CyFEDSQ7a3KDFKMoWmztfJ.json`
- No PDF in `papers` yet (`[pending-pdf]` — AJ can add if verbatim re-quoting needed)
