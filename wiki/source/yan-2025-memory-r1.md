---
type: source
name: "Yan et al. 2025 — Memory-R1: RL for LLM memory management & utilization"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, memory-operations, credit-assignment, ppo, grpo, full-read, contests-caddy-rock3]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–G, including prompt templates and algorithms). All claims below verified against the paper per [[feedback_load_bearing_sources]]. Supersedes the 2026-06-10 abstract-only version of this page.

## Citation

Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schütze, Volker Tresp, Yunpu Ma. *Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning.* arXiv:2508.19828 (v5). LMU Munich / MCML / TUM / Cambridge / HKU / TU Darmstadt / Edinburgh.

## Location

- https://arxiv.org/abs/2508.19828
- PDF: https://arxiv.org/pdf/2508.19828v5
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **Two separately-trained agents, text memory bank.** A **Memory Manager** picks {ADD, UPDATE, DELETE, NOOP} + updated content per extracted fact (Eq. 1; operator set adopted from Mem0); an **Answer Agent** does "Memory Distillation" — selects relevant entries from 60 retrieved candidates before answering (Eq. 5, §3.2). Distinct from R2: two policies, not one shared backbone.
- **Retrieval is NOT trained** (same as R2): top-30 similarity RAG per speaker → 60 candidates (Algorithm 2).
- **Reward = Exact Match** on the final answer (Eq. 4), for both agents. They ablated an LLM-as-a-Judge reward (Table 2): it lifts J (63.58) but craters F1/B1 by encouraging verbose answers; EM kept for metric balance. Note the circularity surface: reward metric ∈ evaluation metrics.
- **Strictly staged training (App E, Limitations).** Manager trained with **frozen Answer Agent** providing reward; Answer Agent trained with **fixed Manager**. Never joint: "we train [them] separately to ensure stability under sparse rewards" (Limitations). They name end-to-end multi-agent RL as future work.
- **PPO (Eq. 2) and GRPO (Eq. 3)** both work; GRPO generally better and converges faster (Fig. 7). VERL framework, 4×H100 (8 for 14B), LoCoMo only.

## The load-bearing detail: credit assignment is per-turn, not long-horizon

This is the thing the abstract hides. Training data construction (App B.2, Algorithms 1 & 5):

- For each dialogue turn, **GPT-4o-mini pre-builds a "temporal memory bank"** snapshot from the preceding turns (B.2 prose says 24 turns; Algorithm 1 says 50 — see inconsistencies below). The training input is (snapshot bank, current turn, **QA pairs linked to that turn**).
- The manager makes its op decision against that snapshot, the frozen Answer Agent answers the turn-linked question, EM reward flows to **that single decision**.

