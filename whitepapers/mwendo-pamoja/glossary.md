# Reader's Guide: Disciplines, Terms, and Mathematical Notation

## How to use this guide

Mwendo Pamoja follows one economic event through several institutional worlds. A fuel-price increase, vehicle interruption, platform commission change, or reduction in trip demand first affects the driver's operating cash flow. It then appears in wallet and telematics data, enters a governed underwriting process, activates a policy response, changes accounting and portfolio measures, and may ultimately affect the SPV's collections and lender cash flows. No single professional discipline owns that entire chain.

This guide has two layers. The first is an interdisciplinary field map showing where the white paper draws from economics, insurance, finance, statistics, technology, law, accounting, and operations. The second is an alphabetical technical glossary defining the paper's principal terms and symbols in their Mwendo Pamoja context. A definition here is a navigational aid, not a substitute for the fuller discussion, qualifications, equations, or IEEE sources in Parts 1 through 6.

Terms are defined according to their intended role in this architecture. In particular, the neural representation, Explicit Liquidity Feature Path, Bayesian underwriting layer, and Credit Policy and Compliance Gate are separate components. Similarly, customer pricing, SPV note pricing, accounting impairment, prudential capital, and market-consistent valuation are related but distinct calculations.

## Interdisciplinary field map

### Economics and the driver's operating reality

The paper begins in microeconomics rather than in model architecture. It treats a gig driver as a small income-producing enterprise whose labour, vehicle, insurance, liquidity, and platform access are mutually dependent. Household finance explains reserve depletion and short-term borrowing; labour and platform economics explain variable work opportunities and commissions; behavioural economics informs repayment and intervention design. Macroeconomics, monetary economics, fuel-price exposure, urban mobility, and the transition toward lower-emission vehicles provide the external conditions under which the driver operates. Development economics and financial inclusion supply the broader question: whether finance can preserve productive capacity without converting continuous observation into continuous punishment.

### Lending, insurance, and embedded-finance product design

Mwendo Pamoja combines digital lending, microfinance, revolving credit, insurance premium financing, and usage-sensitive insurance within an embedded-finance experience. These disciplines meet at origination, affordability assessment, limit management, premium funding, collections, restructuring, and servicing. Insurance and lending remain legally and economically distinct. The insurer receives premium under the applicable insurance arrangement; the IPF lender holds a finance receivable against the driver; and the SPV may acquire only eligible receivables and rights that can legally be transferred. Continuous underwriting updates risk between conventional application or renewal dates, while the policy layer determines which operational response is permitted.

### Project finance, structured finance, and institutional capital

The financing proposition draws on project finance, structured finance, securitisation, fixed-income analysis, and corporate finance. HoldCo owns and develops the operating capability, while a ring-fenced SPV purchases eligible receivables and allocates collections through a priority of payments. Senior debt, mezzanine debt, and first-loss equity form the capital stack. Overcollateralisation, a cash reserve account, subordination, asset eligibility, concentration limits, recovery rights, covenants, and early amortisation provide structural protection. Lender underwriting evaluates debt service, liquidity, losses, recovery timing, and stress performance rather than relying on an unsupported claim of principal protection.

### Treasury, pricing, and balance-sheet management

KESONIA connects monetary conditions to customer and institutional pricing. The paper therefore covers benchmark compounding, risk-based credit pricing, expected loss, funding margins, net interest margin, liquidity ladders, asset-liability management, and matched-funding attribution. It distinguishes the customer's lending rate from the SPV asset yield, Class A and Class B note margins, internal or analytical funds-transfer prices, investor hurdle rates, and valuation discount rates. Interest-rate risk, foreign-exchange exposure, reserve cash drag, behavioural maturity, and collection timing are treated as cash-flow questions. IRRBB remains a prudential banking concept even when the SPV faces analogous repricing and basis risks.

### Mathematics, statistics, and quantitative risk

The underwriting design combines probability theory, hierarchical Bayesian statistics, logistic regression, nonlinear splines, time-varying effects, shrinkage priors, and posterior computation. Linear algebra appears through QR orthogonalisation, whitening, projections, and Cholesky factorisation. MCMC diagnostics, posterior predictive checks, calibration, discrimination, and out-of-time validation govern whether the model is usable. Copulas and tail-dependence measures address correlated product losses. Structural and reduced-form credit models appear as valuation and methodological comparators. Decision theory converts posterior risk and uncertainty into an action only after costs and policy constraints are made explicit.

### Artificial intelligence and responsible model use

Deep learning is used for temporal representation, not as an unconstrained final decision-maker. GRUs encode short-horizon operational sequences; Transformers encode longer-horizon context; attention mechanisms align information arriving at different frequencies. Explicit financial variables have a separate owner and enter the Bayesian layer directly. Cross-fitted residualisation, a narrow bottleneck, whitening, block-specific priors, ablation tests, and stability checks reduce duplicate signal. Explainability, fairness assessment, customer reason codes, model-risk governance, challenger testing, and human review address how predictive systems should be governed rather than merely how they can be built.

