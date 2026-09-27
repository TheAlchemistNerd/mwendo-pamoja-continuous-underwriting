# Mwendo Pamoja: pricing, SPV and modelling extensions

**23 September 2026 · Two-paste review · Proposed future work**

The linked `output/` review packs are preserved local evidence, excluded from Git. This note is a dated development proposal; it does not report implementation of the proposed models or authorize changes in neighbouring repositories.

## What is already developed

Part 5 §1.2.1 separates customer pricing, physical default probability, investor valuation and note margins. §2.1 connects borrower states to cohort cash and the waterfall, including refunds, recovery costs, dependence and reverse stress. Part 6 §7.2 identifies transaction-readiness requirements and the existing illustrative capital structure. Part 2a covers temporal inputs and fusion; Part 2b covers hierarchy, shrinkage and dependence. The new material is most useful as a route from these specifications to reproducible cases.

## SPV extension: a transaction model with linked schedules

Create the following later, using the approved current structure rather than importing different illustrative amounts from the pasted conversation:

1. **Asset tape and eligibility:** contract, product, borrower, balance, maturity, currency, arrears, evidence date, eligibility reason and haircut.
2. **Purchase and funding:** purchase price, available funding, advance basis, originator contribution and opening reserves; distinguish the proposed advance convention from debt-note OC.
3. **Cohort cash:** contractual receipts, prepayment, cure, default, recovery costs/delay and separately eligible IPF refund.
4. **Accounts:** receipts, availability, restrictions, servicing remittances, reserve drawings and replenishment.
5. **Notes and waterfall:** interest, principal, shortfall, reserve cure, fees, residual distribution and closing balance by class.
6. **Triggers:** thresholds, measurement dates, persistence, cure periods, data fallbacks and the contractual change from revolving purchases to amortisation.
7. **Reporting:** opening-to-closing reconciliations, one-year and ultimate loss, payment delay and principal shortfall by scenario.

Design tests around a functioning waterfall, not a predetermined senior-note outcome. Vary recoveries and refunds independently of default incidence; test simultaneous borrower stress, protection delay and servicing interruption. Add collateral/margin cash only where an actual hedge structure is contemplated.

### Proposed paragraph for Part 5 §2

The transaction model should preserve separate evidence for legal transfer, accounting treatment, capital recognition and cash availability. A receivable can satisfy one test without settling the others. Eligibility and purchase rules determine what enters the pool; the controlled accounts establish what has actually been received; and the waterfall determines which claim is paid next. Each result should be traceable to a term in the documents or a labelled scenario assumption.

Counsel's transaction analysis remains necessary. The [CMA ABS guidance](https://cma.or.ke/wp-content/uploads/2023/03/Policy-Guidance-Note-on-Asset-Backed-Securities-2017.pdf) provides a starting structure for transfer and enforceability questions; this review does not establish a completed transaction or an insolvency outcome.

## Pricing extension

Translate each financial cost into money on a consistent period and exposure basis before deriving the rate component. Use Underwrite Part 5 §2.1 as the reconciliation pattern. Preserve customer K, matched FTP, asset yield, note margin and capital charge as distinct fields. Compare the same cohort under different funding dates and collection delays.

## Modelling implementation note

For the cross-attention implementation, specify the dimensions and the context registry explicitly. Token-level attention uses multiple approved Transformer tokens as keys and values and a GRU query, with availability masks. If the serving design retains only one pooled macro vector, describe fusion as gating or concatenation unless the implementation introduces a meaningful multi-token key set. With one key, a softmax attention weight is one. This concrete interface makes the existing conceptual treatment implementable.

For dependence, compare independent conditional outcomes and candidate residual dependence structures under identical marginal risks and economic scenarios. Specify the treatment of discrete outcomes, tail orientation, parameter uncertainty and common-shock attribution. Report the resulting pool and tranche sensitivity; do not select a capital increase or decrease in advance.

## Insurance/IPF connection

Use the companion insurance note to trace premium, coverage, cancellation, refund entitlement, payment and lender allocation. Part 3 owns the insurer interface; Part 4 receives approved entity-specific events; Part 5 consumes cash available to the vehicle. A usage update can inform risk without becoming an automatic accounting entry or a contractual price change.

**Next candidate deliverable:** a documented monthly asset-to-note model with base, delayed-cash and joint-stress cases, plus an event-level audit trail. No canonical chapter was changed by this review.

## Shared review and calculation basis

See the [two-paste review index](<../../output/pricing_treasury_cross_project_review_2026-09-23/00_READ_ME.md>) and [working formulations and checked examples](<../../output/pricing_treasury_cross_project_review_2026-09-23/02_WORKING_FORMULATIONS_AND_EXAMPLES.md>). Catalogue IDs and source-line references are in the central package.
