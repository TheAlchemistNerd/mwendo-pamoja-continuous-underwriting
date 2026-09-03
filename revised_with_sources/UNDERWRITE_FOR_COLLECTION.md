# Underwrite for Collection

## Rebuilding credit architecture around sustainable cash recovery

**By Neville Maloba**  
**Industry article | 30 August 2026**

> A loan is successfully underwritten only when its structure, monitoring and intervention design support sustainable collection after disbursement.

Credit markets naturally celebrate origination. New disbursements are visible, immediate and commercially attractive. They enlarge the loan book, create interest-bearing assets and provide a clear story about financial inclusion or economic growth. Collection is less photogenic. It occurs over months or years, is distributed across servicing teams and systems, and becomes most visible when something has already gone wrong.

That imbalance can distort credit architecture. A lender can build an excellent application funnel, fast identity checks and a sophisticated approval model while treating the performance of the loan after disbursement as somebody else's operational problem. The result is a credit process optimised to answer, “Should we lend today?” when the economically decisive questions are broader: “Can the borrower repay from sustainable cash flow, when could that capacity deteriorate, what intervention would improve the outcome, and what cash will ultimately reach the lender after delay and workout cost?”

This is not an argument for more aggressive collections. It is an argument for designing credit backward from fair, sustainable collectability. Collection should mean preserving recoverable economic value while protecting customers from unsuitable products, avoidable distress and abusive treatment. The architecture must connect product design, underwriting, monitoring, servicing, restructuring, recovery, expected credit loss, capital and funding. It must also keep their responsibilities distinct.

## 1. Read the Kenyan numbers before interpreting the story

Recent Kenyan figures illustrate why disciplined definitions matter. People Daily, reporting Kenya Bankers Association data, stated that banks advanced KSh245.1 billion in new loans to micro, small and medium enterprises during the first half of 2026. It also reported KSh590.3 billion of outstanding MSME credit across reporting institutions at June 2026 [1]. The first number is a six-month flow of new disbursements. The second is a stock at a reporting date.

The Central Bank of Kenya's March 2026 Credit Officer Survey presents a different population. Across the banking sector, gross loans increased from KSh4,369.6 billion in December 2025 to KSh4,453.0 billion in March 2026. The gross non-performing-loan ratio moved from 15.4 percent to 15.6 percent as gross NPLs increased by 3.4 percent [2]. Business Daily, drawing on CBK data, reported that the corresponding NPL stock rose by approximately KSh21 billion, from KSh674.4 billion to KSh695.4 billion [3].

Viewed together, KSh245.1 billion and KSh695.4 billion illuminate different points in the credit cycle rather than two outcomes from one portfolio. They differ in scope, period and denominator:

- KSh245.1 billion is reported new MSME lending during six months.
- KSh695.4 billion is the outstanding stock of gross NPLs across the banking sector at one date.
- One describes originations; the other describes accumulated problem assets.
- One concerns an MSME lending flow; the other covers the banking sector's loan book.

Their combined value is the wider perspective they create: origination growth and asset-quality stress can coexist, strengthening the case for reporting lending activity alongside subsequent portfolio performance. Estimating the default rate of the newly disbursed MSME loans would require vintage-matched performance data drawn from the same population, period and denominator.

The KBA MSME dashboard adds another useful perspective. For June 2026, its selected MSME portfolio displays a 24.5 percent NPL ratio and separately reports value-based ratios, loan counts and the share of loans that are non-performing [4]. These measures can diverge materially. In the dashboard's institution view, banks show a 20.7 percent value ratio but a 5.2 percent NPL share by number of loans. Insurance Premium Financing shows 6.9 percent by value and 14.2 percent by count. Each measure answers a different question. A small number of large defaults can dominate value, while many small defaults can dominate count.

Every public statement about credit quality should therefore identify at least six attributes: population, reporting date, observation period, numerator, denominator and whether the measure is based on balances, accounts, borrowers or cash. Vintage is equally important. A young book can appear healthy because its loans have not had time to mature into delinquency.

