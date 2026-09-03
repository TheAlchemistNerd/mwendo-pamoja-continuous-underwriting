hierarchical negative binomial gamma for usage based insurance motor

premium pricing



A hierarchical negative binomial-gamma model structures usage-based

insurance (UBI) pricing by decomposing risk into driver-specific claim

frequencies (using a Negative Binomial distribution for overdispersed

telematics counts) and claim severities (using a Gamma distribution). 



MDPI



**Core Architecture**



-   **Claim Frequency (Level 1 - Count):** Models the number of claims 



>  for driver i during time period j, conditional on a latent risk

> factor 

>

> , often via a Negative Binomial or Poisson-gamma framework to handle

> unobserved heterogeneity and overdispersion from telematics data. 

>

> Springer Nature Link +2



-   **Driving Behavior Covariates (Level 2 - Exposure):** Incorporates

    dynamic telematics variables---such as total kilometers driven,

    percentage of driving on high-risk motorways, harsh braking

    frequency, and rapid acceleration---as offsets or linear

    predictors. 



-   **Claim Severity (Level 3 - Continuous):** Models the conditional

    cost 



>  of a claim given that a claim has occurred, using a Gamma

> distribution linked to driver behavior and vehicle attributes. 

>

> MDPI +1



-   **Hierarchical / Random Effects:** Uses driver-level random effects

    (



> ) to implement a continuous Bayesian updating scheme (dynamic

> Bonus-Malus system) that updates the pure premium as real-time driving

> data accumulates. 

>

> ArmgPublishing +1



If you\'d like, let me know:



-   Are you focusing on **frequency modeling** or the **full pure

    premium (frequency × severity)**?



-   Do you have access to **high-frequency telematics streams** (e.g.,

    second-by-second GPS) or **aggregated summary metrics** (e.g.,

    monthly mileage/harsh events)?



I can provide specific **model formulation equations** or

an **implementation outline in R or Python**.



-   



> ScienceDirect.com

>

> Hierarchical generalized linear models, correlation and a posteriori

> ratemaking

>

> Hierarchical generalized linear models (HGLM) applied to car insurance

> pricing are investigated. •. The Poisson-gamma HGLM and the\...



-   



> MDPI

>

> A Logistic Regression Based Auto Insurance Rate-Making Model \...

>

> This section is implemented using the GENMOD program in SAS software.

> In this article, two different distributions are used to fig\...

>

> 



-   



> Springer Nature Link

>

> Regional risk classification in emerging automobile insurance markets

> using \...

>

> Article summary. \... Accurate risk classification in automobile

> insurance is crucial for effective actuarial practice, especially \...

>

> 



Show all



Are you focusing on frequency modeling or the full pure premium

(frequency × severity)?pure premiumDo you have access to high-frequency

telematics streams (e.g., second-by-second GPS) or aggregated summary

metrics (e.g., monthly mileage/harsh events)? high frequency telematics



The pure premium is modeled by combining a Hierarchical Negative

Binomial distribution for claim frequency with a Gamma distribution for

claim severity. High-frequency telematics data (second-by-second

GPS/accelerometer) is first aggregated into driver-level risk profiles

to feed this structure.



**1. Mathematical Formulation**



The pure premium for driver i at time period j is defined as:



**Frequency Component: Hierarchical Negative Binomial**



To account for overdispersion and unobserved driver heterogeneity, claim

counts 



 follow a Poisson distribution conditioned on a random effect 



:



-   



> : Exposure baseline (e.g., policy duration or baseline distance).



-   



> : Latent driver risk profile, where 

>

> . This formulation integrates out to a Negative Binomial distribution.



-   



> : Log-linear predictor containing high-frequency telematics risk

> features 

>

> :



**Severity Component: Hierarchical Gamma**



The cost of an individual claim 



 (for claim k of driver i in period j) follows a Gamma distribution:



-   **φ**: Shape parameter handling the heavy-tailed nature of insurance

    losses.



-   



> : Driver-specific severity random effect, where 

>

> .



-   



> : Scale predictor linked to driving risk metrics 

>

>  and vehicle specs:



**2. Feature Engineering from High-Frequency Streams**



Second-by-second telematics streams must be processed into summary

