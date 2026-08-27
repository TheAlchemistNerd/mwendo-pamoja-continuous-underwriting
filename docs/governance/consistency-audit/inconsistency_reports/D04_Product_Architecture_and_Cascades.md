# D04 Inconsistency Report: Product Architecture and Cascades

## Document role and semantic synopsis

D04 explains the product system that creates the SPV assets: insurance premium financing, microloans, and revolving credit. It also describes platform collection, reserve pockets, external shocks, and a correlated multi-product default cascade. This paper should be the authoritative source for product cash flows and causal mechanisms. It succeeds in showing why a driver is one operating cash-flow unit rather than three independent credit products. However, damaged equations, unstable party labels, unsupported dependency claims, and a confusing use of “capital stack” prevent it from serving as a reliable product specification.

The paper's causal narrative is plausible: fuel, commissions, downtime, regulatory change, or insurance loss can reduce net income; the driver draws working capital, misses repayments, loses cover, and may be deactivated. The current text turns that plausible mechanism into deterministic mathematics, sometimes using formulas whose subtraction signs were replaced by commas.

## Executive inconsistency summary

The highest-priority defects are computational. Net income, unearned premium, haircut, reserve, and other formulas contain punctuation corruption that changes their meaning. The “Triple-Product Capital Stack” confuses asset products with financing tranches. The Insurtech is sometimes the policy issuer despite the carrier structure in D01 and D07. Platform escrow and routing powers are assumed rather than contracted. Default correlation is said to converge to one and a Clayton parameter is tied mechanically to shock severity without calibration. The paper also lacks precise contracts, product ledgers, event timing, and customer-protection controls.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D04-I01 | Critical | High | Product sections and cascade formulas | Corrupted arithmetic changes product economics |
| D04-I02 | High | High | “Triple-Product Capital Stack” | Assets and liabilities are conceptually confused |
| D04-I03 | Critical | High | IPF and partner sections | Policy issuer and insurance responsibilities drift |
| D04-I04 | High | High | Microloan and escrow sections | Collection priority and platform authority are unproven |
| D04-I05 | High | High | External shock section | Benchmark reset and borrower repricing are overstated |
| D04-I06 | High | High | Diversification illusion section | Correlation convergence is presented as theorem |
| D04-I07 | High | High | Copula discussion | Shock severity is not a calibrated Clayton parameter |
| D04-I08 | High | Medium | Product mechanics | Default, cancellation, recovery, and draw events lack definitions |
| D04-I09 | Medium | High | Reserve pockets and interventions | Customer safeguards and accounting are incomplete |
| D04-I10 | Medium | High | References and notation | Evidence and symbols are not auditable |

## Detailed findings

### D04-I01: Formula corruption changes the stated mechanics

**Anchor:** “The Gig Driver as a Unified Asset Class,” “Insurance Premium Financing,” “Anatomy of an External Shock,” and “Collateralized Reserve Pockets.” Several expressions use commas where subtraction is intended. Examples include net income that should deduct commission, operating expense, and repayments; an unearned-premium expression that should use `1 - t/T`; a haircut that should use `1 - delta`; and a reserve roll-forward that should deduct paid claims or principal outflows.

**Impact:** These are not cosmetic defects. A comma can turn an arithmetic expression into an undefined list. The resulting model may add costs, overstate collateral, or fail to reduce reserve balances. The same punctuation corruption appears in D05 through D09, suggesting a corpus-wide transformation error.

**Canonical resolution:** Reconstruct each formula from defined variables, dimensional analysis, and the intended cash flow. For example:

```text
I_net,t = gross_fares_t - platform_commission_t - operating_cost_t - debt_service_t
UP_t = initial_premium * max(0, 1 - elapsed_days_t / policy_term_days)
net_recovery_t = gross_refund_t * (1 - administrative_haircut)
reserve_close_t = reserve_open_t + deposits_t + interest_t - permitted_releases_t
```

Add units and acceptance examples. Do not infer the precise legal refund formula from this simplification; carrier terms control.

