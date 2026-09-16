You will receive an agent work session transcript. Extract a memory encoding into the structured slots below. Output ONLY the structured content — no preamble, no commentary, no tool calls, no file saving. Do NOT add prose paragraphs, transitional sentences, or narrative connective tissue. Fill each slot with terse, factual content only.

Use this exact format:

```
BUG: <one-paragraph statement of the bug, including symptoms and user-facing behavior>

LOCATION:
  - file: <path>
  - function: <name>
  - line: <number>
  - related_locations: [<other relevant file:function:line entries>]

FIX_PATTERN: <what shape the fix takes — e.g., "forward kwarg X through wrapper Y", "add nil check before Z" — describe the pattern, not just the diff>

CODE_CHANGES:
  - <each edit as: file:line, old → new, one per entry>

RELATED_IMPORTS_AND_UTILITIES: <existing functions, imports, or patterns in the file or codebase that the fix reuses>

DEAD_ENDS: <things the agent tried or considered that did not pan out, and why>

GOTCHAS: <non-obvious facts about the environment, tooling, edge cases, or codebase conventions>

VERIFICATION: <what tests or checks confirmed the fix works>
```

Be specific. Use exact paths, function names, line numbers. Do not invent slots; if a slot has no content, write `NONE`.

Target length: 1200 tokens. This is a hard limit -- do not exceed it.

## Transcript

{transcript}
