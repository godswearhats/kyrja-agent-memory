# Bare-set boundary probe — blind classification

**Your task:** for each scenario, classify the TARGET fact as one of:
`COLLISION` (second writer unaware of the first) / `SUPERSESSION` (second
writer knowingly overrode the first) / `UNCLEAR` (can't reliably tell).

**Rule:** judge from awareness/intent in the text — do NOT use which session
has the later date as evidence. Then say the current value or whether to escalate.

Record answers as: `N: <COLLISION|SUPERSESSION|UNCLEAR> — <value or ESCALATE>`

Do NOT open `key.json`, `PREREG.md`, or `opus-results-sealed.json` until
you've classified all ten.

---

## Scenario 1

```
[Session log — search infrastructure]

— Tomas, May 5 (capacity baseline)
  Set the search service autoscaling max to 4 replicas — covers normal weekday
  traffic with comfortable margin.

— Rika, May 26 (campaign prep)
  Launch prep for the TV spot: setting the search service autoscaling max to 12
  replicas so we have burst capacity on air dates.

Q1. For the search service autoscaling max: did Rika knowingly override a value
Tomas had already set, or set it independently unaware of him? What is the current
value, or should it be escalated?
```

## Scenario 2

```
[Session log — data warehouse]

— Mia, Sprint 2 (export pipeline)
  Export batch window set to 2 hours — gives the warehouse loader big
  consolidated chunks to work with.

— Jonas, Sprint 3 (loader stability)
  Mia set the export window to 2h last sprint; at that size the warehouse loader
  is choking on the chunks. Overriding it to 30 minutes — change-logged, and
  Mia's in the loop.

Q2. For the export batch window: did Jonas knowingly override a value Mia had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 3

```
[Session log — edge/CDN]

— Priit, Apr 1 (frontend iteration)
  CDN cache TTL for static assets set to 1 hour — invalidation stays fast while
  we're iterating on the frontend weekly.

— Sana, Apr 14 (cost review prep)
  Bumping the CDN cache TTL for static assets to 24 hours to cut origin egress
  ahead of the infrastructure cost review.

Q3. For the CDN static-asset cache TTL: did Sana knowingly override a value Priit
had already set, or set it independently unaware of him? Current value, or
escalate?
```

## Scenario 4

```
[Session log — platform observability]

— Owen, week 1 (logging setup)
  Application log retention set to 30 days — balances disk cost against how far
  back we ever actually debug.

— Lara, week 6 (compliance)
  SOC 2 prep: setting application log retention to 90 days, the auditors want a
  full quarter of history available.

Q4. For the application log retention: did Lara knowingly override a value Owen
had already set, or set it independently unaware of him? Current value, or
escalate?
```

## Scenario 5

```
[Session log — partner API]

— Devi, day 2 (API defaults)
  Default page size for the partner API set to 25 — keeps response times
  predictable for the dashboard views.

— Kofi, day 15 (mobile sync)
  Picking up the mobile-sync workstream. Setting the partner API default page
  size to 100 so the sync client makes fewer round trips on cold start.

Q5. For the partner API default page size: did Kofi knowingly override a value
Devi had already set, or set it independently unaware of her? Current value, or
escalate?
```

## Scenario 6

```
[Session log — integrations]

— Asta, Thu 10:05 (webhook security)
  Webhook signatures: going with Ed25519 — smaller signatures, faster verify,
  and key rotation is much cleaner.

— Viktor, Thu 14:30 (partner pilot, separate thread)
  Partners need webhook signature verification before the pilot starts. Nothing's
  configured for signing as far as I can see, so I'm setting it to HMAC-SHA256 —
  every partner SDK supports it out of the box.

Q6. For the webhook signing algorithm: did Viktor knowingly override a value Asta
had already set, or set it independently unaware of her? Current value, or
escalate?
```

## Scenario 7

```
[Session log — analytics platform]

— Greta, Jun 2 (replica sizing)
  Set the analytics DB connection pool to 50 — matches what the read replicas
  comfortably serve.

— Pavel, Jun 20 (month-end readiness)
  Month-end close runs next week: setting the analytics DB connection pool to
  200 so the batch reports don't queue behind dashboard traffic.

Q7. For the analytics DB connection pool size: did Pavel knowingly override a
value Greta had already set, or set it independently unaware of her? Current
value, or escalate?
```

## Scenario 8

```
[Session log — identity & access]

— Noor, sprint 1 (password policy)
  Password policy: minimum length 8, plus the breached-password check on every
  change.

— Eli, sprint 5 (enterprise tier)
  Raising the minimum password length to 12 for the enterprise security review.

Q8. For the minimum password length: did Eli knowingly override a value Noor had
already set, or set it independently unaware of her? Current value, or escalate?
```

## Scenario 9

```
[Session log — async jobs]

— Hana, Mon (queue defaults)
  Job queue visibility timeout set to 30 seconds — workers ack fast and stuck
  jobs come back for retry quickly.

— Mateus, three weeks later (media pipeline)
  The new video-transcode consumers hold a job for several minutes: setting the
  job queue visibility timeout to 5 minutes so the lease outlives an encode.

Q9. For the job queue visibility timeout: did Mateus knowingly override a value
Hana had already set, or set it independently unaware of her? Current value, or
escalate?
```

## Scenario 10

```
[Session log — retail systems]

— Brigid, Feb 3 (call-centre rollout)
  Session idle timeout set to 20 minutes — shared machines in the call centre,
  we don't want sessions lingering.

— Yusuf, Feb 19 (kiosk deployment)
  Setting up the in-store kiosk deployment: configuring the session idle timeout
  to 60 minutes so shoppers aren't logged out mid-browse.

Q10. For the session idle timeout: did Yusuf knowingly override a value Brigid
had already set, or set it independently unaware of her? Current value, or
escalate?
```
