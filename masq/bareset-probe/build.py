#!/usr/bin/env python3
"""Bare-set boundary probe builder — emits transcripts.json (blind, canonical),
key.json (hidden), transcripts.md (for AJ). See PREREG.md for the locked
predictions and decision rules; this file is the item bank.

Labels: COLLISION / SUPERSESSION (controls + whisper, per the value-awareness
hinge) / BARE (truly unmarked middle; epistemically correct answer = UNCLEAR).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# Identical to gate 1, verbatim, for comparability.
PROMPT = """\
You are reviewing a team's session logs. Config values are set across multiple
sessions. For the TARGET fact named in the question, two different people each
set a value. Decide which case it is:

- SUPERSESSION: the second person knowingly changed a value the first had already
  set (aware of the prior state, intending to replace it).
- COLLISION: the second person set the value independently, unaware the first had
  already set it.
- UNCLEAR: the text does not let you reliably tell which.

Judge ONLY from what the text shows about awareness and intent. Do NOT use which
session has a later date/timestamp as evidence. Then state the outcome: for
SUPERSESSION the current value is the second value; for COLLISION the value is
contested and must be ESCALATED; for UNCLEAR, escalate.

Answer EXACTLY in this form, one line:
CLASSIFICATION: <SUPERSESSION|COLLISION|UNCLEAR>; CURRENT_VALUE: <value or CONTESTED>; ACTION: <USE_VALUE|ESCALATE>; REASON: <one sentence>

--- SCENARIO ---
"""

T = [
    dict(id=1, label="BARE", kind="bare", pair="launch-prep",
         note="forward-looking burst-capacity reason; no awareness route, no greenfield claim",
         body="""[Session log — search infrastructure]

— Tomas, May 5 (capacity baseline)
  Set the search service autoscaling max to 4 replicas — covers normal weekday
  traffic with comfortable margin.

— Rika, May 26 (campaign prep)
  Launch prep for the TV spot: setting the search service autoscaling max to 12
  replicas so we have burst capacity on air dates.

Q1. For the search service autoscaling max: did Rika knowingly override a value
Tomas had already set, or set it independently unaware of him? What is the current
value, or should it be escalated?"""),

    dict(id=2, label="SUPERSESSION", kind="control", pair=None,
         note="explicit: names prior writer, prior value, override + awareness",
         body="""[Session log — data warehouse]

— Mia, Sprint 2 (export pipeline)
  Export batch window set to 2 hours — gives the warehouse loader big
  consolidated chunks to work with.

— Jonas, Sprint 3 (loader stability)
  Mia set the export window to 2h last sprint; at that size the warehouse loader
  is choking on the chunks. Overriding it to 30 minutes — change-logged, and
  Mia's in the loop.

