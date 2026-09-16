---
type: source
name: "Fountas et al. 2024 — Human-inspired Episodic Memory for Infinite Context LLMs (EM-LLM, ICLR 2025)"
status: timeless
last_ingested: 2026-05-21
sources: []
tags: [em-llm, event-segmentation, surprise-based, modularity-graph, norman-rubric-ceiling, fountas, iclr-2025, kv-cache-management]
---

## Citation

Fountas, Z. et al. (2024). *Human-inspired Episodic Memory for Infinite Context LLMs.* arXiv:2407.09450. Accepted at the Thirteenth International Conference on Learning Representations (ICLR 2025).

Affiliations: Huawei Noah's Ark Lab and UCL.

## Location

- arXiv: https://arxiv.org/abs/2407.09450
- Cited by [dong-2025-norman-episodic](./dong-2025-norman-episodic.md) reference [66]
- Local verbatim text extract: `mcp-arxiv-download_paper-1778979158657.txt` (full paper as plain text, ~140KB on a single line)

## Major correction landed 2026-05-17

`[ASSERTED]` **EM-LLM is NOT a sidecar architecture.** Prior wiki framing (this page in STUB form, and conversational shorthand) had positioned EM-LLM as "the closest sidecar precedent" for the caddy. Verbatim read corrects this: EM-LLM operates as a **per-layer, per-head KV-cache management scheme inside the existing self-attention pipeline at every layer**. The base LLM is frozen — true — but the integration is far more intrusive than a clean sidecar.

This correction has propagation implications: EM-LLM remains the Norman-rubric ceiling we must beat, but the architectural template for the caddy comes from [Memorizing Transformer](./wu-2022-memorizing-transformer.md), not EM-LLM. See [caddy-architecture](../concept/caddy-architecture.md) for the corrected framing.

## Key claims (with our restatements)

### Architecture: frozen base, per-layer per-head KV-cache substitution

**Paper §3.1, verbatim:** *"EM-LLM is designed to be applied directly to pre-trained LLMs."* Five base LLMs tested without modification: Mistral-v2 (7B), LLaMA-3 (8B), LLaMA-3.1 (8B), Phi-3, Phi-3.5. Headline figures use LLaMA-3.1-8B. From the abstract: *"EM-LLM, a novel approach that integrates key aspects of human episodic memory and event cognition into LLMs **with no fine-tuning**."*

