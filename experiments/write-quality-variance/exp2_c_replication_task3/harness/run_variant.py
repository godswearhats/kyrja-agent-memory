#!/usr/bin/env python3
"""Run a single trial of variant <X> on where_keep_attrs_coord (Task 3).

Exp 2 — C-Replication on Task 3.
Differences from parent run_variant.py:
  - Downstream task = where_keep_attrs_coord (Task 3, pydata__xarray-7229).
  - Encodings loaded from exp2_c_replication_task3/encodings/ (4.6-distilled).
  - Memory header references Task 2 (where_keep_attrs_scalar) as the prior session.
  - Trial logs written to exp2 data dir.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

EXP_DIR = Path(__file__).parent.parent
PARENT_EXP_DIR = EXP_DIR.parent
REPO_DIR = PARENT_EXP_DIR / "repo"
WORKTREES_DIR = PARENT_EXP_DIR / "worktrees"
ENCODINGS_DIR = EXP_DIR / "encodings"
DATA_DIR = EXP_DIR / "data"
TRIAL_LOGS_DIR = DATA_DIR / "trial_logs"
ORIG_PROMPTS_DIR = PARENT_EXP_DIR / "original_prompts"
PILOT_TASKS = PARENT_EXP_DIR / "pilot_tasks.json"
CLAUDE_BIN = "/opt/claude"
VENV_PYTHON = PARENT_EXP_DIR / "venv" / "bin" / "python"

TASK_LABEL = "where_keep_attrs_coord"
TASK_PROMPT_FILE = ORIG_PROMPTS_DIR / "task_03_where_keep_attrs_coord.md"
MEMORY_HEADER = "## Prior session: pydata__xarray-6461 (xr.where scalar/lambda fix)"


def load_task():
    with open(PILOT_TASKS) as f:
        return json.load(f)[TASK_LABEL]


def create_worktree(task_data, trial_id):
    worktree_path = WORKTREES_DIR / trial_id
    if worktree_path.exists():
        subprocess.run(
            ["git", "worktree", "remove", "--force", str(worktree_path)],
            cwd=REPO_DIR, capture_output=True,
        )
    subprocess.run(
        ["git", "worktree", "add", "--detach", str(worktree_path), task_data["base_commit"]],
        cwd=REPO_DIR, capture_output=True, check=True,
    )
    return worktree_path


def remove_worktree(worktree_path):
    subprocess.run(
        ["git", "worktree", "remove", "--force", str(worktree_path)],
        cwd=REPO_DIR, capture_output=True,
    )


def build_prompt(task_prompt, variant):
    if variant == "cold":
        return task_prompt
    encoding_path = ENCODINGS_DIR / f"{variant}_encoding.md"
    if not encoding_path.exists():
        raise FileNotFoundError(f"Encoding not found: {encoding_path}")
    memory = encoding_path.read_text()
    return f"<memory>\n{MEMORY_HEADER}\n\n{memory}\n</memory>\n\n{task_prompt}"


def run_agent(prompt, worktree_path, model="claude-opus-4-6", timeout=600):
    result = subprocess.run(
        [
            CLAUDE_BIN,
            "--setting-sources", "",
            "--model", model,
            "-p", prompt,
            "--output-format", "json",
            "--no-session-persistence",
            "--disable-slash-commands",
            "--dangerously-skip-permissions",
            "--allow-dangerously-skip-permissions",
        ],
        cwd=worktree_path,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0 and not result.stdout.strip():
        return {"error": result.stderr, "returncode": result.returncode}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "JSON parse failed", "stdout": result.stdout[:2000], "stderr": result.stderr[:1000]}


def _files_in_patch(patch_text):
    """Extract the set of files a unified diff modifies (b/<path> entries)."""
    files = set()
    for line in patch_text.splitlines():
        if line.startswith("+++ b/"):
            files.add(line[len("+++ b/"):].strip())
        elif line.startswith("diff --git a/") and " b/" in line:
            b_part = line.split(" b/", 1)[1].strip()
            files.add(b_part)
    files.discard("/dev/null")
    return sorted(files)


def evaluate_patch(worktree_path, task_data):
    test_patch = task_data["test_patch"]
    fail_to_pass = task_data.get("fail_to_pass", [])
    if not fail_to_pass:
        return {"success": None, "reason": "no FAIL_TO_PASS tests defined"}

    # Reset any test files the agent may have touched back to base_commit
    # before applying the gold test_patch. We trust the gold tests, not
    # whatever the agent decided to write.
    test_files = _files_in_patch(test_patch)
    reset_log = []
    for tf in test_files:
        r = subprocess.run(
            ["git", "checkout", "HEAD", "--", tf],
            cwd=worktree_path, capture_output=True, text=True,
        )
        reset_log.append({"file": tf, "rc": r.returncode, "stderr": r.stderr[:200]})

    test_patch_file = worktree_path / "_test_patch.diff"
    test_patch_file.write_text(test_patch)
    apply_result = subprocess.run(
        ["git", "apply", "--allow-empty", str(test_patch_file)],
        cwd=worktree_path, capture_output=True, text=True,
    )
    test_patch_file.unlink()

    if apply_result.returncode != 0:
        return {
            "success": None,
            "reason": f"test patch failed to apply after test-file reset: {apply_result.stderr[:500]}",
            "reset_log": reset_log,
        }

    env = os.environ.copy()
    env["PYTHONPATH"] = str(worktree_path)
    test_result = subprocess.run(
        [str(VENV_PYTHON), "-m", "pytest", "-xvs", "--rootdir", str(worktree_path)] + fail_to_pass,
        cwd=worktree_path, env=env,
        capture_output=True, text=True, timeout=120,
    )
    return {
        "success": test_result.returncode == 0,
        "total": len(fail_to_pass),
        "test_ids": fail_to_pass,
        "returncode": test_result.returncode,
        "stdout_tail": test_result.stdout[-500:] if test_result.returncode != 0 else "",
        "stderr_tail": test_result.stderr[-500:] if test_result.returncode != 0 else "",
    }


def run_trial(variant, run_number, model="claude-opus-4-6", timeout=600, dry_run=False):
    task_data = load_task()
    trial_id = f"{TASK_LABEL}__variant_{variant}__run{run_number}"

    task_prompt = TASK_PROMPT_FILE.read_text()
    prompt = build_prompt(task_prompt, variant)

    print(f"\n{'='*70}")
    print(f"Trial: {trial_id}")
    print(f"  Variant: {variant}")
    print(f"  Run: {run_number}")
    print(f"  Model: {model}")
    print(f"  Prompt: {len(prompt)} chars")
    print(f"{'='*70}")

    if dry_run:
        print(f"[DRY RUN] Would invoke agent with {len(prompt)}-char prompt")
        return None

    worktree_path = create_worktree(task_data, trial_id)
    try:
        start_time = time.time()
        agent_result = run_agent(prompt, worktree_path, model=model, timeout=timeout)
        wall_time = time.time() - start_time

        if "error" in agent_result:
            print(f"  AGENT ERROR: {agent_result['error'][:200]}")
            eval_result = {"success": False, "reason": "agent_error"}
        else:
            print(f"  Agent: {agent_result.get('duration_ms', 0)/1000:.1f}s, {agent_result.get('num_turns', 0)} turns")
            eval_result = evaluate_patch(worktree_path, task_data)
            print(f"  Eval: {'PASS' if eval_result.get('success') else 'FAIL'}")

        usage = agent_result.get("usage", {})
        trial_result = {
            "trial_id": trial_id,
            "task_label": TASK_LABEL,
            "instance_id": task_data["instance_id"],
            "variant": variant,
            "run_number": run_number,
            "model": model,
            "prompt_length_chars": len(prompt),
            "agent": {
                "result_text": agent_result.get("result", "")[:2000],
                "num_turns": agent_result.get("num_turns", 0),
                "duration_ms": agent_result.get("duration_ms", 0),
                "total_cost_usd": agent_result.get("total_cost_usd", 0),
                "stop_reason": agent_result.get("stop_reason", ""),
                "input_tokens": usage.get("input_tokens", 0),
                "output_tokens": usage.get("output_tokens", 0),
                "cache_read_tokens": usage.get("cache_read_input_tokens", 0),
                "cache_creation_tokens": usage.get("cache_creation_input_tokens", 0),
            },
            "evaluation": eval_result,
            "wall_time_seconds": wall_time,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        log_path = TRIAL_LOGS_DIR / f"{trial_id}.json"
        log_path.write_text(json.dumps(trial_result, indent=2))
        print(f"  Cost: ${agent_result.get('total_cost_usd', 0):.4f}  Out tokens: {usage.get('output_tokens', 0)}  Wall: {wall_time:.1f}s")
        print(f"  Saved: {log_path}")

        append_to_trials(trial_result)
        return trial_result
    finally:
        remove_worktree(worktree_path)


def append_to_trials(trial_result):
    trials_path = DATA_DIR / "trials.json"
    if trials_path.exists():
        with open(trials_path) as f:
            trials = json.load(f)
    else:
        trials = []
    trials.append(trial_result)
    with open(trials_path, "w") as f:
        json.dump(trials, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("variant", help="Variant letter (A, C) or 'cold'")
    parser.add_argument("--run", type=int, default=1, help="Run number")
    parser.add_argument("--model", default="claude-opus-4-6")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_trial(args.variant, args.run, model=args.model,
              timeout=args.timeout, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
