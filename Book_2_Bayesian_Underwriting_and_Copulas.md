# Volume II: Advanced Bayesian Underwriting & Asymmetric Risk

## Executive Overview and Pedagogical Philosophy

Welcome to *Volume II: Advanced Bayesian Underwriting & Asymmetric Risk*, the definitive textbook for the modern actuarial syllabus. As the global economy increasingly shifts toward gig-economy structures, embedded finance, and high-frequency digital lending, the traditional deterministic tools of credit scoring and risk underwriting are proving structurally inadequate. The assumption of symmetric, normally distributed risks, independent identically distributed (i.i.d) defaults, and static macroeconomic environments has led to catastrophic portfolio failures. This textbook provides a rigorous, computationally grounded framework to replace these outdated paradigms with Continuous Underwriting via Hierarchical Bayesian Networks and Asymmetric Copulas.

This volume is designed not merely as a theoretical text, but as a comprehensive blueprint for building production-grade underwriting engines. We bridge the gap between abstract measure-theoretic probability, advanced Hamiltonian Monte Carlo (HMC) sampling geometry, and high-performance tensor computation using modern probabilistic programming languages such as `Pyro`, `NumPyro`, and `BlackJAX`. By the end of this text, the modern actuary will understand how to construct hierarchical models that borrow statistical strength across heterogeneous geographies, handle fat-tailed cash flow shocks, map non-linear covariates via autoregressive B-splines, and aggregate portfolio-level tail risk through asymmetric Archimedean copulas.

---

## 1. Literature Review: The Bayesian Renaissance in Actuarial Science

The foundation of our architectural choices rests upon decades of statistical research, which we synthesize here to contextualize the methods deployed throughout this volume. 

### 1.1 Gelman and the Critique of Inverse-Gamma Priors
For decades, the Inverse-Gamma distribution was the default conjugate prior for variance components in hierarchical models. However, as demonstrated by Andrew Gelman in his seminal 2006 paper, *Prior distributions for variance parameters in hierarchical models*, the Inverse-Gamma prior can be pathologically informative when the true variance is close to zero, pulling estimates away from zero and artificially inflating between-group variance. Gelman advocated for the use of the **Half-Cauchy** distribution as a weakly informative prior for scale parameters. The Half-Cauchy allows for heavy tails—accommodating occasional massive variance between clusters—while maintaining a finite peak at zero, permitting the model to collapse to complete pooling if the data does not support group-level heterogeneity.

### 1.2 Carvalho, Polson, and Scott: The Horseshoe and Heavy-Tailed Shrinkage
In high-dimensional covariate spaces—such as those produced by our neural embedding layers (e.g., GRU outputs)—we face the curse of dimensionality. Carvalho, Polson, and Scott (2010) introduced the **Horseshoe Prior**, a scale mixture of normals that achieves a delicate balance: infinite mass at zero to heavily penalize noise (driving irrelevant coefficients to exactly zero) and infinitely heavy, Cauchy-like tails to allow true signals to remain completely un-shrunk. This global-local shrinkage paradigm heavily influences our approach to modeling fat-tailed cash flow shocks and selecting regularizing priors for neural features.

### 1.3 AR(1) Splines and Non-Linear Smoothing
The transition from linear models to generalized additive models (GAMs) in Bayesian contexts relies heavily on basis functions. Lang and Brezger (2004) popularized the use of Bayesian P-splines, where the coefficients of adjacent B-spline basis functions are linked via random walk priors (RW1 or RW2) to enforce smoothness. In gig-economy cash flows, where out-of-distribution outliers are common, we extend this literature by employing **Autoregressive Order 1 (AR(1)) priors** on spline coefficients. This guarantees mean-reversion at the boundaries, preventing the catastrophic extrapolation typical of unregularized polynomials or standard random walks.

---

## 2. Chapter 1: The Foundations of Hierarchical Bayesian Modeling

### 2.1 From Deterministic Embeddings to Posterior Distributions
In traditional machine learning, a neural network maps a covariate vector to a deterministic probability estimate. While optimized for accuracy on a hold-out set, this approach strips away epistemic uncertainty. When a bank underwrites a gig worker in a newly launched geographic corridor, the model cannot simply predict a default probability of 5%; it must quantify its ignorance. 

