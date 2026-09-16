#!/usr/bin/env python3
"""OpenAI-compatible chat-completions proxy backed by `claude -p`.

Lets supermemory-server's memory-extraction agent run on the Claude Code
subscription instead of the metered API: point OPENAI_BASE_URL at this proxy
and every /v1/chat/completions request is serviced by a `claude -p` call with
the SAME model and the SAME prompts. What changes is transport only — with one
honest exception: tool calling is prompt-encoded (schemas embedded in the
prompt, JSON parsed from the reply) instead of API-native. Shim fidelity is
validated against the 323 API-extracted documents before results are trusted.

Every call is logged to proxy-log.jsonl (prompt size, tool count, duration,
usage as reported by `claude -p --output-format json`) — this doubles as the
cost/cap diagnosis for the 35c-per-document mystery.

Usage:  python3 smem_claude_proxy.py [port]        # default 8787
Env for supermemory:  OPENAI_BASE_URL=http://localhost:8787/v1
                      OPENAI_API_KEY=subscription   OPENAI_MODEL=claude-opus-4-8
"""
import collections, json, os, subprocess, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proxy-log.jsonl")
_log_lock = threading.Lock()

# Throttle: at most RATE_PER_HOUR claude invocations per rolling hour, so an
# overnight ingest stays under the subscription session-window budget by
# pacing rather than by luck (repair calibration 2026-07-24: ~880 calls
# exhausted one window; 150/h * 5h = 750 stays under).
RATE_PER_HOUR = int(os.environ.get("SMEM_PROXY_RATE_PER_HOUR", "150"))
# Uniform pacer, NOT a rolling-window bucket: a bucket lets the client burst
# the whole budget in minutes and then hit a 20+ min wall, during which held
# requests exceed the server's ~5-min client timeout and get connection-reset
# (measured overnight 2026-07-25: 111 resets, all at >=324s held). Spacing
# call *starts* uniformly (3600/RATE apart) bounds any request's hold to
# roughly (concurrent pending x spacing) ~= 1-2 min.
_next_slot = [0.0]
_slot_lock = threading.Lock()

# Cap resilience: `claude -p` exiting rc=1 during a subscription-cap window
# must NOT surface as an instant error — supermemory-server v0.0.3 marks the
# document done-with-zero-memories on LLM failure (the 2026-07-22 silent
# contamination). Retry with backoff, holding the HTTP request open; total
# hold stays under a typical OpenAI-client timeout (10 min).
CAP_BACKOFFS_S = (60, 120, 240)

# The cap has TWO presentations (both observed): rc=1 (2026-07-22 outage) and
# rc=0 with the cap message as the result text (2026-06-26 reader
# contamination). Signatures here must be phrases that can ONLY come from the
# cap UI, never from extraction output that quotes corpus prose — the MASQ
# corpus is about rate limiting, so generic ops vocabulary ("overloaded",
# "usage limit") false-positives (2026-07-25: s0401's prose contains
# "overloaded"; the borrowed reader-cleaning list perma-failed that doc).
CAP_SIGNATURES = ("hit your session limit", "hit your usage",
                  "session limit · resets", "usage limit · resets",
                  "anthropic api error")


def _is_cap_text(text):
    if not text or len(text) > 400:
        return False
    low = text.lower()
    return any(sig in low for sig in CAP_SIGNATURES)


def _throttle():
    """Block until this call's uniform slot arrives; return seconds waited."""
    spacing = 3600.0 / RATE_PER_HOUR
    with _slot_lock:
        now = time.monotonic()
        slot = max(now, _next_slot[0])
        _next_slot[0] = slot + spacing
    wait = slot - now
    if wait > 0:
        time.sleep(wait)
    return wait

TOOL_INSTR = """\

# Tool calling
You have access to the following tools, defined as JSON schemas:

{schemas}

To call one or more tools, reply with ONLY a JSON object (no prose, no code \
fence) of the form:
{{"tool_calls": [{{"name": "<tool name>", "arguments": {{...}}}}]}}
If no tool call is needed, reply with your normal answer as plain text."""


def _render_transcript(messages):
    """Non-system messages -> a plain conversation transcript."""
    parts = []
    for m in messages:
        role = m.get("role")
        content = m.get("content")
        if isinstance(content, list):  # content-part arrays -> text
            content = "\n".join(p.get("text", "") for p in content
                                if isinstance(p, dict))
        if role == "system":
            continue
        if role == "tool":
            parts.append(f"[tool result for call {m.get('tool_call_id','?')}]\n"
                         f"{content}")
        elif role == "assistant" and m.get("tool_calls"):
            calls = [{"name": c["function"]["name"],
                      "arguments": json.loads(c["function"]["arguments"])
                      if isinstance(c["function"].get("arguments"), str)
                      else c["function"].get("arguments", {})}
                     for c in m["tool_calls"]]
            parts.append("[assistant tool calls]\n"
                         + json.dumps({"tool_calls": calls}))
        else:
            parts.append(f"[{role}]\n{content or ''}")
    return "\n\n".join(parts)


