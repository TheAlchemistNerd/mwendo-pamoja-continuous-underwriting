---
title: "Implementation Documentation: Implementation Roadmap, Validation, and Controlled Scale"
author: "Nevil Maloba"
date: "24 August 2026"
status: "Execution baseline for sponsor, lender, insurer, platform, servicer, and investor approval"
---

# Programme Objective

The implementation objective is to prove that Mwendo Pamoja can improve driver cash-flow resilience and produce a transparent, controllable receivables portfolio without creating unacceptable customer, legal, accounting, model, operational, or investor risk.

The technical evidence gates for observation units, P-splines, Pólya-Gamma inference, survival timing, complete loss components, posterior artifacts, ECL, and SPV reconciliation are defined in `CREDIT_RISK_MODEL_AND_LOSS_ARCHITECTURE_SPECIFICATION.md` and must be represented in the phase acceptance packs below.

The roadmap does not assume that a complete institutional platform can be delivered safely in six months. A bounded shadow and live pilot can be achieved earlier if data rights, product contracts, financial modelling, controls, and independent validation are ready. Full scale follows only after measured evidence.

The programme is organised around decision gates, not software activity. A phase finishes when its evidence is accepted by accountable owners, not when a development team reports that code is complete.

# Scope and Success Definition

The initial scope covers:

- one approved Kenyan legal and licensing model;
- one lead lender;
- one licensed insurer;
- one or two mobility or delivery platforms;
- three product families: insurance-premium finance, microloan, and revolving credit;
- the Explicit Liquidity Feature Path and a bounded neural representation;
- redundancy-controlled Hierarchical Bayesian Logistic Regression;
- the separate Credit Policy and Compliance Gate;
- contract-level servicing and collection;
- a USD-equivalent 9 million SPV design in KES operating currency;
- an optional USD 1 million HoldCo funding overlay;
- controlled accounting into the selected general ledger;
- a lender and investor reporting package; and
- a measured shadow and live pilot.

Success is not defined as model accuracy alone. It requires:

- safer and more understandable customer outcomes;
- reliable product and cash-flow operations;
- calibrated and stable risk estimates;
- legal and accounting sign-off;
- reproducible decisions;
- complete and timely reconciliation;
- scenario-tested lender protection;
- evidence of incremental benefit compared with simpler policy and explicit-feature baselines; and
- an economics case that remains viable after losses, servicing, technology, compliance, tax, liquidity, and funding costs.

# Programme Governance

## Decision bodies

| Body | Core remit | Minimum membership |
|---|---|---|
| Executive Steering Committee | Scope, budget, counterparties, risk acceptance, and gate approval | Sponsor, lender, insurer, platform, finance, risk |
| Product and Customer Committee | Product terms, affordability, disclosures, interventions, complaints | Product, compliance, legal, servicing, customer representative |
| Model Risk Committee | Model purpose, validation, limitations, monitoring, fallback, change | Model owner, independent validation, credit risk, compliance |
| Data and Privacy Council | Data rights, lawful purpose, minimisation, retention, security | Privacy, security, data owners, legal, architecture |
| SPV and Finance Committee | Capital stack, legal structure, model, waterfall, accounting, investor reports | Treasury, accounting, tax, legal, arranger, trustee adviser |
| Change Advisory Board | Release risk, dependencies, rollback, operational readiness | Technology, operations, security, model, vendor owners |

## RACI

The detailed RACI must assign one accountable owner per deliverable. The following is the baseline.

| Deliverable | Accountable | Responsible | Consulted |
|---|---|---|---|
| Licensing and activity-perimeter opinion | General Counsel | Kenyan external counsel | Lender, insurer, platform |
| Product contracts and disclosures | Product Executive | Legal and product teams | Compliance, servicing, customer research |
| Data-protection impact assessment | Data Protection Officer | Privacy and data teams | Legal, security, counterparties |
| Event and data contracts | Chief Data Officer | Data engineering | Platform, wallet, carrier, model, servicing |
| HLR and feature specification | Chief Risk Officer | Model development | Credit, product, data science |
| Independent model validation | Model Risk Head | Independent validation | Audit, compliance |
| SPV financial model | Chief Financial Officer | Project finance team | Arranger, lender, tax, accounting |
| Term sheet and transaction documents | Transaction Sponsor | Counsel and arranger | Trustee, lender, insurer, servicer |
| Servicing and accounting design | Chief Operating Officer | Operations and finance systems | Accounting, audit, technology |
| Cybersecurity and resilience | Chief Information Security Officer | Security and infrastructure | Vendors, privacy, operations |
| Pilot operations | Chief Operating Officer | Product, servicing, customer support | Risk, insurer, platform |
| Scale decision | Executive Steering Committee | Programme Director | All control owners |