Context is split into three groups: 128 initial "attention sink" tokens, the local context (most recent tokens, fits within the underlying LLM's native window, uses full softmax attention), and evicted tokens managed by the episodic memory. At inference, retrieved events' KV pairs are concatenated into the attention computation alongside local context, sinks, and contiguity-buffer events.

Verbatim from appendix E.1: *"Retrieval is done individually per-layer further supporting the transformer's learned ability to focus on different aspects of the sequence."*

Retrieved tokens get a fixed positional embedding because their original positions are out of distribution (citing Raffel et al. 2020, Xiao et al. 2024a).

**Our restatement:** `[ASSERTED]` EM-LLM is **fully frozen base + zero trainable components**. The entire pipeline (surprise detection, boundary refinement, representative-token selection, kNN, contiguity buffer) is hand-engineered. This is the strongest possible "no co-training needed" stance — but it pays for it in architectural intrusiveness. The caddy concept goes the other direction: lightly-finetuned base + trainable caddy module + simpler integration point.

### Event segmentation: surprise threshold + modularity-graph refinement

**Paper §3.2, Equation (1), verbatim:** *"a token x_t is considered a potential boundary if its surprise value exceeds a threshold T: −log P(x_t|x_1,…,x_{t−1};θ) > T with T = μ_{t−τ:t} + γ σ_{t−τ:t}"*

Surprise signal is the base LLM's own next-token NLL. Adaptive threshold: rolling mean + γ·std over a window of offset τ. γ values: 1, 2, 1, 1, 1 for Mistral, LLaMA-3, LLaMA-3.1, Phi-3, Phi-3.5.

Graph-theoretic refinement (Algorithm 1): after surprise produces candidate boundaries `B = {b_1,…,b_k}`, the algorithm sweeps each adjacent pair (α, β) and moves β to `argmax_{β̂ ∈ (α, β]} f(A, {α, β̂})` where `A^h_{ij} = sim(K^h_i, K^h_j)` is the dot-product similarity matrix of attention keys within the local context window, treated as a weighted adjacency matrix.

Two metrics tested: **modularity** (Newman–Girvan, maximized) and **conductance** (minimized). Modularity wins empirically.

**Our restatement:** `[ASSERTED]` The event segmentation mechanism is more sophisticated than secondary citations suggested. Surface threshold + graph-theoretic refinement using modularity over attention key similarity. This is the **architectural template for the caddy's E1 op** (surprise-based event boundary detection). The caddy research prototype inherits this mechanism wholesale.

### Retrieval: per-layer per-head query against representative tokens

**Paper §3.4, verbatim:** *"each layer retrieves and attends to these k events individually."*

Retrieval cue: the current query vector q at that layer/head — the LLM's own attention query, not a separately learned encoder. kNN over per-event "representative tokens" selected per InfLLM (Xiao et al. 2024a). Similarity = dot product between current query and event representatives. Approximate kNN via FAISS for large stores.

Temporal-contiguity buffer: FIFO queue of size k_c. When an event is retrieved by similarity, its neighbors within ±n positions in the original sequence are enqueued. n = 1 in all experiments. Total events into context k = k_s (similarity) + k_c (contiguity). Tuned ratio k_r = k_c/k preferred at 0.3 (similarity dominates).

**Our restatement:** `[ASSERTED]` Per-layer per-head retrieval is what makes EM-LLM intrusive. Every layer's attention computation has memory access. This contrasts sharply with [Memorizing Transformer](./wu-2022-memorizing-transformer.md)'s single-layer integration. The caddy follows MemTx's single-layer pattern, not EM-LLM's per-layer pattern.

The **temporal contiguity buffer** is the mechanism Norman et al. credit EM-LLM for satisfying property 4 (partial — local contiguity only, not scale-invariant TCM-style).

### What's stored: raw KV pairs, write-once

**Paper §3.2:** Episodic memory is *"the organised, event-based collection of past key-value pairs."* Stored form: raw KV pairs from the base LLM's attention layers, plus indices/identities of representative tokens per event for the kNN index. Not learned embeddings, not raw tokens, not compressed summaries.

Mutability: write-once / append-only. Events form as surprise threshold is crossed; refinement adjusts boundary positions before commit. No described update, overwrite, or consolidation step. Authors flag this as a limitation (E.1 §3.4: *"The model lacks mechanisms for long-term memory formation processes and systems consolidation"*).

**Our restatement:** `[ASSERTED]` The stored-as-raw-KV property is the **deepest dis-analogy with the caddy**. EM-LLM stores K/V vectors tied to the specific base model's weights — swapping base models invalidates the store. The caddy stores **learned representations** produced by a trainable encoder, in a representation space that's co-trained with the consumer's query head. Storage is model-agnostic at the K-space level (assuming Q/K alignment is maintained).

### Empirical results: passkey 100% accuracy to 10.2M tokens

**Paper, headline:** vs InfLLM (prior SOTA group-kNN retrieval): *"EM-LLM is able to improve on InfLLM across 5 different base LLMs, 80% of individual task groups of LongBench and on the overall average … with up to a 40% and 29.7% improvement over InfLLM"* on retrieval and QA tasks.

vs RAG (NV-Embed-v2) on LLaMA-3.1-8B: *"exceeding the performance of NV-Embed-v2 by 30.5% on LongBench and by 11.5% on ∞-Bench."*

Passkey scaling: 100% accuracy up to 10.2M tokens.

Benchmarks: LongBench (Bai et al. 2023), ∞-Bench (Zhang et al. 2024), PG-19 (for segmentation quality), human-annotated podcast dataset (Kumar et al. 2023) for human-event-boundary correlation. **No NIAH (separately) and no BABILong.**

**Our restatement:** `[ASSERTED]` EM-LLM convincingly beats prior long-context retrieval baselines on LongBench and ∞-Bench, *within a single context*. This is the **2.5/5 Norman-rubric ceiling** — the highest published score. The caddy research prototype targets 3.5-4/5, beating this decisively while staying within feasibility bounds.

### Author-flagged limitations

**Paper §E.1:**
1. **Non-parametric** — *"our method relies on non-parametric storage of key-value pairs"*. No learning into weights.
2. **No hierarchical event structure** — *"lacks the sophisticated nested event representations observed in human cognition."*
3. **No cross-modal integration** in current implementation.
4. **No memory consolidation** — no long-term / systems-consolidation analog.

Authors are careful: *"we only claim an EM-inspired approach, rather than an actual human-like EM process"* (E.1).

**Our restatement:** `[ASSERTED]` Authors explicitly identify the gaps the caddy proposes to fill: (1) learned parametric storage via T_A1; (4) memory consolidation via K2+T_A3. EM-LLM stops at the architectural pattern; the caddy continues into the training-time mechanisms that pattern enables.

## Norman-rubric score: ~2.5/5

`[ASSERTED]` Kyrja-internal scoring based on full verbatim read 2026-05-17:

| Norman property | EM-LLM | Reasoning |
|---|---|---|
| N1 Dynamic memory updating | ✗ | No reconsolidation mechanism; events frozen-at-write |
| N2 Event segmentation | ✓ | Surprise + modularity refinement, fully implemented |
| N3 Selective encoding | ✓ | Boundary-aligned encoding is implicit selectivity |
| N3 Selective retrieval | partial | Triggered every layer/head, not by prediction failure or schema gap |
| N4 Temporal contiguity | partial | Local contiguity only (n=1), not scale-invariant TCM |
| N5 Competition | partial | kNN top-k (k_s), bounded but not winner-take-all |

**Score: ~2.5/5.** Highest among published MA-LLMs. Empirical ceiling for the caddy to beat.

## Important caveats

- **NOT a sidecar architecture.** Per-layer per-head KV-cache management; deeply intrusive. The "frozen base" property comes at the cost of architectural intrusiveness.
- **No cross-session persistence.** All claims are within-context (passkey works to 10.2M *within one context window*; nothing about retention across deployments).
- **Storage is base-model-specific.** K/V vectors are tied to the base model's layer weights. Swap models, invalidate the store.
- **No learned representations.** The "episode" is just a span of original KV; no compact, model-agnostic descriptor.
- **Hyperparameters grid-searched, not learned.** γ, k_r, etc. tuned on LongBench. Doesn't generalize across deployments without re-tuning.
- **Memory cost grows with sequence.** Appendix C documents GPU/CPU memory overhead scaling.

## Relevance to Kyrja

- **The Norman-rubric ceiling we must beat.** EM-LLM is the empirical baseline. Caddy research prototype target: 3.5-4/5.
- **Architectural template for E1 (event segmentation).** Surprise + modularity-graph refinement is the cleanest published mechanism. Caddy inherits.
- **Demarcates the integration-architecture trade-off.** EM-LLM = frozen base + intrusive integration. Caddy = lightly-finetuned base + simple integration. Different sweet spots in the design space.
- **The "no consolidation" gap is exactly the caddy's wedge.** EM-LLM authors explicitly flag this; the caddy's K2+T_A3 commitment proposes the fill.
- **Cited by:** [caddy](../concept/caddy.md), [caddy-architecture](../concept/caddy-architecture.md), [caddy-interface-doors](../concept/caddy-interface-doors.md), [norman-rubric](../concept/norman-rubric.md), [open-question/memory-caddy](../open-question/memory-caddy.md).

## Audit history

- 2026-05-16 — STUB created based on Norman et al. 2025 secondary commentary.
- 2026-05-17 — Promoted STUB → full verbatim read. Major correction: NOT a sidecar; per-layer per-head KV-cache management inside attention pipeline. Conducted by Nils (indigo) via subagent extraction.
- 2026-05-20 — Implementation availability recon (Nils). See **Implementation availability** section below.

## Implementation availability

`[ASSERTED]` Repository: [github.com/em-llm/EM-LLM-model](https://github.com/em-llm/EM-LLM-model). License: **MIT** (THUNLP 2024 copyright). Official ICLR 2025 reference implementation.

**Code structure (2026-05-20 recon):**

- `em_llm/attention/similarity_refinement/` — **isolated, ~142 lines, pure PyTorch.** Contains `segmentation.py` (`events_with_similarity_adjustment(events_base, A, ...)`, 50 lines) and `similarity.py` (`modularity`, `conductance`, `intra_inter_sim`, `calc_adjacent_similarity_with_offset`, 92 lines). Zero coupling to the rest of the EM-LLM pipeline. **Liftable wholesale under MIT (attribute).**
- `em_llm/attention/context_manager.py` and `em_llm/attention/em_llm.py` — surprise-threshold detection is embedded here (1019 + 276 lines) but the algorithm itself is trivial: NLL surprisal computed as `prob = softmax(logits); surprisal = -log(gather(prob, labels))` (2 lines), thresholded as `divide = surprisal > gamma * std(window) + mean(window)` (1 line). Reimplemented standalone in ~30 lines without lifting the surrounding KV-cache plumbing we don't need.

**Integration estimate for caddy work: ~1 day total**, not the 1-2 weeks earlier audit suggested. Lift `similarity_refinement/` wholesale; reimplement the threshold detector; hook HF attention-key extraction at the configured refinement layer. The "moderately coupled" framing from the GitHub UI was misleading because the *algorithm* is exceptionally clean; what's coupled is the *segmentation-triggered-inside-the-inference-KV-cache-loop*, which we don't need (we segment offline, once, on a training corpus).

**Hyperparameters inherited from paper:**

- γ (surprise-threshold scaling): 1.0 for LLaMA-3.1-8B, LLaMA-3-8B was 2.0, Mistral-v2-7B 1.0, Phi-3 1.0, Phi-3.5 1.0. **Phi-3-mini inherits γ=1.0.**
- Refinement metric: modularity (won empirically over conductance in their experiments; default in `events_with_similarity_adjustment`).
- τ (rolling window offset): paper default; preserved.

**Caveat — base-LLM specificity:** the refinement adjacency matrix `A` is computed from base-LLM attention keys. Segmentation outputs are therefore tied to the chosen base LLM; switching base models requires re-running segmentation. This is fine for an offline pre-training pipeline (segment once per base-model decision) but worth knowing if the experiment iterates on the base model.

## Archive location

- arXiv source: https://arxiv.org/abs/2407.09450
- Local verbatim text extract (full paper): `mcp-arxiv-download_paper-1778979158657.txt`
- No PDF in `papers` yet (`[pending-pdf]` — AJ can add if verbatim re-quoting needed)
