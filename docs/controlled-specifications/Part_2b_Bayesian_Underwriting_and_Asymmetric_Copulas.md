---
title: "Implementation Documentation: Redundancy-Controlled Hierarchical Bayesian Underwriting and Portfolio Dependence"
author: "Nevil Maloba"
date: "24 August 2026"
---

# Model Purpose, Uses, and Exclusions

This document specifies the Hierarchical Bayesian Logistic Regression, or HLR/HBLR, that converts the Part 2a model-input contract into calibrated real-world default probabilities and uncertainty. It also defines decision analysis, portfolio dependence, stress simulation, explanations, fairness, validation, and governance.

The core underwriting output is \(PD_{\mathbb P}\), a probability under the real-world measure for a defined product and horizon. It is not automatically:

- a risk-neutral probability \(PD_{\mathbb Q}\);
- an IFRS 9 expected-credit-loss result;
- a customer price;
- a policy decision;
- a regulatory capital parameter; or
- a guarantee that an intervention or tranche will perform.

Each downstream use requires its own owner, horizon, validation, and control.

| Use | Primary output | Owner and boundary |
|---|---|---|
| Origination and limit review | Calibrated \(PD_{\mathbb P}\), uncertainty, reason contributions | Licensed lender and approved credit policy |
| Intervention prioritisation | Risk and uncertainty plus treatment eligibility | Product and policy owner; effect must be evaluated |
| IFRS 9 input | Approved real-world PD component | Reporting entity under accounting policy |
| Customer pricing input | Expected-loss and borrower-risk components | Pricing and compliance under CBK framework |
| Portfolio stress | Marginal risk plus dependence, EAD, LGD, and recovery | Portfolio risk and SPV modeller |
| Covenant monitoring | Model-health and portfolio facts | Calculation agent and finance documents |

# Population, Outcome, and Observation Unit

For observation \(i\), define:

- driver, product, contract, platform, geography, and cohort identifiers;
- decision time \(t_i^d\);
- product-specific performance horizon \(H_{p[i]}\);
- binary outcome \(y_i=1\) only under the approved default definition;
- intervention and policy state during the outcome window;
- exposure at default and recovery observation period; and
- data-maturity status.

Training and validation separate drivers and time. A later observation from the same driver cannot cross into an earlier validation fold. Rejected applications, policy changes, interventions, and delayed outcomes are recorded because observed default is affected by who receives credit and assistance.

# Input Contract and Redundancy Controls

Part 2a provides raw neural embeddings \(\mathbf h_i\), Explicit Liquidity Features \(\mathbf z_i\), quality and missingness flags, identifiers, versions, and a point-in-time snapshot manifest.

The engineered variables CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved interactions occur only in the explicit block. They are not duplicated as engineered GRU or Transformer inputs.

## Step 1: Robust Centring and Feature Review

Continuous explicit variables are centred and scaled using development-only robust statistics. Formula-equivalent features, aliases, duplicated horizons, and variables that mechanically contain the target are removed. Diagnostics include:

- semantic lineage comparison;
- pairwise and rank correlation;
- VIF for interpretable main effects;
- singular values, effective rank, and condition indices;
- missingness and source correlation;
- stability across time and platform; and
- univariate and multivariate calibration contribution.

High correlation alone does not require deletion when features have distinct policy meaning, but any retained pair must have documented incremental value and stable attribution.

## Step 2: Spline Basis and Orthonormalisation

Approved nonlinear explicit effects use restricted or natural cubic splines with knots chosen on development data. Let \(\mathbf B_Z\) denote the centred main-effect and spline design. A thin QR decomposition is fitted on the development fold:

$$
\mathbf B_Z=\mathbf Q_Z\mathbf R_Z.
$$

The HLR uses \(\mathbf q_i\), the corresponding row of \(\mathbf Q_Z\), to reduce numerical collinearity among spline columns. Coefficients can be back-transformed through \(\mathbf R_Z^{-1}\) for interpretation on the original basis. Rank-deficient columns are removed under a logged tolerance.

## Step 3: Cross-Fitted Neural Residualisation

Raw wallet timing and other shared source information can allow the neural representation to reproduce explicit liquidity signal even when named engineered features are excluded. To reduce this redundancy without using outcome data, fit a ridge projection of the neural embedding \(\mathbf H\) on the explicit design \(\mathbf B_Z\) within training folds only.

For fold \(k\):