Hierarchical Bayesian Logistic Regression (HBLR) elevates the deterministic neural embedding $\mathbf{\Phi}_{it}$ into an explicit posterior distribution over the default probability $\theta_{ijt}$. The foundational likelihood is:
$$Y_{ijt} \sim \text{Bernoulli}(\theta_{ijt})$$
$$\text{logit}(\theta_{ijt}) = \alpha_j + \boldsymbol{\beta}_j^T \mathbf{\Phi}_{it}$$

Through this formulation, the model generates full credible intervals. This uncertainty quantification directly drives the "Uncertainty Kill-Switch," a mechanism that automatically freezes credit line extensions when the 95th percentile of the posterior PD breaches regulatory limits, even if the mean PD remains acceptable.

### 2.2 The Partial Pooling Framework
The hierarchical structure addresses the "cold-start" problem in financial underwriting. Consider three approaches:
1. **Complete Pooling:** A single $\boldsymbol{\beta}$ is estimated for all drivers, ignoring structural differences between urban CBD drivers and peri-urban drivers.
2. **No Pooling:** Independent models for each cluster. For a new cluster with zero defaults in its first month, the maximum likelihood estimate for default is 0%, leading to massive over-leveraging.
3. **Partial Pooling (Hierarchical):** Cluster-specific parameters $\alpha_j, \boldsymbol{\beta}_j$ are drawn from a global portfolio distribution. Sparse clusters borrow statistical strength from the global mean, naturally shrinking their estimates toward the portfolio average.

### 2.3 Priors for Fat-Tailed Cash Flows: Half-Normal, Half-Cauchy, and Half-Student T
In gig-economy contexts, cash flows and risks are characterized by fat tails and heteroskedasticity. The choice of prior for the group-level standard deviation $\sigma_\alpha$ is critical. 

- **Half-Normal Prior:** $\sigma \sim \mathcal{HN}(s)$. The Half-Normal has light tails. It strongly regularizes the scale parameter toward zero. While computationally very stable and easy for HMC to sample, it is dangerously restrictive if the portfolio contains clusters with genuinely massive risk divergences (e.g., an economic collapse isolated to a single mining town).
- **Half-Cauchy Prior:** $\sigma \sim \mathcal{HC}(s)$. As recommended by Gelman, the Half-Cauchy's density $f(\sigma) \propto (1 + (\sigma/s)^2)^{-1}$ decays extremely slowly. It allows the model to learn large variances when necessary. However, its infinite variance can occasionally cause the HMC sampler to explore excessively large parameter spaces, leading to divergent transitions if not carefully parameterized.
- **Half-Student T Prior:** $\sigma \sim \text{Half-T}(\nu, 0, s)$. This is the gold-ilocks compromise. With degrees of freedom $\nu$ (typically between 3 and 7), the Half-Student T offers heavier tails than the Half-Normal but finite variance (for $\nu > 2$). It perfectly models the localized, extreme liquidity shocks of gig-workers, allowing for robust out-of-distribution anomalies without completely destabilizing the geometry of the posterior.

### 2.4 Escaping the Funnel: Non-Centered Parameterizations and LKJ Cholesky
A naive "centered" implementation of hierarchical models ($\alpha_j \sim \mathcal{N}(\mu, \sigma)$) induces Neal's Funnel. When $\sigma \to 0$, the $\alpha_j$ parameters are forced into an infinitesimally narrow region. The Hamiltonian Monte Carlo (HMC) leapfrog integrator, operating with a fixed step size, cannot navigate this extreme curvature, resulting in divergent transitions and biased inference.

We resolve this mathematically using the **Non-Centered Parameterization**:
$$\alpha_{j, \text{raw}} \sim \mathcal{N}(0, 1)$$
$$\alpha_j = \mu + \alpha_{j, \text{raw}} \cdot \sigma$$

This transforms the prior geometry into a perfectly isotropic standard multivariate normal space, completely decoupling the hierarchical variance from the random effects during the sampling phase.