The CBK survey nevertheless supports the underlying concern about recovery. For the quarter ending June 2026, respondents expected banks to intensify credit-recovery efforts in nine of eleven economic sectors. The highest reported intentions were in trade, at 78 percent of respondents; personal and household, at 75 percent; real estate and building and construction, each at 68 percent; transport and communication, at 66 percent; and tourism, restaurants and hotels, at 61 percent [2]. The lesson is not that lending should stop. It is that performance after disbursement deserves the same institutional attention as approval.

## 2. Collection is a design property, not a late-stage department

The most expensive collection problem often begins before a collector receives an account. It may begin with a repayment date unrelated to the borrower's income cycle, a tenor shorter than the productive use of the funds, an instalment that ignores volatile essential expenditure, an initial limit calibrated to demand rather than affordability, or a refinancing structure that conceals rather than cures distress.

Basel's current credit-risk principles frame sound practice across four connected areas: a suitable credit-risk environment, a sound credit-granting process, appropriate credit administration, measurement and monitoring, and adequate controls [5]. The sequence matters. Credit is not governed only at approval. Monitoring, classification and remedial management are part of the original risk architecture.

For households, gig workers and small enterprises, affordability should be cash-flow based. A static income declaration or average wallet balance can hide timing risk. The borrower may generate sufficient monthly revenue but still fail because collections fall before the week's main receipts, fuel or inventory absorbs working liquidity, or several lenders sweep the same account. Product design should therefore consider:

- the timing, variability and concentration of income;
- essential operating and household expenditure;
- existing repayment obligations across providers;
- seasonality and shock sensitivity;
- a sufficient residual cash buffer after repayment;
- and a repayment schedule aligned with how the financed activity generates cash.

This does not mean that every lender must observe every transaction. Data minimisation remains essential. It means that the evidence selected for underwriting should answer a clear economic question and be collected lawfully for a stated purpose.

The institution should define success before choosing a model. Approval rate and disbursement volume are incomplete objectives. A balanced outcome function should include durable customer performance, risk-adjusted margin, net present value of recoveries, conduct outcomes, complaints, operational cost, capital consumption and funding consequences. Sales incentives should not reward volume while transferring all later losses and remediation costs to risk and collections teams.

## 3. Build a single credit-state and cash-flow truth

Many lenders cannot reconstruct the life of a loan without combining application tables, core-ledger balances, payment switches, collection notes, restructures, CRB files and finance journals. When these systems disagree, the lender cannot reliably train a model, calculate roll rates, explain a decision or reconcile expected loss to cash.

The foundation should be a canonical, event-time credit ledger. Each material event needs an effective timestamp, processing timestamp, source, version and reversal logic. The ledger should distinguish at least:

- application, offer, acceptance and disbursement;
- scheduled amount due and contractual due date;
- payment initiation, settlement, allocation and reversal;
- fees, interest, principal and penalty components;
- delinquency entry, days past due and cure;
- limit change, draw freeze and account closure;
- modification, restructuring and forbearance;
- collateral, guarantee and insurance proceeds;
- recovery cash, recovery cost and write-off;
- complaint, vulnerability and communication preference;
- model score, uncertainty, policy decision and human override.

Point-in-time correctness is non-negotiable. A model trained on data that became available after the decision date learns the future. A collections model can be similarly contaminated if a feature incorporates a payment reversal or recovery outcome recorded later. Historical features must be rebuilt as they would have been known at the decision time, with late-arriving events and corrections governed explicitly.

BCBS 239 emphasises accurate, complete, timely and adaptable risk-data aggregation [6]. Those principles are valuable far beyond globally systemic banks. A smaller lender can implement them proportionately through authoritative data sources, a common dictionary, automated reconciliation, lineage, quality thresholds and controlled manual adjustments.

Five clocks should remain distinct: origination age, contractual days past due, time since the last payment, time since a material deterioration signal and time since an intervention. Collapsing them into one “status” field discards information needed to understand delinquency, treatment and cure.

## 4. Model both whether and when cash deteriorates

