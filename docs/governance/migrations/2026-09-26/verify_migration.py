"""Verify installed siblings; record checks without changing scientific baselines."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DOWNLOADS = ROOT.parent
BAYES = DOWNLOADS/'bayesian-telematics-relativities'
KES = DOWNLOADS/'regtech-kesonia-treasury'
UNDERWRITE = DOWNLOADS/'behavioural credit scoring - underwrite to collect rct'

def sha(p):
    return hashlib.sha256(Path('\\\\?\\'+str(p.resolve())).read_bytes()).hexdigest()

def run(name, cwd, args, expected=0):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding='utf-8')
    return {'name': name, 'exit_code': p.returncode, 'expected_exit_code': expected,
            'matched_expected': p.returncode == expected, 'stdout': p.stdout, 'stderr': p.stderr}

def main():
    transfer = json.loads((HERE/'transfer_manifest.json').read_text(encoding='utf-8'))
    originals = [{'path': r['source'], 'unchanged': sha(Path(r['source'])) == r['source_sha256']} for r in transfer['files']]
    installed = [{'path': str(DOWNLOADS/r['repository']/r['relative_path']),
                  'matches_prepared_snapshot': sha(DOWNLOADS/r['repository']/r['relative_path']) == r['destination_sha256']}
                  for r in transfer['files']]
    assert all(x['unchanged'] for x in originals)
    regenerated = {str(KES/'output/kesonia_treasury_deep_review_2026-09-25'/f'{n}.html') for n in [
        '00_READ_ME','01_DETAILED_MATERIAL_REVIEW','02_CALCULATION_AND_CASEBOOK',
        '03_REVISION_BLUEPRINT_AND_INSERTS','04_READING_MAP_AND_REFERENCES',
        '05_STP_AND_ALM_FTP_SOFTWARE_REVIEW','06_WHAT_REMAINS_TO_BE_DEVELOPED','07_FRTB_SCOPE_AND_DEVELOPMENT_NOTE']}
    assert all(x['matches_prepared_snapshot'] or x['path'] in regenerated for x in installed)
    restored = []
    for relative, expected in transfer['underwrite']['standalone_logical_hashes'].items():
        if relative in {'README.md', 'series/build/build_whitepaper_pdf.ps1'}:
            continue
        restored.append({'path': relative, 'unchanged': sha(UNDERWRITE/relative) == expected})
    assert all(r['unchanged'] for r in restored)
    for relative in transfer['underwrite']['inner_only']:
        assert sha(UNDERWRITE/relative) == transfer['underwrite']['inner_hashes'][relative]
    checks = [
        run('Bayesian canonical structure', BAYES/'whitepapers/telematics-relativities', [sys.executable, '-X', 'utf8', 'validate.py', 'paper.md']),
        run('Submission baseline (known pre-migration hash mismatch)', BAYES/'publications/submissions/brian-hey-2026', [sys.executable, '-X', 'utf8', 'validation/validate_submission.py'], expected=1),
        run('KESONIA illustrative arithmetic', KES, [sys.executable, '-X', 'utf8', 'output/kesonia_treasury_deep_review_2026-09-25/verify_examples.py']),
        run('KESONIA local rendering', KES, [sys.executable, '-X', 'utf8', 'output/kesonia_treasury_deep_review_2026-09-25/build_reading_pack.py']),
    ]
    (HERE/'check_outputs.json').write_text(json.dumps(checks, indent=2)+'\n', encoding='utf-8')
    known_hash = 'EF155755DA4B1907C34C8A127D4C394CD84A551BDBDB7A014B3C2191947A16A4'
    assert 'canonical paper hash changed: '+known_hash in checks[1]['stderr'], 'Submission failure changed from pre-migration baseline'
    assert all(c['matched_expected'] for c in checks)
    parsed = []
    for repo in (BAYES, KES):
        for p in repo.rglob('*.py'):
            if '__pycache__' not in p.parts:
                ast.parse(p.read_text(encoding='utf-8-sig'), filename=str(p))
                parsed.append(str(p))
    report = {'date': '2026-09-26', 'source_hash_checks': originals,
              'installed_snapshot_checks': installed, 'regenerated_html_paths': sorted(regenerated), 'underwrite_restoration_checks': restored,
              'underwrite_additions': transfer['underwrite']['inner_only'], 'checks': checks,
              'python_files_parsed': parsed, 'migration_checks_passed': True,
              'known_open_validation_issue': 'Submission canonical-paper hash differs from its pinned baseline, identically before and after extraction.',
              'scope': 'File preservation, structural checks, illustrative arithmetic and local HTML rendering; no empirical validation or full PDF rebuild.'}
    (HERE/'validation_report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    for repo in (BAYES, KES):
        (repo/'MIGRATION_VALIDATION.json').write_text(json.dumps({'date': report['date'], 'checks': [c for c in checks if (repo==BAYES and c['name'].startswith(('Bayesian','Submission'))) or (repo==KES and c['name'].startswith('KESONIA'))], 'scope': report['scope']}, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'source_files_verified': len(originals), 'copied_files_verified': len(installed),
                      'underwrite_files_restored_unchanged': len(restored),
                      'checks': [{k:c[k] for k in ('name','exit_code','matched_expected')} for c in checks],
                      'python_files_parsed': len(parsed)}, indent=2))

if __name__ == '__main__':
    main()
