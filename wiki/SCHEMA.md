---
tags:
  - exclude-from-graph
---
# Kyrja Wiki Schema

**Purpose.** A linked, agent-maintained wiki for Kyrja research. Solves the re-consumption problem: AJ can re-enter the project at any time and recover what-and-why in under 90 seconds by reading `NOW.md` (current state) then drilling from `README.md` (orientation) into the graph.

**Built on** Karpathy's LLM-wiki pattern, hardened with provenance enforcement, epistemic-status discipline, anti-sprawl rules, and an explicit cross-agent federation model.

**Status of this schema.** Living. Edit as conventions evolve. Schema changes require a conversation with AJ before version bump -- this is not a unilateral agent action.

---

## Three-layer architecture

1. **Raw sources** — immutable external material. Papers (PDFs in `kyrja/library/papers/`), vendor documentation, third-party benchmarks, blog posts. The wiki *cites* these via `source/*` pages; it never modifies them.
2. **Wiki** — atomic, cross-linked pages. Lives at `wiki/`. Agent-maintained.
3. **Schema** — this file. Tells the agent how to maintain layer 2.

**Our own historical artifacts are not raw sources.** The deep-dive, THESIS.md, old experiment specs, archived hypotheses, scale-model docs -- these contain *our* synthesis with *our* priors. They are material to be **atomized into wiki pages**, not citation targets. Each piece (cascading-failures equation, seven-layer stack, competitor analysis, LIMIT correction) migrates into the appropriate page type. The wiki page becomes canonical; the original artifact stays in `kyrja` as an archived raw artifact we don't cite into. This avoids perpetuating past synthesis as ground truth.

---

## Page types (seven)

Every page **inside a wiki subdirectory** is exactly one type. Type determines required fields and lifecycle.