Furthermore, for multivariate slopes, we avoid Inverse-Wishart priors, which impose symmetric constraints on variances and correlations. Instead, we decompose the covariance matrix using the **LKJ Cholesky Decomposition**:
$$\boldsymbol{\Sigma} = \mathbf{D} \mathbf{L} \mathbf{L}^T \mathbf{D}$$
Where $\mathbf{D}$ is a diagonal matrix of Half-Student T scale parameters, and $\mathbf{L}$ is the Cholesky factor of a correlation matrix governed by the LKJ prior. This separates the modeling of variances (volatility) from correlations (structural dependency), allowing HMC to efficiently explore the manifold.

---

## 3. Chapter 2: Nonlinear Functional Forms and Basis Expansions

Credit risk variables almost never exhibit strict log-linear relationships with the probability of default. Consider the Debt-to-Liquidity Ratio (DLR) or a driver's tenure on the platform. Risk declines steeply in the first 90 days of tenure as drivers learn the platform's kinematics, then plateaus. A naive linear term $\beta \times \text{Tenure}$ implies risk decreases forever, eventually resulting in zero probability of default, which is absurd. 

### 3.1 The Limitations of Binning and Step Functions
The industry-standard response to nonlinearity is **binning**—converting continuous variables into discrete buckets (e.g., Age 18-25, 26-35, etc.). 

**Limitations of Binning:**
1. **Piecewise Constant Approximations:** Binning forces the risk model to assume that a 25.9-year-old and an 18-year-old possess the exact same baseline risk, while a 26.0-year-old is treated as fundamentally different. This introduces artificial step-function discontinuities.
2. **Boundary Collapse:** If a specific bin contains zero defaults (due to small sample size), the maximum likelihood log-odds estimate diverges to $-\infty$. 
3. **Equivalence to Tree-Based Models:** Mathematically, binning maps continuous variables to orthogonal indicator functions. This is strictly equivalent to the splits performed by Random Forests or XGBoost. While trees are powerful, their piecewise-constant nature limits their use in regulated credit models where smoothness, monotonicity, and continuous derivatives are mandated for stress-testing and economic interpretation.

### 3.2 B-Splines: Mathematical Foundations and AR(1) Smoothing
To resolve the pathologies of binning, we deploy **B-Splines** (Basis Splines). A B-spline maps a continuous variable $x$ into a high-dimensional space using a set of $K$ continuous, overlapping basis functions $B_k(x)$. The predictor becomes a linear combination:
$$f(x) = \sum_{k=1}^K \zeta_k B_k(x)$$

This guarantees continuous derivatives and a smooth topology. However, if unconstrained, a high-degree spline will violently overfit noise, oscillating wildly between knots.

We regularize this using an **Autoregressive Order 1 (AR(1)) Prior** on the spline coefficients $\zeta_k$:
$$\zeta_k \sim \mathcal{N}(\rho \zeta_{k-1}, \sigma_\zeta^2)$$

Because the mean-reversion parameter $|\rho| < 1$, as the variable moves into unobserved out-of-distribution (OOD) territory (e.g., an unprecedented spike in earnings velocity), the coefficients exponentially decay back toward zero. This acts as a mathematical kill-switch, pulling extrapolations safely back to the global intercept, preventing the catastrophic blow-ups typical of unregularized deep learning models.

---

## 4. Chapter 3: Dynamic Coefficients and Macroeconomic Embedding

Under the IFRS 9 accounting standard, Expected Credit Loss (ECL) models must incorporate forward-looking macroeconomic scenarios. A static logistic regression trained on data from 2021 to 2023 will systematically misprice risk in 2026 if fuel prices double or inflation spikes.

To solve this, our Bayesian architecture models the macroeconomic sensitivities $\boldsymbol{\delta}$ as time-varying parameters governed by AR(1) processes:
$$\delta_{k,t} \sim \mathcal{N}\left(\mu_k + \rho_k(\delta_{k,t-1} - \mu_k),\, \sigma_{\delta_k}^2\right)$$

This allows the model's sensitivity to factors like gas prices and ZEV (Zero Emission Vehicle) mandate tiers to evolve dynamically as macroeconomic regimes shift. By maintaining a stationary AR(1) prior rather than a non-stationary Random Walk (RW1), we ensure that the coefficients eventually mean-revert to historical averages in the absence of new, disruptive data, providing crucial stability for long-term capital forecasting.

---

