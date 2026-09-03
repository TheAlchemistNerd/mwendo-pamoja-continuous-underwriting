---
title: "Controlled Specification: Credit-Risk Model, Timing, Loss, and Production Architecture"
author: "Nevil Maloba"
date: "30 August 2026"
status: "Implementation control specification"
---

# 1. Purpose and Authority

This specification is the common technical contract for the credit-risk enhancements described across Mwendo Pamoja Parts 1 through 6. It advances the existing redundancy-controlled Hierarchical Bayesian Logistic Regression, or HLR, without replacing its economic meaning. The champion estimates calibrated real-world default probability for a product and horizon. A timing model, EAD model, cure and recovery models, dependence model, accounting process, policy gate, and SPV waterfall remain separate governed components.

The matching Part 1 through Part 6 controlled specifications define product, data, regulatory, enterprise, financial, and programme controls. Where a duplicated technical definition differs, this document controls the model and loss interface. Executed contracts, applicable law, approved accounting policy, and formal model approval prevail for their own domains.

# 2. Canonical Observation and Clock Contract

The atomic model record is a driver-product-risk episode at decision time:

$$
o=(i,p,e,t_d,H_p),
$$

where \(i\) identifies the driver, \(p\) the product, \(e\) the risk episode or contract state, \(t_d\) the decision time, and \(H_p\) the approved performance horizon. The record also carries facility, contract, vehicle, policy, platform, geography, cohort, currency, decision purpose, and intervention history.

Every source and derived object preserves:

1. event time, when the economic or operational fact occurred;
2. availability time, when it became lawfully and technically usable;
3. decision time, when the score or action was produced;
4. label-maturity time, when the full outcome horizon became observable;
5. accounting-effective time; and
6. cash-realisation time for collections, refunds, costs, and recoveries.

A feature may be joined only when availability time is no later than decision time. A fully matured binary label may enter a training cutoff only when its label-maturity time is no later than that cutoff. Open episodes are right censored for timing analysis and are not automatically treated as non-defaults.

Five connected ledgers are mandatory:

- identity and exposure ledger;
- obligation and contractual-state ledger;
- decision, policy, action, and intervention ledger;
- outcome, censoring, and label-maturity ledger; and
- collection, refund, recovery, cost, and cash-flow ledger.

The same ledgers generate HLR labels, survival risk sets, ECL inputs, and SPV cohort cash flows.

# 3. Primary Fixed-Horizon HLR

For a matured product outcome,

$$
Y_i^{(p,H_p)}\sim\operatorname{Bernoulli}(p_i),
\qquad
\operatorname{logit}(p_i)=\eta_i.
$$

The primary predictor is

$$
\eta_i=
\alpha
+a_{g[i]}
+b_{p[i]}
+c_{t[i]}
+\mathbf q_i^{\mathsf T}\boldsymbol\beta_z
+\widetilde{\mathbf h}_i^{\mathsf T}\boldsymbol\beta_h
+\boldsymbol\psi_i^{\mathsf T}\boldsymbol\gamma
+\mathbf m_i^{\mathsf T}\boldsymbol\delta.
$$

Here \(a\), \(b\), and \(c\) are identified, partially pooled geography or platform, product, and cohort-time effects. \(\mathbf q_i\) is the governed P-spline design for Explicit Liquidity Features. \(\widetilde{\mathbf h}_i\) is the cross-fitted residual neural bottleneck. \(\boldsymbol\psi_i\) contains a small strong-heredity interaction set. \(\mathbf m_i\) contains approved contract, missingness, and source-health terms.

The hierarchy is retained under every approved inference method. Driver random effects are optional and require repeated matured episodes, identification, stability, and an incremental validation result. They are not the reason for adopting Pólya-Gamma augmentation.

# 4. Governed P-Splines and Preserved Alternatives

For an explicit feature \(x\), the champion uses

$$
f(x)=\sum_{k=1}^{K}B_{k,d}(x)\zeta_k,
$$

with a first- or second-order difference penalty chosen during development. The default research candidate is

$$
\Delta^2\boldsymbol\zeta\sim
\mathcal N(\mathbf 0,\tau_f^2\mathbf I).
$$

The basis degree, boundary and interior knots, penalty order, penalty matrix, smoothing-scale prior, centring transform, numerical reparameterisation, validated support, clipping or extrapolation rule, missingness rule, and back-transformation are artifact metadata. A QR or eigen transform must preserve the penalty null space. The reported curve is expressed on the original feature scale.

A shared shape plus a partially pooled product deviation is permitted when identified:

$$
f_p(x)=f_0(x)+g_p(x).
$$

The B-spline RW1 and B-spline AR1 priors remain challenger specifications. Time-varying macro or cohort effects are separately named time processes so an AR1 smoothing alternative cannot be confused with an AR1 calendar effect.

# 5. Neural Residualisation and Shrinkage

