# D06 Implementation Plan: Bayesian Underwriting and Asymmetric Copulas

## Objective and model scope

Rewrite D06 as a model methodology and governance paper for a real-world credit-risk and decision system. The document should specify use cases, population, target, horizon, feature interface, hierarchical likelihood, priors, inference, online scoring, validation, decision losses, dependence modelling, economic-capital output, explanation, fairness, and model-risk controls. It should state what the model does not do: it does not by itself create a risk-neutral measure, prove causality, guarantee senior protection, modify Basel regulatory correlations, or determine legal policy.

The core modelling proposition remains viable. Neural representations and Explicit Liquidity Features can enter a hierarchical Bayesian logistic model, with partial pooling across clusters and uncertainty-aware decisions. The implementation must be simplified where complexity does not survive validation and must preserve an explicit benchmark model.

## Proposed document architecture

1. Model purpose, users, exclusions, and notation.
2. Population, observations, labels, horizons, and interventions.
3. Input contract from D05.
4. Hierarchical Bayesian model and priors.
5. Scalable offline inference and online posterior prediction.
6. Validation, calibration, uncertainty, stability, and challengers.
7. Decision analysis and Credit Policy and Compliance Gate interface.
8. Customer pricing and optional market-consistent valuation overlay.
9. Dependence, copulas, portfolio loss, and economic capital.
10. Explainability, fairness, monitoring, and model-risk governance.
11. Limitations, evidence, acceptance criteria, and references.

## Section-level implementation actions

### D06-P01: Rebuild notation and equation control

**Action:** Add a controlled notation section and re-key every formula.

**Resolves:** D06-I13.

**Content:** Define `PD_P`, `PD_Q`, `Phi_neural`, `Z_liquidity`, cluster and time indexes, coefficients, spline basis, random effects, AR parameters, copula uniforms and parameters, exposure, LGD, recovery, expected loss, unexpected loss, VaR, expected shortfall, credible interval, `K_RBCP`, `K_cap`, `m_A`, `m_B`, `CoC`, and `OpEx`. State units and horizon.

Reconstruct spline recursion, logit, priors, Cholesky parameterisation, copula density, and capital equations from primary sources. Use executable notebooks or tests as reference, not converted prose. Include dimensional and numerical examples.

**Acceptance tests:** No symbol has two meanings. Minus signs and inequalities render correctly. Each formula matches a tested implementation and references its test case.

### D06-P02: Define separate model use cases and decision owners

**Action:** Rewrite the introduction and taxonomy.

**Resolves:** D06-I01 and D06-I08.

**Content:** Create a use-case table for origination, limit management, intervention prioritisation, IFRS 9 input, portfolio stress, customer pricing input, and covenant monitoring. For each specify population, target, horizon, measure, output, decision owner, policy owner, frequency, validation standard, and permitted reuse.

State that underwriting predicts `PD_P` or another real-world event. IFRS 9 uses an approved real-world forward-looking methodology [5]. Customer pricing uses `K_RBCP` under [1], [2]. Portfolio stress uses dependence and cash flows. Contractual covenants and hard rules remain outside the model.

**Acceptance tests:** Every output has one named use and owner. A model cannot be reused for accounting or pricing without a fitness assessment. Decision and policy code are versioned separately.

### D06-P03: Freeze the D05 input interface and feature treatment

**Action:** Rewrite “Full Mathematical Model Specification” inputs.

**Resolves:** D06-I01.

**Content:** Import versioned `Phi_neural`, `Z_liquidity`, identifiers, masks, quality flags, and decision timestamp. List CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and interactions only in `Z_liquidity`. Prohibit those named metrics from the neural vector by design review.

Define standardisation using training-only statistics, spline knots, monotonic or shape expectations where justified, missing values, clipping, interactions, and shrinkage. Record protected and sensitive attributes used only for approved fairness testing, unless lawful model use is separately justified.

**Acceptance tests:** An automated manifest shows each feature once. Feature vintage is no later than decision time. Model artifacts pin the feature-set version and preprocessing.

### D06-P04: Replace unsafe binomial aggregation with a validated scaling method

**Action:** Rewrite “Bernoulli-to-Binomial Aggregation.”

**Resolves:** D06-I02.

