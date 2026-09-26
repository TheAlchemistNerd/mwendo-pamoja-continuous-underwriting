# PDF cleanup — 25 September 2026

**Completed in the main project only.** Nine PDFs, totalling 31,845,854 bytes (about 30.4 MiB), were moved into `_archive/pdf_cleanup_2026-09-25/`. Their original directory structure is retained and every archived file passed SHA-256 verification. This consolidates historical material without permanently deleting it or claiming disk-space savings.

There were no PDFs directly in the project root. The initial recursive listing found 31 PDFs including existing archives, backups and the inner Underwrite copy. No PDFs are currently tracked by the main Git repository; generic generated PDFs are ignored.

## Archived files

| Original location | Reason |
|---|---|
| `output/pdf/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-30.pdf` | Historical export; identical to its historical dist counterpart |
| `output/pdf/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-30_Rev3.pdf` | Historical export; identical to its historical dist counterpart |
| `whitepapers/mwendo-pamoja/dist/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-30.pdf` | Earlier 186-page edition |
| `whitepapers/mwendo-pamoja/dist/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-30_Rev2.pdf` | Earlier 186-page revision |
| `whitepapers/mwendo-pamoja/dist/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-30_Rev3.pdf` | Earlier 186-page revision |
| `whitepapers/mwendo-pamoja/dist/Mwendo_Pamoja_Continuous_Underwriting_White_Paper_2026-08-31_Rev4.pdf` | Earlier 186-page revision |
| `output/pdf/Bayesian_Credibility_and_Exposure_Normalised_Telematics_Relativities.pdf` | Earlier 42-page export; later licensed publication and submission copies retained |
| `revised_with_sources/tmp/pdfs/UNDERWRITE_FOR_COLLECTION.pdf` | Temporary byte-identical copy of the retained practitioner article |
| `scratchpad/rendering-qa/whitepaper/pdfs/whitepaper-debug.pdf` | Historical rendering diagnostic |

The [machine-readable move manifest](PDF_CLEANUP_2026-09-25.json) records original/archived absolute paths, sizes, checksums, reasons and completion status. The archive contains its own copy of the manifest. Restoration should follow those explicit paths and refuse to overwrite any subsequently regenerated file.

## Preserved

- The three dated publication editions in `publications/pdfs/`.
- The dated Mwendo edition in `whitepapers/mwendo-pamoja/dist/` and Bayesian build PDF. These differ from their publication counterparts; they were not treated as byte-identical clutter.
- The Brian Hey submission PDF and KBA concept/proposal PDFs.
- The original practitioner article in `publications/linkedin/` and the KBA call-for-papers source.
- Existing revision archives and backups.
- All files within the inner Underwrite integration copy and the standalone Downloads repositories.

Only first-page text, page counts and file hashes were inspected for the publication/build comparison; this was not a page-by-page content equivalence audit. The root README's pre-existing link to a nonexistent `..._Final.pdf` was replaced with a link to the existing dated publication edition. The [publication index](../../publications/pdfs/README.md) identifies the retained reading copies.
