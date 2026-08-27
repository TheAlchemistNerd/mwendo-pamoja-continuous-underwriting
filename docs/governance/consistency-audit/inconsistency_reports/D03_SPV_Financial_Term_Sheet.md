# D03 Inconsistency Report: SPV Financial Term Sheet

## Document role and semantic synopsis

D03 is the shortest target and is intended to be the controlling commercial summary for the SPV financing. It states a USD 9 million facility, three classes, basic yields, credit enhancements, portfolio triggers, and regulatory alignment. That role gives it higher contractual importance than its length suggests. Yet most terms are headlines rather than operative definitions, and several conflict with the strategic, pricing, and technical papers.

The 75%, 15%, and 10% stack reconciles arithmetically to USD 9 million: Class A USD 6.75 million, Class B USD 1.35 million, and Class C USD 0.90 million. That is a sound starting point. The problem is that Class A's 75% share is adjacent to a 75% advance-rate concept, the benchmark differs from the KESONIA series, the facility currency does not match the asset mechanics, and credit protections are presented without the transaction definitions needed to enforce them.

## Executive inconsistency summary

D03 is not yet a lender-grade term sheet. It lacks definitions of eligible receivables, borrowing base, purchase price, concentration, delinquency, default, recovery, cash available, reserve requirement, permitted investments, amortization, servicing, reporting, events of default, hedging, and conditions precedent. Its most serious inconsistencies are the 91-day T-bill basis versus the canonical KESONIA basis, mixed USD and KES exposure, conflation of tranche percentage and advance rate, and language implying that interventions and first-loss equity guarantee Class A. It also treats PSI and NPL triggers as self-executing without defining calculation or consequence.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D03-I01 | Critical | High | Sections 1 and 2 | Currency and benchmark do not define a coherent debt instrument |
| D03-I02 | Critical | High | Sections 2 and 3 | Capital share, advance rate, and OC are conflated |
| D03-I03 | High | High | Section 2 | T-bill coupon conflicts with KESONIA pricing baseline |
| D03-I04 | Critical | High | Section 3 | Class A guarantee language is unsupported |
| D03-I05 | Critical | High | Sections 1 to 4 | Borrowing-base and waterfall definitions are missing |
| D03-I06 | High | High | Section 4 | Triggers lack definitions, cure, and consequences |
| D03-I07 | High | High | Sections 1 and 3 | True sale, servicing, account control, and hedge terms are absent |
| D03-I08 | High | High | Section 5 | IFRS and ESG statements have no party or test |
| D03-I09 | High | High | Section 5 | Prudential and regulatory language overstates applicability |
| D03-I10 | Medium | High | Throughout | No evidence status, dates, or precedence clause |

## Detailed findings

### D03-I01: The instrument's denomination and cash source are incoherent

**Anchor:** Sections 1 and 2. The facility is presented in USD, while receivables and borrower pricing are in KES and the coupon references a Kenyan T-bill. D01 calls reserve cash a self-hedge; D09 alternates among KESONIA, USD debt, and SOFR-like ideas.

**Impact:** Denomination determines principal repayment, interest accrual, FX gains or losses, reserve currency, hedge needs, tax, accounting, and default tests. A USD principal claim cannot be serviced predictably from unhedged KES cash simply because the term sheet translates the opening amount.

**Canonical resolution:** State that SPV assets, notes, accounts, and waterfall are KES, with USD equivalent shown for investor reporting. If investors require USD notes, include a cross-currency swap or forward programme, hedge counterparty, collateral, replacement trigger, termination payment priority, and stressed hedge cost. Link the election to D01, D09, and the financial model.

### D03-I02: The 75% figure performs three incompatible jobs

**Anchor:** Sections 2 and 3. Class A equals 75% of the capital stack. Elsewhere the corpus calls 75% an advance rate. The term sheet also requires 125% OC without stating whether the denominator is A, A plus B, or total capital.

