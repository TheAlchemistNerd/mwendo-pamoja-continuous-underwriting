"""Prepare reviewed snapshots inside Mwendo; no writes to sibling repositories."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[4]
DOWNLOADS = ROOT.parent
HERE = Path(__file__).resolve().parent
ARCHIVE = ROOT / '_archive/repository_migration_2026-09-26'
STAGE = ARCHIVE / 'staging'
UNDERWRITE = DOWNLOADS / 'behavioural credit scoring - underwrite to collect rct'
NAMES = ('bayesian-telematics-relativities', 'regtech-kesonia-treasury')
SKIP = {'.git', 'node_modules', '__pycache__', '.venv', 'scratchpad', 'tmp'}

def long(p):
    return Path('\\\\?\\'+str(p.resolve()))

def sha(p):
    return hashlib.sha256(long(p).read_bytes()).hexdigest()

def files(base):
    for folder, dirs, names in os.walk(base):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for name in names:
            yield Path(folder) / name

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True, encoding='utf-8')

def save(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def main():
    assert ROOT.name == 'insuretech & embedded finance'
    # Preparation may be resumed before installation; it only regenerates this stage.
    for name in NAMES:
        assert not (DOWNLOADS/name).exists(), f'Destination already exists: {name}'
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    state = {p.name: {'head': git(p, 'rev-parse', 'HEAD').strip(),
             'status': git(p, 'status', '--porcelain=v1', '--untracked-files=all')}
             for p in (ROOT, UNDERWRITE)}
    if not (HERE/'pre_migration_state.json').exists():
        save(HERE/'pre_migration_state.json', json.dumps(state, indent=2)+'\n')
    for name, p in [('mwendo', ROOT), ('underwrite', UNDERWRITE)]:
        if not (ARCHIVE/f'{name}_pre_migration.bundle').exists():
            subprocess.run(['git', '-C', str(p), 'bundle', 'create', str(ARCHIVE/f'{name}_pre_migration.bundle'), '--all'], check=True)

    # Snapshot boundaries preserve existing relative build paths.
    groups = [
        (NAMES[0], 'whitepapers/telematics-relativities'),
        (NAMES[0], 'publications/submissions/brian-hey-2026'),
        (NAMES[1], 'docs/research/kesonia'),
        (NAMES[1], 'output/kesonia_treasury_deep_review_2026-09-25'),
    ]
    selections = []
    excluded = []
    for name, rel in groups:
        for p in files(ROOT/rel):
            if p.name.startswith('~') or p.suffix == '.tmp' or ('telematics-relativities' in p.parts and ('build' in p.relative_to(ROOT/rel).parts or p.name == 'paper.docx')):
                excluded.append({'path': str(p), 'reason': 'Office lock or generated intermediate; preserved in the local retirement archive'})
                continue
            selections.append((name, p, p.relative_to(ROOT)))
    published = ROOT/'publications/pdfs/Bayesian_Credibility_and_Exposure_Normalised_Telematics_Relativities_CC_BY_NC_SA_4_0_2026-09-08.pdf'
    selections.append((NAMES[0], published, published.relative_to(ROOT)))
    for filename in ['source_01_original.txt', 'source_02_original.txt', '02_WORKING_FORMULATIONS_AND_EXAMPLES.md', 'review.css']:
        p = ROOT/'output/pricing_treasury_cross_project_review_2026-09-23'/filename
        selections.append((NAMES[1], p, p.relative_to(ROOT)))
    mapping = {p.resolve(): DOWNLOADS/name/rel for name, p, rel in selections}
    rows = []
    for name, source, rel in selections:
        staged = STAGE/name/rel
        staged.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, staged)
        assert sha(source) == sha(staged)
        rows.append({'repository': name, 'source': str(source), 'relative_path': rel.as_posix(), 'source_sha256': sha(source)})

    # Keep source pastes, experiment records and historical hashes byte-identical.
    # Rebase Markdown links in owned working notes; external project references remain explicit.
    for name, source, rel in selections:
        if source.suffix != '.md':
            continue
        staged = STAGE/name/rel
        destination = DOWNLOADS/name/rel
        text = staged.read_text(encoding='utf-8-sig')
        def link(match):
            value = match.group(1).strip('<>')
            if re.match(r'^(https?|mailto):', value) or value.startswith('#'):
                return match.group(0)
            target, sep, fragment = unquote(value).partition('#')
            if target.startswith('file:///'):
                target = target[8:]
            p = Path(target)
            if not p.is_absolute():
                p = source.parent/p
            p = p.resolve()
            if not p.exists():
                return match.group(0)
            mapped = mapping.get(p, p)
            if mapped.is_relative_to(DOWNLOADS/name):
                out = Path(os.path.relpath(mapped, destination.parent)).as_posix()
            else:
                out = mapped.as_posix()
            out += '#'+fragment if sep else ''
            if out == value:
                return match.group(0)
            return '](<'+out+'>)'
        text = re.sub(r'\]\((<[^>]+>|[^)]+)\)', link, text)
        if text != staged.read_text(encoding='utf-8-sig'):
            save(staged, text)

    # The former builder also wrote into the parent project. Its replacement only
    # renders this repository's pack and never distributes material into guest repos.
    pack_rel = Path('output/kesonia_treasury_deep_review_2026-09-25')
    save(STAGE/NAMES[1]/pack_rel/'build_reading_pack.py', '''"""Render this repository's existing review notes locally; no cross-project writes."""
