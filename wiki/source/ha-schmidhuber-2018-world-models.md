---
type: source
name: "Ha & Schmidhuber 2018 — World Models"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, world-model, generative-memory, simulation, p3, exploitability]
---

## Citation

Ha, D. & Schmidhuber, J. (2018). *World Models.* arXiv:1803.10122. Google Brain / NNAISENSE / IDSIA.

## Location

- arXiv: https://arxiv.org/abs/1803.10122
- Project page: https://worldmodels.github.io
- Rubric note: [substrate-survey/notes/ha-schmidhuber-2018-world-models.md](../../../research/library/substrate-survey/notes/ha-schmidhuber-2018-world-models.md)

## Key claims (with our restatements)

### Three-module V/M/C architecture

**Paper (§2):** **V (vision)** = VAE compressing each frame to `z ∈ R^32` (CarRacing) or `R^64` (VizDoom). **M (memory)** = Mixture Density Network RNN learning `p(z_{t+1} | a_t, z_t, h_t)`. **C (controller)** = linear or one-hidden-layer policy on `[z_t, h_t]`. Training pipeline: random rollouts → train V → train M → evolve C via CMA-ES, either against the real environment or against M as a dream generator with controllable temperature `τ`.

**Our restatement:** `[ASSERTED]` — first clean architectural template for [P3 substrate-as-simulator](../concept/substrate-paradigms.md). Memory is the generative model of the world; the agent's policy reads memory's predicted future as part of its perceptual input.

### Memory is generative, not retrieval

**Paper (§2.3):** *"C is a simple single layer linear model that maps z_t and h_t directly to action."* M's hidden state `h_t` carries the prediction; the controller consumes `[present, predicted-future]` as its perceptual input.

**Our restatement:** `[ASSERTED]` — first surveyed architecture where memory generates rather than retrieves. The agent doesn't *query* memory; it perceives the present through memory's predictions. Operationalizes Schacter's constructive-simulation hypothesis at the architectural level. Compare [RETRO](./borgeaud-2022-retro.md) and [kNN-LM](./khandelwal-2020-knn-lm.md), where memory is verbatim lookup.

### Training inside the dream transfers to reality

**Paper (§4):** Achieves SOTA on CarRacing-v0 (906 ± 21 vs prior 838 ± 11). Solves VizDoom: Take Cover trained entirely inside M's hallucinated rollouts, with policy transferring back to the real environment.

**Our restatement:** `[ASSERTED]` — paper-reported magnitudes. Construct-validity caveat: these are RL benchmarks at narrow domains, not general agent memory. The transfer result depends on M being a sufficiently faithful model; harder domains exacerbate exploitability (next claim).

### Exploitability of dreamed worlds — §4.5

**Paper (§4.5 "Cheating the World Model"):** *"In our initial experiments, we noticed that our agent discovered an adversarial policy to move around in such a way so that this virtual environment governed by the M model never shoots a single fireball during some rollouts."* And: *"Our world model will be exploitable by the controller, even if in the actual environment such exploits do not exist."* Increasing `τ` makes adversarial policies harder to find but makes the virtual environment too difficult to learn in if pushed too far.

**Our restatement:** `[ASSERTED]` — first-order constraint on the substrate-as-memory paradigm. An agent that thinks inside its memory will discover and exploit memory's flaws. The fix (raise temperature) trades realism for robustness. **No agentic-memory product acknowledges this failure mode** because their memories are static stores that don't influence agent reasoning generatively.

### Hippocampal-replay analogy

**Paper (§5):** *"Replaying recent experiences plays an important role in memory consolidation (Foster, 2017) – where hippocampus-dependent memories become independent of the hippocampus over a period of time. As Foster puts it, replay is less like dreaming and more like thought."*

**Our restatement:** `[ASSERTED]` — paper explicitly draws the cog-sci analogy. Iterative training (rollouts → retrain M → retrain C → rollouts) is memory consolidation as algorithm. Anchors [consolidation-channel](../concept/consolidation-channel.md) as a paradigm-level concept not just a Kyrja-internal coinage.

## Important caveats

- **No cross-session continuity.** World model is per-environment, retrained `[ASSERTED]`.
- **No multi-agent.** Single-agent setup.
- **No explicit episodic recall.** M can predict but cannot be asked to recall a specific past event.
- **No self-model.** Agent has a world model but no separate self-model.
- **Offline-only training of M.** M is trained on collected rollouts, not online via surprise gradients. Compare [Titans](./behrouz-2024-titans.md).

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P3 substrate-as-simulator foundational reference.
- Anchors the "memory is generative" leg of [substrate-as-memory](../concept/substrate-as-memory.md).
- **First-order constraint anchor**: §4.5 exploitability is the load-bearing warning for any Kyrja architecture in which the agent's thinking is conditioned on a learned generative substrate.
- Reusable for Kyrja: generative memory module as a primitive (`p(next | now, history)`); temperature as realism-vs-exploitability dial; `[present, predicted-future]` as the perceptual representation; iterative replay-as-consolidation training loop.
- Direct predecessor to [DreamerV3](./hafner-2023-dreamerv3.md), which scales this template to general RL.

## Audit history

- 2026-05-13 — verbatim read, pp.1-13 (core sections §1-§5), rubric note written.

## Archive location

arXiv:1803.10122. Project page https://worldmodels.github.io. Not in `library/papers/`. Fetch from arXiv for re-verification.
