# D03 Implementation Plan: SPV Financial Term Sheet

## Objective and legal status

Rewrite D03 as a comprehensive non-binding commercial term sheet that can instruct counsel, the financial modeller, rating or risk advisers, the servicer, the trustee, and prospective Class A and B investors. It should contain enough defined mechanics for two independent readers to calculate the same borrowing base, waterfall, trigger status, and expected return. It should not claim to be the definitive agreement, a legal opinion, an accounting policy, or a regulatory approval.

The revised term sheet should include a clear precedence statement: executed finance documents prevail; before execution, D03 controls financing assumptions used in D01, D09, and the workbook. Technical papers cannot silently change commercial terms. All values are proposed and subject to diligence, credit approval, tax, legal, accounting, hedge, and regulatory review.

## Proposed document architecture

1. Cover, status, parties, transaction purpose, and definitions.
2. Facility, currency, accounts, and conditions precedent.
3. Asset purchase, eligibility, borrowing base, and concentration.
4. Capital stack, benchmark, margins, fees, and hedge.
5. Revolving period, amortization, and cash waterfalls.
6. Credit enhancement, reserves, and permitted investments.
7. Covenants, triggers, cures, early amortization, and events of default.
8. Servicing, reporting, data, model, and audit rights.
9. Accounting, tax, regulatory, ESG, and customer protections.
10. Representations, undertakings, transfer, governing law, and next steps.
11. Schedules for definitions, eligibility, calculations, reports, and sources.

## Section-level implementation actions

### D03-P01: Add document control, party definitions, and precedence

**Action:** Add a cover and replace the opening.

**Resolves:** D03-I10.

**Content:** Include version, date, validity period, sponsor, proposed issuers and investors, confidentiality, non-binding status, governing-law proposal, and reservations. Define HoldCo, OpCo if retained, originator, seller, SPV, servicer, backup servicer, trustee or security agent, collection-account bank, hedge counterparty, carrier, platform, driver, Class A, Class B, and Class C.

Define terms such as Business Day, Calculation Date, Collection Period, Payment Date, Revolving Period, Amortization Period, Early Amortization Event, Event of Default, Eligible Receivable, Defaulted Receivable, Delinquent Receivable, Purchased Receivable, Collections, Principal Collections, Finance Charge Collections, Recoveries, Cash Available, and Required Reserve.

**Acceptance tests:** Every capitalised term used later has one definition. D03 states that it controls the model assumption set. There is no conflict between “facility,” “capitalization,” and “consolidated funding.”

### D03-P02: Freeze the transaction perimeter, currency, and legal conditions

**Action:** Rewrite Section 1.

**Resolves:** D03-I01 and D03-I07.

**Content:** Set the primary SPV capitalization at USD 9 million equivalent, denominated and settled in KES under the canonical case. State the conversion rate used for headline reporting and that principal obligations are KES. Put the optional USD 1 million HoldCo facility outside D03 or in a clearly non-SPV note. If investors require USD obligations, replace the canonical case only through a formal term decision and add full hedging terms.

List conditions precedent: incorporated and bankruptcy-remote SPV; constitutional restrictions; executed receivables sale; true-sale, perfection, non-consolidation, enforceability, tax, and data opinions; licences; carrier and platform agreements; controlled accounts; servicing and backup servicing; KYC and AML; privacy DPIA; financial model approval; initial borrowing-base certificate; Class C funding; insurance and business continuity; and hedge documents where applicable.

**Acceptance tests:** Operating currency, note currency, reporting currency, and hedge treatment are each explicit. HoldCo use of proceeds cannot be paid from SPV cash. Legal remoteness is conditional on documents and conduct.

### D03-P03: Create an asset purchase and borrowing-base schedule

**Action:** Add after Facility Overview.

**Resolves:** D03-I02 and D03-I05.

**Content:** Define the purchase mechanism and price for IPF, microloan, and revolving receivables. Specify whether purchases are true sales at par, discount, or formula price. List eligibility: valid contract, licensed origination, customer consent and disclosure, KES denomination, current insurance or product status, platform and geography, minimum data, maximum delinquency, no fraud flag, no dispute, no set-off, no prior sale, correct documentation, and remaining tenor.

