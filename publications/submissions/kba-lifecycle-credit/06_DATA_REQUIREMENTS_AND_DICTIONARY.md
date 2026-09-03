# Data Requirements and Dictionary

## 1. Research datasets

The project will maintain four separated analytical datasets:

1. `public_benchmark_daily`: KESONIA, compounded index, CBR, and related market observations.
2. `public_product_pricing`: bank-product pricing and total-cost disclosures.
3. `public_credit_conditions`: aggregate MSME credit, asset-quality, survey, and macroeconomic observations.
4. `institution_credit_lifecycle`: anonymised account-period, transition, intervention, and recovery observations.

The public datasets can be built independently. The institution dataset requires a governed data partnership.

## 2. Common metadata

| Field | Definition | Type | Required |
|---|---|---:|---:|
| `source_id` | Stable identifier for the originating publication or system | Text | Yes |
| `source_url` | Canonical public URL, where applicable | Text | Public data |
| `retrieved_at` | Timestamp at which the source was acquired | Datetime | Yes |
| `published_at` | Publication or release date | Date | Where available |
| `observation_date` | Economic or account date represented | Date | Yes |
| `effective_date` | Date on which a rate, rule, or contract value became effective | Date | Where relevant |
| `revision_id` | Source revision or snapshot identifier | Text | Where available |
| `unit` | Currency, percentage, basis points, count, days, or index | Text | Yes |
| `definition_version` | Version of the business definition applied | Text | Yes |
| `quality_flag` | Valid, missing, stale, revised, inconsistent, or excluded | Category | Yes |

## 3. Public benchmark data

| Field | Definition | Frequency |
|---|---|---|
| `kesonia_rate` | Official annualised KESONIA observation | Business day |
| `kesonia_index` | Official compounded KESONIA index | Business day |
| `cbr_rate` | Central Bank Rate effective on observation date | Event/daily carry-forward |
| `tbill_91_rate` | Official 91-day Treasury bill rate used as a macro or comparison series | Auction/weekly |
| `interbank_volume` | Underlying eligible transaction volume if officially published | Daily |
| `business_day_flag` | Kenyan business-day classification | Daily |
| `publication_time` | Actual or expected publication timestamp | Daily |

KESONIA and its index will be consumed as official values. Any independently reconstructed factor is a control calculation and must reconcile within an approved tolerance.

## 4. Public bank-product pricing

| Field | Definition |
|---|---|
| `institution_id` | Stable public institution identifier |
| `product_id` | Stable institution-product identifier |
| `product_name` | Published product label |
| `customer_segment` | Published target segment |
| `secured_flag` | Published security status where available |
| `currency` | Product currency |
| `benchmark_basis` | KESONIA, CBR, fixed, or other disclosed basis |
| `published_reference_rate` | Reference rate displayed for the product observation |
| `published_k_rbcp` | Published bank or product premium |
| `published_lending_rate` | Displayed nominal lending rate |
| `fee_amount` | Disclosed fee amount for the standard example |
| `fee_rate` | Disclosed fee percentage where applicable |
| `insurance_or_third_party_cost` | Separately disclosed non-interest cost where applicable |
| `total_cost_amount` | Total cost for the standard example |
| `apr_or_effective_rate` | Published annual percentage or effective rate where available |
| `illustrative_amount` | Principal assumed by the public calculator |
| `illustrative_tenor` | Tenor assumed by the public calculator |
| `last_updated` | Published product update date |
| `missingness_reason` | N/A, not disclosed, not applicable, parsing failure, or unknown |

Product observations will not be compared until amount, tenor, currency, security, and fee bases are standardised or controlled.

## 5. Public credit conditions

| Field | Definition | Typical source |
|---|---|---|
| `credit_outstanding_value` | Outstanding credit balance for the stated population | KBA/CBK |
| `new_credit_value` | New disbursement flow during the stated period | KBA/CBK |
| `npl_value` | Point-in-time NPL balance under the source definition | KBA/CBK |
| `npl_ratio_value` | NPL value divided by applicable outstanding credit value | KBA/CBK |
| `npl_account_count` | Number of NPL accounts | KBA dashboard |
| `account_npl_share` | NPL account count divided by applicable account count | KBA dashboard |
| `product_type` | Published credit product grouping | KBA dashboard |
| `business_size` | Micro, small, medium, large, or unknown under source methodology | KBA dashboard |
| `ownership_gender` | Female-owned, male-owned, jointly owned, or unknown | KBA dashboard |
| `sector` | Published economic sector | KBA/CBK |
| `credit_standard_direction` | Tightened, unchanged, or eased | CBK survey |
| `credit_demand_direction` | Increased, unchanged, or decreased | CBK survey |
| `recovery_intention` | Surveyed expectation or planned recovery activity | CBK survey |
| `inflation_rate` | Official CPI inflation measure | KNBS/CBK |
| `exchange_rate` | Official or selected market exchange rate | CBK |
| `fuel_price` | Official regulated fuel price observation | EPRA |
| `activity_index` | GDP, sector output, PMI, or other documented activity measure | KNBS/authoritative source |