The named CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved financial interactions belong to the Explicit Liquidity Feature Path. The neural branch may observe governed raw sequences but does not receive those engineered metrics or deterministic aliases.

Within development fold \(k\), fit a ridge projection of neural bottleneck \(\mathbf H\) on the explicit and approved metadata design \(\mathbf B\):

$$
\widehat{\mathbf A}^{(-k)}_\lambda
=
\left[(\mathbf B^{(-k)})^{\mathsf T}\mathbf B^{(-k)}+\lambda\mathbf I\right]^{-1}
(\mathbf B^{(-k)})^{\mathsf T}\mathbf H^{(-k)},
$$

$$
\widetilde{\mathbf H}^{(k)}
=
\mathbf H^{(k)}-\mathbf B^{(k)}\widehat{\mathbf A}^{(-k)}_\lambda.
$$

Whitening is optional after residualisation and is fitted inside the training fold. A regularised-horseshoe or comparable finite-slab block prior controls the residual neural coefficients. Residualisation reduces linear duplication; it does not claim statistical independence. The combined model must beat the explicit-only hierarchy on pre-specified time-forward calibration, utility, stability, fairness, and operational-cost criteria.

# 6. Offline Pólya-Gamma Inference

Pólya-Gamma augmentation is a candidate inference method for the complete HLR. Let \(\eta_i=\mathbf x_i^{\mathsf T}\boldsymbol\vartheta\) and introduce

$$
\omega_i\mid\eta_i\sim\operatorname{PG}(1,\eta_i).
$$

Conditional on \(\boldsymbol\omega\), Gaussian coefficient and hierarchy blocks have Gaussian full conditionals. The P-spline precision remains sparse. Product, platform, geography, cohort, selected time, and any approved driver effects retain partial pooling.

The model is conditionally conjugate rather than fully closed form. Separate updates remain necessary for Pólya-Gamma variables, hierarchy variance and correlation, smoothing scales, regularised-horseshoe scales, time persistence, and calibration parameters. A candidate blocked cycle updates latent variables, Gaussian blocks, variance and covariance blocks, horseshoe scales, then predictions and diagnostics.

NUTS or HMC remains the reference fit unless model governance approves another benchmark. Pólya-Gamma inference is accepted only after posterior, tail, shrinkage, calibration, effective-sample-size, and decision agreement tests on representative portfolios. All posterior estimation is offline.

# 7. Timing Challenger and Censoring

The timing challenger is a hierarchical piecewise-exponential proportional-hazards model. Split episode \(i\) into intervals \(j\) with at-risk duration \(E_{ij}\), event count \(d_{ij}\), and time-valid design \(\mathbf x_{ij}\):

$$
d_{ij}\sim\operatorname{Poisson}(E_{ij}\lambda_{ij}),
$$

$$
\log\lambda_{ij}
=
\alpha_j+\mathbf x_{ij}^{\mathsf T}\boldsymbol\beta
+u_{g[i]}+v_{p[i]}.
$$

The risk-set builder records delayed entry where relevant, event, right censoring, product closure, prepayment, intervention, modification, competing operational exit, and covariates available at each interval boundary. Product-specific baseline hazards may be pooled where evidence supports it.

For cumulative hazard \(\Lambda_i(t)\),

$$
S_i(t)=\exp[-\Lambda_i(t)],
\qquad
PD_i(0,t)=1-S_i(t).
$$

The marginal default probability for interval \(m\) is

$$
q_{i,m}=S_i(t_{m-1})-S_i(t_m).
$$

At every shared horizon, the survival-derived cumulative PD is reconciled with the calibrated HLR output. The models may serve different decisions, but their definitions and overlapping forecasts cannot diverge without diagnosis and approval.

A Gamma-frailty extension is a survival challenger. A joint longitudinal-survival extension is considered only for a repeatedly measured latent trajectory with material measurement error or endogenous observation. Neither extension may recreate named explicit liquidity metrics as latent duplicates.

# 8. PD, EAD, Cure, LGD, Refund, and Recovery

The loss architecture separates:

- default event and timing;
- scheduled and stressed EAD, including revolving conversion;
- cure, modification, prepayment, and closure;
- gross recovery, cost, and delay;
- eligible IPF cancellation refund, deductions, set-off, and delay; and
- ordinary collection and servicing cash flow.

For draw \(s\),

$$
\mathcal L_{i,p}^{(s)}
=D_{i,p}^{(s)}EAD_{i,p}^{(s)}
-R_{i,p}^{(s)}-U_{i,p}^{(s)}+C_{i,p}^{(s)}.
$$

Each submodel has a separate target, horizon, feature manifest, validation, owner, and fallback. Cure collections cannot also be credited as ordinary recovery. An IPF refund cannot also be embedded in LGD without reconciliation. Common scenario factors are mapped once across components to prevent double counting.

