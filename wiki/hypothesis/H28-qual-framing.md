---
type: hypothesis
name: H-QUAL-FRAMING — briefing framing beats summary framing
status: PROPOSED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [encoding, framing, underpowered]
---

## Claim

Briefing-style encoding (variant A: imperative instructions to a future agent — "you will encounter X; do Y") beats summary-style encoding (variant B: retrospective narration — "the agent found X and did Y") on cost reduction.

**Status note.** PROPOSED. Exp 1 data is suggestive in the *opposite* direction (B trends lower than A) but underpowered at n=4 with overlapping CIs. Not enough evidence to reject; not enough to support.

## What would falsify it

Any of: B shows lower cost than A with disjoint CIs (rejects in reverse); A and B show indistinguishable cost at adequate n (rejects by null result); or A is consistently elevated vs B across multiple tasks.

## Evidence for

None beyond the loose intuition that imperative framing maps more directly to next-action selection in an agent loop. Untested.

## Evidence against

- Exp 1 (Task 2): B $0.200 vs A $0.247. B trends **cheaper**, opposite to the hypothesis. 95% CIs **overlap** at n=4 (B [0.139, 0.281] vs A [0.215, 0.279]). `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* cost metric is valid; the CI overlap is the load-bearing concern, not the metric.
- Not replicated in Exp 2 (which only tested A and C, not B).

## Open sub-questions

- **Power.** What n is needed to distinguish A and B at the observed effect size? Rough estimate: if true effect is ~$0.047 with pooled SD ~$0.05, n≈8-12 per arm gets reasonable power. Cheap to run if worth doing.
- **Is framing dominated by structure?** Since slot-format (C) wins by a far larger margin than any framing comparison, framing differences may be irrelevant in production — the wedge will use C regardless. Open question whether resolving framing is worth the cost.
- **Re-examine framing within the slot regime.** "Briefing slots" vs "summary slots" is a different comparison than briefing prose vs summary prose. Untested.

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — Exp 1 only; Exp 2 did not test framing.
- [H27-qual-structure](./H27-qual-structure.md) — the format question that probably dominates this one.
- [H23-util](./H23-util.md) — parent claim about memory utility.
