---
title: "Part 2a: Advanced Predictive Modeling, Deep Temporal Representation and Feature Engineering"
author: "Nevil Maloba"
date: "25 August 2026"
status: "Narrative white paper edition"
output:
  pdf_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
  word_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
---

# 1. Introduction to Continuous Underwriting Data Architectures

Part 1 ended at the moment a driver, a vehicle, and three financial products begin to fail together. Part 2a moves inside that moment. It asks what the platform could actually have known before the cascade, which timestamp makes that knowledge legitimate, how a physical signal becomes a feature, and how a feature reaches a model without being counted twice.

The ambition is to predict and interrupt avoidable failure before it reaches the loss ledger. A bureau score remains valuable evidence of prior credit behaviour; it does not have "zero" predictive weight. Its limitation is temporal resolution. A driver may cross the sufficiency boundary \(I_{\text{net}}<S\) between reporting cycles after a repair, fuel, platform, or demand shock. Higher-frequency information may improve the timing of a response, provided it is consented, point-in-time correct, relevant, stable, and tested against simpler baselines.

Two structural failure modes motivate the architecture. First, **temporal blindness**: a feature can reflect the last bureau pull rather than the decision moment. Second, **population and label mismatch**: a model trained on a different employment and product population may not transfer cleanly to variable platform income. The empirical distribution may be skewed, heavy-tailed, seasonal, zero-inflated, or regime-dependent; it should not be declared Gaussian or power-law without testing. The design therefore keeps distributional assumptions visible and validates them by product, platform, geography, and time.

The system complements conventional evidence with a daily or event-triggered posterior distribution. A GRU branch learns short-term operational and sequence state [1]. A Transformer branch represents slower macroeconomic, platform, and regulatory context [2]. A separate Explicit Liquidity Feature Path calculates CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and defined interactions. These engineered financial variables do not enter either neural encoder. The branches meet only at the redundancy-controlled HLR in Part 2b.

Point-in-time controls can materially reduce look-ahead leakage, but no library call can guarantee it. Source corrections, late events, label construction, clock skew, backfills, and changing definitions still require tests and lineage.

# 2. Edge Capture: Hardware Layer and Raw Data Format

Before any streaming architecture can be discussed, the physical origin of the data must be understood precisely. The gig driver's vehicle is a rolling sensor array. At the telematics hardware level, three distinct sensor families generate the raw input streams:

**IMU / gyrometer layer:** The Inertial Measurement Unit records tri-axial linear acceleration \((a_x,a_y,a_z)\) and angular velocity \((\omega_x,\omega_y,\omega_z)\). At 10 Hz, six channels yield 60 scalar readings per second before other sensor fields. Thresholds such as \(|a_{\text{brake}}|>0.6g\) for 500 milliseconds are candidate event definitions, not universal facts. Road geometry, device mounting, vehicle type, speed, calibration, and sensor noise can change the observed pattern. Fatigue is not directly observed by yaw oscillation; it is a risk hypothesis requiring safe validation.

**GNSS Layer:** The Global Navigation Satellite System receiver generates latitude, longitude, altitude, instantaneous speed (km/h), and heading at 1 Hz (1 sample per second). Speed data cross-validates the OBD-II reading, enables geofence computation, and provides the ground-truth mileage feed for the UBI per-kilometer premium calculation $\text{Premium}_{\text{daily}} = \text{Base}_{\text{static}} + \gamma \cdot \text{MilesDriven}_{\text{daily}}$.

**OBD-II / CAN-bus layer:** Subject to vehicle compatibility and permission, the interface can expose engine RPM, throttle position, fuel level, manifold pressure, coolant temperature, and Diagnostic Trouble Codes. A code such as P0301 indicates a cylinder-one misfire condition; it does not create a universal 72-hour forecast of engine failure. The useful feature is the code, recurrence, severity, associated measurements, service history, and verified outcome.

On arrival at the cloud infrastructure, all sensor streams converge into tabular records in PostgreSQL or MySQL operational databases with the schema:

```
timestamp (BIGINT, unix microseconds)
vehicle_id (UUID)
lat (FLOAT8), lon (FLOAT8), altitude_m (FLOAT4), speed_kmh (FLOAT4)
accel_x, accel_y, accel_z (FLOAT4)    -- m/s^2
g_force_lateral, g_force_longitudinal (FLOAT4)
angular_vel_x, angular_vel_y, angular_vel_z (FLOAT4)   -- rad/s
rpm (INT), fuel_pct (FLOAT4)
dtc_codes (TEXT[])
```

A fleet of 50,000 vehicles sampled continuously at 10 Hz would generate 43.2 billion device-time observations per day before aggregation, or far more scalar readings if every sensor channel is stored separately. Real duty cycles, edge aggregation, compression, sampling policies, connectivity, and retention will change the volume. The calculation is therefore a capacity envelope, not a production forecast. It nonetheless explains why raw sensor ingestion should be decoupled from transactional ledgers and why event streaming, edge summarisation, and tiered storage are required.


# 3. Architectural Implementation: Refined Data Engineering Pipeline

The Insurtech's data engineering backbone implements a modern **Lakehouse streaming architecture** organized around four sequential layers: Change Data Capture, Event Streaming, Real-Time Stream Processing, and Open-Format Lakehouse storage. This pipeline ensures that high-frequency telematics events are scored in near-real-time by the GRU inference layer, while simultaneously building the immutable long-term historical record that the Transformer queries for macro context encoding, as detailed in **Figure 1**.


**Figure 1: Multimodal Data Engineering Pipeline**