from pathlib import Path
import argparse
import html
import re
import shutil
import subprocess
from urllib.parse import unquote

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pandoc', default=shutil.which('pandoc'))
    args = parser.parse_args()
    if not args.pandoc:
        parser.error('Pandoc is required; pass --pandoc with its executable path')
    pack = Path(__file__).resolve().parent
    docs = sorted(pack.glob('[0-9][0-9]_*.md'))
    for md in docs:
        title = md.read_text(encoding='utf-8-sig').splitlines()[0].lstrip('# ')
        run = subprocess.run([args.pandoc, str(md), '--standalone', '--toc', '--mathml',
            '--from=markdown+tex_math_single_backslash', '--css=review.css',
            '--metadata', 'pagetitle='+title], check=True, capture_output=True, encoding='utf-8')
        def link(match):
            raw = html.unescape(match.group(1))
            target, sep, fragment = unquote(raw).partition('#')
            p = Path(target)
            if p.is_absolute():
                raw = p.as_uri()+('#'+fragment if sep else '')
            elif target.endswith('.md') and (md.parent/target).with_suffix('.html').exists():
                raw = target[:-3]+'.html'+('#'+fragment if sep else '')
            return 'href="'+html.escape(raw, quote=True)+'"'
        rendered = re.sub(r'href="([^"]+)"', link, run.stdout)
        md.with_suffix('.html').write_text(rendered, encoding='utf-8')
    print(f'Rendered {len(docs)} local review documents')

if __name__ == '__main__':
    main()
''')

    common_ignore = '__pycache__/\n*.py[cod]\n.venv/\nnode_modules/\nscratchpad/\n*.tmp\n~$*\n*.aux\n*.log\n*.toc\n*.out\n'
    save(STAGE/NAMES[0]/'.gitignore', common_ignore+'/whitepapers/telematics-relativities/build/\n/whitepapers/telematics-relativities/paper.docx\n')
    save(STAGE/NAMES[1]/'.gitignore', common_ignore)
    save(STAGE/NAMES[0]/'README.md', '''# Bayesian telematics relativities

Authoritative standalone working repository, extracted on 26 September 2026 from Mwendo Pamoja. This is a recorded working-tree snapshot, including unpublished changes; earlier history remains in the originating repository and its local migration bundle.

## Start here

- [Canonical paper](whitepapers/telematics-relativities/paper.md)
- [Mathematical derivations](whitepapers/telematics-relativities/Mathematical_Derivations.md)
- [Implementation plan](whitepapers/telematics-relativities/DETAILED_IMPLEMENTATION_PLAN.md)
- [Correction ledger](whitepapers/telematics-relativities/IMPLEMENTATION_CORRECTION_LEDGER.md)
- [Brian Hey submission package](publications/submissions/brian-hey-2026/README.md)
- [Migration provenance](MIGRATION.md)

## Checks and builds

Run `python validate.py paper.md` from `whitepapers/telematics-relativities`. Build with `scripts/build_paper.ps1` from that directory; it requires Pandoc, Mermaid CLI and the Python document-processing dependencies. Existing relative paths are retained deliberately.

Run `python validation/validate_submission.py` from `publications/submissions/brian-hey-2026` (requires pandas). At extraction this passes the structural/result checks and fails its final canonical-paper hash gate: the working paper differs from the pinned submission baseline. That pre-existing issue remains open; the expected hash has not been reset to make the check pass.

The published PDF is a dated release. Submission outputs and guidelines are curated package assets; build intermediates stay outside version control. The IFRS 17 discussion remains a research interface, not a separate implemented accounting product. Mwendo's controlled specifications and SPV model remain owned by the Mwendo repository.
''')
    save(STAGE/NAMES[1]/'README.md', '''# RegTech–KESONIA Treasury

Authoritative standalone working repository, extracted on 26 September 2026. Initial scope: the four-part RegTech–KESONIA series, benchmark compounding, curve and FTP teaching cases, and governed Treasury workflows. The remaining-work register is a development backlog, not a claim of completed banking models or integrations.

## Start here

- [Part 1: enterprise architecture](docs/research/kesonia/Part1_KESONIA_Reform_and_Enterprise_Architecture.md)
- [Part 2: compounding mathematics and SQL](docs/research/kesonia/Part2_Daily_Compounding_Engine_Mathematics_and_SQL.md)
- [Part 3: pricing and IFRS 9](docs/research/kesonia/Part3_AI_Pricing_Engine_and_IFRS9_Integration.md)
- [Part 4: platform and roadmap](docs/research/kesonia/Part4_RegTech_Sweep_Platform_Deep_Dives_and_Roadmap.md)
- [Review pack and worked cases](output/kesonia_treasury_deep_review_2026-09-25/00_READ_ME.md)
- [18-item remaining-work register](docs/research/kesonia/TREASURY_REMAINING_WORK_REGISTER_2026-09-25.md)
- [Migration provenance](MIGRATION.md)