**Impact:** A borrowing base cannot be monitored and a lender cannot determine collateral deficiency. The current text could imply USD 9 million collateral, USD 12 million collateral, or different protection for Class A and B.

**Canonical resolution:** Preserve Class A as 75% of total capitalization. Define the borrowing-base advance rate separately. Use `eligible receivables / (A + B outstanding)` for OC, with 125% minimum. If the model assumes USD 12 million eligible receivables at close, state that it results from USD 9 million divided by a 75% total-capital funding rate and gives 148.15% debt-note OC. Add eligibility and haircut schedules.

### D03-I03: Class A benchmark conflicts with the project pricing architecture

**Anchor:** Section 2. D03 uses 91-day T-bill plus 200 basis points. D01 and D09 present KESONIA-based economics. Current CBK materials make KESONIA the reference for variable KES customer lending, though they do not prescribe the SPV note [1]-[3].

**Impact:** The note and assets can have different reset dates and basis risk. A T-bill benchmark does not automatically move with overnight compounded KESONIA. Lender return and borrower rate must not be confused.

**Canonical resolution:** Use compounded KESONIA in arrears plus negotiated `m_A` for Class A, with contractual CBR fallback where appropriate. Use `m_B` or a fixed coupon for Class B. Retain 91-day T-bill only as a comparator or an expressly negotiated alternative. Define compounding, day count, lookback, observation shift, reset, floor, rounding, and fallback.

### D03-I04: Credit enhancement is expressed as a guarantee

**Anchor:** Section 3. The document suggests that first-loss equity, recovery, and interventions guarantee or protect Class A principal.

**Impact:** Subordination and reserves protect only up to available amounts. Recoveries are delayed and uncertain. Interventions cost cash and may fail. Legal defects, commingling, hedge termination, servicer disruption, fraud, and tail dependence can reach senior principal.

**Canonical resolution:** Replace guarantees with the exact structural mechanics and model-dependent outcome. Define Class C subordination, OC, reserve, excess spread, cash sweep, eligibility stop, and liquidation process. State Class A loss only as a calculated scenario result with assumptions. Include reverse stress and recovery-lag sensitivity.

### D03-I05: The term sheet omits the mechanics that create a borrowing base and waterfall

**Anchor:** Sections 1 through 4. There are no definitions for receivable purchase, eligible receivable, defaulted receivable, delinquency, dilution, concentration, purchase price, cash available, collections, or principal proceeds. Waterfall priorities and revolving or amortizing periods are absent.

**Impact:** The SPV cannot calculate how much it may purchase, what cash can be reinvested, or when lenders receive principal. Product-specific cash flows for IPF, microloans, and revolving draws behave differently and cannot share an undefined average.

**Canonical resolution:** Add a definitions schedule, eligibility criteria, ineligibility haircuts, purchase mechanics, borrowing-base certificate, collection allocation, revolving-period conditions, controlled accounts, monthly waterfall, early-amortization waterfall, liquidation waterfall, and permitted investments. State how insurance refunds, prepaid principal, recoveries, fees, and hedge cash are classified.

### D03-I06: PSI, NPL, concentration, OC, and reserve triggers are under-specified

**Anchor:** Section 4. PSI 0.25, NPL 6.5%, platform 25%, geography 15%, OC 125%, and reserve months are presented without data source, formula, observation period, aggregation, cure, or effect.

**Impact:** Parties may calculate different results. A single anomalous day could halt purchases, or a persistent deterioration could escape because the denominator changes. PSI is a model-governance convention, not a statutory default [9].

**Canonical resolution:** For each trigger state numerator, denominator, population, window, calculation date, responsible calculation agent, dispute process, cure period, and consequence. PSI should trigger investigation, challenger comparison, approval requirements, and possibly purchase suspension under contract. NPL should state days past due, default and cure definitions. Concentration must distinguish platform originations, outstanding balance, and eligible balance.

### D03-I07: Legal, servicing, and hedge protections are not term-sheeted

