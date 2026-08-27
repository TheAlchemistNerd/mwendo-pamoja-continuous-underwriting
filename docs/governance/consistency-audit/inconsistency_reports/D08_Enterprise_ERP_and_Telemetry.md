# D08 Inconsistency Report: Enterprise ERP and Telemetry

## Document role and semantic synopsis

D08 is meant to institutionalise the model through Dynamics 365 Finance, accounting journals, statutory records, explainability telemetry, medallion data flows, cryptographic controls, and regulatory reporting. It correctly recognises that an underwriting platform is incomplete without controlled posting, reconciliation, evidence, and access governance. It also proposes useful defence layers such as WORM retention, authenticated encryption, maker-checker approval, certificates, and mTLS.

The paper nevertheless turns D365 into several systems it is not: banking loan subledger, insurer subledger, ALM and FTP engine, immutable evidence store, policy orchestrator, and regulator SupTech gateway. It assigns both the Gold lakehouse and D365 as the ultimate record. It assumes GL entries create SPV segregation, direct Kappa-to-Gold writes preserve control, and custom ISO 20022 tags establish external interoperability.

## Executive inconsistency summary

D08 should be rewritten as a system-of-record and control-boundary specification. D365 Finance should own approved statutory accounting journals and general-ledger balances. A servicing ledger should own contractual receivable balances and cash allocation. The event lake should own raw and curated telemetry, the feature store should own online feature versions, the model registry should own approved models, and an evidence vault should own immutable audit artefacts. D365 can receive summarised or instrument-level postings through controlled interfaces but does not natively supply financial ALM or matched-maturity FTP [14]-[17].

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D08-I01 | Critical | High | Sections 1 to 4 | D365 is assigned unsupported banking and insurance functions |
| D08-I02 | High | High | Pricing and ALM claims | Microsoft ALM is confused with asset-liability management |
| D08-I03 | Critical | High | GL segregation | Accounting entries are treated as bankruptcy remoteness |
| D08-I04 | Critical | High | Kappa-to-Delta bridge | Gold and D365 both claim ultimate authority |
| D08-I05 | High | High | Direct statutory bridge | Proposed flow bypasses validation and close controls |
| D08-I06 | Critical | High | Regulatory sweep | ISO 20022 and CBK SupTech fields are unverified |
| D08-I07 | High | High | Encryption section | Security language is absolute and performance is unsupported |
| D08-I08 | High | High | Telemetry and XAI | Data protection, retention, and access purposes are incomplete |
| D08-I09 | High | High | Model and policy integration | Dynamic `K` changes and rule versioning lack control |
| D08-I10 | High | Medium | Journal examples | Entries and intercompany mechanics may contradict true sale |
| D08-I11 | Medium | High | Heading and editorial structure | Numbering and evidence hierarchy are broken |

## Detailed findings

### D08-I01: Dynamics 365 is treated as a native regulated-finance platform

**Anchor:** “Microsoft Dynamics 365 Finance: The Regulatory ERP Endpoint,” “D365 Sub-Ledger Architecture,” and “Mapping the K-Generator.” The draft suggests D365 natively manages microloan, revolving, insurance, ECL, pricing, ALM, FTP, and regulatory functions.

**Impact:** D365 is a capable ERP, but product servicing, loan-level accrual, credit-state transitions, insurance contract measurement, model execution, and matched-maturity FTP generally require specialist applications, ISV solutions, or controlled customisation. Misstating native capability creates procurement, audit, and operational risk.

**Canonical resolution:** Define D365 as the ERP and general-ledger endpoint. Conduct a fit-gap by requirement. Assign contractual balances and customer schedules to a servicing ledger; IFRS 9 calculations to an approved risk engine; model decisions to the underwriting service; insurance accounting to the carrier; and instrument-level ALM or FTP to a specialist engine if required. Oracle documents show the depth of native FTP and ALM functions [14], [15].

### D08-I02: “ALM” citations refer to application lifecycle management

**Anchor:** D365 capability discussion and related question-draft sources. Microsoft pages [16], [17] use ALM to mean application lifecycle management, not asset-liability management. A Marketplace “FTP connector” [39] refers to file transfer protocol, not funds-transfer pricing.

