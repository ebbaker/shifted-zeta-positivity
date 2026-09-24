#!/usr/bin/env python3
"""Bracket the length R_A at which the prime-free central form Q^A loses positivity.

Q^A_R is the central form with every delayed arithmetic term removed (local
constant, complete gamma memory and both poles kept).  For R < log 2 it equals the
complete form.  The unchanged weil-depth Arb builder is run with its prime list
emptied:
  * at --lower, the full weil-depth Schur test (analytic tail, full-output Grams)
    is replayed at a floor m > 0: Q^A_lower >= m I on all inputs;
  * at --upper, a rational Ritz vector v of the N-mode head gives a certified
    ball bound <v, Q^A v>/<v, v> + eta < 0: Q^A_upper is not positive.
Hence lower < R_A <= upper, where R_A = inf{R : Q^A_R is not positive}.

Prepared for Edward Baker, 24 September 2026, by Claude (Anthropic); session
configured as claude-fable-5-1, runtime-reported serving model Claude Opus 5.5
(claude-opus-5-5); the serving model may differ.  Reasoning effort not exposed.
"""
import argparse, hashlib, importlib.util, json, platform, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

if not __debug__:
    raise SystemExit('Do not disable certificate assertions with python -O.')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--lower', default='37/50')
    ap.add_argument('--upper', default='149/200')
    ap.add_argument('--floor', default=None, help='floor at --lower; default 0.97 x head minimum (3 s.f., down)')
    ap.add_argument('--N', type=int, default=128)
    ap.add_argument('--M', type=int, default=180)
    ap.add_argument('--bits', type=int, default=1536)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.repository or Path(__file__).resolve().parents[6]
    builder = root/'papers/shifted-zeta/weil-depth/numerics/certify_arb.py'
    spec = importlib.util.spec_from_file_location('weil_depth_certify_arb', builder)
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
    from flint import arb as A, ctx
    ctx.prec = args.bits
    t0 = time.time()
    c.prime_powers = lambda L, lh=None: []          # remove every delayed arithmetic term
    N = args.N
    sectors = {'even': list(range(0, N, 2)), 'odd': list(range(1, N, 2))}
    out = {}
    # lower horizon: full Schur test of the prime-free form
    lo = c.build(argparse.Namespace(N=N, M=args.M, horizon=args.lower, log_horizon=None))
    assert lo['active_prime_powers'] == []
    Qlo = np.array([[float(c.unpack(x).mid()) for x in row] for row in lo['matrices']['Q']])
    hm = min(np.linalg.eigvalsh(Qlo[np.ix_(ids, ids)])[0] for ids in sectors.values())
    if args.floor is None:
        import math
        e = math.floor(math.log10(0.97*hm)); q = F(10)**(e - 2)
        args.floor = str(F(math.floor(F(0.97*hm)/q))*q)
    res = c.validate(lo, args.floor)
    assert res['status'] == 'PASS', 'prime-free Schur test failed at the lower horizon'
    out['lower'] = {'R': args.lower, 'decimal': float(F(args.lower)), 'prime_free_floor': args.floor,
                    'head_lambda_min_diagnostic': float(hm), 'schur_test': 'PASS',
                    'matrices_content_sha256': c.content_sha256(lo)}
    # upper horizon: certified negative Rayleigh quotient
    up = c.build(argparse.Namespace(N=N, M=args.M, horizon=args.upper, log_horizon=None))
    assert up['active_prime_powers'] == []
    from flint import arb_mat as AM
    Q = AM([[c.unpack(x) for x in row] for row in up['matrices']['Q']])
    eta = A(c.unpack(up['bounds']['profile_remainder']).upper())
    qm = np.array([[float(Q[i, j].mid()) for j in range(N)] for i in range(N)])
    best = None
    for name, ids in sectors.items():
        w, V = np.linalg.eigh(qm[np.ix_(ids, ids)])
        v = [F(int(round(float(t)*2**64)), 2**64) for t in V[:, 0]]
        va = [c.rat(t) for t in v]
        num = A(0)
        for i in range(len(ids)):
            row = A(0)
            for j in range(len(ids)):
                row += Q[ids[i], ids[j]]*va[j]
            num += va[i]*row
        ub = num/c.rat(sum((t*t for t in v), F(0))) + eta
        rec = {'sector': name, 'head_lambda_min_diagnostic': float(w[0]), 'rayleigh_plus_eta_upper': c.show(ub),
               'negative_certified': bool(ub < 0)}
        if best is None or (rec['negative_certified'] and not best['negative_certified']):
            best = rec
    assert best['negative_certified'], 'no certified negative direction at the upper horizon'
    out['upper'] = {'R': args.upper, 'decimal': float(F(args.upper)), 'witness': best,
                    'matrices_content_sha256': c.content_sha256(up)}
    result = {'date': '2026-09-24',
              'model': 'Claude (Anthropic); session configured claude-fable-5-1; runtime-reported serving model Claude Opus 5.5 (claude-opus-5-5); serving model may differ',
              'reasoning_effort': 'not exposed', 'N': N, 'M': args.M, 'precision_bits': args.bits,
              'bracket': out, 'conclusion': f'{args.lower} < R_A <= {args.upper} for the prime-free central form',
              'log2_decimal': float(np.log(2.0)),
              'builder_source_sha256': hashlib.sha256(builder.read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'runtime': {'python': platform.python_version(), 'numpy': np.__version__},
              'elapsed_seconds': time.time() - t0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['bracket'], indent=1)); print(result['conclusion'])


if __name__ == '__main__':
    main()