covariates (



 and 



) before model fitting:



-   **Kinematic Thresholding:** Extract the frequency of jerk events

    (rate of change of acceleration) exceeding ± 3.0 m/s³ to isolate

    aggressive lane changes or hard braking.



-   **Contextual Risk Profiles:** Cross-reference GPS coordinates with

    digital maps to compute the ratio of nighttime driving (22:00 -

    04:00) and urban vs. highway mileage.



-   **Speed Volatility:** Calculate the rolling standard deviation of

    speed over 10-second intervals to capture erratic pace keeping.



**3. Python Implementation Outline**



This script uses pymc to estimate the joint frequency-severity model

using Bayesian Markov Chain Monte Carlo (MCMC).



python



import pymc as pm



import numpy as np



*\# Sample Data Dimensions*



num_drivers = 500



num_periods = 12 *\# e.g., monthly observations*



*\# Dummy data placeholder: telematics features and exposures*



X_telematics = np.random.randn(num_drivers, num_periods) *\# e.g., Harsh

braking rate*



Z_telematics = np.random.randn(num_drivers, num_periods) *\# e.g., Night

driving ratio*



exposure = np.ones((num_drivers, num_periods)) *\# Exposure time*



driver_idx = np.repeat(np.arange(num_drivers), num_periods)



*\# Flatten data for PyMC*



X_flat = X_telematics.flatten()



Z_flat = Z_telematics.flatten()



exp_flat = exposure.flatten()



*\# Observed claims and costs (simulated)*



observed_counts = np.random.poisson(0.1, size=num_drivers \*

num_periods)



observed_severities = np.random.gamma(2.0, 500.0, size=num_drivers \*

num_periods)



*\# Mask severities where no claim occurred*



observed_severities\[observed_counts == 0\] = np.nan



with pm.Model() as ubi_model:



*\# \-\-- FREQUENCY PRIORS \-\--*



