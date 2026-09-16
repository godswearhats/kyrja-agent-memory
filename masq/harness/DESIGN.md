# MASQ oracle/baseline harness — design (v0 draft, 2026-06-10)

> **PARTIALLY SUPERSEDED 2026-06-26 by `DESIGN-v2-analysis.md`.** §5 (statistics)
> and §6 (reference-size fork) were written for the v1 2×2 party×time factorial
> — the MASQ-score-as-all-4-cells metric, the ΔΔ interaction contrast, and the
> multi-model-averaged reader. v2 uses multi-scope confusability chains (no
> cells, single decision/scenario), a **single fixed Opus reader** (the held-
> constant probe; multi-model is now a stretch appendix), per-arm B-pass with
> paired McNemar as the headline, and size reported with no predicted shape.
> The **harness mechanics** in §1–§4 (one-function score, the MemoryAdapter
> `ingest`/`deliver` contract, frozen reader/queries/grading, parse discipline,
> sanity gates) remain current. Read `DESIGN-v2-analysis.md` for the live
> analysis pre-registration.

**Status:** DRAFT — awaiting AJ approval before implementation.
**Honors:** `../c4-worked-family.md` §3 (GT), §4 (stats), §7 (B rubric,
preamble, reader), §8 (naming, MASQ score, I8). Reader = multiple
frontier models (see §1), results averaged; identical across arms.

## 1. What the harness is

One function, run many times:

```
score(scenario, cell, arm, size, model) :
    corpus  = rendered cell corpus at `size`           (generator output)
    context = arm.deliver(corpus, query)               (the memory system)
    answers = reader(PREAMBLE + query, context, model) (frozen call, temp 0)
    return   grade(answers, scenario.ground_truth)     (exact-match, closed)
```

Everything that varies between memory systems is inside `arm.deliver`. The
reader, queries, preamble, parsing, and grading are frozen and identical.
That is the §7.2 rationale: B probes **what memory delivered**, nothing else.

**Reader models.** Results are computed per-model and then averaged. The
headline MASQ score is the mean across models; per-model breakdowns are
reported as diagnostics. Model is a nuisance variable we average over, not
a fixed parameter — the claim is about the *task*, not one model's quirks.
Initial model set (pre-registered before any system run):

- `claude-opus-4-8` (Anthropic, 1M context)
- `claude-sonnet-4-6` (Anthropic, 1M context)
- at least one non-Anthropic frontier model (TBD; same 1M-class window)

All frontier models currently ship with 1M context windows. The harness
assumes all corpus sizes fit within the reader window (no truncation at
any sweep point). See §6 for implications.

## 2. Arms

| arm (public name) | `deliver(corpus, query)` returns |
|---|---|
| **paste-everything baseline** | the whole cell corpus, verbatim (identity memory). Also the volume-sweep arm. |
| **last-write-wins** | the single most recent session that writes the queried fact (mechanical stub, no LLM). Designed signature: C1✓ C2✓ C3✗ C4✓ → MASQ 0%. |
| **perfect-retrieval ceiling** | the faithful GT memory state rendered as text: every kernel-fact write with writer/day/marker — *contested, never pre-resolved* for C3 (§7.3). Normaliser for reader competence. |
| **memory system under test** | via the adapter API (§3). |

Sanity gates (pre-registered, run before any system comparison):
- ceiling must pass B in ≥90% of scenarios per cell — else the construction
  or rubric is broken, stop;
- last-write-wins must show exactly the designed signature — else the
  generator or grader is broken, stop.

## 3. Memory-system adapter API

Streaming, matching real deployment — a system never sees the corpus as one
blob:

```
class MemoryAdapter:
    def ingest(self, session: dict): ...   # called once per session, in day order
    def deliver(self, query: str) -> str:  # context string for the reader
```

Sessions are the generator's emitted objects (id/writer/day/prose). The
adapter may do anything internally (embed, summarize, graph, call its own
LLMs) but the *reader* it must convince is ours. Paste-everything and
last-write-wins are trivially expressed in this API; ceiling bypasses
ingest (it is handed GT — that's the point).

## 4. Queries, output format, parsing

Two reader calls per (scenario, cell, arm):

**A-query (Memory score)** — domain-parameterized from the family JSON:
*"As of now, what is the {kernel fact} {param}? Who set the current value?
Was it ever changed — if so, from what, by whom?"* Answer format, one line
per field, closed-set:

```
CURRENT_VALUE: <value|contested>
CURRENT_SETTER: <name|contested>
WAS_CHANGED: <yes|no|n/a>
PRIOR_VALUE: <value|n/a>
PRIOR_SETTER: <name|n/a>
```

A-score = mean exact-match over the cell's applicable fields (§3 of the
family doc); `contested` first-class in both directions.