**Content:** Explain why binomial grouping is exact only for observations with identical conditional probability. Retain individual Bernoulli likelihood as the reference. Evaluate scaling alternatives: vectorised likelihood, minibatch variational inference, Laplace approximation, subsampling with likelihood correction, GPU acceleration, or exact grouping of identical design rows.

If any approximation is used, compare coefficients, posterior intervals, calibration, tail predictions, subgroup results, and decision outcomes to the individual reference on representative samples. Define an acceptable maximum deviation and performance gain. Do not average neural embeddings into one probability without an approximation disclosure.

**Acceptance tests:** Approximation error stays within approved tolerances across time and high-risk segments. If not, use the individual likelihood. The paper no longer calls heterogeneous aggregation exact.

### D06-P05: Separate offline posterior estimation from online scoring

**Action:** Rewrite MCMC and BlackJAX production sections.

**Resolves:** D06-I03.

**Content:** Use NUTS or HMC offline for reference posterior estimation and complex-model validation. Specify chains, warm-up, draws, seeds, adaptation, target acceptance, divergences, tree depth, `R-hat`, ESS, energy diagnostics, and posterior predictive checks. Evaluate variational or Laplace approximation if needed for scheduled refresh.

Publish a signed posterior artifact or representative fixed draws to a deterministic online scoring service. Define calculation of posterior mean, quantiles, exceedance, and uncertainty. Set latency, throughput, numerical tolerance, fallback, refresh cadence, emergency suspension, and rollback. Use a simpler approved model if artifacts are stale or service health fails.

**Acceptance tests:** Online scores reproduce offline predictions within tolerance. No request launches NUTS. Model refresh passes convergence and validation before promotion. Rollback is rehearsed.

### D06-P06: Expand validation beyond sampler diagnostics

**Action:** Rewrite convergence, posterior checks, and performance sections.

**Resolves:** D06-I08 and D06-I09.

**Content:** Separate computational diagnostics from model validity. Use driver-separated, time-forward, platform-held-out, and geography-held-out evaluation. Assess discrimination, Brier score, log score, calibration intercept and slope, calibration curves, credible-interval coverage, lift, stability, subgroup uncertainty, and decision utility. Include delayed outcomes and minimum maturity.

Address selection and policy feedback: rejected applicants lack ordinary outcomes; interventions change observed defaults; limit changes change exposure. Capture policy and treatment variables and apply causal or sensitivity methods where appropriate. Compare explicit-only Bayesian logistic, conventional logistic, gradient boosting, neural-only, and full models.

**Acceptance tests:** The full model must beat a simpler challenger on pre-specified out-of-time criteria and justify complexity. Calibration and uncertainty must pass, not only AUC. Results include confidence intervals and failure segments.

### D06-P07: Separate decision losses, CBK pricing, and market valuation

**Action:** Rewrite “Real-Time Bayesian Decision Boundaries” and “Friction-Adjusted Risk-Neutral Pricing.”

**Resolves:** D06-I04 and D06-I08.

**Content:** Define a decision-loss matrix for approve, decline, reduce limit, freeze, or intervene, including expected loss, customer value, capital or liquidity constraint, operating cost, and uncertainty. Require policy review for thresholds. Use posterior integration rather than only point PD.

For customer pricing, state KESONIA plus `K_RBCP`; internally decompose expected loss, operating and funding cost, shareholder return or capital, liquidity, uncertainty, and borrower risk without double counting [1], [2]. Keep fees separate in total cost.

Create a distinct optional valuation subsection for `PD_Q`. State that it requires observable market prices or transaction spreads, separation of liquidity and structural enhancement, recovery convention, and validation [20], [35], [36]. Where data are absent, do not calculate or label `PD_Q`.

**Acceptance tests:** `PD_P` is never renamed `PD_Q`. Pricing outputs reconcile to D09. Thresholds comply with the downstream gate and customer contract.

### D06-P08: Rebuild the copula methodology and simulation

**Action:** Rewrite all copula sections.

**Resolves:** D06-I05 and D06-I06.

**Content:** Define outcome marginals and dependence variables by product, driver, platform, geography, and period. Explain variable orientation. Compare Gaussian, Student-t, Clayton, rotated Clayton, Gumbel, Frank, and vine candidates. Define estimation, censoring, weights, parameter uncertainty, time variation, goodness of fit, and out-of-sample evaluation.