```{.mermaid layout=fullpage}
%%{init: {"flowchart": {"defaultRenderer": "elk"}}}%%
graph TD
    %% Edge Hardware
    subgraph EdgeLayer [Edge: Vehicle Sensor Array]
        IMU[IMU / Gyrometer\n10 Hz: accel, angular_vel]
        GNSS[GNSS\n1 Hz: lat, lon, speed, altitude]
        OBD[OBD-II / CAN-Bus\nRPM, fuel, DTCs]
    end

    %% Operational Databases
    subgraph OpsDB [Cloud Operational Databases]
        TelDB[(Telematics DB\nPostgreSQL)]
        WalletDB[(Wallet / Ledger DB\nMySQL)]
        MacroDB[(Macro / Regulatory DB\nPostgreSQL SCD Type-2)]
    end

    %% CDC Layer
    subgraph CDCLayer [Change Data Capture: Debezium]
        CDC_Tel[Debezium Connector\nWAL / Binlog Attach]
        CDC_Wallet[Debezium Connector\nWallet & Ledger CDC]
    end

    %% Dual Path Routing
    subgraph KafkaLayer [Apache Kafka: Event Streaming Backbone]
        K_Tel[Topic: vehicle-telemetry-stream]
        K_Wallet[Topic: wallet-ledger-stream]
    end

    subgraph LakehouseBronze [Data Lakehouse: Bronze Zone]
        Bronze[(Bronze Tables: Apache Iceberg\nRaw Macro & Platform Data)]
    end

    %% Processing
    subgraph FlinkLayer [Apache Flink: Stateful Stream & Batch Processing]
        F_Kappa[Kappa Path: Real-Time Stream\n5-sec Windows & Join]
        F_Delta[Delta Path: Batch/Micro-batch\nClean & Enrich Bronze Data]
    end

    %% Lakehouse Silver Storage
    subgraph LakehouseSilver [Data Lakehouse: Silver Zone]
        Silver[(Silver Tables: Apache Iceberg\nCleaned High-Freq History & Macro Data)]
    end

    %% Downstream Consumers
    subgraph Consumers [Downstream Consumers]
        GRU_Model[GRU Inference Layer\nShort-Term Latent State h_t]
        Trans_Model[Transformer Layer\nMonthly Batch: Long-Term Context c_L,τ]
        Fusion[Feature Fusion Layer\nΦ_it = h_t concat c_L,τ]
        TabularVars[Explicit Liquidity Feature Path\nInterpretable financial variables]
        Bayes[Hierarchical Bayesian\nUnderwriting Engine]
        Gate[Credit Policy and Compliance Gate\nRules, rights, limits and uncertainty]
    end

    %% Data Flow Connections
    IMU --> TelDB
    GNSS --> TelDB
    OBD --> TelDB

    TelDB --> CDC_Tel
    WalletDB --> CDC_Wallet
    MacroDB -->|Batch ELT / Airbyte| Bronze

    %% Path Split
    CDC_Tel --> K_Tel
    CDC_Wallet --> K_Wallet

    %% Kappa Path (Stream)
    K_Tel --> F_Kappa
    K_Wallet --> F_Kappa
    F_Kappa -->|State Updates| F_Sink[Kappa-to-Delta Bridge\nStatutory ERP Integration]
    F_Delta -->|Historical Rebuild| Bronze
    F_Kappa -->|Neural Path| GRU_Model
    F_Kappa -->|Explicit Liquidity Feature Path| TabularVars
    F_Kappa --> Silver

    %% Delta Path (Batch/Macro)
    Bronze --> F_Delta
    F_Delta --> Silver
    Silver --> Trans_Model

    %% Fusion
    GRU_Model --> Fusion
    Trans_Model --> Fusion
    Fusion -->|Neural Embedding Φ_it| Bayes
    TabularVars -->|B-Splines / Interactions| Bayes
    Bayes -->|Posterior PD and interval| Gate

    style F_Kappa fill:#e67e22,color:#fff
    style F_Delta fill:#2980b9,color:#fff
    style Bronze fill:#7f8c8d,color:#fff
    style Silver fill:#95a5a6,color:#fff
    style EdgeLayer fill:#2c3e50,color:#fff
    style CDCLayer fill:#8e44ad,color:#fff
    style KafkaLayer fill:#231f20,color:#fff
    style FlinkLayer fill:#e6522c,color:#fff
    style Consumers fill:#27ae60,color:#fff
```

## 3.1. Change Data Capture via Debezium

Debezium can read the PostgreSQL Write-Ahead Log or MySQL binary log and publish committed row-level changes without periodic table scans. A connector envelope can include `before`, `after`, operation, source metadata, and processing timestamps in Avro or JSON. Field availability and timestamp meaning depend on connector and configuration [3]. End-to-end latency such as 50 milliseconds is a benchmark target, not an architectural fact. More importantly, source commit time, connector time, ingestion time, and event time must not be collapsed into a misleading two-clock story.

Log-based CDC can reduce polling load, but snapshotting, log retention, connector lag, backpressure, schema changes, and recovery still require controls. Telematics does not normally originate in a relational WAL; its device or gateway path is separate. A 10 Hz stream and sub-second downstream latency are capacity and service-level assumptions to test on representative devices, networks, partitions, and failure modes.

## 3.2. Apache Kafka: Fault-Tolerant Event Streaming

Connectors publish changes to Kafka topics organised by data domain. A `vehicle-telemetry-stream` topic may be keyed by `vehicle_id` so records with the same effective key are assigned to the same partition under a stable partitioning strategy. Kafka preserves order within a partition, not across partitions [4], and producer retries, key changes, duplicate delivery, late device events, and replay still require sequence numbers, idempotency, event-time buffering, and tests. The GRU input builder, rather than Kafka alone, is responsible for reconstructing the ordered sequence $\mathbf{x}_{t-1},\mathbf{x}_t$.

Kafka's retention policy implements a tiered storage strategy: a 7-day hot window on NVMe SSD for low-latency GRU stream consumption, with automated tiered offload to object storage (S3 or GCS) for long-term archival. The archived topics serve as the historical data source for Transformer training and periodic full-model retraining.

## 3.3. Apache Flink: Stateful Real-Time Stream Processing

Apache Flink consumes the Kafka topics via the Flink SQL or DataStream API, executing four classes of real-time operations in parallel [5]:

- **1. Tumbling Window Aggregations:** 5-second tumbling windows aggregate raw telematics into the per-window statistics required for feature engineering, mean speed, peak G-force, count of hard-braking events, fuel consumption delta. These window outputs serve as the input vectors $\mathbf{x}_t^{\text{tele}}$ for the GRU layer.

- **2. Hard-Braking and Operational Stress Rules:** Stateless rule evaluators flag individual events exceeding configurable thresholds. A hard-braking event is flagged when $|a_{\text{brake}}| > 0.6g$ sustained over 500ms. Fatigue detection fires when cumulative consecutive driving hours within a single session exceed a configurable threshold (typically 10 hours without a 30-minute break). DTC code detection flags any non-empty `dtc_codes` array, immediately triggering an alert to the underwriting engine.

- **3. Temporal Table Joins for Point-in-Time Correctness:** Flink's `FOR SYSTEM_TIME AS OF` syntax implements zero-look-ahead joins between the high-frequency telematics stream and low-frequency macro state tables:

  ```sql
  SELECT
      t.vehicle_id,
      t.window_end_ts,
      t.mean_speed_kmh,
      t.peak_g_force,
      m.gas_price_index,
      m.platform_commission_pct,
      r.zev_mandate_tier
  FROM telematics_windows AS t
  JOIN macro_table FOR SYSTEM_TIME AS OF t.window_end_ts AS m
      ON t.jurisdiction_code = m.jurisdiction_code
  JOIN regulatory_table FOR SYSTEM_TIME AS OF t.window_end_ts AS r
      ON t.jurisdiction_code = r.jurisdiction_code
  ```

  The intended temporal join selects the version valid and available at the historical decision time. The exact Flink syntax depends on whether the table is versioned by event time or processing time and on connector support. The test suite must prove the behaviour under late events, corrections, backfills, and out-of-order arrival.