The discussion now moves from operating design to behavioural scoring because digital lenders increasingly use repayment patterns, transaction behaviour and cash-flow changes to monitor credit between conventional review points. Behavioural scoring is one source of evidence within the wider credit lifecycle. It can help detect deterioration after disbursement, while affordability, product structure, bureau evidence, verified cash flows and servicing history continue to anchor the credit decision. The modelling components below therefore give behavioural signals a defined role instead of allowing a single score to carry the entire collection strategy.

A conventional probability-of-default model estimates whether a defined default event will occur within a fixed horizon. It provides a useful foundation when calibrated by product, vintage and economic regime. Timing, transition, exposure and recovery models then extend that foundation into the collection lifecycle.

A lender also needs timing and transition views. A survival or hazard challenger can estimate when delinquency or default may occur. A multi-state model can represent movement among current, early arrears, late arrears, cure, modification, prepayment, default, recovery and closure. Loss-given-default and recovery models should estimate not only the percentage recovered, but its timing and cost. Exposure-at-default must reflect undrawn commitments and adverse utilisation where revolving facilities can be drawn as conditions weaken.

These components answer different questions:

- Fixed-horizon PD: What is the probability of default within the governed horizon?
- Hazard: When is deterioration most likely?
- State transition: Where could the account move next?
- EAD: What will be owed when default occurs?
- LGD and recovery: How much net cash will be lost or recovered, and when?
- Treatment model: Which permissible action is likely to improve the outcome?

For thin-data segments, hierarchical models can pool information across products, locations, platforms or cohorts while allowing well-observed groups to differentiate. Posterior uncertainty should affect decisions. A high estimated risk with wide uncertainty is not the same as a precisely estimated high risk. The policy may request more evidence, reduce an initial limit or route the case for review rather than treating the score as certainty.

Within this advanced layer, “neural” refers to artificial intelligence, specifically neural-network models that learn representations from sequences of transactions, repayments or other permitted behavioural observations. AI-based neural representations can improve early warning, while interpretable variables such as repayment velocity, earnings velocity, cash-flow asymmetry, debt-to-liquidity and wallet volatility retain precise definitions, observation windows and one canonical owner. When neural embeddings are learned from the same raw sequences, the representation can be cross-fitted and residualised against the explicit variables before shrinkage is applied. This reduces duplicated signal and makes the AI model's incremental contribution testable. Simpler behavioural scorecards remain the benchmark, and neural models advance only when they demonstrate stable, explainable improvement across time, segments and policy changes.

Model development should include out-of-time and out-of-segment validation, calibration, drift analysis, sensitivity testing, benchmark models and documented limitations. As a comparative model-risk reference, current United States interagency guidance emphasises risk-based governance, sound development, validation and controlled use proportionate to materiality [7]. NIST's voluntary AI Risk Management Framework similarly organises AI risk work around governing, mapping, measuring and managing throughout the lifecycle [8].

## 5. Keep prediction, policy and action separate

A model estimates an outcome. It should not silently define what the institution is permitted or required to do.

A governed credit architecture separates four layers:

1. **Evidence layer:** validated application, bureau, ledger, payment and permitted contextual data.
2. **Inference layer:** PD, timing, state-transition, EAD, LGD, recovery and uncertainty estimates.
3. **Credit Policy and Compliance Gate:** affordability limits, eligibility, concentration, conduct, legal, contractual and risk-appetite rules.
4. **Action layer:** approve, set a limit, request evidence, send a reminder, offer a payment-date change, restructure, freeze a draw, transfer to workout, initiate a governed recovery strategy or close.

This separation creates traceability. It also prevents a statistical convention from being described as law, or a legal restriction from being treated as just another model feature. Every action should carry a reason code showing the evidence, model version, policy version and decision authority.

Production scoring should use an approved, versioned model artefact. Computationally intensive posterior estimation, cross-fitting and recalibration belong offline. Online systems should calculate governed features, retrieve the approved posterior or scoring representation, evaluate policy rules and record the result. That design reduces latency and makes exact historical reproduction possible.