### Data engineering, telematics, and computation

The data architecture spans edge capture, vehicle telematics, mobile and wallet events, change-data capture, durable streaming, stateful event-time processing, and lakehouse storage. Kafka, Flink, Debezium, Redis-style serving, and Bronze, Silver, and Gold layers illustrate the required functions. Bitemporal records and as-of joins preserve point-in-time correctness. Missingness, late events, identity resolution, data lineage, quality controls, and replay determine whether a model result can be reproduced. SQL supports benchmark-rate compounding and accounting interfaces, while GPU or TPU computation is a possible acceleration mechanism for posterior inference rather than an architectural requirement.

### Accounting, prudential risk, law, and assurance

IFRS 9 connects instrument-level evidence to staging, expected credit loss, modifications, write-offs, and recoveries. IFRS 17 remains an insurer-accounting interface rather than an SPV receivable rule. Basel capital and IRRBB are bank-owned prudential workstreams. Kenyan banking, digital-credit, insurance, capital-markets, consumer-protection, and data-protection requirements determine what the parties may originate, transfer, process, explain, and report. True sale, enforceability, perfection, account control, insolvency analysis, and servicing continuity support the SPV structure. Audit trails, maker-checker approval, immutable records, encryption, signatures, and reconciliation provide complementary forms of assurance.

### Enterprise systems, cybersecurity, and operating controls

Enterprise architecture links product services and subledgers to Microsoft Dynamics 365 Finance without making the general ledger perform every instrument-level calculation. Oracle OFSAA is discussed as an optional institutional mechanism for cash-flow modelling, ALM, and FTP where scale and governance justify it. Cybersecurity includes encryption, public-key infrastructure, mutual authentication, access control, evidence retention, and safe degradation. Reliability engineering, reconciliation, service levels, backup servicing, and business continuity ensure that a valid model result can become a controlled operational and accounting event.

### Product delivery, governance, and institutional change

The implementation roadmap draws on product management, service design, human-centred research, operational-risk management, programme delivery, pilot design, change management, and due diligence. It assigns decision rights among the driver, platform, lender, insurer, servicer, SPV, trustee, account bank, investors, model developers, validators, finance teams, and regulators. Scale is stage-gated. A more complex model or larger financing structure is promoted only after the baseline, data lineage, customer treatment, cash movements, accounting, and validation evidence remain stable.

## Mathematical notation at a glance

- **\(\mathbb P\):** The physical or real-world probability measure used for underwriting, portfolio risk, stress evidence, and IFRS 9 inputs.
- **\(\mathbb Q\):** A risk-neutral or market-consistent measure used only for an appropriate valuation purpose with a defensible calibration basis.
- **\(\mathbf z_i\):** The original Explicit Liquidity Feature vector for observation \(i\).
- **\(\mathbf q_i=Q(\mathbf z_i)\):** The centred, scaled, and QR-orthogonalised spline representation of the Explicit Liquidity Features.
- **\(\mathbf h_i\):** The low-dimensional neural embedding before residualisation.
- **\(\widetilde{\mathbf h}_i\):** The cross-fitted residual neural embedding after removing the component predicted by explicit liquidity and approved metadata.
- **\(\mathbf m_i\) or \(\mathbf x_i\):** Approved contract, product, data-quality, and other essential metadata, according to the notation used in the relevant specification.
- **\(\boldsymbol\beta_z\) and \(\boldsymbol\beta_h\):** Coefficients for the explicit-liquidity and residual-neural blocks.
- **\(PD\), \(LGD\), and \(EAD\):** Probability of default, loss given default, and exposure at default.
- **\(EL\):** Expected loss over a stated horizon, ordinarily derived from consistent PD, LGD, and EAD definitions.
- **\(K_{\mathrm{RBCP}}\):** The customer-pricing premium over KESONIA under the applicable risk-based credit-pricing formulation.
- **\(K_{\mathrm{cap}}\):** Regulatory or economic capital notation, deliberately distinct from \(K_{\mathrm{RBCP}}\).
- **\(m_A\) and \(m_B\):** Negotiated margins for the Class A and Class B notes.
- **\(\lambda_L\) and \(\lambda_U\):** Lower-tail and upper-tail dependence coefficients.

## Alphabetical technical glossary

```{=latex}
\begingroup
\footnotesize
\setstretch{1.08}
\setlength{\parskip}{0.32em}
\raggedcolumns
\begin{multicols}{2}
```

### A

**Advance rate.** The proportion of an eligible receivable pool that a financing facility is willing to fund. It must be distinguished from overcollateralisation because the two tests can use different denominators. In the SPV model, the applicable asset definition, haircut, and debt basis must be stated explicitly. See Parts 1 and 5.

**Algorithmic matching elasticity.** A measure or proxy describing how responsive a platform's trip allocation or matching activity is to changes in driver supply, passenger demand, geography, time, or platform policy. It is contextual information, not a protected characteristic and not automatically a causal estimate. See Part 2a.

