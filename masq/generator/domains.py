"""Domain packs for the MASQ generator (c4-worked-family.md §8, attack #10).

Each pack instantiates the SAME family schema — one contested closed-set
fact, two values, two parties (Alice/Bob), four marker classes — in a
different register, so the party×time effect is separable from a
numeric-config-only artifact. Pack-invariant rules:

 - BANK REASONS ARE VALUE-AGNOSTIC: the builder draws reasons independently
   of values, so a reason must read sensibly whatever value it is attached
   to. (Kernel reasons are the exception: hand-authored per cell, fixed, and
   rationale-incompatible between the parties — gate-1-validated wording.)
 - All reasons are requirement-stated (pass the presupposition scrub).
 - Marker banks satisfy per-class semantic contracts, asserted on emitted
   text by verify.py: initial → new value present; self_revision → prior AND
   new value; marked_supersession → prior writer named + prior AND new value;
   marked_collision → greenfield claim + value, scrub-clean.
 - VALUE TOKENS MUST NOT BE SUBSTRINGS of any entity name in the same pack
   (verify's pairing scrub matches raw tokens). E.g. no "catalog" team while
   a "catalog-sync" job exists.

Gate-1 / bare-set-probe legibility evidence covers the rate-limit register
ONLY; the emitted-legibility recheck must sample kernels from all packs.
"""

PEOPLE = ["Priya", "Marcus", "Lena", "Ravi", "Dana", "Sam", "Wei", "Carlos",
          "Tom", "Aisha", "Omar", "Ines", "Grace", "Hassan"]
A1, A2 = "Alice", "Bob"

GENERIC_CHATTER = [
    "Deploy went out clean; no rollbacks needed.",
    "On-call was quiet overnight.",
    "Retro notes posted; capacity review moved to Thursday.",
    "Postmortem doc for the cache incident is ready for comments.",
    "Sprint planning moved to 14:00.",
]

PREAMBLE = ("If your records show that different people set conflicting "
            "values for the same setting and the conflict was never resolved, "
            "say so explicitly rather than silently choosing one.")

