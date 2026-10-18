# Reproducible industry applications and publication plan

Author: Nevil Maloba, Philtechent Limited
Updated: 18 October 2026

## Our principle

Every industry application connects an economic question to a reproducible case. A reader should be able to inspect the assumptions, follow the dated evidence and cash flows, run the calculations, compare decisions, reconcile outcomes and understand what would be measured in a partner pilot.

The narrative gives the calculations economic meaning. Computation gives the narrative an inspectable basis. A figure is generated from the case outputs, and its caption identifies the population, currency, horizon and assumptions. Empirical claims carry their own identification and validation evidence.

## Publication requirements

1. State three research questions and the decision each one informs.
2. Identify the economic actors, contractual rights, data provenance, time horizon and units.
3. Publish a parameter file distinguishing observed public information, synthetic assumptions and parameters requiring partner data.
4. Specify the transaction and cash-flow sequence, decision rules, terminal balances and treatment of timing, arrears and recoveries.
5. Include a runnable calculation with a fixed seed where relevant, dependencies, instructions and versioned outputs.
6. Reconcile transfers and balances. Test limiting cases, timing, eligibility and material sensitivities with independent numerical checks.
7. Report the outcomes that matter to each actor: customer cash and service, lender or insurer contribution, liquidity, retained risk and capital treatment where modelled.
8. Identify proposed causal mechanisms and the study design needed to estimate intervention effects. Report parameter, predictive and decision uncertainty separately where relevant.
9. Derive every numerical chart and publication table from the same versioned outputs. Match the article, Word, deck, post and video description to that output version.
10. Record the next empirical or engineering step, the evidence needed, the responsible reviewer and measurable acceptance criteria. Include data purpose, access, minimisation, decision rights, customer correction and the approval/execution record in the proposed workflow.

A worked calculation establishes an arithmetic example. An executable component establishes a reproducible part of the mechanism. A connected case joins the mechanisms within an explicit scope. A calibrated case adds empirical estimation and validation. These labels describe the evidence available to the reader.

## Current five applications

| Application | What exists | Scope and next extension |
|---|---|---|
| Moove × Mwendo Pamoja | Parameterised 156-week driver, operator/equity and funder model; four scenarios; weekly ledgers; transfer records; cash checks; test suite | A connected synthetic financing case. Add actual contractual calibration, capped sponsor commitments and a separately specified receivables funding layer as needed. |
| Moove × Bayesian Relativities | Synthetic claim history; Gamma-Poisson frequency and inverse-Gamma/Gamma severity posteriors; normalised tariffs; insurer, operator and driver economics; reserve/capital/cash projections; fixed-seed simulation and tests | A connected synthetic insurance profit test with a separate 156-week financing bridge. Empirical claim/telematics calibration, tail convergence and measured intervention effects are next steps. |
| 4G Capital × Underwrite for Collection | Twelve merchants; seven scenarios; daily stock, cash, loans, repeat decisions, operating payables, lender funding, two-layer claims and recovery sharing; 24 tests | Connected synthetic merchant and lender case. Executed guarantee terms and a prospective study would establish partner-specific commercial and causal conclusions. |
| Moniepoint × Underwrite for Collection | Ten scenarios; transaction provenance, known-at timestamps, duplicate/reversal controls, three cash cycles, facility schedules, dated payment allocation, human decision records and post-disbursement outcomes; 36 passing tests | Connected synthetic transaction-to-decision case. Current uncertainty summaries describe cash; causal action effects, partner calibration and prospective policy evaluation have their own research design. Contracted cash commitments and prescribed repeat applications are explicit scenario assumptions. |
| Deposit Beta, KESONIA and Bank Risk | A 24-month expected-cohort bank case; nine scenario/policy cases plus nine sensitivities; contractual loan resets, deposits and migration, funding, workout recoveries, allowances and equity; 21 passing tests | Connected synthetic bank case. Borrower cash capacity determines an assumed hazard; expected surviving-cohort payments and workout cash reconcile. Bank-level calibration and empirical estimation of behaviour remain the next steps. |

