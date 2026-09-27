# What the multidisciplinary posts confirm, improve and leave open

## How to interpret coverage

**Covered in design** means a substantive, technically useful treatment exists in the cited manuscript or controlled specification. **Planned** means the research plan specifies an analysis but has not produced its results. **Needs strengthening** means a concrete question or implementation detail is still missing. None of these labels means proven effectiveness in a live portfolio.

| Material supplied | Existing substantive coverage | Assessment | Required improvement and research destination |
|---|---|---|---|
| Irvin Martinez: PD, LGD, EAD, expected/unexpected loss and portfolio risk | M0 §§3, 7–12 separates horizon PD, timing, exposure, cure, recovery and cash; M2b and U2b provide hierarchy, inference, dependence and validation. | **Covered in design.** The post confirms the breadth of the architecture. | Keep definitions and interfaces explicit. RQ4–5 test whether state paths improve cash/loss forecasts; RQ7 tests shared shocks. Do not turn the literature review into a generic statistics syllabus. |
| Irvin Martinez: scorecards, WOE/IV, vintage/roll rates, calibration and model validation | R5 P7–P8 already prescribes comparators, calibration, proper scores and temporal/grouped validation. M2b discusses PSI, Gini and governance. | **Mostly covered/planned; vintage was insufficiently formalised.** WOE/IV is not necessary for every model. | Add protocol V below. If a scorecard is useful, fit binning, smoothing and variable selection within training folds. AUC/Gini/KS are diagnostics, not substitutes for calibration or economic value. |
| Mohammed Adeleke: the credit analysis can expire before disbursement | M0 §2 and M2a §4 prohibit unavailable information; R5 P2/P15 separates information, scoring and refitting. B §§5–7 preserves uncertain economic evidence. | **Foundation covered; operational gap remains.** Historical correctness does not establish freshness today. | Add protocol F: timestamps for assessment, approval and disbursement; source-specific freshness; material-event triggers; revalidation and override records. RQ1 and RQ8 own the test. Actual workflow data require a partner. |
| Kaiyuan Chen: contractual option ownership, changing cash-flow profiles and convexity | U5 §§7.5–7.6 already treats prepayment, extension, drawdown, deposits, curve/basis sensitivity, hedging and ALCO assumption registers. M5 §§4.1–4.2 distinguishes partner-bank IRRBB from SPV ALM. | **Well covered conceptually; scenario implementation remains planned.** | Add protocol O: identify each option's holder and contractual conditions; compare fixed and behavioural cash flows in identical rate scenarios. Report NII/EVE, liquidity and residual sensitivities separately. A first-order hedge does not establish curvature protection; a bond or swap can itself have convexity. |
| Nitesh Kumar Jain: IFRS 9 and a Vasicek PIT conversion | M0 §11 and M3 §2.1 put ECL under the accounting owner; U5 §§3–5 separates financial measures. RQ3/RQ5/RQ8 address uncertainty, loss and changing conditions. | **Main accounting separation covered; screenshot calculation needs correction.** | Include Stage 3 and distinguish default horizon from loss-realisation horizon. LGD and EAD are forecasts where future outcomes are unknown. Use the square-root factor loadings shown in protocol A. Vasicek is a benchmark with assumptions, not a required IFRS 9 algorithm. |
| Judy Chege: onboarding quality, real facility need, targets and purpose | B §§3–8 develops entity boundaries, provenance, financing inflows, uncertainty and sustainable repayment; U3 §4 makes authority, affordability and conduct part of the action gate. | **Strong conceptual coverage; incentive and execution evidence need detail.** | Add protocol G: verified purpose/use, evidence age, decision/override owners, targets and exceptions, and changes after disbursement. Preserve rejected/withdrawn applications where lawful. Target pressure is a hypothesis requiring measurement, not an observed fact in mortgage data. |
| Judy Chege: early delinquency, respectful contact and relationship preservation | M3 §5 specifies an assistive ecosystem and treatment/selective-label ledger. U2b §7 separates prognosis from causal effects; U3 §§3–7 supplies the intervention ladder and conduct gate. R5 P10–P11 supplies trial/target-trial design. | **Covered in depth as design; effectiveness unproven.** | Add protocol I's operational fields and endpoints. Test early-contact timing rather than assuming the first two weeks are universally optimal. Measure offers, assignment, delivery, consent/authority, promises kept, durable cure, recurrence, complaints and retention. |

## Interpretation of the posts

The posts are useful practitioner prompts. They are not independent validation of the proposed model or evidence that all lenders have the stated failures. In particular:

1. An outdated assessment can be a risk even if it was correct when written; elapsed time alone does not prove deterioration.
2. Monitoring can reveal both weak origination and genuinely new shocks. It is too strong to classify every later failure as an onboarding failure.
3. A courteous intervention may protect a relationship, but its causal effect on repayment must still be estimated.
4. A technically cured loan can remain economically fragile or refinance its arrears elsewhere. B §8 already makes this distinction.
5. A regulatory/accounting formula is not made correct by an intuitive explanation. Definitions, units, timing, model assumptions and applicable entity matter.
6. Excel, SQL and Python competence supports execution. It is not a separate research contribution.

