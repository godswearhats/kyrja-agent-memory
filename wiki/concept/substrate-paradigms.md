---
type: concept
name: Substrate paradigms (P1/P2/P3 taxonomy)
status: timeless
last_ingested: 2026-05-16
sources: [../source/gu-dao-2023-mamba.md, ../source/behrouz-2024-titans.md, ../source/sun-2024-ttt.md, ../source/graves-2014-ntm.md, ../source/borgeaud-2022-retro.md, ../source/khandelwal-2020-knn-lm.md, ../source/ha-schmidhuber-2018-world-models.md, ../source/hafner-2023-dreamerv3.md, ../source/lecun-2022-autonomous-mi.md, ../source/yu-2026-evosc.md, ../source/behrouz-2026-nested-learning.md, ../source/wayne-2018-merlin.md]
epistemic_tags: [asserted, speculated]
tags: [substrate-memory, taxonomy, paradigm]
program: kerros
---

> **Program: [Kerros](./kerros.md) (assigned 2026-05-25).** Part of the substrate-memory research program. "Kyrja" / "wedge" / "Phase-3" references below are product-era chronicle; the design space named here serves Kerros research, not a product roadmap.

## Definition

**Substrate paradigms** is the three-way taxonomy of architectures inside the [substrate-as-memory](./substrate-as-memory.md) paradigm. It partitions substrate architectures by where memory lives in the model:

- **P1 — Substrate-as-state.** Memory is the model's continuously-updated hidden state. The state is the memory; there is no separate store.
- **P2 — Substrate-as-module.** Memory is a separate differentiable module the model reads from and writes to, coupled to the main network via attention or gating.
- **P3 — Substrate-as-simulator.** Memory is the generative dynamics of a learned world model; remembering means simulating forward.

Cognitive architectures (ACT-R, SOAR) are sometimes called a "fourth paradigm" but they predate the substrate-as-memory frame and operate at a categorically different abstraction. They are noted in scope-limits below, not assigned a P-number.

This concept page exists because the taxonomy is referenced by all ten surveyed papers in the substrate work and by both substrate hypotheses ([H29](../hypothesis/H29-edge-substrate-memory.md), [H37](../hypothesis/H37-pluggable-substrate.md)).

## P1 — Substrate-as-state

The hidden state of a recurrent or state-space model serves as the memory. State updates are the memory updates; state reads are the memory reads. No separate store, no separate operator.

| Paper | Mechanism | Key claim |
|---|---|---|
| [Mamba](../source/gu-dao-2023-mamba.md) | Selective state-space model with input-dependent transitions | Substrate-as-memory empirically viable at foundation-model scale `[ASSERTED]` |
| [Titans](../source/behrouz-2024-titans.md) | Test-time gradient updates driven by gradient-as-surprise | Schacter's re-encoding satisfied; explicit short/long/persistent splits `[ASSERTED]` |
| [TTT](../source/sun-2024-ttt.md) | Hidden state itself is a trainable model (linear, MLP, or Transformer) | Theorem 2: self-attention is a special case of TTT with Nadaraya-Watson kernel `[ASSERTED]` |
| [Nested Learning / Hope](../source/behrouz-2026-nested-learning.md) | Self-modifying Titans (inner) + Continuum Memory System (outer); frequency-stratified MLP chain | Substrate-as-memory recast as a (depth × frequency) continuum; optimisers reframed as associative-memory modules; stage-1-only consolidation `[ASSERTED]` |

**P1 strength.** Strong unification — the entire sequence-modeling design space reduces to "what kind of learner is your hidden state" ([TTT](../source/sun-2024-ttt.md)). Tight coupling between memory and reasoning; gradients flow naturally between them.

**P1 weakness.** No native concept of exemplar lookup. Memory is implicit in state, hard to inspect, hard to durably preserve across sessions. Mamba's plateau at 16k tokens shows vector hidden states have a structural ceiling `[ASSERTED]` ([source](../source/sun-2024-ttt.md)). TTT-MLP scales further but memory I/O becomes the bottleneck.

## P2 — Substrate-as-module