$$
\widehat{\mathbf A}^{(-k)}_{\lambda}
=\left((\mathbf B_Z^{(-k)})^{\top}\mathbf B_Z^{(-k)}
+\lambda\mathbf I\right)^{-1}
(\mathbf B_Z^{(-k)})^{\top}\mathbf H^{(-k)},
$$

$$
\widetilde{\mathbf H}^{(k)}
=\mathbf H^{(k)}-\mathbf B_Z^{(k)}
\widehat{\mathbf A}^{(-k)}_{\lambda}.
$$

The ridge parameter \(\lambda\) is selected within the development data without using the final validation outcome. Production uses \(\widehat{\mathbf A}_{\lambda}\) fitted on the approved development window. Cross-fitting prevents the same observation from determining its own projection.

Residualisation controls linear redundancy. It does not prove independence or remove all nonlinear overlap. The neural training objective may add a bounded cross-covariance penalty:

$$
\mathcal L_{\text{repr}}
=\mathcal L_{\text{task}}
+\lambda_{\text{decorr}}
\left\|\widehat{\operatorname{Cov}}(\mathbf H,\mathbf B_Z)\right\|_F^2,
$$

but only if out-of-time validation shows better stability without material loss of calibration or useful signal. The explicit-only HLR remains the mandatory fallback.

## Step 4: Restricted Interactions and Strong Heredity

Candidate interaction terms are centred and limited to business hypotheses defined before final validation. An interaction can enter only if both parent main effects are retained. This strong-heredity rule prevents an unstable interaction from substituting for a missing main effect.

For centred explicit variables \(z_j\) and \(z_l\):

$$
\psi_{jl,i}=(z_{j,i}-\bar z_j)(z_{l,i}-\bar z_l).
$$

Interactions use group shrinkage and must add stable out-of-time calibration or decision value. Candidate examples include utilisation with prior delinquency, commission change with DLR, late-night driving concentration with arrears, and ZEV-policy proximity with vehicle class.

# Hierarchical Logistic Regression Specification

## Likelihood

The reference model retains the individual Bernoulli likelihood:

$$
y_i\sim\operatorname{Bernoulli}(p_i),
$$

$$
\operatorname{logit}(p_i)=\eta_i.
$$

Binomial aggregation is exact only when grouped observations have the same conditional probability and identical design row. Group averages of heterogeneous features do not produce an exact binomial likelihood. Scaling uses vectorisation, efficient autodiff, approximate inference benchmarked to the individual model, or exact grouping only where design rows are identical.

## Linear Predictor

The redundancy-controlled predictor is:

$$
\boxed{
\eta_i=
\alpha
+a_{g[i]}
+b_{p[i]}
+c_{t[i]}
+\mathbf q_i^{\top}\boldsymbol\beta_z
+\widetilde{\mathbf h}_i^{\top}\boldsymbol\beta_h
+\boldsymbol\psi_i^{\top}\boldsymbol\gamma
+\mathbf m_i^{\top}\boldsymbol\delta
}
$$

where:

- \(\alpha\) is the global intercept;
- \(a_{g[i]}\) is a partially pooled platform, geography, or operational-cluster effect;
- \(b_{p[i]}\) is a product effect;
- \(c_{t[i]}\) is a residual cohort or time effect after observed macro variables;
- \(\mathbf q_i\) is the orthonormal explicit main-effect and spline basis;
- \(\widetilde{\mathbf h}_i\) is the residual neural embedding;
- \(\boldsymbol\psi_i\) is the restricted interaction vector; and
- \(\mathbf m_i\) contains missingness and source-health indicators.

Cluster indicators are not repeated inside \(\mathbf q_i\) or the neural block as explicit one-hot variables. Group and time effects use centred or sum-to-zero identification. The time effect is a residual effect and must not duplicate a comprehensive set of observed macro factors without shrinkage.

## Priors and Partial Pooling

Use a non-centred hierarchical parameterisation:

$$
a_g=\sigma_a a_g^{*},
\qquad a_g^{*}\sim\mathcal N(0,1),
$$

$$
b_p=\sigma_b b_p^{*},
\qquad b_p^{*}\sim\mathcal N(0,1).
$$

Scale priors are weakly informative and calibrated to the standardised log-odds scale. They are not chosen merely because they are conventional.

For a residual time effect:

$$
c_t=\rho c_{t-1}+\epsilon_t,
\qquad
\epsilon_t\sim\mathcal N(0,\sigma_c^2),
\qquad |\rho|<1.
$$

