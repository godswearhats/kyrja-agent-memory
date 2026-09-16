#!/bin/bash
# Sequential sweep: variants A, B, C, D × runs 2, 3, 4 (run 1 of A already done as smoke test).
# Run from experiment root: bash harness/run_sweep.sh
set -e
cd "$(dirname "$0")/.."

# Complete A (runs 2, 3, 4)
for run in 2 3 4; do
    echo ">>> A run $run"
    python3 harness/run_variant.py A --run $run
done

# B, C, D each for runs 1-4
for variant in B C D; do
    for run in 1 2 3 4; do
        echo ">>> $variant run $run"
        python3 harness/run_variant.py $variant --run $run
    done
done

echo
echo "Sweep complete."
