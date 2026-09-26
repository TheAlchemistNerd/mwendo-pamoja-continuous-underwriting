# Repository boundaries and proposed independent projects

> **Implemented on 26 September 2026.** The approved Underwrite reconciliation and Bayesian/KESONIA extractions are complete. See [the migration record](REPOSITORY_MIGRATION_2026-09-26.md). The remainder of this document preserves the original planning assessment and its pre-migration observations; statements below about proposed folders or unperformed moves describe that earlier state.

**25 September 2026 | Read-only repository comparison and proposed split plan**

## Confirmed working boundary

The user has selected **independent repositories side by side in Downloads**. This note records proposed boundaries; it does not create repositories or move project source trees.

This task's writable project is `C:/Users/Nevo/Downloads/insuretech & embedded finance`. The user has instructed that guest repositories, including the business/blog website and financial-material projects, must not be changed. This boundary supersedes the earlier instruction to copy relevant reviews into those projects. No further file copies, edits, cleanup, staging, commits or pushes should be performed in guest repositories without a new explicit instruction. Read-only inspection is appropriate when the user asks for a comparison.

No Git commits or pushes were made during this review, the preceding SokoIntel comparison, or the reader-feedback review. Existing modifications and history were inspected without resetting or staging them.

## Repositories identified

| Directory under Downloads | Git status and role | Treatment in this task |
|---|---|---|
| `insuretech & embedded finance` | Main repository; HEAD observed as `1420ffe`, dated 3 September 2026; existing tracked modifications and deletions present | Main project work only; stage by explicit ownership if a commit is later requested |
| `behavioural credit scoring - underwrite to collect rct` | Separate repository; HEAD observed as `4d3ea5c`, dated 15 September 2026 | Read-only comparison; reconcile its uncommitted relocation before treating the layout as settled |
| `business and technical website blog` | Separate repository; includes SokoIntel product architecture | Guest: no further changes, commits or cleanup |
| `financial material` | Separate repository; includes Business Credit and Owner Earnings projects | Guest: no changes, commits or cleanup |

The repository inside which this task runs contains a same-named Underwrite folder, but that inner folder **has no `.git` directory**. The main `.gitignore` explicitly excludes it as a local integration mirror. Changes inside it are therefore not included in an ordinary main-repository commit.

## The two Underwrite folders: confirmed difference

### Inner integration copy

`C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct`

Its active manuscripts and research notes are under `series/`. It is a real directory, not a symlink or an independent Git checkout.

### Standalone repository

`C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct`

It has its own Git history. Its current working tree has the series under **`source_library/series/`**, while Git still tracks the old **`series/`** locations. Consequently, status reports the old tracked files as deleted and the relocated directory as untracked. The check does not establish who moved them or whether that move was intended.

This location also conflicts with its README's stated role for `source_library` as frozen source copies. The active-series layout and tracked paths need deliberate reconciliation; the apparent deletions should not be committed blindly.

### Content comparison

Compared active editorial/source text under the inner `series/` with the standalone `source_library/series/`, excluding generated output, builds, revision snapshots and reference-copy trees:

- **48 shared files are byte-identical**, including the six existing manuscript parts.
- **No differing files** were found among those 48 shared paths.
- **Two newer research notes exist only in the inner copy:**
  - `research/ADDITIONAL_PRICING_REVIEW_AND_CONTENT_PLAN_2026-09-25.md`
  - `research/COLLECTABILITY_FEEDBACK_AND_CONTINUOUS_REVERIFICATION_2026-09-25.md`

The preserved feedback image also belongs to the recent local review; images were outside this text comparison. This is not a claim that every binary, build, archive or source-library file is synchronized. The detailed comparison is in [the audit manifest](UNDERWRITE_FOLDER_COMPARISON_2026-09-25.json).

**Conclusion:** the directories represent one research series with two working locations, not two independent editions of the research. The existing standalone Git repository is the intended independent project, but the inner copy cannot yet be retired as a redundant folder. Reconciliation must preserve the two newer notes, source evidence and current working changes.

## Recommended new repositories

Names are suggestions, not directories created by this task.