**Impact:** This is a direct semantic-source mismatch. It could lead readers to approve a system without the cash-flow, yield-curve, repricing, liquidity, and behavioural functions needed for financial ALM.

**Canonical resolution:** Remove those citations from asset-liability and funds-transfer-pricing claims. Retain [16], [17] only for software release governance. Use [14], [15] to define specialist requirements, then select technology through a fit-gap and cost-benefit assessment.

### D08-I03: Ledger segregation does not create bankruptcy remoteness

**Anchor:** “General Ledger Consolidation and SPV Segregation.” The paper treats intercompany journals, dimensions, and separate books as creating legal ring-fencing.

**Impact:** Legal ownership, perfected transfer, separateness, controlled accounts, servicing continuity, and non-consolidation depend on transaction documents and conduct. A shared ERP can support evidence but cannot cure a defective sale or commingling.

**Canonical resolution:** Rewrite the section as “Accounting Evidence for SPV Separateness.” Link every journal to purchase agreement, cash movement, receivable-level transfer file, bank statement, borrowing-base certificate, and reconciliation. List true-sale and non-consolidation opinions as external conditions.

### D08-I04: The authoritative-record model contradicts itself

**Anchor:** “Executive Summary,” “D365 Regulatory ERP Endpoint,” “Asynchronous Kappa-to-Delta Statutory Bridge,” and cryptographic sweep. D365 is called the immutable ultimate source while Gold is called the statutory or sovereign source.

**Impact:** During a correction, audit, dispute, or replay, teams will not know which record controls. An analytical Gold table may be recomputed, while an ERP journal may be posted and later adjusted. Neither should silently overwrite the other.

**Canonical resolution:** Publish a system-of-record matrix: source platforms for original business events; servicing ledger for contractual balances; controlled lakehouse for curated event history; feature store for online features; model registry for approved artifacts; D365 for posted accounting; evidence vault for immutable approvals and payloads. Reconcile, do not collapse, these authorities.

### D08-I05: Direct Kappa-to-Gold and real-time statutory posting bypass controls

**Anchor:** “The Asynchronous Kappa-to-Delta Statutory Bridge.” The design suggests streaming outputs can write directly to Gold and D365 at very high frequency.

**Impact:** Raw or preliminary model events can become statutory facts before validation, deduplication, approval, cutoff, and period-close controls. Exactly-once stream processing does not guarantee balanced, approved, exactly-once journals.

**Canonical resolution:** Raw events enter Bronze, validated and deduplicated events enter Silver, and approved facts enter Gold. Financial postings use a journal staging area with batch ID, source total, debit-credit balance, maker-checker approval, idempotency, ERP response, rejection handling, and reconciliation. Real-time operational estimates remain separate from posted accounting.

### D08-I06: Regulatory messaging is speculative

**Anchor:** “The Cryptographic RegTech Sweep” and transmission stages. The document presents custom ISO 20022 tags, `auth.015`, XBRL, and direct CBK telemetry as established interfaces.

**Impact:** There is no evidence in the corpus that CBK accepts these model and accounting fields. ISO 20022 messages have governed business definitions and XBRL has separate taxonomy processes [13]. An invented schema can fail validation and misrepresent regulatory readiness.

**Canonical resolution:** Inventory actual regulator reports and channels. Keep internal evidence in an immutable package containing model version, feature version, rule version, score, uncertainty, decision, reason codes, approvals, and accounting link. Build an external adapter only after the regulator supplies or approves a schema and endpoint.

### D08-I07: Cryptography is described as absolute security

**Anchor:** AES-256-GCM, WORM, PKI, and mTLS sections. The draft uses terms such as “military grade,” “absolute,” and very high throughput without benchmark conditions.

**Impact:** AES-GCM can fail catastrophically with nonce reuse, weak key handling, or skipped tag verification. WORM storage does not guarantee semantic accuracy. Certificates do not guarantee authorised business content.

**Canonical resolution:** Use control-specific language. Define key ownership, HSM or managed-key service, IV construction, tag size, rotation, revocation, access, audit, performance test, backup, recovery, and incident response, following [12]. Distinguish confidentiality, integrity, authenticity, non-repudiation, retention, and application approval.