## Screenshot inventory

The supplied filenames are preserved here so the assessment can be traced to the visible material. Cropped endings were not reconstructed.

| Image | File identifier after `codex-clipboard-` | Visible material |
|---|---|---|
| 1 | 43d424fc-e94d-47af-a4f9-ae456d0a68dd.jpg | Martinez: foundations, statistics and tools |
| 2 | 24b87140-80d4-4251-978d-8bc85c709772.jpg | Adeleke: assessment-to-disbursement delay |
| 3 | c37dd16a-fe3b-4965-9c18-19589db8c46a.jpg | Adeleke: changed facts and revalidation |
| 4 | 6b929d6f-b317-4494-98c7-56954f998555.jpg | Chen: option ownership and convexity |
| 5 | 6b2826a8-6207-411e-9d2a-e2c8d8568b5e.jpg | Jain: IFRS 9 concepts |
| 6 | 73c656e4-a9db-4739-be91-697266e54a26.jpg | Jain: Vasicek calculation |
| 7 | 1496e8fb-5783-41ea-8cd4-64026de7dd29.jpg | Duplicate/overlapping IFRS 9 material |
| 8 | dd79212a-f60a-41b2-b7ce-5ab81a0aa7cf.jpg | Duplicate/overlapping Vasicek material |
| 9 | 1245ca9c-97ff-485d-b656-cb188313bfcf.jpg | Chege: monitoring and onboarding evidence |
| 10 | 5a6831c8-c93e-42ec-82d7-9765903aa72a.jpg | Chege: need, purpose and target pressure |
| 11 | 1ec40129-e50a-407d-b724-fee5986b155e.jpg | Chege: first response to arrears |
| 12 | b7130e39-de17-4489-93cd-4125effe273b.jpg | Chege: respectful servicing and continuity |
| 13 | 2e671a5f-eafd-4d3c-a49b-32bb9d219ec5.jpg | Martinez: models, IFRS 9/CECL and validation |

## Sources within the workspace

- **M0** — [Controlled credit-risk model and loss architecture](../../controlled-specifications/CREDIT_RISK_MODEL_AND_LOSS_ARCHITECTURE_SPECIFICATION.md).
- **M2a** — [Mwendo Pamoja Part 2a](../../../whitepapers/mwendo-pamoja/parts/Part_2a_Deep_Temporal_Representation_and_Feature_Engineering.md).
- **M2b** — [Mwendo Pamoja Part 2b](../../../whitepapers/mwendo-pamoja/parts/Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md).
- **M3** — [Mwendo Pamoja Part 3](../../../whitepapers/mwendo-pamoja/parts/Part_3_Regulatory_Orchestration_and_Interventions.md).
- **M4** — [Mwendo Pamoja Part 4](../../../whitepapers/mwendo-pamoja/parts/Part_4_Enterprise_ERP_and_Telemetry.md).
- **M5** — [Mwendo Pamoja Part 5](../../../whitepapers/mwendo-pamoja/parts/Part_5_KESONIA_Pricing_and_Capital_Orchestration.md).
- **U2b** — [Underwrite for Collection Part 2b](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md>).
- **U3** — [Underwrite for Collection Part 3](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_3_Regulatory_Orchestration_Fair_Intervention_and_Collection_Governance.md>).
- **U5** — [Underwrite for Collection Part 5](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md>).
- **B** — [Before the Ratio: entity-resolved cash-flow article](../../../publications/linkedin/BEFORE_THE_RATIO_ENTITY_RESOLVED_CASHFLOW_UNDERWRITING.md).
- **T** — [Bayesian telematics relativities paper](../../../whitepapers/telematics-relativities/paper.md).
- **R1** — [Main research-paper outline](../../../output/credit_lifecycle_research_plan_2026-09-21/01_MAIN_PAPER_DETAILED_OUTLINE.md).
- **R2** — [Freddie Mac paper and protocol](../../../output/credit_lifecycle_research_plan_2026-09-21/02_FREDDIE_MAC_PAPER_AND_PROTOCOL.md).
- **R3** — [Fannie Mae paper and protocol](../../../output/credit_lifecycle_research_plan_2026-09-21/03_FANNIE_MAE_PAPER_AND_PROTOCOL.md).
- **R4** — [Earlier source audit and derivations](../../../output/credit_lifecycle_research_plan_2026-09-21/04_SOURCE_AUDIT_AND_DERIVATIONS.md).
- **R5** — [Shared research protocols P0-P15](../../../output/credit_lifecycle_research_plan_2026-09-21/05_SHARED_RESEARCH_PROTOCOLS.md).

<!-- ADDITIONAL_MATERIAL_2026_09_23 -->

## Second set of practitioner material — 23 September 2026

The [additional coverage matrix and protocols](06_ADDITIONAL_MATERIAL_REVIEW_2026-09-23.md) extend this review to the 13 new screenshots. Recovery/protection, product-purpose fit and simple-model governance already have substantial written coverage; the additions concern dated evidence, denominators, execution and measurable acceptance gates. No new empirical finding is implied.
