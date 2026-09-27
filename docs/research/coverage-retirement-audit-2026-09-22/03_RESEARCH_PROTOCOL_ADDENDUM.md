# Addendum to the three-paper longitudinal research programme

**Status: specified research and implementation work; no empirical results claimed.** This supplements R5 P0–P15 and the two provider protocols. It changes neither the three-paper division of work nor the main manuscript's 10,000 + 5,000 word contract.

## Placement and ownership

| Addition | Existing research questions | Main-paper placement | Empirical owner / data boundary |
|---|---|---|---|
| V: Vintage, roll rates and cure | RQ2, RQ4 | Literature §2.4; methods §§3.2/3.4; results §§4.1/4.4; lifecycle appendix | Paper 2 primary; Paper 3 cohort/transfer diagnostics |
| F: Information freshness and revalidation | RQ1, RQ8 | §§2.1, 3.2/3.3, 4.1/4.2/4.7 | Paper 1 simulation; later partner workflow study |
| G/I: Origination governance and intervention delivery | RQ1, RQ6 | §§2.1/2.6, 3.5, 4.6 | Paper 1 design/simulation; partner study for causal evidence |
| A: PIT/TTC and accounting bridge | RQ3, RQ5, RQ8 | §§2.3/2.5, 3.6, 4.5/4.7; technical appendix | Paper 3 predictive benchmark; Paper 1 financial sensitivity |
| O/D: Optionality and liquidity-constrained decisions | RQ5, RQ7, RQ8 | §§2.5, 3.6, 4.5/4.7 | Paper 1 scenario work; actual treasury application requires contracts |
| B: Scorecards, monitoring and validation | RQ2, RQ3, RQ8 | §§2.2/2.3, 3.7; diagnostics appendix | All papers under a shared specification |

Use these to replace generic discussion within existing subsection allocations. Detailed data definitions and algebra belong in the existing technical appendices. Report main results only for studies actually run; missing partner data remain a limitation and future study, not a fabricated results section.

## V. Vintage analysis, roll rates and genuine cure

### V1. Cohort and age contract

Define vintage by origination month, with quarter aggregation only under a declared precision rule. Let $v_i$ be origination month and $m$ be months on book (MOB), with origination month $m=0$. If a provider's loan-age field uses another convention, preserve it and explicitly reconcile it to the research convention. Acquisition quarter, first payment month and first observed reporting month are separate dates.

Count unique loan/lineage identifiers, not loan-month rows. In each provider, retain the original cohort size $N_v$, first observable MOB, last observable month, gaps and terminal codes. Late acquisition creates delayed entry. Do not label an unobserved early history as performing. Report an inception-observed cohort separately from a delayed-entry cohort.

A month-by-vintage coverage heat map must precede performance curves. For every displayed point show original size, observed active count, observed exits and unresolved histories. Unknown is a state of knowledge, not current performance or default.

### V2. Distinguish three quantities

For threshold $k$ in the documented monthly delinquency classification, define:

1. **Current prevalence among observed active loans:** $PIT_{v,m,k}=D_{v,m,k}/A_{v,m}$, where $D$ is the active observed count at or above $k$ and $A$ is the active observed denominator. Report loan-count and balance-weighted measures separately; they answer different questions.
2. **Cumulative first crossing:** $F_{v,k}(m)=P(T_k\le m,J=k\mid v)$, where $T_k$ is first threshold crossing and competing terminal events are defined in advance. On a fully observed inception cohort, the descriptive ever-crossed count divided by $N_v$ is available directly. Under censoring or delayed entry, use an explicitly justified competing-risk estimator and report assumptions. An unknown history gives a lower bound on known ever-crossing, not a complete cumulative incidence.
3. **Incremental first crossing:** $\Delta F_{v,k}(m)=F_{v,k}(m)-F_{v,k}(m-1)$. This is an increment in cohort incidence, not the conditional transition hazard. Estimate the latter using the appropriate remaining event-free risk set.

Use provider status categories according to their dictionaries; a monthly category is not a precise daily DPD observation. Never overwrite original codes with assumed equivalence. No-event prepayment is a competing exit for first-distress incidence; administrative data cutoff is censoring. Foreclosure, credit loss, repurchase and other removals follow the provider-specific protocol. Unknown disappearance is investigated separately.

### V3. Why cumulative minus current does not identify cure

