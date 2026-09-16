---
type: source
name: "Mao et al. 2026 — TreeMem: pipeline-tree Monte Carlo credit for memory agents; independent replication of structural credit"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, grpo, credit-assignment, structural-credit, multi-agent-pipeline, full-read, latent-densifier-candidate]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–E incl. agent prompts and reward-model prompt), per [[feedback_load_bearing_sources]]. Page created directly at full-read status. Read as the independent check on [Mem-T](./yue-2026-mem-t.md)'s structural-credit mechanism.

## Citation

Marina Mao, Alexandr Liu, Pengbo Li, Siheng Li, Bo Zhou, Xiang Wang. *Tree-based Credit Assignment for Multi-Agent Memory System.* arXiv:2605.04811v1 (06 May 2026). USTC / Tencent LLM Dept. / HKUST / CUHK.

## Location

- https://arxiv.org/abs/2605.04811
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **"Multi-agent" = pipeline roles, single user.** Builder (history → fact-level entries) → Summarizer (entries → higher-level summaries) → Retrieval/Responder (query + both memory levels → answer), Eq. 1. Three separate policies updated jointly. **No multi-party writers anywhere** — zero overlap with the MASQ axis.
- **Tree-structured rollout (§3.2):** per training example, G builder outputs; J summarizer outputs per builder; K answers per builder–summarizer pair → G·J·K trajectories. **Reward exists only at leaves** (answer vs gold). Credit (Eq. 5): responder = own leaf reward; summarizer = mean over its K leaves; **builder = mean over its J·K leaves** + a length penalty on |memory|/|history| (discourages verbatim copying). Pure Monte Carlo branch-averaging — no intermediate supervision, no annotations in the reward.
- **Optimization (§3.3):** sample one trajectory per builder subtree (G total), z-score each agent's credits across the group (Eq. 7), PPO-clipped per-agent objectives (Eq. 8), all three policies updated simultaneously. Tree used at training only; flat pipeline at inference.
- **Leaf reward is an LLM judge — but at the leaf only** (App. B.1): a 3B same-family model scores generated-answer-vs-reference semantic match in [0,1]. It reads answers, never store contents.
- **The horizon dodge (App. A "Data Processing"):** training examples are (H, q) pairs where **H = the single session containing the query's evidence, located via the benchmark's annotations**. The builder always sees the evidence-bearing session and emits its memory in one shot; tree depth is just the 3 pipeline stages. The annotation-free claim is true of the *reward*, not the *data curation* — evidence locations collapse the horizon before RL starts.
- Setup: Builder/Summarizer/reward-model = Qwen2.5-3B or Llama-3.2-3B; Responder = Qwen2.5-7B or Llama-3.1-8B; 8×A100; results averaged over ≥3 seeds.

## Headline results (verified)

- **PersonaMem (Table 1, main testbed; 32K/128K/1M histories):** TreeMem 0.69/0.75/0.71 (Qwen) vs best compared method CoMAM 0.64/0.70/0.66; +7.5% avg (Qwen), +5.5% (Llama). Also best on LongMemEval (F1 63.46 vs Memory-R1 54.36) and LoCoMo (48.88 vs 45.77 GAM) with Qwen2.5-7B (Table 2).
- **Table 3 — the control we care about:** same system trained with (a) uniform terminal-reward broadcast (the AgeMem move): 0.60–0.67; (b) hand-designed task-specific rewards (the Mem-α/CoMAM move): no better, sometimes worse; (c) sum of both: marginal gain; (d) tree credit: best everywhere (0.69–0.75 Qwen). **Structural credit beats both uniform broadcast and engineered intermediate rewards in a controlled comparison.**
- **Table 4:** removing tree credit from either single agent (builder or summarizer) hurts; full tree best across all context lengths.
- Sensitivity (Fig. 4): J, K small → noisy credit, performance drops; gains plateau with more branches. Convergence faster than both reward baselines; lowest memory-token/history-token ratio (Fig. 5).

## The Rock-3 reading — independent replication of the content-free densifier

Same mechanism family as Mem-T — **branch the computation, average leaf outcomes downstream, credit the node** — from an independent group, on a different decomposition axis (pipeline stages across heterogeneous policies vs retrieval steps within one policy). The credit signal consumes leaf outcomes, branching topology, and a length ratio; for a latent store, all three remain observable (outcome, topology, slot count). The leaf LLM judge is latent-compatible: final answers are text in any architecture; only store-reading judges break.

Convergence-is-evidence ([[feedback_convergence_evidence]]): two independent instances of structural credit beating broadcast supervision upgrades the latent-densifier question from "single-paper candidate" to "replicated mechanism family." The shared limit also replicates: **the genuinely long write horizon is never trained** — Mem-T retreats to filtered SFT; TreeMem collapses construction to a single-shot builder action on a privileged evidence-located session. And the paper's own Limitation section concedes branching cost grows with tree size — at 500-turn construction horizons, naive branch-and-average explodes. Structural credit is the most latent-portable densifier in the literature *and* its long-horizon viability is untested.

## Important caveats

- Text store; nothing latent. Latent-port argument is our extrapolation.
- LLM-judge leaf reward is same-family (3B judging its larger sibling's answers) — judge bias unexamined; no human-agreement study.
- Training data uses benchmark evidence-location annotations for session selection (privileged curation, see above) — the "without task-specific annotations" headline needs that qualifier.
- PersonaMem queries are 4-way multiple choice; LoCoMo/LongMemEval here are reimplementations (their Memory-R1 LoCoMo F1 43.14 differs from both the original 39.25 and other reimplementations — cross-paper number comparisons unreliable).
- Builder emits memory in one generation pass — no incremental ADD/UPDATE/DELETE stream, so supersession machinery is out of scope by construction.

## Relevance to Kyrja

- Updates [caddy § Rock 3](../concept/caddy.md) jointly with [Mem-T](./yue-2026-mem-t.md): replicated content-free densifier family — see the 2026-06-12 paragraph there.
- Confirms the multi-agent-memory naming hazard flagged in the 2026-06-12 sweep: "multi-agent memory system" in this literature means pipeline roles, not multi-party writers; no contact with [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md).
- Borrowable ([[feedback_borrow_not_adopt]]): the Table-3 experimental design itself — broadcast vs engineered vs structural reward as a three-way control — is the right template for any future Kerros densifier experiment.

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); "without task-specific annotations" qualified on inspection of App. A (evidence-located training sessions); leaf LLM judge surfaced from App. B.1.

## Archive location

arXiv:2605.04811v1 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.
