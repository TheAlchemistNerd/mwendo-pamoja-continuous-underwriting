# D06 Inconsistency Report: Bayesian Underwriting and Asymmetric Copulas

## Document role and semantic synopsis

D06 is the mathematical core of the corpus. It proposes hierarchical Bayesian logistic regression over neural and explicit features, spline effects, time-varying priors, MCMC, decision rules, a friction-adjusted pricing layer, copula dependence, explainability, model-risk governance, and fairness. An appendix argues that stochastic calculus and the equivalent martingale measure are redundant for short-horizon gig credit.

The paper contains valuable instincts: partial pooling can stabilise sparse clusters; posterior uncertainty can improve decisions; calibration matters; nonlinear liquidity effects should not be coarsely binned; and linear correlation does not capture tail dependence. The difficulties are in method selection and claims of sufficiency. Aggregation, online MCMC, risk-neutral pricing, copula simulation, regulatory capital, and fairness are treated more definitively than the mathematics or evidence permits.

## Executive inconsistency summary

The model should be reframed as a real-world credit-risk and decision system. It does not become risk neutral merely by adding a friction term. A market-consistent P-to-Q transformation requires market calibration and separation of liquidity and structural enhancement [20]. Grouping Bernoulli outcomes into a binomial likelihood is exact only when individuals share the same probability, not when group averages conceal heterogeneous features. Daily warm-started NUTS is not a credible low-latency scoring architecture. The copula simulation description does not correctly construct joint default events, and a Clayton parameter cannot lower prescribed Basel correlation. The appendix's claim that P-Q divergence is negligible for 7 to 30 days is unsupported.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D06-I01 | Critical | High | HBLR specification and explicit inputs | Feature interface and notation are not fully stable |
| D06-I02 | Critical | High | Bernoulli-to-Binomial aggregation | Likelihood is not exact under heterogeneous covariates |
| D06-I03 | High | High | Production inference | HMC and NUTS are unsuitable for online scoring as described |
| D06-I04 | Critical | High | Risk-neutral pricing and Appendix A | Real-world PD is incorrectly relabelled risk neutral |
| D06-I05 | Critical | High | Copula simulation | Joint-default algorithm is technically incomplete or wrong |
| D06-I06 | High | High | Copula family selection | Clayton is asserted rather than selected empirically |
| D06-I07 | Critical | High | Regulatory capital linkage | Internal dependence cannot override Basel prescriptions |
| D06-I08 | High | High | Decision loss and ECL | Underwriting, pricing, IFRS 9, and policy loss functions drift |
| D06-I09 | High | High | Calibration and diagnostics | Validation omits temporal, intervention, and decision feedback |
| D06-I10 | High | High | XAI section | SHAP and LIME explanations do not establish causal or legal reasons |
| D06-I11 | High | High | MRM and PSI | Foreign guidance and heuristic thresholds are overstated |
| D06-I12 | High | High | Fairness section | Blindness and DIR are insufficient governance |
| D06-I13 | Medium | High | Equations throughout | Punctuation corruption makes formulas unreliable |

## Detailed findings

### D06-I01: Model interface still depends on unresolved feature ownership

**Anchor:** “Full Mathematical Model Specification,” “Nonlinear Functional Forms,” and D05's feature sections. The HBLR specification accepts neural representation and explicit variables, but the corpus does not consistently prevent CFA or Earnings Velocity from also appearing inside the neural encoder.

**Impact:** Duplicate engineered information makes coefficients and attributions unstable. It also undermines the claimed interpretable bypass and can create hidden leakage when one branch uses a differently timestamped calculation.

**Canonical resolution:** Define `Phi_neural` and `Z_liquidity` as versioned interfaces. CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved interactions occur only in `Z_liquidity`. Record feature lineage and decision cut-off. Use spline priors and shrinkage sufficient to control interaction complexity. The policy gate stays downstream.

### D06-I02: Binomial aggregation loses individual information

**Anchor:** “The Bernoulli-to-Binomial Aggregation for Computational Scaling.” The paper treats grouped successes and failures as an exact computational substitute while using averaged or shared features.

**Impact:** A binomial likelihood is exact when trials have the same conditional probability. If drivers within a group have different neural embeddings, liquidity features, exposures, or times, the count distribution is Poisson-binomial and a group-average logit does not recover the individual likelihood. Coefficients, uncertainty, and calibration can be biased.

**Canonical resolution:** Retain individual Bernoulli likelihood for model development or group only observations with identical design rows after deterministic discretisation. Consider mini-batch variational inference, Laplace approximation, expectation propagation, case-control sampling with weights, or sufficient-statistic aggregation only for genuinely shared predictors. Quantify approximation error against an individual benchmark.

### D06-I03: Online NUTS is operationally implausible

**Anchor:** “Production Inference: BlackJAX on GPU/TPU” and MCMC architecture. The paper suggests frequent warm-started MCMC or HMC for production decisions.

