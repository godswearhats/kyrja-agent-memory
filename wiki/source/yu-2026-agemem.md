---
type: source
name: "Yu et al. 2026 — AgeMem: unified LTM+STM management learned in the agent's own policy"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, unified-memory, grpo, reward-shaping, full-read, contests-caddy-rock3]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–D, incl. tool schemas, reward formulas, algorithms, case studies), per [[feedback_load_bearing_sources]]. Page created directly at full-read status.

## Citation

Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu. *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents.* arXiv:2601.01885. Alibaba Group / Wuhan University.

## Location

- https://arxiv.org/abs/2601.01885
- PDF: https://arxiv.org/pdf/2601.01885
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **One policy does everything — the cluster's only no-frozen-counterpart design.** Six memory tools live in the *agent's own* action space alongside language generation: LTM **Add/Update/Delete**, STM **Retrieve/Summary/Filter** (Table 1, App. A.1, exact JSON schemas in Figs. 6–7). No separate memory-manager model, no frozen answer agent: the same weights write memory, manage context, and answer. (R1/R2/Mem-α all train against a frozen counterpart; AgeMem is the existence proof that joint training-time plasticity works at this scale/horizon.)
- **Three-stage trajectory** (§3.1, §3.3, Algs. 3–5): Stage 1 — casual conversation carrying the task-relevant context, agent decides what to Add to LTM (task query not yet revealed → must store on general salience cues); Stage 2 — **STM context reset** (LTM persists), semantically-related distractors injected, agent must Filter (cosine threshold θ=0.6) / Summarize; Stage 3 — query revealed, agent Retrieves + answers. The reset forces answers to flow through LTM, not residual context.
- **"Step-wise GRPO" is less than the name claims.** Intermediate rewards are zero (§3.1); the composite **terminal** reward is group-normalized (K=8 rollouts) and the terminal advantage is **broadcast uniformly to every step**: A_t = A_T (Eq. 5, Alg. 2 line 29 "// Broadcast"). Per-step elements are only the stored old-policy log-probs/importance ratios. This is exactly the uniform trajectory-credit scheme Memory-R2 names as the unfair-credit pathology — AgeMem lives with it and compensates by reward shaping.
- **Composite shaped reward (§3.5, App. A.2):** R = (R_task + R_context + R_memory)/3 + penalties. R_task = LLM-judge score (Qwen-Max), −1 if no answer. R_context = compression + preventive-action indicator + key-phrase preservation (⅓ each). R_memory = storage quality (**fraction of stored entries judged high-quality by an LLM with access to the query AND its expected answer A_q**) + maintenance (**literal indicator 1[any update-or-delete performed]**) + retrieval relevance (LLM score), ⅓ each. Penalties: rounds −1, overflow −0.5.
- **Training:** HotpotQA only (supporting-fact annotations supply Stage-1 context), zero-shot eval on ALFWorld/SciWorld/PDDL/BabyAI. Qwen2.5-7B + Qwen3-4B backbones; Trinity framework, KL β=0.1, 8192-token context cap, 8×RTX 4090 (App. C.4 — by far the cheapest training setup in the cluster).

## Headline results (verified)

