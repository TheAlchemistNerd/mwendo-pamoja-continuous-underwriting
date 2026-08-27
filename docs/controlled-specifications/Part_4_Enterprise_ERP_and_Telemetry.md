---
title: "Implementation Documentation: Enterprise Accounting, Servicing, Telemetry, and Evidence Architecture"
author: "Nevil Maloba"
date: "24 August 2026"
status: "Target-state capability and control specification"
---

# Executive Design

Mwendo Pamoja requires a controlled bridge from high-frequency operational events to contractual balances, accounting entries, investor reports, and reproducible regulatory evidence. No single product is the system of record for every layer. The architecture therefore assigns each fact to an authoritative capability and reconciles facts as they cross boundaries.

Microsoft Dynamics 365 Finance is the proposed enterprise resource planning and general-ledger endpoint. It is not assumed to be the native loan-servicing engine, insurance-policy administration system, feature store, model registry, asset-liability management engine, or immutable evidence vault. Any product selection remains subject to a documented capability fit-gap, licensing, performance, control, and total-cost assessment.

The design has four goals:

1. preserve point-in-time telemetry and financial-event lineage;
2. maintain contract-level balances in a fit-for-purpose servicing subledger;
3. post controlled, reconcilable summaries and exceptions to the legal entity's general ledger; and
4. reproduce each material customer, accounting, and investor outcome from approved versions and evidence.

# Capability Architecture

~~~mermaid
flowchart LR
    A[Platform, wallet, telematics, lender, and carrier events] --> B[Immutable landing and schema validation]
    B --> C[Streaming and lakehouse processing]
    C --> D[Online feature service]
    C --> E[Historical analytical tables]
    D --> F[Model service]
    F --> G[Credit Policy and Compliance Gate]
    G --> H[Servicing and receivables subledger]
    H --> I[Controlled journal staging]
    I --> J[Dynamics 365 Finance general ledger]
    H --> K[Waterfall and investor calculation]
    J --> L[Financial and regulatory reporting mart]
    K --> L
    B --> M[Evidence vault]
    C --> M
    F --> M
    G --> M
    H --> M
    I --> M
~~~

The architecture keeps the operational decision path separate from the accounting close path. Streaming can provide rapid decisions, but booked balances, journals, and investor distributions pass through completeness, validity, and reconciliation gates.

# Capability Fit-Gap

The programme must issue a scored requirements matrix before confirming products. Each requirement should record volume, latency, availability, recovery, retention, jurisdiction, integration, evidence, licensing, and control needs.

| Capability | Required function | Candidate system class | Selection position |
|---|---|---|---|
| Event ingestion | Receive platform, wallet, telematics, servicing, and carrier events | Kafka-compatible event backbone and secure APIs | Required |
| Immutable landing | Preserve raw payload, source time, receipt time, schema, and hash | Versioned object storage with retention controls | Required |
| Stream processing | Validate, enrich, window, and route events | Apache Flink or equivalent | Required |
| Historical lakehouse | Point-in-time training, analytics, audit, and replay | Open table format such as Apache Iceberg | Required |
| Online feature service | Low-latency Explicit Liquidity Features and model inputs | Kappa-style state plus Redis-compatible serving | Required |
| Model registry and service | Approve, deploy, monitor, and reproduce models | Specialist model platform | Required |
| Policy decision service | Apply versioned Credit Policy and Compliance Gate | Rules or decision-management engine | Required |
| Credit servicing | Contracts, schedules, balances, delinquency, modifications, collections | Fit-for-purpose loan and receivables subledger | Required |
| Insurance administration | Policies, coverage, premium, cancellation, refund, claims | Insurer's authoritative system | External authority |
| Cash and reserve accounting | Bank, trust, reserve, and waterfall transactions | Treasury, subledger, and controlled calculation engine | Required |
| General ledger | Legal-entity books, journals, close, consolidation, procurement | Dynamics 365 Finance or selected ERP | Proposed |
| Evidence vault | Immutable decision and control evidence with legal holds | WORM-capable controlled repository | Required |
| Reporting mart | Financial, portfolio, model, and confirmed regulatory outputs | Governed analytical and reporting layer | Required |

A fit-gap result can identify D365 extensions or partner solutions, but custom code must not be treated as free. It introduces maintenance, security, testing, and upgrade obligations.

# Authoritative System-of-Record Matrix

