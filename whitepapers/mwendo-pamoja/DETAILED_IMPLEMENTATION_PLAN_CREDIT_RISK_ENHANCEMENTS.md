Detailed implementation plan for strengthening Mwendo Pamoja
1. Intended outcome
The Mwendo Pamoja manuscripts already contain a strong credit-risk architecture: explicit liquidity variables, GRU and Transformer representations, hierarchical Bayesian underwriting, asymmetric dependence modelling, KESONIA-linked pricing, policy gates, IFRS 9 interfaces, SPV financing and an implementation roadmap.
The telematics paper adds something complementary. Its greatest contribution is not an insurance formula that can simply be copied into credit. It is the discipline with which it connects:
- exposure to statistical likelihood;
- persistent heterogeneity to credibility;
- explicit variables to neural representations;
- posterior predictions to financial quantities;
- offline estimation to online operation;
- individual outcomes to portfolio loss;
- loss emergence to reserves, capital and risk transfer;
- and every model layer to a specific owner, validation test and governance use.
The proposed revision will use that discipline to make the Mwendo Pamoja manuscripts more coherent from the first wallet event through default, recovery, IFRS 9 ECL, economic capital and the SPV waterfall.
The principal manuscripts affected are:
- [Part 1: Product Architecture and Cascades](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_1_Product_Architecture_and_Cascades.md)
- [Part 2a: Temporal Representation and Feature Engineering](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_2a_Deep_Temporal_Representation_and_Feature_Engineering.md)
- [Part 2b: Bayesian Underwriting and Asymmetric Copulas](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md)
- [Part 3: Regulatory Orchestration and Interventions](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_3_Regulatory_Orchestration_and_Interventions.md)
- [Part 4: Enterprise ERP and Telemetry](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_4_Enterprise_ERP_and_Telemetry.md)
- [Part 5: KESONIA Pricing and Capital Orchestration](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_5_KESONIA_Pricing_and_Capital_Orchestration.md)
- [Part 6: Implementation Roadmap](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_6_Implementation_Roadmap_and_Execution.md)
The main transfer source is the [telematics relativity paper](C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/telematics-relativities/paper.md), supported by the controlled specifications and modelling notes in the docs directory.
1.1 Editorial and development posture
The implementation language will be constructive, advancing and improvement-oriented. The revision will present Mwendo Pamoja as an architecture being deepened, connected and made more operationally complete. It will preserve the manuscripts' innovative propositions, mathematical ambition, human narrative and existing technical contributions while improving definitions, interfaces, empirical qualification and model governance.

The editorial method will:
- lead with the capability being created or strengthened;
- describe each refinement as an extension, integration, calibration, validation or next stage of the architecture;
- express boundaries affirmatively through intended purpose, applicable conditions, ownership and validation requirements;
- frame uncertainty as a quantity to estimate and govern;
- frame evidence gaps as research, data, validation or transaction-readiness tasks;
- present alternative models as benchmarked candidates with distinct strengths and use cases;
- preserve useful equations and move specialised derivations to appendices when they would interrupt the main narrative;
- explain how a proposed mechanism becomes production-ready instead of allowing a qualification to dominate the paragraph;
- use conditional language for model-dependent results, such as “under the stated assumptions” or “subject to validated calibration,” while keeping the surrounding narrative confident and forward-looking; and
- retain legal, accounting and regulatory precision without adopting a disputational or corrective voice.

Where an earlier passage is technically bounded, the revision will convert defensive wording into an advancing formulation. For example:
- “The deterministic model provides the transparent planning foundation for the stochastic cohort and waterfall extension,” rather than centring the paragraph on what the prototype does not yet perform.
- “PSI operates as a governed internal or contractual monitoring convention and routes material movement to investigation and recalibration,” rather than leading with a denial that it is a statutory threshold.
- “Transport security establishes confidentiality, integrity, authentication and provenance, while fairness, accounting and legal assurance are established through their dedicated control layers,” rather than listing what encryption cannot prove.
- “The P-spline is the principal smoothing candidate, with the retained B-spline, RW1 and AR(1) formulations preserved as comparative models in the appendix,” rather than presenting the refinement as replacement or rejection.
- “Senior-note protection is evaluated through the stated loss, recovery, reserve and waterfall scenarios,” rather than framing the discussion around an unsupported absolute guarantee.

This posture will not dilute technical accuracy. It will make every qualification useful by linking it to a stronger definition, implementation mechanism, validation test, decision owner or future development path.
2. Central semantic finding
The present Mwendo Pamoja architecture is strongest at two ends:
1. It has a rich, well-controlled feature and representation architecture.
2. It has a detailed financial destination in expected loss, pricing, capital, covenants and SPV cash flows.
The middle can be strengthened.
At present, Part 2b principally models a product-specific binary default outcome over a defined horizon:
\[
Y_{i,p,h}\sim\operatorname{Bernoulli}(PD_{i,p,h}).
\]That is useful for underwriting, but it compresses several economically distinct credit processes:
- time exposed to default;
- contract age;
- scheduled-payment opportunities;
- default timing;
- revolving utilisation before default;
- cure and restructuring;
- prepayment;
- balance at default;
- recovery amount;
- recovery timing;
- and repeated borrowing episodes.
Part 5 subsequently requires these quantities to construct losses and waterfall cash flows. Consequently, the current handoff is conceptually wider than the Part 2b likelihood itself.
The actuarial paper solves an analogous problem by distinguishing frequency, severity, exposure, loss development and risk transfer. The credit translation should be:
Actuarial construct	Credit-risk adaptation
Earned exposure	Time and amount genuinely at risk
Claim frequency	Default or delinquency-event intensity
Conditional severity	LGD and recovery severity
Claim occurrence	Default or arrears-state entry
Claims development	Cure, restructuring, write-off and recovery cash flows
Policyholder frailty	Persistent driver credit heterogeneity
Pure premium	Expected credit loss
Reserve distribution	IFRS 9 cash-shortfall distribution
Economic capital	Unexpected portfolio credit loss and related risks
Reinsurance	Subordination, OC, CRA, guarantees and risk transfer
Gross-to-net loss	Originated-pool loss to SPV and retained-loss allocation


