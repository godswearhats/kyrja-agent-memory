---
type: source
name: "Behrouz, Razaviyayn, Zhong & Mirrokni 2026 — Nested Learning: The Illusion of Deep Learning Architectures"
status: timeless
last_ingested: 2026-05-14
sources: []
tags: [substrate-memory, nested-learning, hope, titans-descendant, optimizers-as-memory, continuum-memory, consolidation-channel, online-consolidation, p1-substrate-as-state, neurips-2025]
---

## Citation

Behrouz, A., Razaviyayn, M., Zhong, P. & Mirrokni, V. (2026). *Nested Learning: The Illusion of Deep Learning Architectures.* arXiv:2512.24695. Google Research (with Razaviyayn at Google Research; Zhong at Columbia University). Published at NeurIPS 2025.

## Location

- arXiv: https://arxiv.org/abs/2512.24695
- Read in full 2026-05-14 via subagent verbatim slicing; full text archived at `mcp-arxiv-download_paper-1778715548056.txt` (244,398 chars).

## Key claims (with our restatements)

### Definitional move — Nested Learning paradigm

**Paper (§3.2, Definition 3):** *"A (ordered) nested system is a system with K (ordered) levels such that each level k, 1 ≤ k ≤ K, consists of a set of optimization problems {(L_i^(k), C_i^(k), Θ_i^(k))}_{i=1}^{N_k}, where L_i(·;·) is the optimization objective in the i-th problem, C_i is its context (the data that is optimized on), Θ_i is the feasible set of its parameters, and each parameter is optimized using gradient descent."* Ordering is by update frequency (Def 2): "f_A as its number of updates per unit of time." Generalised forms (Appendix A, Defs 6-7) drop the gradient-descent restriction.

**Our restatement:** `[ASSERTED]` The NL formalism re-frames a neural model as a *stack of optimization problems*, each with its own "context flow" (the data the box is optimised on). Existing architectures fall out as instances: a Transformer block, an SSM, a momentum buffer, and an MLP layer are all instances of Nested Sequence Associative Memory (NSAM, Def 4). This is a unifying re-description, not an architectural innovation in itself.

### Optimizers are associative memory modules

**Paper (§4.1, Eq 30-31):** For a deep MLP, per-layer GD step *"Ŵ_ℓ ← W_ℓ − η · δ_ℓ · x̂_{ℓ−1}^⊤"* is reformulated as *"an associative memory module that aim to map the input of each layer x̂_{ℓ−1} to its local error signal, δ_ℓ."* Section 4.2 (Eq 33-34) gives momentum as inner-loop GD on `m·∇L(W_i; x_i)`. Adam, AdaGrad, RMSProp, Lion, NAdam, AMSGrad, RAdam, SignSGD, Shampoo, SOAP all derive (Appendix B, Eqs 101-103) by varying the inner-loop objective. Muon's Newton-Schulz operator is reframed (Eq 43-44) as a 3-degree polynomial GD step on an orthogonalisation objective.

**Our restatement:** `[ASSERTED]` This is the paper's most cross-cutting theoretical claim: any gradient-based optimizer is an associative-memory module that *compresses gradients into a preconditioner-shaped statistic*. The construct is rigorous (closed-form solutions verified in Appendix B). For Kyrja, it sharpens the [active-stages framework](../concept/active-stages-framework.md) framing of *consolidation as a learned compressor*: the same machinery used to compress gradients can compress trajectories, which is what a consolidation channel does. We do not adopt the deeper-optimizer artefact (M3, see §7.2) — it is acknowledged in §7.2 as a "proof-of-concept" with computational overhead at scale.

### Self-modifying learning module (deep self-referential Titans)

**Paper (§8.1, Eq 86):** *"k_t = M_k(x_t), η_t = M_η(x_t), α_t = M_α(x_t), v_t = M_v(x_t)"* with memory update *"M_memory ← M_memory − η_t · ∇_M L(M_memory; k_t, v_t) + α_t·(weight decay)"* — the keys, values, learning-rate, and forget-gate are themselves outputs of meta-learned associative-memory sub-modules, not static projections of x_t. Only the query q_t = x_t W_q remains a fixed projection. Initial states M_□,0 are meta-learned across all sequences (outer level). Optimisation uses Delta Gradient Descent (Def 5, §4.5) because tokens are dependent samples. Each memory M_□ is a 2-layer MLP.

