# Source retirement ledger and corrections

## Decision

Retire the original continuous-underwriting dialogue as an active technical specification. Preserve the complete DOCX and extracted text as historical provenance. Its useful questions survive in the current papers and the new addendum; its code, invented evidence and blanket compliance claims must not be carried forward as validated work.

The table below covers **P0001–P1765 without gaps or overlapping ranges**. The accompanying TSV attaches every numbered paragraph to its disposition, replacement and review note. Repeated search snippets, conversational questions, tables, code and slide material remain in the transcript. Retirement means superseded as authority; it does not mean deleted or empirically disproved in every detail.

| Source paragraphs | Disposition | Subject | Current replacement / destination | Review finding |
|---|---|---|---|---|
| P0001–P0094 | Retire overview and search fragments | Hierarchy and Bayesian modelling foundations | M0 §§3–6; M2b §§1–3 | Keep the question of sparse-group reliability. Replace claims that hierarchy prevents overfitting, guarantees compliance or provides causal explanations with registered comparisons. Search snippets are leads, not verified literature. |
| P0095–P0195 | Retire architecture advocacy | GRU, Transformer and hierarchical combination | M0 §§4–6; M2a §§5–6; R5 P15 | Retain encoder ablations and training-only residualisation. Short/long horizon roles are hypotheses. A frozen neural encoder does not propagate all neural uncertainty. |
| P0196–P0252 | Replace faulty timing and decision arguments | Mixed frequencies and uncertainty thresholds | M0 §2; M2b §4; R5 P2/P14 | Use availability-time joins. A monthly figure may not be available during its reference month. Keep mean-payoff and uncertainty constraints separate; widening a posterior does not mechanically imply rejection. |
| P0253–P0310 | Retain missingness question; replace implementation | Asynchronous inputs and fallback | M0 §§2, 5, 10; R5 P6/P15 | Separate source outage, reporting lag and borrower missingness. Missing bureau data does not establish concealment or identify MNAR. Test fallback calibration and action burden. |
| P0311–P0358 | Replace probability dynamics and stress shortcuts | Microloans, revolving use and shocks | M0 §§7–9; M5 §§1–2; R5 P13/P14 | One repayment need not collapse posterior uncertainty. Put a random walk on an unconstrained latent scale, not directly on PD. Preserve product-specific exposure and funding scenarios. |
| P0359–P0461 | Retire examples; retain corrected payoff derivation | VaR, posterior prediction and product economics | M2b §4; M0 §§8–11; addendum A | Use predictive loss quantiles and consistent payoff horizons. Distinguish a chance constraint from expected value. Reconcile fees, interest, losses and recoveries across states. |
| P0462–P0525 | Retain economic question; rederive | Drawdown, default timing, liquidity and fairness | U5 §§6–8; R5 P14; addendum D | Use a joint timing/exposure process. Realised future default time is unavailable at scoring. Liquidity scarcity is a cost/constraint on approval; raising the cost of denial makes approval more permissive. |
| P0526–P0642 | Retire code and automatic-action claims | Fairness threshold optimisation and restructuring | M3 §5; U3 §4; R5 P10–P11 | Hard-threshold objectives are often piecewise constant, making generic gradient optimisation unsuitable. Empty groups cannot establish fairness. Offers need authority, customer response and proper accounting, not silent conversion or balance-zero SQL. |
| P0643–P0718 | Retire accounting and capital shortcuts | IFRS 9, Basel and short-tenor claims | M0 §11; M3 §2; U5 §§3–5; addendum A | ECL is not regulatory/economic capital or a cash reserve. SICR is not a posterior interval rule. Model correlation and prescribed prudential correlation are different. Applicability belongs to the legal entity and approved use. |
| P0719–P0806 | Retire illustrative audit conclusions | SHAP, CCF and fairness/audit templates | M0 §§8, 10–12; M4 §§2–3 | An attribution is not a causal explanation. No universal 40% CCF follows from a revolving label. High utilisation does not determine residual conversion. Numeric compliance and fairness assertions are illustrations without evidence. |
| P0807–P0944 | Retain monitoring requirements; replace guarantees | Logs, SHAP latency, PSI and statistical tests | M4 §3; M2b §§3, 6; R5 P8/P15 | SQL tables alone are not immutable. Latency must be benchmarked. Distribution tests require dependence/multiplicity treatment. PSI cutoffs are conventions; an ADF result does not validate a credit model. |
| P0945–P1002 | Retain institutional boundary correction | Lender identities and Kenyan applicability | M3 §1; active DCP positioning note | Keep institution-neutral methodology distinct from a DCP-led implementation and bank-owned prudential processes. Do not generalise legal duties from brand names or invented delinquency cutoffs. |
| P1003–P1071 | Retain complementarity; retire equality claim | Accounting and capital interaction | M0 §11; U5 §§3–5 | Shared evidence can feed distinct measures. Accounting ECL cannot simply be subtracted from an arbitrary VaR to obtain economic capital; horizon, loss basis and expected-loss definition must reconcile. |
| P1072–P1142 | Retire policy assertions and arbitrary formula | Conservation-of-risk narrative and TTC scaling | U5 §§3–5; R5 P3/P14; addendum A/D | No general rule forces identical distributions across all functions. A group intercept transformed by sigmoid is not portfolio TTC PD. Log-confidence scaling can be singular or negative and is not a regulatory standard. |
| P1143–P1255 | Retire code; retain validation checklist | PSI implementation, cost of equity and audit runbook | M2b §6; U5 §§7, 11; addendum B | Handle tied/empty bins, out-of-support observations and normalised smoothing. Leverage-based cost-of-equity formulae need assumptions. An audit template is not proof of legal compliance. |
| P1256–P1375 | Retire slides and deployment commands | Outage stress, automatic cuts and MCMC | M0 §§6, 10, 12; R5 P7/P15; addendum F | Do not interpret infrastructure blackout as borrower misconduct. Replace hardcoded 30% cuts with tested fallback policies. NUTS tuning and draw counts do not guarantee diagnostics or legality. Embedded system commands remain inert source text. |
| P1376–P1450 | Retire duplicated slides and mock model | PyMC demonstration | M0 §§3–6; R5 P7/P9 | Mock outcomes independent of features do not validate predictive signal. Identify global and group intercepts; validate the hierarchy through meaningful data-generating experiments. |
| P1451–P1586 | Rebuild selected derivations | Inflation, SQL joins, PiT adjustment and noncentering | M0 §2; R5 P2/P7; addendum A/D | Do not divide by zero/negative baseline inflation or reverse a multiplier without a defined objective. Report-month joins can leak future releases. Noncentering changes computation, not economic identification. |
| P1587–P1765 | Retire mock evidence; preserve release questions | Dash demonstration, stress table and production checklist | M0 §§10–12; M4 §3; R5 P7/P15 | Random SHAP values are mock graphics. Assumed shock transmission, optimal coefficients, NPL and solvency figures are not findings. Keep traceable validation, fallback, parity and approval deliverables. |

