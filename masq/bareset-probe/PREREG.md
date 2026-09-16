# Bare-set boundary probe — PRE-REGISTRATION

**Date locked:** 2026-06-09 (Nils/indigo), BEFORE any reader ran.
**Question:** Gate 1 banned the "bare-set middle" — a second write "set X to Y"
carrying neither an explicit greenfield marker (→C3) nor a value-awareness
marker (→C4) — from the generated corpus, on the *hypothesis* that it is
genuinely ambiguous rather than merely hard. This probe tests that hypothesis,
and separately tests whether **presupposition verbs alone** ("raising/bumping
X to Y") are a sufficient legible awareness marker.

## Design

10 items, same classification prompt as gate 1 verbatim (comparability), new
domains (no gate-1 reuse):

- **6 truly-bare items** as **3 structure-matched pairs** (same logical
  skeleton, different domain/surface): launch-prep pair (#1,#7), external-
  requirement pair (#4,#9), new-workstream pair (#5,#10). Second write has NO
  awareness route (no prior-value reference, no symptom of current behaviour,
  no named person, no library-default mention) and NO greenfield claim.
  Hidden label: `BARE` — the epistemically correct answer is UNCLEAR.
- **2 whisper items** (#3,#8): the ONLY cue is a presupposition verb
  ("bumping…to", "raising…to" — presupposes a current value exists). Hidden
  label: SUPERSESSION per the locked value-awareness hinge (awareness "by any
  route"). These test whether the hinge's weakest natural marker is legible.
- **2 marked controls** (#2 explicit supersession, #6 explicit greenfield
  collision): attention checks; probe invalid if either reader misses either.

Readers: AJ blind by hand (`transcripts.md`); Opus pinned `claude-opus-4-8`
via `claude -p` (same as gate 1), run BEFORE AJ's pass but **sealed** to file
(`opus-results-sealed.json`, not printed) so AJ stays blind.

## Pre-registered predictions

P1. Controls: 2/2 both readers (else probe invalid, rebuild).
P2. **Opus forces labels on bare items**: UNCLEAR on ≤1 of 6 (gate-1 showed it
    resolves rather than escalates), with a **SUPERSESSION skew (≥4/6)** —
    the classification-form of the recency default (treat the later write as
    operative).
P3. **AJ**, now hinge-aware (contamination noted below), goes UNCLEAR on ≥4/6
    bare items.
P4. Whisper items: SUPERSESSION from both readers (2/2 each) — presupposition
    verbs are a sufficient marker.

## Decision rules (locked)

- **Ban CONFIRMED** if bare items fail to yield manufacturable ground truth on
  ANY of: (a) reader-vs-reader label agreement < 80% on the 6 bare items
  (UNCLEAR counted as a label), (b) either reader forces labels (UNCLEAR ≤ 50%)
  in a direction not derivable from the text, (c) within-pair inconsistency
  (same skeleton, different label) in either reader on ≥2 of 3 pairs.
  → bare-set stays banned as C3/C4 material.
- **Ban RELAXED-TO-RECLASSIFY** if both readers give UNCLEAR on ≥80% of bare
  items AND are pair-consistent: bare-set becomes admissible as a
  *designed-ambiguous* condition with GT = escalate/unclear — never as C3 or
  C4 ground truth.
- **Whisper rule:** if P4 holds (4/4), "presupposition verb" enters the C4
  generator marker vocabulary (soft marker, improves naturalness). If any
  miss, C4 markers must stay explicit (named-prior-value or named-person).

## Known contaminations / limitations (declared up front)

- AJ is no longer naive: he knows the value-awareness hinge and gate-1
  results. His UNCLEAR rate is an upper bound on a careful-informed reader,
  not an estimate of a naive one. Opus (same neutral prompt as gate 1, no
  hinge briefing) carries the naive-reader measurement.
- Builder = Nils (same as gate 1); the "truly bare" property is
  builder-judged. If a reader cites a textual awareness route I missed, that
  item is scored as authored-leak, reported, and excluded from the bare
  denominator (with the exclusion count reported).
- N=6 bare items: this gates a *generation rule*, not a population claim.