### D04-I02: Product pool is mislabeled as a capital stack

**Anchor:** “The Triple-Product Capital Stack.” IPF, microloans, and revolving credit are asset products or receivable types. D03's Class A, B, and C are the capital stack.

**Impact:** The label invites readers to treat product diversification as structural subordination. It also obscures that the three products may be owed by the same driver and therefore have correlated exposure.

**Canonical resolution:** Rename the section “Three-Product Receivables Pool” or “Integrated Driver Product Suite.” Add a separate bridge showing how product balances fund the Class A, B, and C liabilities. State product-specific eligibility, yield, tenor, default, recovery, and concentration.

### D04-I03: Policy issuance and insurance accounting are assigned inconsistently

**Anchor:** “Product 1: Insurance Premium Financing,” “Partnership and Counterparty Structure,” and “Insurance Premium Financing Operational Asset Structure.” The paper sometimes says the Insurtech issues the policy. D01 identifies a carrier partnership, while D07 alternates between Insurtech and carrier under IFRS 17.

**Impact:** Policy issuance is a licensed activity. The entity that bears insurance risk determines customer rights, premium refund, cancellation, claims, reserves, and IFRS 17 accounting [6]. The SPV normally owns a financing receivable, not the insurance contract risk.

**Canonical resolution:** State that the licensed carrier issues and administers the insurance contract. The originator or SPV finances premium payment under a separate credit agreement. The technology provider supplies data and services only within agreed authority. Map cash and accounting among driver, carrier, originator, SPV, and servicer.

### D04-I04: Escrow priority is called inherently senior

**Anchor:** “Microloan Repayment Mechanics” and “Direct Platform Escrows.” The text assumes fare deductions and calls them constitutionally or structurally senior without an executed platform agreement, customer authorisation, account-control arrangement, or legal analysis.

**Impact:** Platform wallet funds may be subject to driver rights, set-off, other lenders, taxes, fees, attachment, and consumer-protection restrictions. Aggressive deductions can reduce subsistence and increase adverse behaviour. Seniority is legal and contractual, not a property of an API.

**Canonical resolution:** Describe escrow or split-settlement as a proposed collection mechanism. Specify consent, maximum deduction, priority, sufficiency floor, notices, revocation, disputes, refunds, platform insolvency, reconciliation, and fallback collection. Obtain Kenyan legal advice and platform commitment before treating it as credit enhancement.

### D04-I05: A KESONIA change is assumed to pass instantly to borrowers

**Anchor:** “Anatomy of an External Shock.” The cascade uses a benchmark spike as an immediate borrower cost shock, sometimes described as predatory repricing. CBK's framework defines the reference and premium, but contractual reset frequency, notice, floors, caps, and product scope determine transmission [1]-[3].

**Impact:** Stress timing can be materially wrong. A monthly-reset loan does not reprice on every daily observation, and a fixed-rate or foreign-currency facility is outside the same formulation.

**Canonical resolution:** Model rate shock by contract: benchmark observation period, compounding, reset date, notice, floor, cap, and remaining tenor. Separate lawful benchmark pass-through from discretionary changes to `K_RBCP`. Use scenario language rather than “predatory” unless evidence supports misconduct.

### D04-I06: Default correlation convergence is unsupported

**Anchor:** “The Diversification Illusion: Endogenous Default Correlation.” The paper argues that common shocks cause correlations to converge toward one as if this were a general mathematical result.

**Impact:** Tail dependence can rise materially without pairwise default correlation reaching one. A deterministic claim overstates the case and may produce excessive or misdirected capital assumptions.

**Canonical resolution:** Reframe as a testable hypothesis: exposure to common fuel, platform, geographic, and regulatory factors can increase conditional dependence. Estimate joint default and transition rates by product, driver, cohort, platform, and shock regime. Report uncertainty and compare dependence families.

### D04-I07: Clayton parameter is mechanically linked to shock severity

