# Research presentations: five video practice guides

Author: Nevil Maloba, Philtechent Limited
Prepared: 18 October 2026
Purpose: explain the completed research and practise presenting an economic argument, a reproducible calculation and a decision.

## The format for every recording

Aim for 12 minutes on the first pass, with a 10–15 minute range. Use six visual stops: the business question; the model; one calculation; two scenarios; the decision; three audience questions. Keep a local copy of the article, case inputs and chart outputs open. Select one case version before recording so every number and caption agrees.

| Time | What to show | What to say |
|---|---|---|
| 0:00–1:15 | Title and one business question | Identify the decision maker, the problem and the outcome that matters. |
| 1:15–3:15 | Actors and model flow | Follow money and evidence through the model. Explain the time horizon, units and three important assumptions. |
| 3:15–5:15 | One calculation | Name each input, calculate slowly and interpret the result in ordinary language. |
| 5:15–7:30 | A scenario comparison | Change one mechanism, identify who gains or funds the change, and explain any timing effect. |
| 7:30–9:00 | Decision and evidence | State the decision informed by the case and the partner evidence needed to assess it commercially. |
| 9:00–12:00 | Three audience questions | Give a direct answer, show the supporting evidence and state the next useful test. |

A synthetic case demonstrates the consequences of its stated assumptions. Explain that status once when introducing the inputs. When discussing a proposed intervention, identify the measurement or study that would establish its effect. This lets the audience distinguish the arithmetic, the business hypothesis and the evidence needed for a real decision.

## 1. Moove × Mwendo Pamoja — vehicle operations, financing and sustainable collections

**Business question:** When vehicle downtime interrupts earnings, how should an operator fund repair and structure collection so that the driver can keep earning and the financing remains viable?

**Opening cue:** “A vehicle can be financed on paper and still become difficult to repay when it stops earning. This case follows the driver, operator and funder through the same interruption, so we can see who needs cash, when it is needed and how the contract recovers.”

**Model walkthrough:** Show the 156-week contract. Trace fares to the platform fee, energy, household need, driver wallet and package payment. Then trace package collections into the operator's insurance, maintenance, debt service and equity cash. Explain annual insurance dates and the vehicle transfer at completion. Point out that the sponsor funding required to support the cash policy is an output.

**One calculation:** Under full availability, weekly cash after the platform fee and energy is KES70,000 × 80% − KES16,000 = KES40,000. Paying KES12,000 of household need and a KES25,000 package leaves KES3,000 for the driver's wallet/surplus rule. Show how fewer working days reduce the first quantity while the bill retains its contractual date.

**Scenario comparison:** Compare 12 days of downtime with two. Under the specified assumptions, faster repair increases driver discretionary cash over the contract from KES399,428.57 to KES456,571.43 and reduces additional operator equity calls from KES62,926.46 to KES26,472.67. Explain why the operator's equity NPV also depends on the extra repair cost and timing: both paths eventually collect the full package amount. This is a useful commercial tension to explain clearly.

**Decision:** Which service commitment, repair budget and benefit-sharing arrangement would make an uptime programme viable for the customer and the operator?

**Audience questions:**
1. If both paths eventually collect the full amount, why fund faster repair? Discuss driver resilience, liquidity commitment and the additional benefits a pilot would measure.
2. What changes if the sponsor has a fixed funding limit? Describe a capped-commitment scenario and the resulting payment/default waterfall.
3. How would a receivables funding structure connect? Identify eligible collections, account control, servicing and reserves as a separately specified financing layer.

**Evidence to open:** [case README](../../../research_lab/mobility_fleet_case/README.md), [full economic narrative](../MWENDO_MOBILITY_FLEET_APPLICATION_AND_WORKED_CASE_2026-10-13.md), and the scenario table/weekly ledgers in `output/mobility_fleet_case_2026-10-13`.

## 2. Moove × Bayesian Relativities — telematics, insurance pricing and profit testing

**Business question:** How can exposure-based insurance evidence support useful pricing while accounting for customer cash, claims, service costs and insurer profitability?

