#!/usr/bin/env python3
"""Certified outer bounds on the admissible prime-2 weight for central positivity.

For a horizon R in (log 2, log 3] only the delay log 2 enters the central form:
    Q_R(s) = Q_R^A + s M_2,   M_2 = -(log 2/sqrt 2)(S_a + S_a^*),  a = log 2,
s = 1 being the arithmetic weight.  The admissible set {s : Q_R(s) >= 0} is an
interval (Q_R(s) is affine in s).  This program

  * builds, with the unchanged weil-depth Arb builder (papers/shifted-zeta/
    weil-depth/numerics/certify_arb.py), the N-mode Legendre head of Q_R(1) and,
    with the prime list emptied, of Q_R^A;  M_2 = Q_R(1) - Q_R^A on the head;
  * for each requested trial weight s outside the admissible interval, certifies
        <v, Q_R(s) v>/<v, v> + eta < 0
    for a rational vector v (eta = profile remainder of the head).  Since the head
    is the exact form on the retained polynomials up to eta in operator norm,
    this proves that Q_R(s) is NOT positive: an outer bound on the interval;
  * optionally replays the weil-depth full Schur test for s = 1 at a floor m and
    records the elementary inner bound |s - 1| <= m / (log 2/sqrt 2), valid since
    ||M_2|| <= log 2/sqrt 2 when 2 log 2 > R.
Only python-flint (Arb), exact rationals and the standard library decide signs;
NumPy supplies candidate vectors and floating diagnostics only.

Prepared for Edward Baker, 24 September 2026, by Claude (Anthropic); session
configured as claude-fable-5-1, runtime-reported serving model Claude Opus 5.5
(claude-opus-5-5); the serving model may differ.  Reasoning effort not exposed.
"""
import argparse, hashlib, importlib.util, json, math, platform, sys, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

if not __debug__:
    raise SystemExit('Do not disable certificate assertions with python -O.')


