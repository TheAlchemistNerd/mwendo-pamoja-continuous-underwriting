# KBA Lifecycle Credit Research Package

## Purpose

This directory contains the new Kenya Bankers Association research package developed from the existing “Underwrite for Collection,” KESONIA, and Mwendo Pamoja manuscripts. It is an independent publication stream. The source manuscripts remain unchanged.

## Proposed research paper

**From KESONIA to Sustainable Collection: Risk-Based Pricing, MSME Credit Quality and Lifecycle Underwriting in Kenya**

The paper asks how Kenya's transition to KESONIA-anchored risk-based pricing affects pricing transmission, MSME credit access, and collectability, and how a lifecycle-underwriting framework can connect origination, monitoring, intervention, durable cure, and net recovery.

## Publication strategy

The package separates two editorial products:

1. **Research proposal and full empirical paper.** Intended for a route confirmed by the KBA Research Centre, including a possible off-cycle Working Paper or a future Annual Banking Research Conference.
2. **Practitioner article.** A KBA Economic Bulletin adaptation of “Underwrite for Collection.” The existing article is a strong narrative and policy foundation but will not be represented as an empirical conference paper without data, methodology, results, and validation.

The standard 2026 conference submission stages have passed. The conference itself is scheduled for 17 and 18 September 2026. The editorial enquiry therefore requests guidance rather than assuming that a late submission will be accepted.

## Files

- `01_KBA_EDITORIAL_ENQUIRY.md`: concise email to the KBA Research Centre.
- `02_ONE_PAGE_CONCEPT_NOTE.md`: short description suitable for an initial editorial discussion.
- `03_FIVE_PAGE_RESEARCH_PROPOSAL.md`: proposal structured around KBA's stated requirements.
- `04_CANONICAL_RESEARCH_SPECIFICATION.md`: locked research question, definitions, hypotheses, estimands, and evidence boundaries.
- `05_SOURCE_EXTRACTION_LEDGER.md`: controlled map from existing manuscripts to the new work.
- `06_DATA_REQUIREMENTS_AND_DICTIONARY.md`: public and institution-level data specification.
- `07_SOURCE_BASELINE.md`: source hashes taken before extraction or adaptation.
- `08_KBA_ECONOMIC_BULLETIN_ARTICLE_DRAFT.md`: first practitioner adaptation of “Underwrite for Collection” with KESONIA framing.
- `09_PUBLIC_DATA_BASELINE_NOTE.md`: initial observations, limitations, and data-quality questions from the public snapshot.
- `10_VALIDATION_REPORT.md`: automated and editorial checks completed on the initial package.
- `11_KBA_CORRESPONDENCE_LOG.md`: auditable record of the enquiry sent to KBA and its attachments.
- `data/source_registry.csv`: controlled public-source register.
- `data/raw/public/2026-09-02/`: first reproducible CBK and KBA data snapshot.
- `scripts/collect_public_baseline.py`: collector for supported official public sources.

## Locked editorial principles

- Use KESONIA as the reference component of the revised risk-based credit-pricing model, not as a replacement for that model.
- Keep the reference rate, `K_RBCP`, fees, expected loss, funding cost, capital, and shareholder return conceptually distinct.
- Treat lending flows, outstanding balances, NPL stocks, and NPL ratios according to their periods and denominators.
- Separate prediction, policy, intervention, and realised outcome.
- Treat collectability as a lifecycle property measured through payment, cure, re-default, recovery, cost, and time.
- Use point-in-time data and out-of-vintage validation.
- Make causal claims about interventions only where assignment and comparison support them.
- Present neural or advanced Bayesian components as incremental challengers unless evidence supports their inclusion in the primary model.
- Distinguish regulation, contract, internal policy, and proposed architecture.
- Use constructive language and implementable recommendations.

## Current status

| Work item | Status |
|---|---|
| Official call and dates verified | Complete |
| Outlet strategy agreed | Complete |
| Editorial enquiry | Drafted |
| One-page concept note | Drafted |
| Five-page proposal | Drafted for page-layout testing |
| Canonical research specification | Drafted |
| Source extraction ledger | Drafted |
| Data dictionary | Drafted |
| KBA enquiry | Sent on 2 September 2026 with concept note and research proposal |
| KBA response | Pending |
| Public dataset | Initial CBK and KBA baseline assembled and validated |
| Institutional data partner | Not yet secured |
| Empirical estimates | Not yet produced |
| Full working paper | Dependent on data and route confirmation |

The dated baseline is stored under `data/raw/public/2026-09-02/`. It includes a run manifest and source hashes. The Total Cost of Credit interface, CBK survey index, macroeconomic controls, and historical product-pricing observations remain to be added.
