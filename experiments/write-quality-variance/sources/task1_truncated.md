**Tool [Bash]:** `find experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add -type f -name "*.py" | head -20 && echo "---" && ls experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add`

**Tool result:** experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/.github/workflows/parse_logs.py
experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/asv_bench/benchmarks/__init__.
  [...truncated...]
  /plot_control_colorbar.py
---
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
HOW_TO_RELEASE.md
LICENSE
README.rst
asv_bench
ci
conftest.py
design_notes
doc
licenses
properties
pyproject.toml
readthedocs.yml
requirements.txt
setup.cfg
setup.py
xarray

**Tool [Grep]:** pattern=`^def where` in `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py`

**Tool result:** 1730:def where(cond, x, y):

**Tool [Read]:** `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py` (lines 1725-1805)

**Tool result:** 1725	        dask="allowed",
1726	    )
1727	    return result.transpose(*all_dims, missing_dims="ignore")
1728	
1729	
1730	def where(cond, x, y):
1731	    """Return elements from `x` or `y` depending on `cond`.
1732	
1733	    Performs xarray-like br
  [...truncated...]
  rue, False], dims=["x"])
1798	    >>> x = xr.DataArray([1, 2], dims=["y"])
1799	    >>> xr.where(cond, x, 0)
1800	    <xarray.DataArray (x: 2, y: 2)>
1801	    array([[1, 2],
1802	           [0, 0]])
1803	    Dimensions without coordinates: x, y
1804	

**Tool [Read]:** `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py` (lines 1804-1854)

**Tool result:** 1804	
1805	    See Also
1806	    --------
1807	    numpy.where : corresponding numpy function
1808	    Dataset.where, DataArray.where :
1809	        equivalent methods
1810	    """
1811	    # alignment for three arguments is complicated, so don't sup
  [...truncated...]
  848	        np.vander(x, int(deg_coord.max()) + 1),
1849	        dims=(coord.name, degree_dim),
1850	        coords={coord.name: coord, degree_dim: np.arange(deg_coord.max() + 1)[::-1]},
1851	    )
1852	    return (lhs * coeffs).sum(degree_dim)
1853	

**Tool [Grep]:** pattern=`keep_attrs` in `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py`

**Tool result:** 32:from .options import OPTIONS, _get_keep_attrs
267:    keep_attrs="override",
281:    if keep_attrs == "drop":
287:        args, signature, exclude_dims, combine_attrs=keep_attrs
302:    attrs = merge_attrs([x.attrs for x in objs], combine_attrs=ke
  [...truncated...]
  eep_attrs,
1145:            keep_attrs=keep_attrs,
1162:            keep_attrs=keep_attrs,
1172:            keep_attrs=keep_attrs,
1862:    keep_attrs: bool = None,
1892:    indx = func(array, dim=dim, axis=None, keep_attrs=keep_attrs, skipna=skipna)

**Tool [Read]:** `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py` (lines 1110-1140)

**Tool result:** 1110	            )
1111	            dask_gufunc_kwargs.setdefault("output_sizes", output_sizes)
1112	
1113	    if kwargs:
1114	        func = functools.partial(func, **kwargs)
1115	
1116	    if keep_attrs is None:
1117	        keep_attrs = _get_keep_
  [...truncated...]
   groupby-apply_ufunc through apply_groupby_func
1135	    if any(isinstance(a, GroupBy) for a in args):
1136	        this_apply = functools.partial(
1137	            apply_ufunc,
1138	            func,
1139	            input_core_dims=input_core_dims,

**Tool [Grep]:** pattern=`combine_attrs=keep_attrs` in `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py`

**Tool result:** 287:        args, signature, exclude_dims, combine_attrs=keep_attrs
302:    attrs = merge_attrs([x.attrs for x in objs], combine_attrs=keep_attrs)
444:        args, signature, exclude_dims, combine_attrs=keep_attrs
458:    attrs = merge_attrs([x.attrs for x in objs], combine_attrs=keep_attrs)
752:        combine_attrs=keep_attrs,

**Tool [Read]:** `experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py` (lines 280-310)

**Tool result:** 280	
281	    if keep_attrs == "drop":
282	        name = result_name(args)
283	    else:
284	        first_obj = _first_of_type(args, DataArray)
285	        name = first_obj.name
286	    result_coords = build_output_coords(
287	        args, signatur
  [...truncated...]
  ue)
301	
302	    attrs = merge_attrs([x.attrs for x in objs], combine_attrs=keep_attrs)
303	    if isinstance(out, tuple):
304	        for da in out:
305	            da.attrs = attrs
306	    else:
307	        out.attrs = attrs
308	
309	    return out
