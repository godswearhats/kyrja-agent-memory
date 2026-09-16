---
type: source
name: "Wayne et al. 2018 — Unsupervised Predictive Memory in a Goal-Directed Agent (MERLIN)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, p2, differentiable-memory, predictive-coding, deepmind, caddy-precedent]
---

## Citation

Wayne, G., Hung, C.-C., Amos, D., Mirza, M., Ahuja, A., Grabska-Barwinska, A., Rae, J., Mirowski, P., Leibo, J. Z., Santoro, A., Gemici, M., Reynolds, M., Harley, T., Abramson, J., Mohamed, S., Rezende, D., Saxton, D., Cain, A., Hillier, C., Silver, D., Kavukcuoglu, K., Botvinick, M., Hassabis, D., Lillicrap, T. (2018). *Unsupervised Predictive Memory in a Goal-Directed Agent.* arXiv:1803.10760. DeepMind. Submitted 2018-03-28.

## Location

- arXiv: https://arxiv.org/abs/1803.10760
- HTML (verbatim quotes drawn from this read): https://ar5iv.labs.arxiv.org/html/1803.10760

**Meta-finding (2026-05-15):** MERLIN is **absent** from the [Shichun-Liu Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) (the 150+ paper catalogue cross-referenced from the `reference_paper_repo` project-memory entry). The modern survey's omission of DeepMind RL-era differentiable-memory architectures is itself a signal — the LLM-era agent-memory community treats RETRO/Memorizing-Transformer-style work as the relevant lineage, not MERLIN/DNC. This shapes the available prior art for the [memory-caddy](../open-question/memory-caddy.md) question.

## Key claims (with our restatements)

### Memory matrix architecture

**Paper (§2.2):** *"a two-dimensional matrix M_t of size (N^mem, 2×|z|), where |z| is the dimensionality of the latent state vector."* The write head is **positional**: *"The write weighting v_t^wr has length N^mem and always appends information to the t-th row of the memory matrix at time t, i.e., v_t^wr[i]=δ_{it}."* Memory updates (Eq. 2): `M_t = M_{t-1} + v_t^wr·[z_t,0]^⊤ + v_t^ret·[0,z_t]^⊤`.

**Our restatement:** `[ASSERTED]` — paper-supported. Memory is a fixed-capacity matrix; one row per timestep within an episode; write location is determined by the clock, not by content. This is **half** of what the [memory-caddy](../open-question/memory-caddy.md) third axis (computation-as-recall) names — the write side is mechanical, not learned. The read side (below) is where the learning happens.

### Read head — learned attention as recall

**Paper (§2.2):** Reading is **content-based**, proceeds in two stages: *"cosine similarity between each read key and each memory row j: c_t^{ij}=cos(k_t^i, M_{t-1}[j,·])"*, then *"a normalised weighting vector...w_t^i[j]=exp(β_t^i·c_t^{ij})/Σ_{j'} exp(β_t^i·c_t^{ij'})"*. Final readout: *"m_t^i = M_{t-1}^⊤·w_t^i"*. The K^r read keys and per-key temperatures β_t^i are produced by the controller as part of the *"memory interface vector i_t"* — *"segmented into K^r read key vectors k_t^1, ..., k_t^{K^r} and K^r scalars passed through SoftPlus"*.

