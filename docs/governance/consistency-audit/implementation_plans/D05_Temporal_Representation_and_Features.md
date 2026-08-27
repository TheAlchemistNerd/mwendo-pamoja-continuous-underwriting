# D05 Implementation Plan: Temporal Representation and Features

## Objective and engineering contract

Rewrite D05 as a testable data and feature architecture specification. The revised document should define source events, clocks, schemas, volumes, stream processing, lakehouse zones, point-in-time correctness, feature ownership, neural tensor interfaces, missing-data behaviour, privacy controls, replay, and online-offline parity. It must serve both model developers and production engineers without relying on ambiguous product names or mathematically decorative components.

The revised design uses raw telematics and wallet events, Flink feature services, a neural sequence branch, the Explicit Liquidity Feature Path, hierarchical Bayesian underwriting, and a downstream Credit Policy and Compliance Gate. D05 ends at the versioned model-input interface and operational feature quality. D06 owns statistical inference. D07 owns compliance and policy authority. D08 owns accounting and external evidence posting.

## Proposed document architecture

1. Scope, non-functional requirements, terms, and source authority.
2. Edge devices, event contracts, sampling, volume, and privacy.
3. Time semantics and point-in-time correctness.
4. Ingestion, CDC, Kafka, Flink, and replay.
5. Lakehouse format, medallion zones, lineage, and retention.
6. Feature registry and Explicit Liquidity Feature Path.
7. Neural sequence preparation and context tokens.
8. Fusion design and HBLR interface.
9. Missingness, uncertainty, data quality, and fallbacks.
10. Security, privacy, observability, recovery, and cost.
11. Test strategy, acceptance criteria, and references.

## Section-level implementation actions

### D05-P01: Add a terminology, symbol, and formula control section

**Action:** Add before the current introduction and audit all equations.

**Resolves:** D05-I11.

**Content:** Define event, feature, label, observation window, outcome window, event time, source commit, ingestion, availability, business effective date, accounting date, decision time, watermark, lateness, correction, replay, snapshot, table format, medallion, Kappa, neural embedding, and explicit feature. Add tensor and feature symbol tables with dimensions and units.

Re-key GRU, attention, spline, normalisation, and as-of formulas from authoritative references or executable implementations. Use ASCII minus where conversion risk exists. For every equation include a numerical or tensor-shape test. Mark illustrative architecture choices separately from current implementation.

**Acceptance tests:** Equations render in Markdown, executable reference tests pass, and no symbol changes meaning. “Delta” cannot refer simultaneously to a table product, architecture, and numeric difference without qualification.

### D05-P02: Redesign edge capture around an event and capacity contract

**Action:** Rewrite “Edge Capture: Hardware Layer and Raw Data Format.”

**Resolves:** D05-I06 and D05-I10.

**Content:** Define device classes, firmware, source clock, synchronisation, sampling frequency, batch size, message encoding, sensor units, coordinate system, calibration, quality flag, device ID rotation, driver and vehicle binding, and offline buffer. Distinguish raw IMU samples, GNSS observations, OBD events, trip summaries, wallet events, and repayment records.

Create a volume model with pilot, base, and peak cases. For each state connected devices, active duty cycle, messages per second, readings per message, bytes, compression, daily ingest, retention by zone, downsampling, egress, and cost. Reconcile the 50,000 vehicle arithmetic and remove the unsupported 30 billion-row statement unless its row definition matches.

Integrate purpose limitation, minimisation, notice, lawful basis, consent where used, retention, deletion, access, and DPIA [10], [11]. Explain when edge aggregation replaces raw collection. Add a safety rule preventing credit punishment for device faults until source health is assessed.

**Acceptance tests:** Capacity calculations reconcile from device to storage. Every collected field has a purpose and retention. A lost connection has a bounded buffer and recovery path.

### D05-P03: Establish the clock dictionary and point-in-time join specification

**Action:** Replace “Point-in-Time Correctness” and cross-reference every source section.

**Resolves:** D05-I01 and D05-I05.

**Content:** Define clocks per event source: device event time, source transaction time, source commit, Debezium capture, Kafka append, Flink processing, first availability, correction availability, business effective date, accounting date, feature calculation, score request, and decision. State trust and fallback for each clock. Store raw clock values and normalised UTC with source timezone and precision.