## 5. Chapter 4: Copulas and Asymmetric Tail Risk

The Hierarchical Bayesian engine produces exceptional marginal distributions for the PD of individual products (e.g., Microloans, Revolving Credit, Insurance Premium Financing). However, banks hold these products simultaneously. The true portfolio risk is the joint probability of simultaneous default across all products.

### 5.1 The Failure of the Gaussian Copula
Historically, risk managers used the Gaussian Copula to bind marginal distributions together. The Gaussian Copula assumes symmetric tail dependence. It implies that if drivers default together during a crisis, they must also over-perform together during a boom. This is empirically false in gig-economy portfolios. Systemic shocks (e.g., algorithmic platform lockouts, regional fuel strikes) cause massive, lockstep defaults (lower tail dependence), but boom periods show highly diversified, uncorrelated outperformance (zero upper tail dependence).

### 5.2 Sklar's Theorem and the Clayton Copula
Sklar's Theorem allows us to decompose any multivariate distribution into its marginals and a dependency structure (the copula):
$$F(t^{\text{micro}}, t^{\text{revol}}, t^{\text{IPF}}) = C\left(F_1(t^{\text{micro}}), F_2(t^{\text{revol}}), F_3(t^{\text{IPF}});\, \alpha_c\right)$$

We replace the Gaussian Copula with the **Clayton Copula**, an Archimedean copula parameterized by $\alpha_c > 0$. Its lower tail dependence coefficient is:
$$\lambda_L = 2^{-1/\alpha_c}$$
Crucially, its upper tail dependence $\lambda_U = 0$. 

As macroeconomic shocks increase the severity parameter $\alpha_c$, $\lambda_L \to 1.0$. This mathematically formalizes the default contagion cascade. By coupling Bayesian MCMC marginals with a Clayton Copula, we simulate joint portfolio losses that accurately reflect the non-linear spikes in Unexpected Loss (UL) during stress scenarios—a capability directly necessary for Basel IV capital adequacy compliance.

---

## 6. Chapter 5: Computational Implementation in Pyro and JAX

Theory must be instantiated in code. In this section, we provide expansive, deeply commented implementations of the aforementioned architectures. We begin with `Pyro` (built on PyTorch) for its flexibility in defining deep probabilistic models, and follow with `NumPyro`/`BlackJAX` (built on JAX) for XLA-compiled, GPU-accelerated Hamiltonian Monte Carlo needed for production-scale portfolios.

### 6.1 Pyro Implementation: Hierarchical Bayesian Logistic Regression with B-Splines

The following `Pyro` code implements a hierarchical logistic regression model. It includes non-centered parameterization, a Half-Student T prior for scale, and an AR(1) prior over B-spline coefficients for a continuous covariate (e.g., Driver Tenure).