This gives the revised manuscripts one continuous chain:
Contract and wallet events
            ↓
At-risk exposure and payment-state ledgers
            ↓
Explicit liquidity features + residual neural representation
            ↓
Default timing + EAD + cure + LGD/recovery models
            ↓
Calibrated product and horizon loss distributions
            ↓
Credit Policy and Compliance Gate
            ↓
IFRS 9 ECL, pricing and portfolio limits
            ↓
Dependent portfolio loss distribution
            ↓
SPV reserves, OC, tranches, waterfall and economic capital
3. Canonical model architecture
The revised canonical architecture should have six distinct statistical and operational layers.
Layer 1: Point-in-time credit state
The system constructs the borrower’s state as it was knowable at the decision time:
- active contracts;
- contractual balance;
- accrued interest and fees;
- scheduled payments;
- arrears bucket;
- revolving limit and utilisation;
- available wallet liquidity;
- insurance status;
- IPF premium-funding and refund status;
- existing interventions;
- platform, geography and macroeconomic state;
- data-quality and feature-availability status.
This becomes the model’s observation spine.
Layer 2: Representation
Two representation branches remain:
- GRU and Transformer neural embeddings.
- Explicit Liquidity Feature Path.
CFA, DLR, Earnings Velocity, Repayment Velocity, utilisation, reserve balance and time since depletion remain exclusively owned by the explicit path.
Neural encoders may observe raw transaction timing, sequences and context, but they should not receive the already engineered versions of those named variables.
Layer 3: Marginal credit processes
Rather than asking one PD model to represent all credit economics, the architecture will model:
- entry into delinquency or default;
- EAD, especially revolving drawdown;
- cure and restructuring;
- recovery amount;
- recovery timing;
- prepayment or early settlement;
- and, for IPF, cancellation-refund timing and carrier-related recovery.
Layer 4: Calibration and uncertainty
Raw posterior estimates will be calibrated by:
- product;
- forecast horizon;
- cohort or vintage;
- and, where justified, portfolio regime.
The model will retain both raw and calibrated results, including credible intervals and threshold-exceedance probabilities.
Layer 5: Policy and accounting uses
A separate Credit Policy and Compliance Gate will convert statistical outputs into actions. IFRS 9 staging and ECL will consume governed PD, LGD, EAD, scenario and cash-shortfall components through a distinct accounting policy.
Layer 6: Portfolio dependence and financing
Common borrower, platform, geography and macroeconomic effects will be modelled before a residual copula is introduced. Posterior loss paths will then enter:
- portfolio limits;
- economic-capital analysis;
- SPV purchase eligibility;
- OC and CRA calculations;
- tranche loss;
- waterfall survival;
- and early-amortisation analysis.
4. Detailed modelling improvements
4.1 Define the observation unit and credit exposure
The credit manuscripts should borrow the telematics paper’s insistence that exposure be defined before modelling the outcome.
Credit exposure is not a single scalar comparable across all products. It has at least three dimensions:
- time at risk;
- contractual or drawn balance;
- and the number of scheduled performance opportunities.
The model-ready ledger should define a row for a driver, product, risk episode and interval:
\[
(i,p,e,t),
\]where:
- \(i\) identifies the driver;
- \(p\) identifies microloan, revolving credit or IPF;
- \(e\) identifies the contract or risk episode;
- \(t\) identifies the observation interval.
Each row should contain:
\[
\left(
Y^{risk}_{ipet},
\Delta t_{ipet},
B_{ipet},
S_{ipet},
X_{ipet},
A_{ipet},
D_{ipet}
\right),
\]where:
- \(Y^{risk}\) indicates that the facility is still at risk;
- \(\Delta t\) is the at-risk interval;
- \(B\) is balance or exposure;
- \(S\) is contractual state;
- \(X\) contains point-in-time features;
- \(A\) records prior actions or interventions;
- \(D\) records default or state transition.
Product-specific conventions should be explicit:
- Microloan: contract-day or contract-week observations through maturity, prepayment, default or restructuring.
- Revolving credit: account-day or account-week observations with current utilisation, undrawn limit and potential further draw.
- IPF: finance-receivable observations linked to policy status, insurer payment confirmation, cancellation eligibility, unearned-premium refund and refund collection.
This avoids treating 30 daily observations from one loan as 30 independent borrowers. It also makes censoring, maturity and repeated borrowing episodes visible.
4.2 Introduce default timing without discarding the HLR
The existing logistic HLR should remain as a benchmark and underwriting reference model. A piecewise-exponential hazard specification should be introduced as a challenger and potential production extension.
For interval \(t\):
\[
D_{ipet}
\sim
\operatorname{Bernoulli}
\left(
1-\exp\{-\theta_i\lambda_{ipet}\Delta t_{ipet}\}
\right),
\]with:
\[
\log \lambda_{ipet}
=
\alpha_{p,a(t)}
+
f_p(\mathbf z_{ipet})
+
\boldsymbol{\beta}_{h,p}^{\top}\widetilde{\mathbf h}_{ipet}
+
u_{\mathrm{geo}}
+
u_{\mathrm{platform}}
+
u_{\mathrm{cohort},t}.
\]Here:
- \(\alpha_{p,a(t)}\) is a product-specific baseline hazard by contract age;
- \(f_p(\mathbf z)\) contains explicit nonlinear liquidity effects;
- \(\widetilde{\mathbf h}\) is the residual neural representation;
- \(\theta_i\) is persistent driver heterogeneity.
This is equivalent to a complementary-log-log formulation:
\[
\log\{-\log(1-PD_{ipet})\}
=
\log\Delta t_{ipet}
+
\log\theta_i
+
\eta_{ipet}.
\]It provides a natural bridge between:
- a seven-day microloan PD;
- a 30-day revolving PD;
- a 12-month IFRS 9 PD;
- lifetime default probability;
- and monthly SPV cash-flow losses.
The existing logit HLR and the hazard model should be compared on future vintages. Promotion should depend on calibration, stability, decision utility and cash-flow accuracy.
4.3 Conjugate driver credibility
The existing logistic-normal random effect is nonconjugate. There are two credible paths, and the manuscripts should distinguish them.
Recommended sequential extension: Gamma frailty
Let:
\[
\theta_i\sim\operatorname{Gamma}(a_0,b_0),
\]using the shape-rate convention, normally with \(a_0=b_0\) so that:
\[
\mathbb E[\theta_i]=1.
\]Conditional on a piecewise-exponential baseline, define:
\[
Q_{i,T}
=
\sum_{p,e,t\le T}
Y^{risk}_{ipet}
\lambda_{ipet}
\Delta t_{ipet}
\]and:
\[
N_{i,T}
=
\sum_{p,e,t\le T}D_{ipet}.
\]The driver posterior becomes:
\[
\theta_i\mid\mathcal D_T
\sim
\operatorname{Gamma}
\left(
a_0+N_{i,T},
b_0+Q_{i,T}
\right).
\]This creates an interpretable credibility ledger:
- matured, performing exposure increases the posterior rate;
- default events increase the posterior shape;
- thin-file drivers remain close to the collective prior;
- repeated lending episodes add evidence without erasing prior history;
- the posterior can be updated through sufficient statistics.
The frailty should be the single owner of persistent driver-level default heterogeneity. A separate unrestricted driver intercept should not coexist with it.
The ledger must also specify:
- when a default event is mature;
- how cures and re-defaults create new risk episodes;
- whether different products share one driver frailty;
- when sufficient statistics are restated after a material baseline-model change;
- and how transferred, closed or legally expired observations cease contributing exposure.
Offline logistic alternative: Pólya–Gamma augmentation
If the logistic HLR remains the preferred production likelihood, Pólya–Gamma augmentation can make logistic coefficients and random effects conditionally Gaussian inside an offline Gibbs sampler. It does not make the marginal logit model conjugate in the ordinary online sense because the latent Pólya–Gamma variables must still be sampled or approximated. The original method is described by Polson, Scott and Windle in their JASA paper.
The manuscripts should therefore describe it as:
- an offline inference candidate;
- potentially useful for structured Gibbs updates;
- benchmarkable against NUTS;
- and separate from the streaming Gamma-frailty credibility ledger.
4.4 Move full posterior estimation offline
Part 2b should clearly distinguish three cadences.
Event-time feature refresh
Wallet, repayment, balance and telematics state can update in seconds or minutes.
Online score refresh
A scoring service evaluates new features against a previously approved posterior artifact. It can refresh PD and uncertainty without refitting the HLR.
Offline model refresh
NUTS, HMC, Pólya–Gamma Gibbs, SMC, variational inference or Laplace estimation occurs offline under governed conditions.
The production service should load a signed artifact containing:
- model and schema versions;
- feature definitions;
- transformations;
- spline knots and penalty matrices;
- neural encoder version;
- residualisation projection;
- whitening transform, if retained;
- posterior draws or an approved analytic approximation;
- calibration parameters;
- threshold-exceedance logic;
- reason-code mapping;
- validation status;
- effective date;
- expiry or review date;
- fallback and rollback identifiers.
Online scoring then consists of deterministic operations:
1. Retrieve the point-in-time feature vector.
2. Apply the approved transformations.
3. Evaluate P-spline bases.
4. Generate or fetch the neural representation.
5. Apply residualisation and optional whitening.
6. Score against representative posterior draws or approved moments.
7. Apply product and horizon calibration.
8. Calculate posterior tail probabilities.
9. Pass outputs to the policy gate.
10. Store the complete decision record.
Full MCMC should run on a monthly, quarterly or trigger-based cadence. A drift alert may initiate review, but it should not automatically launch model retraining.
The GPU/BlackJAX discussion should be repositioned as an implementation option. The target is reproducible posterior estimation with acceptable diagnostics, regardless of whether computation runs on CPU, GPU or TPU.
4.5 Extend the current spline treatment with governed Bayesian P-splines
The current Part 2b uses B-splines with an AR(1) or RW1-style prior over adjacent coefficients. That material will be preserved rather than discarded. It will move to the Part 2b modelling appendix as a fully documented benchmark and alternative smoothing-prior specification, retaining its equations, interpretation, boundary treatment, diagnostic discussion and validation role. The main body will define the governed P-spline specification used as the principal candidate, while the appendix will compare the P-spline difference penalty with the retained B-spline plus RW1 and B-spline plus AR(1) constructions.

