---
title: "Part 3: Joint Regulatory Capital Orchestration, Algorithmic Fairness, and Assistive Controls"
author: "Nevil Maloba"
date: "25 August 2026"
status: "Narrative white paper edition"
output:
  pdf_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
  word_document:
    pandoc_args: ["--lua-filter=mermaid-filter.lua"]
---

# 1. From prediction to permission: a Kenya-first control architecture

Parts 1 and 2 described a system that can observe, estimate, and simulate. Part 3 asks a more human question: **who is allowed to act, on whose behalf, and what record must remain after the action?** A posterior PD cannot grant an insurance holiday. A telematics alert cannot amend a loan. A copula cannot set regulatory capital. Those decisions belong to licensed institutions, contractual parties, accountants, governance bodies, and, where applicable, supervisors.

The architecture is Kenya-first. IFRS 9 and IFRS 17 apply according to the reporting entity and instrument [13], [14]. Basel standards inform prudential treatment through the implementing rules applicable to the banking partner [15]. Solvency II, EBA guidance, and U.S. ECOA or SR 11-7 appear only as comparative design references unless the relevant entity or jurisdiction makes them applicable. This distinction does not weaken the technology. It tells every partner which propositions are models, which are internal policies, which are covenants, and which are legal requirements.

The canonical sequence is:

~~~mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#EAF2F8", "primaryBorderColor": "#2E6F95",
  "secondaryColor": "#EAF7EE", "tertiaryColor": "#FFF4DB",
  "lineColor": "#526D82"
}}}%%
flowchart LR
    OBS["Consented events and records"] --> FEAT["Neural representation +<br/>Explicit Liquidity Features"]
    FEAT --> HLR["Calibrated HLR<br/>PD + interval + tail probability"]
    HLR --> GATE["Credit Policy and Compliance Gate"]
    GATE --> OWN{"Named decision owner"}
    OWN -->|Licensed lender| CREDIT["Credit action"]
    OWN -->|Licensed insurer| INS["Policy action"]
    OWN -->|Servicer / platform contract| OPS["Operational intervention"]
    OWN -->|SPV documents| PORT["Purchase, sweep or distribution control"]
    CREDIT --> REC["Notice + reason + consent + ledger + challenge"]
    INS --> REC
    OPS --> REC
    PORT --> REC
~~~

# 2. Bank-counterparty accounting and prudential integration

## 2.1. IFRS 9 Impairment Pipeline under Joint Tail Distress

The core mandate of IFRS 9 is the forward-looking recognition of Expected Credit Losses before losses are realized in the income statement. The Expected Credit Loss (ECL) model under IFRS 9 has reshaped the way entities manage and report credit risk, shifting from a backward-looking incurred loss model to a more proactive, forward-looking approach [7]. ECL under IFRS 9 estimates credit losses using PD, LGD, and EAD across three stages. Stage 1 accounts for 12-month ECL, while Stages 2 and 3 account for Lifetime ECL [8]. In a gig-economy portfolio characterized by extreme short-term volatility, relying on 30-day past-due metrics as the primary SICR trigger is operationally catastrophic. A driver can transition from fully performing to default-cascade-complete within 20 days of a fuel shock, entirely within the 30-day past-due window that would first flag the deterioration under a lagging threshold approach. The continuous telemetry pipeline allows the bank to preemptively shift assets across IFRS 9 impairment stages before a cash flow interruption occurs.

The Bayesian engine does not rewrite IFRS 9. The financial-asset holder's approved ECL methodology consumes relevant, reasonable, supportable, forward-looking evidence. The following mapping is an operating design:

- **Stage 1, 12-month ECL:** The exposure has not experienced a Significant Increase in Credit Risk under the approved framework. Neural state, explicit liquidity features, contractual performance, and macro scenarios may inform the estimate. CFA is an Explicit Liquidity Feature, not part of the GRU, and 0.6 is not a universal accounting threshold.

  $$\text{ECL}^{(\text{Stage 1})} = \text{PD}_{ij}^{(\text{12M})}(\boldsymbol{\Phi}_{it}) \times \text{LGD}_{ij}(v_t) \times \text{EAD}_{ij}$$

