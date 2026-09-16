# Discovery arc × Corporate — Batch 3 (Tier C)

---

## Di-arc-Co3-01

**Scenario.** A senior fraud analyst at a regional bank has spent three years building a model that flags small-business loan applications from a specific zip code cluster as high-risk. When a new compliance officer audits the model's historical performance, the analyst is forced to look at what his flags actually predicted versus what defaulted. His belief that the model is working correctly does not survive the comparison.

> A = Marcus Teel (senior fraud analyst); B = the proposition that the zip-code-cluster flag is a reliable predictor of small-business loan default; E = a side-by-side audit table showing that flagged applications from the cluster defaulted at 4.1% while unflagged applications from comparable income-bracket zip codes defaulted at 11.3%; B′ = the proposition that the zip-code flag is not predictive of default risk and has been suppressing approvals for creditworthy applicants

5 beats, chronological

**E1 (prior belief established).** The risk committee room, third floor, a Tuesday morning in February. Marcus pulled up his model's dashboard as the quarterly review opened and walked the committee through the flag logic he had built in 2021: any application from the six-zip cluster showing annual revenue under $280,000 and fewer than three years of banking history received an automatic secondary review, which in practice meant a two-week delay and a 60% decline rate.

"The cluster has been our highest-exposure segment for three consecutive years," he told them. "The flag is performing as designed."

The committee chair, Paula Reinholt, nodded and moved to the next item. Nobody asked what "performing as designed" meant in terms of actual default outcomes. Marcus had not offered to show them.

**E2 (belief reinforced).** The following week, Marcus presented the same metrics at the branch managers' call. One of the managers, Divya Chowdhury at the Eastside branch, asked whether the two-week delay was creating friction with local business owners who were going elsewhere for financing. Marcus said that secondary review was a risk-management tool, not a customer-experience tool, and that the friction was an acceptable cost of maintaining portfolio quality. Chowdhury did not press it. The call ended. Marcus annotated his notes: *Eastside flagging concern — addressable via community liaison if needed. No model change warranted.*

The annotation made him feel thorough.

**E3 (partial/ambiguous evidence).** The new compliance officer, Renata Sousa, had been in the role for six weeks when she stopped by Marcus's desk with a printed spreadsheet. She said she had been running a retrospective on the secondary-review queue and had some questions about how the model's accuracy was being measured. Marcus told her the model's performance was benchmarked against flag rate, secondary-review volume, and time-to-decision. Sousa looked at her spreadsheet and said she had been measuring something different. She asked whether Marcus had a figure for the default rate among flagged applications that were eventually approved, as distinct from the applications that were declined. Marcus said he did not have that figure to hand but could pull it. Sousa said she would appreciate that. She left the spreadsheet on his desk.

Marcus looked at it after she left. It was a partially completed two-column table. The right column was blank. The left column had headers he recognised — but the structure of the comparison she was building was not one he had used before, and he put the sheet in his in-tray and went back to the queue.

**E4 (contradicting evidence encountered).** Sousa's office, the following Thursday. She had prepared the completed audit table on her monitor and had printed a copy for Marcus. The table showed three years of outcomes for two groups: applications from the zip-code cluster that had been flagged and subsequently approved after secondary review, and applications from matched income-bracket zip codes outside the cluster that had not been flagged. Default rate for the flagged-and-approved cluster applicants: 4.1%. Default rate for the unflagged comparison group: 11.3%.

Marcus read the table twice. He asked about the matching methodology. Sousa walked him through it: matched on reported annual revenue band, years in business, and loan size. The comparison group was not identical to the cluster — no geographic comparison could be — but the methodology was sound enough that the gap could not be explained by observable differences in applicant profile.

He asked whether the data covered all three years. It did. He asked whether the secondary-review delay itself might have filtered out the highest-risk applicants, making the approved group artificially clean. Sousa said she had considered that and had modelled the expected effect: even under a generous filtering assumption, the gap remained. The cluster applicants who cleared secondary review were not just marginally lower-risk than the comparison group. They were substantially lower-risk, by a margin that the filtering effect alone did not explain.

Marcus sat with the table for a long moment. The flag was not identifying high-risk applicants. It was identifying applicants from a geographic area, delaying and declining a substantial fraction of them, and approving the remainder — who then defaulted at a rate well below the comparable population that had never been flagged at all.