The appendix treatment will explain that RW1 expresses locally evolving adjacent coefficients without a mean-reverting level, while AR(1) expresses coefficient persistence around a long-run level when that interpretation is substantively justified. It will also show how the retained constructions are centred, how their innovation scales are assigned priors, how boundary and extrapolation behaviour is controlled, and how they are compared with the P-spline using future-period calibration, predictive performance, effective degrees of freedom, posterior geometry and decision value. This preserves the mathematical development and makes the choice among P-spline, RW1 and AR(1) an empirical model-comparison question.

The proposed revision should therefore define a P-spline explicitly in the main modelling sequence while maintaining the existing B-spline, AR(1) and RW1 development in the appendix.
A P-spline combines a reasonably rich B-spline basis with a discrete penalty over neighbouring coefficients, as introduced by Eilers and Marx in Flexible Smoothing with B-splines and Penalties.
For a continuous feature \(x\):
\[
f(x)=\sum_{k=1}^{K}B_{k,3}(x)\zeta_k,
\]using cubic B-splines.
For smooth curvature, apply a second-difference prior:
\[
\Delta^2\zeta_k
=
\zeta_k-2\zeta_{k-1}+\zeta_{k-2}
\sim
\mathcal N(0,\tau_f^2).
\]Equivalently:
\[
p(\boldsymbol\zeta\mid\tau_f)
\propto
\exp\left[
-\frac{1}{2\tau_f^2}
\boldsymbol\zeta^\top
D_2^\top D_2
\boldsymbol\zeta
\right].
\]Knot-setting protocol
Each feature will have a documented spline specification:
1. Define the economic scale and transformation.
   - log1p may be appropriate for strongly skewed ratios or durations.
   - Bounded proportions may use an appropriate bounded transformation or remain on their natural scale.
