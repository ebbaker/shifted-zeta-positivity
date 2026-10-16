"""Write the exact rational Galerkin continuation for a second-step build record.

Same construction as certify_step.py (J = -F^{-1} B on the head, rounded to
decimal rationals), but reading the head through the streaming loader and
without the 1 MiB size assertion: for 96-mode slabs the record is about 3 MB
and is kept beside the external archive, with its hash recorded by the replay.
Lives outside numerics/recursion/ so that the builder-source hashes recorded in
the archives are unaffected.
"""
import argparse, json, sys
from pathlib import Path
import mpmath as mp
from flint import arb_mat as AM, ctx
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'recursion'))
from common import *
import stream_io

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--record', required=True); p.add_argument('--output', required=True)
p.add_argument('--bits', type=int, default=2048); p.add_argument('--digits', type=int, default=80)
a = p.parse_args()
ctx.prec = a.bits; mp.mp.dps = a.digits + 40
meta, mats, record, path = stream_io.load_record(a.record, want={'head'})
H = mats['head']; modes = meta['modes']; nn = modes[-1]; no = H.nrows() - nn
F = sub(H, range(no, no + nn), range(no, no + nn)); B = sub(H, range(no, no + nn), range(no))
J, strings = residual.rational_matrix(-F.solve(B), a.digits)
Path(a.output).write_text(json.dumps({'scope': 'Exact rational Galerkin continuation, zero on the omitted old modes.',
    'modes': modes, 'decimal_digits': a.digits, 'continuation_rational_coefficients': strings,
    'matrix_archive_sha256': record['matrix_archive_sha256']}, separators=(',', ':')) + '\n')
print('continuation', J.nrows(), 'x', J.ncols(), 'written to', a.output, Path(a.output).stat().st_size, 'bytes')