Define the point-in-time rule: for a decision at time `t_d`, use only the latest valid record version with availability time no later than `t_d`, subject to its business-effective interval. Backdated corrections arriving after `t_d` cannot enter the historical training row, although they can be used for later accounting and label correction under explicit policy. For rate data, pin publication vintage.

Add pseudo-SQL or logical conditions, bitemporal examples, late wallet repayment, corrected policy cancellation, and platform file delay. Define training snapshot manifests.

**Acceptance tests:** Synthetic future-leak records are excluded. Re-running a historical snapshot by manifest gives identical input. Event and availability time are never silently substituted.

### D05-P04: Clarify ingestion, processing, table format, and replay boundaries

**Action:** Rewrite CDC, Kafka, Flink, Data Lakehouse, and Kappa sections.

**Resolves:** D05-I02, D05-I05, and D05-I09.

**Content:** State the selected table format, such as Apache Iceberg, and its catalogue, partition, compaction, snapshot, schema-evolution, and retention policy. Name Bronze, Silver, and Gold as medallion quality zones. Describe the online path as Kappa-style if it processes one replayable stream. If batch recomputation exists, call the architecture hybrid.

For Debezium define source log, transaction ordering, snapshot mode, primary key, delete tombstone, and timestamp meaning. For Kafka define topic ownership, partition key, ordering scope, schema registry, compatibility, retention, and DLQ. For Flink define event-time extraction, watermark, allowed lateness, keyed state, checkpoint, savepoint, state TTL, idempotent sink, and backpressure.

Define replay run ID, start offset or source snapshot, feature version, output namespace, promotion, reconciliation, and rollback. Clarify that exactly-once processing stops at unsupported external boundaries.

**Acceptance tests:** Duplicate, reorder, late, delete, schema change, partial sink, and replay tests pass. Gold receives only validated Silver facts. Product and architecture names are not conflated.

### D05-P05: Build the asynchronous as-of join matrix as a governed table

**Action:** Retain the concept but rebuild its fields.

**Resolves:** D05-I01 and D05-I07.

**Content:** For each source state entity key, event grain, event clock, availability clock, update frequency, expected delay, maximum age, allowed lateness, as-of selection, correction policy, null meaning, and training and serving source. Include telematics, trips, wallet, platform commission, fuel, KESONIA, macro, insurance policy, premium refund, credit balance, repayment, reserve, vehicle, geography, and regulatory status.

Define join precedence where driver, vehicle, wallet, and policy relationships change. Use effective-dated identity mapping. Add controls for many-to-one and one-to-many joins and row-count explosions. Record source freshness in the model input.

**Acceptance tests:** Each feature can trace to source versions. Join cardinality is asserted and monitored. Stale macro data and late wallet data produce defined outcomes.

### D05-P06: Create the feature registry and freeze explicit feature ownership

**Action:** Rewrite all feature-engineering sections.

**Resolves:** D05-I03 and D05-I07.

**Content:** Use a registry with feature ID, name, description, owner path, source, formula, units, entity grain, window, lag, minimum history, availability, null, clipping, monotonic expectation, interaction eligibility, privacy class, version, and tests. Include label definition and prohibited future information.

Assign CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, cash-out ratio, debt coverage, and approved interactions to the Explicit Liquidity Feature Path. Define each formula and denominator protection. State that raw wallet sequences may enter neural learning but named explicit metrics cannot. Add feature-store online and offline views with one transformation definition.

**Acceptance tests:** Registry contains no duplicate semantic feature under a different name. Online-offline values match within tolerance. Feature freshness and calculation failures are observable. Interaction count is controlled and maps to D06 priors.

### D05-P07: Correct neural context and fusion design

**Action:** Rewrite “The Dual-Regime Neural Architecture” through “Cross-Attention Feature Fusion.”

**Resolves:** D05-I04.

**Content:** Define GRU input tensor, sequence length, sampling and aggregation, mask, categorical embeddings, and output tokens. Define macro Transformer inputs as an ordered sequence of contextual tokens with observation dates, release dates, vintage, masks, and positional encodings. Avoid future macro revisions.

