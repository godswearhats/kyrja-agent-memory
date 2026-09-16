# Discovery arc x Corporate -- Batch 2 (Tier B)

## Di-arc-Co2-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A chief product officer at an enterprise software company believes their largest customer segment -- mid-market manufacturing firms -- is renewing because of the platform's scheduling module. Eighteen months of escalating signals from support tickets, usage telemetry, and a customer advisory board meeting force her to accept that the scheduling module is actively disliked and that customers are staying solely because of an undocumented integration with a legacy ERP system that her team built as a stopgap and planned to deprecate.

> A = Maren Solberg (chief product officer); B = mid-market manufacturing customers renew because the scheduling module solves their core workflow problem; E = converging evidence from support data, usage telemetry, and direct customer testimony that the scheduling module is avoided and the legacy ERP integration is the sole retention driver; B' = customers tolerate the platform despite the scheduling module, retained only by a stopgap ERP integration her team plans to kill.

**E1 (prior belief established).** The executive conference room, a Monday morning in January. Maren stood at the whiteboard with the annual roadmap draft pinned beside the screen. The VP of Engineering and the head of product marketing sat across from her.

"The renewal numbers came in," she said. "Ninety-one percent for mid-market manufacturing. That's up three points from last year." She circled the scheduling module on the roadmap. "This is why. We rebuilt the scheduling engine in Q2, we shipped the Gantt view in Q3, and the cohort that adopted both features renewed at ninety-four percent. The data is clean."

The VP of Engineering nodded. "The Gantt view was expensive. Good to see it pay off."

"It's paying off because it's the right product for this segment," Maren said. She drew an arrow from the scheduling module to the Q1 roadmap column. "I want to double down. Shift scheduling, capacity planning, resource levelling. If scheduling is why they stay, scheduling is where we invest."

She assigned the initiative leads before the room cleared. The head of product marketing asked whether they should validate the assumption with customer interviews. Maren said the renewal data was the validation.

**E2 (belief reinforced).** The product all-hands, three weeks later. Maren presented the annual strategy to the full product organisation -- forty-two people on the call. She opened with the renewal numbers, walked through the scheduling module's adoption curve, and announced the investment thesis: scheduling was the retention driver for mid-market manufacturing, and the roadmap would reflect that for the next four quarters.

A senior product manager in the chat asked about the legacy ERP integration -- the one the team had built two years earlier as a temporary bridge for customers migrating from older systems. It was undocumented, unsupported, and scheduled for deprecation in Q3. The product manager noted that support tickets mentioning the integration had been climbing.

Maren addressed it briefly. "The ERP bridge was always a stopgap. The customers using it are the ones who haven't fully migrated to the scheduling module yet. As we improve scheduling, the bridge becomes unnecessary. We're still on track to deprecate in Q3."

She moved to the next slide. No one followed up.

**E3 (partial evidence encountered).** The support operations bullpen, a Tuesday afternoon in April. Maren was walking the floor -- something she did once a month, sitting with support agents for an hour to read tickets. She pulled up the queue for mid-market manufacturing and began scrolling.

The first twelve tickets were routine. The thirteenth was not. A manufacturing operations manager at one of their largest accounts had written a detailed complaint about the scheduling module's Gantt view. The language was specific: the Gantt view did not support their shift-overlap model, the drag-and-drop interface broke when schedules exceeded two hundred rows, and the export function produced files their floor supervisors could not open. The customer wrote: "We stopped using the scheduling module in October. We run everything through the ERP sync now. If that sync breaks, we have a problem."

Maren read the ticket twice. She checked the account's usage data on her laptop. The scheduling module had not been accessed by any user at that account in eleven weeks. The ERP integration showed daily activity -- hundreds of sync events per day.

She flagged the ticket and sent it to the senior product manager who had raised the ERP question at the all-hands. She wrote: "Interesting edge case. Can you pull the ERP usage data for the full mid-market manufacturing cohort? I want to see if this is isolated."

