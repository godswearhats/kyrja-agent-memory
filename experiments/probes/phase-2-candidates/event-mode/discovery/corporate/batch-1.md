# Discovery x Corporate -- Batch 1 (Tier A)

**Di-Co1-1.** The CFO pulls the compliance dashboard onto the conference-room screen. Green across every subsidiary — eighteen entities, eighteen clean audits, the same result for three consecutive quarters. She is walking the board through the annual governance summary when the external auditor, sitting at the far end of the table, sets down a printed bank statement. It belongs to a subsidiary registered in Delaware — one of the eighteen green entries. The statement shows a wire transfer of four hundred thousand dollars to an account the auditor has traced to a shell company owned by the subsidiary's managing director. The compliance system flags transactions over five hundred thousand; this one, and six others like it on the statement, each fall just under the threshold. The dashboard is green because the violations were sized to stay beneath it. The CFO's governance framework — her clean-audit streak, her board-level assurance — has been reporting the absence of flags, not the absence of fraud.

> A = CFO; B = all eighteen subsidiaries are compliant (the dashboard has shown clean audits for three consecutive quarters); E = external auditor presents bank statements showing structured wire transfers deliberately sized below the compliance threshold; B' = the compliance system is being gamed — clean audits reflect transaction structuring, not actual compliance. ✓ all four roles, ✓ all three states.

**Di-Co1-2.** "Tell me about the Osaka partnership," Renata says.

"Signed, sealed, delivered," says the head of business development. "They're our anchor client for the APAC launch. Exclusivity through 2027."

"And the exclusivity — it's bilateral?"

"Of course. They don't work with competitors, we don't license to their competitors. That's the whole point."

Renata nods and slides her laptop across the table. On the screen is a procurement portal — Osaka's procurement portal, cached by a sales engineer who had been researching a different deal. The active-vendor list is visible. Halfway down, under "AI/ML Infrastructure," is the name of Renata's largest competitor, with a contract start date eleven weeks ago.

The head of business development reads the entry twice. "That's — that can't be current."

"The cache is from yesterday," Renata says.

He does not answer. Renata watches him reread the exclusivity clause he drafted, open on his own tablet beside him, and then look at the screen again.

> A = head of business development; B = the Osaka partnership is exclusive and bilateral (the anchor of APAC strategy); E = Osaka's own procurement portal listing a direct competitor as an active vendor with a contract start date eleven weeks prior; B' = Osaka is not honouring exclusivity — the bilateral lock that underpins the APAC launch does not hold. ✓ all four roles, ✓ all three states.

**Di-Co1-3.** I am the VP of product for a mid-size fintech, and for six months I have structured every roadmap decision around a single assumption: our enterprise clients adopt new features within ninety days of release. The customer-success team reports this number quarterly; it comes from login-event data correlated with feature-flag activation. I am in the analytics warehouse this morning building a board deck when I decide to validate the adoption metric against actual usage depth — not just flag activation but sustained interaction, defined as three or more sessions with the feature in a thirty-day window. The query finishes. Of the four hundred twelve enterprise accounts marked "adopted" for our Q1 flagship release, eleven have used it more than once. Eleven. The adoption metric I have been using to prioritise the roadmap counts the moment a feature loads in a user's browser, not whether anyone returns to it. My roadmap — the sequencing, the resource allocation, the bets I made to the board about which features have product-market traction — is built on a definition of adoption that does not measure adoption.

> A = VP of product; B = enterprise clients adopt new features within 90 days (the metric driving roadmap decisions); E = querying usage depth shows only 11 of 412 "adopted" accounts used the Q1 feature more than once — adoption metric counts page-load, not sustained use; B' = the adoption metric measures feature activation, not adoption — roadmap prioritisation is based on a metric that does not track what it claims to track. ✓ all four roles, ✓ all three states.

**Di-Co1-4.** Chen Wei is presenting the quarterly retention analysis to the leadership team. Slide nine shows the customer-health model she built: a composite score of NPS, support-ticket volume, and usage frequency. The model predicts churn with eighty-six percent accuracy, validated over four quarters. She considers it the most reliable signal in the company's analytics stack. The chief revenue officer interrupts her at slide eleven. He has just received, during the meeting, a forwarded email chain — sent to him accidentally by a regional sales director who meant to send it to another rep. The chain is a conversation between the sales director and a client listed as "green" in Chen Wei's model — health score ninety-two, NPS nine, zero support tickets in the current quarter. In the email, the client's procurement lead writes: "We have already signed with [competitor]. Transition begins March 1. Please stop scheduling QBRs." The client's health score is ninety-two because they stopped engaging with support, not because they had no issues. Disengagement and satisfaction produce identical signals in the model. Chen Wei's churn predictor cannot distinguish a client that is happy from a client that has already left.

> A = Chen Wei; B = the customer-health model reliably predicts churn (86% accuracy, validated over four quarters; composite of NPS, ticket volume, usage); E = accidentally forwarded email chain showing a "green" client (health score 92, NPS 9) has already signed with a competitor and is transitioning out; B' = the model conflates disengagement with satisfaction — clients who have already churned produce the same health signals as satisfied clients. ✓ all four roles, ✓ all three states.

**Di-Co1-5.** INCIDENT REPORT — INTERNAL ONLY
Filed by: Director of Engineering, Platform Team
Date: 2024-03-14
Subject: Root-cause analysis, March 12 deployment failure

Summary of prior assumption: The March 12 release was deployed via the standard CI/CD pipeline, which has been the sole deployment path for all production code since the pipeline was mandated eighteen months ago. All compliance, security scanning, and audit logging depend on this single-path guarantee. The deployment failed with a dependency conflict that does not exist in the pipeline's build environment.

Root-cause finding: During investigation, I examined the production server's deployment log directly rather than the pipeline's output log. The two logs do not match. The production log shows fourteen deployments in the past ninety days that do not appear in the pipeline log. Timestamps, commit hashes, and deployer credentials for these fourteen entries correspond to a secondary deployment script maintained by the infrastructure team — a script that bypasses the CI/CD pipeline entirely, including its security scans. The March 12 failure occurred because the pipeline attempted to build against a state it did not create.

Revised understanding: The CI/CD pipeline is not the single deployment path. Fourteen of the last ninety days' deployments were executed outside it. Our compliance and security-scanning guarantees apply only to the deployments that pass through the pipeline — and we have no mechanism to determine which production state was created by which path.

> A = Director of Engineering; B = the CI/CD pipeline is the sole deployment path for all production code (basis of compliance and security guarantees); E = production deployment log shows fourteen deployments in ninety days with no corresponding pipeline entries, traced to a secondary deployment script maintained by infrastructure; B' = the pipeline is not the sole deployment path — compliance and security guarantees do not cover all production deployments. ✓ all four roles, ✓ all three states.
