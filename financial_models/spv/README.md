# Mwendo Pamoja SPV Financial Model

This directory retains the illustrative 36-month SPV workbook, its model guide, generator source, and concise formula audit.

## Status

The workbook is a structuring and diligence prototype. It demonstrates product schedules, collections, losses, debt service, reserves, overcollateralisation, waterfall priority, covenants, returns, and source tracking. It is not an executed financing model and should not be used for lender reliance until provisional assumptions and structural terms are replaced with validated evidence.

The current generator records assumptions from the modelling iteration in which it was produced. A controlled next revision should reconcile the HoldCo overlay and rate conventions to the latest term sheet and white-paper baseline, validate the IPF receivable perimeter, and independently review all cohort, tax, reserve, debt, and waterfall formulas.

## Build source

The generator uses the OpenAI artifact runtime and the Financial Budget reference workbook. Set the reference workbook explicitly rather than relying on a machine-specific path:

```powershell
$env:FINANCIAL_BUDGET_TEMPLATE = 'C:\path\to\reference.xlsx'
node .\financial_models\spv\build\build_workbook.mjs
```

Set `MWENDO_MODEL_OUTPUT_DIR` to redirect generated output. Without it, the generator writes to this directory.

## Version-control policy

The canonical `.xlsx` is intentionally tracked because it contains substantive SPV formulas and assumptions. Preview images, inspection streams, Office lock files, and intermediate recalculation copies are ignored or retained only in the local archive.
