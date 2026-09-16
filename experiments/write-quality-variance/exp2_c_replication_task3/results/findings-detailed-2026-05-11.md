# Exp 2 — C-Replication on Task 3 — Detailed Findings

**Date:** 2026-05-11
**Spec:** `../spec.md`
**Summary:** `findings-summary-2026-05-11.md`

## Setup

- **Target task:** `where_keep_attrs_coord` (pydata__xarray-7229). Tier 1, Task 3 in the Phase 2 causal chain.
- **Memory source:** Task 2 (`where_keep_attrs_scalar`) full transcript from Phase 2 bootstrap.
- **Distiller:** Opus 4.6 (explicit, not the `opus` alias which now resolves to 4.7).
- **Agent (downstream):** Opus 4.6.
- **Variants:** cold (no memory), A (prose briefing), C (structured slots). B and D dropped from this replication to focus on the core question.
- **n:** 4 per variant × 3 variants = 12 trials. Plus 4 contaminated cold trials run before the harness fix (archived).

## Raw results

```
variant     n    mean_$     std_$         95% CI ($)     out_tok    turns    pass
cold        4     1.334     0.194      [1.175,1.521]       17753     28.8     0/4
A           4     1.105     0.163      [0.957,1.249]       15346     26.5     0/4
C           4     0.805     0.131      [0.698,0.912]       12434     22.8     0/4
```

Individual trial costs:
- cold: $1.297, $1.128, $1.316, $1.595
- A: $1.300, $1.097, $1.122, $0.902
- C: $0.906, $0.647, $0.919, $0.749

## Mid-experiment course correction

The first cold sweep (archived at `data/preliminary/`) hit both pre-registered halt rules:
1. **Halt rule 5 (cold cost band):** observed $0.55–$0.95, expected $0.15–$0.50.
2. **Halt rule 6 (cold pass rate ≥ 3/4):** observed 1/4.

Investigation revealed: 3 of the 4 cold "FAIL"s were inconclusive, not genuine failures. Agents wrote their own tests in `xarray/tests/test_computation.py`, which broke `git apply` of the gold test_patch ("patch failed: xarray/tests/test_computation.py:1925"). Agents had produced fixes; the harness couldn't evaluate them.

**Harness fix** (committed mid-experiment): `evaluate_patch` now resets any test file modified by the gold test_patch back to `base_commit` before applying the patch. Preserves agent's source-code fix; discards agent's test additions. Standard SWE-bench-style evaluation pattern.

