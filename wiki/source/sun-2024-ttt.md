---
type: source
name: "Sun et al. 2024 — Learning to (Learn at Test Time): RNNs with Expressive Hidden States (TTT)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, test-time-learning, ttt, p1, icml-2024, guidepost, unification]
---

## Citation

Sun, Y., Li, X., Dalal, K., Xu, J., Vikram, A., Zhang, G., Dubois, Y., Chen, X., Wang, X., Koyejo, S., Hashimoto, T. & Guestrin, C. (2024). *Learning to (Learn at Test Time): RNNs with Expressive Hidden States.* arXiv:2407.04620. ICML 2024. Stanford / UC San Diego / UC Berkeley / Meta AI.

## Location

- arXiv: https://arxiv.org/abs/2407.04620
- ICML 2024 proceedings
- Rubric note: [substrate-survey/notes/sun-2024-ttt.md](../../../research/library/substrate-survey/notes/sun-2024-ttt.md)

## Key claims (with our restatements)

### Hidden state as a parametric model

**Paper (§2.1):** Every sequence model can be expressed as `s_0`, update rule `s_t = update(s_{t-1}, x_t)`, output rule `z_t = output(s_t, x_t)`. RNNs compress context into a fixed-size vector; attention keeps an unbounded list. TTT proposes the hidden state *is a parametric model* `W_t`, with output `z_t = f(x_t; W_t)` and update `W_t = W_{t-1} − η∇ℓ(W_{t-1}; x_t)`. Self-supervised loss is multi-view reconstruction with learnable projections `θ_K, θ_V, θ_Q`.

**Our restatement:** `[ASSERTED]` — TTT is the architectural framework for [P1 substrate-as-state](../concept/substrate-paradigms.md). Hidden state is no longer a vector but a learner. Strongest form of "memory is reasoning" because the substrate IS the inference engine.

### Theorem 2 — self-attention is TTT

**Paper (§2.6, Theorem 2):** A TTT layer with a Nadaraya-Watson nonparametric kernel learner produces *exactly* the self-attention output. **Theorem 1**: TTT-Linear with batch gradient descent equals linear attention.

**Our restatement:** `[ASSERTED]` — categorical reframing of the entire sequence-modeling design space. The Transformer is a TTT layer with a particular (nonparametric, kernel-based) inner-loop learner. **For Kyrja: the question "what should agent memory be?" reformulates as "what kind of online learner should the agent's substrate be?"**

### Vector hidden states plateau; parametric hidden states don't

**Paper (§1, §4):** *"once context is long enough, existing RNNs such as Mamba struggle to actually take advantage of the extra information."* Mamba plateaus after 16k tokens; TTT-Linear and TTT-MLP keep reducing perplexity through 32k.

**Our restatement:** `[ASSERTED]` — Mamba's hidden state is a vector that gets crowded; TTT's hidden state is a model with enough capacity to keep absorbing information. For agent memory: a database or fixed-dimensional embedding faces the same scaling wall; a parametric substrate scales more gracefully.

### Surprise-as-memorability, learned

**Paper (§2.1, §3):** *"our W remembers inputs that produce large gradients — intuitively, inputs that make W learn a lot."*

**Our restatement:** `[ASSERTED]` — same primitive [Titans](./behrouz-2024-titans.md) operationalizes; TTT is the predecessor. Surprise should drive encoding, and this should be learned rather than hand-engineered. Compare hand-engineered importance/surprise/emotion utility functions in agentic-memory products.

### Inner-loop / outer-loop meta-learning

**Paper:** Outer loop trains `θ_K, θ_V, θ_Q` and rest-of-network via standard backprop. Inner loop updates `W` during the forward pass on the test sequence via SGD. *"the outer loop can be interpreted as selecting a task from this family"* of multi-view reconstruction tasks.

**Our restatement:** `[ASSERTED]` — deepest form of "learn to learn" applied to memory. For agent memory, the substrate-update rule could itself be learned rather than hand-specified ("store messages with importance > 0.7"). The substrate learns *how* to learn from experience.

### Dual form for hardware efficiency

**Paper (§2.5):** Lets gradient computations leverage matmul hardware (TensorCores) rather than naïve sequential GD. ~5× speedup.

**Our restatement:** `[ASSERTED]` — substrate-update operations should be expressible as matmuls for GPU efficiency. Practical engineering primitive.

## Important caveats

- **TTT-MLP has acknowledged memory I/O problems** `[ASSERTED]`. Paper abstract: *"TTT-MLP still faces challenges in memory I/O."* Long-context deployment is research-grade, not production-ready.
- **No cross-session continuity.** Inner-loop `W` is reset between sequences; outer-loop `θ` persists. Same gap as every other sequence model `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **No simulation primitive.** Pure sequence modeling; no planning, no environment, no rollout.
- **No engagement with cog-sci.** Engineering paper; convergent design rather than cog-sci-grounded.
- **Active critique** `[ASSERTED]`: *Impossibility Triangle of Long-Context Modeling* (Zhou 2026) — theoretical limits paper; *Topological Trouble With Transformers* (Mozer et al. 2026) — likely critique of transformer architectures broadly. Critique targets specific architectural limits, not the paradigm.
- **Unification theorem is reframing, not deployable architecture.** Tells you the design space; doesn't tell you which point to occupy for agent memory.

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) — TTT is the most general P1 substrate-as-state framework; Mamba/Titans/attention are particular instances.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md) — TTT provides the architectural-theory scaffold for the entire substrate-as-memory design space.
- Anchors [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md) — TTT's `(θ-projections, W-state)` split is one possible interface for the pluggable-substrate hypothesis.
- Predecessor cited by [Titans](./behrouz-2024-titans.md).
- **Citation graph contains the thesis-validating paper** [Xu/Dai/Zhang 2026 "Contextual Agentic Memory is a Memo, Not True Memory"](./xu-2026-agentic-memo.md) — the Phase-2 deep-read that grounded Kyrja's consolidation-channel wedge.
- Application footprint across LLM agents (Sensi 2026), vision (TTT-as-attention linearization 2026), 3D reconstruction (Mem3R 2026), LLM reasoning (Zhou et al. 2026 — MIT/Jaakkola), suggesting substrate-as-memory for agents is being actively explored — though no commercial product has yet shipped it.
- Reusable for Kyrja: hidden-state-as-learner (not vector); learned self-supervised loss as the substrate-update objective; inner-loop/outer-loop meta-learning split; dual-form matmul-friendly gradient computation; mini-batch GD for parallelism with online-update semantics.

## Audit history

- 2026-05-13 — verbatim read, pp.1-10 (core sections §1-§3 plus Theorems 1 and 2), rubric note written with field-temperature memo.

## Archive location

arXiv:2407.04620. ICML 2024 proceedings. Not in `library/papers/`. Fetch from arXiv for re-verification.
