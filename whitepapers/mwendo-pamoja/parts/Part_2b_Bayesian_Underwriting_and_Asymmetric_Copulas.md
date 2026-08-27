---
title: "Part 2b: Continuous Underwriting via Hierarchical Bayesian Logistic Regression and Asymmetric Copulas"
author: "Nevil Maloba"
date: "25 August 2026"
status: "Narrative white paper edition"
output:
  pdf_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
  word_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
---

# 1. Continuous Underwriting via Hierarchical Bayesian Logistic Regression

## 1.1. From Deterministic Embeddings to Posterior Distributions

Part 2a ended with two objects arriving at the same inferential boundary. The first is a neural representation \(\boldsymbol\Phi_{it}\) of short-term sequence and slower context. The second is an explicit vector \(\mathbf z_{it}\) of named liquidity variables. Neither is a sufficient statistic, neither is a probability, and neither is allowed to decide credit on its own. Part 2b asks how to combine them without counting the same economic signal twice, how to represent uncertainty in sparse cohorts, and how to carry marginal risk into a portfolio dependence model.

The Hierarchical Bayesian Logistic Regression translates those inputs into a posterior predictive distribution [1], [2]. Partial pooling can stabilise sparse geography, platform, product, and time effects. Posterior intervals expose parameter and predictive uncertainty under the specified model. Explicit spline terms remain economically interpretable, while latent neural coefficients do not become causal simply because they sit inside a regression. The model is therefore a governed predictive instrument, not a causal proof or an accounting engine.

The human use of that uncertainty is central. A thin-file driver should not be described as unsafe merely because the model knows less. The posterior and its data-quality context move to a separate Credit Policy and Compliance Gate, which can select a smaller limit, request another lawful signal, use an explicit-only fallback, refer the case, or decline where the product rule requires it.

## 1.2. The Partial Pooling Framework and Model Taxonomy

The choice of partial pooling, hierarchical Bayesian modeling, over alternative approaches requires precise justification, since it is a non-trivial modeling decision with substantial implications for both predictive performance and regulatory acceptability.

- **Complete Pooling (standard logistic regression):** A single global coefficient vector $\boldsymbol{\beta}$ is estimated across all drivers, treating the portfolio as a homogeneous population. This ignores the structural heterogeneity of the gig-economy portfolio: a driver in a dense Nairobi CBD corridor faces fundamentally different surge patterns, traffic kinematics, and macro exposure than a driver in a peri-urban Kisumu route with degraded infrastructure and lower baseline demand. A single global $\boldsymbol{\beta}$ systematically mis-estimates PD for every specific cluster.
- **No Pooling (independent models per cluster):** An independent logistic regression is fit for each cluster $j = [\text{geohash}, \text{platform}]$. For data-rich clusters (hundreds of observed defaults), this is unproblematic. For newly launched clusters (zero observed defaults in the first 60 days), the maximum likelihood estimate of the default probability is identically zero, the model learns that default is impossible in a new corridor simply because it hasn't happened yet. This is not a feature; it is catastrophic overfitting in sparse data.
- **Partial Pooling (hierarchical Bayesian):** Cluster-specific parameters $[\alpha_j, \boldsymbol{\beta}_j]$ are treated as random variables drawn from a global portfolio-level distribution. Data-sparse clusters borrow statistical strength from the global posterior, their PD estimates are pulled toward the portfolio mean, preventing the zero-default pathology. Data-rich clusters have sufficient evidence to pull their estimates away from the mean, capturing genuine local heterogeneity. This is the Bayesian analogue of shrinkage estimation: sparse clusters are shrunk toward the global mean; dense clusters are shrunk less. The degree of shrinkage is not set by the analyst but is inferred from the data through the hyperprior on the between-cluster variance.

The three-level hierarchical structure is:

- **Level 1, Individual Driver Likelihood:**
  $$Y_{ijt}^{(p)} \sim \text{Bernoulli}(\theta_{ijt}^{(p)})$$

  for driver $i$ in cluster $j$, concerning product $p \in \{\text{micro}, \text{revol}, \text{IPF}\}$, at time $t$.

- **Level 2, Cluster Prior (Non-Centered Parameterization):**
  To avoid **Neal's Funnel** geometry, a pathology in hierarchical models where gradient-based samplers (like HMC/NUTS) struggle as the scale parameter approaches zero, creating a narrow bottleneck, we utilize the "Matt trick" (non-centered parameterization). This mathematically detaches the dependence between the group-level effects and their overarching scale parameter, transforming a highly curved probability space into a smooth, isotropic Gaussian distribution.

  The raw, independent standard normal noise components are defined as:
  $$\tilde{\alpha}_j^{(p)} \sim \mathcal{N}(0, 1), \qquad \tilde{\boldsymbol{\beta}}_j^{(p)} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

  The actual cluster-level effects are then deterministically shifted and scaled:
  $$\alpha_j^{(p)} = \mu_\alpha^{(p)} + \sigma_\alpha^{(p)} \cdot \tilde{\alpha}_j^{(p)}$$
  $$\boldsymbol{\beta}_j^{(p)} = \boldsymbol{\mu}_\beta^{(p)} + \boldsymbol{\sigma}_\beta^{(p)} \odot \tilde{\boldsymbol{\beta}}_j^{(p)}$$

- **Level 3, Portfolio Hyperpriors:**
  $$\mu_\alpha^{(p)} \sim \mathcal{N}(0, 2), \qquad \boldsymbol{\mu}_\beta^{(p)} \sim \mathcal{N}(\mathbf{0}, 2\mathbf{I})$$
  $$\sigma_\alpha^{(p)} \sim \text{Half-StudentT}(\nu=3, \sigma_0=1), \qquad \boldsymbol{\sigma}_\beta^{(p)} \sim \text{Half-StudentT}(\nu=3, \sigma_0=1)$$

The scale parameters ($\sigma$) are regularized using a **Half-Student T** prior.
Its generalized probability density function is:

$$f(\sigma) = \frac{2}{\sigma_0} \frac{\Gamma(\frac{\nu+1}{2})}{\Gamma(\frac{\nu}{2}) \sqrt{\nu\pi}} \left(1 + \frac{1}{\nu}\left(\frac{\sigma}{\sigma_0}\right)^2\right)^{-\frac{\nu+1}{2}}, \quad \sigma > 0$$

*Structural Note on Tail Geometry:* While the non-centered parameterization fixes the underlying coordinate system, we must still carefully govern the scale prior. Setting the degrees of freedom to $\nu = 1$ collapses the Half-Student T into a **Half-Cauchy** distribution. While a Half-Cauchy(1) maximizes sparsity, its extreme heavy tails allow the scale parameter to drift into unproportionally large values when data is sparse, forcing the NUTS sampler to diverge across the wide body of the funnel. To gently curb this extreme tail behavior while preserving robustness to genuine structural breaks, we explicitly regularize the prior by setting $\nu=3$ (or alternatively, utilizing a Half-Normal). This achieves the optimal mathematical compromise between heavy-tailed adaptability and HMC sampling efficiency.

Unlike the Normal distribution (which would assign negative mass to variance parameters and requires truncation), and unlike the Inverse-Gamma distribution (which concentrates too much mass away from zero and over-regularizes in the presence of genuine between-cluster heterogeneity, the Gelman critique), the Half-Student T ($\nu=3$) allows the model to discover genuinely large inter-cluster variance when the data supports it without destabilizing the leapfrog integrator.

## 1.3. Full Mathematical Model Specification

The production specification is intentionally block-structured:

$$
Y_i^{(p)}\sim\operatorname{Bernoulli}(p_i^{(p)}),
\qquad
\operatorname{logit}(p_i^{(p)})=\eta_i^{(p)},
$$