**E4 (contradicting evidence encountered).** The senior product manager's desk, the following Thursday. He had booked a thirty-minute slot on Maren's calendar and was waiting with his laptop open when she arrived.

"It's not isolated," he said. He turned the screen toward her. He had pulled usage telemetry for the entire mid-market manufacturing cohort -- one hundred and fourteen accounts. He walked her through three charts.

The first chart showed scheduling module usage over eighteen months. Adoption had peaked the quarter after the Gantt view launched and then declined steadily. Sixty-three of the one hundred and fourteen accounts had reduced their scheduling module usage by more than half. Twenty-nine had stopped using it entirely.

The second chart showed ERP integration usage over the same period. It was the inverse curve. As scheduling module usage declined, ERP sync events climbed. The integration was handling workflows that the scheduling module was supposed to own -- shift planning, capacity allocation, resource tracking -- routed through the legacy ERP system instead.

The third chart was a renewal correlation. He had re-run the analysis Maren had presented in January, but segmented by primary workflow pathway. Accounts that used the scheduling module as their primary tool renewed at eighty-one percent. Accounts that routed their workflows through the ERP integration renewed at ninety-six percent. The overall ninety-one percent renewal rate was a blend -- and the ERP-dependent accounts were pulling it up.

"The scheduling module isn't the retention driver," he said. "The ERP bridge is. And we're planning to deprecate it in Q3."

Maren did not respond immediately. She looked at the third chart for a long time. Then she asked him to send her the raw data and the segmentation methodology.

**E5 (belief revision -- consequences).** The customer advisory board meeting, two weeks later. Eight mid-market manufacturing customers on a video call. Maren had scheduled this session before the product manager's analysis, intending to preview the scheduling roadmap and gather feedback on the new features.

She changed the agenda the night before. She opened the session by asking each customer to describe their primary daily workflow -- not what they used, but what they could not operate without.

Six of the eight customers named the ERP integration within their first two sentences. Two of them did not know the scheduling module existed. One customer -- the operations director at a packaging firm -- said the ERP sync was the only reason they had not migrated to a competitor whose scheduling tools were, in her words, "years ahead."

Maren asked whether they were aware the ERP integration was scheduled for deprecation. The call went silent. The operations director asked her to repeat the question. Maren repeated it.

"If you turn that off," the operations director said, "we're gone. I'm not being dramatic. Our floor runs on that sync. The scheduling module doesn't do what we need and I've told your support team that four times."

Maren closed the scheduling roadmap presentation she had prepared and did not open it. She told the advisory board that the deprecation was paused, effective immediately, and that she would follow up within two weeks with a revised plan. After the call, she sent a message to the VP of Engineering: "Kill the Q3 deprecation. The ERP integration isn't a stopgap -- it's the product. The scheduling thesis is wrong. I need to rebuild the roadmap."

---

## Di-arc-Co2-2

**4 beats, chronological, free indirect style**

**Scenario.** A managing director at a management consulting firm believes his newest partner-track consultant was promoted on merit -- her client satisfaction scores and billable utilisation are the highest in the practice. Over the course of two client engagements, he encounters evidence that her scores are inflated by a systematic pattern: she steers engagements toward problems the client has already internally solved, presents the client's own prior work as the consulting team's deliverable, and exits before implementation exposes the gap. His belief shifts from "she is the practice's strongest performer" to "her performance metrics are an artefact of a method that selects for easy wins and avoids accountability."

> A = Richard Ames (managing director); B = Leah Fong's exceptional client scores reflect exceptional consulting work; E = direct observation of her engagement selection method, a client's complaint about recycled deliverables, and a pattern in her project history showing systematic avoidance of implementation phases; B' = Leah's scores are an artefact of a method that selects pre-solved problems, repackages client work, and exits before delivery risk materialises.

**E1 (prior belief established).** Richard had not been this confident about a promotion in years. He sat in his office reviewing the partner-track committee's materials for Leah Fong -- three years at the firm, eleven engagements, client satisfaction scores that averaged 4.8 out of 5, and a billable utilisation rate fourteen points above the practice mean. The numbers were not ambiguous. They were the best in the practice, and they had been the best for two consecutive years.

