---
title: "Part 4: Enterprise ERP and Telemetry"
author: "Nevil Maloba"
date: "25 August 2026"
status: "Narrative enterprise architecture edition"
output:
  pdf_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
  word_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
---




## 1. Institutionalization, Architectural Preservation, and the Microsoft Dynamics 365 Finance ERP Endpoint
### 1.1. Executive summary: when the model meets the books

At midnight, the driver's day must become a ledger that another institution can trust. A completed trip may have produced a fare, platform commission, protected operating amount, premium deduction, loan receipt, reserve movement, servicing fee, and SPV collection. The underwriting system may have changed a limit or recommended support. None of those facts becomes accounting merely because the model emitted JSON.

Parts 1 through 3 developed the economic, data, model, and intervention logic. Part 4 describes the institutional boundary: how approved product events become balanced journals, how legal entities remain separate, how a decision can be replayed, and how an ERP consumes financial primitives without ingesting raw 10 Hz telemetry.

The target stack uses Microsoft Dynamics 365 Finance as an enterprise general-ledger and entity-accounting endpoint, with Power BI as one reporting surface. Neither product is assumed to provide a complete lending subledger, IFRS 9 engine, IFRS 17 actuarial engine, asset-liability system, funds-transfer-pricing engine, trustee waterfall, or regulatory gateway. Those capabilities belong to specialised product services, controlled calculations, partner systems, or configured extensions.

The architecture cannot prove compliance by design. It creates evidence: reconciled events, model and policy versions, balanced entries, approvals, data lineage, exception queues, retained source documents, and reports that can be validated. The HLR produces calibrated risk evidence. A governed pricing service assembles \(K_{\mathrm{RBCP}}\) from risk and non-risk components. D365 records resulting accounting events after approval; it does not receive a model output as accounting truth.

### 1.2. Architectural Preservation and Augmentation Strategy

The most critical architectural constraint is preserving the high-frequency telemetry path without asking the enterprise ledger to become a stream processor. Banking ERPs are commonly optimised for controlled transactions, subledger integration, period close, and reporting. Even where an ERP can accept frequent events, raw 10 Hz telemetry, kinematic windows, and wallet-state computation belong in specialised event and analytical services. The underwriting path is therefore separated from the general ledger, with governed financial events crossing the boundary.

The architecture adopts a strictly decoupled, multi-layered approach:

**Figure 1: Event, decision, product-ledger, accounting, and reporting boundaries**

~~~mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#EAF2F8", "primaryBorderColor": "#2E6F95",
  "secondaryColor": "#EAF7EE", "tertiaryColor": "#FFF4DB",
  "lineColor": "#526D82"
}}}%%
flowchart LR
    subgraph STREAM["Operational and analytical plane"]
        SRC["Telematics | wallet | trip | policy | repayment"]
        KF["Kafka + Flink<br/>event time, state, quality"]
        NF["Neural representation"]
        EF["Explicit Liquidity Feature Path"]
        HLR["Calibrated HLR"]
        GATE["Credit Policy and Compliance Gate"]
        SRC --> KF
        KF --> NF
        KF --> EF
        NF --> HLR
        EF --> HLR
        HLR --> GATE
    end

    subgraph PROD["Contract and product plane"]
        LOAN["Loan servicing ledger"]
        POLICY["Insurer policy and claims system"]
        WALLET["Wallet / collection ledger"]
        SPV["SPV asset register + waterfall"]
        PRICE["Pricing component service"]
    end

    subgraph ACCOUNT["Accounting and control plane"]
        EVENT["Versioned accounting-event contract"]
        RULE["Accounting rules + maker-checker"]
        D365["D365 legal-entity ledgers<br/>subledger summaries + GL"]
        REC["Reconciliation and exception store"]
        EVENT --> RULE --> D365
        EVENT --> REC
        D365 --> REC
    end

    subgraph REPORT["Evidence and reporting plane"]
        LAKE["Immutable raw + curated evidence"]
        BI["Power BI management and investor views"]
        ADAPT["Regulatory / partner adapters<br/>only to issued specifications"]
        AUDIT["Audit replay package"]
        LAKE --> BI
        D365 --> BI
        D365 --> ADAPT
        REC --> AUDIT
        LAKE --> AUDIT
    end

    GATE -->|"authorised command"| LOAN
    GATE -->|"approved request"| POLICY
    LOAN --> EVENT
    POLICY --> EVENT
    WALLET --> EVENT
    SPV --> EVENT
    PRICE --> LOAN
    KF --> LAKE
    GATE --> LAKE