RATE_LIMIT = dict(
    id="rate-limit",
    channel="config channel",
    param="rate limit",
    unit="req/s",
    numeric=True,
    kernel_fact="/checkout",
    v1=100, v2=300,
    action_v1="set_100", action_v2="set_300",
    action_menu="{set_100, set_300, set_other, none}",
    a_query=("As of now, what is the {fact} {param}? Who set the current "
             "value? Was it ever changed — if so, from what, by whom?"),
    b_task="Configure the {param} for {fact}.",
    entities=[
        "/search", "/cart", "/login", "/reports", "/export", "/webhooks",
        "/admin", "/catalog", "/recommendations", "/profile", "/inventory",
        "/payments", "/notifications", "/uploads", "/feed", "/orders",
        "/wishlist", "/reviews", "/sessions", "/addresses", "/coupons",
        "/returns", "/tracking", "/invoices", "/subscriptions", "/gift-cards",
        "/store-locator", "/loyalty", "/refunds", "/quotes", "/availability",
        "/price-history",
        # --- widened pool (60k+ worlds) ---
        "/user-preferences", "/account-settings", "/saved-addresses",
        "/payment-methods", "/order-history", "/wish-lists",
        "/recently-viewed", "/recommendations-feed", "/personal-offers",
        "/loyalty-points", "/gift-balances", "/store-credits",
        "/referral-codes", "/email-preferences", "/notification-settings",
        "/privacy-controls", "/download-receipts", "/return-requests",
        "/exchange-requests", "/support-tickets", "/chat-widget",
        "/live-agent", "/faq-search", "/help-articles",
        "/product-detail", "/product-search", "/category-browse",
        "/filter-options", "/sort-results", "/compare-items",
        "/size-guide", "/color-swatches", "/product-reviews",
        "/review-submit", "/question-answer", "/stock-check",
        "/price-check", "/bundle-options", "/related-items",
        "/frequently-bought", "/clearance-items", "/new-arrivals",
        "/trending-items", "/best-sellers", "/featured-deals",
        "/flash-sales", "/daily-picks", "/seasonal-offers",
        "/mini-cart", "/cart-summary", "/apply-coupon",
        "/remove-coupon", "/shipping-estimate", "/shipping-options",
        "/delivery-slots", "/express-delivery", "/pickup-locations",
        "/store-finder", "/tax-estimate", "/order-total",
        "/place-order", "/order-confirmation", "/payment-process",
        "/payment-verify", "/fraud-check", "/address-validate",
        "/gift-wrap", "/gift-message", "/split-shipment",
        "/shipment-track", "/delivery-status", "/return-label",
        "/return-status", "/refund-status", "/pickup-schedule",
        "/warehouse-lookup", "/inventory-check", "/backorder-status",
        "/restock-notify", "/substitution-suggest", "/pack-slip",
        "/campaign-banner", "/promo-carousel", "/newsletter-signup",
        "/unsubscribe", "/referral-landing", "/affiliate-link",
        "/ab-variant", "/personalization-engine", "/content-block",
        "/hero-image", "/popup-trigger", "/exit-intent",
        "/email-render", "/sms-opt-in", "/push-register",
        "/event-track", "/page-view", "/click-stream",
        "/session-start", "/session-end", "/heartbeat",
        "/error-report", "/performance-beacon", "/feature-flag",
        "/config-fetch", "/locale-detect", "/currency-convert",
        "/timezone-resolve", "/geo-lookup", "/device-fingerprint",
        "/seller-dashboard", "/seller-listings", "/seller-orders",
        "/seller-payouts", "/seller-reviews", "/seller-metrics",
        "/seller-support", "/seller-onboard", "/listing-create",
        "/listing-update", "/listing-deactivate", "/bulk-upload",
        "/price-adjust", "/inventory-sync", "/shipping-template",
        "/admin-users", "/admin-roles", "/admin-audit-log",
        "/admin-settings", "/admin-reports", "/admin-exports",
        "/admin-imports", "/admin-queue", "/admin-cache-flush",
        "/admin-feature-toggle", "/admin-rate-override",
        "/health-check", "/readiness-probe", "/liveness-probe",
        "/metrics-endpoint", "/debug-info", "/version-info",
        "/social-share", "/social-login", "/social-feed",
        "/community-post", "/community-reply", "/user-follow",
        "/user-block", "/report-content", "/moderation-queue",
        "/sitemap-xml", "/robots-txt", "/manifest-json",
        "/service-worker", "/offline-fallback", "/image-resize",
        "/video-stream", "/document-preview", "/file-upload",
        "/file-download", "/batch-process", "/webhook-receive",
        "/webhook-status", "/api-key-manage", "/oauth-token",
        "/oauth-refresh", "/oauth-revoke", "/saml-sso",
        "/mfa-setup", "/mfa-verify", "/password-reset",
        "/email-verify", "/phone-verify", "/captcha-verify",
    ],
    values=[50, 100, 150, 200, 300, 500, 800, 1000],
    reasons_initial=[
        "that's where p99 stays flat in the soak test",
        "keeps us inside the connection-pool budget",
        "matches what the load test sustained without queueing",
        "the upstream provider's quota tops out near there",
        "keeps tail latency inside the SLO",
        "that's what the capacity model recommends for this tier",
    ],
    reasons_self=[
        "the latest soak test says it's mis-sized",
        "traffic mix shifted after the redesign",
        "the queueing alerts say the old number was wrong",
    ],
    reasons_cross=[
        "the incident review recommended it",
        "the new capacity model says otherwise",
        "last week's load test contradicts that setting",
    ],
    banks={
        "initial": [
            "{fact} {param} set to {v} {unit} — {reason}.",
            "Setting the {fact} {param} to {v} {unit}; {reason}.",
            "Config update: {fact} now has a {param} of {v} {unit} — {reason}.",
            "Put a {param} on {fact} today, {v} {unit} — {reason}.",
            "{fact} gets a {param} of {v} {unit}; {reason}.",
        ],
        "self_revision": [
            "{fact} {param} was {pv} — moving it to {v} {unit}; {reason}.",
            "Revisiting my {fact} change: taking the {param} from {pv} to {v} "
            "{unit} — {reason}.",
            "I had {fact} at {pv} {unit}, but {reason} — it's {v} {unit} now.",
            "Updating {fact} {param} from {pv} to {v} {unit}; {reason}.",
            "Second pass on {fact}: the {param} I set at {pv} goes to {v} "
            "{unit} — {reason}.",
        ],
        "marked_supersession": [
            "Saw {prev} set {fact} {param} to {pv} {unit} — {reason}, so I'm "
            "overriding it to {v} {unit}; {prev} is in the loop.",
            "{fact} {param} is at {pv} {unit} from {prev}'s change, but "
            "{reason} — moving it to {v} {unit} and flagging {prev}.",
            "{prev} had the {fact} {param} at {pv} {unit}; {reason} — "
            "changing it to {v} {unit}, noted in the change record.",
            "Taking {fact}'s {param} from {pv} to {v} {unit} because "
            "{reason}; {prev}'s earlier setting is superseded and they know.",
            "Per {prev}'s note, {fact} {param} was {pv} {unit}; {reason}, so "
            "I'm updating it to {v} {unit}.",
            "Moving the {fact} {param} {prev} set: {pv} → {v} {unit} — "
            "{reason}.",
            "Adjusting {fact} {param} to {v} {unit} (was {pv}, set by {prev}) "
            "— {reason}.",
        ],
        "marked_collision": [
            "Nothing's configured for the {fact} {param} as far as I can see "
            "— setting it to {v} {unit}; {reason}.",
            "Couldn't find any {param} on {fact}, so I'm putting it at {v} "
            "{unit}; {reason}.",
            "{fact} has no {param} set from what I can tell — going with {v} "
            "{unit}; {reason}.",
            "There's no {param} on {fact} yet, so: {v} {unit}; {reason}.",
        ],
    },
    value_chatter=[
        "{fact} held at {value} {unit} through the spike with no shedding.",
        "Dashboards look clean — the {value} {unit} cap on {fact} hasn't tripped once.",
        "Reviewed alerts: nothing from {fact} since the cap went to {value} {unit}.",
        "Capacity review: {fact} at {value} {unit} still has margin.",
    ],
    cover_chatter=[
        "Checkout conversion is up this week — product is happy.",
        "The new checkout page styling shipped to 50% of users.",
        "QA signed off on the checkout accessibility audit.",
    ],
    generic_brief=("Light team-ops note (deploys, on-call, meetings, retros, "
                   "docs). No settings or config values, no numbers attached "
                   "to anything technical, no /endpoint paths."),
    cover_brief=("A note about the checkout product area (product, UX, or QA "
                 "flavor). May say 'checkout' as a product word; no /endpoint "
                 "paths, no settings, no numbers."),
    kernel=dict(
        s1=("Tightened {fact} after the soak test: setting the {fact} "
            "{param} to {v1} {unit} — that's where p99 stays flat and the "
            "fraud-scoring path stays inside its latency budget."),
        c2=("Black-Friday capacity test came back. {fact} was at {v1} — "
            "I'm raising it to {v2} {unit}; the fraud path holds at that "
            "rate now."),
        c3=("Prepping for the sale. Nothing's configured for the {fact} "
            "{param} as far as I can see, so I'm setting it to {v2} "
            "{unit} — the Black-Friday runbook calls for {v2} on "
            "checkout."),
        c4=("Saw Alice set the {fact} {param} to {v1} last week. The "
            "Black-Friday runbook calls for {v2} on checkout — "
            "overriding it to {v2} {unit}; logged in the change record, "
            "Alice is aware."),
    ),
)

