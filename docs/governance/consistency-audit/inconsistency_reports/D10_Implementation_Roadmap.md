# D10 Inconsistency Report: Implementation Roadmap and Execution

## Document role and semantic synopsis

D10 is the execution bridge from the architecture and financing papers to an operational pilot. It proposes a six-to-seven-month sequence involving data engineering, middleware, Dynamics 365, Power BI, shadow validation, a revised SPV model, Azure services, ISO 20022, and regulatory positioning. Its value is that it names tangible work packages rather than stopping at strategy.

The roadmap is nevertheless ordered around technology installation rather than transaction readiness and controlled learning. Legal entity design, licences, platform and carrier contracts, data rights, privacy assessment, portfolio definitions, model validation, security threat modelling, procurement, servicing, accounting policy, and operational readiness are not credible prerequisites. The SPV model appears late, after ERP configuration, even though it should define many requirements. The schedule has no critical path, accountable owners, entry and exit evidence, go or no-go decisions, rollback, or contingency.

## Executive inconsistency summary

The timeline is an aspiration rather than an implementation baseline. It should be replaced with gated phases that can overlap only where dependencies allow: mobilisation and decision rights; legal, commercial, data, and financial foundations; governed data pilot; model development and independent validation; product, servicing, accounting, and policy integration; shadow operation; controlled live pilot; and scale decision. The financial model and term sheet must be established before D365 design. ISO 20022 and regulatory telemetry must wait for verified schemas. Exact Azure product choices and a `generate_spv_model.ps1` script should not be presented as facts without repository evidence or architecture decisions.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D10-I01 | Critical | High | Sections 15 and 16 | Sequence places legal and financial foundations too late |
| D10-I02 | Critical | High | Months 1 to 6 | Six-month plan omits material dependencies and approvals |
| D10-I03 | High | High | All phases | No RACI, gates, acceptance criteria, or rollback |
| D10-I04 | High | High | D365 and Azure phases | Product choices precede fit-gap and procurement |
| D10-I05 | High | High | SPV model enhancements | Model generation and validation are under-specified |
| D10-I06 | Critical | High | ISO 20022 convergence | External messaging assumptions are unverified |
| D10-I07 | Critical | High | Data pipeline and shadow mode | Privacy, consent, and data rights are not gating work |
| D10-I08 | High | High | MLflow and control claims | Reproducibility and immutability are overstated |
| D10-I09 | High | Medium | Scale assumptions | Driver volumes and infrastructure capacity lack evidence |
| D10-I10 | High | High | Operational rollout | Servicing, resilience, support, and customer safeguards are missing |
| D10-I11 | Medium | High | References and synthesis | Sources and regulatory positioning overstate readiness |

## Detailed findings

### D10-I01: The critical path is reversed

**Anchor:** “The Strategic Execution Architecture,” “Data Engineering,” “D365 ERP Instantiation,” and “Enhancements to the SPV Financial Model.” The roadmap starts data and ERP work, then revisits the SPV model in a later section.

**Impact:** Product ledgers, receivable eligibility, purchase mechanics, waterfall, reporting, accounting, and data requirements are defined by the transaction. Configuring systems first creates expensive rework and may encode legally invalid flows.

**Canonical resolution:** Phase zero must freeze entity roles, product contracts, financing baseline, asset eligibility, note currency and benchmark, cash waterfall, data rights, accounting perimeter, and decision rights. A working 36-month cohort and waterfall model should be approved before ERP configuration. Technology requirements then derive from those controlled artefacts.

### D10-I02: The stated duration omits major work

**Anchor:** Months 1 to 6 and final synthesis. The plan gives two-month blocks for data, ERP, and reporting but omits licensing, true-sale work, platform negotiation, carrier integration, procurement, security, privacy, independent model validation, tax, audit, backup servicing, user acceptance, and regulatory engagement.

**Impact:** Decision-makers may underfund the programme and make commitments before prerequisites exist. A delay in any external contract or approval can invalidate the whole sequence.