~~~

- **Layer 1: The Telemetry and Data Engineering Core**
  The Apache Kafka and Apache Flink stream processing layer acts as the foundational ingestion engine. Debezium captures Change Data Capture (CDC) events from the raw telematics databases and platform ledgers. This layer executes stateful stream processing, ensuring point-in-time correctness for the machine learning models.

- **Layer 2: The Neural-Bayesian Underwriting Engine**
  The neural and Explicit Liquidity Feature paths meet in the redundancy-controlled HLR. It emits calibrated PD, uncertainty, model version, and explanation inputs. The downstream Credit Policy and Compliance Gate emits an authorised action. Pricing is a separate service that reconciles \(K_{\mathrm{RBCP}}\) to expected loss, cost of capital, operating and liquidity costs, margin, and approved adjustments.

- **Layer 3: The Integration API and Transformation Middleware**
  The middleware validates commands from named product owners and translates product-ledger events into versioned accounting-event contracts. It does not invent an "IFRS-compliant" journal from a model action. A premium holiday first changes the insurer's policy or finance contract, then the responsible accounting rule produces entries supported by that change.

- **Layer 4: Microsoft Dynamics 365 Finance & Operations (GDI & SupTech Node)**
  D365 serves as the general-ledger and legal-entity accounting endpoint for configured journals. Product ledgers remain systems of record for contracts and transaction detail. Regulatory or partner submissions use separate adapters built only after an authoritative schema, taxonomy, frequency, and submission protocol are confirmed. No CBK GDI or SupTech interface is assumed.

- **Layer 5: Microsoft Power BI & The Regulatory Gold Tables**
  Power BI presents management, model-risk, servicing, SPV, and investor views from governed semantic models. A dashboard is not a regulatory filing or evidence by itself. Every metric retains source, owner, as-of time, definition, and reconciliation status.

### 1.3. Microsoft Dynamics 365 Finance: The Regulatory ERP Endpoint

The selection of D365 is a strategic ERP choice, subject to fit-gap, configuration, volume, licensing, security, and integration testing. D365 can be the authoritative general ledger for each configured legal entity. The loan servicer, insurer, wallet ledger, and SPV register remain authoritative for their own contracts and events, then reconcile to D365.

#### 1.3.1. Product subledgers and the D365 integration boundary
A scaled gig-economy portfolio can produce many daily credit, insurance, wallet, settlement, and reversal events. A single driver may generate a loan disbursement, several authorised fare deductions, a policy transaction, and a reserve movement in one day. The target volume must be benchmarked rather than fixed at an unsupported 100,000 drivers. Product systems retain contract-level operational state, while the D365 design receives the detail or summary needed for controlled accounting and reporting.

- **Loan servicing ledger:** Tracks contract principal, interest, fees, schedules, receipts, arrears, modifications, write-offs, and customer balances. D365 receives controlled summaries or detailed journals according to the chosen design.
- **Insurer policy and claims system:** Tracks premium, coverage, claims, cancellation, and insurer accounting inputs. An IPF receivable remains distinct from the insurer's unearned coverage liability.
- **Wallet and collection ledger:** Tracks settlement ownership, authorised deductions, reversals, residuals, driver reserves, and controlled SPV collections. It is not called escrow without the legal account structure.
- **SPV asset register and waterfall:** Tracks eligibility, purchase, note balances, reserves, tests, and priority of payments.

The credit-risk extension adds a common contract-and-risk spine to these systems. At minimum it carries driver, product, facility, contract, risk-episode, vehicle, policy, platform, geography, and cohort keys; contractual schedule and next due date; limit, utilisation, principal, interest, fees, arrears, modification, default, cure, and closure states; event, availability, decision, label-maturity, accounting, and cash-realisation times; current and stressed EAD; recovery, refund, cost, and write-off cash flows; intervention and policy versions; and model, calibration, feature, hierarchy, and posterior-artifact versions. Each field has one authoritative owner and an effective-time history.

The risk platform retains the granular posterior and timing paths. The servicing ledger retains contractual balances and states. The ECL engine retains scenario-weighted accounting estimates. The SPV register retains purchased-asset and waterfall facts. D365 receives approved accounting events and reconciliation keys. This distribution allows every institution to use the same economic episode without asking the general ledger to store posterior draws or the model registry to become a receivables ledger.

