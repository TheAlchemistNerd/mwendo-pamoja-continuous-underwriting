# D01 Inconsistency Report: Strategic Partnership Memorandum

## Document role and semantic synopsis

D01 is intended to persuade banks, insurers, platforms, DFIs, and capital providers that Mwendo Pamoja can combine continuous underwriting with a ring-fenced receivables vehicle. It therefore performs three jobs at once: strategic memorandum, technical architecture summary, and preliminary financing paper. Its strongest idea is that driver insurance, working capital, and repayment capacity share a common cash-flow state and should be managed jointly. Its central weakness is that proposed mechanics, illustrative forecasts, regulatory conclusions, and contractual protections are expressed at the same level of certainty.

The memorandum describes HoldCo and an SPV, real-time ingestion, dual-regime modelling, a liquidity path, Bayesian decisions, credit enhancements, IFRS accounting, interventions, portfolio economics, and a USD 10 million financing request. Comparison with D02 through D10 shows that many terms appear stable only within D01. The facility amount, benchmark, entity responsibility, feature ownership, collateral denominator, and evidence status change elsewhere.

## Executive inconsistency summary

The document should not be circulated for lender reliance in its current form. The most material issues are: a USD 2.5 million HoldCo request that conflicts with the USD 1 million canonical overlay; an unclear USD-debt and KES-asset currency position; a 75% figure used without distinguishing tranche share from collateral advance rate; a Class A protection claim that exceeds the evidence; customer pricing and note pricing that are not separated; and an architecture that partially merges an interpretable feature path with hard policy rules. Claims about historical recovery, yields, originations, model lead time, and stress performance lack a portfolio tape or reproducible workbook.

## Prioritised issue matrix

| Finding | Severity | Confidence | Primary anchor | Main impact |
|---|---|---|---|---|
| D01-I01 | Critical | High | Section 1; Section 3.2 | Financing request and uses do not reconcile |
| D01-I02 | Critical | High | Section 3.1; Section 3.2 | Currency and bankruptcy-remoteness claims mislead lenders |
| D01-I03 | Critical | High | Section 3.2; Section 6.3 | Advance rate, OC, and capital share are conflated |
| D01-I04 | High | High | Sections 3 and 6 | Customer rate and note coupon lack a canonical benchmark split |
| D01-I05 | High | High | Sections 2.2 and 2.3 | Feature path and policy gate are not fully separated |
| D01-I06 | Critical | High | Sections 4 and 6 | Protection and stress claims are unsupported guarantees |
| D01-I07 | High | High | Sections 1 and 6 | Commercial metrics have no evidence status or period |
| D01-I08 | High | Medium | Sections 1.1 and 3.1 | Counterparty and true-sale responsibilities are incomplete |
| D01-I09 | High | High | Section 5.1 | IFRS 9 scope and model measure are over-simplified |
| D01-I10 | Medium | High | Section 5.2 | Insurance, ESG, and intervention authority are blurred |
| D01-I11 | Medium | High | Throughout | Citations and drafting defects impair auditability |

## Detailed findings

### D01-I01: Facility size and use-of-proceeds contradiction

**Anchor:** Section 1, “Executive Summary,” and Section 3, “Project Finance Structure & Cash Flow Waterfall.” D01 presents a USD 10 million programme while allocating USD 2.5 million to HoldCo and using a separate SPV financing narrative. D09 repeats USD 2.5 million, while the agreed financing baseline and lender model use USD 9 million for the SPV plus USD 1 million for HoldCo. The alternatives cannot both be the same transaction.

**Impact:** A lender cannot identify the borrowing entity, consolidated ask, SPV purchase capacity, sponsor contribution, or debt service source. Mixing HoldCo venture debt into SPV sources also risks suggesting that operating expenditure can be paid ahead of noteholders.

**Resolution:** State a USD 9 million SPV capitalization and an optional USD 1 million HoldCo facility. Show USD 10 million only as a consolidated view. Provide separate sources and uses, accounts, covenants, obligors, maturity, and recourse. HoldCo cash must never enter the SPV waterfall unless a documented subordinated contribution is made. This resolution controls D01-P02, D01-P06, and D01-P09.

### D01-I02: Currency mismatch and false self-hedge

**Anchor:** Sections 3.1 and 3.2. The memorandum refers to USD investor capital, KES receivables, and a reserve account that “self-hedges” exposure. D03 mentions a TCX-style hedge, while D09 alternates between KESONIA and USD or SOFR concepts.

