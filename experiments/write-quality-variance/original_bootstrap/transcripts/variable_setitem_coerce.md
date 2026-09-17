**Tool [Read]:** `variable.py` (lines 165-185)

**Tool result:** 165	
166	
167	def _maybe_wrap_data(data):
168	    """
169	    Put pandas.Index and numpy.ndarray arguments in adapter objects to ensure
170	    they can be indexed properly.
171	
172	    NumpyArrayAdapter, PandasIndexAdapter and LazilyOuterIndexedArr
  [...truncated...]
  
182	    datetime64 and timedelta64, according to the pandas convention. Also used for
183	    validating that datetime64 and timedelta64 objects are within the valid date
184	    range for ns precision, as pandas will raise an error if they are not.

**Tool [Grep]:** pattern=`hasattr.*values|\.values` in `variable.py`

**Tool result:** 363:            return self.values
573:            item["data"] = ensure_us_time_resolution(self.values).tolist()
797:        array `x.values` directly.
1462:            shape = dims.values()
1556:        new_dim_sizes = tuple(dims.values())
2309:   
  [...truncated...]
  lues():
2527:    @Variable.values.setter  # type: ignore
2530:            f"Cannot assign to the .values attribute of dimension coordinate a.k.a IndexVariable {self.name!r}. "
2827:    duplicate_names = [v for v in level_names.values() if len(v) > 1]

**Tool [Grep]:** pattern=`as_compatible_data` in `variable.py`

**Tool result:** 139:        data = as_compatible_data(obj)
189:def as_compatible_data(data, fastpath=False):
330:        self._data = as_compatible_data(data, fastpath=fastpath)
367:        data = as_compatible_data(data)
468:            self._data = as_compatible_data(self._data.compute(**kwargs))
858:            value = as_compatible_data(value)
972:            data = as_compatible_data(data)
2625:            data = as_compatible_data(data)

**Tool [Read]:** `variable.py` (lines 189-249)

**Tool result:** 189	def as_compatible_data(data, fastpath=False):
190	    """Prepare and wrap data to put in a Variable.
191	
192	    - If data does not have the necessary attributes, convert it to ndarray.
193	    - If data has dtype=datetime64, ensure that it has 
  [...truncated...]
   'variable "NUMPY_EXPERIMENTAL_ARRAY_FUNCTION" is set to '
242	                    '"1"'
243	                )
244	
245	    # validate whether the data is valid data types.
246	    data = np.asarray(data)
247	
248	    if isinstance(data, np.ndarray):

**Tool [Edit]:** `variable.py`
  ```
  -     # we don't want nested self-described arrays
    data = getattr(data, "values", data)
  +     # we don't want nested self-described arrays
    if isinstance(data, (pd.Series, pd.Index, pd.DataFrame)):
        data = data.values
  ```

**Tool result:** The file variable.py has been updated successfully. (file state is current in your context — no need to Read it back)

**Agent:** Let me verify the fix works with the minimal example:

**Tool [Bash]:** `python -c "
import xarray as xr
import numpy as np

good_indexed, bad_indexed = xr.DataArray([None]), xr.DataArray([None])

class HasValues(object):
    values = 5
    
good_indexed.loc[{'dim_0': 0}] = set()
bad_indexed.loc[{'dim_0': 0}] = HasValues()

print('good:', good_indexed.values)
print('bad:`

**Tool result:** Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import xarray as xr
  File "__init__.py", line 1, in <module>
    import pkg_resources
ModuleNotFoundError: No module named 'pkg_resources'

**Tool [Bash]:** `pip install setuptools 2>&1 | tail -3`

**Tool result:** note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

**Tool [Bash]:** `ls bootstrap_variable_setitem_coerce | head; which python; python --version`

**Tool result:** CODE_OF_CONDUCT.md
CONTRIBUTING.md
HOW_TO_RELEASE.md
LICENSE
README.rst
asv_bench
ci
conftest.py
doc
licenses
/usr/bin/python
Python 3.14.4