# 9. Calibration and Dependence Order

Product calibration is estimated on a later validation period:

$$
\operatorname{logit}(PD_i^{\mathrm{cal}})
=\kappa_{p[i]}+s\eta_i,
\qquad s>0.
$$

Residualisation, probability calibration, financial calibration, and market-consistent valuation are distinct transformations.

Dependence is represented in order:

1. observed systematic and scenario factors;
2. partially pooled platform, geography, product, cohort, and time effects;
3. explicit within-driver multi-product linkage;
4. residual copula or alternative dependence challenger; and
5. separate model-form stress.

Copula selection uses held-out joint outcomes, probability-integral-transform diagnostics, tail counts, parameter stability, and portfolio cash-flow impact. A copula parameter never substitutes for omitted hierarchy or a transmission path already represented in product states.

# 10. Production Artifact and Online Scoring

The online service loads a signed artifact containing:

- model and feature schemas;
- posterior draws or approved analytic approximation;
- P-spline basis, penalty, support, and back-transform;
- residualisation and optional whitening transforms;
- hierarchy mappings and new-group integration rules;
- calibration parameters;
- default horizons and survival reconciliation version;
- reason concepts and explanation grouping;
- numerical precision and parity tolerances;
- code, data, environment, and approval digests; and
- fallback and rollback instructions.

It returns calibrated real-world PD, horizon, uncertainty interval, exceedance probabilities, contribution groups, quality and support flags, and all version identifiers. It performs no posterior sampling during the underwriting request.

# 11. Accounting and SPV Interfaces

IFRS 9 ECL uses the approved reporting entity's probability-weighted discounted cash-shortfall method. A PD-LGD-EAD representation is used only when its marginal default, exposure, severity, timing, and discounting are consistent with that method. The ECL engine, not the HLR, owns staging, macro scenario weights, effective-interest discounting, management overlays, and journals.

The SPV cohort engine receives monthly collections, recoveries, refunds, costs, purchases, and exposure states. It produces one-year and ultimate pool loss, Class A/B/C cash and loss, reserve and OC paths, trigger timing, and reverse stresses. Pricing EL, accounting ECL, economic capital, regulatory capital, and transaction credit enhancement retain separate definitions.

# 12. Validation and Acceptance

Approval requires:

1. point-in-time and label-maturity reconstruction;
2. driver-grouped and time-forward validation;
3. held-out platform and geography tests where relevant;
4. P-spline shape, support, prior, and penalty sensitivity;
5. explicit-only, neural-only, raw-combination, and residual-combination ablations;
6. NUTS versus Pólya-Gamma posterior and decision agreement if the latter is used;
7. convergence, Monte Carlo error, and posterior predictive diagnostics;
8. HLR-survival horizon reconciliation and censoring audit;
9. EAD, cure, LGD, recovery, refund, and timing backtests;
10. dependence-family and no-copula benchmarks;
11. calibration, discrimination, uncertainty coverage, fairness, and action stability;
12. online-offline numerical parity and safe fallback;
13. IFRS 9 cash-shortfall reconciliation; and
14. SPV cohort, waterfall, tranche-loss, and reverse-stress reconciliation.

The production champion is the least complex approved model that provides stable decision-relevant value. The explicit-only hierarchical model is the mandatory fallback. Advanced challengers remain available as evidence grows.

# References

[1] P. H. C. Eilers and B. D. Marx, “Flexible smoothing with B-splines and penalties,” *Statistical Science*, vol. 11, no. 2, pp. 89-121, 1996, doi: 10.1214/ss/1038425655.

[2] N. G. Polson, J. G. Scott, and J. Windle, “Bayesian inference for logistic models using Pólya-Gamma latent variables,” *Journal of the American Statistical Association*, vol. 108, no. 504, pp. 1339-1349, 2013, doi: 10.1080/01621459.2013.829001.

[3] D. R. Cox, “Regression models and life-tables,” *Journal of the Royal Statistical Society: Series B*, vol. 34, no. 2, pp. 187-220, 1972, doi: 10.1111/j.2517-6161.1972.tb00899.x.

[4] N. Laird and D. Olivier, “Covariance analysis of censored survival data using log-linear analysis techniques,” *Journal of the American Statistical Association*, vol. 76, no. 374, pp. 231-240, 1981, doi: 10.1080/01621459.1981.10477634.

[5] M. S. Wulfsohn and A. A. Tsiatis, “A joint model for survival and longitudinal data measured with error,” *Biometrics*, vol. 53, no. 1, pp. 330-339, 1997, doi: 10.2307/2533118.

[6] J. Piironen and A. Vehtari, “Sparsity information and regularization in the horseshoe and other shrinkage priors,” *Electronic Journal of Statistics*, vol. 11, no. 2, pp. 5018-5051, 2017, doi: 10.1214/17-EJS1337SI.