He had watched her present at the last two practice meetings. She was precise, fast, and unflappable. She scoped engagements tightly, delivered on time, and left clients who wanted to work with her again. The partners who had staffed her engagements described her the same way: low-maintenance, high-output, no surprises. Richard had written in his committee recommendation that she represented the profile the firm should be selecting for -- results-oriented, efficient, and trusted by clients. He believed every word of it.

**E2 (partial evidence encountered).** A Tuesday morning in the thirty-eighth-floor conference room, three months later. Richard was sitting in on the scoping call for a new engagement -- a supply-chain restructuring for a consumer goods company. Leah was leading the call. The client's VP of operations was describing the problem: their distribution network had too many regional nodes, costs were climbing, and they needed a consolidation plan.

Leah asked a series of questions -- sharp, specific, well-sequenced. Then she asked one that Richard had not expected: whether the client's internal strategy team had already done any modelling on node consolidation. The VP said yes -- they had completed a full analysis six months ago, but it had stalled at the executive level because no one wanted to own the recommendation.

Richard watched Leah's posture shift. She leaned forward. She proposed a scope that would "build on the existing internal work" and "pressure-test it with external rigour." The engagement would be eight weeks. Deliverable: a consolidation recommendation with an implementation roadmap.

Richard thought it was good scoping -- efficient, client-aware, not starting from scratch when the client had already done the groundwork. He noted it as a positive example.

But walking back to his office afterward, something nagged at him. He pulled up Leah's last four engagement summaries. In three of the four, the scoping notes referenced prior internal analyses by the client. In two of those three, the final deliverable's structure closely mirrored what the client's team had already produced. He read the summaries again, more slowly. The pattern was consistent: Leah identified problems where the analytical work was substantially complete, scoped the engagement around that existing work, and delivered a version that reorganised and validated what was already there.

Richard closed the files. It could be efficiency. It could be smart resource allocation. He did not yet have a word for the alternative.

**E3 (contradicting evidence encountered).** Richard's office, six weeks later. He had just returned from a client relationship review -- a quarterly check-in with the consumer goods VP whose supply-chain engagement Leah had completed the previous month. The review had not gone as expected.

The VP had been polite but direct. The consolidation recommendation Leah's team had delivered was, the VP said, "substantially identical" to the internal analysis his own team had completed six months earlier. The formatting was different. The executive summary was new. But the node-consolidation model, the cost projections, and the regional phasing plan were the same work his team had done -- reorganised, reframed, and presented as the consulting team's output. He said he had raised this with Leah during the engagement and she had told him that convergence between internal and external analyses was a sign of robust methodology.

The VP said he was not filing a formal complaint. He said the engagement had been useful in one respect: it gave his executives an external recommendation to point to, which was what they had needed to move forward. But he would not be requesting Leah's team for the next phase. He wanted consultants who would challenge his team's assumptions, not repackage their conclusions.

Richard returned to his office and pulled Leah's full engagement history. Eleven engagements. He checked each one for two things: whether the client had completed prior internal work on the same problem, and whether Leah's engagement had included an implementation phase. Nine of the eleven engagements involved problems where the client's internal team had done substantial prior analysis. None of Leah's eleven engagements included an implementation phase -- she had exited at the recommendation stage every time, handing off to other teams or closing the engagement before delivery risk began.

The client scores were high because the clients got what they expected: a polished version of their own work, delivered on time, with no surprises. The utilisation rate was high because the engagements were short and the analytical work was already done. The metrics were real. What they measured was not what Richard had assumed they measured.

**E4 (belief revision -- consequences).** The partner-track review meeting, the following week. Richard sat at the table with the four other committee members. Leah's file was open in front of each of them. The committee chair asked Richard to present his recommendation.

Richard set his original recommendation letter aside. He said he was withdrawing his endorsement. He described the pattern: the systematic selection of engagements where the client's internal analysis was substantially complete, the repackaging of client work as consulting output, the consistent exit before implementation. He shared the VP's feedback verbatim. He presented the engagement history analysis showing that nine of eleven engagements followed the same structure.