Telematics does not become a journal. Financial product events are reconciled and transformed into balanced journal batches. Posting may occur intraday or at a controlled cut-off, with idempotency key, debit-credit balance, entity, currency, account, dimension, source event, reversal reference, approval, and period status. OData or the Data Management Framework is selected after throughput testing. Driver-level auditability remains in the product ledger and evidence store even when the GL receives a summary.

#### 1.3.2. Mapping the governed pricing service to product and accounting systems
Under CBK's revised framework, the customer lending rate is $R_{\mathrm{customer}}=\mathrm{KESONIA}+K_{\mathrm{RBCP}}$, with fees and charges added for total cost of credit [4], [5]. The HLR supplies calibrated risk inputs; the governed pricing service calculates and approves the full premium.

The authoritative KESONIA series is ingested with publication date, effective date, source, checksum, calendar, corrections, and fallback status [6]. Whether D365 can calculate the exact contractual convention natively is a fit-gap item; the loan servicing or pricing engine may calculate accrual and post the result.

The fit-gap is resolved contract by contract rather than by treating "D365 integration" as a complete design. The implementation team first records the KESONIA observation window, compounding method, day-count basis, margin, floor, cap, reset date, customer-notice rule, fallback, rounding, and correction treatment. It then configures representative IPF, microloan, and revolving contracts in a controlled environment and compares the native result with an independently approved calculation schedule. Finance, product, risk, accounting, and technology owners jointly approve the result and the system boundary [7].

Where native configuration reproduces the contract and required audit trail, D365 may calculate or control the event. Where it does not, the pricing or product subledger remains the calculation engine and sends an approved accrual or accounting event to D365. The interface retains instrument identifier, source series, observation dates, factor, spread, effective date, currency, correction status, approval, and reconciliation key. This approach addresses the fit-gap without forcing the general ledger to imitate a product engine or allowing an external service to post unexplained totals.

A contractual rate changes only under the loan terms, customer notice, applicable rules, and authorised lender policy. Daily model movement must not silently reprice an existing contract. The record distinguishes a new-offer price, a permitted reset, a modification, and a monitoring-only risk movement. IFRS 9 classification follows the reporting entity's analysis, not an ERP timestamp.

#### 1.3.3. Automating Assistive Interventions in D365
Assistive interventions become accounting events only after the licensed product owner authorises a contractual action and the responsible accounting function assigns treatment.

- **Premium schedule support:** The licensed insurer and finance provider first approve any contract or collection change. Their product systems emit the amended coverage, receivable, premium, and cash-flow events. Accounting rules then post the appropriate entries. Cover, earned premium, liability, ECL, and modification treatment are not fixed by a generic D365 flag.
- **Micro-reward bridge:** The platform and lender record the offer, driver acceptance, fare, deduction authority, and loan receipt. Cash is allocated according to the actual contract and law. Receipt may support cure but does not automatically avert Stage 3.

### 1.4. Sub-Ledger to General Ledger Pipeline Mechanics and IFRS 9 Staging

The ECL process can use higher-frequency evidence, but the accounting owner remains responsible. Integration automates data preparation, calculation inputs, journal workflow, and evidence retention while preserving review, overlays, and controls.

#### 1.4.1. Higher-frequency IFRS 9 evidence and controlled staging
Days past due remains important and may serve as a rebuttable backstop under an entity's IFRS 9 methodology, but it need not be the only evidence of Significant Increase in Credit Risk. For some gig-economy borrowers, cash flow can deteriorate before a contractual payment becomes past due. The platform tests whether permitted higher-frequency evidence provides reliable incremental warning; it does not assume that every driver reaches zero cash or that a universal 20-day clock exists.

The HLR is an evidence source, not a staging oracle. The approved SICR service evaluates lifetime-PD movement, ratings, arrears, qualitative factors, macro scenarios, backstops, and overrides. DPD remains relevant evidence. The service writes a proposed stage, reasons, calculation version, and approval status; it does not bypass the methodology.

The base configuration uses a governed ECL engine outside the general ledger, with D365 controlling approved journals, consolidation, workflow, and reporting. A native or hybrid D365 route remains available if the fit-gap test proves that it reproduces the reporting entity's approved methodology, contract-level cash flows, scenario logic, effective-interest discounting, overlays, and audit evidence [8].

The governing quantity is the probability-weighted present value of cash shortfalls. For scenario \(s\) and cash-flow date \(\tau\),

$$
ECL_i
=
\sum_s w_s
\sum_\tau
\left(
CF^{\mathrm{contract}}_{i,\tau}
-CF^{\mathrm{expected}}_{i,s,\tau}
\right)
DF_{i,\tau}.
$$

