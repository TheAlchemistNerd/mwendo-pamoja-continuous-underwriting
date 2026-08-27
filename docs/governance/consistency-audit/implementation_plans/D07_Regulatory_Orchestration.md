# D07 Implementation Plan: Regulatory Orchestration and Interventions

## Objective and legal method

Rewrite D07 as a jurisdiction-aware control framework. Its purpose is to show how Kenyan legal, regulatory, accounting, prudential, data-protection, contractual, model-governance, and customer-protection requirements attach to specific entities and decisions. Comparative frameworks may be retained where they add design value, but must be labelled non-binding unless counsel establishes otherwise.

The document should not imply that technology provides compliance automatically. It should define control owners, decision evidence, reporting, escalation, and legal review. IFRS 9 and IFRS 17 are accounting standards. Basel is implemented through regulated lenders and supervisory permission. Internal credit policy, contractual covenants, statistical monitoring, and law must occupy separate layers.

## Proposed document architecture

1. Scope, as-of date, jurisdiction, and authority hierarchy.
2. Entity and regulatory-perimeter matrix.
3. Accounting perimeter: IFRS 9 and IFRS 17.
4. Lender prudential capital and SPV structural risk.
5. Model governance and monitoring.
6. Intervention, modification, forbearance, and customer treatment.
7. Fairness, automated decisions, privacy, and appeal.
8. Regulatory and contractual reporting inventory.
9. Control library, evidence model, incidents, and assurance.
10. Open legal questions, diligence, and references.

## Section-level implementation actions

### D07-P01: Add authority, notation, and equation controls

**Action:** Add before the opening framework and audit formulas.

**Resolves:** D07-I04 and D07-I11.

**Content:** State the legal review date and hierarchy: Kenyan legislation and regulator instruments; applicable IFRS; lender or insurer prudential requirements; executed contracts; approved internal policies; and statistical conventions. Add a source-status label for every rule. Re-key Basel and accounting expressions from primary sources. Define `K_RBCP`, `K_cap`, `PD_P`, `PD_Q`, ECL, RWA, SCR, PSI, SICR, default, modification, forbearance, and intervention.

**Acceptance tests:** No formula relies on corrupted punctuation. Every threshold identifies its authority. “Basel IV” is labelled informal where used.

### D07-P02: Build the jurisdiction and applicability matrix

**Action:** Replace the introductory framework.

**Resolves:** D07-I01.

**Content:** Rows should include Kenyan credit and banking law, CBK risk-based pricing, digital credit or lending licence as relevant, insurance law and IRA requirements, Kenya Data Protection Act and ODPC guidance, AML and sanctions, IFRS 9, IFRS 17, Basel implementation, tax, consumer protection, contract covenants, internal policy, Solvency II, EBA, ECOA, and SR 11-7. Columns should show source, jurisdiction, entity, topic, binding or comparative status, effective date, control owner, evidence, and legal-review status.

Foreign regimes should be retained only when they inform a voluntary control or a counterparty obligation. Remove language that suggests direct compliance where no basis exists.

**Acceptance tests:** A reader can identify exactly why each framework appears. No comparative source is placed above Kenyan authority.

### D07-P03: Freeze the regulated-entity and licence perimeter

**Action:** Rewrite the bank and Insurtech framework headings.

**Resolves:** D07-I01 and D07-I07.

**Content:** Define HoldCo, OpCo, licensed lender, SPV, carrier, platform, servicer, trustee, and data processors. State licence, regulated activities, accounting perimeter, capital regime, reporting, and prohibited activities. The carrier issues insurance and owns IFRS 17. The financial-asset holder applies IFRS 9. The platform acts only within its payment, data, and routing contracts. The technology provider does not become a carrier or bank by supplying models.

Add a responsibility matrix for origination, pricing, approval, policy issuance, premium payment, receivable sale, collections, servicing, interventions, complaints, data-subject rights, reporting, and incident notification.

**Acceptance tests:** No activity has two primary accountable entities. Licence assumptions are marked pending legal confirmation. Entity roles reconcile to D01, D03, and D04.

### D07-P04: Rebuild IFRS 9 and IFRS 17 as separate accounting workstreams

