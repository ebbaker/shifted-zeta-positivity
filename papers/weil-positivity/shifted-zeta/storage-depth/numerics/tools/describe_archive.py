"""Write a one-entry hash catalog for a first-step archive built locally.

A rebuilt gzip has its own file hash, so the committed catalog
(records/closure_256_96_catalog.json) will not match a local rebuild; run this
on your own archive and compare the matrices_content_sha256 with the committed
one to recognize identical serialized matrices.
"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'archive/drafts/v0.1_2026-09-10/numerics'))
import archive_io
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--archive', required=True, help='path to closure_256_96.matrices.json.gz')
p.add_argument('--output', required=True, help='catalog to write, e.g. <seed folder>/ARCHIVE_RECORDS.json')
a = p.parse_args()
rec = archive_io.describe(a.archive, Path(a.archive).name)
Path(a.output).write_text(json.dumps({'schema_version': 1, 'archives': [rec],
    'scope': 'Catalog for a locally rebuilt first-step archive; identity record, not a proof.'}, indent=2) + '\n')
print(json.dumps(rec, indent=1))
