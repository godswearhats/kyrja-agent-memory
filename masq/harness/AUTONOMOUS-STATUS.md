# Autonomous session status (Nils, overnight 2026-06-23)

AJ went AFK ~23:20. Running the v2 calibration→headline pipeline solo.

## Plan (gated, budget-safe)

**Phase 0 — pilot finishing** (old harness, 6k/25k/60k, paste+ceiling). Only
value now is the stored `a_raw` (re-graded free) — its B is superseded by the
B_FORMAT fix.

**Phase 1 — validate fixes on cheap sizes:**
- A re-grade (FREE, no reader calls) via `regrade_a.py`
- B re-run with fixed B_FORMAT via `rerun_b.py` (~72 cheap calls)
- Gate: ceiling A ≥90% AND ceiling B ≥90% (split resolved vs unresolved)

**Phase 2 — headline curve (ONLY if Phase 1 gates pass):**
- Run fixed harness on 150k + 400k (`sweep_run.py`, ~96 calls, guarded reader)
- Re-grade A, combine with cheap sizes → full 5-point degradation curve
- Check escalation gate (paste <85% at 60k) and the predicted ~68/48/32/15/4%

**Stop conditions:** ceiling fails gate → STOP, document, no big spend.
Weekly cap hit (persistent empty/infra-retry exhaustion) → STOP gracefully.

## Two harness bugs found by the pilot (both fixed in run.py)
1. A-grader exact-matched bare GT values vs prose "X team" → LCS cascade.
   Fix: closed-vocab subset match. VALIDATED free: ceiling A 84%→99%.
2. B_FORMAT said "two lines, nothing else" but b_query asked for a rationale;
   no reasoning scaffold → escalation bias on resolved chains. Fix: removed
   contradiction, added chain-trace scaffold, symmetric decision rule,
   last-match parser. Re-run pending.

## GATES PASSED (cleaned harness) — proceeding to headline

Both pre-registered gates clear on 6k/25k/60k after the two fixes:
- Sanity: ceiling A 98%, ceiling B 100% (100% on BOTH resolved & unresolved
  chains — fix 2 killed the escalation bias entirely).
- Escalation: paste-everything B degrades 58%→25%→25% (<<85% at 60k).
- Paste failures are genuine confusability (wrong scope's value, wrong chain
  step, missed real conflict) — not contamination.

Cheap-size curve (paste A / ceil A / paste B / ceil B):
  6k:  89 / 97 / 58 / 100
  25k: 89 / 96 / 25 / 100
  60k: 84 /100 / 25 / 100

Phase 2 (150k/400k) launched to complete the 5-point curve.
Run `python3 final_curve.py` for the assembled table.

## HANDOFF (00:22 2026-06-24) — session cap imminent (89% used)

Weekly usage resets ~01:02; 5-hour session resets ~03:12. A **durable cron
is set for 03:27** to resume after the session reset (re-run any
incomplete/contaminated 150k/400k scenarios on fresh budget, then assemble
`final_curve.py`, verify gates, write the verdict here + to memory).

If resuming manually:
```
cd masq/harness
# 1. check which 150k/400k scenarios are missing or contaminated
#    (contaminated = ceiling B fails or empty a_raw/b_raw):
ls generator/../generator/sweep-v2/*/*/{150k,400k}/results-*.json
# 2. re-run big sizes (guarded reader retries transient rate-limits):
python3 sweep_run.py ../generator/sweep-v2 --sizes 150k,400k --arms paste,ceiling --concurrency 2
# 3. assemble + verify:
python3 final_curve.py
```
Cheap sizes (6k/25k/60k) are FINAL — do not re-run. Both bugs are fixed and
validated; do not revisit run.py grading/format.

## FINAL VERDICT (00:25 2026-06-24)

**Benchmark construction is VALIDATED on cheap sizes. Big sizes need re-run.**

Full curve as it stands (paste A / ceil A / paste B / ceil B):
```
6k    89 / 97 / 58 / 100   CLEAN — final
25k   89 / 96 / 25 / 100   CLEAN — final
60k   84 /100 / 25 / 100   CLEAN — final
150k  20 / 25 /  0 /  25   CONTAMINATED (cap) — re-run
400k  22 / 25 /  8 /  25   CONTAMINATED (cap) — re-run
```
150k/400k ceiling collapsed to 25% (= paste) → rate-limit contamination
during the session/weekly cap (576 infra-retries, 36 ceiling WARNs in
phase2-bigsweep.log). NOT real degradation. Discard and re-run on fresh
budget: `python3 sweep_run.py ../generator/sweep-v2 --sizes 150k,400k --arms paste,ceiling --concurrency 2` then `python3 final_curve.py`.

**What the clean data already establishes:** both pre-registered gates pass
(ceiling A 98% / B 100%; paste B 58→25→25% well under the 85% too-easy
line). The v2 confusability redesign WORKS — paste-everything fails on
genuine disambiguation (wrong scope's value, wrong chain step, missed
unresolved conflict) even when the corpus fits the context window. Once
150k/400k are re-run clean, the 5-point curve is ready and the benchmark is
green-lit for the N=50 headline run.

## Results land in
- `generator/sweep-v2/brerun-claude-opus-4-8.json` (B re-run)
- `generator/sweep-v2/sweep-results-claude-opus-4-8.json` (full sweep, phase 2)
- Final summary appended to this file.

