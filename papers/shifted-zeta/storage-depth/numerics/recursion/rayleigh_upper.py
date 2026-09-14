"""Ball Rayleigh upper bounds for lambda_min(Q_{0,L}) from the spatial heads.

For a rational vector v in the verification space, Q[v]/||v||^2 is exactly
(v* (P Q P) v)/||v||^2, and the stored model head differs from P Q P by at most
eta in operator norm, so

    lambda_min(Q_{0,L}) <= (v* H~ v)/(v* v) + eta,

evaluated in ball arithmetic and rounded outward. The vector is the lowest
eigenvector of the head midpoints (approximate complex eigensolver at modest
precision), rounded to decimal rationals. This is the same device as the upper
bounds of the Weil-depth paper. It is an upper bound within the working
normalization; it uses nothing but the hash-verified head.
"""
import argparse
import json
import time
from pathlib import Path
import mpmath as mp
from flint import arb as A, arb_mat as AM, acb_mat as CM, ctx
from common import *
import stream_io

RECORDS = Path(__file__).resolve().parent.parent / 'records'


def run(args):
    assert __debug__
    start = time.monotonic()
    if args.step == 1:
        rel = 'history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz'
        meta, mats, record, path = stream_io.load_legacy(rel, want={'head'})
        identity = {'archive': rel, 'matrix_archive_sha256': record['matrix_archive_sha256'],
                    'matrices_content_sha256': record['matrices_content_sha256']}
        horizon = 'L_q = 3/4 log 14'
    else:
        record_path = RECORDS / 'second-quarter-build.json'
        meta, mats, record, path = stream_io.load_record(record_path, want={'head'})
        identity = {'archive': record['matrix_archive'], 'matrix_archive_sha256': record['matrix_archive_sha256'],
                    'matrices_content_sha256': record['matrices_content_sha256'],
                    'build_record_sha256': legacy_io.file_hash(record_path)}
        horizon = 'L_2 = log(56)/2'
    H = mats['head']
    n = H.nrows()
    eta = c.unpack(meta['eta']).upper()
    # approximate lowest eigenvector from midpoints
    ctx.prec = args.approx_bits
    mid = AM([[x.mid() for x in row] for row in H.tolist()])
    E, R = CM(mid).eig(right=True, algorithm='approx')
    k = min(range(n), key=lambda i: float(E[i].real.mid()))
    vec = [R[i, k].real.mid() for i in range(n)]
    scale = max(abs(float(x)) for x in vec)
    mp.mp.dps = args.digits + 10
    strings = [mp.nstr(mp.mpf(x.str(args.digits + 5, radius=False)) / mp.mpf(str(scale)), args.digits) for x in vec]
    # rigorous quotient
    ctx.prec = args.bits
    v = AM([[rat(s)] for s in strings])
    num = (v.transpose() * H * v)[0, 0]
    den = (v.transpose() * v)[0, 0]
    quotient = num / den
    upper = (quotient + eta).upper()
    out = {'scope': 'Ball Rayleigh upper bound for lambda_min of the central form from the spatial head; working normalization.',
           'step': args.step, 'horizon': horizon, 'modes': n, 'precision_bits': args.bits,
           'approximate_eigenvalue_midpoint': E[k].real.mid().str(20, radius=False),
           'rayleigh_quotient': quotient.str(40), 'head_error_eta_upper': eta.str(20),
           'upper_bound_lambda_min': upper.str(20),
           'vector_decimal_digits': args.digits, 'vector': strings,
           'identity': identity, 'source_sha256': source_hashes(), 'seconds': time.monotonic() - start}
    Path(args.output).write_text(json.dumps(out, indent=2) + '\n')
    print('step', args.step, 'upper bound lambda_min <=', upper.str(12), 'quotient', quotient.str(15), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--step', type=int, choices=[1, 2], required=True)
    p.add_argument('--bits', type=int, default=2048)
    p.add_argument('--approx-bits', type=int, default=768)
    p.add_argument('--digits', type=int, default=60)
    p.add_argument('--output', required=True)
    run(p.parse_args())
