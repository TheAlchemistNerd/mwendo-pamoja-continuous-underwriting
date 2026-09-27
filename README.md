# Mwendo Pamoja

**Continuous underwriting for gig-economy resilience**

Mwendo Pamoja is an insurtech and embedded-finance research and implementation programme for gig-economy drivers. It combines governed telematics and wallet data, explicit liquidity features, redundancy-controlled Bayesian underwriting, policy and compliance controls, intervention design, KESONIA-linked pricing, and ring-fenced SPV finance.

The repository is organized around canonical publications, controlled implementation specifications, supporting research, and auditable financial artefacts. Numerical projections remain illustrative until replaced by validated portfolio data, executed agreements, and approved accounting, legal, actuarial, and model-governance decisions.

[Read the published white-paper edition dated 8 September 2026](publications/pdfs/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_CC_BY_NC_SA_4_0_2026-09-08.pdf)

[Published PDF index](publications/pdfs/README.md) · [Repository boundaries](docs/governance/REPOSITORY_BOUNDARIES_AND_SPLIT_PLAN_2026-09-25.md) · [Completed repository migration](docs/governance/REPOSITORY_MIGRATION_2026-09-26.md)

Independent projects now live side by side in Downloads: Underwrite for Collection, Bayesian telematics relativities and RegTech–KESONIA Treasury. Their former locations in this repository contain navigation pointers; the original trees are archived locally. Guest repositories, including `financial material` and `business and technical website blog`, remain outside this task's write boundary. See the completed migration record for authoritative locations, validation and remaining work.

The [28 September resolution record](docs/governance/PENDING_CHANGES_RESOLUTION_2026-09-28.md) records the retained research reviews, verified source retirement, publication links and licence-page checks. The [RegTech project comparison](docs/governance/REGTECH_PROJECT_COMPARISON_2026-09-28.md) identifies an older overlapping Documents repository whose unique history and publication assets still need reconciliation.

## Core architectural question

> How can an insurtech and embedded-finance platform observe a driver's changing operating state early enough to support fair intervention, continuously recalibrate risk, and protect both livelihoods and ring-fenced receivable cash flows without confusing prediction, policy, accounting, or regulation?

The canonical decision sequence is:

```text
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
```

The neural branch and Explicit Liquidity Feature Path have separate feature ownership. CFA, DLR, Earnings Velocity, Repayment Velocity, wallet volatility, reserve balance, time since depletion, utilization, and approved financial interactions are not duplicated as engineered neural inputs. Hard-coded credit, contractual, regulatory, concentration, reserve, and operational rules remain downstream in the Credit Policy and Compliance Gate.

## Repository map

| Path | Purpose |
|---|---|
| `whitepapers/mwendo-pamoja/` | Canonical seven-part white paper, glossary, publication build configuration, and final PDF. |
| `whitepapers/telematics-relativities/` | Navigation pointers to the independent Bayesian telematics relativities repository. |
| `docs/transaction/` | Strategic partnership memorandum, HoldCo technical pitch, SPV term sheet, and retained source material. |
| `docs/controlled-specifications/` | Implementation, legal-boundary, accounting, data, model-governance, SPV, and programme-control specifications. |
| `docs/governance/` | Editorial standards, revision ledgers, canonical baseline, source index, inconsistency reports, and remediation plans. |
| `docs/research/` | Data-architecture, Bayesian, neural, and implementation research notes; KESONIA pointers lead to its independent repository. |
| `docs/implementation/` | Launch and execution material that supports programme delivery. |
| `financial_models/spv/` | Illustrative SPV workbook, model guide, generator source, and validation records. |
| `presentations/lender-dfi/` | Lender and DFI presentation source. Release decks are added only after visual approval. |
| `publications/linkedin/` | Shorter public articles derived from the core research. |
| `_archive/` | Ignored local snapshots, superseded artefacts, source extractions, and historical deliverables. |
| `scratchpad/` | Ignored working notes, caches, renderings, inspections, and temporary build output. |

## Canonical publications

The Mwendo Pamoja white paper is assembled from:

1. Product Architecture and Cascades.
2. Deep Temporal Representation and Feature Engineering.
3. Bayesian Underwriting and Asymmetric Copulas.
4. Regulatory Orchestration and Interventions.
5. Enterprise ERP and Telemetry.
6. KESONIA Pricing and Capital Orchestration.
7. Implementation Roadmap and Execution.
8. Interdisciplinary Field Map and Technical Glossary.