**Canonical resolution:** Treat six to seven months as a pilot target with range and confidence, not a commitment. Build a dependency register with internal and external lead times. Identify the critical path, decision deadlines, contingency, and minimum viable pilot scope. Show separate dates for technical shadow scoring, accounting parallel run, first funded asset, and scale approval.

### D10-I03: Work packages have no governance gates

**Anchor:** Sections 15 through 17. Activities are described, but ownership, approval, entry criteria, exit evidence, risk acceptance, escalation, and rollback are absent.

**Impact:** Completion becomes subjective. A dashboard may be “delivered” even if data lineage, reconciliation, fairness, or security fails. No party can stop unsafe launch.

**Canonical resolution:** Assign responsible, accountable, consulted, and informed roles for every workstream. Add gates: concept approval, legal and data readiness, architecture approval, model validation, integration test, operational readiness, shadow exit, live pilot, and scale. Each gate needs measurable tests, evidence owner, independent reviewer, go or no-go body, exceptions, expiry, and rollback.

### D10-I04: Technology selection is predetermined without fit-gap

**Anchor:** D365 protocol and Azure PaaS execution. The roadmap names exact Azure services and assumes Synapse, Iceberg, MLflow, D365, and Power BI form the final platform. It also implies native D365 banking functions.

**Impact:** Services may not meet regional availability, latency, cost, security, interoperability, or regulated-record requirements. Microsoft “ALM” evidence in the question draft is application lifecycle management, not asset-liability management [16], [17].

**Canonical resolution:** Convert product names to required capabilities in the baseline plan: event ingestion, event-time processing, governed table format, online feature store, model registry, servicing ledger, accounting ERP, evidence vault, reporting, and observability. Run fit-gap, proof of concept, total-cost, security, data-residency, exit, and procurement assessments. Then record approved products in architecture decisions.

### D10-I05: SPV model generation is treated as an automation script

**Anchor:** “Enhancements to the SPV Financial Model.” The plan refers to `generate_spv_model.ps1` and Excel or D365 automation without showing that the script exists or defining the workbook's audit controls.

**Impact:** A generated workbook can contain hardcoded assumptions, broken formulas, unsupported tax, and unvalidated stress while appearing authoritative. PowerShell COM automation is brittle and tied to desktop Excel.

**Canonical resolution:** Specify the model first: 36 monthly periods, three product cohorts, collections, defaults, recoveries, reserves, debt, waterfall, covenants, returns, sensitivities, checks, and sources. Require formula compatibility, no external links, no `@`, controlled inputs, independent review, version hash, and workbook-to-deck reconciliation. Automation may populate or test the workbook but cannot replace review.

### D10-I06: ISO 20022 convergence is not an available endpoint

**Anchor:** “ISO 20022 Convergence and Continuous Control Monitoring.” The roadmap schedules custom CBK messages and model-risk fields without verified regulator schema or channel.

**Impact:** A team may build a non-compliant interface that never connects. `auth.015` and invented tags do not become standard through implementation [13].

**Canonical resolution:** First inventory actual regulatory reports and meet supervisors. Build an internal evidence model independent of transport. Implement adapters only for verified schemas, certification environments, credentials, frequencies, acknowledgements, and error procedures. Treat real-time SupTech as a future option.

### D10-I07: Privacy and data rights are not launch gates

**Anchor:** data engineering and shadow validation. The plan assumes access to telematics, wallet, platform, insurance, and credit data without a contract and privacy workstream.

**Impact:** Development data may be unlawfully processed or impossible to use in production. High-risk monitoring and automated decisions require early necessity, proportionality, retention, rights, processor, and security analysis [10], [11].

**Canonical resolution:** Add data-contract inventory, controller and processor assignments, DPIA, privacy notice, lawful basis, consent where applicable, data minimisation, retention, deletion, cross-border review, data-subject requests, and incident response as Phase zero gates. Use synthetic or de-identified data until rights are approved.