The two Moove rows record the scope of their existing cases. The 4G, Moniepoint and Deposit Beta rows include the connected implementations verified on 18 October. Each case verification file records the output version used to synchronise its publication assets. All five numerical applications use synthetic assumptions; partner calibration and causal evaluation have their own evidence requirements.

## Reproduction entry points

- Moove operating case: `research_lab/mobility_fleet_case/README.md`.
- Moove insurance case: `research_lab/mobility_insurance_profit_case/README.md`.
- 4G case: `research_lab/four_g_merchant_finance_case/README.md`.
- Moniepoint connected case: `research_lab/moniepoint_cashflow_case/model.py`, `run_case.py` and `test_model.py`; outputs in `output/moniepoint_cashflow_case_2026-10-18/`.
- Deposit-beta connected case: sibling `regtech-kesonia-treasury/research_lab/deposit_beta_dynamic_case/`; tests in `tests/test_deposit_beta_dynamic_case.py`; outputs in `output/deposit_beta_dynamic_case_2026-10-18/`. The case reuses the benchmark and deposit-behaviour components.

## YouTube titles

1. Moove × Mwendo Pamoja — vehicle operations, financing and sustainable collections
2. Moove × Bayesian Relativities — telematics, insurance pricing and profit testing
3. 4G Capital × Underwrite for Collection — merchant cash flows, repeat lending and IFC risk sharing
4. Moniepoint × Underwrite for Collection — turning payment activity into repayment-capacity evidence
5. Deposit Beta, KESONIA and Bank Risk — deposit behaviour, loan repricing and bank decisions

The fifth title removes “connecting” for a shorter display title. Each video's description should link the article, reproducible case, assumptions and source references, and state the case's implementation level from the table above. Video structure: economic question; actors and cash calendar; one calculation; scenario comparison; human decision; next empirical step.

## Five proposed research applications

These are proposed article and case directions to support a scoped research conversation with the named organisations.

### 1 M-KOPA with Underwrite for Collection and Mwendo Pamoja

**Working title:** Asset finance that supports continued earning

M-KOPA describes smartphone and electric-motorbike financing, flexible repayment and access to additional financial services [1]. That creates a concrete application for product-use continuity, household cash and sustainable collection.

Research questions:
1. How do device or vehicle use, earnings volatility and household commitments determine a sustainable repayment schedule?
2. Which support or payment adjustment improves continued use, customer surplus and durable repayment?
3. How do repeat finance and embedded protection change customer outcomes, lender cash and lifetime contribution?

Reproducible case: a daily asset-finance ledger with equipment availability, receipts, essential spending, repair/claim events, support costs, repayment, renewal and lender funding. Compare a fixed schedule with explicitly specified adaptive and supported scenarios. A pilot would estimate the intervention effects.

### 2 Britam with Bayesian Relativities and Shared Value Insurance

**Working title:** Claims speed, customer recovery and insurance profitability

Britam's March 2026 announcement describes AI-assisted assessment and a two-hour settlement target for eligible minor motor claims [2]. The research opportunity is the economic connection between claim handling, repair completion, customer downtime and insurer profitability.

Research questions:
1. How do assessment, settlement and repair delays jointly affect the customer's lost earnings and liquidity?
2. Which claims-routing and repair intervention produces the best combined customer and insurer outcome after delivery costs?
3. How should posterior frequency/severity uncertainty, reserves, reinsurance and capital enter the profit test?

Reproducible case: claim-event and repair-state simulation joined to an insurer ledger and a customer earnings ledger. Compare service pathways, include dispute/rework states and measure settlement and repair completion separately. A prospective design would estimate causal service effects.

### 3 Equity Bank Kenya with Underwrite for Collection and RegTech KESONIA

**Working title:** Guaranteed MSME lending from affordability to capital

IFC identifies Equity Bank Kenya among its Kenyan catalytic first-loss guarantee partners [3]. The next application can connect borrower cash capacity, additional lending, guarantee cash and the bank's funding and portfolio economics.