Value-based and account-count NPL measures will never share the same label. MSME-filtered and full-portfolio dashboard views will be stored separately.

## 6. Institution lifecycle data

### 6.1 Static and origination fields

| Field | Definition |
|---|---|
| `account_key` | Research pseudonym unique to a facility |
| `customer_key` | Research pseudonym linking permitted facilities without identifying the customer |
| `institution_key` | Anonymous institution or business-unit code where required |
| `product_code` | Governed product definition |
| `application_date` | Completed application timestamp |
| `decision_date` | Credit decision timestamp |
| `disbursement_date` | Funds-disbursed timestamp |
| `approved_amount` | Approved principal or limit |
| `disbursed_amount` | Actual initial disbursement |
| `contractual_tenor_days` | Contractual maturity in days |
| `benchmark_basis` | Contractual reference-rate basis |
| `contractual_margin` | Contractual margin distinct from public product premium |
| `fees_charges` | Contractual fees and charges with payer and basis |
| `origination_score` | Score available at decision time, with model version |
| `decision` | Approve, decline, defer, or refer |
| `override_code` | Documented override reason |

### 6.2 Account-period fields

| Field | Definition |
|---|---|
| `period_start` / `period_end` | Observation interval |
| `opening_balance` | Balance at interval start |
| `scheduled_principal` | Principal contractually due in interval |
| `scheduled_interest` | Interest contractually due in interval |
| `amount_paid` | Eligible cash received in interval |
| `payment_timestamp` | Timestamp for each payment in event table |
| `closing_balance` | Reconciled interval-end balance |
| `days_past_due` | DPD under approved end-of-period convention |
| `utilisation` | Drawn amount divided by approved limit where meaningful |
| `credit_state` | Current, early arrears, late arrears, default, write-off, or closed |
| `repayment_velocity` | Governed ratio of recent realised repayment to scheduled or historical repayment |
| `scheduled_actual_ratio` | Amount paid divided by amount due over specified window |
| `time_since_full_payment` | Days since last qualifying full payment |
| `modification_flag` | Whether contract was modified by the cutoff |
| `forbearance_flag` | Approved forbearance classification where applicable |

Each engineered field requires a lookback window, denominator, zero-denominator rule, winsorisation policy, and availability timestamp.

### 6.3 Outcome and recovery fields

| Field | Definition |
|---|---|
| `first_payment_default` | Default or defined material delinquency on the first scheduled payment |
| `npl_entry_date` | First date meeting the adopted NPL definition |
| `cure_date` | First date meeting the approved cure rule |
| `durable_cure_flag` | Cure sustained for the selected follow-up window |
| `redefault_date` | First material delinquency after cure |
| `writeoff_date` | Accounting write-off date |
| `gross_recovery_amount` | Cash recovered after default before direct costs |
| `recovery_timestamp` | Receipt timestamp for recovery cash |
| `collection_cost` | Directly attributable collection expense |
| `legal_cost` | Directly attributable legal expense |
| `net_recovery_amount` | Gross recovery less approved direct costs |
| `closure_date` | Final account closure date under the source system |

### 6.4 Intervention fields

| Field | Definition |
|---|---|
| `eligibility_timestamp` | Time at which the account entered the action-eligible population |
| `eligibility_rule_version` | Approved rule governing eligibility |
| `assigned_action` | Action assigned, including no-action control |
| `assignment_method` | Randomised, phased, policy threshold, manual, or observational |
| `action_timestamp` | Time action was initiated |
| `action_channel` | SMS, call, app, branch, restructure review, or other governed channel |
| `action_cost` | Direct economic cost of the intervention |
| `action_completion` | Whether the action was delivered or completed |
| `customer_response` | Governed response category |
| `complaint_or_hardship_flag` | Approved customer-outcome indicator |

## 7. Maturity and censoring

Every outcome will have a maturity rule. Accounts without sufficient follow-up will be censored or excluded according to a documented rule rather than labelled non-events. Recovery estimates will recognise right censoring and delayed cash. Vintage validation will ensure that training outcomes were mature before the scoring period used for testing.

## 8. Reconciliation controls

- Opening balance plus disbursements and charges less payments, credits, write-offs, and adjustments must reconcile to closing balance.
- Aggregate account balances must reconcile to the supplied portfolio control total within an approved tolerance.
- State transitions must be temporally valid.
- Payment timestamps may not precede disbursement.
- Intervention timestamps may not precede eligibility or use future outcomes.
- Gross recovery, cost, and net recovery must reconcile.
- Published benchmark and product-rate observations must preserve actual update dates.
- Data exclusions must be quantified by count and value.