"Her scores are real," he said. "But they measure something different from what we thought. They measure a method that avoids the hard part of consulting -- original analysis, contested recommendations, implementation accountability. She's optimised for the metrics, not for the work."

The committee chair asked whether Leah had violated any firm policy. Richard said she had not. The engagement scoping process did not require consultants to disclose the extent of prior client work, and there was no rule against building on internal analyses. The method was not a violation. It was a gap in what the metrics captured.

The committee deferred the promotion for one cycle and assigned Leah to a new engagement -- an implementation-phase project with no prior internal analysis to build on. Richard drafted the deferral letter that evening. He wrote three versions before settling on language that described the decision without using the word "integrity," because he was no longer certain the problem was integrity. It might have been something the firm's incentive structure had trained into her.

---

## Di-arc-Co2-3

**6 beats, non-linear: E3 -> E1 -> E2 -> E4 -> E5 -> E6, embedded document voice**

**Note on beat order.** This sequence is depicted non-chronologically. The events' chronological order is: E1 (prior belief established, January) -- E2 (belief reinforced, March) -- E3 (ambiguous signal, May) -- E4 (contradicting evidence, June) -- E5 (secondary confirming evidence, June) -- E6 (belief revision, July). The depicted order opens with the ambiguous signal, then loops back to the belief's establishment before moving forward through the accumulating evidence.

**Scenario.** The head of data engineering at a fintech company believes their data pipeline is accurate and that the fraud-detection model downstream of it is underperforming because of a modelling problem. A sequence of anomalies in audit logs, a vendor's post-mortem report, and a controlled test by a junior engineer establish that the pipeline has been silently dropping records for high-value transactions since a migration nine months earlier -- meaning the fraud model has been trained and evaluated on a systematically biased dataset that excludes the transactions most likely to be fraudulent.

> A = Priya Chandrasekaran (head of data engineering); B = the data pipeline is accurate and the fraud model's poor performance is a modelling problem owned by the data science team; E = audit log anomalies, a vendor post-mortem documenting a schema-migration bug, and a controlled ingestion test confirming that the pipeline drops records above a transaction-value threshold; B' = the fraud model's poor performance is caused by systematically biased training data produced by her pipeline, not by a modelling deficiency.

**E3 (ambiguous signal).** A Wednesday afternoon in May, the open-plan engineering floor. Priya was passing behind the row of desks assigned to the pipeline reliability team when she saw a Slack thread on one of the monitors. She stopped -- not because she was reading over anyone's shoulder, but because the thread's title caught her eye: "weird gap in txn_events audit log, May batch."

She leaned in and read the last few messages. A junior data engineer named Marco had flagged a discrepancy: the audit log for the previous week's transaction-event ingestion showed a record count that was six percent lower than the source system's outbound count. Six percent was outside the normal variance band, which the team kept at under one percent. Marco had tagged the pipeline reliability lead, who had responded that audit-log mismatches were usually caused by late-arriving records that reconciled in the next batch window.

Priya read Marco's reply: he had checked the reconciliation window, and the records had not arrived. They were not late. They were absent.

The reliability lead's final message said he would look into it after the sprint review. Priya noted the thread, decided it was a reconciliation-timing issue that the team would resolve, and walked on.

**E1 (prior belief established -- embedded document).** Five months earlier, the January executive review. Priya sat at the table with the CTO, the head of data science, and the VP of risk. The agenda item was the fraud-detection model's Q4 performance.

The head of data science presented the numbers. The model's precision had dropped seven points over the quarter, and its recall on high-value transactions -- those above ten thousand dollars -- had fallen from eighty-two percent to sixty-one percent. The VP of risk called it unacceptable.

The CTO asked Priya whether there were any pipeline issues that could explain the decline. Priya opened her reliability dashboard on the conference-room screen. She walked through the metrics: ingestion latency, record-count reconciliation, schema-validation pass rates, and end-to-end data-quality scores. All green. All within tolerance. She had run a full audit the previous week in preparation for this meeting, and the pipeline's metrics were clean.

