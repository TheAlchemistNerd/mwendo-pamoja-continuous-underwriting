# Underwrite for Collection in the KESONIA Era

## Connecting transparent pricing to durable credit performance

**By Neville Maloba**  
**Candidate article for editorial consideration by the Kenya Bankers Economic Bulletin**  
**Draft date:** 2 September 2026

> Credit pricing becomes complete when the benchmark, borrower terms, repayment design, monitoring, intervention, and realised cash outcome can be understood as one governed lifecycle.

Kenya's revised risk-based credit-pricing framework creates an important opportunity. A variable lending rate can now be explained through a visible market reference, a bank-specific pricing premium, and disclosed fees and charges. That separation can strengthen price discovery, comparability, and monetary-policy transmission. It can also improve the conversation between the lender and the customer about why credit costs what it does.

The economic test continues after the loan is disbursed. The borrower must generate cash at the right time, the payment schedule must remain compatible with that cash, deterioration must be recognised early, and any intervention must produce a sustainable improvement. The lender must then translate the resulting payment, cure, default, and recovery experience into expected credit loss, capital, liquidity, and the next pricing decision.

This is the practical meaning of underwriting for collection. It is not a call for more forceful recovery. It is a proposal to design credit around fair and sustainable collectability from the beginning.

## A benchmark starts the pricing story

The Central Bank of Kenya describes the revised public pricing relationship as:

**Total lending rate = KESONIA + K_RBCP**

**Total cost of credit = KESONIA + K_RBCP + fees and charges**

KESONIA is the transaction-based, volume-weighted average rate for unsecured overnight Kenya shilling interbank transactions. CBK began publishing KESONIA and a compounded index on 1 September 2025. The revised framework applied to new variable-rate loans from that date and to existing variable-rate loans from 28 February 2026 [1], [2].

The bank-specific premium, K_RBCP, incorporates lending-related operating costs, shareholder return, and the borrower's risk profile [2]. This definition matters. The premium is not simply a probability of default converted into a percentage. Credit risk may be informed by probability of default, loss given default, exposure, concentration, and uncertainty, but the published premium also reflects the economics of originating and maintaining the facility and the return required by the institution.

Transparent decomposition creates a basis for better questions. How quickly does a KESONIA movement reach the customer's rate? Does the product reset daily, monthly, or at another contractual interval? Which observation, lookback, compounding, day-count, floor, cap, and fallback conventions apply? How much of a change in total cost comes from the market benchmark, the bank premium, or fees? Do product disclosures remain current as rates change?

These questions should be answered before the lender moves to behavioural models. A precisely estimated credit score cannot compensate for an ambiguous contract or a pricing record that cannot be reproduced.

## Disbursement and performance need a shared denominator

Credit markets naturally celebrate new lending. Disbursement is immediate and visible. It expands the loan book and demonstrates support for households and enterprises. Credit deterioration emerges later, across different vintages and reporting systems. That timing difference can separate the teams that create the exposure from those that manage its consequences.

Public lending and NPL figures illustrate the need for disciplined interpretation. New credit during a period is a flow. Outstanding loans and gross NPLs on a reporting date are stocks. An NPL ratio adds a denominator, while an account-based NPL share answers a different question from a value-based ratio. A large number of small delinquent accounts can dominate the count even when a smaller number of large facilities dominate value.

The useful policy question is therefore not whether a current lending-flow announcement can be compared directly with the banking sector's accumulated NPL stock. It is how the newly originated vintages perform as they season. That requires records connecting the same population through disbursement, scheduled payment, actual payment, arrears, cure, modification, default, recovery, and closure.

The KBA MSME Credit Dashboard already demonstrates the value of keeping product, borrower, count, balance, and performance views distinct [3]. A lifecycle research infrastructure can extend this discipline by preserving origination vintage, contractual schedule, state transitions, and recovery timing.

## Collection begins in product design

Many collection problems are created before an account enters arrears. A repayment date may not align with the borrower's receipt cycle. A working-capital loan may amortise faster than the inventory cycle. A revolving limit may permit utilisation that becomes difficult to reverse when income weakens. Multiple deductions may compete for the same cash. A restructure may reduce the current instalment without restoring long-term viability.

Underwriting for collection begins with product questions:

- What economic activity produces repayment cash?
- When is that cash expected to arrive?
- How variable and concentrated is it?
- Which essential operating and household costs must be paid first?
- How much residual liquidity remains after debt service?
- How would a benchmark increase affect the instalment or total repayment burden?
- Which shocks could interrupt the cash-generating activity?
- Which modification would restore viability if one of those shocks occurs?

This reasoning is especially relevant to MSMEs. Revenue can be seasonal, concentrated in a few customers, sensitive to inventory and fuel costs, and entangled with household cash flow. A monthly income average can therefore hide a weekly or daily liquidity shortage.

