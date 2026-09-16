---
type: source
name: "Mei et al. — According to Me: Long-Term Personalized Referential Memory QA (ATM-Bench)"
status: timeless
program: masq-bench
last_ingested: 2026-06-07
sources: []
tags: [masq, benchmark, memory-eval, anonymization]
---

## Citation

Jingbiao Mei, Jinghong Chen, Guangyu Yang, Xinyu Hou, Margaret Li, Bill Byrne. "According to Me: Long-Term Personalized Referential Memory QA." arXiv:2603.01990 (Mar 2026). **NB:** the Phase 0 survey agent mis-cited this as "arXiv 2606"; ID verified by title search 2026-06-07 — never trust secondary citations for IDs.

## Location

- https://arxiv.org/abs/2603.01990
- Code: https://github.com/JingbiaoMei/ATM-Bench

## Key claims (with our restatements)

### Single-owner, first-person life-log

**Paper:** §3.1: "retrieving and reasoning over **a user's** long-term, multimodal, and multi-source personal memories." §B.3 annotation rule: "Questions must be written as if asked by the photo owner ('Where did I…')." Fig 1A: reference resolution = "resolve the user's reference ('Grace') by linking to the user's past memory."

**Our restatement:** the closest surface-neighbor to MASQ ("referential memory") is orthogonal on the party axis — entities appear *in* one person's data; nothing *writes* to a shared store. Referent-resolution ≠ author-attribution. Anchors the [multi-party attribution gap](../concept/multi-party-attribution-gap.md).

### Conflicting evidence = temporal recency → MASQ design control

**Paper:** Fig 1(B): the model "resolves conflicts between booking records and finalized invoices, and prioritizes later-updated memory entries"; §F.1: failure mode = not "preferring the most recent and authoritative record."

**Our restatement (extrapolation, ours):** recency is the field's default conflict-resolution prior. **MASQ's conflicting-needle queries must vary author and recency independently**, or authorship effects are confounded with recency — pre-registered as a needle-design control in [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md).

### Real-data anonymization pipeline (template for our scrub)

**Paper:** §A.1: VLM risk screening (Qwen2.5-VL-7B + GPT-4o-mini) → automated face blurring → ~150 hrs manual redaction; emails: metadata stripping + **LLM paraphrase to remove linguistic fingerprints** + **synthetic PII injection** (dummy tracking numbers, fictitious addresses). §A.2: informed consent from contributors.

**Our restatement:** the published precedent for releasing real personal data in a memory benchmark — adopt this pipeline shape for the MASQ-v2 team-data scrub (screening → paraphrase → synthetic-PII → manual spot-check).

### Scale, scoring, headline

**Paper:** ~4 years of data; 6,741 emails / 3,759 images / 533 videos; 1,038 QA pairs (Table 2, §3.3). Hard split: avg 6.3 evidence items, evidence span avg 226 days, max 933 (§3.2–3.3). Scoring: answer-type-aware QS (EM/Jaccard/LLM-judge, §3.4 Eq. 2–3) and **Joint@k = QS × Recall@k** (Eq. 4). "<20% on Hard" = **Joint@10** (best: Mem0_Agentic 16.0, Table 3); Oracle GPT-5 on Hard ≈ 74.7 QS (Table 4).

**Our restatement:** when citing the <20% number, name the metric — it composes answer and retrieval quality; raw QS on Hard runs ~33–48.

## Important caveats

- "Contributors" (plural) is ambiguous in §A.2, but the task structure is strictly one owner's first-person memory — likely multiple separately-collected single-person corpora, not co-authors of one shared store.
- SGM (their system, §4.2) is per-item schema normalization (time/location/entities/OCR/tags); **no authoring-party field** — even their schema has no slot for the axis MASQ tests.

## Relevance to Kyrja

- Anchors [concept/multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) (most important kill-criterion check) and two commitments in [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md) (needle confound control; scrub pipeline).
- Paper-claimed: quoted material. Our extrapolations: the recency↔authorship confound implication; the scrub-template adoption.

## Audit history

2026-06-07, Nils (indigo): 100% read incl. appendices A–G via structured delegation (verbatim-quote contract; exhaustive keyword sweep — zero hits on speakermulti-party terms). Notes: [masq/reads/atm-bench-2603.01990-notes.md](../../masq/reads/atm-bench-2603.01990-notes.md).

## Archive location

arXiv 2603.01990 — re-fetch via arxiv MCP `download_paper`; verify quotes against §3.1/§A.1/§F.1 before cross-referencing.