## Corrections that matter to the research

### 1. Bayesian structure does not establish usefulness by itself

Partial pooling can improve estimates when groups share information in a defensible way; incompatible groups or bad priors can make it harmful. Latent neural coefficients complicate interpretation. Neither hierarchy nor a posterior establishes causal identification, fairness or regulatory approval. Keep the pooled, explicit-only and tree comparators under matched data and tuning budgets. RQ2–3 already provides this falsifiable structure.

A deterministic encoder feeding a Bayesian final layer supplies conditional uncertainty about that layer. It does not automatically integrate encoder training uncertainty, data-linkage uncertainty or model-form error. Label which uncertainty is included and test omitted uncertainty separately.

### 2. A wider posterior is not automatically a reason to decline

Suppose approving yields net gain $G$ if the borrower performs and loss $L$ on default; declining costs $O$ only when the borrower would have performed. All quantities use the same horizon and valuation basis. For posterior mean PD $\bar p$,

$$EU(approve)=(1-\bar p)G-\bar pL,\qquad EU(decline)=-(1-\bar p)O.$$

The approval threshold is

$$\bar p\le p^*=\frac{G+O}{G+L+O}.$$

Posterior variance does not enter this linear-payoff result. A probability-of-exceedance gate, nonlinear loss or value-of-information policy can depend on uncertainty, but that is an additional decision rule with a stated rationale. In P0462–0525 the source makes funding scarcity raise $O$ and interprets the result as tighter lending. Yet

$$\frac{\partial p^*}{\partial O}=\frac{L}{(G+L+O)^2}>0.$$

A funding cost belongs in the approval cash flows or a portfolio capacity constraint. Moving it to the denial penalty reverses the intended effect. This is a derivation, not an estimated empirical result.

### 3. Probability, timing and missingness need coherent support

A Gaussian random walk applied directly to PD can produce values below zero or above one. One admissible alternative is a latent process $\eta_t=\eta_{t-1}+\epsilon_t$, with $p_t=\operatorname{logit}^{-1}(\eta_t)$. Its innovation scale and predictive value still need estimation. A repayment does not guarantee that uncertainty shrinks; a regime change or contradictory evidence can widen it.

A missing-data flag can be useful without establishing why an observation is absent. Source outage, a delayed bureau update and deliberate non-disclosure are different mechanisms. Calling the last mechanism MNAR does not identify it from missingness alone. Evaluate scenarios, alternative assumptions and observed source health. Monthly reference dates cannot replace lawful availability dates in historical joins.

### 4. Loss prediction, quantiles and capital are distinct

For posterior predictive loss $\mathcal L$, define