---

## CLEAN FINAL VERDICT (09:?? 2026-06-24) — supersedes the CONTAMINATED block above

Targeted resume of the 9 contaminated big-size scenarios ran on fresh budget:
**4 infra-retries, 0 ceiling WARNs** (vs 276–576 retries / 17–36 WARNs when
capped). That is the fingerprint of an uncontaminated run. Full merged curve:

```
size   paste A  ceil A  paste B  ceil B  n/arm
6k        89%     97%     58%    100%     12
25k       89%     96%     25%    100%     12
60k       84%    100%     25%    100%     12
150k      92%    100%     33%    100%     12
400k      86%    100%     50%    100%     12
SANITY (all sizes): ceiling B 100%  ceiling A 99%   [gate >=90%]  PASS
```

### What is ROBUST (report these)
- **Contamination fixed.** Ceiling clean at 100% across all 5 sizes (n=60).
- **Benchmark VALIDATED.** Pooled ceiling-B 60/60 = **100%** (CI 94–100%) vs
  pooled paste-B 23/60 = **38%** (CI 27–51%). The gap is large and the CIs do
  not overlap at any size. A perfect retriever solves it; paste-everything
  fails ~62% of scenarios *even when the corpus fits the window*. Both
  pre-registered gates PASS (sanity ceiling >=90% everywhere; escalation
  paste <85% at 60k — in fact <85% at every size).
- Paste failures are genuine confusability (wrong scope's value, wrong chain
  step, missed/false conflict), confirmed in the per-scenario FAIL log.

### What is NOT supported (do NOT report as a finding)
- **The degradation-curve-vs-size shape.** Paste-B by size is 58/25/25/33/50%.
  It is **non-monotonic**, and with n=12/size **no two size cells have
  separable 95% CIs** — the wiggle is sampling noise. Paste is statistically
  flat at ~38% across 6k→400k.
- The **pre-registered prediction (68/48/32/15/4, monotonic collapse) is
  falsified in strong form**: paste is 50% at 400k, not ~4%. Honest call:
  this is *consistent with the v2 design intent* — v2 deliberately replaced
  v1's context-overflow mechanism with confusability, decoupling difficulty
  from raw token count. So difficulty does NOT rise with size; the gap is
  size-invariant. That is a cleaner story, not a broken benchmark — but the
  headline must be the **size-invariant ceiling-vs-paste gap**, not "paste
  collapses as the corpus grows."

### Recommended next step (methodology call — Nils)
1. n=12/size is too underpowered to plot any curve. For N=50, **drop the
   "paste collapses with size" framing**; report the pooled ceiling-vs-paste
   gap (and the other arms) with tight CIs, holding size as a secondary axis
   showing *invariance*, not decline.
2. **Pilot only ran paste + ceiling.** The benchmark earns its discriminative
   power from the middle arms — `last-write-wins` and the actual
   `memory-system-under-test` must land BETWEEN ceiling (100%) and paste
   (38%). Run those two arms on the existing sweep-v2 worlds BEFORE the N=50
   headline; that, not the size axis, is the load-bearing result for a
   "SWE-bench for memory" claim.
3. Cheap+big worlds are all generated and clean; only reader calls remain.

---

## LWW ARM ADDED (2026-06-24) — third reference point, clean

Ran `lww` across all 5 sizes (120 calls, conc 2, fresh budget). Clean:
empty=0 everywhere; rl-sig hits were FALSE POSITIVES (the "rate-limit"
domain's own prose). Per-scenario paste/ceiling backed up to `.pc.bak`
and re-merged via `lww_merge.py` (run.py untouched).

```
size    ceiling B   paste B     lww B      lww A-mean
6k      100%        58%         50%        42%
25k     100%        25%         25%         9%
60k     100%        25%         25%        10%
150k    100%        33%         33%         8%
400k    100%        50%         50%        21%
pooled  60/60=100%  23/60=38%   22/60=37%  ~18%
```

### Finding (ROBUST)
- **lww ties paste at the floor (37% vs 38%).** Two opposite naive
  strategies — paste (all info, self-disambiguate) and lww (one note,
  scope-blind) — converge on the same ~chance floor. Naive scope-guessing
  ≈ 1/n_scopes (n=2–5) ≈ 31%; both arms sit barely above it.
- **Benchmark is currently BIMODAL on B:** ~chance-floor (paste, lww) vs
  ceiling (100%). Scope resolution is the entire measured skill. Nothing
  populates the middle yet.
- lww A-mean ≈ chance (steps 0–2/9 at big sizes) — by design it cannot
  reconstruct a chain. A separates lww from ceiling even though B does not
  separate lww from paste.
- Size axis still flat (lww B 50/25/25/33/50) — same non-monotonic noise
  as paste. Reframe holds.

### Implication
The `memory-system-under-test` arm is now THE experiment, not optional.
It must land strictly between ~38% and 100% to make this a *graded*
benchmark. If it also lands at ~38%, the paper's claim becomes
"off-the-shelf memory systems perform at chance on scope-disambiguation"
— bold but publishable. Either way the discriminative result lives in
that arm. That arm does not exist yet (only paste/lww/ceiling in run.py)
— it is a build (pick a system: Mem0/Letta/Zep + write an adapter arm),
to be scoped separately.