**E5 (consequences of revision).** Marcus's desk, that evening after Sousa had gone home. He opened his model documentation and read the section he had written in 2021 under the heading *Performance Rationale*, where he had described the zip-code cluster as a "validated high-exposure segment." The phrase had meant, at the time, that the cluster had a higher flag rate. He had not, in 2021, checked what the flag rate corresponded to in actual defaults. He had measured the model's output and called it performance.

He opened a new document and began drafting a memo to Paula Reinholt. He did not use the word *validated*. He wrote that the model's geographic flag did not demonstrate predictive validity against the outcome it was ostensibly predicting, and that the committee should be aware that three years of secondary-review delays and declines in the cluster had been applied to a population that was, by the available outcome data, less risky than the baseline the model was designed to protect against. He recommended a full methodology review and a suspension of automatic secondary review for cluster applications pending that review.

He saved the draft, read it once more, and sent it before he could decide to wait until morning.

---

## Di-arc-Co3-02

**Scenario.** The head of talent acquisition at a fast-growing logistics firm believes that candidates who attended four-year universities are significantly more likely to succeed in operations management roles than those without degrees, and has structured the firm's hiring pipeline accordingly. A VP of operations, reviewing promotion data after a reorganisation, presents evidence that contradicts this assumption. The sequence is told in present tense from the VP's point of view.

> A = Carla Weiss (VP of Operations); B = the proposition that four-year university attendance is a positive predictor of operations management success at Fulton Logistics; E = a two-year promotion-and-retention dataset showing that non-degree hires promoted into operations management roles outperformed degree hires on every tracked metric at 18 months; B′ = the proposition that four-year degree status is not a valid predictor of operations management success in this firm's context, and that the degree filter is excluding the better-performing candidate pool

4 beats, chronological

**E1 (prior belief established).** It is 8 a.m. on a Monday and Carla is sitting across from Dion Massey, the head of talent acquisition, in one of the glass-walled conference rooms on the second floor. The reorganisation has just closed and Dion has asked for the meeting to discuss headcount for the three new regional operations lead roles.

Dion has a template open on his laptop showing the candidate profile he uses for operations management searches. It requires a four-year degree from an accredited institution. He explains to Carla that this requirement has been in place since he joined the firm and that it is based on the original operations director's view that the role demands analytical rigour that correlates with degree completion. He says the requirement has served them well. Carla does not have specific data to dispute this. She asks him to send her the template after the meeting and agrees to the search parameters he has outlined.

On her way back to her office, she makes a note to herself to check the data before the search closes. She has a feeling — not a strong one, just a feeling — that some of the best regional managers she has worked with in the past two years came up through the operations floor rather than through the degree-track pipeline. But a feeling is not a number.

**E2 (partial/ambiguous evidence).** That afternoon, Carla pulls the promotion records for the past two years from the HR system. The data is messy — some fields are inconsistently coded, and the performance ratings prior to the reorganisation used a different scale than the current one. She can see that the firm has promoted fourteen people into operations management roles over the period, but she cannot yet get a clean breakdown by educational background without asking HR to run a specific query.

She emails the HR analytics lead, Priya Nair, and asks for a cut of the data: promotions into operations management in the last 24 months, segmented by degree status at hire, with 18-month performance ratings and retention status attached. She flags it as non-urgent. Priya says she can have it by Thursday.

Carla returns to the reorganisation backlog. She does not think about the data query again until Thursday morning, when Priya's file lands in her inbox.

**E3 (contradicting evidence encountered).** Carla opens the file at her standing desk, half her attention still on a Slack thread about a warehouse delay in the Cincinnati hub. The file contains a clean two-by-two breakdown: degree hires versus non-degree hires promoted into operations management, by 18-month performance rating and retention status.

The numbers are not ambiguous. Of the fourteen promotions, six were degree hires and eight were non-degree hires who had come up through floor supervisor or dispatch coordinator roles. The 18-month average performance rating for the degree group is 3.4 out of 5. The 18-month average for the non-degree group is 4.1. Retention at 18 months: degree group, four of six still in role. Non-degree group, eight of eight still in role.

Carla closes the Slack thread. She reads the file a second time to check whether the performance scale changed between the two groups' promotion dates. It did not — Priya has normalised the ratings in a footnote. The groups are small, and she knows that, but the direction of the gap and its magnitude are not consistent with the assumption Dion has been operating on. A filter designed to select for analytical rigour appears to have been selecting against the candidates who actually performed better in the role.

She sits with that for a moment. Then she forwards the file to Dion and asks for thirty minutes that week.

