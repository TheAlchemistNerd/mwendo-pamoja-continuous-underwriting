# D02 Implementation Plan: HoldCo Venture Capital Technical Pitch

## Objective and target reader

Rewrite D02 as an evidence-disciplined venture pitch for HoldCo. The investor should understand what HoldCo owns, how it earns revenue, what capital it needs, which SPV risks it retains, why its data and technical architecture can become defensible, and what must be validated. The revised pitch should remain ambitious but convert monopoly, certainty, and guarantee language into measurable investment hypotheses.

The pitch must be financially separate from the SPV. Receivables, Class A and B funding, and waterfall cash belong in D03 and the SPV model. HoldCo value comes from IP, contracted services, licences, integration, operating data rights, talent, governance, and any separately disclosed Class C position. The document should state current evidence and future milestones without treating case studies as proof of local performance.

## Proposed document architecture

1. Investment snapshot and evidence status.
2. Market problem and customer proposition.
3. Corporate structure, ownership, and funding.
4. Data rights and edge-to-feature architecture.
5. Underwriting model and policy boundary.
6. Tail risk, intervention, validation, and governance.
7. Fairness, privacy, and customer trust.
8. Data flywheel and defensibility.
9. Revenue architecture and unit economics.
10. Valuation approach, expansion options, milestones, and ask.
11. Risks, diligence, definitions, and sources.

## Section-level implementation actions

### D02-P01: Create an investment snapshot with claim discipline

**Action:** Add before Executive Vision and rewrite that section.

**Resolves:** D02-I05 and D02-I11.

**Content:** State the HoldCo funding ask, proposed instrument, runway, current stage, primary use of proceeds, milestones, and relationship to the SPV. Use USD 1 million as the optional HoldCo facility unless an approved financing decision changes it. Include an evidence legend with `Observed`, `Contracted`, `Prototype result`, `Illustrative`, and `Target`. Summarise the thesis in five claims: integrated risk view, proprietary permitted data, low-latency explicit features, Bayesian uncertainty, and intervention workflow.

Replace “near-perfect certainty,” “pricing monopoly,” and similar claims with target metrics and dates. State that no historical portfolio tape is currently evidenced if accurate. State that the pitch is not the lender term sheet.

**Acceptance tests:** Every claim about performance has a metric, sample, period, and evidence status. The funding ask reconciles to the master baseline. No absolute market-power claim remains.

### D02-P02: Clarify HoldCo, OpCo, SPV, and Class C exposure

**Action:** Rewrite Section 1 opening and Section 7.1.

**Resolves:** D02-I01.

**Content:** Use an entity diagram with assets, contracts, revenue, and risk. HoldCo owns IP and receives licence, platform, analytics, implementation, or servicing-related revenue only where contracts support it. OpCo performs customer and integration functions if retained. The SPV purchases eligible receivables and issues or supports Class A and B notes. Class C is funded by the identified sponsor or HoldCo vehicle.

Disclose that Class C exposes the holder to first-loss risk. State maximum investment, expected accounting, funding source, distributions, concentration, and whether any recourse, repurchase, indemnity, or servicing support reaches HoldCo. Replace “zero balance-sheet credit risk” with “ring-fenced exposure subject to disclosed retained interests and contractual obligations.”

**Acceptance tests:** The diagram reconciles with D01 and D03. HoldCo operating cash cannot be swept to noteholders except under an explicit support contract. Class C exposure is included in HoldCo cash planning.

### D02-P03: Rebuild the cap table and governance proposal

**Action:** Replace Section 1.1.

**Resolves:** D02-I01 and D02-I02.

**Content:** Show pre-money ownership, financing instrument, post-money ownership, option pool, and fully diluted basis. Add at least three scenarios: current financing, next institutional round, and strategic partner issue. Separate economic ownership from voting control, board seats, reserved matters, founder vesting, pre-emption, information rights, and anti-dilution. If founders require 51% voting control, present a lawful mechanism and its investor trade-offs. Do not promise non-dilutable economic ownership.

Add governance for related-party transactions between HoldCo and SPV, IP licence pricing, Class C investment, conflicts, model decisions, data sharing, and founder transactions.