```python
import torch
import pyro
import pyro.distributions as dist
from pyro.infer import MCMC, NUTS
import torch.nn.functional as F

def b_spline_basis(x, knots, degree=3):
    """
    Constructs a B-spline basis matrix for continuous covariate x.
    In a production system, this would use scipy.interpolate.BSpline
    pre-computed and passed as a tensor.
    """
    # Placeholder for B-spline matrix generation
    # Assume it returns a tensor of shape [N, num_basis_funcs]
    pass

def pyro_hierarchical_underwriting_model(
    cluster_ids,         # Tensor of shape [N], containing integer cluster IDs (0 to J-1)
    dense_features,      # Tensor of shape [N, D], e.g., GRU embeddings
    spline_basis,        # Tensor of shape [N, K], evaluated B-spline basis functions
    outcomes=None,       # Tensor of shape [N], binary default indicators {0, 1}
    num_clusters=10, 
    num_basis=8
):
    """
    Pyro model for Advanced Bayesian Underwriting.
    Incorporates:
    - Non-centered hierarchical intercepts
    - Half-Student T priors for robust scale estimation
    - AR(1) smoothing for B-spline basis coefficients
    """
    D = dense_features.shape[1]
    
    # ---------------------------------------------------------
    # 1. Global Hyperpriors
    # ---------------------------------------------------------
    # Mean of the global intercept
    mu_alpha = pyro.sample("mu_alpha", dist.Normal(0.0, 2.0))
    
    # Scale of the hierarchical intercepts using a robust Half-Student T prior
    # Degrees of freedom = 4 allows for heavy tails (fat-tailed cash flow shocks)
    sigma_alpha = pyro.sample("sigma_alpha", dist.StudentT(df=4.0, loc=0.0, scale=1.0))
    # Constrain to positive domain (Half-T)
    sigma_alpha = torch.abs(sigma_alpha)
    
    # ---------------------------------------------------------
    # 2. Non-Centered Hierarchical Intercepts
    # ---------------------------------------------------------
    # Sample raw, standard normal variables to avoid Neal's Funnel
    with pyro.plate("cluster_plate", num_clusters):
        alpha_raw = pyro.sample("alpha_raw", dist.Normal(0.0, 1.0))
        
    # Deterministic transformation to the true hierarchical intercept
    alpha = mu_alpha + alpha_raw * sigma_alpha
    
    # ---------------------------------------------------------
    # 3. Global Dense Feature Coefficients
    # ---------------------------------------------------------
    # Standard normal priors for GRU embeddings. In practice, a Horseshoe prior 
    # could be placed here for high-dimensional sparsity.
    with pyro.plate("features_plate", D):
        beta = pyro.sample("beta", dist.Normal(0.0, 1.0))
        
    # ---------------------------------------------------------
    # 4. AR(1) Smoothed B-Spline Coefficients
    # ---------------------------------------------------------
    # The AR(1) persistence parameter, bound between -1 and 1
    # We use a Beta prior mapped to (-1, 1) to encourage smoothness (positive correlation)
    rho_raw = pyro.sample("rho_raw", dist.Beta(8.0, 2.0)) 
    rho = rho_raw * 2.0 - 1.0
    
    # Innovation variance for the spline coefficients
    sigma_zeta = pyro.sample("sigma_zeta", dist.HalfCauchy(1.0))
    
    # Sample the spline coefficients autoregressively
    zeta = [pyro.sample("zeta_0", dist.Normal(0.0, sigma_zeta))]
    for k in range(1, num_basis):
        # Each coefficient depends on the previous one, shrinking toward 0 at boundaries
        mean_k = rho * zeta[k-1]
        zeta_k = pyro.sample(f"zeta_{k}", dist.Normal(mean_k, sigma_zeta))
        zeta.append(zeta_k)
        
    zeta_tensor = torch.stack(zeta)
    
    # ---------------------------------------------------------
    # 5. Likelihood Construction
    # ---------------------------------------------------------
    # Gather the specific intercept for each driver based on their cluster_id
    driver_alpha = alpha[cluster_ids]
    
    # Linear predictor from dense neural features
    linear_embed = torch.matmul(dense_features, beta)
    
    # Non-linear spline predictor
    spline_effect = torch.matmul(spline_basis, zeta_tensor)
    
    # Total Log-Odds
    logit_theta = driver_alpha + linear_embed + spline_effect
    
    # Map to probabilities and sample the Bernoulli likelihood
    with pyro.plate("data_plate", len(cluster_ids)):
        pyro.sample("obs", dist.Bernoulli(logits=logit_theta), obs=outcomes)

# To run inference:
# nuts_kernel = NUTS(pyro_hierarchical_underwriting_model)
# mcmc = MCMC(nuts_kernel, num_samples=1000, warmup_steps=500)
# mcmc.run(cluster_ids, dense_features, spline_basis, outcomes, num_clusters=10, num_basis=8)
```

### 6.3 NumPyro and BlackJAX Implementation: High-Performance GPU Inference

While `Pyro` is incredibly expressive, `NumPyro` leverages JAX for Just-In-Time (JIT) compilation to XLA, enabling execution on GPUs and TPUs. This is strictly required when scaling to portfolios with hundreds of thousands of active drivers. Here, we implement a binomial-aggregated model with an LKJ Cholesky prior for multivariate hierarchical slopes.

