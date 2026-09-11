"""Export the hash-verified first-step spatial head (288 modes) as decimal
midpoints for the Fourier-side experiment. Radii are recorded separately so
the diagnostic knows the enclosure widths it is discarding."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'recursion'))
import stream_io
from flint import ctx
ctx.prec = 6144
rel = 'history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz'
meta, mats, record, path = stream_io.load_legacy(rel, want={'head'})
H = mats['head']
n = H.nrows()
out = {'scope': 'Midpoints of the hash-verified first-step spatial head; diagnostic export for the Fourier-side check.',
       'archive': rel, 'matrix_archive_sha256': record['matrix_archive_sha256'],
       'matrices_content_sha256': record['matrices_content_sha256'],
       'old_modes': meta['old_modes'], 'new_modes': meta['new_modes'],
       'max_radius': max(x.rad() for x in H.entries()).str(5),
       'head_mid': [[H[i, j].mid().str(70, radius=False) for j in range(n)] for i in range(n)]}
Path(sys.argv[1]).write_text(json.dumps(out))
print('exported', n, 'max radius', out['max_radius'])