Choose one of two designs. If retaining cross-attention, preserve multiple context tokens as keys and values and define driver tokens as queries. If context is pooled, replace attention with gated fusion or concatenation. Include exact tensor shapes, residuals, normalisation, dropout, training objective, and output dimension. Add ablation comparisons against simple logistic, explicit-only, neural-only, concatenation, and attention.

**Acceptance tests:** Softmax has more than one meaningful key when called attention. The selected design improves a pre-specified time-split metric without harming calibration or subgroup stability. Latency and memory meet serving SLOs.

### D05-P08: Separate missing-data engineering from policy action

**Action:** Rewrite “Handling Asynchronous Clock Cycles and Missing Data.”

**Resolves:** D05-I08.

**Content:** Classify structural absence, random packet loss, source outage, stale data, customer opt-out, device failure, and suspicious suppression. Define imputation by feature type, mask and age indicators, uncertainty propagation, maximum staleness, and fallback representation. Do not automatically turn missingness into a negative credit action.

The downstream policy gate should own rules for manual review, lower limit, product restriction, or score unavailability. Add fairness analysis of missingness by device, network, geography, platform, and relevant groups. Include incident correlation so a platform outage does not decline a population.

**Acceptance tests:** Source outage simulation activates fallback without mass adverse action. Missingness reasons are observable. Imputation is fitted only on training data and versioned.

### D05-P09: Define the model-input contract to D06

**Action:** Rewrite “The Feature Fusion Vector as the Interface to Bayesian Inference.”

**Resolves:** D05-I03 and D05-I07.

**Content:** Define `Phi_neural`, `Z_liquidity`, model context, masks, uncertainty or quality flags, identifiers, decision timestamp, feature-set version, neural-model version, and source snapshot. State dimensions and ranges. Explain how cluster, product, platform, geography, and cohort IDs enter D06 without leaking protected or future information.

Define training and scoring serialization, backward compatibility, schema changes, deprecation, and consumer-driven contract tests. Add reason-code groupings so explicit features remain understandable.

**Acceptance tests:** D06 can consume a fixed contract without reading D05 internals. Old approved model versions can retrieve their exact feature contract. Breaking changes require approval and parallel validation.

### D05-P10: Add production quality, security, privacy, and recovery controls

**Action:** Add near the end.

**Resolves:** D05-I09 and D05-I10.

**Content:** Define SLOs for ingest completeness, event lateness, feature freshness, online availability, score latency, reconciliation, and replay. Add observability by source, platform, geography, product, and schema version. Define access roles, service identities, encryption, secrets, network boundaries, audit, key rotation, incident response, disaster recovery, and deletion or legal hold.

Link privacy fields to the DPIA and field inventory. State that pseudonymisation reduces risk but does not remove obligations. Define vendor and cross-border controls.

**Acceptance tests:** SLO breach creates an owned incident and policy fallback. Restore and replay drills meet RTO and RPO. A data-subject deletion or restriction request follows a documented path without corrupting statutory records.

### D05-P11: Build the full engineering acceptance suite

**Action:** Replace conclusion and references with test and decision criteria.

**Resolves:** D05-I11 and closes all findings.

**Content:** List unit tests for formulas, schema tests, contract tests, point-in-time tests, late and duplicate events, replay, online-offline parity, capacity, chaos, security, privacy, bias, and cost. Include golden datasets with known outputs. Require independent data and model-risk review. Cite official technology documentation and [10]-[12] for privacy and security rather than vendor marketing.

**Acceptance tests:** No critical test is manual-only. Every release has code, schema, feature, data snapshot, environment, and result hashes. Documentation and implementation are reviewed together.

## Migration and rollout strategy

Start with a small set of wallet, repayment, policy, and trip-summary events rather than full 10 Hz telemetry. Establish point-in-time correctness and explicit features first. Develop an explicit-only Bayesian benchmark. Add neural telemetry only when contracts, privacy, volume, and incremental validation justify it. This staged approach provides a credible fallback and quantifies the value of complexity.