**Acceptance tests:** Each scenario sums to 100% on a fully diluted basis. Future rounds can occur without logical impossibility. Voting and economic percentages are not conflated. Counsel has a list of provisions to draft.

### D02-P04: Rewrite the data moat as a governed rights and integration asset

**Action:** Rewrite Sections 2.1 and 6.

**Resolves:** D02-I04 and D02-I09.

**Content:** Present the pipeline from source events to governed features and labelled outcomes. For each data source identify counterparty, contractual right, lawful purpose, duration, exclusivity if any, portability, revocation, retention, permitted model use, and output ownership. Include driver notice, lawful basis, consent where used, DPIA, data minimisation, processor roles, cross-border transfer, rights handling, and deletion [10], [11].

Define the flywheel through measurable stages: contracted coverage, usable-event completeness, label maturity, model uplift, intervention learning, integration switching cost, renewal, and incremental gross margin. Explain that more raw data can add noise or risk; defensibility depends on lawful reusable outcomes and operational integration.

**Acceptance tests:** Every “proprietary” data claim names a right. The architecture includes retention and deletion. The flywheel has leading and lagging KPIs and failure conditions.

### D02-P05: Freeze neural and explicit feature ownership

**Action:** Rewrite Section 2.2, Section 2.3, and the feature portions of Section 9.

**Resolves:** D02-I03.

**Content:** Define the neural branch as raw or minimally transformed telematics, driving-session, wallet timing, and contextual sequences. Define the Explicit Liquidity Feature Path as the Flink and Redis computation and serving path for CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved interactions. State that those named metrics bypass GRU and Transformer encoders and enter HBLR through splines and interactions.

Add a feature registry excerpt with formula owner, time window, unit, lag, availability, null policy, version, and business interpretation. Explain that shared raw sources are allowed, but engineered metric duplication is not.

**Acceptance tests:** Earnings Velocity is absent from GRU input lists. CFA is absent from neural input lists. Every diagram and glossary entry uses the same ownership.

### D02-P06: Replace the legacy architecture with a validated decision stack

**Action:** Replace the figure and rewrite Sections 2.3 and 2.4.

**Resolves:** D02-I03, D02-I04, and D02-I08.

**Content:** Use the canonical Flink split, neural embeddings plus explicit features, HBLR, then Credit Policy and Compliance Gate. Explain model outputs and uncertainty. Define the gate's hard rules and owners. Add a model lifecycle sidebar: development, independent validation, approval, deployment, monitoring, change, incident, rollback, and retirement.

Do not call Kappa a policy engine. Do not call explicit features regulatory compliance. Explain how reason codes combine posterior contributions and actual policy rules. PSI is an internal monitoring convention unless contracted or mandated.

**Acceptance tests:** “Tabular Bypass” does not appear. Policy rules are versioned separately from model artifacts. A reader can identify who approves a model and who approves a credit rule.

### D02-P07: Reframe Bayesian and copula value as testable advantage

**Action:** Rewrite Section 2.4 and Section 3.

**Resolves:** D02-I05 and D02-I06.

**Content:** Explain partial pooling, posterior uncertainty, nonlinear explicit features, and cohort effects without promising certainty. Set validation targets: time-split AUC or Gini, calibration error, Brier score, approval uplift at fixed loss, lead time, uncertainty coverage, and subgroup performance. Explain offline posterior inference and deterministic online scoring.

Present Clayton as one candidate dependency model. Compare Student-t, Gaussian, Clayton, Gumbel, and vines. Describe empirical selection, parameter uncertainty, stress overlays, and waterfall output. State that credit enhancement protects investors through cash and contracts and that the model only estimates risk.

**Acceptance tests:** No model family is called inherently superior without test criteria. Copula output maps to stress loss, not regulatory capital relief or a guarantee. All performance claims have a validation plan.

### D02-P08: Replace fairness guarantee with governance and outcome testing

**Action:** Rewrite Section 4 and connect it to model governance.

**Resolves:** D02-I07 and D02-I08.