- **Stage 2, lifetime ECL after SICR:** The asset holder compares credit risk at the reporting date with credit risk at initial recognition using quantitative, qualitative, forward-looking, and backstop evidence. A twofold lifetime-PD movement may be one rebuttable quantitative indicator. CFA and Earnings Velocity enter through the Explicit Liquidity Feature Path; the GRU supplies only the permitted sequence representation.

  $$
  \mathrm{SICRScore}_{i,t}
  =
  g\left(
  \frac{PD_{i,t}^{\mathrm{life}}}{PD_{i,0}^{\mathrm{life}}},
  \Delta\mathrm{rating}_{i,t},
  \mathrm{arrears}_{i,t},
  \mathrm{qualitative}_{i,t},
  \mathrm{macro}_{t}
  \right).
  $$

  Upon an approved Stage 2 transition, the reporting entity recognises lifetime expected credit losses, measured as the applicable probability-weighted present value of cash shortfalls over the expected life. For a 30-day microloan, the 12-month and lifetime horizon can cover the same remaining contractual period, but revolving facilities require the entity's expected-life and exposure methodology, including drawdown and behavioural evidence.

- **Stage 3, credit-impaired:** Credit-impaired status follows the applicable default and impairment evidence. A single missed payment may be relevant but is not declared an automatic universal Stage 3 trigger. Interest revenue is calculated on the net carrying amount for credit-impaired financial assets as required by the applicable treatment.

- **Dynamic LGD:** LGD may depend on contractual collection routing, cure, recovery cost, recovery lag, policy refund rights, collateral, platform continuity, and calibrated Earnings Velocity. Mwendo Pamoja does not "garnish" earnings by unilateral operational control. Any deduction requires contractual and legal authority. Prudential floors depend on the exposure class, approach, and implementing rules; no 30%-45% range is asserted here without the banking partner's classification.

## 2.2. Basel prudential treatment as a bank-owned workstream

The banking partner determines whether exposures use a standardised or authorised IRB approach under applicable implementation. IFRS 9 allowance and prudential expected-loss treatment interact, but accounting provisions should not be described simply as "absorbing EL into pricing." The following formula is an analytical reference, not a claim that the SPV or platform may use A-IRB.

The Basel IV regulatory asset correlation function for retail exposures (CRE31 formula) is PD-dependent:

$$
R
=
0.03\frac{1-e^{-35PD}}{1-e^{-35}}
+0.16\left(
1-\frac{1-e^{-35PD}}{1-e^{-35}}
\right).
$$

The relevant asset-class formula, PD definition, LGD, EAD, maturity, floors, scaling, and output-floor phase-in must be confirmed by the bank. No gig-portfolio range is treated as regulatory input before classification.

The capital requirement $K$ per unit of EAD is:

$$
K_{\mathrm{cap}}
=
LGD
\left[
\Phi\left(
\frac{\Phi^{-1}(PD)}{\sqrt{1-R}}
+
\sqrt{\frac{R}{1-R}}\Phi^{-1}(0.999)
\right)
-PD
\right].
$$

where $\Phi$ denotes the standard normal CDF and the 0.999 quantile reflects the Basel 99.9% one-year confidence level. Risk-Weighted Assets are then $\text{RWA} = K \times 12.5 \times \text{EAD}$, with the Basel IV **72.5% output floor** applying as a minimum relative to the Standardised Approach RWA. This output floor is the most significant Basel IV change for portfolios using Advanced IRB: internal models cannot reduce RWA below 72.5% of the Standardised Approach, limiting the capital relief from sophisticated internal PD estimation.

**The copula bridge:** The prescribed prudential formula and the institution's economic-capital stress model serve different purposes. A candidate Clayton model can inform concentration, tail stress, limits, and the SPV waterfall. It does not entitle the bank to replace prescribed correlation, alter \(R\), claim capital relief, or prove an intervention effect. Any use in prudential modelling requires the bank's approved governance and supervisory process.

