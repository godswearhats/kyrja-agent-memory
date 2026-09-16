---
type: source
name: "Wang et al. 2025 — Mem-α: learning memory construction via RL over a structured (core/episodic/semantic) store"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, structured-memory, grpo, process-reward, full-read, contests-caddy-rock3]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–C, incl. prompts and reward definitions), per [[feedback_load_bearing_sources]]. Page created directly at full-read status (no abstract-only predecessor existed).

## Citation

Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen Mao, Yuanzhe Hu, Julian McAuley, Xiaojian Wu. *Mem-α: Learning Memory Construction via Reinforcement Learning.* arXiv:2509.25911. Anuttacon / UC San Diego / Stanford. (First author Yu Wang is the MemoryLLM / M+ / MIRIX author — a latent-memory researcher who went text-store for this one; their related-work section explains why: latent capacity bounds + needing model internals.)

## Location

- https://arxiv.org/abs/2509.25911
- PDF: https://arxiv.org/pdf/2509.25911
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **Structured three-component text store** (§3.3): **Core** (≤512-token summary, always in context, `memory_update` only — MemGPT-style), **Semantic** (atomic facts), **Episodic** (timestamped events); the latter two support `memory_insert`/`update`/`delete`. Architecture explicitly modular/decoupled from the RL framework.
- **Genuine multi-step horizon** (§3.1.1): agent starts from empty memory, processes n chunks sequentially (instances up to 30k tokens), and may issue a *sequence* of K_t tool calls per chunk. This is trajectory-level, unlike Memory-R1's per-turn bandit.
- **Write-only learnable, same decoupling as R1/R2** (§3.1.3): retrieval is fixed BM25 top-k; the answer generator is frozen Qwen3-32B; reward flows only to the construction policy.
- **Reward (Eq. 1, App. B): r = r1 + r2 + β·r3 + γ·r4**, where r1 = QA accuracy over the **final** memory M_n (global, shared by every action in the trajectory), r3 = compression 1 − l_mem/l_chunks (global), r2 = per-action tool-call format/execution success, **r4 = per-action semantic validity judged by Qwen3-32B against rubric prompts** (Figs. 7–9: e.g. episodic entries must have temporal info; core must not be a placeholder).
- **GRPO with the KL term discarded** (§3.2); Qwen3-4B backbone; verl; 32 H100s × 3 days, 205 steps, 562 stratified training instances from 8 datasets (SQuAD/HotpotQA/PerLTQA/LongMemEval-train/NLU/TREC-C/PubMed-RCT/BookSum), Table 7.
- **Universal prompt scaffold** (Fig. 6): one prompt that tells the agent exactly what belongs in each memory type. RL again fine-tunes within a hand-built scaffold.

## Headline results (verified)

- **Validation (Table 1):** Mem-α avg 0.642 vs Long-Context Qwen3-32B 0.588, RAG-Top2 0.567, MemAgent 0.236, MEM1 0.111.
- **The RL-vs-architecture ablation (Table 3) is the clean one:** same memory framework, three drivers — base Qwen3-4B 0.389, gpt-4.1-mini 0.517, RL-tuned Qwen3-4B 0.642. RL training, not the memory structure, carries the gain; a 4B tuned model beats a frontier-mini prompted one.
- **OOD (MemoryAgentBench, Table 2):** avg 0.592 vs long-context 0.461 / RAG 0.502. **Length generalization 13×**: trained on ≤30k-token instances, works on up-to-474k-token streams.
- **Compression is modest in practice:** test-time memory averages ~129K tokens vs ~207K full storage — the store grows large; pushing β to 0.2–0.4 shrinks it but collapses test-time-learning tasks (Banking77 0.700 → 0.020 at β=0.2, Table 9).
- **Scale anomaly (App C.1):** Qwen3-**8B** was *worse* than 4B — systematically malformed tool-call arguments (`'semantic_memory'` suffix) and lower reward even after accommodating the format. Tool-call instruction-following does not improve monotonically with scale.

## The Rock-3 reading

