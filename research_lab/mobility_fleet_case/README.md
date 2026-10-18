# Mobility fleet: full-contract operating and financing case

This reproducible application accompanies [the standalone research note](../../docs/research/MWENDO_MOBILITY_FLEET_APPLICATION_AND_WORKED_CASE_2026-10-13.md). It extends Mwendo Pamoja to a bundled vehicle-ownership arrangement with 156 weekly payments. All values are hypothetical author-selected inputs. Public descriptions of Moove motivate the application; actual Moove contract terms and performance data would support subsequent calibration.

## Run

From the repository root, using Python 3.10 or later:

```text
python research_lab/mobility_fleet_case/run_case.py
python -m unittest discover -s research_lab/mobility_fleet_case -p test_model.py -v
```

Python's standard library supplies Decimal arithmetic, JSON, CSV and reporting. The maintained calculation is the Python case. The existing six-period Mwendo case continues to illustrate its three-product and receivables-pool structure.

Default output: `output/mobility_fleet_case_2026-10-13/`

- `00_MOBILITY_FLEET_CASE.html` and `.md`: readable comparison.
- `results.json`: exact results, weekly balances and actor transfers.
- Four `*_weekly_ledger.csv` files: 156 weeks per scenario.
- Four `*_transfers.csv` files: every source, recipient, amount and purpose.
- `inputs.json` and `verification.json`: frozen assumptions, implementation hashes and cash-check results.

The committed `baseline_verification.json` preserves the tested baseline results. Rerunning produces the same scenario values and cash identities. Output is rounded only for display; calculations retain 40-digit Decimal precision. Contract-specific currency rounding is an explicit future integration choice.

## What is being tested

The operator buys a KES 1.8 million vehicle using a KES 1.35 million amortising loan and equity. Equity also funds setup and opening operating cash. The driver pays a fixed KES 25,000 weekly package and receives vehicle ownership at completion when the stipulated conditions are met. The operator pays annual insurance premiums, routine maintenance, administration and the covered mechanical repair. Energy, platform charges and essential household consumption belong to the driver's cash account.

The control has full availability. Two scenarios assume 12 or two unavailable days after the same shock; the operator pays KES 30,000 or KES 35,000 respectively. A fourth scenario adds an authorised one-week fee waiver. The downtime response is supplied as a scenario input; a pilot would estimate the causal repair effect.

The calculation preserves four separate objects: contractual bill, actual collection, unpaid balance and shareholder cash. Faster repair improves driver surplus and reduces the additional equity needed to sustain the operator's cash policy. The higher repair expense still reduces operator NPV in the baseline where both collection paths ultimately cure. The result identifies the commercial evidence needed for pricing and benefit-sharing.

## Contract elections and interpretation

- Seven calendar days define a model week; the full-availability revenue is a scenario capacity, with safe hours and real working patterns supplied by a pilot.
- Household need is paid before package collection. Collections also preserve a KES 10,000 wallet floor where funds allow. Household shortfalls are reported explicitly in severe stress.
- Routine maintenance and the shock repair are separate operator payments. The shock repair is covered within the package and adds zero driver debt.
- Premiums are paid at weeks 1, 53 and 105. A cash target builds toward the next premium, alongside KES 50,000 operating liquidity. This cash target is an internal funding policy.
- Sponsor equity calls explicitly meet every shortfall under that policy. The outputs show the required commitment; funder repayment in a stress scenario depends on those calls being funded. A hard commitment cap and lender default path are further contractual extensions.
- The funder's loan amortises in equal principal amounts; its effective annual interest rate is 12%. Customer fees are fixed. No interest benchmark is imported into the customer contract.
- At successful completion, the KES 450,000 vehicle value belongs to the driver and appears once as a non-cash wealth item. If conditions fail, the elected terminal scenario returns and sells the vehicle for the operator, with KES 25,000 disposal cost. Outstanding driver fees remain visible pending their own resolution.
- Net present value uses cash timing, with 18% for operator equity and 10% for driver cash. Household consumption is reported alongside driver surplus. The vehicle book-value proxy is a simple depreciation assumption for this economic case; the accounting owner determines recognition and classification.
- Ring-fenced receivables financing is an optional additional contract layer described in the research note. This case's funder lends to the operator.

## Sensitivity runs

Copy the baseline inputs, edit supported numeric assumptions, and use a separate destination:

```text
python research_lab/mobility_fleet_case/run_case.py --inputs scratchpad/mobility_sensitivity.json --output output/mobility_sensitivity
```

Supported changes include fees, costs, discount rates, debt amount, wallet/cash policy, repair expense, downtime within the term and dated fee waivers. A different contract architecture, early termination, taxes, insurance claim recoveries, arrears interest, monthly rather than weekly periods, or capped sponsor funding would call for a separately specified and tested extension.
