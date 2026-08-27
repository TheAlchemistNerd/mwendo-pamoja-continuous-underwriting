# D05 Inconsistency Report: Temporal Representation and Features

## Document role and semantic synopsis

D05 is the technical specification for edge telemetry, streaming, lakehouse storage, point-in-time joins, engineered features, neural encoders, and the interface to Bayesian underwriting. It is the architectural hinge of the series: D04 defines product events, D06 consumes model inputs, D08 posts accounting results, and D10 implements the system. The paper contains useful detail on IMU and GNSS signals, Debezium, Kafka, Flink, asynchronous clocks, missing data, GRUs, Transformers, and an explicit liquidity branch.

Its greatest problem is not ambition but boundary control. The document simultaneously calls the storage system Iceberg and “Delta,” treats time travel as point-in-time correctness, and assigns some financial metrics to more than one path. Its cross-attention block is mathematically uninformative if the Transformer context has already been pooled to a single token. Event time, system time, effective time, and data availability are not consistently separated. Volume claims and schema granularity do not reconcile.

## Executive inconsistency summary

The architecture should be retained but rewritten around explicit contracts. Raw events flow to governed feature services; Flink produces a neural sequence branch and the Explicit Liquidity Feature Path; both feed HBLR; a separate Credit Policy and Compliance Gate applies rules. CFA, DLR, Earnings Velocity, and Repayment Velocity must have one engineered owner. Point-in-time correctness must use availability-time snapshots and event-time watermarks, not only lakehouse time travel. The storage product and architecture pattern must be named separately. The fusion mechanism must match the tensor shapes actually passed to it.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D05-I01 | Critical | High | Sections on pipelines and as-of joins | Point-in-time correctness is not actually guaranteed |
| D05-I02 | High | High | Data Lakehouse and Kappa sections | Delta, Iceberg, medallion, and Kappa are conflated |
| D05-I03 | High | High | Feature sections | Named liquidity metrics have duplicate ownership risk |
| D05-I04 | High | High | Cross-Attention Feature Fusion | Single-token attention cannot learn temporal alignment |
| D05-I05 | High | High | CDC and Flink sections | Event, processing, system, and effective time drift |
| D05-I06 | High | Medium | Edge and raw format | Telemetry volume and row-granularity arithmetic conflict |
| D05-I07 | High | High | Feature engineering | Leakage, labels, windows, and availability are under-specified |
| D05-I08 | Medium | High | Missing data | Missingness controls mix imputation and credit action |
| D05-I09 | High | Medium | Production architecture | Idempotency, replay, schema evolution, and deletion are incomplete |
| D05-I10 | High | High | Edge capture and storage | Privacy, consent, retention, and security are secondary |
| D05-I11 | Medium | High | Mathematics throughout | Formula and symbol corruption blocks reproducibility |

## Detailed findings

### D05-I01: Time travel is mistaken for point-in-time correctness

**Anchor:** “Point-in-Time Correctness: The Asynchronous As-Of Join Matrix” and “Data Lakehouse.” The draft relies on time-travel queries and `FOR SYSTEM_TIME AS OF` language as if selecting an older table version guarantees that only information available at a historical decision is used.

**Impact:** A record can carry an old effective date but arrive or be corrected later. Querying by event date or the latest historical snapshot can leak future information. Training leakage would inflate reported discrimination and invalidate underwriting, fairness, and stress results.

**Canonical resolution:** Store event time, source transaction time, ingestion time, first-availability time, correction version, and decision cut-off. A training join must use the latest valid version whose availability time was no later than the decision time. Define bitemporal or tritemporal rules. Snapshot and rate vintages should be immutable, but corrections should remain linked. Add automated leakage tests with deliberately late events.

### D05-I02: Architecture patterns and storage products are conflated

**Anchor:** “Data Lakehouse: Unified Tiered Storage (The Delta Architecture),” “The Kappa Architecture,” and the implementation description. The document discusses Apache Iceberg tables while calling them Delta Architecture or Delta Lake, and sometimes uses medallion layers as if they were the same concept.

**Impact:** Engineers may provision the wrong connectors and SQL semantics. “Delta” can mean Delta Lake, the older batch-plus-stream Delta architecture, or a change increment. Kappa is a processing pattern, while Bronze, Silver, and Gold are governance zones.