**PSI in model governance:** Weekly PSI and other drift metrics can support the bank's monitoring plan. A threshold of 0.25 is an internal convention or contractual trigger. It does not automatically require regulatory notification, model recertification, or suspension of IRB calculations under SR 11-7 or Basel. The bank's approved change policy determines escalation after the cause and performance impact are assessed.

**Currency risk:** The canonical SPV case is funded and serviced in KES, with USD used for headline reporting. The 130 KES/USD rate is an illustrative translation input, not a peg. If a USD note is issued against KES receivables, a forecast and excess KES reserve do not hedge it. The parties need an executed hedge or explicit unhedged loss allocation, with counterparty, collateral, tenor, basis, and break-cost treatment.


# 3. Insurer accounting and capital interfaces

The licensed insurer, not Mwendo Pamoja by default, maps policy cash flows into IFRS 17 and its applicable insurance-capital regime. If Mwendo Pamoja later becomes a licensed intermediary or risk carrier, that role requires its own analysis. Solvency II is presented as a comparative framework for a European-regulated carrier, not as Kenya's insurance-capital law.

## 3.1. IFRS 17 Accounting Protocols for Dynamic UBI

IFRS 17 establishes the accounting for insurance contracts within scope [14]. The insurer determines whether the Premium Allocation Approach is eligible for a group, including the coverage-period and material-difference criteria. The platform can supply exposure and policy-service data; it cannot elect the accounting method for the carrier.

### 3.1.1. The Building Block Approach (BBA) as Regulatory Backstop

Where an insurer validly applies the Premium Allocation Approach, the general measurement model is not described as an automatic backstop that the platform can trigger. The insurer assesses eligibility and the required measurement under IFRS 17. Under the general model, measurement includes probability-weighted fulfilment cash flows, discounting, a risk adjustment for non-financial risk, and the contractual service margin where applicable [3], [4].

Three design questions determine whether the simplified narrative remains appropriate:

- **1. Onerous Contract Identification:** IFRS 17 strictly prohibits masking loss-making policies within profitable portfolios. Even under PAA, groups of contracts must be monitored, and **Onerous Contracts** (groups of policies where the expected future cash flows and claims exceed the remaining premium, i.e., where expected FCF exceeds the Liability for Remaining Coverage (LRC)) must be identified and loss recognized immediately [5]. To test whether a cluster $j$ of drivers constitutes an onerous group, the Insurtech cannot rely on PAA; it must invoke the first three BBA blocks to calculate true FCF:

  $$\text{If} \quad \mathbb{E}[\text{FCF}_j] > \text{LRC}_j \implies \text{Onerous Contract Group}$$

  Model outputs can supply evidence to the insurer's fulfilment-cash-flow and onerous-group process, but the insurance actuarial model owns claim frequency, severity, expenses, lapse, discounting, risk adjustment, coverage units, and grouping. A credit PD or driver-liquidity shock is not substituted directly for an insurance-claim forecast.

- **2. Multi-year policy assessment:** A multi-year group loses the automatic short-coverage route but may still qualify if the insurer demonstrates that PAA measurement would not materially differ from the general model. Telematics volatility and a candidate copula do not decide that test.

- **3. Risk adjustment evidence:** A candidate dependence model may inform the insurer's non-financial risk analysis, subject to actuarial validation and the insurer's disclosed confidence-level or cost-of-capital method. The credit-product copula does not automatically set the IFRS 17 risk adjustment.

## 3.2. Solvency II as a comparative internal-model case

Where a carrier is actually subject to Solvency II, it calculates SCR under the applicable standard formula or approved internal model. Mwendo Pamoja is not assumed to be that carrier.

The Solvency II standard formula aggregates prescribed risk modules and dependencies under its own calibration. A separate economic-risk analysis may test whether the platform's insurance and credit exposures exhibit tail behaviour not captured by a simpler dependence assumption. A Clayton copula is one candidate for lower-tail dependence, not a correction that can replace the insurer's prescribed calculation or prove that the standard formula understates this portfolio.

An approved partial internal model cannot be assumed or overridden by the platform. A carrier would need governance, data, use-test, calibration, validation, documentation, and supervisory approval. No capital relief is claimed for an intervention until the carrier and supervisor accept the evidence. For the current Kenya-first design, the copula remains an economic stress tool and the licensed insurer owns capital treatment.