**Action:** Rewrite the impairment and insurance sections.

**Resolves:** D07-I02 and D07-I07.

**Content:** For IFRS 9, identify reporting entity, instrument, classification, EIR, staging, SICR, default, cure, write-off, modification, EAD, LGD, `PD_P`, scenarios, weighting, management overlay, controls, close timing, journal, validation, and disclosure [5]. Show how underwriting outputs may be governed inputs without being the whole ECL model.

For IFRS 17, identify carrier, policy groups, contract boundary, PAA eligibility, general model fallback, fulfilment cash flows, risk adjustment, onerous contracts, claims, premium refund, and accounting data [6]. State how an enforceable premium refund receivable reaches the SPV, with timing and haircut, without importing the carrier's accounting result into SPV capital.

**Acceptance tests:** IFRS 9 and 17 cash and journals do not overlap incorrectly. Risk-neutral PD is absent from ordinary ECL. PAA is conditional, not automatic.

### D07-P05: Reframe Basel and prudential capital as lender-owned analysis

**Action:** Rewrite the A-IRB and output-floor section.

**Resolves:** D07-I03 and D07-I04.

**Content:** Explain exposure classification, standardised versus IRB approaches, permission, long-run data, parameter estimation, validation, prescribed correlation, floors, maturity, credit-risk mitigation, and output floor at a high level using [8]. State that each lender applies its local CBK framework. The SPV and model vendor do not elect A-IRB.

Place the Clayton copula in internal economic-capital and stress analysis. Add a data pack that may help lender assessment: pool composition, historical performance, model validation, legal structure, subordination, OC, reserve, servicing, and stress. Remove promised capital relief.

**Acceptance tests:** No formula permits replacing prescribed correlation with `theta`. Any RWA estimate is labelled illustrative and lender-owned. Implementation date is as-of and jurisdiction-qualified.

### D07-P06: Create a model governance and monitoring control set

**Action:** Rewrite PSI and supervisory-audit sections.

**Resolves:** D07-I06.

**Content:** Define model inventory, intended use, risk tier, owner, independent validation, approval, deployment, monitoring, change, incident, override, rollback, and retirement. Use SR 11-7 only as comparative practice [9]. For PSI, define variable, population, bins, baseline, minimum sample, window, warning, escalation, investigation, and decision. Label 0.10 and 0.25 as conventions if retained.

Monitor data quality, freshness, missingness, calibration, discrimination, uncertainty coverage, stability, fairness, decision outcomes, intervention outcomes, overrides, complaints, and financial impact. Establish incident severity and regulator-notification assessment by legal and compliance, not an automatic PSI branch.

**Acceptance tests:** PSI alone cannot be described as model failure or legal notification. Every monitored metric has owner, threshold status, response, and evidence.

### D07-P07: Build an intervention, modification, and forbearance decision tree

**Action:** Rewrite assistive ecosystem and forbearance sections.

**Resolves:** D07-I05 and D07-I10.

**Content:** For each premium holiday, micro-reward bridge, payment reschedule, limit reduction, draw freeze, reserve release, and routing intervention, define initiator, decision owner, customer difficulty, contractual change, concession, NPV effect, EIR effect, stage or default effect, funding, duration, notice, consent, appeal, outcome, and ledger entry.

Do not use a universal one-percent rule. Do not generalise a 10% liability test to assets. Use IFRS 9 and entity policy [5], plus Kenyan regulatory advice. Define anti-shadow-forbearance controls: intervention reason, independent accounting classification, no target to avoid Stage 3, outcome monitoring, repeat interventions, and audit sampling.

**Acceptance tests:** The same facts produce the same classification under a tested decision table. An intervention can increase stage or be recognised as forbearance. Customer support is not conditioned on accounting optics.

### D07-P08: Replace fairness claims with a customer-rights control framework

**Action:** Rewrite equalized odds, ECOA, and LDA sections.

**Resolves:** D07-I09 and D07-I10.

**Content:** Start with Kenyan equality, consumer, credit, and data-protection legal review. Label ECOA and LDA as comparative. Define automated-decision transparency, notice, reason, review, correction, appeal, and complaint. Link DPIA and data rights to [10], [11].