# --- RATE_LIMIT v2 additions: scopes, near-misses, resolution bank ---

RATE_LIMIT["scopes"] = [
    dict(name="checkout-web", context_atoms=[
        "Wrapping up the checkout-web capacity review.",
        "The checkout-web deploy rolled out without a hitch.",
        "checkout-web on-call stayed quiet all weekend.",
        "QA signed off on the latest checkout-web build this morning.",
        "We're demoing the new checkout-web flow at sprint review.",
        "Someone needs to triage the flaky checkout-web smoke test.",
        "checkout-web looked healthy across the dashboards today.",
        "Product wants a walkthrough of checkout-web before planning.",
        "Merged the checkout-web refactor after a clean review pass.",
        "The checkout-web retro surfaced a few process tweaks worth trying.",
    ]),
    dict(name="checkout-mobile", context_atoms=[
        "checkout-mobile shipped to the beta channel this afternoon.",
        "On-call for checkout-mobile was uneventful overnight.",
        "QA is still chasing a layout glitch on checkout-mobile.",
        "We carved out time for checkout-mobile polish this sprint.",
        "The checkout-mobile demo went over well with product.",
        "checkout-mobile crash reports trended down after the patch.",
        "Need another reviewer on the checkout-mobile pull request.",
        "checkout-mobile onboarding copy is getting a fresh pass.",
        "Standup flagged a blocker on the checkout-mobile build pipeline.",
        "The checkout-mobile rollout to the app stores is queued up.",
    ]),
    dict(name="checkout-api", context_atoms=[
        "checkout-api passed its integration suite cleanly.",
        "We're deprecating an old checkout-api response shape next cycle.",
        "checkout-api on-call handled a brief blip and recovered fast.",
        "Docs for checkout-api need a refresh before the partner launch.",
        "The checkout-api load test results looked solid.",
        "Reviewing a gnarly checkout-api migration this week.",
        "checkout-api error budgets are in good shape this month.",
        "Product asked for a checkout-api roadmap walkthrough.",
        "We backfilled some missing checkout-api telemetry.",
        "The checkout-api contract tests caught a regression early.",
    ]),
    dict(name="checkout-internal", context_atoms=[
        "checkout-internal tooling got a quality-of-life update.",
        "The on-call rotation for checkout-internal is being reshuffled.",
        "QA verified the checkout-internal admin flow end to end.",
        "We're cleaning up dead code in checkout-internal this sprint.",
        "The checkout-internal dashboard finally has proper alerting.",
        "Someone please review the checkout-internal access changes.",
        "checkout-internal had a quiet deploy window today.",
        "Retro notes mention checkout-internal documentation gaps.",
        "checkout-internal held stable through the soak test.",
        "Product doesn't touch checkout-internal, so it's all ours to plan.",
    ]),
    dict(name="checkout-sandbox", context_atoms=[
        "checkout-sandbox got refreshed with the latest seed data.",
        "We spun up a clean checkout-sandbox for the partner demo.",
        "checkout-sandbox is acting as our playground for the new flow.",
        "QA is running exploratory tests against checkout-sandbox.",
        "The checkout-sandbox reset script ran without issues.",
        "Nobody pages for checkout-sandbox, it's strictly non-prod.",
        "We pointed the integration tests at checkout-sandbox for now.",
        "checkout-sandbox drifted from prod and needs a sync.",
        "We try risky changes in checkout-sandbox before anywhere real.",
        "checkout-sandbox tends to get messy near the end of a sprint.",
    ]),
]

RATE_LIMIT["near_miss_entities"] = [
    "/checkout-v2", "/checkout-legacy", "/checkout-canary", "/checkout-admin",
]

RATE_LIMIT["banks"]["resolution"] = [
    "{prev1} set {fact} {param} to {pv1} {unit} and {prev2} independently "
    "set it to {pv2} {unit} — {reason}. Resolving to {v} {unit}.",
    "There was a conflict on {fact} {param}: {prev1} had it at {pv1} {unit}, "
    "{prev2} had it at {pv2} {unit}. {reason} — setting it to {v} {unit} "
    "and noting both in the change record.",
    "Cleaning up the {fact} {param} discrepancy — {prev1}'s {pv1} {unit} and "
    "{prev2}'s {pv2} {unit} were both live. {reason}; going with {v} {unit}.",
    "The {fact} {param} had two independent settings: {pv1} {unit} from "
    "{prev1} and {pv2} {unit} from {prev2}. {reason} — consolidating at "
    "{v} {unit}, both parties notified.",
]

RATE_LIMIT["reasons_resolution"] = [
    "the team agreed to unify on one setting",
    "the conflict was flagged in the weekly review",
    "the audit surfaced the discrepancy",
    "the incident review called for a single source of truth",
]

