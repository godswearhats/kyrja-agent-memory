---
type: hypothesis
name: H-QUAL-STRUCTURE — prose-format encoding beats slot-format
status: REJECTED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [encoding, format]
---

## Claim

Prose-format memory encoding (variant A: natural-language briefing for a future agent) beats slot-format encoding (variant C: structured fields like problem/cause/fix/test) on cost reduction.

**Status note.** REJECTED **in reverse**: the opposite direction (slots beat prose) holds with high confidence across two tasks and two distillers.

## What would falsify it

Slot-format (C) shows lower mean cost than prose (A) with disjoint 95% confidence intervals on a head-to-head run.

## Evidence for

None. The hypothesis was not supported.

## Evidence against

- Exp 1 (Task 2): C $0.142 vs A $0.247, −42%, CIs disjoint. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* cost as primary metric; both variants use the same source content distilled into different formats — direct format-vs-format comparison.
- Exp 2 (Task 3): C $0.805 vs A $1.105, −27%, CIs disjoint. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* same as above.
- Direction holds across two tasks and two distillers (Opus 4.7 and Opus 4.6).

## Open sub-questions

- **Why does slot format win?** Candidate mechanisms, none falsified: (a) lower input-side token cost; (b) less semantic noise; (c) easier to pattern-match against the current task; (d) doesn't trigger summary-style attention dispersion. Worth disentangling for MTP design — if (a) dominates, an even more compressed format may win further.
- Does the win hold under **adversarial slot-fields** (wrong field names, missing fields)? Robustness boundary unknown.
- Does the win hold when the agent **cannot tell** the memory is slot-formatted (e.g., serialized as flowing text at injection time)?

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — evidence anchor.
- [H25-replicate](./H25-replicate.md) — confirms the format-direction across tasks.
- [H23-util](./H23-util.md) — parent claim that one of the formats reduces cost.
- slot-format encoding for memory (pending atomization; rests on this and H25).