## 6. Intervene before delinquency, then learn causally

Continuous monitoring is useful only if it leads to proportionate, testable interventions. A falling income trajectory may justify a reminder timed to expected receipts, a lower undrawn limit, a voluntary payment-date change or a temporary restructuring assessment. It should not automatically trigger harassment or an unexplained adverse decision.

Observed collection outcomes are affected by earlier actions. Customers selected for intensive contact may appear riskier because they were selected, not because the contact caused the risk. A simple correlation between an intervention and repayment can therefore mislead. Lenders should use randomised pilots where lawful and ethical, or credible quasi-experimental designs, to estimate incremental treatment effects. Champion-challenger programmes should compare net cash outcomes, customer harm, complaints and recurrence, not merely short-term promises to pay.

Every treatment needs eligibility rules, contact-frequency limits, a customer explanation, an exit condition and a rollback mechanism. Restructuring should be reserved for borrowers with a credible path to viability and should align revised payments with expected cash flow. Otherwise it can become evergreening, which delays recognition without restoring repayment capacity. The World Bank recommends distinguishing viable borrowers suitable for restructuring from non-viable cases requiring orderly resolution, and warns against repeated rollovers that conceal asset quality [9].

Specialised workout teams can improve accountability for distressed exposures. They should be operationally separate from originators, supported by complete cash-flow and collateral data, and measured on sustainable outcomes. Recovery strategy should consider consensual cure, restructuring, collateral or guarantee realisation, legal enforcement, sale and write-off as distinct tools, each with time, cost and conduct implications.

## 7. Fair collection is a risk control

Sustainable collectability is incompatible with abusive recovery. Kenya's Digital Credit Providers Regulations prohibit threats, violence, shaming, unauthorised contact with a customer's phone contacts, unconscionable tactics, harassment, oppression and abuse. They also require transaction acknowledgements, complaint channels and complaint records, with unresolved complaints generally to be resolved within 30 days [10]. These are not public-relations details. They are production requirements for collection systems, agents and outsourced service providers.

The Data Protection Act requires lawful, fair and transparent processing, purpose limitation, data minimisation, accuracy and appropriate retention. It also gives data subjects protections concerning solely automated decisions with legal or similarly significant effects [11]. The General Regulations require meaningful information about automated logic and consequences, appropriate mathematical or statistical procedures, error controls, measures against discriminatory effects and access to human intervention [12].

Accordingly, a lender should maintain:

- lawful-purpose and necessity assessments for each data source;
- data-protection impact assessments where required;
- adverse-action and intervention explanations that customers can understand;
- human review paths with real authority;
- fairness testing by relevant segment and outcome;
- controls over contact channel, frequency, language and time;
- vulnerability and hardship protocols;
- complaint-root-cause analysis linked to product and model changes;
- oversight of collection agencies using the same standards as internal teams.

The balanced objective is not maximum immediate recovery. It is the highest sustainable, lawful risk-adjusted value after customer harm, complaint risk, operating cost and long-term relationship effects are considered.

## 8. Connect realised cash to accounting, capital and funding

Collections data should flow back into finance and risk. IFRS 9 expected credit loss is not a collections target, and the 12-month ECL is not simply the cash expected to be missed in the next twelve months. The standard requires an unbiased, probability-weighted amount, the time value of money and reasonable and supportable historical, current and forward-looking information [13]. Collection timing, cures, modifications, prepayments, collateral proceeds and workout costs affect expected cash shortfalls and therefore need reconciled data.

The institution should maintain separate but connected views:

- operational arrears and treatment state;
- regulatory or contractual default definition;
- accounting stage and ECL;
- risk appetite and economic capital;
- liquidity and funding cash flow;
- securitisation or receivables-finance eligibility, where relevant.

