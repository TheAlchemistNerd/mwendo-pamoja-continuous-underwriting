# D10 Implementation Plan: Implementation Roadmap and Execution

## Objective and planning standard

Rewrite D10 as a gated delivery plan that converts the canonical legal, financial, product, data, model, regulatory, accounting, security, and operating designs into a controlled pilot. Dates should reflect dependencies and uncertainty. A six-to-seven-month target may remain as an aggressive pilot ambition, but it must not imply that external contracts, approvals, or evidence can be scheduled by assertion.

The roadmap should define deliverables, responsible and accountable owners, entry criteria, exit evidence, go or no-go authority, dependencies, risks, budget, rollback, and operational transition. Product names should appear only after capability fit-gap and architecture decisions. Financial model and transaction mechanics must precede ERP configuration.

## Proposed document architecture

1. Programme charter, decision rights, scope, and success measures.
2. Dependency map, critical path, budget, and release strategy.
3. Phase 0: legal, commercial, data, product, and financial foundations.
4. Phase 1: governed data and explicit-feature pilot.
5. Phase 2: model development, validation, and policy design.
6. Phase 3: servicing, accounting, cash, and partner integration.
7. Phase 4: security, privacy, resilience, and operational readiness.
8. Phase 5: shadow scoring and accounting parallel run.
9. Phase 6: bounded live pilot and monitoring.
10. Phase 7: lender and scale decision.
11. Reporting, risk, change, evidence, and references.

## Section-level implementation actions

### D10-P01: Create the programme charter and RACI

**Action:** Replace the opening and strategic architecture.

**Resolves:** D10-I03.

**Content:** State sponsor, programme director, objectives, exclusions, pilot population, products, platforms, geography, budget range, decision bodies, and success metrics. Define workstreams: legal and regulatory; finance and SPV; product and customer; partner and commercial; data and privacy; model and policy; servicing and operations; accounting and ERP; security and resilience; infrastructure; and assurance.

Create a RACI for every workstream and gate. Define change control, dependency owner, risk acceptance, escalation, issue ageing, and meeting cadence. Add evidence-status labels.

**Acceptance tests:** Every deliverable has one accountable owner. No owner approves its own independent validation. Scope and out-of-scope items are explicit.

### D10-P02: Build the dependency map, critical path, and realistic schedule

**Action:** Replace the fixed two-month blocks with a network plan.

**Resolves:** D10-I01 and D10-I02.

**Content:** Identify dependencies among licences, legal entity, receivable transfer, platform and carrier contracts, data rights, product contracts, financial model, servicing, privacy, architecture, procurement, historical data, model validation, integration, accounting, security, regulator engagement, and funding. Give optimistic, base, and conservative durations and identify external lead times.

Define distinct milestones: architecture and term baseline approved; lawful data received; first reproducible feature; model development freeze; independent validation passed; first balanced test journal; first reconciled shadow waterfall; operational readiness passed; first funded pilot asset; first investor report; scale decision.

**Acceptance tests:** Critical path recalculates when a dependency changes. The six-to-seven-month case visibly states assumptions and confidence. No build starts without its minimum entry criteria.

### D10-P03: Add Phase 0 for legal, commercial, data, product, and finance foundations

**Action:** Insert before existing Month 1 work.

**Resolves:** D10-I01, D10-I05, and D10-I07.

**Content:** Deliver approved entity and responsibility map; licence and regulatory issue list; platform, carrier, originator, servicer, data, and account term heads; privacy data inventory and DPIA plan; D04 product states; D03 term sheet; 36-month deterministic SPV workbook; accounting and tax issue lists; target operating model; pilot population; and data-sharing contracts.

The financial model should include product cohorts, collections, defaults, recoveries, reserve, debt, waterfall, covenants, returns, checks, and sources before D365 configuration. Source documents remain controlled; changes go through decisions.

**Gate 0 acceptance:** Sponsor, finance, counsel, data, privacy, product, and risk sign off. Critical red legal or data issues block further use of real personal data or funded assets.

### D10-P04: Define stage gates, evidence, and regulatory maturity labels

**Action:** Add a common gate template and rewrite final synthesis.