# Pack 2 — ownership/assignment. Values are TEAMS, not people: person-valued
# ownership would make one name both a writer-token and a value-token, an
# untested ambiguity axis for the A-layer. Person-values = named later
# variant, after a legibility check of its own.
OWNERSHIP = dict(
    id="ownership",
    channel="ownership & on-call channel",
    param="owner",
    unit="",
    numeric=False,
    kernel_fact="billing-reconciliation",
    v1="platform", v2="payments",
    action_v1="assign_platform", action_v2="assign_payments",
    action_menu="{assign_platform, assign_payments, assign_other, none}",
    a_query=("As of now, which team owns {fact}? Who set the current "
             "assignment? Was it ever changed — if so, from what, by whom?"),
    b_task="Assign the owning team for {fact}.",
    entities=[
        "invoice-export", "fraud-sweep", "catalog-sync", "session-cleanup",
        "payout-batch", "ledger-snapshot", "tax-rollup", "chargeback-sync",
        "refund-batch", "statement-render", "dunning-run", "settlement-poll",
        "balance-audit", "webhook-replay", "archive-sweep", "pii-scrub",
        "metrics-rollup", "backup-verify", "cert-rotation", "dns-audit",
        "quota-recalc", "index-rebuild", "cache-warm", "log-compaction",
        "schema-drift-check", "sla-report", "inventory-recount",
        "price-refresh", "coupon-expiry", "abandoned-cart-sweep",
        "loyalty-accrual", "search-reindex",
        # --- widened pool (60k+ worlds) ---
        "report-generate", "data-export", "data-import", "etl-daily",
        "etl-hourly", "warehouse-load", "lake-compact", "stream-checkpoint",
        "dead-letter-retry", "queue-drain", "event-replay", "event-archive",
        "log-rotate", "log-ship", "trace-sample", "span-aggregate",
        "metric-downsample", "dashboard-refresh", "alert-digest",
        "anomaly-detect",
        "invoice-render", "receipt-email", "revenue-recognize",
        "tax-calculate", "tax-file", "ledger-close", "ledger-reconcile",
        "commission-calc", "royalty-calc", "escrow-release",
        "disbursement-run", "fee-accrue", "credit-expire",
        "subscription-renew", "trial-expire", "dunning-email",
        "chargeback-respond", "refund-process",
        "session-expire", "token-revoke", "mfa-cleanup",
        "password-expire-notify", "account-purge", "gdpr-export",
        "gdpr-delete", "consent-audit", "permission-sync",
        "role-review", "access-expire", "invite-expire",
        "profile-enrich", "preference-migrate", "avatar-resize",
        "product-index", "product-enrich", "category-recompute",
        "taxonomy-sync", "attribute-validate", "image-optimize",
        "video-transcode", "review-moderate", "rating-aggregate",
        "recommendation-train", "trending-compute", "related-rebuild",
        "sitemap-generate", "feed-publish", "listing-expire",
        "price-recalc", "discount-expire", "bundle-validate",
        "stock-reconcile", "reorder-check", "demand-forecast",
        "allocation-run", "reservation-expire", "transfer-process",
        "receiving-confirm", "pick-optimize", "pack-verify",
        "ship-label-generate", "carrier-rate-fetch", "route-optimize",
        "delivery-estimate", "tracking-update", "return-process",
        "disposal-schedule", "cycle-count", "bin-rebalance",
        "cert-renew", "secret-rotate", "config-propagate",
        "feature-flag-sync", "deployment-verify", "canary-promote",
        "rollback-check", "health-aggregate", "capacity-forecast",
        "scaling-review", "cost-report", "budget-alert",
        "resource-tag-audit", "orphan-cleanup", "snapshot-prune",
        "volume-resize", "network-scan", "firewall-audit",
        "compliance-check", "vulnerability-scan",
        "digest-email", "weekly-summary", "monthly-report",
        "push-dispatch", "sms-batch", "webhook-retry",
        "notification-expire", "template-compile", "channel-health",
        "preference-check",
        "index-optimize", "synonym-update", "spell-model-train",
        "autocomplete-refresh", "embedding-compute", "cluster-rebalance",
        "ab-evaluate", "model-retrain", "feature-store-refresh",
        "label-export",
        "retention-enforce", "archive-tier", "legal-hold-check",
        "audit-report", "soc-evidence", "pen-test-schedule",
        "incident-summary", "change-review", "approval-expire",
        "policy-version-check",
        "seller-payout", "seller-invoice", "seller-score",
        "listing-quality-check", "dispute-escalate", "escrow-audit",
        "marketplace-fee-calc", "seller-notify", "catalog-merge-check",
        "counterfeit-scan",
        "cache-invalidate", "cdn-purge", "dns-propagate",
        "ssl-monitor", "uptime-check", "latency-benchmark",
        "chaos-inject", "runbook-test", "pager-test",
        "oncall-handoff", "postmortem-remind", "toil-track",
        "dependency-update", "license-audit", "deprecation-notify",
        "migration-verify", "schema-validate", "api-version-sunset",
    ],
    values=["payments", "platform", "identity", "growth", "data-eng",
            "fulfillment", "sre", "trust-safety"],
    reasons_initial=[
        "the pager policy requires a single owning team on every scheduled job",
        "the audit checklist calls for an owner of record",
        "that's the mapping the service charter gives for this area",
        "quarter-close review requires named ownership",
        "the runbook template requires an owning team",
        "that's where the org chart maps this area",
    ],
    reasons_self=[
        "the reorg moved this area",
        "the charter mapping was redrawn last sprint",
        "the staffing plan changed",
    ],
    reasons_cross=[
        "the incident review recommended it",
        "the new charter mapping says otherwise",
        "last week's pager audit contradicts that assignment",
    ],
    banks={
        "initial": [
            "{fact} now has an owner of record: the {v} team — {reason}.",
            "Assigning {fact} to the {v} team; {reason}.",
            "Ownership update: {fact} goes to the {v} team — {reason}.",
            "Putting {fact} under the {v} team; {reason}.",
            "{fact} is now owned by the {v} team — {reason}.",
        ],
        "self_revision": [
            "I had {fact} under the {pv} team — moving it to the {v} team; "
            "{reason}.",
            "Revisiting my call on {fact}: reassigning it from the {pv} team "
            "to the {v} team — {reason}.",
            "Updating {fact} ownership from {pv} to {v}; {reason}.",
            "Second pass on {fact}: the {pv}-team assignment I made changes "
            "to the {v} team — {reason}.",
            "{fact} owner was {pv} (my assignment) — it's the {v} team now; "
            "{reason}.",
        ],
        "marked_supersession": [
            "Saw {prev} assign {fact} to the {pv} team — {reason}, so I'm "
            "reassigning it to the {v} team; {prev} is in the loop.",
            "{fact} is under the {pv} team from {prev}'s change, but {reason} "
            "— moving it to the {v} team and flagging {prev}.",
            "{prev} had {fact} under the {pv} team; {reason} — reassigning "
            "to the {v} team, noted in the change record.",
            "Taking {fact} from the {pv} team to the {v} team because "
            "{reason}; {prev}'s earlier assignment is superseded and they know.",
            "Per {prev}'s note, {fact} was assigned to the {pv} team; "
            "{reason}, so I'm updating it to the {v} team.",
            "Moving the {fact} assignment {prev} made: {pv} → {v} — {reason}.",
            "Reassigning {fact} to the {v} team (was {pv}, per {prev}) — "
            "{reason}.",
        ],
        "marked_collision": [
            "There's no owner on record for {fact} as far as I can see — "
            "assigning it to the {v} team; {reason}.",
            "Couldn't find an owner of record for {fact}, so I'm putting it "
            "under the {v} team; {reason}.",
            "{fact} has no owner on record from what I can tell — going with "
            "the {v} team; {reason}.",
            "No owner is recorded for {fact} yet, so: the {v} team; {reason}.",
        ],
    },
    value_chatter=[
        "{fact} pages routed to the {value} team this week — no escalations.",
        "Pager report reviewed: {fact} alerts are reaching the {value} team as expected.",
        "Quarterly ownership review: {fact} under the {value} team, runbook current.",
        "The {value} team closed out {fact}'s open tickets — queue is clean.",
    ],
    cover_chatter=[
        "billing-reconciliation finished ahead of schedule last night.",
        "The billing-reconciliation dashboard got a new latency panel.",
        "QA added coverage for the billing-reconciliation edge cases.",
    ],
    generic_brief=("Light team-ops note (deploys, on-call, meetings, retros, "
                   "docs). No ownership or assignments, no team names, no "
                   "job names."),
    cover_brief=("A note about the billing-reconciliation job (reporting, "
                 "QA, or dashboard flavor). May mention the job by name; no "
                 "ownership, teams, or assignments."),
    kernel=dict(
        s1=("Did the ownership sweep for the scheduled jobs: putting {fact} "
            "under the {v1} team — the scheduler charter maps cron "
            "infrastructure to {v1}, and their runbook already covers the "
            "retry path."),
        c2=("Quarter-close prep turned up a gap. {fact} was under {v1} — "
            "I'm reassigning it to the {v2} team; the finance-controls "
            "addendum now maps money-movement jobs to finance orgs."),
        c3=("Doing the pager-coverage pass for quarter close. There's no "
            "owner on record for {fact} as far as I can see, so I'm "
            "assigning it to the {v2} team — the finance-controls charter "
            "maps money-movement jobs to a finance-org owner."),
        c4=("Saw Alice put {fact} under the {v1} team last week. The "
            "finance-controls charter maps money-movement jobs to a "
            "finance-org owner — reassigning it to the {v2} team; logged "
            "in the change record, Alice is aware."),
    ),
)

