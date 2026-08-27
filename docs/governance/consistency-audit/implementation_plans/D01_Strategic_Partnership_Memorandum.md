# D01 Implementation Plan: Strategic Partnership Memorandum

## Objective and target reader

Rewrite D01 as a decision memorandum for strategic counterparties and financing participants. It should explain the shared driver cash-flow problem, the proposed operating and financing structure, the underwriting and intervention logic, the evidence available, the economics requiring diligence, and the decision requested. It should not try to function as the detailed term sheet, mathematical model paper, accounting manual, or technology build guide. Those subjects should be summarised and linked to D03, D05, D06, D07, D08, and D09.

The revised memorandum should be readable by a bank executive, carrier executive, platform general manager, DFI investment officer, and transaction counsel. A reader must be able to distinguish: current fact, proposed responsibility, illustrative assumption, calculated model output, and unresolved condition. The document should be dated and explicitly non-binding unless counsel chooses another form.

## Proposed document architecture

Use this sequence:

1. Document status, parties, decision requested, and evidence legend.
2. Executive proposition and problem definition.
3. Entity, counterparty, and contractual responsibility model.
4. Product and customer cash-flow mechanics.
5. Canonical underwriting, feature, and policy architecture.
6. Primary SPV financing structure and optional HoldCo overlay.
7. Waterfall, credit enhancement, and covenant framework.
8. Accounting, regulation, privacy, and intervention governance.
9. Illustrative economics and scenario results.
10. Implementation, diligence, conditions, and next decision.
11. Definitions, sources, assumptions, and cross-document controls.

## Section-level implementation actions

### D01-P01: Add a controlled cover and evidence legend

**Action:** Add before the existing Executive Summary.

**Resolves:** D01-I07 and D01-I11.

**Content:** State title, version, as-of date, owner, audience, confidentiality, and non-binding status. Name the ten-document set and declare that D03 controls commercial terms until definitive documents supersede it. Add a five-status evidence legend: `Source-backed`, `Derived`, `Illustrative assumption`, `Target`, and `Model output`. Explain that `glossary.md` is not an evidence source. Include a two-sentence warning that portfolio tape and executed partner agreements are not yet available if that remains true.

**Acceptance tests:** Every material number in the memorandum carries one status. The page names the reporting currencies and the effective date. No reader could reasonably interpret an illustrative rate as historical performance.

### D01-P02: Rewrite the Executive Summary around one financing request

**Action:** Rewrite Section 1 and split the current funding paragraph from the solution thesis.

**Resolves:** D01-I01 and D01-I07.

**Content:** Begin with the decision sought: permission to proceed to structured diligence for a USD 9 million equivalent KES SPV and optional USD 1 million HoldCo facility. State the consolidated USD 10 million view only after the separate uses are clear. Summarise the product pool, continuous risk monitoring, early intervention hypothesis, and ring-fenced cash flows. Replace any 35% yield, default, recovery, origination, or lead-time claim with either a sourced result or an illustrative range linked to the model. End with the four approval conditions: partner contracts, legal and regulatory review, validated portfolio economics, and operational pilot readiness.

**Move:** Detailed architecture descriptions to the later architecture section. Move exact tranche terms to financing and D03.

**Acceptance tests:** USD 9 million plus USD 1 million equals the only USD 10 million consolidated view. No USD 2.5 million HoldCo request remains. The summary contains no guarantee language.

### D01-P03: Replace the counterparty table with a legal and operational responsibility matrix

**Action:** Rewrite Section 1.1 and expand it.

**Resolves:** D01-I02, D01-I08, and D01-I10.

**Content:** Use rows for HoldCo, OpCo if retained, licensed lender or originator, SPV, carrier, platform, servicer, backup servicer, trustee or security agent, collection-account bank, hedge counterparty, Class A, Class B, Class C, and driver. Columns should state legal role, licence or authority, asset or obligation owned, cash received or paid, data supplied, decision rights, accounting standard, and required agreement.