$$
\eta_i^{(p)}
=
\alpha^{(p)}
+a_{g[i]}^{(p)}
+b_{\ell[i]}^{(p)}
+c_{t[i]}^{(p)}
+\mathbf q_i^{\mathsf T}\boldsymbol\beta_z^{(p)}
+\widetilde{\mathbf h}_i^{\mathsf T}\boldsymbol\beta_h^{(p)}
+\boldsymbol\psi_i^{\mathsf T}\boldsymbol\gamma^{(p)}
+\mathbf m_i^{\mathsf T}\boldsymbol\delta^{(p)}.
$$

The blocks have different jobs:

- \(\alpha^{(p)}\) is the product intercept.
- \(a_{g[i]}^{(p)}\), \(b_{\ell[i]}^{(p)}\), and \(c_{t[i]}^{(p)}\) are centered, partially pooled geography, platform, and cohort-time effects.
- \(\mathbf q_i=Q(\mathbf z_i)\) is a centered and QR-orthogonalised B-spline basis of the Explicit Liquidity Features.
- \(\widetilde{\mathbf h}_i\) is the neural representation after out-of-fold residualisation against explicit liquidity and metadata.
- \(\boldsymbol\psi_i\) contains a small pre-registered interaction set under strong heredity.
- \(\mathbf m_i\) contains approved metadata and data-quality terms that are neither neural nor liquidity metrics.

The residual neural block is defined by

$$
\widetilde{\mathbf h}_i
=
\mathbf h_i-
\widehat{\mathbb E}_{-k(i)}
\left[\mathbf h_i\mid\mathbf q_i,\mathbf m_i\right].
$$

The projection is fitted without observation \(i\)'s validation fold. It does not guarantee perfect orthogonality in a new regime, but it sharply reduces the route by which the neural branch can reconstruct CFA, DLR, Earnings Velocity, Repayment Velocity, or reserve balance and count it again.

To keep a high-dimensional neural block from overwhelming the interpretable model, the implementation uses:

1. a fixed low-dimensional bottleneck selected inside training folds;
2. standardisation and whitening fitted on training data;
3. a regularized horseshoe or comparable block-shrinkage prior on \(\boldsymbol\beta_h\) [3], [17];
4. separate shrinkage scales for explicit, neural, interaction, and metadata blocks;
5. strong heredity for interactions;
6. non-centred hierarchical effects with sum-to-zero identification; and
7. ablation gates requiring stable incremental value over the explicit-only model.

The score is calibrated out of time by product:

$$
\operatorname{logit}\left(PD_{i,\mathrm{cal}}^{(p)}\right)
=
\kappa_p+s_p\eta_i^{(p)},
\qquad s_p>0.
$$

Calibration is part of the model, not a cosmetic report. The decision service records the calibrated PD, interval, tail probability, model version, feature versions, fallback status, and reason-code inputs.

This specification deliberately avoids cluster-specific coefficient vectors over the full neural embedding. With limited defaults, that construction would multiply a high-dimensional identifiability problem across clusters. Partial pooling is concentrated in interpretable intercepts and a small number of pre-registered slopes where the data supports them.

## 1.4. Nonlinear Functional Forms: B-Splines as Smooth Alternatives to Binning

Several key continuous covariates exhibit strongly nonlinear relationships with default probability that linear terms cannot capture:

- **DLR** ($\mathrm{DLR}^{(h)}_i$): the relationship may steepen as obligations due over horizon $h$ approach or exceed available liquidity. Values near one have economic meaning, but no universal default boundary or curve shape is imposed.
- **Repayment Velocity** ($v_{\text{repay}}$): movement from missed to scheduled repayment may be more informative than movement among large prepayments. The plateau and direction are tested by product and window.
- **Driver tenure:** an early learning or selection effect may flatten over time. A spline prevents an unbounded linear extrapolation while allowing the evidence to determine whether the relationship exists.

The diagnostic protocol begins with a regularised linear baseline. For a discrete Bernoulli outcome, a randomized quantile residual is

$$
r_i=\Phi^{-1}\!\left(F_i(y_i^-)+u_i\left[F_i(y_i)-F_i(y_i^-)\right]\right),
\qquad u_i\sim\operatorname{Uniform}(0,1),
$$

where $F_i(y_i^-)$ is the probability strictly below the observed outcome. Under correct specification these residuals should be approximately standard normal, subject to estimation and dependence [4]. Residual structure, calibration curves, partial-residual plots, and out-of-time performance can motivate a spline. Binning is used for visual diagnostics with uncertainty and adequate counts, not as the sole test.

A B-spline of degree $d$ over a continuous covariate $x$ is defined by a non-decreasing knot sequence $\xi_0\le\xi_1\le\ldots\le\xi_{K+d}$ and $K$ basis functions with the Cox-de Boor recursive definition [5]:

$$B_{k,0}(x) = \mathbf{1}[\xi_k \leq x < \xi_{k+1}]$$
$$
B_{k,d}(x)
=
\frac{x-\xi_k}{\xi_{k+d}-\xi_k}B_{k,d-1}(x)
+
\frac{\xi_{k+d+1}-x}{\xi_{k+d+1}-\xi_{k+1}}B_{k+1,d-1}(x),
$$

with a fraction defined as zero when its denominator is zero.

The resulting $f(x)=\sum_{k=1}^{K}\zeta_kB_{k,d}(x)$ is a piecewise polynomial of degree $d$. At a simple interior knot it has continuity through derivative order $d-1$; repeated knots reduce continuity. In contrast, a binned single-variable effect is piecewise constant unless further structure is added. B-splines avoid forced jumps at ordinary internal knots, but knot placement, boundary handling, shrinkage, and extrapolation still affect the fitted curve.

Adjacent B-spline bases overlap, so independent diffuse coefficients can create an unnecessarily rough and weakly identified curve. A first-order random-walk or AR(1) prior can regularise adjacent coefficients. This is a smoothing choice, not an out-of-distribution defence by itself.

One candidate specification uses an **autoregressive order 1 prior** [6]:

$$\zeta_k \sim \mathcal{N}(\rho \zeta_{k-1}, \sigma_\zeta^2), \quad k = 2, \ldots, K$$

An AR(1) prior smooths adjacent coefficients when the coefficient index has an appropriate ordering. It is not a universal out-of-distribution kill-switch, and B-splines outside their boundary knots require an explicit extrapolation rule. Production therefore clips to validated support, adds an out-of-range indicator, widens uncertainty, and sends the action to the policy gate.

The innovation variance $\sigma_\zeta^2$ controls the degree of local variation: as $\sigma_\zeta\to0$, adjacent coefficients are pulled toward the AR(1) path; larger values permit more variation. The posterior estimates $\sigma_\zeta$ jointly with the coefficients under an analyst-chosen prior. The data do not choose smoothing free of judgement, so prior predictive checks, sensitivity analysis, boundary behaviour, and out-of-time comparison remain necessary.

The positive innovation scale \(\sigma_\zeta\) can receive a Half-Student-\(t\) prior [16]. This choice permits more prior mass on large scales than a half-normal while still regularising. It does not make extreme observations penalty-free, and sensitivity to the scale and degrees of freedom must be reported.

For weakly identified group scales, a non-centred parameterisation often improves HMC geometry, but centred and non-centred alternatives should be tested. To separate the spline level from intercepts, centre the realised smooth over the training observations,

$$
\sum_{i=1}^{N}f(x_i)=\sum_{i=1}^{N}\sum_{k=1}^{K}\zeta_kB_{k,d}(x_i)=0,
$$

or use an equivalent centred basis. This assigns the average spline level to the intercept while retaining nonlinear shape; it does not eliminate all posterior dependence.

Centering, constraints, orthogonalisation, and non-centred parameterisation can reduce posterior dependence and improve sampling geometry. Diagnostics determine whether they succeeded; the design does not eliminate correlation by assertion.

PSIS-LOO can estimate observation-level expected log predictive density without literally refitting $N$ times, provided its Pareto diagnostics are acceptable [7]. Because records repeat by driver, platform, geography, and time, grouped and out-of-time validation remains essential; naive row-level LOO can overstate transportability. A spline is retained when diagnostics, calibration, decision value, and held-out performance support it. WAIC can be secondary evidence, not an independent confirmation when both criteria use the same posterior and data.