2. Determine validated support using the development period only.
3. Place a moderate but sufficiently rich knot grid.
   - Equally spaced knots on a suitably transformed scale are the standard P-spline construction.
   - Quantile-spaced knots can be retained as a sensitivity where data density is extremely uneven.
4. Use cubic basis functions unless an identified reason supports another degree.
5. Use a second-difference penalty for smooth curvature.
   - RW1 is appropriate only where first differences themselves are the intended regularity.
   - AR(1) should be reserved for genuinely mean-reverting ordered processes, such as selected time-varying coefficients.
6. Provide proper priors for the unpenalised null space.
7. Centre the realised smooth so its average contribution over the development population is zero.
8. Freeze knots, transformations and boundary rules in the release artifact.
9. Clip or flag out-of-support values and route material extrapolation to the policy gate.
10. Retain a nonlinear effect only when it improves future-period calibration, economic loss estimation or decision utility.
QR and penalty compatibility
Part 2a currently refers to QR-orthogonalised spline bases. A naive combination of QR orthogonalisation and an adjacent-coefficient penalty would be mathematically inconsistent because adjacency in the transformed basis no longer has the original spline meaning.
If:
\[
B=QR
\]and:
\[
\boldsymbol\theta=R\boldsymbol\zeta,
\]then the original P-spline penalty must become:
\[
\boldsymbol\theta^\top
R^{-\top}D_2^\top D_2R^{-1}
\boldsymbol\theta.
\]The implementation should use one of two approaches:
- retain the original B-spline basis and apply \(D_2^\top D_2\) directly; or
- use a Demmler–Reinsch or equivalent reparameterisation that diagonalises the smoothness structure while preserving the penalty.
The manuscript should not state that QR alone solves multicollinearity. It improves numerical conditioning; identifiability constraints, shrinkage and posterior diagnostics complete the control.
Candidate credit features for P-splines
P-splines are especially appropriate for:
- DLR;
- Earnings Velocity;
- Repayment Velocity;
- revolving utilisation;
- time since depletion;
- wallet volatility;
- loan tenure;
- contract age;
- platform tenure;
- arrears duration;
- number of recent credit episodes.
Product-varying smooths should use:
\[
f_p(x)=f_0(x)+d_p(x),
\]where \(f_0\) is the shared portfolio smooth and \(d_p\) is a more strongly shrunk product deviation. This is preferable to fitting unrelated curves for every product.
4.6 Strengthen neural redundancy control
The manuscripts already contain cross-fitted residualisation and optional whitening. These should be specified more tightly.
For each outer validation split:
1. Train the GRU and Transformer on the development portion.
2. Freeze their encoders.
3. Construct a fixed-dimensional bottleneck.
4. Fit a nuisance projection from the complete explicit design to each neural coordinate:
\[
\widehat{\mathbb E}_{-k}
\left[
\mathbf h_i\mid
Q_i,X_i,G_i,T_i
\right].
\]5. Calculate:
\[
\widetilde{\mathbf h}_i
=
\mathbf h_i-
\widehat{\mathbb E}_{-k(i)}
\left[
\mathbf h_i\mid
Q_i,X_i,G_i,T_i
\right].
\]6. Fit the projection without outcome labels.
7. Group folds by driver and order them in time.
8. Repeat the operation inside every outer validation split.
9. Apply optional whitening only after residualisation.
10. Version the residualiser and whitening transform with the model.
The residualisation design should include the explicit spline block, essential contract metadata and relevant group/time controls. Otherwise the neural block may reintroduce information already represented elsewhere.
Whitening remains optional. It should be retained only if it improves:
- posterior conditioning;
- effective sample sizes;
- coefficient stability;
- sensitivity to prior scale;
- or out-of-time performance.
It should not be presented as causal independence or fairness.
4.7 Fully specify the regularised horseshoe
The embedding block should receive a regularised horseshoe rather than a generic “shrinkage prior.”
For neural coefficient \(j\):
\[
\beta_{h,j}
\sim
\mathcal N
\left(
0,\tau_h^2\widetilde{\lambda}_j^2
\right),
\]where:
\[
\widetilde{\lambda}_j^2
=
\frac{c^2\lambda_j^2}
{c^2+\tau_h^2\lambda_j^2}.
\]Here:
- \(\tau_h\) controls global sparsity;
- \(\lambda_j\) allows locally supported coefficients to escape global shrinkage;
- \(c\) defines a finite slab for large coefficients.
The prior for \(\tau_h\) should be calibrated through a prior belief about the effective number of useful embedding coordinates, rather than adopting an arbitrary default. The regularised horseshoe and effective-nonzero formulation are developed by Piironen and Vehtari in the Electronic Journal of Statistics.
Separate global scales should govern:
- GRU-derived coordinates;
- Transformer-derived coordinates;
- fused coordinates, if retained;
- pre-registered interactions.
The P-spline coefficient block should use its smoothness prior rather than a horseshoe. The explicit main effects should use regularising priors consistent with their scale and economic interpretation.
Interactions should follow strong heredity: an interaction receives material prior freedom only when its parent effects are represented.
4.8 Separate PD, EAD, cure and LGD
The actuarial frequency-severity separation should become a credit loss decomposition.
For each posterior simulation:
\[
L_{ip}^{(s)}
=
D_{ip}^{(s)}EAD_{ip}^{(s)}
-
PV\left(
\sum_{\ell\ge0}
R_{ip,\ell}^{(s)}
\right),
\]where:
- \(D\) represents default timing;
- \(EAD\) represents balance when default occurs;
- \(R_{\ell}\) represents recovery cash flows.
The model family should include:
Default and delinquency
Discrete-time or piecewise-exponential state-transition hazards.
EAD
- contractual amortisation for microloans;
- utilisation and stressed drawdown for revolving credit;
- outstanding financed amount for IPF.
Cure and restructuring
A competing state-transition model distinguishing:
- cure;
- restructure;
- continued default;
- prepayment;
- and write-off.
Recovery amount
A two-part model can separate:
- probability of any recovery;
- positive recovery amount conditional on recovery.
Recovery timing
A survival or discrete development model can estimate when cash is likely to arrive.
IPF refund
IPF should separately model:
- policy cancellation eligibility;
- insurer confirmation;
- gross unearned-premium refund;
- administrative deductions;
- assignment and account control;
- receipt timing;
- net application to the finance receivable.
This will give Part 5 cash-flow distributions rather than point assumptions attached after the PD model.
4.9 Calibration should be a separate financial control
The revised manuscripts should distinguish:
- representation residualisation;
- probability calibration;
- and portfolio financial calibration.
A product-horizon calibration model can use:
\[
\operatorname{logit}
\left(
PD^{cal}_{i,p,h}
\right)
=
\kappa_{p,h,v}
+
s_{p,h}
\operatorname{logit}
\left(
PD^{raw}_{i,p,h}
\right),
\]where \(v\) identifies an approved vintage or regime and \(s_{p,h}>0\).
The calibration layer should preserve:
- rank where appropriate;
- central tendency;
- product and horizon consistency;
- and credible uncertainty.
An expected-loss-weighted reconciliation can then test:
\[
\sum_i
EAD_i
PD^{cal}_i
LGD_i
\]against the approved portfolio loss expectation for the relevant cohort. This is the credit analogue of exposure-normalised tariff balance. It should operate at a credible portfolio or vintage level, with partial pooling where cells are sparse.
The system should store:
- raw PD;
- calibrated PD;
- calibration version;
- calibration population;
- calibration uncertainty;
- and the resulting expected loss.
4.10 Establish a dependence hierarchy before applying copulas
The current copula discussion is valuable, but the revised manuscript should make the order of dependence modelling explicit.
1. Shared driver state: Persistent borrower heterogeneity or liquidity condition.
2. Shared observed factors: Platform commission, fuel prices, geography and macroeconomic conditions.
3. Shared hierarchical shocks: Platform, location, cohort and calendar effects.
4. Residual dependence: Dependence remaining after the marginal models and shared factors.
5. Copula: A selected model for that residual dependence.
6. Scenario overlay: Structured shocks beyond the reliably observed range.
This prevents the same economic shock from appearing simultaneously in:
- a shared time effect;
- driver frailty;
- stressed marginal PD;
- copula parameter;
- and an external scenario multiplier.
For lower-tail default modelling with Clayton, the manuscript should retain the explicit convention:
\[
Y_{i,p}^{(s)}
=
\mathbf 1
\left[
U_{i,p}^{(s)}
\le PD_{i,p}^{(s)}
\right].
\]Under this orientation, small uniform values correspond to joint default events, making Clayton’s lower-tail dependence economically relevant.
Validation must examine:
- joint default counts;
- product-pair co-default rates;
- tail concentration;
- parameter stability;
- PIT or randomized-PIT behaviour;
- portfolio loss quantiles;
- waterfall outcomes;
- and sensitivity to alternative copula families.
4.11 Model interventions as actions affecting future observations
Credit decisions and interventions change the data subsequently observed.
Examples include:
- declined applications;
- reduced limits;
- frozen draws;
- premium holidays;
- restructuring;
- repayment reminders;
- reserve-pocket transfers;
- route or income interventions.
The model must retain a decision-and-treatment ledger containing:
- score and uncertainty before the action;
- policy rules applied;
- action selected;
- override;
- customer response;
- subsequent exposure;
- and matured outcome.
This supports analysis of:
- selective labels from approved-only customers;
- informative censoring;
- changes in exposure caused by limit decisions;
- cure caused by restructuring;
- and outcomes affected by an intervention.
Shadow scoring, carefully bounded pilots and causal-sensitivity analysis should be incorporated before claiming that an intervention reduced default.
5. Manuscript-by-manuscript implementation
Part 1: Product Architecture and Cascades
Part 1 should remain the human and microeconomic entry point.
Add a new subsection explaining the three credit clocks:
- income and liquidity clock;
- contractual repayment clock;
- default and recovery clock.
Show how the same fuel-price or platform shock can affect:
- wallet liquidity;
- repayment capacity;
- revolving utilisation;
- insurance continuity;
- EAD;
- default timing;
- recovery;
- and SPV collections.
Extend the cascade diagram into:
External shock
    ↓
