# D04 Implementation Plan: Product Architecture and Cascades

## Objective and target use

Rewrite D04 as the authoritative product and cash-event specification for the three-product receivables pool. It should explain contractual parties, customer journeys, product state machines, ledgers, cash flows, external shocks, cross-product dependence, and portfolio mitigants. D03 should be able to derive asset eligibility and collection rules from it; D05 should derive event schemas and labels; D06 should derive prediction targets; D07 should derive intervention controls; D08 should derive journals; and D09 should derive cohort cash flows.

The revised paper should preserve the unifying thesis that a driver's vehicle, income, insurance, wallet, and credit obligations form one operating cash-flow system. It must stop presenting plausible cascades as deterministic theorems and must correct every formula. Product and customer descriptions should be comprehensible to counsel and operators, while formal definitions should be precise enough for engineers and modellers.

## Proposed document architecture

1. Purpose, scope, evidence status, and controlled definitions.
2. Counterparty and contract map.
3. Driver operating cash-flow identity.
4. Three-product receivables pool overview.
5. IPF lifecycle and carrier refund mechanics.
6. Microloan lifecycle and collection mechanics.
7. Revolving-credit lifecycle and utilisation controls.
8. Unified product event and state-transition model.
9. External shocks and correlated cascade hypotheses.
10. Collection, reserve, intervention, and customer safeguards.
11. SPV eligibility and cohort-model interface.
12. Evidence, experiments, assumptions, and references.

## Section-level implementation actions

### D04-P01: Add document controls, symbols, and evidence status

**Action:** Add before the introduction and rebuild references at the end.

**Resolves:** D04-I10.

**Content:** State version, date, owner, audience, and relationship to D03 through D09. Add evidence labels for contractual term, observed historical fact, proposed design, illustrative assumption, and calculated output. Create a symbol table with unique symbol, definition, units, grain, sign, frequency, and source. Reserve `K_RBCP` for customer premium and avoid using `K` for capital or other concepts.

Add a formula-control rule: every expression has defined inputs, dimensional check, numerical example, and executable unit test. Add the global IEEE citations and explicitly state when media such as [31] supports only a scenario rationale.

**Acceptance tests:** Every formula symbol is defined once. Every percentage states a period and denominator. References support the attached proposition.

### D04-P02: Repair the driver cash-flow identity and all damaged equations

**Action:** Rewrite “The Gig Driver as a Unified Asset Class” and audit every later formula.

**Resolves:** D04-I01.

**Content:** Define gross fares, platform commission, fuel, maintenance, insurance, taxes, other operating expenses, debt payments, reserve deposits and releases, and net disposable cash. Decide whether debt service is included before or after operating cash flow and use consistent labels. Correct subtraction signs and make cash direction explicit.

Include one monthly numerical example showing gross fares through net cash, then a daily or trip-level event bridge. Verify unearned premium uses remaining coverage proportion, net refund uses one minus haircut, and reserve close deducts permitted releases. State that actual carrier refund terms and accounting can differ from the simplifying formula.

**Acceptance tests:** A spreadsheet and the displayed equations produce the same example. Changing any cost upward cannot increase net income absent an explicitly modelled offset. Automated scan finds no commas substituting for minus signs.

### D04-P03: Rename and define the three-product receivables pool

**Action:** Replace “The Triple-Product Capital Stack” and add a pool summary.

**Resolves:** D04-I02 and D04-I08.

**Content:** Call IPF, microloans, and revolving credit the “Three-Product Receivables Pool.” Present a table with obligor, originator, legal contract, funded amount, tenor, repayment frequency, pricing, fee, collateral or recovery source, delinquency, default, cure, cancellation, prepayment, restructuring, recovery, and SPV eligibility. Add a separate diagram showing that these assets support Class A, B, and C liabilities defined in D03.

Describe aggregate exposure by driver and establish a master driver ID across products. Explain that product diversity does not diversify driver-level income risk when obligations share the same payer.