Define ineligibility and haircuts for arrears, concentration, dilution, carrier refund uncertainty, platform exposure, data defects, and product caps. The borrowing base should be a sum of eligible principal or purchase value multiplied by product advance rates, less reserves and deficiencies. Define frequency, preparer, verification, dispute, and cure.

Separate the Class A 75% capital share from any 75% funding assumption. State OC as eligible receivables divided by A plus B. Show the illustrative USD-equivalent calculations and label them non-operative until KES closing amounts are set.

**Acceptance tests:** A modeller can reconstruct the borrowing base without inference. A sold receivable has one owner and unique identifier. Ratios name numerator, denominator, currency, and date.

### D03-P04: Replace yield headlines with complete rate terms

**Action:** Rewrite Section 2.

**Resolves:** D03-I01 and D03-I03.

**Content:** Class A principal is KES equivalent of USD 6.75 million at closing; Class B is KES equivalent of USD 1.35 million; Class C is KES equivalent of USD 0.90 million. Class A accrues compounded KESONIA in arrears plus `m_A`; Class B accrues compounded KESONIA plus `m_B` or an expressly negotiated fixed coupon. State margin assumptions as illustrative until lender quotes exist.

Add day-count, reset period, observation period, lookback or lag, observation shift, business-day calendar, floor, cap if any, rounding, publication fallback, CBR fallback, payment dates, default interest, and withholding gross-up policy. State that 91-day T-bill is a comparison metric unless elected by amendment. Define upfront, commitment, trustee, servicing, backup servicing, hedge, and legal fees and who bears them.

**Acceptance tests:** The coupon can be calculated for a sample period from CBK rates. Customer `K_RBCP` does not appear in note coupon formulas. Basis risk is identified and stressed.

### D03-P05: Write the revolving, amortization, and waterfall mechanics

**Action:** Replace Section 3 and expand it.

**Resolves:** D03-I02, D03-I04, and D03-I05.

**Content:** Define initial funding, revolving-period conditions, permitted reinvestment, purchase dates, commitment expiry, scheduled amortization, legal final maturity, and cleanup call if any. Add separate pre-enforcement, early-amortization, and enforcement waterfalls.

The normal waterfall should allocate statutory and trustee expenses, servicing and backup servicing, hedge payments where agreed, Class A interest, Class A principal required under schedule or borrowing-base deficiency, Class B interest, Class B principal, reserve replenishment, permitted purchases during an active revolving period, and Class C residual. Define allocation of principal collections, finance charges, recoveries, insurance refunds, fees, and hedge receipts. Define pro rata versus sequential principal and whether Class B interest can be deferred.

The early-amortization waterfall should stop purchases and residual distributions and sweep cash sequentially to Class A then Class B after senior costs and interest. The enforcement waterfall should address security realisation and hedge termination.

**Acceptance tests:** Cash Available is fully allocated or retained in a named account. Equity receives nothing when a blocking condition applies. The model reproduces all three waterfalls and passes a zero-cash and excess-cash test.

### D03-P06: Add servicing, accounts, security, and operational continuity

**Action:** Add new section.

**Resolves:** D03-I05 and D03-I07.

**Content:** Define collection accounts, reserve account, permitted investments, account control, daily sweep, commingling limit, reconciliation, platform settlement, carrier refund account, and bank-statement access. Specify security over receivables, accounts, rights, data and servicing records to the extent lawful.

Define servicer duties, standard of care, collections policy, modifications, waivers, complaints, data maintenance, monthly report, audit, and cash transfer. List servicer termination events, notice, transition cooperation, data and credential escrow, backup servicer activation, costs, and customer communication. Address platform and carrier replacement or suspension.

**Acceptance tests:** A servicing outage has a documented cash and data continuity path. Every controlled account has owner, bank, currency, signatory, permitted debit, and reconciliation. The SPV can transfer servicing without losing essential lawful data.

### D03-P07: Convert headline covenants into executable tests

**Action:** Rewrite Section 4.

**Resolves:** D03-I04 and D03-I06.

**Content:** Create a schedule for OC 125%, Required Reserve of three months, NPL 6.5%, platform 25%, urban geography 15%, product limits, carrier and bank concentrations, arrears, cumulative net loss, excess spread, data quality, hedge, payment, servicing, representation breach, and model-governance triggers.