```python
import jax
import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS

def numpyro_binomial_copula_model(
    cluster_ids,     # Array [G], group cluster IDs
    dense_features,  # Array [G, D], aggregated group features
    trials,          # Array [G], n_g drivers in this aggregated group
    defaults=None,   # Array [G], k_g defaults observed
    num_clusters=10,
    D=5
):
    """
    NumPyro implementation for GPU-accelerated Binomial aggregation.
    Features:
    - LKJ Cholesky Decomposition for multivariate cluster effects
    - Binomial likelihood for O(G) vs O(N) scaling
    - JAX XLA compatibility
    """
    G = cluster_ids.shape[0]
    
    # ---------------------------------------------------------
    # 1. LKJ Cholesky Decomposition for Covariance
    # ---------------------------------------------------------
    # We want a hierarchical intercept AND hierarchical slopes for all D features.
    # Total hierarchical parameters per cluster = 1 + D.
    K = 1 + D
    
    # Global means for intercept and slopes
    mu = numpyro.sample("mu", dist.Normal(0.0, 2.0).expand([K]))
    
    # Half-Cauchy priors for the scale (variance) of each of the K parameters
    sigma = numpyro.sample("sigma", dist.HalfCauchy(1.0).expand([K]))
    
    # LKJ Prior on the Cholesky factor of the correlation matrix.
    # concentration=2.0 pushes correlations slightly towards zero, regularizing the matrix.
    L_corr = numpyro.sample("L_corr", dist.LKJCholesky(dimension=K, concentration=2.0))
    
    # Create the Cholesky factor of the covariance matrix: L_cov = diag(sigma) * L_corr
    L_cov = jnp.matmul(jnp.diag(sigma), L_corr)
    
    # ---------------------------------------------------------
    # 2. Non-Centered Sampling of Multivariate Cluster Effects
    # ---------------------------------------------------------
    # Sample raw standard normal vectors for each cluster
    with numpyro.plate("cluster_plate", num_clusters):
        # Shape: [num_clusters, K]
        cluster_effects_raw = numpyro.sample("cluster_effects_raw", dist.Normal(0.0, 1.0).expand([K]))
        
    # Deterministic rotation and scaling to induce correlation and variance
    # delta = mu + L_cov * raw
    # We use jax.vmap or simple matrix math
    cluster_effects = mu + jnp.matmul(cluster_effects_raw, L_cov.T)
    
    # Extract intercepts (first column) and slopes (remaining columns)
    alpha = cluster_effects[:, 0]
    beta = cluster_effects[:, 1:]
    
    # ---------------------------------------------------------
    # 3. Aggregated Binomial Likelihood
    # ---------------------------------------------------------
    # Extract specific parameters for each aggregated group
    group_alpha = alpha[cluster_ids]
    group_beta = beta[cluster_ids]
    
    # Compute dot product of features and slopes for each group
    # group_beta is [G, D], dense_features is [G, D]
    linear_embed = jnp.sum(group_beta * dense_features, axis=-1)
    
    # Logit calculation
    logit_theta = group_alpha + linear_embed
    
    # Binomial Likelihood. Drastically faster than Bernoulli for large datasets.
    with numpyro.plate("data_plate", G):
        numpyro.sample("obs", dist.Binomial(total_count=trials, logits=logit_theta), obs=defaults)

# Inference execution (Compiles to XLA for GPU)
# nuts_kernel = NUTS(numpyro_binomial_copula_model, target_accept_prob=0.95)
# mcmc = MCMC(nuts_kernel, num_warmup=1000, num_samples=2000, num_chains=4)
# mcmc.run(jax.random.PRNGKey(0), cluster_ids, dense_features, trials, defaults, num_clusters=10, D=5)
```

By leveraging `NumPyro` and JAX, we calculate gradients over millions of parameters instantly via automatic differentiation across accelerated tensor cores. This permits the modeling of extreme asymmetric tail risks and fat-tailed shocks without sacrificing the mathematical integrity necessary for Basel IV model validation.

---
## Conclusion

This text has fundamentally deconstructed the determinism of traditional underwriting. By fusing neural embeddings with Hierarchical Bayesian networks, utilizing robust Half-Student T priors for heavy-tailed phenomena, regularizing continuous features with AR(1) B-splines, and binding joint risk through the Clayton Copula, we provide a mathematically uncompromising blueprint for the modern Insurtech risk engine. As gig-worker economies continue to exhibit asymmetric, cascading tail risks, the methodologies encoded in this volume represent the standard by which all future regulatory and financial credit models will be judged.