- **Table 2 averages:** AgeMem 41.96 (Qwen2.5-7B) and 54.31 (Qwen3-4B) vs best baselines Mem0 37.14 / A-Mem 45.74. RL adds +8.53 / +8.72 points over AgeMem-noRL.
- **Untrained tool interface can hurt:** AgeMem-noRL *underperforms* even No-Memory on PDDL (8.87 vs 10.15) and BabyAI (46.34 vs 50.80) on Qwen2.5-7B. Giving a model six memory tools without training makes things worse; RL rescues it. (Echoes Mem-α's base-Qwen3-4B result.)
- **Reward-shaping ablation (Tables 4–5):** Answer-Only (pure outcome reward) still trains — J 0.509 vs All-Returns 0.544 (Qwen2.5-7B). The shaping buys quality, not trainability: Memory Quality 0.533 vs 0.479, and on Qwen3-4B MQ 0.605 vs 0.415 with near-identical J (0.555 vs 0.546). Note the consistency with R2: at *short horizons* outcome-only converges; AgeMem horizons are short (8k-token context, ~5–9 tool calls/episode, Table 3).
- **Tool-usage shift after RL (Table 3):** Add 0.92→1.64, Update 0.00→0.13, Delete 0.00→0.08 per episode (Qwen2.5-7B). Maintenance ops essentially don't exist pre-RL.
- **STM tools beat RAG by a little:** token reduction 3.1% / 5.1% vs the -RAG variants (Fig. 3) — real but marginal.

## The Rock-3 reading

Fourth and final cluster member. The abstract's promise — machinery "to address sparse and discontinuous rewards induced by memory operations" — resolves on full read to: **(a) uniform terminal-advantage broadcast (no per-step attribution at all) plus (b) dense reward *shaping* via LLM judges that see the ground-truth answer at training time, plus (c) short horizons.** The discontinuity (Stage-1/2 context reset) is handled by the broadcast, not by any clever attribution.

This completes the four-paper pattern, with a useful wrinkle:

| Paper | Horizon | Frozen counterpart? | Densifier |
|---|---|---|---|
| Memory-R1 | 1 op (bandit) | yes (answer agent) | turn-attributed QA |
| Memory-R2 | 8→32 sessions | yes (answer agent) | curriculum + cached-state rerollouts + session-attributed QA |
| Mem-α | ~8–23 chunks | yes (RAG generator) | per-action LM-judge validity + format |
| AgeMem | ~5–9 calls, 8k ctx | **no — single policy** | terminal shaping (LLM judges w/ ground truth) + maintenance-op indicator |

Two takeaways for the caddy: (1) the **no-frozen-counterpart existence proof** — a single policy can learn write + read + answer jointly, *but only at the shortest horizon in the cluster and with ground-truth-informed shaping*; (2) AgeMem's Answer-Only ablation converging confirms R2's horizon story from the other side: the rock bites as horizon grows, not because discrete ops are inherently untrainable.

**Reward-hacking surface worth remembering:** R_maintenance = 1[any update/delete performed] rewards the *existence* of a maintenance op, not its correctness. Post-RL Update/Delete rates rising from ~0 is partly this incentive. A blunt "do hygiene, get paid" term — the paper doesn't analyze whether the ops are *right*.

## Other findings relevant to Kyrja

- **Fact-supersession in the wild, case study B.1:** preference changes 60→120 min → agent issues Update (writing "(updated from 60 minutes)" provenance *into the content string*); later, when the user confirms permanence, it Retrieves, **Deletes the entry, and Adds a clean one** to purge the stale historical reference. Curated trace, but it's the supersession-hygiene loop [fact-supersession](../concept/fact-supersession.md) cares about — including the failure-prone pattern of provenance-in-content that then *requires* cleanup.
- **STM management as policy, not schedule:** Filter/Summary as learned actions vs ReSum-style fixed schedules — the capabilities-not-policies framing ([[feedback_capabilities_not_policies]]) appearing in the wild: tools are capabilities; *when* to fire them is learned.
- **Freeze-topology note** ([freeze-topology](../open-question/freeze-topology.md)): the cluster's training-time freeze choices now span both poles — three papers freeze the counterpart for reward stability, AgeMem trains everything jointly and survives. Still **zero** post-deployment plasticity anywhere in the cluster: all four freeze the policy at deployment; store contents are the only thing that changes in use.
- **Distractor-injection Stage 2** is a reusable harness idea: train/test context-hygiene under semantically-adjacent noise (their DistractorGen). MASQ's near-miss siblings are the benchmark-side cousin of this.

## Important caveats

- Text store + tool calls; nothing latent. Caddy commitment 4 untouched. The Rock-3 text/latent split survives all four papers.
- All reward judges (Qwen-Max) see ground-truth answers/supporting facts at training time — privileged supervision, again training-time-only scaffolding.
- HotpotQA-only training; the multi-benchmark transfer is real but all evals are short-horizon agentic tasks, not week-scale memory.
- LLM-judge metrics (J, MQ) graded by the same family (Qwen-Max) that the policy is built from (Qwen2.5/Qwen3) — same-family-judge bias unexamined.
- Several reward weights/thresholds asserted without sensitivity analysis (θ=0.6 filter, uniform ⅓ weights "without manual tuning").

## Relevance to Kyrja

- Cited by [caddy § Rock 3](../concept/caddy.md) cluster — now verified; the cluster read is COMPLETE (4/4 full reads, 2026-06-12).
- Borrowable ([[feedback_borrow_not_adopt]]): Stage-2 distractor curriculum; the context-reset trick to force information through the persistent store (clean way to isolate write-path contribution in *our* eventual experiments — same spirit as MASQ's sealed-reader probes); the no-RL-tools-hurt baseline as a confound control.
- Cautionary: maintenance-indicator rewards as a reward-hacking template to avoid.
- Cluster siblings: [Memory-R1](./yan-2025-memory-r1.md), [Memory-R2](./yan-2026-memory-r2.md), [Mem-α](./wang-2025-mem-alpha.md).

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); abstract's "step-wise GRPO for sparse/discontinuous rewards" claim deflated to broadcast-advantage + shaping on inspection of Eq. 5 / Alg. 2.

## Archive location

arXiv:2601.01885 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.