After the fix, the cold sweep was re-run from scratch. The cost variance turned out to be real (mean $1.33 vs Task 2's $0.30) — Task 3 is genuinely harder. We continued with pass-rate added as a co-primary signal, treating "memory swings pass-rate on a hard task" as the more interpretable signal than cost on this baseline.

That bet did not pay off — pass-rate stayed 0/4 across all variants, and on inspection, for reasons that have nothing to do with whether memory helps.

## Why pass-rate is 0/4 across all variants

The forensic on this is the most important content of the experiment, because it's the part that retracts the quality framing.

### What every agent did

Across all 12 trials (cold, A, C), agents converged on essentially **the same fix**:

1. Pass `keep_attrs="override"` to `apply_ufunc` for coordinate merging (instead of using the lambda).
2. After the call, set `result.attrs = getattr(x, "attrs", {})` for data-variable attrs.

This is true for cold (which derived it from the issue's hints) and for A/C (which received it via memory). All 12 trials cite the closure-based `getattr(x, "attrs", {})` pattern from Task 2.

Wording samples:

> *(cold r1)* "Pass `keep_attrs="override"` to `apply_ufunc`, which correctly preserves coordinate attributes from the inputs. After the call, manually set `result.attrs = getattr(x, "attrs", {})`."

> *(A r2)* "The fix passes `"override"` as the `keep_attrs` strategy to `apply_ufunc`, then manually sets `result.attrs` from `x`. This handles both the original scalar-`x` case (#6461) and the coordinate attrs case (#7229)."

> *(C r2)* "Pass `"override"` to `apply_ufunc`, then manually set `result.attrs = getattr(x, "attrs", {})`. This preserves coordinate attrs while still keeping `x`'s data variable attrs, and remains safe for the scalar `x` case from #6461."

### Why the gold test fails them

The gold `test_where_attrs` exercises five cases:

```python
cond["a"].attrs = {"attr": "cond_coord"}   # cond's coord attr
x["a"].attrs    = {"attr": "x_coord"}      # x's coord attr
y["a"].attrs    = {"attr": "y_coord"}      # y's coord attr

# Case 1: three DataArrays. EXPECTED coord attr: "x_coord" (from x).
```

The agents' fix uses `keep_attrs="override"` for coordinate merging. `"override"` semantics in xarray is "preserve coord attrs from the **first** matching input" — which is `cond`. So the agents' fix produces `"cond_coord"` where the test expects `"x_coord"`.

This is a **subtle correctness bug shared by all 12 agents**. They're using the wrong xarray merge semantics for "preserve x's coord attrs" — they need a strategy that takes attrs from a specific input by position, not "first input wins."

The issue's stated bug ("coordinate attributes are getting overwritten by *variable* attributes") doesn't mention which-input-supplies-the-coord-attr. The MVCE uses the same DataArray for x and y (`xr.where(True, ds.air, ds.air, ...)`), so the question "x's coord attrs or cond's coord attrs?" doesn't arise. The maintainer's expanded test introduces the disambiguation as part of the fix's evaluation. Agents had no way to learn about this constraint from the issue text or from Task 2's memory.

### Why memory doesn't help here

Task 2's memory describes the closure-based access for `x`'s **top-level (data variable)** attrs in the scalar case. It says nothing about coord-level attribute sourcing. Both pieces of information are about `x.attrs`, but at different levels (DataArray.attrs vs DataArray.coords["a"].attrs). The agent's fix correctly applies the closure pattern at the data-variable level (`result.attrs = getattr(x, "attrs", {})`) but uses the wrong strategy (`"override"`) at the coord level.

No amount of better encoding of Task 2's fix would change this, because the failing invariant is not in Task 2's domain.

### Behavioral side finding: memory short-circuits self-verification

A separate, real behavior change visible in the trial logs:

- **Cold (4/4):** Each agent wrote a new test in `xarray/tests/test_computation.py`. They cite specific line numbers (1938-1947, 1940-1962, etc.). They added tests like `test_where_attrs_preserve_coord_attrs`.
- **A (0/4):** None mentioned writing a test. They described the fix and stopped.
- **C (1/4):** Only C r1 explicitly ran existing tests ("All 57 `keep_attrs` tests pass"). C r2-r4 didn't mention testing at all.

Memory-equipped agents skip writing their own verification tests. They trust the prior pattern. This is presumably part of where the cost savings come from — fewer turns spent constructing and running self-written tests.

It's also a risk to flag for production: if memory makes an agent overconfident, and the prior pattern doesn't cover a new edge case, the agent ships a wrong fix faster than they would have without memory.

### Memory is partly redundant with the prompt

The cold prompt's "Hints" section (written by the issue reporter, included in the SWE-bench problem statement) **already contains Task 2's fix**:

> Original looks like this:
> ```python
> keep_attrs = lambda attrs, context: attrs[1]
> ```
> New one looks like this:
> ```python
> keep_attrs = lambda attrs, context: getattr(x, "attrs", {})
> ```

The reporter also discusses `_get_all_of_type`, scalar handling, and links to the original PR discussion threads. So cold agents are not ignorant of Task 2 — they have Task 2's fix described in prose form in the issue.

This reframes what the cost win measures:
- C beating cold is **"structured memory + prose hints" vs "prose hints alone"**, not "memory vs no memory."
- The 40% reduction is at least partly a presentation-format effect on already-available information.
- The clean version of the experiment would have a `cold-no-hints` arm (strip the `## Hints` section). I'd predict the gap between cold-with-hints and cold-no-hints accounts for a meaningful portion of the wedge value we've been attributing to memory.

## What this implies for Exp 1

Exp 1 (Task 2, where_keep_attrs_scalar) ran in the same harness with the same evaluation. The same issue applies retroactively:

- Exp 1 cost numbers are real and stand. Slot-format wins on cost: replicated.
- Exp 1 pass-rate numbers (3/4, 4/4 mostly) were higher than Exp 2's. That's because Task 2 is easier and the agent's "minimal fix matching the issue" happens to align with the gold test more often. It's not strong evidence that memory helps quality.
- The Exp 1 finding "Variant D didn't degrade" should be re-read as "Variant D didn't degrade on cost." Whether it degraded quality is unmeasured by the same yardstick.

## What this implies for the wedge

1. **Slot-format encoding is the working architectural assumption.** Both replications support this. Distiller-version-independent. Commit to slot format for MTP.
2. **The Phase 2 cost-savings claim survives.** Two independent SWE-bench-derived experiments at n=4 each show ~17% for prose memory, ~40-50% for slot memory, on causally-related tasks within the same file.
3. **The Phase 2 quality-stays-good claim is unmeasured.** Pass-rate on SWE-bench gold tests is not a clean read on this. We don't actually know whether memory affects fix quality up or down.
4. **The "memory makes agents overconfident" hypothesis is novel and worth flagging.** Cold agents wrote tests; memory agents didn't. If this generalizes, it's a real failure mode of the wedge.

## What to do next

**Recommended:** Move to Goal 5 (MTP build). Real-codebase usage on AJ's own work will give us a much cleaner read on "does memory help in production" than any SWE-bench-derived experiment can.

**Optional, low-cost experiments if we want more signal first:**
1. **cold-no-hints arm** on Task 3 (~$5). Bounds the marginal value of structured memory beyond prose hints. Single condition, 4 trials, easy to fold into existing harness.
2. **LLM-as-judge on diffs** from the 12 existing trials (~$1). Have a judge LLM read the agent's diff and the stated problem (no edge cases) and rate "does this fix the stated bug." Tests whether all 12 fixes are equivalent in stated-bug-solving quality, which would confirm that cost is the only differentiator and that memory neither helps nor hurts stated-bug quality.

**Deferred:**
- Worst-case source experiment (follow-up #1). The eval-framework problem makes this not worth doing here.
- Cross-repo Sphinx generalization. Same reason.

## Methodology callouts

- **Pre-registration caught the harness bug.** The cost-band halt rule on cold trial 1 fired immediately and forced a diagnostic step. Without it, we'd have run all 12 trials, seen 0/4 pass everywhere, and incorrectly concluded "memory doesn't affect quality." Instead, we identified the test-file-reset issue and re-ran. Good methodology hygiene paying off.
- **Pre-registration also forced the harder honesty.** We had to write down before the run that 0/4 pass meant H-MEMORY-NO-TRANSFER and look at the actual failure modes. That's how we discovered the convergent-fix and shared-invariant findings — not by celebrating a cost win.
- **n=4 is still underpowered for the magnitudes question.** Across both Exp 1 and Exp 2, the C-vs-A and C-vs-cold gaps are wide enough at n=4 to land on disjoint CIs. The A-vs-cold gap is not. If A's effect were the headline (it isn't), we'd need n=8+.
- **One uncaptured invariant per trial:** the agent's actual diff. The current harness discards the worktree after evaluation. Adding `git diff base_commit` to the trial log before destroying the worktree would be a small change with large forensic value. Recommended for any future runs.

## Artifacts

```
exp2_c_replication_task3/
├── spec.md                              (with mid-run amendment)
├── sources/task2_full.md                (Phase 2 bootstrap)
├── encodings/
│   ├── A_encoding.md  A_meta.json       (Opus 4.6-distilled)
│   └── C_encoding.md  C_meta.json
├── harness/
│   ├── generate_encoding.py             (4.6 distiller, Task 2 source)
│   ├── run_variant.py                   (Task 3 target, test-file reset)
│   ├── run_sweep.sh
│   └── analyze.py
├── data/
│   ├── trials.json                      (12 trials, v2)
│   ├── trial_logs/                      (per-trial JSON)
│   ├── sweep_v2.log
│   └── preliminary/                     (4 contaminated cold trials, v1 harness)
└── results/
    ├── findings-summary-2026-05-11.md
    └── findings-detailed-2026-05-11.md  (this doc)
```