- **4. ACID Lakehouse Sink:** In parallel with GRU inference feeding, Flink sinks all processed records to the Lakehouse via Apache Iceberg's transactional write protocol. Iceberg snapshot isolation supports consistent reads of committed historical state for Transformer training [6].

## 3.4. Data Lakehouse: Unified Tiered Storage (The Delta Architecture)

A Delta Architecture (often called a Data Lakehouse) is designed to store massive amounts of historical data reliably so that data scientists can train AI models on it offline. It uses a concept called the "Medallion Architecture" to represent data as it gets cleaner and more refined. The Lakehouse implements a three-tier table architecture:

- **Bronze tables (retained source events):** This layer preserves received payloads, source metadata, schema version, and arrival lineage. It is evidence of what the platform received, not proof that the upstream fact was correct. Versioned macro, regulatory, and platform configuration records should distinguish effective time from knowledge and ingestion time rather than relying on `valid_from` and `valid_to` alone.
- **Silver Tables (Cleaned & Filtered):** The data engineering pipeline (Apache Flink) cleans the Bronze data. It handles missing values, converts timestamps, and partitions the data by `vehicle_id` and `date`. Each partition contains the chronologically ordered sequence of Flink-windowed feature vectors for a specific driver. These are the input sequences consumed by the Transformer's monthly batch processing to construct the 12, 24 month historical token window $\mathbf{X}^{\text{macro}}$.
- **Gold tables (approved analytical and integration views):** Gold views can hold reconciled KESONIA calculations, approved risk and accounting inputs, SPV waterfall results, and reporting aggregates. They are not statutory ledgers and should not be called immutable merely because they are curated. Product subledgers, the SPV register, and D365 remain authoritative for their allocated records, while Gold views preserve lineage to the approved source events.

**The Problem with Delta for Real-Time Underwriting:**
Delta architecture relies on writing files to disk (like AWS S3 or GCS). Writing and reading from disk takes seconds or minutes. If a driver requests a microloan, the system cannot wait 30 seconds for the Delta Lake to retrieve their wallet balance. Therefore, while the Gold layer is the ultimate destination for statutory accounting (resolved via the **Asynchronous Kappa-to-Delta Bridge** detailed in **Part 4**), the actual real-time credit decision must bypass it.

## 3.5. The Kappa Architecture (The "Stream")

The Kappa Architecture was invented to solve the speed problem. In a Kappa architecture, everything is treated as a continuous stream of events. There is no "batch" database to query for real-time decisions. When data streams in (like a Debezium CDC event showing a driver just spent $10), a stream processor like Apache Flink updates the driver's total wallet balance in its internal RocksDB memory (or an external high-speed memory cache like Redis) instantly. Because the data lives in active memory (not written to a slow disk), the inference engine can fetch the driver's exact wallet balance in under 2 milliseconds.

### 3.5.1. The Mwendo Pamoja Case Study: Why Both Are Required

Consider a real-time scenario where a driver requests a microloan at 2:00 PM on a Tuesday. The system has 100 milliseconds to approve or deny it. This requires orchestrating data across both offline batch and real-time streaming architectures.

- **1. The Transformer (Using Delta / Low-Frequency):** The Transformer model needs to know the macroeconomic context (fuel prices, inflation, platform commission rates over the last 24 months). This data changes very slowly. Once a month, the system trains the Transformer on the massive historical Silver Tables in the Delta Lake. The Transformer outputs a single dense "context vector" ($\mathbf{c}_{L,\tau}$) that represents the current economy. That vector just sits quietly waiting to be used.

- **2. The GRU & Cross-Attention (Kappa / High-Frequency):** Simultaneously, the driver's real-time kinematic telemetry is processed by the GRU ($\mathbf{h}_T^{\text{GRU}}$). The system uses a Cross-Attention Fusion layer to fuse the GRU's current behavioral state with the Transformer's macro context vector, generating a single, unified neural representation of the driver's risk state ($\boldsymbol{\Phi}_{it}$).

- **3. The Explicit Liquidity Feature Path (Using Kappa / Liquidity):** The Bayesian risk model *also* needs to know the driver's exact Wallet Cash-Flow Asymmetry (CFA) right at this second. The system cannot query the Delta Lake for this; it’s too slow. Instead, every time the driver earns or spends a cent, the Debezium stream updates the driver's CFA in a lightning-fast Redis cache (Kappa Architecture).

- **The moment of decision:** At 2:00 PM, the system retrieves the versioned neural representation and the latest valid Explicit Liquidity Features. The HLR produces a posterior PD and uncertainty summary; the Credit Policy and Compliance Gate then determines the permitted action. Forty-five milliseconds remains an end-to-end latency target with a defined percentile and load profile. The lakehouse supports reproducible history; the online path supports the present.

## 3.6. Low-Frequency Data Ingestion: Macro, Regulatory, and Platform Context

The Transformer's effectiveness depends on ingesting all structural factors that affect gig-driver earning capacity and credit risk on timescales longer than the GRU's daily window. Four categories are relevant:

- **Macroeconomic conditions** (fuel-price measures, CPI, exchange rates, and central-bank policy or benchmark rates): Monthly or release-driven ingestion uses Central Bank of Kenya publications and benchmark series, World Bank indicator APIs, and IMF SDMX or Data APIs [7]-[9]. Where a Kenyan source publishes files rather than an API, a scheduled ingestion job retrieves the authoritative release. Python Airflow DAGs commit results to Bronze SCD Type 2 tables with the publication date, effective date, source version, and revision lineage.
- **Platform algorithmic regimes** (base-fare floors, surge policies, and commission rates): Contracted webhooks, published notices, or other authorised interfaces can provide versioned configuration evidence. An illustrative one to four hour refresh target must be tested against what the partner actually exposes. The system must not assume access to a platform's internal configuration database.
- **Regulatory and ZEV mandates** (gig-worker reclassification laws, metropolitan vehicle permit caps, zero-emission vehicle transition deadlines): Web-scraping pipelines and legal API feeds, committed with the regulatory `effective_date` and `jurisdiction_code`. Mapped to geohash zones for regional driver impact computation.
- **Urban infrastructure events** (prolonged highway reconstructions, corridor capacity changes): Open Street Map and city open-data feeds. Relevant because permanent road closures or capacity degradation durably depress hourly earning capacity for all drivers operating specific geohash corridors.


