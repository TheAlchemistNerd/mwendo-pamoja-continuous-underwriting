# D08 Implementation Plan: Enterprise ERP and Telemetry

## Objective and system boundary

Rewrite D08 as the enterprise accounting, systems-of-record, integration, evidence, and security architecture. Its purpose is to show how operational events become validated product balances, model evidence, cash allocations, and approved accounting journals without confusing an ERP with a loan-servicing, insurance, model, ALM, FTP, or immutable-storage platform.

The revised design should be capability-led. Dynamics 365 Finance is the proposed ERP and general-ledger endpoint for approved postings. A servicing ledger owns contractual receivable balances. The carrier owns insurance-contract records. The event lakehouse owns governed event history. The feature store owns online feature values. The model registry owns approved model artifacts. The policy service owns rules. An evidence vault retains signed decision and reporting packages. A specialist ALM or FTP engine is added only if requirements justify it.

## Proposed document architecture

1. Purpose, scope, target state, and current-state assumptions.
2. Capability map and system-of-record matrix.
3. Product servicing, subledger, and accounting boundaries.
4. SPV legal form, cash, journals, and reconciliation.
5. Event-to-accounting integration and close controls.
6. Pricing, model, policy, and intervention interfaces.
7. Data governance, privacy, retention, and evidence.
8. Security architecture and operational resilience.
9. Regulatory and investor reporting adapters.
10. Fit-gap, implementation decisions, tests, and references.

## Section-level implementation actions

### D08-P01: Rebuild structure, status, and requirements language

**Action:** Replace the opening and renumber all headings.

**Resolves:** D08-I11.

**Content:** State target state versus implemented state, version, date, owner, and dependencies. Replace marketing conclusions with requirement IDs. Use `REQ`, `CTRL`, `IF`, and `TEST` identifiers for capability, control, interface, and acceptance test. Label vendor claims as product documentation, not implemented proof. Use the global IEEE index.

**Acceptance tests:** Headings are sequential. Every technology claim is target, decision, or verified implementation. No repeated Section 9 or broken numbering remains.

### D08-P02: Perform a capability-led D365 and specialist-system fit-gap

**Action:** Rewrite “Architectural Preservation,” “D365 Regulatory ERP Endpoint,” and pricing-engine claims.

**Resolves:** D08-I01 and D08-I02.

**Content:** List capabilities: customer and contract servicing, revolving limits, daily accrual, delinquency, collections, modification, receivable sale, borrowing base, ECL, insurance records, general ledger, consolidation, cash management, tax, fixed assets, procurement, model execution, policy rules, evidence retention, ALM, FTP, and reporting. For each state required grain and control, proposed system, native, configured, custom, ISV, integration, or out of scope.

Use Microsoft [16], [17] only for application lifecycle management. Use Oracle [14], [15] to illustrate specialist FTP and ALM depth, not to preselect Oracle. Remove the file-transfer connector [39] from funds-transfer-pricing evidence. Conduct demonstrations and proof of concept using representative cash and volume.

**Acceptance tests:** No capability is assigned based on acronym similarity. D365 native and custom functions are documented. Procurement can estimate licence, build, support, and exit cost.

### D08-P03: Publish the authoritative system-of-record matrix

**Action:** Replace the “regulatory endpoint” and “sovereign source” language.

**Resolves:** D08-I01 and D08-I04.

**Content:** Create rows for customer identity, consent, driver and vehicle relationship, policy, credit contract, receivable balance, wallet event, platform settlement, cash bank statement, feature, score, model, policy rule, decision, intervention, borrowing base, accounting journal, financial statement, and regulator submission. Columns should identify authoritative source, replica, record key, clock, retention, correction, owner, and reconciliation.

State that D365 owns posted accounting journals and general-ledger balances, not raw telemetry or online features. The bank statement owns evidence of cash; legal agreements own contractual rights. The servicing ledger owns contractual balances. The evidence vault owns signed release packages. Define how conflicts are resolved and how corrections propagate.

**Acceptance tests:** Each record has one primary authority. No phrase says Gold and D365 are both ultimate. Reconciliation, not overwrite, resolves differences.