**Impact:** A cash reserve denominated in the same currency as collections provides liquidity, not a hedge against a USD liability. Depreciation can reduce USD debt-service capacity even where KES collections perform. The omission materially affects DSCR, note yield, reserve sizing, and loss allocation.

**Resolution:** Use KES as the operating and waterfall currency. If notes are denominated in USD, add a defined cross-currency hedge, counterparty, collateral, termination waterfall, and stress. Otherwise issue KES notes and translate only for investor reporting. Replace “self-hedge” with quantified liquidity coverage. D03 and D09 must adopt the same election.

### D01-I03: Advance rate and OC denominator conflict

**Anchor:** Section 3.2 and Section 6.3. The 75% figure is used near the Class A share and as an advance-rate concept, while a 125% OC requirement is asserted without a consistent denominator.

**Impact:** The same percentage appears to describe how the capital stack is divided, how much collateral can be funded, and how much senior debt is protected. These are different calculations. A lender cannot reproduce collateral headroom or determine when purchases stop.

**Resolution:** Define Class A at 75% of USD 9 million. Define borrowing-base advance separately. Define OC as eligible receivables divided by Class A plus Class B outstanding. If total capital divided by 75% implies USD 12 million of collateral, show that calculation and the resulting 148.15% debt-note OC. Specify eligibility, delinquency, concentration, dilution, and haircut rules.

### D01-I04: Customer pricing and liability pricing are conflated

**Anchor:** Sections 3.2, 6.1, and 6.3. The draft uses benchmark and yield language without separating borrower interest, total cost of credit, asset yield, Class A coupon, Class B coupon, and investor hurdle rate. D03 elects a 91-day T-bill while D09 uses KESONIA plus an additional `K` and bank margin.

**Impact:** Double counting can overstate customer yield or understate the SPV's liability cost. It also creates an inaccurate statement of the CBK revised pricing model.

**Resolution:** Customer lending rate is KESONIA plus `K_RBCP`; total cost adds disclosed fees [1], [2]. `K_RBCP` includes lending costs, shareholder return, and borrower risk. Class A should be compounded KESONIA in arrears plus `m_A`, with CBR fallback if appropriate; the T-bill is comparison only. Use different rows and symbols for asset pricing, note pricing, FTP, EL, and CoC.

### D01-I05: Explicit features and policy controls are merged

**Anchor:** Sections 2.2 and 2.3. D01 correctly recognises interpretable liquidity variables, but describes the bypass as both a model input path and regulatory explainability or policy mechanism. D02 and D05 also place Earnings Velocity or CFA inconsistently in neural and explicit branches.

**Impact:** Engineers could calculate the same metric twice, validators could not identify the model boundary, and policy owners could mistake a predictive feature for a legally binding rule.

**Resolution:** Use the four-layer canonical architecture. CFA, DLR, Earnings Velocity, and Repayment Velocity belong to the Explicit Liquidity Feature Path and enter HBLR directly. The downstream Credit Policy and Compliance Gate owns affordability, exposure, uncertainty, concentration, reserve, and eligibility rules. Raw wallet events may still support neural sequence learning.

### D01-I06: Principal-protection and stress assertions exceed evidence

**Anchor:** Sections 4.1, 4.2, and 6.2. The memorandum presents Class A protection, recovery and loss absorption with near-contractual certainty. It describes stress outcomes without a linked formula-driven model, scenario definitions, timing assumptions, or legal enforceability analysis.

**Impact:** “Protected,” “guaranteed,” or equivalent wording can mislead an investment committee. First-loss equity and interventions reduce loss only to the extent of funded cash, recoveries, and enforceable collections. Tail losses, hedge termination, servicing interruption, and commingling are omitted.

**Resolution:** Say that the model projects no Class A principal loss under a named scenario only if the workbook supports it. Report peak cumulative default, recovery lag, liquidation haircut, OC, reserve draw, interest shortfall, principal shortfall, and early-amortization month. Add reverse stress and break-even default. Treat interventions as costs and uncertain effectiveness, not automatic collateral.

### D01-I07: Unsupported commercial and empirical metrics

**Anchor:** Section 1 and Section 6. Statements include high yields, low defaults, large originations, approximately 40% recovery, and advance distress detection. The corpus contains no historical portfolio tape, cohort definition, experiment, or audited performance source.

**Impact:** Readers may interpret illustrative values as realised history. Inconsistent horizons also make annual yields, monthly originations, and lifetime defaults incomparable.