# 4. Point-in-Time Correctness: The Asynchronous As-Of Join Matrix

One of the greatest engineering hazards in retrospective underwriting is **look-ahead bias**: allowing a historical feature to contain information that was not available at the decision time. If a training record at `2024-03-15 11:30 AM` contains a gas-price observation first knowable to the platform at `2024-03-15 12:00 PM`, perhaps because event time was confused with arrival time, the back-test can learn a relationship unavailable in production. Apparent accuracy then disappears when the model meets the live clock.

The event envelope and source metadata should preserve at least business-effective time $T_e$, source commit time $T_c$, ingestion time $T_i$, and model decision time $T_d$. Field names depend on the connector and database and should not be inferred from precision suffixes alone. A necessary availability constraint is:

$$
T_i\le T_d,\qquad
T_e\le T_d,\qquad
\operatorname{version}(x,T_d)
=\max\{v:T_i(v)\le T_d\}.
$$

A decision may only use a version that had arrived by the decision timestamp and whose effective-time treatment is valid for the feature definition. This prevents a known future version from entering the row when the source and pipeline honour the contract. It does not eliminate label leakage, incorrect effective dates, backfilled facts, or accidental reuse of present-day dimensions.

When no new low-frequency record has been committed since the last join, the pipeline applies a **Zero-Order Hold**: the last committed macro state is broadcast unchanged across all subsequent high-frequency events until a new commitment arrives. This is equivalent to the asynchronous decoupled clock cycle of the GRU/Transformer dual-regime architecture: the Transformer's $\mathbf{c}_{L,\tau}$ vector is held constant across all daily GRU cycles until a new monthly Transformer run produces $\mathbf{c}_{L,\tau+1}$.

The feature-store pattern formalises the retrieval contract. A spine containing decision time and entity identifiers is joined to versioned feature views using documented availability and validity rules. The returned training frame is accepted only after automated leakage tests, boundary cases, replay comparison, source-to-feature lineage, and sign-off on label timing.

## 4.1. The Credit-State Ledger and Five Clocks

Point-in-time correctness becomes operational when every training row can be reconstructed from five connected ledgers. The **identity and exposure ledger** links the driver, product, facility, contract, vehicle, platform, policy, geography, and risk episode. The **obligation ledger** records schedules, due amounts, limits, draws, repayments, policy finance, arrears, and modifications. The **decision and action ledger** records the model artifact, feature snapshot, calibrated estimate, policy version, human approval, intervention, notice, and override. The **outcome and maturity ledger** records product-specific default, cure, closure, censoring, and the date on which a label became observable. The **recovery and cash-flow ledger** records collections, IPF refunds, write-offs, recoveries, costs, delays, and SPV allocation.

These ledgers preserve five times whose names should not be collapsed:

| Clock | Meaning | Principal control |
|---|---|---|
| Event time \(T_e\) | When the underlying activity occurred | Source sequence and correction lineage |
| Availability time \(T_a\) | When the platform could lawfully and technically use it | Point-in-time feature join |
| Decision time \(T_d\) | When a score or action was produced | Immutable decision snapshot |
| Label-maturity time \(T_m\) | When the full product outcome window became observable | Training eligibility and censoring |
| Cash-realisation time \(T_c\) | When collection, refund, cost, or recovery affected cash | ECL, loss, and SPV cohort timing |

A feature is eligible only when

$$
T_a\le T_d,
$$

and a fully matured supervised label can enter a training cutoff \(T_{\mathrm{train}}\) only when

$$
T_m\le T_{\mathrm{train}}.
$$

Rows that have entered the risk set but have not completed the outcome window are not silently labelled as non-defaults. The fixed-horizon HLR uses matured binary outcomes or a formally approved censoring treatment. The timing challenger in Part 2b uses the same ledgers to construct at-risk exposure intervals and right-censored event histories. This common source prevents the logistic and survival views from becoming two inconsistent credit histories.


# 5. Feature Engineering for the Gig Economy

Before feeding data into the neural architectures, raw telemetry and transactional logs must be engineered into financially meaningful feature vectors. The gig driver's risk profile demands features that capture liquidity constraints, operational stress, behavioral degradation, and structural macro exposure simultaneously.

## 5.1. High-Frequency Behavioral Stream (GRU Input Path)

**Kinematic features:** Speed EMA computed over 1-minute, 5-minute, and 15-minute trailing windows. Braking delta $\Delta|a_{\text{brake}}|$ (change in peak braking G-force between consecutive windows). Cornering lateral G-force. Angular velocity variance (yaw oscillation, indicative of fatigue-driven lane instability). These features collectively constitute the driver's real-time **operational stress signature**.

**Temporal session markers:** Consecutive driving hours within the current session (reset on breaks $> 30$ min). Shift-start time encoded as a cyclical feature: $\sin(2\pi h / 24)$, $\cos(2\pi h / 24)$ where $h$ is the hour of shift start. Hours since last 30-minute break. Circadian fatigue accumulation: integration of trailing 7-day hours driven during the driver's biological sleep window (the highest-stress but highest-surge-opportunity period).

**Permitted raw wallet-event sequence:** The GRU may observe a minimised sequence of event type, direction, amount bucket, and time gap when the data basis permits. It does not receive CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, cash-out ratio, reserve balance, time since depletion, or deterministic transformations of them. Those engineered concepts belong to the Explicit Liquidity Feature Path. This boundary lets the neural branch learn timing and rhythm without giving the downstream HLR two versions of the same named financial variable.

**Engineering transformations:** EMA decay, window size, thresholds, and clipping are versioned hyperparameters estimated from training evidence. Scaling parameters are fitted without validation or future leakage, then frozen for the model version or updated through a governed recalibration. A rolling global scaler does not prevent drift and can conceal it. Irregular sampling receives a mask, age-of-data, coverage, and reason code where available.

**Input tensor:** $\mathbf{X}^{\text{tele}} \in \mathbb{R}^{B \times T_{hf} \times d_{hf}}$ where $B$ is batch size, $T_{hf} = 14$ days (daily resolution lookback), and $d_{hf}$ is the telematics feature dimension.

## 5.2. Low-Frequency Structural Context (Transformer Input Path)

**Macroeconomic indicators:** Gas price index (7-day percentage change from 30-day trailing mean, removes level effects; captures rate-of-change signal). CPI-adjusted real wage index for the driver's metropolitan area (normalizes nominal earnings against purchasing power drift). Central bank policy rate (affects driver consumer demand through discretionary income compression).