Good product design does not require the lender to collect every available data point. It requires the institution to identify the evidence necessary for a specific economic question, collect it lawfully, and explain how it affects the decision. Data minimisation, customer consent where applicable, accuracy, and purpose limitation remain part of the risk design. This lifecycle view also reflects the Basel Committee's connection between the credit-granting process, ongoing administration and monitoring, remedial management, and control [4].

## Build one event-time account history

A lender cannot reliably evaluate collectability if the loan's history is fragmented across origination, core banking, payment, collection, CRM, restructure, CRB, and general-ledger systems. A canonical event-time record should preserve:

- application, offer, acceptance, and disbursement;
- contractual amount due and due date;
- payment initiation, settlement, allocation, and reversal;
- principal, interest, fee, and penalty components;
- days past due and credit state;
- limit changes and additional drawings;
- contact, approved intervention, and customer response;
- modification, restructuring, and forbearance;
- write-off, gross recovery, collection cost, and net recovery;
- model version, policy version, reason code, and human override.

Each event needs an effective timestamp, processing timestamp, source, and correction history. These distinctions support both operational truth and research integrity. A model must be trained on information that existed when the decision was made. If a later reversal, restructure, or recovery is allowed to leak into an earlier score, the apparent predictive improvement will not survive production.

The same record supports reconciliation. Opening balance, disbursement, accrued amounts, payments, reversals, write-offs, and closing balance should form an explainable cash bridge. Aggregated account values should reconcile to finance control totals. Data excluded from analysis should be reported by account count and balance.

## Behavioural scoring belongs inside the lifecycle

Traditional origination models remain necessary. They evaluate the customer and product before performance evidence exists. Behavioural scoring becomes valuable after disbursement because it can observe whether the account is moving toward or away from the conditions assumed at approval.

Useful indicators may include repayment velocity, scheduled-to-actual payment ratio, utilisation, balance volatility, time since a full payment, and the durability of a prior cure. Where cash-flow information is lawfully available, the lender may evaluate the timing and stability of receipts relative to essential expenditure and debt service.

Artificial intelligence can extend this evidence. Neural-network models can learn representations from permitted sequences of transactions, payments, and account states. Their role should be incremental and testable. Explicit variables retain defined windows, denominators, timestamps, and economic meanings. Learned representations should be trained out of sample, checked for duplicated signal, and accepted only when they improve future-vintage calibration and economic decisions over a transparent benchmark.

The modelling sequence can remain practical:

1. Estimate whether a defined delinquency or default event will occur within a governed horizon.
2. Estimate when deterioration may occur.
3. Model movement among current, early-arrears, late-arrears, cure, restructure, default, write-off, and recovery states.
4. Estimate exposure when the event occurs.
5. Estimate the amount, cost, and timing of recovery.

Hierarchical models can share evidence across products, sectors, geographies, and vintages while allowing well-observed groups to differ. Nonlinear relationships can be represented by governed splines. Model uncertainty can guide referral or evidence gathering where the estimate is not sufficiently precise. The result is a richer view of collectability without making a single score responsible for the entire customer relationship.

## Keep prediction, policy, and intervention separate

A model estimates an outcome. Credit policy determines what the institution permits. An intervention changes the customer's experience. The subsequent payment and customer outcomes show whether that action worked.

A clear architecture has five stages:

**Observed evidence -> estimated risk and uncertainty -> credit-policy constraints -> authorised intervention -> measured outcome**

This separation makes decisions challengeable. It prevents a model threshold from becoming an unwritten policy and prevents a policy preference from being presented as a statistical fact. Every material action should record the evidence, model version, policy version, decision authority, and reason communicated to the customer where appropriate.

Possible early actions include a reminder timed to expected receipts, a payment-date alignment, a temporary limit adjustment, an affordability review, a restructure assessment, or referral to a trained relationship or workout team. Eligibility, contact frequency, customer choice, exit conditions, and escalation must be governed.

The value of an intervention should be measured causally where possible. Customers selected for an action are often already different from customers who are not selected. A repayment following a call does not by itself prove that the call caused the payment. Randomised pilots, governed phased rollout, or credible quasi-experimental comparisons can estimate incremental effects. For digital credit, action design must also respect Kenya's restrictions on abusive collection conduct [5] and the lawful, fair, purpose-limited processing and automated-decision safeguards established by data-protection law [6].

The outcome should be durable. A cure that returns to arrears after one instalment is different from a cure sustained for six or twelve months. A short-term cash receipt may be uneconomic after contact, legal, or repossession costs. Intervention evaluation should therefore include cure, re-default, discounted net recovery, cost, complaints, hardship outcomes, and access effects.

## Connect collection evidence to finance

The same lifecycle evidence should reach accounting, capital, treasury, and funding decisions.

