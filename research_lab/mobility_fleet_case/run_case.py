"""Regenerate portable cash ledgers and scenario summaries."""
import argparse
import csv
import hashlib
import html
import json
from decimal import Decimal
from pathlib import Path
from model import run_case

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def serial(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(type(obj).__name__)


def fmt(value):
    if isinstance(value, Decimal):
        return f"{value:,.2f}"
    return str(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=HERE / "assumptions.json")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "mobility_fleet_case_2026-10-13")
    args = parser.parse_args()
    p = json.loads(args.inputs.read_text(encoding="utf-8"))
    results = [run_case(p, s) for s in p["scenarios"]]
    args.output.mkdir(parents=True, exist_ok=True)
    for result in results:
        label = result["summary"]["scenario"]
        for name in ["weekly_ledger", "transfers"]:
            rows = result[name]
            with (args.output / f"{label}_{name}.csv").open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
    (args.output / "results.json").write_text(json.dumps(results, default=serial, indent=2) + "\n", encoding="utf-8")
    (args.output / "inputs.json").write_text(json.dumps(p, indent=2) + "\n", encoding="utf-8")
    summaries = [r["summary"] for r in results]
    keys = ["unavailable_days", "peak_arrears", "cure_week", "collected_fees", "driver_cash_surplus", "household_shortfall", "driver_terminal_vehicle_value", "additional_equity", "equity_net_cash", "equity_npv", "funder_npv_at_contract_rate"]
    lines = ["# Mobility fleet: 156-week operating and financing case", "", p["status"] + ". Currency: " + p["currency"] + ".", "", "All figures are author-selected scenario calculations. Three perspectives are linked by the same dated transfer ledger: driver, operator/equity and funder.", "", "| Measure | " + " | ".join(s["scenario"] for s in summaries) + " |", "|---|" + "---:|" * len(summaries)]
    for key in keys:
        lines.append("| " + key.replace("_", " ") + " | " + " | ".join(fmt(s[key]) for s in summaries) + " |")
    lines.extend(["", "Repair time is an input assumption. Contract bills, actual collections and arrears have separate columns. Covered repair costs are paid by the operator. The driver receives the terminal vehicle once the specified completion conditions are met; its value is recorded as a non-cash asset, and the operator receives zero residual sale cash in those runs.", "", "NPVs use dated cash flows. Operator equity NPV discounts at the supplied 18% annual effective rate; funder NPV uses its supplied 12% funding rate. Driver cash NPV uses 10%, with essential household consumption reported separately. Driver wealth NPV adds the conditional terminal vehicle value.", "", "The CSV files retain every weekly state and every transfer. Input and implementation hashes are recorded in verification.json."])
    md = "\n".join(lines) + "\n"
    (args.output / "00_MOBILITY_FLEET_CASE.md").write_text(md, encoding="utf-8")
    headings = "".join("<th>" + html.escape(s["scenario"]) + "</th>" for s in summaries)
    table = "<table><thead><tr><th>Measure</th>" + headings + "</tr></thead><tbody>"
    table += "".join("<tr><td>" + key.replace("_", " ") + "</td>" + "".join("<td>" + fmt(s[key]) + "</td>" for s in summaries) + "</tr>" for key in keys) + "</tbody></table>"
    links = "".join(f'<li><a href="{r["summary"]["scenario"]}_weekly_ledger.csv">{r["summary"]["scenario"]}: weekly ledger</a> · <a href="{r["summary"]["scenario"]}_transfers.csv">transfers</a></li>' for r in results)
    page = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Mobility fleet worked case</title><style>body{font:17px/1.6 system-ui;max-width:1200px;margin:50px auto;padding:0 24px;color:#173047}h1{font-size:2.3rem}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:10px;border-bottom:1px solid #cbd5df;text-align:right}td:first-child,th:first-child{text-align:left}th{background:#e6eff4}p{max-width:950px}a{color:#006e83}</style><h1>Mobility fleet: 156-week operating and financing case</h1><p>' + html.escape(p["status"]) + '. All cash figures are KES.</p>' + table + '<h2>Reading the case</h2>' + ''.join('<p>' + html.escape(x) + '</p>' for x in lines[-5:] if x) + '<h2>Reproducible ledgers</h2><ul>' + links + '</ul><p><a href="results.json">Exact results</a> · <a href="inputs.json">Assumptions</a> · <a href="verification.json">Cash and source checks</a></p></html>'
    (args.output / "00_MOBILITY_FLEET_CASE.html").write_text(page, encoding="utf-8")
    verification = {"cash_checks_pass": all(s["maximum_reconciliation_error"] < Decimal("1e-8") for s in summaries), "scenarios": len(summaries), "weekly_rows": sum(len(r["weekly_ledger"]) for r in results), "input_sha256": hashlib.sha256(args.inputs.read_bytes()).hexdigest(), "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE / "model.py", HERE / "run_case.py"]}, "summaries": summaries}
    (args.output / "verification.json").write_text(json.dumps(verification, default=serial, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summaries, default=serial, indent=2))


if __name__ == "__main__":
    main()