Income and liquidity deterioration
    ↓
Product-specific exposure changes
    ↓
Arrears and utilisation transitions
    ↓
Default, cure or restructuring
    ↓
Recovery cash flows
    ↓
SPV loss and waterfall consequences
Clarify that correlated defaults have three sources:
- a common driver across multiple products;
- common platform/geographic shocks across drivers;
- residual dependence after those factors.
This prepares the reader for the frailty and copula hierarchy in Part 2b.
Part 2a: Data and representation
Add five canonical ledgers:
1. Credit exposure and risk-set ledger.
2. Contractual schedule and arrears ledger.
3. Decision and intervention ledger.
4. Default, cure and recovery ledger.
5. Model-artifact and scoring ledger.
Every modelling row should have:
- event time;
- ingestion time;
- available time;
- decision time;
- label-maturity time;
- contract episode;
- product;
- balance;
- state;
- action;
- outcome maturity.
Add a formal rule:
\[
\text{feature\_available\_time}
\le
\text{decision\_time}
\]and:
\[
\text{label\_maturity\_time}
\le
\text{training\_cutoff}.
\]Clarify that the spline design is generated from a versioned basis service. Part 2a owns computation and point-in-time reproducibility; Part 2b owns its statistical prior and penalty.
Add the offline-to-online artifact diagram and specify parity tests between batch training and streaming scoring.
Part 2b: Bayesian underwriting
This part receives the most substantial enhancement.
Recommended revised order:
1. Outcomes, horizons, censoring and risk episodes.
2. Product-specific marginal default models.
3. Explicit P-spline effects.
4. Neural residualisation and regularised horseshoe.
5. Hierarchical group effects.
6. Driver credibility and Gamma-frailty extension.
7. Offline posterior inference and online scoring.
8. Calibration and posterior decision quantities.
9. EAD, cure, LGD and recovery interfaces.
10. Dependence hierarchy and copulas.
11. Validation, fairness and model governance.
12. Alternatives and benchmarking appendix.
The existing logistic HLR should be retained as the reference model. The hazard/frailty model should be introduced as the preferred sequential-credibility challenger.
The appendix should compare:
- Bernoulli-logit HLR with NUTS;
- logit HLR with Pólya–Gamma augmentation;
- complementary-log-log or piecewise-exponential hazard with Gamma frailty;
- the principal P-spline specification with the retained B-spline plus RW1 and B-spline plus AR(1) alternatives;
- Laplace and variational approximations;
- explicit-only baseline;
- explicit-plus-neural model.
Part 3: Regulatory orchestration
Add a clear distinction among:
- model posterior;
- calibrated credit estimate;
- accounting interpretation;
- contractual covenant;
- credit policy;
- compliance rule;
- intervention;
- and manual override.
Expand the policy gate inputs to include:
- PD by horizon;
- EAD;
- LGD and recovery timing;
- uncertainty;
- exposure concentration;
- data quality;
- action history;
- and model freshness.
Add governance for sequential credibility:
- matured-event eligibility;
- sufficient-statistic restatement;
- model-version changes;
- thin-file treatment;
- maximum individual-effect influence;
- appeal and correction;
- fallback to pooled estimates.
Integrate intervention evaluation, selective labels and outcome maturity into model-risk governance.
Part 4: ERP and telemetry
Extend the ERP architecture beyond balances and impairment journals.
Add subledger fields for:
- contract episode;
- schedule version;
- arrears entry and exit;
- default date;
- cure date;
- restructure date;
- write-off;
- recovery amount and date;
- IPF refund claim, confirmation and receipt;
- decision and policy version;
- PD, EAD and LGD version;
- calibration version;
- posterior-artifact version.
Define a governed ECL handoff containing:
\[
PD_{\mathbb P},
EAD,
LGD,
\text{cash-shortfall timing},
\text{scenario},
\text{stage},
\text{discount rate},
\text{model version}.
\]D365 should receive approved accounting outputs and lineage, while the risk platform retains granular statistical computation and posterior artifacts.
Part 5: Pricing, capital and SPV finance
Part 5 should consume posterior loss paths from Part 2b.
Add a section called:
From borrower posterior to SPV cash-flow distribution
For every simulation:
1. Draw calibrated default time.
2. Draw EAD or contractual balance.
3. Draw cure, prepayment or restructuring.
4. Draw recovery amount and timing.
5. Apply IPF refund mechanics where relevant.
6. Aggregate collections and losses by month.
7. Apply purchase eligibility.
8. Apply servicing and operating costs.
9. Replenish or release CRA.
10. Apply the waterfall.
11. Calculate tranche interest and principal loss.
12. Calculate OC, DSCR, trigger month and residual equity return.
Add explicit distinctions among:
- IFRS 9 ECL;
- pricing expected loss;
- economic capital;
- regulatory capital;
- SPV first-loss support;
- CRA;
- overcollateralisation;
- subordination;
- and investor risk premium.
Borrow the telematics paper’s gross-to-net framework:
Originated gross pool
        ↓