For IFRS 9, expected credit loss reflects probability-weighted cash shortfalls, the time value of money, and reasonable and supportable information [7]. Cure, modification, prepayment, recovery timing, and workout cost affect those cash shortfalls. The operational collection ledger and the accounting model must therefore reconcile without becoming identical. Days past due, regulatory default, IFRS 9 stage, internal watchlist, and collection treatment may have different definitions and purposes.

Economic capital extends the analysis from expected loss to adverse loss distributions and concentration. A portfolio may be exposed to the same sector, platform, geography, supply chain, commodity price, or macroeconomic shock. Dependence can weaken the benefit of diversification precisely when liquidity is most important.

Funds-transfer pricing should reflect the tenor and repricing behaviour of the asset, liquidity consumption, and basis risk between the lending contract and the institution's funding. If the customer's asset rate resets differently from the funding benchmark, the margin can change even when credit performance is stable.

Where receivables support a ring-fenced funding vehicle, the analysis becomes a monthly cash-flow question. Investors receive cash after scheduled collection, delinquency, recovery lag, servicing expense, reserves, and the priority of payments. Eligibility, advance rate, overcollateralisation, concentration, reserve requirements, and early-amortisation triggers should be linked to observed asset behaviour.

## A lifecycle scorecard for management

Origination volume, approval rate, and turnaround time should remain visible. They should sit beside measures that show what happened afterward:

- first-payment default by product and vintage;
- roll rates through 1, 30, 60, and 90 days past due;
- cure and re-default after cure;
- modification rate and post-modification performance;
- contractual cash due and cash settled;
- gross recovery, direct workout cost, and discounted net recovery;
- time to cure, recovery, or resolution;
- realised and expected loss by vintage;
- intervention uplift relative to a credible comparison;
- complaints, contact breaches, and customer-harm indicators;
- ECL coverage, capital consumption, and funding headroom.

Every metric should publish its population, date, observation window, numerator, denominator, value or count basis, and treatment of modifications, prepayments, disputes, and reversals. This makes the scorecard a management tool rather than a collection of attractive percentages.

## An industry research agenda

The KESONIA era creates a natural programme of collaborative research for banks, KBA, CBK, CRBs, fintechs, and development partners.

First, public product-pricing histories can show benchmark pass-through, repricing lags, and dispersion in the bank-specific premium and total cost of credit. Second, anonymised vintage data can connect new MSME lending to subsequent credit performance using consistent populations and denominators. Third, common definitions of cure, re-default, modification, recovery cost, and discounted net recovery can improve comparability. Fourth, intervention trials can identify which supportive actions restore repayment capacity. Fifth, the results can be connected to ECL, capital, liquidity, and credit de-risking.

The research should begin with transparent models and add complexity only when it changes a decision. It should preserve point-in-time data, report uncertainty, test future vintages, and examine access and fairness alongside portfolio value.

## Conclusion

KESONIA strengthens the architecture of credit pricing by giving the market benchmark a visible and reproducible role. Lifecycle underwriting can extend that discipline from the first price quotation to the final cash outcome.

The practical objective is not to make every customer predictable. It is to make the institution's reasoning coherent. The lender should be able to explain the benchmark, premium, fees, repayment design, observed deterioration, permitted response, customer treatment, accounting consequence, and realised recovery as connected but distinct decisions.

That is how lending growth and asset quality can be considered together. Underwrite for sustainable collection, intervene while viability can still be restored, and measure success through durable, risk-adjusted cash and fair customer outcomes.

## References

[1] Central Bank of Kenya, “Kenya Shilling Overnight Interbank Average,” 2026. [Online]. Available: https://www.centralbank.go.ke/kesonia/. [Accessed: Sep. 2, 2026].

[2] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*. Nairobi, Kenya: CBK, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. [Accessed: Sep. 2, 2026].

[3] Kenya Bankers Association, “MSME Credit Analysis Dashboard,” 2026. [Online]. Available: https://msmedata.kba.co.ke/. [Accessed: Sep. 2, 2026].

[4] Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*. Basel, Switzerland: Bank for International Settlements, Apr. 2025. [Online]. Available: https://www.bis.org/bcbs/publ/d595.pdf. [Accessed: Sep. 2, 2026].

[5] Central Bank of Kenya, *The Central Bank of Kenya (Digital Credit Providers) Regulations, 2022*, Legal Notice No. 46. Nairobi, Kenya, 2022. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2022/03/L-.N.-No.-46-Central-Bank-of-Kenya-Digital-Credit-Providers-Regulations-2022.pdf. [Accessed: Sep. 2, 2026].

[6] Republic of Kenya, *Data Protection Act, 2019*. Nairobi, Kenya: Kenya Law, 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2022-12-31. [Accessed: Sep. 2, 2026].

[7] IFRS Foundation, “IFRS 9 Financial Instruments,” 2026. [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/. [Accessed: Sep. 2, 2026].