**Platform configuration:** Surge dampening coefficient (weekly update frequency). Base fare floor percentage change from the previous month. New competitor market entry indicator (binary flag; entry of a new ride-hailing competitor typically compresses surge pricing across the market). Algorithmic matching elasticity (internal metric proxying the localized dispatch density).

**Regulatory environment:** Emissions zone restriction intensity for the driver's primary jurisdiction (ordinal encoding: 0 = no restriction, 1 = announced pricing, 2 = active tolling, 3 = complete combustion ban). Gig-worker classification statute status (binary: reclassified to employee status / independent contractor). Metropolitan vehicle permit utilization rate (fraction of total licensed permits currently active, a proxy for market saturation).

**Urban infrastructure:** Major corridor disruption indicator for geohashes where the driver operates more than 30% of their trips. Highway reconstruction duration in weeks (longer duration = permanent earning capacity depression for affected geohash corridors).

**Engineering:** Target encoding for categorical regulatory zone identifiers (smoothed target encoding using a Bayesian hierarchical mean to prevent overfitting to small jurisdiction groups). Percentage change from trailing 30-day average for all numerical macro indicators. **Input tensor:** $\mathbf{X}^{\text{macro}} \in \mathbb{R}^{B \times T_{lf} \times d_{lf}}$ where $T_{lf} = 24$ monthly tokens and $d_{lf}$ is the macro feature dimension.

## 5.3. Driver Liquidity and Solvency Features (Explicit Liquidity Feature Path)

**Architectural routing note: controlling redundancy**
The central vulnerability in a hybrid neural-Bayesian model is representation redundancy. The same raw event can legitimately be available to multiple services, but a named engineered liquidity metric must have one owner. Explicit metrics strictly bypass the neural encoders. Part 2b then residualises the neural representation against the explicit feature block out of fold, orthogonalises spline bases, and uses block shrinkage. These controls reduce instability and multicollinearity; identifiability still has to be tested.

Unlike slower contextual variables read from versioned lakehouse tables, the high-velocity Explicit Liquidity Features use a Kappa-style online path. Flink processes source events and materialises live state into a low-latency key-value store such as Redis. At decision time, the service fetches the latest valid versions and quality flags, routes them directly into the HLR, and records the feature timestamp and definition version. A sub-millisecond cache read is a performance target to be benchmarked, not a property guaranteed by selecting Redis.

**Wallet Cash-Flow Asymmetry (CFA):**

$$
\mathrm{CFA}_i(t)
=
\frac{
\operatorname{mean}\left(E_{i,d}:E_{i,d}\ge Q_{0.95,i}^{(w)}\right)
}{
\operatorname{median}\left(E_{i,d}:E_{i,d}>0\right)+\varepsilon
}.
$$

Here \(E_{i,d}\) is net settled daily earnings over window \(w\), and \(Q_{0.95,i}^{(w)}\) is the driver's 95th percentile. CFA is dimensionless. A large value means upper-tail earning days are much larger than the typical positive day; it does not by itself prove dependency or insolvency. Minimum observations, clipping, seasonality, and the relationship to downside sufficiency must be calibrated.

**Dynamic Debt-to-Liquidity Ratio (DLR):**

$$
\mathrm{DLR}^{(h)}_i(t)
=
\frac{D^{\mathrm{due}}_i(t,t+h)}
{W^{\mathrm{available}}_i(t)+R^{\mathrm{available}}_i(t)+S^{\mathrm{earned\ but\ pending}}_i(t)+\varepsilon}.
$$

The numerator is debt contractually due over horizon $h$, initially seven days. The denominator contains cash currently available for those obligations, any reserve amount legally and operationally available, and settlement already earned but pending when that feed is reliable. Assets with withdrawal restrictions are excluded or haircutted. DLR is dimensionless and horizon-matched. It does not divide total debt by a daily income average, which would mix maturity and liquidity concepts and duplicate more of Earnings Velocity.

**Repayment Velocity:**

$$
v_{\mathrm{repay},i}^{(h)}(t)
=
\frac{P^{\mathrm{principal\ paid}}_i(t-h,t)}
{P^{\mathrm{principal\ scheduled}}_i(t-h,t)+\varepsilon}.
$$

Fees, interest, reversals, prepayments, restructurings, and products with no scheduled principal receive explicit treatment. A zero scheduled denominator is “not applicable,” not evidence of failed repayment. The feature can be clipped for model stability while the raw ratio remains in the audit record.

**Wallet Cash Flow Volatility (\(\sigma_{\text{wallet}}\)):** A robust rolling dispersion measure of daily net settled earnings, reported with its window, scale, and missing-day rule. Two drivers with the same mean can have different liquidity risk. The direction and magnitude of the effect remain empirical because high variance can also accompany seasonal opportunity and strong buffers.

**Time Since Last Zero-Balance Event, Exponential Recency Decay:**
A complete wallet depletion yesterday carries exponentially more predictive weight regarding an impending IPF lapse than a depletion from 24 months prior. This recency structure is captured via dual encoding:

- **Decay transform:** \(e^{-\lambda\Delta T}\), where \(\Delta T=T_{\text{current}}-T_{\text{last depletion}}\) in days. The initial \(\lambda=0.01\) is a candidate, not a calibrated fact until cohort evidence is available.
- **Binary indicator:** $\mathbf{1}[\text{has\_prior\_observed\_depletion}]\in\{0,1\}$. The decay captures recency and the indicator distinguishes no observed depletion from a remote one. Neither proves permanent fragility, especially when wallet history is short or incomplete.

**Earnings Velocity ($\nu_{\text{earn}}$):** The ratio of average net settled earnings over the trailing seven days to the average over the preceding 90-day baseline:

$$
\nu_{\text{earn},i,t}
=
\frac{
\frac{1}{7}\sum_{d=t-6}^{t}E_{i,d}
}{
\frac{1}{N_B}\sum_{d=t-96}^{t-7}E_{i,d}
+\varepsilon
}.
$$

Here $N_B$ is the number of valid days in the preceding 90-day baseline, and missing or non-working days follow a documented rule. A value below one indicates recent earnings below the historical daily baseline, not necessarily suffocation; operating costs, obligations, seasonality, and buffers still matter. Its spline effect is learned rather than forced to be linear or monotonic.

**Reserve Pocket Balance (\(R_i(t)\)):** The driver-owned or contractually controlled reserve balance and a separately calculated ratio to due obligations. The feature registry must state ownership and availability. It is not the SPV Cash Reserve Account.