For every test define numerator, denominator, eligible population, observation window, frequency, source system, calculation agent, verification, threshold, warning, breach, cure, dispute, and consequence. Define PSI 0.25 as a contractual or policy monitoring trigger, not law. Consequences may include investigation, challenger review, purchase suspension, borrowing-base haircut, reserve cure, early amortization, or Event of Default, with proportional sequencing.

Add distribution conditions and a highest-priority breach rule. Include reverse stress and lender consent for material model, policy, product, servicer, platform, carrier, data, or contract changes.

**Acceptance tests:** The workbook gives the same PASS or FAIL as the written formula for boundary values. At exactly 6.5% NPL, the intended treatment is explicit. Trigger consequences do not depend on an undefined discretion.

### D03-P08: Add FX, hedge, tax, and payment protections

**Action:** Add only to the extent relevant after currency choice.

**Resolves:** D03-I01 and D03-I07.

**Content:** Under the KES canonical case, state that USD values are reporting translations and investors bear translation outside the SPV. If USD notes are selected, define hedge notional, amortization, counterparty rating, collateral, termination, replacement, mismatch, payment priority, and unhedged limits. Include account-bank replacement and permitted-investment criteria.

State taxes, withholding, gross-up, stamp, VAT or excise, deductibility, and tax-reserve treatment as subject to Kenyan advice. Do not assume a Class A-only tax shield. Define payment mechanics, business-day convention, interest shortfall, principal shortfall, and record date.

**Acceptance tests:** No reserve is described as an FX hedge. Tax inputs in the workbook trace to the term sheet or are explicitly provisional. Hedge termination is included in stress.

### D03-P09: Rebuild regulatory, accounting, ESG, and customer protections

**Action:** Rewrite Section 5.

**Resolves:** D03-I08 and D03-I09.

**Content:** Identify the SPV's IFRS 9 reporting responsibilities and the carrier's IFRS 17 responsibilities [5], [6]. State that lender prudential capital is determined by the lender and applicable CBK rules; no IRB benefit is promised [8]. Include compliance with applicable Kenyan credit, insurance, data-protection, consumer, AML, sanctions, and tax requirements, subject to counsel.

Turn ESG claims into reporting metrics: active insurance continuity, income stabilisation, complaint rate, appeal resolution, intervention receipt and effect, pricing distribution, protected or proxy group outcomes where lawful, road-safety events, and customer net cash effect. Define data minimisation, privacy notices, DPIA, automated-decision explanation, and incident reporting [10], [11].

**Acceptance tests:** Accounting standards are assigned to entities. Comparative foreign guidance is labelled. ESG metrics have definitions and reporting frequency.

### D03-P10: Add reporting, representations, events of default, and closing process

**Action:** Add final operative sections and schedules.

**Resolves:** D03-I10 and closes all findings.

**Content:** Specify daily or monthly cash and operational data, monthly investor report, quarterly financials and model monitoring, annual audited statements, ad hoc incidents, and lender audit rights. Add representations for organisation, authority, licence, receivable validity, title, no prior assignment, data accuracy, compliance, taxes, contracts, litigation, security, and model-use limits. Add undertakings for separateness, permitted business, debt, distributions, accounts, insurance, systems, data, servicing, and change control.

Define Events of Default separately from early-amortization events: payment failure, insolvency, unenforceability, material representation breach, unremedied covenant breach, loss of licence or key contract, servicing failure, account-control failure, hedge failure if material, fraud, data loss preventing enforcement, and judgment. State acceleration, enforcement, and voting by class.

End with diligence workplan, drafting responsibility, target closing, costs, exclusivity if any, and required approvals.

**Acceptance tests:** Each lender protection has an operative consequence. Reporting supplies every calculation input. No narrative paper can change D03 without documented amendment.

## Workbook and legal drafting handoff

Create a term-to-model matrix with one row for every amount, rate, fee, date, eligibility rule, haircut, trigger, account, and waterfall step. Columns should show D03 clause, workbook sheet and cell or named range, source status, legal-document destination, calculation owner, and test case. The modeller should not introduce silent assumptions; unresolved terms go to a visible assumption register.