**Our restatement:** `[ASSERTED]` The self-modifying construction makes the inner-loop update rule itself parametric and learnable. This is the paper's strongest novelty over Titans (Behrouz et al. 2024). For Kyrja, it lands at **substrate-depth ladder rung 2-3 *but ephemeral*** — verbatim §6: *"test-time training and test-time memorization are in fact instances of parametric in-context learning, where the acquired in-context knowledge does not persist once the current context is removed."* Inference-time weight modifications are wiped when the context window rolls. This is structurally different from EvoSC-style soft-prompt persistence and from MEMIT-style targeted edits — it is *transient* parametric memory.

### Continuum Memory System (CMS)

**Paper (§7.1, Eq 71):** *"the parameters of ℓ-th MLP block, i.e., θ^(f_ℓ), are updated every C^(ℓ) steps"* — a chain of MLP blocks each updated at a different frequency, where C^(ℓ) is the chunk size at level ℓ. *"The conventional Transformer block (Vaswani et al. 2017) is a special instance of this formulation, where k = 1 and frequency of update is zero."* Three variants: **Nested CMS** (Eq 72; higher level meta-learns initial state of next), **Sequential CMS** (Eq 73; chained input/output, lowest-frequency level absorbs gradient), **Independent / Head-wise CMS** (Eq 74; parallel blocks with Agg(·)).

The forgetting-mitigation argument (verbatim, §7.1): *"when updating an arbitrary block of MLP^(f_ℓ)(·) … the potentially forgotten knowledge from MLP^(f_ℓ)(·) is still stored in other components such as MLP^(f_ℓ')(·), where ℓ' < ℓ. … the knowledge transfer through backpropagation (for their initial state) can circle back the knowledge to MLP^(f_ℓ)(·), resulting in a loop through time dimension, and so hardly forgetting important knowledge."*

**Our restatement:** `[ASSERTED]` CMS is the *frequency-stratified substrate*: instead of a single hidden state or single MLP block, you have a chain operating at multiple update rates. The same architectural shape that exists in CLS biology (hippocampal fast write + neocortical slow consolidation) is realised as a continuum of frequencies, not a binary fast/slow split. This is the paper's most consequential idea for Kyrja's [consolidation-channel](../concept/consolidation-channel.md) design, because it shifts the question from "what depth on the ladder" to "what *frequency spectrum* of depths."

### Hope architecture

**Paper (§8.3, Eq 92):** *"Hope architecture: A neural learning module that incorporates self-modifying Titans followed by Continuum Memory System."* Forward pass: `y_t = CMS(SelfModTitans(x_t))`. L2-normalised q and k; local convolutions with window 4. Variant **Hope-Attention** replaces self-modifying Titans with softmax global attention.

Reported scales:
- §9.1 (continual learning): Llama-3-8B and Llama-3-3B backbones with §7.3 "ad-hoc level stacking" (MLP blocks reinitialised from pretrained weights into CMS levels), 15B-token continual pretraining.
- §9.2-9.4 (from scratch): 760M / 30B tokens and 1.3B / 100B tokens. AdamW optimiser. Vocab 32K. FineWeb-Edu mixture.
- §9.2 long context: ~50B tokens.

**Our restatement:** `[ASSERTED]` Hope is two stacked submodules with different operational depths — depth-2-ephemeral inner (self-mod Titans) plus depth-5-at-training-time outer (CMS). It is *not* a pluggable external store and *not* a P2-style differentiable read/write module. It belongs in the [substrate-paradigms](../concept/substrate-paradigms.md) **P1 substrate-as-state** family as a Titans descendant. The novelty over Titans is the frequency-stratified outer chain and the self-modifying inner-loop update rule. See §10 ("Is Catastrophic Forgetting Solved?") for the explicit caveat: *"the undesirable phenomenon of catastrophic forgetting is not 'solved' in general. From nested learning viewpoint … catastrophic forgetting is a natural consequence of compression."*

