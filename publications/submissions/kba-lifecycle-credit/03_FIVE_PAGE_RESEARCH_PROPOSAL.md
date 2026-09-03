# From KESONIA to Sustainable Collection

## Risk-Based Pricing, MSME Credit Quality and Lifecycle Underwriting in Kenya

**Author:** Neville Maloba  
**Affiliation:** Independent researcher  
**Email:** nevillemaloba@gmail.com  
**Proposed KBA theme:** Monetary Policy and Bank Credit Pricing Dynamics  
**Secondary track:** Methodological Session

## Abstract

Kenya's revised risk-based credit-pricing framework anchors variable lending rates to the Kenya Shilling Overnight Interbank Average, or KESONIA, while retaining a bank-specific premium and disclosed fees and charges. The framework improves benchmark transparency and monetary-policy transmission, but the economic performance of a loan is determined after disbursement through payment timing, utilisation, cure, modification, delinquency, default, collection cost, and recovery. This study asks how KESONIA changes are transmitted into bank-product pricing and how lifecycle underwriting can improve the connection between transparent pricing, MSME credit access, durable collection, and non-performing-loan management.

The research has two linked empirical layers. The first constructs a public panel from Central Bank of Kenya KESONIA and CBR series, commercial-bank weighted average rates, Kenya Bankers Association Total Cost of Credit disclosures, the KBA MSME Credit Dashboard, Credit Officer Surveys, and official macroeconomic controls. It will estimate benchmark pass-through, repricing lags, and bank-product dispersion while distinguishing new lending flows, outstanding balances, NPL stocks, and NPL ratios. The second layer, subject to an institutional data partnership, will use anonymised account or cohort histories to model transitions among current, early-arrears, late-arrears, cure, restructure, default, write-off, and recovery states. It will compare an origination-only model with lifecycle hazard or multistate specifications and test whether post-disbursement indicators add out-of-vintage information about delinquency, durable cure, and discounted net recovery.

The study's contribution is a measurement bridge between benchmark reform and collectability. It treats collection as a design property of the loan and separates prediction, credit policy, intervention, and realised outcome. Hierarchical pooling and governed nonlinear effects will be introduced where supported by the data. Advanced behavioural or neural representations will be assessed only for incremental calibration and economic value over transparent variables. Intervention effects will be interpreted causally only where assignment and comparison are defensible.

The expected outputs are implementable recommendations for pricing governance, early warning, restructuring, fair collection, IFRS 9, economic capital, funds-transfer pricing, and credit de-risking. The paper is intended to help Kenyan institutions expand credit on terms that remain transparent at origination and sustainable through collection.

**Keywords:** KESONIA; risk-based credit pricing; MSME finance; lifecycle underwriting; non-performing loans; collections; cure; recovery; IFRS 9

## 1. Motivation and policy relevance

Kenya's transition to KESONIA-anchored variable lending creates an opportunity to examine how a transparent market benchmark reaches borrowers and how bank-specific pricing responds [1]. The Central Bank of Kenya defines the public pricing relationship as the applicable reference rate plus a bank-specific risk-based credit-pricing premium, with fees and charges added to obtain total cost of credit. The premium incorporates lending-related operating costs, shareholder return, and the borrower's risk profile [2]. It should therefore not be interpreted as a default-probability coefficient or expected-loss charge alone.

Benchmark transparency addresses only part of the credit problem. A loan that appears acceptable at origination can deteriorate when revenue, expenditure, liquidity, utilisation, or repayment behaviour changes. A lender that sees those changes only through conventional arrears buckets learns late. Conversely, behavioural information used without clear definitions, consent, validation, and policy boundaries can amplify exclusion or create interventions that appear effective because the highest-risk customers were never offered them.