alpha = pm.Exponential(\"alpha\", lam=1.0)



theta = pm.Gamma(\"theta\", alpha=alpha, beta=alpha, shape=num_drivers)



beta_0 = pm.Normal(\"beta_0\", mu=0, sigma=2)



beta_1 = pm.Normal(\"beta_1\", mu=0, sigma=1)



*\# Frequency Likelihood*



mu = pm.math.exp(beta_0 + beta_1 \* X_flat)



lambda_freq = mu \* theta\[driver_idx\] \* exp_flat



y_freq = pm.Poisson(\"y_freq\", mu=lambda_freq,

observed=observed_counts)



*\# \-\-- SEVERITY PRIORS \-\--*



phi = pm.Exponential(\"phi\", lam=0.1)



nu = pm.Exponential(\"nu\", lam=1.0)



omega = pm.InverseGamma(\"omega\", alpha=nu, beta=nu, shape=num_drivers)



gamma_0 = pm.Normal(\"gamma_0\", mu=6, sigma=2) *\# log scale*



gamma_1 = pm.Normal(\"gamma_1\", mu=0, sigma=1)



*\# Severity Likelihood (evaluated only where claims \> 0)*



claim_mask = observed_counts \> 0



lambda_sev = pm.math.exp(gamma_0 + gamma_1 \* Z_flat\[claim_mask\]) \*

omega\[driver_idx\[claim_mask\]\]



y_sev = pm.Gamma(



\"y_sev\",



alpha=phi,



beta=phi / lambda_sev,



observed=observed_severities\[claim_mask\]



)



*\# \-\-- MCMC Sampling \-\--*



trace = pm.sample(draws=1000, tune=1000, return_inferencedata=True)



Use code with caution.



If you are ready to build this out, would you like to explore **how to

update the random effects (**



**) in real time** as new telematics data rolls in, or look closer at

the **kinematic algorithms for feature extraction**?



Using GRU for feature extraction and neural residualisation



Using Gated Recurrent Units (GRUs) for feature extraction allows you to

ingest raw, second-by-second telematics time series directly,

eliminating manual thresholding. Neural residualization ensures that the

deep telematics features remain strictly orthogonal to traditional

actuarial risk factors (like age, region, or vehicle power), protecting

the model from double-counting risk and maintaining regulatory

transparency.



**1. Architectural Pipeline**



The framework operates in three sequential layers:



1.  **The GRU Sequence Encoder:** Processes a variable-length window of

    second-by-second telematics inputs (speed, acceleration, angular

    velocity) into a fixed-size behavioral embedding vector 



> .



2.  **The Actuarial Residualization Layer:** Projects the deep

    behavioral embedding into a residual space by regressing out the

    influence of traditional pricing covariates.



3.  **The GLM Core (Frequency & Severity):** Combines the traditional

    features and the orthogonalized telematics residuals inside the

    Hierarchical Negative Binomial-Gamma framework.



\[Raw 1Hz Telematics Data\] ──\> \[ GRU Encoder \] ──\> \[ Embedding (h)

\]



│



\[Traditional Covariates (X)\] ────────────────────────────┼──\> \[

Linear Projection \]



│ │



▼ ▼



\[ Residualization: h - h_hat \]



│



▼



\[ Pure Premium Estimation \]



(NegBin Frequency / Gamma Severity)



**2. Mathematical Formulation of Neural Residualization**



Let 



 be the vector of traditional socio-demographic and vehicle risk factors

for driver i in period j. Let 



 be the raw embedding generated by the GRU network from the telematics

time series.



To isolate pure behavioral risk that cannot be explained by traditional

variables, we fit a projection mapping 



---typically a multi-layer perceptron or a regularized linear

projection---to predict the embedding 



:



The **telematics residual** 



 is defined as:



By construction, 



 captures variations in driving behavior that are strictly uncorrelated

with traditional factors. The log-linear predictors for frequency (



) and severity (



) are then structured as:



This prevents the GRU from inadvertently proxies for protected

attributes (e.g., inferring a driver\'s age group from acceleration

patterns) which could violate insurance compliance laws.



**3. PyTorch Implementation Pipeline**



This implementation defines the GRU encoder, executes the

residualization step, and outputs the components needed for the

hierarchical GLM.



python



import torch



import torch.nn as nn



class TelematicsResidualPricingNet(nn.Module):



def \_\_init\_\_(self, num_telematics_features, gru_hidden_dim,

num_traditional_features):



super(TelematicsResidualPricingNet, self).\_\_init\_\_()



*\# 1. GRU Sequential Encoder*



self.gru = nn.GRU(



input_size=num_telematics_features,



hidden_size=gru_hidden_dim,



num_layers=2,



batch_first=True,



dropout=0.2



)



*\# 2. Residualization Network (Projects traditional features to

embedding space)*



self.residual_projector = nn.Sequential(



nn.Linear(num_traditional_features, gru_hidden_dim \* 2),



nn.ReLU(),



nn.Linear(gru_hidden_dim \* 2, gru_hidden_dim)



)



*\# 3. Output Pricing Layers (GLM Links)*



self.frequency_link = nn.Linear(num_traditional_features +

gru_hidden_dim, 1)



self.severity_link = nn.Linear(num_traditional_features +

gru_hidden_dim, 1)



def forward(self, telematics_seq, traditional_feats):



*\# Extract behavioral embedding from the last GRU hidden state*



gru_out, h_n = self.gru(telematics_seq)



h_behavior = h_n\[-1\] *\# Shape: \[batch_size, gru_hidden_dim\]*



*\# Predict the behavior embedding using traditional features*



h_predicted = self.residual_projector(traditional_feats)



*\# Calculate the orthogonalized telematics residual*



h_residual = h_behavior - h_predicted



*\# Combine traditional features with orthogonalized behavior residuals*



combined_features = torch.cat((traditional_feats, h_residual), dim=1)



*\# Output log-linear linear predictors for the hierarchical layers*



log_mu = self.frequency_link(combined_features)



log_lambda = self.severity_link(combined_features)



return log_mu, log_lambda, h_residual



Use code with caution.



**4. Two-Stage vs. Joint Optimization Training**



When deploying this model, you can choose between two training

paradigms:



-   **Two-Stage Estimation (Actuarial Standard):** First, fit a standard

    Poisson/Gamma GLM on traditional features. Second, train the GRU to

    predict the residuals of that GLM. This guarantees that traditional

    tariffs remain completely unchanged and readable, while the GRU only

    calculates a dynamic discount/loading factor.



-   **End-to-End Joint Estimation:** Minimize a custom loss function

    combining the Negative Binomial log-likelihood, Gamma

    log-likelihood, and an explicit penalty term (like Maximum Mean

    Discrepancy or a covariance penalty) to force dependency between 



>  and 

>

>  to zero.



If you want to move to the execution phase, let me know:



-   Do you prefer a **Two-Stage training approach** to keep the core

    pricing structure separate, or an **End-to-End joint optimization**?



-   Would you like to review the **loss function equations** required to

    train this directly on combined count and cost insurance data?



how to update the random effects (\\(\\theta_i, \\Omega_i\\)) in real

time



To update driver-specific random effects (



 for frequency, 



 for severity) in real time without retraining the deep learning network

or re-running MCMC chains, you must leverage **Conjugate Bayesian

Updating**.



Because the Negative Binomial maps to a Poisson-Gamma mixture and the

Hierarchical Severity model maps to a Gamma-Inverse Gamma mixture, the

posterior distribution updates instantly using simple algebraic addition

as new driving data streams in.



**1. Dynamic Frequency Update (**



**)**



The latent risk factor 



 acts as a multiplier on the driver\'s baseline expected claim

frequency.



**Mathematical Conjugacy**



-   **Prior:** 



>  with mean = 1 and variance = 

>

> .



-   **New Streaming Data:** Over a new streaming period, the driver

    accumulates exposure 



>  (e.g., fractional year or 1,000 km) and records 

>

>  claims.



-   **Model Baseline:** Let 



>  be the neural-residualized baseline frequency.



The closed-form posterior update for the shape and rate parameters is:



**Real-Time Credibility Factor**



The updated point estimate for the driver's frequency random effect

becomes:



-   **If a driver has zero claims (**



> **):** As exposure 

>

>  increases, the denominator grows, dropping 

>

>  below 1.0, automatically generating a real-time safe-driving premium

> discount.



**2. Dynamic Severity Update (**



**)**



The severity random effect 



 scales the expected cost per claim based on observed individual loss

behaviors.



**Mathematical Conjugacy**



-   **Prior:** 



>  with mean = 

>

> .



-   **New Streaming Data:** The driver experiences 



>  claims during the streaming window, with individual claim costs 

>

> .



-   **Model Baseline:** Let 



>  be the neural-residualized expected cost, and 

>

>  be the Gamma shape parameter.



The closed-form posterior update for the Inverse-Gamma parameters is:



**Real-Time Credibility Factor**



The updated point estimate for the driver\'s severity random effect

becomes:



-   **If no claims occur:** 



>  does not change, meaning severity profiles are only modified when

> physical loss events take place.



**3. Production Stream Architecture**



In a production telematics pipeline, updates are executed in a

dual-velocity architecture (Lambda Architecture):



┌──────────────────────────────┐



│ Raw 1Hz Telematics Stream │



└──────────────┬───────────────┘



│



▼



┌──────────────────────────────┐



│ Real-Time Feature Engine │



│ (GRU Forward Pass via Kafka) │



└──────────────┬───────────────┘



│ Output: h_residual



▼



┌──────────────────────────────┐



│ Micro-Batch Baseline Calc │



│ Compute μ_ij and Λ_ij │



└──────────────┬───────────────┘



│



┌────────────────────────┴────────────────────────┐



▼ ▼



┌──────────────────────────┐ ┌──────────────────────────┐



│ Frequency Update (Daily) │ │ Severity Update (Event) │



│ ΔN_i: Claims in window │ │ Y_ik: Cost of new claim │



│ ΔE_i: Distance in window │ │ Update rule: │



│ Update rule: │ │ ν_scale += φ\*Y / Λ │



│ β_new += μ_ij \* ΔE │ │ ν_shape += φ │



└────────────┬─────────────┘ └────────────┬─────────────┘



│ │



└────────────────────────┬────────────────────────┘



▼



┌──────────────────────────────┐



│ Dynamic Pure Premium │



│ E\[N\] \* E\[Y\] \* θ_new \* Ω_new │



└──────────────────────────────┘



**4. Production Python Update Function**



This production-ready block implements the algebraic updates on top of

the saved static parameters from your training loop.



python



import numpy as np



class RealTimeUBIUpdater:



def \_\_init\_\_(self, alpha_prior, nu_prior, phi_prior):



*\# Global priors learned from historical MCMC/Empirical Bayes training*



self.alpha = alpha_prior *\# Freq Gamma prior shape/rate*



self.nu = nu_prior *\# Sev Inv-Gamma prior shape/scale*



self.phi = phi_prior *\# Sev Gamma likelihood shape parameter*



def update_driver_premium(self,



base_mu, *\# Neural GLM frequency output (μ)*



base_lambda, *\# Neural GLM severity output (Λ)*



delta_exposure,*\# Exposure accumulated in window (ΔE)*



delta_claims, *\# Claims counted in window (ΔN)*



claim_costs): *\# List of claim costs in window \[Y_1, Y_2, \...\]*



*\# 1. Frequency Random Effect Posterior Update*



alpha_post = self.alpha + delta_claims



beta_post = self.alpha + (base_mu \* delta_exposure)



theta_updated = alpha_post / beta_post



*\# 2. Severity Random Effect Posterior Update*



if delta_claims \> 0 and len(claim_costs) \> 0:



nu_shape_post = self.nu + (self.phi \* delta_claims)



scaled_costs_sum = sum(\[(self.phi \* y) / base_lambda for y in

claim_costs\])



nu_scale_post = self.nu + scaled_costs_sum



omega_updated = nu_scale_post / (nu_shape_post - 1.0)



else:



*\# No claims means severity random effect stays at prior mean*



omega_updated = self.nu / (self.nu - 1.0)



*\# 3. Calculate Updated Pure Premium Output*



updated_frequency = base_mu \* delta_exposure \* theta_updated



updated_severity = base_lambda \* omega_updated



updated_pure_premium = updated_frequency \* updated_severity



return {



\"theta_i\": theta_updated,



\"omega_i\": omega_updated,



\"realtime_pure_premium\": updated_pure_premium



}



*\# \-\-- Quick Usage Verification \-\--*



*\# Let\'s say a baseline driver is expected to have 0.1 claims per

year, with \$2000 average severity.*



updater = RealTimeUBIUpdater(alpha_prior=2.5, nu_prior=3.0,

phi_prior=1.5)



*\# Case A: Driver drives safe for 0.2 years (no claims)*



safe_profile = updater.update_driver_premium(base_mu=0.1,

base_lambda=2000, delta_exposure=0.2, delta_claims=0, claim_costs=\[\])



print(f\"Safe Driver Premium Factor (theta):

{safe_profile\[\'theta_i\'\]:.4f}\")



*\# Case B: Driver has 1 claim costing \$4500*



risk_profile = updater.update_driver_premium(base_mu=0.1,

base_lambda=2000, delta_exposure=0.2, delta_claims=1,

claim_costs=\[4500\])



print(f\"Accident Driver Premium Factor (theta):

{risk_profile\[\'theta_i\'\]:.4f} \| Severity Factor (omega):

{risk_profile\[\'omega_i\'\]:.4f}\")



Use code with caution.



If you are evaluating deployment methods, would you like to cover **the

loss function equations for the Two-Stage neural

residualization** training loop, or explore **how to calibrate the prior

variables (**



**) using empirical Bayes**?



yes



To execute the two-stage training loop and anchor the real-time updating

architecture, you need both the neural loss functions that enforce

residualization and the Empirical Bayes formulas to calibrate the global

priors.



**1. Two-Stage Neural Residualization Loss Functions**



In the Two-Stage framework, traditional risk factors are locked first,

and the GRU model is penalized if its embeddings can be predicted by

those traditional features.



**Stage 1: The Actuarial Baseline Model**



Train a standard GLM (or Gradient Boosted Tree) on traditional features 



 to isolate baseline frequency 



 and severity 



.



**Stage 2: The GRU Residualization Network**



The GRU processes the telematics time-series to yield raw behavioral

embeddings 



. We define an adversarial projection network 



 that attempts to reconstruct 

The above content does NOT show the entire file contents. If you need to view any lines of the file which were not shown to complete your task, call this tool again to view those lines.
