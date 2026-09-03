# Public Data Workspace

This directory holds dated, source-preserving public-data snapshots for the KBA lifecycle-credit research programme.

Run the baseline collector from the repository root:

```powershell
python publications/submissions/kba-lifecycle-credit/scripts/collect_public_baseline.py --as-of 2026-09-02
```

The collector currently supports:

- CBK KESONIA observations.
- CBK KESONIA compounded-index observations.
- CBK commercial-bank weighted average rates.
- The visible tables and headline measures on the KBA MSME loan-performance dashboard.

The Total Cost of Credit portal is registered but not yet automatically extracted. Its rendered page uses a client-side application, and the historical update behaviour must be understood before product observations are treated as a time series.

Generated snapshots include the retrieval date, source URL, and a run manifest. A public value shown on a later retrieval date may have been revised. Comparisons should therefore use the dated snapshot rather than silently refreshing earlier analyses.

