"""Ball Rayleigh upper bound for lambda_min from any second-step build record.

Identical device to recursion/rayleigh_upper.py (rounded lowest eigenvector of
the head midpoints; ball quotient plus the head error eta), for an arbitrary
--record. Lives outside numerics/recursion/ to leave the recorded builder-source
hashes untouched.
"""
import argparse, json, sys, time
from pathlib import Path
import mpmath as mp
from flint import arb as A, arb_mat as AM, acb_mat as CM, ctx
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'recursion'))
from common import *
import stream_io

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--record', required=True); p.add_argument('--output', required=True)
p.add_argument('--bits', type=int, default=2048); p.add_argument('--approx-bits', type=int, default=768)
p.add_argument('--digits', type=int, default=60)
a = p.parse_args(); start = time.monotonic()
meta, mats, record, path = stream_io.load_record(a.record, want={'head'})
H = mats['head']; n = H.nrows(); eta = c.unpack(meta['eta']).upper()
ctx.prec = a.approx_bits
E, R = CM(AM([[x.mid() for x in row] for row in H.tolist()])).eig(right=True, algorithm='approx')
k = min(range(n), key=lambda i: float(E[i].real.mid()))
vec = [R[i, k].real.mid() for i in range(n)]; scale = max(abs(float(x)) for x in vec)
mp.mp.dps = a.digits + 10
strings = [mp.nstr(mp.mpf(x.str(a.digits + 5, radius=False)) / mp.mpf(str(scale)), a.digits) for x in vec]
ctx.prec = a.bits
v = AM([[rat(s)] for s in strings])
quotient = (v.transpose() * H * v)[0, 0] / (v.transpose() * v)[0, 0]
upper = (quotient + eta).upper()
out = {'scope': 'Ball Rayleigh upper bound for lambda_min of the central form from the spatial head; working normalization.',
       'record': str(a.record), 'modes': meta['modes'], 'precision_bits': a.bits,
       'approximate_eigenvalue_midpoint': E[k].real.mid().str(20, radius=False),
       'rayleigh_quotient': quotient.str(40), 'head_error_eta_upper': eta.str(20), 'upper_bound_lambda_min': upper.str(20),
       'vector_decimal_digits': a.digits, 'vector': strings,
       'identity': {'archive': record['matrix_archive'], 'matrix_archive_sha256': record['matrix_archive_sha256'],
                    'matrices_content_sha256': record['matrices_content_sha256'], 'build_record_sha256': legacy_io.file_hash(a.record)},
       'source_sha256': source_hashes(), 'seconds': time.monotonic() - start}
Path(a.output).write_text(json.dumps(out, indent=2) + '\n')
print('upper bound lambda_min <=', upper.str(12), 'quotient', quotient.str(15))
