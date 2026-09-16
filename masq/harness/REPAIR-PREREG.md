# Pre-registration: Supermemory store repair + reader re-run

**Written 2026-07-24, before the repaired-store reader runs.** (Nils/indigo;
AJ approved plan + overnight schedule same day.)

## What happened (excluded-for-cause)

The 2026-07-22 smoke numbers (A=8%, B=FAIL `set_50`) are EXCLUDED for
documented instrument failure, not for being disappointing: the subscription
cap killed every `claude -p` call from 23:38:07Z (2,166/3,049 proxy calls
rc=1, one contiguous 53-min window), supermemory-server v0.0.3 marked the
affected docs done-with-zero-memories, and 340/626 docs (all sessions from
world-day ~80 on) contributed nothing to the store. `set_50` is the most
recent kernel memory extracted before the outage.

## The repair

Re-extract the 340 zero-yield docs, chronological order, claude-opus-4-8 via
the throttled stall-on-cap proxy (150 calls/h). Store is valid iff the final
census shows every doc >= 1 memory and no unrepaired error-window docs
(`audit_repair.py` verification JSON must be `pass: true`).

## Predictions (registered before the reader runs)

1. **A-score rises off the below-floor artifact.** Directional: toward the
   vector-arm region (vector_k10 = 79% on this core), not to ceiling. No
   point prediction — format asymmetry (20 one-sentence memories vs full
   sessions) is an unresolved confound either way.
2. **B: no prediction on pass/fail** (n=1 core; B on this benchmark is a
   step function on scope purity and the retrieved set changes wholesale).
   Registered expectation: the specific `set_50` answer disappears; if B
   still fails it fails by confusing a *different* sibling scope's value.
3. **Scope-binding of retrieved kernel-entity memories stays ~0%.** The
   atomization mechanism (scope lives in a chatter aside; extraction emits
   independent facts) is store-completeness-independent — demonstrated at
   store-size 0 on 2026-07-24 (container `masq-audit-h46-size0`). If
   binding jumps with a complete store, the atomization account is wrong.

## Decision rules

- These numbers REPLACE the smoke as the system #2 single-core result; the
  smoke page is annotated excluded-for-cause, evidence retained.
- K=20 and all 2026-07-15 pre-registrations stand unchanged. n=1 core:
  no endpoint claims either way (endpoints remain 15-core counts).
- If verification FAILs, no reader run — repair issues get fixed first;
  a reader result on an unverified store is not reportable under any label.
