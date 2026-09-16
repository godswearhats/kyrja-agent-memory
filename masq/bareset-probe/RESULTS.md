# Bare-set boundary probe — Result: BAN CONFIRMED (decisively)

**Date:** 2026-06-09 (Nils/indigo). Readers: AJ (blind, hand) + Opus 4.8
(pinned, sealed before AJ's pass). Pre-registration: `PREREG.md` (locked before
any reader ran). Scoring: `score.py`.

## Headline

**The bare-set middle cannot carry C3/C4 ground truth. Reader agreement on the
6 truly-bare items: 0/6 (0%).** Not "hard" — *illegible*: two careful readers
applied contradictory inference rules and never once produced the same label.
All three ban-confirmation sub-rules fired; only one was needed:

- (a) AJ⟷Opus agreement 0% (threshold 80%).
- (b) Opus forced labels (UNCLEAR 0/6) in directions not derivable from text.
- (c) AJ pair-consistent on only 1/3 matched pairs.

Controls 2/2 for both readers (probe valid). Full table in `score.py` output.

## Pre-registered predictions, scored honestly

- **P1 controls 2/2 both: PASS.**
- **P2 Opus forces labels (UNCLEAR ≤1/6): PASS (0/6). Direction: FAIL** — I
  predicted a SUPERSESSION/recency skew; Opus actually went **COLLISION 4/6**.
  The recency-default does not generalize to Opus's *classification* of
  unmarked items; its rule is "no stated awareness route → unaware →
  collision" (absence of evidence read as evidence of absence).
- **P3 AJ UNCLEAR ≥4/6: PASS (4/6).**
- **P4 whisper 4/4 SUPERSESSION: PASS** — presupposition verbs ("bumping/
  raising X to Y") are a legible awareness marker for both readers.

## What the disagreement is made of (the real finding)

The two readers keyed on **different awareness routes**, and one invented one:

- **AJ** treated **purpose-clause presuppositions** as awareness: #9 ("so the
  lease outlives an encode") and #10 ("so shoppers aren't logged out
  mid-browse") presuppose a current too-short value → SUPERSESSION.
  **Mechanism CONFIRMED by AJ post-hoc (2026-06-09):** "the reasoning was given
  in a way that led me to believe they knew the current value, so I inferred
  this was an update to an existing value, rather than setting one arbitrarily." Where the
  purpose clause was requirement-stated (#4 "auditors want a quarter") or he
  didn't register the presupposition (#1, #5, #7), he went UNCLEAR.
- **Opus** treated the same kind of presupposition as awareness on #1 ("burst
  capacity ... against the existing baseline") but NOT on #9/#10 (read as
  fresh/independent → COLLISION), and on **#7 it fabricated an awareness route**
  ("explicitly changes it" — the text contains no reference to an existing
  value). A model reader, given an unmarked item and no UNCLEAR appetite,
  will confidently hallucinate intent evidence.

So "truly bare" is **nearly impossible to author**: purposive language almost
inevitably presupposes a baseline (comparatives, counterfactual-present
clauses), and readers disagree wildly — and inconsistently with themselves —
about which presuppositions count as awareness. That is precisely why the
generated corpus must never rely on this register for ground truth.

## Consequences for the generator (locked)

1. **Bare-set ban CONFIRMED** as a generation invariant: every two-writer item
   carries either an explicit greenfield marker (C3) or an explicit
   value-awareness marker (C4). No unmarked middle, ever.
2. **Whisper verbs admitted as C4 *soft* markers** (P4: 4/4): "raise / bump /
   lower / increase X to Y" may carry C4 naturalness; the *primary* C4 marker
   stays explicit (named prior value, named person, symptom, or default).
3. **NEW — presupposition scrub for C3 reasons.** C3 second-write purpose
   clauses must be **absolute / requirement-stated** ("the auditors want a
   full quarter of history"), never baseline-presupposing: no comparatives
   ("fewer", "more headroom"), no counterfactual-present ("so X doesn't keep
   happening", "aren't logged out mid-browse"), no capacity-relative framing
   ("burst capacity"). These constructions read as awareness routes to some
   readers and not others — exactly the ambiguity the marker is supposed to
   override. Reserve them for C4.
4. **Generator QA check:** sample generated C3 items and verify readers don't
   extract an unintended awareness route from the purpose clause (the #1/#7
   failure mode, authored by me despite trying not to).

## Files

`PREREG.md` (locked first) · `build.py` · `transcripts.{json,md}` · `key.json`
(hidden) · `aj-answers.md` · `run_opus.py` (sealed mode) ·
`opus-results-sealed.json` · `score.py` · this file.