**Content:** Define applicable Kenyan legal review, protected and sensitive attributes, proxy analysis, customer notices, reason codes, appeal, human review, and adverse-action controls. Present metrics for selection, pricing, limits, calibration, false-positive and false-negative rates, interventions, complaints, and outcomes. Include confidence intervals and minimum group sizes.

Describe MMD, representation constraints, or feature orthogonalisation as candidate mitigations, not guarantees. Explain the known tension among equalized odds, calibration, and differing base rates. Require less-discriminatory-alternative comparison and independent review.

**Acceptance tests:** No claim says MMD guarantees equalized odds. Fairness is tested before launch and continuously. Legal and statistical conclusions are visibly separate.

### D02-P09: Rebuild the moat and case studies around evidence

**Action:** Rewrite Sections 2.5 and 6.

**Resolves:** D02-I05 and D02-I09.

**Content:** Retain case studies only as analogies. For each, state company, product, what is comparable, what is not, and the source. Do not infer Mwendo Pamoja performance from another company's funding or valuation. Build a moat scorecard: data rights, outcome labels, integration coverage, model uplift, decision latency, partner switching cost, regulatory readiness, security, and unit economics.

Add risks that weaken the moat: platform concentration, revoked API access, concept drift, alternative data restrictions, incumbent replication, sparse defaults, low customer trust, and costly servicing.

**Acceptance tests:** Every case study has a limitation. “Network effect” is supported by metrics, not raw-event volume. Investor diligence can verify each moat component.

### D02-P10: Separate HoldCo revenue from SPV investor return

**Action:** Rewrite Sections 5, 7.1, and 7.2.

**Resolves:** D02-I01 and D02-I10.

**Content:** Create a revenue table with payer, service, contract basis, recurring or one-time status, gross margin, implementation cost, capital need, credit exposure, and regulatory dependency. Possible rows are platform licence, carrier analytics, lender underwriting service, servicing or monitoring, implementation, and performance fee, but include only plausible contracted categories.

Show Class C distributions separately as investment cash flow, not SaaS revenue. Build HoldCo operating forecasts and runway excluding SPV collections. Use valuation scenarios based on revenue quality, comparable selection, dilution, and execution milestones. Do not apply a generic SaaS multiple to total SPV asset yield.

**Acceptance tests:** HoldCo revenue ties to contracts or labelled assumptions. Gross margin excludes pass-through SPV cash. Class C exposure and return are separately valued.

### D02-P11: Reframe market expansion as gated options

**Action:** Rewrite Section 8.

**Resolves:** D02-I10.

**Content:** Divide expansion into Kenya platform expansion, adjacent driver products, new African jurisdictions, and technology licensing. For each define customer, licence, insurance distribution, credit regulation, benchmark, currency, data law, required partner, integration, minimum data, capital, and go or no-go evidence. Use staged experiments and option value rather than a deterministic rollout.

**Acceptance tests:** No jurisdiction is treated as a copy of Kenya. Expansion costs and regulatory dependencies appear in runway. Each option has measurable entry criteria.

### D02-P12: Replace the glossary with controlled definitions, risks, and sources

**Action:** Rewrite Section 9 and add closing diligence.

**Resolves:** D02-I11 and closes all findings.

**Content:** Use the master terminology and notation. Add an investment-risk register covering partner concentration, data rights, model performance, intervention harm, regulatory uncertainty, Class C exposure, funding, security, talent, and execution. Cite global IEEE sources and mark primary versus comparative. Remove long dashes, corrupted symbols, and unsupported absolutes.

**Acceptance tests:** The internal glossary agrees with D05 and D06. Every external claim has an indexed citation. Automated scans find no “Tabular Bypass,” “non-dilutable” guarantee, “zero credit risk,” “near-perfect,” or “monopoly” claim.

## Recommended editing order and reviewers

Perform P01 through P03 first with founders, corporate counsel, and finance. Perform P04 through P06 with the data architect, DPO, model owner, and compliance lead. Complete P07 and P08 with independent validation and fairness review. Complete P10 only after the revenue model and SPV separation are approved. Finish expansion, definitions, and sources last.