Memory is a separate differentiable module connected to the main model via learned read/write operations.

| Paper | Mechanism | Key claim |
|---|---|---|
| [NTM](../source/graves-2014-ntm.md) | External memory matrix + content/location addressing | First architecture in this paradigm; foundational `[ASSERTED]` |
| [MERLIN](../source/wayne-2018-merlin.md) | External memory matrix + content-addressed read head + MBP auxiliary world-model loss + gradient-stop policy | Distinctive structural element: memory representations shaped by **non-task auxiliary loss** (MBP) while policy consumes them through learned attention — joint training of memory + consumer under separate objectives `[ASSERTED]` |
| [kNN-LM](../source/khandelwal-2020-knn-lm.md) | Frozen LM + FAISS over training-data embeddings + λ-interpolation | Wiki-100M model + Wiki-3B datastore (13.73 ppl) beats Wiki-3B trained model (15.17 ppl) — retrieval can substitute for training `[ASSERTED]` |
| [RETRO](../source/borgeaud-2022-retro.md) | Trillion-token retrieval store + cross-attention | Frozen backbone, learned integration; the P2 frontier `[ASSERTED]`. Architectural inheritor of MERLIN's read head; dropped the MBP — see [memory-caddy](../open-question/memory-caddy.md) |

**P2 strength.** Native exemplar lookup, durable storage, inspectable. Can scale store size independently of model size.

**P2 weakness.** Read/write ops are differentiable in research but commonly degraded in production. The agentic-memory field has copied the static-DB worst-case (P2-degenerate) — prompt-concatenation instead of λ-interpolation or cross-attention — losing the learned integration that made P2 work. See [active-stages-framework](./active-stages-framework.md).

## P3 — Substrate-as-simulator

Memory is implicit in the parameters of a learned world model. To remember, the model simulates forward. To learn, it updates the world model itself.

| Paper | Mechanism | Key claim |
|---|---|---|
| [Ha & Schmidhuber 2018](../source/ha-schmidhuber-2018-world-models.md) | VAE + MDN-RNN; agent trained inside dream | First constructive-simulation substrate; documents the exploitability failure mode in §4.5 `[ASSERTED]` |
| [DreamerV3](../source/hafner-2023-dreamerv3.md) | RSSM with discrete-categorical latents; actor learned from imagined rollouts | Substrate is doing 4-5× more learning than the task-specific reward signal; published Nature 2025 `[ASSERTED]` |
| [LeCun 2022](../source/lecun-2022-autonomous-mi.md) | Six-module cognitive architecture; JEPA predicts in representation space (anti-generative) | The most complete theoretical substrate architecture; H-JEPA hierarchy `[ASSERTED]` |

**P3 strength.** Counterfactual reasoning via forward simulation, not just past lookup. Constructive memory in Schacter's sense. Tightly coupled with planning.

**P3 weakness.** Exploitability — agents trained inside a learned world model find adversarial policies exploiting model flaws ([Ha & Schmidhuber §4.5](../source/ha-schmidhuber-2018-world-models.md)). Generative-vs-JEPA split inside P3 is unresolved: [DreamerV3](../source/hafner-2023-dreamerv3.md) wins empirically while being generative, [LeCun 2022](../source/lecun-2022-autonomous-mi.md) argues against generative substrates, and hybrids (N-JEPA, MIND-V) are emerging `[ASSERTED]`.

## Hybrid architectures

The clean P1/P2/P3 partition is empirically softening:

- **N-JEPA** brings diffusion into JEPA (generative element in an anti-generative paradigm) `[ASSERTED]`.
- **MIND-V** uses V-JEPA 2 + Dreamer-style imagination together (P3 hybrid).
- **R2I** integrates Mamba/SSM into Dreamer for memory tasks (P1+P3).
- **Titans** internally splits short/long/persistent memory (P1 with P2-like categorical structure).
- **[EvoSC](../source/yu-2026-evosc.md)** pairs P2-degenerate retrieval (text-concatenated `Exp_c`, `Exp_s`, `C_s`) with a small learned soft-prompt prefix (`P_θ`, 20 tokens) `[ASSERTED]`. The soft prompt does not cleanly fit any of P1/P2/P3 — it is parameter-efficient adaptation atop a frozen base. By the strict-paradigm criterion it remains in the database paradigm; the [substrate-depth ladder](./consolidation-channel.md#substrate-depth-ladder) on [consolidation-channel](./consolidation-channel.md) is a better fit than a P-number.
- **[Hope (Nested Learning)](../source/behrouz-2026-nested-learning.md)** is P1-canonical (Titans descendant) but introduces an orthogonal axis: a **frequency-stratified MLP chain** where each block updates at a different rate `[ASSERTED]`. Different blocks of the same architecture occupy different rungs of the [substrate-depth ladder](./consolidation-channel.md#substrate-depth-ladder) simultaneously — high-frequency blocks at rung 2-3 (transient), low-frequency blocks at rung 5 (full FT at training time). The P1 family is best read as `(depth, frequency)`-pair-valued, not as a single point on a single axis. See [consolidation-channel § Frequency axis](./consolidation-channel.md#frequency-axis--depth-is-not-one-dimensional).

For Kerros, this means the design choice is not "pick a paradigm" but "what combination tested empirically." See [cross-session-continuity](../open-question/cross-session-continuity.md).

## Why this taxonomy matters for Kerros

- **It names the design space.** Every substrate-architectural decision is "P1, P2, P3, or hybrid." Without the taxonomy, candidate architectures are evaluated ad hoc.
- **It exposes the field's gap.** The agentic-memory products ([Mem0](../incumbent/mem0.md), [Cognee](../incumbent/cognee.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [LightMem](../incumbent/lightmem.md)) are all degenerate-P2 — they have a memory module but no differentiable read/write, no learned integration `[ASSERTED]`.
- **It anchors the [consolidation-channel](./consolidation-channel.md) design.** The channel needs to specify what paradigm the source store is (P2-exemplar) and what paradigm the target representation is (P1 state, P2 differentiable module, or P3 world-model weights).

## Scope limits

- The taxonomy classifies architectures, not implementations. A degenerate-P2 with prompt-concat retrieval is structurally P2 even if it loses the paradigm's value.
- **P0 — Cognitive architectures (ACT-R, SOAR)** are not included as a substrate paradigm. They predate the substrate-as-memory frame, operate at a symbolic abstraction (working/procedural/semantic/episodic stores), and are categorically different. The agentic-memory products inherit categorical structure from SOAR (30-year-old cognitive engineering) but do not implement substrate-as-memory.
- Production cost / scaling / inference economics are not in this taxonomy. Those are addressed by the [seven-layer-stack](./seven-layer-stack.md).

## Related

- [substrate-as-memory](./substrate-as-memory.md) — paradigm that contains all three sub-paradigms
- [consolidation-channel](./consolidation-channel.md) — operator across paradigm tiers
- [active-stages-framework](./active-stages-framework.md) — orthogonal axis (selection/consolidation/forgetting/updating); substrate paradigms vary in *how* they implement these stages
- [seven-layer-stack](./seven-layer-stack.md) — production-engineering axis; orthogonal to paradigm
- [H29-edge-substrate-memory](../hypothesis/H29-edge-substrate-memory.md) — predicts deployment locus of substrate paradigms
- [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md) — predicts pluggable-substrate path inside the paradigm
- [MEGa (Pan/Hahami/Zhang/Sompolinsky 2025)](../source/pan-2025-mega.md) — **P1 in-weights variant of CLS-grounded memory**. Per-memory gated LoRA adapters on Llama-3.1-8B base; softmax-gated retrieval over context keys. Explicit CLS framing in paper (verbatim §5: *"gating systems and associated LoRA weights correspond to the fast learner ('hippocampus') while the rehearsal-triggered fine-tuning of the base weights correspond to the slow learner ('cortex')"*). Linear parameter growth limitation. The cog-sci-grounded in-weights variant; foil for the sidecar [caddy](./caddy.md) pitch.

## Source archive

Substrate survey: `comparison-grid.md` (master 6-axis grid that motivated the taxonomy).