State explicitly that the carrier issues insurance, the SPV purchases eligible receivables, and the platform's deduction or routing powers exist only under contract. State that HoldCo owns IP but cannot use SPV cash for operating expenditure. Add a transaction-document map covering receivables sale, servicing, platform collection, carrier, account control, note subscription, security, hedging if relevant, data processing, and intercompany IP licence.

**Acceptance tests:** Each material activity has one accountable legal entity. Carrier and Insurtech are not interchangeable. True sale and non-consolidation are described as counsel conclusions subject to conditions, not software results.

### D01-P04: Rebuild the ingestion and model overview using the canonical architecture

**Action:** Rewrite Sections 2.1 and 2.2; add one compact diagram.

**Resolves:** D01-I05.

**Content:** Show raw telematics and wallet events flowing into Flink services, then branching into GRU or Transformer neural embeddings and the Explicit Liquidity Feature Path. Both enter hierarchical Bayesian underwriting, which produces posterior real-world PD and uncertainty. The Credit Policy and Compliance Gate sits downstream. State that Kappa and Redis describe low-latency computation and serving, not a rule system.

Add a feature ownership table. Assign CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and defined interactions to the explicit path. Explain that raw wallet timing may enter neural sequence learning but the named engineered metrics are not duplicated.

**Remove:** “Tabular Bypass,” any statement that explicit features themselves constitute compliance, and any claim of deterministic prevention.

**Acceptance tests:** The architecture agrees word-for-word with the master baseline. Each named feature has one owner. The policy gate is visibly after Bayesian inference.

### D01-P05: Split model outputs from policy and intervention decisions

**Action:** Rewrite Sections 2.3 and 2.4 into two subsections.

**Resolves:** D01-I05 and D01-I10.

**Content:** The first subsection should define model outputs: posterior mean and median `PD_P`, credible interval, threshold-exceedance probability, expected loss input, and cluster shock indicator. It should state that these are predictive measures and not regulatory rules. The second subsection should define the Credit Policy and Compliance Gate: licence and product eligibility, affordability or sufficiency, maximum debt, uncertainty kill-switch, product and concentration caps, insurance status, data-quality fallback, reserve and OC tests, NPL trigger, purchase stop, and distribution block.

For each intervention, identify owner, funding source, customer notice, consent where required, duration, accounting, override, appeal, and evaluation. Premium holidays require carrier and lender coordination; routing changes require platform authority; draw freezes require contract and policy.

**Acceptance tests:** No policy threshold is described as learned by the neural network. No statistical threshold is described as law without [1]-[13] or Kenyan legal authority. Each action has an accountable party.

### D01-P06: Rewrite SPV structure, currency, borrowing base, and waterfall

**Action:** Replace Section 3.

**Resolves:** D01-I01, D01-I02, D01-I03, and D01-I08.

**Content:** Start with a diagram showing receivable sale, KES collections, controlled accounts, and investor funding. Use the canonical Class A USD 6.75 million equivalent, Class B USD 1.35 million, and Class C USD 0.90 million. State KES as operating and waterfall currency, with USD investor translation. If transaction sponsors later elect USD notes, show hedging as an unresolved condition and remove “self-hedge.”

Define Class A share separately from borrowing-base advance rate. Include both illustrative calculations: USD 12 million eligible receivables from USD 9 million divided by 75%, and 148.15% debt-note OC from USD 12 million divided by USD 8.10 million. State that 125% is the minimum OC and that D03 must define eligibility and haircuts.

Summarise the waterfall: statutory and trustee costs, servicing and backup servicing, Class A interest, Class A principal, Class B interest, Class B principal, reserve replenishment, and residual distribution, subject to trigger sweeps. Explain that legal remoteness requires sale, perfection, separateness, account control, non-petition, and servicing continuity.

**Acceptance tests:** The stack sums exactly. Every ratio names its numerator and denominator. Currency and hedge treatment are unambiguous. HoldCo cash is absent from the SPV waterfall.

### D01-P07: Replace the compliance section with an applicability and accounting perimeter

**Action:** Rewrite Section 5 and move detailed formulas to D07 and D09.