# 4. Algorithmic Equity and Fairness Frameworks
## 4.1. The Structural Bias Risk in Deep Temporal Architectures

Continuous underwriting introduces a serious ethical and conduct risk: a model may reproduce historical disadvantage through geography, platform, device, work schedule, vehicle, road quality, missingness, or labels. The affected Kenyan populations, protected attributes, and legal tests must be identified from applicable law and institutional policy. U.S. ECOA is a comparative example, not an assumed Kenyan cause of action.

The risk is structural, not incidental. The GRU's hidden state $\mathbf{h}_t^{\text{GRU}}$ will encode whatever patterns are predictive of default in the training data, including patterns driven by systemic infrastructural inequality rather than individual creditworthiness. No amount of removing explicit demographic features from the input resolves this if the telematics features (geohash, circadian fatigue accumulation, average trip distance) serve as effective demographic proxies. The solution must be embedded in the training objective itself [9].

## 4.2. The Mathematical Constraint: Equalized Odds

Equalized odds is retained as one diagnostic and possible optimisation objective, not a guarantee or a universal legal standard. Let \(A\) be a lawfully held audit attribute, \(Y\) a carefully defined observed outcome, and \(\hat Y\) the decision. Protected attributes should not be inferred from geohash merely to complete a formula; the fairness data design requires lawful basis, access separation, minimisation, and an impact assessment.

A model satisfies Equalized Odds if its approval decisions are independent of the protected attribute $A$, conditional on the true outcome $Y$. Formally, both the True Positive Rate (TPR) and the False Positive Rate (FPR) must be identical across all protected groups:

$$P(\hat{Y} = 1 \mid Y = y, A = 1) = P(\hat{Y} = 1 \mid Y = y, A = 0), \quad \forall y \in \{0, 1\}$$

This constraint has two components with distinct policy implications [10]:

1. **Equal Opportunity (Equal TPR):** A creditworthy driver from a marginalized background ($A = 1$) must have the same mathematical probability of being approved for a revolving credit line as a creditworthy driver from a non-marginalized background ($A = 0$), conditional on both being genuinely creditworthy. This prevents the model from systematically denying credit to creditworthy marginalized drivers due to geohash-correlated proxy features.

2. **Equal FPR:** A non-creditworthy driver from a marginalized background must have the same probability of being *incorrectly* approved as a non-creditworthy driver from a non-marginalized background. This prevents the inverse bias: a model that incorrectly approves marginalized drivers at higher rates (a patronizing form of bias that leads to higher default rates in that group and subsequent portfolio-wide tightening).

## 4.3. Optimization Integration and Continuous Monitoring

Enforcing Equalized Odds creates a trade-off with absolute predictive accuracy (AUC-ROC), because the model is mathematically constrained from exploiting highly predictive but biased proxies. This accuracy-fairness frontier is not a binary choice: the fairness regularization parameter $\lambda_{\text{fair}}$ controls the operating point on the frontier.

The Insurtech operationalizes this by adding a **Maximum Mean Discrepancy (MMD) regularization penalty** to the neural network's training loss function:

$$
\mathcal L_{\mathrm{total}}
=
\mathcal L_{\mathrm{predictive}}
+\lambda_{\mathrm{fair}}
\mathcal D_{\mathrm{fair}},
$$

where \(\mathcal D_{\mathrm{fair}}\) may be an MMD-based representation discrepancy or another approved differentiable surrogate. TPR and FPR are rates rather than raw distributions, so an MMD term must specify which conditional score or representation distributions it compares.

A Bayesian analysis can express uncertainty around subgroup TPR, FPR, calibration, or outcome gaps when the sampling and model assumptions are appropriate. A point estimate can hide uncertainty, especially in small groups. A statement such as “the posterior probability that a defined TPR gap is below 3 percent is 95 percent, conditional on the data and model” is an analytical result, not a declaration of legal compliance. It must be accompanied by sample size, prior sensitivity, label quality, missingness, and practical impact.

**Continuous fairness monitoring on Flink:** The Flink pipeline computes metrics continuously and provides XAI (Explainable AI) governance:

1. **Explanations:** SHAP, local surrogates, explicit feature contributions, and counterfactual tests help diagnose model behaviour. They do not prove the absence of proxies.
2. **Outcome ratios:** DIR is monitored with confidence intervals and sample-size disclosure. The U.S. four-fifths convention may be used as a diagnostic benchmark, not a universal legal safe harbour or violation threshold.
3. **Conditional performance:** Calibration, TPR, FPR, false restriction, price, limit, intervention, complaint, and cure outcomes are measured by relevant groups and intersections.
4. **Drift:** PSI and data-quality measures trigger investigation. Drift is not itself unfairness and must be linked to outcomes and model pathways.


# 5. Operationalizing the Assistive Ecosystem
## 5.1. From Punitive to Non-Punitive Underwriting

The purpose of detecting a joint cascade early is not merely to measure it. It is to create time in which an authorised party may choose a less destructive path. The transition can be described simply: detect stress, diagnose its likely cause, offer an approved intervention, observe the result, and revise the decision. Collections and impairment recognition remain necessary when facts require them; assistive design must not become delayed recognition by another name.

An early intervention may cost less than an avoidable default and may preserve insured, productive time, but that is a hypothesis for cohort evidence. The evaluation must include the intervention cost, adverse selection, repeat use, modification accounting, driver welfare, opportunity cost, cure durability, ECL, and SPV cash timing. The ethical and financial case becomes stronger when both are measured rather than asserted.

When calibrated risk and uncertainty approach an action threshold, the Credit Policy and Compliance Gate selects only actions authorised for the product and counterparty. The following interventions are product hypotheses. Each requires a named owner, driver communication and consent where required, duration, exit rule, cost bearer, accounting treatment, fairness monitoring, and experimental evidence.

| Intervention | Decision owner | Precondition | Primary evidence |
|---|---|---|---|
| Premium schedule support | Licensed insurer and finance provider | Policy wording and finance terms permit it | Cover continuity, claims, modification and cash-flow analysis |
| Micro-reward bridge | Licensed lender plus contracted platform | Platform can lawfully offer work without discriminatory allocation | Driver take-home, arrears cure, complaints and outcome test |
| Fatigue mitigation | Platform or safety owner | Verified safety basis and lawful routing authority | Safety benefit, income impact, false restriction and appeal |
| ZEV routing support | Platform | Verified charger and range data | Uptime, income, data quality and geographic fairness |
| Margin compression support | Lender and funder | Contract and funded support budget | NIM, affordability, SPV cash flow and allocation of loss |

## 5.2. The Financial Safety Net Interventions

- **Intervention 1: Dynamic Premium Holidays**
  A proposed trigger combines calibrated IPF risk with an acute decline in Explicit Liquidity Features such as Earnings Velocity, not a wallet metric hidden inside the GRU. A pause, extension, repricing, or continued cover occurs only if the insurer and finance provider approve it under the contracts. The model does not assume that stress will revert to the historical mean.

  Unearned premium, coverage, policy liability, receivable modification, and SPV eligibility continue to evolve under the actual terms. The cost is allocated to Class C only if the SPV documents and funded model provide for it. The intervention objective is to preserve viable cover and work, not to declare the lender insulated.

- **Intervention 2: Micro-reward bridge and consensual restructuring**
  A bridge may be considered when approved arrears, liquidity, and viability criteria indicate that a short, funded opportunity could restore the payment path. The lender owns any restructuring. A contracted mobility platform may offer an opt-in incentive, additional earning opportunity, or sponsor-funded reward under transparent allocation rules. Any deduction from the resulting fare requires prior authority, a sufficiency control, clear communication, and a product-ledger receipt. The design must not reserve desirable work exclusively for distressed borrowers in a way that unfairly shifts income or safety risk to other drivers.

  The outcome must be measured rather than pre-written. A bridge may support cure, but it does not automatically avoid Stage 3 or change the accounting evidence. Preferential route allocation can affect other workers and may create safety, fairness, labour, platform, and conduct issues. The platform must opt in as the routing owner.