### D08-P04: Rewrite SPV accounting as evidence of legal transactions

**Action:** Replace GL segregation and subledger examples.

**Resolves:** D08-I03 and D08-I10.

**Content:** Begin with legal transaction events from D03 and D04: origination, carrier premium payment, receivable sale, cash purchase consideration, servicing, collection, refund, default, recovery, note funding, interest, principal, reserve, and distribution. For each show source document, servicing entry, cash entry, D365 journal, entity, currency, date, and reconciliation.

State that separate legal entities, accounts, dimensions, books, and journals support separateness but do not create true sale. Link legal opinions, account control, and servicing continuity. Have auditors decide derecognition, continuing involvement, consolidation, fee, tax, and FX policies. Avoid unsupported intercompany payable shortcuts.

**Acceptance tests:** Every journal balances and ties to cash or a documented accrual. Entity and currency are correct. Receivable sale entries follow legal and accounting conclusions.

### D08-P05: Design the medallion-to-accounting control bridge

**Action:** Rewrite “Asynchronous Kappa-to-Delta Statutory Bridge.”

**Resolves:** D08-I04 and D08-I05.

**Content:** Operational events enter Bronze. Silver validates schema, deduplicates, applies reference data, records corrections, and reconciles to source. Gold contains approved analytical and accounting facts, but it does not replace the ERP. Accounting facts move into a journal staging service with source batch, control totals, debit-credit balance, entity, period, currency, approval, idempotency, and posting status.

Define batch and event cut-off, failed records, partial posting, reversal, repost, close lock, late adjustment, intercompany elimination, and audit trail. Separate real-time operational estimates from period-end accounting. D365 acknowledgements and bank statements return for reconciliation.

**Acceptance tests:** Duplicate delivery cannot create duplicate journal. A partial failure is recoverable without imbalance. Gold, staging, D365, and bank cash reconcile by control ID.

### D08-P06: Govern pricing, models, policies, interventions, and journal effects

**Action:** Rewrite K-Generator and intervention automation.

**Resolves:** D08-I05, D08-I09, and D08-I10.

**Content:** Define interfaces among KESONIA service, pricing engine, model service, Credit Policy and Compliance Gate, servicing ledger, and D365. Customer rates for new or contractually eligible resets use KESONIA plus approved `K_RBCP` [1], [2]. D365 stores the approved contract schedule and accounting accrual. It does not recalculate risk premiums from SHAP values.

Record model version, feature version, posterior output, pricing decomposition, rule version, approval, effective date, notice, and contract. Define intervention orders and resulting cash, servicing, modification, ECL, and journal effects. Prevent retroactive repricing. Require maker-checker and legal or compliance approval for rule changes.

**Acceptance tests:** A model update cannot alter an existing contract. Pricing and journal examples reconcile to D09. Every intervention creates either a defined financial event or an explicitly non-financial audit event.

### D08-P07: Add data governance, privacy, and evidence-minimisation design

**Action:** Rewrite telemetry and explainability sections.

**Resolves:** D08-I08.

**Content:** Create a field inventory for D365, servicing, lakehouse, feature store, model registry, and evidence vault. For each field state purpose, authority, privacy class, lawful basis, owner, processor, access, encryption, retention, deletion, legal hold, export, and data-subject response. D365 should not copy high-frequency telemetry unless accounting or operations requires it.

Define a decision evidence record using immutable IDs and references rather than duplicating full payloads. Store feature, model, and rule versions plus approved reason codes. Protect sensitive explanations. Link DPIA and notices to [10], [11].

**Acceptance tests:** Purpose and retention exist for every personal field. Deletion and restriction are tested. Evidence remains sufficient without unnecessary raw data.

### D08-P08: Replace absolute security claims with a control architecture

**Action:** Rewrite the five cryptographic stages.

**Resolves:** D08-I07 and D08-I08.

