# Mwendo Pamoja Narrative Editorial Standard

## Editorial purpose

The root series is written for an intelligent public audience that may include drivers, founders, investors, bankers, insurers, regulators, data scientists, and engineers. Each paper must read as an argument and a story before it reads as a specification.

The reader should encounter the work in this order:

1. a recognisable human or market situation;
2. the microeconomic mechanism beneath that situation;
3. the failure of the conventional institutional response;
4. the Mwendo Pamoja design insight;
5. the mathematical or computational formulation;
6. a visual explanation;
7. the business and project-finance consequence;
8. the limits, assumptions, and evidence still required; and
9. a transition that invites the next paper.

Technical depth is retained. Definitions and controls are introduced at the moment the reader needs them instead of appearing as an opening wall of qualifications.

## Relationship to implementation documentation

The root papers explain why the platform should exist, how its economic and computational ideas fit together, and what the financing architecture makes possible. The companion controlled specifications define precise responsibilities, interfaces, tests, and conditions.

The root papers may use vivid language, hypotheses, scenarios, and innovative formulae. They must distinguish measured evidence from proposed mechanism and conditional model output. The controlled specifications remain the operational interpretation where narrative compression would otherwise create ambiguity.

## Canonical story arc

The recurring protagonist is the driver as a small operating business. Gross fare is not disposable income. Fuel, platform commission, insurance, maintenance, debt service, household sufficiency, and time create a fragile working-capital cycle. A small shock can remove the vehicle from service and make several obligations fail together.

Mwendo Pamoja responds by observing the operating cycle continuously, separating latent behavioural learning from explicit liquidity measurement, estimating default risk and uncertainty through a hierarchical Bayesian model, and applying a separate policy and compliance decision layer. Supportive interventions seek to preserve productive capacity before collections collapse.

The SPV translates that operating insight into institutional finance through eligibility, true sale, controlled accounts, subordination, overcollateralisation, reserves, concentration limits, and a waterfall. These mechanisms mitigate risk but do not guarantee an outcome.

## Canonical architecture

The visible architecture is:

~~~text
Raw telematics, trip, wallet, repayment, insurance, and macro events
                               |
                  Flink event and feature services
                       /                       \
          GRU and Transformer              Explicit Liquidity
          neural representation             Feature Path
                       \                       /
             Redundancy-controlled hierarchical
                    Bayesian underwriting
                               |
                Credit Policy and Compliance Gate
                               |
             Credit action, intervention, servicing,
                 SPV eligibility, and monitoring
~~~

The engineered variables CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved financial interactions belong only to the Explicit Liquidity Feature Path. Neural processing may observe governed raw sequences but does not receive those named engineered metrics as duplicate inputs.

## HLR mathematical standard

The full narrative model uses:

$$
\operatorname{logit}(p_i)=\eta_i,
$$

$$
\eta_i=
\alpha+a_{g[i]}+b_{p[i]}+c_{t[i]}
+\mathbf q_i^{\top}\boldsymbol\beta_z
+\widetilde{\mathbf h}_i^{\top}\boldsymbol\beta_h
+\boldsymbol\psi_i^{\top}\boldsymbol\gamma
+\mathbf m_i^{\top}\boldsymbol\delta.
$$

The explicit spline design is centred and QR-orthogonalised. The neural representation is residualised out of fold against the explicit design using ridge projection. Interactions obey strong heredity. Hierarchical effects are centred or constrained. Coefficient blocks receive separate grouped shrinkage. Calibration is estimated on a later validation period:

$$
\operatorname{logit}(PD_i^{\mathrm{cal}})
=\kappa_{p[i]}+s\eta_i,\qquad s>0.
$$

The explicit-only hierarchical model is the production fallback when the residual neural block has no stable incremental value.

## Financial standard

- Primary SPV capitalisation: USD-equivalent 9.00 million.
- Optional HoldCo facility: USD 1.00 million.
- Consolidated funding view: USD 10.00 million.
- Class A: USD-equivalent 6.75 million, 75 percent.
- Class B: USD-equivalent 1.35 million, 15 percent.
- Class C: USD-equivalent 0.90 million, 10 percent.
- Operating and waterfall currency: KES.
- Class A reference: compounded KESONIA in arrears plus \(m_A\), subject to contract.
- Customer variable lending rate: KESONIA plus \(K_{\mathrm{RBCP}}\).
- Minimum debt-note OC: 125 percent.
- Illustrative closing OC under the total-capital advance-rate convention: 148.15 percent.
- Cash reserve target: three months of defined Class A and B debt service.

The note coupon, customer rate, asset yield, expected loss, FTP charge, WACC or hurdle rate, and regulatory capital are never treated as the same number.

## Claim discipline

Prefer:

- “is designed to” instead of “guarantees”;
- “can detect” or “the pilot will test whether it detects” instead of unsupported lead-time certainty;
- “conditional on the scenario and assumptions” instead of “principal protected”;
- “comparative model-risk practice” instead of presenting foreign guidance as Kenyan law;
- “contractual or internal trigger” instead of “regulatory threshold” unless authority is cited; and
- “candidate dependence family” instead of assuming one copula is universally correct.

Qualifications should sit next to the relevant claim and preserve the rhythm of the paragraph. They should not turn every paragraph into a legal disclaimer.

## Citation standard

Use IEEE bracket citations after the sentence or paragraph they support. Prefer primary sources, official methodologies, standards, legislation, original research, and official vendor documentation. Secondary sources are used for context, market reaction, or accessible explanation.

Each paper ends with a Selected IEEE References section containing every cited source in the order in which it first appears in that paper. Mutable web sources include an access date. Inaccessible sources do not support substantive claims.

## Diagram standard

Diagrams should explain causality, sequence, or institutional structure. They should be dense enough to reward inspection while remaining readable when exported.

Each Mermaid diagram should:

- have a descriptive figure title in prose;
- use short node labels with line breaks where necessary;
- group related systems or institutions in subgraphs;
- show ownership and cash flow separately from data flow where possible;
- use consistent colour semantics;
- avoid unsupported claims in node labels;
- include a paragraph explaining how to read it; and
- be referenced from the surrounding narrative.

## Mathematical narration

Every important equation is introduced in plain language, displayed, and interpreted. Units, horizon, sign, and data cutoff are stated where they matter. Innovative formulae are retained as hypotheses or proposed measures when they are dimensionally coherent. Calibration status is made explicit.

The papers do not apologise for mathematical depth. They earn it by explaining what the mathematics reveals about a driver's lived economics, a lender's risk, an insurer's coverage, or an investor's cash flow.