**B-query (Decision score)** — the §7.3 uniform preamble verbatim on every
item, then the action task with the cell-agnostic menu from the domain pack.
Answer format:

```
ACTION: <menu item>
CONFLICT: <true|false>
```

B pass per §7.2: C1/C2/C4 = correct action ∧ ¬flag; C3 = flag (action
recorded, unscored; logged as the descriptive policy tier).

Parsing: strict regex (the `mini_legibility.py` pattern). One re-ask on
PARSE_FAIL with a format reminder; second failure scores as fail and is
logged. Pre-registered: parse failures are failures, never excluded.

## 5. Scoring & statistics (pre-registered)

- **Headline: MASQ score** = % scenarios solved (all four cells pass B), per
  arm (§8.2). Reported raw and ceiling-normalised.
- **Diagnostic table:** per-cell B rates (public names), collisions caught,
  false alarms, A-layer composite per cell.
- **Significance (primary):** per-scenario paired interaction contrast
  ΔΔ = (C4 − C3) − (C2 − C1) on B pass; permutation test (10k shuffles of
  cell labels within scenario), pre-registered α = .05, one-sided in the
  predicted direction for the memory-system-vs-baseline comparison.
- **Confirmatory:** logistic GLMM `B ~ party*time + (1|scenario)` — reported,
  not load-bearing (50 binary obs/cell is thin for GLMM asymptotics; the
  permutation test carries inference).
- **Exploratory only:** per-domain breakdown (no confirmatory domain claims
  in v1 — see fork 2).
- **Repeated-call variance check (pre-registered; added 2026-06-12, AJ
  approved; protocol borrowed from STALE App. E.2, arXiv:2605.06527):**
  reader calls are temp-0 but serving-side nondeterminism is real. Fixed
  subset = 2 scenarios × 4 cells × 3 arms (paste-everything,
  perfect-retrieval ceiling, system under test) at reference size; 5
  repeated reader calls per (item, model); report per-dimension mean±sd and
  confirm the headline findings (interaction direction, sanity-gate
  outcomes) hold in **every** run, not just on average. ~720 extra reader
  calls (~7% of budget). Run during the sweep pilot, before the N=50
  headline run. If overall sd exceeds 5 percentage points, raise with AJ
  before proceeding (sample size or seed-averaging may need revisiting).

Grading-robustness note (rationale, 2026-06-12): grading stays closed-form
exact-match over the structured `(action, conflict_flag)` output — no LLM
judge anywhere in scoring. This is deliberate: STALE's LLM-judge protocol
required a 240-response human-agreement study (95.8% agreement) to be
trusted; closed-form grading avoids that burden entirely. Pre-registered
consequence: if any open-ended grading ever enters the harness, a
STALE-style stratified human-agreement study (with error-direction check —
judge must deflate, not inflate) becomes mandatory before results are
reported.

Goalpost tells (pre-registered, per our own rules): changing reference size
after seeing system scores; dropping a domain or scenario post-hoc;
reclassifying parse failures; promoting the exploratory domain breakdown to
a claim.

## 6. Fork 1 — reference corpus size & sweep points (DECIDED: 60k provisional)

**Reference size = ~60k tokens/cell.** Headline MASQ scores and the
interaction test are computed here, for every arm. Rationale: (a) an order
of magnitude above the pilot (6k), enough chatter/sibling mass for
confusability to bite; (b) comfortably inside the reader's context, so
paste-everything is a *fair, strong* baseline at reference — its failures
are confusability failures, not truncation artifacts. Fixed now, before any
system run (goalpost insurance).

**Sweep = {6k, 25k, 60k*, 150k, 400k} tokens/cell**, log-spaced, 12
scenarios (4/domain), paste-everything + systems (no point sweeping
last-write-wins; ceiling is size-invariant by construction).

**Context window assumption.** All frontier reader models currently have 1M
context windows. Every sweep point fits within the window — paste-everything
is never truncated at any size. This is by design: the sweep measures
**confusability-driven degradation**, not overflow. As corpus grows, sibling
mass and temporal noise increase while the kernel signal stays constant. The
hypothesis is that paste-everything fails because the reader cannot
disambiguate the kernel entity from its confusable siblings, and cannot
detect conflicts from chronological noise alone — not because the corpus
was cut off. Showing that paste-everything fails *even when it fits* is
the stronger and more novel claim.