## 1.5. Time-Varying Coefficients: AR(1) Autoregressive Priors

IFRS 9 expected credit loss uses reasonable and supportable forward-looking information [12]. For underwriting, this motivates testing whether macro-related coefficients $\boldsymbol{\delta}$, including sensitivity to fuel prices, platform commission, and ZEV transition, vary through time. A time-varying coefficient is adopted only if the data identify it and held-out performance supports it.

A coefficient estimated on a 2020 to 2023 window may not transport to a later portfolio under different energy prices, demand, platform rules, or ZEV policy. One candidate is to model selected macro coefficients as time-indexed parameters governed by first-order autoregressive priors:

$$
\delta_{k,t}
\sim
\mathcal N\left(
\mu_k+\rho_k(\delta_{k,t-1}-\mu_k),
\sigma_{\delta_k}^2
\right).
$$

where:

- $\mu_k$ is the long-run stationary mean of the $k$-th macro coefficient, the baseline sensitivity when no regime shift has occurred.
- \(\rho_k\in(-1,1)\) is the persistence coefficient. A range such as 0.85-0.95 may be used in sensitivity analysis, but is not described as empirically appropriate before fitting and validating the relevant series.
- $\sigma_{\delta_k}^2$ is the innovation variance, the magnitude by which the coefficient can shift from one period to the next, controlling the sensitivity of the model to new macro information.

Under a stationary initial distribution and \(|\rho_k|<1\), the AR(1) variance is \(\operatorname{Var}[\delta_{k,t}]=\sigma_{\delta_k}^2/(1-\rho_k^2)\). This contrasts with the random-walk special case \(\rho_k=1\):

$$\delta_{k,t} \sim \mathcal{N}(\delta_{k,t-1}, \sigma_{\delta_k}^2)$$

The RW1 is non-stationary and has no mean-reverting level. It may represent gradual drift, while a stationary AR(1) represents variation around a long-run mean. Neither prior should be selected merely by labelling a shock permanent or cyclical. Prior predictive behaviour, forecast performance, and sensitivity determine which description is adequate.

The **time-varying cohort shock effect** $\gamma_{jt}$, an AR(1) prior on cluster-level baseline risk, follows the same structure:

$$\gamma_{jt} \sim \mathcal{N}(\rho_j \gamma_{j,t-1}, \sigma_\gamma^2)$$

When an unobserved common shock affects cluster $j$, such as a regional fuel disruption, labour action, or local platform change, the posterior for $\gamma_{jt}$ may shift for the cluster. A driver with otherwise stable evidence can therefore receive a higher conditional PD because peers share an adverse state. This is one Bayesian representation of default clustering; it must not be interpreted as proof that every member was exposed to the same cause.

If the time series per cluster is long enough to identify separate persistence, one may use $\rho_j\sim\operatorname{Beta}(a_\rho,b_\rho)$ on $(0,1)$ with hierarchical pooling. Otherwise a shared or parsimonious persistence structure is safer. The posterior location is an empirical result; corridor labels do not predetermine it.


# 2. Scaling to Large Policyholder Portfolios: MCMC Architecture
## 2.1. The Bernoulli-to-Binomial Aggregation for Computational Scaling

As the Insurtech scales to portfolios of hundreds of thousands of active drivers, the computational cost of full MCMC over individual Bernoulli likelihoods becomes prohibitive. Each leapfrog step in Hamiltonian Monte Carlo requires evaluating the gradient of the log-posterior with respect to all model parameters. For a Bernoulli likelihood with $N$ observations, this gradient has $O(N)$ computational complexity. At $N = 200{,}000$ drivers with daily updates, the gradient cost renders NUTS infeasible at the required update cadence.

One scaling option is Bernoulli-to-Binomial aggregation for observations with **exactly identical predictors, offsets, exposure definition, and applicable weights**. For an eligible group \(j\):

$$K_j = \sum_{i=1}^{n_j} Y_{ij} \sim \operatorname{Binomial}(n_j, \theta_j)$$

For exact equality, \(K_j\) is sufficient for the common probability. Quantising "near-identical" continuous covariates is an approximation and does not preserve the individual likelihood or Fisher information. Any such approximation must be benchmarked against an unaggregated holdout for calibration, tails, subgroup effects, and decision changes. The system should also compare minibatch variational inference, Laplace approximations, sequential updating, and periodic NUTS validation rather than assuming daily full-portfolio NUTS.

Evaluating splines at group averages does not recover within-group heterogeneity. Exact aggregation is reserved for identical design rows and a common probability. Quantised cells are explicitly labelled an approximation, benchmarked against individual likelihoods, and never described as sufficient. Individual scoring retains the original covariates.

## 2.2. LKJ Cholesky Decompositions and the Funnel Geometry

Hierarchical models can exhibit Neal's funnel when a weakly identified group scale approaches zero and group effects concentrate near the global mean. This geometry can produce divergent transitions or inefficient exploration under HMC. Divergences warn that numerical exploration is unreliable; whether estimates are materially biased depends on where the sampler failed to explore.

For correlated random effects, the implementation separates marginal scales from a Cholesky factor of the correlation matrix and can place an LKJ prior on correlation. A non-centred form is compared with a centred form. This is preferable to invoking an inverse-Wishart prior without a reason, but the exact choice remains part of model design and sensitivity analysis.

The covariance can be written as $\Sigma=\operatorname{diag}(\boldsymbol\sigma)\Omega\operatorname{diag}(\boldsymbol\sigma)$, where $\Omega$ is a correlation matrix. This parameterisation separates their prior specification, but posterior dependence can remain because the data couple scale and correlation. The sampler transforms standard-normal latent variables using the Cholesky factor.

This usually improves posterior geometry, but it does not make the target perfectly isotropic or guarantee zero divergences. \(\hat R\), effective sample size, energy diagnostics, divergences, tree depth, and posterior sensitivity must be reported from the actual fit.

The probabilistic programming pseudocode (language-agnostic conceptual representation for PyMC/NumPyro/Stan architectures) implementing the full MCMC specification:

```text
ALGORITHM: Redundancy-controlled hierarchical Bayesian logistic regression

INPUTS:
  Y[N]             Bernoulli outcomes at a defined product horizon
  Q[N, Kz]         centred, scaled, QR-orthogonalised explicit spline basis
  H_RES[N, Kh]     cross-fitted residual neural bottleneck
  R[N, Kr]         small pre-registered interaction block
  X[N, Kx]         essential contract and product metadata
  geo_id[N]        geography hierarchy
  platform_id[N]   platform or cohort hierarchy
  time_id[N]       calendar hierarchy

PRIORS:
  alpha                 ~ Normal(0, 1.5)
  sigma_geo             ~ HalfStudentT(nu=3, scale=s_geo)
  sigma_platform        ~ HalfStudentT(nu=3, scale=s_platform)
  sigma_time            ~ HalfStudentT(nu=3, scale=s_time)
  geo_raw[J]            ~ Normal(0, 1)
  platform_raw[S]       ~ Normal(0, 1)
  time effect           ~ approved AR(1), RW1, or simpler pooled structure
  beta_z, beta_h        ~ separate regularising block-shrinkage priors
  gamma_interaction     ~ strong-heredity shrinkage prior
  delta_metadata        ~ regularising prior

TRANSFORM:
  u_geo      = sigma_geo * geo_raw
  v_platform = sigma_platform * platform_raw
  tau_time   = centred time process

LINEAR PREDICTOR FOR OBSERVATION i:
  eta[i] = alpha
           + u_geo[geo_id[i]]
           + v_platform[platform_id[i]]
           + tau_time[time_id[i]]
           + dot(Q[i], beta_z)
           + dot(H_RES[i], beta_h)
           + dot(R[i], gamma_interaction)
           + dot(X[i], delta_metadata)

LIKELIHOOD:
  Y[i] ~ BernoulliLogit(eta[i])

OPTIONAL EXACT AGGREGATION:
  Only observations with an identical design row and common probability
  may be collapsed to a Binomial count. Quantised rows are approximations.

POST-FIT:
  Apply product-level out-of-fold calibration, then pass calibrated PD,
  uncertainty, data quality and reasons to the policy and compliance gate.
```

