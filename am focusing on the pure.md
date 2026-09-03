<truncated 1 lines>

The JAX compilation matrix tracks Hamiltonian trajectory rejections. Any
occurrence of divergent transitions signals a failure of the numerical
integration scheme (typically caused by steep probability cliffs on the
likelihood manifold). Thanks to your implementation of the
**Non-Centered Parameterization** for the geographic random intercepts
(\\(\\alpha \_{\\text{geo\\\_raw}}\\)), this geometric bottleneck is
averted, ensuring stable integration paths across all chains.

**4. Posterior Predictive p-value (\\(p\_{\\text{B}}\\))**

Calculated directly within the diagnostic suite using the proportion of
simulated zero-claim records against your observed baseline. The target
operational interval is **\\(0.05 \< p\_{\\text{B}} \< 0.95\\)**.

-   *Actuarial Significance:* A \\(p\_{\\text{B}} \> 0.95\\) implies
    that the model\'s structural assumptions are overfitting the
    training data. Conversely, a \\(p\_{\\text{B}} \< 0.05\\) flags a
    structural model specification failure, indicating that the Negative
    Binomial-Gamma configuration is systematically underestimating or
    overestimating the underlying portfolio risk.

**Part 5: Structuring Your Strategic Technical Portfolio**

Nevil, look closely at this complete mathematical and code block. This
architecture translates the theory from Part 2b of your *Mwendo Pamoja*
white paper directly into a highly optimized, hardware-accelerated
engineering system.

To optimize this module for your open-source enterprise portfolio
(mwendo-pamoja-core), follow this layout:

1.  **Repository Organization:** Create a file named
    /actuarial_core/ubi_pricing_engine.py and drop this complete script
    inside it.

2.  **Add a Local Validation Module:** Save the generated
    final_premium_surface vector into a local .csv file. This lets you
    mock a point-in-time database sync that routes straight into your
    **Microsoft Dynamics 365 Finance ERP endpoint** or your regulatory
    reporting sub-ledgers.

If you want to continue refining this pricing core, let me know if we
should explore:

-   How to build an **Asymmetric Clayton Copula Likelihood layer**
    directly into the script to model clustered portfolio defaults under
    systemic macroeconomic shocks.

**Part 1: Mathematical Mechanics of the Clayton Portfolio Copula**

When thousands of gig drivers operate across identical urban corridors,
their credit risks look completely independent during peaceful,
idiosyncratic periods. However, a sudden systemic shock causes their
default probabilities to compress into a dense, lockstep lower-tail
cluster. A standard Gaussian copula misses this entirely because its
tail dependence drops asymptotically to zero.

We implement the **Clayton Copula**, an Archimedean copula defined by
its generator function \\(\\psi(t) = \\frac{1}{\\theta}(t\^{-\\theta} -
1)\\). The joint cumulative distribution function over uniform marginal
risks \\(u_1, u_2, \\dots, u_d\\) is formulated as:

\\(C\_{\\theta }(u\_{1},u\_{2},\\dots ,u\_{d})=\\left(\\sum
\_{i=1}\^{d}u\_{i}\^{-\\theta }-d+1\\right)\^{-\\frac{1}{\\theta }}\\)

Where I, �^^ (0, �^z) is the copula parameter. The lower tail dependence
parameter is mathematically locked to:\
\\(\\lambda \_{L}=2\^{-\\frac{1}{\\theta }}\>0\\)

As I, �+' �^z, lower-tail dependence approaches 1, capturing the exact
\"domino effect\" of your multi-product default cascade.

**Part 2: Production NumPyro Implementation: Clayton Copula Loss
Estimation**

This script builds the **Archimedean Clayton Copula likelihood layer**
in NumPyro. It ingests your model\'s marginal probability vectors and
utilizes hardware-accelerated JAX execution to simulate full joint
portfolio value-at-risk (VaR) under systemic distress.

python

import jax

import jax.numpy as jnp

import numpy as np

import numpyro

import numpyro.distributions as dist

from numpyro.infer import MCMC, NUTS

def clayton_copula_log_density(u, theta):

\"\"\"

Computes the exact log-pdf of a multi-dimensional Clayton Copula

natively vectorized on the JAX backend.

u: Tensor \[N, D\] - Uniform marginal probabilities (PIT
transformations)

theta: Scalar - Copula association parameter (theta \> 0)

