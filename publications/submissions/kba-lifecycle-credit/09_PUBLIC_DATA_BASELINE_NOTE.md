# Public Data Baseline Note

**Snapshot date:** 2 September 2026  
**KBA MSME dashboard reporting month:** June 2026

## 1. Extracted records

The first reproducible public-data snapshot contains:

| Dataset | Records | Coverage visible in snapshot |
|---|---:|---|
| CBK KESONIA | 249 | 1 September 2025 to 1 September 2026 |
| CBK KESONIA compounded index | 250 | 1 September 2025 to 2 September 2026 |
| CBK commercial-bank weighted average rates | 423 | July 1991 to July 2026 |
| KBA MSME NPL by gender | 4 | June 2026 snapshot |
| KBA MSME NPL by institution type | 8 | June 2026 snapshot |
| KBA MSME NPL by sector | 10 | June 2026 snapshot |
| KBA MSME NPL by product type | 13 | June 2026 snapshot |
| KBA MSME NPL by client type | 2 | June 2026 snapshot |
| KBA MSME NPL by collateral status | 2 | June 2026 snapshot |
| KBA MSME NPL by loan status | 8 | June 2026 snapshot |
| KBA MSME monthly NPL trend | 12 | July 2025 to June 2026 |

The run manifest records row counts and SHA-256 hashes for each output.

## 2. Initial descriptive observations

The daily KESONIA series begins at 9.5922 percent on 1 September 2025 and records 8.7500 percent on 1 September 2026. Monthly average KESONIA declined from approximately 9.4791 percent in September 2025 to approximately 8.7505 percent in August 2026.

The CBK commercial-bank weighted average lending rate was 15.17 percent in August 2025, 15.07 percent in September 2025, 14.78 percent in February 2026, 14.38 percent in June 2026, and 14.39 percent in July 2026. The overdraft rate moved from 13.89 percent in August 2025 to 12.97 percent in July 2026.

These movements are descriptive. They do not yet estimate KESONIA pass-through. The weighted average lending rate covers a broader population than KESONIA-linked variable products and may reflect fixed-rate products, portfolio composition, maturities, new and existing facilities, bank-specific premium changes, and concurrent monetary and macroeconomic conditions.

The KBA MSME loan-performance page reports a 24.5 percent value-based NPL ratio and KES 234.67 billion of NPL outstanding for its selected June 2026 view. Product tables separately report value-based ratios, loan counts, NPL loan counts, and count-based shares. The distinction will be preserved in every analysis.

## 3. Data-quality questions identified

The dashboard's visible monthly NPL series changes from 21.7 percent in September 2025 to 11.0 percent in October 2025 and then to 23.3 percent in November 2025. That discontinuity requires investigation before a time-series model is estimated. Possible explanations include a change in reporting coverage, filter population, classification, source refresh, data revision, or a dashboard extraction issue. No explanation will be selected without evidence from the methodology, KBA, or the underlying source.

The KBA dashboard headline is tied to its selected filters and methodology. MSME-focused and full-portfolio NPL indicators can differ. Each subsequent dataset must retain the filter state, population scope, value or count basis, and reporting date.

The KESONIA compounded index contains an observation for 2 September 2026 while the daily rate series ends on 1 September 2026. This is consistent with an index carried to the next observation date using the preceding business day's rate, but the calculation will be checked against the official methodology before the index is reconstructed independently.

## 4. Next public-data tasks

1. Acquire and version the official KESONIA methodology and FAQ documents.
2. Build an event table for CBR decisions and revised-RBCPM implementation dates.
3. Index the June 2026 and preceding CBK Credit Officer Survey reports.
4. Capture KBA MSME dashboard methodology and filter-state metadata.
5. Resolve the October 2025 NPL discontinuity.
6. Discover and validate the KBA Total Cost of Credit data interface.
7. Determine whether product updates can be reconstructed historically or only snapshotted prospectively.
8. Add official inflation, exchange-rate, Treasury-rate, fuel-price, and activity controls.
9. Define a monthly merge calendar that distinguishes observation, publication, and effective dates.
10. Produce descriptive charts only after the source and denominator controls pass review.

## 5. Interpretation boundary

This baseline supports data discovery and descriptive research. It does not yet support a causal claim about the effect of KESONIA on lending rates, MSME credit, or NPLs. It also does not support borrower-level conclusions about default, cure, or recovery. Those conclusions require an appropriate identification strategy and, for lifecycle outcomes, an anonymised institutional dataset.