**Impact:** NUTS is valuable for offline posterior inference but has unpredictable trajectory length, warm-up cost, convergence requirements, and hardware dependence. Warm starts can preserve bias after drift. Low-latency credit decisions need deterministic and highly available scoring.

**Canonical resolution:** Use offline or scheduled posterior estimation with robust diagnostics. Publish an approved posterior artifact or approximate posterior to an online scoring service. Online scoring should compute posterior predictive summaries through fixed draws, analytic approximation, or distilled uncertainty model. Define refresh cadence, emergency fallback, maximum latency, numerical tolerance, and rollback. Use HMC as a validation benchmark, not an API dependency.

### D06-I04: The P-to-Q transition is not established

**Anchor:** “Friction-Adjusted Risk-Neutral Pricing,” “The Transition from Deterministic Spread,” and Appendix A. The paper calls the HBLR output risk neutral after adding friction and argues that short tenor makes P-Q divergence negligible.

**Impact:** Real-world `PD_P` estimates expected frequency. `PD_Q` reflects market pricing of risk and is inferred from tradable prices under assumptions. Short maturity does not make the measures identical, especially in illiquid, correlated, and non-traded credit. Mislabeling affects pricing, valuation, accounting, and investor disclosure.

**Canonical resolution:** Call HBLR output `PD_P`. Price customer assets using KESONIA plus `K_RBCP`, where components include expected loss, operating and funding cost, capital or shareholder return, liquidity, uncertainty, and borrower risk within the CBK framework [1], [2]. Add an optional market-consistent valuation overlay only after calibration to relevant ABS, loan-sale, guarantee, or comparable spread data, stripping liquidity and structural enhancement [20], [35], [36]. Do not claim uniqueness.

### D06-I05: Copula simulation does not correctly generate portfolio defaults

**Anchor:** “Sklar's Theorem and the Clayton Copula” and “Unexpected Loss Quantification.” The narrative appears to transform marginal PDs by probability-integral transforms, apply a copula inverse, and equate simulated quantiles with Bayesian credible intervals.

**Impact:** A copula joins random marginal variables. To simulate correlated Bernoulli defaults, one draws dependent uniforms from the copula and compares each uniform with the relevant conditional default probability. Static PDs are thresholds, not observations to PIT. Portfolio VaR is a loss-distribution quantile; a Bayesian credible interval describes parameter or predictive uncertainty. They are not interchangeable.

**Canonical resolution:** Specify marginals, dependence data, orientation, parameter estimation, conditional simulation, exposure, LGD, recovery timing, and aggregation. Propagate parameter uncertainty separately from process loss. Validate with probability scores, tail counts, likelihood or information criteria, out-of-sample stress performance, and sensitivity to family choice.

### D06-I06: Clayton is treated as universally superior

**Anchor:** “The Failure of Linear Correlation and Gaussian Copulas” and “The Clayton Copula.” Lower-tail dependence may be relevant when low income and repayment outcomes co-occur, but product default events and loss orientation need explicit mapping.

**Impact:** Clayton has asymmetric dependence and may miss upper-tail, symmetric, or mixed structures. Product pairs can differ and dependence can vary by platform, geography, and regime.

**Canonical resolution:** Treat Clayton as a candidate. Compare Gaussian, Student-t, Clayton, Gumbel, Frank, rotations, and vines using consistent marginals. Estimate uncertainty and stability by cohort. Use stress overlays where data are sparse. Explain how the chosen tail corresponds to default after variable orientation.

### D06-I07: Copula parameters cannot directly reduce Basel capital

**Anchor:** “Unexpected Loss Quantification and Regulatory Capital Linkage.” The paper suggests the empirically lower portfolio dependence can replace or reduce prescribed regulatory asset correlation and deliver capital relief.

**Impact:** Basel IRB formulas and local implementation specify correlations, parameters, floors, and supervisory approval. An internal model can inform economic capital and risk management but does not modify the formula by assertion [8], [19].

**Canonical resolution:** Separate economic-capital simulation, lender regulatory capital, SPV credit enhancement, and investor stress. State that any regulatory treatment is determined by the regulated lender and CBK. Use the copula to size internal buffers and scenario losses, not to promise IRB benefit.

### D06-I08: Four decision purposes share one ambiguous loss function

**Anchor:** “Real-Time Bayesian Decision Boundaries,” “Expected Value Maximization,” “Risk-Neutral Pricing,” and D07 IFRS sections. The text moves among approval, intervention, pricing, and ECL as if the same PD and cost matrix control all.

**Impact:** Underwriting optimises expected customer and portfolio outcomes under policy. Pricing follows CBK and contract constraints. IFRS 9 estimates unbiased ECL. Portfolio covenants protect noteholders. Different horizons, costs, and decision rights apply.

**Canonical resolution:** Define separate use cases with model owner, horizon, target, loss measure, input vintage, output, threshold owner, and override. Reuse validated components only with documented fitness. Keep hard caps in the Credit Policy and Compliance Gate.