Eligible receivables purchased by SPV
        ↓
Collections, defaults and recoveries
        ↓
Excess spread + CRA + OC + subordination
        ↓
Class A loss
Class B loss
Class C residual loss
        ↓
Sponsor-retained and investor-transferred risk
Add one-year and ultimate views:
- one-year loss and covenant deterioration;
- ultimate cohort loss through final recovery;
- economic capital or required support at selected VaR and expected-shortfall levels;
- tranche attachment and exhaustion probability;
- expected early-amortisation month;
- reserve survival.
Part 6: Roadmap
Reorganise delivery gates around evidence maturity.
Phase 0: Definitions and ledgers
- Default, cure, restructure, write-off and recovery definitions.
- Product horizons.
- Risk episodes and censoring.
- Exposure and balance conventions.
- Action and outcome ledgers.
Phase 1: Explicit baseline
- Product-specific logistic and hazard baselines.
- P-spline specifications.
- Group effects.
- Calibration.
- Point-in-time validation.
Phase 2: Hierarchical and sequential credibility
- Offline NUTS reference.
- Gamma-frailty challenger.
- Sufficient-statistic ledger.
- Artifact publishing.
- Online scoring parity.
Phase 3: Neural challenger
- Frozen encoder.
- Cross-fitted residualisation.
- Optional whitening.
- Regularised horseshoe.
- Explicit-only fallback.
- Incremental-value gate.
Phase 4: Full loss modelling
- EAD.
- Cure and prepayment.
- LGD.
- Recovery amount and timing.
- IPF refund development.
Phase 5: Dependence and portfolio loss
- Common-shock hierarchy.
- Residual copula.
- Economic capital.
- SPV waterfall.
- Reverse stress.
Phase 6: Shadow and bounded pilot
- No-action shadow period.
- Selective-label analysis.
- Intervention evaluation.
- Data-quality and fairness gates.
- Exposure caps and rollback.
Phase 7: Transaction and scale readiness
- Lender validation.
- Independent model review.
- SPV scenario pack.
- Accounting reconciliation.
- Model release, rollback and monitoring runbooks.
6. Controlled-specification updates
The public manuscripts should preserve narrative flow. Technical implementation detail should be concentrated in the controlled specifications.
The controlled documents should receive:
- full data schemas;
- likelihood definitions;
- risk-set construction;
- spline matrices and penalties;
- prior specifications;
- artifact schemas;
- sequential-update rules;
- restatement logic;
- validation tests;
- decision interfaces;
- and accounting mappings.
The modelling notes can remain an idea inventory, but claims entering the canonical manuscripts should be reconciled against primary sources and actual implementation tests.
7. Validation programme
The revised model should pass six validation families.
Statistical validation
- Prior predictive checks.
- Posterior predictive checks.
- Rank-normalised \(\hat R\).
- Bulk and tail ESS.
- Monte Carlo standard error.
- Divergences and energy diagnostics.
- Calibration intercept and slope.
- Brier and log scores.
- Survival calibration by horizon.
- Recovery amount and timing validation.
Temporal and hierarchical validation
- Forward-time holdouts.
- Driver-grouped splits.
- Platform and geography holdouts.
- New-driver performance.
- New-platform transportability.
- Vintage calibration.
- Outcome-maturity checks.
Redundancy validation
- Condition numbers.
- Singular values.
- Posterior correlations.
- Variance inflation diagnostics for explicit blocks.
- Spline effective degrees of freedom.
- Neural ablations.
- Explicit-only versus combined model.
- Residualiser leakage tests.
- Whitening sensitivity.
Financial validation
- PD, LGD and EAD reconciliation.
- Expected-loss reconciliation.
- Recovery cash-flow back-tests.
- Cohort cash-flow accuracy.
- SPV waterfall reconciliation.
- Tranche attachment and loss back-testing.
- CRA and OC trigger reproduction.
Operational validation
- Online and offline feature parity.
- Basis-function parity.
- Posterior artifact reproducibility.
- Score replay from historical snapshots.
- Late-event correction.
- Artifact expiry and rollback.
- Explicit-only fallback.
Decision and fairness validation
- Approval, limit and price outcomes.
- Uncertainty-driven actions.
- Override rates.
- Calibration by reviewed groups.
- False-positive and false-negative consequences.
- Cure and restructuring outcomes.
- Complaints and appeals.
- Intervention effects.
- Thin-file treatment.
8. Acceptance criteria
The revision should be accepted only when:
- Every product has a defined observation unit, risk horizon and maturity rule.
- Default timing is distinguishable from point-in-time PD.
- The logit HLR is not described as conjugate.
- Gamma-frailty conjugacy is tied to a compatible hazard likelihood.
- Pólya–Gamma augmentation is described as an offline inference option.
- Full MCMC never appears in the online request path.
- The production artifact contains all transformations and calibration parameters.
- Each P-spline records degree, knots, support, penalty order, prior and boundary treatment.
- The existing B-spline, RW1 and AR(1) formulations remain preserved in the Part 2b appendix with their equations, priors, centring, boundary rules and comparative-validation criteria.
- QR or Demmler–Reinsch reparameterisation preserves the spline penalty.
- CFA, DLR, Earnings Velocity and Repayment Velocity have one engineered owner.
- Neural residualisation is cross-fitted by driver and time.
- Whitening is optional and development-fold-specific.
- The regularised horseshoe has a finite slab and calibrated global scale.
- Persistent driver heterogeneity has one canonical owner.
- PD, EAD, cure, LGD and recovery timing remain distinct.
- IFRS 9 ECL, pricing loss, economic capital and SPV protection are not conflated.
- Common factors are modelled before residual copula dependence.
- Portfolio simulations do not apply the same shock twice.
- Policy actions and interventions are recorded as treatments.
- Part 5 receives posterior cash-flow paths rather than only point expected loss.
- SPV protection claims are conditional on calculated scenarios.
- The explicit-only model remains operational as the champion or fallback when neural incremental value is unstable.
- The revised manuscripts use advancing, improvement-oriented language: technical boundaries are expressed through purpose, conditions, controls, validation and next-stage capability rather than defensive disclaimers or a disputational tone.
The result will preserve Mwendo Pamoja’s central credit-risk identity while giving it the same end-to-end discipline achieved in the actuarial paper: correctly defined exposure, credible individual learning, controlled nonlinearities, offline Bayesian estimation, real-time reproducible decisions and a continuous mathematical bridge from driver liquidity to recoveries, capital and lender cash flows.

