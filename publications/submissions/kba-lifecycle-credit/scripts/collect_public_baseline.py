#!/usr/bin/env python3
"""Collect the initial official public-data baseline for the KBA research package.

The script preserves dated extracts and source metadata. It intentionally does not
scrape the client-rendered Total Cost of Credit portal until its endpoint and
historical update behaviour have been validated.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import requests
from lxml import html


REPO_ROOT = Path(__file__).resolve().parents[4]
PACKAGE_ROOT = Path(__file__).resolve().parents[1]

CBK_TABLES = {
    "cbk_kesonia": {
        "page_url": "https://www.centralbank.go.ke/kesonia/",
        "table_id": 194,
        "columns": ["observation_date", "kesonia_rate_percent"],
    },
    "cbk_kesonia_compounded_index": {
        "page_url": "https://www.centralbank.go.ke/kesonia-compounded-index/",
        "table_id": 195,
        "columns": ["observation_date", "kesonia_index"],
    },
    "cbk_weighted_average_rates": {
        "page_url": "https://www.centralbank.go.ke/commercial-banks-weighted-average-rates/",
        "table_id": 17,
        "columns": [
            "year",
            "month",
            "deposit_rate_percent",
            "savings_rate_percent",
            "lending_rate_percent",
            "overdraft_rate_percent",
        ],
    },
}

MSME_URL = "https://msmedata.kba.co.ke/kba/loan-performance"
MSME_TABLE_NAMES = [
    "npl_by_gender",
    "npl_by_institution_type",
    "npl_by_sector",
    "npl_by_product_type",
    "npl_by_client_type",
    "npl_by_collateral_status",
    "npl_by_loan_status",
    "npl_monthly_trend",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--as-of",
        required=True,
        help="Snapshot date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=PACKAGE_ROOT / "data" / "raw" / "public",
        help="Base output directory.",
    )
    return parser.parse_args()


def validate_as_of(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").date().isoformat()


def get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (compatible; KBA-Lifecycle-Credit-Research/0.1; "
                "+mailto:nevillemaloba@gmail.com)"
            )
        }
    )
    return session


def write_csv(path: Path, columns: list[str], rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_text(value: str) -> str:
    return " ".join(value.replace("\ufffd", " ").split())


def fetch_cbk_table(
    session: requests.Session, table_id: int, expected_columns: list[str]
) -> list[dict]:
    endpoint = (
        "https://www.centralbank.go.ke/wp-admin/admin-ajax.php"
        f"?action=get_wdtable&table_id={table_id}"
    )
    response = session.post(
        endpoint,
        data={"draw": 1, "start": 0, "length": 10000},
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    records = payload.get("data", [])
    if int(payload.get("recordsFiltered", len(records))) != len(records):
        raise RuntimeError(f"Incomplete CBK table {table_id}: pagination mismatch")

    rows: list[dict] = []
    for record in records:
        if len(record) < len(expected_columns):
            raise RuntimeError(
                f"CBK table {table_id} returned {len(record)} fields; "
                f"expected {len(expected_columns)}"
            )
        row = dict(zip(expected_columns, (clean_text(str(v)) for v in record)))
        if "observation_date" in row:
            row["observation_date"] = datetime.strptime(
                row["observation_date"], "%d/%m/%Y"
            ).date().isoformat()
        rows.append(row)
    return rows


def extract_msme_tables(session: requests.Session) -> tuple[str, list[tuple[str, list[str], list[dict]]], dict]:
    response = session.get(MSME_URL, timeout=60)
    response.raise_for_status()
    document = html.fromstring(response.content)
    body_text = clean_text(document.text_content())

    as_of_match = re.search(r"As of\s+([A-Z][a-z]{2}\s+\d{4})", body_text)
    as_of_label = as_of_match.group(1) if as_of_match else "Unknown"

    ratio_match = re.search(
        r"total npl ratio across all reporting financial institutions as of .*? is ([0-9.]+)%",
        body_text,
        re.IGNORECASE,
    )
    amount_match = re.search(r"NPL Outstanding\s*KES\s*([0-9.]+)([BMK])", body_text)
    amount_value = None
    if amount_match:
        multiplier = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}[
            amount_match.group(2)
        ]
        amount_value = float(amount_match.group(1)) * multiplier

    summary = {
        "as_of_label": as_of_label,
        "total_npl_ratio_percent": float(ratio_match.group(1)) if ratio_match else None,
        "npl_outstanding_kes": amount_value,
        "source_url": MSME_URL,
    }

    tables = document.xpath("//table")
    if len(tables) < len(MSME_TABLE_NAMES):
        raise RuntimeError(
            f"Expected at least {len(MSME_TABLE_NAMES)} KBA tables, found {len(tables)}"
        )

    outputs: list[tuple[str, list[str], list[dict]]] = []
    for table_name, table in zip(MSME_TABLE_NAMES, tables):
        columns = [clean_text(node.text_content()) for node in table.xpath(".//th")]
        if not columns:
            raise RuntimeError(f"KBA table {table_name} has no headers")
        rows = []
        for tr in table.xpath(".//tr"):
            values = [clean_text(node.text_content()) for node in tr.xpath("./td")]
            if not values:
                continue
            values = values[: len(columns)]
            if len(values) != len(columns):
                raise RuntimeError(
                    f"KBA table {table_name} row has {len(values)} fields; "
                    f"expected {len(columns)}"
                )
            row = dict(zip(columns, values))
            row["as_of_label"] = as_of_label
            row["source_url"] = MSME_URL
            rows.append(row)
        outputs.append(
            (table_name, columns + ["as_of_label", "source_url"], rows)
        )

    return as_of_label, outputs, summary


def main() -> None:
    args = parse_args()
    as_of = validate_as_of(args.as_of)
    output_dir = args.output_root.resolve() / as_of
    output_dir.mkdir(parents=True, exist_ok=True)
    session = get_session()
    manifest = {
        "as_of": as_of,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "collector": str(Path(__file__).resolve().relative_to(REPO_ROOT)),
        "files": [],
    }

    for name, specification in CBK_TABLES.items():
        rows = fetch_cbk_table(
            session,
            specification["table_id"],
            specification["columns"],
        )
        enriched = []
        for row in rows:
            enriched.append(
                {
                    **row,
                    "source_url": specification["page_url"],
                    "retrieved_as_of": as_of,
                }
            )
        columns = specification["columns"] + ["source_url", "retrieved_as_of"]
        path = output_dir / f"{name}.csv"
        write_csv(path, columns, enriched)
        manifest["files"].append(
            {"path": path.name, "rows": len(enriched), "sha256": sha256(path)}
        )

    _, tables, summary = extract_msme_tables(session)
    for table_name, columns, rows in tables:
        path = output_dir / f"kba_msme_{table_name}.csv"
        write_csv(path, columns, rows)
        manifest["files"].append(
            {"path": path.name, "rows": len(rows), "sha256": sha256(path)}
        )

    summary_path = output_dir / "kba_msme_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    manifest["files"].append(
        {"path": summary_path.name, "rows": 1, "sha256": sha256(summary_path)}
    )

    manifest_path = output_dir / "run_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

