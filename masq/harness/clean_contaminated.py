#!/usr/bin/env python3
"""Delete contaminated result files so `sweep_run.py --resume` re-runs them.

A scenario's results file is contaminated when a reader subprocess received an
account-level error (session/usage limit, overload) *instead of* a completion —
the harness then records a_score=0 / PARSE_FAIL on what should be a clean call.
The unmistakable canary: the perfect-retrieval (ceiling) arm, which is HANDED
the correct chain, scoring near zero; and/or the raw reader text being an API
error notice rather than org-corpus prose.

Detection (a file is contaminated if EITHER):
  1. any arm's a_raw / b_raw contains a known API-error signature, or
  2. the ceiling arm scored a_score < 0.8 (perfect retrieval cannot fail this
     low on a real call).

NB: we deliberately do NOT match the bare phrase "rate limit" — "rate-limit" is
one of the benchmark domains and appears in legitimate corpus prose. We match
only phrases that never occur in generated text.

Usage:
    python3 clean_contaminated.py <root> [--apply] [--model claude-opus-4-8]
Without --apply it only reports (dry run).
"""
import argparse, glob, json, os, sys

# Signatures that only appear in account/infra error responses, never in the
# synthetic org corpus. Matched case-insensitively against a_raw + b_raw.
ERROR_SIGNATURES = [
    "hit your session limit",
    "session limit · resets",
    "usage limit",
    "hit your usage",
    "overloaded",
    "please try again later",
    "service is temporarily",
    "rate_limit_error",   # API error code form, not the domain name
    "anthropic api error",
]
CEILING_FLOOR = 0.8  # perfect-retrieval a_score below this = bad call


def is_contaminated(d):
    reasons = []
    for r in d.get("results", []):
        blob = (str(r.get("a_raw", "")) + " " + str(r.get("b_raw", ""))).lower()
        for sig in ERROR_SIGNATURES:
            if sig in blob:
                reasons.append(f"{r.get('arm_key')}:error-signature({sig!r})")
                break
        if r.get("arm_key") == "ceiling":
            asc = r.get("a_score")
            if asc is None or asc < CEILING_FLOOR:
                reasons.append(f"ceiling:a_score={asc}")
    return reasons


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--apply", action="store_true", help="actually delete (default: dry run)")
    ap.add_argument("--model", default="claude-opus-4-8")
    a = ap.parse_args()

    root = os.path.abspath(a.root)
    pat = os.path.join(root, "**", f"results-*{a.model}*.json")
    files = sorted(glob.glob(pat, recursive=True))

    contaminated = []
    for f in files:
        try:
            d = json.load(open(f))
        except Exception as e:
            contaminated.append((f, [f"unreadable:{e}"]))
            continue
        reasons = is_contaminated(d)
        if reasons:
            contaminated.append((f, reasons))

    print(f"scanned {len(files)} result files under {root}")
    print(f"contaminated: {len(contaminated)}  clean: {len(files)-len(contaminated)}")
    for f, reasons in contaminated:
        rel = f.replace(root + "/", "")
        print(f"  [{'DELETE' if a.apply else 'would delete'}] {rel}  <- {', '.join(reasons)}")
        if a.apply:
            os.remove(f)

    if not a.apply and contaminated:
        print("\n(dry run — re-run with --apply to delete, then sweep_run.py --resume)")
    return len(contaminated)


if __name__ == "__main__":
    sys.exit(0 if main() >= 0 else 1)