Third data point, and the pattern now has three legs. Mem-α faces the closest thing yet to the real long-horizon problem (trajectory of write ops, mostly-global outcome reward) and its escape hatch is **dense per-action process rewards**: r2 (format) and r4 (LM-judge semantic validity) give every single tool call an immediate score. Their own ablation (§4.4, Tables 4/9): **γ=0 (drop the judge reward) → "catastrophic performance degradation"** — avg falls 0.642→0.543 on validation, 0.592→0.445 OOD, with TREC-C 0.666→0.423. The pure-outcome regime fails to learn memory construction; the judge-shaped regime learns it.

Updated cross-paper pattern (all three verified):

| Paper | Horizon | What densifies the reward |
|---|---|---|
| Memory-R1 | one op (bandit) | turn-attributed QA pairs |
| Memory-R2 | 8→32 sessions | curriculum + cached-state rerollouts + session-attributed QA |
| Mem-α | ~8–23 chunks | per-action LM-judge validity + format rewards |

**Nobody trains a discrete write policy on sparse end-of-trajectory reward alone.** The text-level claim survives in all three, and in all three convergence is purchased with some form of reward densification. For the caddy's latent variant the question is now sharp: which densifier ports? An LM judge can't read a latent slot, so Mem-α's r4 doesn't port directly — unless the probe/decoder gives the judge something legible, which loops back to the auxiliary-objective commitment (commitment 5).

## Other findings relevant to Kyrja

- **MASQ positioning quote (§3.4), verbatim:** "Our work focuses on the first three dimensions, **excluding Conflict Resolution due to the lack of realistic evaluation benchmarks—existing datasets for this dimension remain predominantly synthetic and do not adequately capture real-world complexity.**" A 2025 RL-memory paper explicitly skips the supersession/conflict dimension *for want of a credible benchmark*. That is MASQ's gap, stated by a third party. Cite this in the paper's positioning.
- **Schemas-in-the-store sighting** ([freeze-topology](../open-question/freeze-topology.md) interaction): the test-time-learning tasks store *classification rules* in core memory ("label 1: meaning; label 2: meaning…", Fig. 6) and apply them to new instances — learned-at-runtime rules living in store-as-data while all weights stay frozen. Existence proof (text-level) that grammar-ish content can live in the operand store; bears on the K2+T_A3 sub-question.
- **Memory-type taxonomy match:** core/episodic/semantic with per-type ops is the closest published structure to our tier framing in [verbatim-vs-latent-tiers](../concept/verbatim-vs-latent-tiers.md) — but flat, no consolidation between tiers, and conflict-free by dataset construction.
- **Frozen reader, again:** answer prompt (Fig. 10) tells the reader to acknowledge insufficiency, with no recency rule this time — their benchmarks exclude contradictions, so the reader never faces the MASQ situation at all.

## Important caveats

- Text store + tool calls; speaks to caddy commitment 4 not at all. Latent-level Rock 3 untouched (ironic, given the first author's latent-memory lineage — they state the latent capacity/access limits as their reason to go text).
- Reward needs a frozen 32B generator AND a 32B judge per action at training time — heavyweight scaffolding (32 H100s × 3 days for a 4B policy).
- Conflict resolution explicitly out of scope: the store only ever accretes/refines compatible facts in their data. DELETE exists but its training signal in conflict-free data is unclear (not analyzed in the paper).
- **Internal inconsistency:** §4.1 says hyperparameters "β=0.05, γ=1"; §4.4 says defaults are "β=0.05 and γ=0.1". One is a typo — the ablation tables make 0.1 the plausible value. Don't cite γ without this caveat.

## Relevance to Kyrja

- Cited by [caddy § Rock 3](../concept/caddy.md) cluster — now verified; completes the reward-densification pattern with R1/R2.
- Borrowable ([[feedback_borrow_not_adopt]]): per-action LM-judge validity reward (process supervision for write ops — the portable question is what plays "judge" for a latent slot); the RL-vs-architecture ablation design (Table 3) — clean way to show *training* beats *structure*; stratified small-N instance sampling for expensive RL.
- Direct MASQ asset: the conflict-resolution exclusion quote.
- Sibling cluster: [Memory-R1](./yan-2025-memory-r1.md), [Memory-R2](./yan-2026-memory-r2.md), AgeMem (arXiv:2601.01885, still abstract-only).

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); all claims verified against full text with section/equation/table numbers.

## Archive location

arXiv:2509.25911 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.
