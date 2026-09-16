---
type: concept
name: Evidence Anchoring — how Kyrja claims are pointed at evidence
status: timeless
last_ingested: 2026-05-26
sources: []
epistemic_tags: []
tags: [discipline, schema, audit, methodology]
---

## Definition

**Evidence anchoring** is the discipline of pointing each tagged claim in the wiki at the evidence that supports it. A claim tagged *MEASURED*, *ASSERTED*, *SPECULATED*, or *CONTESTED* carries an implicit promise: a future reader can find the evidence (or the absence of it) and judge trustworthiness for themselves.

This page is descriptive — it names the shapes anchoring actually takes in the Kyrja wiki, and names what to check when reviewing a page. The mechanical lint rules at `wiki-lint` enforce only the structural subset of this framework; the rest is authoring discipline and (eventually) LLM-based audit.

## The five legitimate shapes of evidence anchoring

A claim can be anchored to evidence in any of the following ways. All five are valid; the lint cannot reliably detect all of them.

1. **Inline link in the same bullet.** A *MEASURED* or *ASSERTED* claim followed (or preceded) by a same-bullet markdown link to a `source/*` or `experiment/*` page. The strictest and easiest shape to check.
2. **Frontmatter `sources:` list at the page level.** The page declares which sources it draws from in its frontmatter; specific claims on the page inherit that anchoring without each bullet needing its own link. Required for `concept/`, `decision/`, `hypothesis/`, and any page that asserts external facts.
3. **The page IS the source.** A `source/*` page's `Citation`, `Location`, and `Key claims` sections ARE the citation for everything on that page. Self-reference is structurally fine — the `type: source` frontmatter is the page-level commitment to being external evidence.
4. **Construct-validity note in prose.** A nearby sentence names the source explicitly ("from ANN-Benchmarks synthetic corpora", "per the MN-RU paper"). The link may or may not appear inline; the prose carries the anchoring.
5. **Restatement of a tagged claim elsewhere.** A number that is fully sourced on its canonical page (e.g. cascading-failures.md) is restated on a sibling page (e.g. benchmark-replication-gap.md). The restatement does not need to re-anchor — readers follow the link to the canonical claim.

## The Cat 1 / 2 / 3 triage schema (when auditing a page)

When sweeping a page for evidence-anchoring discipline (see deep-dive sweep log 2026-05-13), each unanchored claim falls into one of three actions:

- **Cat 1 — Re-anchor to an existing external source.** The claim is real, the source exists in the wiki or as a citable external artifact; add the inline link and (if missing) a brief construct-validity note. No new pages.
- **Cat 2 — Promote a new `source/*` stub.** The claim is real and externally anchored, but no `source/*` page yet exists for the underlying artifact (paper, vendor doc, dataset). Create the stub with the standard sections (Citation, Location, Key claims with our restatement, Construct-validity caveats, Relevance to Kyrja). Per [load-bearing sources discipline], include "not read verbatim" caveats unless the agent has read the paper line-by-line.
- **Cat 3 — Re-tag *ASSERTED* → *SPECULATED*.** The claim is *Kyrja-internal synthesis* (a conjecture, a diagnostic observation, a structural-reasoning argument) mis-tagged as if it were externally anchored. The right move is the lower tag plus an explicit note that this is Kyrja's reading.

The cost-leg sweep (2026-05-13 morning) and the residual unsourced-claim sweep (2026-05-13 afternoon) both used this categorization. See `lint/2026-05-13.md` and `log.md` for worked examples.

## The two-shape split on `source/*` pages

When a `source/*` page makes a claim, the claim falls into one of two shapes:

- **B1 — true self-reference.** The claim paraphrases the paper named in the page header. The page's `Citation` / `Location` sections are the anchoring. Asking for an inline `source/*` link is redundant.
- **B2 — adjacent-cite gap.** The claim is about a *different* artifact mentioned in prose (an independent eval, a vendor-reported number, a sibling paper). The right fix is an inline link to the adjacent `source/*` page, not a rule exemption. This is the same pattern as Cat 1 on non-source pages.