**Resolves:** D01-I04, D01-I09, and D01-I10.

**Content:** Add a concise matrix for Kenyan credit pricing, IFRS 9, IFRS 17, lender prudential capital, data protection, insurance regulation, contractual covenants, and internal policy. State entity and status for each. Customer pricing should use KESONIA plus `K_RBCP` and cite [1]-[3]. Class A should use compounded KESONIA plus `m_A` under the proposed term sheet. Define CBR fallback and T-bill comparison without conflation.

State that financial-asset holders apply IFRS 9 using real-world forward-looking measures [5], while the carrier applies IFRS 17 to insurance contracts [6]. Describe Basel, Solvency II, EBA, ECOA, and SR 11-7 only with jurisdictional qualification. Add privacy and DPIA obligations using [10], [11].

**Acceptance tests:** No framework is called binding without entity and jurisdiction. `K_RBCP`, `K_cap`, `m_A`, `m_B`, `EL`, `CoC`, and `OpEx` are distinct. Risk-neutral terminology is absent unless explicitly qualified.

### D01-P08: Rebuild risk mitigation as conditional structural protection

**Action:** Rewrite Section 4 and the stress subsection of Section 6.

**Resolves:** D01-I06 and D01-I07.

**Content:** Separate legal protections, cash protections, portfolio rules, model monitoring, and operational resilience. Legal protections include true sale and controlled accounts. Cash protections include Class C, subordination, OC, reserve, excess spread, recovery, and early amortization. Portfolio rules include eligibility and concentrations. Model controls include uncertainty and drift. Operational controls include backup servicing, reconciliation, incident response, and manual fallback.

Show Base, Mild Shock, and Severe Contagion only with linked model outputs. For each display defaults, recovery and lag, collection delay, OC, reserve draw, minimum DSCR, interest shortfall, principal loss by class, and trigger month. Add reverse stress and break-even Class A loss. Replace “protected” with “the illustrative model projects no loss under stated assumptions” where true.

**Acceptance tests:** Every scenario number ties to a workbook cell or named output. Intervention effectiveness can be zero in sensitivity. No structural feature is called a guarantee.

### D01-P09: Reconstruct portfolio economics and uses of proceeds

**Action:** Rewrite Section 6 and add a separate HoldCo overlay.

**Resolves:** D01-I01, D01-I04, and D01-I06.

**Content:** Present product-level originations, average balance, tenor, gross customer yield, fees, expected loss, recovery, servicing, carrier payments, hedge cost, and cash yield. Then present SPV liabilities and waterfall returns. Add an optional HoldCo uses-of-proceeds table for engineering, regulatory work, partner integrations, data, independent validation, fairness audit, servicing readiness, legal, and transaction costs, totalling USD 1 million.

Do not use WACC as the SPV's monthly cash cost. Report Class A yield, Class B yield, and Class C IRR from actual cash flows. Label tax assumptions pending counsel. Report KES and USD translation separately.

**Acceptance tests:** Customer pricing follows [1], [2]. Note margin is not called borrower `K`. All uses total to their facilities. No unverified “historical” label remains.

### D01-P10: Add a covenant and information-rights summary

**Action:** Add after the waterfall.

**Resolves:** D01-I03 and supports D01-I06.

**Content:** Summarise OC 125%, three-month reserve, NPL 6.5%, PSI monitoring 0.25 as a contractual or policy convention, platform 25%, geography 15%, payment, data-quality, hedge, and servicing triggers. For each, name formula, measurement frequency, cure, and effect. Add lender reports: borrowing base, servicer, collections, arrears, defaults, recoveries, concentrations, reserve, OC, cash waterfall, model monitoring, incidents, and financial statements.

**Acceptance tests:** Every trigger maps to D03 and the workbook. PSI is not represented as a statute. Early amortization stops new purchases and residual distributions where contracted.

### D01-P11: Add a diligence and evidence-gap register

**Action:** Add near conclusion.

**Resolves:** D01-I07 and D01-I11.