For a funded portfolio or a ring-fenced special-purpose vehicle (SPV) holding eligible receivables through controlled collection accounts, investors are not protected by a headline PD alone. They receive cash after collection lags, servicing expenses, workout costs, recoveries, reserves and the priority of payments. Cohort-level models should project monthly scheduled collections, prepayments, defaults, recoveries and costs into a cash waterfall. Stress tests should vary default incidence, timing, recovery rate, recovery lag, utilisation, concentration and operating costs. Covenants and early-amortisation triggers should respond to calculated asset performance, not optimistic narrative.

Economic capital should similarly reflect the tail of the loss distribution and concentration, not merely expected loss. Repeated exposure to the same platform, geography, supply chain or income shock can make defaults dependent. Portfolio decisions should therefore consider correlated stress and the timing of cash depletion, with model uncertainty disclosed rather than buried.

## 9. Replace the origination dashboard with a lifecycle scorecard

Boards and executives should still see disbursement, approval and turnaround time. They should see them beside metrics that reveal whether the credit promise was fulfilled. A practical scorecard includes:

- first-payment default, by vintage and product;
- 1, 7, 30, 60 and 90 days-past-due roll rates;
- cure rate and re-default after cure;
- promise-to-pay kept rate, with a defined observation period;
- modification rate and post-modification performance;
- gross cash collected against contractually due cash;
- net present value of recovery after workout cost and delay;
- time to cure, recovery or resolution;
- realised loss and observed-to-expected loss by vintage;
- complaints, contact-policy breaches and adverse fairness outcomes;
- intervention uplift compared with a credible control;
- ECL coverage, capital consumption and funding-covenant headroom.

The formulas must declare their denominators. For example:

**Collection efficiencyₜ = cash settled and retained in period t ÷ contractual cash due in period t**

The denominator policy must state how prepayments, modifications, disputed amounts, reversals and sold accounts are treated.

Net recovery should recognise time and cost:

**Net recovery value = ∑ⱼ₌₁ᴶ [(recovery cashⱼ − direct workout costⱼ) ÷ (1 + r)ᵗʲ]**

Here, r is the discount rate and tⱼ is the elapsed time to recovery cash flow j, expressed consistently with that rate.

A cure should be tested for durability:

**Durable cure rate = cured accounts remaining current after h months ÷ accounts classified as cured**

No universal value of (h) is correct for every product. It should reflect payment frequency, tenor and governance policy.

## 10. A practical implementation sequence

During the first 90 days, define the credit lifecycle, data dictionary and decision responsibilities. Reconcile due, paid, reversed, modified, recovered and written-off amounts to the general ledger. Freeze metric definitions and produce vintage reporting. Review product affordability, repayment timing, contact practices and incentive structures. Establish a cross-functional committee including credit, collections, finance, data, compliance, customer operations and model risk.

From 90 to 180 days, implement early-warning features and a governed case-management workflow. Separate inference from policy. Introduce reason codes, treatment eligibility, complaint integration and manual review. Pilot a small number of supportive interventions with control groups. Build fixed-horizon PD, timing and state-transition benchmarks before introducing complex models.

From 180 to 365 days, validate hierarchical or machine-learning challengers, quantify treatment uplift, integrate cash-flow outcomes into IFRS 9 and capital processes, and connect portfolio performance to funding and covenant reports. Establish independent validation, change control, monitoring thresholds, model-use restrictions and periodic policy review. Scale only interventions that improve net cash and customer outcomes together.

## Conclusion

The debate should move beyond whether lenders celebrate disbursement more than collection. The deeper question is whether the institution's product, data, model, policy and operating design make sustainable collection likely from the beginning.

Good credit architecture works backward from realised cash without reducing borrowers to recovery targets. It asks whether the repayment structure fits the activity being financed, whether deterioration can be detected before arrears harden, whether an intervention genuinely changes the outcome, whether customers are treated lawfully and fairly, and whether the resulting cash flows reconcile to expected loss, capital and funding.

Origination remains important. Credit cannot support enterprise and households unless it is extended. But a disbursement is the start of the underwriting evidence, not its conclusion. The true performance record is written afterward, in payments that remain affordable, interventions that restore viability, recoveries measured net of time and cost, and losses recognised without delay.

