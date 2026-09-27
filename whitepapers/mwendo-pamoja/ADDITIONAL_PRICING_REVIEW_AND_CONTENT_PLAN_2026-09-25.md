# Mwendo Pamoja and Underwrite for Collection: pricing development notes

**25 September 2026 | Editorial additions proposed; canonical manuscripts preserved**

This is the canonical cross-series pricing/content plan retained by Mwendo. The LinkedIn directory links here. Section and line references identify the editions reviewed on 25 September, rather than stable positions after later edits. Linked evidence under `output/` is a preserved local review pack and is not distributed in a Git clone. Underwrite has its own sibling repository; this plan does not authorize edits there or in the SokoIntel guest project.

## 1. Keep the document families distinct

There are three relevant editorial bodies, not one interchangeable series:

1. **Underwrite for Collection, MSME Lifecycle Credit Research Series**, in `behavioural credit scoring - underwrite to collect rct/series/parts`. Its Part 5 is already a substantial pricing, ECL, capital, Treasury, protection and funding chapter.
2. **Mwendo Pamoja**, in `whitepapers/mwendo-pamoja/parts`, applies the lifecycle to IPF, microloans, revolving lines and the proposed financing SPV. The controlled model specification and SPV term sheet govern their respective interfaces and assumptions.
3. **Practitioner and LinkedIn material**, in `publications/linkedin`: the standalone *Underwrite for Collection*, *Before the Ratio*, and the earlier gig-economy Parts 1, 2a, 2b and 3. These public-facing drafts vary in how far they reflect subsequent whitepaper development.

The pricing paste strengthens a common financial casebook. It does not require merging the two whitepapers or re-deriving their established foundations.

## 2. Coverage assessment and exact development locations

For readability, **U5** below means [Underwrite Part 5](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md>), and **M5** means [Mwendo Part 5](<parts/Part_5_KESONIA_Pricing_and_Capital_Orchestration.md>).

| Topic | What is already written | What the pricing paste usefully develops |
|---|---|---|
| Customer premium and lender economics | U5 §2.1, lines 64–171, already reconciles KESONIA, FTP, pricing loss, operating cost, capital charge and commercial return. M5 §1.2.1 separates underwriting risk, customer pricing and investor pricing. | Add one money-based schedule linking pre-capital contribution, RAROC, economic profit and the final customer quote; use the same facility in each exhibit. |
| Changing utilisation and EAD | Mwendo Part 1 §1.2.3 and the controlled loss specification §8 already distinguish drawdown and loss. U5's economic-capital and funding discussions include further draws and conversion. | Add dated limit histories, default-sample CCF definitions, expected funded balances and commitment costs to a worked revolving case. |
| Guarantees and recoverability | U5 §§9–9.2, lines 709–781, already specify contract payoffs, recognition boundaries, claims, gross/net loss, delay and counterparty risk. | Extend to a claim-state ledger and numeric fee/delay sensitivity, not another general explanation of why guarantees matter. |
| Recovery economics and sustainable cash | The practitioner article §§2–4 and *Before the Ratio* explain product design and economic cash attribution. U5 §8 measures causal intervention value. | Connect borrower cash capacity to the lender's required price; test the trade-off between a lower payment burden and the cost of carrying exposure. |
| Migration and vintage | Underwrite and the longitudinal research plans already identify state transitions, seasoning and durable outcomes. | Add a transparent matrix example that distinguishes fixed cohort mass from evolving balances; preserve censoring, competing exits and at-risk denominators. |
| SPV and reserves | U5 §§10.1–10.8, lines 824–943, already covers accounts, borrowing base, ALM, notes, reserves, triggers and reporting. M5 §2 and the controlled term sheet supply Mwendo's illustrative structure. | Produce the linked monthly model and payment-date cases. Show what happens to cash after a trigger, not only that a threshold was breached. |
| Financial ownership | U5 §11, lines 994–1071, already assigns intended-use approval and monthly reconciliation. Mwendo Part 4 §1.3.1 assigns operational ledgers and GL boundaries. | Translate this ownership into software input/output contracts and reusable evidence reports. |
| Structural valuation | M5 Appendix A already treats Merton and the physical/pricing-measure boundary. | Geske supplies an optional multi-date contingent-claim extension with a critical-value solver, numerical benchmarks and clearly stated calibration requirements. |
| Syndication, CVA and IRB | These are adjacent institutional-finance applications; they do not define the customer lifecycle. | Retain advanced corporate/treasury modules with separate fees, exposure, accounting and capital conventions. Do not make them prerequisites for MSME collection tools. |