def _parse_tool_calls(text):
    """Find a {"tool_calls": [...]} object in the reply, tolerant of fences."""
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t.startswith("json"):
            t = t[4:]
        t = t.strip()
    start = t.find('{"tool_calls"')
    if start == -1:
        start = t.find('{ "tool_calls"')
    if start == -1:
        return None
    dec = json.JSONDecoder()
    try:
        obj, _ = dec.raw_decode(t[start:])
    except ValueError:
        return None
    calls = obj.get("tool_calls")
    if not isinstance(calls, list) or not calls:
        return None
    out = []
    for i, c in enumerate(calls):
        if not isinstance(c, dict) or "name" not in c:
            return None
        out.append({
            "id": f"call_{int(time.time()*1000)}_{i}",
            "type": "function",
            "function": {"name": c["name"],
                         "arguments": json.dumps(c.get("arguments", {}))},
        })
    return out


def _call_claude(model, system_prompt, prompt):
    throttle_s = _throttle()
    retries = 0
    for backoff in CAP_BACKOFFS_S + (None,):
        r = subprocess.run(
            ["claude", "-p", "--model", model, "--system-prompt", system_prompt,
             "--output-format", "json"],
            input=prompt, capture_output=True, text=True, timeout=600)
        if r.returncode == 0 and r.stdout.strip():
            out = json.loads(r.stdout)
            if not _is_cap_text(out.get("result", "")):
                return (out.get("result", ""), out.get("usage", {}),
                        {"throttle_s": round(throttle_s, 1),
                         "retries": retries})
        if backoff is None:
            break
        retries += 1
        with _log_lock, open(LOG, "a") as f:
            f.write(json.dumps({"ts": time.time(), "stalled": True,
                                "rc": r.returncode, "backoff_s": backoff,
                                "stderr": r.stderr[:200],
                                "stdout": r.stdout[:200]}) + "\n")
        time.sleep(backoff)
    raise RuntimeError(f"claude -p rc={r.returncode} after {retries} retries: "
                       f"{r.stderr[:200]} {r.stdout[:200]}")


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):  # quiet
        pass

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            self._json(200, {"object": "list", "data": [
                {"id": "claude-opus-4-8", "object": "model",
                 "created": 0, "owned_by": "anthropic"}]})
        else:
            self._json(404, {"error": {"message": "not found"}})

    def do_POST(self):
        if not self.path.rstrip("/").endswith("/chat/completions"):
            self._json(404, {"error": {"message": "not found"}})
            return
        t0 = time.time()
        try:
            n = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(n))
            model = req.get("model", "claude-opus-4-8")
            messages = req.get("messages", [])
            tools = req.get("tools") or []

            system_parts = [m.get("content", "") for m in messages
                            if m.get("role") == "system"
                            and isinstance(m.get("content"), str)]
            system_prompt = "\n\n".join(system_parts) or "You are a helpful assistant."
            if tools:
                schemas = json.dumps([t.get("function", t) for t in tools],
                                     indent=1)
                system_prompt += TOOL_INSTR.format(schemas=schemas)
            prompt = _render_transcript(messages)

            text, usage, extra = _call_claude(model, system_prompt, prompt)
            tool_calls = _parse_tool_calls(text) if tools else None

            msg = ({"role": "assistant", "content": None,
                    "tool_calls": tool_calls}
                   if tool_calls else
                   {"role": "assistant", "content": text})
            resp = {
                "id": f"chatcmpl-proxy{int(t0*1000)}",
                "object": "chat.completion",
                "created": int(t0),
                "model": model,
                "choices": [{"index": 0, "message": msg,
                             "finish_reason": "tool_calls" if tool_calls
                             else "stop"}],
                "usage": {
                    "prompt_tokens": usage.get("input_tokens",
                                               len(prompt) // 4),
                    "completion_tokens": usage.get("output_tokens",
                                                   len(text) // 4),
                    "total_tokens": (usage.get("input_tokens", 0)
                                     + usage.get("output_tokens", 0)),
                },
            }
            self._json(200, resp)
            rec = {
                "ts": t0, "dur_s": round(time.time() - t0, 1),
                "n_messages": len(messages), "n_tools": len(tools),
                "system_chars": len(system_prompt),
                "prompt_chars": len(prompt),
                "reply_chars": len(text),
                "tool_call": bool(tool_calls),
                "usage": usage, **extra,
            }
        except Exception as e:
            rec = {"ts": t0, "dur_s": round(time.time() - t0, 1),
                   "error": str(e)[:400]}
            try:
                self._json(500, {"error": {"message": str(e)[:400],
                                           "type": "proxy_error"}})
            except Exception:
                pass
        with _log_lock, open(LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    print(f"claude-p proxy on http://localhost:{PORT}/v1  log={LOG}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
