---
type: experiment
name: MASQ Supermemory audit + store repair + first valid result (smoke core)
status: LANDED
last_ingested: 2026-07-25
sources: []
epistemic_tags: [MEASURED]
tags: [masq, supermemory, extraction-first, scope-smear, atomization, system-under-test, audit, v2]
---

Audit, repair, and re-run of the [2026-07-22 Supermemory smoke](./2026-07-22-masq-supermemory-smoke.md),
whose graded numbers are now **EXCLUDED FOR CAUSE** (documented instrument
failure, not a bad-looking result). This page carries the first *valid*
Supermemory numbers and the mechanism findings the audit produced.
Pre-registration: [REPAIR-PREREG.md](../../masq/harness/REPAIR-PREREG.md)
(written 2026-07-24, before any reader call on the repaired store).

## Why the smoke was invalid (the cause)

`[MEASURED]` The subscription cap killed every `claude -p` call from
2026-07-21 23:38:07Z (2,166 of 3,049 proxy calls rc=1, one contiguous 53-min
window — the smoke page's original "~2,900 successful calls, 0 parse errors"
was wrong; true count 883 ok / 2,166 failed). supermemory-server **v0.0.3
marks a document `done` with zero extracted memories when its LLM calls fail**
(silent-failure bug; deployment-relevant finding in its own right). Result:
340/626 documents — every session from world-day ~80 on — contributed nothing
to the store the smoke queried.

## Repair method

Re-extract the 340 zero-yield docs chronologically (deployment-shaped: later
sessions extract into a store already holding earlier memories) via the
throttled `claude -p` proxy, health-gated batches, per-doc yield verification,
iterated boundary passes over proxy error windows, and a final full census
gate: **verification passes iff all 626 docs have ≥1 memory and no unhandled
error events** ([audit_repair.py](../../masq/harness/audit_repair.py)).
The reader is mechanically blocked on verification FAIL.

The gate earned its keep: it caught two instrument bugs before any number was
graded, refusing to pass twice —

1. **Bursty throttle** (rolling-hour budget → burst-then-wall): requests held
   ≥324 s exceeded the server's ~5-min client timeout → 111 connection resets
   → done-empty docs. Fix: uniform pacer (one call start per 24 s).
2. **Cap-detector false positive**: the proxy's cap-text check reused the
   reader-cleaning signature list, which contains "overloaded" — a word that
   appears in this rate-limiting corpus's own prose (e.g. s0401). Extraction
   replies quoting the prose were misread as cap messages and deterministically
   failed. Fix: cap detection now matches only cap-UI-specific phrasings
   ("hit your session limit", "· resets", …). *Meta-lesson: contamination
   signature lists are context-specific; a list curated for reader answers
   does not transplant to a proxy whose traffic quotes the corpus.*

Final verification: **PASS** — 626/626 docs, 3,537 extracted memories, zero
error/stall events ([verification JSON](../../masq/generator/headline/rate-limit/s4001/60k/repair-verification-masq-rate-limit-s4001-60k-cc.json)).

## Results (rate-limit/s4001/60k, reader claude-opus-4-8, K=20)

| arm (this core) | A-score | B | B action |
|---|---|---|---|
| ceiling | 100% | PASS | set_800 |
| scope-filter | 100% | PASS | set_800 |
| paste | 69% | FAIL | set_50 |
| vector_k10 | 69% | FAIL | set_50 |
| bm25_k10 | 69% | FAIL | set_50 |
| **supermemory-k20** | **31%** | **FAIL** | **set_50** |
| lww | 8% | FAIL | set_50 |

`[MEASURED]` (n=1 core — no endpoint claims; endpoints stay 15-core counts.)
Note: per-core paste/vector values in the merged results JSON are 69%, not the
84%/79% transcribed onto the smoke page — corrected there.

