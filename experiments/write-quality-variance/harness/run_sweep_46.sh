#!/bin/bash
# Full diagnostic sweep under Opus 4.6.
# Includes reproduction controls: A_orig (Phase 2 original encoding), cold (no memory).
set -e
cd "$(dirname "$0")/.."

# Diagnostic controls first (cheapest to inspect if something is wrong)
for variant in A_orig cold; do
    for run in 1 2 3 4; do
        echo ">>> $variant run $run"
        python3 harness/run_variant.py $variant --run $run
    done
done

# Main variants
for variant in A B C D; do
    for run in 1 2 3 4; do
        echo ">>> $variant run $run"
        python3 harness/run_variant.py $variant --run $run
    done
done

echo
echo "Sweep complete."
