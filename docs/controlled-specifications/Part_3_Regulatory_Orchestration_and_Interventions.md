---
title: "Implementation Documentation: Regulatory Orchestration, Customer Protection, and Assistive Interventions"
author: "Nevil Maloba"
date: "24 August 2026"
status: "Controlled design specification for legal, compliance, accounting, risk, and operations review"
---

# Purpose and Control Philosophy

Mwendo Pamoja combines credit, insurance-premium finance, wallet collections, telematics, and behavioural interventions. Its regulatory design must therefore begin with legal-entity and activity analysis, not with a single technology label. This chapter defines the control perimeter for the proposed Kenyan pilot and the evidence needed before any automated action is used in production.

The platform is intended to help a licensed lender, insurer, platform, servicer, and bankruptcy-remote special-purpose vehicle coordinate decisions. It does not transfer the legal obligations of those parties to the model or to the technology provider. Each decision remains attributable to an authorised entity, an approved policy, a versioned model or rule, and a named human owner.

The design follows five principles:

1. A predictive signal is not a legal rule.
2. A contractual covenant is not automatically a regulatory requirement.
3. A supportive intervention can still be a concession, modification, or forbearance measure.
4. Model monitoring is evidence for governance, not a substitute for legal analysis.
5. Every material customer or investor outcome must be reconstructable from point-in-time data.

# Authority and Evidence Labels

Every requirement in the implementation control library must carry one of the following labels.

| Label | Meaning | Approval needed |
|---|---|---|
| Kenyan law or regulation | Binding requirement within its stated scope and effective date | Legal and compliance confirmation |
| Regulator guidance | Supervisory expectation or interpretive guidance | Compliance interpretation |
| Accounting standard | Reporting requirement for the entity applying the standard | Accounting-policy approval and auditor review |
| Contractual control | Obligation created by financing, servicing, insurance, or platform documents | Legal execution and covenant owner |
| Internal policy | Risk appetite, customer-treatment, model, or operating requirement | Designated policy owner |
| Statistical convention | Monitoring threshold or analytical heuristic | Model Risk Committee |
| Comparative reference | Foreign or international framework used as design guidance only | Explicit non-binding label |

References to Basel, European Banking Authority guidance, Solvency II, the United States Equal Credit Opportunity Act, or overseas fair-lending practice are comparative unless Kenyan counsel and the relevant regulated institution determine otherwise. They must not be presented as Kenyan law.

# Jurisdiction and Applicability Matrix

The following matrix is the starting position, subject to transaction-specific legal opinions and the final licensing model.

| Topic | Primary affected party | Proposed treatment | Required confirmation |
|---|---|---|---|
| Banking and lending | Licensed bank or other authorised lender | Lender owns credit approval, pricing, disclosures, collections policy, and prudential compliance | Licence scope, outsourcing permissions, consumer-credit obligations |
| Digital credit | Digital credit provider, if the activity falls within the statutory perimeter | Apply Digital Credit Providers Regulations and CBK directions where applicable | Whether the operator, originator, or servicer requires a licence |
| Insurance | Licensed insurer and intermediaries | Insurer owns underwriting authority, policy issuance, premium treatment, cancellation, and claims | Product approval, premium-finance structure, intermediary permissions |
| Data protection | Each controller and processor | Define lawful basis, notices, minimisation, retention, security, data-subject rights, and processor terms | Controller and joint-controller allocation |
| Credit reporting | Credit provider and credit-reference participants | Use accurate, timely, challengeable reporting with required notices | Permitted data, timing, dispute workflow |
| Payments and wallet deductions | Payment service providers and contracting parties | Use explicit mandates, reconciliation, revocation rules, and failure handling | Payment authorisation and e-money perimeter |
| SPV funding | Issuer, trustee, security trustee, investors, originator, and servicer | Govern by transaction documents, securities law, tax law, and true-sale analysis | Offering restrictions, perfection, bankruptcy remoteness, tax |
| AML and sanctions | Each obligated institution | Apply risk-based customer due diligence, screening, monitoring, and escalation | Reliance, outsourcing, record-sharing, reporting responsibilities |
| Accounting | Holder or issuer of each contract | Apply IFRS 9, IFRS 15, IFRS 17, and other standards according to contract and entity | Formal accounting papers and auditor review |