### In-context learning naturally emerges

**Paper (§6):** *"in-context learning is a model's capability that is transparent from its NL representation, and per se it is not an emergent characteristic but a direct consequence of having multiple levels in the NL representation of the neural learning module."* Also: *"Pre-training is In-Context Learning with Ultra-Large Context Length: From NL's viewpoint pre-training is only one of the possible instances of in-context learning, where the context is the entire pre-training data."*

**Our restatement:** `[ASSERTED]` as a *theoretical reframing*, `[SPECULATED]` as an *empirical claim about LLM emergence*. The paper does not run scaling-curve experiments demonstrating "more levels → ICL emerges in the Brown 2020 sense." Figure 7 and Table 8 show monotone gains with more levels, but those gains are on retrieval and translation, not on the canonical few-shot ICL benchmarks. The "naturally emerges" framing is stronger than the evidence supports.

### Empirical headline (language modelling + common sense)

**Paper (Table 2, 1.3B / 100B tokens):**

| Model | Wikitext ppl ↓ | LMB ppl ↓ | Avg acc ↑ |
|---|---|---|---|
| Transformer++ | 17.92 | 17.73 | 53.38 |
| Samba | 16.15 | 13.21 | 54.46 |
| Titans | 15.60 | 11.41 | 56.82 |
| **Hope** | **14.39** | **10.08** | **58.04** |

(760M / 30B-token row also shows Hope leading: 18.68 / 20.07 / 52.28 vs Titans 20.08 / 21.52 / 51.68.)

**Our restatement:** `[ASSERTED]` paper-reported. **Construct-validity caveat:** single-seed throughout, no confidence intervals, no significance tests, no error bars reported anywhere in §9. The Hope-vs-Titans deltas (1.21 ppl on Wikitext, 1.33 on LMB, 1.22 acc) are meaningful magnitudes but the paper provides no variance estimate. The metric is standard language-modelling perplexity / common-sense accuracy — measures what it claims to measure for *language modelling*, but does *not* directly measure agentic memory or consolidation quality. Treat as evidence Hope is competitive at language modelling, not as evidence for the consolidation-channel framing.

### Multi-key NIAH — the gap to attention

**Paper (Table 1, MK/MQ/MV-NIAH at 4K/8K/16K):**

| Model | MK-NIAH-1 | MQ-NIAH | MV-NIAH |
|---|---|---|---|
| Transformer | 79.4 / 83.0 / 61.4 | 58.9 / 48.0 / 29.8 | 37.5 / 34.1 / 21.5 |
| Hope-Attention | 80.2 / 84.8 / 60.8 | 60.4 / 47.8 / 30.6 | 35.2 / 34.4 / 24.8 |
| **Hope** | 29.4 / 24.8 / 14.8 | 31.7 / 24.8 / 14.2 | 31.4 / 17.2 / 11.4 |

**Our restatement:** `[ASSERTED]` paper-reported. **Construct-validity caveat — this is the load-bearing finding the paper minimises.** Hope (attention-free) loses to Transformer / Hope-Attention by very large margins (up to 4× at 16K). Hope-Attention wins these — but Hope-Attention is "Hope architecture with softmax attention swapped in," which means *the gains on these workloads come from CMS, not from self-modifying Titans*. The paper's headline framing ("Hope outperforms attention-free baselines") elides the gap to attention; the more accurate reading is that CMS-on-top-of-attention is the strongest variant and the self-modifying inner-loop's contribution to long-context retrieval is unclear.

## Important caveats

