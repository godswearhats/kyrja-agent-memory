---
type: source
name: "Wu et al. — LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
status: timeless
program: masq-bench
last_ingested: 2026-06-07
sources: []
tags: [masq, benchmark, memory-eval]
---

## Citation

Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu. "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory." arXiv:2410.10813 (Oct 2024), ICLR 2025. UCLA / Tencent AI Lab / UCSD.

## Location

- https://arxiv.org/abs/2410.10813
- Code/data: https://github.com/xiaowu0162/LongMemEval

## Key claims (with our restatements)

### Strictly dyadic by construction

**Paper:** §3.1 formalizes the history as sessions where each "Sᵢ is a multi-turn interaction between the user and a chat assistant… one user message followed by one assistant response." §A.1: when the generating LLM produces multi-party-like output ("the user LLM fails by assuming the assistant role"), the instance is **discarded**.

**Our restatement:** the benchmark cannot test speaker attribution because multi-party structure is defined out of existence — literally a generation bug. Anchors the [multi-party attribution gap](../concept/multi-party-attribution-gap.md).

### The role axis is content-source, not speaker identity

**Paper:** the novelty claimed over LoCoMo is "recalling assistant side information" (§2); IE splits into single-session-user vs single-session-assistant question types (§3.2). Abstention (ABS) = "identify questions seeking unknown information… and answer 'I don't know'" — built as 30 false-premise rewrites (§3.2).

**Our restatement:** two fixed roles in one dyad ≠ identity among many parties. ABS triggers on information *absence*, not who-said-what disambiguation — closest analogue to MASQ's rejection queries, still orthogonal. (The orthogonality framing is our extrapolation.)

### Headline degradation number

**Paper:** GPT-4o Oracle 0.870 → full LongMemEval_S 0.606 = **30.3% drop** (Fig 3(b), no-CoN); range claim "30%∼60%" (§1). Commercial human study (§3.4/Fig 3(a)): ChatGPT(GPT-4o) 0.5773, Coze(GPT-4o) 0.3299 vs offline-reading 0.9184.

**Our restatement:** citable as "even single-party long-term memory is unsolved"; use the Fig 3(b) number — it is the literal source of the abstract's 30% claim.

### Scale & scoring

**Paper:** 500 curated questions; _S ≈ 50 sessions/~115k tokens, _M = 500 sessions/~1.5M tokens (§1, Table 1). Scoring = prompt-engineered gpt-4o-2024-08-06 judge, per-type rubrics, ≥97% human agreement (§3.3, §A.4).

**Our restatement:** the 500-question scale matches MASQ v1. Their judge-only scoring is the design MASQ deliberately deviates from (deterministic exact-match on attribution fields).

## Important caveats

- LLM-generated corpus (self-chat) with human verification — same synthetic-provenance class as MASQ v1; they scope claims accordingly.
- Distractors are *intra-user* noise (25% ShareGPT / 25% UltraChat / 50% simulated, §A.2) — no cross-speaker vocabulary collision.

## Relevance to Kyrja

- Anchors [concept/multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) (closest neighbor on query-type design) and [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md).
- Paper-claimed: all quoted material. Our extrapolation: the content-source vs speaker-identity axis framing.

## Audit history

2026-06-07, Nils (indigo): 100% read via structured delegation (verbatim-quote contract; exhaustive keyword sweep — zero hits on speaker/multi-party/attribution terms). Notes: [masq/reads/longmemeval-2410.10813-notes.md](../../masq/reads/longmemeval-2410.10813-notes.md).

## Archive location

arXiv 2410.10813 — re-fetch via arxiv MCP `download_paper`; verify quotes against §3.1/§3.2/§A.1 before cross-referencing.
