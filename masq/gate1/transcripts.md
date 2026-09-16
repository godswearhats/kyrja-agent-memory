# Gate 1 — blind C3/C4 discriminability check

**Your task:** for each scenario, classify the TARGET fact as one of:
`COLLISION` (second writer unaware of the first) / `SUPERSESSION` (second
writer knowingly overrode the first) / `UNCLEAR` (can't reliably tell).

**Rule:** judge from awareness/intent in the text — do NOT use which session
has the later date as evidence. Then say the current value or whether to escalate.

Record answers as: `N: <COLLISION|SUPERSESSION|UNCLEAR> — <value or ESCALATE>`

Do NOT open `key.json` until you've classified all ten.

---

## Scenario 1

```
[Session log — platform team, sprint 14]

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
value, or should it be escalated?
```

## Scenario 2

```
[Session log — search & discovery]

— Lena, Jan 8 (v1 search API)
  Shipping the v1 search API. Capping page size at 50 results — keeps the
  response under our latency budget. Reporting export timeout stays at 30s.

— Ravi, Mar 19 (pre-launch audit)
  Going through search config before the public launch. Surprised the page-size
  cap isn't set anywhere — it looks unbounded to me. Setting it to 100 so we don't
  let someone request the whole index in one call.

Q2. For the search page-size cap: did Ravi knowingly override a value Lena had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 3

```
[Session log — payments]

— Dana, week 1 (billing webhooks)
  Billing webhook delivery: max retries = 3, exponential backoff. Good enough for
  launch.

— Sam, week 5 (incident follow-up)
  Dug into last month's billing webhook drops. Dana had max retries at 3, and
  transient 503s from the downstream are eating deliveries past that. Raising it
  to 5. Also left the auth token TTL alone at 30m.

Q3. For the billing webhook max retries: did Sam knowingly override a value Dana
had already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 4

```
[Session log — analytics]

— Nadia, Mon (reporting setup)
  Report export timeout set to 30 seconds. Most exports finish in under five.

— Felix, Thu (tenant escalation)
  Big-tenant report exports are timing out and the customers are furious. Setting
  the export timeout to 120 seconds so the large jobs can finish.

Q4. For the report export timeout: did Felix knowingly override a value Nadia had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 5

```
[Session log — storefront]

— Alice, Mar 10, 08:50 (checkout perf)
  Checkout rate limit set to 100 req/s — that's where p99 stays flat in the soak
  test. Cart service untouched.

— Bob, Mar 10, 15:20 (peak readiness)
  Saw Alice cap checkout at 100/s this morning. The peak-load test shows that
  throttles legitimate buyers during the sale, so I'm overriding it to 300 req/s.
  Logged in the change record; Alice is aware.

Q5. For the checkout rate limit: did Bob knowingly override a value Alice had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 6

```
[Session log — data platform]

— Wei, Apr 2 (ingest rollout)
  Ingest pipeline batch size set to 1000 for the initial rollout — conservative
  while we watch memory. Notifications rate limit left at 200/s.

— Carlos, Apr 3 (throughput tuning)
  Setting up the ingest pipeline batch size — config's a clean slate, nothing in
  there. Going with 5000 for throughput; the workers can handle it.

Q6. For the ingest pipeline batch size: did Carlos knowingly override a value Wei
had already set, or set it independently unaware of him? Current value, or escalate?
```

## Scenario 7

```
[Session log — messaging]

— Tom, day 1 (notifications)
  Notification fan-out rate limit: 200/s. Keeps us under the provider's quota.

— Aisha, day 9 (marketing campaign prep)
  Checked the notification config — it's at 200/s right now, but the marketing
  blast next week needs way more headroom. Moving it to 500/s and we'll request a
  quota bump from the provider.

Q7. For the notifications rate limit: did Aisha knowingly override a value Tom had
already set, or set it independently unaware of him? Current value, or escalate?
```

## Scenario 8

```
[Session log — payments / finance]

— Yuki, Sprint 3 (invoicing)
  Set the currency rounding mode to half-up for invoice totals. Matches what
  finance asked for.

— Paolo, Sprint 4 (tax compliance)
  The payment library defaults to half-up, which has a systematic bias. Switching
  us to bankers' rounding for EU tax compliance.

Q8. For the currency rounding mode: did Paolo knowingly override a value Yuki had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 9

```
[Session log — growth / experimentation]

— Omar, Fri 11:00 (dashboard launch)
  Enabling the new-dashboard feature flag — starting the rollout at 10% of users
  to watch error rates before we widen it.

— Ines, Fri 11:25 (dashboard launch, separate thread)
  Kicking off the new-dashboard rollout. Nobody's started it yet as far as I can
  see, so I'm opening it at 25% — we need volume to get signal on the funnel this
  week.

Q9. For the new-dashboard rollout percentage: did Ines knowingly override a value
Omar had already set, or set it independently unaware of him? Current value, or
escalate?
```

## Scenario 10

```
[Session log — identity]

— Grace, week 2 (account security)
  Login lockout threshold set to 5 failed attempts, then a 15-minute cooldown.

— Hassan, week 6 (support load)
  Support's drowning in lockout tickets — legit users fat-finger passwords more
  than 5 times. The threshold is at 5 now; raising it to 10 before the cooldown
  kicks in. Keeping the cooldown at 15 minutes.

Q10. For the login lockout threshold: did Hassan knowingly override a value Grace
had already set, or set it independently unaware of her? Current value, or escalate?
```
