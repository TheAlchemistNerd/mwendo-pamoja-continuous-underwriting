---
title: "Mwendo Pamoja SPV Financial Term Sheet"
subtitle: "Narrative discussion draft for a KES receivables facility"
author: "Nevil Maloba"
date: "24 August 2026"
status: "Indicative, non-binding, subject to diligence and definitive documents"
output:
  word_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
  pdf_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
---

**Confidential and proprietary**

**Proposed issuer:** A newly incorporated Mwendo Pamoja receivables SPV
**Technology provider and proposed servicer:** Mwendo Pamoja HoldCo or its operating subsidiary
**Originator:** A licensed or otherwise authorised lender identified in the definitive structure
**Primary facility:** KES-funded notes with a USD 9,000,000 equivalent headline
**Optional HoldCo facility:** USD 1,000,000 equivalent, legally and economically outside the SPV
**Consolidated funding narrative:** USD 10,000,000 equivalent

## How to read this term sheet

This document turns the wider Mwendo Pamoja story into a concise financing conversation. The driver earns and repays in Kenya shillings. The insurer issues the motor policy. A licensed lender originates the credit. Mwendo Pamoja supplies technology, decisioning, and servicing. The SPV purchases only eligible receivables and applies collections for investors.

The terms below are indicative. They do not constitute an offer, a commitment, regulatory approval, a true-sale opinion, an accounting conclusion, or a guarantee of principal. Rates, thresholds, fees, losses, recoveries, currency equivalents, and dates must be confirmed against a data tape, financial model, legal structure, tax advice, partner contracts, and negotiated transaction documents.

## 1. Transaction overview

| Item | Indicative term |
|---|---|
| Structure | Bankruptcy-remote receivables SPV issuing tranched asset-backed notes |
| Assets | Eligible Insurance Premium Financing receivables, short-term working-capital microloans, and any approved revolving receivables |
| Borrower population | Eligible gig-economy drivers and riders on contracted partner platforms |
| Operating currency | KES |
| Headline reporting | USD equivalent at the model reporting rate |
| Purchase period | 12-month revolving purchase period |
| Amortisation period | Six-month managed amortisation, subject to extension, clean-up, and early-amortisation terms |
| Interest payment | Monthly in arrears |
| Advance rate | 75% against eligible receivables under the defined borrowing-base convention |
| Minimum OC | 125% of eligible receivables against Class A plus Class B outstanding |
| SPV CRA | Three months of defined forward Class A and Class B debt service |

The SPV is intended to purchase receivables under a receivables purchase agreement. Bankruptcy remoteness and true sale depend on legal opinions, perfection of security, account control, servicing continuity, restrictions on commingling, set-off analysis, and the facts of the transfer. The SPV does not fund HoldCo payroll, engineering, or expansion.

## 2. Capital stack and return basis

| Tranche | Share | USD-equivalent headline | Target investor | Indicative return basis | Priority |
|---|---:|---:|---|---|---|
| **Class A senior notes** | 75% | USD 6,750,000 | Commercial banks and DFIs | Compounded KESONIA in arrears plus \(m_A\) | First |
| **Class B mezzanine notes** | 15% | USD 1,350,000 | Structured credit and impact funds | Negotiated fixed KES yield or KESONIA plus \(m_B\); 18%-22% is an illustrative range | Second |
| **Class C first-loss equity** | 10% | USD 900,000 | Sponsor and eligible co-investors | Residual return after all release tests | Subordinated |
| **Total SPV** | **100%** | **USD 9,000,000** |  |  |  |

Class A is protected by 25% nominal subordination at inception, but subordination is not a guarantee. Timing of default, recovery, fees, reserve use, concentration, dilution, set-off, servicing continuity, and currency all affect actual protection.

KESONIA is the proposed primary KES reference rate [1]. Definitive documents should state the compounding formula, observation window, day count, payment lag, floor, non-publication rule, disruption fallback, replacement benchmark process, and margin. The 91-day Treasury bill may be shown as a market comparator or negotiated fallback, but it is not the base index in this term sheet.

The customer rate is separate from the note rate. Where CBK's revised risk-based pricing framework applies:

\[
R_{\mathrm{customer}}=\mathrm{KESONIA}+K_{\mathrm{RBCP}},
\]

with fees and charges added to determine total cost of credit [2], [3]. \(K_{\mathrm{RBCP}}\), \(m_A\), \(m_B\), expected loss, and regulatory capital are separate quantities.

## 3. Borrowing base, advance rate, and OC

An asset becomes eligible only if it satisfies the final criteria, which should address product, documentation, consent, lender authority, policy status, delinquency, remaining tenor, concentration, data quality, set-off, fraud, and any required insurance or platform agreement.

The initial collateral implication of a 75% advance rate is:

\[
\mathrm{EligibleReceivables}_0
=\frac{\mathrm{SPVCapital}_0}{0.75}
=\frac{9.0}{0.75}
=12.0\text{ million USD equivalent}.
\]

The debt-note OC test is:

\[
OC_t
=
\frac{\mathrm{EligibleReceivables}_t}
{\mathrm{ClassA}_t+\mathrm{ClassB}_t}.
\]

At inception, using USD-equivalent headline values:

\[
OC_0=\frac{12.0}{6.75+1.35}=148.15\%.
\]

The minimum 125% covenant is tested separately. This explicit denominator prevents the advance rate from being mistaken for the OC ratio.

## 4. Cash control and priority

Collections should pass through a controlled account held with the appointed account bank. A platform split-settlement instruction is effective only when the commercial and legal parties have agreed it and the reconciliation works. Driver reserve pockets and the SPV CRA are separate accounts with separate owners and purposes.

**Figure 1: Indicative SPV flow of funds**

~~~mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#EAF2F8", "primaryBorderColor": "#2E6F95",
  "secondaryColor": "#EAF7EE", "tertiaryColor": "#F7EEF8",
  "lineColor": "#526D82"
}}}%%
flowchart LR
    INV["Class A + Class B investors"] -->|"note proceeds in KES"| SPV["Receivables SPV"]
    EQ["Class C investor"] -->|"first-loss capital"| SPV
    SPV -->|"purchase price"| ORG["Licensed originator"]
    ORG -->|"eligible receivable"| SPV
    DR["Drivers / riders"] -->|"contractual repayments"| CA["Controlled collection account"]
    PLAT["Partner platform"] -->|"permitted split settlement"| CA
    CA --> WF["Priority of payments"]

    subgraph WATERFALL["Indicative waterfall"]
        W1["1. Taxes, trustee and account costs"]
        W2["2. Approved servicing and continuity costs"]
        W3["3. Class A interest"]
        W4["4. Class A principal / senior sweep"]
        W5["5. Class B interest"]
        W6["6. Class B principal"]
        W7["7. CRA replenishment"]
        W8["8. Residual to Class C if release tests pass"]
        W1 --> W2 --> W3 --> W4 --> W5 --> W6 --> W7 --> W8
    end

    WF --> W1
    W7 --> CRA["SPV CRA"]
~~~

The final waterfall may change through negotiation. No Class C distribution is permitted while senior interest or principal is unpaid, the OC test fails, the CRA is below requirement, early amortisation is active, or another distribution condition is uncured.

## 5. Credit enhancement

- **Subordination:** Class C absorbs allocated portfolio losses before Class B, and Class B before Class A, subject to the transaction documents.
- **Overcollateralisation:** Minimum 125% eligible-receivable coverage against Class A plus Class B.
- **SPV CRA:** Required balance equal to three months of defined forward debt service, with funding, replenishment, investment, and release rules.
- **Excess spread:** Asset yield after expected loss, funding, servicing, trustee, hedge, tax, and operating costs. It must be demonstrated by the model.
- **Eligibility and concentration:** Excludes assets that fail documented criteria and restricts common dependencies.
- **Stop-purchase and early amortisation:** Redirects cash from new purchases and residual distributions to senior repayment when defined events occur.
- **Servicing continuity:** Requires data export, controlled accounts, a transition plan, and a replaceable-servicer mechanism.

The 40% net recovery rate is an illustrative assumption, not a historical fact unless supported by comparable Kenyan product, vintage, collateral, cost, and timing evidence. Recovery must be modelled as cash received after legal and operating expenses and after the relevant lag. Insurance proceeds and unearned-premium refunds are governed by policy wording and should not be assumed to behave like repossession proceeds.