Research questions:
1. Which customers receive additional sustainable credit because risk sharing becomes available?
2. How do guarantee eligibility, capacity consumption, recovery sharing and settlement delays affect retained loss and funding needs?
3. How should internal funding cost and portfolio constraints influence customer pricing, limits and lending capacity?

Reproducible case: multiple MSME cohorts with loan cash flows, guarantee events, explicit deposit/wholesale funding, internal transfer charges and decision alternatives. Recognition of prudential capital benefits would follow the applicable instrument and supervisory treatment.

### 4 NCBA with RegTech KESONIA

**Working title:** Linking loan repricing, deposit behaviour and lending capacity

NCBA Investment Bank's public research reports KESONIA and interbank liquidity alongside interest-rate conditions [4]. This provides a public starting point for an institution-style transmission case.

Research questions:
1. How do contractual loan resets and asymmetric, lagged deposit repricing change income and borrower debt service?
2. When do withdrawals and product migration reverse an apparent funding advantage?
3. Which funding and lending decisions preserve liquidity and acceptable risk-adjusted economics across scenarios?

Reproducible case: a synthetic bank with an amortising loan book, rate-reset calendar, deposit cohorts, migration/runoff, funding replacement and credit-loss transitions. Treasury, Credit and ALCO receive results from the same scenario ledger. Public market information anchors scenarios; institutional calibration is a later partner-data step.

### 5 FSD Kenya with Underwrite for Collection

**Working title:** Cash-flow evidence for enterprise and household resilience

The Kenya Small Firm Diaries documents volatile business cash flows and the importance of working capital, including the relationship between firms and workers [5]. It offers a natural research dialogue about what lending success should measure across successive business cycles.

Research questions:
1. Which transaction and diary measures distinguish sustainable operating receipts from transfers, borrowing and temporary cash?
2. How do working-capital schedules affect inventory, enterprise cash, household commitments and worker payment continuity?
3. Which prospective comparisons identify improvements in resilience and credit access across business segments?

Reproducible case: diary-style synthetic transactions with enterprise/household boundaries, timing uncertainty, supplier credit, customer receivables and several repayment schedules. Compare borrowing capacity and resilience measures under complete and incomplete data. A study protocol would connect outcomes to intervention timing and selection assumptions.

## Suggested development order

Complete the present publication packages, then develop M-KOPA and Britam first because the existing asset-finance and insurance engines provide substantial reusable foundations. Equity and NCBA extend the lender and balance-sheet cases. FSD Kenya provides a cross-cutting empirical research design for evaluating the outcomes of these applications.

## Primary sources for the proposed applications

[1] M-KOPA, “Impact,” 2025 report and product model. Accessed: Oct. 18, 2026. https://www.m-kopa.com/impact

[2] Britam, “Britam Leverages AI to Settle Motor Claims in Two Hours,” Mar. 3, 2026. https://ke.britam.com/newsroom/britam-leverages-ai-to-settle-motor-claims-in-two-hours

[3] IFC, “IFC Supports Expansion of Financing for Kenya's Small Businesses through the First Catalytic First Loss Guarantee Transactions in Africa,” Aug. 4, 2026. https://www.ifc.org/en/pressroom/2026/ifc-supports-expansion-of-financing-for-kenya-s-small-businesses-through-the-first

[4] NCBA Investment Bank, “Stock Picks January 2026,” market and liquidity review. https://investment-bank.ncbagroup.com/wp-content/uploads/2026/01/Stock-Picks-January-2026.pdf

[5] FSD Kenya, “The Kenya Small Firm Diaries: A new perspective on small firms in Kenya.” https://www.fsdkenya.org/blogs-publications/the-kenya-small-firm-diaries-a-new-perspective-on-small-firms-in-kenya/

## Current file locations

[Complete publication and recording index](<C:/Users/Nevo/Downloads/insuretech & embedded finance/publications/industry-engagement/APPLICATIONS_AND_RECORDING_INDEX_2026-10-18.md>)

4G and Moniepoint are maintained in Underwrite for Collection; the Moove insurance case is in Bayesian Relativities; the Moove operating case remains in Mwendo Pamoja; Deposit Beta remains in RegTech KESONIA.