**Algorithmic redlining.** A pattern in which a model or policy produces unjustified exclusion or materially worse treatment for protected or vulnerable groups, potentially through proxy variables such as geography. The paper addresses it through feature governance, fairness testing, reason review, less discriminatory alternatives, and human oversight. See Parts 2b and 3.

**AR(1) prior.** A first-order autoregressive prior in which a current time effect depends on the preceding effect plus innovation noise. It can represent persistence in cohort or calendar effects and can smooth adjacent spline coefficients. It is a modelling choice that requires stability and sensitivity testing. See Part 2b.

**As-of join.** A temporal join that matches each observation only to information available by the decision timestamp. It is essential when telemetry, wallet, platform, macroeconomic, and regulatory data arrive on different clocks. See Part 2a.

**Asset-liability management (ALM).** The measurement and management of timing, repricing, currency, liquidity, and behavioural differences between assets and funding obligations. For the SPV, it means a receivable and waterfall cash-flow ladder; for the partner bank, it may also form part of prudential balance-sheet management. See Part 5.

**Assistive intervention.** A controlled action intended to preserve the driver's productive capacity or prevent avoidable deterioration, such as a temporary payment adjustment, premium holiday, micro-reward bridge, routing support, or draw restriction. Its eligibility, accounting effect, customer communication, and policy authority must be recorded. See Part 3.

**Asymmetric copula.** A dependence model that permits stronger association in one tail of a joint distribution than in the other. The Clayton copula is considered because joint distress may be more pronounced than joint favourable outcomes. Selection remains an empirical portfolio question. See Part 2b.

### B

**Bankruptcy remoteness.** The degree to which SPV assets and cash flows are insulated from the insolvency of the originator or sponsor. It depends on legal transfer, enforceability, perfection, separateness, account control, servicing continuity, commingling and set-off analysis, and applicable insolvency law. The label SPV does not create remoteness by itself. See Parts 1, 5, and 6.

**Basel framework.** International prudential standards for bank capital, risk management, disclosure, and related controls. In this paper, Basel calculations and approvals remain responsibilities of the regulated partner bank. They are not automatically obligations of the SPV or technology provider. See Parts 3 and 5.

**Behavioural maturity.** The expected timing of an asset or liability's cash flows after considering borrower behaviour such as prepayment, redraw, delinquency, restructuring, or tenor extension. It may differ from contractual maturity and is important to ALM and stress testing. See Part 5.

**Bitemporal data.** Data carrying both valid time, when a fact was economically effective, and system time, when the platform recorded or learned it. Bitemporality supports reproducibility, correction handling, and point-in-time model reconstruction. See Parts 2a and 6.

**Brier score.** The mean squared difference between a predicted probability and the observed binary outcome. It reflects both calibration and resolution and should be interpreted alongside product horizon, class balance, discrimination, and operational decision value. See Part 2b.

**B-spline.** A locally supported piecewise-polynomial basis used to model a smooth nonlinear relationship without imposing abrupt bins. The paper applies centred and regularised spline bases to selected Explicit Liquidity Features. Knot placement, extrapolation, and smoothing remain governed modelling decisions. See Part 2b.

### C

**Calibration.** Agreement between predicted probabilities and observed outcome frequencies over a defined product, population, and horizon. A model may discriminate well but remain poorly calibrated. Mwendo Pamoja therefore tests calibration by product, cohort, time, and relevant groups. See Part 2b.

**Capital stack.** The ordered combination of Class A senior debt, Class B mezzanine debt, and Class C first-loss equity used to finance the SPV. Subordination determines which class absorbs loss or receives cash first under the waterfall. See Parts 1 and 5.

**Cash Reserve Account (CRA).** A controlled SPV account maintained to cover a defined number of months or amount of debt service, fees, or other senior obligations. Its target, permitted uses, replenishment order, release conditions, and investment treatment must be contractual. See Part 5.

**Cash-flow asymmetry (CFA).** An Explicit Liquidity Feature measuring the imbalance between unusually large positive wallet inflows and the driver's ordinary earnings base. Its exact numerator, denominator, window, winsorisation, and treatment of reversals must be specified before use. CFA bypasses the GRU and Transformer encoders and enters the Bayesian layer directly. See Part 2a.

**Champion-challenger framework.** A governance process in which a production model is compared with credible alternatives under the same data, horizon, and acceptance criteria. The explicit-only model remains a valid champion unless neural or dependence challengers demonstrate stable incremental value. See Parts 2b and 6.

**Change data capture (CDC).** The capture of database inserts, updates, and deletes as an ordered event stream. Debezium is used as an architectural example. CDC supports auditability and replay but does not by itself guarantee correct economic timestamps or complete source data. See Part 2a.

**Clayton copula.** An Archimedean copula with lower-tail dependence and no upper-tail dependence in its standard bivariate form. It is a candidate for modelling joint deterioration across products, subject to held-out fit, tail calibration, stability, and cash-flow relevance. See Part 2b.

**Collections account.** A controlled bank account into which borrower or platform deductions are directed before allocation through servicing and SPV rules. Account ownership, control, reconciliation, commingling protection, refund handling, and waterfall treatment must be documented. See Parts 1 and 5.