Q2. For the export batch window: did Jonas knowingly override a value Mia had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=3, label="SUPERSESSION", kind="whisper", pair=None,
         note="ONLY cue = presupposition verb 'bumping ... to' (implies a current TTL exists)",
         body="""[Session log — edge/CDN]

— Priit, Apr 1 (frontend iteration)
  CDN cache TTL for static assets set to 1 hour — invalidation stays fast while
  we're iterating on the frontend weekly.

— Sana, Apr 14 (cost review prep)
  Bumping the CDN cache TTL for static assets to 24 hours to cut origin egress
  ahead of the infrastructure cost review.

Q3. For the CDN static-asset cache TTL: did Sana knowingly override a value Priit
had already set, or set it independently unaware of him? Current value, or
escalate?"""),

    dict(id=4, label="BARE", kind="bare", pair="external-requirement",
         note="new external requirement (audit); forward-looking; no awareness route",
         body="""[Session log — platform observability]

— Owen, week 1 (logging setup)
  Application log retention set to 30 days — balances disk cost against how far
  back we ever actually debug.

— Lara, week 6 (compliance)
  SOC 2 prep: setting application log retention to 90 days, the auditors want a
  full quarter of history available.

Q4. For the application log retention: did Lara knowingly override a value Owen
had already set, or set it independently unaware of him? Current value, or
escalate?"""),

    dict(id=5, label="BARE", kind="bare", pair="new-workstream",
         note="picks up a workstream; forward-looking efficiency reason; no awareness route",
         body="""[Session log — partner API]

— Devi, day 2 (API defaults)
  Default page size for the partner API set to 25 — keeps response times
  predictable for the dashboard views.

— Kofi, day 15 (mobile sync)
  Picking up the mobile-sync workstream. Setting the partner API default page
  size to 100 so the sync client makes fewer round trips on cold start.

Q5. For the partner API default page size: did Kofi knowingly override a value
Devi had already set, or set it independently unaware of her? Current value, or
escalate?"""),

    dict(id=6, label="COLLISION", kind="control", pair=None,
         note="explicit greenfield claim ('nothing's configured as far as I can see'), parallel day",
         body="""[Session log — integrations]

— Asta, Thu 10:05 (webhook security)
  Webhook signatures: going with Ed25519 — smaller signatures, faster verify,
  and key rotation is much cleaner.

— Viktor, Thu 14:30 (partner pilot, separate thread)
  Partners need webhook signature verification before the pilot starts. Nothing's
  configured for signing as far as I can see, so I'm setting it to HMAC-SHA256 —
  every partner SDK supports it out of the box.

Q6. For the webhook signing algorithm: did Viktor knowingly override a value Asta
had already set, or set it independently unaware of her? Current value, or
escalate?"""),

    dict(id=7, label="BARE", kind="bare", pair="launch-prep",
         note="matched to #1: upcoming-event burst reason; no awareness route",
         body="""[Session log — analytics platform]

— Greta, Jun 2 (replica sizing)
  Set the analytics DB connection pool to 50 — matches what the read replicas
  comfortably serve.

— Pavel, Jun 20 (month-end readiness)
  Month-end close runs next week: setting the analytics DB connection pool to
  200 so the batch reports don't queue behind dashboard traffic.

Q7. For the analytics DB connection pool size: did Pavel knowingly override a
value Greta had already set, or set it independently unaware of her? Current
value, or escalate?"""),

    dict(id=8, label="SUPERSESSION", kind="whisper", pair=None,
         note="ONLY cue = presupposition verb 'raising ... to' (implies a current minimum exists)",
         body="""[Session log — identity & access]

— Noor, sprint 1 (password policy)
  Password policy: minimum length 8, plus the breached-password check on every
  change.

— Eli, sprint 5 (enterprise tier)
  Raising the minimum password length to 12 for the enterprise security review.

Q8. For the minimum password length: did Eli knowingly override a value Noor had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=9, label="BARE", kind="bare", pair="external-requirement",
         note="matched to #4: new consumer requirement; forward-looking; no awareness route",
         body="""[Session log — async jobs]

— Hana, Mon (queue defaults)
  Job queue visibility timeout set to 30 seconds — workers ack fast and stuck
  jobs come back for retry quickly.

— Mateus, three weeks later (media pipeline)
  The new video-transcode consumers hold a job for several minutes: setting the
  job queue visibility timeout to 5 minutes so the lease outlives an encode.

Q9. For the job queue visibility timeout: did Mateus knowingly override a value
Hana had already set, or set it independently unaware of her? Current value, or
escalate?"""),

    dict(id=10, label="BARE", kind="bare", pair="new-workstream",
         note="matched to #5: new deployment setup; security-vs-UX value tension; no awareness route",
         body="""[Session log — retail systems]

— Brigid, Feb 3 (call-centre rollout)
  Session idle timeout set to 20 minutes — shared machines in the call centre,
  we don't want sessions lingering.

— Yusuf, Feb 19 (kiosk deployment)
  Setting up the in-store kiosk deployment: configuring the session idle timeout
  to 60 minutes so shoppers aren't logged out mid-browse.

Q10. For the session idle timeout: did Yusuf knowingly override a value Brigid
had already set, or set it independently unaware of her? Current value, or
escalate?"""),
]

transcripts = [dict(id=t["id"], body=t["body"]) for t in T]
with open(os.path.join(HERE, "transcripts.json"), "w") as f:
    json.dump({"prompt": PROMPT, "transcripts": transcripts}, f, indent=2)

key = [dict(id=t["id"], label=t["label"], kind=t["kind"], pair=t["pair"],
            note=t["note"]) for t in T]
with open(os.path.join(HERE, "key.json"), "w") as f:
    json.dump(key, f, indent=2)

lines = [
    "# Bare-set boundary probe — blind classification",
    "",
    "**Your task:** for each scenario, classify the TARGET fact as one of:",
    "`COLLISION` (second writer unaware of the first) / `SUPERSESSION` (second",
    "writer knowingly overrode the first) / `UNCLEAR` (can't reliably tell).",
    "",
    "**Rule:** judge from awareness/intent in the text — do NOT use which session",
    "has the later date as evidence. Then say the current value or whether to escalate.",
    "",
    "Record answers as: `N: <COLLISION|SUPERSESSION|UNCLEAR> — <value or ESCALATE>`",
    "",
    "Do NOT open `key.json`, `PREREG.md`, or `opus-results-sealed.json` until",
    "you've classified all ten.",
    "",
    "---",
    "",
]
for t in T:
    lines.append(f"## Scenario {t['id']}")
    lines.append("")
    lines.append("```")
    lines.append(t["body"])
    lines.append("```")
    lines.append("")
with open(os.path.join(HERE, "transcripts.md"), "w") as f:
    f.write("\n".join(lines))

kinds = {}
for t in T:
    kinds[t["kind"]] = kinds.get(t["kind"], 0) + 1
print(f"Wrote {len(T)} scenarios: {kinds}")
print("Files: transcripts.json (blind+prompt), key.json (hidden), transcripts.md (for AJ).")
