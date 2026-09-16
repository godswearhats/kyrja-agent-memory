---
type: source
name: "Yan et al. 2026 — Memory-R2: fair credit assignment for long-horizon memory-augmented LLM agents"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, credit-assignment, grpo, multi-session, full-read, contests-caddy-rock3]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv HTML full text (main body + appendices A–E, including prompt templates). All claims below verified against the paper with section/equation numbers per [[feedback_load_bearing_sources]]. Supersedes the 2026-06-10 abstract-only version of this page.

## Citation

Sikuan Yan, Ahmed Bahloul, Ercong Nie, Susanna Schwarzmann, Riccardo Trivisonno, Volker Tresp, Yunpu Ma. *Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents.* arXiv:2605.21768v1 (submitted 2026-05-20). LMU Munich / MCML / Huawei Heisenberg Research Center / TUM.

## Location

- https://arxiv.org/abs/2605.21768
- PDF: https://arxiv.org/pdf/2605.21768v1
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **Text memory bank, tool-call operations.** A fact extractor proposes atomic facts (Eq. 1); a memory manager picks **INSERT / UPDATE / DELETE** (+ NO OPERATION via prompt) conditioned on the extracted fact and current bank (Eq. 2); a deterministic transition operator applies the op (Eq. 3). Both roles are **one shared Qwen2.5-7B-Instruct backbone with role-specific prompts** (Eq. 6, §3.1).
- **Retrieval is NOT trained.** Answer-time retrieval is top-30 embedding similarity per speaker with threshold 0.3 (§A.1). They train memory *formation* and *evolution* only.
- **Reward (§3.3, Eq. 8–10):** session-level reward `R = QA(M, Q_t) − λ_comp·Comp(M, t)` where QA is token-level F1 produced by a **fixed answer agent** (GPT-OSS-120B during training, "since a weaker answer model would yield noisy reward signals," §4.1) and Comp penalizes bank size above an α-fraction token budget. Best λ_comp = 0.3 (§4.4).
- **LoGo-GRPO (§3.3):** global branch = standard GRPO over n=16 trajectory rollouts, terminal memory scored per session-attributed question set (Eq. 11–12). Local branch = each session selected with p_local = 0.5 (Eq. 13); pick an anchor rollout, **retrieve the cached memory state M_{t−1} immediately before session t**, sample m=4 rerollouts of that session only from the shared state (Eq. 14–15). Unified dual-clipped step-level objective (Eq. 16–17) with length-normalized step ratios (Eq. 7) to stop the shared policy drifting verbose.
- **Curriculum (§3.4, A.2):** horizon 8 → 16 → 32 sessions (10/5/5 epochs), best validation checkpoint seeds the next stage.

## Headline results (verified)

- **Table 1 (LoCoMo, backbone-controlled):** Memory-R2 overall **F1 50.60, B1 44.01, J 80.99** vs Memory-R1 **43.14 / 36.44 / 61.51** (R1 numbers as reported in their paper). RL-tuned 7B answer agent beats the frozen GPT-OSS-120B variant on F1/B1. σ over 3 seeds in Table 3 (overall F1 ±1.34).
- **Data efficiency (A.2):** memory-construction policy trained on **two LoCoMo conversations (328 QA pairs total)**, 2:1:7 conversation-level split. OOD zero-shot transfer to LongMemEval (oracle F1 27.88 → 50.60), MSC-Self-Instruct, MemBench (§4.2, Fig. 2a). Scale transfer: Qwen2.5-3B F1 10.3 → 46.8 (Fig. 2b).
- **Ablations (Table 2) — the load-bearing decomposition:**
  - LoGo-GRPO → plain GRPO: **49.67 → 46.62 F1 (−3.05)**, M-Fail 6.72 → 10.20. The fairness fix is real but **modest**.
  - **− curriculum: 49.67 → 24.12 F1 (−25.55), M-Fail → 46.5%.** Direct 32-session training peaks at F1 0.47 then collapses to 0.27 with M-Fail exploding past 70% (Fig. 3c–d, Fig. 11). **Curriculum, not LoGo, carries most of the stability.**
  - − length norm: −6.14 F1. Single merged agent: −10.53. Separate (non-shared) params: −5.36, M-Fail +26.28.
- **M-Fail metric (Eq. 18, §C.2):** fraction of gold evidence dialogue-turn IDs missing from the bank — isolates construction failure from retrieval/answering failure. Borrowable diagnostic.

## The Rock-3 verdict on full read

**The contested claim survives: a discrete memory-op write policy trained by outcome-ish reward converges at the text-store level and beats baselines.** But the full text *also confirms the rock's mechanism*: without the variance-engineering, training behaves exactly as the NTM/DNC/MERLIN history predicts — direct long-horizon training **collapses** (F1 0.47→0.27, M-Fail >70%). Convergence is purchased by four mechanisms, not by the regime being benign:

1. **Curriculum over horizon** (the single biggest contributor, −25.55 F1 when removed);
2. **Local rerollouts from cached memory states** (the fairness fix; worth ~3 F1);
3. **Session-attributed rewards** — Q_t is "the subset [of QA pairs] whose required evidence is attributed to session t" (§3.3). This is **privileged supervision** from LoCoMo's evidence-location annotations, denser than a pure end-of-trajectory reward. "Minimal supervision" framing should be read with this in mind;
4. **A heavy hand-coded prior.** The extractor and manager prompts (Figs. 6–7, App. B) are large rule systems: atomicity, 20-word cap, self-containment, a fixed 4-step decision order (DELETE on contradiction → NO-OP on semantic equivalence → UPDATE on same-story progression → INSERT), and a monotonicity rule ("factual information must never be lost unless explicitly contradicted"). RL fine-tunes *within* this scaffold. This is **RL-polished prompt-scaffolded policy**, not a write policy learned from scratch — relevant contrast for caddy commitment 2.

**Correction to the previous (abstract-only) caveat.** The page previously speculated that the fairness fix can't port to a latent store because "you cannot cheaply re-roll from a 'shared' injected state." On full read this is the wrong bottleneck: the local branch needs (a) a **checkpointable memory state** — cheap for a latent store too, it's tensors; (b) a **replayable environment** — available at training time by construction (replayed dialogue); and (c) **session-attributable probe rewards** — this is the genuinely expensive ingredient, and it is supervision-shaped, not architecture-shaped. The latent-port question reduces mainly to (c) plus reward propagation through an injection interface instead of a frozen answer agent.

## Other findings relevant to Kyrja

- **[fact-supersession](../concept/fact-supersession.md):** their action space *contains* a supersession-ish move — UPDATE explicitly covers "later development or confirmation of the SAME entity's ongoing story (plan → outcome)" with same-ID rewrite, and DELETE fires only when a fact is "explicitly prove[d] false or invalid (**not merely outdated**)" (Fig. 7). This matches our design lemma 2 (the action space must contain the reconciling action) — but the disposition is *prompt-engineered*, not learned, and outdated-but-true state is retained by monotonicity rule, deferring conflict resolution to read time.
- **MASQ crossover:** the answer-agent prompt hard-codes "If the memories contain contradictory information, **prioritize the most recent memory**" (Fig. 8, App. B.3). A recency-default reader is baked into the harness — exactly the reader-policy confound MASQ's C3/C4 design holds fixed and probes. Their Temporal-category J score (69.90, their weakest J category for the 7B variant) is graded under this hard-coded recency rule.
- **Internal inconsistency worth knowing:** Table 2's Training-Target ablation (train-only-manager 45.34 vs train-only-extractor 28.30) is summarized in §4.3 as "fact extraction is the more brittle of the two roles when left untrained" — but train-only-manager (extractor untrained) is the *smaller* drop. Either the table rows or the prose conclusion is flipped. Don't cite that sentence.
- Horizon ceiling unchanged: 32 sessions, single benchmark family for training (LoCoMo). The "store in session 1, pays off weeks later" regime the caddy targets remains untested.

## Important caveats

- Text store, tool-call operations — does **not** establish that a latent-store / activation-injected controller (caddy commitment 4) trains. The Rock-3 split (text-level vs latent-level) stands; this paper settles only the text side.
- Reward depends on a fixed strong answer agent and annotated evidence locations; both are training-time scaffolds a deployed system wouldn't have.
- Closer to **bolt-on-with-learned-controller** than to the caddy in our taxonomy ([caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md)).

## Relevance to Kyrja

- Cited by [caddy § Rock 3](../concept/caddy.md) as the most on-point text-level contesting evidence — **now verified on full read**.
- Borrowable mechanisms ([[feedback_borrow_not_adopt]]): checkpoint-and-reroll credit assignment; horizon curriculum; M-Fail-style construction diagnostic; length-normalized step-level objective for shared multi-role policies.
- Directly relevant to [fact-supersession](../concept/fact-supersession.md) (see above).
- Same group as [Memory-R1](./yan-2025-memory-r1.md) (Yan, Nie, Tresp, Ma).

## Audit history

- 2026-06-10 — page created from abstract by Nils (indigo).
- 2026-06-12 — **full-text verbatim read by Nils (indigo)**; all claims verified with section/equation numbers; abstract-only caveats resolved; latent-port caveat corrected (checkpointing is cheap; session-attributable probe rewards are the expensive ingredient).

## Archive location

arXiv:2605.21768v1 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` still pending.