**Opening cue:** “A risk relativity becomes commercially useful when we can follow it into a premium, a claim payment and an economic result. This case connects Bayesian evidence to an insurer profit test and a separate fleet-financing bridge.”

**Model walkthrough:** Begin with exposure, claim counts and severities. Show the posterior uncertainty, the normalised tariff and then the insurer ledger: premium, expenses, reinsurance, claims, reserves and capital cost. Distinguish parameter uncertainty from the variability of future claims. Explain which customer and operator cash flows the financing bridge follows.

**One calculation:** The stable-group synthetic frequency model uses a Gamma shape-rate prior with parameters 2 and 2. With 47 claims and 756 exposure units at base frequency 0.08, the posterior is Gamma(49, 62.48). Its mean frequency multiplier is 49 ÷ 62.48 ≈ 0.7843. Explain why exposure belongs in the denominator and why a posterior interval accompanies the mean.

**Scenario comparison:** Compare a flat tariff, a portfolio-neutral differentiated tariff and a separately specified frequency-reduction scenario. Show how tariff allocation changes who pays while the intervention assumption changes expected losses. Select one profit-and-cash chart and one uncertainty chart from the same seeded run.

**Decision:** What combination of premium, service cost, customer benefit and retained risk merits a prospective test?

**Audience questions:**
1. Does a lower risk score prove that the intervention reduced claims? Explain the distinct estimation and causal questions.
2. How does the profit test include claim delay and reinsurance recovery? Follow one dated cash path and the reserve reconciliation.
3. How much simulation evidence supports the tail estimate? Explain the number of simulated paths, tail sampling and the convergence checks that would precede a commercial decision.

**Evidence to open:** [case README](<C:/Users/Nevo/Downloads/bayesian-telematics-relativities/research_lab/mobility_insurance_profit_case/README.md>), [profit-testing narrative](../MOOVE_BAYESIAN_INSURANCE_PROFIT_TESTING_CASE_2026-10-14.md), and `research_lab/mobility_insurance_profit_case/output`.

## 3. 4G Capital × Underwrite for Collection — merchant cash flows, repeat lending and IFC risk sharing

**Business question:** How can short-cycle merchant lending remain useful and profitable when sales arrive late, margins narrow or guarantee claims take longer to settle?

**Opening cue:** “The useful lending question is what happens after the stock is bought. This case follows merchant cash, repeat facilities and lender funding through sales, repayment and a synthetic guarantee claim.”

**Model walkthrough:** Introduce twelve merchants, daily cash flows, up to six lending cycles and seven scenarios. Follow purchase, sale, settlement, operating obligations, household commitments and repayment. Then show repeat eligibility, lender costs, protection fees and the claim lifecycle. The two-layer protection parameters are synthetic inputs motivated by the public IFC disclosure.

**One calculation:** In the first trading cycle, KES20,000 opening cash + KES125,000 receipts − KES4,200 operating costs − KES3,150 household commitments − KES100,000 principal − KES5,000 fee = KES32,650 closing cash. Show the daily ledger behind that aggregate so the audience sees when cash arrives.

**Scenario comparison:** In the current verified run, baseline lender contribution is KES320,096 with protection and KES322,671 without it. Under delayed sales, the corresponding amounts are KES190,858 and KES124,471. Explain the protection fee in the first comparison and the claim cash in the second. Contribution here is after the modelled direct costs and realised losses, before tax, central overhead and a capital hurdle.

**Decision:** Which repeat-limit, support, reserve and claims-funding rules sustain merchant activity while keeping lender economics visible?

**Audience questions:**
1. Why does protection reduce contribution in the baseline? Walk through the fee and the absence of claim benefit in that scenario.
2. What happens while an accepted claim awaits settlement? Show the lender funding chart and the dated claim events.
3. How do we establish the benefit of support and rescheduling? Separate the assumed trading improvement from the proposed prospective evaluation.