With identical original-cohort denominators and complete histories, cumulative ever-90+ minus current 90+ identifies the proportion that previously crossed 90+ and is no longer in that state. It can contain current loans, 30/60-day arrears, prepaid loans, foreclosure or other exits. With active-loan denominators the subtraction also mixes populations.

Example: of 100 loans, 20 ever crossed 90+. Today five remain 90+, four are in lesser arrears, six are current, three prepaid and two exited through foreclosure. The subtraction gives 15%, while only six loans are currently back to current. Even those six have not established durable cure. This is a constructed accounting example, not a portfolio estimate.

### V4. Transition and episode analysis

For consecutive observed months define states current, lesser delinquency buckets, serious delinquency, and documented absorbing/terminal outcomes. Report

$$\widehat P_{ab}(v,m)=\frac{\#\{S_m=a,S_{m+1}=b\}}{\#\{S_m=a,\text{next-month status ascertainable}\}}.$$

Include recorded terminal exits in the next-state counts. Report missing next states and coverage separately, because conditioning on ascertainable status can select the sample. Do not bridge an observation gap as though intermediate states were known. Use an explicit missing-observation likelihood or sensitivity analysis if gaps materially affect the inference.

Identify distress episodes, time in state, improvement, cure confirmation, recurrent distress and terminal resolution. Preserve Paper 2's primary endpoint: **cure confirmed within six months of a serious-distress landmark and 12 subsequent months without renewed serious distress or a credit-related terminal exit**, allowing up to 18 months of follow-up. Retain the protocol's confirmation rule and stricter all-current secondary endpoint. Prepayment is reported separately; it is not silently counted as a durable cure. Repeated episodes require loan/lineage clustering and a declared weighting rule.

### V5. Performance windows and comparisons

Use development cohorts to assess candidate windows such as 6, 12, 24 and 36 MOB. The final choice depends on the endpoint, incremental events, cohort maturity, precision, attrition and operational horizon. Do not adopt the screenshot's 30–35 MOB region as a universal stabilisation point. Do not select a horizon by inspecting final test curves.

Compare vintages at common attained ages and common observable support. Report unadjusted curves and a separately standardised view with a declared reference population. Calendar time, age and vintage obey calendar = vintage + age: unrestricted effects for all three are not separately identified. Specify constraints or a parsimonious model and test sensitivity rather than claiming a unique decomposition.

Required exhibits: cohort/coverage triangle; current and cumulative curves with labelled denominators; incremental crossing plot; roll-rate matrices; cure/recurrence curves; counts at risk; and maturity/sensitivity table. Use uncertainty intervals clustered by loan/lineage and calendar-block sensitivity. Publish both favourable and unfavourable vintages.

## F. Freshness, assessment expiry and revalidation

Record, for each source $j$, economic date, collection time, lawful availability time and last verification time. At proposed disbursement $t_d$, evidence age is $a_j=t_d-t^{verify}_j$. Preserve separate assessment, approval, offer expiry and disbursement timestamps, source-health status, changes since approval, reviewer, exception reason and result.

Define a review gate $R=1$ when a material source exceeds its product-specific approved age, a material event is reported, or a critical source is unavailable. Age limits and triggers are study/policy parameters to be calibrated, not invented legal deadlines. Revalidation can confirm unchanged facts, revise terms through proper authority, refer, or defer. An outage does not automatically justify an adverse borrower decision.

Compare frozen assessment, scheduled refresh and event-triggered refresh under equal information-access and servicing budgets. Primary predictive endpoints: calibration and proper score at disbursement and a common later horizon. Decision endpoints: material changes detected, false escalation, turnaround time, abandonment, review cost and action stability. Track subsequent repayment and customer impact. Avoid treating longer approval delays as randomly assigned; operational difficulty can cause both delay and bad outcomes.

Mortgage monthly observations can test delayed information and update cadence. They do not establish the value of an approval-to-disbursement recheck without actual application/workflow timestamps. Use simulation to vary observation delay, stale covariates and genuine state change independently. A causal policy evaluation needs randomisation or credible identified variation.

## G. Origination integrity and use of proceeds

Extend the partner data request with declared facility purpose, verification evidence, actual disbursement destination, subsequent use-of-proceeds check, facility alternatives, affordability assessment, aggregate debt evidence, application outcome, override owner/reason and the target or incentive regime in force. Use provenance confidence and explicit unknown categories, avoiding inferred intent from an unexplained transfer.

Prespecify whether the question concerns predictive value of evidence quality or the causal effect of an origination policy. Compare purpose-consistent use with later outcomes, accounting for selection and measurement error. An association between overrides and default is not proof that incentives caused default. Retain withdrawn and declined application information where authorised, recognising that counterfactual repayment remains unobserved. Public mortgage fields cannot stand in for KYC quality, business need or employee incentives.

## I. Intervention delivery, promises and relationship outcomes

Before analysing a support intervention, define eligibility and time zero, assignment, permitted alternatives, timing, content, contact channel and capacity. Log offer, attempted contact, delivery, response, acceptance, executed terms, promise amount/date, actual settled and allocated payment, staff actions, direct costs, complaints and repeat contact. Authority to contact an employer or third party is not presumed from a social-media suggestion.

Primary causal reporting follows R5 P10's intention-to-treat design. Keep immediate repayment, durable cure, recurrence, discounted net receipts, relationship retention, business continuity and customer burden separate. A promise to pay is a process measure; fulfilment is an outcome. Twelve-month retention alone can include a persistently distressed customer and is not sufficient evidence of benefit.

Register timing comparisons before the study. The first two weeks is a candidate window, not an established optimum. No required protection is withheld for experimentation. Without assignment/confounder and delivery records, report prediction or association rather than treatment effects.

## A. PIT/TTC, Vasicek and the accounting interface

### A1. Correct factor-model benchmark

For independent standard normal $Z$ and $\epsilon_i$, define latent asset value

$$A_i=\sqrt{\rho_i}Z+\sqrt{1-\rho_i}\epsilon_i,\qquad 0\le\rho_i<1.$$

Default occurs when $A_i\le\Phi^{-1}(p_i^{TTC})$. Conditional on $Z=z$,

$$p_i(z)=\Phi\!\left(\frac{\Phi^{-1}(p_i^{TTC})-\sqrt{\rho_i}z}{\sqrt{1-\rho_i}}\right).$$

The square roots are necessary for unit variance. Positive $z$ is favourable under this convention; an adverse-sign factor reverses the sign consistently. The screenshot's use of correlation in place of its square root and $1-\rho$ in place of $\sqrt{1-\rho}$ is incorrect. The underlying Gaussian-factor framework is explained in the [BCBS IRB technical note](https://www.bis.org/publications/explanatory-note-basel-ii-irb-risk-weight-functions.pdf).

Here $\rho$ is a latent asset-correlation parameter, not an ordinary correlation between one borrower's observed repayment and GDP. A macro-to-factor mapping needs estimation and out-of-time validation. A raw historical default proportion is not automatically a comparable TTC parameter. Align default definition, horizon and population. Adding an arbitrary inverse macro z-score is not a valid alternative derivation.

For Paper 3, compare this transparent benchmark with dynamic hierarchical predictions on identical information. Estimate macro mapping and calibration within development data; assess new vintages, sparse groups and prior conflict. Report whether the benchmark helps. Do not require the main model to conform to a single-factor Gaussian truth.

### A2. ECL bridge

For the general IFRS 9 impairment approach, Stage 1 uses 12-month ECL; Stage 2 uses lifetime ECL after a significant increase in credit risk; Stage 3 concerns credit-impaired assets and also uses lifetime ECL. Twelve-month ECL concerns lifetime shortfalls associated with possible defaults in the next 12 months, not only cash missing during those months. See the [OSFI IFRS 9 guidance](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/ifrs-9-financial-instruments-disclosures) for the accounting concepts; its Canadian supervisory scope is not Kenyan law.

A research decomposition for a performing asset is

$$ECL=\sum_s w_s\sum_{m=1}^{M}q_{m,s}\,\mathbb E[DF_{m,s}EAD_{m,s}LGD_{m,s}\mid T_D\in m,s],$$

where $q_{m,s}$ is **marginal first-default probability**, $w_s$ are scenario weights, and recovery timing is consistently included in conditional severity/discounting. Separate modelling is required where this decomposition does not capture the contractual cash-shortfall definition. Do not sum cumulative PDs across months. Do not double discount recoveries already present-valued inside LGD.

LGD and EAD are not simply known constants when future default, draws, recoveries and costs are unknown. A factor conversion is a model choice, not an IFRS requirement. SICR needs an approved lifetime-risk assessment and relevant evidence; credible-interval width is not a staging rule. The public studies provide methodological tests, not an institution's audited allowance calculation. IFRS 9 and US CECL are distinct frameworks; do not transfer the stage structure to CECL merely because US mortgage data are used.

## O/D. Contractual optionality and funding-constrained decisions

Build an option inventory by legal entity and instrument: holder, right, exercise conditions, notice, penalty, floor/cap, currency, reset, maturity, funded/unfunded status and data source. Include prepayment, extension/modification, revolving draws, cancellation/refund and callable funding where contracts actually contain them. Deposits belong only to an entity with such liabilities. Public mortgage histories do not reproduce Mwendo's complete funding structure.

Compare identical rate scenarios under fixed contractual behaviour, estimated behaviour and stressed behaviour. Recalculate cash profiles, EVE, NII, reserve use, liquidity shortfall and waterfall results. Report curve/basis sensitivities and residual option exposure. Design changes, first-order hedges and explicit options have different costs and effects; do not assume a derivative is required or available. These are consistent with the distinct earnings/economic-value and optionality perspectives in [BCBS IRRBB](https://www.bis.org/basel_framework/chapter/SRP/31.htm?inforce=20191215&published=20191215).

If value is loss-positive as $EaR=NII_{base}-NII_{shock}$, a positive EaR denotes an earnings loss. Use the same sign in explanations and limits.

For capacity $B$ and approved funding usage $f_i$, choose actions subject to $\sum_i f_i(a_i)\le B$. A Lagrange multiplier $\lambda\ge0$ places scarcity cost $\lambda f_i(a_i)$ on the action using funds. This preserves the intended economics and avoids increasing the source's penalty for declining a loan. Compare value, access, liquidity and sensitivity; an estimated predictive model alone cannot establish counterfactual action returns.

## B. Benchmark and monitoring details

A conventional scorecard is an optional transparent comparator. Define WOE consistently, for example $\log(P(bin\mid Y=0)/P(bin\mid Y=1))$. Select bins, smoothing and IV screening using training outcomes only; freeze them for validation/test periods. Report zero counts, missing categories and population drift. IV does not establish causality or fairness.

AUC, Gini ($2AUC-1$ under the same binary ranking convention), KS separation and PSI complement proper scoring and calibration. Distinguish score-separation KS from a reference-versus-current distribution test. Use matured, appropriately defined outcomes and censoring methods where needed. Missing bins, equal-score ties and out-of-range observations require declared handling. Confidence intervals and resampling must respect repeated loans and common calendar shocks.

Acceptance of an advanced model requires a useful gain over simpler alternatives, adequate calibration and uncertainty, operational feasibility and defensible decisions. Passing sampler diagnostics alone does not meet that standard.

## Completion evidence

The following remain execution deliverables: frozen release manifests; validated panel and state dictionaries; vintage/coverage exhibits; leakage and maturity checks; registered comparisons; actual fitted-model diagnostics; holdout estimates with uncertainty; cash reconciliation; and limitations. Partner-only protocols additionally require authorised linked data and a registered study. None is replaced by a mock dashboard or an asserted percentage improvement.

<!-- ADDITIONAL_MATERIAL_2026_09_23 -->

## Additional protocols — 23 September 2026

Apply the [detailed supplement](06_ADDITIONAL_MATERIAL_REVIEW_2026-09-23.md) alongside V/F/G/I/A/O/D/B:

- **RR:** dated recovery-rights/protection evidence; conditional severity, recovery delay and loss validation; selection and availability safeguards.
- **AR:** invoice/order/customer reconciliation and distinct current, prospective, disputed and protected exposure; collection metrics with fixed denominators.
- **ACT:** evidence, review, authorisation, execution and outcome logs; delay and delivery metrics; causal assignment requirements.
- **PM:** applicable-framework check and an eligible-receivables provision-matrix benchmark; historical/current/forecast loss rates and matched longitudinal denominators.
- **PV:** stated/approved/evidenced use, uncertainty and proportional verification; post-disbursement information restricted to later decisions.
- **MC:** preregistered predictive/decision gain, feature durability, operating cost and fallback gates.

These refine existing RQs and appendix allocations. Unavailable legal, invoice, purpose-verification or action histories remain partner-data requirements; public mortgage records do not establish those mechanisms. Canonical manuscript errata and empirical work remain open.
