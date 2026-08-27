# Repository Reorganization Record

## Scope

On 27 August 2026, the Mwendo Pamoja working directory was reorganized for a private-first remote repository. The operation separated canonical sources, controlled documentation, research, financial artefacts, publication sources, local history, and reproducible working output.

No source or deliverable was deleted during the move.

## Safety snapshot

The pre-reorganization state is preserved locally at:

```text
_archive/2026-08-27_pre_repository_reorganization/
```

`SHA256_MANIFEST.json` records relative paths, byte sizes, and hashes for 184 files totaling 38.49 MB. The snapshot deliberately excludes `.git`, `_archive`, `node_modules`, PDF-rendering temporary files, and the Mermaid cache. Those exclusions are reproducible dependencies or working caches rather than unique source material.

## Classification policy

- Canonical narrative papers and the final reviewed PDF moved to `whitepapers/mwendo-pamoja/`.
- The standalone actuarial paper and research note moved to `whitepapers/telematics-relativities/`.
- Transaction documents moved to `docs/transaction/`.
- Controlled specifications and governance ledgers moved to `docs/controlled-specifications/` and `docs/governance/`.
- KESONIA, RegTech, data, Bayesian, and neural research moved to `docs/research/`.
- The SPV workbook and its source moved to `financial_models/spv/`.
- The lender-deck generator moved to `presentations/lender-dfi/source/`; the unapproved PPTX moved to `_archive/`.
- Public article editions moved to `publications/linkedin/`.
- Backups, superseded artefacts, raw Word conversions, and extracted media moved to `_archive/`.
- Scratch plans, renderings, caches, logs, inspection output, and transient files moved to `scratchpad/`.

## Historical files

The deleted `Book_1` through `Book_3`, legacy outlines, `Strategic_Execution_Plan.md`, and `project_finance_pitch_and_outline.md` remain recoverable from Git history. They were not restored into the canonical tree because their material is superseded by the current white-paper parts, transaction documents, controlled specifications, and implementation records.

## Remote policy

The repository has no remote configured at the time of this record. Its history already contains transaction and financing documents, so the current repository should be pushed only to a private remote. A public version should be created as a separate sanitized publication repository.