Define fairness metrics across access, approval, price, limit, false outcomes, calibration, interventions, insurance continuity, complaints, and net customer effect. Include uncertainty, sample sufficiency, intersectionality, and proxy review. State trade-offs among equalized odds and calibration. Treat MMD and orthogonalisation as testable mitigations only.

**Acceptance tests:** No technical method guarantees legal compliance. A failed metric has investigation, alternative analysis, remediation, and launch or suspension criteria. Customer remedies are operational.

### D07-P09: Replace speculative ISO and XBRL claims with a reporting inventory

**Action:** Rewrite “Continuous Control Monitoring via ISO 20022 and XBRL.”

**Resolves:** D07-I08.

**Content:** Inventory actual CBK, IRA, credit-bureau, AML, tax, company, financial-statement, lender, trustee, and investor reports. For each state reporting entity, recipient, legal source, frequency, due date, schema, channel, preparer, approver, signer, retention, reconciliation, acknowledgement, and correction.

Use ISO 20022 only for a verified message and implementation guide [13]. Use XBRL only where a required taxonomy applies. Treat model explanations and EIR evidence as internal regulatory evidence packages unless a regulator requests a defined payload. Remove invented message tags and unverified real-time CBK API claims.

**Acceptance tests:** Every external endpoint has authoritative documentation or is marked proposed. Internal evidence is transport-neutral. Reporting failures have escalation and correction.

### D07-P10: Create a regulatory control library and assurance plan

**Action:** Add final control section and rebuild references.

**Resolves:** D07-I11 and closes all findings.

**Content:** Create stable control IDs with obligation, risk, entity, owner, preventive or detective type, frequency, evidence, system, exception, escalation, and assurance. Link controls to D08 records and D10 implementation gates. Include first-line operation, second-line compliance and risk, independent validation, internal audit, external audit, and legal review.

Add an open-questions register for licence, true sale, data processing, customer deductions, insurance distribution, intervention classification, capital treatment, regulator reporting, and tax. Cite primary sources and date all conclusions.

**Acceptance tests:** Every material obligation maps to at least one control and evidence item. Every control maps to an owner and test. No orphan rule or unverified citation remains.

## Evidence architecture and regulator engagement

Define a decision evidence package containing customer and product ID, decision time, source-data snapshot, feature version, model version, posterior output, uncertainty, policy-rule version, actual rule hits, reason codes, intervention, approval or override, customer communication, ledger reference, and retention class. The package should be immutable after closure, with corrections appended rather than overwritten. Privacy access should be limited to purpose.

Regulator engagement should begin with a concise architecture and control description, not a proprietary XML proposal. Maintain a question log, meeting record, commitments, owners, due dates, and changes to assumptions. Do not describe a meeting, sandbox application, or notification as approval. Counsel should record when formal non-objection or permission is required.

## Recommended editing order and reviewers

Perform P01 through P03 first with Kenyan counsel. Complete accounting and capital sections with relevant entity finance and lender risk. Complete model governance before fairness and intervention controls. Build reporting inventory only after actual obligations are confirmed. Finish the control library and assurance plan last.

Required reviewers include Kenyan banking and insurance counsel, DPO, bank compliance and prudential capital, carrier compliance and actuarial, IFRS adviser or auditor, model-risk and validation, product and servicing, platform counsel, consumer-protection specialist, information security, internal audit, trustee reporting, and financial modeller.

## Pre-publication validation checklist

- Authority and jurisdiction are labelled for every rule.
- Entity and licence perimeter is consistent.
- IFRS 9 and IFRS 17 workstreams are separate.
- IRB use and capital relief are not assumed.
- PSI and fairness thresholds have correct status.
- Intervention and forbearance decision tables pass cases.
- Data-protection and customer remedies are included.
- External schemas are verified.
- Control and evidence mappings are complete.
- Formulas, citations, dates, and punctuation pass review.

## Legal-opinion and policy decision register

