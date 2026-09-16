---
tags:
  - exclude-from-graph
---
# Kyrja Wiki

*Research wiki for Kyrja — the agent-memory work. This is the canonical thinking surface; all atomized research lives here.*

---

## How to start

1. **Read [NOW.md](./NOW.md) first.** Current active question, what we're working on right now, immediate next step. This is the working memory between sessions.
2. **Drill into the graph from there.** Pages are interlinked; the wiki is not designed to be read end-to-end.
3. **Use [index.md](./index.md) as the catalog** if you're looking for something specific.
4. **See [SCHEMA.md](./SCHEMA.md) for conventions** — page types, lifecycle, frontmatter, link rules, lint.

---

## What lives here

The wiki captures all of our thinking about agent memory — not just what's load-bearing for the current wedge. Inclusion test: *"is this a real research idea worth tracking?"* — not *"is this in scope for what we ship?"* Anti-sprawl rules (3+ inbound refs OR own status lifecycle) are the gate against duplication, not against ambition.

---

## Page types

| Type | Purpose | Lifecycle |
|---|---|---|
| [`hypothesis/`](./hypothesis/) | falsifiable claim under test | PROPOSED → SUPPORTED \| REJECTED \| SUPERSEDED |
| [`experiment/`](./experiment/) | something we ran | PROPOSED → RUNNING → LANDED \| INVALIDATED |
| [`decision/`](./decision/) | architectural or methodological choice | ACTIVE \| REVERSED \| SUPERSEDED |
| [`concept/`](./concept/) | primitive cited across pages | timeless |
| [`source/`](./source/) | external paper / doc we cite | timeless |
| [`incumbent/`](./incumbent/) | competing or related system | dated (`status_current_as_of`) |
| [`open-question/`](./open-question/) | known gap awaiting resolution | OPEN → HYPOTHESIS-FORMED \| RESOLVED \| DEPRIORITIZED |

Each subdirectory's conventions are detailed in [SCHEMA.md § Page types](./SCHEMA.md#page-types-seven).

---

## Root files

| File | Role | Update cadence |
|---|---|---|
| [README.md](./README.md) | orientation; what this wiki is and how to use it | rarely |
| [NOW.md](./NOW.md) | working state; active question, current sub-task, next step | end of each working session |
| [index.md](./index.md) | catalog of every page by type | per ingest |
| [SCHEMA.md](./SCHEMA.md) | conventions, frontmatter, link rules, lint | per schema change (requires AJ approval) |
| [log.md](./log.md) | append-only ingest record | per ingest |

---

## How the wiki gets maintained

- **Ingest** at end of working session — `/wiki-ingest` skill folds new material into the appropriate pages.
- **Lint** on demand — `/wiki-lint` skill checks anti-sprawl, evidence-anchoring, link rules.
- **Working state** in [NOW.md](./NOW.md) — read first each session, updated last.

---

## Cross-agent material

Other agents on the team (Kerman/red, Eira/coral, …) keep their work under `/team-share/<colour>/`. The wiki cites them; it doesn't duplicate. See [SCHEMA.md § Cross-agent federation](./SCHEMA.md#cross-agent-federation).

---

## Archive

Documents that have been replaced or retired live in [`./archive/`](./archive/). Kept for historical reference; do not treat as current.
