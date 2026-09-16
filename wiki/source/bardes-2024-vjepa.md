---
type: source
name: "Bardes et al. 2024 — Revisiting Feature Prediction for Learning Visual Representations from Video (V-JEPA)"
status: timeless
last_ingested: 2026-05-20
sources: []
epistemic_tags: [asserted]
tags: [v-jepa, jepa, byol-family, feature-prediction, ema-target, stop-gradient, frontier-anchor, t_a1b, h44]
---

## Citation

Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., Assran, M., Ballas, N. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video.* arXiv:2404.08471. Meta FAIR + collaborators. Code: https://github.com/facebookresearch/jepa.

## Location

- arXiv: https://arxiv.org/abs/2404.08471
- Local verbatim text extract: `mcp-arxiv-download_paper-1779306299788.txt` (~121K characters on a single line; slice via `python3 -c "print(open(path).read()[A:B])"` in ≤80K-char spans).

## Why we care

V-JEPA is the **frontier-adjacent anchor** for the auxiliary loss in our load-bearing T4 research target T_A1b (see [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md)). Our experiment proposes to lift the V-JEPA recipe (encoder + narrow predictor + EMA target + stop-gradient + feature-space loss) from video patches to event-segmented text representations. This page anchors the claim "what V-JEPA actually does vs. what we're proposing" so deliberate deviations are visible and defensible (per [[feedback_load_bearing_sources]]).

## Key claims (with our restatements)

### The loss is L1 in feature space, not cosine

**Paper §3.1, Eq. 1, verbatim:**

> "minimize_{θ,φ} ‖P_φ(E_θ(x), Δ_y) − sg(Ē_θ(y))‖_1"

where `E_θ` is the encoder (over the unmasked context `x`), `P_φ` is the predictor (conditioned on positional information `Δ_y` for the masked region), `Ē_θ` is the EMA target encoder, and `sg(·)` is stop-gradient. **Paper §3.1, on the choice:**

> "we modify it to use an ℓ_1 regression, which we found to be more stable"

The predecessor I-JEPA used L2. V-JEPA explicitly moves to L1 *for stability*. Targets are **per-token, un-normalised** features from the y-encoder output (not pooled, not normalised). **Paper §9, Eq. 2:**

> "Loss = (1/M) Σ_{k ∈ (i_1,...,i_M)} ‖ŝ_k − s_k‖_1 — the average L_1 distance between the output of the predictor and the y-encoder"