### D06-I09: Validation ignores intervention feedback and temporal dependence

**Anchor:** “MCMC Convergence Diagnostics,” “Posterior Predictive Checks,” and “Discrimination, Calibration, and Stability.” R-hat and ESS assess sampler behaviour, not business validity. Random holdouts can leak driver and time information, and interventions alter observed labels.

**Impact:** A model trained on treated outcomes may learn that risky drivers are safe because interventions prevented default. Cluster leakage inflates performance. Calibration may fail after platform or pricing changes.

**Canonical resolution:** Add time-based and platform-held-out validation, driver-level separation, nested calibration, policy-off or causal treatment analysis, rejection inference, delayed-outcome controls, subgroup uncertainty, stress backtesting, and decision-curve analysis. Maintain challenger and champion versions. Report confidence intervals rather than point metrics.

### D06-I10: XAI outputs are not explanations of cause or compliance

**Anchor:** SHAP and LIME sections. The paper treats local attributions as authoritative reasons and regulatory evidence.

**Impact:** SHAP values depend on background distribution and feature dependence. Correlated raw and engineered features can split attribution arbitrarily. LIME can be unstable. Neither proves causality, legality, fairness, or policy consistency.

**Canonical resolution:** Use model-specific posterior contributions where possible, grouped features, sensitivity tests, stability checks, and reason-code mapping approved by compliance. Distinguish predictive contribution from causal explanation. The policy gate should store the actual rule and data that determined the action.

### D06-I11: Model-risk guidance and PSI thresholds are overstated

**Anchor:** “Model Risk Management” and “Continuous Monitoring.” SR 11-7 is cited as if direct compliance applies, and PSI 0.25 is linked to automatic regulatory outcomes.

**Impact:** Foreign guidance can be a benchmark but not a Kenyan legal requirement. PSI is sensitive to binning and sample size and does not diagnose calibration, label shift, or causal harm.

**Canonical resolution:** Adopt SR 11-7 as comparative good practice [9]. Label PSI thresholds as approved internal or contractual conventions. Combine PSI with missingness, calibration, discrimination, uncertainty, outcomes, fairness, and data-quality monitoring. Define escalation and authority without inventing regulatory notification.

### D06-I12: Fairness controls are incomplete

**Anchor:** “Algorithmic Fairness and Bias Mitigation.” Feature blindness, orthogonalization, and disparate-impact ratio are treated as sufficient.

**Impact:** Proxies remain, labels may encode structural inequity, and selection occurs before outcomes are observed. Equalized odds can conflict with calibration, while DIR alone ignores error costs and uncertainty.

**Canonical resolution:** Define legal scope with Kenyan counsel; measure selection, error rates, calibration, pricing, limits, interventions, complaints, and adverse outcomes. Use confidence intervals and minimum samples. Establish review, appeal, override, and less-discriminatory-alternative testing. Conduct the DPIA described in [10], [11].

### D06-I13: Equation corruption prevents faithful implementation

**Anchor:** spline recursion, AR priors, copula formulas, Basel formulas, and Appendix A. Minus signs and inequalities have been replaced or mangled in several expressions.

**Impact:** A visually plausible formula may be mathematically different. This is especially dangerous for `1 - theta`, B-spline recursion, inverse transforms, and capital functions.

**Canonical resolution:** Re-key from primary sources, add symbol and dimension tables, create executable unit tests with known values, and render every equation. Do not treat old code snippets as authoritative where they contain corrupted punctuation.

## Dependencies, evidence gaps, and remediation sequence

D06 depends on D04 labels, D05 point-in-time features, D07 policy and regulatory boundaries, D09 pricing components, and D03 waterfall outputs. Evidence needed includes individual-level development data, intervention flags, rejection data, market-spread comparables, copula calibration data, validation reports, latency benchmarks, fairness legal advice, and approved model governance.

Remediation order is: freeze model use cases and interfaces; repair equations; retain individual likelihood or prove aggregation error is immaterial; separate offline inference from online scoring; replace risk-neutral claims; rebuild dependence simulation; separate economic from regulatory capital; then expand validation, XAI, fairness, and monitoring. The model is ready only when every output has one decision use, one measure, one time basis, and one accountable owner.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D06-I01 | D06-P02, D06-P03 |
| D06-I02 | D06-P04 |
| D06-I03 | D06-P05 |
| D06-I04 | D06-P07, D06-P12 |
| D06-I05 | D06-P08 |
| D06-I06 | D06-P08 |
| D06-I07 | D06-P09 |
| D06-I08 | D06-P02, D06-P06, D06-P07 |
| D06-I09 | D06-P06, D06-P10 |
| D06-I10 | D06-P10 |
| D06-I11 | D06-P10 |
| D06-I12 | D06-P11 |
| D06-I13 | D06-P01, D06-P13 |