- **Stage-1 consolidation only.** Verbatim §1.1: *"in this work, we focus on the first stage: memory consolidation as an online process."* Stage-2 offline / replay consolidation (SWR-mediated, Yang et al. 2024) is acknowledged as crucial and then dropped. The implication for [consolidation-channel](../concept/consolidation-channel.md) design: Hope is the *gradient-coupled-online* half of CLS only. See [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md).
- **No statistical significance.** Single-seed numbers throughout §9 (Tables 1-8, Figures 6-12). No confidence intervals, no error bars, no seed counts, no significance tests. Construct-validity flag on every reported number.
- **Ablation Table 6 contradicts the "all components contribute" claim.** Removing the inner-projection q *improves* Wikitext ppl from 12.24 to 12.19 (accuracy drops 58.1 → 57.4). The paper text claims "All components of Hope are positively contributing to its performance" — Table 6's own data shows this is at best ambiguous for the q-projection.
- **Cartridges baseline explicitly excluded** (§9.1, "we exclude their comparison with Hope mainly due to … higher memory usage and … fundamental differences in their computational costs"). Cartridges is the most relevant memory-vs-memory baseline; the exclusion is defensible but leaves the strongest test of the CMS framing unrun.
- **BABILong "10M context" claim** is figure-only with no verbatim number in main text. Paper concedes (§9.2) *"the performance of all small models, including Hope, can drop significantly when used without fine-tuning"* — leaving open whether 10M is real long-context generalisation or BABILong-distribution memorisation.
- **Continual-learning experiments (§9.1) and from-scratch experiments (§9.2-9.4) use different "Hope"s.** §9.1 reuses Llama-3 backbone with CMS-style MLP scheduling; §9.2-9.4 trains Hope from scratch. The architecture name is shared; the trained model is not. Cite carefully.
- **M3 optimizer is "proof-of-concept" (§7.2)** with acknowledged scaling overhead. Do not adopt as a recommended optimiser based on the paper.
- **Self-modifying Titans is *transient* parametric memory.** §6: "the acquired in-context knowledge does not persist once the current context is removed." This is not the same shape as MEMIT, LoRA, or full FT — it does not survive context-window roll. Important for any Kyrja design that pulls inspiration from Hope.
- **Catastrophic forgetting not solved.** §10 verbatim: *"the undesirable phenomenon of catastrophic forgetting is not 'solved' in general. From nested learning viewpoint … catastrophic forgetting is a natural consequence of compression."* CMS's frequency-loop mechanism *mitigates* forgetting; it does not eliminate it.
- **In-context learning "emergence" claim is theoretical not empirical.** The paper deduces ICL from the multi-level structure; it does not run scaling experiments at multiple model sizes targeted at ICL emergence in the Brown 2020 sense.

## Relevance to Kyrja

- **Anchors [consolidation-channel](../concept/consolidation-channel.md).** Hope is the cleanest implementation to date of a CLS-grounded substrate-side mechanism: short-/long-term memory becomes a *frequency continuum*, not a binary tier. The substrate-depth ladder gains a second axis (frequency).
- **Anchors [substrate-paradigms](../concept/substrate-paradigms.md) P1.** Hope is a Titans descendant — substrate-as-state with frequency-stratified MLP chain. Strengthens the P1 family's claim that the entire sequence-modelling design space reduces to "what kind of learner is your hidden state."
- **Sharpens [active-stages-framework](../concept/active-stages-framework.md).** The "optimizers are associative memory" reframing supports the active-stages claim that consolidation is fundamentally *a learned compressor*. Hope addresses consolidation, forgetting, and updating; **curation remains unaddressed** — there is no analogue of CLS replay-selection at write time.
- **Names the online-vs-offline design fork.** Stage-1 vs stage-2 consolidation is now an explicit open question for Kyrja's wedge. See [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md).
- **Speaks to but does not resolve [H37 — pluggable substrate](../hypothesis/H37-pluggable-substrate.md).** §3.3 ("Connections with Generation") frames hypernetworks and optimizers as "one lower-frequency (resp. higher-frequency) block generates the weight of a higher-frequency (resp. lower-frequency) block" — the NL vocabulary supports a level-that-generates-an-interface (the H37 shape). The paper does not instantiate this. Vocabulary-friendly, not evidence.
- **Complements [Xu et al. 2026](./xu-2026-agentic-memo.md).** Xu names the consolidation channel architecturally and provides the CSC theorem. Behrouz et al. build *half* of the operator (online consolidation). The Skill-SD-style offline branch Xu also cites is *not* implemented here. The two papers together leave a clean fork.
- **Complements [EvoSC](./yu-2026-evosc.md).** EvoSC is at depth 2 (soft prompt) with online distillation. Hope is at depth 2-ephemeral inner + depth 5 outer with frequency stratification. Together they trace a partial map of the design space: EvoSC = shallow/persistent, Hope = mixed-depth/transient-inner + slow-outer.

