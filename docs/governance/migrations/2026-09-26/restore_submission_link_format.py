"""Keep unchanged relative image links byte-identical to their source manuscript."""
from pathlib import Path
import hashlib
import json
import shutil

here = Path(__file__).resolve().parent
root = here.parents[3]
name = 'bayesian-telematics-relativities'
stage = root/'_archive/repository_migration_2026-09-26/staging'
rel = 'publications/submissions/brian-hey-2026/Bayesian_Credibility_Telematics_Brian_Hey_2026.md'
source = root/rel
digest = hashlib.sha256(source.read_bytes()).hexdigest()
for destination in [stage/name/rel, root.parent/name/rel]:
    shutil.copy2(source, destination)
for manifest in [here/'transfer_manifest.json', stage/name/'MIGRATION_MANIFEST.json', root.parent/name/'MIGRATION_MANIFEST.json']:
    data = json.loads(manifest.read_text(encoding='utf-8'))
    for row in data['files']:
        if row['repository']==name and row['relative_path']==rel:
            assert row['source_sha256']==digest
            row['destination_sha256']=digest
            row['adapted']=False
    manifest.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
hash_path = here/'staged_hashes.json'
hashes = json.loads(hash_path.read_text(encoding='utf-8'))
for p in [stage/name/rel, stage/name/'MIGRATION_MANIFEST.json']:
    hashes[str(p.relative_to(stage))]=hashlib.sha256(p.read_bytes()).hexdigest()
hash_path.write_text(json.dumps(hashes, indent=2)+'\n', encoding='utf-8')
print('Restored source-exact submission Markdown and updated transfer hashes.')