**Escalation gate (pre-registered).** If paste-everything passes B at ≥85%
across cells in the 12-scenario sweep pilot, the confusable siblings are
not doing their job at current density. Response: increase sibling density
(8 → 20+ per domain, with names/values deliberately closer to the kernel
entity) and re-run before proceeding to N=50. This is a construction fix,
not a goalpost move — the benchmark must be hard enough to differentiate.

Generator implications (known): widen entity pools (32 → ~200 per domain)
and `--days` (28 → 180) before 60k+ worlds; both are pack-registry edits,
no schema change.

## 7. Fork 2 — pooled vs domain-stratified power (DECIDED: pooled)

**Pooled: 50 scenarios, ~17 per domain, domain as exploratory breakdown.**
The v1 claim is "memory systems fail the party×time interaction", not "…in
every domain"; ≥3 domains exist to rule out a numeric-only artifact (§5
attack #10), which the pooled design already does. Stratified power
(50/domain = 150 scenarios, ~30M stored tokens) triples cost to support a
domain-level claim we are not making. Decision rule if the pilot disagrees:
should the 12-scenario sweep pilot show ceiling-arm B differing by >20pp
across domains, that's a construction problem to fix — not a reason to
triple N.

## 8. Fork 3 — atom-bank composition (DECIDED: fine-grained, multi-layer)

Hand-drafted prose stops at ~10M tokens (~90k sessions). Amendment: push
the authoring grain to **sentence level** and let the generator compose
upward through multiple layers to defeat pattern-matching.

**Layer 0 — Atoms** (~50–60 per writer, 800–960 total across 16 writers):
sentence-level units. Each is persona-true, fact-agnostic, a complete
thought. Examples: "Finished the morning deploy check." / "Retrospective
ran long, good discussion though." The existing hard rules (no values, no
settings, no cross-references in free prose) apply identically to atoms.

**Layer 1 — Compound sentences**: generator pairs 2 atoms with a sampled
connective/transition (~20–30 connectives authored by Maren). ~2,400
ordered pairs per writer — no compound sentence repeats at corpus scale.

**Layer 2 — Paragraphs**: 2–3 compound sentences, count varied per session.
Millions of distinct paragraphs per writer.

**Layer 3 — Session body**: 1–2 composed paragraphs wrapped around the
locked sentence (which stays verbatim, exactly once). The locked sentence
is the only recognisable repeated element — by design.

At sentence grain, atoms are too small to pattern-match. A recurring clause
embedded in a different compound sentence, different paragraph, different
session is below the recognition threshold.

Maren's authoring task: ~50–60 atoms/writer + ~20–30 connectives. More
items than paragraph-level blocks, but each is one sentence — arguably
faster to write. Generator handles all composition under seeded RNG.

- **Acceptance gate (pre-registered):** compose one full cell; verify.py all
  pass; mini-legibility vs the hand-drafted demo-prose cell (no degradation
  on kernel tier); spot-read by AJ for obvious template smell.

Maren's effort shifts from O(corpus) to O(bank) — one authoring task,
reusable across all sizes and seeds.

## 9. Cost & mechanics (flagged, not self-policed)

Reader calls at reference (per model): 50 scenarios × 4 cells × 2 queries
× 5 arms ≈ 2,000. Sweep adds ≈ 12 × 5 sizes × 4 × 2 × 3 arms ≈ 1,440.
Multiply by number of reader models (initially 3) for totals: ~6,000
reference + ~4,320 sweep ≈ **10,320 reader calls**. Input tokens dominated
by paste-everything at 150k/400k; ≈90M reader-input tokens per model
pre-caching (~270M total across 3 models), with prompt caching cutting most
of it (corpus prefix shared between the A and B call per (cell, arm, size,
model)). Concurrency 4 per model. All results to JSON with full provenance
(model id, seed, size, arm, raw reader output) — re-gradeable without
re-querying.

## 10. Build order (after approval)

1. `harness/run.py` — arms (paste/LWW/ceiling), queries, parsing, grading;
   smoke-run on `demo-prose/` (8-sibling, 1 scenario) end-to-end.
2. Sanity gates (§2) on the pilot scenario ×3 domains once Maren's packs
   merge.
3. Entity-pool/days widening; one 60k world; re-verify invariants at size.
4. Wrapper-bank spec to Maren (separate brief, after fork-3 approval).
5. Sweep pilot (12 scenarios) → then the 50-scenario headline run.