- **Intervention 3: Fatigue Mitigation Routing**
  Triggered by validated safety signals and operating rules, not a latent "desperation" label. A financial state must not be inferred from driving hours alone.

  A platform may test a cooling-off, rest, or alternative-task option if it has authority and evidence. The test must measure collision proxy outcomes, actual claims where available, take-home income, false restrictions, and worker choice. No IFRS 17 or onerous-group result is guaranteed.

- **Intervention 4: ZEV-aware work and charging support**
  For drivers transitioning to zero-emission vehicles, charging availability, queueing, range, charger compatibility, and trip geography can affect productive time. A prolonged charging interruption during peak demand can reduce fare income and create a new operating-cost pattern that older vehicle-finance models may not capture.

  Where lawful and contractually available, a context service can use verified charger location, compatibility, availability, price, queue, range, trip, and time data to recommend charging windows or work zones. The mobility platform remains the routing owner, and the driver should retain meaningful choice. The pilot measures charger-data quality, actual wait time, income, safety, geographic access, battery state, false recommendations, and effects on other drivers. The service seeks to reduce avoidable downtime; it cannot ensure income continuity or repayment.

- **Intervention 5: Funded rate-shock support**
  The governed benchmark service observes KESONIA, while treasury scenarios and the Transformer context branch can assess the wider economic regime. A contractual reset can affect driver affordability, but the timing and magnitude depend on product terms, notices, floors, caps, and lender policy. The platform does not characterise every lawful benchmark transmission as predatory or treat a model alert as authority to alter a contract.

  During a funded support period, the lender may hold or cap a reset, use an agreed subsidy, or restructure the product. The model then shows who absorbs the difference and whether SPV eligibility, yield, ECL, and waterfall change. Class C does not automatically pay the cost, and senior notes are not mathematically insulated until the cash-flow model demonstrates it.


# 6. Supervisory Auditing of Behavioral Interventions

The implementation of behavioral interventions (Dynamic Grace Periods, Micro-Reward Bridging, Fatigue Mitigation Routing, and ZEV Smart Routing) fundamentally shifts the platform from a passive observer of default cascades into an active, protective financial safety net. However, within a strictly regulated banking environment, these algorithmic interventions introduce profound compliance risks.

Automated changes to payment timing, limits, routing, or policy service can affect customer rights, accounting, credit classification, eligibility, and fairness. Kenya-first legal and accounting analysis governs the production design. EBA and ECOA materials are comparative references for partners subject to them, not direct Kenyan mandates.

## 6.1. Forbearance vs. Assistive Interventions (IFRS 9 and EBA Guidelines)

### 6.1.1. The Regulatory Threat: "Shadow Forbearance"
Under the EBA's Guidelines on the application of the definition of default, and the overarching IFRS 9 Expected Credit Loss (ECL) framework, a critical distinction exists between standard contract modifications and **Forbearance**.

Forbearance commonly concerns a concession granted because a borrower is experiencing financial difficulty, but definitions and consequences depend on the applicable framework and institutional policy. Automated grace periods can create “shadow forbearance” risk if they delay recognition without changing the underlying condition. The lender must therefore classify, report, and provision from the facts, with clear modification, cure, and probation rules. Potential supervisory consequences should be stated only under an applicable Kenyan authority, not imported from a foreign framework as an automatic penalty.

### 6.1.2. The Architectural Solution: Proactive vs. Reactive Classification
The intervention register distinguishes preventive support, modification, concession due to financial difficulty, cure, and default. Timing is relevant but not conclusive. An ERP records the classification and evidence; it does not mathematically prove the legal or accounting conclusion.

1. **Proactive support:** A validated operational or liquidity signal may justify offering information, a funded incentive, or another action already permitted by the contract before arrears. The classification still depends on the driver's condition, the nature of the concession, and the applicable accounting and regulatory framework. An offline charger does not by itself establish financial distress, nor does calling an action proactive prove that it is outside forbearance analysis.
2. **Forbearance Interventions (Reactive):** Interventions triggered *after* a missed split-fare repayment (such as the Micro-Reward Bridge initiated at IFRS 9 Stage 2 or Stage 3).