**Resolves:** D10-I03 and D10-I11.

**Content:** Every gate should list entry, deliverables, test evidence, unresolved risks, exceptions, expiry, owner, independent reviewer, decision body, and rollback. Use maturity labels: concept, designed, built, internally tested, independently validated, contractually enabled, regulator-notified, approved where required, shadow live, pilot live, and scaled.

Create gates for foundation, architecture, data readiness, model validation, integration, accounting parallel run, security and privacy, operational readiness, shadow exit, live pilot, and scale. Record formal decisions and reservations.

**Acceptance tests:** A claim of “ready” maps to one maturity definition. No sandbox meeting or notification is called approval. Exceptions have owner and expiry.

### D10-P05: Replace predetermined products with capability fit-gap and capacity proof

**Action:** Rewrite D365 and Azure sections.

**Resolves:** D10-I04 and D10-I09.

**Content:** Define required capabilities from D05 and D08: event ingestion, event-time processing, governed table format, feature store, model registry, policy service, servicing ledger, ERP, cash and reconciliation, evidence vault, reporting, observability, security, and recovery. Evaluate products for function, region, integration, data residency, latency, volume, cost, support, lock-in, exit, and control.

Create pilot, year-one, and stress capacity models using active devices, duty cycle, message grain, event bytes, storage, retention, score rate, journals, reports, and concurrency. Run proof of concept before final selection. `generate_spv_model.ps1` and any exact service are listed only if verified and approved.

**Acceptance tests:** Every product has an architecture decision record. Capacity arithmetic reconciles to D05. Cost and performance tests use representative data.

### D10-P06: Make data rights and privacy a delivery workstream

**Action:** Add across Phase 0, data, shadow, and live pilot.

**Resolves:** D10-I07.

**Content:** Deliver controller and processor matrix, lawful basis, contract clauses, privacy notices, consent where needed, minimisation, retention, deletion, cross-border assessment, access, rights response, automated-decision review, DPIA, and incident obligations [10], [11]. Define development, test, shadow, and production datasets and prevent production personal data from entering uncontrolled environments.

Use synthetic or approved de-identified data until rights are complete. Add privacy test cases for opt-out, correction, deletion, restriction, appeal, and partner termination.

**Acceptance tests:** DPIA and contracts are approved before live high-risk processing. Every field has purpose and retention. Data-right loss has a shutdown and deletion plan.

### D10-P07: Build reproducible model and release engineering

**Action:** Rewrite MLflow and Azure model-lifecycle claims.

**Resolves:** D10-I08.

**Content:** Record source commit, data snapshot, feature set, schema, preprocessing, environment lock, container digest, random seeds, posterior artifact, model signature, policy version, validation report, fairness report, approval, deployment, and rollback. Store signed release bundles under immutable retention. Treat model registry metadata as one component, not proof of immutability.

Create development, validation, staging, shadow, and production separation. Define promotion, segregation of duties, emergency rollback, stale-artifact fallback, and reproduction test.

**Acceptance tests:** A second environment reproduces approved outputs within tolerance. An unauthorised tag change cannot promote a model. Rollback and restoration pass.

### D10-P08: Implement and independently validate the SPV model before automation

**Action:** Rewrite “Enhancements to the SPV Financial Model.”

**Resolves:** D10-I05.

**Content:** Build the model from D03 and D09 with 36 monthly periods, IPF, microloan and revolver cohorts, origination, collection, default, recovery, prepayment, reserve, debt, waterfall, covenants, returns, sensitivities, HoldCo overlay, checks, and sources. Inputs must show source status and as-of date. Avoid external links, `@`, structured references, volatile formulas, and hidden hardcodes.

Test stack, cash, debt, reserve, OC, triggers, distributions, base and stress cases, and reverse stress. Have an independent modeller review formulas and assumptions. Automation may generate or populate only after the controlled workbook passes. Tie presentation outputs to named ranges.

**Acceptance tests:** Workbook passes all acceptance criteria from the project plan. Every number in D01 and D03 ties to it. Severe-case statements are calculated, not promised.

### D10-P09: Replace ISO convergence with verified reporting discovery and adapters