The matrix must be updated if a new product, country, data source, distribution channel, or legal entity is added.

# Entity, Licence, and Accountability Perimeter

## HoldCo and technology operator

HoldCo owns intellectual property and may provide analytics, integration, and programme-management services. It does not become a bank, insurer, trustee, or payment service provider merely because it supplies software. It must not make a regulated decision in its own name unless authorised to do so. Contracts must allocate:

- intellectual-property ownership and licences;
- controller and processor roles;
- security, incident, retention, and audit duties;
- service levels and business-continuity obligations;
- model-change approval rights;
- liability for data and decision errors; and
- termination assistance and data portability.

## Licensed lender

The lender owns the credit policy, customer pricing, affordability and suitability controls, approval authority, adverse-decision process, IFRS 9 policy for assets it recognises, and any prudential capital treatment that applies to it. Use of the HLR does not transfer those duties to HoldCo.

## Insurer and insurance intermediaries

The insurer owns the insurance contract, underwriting authority, claims promise, policy administration, and IFRS 17 accounting for insurance contracts it issues. The premium-finance receivable is a separate financial arrangement. Its legal holder applies the relevant financial-instrument accounting. Cancellation value, unearned premium, refund timing, and assignment rights must be confirmed in the insurance and finance contracts.

## SPV, trustee, and servicer

The SPV owns only the receivables and related rights validly transferred to it. Bankruptcy remoteness depends on incorporation, governance, separateness covenants, true sale, security perfection, non-petition provisions, commingling controls, and enforceability. An ERP ledger, warehouse tag, or bank-account label does not create legal isolation.

The servicer executes customer and receivable operations under a servicing agreement. The trustee and calculation agent verify accounts, borrowing-base reports, waterfall calculations, and covenant notices as specified in the finance documents.

## Platform and payment providers

The mobility platform supplies only data and payment-routing rights covered by executed agreements. Fare-linked deductions are contractual arrangements, not assumed legal priorities. Failed deductions, refunds, reversals, platform outages, mandate withdrawal, and commingling must have defined treatment.

# Accounting Workstreams

## IFRS 9 for financial assets

The entity recognising a loan or receivable applies its approved IFRS 9 classification, measurement, modification, derecognition, and impairment policy. The HLR can provide a validated real-world probability-of-default input, but expected credit loss also requires exposure at default, loss given default, discounting, scenario weights, staging logic, and forward-looking information.

Stage allocation is not determined by a single PSI value, an intervention label, or a product state. Significant increase in credit risk must be assessed under the reporting entity's policy using reasonable and supportable information. Default, cure, probation, write-off, and recovery definitions must be consistent across finance, risk, and servicing.

If contractual cash flows change, accounting must determine:

1. whether the change was contemplated by the original contract;
2. whether it is a modification, a derecognition event, a new instrument, or an administrative correction;
3. whether financial difficulty motivated a concession;
4. whether gross carrying amount and modification gain or loss must be recalculated; and
5. whether credit risk and staging change.

No universal one-percent net-present-value rule is adopted. The ten-percent test commonly discussed for financial liabilities must not be copied into the asset analysis as a general bright line.

## IFRS 17 for insurance contracts

The insurer applies IFRS 17 to insurance contracts within its scope. HoldCo, the lender, and the SPV do not apply IFRS 17 merely because a receivable finances an insurance premium. Interfaces must distinguish:

- insurance premium and coverage data;
- premium-finance principal and interest;
- insurer commission or service revenue;
- policy cancellation and refund receivables;
- claims data and consent restrictions; and
- cash collected as agent versus cash owned by the collector.

The programme may provide validated usage data to the insurer, but measurement, grouping, fulfilment cash flows, contractual service margin, premium allocation approach eligibility, and onerous-contract testing remain the insurer's responsibilities.

# Prudential Capital and Lender Risk

Basel standards govern banks through national implementation. The platform's HLR is not an approved internal-ratings-based capital model by default. Any lender wishing to use model outputs in regulatory capital must make a separate assessment with its supervisor and satisfy all applicable data, validation, governance, and approval requirements.

For the pilot:

- lender regulatory capital is a lender-owned calculation;
- SPV first-loss equity and overcollateralisation are transaction credit enhancement, not substitutes for bank capital;
- the Bayesian posterior PD used for underwriting does not automatically qualify as an IRB parameter;
- Basel output-floor calculations apply only within the bank's prudential framework; and
- the term sheet must not promise regulatory capital relief.

The lender should run its normal standardised or approved prudential treatment independently from the SPV cash-flow model.

# Model Governance and Monitoring

## Model inventory and ownership

The model inventory must record:

- model purpose and prohibited uses;
- owner, developer, validator, and approving committee;
- population, products, horizons, and outcomes;
- data lineage and feature versions;
- HLR specification, calibration layer, and copula module;
- known limitations and fallback;
- implementation version and release hash;
- validation date and next review; and
- linked policy and customer communications.

The HLR architecture is defined in Part 2b. Explicit Liquidity Features have one engineered owner. Neural embeddings are cross-fitted and residualised against the explicit design before entering the HLR. Orthogonalised splines, grouped shrinkage, centred hierarchical effects, and strong interaction heredity reduce redundant attribution and multicollinearity. The model must fall back to the explicit-only specification when the residual neural block lacks stable incremental value.

## Monitoring thresholds

Monitoring covers discrimination, calibration, uncertainty, drift, stability, fairness, data quality, and decision outcomes. Thresholds are approved internal or contractual controls. They are not described as statutory unless a cited Kenyan authority imposes them.

Population Stability Index may be used as one screening metric:

- PSI below 0.10: ordinarily stable, subject to other evidence;
- PSI from 0.10 to below 0.25: investigate and increase review;
- PSI at or above 0.25: material-drift trigger under internal policy.

These bands are conventions, not proof of model failure. A trigger can freeze a release or require recalibration, but escalation depends on materiality, performance, customer impact, and the approved policy.

## Change classification

| Change | Example | Minimum control |
|---|---|---|
| Data repair | Corrected timestamp parser | Regression test, lineage update, owner approval |
| Parameter refresh | Calibration intercept update | Out-of-time evidence, validator review |
| Minor model change | Approved knot or threshold change | Impact analysis, controlled release |
| Material model change | New outcome, feature block, architecture, or product | Independent validation and committee approval |
| Emergency policy change | Temporary draw freeze after incident | Time limit, senior approval, retrospective review |

# Credit Policy and Compliance Gate

The HLR produces calibrated posterior risk and uncertainty. The separate Credit Policy and Compliance Gate applies legal, contractual, risk-appetite, and operational rules.

Inputs include:

- posterior PD and credible interval;
- product, amount, maturity, and aggregate exposure;
- Explicit Liquidity Features;
- identity, consent, insurance, and eligibility status;
- affordability and sufficiency results;
- portfolio concentration and covenant status;
- data-quality and model-health flags; and
- intervention history.

Outputs are controlled actions:

- approve;
- decline with an intelligible reason;
- reduce a proposed limit;
- freeze a new draw;
- require manual review;
- offer a permitted restructuring;
- activate a premium holiday or support intervention;
- stop SPV purchases;
- trigger an account or portfolio cash sweep; or
- suspend equity distributions.

Every action record includes input snapshot, model and policy versions, reason codes, decision owner, timestamp, notice status, and override record.

# Intervention, Modification, and Forbearance Framework

Assistive interventions are valuable only when customer welfare, accounting, collections, and conduct consequences are controlled.

## Decision sequence

1. **Detect:** Identify a verified risk state with adequate data quality.
2. **Protect:** Apply any immediate safety or fraud control.
3. **Assess:** Determine customer need, affordability, product eligibility, and legal constraints.
4. **Classify:** Decide whether the action is operational assistance, a contractual option, a modification, a concession due to financial difficulty, or collections activity.
5. **Authorise:** Route to the accountable lender, insurer, platform, or servicer.
6. **Communicate:** Obtain any required consent and provide clear effects on cost, term, coverage, and reporting.
7. **Account:** Record the correct cash-flow, modification, staging, and revenue consequences.
8. **Monitor:** Measure customer and portfolio outcomes against a suitable comparison group.
9. **Exit:** End, renew, or escalate the intervention under documented criteria.

## Classification table

