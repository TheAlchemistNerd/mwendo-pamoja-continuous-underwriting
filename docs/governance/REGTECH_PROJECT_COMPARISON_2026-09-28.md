# RegTech project comparison — 28 September 2026

## Finding

The Documents project and the new Downloads repository share the same four-part KESONIA series. All four core manuscripts are byte-identical, including the Documents working-tree versions. These are overlapping project locations with complementary material, not two independent research programmes.

The September 26 extraction from Mwendo did not inspect or incorporate the existing Documents repository. Its unique publication assets, Git history and uncommitted changes therefore remain to be reconciled. The earlier description of Downloads as the authoritative repository records the migration decision; it does not establish that all earlier RegTech material was captured.

## Locations and roles

| Aspect | `Documents/Regulatory Tech for Banks and neobanks` | `Downloads/regtech-kesonia-treasury` |
|---|---|---|
| Core source | Four KESONIA manuscripts at root | The same four manuscripts under `docs/research/kesonia/` |
| Distinctive material | Original authoring/publication package: LinkedIn editions using Unicode mathematics, four promotional posts, 36-item annotated bibliography, diagrams/rendering tools and historical drafts | September 23–25 Treasury review/casebook, original pasted texts, arithmetic checker, STP/software review, FRTB note, compounding/term-structure note and 18-item remaining-work register |
| Broader scope | `Drafts/neobank & fintech outline.md` develops a wider digital-lender outline: temporal modelling, hierarchy, product-specific credit, dependence and interventions | Explicit benchmark, curve, FTP, ALM and Treasury development programme, connected to the wider credit research |
| Maturity | Manuscripts, SQL/design illustrations and publishing utilities; no standalone deployable banking engine identified | Manuscripts plus executable illustrative arithmetic and local HTML rendering; operational integrations remain planned |
| Git at inspection | `main`, `0ca6438`, original July 12 commit; local changes; no remote configured | `codex/repository-separation`, `dc4ef18`; clean working tree; no remote configured |

## Evidence and entry points

- [Original Part 1](<C:/Users/Nevo/Documents/Regulatory Tech for Banks and neobanks/Part1_KESONIA_Reform_and_Enterprise_Architecture.md>) and [new Part 1](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/docs/research/kesonia/Part1_KESONIA_Reform_and_Enterprise_Architecture.md>).
- [Original promotional drafts](<C:/Users/Nevo/Documents/Regulatory Tech for Banks and neobanks/linkedin_posts.md>) and [broader neobank outline](<C:/Users/Nevo/Documents/Regulatory Tech for Banks and neobanks/Drafts/neobank & fintech outline.md>).
- [New repository scope](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/README.md>) and [migration provenance](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/MIGRATION.md>).
- [New worked Treasury cases](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/output/kesonia_treasury_deep_review_2026-09-25/02_CALCULATION_AND_CASEBOOK.md>) and [remaining-work register](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/docs/research/kesonia/TREASURY_REMAINING_WORK_REGISTER_2026-09-25.md>).
- [Core-file hash comparison](REGTECH_PROJECT_COMPARISON_2026-09-28.json).

## Recommended consolidation, not executed

Use one future working project, with distinct research, publication and implementation areas. Downloads remains the practical proposed destination under the user's side-by-side Downloads preference. Before retiring either location, preserve the Documents repository's history and working state, inventory its unique files, incorporate the useful original publishing/bibliography/draft assets, and verify all copies and build paths. If lineage is important, retain or import the original Git history rather than treating the September snapshot as the project's inception.

The four identical manuscripts need no content merge at the observed state. Unique material and publication-specific variants still require review. No automatic reset, blanket copy, move, commit or push was performed in either RegTech location during this comparison. Guest financial-material and website repositories were also untouched.

The content and Git checks support the ownership comparison. They are not a new legal, regulatory, bibliographic or empirical validation of either research programme.