**Action:** Rewrite Section 16.5.2.

**Resolves:** D10-I06.

**Content:** Start with D07's reporting inventory and regulator engagement. Define internal canonical evidence and report schemas independent of transport. For each verified recipient, build mapping, validation, signer, transport, acknowledgement, error, and correction. Use ISO 20022 only under a valid message and implementation guide [13]; use XBRL only with an applicable taxonomy.

Treat real-time SupTech as a future option. Remove invented fields and `auth.015` claims unless an authority approves them. Schedule certification only after specifications and credentials exist.

**Acceptance tests:** Every production adapter has authoritative schema, test environment, and acknowledgement. A transport change does not alter internal accounting facts.

### D10-P10: Add shadow, live pilot, operations, resilience, and scale gates

**Action:** Replace simple Power BI shadow validation and extend the timeline.

**Resolves:** D10-I02 and D10-I10.

**Content:** Shadow mode should run source ingestion, features, scores, policy proposals, servicing simulations, accruals, journals, cash reconciliation, borrowing base, waterfall, investor reports, alerts, privacy, fairness, and incident response without changing customer credit. Define minimum mature outcomes and comparison to current decisions.

Operational readiness includes staffing, support, complaints and appeal, manual fallback, model outage, data outage, platform disconnect, carrier interruption, collection failure, account-bank failure, key compromise, disaster recovery, backup servicing, incident communication, and reconciliation breaks. Define RTO, RPO, SLAs, runbooks, on-call, training, and tabletop exercises.

Live pilot should use bounded customers, exposure, products, platform, geography, and duration. Define stop-loss, daily monitoring, independent oversight, customer safeguards, and rollback. Scale only after performance, calibration, fairness, cash, accounting, security, and operations pass.

**Acceptance tests:** Shadow exit criteria are quantitative. A live-pilot stop can freeze new exposure without losing servicing. Operations pass end-to-end and failure exercises.

### D10-P11: Rebuild programme reporting, risk, benefits, and references

**Action:** Replace final synthesis and references.

**Resolves:** D10-I11 and closes all findings.

**Content:** Create weekly delivery dashboard, monthly steering pack, risk and dependency register, decision log, budget and forecast, benefits register, change log, and evidence index. Benefits should include portfolio, customer, partner, operating, compliance, and investor metrics with baseline, target, owner, and method. Distinguish leading delivery measures from mature credit outcomes.

Use the global IEEE index and cite primary sources. State as-of dates. Remove long dashes, corrupted punctuation, unsupported capacity and approval claims, and exact product promises lacking decisions.

**Acceptance tests:** Status is supported by evidence links. Benefits cannot be claimed before measurement window matures. Risks have quantified exposure, owner, mitigation, and contingency.

## Detailed phase deliverables

**Phase 0, foundations:** approved D01 to D04 baselines, legal and licence assessment, partner heads, data rights, DPIA plan, financial model, target operating model, pilot scope, budget, and architecture requirements.

**Phase 1, data and explicit path:** source contracts, event schemas, clock dictionary, Bronze and Silver flows, feature registry, Explicit Liquidity Feature Path, online-offline parity, reconciliation, privacy controls, and capacity evidence.

**Phase 2, model and policy:** explicit-only benchmark, neural experiments, HBLR, offline inference, online scoring artifact, validation, fairness, policy rules, reasons, monitoring, and rollback.

**Phase 3, product and finance integration:** servicing states, carrier and platform flows, D365 staging, journals, bank cash, reserve, borrowing base, waterfall, reports, and close simulation.

**Phase 4, assurance:** threat testing, privacy test, disaster recovery, model validation closure, user acceptance, backup servicing, operations training, and control evidence.

**Phase 5, shadow:** end-to-end parallel decisions and accounting for a defined period with no customer action.

**Phase 6, live pilot:** bounded funding and customer exposure under daily governance and stop conditions.

**Phase 7, scale:** lender, carrier, platform, sponsor, risk, finance, legal, privacy, and operations decision based on mature evidence.

## Recommended editing order and reviewers

Perform P01 through P04 first. Complete the capability and privacy work before build commitments. Complete the deterministic financial model before ERP configuration. Build release engineering and independent validation in parallel with model development, not afterward. Design shadow and operations before live integration. Add reporting and benefits throughout.

