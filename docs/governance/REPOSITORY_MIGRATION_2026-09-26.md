# Repository migration — 26 September 2026

The saved split plan has been implemented. The three independent projects sit side by side in Downloads. Mwendo retains its core white paper, controlled specifications, programme research and SPV model. Neither guest repository was edited, copied into, cleaned, staged or committed during this migration.

## Authoritative locations

| Project | Working repository | Result |
|---|---|---|
| Mwendo Pamoja | [Current repository](../../README.md) | Retains the programme and shared controlled specifications; former extracted locations now point to their owners. |
| Underwrite for Collection | [Standalone repository](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/README.md>) | Existing Git history retained; active series restored to `series/`. |
| Bayesian telematics relativities | [New standalone repository](<C:/Users/Nevo/Downloads/bayesian-telematics-relativities/README.md>) | Canonical paper, derivations, figures, validation, submission package, experiments and dated Bayesian publication. |
| RegTech–KESONIA Treasury | [New standalone repository](<C:/Users/Nevo/Downloads/regtech-kesonia-treasury/README.md>) | Four-part series, research notes, Treasury review/casebook, source pastes and arithmetic checks. |

`financial material` and `business and technical website blog` remain guest repositories. Existing SokoIntel and Owner Earnings material there has not been reorganized by this task. No remote repository has been created and no push has been made.

## Scoped local commits

| Repository | Migration commit | Branch |
|---|---|---|
| Bayesian telematics relativities | `4b8d9ab` | `codex/repository-separation` |
| RegTech–KESONIA Treasury | `dc4ef18` | `codex/repository-separation` |
| Underwrite for Collection | `8b0676d` | `codex/repository-separation` |

The parent migration commit records the source retirement, navigation files and audit documents. Existing unrelated main-repository modifications remain unstaged; the working README and ignore-file wording were updated for navigation without incorporating their earlier changes into this commit. The two new repositories have clean working trees. Underwrite retains the pre-existing PDF deletions and older untracked review noted below.

## What changed

### Underwrite

The standalone repository's `source_library/series/` working files were moved back to the Git-tracked `series/` path. Its frozen source-library comparators were preserved. Three newer items were copied from the inner integration folder: the September 25 pricing/content review, collectability/re-verification feedback note, and feedback image. Of the standalone files checked, 133 retained their exact bytes; intentional edits were limited to the root README and build-root correction, with additional migration documentation.

The shared historical SHA-256 list differed in path prefixes. The standalone list and its two additional historical manuscripts were retained. Both variants remain recoverable in the archive. The PDF build now places scratch output inside the Underwrite repository rather than Downloads.

Two historical PDF paths were already absent from the standalone working files, and the September 23 review was already untracked. Those pre-existing changes are preserved outside the scoped migration commit.

### Bayesian and KESONIA

The new repositories start from explicitly recorded **working-tree snapshots**, including unpublished changes. They do not imply that every copied file existed at the originating Mwendo commit `1420ffef345910e90aad8fad28c8acc537cad248`. Source history remains in Mwendo, with additional local Git bundles for recovery.

105 selected source/package files were checked before and after copying; 115 staged files included the new entry points and provenance documents. Existing directory layouts were retained so publication builds and submission discovery continue to resolve their local inputs. Links in research notes were rebased where needed. Original pasted texts, scientific manuscripts, experiment results and historical evidence records retain their source content.

The Treasury renderer now writes only its local reading pack. Its former cross-project distribution and historical-manifest mutation were removed. Dated HTML files were rebuilt after installation; their final hashes therefore differ from the copied historical exports. The migration validation records that distinction explicitly.

### Former working locations and PDF clutter

Five old trees were moved into `_archive/repository_migration_2026-09-26/retired/`: the inner Underwrite tree, Bayesian paper tree, Brian Hey package, KESONIA research tree, and Treasury reading pack. **237 archived source files passed hash verification.** The archival move also preserves generated intermediates and Office locks; those were not imported as active sources.

The old locations now contain small navigation files, including 143 document pointers, so existing reading links can lead to the new authoritative copies. These folders are not second editable research trees and are not Git submodules or junctions. Dated PDFs in `publications/pdfs/` remain distribution copies. The [earlier nine-file PDF cleanup](PDF_CLEANUP_2026-09-25.md) remains complete; it was not repeated.

## Verification and limitations

| Check | Result |
|---|---|
| Copied selected files and archived originals | SHA-256 preservation verified. |
| Bayesian canonical paper | Passed: 10,133 body words, 51 references, 43 equations, seven Mermaid figures. |
| Brian Hey submission | Existing structural/result checks reach the canonical-paper hash gate; that gate fails with the same hash before and after extraction. Expected hash was not reset. |
| Treasury arithmetic | All illustrative calculation assertions passed. |
| Treasury HTML | Eight local reading documents rebuilt successfully with Pandoc. |
| Python syntax | Eight imported Python files parsed. |
| Underwrite PDF build script | PowerShell syntax parsed; project-root path corrected. |

This was a repository migration, not a full PDF re-render or empirical validation of credit, insurance or Treasury models. The submission's pinned canonical hash still requires a deliberate baseline reconciliation before claiming a clean submission validation.

## Recovery and audit records

- [Pre-migration Git state](migrations/2026-09-26/pre_migration_state.json)
- [Source and destination transfer manifest](migrations/2026-09-26/transfer_manifest.json)
- [Validation report](migrations/2026-09-26/validation_report.json)
- [Archive and navigation report](migrations/2026-09-26/retirement_report.json)
- Local recovery bundles: `_archive/repository_migration_2026-09-26/mwendo_pre_migration.bundle` and `underwrite_pre_migration.bundle`.
- Original standalone series snapshot: `_archive/repository_migration_2026-09-26/underwrite_standalone_series_before/`.
- Each new repository includes its own migration manifest, source-history record and validation summary.

Archives are local recovery material and remain ignored by Git. The new repositories' snapshot commits protect their selected working sources; they do not replace a separate backup of local archives.

## Remaining research work

Repository separation does not complete the scientific and editorial backlogs. Continue the existing Bayesian correction/implementation ledger, Underwrite publication plan and KESONIA 18-item remaining-work register in their owning repositories. The cumulative screenshot catalogue remains a separate research follow-up. A separate mortgage-research repository, separate SPV engine and separate IFRS 17 repository remain deferred, as recorded in the split plan.