**Content:** Create separate controls for input validation, immutable retention, encryption at rest, authenticated encryption in transit or payload, key management, digital signatures, certificate lifecycle, mTLS, maker-checker, access, audit, secrets, vulnerability management, backup, disaster recovery, and incident response. For AES-GCM specify key and nonce management, tag validation, rotation, and performance benchmark [12].

Define threat actors and failure modes: device spoofing, replay, credential theft, insider change, ransomware, data exfiltration, journal manipulation, key compromise, model substitution, and regulator-payload tampering. Map controls and residual risk.

**Acceptance tests:** No “absolute” or “military-grade” language remains. Nonce uniqueness and key recovery are tested. Security performance claims cite benchmark conditions. Restore and compromise exercises pass.

### D08-P09: Replace invented regulator telemetry with verified reporting adapters

**Action:** Rewrite “Cryptographic RegTech Sweep” transmission and external reporting.

**Resolves:** D08-I06.

**Content:** Import D07's regulatory reporting inventory. For each verified report define source facts, schema, validation, reconciliation, preparer, approver, signer, transport, acknowledgement, retention, and correction. Use ISO 20022 only for valid registered messages under an implementation guide [13]. Use XBRL only for an applicable taxonomy.

Create a transport-neutral internal canonical report and evidence package. If CBK or another authority later supplies an API, build an adapter and certification tests. Remove `auth.015` and custom tags from standard claims unless officially approved.

**Acceptance tests:** Every external interface has a recipient specification. A rejected submission is detected and corrected. Internal records can reproduce the exact submitted payload.

### D08-P10: Add fit-gap decisions, implementation controls, and acceptance tests

**Action:** Replace the conclusion and references.

**Resolves:** D08-I11 and closes all findings.

**Content:** Create architecture decision records for servicing ledger, D365 configuration, table format, feature store, evidence vault, key service, integration, ALM or FTP need, and reporting. Each decision should state options, requirements, security, privacy, cost, lock-in, recovery, operations, and approval.

List test suites: product and journal, receivable sale, daily accrual, close, cash reconciliation, waterfall export, duplicate and replay, performance, access, segregation of duties, encryption, key rotation, recovery, privacy, regulatory submission, and audit evidence. Use official and current product documentation.

**Acceptance tests:** No system is selected without a decision record. Critical accounting and security controls have automated or witnessed tests. The document differentiates designed, built, tested, and live states.

## Accounting reconciliation blueprint

Build daily and monthly reconciliations among servicing principal, receivables purchased by SPV, platform settlement, controlled bank cash, carrier premiums and refunds, reserve accounts, note balances, and D365 general ledger. Each reconciliation should have tolerance, break classification, owner, ageing, escalation, correction, and sign-off. No model score should directly alter a posted financial balance without a product event and approved journal.

At month end, freeze the servicing cut, ingest bank statements, complete cash application, resolve or reserve breaks, calculate EIR and ECL under approved policy, post controlled journals, reconcile subledger to GL, produce borrowing-base and waterfall reports, and retain evidence. Define late-event handling and post-close adjustment. This blueprint should be a formal dependency of D03 and D09.

## Recommended editing order and reviewers

Perform P01 through P03 first. Complete fit-gap before naming final products. Complete P04 and P05 with finance, servicing, cash, and audit. Complete P06 with D06, D07, and D09 owners. Complete privacy and security before building reporting adapters. Finish decisions and tests last.

Reviewers should include enterprise architect, D365 solution architect, servicing vendor, finance controller, accountant or auditor, treasury and cash operations, transaction counsel, DPO, security architect, SRE, model and policy owners, data architect, internal audit, regulatory reporting, trustee, platform, carrier, and bank operations.

## Pre-publication validation checklist

- Capability fit-gap is complete.
- System-of-record matrix has one authority per record.
- D365 is limited to approved ERP functions.
- Legal remoteness is not attributed to journals.
- Event-to-journal flow has control totals and idempotency.
- Pricing cannot change contracts retroactively.
- Privacy fields and evidence retention are controlled.
- Security claims are specific and tested.
- Regulator schemas are verified.
- Reconciliations and close process are complete.
- Headings, sources, and punctuation pass review.

## Interface specification catalogue

