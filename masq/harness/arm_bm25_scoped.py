"""Scope-aware lexical arm — `arm_bm25` with the discriminator un-diluted.

Differs from `arm_bm25` in exactly two places, both deployable (no ground-truth
field is read anywhere in this module):

1. **Tokenization.** `arm_bm25` uses `[a-z0-9]+`, the Lucene default, which splits
   `checkout-web` into `checkout` + `web`. Every sibling scope in a MASQ family
   shares the `checkout` prefix, so that token carries ~0 IDF while the shared
   split makes all siblings match the query equally. Keeping hyphenated compounds
   whole (`[a-z0-9][a-z0-9-]*`) makes `checkout-web` itself the high-IDF term.

2. **Query formulation.** `arm_bm25` retrieves with the whole ~63-word task prompt,
   in which the one discriminating token competes with boilerplate ("supersession",
   "collision", "reconstruct", "history") that every sibling chain matches. This arm
   retrieves with the scope phrase alone, parsed out of the query text the benchmark
   already hands every arm.

`k` is unchanged at 10, so this isolates tokenization + query against `bm25_k10`.
Note the arm still returns 10 sessions: roughly 3 target-chain sessions and ~6
unscoped chatter sessions. It is therefore *not* equivalent to `arm_scopefilter`,
which returns the target chain alone — the extra chatter is the cost of ranking.

Pre-registration: PREREG-scoped-bm25.md (H47).
"""
import re

from arm_bm25 import _bm25_scores, _sessions
from arm_vector import _format

_TOK = re.compile(r"[a-z0-9][a-z0-9-]*")
_SCOPE_PREFIX = re.compile(r"In the context of ([^:]+):")


def _tokenize(text):
    return _TOK.findall(text.lower())


def _scope_query(family):
    """Recover the scope phrase from the query the benchmark supplies.

    Falls back to the full query if the preamble is ever absent, so the arm
    degrades to `bm25_k10`-with-compound-tokens rather than failing.
    """
    q = family["a_query"]
    m = _SCOPE_PREFIX.match(q)
    return m.group(1).strip() if m else q


def make_bm25_scoped_arm(k=10):
    def arm(family, _corpus_dir):
        sess = _sessions(family)
        if not sess:
            return "[No memories retrieved]"
        doc_tokens = [_tokenize(t) for _, t in sess]
        q_tokens = _tokenize(_scope_query(family))
        scores = _bm25_scores(doc_tokens, q_tokens)
        k_eff = min(k, len(sess))
        order = sorted(range(len(sess)), key=lambda i: scores[i], reverse=True)[:k_eff]
        return _format([sess[i][0] for i in order])

    return arm