The proposed study joins pricing transmission and collectability. It follows a facility from the applicable benchmark and premium through disbursement, contractual payment, observed payment behaviour, intervention, cure, re-default, default, recovery, and closure. The resulting evidence can inform pricing, approval, limit management, collection strategy, modification, IFRS 9 expected credit loss, economic capital, liquidity, and funding. This is directly relevant to KBA's stated interest in risk-based pricing, credit growth, access, NPL-management schemes, and credit de-risking [3].

## 2. Research questions and hypotheses

The primary question is:

> How does Kenya's transition to KESONIA-anchored risk-based pricing affect pricing transmission, MSME credit access, and loan collectability, and how can a lifecycle-underwriting framework improve the connection between origination, early intervention, durable cure, and net recovery?

The empirical work will test four hypotheses, subject to data availability:

**H1: Benchmark transmission.** Changes in the applicable reference rate transmit into variable lending rates with measurable lags and material heterogeneity across bank-product combinations.

**H2: Pricing dispersion.** Published credit-pricing premiums remain materially dispersed after accounting for benchmark basis and observable product characteristics. The study will describe this dispersion without treating it as a pure measure of credit risk because operating cost, customer risk, product design, and required return can all contribute.

**H3: Lifecycle information.** Properly timed post-disbursement indicators add out-of-vintage information about delinquency, cure, and recovery beyond origination-only variables.

**H4: Intervention value.** Targeted early interventions improve durable cure or discounted net recovery relative to comparable untreated accounts without disproportionate deterioration in access or customer outcomes.

H4 will remain a research proposition unless the data include intervention assignment and an appropriate comparison design.

## 3. Data

The public-data layer will combine:

- Daily KESONIA, the compounded KESONIA index, and CBR decisions from CBK.
- Monthly commercial-bank weighted average lending, overdraft, deposit, and savings rates.
- CBK Credit Officer Surveys covering demand, standards, NPL expectations, recovery activity, and sector conditions [4].
- KBA MSME Credit Dashboard measures of outstanding credit, loan performance, product, borrower type, gender, and other available dimensions, interpreted according to the dashboard methodology [5].
- KBA Total Cost of Credit observations on benchmark basis, product rate, published premium, fees, charges, and update date [6].
- Official inflation, exchange-rate, Treasury-yield, fuel-price, activity, and fiscal controls where relevant.

Each observation will retain source, retrieval date, observation date, unit, definition, and revision status. Missing Total Cost of Credit entries and asynchronous product updates will be analysed rather than silently discarded.

The institution-data layer will seek anonymised account or cohort records containing origination terms, benchmark basis, reset dates, schedule, amount due, amount paid, days past due, utilisation, modification, cure, re-default, write-off, recovery, collection cost, and approved intervention history. Direct identifiers will not enter the research environment. The data partnership will specify lawful purpose, minimisation, access, retention, disclosure review, and publication thresholds.

If institution data are unavailable, a synthetic portfolio will be used only to demonstrate model mechanics. Its assumptions and calibration targets will be published, and its results will not be treated as evidence about Kenyan borrowers.

## 4. Methodology

### 4.1 Pricing transmission

The analysis will first reconstruct the public pricing identity:

```text
Published lending rate = applicable reference rate + K_RBCP
Published total cost of credit = lending rate + fees and charges
```

It will describe cross-bank and cross-product distributions, benchmark choices, repricing dates, premium movements, and total-cost dispersion. Distributed-lag panel models will estimate how changes in the applicable benchmark reach published product rates. Bank-product effects will absorb stable product characteristics. Macroeconomic controls and documented product changes will be added where identifiable.

The implementation dates of 1 September 2025 for new variable-rate loans and 28 February 2026 for existing variable-rate loans provide event anchors. They will not automatically be treated as causal experiments. The study will assess pre-trends, observation length, adoption heterogeneity, concurrent policy changes, and available comparison groups before making any causal interpretation.

### 4.2 Lifecycle performance