No vendor is accountable for a regulated institution's statutory duty merely because it operates a system.

# Delivery Principles

1. **Contract before automation:** Product, data, servicing, and waterfall rules must be defined before code hardens them.
2. **Point-in-time evidence:** Every score, decision, journal, and investor calculation must be reproducible.
3. **Simple baseline first:** Explicit-only and policy-only baselines are built before the neural extension.
4. **One feature owner:** CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and explicit interactions remain in the Explicit Liquidity Feature Path.
5. **Independent challenge:** Model, legal, accounting, tax, security, and financial assumptions are reviewed outside their originating teams.
6. **Controlled reversibility:** Every release has a fallback, rollback, exposure limit, and owner.
7. **No unsupported interface:** Regulatory and payment adapters use confirmed schemas and channels.
8. **Measured benefit:** Scale depends on causal or quasi-experimental evidence, not dashboard correlation.

# Dependency and Critical Path

The critical path is:

~~~text
Counterparty intent
        |
Legal and licence perimeter
        |
Product, data-rights, and payment contracts
        |
Historical data access and quality proof
        |
Outcome definitions and financial baseline
        |
Feature, HLR, policy, servicing, and SPV model validation
        |
Controlled integration and reconciliation
        |
Shadow operation
        |
Bounded live pilot
        |
Independent outcome and economics review
        |
Scale, redesign, or stop decision
~~~

Technology procurement may proceed in parallel only where it does not presume an unresolved legal, product, or data decision.

# Indicative Timeline

The working timeline is 15 months to a defensible scale decision. It is a planning baseline, not a commitment.

| Phase | Indicative months | Outcome |
|---|---|---|
| Phase 0: Mobilisation and evidence room | 0 to 1 | Charter, RACI, source register, decisions, risks |
| Phase 1: Legal, commercial, product, and data foundations | 1 to 3 | Approved perimeter and executable pilot design |
| Phase 2: Data proof, financial baseline, and simple controls | 2 to 5 | Reliable data, cohort model, explicit baseline |
| Phase 3: Model, SPV, systems, and control build | 4 to 8 | Validated components and reconciled integration |
| Phase 4: End-to-end testing and shadow operation | 8 to 10 | Production-like evidence without automated customer impact |
| Phase 5: Bounded live pilot | 10 to 12 | Limited exposure and measured customer outcomes |
| Phase 6: Observation, validation, and transaction readiness | 12 to 15 | Mature outcome evidence and investment decision |
| Phase 7: Controlled scale | After gate approval | Tranche, platform, product, and geography expansion |

Overlaps depend on gate conditions. A blocked dependency changes the dates and the exposure plan; it is not concealed by relabelling incomplete work as “agile.”

# Phase 0: Mobilisation and Evidence Room

## Deliverables

- signed programme charter;
- scope, exclusions, and decision rights;
- counterparties and legal entities;
- initial RACI and committee calendar;
- controlled document and source register;
- assumption and decision log;
- risk, issue, dependency, and change registers;
- baseline architecture and terminology;
- secure diligence room;
- benefit hypotheses and measurement protocol; and
- initial budget and capacity plan.

The canonical terminology is frozen:

- Explicit Liquidity Feature Path;
- Explicit Liquidity Features;
- Hierarchical Bayesian Logistic Regression;
- Credit Policy and Compliance Gate;
- real-world probability \(PD_{\mathbb P}\);
- optional risk-neutral probability \(PD_{\mathbb Q}\);
- \(K_{\mathrm{RBCP}}\) for the customer pricing premium;
- \(K_{\mathrm{cap}}\) for regulatory capital; and
- \(m_A\) and \(m_B\) for SPV note margins.

## Gate G0: mobilisation accepted

Evidence:

- named accountable owners;
- agreed target outcomes;
- funding for the next phase;
- secure information-sharing process;
- no unresolved contradiction about primary SPV size or legal entities; and
- approved rule that source-backed, illustrative, and proposed claims remain distinguishable.

# Phase 1: Legal, Commercial, Product, and Data Foundations

## Legal and licensing

Kenyan counsel produces an activity-perimeter analysis covering lending, digital credit, insurance, intermediation, payments, credit reporting, data protection, AML, outsourcing, SPV issuance, security, tax, and consumer protection. Comparative Basel, Solvency II, EBA, or foreign fair-lending material is labelled as comparative.

## Product definition

For each product, define:

- provider and legal creditor;
- eligibility and exclusions;
- principal, price, fees, term, and repayment order;
- KESONIA reset and fallback where applicable;
- affordability and customer-sufficiency controls;
- insurance coverage and cancellation mechanics;
- draw, freeze, cure, modification, and exit;
- collection mandate and failure;
- credit-reference treatment;
- complaints, correction, and human review;
- assistance and forbearance classification; and
- transferability to the SPV.

## Data rights and privacy

Complete data maps and contract schedules for platform, wallet, lender, insurer, payment, servicing, and model data. The data-protection impact assessment specifies lawful purpose, necessity, controller and processor roles, sensitive inferences, retention, cross-border transfer, automated-decision safeguards, and rights handling.

No data is considered “available” until its owner, licence, purpose, field meaning, history, quality, update frequency, and termination rights are documented.

## Gate G1: lawful and executable pilot

Evidence:

- legal opinion and licence responsibility;
- draft executable product terms;
- counterparty heads of terms;
- approved privacy assessment;
- data-sharing and payment-rights path;
- customer disclosure and review concept;
- preliminary accounting and tax position; and
- no critical unresolved legal or customer-protection issue.

# Phase 2: Data Proof, Financial Baseline, and Simple Controls

## Data proof

Acquire representative historical extracts. Reconcile source counts, timestamps, identifiers, currency, wallet settlements, trip earnings, repayments, insurance status, defaults, cures, write-offs, and recoveries.

Build the point-in-time event contract and clock dictionary from Part 2a. Demonstrate:

- event-time and availability-time correctness;
- late-data handling;
- duplicate prevention;
- history and correction preservation;
- consent and purpose filtering;
- deletion propagation; and
- training data that cannot see future information.

## Outcome and cohort definitions

Credit, accounting, collections, and model teams approve common definitions for default, arrears, cure, write-off, recovery, intervention, forbearance, exposure, and horizon. If multiple definitions are required, they receive different names and mappings.

## Deterministic SPV model

Build the 36-month product-cohort model before enterprise automation. It includes:

- originations and eligibility;
- scheduled and actual collections;
- defaults, cures, recoveries, and lags;
- KESONIA-linked asset and note cash flows;
- Class A, B, and C schedules;
- advance rate and OC;
- cash reserve account;
- waterfall and early amortisation;
- base, mild, severe, and user cases;
- sensitivity and assumption register;
- tax, fee, cost, and FX status; and
- balance and cash checks.

## Simple decision baselines

Implement:

1. approved hard policy without a statistical model;
2. an interpretable explicit-feature logistic or Bayesian baseline; and
3. conservative missing-data and outage fallback.

These establish the minimum benchmark the neural extension must beat.

## Gate G2: evidence-quality baseline

Evidence:

- historical data-quality report;
- approved outcomes and horizons;
- point-in-time leakage tests;
- reconciled deterministic SPV model;
- executed assumptions and diligence gaps;
- baseline model validation; and
- quantified feasibility of expected pilot volume.

# Phase 3: Model, SPV, Systems, and Control Build

## Feature and model build

Build the neural branch and Explicit Liquidity Feature Path with one engineered owner per feature. The HLR implementation must include:

- robust centring and semantic duplicate removal;
- orthogonalised spline design;
- cross-fitted ridge residualisation of neural embeddings against the explicit design;
- centred hierarchical effects;
- grouped shrinkage;
- strong interaction heredity;
- posterior predictive and convergence checks;
- out-of-time calibration;
- platform, geography, product, and subgroup stability tests;
- explicit-only fallback; and
- documented rejection if the neural residual lacks stable incremental value.