**Content:** List the missing portfolio tape, product contracts, licences, partner agreements, carrier refund data, platform settlement data, recoveries, tax opinion, legal opinions, accounting policy, hedge quote, model validation, fairness assessment, DPIA, security assessment, servicing plan, and regulator engagement. Assign owner, due date, decision affected, and required evidence.

**Acceptance tests:** Every illustrative material input has a replacement request. Critical conditions are not hidden in footnotes.

### D01-P12: Perform final editorial and cross-document control

**Action:** Rewrite the conclusion and append definitions, assumptions, and IEEE references.

**Resolves:** D01-I11 and closes all findings.

**Content:** Use controlled entity, architecture, financial, accounting, and pricing terminology. Correct all formulas and encoding. Replace long dashes with suitable punctuation. Link references to the shared IEEE numbering. Add a document control table showing D03 controls financing, D04 product mechanics, D05 features, D06 models, D07 governance, D08 systems, D09 pricing, and D10 execution.

**Acceptance tests:** Automated scans find no “Tabular Bypass,” long dash, mojibake, unsupported guarantee, USD 2.5 million HoldCo amount, or formula corruption. All cross-references resolve.

## Recommended editing order and reviewers

Execute D01-P01 through P03 first because role, authority, and financing affect all prose. Perform P06 and P09 with the financial modeller and transaction counsel. Perform P04 and P05 with the chief data scientist, data architect, credit-risk owner, and compliance owner. Perform P07 with Kenyan regulatory counsel, IFRS adviser, carrier finance, and bank risk. Complete P08 and P10 only after the model and D03 are stable. Finish evidence and editorial actions last.

Required reviewers are sponsor executive, transaction counsel, bank credit and treasury, carrier underwriting and finance, platform commercial and data leads, SPV modeller, accountant or auditor, privacy counsel or DPO, model validator, security lead, servicer, and DFI safeguards specialist.

## Pre-publication validation checklist

- Confirm USD 9 million SPV, USD 1 million HoldCo, and USD 10 million consolidated totals.
- Confirm A, B, and C amounts and percentages.
- Confirm KES operating currency and any hedge election.
- Recalculate borrowing-base and OC examples.
- Reconcile every yield and loss to the workbook.
- Confirm customer and note pricing use distinct notation.
- Confirm feature ownership and downstream policy gate.
- Confirm insurer, lender, platform, servicer, and SPV roles.
- Confirm regulatory jurisdiction and as-of dates.
- Confirm all assumptions have evidence status.
- Confirm no source document was changed during this planning work.

## Definition of done

D01 is complete when a strategic decision-maker can approve or decline diligence based on one coherent financing request, one entity map, one model and policy boundary, one waterfall summary, conditional rather than guaranteed risk claims, and a transparent evidence-gap register. It must reconcile exactly with D03 and the financial model and must not introduce technical, accounting, or regulatory claims that contradict D05 through D09.

## Document control and change-management protocol

After the first rewrite, place D01 under a formal change protocol. Assign a document owner and create a decision log for facility amount, note currency, benchmark, advance rate, OC definition, reserve definition, product scope, and partner roles. A proposed change to any of those terms must identify the affected workbook cells and sections of D03 through D10. Finance should rerun scenarios before commercial language changes. Model governance should review any change to feature ownership, model output, threshold, or intervention. Counsel should review any change to legal responsibility, licence, customer right, data use, covenant, or protection claim.

Create a release checklist with evidence links. The final source pack should include the current D03, the approved workbook version and hash, legal and accounting issue lists, architecture diagram, model validation status, DPIA status, and the shared IEEE index. Record reviewer name, role, date, comments resolved, and any explicit reservation. Do not publish a revised memorandum when the controlling term sheet or model is still on a different version.

Run a reader test with one lender, one carrier, one platform, and one DFI reviewer who did not draft the paper. Ask each to state the facility, parties, cash source, first-loss position, model boundary, main triggers, and unresolved risks without assistance. Any inconsistent answer is a drafting defect to correct. This test ensures the memorandum performs its strategic role instead of merely containing technically accurate fragments.
