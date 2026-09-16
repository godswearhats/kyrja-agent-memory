---
type: concept
name: Multi-party attribution gap
status: OPEN
program: masq-bench
last_ingested: 2026-06-12
sources: [../source/wu-2024-longmemeval.md, ../source/he-2026-memoryarena.md, ../source/mei-2026-atm-bench.md, ../source/wang-2025-mem-alpha.md, ../source/chao-2026-stale.md]
epistemic_tags: [MEASURED]
tags: [masq, benchmark, positioning, falsifiable]
---

## Definition

The claim that, as of 2026-06-07, **no existing LLM/agent memory benchmark makes multi-party shared-workspace attribution a scored, primary task** — i.e., "who said/decided X, in which team/project context," over a store written to by many identified parties whose vocabularies deliberately overlap. This is MASQ's positioning cell. The claim is deliberately narrow: it concerns a *benchmark axis*, not systems, datasets, or "long-term memory" broadly.

This page exists because the claim has its own lifecycle: it is falsified the day a benchmark ships this axis, and it must be re-verified before any paper submission.

## Evidence `[MEASURED]`

*Construct-validity note: "measured" = exhaustive keyword sweeps over 100%-read texts of the three closest neighbors + a ~15-benchmark breadth survey (2026-06-07). The construct is "published benchmarks discoverable via arXiv/web/survey indexes" — it cannot rule out unpublished or concurrent work; hence the refresh discipline below.*

- **Breadth:** ~15 benchmarks surveyed (LoCoMo, LongMemEval, MemBench, RULER, LTM-Benchmark, MSC, PerLTQA, MemoryArena, MemoryAgentBench, vendor evals, the 2025–26 enterprise-trace wave). Every one is single-user-dyadic or single-agent-in-environment. The 2026 surveys (arXiv 2512.13564, 2602.19320, 2602.06052) list multi-agent memory as an *emerging frontier*, not a benchmarked area.
- **Depth (verbatim reads; keyword sweeps at zero hits for speaker/attribution/multi-party terms):**
  - [LongMemEval](../source/wu-2024-longmemeval.md): formally a two-role dyad (§3.1); multi-party generation output is a *discarded failure mode* (§A.1). Its role axis is content-source (user-vs-assistant), not speaker identity.
  - [MemoryArena](../source/he-2026-memoryarena.md): single agent 𝒜/ℰ/ℳ (§3.2). Group Travel personas are *constraints to satisfy*, never authors to attribute.
  - [ATM-Bench](../source/mei-2026-atm-bench.md): single-owner first-person life-log (§3.1, §B.3). "Reference resolution" resolves entities in the owner's memory, not authorship.

## Distinctions that keep the claim precise

| Easily-conflated axis | Who has it | Why it is NOT this gap |
|---|---|---|
| Content-source (user-said vs assistant-said) | LongMemEval | Two fixed roles in one dyad; no identity among many parties |
| Constraint ownership (whose preference applies) | MemoryArena Group Travel | Personas constrain a plan; no query attributes an utterance |
| Entity-reference resolution ("Grace") | ATM-Bench | Referents *in* one person's data, not parties *writing* to a shared store |
| Temporal conflict resolution (newest wins) | ATM-Bench MUT | Recency, not authorship — and a confound MASQ must control |

A structural observation that explains the emptiness: the field conflates "multi-session" with "multi-party," and they are orthogonal — every multi-session benchmark is still single-party.

## Expansion (2026-06-08) — the gap is two-dimensional

The original claim is the *party* axis (attribution among many writers). The 2026-06-08 reframe ([masq-ab-factorial-design](../decision/masq-ab-factorial-design.md)) sharpens the occupied cell to **multi-party × temporal × decision-quality**:

- **Temporal:** the distinctive phenomena are cross-party decisions that *evolve* (supersession) or *collide* (a party acts unaware of another's prior decision). The static attribution axis is a control cell, not the headline.
- **Decision-quality (B-layer):** beyond "did it retrieve the right memory" (A), "did it take the correct *action* given that memory" (B). [Du 2026](../source/du-2026-autonomous-memory-survey.md) §5.1 calls for jointly assessing *memory quality and decision quality*; §9.6 names multi-agent memory governance and §9.10 standardized evaluation as unsolved — i.e. the field recognizes both halves of our cell as open.

This does not move the falsifiable core (no benchmark scores multi-party attribution over a shared store); it *adds* dimensions the neighbors also lack. [MemoryArena](../source/he-2026-memoryarena.md) has decision-quality (PS/SR) but single-agent; LongMemEval has temporal but dyadic. The intersection — decision-quality under cross-party temporal conflict — remains unoccupied.

**Training-side corroboration (2026-06-12, full-read verified).** [Mem-α](../source/wang-2025-mem-alpha.md) §3.4 — an RL-memory *training* paper — excludes conflict resolution from its training dimensions, verbatim: "excluding Conflict Resolution due to the lack of realistic evaluation benchmarks—existing datasets for this dimension remain predominantly synthetic and do not adequately capture real-world complexity." A third party stating, in print, that the conflict/supersession axis lacks a credible benchmark — independent support for the temporal leg of the gap, from the supply side (papers that *would train against* such a benchmark if it existed). The same cluster also bakes a recency-default reader into its harnesses ([Memory-R1](../source/yan-2025-memory-r1.md) Fig. 11; [Memory-R2](../source/yan-2026-memory-r2.md) Fig. 8: "prioritize the most recent memory") — the reader-policy confound MASQ's C3/C4 design holds fixed. Quote-grade material for the paper's positioning section.

**Temporal-leg qualifier (2026-06-12, full-read verified).** [STALE](../source/chao-2026-stale.md) (arXiv:2605.06527, May 2026) now occupies the **single-user** implicit-conflict cell: 400 scenarios where a later observation invalidates an earlier memory without explicit negation, probed via premise-resistance and downstream-behavior dimensions. The Mem-α quote (Sep 2025) must therefore carry a "since partially addressed by STALE" caveat when cited. The *multi-party* core claim is untouched — STALE is one user, one writer; its invalidation is mediated by commonsense world knowledge, MASQ's by another party's authority over a shared store, which STALE structurally cannot pose. Differentiation duty: MASQ's positioning must cite STALE and separate on the party axis. **Design-rationale asset from the contrast:** STALE has no negative controls (every instance contains a conflict; a blanket staleness bias scores well) — MASQ's C1/C2/C4 false-alarm arm with hit-vs-false-alarm discrimination is exactly the missing control, and is to be treated as load-bearing, not incidental.

## Why this matters

The entire MASQ paper claim ([decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md)) rests on this cell being empty — it is the load-bearing positioning fact for the program.

## Falsification & refresh discipline

- **Falsified by:** any published benchmark scoring speaker/team attribution over a multi-party shared store. Pre-registered response = reposition or fold (per the decision page), not push.
- **Refresh rule:** re-run the survey (at minimum: arXiv search + citing-work of the three survey papers) immediately before any submission or public claim. A 2026-06-07 verification has a short shelf life in this field.
- **Refresh log — 2026-06-12** (citation sweep of the RL-memory cluster, ~100 Memory-R1 citers + 15 Mem-α citers + arXiv keyword sweep): closest new neighbors checked — [STALE](../source/chao-2026-stale.md) full-read (single-user implicit conflict; qualifier above); MINTEval (arXiv:2605.18565; interference/updates robustness over multi-author *data* — Wikipedia revisions, GitHub commits — but no attribution task, abstract-level); LongMemEval-V2 (arXiv:2605.12493; single-agent environment-experience memory for web agents, abstract-level); plus a personalization-benchmark wave (PERMA, Personalize-then-Store, VitaBench 2.0 — all single-user). **Core claim stands: nothing scores multi-party attribution over a shared store.**

## Scope limits

- Says nothing about multi-agent *systems* (MAGMA et al. exist; they evaluate on single-user benchmarks — a naming collision, not a competing benchmark).
- Does not claim MASQ has the first multi-party *dataset* — meeting corpora exist; the gap is the scored attribution task over a memory store.

## Related

- [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md) (rests on this page)
- [source/wu-2024-longmemeval](../source/wu-2024-longmemeval.md), [source/he-2026-memoryarena](../source/he-2026-memoryarena.md), [source/mei-2026-atm-bench](../source/mei-2026-atm-bench.md)

## Source archive

Survey + verbatim-read notes: [masq/reads/](../../masq/reads/)
