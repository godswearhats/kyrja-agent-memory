---
type: source
name: "Feng et al. 2026 — ElasticMem: RL over latent memory is read-side only; the latent write cell stays empty"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, latent-memory, grpo, soft-tokens, read-side-only, full-read, caddy-commitment-check]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices C–F incl. training algorithm, dataset construction, and all prompts), per [[feedback_load_bearing_sources]]. Page created directly at full-read status. Read to settle one load-bearing fact: has anyone trained a latent *write* policy? (Answer: no.)

## Citation

Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Ge Liu, Jiaxuan You. *ElasticMem: Latent Memory as a Learnable Resource for LLM Agents.* arXiv:2605.30690v1 (29 May 2026). UIUC / NTU.

## Location

- https://arxiv.org/abs/2605.30690
- Code (announced): https://github.com/ulab-uiuc/ElasticMem
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **The bank is offline, frozen, and read-only** (§3.2, Alg. 1): each memory chunk is encoded once by a frozen LLM encoder; final hidden state = retrieval key, last N_c hidden states = content cache. "The offline memory bank remains fixed during training" — verbatim, twice (§3.6, App. C).
- **What RL trains (GRPO, outcome rewards): read side only.** (1) LoRA-adapted reasoner samples a retrieval-control token so the retrieval query comes from the model's own hidden state (Eq. 7–8; cosine vs cached keys, top-Z); (2) a small Transformer **budget policy** assigns each retrieved chunk b_j ∈ {0..B_max} soft tokens, b_j=0 = suppression (Eq. 12–15); (3) a projector maps selected cached states into the reasoner's embedding space (Eq. 16–17). Trajectory likelihood factorizes over control token × budgets × generation (Eq. 25). Single-shot per query — no multi-step memory interaction.
- **The store is latent at the injection interface only.** App. F: bank contents originate as *text* — prompted-LLM skill extraction ("SKILL: …" templates for QA; Gemini summarizes ALFWorld expert trajectories into 150–250-word procedural cards) — then encoded once. The original text is kept in the bank tuple (m_i, k_i, C_i). **The write side is the same prompted-extraction pipeline as prompt-era systems; nothing about what to store, how to consolidate, or when to update is learned. There is no streaming ingest at all** — the bank is batch-built before training.
- **"Budget" = truncation**: chunk's cache trimmed to its last b_j positions — learned *selection* of a fixed encoding, not learned compression.
- Rewards are closed-form where it matters: QA tasks are multiple-choice accuracy; ALFWorld is exact-match-to-expert-action after snap-to-admissible (App. D.2, imitation-style GRPO on 4,260 per-step samples from 709 expert trajectories).

## Headline results (verified)

- **MemorySuite-QA (Table 2):** weighted avg accuracy 0.74 (Qwen2.5-3B) / 0.83 (7B) vs strongest latent baseline MemGen 0.59 / 0.67; +26.2% / +24.6% over strongest baseline overall. ALFWorld avg SR 0.45 / 0.53 vs 0.27 / 0.42, with lowest token cost.
- **Ablations (Fig. 2):** Transformer budget policy > MLP > Uniform > Random (cross-memory attention matters); trainable reasoner-state retrieval > frozen-state > pure semantic similarity; B_max=20 optimum.
- **Qualitative (§4.3):** learns to suppress high-cosine-but-useless chunks and boost low-ranked evidence-bearing ones; in ALFWorld allocates budget by transferable plan structure (a `cool`-task card with shelf placement gets budget for a `heat`-to-countertop task) rather than task-type labels.

## The Rock-3 / commitment reading — the cell stays empty

The field's first "RL + latent memory" paper trains **zero write-side parameters**. What it establishes: the latent **read** side trains fine with content-free signals at short horizon — the budget policy's inputs are keys, similarity scores, and rank embeddings (metadata, never chunk contents), reward is closed-form at the leaf, and it learns genuinely non-obvious utility-vs-similarity distinctions. Consistent with the structural-credit picture from [Mem-T](./yue-2026-mem-t.md)/[TreeMem](./mao-2026-treemem.md).

What it leaves untouched: **a learned policy deciding what enters an opaque store, streaming, long-horizon — the caddy's commitment-2-over-latent-state bet ([caddy](../concept/caddy.md)) — remains unoccupied in the published literature as of 2026-06.** Capability-vs-resource caution applies ([[feedback_capability_vs_resource]]): absence here reads as "small teams pick the tractable read side," not as evidence the write side is unmeritorious.

## Important caveats

- **Benchmark protocol is non-comparable to the rest of the literature:** LoCoMo and LongMemEval are converted to 10-way multiple choice with "one option is guaranteed correct — do NOT say not answerable" — this deletes LongMemEval's abstention category and makes their numbers incomparable to F1-based reports elsewhere.
- **Trained-vs-untrained confound:** ElasticMem is trained on each benchmark's own 80/10/10 split; most text-space baselines are prompt-based and untrained. Part of the margin is training-on-distribution, though MemGen/M+ are trained latent baselines and the gap there is still large.
- ALFWorld training is imitation of an oracle planner (exact-match-to-expert reward) — IL dressed as GRPO; success transfers to unseen layouts but the signal is fully privileged.
- Single-shot memory use per query/step; no multi-step retrieval, no incremental store evolution; supersession machinery absent by construction.

## Relevance to Kyrja

- Anchors the "latent write policy untrained by anyone" clause in [caddy § Rock 3](../concept/caddy.md) (2026-06-12 paragraph) — previously suspected from the abstract, now full-read verified.
- Positive borrowable ([[feedback_borrow_not_adopt]]): the b_j=0 suppression action — retrieval proposes, allocation disposes — is a clean two-stage read-gating design; and the demonstration that utility ≠ cosine similarity is directly relevant to any caddy retrieval head.
- Sibling reads: [Mem-T](./yue-2026-mem-t.md), [TreeMem](./mao-2026-treemem.md) (same 2026-06-12 read queue).

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); abstract-level suspicion ("bank built offline so write side appears unlearned") confirmed against Alg. 1 and App. F; "latent store" qualified to "latent injection interface over text-derived content."

## Archive location

arXiv:2605.30690v1 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.
