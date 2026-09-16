---
type: source
name: "Ge et al. 2024 — In-context Autoencoder for Context Compression in a Large Language Model (ICAE)"
status: timeless
last_ingested: 2026-05-20
sources: []
epistemic_tags: [asserted]
tags: [icae, context-compression, autoencoder, lora-encoder, frozen-decoder, memory-slots, dual-objective, ae-lm, t_a1b, h44, auxiliary-loss-precedent]
---

## Citation

Ge, T., Hu, J., Wang, L., Wang, X., Chen, S.-Q., Wei, F. (2024). *In-context Autoencoder for Context Compression in a Large Language Model.* ICLR 2024. arXiv:2307.06945 (v3 / camera-ready). Microsoft Corporation. Code & models: https://github.com/getao/icae.

## Location

- arXiv: https://arxiv.org/abs/2307.06945
- Local verbatim text extract: `mcp-arxiv-read_paper-1779311385353.txt` (~76.5K characters on a single line; slice via `python3 -c "print(open(path).read()[A:B])"` in ≤80K-char spans).

## Why we care

ICAE is repeatedly cited across the wiki as **the closest existing precedent for "auxiliary objective on a memory module" at LLM scale** — most visibly in [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) (evidence-for §), [concept/caddy](../concept/caddy.md) (precedents list), [concept/caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) (commitment 5 evidence), and [open-question/memory-caddy](../open-question/memory-caddy.md) (auxiliary-loss precedent paragraph). The shorthand has been "dual pretraining objective (autoencoding reconstruction + LM continuation), Table 5 shows AE+LM beats either alone, existence proof for auxiliary loss on memory representations."

This verbatim read tests that shorthand against paper text. **The framing is mostly correct in mechanism but materially imprecise in two ways**: (i) Table 5 is win-rate pairwise comparisons on a downstream instruction-following task after fine-tuning, *not* a clean pretraining-loss ablation; (ii) the gradient path is "auxiliary loss on the encoder that produces memory slots," not "auxiliary loss on the memory slots as a representation module with internal parameters." Both nuances flow forward into H44 design choices.

## Key claims (with our restatements)

### Architecture: LoRA-adapted encoder + frozen decoder, both based on the same target LLM

**Paper §2.1, verbatim:**

> "Like a typical autoencoder (Kramer, 1991), ICAE consists of an encoder and a decoder. Similar to the design of Gisting (Mu et al., 2023) and AutoCompressor (Chevalier et al., 2023), the ICAE performs both the encoding and decoding processes in an in-context manner"

> "Given the intuition, we propose to use a LoRA-adapted LLM as the encoder of the ICAE, as illustrated in Figure 3. When encoding a context c = (w_1, ..., w_L) with the length L, we first append k (k << L) memory tokens (m_1, ..., m_k) to the context c to obtain their outputs (m̃_1, ..., m̃_k) as the memory slots for the context c. Therefore, the ICAE encoder is very lightweight – it only adds a LoRA adapter and an embedding lookup for memory tokens compared with the target LLM."

> "we use the untouched target LLM as the decoder of the ICAE to ensure the compatibility of memory slots within the target LLM."

**Paper §3.1, verbatim (model configuration):**

> "We use the LlaMa (Touvron et al., 2023a;b) as the target LLM to test the ICAE's performance in context compression. For the encoder of the ICAE, LoRA is applied to the query and value projections of the LLM's multi-head attention. In our default setting, the memory slot length k is set to 128, and the LoRA rank r is set to 128 unless otherwise specified. The resulting ICAE only adds about 1% learnable parameters on top of the target LLM."

**Our restatement:** `[ASSERTED]` Encoder is the target LLM with a LoRA adapter on Q/V projections (rank 128) plus a learnable embedding lookup `e_m` for `k=128` special memory tokens. Decoder is the *untouched* (frozen) target LLM — same weights, no LoRA. Both share the same base model (Llama-7b, Llama-2-7b, Llama-2-7b-chat, Llama-2-13b-chat across experiments). The encoder is run with the input context concatenated with `k` learnable memory token IDs; the hidden states *at the memory token positions* in the encoder's final layer become the memory slots. The decoder consumes those memory slots (as input embeddings/hidden states, not token IDs) prefixing the prompt. **Wiki framing was correct on architecture.**

