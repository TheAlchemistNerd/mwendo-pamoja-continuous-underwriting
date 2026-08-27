# Mwendo Pamoja Narrative Reconstruction Ledger

## Purpose and edition boundary

This ledger records the narrative reconstruction completed on 25 August 2026. The ten public-facing narrative editions are now organized between `whitepapers/mwendo-pamoja/parts/` and `docs/transaction/`. They are intended to support a long-form white paper, a serialized Substack publication, technically serious LinkedIn articles, investor reading, and partner discussion. They preserve the original ambition: begin with a recognisable driver or institutional problem, reveal its microeconomics, build the computational response, and then connect the response to insurance, embedded finance, and project-finance structure.

The coordinated legal, implementation, accounting, data, and model-governance editions created before this reconstruction remain available in `docs/controlled-specifications/`. Those files were not discarded or silently overwritten. They are companion specifications whose job is to define controls, ownership, interfaces, tests, contractual dependencies, and qualification language. The narrative papers explain the idea and its significance; the controlled specifications describe how it must be bounded in implementation.

The original source corpus also remains in the dated backup:

`C:\Users\Nevo\Downloads\insuretech & embedded finance\revision_backups\2026-08-24_pre_coordinated_rewrite`

That backup contains the original `question drafts`, `regulatory_tech_kesonia`, and `revised_with_sources` folders. No backup file was edited during the narrative reconstruction.

## Backup integrity record

The ten source-paper SHA-256 values recorded at final validation are:

| Source paper | SHA-256 in dated backup |
|---|---|
| Strategic Partnership Memorandum | `A5C95DEE28EF38EC99EEC67697B14A2DBD16DE78B90ABBBAD999729AF2C3514B` |
| HoldCo Venture Capital Technical Pitch | `1AE90A9497BE2CDEBA5FF18E9641C85CC2639BF782B0D246D31B1F7F2458A6DA` |
| SPV Financial Term Sheet | `CC1763277FFE59AB74580AC7DD6A05F62A1052668A012C32819A04465A4A2242` |
| Part 1: Product Architecture and Cascades | `3C6D51591B06481A45057548F9929891C9A4EF5023C21441254EF476C681978F` |
| Part 2a: Deep Temporal Representation and Feature Engineering | `15794A905B5882E9813FEAA11CD1DCAB796118C214111D595B22415E09E2A7DD` |
| Part 2b: Bayesian Underwriting and Asymmetric Copulas | `010CEAD5E1EB4BC5F61B423D26F99752A98A23CF476FB99668D2C4767AB41ED3` |
| Part 3: Regulatory Orchestration and Interventions | `A0A736C05A6D49ED005F7937479D6ECE0C9276D6F059AEEA47239BD41FAF2115` |
| Part 4: Enterprise ERP and Telemetry | `F2BFA4133BC2FB94725BD67203842D89B32ADF860B71D4B22DE70D494D147958` |
| Part 5: KESONIA Pricing and Capital Orchestration | `AB13A442B77310931DDA5EF12B220FBE2FB6D9DC7CE2728D9E7B06CE52E7950D` |
| Part 6: Implementation Roadmap and Execution | `1D9B26530CA84FC606A155FCBEF48B8FC5D010AB1D8D87EE8A08509861883173` |

The backup also contains `glossary.md`. The glossary was excluded from this narrative reconstruction.

## What was retained

The reconstruction did not flatten the work into a conventional compliance memorandum. It retained and, where useful, expanded:

- the driver as a small operating business rather than a generic retail borrower;
- the correlated cash-flow cascade linking earnings, fuel, insurance, credit, vehicle continuity, and platform access;
- the explicit financial feature formulae, temporal models, Bayesian hierarchy, copula exploration, and stochastic-calculus appendix;
- the architecture diagrams, event and decision sequences, SPV relationships, accounting flows, and implementation dependencies;
- the distinction between insurtech product mechanics and embedded-finance credit mechanics;
- long-form explanatory passages that introduce mathematics through a lived or institutional problem; and
- dense IEEE-style references, strengthened with official and primary sources where the earlier citation could not carry the claim made around it.

Innovative constructs were treated as candidate mechanisms to be calibrated, validated, and governed, not removed merely because they are novel.

## Canonical consistency decisions

### Feature and decision architecture

The canonical flow is:

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

The old label “Tabular Bypass” has been retired in the public papers. CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilisation, and approved financial interactions belong to the Explicit Liquidity Feature Path. The neural branch may observe governed raw sequences, but it does not receive duplicate versions of those named engineered metrics. The Credit Policy and Compliance Gate is downstream of underwriting and is not described as another predictive feature path.

### HLR redundancy and multicollinearity controls

The primary underwriting equation is retained, but its design is now explicit about redundancy control:

$$
\operatorname{logit}(p_i)
=
\alpha+a_{g[i]}+b_{p[i]}+c_{t[i]}
+\mathbf q_i^{\top}\boldsymbol\beta_z
+\widetilde{\mathbf h}_i^{\top}\boldsymbol\beta_h
+\boldsymbol\psi_i^{\top}\boldsymbol\gamma
+\mathbf m_i^{\top}\boldsymbol\delta.
$$