The simulation algorithm should draw dependent uniforms from the fitted copula, compare each to the relevant conditional default threshold, apply exposure and stochastic or scenario LGD and recovery lag, aggregate monthly cash, and pass it to the D03 waterfall. Separate process randomness, parameter uncertainty, and model uncertainty. Report loss distribution VaR and expected shortfall separately from Bayesian credible intervals.

**Acceptance tests:** Simulation recovers independent and perfectly dependent limiting cases. Marginal default rates match inputs. Dependence metrics match fitted data within tolerance. Family sensitivity is disclosed.

### D06-P09: Separate economic capital, SPV enhancement, and regulatory capital

**Action:** Rewrite “Unexpected Loss Quantification and Regulatory Capital Linkage.”

**Resolves:** D06-I07.

**Content:** Define economic capital as an internal loss percentile or expected-shortfall measure net of expected loss under a stated horizon and confidence. Define SPV protection as Class C, subordination, OC, reserve, excess spread, and cash waterfall. Define lender regulatory capital as an external calculation under the lender's applicable approach and CBK implementation.

Use Basel [8] only to explain why internal copula parameters do not replace prescribed correlations. Do not claim IRB permission or capital relief. Provide lender data outputs and stress results for its own assessment.

**Acceptance tests:** Capital values carry owner, purpose, currency, horizon, percentile, and authority. A lower copula estimate cannot automatically reduce RWA or Class C.

### D06-P10: Integrate explainability, monitoring, and model-risk governance

**Action:** Rewrite XAI and MRM sections.

**Resolves:** D06-I09, D06-I10, and D06-I11.

**Content:** Prefer posterior coefficient and spline contributions for explicit features, plus grouped neural attribution with stability checks. Define background dataset, correlated-feature grouping, local and global explanation, reason-code mapping, and limitations. Store actual policy rules separately from predictive explanations.

Create model inventory, risk tier, owner, developer, independent validator, approval committee, limitations, change thresholds, deployment sign-off, incident levels, monitoring, retraining, challenger, rollback, and retirement. Treat SR 11-7 as comparative practice [9]. Define PSI thresholds as internal conventions and monitor calibration, discrimination, uncertainty, data quality, missingness, fairness, and outcomes alongside PSI.

**Acceptance tests:** Reason codes reproduce the decision path. Explanations are stable under small perturbations. Model changes cannot reach production without independent approval. PSI alone cannot force a legally characterised action.

### D06-P11: Build a legally reviewed fairness and customer-outcome framework

**Action:** Rewrite fairness sections.

**Resolves:** D06-I12.

**Content:** Define groups and attributes through Kenyan legal and privacy review. Measure selection, rate, limit, calibration, false-positive and false-negative rates, interventions, complaints, appeal, and downstream outcomes. Include sample sufficiency, uncertainty, intersectional analysis, and multiple-testing controls.

Explain that feature blindness does not remove proxies and MMD does not guarantee equalized odds. Compare mitigation alternatives and report utility and fairness trade-offs. Include less-discriminatory-alternative testing, customer explanations, appeal, and human override governance.

**Acceptance tests:** No fairness guarantee remains. Metrics and thresholds are approved and reproducible. A subgroup failure has an escalation, remediation, and launch-blocking rule where appropriate.

### D06-P12: Replace Appendix A with a measured P-versus-Q boundary

**Action:** Remove the claim that stochastic calculus is redundant and replace the appendix.

**Resolves:** D06-I04.

**Content:** Explain that structural and reduced-form models may be impractical or poorly identified for the target assets, but that does not eliminate the distinction between physical and risk-neutral measures. Describe when real-world expected-loss pricing is sufficient for management and when fair-value or investor pricing may need a market overlay. State data requirements and uncertainty. Use [20] as the core empirical boundary source.

**Acceptance tests:** No tenor-based claim says P-Q divergence is negligible without evidence. The appendix supports, rather than contradicts, D09's rate taxonomy.

### D06-P13: Add reproducibility, test artefacts, and references

**Action:** Rewrite conclusion and reference section.

**Resolves:** D06-I13 and closes all findings.

**Content:** Require versioned data snapshot, feature contract, code commit, environment lock, random seeds, posterior samples, diagnostics, validation report, fairness report, decision-policy version, and signed approval. Add synthetic and golden datasets for likelihood, spline, posterior prediction, copula simulation, and policy interface. Use the global IEEE sequence and distinguish governing standards from analogies.

