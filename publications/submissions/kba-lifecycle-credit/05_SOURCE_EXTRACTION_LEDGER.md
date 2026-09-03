# Source Extraction Ledger

## Purpose

This ledger controls how existing project material may inform the KBA research package. It prevents wholesale copying, unresolved terminology from entering the paper, and one source document from determining the structure of the new manuscript.

| ID | Source | Source section | Intended use | Treatment before reuse | Target output |
|---|---|---|---|---|---|
| S01 | `publications/linkedin/UNDERWRITE_FOR_COLLECTION.md` | Opening and section 1 | Human motivation and disciplined interpretation of Kenyan lending and NPL figures | Update all as-of dates; retain flow-stock distinction; replace rhetorical claims with sourced research motivation | Proposal introduction; Bulletin article; full-paper introduction |
| S02 | Same | Section 2, “Collection is a design property” | Core lifecycle-underwriting thesis | Preserve narrative; define measurable collectability outcomes | Concept note; introduction; implications |
| S03 | Same | Section 3, credit-state and cash-flow truth | Canonical event ledger and system-of-record concept | Convert architecture into research data specification; distinguish source ledgers from derived analytical tables | Data section; implementation recommendations |
| S04 | Same | Section 4, whether and when cash deteriorates | Probability, timing, exposure, cure, and recovery decomposition | Use transparent benchmark first; move advanced model details to methods and appendix | Methodology |
| S05 | Same | Section 5, prediction, policy, and action | Governance separation | Retain as canonical decision chain; add observed outcome and intervention assignment | Governance and intervention design |
| S06 | Same | Section 6, intervention before delinquency | Early intervention and causal learning | Define treatment, eligibility, counterfactual, cost, durable cure, and re-default | Intervention methodology |
| S07 | Same | Section 7, fair collection | Fair treatment as credit-risk control | Align to Kenyan law and partner policy; avoid importing foreign legal tests as Kenyan requirements | Ethics, governance, recommendations |
| S08 | Same | Section 8, accounting, capital, and funding | ECL, capital, FTP, and ring-fenced financing consequences | Retain lifecycle link; remove project-specific SPV assumptions; distinguish bank balance-sheet and SPV contexts | Banking implications |
| S09 | Same | Sections 9 and 10 | Lifecycle scorecard and implementation sequence | Convert into measurable research outputs and institutional recommendations | Policy brief; Bulletin article |
| S10 | `docs/research/kesonia/Part1_KESONIA_Reform_and_Enterprise_Architecture.md` | Sections I and II | Policy motivation and pricing formula | Replace “from RBCPM to KESONIA” framing with KESONIA within revised RBCPM; use official CBK definitions | Institutional framework |
| S11 | Same | Sections III to V | Enterprise data and operational integration | Reframe ERP as governed accounting and operational architecture; do not designate one universal regulatory source of truth | Implementation recommendations |
| S12 | `docs/research/kesonia/Part2_Daily_Compounding_Engine_Mathematics_and_SQL.md` | Sections II to IV | Compounding, calendar, and observation conventions | Verify against official KESONIA methodology and actual loan contract; distinguish index/factor, annual rate, and accrual amount | Technical appendix |
| S13 | Same | SQL sections | Reproducible benchmark and accrual implementation | Treat as prototype until dialect-specific tests pass; retain calendar and reconciliation principles | Reproducibility appendix |
| S14 | `docs/research/kesonia/Part3_AI_Pricing_Engine_and_IFRS9_Integration.md` | Sections I to V | Separation of benchmark and borrower risk; behavioural evidence; explainability | Correct `K_RBCP` composition; present PD/LGD/EAD as risk and loss inputs, not the whole premium; describe AI as proposed, not mandated | Institutional framework; methods |
| S15 | Same | Sections VIII to XII | IFRS 9, EIR, FTP, ALM, and audit | Reconcile with Part 5's newer treatment; distinguish contractual repricing, ECL, funding, and IRRBB | Banking implications |
| S16 | `docs/research/kesonia/Part4_RegTech_Sweep_Platform_Deep_Dives_and_Roadmap.md` | Sections I to V | Controls, lineage, validation, maker-checker, and audit | Describe as reference architecture; retain only controls relevant to research implementation | Data governance; recommendations |
| S17 | Same | Vendor deep dives | Possible implementation pathways | Cite current official vendor documentation; avoid product endorsement and unsupported production-readiness claims | Optional implementation appendix |
| S18 | `whitepapers/mwendo-pamoja/parts/Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md` | Sections 1.1 to 1.5 | HLR, observation unit, hierarchy, P-splines, and time effects | Simplify notation for banking dataset; use only identified grouping structure; retain detailed derivation in appendix | Methodology; technical appendix |
| S19 | Same | Section 2 | Pólya-Gamma offline inference and production artefacts | Preserve conditional-conjugacy interpretation and hierarchical pooling; exclude request-time sampling | Technical appendix; reproducibility |
| S20 | Same | Sections 2.5 and 3 | Timing challenger and validation | Use hazard or multistate model as main lifecycle benchmark if data support; retain diagnostics | Methodology; validation |
| S21 | Same | Section 4 | Expected-value decision boundaries and cash loss | Replace project product actions with general bank interventions; add treatment costs and authorised policy | Intervention and economic evaluation |
| S22 | Same | Section 5 | Asymmetric dependence and capital | Use as portfolio stress challenger only; do not make it central without multi-product or clustered-loss evidence | Optional appendix |
| S23 | Same | Section 6 | Explainability, model risk, fairness | Use as comparative practice; anchor Kenyan obligations separately; do not label PSI thresholds as legal requirements | Governance and limitations |
| S24 | `whitepapers/mwendo-pamoja/parts/Part_3_Regulatory_Orchestration_and_Interventions.md` | Sections 1 and 5 | Credit Policy and Compliance Gate; assistive interventions | Generalise from driver products to bank credit; retain prediction-policy-action separation | Governance; policy recommendations |
| S25 | Same | Sections 2 and 6 | IFRS 9, forbearance, intervention records | Retain classification and cash-shortfall logic; verify current accounting references | Banking implications; data dictionary |
| S26 | Same | Sections 3 and 4 | Insurance and foreign fairness material | Exclude from core banking paper; retain only clearly labelled comparative insights if relevant | Optional comparative note |
| S27 | `whitepapers/mwendo-pamoja/parts/Part_5_KESONIA_Pricing_and_Capital_Orchestration.md` | Sections 1.1 to 1.3 | Canonical KESONIA pricing and compounding distinction | Use as primary internal technical source; remove driver-specific language; cross-check every external statement | Institutional framework; appendix |
| S28 | Same | Sections 2.1 and 2.2 | From posterior PD to cash-flow distribution, reserves, and capital | Generalise to bank portfolio and optional de-risking structure; exclude fixed facility amounts | Implications; optional structured-finance box |
| S29 | Same | Sections 3 and 4 | IFRS 9, modification, ALM, FTP, and IRRBB | Retain bank-owned prudential treatment and dimensional discipline; shorten for main paper | Banking implications |
| S30 | Telematics actuarial paper | Frequency-severity, credibility, predictive validation, capital and risk-transfer chain | Transfer modelling practices only; exclude motor and insurance subject matter | Methods and validation principles |

## Excluded material

- Project-specific facility sizes, tranches, counterparties, and commercial promises.
- Claims that AI methods are mandated by CBK.
- Unverified real-time supervisory APIs or fixed payloads.
- Vendor-specific “production grade” claims not supported by executed tests.
- Foreign regulatory language presented as Kenyan law.
- Unsupported claims of senior protection, capital relief, or causal intervention benefit.
- Duplicate formulas that use the same symbol for pricing premium, capital, and model coefficients.

## Extraction acceptance test

Every reused element must have a source ID, new purpose, factual check, and final citation. The new paper must remain readable without access to any Mwendo Pamoja document and must not rely on the project's proprietary narrative for its empirical conclusions.

