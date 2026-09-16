---
type: source
name: "Hafner, Pasukonis, Ba & Lillicrap 2023 — DreamerV3: Mastering Diverse Domains through World Models"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, world-model, simulation, p3, nature-2025, guidepost]
---

## Citation

Hafner, D., Pasukonis, J., Ba, J. & Lillicrap, T. (2023). *Mastering Diverse Domains through World Models.* arXiv:2301.04104 (v4 Apr 2024). Google DeepMind / University of Toronto. **Published in Nature 2025 as "Mastering diverse control tasks through world models."**

## Location

- arXiv: https://arxiv.org/abs/2301.04104
- Nature 2025: https://www.nature.com/articles/s41586-025-08744-2 (Hafner et al. 2025)
- Rubric note: [substrate-survey/notes/hafner-2023-dreamerv3.md](../../../research/library/substrate-survey/notes/hafner-2023-dreamerv3.md)

## Key claims (with our restatements)

### Single algorithm, fixed hyperparameters, 150+ tasks

**Paper (§4):** DreamerV3 with a single fixed hyperparameter configuration achieves SOTA across 150+ tasks spanning Atari, ProcGen, DMLab, Minecraft, BSuite, and continuous-control benchmarks. First algorithm to **mine diamonds in Minecraft from scratch** — no human data, no curricula.

**Our restatement:** `[ASSERTED]` — paper-reported magnitudes. Construct-validity caveat: cross-domain generalization is on RL benchmarks; the leap to dialogue / personal-assistant substrates is non-trivial since dialogue lacks dense reward and pixel-style reconstruction objectives.

### RSSM architecture with discrete categorical latents

**Paper (§2):** World model state `s_t = {h_t, z_t}`. `h_t` is a deterministic recurrent state; `z_t` is a **discrete stochastic latent** (categorical, sampled via straight-through gradients). Components: sequence model `h_t = f_φ(h_{t-1}, z_{t-1}, a_{t-1})`; encoder `z_t ~ q_φ(z_t | h_t, x_t)`; dynamics predictor `ẑ_t ~ p_φ(ẑ_t | h_t)`; decoder + reward predictor + continue predictor. Actor and critic train entirely on imagined trajectories of horizon `T=16`.

**Our restatement:** `[ASSERTED]` — discrete categorical latents are **token-shaped**, making the world-model substrate structurally compatible with the LM input space. Compared to [Ha & Schmidhuber 2018](./ha-schmidhuber-2018-world-models.md)'s continuous Gaussian latents, this is the move toward LM-compatibility.

### World model is the dominant learning signal — Fig 6b

**Paper (Fig 6b ablations):** With both signals → 100%; without reward/value gradients → ~85%; **without reconstruction gradient → ~20%.** Paper text: *"Dreamer rests predominantly on the unsupervised reconstruction loss of its world model, unlike most prior algorithms that rely predominantly on reward and value prediction gradients."*

**Our restatement:** `[ASSERTED]` — the substrate is doing 4-5× more learning than the task-specific reward signal. **Strongest existing architectural evidence for the [substrate-as-memory](../concept/substrate-as-memory.md) thesis**: when both signals are available, the substrate dominates. Construct-validity caveat: measured in dense-reward RL environments; the 4-5× ratio may not transfer to dialogue.

### Exploitability addressed via regularization

**Paper (§3 robustness tricks):** Discrete latents reduce smooth exploitable trajectories; **1%-uniform mixing** of categorical predictions prevents determinism; **KL balance + free bits** (clip KL below 1 nat ≈ 1.44 bits) force the world model to remain stochastic; **short imagination horizon T=16** limits how far the agent can plan into hallucinated futures.

**Our restatement:** `[ASSERTED]` — these reduce but do not eliminate the exploitability failure mode described in [Ha & Schmidhuber 2018 §4.5](./ha-schmidhuber-2018-world-models.md). The lesson: substrate-as-memory needs explicit regularization to prevent the agent from cheating its own memory.

### Cross-domain stability tricks

**Paper:** Symlog input transformation; return normalization to 5th-95th percentile range; categorical bin prediction with symexp twohot loss.

**Our restatement:** `[ASSERTED]` — general-purpose techniques. The symexp-twohot categorical-bin-prediction technique is reusable for any quantity an agent reasons about (timestamps, importance scores) rather than scalar regression.

## Important caveats

- **Per-environment training.** Despite fixed hyperparameters across 150+ tasks, a *separate* world model is trained per environment. No cross-task memory transfer `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **Imagination horizon is short.** `T=16`. For agent memory where conversations span hundreds of turns, this is insufficient. R2I (Samsami 2024, ICLR) integrates SSMs into Dreamer to fix this and is the direct successor for substrate-as-memory.
- **Replay buffer is verbatim and external.** Substrate (world model) is lossy/learned; buffer outside is lossless/accumulating. Mirrors the kNN-LM split.
- **No self-model dimension.** Models environment, not agent.
- **Active critique** `[ASSERTED]`: Biased Dreams (2026) — epistemic uncertainty quantification fails in latent-space models; TRAP (2026) — adversarial attacks against world-model planning; Hamiltonian World Models (2026) — current latent world models physically un-grounded. Critiques target specific limitations, not the paradigm.

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P3 substrate-as-simulator domain-general empirical proof point.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md) — Fig 6b is the strongest architectural evidence that "substrate does most of the learning" empirically.
- Anchors [consolidation-channel](../concept/consolidation-channel.md) — imagination + replay loop is consolidation as algorithm.
- **Nature 2025 publication is the strongest single peer-review credential in the substrate survey.** Legitimizes the world-model paradigm beyond what an arXiv-only paper could.
- Reusable for Kyrja: RSSM-style `(deterministic + stochastic-discrete)` state split; free-bits + KL balance to prevent over-confidence; categorical bin prediction with symexp twohot; world-model-dominant learning principle.
- R2I (Samsami 2024, ICLR) is the substrate-survey's queued direct follow-up — Mamba/SSM inside Dreamer for memory tasks. Deferred per [phase1-temperature-checks](../../../research/library/substrate-survey/phase1-temperature-checks.md).

## Audit history

- 2026-05-13 — verbatim read, pp.1-10 (core sections §1-§4 + Fig 6 ablations), rubric note written with field-temperature memo.

## Archive location

arXiv:2301.04104. Nature 2025 reprint at the Nature DOI. Not in `library/papers/`. Fetch from arXiv or Nature for re-verification.