**Acceptance tests:** A second team can reproduce published metrics within tolerance. All equations and numerical examples pass. Artefacts are retained under approved model-governance policy.

## Recommended editing and model-development order

Perform P01 through P03 before code changes. Build individual-likelihood benchmark under P04. Establish offline and online separation in P05. Complete validation design in P06 before selecting the final architecture. Implement pricing and dependence only after core calibration succeeds. Complete governance and fairness before shadow deployment. Replace the appendix and publish references last.

Required reviewers include credit-risk owner, Bayesian statistician, ML engineer, independent model validator, financial modeller, treasury and pricing, IFRS 9 adviser, bank regulatory capital specialist, product and policy owners, fairness specialist, DPO, Kenyan counsel, security and SRE leads, and lender model-risk representatives.

## Pre-publication validation checklist

- All use cases, targets, and horizons are explicit.
- Input manifest has no duplicate engineered liquidity feature.
- Scaling approximation is benchmarked.
- Online scoring does not run MCMC.
- Calibration and uncertainty pass out-of-time tests.
- `PD_P` and `PD_Q` are separated.
- Copula simulation and family sensitivity pass.
- Economic, SPV, and regulatory capital are distinct.
- Explainability and policy reason codes reconcile.
- Fairness, monitoring, governance, and reproducibility artefacts exist.
- Equations render and numerical tests pass.

## Model approval scorecard and launch thresholds

Create a scorecard with minimum and target criteria for data sufficiency, label maturity, leakage, computational diagnostics, calibration, discrimination, uncertainty coverage, stability, fairness, explanation, latency, resilience, and business value. Criteria should be set before final model comparison. Each result records development, validation, and risk-acceptance views. A strong aggregate AUC cannot compensate for material calibration failure, leakage, or unsafe subgroup performance.

Use a staged approval. Research approval permits experimentation on governed data. Development approval freezes target, features, and candidate architecture. Validation acceptance closes critical findings. Shadow approval permits scores without customer effect. Limited-use approval permits bounded decisions and exposures. Full approval follows mature outcomes and operational evidence. Each stage has expiry and monitoring conditions.

Document limitations that remain after approval: sparse severe defaults, platform concentration, intervention feedback, unobserved rejections, market-regime change, telematics missingness, and absence of direct `PD_Q` calibration. Connect each limitation to usage constraint, buffer, manual review, data collection, challenger, or stop condition. This provides a more credible control than claiming the posterior absorbs every uncertainty.

## Portfolio-model and waterfall integration tests

Create a fixed interface from individual or cohort posterior outputs to D09 and D03. Specify exposure date, conditional horizon, marginal default probability, dependence regime, LGD distribution, recovery curve, prepayment, and scenario weight. Ensure the same default event is not counted both in marginal stress and an additive copula shock. Separate model-estimated dependence from management stress.

Use golden portfolios to test independent defaults, common marginal increase, dependence increase, delayed recovery, zero recovery, full recovery, and concentrated platform loss. Verify marginal rates, joint rates, loss distribution, cash timing, OC, reserve, early amortization, and tranche loss. Report whether senior protection is a scenario output and where it breaks.

Validate aggregation from driver to product, cohort, platform, geography, and SPV. Preserve driver-level joint exposure so three product defaults are not mistakenly treated as three independent obligors. Verify that policy interventions affect cash and future outcomes through explicit scenario or causal assumptions, not an arbitrary PD reduction.

## Independent validation work programme

The independent validator should reproduce data lineage and labels; challenge feature ownership; review priors and identifiability; replicate inference diagnostics; benchmark approximation; test calibration and uncertainty; evaluate temporal and cluster validation; challenge copula orientation and family; review pricing separation; test explanations; assess fairness and privacy dependencies; and verify online implementation. Validation should have access to code and data manifests without relying on developer-generated summaries.

Findings should be rated, owned, dated, and linked to approval conditions. A critical unresolved finding blocks use. High findings require closure or explicit risk acceptance by an authority independent of development. Medium and low findings remain in monitored action plans. Retesting evidence should be archived with the approved release.

## Definition of done

D06 is complete when the model's statistical claims, operational implementation, decision use, pricing role, dependence output, explanations, and governance can each be independently validated. Complexity must earn its place against simple challengers. No part of the paper may turn a statistical estimate into a legal rule, market measure, capital permission, or guarantee without separate evidence and authority.
