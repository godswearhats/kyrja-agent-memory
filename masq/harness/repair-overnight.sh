#!/bin/bash
# Overnight repair of the cap-contaminated Supermemory store (2026-07-24).
# Self-checks the stack, then runs the batched cap-safe repair; on
# verification PASS, re-runs the MASQ reader for the supermemory arm only.
# Pre-registration: REPAIR-PREREG.md (written before this runs).
set -u
cd "$(dirname "$0")"
SCEN=../generator/headline/rate-limit/s4001/60k
LOG=repair-overnight.log

echo "=== repair-overnight start $(date -Is) ===" >> "$LOG"

# supermemory-server up?
if ! curl -s -m 5 -o /dev/null http://localhost:6767/v1/models 2>/dev/null; then
  echo "starting supermemory-server" >> "$LOG"
  env $(cat ~/.supermemory/env | xargs) nohup supermemory-server \
      >> /tmp/smem-server.log 2>&1 &
  sleep 15
fi
# claude-p proxy up?
if ! curl -s -m 5 http://localhost:8787/v1/models >/dev/null 2>&1; then
  echo "starting claude-p proxy" >> "$LOG"
  nohup python3 smem_claude_proxy.py 8787 >> /tmp/smem-proxy.log 2>&1 &
  sleep 3
fi

python3 audit_repair.py "$SCEN" --reader >> "$LOG" 2>&1
rc=$?
echo "=== repair-overnight done $(date -Is) rc=$rc ===" >> "$LOG"
