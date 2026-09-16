# MASQ prose-realism pass — protocol (Nils ⇄ Maren)

**Status:** DRAFT 2026-06-10 (Nils/indigo), awaiting AJ approval before handoff.
**Implements:** README "Next #1". Roles per the standing workflow: Nils owns
schema + structural QA, Maren (purple) owns prose, AJ spot-checks legibility.

---

## 1. Goal and non-goals

**Goal:** replace v0's template-flat surface text with realistic, varied,
multi-paragraph session prose — for distractor credibility and to make the
volume knob meaningful (README limitation #2) — while provably preserving
every generation invariant on the **emitted** text.

**Non-goals:** no change to world structure (facts, values, writers, days,
timelines), no change to kernel semantics, no intra-write "messy phrasing"
noise arm (that is the named v2 external-validity arm, c4 family doc attack #9).

## 2. Threat model — what a prose pass can silently break

The bare-set probe is the controlling evidence here: *authorial care leaks*,
and purposive prose almost inevitably presupposes a baseline ("so shoppers
aren't logged out" reads as awareness of a current value). A well-meaning
prose pass is therefore the single most likely place for ground truth to
corrode. Specific failure classes:

- **T1 marker corrosion** — paraphrasing weakens an awareness/greenfield
  marker below legibility (probe: readers disagree wildly on which
  presuppositions count as awareness).
- **T2 awareness injection into C3** — added colour ("given how the sale went
  last year…", comparatives, counterfactual-present clauses) creates an
  awareness route where GT says greenfield.
- **T3 keyword keys** — if every supersession says "Saw X set…", the marker
  itself becomes a retrievable signature (family doc attack #9).
- **T4 token drift** — paraphrasing "rate limit" → "throttle cap" breaks I3
  recurrence; the confusability argument needs the tokens to recur.
- **T5 spurious fact-value pairings** — invented numbers ("bumped /search to
  450 last sprint") create writes that exist in prose but not in GT.
- **T6 phantom cross-references** — "as Priya said yesterday" creates an
  unmarked apparent awareness route between writers.
- **T7 kernel-focused care** — if the prose author knows which fact is scored,
  care concentrates there and becomes a key (the bare-set probe's lesson in
  authorship leakage).

## 3. Core design decision: the locked-sentence model

Each session's text is split into **one locked sentence** (the structural
write/marker content, generator-authored) **plus free prose** (Maren-authored)
around it.

- The generator emits, per session, a `locked` sentence and a constraint card
  (§5). Maren may position the locked sentence anywhere in the session body
  but must reproduce it **verbatim**.
- Marker *variety* is therefore a **generator-side** job: the marker banks in
  `embedding.py` get widened (≥6 phrasings per marker class, seeded choice) so
  T3 is solved without ever letting prose touch marker semantics (T1/T2).
- Chatter sessions (`chatter_*`) have no locked sentence — only locked tokens
  (the (fact, value) pair for value-chatter) and the global bans.

Rationale: the probe showed that even a careful author writing *structured*
items leaked presuppositions. Free re-expression of marker semantics by a
prose-focused author is strictly riskier, and verbatim locked sentences make
I4/I4b verification exact instead of taxonomic. The cost — a slightly stilted
seam between locked sentence and surrounding prose — is acceptable at v1 and
is invisible once session shapes vary (§6).

## 4. Blinding

Maren is **not told which fact is the kernel**, which sessions are kernel
writes, or that cells/scoring exist. She receives one flat list of sessions
(world + the 5 distinct kernel sessions mixed in), each with the same shape of
constraint card. Kernel sessions are not distinguishable by card shape:
sibling supersessions also carry locked marker sentences, sibling initials
also carry locked write sentences. This neutralises T7.

(She may infer *something* is special if she studies value collisions across
the file; the instructions ask her to treat sessions independently, and
structural QA + the emitted-legibility recheck are the backstop.)

## 5. The handoff artifact

`handoff.json`: a list of session objects, each:

```json
{
  "id": "s041",
  "writer": "Priya",
  "day": 12,
  "shape": "incident-comment",        // requested session shape, §6
  "target_length": "2-3 paragraphs",
  "locked_sentence": "Saw Marcus set /reports rate limit to 200 req/s. ...",
  "locked_tokens": ["/reports", "rate limit", "200 req/s"],
  "free_prose_rules": "global rules apply (see instructions doc)"
}
```

Maren returns the same JSON with one added field per session: `"prose"` (the
full session body, containing the locked sentence verbatim). Nothing else may
change. Re-rendering and recomposition into the four cells stays on the Nils
side, so the matched-family property (world byte-identical across cells,
kernel S1 shared verbatim) holds **by construction**, not by Maren's care.

## 6. Variation plan (what Maren owns)

1. **Personas:** one voice sheet per writer (16 writers), designed by Maren —
   register, verbosity, tics, punctuation habits. Consistent per writer across
   sessions. (Voice binds to *writer*, which is already metadata, so it adds
   realism without adding a fact-binding key.)
2. **Session shapes**, assigned per-session by the generator from a target
   mix: standup note, incident comment, change-record description, channel
   message, handoff note, retro fragment.
3. **Length:** 1–4 paragraphs per the card; this is what turns the volume
   knob into real token mass.
4. **No verbatim repeats:** no two session bodies identical (the v0 complaint).

## 7. Global free-prose rules (the bans, stated for Maren)

1. The locked sentence appears **verbatim, exactly once**, unmodified.
2. **No numbers attached to endpoints or settings** anywhere in free prose —
   no config values, limits, quotas, percentages-of-traffic for any `/path`.
   (Dates, times, ticket numbers, meeting times are fine.) [kills T5]
3. **Never paraphrase or restate** the locked sentence's content elsewhere in
   the session — no "in other words, the limit is now…". [kills T1]
4. **No references to other people's changes or settings** outside the locked
   sentence — no "as X mentioned", "following Y's change", "like we discussed".
   Own prior work may be referenced only generically ("my earlier cleanup").
   [kills T6]
5. **No purpose clauses about settings** in free prose — don't explain *why* a
   value was chosen beyond what the locked sentence says; colour goes to
   process, scheduling, people, and unrelated work instead. [kills T2 — this
   is the probe's central lesson: purposive language presupposes baselines]
6. Locked tokens (endpoint names, "rate limit", value+unit) may be *mentioned*
   in free prose only if they already appear in the locked sentence of the
   same session, and never with a different value.

## 8. Verification & QA loop (Nils side, all on emitted text)

Pre-handoff, `verify.py` is upgraded to be template-agnostic:

- **I4/I4b** check locked-sentence presence **verbatim** (from `handoff.json`)
  instead of the current `"Saw {prev} set"` template regex; marker-bank
  membership is checked at generation time against the widened banks.
- **New I6 (spurious-pairing scrub):** in every emitted session, any
  `<number> req/s`-style value co-occurring with an endpoint token must match
  an allowed (fact, value, ≤day) tuple from the world spec. Catches T5
  mechanically rather than by trust in rule §7.2.
- **New I7 (cross-reference scrub):** regex screen of free prose for
  cross-writer reference constructions (names + said/set/changed/mentioned/
  agreed) outside locked sentences. Screen-then-eyeball, not auto-fail.
- **New I8 (off-kernel collisions, c4 doc §8.3):** the shared world carries
  1–2 marked sibling collisions, unreconciled, excluded from value-chatter,
  never the kernel fact. Lands in `embedding.py` BEFORE the handoff — their
  locked greenfield sentences are one more reason kernel sessions aren't
  distinguishable to Maren (§4).
- **Diff audit:** only `prose` added; `writer`/`day`/`locked_sentence`
  untouched; no session bodies identical.
- Existing I1–I3, I5 re-run unchanged on the re-rendered corpora.

**Iteration rule:** failures go back to Maren as tightened constraint cards,
≤2 rounds. Nils never hand-fixes prose (provenance: all prose is Maren's, all
structure is the generator's — that separation is what we report in the paper's
construction section).

## 9. Pilot scope & acceptance criteria

Pilot = the 8-sibling demo family (seed 109), ~60 sessions. Accept when:

1. `verify.py` (upgraded) all-pass on the rewritten family, all four cells;
2. diff audit clean; zero identical session bodies;
3. token mass per cell grows ≈3–5× (≈1.1k → 3–5k tokens at 8 siblings);
4. **mini legibility check:** fresh pinned-Opus read of the emitted C3 and C4
   kernels in prose form, plus 4 marked sibling supersessions — all classified
   correctly. (This is a smoke test only; the full emitted-legibility recheck
   — README limitation #5 — runs after domain packs land, on a proper sample.)

Then: same protocol, no changes, for domain packs 2–3.

## 10. Open risks carried forward

- Locked-sentence seams may read as stilted; if AJ's spot-read says so, the
  v1.1 relaxation is letting Maren lightly inflect locked sentences under a
  bank-membership (not verbatim) check — only after the mini legibility check
  has a baseline.
- Maren's compliance with §7.5 (no purpose clauses) is the rule most likely to
  chafe against narrative instinct; I6/I7 + spot-reads are the net.