### D08-I08: Telemetry governance lacks purpose and retention boundaries

**Anchor:** “Telemetry, SHAP/XAI, and Data Pipeline Enhancements.” The design stores detailed driver and model information in multiple systems but does not consistently state purpose, lawful basis, minimisation, retention, or customer rights.

**Impact:** Duplicated sensitive data expands breach exposure and makes deletion difficult. SHAP artefacts can reveal sensitive inferences and model intellectual property. Kenyan data-protection obligations remain even when records are encrypted [10], [11].

**Canonical resolution:** Create a field-level data inventory with purpose, owner, processor, lawful basis, access role, encryption, retention, deletion, and export control. D365 should receive only accounting and operational fields needed for its role. Keep detailed telemetry and explanations in governed stores and reference them by immutable ID.

### D08-I09: Dynamic pricing and policy rules lack contract and release controls

**Anchor:** “Mapping the K-Generator to D365 Pricing Engines” and intervention automation. The text implies that model changes can dynamically update `K` or customer terms through D365.

**Impact:** A score change does not authorise repricing an existing contract. Changes may require notice, consent, contractual reset dates, fair-treatment review, and accounting analysis. Rule and model changes also need versioned approval.

**Canonical resolution:** D365 stores the contract rate and approved schedule. A pricing service proposes rates for new or contractually eligible resets using KESONIA plus `K_RBCP`. The policy gate verifies floor, cap, affordability, notice, and approval. Record model version, pricing decomposition, rule version, effective date, and customer disclosure. No retroactive updates.

### D08-I10: Journal examples may undermine true-sale cash logic

**Anchor:** subledger and GL pipeline examples. The paper uses intercompany payable or receivable entries for SPV acquisition without a complete purchase consideration and settlement trail.

**Impact:** An intercompany balance can imply financing or retained control rather than cash sale. Incorrect gross versus net treatment can misstate receivables, premium remittance, servicing fees, and consolidation.

**Canonical resolution:** Have transaction counsel and auditors approve illustrative entries. Show origination, carrier premium payment, receivable sale, cash consideration, derecognition or continuing involvement, servicing fee, collections, reserve, defaults, recoveries, note interest, and distributions. Tie every entry to legal form and bank cash.

### D08-I11: Structure and citations obstruct review

**Anchor:** Heading numbers jump from Section 4 to 9 and repeat 9. References mix official, vendor, and weak sources. Marketing terms are used as control conclusions.

**Impact:** Requirements, controls, and evidence cannot be traced. Reviewers may mistake a vendor capability claim for an implemented control.

**Canonical resolution:** Renumber sequentially, add requirement and control IDs, cite the IEEE index, label target versus implemented state, and add a fit-gap appendix. Remove long dashes, mojibake, and absolute claims.

## Dependencies, evidence gaps, and remediation sequence

D08 depends on D04's product ledger, D05's event lineage, D06's model outputs, D07's reporting inventory, D09's accounting and FTP requirements, and D10's deployment gates. Required evidence includes D365 licence and configuration scope, solution architecture, servicing platform choice, chart of accounts, journal design, audit requirements, data inventory, DPIA, key-management design, regulator schemas, integration tests, backup-servicing plan, and legal opinions.

Remediation order is: freeze authoritative systems; perform fit-gap; define accounting staging and reconciliation; separate operational from statutory latency; establish privacy and security controls; govern pricing and interventions; then build regulator adapters only from verified requirements. D08 is ready when every record has one authority and every journal ties to cash, contract, source event, approval, and immutable evidence.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D08-I01 | D08-P02, D08-P03 |
| D08-I02 | D08-P02 |
| D08-I03 | D08-P04 |
| D08-I04 | D08-P03, D08-P05 |
| D08-I05 | D08-P05, D08-P06 |
| D08-I06 | D08-P09 |
| D08-I07 | D08-P08 |
| D08-I08 | D08-P07, D08-P08 |
| D08-I09 | D08-P06 |
| D08-I10 | D08-P04, D08-P06 |
| D08-I11 | D08-P01, D08-P10 |
