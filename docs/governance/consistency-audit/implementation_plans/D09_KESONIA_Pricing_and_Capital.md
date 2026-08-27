# D09 Implementation Plan: KESONIA Pricing and Capital Orchestration

## Objective and financial boundary

Rewrite D09 as the authoritative methodology for KESONIA accrual, customer price composition, SPV liability pricing, product and cohort cash flows, reserves, waterfall returns, accounting interfaces, matched-maturity FTP where needed, market-consistent valuation where supportable, and interest-rate stress. It should no longer use one `K` or one weighted rate to represent several different economic quantities.

D03 controls commercial note terms. D04 supplies product cash events. D06 supplies real-world risk outputs and any optional valuation inputs. D07 governs accounting and prudential interpretation. D08 governs journal and system boundaries. D09 translates those inputs into auditable calculations and model requirements. All tax, fee, rate, loss, and recovery assumptions must be sourced, provisional, or calculated.

## Proposed document architecture

1. Scope, rate taxonomy, notation, and assumptions status.
2. CBK customer pricing and disclosure.
3. KESONIA data, compounding, fallback, and contract conventions.
4. SQL or calculation-engine design and controls.
5. SPV sources, uses, capital stack, and note schedules.
6. Tax, fees, hedge, servicing, and transaction costs.
7. Product cohorts, asset yield, collections, losses, and recoveries.
8. Waterfall, reserves, OC, covenants, and investor returns.
9. IFRS 9 accounting interface and carrier IFRS 17 boundary.
10. FTP, valuation, and IRRBB or SPV rate stress.
11. Scenario, Monte Carlo, validation, and model governance.
12. Sources, diligence, acceptance criteria, and references.

## Section-level implementation actions

### D09-P01: Freeze notation, units, and evidence status

**Action:** Add before the current introduction and audit every equation.

**Resolves:** D09-I13.

**Content:** Define KESONIA, CBR, 91-day T-bill, SOFR only if a USD scenario is retained, `K_RBCP`, `K_cap`, `m_A`, `m_B`, `PD_P`, `PD_Q`, `EL`, `CoC`, `OpEx`, EIR, FTP, NIM, DSCR, OC, CRA, RWA, EVE, and EaR. State whether rates are decimal or percentage, nominal or effective, annual or period, simple or compounded. State currency and as-of date.

Create assumption statuses: official or contractual, portfolio evidence, derived, illustrative, scenario, and output. Re-key damaged formulas and add known-answer examples.

**Acceptance tests:** No `K` stands alone. Every rate has basis and period. All equations render and match executable tests.

### D09-P02: Create a rate taxonomy and cash-flow map

**Action:** Replace the “K-Generator” framing and introduce the document.

**Resolves:** D09-I01 and D09-I02.

**Content:** Use a table with customer base rate, `K_RBCP`, fees, total cost, Class A benchmark and margin, Class B benchmark and margin, asset yield, FTP charge, hedge cost, sponsor discount rate, and optional market-consistent discount or spread. For each state payer, recipient, legal basis, cash or non-cash status, reset, source, and model location.

Explain that customer pricing follows CBK; note pricing follows D03; FTP allocates internal bank funding economics; WACC or discount rate values HoldCo or sponsor cash; and `PD_Q` is used only in a supported market valuation overlay.

**Acceptance tests:** No rate appears in more than one role without an explicit bridge. The model cannot add an unspecified bank margin after `K_RBCP`.

### D09-P03: Rewrite CBK customer pricing and premium decomposition

**Action:** Rewrite Sections 5 and 6.

**Resolves:** D09-I01.

**Content:** State `Total lending rate = KESONIA + K_RBCP` and `Total cost of credit = KESONIA + K_RBCP + fees and charges`, citing [1], [2]. State effective dates and scope from official material, including fixed and foreign-currency exclusions and CBR alternative where applicable. Explain that `K_RBCP` includes lending-related cost, shareholder return, and borrower risk.

Build an internal decomposition with expected loss, funding or liquidity allocation, operating cost, capital or shareholder return, borrower risk, and uncertainty, with checks against double counting. Use `PD_P`, LGD, EAD, and horizon for expected loss. Describe governance, maximum and minimum, approval, disclosure, notice, and customer contract. Do not call the Bayesian engine the “ultimate” pricing authority; the policy and approval process owns the price.