**Anchor:** Sections 1 and 3. The term sheet uses bankruptcy-remote language without true-sale conditions, perfection, non-consolidation, account control, backup servicing, commingling, set-off, or data continuity. It mentions protection without hedge obligations.

**Impact:** These omissions can be more important than subordination. A valid receivable may not transfer, collections may be trapped, and the SPV may lose the data required to service or enforce.

**Canonical resolution:** Add conditions precedent for legal opinions, licences, eligibility, executed platform and carrier agreements, account-control documents, privacy and data rights, servicing and backup servicing, business continuity, tax, and hedge documentation. Define servicer termination and transfer mechanics.

### D03-I08: Accounting and ESG alignment is declaratory

**Anchor:** Section 5. IFRS 9, IFRS 17, and ESG are named without identifying the reporting entity, accounting policy, objective evidence, or reporting metric.

**Impact:** The SPV may hold IFRS 9 receivables, while the carrier accounts for insurance contracts under IFRS 17 [5], [6]. Labeling an intervention ESG does not prove additionality or customer benefit.

**Canonical resolution:** Assign IFRS 9 responsibilities to the holder or originator as applicable; assign IFRS 17 to the carrier. State auditor-reviewed policies, data, journal responsibility, and reporting dates. Define ESG metrics such as coverage continuity, income stabilisation, complaints, adverse-action outcomes, and intervention treatment effect.

### D03-I09: Regulatory labels lack jurisdiction and permission

**Anchor:** Section 5. Basel and other frameworks are presented as direct SPV protections. The SPV is not automatically an approved IRB bank, and a copula model does not change prescribed Basel correlations [8].

**Impact:** A bank credit committee may reject the paper for claiming capital benefit before eligibility and supervisory analysis. Foreign frameworks can be informative but not binding in Kenya.

**Canonical resolution:** State that lender capital treatment is determined by each regulated lender under applicable CBK and Basel implementation. Make regulatory capital benefit a diligence workstream. Identify contractual controls separately from internal policy and actual regulation.

### D03-I10: Evidence status and precedence are missing

**Anchor:** Throughout. The term sheet has no date, version, non-binding status, assumption register, information-rights schedule, or precedence over narrative documents.

**Impact:** Conflicting terms in D01 and D09 may be treated as equally authoritative. Time-sensitive benchmark and tax assumptions can silently become stale.

**Canonical resolution:** Add cover metadata, non-binding qualification, confidentiality, governing law, validity period, information status, and a precedence clause stating that executed finance documents prevail. Append sources and assumptions with as-of dates.

## Cross-document dependencies and diligence

D03 must control D01 and D09 for financing economics. D04 supplies asset mechanics, D05 and D08 supply data and servicing controls, D06 supplies model outputs but not contractual guarantees, D07 supplies qualification, and D10 supplies closing conditions and execution dates. Required diligence includes portfolio tape, legal entity documents, originator and carrier licences, tax opinion, true-sale and non-consolidation opinions, platform agreements, controlled-account structure, servicing plan, hedge quote, KESONIA term conventions, financial model, and draft reporting package.

## Prioritised remediation sequence

First choose denomination and benchmark. Second define eligible assets, purchase mechanics, borrowing base, OC, and reserves. Third write the cash waterfalls and amortization events. Fourth add servicing, accounts, hedge, legal, tax, and data protections. Fifth define every covenant and event of default. Sixth replace guarantees and qualify accounting and regulatory language. Last, reconcile the term sheet to the workbook and memorandum.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D03-I01 | D03-P02, D03-P04, D03-P08 |
| D03-I02 | D03-P03, D03-P05 |
| D03-I03 | D03-P04 |
| D03-I04 | D03-P05, D03-P07 |
| D03-I05 | D03-P03, D03-P05, D03-P06 |
| D03-I06 | D03-P07 |
| D03-I07 | D03-P02, D03-P06, D03-P08 |
| D03-I08 | D03-P09 |
| D03-I09 | D03-P09 |
| D03-I10 | D03-P01, D03-P10 |