**Continuous underwriting.** The governed reassessment of risk as new authorised operational, wallet, repayment, and contextual evidence becomes available. It supplements rather than erases contractual rights, customer notice, fairness review, accounting governance, and policy controls. See Parts 1 through 3.

**Copula.** A function that joins marginal distributions into a multivariate distribution and isolates a chosen form of dependence. A copula does not repair miscalibrated marginal PDs, prove causality, or automatically determine regulatory capital. See Part 2b.

**Credit Policy and Compliance Gate.** The downstream rule layer that receives posterior risk, uncertainty, explicit features, exposure, concentration, reserve, and covenant information and returns an authorised action. It contains contractual, regulatory, policy, and operational controls. It is neither a neural model nor another feature service. See Parts 2b, 3, and 6.

**Cross-attention.** An attention mechanism in which one representation supplies queries and another supplies keys and values. It is used conceptually to align short-horizon driver state with longer-horizon contextual information. See Part 2a.

**Cross-fitted residualisation.** The removal from a neural embedding of the component predicted by explicit liquidity features and approved metadata, using a projection trained without the observation's validation fold. It reduces duplicate signal and leakage but does not guarantee permanent orthogonality under a new regime. See Parts 2b and 6.

### D

**Data lineage.** The traceable path from a source event through transformations, features, model versions, policy decisions, accounting entries, and reports. Lineage supports reproducibility, audit, complaints handling, and controlled correction. See Parts 2a, 4, and 6.

**Debt service coverage ratio (DSCR).** Cash available for debt service divided by the debt service due over the same period and under a stated waterfall definition. The numerator, reserve use, taxes, fees, and principal schedule must be explicit. See Part 5.

**Debezium.** An open-source change-data-capture platform used in the paper as an example of how operational database changes can enter a durable event stream. It is a component choice, not the source of legal authority or economic meaning. See Part 2a.

**Default cascade.** A feedback process in which an external shock reduces driver cash flow, causes arrears or insurance disruption, threatens platform access, and increases the likelihood of default across several products. It is a systems hypothesis to be measured rather than assumed universal. See Part 1.

**Disparate Impact Ratio (DIR).** A group fairness statistic comparing the rate of a favourable outcome between groups. It can flag potential disparity but does not, by itself, establish legal discrimination, fairness, or causal mechanism. See Parts 2b and 3.

**Dynamic Debt-to-Liquidity Ratio (DLR).** Short-horizon debt obligations divided by a governed measure of available wallet liquidity. It is an Explicit Liquidity Feature and may enter the HLR through a nonlinear spline. Its obligations, liquidity exclusions, horizon, and zero-denominator treatment require specification. See Parts 2a and 2b.

**Dynamics 365 Finance (D365).** The enterprise resource-planning endpoint used for approved journals, legal-entity accounting, dimensions, consolidation, workflow, and reporting. Product subledgers and governed engines may retain instrument-level calculations that D365 cannot represent natively. See Part 4.

### E

**Earnings Velocity.** An Explicit Liquidity Feature comparing recent net earnings with a longer historical baseline. It indicates acceleration or deterioration in earnings capacity. It belongs to the direct liquidity path rather than being duplicated as a defined GRU input. See Part 2a.

**Effective interest rate (EIR).** The IFRS 9 rate that exactly discounts estimated contractual cash flows over an instrument's expected life to its initial gross carrying amount, subject to the standard's requirements. It is not interchangeable with KESONIA, the customer rate, or the investor hurdle. See Parts 4 and 5.

**Effective sample size (ESS).** The amount of independent-equivalent posterior information contained in autocorrelated MCMC draws. ESS is assessed for relevant parameters and quantities together with convergence, divergences, and Monte Carlo error. See Part 2b.

**Eligible receivable.** A receivable satisfying contractual purchase criteria relating to ownership, documentation, performance, data quality, currency, product, concentration, policy status where relevant, and absence of prohibited encumbrances. Insurer-owned premium cash is not an eligible loan receivable. See Parts 1, 5, and 6.

**Embedded finance.** The delivery of a financial product within a non-financial operating journey, such as a driver or mobility platform. Embedding changes distribution and data access but does not remove licensing, conduct, accounting, or contractual responsibilities. See Part 1.

**Equalized odds.** A fairness criterion requiring equal true-positive and false-positive rates across specified groups, conditional on the observed outcome. It can conflict with calibration or other objectives when base rates differ and must be applied in a legally and operationally grounded governance process. See Parts 2b and 3.

**Expected credit loss (ECL).** The probability-weighted present value of credit cash shortfalls under IFRS 9, including reasonable and supportable forward-looking information. ECL is an accounting measurement, not simply the underwriting PD multiplied by a fixed loss rate. See Parts 3 through 5.

**Expected loss (EL).** The statistical expectation of credit loss over a stated horizon, often represented as a consistent combination of PD, LGD, and EAD. Its horizon, timing, discounting, cure, and recovery assumptions must align with the use case. See Parts 2b and 5.