9. Implementation decision note: general HLR conditional conjugacy
This note records a modelling option to be evaluated during implementation. It does not amend the architecture selected in the preceding plan. The implementation decision will be made after benchmarking posterior accuracy, computational efficiency, pooling behaviour, diagnostics and operational fit.

The principal question is whether conjugacy should be used primarily as an inference strategy for the general hierarchical Bayesian logistic regression rather than being centred on driver-specific random effects. Pólya–Gamma augmentation provides a coherent route because it preserves the HLR and makes its Gaussian parameter blocks conditionally conjugate without removing hierarchical pooling.

For the existing model:
\[
Y_i
\sim
\operatorname{Bernoulli}
\left(
\operatorname{logit}^{-1}(\eta_i)
\right),
\]
with:
\[
\eta_i
=
\alpha
+Q_i\boldsymbol\beta_z
+\widetilde H_i\boldsymbol\beta_h
+R_i\boldsymbol\gamma
+u_{\mathrm{geo}(i)}
+v_{\mathrm{platform}(i)}
+\delta_{t(i)},
\]
introduce:
\[
\omega_i\mid\eta_i
\sim
\operatorname{PG}(1,\eta_i).
\]

Conditional on \(\boldsymbol\omega\), the logistic likelihood becomes Gaussian in the linear predictor. This permits efficient conditional updates while preserving the meaning and structure of the following blocks:
- global and product intercepts;
- explicit liquidity coefficients;
- P-spline coefficients;
- residual neural-embedding coefficients;
- geography, platform and cohort effects;
- AR(1) or RW1 time effects;
- selected interactions; and
- driver effects where repeated matured credit episodes provide adequate identification.