**Resolution:** Tag each metric as source-backed, derived, illustrative, target, or model output. State observation window, cohort, product, currency, gross or net basis, and as-of date. Move unsupported values to an assumptions table and add diligence requests for loan tape, policy ledger, collection records, platform data, and intervention trials. The Star article supports fuel and purchasing-power stress as a scenario, not the document's exact loss rates [31].

### D01-I08: Counterparty and true-sale incompleteness

**Anchor:** Sections 1.1 and 3.1. Roles are named but not expressed as contractual obligations. The document implies bankruptcy remoteness from organisational design and does not address licensing, data rights, receivables assignment, account control, perfection, commingling, backup servicing, or platform set-off.

**Impact:** The asset may not be legally transferable or collections may remain exposed to originator and platform insolvency. The waterfall is not credible without controlled accounts and servicing continuity.

**Resolution:** Add a responsibility matrix and transaction-document map. Reserve true-sale and non-consolidation conclusions for counsel. Identify owner and licence for origination, servicing, policy issuance, premium collection, data processing, and interventions. List legal opinions and conditions precedent.

### D01-I09: IFRS 9 is presented as an automated model label

**Anchor:** Section 5.1. D01 implies the continuous underwriting score directly creates IFRS 9 compliance. It does not identify the reporting entity, instrument classification, EIR, staging policy, scenario weighting, cure, write-off, or governance.

**Impact:** A posterior PD can be an input, but cannot alone establish ECL or accounting policy. Risk-neutral pricing outputs would be inappropriate for ordinary ECL, which uses real-world forward-looking measures [5], [20].

**Resolution:** Separate underwriting PD, IFRS 9 `PD_P`, pricing overlays, and contractual triggers. Assign the ECL calculation to each holder of financial assets, with validated PD, LGD, EAD, macro scenarios, SICR policy, controls, and journals. Do not imply IFRS 17 applies to the SPV's receivables [6].

### D01-I10: Insurance, ESG, and intervention authority are blurred

**Anchor:** Sections 1.1 and 5.2. D01 alternates among Insurtech, carrier, and platform roles and treats premium holidays, rewards, routing, and draw freezes as readily executable.

**Impact:** A technology provider cannot issue or amend insurance unless authorised. Platform routing and wallet deductions require contract, customer notice, consent, and operational integration. Interventions can become forbearance, discrimination, or an unfair-practice issue.

**Resolution:** State that the licensed carrier owns policy issuance and insurance accounting. Define which party funds each intervention, customer eligibility, consent, accounting treatment, override, appeal, adverse-action explanation, and outcome testing. Frame ESG additionality as a measurable hypothesis.

### D01-I11: Evidence and editorial integrity defects

**Anchor:** Throughout. Several claims lack references, cross-document definitions drift, and source-derived formulas contain punctuation damage elsewhere in the series. The memorandum has no evidence-status legend or controlled definitions.

**Impact:** A reader cannot tell whether a statement is law, term, assumption, forecast, or aspiration. Errors will propagate into D03 and the model.

**Resolution:** Add numbered assumptions, one definitions table, IEEE citations, as-of dates, and explicit cross-references to D03, D05, D06, D07, and D09. Run formula and mojibake checks. Avoid long dashes and unsupported absolutes.

## Dependencies, diligence, and remediation sequence

D01 depends on D03 for definitive economics, D05 and D06 for the model boundary, D07 for regulatory qualification, D08 for system-of-record controls, D09 for pricing and accounting, and D10 for execution evidence. Required diligence includes executed platform and carrier agreements, legal entity charts, licences, historical loan and policy tapes, FX election, draft cash-management agreement, tax analysis, underwriting-validation results, intervention experiments, and a reproducible 36-month waterfall.

Remediation should proceed in this order: reconcile the financing ask and entities; select note currency and benchmark; define borrowing base and waterfall; separate technical model from policy gate; qualify accounting and regulatory claims; replace guarantees with scenario outputs; then edit metrics and citations. D01 is ready only when every capital, yield, loss, and protection statement ties to D03 and the financial model, and every technology claim ties to D05 through D08.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D01-I01 | D01-P02, D01-P06, D01-P09 |
| D01-I02 | D01-P03, D01-P06 |
| D01-I03 | D01-P06, D01-P10 |
| D01-I04 | D01-P07, D01-P09 |
| D01-I05 | D01-P04, D01-P05 |
| D01-I06 | D01-P08, D01-P09 |
| D01-I07 | D01-P01, D01-P08, D01-P11 |
| D01-I08 | D01-P03, D01-P06 |
| D01-I09 | D01-P07 |
| D01-I10 | D01-P03, D01-P07 |
| D01-I11 | D01-P01, D01-P11, D01-P12 |