**Explicit Liquidity Feature Path.** A low-latency Kappa and Redis-style feature service that computes interpretable financial variables and routes them directly into the HLR through splines and controlled interactions. These engineered metrics bypass the GRU and Transformer encoders. See Parts 2a, 2b, and 6.

**Explicit Liquidity Features.** Governed variables including CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilization, and approved interactions. Each feature requires a definition, owner, timestamp, lineage, and monitoring rule. See Part 2a.

**Exposure at default (EAD).** The expected amount exposed when default occurs, including the treatment of drawn balances and, where relevant, future drawings or credit-conversion effects. It must be product- and horizon-specific. See Parts 2b, 3, and 5.

### F

**Feature ownership.** The rule assigning each engineered variable to one canonical computation and model path. Raw wallet events may inform more than one branch, but CFA, DLR, Earnings Velocity, and Repayment Velocity are not independently reconstructed and counted in both neural and explicit blocks. See Parts 2a and 6.

**Flink.** Apache Flink, used as the principal example of stateful stream processing with event-time semantics, windows, late-event handling, and continuously updated features. See Part 2a.

**Funds-transfer pricing (FTP).** A method for attributing funding, liquidity, and sometimes optionality costs to assets, products, or business units. In the SPV context, the paper uses matched-funding attribution by product cohort rather than implying a full bank-wide internal FTP system. See Part 5.

### G

**Gated Recurrent Unit (GRU).** A recurrent neural architecture with update and reset gates used to encode short-horizon sequences such as kinematic and operating behaviour. Its output is a low-dimensional representation, not a final credit decision. See Part 2a.

**Geohash.** A hierarchical encoding of geographic location. It can support exposure aggregation, routing, and partial pooling, but fine-grained geography can create privacy, sparsity, proxy-discrimination, and re-identification risks. See Parts 2a through 3.

**Gini coefficient.** A rank-order discrimination measure related to the area under the ROC curve. It does not measure calibration, fairness, causal validity, or customer benefit and should not be used alone for model approval. See Part 2b.

**General Ledger (GL).** The authoritative enterprise accounting record for approved financial postings. Detailed contractual and behavioural calculations remain in governed product subledgers or specialised engines. See Part 4.

**GNSS.** Global navigation satellite systems used to derive location, speed, route, and temporal movement information. Collection and use require data minimisation, quality controls, lawful purpose, and protection against inappropriate inference. See Part 2a.

### H

**Hamiltonian Monte Carlo (HMC).** An MCMC method that uses gradients and auxiliary momentum to explore a posterior distribution more efficiently than a simple random walk. Reliable use still requires convergence, divergence, effective-sample-size, and posterior predictive diagnostics. See Part 2b.

**Hierarchical Bayesian logistic regression (HLR).** The principal underwriting model combining partially pooled geography, platform or cohort, and time effects with explicit liquidity splines, residual neural information, controlled interactions, and approved metadata. It produces posterior PD and uncertainty rather than an unqualified deterministic score. See Part 2b.

**Horseshoe prior.** A global-local shrinkage prior that pulls many weak coefficients strongly toward zero while permitting a smaller number of signals to remain substantial. The regularized horseshoe adds a finite slab. In this paper it is a candidate for the residual neural block, with separately governed priors for other blocks. It does not orthogonalise correlated predictors. See Parts 2b and 6.

### I

**IFRS 9.** The financial-instruments standard governing classification and measurement, impairment, EIR, modification, write-off, and related accounting for relevant receivables and financial liabilities. The responsible reporting entity must approve its methodology. See Parts 3 through 5.

**IFRS 17.** The accounting standard for insurance contracts. It applies to the insurer's relevant contracts and reporting, not automatically to the SPV's purchased loan receivables. Interfaces arise through premium, coverage, cancellation, and insurer cash-flow information. See Parts 3 and 5.

**Insurance premium financing (IPF).** Credit used to fund an insurance premium that would otherwise be paid upfront or on a less convenient schedule. Once premium is validly paid to the insurer, the lender may hold a separate finance receivable against the driver. See Part 1.

**IPF finance receivable.** The lender-owned right to collect funded premium principal, interest, and authorised charges from the borrower under the IPF agreement. It is distinct from insurer-owned premium cash and may be transferred to the SPV only if legally assignable and eligible. See Parts 1 and 5.

**Interest rate risk in the banking book (IRRBB).** The bank's exposure to adverse changes in earnings or economic value caused by interest-rate movements affecting banking-book assets and liabilities. The SPV has analogous repricing and basis risk, but it is not itself labelled a regulated banking book. See Part 5.

### K

**Kafka.** Apache Kafka, used as the durable distributed event-streaming backbone for telemetry, wallet, platform, and operational events. Durability and replay support recovery and reproducibility, but semantic correctness still depends on event contracts and controls. See Part 2a.

**Kappa architecture.** A stream-first data architecture in which current state and derived features are computed from a durable event log rather than maintained through separate batch and speed code paths. Mwendo Pamoja combines this low-latency role with a historical lakehouse. See Part 2a.