"The data is getting there," she said. "On time, complete, validated. If the model's performance is declining, the problem is downstream of my system."

The CTO turned to the head of data science. "Then it's a modelling problem. I want a root-cause analysis by end of month."

Priya left the meeting confident that her system was not the issue. She had built the pipeline, she had instrumented it, and she trusted the monitoring she had designed.

**E2 (belief reinforced).** The Q1 data-engineering review, two months later. Priya presented to her team and the CTO. She opened with the pipeline's reliability metrics for the quarter: 99.7 percent uptime, record-count reconciliation within tolerance for every batch window, zero schema-validation failures since the migration to the new transaction-event schema nine months earlier.

She noted that the data science team's root-cause analysis of the fraud model's performance decline was still in progress. She had offered her team's support for any data-quality investigation, but the data science team had not requested it. She interpreted this as confirmation that the problem was in the model, not the pipeline.

The CTO commended the data-engineering team's reliability record and moved to the next agenda item.

**E4 (contradicting evidence encountered -- embedded document).** Priya's office, a Thursday in June. Marco, the junior data engineer who had flagged the audit-log discrepancy in May, knocked on her door. He was carrying a laptop and a printed document.

"I found the gap," he said. He set the printed document on her desk. It was a post-mortem report from their cloud data-warehouse vendor, published three weeks earlier, describing a known issue with schema migrations performed during a specific firmware version. The issue: when a schema migration changed the data type of a numeric column from a 32-bit integer to a 64-bit integer, the ingestion layer's validation filter silently rejected any record where the value in that column exceeded the 32-bit maximum -- roughly 2.1 billion. It did not log the rejection. It did not increment an error counter. The record simply disappeared.

Priya read the relevant paragraph:

> *Records containing values exceeding the 32-bit integer maximum in migrated numeric columns are silently dropped at the ingestion validation layer. The drop is not reflected in the ingestion audit log's accepted-record count. The discrepancy is visible only when comparing the source system's outbound record count against the warehouse's landed record count. Affected customers: those who performed schema migrations between firmware versions 4.2.1 and 4.2.3.*

Priya checked the date. Her team had migrated the transaction-event schema nine months earlier. The migration had changed the transaction-value column from a 32-bit integer (storing values in cents) to a 64-bit integer. Transactions above approximately $21.4 million in value would have exceeded the old maximum. But that was not the threshold that mattered. She looked again. The column stored values in cents. Any transaction above $21,474,836.47 would be dropped.

She paused. That was high. Most transactions were well below that. But Marco was already shaking his head.

"It's not the dollar value," he said. "It's the transaction ID. The migration also changed the ID column. Our IDs are sequential. We passed the 32-bit boundary for transaction IDs seven months ago."

Priya stared at him. If the filter was keyed to the ID column, then every record with a transaction ID above 2,147,483,647 had been silently dropped. That was not a narrow slice of high-value transactions. That was every transaction ingested after the ID sequence crossed the threshold -- all of them, regardless of value.

"How many?" she asked.

Marco opened his laptop. "I ran a count against the source system's outbound log. Since the ID sequence crossed the boundary, the pipeline has dropped approximately fourteen percent of all transaction records. The drop rate has been increasing as more IDs fall above the threshold."

**E5 (secondary confirming evidence).** The data-engineering lab, the following morning. Priya had asked Marco to run a controlled test overnight. He had set up a parallel ingestion pipeline using an isolated copy of their production schema and fed it a synthetic batch of transaction records -- half with IDs below the 32-bit boundary, half above.

Marco showed her the results. Every record with an ID below the boundary landed in the warehouse and appeared in the audit log. Every record with an ID above the boundary was silently dropped. The audit log showed no trace of the missing records. The reconciliation dashboard -- the same dashboard Priya had shown the CTO in January -- reported the batch as fully ingested with zero errors.