**E4 (confrontation scene).** Dion's office, Wednesday afternoon. The data file is open on his screen and he has been looking at it before Carla arrived, which she can tell from the way he clicks past it when she sits down rather than opening it fresh.

"I want to understand the methodology," he says.

Carla walks him through it: 24-month window, 14 promotions, Priya's normalisation of the rating scale. Dion says the sample is too small to draw conclusions. Carla agrees the sample is small. She asks him whether he has any performance data from operations management hires that would show the degree filter performing as expected — higher ratings, better retention — across a larger group. Dion says that data would require a longer lookback than 24 months and that the role responsibilities have changed enough that earlier data might not be comparable.

"I need you to remove the degree requirement from the three new searches," Carla says. "We can add it back if a clean dataset eventually supports it. Right now the data we have points the other way."

Dion says he is not comfortable removing a long-standing qualification requirement on the basis of fourteen observations. He says the operational director who put it in place had reasons that went beyond what shows up in a performance rating. He says he would want to loop in the CHRO before changing it.

"Then let's loop in the CHRO," Carla says. "I'm happy to present the data to her. I want a decision before the search briefs go out on the fifteenth."

She waits. Dion looks at his screen.

"I'll set it up for next week," he says finally. Resolution: deferred to named authority (the CHRO).

---

## Di-arc-Co3-03

**Scenario.** A product director at a software firm believes that the company's enterprise customers are staying because of the platform's reporting features, which the team has invested heavily in over two years. A customer success manager who has been running exit interviews with churned accounts brings a different account of what customers actually valued — and what they didn't. The sequence is told in free indirect style from the product director's perspective.

> A = Nadia Okonkwo (Product Director); B = the proposition that enterprise customers stay on the platform primarily because of its reporting and analytics features; E = a structured exit-interview summary showing that no churned customer cited reporting as a reason for leaving, and that retained customers in a parallel survey ranked reporting eighth out of ten features by importance; B′ = the proposition that reporting features are not the primary driver of enterprise retention, and that the team's two-year investment thesis has been misaligned with the actual reasons customers stay

6 beats, non-linear: E4 → E1 → E2 → E3 → E5 → E6

**Note on beat order.** The sequence opens in the present (E4, the evidence scene) and then cuts back to establish the prior belief and its reinforcement before returning to the aftermath. Chronological order: E1 → E2 → E3 → E4 → E5 → E6.

**E4 (contradicting evidence encountered — depicted first).** The email from Felix Strand, the senior customer success manager, arrived on a Tuesday with the subject line "Exit interview summary — Q1." Nadia opened it at her desk before the morning standup. It was a six-page PDF with a cover note that said: *I wanted to get this to you before the roadmap review. Some of what's here surprised me.*

The summary covered eighteen months of structured exit interviews across eleven churned enterprise accounts. Felix had asked each account two questions: what features they had used most heavily, and what feature gaps or service failures had contributed to their decision to leave. Reporting and analytics appeared in the usage column for four of the eleven accounts. It appeared in the gap column for zero of them. Not once, across eleven churned accounts, had a customer named reporting deficiencies as a reason for leaving.

The second section was newer: a parallel survey Felix had run with twenty retained accounts the previous month, asking them to rank ten platform features by importance to their renewal decision. Reporting ranked eighth. The top three were data integration reliability, bulk-action tooling, and permission-scoping. Nadia had put none of these features on the roadmap in the past two years. She had put reporting on the roadmap four times.

She read the summary through to the end. She did not forward it to her team before the standup.

**E1 (prior belief established).** Two years earlier, the product strategy offsite, a lodge outside the city. The whiteboard at the end of the room was covered in post-it notes from the morning session and the facilitator had been grouping them into themes. The largest cluster was labelled *data visibility / reporting*. Nadia had put three of those notes up herself.

The sales director had said, flatly and without qualification, that the two deals they had lost the previous quarter had both named reporting gaps in their offboarding calls. The CS lead at the time — not Felix; Felix came later — had confirmed it. Nadia had taken two pages of notes and had left the offsite with a clear mandate: build reporting, grow the enterprise tier.

The strategy memo she wrote on the plane home had a section heading that read: *Enterprise customers stay because they can see their data.* It was an inference, not a data point. But it felt load-bearing. She had treated it as such.

**E2 (belief reinforced).** The following spring, the product team's NPS survey went out to the enterprise tier. The open-text responses for the top-promoter segment were dominated by mentions of the reporting dashboard. Nadia had screenshotted three of them and put them in the quarterly deck. The board loved the deck. The board chair said, specifically, that it was good to see investment going where the customers were telling you it mattered.

