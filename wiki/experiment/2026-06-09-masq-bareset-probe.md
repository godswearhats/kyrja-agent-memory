---
type: experiment
name: MASQ bare-set boundary probe (2026-06-09)
status: LANDED
program: masq-bench
last_ingested: 2026-06-09
epistemic_tags: [MEASURED]
tags: [masq, benchmark, gate, construct-validity, bare-set, presupposition]
---

Follow-up probe to [gate 1](./2026-06-08-masq-gate1-c3c4-discriminability.md),
pre-registered before any reader ran (`PREREG.md` in the artifact dir): is the
**bare-set middle** — a second write "set X to Y" with neither a greenfield
marker nor a value-awareness marker — genuinely ambiguous, justifying gate 1's
generation ban? **Result: ban CONFIRMED, decisively — reader agreement on bare
items was 0/6 (0%).** A secondary arm validated presupposition verbs
("raising/bumping X to Y") as legible C4 markers (4/4).

## Hypotheses tested

- Gate-1 invariant #4 ("ban the bare-set middle") rests on: *bare-set items
  cannot yield manufacturable C3/C4 ground truth.* **Verdict: supported,
  via all three pre-registered sub-rules** (agreement 0% < 80%; Opus forced
  labels, UNCLEAR 0/6, in non-text-derivable directions; AJ pair-consistent on
  only 1/3 matched pairs).
- Secondary: *presupposition verbs alone are a sufficient awareness marker.*
  **Supported (4/4 across both readers).**

## Method

10 items, gate-1 classification prompt **verbatim** (instrument held fixed so
behavior changes attribute to items, not instructions; gate 1 is the
calibration). New domains, no gate-1 reuse. 6 truly-bare items as 3
structure-matched pairs (within-reader consistency measure), 2 whisper items
(presupposition verb as only cue), 2 marked controls (attention check — both
readers 2/2, probe valid). Readers: AJ blind by hand; Opus 4.8 pinned via
`claude -p`, run **sealed** (results to file, unprinted) before AJ's pass to
preserve his blindness. Predictions and decision rules locked in `PREREG.md`
before either reader ran.

## Results `[MEASURED]`

- **Bare items: AJ⟷Opus agreement 0/6.** AJ: UNCLEAR 4/6, SUPERSESSION 2/6.
  Opus: COLLISION 4/6, SUPERSESSION 2/6, UNCLEAR 0/6 — never once the same
  label on the same item.
- **Pre-registered direction miss, reported honestly:** I predicted Opus would
  skew SUPERSESSION (recency-default). It skewed **COLLISION** — its rule is
  "no stated awareness route → unaware → collision" (absence of evidence read
  as evidence of absence). The recency-default does not generalize to Opus's
  classification behavior on unmarked items.
- **Mechanism of disagreement:** the readers keyed on different
  **purpose-clause presuppositions** as awareness routes (AJ: "so shoppers
  aren't logged out mid-browse" → aware — mechanism confirmed by AJ post-hoc;
  Opus: "burst capacity" → aware), each
  inconsistently with themselves across matched pairs — and on one item Opus
  **fabricated** an awareness route ("explicitly changes it" where the text
  references no prior value). Unmarked items make a no-UNCLEAR model reader
  hallucinate intent evidence.
- **Whisper arm:** "bumping/raising X to Y" → SUPERSESSION 4/4.

### Construct validity

Agreement between two careful readers on builder-authored items measures
whether bare-set ground truth is *manufacturable*, not the natural prevalence
of collisions vs supersessions. 0% agreement with valid controls is the
strongest available evidence of non-manufacturability at this N; N=6 bare
items gates a generation rule, not a population claim.

## Consequences (locked into the generation spec, family §7.4)

1. Bare-set ban **confirmed** as a hard generation invariant.
2. Presupposition verbs admitted as C4 **soft** markers (primary C4 marker
   stays explicit).
3. **New invariant — C3 presupposition scrub:** C3 purpose clauses must be
   absolute/requirement-stated; no comparatives, counterfactual-present
   clauses, or capacity-relative framing (these read as awareness routes to
   some readers and not others). Reserve them for C4.
4. Generator QA must sample C3 items for unintended awareness routes — the
   builder (me) leaked presuppositions into 2/6 "bare" items despite actively
   trying not to, so generated text will too.

## Limitations

- AJ hinge-aware (declared in PREREG; his UNCLEAR rate is an informed-reader
  upper bound; Opus carries the naive-reader measurement).
- Builder-judged "bareness" failed twice (#1, #7 leaked presuppositions by
  Opus's reading) — which is itself the finding, but means the bare/whisper
  boundary is fuzzier than the item taxonomy implies.
- Single Opus sample per item (deterministic-ish `claude -p`); no
  self-consistency replicates.

## Raw artifacts

- `masq/bareset-probe/` — `PREREG.md`, `RESULTS.md`,
  `build.py`, `transcripts.{json,md}`, `key.json`, `aj-answers.md`,
  `run_opus.py`, `opus-results-sealed.json`, `score.py`.

## Related

- Confirms invariant #4 of [gate 1](./2026-06-08-masq-gate1-c3c4-discriminability.md);
  adds invariants 2–4 above to the generation spec
  (`masq/c4-worked-family.md` §7.4).
- Updates the generation commitments in
  [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md).
- Clears the path to the **confusable-sibling embedding** build (generation
  rules now frozen).
