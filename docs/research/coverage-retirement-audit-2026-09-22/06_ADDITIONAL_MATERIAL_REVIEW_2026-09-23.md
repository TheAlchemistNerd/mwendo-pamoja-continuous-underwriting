# Additional material review: from risk signals to cash decisions

**Prepared for Nevil Maloba · 23 September 2026**

**Status: coverage assessment and proposed protocol additions; no new empirical results.**

## Executive assessment

The new posts reinforce the programme's central proposition: credit quality depends on the fit between financing, changing business conditions, collectability and the decisions made throughout the relationship. They do not require restarting the papers. They do require making several existing ideas more measurable.

The strongest addition is a distinction between **borrower deterioration and deterioration in the lender's recovery position**. The most useful operational addition is to follow a signal all the way to an authorised decision, execution and observed cash outcome. The strongest methodological challenge is that additional model complexity must demonstrate durable value after its data and operating costs.

**Adequately covered in writing** means that the checked sources explain the mechanism and its controls. It does not mean the mechanism has been implemented or validated. The public mortgage experiments remain planned. Trade-receivable, use-of-proceeds and detailed collateral-rights questions need suitable partner data or explicitly labelled simulation.

## 1. Coverage against the six groups of posts

| Supplied material | Existing coverage and evidence | Assessment | Incremental work justified |
|---|---|---|---|
| Rizwan Saud: credit management before sale; sales-to-cash pillars | [U1] §§1 and 3 already connect purpose, product structure, receivables and repayment timing. [U5] §§9–10 distinguish insurance, guarantees, settled cash and eligible collateral. [M0] §§2, 8 and 11 separate observation, loss and accounting ledgers. | Strong lifecycle foundation; trade-credit reporting needs a more explicit contract. | An invoice/order/customer ledger; non-overlapping exposure measures; disputes; agreed collection and ageing denominators. See AR. |
| Luke Sculthorp: continuous credit intelligence must change decisions | [U4] §3 distinguishes evidence, decision, policy and execution times; its responsibility framework assigns business, servicing, model and financial ownership. [U3] §4 constrains feasible actions. Existing addendum F/I covers freshness and delivery. | Already covered architecturally. The useful challenge is whether the control actually operates. | Measure signal-to-review and decision-to-execution delays, unresolved exceptions, overrides and cash outcomes. See ACT. |
| Trudie Wessels: a provision percentage is not a methodology | Existing addendum A and [U5] cover forward-looking loss, cash shortfalls and accounting boundaries. A dedicated receivables provision-matrix protocol was not established in the reviewed programme. | Accounting principle confirmed; a scoped benchmark is an addition. | Applicable-framework decision; historical cohort construction; ageing/segment loss rates; forecast adjustments and backtesting. See PM. |
| Shailaja Amle: early warning must include recovery risk | [M0] §8 separates PD, EAD, cure, recovery and LGD. [U5] §9 already addresses eligibility, exclusions, claim delay, counterparty risk, expiry and actual settlement; §10 addresses enforceability and encumbrances. | Recovery risk is substantially covered. A dated recovery-readiness signal is less explicit. | Track changes in protection and collateral evidence before default; test amount and timing of loss separately from default discrimination. See RR. |
| Igor Vidakovic: sophistication is not automatically better | [M0] §12 explicitly selects the least complex approved model with stable decision value and retains the explicit-only hierarchical fallback. [R5] P8/P14/P15 require validation, economics and update comparisons. | Strongly confirms an existing design rule. | A preregistered complexity acceptance table, including unavailable features, operating cost and fallback performance. See MC. |
| Siddharth Pandey and Sukrit Ghidiyal: purpose, financial fit and observable evidence | [U1] §§1 and 3 link purpose to product and cash generation. [B] §§4–6 distinguish economic provenance, supported classification and uncertainty. Existing addendum G covers use of proceeds. | Substantial conceptual coverage. Verification needs a longitudinal measurement protocol. | Separate stated, approved and evidenced use; reconcile amounts; distinguish missing evidence from misuse; prevent post-disbursement leakage. See PV. |