Lint rules treating all source-page claims as self-reference would lose discipline against B2. Conversely, treating none as self-reference produces the noise that motivated retiring Rule 3 in lint v0.4.

## The central audit question — internal synthesis ≠ external evidence

The load-bearing test for any tagged claim, especially on `source/*` pages: **is this Kyrja-internal synthesis hiding as external evidence?**

A `source/*` page is structurally a commitment that its content is external evidence. If a claim on that page is actually Kyrja's reading of multiple papers, our extrapolation to a new regime, or a diagnostic observation from a grading exercise, it must be either (a) re-tagged *SPECULATED* with explicit note, or (b) atomized out to a `concept/*` page where Kyrja synthesis is the type-appropriate shape.

This is the lifecycle of the deep-dive (`agentic-memory-scaling-deep-dive.md`): it was Kyrja-internal synthesis, was mis-cited as a `source/*` for a while during Phase F, and the 2026-05-13 deep-dive sweep ran the entire wiki through the Cat 1/2/3 triage to clean it up. The principle generalizes: any long-form synthesis we produce internally is not a citation target; it is material to be atomized.

## The verbatim-read discipline

For claims with magnitude numbers from a specific paper, the agent should have read the paper verbatim — not just summarized from prior agents' summaries. When a page is anchored to a paper that has not been verbatim-read, the page MUST carry a "not read verbatim" construct-validity caveat. See `[load-bearing sources]` discipline (in user memory).

`source/*` page stubs created during sweeps (e.g. the 5 stubs from the 2026-05-13 residual sweep) are explicitly "not read verbatim"; this is acceptable as an anchor point, but a numeric claim on the page should not be cited as load-bearing without the verbatim read happening first.

## What lint can and cannot enforce

Lint v0.4 retired Rules 3 (unsourced-claim) and 7 (untagged-claim) because the regex heuristics could only detect shape 1 above (inline link in same bullet). Shapes 2–5 are equally legitimate and not detectable by regex. The post-v0.4 lint enforces only what is reliably detectable:

- **Frontmatter `sources:` non-empty** for any `concept/`, `decision/`, `hypothesis/`, `open-question/`, or `incumbent/` page that contains a *MEASURED* or *ASSERTED* tag.
- **`source/*` page has an external URL** in its body (the page must point to its underlying paper or vendor doc somewhere).
- Plus the unchanged Rules 1, 2, 4 (inventory), 5, 6, 8, 9.

The judgment-shaped checks (is this claim really sourced? is this Kyrja synthesis pretending to be evidence?) are delegated to authoring discipline and to a future `/wiki-audit` skill that uses an LLM to walk a page and apply the Cat 1/2/3 schema. The framework on this page is the spec for that skill.

## Role in Kyrja thesis

This page is operational, not thesis-bearing. But evidence-anchoring discipline IS load-bearing for the wiki's role as cognitive substrate: if a future agent (or future AJ) cannot trust the wiki's tagged claims, the wiki stops being a trustworthy re-entry surface. Anchoring discipline is what makes the substrate reliable.

## Related

- [decision/research-integrity-checks](../decision/research-integrity-checks.md) — the complementary half. Evidence-anchoring governs *claim*-provenance (is this number pointed at its source?); the integrity checks govern *result*-integrity (was the number produced by a silent bug or a leaked rubric?). Together they make the wiki trustworthy as research.
- [SCHEMA.md](../SCHEMA.md) — v0.4 documents the post-lint-v0.4 rule set and references this concept page for the framework
- `wiki-lint` — the structural lint that enforces the detectable subset
- [`lint/2026-05-13.md`](../lint/2026-05-13.md) — the report whose triage produced this framework
- [`log.md`](../log.md) — deep-dive sweep entry (2026-05-13 morning) and residual sweep entry (2026-05-13 afternoon), both worked examples of Cat 1/2/3 in action

## Source archive

This page captures discipline developed across the 2026-05-13 paired sweeps. No external citation — the framework is Kyrja-internal methodology. The user-memory entries `feedback_internal_synthesis_evidence`, `feedback_load_bearing_sources`, and `feedback_epistemic_lens` are the parent epistemic-discipline notes from which this page operationalizes the wiki-side rules.
