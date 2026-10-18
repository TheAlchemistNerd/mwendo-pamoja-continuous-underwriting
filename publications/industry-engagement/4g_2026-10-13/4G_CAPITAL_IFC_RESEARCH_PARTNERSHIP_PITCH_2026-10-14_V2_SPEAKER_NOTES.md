# 4G Capital × Underwrite for Collection

## Speaker notes

Updated18October2026. All model results are synthetic teaching calculations.

## Slide 1

The proposed research partnership uses Underwrite for Collection as its organising framework. The completed synthetic case is available for joint review and adaptation to an agreed product. All merchant performance and commercial terms in the calculations are author-selected teaching assumptions.

Sources
[1] N. Maloba, Underwrite for Collection: MSME Credit Lifecycle Whitepaper, 2026. doi: 10.5281/zenodo.23343888. https://doi.org/10.5281/zenodo.23343888

[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 2

These questions connect the customer operating cycle to portfolio strategy. The first task measures the source of repayment. The second estimates the effect of a decision. The third evaluates the lender economics of risk sharing and the extent to which it supports additional lending.

Sources
[1] N. Maloba, Underwrite for Collection: MSME Credit Lifecycle Whitepaper, 2026. doi: 10.5281/zenodo.23343888. https://doi.org/10.5281/zenodo.23343888

[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

[10] World Bank and FIRST Initiative, Principles for Public Credit Guarantee Schemes for SMEs, 2015. https://www.worldbank.org/en/topic/financialsector/publication/principles-for-public-credit-guarantee-schemes-cgss-for-smes

## Slide 3

Public products and SII were checked on18 October 2026. IFC disclosure narrative describes a $44.4m-equivalent portfolio and up to$6.2m maximum risk, whereas the indicative Board table displays$8.2m. Use the dated executed agreement to configure the actual programme.

Sources
[2] 4G Capital, UPIA: 30-Day Working Capital Business Loans. Accessed 18 October 2026. https://www.4g-capital.com/upia

[3] 4G Capital, KUZA: Embedded Retail Credit for Distributors. Accessed 18 October 2026. https://www.4g-capital.com/kuza

[4] IFC, MFP-CFLG-4G CAP, Summary of Investment Information, project 53511, updated4July2026. Accessed18 October 2026. https://disclosures.ifc.org/project-detail/SII/53511/mfp-cflg-4g-cap

## Slide 4

All listed commercial values are synthetic. Six stable merchants, three delayed merchants and three vulnerable merchants share the baseline. Scenario shocks start in cycle 3. One merchant is guarantee-ineligible. Origination stops on day 160 and guarantee inclusion on day 150. The model separately records inventory, receivables, accrued operating expenses and household shortfalls.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 5

The first cycle leaves KES 32,650 after repayment
C21=20,000+125,000−4,200−3,150−100,000−5,000=32,650. Distributor payment creates inventory directly. Principal movement is financing and sales revenue is operating inflow. The first cycle assumes all stock sells and the receipts settle before repayment.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 6

The implemented gate is deterministic cash arithmetic using information from completed cycles. It is not fitted Bayesian or causal estimation. A later validated probabilistic extension can place predictive intervals around turnover, margins and cash and carry those intervals to authorised staff. Model code retains operating expense arrears and household shortfalls so loan repayment does not hide unpaid commitments.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 7

Repeat loans and defaults change with trading conditions
Baseline:72loans,60repeat,0defaults. Delayed sales:60loans,48repeat,3defaults. Support plus extension:66loans,54repeat,0defaults. Common severe shock:36loans,24repeat,12defaults. Support outcomes follow stated assumptions and motivate a prospective impact study.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 8

Merchant cash reveals the consequences of each lending decision
V01 provides one merchant trajectory. Opening merchant cash is KES 20,000. Cash declines and repeat eligibility changes when trading slows. The supported case assumes improved sell-through and changed timing. Inventory, operating arrears and household shortfalls accompany cash in the exported ledgers.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 9

Support assumes92% sell-through,25%markup,24sellingdays and3settlement-lagdays for affected loans, plus a14-day extension. These assumptions are not an estimated causal treatment effect. The experimental literature supports evaluating the design of business training locally. Preserve completed and censored cycles, cluster dependence, spillovers and intervention costs in the protocol.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

[6] F. Campos et al., Teaching personal initiative beats traditional training in boosting small business in West Africa, Science,357(6357),1287-1290, 2017. doi: 10.1126/science.aan5329. https://doi.org/10.1126/science.aan5329

[7] M. A. Hernan and J. M. Robins, Causal Inference: What If, Chapman & Hall/CRC, 2020. https://miguelhernan.org/whatifbook

## Slide 10

Contribution=collected fees−origination−servicing−collection−support−funding−guarantee fees−written-off principal+borrower recovery+guarantee cash−recovery remittance. Baseline414000−39024−52377.2615−2502.7397=320095.9988. Delayed-sales316500−33936−44280.9194−2633.9427−44790.9091=190858.2288. Rounded displayed rows can differ byKES 1.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 11

Scenario contribution compares the same merchant paths with and without protection
Each protected/unprotected pair keeps merchant behaviour identical. Protection changes guarantee cash, fees and the funding path. It does not change default outcomes within a pair. Negative severe-shock contribution makes retained concentration risk visible.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 12

Every result derives from the same exported summary. The case reports realised contribution, not a calibrated return forecast for4G. The severe scenario has12defaults and KES 590058.453 retained credit loss after guarantee benefit and recovery. These comparative results identify what a proposed pilot would measure and validate.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 13

The publicly disclosed first/second layer proportions motivate this KES scale illustration. The KES values are independent teaching amounts, not a currency conversion ofIFC commitments. Processing delays, fees, eligibility, ordering and recovery allocation are selected conventions. The executed agreement would control the actual implementation.

Sources
[4] IFC, MFP-CFLG-4G CAP, Summary of Investment Information, project 53511, updated4July2026. Accessed18 October 2026. https://disclosures.ifc.org/project-detail/SII/53511/mfp-cflg-4g-cap

[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

[10] World Bank and FIRST Initiative, Principles for Public Credit Guarantee Schemes for SMEs, 2015. https://www.worldbank.org/en/topic/financialsector/publication/principles-for-public-credit-guarantee-schemes-cgss-for-smes

## Slide 14

Claim settlement and recovery have separate cash dates
Delayed-sales loan V01-C03 defaults day 107 with KES 37,900 unpaid principal. Claim allocation KES 34,454.545 follows submission112, acceptance122 and settlement152. That scenario has no borrower recovery after the model settles operating arrears. In the common severe shock, D01-C03 receives KES 67,727.273 on day 152 and remits KES 4,727.273 after recovery on day 167. Aggregate severe recoveries are KES 62,400 and remittances KES 18,124.330.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 15

Settlement lags run from acceptance.30-day settlement occurs day 152;90-day settlement occurs day 212. Both delayed-sales cases have no post-default borrower recovery and receive KES 68,909.09 guarantee cash. Clearing operating arrears before the recovery event leaves no recovery surplus in this scenario. Retained loss is identical KES 44,790.91. Additional funding is204.1637. These amounts are a timing comparison within the simulation.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 16

Funding follows disbursements, collections and settled claims
Lender starts with zero cash, draws borrowing as needed, and repays debt with incoming cash. Funding accrues at12%annual on opening debt. Delayed-sales protected peak isKES 1361758.53. A claim receivable remains separate from cash. The severe scenario leaves closing borrowing ofKES 568864.42.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 17

Gross loss894000 minus borrower recovery62400 minus guarantee cash259665.8768 plus recovery remittance18124.3297 equals retained loss590058.4529. D01-C03: claim67727.2727 atday 152, borrower recovery5200 and remittance4727.2727 atday 167. Borrower unresolved principal831600 remains distinct from the lender retained loss after guarantee compensation. In the support scenario, closing inventory164640 is carried at cost and requires valuation sensitivity. An approved pilot would add capital return, concentration limits and inventory valuation sensitivity.

Sources
[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 18

Proposed workflow rather than a deployed system. The generative layer prepares structured evidence and explanations using approved tools. Calculation services supply numerical results. Decision services enforce permissions and configured policy. A correlationID connects the case; eventIDs, timestamps, approverIDs, modelversions and execution receipts establish the sequence. Customer review and complaint routes remain traceable.

Sources
[1] N. Maloba, Underwrite for Collection: MSME Credit Lifecycle Whitepaper, 2026. doi: 10.5281/zenodo.23343888. https://doi.org/10.5281/zenodo.23343888

[8] Republic of Kenya, Data Protection Act, No. 24 of 2019, ss.25,26,29-31,35,41-43,48-49. https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2019-11-15/source

[9] Republic of Kenya, Data Protection (General) Regulations, 2021, reg.22 and applicable processing safeguards. https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf

## Slide 19

This is a proposed sequence rather than a promised timetable or signed engagement. Historical observations alone do not establish intervention effects. Design the prospective stage around eligibility, clustering, intervention fidelity, delayed outcomes and power. Choose approval thresholds and acceptance metrics with the partner before execution.

Sources
[6] F. Campos et al., Teaching personal initiative beats traditional training in boosting small business in West Africa, Science,357(6357),1287-1290, 2017. doi: 10.1126/science.aan5329. https://doi.org/10.1126/science.aan5329

[7] M. A. Hernan and J. M. Robins, Causal Inference: What If, Chapman & Hall/CRC, 2020. https://miguelhernan.org/whatifbook

[8] Republic of Kenya, Data Protection Act, No. 24 of 2019, ss.25,26,29-31,35,41-43,48-49. https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2019-11-15/source

[9] Republic of Kenya, Data Protection (General) Regulations, 2021, reg.22 and applicable processing safeguards. https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf

## Slide 20

Operational legal mapping should confirm applicability to the entity, product, processing purpose and decision. RelevantDPA duties include principles, rights, notice, lawfulprocessing, DPIA, automateddecisions, security and transfers. GeneralRegulations2021reg22 addresses automated individual decision-making. A human review process needs effective authority, enough information and recorded reasons.

Sources
[8] Republic of Kenya, Data Protection Act, No. 24 of 2019, ss.25,26,29-31,35,41-43,48-49. https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2019-11-15/source

[9] Republic of Kenya, Data Protection (General) Regulations, 2021, reg.22 and applicable processing safeguards. https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf

## Slide 21

The initial request is a scoping discussion, not a procurement or deployment commitment. The reproducible case and article can accompany the deck for technical review. Subsequent commercial scope, access controls and responsibilities would be agreed with the relevant4G team.

Sources
[1] N. Maloba, Underwrite for Collection: MSME Credit Lifecycle Whitepaper, 2026. doi: 10.5281/zenodo.23343888. https://doi.org/10.5281/zenodo.23343888

[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

## Slide 22

Full numbered references and hyperlinks appear in the speaker notes. Reproduction uses assumptions.json, model.py, run_case.py, exportedCSV ledgers and summary.json. Deck and original analysis: Creative Commons Attribution-NonCommercial-ShareAlike4.0International. https://creativecommons.org/licenses/by-nc-sa/4.0/

Sources
[1] N. Maloba, Underwrite for Collection: MSME Credit Lifecycle Whitepaper, 2026. doi: 10.5281/zenodo.23343888. https://doi.org/10.5281/zenodo.23343888

[2] 4G Capital, UPIA: 30-Day Working Capital Business Loans. Accessed 18 October 2026. https://www.4g-capital.com/upia

[3] 4G Capital, KUZA: Embedded Retail Credit for Distributors. Accessed 18 October 2026. https://www.4g-capital.com/kuza

[4] IFC, MFP-CFLG-4G CAP, Summary of Investment Information, project 53511, updated4July2026. Accessed18 October 2026. https://disclosures.ifc.org/project-detail/SII/53511/mfp-cflg-4g-cap

[5] N. Maloba, 4G-inspired merchant cycle and risk-sharing teaching case, 2026. Reproducible code: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case . Local source: research_lab/four_g_merchant_finance_case/assumptions.json and model.py. Output: output/four_g_merchant_finance_case_2026-10-16/summary.json and scenario ledgers.

[6] F. Campos et al., Teaching personal initiative beats traditional training in boosting small business in West Africa, Science,357(6357),1287-1290, 2017. doi: 10.1126/science.aan5329. https://doi.org/10.1126/science.aan5329

[7] M. A. Hernan and J. M. Robins, Causal Inference: What If, Chapman & Hall/CRC, 2020. https://miguelhernan.org/whatifbook

[8] Republic of Kenya, Data Protection Act, No. 24 of 2019, ss.25,26,29-31,35,41-43,48-49. https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2019-11-15/source

[9] Republic of Kenya, Data Protection (General) Regulations, 2021, reg.22 and applicable processing safeguards. https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf

[10] World Bank and FIRST Initiative, Principles for Public Credit Guarantee Schemes for SMEs, 2015. https://www.worldbank.org/en/topic/financialsector/publication/principles-for-public-credit-guarantee-schemes-cgss-for-smes

Licence: CC BY-NC-SA 4.0.