**Tool [Bash]:** `ls .venv 2>/dev/null; find / -name "xarray*" -path "*site-packages*" 2>/dev/null | head -5`

**Tool result:** (Bash completed with no output)

**Tool [Bash]:** `ls /usr/bin/python* /opt/*/bin/python* 2>/dev/null; find / -name "pytest" -type f 2>/dev/null | head -5`

**Tool result:** /usr/bin/python
/usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/python-config
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/usr/share/bash-completion/completions/pytest
pytest
pytest
pytest
pytest

**Tool [Bash]:** `python -c "import sys; sys.path.insert(0, 'bootstrap_variable_setitem_coerce'); import xarray; print(xarray.__file__)"`

**Tool result:** __init__.py

**Tool [Bash]:** `python -c "
import sys
sys.path.insert(0, '.')
import xarray as xr
import numpy as np

good_indexed, bad_indexed = xr.DataArray([None]), xr.DataArray([None])

class HasValues(object):
    values = 5
    
good_indexed.loc[{'dim_0': 0}] = `

**Tool result:** Exit code 1
Traceback (most recent call last):
  File "indexing.py", line 1307, in __setitem__
    array[key] = value
    ~~~~~^^^^^
ValueErr
  [...truncated...]
  rkspace/kyrja/research/experiments/phase2-utility/worktrees/bootstrap_variable_setitem_coerce/xarray/core/indexing.py", line 1311, in __setitem__
    raise ValueError(
ValueError: Assignment destination is a view.  Do you want to .copy() array first?

**Tool [Bash]:** `python -c "
import numpy as np
import xarray as xr

class HasValues(object):
    values = 5

# Test Variable directly - easier to isolate from locked indexing behaviors
v = xr.Variable(dims=['x'], data=np.array([None, None], dtype=object`

**Tool result:** Exit code 1
Traceback (most recent call last):
  File "indexing.py", line 1307, in __setitem__
    array[key] = value
    ~~~~~^^^^^
ValueErr
  [...truncated...]
  rkspace/kyrja/research/experiments/phase2-utility/worktrees/bootstrap_variable_setitem_coerce/xarray/core/indexing.py", line 1311, in __setitem__
    raise ValueError(
ValueError: Assignment destination is a view.  Do you want to .copy() array first?

**Tool [Bash]:** `python -c "
import numpy as np
import pandas as pd
from xarray.core.variable import as_compatible_data

class HasValues(object):
    values = 5

# Before fix: would return np.asarray(5) = array(5)
# After fix: should wrap HasValues as-is`

**Tool result:** result: <__main__.HasValues object at 0x7f37ae9304a0> dtype: object
PASS HasValues
series result: [1 2 3] type: ndarray
PASS Series
index result: PandasIndexAdapter(array=Index([1, 2, 3], dtype='int64'), dtype=dtype('int64')) type: PandasIndexAdapter
PASS Index
df result: [[1 3]
 [2 4]] type: ndarray
PASS DataFrame

**Agent:** The fix works correctly. Now let me run the test suite for variable to make sure I haven't broken anything:

**Tool [Bash]:** `python -m pytest xarray/tests/test_variable.py -x -q 2>&1 | tail -30`

**Tool result:** =============================== warnings summary ===============================
xarray/__init__.py:1
  __init__.py:1: DeprecationWarning: pkg_res
  [...truncated...]
   test summary info ============================
FAILED xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime - ...
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 11 passed, 9 warnings in 0.74s

**Tool [Bash]:** `python -m pytest xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime -x 2>&1 | tail -30`

**Tool result:** =============================== warnings summary ===============================
xarray/__init__.py:1
  __init__.py:1: DeprecationWarning: pkg_res
  [...truncated...]
  =======
FAILED xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime - ...
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
======================== 1 failed, 9 warnings in 0.60s =========================

**Tool [Bash]:** `python -m pytest xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime -x --tb=long 2>&1 | grep -A 40 "FAILED\|test_index_0d_datetime\|Error\|assert"`

**Tool result:** _____________________ TestVariable.test_index_0d_datetime ______________________

self = <xarray.tests.test_variable.TestVariable object at 0x7f968d51a5d0>

    def test_index_0d_datetime(self):
        d = datetime(2000, 1, 1)
        x = self.cls([
  [...truncated...]
  =======
FAILED xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime - ...
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
======================== 1 failed, 9 warnings in 0.59s =========================

**Tool [Bash]:** `git stash && python -m pytest xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime -x --tb=line 2>&1 | tail -5; git stash pop`

**Tool result:** Saved working directory and index state WIP on (no branch): 7c4e2ac8 Revert defaults of beckends' open_datasets to prepare the switch to APIv2 #4309 (#4899)
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=====================
  [...truncated...]
  mmitted)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   xarray/core/variable.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (e7872e20c3810947ff6cd57dcbd6da94f0ee26f0)

**Agent:** Pre-existing failure unrelated to the fix. Let me run the remaining tests skipping known environment failures:

**Tool [Bash]:** `python -m pytest xarray/tests/test_variable.py --deselect xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime -q --no-header 2>&1 | tail -15`

**Tool result:** FAILED xarray/tests/test_variable.py::TestVariable::test_timedelta64_conversion_scalar
FAILED xarray/tests/test_variable.py::TestVariable::test_0d_timedelta - Asser...
FAILED xarray/tests/test_variable.py::TestVariableWithDask::test_index_0d_datetime
  [...truncated...]
  D xarray/tests/test_variable.py::TestAsCompatibleData::test_unchanged_types
FAILED xarray/tests/test_variable.py::TestAsCompatibleData::test_datetime - A...
19 failed, 342 passed, 3 skipped, 1 deselected, 70 xfailed, 23 xpassed, 117 warnings in 7.37s

**Tool [Bash]:** `git stash && python -m pytest xarray/tests/test_variable.py --deselect xarray/tests/test_variable.py::TestVariable::test_index_0d_datetime -q --no-header 2>&1 | tail -5; git stash pop`

**Tool result:** Saved working directory and index state WIP on (no branch): 7c4e2ac8 Revert defaults of beckends' open_datasets to prepare the switch to APIv2 #4309 (#4899)
FAILED xarray/tests/test_variable.py::TestIndexVariable::test_timedelta64_conversion
FAILED x
  [...truncated...]
  mmitted)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   xarray/core/variable.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (dbd97f4017252bbfb66eb6d251f873d6a0186ca7)

**Agent:** Same 19 failures with or without the fix — all are pre-existing environment issues (numpy datetime precision). The fix is complete:

**Change made** at `xarray/core/variable.py:221`:
```python
# Before:
data = getattr(data, "values", data)

# After:
if isinstance(data, (pd.Series, pd.Index, pd.DataFrame)):
    data = data.values
```

This replaces duck-typing on the `values` attribute with explicit type checking, so arbitrary objects with a `.values` attribute (like `lmfit.ModelResult` or the `HasValues` example) are no longer incorrectly coerced when stored in object-dtype arrays. Verified the fix works via direct `as_compatible_data` testing.

**Final result:** Same 19 failures with or without the fix — all are pre-existing environment issues (numpy datetime precision). The fix is complete:

**Change made** at `xarray/core/variable.py:221`:
```python
# Before:
data = getattr(data, "values", data)

# After:
if isinstance(data, (pd.Series, pd.Index, pd.DataFrame)):
    data = data.values
```

This replaces duck-typing on the `values` attribute with explicit type checking, so arbitrary objects with a `.values` attribute (like `lmfit.ModelResult` or the `HasValues` example) are no longer incorrectly coerced when stored in object-dtype arrays. Verified the fix works via direct `as_compatible_data` testing.

**Usage:** input=25, output=5586, cost=$0.5973, turns=21