The lifecycle study will begin with an origination-only logistic or scorecard benchmark. It will then estimate discrete-time hazard or multistate transition models for movement among current, early arrears, late arrears, cure, restructure, default, write-off, and recovery. Outcomes will include first-payment default, 30-day and 90-day delinquency, time to default, cure within a stated horizon, re-default following cure, gross recovery, recovery delay, collection expense, and discounted net recovery.

Candidate time-varying variables include repayment velocity, scheduled-to-actual payment ratio, utilisation, balance volatility, time since full payment, prior cure durability, and lawful cash-flow indicators. Features will be reconstructed as they were known at the decision time. Post-outcome and post-intervention information will be excluded from earlier scores.

Hierarchical effects may pool across products, institutions, sectors, geographies, and vintages. Governed P-splines may capture nonlinearities. Pólya-Gamma augmentation may support efficient offline Bayesian inference while preserving hierarchical pooling. Neural behavioural representations will be cross-fitted, residualised against explicit variables, regularised, and retained only if they add stable out-of-vintage value.

### 4.3 Intervention and validation

Where intervention data exist, the preferred design is randomised or phased implementation. Otherwise, the study will consider staggered adoption, matching, propensity weighting, doubly robust estimation, or a valid threshold design. Contact attempts or short-lived repayment will not be accepted as the principal outcome. The analysis will measure durable cure, re-default, net recovery after cost, customer complaints or hardship outcomes where available, and access effects.

Validation will report deviance or log loss, Brier score, calibration intercept and slope, observed-to-expected outcomes, precision-recall measures, vintage stability, covariate shift, posterior-predictive coverage where applicable, and incremental value over the origination-only model. Economic validation will report expected cash-loss error, intervention value net of cost, ECL sensitivity, and capital consequences.

## 5. Expected contribution and recommendations

The research will contribute:

1. A documented view of KESONIA pricing transmission and public bank-product dispersion.
2. A lifecycle definition of successful underwriting based on sustainable cash collection rather than disbursement alone.
3. A model that separates the probability and timing of deterioration, exposure, cure, recovery, and collection cost.
4. A governance architecture that separates prediction, policy constraints, authorised intervention, and measured outcome.
5. Practical links from realised credit cash flow to IFRS 9, economic capital, funds-transfer pricing, and credit de-risking.

Potential recommendations will be tested against the evidence. They may include stronger publication of product repricing histories; shared definitions for cure, re-default, and net recovery; point-in-time lifecycle data standards; intervention-effect measurement; fair-treatment monitoring; and bank dashboards that report collection and recovery outcomes alongside origination volumes.

## 6. Work plan and outputs

The work will proceed through public-data construction, partner-data acquisition, descriptive analysis, lifecycle modelling, robustness testing, and policy translation. Deliverables will include the full research paper, a two to four-page policy brief, a reproducible analytical package, and a shorter practitioner article for an outlet confirmed by KBA.

## Selected references

[1] Central Bank of Kenya, “Kenya Shilling Overnight Interbank Average,” 2026. [Online]. Available: https://www.centralbank.go.ke/kesonia/

[2] Central Bank of Kenya, “Revised Risk-Based Credit Pricing Model,” Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf

[3] Kenya Bankers Association, “15th Annual Banking Research Conference: Call for Papers,” Mar. 2026. [Online]. Available: https://www.kba.co.ke/wp-content/uploads/2026/03/KBA-Call-for-Papers-2026-Advert-3.pdf

[4] Central Bank of Kenya, “Bank Supervision and Banking Sector Reports,” 2026. [Online]. Available: https://www.centralbank.go.ke/reports/bank-supervision-and-banking-sector-reports/

[5] Kenya Bankers Association, “MSME Credit Analysis Dashboard,” 2026. [Online]. Available: https://msmedata.kba.co.ke/

[6] Kenya Bankers Association, “Total Cost of Credit,” 2026. [Online]. Available: https://www.costofcredit.co.ke/site/interest-rate