**Acceptance tests:** Formula matches [1], [2]. Fee disclosure is separate. A pricing example reconciles decomposition and customer rate without double counting.

### D09-P04: Build a contractual KESONIA compounding specification and safe engine

**Action:** Rewrite Section 7 and its SQL.

**Resolves:** D09-I03 and D09-I04.

**Content:** Define source URL and publication timestamp [3], rate vintage, holiday calendar, observation period, day-count basis, lookback or lag, observation shift, lockout, floor, rounding, payment delay, missing publication, CBR fallback, correction, and customer notice. Label a five-day lookback as a negotiated convention unless official terms establish it.

Implement a contract-specific daily observation schedule. Store rates as decimals with metadata and approval. Use the product form over each applicable day, or numerically stable log-sum only when all domain constraints hold. Preserve high precision until contractual rounding. Freeze posted periods and post adjustments for corrections.

Create SQL layers for raw rates, approved rates, calendar, contract terms, daily observations, period factors, accruals, exceptions, and reconciliation. Enforce unique rate and day records.

**Acceptance tests:** Known-answer cases cover weekends, holidays, leap year, missing rates, rate correction, floors, partial periods, and zero or negative rates if contract permits. Direct product and log-sum agree within tolerance. No 10.5 versus 0.105 scale ambiguity exists.

### D09-P05: Reconcile capital stack, advance rate, OC, and actual liability cost

**Action:** Rewrite Sections 12.1 through 12.3.1.

**Resolves:** D09-I02, D09-I05, and D09-I07.

**Content:** Use USD 9 million equivalent SPV capitalization and USD 1 million optional HoldCo overlay. Show Class A 6.75 million, B 1.35 million, and C 0.90 million equivalent, all settled in KES under the canonical case. Separate capital share, borrowing-base advance, and OC. Use 125% minimum OC and explicit denominator.

Build monthly Class A and B schedules from compounded KESONIA plus margins, draws, principal, sweeps, and ending balance. Compute Class C return from residual cash rather than assumed equity coupon. Remove 12.06% “working WACC” from waterfall use. If sponsor valuation needs WACC, calculate it separately with supported market inputs and cash-flow perimeter [21]-[23], [32], [33].

**Acceptance tests:** Stack and sources and uses reconcile. Liability cash equals waterfall payments. Changes in KESONIA affect debt according to contract. WACC does not allocate cash.

### D09-P06: Replace unsupported tax, fee, and hedge constants

**Action:** Add a transaction-cost and tax schedule and rewrite Appendix assumptions.

**Resolves:** D09-I06.

**Content:** List corporate tax, interest deductibility, withholding, VAT or excise, origination and servicing fees, trustee, legal, audit, hedge, and platform costs. For each state payer, recipient, taxable base, rate, timing, source, recoverability, and provisional status. Obtain Kenyan tax advice before applying 30%, 20%, 3%, or any shield.

Apply Class A and B tax treatment according to legal form, not seniority. Determine whether the SPV can use deductions. Separate customer fees from SPV revenue and show total cost disclosures. If USD exposure remains, model hedge quotes, collateral, basis, and termination.

**Acceptance tests:** Tax cash reconciles to taxable base. A zero-tax-shield scenario works. All fees flow to both customer disclosure and SPV cash where relevant.

### D09-P07: Build product-cohort asset yield and waterfall returns

**Action:** Add the missing asset cash-flow core and rewrite NIM.

**Resolves:** D09-I02 and D09-I05.

**Content:** Create monthly IPF, microloan, and revolver cohorts from D04. Model origination, scheduled principal, interest, fees, prepayment, delinquency, default, recovery, recovery lag, refund, cancellation, utilisation, and closing balance. Calculate effective asset yield and cash collections by cohort.

Feed collections to the D03 waterfall. Model servicing, trustee, hedge, taxes, purchases, reserve, A and B debt service, and residual. Report gross yield, net portfolio yield, excess spread, NIM with a precise denominator, DSCR, cash, Class A and B yields, and Class C IRR. Distinguish accounting interest from cash.

**Acceptance tests:** Each cohort and cash account rolls forward. Yield is not used as cash. Investor returns derive only from dated cash flows. Product results reconcile to aggregate portfolio.

### D09-P08: Correct IFRS 9 EIR and modification treatment