| Proposed action | Primary questions | Possible consequences |
|---|---|---|
| Route or rest recommendation | Is it safety guidance, an employment direction, or a credit condition? | Customer notice, platform coordination, non-discrimination review |
| Premium holiday | Does cover continue, who funds the premium, and does the contract permit deferral? | Modification, insurer receivable, lapse risk, disclosure |
| Micro-reward bridge | Is it a grant, fee rebate, additional loan, or capitalised balance? | Tax, credit, accounting, affordability, abuse controls |
| Limit reduction or draw freeze | Is the action prospective and contractually permitted? | Adverse-decision reasons, customer notice, manual review |
| Repayment reschedule | Is the customer in financial difficulty and is a concession granted? | Forbearance classification, modification accounting, staging review |
| Reserve transfer | Whose cash is moved, under what mandate, and can it be recalled? | Safeguarding, consent, ledger, and reconciliation controls |

The product team must not describe an action as "non-punitive" solely because its intention is supportive. The actual cost, customer choice, coverage, credit-reporting effect, and risk of exclusion determine its treatment.

# Customer Rights, Fairness, and Data Protection

## Lawful and proportionate data use

Telematics and wallet data can reveal location, income patterns, health proxies, religion or routine, social relationships, and other sensitive inferences. The data-protection assessment must specify:

- controller and processor for each purpose;
- lawful basis for collection and processing;
- necessity and proportionality;
- data categories excluded from credit use;
- retention and deletion rules;
- cross-border transfers;
- rights-request and correction workflows;
- security controls;
- automated-decision safeguards; and
- whether a data-protection impact assessment is required.

Consent must not be treated as universally valid where it is bundled, non-specific, or cannot be withdrawn without disproportionate harm. A lawful basis for one purpose does not automatically authorise reuse for another.

## Automated decisions and meaningful review

Where a decision is based solely on automated processing and produces legal or similarly significant effects, the responsible entity must assess the safeguards required under Kenyan data-protection law. The production design should provide:

- clear notice that automated processing is used;
- accessible principal reasons;
- a way to correct inaccurate source data;
- a channel to request human review where required or promised;
- authority for the reviewer to change the outcome;
- time-bound complaint handling; and
- records of review quality and overturn rates.

## Fairness framework

Equalised odds, demographic parity, calibration by group, and error-rate ratios describe different properties and can conflict. The programme will not promise a mathematically perfect fairness state. It will:

1. define protected and vulnerable groups that may lawfully and ethically be tested;
2. establish minimum sample-size and uncertainty rules;
3. test data coverage, missingness, calibration, approval, pricing, error rates, limit changes, and interventions;
4. investigate causal mechanisms and less discriminatory alternatives;
5. document legitimate business necessity and proportionality;
6. use expert and customer review; and
7. monitor realised harm, complaints, and reversals.

Sensitive attributes used for fairness testing must be access-controlled and segregated from ordinary decisioning unless legally justified.

# Reporting and Supervisory Interfaces

The programme will not invent regulator-specific ISO 20022 elements or assume a live CBK supervisory API. A verified reporting inventory must be completed before any adapter is built.

| Reporting object | Owner | Source of record | Format and channel | Frequency | Evidence status |
|---|---|---|---|---|
| Statutory financial statements | Reporting entity | Approved general ledger and consolidation | Applicable reporting standard | Statutory | Confirmed by finance |
| Prudential return | Regulated lender or insurer | Regulatory reporting mart | Regulator-prescribed schema | As prescribed | Confirm with institution |
| Credit-reference reporting | Credit provider | Servicing ledger | Approved bureau interface | Contractual or prescribed | Confirm with bureau |
| SPV investor report | Servicer or calculation agent | Servicing, bank, reserve, and GL reconciliations | Finance-document template | Monthly | Define in transaction documents |
| Model-risk report | Model owner | Registry and monitoring store | Governance template | Monthly or quarterly | Internal policy |
| Data-protection incident notice | Controller or processor | Incident register | Legally prescribed channel | Event-driven | Legal determination |

ISO 20022 may be used for payment messages where the actual payment provider and scheme support it. XBRL may be used where a regulator or filing platform prescribes a valid taxonomy. Neither standard creates regulatory compliance on its own.

# Portfolio Controls and Covenants

