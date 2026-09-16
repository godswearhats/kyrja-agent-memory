#!/usr/bin/env python3
"""Gate 1 builder — emits canonical transcripts.json, hidden key.json, and a
human-readable transcripts.md so AJ and Opus read byte-identical text.

Gate 1 question: is the collision-vs-supersession distinction reliably legible
from the TEXT (intent/awareness), with NO recourse to wall-clock? Pass bar:
clear items >=90% for both human and Opus. Boundary items are diagnostic — they
map where the line gets fuzzy and must be excluded from the 90% denominator.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# The classification prompt — identical for AJ's instructions and every Opus call.
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

# Canonical scenarios. label in {COLLISION, SUPERSESSION, UNCLEAR}.
# Slot order is intentionally non-alternating so base-rate can't be gamed.
T = [
    dict(id=1, label="COLLISION", difficulty="easy", herring="self-supersession distractor (billing timeout)",
         marker="\"no access-token TTL defined anywhere I can find\" -> unaware; same day",
         body="""[Session log — platform team, sprint 14]

— Priya, Tue 09:14 (auth hardening)
  Tightened the auth service this morning. Access-token TTL set to 30 minutes —
  short window keeps blast radius low if a token leaks. Also rotated the signing
  key and bumped the billing service's webhook timeout from 10s to 20s while I
  was in there.

— Marcus, Tue 16:40 (mobile client onboarding)
  Wiring up auth for the new mobile client. There's no access-token TTL defined
  anywhere I can find, so I'm setting it to 60 minutes — mobile users hate getting
  bounced mid-session. Left search result caching at the default 50 per page.

Q1. For the auth service access-token TTL: did Marcus knowingly override a value
Priya had already set, or set it independently unaware of her? What is the current
value, or should it be escalated?"""),

    dict(id=2, label="COLLISION", difficulty="hard (time misdirection: 2-month gap)", herring="large time gap tempts supersession",
         marker="\"isn't set anywhere... looks unbounded to me\" -> unaware despite gap",
         body="""[Session log — search & discovery]

— Lena, Jan 8 (v1 search API)
  Shipping the v1 search API. Capping page size at 50 results — keeps the
  response under our latency budget. Reporting export timeout stays at 30s.

— Ravi, Mar 19 (pre-launch audit)
  Going through search config before the public launch. Surprised the page-size
  cap isn't set anywhere — it looks unbounded to me. Setting it to 100 so we don't
  let someone request the whole index in one call.

Q2. For the search page-size cap: did Ravi knowingly override a value Lena had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=3, label="SUPERSESSION", difficulty="easy", herring="distractor: auth TTL mentioned but untouched",
         marker="\"Dana had max retries at 3 ... Raising it to 5\" -> aware + replace",
         body="""[Session log — payments]

— Dana, week 1 (billing webhooks)
  Billing webhook delivery: max retries = 3, exponential backoff. Good enough for
  launch.

— Sam, week 5 (incident follow-up)
  Dug into last month's billing webhook drops. Dana had max retries at 3, and
  transient 503s from the downstream are eating deliveries past that. Raising it
  to 5. Also left the auth token TTL alone at 30m.

Q3. For the billing webhook max retries: did Sam knowingly override a value Dana
had already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=4, label="UNCLEAR", difficulty="BOUNDARY", herring="symptom reaction without reference",
         marker="Felix reacts to a symptom (timeouts) but never references Nadia or '30s'; could be reacting to default behaviour. Maps the forbidden middle.",
         body="""[Session log — analytics]

— Nadia, Mon (reporting setup)
  Report export timeout set to 30 seconds. Most exports finish in under five.

— Felix, Thu (tenant escalation)
  Big-tenant report exports are timing out and the customers are furious. Setting
  the export timeout to 120 seconds so the large jobs can finish.

Q4. For the report export timeout: did Felix knowingly override a value Nadia had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=5, label="SUPERSESSION", difficulty="easy-medium (time misdirection: same day)", herring="same-day tempts collision",
         marker="\"Saw Alice cap checkout at 100 ... overriding it to 300 ... Alice is aware\"",
         body="""[Session log — storefront]

— Alice, Mar 10, 08:50 (checkout perf)
  Checkout rate limit set to 100 req/s — that's where p99 stays flat in the soak
  test. Cart service untouched.

— Bob, Mar 10, 15:20 (peak readiness)
  Saw Alice cap checkout at 100/s this morning. The peak-load test shows that
  throttles legitimate buyers during the sale, so I'm overriding it to 300 req/s.
  Logged in the change record; Alice is aware.

Q5. For the checkout rate limit: did Bob knowingly override a value Alice had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=6, label="COLLISION", difficulty="medium (verb misdirection)", herring="strong verb 'setting up ... 5000' but greenfield framing",
         marker="\"config's a clean slate, nothing in there\" -> unaware",
         body="""[Session log — data platform]

— Wei, Apr 2 (ingest rollout)
  Ingest pipeline batch size set to 1000 for the initial rollout — conservative
  while we watch memory. Notifications rate limit left at 200/s.