**Our restatement:** `[ASSERTED]`. The read head is **the strongest existing template for "learned interface" between a memory module and a consumer**. Cosine-similarity attention over stored latents with learned keys + learned per-key temperatures. The mechanism that later appeared in [Memorizing Transformer](https://arxiv.org/abs/2203.08913) and conceptually in [RETRO](./borgeaud-2022-retro.md) (chunked cross-attention to a frozen kNN store) is structurally this read head, transposed to the LLM domain. **This is the half of MERLIN that the LLM-era retrieval-augmented language models inherited.**

### Memory-Based Predictor (MBP) — world-model objective

**Paper (§2.1, §3.1):** The MBP is trained with a **variational lower bound** (Eq. 3): `log p(x_{0:t}, y_{0:t}) ≥ Σ_τ E_q[E_q[log p(x_τ, y_τ | z_τ)] - D_KL[q(z_τ|·)||p(z_τ|·)]]`. The reconstruction loss (Eq. 5) decomposes into per-modality components: *"α_image·L_image + α_return·L_return + α_reward·L_reward + α_action·L_action + α_velocity·L_velocity + α_text·L_text"*. The framing: *"an agent's perceptual system should produce compressed representations...predictive modeling is a good way to build those representations; and the agent's memory should then store them directly."* The MBP *"is optimised to function as a 'world model': in particular, to produce predictions consistent with probabilities of observed sensory sequences."*

**Our restatement:** `[ASSERTED]` — paper-supported. **The MBP is MERLIN's distinctive structural element.** It shapes memory representations under a **non-task auxiliary loss** (multi-modality reconstruction + prediction) rather than under task reward alone. This is the predictive-coding / VAE shape: a dense, always-available training signal that builds useful memory structure *before* the policy learns to exploit it.

**Why this matters for Kyrja's [consolidation-channel](../concept/consolidation-channel.md):** the MBP is a worked example of the channel's write-side objective being something *other* than next-token prediction — a structurally different shape than what RETRO and the LLM-era retrieval models adopted. `[SPECULATED]` This raises an open empirical question carried into [memory-caddy](../open-question/memory-caddy.md): in the LLM era, does adding an MBP-style auxiliary world-model loss to a RETRO-shaped architecture improve over plain co-trained memory, or is the LLM's own next-token loss already doing what the MBP did?

### Policy interface — concatenation with gradient stop

**Paper (§2.3):** *"The policy can primarily be the downstream recipient of those state variables and memory contents."* The policy executes *"one cycle, but using only one read key, giving outputs [h̃_t, m̃_t]"* which are *"concatenated again with the latent variable [z_t, h̃_t, m̃_t]"* before producing actions. Critically: *"Parameters of the policy are entirely independent...via a gradient stop between the policy and the state variable z_t."* Training uses *"two separate ADAM optimisers with independent learning rates η^mbp and η^π."*

**Our restatement:** `[ASSERTED]`. The MBP's representations are *shaped by the MBP loss*; the policy *consumes* them but its gradients do not flow back into the MBP. This is the **decoupled-training pattern**: world model and consumer learn under separate losses through the same shared memory. For the [memory-caddy](../open-question/memory-caddy.md): it is a worked precedent for "memory model and consumer trained jointly but with independent objectives" — a more nuanced shape than either "frozen consumer + bolt-on memory" or "fully end-to-end co-training."

### Training regime — within-episode memory, between-episode reset

**Paper (§2.5, §3.2):** *"Memory is initialised blank, namely M_0 = 0"* at episode start. Training uses *"truncated backpropagation through time...MERLIN exclusively used a window of 1.3s to solve tasks requiring memory over much longer intervals."*

**Our restatement:** `[ASSERTED]`. Memory persists **within** an episode and **resets between** episodes. This is a *narrow* form of online learning — the memory matrix accumulates rows during deployment of a single episode, but neither the matrix nor the weights persist across episodes. For LLM agentic memory the relevant cadence is *across* sessions/deployments, which MERLIN does not address. **This is one of three structural reasons MERLIN has not been ported to LLM agents** (the others: end-to-end training cost, and the LLM's pretraining already partly subsumes the MBP role).

### Comparison to DNC

**Paper (§4.1):** Authors test an RL-DNC baseline — *"the same as the RL-LSTM except that the deep LSTM is replaced by a Differentiable Neural Computer...only applied to the memory game where episodes are short."* Their critique: *"external memory systems have been optimised 'end-to-end'...fails if a task demands high-fidelity perceptual memory."* MERLIN's alternative: memory is shaped by **unsupervised prediction** (the MBP), not by end-to-end task reward gradients flowing through the memory.

**Our restatement:** `[ASSERTED]` — paper-supported. The MERLIN-vs-DNC choice is precisely *what loss shapes the memory representations*: end-to-end task reward (DNC) vs separate predictive auxiliary loss (MERLIN). This is the **load-bearing architectural distinction**, not the addressing scheme or the memory data structure.

## Important caveats

- **Not an LLM-era system.** MERLIN was demonstrated on 3D partially-observable navigation tasks (DM Lab, Memory Maze variants), not language modelling or tool-using agents. Direct transferability to LLM agentic memory is `[SPECULATED]`.
- **Memory matrix is O(timesteps × |z|).** Within-episode scaling is fine for minute-scale episodes; lifetime memory at the agent timescale would blow the matrix size out unless additional consolidation/compression is added.
- **No surprise-weighted writes.** Writes are positional (every step → t-th row). MERLIN has no mechanism analogous to [Prioritized Experience Replay](./yang-et-al-2024-selection-of-experience.md) (Schaul 2016) — the priority signal would have to be added if MERLIN's shape were combined with PER's contribution. This is a candidate open hypothesis flagged in [memory-caddy](../open-question/memory-caddy.md).
- **MBP loss is multi-modality reconstruction**, not language modelling. The components (image, return, reward, action, velocity, text) are domain-specific to the navigation tasks. An LLM-era MBP would have to specify what the analogous prediction targets are. `[SPECULATED]` — the LLM's own next-token loss may or may not be a sufficient stand-in; this is unresolved.
- **Gradient stop is asymmetric.** Policy → MBP gradient is blocked; MBP → policy is implicit through the shared memory. This is a non-trivial training-engineering choice that may not transfer cleanly to a frozen-pretrained-LLM setting.

## Relevance to Kyrja

- **Cited by [memory-caddy](../open-question/memory-caddy.md)** — MERLIN is the cleanest existing template for "memory model jointly trained with a consumer under a non-task auxiliary loss." Three-axis check performed 2026-05-15: axis 1 (online learning) partial — within-episode only; axis 2 (learned interface) strong — content-addressed read head with learned keys + temperatures; axis 3 (computation-as-recall) partial — attention-as-recall over stored latents, not full-forward-pass-as-recall.
- **Cited by [consolidation-channel](../concept/consolidation-channel.md)** — MBP is a worked precedent for the channel's write-side objective being shaped by something other than the consumer's task loss. Predictive-coding shape distinct from CLS's biological framing but operationally aligned (build useful structure from dense observation signal, independent of reward).
- **Taxonomy:** P2-substrate-as-module in the [substrate-paradigms](../concept/substrate-paradigms.md) sense — separate differentiable module with learned read/write coupled to a controller. Closest historical ancestor of the LLM-era [RETRO](./borgeaud-2022-retro.md), which inherited the cross-attention read head but dropped the MBP.
- **Sharpens the open empirical question:** the LLM-era retrieval-augmented models ([RETRO](./borgeaud-2022-retro.md), Memorizing Transformer — `source/wu-2022-memorizing-transformer.md "pending"`) took MERLIN's learned read head into the language domain. They did not adopt the MBP's auxiliary world-model loss. Whether adding it back (MBP-style auxiliary loss + co-trained memory + cross-attention interface) improves over the existing co-trained-memory baseline is, as far as we have surveyed, an unmeasured ablation. This is the cleanest testable hypothesis in the caddy space.

## Audit history

- 2026-05-15 — verbatim quotes pulled from arXiv HTML render (ar5iv); §2.1-§2.5, §3.1-§3.2, §4.1 covered. Full paper not re-read end-to-end; subsequent claims that depend on §5 (results) or §6 (discussion) require a return pass.

## Archive location

arXiv:1803.10760. Not in `library/papers/`. Fetch from arXiv or ar5iv for re-verification. The HTML render at https://ar5iv.labs.arxiv.org/html/1803.10760 is the source for this page's verbatim quotes.
