# Reproducible 4G-inspired merchant finance case

This case follows twelve synthetic merchants from financed inventory to sales, receipts, repayment, repeat lending and workout. A paired lender ledger measures funding, collected fees, operating costs, realised credit loss and guarantee cash under seven scenarios. It supports the 4G Capital application of Underwrite for Collection.

## Run and verify

Python 3.10 or later is sufficient. The model uses the Python standard library.

From the repository root:

```powershell
python -B research_lab/four_g_merchant_finance_case/run_case.py
python -B -m unittest discover -s research_lab/four_g_merchant_finance_case -p test_model.py -v
```

The runner writes to `output/four_g_merchant_finance_case_2026-10-16`. Use `--inputs` and `--output` to run a separate assumption set and retain the published case.

## Economic conventions

- Currency is KES. Merchants trade for 180 days; the ledger follows claims and recovery through day 300.
- The initial KES100,000 facility pays the distributor. Inventory enters the merchant balance sheet, while customer settlement enters merchant cash.
- First-cycle cash is 20,000 + 125,000 - 4,200 - 3,150 - 100,000 - 5,000 = KES32,650.
- Daily operating costs accrue even when cash is insufficient. Workout cash pays accumulated operating bills and preserves the KES10,000 operating floor before repayment of residual loan principal. This priority is an explicit teaching assumption.
- Repayment applies to principal before fees. A repeat facility requires the previous cycle to settle, its sales and receipts to finish, the cooling-off period to pass, and the cash gate to be met. Loan limits are bounded by the parameter file.
- The model reports realised lender contribution before tax, allocated central overhead and a capital hurdle. Its separate cash and balance reconciliations identify performing loans, unresolved default principal, unpaid fees and unsettled claims.
- Support changes stated stock-conversion assumptions and incurs a stated delivery cost. Its effect is a scenario input for subsequent empirical evaluation.

## Guarantee convention

The teaching schedule uses a KES4.44m cumulative origination inclusion budget, a first layer of KES220,000 with KES200,000 maximum protection and a second layer of KES4.22m with KES420,000 maximum protection. Public IFC disclosures motivated the layer proportions. The KES scale and operating conventions are author-selected parameters.

Each eligible default receives the increment in cumulative layer protection. Claim submission, acceptance and settlement have separate dates. Recovery before settlement adjusts the claim; recovery after settlement generates a remittance. The elected contract retains used capacity after recovery. The severe-shock case exercises both layers and recovery sharing. The delayed-sales timing comparison isolates a thirty-day versus ninety-day settlement lag.

## Outputs and tests

`scenario_summary.csv` contains fourteen rows: seven scenarios, each with and without protection. Each scenario folder includes merchant daily records, a loan ledger and paired lender cash ledgers. Scenarios with claims also include claim and guarantee-event records. `verification.json` records the exact source and assumption hashes used for that run.

The 24 tests cover the first-cycle calculation, merchant cash and wealth, inventory and receivables, operating payables, principal, lender cash and contribution, repeat eligibility, layer boundaries, recovery timing, unsettled claims and deterministic reproduction.

The final publication refresh on 18 October 2026 regenerated outputs from the tested source. Delayed-sales contribution is KES190,858 with protection and KES124,471 without it. The correlated-shock contributions are KES-568,864 and KES-819,526 respectively. These replace earlier exported figures that preceded the operating-payables treatment.

Charts are generated from these ledgers by `research_lab/partner_case_visuals/build_four_g_case_charts.py` using Pillow and Arial. The six PNGs are saved in `publications/industry-engagement/4g_2026-10-13/charts`.

## Sources and licence

- Underwrite for Collection: https://doi.org/10.5281/zenodo.23343888
- 4G Capital KUZA: https://www.4g-capital.com/kuza
- 4G Capital UPIA: https://www.4g-capital.com/upia
- IFC project disclosure 53511: https://disclosures.ifc.org/project-detail/SII/53511/mfp-cflg-4g-cap

Author: Nevil Maloba, Philtechent Limited. Contact: nevilmaloba@philtechent.com.

The article and presentation follow the project's Creative Commons Attribution-NonCommercial-ShareAlike 4.0 licence. Source code follows the repository's applicable code licence.