Nadia had not thought to ask Felix, who had joined six months earlier, whether the NPS open-text promoters were representative of the full enterprise cohort. She had the promoters' quotes. That had felt like enough.

**E3 (partial/ambiguous evidence).** Felix had flagged something in a one-on-one eight months before the exit summary arrived. He had said, carefully, that the churned accounts he was working with were not mentioning reporting in their offboarding calls. Nadia had asked him what they were mentioning. He had said integration pain, mostly. And one account had been very specific about bulk-action tooling.

Nadia had filed this under *individual account issues* and had not changed the roadmap. One account's feedback was not a signal. A pattern was a signal. She had told Felix as much, and he had nodded and not pushed back, and she had thought that was the end of it.

Eight months later she understood that Felix had been building the pattern. He just had not had enough data yet to make it impossible to dismiss.

**E5 (belief revision).** The roadmap review meeting, the afternoon after the email. Nadia had forwarded the summary to the team two hours before the meeting and had asked them to read it. She opened by saying she had spent the morning thinking about what the data meant and had concluded that the investment thesis underpinning the past two roadmap cycles was not supported by the outcome evidence.

That was a strange sentence to say out loud. She said it anyway.

She told them that the reporting features they had built were not what customers were citing as reasons to stay or reasons to leave. She said the two years of roadmap priority she had given to reporting had been built on a belief she had formed at an offsite and reinforced with a sample that turned out to be unrepresentative. She said she did not think the team had done bad work — the reporting features were good — but that good execution on the wrong hypothesis was still the wrong hypothesis.

Nobody said anything for a moment. Then the engineering lead said: "So what's the thesis now?"

Nadia had three candidate answers. She told him she was not ready to commit to a new thesis until she had spent more time with Felix's data and had talked directly with some of the retained accounts. She was not going to replace one unexamined belief with another.

**E6 (consequences of revision).** Felix's desk, the following day. Nadia asked him to walk her through the methodology behind the retained-account survey — not because she doubted it, but because she wanted to understand what he had controlled for and where the gaps were. Felix looked slightly startled to be asked to explain his methodology to the product director. He walked her through it anyway: sample selection, question design, the response rate, the two accounts he had excluded and why.

Nadia took notes. She asked whether he had verbatim responses she could read. He did. She read through eleven pages of them, sitting at the spare chair by his desk, and she did not try to match them to the roadmap she had already built. She was looking for what customers had said, not for confirmation of what she had already decided to build next.

That was, she recognised, a different way to use customer data than she had been using it. She was not sure yet what it would mean for the roadmap. That felt, provisionally, like the correct amount of uncertainty.

---

## Di-arc-Co3-04

**Scenario.** The CFO of a mid-sized retail chain has operated for two years on the belief that their private-label margin advantage is protecting overall company profitability against branded-goods price erosion. When the finance team completes a contribution-margin analysis by SKU, the CFO's assumption does not hold: the private-label lines are profitable on gross margin but are consuming disproportionate warehouse and logistics overhead. The sequence uses embedded document form for the evidence beat.

> A = Phillip Arndt (CFO); B = the proposition that the private-label product lines are protecting overall company profitability by providing a margin buffer against branded-goods price erosion; E = a contribution-margin analysis showing that when warehouse slot cost, pick-and-pack cost, and returns processing cost are allocated to private-label SKUs, the net contribution margin of the private-label segment is 2.1%, compared to 9.4% for the branded segment; B′ = the proposition that the private-label segment is not a margin buffer but a margin drain when fully-loaded costs are applied, and that the company's profitability assumption has been based on an incomplete cost picture

5 beats, chronological

**E1 (prior belief established).** The board strategy session, eighteen months earlier. The deck that Phillip had presented was titled *Private Label as Margin Architecture*, and the central claim was simple: private-label gross margins ran at 38% against branded-goods gross margins of 22%, and the company's deliberate expansion of its private-label assortment was building structural insulation against the price pressure that was squeezing branded-goods retailers across the sector.

The board had approved an expansion of the private-label line from 140 SKUs to 280 over the following fiscal year. Phillip had recommended the expansion. He had built the model that justified it. The model used gross margin as its central metric because gross margin was what he had available, clean and consistent, across both segments.

He had noted in a footnote that fully-allocated overhead costs were not included in the analysis due to the difficulty of attributing shared warehouse and logistics infrastructure to individual product lines. He had not weighted the footnote. Nobody had asked about it.

