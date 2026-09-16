---
type: experiment
name: MASQ Supermemory smoke core (system #2, first structured-memory arm)
status: EXCLUDED-FOR-CAUSE (graded numbers); mechanism observations upheld
last_ingested: 2026-07-25
sources: []
epistemic_tags: [EXCLUDED-FOR-CAUSE]
tags: [masq, supermemory, extraction-first, scope-smear, system-under-test, v2]
---

> **2026-07-25 UPDATE — graded numbers EXCLUDED FOR CAUSE.** The audit AJ
> called for found a documented instrument failure: a subscription-cap outage
> (23:38:07Z 2026-07-21) plus a supermemory-server v0.0.3 silent-failure bug
> left **340/626 documents with zero extracted memories** — the smoke queried
> a store missing everything from world-day ~80 on. A=8%/B-FAIL are excluded
> as measurements of Supermemory (evidence retained below). The store was
> repaired, verified, and re-run: see
> [2026-07-25 repair experiment](./2026-07-25-masq-supermemory-repair.md)
> (valid result: A=31%, B-FAIL `set_50`; scope-binding 0% confirmed on the
> full repaired store). Corrections to this page are marked ⚠ inline. The
> `set_50` reading below ("another scope's most recent value... before the
> outage") was wrong in its outage clause: `set_50` is the canonical
> scope-blind wrong answer on this core — every scope-blind arm gives it,
> outage or not.

First run of a real memory-system-under-test on MASQ: Supermemory (self-hosted
v0.0.3, extraction-first, embedded graph) on one 60k core
(rate-limit/s4001), extraction by claude-opus-4-8. **Verdict was held
PRELIMINARY and methodology-suspect by AJ's call (2026-07-22)** — vindicated:
the audit excluded the graded numbers for cause (see banner).

## Hypotheses tested

- [H45-exclusion-over-recall](../hypothesis/H45-exclusion-over-recall.md) — extends the exclusion story from read-time ranking to write-time extraction (context only; H45's own claim unchanged)
- [H46-consolidation-scope-smear](../hypothesis/H46-consolidation-scope-smear.md) — PROPOSED here; this experiment supplies its motivating observation

## Method

Same fixed arm contract as every MASQ arm (`arm_fn(family, corpus) → context`;
reader claude-opus-4-8 + closed-form grader untouched). Arm:
[arm_supermemory.py](../../masq/harness/arm_supermemory.py).
Deployment-shaped ingest: one document per world session (626 docs), writer/day
header + prose, idempotent via custom_id; query = `a_query`, K=20 memories,
server defaults, relevance order (pre-registered 2026-07-15).

**Extraction model = claude-opus-4-8 throughout, two transports:**

1. *API transport* (Anthropic OpenAI-compat endpoint; ~323 docs before credit
   exhaustion) — retained as fidelity control. Cost forensics `[MEASURED]`:
   ~35¢/doc — the memory agent is a multi-round tool-calling loop (3+ LLM
   calls/doc) with no prompt caching on the compat path, so the fixed prefix
   re-bills every round. Native provider path was rejected: it hardcodes
   claude-haiku-4-5 (silent model confound).
2. *CLI transport* (all 626 docs, the experiment store): local
   OpenAI-compat proxy backed by `claude -p`
   ([smem_claude_proxy.py](../../masq/harness/smem_claude_proxy.py)),
   subscription-billed, prompt-cache-absorbed. Tool calling is prompt-encoded
   (the one transport difference); ⚠ *corrected 2026-07-25:* 883 successful
   calls / 2,166 rc=1 (the cap outage), not the "~2,900 successful, 0 parse
   errors" originally recorded here.
   **Shim fidelity check `[MEASURED]`:** scope-binding rate of retrieved
   kernel-entity memories identical across transports (0/6 CLI vs 0/13 API) —
   the failure signature is Supermemory's, not the shim's.

## Results

| arm (this core) | A-score | B |
|---|---|---|
| ceiling | 100% | PASS |
| paste | 69% ⚠ | (baseline set) |
| vector_k10 | 69% ⚠ | (baseline set) |
| **supermemory-k20** | **8% — EXCLUDED** | **FAIL — EXCLUDED** |

⚠ paste/vector corrected 2026-07-25 to the merged results JSON (84%/79% were
mistranscribed). `[EXCLUDED-FOR-CAUSE]` Supermemory landed *below* the
scope-blind floor — on a store missing 340/626 documents:
0/9 chain steps reconstructed, and the B action taken was another scope's
most recent value. n=1 core — no endpoint claim (pre-registered endpoints are
15-core counts).

**Mechanistic read `[MEASURED]` (upheld post-repair):** 18/18 chain-session
prose texts name their scope — ⚠ *wording sharpened 2026-07-25:* in a
**discourse aside** ("merged the checkout-web refactor…"), not bound to the
fact sentence, which is unscoped. 0 of the kernel-entity (`/checkout`)
rate-limit memories in the retrieved top-40 carry any scope qualifier, on
both transports. Writer,
day, and value are preserved; the scope binding is dropped. Near-miss
*endpoints* (`/checkout-admin` etc.) survive because they are part of the path
string; the five confusable *scopes* qualifying the same endpoint do not.

### Construct-validity note

Two known gaps, which are exactly why the verdict is held preliminary:
(1) the 0% scope-binding census was taken over **retrieved top-40 memories,
not the full ~1,800-memory store** — if scope-bound memories exist but are
out-ranked, the failure is partly retrieval-budget, not write-time
destruction; (2) the arm's context (20 one-sentence memories, ~2.7k chars) is
format-asymmetric vs. session-based arms (paste ~274k chars; scope-filter full
target sessions) — A-score may be depressed by starvation independent of
scope-smear. Both are audit items, not resolved.

## Limitations

- n=1 core, single domain (rate-limit), single seed — anecdote-level for the
  graded numbers; only the scope-binding measurement has within-core n.
- Retrieved-set census, not full-store census (see construct-validity note).
- K=20 fixed by pre-registration; no k-sensitivity sweep yet.
- API-transport store is partial (~323/626 docs) — fidelity comparison is on
  matched retrieval procedure, not matched corpus coverage.
- Cap-stall/resume cycles during ingest (session usage limits) — extraction
  completed across 2 sessions; no evidence this affects extraction content,
  but it is uncontrolled.

## Pre-registered follow-ups (gate the 14-core sweep — AJ 2026-07-22)

AJ's standing call: *a result this bad is methodology-suspect until audited.*

1. **Full-store scope-binding census** — ✅ DONE 2026-07-24/25: on the
   repaired 3,537-memory store, 23 kernel-entity memories, 0 scope-bound —
   the 0% is write-time destruction, not retrieval-budget
   ([repair experiment](./2026-07-25-masq-supermemory-repair.md)).
2. **Retrieval-budget sensitivity** — K ∈ {20, 40, 80}: still pending.
3. **Format-asymmetry probe** — oracle-selected memory subset: still pending
   (now bounds A=31%, not A=8%).
4. **H46 store-size sweep** — ✅ resolved short of the full sweep: the
   store-size-0 probe already rejected H46 (see hypothesis page).

## Raw artifacts

- Results JSON (merged, all 7 arms): [results-rate-limit-claude-opus-4-8.json](../../masq/generator/headline/rate-limit/s4001/60k/results-rate-limit-claude-opus-4-8.json)
- Proxy call log (cost/cap forensics): [proxy-log.jsonl](../../masq/harness/proxy-log.jsonl)
- Stores: supermemory containers `masq-rate-limit-s4001-60k-cc` (CLI, complete) and `masq-rate-limit-s4001-60k` (API, fidelity control), local server data `.supermemory` (indigo container)

## Related

- [2026-07-25 repair experiment](./2026-07-25-masq-supermemory-repair.md) — **supersedes this page's graded numbers**; carries the valid result + mechanism
- [structured-memory-auto-scope-index](../open-question/structured-memory-auto-scope-index.md) — the question this experiment begins to answer
- [H46-consolidation-scope-smear](../hypothesis/H46-consolidation-scope-smear.md) — mechanism hypothesis spawned here
- [Supermemory incumbent page](../incumbent/supermemory.md) — vendor claims vs. this measurement
- [2026-06-30 retrieval arms](./2026-06-30-masq-retrieval-arms.md) — the read-time half of the exclusion story
- [structured-filter-first](../decision/structured-filter-first.md) — deployability decision this informs