**Action:** Rewrite Section 14.

**Resolves:** D09-I09.

**Content:** Separate initial benchmark transition, ordinary contractual floating-rate reset, and discretionary change to `K_RBCP` or terms. Explain the narrow IBOR Reform Phase 2 context [4]. Define EIR, prospective floating accrual, modification gain or loss, derecognition, fees, costs, stage, forbearance, and journal responsibilities under entity policy [5].

Do not apply a universal 10% test to financial assets. Create a decision tree reviewed by auditors. Link approved results to D08 journal staging.

**Acceptance tests:** Sample ordinary reset, benchmark replacement, risk-premium change, extension, and hardship restructure produce approved accounting outcomes. No phase-two expedient is used outside its conditions.

### D09-P09: Separate IFRS 17, lender capital, and SPV protection

**Action:** Rewrite Sections 12.4, 13.1, and 13.2.

**Resolves:** D09-I08 and D09-I11.

**Content:** Move carrier insurance accounting to an interface summary. The SPV model includes only enforceable premium refund cash, haircut, lag, and carrier counterparty risk. Assign IFRS 17 to the carrier [6].

Separate lender RWA and Basel analysis from the SPV model. Provide pool data and stress results; do not promise A-IRB or copula capital relief [8]. Define SPV protection through subordination, OC, reserve, excess spread, recovery, and waterfall. Keep economic capital as an internal risk measure.

**Acceptance tests:** No IFRS 17 metric creates SPV cash without a contract. No internal copula directly changes regulatory RWA. Capital labels state owner and purpose.

### D09-P10: Rebuild FTP, valuation, and interest-rate stress

**Action:** Rewrite Section 15.

**Resolves:** D09-I02 and D09-I10.

**Content:** If a bank requires matched-maturity FTP, define instrument cash flows, curve, liquidity premium, prepayment, option, term, currency, allocation, and reconciliation, using [14] as capability context. Do not treat FTP as SPV cash unless contractually charged.

For valuation, distinguish sponsor cash and any market-consistent asset valuation. Use `PD_Q` only after market calibration [20]. For rate risk, build asset and liability repricing ladders, floors, caps, reset lags, runoff, and scenarios. Call it SPV KESONIA basis and repricing risk unless IRRBB legally applies. Use [7] for bank methodology.

**Acceptance tests:** NII and present-value changes derive from dated cash flows. Stress is dimensionally correct. Bank ALM, SPV cash, and sponsor valuation do not share one rate.

### D09-P11: Rebuild Monte Carlo as a governed extension of the deterministic model

**Action:** Replace the Appendix code and narrative.

**Resolves:** D09-I04 and D09-I12.

**Content:** Put production code in a versioned repository. Load assumptions from controlled input tables. Simulate origination, defaults, dependence, recoveries, lag, prepayment, rates, FX if any, servicing interruption, and hedge events, then run the exact deterministic waterfall. Separate process, parameter, and scenario uncertainty. Pin seed, dependencies, environment, and output hash.

Validate simulation against no-default, deterministic-default, independent, and stressed-dependence cases. Report distributions of DSCR, OC, reserve, trigger month, and tranche losses. Add reverse stress.

**Acceptance tests:** Monte Carlo mean converges to deterministic expectation in simple cases. Every chart links to model version and assumptions. No code comment acts as a source.

### D09-P12: Add model governance, source audit, and publication controls

**Action:** Rewrite conclusion and references.

**Resolves:** D09-I12 and D09-I13.

**Content:** Record owner, reviewer, version, assumption source, rate vintage, code, workbook, validation, change, and approval. Create a source-audit table linked to the IEEE index. Mark unsupported assumptions as diligence requirements. Link D03 terms to workbook cells and D08 journals.

**Acceptance tests:** A reviewer can reproduce outputs from retained artifacts. Automated scans find no standalone `K`, formula corruption, long dash, 2.5 million HoldCo amount, 12.06% hardcode, or unqualified regulatory benefit.

## Recommended editing order and reviewers

Perform P01 through P04 first. Freeze D03 terms before P05. Obtain tax and accounting decisions before P06 and P08. Build deterministic cohorts and waterfall before Monte Carlo. Add FTP and valuation only where a decision use exists. Complete governance and sources last.