Required reviewers include executive sponsor, programme director, PMO, transaction and regulatory counsel, CFO and financial modeller, product, partner leads, data architect, DPO, model owner and independent validator, security and SRE, servicing and operations, D365 and infrastructure architects, auditor, internal audit, lender, carrier, platform, trustee, and customer-support lead.

## Pre-publication validation checklist

- Charter, scope, RACI, budget, and decision rights exist.
- Dependencies and critical path include external parties.
- Phase 0 precedes technology build.
- Financial model precedes ERP design.
- Technology products follow fit-gap decisions.
- Privacy and data rights are gates.
- Release artifacts are reproducible.
- Regulator interfaces are verified.
- Shadow and live pilot have measurable exits and stops.
- Operations, backup servicing, and recovery are tested.
- Status and benefits use evidence and maturity labels.

## Work breakdown and deliverable register

Create a deliverable register beneath the phase plan. Each row should have stable ID, workstream, deliverable, description, accountable owner, responsible team, dependency, planned start and finish, effort, cash budget, external party, acceptance test, evidence link, status, risk, and decision gate. Summary dates should be calculated from this register rather than manually typed into narrative.

For legal and commercial work, include entity documents, licences, legal opinions, carrier and platform agreements, receivable sale, servicing, account control, data processing, and investor documents. For finance, include D03, workbook, tax, accounting, treasury, bank accounts, hedge decision, and investor reporting. For data and model, include contracts, schemas, clocks, feature registry, benchmark, development, validation, fairness, monitoring, and policy. For operations, include servicing, customer communication, complaints, training, support, business continuity, and backup servicing.

Define dependency types and lead or lag. A draft platform agreement may permit synthetic integration design but not production wallet access. A preliminary tax view may permit scenarios but not investor disclosure. A model-development dataset may be available before a live decision lawful basis. These partial states should have bounded permissions.

## Budget, resources, and procurement controls

Build a monthly budget for people, advisers, licences, cloud, devices, data, integration, model validation, audit, legal, tax, security testing, insurance, servicing, backup servicing, travel, customer research, contingency, and transaction costs. Reconcile to the USD 1 million HoldCo overlay and identify sponsor-funded or SPV-eligible costs. Do not charge SPV investors for HoldCo development without a permitted agreement and budget.

Create a named capacity plan for product, finance, legal, data, ML, platform, security, D365, servicing, operations, support, validation, and PMO. Identify scarce roles and external procurement lead times. Require statements of work with deliverables, acceptance, IP, data, security, exit, support, and pricing. Track committed, actual, forecast, and contingency.

Procurement gates should require fit-gap, architecture, security, privacy, legal, finance, references, total cost, data export, termination, and business continuity review. A successful demonstration does not establish operating support or exit. Avoid dependence on a single consultant for critical model, servicing, ERP, or key-management knowledge.

## Benefits measurement and pilot learning design

Define baselines and measurement for approval access, price, default, loss, collection, insurance continuity, driver downtime, net cash, intervention uptake, complaints, fairness, processing latency, reconciliation, close time, and operating cost. Separate model prediction quality from causal intervention effect and from portfolio economics. Set observation maturity before claiming benefit.

Use a controlled pilot design with eligibility rules, comparison group where ethical and feasible, exposure cap, random or staged intervention assignment, pre-specified outcomes, analysis plan, and stopping rules. Record deviations. Ensure customer support and appeal exist regardless of study arm. Independent risk and customer-protection reviewers should monitor adverse outcomes.

At scale gate, report achieved, not projected, operational controls; mature and immature credit outcomes; financial model updates; unresolved legal and partner conditions; incidents; customer outcomes; and sensitivity. The steering committee should be able to choose scale, extend, narrow, remediate, or stop based on evidence.

## Definition of done

D10 is complete when the programme can show what will be delivered, by whom, in what order, under which authority, with what evidence, at what cost, and with which stop and rollback conditions. A schedule is credible only when legal, data, financial, model, accounting, security, partner, and operational dependencies are visible and govern the release decision.