**Evidence to open:** [case README](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/research_lab/four_g_merchant_finance_case/README.md>), [final article](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/publications/linkedin/4g_capital_application_2026-10-13/UNDERWRITE_FOR_COLLECTION_4G_CAPITAL_LINKEDIN_ARTICLE_3000_WORDS.md>), and [chart folder](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/publications/industry-engagement/4g_2026-10-13/charts>). Use the 18 October refresh: 24 passing model tests, 13 Word pages and 22 deck slides.

## 4. Moniepoint × Underwrite for Collection — turning payment activity into repayment-capacity evidence

**Business question:** Which recorded credits are sustainable operating receipts, and what facility can the business service on its actual cash calendar?

**Opening cue:** “An account can show strong inflows while the business has much less cash available for a new payment. We start with the transactions, establish whose cash they represent and follow the result into a reviewable credit decision.”

**Model walkthrough:** Use the detailed governed workflow to trace source permission, economic-event identity, duplicate/reversal checks, ownership and classification into the cash engine. Follow affordability and uncertainty into the officer's decision, maker–checker approval, execution and subsequent outcomes. Highlight the difference between an economic change and a missing data channel.

**One calculation:** KES500,000 total credits contain KES45,000 owner funding, KES30,000 borrowing and KES15,000 refund credits. The remaining KES410,000 comprises the stated sales receipts. After KES270,000 supplier payments, KES70,000 operating expenses, KES20,000 owner/household commitments and KES25,000 existing debt payments, KES25,000 remains against a KES35,000 proposed payment. Explain how the dated cash forecast determines a workable alternative.

**Scenario comparison:** Compare the complete source record, missing wallet coverage and a genuine sales shock using the ten-scenario case. Then compare delayed settlement with an approved extension: contractual arrears fall from eight days to zero, while both scenarios retain a KES20,000 household shortfall. Explain why the payment arrangement and household recovery are separate outcomes. The case has 36 passing tests; use its verification manifest and current charts when recording.

**Decision:** What evidence, terms and review route support a defensible facility decision, followed by proportionate monitoring and servicing?

**Audience questions:**
1. How are internal transfers and duplicate feeds handled? Show economic-event IDs and the provenance ledger.
2. What does the language model do, and who approves the loan? Trace tool receipts, the proposal packet, human mandate and execution service.
3. Can repayment outcomes from approved applicants establish performance for everyone? Explain selection, support and the evidence required for broader policy evaluation.

**Five-article connection:** Article 1 supplies experiments and assignment records; Article 2 supplies sequential servicing and decision uncertainty; Article 3 supplies selective-outcome and policy-evaluation diagnostics; Article 4 supplies the portfolio funding interface; Article 5 supplies controlled orchestration, review, execution and release. The source mapping accompanying the detailed workflow identifies the relevant sections.

**Evidence to open:** [Moniepoint article](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/publications/linkedin/moniepoint_cashflow_2026-10-14/MONIEPOINT_CASHFLOW_UNDERWRITE_FOR_COLLECTION_LINKEDIN_ARTICLE.md>), its standalone workflow images, [case code](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/research_lab/moniepoint_cashflow_case/model.py>) and [verified outputs](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/output/moniepoint_cashflow_case_2026-10-18/verification.json>).

## 5. Deposit Beta, KESONIA and Bank Risk — deposit behaviour, loan repricing and bank decisions

**Business question:** How does the same market-rate change affect loan income, borrower repayment capacity and the bank's deposit and replacement-funding costs?

**Opening cue:** “A rate rise can improve the lending margin and weaken the borrower's cash position at the same time. This case joins the asset and liability paths so Treasury, Credit and ALCO can examine the same scenario.”

**Model walkthrough:** Start with contractual loan repricing and debt service. Follow deposit repricing, lag, product migration, external withdrawal and wholesale replacement. Bring the two paths together in cash, income, expected loss and equity. Use the complete channel diagram before showing the dynamic balance-sheet charts.

**One calculation:** The existing static example produces KES1.240 million additional annual net interest income from the rate change, before runoff and credit effects. The additional replacement-funding cost is KES584,000 and the expected-loss increment is KES900,000. KES1,240,000 − KES584,000 − KES900,000 = −KES244,000. Explain the horizon and why an expected-loss increment is distinct from an immediate cash payment.

