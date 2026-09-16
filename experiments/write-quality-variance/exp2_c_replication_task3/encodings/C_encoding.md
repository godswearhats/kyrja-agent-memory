```
BUG: `xr.where(cond, scalar_x, y)` with `keep_attrs=True` raises an IndexError. The `keep_attrs` lambda `lambda attrs, context: attrs[1]` assumes `x` is always in the attrs list, but `apply_ufunc` filters out non-xarray args before building that list. When `x` is a scalar (e.g., `xr.where(da > 0, 1, 0)`), the attrs list has fewer entries than expected, so `attrs[1]` goes out of bounds.

LOCATION:
  - file: xarray/core/computation.py
  - function: where (module-level)
  - line: 1832
  - related_locations: [xarray/core/computation.py:apply_dataarray_vfunc:280-318, xarray/core/merge.py:merge_attrs]

FIX_PATTERN: Replace index-based access into a filtered attrs list (`attrs[1]`) with direct attribute access on the original argument via closure (`getattr(x, "attrs", {})`), bypassing the filtered list entirely and making it safe for scalar inputs.

CODE_CHANGES:
  - xarray/core/computation.py:1832, old → `keep_attrs = lambda attrs, context: attrs[1]`, new → `keep_attrs = lambda attrs, context: getattr(x, "attrs", {})`

RELATED_IMPORTS_AND_UTILITIES: `_get_keep_attrs` from `xarray/core/options` (used at line 1827 to check user setting), `merge_attrs` from `xarray/core/merge` (called downstream with the `keep_attrs` value), `apply_dataarray_vfunc` (lines 280-318, where attrs list is built from xarray-only objects and `merge_attrs` is called).

DEAD_ENDS: NONE

GOTCHAS: `apply_ufunc` internally filters args to only xarray types (DataArray/Dataset) before constructing the attrs list passed to the `keep_attrs` callable. This means positional indices into `attrs` do not correspond to positional indices of the original function arguments when some args are scalars. Any callable `keep_attrs` that indexes into the attrs list must account for this filtering.

VERIFICATION: Ran manual tests via the project venv: (1) `xr.where(DataArray([1,2,3]) > 0, 1, 0)` — scalar x, previously crashed, now returns correct values; (2) `xr.where` with `keep_attrs=True` via `set_options` and scalar x; (3) `xr.where` with DataArray x having `attrs={'foo':'bar'}` — attrs correctly preserved on result; (4) both x and y as DataArrays — x's attrs preserved.
```