The expected cash flow includes scheduled exposure, drawdown, cure, prepayment, modification, ordinary recovery, eligible IPF refund, costs, and their timing. The factorised PD-LGD-EAD form below is a controlled computational representation only when its marginal default convention, exposure path, loss severity, cash timing, and discounting reproduce the approved cash-shortfall methodology.

For scenario (s) and future interval \(\tau\), the controlled calculation can be represented as:

$$
ECL_i
=
\sum_s w_s
\sum_{\tau}
PD_{i,s,\tau}
\times LGD_{i,s,\tau}
\times EAD_{i,s,\tau}
\times DF_{i,\tau},
$$

with the horizon, marginal or conditional PD convention, cure and recovery treatment, scenario weights, and discount factor defined in the accounting methodology. The HLR contributes calibrated evidence; the approved SICR and ECL services determine how that evidence enters staging and measurement.

The fixed-horizon HLR and the timing challenger enter through an approved reconciliation layer. Cumulative PD is never multiplied afresh in each month. Where the survival model is used, monthly marginal default probability is \(q_{i,m}=S_i(t_{m-1})-S_i(t_m)\). Where only horizon PD is approved, a documented term-structure allocation converts it to marginal cash-flow intervals and is calibrated back to the horizon total. The accounting engine records which route and artifact version generated each estimate.

The approved output passed to D365 contains the legal entity and reporting period; instrument or portfolio identifier; approved IFRS 9 stage; PD, LGD, EAD, scenario, model, rule, and overlay versions; opening and closing allowance; impairment movement; modification, write-off, recovery, and reversal identifiers; maker-checker status; posting profile; dimensions; journal date; currency; and reconciliation key. The loan subledger remains capable of reproducing the contract balance and ECL source data even when the general ledger receives an aggregated entry.

This creates three controlled deployment choices. A **native route** is used where D365 passes the fit-gap and independent recalculation. An **external route** calculates staging and ECL in a dedicated governed engine and sends approved journal instructions. A **hybrid route** retains the detailed calculation externally while using D365 for workflow, posting, consolidation, control evidence, and reporting. In every route, an unapproved model payload cannot unilaterally change an accounting stage.

#### 1.4.2. General Ledger Consolidation and SPV Segregation
Mwendo Pamoja operates multiple legal entities, primarily the main operating Insurtech entity and the proposed bankruptcy-remote Special Purpose Vehicle (SPV) that holds eligible purchased microloan, revolving-credit, and IPF finance receivables, excluding insurer-owned or unremitted premium cash. D365 Finance's multi-company architecture can represent the resulting multi-entity accounting structure after the legal and accounting design is approved.

The ERP provisions distinct legal-entity ledgers and dimensions. The licensed originator first records the loan under its approved accounting. A later receivable sale is recorded only after eligibility, purchase price, transfer, settlement, derecognition or continuing-involvement analysis, and supporting documents. The precise journals depend on those facts and are defined in an accounting-rules catalogue rather than hard-coded in this narrative.

Multi-company bookkeeping supports reconciliation but does not create bankruptcy remoteness, true sale, security, account control, or servicing continuity. Those are legal and operational conditions. When established, D365 records each entity's approved journals while the SPV asset register and waterfall calculate investor allocations. The USD 9 million equivalent structure is operated in KES and remains subject to the transaction tests described in the memorandum and term sheet.

## 2. Telemetry, SHAP/XAI, and Data Pipeline Enhancements
### 2.1. Explainability and the Algorithmic Fairness Mandate

The decision record must be explainable to the driver, lender, validator, auditor, and, where applicable, supervisor. "Total" or legally indisputable transparency is not promised. The record combines explicit feature contributions, neural diagnostics, pricing-component reconciliation, policy reasons, data quality, overrides, and outcome monitoring.

#### 2.1.1. SHAP (SHapley Additive exPlanations) for Regulatory Governance
The dual-regime architecture outputs a residual neural representation which, together with the Explicit Liquidity Features, enters the HLR and contributes to posterior PD. A SHAP pipeline may help explain a clearly identified model output. It cannot attribute the full customer premium because $K_{\mathrm{RBCP}}$ also contains cost, capital, liquidity, margin, and approved adjustments.

SHAP values provide an additive attribution under a specified value function and background distribution. They describe model behaviour rather than causal blame, and their stability and approximation error must be tested. The evidence flow is:

1. **Inference time:** The service records the feature and model versions, calibrated output, uncertainty, policy result, and latency. A local explanation may be synchronous only when a tested method meets the service level.
2. **Evidence storage:** Explanation artefacts are stored with model, background distribution, feature, and decision versions. Earnings Velocity and Repayment Velocity remain explicit features and are not attributed to the GRU.
3. **Analysis and reporting:** Gold views may aggregate explanation diagnostics for authorised validation, risk, complaints, and audit users. Any supervisory access or submission follows an actual request and prescribed channel; a Power BI view is not presumed to be a CBK regulatory interface.

If a driver challenges \(K_{\mathrm{RBCP}}\), an authorised user can retrieve the customer price, component reconciliation, material reason codes, model limitations, and review route. SHAP explains model behaviour under assumptions; it does not by itself justify the entire price.

#### 2.1.2. Equalized Odds and Continuous Fairness Monitoring
The architecture monitors fairness as an ongoing risk rather than claiming to prevent it by formula.

- **Monitoring service:** A controlled analytics service calculates coverage, calibration, error, approval, price, limit, intervention, complaint, and outcome metrics on lawfully governed audit attributes. Protected status is not casually inferred from geography.
- **DIR alerts:** A value such as 0.80 is a diagnostic benchmark, not a universal Kenyan regulatory threshold.
- **Case management:** A material alert creates a case for review. Any corridor-level restriction requires evidence, authority, impact analysis, and a cure rule; an alert does not automatically penalise every driver in that place.

### 2.2. The Asynchronous Kappa-to-Delta Statutory Bridge

As established in **Part 2a**, the real-time underwriting decisions execute on a high-speed Kappa stream (via Redis and Flink) to bypass the latency of the data lake. However, Microsoft Dynamics 365 and Power BI require immutable, structured relational data to perform statutory accounting.

To resolve this latency mismatch, the architecture utilizes an **Asynchronous Kappa-to-Delta Bridge**. This strictly contrasts the real-time underwriting execution (the high-frequency Kappa path running on Redis/Flink) from the statutory compliance pipeline (the Delta/Medallion batch path required for historical audibility).

The integration layer consumes durable product and decision events. A loan issue, receipt, modification, write-off, policy event, asset purchase, waterfall allocation, or approved staging result can create an accounting or evidence record. A routine posterior update does not create a GL entry. Curated tables are derived data products, not "rigid accounting ledgers."

This Gold Layer acts as the ultimate Statutory ERP Bridge, containing:
- **The SPV Waterfall Table:** Pre-aggregated daily interest collections, micro-loan originations, and Class A/B allocations.
- **The IFRS 9 Staging Table:** Driver-level probability of default, LGD, and SICR flags.
- **The Pricing Engine Table:** The daily calculated Cumulative Compounded Rate (CCR) for KESONIA, merged with the driver's "K" premium.

D365 receives validated journal interfaces and reference data; Power BI reads governed semantic models. Neither is required to use the same Gold table, and both reconcile to authoritative product ledgers and the GL.





## 3. The controlled reporting and evidence pipeline

Enterprise integration does not solve IFRS 9 or regulatory reporting by itself. The responsible institution first identifies each actual filing, partner report, investor report, frequency, schema, signatory, control, and delivery channel. The evidence pipeline then implements those requirements.

Automation prepares and validates reports, but accountable review remains where the filing or internal policy requires it. The five stages below are a control pattern, not a claim about a CBK submission interface.

### 3.1. Stage 1: Automated Validation Gates and Bounds Checking

Before a controlled report leaves the institution, validation checks the schema, source reconciliation, accounting period, currency, sign, range, completeness, duplicate status, exceptions, approvals, and report-specific rules. The ERP is one source and workflow endpoint, not an infallible sovereign.

The validation gates execute:
1. **Contract and legal bounds:** Apply counsel-approved interest, fee, notice, product, and in-duplum logic to the relevant balance and circumstance.
2. **Rate controls:** Reconcile KESONIA to the official publication and the contractual compounding convention; investigate material change without treating volatility as an error.
3. **Identity and KYC controls:** Validate required status through authorised sources and preserve error, unavailable, and review states. A hash match is not proof of identity or legal eligibility.

If a loan record fails a validation gate, it is instantly routed to an Exception Queue within D365. Crucially, the architecture utilizes non-blocking exception routing: the failure of Loan A does not prevent the transmission of compliant Loans B through Z. This prevents the "batch failure" pathologies common in legacy banking architectures.

### 3.2. Stage 2: Immutable WORM Repositories