“Already written” means documentary coverage. It does not certify a working implementation, model calibration, achieved outcome or completed transaction.

## 3. Ready-to-adapt whitepaper additions

### A. U5 §2.1 and M5 §1.2.1: reconcile money before comparing rates

**Proposed insertion:**

> A pricing case should begin with dated money amounts. Interest and eligible fees are compared with funding, servicing, expected cash loss and the return required on allocated capital. The balance that earns interest may differ from the exposure that would exist at default, especially for a revolving facility. The worksheet therefore retains expected funded balance, undrawn commitment and conditional default exposure separately. It converts the resulting costs to a spread only after stating the time, day-count and balance basis. Beside this lender view, a borrower cash calendar shows whether the proposed payment dates leave the enterprise enough cash to operate and meet its other commitments.

**Equation and interpretation to place immediately below it:**

$$\Pi_{RA}=I+F-C_{fund}-C_{op}-EL,\qquad EP=\Pi_{RA}-hEC.$$

RAROC is \(\Pi_{RA}/EC\) for the declared convention. U5's existing margin after the capital charge corresponds to an economic-profit-type residual on its stated rate basis; it should not be relabelled as the pre-capital RAROC numerator. Separate any additional commercial margin from the hurdle return already charged. Under a full cash-flow model, derive a hurdle-consistent price from cash dates and the chosen discount/funding convention.

**Exhibit:** Case A and Case B in the [checked casebook](<../../output/pricing_mwendo_underwrite_sokointel_review_2026-09-25/04_WORKED_PRICING_AND_CASHFLOW_CASES.md>). Add a bridge from amounts to rate components; retain the existing U5 reconciliation ownership table.

### B. U5 §§3/5/7 and Mwendo Part 1 §1.2.3: price the unused line

> A credit line is both today's funded balance and a promise about tomorrow's liquidity. A KES 10 million commitment with KES 4 million drawn can earn interest on KES 4 million while exposing the lender to a much larger amount if the borrower draws before default. The pricing case should therefore show income on expected utilisation, the cost of funding expected draws, the cost of maintaining the commitment and loss on the modelled default exposure. A proposed limit change is evaluated as a governed action that may affect business continuity, customer behaviour and future cash; it is not implemented merely by changing the CCF input.

**Implementation extension:** preserve each limit amendment's effective and availability dates, draw permissions, notice terms, cancelled capacity, overlimit balances and observation horizon. Test contractual capacity and observed stress conversion separately. Show sensitivity to low ordinary utilisation and high stress drawdown in the same case.

### C. U5 §§9.1–9.2 and M5 §2.1: measure recovery readiness

> The protection schedule should carry a claim through eligibility, notification, validation, acceptance, payment and final allocation. At each stage it identifies the outstanding amount, supporting evidence, expiry or deadline, expected receipt date and responsible party. This turns nominal cover into a recoverability forecast. The loss model can then show the effect of a delayed or rejected claim, while Treasury shows the funding required before usable cash arrives. Recovery sharing, subrogation and refund allocation ensure that a single receipt is credited once to the party entitled to it.

**Exhibit:** compare identical gross borrower losses under no protection, a partial guarantee with delayed payment, and funded liquidity support. A reserve draw remains a transfer from an existing asset, not income or a recovered borrower payment. Apply the reporting entity's approved IFRS 9 enhancement treatment separately.

### D. U5 §§10.5–10.8 and M5 §§2.1–2.2: make the SPV executable on paper

> Each payment date should be reproducible from five linked records: the eligible asset tape, settled collection accounts, note register, reserve ledger and transaction rule set. Every waterfall step states the opening cash, amount due, amount paid, unpaid amount and next permitted use. When a trigger activates, the model records the rule and effective date, stops or changes purchases as required, and carries the resulting allocation into future months. Residual cash is distributed only after the contractual conditions are satisfied. The report consequently explains both the economic deterioration and the cash action taken in response.