Required reviewers include financial modeller, lender treasury and credit, CBK pricing compliance, tax adviser, IFRS adviser or auditor, servicing and finance operations, model validator, transaction counsel, carrier finance, data engineer, ALM or FTP specialist if used, investor, and internal audit.

## Pre-publication validation checklist

- Rate taxonomy and notation are unique.
- CBK pricing formula matches [1], [2].
- KESONIA compounding passes known-answer tests.
- Stack, advance, OC, reserve, and waterfall reconcile.
- Tax and fees have sources or visible provisional status.
- Cohorts and debt schedules roll forward.
- IFRS 9 and 17 boundaries are correct.
- FTP, valuation, and stress have separate purposes.
- Monte Carlo runs the exact waterfall.
- Every output is reproducible and cited.

## Workbook implementation map

Translate the revised paper into controlled workbook modules: Cover and Summary; Assumptions and Sources; Scenario Control; KESONIA Calendar and Compounding; Customer Pricing; Origination Drivers; IPF, Microloan and Revolver Cohorts; Collections and Losses; SPV Cash Flow; Waterfall; Class A and B Debt; Reserves and OC; Covenants; Returns; Sensitivities; HoldCo Overlay; Accounting Interface; Tax and Fees; Checks; and Source Audit. Each D09 formula should map to a sheet and named range.

Inputs use consistent colours and status fields. Formulas use bounded references and avoid `@`, structured references, full-column scans, `INDIRECT`, `OFFSET`, hidden hardcodes, external links, and unsupported circularity. KESONIA observations should be imported or pasted into a controlled table with date, rate, scale, source, publication, approval, and vintage. Posted periods remain locked and corrections appear as adjustments.

Build check rows for stack percentage, sources and uses, cohort roll-forward, cash, debt, reserve, borrowing base, OC, waterfall allocation, interest accrual, tax, KES and USD translation, scenario propagation, and output tie. The Summary should show model status and the highest-priority failure. Every chart and narrative output must derive from formula cells.

## Independent model validation and model-use controls

An independent reviewer should inspect scope, formulas, inputs, benchmark conventions, tax, accounting, cash timing, cohort curves, default and recovery, dependence, FX, hedge, reserve, waterfall, covenants, and returns. The review should reproduce a sample KESONIA period and trace one product cohort through collection, default, recovery, cash, debt service, and investor distribution.

Use sensitivity and reverse-stress tests to identify assumptions driving Class A and B loss. Test zero originations, zero defaults, immediate default, zero recovery, delayed recovery, high prepayment, platform concentration, carrier refund failure, KESONIA shock, margin change, tax change, FX shock if applicable, servicing disruption, reserve shortfall, and early amortization. Confirm discontinuities occur only where contractual rules create them.

Define approved uses: transaction structuring, lender diligence, scenario analysis, budgeting, and investor reporting. Prohibit customer pricing or accounting posting directly from an unapproved workbook. Record owner, version, review date, limitations, and expiry. Revalidate after material product, facility, benchmark, tax, accounting, or data change.

## Financial disclosure and claim-control table

Create a table for every headline claim in D01, D02, D03, D09, and the lender presentation. State claim, formula, workbook location, scenario, as-of date, currency, period, assumptions, sensitivity, owner, and permitted wording. For example, “no Class A principal loss” is permitted only as “the selected model scenario projects no Class A principal loss under the listed assumptions.”

The table should block publication of yields without gross or net basis, defaults without horizon, recovery without timing, DSCR without definition, OC without denominator, reserve without included debt service, or returns without cash-flow dates. This is the final defence against the narrative reintroducing the inconsistencies that the revised model removes.

## Definition of done

D09 is complete when customer price, asset cash, note cash, fees, tax, reserve, waterfall, accounting, valuation, and rate-risk calculations can be traced separately and then reconciled. The model must respond coherently to KESONIA, default, recovery, timing, advance-rate, OC, tax, and FX assumptions without double counting or unsupported regulatory claims.

## Periodic benchmark and assumption review

Review KESONIA sources and contractual conventions on each model update, and review pricing, portfolio, recovery, tax, fee, hedge, and liability assumptions at least quarterly during the pilot. Keep original vintages for reproduction. Any change that affects customer cost, investor return, accounting, covenant, or protection claim must trigger revalidation and cross-document reconciliation before publication.