So the Memory Manager is trained as a **contextual bandit, one op per episode, with turn-attributed reward** — not over multi-session trajectories. The long-horizon credit-assignment problem Rock 3 is about is engineered away in the data construction, via (a) turn-linked QA annotations (privileged attribution, same flavour as R2's session-attributed Q_t) and (b) a strong external model (GPT-4o-mini) manufacturing the bank states the policy trains against. "Minimal supervision" = 152 QA pairs, but each is a dense, perfectly-attributed reward for a one-step decision.

This also explains the sibling paper's existence: **Memory-R2's entire contribution is extending this per-turn scheme to actual multi-session trajectories — and that required curriculum + LoGo to avoid collapse** (see [yan-2026-memory-r2](./yan-2026-memory-r2.md), Rock-3 verdict).

## Headline results (verified)

- **"152 training QA pairs" is real**: 1:1:8 conversation-level split of LoCoMo = 152/81/1307 questions (§4.1); trained only on LoCoMo, zero-shot on MSC + LongMemEval.
- **Table 1 (LoCoMo):** LLaMA-3.1-8B GRPO overall **F1 45.02 / B1 37.51 / J 62.74** (best); Qwen-2.5-7B GRPO **43.14 / 36.44 / 61.51** — matches the numbers R2 cites for R1. Relative gains ~28% F1 / ~30% J over strongest non-RL baseline (MemoryOS).
- **RL beats SFT-from-GPT-5**: Memory-SFT (behaviour cloning on GPT-5 trajectories, same data) gets 42.81 F1 vs GRPO 45.02 on LLaMA — outcome-driven RL > imitation of a much stronger teacher, on this task.
- **Ablations (Fig. 5, LLaMA-8B):** RL'd Answer Agent is the bigger contributor (PPO 32.5→41.0 F1) vs RL'd Manager (34.5→41.0); distillation worth ~4 F1 for GRPO (41.0→45.0). Stronger manager (GPT-4o-mini) amplifies Answer-Agent gains (Fig. 6) — quality compounds across the pipeline.
- **Scale transfer:** Qwen 3B/7B/14B all improve under PPO/GRPO (Table 3). Zero-shot LongMemEval: GRPO beats all baselines on both backbones (Table 5).

## The Rock-3 reading

Confirms the abstract-level claim — **discrete text-store memory ops are RL-trainable with tiny data** — but the mechanism is even more supervision-shaped than R2's:

1. **No long-horizon training at all** for the manager (per-turn bandit, above). The historical NTM/DNC/MERLIN failure mode is avoided by never entering its regime.
2. **Heavy prompt scaffold, again.** The Manager prompt (Figs. 9–10, adapted from Mem0) is a rule system with worked examples per op; the RL polishes a prompted policy. Same pattern as R2 (caddy commitment-2 contrast).
3. **Frozen-counterpart staging, again.** Each policy trains against a frozen partner — relevant precedent for [freeze-topology](../open-question/freeze-topology.md): even at training time, nothing here is jointly plastic.

Pattern across both Yan papers: **convergence is purchased with reward-attribution density** (turn-linked here, session-attributed in R2), not by the discrete-write regime being benign. The caddy's latent variant has neither paper's escape hatch unless we manufacture equivalent probe-attributed rewards.

## Other findings relevant to Kyrja

- **MASQ crossover, confirmed in R1 too:** Answer Agent prompt instruction 4: "If the memories contain contradictory information, prioritize the most recent memory" (Fig. 11). The hard-coded recency-default reader predates R2 — it's inherited harness furniture in this lineage, exactly the reader-policy confound MASQ holds fixed.
- **[fact-supersession](../concept/fact-supersession.md):** Fig. 1 / App A.1 case studies are supersession failures verbatim — vanilla manager treats "adopted another dog named Scout" as contradiction → DELETE+ADD fragments memory; RL'd manager issues consolidating UPDATE. Their motivating example *is* our design lemma 2 in the wild. But DELETE semantics are coarse: Algorithm 3/5 line "M ← M \ M_ret" drops the **entire retrieved set** on a DELETE.
- **Latency (App G):** GRPO'd Answer Agent is *faster* than base (p95 0.67s vs 3.07s on LLaMA) — RL compressed the reasoning; accuracy-latency Pareto improvement, not trade-off. Useful counter to "learned components must cost latency."

## Internal inconsistencies / hygiene flags (verified, don't cite these parts)

- **24 vs 50 turns:** B.2 prose says GPT-4o-mini builds the bank "from the preceding 24 turns"; Algorithm 1 line 5 says "previous 50 turns." One is wrong.
- **LoCoMo stats differ across sections:** §4.1 says "about 600 turns, 26k tokens"; App B.1 says "averaging 300 turns and 9k tokens" for the same benchmark.
- **Reference-list rot:** Sulemani 2021 cites `https://example.com/your-link-here` (placeholder URL); the ReadAgent and MemoryBank entries carry author lists that don't match the actual papers; a raw bibkey (`lee2024human`) leaks into §2.1. Treat the related-work citations with suspicion; verify independently before reusing any.

## Important caveats

- Text store, tool-call ops — does **not** speak to the caddy's latent/activation-injection variant (commitment 4). Rock-3 split (text vs latent level) stands; this paper settles only the text side, and only at one-step credit-assignment depth.
- GPT-4o-mini in the training-data loop and a frozen answer agent in the reward loop are scaffolds a deployed self-contained system wouldn't have.
- Closer to **bolt-on-with-learned-controller** than to the caddy ([caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md)).

## Relevance to Kyrja

- Cited by [caddy § Rock 3](../concept/caddy.md) as text-level contesting evidence — **now verified on full read**; verdict: claim confirmed at text level, but with one-step credit assignment, so it contests Rock 3 *less* deeply than R2 does.
- Borrowable ([[feedback_borrow_not_adopt]]): per-turn reward-attribution trick (manufacture dense single-decision episodes from long-horizon data); EM-vs-J reward-metric interaction (Table 2) as a worked example of reward/metric circularity; the SFT-from-stronger-teacher baseline design.
- Directly relevant to [fact-supersession](../concept/fact-supersession.md) and to [freeze-topology](../open-question/freeze-topology.md) (frozen-counterpart staging precedent).
- Same group as [Memory-R2](./yan-2026-memory-r2.md) (Yan, Nie, Tresp, Ma); R2 is the long-horizon successor.

## Audit history

- 2026-06-10 — page created from abstract by Nils (indigo).
- 2026-06-12 — **full-text verbatim read by Nils (indigo)**; abstract claims verified (152 pairs, ops, PPO/GRPO, transfer); key new finding: per-turn bandit credit assignment + GPT-4o-mini-constructed bank states; inconsistencies and citation-hygiene flags recorded.

## Archive location

arXiv:2508.19828v5 (full text read 2026-06-12). PDF download to `kyrja/library/papers/` still pending.