The copula module remains a portfolio stress component, not an individual approval model.

## Financial and legal structuring

Advance the term sheet, true-sale and security analysis, tax position, accounts, servicing agreement, eligibility criteria, reserve, waterfall, triggers, investor reporting, and backup servicing. Financing documents must follow the validated model, while the model must reflect the negotiated documents. Differences are resolved through a controlled term-to-model reconciliation.

## Capability-led systems build

Complete the fit-gap before contracting major platforms. Build or integrate:

- secure event ingestion and immutable landing;
- stream processing and lakehouse;
- online feature service;
- model registry and scoring;
- policy decision service;
- servicing and receivables subledger;
- bank and reserve interfaces;
- journal staging and D365 general-ledger posting;
- SPV waterfall and reporting;
- monitoring and evidence vault; and
- confirmed external reporting adapters.

## Gate G3: component validation

Evidence:

- independent HLR validation and approved limitations;
- security and privacy design approval;
- product and policy rule sign-off;
- SPV model independent review;
- capability fit-gap and vendor capacity proof;
- interface contracts and reconciliation design;
- test data and environments;
- operational procedures and training plan; and
- approved remaining risks.

# Phase 4: End-to-End Testing and Shadow Operation

## Test levels

- unit tests for formulas, rules, features, and mappings;
- contract tests for each API and event schema;
- point-in-time and replay tests;
- model implementation parity;
- journal and waterfall golden cases;
- performance, soak, and capacity tests;
- privacy and access tests;
- penetration and dependency tests;
- recovery, failover, and backup restore;
- customer communication and complaint simulations;
- accounting close and investor-report dry runs; and
- incident exercises.

## Shadow mode

Shadow mode processes live or production-representative data but does not allow the new model to make an unreviewed customer decision. Compare:

- data coverage and latency;
- baseline and HLR predictions;
- calibration and uncertainty;
- policy actions and human decisions;
- customer reason quality;
- servicing effects;
- accounting entries;
- borrowing base, reserve, and waterfall;
- subgroup outcomes;
- exceptions and overrides; and
- support workload.

Shadow mode continues long enough to observe meaningful outcomes for the product horizons. Short-lag operational metrics cannot substitute for default and recovery maturity.

## Gate G4: production readiness

Evidence:

- no critical security, privacy, accounting, or reconciliation defect;
- model performance meets pre-agreed floors;
- neural residual demonstrates stable incremental value or is excluded;
- policy outcomes are within risk appetite;
- fairness and customer-rights controls operate;
- explicit-only and manual fallbacks pass;
- close and investor reports reconcile;
- service desk and incident response are staffed;
- pilot exposure limits are approved; and
- change and rollback plans are signed.

# Phase 5: Bounded Live Pilot

## Pilot limits

The live pilot is constrained by:

- maximum number of customers;
- maximum aggregate exposure;
- product and ticket-size limits;
- platform and geography limits;
- daily and monthly origination caps;
- minimum data-quality coverage;
- permitted automated actions;
- manual-review bands;
- reserve and loss stop levels;
- complaint and adverse-outcome thresholds; and
- immediate pause authority.

The severe-contagion scenario is not evidence that the pilot is safe. It is one input to the exposure and stop limits.

## Experimental design

Where lawful and ethical, use randomised or phased rollout for supportive interventions. Otherwise use a pre-specified quasi-experimental design with matching, difference-in-differences, regression discontinuity, or another appropriate method.

Measure:

- default, arrears, cure, and recovery;
- insurance continuity;
- net driver earnings and cash sufficiency;
- work and rest patterns where ethically justified;
- approval, price, limit, and adverse-action distribution;
- complaints, appeals, corrections, and overturns;
- intervention acceptance and completion;
- platform and geography heterogeneity;
- unit economics;
- serving and reconciliation reliability; and
- unintended displacement or exclusion.

The analysis distinguishes predictive performance from causal intervention effect.

## Gate G5: pilot continuation

Weekly operational and monthly governance reviews can continue, pause, narrow, or stop the pilot. A critical customer, privacy, fraud, accounting, liquidity, or model incident triggers the predefined incident process.

# Phase 6: Observation, Validation, and Transaction Readiness

Allow outcomes to mature. Independent validation reviews:

- discrimination and calibration over product horizons;
- posterior uncertainty and coverage;
- coefficient and feature stability;
- multicollinearity diagnostics and ablations;
- neural residual incremental value;
- subgroup and platform performance;
- selection, intervention, and reject bias;
- copula and stress plausibility;
- realised versus modelled loss and recovery;
- reserve, OC, DSCR, and waterfall behaviour; and
- customer and operational outcomes.

Finance replaces illustrative assumptions with portfolio tape, executed contracts, vendor quotations, tax advice, hedge indications, and audited or reconciled costs.

Transaction readiness also requires:

- final legal structure and true-sale opinion;
- security-perfection plan;
- executed or agreed-form servicing and data arrangements;
- backup servicing;
- bank and trust accounts;
- final eligibility and waterfall;
- investor diligence package;
- accounting papers;
- final model and source audit; and
- conditions-precedent register.

## Gate G6: scale, redesign, or stop

The Steering Committee chooses one of three outcomes:

- scale within approved limits;
- redesign and repeat a bounded pilot; or
- stop and execute an orderly customer, data, and financial wind-down.

A scale decision requires measured benefit, acceptable harm, operational stability, and financeable economics. Sunk cost is not a criterion.

# Phase 7: Controlled Scale

Scale is by tranche. Only one material dimension changes at a time where practical:

- customer count;
- platform;
- geography;
- product;
- limit;
- automation authority;
- funding class; or
- data source.

Each expansion has preconditions, exposure cap, monitoring, rollback, and observation period. Models are not assumed portable to a new platform or geography without evidence.

# Model and Release Engineering

Every production release is built from version-controlled:

- source code;
- environment and dependency lock;
- data and feature contracts;
- training and validation configuration;
- immutable input manifest;
- model artefact and checksum;
- calibration parameters;
- policy rule package;
- schema migrations;
- infrastructure definition;
- test evidence; and
- approval record.

Promotion moves the same signed artefact through environments. Production is not rebuilt from an analyst notebook.

The release gate checks:

- training-serving parity;
- point-in-time leakage;
- feature ownership;
- HLR rank and condition diagnostics;
- posterior convergence and predictive checks;
- calibration;
- fairness and customer impact;
- security;
- performance;
- fallback;
- journal and reporting effects; and
- rollback.

Emergency changes expire automatically unless ratified through normal governance.

# HLR Multicollinearity and Redundancy Acceptance

Because the explicit and neural branches can observe related raw wallet information, the following tests are mandatory:

1. no named Explicit Liquidity Feature is engineered in the neural input;
2. duplicate and formula-equivalent explicit columns are removed;
3. spline blocks are centred and QR-orthogonalised;
4. neural embeddings are residualised out of fold against the explicit design using ridge projection without outcome labels;
5. interactions obey strong heredity and use centred parents;
6. group shrinkage controls whole blocks rather than allowing unstable coefficient substitution;
7. hierarchical effects are centred or constrained;
8. condition indices, singular values, VIF, posterior correlation, coefficient stability, and ablation results are reviewed;
9. incremental neural value persists out of time and across material segments; and
10. the explicit-only fallback remains calibrated and operational.

There is no universal VIF or condition-number value that alone accepts the model. Thresholds are documented before validation, interpreted with sample size and design, and supplemented by stability and predictive evidence.

# Verified Reporting Discovery

Before building a regulator, bureau, payment, insurer, or investor interface:

1. identify the legal or contractual obligation;
2. obtain the current schema, taxonomy, calendar, and channel;
3. identify reporting entity and signatory;
4. map each field to an authoritative source;
5. validate sample files with the recipient where possible;
6. design acknowledgement, rejection, correction, and resubmission;
7. retain the submission and receipt evidence; and
8. assign change ownership.

ISO 20022 applies only to supported payment messages. XBRL applies only to an issued taxonomy. No speculative CBK SupTech API or invented field is included in the critical path.

# Operations and Resilience

The operating model includes:

- customer support and complaints;
- credit review and override;
- intervention operations;
- collections and hardship;
- insurance coverage and cancellation exception;
- wallet and bank reconciliation;
- data-quality operations;
- model monitoring;
- security operations;
- servicing and accounting close;
- trustee and investor reporting;
- vendor management; and
- incident command.