## 2.3. Production Inference: BlackJAX on GPU/TPU

BlackJAX is a candidate JAX-native inference implementation that can use compiled accelerators. The example of 200,000 observations and 4,000 groups is a benchmark scenario to be reproduced with the production likelihood. No fixed 50-fold speed-up is assumed; compilation, memory transfer, chain count, precision, and approximation error are included in the benchmark.

- **Inference candidates:** Full-data NUTS, Laplace approximation, variational inference, sequential Monte Carlo, or other methods are benchmarked on the actual posterior. Subsampled HMC with control variates is not described as unbiased or deployed until its estimator and diagnostics establish that result for this implementation. High dimension increases cost, while divergence is primarily a posterior-geometry and integration issue rather than “gradient variance” in ordinary full-data NUTS.
- **Incremental updating:** A previous posterior can initialise a later fit, but material new data, drift, or model change may invalidate the old mass matrix and step size. Adaptation is not skipped by default. The approved cadence balances information gain, inference quality, model-change governance, and operational need; underwriting scores can update from new features without retraining the whole HLR each day.


# 3. MCMC Convergence Diagnostics and Model Validation

Before a posterior summary informs portfolio analysis, accounting evidence, or a credit-policy input, inference quality must be verified. Diagnostics are rerun for every approved model version and after material data, feature, product, or method change. A PSI value of 0.25 is an internal investigation threshold, not by itself a retraining command.

## 3.1. $\hat{R}$: Rank-normalised Gelman-Rubin convergence statistic

An approved NUTS run uses multiple chains with dispersed initialisation. The classical variance-ratio intuition is

$$\hat{R} = \sqrt{\frac{\frac{N-1}{N}W + \frac{1}{N}B}{W}}$$

Modern diagnostics use split rank-normalised and folded $\hat R$, not only this classical expression [8]. Values close to one are necessary but not sufficient. A candidate acceptance threshold such as $\hat R<1.01$ is paired with effective sample size, Monte Carlo standard error, divergences, energy and tree-depth diagnostics, trace review, and sensitivity. Non-centred parameterisation can help a scale parameter but does not routinely resolve every pathology.

## 3.2. Effective Sample Size (ESS)

The Effective Sample Size corrects for autocorrelation within MCMC chains. Highly autocorrelated chains produce fewer informative samples per iteration. ESS is estimated from lag-$k$ autocorrelations $\rho_k$ of the sample sequence:

$$\text{ESS} = \frac{S}{1 + 2\sum_{k=1}^{\infty} \rho_k}$$

Bulk and tail ESS are evaluated relative to the estimand and required Monte Carlo precision. A count such as 400 can be an initial screening convention, not a universal promise that every 95 percent interval is reliable. The model uses the stated Half-Student-$t$ or other approved scale priors consistently; it does not silently switch to Half-Cauchy priors in the diagnostic narrative.

## 3.3. Posterior Predictive Checks: Exhaustive Treatment

Posterior Predictive Checks (PPCs) answer the question: "If the model is correctly specified, can it reproduce the statistical properties of the observed data?" Each PPC generates simulated outcomes $\tilde{Y}^{(s)}$ from the posterior predictive distribution for $s = 1, \ldots, S$ MCMC samples, compares their distribution to the observed outcomes $Y^{\text{obs}}$, and reports a Bayesian p-value $p_B = P(T(\tilde{Y}) \geq T(Y^{\text{obs}}))$ for a test statistic $T$.

- **PPC 1, central tendency:** Compare the posterior-predictive default-rate distribution with observed rates overall and by product, time, and relevant cohort. A discrepancy can arise from intercept, covariate, hierarchy, time, label, sampling, or calibration problems. Bayesian predictive tail areas are descriptive diagnostics and are not interpreted exactly like uniform frequentist p-values.

- **PPC 2, Tail-Risk Cascade Clustering:** Test statistic from the `.rmd` specification:

  $$T(Y) = \max_{j} \left(\frac{1}{n_j} \sum_{i \in j} Y_{ij}\right)$$

  This statistic probes extreme cluster default rates, subject to cluster size and multiple-comparison sensitivity. Failure of the marginal HLR to reproduce a cluster spike does not instruct the team to increase a Clayton parameter. First diagnose marginal calibration, omitted common factors, label and exposure definitions, hierarchy, and time structure. Dependence candidates are validated separately against joint outcomes and portfolio-loss behaviour.

- **PPC 3, Repayment Velocity nonlinearity:** Predicted PD is evaluated across observed $v_{\text{repay}}$ and compared with empirical default rates in bins that retain adequate sample size. Residual curvature, including any transition near $0.8<v_{\text{repay}}<1.2$, is evidence to test a spline, not proof that a fixed “critical zone” exists. The check is repeated when the model or population changes.

- **PPC 4, cluster heterogeneity:** Compare observed and posterior-predictive between-cluster variation with uncertainty and minimum-count rules. Underdispersion can reflect excessive shrinkage, omitted predictors, time effects, labels, or the likelihood, while apparent overdispersion can reflect small cells. Prior-scale sensitivity is one diagnostic, not an automatic instruction to double a parameter.

- **PPC 5, time-varying cohort effect:** Compare predicted and observed monthly rates by adequately sized clusters, then inspect residual autocorrelation. A pattern may implicate persistence, omitted seasonality or shocks, exposure mix, reporting lag, or label drift. Recent data enter through the governed update process, and a prior changes only after documented sensitivity and validation.

## 3.4. Discrimination, Calibration, and Stability Metrics

**Kolmogorov-Smirnov statistic:** Measures the maximum separation between score distributions for observed defaulters and non-defaulters. No universal KS above 0.40 is asserted as an IFRS 9 or Kenyan regulatory requirement. Thresholds are product- and use-specific and cannot replace calibration or accounting governance.

**Gini coefficient and AUC-ROC:** These measure ranking discrimination. An AUC target such as 0.75 can be a development objective, not a universal acceptability boundary. Partial pooling may reduce unstable extremes in sparse groups, but whether it improves held-out discrimination and calibration is measured.

**Brier score:**

$$
\operatorname{BS}=\frac{1}{N}\sum_{i=1}^{N}\left(p_i^{\mathrm{cal}}-Y_i\right)^2.
$$

The score measures squared probability error and reflects both calibration and resolution [9]. Partial pooling and shrinkage can help sparse groups, but superiority over a classical or explicit-only baseline is an out-of-time empirical result, not a mathematical consequence of being Bayesian.

**Population Stability Index (PSI), production monitoring:** PSI compares the model's current score distribution $A_b$ with a reference distribution $E_b$ across $B$ bins:

$$
\mathrm{PSI}
=
\sum_{b=1}^{B}
(A_b-E_b)
\ln\left(\frac{A_b+\varepsilon}{E_b+\varepsilon}\right).
$$

**Table 1: Discrimination, Calibration, and Stability Metrics Summary**

| PSI Range | Interpretation | Action |
|---|---|---|
| PSI < 0.10 | Limited shift under this convention | Continue routine monitoring |
| \(0.10\le\mathrm{PSI}<0.25\) | Monitoring convention: moderate shift | Investigate data, population, and performance |
| \(\mathrm{PSI}\ge0.25\) | Monitoring convention: large shift | Escalate; consider restrictions and recalibration after diagnosis |