Run offline backfill in an isolated namespace, compare to source ledgers, and promote only signed snapshots. In shadow mode, calculate features and scores without changing customer terms. Measure latency, completeness, drift, calibration, fairness, and operational incidents. Live activation should begin with bounded exposures and policy rules, plus manual and system rollback.

## Recommended editing order and reviewers

Perform P01 through P03 first. Complete P04 and P05 with platform and source owners. Freeze P06 before model development. Complete P07 and P09 jointly with D06. Complete P08 with policy and fairness reviewers. Add P10 and P11 before any live pilot.

Reviewers should include data architect, streaming engineer, source-system owners, ML engineer, chief data scientist, independent model validator, product owner, security architect, DPO, legal counsel, servicing and finance data owners, site reliability, and cost-management lead.

## Pre-publication validation checklist

- Clock dictionary and availability-time rules are complete.
- Table format and architecture pattern are named correctly.
- Volume arithmetic and cost tiers reconcile.
- Explicit features have one owner.
- Fusion design matches tensor shapes.
- Missingness and policy actions are separate.
- Replay and online-offline parity pass.
- Privacy and retention are field-level requirements.
- Model-input contract is versioned.
- Equations and punctuation pass automated and numerical tests.

## Data-quality SLO and control catalogue

Add a detailed SLO table by source and pipeline stage. Measures should include source availability, event completeness, duplicate rate, invalid schema, clock skew, lateness distribution, unresolved identity, reconciliation difference, feature freshness, online-offline parity, serving error, and correction backlog. For every metric state formula, dimension, target, warning, breach, measurement window, owner, alert, policy consequence, and recovery evidence.

Controls should distinguish prevention, detection, and correction. Schema validation and producer contracts prevent malformed events. Sequence and control totals detect gaps. Idempotency suppresses duplicates. Watermarks and quarantine handle lateness. Source-to-Silver and servicing reconciliation detects semantic drift. Feature parity tests detect transformation divergence. None of these controls alone proves point-in-time correctness, so the golden historical-snapshot tests remain mandatory.

Define how SLOs affect scoring. A single stale macro field may use an approved previous value plus age indicator. Missing repayment data may block a score or route to manual review. A population-wide platform outage should activate a source incident and stable fallback, not individual declines. The Credit Policy and Compliance Gate owns the business action, but D05 supplies health signals and reason.

## Cost, retention, and capacity governance

Build a monthly cost model by ingestion, streaming compute, state, lakehouse storage, compaction, feature serving, model serving, network egress, monitoring, backup, and recovery. Tie cost to the pilot, base, and peak volume assumptions from P02. State retention by raw and derived class, including legal, accounting, validation, privacy, and scientific need. Do not retain 10 Hz raw telemetry indefinitely because storage is cheap at pilot scale.

Define capacity gates at 25%, 50%, 75%, and 100% of target load. Measure p50, p95, and p99 latency, backpressure, checkpoint time, recovery, state size, compaction, feature freshness, and cost per connected and active driver. Include source bursts and replay while live traffic continues. Establish autoscaling boundaries and cost alarms.

An architecture review should approve any increased sampling, retention, or source. The proposer must show incremental decision value, privacy necessity, cost, security, and deletion capability. This converts data minimisation and cost discipline into ongoing engineering decisions rather than one-time prose.

## Data-contract change and backward compatibility

Create a formal schema and feature change process. Producers publish proposals with semantic meaning, units, clock, null and deletion behaviour, example payloads, migration, and sunset. Consumers run compatibility and historical replay tests. Breaking changes receive a new major contract version and coexist during migration. Feature formula changes create a new feature version even when the name remains similar.

Maintain a dependency graph from source field through Silver fact, feature, model, decision, policy reason, and report. Before removal or reinterpretation, identify every consumer and historical reproducibility obligation. Preserve approved model versions' input contract and transformation artifacts through their required retention. This is essential for audit and customer dispute resolution.

## Definition of done

D05 is complete when an engineer can implement the pipeline and a validator can reproduce any historical model input without guessing clocks, schemas, windows, or feature ownership. The system must demonstrate point-in-time correctness, online-offline parity, bounded replay, measurable quality, privacy by design, and a stable D06 interface under tested pilot volumes.
