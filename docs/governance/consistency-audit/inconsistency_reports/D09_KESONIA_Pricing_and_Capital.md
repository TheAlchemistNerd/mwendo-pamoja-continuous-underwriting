# D09 Inconsistency Report: KESONIA Pricing and Capital Orchestration

## Document role and semantic synopsis

D09 attempts to join customer pricing, KESONIA compounding, Bayesian risk premiums, SPV capital structure, reserves, WACC, stress, Basel capital, IFRS 17, IFRS 9 EIR, modification accounting, FTP, IRRBB, SQL, and Monte Carlo simulation. It is the most financially consequential technical paper because D01 and D03 rely on its economics and D08 relies on its journal logic. It also draws heavily on the question drafts about risk-neutral measures, mature FTP, and project-finance cost of capital.

The paper's central ambition is useful: a benchmark-rate engine, credit-risk engine, liability schedule, ECL process, and cash waterfall should reconcile. The present draft does not maintain those boundaries. It reuses `K` for customer premium, ECL-only risk charge, bank margin, and capital; adds a bank margin after `K`; mixes Class A note pricing between KESONIA, T-bill, and possible USD benchmarks; applies a tax shield inconsistently; and calls the result WACC even when it is a contractual waterfall cost.

## Executive inconsistency summary

D09 must be rebuilt from a notation and cash-flow dictionary. Official CBK material supports total lending rate equals KESONIA plus `K_RBCP`, with fees and charges added for total cost [1], [2]. `K_RBCP` is not restricted to expected loss and a separate generic bank margin should not be double counted. The note coupon is a different contract. The Class A basis should be compounded KESONIA plus `m_A` under the canonical baseline. WACC should be reserved for valuation; SPV debt service should use contractual coupons and actual tax. The 2.5 million HoldCo facility, dynamic 85% to 70% advance rate, 20% excise duty, 3% fee, 12.06% WACC, and 10.5% KESONIA are unsupported assumptions.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D09-I01 | Critical | High | Sections 5 and 6; Appendix | CBK pricing formula is misstated and double counts margin |
| D09-I02 | Critical | High | Sections 6 and 7 | Customer, note, FTP, discount, and hurdle rates are conflated |
| D09-I03 | High | High | Compounding engine | Contract conventions and rate vintages are incomplete |
| D09-I04 | High | High | SQL implementation | Observation, day weighting, and decimal controls are unsafe |
| D09-I05 | Critical | High | Capital stack and WACC | WACC is substituted for waterfall cost |
| D09-I06 | Critical | High | Tax and Appendix | Class B, tax shield, excise duty, and fee assumptions lack basis |
| D09-I07 | Critical | High | SPV financing | HoldCo amount and dynamic advance rates conflict with baseline |
| D09-I08 | High | High | Basel capital | IRB and copula benefits are overstated |
| D09-I09 | High | High | IFRS 9 Phase 2 and modifications | Benchmark relief and thresholds are misapplied |
| D09-I10 | High | High | IRRBB | NII and EVE stress formulas are dimensionally incomplete |
| D09-I11 | High | High | IFRS 17 | Insurer accounting is mixed into SPV capital orchestration |
| D09-I12 | High | High | Monte Carlo appendix | Code embeds unsupported constants and incomplete dependencies |
| D09-I13 | Medium | High | Throughout | Notation, equations, and punctuation are corrupted |

## Detailed findings

### D09-I01: `K` is defined contrary to the current CBK formulation

**Anchor:** “The KESONIA K-Generator Framework,” “Translating Posterior PD,” and Appendix comments saying `Lending Rate = KESONIA + K + Bank Margin` and `K strictly prices ECL`.

**Impact:** Official CBK materials state total lending rate equals KESONIA plus premium `K`, with total cost adding fees and charges. `K` includes lending-related costs, shareholder return, and borrower risk [1], [2]. Restricting `K` to ECL and adding a bank margin can double count capital, operating, and shareholder return.

**Canonical resolution:** Rename it `K_RBCP`. Build a transparent internal decomposition such as expected loss, allocated operating and funding cost, capital or shareholder return, liquidity, and borrower-risk adjustment, subject to CBK and contract requirements. The disclosed customer formula remains KESONIA plus `K_RBCP`; fees are separate in total cost.

### D09-I02: Five different rates are treated as one economic object

**Anchor:** Sections 6, 7, 12, 15, and Appendix. Customer rate, Class A and B coupons, asset yield, matched-maturity FTP, WACC, and risk-neutral discounting appear to flow from the same `K` or benchmark.

**Impact:** The model can double count risk or omit basis. A customer's risk premium is not the SPV note margin, an internal FTP charge is not cash paid under the waterfall, and WACC is not a contractual coupon. `PD_P` is not `PD_Q` [20].