**\(K_{\mathrm{cap}}\).** Notation reserved for regulatory or economic capital where required. It prevents the symbol \(K\) from being reused for customer pricing, capital, and unrelated concepts. See Parts 2b and 5.

**\(K_{\mathrm{RBCP}}\).** The borrower-specific premium added to KESONIA under the applicable risk-based credit-pricing formulation. It may reflect lending-related costs, shareholder return, and the borrower's risk profile. It is not identical to PD or an SPV note margin. See Parts 2b and 5.

**KESONIA.** The Kenya Shilling Overnight Interbank Average, used as the Kenyan shilling overnight reference benchmark in the paper's pricing and funding architecture. Contractual use requires an approved compounding, observation, day-count, publication, correction, and fallback convention. See Part 5.

### L

**Lakehouse.** A data platform combining durable object-style storage with table formats, transactions, schema controls, and analytical access. It supports replay, point-in-time reconstruction, feature development, validation, accounting evidence, and reporting. See Part 2a.

**Late-arriving event.** An event that becomes available after its economic event time or expected processing window. The architecture must decide whether to update current state, revise history, initiate an accounting correction, or preserve the original decision while recording the later evidence. See Parts 2a and 6.

**Less discriminatory alternative (LDA).** A feasible alternative model, feature set, threshold, or policy that achieves the legitimate objective with less adverse group effect. LDA testing requires comparable performance, operational feasibility, legal review, and documented trade-offs. See Part 3.

**LIME.** Local Interpretable Model-Agnostic Explanations, a technique that fits a local surrogate around a selected observation. Its output depends on the perturbation distribution, neighbourhood, and kernel and should not be mistaken for a causal explanation. See Part 2b.

**Loss given default (LGD).** The proportion of exposure lost after recoveries, costs, timing, collateral or refund proceeds, and discounting. IPF, microloan, and revolving-credit LGDs require separate evidence and recovery mechanics. See Parts 2b, 3, and 5.

### M

**Maker-checker control.** A segregation-of-duties control requiring one authorised person or service to prepare an action and another to approve it. It is applied to model promotion, accounting entries, reporting submissions, and material overrides. See Parts 3, 4, and 6.

**Markov-chain Monte Carlo (MCMC).** A family of methods that generates dependent samples from a posterior distribution. The paper discusses computational scaling, sampling geometry, and validation because merely completing a chain does not establish reliable inference. See Part 2b.

**Medallion architecture.** A tiered data design commonly described as Bronze, Silver, and Gold. Bronze preserves source events, Silver conforms and validates them, and Gold supplies governed analytical, accounting, or reporting outputs. See Parts 2a, 4, and 5.

**Missingness mechanism.** The process determining why information is absent. Missing completely at random, missing at random, and missing not at random have different implications. In production, missingness can also indicate device failure, consent withdrawal, network interruption, platform change, or deliberate manipulation. See Part 2a.

**Model-risk management.** The governance of model purpose, data, assumptions, development, validation, approval, implementation, monitoring, limitations, changes, and retirement. It converts a mathematically plausible model into a challengeable institutional process. See Parts 2b, 3, and 6.

**Multi-head self-attention.** An attention operation using several learned projections to represent different relationships within a sequence. The Transformer branch applies it to longer-horizon contextual information. See Part 2a.

**Multimodal fusion.** The combination of information from different modalities, such as telematics, wallet events, repayments, platform operations, and macroeconomic context. Fusion must respect timestamps, permissions, missingness, feature ownership, and validation boundaries. See Part 2a.

**Mutual TLS (mTLS).** Transport Layer Security in which both parties authenticate using certificates. It protects the communication channel and counterparty authentication; it does not independently prove the correctness, fairness, or legal meaning of the transmitted data. See Part 4.

### N

**Net interest margin (NIM).** Asset interest and related income less funding and specified financing costs, expressed as an amount or rate over a consistent asset base. The paper examines NIM sensitivity to KESONIA, losses, servicing costs, reserves, and product mix. See Part 5.

**Neural embedding.** A learned low-dimensional vector representing temporal or contextual information from the GRU, Transformer, and fusion process. It is an intermediate model input rather than a customer-facing reason, policy rule, or final credit decision. See Parts 2a and 2b.

**Neural residual.** The embedding remaining after cross-fitted prediction from explicit liquidity features and approved metadata has been subtracted. The HLR uses this residualised block to reduce double-counting. Whitening and shrinkage provide further controls. See Parts 2b and 6.

**Non-performing loan (NPL) trigger.** A contractual portfolio test based on a defined non-performing exposure ratio. If the agreed threshold is breached, it may stop new purchases, block equity distributions, or initiate early amortisation. The definition, cure, numerator, denominator, and measurement date must be contractual. See Part 5.

### O

**OBD-II.** On-board diagnostics data from a vehicle, such as fault or diagnostic events. It may help identify operating interruptions but requires device compatibility, quality controls, lawful use, and careful interpretation. See Part 2a.

