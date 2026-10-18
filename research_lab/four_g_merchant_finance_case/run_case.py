"""Run from repository root; all generated output stays in the chosen case folder."""
import argparse
import csv
import hashlib
import json
from decimal import Decimal
from pathlib import Path
from model import run_all

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent

def serial(x):
    if isinstance(x,Decimal):return format(x,'.12f')
    raise TypeError(type(x).__name__)

def write_csv(path,rows):
    if not rows:return
    with path.open('w',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows({k:serial(v) if isinstance(v,Decimal) else v for k,v in row.items()} for row in rows)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',type=Path,default=HERE/'assumptions.json')
    parser.add_argument('--output',type=Path,default=ROOT/'output/four_g_merchant_finance_case_2026-10-16')
    args=parser.parse_args();p=json.loads(args.inputs.read_text(encoding='utf-8-sig'))
    cases=run_all(p);args.output.mkdir(parents=True,exist_ok=True)
    summary=[];manifest={'assumptions_sha256':hashlib.sha256(args.inputs.read_bytes()).hexdigest(),'source_sha256':{},'scenarios':list(cases),'currency':'KES','rounding':'12 decimal places in exports; Decimal precision 40 internally'}
    for file in ['model.py','run_case.py']:
        manifest['source_sha256'][file]=hashlib.sha256((HERE/file).read_bytes()).hexdigest()
    for name,case in cases.items():
        dest=args.output/name;dest.mkdir(exist_ok=True)
        write_csv(dest/'merchant_daily.csv',case['merchant_daily'])
        write_csv(dest/'loan_ledger.csv',case['loans'])
        write_csv(dest/'guarantee_claims.csv',case['claims'])
        write_csv(dest/'guarantee_events.csv',case['guarantee_events'])
        for mode,ledger in case['lender_daily'].items():write_csv(dest/('lender_daily_'+mode+'.csv'),ledger)
        summary.extend(case['summaries'])
    (args.output/'inputs.json').write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
    (args.output/'summary.json').write_text(json.dumps(summary,default=serial,indent=2)+'\n',encoding='utf-8')
    write_csv(args.output/'scenario_summary.csv',summary)
    manifest['merchant_rows_per_scenario']=len(next(iter(cases.values()))['merchant_daily'])
    manifest['summary_rows']=len(summary)
    (args.output/'verification.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    for s in summary:
        print(s['scenario'], 'protected' if s['protection'] else 'unprotected', 'loans',s['loans_originated'],'defaults',s['defaults'],'profit',round(s['lender_profit'],2),'merchant cash',round(s['merchant_closing_cash'],2),'claims',round(s['guarantee_cash_received'],2))
    print('Saved',args.output)
if __name__=='__main__':main()