The explicit liquidity spline design is centred and QR-orthogonalised. The neural bottleneck is cross-fitted and ridge-residualised against the explicit design before entering the HLR. Interactions obey strong heredity, hierarchy effects are constrained or centred, and each coefficient block receives its own shrinkage scale. Candidate terms must demonstrate stable out-of-time incremental value. If the neural residual block does not add stable calibration or decision value, the explicit-only hierarchical model is the production fallback. This design reduces avoidable duplication without pretending that statistical orthogonalisation eliminates every form of economic dependence.

### Finance, accounting, and pricing

The primary SPV is USD-equivalent 9.00 million, comprising Class A of 6.75 million, Class B of 1.35 million, and Class C of 0.90 million. The optional HoldCo facility is USD 1.00 million, producing a USD 10.00 million consolidated funding view without mixing HoldCo cash flow into the SPV waterfall. Operating and waterfall cash flows are denominated in KES.

Compounded KESONIA in arrears plus a negotiated tranche margin is the canonical Class A reference basis, subject to contract. KESONIA plus the risk-based credit premium is the customer floating-rate construct under the relevant framework. Those rates remain distinct from asset yield, expected loss, funds-transfer pricing, regulatory capital, and the investor hurdle rate. IFRS 9, IFRS 17, contractual covenants, internal policy, statistical monitoring conventions, and comparative foreign guidance are also kept distinct.

## Paper-by-paper reconstruction

| Paper | Narrative reconstruction and consistency repair |
|---|---|
| Strategic Partnership Memorandum | Restored the driver-centred investment story, connected the operating cascade to institutional roles, retained the financing thesis, and made legal and performance outcomes conditional on contracts, evidence, and model results. |
| HoldCo Venture Capital Technical Pitch | Restored the venture narrative and technical ambition, qualified external fintech analogies, defined the governed operating system as the moat, and connected technical evidence to scalable HoldCo value without claiming mathematical exclusivity. |
| SPV Financial Term Sheet | Preserved the concise term-sheet form while clarifying currency, capital stack, true sale, collateral, advance rate, OC, reserves, waterfall, benchmark, eligibility, and conditional stress protection. |
| Part 1 | Rebuilt the relatable microeconomic cascade, distinguished arrears from authoritative insurance status and platform action, and connected product mechanics to controlled collections and driver sufficiency. |
| Part 2a | Preserved detailed temporal and feature engineering while clarifying event-time truth, raw-versus-engineered ownership, point-in-time controls, and dimensionally coherent definitions of DLR, Earnings Velocity, and Repayment Velocity. |
| Part 2b | Preserved the deepest mathematics, corrected spline, residual, hierarchy, diagnostic, copula, and valuation claims, and introduced a calibrated HLR specification designed to reduce multicollinearity and duplicated signal. |
| Part 3 | Restored the supportive intervention story while assigning actions to authorised parties, separating accounting evidence from policy triggers, and qualifying fairness, forbearance, insurance, and comparative-regulatory claims. |
| Part 4 | Preserved the enterprise-control narrative while distinguishing product subledgers, analytical views, accounting evidence, and the D365 general-ledger boundary. |
| Part 5 | Retained KESONIA compounding, pricing, FTP, capital, and accounting mathematics while separating benchmark observation, contractual accrual, customer pricing, note pricing, risk measurement, and policy action. |
| Part 6 | Replaced a vendor-first checklist with a human, 18-month, stage-gated execution narrative that begins with a driver event and builds evidence, ledgers, models, controlled interventions, institutional controls, and SPV scale in dependency order. |

## Validation record

At completion:

- all ten narrative files and all ten controlled specification files were present;
- the dated backup contained all ten original target files and the excluded glossary;
- all ten narrative files parsed successfully through Pandoc 3.1.11.1 as Markdown ASTs;
- all fenced blocks were balanced;
- every in-text numeric citation resolved to a defined reference in its paper;
- obsolete labels, malformed front-matter keys, placeholder continuation comments, mojibake, and unintended long dashes were scanned;
- capital-stack arithmetic, advance-rate and OC denominators, feature ownership, HLR design, KESONIA notation, and policy-layer separation were checked across the series; and
- no source file in the dated backup was edited.

All nineteen Mermaid figures rendered successfully through the project Pandoc and Mermaid CLI path during the final direct pass. The generated validation HTML files were then removed; the narrative Markdown and the renderer cache were retained. A final publication export should still inspect every figure in the intended Substack, website, PDF, or presentation toolchain because Mermaid layout can vary by renderer, page width, and font environment.

## Publication use

For public serialisation, begin with Part 1, continue through Parts 2a, 2b, and 3, and then use Parts 4 through 6 as the institutionalisation arc. The memorandum, HoldCo pitch, and SPV term sheet are companion views for partners, equity investors, and structured-finance readers. Before a formal financing, regulatory submission, or model approval, replace illustrative assumptions with dated evidence and reconcile each public claim against the controlled specification, executed contract, approved accounting policy, and validated production artefact.