## Substrate-depth ladder mapping

Hope occupies *multiple rungs simultaneously*, which is the first clean evidence that the [substrate-depth ladder](../concept/consolidation-channel.md#substrate-depth-ladder) needs a second (frequency) axis:

- **Self-modifying Titans (inner):** ladder rung 2-3 *but ephemeral*. Per-token DGD writes into a 2-layer MLP M_memory inside the forward pass; writes do not persist beyond the context.
- **CMS blocks (outer) at training time:** ladder rung 5. Real weight modification, gradient-driven, at low frequencies.
- **CMS blocks (outer) at frozen-inference:** ladder rung 0 / reduces to a fixed forward.

The architecturally interesting claim is that the *frequency* of update is itself a design parameter. Kyrja's depth ladder is currently one-dimensional (rung 0 → 5). Hope reveals (depth, frequency) as a 2D design space. See [consolidation-channel § Substrate-depth ladder](../concept/consolidation-channel.md#substrate-depth-ladder) for the integration.

## References worth tracking

CLS / hippocampus / consolidation:
- Frey & Morris 1997 — Synaptic tagging and LTP, *Nature*.
- Yang, Sun, Buzsáki et al. 2024 — Selection of experience for memory by hippocampal sharp wave ripples, *Science*. (Most relevant to the offline-consolidation branch.)
- Foster & Wilson 2006 — reverse replay, *Nature*.
- Diekelmann & Born 2010 — memory function of sleep.
- Staresina et al. 2015 — hierarchical nesting of oscillations / spindles / ripples, *Nature Neuroscience*.
- Kitamura et al. 2017; Roy et al. 2022 — distributed engrams.
- Gershman, Fiete & Irie 2025 — Key-value memory in the brain, *Neuron*.

Titans / TTT / self-referential family:
- Behrouz, Zhong & Mirrokni 2024 — [Titans](./behrouz-2024-titans.md).
- Behrouz et al. 2025c — Titans full version (NeurIPS 2025).
- Sun et al. 2024 — [TTT](./sun-2024-ttt.md).
- Schmidhuber 1992, 1993, 2003 — fast weight programmers, SRWM, Gödel machines.
- Irie, Schlag, Csordas, Schmidhuber 2022 — modern SRWM.
- Liu et al. 2024b — Longhorn (SSMs as amortised online learners).
- Wang, Shi & Fox 2025 — Test-time regression unifying framework.

Continual learning / soft prompts:
- Kirkpatrick et al. 2017 — EWC.
- Momeni, Mazumder, Ke & Liu 2025 — InCA.
- Eyuboglu et al. 2025 — Cartridges (explicitly-excluded baseline).
- Akyürek et al. 2024a — surprising effectiveness of TTT for few-shot.

Optimisers:
- Jordan et al. 2024 — Muon.
- Vyas et al. 2025 — SOAP.
- Si, Zhang & Shen 2025 — AdaMuon.
- Pagliardini, Ablin & Grangier 2025 — AdEMAMix.

## Audit history

- 2026-05-14 — verbatim read via subagent slicing of arXiv:2512.24695 (244,398 chars). Coverage: all equation blocks, §1.1 cog-sci motivation, §3 NL formalism, §4 optimisers-as-AM, §6 ICL framing, §7 CMS, §8 Hope, §9 experiments, §10 forgetting caveat, Appendix A generalised NL, Appendix B Adam derivation.

## Archive location

arXiv:2512.24695. Local cache at `mcp-arxiv-download_paper-1778715548056.txt` (transient; re-fetch from arXiv for re-verification).
