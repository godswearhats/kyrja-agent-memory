#!/usr/bin/env python3
"""Run a single trial of variant <X> on where_keep_attrs_scalar.

Adapted from Phase 2 run_trial.py. Differences:
  - Conditions are named A, B, C, D (or 'cold' as baseline reproduction).
  - Memory context is loaded from encodings/{variant}_encoding.md.
  - Trials write to data/trial_logs/ with trial_id encoding the variant.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

EXP_DIR = Path(__file__).parent.parent
REPO_DIR = EXP_DIR / "repo"
ENCODINGS_DIR = EXP_DIR / "encodings"
WORKTREES_DIR = EXP_DIR / "worktrees"
DATA_DIR = EXP_DIR / "data"
TRIAL_LOGS_DIR = DATA_DIR / "trial_logs"
ORIG_PROMPTS_DIR = EXP_DIR / "original_prompts"
PILOT_TASKS = EXP_DIR / "pilot_tasks.json"
CLAUDE_BIN = "/opt/claude"
VENV_PYTHON = EXP_DIR / "venv" / "bin" / "python"

TASK_LABEL = "where_keep_attrs_scalar"
TASK_PROMPT_FILE = ORIG_PROMPTS_DIR / "task_02_where_keep_attrs_scalar.md"


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
    return f"<memory>\n## Prior session: pydata__xarray-4687 (xr.where keep_attrs)\n\n{memory}\n</memory>\n\n{task_prompt}"


def run_agent(prompt, worktree_path, model="opus", timeout=600):
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


def evaluate_patch(worktree_path, task_data):
    test_patch = task_data["test_patch"]
    fail_to_pass = task_data.get("fail_to_pass", [])
    if not fail_to_pass:
        return {"success": None, "reason": "no FAIL_TO_PASS tests defined"}

    test_patch_file = worktree_path / "_test_patch.diff"
    test_patch_file.write_text(test_patch)
    apply_result = subprocess.run(
        ["git", "apply", "--allow-empty", str(test_patch_file)],
        cwd=worktree_path, capture_output=True, text=True,
    )
    test_patch_file.unlink()

    if apply_result.returncode != 0:
        return {"success": None, "reason": f"test patch failed to apply: {apply_result.stderr[:500]}"}

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


def run_trial(variant, run_number, model="opus", timeout=600, dry_run=False):
    task_data = load_task()
    trial_id = f"{TASK_LABEL}__variant_{variant}__run{run_number}"

    task_prompt = TASK_PROMPT_FILE.read_text()
    prompt = build_prompt(task_prompt, variant)

    print(f"\n{'='*70}")
    print(f"Trial: {trial_id}")
    print(f"  Variant: {variant}")
    print(f"  Run: {run_number}")
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
    parser.add_argument("variant", help="Variant letter (A, B, C, D) or 'cold'")
    parser.add_argument("--run", type=int, default=1, help="Run number")
    parser.add_argument("--model", default="claude-opus-4-6")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_trial(args.variant, args.run, model=args.model,
              timeout=args.timeout, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