## Evidence and local checks

`python output/kesonia_treasury_deep_review_2026-09-25/verify_examples.py` checks illustrative arithmetic and regenerates its result JSON. `python output/kesonia_treasury_deep_review_2026-09-25/build_reading_pack.py` renders the eight local review notes with Pandoc. The renderer writes only within this repository; it no longer distributes files to other projects or modifies historical reading manifests.

The two original pasted texts and the earlier formulations note are preserved in `output/pricing_treasury_cross_project_review_2026-09-23/`. Treat them as research evidence. Historical reading/delivery manifests retain their original paths and hashes. The current ownership and copy verification are in `MIGRATION_MANIFEST.json`.

The four manuscripts and notes in `docs/research/kesonia` are working source. The September 25 reading pack is a dated review edition; coordinate revisions explicitly if publishing a new edition. Broader credit, SPV and accounting specifications remain in Mwendo and are external research dependencies. Financial Material and the SokoIntel website project remain guest repositories; this repository does not write to them.
''')
    for name in NAMES:
        provenance = f'''# Migration provenance — 26 September 2026

Source: `{ROOT}`. Source Git HEAD: `{state[ROOT.name]['head']}`.

New authoritative location: `{DOWNLOADS/name}`.

This repository begins with a snapshot of the selected working files, including uncommitted research. It does not claim that all content existed at the originating commit. `MIGRATION_MANIFEST.json` records every source path, original SHA-256, destination path and post-adaptation SHA-256. Source history remains in Mwendo; a complete local Git bundle and retired originals are preserved under `{ARCHIVE}`.

Changes during extraction are limited to entry points, link portability and the Treasury renderer's write boundary. Financial assumptions, manuscript claims, original pastes, experiment outputs and historical validation hashes are not refreshed by this migration. No remote is configured by the migration.

Generated intermediates and Office locks are not imported as active source. Retired originals are preserved in the local archive. Dated published PDFs in Mwendo may remain distribution copies. Guest repositories are outside the write boundary.
'''
        save(STAGE/name/'MIGRATION.md', provenance)
        log = git(ROOT, 'log', '--format=fuller', '--name-status', '--', *[rel for n,rel in groups if n==name])
        save(STAGE/name/'SOURCE_HISTORY.txt', log)

    for row in rows:
        row['destination_sha256'] = sha(STAGE/row['repository']/row['relative_path'])
        row['adapted'] = row['source_sha256'] != row['destination_sha256']
    for name in NAMES:
        save(STAGE/name/'MIGRATION_MANIFEST.json', json.dumps({'date': '2026-09-26', 'source_head': state[ROOT.name]['head'], 'files': [r for r in rows if r['repository']==name]}, indent=2)+'\n')

    # Preserve and compare Underwrite without altering the standalone checkout yet.
    inner = ROOT/UNDERWRITE.name
    a = {p.relative_to(inner).as_posix(): sha(p) for p in files(inner)}
    b = {p.relative_to(UNDERWRITE).as_posix(): sha(p) for p in files(UNDERWRITE)}
    b = {k.replace('source_library/series/','series/',1) if k.startswith('source_library/series/') else k:v for k,v in b.items()}
    diff = sorted(k for k in a.keys()&b.keys() if a[k] != b[k])
    assert diff == ['series/governance/revision_snapshots/2026-09-15_pre_cash_provenance_extension/SHA256SUMS.txt'], diff
    additions = sorted(a.keys()-b.keys())
    assert len(additions)==3 and all(k.startswith('series/research/') for k in additions)
    save(HERE/'transfer_manifest.json', json.dumps({'files': rows, 'excluded_from_active_copy': excluded,
        'underwrite': {'inner': str(inner), 'standalone': str(UNDERWRITE), 'inner_hashes': a,
        'standalone_logical_hashes': b, 'inner_only': additions, 'different': diff,
        'resolution': 'Keep standalone historical snapshot and hash list; transfer only three missing research items.'}}, indent=2)+'\n')
    # Exact pre-mutation relocated series copy, including generated publication files.
    shutil.copytree(long(UNDERWRITE/'source_library/series'), long(ARCHIVE/'underwrite_standalone_series_before'), dirs_exist_ok=True)
    stage_hashes = {str(p.relative_to(STAGE)): sha(p) for p in files(STAGE)}
    save(HERE/'staged_hashes.json', json.dumps(stage_hashes, indent=2)+'\n')
    print(json.dumps({'prepared_files': len(rows), 'staged_files': len(stage_hashes), 'underwrite_additions': additions, 'stage': str(STAGE)}, indent=2))

if __name__ == '__main__':
    main()