**Headline candidate:** on a complete store, Supermemory's extracted-memory
layer scores **below the scope-blind retrieval plateau** (31% vs 69%), while
its B failure is *identical* to every scope-blind arm (`set_50` — the latest
unscoped `/checkout` write, a sibling scope's value, Lena day 173). Extraction
loses more than scope: **0/3 target-chain steps (days 24/42/57) appear in the
top-20 retrieved memories** (vector recalls ~2.8/3 of the chain at session
level). The chunk-level product path (`search.documents`, audit item 3 on
2026-07-24) retrieves 3/3 chain steps — so the deficit is specifically the
extraction layer, and the claim is scoped to it.

## Pre-registration scorecard

1. *A rises toward the vector region* — **partially confirmed**: rose 8%→31%
   (off the below-floor artifact), but reaches less than half the scope-blind
   plateau. The gap is explained by the new recall finding above, but "toward
   the vector region" was optimistic; registered honestly as a miss on
   magnitude.
2. *`set_50` disappears* — **REFUTED**. `set_50` persists on the complete
   store because it was never an outage artifact: it is the canonical
   scope-blind wrong answer on this core (every failing arm gives it). The
   smoke-era interpretation ("last kernel memory before the outage") was
   wrong; the exclusion-for-cause stands independently on the documented
   instrument failure.
3. *Scope-binding stays ~0%* — **CONFIRMED**. Retrieved top-20: 10
   kernel-entity memories, 0 scope-bound. Full-store census: 3,537 memories,
   23 kernel-entity `/checkout` value-memories, **0 scope-bound (0%)** —
   while 18 scope *mentions* survive as separate atoms from 18/18 chain
   sessions. The scope tokens are preserved; the *binding* between scope atom
   and value atom is what extraction destroys.

## Mechanism: discourse-level atomization (H46 rejected)

`[MEASURED]` [H46](../hypothesis/H46-consolidation-scope-smear.md)
(consolidation smears scope as the store grows) is **REJECTED by its own
pre-registered falsification test**: extraction of corpus session s0199 into
an *empty* store (container `masq-audit-h46-size0`, 2026-07-24) already yields
unscoped kernel memories. The smear is store-size-independent. The account
that survives: MASQ prose binds scope at *discourse* level (the scope is named
in a chatter aside — "merged the checkout-web refactor" — while the fact
sentence is unscoped); Supermemory's extraction agent atomizes sessions into
independent one-sentence memories preserving (writer, day) but destroying
cross-sentence co-occurrence. Scope and value end up in different atoms with
no edge between them.

## Limitations

- n=1 core, single domain/seed; the graded numbers are anecdote-level.
- Format asymmetry unresolved: 20 one-sentence memories (~2.7k chars) vs
  session-scale contexts; how much of 31% is starvation is bounded only by
  the still-pending oracle-subset probe (audit item 3 of the smoke page).
- K=20 fixed by pre-registration; K ∈ {40, 80} sensitivity unrun.
- Repair-shaped store: back half re-extracted after a gap, into a store
  already holding front-half memories — deployment-shaped but not identical
  to an uninterrupted ingest.

## Raw artifacts

- [Repair pre-registration](../../masq/harness/REPAIR-PREREG.md)
- [Verification JSON](../../masq/generator/headline/rate-limit/s4001/60k/repair-verification-masq-rate-limit-s4001-60k-cc.json) · [full-store census JSON](../../masq/generator/headline/rate-limit/s4001/60k/audit-census-masq-rate-limit-s4001-60k-cc.json)
- [Merged results JSON](../../masq/generator/headline/rate-limit/s4001/60k/results-rate-limit-claude-opus-4-8.json) (7 arms)
- Repair log: [repair-overnight.log](../../masq/harness/repair-overnight.log) · proxy forensics: [proxy-log.jsonl](../../masq/harness/proxy-log.jsonl)
- Store: container `masq-rate-limit-s4001-60k-cc` (repaired, verified); H46 probe container `masq-audit-h46-size0`

## Related

- [2026-07-22 smoke](./2026-07-22-masq-supermemory-smoke.md) — superseded graded numbers (excluded for cause); mechanism observations upheld
- [H46](../hypothesis/H46-consolidation-scope-smear.md) — REJECTED here
- [H45-exclusion-over-recall](../hypothesis/H45-exclusion-over-recall.md) — read-time sibling; this page adds the write-time half
- [structured-memory-auto-scope-index](../open-question/structured-memory-auto-scope-index.md) — answered for Supermemory: no, it does not auto-build the scope index
- [Supermemory incumbent page](../incumbent/supermemory.md)