**Wiki-root files are exempt from type classification.** `README.md`, `NOW.md`, `index.md`, `log.md`, `SCHEMA.md`, and any other root-level navigation/spine files do not need a `type:` field. If the wiki root accumulates many such files, revisit this exemption. The roles of each root file are formalized in [§ Root files](#root-files) below.

### `hypothesis/`
- **Purpose**: A falsifiable claim under test.
- **Status lifecycle**: `PROPOSED → SUPPORTED | REJECTED | SUPERSEDED`
- **Required sections**: claim (one sentence), what-would-falsify-it, evidence-for (linked), evidence-against (linked), open sub-questions.
- **Filename**: `H##-short-slug.md`. Archive hypotheses keep their H-numbers (H01–H22). New hypotheses start at H23.

### `experiment/`
- **Purpose**: Something we ran.
- **Status lifecycle**: `PROPOSED → RUNNING → LANDED | INVALIDATED`
- **Required sections**: hypotheses tested (links), method, results (with construct-validity statement: what the metric actually measures and whether that matches the claim), links to raw artifacts.
- **Filename — single run**: `YYYY-MM-DD-short-slug.md`.
- **Filename — multi-run investigation**: `YYYY-MM-DD-investigation-slug/README.md` (umbrella) plus one sibling file per run (e.g. `exp1-task2.md`, `exp2-task3.md`). The folder name uses the date of the first run; sub-runs may land later without renaming the folder.

### `decision/`
- **Purpose**: An architectural or methodological choice we've made.
- **Status lifecycle**: `ACTIVE | REVERSED | SUPERSEDED`
- **Required sections**: decision, motivation (links), commitments (what this locks us into), reversibility (cheap / expensive / one-way).
- **Filename**: short-slug.md (e.g. `repo-bounded-scope.md`).

### `concept/`
- **Purpose**: A primitive we use repeatedly across pages. Defined once, cited everywhere.
- **Status**: timeless.
- **Required sections**: definition, role in Kyrja thesis, source link(s) for deeper read.
- **Filename**: short-slug.md (e.g. `limit-bound.md`, `cascading-failures.md`).

### `source/`
- **Purpose**: One page per raw *external* document. The provenance anchor.
- **Status**: timeless.
- **Required sections**: citation, file/URL path, key claims with our restatement, relevance to Kyrja.
- **Filename**: `first-author-year-slug.md` (e.g. `weller-2024-limit.md`).
- **Note**: Internal artifacts do not get `source/` pages — they are atomized into the wiki.

### `incumbent/`
- **Purpose**: One per competing/related system.
- **Status field**: `status_current_as_of: YYYY-MM-DD`
- **Required sections**: what it does, what it doesn't, which layer(s) of our seven-layer stack it covers, where it fails.
- **Filename**: short-slug.md (e.g. `mem0.md`, `cognee.md`).

### `open-question/`
- **Purpose**: A known gap. Lives until promoted to a hypothesis or closed.
- **Status lifecycle**: `OPEN → HYPOTHESIS-FORMED | RESOLVED | DEPRIORITIZED`
- **Required sections**: the question, why it matters, what evidence would resolve it.
- **Filename**: short-slug.md (e.g. `multiplicativity-vs-overlap.md`).

---

## Root files

Five files live at the wiki root. They are exempt from page-type frontmatter (no `type:` field required) but have defined roles and update cadences. Adding a new root file requires a SCHEMA bump.

| File | Role | Update cadence | Owner |
|---|---|---|---|
| `README.md` | Orientation — what the wiki is, how to use it, page-type overview, archive pointer. Static-ish. | rare (when wiki structure or conventions change) | any agent during ingest |
| `NOW.md` | Working state — current active question, current sub-task, immediate next step. Rewritten in place each session (not appended). Dynamic. | end of each working session | session author (whoever closes out) |
| `SCHEMA.md` | This file. Conventions, frontmatter, link rules, lint rules, version history. | per schema change; **requires AJ approval** | any agent, with AJ approval |
| `index.md` | Catalog of every page by type with one-line summaries. | per `/wiki-ingest` run | `/wiki-ingest` skill |
| `log.md` | Append-only session record. Each session appends a brief (≤15 line) entry; no rewriting of prior entries. Archived when it exceeds ~500 lines. | per `/wiki-ingest` run or session close | `/wiki-ingest` skill |

**`NOW.md` conventions:**

- **Read first** at session start. The active question + current sub-task + immediate next step orient the session.
- **Rewritten** at session end. Whoever closes the session rewrites the relevant sections to reflect current state. NOW.md is a state document — it says *where we are*, not *how we got here*. Don't append dated blocks; rewrite in place.
- **Target length: ≤80 lines.** If it grows past this, content is migrating here that belongs in the wiki graph or in log.md.
- **Provisional state** is allowed and expected. Mark uncertain classifications as provisional rather than committing prematurely.

**`log.md` conventions:**

- **Append-only.** Each session appends one entry. Never rewrite prior entries.
- **≤15 lines per entry.** What changed, pages created/updated, next entry point. No session narratives, no drift/residual sections unless genuinely surprising.
- **Archived at ~500 lines.** Move everything except the most recent ~10 entries to `archive/log-<date-range>.md`. The archive is the historical record; the active log.md stays concise.

**Archive.** Retired root files move to `./archive/` with a date-stamped filename (e.g. `archive/BIG-PICTURE-2026-05-14.md`). They are not deleted; they are dropped from the active path and preserved for historical reference.

---

## Mandatory frontmatter

YAML at the top of every page (in wiki subdirectories; root files are exempt):

```yaml
---
type: hypothesis | experiment | decision | concept | source | incumbent | open-question
name: short title (human-readable)
status: <per type lifecycle>
last_ingested: 2026-05-17
sources: [paths to source/* pages this page cites — descriptive list, not a constraint]
---
```

**Note on `sources` semantics.** This field is a descriptive roll-up of source pages cited from this page's prose. It is not a strict requirement: a page may have `sources: []` while still containing empirical claims, as long as each inline claim links to its provenance (per the link rules). Use the frontmatter list for navigation and Dataview queries; the discipline lives at the inline-tag level.

**Note on list syntax.** Both YAML list forms are accepted for `sources:` (and any list-valued field) — inline `sources: [../source/a.md, ../source/b.md]` and block:

```yaml
sources:
  - ../source/a.md
  - ../source/b.md
```

The lint parser reads both (since v0.7.1). Obsidian renders both. Pick whichever is readable; inline is conventional for short lists.

## Optional frontmatter

```yaml
supersedes: [list of page paths this page replaces]
superseded_by: [list of page paths that replace this one]
epistemic_tags: [measured, asserted, speculated, contested]  # roll-up of inline tags; enables Dataview filtering
tags: [wedge-relevant, integration-gap, post-limit, ...]  # free-form cross-cutting tags; Obsidian-pane aggregation
program: kerros  # research-program assignment (v0.7); absence = unassigned (the default). Only `kerros` in use as of v0.7. See § Program assignment.
contributed_by: <agent-name>  # if page originated from another agent's work
contributed_at: YYYY-MM-DD    # required if contributed_by is set
```

YAML format must be preserved exactly (no auto-reformatting by editor tooling). AJ is using Obsidian as a viewer only -- authoring stays in agent tools, which keeps YAML stable.

---

## Program assignment (v0.7)

The wiki is a **chronicle**: it records what we thought and when. Restructuring it wholesale to match current framing would erase that record, so we don't.

Pages carry an optional `program:` frontmatter field naming the research program they belong to:

- **Absence = unassigned.** This is the default. Most pages have no `program:` field and we do **not** mass-add one. Unassigned is a real, valid state.
- **`program: kerros`** — the substrate-memory research program (memory the *model* thinks with). The only value in use as of v0.7. See [kerros](./concept/kerros.md).
- Future programs (and the product line, once named) get their own values.

**Assignment is lazy.** A page gets a `program:` field when we next touch it for substantive reasons, not in a sweep. At that point we make a judgement call: move the page wholesale (it belongs entirely to one program) or split it (it conflates two — extract the part that belongs, leave the rest).

**The assignment rule is the boltability test.** If the page's claim is achievable by a frozen LLM + external store + prompt engineering (*persistence*), it is memory-for-the-agent → unassigned (later: product). If it requires the persisted information to enter the model's computation (*integration*), it is memory-for-the-model → `kerros`. See [kerros](./concept/kerros.md) for the gate.

**Superseded framing stays as chronicle.** When a page assigned to a program still carries older product-wedge language, dated historical notes (e.g. "as of 2026-05-13") are preserved; only the page's *active, undated* framing is updated to the current program lens. Add a dated note rather than rewriting a dated one.

---

## Epistemic status tags (inline, in prose)

Tag claims in prose with one of:

- `[MEASURED]` — we have data; source linked. Must include a construct-validity note: what the metric measures and whether that matches the claim.
- `[ASSERTED]` — claimed, not measured. Borrowed from a paper or competitor.
- `[SPECULATED]` — our hypothesis, no evidence yet.
- `[CONTESTED]` — sources disagree.

**Example:**

> The cascading-failures product reaches 30-50% effective recall `[ASSERTED]` ([source](../source/weller-2024-limit.md)). Multiplicativity vs overlap of the four failure modes is `[SPECULATED]`. HNSW recall on LongMemEval at production scale is `[MEASURED]` at ~52% ([source](../source/mem0-self-report-2024.md); construct-validity note: LongMemEval measures retrieval accuracy on conversational memory, which approximates -- but does not equal -- the agentic-memory recall we care about).

This is the discipline that makes the wiki readable as research, not opinion. Untagged empirical-shaped claims fail lint.

---

## Link rules (mandatory)

1. **Every empirical claim** links to a `source/*` page, an `experiment/*` page, or a `[pending]` marker (see "Pending-link convention" below). Unsourced claims with no provenance marker are lint failures.
2. **Every experiment** links forward to the hypotheses it tests and the concepts it depends on.
3. **Every decision** links to (a) the motivation that drove it and (b) what it commits us to. Motivations are *linked pages* when a relevant wiki page exists; otherwise inline prose with a path link to the archive artifact is acceptable, with the linked target flagged for atomization.
4. **Every hypothesis** links to evidence-for and evidence-against. Asymmetric evidence is a signal worth flagging.
5. **Every concept** has at least one inbound link from a hypothesis, experiment, or decision — else it's orphaned and a lint failure.
6. **Every incumbent** maps to the seven-layer stack: which layer(s) it covers, which it doesn't.

Links are relative paths, markdown-style: `[anchor text](../hypothesis/H08-filter-first.md)`. Not wikilinks.

**Filepaths in prose should be links, not bare paths.** Use `[file label](../../path/to/file.md)` rather than backticked raw paths, so Obsidian (and any other reader) can navigate to the artifact.

**Cross-agent paths use absolute form.** The wiki lives at `wiki/` — a shared location accessible to all agents. Relative paths within the wiki are portable. Paths to other team-share locations (`coral`, etc.) use absolute form.

The host has a symlink at `/team-share/` pointing to `~/team/`, so absolute `...` resolves on both sides:
- Container: native `/team-share/` mount.
- Host: `/team-share/` symlink → `~/team/`.

Example:

```markdown
See Eira's commercial framing for the market sizing thread.
```

**Project-memory references are transitional.** Pages under `memory` are container-only and cannot be linked from the host's view. Keep these as backticked prose (e.g. `` `project_kyrja_active.md` ``) rather than markdown links. The endgame is full atomization of memory into wiki pages, after which these references disappear entirely.

## Pending-link convention

When referencing a wiki page that doesn't yet exist (planned but not written), mark the link with a `"pending"` title attribute:

```markdown
[multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md "pending")
```

Lint treats `"pending"` links as known-future targets, not dangling-link violations. When the target page is created, remove the title attribute. This keeps planning visible in the wiki without polluting lint output.

---

## Anti-sprawl rules

1. **Update before create.** New page only if either (a) the topic is or will be referenced by 3+ existing pages, or (b) the topic has its own status lifecycle.
2. **One concept per page.** No compound pages like "Embeddings and HNSW." Split.
3. **500-line ceiling.** Any page over 500 lines is a split candidate at next ingest.
4. **No duplicate claims across pages.** Cite, don't repeat. If duplication is found, promote the claim to a concept page and cite from both.

---

## Lint rules (definitions)

The lint pass is owned by the `/wiki-lint` skill. The rules it enforces:

1. **(retired in v0.5.3)** — `stale-source` (was: citing page's `last_ingested` < cited `source/*` or `experiment/*` page's `last_ingested`). Rule fired *after* a human author already decided whether to propagate a re-read, so it could only flag decisions that had been made — never surface ones that had been missed. On bulk-ingest days it produced 170+ findings, almost all spurious (file touches, frontmatter bumps, parallel ingests). The genuine cases (vendor docs that materially change, our own aggregation pages that absorb new data, re-reads that correct a downstream framing — e.g. the 2026-05-17 EM-LLM "sidecar" correction) are best handled by author-side propagation discipline at edit time, not by post-hoc lint. See **author-side propagation** below.
2. **orphan** — page has zero inbound links. May be intentional; flag for review.
3. **tagged-page-needs-sources** — a `concept/`, `decision/`, `hypothesis/`, `open-question/`, or `incumbent/` page that contains any `[MEASURED]` or `[ASSERTED]` tag must declare a non-empty `sources:` list in frontmatter. (v0.4: replaces the v0.3 inline-link regex; see [concept/evidence-anchoring](./concept/evidence-anchoring.md) for why.)
3b. **source-page-needs-citation** — a `source/*` page must contain at least one external URL in its body. The URL is the page's commitment to its underlying external artifact; without it, internal synthesis can structurally hide as evidence.
4. **contradiction** — same claim with different epistemic tags across pages.
5. **dangling-link** — link target doesn't exist.
6. **status-mismatch** — e.g., hypothesis marked `SUPPORTED` with no linked supporting experiment; decision marked `ACTIVE` that's been superseded.
7. **(retired in v0.4)** — `untagged-claim` (was: quantitative/universal claims without an epistemic tag). Regex couldn't distinguish methodology metadata from real claims at acceptable false-positive rate. Discipline moves to authoring and to a future `/wiki-audit` skill.
8. **missing-construct-validity** — a `[MEASURED]` claim without an accompanying note on what the metric actually measures. **Source pages exempt (v0.5.3):** for `source/*` pages we are quoting paper-internal measurements where the experimental paradigm IS the construct; rule 8 was designed for *Kyrja-internal* translations of metrics, not for re-stating a paper's own methodology. Applies to: `concept/`, `decision/`, `hypothesis/`, `experiment/`, `open-question/`, `incumbent/`.
9. **dangling-link-without-pending** — link target doesn't exist AND the link has no `"pending"` title attribute. (Covered by `dangling-link` rule 5; this is its refinement.)

### Author-side propagation (replaces retired rule 1, v0.5.3)

When you substantively edit a `source/*` page in a way that changes a downstream-cited claim (e.g. correcting a prior framing, adding a finding that affects a citing page's argument, reading a vendor doc that has changed), walk the inbound `[[citing-page]]` links and update the citing pages in the same ingest. Routine non-substantive edits (frontmatter bumps, typo fixes, formatting) do not require propagation. This discipline lives at edit time, where the author has the context to judge "is this change load-bearing for any downstream page?"; lint cannot answer that question for you.

The structural failure mode the retired rule tried to catch is rare in practice because:
- `source/*` pages cite frozen artifacts (papers, fixed-version vendor docs) that don't change underneath us;
- when our own *summary* of the artifact changes (the EM-LLM case), the author doing the re-read is the same author who would propagate, and the propagation work is part of that same ingest's planning;
- when a vendor doc materially changes, the human re-reading the doc is the right judge of "does this break downstream claims?" — not a date-comparison rule.

See [concept/evidence-anchoring](./concept/evidence-anchoring.md) for the framework behind the v0.4 retirement of rules 3 (old form) and 7. The framework also serves as the spec for a future `/wiki-audit` skill that uses an LLM to apply the Cat 1 / 2 / 3 triage that the regex couldn't.

---

## Operations

Procedural detail lives in dedicated skills, not in this schema.

- **Ingest** — owned by the `/wiki-ingest` skill. Called by `/tidy` at end of session, or invokable directly when material lands mid-session.
- **Lint** — owned by the `/wiki-lint` skill. Invokable on demand or on schedule. Skip set: `{SCHEMA.md, log.md, lint/, archive/}` (v0.5.1). Archive files are retired-and-frozen by design; lint-ing them inverts the rule signal.
- **Query** — no skill needed. Querying is reading; start at `NOW.md`, drill from `README.md` into the graph, use `index.md` as catalog.

---

## Cross-agent federation

Other agents on the team have their own working spaces under `/team-share/<colour>/`. The wiki does **not** reach into those folders live. Instead:

- When AJ wants material from another agent's work brought in, an explicit ingest happens at a chosen point in time.
- The ingested page records `contributed_by: <agent>` and `contributed_at: YYYY-MM-DD` in frontmatter.
- The wiki owns its copy. The original folder stays autonomous; subsequent changes there don't propagate automatically.

Known team contributors and the kinds of material they may surface:

- **Kerman (red)** — Testing, performance, benchmarking. MASQ benchmark data lives at `memory-benchmarks`. Benchmark datasets become `source/` pages; runs we participate in become `experiment/` pages.
- **Eira (coral)** — Product management, market analysis. Commercial framing lives in `coral`. Cross-referenced from the wiki, not duplicated into it.
- Others may surface contributions as the project evolves.

---

## What is *not* in the wiki

- **Eira's commercial / GTM material.** Lives in `coral`. Wiki links out; does not duplicate.
- **Kerman's benchmark datasets and full run logs.** Live in `memory-benchmarks`. Wiki ingests *findings* as `source/` or `experiment/` pages, not the raw data.
- **Day-to-day session scratch.** Use the normal chat; only what ingest decides is wiki-worthy gets persisted.

---

## Schema-change discipline

This schema is v0.2 and will be wrong somewhere. Signals it needs editing:

- A class of content doesn't fit any of the seven page types → add a type, don't force a fit.
- Lint passes but pages are still hard to navigate → schema is permissive where it should be strict.
- Lint fails on legitimate content → schema is strict where it should be permissive.
- A discipline that's needed for research isn't enforced → add it to lint rules or frontmatter.

**Schema changes require a conversation with AJ before the version is bumped.** Not a unilateral agent action. Bump the version at the bottom and note the change in `log.md` after AJ approves.

---

## Directory layout

```
kyrja/wiki/
├── README.md          ← orientation; what this wiki is, how to use it
├── NOW.md             ← working state; active question, current sub-task, next step
├── SCHEMA.md          ← this file; conventions
├── index.md           ← catalog: every page, one-line summary, by type
├── log.md             ← append-only ingest record
├── archive/           ← retired root docs (e.g. former BIG-PICTURE snapshots)
├── hypothesis/
├── experiment/
├── decision/
├── concept/
├── source/
├── incumbent/
└── open-question/
```

---

## Version history

- `v0.1` — initial draft, 2026-05-11 (Nils/indigo).
- `v0.2` — 2026-05-11 (Nils/indigo, with AJ review): internal artifacts atomized rather than treated as `source/` pages; operations moved out of schema into `/wiki-ingest` and `/wiki-lint` skills; cross-agent federation model added (`contributed_by`/`contributed_at` frontmatter, Kerman reference, stale Idris reference removed); Obsidian-aware additions (`epistemic_tags` and `tags` optional frontmatter); construct-validity discipline baked into `[MEASURED]` tag and new lint rule; schema-change discipline made explicit.
- `v0.3` — 2026-05-11 (Nils/indigo, with AJ review): root-level files exempt from type classification (drops ad-hoc `navigation` type); `sources` frontmatter clarified as descriptive (discipline lives at inline-tag level); `[pending]` link convention added (title attribute "pending" exempts dangling links); `untagged-claim` lint rule narrowed to quantitative/universal claims (soft prose exempt); decision link rule 3 clarified (motivation links when wiki page exists, archive prose otherwise); experiment filename convention adds folder pattern for multi-run investigations; filepath-as-link convention noted.
- `v0.3.1` — 2026-05-12 (Nils/indigo, with AJ approval): cross-mount path convention clarified. The wiki spans a container/host bind-mount boundary; relative paths that escape `/workspace/` don't resolve identically on both sides. Rule: cross-mount references use absolute paths (`...`); project-memory references stay as backticked prose pending full atomization. Sub-version bump rather than v0.4 because no new rules or types — clarification of existing link-rule discipline.
- `v0.4` — 2026-05-13 (Nils/indigo, with AJ approval): retired lint rules 3 (`unsourced-claim`, the same-bullet inline-link regex) and 7 (`untagged-claim`) after two rounds of regex narrowing failed to converge — the rules could only detect one of the five legitimate evidence-anchoring shapes and produced ~150 false-positives per run. Replaced with two structural rules: `tagged-page-needs-sources` (page-level frontmatter check) and `source-page-needs-citation` (source/* pages must contain an external URL). The judgment-shaped checks move to authoring discipline and a future `/wiki-audit` skill. Framework documented in [concept/evidence-anchoring](./concept/evidence-anchoring.md).
- `v0.5` — 2026-05-14 (Nils/indigo, with AJ approval): root-file restructuring. `BIG-PICTURE.md` retired (archived to `archive/BIG-PICTURE-2026-05-14.md`) — its thesis-shaped layout became unwriteable mid-investigation, when the project sat on an unresolved fork between memory-as-substrate and memory-as-bolt-on. Replaced with two new root files: `README.md` (orientation, static-ish) and `NOW.md` (working state, updated end-of-session). New `§ Root files` section formalizes the five-file convention, roles, update cadences, and archive discipline. Directory layout updated to reflect new spine and `archive/` subdirectory.
- `v0.5.1` — 2026-05-15 (Nils/indigo, with AJ approval): `archive/` directory added to the lint skip list. Archived root files use relative paths that worked when they were root-level but don't resolve from the `archive/` subdir; expecting them to is anti-purpose (archive is explicitly frozen and not maintained). The 2026-05-15 lint run surfaced 56 dangling-link errors all sourced to one archived file, dominating the report's signal-to-noise. The skip set is now `{SCHEMA.md, log.md, lint/, archive/}`. Sub-version bump rather than v0.6 because no new rules or types — extension of the existing lint-skip discipline.
- `v0.5.2` — 2026-05-17 (Nils/indigo, with AJ approval): canonical raw-source location corrected from `Shared/` to `kyrja/library/papers/` in § Three-layer architecture. The original `Shared/` reference was stale — `Shared` is a transient network share, while `kyrja/library/papers/` is the maintained canonical location (~30 papers already present, with ~9 wiki source pages already using it). 2026-05-17 RC literature-review ingest surfaced the drift when it landed PDFs in `library/papers/` per the actual convention. Companion sweep of 30+ `source/*` page Archive-location sections (replacing "Not in `Shared/`" with "Not in `library/papers/`") landed in the same pass. Sub-version bump rather than v0.6 because no new rules or types — correction of an existing location-convention reference.
- `v0.5.3` — 2026-05-17 (Nils/indigo, with AJ approval): two lint-rule changes after the second 2026-05-17 lint run surfaced ~94% of warnings as either structurally-pointless (rule 1 firing on file-touches, 176 findings) or pattern-mismatched (rule 8 firing on biology source-page paper-quotes, ~38 of 55 findings). (a) Retired rule 1 (`stale-source`) — the rule fired after author had already made the propagation decision, producing high false-positive rate on bulk-ingest days with no compensating signal-catch. Replaced with the **author-side propagation** discipline paragraph in § Lint rules. (b) Rule 8 (`missing-construct-validity`) now exempts `source/*` pages — paper-internal measurements have the experimental paradigm AS their construct; demanding a separate Kyrja-authored construct-validity note re-states the obvious. Net effect: warning count drops from 247 to ~30, all of which represent genuine review work. Sub-version bump rather than v0.6 because the rule taxonomy is unchanged; this is calibration of two existing rules.
- `v0.6` — 2026-05-23 (Nils/indigo, with AJ approval): NOW.md and log.md convention overhaul. NOW.md becomes a rewrite-in-place state document (≤80 lines) — session signposts removed; that role belongs solely to log.md. log.md entries capped at ≤15 lines; archived at ~500 lines to `archive/log-<date-range>.md`. `/wiki-ingest` skill simplified from 6 steps to 4: steps 5-6 (update index/NOW.md + append log.md) collapsed into one step; propagation pass (step 4→3) narrowed to load-bearing changes only, dropping mechanical `last_ingested` bumps on untouched content. Motivation: NOW.md had grown to 353 lines (mostly duplicating log.md signposts); log.md was 2507 lines and never read in full; ingest ceremony was spending more time on state-file bookkeeping than on the actual synthesis work.
- `v0.7` — 2026-05-25 (Nils/indigo, with AJ approval): added the `program:` optional frontmatter field and the **§ Program assignment** convention. Records the split of the "Kyrja" umbrella into distinct projects: **Kerros** (substrate-memory research program — memory the model thinks with) and a product line (memory the agent uses; named later). Absence of `program:` = unassigned (the default; no mass migration). Assignment is lazy and uses the boltability test (integration → kerros; persistence → product/unassigned). The wiki is treated explicitly as a chronicle: superseded framing is preserved, not rewritten. Anchor page: [concept/kerros](./concept/kerros.md). No new page type or lint rule — single optional field + one convention section.
- `v0.7.1` — 2026-06-07 (Nils/indigo, with AJ approval): lint-parser tolerance fix. `parse_frontmatter` in `lint.py` previously read only the inline list form (`sources: [a, b]`) and silently treated block-list YAML (`sources:` then `  - a` / `  - b`) as an empty scalar — producing a false `tagged-page-needs-sources` warning on any page that used the (equally valid, Obsidian-rendered) block form. The parser now accumulates `-`-prefixed continuation lines into the current key as a list; genuinely-empty `sources:` still reads falsy, so rule 3 still catches real gaps. Surfaced by the 2026-06-07 MASQ ingest (three new pages authored in block form). Documented in § Mandatory frontmatter ("Note on list syntax"). Sub-version bump rather than v0.8 because no new rules, types, or conventions — robustness fix so the tooling matches the YAML the schema already permits.