### 6.1.3. Accounting integration and discounted-cash-flow testing
For a modified financial asset, the reporting entity applies its approved IFRS 9 modification, derecognition, EIR, and credit-impaired analysis. For a partner subject to EBA default rules, the diminished-financial-obligation calculation is a separate prudential test.

No universal IFRS 9 "1% rule" is used in this paper. Any EBA quantitative threshold is applied only by an institution within scope and with the complete qualitative default criteria. The system calculates the present-value difference without converting the result into an automatic accounting conclusion:

$$
\Delta NPV
=
\frac{
NPV_{\mathrm{original}}-NPV_{\mathrm{modified}}
}{
NPV_{\mathrm{original}}
},
$$

using the appropriate original EIR and cash-flow definitions. A micro-reward bridge can change timing even without principal forgiveness, so \(\Delta NPV\) is not assumed to be zero. The accounting owner decides modification, derecognition, staging, and interest treatment.

## 6.2. Algorithmic Fairness and Fair Lending (ECOA/Disparate Impact)

### 6.2.1. The Regulatory Threat: Algorithmic Redlining
In jurisdictions governed by the Equal Credit Opportunity Act or related fair-lending doctrines, behavioural interventions can create discrimination risk when a facially neutral design produces unjustified adverse effects for a protected class. For this Kenya-first platform, ECOA remains comparative material. Kenyan law, product duties, data-protection principles, contracts, and partner policy determine the production analysis.

Suppose the architecture offers valuable bridge opportunities more often to men in affluent Nairobi areas while imposing limit reductions more often on women in peri-urban Kisumu. That pattern demands investigation of exposure, need, data coverage, labels, product eligibility, platform behaviour, model pathways, policy rules, and outcomes. Excluding gender or ethnicity from decision inputs does not remove proxy risk: geography, shift time, device quality, vehicle, or platform can retain association. The strength and legal meaning of that association must be measured rather than assumed perfect.

### 6.2.2. The Architectural Solution: Less Discriminatory Alternative (LDA) Testing
To govern this, the Mwendo Pamoja architecture embeds a continuous Fair Lending validation engine directly into the Azure MLflow pipeline.

The Model Risk Committee uses a locally applicable fairness and data-protection framework. U.S. less-discriminatory-alternative analysis can be a comparative technique. Before deployment, the model is evaluated on lawfully governed audit data, with access separated from production decisioning where appropriate.

The system continuously calculates the **Disparate Impact Ratio (DIR)** for every specific behavioral intervention:
$$DIR_{Intervention} = \frac{P(Intervention | \text{Unprivileged Group})}{P(Intervention | \text{Privileged Group})}$$

If a diagnostic threshold is breached, release is blocked pending review. The team cannot "prove fairness" with SHAP or assume an apparently objective variable is harmless. It must investigate data, labels, features, model, policy, partner process, alternatives, outcome trade-offs, and driver impact.

## 6.3. Continuous control monitoring and reporting adapters

Transparency requires a complete internal intervention record before it requires a particular message standard. The canonical record contains:

- decision, trigger, model, feature, data-quality, and policy versions;
- calibrated PD, uncertainty, explicit reason codes, and overrides;
- decision owner, authority, driver communication, consent status, and challenge path;
- original and modified contractual cash flows;
- ECL, eligibility, waterfall, and accounting assessments;
- fairness and outcome-monitoring fields; and
- maker-checker approval, integrity evidence, and retention classification.

ISO 20022 message definitions and XBRL taxonomies can be implemented as **adapters** where a bank, payment rail, supervisor, or filing regime specifies them [16]. Governed, partner-specific adapters allow the canonical intervention record to travel through an approved schema while preserving its source, meaning, ownership, reconciliation status, and review history.

# 7. Conclusion

The gig economy changes the timing and observability of labour, cash flow, insurance exposure, and credit risk. The cascade in Part 1 is a plausible path created by shared dependencies, not a deterministic fate. The value of the architecture lies in making those dependencies visible early enough for a licensed and accountable party to choose a proportionate action.

The architecture developed across this series constitutes a mathematically rigorous, computationally scalable, and regulatorily compliant alternative to the legacy paradigm:

- **Part 1** located the shared productive asset and mapped how three products can transmit stress.
- **Part 2a** established event-time, point-in-time, and feature-ownership controls for neural and explicit paths.
- **Part 2b** calibrated a redundancy-controlled HLR and framed Clayton as one candidate for lower-tail dependence.
- **Part 3** separated model inference from policy permission, assigned decisions to the lender, insurer, platform, servicer, SPV, and accounting owners, and preserved foreign frameworks as comparative rather than invented local law.

The target system has six testable properties: calibrated posterior risk with uncertainty; partial pooling for sparse cohorts; explicitly owned liquidity features; a separately validated dependence model; a Credit Policy and Compliance Gate with named decision owners; and interventions whose human and financial outcomes are measured. It earns the description "assistive" only when the evidence shows that it preserves viable work, respects rights, avoids unfair restriction, and improves portfolio outcomes.



```{=latex}
\clearpage
```

## References

[1] Casualty Actuarial Society (CAS), "IFRS 17 and PAA Eligibility," [Online]. Available: https://www.casact.org/sites/default/files/2021-02/IFRS_17_PAA_Eligibility.pdf

[2] Grant Thornton, "Applying the Premium Allocation Approach under IFRS 17," [Online]. Available: https://www.grantthornton.global/en/insights/ifrs-17/applying-paa/

[3] PwC, "IFRS 17 in a box," [Online]. Available: https://www.pwc.com/gx/en/services/audit-assurance/ifrs-reporting/ifrs-17-in-a-box.html

[4] KPMG, "IFRS 17: General Measurement Model (BBA)," [Online]. Available: https://kpmg.com/xx/en/home/services/audit/ifrs-17.html

[5] BDO, "Onerous Contracts under IFRS 17," [Online]. Available: https://www.bdo.global/en-gb/services/audit-assurance/ifrs/ifrs-17-insurance-contracts

[6] Actuarial Society of South Africa, "Assessing PAA Eligibility for Multi-Year Contracts," [Online]. Available: https://www.actuarialsociety.org.za/

[7] Uniqus, "Expected Credit Losses under IFRS 9," [Online]. Available: https://uniqus.com/expected-credit-losses-under-ifrs-9/

[8] ElysianNXT, "ECL Under IFRS 9: 3-Stage Model, PD, LGD and EAD Explained," [Online]. Available: https://www.elysiannxt.com/what-is-ecl-under-ifrs-9/

[9] P. N. et al., "A survey on Bias and Fairness in Machine Learning," *arXiv*, arXiv:2106.11978, 2021. [Online]. Available: https://arxiv.org/abs/2106.11978

[10] A. M. et al., "The Costs of Fairness in Machine Learning," *arXiv*, arXiv:1808.06454, 2018. [Online]. Available: https://arxiv.org/abs/1808.06454

[11] Board of Governors of the Federal Reserve System, "Supervisory Guidance on Model Risk Management," SR 11-7, 2011. [Online]. Available: https://www.federalreserve.gov/supervisorypubs/sr-letters/sr1107a1.pdf

[12] Consumer Financial Protection Bureau (CFPB), "Equal Credit Opportunity Act (ECOA) Baseline Review Module," [Online]. Available: https://www.consumerfinance.gov/compliance/supervision-examinations/equal-credit-opportunity-act-ecoa-baseline-review-module/

[13] IFRS Foundation, "IFRS 9 Financial Instruments." [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/. Accessed: Aug. 25, 2026.

[14] IFRS Foundation, "IFRS 17 Insurance Contracts." [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/. Accessed: Aug. 25, 2026.

[15] Basel Committee on Banking Supervision, "Calculation of RWA for credit risk: IRB approach," *Basel Framework*, CRE31. [Online]. Available: https://www.bis.org/basel_framework/chapter/CRE/31.htm. Accessed: Aug. 25, 2026.

[16] International Organization for Standardization, "ISO 20022 message definitions." [Online]. Available: https://www.iso20022.org/iso-20022-message-definitions. Accessed: Aug. 25, 2026.

[17] Republic of Kenya, *Data Protection Act, 2019*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24. Accessed: Aug. 25, 2026.
