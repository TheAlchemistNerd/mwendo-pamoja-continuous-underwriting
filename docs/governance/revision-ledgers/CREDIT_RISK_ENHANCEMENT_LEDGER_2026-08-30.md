# Mwendo Pamoja Credit-Risk Enhancement Ledger

## Revision boundary

This ledger records the coordinated credit-risk enhancement implemented on 30 August 2026 from `DETAILED_IMPLEMENTATION_PLAN_CREDIT_RISK_ENHANCEMENTS.md`. The edition advances the seven public Parts and their controlled specifications. It preserves the driver-centred narrative, the Explicit Liquidity Feature Path, the redundancy-controlled HLR, the neural architecture, the existing B-spline RW1 and AR1 research, the copula programme, and the SPV finance narrative.

The pre-edit sources are preserved at:

`revision_backups/2026-08-30_pre_credit_risk_enhancements/`

The backup contains 17 source files and `manifest.csv`; the manifest SHA-256 is `A876572AA86F4B8E72D8166E52212268CB3FE638F90EC0AE65160EDDA883A58B`.

## Canonical decisions

| ID | Decision | Implementation |
|---|---|---|
| CR-E01 | Stable observation unit | Driver-product-risk episode at decision time, with product horizon and intervention state |
| CR-E02 | Clock separation | Event, availability, decision, label-maturity, accounting, and cash-realisation times |
| CR-E03 | Ledger spine | Identity/exposure, obligations, decisions/actions, outcomes/maturity, and recoveries/cash flows |
| CR-E04 | Primary model | Fixed-horizon redundancy-controlled hierarchical Bayesian logistic regression |
| CR-E05 | Nonlinearity | Governed P-splines in the champion; B-spline RW1 and AR1 alternatives preserved in the appendix |
| CR-E06 | Neural block | Cross-fitted residual representation, optional training-fold whitening, regularised-horseshoe shrinkage |
| CR-E07 | Inference | NUTS/HMC reference; Pólya-Gamma blocked Gibbs as an offline conditional-conjugacy candidate |
| CR-E08 | Pooling | Product, platform, geography, cohort, and selected time effects remain hierarchical under every inference method |
| CR-E09 | Timing | Hierarchical piecewise-exponential proportional-hazards challenger with right censoring and horizon reconciliation |
| CR-E10 | Advanced timing research | Gamma frailty and joint longitudinal-survival structures retained as evidence-dependent challengers |
| CR-E11 | Loss chain | Separate PD, EAD, cure, modification, LGD, ordinary recovery, IPF refund, cost, and timing components |
| CR-E12 | Dependence order | Observed factors, hierarchy, within-driver linkage, then residual dependence challenger |
| CR-E13 | Production | Signed posterior scoring artifact; no MCMC during an underwriting request |
| CR-E14 | Institutional interfaces | Distinct accounting ECL, pricing EL, economic capital, regulatory capital, and SPV protection views |

## Public manuscript changes

| Part | Enhancement |
|---|---|
| Part 1 | Added three credit clocks, risk-episode observation, and a three-source dependence explanation |
| Part 2a | Added five ledgers and clock controls, P-spline artifact ownership, and online-offline parity contract |
| Part 2b | Added observation and censoring definitions, governed P-splines, Pólya-Gamma inference, timing challenger, complete loss chain, dependence ordering, revised pipeline, and preserved research appendices |
| Part 3 | Added typed decision taxonomy and gate payload, refined fast-deterioration accounting language, and added treatment/selective-label ledger |
| Part 4 | Added common contract-and-risk spine, cash-shortfall-first ECL interface, and survival-to-monthly marginal-PD controls |
| Part 5 | Added borrower-posterior-to-SPV cash-flow bridge, one-year and ultimate loss, tranche allocation, and reverse stress |
| Part 6 | Added ledger gate, P-spline stage, offline inference comparison, survival and loss stages, dependence order, and intervention evaluation design |

## Technical material adopted from the shared research note

The implementation retains partial pooling, non-centred hierarchical effects where helpful, low-dimensional varying effects with governed covariance, group-level posterior predictive validation, right-censoring, piecewise-exponential risk-set construction, survival-to-PD mapping, and joint longitudinal-survival modelling as a research challenger.

The implementation does not adopt claims that non-centering eliminates divergences, row-level PSIS-LOO proves new-group transport, a piecewise-exponential model is an unspecified Cox partial-likelihood fit, coefficient variance is a direct volatility process, or a simple product of PD, LGD, and EAD is a complete IFRS 9 methodology.

## Validation record to complete

Before promotion, verify Markdown parsing, headings, equation delimiters, citation resolution, Mermaid rendering, cross-references, public-controlled consistency, absence of duplicate feature ownership, and diffs against the preserved snapshot. Model implementation must later complete the empirical acceptance tests in the new controlled specification.