Runbooks define triggers, roles, access, communication, evidence, fallback, recovery, and post-incident review. Exercises include data corruption, model outage, mass decision error, duplicate collection, insurer mismatch, servicing failure, bank delay, cyber incident, reserve shortfall, and early amortisation.

# Programme Reporting

The Programme Director reports:

- milestone status against accepted evidence;
- decisions due and decision ageing;
- critical-path movement;
- budget actual, commitment, forecast, and contingency;
- resource capacity and key-person risk;
- counterparty deliverables;
- risks, issues, assumptions, and dependencies;
- test and defect status;
- customer and control incidents;
- benefits and harms;
- model and data health; and
- SPV model and transaction readiness.

Status is evidence-based. A deliverable cannot be green when a required approver has not accepted it.

# Budget, Resources, and Procurement

The budget is built bottom-up by work package:

- legal, regulatory, tax, and accounting advice;
- customer and product research;
- data acquisition and platform integration;
- cloud, streaming, lakehouse, and online serving;
- model development and independent validation;
- servicing and accounting systems;
- security, privacy, audit, and penetration testing;
- SPV structuring, trustee, banking, and arranger work;
- pilot capital, reserves, expected losses, and customer remediation;
- operations, support, training, and change;
- licences and vendors;
- contingency; and
- controlled scale.

Each line has quantity, rate, duration, currency, tax status, owner, quote status, commitment, and confidence. Procurement evaluates capability, portability, security, service, evidence access, data exit, subcontractors, implementation capacity, and total cost. A vendor roadmap is not accepted as current functionality without a tested commitment.

# Benefits and Learning

The benefits register links each claim to a metric, baseline, target range, observation window, data source, analytic method, owner, and decision use.

Benefits include:

- reduced multi-product default and arrears;
- faster cure and improved recovery;
- fewer avoidable insurance lapses;
- greater driver cash-flow sufficiency;
- lower loss and servicing cost;
- more stable asset cash yield;
- reduced reconciliation breaks;
- faster controlled close and reporting;
- improved explanation and dispute resolution; and
- financeable SPV performance.

Potential harms include:

- exclusion or unfair pricing;
- excessive surveillance;
- unsafe work incentives;
- debt escalation;
- hidden forbearance;
- insurance coverage gaps;
- collection errors;
- privacy or security incidents;
- model overconfidence; and
- concentration or liquidity stress.

The scale case reports benefits and harms together.

# Final Acceptance Criteria

The programme is ready for controlled scale only when:

- legal entities, licences, and accountable decisions are approved;
- product, data, payment, servicing, and insurance contracts are executable;
- historical data is representative enough for stated use;
- point-in-time correctness and feature ownership are proven;
- the HLR passes redundancy, multicollinearity, calibration, stability, and fairness review;
- the neural residual adds stable out-of-time value or is excluded;
- the policy gate, manual review, and fallback work;
- the deterministic SPV model and Monte Carlo extension are independently reviewed;
- capital stack, OC, reserve, waterfall, and KESONIA conventions match finance documents;
- tax, fees, costs, FX, and hedging are evidence-labelled;
- servicing, cash, collateral, GL, and investor reports reconcile;
- privacy, security, recovery, and incident tests pass;
- the bounded pilot shows acceptable customer outcomes and unit economics;
- reporting adapters use verified obligations and schemas;
- remaining risks have named owners and approved appetite; and
- the Steering Committee records a reasoned scale decision.

# References

1. Central Bank of Kenya, “Revised Risk-Based Credit Pricing Model,” Aug. 2025. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf
2. Kenya Law, “Data Protection Act, 2019,” current consolidated text. Available: https://new.kenyalaw.org/akn/ke/act/2019/24
3. IFRS Foundation, “IFRS 9 Financial Instruments.” Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
4. Basel Committee on Banking Supervision, “The Basel Framework.” Available: https://www.bis.org/baselframework/
5. Microsoft, “Dynamics 365 implementation guidance.” Available: https://learn.microsoft.com/dynamics365/guidance/
6. Apache Flink, “Documentation.” Available: https://nightlies.apache.org/flink/flink-docs-stable/
7. Apache Iceberg, “Documentation.” Available: https://iceberg.apache.org/docs/latest/