— Carlos, Apr 3 (throughput tuning)
  Setting up the ingest pipeline batch size — config's a clean slate, nothing in
  there. Going with 5000 for throughput; the workers can handle it.

Q6. For the ingest pipeline batch size: did Carlos knowingly override a value Wei
had already set, or set it independently unaware of him? Current value, or escalate?"""),

    dict(id=7, label="SUPERSESSION", difficulty="medium (soft, value-aware no name)", herring="no name reference, only current-value awareness",
         marker="\"it's at 200/s right now ... Moving it to 500/s\" -> value-aware replacement",
         body="""[Session log — messaging]

— Tom, day 1 (notifications)
  Notification fan-out rate limit: 200/s. Keeps us under the provider's quota.

— Aisha, day 9 (marketing campaign prep)
  Checked the notification config — it's at 200/s right now, but the marketing
  blast next week needs way more headroom. Moving it to 500/s and we'll request a
  quota bump from the provider.

Q7. For the notifications rate limit: did Aisha knowingly override a value Tom had
already set, or set it independently unaware of him? Current value, or escalate?"""),

    dict(id=8, label="UNCLEAR", difficulty="BOUNDARY", herring="references the value as a LIBRARY default, not as the other party's decision",
         marker="Paolo names half-up as the library default and 'switches' from it — may be unaware Yuki explicitly set it. Aware-of-value vs aware-of-write ambiguity.",
         body="""[Session log — payments / finance]

— Yuki, Sprint 3 (invoicing)
  Set the currency rounding mode to half-up for invoice totals. Matches what
  finance asked for.

— Paolo, Sprint 4 (tax compliance)
  The payment library defaults to half-up, which has a systematic bias. Switching
  us to bankers' rounding for EU tax compliance.

Q8. For the currency rounding mode: did Paolo knowingly override a value Yuki had
already set, or set it independently unaware of her? Current value, or escalate?"""),

    dict(id=9, label="COLLISION", difficulty="easy-medium", herring="near-simultaneous parallel threads",
         marker="\"Nobody's started it yet as far as I can see\" -> unaware, ~same time",
         body="""[Session log — growth / experimentation]

— Omar, Fri 11:00 (dashboard launch)
  Enabling the new-dashboard feature flag — starting the rollout at 10% of users
  to watch error rates before we widen it.

— Ines, Fri 11:25 (dashboard launch, separate thread)
  Kicking off the new-dashboard rollout. Nobody's started it yet as far as I can
  see, so I'm opening it at 25% — we need volume to get signal on the funnel this
  week.

Q9. For the new-dashboard rollout percentage: did Ines knowingly override a value
Omar had already set, or set it independently unaware of him? Current value, or
escalate?"""),

    dict(id=10, label="SUPERSESSION", difficulty="easy", herring="explicit current-value reference",
         marker="\"The threshold is at 5 now; raising it to 10\"",
         body="""[Session log — identity]

— Grace, week 2 (account security)
  Login lockout threshold set to 5 failed attempts, then a 15-minute cooldown.

— Hassan, week 6 (support load)
  Support's drowning in lockout tickets — legit users fat-finger passwords more
  than 5 times. The threshold is at 5 now; raising it to 10 before the cooldown
  kicks in. Keeping the cooldown at 15 minutes.

Q10. For the login lockout threshold: did Hassan knowingly override a value Grace
had already set, or set it independently unaware of her? Current value, or escalate?"""),
]

# transcripts.json — blind (no labels), canonical text for both readers.
transcripts = [dict(id=t["id"], body=t["body"]) for t in T]
with open(os.path.join(HERE, "transcripts.json"), "w") as f:
    json.dump({"prompt": PROMPT, "transcripts": transcripts}, f, indent=2)

# key.json — hidden.
key = [dict(id=t["id"], label=t["label"], difficulty=t["difficulty"],
            herring=t["herring"], marker=t["marker"]) for t in T]
with open(os.path.join(HERE, "key.json"), "w") as f:
    json.dump(key, f, indent=2)

# transcripts.md — human-readable, blind, for AJ to classify by hand.
lines = [
    "# Gate 1 — blind C3/C4 discriminability check",
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
    "Do NOT open `key.json` until you've classified all ten.",
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

n_clear = sum(1 for t in T if t["difficulty"] != "BOUNDARY")
n_col = sum(1 for t in T if t["label"] == "COLLISION")
n_sup = sum(1 for t in T if t["label"] == "SUPERSESSION")
n_unc = sum(1 for t in T if t["label"] == "UNCLEAR")
print(f"Wrote {len(T)} scenarios: {n_col} collision, {n_sup} supersession, {n_unc} boundary/unclear.")
print(f"Clear items (90% denominator): {n_clear}. Boundary items (diagnostic): {len(T)-n_clear}.")
print("Files: transcripts.json (blind+prompt), key.json (hidden), transcripts.md (for AJ).")
