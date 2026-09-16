---
type: open-question
name: Can an off-the-shelf structured memory auto-build the scope index?
status: OPEN
last_ingested: 2026-07-22
sources: [../experiment/2026-06-30-masq-retrieval-arms.md, ../experiment/2026-07-22-masq-supermemory-smoke.md]
epistemic_tags: []
tags: [masq, retrieval, structured-filter, cognee, incumbent, v2]
---

## The question

[H45](../hypothesis/H45-exclusion-over-recall.md) showed (within MASQ's construct) that
an **oracle** scope filter (`WHERE scope=target`, using ground-truth tags) reaches
ceiling decision accuracy while every similarity-ranking arm floors. But the oracle is
handed the scope index for free. The deployable question is: **does an off-the-shelf
structured / knowledge-graph memory system, given only the raw messages, automatically
build a scope index that approximates `WHERE scope=target` — or does its entity-extraction
merge the five `checkout-*` scopes into one node, reproducing the embedding scope-merge?**
Supermemory (self-hosted, embedded graph engine, LLM memory-extraction agent) is the designated system #2 for this test (selected 2026-07-01 over Cognee for implementation simplicity; Cognee remains a candidate for system #3 if needed).

**Status 2026-07-22 — first evidence in, held provisional.** The
[Supermemory smoke core](../experiment/2026-07-22-masq-supermemory-smoke.md)
landed at A=8% / B-FAIL — *below* the scope-blind floor — with a mechanistic
read pointing at the second branch below in sharpened form: extraction appears
to smear the five `checkout-*` scopes at **write time** (0 scope-bound
kernel-entity memories retrieved, both transports, despite 18/18 source
sessions naming their scope). The question stays OPEN rather than resolving to
that branch because the result is **methodology-suspect by AJ's call**: the
scope census covered only retrieved memories (not the full store) and the
arm's context format is asymmetric vs. session-based arms. The experiment
page's pre-registered audit items gate any resolution and the 14-core sweep.
Mechanism candidate: [H46-consolidation-scope-smear](../hypothesis/H46-consolidation-scope-smear.md).

## Why it matters

- **If a structured system reaches ~ceiling:** there is a *deployable* path to the oracle filter; the MASQ story becomes "off-the-shelf *similarity* memory fails, off-the-shelf *structured* memory succeeds," and structured-memory adoption is the recommendation. Gives the first non-oracle arm strictly above the paste plateau (the graded point the ladder currently lacks).
- **If its extraction smears the scopes (floors like ranking):** the lesson sharpens to "building the scope index is itself the hard, unsolved part" — auto entity-resolution is the bottleneck, and the wedge sits in *how* the index is built, not in having one.
- Gates whether [structured-filter-first](../decision/structured-filter-first.md) has a turnkey realization or requires bespoke index construction.

## What evidence would resolve it

Add a Supermemory arm to the same fixed contract (`arm_fn(family, corpus) → context`), reader
and grader unchanged, run on the existing 15 cores at 60k. **Must use a frontier LLM**
(Sonnet/Opus) for Supermemory's memory-extraction agent — local models strip scope bindings
during extraction, making the result unfalsifiable (confirmed 2026-07-01 spike). Compare its
B-pass against the scopefilter oracle (upper bound) and the paste/vector plateau (lower bound).
Same closed-form A/B grading; no new metrics. Inspect its extracted memories for whether the
five scopes produce scope-bound facts or scope-stripped facts (the mechanistic read, analogous
to the recall-vs-exclusion diagnostic).

**Adequate signal:** the predicted endpoints differ by enough magnitude (ceiling 100% vs
plateau ≤60%) that even n=15 at one size discriminates, as it did for scopefilter. A landing
strictly between the two would itself be the sought graded point.

## Sub-questions

- Does Cognee's entity resolution distinguish `checkout-web` from `checkout-api`, or collapse them?
- Is any gain from the graph structure or just from a better-curated candidate set?
- Would a cheap hand-built scope extractor (regex/NER on the scope key) beat the full graph pipeline — i.e. is the graph worth its cost here?

## Related

- [H45-exclusion-over-recall](../hypothesis/H45-exclusion-over-recall.md) — establishes the oracle upper bound this question chases
- [experiment 2026-06-30 MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md) — the ladder this extends
- [structured-filter-first](../decision/structured-filter-first.md) — the decision whose deployability this gates
- [Cognee](../incumbent/cognee.md) — designated system #2