That is the standard worth institutionalising:

> Underwrite for sustainable collection, monitor for timely support, and measure success in realised, risk-adjusted cash and fair customer outcomes.

## References

[1] F. Lagat, “MSMEs borrow KSh245.1B in the first half of 2026,” *People Daily*, Aug. 19, 2026. [Online]. Available: https://peopledaily.digital/business/msmes-borrow-ksh245-1b-in-the-first-half-of-2026/amp. [Accessed: Aug. 30, 2026].

[2] Central Bank of Kenya, *Commercial Banks' Credit Officer Survey: Quarter Ended March 31, 2026*. Nairobi, Kenya: CBK, 2026. [Online]. Available: https://www.centralbank.go.ke/uploads/banking_sector_reports/1537159667_Credit%20Officer%20Survey%20Report%20-%20March%202026.pdf. [Accessed: Aug. 30, 2026].

[3] C. Mwaniki, “Bank loan defaults rise by Sh21bn despite lower credit cost,” *Business Daily*, Apr. 9, 2026. [Online]. Available: https://www.businessdailyafrica.com/bd/economy/bank-loan-defaults-rise-by-sh21bn-despite-lower-credit-cost-5418306. [Accessed: Aug. 30, 2026].

[4] Kenya Bankers Association, “MSME Credit Analysis: Loan Performance,” Jun. 2026. [Online]. Available: https://msmedata.kba.co.ke/kba/loan-performance. [Accessed: Aug. 30, 2026].

[5] Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*. Basel, Switzerland: Bank for International Settlements, Apr. 2025. [Online]. Available: https://www.bis.org/bcbs/publ/d595.pdf. [Accessed: Aug. 30, 2026].

[6] Basel Committee on Banking Supervision, *Principles for Effective Risk Data Aggregation and Risk Reporting*. Basel, Switzerland: Bank for International Settlements, Jan. 2013. [Online]. Available: https://www.bis.org/publ/bcbs239.pdf. [Accessed: Aug. 30, 2026].

[7] Board of Governors of the Federal Reserve System, “SR 26-2: Revised Guidance on Model Risk Management,” Apr. 17, 2026. [Online]. Available: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm. [Accessed: Aug. 30, 2026].

[8] E. Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1. Gaithersburg, MD, USA: National Institute of Standards and Technology, Jan. 2023, doi: 10.6028/NIST.AI.100-1. [Online]. Available: https://doi.org/10.6028/NIST.AI.100-1. [Accessed: Aug. 30, 2026].

[9] World Bank, *World Development Report 2022: Finance for an Equitable Recovery*, ch. 2. Washington, DC, USA: World Bank, 2022. [Online]. Available: https://www.worldbank.org/en/publication/wdr2022/brief/chapter-2-resolving-bank-asset-distress. [Accessed: Aug. 30, 2026].

[10] Central Bank of Kenya, *The Central Bank of Kenya (Digital Credit Providers) Regulations, 2022*, Legal Notice No. 46. Nairobi, Kenya, 2022. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2022/03/L-.N.-No.-46-Central-Bank-of-Kenya-Digital-Credit-Providers-Regulations-2022.pdf. [Accessed: Aug. 30, 2026].

[11] Republic of Kenya, *Data Protection Act, 2019*, No. 24 of 2019. Nairobi, Kenya: Kenya Law, 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24. [Accessed: Aug. 30, 2026].

[12] Republic of Kenya, *The Data Protection (General) Regulations*, Legal Notice No. 263 of 2021. Nairobi, Kenya: Kenya Law, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31. [Accessed: Aug. 30, 2026].

[13] International Accounting Standards Board, *IFRS 9 Financial Instruments*. London, UK: IFRS Foundation, 2022 issued standards. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-9-financial-instruments.pdf?bypass=on. [Accessed: Aug. 30, 2026].

*This article provides industry analysis and design recommendations. It is not legal, accounting or investment advice. Institutions should apply Kenyan requirements and other applicable rules to their own licences, products, contracts and customers.*
