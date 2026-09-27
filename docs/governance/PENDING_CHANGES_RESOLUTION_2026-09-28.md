# Pending Mwendo changes resolved — 28 September 2026

## Scope

This resolves the five modified files, seven tracked deletions and 21 untracked files reported after the migration push. It preserves the research reviews, records the prior reversible cleanup, consolidates duplicated editorial planning and makes the publication entry points usable from the repository. It does not complete the empirical or manuscript-revision backlogs described in those reviews.

## Disposition

| Pending material | Resolution |
|---|---|
| README and ignore rules | Retain migration/research navigation; explicitly track the three curated dated PDFs and original practitioner article linked by the reading index. Build output and archives remain ignored. |
| Seven tracked root deletions | Accept the recorded retirement. All twelve archived root sources/diagnostic files were rechecked against their original SHA-256 values. Tracked originals also remain in prior Git history. |
| Historical modelling note | Keep the superseded-source warning and point it to the tracked retirement ledger. Preserve the original dialogue below the notice. |
| Coverage review, protocols and JSON manifests | Retain the complete review package. Mark original paragraph/line references, source hashes and validation reports as dated evidence; local-only `output/` and archive dependencies are disclosed. Historical JSON reports were not rewritten as new validation. |
| DCP positioning note | Add an explicit proposed-status/research-lead notice and remove conversational acknowledgments. This note does not establish a licence or executed transaction; dated verification of comparator claims remains open. The original discussion is preserved locally. |
| Two copies of the pricing/content plan | Keep the complete plan in `whitepapers/mwendo-pamoja`; replace the identical LinkedIn copy with a pointer to its publication sections. Update navigation and identify source editions. |
| Before the Ratio article | Preserve the article and clarify §6: debt-service coverage uses cash available after declared operating/tax/working-capital/investment treatment, over a matching period. Gross eligible receipts alone are not the numerator. Add a primary-source reference. |
| Stray `revised_with_sources/--` | Identified as generated Pandoc JSON (348 document blocks); archived intact as `pandoc-generated-document.json`, with SHA-256 verification. |
| Licence-page build/header changes | Keep the pending publication changes after PowerShell parsing, isolated Pandoc/XeLaTeX compilation and visual inspection of the cover, licence and contents. No full-manuscript rebuild or replacement of dated publications was performed. |

The cash-availability clarification follows the [World Bank's discussion of debt-service coverage](https://ppp.worldbank.org/print/pdf/node/3537), with the article explicitly declaring its MSME analytical convention. This targeted edit does not imply fresh verification of every historical citation or legal statement in the research corpus.

## Verification and recovery

- [Resolution manifest](PENDING_CHANGES_RESOLUTION_2026-09-28.json): initial scope, file/archive hashes, curated PDFs, local-link checks and before-edit backups.
- [Publication-layer QA](PUBLICATION_BUILD_VALIDATION_2026-09-28.json): syntax, actual header integration, isolated compile, page order and visual review. It is not a full whitepaper-validation report.
- The 13 archived additional screenshots also matched their recorded hashes during the review.
- Original pending Markdown copies are preserved under `_archive/pending-resolution-2026-09-28/before-edit/`; the stray-file archive is beside them.
- Historical retirement sources remain under `_archive/2026-09-22-source-retirement/`.

These archives remain local and ignored. The four dated reading PDFs are curated distribution copies, while their owning repositories control subsequent source development.

## Related RegTech comparison

The requested [Documents-versus-Downloads RegTech comparison](REGTECH_PROJECT_COMPARISON_2026-09-28.md) found four identical core manuscripts and useful unique material in each project. The earlier extraction did not incorporate the Documents repository's history and publication assets. A proposed consolidation is documented; neither RegTech tree was changed during this comparison.

## Git boundary

Only Mwendo changes are included in this resolution. The sibling Underwrite, Bayesian and KESONIA repositories, the Documents RegTech repository, and the guest financial-material and business/blog website repositories were not edited or committed. The existing `codex/repository-separation` branch is the publication target; `main` is not merged by this task.