No hard-coded range such as 0.85 to 0.95 is assumed. The model compares AR(1), random-walk, fixed cohort, and no residual-time alternatives. If observed macro features explain the variation, shrinkage should reduce \(c_t\).

The explicit, neural, and interaction coefficient blocks use separate grouped regularised-horseshoe or comparable shrinkage priors. Conceptually:

$$
\beta_{r,j}\sim\mathcal N(0,\tau_r^2\widetilde\lambda_{r,j}^2),
\qquad r\in\{z,h,\psi,m\},
$$

with finite slab scale so weak data cannot create arbitrarily large coefficients. Separate global scales allow the model to shrink an entire redundant block. Interactions receive the strongest prior shrinkage.

# Calibration Layer

Shrinkage and partial pooling improve estimation but do not ensure calibrated probabilities. After the development model is frozen, fit a calibration model on a strictly later validation period:

$$
\operatorname{logit}(PD^{\text{cal}}_i)
=\kappa_{p[i]}+s\eta_i,
$$

$$
\kappa_p\sim\mathcal N(\kappa_0,\sigma_{\kappa}^2),
\qquad s>0.
$$

The partially pooled product intercepts correct level differences while the common positive slope corrects over- or under-dispersion. Product-specific slopes are allowed only with sufficient validation data and pre-specified regularisation. If a simple intercept and slope do not calibrate adequately, compare beta calibration or monotone methods without using the test period.

The final test period remains untouched until all modelling, residualisation, shrinkage, and calibration choices are fixed.

# Multicollinearity and Redundancy Acceptance Tests

The model is approved only if the combined representation passes all relevant tests:

1. **Feature-manifest test:** No named Explicit Liquidity Feature or alias appears in the neural input contract.
2. **Rank test:** The explicit design retains adequate numerical rank after spline construction.
3. **Condition test:** Condition indices and singular values are stable across development folds.
4. **Posterior-correlation test:** Large coefficient correlations are explained, reduced, or covered by group shrinkage and combined effect reporting.
5. **Coefficient-stability test:** Signs, shapes, and material effects remain stable across time and platform folds.
6. **Ablation test:** Explicit-only, neural-only, raw concatenation, residualised combination, and interaction variants are compared.
7. **Incremental-value test:** The neural residual adds pre-specified out-of-time calibration or decision utility.
8. **Explanation-stability test:** Small perturbations do not cause arbitrary switching among redundant reasons.
9. **Calibration test:** Intercept, slope, Brier score, log score, and curves pass overall and material segments.
10. **Complexity fallback:** If the combined model fails, deploy the simpler approved model.

VIF is interpreted carefully because spline columns and hierarchical effects are structured. It is used as a diagnostic, not a mechanical deletion rule. Posterior regularisation does not make redundancy harmless; the manifest, residualisation, orthogonalisation, ablation, and explanation tests remain necessary.

# Inference and Production Scoring

## Offline Reference Inference

NUTS or HMC is used offline for the reference posterior. The development report records chains, warm-up, draws, seeds, adaptation, target acceptance, divergences, tree depth, rank-normalised \(\widehat R\), bulk and tail ESS, energy diagnostics, and posterior predictive checks.

Computational convergence does not prove business validity. Poor geometry can signal redundant parameters, weak identification, or scale problems and should trigger simplification.

## Scalable Approximation

If reference inference is too costly, candidates include Laplace approximation, variational inference, or structured subsampling. Each approximation is benchmarked against the individual-level reference on representative datasets for:

- posterior means and intervals;
- calibration and discrimination;
- tail predictions;
- subgroup outcomes;
- coefficient and shape stability; and
- actual policy decisions.

Approximation is accepted only within documented tolerances.

## Online Service

Production does not launch NUTS for each request. It loads a signed posterior artifact, projection parameters, calibration layer, feature schema, and approved representative posterior draws or analytic approximation. The service returns:

- calibrated posterior mean or median \(PD_{\mathbb P}\);
- uncertainty interval;
- probability that PD exceeds an approved action threshold;
- product and horizon;
- explicit and grouped neural contribution summaries;
- model, feature, projection, and calibration versions; and
- source-health status.

Latency, throughput, numerical tolerance, stale-artifact handling, service fallback, rollback, and reproduction are tested before activation.

# Validation Framework

## Data and Split Design

Validation uses driver-separated and time-forward splits, plus platform- and geography-held-out tests where material. Labels must be mature. Point-in-time reconstruction and intervention flags are independently checked.