**Canonical resolution:** Add a rate taxonomy and separate schedules. Customer: KESONIA plus `K_RBCP`. Class A: compounded KESONIA plus `m_A`. Class B: KESONIA plus `m_B` or fixed coupon. FTP: an internal matched-maturity allocation if a bank needs it [14]. WACC or sponsor discount rate: valuation only. Market-consistent spread: optional and calibrated to observables.

### D09-I03: KESONIA accrual lacks a contractual convention

**Anchor:** “The CCR Formula” and “Calendar Modeling and Observation Lookbacks.” The draft imports a five-day lookback and compounding mechanics resembling SOFR or SONIA without a cited CBK contractual standard.

**Impact:** Different observation shift, lag, lockout, and non-business-day conventions produce different interest. A weekend rate may accrue for several days. Contract and system can disagree even if both use daily KESONIA [3].

**Canonical resolution:** Define observation period, lookback or lag, observation shift, lockout, day-count basis, business-day calendar, rate publication time, floor, rounding, restatement, missing-rate fallback, CBR fallback, reset notice, and payment delay. Label any five-day lookback as a negotiated assumption, not a mandate.

### D09-I04: SQL is not safe for authoritative accrual

**Anchor:** “Production SQL Compounding Logic.” The query relies on a `kesonia_reference`, calendar joins, and log-sum transformation without adequately controlling loan-specific observation boundaries, multiple rate publications, rate representation, last-day weight, nulls, negative rates, or versioning.

**Impact:** Storing 10.5 instead of 0.105 changes accrual by one hundred times. An incorrect day weight or duplicate rate can overcharge customers and misstate interest. Re-running after a restatement can change a posted period.

**Canonical resolution:** Store rate and scale explicitly, enforce one approved rate vintage per publication date, materialise a contract-specific daily schedule, weight each calendar day once, use high-precision decimal arithmetic, validate log-domain constraints, and reconcile against a direct product calculation. Freeze posted accruals and process corrections through adjustments. Add known-answer tests over weekends, holidays, leap years, missing rates, and period ends.

### D09-I05: WACC is substituted for actual SPV cash cost

**Anchor:** “Working Cost of Capital (WACC) Calculation.” The draft calculates approximately 12.06% using tranche weights, a 10.5% benchmark, debt tax shield, and equity return, then uses the result within SPV economics.

**Impact:** WACC is a valuation discount rate for a defined entity and capital structure. The waterfall pays contractual interest, fees, hedge cash, taxes, and residual distributions by time. Class C has no fixed coupon. A static weighted rate cannot test liquidity or tranche loss [21]-[23], [32], [33].

**Canonical resolution:** Rename “working cost of capital” to avoid WACF or WACC ambiguity. Build monthly debt and cash schedules. Calculate lender yields and Class C IRR from actual cash flows. Use a sponsor valuation discount rate only for HoldCo or project NPV and document its basis. Do not use it to allocate waterfall cash.

### D09-I06: Tax and fee mechanics are unsupported and inconsistent

**Anchor:** WACC, tax shield, and Appendix comments. Class A appears to receive a tax shield while Class B is treated as equity-like. The code hardcodes a 30% tax rate, 20% excise duty, and 3% origination fee.

**Impact:** Subordination does not make debt equity for tax. The SPV may be tax neutral, have limited taxable income, or face instrument-specific treatment. A fee and excise assumption change customer total cost and SPV cash. The corpus provides no Kenyan tax opinion.

**Canonical resolution:** Add a tax assumptions schedule approved by Kenyan tax counsel: entity status, taxable income, interest deductibility, withholding, VAT or excise treatment, fees, loss utilisation, and transfer pricing. Apply treatment consistently to Class A and B according to legal form. Label all values illustrative until confirmed.

### D09-I07: Funding amount and advance rates conflict

**Anchor:** capital structure and stress sections. D09 includes USD 2.5 million HoldCo debt and dynamic advance rates from 85% to 70%, while the canonical baseline is USD 1 million HoldCo and a distinct 75% funding assumption with 125% OC.

**Impact:** Sources and uses, collateral, interest, and dilution no longer reconcile with D01 and D03. Dynamic changes can cause immediate funding gaps unless the purchase and cure mechanism is defined.

**Canonical resolution:** Set HoldCo overlay at USD 1 million. Keep the primary SPV at USD 9 million. Separate Class A share, total-capital funding rate, borrowing-base advance rate, and OC. Model advance-rate haircuts only as contractual scenario inputs with cure, stop-purchase, and cash-sweep consequences.

### D09-I08: Regulatory capital benefits are not established

**Anchor:** “Basel IV Advanced IRB and Output Floors.” The paper suggests HBLR and copula sophistication creates capital synergy.

**Impact:** The regulated lender determines capital treatment under local rules and permissions. Internal dependency estimates do not override prescribed Basel formulas or output floors [8].

**Canonical resolution:** Present bank capital as an external lender analysis. Provide data and stress outputs that may support due diligence, but do not promise relief. Separate economic capital, SPV subordination, accounting ECL, and regulatory RWA.