**Oracle OFSAA.** Oracle Financial Services Analytical Applications, discussed as an optional institutional platform for instrument cash-flow modelling, ALM, FTP, and related analytics. A validated cohort and waterfall model may remain more proportionate during the pilot. See Part 5.

**Out-of-time validation.** Evaluation on a later period excluded from model fitting and tuning. It tests temporal transportability, calibration, drift, and operational stability more credibly than a random row-level split when drivers and conditions repeat through time. See Parts 2b and 6.

**Overcollateralisation (OC).** The amount by which eligible collateral exceeds the relevant debt claim, usually expressed as a ratio. The receivable definition and debt denominator must be explicit. A 125 percent threshold is not the same calculation as a 75 percent advance rate. See Part 5.

### P

**Partial pooling.** Hierarchical estimation in which sparse groups borrow information from the wider portfolio while data-rich groups may deviate when supported by evidence. It lies between one model for everyone and unrelated models for every cluster. See Part 2b.

**Physical measure \(\mathbb P\).** The probability measure describing real-world event frequencies. Underwriting PD, portfolio monitoring, stress evidence, and IFRS 9 inputs generally begin under this measure. It must not be relabelled risk-neutral merely by adding a funding or credit spread. See Parts 2b and 5.

**Point-in-time correctness.** The requirement that a training record, backtest, or reconstructed decision use only information actually available at that decision time. It prevents look-ahead bias and requires temporal source and revision lineage. See Part 2a.

**Population Stability Index (PSI).** A binned measure of change between a current and reference distribution. Thresholds such as 0.10 or 0.25 are governance conventions unless established otherwise by applicable authority or contract. PSI is a monitoring signal, not proof of model failure or discrimination. See Parts 2b and 5.

**Posterior predictive check (PPC).** A comparison between statistics or patterns observed in real data and those generated from the fitted posterior predictive distribution. PPCs test whether the model reproduces decision-relevant features, not whether it is universally true. See Part 2b.

**Premium cash.** Money payable to or received for the licensed insurer under the applicable insurance arrangement. It must not be confused with an IPF lender's finance receivable or treated as an ordinary SPV loan asset merely because the lender facilitated payment. See Part 1.

**Probability of default (PD).** The probability that a defined default event occurs within a stated horizon for a specified product and exposure. PD requires a precise default definition, observation window, cure treatment, and calibration population. See Parts 2b, 3, and 5.

**Project finance.** Financing evaluated primarily through the cash flows, contracts, controls, and risks of a defined project or ring-fenced vehicle. In Mwendo Pamoja it informs the SPV, waterfall, reserves, covenants, and lender diligence. See Parts 1, 5, and 6.

### Q

**QR orthogonalisation.** A linear-algebra transformation that converts a design matrix into orthogonal basis directions. The paper applies it to the centred and scaled spline basis of Explicit Liquidity Features. It improves conditioning but does not establish causal independence or permanent out-of-sample orthogonality. See Parts 2b and 6.

### R

**Rank-normalised \(\widehat R\).** An MCMC convergence diagnostic comparing within-chain and between-chain variation after rank normalisation. Values near one are necessary but not sufficient evidence of reliable posterior computation. See Part 2b.

**Real-time decision boundary.** A governed mapping from posterior risk, uncertainty, exposure, costs, and constraints to a candidate action. The Credit Policy and Compliance Gate remains responsible for whether the action is permitted. See Part 2b.

**Recovery.** Cash or economic value received after delinquency or default, net of timing, costs, haircuts, and legal limitations. Recoveries may come from borrower payments, assigned refunds, collateral rights, or other valid sources and should be modelled by product and cohort. See Parts 1, 2b, and 5.

**Repayment Velocity.** An Explicit Liquidity Feature comparing actual principal repayment with contractually scheduled repayment over a governed window. It may indicate acceleration, deterioration, cure, or restructuring effects and should not be interpreted without contract status. See Parts 2a and 2b.

**Revolving credit.** A facility under which a borrower may draw, repay, and redraw up to an approved limit, subject to policy and contract. The model distinguishes ordinary operating utilization from a stress-driven full-draw or adverse-utilization pattern. See Parts 1 and 5.

**Risk-based credit-pricing model (RBCPM).** The applicable framework under which the total lending rate is expressed as KESONIA plus a borrower-specific premium, with fees and charges forming part of total cost of credit. Governance must distinguish customer pricing from SPV financing terms. See Part 5.

**Risk-neutral measure \(\mathbb Q\).** A measure used for market-consistent valuation under conditions supporting such a transformation or calibration. It is distinct from the physical probability used to forecast actual defaults and is not required for every customer or SPV pricing calculation. See Part 5 and its Appendix A.

### S

**Significant increase in credit risk (SICR).** The IFRS 9 assessment that credit risk has increased significantly since initial recognition, subject to the reporting entity's approved policy and evidence. A model signal may inform SICR but does not bypass accounting governance. See Parts 3 and 4.

**SHAP.** SHapley Additive exPlanations, a family of methods allocating a model output difference among input features under a chosen background and conditionality assumption. SHAP supports model analysis but does not automatically provide a causal or legally sufficient customer reason. See Parts 2b and 4.