**Acceptance tests:** No product is called a capital tranche. Product balances reconcile to aggregate driver and SPV exposure. Every state used in a formula is defined.

### D04-P04: Freeze partner, carrier, platform, and collection responsibilities

**Action:** Rewrite “Partnership and Counterparty Structure” and relevant product paragraphs.

**Resolves:** D04-I03 and D04-I04.

**Content:** State that the licensed carrier issues the insurance policy and owns insurance-risk decisions. Define originator and SPV ownership of financing receivables. Define servicer duties. Treat platform fare split or escrow as a proposed contractual mechanism. Add rows for customer consent, deduction cap, sufficiency floor, notices, revocation, dispute, refund, platform set-off, insolvency, API outage, and reconciliation.

Use a funds-flow diagram: driver fare payer to platform wallet; permitted deductions to controlled collection account; carrier premium payments; receivable sale consideration; SPV collections; reserve pocket; and customer remainder. Show legal ownership at each step.

**Acceptance tests:** Technology provider is not called insurer unless licensed. No API is described as legally senior. Every collection priority has a contract and legal-review dependency.

### D04-P05: Build product state machines and ledger events

**Action:** Rewrite the IPF, microloan, revolving, and “Siloed Product Mechanics” sections.

**Resolves:** D04-I01 and D04-I08.

**Content:** For each product define states and permitted transitions. IPF may include quoted, accepted, premium paid, policy active, instalment current, grace, cancellation requested, carrier-confirmed cancellation, refund due, refund collected, delinquent, default, written off, and recovered. Microloan may include approved, disbursed, current, past due buckets, restructured, default, written off, and recovered. Revolver may include approved limit, available, drawn, current, frozen, over-limit, past due, terminated, default, and recovered.

For each transition state trigger event, event time, effective time, ledger debit and credit, customer notice, model label, SPV eligibility, covenant effect, accounting handoff, and allowed intervention. Define cure and reversal. Include unique event IDs and correction handling.

**Acceptance tests:** No impossible transition can occur. Cash and contractual balances roll forward. D05 can derive labels without reading narrative prose. D08 can map every financial event to a journal or non-posting status.

### D04-P06: Reframe external shocks as timed causal scenarios

**Action:** Rewrite “Anatomy of an External Shock,” “Default Domino Effect,” and correlation narrative.

**Resolves:** D04-I05 and D04-I06.

**Content:** Define shocks such as fuel price, platform commission, demand reduction, vehicle downtime, regulatory restriction, benchmark rate, FX where relevant, and carrier action. For each give transmission channel, exposed cash-flow component, lag, duration, reversibility, and evidence. KESONIA affects customer cash only at contract reset and according to contract [1]-[3].

Present the cascade as a directed hypothesis graph, not a theorem. Show positive and negative feedback: a reserve or intervention can interrupt the path; platform deactivation can intensify it. Define empirical tests using event studies, survival analysis, state transitions, and treatment-effect designs. State confounders.

**Acceptance tests:** No text says correlation converges to one. Every shock has a time convention. Benchmark stress cannot affect a fixed-rate loan before its terms permit.

### D04-P07: Redesign collection, reserves, and interventions with safeguards

**Action:** Rewrite “Direct Platform Escrows,” “Collateralized Reserve Pockets,” and mitigation sections.

**Resolves:** D04-I04 and D04-I09.

**Content:** Separate the driver's reserve pocket from the SPV cash reserve account. For driver reserves define legal owner, custodian, interest, contribution rule, withdrawals, lien or set-off, disclosures, hardship, exit, death, dispute, and data reporting. For platform collections define lawful deduction, customer sufficiency, order, cap, reconciliation, outage, and fallback.

For premium holidays, micro-reward bridges, draw freezes, limit reductions, and fatigue routing, create an intervention table with model or policy trigger, decision owner, required human review, funder, amount, duration, customer notice, consent, contractual basis, accounting, appeal, safety risk, and success metric. Include do-no-harm and fairness review.

