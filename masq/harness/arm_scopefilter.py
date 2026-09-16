"""Scope-filter retrieval arm for MASQ v2 — the `WHERE scope = target` arm.

The diagnostic on vector/bm25 showed both retrievers RECALL the target scope well
(~2.8 of 3 sessions) but cannot EXCLUDE the confusable siblings (~5.5 of 10 hits),
because the siblings are by construction as content-relevant to the query as the
target. Relevance ranking is `ORDER BY similarity LIMIT k`; this task actually
needs `WHERE scope = 'checkout-web'`. This arm does exactly that: it returns every
session tagged with the target scope and drops all siblings — an exact-match filter
on the scope column, no ranking.

Distinct from `ceiling`: ceiling also scope-filters, but additionally hands the
model each step's resolution TYPE label ([initial]/[self_revision]/[supersession])
— i.e. the conflict pre-classified. This arm returns the same target rows as RAW
prose in temporal order, no labels, so the reader must resolve the chain itself.

Formatting is identical to the vector/bm25 arms ("[Retrieved memories]" + the same
per-session layout), so the ONLY thing that differs from those retrieval arms is
WHICH sessions are selected (filter vs. top-k rank). Three-way contrast:
    vector/bm25  : target + siblings (rank)   -> floods context with look-alikes
    scope-filter : target only (filter)        -> isolates the exclusion effect
    ceiling      : target only + type labels   -> isolates the resolution-hint effect

The reader and grader are untouched; this arm differs only in the context string.
"""
from arm_vector import _format


def arm_scopefilter(family, _corpus_dir):
    target = family["meta"]["target_scope"]
    selected = [s for s in family["world_sessions"] if s.get("scope") == target]
    if not selected:
        return "[No memories retrieved]"
    return _format(selected)