**Canonical resolution:** Choose and state the table format, preferably “Apache Iceberg table format” if that is the actual design. Call Bronze, Silver, and Gold the medallion data-quality zones. Call the real-time path Kappa-style only if one replayable stream is the processing source. If batch recomputation is retained, explain the hybrid rather than claiming doctrinal purity.

### D05-I03: Explicit financial features need one owner

**Anchor:** “High-Frequency Behavioral Stream,” “Driver Liquidity and Solvency Features,” “The Dual-Regime Neural Architecture,” and D02 Section 2.2. Earnings Velocity and related financial variables appear in neural descriptions while the explicit section says they bypass the encoders.

**Impact:** Duplicate engineered metrics can produce unstable coefficients and misleading SHAP explanations. It becomes impossible to say whether a policy decision arose from a latent embedding, a spline, or a rule.

**Canonical resolution:** CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved financial interactions are Explicit Liquidity Features. Raw wallet-event sequences may enter the neural path to learn rhythm, but not the named engineered values. Record an owner, formula, window, time cut-off, units, null policy, monotonic expectation, and version for each feature.

### D05-I04: The cross-attention design is degenerate after pooling

**Anchor:** “Branch 2,” “Asynchronous Dual-Rate Clock Coupling,” and “Cross-Attention Feature Fusion.” The text appears to reduce macro context to one Transformer vector and then uses it as attention keys and values for the GRU representation.

**Impact:** With one key, the softmax is one. The block cannot choose among contextual times or regimes, so claims about temporal alignment are false. It adds parameters without the stated function.

**Canonical resolution:** Preserve a sequence of contextual Transformer tokens, including dates and masks, as keys and values if cross-attention is required. Query with driver-session tokens or current state. Alternatively, use gated fusion or concatenation of pooled embeddings and explain that design honestly. Specify tensor shapes, masks, positional encodings, training objective, and ablation acceptance test.

### D05-I05: Multiple clocks are named but not operationally defined

**Anchor:** “Change Data Capture,” “Apache Flink,” and “Asynchronous Dual-Rate Clock Coupling.” Debezium timestamps, Kafka offsets, event timestamps, Flink watermarks, ERP effective dates, and model-decision times are treated inconsistently. `ts_us` can reflect connector or source metadata and is not automatically the legal transaction time.

**Impact:** Late repayments may change delinquency, duplicate events may double count wallet cash, and backdated policy changes may contaminate labels. Finance close and model replay will disagree.

**Canonical resolution:** Create a clock dictionary. Define producer event time, source-commit time, connector capture time, Kafka append time, Flink processing time, business effective date, accounting date, and model decision time. Select the authoritative clock by event type. Set watermark and allowed-lateness policies, correction paths, idempotency keys, and reconciliation controls.

### D05-I06: Telemetry volume does not reconcile to the row schema

**Anchor:** “Edge Capture: Hardware Layer and Raw Data Format.” The paper combines 50,000 vehicles, 10 Hz capture, multiple scalar channels, and an approximate 30 billion rows per day. If one row holds all scalars at each timestamp, 50,000 times 10 times 86,400 equals 43.2 billion timestamp rows per day. If one row represents a scalar, volume is much larger. Driving hours would reduce the figure, but are not stated.

**Impact:** Storage, bandwidth, partitioning, cost, retention, and model-latency plans can be wrong by an order of magnitude.

**Canonical resolution:** Define record granularity, active vehicles by hour, duty cycle, sampling, compression, edge aggregation, message size, and retention by zone. Provide low, base, and peak calculations in bytes per second and terabytes per day. State which raw frequency is retained and which derived statistics are downsampled.

### D05-I07: Feature definitions omit label and window discipline

**Anchor:** “Exhaustive Feature Engineering” and “Gig-Economy Specific Interaction Effects.” Many features have attractive names but incomplete formulas, observation windows, minimum history, denominator guards, availability delay, and relationship to prediction horizons.

**Impact:** A feature may contain repayments occurring after the score, use a zero denominator, or aggregate over the outcome window. Reproducibility and fairness monitoring fail when product cohorts have different history.

**Canonical resolution:** Build a feature registry with formula, entity key, grain, units, window, lag, publication delay, minimum observations, null semantics, clipping, monotonic hypothesis, prohibited sources, label window, and owner. Add point-in-time unit tests. Define interactions only after primary features are stable and regularise them in D06.