| Proposed repository | Recommendation | Material and boundary |
|---|---|---|
| `bayesian-telematics-relativities` | **First extraction candidate** | Own the actuarial paper, derivations, model/validation code, mathematical examples, figures, build and submission preparation. Start from `whitepapers/telematics-relativities/`, plus explicitly inventoried publication/submission assets. |
| `regtech-kesonia-treasury` | **Second candidate, after its scope is agreed** | Own the RegTech–KESONIA series, benchmark/curve/FTP examples, controlled Treasury specifications and implementation tests. Start from `docs/research/kesonia/`; incorporate review material selectively. Institution-specific legal and regulatory applicability remains explicit. |
| `credit-lifecycle-research` | **Conditional later split** | Potential home for independently reproducible Fannie Mae/Freddie Mac experiments, data dictionaries, extraction code, validation and research papers. Create only if those research outputs need a lifecycle distinct from the Underwrite series; otherwise retain a research module there. |
| `mwendo-spv-model` | **Keep within Mwendo for now** | The existing `financial_models/spv/` is closely coupled to Mwendo's products, eligibility, transaction terms, reserves and waterfall. A standalone engine becomes useful when multiple distinct transactions require a stable shared interface. |
| Separate IFRS 17 repository | **Keep with the relevant insurance research for now** | An accounting interface in the Bayesian paper does not itself justify a new project. Reconsider when there is an independently specified and tested accounting/measurement product. |
| SokoIntel, Owner Earnings or Business Credit extraction | **Outside this task** | These belong to guest projects. No restructuring or new repository is proposed inside them here. |

Bayesian relativities is the strongest candidate because its writing guide already defines a standalone paper, audience and methodology. Its folder contains `paper.md`, `Mathematical_Derivations.md`, `validate.py`, scripts, a detailed implementation plan, a correction ledger and a Brian Hey submission plan. It has 21 files tracked by the main repository at the inspected state. Its own release and research schedule can develop independently while Mwendo cites it as a dependency.

RegTech–KESONIA has a distinct four-part series and Treasury review programme. Its 18-item remaining-work register is a backlog, not a requirement to implement all of bank risk management before a first release. An initial independent scope should identify the benchmark/curve/FTP calculations and the intended institutional users.

## Intended layout

```text
C:/Users/Nevo/Downloads/
├── insuretech & embedded finance/                  existing Mwendo repository
├── behavioural credit scoring - underwrite to collect rct/  existing independent repository
├── bayesian-telematics-relativities/               proposed first split
├── regtech-kesonia-treasury/                        proposed second split
├── financial material/                            guest; unchanged
└── business and technical website blog/            guest; unchanged
```

Each independent project should have one authoritative working tree and its own Git history. The main project can retain a small dependency index naming the source repository and version, rather than a second editable mirror. A cross-project review belongs in the repository that owns the change, with links from related work. A shared theorem or financial convention should be cited and versioned rather than repeatedly rewritten.

## Safe extraction sequence for a later migration task

1. Inventory the selected source, its tracked history and all uncommitted work. Assign publication assets, tests and build dependencies to an owner.
2. Decide whether the new repository should retain relevant history or begin from an explicitly recorded snapshot. The current working changes must be preserved either way.
3. Create the selected sibling checkout, copy the agreed complete source set, compare hashes and verify its build/reference paths independently.
4. Record the originating commit, migration manifest, dependencies and new authoritative location.
5. Only after verification, replace the old editable location with a short pointer or archive it under a documented retirement record. Do not keep two unlabelled active copies.
6. Commit separately in each explicitly authorized repository, with no blanket staging across projects. Create or push a remote only as part of the requested migration scope.

For Underwrite, first reconcile `series/` versus `source_library/series/` and account for the newer local notes. This audit did not perform that repair or alter the standalone repository.

## Completed PDF cleanup

Nine historical exports, duplicate renderings and a diagnostic PDF were archived within the main repository's ignored local archive. Source papers, published editions, submission documents, the inner Underwrite folder and all standalone/guest repositories were preserved. See [cleanup record](PDF_CLEANUP_2026-09-25.md).