### D09-I09: IFRS 9 benchmark and modification relief is misapplied

**Anchor:** “IFRS 9 Phase 2 Practical Expedient” and “Substantial vs. Non-Substantial Modification Accounting.” Routine KESONIA accrual and changes to `K` are placed under IBOR reform relief; a 10% test is generalised.

**Impact:** Phase 2 relief addressed qualifying benchmark replacement, not every ongoing reset [4]. A discretionary risk-premium change may be a contractual repricing or modification. Asset and liability derecognition analyses differ [5].

**Canonical resolution:** Separate transition from CBR or another benchmark, ordinary floating-rate accrual, and discretionary contract modification. Have accounting policy define prospective EIR updates, modification gain or loss, derecognition, notices, and stage consequences. Use the 10% test only in the context where the standard and policy support it.

### D09-I10: IRRBB formulas lack cash-flow dimensions

**Anchor:** “IRRBB, Earnings at Risk, and EVE.” A simplified change-in-NII expression multiplies a rate shock by assets, and stress magnitudes are presented as uniform.

**Impact:** NII depends on repricing gaps, floors, caps, pass-through, balances, behavioural assumptions, and time. EVE discounts instrument cash flows across prescribed yield-curve scenarios. A non-bank SPV is not itself an IRRBB-regulated bank [7].

**Canonical resolution:** If the lender needs IRRBB analysis, model asset and liability cash flows by repricing bucket and contractual option. Run applicable prescribed scenarios under the lender's framework. For the SPV, call the analysis KESONIA basis and repricing stress unless legal scope establishes IRRBB reporting.

### D09-I11: IFRS 17 is inserted into SPV capital without entity separation

**Anchor:** “Regulatory Capital Synergies” and “IFRS 17 and Onerous Contract Testing.” The draft mixes carrier insurance measurement with the SPV receivables waterfall.

**Impact:** The carrier's IFRS 17 result and prudential capital do not automatically provide SPV cash. An insurance refund receivable may support IPF recovery only under contract and collection timing [6].

**Canonical resolution:** Move IFRS 17 mechanics to the carrier interface. In the SPV model, include only enforceable premium-refund receivables, timing, haircut, and counterparty risk. Report carrier obligations and eligibility conditions.

### D09-I12: Monte Carlo code embeds conclusions as constants

**Anchor:** Appendix. Code comments hardcode rate, fees, tax, yields, recovery, defaults, and WACC while presenting rich outputs. Dependencies, random seed policy, scenario calibration, unit tests, and cash waterfall are incomplete.

**Impact:** Attractive charts can give false precision. A simulation of loss rates without cohort cash timing, eligibility, and waterfall cannot establish senior protection or investor returns.

**Canonical resolution:** Move code to a governed model repository. Load assumptions from a versioned table with source status. Model product cohorts, collection and recovery lags, debt service, reserve, OC, early amortization, FX, and taxes. Pin dependencies, seed and document randomness, validate against deterministic cases, and reconcile every displayed number to the workbook.

### D09-I13: Symbols and punctuation are not reliable

**Anchor:** equations and Appendix. `K` is reused, subtraction signs are damaged, ranges contain mojibake, and terms such as WACF, WACC, margin, and capital shift meaning.

**Impact:** Reviewers cannot establish dimensional or semantic consistency.

**Canonical resolution:** Adopt the master notation table, use ASCII minus in fragile code blocks, render equations, and test formulas. Add currency, period, basis, source, and as-of date to every assumption.

## Dependencies, evidence gaps, and remediation sequence

D09 is controlled by D03 for note terms and D01 for programme scope. It requires D04 cash-flow states, D06 `PD_P`, D07 accounting and prudential boundaries, D08 ledger controls, and D10 model implementation. Evidence needed includes executed pricing contracts, CBK-compliant disclosure, KESONIA history, lender term indications, tax opinion, FTP methodology if a bank requires it, accounting policy, portfolio tape, recovery timing, hedge quotes, and a validated workbook.

Remediation order is: freeze notation and rate taxonomy; implement contractual KESONIA compounding; reconcile the capital stack; replace WACC with cash schedules; obtain tax and accounting decisions; separate regulatory capital and IFRS 17; rebuild Monte Carlo around the waterfall; then publish only calculated outputs.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D09-I01 | D09-P02, D09-P03 |
| D09-I02 | D09-P02, D09-P05, D09-P07 |
| D09-I03 | D09-P04 |
| D09-I04 | D09-P04, D09-P11 |
| D09-I05 | D09-P05, D09-P07 |
| D09-I06 | D09-P06 |
| D09-I07 | D09-P05 |
| D09-I08 | D09-P09 |
| D09-I09 | D09-P08 |
| D09-I10 | D09-P10 |
| D09-I11 | D09-P09 |
| D09-I12 | D09-P11, D09-P12 |
| D09-I13 | D09-P01, D09-P12 |