**Processing:** These features bypass the neural encoders. The governed main specification evaluates a moderately rich B-spline basis and applies a difference penalty, producing a P-spline effect whose roughness is controlled separately from knot count. The basis degree, boundary knots, interior knots, difference order, penalty matrix, centring transform, support range, clipping rule, and back-transformation are versioned in the feature registry. A QR or penalty-compatible reparameterisation may be used for numerical conditioning, but it must preserve the penalty's null space and interpretation. B-spline with RW1 and AR(1) coefficient priors remain documented challengers in Part 2b's appendix rather than disappearing from the research programme. Half-Student-\(t\) priors may be used for positive group scales, while coefficient blocks receive regularising shrinkage [10]-[12].

## 5.4. Gig-Economy Specific Interaction Effects

Standard credit models include generic interaction terms. In the gig-economy context, four specific pairwise interactions carry structural economic meaning. To prevent structural multicollinearity with the neural embeddings (which dynamically model implicit interactions), these four specific explicit interaction pairs (forming the set $\mathcal{G}$) **strictly bypass the neural encoder**. They are routed directly to the Hierarchical Bayesian Logistic Regression layer as orthogonal linear terms:

1. **High revolving utilisation \(\times\) prior delinquency:** A strong-heredity interaction testing whether utilisation is more informative after delinquency. The 0.80 threshold is an illustrative policy knot, not a universal boundary or a diagnosis of income supplementation.

2. **Platform commission increase \(\times\) high DLR:** Tests whether a commission change has a larger effect where due obligations already consume liquidity. DLR values such as 0.90 and 1.00 are candidate spline knots pending product and outcome calibration.

3. **Late-night driving concentration \(\times\) microloan arrears:** Tests whether arrears and a change in working hours jointly predict risk. It is not labelled "desperation" because night work may be an ordinary preference or market response. The feature requires a within-driver baseline and careful fairness review.

4. **ZEV mandate proximity \(\times\) ICE vehicle ownership:** Represents a scenario interaction only where a verified rule, date, jurisdiction, and affected vehicle class exist. It should not manufacture a mandate or deactivation event from an announcement.


# 6. The Dual-Regime Neural Architecture

The multi-scale feature extraction architecture processes the two neural feature streams - telematics (GRU) and macro (Transformer) - in parallel and fuses their outputs into a single high-dimensional covariate vector $\boldsymbol{\Phi}_{it}$. The financial liquidity variables completely bypass this neural network and are fed directly into the downstream Hierarchical Bayesian Logistic Regression engine alongside $\boldsymbol{\Phi}_{it}$, as illustrated in **Figure 2**.

**Figure 2: The Dual-Regime Neural Architecture**

```{.mermaid layout=fullpage}
%%{init: {"flowchart": {"defaultRenderer": "elk", "curve": "basis", "nodeSpacing": 50, "rankSpacing": 50}}}%%
graph TD
    %% Input Streams
    subgraph InputLayer [Input Feature Streams]
        TeleInput[High-Freq Raw Sequences<br/>Kinematics, sessions, permitted wallet events<br/>No engineered liquidity metrics]
        MacroInput[Low-Freq Macro / RegulatoryGas Price, Emissions Zone, MatchingTensor: B × T_lf × d_lfT_lf = 24 months]
    end

    %% GRU Branch
    subgraph GRUBranch [Branch 1: GRU Short-Term State]
        Mask[Masking Layermask_value=0.0Handles irregular sampling]
        GRU1[GRU Layerhidden_dim=128update gate z_treset gate r_t]
        Drop1[Dropout 0.30]
        H_T[Terminal Hidden State<br/>h_T_GRU ∈ ℝ^128<br/>Short-Term State Embedding]
    end

    %% Transformer Branch
    subgraph TransBranch [Branch 2: Transformer Long-Term Context]
        PosEnc[Positional EncodingSinusoidal: sin/cos month index]
        MHA[Multi-Head Self-Attention4 heads, d_k = embed_dim / 4Attention Q,K,V = softmax QK^T/√d_k V]
        ResNorm1[Add & Layer Norm 1]
        FFN[Feed-Forward NetworkSwiGLU Architecturehidden = embed_dim × 4 / 3, SiLU]
        ResNorm2[Add & Layer Norm 2]
        GAP[Global Average Poolingover time dimension]
        C_L[Context Vectorc_L,τ ∈ ℝ^128Macro Regime Embedding]
    end

    %% Async Clock Coupling
    subgraph AsyncClock [Asynchronous Clock Coupling]
        Registry[Low-Freq RegistryHolds c_L,τ until next monthly run]
        DailyPick[Daily Pick-UpUse last committed c_L,τ]
    end

    %% Cross-Attention Fusion Layer
    subgraph FusionLayer [Cross-Attention Fusion Layer]
        CA[Cross-AttentionQuery: h_T_GRUKey/Value: c_L,τMultiheadAttention batch_first=True]
        Concat[ConcatenateFused Vector]
        Linear_Fuse[Linear Projection→ d_phi]
        PHI[Φ_it ∈ ℝ^d_phiComplete Time-Varying CovariateFeeds Bayesian Engine]
    end

    %% Connections
    TeleInput --> Mask
    Mask --> GRU1
    GRU1 --> Drop1
    Drop1 --> H_T

    MacroInput --> PosEnc
    PosEnc --> MHA
    MHA --> ResNorm1
    ResNorm1 --> FFN
    FFN --> ResNorm2
    ResNorm2 --> GAP
    GAP --> C_L
    C_L --> Registry
    Registry --> DailyPick

    H_T --> CA
    DailyPick --> CA
    CA --> Concat
    Concat --> Linear_Fuse
    Linear_Fuse --> PHI

    %% Styling
    style InputLayer fill:#2c3e50,color:#fff
    style GRUBranch fill:#2980b9,color:#fff
    style TransBranch fill:#8e44ad,color:#fff
    style FusionLayer fill:#e67e22,color:#fff
    style AsyncClock fill:#2c3e50,color:#fff
    style PHI fill:#27ae60,color:#fff
```


## 6.1. Branch 1: Gated Recurrent Units for Short-Term Latent State

The GRU processes the high-frequency telematics tensor $\mathbf{X}^{\text{tele}} = [\mathbf{x}_1^{\text{tele}}, \ldots, \mathbf{x}_{T_{hf}}^{\text{tele}}]$ sequentially, maintaining a hidden state $\mathbf{h}_t^{\text{GRU}} \in \mathbb{R}^{d_1}$ that accumulates the driver's behavioral trajectory. At each time step $t$, the GRU executes:

**Update gate:** determines how much of the previous hidden state to carry forward:
$$\mathbf{z}_t = \sigma(\mathbf{W}_z \mathbf{x}_t^{\text{tele}} + \mathbf{U}_z \mathbf{h}_{t-1}^{\text{GRU}} + \mathbf{b}_z)$$

**Reset gate:** controls how much of the previous hidden state is relevant to the candidate:
$$\mathbf{r}_t = \sigma(\mathbf{W}_r \mathbf{x}_t^{\text{tele}} + \mathbf{U}_r \mathbf{h}_{t-1}^{\text{GRU}} + \mathbf{b}_r)$$

**Candidate hidden state:** the proposed new content for the hidden state, modulated by the reset gate:
$$\tilde{\mathbf{h}}_t = \tanh(\mathbf{W}_h \mathbf{x}_t^{\text{tele}} + \mathbf{U}_h (\mathbf{r}_t \odot \mathbf{h}_{t-1}^{\text{GRU}}) + \mathbf{b}_h)$$

**Final hidden state:** interpolation between old and candidate states, controlled by the update gate:
$$\mathbf{h}_t^{\text{GRU}} = (1-\mathbf{z}_t) \odot \mathbf{h}_{t-1}^{\text{GRU}} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

where $\sigma(\cdot)$ denotes the sigmoid function and $\odot$ the Hadamard (element-wise) product. The weight matrices $\mathbf{W}_z, \mathbf{W}_r, \mathbf{W}_h \in \mathbb{R}^{d_1 \times d_{hf}}$ operate on the input, while $\mathbf{U}_z, \mathbf{U}_r, \mathbf{U}_h \in \mathbb{R}^{d_1 \times d_1}$ operate on the recurrent state.

At the end of the evaluation window \(T_{hf}\), the terminal hidden state \(\mathbf h_T^{\mathrm{GRU}}\) is a compressed short-term representation of permitted sequence information. It may encode combinations of session duration, kinematic change, trip rhythm, and event timing. It is not interpreted as a "desperation profile," and it does not own declining Earnings Velocity. Its economic content is investigated through controlled probes and ablation, while the downstream HLR receives only its redundancy-controlled residual representation.

The GRU is the initial candidate because it is parameter-efficient and suitable for bounded sequential windows. LSTM, temporal convolution, simpler state-space, and non-neural baselines remain challengers. Model choice follows calibrated out-of-time decision value, stability, fairness, latency, and cost rather than an assumed universal performance advantage.

## 6.2. Branch 2: Multi-Head Self-Attention Transformers for Long-Term Context

The Transformer branch processes the low-frequency structural context sequence $\mathbf{X}^{\text{macro}}$, such as a 24-month history of macro indicators, regulatory changes, and authorised platform configuration evidence. Unlike the GRU, which processes tokens recurrently, self-attention can create direct paths among positions in the context window. This can help represent long-range relationships, but it does not eliminate all optimisation problems or prove that an event 18 months ago caused a current risk state.

**Positional encoding** is applied before the attention layers to inject temporal ordering information that the position-agnostic attention mechanism cannot infer from content alone:

$$\text{PE}(\text{pos}, 2i) = \sin\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right), \quad \text{PE}(\text{pos}, 2i+1) = \cos\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right)$$

The core computation is scaled dot-product attention. The input sequence is linearly projected into Query ($\mathbf{Q}$), Key ($\mathbf{K}$), and Value ($\mathbf{V}$) matrices, each of dimension $d_k$:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

The $\sqrt{d_k}$ scaling term prevents the dot products from growing in magnitude with embedding dimension, which would push the softmax into saturation regions with near-zero gradients. With $H = 4$ parallel attention heads, the multi-head variant runs 4 independent attention computations on projected subspaces of dimension $d_k = d_{\text{model}} / H$ and concatenates the results, allowing different heads to specialize on different structural dependencies, one head may learn to track platform commission regime changes, another to track ZEV mandate escalation trajectories, another to track macro fuel price cycles.

Each Transformer block follows a pre-norm architecture: Layer Normalization $\rightarrow$ Attention $\rightarrow$ Residual Add $\rightarrow$ Layer Normalization $\rightarrow$ **SwiGLU Feed-Forward Network (SiLU activation)** $\rightarrow$ Residual Add [13], [14]. The legacy ReLU activation is replaced by the smooth, non-monotonic **SiLU (Swish)** function ($f(x) = x \cdot \sigma(x)$). By dynamically gating the linear projections, SwiGLU preserves subtle negative macroeconomic signals and provides superior representational capacity and smooth gradient flow compared to standard two-layer FFNs. Global average pooling over the time dimension aggregates the $T_{lf}$ token representations into a single dense context vector $\mathbf{c}_L \in \mathbb{R}^{d_2}$.

## 6.3. Asynchronous Dual-Rate Clock Coupling

The GRU operates on a daily cycle: at midnight, the system processes the day's accumulated telematics and wallet vectors to produce $\mathbf{h}_t^{\text{GRU}}$. The Transformer operates on a monthly cycle (or event-triggered cycle upon receipt of a new macro/regulatory update): it ingests the updated 24-month token sequence and generates a new context vector $\mathbf{c}_{L,\tau+1}$.

The **low-frequency registry** holds the last completed Transformer output $\mathbf{c}_{L,\tau}$ as a static vector. At any given day $t$, the daily GRU pipeline queries the registry, retrieves $\mathbf{c}_{L,\tau}$ (the context from the last monthly run), and passes it to the fusion layer alongside $\mathbf{h}_t^{\text{GRU}}$:

$$\mathbf{e}_{it} = [\mathbf{h}_t^{\text{GRU}} \parallel \mathbf{c}_{L,\tau}]$$

The zero-order hold avoids recomputing the Transformer every day and lets the daily path use the most recent approved context vector. Point-in-time correctness still depends on the input versions and publication availability used to create \(\mathbf c_{L,\tau}\). A stale-context flag and maximum age are therefore stored with the vector.

## 6.4. Cross-Attention Feature Fusion

Naive concatenation \(\boldsymbol{\Phi}_{it}=[\mathbf h_T^{\mathrm{GRU}}\parallel\mathbf c_{L,\tau}]\) does not explicitly model relationships between the two neural streams. If short-term operation changes during a fuel-price regime, a learned fusion may add value. Explicit financial indicators are intentionally absent from this fusion and enter the HLR through their own path.