**Scenario comparison:** Use the verified 24-month expected-cohort case to compare a rate rise, deposit withdrawal and joint borrower/funding stress. Baseline modelled profit is KES12.731 million; joint stress produces KES2.584 million. Controlled growth produces KES3.611 million while reducing new lending from KES120 million to KES90 million. Explain both the profit and lending-volume outcomes. Show reset dates, the cash chart and balance-sheet reconciliation. There are 21 passing tests, nine main scenario/policy cases and nine sensitivity cases.

**Decision:** Which funding action, customer-term review or lending-capacity adjustment should each responsible function consider under the shared scenario?

**Audience questions:**
1. Why can a low deposit beta coexist with credit deterioration? Explain the immediate borrower payment channel and the lagged deposit channel.
2. How does migration differ from withdrawal? Trace a change between bank products separately from an outflow leaving the bank.
3. How is expected loss linked to the cash and capital accounts? Walk through the allowance, default/write-off and equity treatment used in the case.

**Evidence to open:** the Deposit Beta article and diagrams in the sibling `regtech-kesonia-treasury/publications/linkedin` folder, its operations methodology and the final dynamic-case verification.

## Practice, playback and review

Record 4G first, then Moniepoint, Moove × Mwendo, Moove × Bayesian and Deposit Beta. This practice order starts with tangible business cash and progresses through evidence, multi-actor finance, probability and the bank balance sheet. The public release order can follow the research narrative.

Before recording, select three charts and one calculation, place the relevant assumptions beside them, and write a one-sentence conclusion. Prepare cue words for each section. In the first take, complete the argument in one pass. Review the recording, select two improvements and make a second take. Keep the first take so progress remains visible.

| Criterion | Playback question | Evidence to record |
|---|---|---|
| Pacing | Did I leave enough time to read the chart and follow the arithmetic? | Section timestamps; places rushed or repeated. |
| Clarity | Could a listener explain the business question and result after one hearing? | One-sentence summary; jargon that needed definition. |
| Quantitative explanation | Did I state units, horizon, assumptions and the meaning of uncertainty? | Any unsupported leap; corrected calculation wording. |
| Visual explanation | Did I guide attention to the relevant axis, actor and scenario? | Chart readability and cursor/annotation choices. |
| Decision relevance | Did I explain what someone would do with the result? | Decision, owner and next evidence requirement. |
| Questions | Did I answer directly and connect the answer to evidence? | Question, answer length and strongest supporting exhibit. |

Score each criterion from 1 to 5, where 1 means the explanation needs substantial rebuilding and 5 means the listener can follow and use it. Record timestamps for feedback. Choose two changes for the next take, such as slowing down the cash bridge and answering the question in the first sentence. When a recording or transcript is available, review it against this same rubric.

## Video description template

Title: [use the title above]

In this walkthrough, I examine [business question] using [case and version]. The calculation connects [inputs] to [customer, lender or insurer outcomes] and compares [scenarios].

Case status: [synthetic connected case / empirical validation stage, as supported by the release].

Article: [public article link]
Code and reproduction instructions: [verified public repository link]
Inputs and outputs: [release or case link]
Research whitepaper: https://doi.org/10.5281/zenodo.23343888

Chapters: [replace with the actual recording timestamps]

Three discussion questions: [use the audience questions above or the final article research questions].

Use the attribution and licence specified in the relevant publication. Identify the case version and link its sources so the viewer can reproduce the numbers.

## Current file locations

[Complete publication and recording index](<C:/Users/Nevo/Downloads/insuretech & embedded finance/publications/industry-engagement/APPLICATIONS_AND_RECORDING_INDEX_2026-10-18.md>)

4G and Moniepoint are maintained in Underwrite for Collection; the Moove insurance case is in Bayesian Relativities; the Moove operating case remains in Mwendo Pamoja; Deposit Beta remains in RegTech KESONIA.