| Information object | Authoritative source | Consumers | Control |
|---|---|---|---|
| Driver identity and consent | Approved identity and consent service | Lender, insurer, model, servicing | Identity match, purpose, version, expiry |
| Platform trips and earnings | Platform-signed feed or reconciled API | Lakehouse, features, servicing | Sequence, duplication, receipt, settlement reconciliation |
| Wallet transactions | Payment provider or regulated wallet ledger | Features, servicing, cash reconciliation | End-to-end transaction ID and bank settlement |
| Insurance policy and coverage | Insurer policy administration | Eligibility, servicing, customer support | Policy, coverage, cancellation, refund reconciliation |
| Credit contract and repayment schedule | Servicing subledger | Policy, collections, accounting, investor reports | Contract version, schedule balance, modification history |
| Receivable ownership and eligibility | SPV collateral register | Borrowing base, waterfall, trustee | Purchase evidence, legal owner, eligibility status |
| Feature value at decision time | Feature registry and point-in-time store | Model, explanation, audit | Definition, version, event cutoff, availability time |
| Model version and score | Model registry and scoring log | Policy service, monitoring, audit | Release hash, signature, input manifest, output |
| Policy action | Policy decision service | Servicing, customer channel, audit | Rule version, reasons, override, notice |
| Accounting journal | Legal entity's general ledger after posting | Financial statements, reporting mart | Batch totals, approvals, reconciliation |
| SPV bank and reserve cash | Bank or trustee statement reconciled to subledger | Waterfall, GL, investor report | Daily or period-end three-way reconciliation |
| Investor allocation | Approved waterfall engine and calculation-agent report | Trustee, GL, investors | Locked inputs, priority tests, approval |

A reporting warehouse can copy an authoritative fact, but it does not become the legal source merely because it is easier to query.

# Operational Event and Accounting Boundary

## Event identifiers and time

Every accepted event has:

- globally unique event ID;
- source-system ID and source event ID;
- driver, contract, product, and legal-entity keys where permitted;
- event time, source-posting time, receipt time, processing time, and correction time;
- schema and contract version;
- currency, amount, sign, and units;
- data classification and lawful-purpose tag;
- payload hash and source authentication result; and
- correction or reversal link.

Part 2a defines point-in-time correctness for features. The same discipline applies to accounting. A late or corrected event is posted through an approved adjustment process; history is not silently rewritten.

## From business event to journal

The serving subledger produces accounting events only after contract and amount validation. Each accounting event maps through a versioned rule to balanced debit and credit lines.

For batch \(b\):

$$
\sum_{j \in b} \mathrm{Debit}_j-\sum_{j \in b}\mathrm{Credit}_j=0.
$$

Balanced lines are necessary but not sufficient. The journal interface also tests:

- expected event count;
- total amount by currency and event type;
- contract-level balance movement;
- duplicate and missing sequence;
- legal entity and accounting date;
- open period and chart-of-accounts mapping;
- tax and fee treatment where approved;
- maker-checker approval; and
- successful ERP posting reference.

The journal batch carries a deterministic idempotency key. A retry with the same key cannot create a second posting. A correction posts a reversal or adjustment linked to the original entry.

# Servicing and Receivables Subledger

The subledger maintains contract-level facts that are too granular or specialised for the general ledger:

- initial principal, disbursement, and fees;
- effective-interest-rate inputs and contractual rate reset;
- repayment schedule and allocation order;
- principal, interest, fee, tax, suspense, and unapplied cash;
- days past due, arrears, default, cure, write-off, and recovery;
- modification and forbearance history;
- insurance premium, policy reference, cancellation, and refund;
- revolving limit, draw, freeze, and repayment;
- lender or SPV ownership by effective date;
- eligibility, concentration, and exclusion reason;
- collection mandate and failure; and
- expected-credit-loss attributes supplied under approved policy.

The subledger must support audit-effective dating. An ownership transfer, modification, or correction produces a new effective record; it does not erase the state used for a prior decision or report.

# Chart of Accounts and Dimensions

The final chart of accounts is owned by finance. At minimum, postings must distinguish:

- legal entity;
- SPV or HoldCo;
- product;
- principal, accrued interest, fee, tax, impairment allowance, write-off, recovery, cash, reserve, and suspense;
- receivable owner;
- platform and geography for analytical reporting where appropriate;
- Class A, Class B, and Class C funding;
- transaction account, collection account, reserve account, and distribution account;
- scenario or budget version where used; and
- intercompany counterparty.

Analytical dimensions must not replace legal ownership. A receivable tagged “SPV” in D365 is not transferred until the legal sale, consideration, assignment, and collateral-register evidence are complete.

# SPV Purchase and Accounting Control

The receivable purchase workflow is:

1. servicing system proposes eligible assets at the cutoff;
2. eligibility engine applies the executed finance-document rules;
3. collateral register records current owner and transfer evidence;
4. originator and SPV approve the purchase file;
5. SPV pays purchase consideration through the controlled account;
6. subledger updates ownership from the effective time;
7. each entity posts its approved accounting treatment;
8. bank, subledger, collateral register, and GL reconcile; and
9. trustee or calculation agent receives the locked borrowing-base report.

Accounting cannot conclude true sale or derecognition from workflow status. Legal and accounting analyses must be documented separately.

# IFRS 9 Data and Posting Interface

The impairment engine may consume HLR real-world PD outputs only after validation and accounting-policy mapping. It also needs approved EAD, LGD, macroeconomic scenarios, discounting, staging, cure, and write-off data.

The interface returns at least:

- reporting date;
- entity and portfolio;
- contract or aggregation key;
- stage;
- gross carrying amount;
- twelve-month or lifetime ECL;
- allowance movement reason;
- scenario and model versions;
- management overlay where approved; and
- reconciliation to prior closing allowance.

D365 records approved journal effects. It does not independently decide Stage 1, Stage 2, Stage 3, modification, or write-off unless finance has explicitly selected and validated a connected capability for that purpose.

# Pricing, Model, and Policy Interfaces

The pricing service receives only approved model and finance inputs:

- compounded KESONIA observation and contract conventions;
- customer-pricing premium \(K_{\mathrm{RBCP}}\);
- fees and charges;
- product cash-flow schedule;
- affordability and sufficiency result; and
- decision timestamp and versions.

The model service provides calibrated posterior PD and uncertainty, not a final approval. The policy service applies the separate Credit Policy and Compliance Gate and returns a controlled action. The servicing system then validates that the action is contractually possible before booking it.

For every decision, the evidence package must contain:

- point-in-time input manifest;
- feature definitions and values;
- model release and calibration versions;
- score, interval, and explanation;
- policy and threshold versions;
- decision and reason codes;
- override and reviewer;
- customer notice; and
- resulting contract or ledger event.

# Medallion-to-Accounting Control Bridge

The terms bronze, silver, and gold describe data refinement, not accounting authority.

## Bronze: immutable receipt

Bronze preserves the source payload, signature, timestamps, schema, and ingestion result. It is append-only except for governed legal retention and deletion procedures.

## Silver: validated canonical events

Silver resolves schema, identity, units, duplicates, corrections, and contract references. Rejected events remain visible with reason and resolution status.

## Gold: purpose-specific outputs

Gold tables support features, servicing, finance, investor calculations, and monitoring. Each output has a declared owner, source lineage, effective date, and reconciliation. A gold table is not automatically a posted balance.

## Accounting bridge

The bridge selects approved business events, freezes a batch cutoff, computes control totals, maps journals, routes approval, posts to D365, captures the ERP batch ID, and reconciles the result. Rejected mappings go to an exception queue; they are not defaulted to a suspense account without limits and ageing controls.

# Reconciliation Framework

The reconciliation hierarchy is:

1. source event to immutable landing;
2. landing to canonical event;
3. canonical event to servicing transaction;
4. servicing schedule to contract balance;
5. servicing transaction to bank settlement;
6. subledger total to journal batch;
7. journal batch to posted general ledger;
8. eligible asset register to SPV carrying balance;
9. bank and reserve balances to waterfall inputs; and
10. waterfall outputs to trustee and investor statements.

Every break has an owner, severity, ageing, financial value, customer impact, and resolution. Material unresolved breaks block close, borrowing-base delivery, or distribution according to policy.

# Data Governance and Privacy

Data classification distinguishes public, internal, confidential, personal, sensitive personal, financial, model-confidential, and legally privileged material. Access is least privilege and purpose-specific.

The evidence design follows minimisation:

- retain raw data only for approved purposes and periods;
- avoid copying precise location into finance or investor systems;
- use stable pseudonymous keys outside operational identity services;
- separate fairness-testing attributes from production decision inputs;
- preserve the minimum evidence needed to explain an outcome;
- apply legal holds without indefinite routine retention;
- log privileged access; and
- make deletion and correction propagate through derived stores where legally required and technically feasible.

The data catalogue records owner, steward, lawful purpose, classification, retention, quality rules, lineage, consumers, and deletion behaviour.

# Security and Cryptographic Controls

Security is layered. No cipher or certificate makes the system “unbreakable.”

Controls include:

- encryption in transit using approved TLS profiles;
- encryption at rest using managed keys;
- authenticated encryption such as AES-GCM where supported;
- central key management, rotation, separation of duties, and revocation;
- workload and user identities with short-lived credentials;
- mutual authentication for high-risk service interfaces where appropriate;
- secrets vaulting and prohibited plaintext secrets;
- signed software artefacts and verified deployment provenance;
- network segmentation and egress controls;
- tamper-evident administrative and decision logs;
- vulnerability, dependency, and configuration management;
- security monitoring and incident response; and
- tested backup, recovery, and ransomware procedures.

WORM retention can protect selected evidence from ordinary modification, but access, export, key, administrator, and application risks still require controls. Digital signatures prove defined integrity and origin properties only when identity, keys, algorithms, validation, and revocation are governed.

# Reporting Adapters

Reports are generated from confirmed obligations, not from speculative schemas.

Each adapter specification includes:

- legal or contractual authority;
- reporting entity and signatory;
- data dictionary and taxonomy version;
- source-of-record mapping;
- validation rules;
- cutoff and resubmission rules;
- delivery channel and security;
- acknowledgement and rejection handling;
- retained submission evidence; and
- change-management owner.

ISO 20022 is used only for actual supported payment messages. XBRL is used only against an issued taxonomy. No custom element is labelled as an official CBK field without confirmation.

# Migration, Cutover, and Parallel Close

## Migration

Historical contracts and transactions are profiled, cleansed, mapped, and reconciled before load. Migration preserves original IDs and legacy balances. Unresolved exceptions are quantified and approved; they are not hidden in opening balances.

## Parallel operation

At least two representative period closes should run in parallel before financial cutover, with a longer period if volume, product, or accounting complexity warrants it. Comparison covers:

- trial balance and subledger reconciliation;
- interest accrual and fee recognition;
- ECL movement;
- bank and reserve balances;
- receivable ownership and borrowing base;
- waterfall allocation;
- tax outputs subject to confirmed treatment;
- investor report; and
- exception counts and ageing.

## Cutover gate

Production cutover requires signed data migration, security, performance, reconciliation, recovery, role, and close approvals. Rollback criteria and the period of heightened support are documented.

# Service Levels and Resilience

The programme defines separate objectives for:

- online feature and decision availability;
- maximum decision latency;
- event ingestion lag;
- servicing posting latency;
- accounting batch completion;
- bank and ledger reconciliation;
- monthly close;
- investor report delivery;
- recovery point objective;
- recovery time objective; and
- evidence retrieval.

Failure modes degrade safely. If neural scoring is unavailable but explicit features and policy remain valid, the approved explicit-only fallback may operate within conservative limits. If data quality, consent, identity, servicing, or accounting integrity fails, the relevant decision or posting stops and enters review.

# Implementation Acceptance Criteria

The enterprise architecture is accepted only when:

- the capability fit-gap is approved without assuming D365 can perform specialist functions;
- the authoritative system-of-record matrix has named owners;
- event, contract, feature, model, policy, journal, and report versions are linked;
- the servicing subledger and GL reconcile by entity, currency, product, and accounting period;
- duplicate submission cannot create duplicate financial posting;
- late and corrected events preserve prior reported state;
- SPV ownership is supported by legal evidence, not an ERP dimension;
- IFRS 9 and IFRS 17 data and ownership remain separate;
- model scores and policy actions can be reproduced from point-in-time evidence;
- privacy and retention controls minimise telemetry in finance and reporting systems;
- security claims are testable and qualified;
- each external reporting interface uses a verified schema and channel;
- parallel close meets agreed tolerances;
- disaster recovery and model fallback are exercised; and
- material reconciliation exceptions block the appropriate close, borrowing-base, or distribution process.

# References

1. Microsoft, “Dynamics 365 Finance documentation.” Available: https://learn.microsoft.com/dynamics365/finance/
2. Microsoft, “General ledger overview.” Available: https://learn.microsoft.com/dynamics365/finance/general-ledger/general-ledger
3. Microsoft, “Dynamics 365 implementation guidance.” Available: https://learn.microsoft.com/dynamics365/guidance/
4. Apache Flink, “Documentation.” Available: https://nightlies.apache.org/flink/flink-docs-stable/
5. Apache Iceberg, “Documentation.” Available: https://iceberg.apache.org/docs/latest/
6. IFRS Foundation, “IFRS 9 Financial Instruments.” Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
7. ISO, “ISO 20022 Universal financial industry message scheme.” Available: https://www.iso20022.org/
8. Kenya Law, “Data Protection Act, 2019,” current consolidated text. Available: https://new.kenyalaw.org/akn/ke/act/2019/24