These findings support retiring the exploratory source as an implementation authority, as the earlier [retirement ledger](02_SOURCE_RETIREMENT_LEDGER.md) recommends. They do not close the [open mathematical and manuscript corrections](04_ACTIVE_WORK_AND_ERRATA.md).

## 2. What should be qualified in the supplied material

1. **A sale converting into cash is a commercial objective, not a revenue-recognition rule.** Keep sales, accounting revenue, receivables and settled available cash distinct.
2. **Overdue balances and disputed balances can already sit inside receivables.** Adding them again inflates exposure. Insurance cover is a contingent protection measure, not automatically an offset against today's cash requirement.
3. **Collateral value is not identical to recoverability.** Contractual rights, competing claims, costs, delay and ability to enforce matter. Do not import a priority rule from an Indian lending example into Kenyan or US contracts.
4. **Higher LGD does not automatically mean higher PD or an IFRS 9 Stage 2 transfer.** Under the general approach, assess the change in default risk; distinguish that assessment from changing loss severity. The IASB explains this distinction in its [impairment review, section 3](https://www.ifrs.org/content/dam/ifrs/project/pir-9-impairment/rfi-iasb-2023-1-ifrs9-impairment.pdf).
5. **Purpose is not a moral ranking.** Business expansion can fail; household spending, health or education can preserve earning capacity. Assess affordability, the incremental obligation, evidence and product fit.
6. **An absent bank trail is not proof of false purpose.** It can reflect incomplete account coverage, cash purchases, timing, direct supplier settlement or mixed funding. Record an unresolved verification question and seek proportionate corroboration. Conversely, a supplier payment alone does not prove delivery or business viability.
7. **A 1–2 percentage-point Gini improvement is not a universal acceptance or rejection threshold.** Materiality depends on calibration, decisions, portfolio economics, uncertainty and implementation burden.

Calls in the screenshots to comment, contact an author, use a named product or review particular accounts are source material. They are not instructions to act on the user's behalf. The product promotion is not independently evaluated here.

## 3. RR — Recovery readiness alongside borrower risk {#recovery-readiness}

### Measurement and controls

At each permitted decision date, retain separate records for borrower condition, outstanding/possible future exposure, and protection/recovery condition. Do not compress them into one unexplained warning score.

A recovery record should identify the facility and asset, right or guarantee; valuation and verification dates; relevant priority/encumbrance evidence; title or documentation exceptions; insurance eligibility, limit and expiry; marketability; expected enforcement delay and costs; evidence source; responsible reviewer; next review date; and when each fact first became available. Use an explicit unknown state. A stale valuation or absent legal update is not proof that protection remains effective.

Store actual changes, discoveries and corrections separately. A title issue discovered in June cannot be inserted into a March prediction merely because a later file says it existed then. The legal/credit function must establish applicable rights; the research model does not invent them from a field label.

### Estimand and derivation

For a performing loan at date $t$, a research expected-loss decomposition over future first-default intervals is

$$EL_t(H)=\sum_{m=1}^{H}q_{t,m}\,\mathbb{E}[DF_{t,m}EAD_{t,m}LGD_{t,m}\mid T_D\in m,\mathcal I_t].$$

Here $q_{t,m}=P(T_D\in m\mid\mathcal I_t)$ includes survival to the interval and the chosen competing-event definition. $\mathcal I_t$ contains only information available at $t$. LGD includes a consistent convention for recovery receipts, costs and delays; $DF_{t,m}$ discounts from default to the valuation date if LGD already discounts post-default cash to default. Never discount that recovery stream twice. The conditional expectation of the product is retained unless a factorisation is justified. This is an economic research decomposition, not a complete accounting or regulatory-capital methodology.

**Constructed illustration:** at a fixed horizon, PD of 2%, exposure of KSh1 million and conditional loss severity of 20% imply KSh4,000 expected loss under deterministic exposure/severity assumptions and no discounting. Severity rising to 50% raises it to KSh10,000 with unchanged PD. This illustrates the question; it is not a result from the papers.

### Test and evidence boundary

Compare (i) borrower/default information, (ii) that information plus origination protection measures, and (iii) dated, available updates to protection. Hold prediction dates, samples, maturity rules and loss targets constant. Evaluate calibration of expected monetary loss, recovery timing, prediction error, concentration of missed losses and review burden, alongside default metrics.

Realised workout LGD is observed mainly among defaulted accounts. Report that selection and incomplete workouts explicitly. Conditional severity performance among defaults does not, by itself, validate a counterfactual LGD for every performing borrower. Aggregate expected-loss validation on the eligible population, sensitivity to observation/selection, and future partner evidence remain necessary. Resample at loan/customer level as available, with temporal stress checks.

Freddie Mac and Fannie Mae experiments may use only documented fields whose availability supports the decision date. Future liquidation expenses or final recovery amounts are outcomes, never pre-default features. Do not claim these public files contain a history of title searches, tax-priority changes or collateral inspection findings. Register the detailed recovery-readiness hypothesis as partner-dependent when those fields are absent.

## 4. AR and ACT — Trade exposure and the completed decision cycle {#trade-exposure}

### A ledger that reconciles

Use customer/economic-group, order, delivery, invoice, allocation, dispute, cash receipt and protection identifiers. Preserve original due dates, authorised amendments, currency, linked credit notes, write-offs, assignments/factoring and data corrections. Show debtor concentration and connected exposures without assuming group links prove shared liability.

Define a prospective trade-exposure view as

$$X_t^{(s)}=AR_t+U_t+O_t^{(s)}-C_t^{(s)},$$

where $AR_t$ is current outstanding invoiced exposure, $U_t$ is delivered but uninvoiced exposure not already in $AR_t$, $O_t^{(s)}$ is additional exposure from presently unfulfilled orders under a stated release scenario, and $C_t^{(s)}$ is eligible payment/credit reduction not already reflected elsewhere. Reconcile transfers among these categories so that delivery and invoicing do not create duplicate exposure. Separate actual cleared reductions from forecast receipts; do not deduct the latter in a current-limit headroom measure as if settled.

Overdue and disputed amounts are **tags/subsets**, not extra additive balances. Show gross exposure, disputed exposure and eligible protection separately; policy terms determine any recognised risk mitigation. Open orders are prospective commitments or contingent business exposure, not automatically booked receivables or regulatory EAD. Apply the actual cancellation/release obligations. The formula is a defined operational view, not a universal accounting identity.

Disputes need reasons: genuine service/delivery issues, documentation errors, pricing disagreements, credit stress or unresolved causes. A dispute is neither automatically default nor proof that the customer is unwilling to pay. Receipt allocation, settlement and unresolved-credit-note controls must precede customer scoring.

### Indicators with denominators

- **DSO:** for the chosen reporting view, period days times average trade receivables divided by credit sales over that period, with consistent tax, currency and perimeter conventions. Also show due-date/cohort measures where growth or seasonality distorts this average. Undefined or tiny sales denominators require flags.
- **Collection realisation:** settled cash allocated to a fixed due cohort divided by that cohort's eligible contractual amount, at specified follow-up horizons. Report credit notes, disputes, write-offs and sales/assignments separately. Define this as a study metric, not an interchangeable version of every published Collection Effectiveness Index.
- **Ageing and concentration:** mutually exclusive age buckets; counts and balances; single-customer and connected-group shares; observed coverage and missing due dates.
- **Utilisation/protection:** compatible exposure and approved limit at the same timestamp; eligible insured amount, policy cap, expiry, exclusions and settlement status. Do not equate sum insured with a collectible claim.

An improving DSO or overdue ratio can arise from write-off, factoring, denominator growth or reclassification. Reconcile its movement to actual collections before concluding collection performance improved.

### ACT: from signal to outcome

For each material signal log: evidence cutoff → detected change → assigned reviewer → authorised decision → execution confirmation → follow-up outcome. Record owner, service deadline, reason, policy/model version, permitted action set, override, customer communication, execution failure and closure evidence.

Measure time to review, decision-to-execution delay, overdue actions, overrides and reversals; also measure cash, durable cure, repeat distress and customer burden. A higher score does not itself authorise a limit cut, a collection escalation or a rejected order. Use existing feasibility and conduct controls and record why no action was appropriate when relevant.

Distinguish an alert's predictive usefulness from an action's causal effect. Observational comparisons of acted-on versus untouched accounts are confounded by targeting. The future partner trial/target-trial protocol must address assignment and outcome maturity. Monthly mortgage records cannot establish a two-day operational service standard or an unobserved phone call's effect.

## 5. PM — A scoped provision-matrix benchmark {#provision-matrix}

The screenshot concerns South Africa's GRAP framework. ASB guidance distinguishes contractual receivables under GRAP 104 from statutory receivables under GRAP 108 and explains lifetime-loss treatment and possible provision matrices for the relevant receivables. It also calls for current and forecast adjustments to historical experience. That is a useful methodological prompt, not authority for applying GRAP to a Kenyan lender. The ASB article is explanatory Secretariat material. [ASB: receivables and revised GRAP 104](https://www.asb.co.za/receivables-in-the-revised-grap-104-what-changed/).

Under IFRS 9, the simplified approach is mandatory for relevant trade receivables/contract assets without a significant financing component, with specified policy choices for those with financing components and lease receivables. It is not a blanket replacement for the general loan impairment approach. [IASB explanation, section 5](https://www.ifrs.org/content/dam/ifrs/project/pir-9-impairment/rfi-iasb-2023-1-ifrs9-impairment.pdf).

Before an experiment, record entity, framework/version, asset class, classification and applicable approach. For an eligible receivables study, a transparent benchmark is

$$\widehat{ECL}_t=\sum_{g,a}B_{g,a,t}\sum_s w_{s,t}\widehat{\ell}_{g,a,t,s},\qquad \sum_s w_{s,t}=1,$$

where $B$ is the reconciled outstanding balance in segment $g$ and age bucket $a$, and $\ell$ is expected remaining lifetime discounted credit shortfall per unit of that balance under scenario $s$. It is a **loss rate**, not simply a default probability. A separate PD/LGD/EAD construction must reconcile to the same target if used.

Freeze segmentation and estimate historical rates from longitudinal invoice/customer cohorts observed at comparable age landmarks, with subsequent cash, adjustments, recoveries and unresolved balances. Align historical denominator and remaining-loss numerator with the current-balance target. Do not divide eventual losses on one origination population by the survivors of another. Account for repeat appearances of an invoice/customer, unresolved follow-up and selection; do not label still-open receivables as zero ultimate loss.

Define discounting and cost treatment for the applicable measurement target. Separate commercial credit notes from credit shortfalls. Estimate current/forecast adjustments using development information, document scenario weights, avoid duplicating a macro adjustment already in the rate, and backtest on later matured cohorts. Report sensitivity to recovery horizons and unsupported segments.

Compare a transparent pooled/segmented matrix with a justified shrinkage challenger only if sample size and objective warrant it. Monetary loss fractions are not Bernoulli loan outcomes; do not attach a binomial likelihood to fractional balance-weighted losses without an appropriate observation model. No invented ageing percentages, compliance claim or mortgage-to-trade-receivables transfer is warranted.

## 6. PV — Purpose verification as longitudinal evidence {#purpose-verification}

Record **stated purpose**, **approved purpose**, **permitted use**, **observed allocation**, **evidence coverage** and **subsequent operating outcome** separately. Mixed-purpose loans need proportions or ranges and a source, not a forced single label.

At application, retain the requested amount, need, proposed suppliers/assets, expected cash-generation or preservation mechanism, other obligations and available corroboration. After disbursement, at registered observation dates, reconcile attributable proceeds into mutually exclusive supported uses, supported alternative uses, identifiable unspent amounts and unresolved amounts. Where money is fungible or accounts are incompletely observed, report an allocation range instead of false exact tracing.

Triangulate consented account evidence with invoices, delivery/asset evidence and counterparty checks where appropriate. Record confidence and reviewer corrections. Missing data should trigger a coverage flag and proportionate review, not an automatic accusation. Measure monetary classification error and adjudicator disagreement on a held-out, blinded verification sample; a repayment outcome is not a gold-standard purpose label.

Origination models use only evidence available before their decision cutoff. Later verified use may enter a later landmark forecast; it cannot be retroactively supplied to the origination model. Separate purpose's predictive association from causal claims about what would happen if a borrower chose a different use. Purpose choice, affordability, product selection and approval all create selection problems.

The mortgage files' documented loan-purpose category is not a verified SME use-of-proceeds trail. Do not equate a refinance code with consumption, misuse or business investment. This protocol belongs in the measurement framework and a future partner study; synthetic examples must be labelled.

## 7. MC — Make added complexity earn its operating cost {#model-complexity}

Retain the existing explicit hierarchical model and simpler conventional comparators. Fit and select challengers inside the development period; lock the out-of-time evaluation and its practical acceptance thresholds before examining test outcomes. Use the same eligible population, feature availability, outcome horizon and operational constraints.

| Gate | Evidence required |
|---|---|
| Predictive value | Calibration, proper prediction scores and discrimination with paired uncertainty; subgroup and later-vintage performance; all registered comparisons |
| Decision value | Relevant loss/cash or constrained policy-value estimates under stated identification assumptions; alert/review capacity and customer outcomes |
| Data durability | Availability and latency by source; missing-source stress; revision sensitivity; drift and replacement plan |
| Operating burden | Inference/refitting time, data fees, infrastructure, human review and maintenance; reproducible cost basis |
| Explainability and control | Reasons for changed risk, feature/decision lineage, independent reproduction, approved fallback and documented override |
| Resilience | Replay with stale/unavailable inputs; safe fallback performance; recovery after source or model failure |

A study can compare

$$\Delta V_{net}=\Delta V_{decision}-\Delta C_{data}-\Delta C_{compute}-\Delta C_{review}-\Delta C_{maintenance}.$$

State whose value is measured, its horizon and uncertainty; avoid double-counting costs already in decision value. Legal, conduct and required control constraints remain gates, not prices that a larger profit can cancel. If causal decision value is unidentified, report scenario/sensitivity estimates rather than realised benefits.

Accept a challenger only when the preregistered evidence supports material, stable improvement and the control requirements. A negative finding is useful: the simpler approved model may remain preferable. Equally, a small aggregate gain can matter for a costly subgroup, so simplicity is a benchmark discipline rather than a predetermined winner.

## 8. Placement in the existing three-paper programme

| Existing destination | Integrate within the allocation | Planned evidence |
|---|---|---|
| Main paper §§2.1, 3.3, 4.1–4.2; RQ1–RQ2 | PV measurement/coverage; AR cash definitions; MC complexity comparison | Conceptual derivations, registered simulation; partner validation explicitly conditional |
| Main paper §§2.5, 3.4, 4.5; RQ5 | RR loss severity and recovery timing; contingent protection; PM as a scoped comparator | Matched cash/loss targets, available public fields and clearly labelled scenarios |
| Main paper §§2.6, 3.5, 4.6; RQ6 | ACT assignment, execution and outcome distinction | Existing causal protocol; no causal result from unobserved actions |
| Main paper §§2.7, 3.7, 4.7; RQ7–RQ8 | Updating/feature outage, decision delay, net complexity value | Sequential comparison with matured labels and operating-cost assumptions |
| Appendices A/D/F/G/J | Measurement uncertainty; availability clocks; joint loss/exposure reconciliation; action value; validation details | Reuse existing 600/400/550/500/450-word allocations; retain total appendix budget |
| Freddie Mac paper | RR where dated fields support it; monetary loss/timing; MC acceptance; preserve vintage and durable-cure endpoints | Longitudinal mortgage panel; detailed legal/title and invoice workflows excluded without data |
| Fannie Mae paper | Prior transport/conflict and sparse-group uncertainty; MC costs/robustness; availability-aware loss extensions where feasible | Existing transfer design; no claim of SME purpose or GRAP validation |

The main paper remains **10,000 body words plus 5,000 appendix words**. These additions refine the existing questions and exhibits. The two companion papers keep their separate contributions. A provision-matrix or trade-credit application should not crowd out the central mortgage experiments merely because it appears in a screenshot.

## 9. Priorities and completion evidence

1. **Before data modelling:** add RR/AR/PV fields to the variable and availability register, mark unavailable fields, and settle loss/receipt/cost definitions. Confirm the entity/framework boundary for PM.
2. **Before evaluating challengers:** freeze MC thresholds and cost assumptions, split rules and proposed loss targets. Preserve existing vintage, censoring, cure and label-maturity requirements.
3. **Before operational or causal claims:** obtain authorised partner histories for rights, invoice allocation, purpose verification and executed actions; register assignment/selection assumptions and outcome follow-up.
4. **Before claiming completion:** produce reconciled cohort tables, loss and cash backtests, decision logs, uncertainty and sensitivity results. The screenshots and this review provide no such empirical results.

No canonical series chapter was rewritten by this supplement. The changes are integrated into the research outline, companion-protocol notices, shared protocols and review navigation. Earlier errata remain open until their manuscript equations and builds are corrected.

## 10. Screenshot provenance and review limits

The 13 supplied images form six topical groups; several are overlapping captures. Image numbers here follow the order in the user's latest message.

| Images | Visible source | Treatment |
|---|---|---|
| 1, 8 | Rizwan Saud text and sales-to-cash infographic | One conceptual group |
| 6, 2 | Luke Sculthorp opening and continuation | Read in this order; promotion not independently verified |
| 3 | Trudie Wessels / Ducharme, GRAP 104 | Checked against ASB and IASB explanatory sources |
| 4, 5 | Shailaja Amle recovery early warning | Opening and continuation |
| 7 | Igor Vidakovic model complexity | Visible post; cropped ending not reconstructed |
| 12, 11, 13, 9, 10 | Siddharth Pandey purpose post/graphic; Sukrit Ghidiyal comment | Overlap consolidated; comment distinguished from original post |

Relative labels such as “1d” do not establish publication dates. No original LinkedIn URLs were supplied for these posts. The [screenshot manifest](additional_material_manifest.json) records exact attachment names and hashes; copies preserve the supplied images. This is a targeted extension to the earlier audit, not a claim to have repeated the full 1,765-paragraph source review or reread every manuscript line today.

## Local sources

The links below identify the checked source documents. Section references in the matrix locate the relevant material. Their claims and planned designs are not treated as implementation evidence.

- [M0] — Controlled credit-risk model and loss architecture.

[M0]: <../../controlled-specifications/CREDIT_RISK_MODEL_AND_LOSS_ARCHITECTURE_SPECIFICATION.md>

- [U1] — Underwrite for Collection Part 1.

[U1]: <../../../behavioural%20credit%20scoring%20-%20underwrite%20to%20collect%20rct/series/parts/Part_1_MSME_Credit_Lifecycle_and_Collection_Cascades.md>

- [U3] — Underwrite for Collection Part 3.

[U3]: <../../../behavioural%20credit%20scoring%20-%20underwrite%20to%20collect%20rct/series/parts/Part_3_Regulatory_Orchestration_Fair_Intervention_and_Collection_Governance.md>

- [U4] — Underwrite for Collection Part 4.

[U4]: <../../../behavioural%20credit%20scoring%20-%20underwrite%20to%20collect%20rct/series/parts/Part_4_Bank_Controlled_Research_Sandboxes_and_Enterprise_Credit_Architecture.md>

- [U5] — Underwrite for Collection Part 5.

[U5]: <../../../behavioural%20credit%20scoring%20-%20underwrite%20to%20collect%20rct/series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md>

- [B] — Before the Ratio: entity-resolved cash-flow article.

[B]: <../../../publications/linkedin/BEFORE_THE_RATIO_ENTITY_RESOLVED_CASHFLOW_UNDERWRITING.md>

- [R5] — Shared research protocols P0-P15.

[R5]: <../../../output/credit_lifecycle_research_plan_2026-09-21/05_SHARED_RESEARCH_PROTOCOLS.md>