def load_builder(root):
    path = root/'papers/shifted-zeta/weil-depth/numerics/certify_arb.py'
    spec = importlib.util.spec_from_file_location('weil_depth_certify_arb', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, path


def build(c, horizon, log_horizon, N, M, arch_only):
    args = argparse.Namespace(N=N, M=M, horizon=horizon, log_horizon=log_horizon)
    original = c.prime_powers
    if arch_only:
        c.prime_powers = lambda L, lh=None: []
    try:
        data = c.build(args)
    finally:
        c.prime_powers = original
    return data


def head(c, data):
    from flint import arb_mat as AM
    return AM([[c.unpack(x) for x in row] for row in data['matrices']['Q']])


def rational_vector(x, bits=64):
    scale = 2**bits
    return [F(int(round(float(t)*scale)), scale) for t in x]


def rayleigh_upper(c, Q, ids, v, eta):
    from flint import arb as A
    n = len(ids)
    va = [c.rat(t) for t in v]
    num = A(0)
    for i in range(n):
        row = A(0)
        for j in range(n):
            row += Q[ids[i], ids[j]]*va[j]
        num += va[i]*row
    den = sum((t*t for t in v), F(0))
    return num/c.rat(den) + eta


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--horizon')
    g.add_argument('--log-horizon', type=int)
    ap.add_argument('--N', type=int, default=128)
    ap.add_argument('--M', type=int, default=180)
    ap.add_argument('--bits', type=int, default=1536)
    ap.add_argument('--trial', action='append', default=[], help='rational trial weight s (repeatable)')
    ap.add_argument('--floor', help='rational central floor to replay at s = 1 (weil-depth Schur test)')
    ap.add_argument('--auto', action='store_true',
                    help='choose outer trials 2%% beyond the floating head edges and a floor 0.98 x head minimum')
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.repository or Path(__file__).resolve().parents[6]
    c, builder_path = load_builder(root)
    from flint import arb as A, arb_mat as AM, ctx
    ctx.prec = args.bits
    t0 = time.time()
    L = A(args.log_horizon).log() if args.log_horizon else c.rat(args.horizon)
    assert A(2).log() < L and (L < A(3).log() or args.log_horizon == 3), 'program scope: log 2 < R <= log 3'
    full = build(c, args.horizon, args.log_horizon, args.N, args.M, False)
    arch = build(c, args.horizon, args.log_horizon, args.N, args.M, True)
    assert [list(v) for v in full['active_prime_powers']] == [[2, 2, 1]]
    assert arch['active_prime_powers'] == []
    Q1, QA = head(c, full), head(c, arch)
    M2 = Q1 - QA
    eta = c.unpack(full['bounds']['profile_remainder'])
    assert eta.overlaps(c.unpack(arch['bounds']['profile_remainder']))
    eta_up = A(eta.upper())
    cstar = A(2).log()/A(2).sqrt()
    N = args.N
    sectors = {'even': list(range(0, N, 2)), 'odd': list(range(1, N, 2))}
    mid = lambda X: np.array([[float(X[i, j].mid()) for j in range(N)] for i in range(N)])
    q1, qa = mid(Q1), mid(QA)
    m2 = q1 - qa
    # Floating diagnostics: admissible interval of the N-mode head, per sector.
    def lam(s, ids):
        return np.linalg.eigvalsh((qa + s*m2)[np.ix_(ids, ids)])[0]
    def edge(ids, direction):
        lo, step = 1.0, 1e-9
        while lam(1.0 + direction*step, ids) > 0 and step < 1e3:
            step *= 2
        if step >= 1e3:
            return None
        a, b = 1.0 + direction*step/2, 1.0 + direction*step
        for _ in range(200):
            m = (a + b)/2
            if lam(m, ids) > 0: a = m
            else: b = m
        return (a + b)/2
    diag = {}
    for name, ids in sectors.items():
        diag[name] = {'head_lambda_min_at_s1': float(lam(1.0, ids)),
                      'head_lambda_min_at_s0': float(lam(0.0, ids)),
                      'head_upper_edge_s': edge(ids, +1), 'head_lower_edge_s': edge(ids, -1)}
    ups = [d['head_upper_edge_s'] for d in diag.values() if d['head_upper_edge_s'] is not None]
    lows = [d['head_lower_edge_s'] for d in diag.values() if d['head_lower_edge_s'] is not None]
    diag['head_interval_s'] = [max(lows) if lows else None, min(ups) if ups else None]
    def three_sig(x, down):
        e = math.floor(math.log10(abs(x)))
        q = F(10)**(e - 2)
        k = F(x)/q
        k = math.floor(k) if down else math.ceil(k)
        return F(k)*q
    if args.auto:
        lo_s, up_s = diag['head_interval_s']
        if up_s is not None:
            args.trial.append(str(1 + three_sig((up_s - 1)*1.02, down=False)))
        if lo_s is not None:
            args.trial.append(str(1 - three_sig((1 - lo_s)*1.02, down=False)))
        if not args.floor:
            hm = min(diag['even']['head_lambda_min_at_s1'], diag['odd']['head_lambda_min_at_s1'])
            args.floor = str(three_sig(0.98*hm, down=True))
    # Certified outer bounds.
    trials = []
    for s_text in args.trial:
        s = F(s_text)
        Qs = QA + M2*c.rat(s)
        best = None
        for name, ids in sectors.items():
            w, V = np.linalg.eigh((qa + float(s)*m2)[np.ix_(ids, ids)])
            v = rational_vector(V[:, 0])
            ub = rayleigh_upper(c, Qs, ids, v, eta_up)
            rec = {'sector': name, 'rayleigh_plus_eta_upper': c.show(ub), 'negative_certified': bool(ub < 0)}
            if best is None or (ub < 0 and not best[0]):
                best = (bool(ub < 0), rec)
        trials.append({'s': str(s), 'c_weight_decimal': float(s)*math.log(2)/math.sqrt(2),
                       'certified_not_positive': best[0], 'witness': best[1]})
        print('trial', s, best, flush=True)
    inner = None
    if args.floor:
        res = c.validate(full, args.floor)
        assert res['status'] == 'PASS', 'floor replay failed'
        m = F(args.floor)
        width = c.rat(m)/cstar
        # exact rational lower value for the inner half-width
        inner = {'central_floor_at_s1': str(m), 'schur_test': 'PASS (weil-depth validate)',
                 'inner_half_width_s_lower': c.show(A(width.lower())),
                 'statement': 'Q_R(s) >= (m - |s-1| log2/sqrt2) I >= 0 for |s-1| <= m sqrt2/log2'}
    out = {'date': '2026-09-24',
           'model': 'Claude (Anthropic); session configured claude-fable-5-1; runtime-reported serving model Claude Opus 5.5 (claude-opus-5-5); serving model may differ',
           'reasoning_effort': 'not exposed',
           'horizon': args.horizon, 'log_horizon': args.log_horizon, 'N': N, 'M': args.M, 'precision_bits': args.bits,
           'profile_remainder_upper': c.show(eta_up),
           'content_sha256': {'with_prime': c.content_sha256(full), 'arch_only': c.content_sha256(arch)},
           'builder_source_sha256': hashlib.sha256(builder_path.read_bytes()).hexdigest(),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'runtime': {'python': platform.python_version(), 'numpy': np.__version__},
           'floating_head_diagnostics': diag,
           'certified_outer_trials': trials, 'inner_bound': inner,
           'elapsed_seconds': time.time() - t0,
           'scope': 'Outer bounds are certified non-positivity of Q_R(s) (ball Rayleigh quotient plus profile remainder). '
                    'The inner bound is elementary from the replayed weil-depth floor. Floating head intervals are diagnostics.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('floating_head_diagnostics', 'inner_bound')}, indent=1))
    print('outer', [(t['s'], t['certified_not_positive']) for t in trials])


if __name__ == '__main__':
    main()
