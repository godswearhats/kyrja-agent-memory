#!/usr/bin/env bash
# Overnight sweep runner — sequential sizes, concurrency 1, resume-safe.
# Logs to sweep_overnight.log. Restartable: --resume skips finished scenarios.
set -euo pipefail

ROOT="masq/generator/sweep"
HARNESS="masq/harness/sweep_run.py"
LOG="masq/harness/sweep_overnight.log"

echo "=== Overnight sweep started $(date) ===" | tee -a "$LOG"

for SIZE in 25k 60k 150k 400k; do
    echo "" | tee -a "$LOG"
    echo ">>> Starting $SIZE at $(date)" | tee -a "$LOG"
    python3 "$HARNESS" "$ROOT" \
        --sizes "$SIZE" \
        --concurrency 1 \
        --resume \
        2>&1 | tee -a "$LOG"
    echo ">>> Finished $SIZE at $(date)" | tee -a "$LOG"
    # Brief pause between sizes to avoid burst
    sleep 10
done

echo "" | tee -a "$LOG"
echo "=== Overnight sweep complete $(date) ===" | tee -a "$LOG"