### Loss formulation: explicit weighted sum of AE and LM, λ ∈ [0.4, 0.6]

**Paper §2.2.1, Eq. (AE), verbatim:**

> "L_AE = max_{m̃_1,...,m̃_k} P(c | m̃_1,...,m̃_k; Θ_LLM) = max_{Θ_LoRA, e_m} P(c | m_1...m_k; Θ_LLM, Θ_LoRA, e_m)"

> "To indicate the autoencoding task, we append a special token '[AE]' to (m̃_1,...,m̃_k) in the decoder, as Figure 3 shows. As this pretraining objective does not need any extra annotation, we can use massive text data to train the In-context Autoencoder."

**Paper §2.2.2, Eq. (LM), verbatim:**

> "L_LM = max_{m̃_1,...,m̃_k} P(o | m̃_1,...,m̃_k; Θ_LLM) = max_{Θ_LoRA, e_m} P(o | m_1...m_k; Θ_LLM, Θ_LoRA, e_m)"

> "where o = (w_{L+1},...,w_{L+N}) denotes the continuation of context c."

**Paper §3.2.2 footnote 3, verbatim (the combined pretraining loss):**

> "L_pretrain = λ L_AE + (1 − λ) L_LM. We find λ = 0.4 ∼ 0.6 leads to the best result."

**Paper §3.2.2, verbatim (the AE+LM mix is justified empirically):**

> "We also examine pretraining objectives and find combining AE and LM yields better results than using AE or LM individually (the 4th row in Table 5)."