Create one controlled specification per integration: source platform to event ingestion; carrier to servicing; platform settlement to servicing and cash; servicing to feature pipeline; feature service to model; model to policy gate; policy to servicing; servicing to journal staging; journal staging to D365; bank statement to reconciliation; D365 and servicing to borrowing base; and report facts to external adapters. Each specification should state producer, consumer, purpose, schema, key, clocks, ordering, delivery, authentication, encryption, privacy, retention, control total, acknowledgement, error, retry, idempotency, version, and owner.

Financial interfaces need debit and credit totals, currency, entity, period, batch, source count and amount, and a hash or signature. Operational interfaces need source-health and freshness. Acknowledgement should distinguish received, validated, accepted, posted, and reconciled. Retry must not create duplicate draw, collection, receivable, journal, or regulator submission. Corrections require a linked reversal or version, not silent mutation.

Define failure behaviour. If the feature service is unavailable, the policy gate uses an approved fallback or blocks only affected decisions. If D365 is unavailable, approved journals remain in staging and no false posting acknowledgement is produced. If platform settlement is missing, servicing records a suspense and cash breaks are escalated. If the regulator adapter fails, evidence is retained and resubmission follows the reporting rule.

## Segregation of duties and privileged access model

Add a role matrix for source administration, schema approval, data-quality override, feature release, model release, policy change, pricing approval, servicing adjustment, journal preparation, journal approval, posting, bank payment, reconciliation, report preparation, signing, key administration, and audit. Prohibit one user or service from creating and approving the same material change. Separate production access from development.

Define privileged-access request, justification, time limit, approval, session logging, credential handling, emergency access, review, and revocation. Service accounts should have least privilege, managed identity where possible, rotation, and owner. Quarterly access certification should compare personnel, roles, and actual use. Departures and partner termination need immediate revocation and key or certificate review.

Maker-checker controls should verify business content, not only file transmission. A valid digital signature proves possession of a key, not correctness of the journal or report. The approver must see control totals, exceptions, source reconciliation, and impact. High-risk adjustments and related-party entries require elevated review.

## Migration, cutover, and parallel-close plan

Define source-data profiling, mapping, cleanse, deduplication, opening balance, contract and event migration, consent and retention, historical feature availability, journal opening, and evidence retention. Reconcile migrated receivables to contracts, customer statements, platform records, carrier records, cash, and legacy accounting. Preserve source identifiers and versions.

Run at least two parallel closes with servicing, cash, EIR, ECL, note balances, reserve, borrowing base, waterfall, and D365. Compare balances and movements, classify differences, correct root causes, and repeat until tolerances pass. Do not use an unexplained top-side journal to force agreement. Obtain finance and audit sign-off.

Cutover should define freeze, final extract, validation, business approval, go or no-go, rollback, customer and partner communication, heightened support, and post-cutover reconciliation. Retire legacy access only after retention and audit obligations are satisfied. This plan turns the architecture into a controlled financial transition instead of an integration demo.

## Definition of done

D08 is complete when auditors, operations, engineers, security, and regulators can trace each material balance and decision from authorised source through validation, approval, journal, report, and retained evidence. Every system must have a bounded role, and no vendor feature, ledger dimension, cryptographic primitive, or message label may be presented as legal compliance by itself.

## Architecture maintenance rule

Maintain the capability map, system-of-record matrix, interface catalogue, role matrix, data inventory, control library, and architecture decisions as versioned operational artefacts. A system, interface, or field change cannot be approved only through a ticket that omits accounting, privacy, security, reconciliation, reporting, and recovery impact. Material changes require design review and regression of the affected golden flows.

Quarterly, compare documented and deployed configurations, active interfaces, privileged roles, certificates, keys, retention, and reports. Record drift, owner, remediation, and risk acceptance. Annually, test vendor exit and data export for critical platforms. This keeps the rewritten paper aligned to the actual environment and prevents target-state diagrams from being mistaken for controls that operate in production.

The enterprise architect and controller should jointly certify the current diagram, reconciliation inventory, open control defects, and next review date. Unsupported drift must block claims of production readiness.