## Predictive and Probabilistic Performance

Report:

- calibration intercept and slope;
- calibration curve and expected calibration error;
- Brier score and log score;
- AUC or Gini with confidence intervals;
- precision, recall, and decision utility at approved thresholds;
- credible-interval coverage;
- performance by product, platform, geography, data history, and material customer group; and
- stability across time and shock periods.

## Posterior Predictive Checks

Posterior predictive checks compare total defaults, cluster and product default rates, temporal patterns, calibration bins, joint defaults, and extreme loss. A failed tail check does not automatically increase a copula parameter; marginal model, dependence family, data, recovery, exposure, and regime specification must all be investigated.

## Policy and Intervention Feedback

The observed outcome depends on previous approval, limit, price, and intervention. Validation records treatment and policy version. Where feasible, use randomised or quasi-experimental designs for interventions and sensitivity analysis for rejection and treatment selection. The underwriting model cannot claim that an intervention caused lower default from treated outcomes alone.

# Bayesian Decision Analysis and Policy Interface

For action \(a\) and uncertain outcome \(\omega\), decision analysis can minimise posterior expected loss:

$$
a_i^*=\arg\min_a
\mathbb E_{\omega\mid\mathcal D}
[\mathcal L(a,\omega)],
$$

where \(\mathcal L\) may include expected credit loss, customer cash effect, operating cost, intervention cost, uncertainty, and portfolio constraints. The loss function is documented and approved; it cannot silently substitute a commercial objective for a legal or policy rule.

The Credit Policy and Compliance Gate applies hard requirements after the model. It returns approve, decline, reduce limit, freeze draw, restructure, intervene, suspend purchases, trigger early amortisation, or block distributions according to authority and contract. Policy version and actual rule hits are stored separately from model explanations.

# Customer Pricing and the P-to-Q Boundary

Under the applicable CBK risk-based framework:

```text
Total lending rate = KESONIA + K_RBCP
Total cost of credit = KESONIA + K_RBCP + fees and charges
```

`K_RBCP` includes lending-related cost, shareholder return, and borrower risk. The internal decomposition may use posterior expected loss:

$$
EL_i=\mathbb E[PD_{\mathbb P,i}\times LGD_i\times EAD_i],
$$

plus controlled funding, operating, capital or shareholder-return, liquidity, uncertainty, and borrower-risk components. The decomposition must prevent double counting and remain subject to contract and approval.

A real-world posterior is not risk neutral. An optional \(PD_{\mathbb Q}\) or market-consistent valuation overlay requires observable transaction or market spreads, recovery conventions, discounting, and separation of liquidity and structural enhancement. Where a liquid Kenyan gig-receivables market does not exist, the uncertainty must be explicit. Short tenor does not eliminate P-to-Q divergence.

# Portfolio Dependence and Copula Modelling

## Marginals and Orientation

The HLR supplies calibrated marginal default probabilities. Dependence is estimated from joint product outcomes at driver and cohort level. Variable orientation must be explicit because Clayton lower-tail dependence applies to the selected uniform representation, while default events may correspond to lower or upper tails depending on transformation.

## Candidate Families

Compare:

- Gaussian for symmetric dependence without tail dependence;
- Student-t for symmetric tail dependence;
- Clayton and rotated Clayton for directional tail dependence;
- Gumbel for the opposite directional tail;
- Frank for symmetric dependence without tail emphasis; and
- vines for heterogeneous pair structures.

Select using likelihood or information criteria, probability scores, joint-tail counts, out-of-sample performance, stability, and interpretability. Sparse data justify conservative stress overlays and wide parameter uncertainty, not an assertion of exact dependence.

For the \(d\)-dimensional Clayton copula with \(\theta>0\):

$$
C_{\theta}(u_1,\ldots,u_d)
=\left(\sum_{j=1}^d u_j^{-\theta}-d+1\right)^{-1/\theta}.
$$

The lower-tail coefficient is:

$$
\lambda_L=2^{-1/\theta}
$$

for the bivariate case. Stress can vary \(\theta\), but the mapping from macro shock to parameter requires evidence or an explicit management scenario.

## Correct Default Simulation

For simulation \(s\):

1. Draw model and calibration parameters from the approved posterior or approximation.
2. Calculate each marginal \(PD^{(s)}_{i,p}\).
3. Draw dependent uniforms \(\mathbf U_i^{(s)}\) from the selected copula.
4. Set \(D_{i,p}^{(s)}=\mathbf 1\{U_{i,p}^{(s)}\le PD_{i,p}^{(s)}\}\).
5. Apply EAD, stochastic or scenario LGD, and recovery timing.
6. Aggregate monthly portfolio cash and run the exact SPV waterfall.