Counsel should convert D03 into note subscription, receivables sale, servicing, security, account-control, intercreditor, hedge, data, platform, carrier, and trustee documents. A legal-issues list should record where a commercial assumption depends on licensing, perfection, consumer rights, privacy, set-off, assignment, or tax. The final term sheet should remain concise through schedules, not by omitting mechanics.

## Recommended editing order and reviewers

Perform P01 and P02 first. Complete P03 through P05 jointly with the financial modeller, originator, servicer, and lender. Complete P06 with operations, platform, account bank, and counsel. Complete P07 only after model tests exist. Complete P08 and P09 with treasury, tax, accounting, regulatory, privacy, and ESG reviewers. Finish P10 and the term-to-model matrix last.

Required reviewers include transaction counsel, Kenyan regulatory counsel, tax adviser, auditor or accounting adviser, lender credit, lender treasury, lender operations, SPV director, servicer and backup servicer, trustee or security agent, account bank, hedge adviser if used, carrier, platform, data-protection officer, model validator, and financial modeller.

## Pre-publication validation checklist

- Stack totals and KES closing equivalents reconcile.
- Currency and hedge choice is explicit.
- Borrowing base and OC use distinct, reproducible formulas.
- KESONIA coupon calculation passes sample tests.
- Normal, early-amortization, and enforcement waterfalls reconcile cash.
- Reserve and all covenants pass boundary testing.
- Eligibility and concentration calculations use the same portfolio grain.
- Legal conditions and servicing transition are complete.
- Accounting, prudential, privacy, and ESG responsibilities are assigned.
- Every assumption maps to the workbook and a drafting destination.
- No guarantee or unsupported capital-relief claim remains.

## Negotiation issues and scenario decisions

Before circulation to investors, prepare a negotiation matrix that distinguishes sponsor opening position, minimum acceptable position, lender request, rationale, financial-model sensitivity, legal consequence, and approval authority. At minimum cover Class A and B margins, margin floor, maturity, revolving period, amortization, commitment and unused fee, reserve months, OC, advance rates by product, eligibility, concentration, excess-spread capture, default definition, early-amortization thresholds, cure, servicing fee, backup servicing, hedge, permitted investments, reporting, voting, transfer, indemnity, and costs.

The matrix should expose coupled terms. A higher advance rate may require more Class C, tighter eligibility, a larger reserve, or stronger cash sweep. A longer revolving period increases reinvestment and model risk. A fixed Class B coupon may reduce benchmark basis but create different fair-value and refinancing effects. A USD note may broaden investors but adds hedge liquidity and termination risk. Model each coupled change rather than negotiating a percentage in isolation.

Prepare at least five term scenarios: sponsor base; lender conservative; lower advance and lower margin; higher advance and larger first loss; and early-amortization stress. Each scenario should show closing collateral, borrowing capacity, OC, reserve, expected debt service, minimum DSCR, Class A and B yield, Class C IRR, break-even loss, and required sponsor cash. The term sheet should not contain a scenario value that the workbook cannot reproduce.

## Data and calculation-agent specification

Add a schedule naming the calculation agent and backup, data cut-off, source systems, file formats, time zone, late data, correction, approval, and record retention. Define receivable-level fields, product states, customer and contract identifiers, platform and geography classifications, balances, collections, arrears, default, recovery, eligibility, and currency. State whether lender calculations prevail, are subject to agent verification, or follow a dispute process.

Create sample certificates for borrowing base, reserve, OC, concentrations, servicer report, waterfall, and early amortization. Use one golden portfolio with known results so the servicer, agent, trustee, investor, and workbook produce the same answer. Include negative cases for duplicate receivable, late collection, disputed policy refund, platform reclassification, stale score, and retroactive correction.

The final data schedule should also grant audit, sample testing, source-document access, model-version disclosure, incident notice, and retention rights proportionate to lender needs and privacy law. Where personal data are unnecessary, provide aggregated or pseudonymised reporting with controlled drill-down.

## Definition of done

D03 is done when counsel can draft definitive documents and the modeller can build the complete SPV without inventing a material term. Two independent calculation agents must obtain the same borrowing base, OC, reserve, interest, waterfall, covenant status, and early-amortization result from the same data. D01 and D09 must then be reconciled to this approved version.
