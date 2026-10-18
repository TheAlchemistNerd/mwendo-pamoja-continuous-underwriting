# Mobility fleet: 156-week operating and financing case

Hypothetical deterministic research case; all numerical inputs are author-selected, with no Moove calibration. Currency: KES.

All figures are author-selected scenario calculations. Three perspectives are linked by the same dated transfer ledger: driver, operator/equity and funder.

| Measure | uninterrupted | scheduled_repair | expedited_repair | expedited_repair_fee_credit |
|---|---:|---:|---:|---:|
| unavailable days | 0 | 12 | 2 | 2 |
| peak arrears | 0.00 | 50,000.00 | 0.00 | 0.00 |
| cure week | None | 32 | None | None |
| collected fees | 3,900,000.00 | 3,900,000.00 | 3,900,000.00 | 3,875,000.00 |
| driver cash surplus | 468,000.00 | 399,428.57 | 456,571.43 | 481,571.43 |
| household shortfall | 0.00 | 0.00 | 0.00 | 0.00 |
| driver terminal vehicle value | 450,000.00 | 450,000.00 | 450,000.00 | 450,000.00 |
| additional equity | 0.00 | 62,926.46 | 26,472.67 | 51,472.67 |
| equity net cash | 1,043,186.46 | 1,013,186.46 | 1,008,186.46 | 983,186.46 |
| equity npv | 640,726.60 | 610,510.28 | 607,145.30 | 583,158.65 |
| funder npv at contract rate | -0.00 | -0.00 | -0.00 | -0.00 |

Repair time is an input assumption. Contract bills, actual collections and arrears have separate columns. Covered repair costs are paid by the operator. The driver receives the terminal vehicle once the specified completion conditions are met; its value is recorded as a non-cash asset, and the operator receives zero residual sale cash in those runs.

NPVs use dated cash flows. Operator equity NPV discounts at the supplied 18% annual effective rate; funder NPV uses its supplied 12% funding rate. Driver cash NPV uses 10%, with essential household consumption reported separately. Driver wealth NPV adds the conditional terminal vehicle value.

The CSV files retain every weekly state and every transfer. Input and implementation hashes are recorded in verification.json.