**Special-purpose vehicle (SPV).** A ring-fenced legal and financing entity established to acquire eligible receivables, issue or receive funding, maintain controlled accounts, and distribute cash through a waterfall. It is not the insurer, originator, technology platform, or customer-facing product issuer. See Parts 1, 5, and 6.

**Strong heredity.** An interaction-selection principle under which an interaction is included or receives material prior support only when its constituent main effects are also represented. It reduces unstable interaction discovery and improves interpretability. See Parts 2b and 6.

**Structured finance.** Financing in which asset eligibility, legal isolation, subordination, reserves, covenants, servicing, and a priority of payments shape investor risk. The economic result depends on the actual asset and cash-flow model rather than the transaction label. See Part 5.

**Subledger.** A governed instrument-level or product-level accounting record supporting balances, accruals, payments, arrears, modifications, ECL attributes, and reconciliation to the general ledger. See Parts 4 and 6.

**Sufficiency threshold.** A governed boundary comparing the driver's available net operating income with essential living and operating obligations. It is a policy and affordability concept, not a claim that default becomes mathematically certain below one universal ratio. See Parts 1 and 3.

### T

**Tail dependence.** Dependence that persists in extreme regions of a joint distribution. Lower-tail dependence is relevant when several products deteriorate together during severe driver or macroeconomic stress. See Part 2b.

**Telematics.** Digitally captured information about vehicle movement, diagnostics, trips, and operating context. Telematics can support safety and underwriting but requires quality, consent, purpose, retention, fairness, and security controls. See Parts 1 through 4.

**Transformer.** A neural architecture based principally on attention rather than recurrence. In Mwendo Pamoja it represents lower-frequency structural and contextual sequences and contributes an embedding to the fusion layer. See Part 2a.

**True sale.** A legal transfer intended to move receivables and associated rights from an originator to an SPV rather than create only a secured loan. Its effectiveness depends on transaction documents, conduct, perfection, recourse, insolvency analysis, and applicable law. See Parts 1, 5, and 6.

### U

**Unearned premium.** The portion of an insurance premium associated with the remaining coverage period. Any cancellation refund depends on policy terms, law, timing, charges, insurer process, and valid assignment; it is not automatically liquid collateral at full face value. See Parts 1 and 5.

**Unexpected loss.** A loss measure beyond expected loss, commonly defined through a portfolio-loss quantile, expected shortfall, or another approved risk metric. Its definition and confidence level must be stated and must not be conflated automatically with regulatory capital. See Part 2b.

**Usage-based insurance (UBI).** Insurance in which permitted driving or usage information affects pricing, coverage, incentives, or risk intervention. The insurer retains underwriting and contractual authority under the applicable arrangement. See Parts 1 and 3.

**Utilization.** The amount drawn under a revolving facility divided by the approved limit. High utilization may be ordinary for working capital or evidence of stress depending on repayment, income, timing, and other conditions. See Parts 1, 2a, and 5.

### V

**Variance inflation factor (VIF).** A diagnostic measuring how much the variance of a regression coefficient is inflated by linear association with other predictors. It is one diagnostic for redundancy and is interpreted with posterior correlation, conditioning, ablation, and stability evidence. See Parts 2b and 6.

### W

**Wallet volatility.** An Explicit Liquidity Feature measuring variability in governed wallet inflows, outflows, or net balances over a specified window. Its value depends on transaction classification, seasonality, reversals, cash-outs, and missing-wallet coverage. See Part 2a.

**Waterfall.** The contractual priority in which available SPV cash pays taxes or statutory costs, servicing, senior interest and principal, mezzanine obligations, reserve replenishment, mandatory sweeps, and residual equity distributions. Trigger events can change or block lower-priority payments. See Part 5.

**Whitening.** A transformation that centres and rescales a multivariate block so that its training-sample covariance is approximately the identity matrix. The neural residual is whitened within training folds to improve conditioning. Whitening does not guarantee independence or future-regime orthogonality. See Parts 2b and 6.

**WORM repository.** Storage designed so records are written once and read many times, protecting approved evidence from ordinary alteration during the retention period. It supports assurance but still requires access control, retention policy, indexing, and reconciliation. See Part 4.

### Z

**Zero-emission vehicle (ZEV).** A vehicle producing no tailpipe emissions during operation. The paper touches on ZEV transition deadlines, charging access, routing, asset obsolescence, and the interaction between vehicle type and credit or operating risk. See Parts 1 through 3.

```{=latex}
\end{multicols}
\endgroup
```

## Closing orientation

The glossary should not be read as a claim that every discipline is resolved by one platform. Its purpose is to preserve boundaries. The predictive model estimates risk; the policy gate authorises action; the accounting process records approved economic events; the insurer governs insurance contracts; the lender governs credit; the bank owns its prudential calculations; and the SPV applies its transaction documents and waterfall. The value of the architecture lies in connecting those responsibilities without collapsing them into one undifferentiated model.
