---
name: xarray IndexVariable.copy(deep=True) drops unicode dtype
description: Bug in xarray/core/variable.py IndexVariable.copy where deep-copying an index variable with <U* dtype silently coerces to object; fix forwards dtype to PandasIndexAdapter
type: project
---

## Bug

When calling `IndexVariable.copy(deep=True)` on an index variable backed by a unicode-dtype array (e.g. `<U3`), the copy comes back with `dtype=object`. Same regression hits `Dataset.copy(deep=True)` and `DataArray.copy()` whenever a string coord is involved. Symptom: round-tripping a Dataset with string coords through `.copy(deep=True)` mutates dtype metadata even though values look identical.

## Location

- File: `xarray/core/variable.py`
- Function: `IndexVariable.copy`, around lines 1944–1955 (in the `if data is None: if deep:` branch)
- Related class: `PandasIndexAdapter` at `xarray/core/indexing.py:1229` — its `__init__(self, array, dtype=None)` is what stores the shadow `_dtype`
- Originating commit that introduced the deep-copy path: `c04234d` ("BUGFIX: deep-copy wasn't copying coords, bug fixed within IndexVariable (#2936)", May 2019)

## Root cause

`PandasIndexAdapter` exists precisely because `pandas.Index` stores strings as object dtype internally, while xarray wants to preserve the original numpy dtype (`<U3`, etc.). The adapter holds the real dtype in a shadow `self._dtype` attribute set from the `dtype=` kwarg.

The deep-copy branch did:
```python
data = PandasIndexAdapter(self._data.array.copy(deep=True))
```
That constructs a fresh adapter with `dtype=None`, so it re-infers from `self.array` — which is a `pd.Index` of strings, i.e. object dtype. The original adapter's shadow dtype is silently dropped.

Verified at the pandas level: `pd.Index(np.array(['foo'], dtype='<U3'))` reports object/str internally; `np.asarray(idx, dtype='<U3')` recovers the unicode dtype, but `np.asarray(idx)` returns object. So the adapter MUST be told the original dtype — it cannot recover it from the index alone.

## Fix

Pass `dtype=self._data.dtype` through to the new adapter:

```python
data = PandasIndexAdapter(self._data.array.copy(deep=True), dtype=self._data.dtype)
```

`self._data.dtype` reads the shadow `_dtype` from the original `PandasIndexAdapter`, so the new adapter is constructed with the same authoritative dtype rather than re-inferring it.

## Investigation notes / gotchas

- The repo is laid out under `worktrees/bootstrap_copy_deep_unicode/` inside `phase2-utility`. It's a checkout of an older xarray (pre–numpy 2.0). The system numpy in `.venv` is 2.4.4, which removed `np.unicode_` — so `import xarray` from this checkout immediately raises `AttributeError: np.unicode_ was removed in the NumPy 2.0 release`. You cannot run xarray's own test suite in-tree against the workspace venv. Either spin up a numpy<2 env, or validate the dtype-preservation logic at the pandas/numpy layer directly (as was done here).
- Tests for the original deep-copy regression live in `xarray/tests/test_dataset.py` and `xarray/tests/test_dataarray.py` (added in commit `c04234d`). Any new test for the unicode-dtype regression should sit alongside them and assert `ds.copy(deep=True).coords['x'].dtype == ds.coords['x'].dtype` for a string coord.
- The `if data is None / if deep` branch has a sibling `else: data = self._data` (shallow) which is unaffected — shallow copy keeps the same adapter object so dtype is naturally preserved. Only the deep branch needed the dtype forwarded.
- Do not be tempted to "fix" this in `PandasIndexAdapter.__init__` by inferring dtype from `array.values` — pandas has already coerced strings to object by then. The dtype must be threaded through from the caller that still has the original.
- The MultiIndex comment in the surrounding code ("doesn't have a copy method, so make a deep copy of the underlying pandas.MultiIndex") explains *why* the branch reconstructs an adapter rather than calling `.copy()` on it — that constraint is what makes dtype-forwarding necessary in the first place.