The construction aligns particularly well with the proposed P-splines because their difference-penalty priors are Gaussian. Conditional on the Pólya–Gamma variables and smoothing scales, the spline coefficients form a sparse Gaussian update. The retained B-spline–RW1 and B-spline–AR(1) alternatives, Gaussian hierarchical effects and Gaussian state processes can be assessed within the same blocked-computation framework.

The model would be conditionally conjugate rather than entirely closed-form. The following components would retain their own updates:
- Pólya–Gamma latent variables;
- hierarchy variance parameters;
- spline smoothing scales;
- regularised-horseshoe local and global scales;
- LKJ correlation structures;
- calibration parameters; and
- selected time-process persistence parameters.

A candidate blocked Gibbs sampler would alternate between:
1. Pólya–Gamma latent-variable updates.
2. Joint or blocked Gaussian coefficient, spline and hierarchical-effect updates.
3. Hierarchical scale and covariance updates.
4. Regularised-horseshoe scale updates.
5. Calibration, posterior summarisation and diagnostic calculations.

The hierarchy itself remains intact:
\[
u_g\mid\sigma_g
\sim
\mathcal N(0,\sigma_g^2),
\]
so sparse groups continue to shrink toward the collective mean while information-rich groups receive greater differentiation. Pólya–Gamma augmentation changes the posterior computation; it does not change the economic meaning of partial pooling.

If this option is selected during implementation, the architecture would be expressed as:
- Primary model: hierarchical Bayesian logistic regression with Pólya–Gamma-augmented offline inference.
- Pooling structure: product, platform, geography, cohort and selected time-varying effects remain hierarchical.
- Nonlinear effects: governed P-splines in the main model, with B-spline–RW1 and B-spline–AR(1) alternatives retained in the appendix.
- Neural block: cross-fitted residual representations with regularised-horseshoe shrinkage.
- Production scoring: an approved posterior artifact, with no Pólya–Gamma sampling or MCMC during an underwriting request.
- Reference inference: NUTS remains available for posterior benchmarking and validation.
- Survival challenger: the hazard/Gamma-frailty construction remains available for default-timing and sequential-credit experiments without automatically replacing the HLR.

Driver-specific random effects can remain part of the hierarchy where repeated matured credit episodes support them. They need not become the reason for adopting conjugacy. The general HLR, including its pooled group effects, explicit nonlinearities and residual neural block, is the broader computational opportunity.

The implementation comparison will therefore test:
- Pólya–Gamma blocked Gibbs against NUTS on the same HLR;
- agreement in posterior means, intervals, tails and group-level shrinkage;
- effective sample size and wall-clock performance;
- behaviour under separation, sparse defaults and weakly identified groups;
- sparse-linear-algebra performance for P-spline and time-effect blocks;
- compatibility with the regularised horseshoe and covariance hierarchy;
- calibration and decision stability on future vintages; and
- the incremental value of the separate hazard/Gamma-frailty challenger for default timing and cash-flow projection.

The decision principle is:

> Use Pólya–Gamma augmentation to make the complete HLR computationally tractable while preserving hierarchical pooling when implementation evidence supports it. Retain Gamma-frailty conjugacy as a separate survival-model extension whose role is determined through comparative validation.