Portfolio covenants are contractual controls with defined calculation agents, observation dates, cures, and consequences.

| Control | Base specification | Classification |
|---|---|---|
| NPL early-amortisation trigger | 6.5 percent, subject to final definition and documents | Contractual |
| Platform concentration limit | 25 percent of defined eligible balance | Contractual |
| Urban-geography limit | 15 percent under agreed geography taxonomy | Contractual |
| Minimum debt-note OC | 125 percent | Contractual |
| Cash reserve account | Three months of defined Class A and B debt service | Contractual |
| PSI material-drift band | 0.25 under approved monitoring policy | Statistical and contractual if incorporated |

For each covenant, the legal documents must define numerator, denominator, exclusions, ageing, cure, waiver, dispute process, and waterfall effect. "NPL," "eligible receivable," "debt service," and "concentration" must not rely on dashboard labels alone.

# Control Library and Evidence

Each control record must include:

- control ID and objective;
- authority and applicability;
- owner and performer;
- preventive or detective classification;
- frequency and trigger;
- input systems and evidence;
- exception path and service level;
- customer or investor impact;
- testing method;
- last test and result; and
- linked policy, model, contract, or law.

High-priority controls include:

- licence and product-perimeter approval;
- customer identity and sanctions screening;
- data-use and automated-decision assessment;
- affordability and sufficiency;
- feature and model version validation;
- manual-review and override governance;
- insurance coverage and cancellation reconciliation;
- receivable eligibility and true-sale evidence;
- daily collection, bank, reserve, subledger, and GL reconciliation;
- covenant calculation and notice;
- complaint and dispute resolution;
- incident containment and regulatory assessment; and
- model fallback and originations freeze.

# Assurance and Incident Response

The first line operates controls. Compliance, risk, privacy, security, and model-risk functions challenge them. Internal audit or an independent assurance provider tests design and operating effectiveness according to risk.

Before pilot launch, scenario exercises must cover:

- erroneous mass decline or limit reduction;
- model drift or corrupted feature input;
- wallet-deduction failure and duplicate collection;
- insurance lapse despite apparent payment;
- data breach involving location or wallet history;
- inability to reconstruct a decision;
- servicer outage;
- covenant breach and delayed notice; and
- prohibited use of a protected or proxy attribute.

The incident decision tree is: contain, preserve evidence, assess customer and financial impact, invoke fallback, identify accountable entities, determine notification duties, remediate customers, validate the repair, and obtain approval before resumption.

# Implementation Acceptance Criteria

The regulatory design is ready for a bounded live pilot only when:

- Kenyan counsel has approved the activity and licence perimeter;
- controller, processor, and data-sharing roles are executed;
- accounting papers separate IFRS 9 and IFRS 17 responsibilities;
- the lender has approved credit, affordability, pricing, collections, and forbearance policies;
- automated-decision notices, reason codes, correction, complaint, and review processes are tested;
- the HLR and fallback have independent validation;
- fairness testing includes uncertainty and outcome monitoring;
- all regulatory interfaces use confirmed schemas and channels;
- no comparative framework is presented as Kenyan law;
- no PSI band is presented as a statutory trigger;
- intervention accounting and customer communications have passed scenario tests;
- SPV covenants have legally defined calculations and owners; and
- evidence is sufficient to reproduce a decision and a waterfall calculation without relying on mutable dashboards.

# References

1. Central Bank of Kenya, "The Banking Act and Prudential Guidelines." Available: https://www.centralbank.go.ke/
2. Central Bank of Kenya, "Digital Credit Providers Regulations, 2022." Available: https://www.centralbank.go.ke/
3. Central Bank of Kenya, "Revised Risk-Based Credit Pricing Model," 2025. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf
4. Kenya Law, "Data Protection Act, 2019," current consolidated text. Available: https://new.kenyalaw.org/akn/ke/act/2019/24
5. Office of the Data Protection Commissioner, "Guidance Notes." Available: https://www.odpc.go.ke/
6. IFRS Foundation, "IFRS 9 Financial Instruments." Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
7. IFRS Foundation, "IFRS 17 Insurance Contracts." Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/
8. Basel Committee on Banking Supervision, "The Basel Framework." Available: https://www.bis.org/baselframework/