### D10-I08: MLflow does not make artefacts immutable or environments exact

**Anchor:** Azure ecosystem and model lifecycle. The draft uses “immutable” and exact reproducibility based on registry tooling alone.

**Impact:** Tags can change, packages can disappear, base images can drift, data snapshots can be unavailable, and external services can change. A registry records metadata but does not by itself guarantee retention or executable equivalence.

**Canonical resolution:** Pin source commit, data snapshot, feature definitions, environment lock, container digest, random seeds, compiler and hardware-relevant versions, model artifact hash, signature, approvals, and retention. Store signed release bundles in immutable object retention. Run a reproduction test and rollback rehearsal before launch.

### D10-I09: Scale and capacity assumptions are unsupported

**Anchor:** executive architecture and Azure sizing. The plan uses figures such as 1.5 million drivers and large real-time volumes without tying them to contracted platform users, active-hour assumptions, message grain, or pilot scope.

**Impact:** Over-sizing wastes capital; under-sizing harms latency and availability. The D05 row-volume inconsistency propagates into cost and schedule.

**Canonical resolution:** Define pilot, year-one, and stress volumes from contracted or sourced populations. Use active devices, duty cycle, frequency, bytes per event, retention, late-event rate, feature throughput, score requests, journal batches, and report frequency. Benchmark cost and latency at each tier.

### D10-I10: Operational readiness is missing

**Anchor:** rollout and final synthesis. The roadmap does not include backup servicing, customer support, complaint and appeal, reconciliation breaks, data outage fallback, model outage, platform disconnection, key compromise, disaster recovery, cash-account failure, or carrier cancellation.

**Impact:** The system may pass a demo but fail to collect, account, explain, or protect customers during ordinary incidents. A lender will not rely on an untested waterfall and servicer.

**Canonical resolution:** Add operating procedures, support model, service levels, incident severities, business continuity, disaster recovery, backup servicing, manual credit fallback, cash reconciliation, complaint and appeal, adverse action, intervention safety, and tabletop exercises. Define recovery time and recovery point objectives and test them.

### D10-I11: Final regulatory positioning exceeds completed work

**Anchor:** “Final Synthesis and Regulatory Positioning.” The section presents regulatory integration and automated reporting as outcomes even though the roadmap contains no verified approvals, legal opinions, regulator schemas, or validation evidence.

**Impact:** Stakeholders can mistake a target architecture for authorised production status.

**Canonical resolution:** Use maturity labels: concept, designed, built, tested, independently validated, contractually enabled, regulator-notified, approved where required, and live. Provide evidence links for each claim. Cite primary sources from the IEEE index and mark foreign practices as comparative.

## Dependencies, evidence gaps, and remediation sequence

D10 depends on every earlier document. D01 and D03 supply business and financing decisions; D04 supplies products; D05 supplies data; D06 supplies the model; D07 supplies legal and governance requirements; D08 supplies accounting and evidence; D09 supplies pricing and the financial model. Required evidence includes sponsor mandate, budget, RACI, contracts, licences, architecture decisions, DPIA, threat model, model validation plan, financial model, vendor estimates, regulator engagement plan, operations manual, and test environments.

Remediation order is: create Phase zero and governance; establish dependencies and critical path; define capability requirements; build financial and product baselines; add privacy, security, and legal gates; create model and integration gates; design shadow and live pilots; add operational resilience; then publish the schedule with ranges. D10 is complete only when every milestone has evidence and an accountable decision-maker.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D10-I01 | D10-P02, D10-P03 |
| D10-I02 | D10-P02, D10-P10 |
| D10-I03 | D10-P01, D10-P04 |
| D10-I04 | D10-P05 |
| D10-I05 | D10-P03, D10-P08 |
| D10-I06 | D10-P09 |
| D10-I07 | D10-P03, D10-P06 |
| D10-I08 | D10-P07 |
| D10-I09 | D10-P05 |
| D10-I10 | D10-P10 |
| D10-I11 | D10-P04, D10-P11 |