A PSI threshold such as 0.25 is a common internal monitoring convention and may be adopted contractually; it is not a universal statutory trigger under SR 11-7, Basel, or Kenyan law. A breach can reflect population movement, seasonality, a pipeline defect, or a definition change. The response is diagnosis, performance review, and proportionate restriction. Automated retraining is not safe without corrected data, validation, approval, and deployment controls.


# 4. Real-Time Bayesian Decision Boundaries
## 4.1. The Loss Function Framework: Expected Value Maximization

A fixed rule such as “approve when $\hat\theta<5\%$” discards posterior uncertainty. Two drivers can share a 4.5 percent posterior mean while one has a narrow credible interval and the other a wide interval caused by thin or conflicting evidence. A probability distribution bounded on $[0,1]$, or posterior draws transformed from the logit scale, should be used rather than an unconstrained normal approximation for PD.

The Bayesian decision framework can integrate a payoff over posterior draws [1]. Define action $a_1$ as approving a limit extension and $a_0$ as declining it. For a linear payoff, expected value depends on the posterior mean, while separate uncertainty and tail rules retain information about width and shape. The asymmetric payoff for $a_1$ is:

- True outcome, no default: gain \(L_{\text{gain}}\), net interest and permitted fees.
- True outcome, default: loss \(L_{\text{loss}}\), unrecovered principal plus defined costs.

The expected financial value of approval is computed by averaging the payoff over all $S$ MCMC posterior samples $\theta^{(s)}$:

$$
\mathbb E[V(a_1)]
=
\frac{1}{S}\sum_{s=1}^{S}
\left[
(1-\theta^{(s)})L_{\text{gain}}
-\theta^{(s)}L_{\text{loss}}
\right].
$$

The expected cost of denial (opportunity cost of rejecting a creditworthy driver):
$$
\mathbb E[V(a_0)]
=
-\frac{1}{S}\sum_{s=1}^{S}
(1-\theta^{(s)})L_{\text{opp}}.
$$

Setting $\mathbb{E}[V(a_1)] = \mathbb{E}[V(a_0)]$ and solving for the break-even posterior mean PD yields the **Bayesian action threshold** $p^*$:

$$p^* = \frac{L_{\text{gain}} + L_{\text{opp}}}{L_{\text{gain}} + L_{\text{opp}} + L_{\text{loss}}}$$

This threshold is not a fixed number: it is calibrated separately for each product, since the loss structure differs materially across the triple product stack.

**For microloans with a 7 to 30 day tenor:**

- $L_{\text{gain}} = K \cdot r \cdot \text{days} / 365$ (annualized fee on principal $K$)
- \(L_{\text{loss}}=K(1-R)\), principal net of a validated recovery rate and recovery cost;
- $L_{\text{opp}} = K \cdot (\text{Alternative Portfolio Yield} / 26)$
- The former 12 to 18 percent threshold is retained only as an illustrative sensitivity range. The production value must be recomputed from lawful price, exposure, loss, recovery timing and cost, funding, operations, affordability, and policy. No “garnishment recovery” is assumed.

**For Revolving Credit Lines:**

- $L_{\text{gain}} = V_{\text{max}} \cdot U \cdot i + M$ (interest on utilized balance $U$ at rate $i$, plus monthly maintenance fee $M$)
- \(L_{\text{loss}}=V_{\max}\psi(1-R)\), potential loss after stress drawdown and recovery;
- \(L_{\text{opp}}=V_{\max}(1-U)\mathrm{CostOfCapital}\);
- The former 3 to 6 percent threshold is an illustrative sensitivity range. A revolving threshold depends on stress utilisation, EAD, LGD, recoveries, income, funding, operations, and portfolio constraints, then remains subject to the policy gate.

## 4.2. Three Automated Decision Rules

1. **Dynamic soft cap:** The economic comparison \(\mathbb E[V(a_1)]>\mathbb E[V(a_0)]\) is an input to the Credit Policy and Compliance Gate, not an automatic approval. Affordability, product eligibility, licence, consent, exposure, and hardship rules remain binding.

2. **Uncertainty gate:** Even if the posterior mean is below \(p^*\), the probability of exceeding a product risk cap may justify a smaller limit, explicit-only fallback, referral, request for another lawful signal, or freeze. The cap is an internal or contractual policy value, not automatically a regulatory threshold:
$$P(\theta_{ijt}^{(p)} > \theta_{\text{cap}}) = \int_{\theta_{\text{cap}}}^{1} p(\theta | \text{Data}) \, d\theta > \epsilon_{\text{kill}}$$
for a configurable exceedance probability \(\epsilon_{\text{kill}}\). The value 0.10 remains a validation candidate, and the action must account for why uncertainty is high.

3. **Portfolio shock review:** A material rise in the cohort-time effect can trigger investigation and portfolio controls. A two-standard-deviation rule is illustrative. A geography-wide rollback requires evidence, fairness review, authority, and a defined cure because the signal can also reflect a data incident or an unmodelled benign shift.


The HLR's pricing handoff ends with calibrated real-world PD, uncertainty, expected-loss inputs, and a documented decision horizon. Part 5, Section 1.2.1 carries those outputs into customer and investor pricing, keeps the physical measure distinct from any market-consistent valuation measure, and reconciles expected loss with the other components of \(K_{\mathrm{RBCP}}\). This leaves Part 2b focused on underwriting inference, dependence, validation, and decision boundaries.

# 5. Actuarial Modeling of Clustered Failures via Asymmetric Copulas
## 5.1. The limits of linear correlation and Gaussian copulas

The hierarchical Bayesian engine estimates marginal posterior PD distributions for each product, $\theta_{ijt}^{(\text{micro})}$, $\theta_{ijt}^{(\text{revol})}$, and $\theta_{ijt}^{(\text{IPF})}$. Their accuracy is an empirical result. A partner holding all three exposures also needs a model of dependence to estimate joint default and portfolio loss; marginal probabilities alone are insufficient.

The portfolio variance under Gaussian dependency assumptions:

$$\text{Var}[\mathcal{L}] = \sum_p \text{Var}[\mathcal{L}_p] + \sum_{p \neq p'} \rho_{pp'} \sqrt{\text{Var}[\mathcal{L}_p]} \sqrt{\text{Var}[\mathcal{L}_{p'}]}$$

A Gaussian copula can be a useful benchmark, but for correlation below one it has zero asymptotic upper and lower tail dependence. It can still show substantial finite-threshold association. Part 1 supplies an economic reason to test lower-tail asymmetry; it does not prove that every pairwise correlation converges to one or that Clayton is the correct family. The observed dependence must be estimated by product, horizon, cohort, and regime.

## 5.2. Sklar's Theorem and the Clayton Copula

By Sklar's theorem, a multivariate distribution can be represented using its marginals and a copula; uniqueness holds for continuous marginals [10]:

$$F(t^{\text{micro}}, t^{\text{revol}}, t^{\text{IPF}}) = C\left(F_1(t^{\text{micro}}), F_2(t^{\text{revol}}), F_3(t^{\text{IPF}});\, \alpha_c\right)$$

where $u_p = F_p(t^{(p)}) \in [0,1]$ are probability integral transforms of the marginals. The copula $C:[0,1]^3\to[0,1]$ represents dependence separately from the marginal specifications. The HLR supplies calibrated marginal risk estimates; candidate copulas provide competing dependence structures. Clayton is not preselected merely because lower-tail dependence is economically plausible.

The \(d\)-dimensional Clayton copula is an Archimedean family for \(\alpha_c>0\):

$$
C_{\alpha_c}(u_1,\ldots,u_d)
=
\left(
\sum_{j=1}^{d}u_j^{-\alpha_c}-d+1
\right)^{-1/\alpha_c}.
$$

For a bivariate margin, the lower-tail dependence coefficient is:

$$
\lambda_L
=
\lim_{u\to0^+}
\Pr(U_2\le u\mid U_1\le u)
=2^{-1/\alpha_c},
\qquad \lambda_U=0.
$$

This asymmetry makes Clayton a meaningful candidate. A fitted or scenario-conditioned increase in \(\alpha_c\) raises lower-tail dependence. It does not demonstrate absolute lockstep default.

**Conditional Clayton sensitivity:** A dependence stress can change the marginals, copula family, parameter, or common-factor structure. The following values show how lower-tail dependence changes if Clayton is retained and $\alpha_c$ is increased; they are not the only permitted stress mechanism:

- **Scenario A, localised cluster shock:** $\alpha_c$ moves from 0.8 to 2.5; pairwise $\lambda_L$ moves from approximately 0.420 to 0.758.
- **Scenario B, macroeconomic liquidity crunch:** $\alpha_c=5.0$ implies pairwise $\lambda_L\approx0.871$.
- **Scenario C, limiting dependence stress:** $\alpha_c\to\infty$ implies $\lambda_L\to1$. This is a mathematical boundary, not a forecast.

The parameters above are illustrative. Production estimation compares competing families using held-out likelihood, probability-integral-transform diagnostics, formal or simulation-based goodness-of-fit checks, tail-event calibration, stability, and the resulting cash-flow decision [11].

## 5.3. Portfolio loss, unexpected loss, and capital boundaries

Let $\mathcal L^{(s)}$ be the simulated portfolio loss after dependent defaults, EAD, LGD, recoveries, and timing. Expected loss is $EL=\mathbb E[\mathcal L]$. “Unexpected loss” must be defined for the use case. Two common economic measures are

$$
UL_{\mathrm{sd}}=\sqrt{\operatorname{Var}(\mathcal L)}
\qquad\text{and}\qquad
UL_q=\operatorname{VaR}_q(\mathcal L)-EL.
$$

The copula simulation produces the joint distribution; a Clayton rank correlation is not inserted into a linear covariance formula as though it were Pearson loss correlation. Tail dependence can materially change high loss quantiles even when ordinary correlation moves little. Neither $UL_{\mathrm{sd}}$ nor $UL_q$ automatically equals regulatory capital. The partner bank applies its authorised prudential approach, while the SPV uses contractually defined stresses and cash-flow tests.

The portfolio simulation separates parameter uncertainty from correlated outcome simulation:

1. Draw HLR parameters and calibrated marginal PDs \(p_{i,p}^{(s)}\) from the posterior.
2. Draw a dependent uniform vector \(\mathbf U_i^{(s)}\) from the selected copula with a jointly estimated or scenario-conditioned parameter.
3. Set \(Y_{i,p}^{(s)}=\mathbf 1[U_{i,p}^{(s)}\le p_{i,p}^{(s)}]\).
4. Draw or scenario-set EAD, LGD, recovery timing, prepayment, and collection timing without double-counting the same systematic factor.
5. Compute monthly product and portfolio cash loss and pass it through the SPV waterfall.

The empirical loss quantile is a modelled VaR-type measure for the stated horizon and measure. A central 90% posterior predictive interval and a 95th loss quantile share an endpoint only under a particular definition; they are not generally equivalent and neither automatically constitutes regulatory capital. The cash-flow model must specify whether losses are real-world, accounting, economic-capital, contractual stress, or market-valued quantities.


**Figure 1: End-to-End Underwriting Pipeline (Data Engineering to Joint Tail Risk Pricing)**
```{.mermaid layout=fullpage}
%%{init: {"flowchart": {"defaultRenderer": "elk"}}}%%
graph TD
    %% Subgraph: Data Engineering & Neural Embeddings
    subgraph DE [Heterogeneous Multimodal Feature Store]
        DB_Tel[(Telematics / Ledger)] -->|Debezium CDC| Kafka[Apache Kafka]
        Kafka --> Flink[Apache Flink Stream: Kappa Path]

        DB_Mac[(Raw Macro Data)] --> Bronze[(Iceberg Bronze Tables)]
        Bronze --> Flink_Batch[Apache Flink Batch: Clean & Enrich]
        Flink_Batch --> Lake[(Iceberg Silver Tables: Delta Path)]

        Flink -->|High-Freq Windowing| GRU[GRU Layer]
        Lake -->|Monthly Batch| Trans[Transformer SwiGLU Layer]

        GRU --> Fusion{Cross-Attention Fusion}
        Trans --> Fusion
        Fusion -->|Dense Vector Φ_t| VectorSpace((Vector Representation))

        Flink -->|Explicit Liquidity Feature Path| TabularVars[Explicit Liquidity Features & Interactions]
    end

    %% Subgraph: Hierarchical Bayesian Inference
    subgraph HBM [Hierarchical Bayesian Underwriting]
        TabularVars --> BinomialAgg[Binomial Aggregation]
        BinomialAgg --> B_Splines[B-Spline Mapping]
        B_Splines -->|"AR(1) Priors"| AR1["Half-Student T Variance Scale"]

        VectorSpace --> Residual[Cross-Fitted Residualization]
        Residual --> MCMC[Hierarchical Bayesian Inference]
        AR1 --> MCMC
        Priors["LKJ Cholesky Hyperpriors"] --> MCMC

        MCMC -->|Non-Centered Param| MarginalPD[Marginal PD Posteriors]
        MarginalPD --> Cal[Product Calibration]
        Cal --> Gate[Credit Policy and Compliance Gate]
    end

    %% Subgraph: Copula and Joint Risk Pricing
    subgraph COP [Joint Tail Risk Pricing]
        Cal --> Clayton[Candidate Dependence Models]
        MacroShock["Macroeconomic Shock Factor theta"] --> Clayton
        Clayton -->|Lower Tail Dependence| UL[Unexpected Loss Quantification]
    end

    DE --> HBM
    HBM --> COP

    style DE fill:#2980b9,color:#fff,stroke:#1f618d
    style HBM fill:#8e44ad,color:#fff,stroke:#732d91
    style COP fill:#e74c3c,color:#fff,stroke:#c0392b
```

# 6. Explainability and model-risk governance for \(K_{\mathrm{RBCP}}\)

The HLR estimates one component of credit risk. Governance must still connect the feature record, calibrated PD, policy action, customer terms, override, and monitoring result. Explainability is therefore organised around the decision and its economic components, not around a claim that a latent vector is causal.

The CBK framework expresses the contractual lending rate through two separately traceable components:

$$
R_{\mathrm{customer},t}
=
\mathrm{KESONIA}_t+K_{\mathrm{RBCP},i,t},
$$

with fees and charges added for total cost of credit [13], [14]. A compounded KESONIA amount may be used for accrual over a period, but \(CCR_t\) should not replace the reference-rate term in the customer-pricing identity. KESONIA requires source, dates, calendar, compounding, and fallback controls; it is not immune to operational error.

The institution should reconcile \(K_{\mathrm{RBCP}}\) to expected loss, cost of capital, operating and liquidity costs, margin, and approved adjustments. A local model explanation cannot prove that the entire price is unbiased or objectively necessary. The audit package therefore combines component reconciliation, explicit reason codes, counterfactual checks, data lineage, subgroup outcomes, overrides, complaints, and independent validation.

## 6.1. Explanation as part of a challengeable decision

A GRU or Transformer representation is not self-explanatory to a credit officer, driver, validator, or auditor. Even an explicit variable can be misunderstood if its window, transformation, interaction, and decision context are hidden. The explanation design must therefore begin with the economic decision, the authorised rule, and the model component that materially influenced it.

SHAP and LIME are useful diagnostic tools, but neither is treated as a compliance certificate or a substitute for intelligible product reason codes. The implementation combines model-behaviour explanations with the explicit-feature record, rule result, price-component reconciliation, contract terms, override, and outcome.

### 6.1.1. SHAP (SHapley Additive exPlanations) Integration

Rooted in cooperative game theory, Shapley values define an additive attribution under a specified value function and background distribution. Exact computation is often infeasible, so practical SHAP implementations use model-specific methods or approximations. Results can change with feature dependence, background data, output scale, and model version.

For a material credit decision, the system may generate a local explanation of the calibrated PD or another clearly identified model output. It does not represent the entire customer premium as a model attribution. An illustrative explanation can separate:

- **Base Rate (Expected Value):** The unconditional mean risk premium for the driver's geographic cluster assuming no behavioral data is provided (e.g., $K = 3.50\%$).
- **Positive SHAP Contributions (Increasing Risk):**
    - an illustrative contribution from declining Repayment Velocity, sourced from the Explicit Liquidity Feature Path rather than the GRU;
    - an illustrative contribution from an approved platform-context term and a separately owned liquidity interaction;
- **Negative SHAP Contributions (Decreasing Risk):**
    - an illustrative protective contribution supported by a validated operational feature.

The production record stores model, feature, data, policy, price-component, and explanation versions under a governed retention schedule. SHAP is a model-behaviour explanation conditional on a background distribution. It cannot demonstrate that a decision was free of discriminatory proxies; outcome and counterfactual testing remain necessary.

For a chosen explanation scale, the SHAP values $\phi_i$ obey the additive representation:
$$f(x) = \phi_0 + \sum_{i=1}^{M} \phi_i$$
where $\phi_0$ is the selected background expectation and $M$ is the number of explained features or representation components. A neural approximation such as DeepSHAP can run asynchronously after inference, but its fidelity must be tested and its output stored with the prediction, background dataset, and explanation version. Bronze and Silver ingestion layers should not manufacture a post-decision explanation as though it were source data.

### 6.1.2. Local Interpretable Model-Agnostic Explanations (LIME)

LIME can provide a complementary local surrogate when its neighbourhood, perturbation process, kernel, and stability are appropriate. It is not assumed to be a reliable fast path merely because it is cheaper than an exact Shapley calculation.

LIME fits a simple local surrogate, such as a sparse linear model, to perturbed observations around a selected representation. Its coefficients approximate local behaviour under the chosen perturbation distribution and kernel; they are not necessarily the true gradient, a causal effect, or stable under correlated inputs.

A local surrogate may help a reviewer explore model sensitivity, but customer-facing reasons should come from stable mappings to material explicit factors, policy rules, and contract actions. The system must not tell a driver that an irregular shift caused a restriction when the explanation only describes a fragile local approximation. A more detailed model-behaviour analysis can run asynchronously for validation and complaints without being mislabelled as a mandated regulatory log.

## 6.2. Model-risk management with SR 11-7 as a comparative benchmark

Kenyan law, CBK requirements, partner policy, and the final institutional governance framework determine the applicable obligations. U.S. Federal Reserve SR 11-7 remains a useful comparative reference for conceptual soundness, validation, governance, and outcomes analysis [15]; it is not Kenyan law, and this paper does not claim compliance with an unverified successor circular.

The target operating model separates development, independent validation, approval, deployment, monitoring, and change control. Satisfying those controls is an evidence-based institutional conclusion, not an architectural property.

### 6.2.1. Separation of Development and Validation

The data science team responsible for training the GRU and Transformer layers is organisationally separated from the function responsible for independent challenge and approval. The validation scope includes:

1. **Conceptual soundness:** Challenge the Half-Student-$t$ hyperpriors, hierarchy, spline basis, residualisation, interactions, likelihood, and candidate copulas. Test whether partial pooling understates or overstates risk in data-sparse corridors and document uncertainty rather than requiring an impossible proof of absence.
2. **Outcome Analysis (Backtesting):** Stress-testing the model against out-of-sample data, specifically evaluating how the model predicts defaults during extreme, unobserved tail events (e.g., a hypothetical 40% overnight fuel price spike or a total platform outage).
3. **Discriminatory Power Metrics:** Calculating the Receiver Operating Characteristic (ROC) curve, Area Under the Curve (AUC), and the Brier Score (to measure the calibration of the predicted probabilities against actual outcomes).

Only after the accountable committees approve the model, limitations, thresholds, monitoring, fallback, and deployment package may a signed artefact enter production.

### 6.2.2. Continuous Monitoring: Population Stability Index (PSI) and Gini Tracking

Gig-economy behaviour and data-generating processes can change when platform rules, fuel costs, regulation, seasonality, or labour supply change. Annual validation alone may therefore miss material drift. Monitoring frequency should match feature volatility, decision materiality, and the institution's response capacity.

**The Population Stability Index (PSI)** is calculated daily to measure distributional shifts between the original training data and the live production inference data. The PSI quantifies how much the underlying population has shifted:
$$PSI = \sum_{b=1}^{B} (\text{Actual}\%_b - \text{Expected}\%_b) \times \ln\left(\frac{\text{Actual}\%_b}{\text{Expected}\%_b}\right)$$
Where $B$ represents the number of decile bins of the predicted probability score.

If input or score distributions shift, PSI may rise. The internal threshold of 0.25 triggers investigation, not an assumption about the cause and not automatic retraining. Controls may restrict affected decisions while data quality, calibration, discrimination, outcomes, and subgroup effects are reviewed.

**Discriminatory power:** Gini or AUC is monitored with calibration, Brier score, log loss, decision value, and realised outcomes. A value such as Gini below 0.35 can be an internal trigger; it is not labelled a universal regulatory minimum without an applicable source.

## 6.3. Algorithmic Fairness and Bias Mitigation

Predictive accuracy alone is not an adequate definition of a sound decision. A model can be well calibrated in aggregate and still allocate errors, limits, prices, or support unevenly. The governance objective is to identify unjustified disparities, proxy pathways, and product effects under applicable Kenyan law and partner policy, then redesign the system where a less harmful approach can achieve the legitimate objective.

The dual-regime neural architecture actively mitigates algorithmic bias through two stringent mechanisms:

### 6.3.1. Feature Orthogonalization and Blindness
Protected attributes are excluded from decision inputs unless lawfully needed for testing or an approved purpose, but "blindness" is not sufficient. Geography, device, platform, work schedule, vehicle, missingness, and wallet behaviour can retain proxy information. Adversarial probes, representation tests, conditional outcome analysis, calibration by group, and feature ablation estimate residual association. Zero mutual information is not promised.

### 6.3.2. Disparate Impact Ratio (DIR) Monitoring
Even with explicit blinding, complex neural models can reconstruct proxies. The governance layer continuously calculates the Disparate Impact Ratio across defined operational clusters. The DIR measures the ratio of favorable outcomes (e.g., micro-loan approval or a risk premium $K$ below a certain threshold) for an unprivileged group compared to a privileged group.

An approval-rate ratio such as 80% can be used as a diagnostic convention. The U.S. four-fifths rule is not imported as a Kenyan legal test, and a geographic corridor is not automatically a protected group. The analysis should cover legally and ethically relevant populations, intersectional groups, error rates, calibration, price, limits, interventions, and complaints.

An alert requires the accountable team to investigate data coverage, label quality, model pathways, policy rules, partner practices, and outcomes. SHAP may help locate model sensitivity, but it cannot prove the disparity is justified. Where a less harmful design achieves the legitimate objective with comparable performance, the design should be changed.

Explainability, model-risk management, and fairness testing create a body of evidence that can be challenged by drivers, partners, validators, auditors, and supervisors. That challengeability, rather than invulnerability to scrutiny, is the standard the platform should seek.

```{=latex}
\clearpage
```

## References

[1] A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin, *Bayesian Data Analysis*, 3rd ed. Boca Raton, FL, USA: CRC Press, 2013.

[2] F. Liu, Z. Hua, and A. Lim, “Identifying future defaulters: A hierarchical Bayesian method,” *European Journal of Operational Research*, vol. 241, no. 1, pp. 202-211, 2015, doi: 10.1016/j.ejor.2014.08.008.

[3] J. Piironen and A. Vehtari, “Sparsity information and regularization in the horseshoe and other shrinkage priors,” *Electronic Journal of Statistics*, vol. 11, no. 2, pp. 5018-5051, 2017, doi: 10.1214/17-EJS1337SI.

[4] P. K. Dunn and G. K. Smyth, “Randomized quantile residuals,” *Journal of Computational and Graphical Statistics*, vol. 5, no. 3, pp. 236-244, 1996, doi: 10.1080/10618600.1996.10474708.

[5] C. de Boor, *A Practical Guide to Splines*, rev. ed. New York, NY, USA: Springer, 2001, doi: 10.1007/978-1-4612-6333-3.

[6] H. Rue and L. Held, *Gaussian Markov Random Fields: Theory and Applications*. Boca Raton, FL, USA: Chapman & Hall/CRC, 2005, doi: 10.1201/9780203492024.

[7] A. Vehtari, A. Gelman, and J. Gabry, “Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC,” *Statistics and Computing*, vol. 27, pp. 1413-1432, 2017, doi: 10.1007/s11222-016-9696-4.

[8] A. Vehtari *et al*., “Rank-normalization, folding, and localization: An improved $\hat R$ for assessing convergence of MCMC,” *Bayesian Analysis*, vol. 16, no. 2, pp. 667-718, 2021, doi: 10.1214/20-BA1221.

[9] T. Gneiting and A. E. Raftery, “Strictly proper scoring rules, prediction, and estimation,” *Journal of the American Statistical Association*, vol. 102, no. 477, pp. 359-378, 2007, doi: 10.1198/016214506000001437.

[10] R. B. Nelsen, *An Introduction to Copulas*, 2nd ed. New York, NY, USA: Springer, 2006, doi: 10.1007/0-387-28678-0.

[11] C. Genest, B. Rémillard, and D. Beaudoin, “Goodness-of-fit tests for copulas: A review and a power study,” *Insurance: Mathematics and Economics*, vol. 44, no. 2, pp. 199-213, 2009, doi: 10.1016/j.insmatheco.2007.10.005.

[12] IFRS Foundation, *IFRS 9 Financial Instruments: Project Summary*, July 2014. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/project/fi-hedge-accounting/ifrs-standard/project-summary.pdf. Accessed: Aug. 25, 2026.

[13] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Nairobi, Kenya, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. Accessed: Aug. 25, 2026.

[14] Central Bank of Kenya, “Issuance of a Revised Risk-Based Credit Pricing Model,” press release, Aug. 26, 2025. [Online]. Available: https://www.centralbank.go.ke/uploads/press_releases/2044081907_Press%20Release%20-%20Issuance%20of%20a%20Revised%20Risk-Based%20Credit%20Pricing%20Model.pdf. Accessed: Aug. 25, 2026.

[15] Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency, *Supervisory Guidance on Model Risk Management*, SR Letter 11-7, Apr. 4, 2011. [Online]. Available: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm. Accessed: Aug. 25, 2026. Comparative guidance; not Kenyan law.

[16] A. Gelman, “Prior distributions for variance parameters in hierarchical models,” *Bayesian Analysis*, vol. 1, no. 3, pp. 515-534, 2006, doi: 10.1214/06-BA117A.

[17] C. M. Carvalho, N. G. Polson, and J. G. Scott, “The horseshoe estimator for sparse signals,” *Biometrika*, vol. 97, no. 2, pp. 465-480, 2010, doi: 10.1093/biomet/asq017.

[18] R. C. Merton, “On the pricing of corporate debt: The risk structure of interest rates,” *The Journal of Finance*, vol. 29, no. 2, pp. 449-470, 1974, doi: 10.1111/j.1540-6261.1974.tb03058.x.

[19] R. A. Jarrow and S. M. Turnbull, “Pricing derivatives on financial securities subject to credit risk,” *The Journal of Finance*, vol. 50, no. 1, pp. 53-85, 1995, doi: 10.1111/j.1540-6261.1995.tb05167.x.

[20] D. Duffie and K. J. Singleton, “Modeling term structures of defaultable bonds,” *The Review of Financial Studies*, vol. 12, no. 4, pp. 687-720, 1999, doi: 10.1093/rfs/12.4.687.

```{=latex}
\clearpage
```

# Appendix A: Underwriting Alternatives and the HLR Suitability Test

## A.1. Structural models as a boundary case

Structural credit models associated with Merton infer default from the relationship between an asset-value process and a debt boundary [18]. They remain important for corporate-credit valuation, but a gig driver and vehicle do not provide the same observable traded firm value or replicating structure. Earnings Velocity is an engineered liquidity feature rather than a market value for the driver-vehicle system, and platform blocks, vehicle failures, and settlement interruptions create discontinuities that a simple geometric diffusion may not represent well.

Part 5, Appendix A retains the structural equations in abridged form and explains how a physical-measure underwriting estimate can remain separate from a market-consistent valuation overlay. Here, the relevant conclusion is narrower: the HLR and structural models address different empirical objects, and the underwriting champion must be selected by calibration, stability, decision relevance, and validation rather than mathematical prestige.

## A.2. Reduced-Form Models and Intensity Processes

Recognizing the limitations of structural models, reduced-form (intensity-based) models treat default as an unpredictable Poisson jump process governed by a stochastic intensity (hazard rate) $\lambda_t$. The time of default $\tau$ is modeled as the first jump of a Cox process.

Under the $\mathbb{Q}$-measure, the price of a defaultable zero-coupon bond with maturity $T$ and zero recovery is:

$$P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T (r_s + \lambda_s) ds\right) \middle| \mathcal{F}_t\right]$$

Here, the credit spread is directly driven by the risk-neutral default intensity $\lambda_s$. In advanced implementations, $\lambda_t$ is modeled as an affine jump-diffusion (AJD) process (e.g., a Cox-Ingersoll-Ross process):

$$d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma_{\lambda} \sqrt{\lambda_t} dW_t^{\mathbb{Q}} + dJ_t$$

Reduced-form models do not require an observed firm value. Basic formulations treat default time through an intensity adapted to available information; richer intensities can include covariates. The comparison should therefore be empirical and use-case specific.

### A.2.1. The Exogenous Fallacy

For a ride-hailing driver, some defaults may be preceded by observable operating or liquidity changes; others arise from abrupt, unobserved, or genuinely exogenous events. The dual-regime architecture tests whether permitted sequences and explicit liquidity features improve warning time. Ten-hertz telematics does not prove determinism, and Earnings Velocity remains in the Explicit Liquidity Feature Path rather than the neural branch.

An intensity model and an HLR answer different questions. For short-duration underwriting with rich covariates, discrete-horizon real-world PD may be the more direct operational target. An intensity or market-consistent overlay can remain useful for valuation, survival analysis, or products whose timing and market inputs support it.

## A.3. The suitability test for the HLR approach

The HLR is preferred only when it produces stable, calibrated, decision-relevant real-world probabilities and transparent uncertainty at the product horizon.

1. **Direct PD estimation:** The HLR models physical default probability \(\mathbb P(\tau\le T)\) over a defined product horizon. No claim is made that \(\mathbb P\) and \(\mathbb Q\) become equal because the tenor is short.
2. **Empirical pricing input:** A simplified one-period break-even credit component may use \(k_{\mathrm{credit}}\approx PD^{\mathrm{cal}}LGD/(1-PD^{\mathrm{cal}})\). It does not guarantee realised loss coverage and is not the whole \(K_{\mathrm{RBCP}}\).
3. **Non-linear and hierarchical structure:** B-splines and cohort-time effects can represent real-world relationships without forcing them into a traded-asset diffusion, subject to the redundancy and calibration controls above.

The conclusion is one of scope, not mathematical taste. Use the HLR for calibrated physical-measure underwriting and portfolio decisions when it outperforms challengers. Use market-consistent methods only where valuation inputs and purpose justify them. Assemble \(K_{\mathrm{RBCP}}\) transparently from risk and non-risk components. The model supports the institution's pricing and governance process; it does not, by itself, establish regulatory compliance, computational efficiency, or fairness.