$$\operatorname{VaR}_{\alpha}(\mathcal L)=\inf\{x:F_{\mathcal L}(x)\ge\alpha\}.$$

Equality $F(x)=\alpha$ need not hold for a discrete loss distribution. An interval for a parameter or PD is not a predictive quantile of portfolio loss. Exposure, default timing, recovery, costs and shared shocks also matter.

Similarly, $\mathbb E[\psi(T)]$ generally differs from $\psi(\mathbb E[T])$. A nonlinear revolving-exposure function cannot replace unknown future default time with its mean without quantifying the approximation. Recovery and default timing should be simulated jointly where dependence matters.

An economic-capital convention such as $\operatorname{VaR}_{\alpha}(\mathcal L_H)-\mathbb E[\mathcal L_H]$ uses a single declared loss basis and horizon. IFRS 9 ECL is not interchangeable with that expectation. Provisioning, capital resources, contractual credit enhancement and available liquidity each have different purposes and constraints; M0 §11 and U5 §§3–6 already preserve them.

### 5. Fairness and interventions require observations and authority

A squared equalized-odds penalty in a demonstration is not a compliance certificate. Hard classifications produce a discontinuous or piecewise-constant objective; optimiser success flags do not prove an optimum. Undefined subgroup rates must be reported as undefined, with denominators and uncertainty. Approval selection also means repayment labels are unavailable for many declined applicants.

Contract change must preserve the offer, legal authority, customer response, schedule, effective date, accounting assessment and complete ledger entries. Setting a loan balance to zero is not a restructuring journal. A GRU state is not automatically an income forecast. A model threshold is not consent. M3 §5 and U3 §4 already provide the corrected decision boundary.

### 6. Diagnostics are evidence about computation and data, not certification

PSI depends on binning and reference populations. Tied quantiles, empty bins and values outside the reference range must be handled. Distribution change is neither automatically bad credit quality nor proof that retraining is useful. Repeated tests on dependent data need a monitoring design; univariate KS or ADF tests cannot validate an entire high-dimensional model.

The source's fixed chain counts, target acceptance and ESS thresholds should become method-specific validation criteria with Monte Carlo precision targets. Modern rank-normalised $\hat R$, bulk/tail ESS and sampler diagnostics help diagnose sampling; none proves real-world calibration. See [Stan's diagnostic guidance](https://mc-stan.org/learn-stan/diagnostics-warnings.html).

A SQL table does not create immutability. A millisecond SHAP claim needs measured hardware, batch size, explanation method and tolerances. A dashboard displaying random explanation values remains a mock. Stress outcomes and compliance statements in the rough source have no attached experiment that establishes them.

## Actuarial notes: what can be retired, and what must be corrected

The negative-binomial/Gamma notes are substantively superseded by T §§3–7: exposure-consistent claim frequency, conditional severity, joint expected pure premium, explicit calibration and recursive credibility ledgers. The original notes still contain errors that should not survive through a copied appendix:

- **Residualisation is not tariff neutrality.** Orthogonality does not imply that exponentiated relativities average to one. T §4.2 supplies explicit expected-loss-weighted normalisation.
- **Residualisation is not equalized odds or freedom from proxies.** Zero linear covariance is weaker than independence and much weaker than a legal/fairness conclusion.
- **Recursive means must carry prior accumulated experience.** A no-claim period can lower frequency credibility without resetting earlier claims. It does not necessarily push the multiplier below one. T §7 preserves this distinction.
- **Severity is conditional on claims, with an explicit maturity basis.** A Gamma working distribution is not a universal heavy-tail model. An inverse-Gamma mean requires the appropriate shape condition.
- **Noncentering is a computational choice.** It does not remove all likelihood coupling or guarantee no divergences.
- **Copula likelihoods for binary events need proper event probabilities.** Clipping observed zero/one defaults and evaluating a continuous copula density is not a valid Bernoulli joint likelihood. The archived pure-premium fragment also drifts into credit defaults; keep insurance loss and credit loss targets separate.

The root `Mathematical_Derivations.md` was byte-identical to the companion file under `whitepapers/telematics-relativities/`. The companion contains several of these obsolete claims despite the improved main paper. It receives a supersession notice and remains available as a historical derivation draft. See the active errata register; do not cite it as the corrected mathematical authority.

## Source and bibliography handling

Small search-result thumbnails and pasted links are not a reviewed bibliography. Retain the 109 extracted external links as provenance, then select primary papers relevant to each research question. A referenced publication's abstract or figure does not establish the rough source's sweeping interpretation. Some smaller root notes contain literal truncation markers from an earlier recovery; preserving the files does not reconstruct their missing original content.

The 2026-09-21 audit of *So picking the hierachical bayesian logistic regression with my econometric.docx* is a separate review with its own paragraph numbering. Do not merge its P-identifiers with those used here.