**Our restatement:** `[ASSERTED]` Pretraining objective is a *linear combination* of two cross-entropy / NLL terms — neither term is a representation-space distance (no L1/L2/cosine on the memory slots themselves). **Both terms are decoder-side next-token losses, differing only in target text:** AE targets the original input `c`; LM targets the continuation `o` following `c`. The `[AE]` special token routes the decoder between the two tasks. λ ≈ 0.5 (paper's empirical sweet spot 0.4–0.6 — no further ablation reported on λ value). No curriculum / no schedule on λ is described; presumed constant across pretraining. **Wiki framing on "dual objective AE + LM" is correct; the precise form (weighted sum, single-headed, both decoder-side LM losses on different target spans) was not previously documented.**

### Compression ratio: 512 → 128 memory slots = 4×; per-document, not experiential

**Paper §3.1, verbatim:**

> "By default, the maximal token length (excluding memory slots) we set during training is 512 in both the ICAE's encoder and decoder in our experiments."

**Paper §1, verbatim:**

> "We show the ICAE (based on Llama) learned with our pretraining and fine-tuning method can effectively produce memory slots with 4× context compression."

**Paper §3.2.1, Figure 5 + Table 1, verbatim:**

> "Compared to k=128 where the BLEU score can still reach over 95% at a context length of 500, the BLEU scores become much less satisfactory for k values of 64 and 32, indicating an inability to losslessly retain the original context. ... This observation is also evident from the loss curve, suggesting that achieving over 4× compression is rather challenging."

**Paper §3.3.3, verbatim (multi-span extension):**

> "Thus far, we have mainly discussed a single span of memory slots. In this section, we shall discuss multiple spans of memory slots. As illustrated in Figure 6 (Left), we can segment a long context into N chunks, compress them individually, and then concatenate them to represent the original long context. However, this did not work initially, because the model had never seen multiple span concatenation patterns during training. Fortunately, we can incorporate a small number of multiple span concatenation samples during training, enabling the model to work with concatenated spans of memory slots"

**Our restatement:** `[ASSERTED]` Per-document, one-shot compression: one input span of up to 512 tokens compresses to k=128 memory slots, ratio 4×. Higher compression (k=64 at 8×, k=32 at 16×) is reported but with significant lossiness. Multi-span (long-context) operation is achieved by *chunking and concatenating* compressed spans, not by training one encoder forward on a long context — meaning long-context memory is composed of independent local compressions, *not* a single representation accumulating across the input. **Wiki framing on "one document → ~128 memory slots" is correct.** The wiki has been precise that ICAE's scope is per-context, not experiential-memory-across-deployments; this read confirms that.

### Table 5 ablation: pairwise win rates on PwC test set after fine-tuning, judged by GPT-4

**Paper §3.2.2 + Table 5, verbatim:**

> "Table 5: ICAE with different memory slot lengths and different pretraining setups. The last row is the comparison between 128-length ICAE's memory and 128-token summary produced by the GPT-4."

Table 5 (verbatim, all rows are Llama-2-7b-chat ICAE):

| System 1 | System 2 | win % | lose % | tie % | win/lose |
|---|---|---|---|---|---|
| k=128 (pretrained) | k=64 (pretrained) | 57.6 | 19.5 | 22.9 | 3.0 |
| k=64 (pretrained) | k=32 (pretrained) | 44.7 | 21.8 | 33.5 | 2.1 |
| k=64 (pretrained) | k=128 (no pretraining) | 33.1 | 28.0 | 38.9 | 1.2 |
| k=128 (pretrained) | k=128 (no pretraining) | 60.4 | 9.5 | 30.1 | 6.4 |
| k=128 (pretrained) | k=128 (pretrained only with AE) | 36.4 | 28.5 | 35.1 | 1.3 |
| k=128 (pretrained) | k=128 (pretrained only with LM) | 35.1 | 24.9 | 40.0 | 1.4 |
| k=128 (pretrained) | 128-token summary (by GPT-4) | 34.1 | 17.6 | 48.3 | 1.9 |

**Paper §3.2.2, the ablation narration, verbatim:**

> "Under the same ratio, the pretrained ICAE performs much better than its non-pretrained counterpart, emphasizing the importance of pretraining."

> "We also examine pretraining objectives and find combining AE and LM yields better results than using AE or LM individually (the 4th row in Table 5)."

(N.B. The paper says "the 4th row" but the AE-only and LM-only comparisons are at rows 5 and 6 of the table as written; the 4th row is "pretrained vs no-pretraining". This appears to be a paper-side numbering slip — the relevant AE-only / LM-only rows are 5 and 6 and they do support the claim that combined AE+LM beats either alone.)

**Our restatement:** `[ASSERTED]` Table 5 is **GPT-4-judged pairwise win/lose/tie on PwC instruction-following responses**, not a pretraining-loss ablation. The metric is downstream instruction-task quality after both pretraining *and* PwC fine-tuning, not reconstruction loss or perplexity. Findings:
1. Pretraining > no-pretraining at same k (60.4 / 9.5 / 30.1, win/lose ratio 6.4).
2. AE+LM combined > AE-only (36.4 / 28.5 / 35.1, ratio 1.3) and > LM-only (35.1 / 24.9 / 40.0, ratio 1.4) — *modest but consistent gains*.
3. 128 memory slots (pretrained) > 128-token GPT-4 summary (34.1 / 17.6 / 48.3, ratio 1.9) — memory slots are denser than natural-language summaries at same token budget.

**Wiki framing was approximately right** on "AE+LM beats AE-only, beats LM-only, beats no-pretraining" but elided two important nuances: (a) the metric is judged downstream task quality after fine-tuning, not pretraining loss; (b) the AE-only and LM-only deltas are *small* (win/lose 1.3–1.4) — the strong effect is pretraining-vs-none (6.4×), not the precise mix.

### Training scale and data

**Paper §3.1, verbatim:**

> "We pretrain the ICAE with the Pile (Gao et al., 2020). For instruction fine-tuning, we use the PwC dataset, as introduced in Section 2.3, which contains 240k (context, prompt, response) samples for training and 18k samples for testing."

**Paper Appendix A, Table 8, verbatim (hyperparameters):**

| Hyperparameter | Value |
|---|---|
| Optimizer | AdamW |
| learning rate | 1e-4 (pretrain); 5e-5 (fine-tuning) |
| batch size | 256 |
| warmup | 300 |
| #updates | 200k (pretrain); 30k (fine-tuning) |
| clip norm | 2.0 |

**Paper Appendix A, verbatim:**

> "We train the ICAE on 8 Nvidia A100 GPUs (80GB). ... We by default train the ICAE with bf16."

**Our restatement:** `[ASSERTED]` Pretraining: Pile, 200k optimizer steps, batch 256 (so ~51M samples seen, each up to 512 tokens — order of ~26B tokens through the encoder if all 512). Hardware: 8× A100 80GB. Compute is order-of-magnitude smaller than V-JEPA (8 A100 vs V-JEPA's multi-node A100; ~26B tokens vs V-JEPA's 270M video samples), and the model is parameter-efficient (1% LoRA tax on a 7B/13B Llama). **This is a tractable scale** — closer to H44's de-risk budget than V-JEPA's, by 1–2 orders of magnitude. Fine-tuning is 30k steps on 240k PwC samples (multiple epochs).

### Headline downstream result: ICAE memory > Alpaca/StableLM on PwC

**Paper §3.2.2 + Table 4, verbatim:**

> "The Llama-7b (ICAE) conditioned on 128 memory slots largely outperforms both Alpaca and StableLM which can access original contexts (∼512 tokens), with a win rate of 56.7% and 74.1% respectively and a win+tie rate of 73%∼81%. However, when compared to the GPT-4 (we regard it as the gold standard), there is still a significant gap, with around 70% of the cases underperforming the GPT-4's results, and a win+tie ratio of about only 30%."

**Our restatement:** `[ASSERTED]` ICAE's 128-slot memory beats Alpaca / StableLM (which see the *full* original context) — but compared against GPT-4 (which also sees full context) ICAE loses on ~70% of cases. The "memory wins" result is *relative to weak baselines*, not relative to a strong model with access to the same context. This is consistent with ICAE's claim — Llama-7b with compressed memory beats other Llama-tuned-7b with full context — but doesn't show that compression *closes* the quality gap to frontier-quality responses on the same context.

## ⚠ Drift between wiki framing and paper

### Drift 1: "Auxiliary loss on memory representations" vs paper's "decoder-side LM loss on different target text"

The wiki shorthand (e.g., open-question/memory-caddy.md L373, caddy.md L120) describes ICAE as evidence that **"auxiliary loss on memory representations adds signal."** Read carefully, both ICAE objectives (AE and LM) are **decoder-side next-token cross-entropy losses on different target sequences (`c` vs `o`)** — neither is a loss applied *to* the memory representations as a representation-space objective (no L1/L2/cosine in feature space, no representation-prediction target).

The gradient flow is:
- Loss computed in the *frozen decoder's* output token logit space.
- Gradient flows back through the (frozen) decoder weights — they're frozen so they don't update, but gradient *passes through* them.
- Gradient reaches the memory slot positions (= the encoder's hidden states at the memory token positions).
- From there, gradient flows back through the encoder forward pass into Θ_LoRA (encoder LoRA adapter) and `e_m` (learnable memory token embeddings).
- Θ_LLM (base LLM weights) are **not** updated; only Θ_LoRA + e_m are trained.

So the auxiliary objective lands on the *encoder's parameters* (LoRA + memory token embedding lookup), not on the memory slots as a representation-prediction target. There is no JEPA-style structure where "predict feature(target) given feature(context) under a distance loss in feature space" — ICAE's loss is entirely in token space.

**Why this matters for H44:** the H44 hypothesis is JEPA-shaped — feature-space prediction loss on memory representations under stop-gradient + EMA target. ICAE is *not* JEPA-shaped; it's reconstruction-via-frozen-decoder. Both add gradient signal to a memory-producing encoder, but the *type* of inductive bias differs:
- ICAE: "memory slots must be sufficient for the decoder to (a) reconstruct input, (b) continue text." Pressure is on *information sufficiency*.
- H44/V-JEPA: "memory representations must predict masked-region representations under L1 distance." Pressure is on *structural predictability* of representations.

These are *different bets*. ICAE proves that adding decoder-grounded auxiliary loss to a memory-producing encoder beats LM-only and beats no-pretraining. **It does not directly prove that representation-space auxiliary losses (JEPA-shape) work at LLM scale.** Wiki citations of ICAE as evidence for the H44 bet should narrow the claim: ICAE is precedent for "an auxiliary objective on the encoder helps," not for "a JEPA-style feature-prediction loss helps."

### Drift 2: "Table 5 ablation" framing implies pretraining-loss comparison; the actual metric is downstream win-rate

The wiki phrasing "Table 5 ablation: AE+LM beats AE-only, beats LM-only, beats no-pretraining" reads like a standard ablation table (loss / perplexity / accuracy). The paper's Table 5 is **GPT-4 judged pairwise preference on PwC instruction-task outputs after fine-tuning**. The metric is win/lose/tie %.

Implications:
- The signal-to-noise of "AE+LM > AE-only" (win/lose ratio 1.3) is much weaker than the signal of "pretraining > no-pretraining" (6.4). The strongest claim Table 5 supports is "pretraining the encoder matters"; the dual-objective claim is supported but with smaller effect size.
- GPT-4 win-rate is known to favor longer / more fluent outputs (paper itself notes this in §3.1 footnote 7); the comparison is not noise-free.
- This is not a loss-ablation under a fixed downstream protocol — it's a head-to-head preference judgement after a full pretraining + fine-tuning + instruction-task pipeline.

### Drift 3: "LoRA-adapted LLM encoder" — partially right, but the encoder *is* the LLM (with LoRA on Q/V), not a separately initialised module

The wiki phrasing across pages reads naturally as "an encoder LLM separate from the decoder LLM, with LoRA on the encoder." This is *almost* correct: there is only **one base LLM**, and the encoder is that same LLM with a LoRA adapter active on Q/V; the decoder is that same LLM with LoRA *inactive* (the "untouched" target LLM). So encoder weights are decoder weights + a (rank-128 Q/V) delta. The capacity of the "encoder" is essentially the full LLM, not a small dedicated encoder module. This matters for cost / scale calculations (you can't run ICAE without LLM-scale encoder forward) and for transfer reasoning (the encoder benefits from all LLM pretraining; H44's analogue would be a much smaller dedicated encoder, which is a *different bet on capacity*).

## Gradient-flow trace (load-bearing for H44 design)

Trained parameters:
- `Θ_LoRA`: LoRA adapter on the encoder's Q/V projections (rank 128). ~1% of LLM params.
- `e_m`: learnable embedding lookup for the k=128 special memory tokens (k × d, where d is the LLM's hidden dim, ≈ 4096 for Llama-7b → ~0.5M params).

Frozen parameters:
- `Θ_LLM`: all base LLM weights, used in both encoder and decoder forward passes.

Forward pass (autoencoding loss):
1. Encoder input: `c = (w_1, ..., w_L)` token embeddings concatenated with `e_m(m_1), ..., e_m(m_k)`.
2. Encoder runs base LLM forward with LoRA on Q/V. Final-layer hidden states at the k memory-token positions are extracted → `m̃_1, ..., m̃_k`.
3. Decoder input: `m̃_1, ..., m̃_k, e([AE]), e(<bos>)` then teacher-forced generation of `c`.
4. Decoder runs base LLM forward (no LoRA, no adapter — "untouched").
5. Loss is next-token cross-entropy on the reconstructed `c` tokens.

Backward pass:
- Gradient computed in decoder logit space.
- Backprop through frozen decoder weights (Θ_LLM, with no updates applied since they're not in the optimiser's param group).
- Gradient arrives at memory-slot positions `m̃_k` → these are encoder outputs.
- Backprop through encoder forward pass.
- Updates: only `Θ_LoRA` and `e_m`.

**No stop-gradient anywhere in the paper.** The frozen decoder is "frozen" by exclusion from the optimiser, not by `detach()` or `stop-gradient` — gradient passes through it freely.

**No EMA target encoder.** ICAE has no target encoder. The decoder serves the role of "discriminator that grades the memory slots."

**Implication for H44 design:** ICAE's "auxiliary loss" works via *information bottleneck through a frozen decoder that must produce text*. H44's auxiliary loss works via *predicting representations under L1 distance with an EMA target*. The collapse-prevention mechanism is also different:
- ICAE: collapse is prevented because trivially-collapsed memory slots can't reconstruct the input → AE loss spikes. The decoder's text-generation requirement *is* the anti-collapse pressure.
- H44/V-JEPA: collapse is prevented by the BYOL triad (EMA + stop-grad + narrow predictor).

These are *different anti-collapse machineries*. ICAE doesn't directly validate the BYOL-triad's necessity at LLM scale; it validates *a different anti-collapse mechanism* (reconstruction through frozen decoder).

## Ablation gaps (matters for H44 design space)

What ICAE *does* ablate:
- Memory slot length k ∈ {32, 64, 128} (Figure 5 + Table 5). Higher k → lower reconstruction loss, higher BLEU.
- Target LLM scale (Llama-7b, Llama-2-7b, Llama-2-13b at Table 6). Larger LLMs → better compression at same k.
- Pretraining objective: AE-only / LM-only / AE+LM (Table 5 rows 5–6).
- Pretraining vs no-pretraining (Table 5 row 4).
- λ ∈ [0.4, 0.6] (footnote 3, no values shown for the entire range).
- Memory slots vs natural-language summary at same token budget (Table 5 last row).
- Content type for restoration (normal text vs patterned random vs completely random, Table 3).
- Single-span vs multi-span compression (§3.3.3).

What ICAE *does not* ablate (relevant to H44):
- **No λ sensitivity curve.** Only a range "0.4–0.6 best" is reported; no graph or value-by-value comparison. Critical for H44 because our λ on auxiliary loss is a load-bearing hyperparameter.
- **No LoRA rank ablation.** Rank 128 is the default; not varied.
- **No encoder-trained-from-scratch vs encoder-LoRA-on-pretrained-LLM comparison.** This is the load-bearing capacity question for H44: do we need full-LLM-scale encoder, or can a small dedicated encoder do it?
- **No decoder-trained vs decoder-frozen ablation.** Paper architecturally commits to frozen decoder for compatibility-with-target-LLM reasons; no empirical check of whether unfreezing decoder helps or hurts.
- **No representation-space-loss ablation.** No comparison of token-space loss (the paper's choice) to feature-space loss (the JEPA / data2vec / VICReg families).
- **No encoder backbone ablation.** Always Llama; never a different architecture (e.g., bidirectional encoder).
- **No collapse / anisotropy diagnostic on the memory slots.** Are the 128 memory slots actually using their 128 d-dim capacity, or are they low-rank? No effective-rank, no IsoScore, no representation-variance metric.
- **No transfer test.** Memory slots are trained on Pile, tested on PwC (also drawn from Pile + GPT-4-generated). No cross-domain / cross-distribution generalisation test.
- **No comparison to a "no-encoder-pretrain, just-instruction-tune" baseline that uses a stronger initialisation than random.**

## Scope mismatches with H44 (what ICAE *doesn't* claim to demonstrate)

- **Cross-domain structural transfer.** ICAE memory is reconstruction-grade compression of in-distribution text. No claim about structural / analogical / cross-modality transfer.
- **Experiential memory across sessions.** Memory slots are per-document, per-call. No persistence, no consolidation, no accumulation across deployments.
- **Predictive structure in representations.** Memory slots are optimised for *sufficiency* (decoder can reconstruct from them), not for *predictability of future representations* (the JEPA bet).
- **Auxiliary loss flowing through memory representations as a representation-space objective.** ICAE's losses are token-space; H44's loss is feature-space.

## What ICAE *does* genuinely demonstrate (load-bearing parts)

1. A LoRA-adapted LLM, run forward with k learnable memory tokens appended, produces hidden states at those positions that can be fed to a frozen LLM and let it reconstruct the input *with high fidelity* (BLEU >95 at 4× compression, k=128) and continue text plausibly (small PPL delta). **Existence proof that high-bandwidth context-summary representations can be extracted from an LLM with only LoRA-scale parameter additions.**
2. Adding a reconstruction objective *in addition to* an LM-continuation objective beats either alone on downstream instruction-following preference, modestly but consistently. **Existence proof that multi-objective pretraining of a memory-producing encoder helps over single-objective.**
3. Pretraining the encoder is much more important than the specific objective mix. **Pretraining > no-pretraining is the big effect (6.4× win/lose); AE+LM > AE-only or LM-only is the small effect (1.3–1.4× win/lose).**
4. The pattern works at LLM-scale on a manageable compute budget (8 A100 × 200k steps, ~26B tokens). **Tractable precedent at LLM scale.**

## Relevance to Kyrja

- **[H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md)** — Evidence-for paragraph should be narrowed: ICAE proves "auxiliary objective on a memory-producing LoRA encoder helps over LM-only," at 4× context compression scope. It does *not* directly support "JEPA-style feature-prediction loss on memory representations helps cross-domain transfer." The pattern generalises in *kind* (auxiliary loss helps) but not in *shape* (different loss family, different anti-collapse mechanism, different scope).
- **[concept/caddy](../concept/caddy.md)** — Existing description ("LoRA-encoder + frozen LLM decoder, dual pretraining objective (autoencoding reconstruction + LM continuation); Table 5 ablation: combining AE+LM beats either alone") is correct in mechanism. Recommended narrowing: "**Loss landed in token space via the frozen decoder, not in representation space.** Effect sizes are pretraining > none (6.4× win/lose) and AE+LM > either alone (1.3–1.4× win/lose). Scope is per-document compression, not experiential memory."
- **[concept/caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md)** — The "commitment 5" framing (auxiliary loss on memory representations) should distinguish *representation-space* auxiliary loss (the H44 bet) from *token-space-through-frozen-decoder* auxiliary loss (the ICAE pattern). Both add gradient signal to memory-producing encoder parameters; only the first lands in feature space.
- **[open-question/memory-caddy](../open-question/memory-caddy.md)** — The "closest auxiliary-loss precedent" paragraph (L373) is materially correct but should add: "Both objectives are decoder-side token-CE losses on different target spans (input vs continuation), combined as λ L_AE + (1−λ) L_LM with λ ≈ 0.5. The gradient updates the encoder's LoRA + memory token embeddings, not the memory slots as a separate-module representation-space objective."
- **[2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)** — ICAE-as-precedent supports the architectural choice of "LoRA-on-LLM as encoder, frozen decoder for compatibility" if we want to match ICAE's setup. If H44 instead uses a *dedicated small encoder* (not a LoRA-on-LLM), we lose ICAE as a direct architectural precedent and we're betting on a *different point* in the design space.

## Open questions raised by this read

- **Is the encoder's capacity essential?** ICAE's encoder *is* the LLM (with LoRA delta). Can a 100M-param dedicated encoder produce comparable memory slots, or does the encoder need to be LLM-scale to absorb LLM-scale context? Important for H44 cost projections.
- **Token-space vs feature-space auxiliary loss.** ICAE proves token-space-through-frozen-decoder works. The JEPA bet is that feature-space works *better* for predictive structure. Direct comparison is unprecedented at this scale.
- **Does the AE objective implicitly enforce information sufficiency, while the LM objective implicitly enforces useful-for-downstream structure?** If so, the analogous decomposition in H44 might be reconstruction (sufficiency) + feature-prediction (predictability). The two-objective combination is a credible default — ICAE supports the *principle* even if not the *specific* JEPA loss form.
- **λ sensitivity.** ICAE reports 0.4–0.6 as best but no curve. If H44 adopts a λ for an auxiliary feature-prediction loss alongside an LM loss, we have no transferable prior for the λ regime — has to be tuned from scratch.
- **What's the equivalent of ICAE's BLEU-recovery sanity check for our event-rep setting?** ICAE confirms memory slots carry information via token-level reconstruction. H44 needs an analogue: probe that confirms the auxiliary-loss-trained reps carry *more / different* information than LM-only reps, before claiming cross-domain transfer.