**Anchor:** Cascade and diversification sections. The narrative implies that a more severe macro shock directly chooses a higher Clayton `theta`. D06 repeats the copula as the preferred tail model.

**Impact:** Copula parameters describe dependence after marginal distributions are specified. They are estimated or stressed, not calculated merely from a fuel-price shock label. Clayton emphasises lower-tail dependence under a chosen orientation and may not fit all product pairs.

**Canonical resolution:** Estimate product-pair and cohort dependence from joint outcomes, transform consistent marginal residuals, and compare Clayton, Student-t, Gaussian, Gumbel, and vine models. Use macro variables in marginal and parameter models where evidence supports time variation. Feed the resulting loss distribution into D03's waterfall without claiming proof of protection.

### D04-I08: Product state transitions are not contract specifications

**Anchor:** All three product sections. Terms such as arrears, default, cure, cancellation, full draw, utilisation trap, recovery, premium holiday, and reserve depletion lack precise time and ledger definitions.

**Impact:** D05 cannot build point-in-time features, D06 cannot define labels, D08 cannot post journals, and D03 cannot write eligibility tests without a common state machine.

**Canonical resolution:** Add one state-transition table per product with event, effective time, ledger entry, cash consequence, accounting consequence, eligibility consequence, customer notice, and cure. Distinguish missed instalment, days past due, default, write-off, restructuring, and recovery. For IPF, distinguish policy cancellation, unearned premium, carrier refund, refund receivable, and collected refund.

### D04-I09: Reserve pockets and interventions lack safeguards

**Anchor:** “Collateralized Reserve Pockets” and portfolio mitigation. The reserve is described mainly as a credit tool, with limited treatment of ownership, permitted use, consent, liquidity, and hardship.

**Impact:** If the balance is the driver's property, it may not be SPV collateral. If mandatory, it may alter total cost and affordability. Automated depletion or freezing can harm customers and create complaints or forbearance concerns.

**Canonical resolution:** Define legal owner, custody account, segregation, interest, withdrawal rules, lien, disclosures, priority, hardship exception, death or exit treatment, and data reporting. Separate driver reserve pockets from the SPV cash reserve account.

### D04-I10: Notation and references do not support implementation

**Anchor:** “References” and formulas throughout. Symbols are introduced locally, reused, or damaged; citations often support broad market context but not the causal or quantitative claim attached.

**Impact:** Downstream technical and financial papers can reproduce different meanings. An engineer cannot turn narrative into validated product events.

**Canonical resolution:** Add a symbol table with units, sign convention, frequency, and source. Attach each external claim to the IEEE index. Treat [31] as scenario context and [1]-[3] as benchmark authority. Label all portfolio values as illustrative pending data.

## Cross-document dependencies and evidence gaps

D04 supplies definitions to D03's eligibility and waterfall, D05's event schema, D06's labels and dependence data, D07's intervention controls, D08's ledgers, D09's cash-flow pricing, and D10's pilot tests. Diligence requires sample product contracts, carrier policy wording, refund rules, platform settlement specifications, collection priority opinion, wallet and loan event dictionaries, historic states and recoveries, customer disclosures, consent language, and intervention outcomes.

## Prioritised remediation sequence

First repair formulas and establish a product symbol dictionary. Second settle counterparty and policy-issuer roles. Third write product state machines and ledger events. Fourth define collection and reserve controls. Fifth replace deterministic cascade and copula statements with estimable hypotheses. Sixth connect products to the SPV borrowing base and lender model. Last, qualify evidence and references.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D04-I01 | D04-P02, D04-P05, D04-P08 |
| D04-I02 | D04-P03, D04-P09 |
| D04-I03 | D04-P04 |
| D04-I04 | D04-P04, D04-P07 |
| D04-I05 | D04-P06 |
| D04-I06 | D04-P06, D04-P08 |
| D04-I07 | D04-P08 |
| D04-I08 | D04-P03, D04-P05 |
| D04-I09 | D04-P07 |
| D04-I10 | D04-P01, D04-P10 |