For Mwendo, retain the [controlled term sheet](<../../docs/controlled-specifications/Mwendo_Pamoja_SPV_Financial_Term_Sheet.md>): KES operations; USD-equivalent presentation of 9 million SPV capital; A/B/C amounts 6.75/1.35/0.90 million; HoldCo outside the waterfall; initial illustrative debt-note OC 12/8.1. Do not transplant the paste's corporate project or syndicated loan amounts into this transaction. Include reserve sources in the closing sources-and-uses statement: a starting reserve cannot appear as free cash.

### E. U5 §8 and the practitioner article §6: connect price and intervention to evidence

> The financial case for an intervention depends on what changes relative to a credible alternative. An earlier payment may reduce funding cost without increasing ultimate collection. A hardship adjustment may reduce receipts this month while increasing durable cure and preserving the customer's business. The evaluation should separate accelerated cash, additional cash, treatment cost, funding effects and capital effects, and report complaints and customer outcomes alongside financial value. A favourable prediction does not establish that the proposed action caused the benefit.

**Research connection:** preserve loan-month/event history, assignment and eligibility times, treatment availability, acceptance and execution, competing exits, cash dates, re-default and recovery tail. Fannie Mae/Freddie Mac studies can test mortgage lifecycle methodology; they cannot supply unobserved Kenyan MSME cash provenance, local guarantee claims or randomised treatment effects.

### F. M5 Appendix A and the advanced SokoIntel library

Add a bounded subsection, “Multi-date debt as a contingent-claim problem.” Explain why meeting an intermediate debt payment depends on the continuation value of the enterprise. Define the critical asset-value boundary and numerical solution; distinguish physical default estimation from pricing-measure valuation; describe what observable inputs are required. Place the full derivation and independent numerical checks in an appendix. It is an advanced valuation comparison, not a replacement for the approved HLR, cash-loss engine or observed MSME repayment evidence.

## 4. LinkedIn alignment and paragraph improvements

The earlier gig-economy articles are separate from the more developed MSME whitepaper. Use the current whitepaper and controlled definitions as the basis for their next editorial revision.

| Existing article and passage | Useful revision |
|---|---|
| Part 1, “Triple-Product Capital Stack” and “Partnership Structure,” lines 32–106 | Use the licensed lender/carrier/platform/SPV role map; describe IPF refund eligibility and policy status contractually. Add the funded-versus-committed revolving example. |
| Part 1, “Four Portfolio-Level Mitigations,” lines 187–236 | Explain how a proposed control changes cash, exposure or recovery; show reserve funding and depletion. Present effects as hypotheses to validate and authorised controls to execute. |
| Part 2a, temporal joins and liquidity features, lines 138–211 | Carry economic cash provenance alongside availability time. Define numerator, denominator and horizon for liquidity measures. Explain that avoiding look-ahead bias is one validation control, with out-of-time performance still measured. |
| Part 2b, decision rules and portfolio loss, lines 180–258 | Replace the short payoff illustration with the reconciled pricing case; keep uncertainty, affordability and policy permissions. Reuse the controlled dependence order and tested event-simulation method from the updated whitepaper. |
| Part 3, lines 12–66 | Present the lender's ECL, bank's capital and insurer's IFRS 17 responsibilities separately. Reuse approved intended-use boundaries; remove claims of automatic accounting or capital outcomes from model movement. |
| Standalone Underwrite for Collection, §§2, 8 and 9 | Add one concise pricing/affordability paragraph, the three financial views below and defined contribution/cash-timing measures. |
| Before the Ratio, §§1–3 | Add the pricing consequence of economic classification: borrowed money supports immediate liquidity but is not recurring operating sales and creates repayment obligations. |

**Short paragraph for the standalone article, following §8:**

> The same facility needs three financial views. The borrower needs a payment schedule that fits sustainable operating cash. The lender needs income that covers funding, servicing, expected loss and its chosen capital hurdle. Where receivables support outside funding, investors need cash to arrive in the right account and pass through the agreed payment priorities. Improving one view does not establish the others. A useful underwriting record shows how they reconcile and what changes when collections arrive late.

