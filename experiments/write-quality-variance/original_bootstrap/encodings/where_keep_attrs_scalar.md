---
name: xarray xr.where keep_attrs scalar IndexError
description: xr.where with keep_attrs=True raises IndexError when x (second arg) is a scalar; fix grabs x.attrs via closure instead of indexing filtered attrs list
type: project
---

## Bug

`xr.where(cond, x, y)` with `keep_attrs=True` (either explicit or via `xr.set_options(keep_attrs=True)`) raises `IndexError: list index out of range` when `x` is a scalar (non-xarray) argument. Example: `xr.where(da > 0, 1, 0)` under `keep_attrs=True`.

## Location

`xarray/core/computation.py:1832` inside the `where` function. The offending code was:

```python
keep_attrs = lambda attrs, context: attrs[1]
```

This lambda is passed as `combine_attrs` into `apply_ufunc`, intended to return `x`'s attrs (the second positional arg to `where`).

## Root cause

`apply_ufunc` builds the `attrs` list passed to the `combine_attrs` callback by filtering args down to **only xarray objects** (DataArray/Dataset) — scalars and plain arrays are dropped before the list is assembled. So when `where(cond_da, 1, 0)` is called, `attrs` is `[cond_da.attrs]` (length 1), and `attrs[1]` is out of bounds. The lambda assumed positional indexing matching the original `where` signature, but that assumption breaks the moment any of `cond`/`x`/`y` is non-xarray.

See `xarray/core/computation.py:289` and `:311` (`merge_attrs([x.attrs for x in objs], combine_attrs=keep_attrs)`) where `objs` is the already-filtered xarray-only list.

## Fix

Replace the lambda with one that captures `x` via closure and reads its attrs directly:

```python
keep_attrs = lambda attrs, context: getattr(x, "attrs", {})
```

`getattr(..., "attrs", {})` is safe for scalars (returns `{}`), DataArrays, and Datasets. This matches the documented intent — "keep the attributes of x, the second parameter, by default to be consistent with the `where` method of `Dataset` and `DataArray`" — without relying on brittle positional indexing into a filtered list.

## Verification

Ran under `python` (numpy 1.26.4). Cases tested:
- `xr.where(da > 0, 1, 0)` — scalar x, previously crashed, now returns `[1 1 1]`
- Same call under `xr.set_options(keep_attrs=True)` — works, empty attrs
- `xr.where(cond, da_with_attrs, 0)` — attrs from `x` preserved
- `xr.where(cond, x_da, y_da)` — attrs from `x` preserved

## Gotchas for future work in this area

1. **`apply_ufunc` filters args before calling `combine_attrs`.** Any `combine_attrs` callable that uses positional indexing (`attrs[n]`) must account for the fact that `n` is an index into the xarray-only subset, not the original call args. If you need a specific arg's attrs, capture it via closure instead.
2. **`merge_attrs` lives in `xarray/core/merge.py`** and normally expects a string `combine_attrs` like `"override"`, `"drop"`, `"no_conflicts"`, etc. Passing a callable is supported but the callable contract (signature `(attrs_list, context)`) is under-documented — follow the `where` pattern of closing over the variable you actually want.
3. **`keep_attrs` in `where` has two layers:** the outer `keep_attrs` bool (resolved from `_get_keep_attrs(default=False)` at `computation.py:1827`) and the inner lambda that implements the "attrs-of-x" semantics. The outer bool gates whether the lambda is used at all; the lambda is where the scalar bug lived.
4. **Related memory already exists:** `bug_xarray_where_keep_attrs.md` covers a different earlier fix (adding the `keep_attrs` kwarg to `xr.where` in the first place). This bug is the follow-on: the kwarg exists but its implementation assumed all three args were xarray objects.
5. Worktrees under `research/experiments/phase2-utility/worktrees/` do not have their own venv — use `python` with `sys.path.insert(0, '.')` to exercise the worktree's xarray source.