Priya pulled up the fraud model's training data manifest. The model had been retrained monthly for the past nine months -- the entire period since the migration. Every training run had used data from her pipeline. Every training run had excluded the silently dropped records. She checked the distribution: the dropped records skewed toward recent transactions, which skewed toward higher-value accounts, which were disproportionately the accounts the fraud model was supposed to flag.

The model's recall on high-value transactions had not declined because of a modelling problem. It had declined because the training data no longer contained the high-value transactions it needed to learn from. The pipeline had been feeding the model a systematically biased dataset for nine months, and every metric Priya had built to catch exactly this kind of failure had reported green.

**E6 (belief revision -- consequences).** The CTO's office, that afternoon. Priya brought Marco and the printed vendor post-mortem. She set the document on the CTO's desk, sat down, and said: "The fraud model's performance decline is not a modelling problem. It's a data problem. My pipeline has been silently dropping transaction records for nine months due to a vendor bug triggered by our schema migration. The fraud model has been trained on biased data that systematically excludes the records most relevant to high-value fraud detection."

She walked through the vendor post-mortem, Marco's controlled test, and the record-count analysis. She presented the numbers: fourteen percent of all transaction records dropped, the drop rate increasing, the bias concentrated in exactly the transaction segment the fraud model was designed to protect.

The CTO asked why her monitoring had not caught it. Priya said the monitoring had been designed to track the metrics the pipeline reported about itself -- and the vendor bug prevented the pipeline from reporting the drops. The audit log, the reconciliation dashboard, the schema-validation checks -- all of them operated downstream of the silent filter. Her monitoring was comprehensive, but it monitored the wrong layer. She had trusted instrumentation that could not see the failure it was supposed to detect.

The CTO cancelled the data science team's root-cause analysis and reassigned the investigation to Priya's team. Priya sent a message to the head of data science that afternoon: "The model isn't broken. The data was. My team owns this. I'm sorry it took six months to find."

---

## Di-arc-Co2-4

**4 beats, chronological, present tense**

**Scenario.** A startup CEO believes her co-founder and CTO is quietly building toward a technical architecture that will make the company acquisition-ready -- aligned with their shared strategy to sell within three years. A failed deployment, a board member's offhand remark, and the CTO's own infrastructure-budget proposal establish that the CTO has been building for IPO-scale independence, not acquisition compatibility, because he no longer believes an acquisition is the right exit.

> A = Dana Kowalski (CEO); B = the CTO is building the technical architecture to optimise for acquisition by a specific class of buyer (enterprise SaaS platforms that would absorb the product into their stack); E = a deployment failure exposing custom infrastructure incompatible with standard enterprise stacks, a board member's comment about the CTO's private conversations regarding IPO timing, and the CTO's own infrastructure-budget proposal describing a multi-year self-hosting buildout; B' = the CTO has been building for IPO-scale independence because he has privately concluded that acquisition would kill the product, and the technical architecture now reflects his exit preference rather than their agreed strategy.

**E1 (prior belief established).** The corner booth at the coffee shop two blocks from the office, a Friday morning in March. Dana and her co-founder, Tomasz, sit across from each other with laptops closed. They do this once a month -- no screens, no agenda, just alignment.

"Where are we on the infra migration?" Dana asks.

Tomasz leans back. "Ahead of schedule. We'll be off the legacy hosting by end of Q2. The new architecture is modular -- clean service boundaries, standard APIs, portable data layer. Exactly what a buyer wants to see."

Dana nods. This is the plan they agreed on eighteen months ago: build the product, prove the market, make the architecture acquisition-friendly so that when an enterprise SaaS platform comes shopping, the integration story writes itself. Three-year horizon. They have talked about this in every monthly sync since the seed round.

"Renner's been asking about our stack," she says. Renner is the VP of corporate development at one of the three companies they have identified as likely acquirers. "He wants a technical overview. I told him Q3."

"Q3 works," Tomasz says. "By then the migration is done and the architecture tells the story we want it to tell."

Dana finishes her coffee. The alignment feels solid. It has felt solid for eighteen months.