Create a structured register for issues that cannot be resolved by editorial interpretation. Required Kenyan advice should cover lending and digital-credit licensing, insurance distribution and policy administration, premium financing, receivable assignment and set-off, platform wallet deductions, reserve-pocket ownership, data controller and processor roles, automated decisions, cross-border data, consumer disclosure, unfair terms, adverse action, interventions, modifications, forbearance, reporting, tax, insolvency, and dispute resolution. Each question should identify affected entity, proposed facts, documents reviewed, counsel conclusion, conditions, reliance, effective date, and review trigger.

Separate legal opinions from internal policy decisions. For example, law may permit a draw freeze under contract, while policy chooses a stricter sufficiency threshold. A covenant may require a 6.5% NPL trigger, while regulation does not. Model governance may select PSI 0.25 as an escalation, while counsel determines whether an incident is notifiable. Record each choice with authority and owner so later drafts do not turn it into a statutory requirement.

Create a policy hierarchy and conflict rule. Law and regulator directions prevail, followed by contract, board-approved policy, delegated procedures, and model configuration. When a partner policy conflicts with the SPV covenant or customer contract, legal and compliance should determine treatment before code changes. Emergency overrides need authority, duration, customer impact, evidence, review, and retrospective approval.

## Control testing and assurance calendar

For each control in D07-P10, define design test, operating-effectiveness test, sample, population, evidence, tester, frequency, and deficiency rating. High-risk controls should include pricing decomposition and disclosure, eligibility, model approval, data rights, automated-decision reasons, intervention classification, ECL close, carrier interface, covenant calculation, report submission, access, incident escalation, and complaint resolution.

First-line owners should self-certify with evidence. Second-line risk, compliance, and privacy should conduct thematic testing and challenge. Independent model validation covers model components. Internal audit should test governance and a risk-based sample of controls. External audit covers relevant financial reporting. Counsel updates legal conclusions after material law, product, partner, or contract changes. Trustee and lenders exercise contractual audit rights without replacing management control.

Maintain a deficiencies log with root cause, affected decisions and periods, customer or financial impact, compensating control, remediation owner, due date, retest, disclosure, and regulator-notification assessment. A control can be designed but not operational, or operational but ineffective. The document should use these maturity states instead of claiming “automated compliance.”

## Regulatory and customer incident decision tree

Add incident categories for data breach, inaccurate customer price, unauthorised decision, discriminatory outcome, model failure, reporting error, ECL misstatement, covenant error, missing collections, platform outage, carrier lapse, servicing breakdown, key compromise, and misleading disclosure. Define detection, containment, customer protection, evidence preservation, materiality, escalation, legal assessment, notification, correction, compensation, root cause, and closure.

Notification is determined by the applicable rule and facts, not by PSI or an engineering severity alone. The system should preserve the score, data, rule, notice, journal, and communication related to affected decisions. Where customers may be harmed, suspend the relevant automation, use a safe fallback, stop new exposure if needed, and prioritise correction and remedy. This section makes the regulatory architecture operational during failures, when its credibility matters most.

## Definition of done

D07 is complete when counsel, compliance, accounting, prudential risk, model validation, and operations can identify the rule that applies, the entity it governs, the control that implements it, and the evidence that proves operation. Comparative frameworks must remain visibly comparative, and no model metric or technology payload may be represented as legal compliance by itself.

## Publication and periodic review rule

Assign an annual full review and event-driven review after a material Kenyan legal or regulatory change, new licence, new jurisdiction, new product, new insurer or lender, altered data purpose, new model use, significant incident, or covenant amendment. Each review should compare the text to current primary sources, contracts, accounting policies, and actual controls. Archive superseded conclusions and effective dates rather than overwriting them.

Publish a short regulatory change notice with affected entities, obligations, controls, systems, customer communications, model or policy changes, implementation deadline, owner, and evidence. Emergency changes should include temporary safeguards and retrospective approval. This ongoing review is necessary because a document that is correct on 24 August 2026 can become misleading after a benchmark, reporting, licence, privacy, accounting, or prudential change.

The compliance owner should certify the reviewed source list, unresolved advice, accepted limitations, and next review date. Any expired conclusion must be marked unusable until refreshed, with dependent automation placed under a documented safe fallback.