The narrative papers explain the human problem, microeconomics, business structure, computation, mathematical design, and financing proposition. The companion controlled specifications define boundaries, owners, interfaces, controls, tests, and implementation conditions. Executed contracts, applicable Kenyan law, approved accounting policy, independent validation, and production evidence prevail over both.

## White-paper build

The publication build uses Pandoc, XeLaTeX, the corporate metadata file, and the Mermaid Lua filter.

```powershell
powershell -ExecutionPolicy Bypass -File .\whitepapers\mwendo-pamoja\build\build_whitepaper.ps1
```

Local assembly and rendering intermediates are written beneath `scratchpad/` and are not committed. The reviewed release PDF is retained in `whitepapers/mwendo-pamoja/dist/`.

## Financial model

The SPV workbook is a 36-month illustrative project-finance model containing the capital stack, origination assumptions, product schedules, collections, losses, debt schedules, reserves, overcollateralisation, waterfall, covenants, returns, sensitivities, and source audit.

It is a diligence and structuring prototype, not an executed financing model. Assumptions marked illustrative or provisional must be replaced with a portfolio tape, agreed note terms, legal and tax advice, verified servicing data, and independently reviewed formulas before lender reliance.

Excel workbooks are intentionally eligible for version control because they may contain substantive SPV financial models. Temporary Office files and intermediate recalculation copies remain ignored.

## Presentation status

The lender and DFI deck source is retained for future refinement. The earlier generated PPTX remains in the ignored local archive because it has not yet passed the desired visual-quality threshold. A presentation will enter `presentations/lender-dfi/release/` only after slide-level rendering, overflow, source, numerical tie-out, and readability checks pass.

## Evidence and governance

The repository distinguishes:

- source-backed values;
- derived values;
- illustrative assumptions;
- scenario shocks;
- calculated outputs;
- internal policy rules;
- contractual covenants;
- accounting requirements;
- regulatory requirements; and
- statistical or model-governance conventions.

The annotated source index uses one stable IEEE sequence. The consistency audit and controlled baseline record how terminology, probability measures, feature ownership, pricing, SPV economics, accounting, and regulatory scope were reconciled.

## Local material and backups

`_archive/` and `scratchpad/` are intentionally excluded from Git. The pre-reorganization snapshot dated 27 August 2026 contains SHA-256 hashes and preserves the full source and deliverable state, excluding only reproducible dependency and rendering caches.

Because ignored folders are not protected by GitHub, local archives should also be copied periodically to independent storage.

## Remote policy

Recommended repository name: `mwendo-pamoja-continuous-underwriting`.

The current repository should be treated as private-first because its Git history contains transaction documents, financial terms, technical specifications, and internal review material. A public edition should be produced as a sanitized publication repository rather than by assuming that `.gitignore` removes files from earlier commits.

## Contact

Neville Maloba<br>
[nevillemaloba@gmail.com](mailto:nevillemaloba@gmail.com)

## Credit research review and source retirement — 22 September 2026

The [coverage audit](docs/research/coverage-retirement-audit-2026-09-22/00_START_HERE.md) maps the supplied practitioner posts and the continuous-underwriting rough document to current papers, identifies corrections, and records the reversible root cleanup. The [research addendum](docs/research/coverage-retirement-audit-2026-09-22/03_RESEARCH_PROTOCOL_ADDENDUM.md) formalises vintage analysis, evidence freshness and operational study protocols. [Open manuscript corrections](docs/research/coverage-retirement-audit-2026-09-22/04_ACTIVE_WORK_AND_ERRATA.md) remain explicit.

The [DCP positioning note](docs/research/industry-engagement/MWENDO_PAMOJA_DCP_POSITIONING_AND_PEER_REFERENCE_NOTE.md) is active. Twelve historical root files are preserved under `_archive/2026-09-22-source-retirement/`; see the [move manifest](docs/research/coverage-retirement-audit-2026-09-22/05_CLEANUP_MANIFEST.md). The *So picking the hierachical bayesian logistic regression with my econometric.docx* source remains at root intentionally because the current research package references it.

<!-- ADDITIONAL_MATERIAL_2026_09_23 -->

### Latest material review — 23 September 2026

[Read the additional coverage notes and protocols](docs/research/coverage-retirement-audit-2026-09-22/06_ADDITIONAL_MATERIAL_REVIEW_2026-09-23.md) for recovery readiness, trade exposure, decision execution, provision matrices, purpose verification and model complexity. This extends the existing research programme; written coverage and untested hypotheses are distinguished.