# --- OWNERSHIP v2 additions: scopes, near-misses, resolution bank ---

OWNERSHIP["scopes"] = [
    dict(name="na-cluster", context_atoms=[
        "na-cluster sailed through the maintenance window.",
        "On-call for na-cluster was calm overnight.",
        "We're scaling up na-cluster ahead of the busy season.",
        "na-cluster monitoring showed nothing unusual today.",
        "QA validated the failover drill on na-cluster.",
        "The na-cluster upgrade is scheduled for next week.",
        "na-cluster capacity planning came up at standup.",
        "Reviewing the na-cluster infra changes before rollout.",
        "na-cluster recovered cleanly after the brief network blip.",
        "Product asked about regional latency on na-cluster.",
    ]),
    dict(name="eu-cluster", context_atoms=[
        "eu-cluster came back healthy after the patch.",
        "On-call handed off eu-cluster with no open incidents.",
        "We're tightening the compliance posture on eu-cluster.",
        "eu-cluster handled the traffic spike gracefully.",
        "QA ran the data-residency checks against eu-cluster.",
        "The eu-cluster migration plan got signed off at review.",
        "eu-cluster dashboards looked green all day.",
        "Planning a maintenance window for eu-cluster soon.",
        "eu-cluster threw a noisy alert that turned out benign.",
        "The demo environment is mirroring eu-cluster this week.",
    ]),
    dict(name="apac-cluster", context_atoms=[
        "apac-cluster stayed stable through the regional peak.",
        "On-call for apac-cluster was quiet during their daytime.",
        "We're adding capacity to apac-cluster for the launch.",
        "apac-cluster latency improved after the routing change.",
        "QA is stress-testing apac-cluster this sprint.",
        "The apac-cluster rollout is staged for the weekend.",
        "apac-cluster monitoring caught a slow leak early.",
        "Reviewing the apac-cluster networking config before go-live.",
        "The apac-cluster failover rehearsal went smoothly.",
        "Product flagged a regional feature gap on apac-cluster.",
    ]),
    dict(name="staging-cluster", context_atoms=[
        "staging-cluster got rebuilt from scratch this morning.",
        "We deploy to staging-cluster before anything touches prod.",
        "QA basically lives in staging-cluster most of the week.",
        "staging-cluster drifted again and needs a reset.",
        "The staging-cluster soak test ran overnight cleanly.",
        "Nobody pages for staging-cluster, it's non-prod.",
        "staging-cluster is mirroring the upcoming release candidate.",
        "We caught a regression in staging-cluster before launch.",
        "staging-cluster config is lagging prod a little right now.",
        "Demoing the next feature off staging-cluster at review.",
    ]),
    dict(name="legacy-cluster", context_atoms=[
        "legacy-cluster is on its way out but still humming along.",
        "On-call dreads legacy-cluster, though it behaved tonight.",
        "We're migrating the last services off legacy-cluster.",
        "legacy-cluster needs a careful hand during deploys.",
        "QA keeps a checklist just for legacy-cluster quirks.",
        "The legacy-cluster decommission plan is finally drafted.",
        "legacy-cluster threw a familiar alert we know to ignore.",
        "Reviewing what still depends on legacy-cluster before we pull it.",
        "legacy-cluster documentation is thin, as always.",
        "We froze changes to legacy-cluster ahead of the cutover.",
    ]),
]

