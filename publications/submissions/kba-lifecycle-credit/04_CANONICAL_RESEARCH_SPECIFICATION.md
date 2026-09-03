# Canonical Research Specification

## 1. Research identity

**Working title:** From KESONIA to Sustainable Collection: Risk-Based Pricing, MSME Credit Quality and Lifecycle Underwriting in Kenya

**Primary audience:** Kenya Bankers Association Research Centre, Kenyan banks, policymakers, credit-risk practitioners, and development-finance institutions.

**Primary contribution:** An evidence-based bridge between transparent benchmark pricing and post-disbursement collectability.

**Unit of analysis:** The unit depends on the research layer:

- Bank-product-month for public pricing transmission.
- Institution-quarter or portfolio-quarter for aggregate credit conditions.
- Account-observation-period or account-state transition for institution-level lifecycle modelling.
- Intervention-eligible account at an explicitly defined decision time for intervention evaluation.

## 2. Primary question

How does Kenya's transition to KESONIA-anchored risk-based pricing affect pricing transmission, MSME credit access, and loan collectability, and how can a lifecycle-underwriting framework improve the connection between origination, early intervention, durable cure, and net recovery?

## 3. Hypotheses and evidence status

| ID | Hypothesis | Minimum evidence | Current status |
|---|---|---|---|
| H1 | Reference-rate changes reach variable product rates with measurable lags and heterogeneous pass-through. | Dated bank-product pricing panel with benchmark basis and repricing observations. | Public-data test planned. |
| H2 | Published `K_RBCP` remains dispersed after observable benchmark and product differences are recognised. | Product definitions, premium values, benchmark basis, update dates, and missingness analysis. | Public-data test planned. |
| H3 | Point-in-time lifecycle indicators add out-of-vintage information about delinquency, cure, and recovery beyond origination variables. | Anonymised account or cohort histories with sufficiently matured outcomes. | Requires institutional partner. |
| H4 | Targeted early interventions improve durable cure or net recovery relative to comparable untreated accounts without disproportionate access or customer harm. | Intervention assignment, timing, cost, outcome, and credible comparison design. | Requires institutional partner or prospective experiment. |

No conclusion will be drafted as a finding until its corresponding evidence and validation are complete.

## 4. Canonical definitions

### 4.1 Pricing

**KESONIA:** The transaction-based, volume-weighted average rate for unsecured overnight Kenya shilling interbank transactions, administered and published by the Central Bank of Kenya.

**Applicable reference rate:** KESONIA for relevant variable-rate lending, or CBR where the revised framework permits its use because KESONIA is impractical or serves as a fallback.

**`K_RBCP`:** The published bank-specific or product-specific premium in the revised risk-based credit-pricing model. It incorporates lending-related operating costs, shareholder return, and the borrower's risk profile. It is not identical to PD, expected loss, economic capital, or FTP.

**Published lending rate:** Applicable reference rate plus `K_RBCP` for the product and observation date.

**Total cost of credit:** Lending rate plus applicable disclosed fees and charges, interpreted using the stated product, amount, and tenor assumptions.

**Contractual accrual rate:** The rate applied to a specific facility according to its contract, including day count, observation convention, compounding, reset, floor, cap, lookback, lag, fallback, and correction rules.

### 4.2 Credit performance

**Origination:** The approved and disbursed credit event. Approval and disbursement will be reported separately where possible.

**Current:** No payment is contractually past due according to the research dataset's end-of-day or end-of-period convention.

**Early arrears:** A prespecified interval after a missed contractual payment but before NPL classification. The main study will report 1 to 30 and 31 to 89 days past due where data support that granularity.

**NPL:** A facility 90 or more days past due or classified Substandard, Doubtful, or Loss according to the applicable prudential and source-data definition. Any alternative source definition will be reported explicitly.

**Cure:** Return from a delinquent state to a defined performing state. The number and value of payments required for cure will be specified.

**Durable cure:** Cure sustained without renewed material delinquency for a fixed evaluation window, provisionally six months and tested at three and twelve months.

**Re-default:** Entry into material delinquency or default after a recorded cure within the defined follow-up window.

**Modification or restructure:** A contractual change recorded separately from cure. Forbearance and non-credit-risk modifications will not be conflated.

**Gross recovery:** Cash recovered after default before directly attributable recovery and collection expenses.

**Net recovery:** Gross recovery less directly attributable collection, legal, repossession, sale, and workout costs.

**Discounted net recovery:** Net recovery discounted from receipt date to the selected valuation date using a documented rate consistent with the analytical purpose.