Records that pass the validation gates are immediately serialized into an Immutable Write-Once-Read-Many (WORM) storage repository hosted on Azure Blob Storage.

Immutable or locked storage can support evidence retention when the applicable schedule and policy require it. This paper does not assert that CBK requires daily SHAP snapshots or a particular WORM service. Retention, legal hold, deletion rights, privacy, and key management must be reconciled.

Hash chaining can make later alteration detectable when anchors, keys, clocks, access logs, and verification are independently controlled. It does not provide absolute assurance or prevent authorised deletion under a misconfigured policy. Verification jobs and incident response are part of the design.

### 3.3. Stage 3: AES-256 GCM Encryption and Authenticated Telemetry

For an approved transmission, the security profile may use AES-GCM in accordance with NIST SP 800-38D [1], subject to nonce uniqueness, approved key management, rotation, access control, and protocol design.

AES-GCM provides authenticated encryption when implemented correctly. Security is not absolute, and performance must be benchmarked at the actual payload size and hardware. Transport, endpoint, credential, metadata, and operational risks remain.

### 3.4. Stage 4: Maker-Checker Segregation and X.509 PKI Digital Signatures

Regulatory submissions carry profound legal weight; submitting inaccurate capital or pricing data is a severe prudential violation. Therefore, the system enforces a strict "Maker-Checker" workflow.

In this architecture, the **Maker** is the automated RegTech Sweep pipeline (executing within Azure Data Factory and D365). It compiles, validates, and encrypts the data. However, the system cannot transmit the data autonomously.

The **Checker** is a designated human Chief Risk Officer (CRO) or Chief Compliance Officer. Through a secure Power Apps interface, the CRO is presented with a high-level statistical summary of the daily submission (e.g., Total Principal Outstanding, Average KESONIA Yield, Max/Min Risk Premium $K$, and Total Records Flagged in Exception Queue).

The approved signatory authorises the submission using the institution's specified authentication and signing control. Hardware-backed X.509 signatures are one option where the receiving specification accepts them. A digital signature provides integrity and signer authentication under the trust framework; it does not make the figures accurate or create absolute non-repudiation.

### 3.5. Stage 5: Mutual TLS (mTLS) Transmission

The final stage of the RegTech sweep is the physical transmission of the signed, encrypted payload. The architecture utilizes a Mutual Transport Layer Security (mTLS) API tunnel to the central bank. Unlike standard TLS (where only the client verifies the server's certificate), mTLS requires both the central bank's server and the Mwendo Pamoja SPV's client server to cryptographically authenticate each other before any data is exchanged.

The five-stage pattern produces a reviewable chain from source event to approved report. Encryption, mutual authentication, signatures, reconciliation, model governance, fairness review, accounting controls, and legal validation operate as complementary layers. Transport controls protect the submission path and provenance, while the wider control framework establishes the quality and authorised meaning of the underlying information.

```{=latex}
\clearpage
```

## References

[1] Dworkin, M. (2007). *Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC*. NIST Special Publication 800-38D. National Institute of Standards and Technology. [https://csrc.nist.gov/publications/detail/sp/800-38d/final](https://csrc.nist.gov/publications/detail/sp/800-38d/final)

[2] Basel Committee on Banking Supervision (BCBS). (2015). *Corporate governance principles for banks*. Bank for International Settlements.

[3] European Union Agency for Cybersecurity (ENISA). (2021). *Security Guidelines on the appropriate use of qualified electronic signatures*.

[4] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Nairobi, Kenya, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. Accessed: Aug. 25, 2026.

[5] Central Bank of Kenya, "Issuance of a revised risk-based credit pricing model," Press Release, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/uploads/press_releases/2044081907_Press%20Release%20-%20Issuance%20of%20a%20Revised%20Risk-Based%20Credit%20Pricing%20Model.pdf. Accessed: Aug. 25, 2026.

[6] Central Bank of Kenya, "Kenya Shilling Overnight Interbank Average (KESONIA)." [Online]. Available: https://www.centralbank.go.ke/kesonia/. Accessed: Aug. 25, 2026.

[7] Microsoft, "Application lifecycle management for Dynamics 365 implementation." [Online]. Available: https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/application-lifecycle-management-product. Accessed: Aug. 25, 2026.

[8] IFRS Foundation, *IFRS 9 Financial Instruments: Project Summary*, July 2014. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/project/fi-hedge-accounting/ifrs-standard/project-summary.pdf. Accessed: Aug. 25, 2026.