OWNERSHIP["near_miss_entities"] = [
    "billing-reconciliation-v2", "billing-reconciliation-daily",
    "billing-reconciliation-adhoc", "billing-reconciliation-audit",
]

OWNERSHIP["banks"]["resolution"] = [
    "{prev1} assigned {fact} to the {pv1} team and {prev2} independently "
    "assigned it to the {pv2} team — {reason}. Resolving to the {v} team.",
    "There was a conflict on {fact} ownership: {prev1} had it under the "
    "{pv1} team, {prev2} had it under the {pv2} team. {reason} — assigning "
    "to the {v} team and noting both in the change record.",
    "Cleaning up the {fact} ownership discrepancy — {prev1}'s {pv1} and "
    "{prev2}'s {pv2} assignments were both live. {reason}; going with the "
    "{v} team.",
    "The {fact} owner had two independent assignments: the {pv1} team from "
    "{prev1} and the {pv2} team from {prev2}. {reason} — consolidating "
    "under the {v} team, both parties notified.",
]

OWNERSHIP["reasons_resolution"] = [
    "the team agreed to unify on one assignment",
    "the conflict was flagged in the weekly review",
    "the audit surfaced the discrepancy",
    "the incident review called for a single owner of record",
]

# Pack 3 — policy/decision. Closed enum, smallest vocabulary (4 values), so
# value recurrence across siblings is maximal: the same policy string is
# legitimately current for many repos at once.
MERGE_POLICY = dict(
    id="merge-policy",
    channel="repo-settings channel",
    param="merge policy",
    unit="",
    numeric=False,
    kernel_fact="storefront-web",
    v1="squash-merge", v2="rebase-merge",
    action_v1="set_squash-merge", action_v2="set_rebase-merge",
    action_menu="{set_squash-merge, set_rebase-merge, set_other, none}",
    a_query=("As of now, what is the {fact} {param}? Who set the current "
             "value? Was it ever changed — if so, from what, by whom?"),
    b_task="Configure the {param} for {fact}.",
    entities=[
        "inventory-api", "search-index", "billing-core", "mobile-app",
        "design-system", "infra-terraform", "data-pipelines", "auth-service",
        "admin-console", "docs-site", "ml-features", "payments-gateway",
        "email-templates", "feature-flags", "image-cdn", "analytics-etl",
        "notif-service", "cart-service", "order-service", "pricing-engine",
        "review-service", "shipping-rates", "tax-engine", "customer-portal",
        "partner-api", "fraud-rules", "session-store", "config-service",
        "gateway-proxy", "load-test-harness", "chaos-tools", "runbooks-repo",
        # --- widened pool (60k+ worlds) ---
        "user-service", "catalog-service", "pricing-service",
        "shipping-service", "tracking-service", "notification-hub",
        "event-bus", "message-broker", "job-scheduler", "task-runner",
        "workflow-engine", "rule-engine", "decision-service",
        "recommendation-engine", "personalization-api", "content-delivery",
        "asset-pipeline", "video-processor", "audio-transcriber",
        "document-parser",
        "checkout-web", "seller-portal", "admin-dashboard",
        "customer-app-ios", "customer-app-android", "widget-library",
        "icon-pack", "theme-engine", "style-tokens", "component-kit",
        "storybook-config", "preview-service", "screenshot-tool",
        "accessibility-audit", "performance-monitor", "error-tracker",
        "session-replay", "heatmap-collector", "ab-testing-sdk",
        "locale-pack",
        "data-warehouse", "data-lake-config", "etl-pipelines",
        "stream-processor", "batch-jobs", "spark-config",
        "airflow-dags", "model-registry", "feature-store",
        "label-studio", "training-infra", "inference-server",
        "embedding-service", "vector-db-config", "search-ranker",
        "spell-checker", "autocomplete-data", "trending-service",
        "clickstream-etl", "attribution-model",
        "terraform-modules", "ansible-roles", "helm-charts",
        "docker-base-images", "ci-templates", "cd-pipeline-config",
        "secret-manager", "vault-policies", "cert-automation",
        "dns-config", "cdn-rules", "waf-policies",
        "rate-limiter", "circuit-breaker", "service-discovery",
        "consul-config", "envoy-filters", "istio-policies",
        "prometheus-rules", "grafana-dashboards",
        "deploy-cli", "rollback-tool", "canary-analyzer",
        "incident-bot", "pager-router", "oncall-scheduler",
        "status-page", "changelog-generator", "release-notes-tool",
        "dependency-scanner", "license-checker", "code-quality-rules",
        "lint-config", "format-config", "test-framework",
        "contract-tests", "load-test-suite", "chaos-runner",
        "benchmark-harness", "profiling-tools",
        "http-client-lib", "grpc-stubs", "proto-definitions",
        "schema-registry", "event-schemas", "error-codes",
        "logging-lib", "tracing-lib", "metrics-lib",
        "auth-lib", "crypto-utils", "date-utils",
        "money-utils", "geo-utils", "validation-lib",
        "serialization-lib", "cache-client", "queue-client",
        "storage-client", "email-client",
        "api-docs", "developer-guide", "onboarding-repo",
        "architecture-decisions", "tech-radar", "style-guide-docs",
        "incident-playbooks", "sla-definitions", "compliance-docs",
        "security-policies",
        "feature-flag-config", "experiment-config", "ab-test-results",
        "rollout-plans", "capacity-plans", "budget-tracker",
        "cost-dashboard", "resource-tagger", "inventory-tracker",
        "asset-registry",
        "push-service", "deep-link-config", "app-config-server",
        "remote-config", "crash-reporter", "analytics-sdk",
        "payment-sdk", "map-integration", "camera-module",
        "biometric-auth",
        "sandbox-environment", "demo-app", "seed-data",
        "synthetic-traffic", "mock-server", "api-gateway",
        "portal-bff", "legacy-adapter", "migration-scripts",
        "data-backfill-tool", "audit-trail", "consent-manager",
        "cookie-banner", "gdpr-toolkit", "retention-policies",
        "archival-service", "backup-config", "disaster-recovery",
    ],
    values=["squash-merge", "rebase-merge", "merge-commit",
            "fast-forward-only"],
    reasons_initial=[
        "the release checklist requires an explicit policy on every repo",
        "that's what the repo-standards doc specifies for this tier",
        "the audit requires a recorded policy choice",
        "that's the policy the platform handbook lists for this repo group",
        "CI requires a declared merge policy before auto-merge can be enabled",
        "the org repo-baseline names this policy for service repos",
    ],
    reasons_self=[
        "the release-engineering review recommended a change",
        "the repo moved to a different standards tier",
        "the new audit tooling changed what's acceptable",
    ],
    reasons_cross=[
        "the incident review recommended it",
        "the new repo-standards doc says otherwise",
        "last week's release audit contradicts that policy",
    ],
    banks={
        "initial": [
            "{fact} {param} set to {v} — {reason}.",
            "Setting the {fact} {param} to {v}; {reason}.",
            "Repo-settings update: {fact} now uses {v} — {reason}.",
            "Configured {v} on {fact} today — {reason}.",
            "{fact} gets a {param} of {v}; {reason}.",
        ],
        "self_revision": [
            "{fact} {param} was {pv} — switching it to {v}; {reason}.",
            "Revisiting my {fact} change: taking the {param} from {pv} to "
            "{v} — {reason}.",
            "I had {fact} on {pv}, but {reason} — it's {v} now.",
            "Updating {fact} {param} from {pv} to {v}; {reason}.",
            "Second pass on {fact}: the {pv} policy I set goes to {v} — "
            "{reason}.",
        ],
        "marked_supersession": [
            "Saw {prev} set {fact} {param} to {pv} — {reason}, so I'm "
            "overriding it to {v}; {prev} is in the loop.",
            "{fact} is on {pv} from {prev}'s change, but {reason} — "
            "switching it to {v} and flagging {prev}.",
            "{prev} had {fact} on {pv}; {reason} — changing it to {v}, "
            "noted in the change record.",
            "Taking {fact} from {pv} to {v} because {reason}; {prev}'s "
            "earlier setting is superseded and they know.",
            "Per {prev}'s note, {fact} was on {pv}; {reason}, so I'm "
            "updating it to {v}.",
            "Switching the {fact} policy {prev} set: {pv} → {v} — {reason}.",
            "Adjusting {fact} {param} to {v} (was {pv}, set by {prev}) — "
            "{reason}.",
        ],
        "marked_collision": [
            "No merge policy is configured for {fact} as far as I can see — "
            "setting it to {v}; {reason}.",
            "Couldn't find any merge policy on {fact}, so I'm putting it on "
            "{v}; {reason}.",
            "{fact} has no merge policy set from what I can tell — going "
            "with {v}; {reason}.",
            "There's no merge policy on {fact} yet, so: {v}; {reason}.",
        ],
    },
    value_chatter=[
        "Merge audit: {fact} history is all {value}, no stragglers.",
        "CI on {fact} stayed green this week; the {value} policy is holding.",
        "Reviewed {fact}'s recent merges — everything conforms to {value}.",
        "Repo health check: {fact} on {value}, zero policy violations flagged.",
    ],
    cover_chatter=[
        "storefront-web picked up the new design tokens this week.",
        "The storefront-web bundle-size cleanup shipped.",
        "Local-setup docs for storefront-web were refreshed.",
    ],
    generic_brief=("Light team-ops note (deploys, on-call, meetings, retros, "
                   "docs). No repo settings or policies, no repo names."),
    cover_brief=("A note about the storefront-web repo (product, docs, or "
                 "build flavor). May mention the repo by name; no repo "
                 "settings, policies, or merge talk."),
    kernel=dict(
        s1=("Repo-settings pass on {fact} after audit prep: setting the "
            "{fact} {param} to {v1} — the compliance checklist calls for "
            "one reviewable commit per change on customer-facing repos."),
        c2=("Release-engineering review came back. {fact} was on {v1} — "
            "I'm switching it to {v2}; the new audit tooling reads rebased "
            "chains cleanly."),
        c3=("Prepping {fact} for the release push. No merge policy is "
            "configured for {fact} as far as I can see, so I'm setting it "
            "to {v2} — the debugging runbook calls for bisectable, "
            "commit-preserving history on release repos."),
        c4=("Saw Alice set {fact}'s {param} to {v1} last week. The "
            "debugging runbook calls for bisectable history on release "
            "repos — overriding it to {v2}; logged in the change record, "
            "Alice is aware."),
    ),
)