**Acceptance tests:** Driver money cannot be counted as SPV collateral without legal basis. Intervention cost and effect can be zero or adverse in the financial model. Customer remedy and appeal are explicit.

### D04-P08: Replace deterministic dependence with an empirical portfolio-risk framework

**Action:** Rewrite “The Diversification Illusion” and copula references.

**Resolves:** D04-I01, D04-I06, and D04-I07.

**Content:** Define marginal outcomes by product and joint outcomes at driver, platform, geography, and time. Explain why unconditional pairwise correlation may hide conditional tail dependence. Present Clayton as one candidate with lower-tail behaviour after correct variable orientation. Require comparison to Gaussian, Student-t, Gumbel, rotations, and vines where data allow.

Explain calibration data, censored outcomes, sparse defaults, parameter uncertainty, regime variation, and out-of-sample validation. State that scenarios can stress dependence where observations are insufficient. Connect resulting loss distributions to D03 waterfall and D09 model. Keep regulatory capital treatment in D07.

**Acceptance tests:** Copula parameter is estimated or explicitly stressed, never set mechanically by shock severity. Portfolio loss includes exposure, LGD, recovery timing, and cash waterfall. No model is said to prove containment.

### D04-P09: Add the SPV eligibility and cohort-model interface

**Action:** Add after mitigation.

**Resolves:** D04-I02 and supports D04-I08.

**Content:** For each product specify the receivable amount entering the SPV, purchase date, opening balance, scheduled principal, finance charge, prepayment, delinquency, default, recovery, closing balance, and eligibility. Define carrier refund as a separate cash or receivable event with haircut and lag. Define revolving commitment versus funded balance. State aggregate driver and product caps.

Map each field to D03 borrowing base and D09 cohort schedule. Add reconciliation identities for balance and cash. Identify data source and update frequency.

**Acceptance tests:** Product cohorts roll forward with zero unexplained difference. The same default is not counted in multiple products without intended joint-loss treatment. Eligibility can be tested from fields present at the calculation date.

### D04-P10: Rebuild references, diagrams, and editorial quality

**Action:** Rewrite conclusion and references and redraw all diagrams.

**Resolves:** D04-I10 and closes all findings.

**Content:** Use diagrams for counterparty flow, product states, cascade hypotheses, and SPV interface, each with legend and source status. Cite CBK for benchmark mechanics, IFRS Foundation for accounting boundaries, and empirical sources for dependence where relevant. Move broad market commentary to context. Add assumptions and diligence register.

Remove corrupted punctuation, long dashes, deterministic absolutes, “constitutional seniority,” and “capital stack” for products. Use consistent headings and document IDs.

**Acceptance tests:** Visual and prose descriptions agree. All equations render. Links resolve to the global IEEE index. The document contains no unexplained legacy label.

## Test pack and evidence collection

Build a product test pack with at least one normal and one edge case per state transition. Examples should include weekend collection, platform reversal, partial payment, prepayment, policy cancellation before and after a carrier cut-off, refund delay, failed wallet debit, duplicate event, backdated correction, reserve withdrawal, hardship, full revolver draw, limit freeze, restructure, default, recovery, and write-off. Each case should state starting balances, events, expected product state, expected cash, expected SPV eligibility, and expected journal handoff.

Collect sample executed or proposed contracts, policy wording, platform settlement file, carrier refund file, wallet and servicing records, notices, and complaint process. Validate that the event dictionary can represent actual partner data. Where a contract does not yet exist, mark the mechanic as proposed and do not model it as certain recovery or collection priority.

## Recommended editing order and reviewers

Perform P01 and P02 first. Freeze roles through P04 before writing product states in P05. Complete P03 and P09 with D03 and D09 owners. Complete P06 and P08 only after the event and outcome data are understood. Complete P07 with counsel, product, fairness, and operations. Finish references and visuals last.

Reviewers should include product owner, carrier underwriter and finance lead, licensed lender, servicer, platform payments lead, transaction counsel, consumer and data-protection counsel, accountant, credit-risk modeller, data architect, financial modeller, operations, and customer-support lead.