Process loss, parameter uncertainty, model uncertainty, and management scenario are reported separately. Portfolio VaR and expected shortfall are not called Bayesian credible intervals.

# Economic Capital, SPV Protection, and Regulatory Capital

Internal economic capital may be defined as loss VaR or expected shortfall net of expected loss for a stated horizon and confidence. The definition must include currency, exposure, recovery, and diversification assumptions.

SPV protection is measured through Class C, Class B subordination, OC, reserve, excess spread, controlled accounts, servicing, and the waterfall. Regulatory capital is calculated by the regulated lender under applicable CBK and Basel implementation. Internal copula parameters do not replace prescribed asset correlations, floors, maturity adjustments, or supervisory approval.

# Explainability

Explicit effects should be presented as posterior spline and interaction contributions on the original feature scale. Neural explanations can use grouped, stability-tested attribution. SHAP and LIME are diagnostic tools, not causal proof or legal compliance. Correlated features can divide attribution arbitrarily, which is why feature ownership, residualisation, grouping, and explanation-stability tests matter.

Customer-facing reasons map to stable business concepts and the actual policy rule. The record contains the decision, model version, calibrated risk, uncertainty, material contributions, policy-rule hits, override, and communication.

# Fairness and Customer Protection

The programme should measure approval, price, limit, calibration, false positive and false negative rates, intervention, insurance continuity, complaints, appeals, and downstream outcomes across legally reviewed groups. Results include confidence intervals, sample thresholds, intersectional review where appropriate, and time stability.

Feature blindness does not remove proxies. MMD or decorrelation does not guarantee equalized odds. Equalized odds may conflict with calibration where base rates differ. The programme therefore compares mitigation alternatives, business utility, customer harm, and less-discriminatory options under Kenyan legal and privacy review.

# Model Risk Governance

The model inventory records owner, intended use, prohibited use, risk tier, data, code, feature set, projection, priors, inference, calibration, limitations, validation, approval, deployment, monitoring, incident, change, fallback, rollback, and retirement.

SR 11-7 can be used as comparative model-risk practice. It is not described as direct Kenyan law. PSI thresholds are internal or contractual conventions. Monitoring combines data quality, freshness, missingness, calibration, discrimination, uncertainty coverage, coefficient and shape stability, posterior correlation, fairness, outcomes, overrides, complaints, and financial impact.

Every production release retains:

- source-code commit;
- data and feature manifests;
- environment and container digest;
- random seeds;
- posterior and calibration artifacts;
- projection parameters;
- model signature;
- validation and fairness reports;
- policy-rule version;
- approvals; and
- rollback package.

# Approval and Fallback

The combined HLR is approved only if it delivers stable incremental out-of-time value over the explicit-only model and passes multicollinearity, calibration, explanation, fairness, latency, and resilience tests. If not, deployment falls back in this order:

1. explicit-only hierarchical logistic model;
2. simpler calibrated logistic model under approved policy; or
3. manual or restricted-product decisioning during a material data or model incident.

This fallback is a design strength. The objective is reliable and governable decision quality, not maximum architectural complexity.

# References

1. A. Gelman *et al.*, *Bayesian Data Analysis*, 3rd ed., CRC Press, 2013.
2. P. Bürkner, “Advanced Bayesian Multilevel Modeling with the R Package brms,” *The R Journal*, 2018.
3. J. Piironen and A. Vehtari, “Sparsity information and regularization in the horseshoe and other shrinkage priors,” *Electronic Journal of Statistics*, 2017.
4. W. Heynderickx, J. Cariboni, W. Schoutens, and B. Smits, “The relationship between actual and risk-neutral default probabilities,” *Applied Economics*, 2016, doi: 10.1080/00036846.2016.1150953.
5. Central Bank of Kenya, “Revised Risk-Based Credit Pricing Model,” Aug. 2025. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf
6. Basel Committee on Banking Supervision, “Calculation of RWA for credit risk: IRB approach.” Available: https://www.bis.org/basel_framework/chapter/CRE/31.htm
7. Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency, “Guidance on Model Risk Management,” SR 11-7, Apr. 2011. Available: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
8. IFRS Foundation, “IFRS 9 Financial Instruments.” Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