Reviewers should include founders, lead investor or adviser, corporate counsel, transaction counsel, finance lead, model validator, chief data scientist, DPO, security lead, bank and carrier partners, product owner, and customer-protection specialist.

## Pre-publication validation checklist

- Reconcile the USD 1 million HoldCo ask and use of proceeds.
- Reconcile cap table scenarios on a fully diluted basis.
- Verify IP and data-rights evidence.
- Separate Class C exposure from operating revenue.
- Verify feature ownership and architecture diagram.
- Replace certainty and guarantee claims with target metrics.
- Validate model and fairness test plans.
- Qualify comparative regulatory references.
- Tie valuation scenarios to revenue quality and dilution.
- Scan terminology, punctuation, and citations.

## Definition of done

D02 is done when an investor can identify HoldCo's assets, contractual revenue, funding need, governance, retained credit exposure, technical differentiation, validation plan, data rights, customer protections, and milestone-based valuation without relying on unsupported certainty or SPV cash. Every technical claim must match D05 and D06, and every financing claim must match D01 and D03.

## Investor diligence data-room design

The rewrite should be accompanied by a data-room index, even if several records remain pending. Corporate materials should include incorporation records, current and fully diluted cap table, option plan, shareholder rights, founder vesting, board and reserved matters, IP assignments, employment and contractor inventions clauses, related-party policy, and beneficial ownership. Commercial materials should include signed or draft platform, carrier, lender, servicing, data, and licensing agreements, plus a contract-to-revenue bridge.

The technology folder should contain architecture decisions, event schemas, feature registry, source-to-feature lineage, security threat model, DPIA, data-retention schedule, model cards, development report, independent validation plan, fairness test plan, incident process, and a reproducible demonstration. The SPV folder should contain D03, the financial model, Class C commitment evidence, true-sale issues, and a clear statement that SPV assets are not HoldCo operating revenue. The finance folder should contain a monthly HoldCo budget, hiring plan, use of proceeds, runway, scenario cash needs, and any intercompany charges.

Each pitch claim should map to one data-room item or to a dated milestone for producing it. A claim such as “exclusive platform data” requires an executed clause and permitted-use analysis. A claim of model uplift requires a validation dataset, comparator, metric, confidence interval, and time split. A claim of recurring revenue requires a signed term, billing basis, implementation obligation, renewal, and termination right. A claim of privacy readiness requires completed risk assessment and operational procedures, not only a policy statement.

## Metric dictionary for the revised pitch

Create a one-page metric dictionary so the pitch and financial forecast cannot use the same label differently. Define active driver, eligible driver, connected driver, scored driver, approved driver, funded driver, policy in force, monthly recurring revenue, annual recurring revenue, gross revenue retention, net revenue retention, implementation revenue, gross margin, contribution margin, default, recovery, intervention, lead time, and model uplift. State whether each measure is monthly, annual, cohort-based, gross, or net.

For the data flywheel, report usable event completeness, latency percentile, feature freshness, outcome-label maturity, online-offline parity, and partner coverage. For model performance, report discrimination and calibration together, plus uncertainty coverage and subgroup ranges. For commercial defensibility, report contract duration, permitted data use, renewal, integration depth, and switching effort. For customer value, report coverage continuity, avoided downtime, complaint rate, appeal outcome, and net cash-flow effect. The metric dictionary prevents the pitch from replacing vague superlatives with equally vague percentages.

## Release governance

Assign the CEO as business owner, CFO as financing and revenue owner, CTO as architecture owner, model-risk lead as performance owner, DPO as data-rights owner, and counsel as legal reviewer. Require sign-off on the exact slide or paragraph claims within each domain. Keep a claim ledger with source, status, owner, expiry, and replacement evidence. Time-sensitive market and regulatory claims should expire after a defined review period.

Before every investor release, reconcile D02 to D01, D03, D05, D06, and the current HoldCo budget. Run automated scans for prohibited legacy terminology, absolute guarantees, unqualified regulatory claims, inconsistent capital amounts, and corrupted punctuation. Archive the released version and evidence pack so later investors can distinguish what was known at each fundraising date.
