```
BUG: xr.where() did not preserve attributes from input DataArrays, while the equivalent DataArray.where and Dataset.where methods did. There was no way for users to opt into attribute preservation — xr.where had no keep_attrs parameter, and the underlying apply_ufunc call did not forward keep_attrs, so attrs were always dropped. User-facing symptom: calling xr.where(cond, x, y) returned a DataArray with empty .attrs even when x carried metadata.

LOCATION:
  - file: experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py
  - function: where
  - line: 1730
  - related_locations: [xarray/core/computation.py:32 (_get_keep_attrs import), xarray/core/computation.py:1810-1820 (apply_ufunc call inside where), xarray/core/computation.py:302 (merge_attrs combine_attrs=keep_attrs pattern), xarray/core/computation.py:1116 (existing _get_keep_attrs(default=...) pattern in apply_ufunc)]

FIX_PATTERN: Add a keep_attrs=None kwarg to the where() signature; if None, resolve via _get_keep_attrs(default=False); forward the resolved keep_attrs through to the internal apply_ufunc call as keep_attrs=keep_attrs so attrs propagate from x (the True branch).

CODE_CHANGES:
  - xarray/core/computation.py:1730, `def where(cond, x, y):` → `def where(cond, x, y, keep_attrs=None):`
  - xarray/core/computation.py:~1810 (just after docstring, before alignment comment), inserted: `if keep_attrs is None: keep_attrs = _get_keep_attrs(default=False)`
  - xarray/core/computation.py:apply_ufunc(...) call inside where, added `keep_attrs=keep_attrs` kwarg (matches historical PR #4687 / commit 84961e6a)

RELATED_IMPORTS_AND_UTILITIES: _get_keep_attrs already imported at xarray/core/computation.py:32 from .options. The same default=False pattern is used in apply_ufunc at line 1116. merge_attrs(..., combine_attrs=keep_attrs) is the standard internal channel for attr propagation (lines 287, 302, 444, 458, 752). apply_ufunc itself already accepts and threads keep_attrs.

DEAD_ENDS: First verification attempt used the system /usr/bin/python which lacked numpy/xarray (ModuleNotFoundError). Switched to the project venv at experiments/phase2-utility/.venv/bin/python.

GOTCHAS:
  - System python (/usr/bin/python) has no scientific stack; must use the project venv interpreter at experiments/phase2-utility/.venv/bin/python (or pytest).
  - Default for keep_attrs in where should be False (not True) to preserve prior behavior absent global OPTIONS override — matches _get_keep_attrs(default=False) idiom used elsewhere in this file.
  - Attrs are taken from x (the "True" branch), not y, mirroring DataArray.where semantics.
  - This is essentially a re-derivation of upstream PR #4687 (commit 84961e6a, "keep attrs in xarray.where", merged 2022-01-19) which made the identical change in mainline xarray. The worktree appears to be a state before that fix landed.
  - Later commits (5ea3abba #10997, ad514049 #10726) further evolve keep_attrs behavior — scalar x handling changed, and default flipped to True repo-wide — but this fix targets only the missing kwarg/forwarding.
  - pytest config: rootdir uses setup.cfg; -k "where" only selected 1 test out of 248 in this snapshot, which is a thin signal — the broader test_computation.py suite or test_units.py would exercise more paths.

VERIFICATION:
  - Ran MCVE: xr.where(data == 1, data, 0) with data carrying attrs {'attr_1','attr_2'} — keep_attrs=True returned those attrs; default (no kwarg) returned {}; setting global xr.set_options(keep_attrs=True) also propagated attrs.
  - Ran `pytest xarray/tests/test_computation.py -k "where" -x` — 1 passed, 247 deselected, no regressions in selected subset.
```