## 6. Covenants and triggers

| Test | Illustrative level | Consequence |
|---|---:|---|
| Population Stability Index | 0.25 | Suspend affected new originations; investigate data, population, and calibration before any retraining |
| Net NPL ratio | 6.5% over the defined measurement period | Stop asset purchases; activate early-amortisation priority |
| Single platform | 25% of eligible exposure | Exclude or defer purchases above limit |
| Single urban cluster | 15% of eligible exposure | Exclude or defer purchases above limit |
| OC | Below 125% | Distribution lock and cure |
| CRA | Below required balance | Distribution lock and replenish |
| Data or servicing failure | As defined in service levels | Fallback, controlled run-off, replacement, or event of default depending on severity |

PSI is a model-monitoring heuristic and proposed contractual control, not a universal regulatory threshold. The definition of NPL, numerator, denominator, cure, dispute process, calculation agent, and testing frequency must appear in definitive documents. An early-amortisation event stops new purchases and changes cash priority; it does not require an uncontrolled fire sale.

## 7. Accounting, legal, data, and conduct conditions

- The SPV or other asset holder evaluates financial instruments and ECL under IFRS 9 [4].
- The licensed insurer evaluates insurance contracts within its applicable IFRS 17 responsibilities [5].
- The originator, servicer, insurer, and platform responsibilities require a written licence and entity map.
- Receivable sale, security, account control, tax, withholding, insolvency, set-off, consumer-credit, insurance, and data-protection opinions are conditions to closing.
- Data collection and automated decision support require a documented lawful basis, purpose limitation, security, retention, driver communication, challenge process, and any necessary impact assessment under Kenya's Data Protection Act [6].
- Driver-facing premium holidays, restructuring, or maintenance support require a named funding source and accounting treatment. Their cost is not automatically allocated to Class C merely because Class C is first loss.

## 8. Currency treatment

The base SPV is funded and serviced in KES because its receivables are denominated and collected in KES. USD amounts are reporting equivalents. If investors require an actual USD note, the parties must execute and model a hedge or specify how unhedged currency loss is allocated. Naming TCX or any other provider does not create a hedge; a facility requires counterparty agreement, pricing, collateral, tenor, termination, and settlement terms.

## 9. Conditions precedent and diligence

Closing should be subject to, at minimum:

1. Satisfactory portfolio tape and cohort-level cash-flow model.
2. Confirmed originator and servicing authority.
3. Executed insurer, platform, lender, account-bank, trustee, and servicing arrangements.
4. True-sale, security, enforceability, insolvency, tax, accounting, insurance, and data-protection analysis.
5. Independent model validation, feature-ownership register, performance thresholds, fallback, and monitoring plan.
6. Agreed eligibility, borrowing base, concentration, reserve, trigger, waterfall, reporting, and audit definitions.
7. Evidence that customer pricing, fees, deductions, and hardship treatment comply with applicable requirements.
8. Funded Class C and CRA in the agreed amounts.
9. Servicing continuity and disaster-recovery tests.
10. Investment committee and all required regulatory, corporate, and counterparty approvals.

## Selected IEEE references

[1] Central Bank of Kenya, "Kenya Shilling Overnight Interbank Average (KESONIA)." [Online]. Available: https://www.centralbank.go.ke/kesonia/. Accessed: Aug. 24, 2026.

[2] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Nairobi, Kenya, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. Accessed: Aug. 24, 2026.

[3] Central Bank of Kenya, "Issuance of a revised risk-based credit pricing model," Press Release, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/uploads/press_releases/2044081907_Press%20Release%20-%20Issuance%20of%20a%20Revised%20Risk-Based%20Credit%20Pricing%20Model.pdf. Accessed: Aug. 24, 2026.

[4] IFRS Foundation, "IFRS 9 Financial Instruments." [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/. Accessed: Aug. 24, 2026.

[5] IFRS Foundation, "IFRS 17 Insurance Contracts." [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/. Accessed: Aug. 24, 2026.

[6] Republic of Kenya, *Data Protection Act, 2019*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24. Accessed: Aug. 24, 2026.