### D05-I08: Missingness treatment includes policy decisions

**Anchor:** “Handling Asynchronous Clock Cycles and Missing Data.” The draft mixes imputation, masks, stale values, uncertainty response, and credit actions. It sometimes treats missing telematics as risk by default.

**Impact:** Missingness may be caused by network coverage, device failure, platform outage, or customer behaviour. Automatically penalising it can create unfair geographic effects and feedback loops.

**Canonical resolution:** Separate technical handling from policy. The feature layer creates age, missingness, and source-health indicators and uses approved imputation. The Bayesian model propagates uncertainty. The policy gate defines fallback products, manual review, or freeze criteria. Test missingness by geography, device, platform, and protected or proxy groups.

### D05-I09: Production guarantees are under-specified

**Anchor:** CDC, Kafka, Flink, Kappa, and lakehouse sections. The narrative names fault-tolerant technologies but does not define delivery semantics at external sinks, duplicate suppression, replay boundaries, schema compatibility, backfill, feature version pinning, or deletion propagation.

**Impact:** “Exactly once” inside a stream processor does not ensure exactly-once financial posting or feature computation across all systems. Replays can alter past scores or duplicate journals.

**Canonical resolution:** Specify idempotency keys, transactional outbox or equivalent, checkpoint and savepoint policy, replay run ID, schema registry compatibility, quarantine, data-quality SLOs, feature materialisation version, online-offline parity tests, and reconciliation to the servicing ledger. Deletion and legal holds must propagate under governed workflows.

### D05-I10: High-risk personal-data processing is treated as an engineering input

**Anchor:** Edge capture and raw-data sections. Continuous GNSS, IMU, wallet, diagnostic, and behavioural data are extensively described, but purpose limitation, lawful basis, notices, driver controls, retention, data minimisation, cross-border processing, and DPIA are not integral to the design.

**Impact:** The data moat can become a compliance and trust liability. Location and financial behaviour enable sensitive inference and automated decisions. Security alone does not establish lawful processing [10], [11].

**Canonical resolution:** Add privacy requirements to every event contract: purpose, lawful basis, minimised fields, sampling justification, retention, access, processor, jurisdiction, deletion, and customer rights. Conduct a DPIA before pilot. Use edge aggregation where raw detail is unnecessary and create a non-telematics fallback where legally and commercially required.

### D05-I11: Mathematical notation is corrupted and incomplete

**Anchor:** Feature formulas, GRU equations, attention, and B-spline expressions. Commas replace subtraction in expressions such as `1 - z`, `1 - theta`, and related gates. Inequality and range characters display as mojibake in several files.

**Impact:** Implementers can code the wrong recurrence or spline basis, and reviewers cannot reproduce results.

**Canonical resolution:** Re-key equations from authoritative definitions, run symbolic and dimensional review, assign every symbol once, and include small numerical tests. Use ASCII minus where encoding stability matters. Render Markdown equations before publication and compare them to executable reference tests.

## Dependencies, diligence, and remediation sequence

D05 requires D04's event and product-state dictionary. It supplies D06's features and tensors, D08's data lineage, and D10's infrastructure requirements. Evidence needed includes sample telemetry payloads, wallet and servicing CDC records, source clocks, platform SLAs, expected vehicle duty cycles, retention policy, data agreements, DPIA, feature registry, schema-registry plan, and prototype benchmarks.

Remediation order is: define clocks and point-in-time rules; freeze storage terminology; reconcile event schema and volume; freeze feature ownership; repair formulas; redesign fusion; specify missingness and privacy; then add production replay and lineage controls. No model-performance claim should survive until offline and online feature parity and leakage tests pass.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D05-I01 | D05-P03, D05-P05 |
| D05-I02 | D05-P04 |
| D05-I03 | D05-P06, D05-P09 |
| D05-I04 | D05-P07 |
| D05-I05 | D05-P03, D05-P04 |
| D05-I06 | D05-P02 |
| D05-I07 | D05-P06, D05-P09 |
| D05-I08 | D05-P08 |
| D05-I09 | D05-P04, D05-P10 |
| D05-I10 | D05-P02, D05-P10 |
| D05-I11 | D05-P01, D05-P11 |
