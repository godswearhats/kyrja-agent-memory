---
type: source
name: "LeCun 2022 — A Path Towards Autonomous Machine Intelligence"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, world-model, jepa, h-jepa, p3, position-paper, guidepost]
---

## Citation

LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence (Version 0.9.2).* OpenReview. Meta FAIR / NYU.

## Location

- OpenReview: https://openreview.net/forum?id=BZ5a1r-kVsf
- Rubric note: [substrate-survey/notes/lecun-2022-autonomous-mi.md](../../../research/library/substrate-survey/notes/lecun-2022-autonomous-mi.md)

## Key claims (with our restatements)

### Six-module cognitive architecture

**Paper:** Six modules: **Configurator** (executive control), **Perception** (encodes percept `x → s`), **World Model** (predicts `s_{t+1}` from `s_t + a_t`, with latent `z` for uncertainty), **Cost** (intrinsic immutable + trainable critic), **Short-term Memory** (key-value associative store; Miller et al. 2016 Memory Networks lineage), **Actor** (produces action sequences). Mode-1 = reactive; Mode-2 = deliberative gradient descent through the world model.

**Our restatement:** `[ASSERTED]` — the most complete theoretical substrate architecture for [P3 substrate-as-simulator](../concept/substrate-paradigms.md). Memory and reasoning are unified: Mode-2 reasoning *is* rolling out the world-model substrate.

### JEPA — predict in representation space, not observation space

**Paper (§4):** Two encoders (`Enc_x` for past/current, `Enc_y` for target/future), a predictor `Pred(s_x, z) → s̃_y`, and a distance `D(s_y, s̃_y)`. Trained non-contrastively via VICReg/Barlow Twins-style losses. Paper: *"we advocate against the use of generative architectures"* because generative models must reproduce unpredictable details and waste capacity on them. *"A JEPA will learn abstract representations that make the world predictable. Unpredictable details will be eliminated by the invariance properties of the encoder."*

**Our restatement:** `[ASSERTED]` — strongest commitment to lossiness in any architecture surveyed. For agent memory: predict the user's intent in representation space, not the user's exact next utterance. None of the [agentic memory products](../incumbent/index.md) do this.

### H-JEPA — hierarchical world models

**Paper (§4.6):** H-JEPA stacks JEPAs at multiple time scales. The "drive to the train station" example: top level plans trajectory ("go to station"), middle level plans subgoals ("stand up, leave house, drive"), bottom level plans muscle commands.

**Our restatement:** `[ASSERTED]` — multi-timescale prediction. For agent memory: predict next user turn (seconds), next user goal change (minutes), next session theme (days). Architectural fix for the agentic field's single-timescale designs.

### Ego-model + world-model split

**Paper (§4.8.1):** *"the agent itself is somewhat more predictable... This suggests that the agent should possess a separate model of itself."*

**Our restatement:** `[ASSERTED]` — first surveyed architecture making explicit room for a self-model. Reusable as a template for modeling *other* agents (multi-agent). Agentic-memory products have zero self-model; LeCun's framework names this gap.

### Short-term key-value memory module

**Paper (§4.9):** *"The state of the world should be maintained in some sort of writable memory... A conventional key-value associative memory can be used for this purpose, similar to what has been proposed in the context of memory-augmented networks (Bordes et al., 2015; Sukhbaatar et al., 2015; Miller et al., 2016)."* Bottle-in-kitchen-then-dining-room example illustrates entity-state tracking.

**Our restatement:** `[ASSERTED]` — LeCun's architecture inherits from the [NTM](./graves-2014-ntm.md) lineage but uses it for world-state tracking rather than algorithm computation. The missing entity-state primitive in every agentic-memory product surveyed.

### Mode-1 / Mode-2 = System 1 / System 2

**Paper:** Direct Kahneman framing. Most decisions are reactive policy lookup (Mode-1); only specific decisions invoke the deliberative loop through the world model (Mode-2).

**Our restatement:** `[ASSERTED]` — for agentic-memory products: most queries should NOT trigger RAG; only specific queries should. Current systems are universally Mode-2 (RAG + LLM for every utterance), which LeCun's framing implies is wasteful.

## Important caveats

- **Position paper, not empirical.** No experiments, baselines, or benchmarks `[ASSERTED]`. The proposed architecture has not been built as a whole; components (JEPA, VICReg, H-JEPA) have partial implementations in I-JEPA, V-JEPA, V-JEPA 2, LLM-JEPA, A-JEPA, MC-JEPA. No integrated agent.
- **OpenReview, not peer-reviewed venue.** Authority comes from author pedigree + subsequent empirical instantiation, not venue review.
- **Anti-generative hard-line is softening.** N-JEPA (2025) integrates diffusion noise; [DreamerV3](./hafner-2023-dreamerv3.md) wins empirically while being generative. Treat "must be non-generative" as a hypothesis under test, not a settled principle `[ASSERTED]`.
- **Cross-session continuity and multi-tenant agent contexts not addressed.** Every JEPA instantiation is single-sequence or single-environment `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **Active critique.** Hamiltonian World Models (Cui & Ma 2026) argues for physics-structured alternative; "Predictive but Not Plannable" (2026) targets planning limits of latent world models. Critique is hybridization, not refutation.

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P3 substrate-as-simulator *theoretical* reference — the most complete substrate architecture in the literature.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md) — the framework whose 7 constraints the agentic memory field violates on 5+.
- Anchors [H29-edge-substrate-memory](../hypothesis/H29-edge-substrate-memory.md) — LeCun's program is at FAIR, a vertical-integrator-adjacent lab.
- Anchors [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md) — the latent-space interface is precisely the kind of substrate-level memory mechanism H37 hypothesizes about.
- Reusable for Kyrja: prediction-in-representation-space framing; H-JEPA multi-timescale prediction; ego-model + world-model split; KV entity-state memory; Mode-1/Mode-2 routing; non-contrastive substrate training (VICReg, Barlow Twins).
- **FAIR follow-up trajectory (load-bearing)**: I-JEPA (Assran et al. 2023, 783c/92i), V-JEPA (Bardes et al. 2024), V-JEPA 2 (Assran/Bardes/...LeCun et al. 2025, 326c/40i; zero-shot real-robot planning on Franka arms at 8B params over 1M+ hours of video), LLM-JEPA (Huang/LeCun/Balestriero 2025).

## Audit history

- 2026-05-13 — verbatim read, pp.1-40 (covering core architecture §1-§4, JEPA §4, H-JEPA §4.6, short-term memory §4.9), rubric note written with field-temperature memo.

## Archive location

OpenReview Version 0.9.2. Not in `library/papers/`. Fetch from OpenReview for re-verification.
