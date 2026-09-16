# LongMemEval (arXiv 2410.10813) — verbatim positioning notes for MASQ

*Read 2026-06-07 (Nils, via verbatim-quote extraction; 100% of paper text covered, exhaustive keyword sweep). Wu, Wang, Yu, Zhang, Chang, Yu — UCLA / Tencent AI Lab / UCSD. ICLR 2025.*

## Party structure: strictly single-user ↔ single-assistant

- §3.1 (Problem Formulation): "𝐒 ≡ [(t₁,S₁),…,(tₙ,Sₙ)] is a sequence of N history chat sessions… where Sᵢ is a multi-turn interaction between **the user and a chat assistant**… Each session can be further decomposed into rounds: **one user message followed by one assistant response**."
- §A.1: sessions built by Llama-3-70B self-chat with exactly two roles; multi-party output is a **discarded failure mode**: "in a few rare instances, the user LLM fails by assuming the assistant role instead. When these failures are identified, we discard the instance."
- Distractors (§A.2): 25% ShareGPT, 25% UltraChat, 50% simulated — all single-dyad.

## Five abilities (§3.2), verbatim anchors

- IE: "recall specific information… including the details mentioned by either the user or the assistant" — the only role-conditioned split is **user-side vs assistant-side content**, a *content-source* axis, not a *speaker-identity* axis.
- MR: "synthesize the information across multiple history sessions… aggregation and comparison."
- KU: "recognize the changes in the user's personal information and update… dynamically over time."
- TR: "explicit time mentions and timestamp metadata."
- **ABS** (closest to MASQ rejection): "identify questions seeking unknown information, i.e., information not mentioned by the user… and answer 'I don't know'." Built as **30 false-premise rewrites**. Trigger = information *absence*, NOT speaker disambiguation.

## Scoring & sizes

- LLM-judge only (no exact match): prompt-engineered **gpt-4o-2024-08-06**, per-type rubrics; meta-eval ≥97% human agreement (§3.3, §A.4, Table 6).
- 500 manually created questions. LongMemEval_S ≈ 50 sessions / ~115k tokens; LongMemEval_M = 500 sessions / ~1.5M tokens (§1, §3.2, Table 1).

## Citable numbers

- Cleanest "30% drop": GPT-4o Oracle 0.870 → full-S 0.606 = **30.3% drop** (Fig 3(b), no-CoN). Range claim: "30%∼60% performance drop" (§1). Commercial (human study, §3.4/Fig 3(a)): ChatGPT(GPT-4o) 0.5773 (37% drop), Coze(GPT-4o) 0.3299 (64% drop) vs offline reading 0.9184.

## Kill-criterion verdict

**Zero occurrences** of: who said / speaker / multi-party / multiple users / source memory / provenance / group chat / workspace. All "attribute" hits = their 164-attribute user ontology. Verbatim negative space — their own novelty claim is the *content-source* axis: §2 "existing QA-based benchmarks overlook… **recalling assistant side information**." → **LongMemEval's multi-role axis is user-vs-assistant content recall in a fixed dyad. MASQ's speaker-identity attribution over a multi-party shared workspace is orthogonal and uncovered.**
