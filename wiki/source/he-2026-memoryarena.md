---
type: source
name: "He et al. — MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
status: timeless
program: masq-bench
last_ingested: 2026-06-08
sources: []
tags: [masq, benchmark, memory-eval, scoring]
---

## Citation

Zexue He, Yu Wang, et al. (14 authors incl. McAuley, Choi, Pentland). "MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks." arXiv:2602.16313 (Feb 2026).

## Location

- https://arxiv.org/abs/2602.16313
- https://memoryarena.github.io/

## Key claims (with our restatements)

### Single agent, formally

**Paper:** §3.2 defines one agent 𝒜, one environment ℰ, one persistent memory ℳ "initialized as empty at the beginning of each evaluation episode"; §4.1 runs "GPT-5.1-mini as the task agent" across all conditions.

**Our restatement:** despite "multi-session" framing, strictly single-party. The Group Travel personas (5–8 incrementally-joining travelers with JOIN/RELATION constraints, e.g. "I want to have dinner with Rebecca on the second day", §3.1) are *constraints the one agent must satisfy*, never authors whose utterances are attributed. Differentiation line for MASQ (our framing): MemoryArena tracks *whose preference a constraint belongs to for plan satisfaction*; MASQ tests *attributing utterances/decisions to speakers across team contexts*.

### Decision-grounded scoring (borrow this)

**Paper:** §4.2: Progress Score PS = fraction of ordered subtasks passed (Eq. 5); SR = all-or-nothing on the final downstream decision ("a task is successful if the final bundle or plan satisfies all group members"); §4.3: sPS = per-constraint partial credit; §4.4: SR@k = survival at subtask depth k.

**Our restatement:** success defined by whether the *final action* is right, not whether facts were recalled — the strongest ecological-validity move of the 2026 wave. MASQ's deterministic attribution scoring adopts the same spirit (closed-set exact-match over judge-fuzz).

### Recall benchmarks under-measure

**Paper:** Abstract: "agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting." Table 3/§4.3: near-zero SR (Group Travel SR/PS = 0.00 across **all** methods); "augmenting GPT-5-mini with external memory or RAG does not consistently outperform using the model's full long-context history alone."

**Our restatement:** citable evidence that recall-style benchmarks saturate while memory *use* fails. Citing caveat: **LoCoMo is not re-run in the paper** — the claim rests on their absolute floor vs LoCoMo saturation reported elsewhere.

### Table 3 SR vs PS — the two metrics (verbatim, re-read 2026-06-08)

**Paper (§4.2 + Table 3, gpt-5.1-mini task agent):** two metrics. **SR** = Task Success Rate, all-or-nothing on the final subtask. **PS** = Progress Score, fraction of subtasks completed. *"all methods achieve low SR and PS, with two environments exhibiting near-zero SR."* Verbatim group averages — **SR ≈ 0.00–0.02** throughout; **PS** by method group: **Long-Context avg 0.64, Memory avg 0.41, RAG avg 0.54** (individual methods: Letta PS ≈ 0.50, Mem0 ≈ 0.45, BM25 ≈ 0.56, Text-Embedding-3-Small ≈ 0.55). All-Method-Avg PS row spans ~0.35–0.57. `[MEASURED — verbatim Table 3, 2026-06-08]`

**Our restatement:** resolves the "40–60% question." [Du 2026 §5.3](./du-2026-autonomous-memory-survey.md) says models *"plummet to 40–60% in MemoryArena"* — that is a **fair citation of PS**, not a fabrication (PS ≈ 0.41–0.64). The stricter **SR collapses to ~0**. The passive→decision-relevant gap holds on both metrics; SR is the more dramatic. *Construct-validity:* SR and PS measure different things (final success vs partial progress) — when we cite the gap, cite both with their definitions, never the rounded gloss alone. Group Travel SR=PS=0 prompted the softer sPS metric (§4.3), so cite SR floors with that context.

## Important caveats

- Hybrid corpus (WebShop/BrowseComp-Plus/TravelPlanner + expert annotation) — task realism, not conversational realism.
- Group Travel's zero scores prompted the softer sPS metric mid-paper (§4.3) — the task may be over-hard; cite SR floors with that context.

## Relevance to Kyrja

- Anchors [concept/multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) (kill-criterion check; strongest 2026 neighbor) and the scoring commitments in [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md).
- Paper-claimed: quoted material. Our extrapolation: "constraint ownership ≠ utterance attribution."

## Audit history

2026-06-07, Nils (indigo): 100% read via structured delegation (verbatim-quote contract; exhaustive keyword sweep — zero hits on multi-agent/speaker/attribution/shared-workspace terms). Notes: [masq/reads/memoryarena-2602.16313-notes.md](../../masq/reads/memoryarena-2602.16313-notes.md).

2026-06-08, Nils (indigo): re-fetched via arxiv MCP `download_paper`; verified Table 3 SR/PS numbers verbatim (the 2026-06-07 notes recorded SR only, not the PS band). Confirmed PS ≈ 0.41–0.64 / SR ≈ 0; resolved the Du "40–60%" question (= PS).

## Archive location

arXiv 2602.16313 — re-fetch via arxiv MCP `download_paper`; verify quotes against §3.2/§4.2 before cross-referencing.