**Cross-attention fusion** resolves this: the GRU output $\mathbf{h}_T^{\text{GRU}}$ serves as the **Query** (the question: "given my current behavioral state, which structural factors are most relevant?"). The Transformer vector $\mathbf{c}_{L,\tau}$ serves as the **Keys and Values** (the structural factors available to condition on). The cross-attention mechanism assigns dynamic attention weights that amplify macro-structural context precisely when the behavioral state signals imminent cascade onset. The result is projected through a linear layer to produce the final fused covariate vector $\boldsymbol{\Phi}_{it} \in \mathbb{R}^{d_\phi}$.


# 7. Handling Asynchronous Clock Cycles and Missing Data
## 7.1. Missing-data strategies and missingness mechanisms

Underwriting streams can be missing because a source is unavailable, a driver is new, consent is absent, a device is incompatible, a platform integration failed, the event did not occur, or the value depends on an unobserved state. Missingness may be MCAR, MAR, or MNAR. It must not be interpreted as intentional concealment without evidence. A missingness indicator can capture operational pattern, but may also proxy device, platform, geography, or income and therefore requires fairness, lawful-processing, and data-quality review [15].

- **Strategy A, Learned Masking Embedding Tokens:** For every low-frequency input feature $x_k$, a binary indicator $m_k \in \{0, 1\}$ is appended, where $m_k = 1$ signals a missing value. Both are passed through the Transformer's input projection layer:

  $$z_k = W_x x_k + W_m m_k$$

  The Transformer can learn whether a missingness pattern adds stable signal. The indicator is not labelled as concealment. Source, consent, outage, applicability, and age-of-data reason codes should be supplied where possible so operational failure is not mistaken for borrower risk.

- **Strategy B, Bayesian generative imputation:** For approved variables and a defensible missingness model, missing values can be treated as unknowns rather than fixed means. A hierarchical prior may use broader cohort information:

  $$X_{\text{missing},j} \sim \mathcal{N}(\mu_{\gamma_j}, \sigma_{\gamma_j}^2)$$

  Joint inference can propagate imputation uncertainty into PD, but a wider interval is an expected tendency rather than a guaranteed ordering for every record. The Credit Policy and Compliance Gate applies an uncertainty rule whose action depends on product, reason for missingness, available alternatives, and consumer impact.

- **Strategy C - validated fallback engines:** Maintain an explicit-only baseline, full hybrid model, GRU-plus-explicit challenger, and Transformer-plus-explicit challenger. The router selects only a version validated for the observed availability pattern. Wider uncertainty is passed to the policy gate; an outage does not automatically penalise a driver if a safe explicit-only decision is available.

## 7.2. The Feature Fusion Vector as the Interface to Bayesian Inference

At each defined evaluation interval, the fusion layer outputs \(\boldsymbol{\Phi}_{it}\), a neural representation of short-term sequence and longer structural context. Before it reaches the HLR, Part 2b residualises it against the explicit and metadata blocks out of fold. The Explicit Liquidity Features enter separately through centered and orthogonalised spline and interaction bases.

Part 2b begins at that interface. It preserves the narrative ambition of a full posterior distribution, but calibrates the HLR so that dimensionality, redundancy, multicollinearity, hierarchy, and out-of-time uncertainty are controlled rather than hidden.

The boundary is implemented as a signed **model-input artifact**, not an informal tensor handoff. For every score it carries the observation-unit key, product and horizon, decision timestamp, explicit-feature values and versions, P-spline basis version, raw and residual neural artifact versions, metadata and quality flags, feature support indicators, missingness reasons, source ages, and a snapshot manifest. Training also stores the fold-specific residualisation and scaling transformations. Production stores the approved full-development transformations and a numerical parity hash.

The online service never estimates a posterior or refits a residualisation model during the request. It applies the approved feature definitions, basis, projection, calibration, and posterior scoring artifact. A parity suite replays representative observations through offline and online implementations and compares explicit features, basis rows, residual embeddings, linear predictors, calibrated PDs, uncertainty summaries, and reason contributions within approved tolerances. A mismatch routes to the explicit-only fallback or manual process rather than becoming an invisible model change.



```{=latex}
\clearpage
```

## References

[1] K. Cho *et al*., "Learning phrase representations using RNN encoder-decoder for statistical machine translation," arXiv:1406.1078, 2014. [Online]. Available: https://arxiv.org/abs/1406.1078. Accessed: Aug. 25, 2026.

[2] A. Vaswani *et al*., "Attention is all you need," in *Advances in Neural Information Processing Systems 30*, 2017. [Online]. Available: https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf. Accessed: Aug. 25, 2026.

[3] Debezium Authors, "Debezium connector for PostgreSQL," *Debezium Documentation*. [Online]. Available: https://debezium.io/documentation/reference/stable/connectors/postgresql.html. Accessed: Aug. 25, 2026.

[4] Apache Software Foundation, "Design," *Apache Kafka Documentation*. [Online]. Available: https://kafka.apache.org/documentation/#design. Accessed: Aug. 25, 2026.

[5] Apache Software Foundation, "Timely stream processing," *Apache Flink Documentation*. [Online]. Available: https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/. Accessed: Aug. 25, 2026.

[6] Apache Iceberg Authors, "Apache Iceberg documentation." [Online]. Available: https://iceberg.apache.org/docs/latest/. Accessed: Aug. 25, 2026.

[7] Central Bank of Kenya, "Statistics." [Online]. Available: https://www.centralbank.go.ke/statistics/. Accessed: Aug. 25, 2026.

[8] World Bank, "API basic call structures," *World Bank Data Help Desk*. [Online]. Available: https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures. Accessed: Aug. 25, 2026.

[9] International Monetary Fund, "IMF Data APIs." [Online]. Available: https://data.imf.org/en/Resource-Pages/IMF-API. Accessed: Aug. 25, 2026.

[10] A. Gelman, "Prior distributions for variance parameters in hierarchical models," *Bayesian Analysis*, vol. 1, no. 3, pp. 515-534, 2006.

[11] C. M. Carvalho, N. G. Polson, and J. G. Scott, "The horseshoe estimator for sparse signals," *Biometrika*, vol. 97, no. 2, pp. 465-480, 2010.

[12] J. Piironen and A. Vehtari, "Sparsity information and regularization in the horseshoe and other shrinkage priors," *Electronic Journal of Statistics*, vol. 11, no. 2, pp. 5018-5051, 2017, doi: 10.1214/17-EJS1337SI.

[13] N. Shazeer, "GLU variants improve Transformer," *arXiv preprint arXiv:2002.05202*, 2020.

[14] H. Touvron *et al*., "LLaMA: Open and efficient foundation language models," *arXiv preprint arXiv:2302.13971*, 2023.

[15] Republic of Kenya, *Data Protection Act, 2019*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24. Accessed: Aug. 25, 2026.
