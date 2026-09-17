---
name: xarray Variable setitem .values coerce bug
description: Bug where as_compatible_data in xarray/core/variable.py used getattr duck-typing on .values, incorrectly unwrapping arbitrary objects (e.g. lmfit.ModelResult) assigned into object-dtype Variables. Fix replaces with explicit pandas isinstance check.
type: project
---

# Bug: xarray Variable setitem coerces objects with `.values` attribute

## Symptom
Assigning an arbitrary Python object that happens to expose a `.values` attribute (e.g. `lmfit.ModelResult`, or a minimal `class HasValues: values = 5`) into a `Variable`/`DataArray` with object dtype causes the object to be silently unwrapped — the stored value becomes `obj.values` instead of `obj`. In contrast, an object without `.values` (like `set()`) is preserved as-is.

## Location
`xarray/core/variable.py`, function `as_compatible_data` (starts at line 189). The offending line is around line 221 (just above the `np.asarray(data)` call at line 246). The comment above it reads `# we don't want nested self-described arrays`.

Other key call sites for `as_compatible_data`: lines 139 (Variable.__init__-ish), 330, 367, 468, 858 (__setitem__), 972, 2625. The setitem path goes through `as_compatible_data` on the RHS before assignment.

## Root Cause
The original code used duck-typing:
```python
data = getattr(data, "values", data)
```
This was intended to unwrap `pd.Series` / `pd.Index` / `pd.DataFrame`, but `getattr` triggers on ANY object with a `.values` attribute. Since pandas' `.values` returns an ndarray-like, the code assumed anything exposing `.values` was pandas-ish — a wrong assumption for arbitrary user objects stored in object arrays.

## Fix
Replace duck-typing with explicit pandas type check:
```python
# we don't want nested self-described arrays
if isinstance(data, (pd.Series, pd.Index, pd.DataFrame)):
    data = data.values
```
`pd` is already imported at module top. The fix preserves the intended pandas-unwrapping behavior while leaving arbitrary objects untouched so they can be stored in object-dtype arrays.

## Verification Notes
- Testing via `DataArray.loc[...] = obj` was blocked in this environment by an unrelated `"Assignment destination is a view. Do you want to .copy() array first?"` error from `xarray/core/indexing.py:1307-1311`. Do NOT chase that — it's orthogonal.
- Instead verify by calling `as_compatible_data` directly: pass `HasValues()`, a `pd.Series`, a `pd.Index`, and a `pd.DataFrame`. Expected: HasValues passes through untouched (wrapped as object-dtype ndarray scalar), pandas types get unwrapped to their underlying arrays.
- Test environment gotcha: the worktree's xarray requires `pkg_resources` (deprecated in Py3.14). Use `python` — it has setuptools. System `/usr/bin/python` (3.14.4) does not.

## Pre-existing Test Failures (DO NOT blame on this fix)
Running `pytest xarray/tests/test_variable.py` produces 19 failures both WITH and WITHOUT the patch. They are numpy datetime64 precision issues (e.g. `test_index_0d_datetime`, `test_0d_timedelta`, `test_timedelta64_conversion_scalar`, `TestAsCompatibleData::test_datetime`, `test_unchanged_types`). Always diff test output against a `git stash` baseline before attributing failures to your change.

## Worktree Path
`bootstrap_variable_setitem_coerce` — this is a bootstrap/demo worktree. The fix matches the memory index entry `bug_xarray_variable_setitem_coerce.md`, which is the canonical record for this bug across worktrees.

## Gotchas for Future Work
1. `getattr(x, "attr", x)` as an unwrap pattern is fragile whenever the container allows arbitrary object dtypes — prefer `isinstance` checks against the exact types you mean to unwrap.
2. The sibling `IndexVariable.copy(deep=True)` unicode-dtype bug (see `bug_xarray_indexvariable_copy_unicode_dtype.md`) lives in the same module family — worth checking if you're touching adapter wrapping logic.
3. `as_compatible_data` is called on the RHS of `Variable.__setitem__` at line 858 — that's why the bug manifests during assignment, not just construction.