**Our restatement:** `[ASSERTED]` The loss is L1, *not* cosine. The BYOL-family lineage uses cosine-on-normalised features (which is MSE-equivalent on unit vectors), but V-JEPA deliberately departs from that — un-normalised features + L1. H44 adopts L1 to match this frontier anchor and to preserve magnitude information in event reps. See [H44 § Claim → Loss spec correction landed 2026-05-20](../hypothesis/H44-T_A1b-cross-domain-transfer.md#claim).

### Collapse prevention is the BYOL triad — but key ablations are absent

**Paper §3.1, verbatim:**

> "The use of an exponential-moving average feature extractor along with a stop-gradient and a predictor has been used as a collapse prevention strategy for image pretraining (Grill et al., 2020), and studied empirically (Xie et al., 2021) and theoretically (Tian et al., 2021)."

The theoretical sketch is that if the predictor is near-optimal under L1, the encoder's gradient is `∇_θ MAD(Y | E_θ(x))`, so the encoder must capture maximum information about the input to minimise the deviation of the target. The EMA encoder evolving slowly than the predictor is the claimed mechanism for keeping the predictor near-optimal and thus the encoder under pressure to encode informative features.

**Confirmation that collapse did not occur is indirect**: downstream-task numbers (§5) and qualitative reconstructions via a separately trained diffusion decoder (§6, Figure 6) which suggest the features carry object-permanence and positional uncertainty information.

**Absent from the paper:**
- No stop-gradient ablation.
- No EMA-τ schedule ablation (only the linear 0.998 → 1.0 schedule is reported).
- No direct collapse measurement (no representation-variance, effective-rank, or anisotropy metric).
- No comparison to a contrastive (InfoNCE) baseline.

**Our restatement:** `[ASSERTED]` The collapse-prevention machinery is asserted by design, theoretically motivated, and validated by downstream performance. The mechanism's *necessity* (stop-grad essential? EMA τ near 1.0 essential?) is *not* empirically isolated. For H44 we adopt the triad as a unit; if H44 fails, attribution to specific machinery elements requires separate ablations we'd have to run ourselves.

### EMA target encoder uses a slow linear schedule

**Paper §10, verbatim:**

> "The y-encoder weights are initialized identically to the x-encoder, and subsequently updated as an exponential moving average (EMA) of the x-encoder weights using a momentum value which starts at 0.998 and is linearly increased to 1.0 during training."

τ start 0.998 → end 1.0, linear ramp. Table 8 confirms identical schedule across all three model sizes. The schedule is computed assuming a fictional 112,500-iteration horizon but training stops at 90,000 — i.e. the *last 20%* of the schedule never runs, and the effective endpoint is around τ ≈ 0.9996.

**Our restatement:** `[ASSERTED]` EMA τ in the 0.998–1.0 range is V-JEPA's default. The 2026-05-18 experiment spec for H44 listed τ ∈ {0.99, 0.996} — meaningfully *faster* than V-JEPA. We update the default to V-JEPA's range to minimise unjustified deviation. See `update` flag on [2026-05-18-T_A1b-isolation-derisk § Architecture](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md#method).

### The predictor is a narrow bottleneck

**Paper §3.3, verbatim:**

> "the predictor is a narrow transformer implemented using 12 blocks with an embedding dimension of 384"

Encoder backbone is ViT-H/16 at embedding dim 1280 (or ViT-L/16 at 1024). **The predictor is 3-4× narrower than the encoder.** Head count is inherited from the backbone (§10). The predictor takes encoder outputs plus *learnable mask tokens* (shared learnable vector + 3D sin-cos positional embedding) and outputs a d-dim vector per masked-token position.

**No ablation on predictor width or depth.** The 12/384 spec is fixed across all three model sizes.

**Our restatement:** `[ASSERTED]` The predictor-as-bottleneck is a deliberate (if unablated) design choice. Information-theoretically, a narrow predictor forces the prediction to compress, which plausibly contributes to the encoder learning *predictable* (i.e. structured) representations. We adopt narrow-predictor as default for H44, even though our event-rep dimensionality and predictor scale will be much smaller than V-JEPA's absolute numbers — the *ratio* of predictor-to-encoder width is the load-bearing design choice to preserve.

### Masking is multi-block at ~90% ratio, **per video** not per frame

**Paper §3.2, verbatim:**

> "To sample y from a video, we sample several (possibly overlapping) spatially continuous blocks with various aspect ratios and repeat the spatial blocks across the entire temporal dimension of the video; x is taken to be the complement."

Two masks per clip (short-range covering 15% per frame × 8 blocks; long-range covering 70% × 2 blocks), each repeated across the full 16-frame temporal extent — effectively masking spatio-temporal *tubes*, not random patches. Average mask ratio ~90%. The y-encoder forward pass is shared across both masks for efficiency (§9).

**Ablation (Table 4 / Figure 8):** multi-block masking beats random-tube[0.9] by 21 pp (K400 51.5 → 72.9). Two masks per clip beat one. ~90% spatial + 100% temporal is the empirical sweet spot.

**Our restatement:** `[ASSERTED]` The masking design encodes a *spatial-temporal locality prior* — blocks span time fully, so prediction is across-space-given-time. This translates non-trivially to event-segmented text, where there is no spatial dimension and events are far sparser than video patches. For H44, the natural analog is "mask N consecutive events, predict from surrounding events" or "mask spans within events" — both are design choices we owe an explicit pre-registration on. See [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) for the open design decision.

### Training scale

**Paper §3.4 + §10:**

- **Pretraining data**: VideoMix2M = HowTo100M ∪ K710 ∪ SSv2, ~2M videos (validation-set overlap removed).
- **Iterations**: 90,000.
- **Batch size**: 3072 (ViT-L/H/16 at 224) or 2400 (ViT-H/16_384).
- **Samples seen**: 270M (Table 15). *"obtained while processing an order of magnitude fewer samples than previous methods, and notably two orders of magnitude fewer samples than OpenCLIP"* (§12.3).
- **Optimiser**: AdamW; LR linear-warmup 2e-4 → 6.25e-4 over 12K iters, cosine-decay to 1e-6; WD ramp 0.04 → 0.4.
- **Hardware**: A100 80G, bfloat16. **No absolute GPU-hours reported**; Figure 5 reports ~2× wallclock speedup vs VideoMAE.

**Our restatement:** `[ASSERTED]` V-JEPA at ViT-H/16 is a multi-A100-month operation. H44's isolation de-risk targets ~1 GPU, weeks. **The scale gap is ~3 orders of magnitude.** A negative H44 result is consistent with "the bet fails" *or* "the bet needs scale we didn't give it" — pre-registered ablations and the cross-domain-vs-token-averaged-baseline framing are designed to detect "structure forming at all" rather than "structure forming at competitive quality," so the scale gap is hopefully cushioned but not eliminated.

### Downstream evaluation is recognition, not structural transfer

**Tasks evaluated** (Table 6, headline ViT-H/16):

| Task | V-JEPA frozen-probe | What it measures |
|---|---|---|
| Kinetics-400 | 82.0 | Action recognition (appearance-heavy) |
| Something-Something-v2 | 71.4 | Motion/temporal action |
| AVA | 25.8 mAP | Action localisation |
| ImageNet-1K | 75.9 | Object recognition |
| Places205 | 61.7 | Scene recognition |
| iNat21 | 67.9 | Fine-grained object recognition |

**Frozen-backbone attentive probing** is the headline protocol (§4.3): a learnable cross-attention layer with a query token, residual + MLP + LayerNorm + linear classifier. Linear (average-pooled) probing is reported only in ablations (Table 12, 13) and is **markedly worse** — for ViT-L/16, the gap is +17 pp on K400 and +16 pp on SSv2 (Table 3). This means the headline numbers rely on a trained pooling layer; the underlying features are not linearly separable to the same degree.

**Absent**: no analogy task, no compositional generalisation, no abstract-pattern benchmark, no cross-modality transfer (text, audio, multimodal), no out-of-distribution structural transfer.

**Our restatement:** `[ASSERTED]` V-JEPA demonstrates **within-modality recognition transfer**. H44 bets on **cross-domain structural transfer** — a property V-JEPA *does not test*. The cross-modality + cross-task-type leap is the load-bearing extrapolation in H44 and the primary reason this is a T4-tier bet, not T3. The 2026-05-18 ingest of H44 phrased this as "V-JEPA representations transfer to downstream structural tasks" — that wording was an overstatement and has been corrected (see [H44 § Evidence for](../hypothesis/H44-T_A1b-cross-domain-transfer.md#evidence-for)).

### What V-JEPA explicitly does *not* claim

- **No cross-modality experiment.** §2 references that data2vec (Baevski et al. 2022b) achieves competitive fine-tuning in image/audio/text — but V-JEPA itself runs no text or audio experiment and makes no quantitative claim about cross-modal transfer.
- **No structural / analogical / compositional benchmark.** All downstream tasks are recognition or localisation.
- **No Limitations or Broader Impacts section.** The closest acknowledgement is §5.2: *"we hypothesize that the datasets used to train V-JEPA and other video models are too constrained and lack the visual diversity of the internet-scale pretraining data used by the images models"* — a data-coverage concession, not a methodological one.
- **Loses to image-only models on appearance-heavy tasks.** DINOv2 ViT-g/14 beats V-JEPA H/16 on K400 frozen-probe (83.4 vs 82.0), ImageNet (86.2 vs 75.9), Places205, iNat21.
- **Loses to MVD on K400 fine-tuning** (87.2 vs 86.6). V-JEPA's claimed edge is *frozen-probe* performance, not full fine-tuning.

### Ablations actually present

- Pixel-vs-feature target (Table 1): feature targets win consistently (+5 pp K400 frozen).
- Pretraining data composition (Table 2): monotonic gains with more data.
- Masking strategy (Table 4 + Figure 8): multi-block beats random-tube, two masks beat one, ~90% ratio is sweet spot.
- Pooling strategy (Tables 3, 12, 13): attentive probe beats linear probe by ~15-17 pp.
- Low-shot label efficiency (Table 7): V-JEPA's gap to VideoMAE widens at 5%-of-labels regime.

### Absent ablations (matters for H44 design space)

- No predictor depth/width ablation.
- No EMA τ ablation.
- No stop-gradient ablation.
- No batch-size ablation.
- No L1-vs-L2-vs-cosine-vs-other-loss ablation (only the implicit "L1 was more stable" comment).
- No contrastive baseline using their backbone.
- **No randomly-initialised / no-pretrain control** (a "is the trained encoder doing anything?" baseline).
- No predictor-target-layer ablation (whether targets from intermediate y-encoder layers would change downstream signal).

## Relevance to Kyrja

- **[H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md)** — frontier-anchor for the loss family. Loss form correction (cosine → L1), evidence-for honest narrowing, ablation-gap disclosure all flow from this page.
- **[2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)** — design defaults inherited: narrow predictor (preserve ratio), EMA τ start 0.998 → 1.0 linear ramp, L1 in feature space, no normalisation on targets, per-token targets, stop-gradient. Deliberate deviations to pre-register: masking strategy (no native temporal-tube analog for events), training scale (~3 orders of magnitude smaller), per-token-vs-per-event target granularity.
- **[caddy-architecture](../concept/caddy-architecture.md)** — op T_A1 (the load-bearing T4) draws on V-JEPA as the precedent for "auxiliary feature-prediction loss with collapse-prevention triad at scale."
- **[caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md)** — V-JEPA scale (270M samples, multi-A100-month) is the cost-leg disadvantage of caddy: research-prototype scale we can afford ≈ 1000× smaller than the frontier anchor, so cross-modality extrapolation has to do disproportionate scientific work.

## Open questions raised by this read

- **Does V-JEPA's narrow predictor design extend to event-rep scale?** V-JEPA's predictor is 3-4× narrower than encoder; we adopt the ratio. But our encoder will be a small projection on top of a frozen base-LLM layer — the absolute dimensions are far smaller, and "narrow" might bottom out where information capacity is too small to predict at all. Pre-implementation design check needed.
- **Per-token vs per-event prediction target.** V-JEPA predicts per-patch-position. Our natural unit is per-event. If we predict per-event reps, we're predicting *one vector per event* vs V-JEPA's many-vectors-per-clip — the per-prediction information density is much higher in our setting. May want to break events into sub-units and predict per-sub-unit (closer to V-JEPA shape) to preserve the inductive bias.
- **Masking analog.** V-JEPA's spatio-temporal tubes don't map cleanly. Plausible options: (a) mask N consecutive events, predict from surrounding events; (b) mask spans of tokens within events; (c) mix. Pre-register before training.
- **What's the equivalent of V-JEPA's diffusion-decoder visualisation for sanity-checking that our reps aren't collapsed?** V-JEPA used a separately trained pixel decoder to confirm the features carry information. We need an analogous probe for event reps — possibly a small generative model conditioned on a rep that produces a paraphrase or near-event-completion.