## Pre-publication validation checklist

- All formulas pass numeric unit tests.
- Product and capital-stack terminology is separated.
- Carrier and financing roles are fixed.
- Product state machines are complete and reversible where needed.
- Collection and reserve ownership are legally qualified.
- KESONIA shocks follow contract timing.
- Dependence statements are empirical hypotheses.
- Product fields map to D03, D05, D06, D08, and D09.
- Customer safeguards and appeals exist.
- Citations and punctuation pass automated scans.

## Product definition and policy catalogue

Create a controlled catalogue for every customer-facing and SPV-relevant rule. For IPF, include eligible policy type, premium amount, tenor, instalment schedule, grace, cancellation, refund, policy reinstatement, claim interaction, carrier settlement, and maximum financed amount. For microloans, include purpose, principal, tenor, instalment, rate, fees, prepayment, delinquency, restructure, hardship, and recovery. For revolvers, include limit assignment, availability, draw, repayment allocation, utilisation, minimum payment, interest, fee, freeze, reinstatement, expiration, and termination.

Each catalogue rule must identify whether it is contract, credit policy, operational procedure, model output, or proposed pilot control. State the owner, approval, effective date, customer disclosure, source system, model feature effect, SPV eligibility effect, accounting effect, and monitoring. This prevents an illustrative product description from silently becoming a policy rule or receivable representation.

Add a cross-product priority table. If cash is insufficient, define how platform deductions, premium, scheduled loan payment, revolving repayment, reserve contribution, taxes, and driver sufficiency interact. Identify which priorities are fixed by law or contract and which remain design choices. Evaluate whether a collection order creates adverse selection, customer harm, or a misleading asset-yield assumption.

## Data-labelling and empirical study plan

Define outcome labels before model development. Each default label should name product, days-past-due threshold, probation, cure, restructuring treatment, write-off, recovery window, and observation maturity. Joint-default labels should specify whether events must occur within the same week, month, or shock window. Insurance lapse, platform deactivation, vehicle downtime, and reserve depletion are separate outcomes, not interchangeable defaults.

Design empirical studies for the proposed cascade. Use a pre-registered causal graph, confounder list, and time ordering. Analyse natural experiments in fuel prices, commission changes, platform outages, vehicle breakdown, and policy cancellations. Compare drivers exposed to an intervention with credible controls, while recognising that high-risk drivers are preferentially treated. Estimate lead time, hazard change, cash-flow effect, default effect, and adverse consequences with uncertainty.

The first pilot should not require proving the full cascade. It can validate event completeness, product-state accuracy, cash reconciliation, and bounded intervention execution. Later stages can assess whether combined features and interventions improve outcomes. Publish negative and inconclusive findings so product policy does not depend on a one-sided narrative.

## Change control and operational ownership

Assign a product-definition committee with product, risk, servicing, finance, carrier, platform, legal, privacy, and customer-support representation. Any change to rate, fee, limit, collection, reserve, cancellation, recovery, state, or intervention must identify affected contracts, notices, D03 eligibility, D05 events and features, D06 labels, D07 controls, D08 journals, D09 model, and D10 test cases.

Maintain semantic versioning for each product. A major version changes customer cash or legal rights; a minor version changes policy within contract; a patch corrects documentation without economic change. Historical receivables retain the terms and state logic under which they originated. The servicing ledger and training data must preserve version so a later change cannot rewrite old performance.

Run quarterly product reconciliation and outcome review during the pilot. Review cash breaks, state exceptions, manual overrides, complaints, cancellations, recoveries, interventions, fairness, and model discrepancies. Require corrective action and, where needed, purchase suspension. This operating forum is the practical mechanism that keeps the rewritten product architecture consistent after publication.

## Definition of done

D04 is complete when legal, product, data, accounting, risk, and finance teams can use the same state and cash definitions without interpretation. Every asset in the SPV must originate from an identified contract and event trail, every mitigation must have authority and measurable effect, and every cascade claim must be testable rather than rhetorical.