**E2 (belief reinforced).** The following Q3 earnings call. The CFO's prepared remarks included a paragraph on the private-label program: gross margins in the segment were 39.2%, up 1.2 points year-over-year, and the private-label mix had grown to 31% of total SKU count. Two sell-side analysts asked about it on the call. One of them called the private-label strategy "a good capital-allocation story." Phillip had agreed that it was.

After the call, the CEO had stopped by Phillip's office. She said the private-label numbers were getting noticed. She asked whether the program was tracking to plan. Phillip said it was tracking ahead of plan on gross margin. The CEO said that was good to hear.

**E3 (partial/ambiguous evidence).** Three months before the contribution-margin analysis was completed, the head of warehouse operations, a direct report of the COO's named Bernice Thao, had raised a flag in a cross-functional planning meeting. She said the private-label expansion had driven a 23% increase in the number of active SKUs in the central distribution center and that the warehouse team was seeing meaningful increases in pick complexity, returns processing volume, and slot replenishment frequency — all cost drivers that were currently sitting in the warehouse operations budget, not allocated to any product line.

Phillip had been in the meeting. He had noted Bernice's point and had said that the next planning cycle would be a good opportunity to look at overhead allocation methodology. Bernice had said she would send him the operational cost data. She had sent it two weeks later. Phillip had forwarded it to his senior analyst with a note to include it in the next quarterly review.

The analyst had included it in the quarterly review. The quarterly review had not yet happened. That was how it had sat, unexamined, for eleven weeks.

**E4 (contradicting evidence encountered — embedded document).** The contribution-margin analysis, prepared by the finance team and distributed to Phillip three days before the quarterly review:

---

*FULTON RETAIL GROUP — CONTRIBUTION MARGIN ANALYSIS BY SEGMENT*
*Period: Full Year FY2024 | Prepared by: Finance Analytics*

*Methodology note: Gross margin figures are consistent with prior reporting. This analysis adds allocation of warehouse slot cost (per SKU per week), pick-and-pack cost (per unit fulfilled), and returns processing cost (per return event) to arrive at contribution margin. Allocations are based on FY2024 actuals from warehouse operations, distributed by SKU activity volume as provided by Bernice Thao, Warehouse Operations.*

| Segment | Gross Margin | Allocated OH/Unit | Net Contribution Margin |
|---|---|---|---|
| Private Label (280 SKUs) | 38.9% | 36.8% | 2.1% |
| Branded Goods (660 SKUs) | 22.1% | 12.7% | 9.4% |

*Private-label SKUs account for 30% of total SKU count but 58% of warehouse slot utilisation and 47% of pick-and-pack labour hours, reflecting higher average SKU velocity, more frequent replenishment cycles, and a 3.1× higher return rate than the branded segment.*

---

Phillip read the table on the morning the analysis arrived and did not open anything else for forty minutes. The gross-margin advantage that had anchored two years of strategy and two board presentations was not wrong — the numbers were accurate — but it had been measuring the revenue side of a cost structure it was not looking at. The private-label program was generating 38.9% gross margin on every unit sold and consuming 36.8% of that margin in warehouse and logistics overhead that had been invisible in every report he had ever shown the board.

He called the senior analyst and asked her to verify the overhead allocation numbers against the raw operational data from Bernice's file. She said she had already done that. She said the numbers were consistent.

**E5 (consequences of revision).** The quarterly review meeting, two days later. The CFO went last, after the commercial and operations leads had presented. He told the room that the private-label contribution-margin analysis had changed his view of the program's economics and that he wanted to walk them through what he now understood to be true, which differed from what he had told the board eighteen months ago.

He presented the table. He explained the methodology. He said the gross-margin analysis he had used to build the private-label expansion case had been measuring the right metric for the wrong cost boundary, and that the overhead allocation data Bernice's team had generated showed the program's net contribution to be materially lower than the gross-margin numbers had implied. He said the board presentation he had given eighteen months ago, including the recommendation to expand from 140 to 280 SKUs, had been built on an incomplete analysis.

The COO asked what a responsible next step looked like. Phillip said he wanted to bring the contribution-margin analysis to the board before the next strategy session, lay out the full picture, and recommend a SKU rationalisation process that would evaluate private-label lines on contribution margin rather than gross margin. He said the expansion had not been a mistake in execution — the warehouse team had done what was asked of them — but the decision framework had been wrong, and he was the one who had built it.

Nobody in the room disputed that assessment.
