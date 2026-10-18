# Mwendo Pamoja: mobility-fleet application and full-contract worked case

**Author:** Nevil Maloba  
**Date:** 13 October 2026  
**Evidence status:** public commercial context; author-selected numerical scenarios; executable cash and contract tests.  
**Companion:** [reproducible Python case](../../research_lab/mobility_fleet_case/README.md).

## 1. Why this application follows from the research

CGAP's 2023 *Putting Gig Data to Work* brief by Malika Anand and Gayatri Murthy describes Moove combining platform data, telematics and support within vehicle financing. It discusses work-to-own terms extending over two to four years and a package including insurance, repairs and maintenance. That evidence motivated this extension: Mwendo's connected analysis of earnings, vehicle availability, support and funding has an identifiable commercial application. The brief also highlights incomplete platform visibility and changing earnings, providing practical reasons to test data coverage and sustainable take-home income. [CGAP brief, particularly pp. 2 and 4](https://documents1.worldbank.org/curated/en/099063023143011873/pdf/P17436207747210ff096970c02a59ed1daf.pdf).

Moove's UK customer material describes fixed weekly payments and insurance and servicing within its offering. Product and country terms therefore become explicit inputs to an application; a package can assign repair expenditure to the operator while retaining the original driver payment schedule. [Moove UK Customer Hub](https://uk.moove.io/customer-hub/).

The proposition is to connect driver resilience, vehicle uptime and financing performance through reproducible cash-flow analysis, uncertainty-aware underwriting and measurable interventions. Moove's current description of capital, infrastructure and operations provides a commercial setting for the separate driver-led and autonomous-fleet applications. [Moove](https://www.moove.io/).

## 2. Why develop a further worked example

The existing [six-period operating case](MWENDO_WORKED_OPERATING_AND_FINANCING_CASE_2026-10-01.md) follows IPF, microloan and revolving exposures into a receivables pool and waterfall. Its repair comparison assumes 12 versus two days of downtime, with a separately financed repair. It remains useful for showing how an operating interruption changes affordability across products.

The new case addresses a different contract: the operator owns and finances a vehicle, charges a weekly package, bears specified operating costs and transfers the vehicle when the driver completes the contract. It runs through 156 weeks. This makes annual insurance bills, full debt amortisation, ownership transfer, the terminal asset and shareholder cash visible in one set of ledgers. It also distinguishes an operator-funded service obligation from a new borrower loan.

All numerical values below are hypothetical inputs selected for reproducibility. The two repair durations represent alternative scenarios. Estimating the incremental effect of an actual repair programme requires operational evidence and an evaluation design.

## 3. Three research questions

1. **Driver viability:** Which combinations of weekly package, earning capacity, operating cost and liquidity buffer support essential household needs and durable repayment through an operating shock?
2. **Intervention value:** How do repair timing, operator-funded support and authorised fee adjustments change driver cash, the timing of collections, required liquidity and the present value of the operator's cash flows?
3. **Finance and evidence:** What data, contractual rights and approved decision records allow those outcomes to be reconstructed and, where appropriate, carried into a ring-fenced receivables financing arrangement?

## 4. Elected assumptions and actor ownership

| Input or cash flow | Hypothetical value | Owner and interpretation |
|---|---:|---|
| Contract horizon | 156 weeks | Driver and operator contract |
| Vehicle purchase | KES 1,800,000 at inception | Operator pays vehicle vendor |
| Operator loan | KES 1,350,000 | Funder advances to operator; equal weekly principal |
| Funding interest | 12% annual effective | Interest on opening operator debt |
| Setup and opening cash | KES 30,000 and KES 200,000 | Funded through operator equity alongside vehicle equity |
| Initial equity | KES 680,000 | Balances debt, purchase, setup and opening cash |
| Weekly package | KES 25,000 | Contractual driver bill; actual cash may arrive later |
| Full-availability fares | KES 70,000 weekly | Driver gross operating receipts |
| Platform fee | 20% of gross fares | Driver payment to platform |
| Energy | KES 16,000 at full weekly availability | Driver cost, proportional to availability |
| Essential household need | KES 12,000 weekly | Paid before package collection, with shortfall recorded |
| Driver opening/target wallet | KES 20,000 | Driver savings; held separately from operator funds |
| Driver payment floor | KES 10,000 | Preserved when collecting fees; essential consumption can draw lower |
| Insurance premium | KES 130,000 at weeks 1, 53 and 105 | Operator pays insurer; zero duplicate driver premium |
| Routine maintenance/admin | KES 1,800 / KES 800 weekly | Operator cash costs |
| Operating cash target | KES 50,000 plus upcoming premium funding | Operator liquidity policy; explicit equity calls meet shortfalls |
| Terminal vehicle value | KES 450,000 | Driver's non-cash asset on completed transfer |
| Disposal cost on returned vehicle | KES 25,000 | Operator cost in the conditional terminal-return scenario |
| Discount rates | 18% operator; 10% driver | Author-selected annual effective evaluation rates |

The seven-day week is a calendar aggregation. Pilot calibration supplies actual shifts, holidays, rest, demand, charging and safe working patterns. Full-availability earnings describe an input level rather than a required work target. The mechanical repair in this case is an operator-covered package cost; insurer claim recoveries would have their own eligibility, excess, expense and cash-payment records.

## 5. Cash and contract mechanics

Let w denote the model week, a_w the fraction of the week available for work, G full-availability gross fares, τ the platform fee fraction, E full-availability energy cost and H essential household need. Let W be the driver's cash wallet, A package arrears and F the scheduled weekly package fee. C_w is actual package cash collected; Q_w is an authorised fee waiver.

Driver operating cash before household consumption is:

**O_w = a_w × [G × (1 − τ) − E].**

Household payment is the smaller of H and available wallet plus operating cash. The unmet amount remains an explicit outcome. After that payment, collection is limited by the outstanding contract claim and the agreed wallet floor:

**C_w = min{A_(w−1) + F − Q_w, max[0, W_available,w − W_floor]}.**

The contract then moves as:

**A_w = A_(w−1) + F − Q_w − C_w.**

Cash above the KES 20,000 wallet target is distributed to the driver as discretionary surplus. Driver household consumption, discretionary surplus, remaining wallet and terminal vehicle value are reported separately. This avoids treating a paid bill, an unpaid claim, cash available today and an asset received at maturity as the same quantity.

For the operator, let B_(w−1) be opening funded principal and r = (1.12)^(1/52) − 1 the weekly funding rate. Scheduled principal equals the initial advance divided by 156; the final payment resolves the precise remaining balance. Interest is r × B_(w−1). Premiums, maintenance, administration and repair are dated operator payments. An internal cash target pre-funds the next annual premium alongside the operating minimum. Sponsor equity calls supply any gap to that target; distributions release the surplus.

**Operator closing cash = opening cash + collections + equity calls + sale proceeds − operating costs − debt service − disposal cost − equity distributions.**

The sponsor's required cash is therefore an output. Funding availability must subsequently be evidenced through an actual commitment. The current calculation meets all funder payments by showing the equity required; a capped commitment and corresponding lender-default path are specified extensions for transaction evaluation.

At week 156, completed package payments and discharged operator debt lead to vehicle transfer. The driver's KES 450,000 asset and zero operator sale proceeds are recorded together. Under the elected alternative where completion fails, the vehicle returns and is sold; the operator receives sale proceeds less disposal cost while outstanding driver fees remain separately visible pending resolution. The economic depreciation proxy from KES 1.8 million to KES 450,000 supports the asset view. Classification and journals follow the approved accounting analysis for the actual contract.

## 6. Results over the full term

| Measure (KES unless stated) | Uninterrupted | Scheduled repair | Expedited repair | Expedited + fee credit |
|---|---:|---:|---:|---:|
| Assumed unavailable days | 0 | 12 | 2 | 2 |
| Covered repair cost | 0 | 30,000 | 35,000 | 35,000 |
| Authorised fee waiver | 0 | 0 | 0 | 25,000 |
| Total package collections | 3,900,000 | 3,900,000 | 3,900,000 | 3,875,000 |
| Peak unpaid package balance | 0 | 50,000 | 0 | 0 |
| First cure week after arrears | — | 32 | — | — |
| Driver discretionary cash surplus | 468,000.00 | 399,428.57 | 456,571.43 | 481,571.43 |
| Essential household cash | 1,872,000 | 1,872,000 | 1,872,000 | 1,872,000 |
| Unmet household need | 0 | 0 | 0 | 0 |
| Additional operator equity called | 0 | 62,926.46 | 26,472.67 | 51,472.67 |
| Equity net cash after all contributions | 1,043,186.46 | 1,013,186.46 | 1,008,186.46 | 983,186.46 |
| Equity NPV at 18% | 640,726.60 | 610,510.28 | 607,145.30 | 583,158.65 |
| Terminal vehicle transferred to driver | 450,000 | 450,000 | 450,000 | 450,000 |
| Operator terminal sale cash | 0 | 0 | 0 | 0 |

Every baseline scenario pays KES 1.35 million operator-loan principal and KES 231,213.54 funding interest. At the contract's 12% effective annual discount rate, the funder's NPV is zero to numerical precision. Its cash receipt is fully linked to the operator payment; it is counted once across the shared event ledger.

The most useful comparison is between the two repair paths. Ten additional productive days increase driver operating cash by KES 57,142.86 under the supplied unit economics. Earlier collections also reduce cumulative additional operator equity calls by KES 36,453.79. The original driver schedule stays in place and the covered repair adds zero driver debt.

Both collection paths ultimately cure. Their lifetime package receipts are therefore equal. Once the KES 5,000 expediting increment and payment timing are recognised, expedited repair produces KES 3,364.98 less equity NPV in this baseline. The commercial test is consequently precise: estimate retained-customer value, avoided workout expense, changes in repair outcomes, or another attributable benefit, then decide whether the improvement supports the extra expense. A benefit-sharing agreement can also allocate a measured gain between the driver and the party funding faster service.

The fee-credit scenario shows a second distinction. Waiving KES 25,000 increases driver surplus by exactly KES 25,000 and reduces the operator's nominal net cash by the same amount. It is a funded contractual concession. A later pilot could estimate additional benefits such as retention or durable cure and add those observed cash consequences to the comparison.

## 7. Bayesian evidence and insurance interfaces

Mwendo Part 2b supplies the modelling structure for a real pilot. The observation should identify driver, vehicle, package contract, decision time, risk horizon, location, platform and contract vintage. Default, arrears, cure, vehicle downtime and insurance claim outcomes require distinct labels. Partial pooling across relevant city, vehicle and vintage groups can stabilise estimates where experience is sparse. New-group predictions also integrate uncertainty in their as-yet unobserved group effects.

A reviewer receives horizon PD with a credible interval; probability of crossing an approved risk cap; predictive collection and household-shortfall distributions; and posterior differences between eligible actions when a causal design identifies the comparison. These quantities answer different questions. They are presented with sample size, exposure, missingness, model version and label maturity. The deterministic case supplies the financial consequences into which validated posterior draws can later flow.

Bayesian Relativities offers a complementary insurance modelling specification: exposure, claim frequency, severity, claims development and uncertainty. A commercial interface passes covered exposure, approved risk measures, loss scenarios and actual claim cash to the relevant owner. The insurer determines cover, pricing and claim liability. The credit owner determines the customer obligation. The operator tracks excesses, repair invoices, asset downtime and cash received. Full insurance premiums already included in the package remain a single operator cost in this case. Replacing those premiums with retained claim risk would require a revised contract allocation and loss model.

## 8. Practical pilot and evidence requirements

The proposed initial pilot covers one market, one vehicle product and one repair pathway. Its sponsor agrees the scope with operations, credit, insurance, finance, data-protection and customer-support owners. The first deliverable is a reconciled historical case file before any automated recommendation reaches the customer.

| Evidence | Authoritative owner | Decision or reconciliation supported |
|---|---|---|
| Executed package, fee schedule, included services and transfer conditions | Product/legal owner | Correct bill, cost allocation, notice and maturity outcome |
| Platform trips, fares, deductions, settlements and reversals | Platform/payment ledger | Driver cash available at the decision time |
| Work availability, repair diagnosis, queue, invoice and completed release | Fleet/repair operations | Timing, cost and productive return |
| Coverage confirmation, excess, claim status and insurer payment | Insurer/policy and claims systems | Separate coverage, invoice and recoverable cash |
| Household/operating needs and permitted supporting evidence | Customer servicing under approved data purpose | Affordable payment and hardship review |
| Operator debt, sponsor commitment, premium dates and cash policy | Finance/treasury | Funding need, debt service and shareholder value |
| Offer, eligible population, assignment, approval and override | Experiment and decision owners | Causal comparison and decision trace |

A repair pilot can compare an enhanced logistics service with the current approved service for eligible cases, subject to safety and service duties. Repair slot capacity creates possible spillovers, so the allocation unit may be a repair site or time block. Pre-specify the intervention, outcome horizon, minimum relevant effect, sample-size or precision calculation, attrition, repeated-driver treatment and analysis of assignment versus receipt. Record treatment availability and propensity where applicable.

Primary outcomes jointly measure productive days, essential-needs shortfall, driver net cash, collection timing, intervention expense and operator NPV. Secondary outcomes include arrears cure, repeat failure, customer retention, complaints, safety and unequal access. Standardising cash definitions lets the finance team reconcile the experimental estimate to the contract ledger. A successful pilot supplies incremental effects and uncertainty as inputs to the next decision cycle.

Data-purpose and legal-basis registers, minimised access, retention, secure partner transfer, human review and customer challenge routes sit in the jurisdiction-specific implementation plan. Kenya-first requirements already developed in Part 3 are adapted by the responsible local owners for each jurisdiction. Fixed customer package terms and local funder conventions travel separately; KESONIA is selected where its institutional and contractual scope applies.

## 9. Optional ring-fenced receivables financing

The base worked case finances the operator and vehicle. A later structure may dedicate eligible customer receivables and identified collection accounts to a funder. That layer needs an eligibility schedule, concentration limits, purchased or pledged rights, collection allocation, service obligations, reserves, borrowing-base adjustments and an enforceable priority of payments. The arrangement may use an SPV where that is the chosen legal vehicle.

Bundled contracts make cost continuity especially relevant. A financing structure should establish which entity remains responsible for insurance, maintenance, repair and driver support after a transfer or servicer replacement. Asset title, the driver's ownership pathway, receivable rights and residual rights need separate records. A promised vehicle transfer leaves its residual with the driver on completion; the funding case values only rights held by the financing parties. Legal and accounting owners establish transfer, security and reporting treatment from the actual documents.

The bridge into the existing Mwendo receivables case is therefore an explicit data contract: dated eligible amounts, settled cash, collection ownership, costs attached to servicing, arrears, modifications, recoveries and maturity events. This full-contract case supplies operating evidence for that bridge. The pool model then applies its own financing terms.

## 10. Autonomous-fleet extension

Waymo's 5 December 2024 announcement assigns fleet operations, facilities and charging infrastructure to Moove in the announced partnership, while retaining responsibility for the Waymo Driver at Waymo. That gives a concrete division of operational responsibility for a separate fleet application. [Waymo announcement](https://waymo.com/blog/2024/12/next-stop-miami/).

The unit becomes vehicle–depot–service contract. Inputs include vehicle availability, charging queues, battery state, energy tariffs, maintenance capacity, cleaning, repositioning and fleet-contract receipts. The same financial discipline links availability to utilisation, service output, settled revenue, operating expense, capital expenditure and financing. Driver household cash is replaced by the actual fleet-service obligations; autonomous operation and vehicle-control authority stay with their contracted owners. This is a separately specified extension of the evidence and cash architecture.

## 11. Reproduction and checks

The [laboratory](../../research_lab/mobility_fleet_case/README.md) contains assumptions, a Decimal model, a report generator, 18 tests and a frozen baseline verification record. It generates 624 weekly rows across four scenarios plus the detailed transfer journal. Run:

```text
python research_lab/mobility_fleet_case/run_case.py
python -m unittest discover -s research_lab/mobility_fleet_case -p test_model.py -v
```

The 18 tests pass. They verify independent driver budgets; the equal-principal funding-interest identity; initial purchase funding; annual insurance dates; the nominal equity reconciliation; every weekly cash/principal balance; counterparties; shock timing; driver income gained from productive days; arrears and cure; operator-paid repair; the exact effect of a fee waiver; single-recipient terminal value; zero-earnings household shortfall and funding calls; a zero-rate funding contract; wallet-floor treatment; discount timing; invalid inputs; and deterministic reproduction. The maximum baseline reconciliation residual is below 10⁻⁸ KES.

The zero-earnings test intentionally exercises a failed customer completion path: household needs remain visible, sponsor funding calls meet operator obligations, the driver receives no terminal vehicle, and the operator records the conditional sale once. This makes the model's severe-stress cash needs reviewable. Calibration, empirical intervention evaluation, default and early-termination paths, taxes, accounting journals and production adapters form subsequent evidence-building workstreams.

## 12. Canonical manuscript integration

| Manuscript | Added application section |
|---|---|
| Part 1 | Bundled mobility contracts, cost ownership and full-term vehicle transfer |
| Part 2a | Contract-aware weekly features, operating reasons and event lineage |
| Part 2b | Mobility cohort uncertainty and decision-level posterior handoff |
| Part 3 | Operator-funded repair, funded concessions and causal support evaluation |
| Part 4 | Driver–vehicle–contract ledger and insurer/credit/ERP interfaces |
| Part 5 | Full-horizon funding, scenario NPV and terminal-rights reconciliation |
| Part 6 | Scoped mobility pilot, local adaptation and autonomous-fleet extension |

These additions develop the supplied analysis into an application, a reproducible new case and specific manuscript content. The commercial article and pitch deck use the same verified result definitions.