**Collection efficiency:** Discounted net recovery divided by a documented exposure denominator, accompanied by the time and cost required to obtain it.

### 4.3 Modelling and decisions

**Prediction:** An estimated probability, transition intensity, timing distribution, exposure, or recovery outcome.

**Credit policy:** Approved institutional constraints that translate estimates and contractual facts into permitted decisions.

**Intervention:** An authorised action directed at a customer or account, such as a reminder, payment-date alignment, temporary limit reduction, restructure review, or collection treatment.

**Outcome:** The subsequent observable customer, cash-flow, risk, accounting, or fairness result.

**Lifecycle underwriting:** The governed process that updates credit assessment and action through origination, payment performance, monitoring, intervention, cure, default, recovery, and closure.

## 5. Measures and estimands

### 5.1 Pricing transmission estimands

- Contemporaneous and lagged change in published product rate per one-percentage-point change in the applicable reference rate.
- Time from a benchmark change to the next observed product-rate update.
- Cross-sectional dispersion in `K_RBCP` by bank, product, benchmark basis, and observation date.
- Dispersion in total cost of credit for standardised product examples.
- Share of product records with missing, stale, or internally inconsistent public fields.

### 5.2 Lifecycle estimands

- Probability of first-payment default within a defined horizon.
- Probability and timing of transition from current to early arrears and NPL.
- Probability of cure conditional on current state and elapsed delinquency duration.
- Probability of re-default conditional on cure.
- Expected gross and discounted net recovery conditional on default.
- Expected cash loss over a consistent horizon.
- Incremental out-of-vintage value of lifecycle variables over origination variables.

### 5.3 Intervention estimands

- Average treatment effect within the intervention-eligible population where identification permits.
- Change in durable cure, re-default, and discounted net recovery.
- Intervention cost and net economic value.
- Differences in access, treatment, or outcomes across appropriately defined customer groups.

## 6. Model sequence

1. Descriptive pricing and credit-quality analysis.
2. Bank-product pricing-transmission model.
3. Origination-only credit benchmark.
4. Discrete-time hazard or multistate lifecycle benchmark.
5. Hierarchical pooling across approved grouping dimensions.
6. Governed P-splines for material nonlinear relationships.
7. Optional time effects using AR(1) or RW1 priors where identified.
8. Optional cross-fitted residual neural representation with regularised shrinkage.
9. Optional dependence stress or portfolio aggregation challenger.
10. Intervention-effect analysis using the strongest feasible assignment design.

Pólya-Gamma augmentation is an offline inference strategy for the complete hierarchical logistic model. It supports conditionally Gaussian coefficient blocks and does not remove partial pooling. MCMC or latent-variable sampling will not run during a production credit decision. Production scoring will use an approved posterior artefact or an independently validated approximation.

## 7. Feature ownership and leakage control

Every engineered variable will have one canonical definition, observation timestamp, transformation owner, and use. Explicit liquidity or repayment variables will not be duplicated as named neural inputs. Learned representations may use raw event sequences, but their incremental contribution will be tested after cross-fitting and residualisation against the explicit design matrix.

No feature may use information recorded after the scoring cutoff. Modification, collector action, recovered amount, future payment, final NPL status, and subsequent account closure are outcomes or time-varying events, not origination predictors.

## 8. Evidence boundaries

- Public aggregate data can describe trends, pricing dispersion, and associations. It cannot establish individual borrower transitions.
- A six-month flow of new credit cannot be divided into or compared with a point-in-time stock of sector-wide NPLs as if they were one cohort.
- Public product premiums cannot be interpreted as pure borrower credit-risk charges.
- The September 2025 and February 2026 implementation dates are event anchors, not automatic causal instruments.
- AI, RegTech, ERP, or supervisory interfaces are recommendations unless an official source establishes a current requirement or interface.
- Structural finance and ring-fenced SPVs are possible credit de-risking mechanisms, not necessary features of every MSME loan portfolio.
- Intervention effectiveness requires observed treatment assignment and a defensible counterfactual.

## 9. Validation and approval gates

The primary model cannot advance unless it demonstrates point-in-time correctness, adequate outcome maturity, stable out-of-vintage calibration, interpretable incremental value, and reproducible estimates. An advanced challenger cannot advance unless it improves economic and statistical outcomes over the transparent benchmark without unacceptable stability, fairness, or governance costs.

The full manuscript cannot describe a result until the corresponding analysis has passed data reconciliation, code review, statistical validation, policy interpretation, and disclosure review.

