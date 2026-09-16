---
type: decision
name: MASQ paper as active program; Kerros parked
status: ACTIVE
program: masq-bench
last_ingested: 2026-06-08
sources: [../source/wu-2024-longmemeval.md, ../source/he-2026-memoryarena.md, ../source/mei-2026-atm-bench.md]
tags: [masq, benchmark, program-scope, kerros]
---

## Decision

MASQ becomes the active research program: an **independent multi-party memory-attribution benchmark paper** (arXiv preprint + workshop target). The Kerros write-side investigation ([incremental-integration-cost](../open-question/incremental-integration-cost.md), the caddy, the Ω(k²) desk-check) is **parked — reversible, sequencing not abandonment**.

## Motivation

- **Strategic (AJ, 2026-06-07).** The portfolio needs a *legible* research artifact first; MASQ is near-complete engineering in AJ's home idiom, and a benchmark is the most engineering-shaped genre in ML. Kerros' deep questions become the second act, stress-tested inside a community rather than solo.
- **The niche is real and bleeding.** Memory-system evaluation is dominated by vendors grading their own homework — the public Zep↔Mem0 dispute (same system scoring 58% vs 84% on LoCoMo depending on who runs the harness) is the field-level symptom `[ASSERTED — from vendor blog war; verify primary numbers before citing in the paper]`. SWE-bench's credibility model (independent authorship, pinned harness) has no memory-space occupant.
- **Phase 0 gates passed (2026-06-07).** (a) Kill criterion clean: no existing benchmark occupies the [multi-party attribution gap](../concept/multi-party-attribution-gap.md) — verified by verbatim reads of the three closest neighbors ([LongMemEval](../source/wu-2024-longmemeval.md), [MemoryArena](../source/he-2026-memoryarena.md), [ATM-Bench](../source/mei-2026-atm-bench.md)) plus a ~15-benchmark breadth survey. (b) Real-corpus feasibility: `/mnt/team-data/` probe found 2,653 sessions / ~553M tokens, fully ordered turns, needle-injection straightforward `[MEASURED — 2026-06-07 probe over Locke's indexes; construct caveat: scrub-prevalence estimates rest on a 5-session sample]`.

## Commitments

- **kyrja_* retrievers are removed from the benchmark** (AJ 2026-06-07): independence is the brand, and they wrap a system that is "ideas partially executed," not a built product.
- **Dual-corpus design:** existing synthetic 12-week-org corpus = controlled condition; team-data real corpus with injected ground-truth needles = ecological condition. Ranking-agreement between the two is itself a reportable finding. Real-corpus claim is scoped: *one* real ecology (all-Claude, single human user), characterized honestly.
- **Deterministic attribution scoring:** speaker/team answers are closed-set exact-match; LLM-judge only for open-ended answer text (anti-Zep/Mem0-dispute design; borrows [MemoryArena](../source/he-2026-memoryarena.md)'s decision-grounded SR framing).
- **Regeneratable private split:** generator + seeds documented; fresh-seed instances on demand (contamination-proof — the SWE-Rebench lesson).
- **Needle design controls author and recency independently** — [ATM-Bench](../source/mei-2026-atm-bench.md) shows recency is the field's default conflict-resolution prior; without the control, authorship effects are confounded.
- Working plan + sized punch list: [masq/phase1-breakdown.md](../../masq/phase1-breakdown.md). Benchmark code: canonical consolidation pending from the slate/red/amber copies under `/team-share/<colour>/kyrja/benchmark/masq`.

## Reframe (2026-06-08) — scientific rebuild over patch

AJ's "do the right science, unconstrain" pass moved the program from *attribution benchmark over the existing 12-week corpus* to a **statistically-defensible A+B factorial benchmark** — see [masq-ab-factorial-design](./masq-ab-factorial-design.md). What changed:

- **Scope widened from A to A+B.** Not just *memory quality* (who-said/decided-X attribution) but also **decision quality** (did the agent take the correct *action* given the memory) — operationalizing [Du 2026 §5.1](../source/du-2026-autonomous-memory-survey.md). The headline is the **party×time interaction on the B-layer**.
- **Multi-party → multi-party-*temporal*.** The distinctive cell is cross-party decisions that evolve/collide over time (supersession + unknowing-collision), not static attribution alone.
- **Corpus: rebuild, not patch.** [2026-06-08 audit](../experiment/2026-06-08-masq-corpus-audit.md) found ≈8 independent distinctive events — too few for subgroup claims. The "Deterministic attribution scoring / dual-corpus / regeneratable split / author-recency control" commitments above are **subsumed** by the factorial design (which keeps all of them and adds the B-layer, the within-items families, and pre-registration).
- **Reader → Opus** (`claude -p`, temp 0, pinned, cached) — budget constraint lifted; the prior gemma3:4b reader could not even attribute with oracle retrieval (audit).
- **Existing results discarded.** v1/v2 numbers are untrustworthy (broken reader, invalid token_f1, garbage mem0 ingest, 86% of queries unrun). AJ: happy to start from scratch.
- **Underlying claim made explicit (AJ):** *a vendor grading its own benchmark cannot expect to be believed* — the independence brand, not any specific replication number. See [benchmark-replication-gap](../concept/benchmark-replication-gap.md).

The Phase-1 punch-list ([phase1-breakdown.md](../../masq/phase1-breakdown.md)) is **paused** in favour of the rebuild; its reproducibility/judge items fold into the factorial design's pre-registration.

## Reversibility

**Cheap.** Kerros' resume point is fully preserved (NOW.md parked-threads section + project memory); nothing is deleted or unpublished. Reversal triggers: (a) a competing benchmark ships the attribution axis first → reposition or fold per the [gap page's](../concept/multi-party-attribution-gap.md) falsification clause; (b) the paper ships → Kerros resumes as planned; (c) Phase 1 reveals MASQ's gold answers are unsalvageable → revisit. The decision costs ~3–5 months of Kerros latency, which AJ priced in deliberately.

## Related

- [concept/multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) — the positioning claim this program rests on.
- [concept/kerros](../concept/kerros.md) — the parked program; resume threads recorded in NOW.md.
- Supersedes the "NEXT: none queued, AJ thinking" state of 2026-05-30; does NOT supersede any Kerros finding (Gate 1 stands).