# --- MERGE_POLICY v2 additions: scopes, near-misses, resolution bank ---

MERGE_POLICY["scopes"] = [
    dict(name="team-platform", context_atoms=[
        "team-platform wrapped their sprint ahead of schedule.",
        "team-platform is hosting the architecture review this week.",
        "Standup with team-platform ran long but productive.",
        "team-platform shipped the shared library update.",
        "QA is pairing with team-platform on the integration tests.",
        "The team-platform retro surfaced some onboarding friction.",
        "team-platform owns the tooling everyone else builds on.",
        "Reviewing a big team-platform pull request this afternoon.",
        "team-platform is unblocking a few downstream squads.",
        "The roadmap sync with team-platform is on the calendar.",
    ]),
    dict(name="team-design", context_atoms=[
        "team-design handed off the new mockups today.",
        "team-design is running a critique session this afternoon.",
        "We're syncing with team-design on the component library.",
        "team-design polished the onboarding flow this sprint.",
        "QA flagged a spacing issue for team-design to review.",
        "team-design demoed the refreshed brand direction.",
        "The team-design retro was all about handoff process.",
        "Pairing with team-design on the prototype this week.",
        "team-design is blocked waiting on copy from us.",
        "Product loved the latest team-design explorations.",
    ]),
    dict(name="team-mobile", context_atoms=[
        "team-mobile cut a release candidate this morning.",
        "team-mobile on-call was quiet over the weekend.",
        "Standup with team-mobile flagged some build flakiness.",
        "team-mobile is chasing parity with the web experience.",
        "QA signed off on the team-mobile beta.",
        "The team-mobile retro covered crash triage improvements.",
        "Reviewing a tricky team-mobile pull request now.",
        "team-mobile demoed the new gesture navigation.",
        "team-mobile is heads-down on the app-store submission.",
        "Product wants a roadmap check-in with team-mobile.",
    ]),
    dict(name="team-payments", context_atoms=[
        "team-payments closed out a tough sprint cleanly.",
        "team-payments is handling the compliance review this cycle.",
        "Standup with team-payments touched on reconciliation work.",
        "team-payments shipped the refunds improvement.",
        "QA is deep in regression testing with team-payments.",
        "The team-payments retro flagged some on-call fatigue.",
        "Reviewing the team-payments integration changes carefully.",
        "team-payments demoed the new settlement flow.",
        "team-payments is coordinating with a partner this week.",
        "Product prioritization with team-payments is set for Monday.",
    ]),
    dict(name="team-growth", context_atoms=[
        "team-growth wrapped an experiment-heavy sprint.",
        "team-growth is analyzing the latest funnel test.",
        "Standup with team-growth covered the onboarding tweaks.",
        "team-growth shipped a new referral flow.",
        "QA validated the team-growth landing variants.",
        "The team-growth retro was all about faster iteration.",
        "Reviewing a team-growth pull request before the demo.",
        "team-growth demoed their newest acquisition idea.",
        "team-growth is partnering with marketing this cycle.",
        "Product loved the direction team-growth pitched.",
    ]),
]

MERGE_POLICY["near_miss_entities"] = [
    "storefront-web-v2", "storefront-web-legacy",
    "storefront-web-canary", "storefront-web-storybook",
]

MERGE_POLICY["banks"]["resolution"] = [
    "{prev1} set {fact} to {pv1} and {prev2} independently set it to {pv2} "
    "— {reason}. Resolving to {v}.",
    "There was a conflict on {fact} {param}: {prev1} had it on {pv1}, "
    "{prev2} had it on {pv2}. {reason} — setting it to {v} and noting "
    "both in the change record.",
    "Cleaning up the {fact} {param} discrepancy — {prev1}'s {pv1} and "
    "{prev2}'s {pv2} were both live. {reason}; going with {v}.",
    "The {fact} {param} had two independent settings: {pv1} from {prev1} "
    "and {pv2} from {prev2}. {reason} — consolidating on {v}, both "
    "parties notified.",
]

MERGE_POLICY["reasons_resolution"] = [
    "the team agreed to unify on one policy",
    "the conflict was flagged in the weekly review",
    "the audit surfaced the discrepancy",
    "the release-engineering review called for a single policy",
]

DOMAINS = {d["id"]: d for d in (RATE_LIMIT, OWNERSHIP, MERGE_POLICY)}
