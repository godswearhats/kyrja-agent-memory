#!/bin/bash
# Exp 2 sweep: cold, A, C × 4 runs each on Task 3 (where_keep_attrs_coord).
# Agent and distiller both Opus 4.6.
set -e
cd "$(dirname "$0")/.."

# Cold first (cheapest signal — confirms task baseline before encodings matter).
for run in 1 2 3 4; do
    echo ">>> cold run $run"
    python3 harness/run_variant.py cold --run $run
done

for variant in A C; do
    for run in 1 2 3 4; do
        echo ">>> $variant run $run"
        python3 harness/run_variant.py $variant --run $run
    done
done

echo
echo "Exp 2 sweep complete."