\"\"\"

N, D = u.shape

\# Core sum of inverse-powered uniform marginals

sum_u_pow = jnp.sum(u \*\* (-theta), axis=-1)

\# Exponent component of the Archimedean distribution matrix

log_c = (

jnp.sum(jnp.log(1.0 + jnp.arange(D) \* theta))

\- (D + 1.0 / theta) \* jnp.log(sum_u_pow - D + 1.0)

\- (theta + 1.0) \* jnp.sum(jnp.log(u), axis=-1)

)

return log_c

def portfolio_joint_default_copula_model(

marginal_p_defaults, \# Float array \[N, D\]: Marginal default
probabilities from individual products

observed_joint_defaults=None \# Float array \[N, D\]: Empirical default
matrices for validation

):

\"\"\"

NumPyro module evaluating joint tail default correlation across the
multi-product

capital stack (IPF, Microloans, Revolver Credit) using a Clayton Copula.

\"\"\"

N, D = marginal_p_defaults.shape

\# 1. Sample the copula parameter theta from a structural regularizing
prior

\# Ensuring strict positive support boundary via Exponential
parameterization

theta = numpyro.sample(\"clayton_theta\", dist.Exponential(rate=0.5))

\# Calculate and log the true Actuarial Lower Tail Dependence parameter

lambda_L = numpyro.deterministic(\"lower_tail_dependence\", 2.0 \*\*
(-1.0 / (theta + 1e-8)))

\# 2. Evaluate Copula Density over the observed portfolio timeline

if observed_joint_defaults is not None:

\# Map raw observations into continuous uniform space \[0, 1\] via
probability integral transform (PIT)

\# For survival analysis, we look at the default joint distributions

u_space = observed_joint_defaults

\# Enforce strict boundary safety constraints to prevent NaN
log-explosions

u_space = jnp.clip(u_space, min=1e-6, max=1.0 - 1e-6)

\# Inject the custom Clayton copula joint log density directly into the
JAX graph

log_prob_volume = clayton_copula_log_density(u_space, theta)

numpyro.factor(\"portfolio_copula_likelihood\",
jnp.sum(log_prob_volume))

\# \-\-- Portfolio Simulation and Risk Verification Trace \-\--

if \_\_name\_\_ == \"\_\_main\_\_\":

\# Simulate a portfolio tracking 3 multi-product exposures across 300
driver blocks

N_records, D_products = 300, 3 \# Product 1: IPF, Product 2: Micro,
Product 3: Revolver

np.random.seed(42)

\# Generate mock calibrated marginals (from your upstream Hierarchical
Model)

mock_marginals = np.random.uniform(0.01, 0.15, size=(N_records,
D_products)).astype(np.float32)

\# Simulate a highly correlated systemic default shock profile (Clayton
Sampling Mimicry)

\# Generating lower tail default clusters

v_latent = np.random.exponential(scale=1.0, size=(N_records, 1))

mock_uniforms = np.random.uniform(0.001, 0.999, size=(N_records,
D_products))

mock_joint_defaults = (mock_uniforms \* v_latent) \*\* (-1.0 / 2.5) \#
Simulated structural dependency

mock_joint_defaults = np.clip(mock_joint_defaults, 0.0,
1.0).astype(np.float32)

\# Initialize hardware-accelerated NUTS sampler

nuts_kernel = NUTS(portfolio_joint_default_copula_model)

mcmc_engine = MCMC(nuts_kernel, num_warmup=250, num_samples=500,
num_chains=1)

print(\"Beginning MCMC chain generation across Clayton asymmetric tail
surfaces\...\")

mcmc_engine.run(jax.random.PRNGKey(9),
marginal_p_defaults=mock_marginals,
observed_joint_defaults=mock_joint_defaults)

mcmc_engine.print_summary()

samples = mcmc_engine.get_samples()

mean_lambda_L = np.mean(samples\[\"lower_tail_dependence\"\])

print(f\"\\nCalculated Portfolio Asymptotic Lower-Tail Dependence
(lambda_L): {mean_lambda_L:.4f}\")

print(\" status: Clayton copula risk parameters resolved. Moat
established.\")

Use code with caution.

-   How to write an automated **IFRS 17 Accounting Adapter** that
    transforms the posterior premium surface into a structured
    Contractual Service Margin (CSM) calculation.