**Short paragraph for Part 2b, following the decision-value illustration:**

> A risk estimate becomes commercially useful when it changes an explicit cash-flow case. For a revolving line, the balance earning interest today can be much smaller than the exposure outstanding at default. For a secured loan, a valuable asset can still take months to realise. The decision therefore combines risk, exposure, recovery timing, funding and customer affordability, with uncertainty and authority recorded alongside the proposed action.

**Short paragraph for Before the Ratio:**

> Cash provenance also affects price. If a lender treats a new borrowing or a repeated internal transfer as sales, it can overstate repayment capacity and offer a larger facility on a misleading risk basis. Reclassifying those flows does not make the cash disappear. It changes its meaning: some funds are available today because another obligation was created. The pricing and affordability worksheets should receive both views, with unresolved amounts and classification confidence visible.

## 5. Three next articles: developed briefs, not a ceiling

These develop the September 23 ideas; the wider editorial pipeline remains open.

### Article 1 — A credit line has two balances and two cash calendars

**Reader question:** Why can a quoted 16% line fail the lender's return test while also burdening the borrower?

**Proposed length:** 1,200–1,600 words. Open with a distributor awaiting an invoice and using a partially drawn line. Explain funded balance versus default exposure; calculate interest, undrawn fee, funding, servicing, loss and capital. Use Case B's 2.33% illustrative RAROC and 18.59% hurdle-clearing rate, then ask whether that rate is affordable. Compare smaller commitment, altered payment dates, protection and explicitly priced commitment service. End with two aligned calendars and a decision record.

**Whitepaper home:** U5 §2.1 and §7; Mwendo Part 5 §1.2.1. **Soko artifact:** pricing/repayment workbook, CR-FR-003–006. **Evidence needed:** dated utilisation, cash capacity, collection paths and cost allocation. Do not present the hurdle or illustrative rate as a Kenyan market quotation.

### Article 2 — A guarantee has a payment date

**Reader question:** How much does protection improve a facility after fees, exclusions and waiting for cash?

**Proposed length:** 1,200–1,600 words. Start with an accepted claim that has not settled. Follow documentation and entitlement through the claim ledger. Compare gross loss and retained loss; show funding during a delay and the difference between a guarantee and funded support. Add an IPF side case distinguishing insurer liability, net cancellation refund and lender receivable. Close with renewal and recoverability indicators.

**Whitepaper home:** U5 §§9–9.2; Mwendo Part 1 §1.2.1 and Part 5 §2.1. **Soko artifact:** protection contract and cash-timing workbook, CR-FR-008/009. **Evidence needed:** actual coverage terms, claims, rejection reasons, cash receipt and recovery sharing. No automatic LGD or capital benefit is assumed.

### Article 3 — When collections become investor cash

**Reader question:** What makes an apparently attractive receivable pool financeable?

**Proposed length:** 1,400–1,800 words. Start with the same receipts under a normal month and a delayed-remittance month. Follow ownership, eligibility, purchase, account control, expenses, notes, reserve and residual. Trigger early amortisation and show the next month's changed cash. Explain initial OC separately from advance rate and show the sources of reserve funding. Close with the report an investor should be able to reproduce.

**Whitepaper home:** U5 §10; Mwendo Parts 1, 5 and 6, controlled term sheet. **Soko artifact:** cohort/borrowing-base/waterfall model, CR-FR-010–012/018. **Evidence needed:** transaction rules and cash schedules, not a favourable default forecast alone.

## 6. Development order

First reconcile the quantity dictionary and cases. Then use them for whitepaper exhibits and article drafting. Promote validated formula versions into the SokoIntel catalogue, followed by independently checked workbooks and professional functions. Introduce fitted longitudinal risk models only after the deterministic interfaces and data contracts can reproduce the case. This preserves the existing work while creating a clear path from explanation to reusable analytical tools.


---

[Central review and checked examples](<../../output/pricing_mwendo_underwrite_sokointel_review_2026-09-25/00_READ_ME.md>).