**E2 (contradicting evidence encountered).** The engineering floor, a Tuesday evening in May. Dana is still at her desk when the on-call Slack channel lights up. A deployment has failed -- not a routine rollback, but a hard failure that takes the staging environment offline for forty minutes. She walks over to the engineering cluster where Tomasz and two senior engineers are working the incident.

She watches over Tomasz's shoulder as he debugs. The failure is in a new service-mesh layer she has not seen before. It is not part of the architecture Tomasz described in their monthly syncs. She reads the configuration files on his screen: custom load balancers, a proprietary service-discovery protocol, a bespoke observability stack that replaces the standard tooling they had been using.

"What is this?" she asks.

"Reliability layer," Tomasz says, not looking up. "The standard tooling couldn't handle the throughput we're projecting for Q4."

Dana does not press the point during the incident. But after the deployment stabilises and the engineers leave, she sits at an empty desk and reads the service-mesh documentation in the internal wiki. The architecture is not modular. It is not portable. It is a custom-built infrastructure layer that would require any acquirer to either maintain a bespoke system indefinitely or rebuild it from scratch. It is the opposite of acquisition-friendly. It is the kind of infrastructure a company builds when it plans to run its own operations at scale, permanently.

She reads for an hour. She does not message Tomasz that night.

**E3 (secondary confirming evidence).** A board dinner, the following week. Dana sits next to Helen Park, the board member who led their Series A. The conversation is casual until Helen mentions, between courses, that Tomasz called her the previous month to discuss IPO timing.

"He had good questions," Helen says. "Market windows, revenue thresholds, the underwriter relationship. I assumed you two were starting to explore the option."

Dana sets down her fork. "We're not. Our exit strategy is acquisition. Tomasz and I have been aligned on that since the seed round."

Helen looks at her. "He didn't mention acquisition. He was asking specifically about what the company would need to look like -- technically and operationally -- to support a standalone public offering. I gave him the framework. I thought it came from both of you."

Dana does not respond immediately. She picks up her glass, drinks, and changes the subject. But she spends the rest of the dinner thinking about the service-mesh layer, the custom infrastructure, and the architecture that makes no sense for a company planning to be absorbed into someone else's stack.

**E4 (belief revision).** Tomasz's office, the following Monday morning. Dana closes the door and sits down. On her phone she has the internal wiki page for the service-mesh architecture and Helen's name in her recent calls.

"I need to see the infrastructure budget proposal for next year," she says.

Tomasz hesitates, then opens a document on his screen and turns the monitor toward her. The proposal describes a three-year infrastructure buildout: dedicated hosting, redundant data centres, a custom deployment platform, and a staffing plan for a twelve-person infrastructure team. The total cost is four times what their current hosting arrangement costs. The document's executive summary uses the phrase "operational independence at scale" twice and "platform self-sufficiency" once. The word "acquisition" does not appear.

"This isn't an acquisition architecture," Dana says. "This is an IPO architecture. You've been building for a standalone company."

Tomasz does not deny it. He says the product is too good to be absorbed into an enterprise platform's feature set. He says an acquisition would mean their technology gets folded into a larger stack, their team gets reassigned, and the product loses its identity within two years. He says he started building for independence ten months ago because he became convinced that the acquisition path would destroy what they built, and he believed that once Dana saw the infrastructure working at scale, she would reach the same conclusion.

"You made a strategic decision for the company without telling me," Dana says. "You built an architecture that forecloses our agreed exit strategy. And you went to our board member to explore an alternative exit behind my back."

Tomasz says he was not going behind her back. He says he was building the case so that when he brought it to her, the evidence would be strong enough to change her mind.

Dana stands. "You don't get to change the company's strategy by building infrastructure that makes the old strategy impossible and then presenting it as a fait accompli. That's not building a case. That's removing my ability to choose."

She tells him she is calling a board meeting for the following week. She tells him the board will decide whether the company's exit strategy is acquisition or IPO, and that until that meeting, no further infrastructure work proceeds on the custom platform. Tomasz asks for two weeks instead of one, to prepare a full presentation. Dana says one week. She leaves the office and closes the door behind her.
