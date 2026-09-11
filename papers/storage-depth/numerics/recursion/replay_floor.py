"""Archive-based replays with chosen or bisected floors, for both steps.

The recorded validators insert a fixed floor (1e-33 at the first step, 1e-36 at
the second) and report a sign. This script re-runs the same three guarded tests
from the hash-verified archives with the floor, residual factor, or comparison
threshold chosen on the command line, and can bisect for the largest passing
three-significant-figure value. It reads matrices through stream_io, so it
runs on machines with a few GB of memory.

Tests (identical reductions and error budgets to the recorded validators):
  absolute   (beta - m)(H - m) - E - [(beta - m) eta + e] I           > 0
  relative   (beta_theta - m)(H_theta - m) - E_theta - budget I        > 0
             passing certifies M_theta >= m, hence H_J >= m and
             R* F^-1 R <= theta H_J, and by the convex-combination lemma
             Q >= m / tau^2 with tau = (q + sqrt(q^2+4))/2, q = ||J||_F
  comparison beta_mu (H_J - mu A) - U_mu* E_o U_mu - budget I          > 0

An optional --oracle-tail-floor replaces the certified analytic complement
floor by a stated number. That run is a diagnostic of the finite matrices
only and is recorded as such; it is never a certificate.
"""
import argparse
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from flint import arb as A, arb_mat as AM, ctx
from common import *
import stream_io
import tails
import mpmath as mp

HERE = Path(__file__).resolve().parent
RECORDS = HERE.parent / 'records'


def brief(result):
    out = {k: v for k, v in result.items() if k not in ['pivots', 'pivot_ball']}
    if 'pivots' in result:
        out['positive_pivot_count'] = len(result['pivots'])
    return out


def three_figures(x):
    """Largest three-significant-figure decimal <= x, as a string."""
    if x <= 0:
        raise ValueError
    e = math.floor(math.log10(x)) - 2
    k = math.floor(x / 10 ** e + 1e-9)
    if k >= 1000:
        k, e = 100, e + 1
    return f'{k}e{e}'


def grid_next(s):
    k, e = s.split('e')
    k, e = int(k) + 1, int(e)
    if k >= 1000:
        k, e = 100, e + 1
    return f'{k}e{e}'


class Step:
    def __init__(self, step, bits, oracle=None, record_path=None, continuation_path=None, proposal_output=None):
        self.step = step
        self.oracle = oracle
        ctx.prec = bits
        self.bits = bits
        if step == 1:
            rel = 'history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz'
            meta, mats, record, path = stream_io.load_legacy(rel)
            self.H, Go, Gn = mats['head'], mats['gram_old'], mats['gram_new']
            self.no, self.nn = meta['old_modes'], meta['new_modes']
            self.modes = [self.no, self.nn]
            self.grams_old = [Go]
            self.Gn = Gn
            self.eta = c.unpack(meta['eta']).upper()
            self.e = c.unpack(meta['leakage_error']).upper()
            tb = meta['tail_bounds']
            self.go = A(tb['old_gamma_tail']).lower()
            self.gn = A(tb['new_gamma_tail']).lower()
            self.bg = A(tb['gamma_cross_norm_upper']).upper()
            self.rho = A(tb['arithmetic_norm_upper']).upper()
            prop_path = HISTORY / 'quarter-step-20260910/residual_128_32.json'
            prop = json.loads(prop_path.read_text())
            self.J = AM(self.nn, self.no)
            for i, row in enumerate(prop['continuation_rational_coefficients']):
                for j, v in enumerate(row):
                    self.J[i, j] = rat(v)
            self.L = logn(7) + (logn(8) - logn(7)) / 4
            self.betaA = (self.go - self.rho).lower()
            self.beta = ((self.go + self.gn - ((self.go - self.gn) ** 2 + 4 * self.bg ** 2).sqrt()) / 2 - self.rho).lower()
            self.identity = {'archive': rel, 'matrix_archive_sha256': record['matrix_archive_sha256'],
                             'matrices_content_sha256': record['matrices_content_sha256'],
                             'continuation_record': str(prop_path.relative_to(HISTORY)),
                             'continuation_record_sha256': legacy_io.file_hash(prop_path)}
        else:
            record_path = Path(record_path) if record_path else RECORDS / 'second-quarter-build.json'
            meta, mats, record, path = stream_io.load_record(record_path)
            self.H = mats['head']
            modes = meta['modes']
            self.modes = modes
            self.nn = modes[-1]
            self.no = self.H.nrows() - self.nn
            allgrams = [mats[f'gram_{i}'] for i in range(len(modes))]
            self.grams_old = allgrams[:-1]
            self.Gn = allgrams[-1]
            self.eta = c.unpack(meta['eta']).upper()
            self.e = c.unpack(meta['leakage_error']).upper()
            tb = meta['tail_bounds']
            self.gamma = AM([[c.unpack(x) for x in row] for row in tb['gamma_comparison']])
            self.rho = A(tb['arithmetic']['norm_upper']).upper()
            self.beta = A(tb['joint_tail_floor']).lower()
            prop_path = Path(continuation_path) if continuation_path else RECORDS / 'second-quarter-continuation.json'
            if prop_path.exists():
                prop = json.loads(prop_path.read_text())
                assert prop['matrix_archive_sha256'] == record['matrix_archive_sha256']
                self.J = AM([[rat(s) for s in row] for row in prop['continuation_rational_coefficients']])
            else:
                # Galerkin continuation on the head, rounded to 80 decimal digits, as in certify_step.py.
                assert proposal_output, 'no continuation record; give --proposal-output to write the Galerkin proposal'
                no_, nn_ = self.no, self.nn
                F = sub(self.H, range(no_, no_ + nn_), range(no_, no_ + nn_))
                B = sub(self.H, range(no_, no_ + nn_), range(no_))
                mp.mp.dps = 120
                self.J, strings = residual.rational_matrix(-F.solve(B), 80)
                prop_path = Path(proposal_output)
                prop_path.write_text(json.dumps({'scope': 'Exact rational Galerkin continuation, zero on the omitted old modes.',
                                                 'modes': modes, 'decimal_digits': 80,
                                                 'continuation_rational_coefficients': strings,
                                                 'matrix_archive_sha256': record['matrix_archive_sha256']},
                                                separators=(',', ':')) + '\n')
                assert prop_path.stat().st_size < 1048576
            assert self.J.nrows() == self.nn and self.J.ncols() == self.no
            lengths = [LogPoint.read(x) for x in meta['partition']]
            self.L = sum(lengths, ZERO)
            gammaold = sub(self.gamma, range(self.gamma.nrows() - 1), range(self.gamma.nrows() - 1))
            self.betaA = tails.eigen_floor(gammaold - ident(gammaold.nrows()) * self.rho)
            self.identity = {'archive': record['matrix_archive'], 'matrix_archive_sha256': record['matrix_archive_sha256'],
                             'matrices_content_sha256': record['matrices_content_sha256'],
                             'build_record_sha256': legacy_io.file_hash(record_path),
                             'continuation_record': prop_path.name,
                             'continuation_record_sha256': legacy_io.file_hash(prop_path)}
        N = self.H.nrows()
        self.N = N
        no, nn = self.no, self.nn
        self.T = ident(N)
        for i in range(nn):
            for j in range(no):
                self.T[no + i, j] = self.J[i, j]
        self.To = sub(self.T, range(N), range(no))
        Go = sum(self.grams_old, AM(N, N))
        Ho = sub(self.H, range(no), range(N))
        Hn = sub(self.H, range(no, N), range(N))
        self.Eo = c.sym(Go - Ho.transpose() * Ho)
        self.En = c.sym(self.Gn - Hn.transpose() * Hn)
        self.E = c.sym(Go + self.Gn - self.H * self.H)
        self.MH = c.sym(self.T.transpose() * self.H * self.T)
        self.Ao = sub(self.H, range(no), range(no))
        self.HJ = sub(self.MH, range(no), range(no))
        self.Eot = c.sym(self.T.transpose() * self.Eo * self.T)
        self.Ent = c.sym(self.T.transpose() * self.En * self.T)
        # Disjoint-window arithmetic cross bound, checked exactly as in certify_step.py.
        oldlength = self.L - ((logn(8) - logn(7)) / 4)
        windows, alpha = [], []
        for n, p, _ in active_powers(self.L):
            lo = max(ZERO, oldlength - logn(n))
            hi = min(oldlength, self.L - logn(n))
            if lo < hi:
                windows.append((lo, hi))
                alpha.append(A(p).log() / A(n).sqrt())
        disjoint = all(not (max(a, c0) < min(b, d)) for i, (a, b) in enumerate(windows) for c0, d in windows[i + 1:])
        self.ba = sum((x * x for x in alpha), A(0)).sqrt() if disjoint else sum(alpha, A(0))
        self.disjoint = disjoint
        q = frob2(self.J).sqrt()
        self.q = q
        self.tau2 = (((q * q + 4).sqrt() + q) / 2) ** 2
        self.f0 = None
        if step == 2:
            self.f0 = residual.row_floor((logn(8) - logn(7)).value() / 4, meta['profile_degree'], c.profile(meta['profile_degree']))
        else:
            self.f0 = residual.row_floor((A(8).log() - A(7).log()) / 4, 320, c.profile(320))

    def tail_floor_relative(self, lam):
        if self.step == 1:
            return ((self.go + self.gn - ((self.go - self.gn) ** 2 + 4 * (lam * self.bg) ** 2).sqrt()) / 2
                    - self.rho - (lam - 1) * self.ba).lower()
        gm = AM(self.gamma.tolist())
        k = gm.nrows() - 1
        for i in range(k):
            gm[i, k] = gm[k, i] = gm[i, k] * lam
        return tails.eigen_floor(gm - ident(k + 1) * (self.rho + (lam - 1) * self.ba))

    def absolute(self, m_text):
        m = rat(m_text)
        beta = A(self.oracle).lower() if self.oracle else self.beta
        bm = (beta - m).lower()
        if not bm > 0:
            return {'positive': False, 'reason': 'No positive complement floor above m'}, beta
        budget = (bm * self.eta + self.e).upper()
        return ldl(c.sym(bm * (self.H - ident(self.N) * m) - self.E - ident(self.N) * budget)), beta

    def relative(self, theta_text, m_text='0'):
        theta = rat(theta_text)
        assert 0 < theta < 1
        lam = (1 / theta).sqrt()
        m = rat(m_text)
        bt = A(self.oracle).lower() if self.oracle else self.tail_floor_relative(lam)
        bm = (bt - m).lower()
        if not bm > 0:
            return {'positive': False, 'reason': 'No positive modified complement floor above m'}, bt
        N, no = self.N, self.no
        Do = AM([[1 if i == j and i < no else lam if i == j else 0 for j in range(N)] for i in range(N)])
        Dn = AM([[lam if i == j and i < no else 1 if i == j else 0 for j in range(N)] for i in range(N)])
        leakage = c.sym(Do * self.Eot * Do + Dn * self.Ent * Dn)
        enlarged = AM([[self.MH[i, j] * (lam if (i < no) != (j < no) else 1) for j in range(N)] for i in range(N)])
        budget = (bm * 2 * lam * self.eta * frob2(self.T) + self.e * (frob2(self.T * Do) + frob2(self.T * Dn))).upper()
        return ldl(c.sym(bm * (enlarged - ident(N) * m) - leakage - ident(N) * budget)), bt

    def comparison(self, mu_text):
        mu = rat(mu_text)
        assert 0 < mu < 1
        U = AM(self.To.tolist())
        for i in range(self.no):
            U[i, i] = 1 - mu
        betaA = A(self.oracle).lower() if self.oracle else self.betaA
        bm = ((1 - mu) * betaA).lower()
        budget = (bm * self.eta * (frob2(self.To) + mu) + self.e * frob2(U)).upper()
        return ldl(c.sym(bm * (self.HJ - mu * self.Ao) - U.transpose() * self.Eo * U - ident(self.no) * budget)), bm


def bisect(test, lo_text, hi_text, log):
    """Largest passing three-figure value in [lo, hi), given lo passes and hi fails."""
    lo, hi = Fraction(lo_text), Fraction(hi_text)
    r, aux = test(lo_text)
    log.append({'value': lo_text, 'check': brief(r)})
    if not r['positive']:
        return None
    r, aux = test(hi_text)
    log.append({'value': hi_text, 'check': brief(r)})
    if r['positive']:
        return hi_text
    best = lo_text
    while True:
        mid = three_figures(math.sqrt(float(lo) * float(hi)))
        if Fraction(mid) <= lo or Fraction(mid) >= hi:
            mid = grid_next(three_figures(float(lo)))
            if Fraction(mid) >= hi:
                return best
        r, aux = test(mid)
        log.append({'value': mid, 'check': brief(r)})
        if r['positive']:
            lo, best = Fraction(mid), mid
        else:
            hi = Fraction(mid)


def run(args):
    assert __debug__
    start = time.monotonic()
    S = Step(args.step, args.bits, args.oracle_tail_floor, args.record, args.continuation, args.proposal_output)
    out = {'scope': ('Archive-based floor replays with chosen or bisected thresholds; same reductions and error budgets '
                     'as the recorded validators; streaming dual-hash verified load.'),
           'step': args.step, 'precision_bits': args.bits, 'modes': S.modes,
           'oracle_tail_floor': args.oracle_tail_floor,
           'oracle_note': (None if not args.oracle_tail_floor else
                           'DIAGNOSTIC ONLY: the analytic complement floor was replaced by the stated number; '
                           'no certificate is claimed from these runs.'),
           'identity': S.identity, 'certified_complement_floor': S.beta.str(40),
           'old_complement_floor_for_comparison': S.betaA.str(40),
           'arithmetic_cross_disjoint_windows': S.disjoint, 'arithmetic_cross_norm_upper': S.ba.upper().str(40),
           'J_frobenius_upper': S.q.upper().str(40), 'graph_norm_squared_upper': S.tau2.upper().str(40),
           'new_slab_floor_lower': S.f0.str(40), 'absolute': [], 'relative': [], 'comparison': [], 'bisections': {}}
    for m in args.absolute or []:
        r, beta = S.absolute(m)
        out['absolute'].append({'floor': m, 'complement_floor': beta.str(40), 'check': brief(r)})
        print('absolute', m, brief(r), flush=True)
    for spec in args.relative or []:
        theta, m = (spec.split(':') + ['0'])[:2]
        r, bt = S.relative(theta, m)
        out['relative'].append({'theta': theta, 'floor': m, 'modified_complement_floor': bt.str(40), 'check': brief(r)})
        print('relative', theta, m, brief(r), flush=True)
    for mu in args.mu or []:
        r, bm = S.comparison(mu)
        out['comparison'].append({'mu': mu, 'tail_floor': bm.str(40), 'check': brief(r)})
        print('comparison', mu, brief(r), flush=True)
    if args.bisect_absolute:
        log = []
        best = bisect(lambda m: S.absolute(m), *args.bisect_absolute, log)
        out['bisections']['absolute'] = {'bracket': args.bisect_absolute, 'largest_passing_floor': best, 'trace': log}
        print('bisect absolute ->', best, flush=True)
    for spec in args.bisect_relative or []:
        theta, lo, hi = spec.split(':')
        log = []
        best = bisect(lambda m: S.relative(theta, m), lo, hi, log)
        out['bisections'][f'relative_theta_{theta}'] = {'theta': theta, 'bracket': [lo, hi], 'largest_passing_floor': best,
                                                        'trace': log}
        if best and not args.oracle_tail_floor:
            out['bisections'][f'relative_theta_{theta}']['direct_floor_lower'] = (rat(best) / S.tau2).lower().str(40)
        print('bisect relative', theta, '->', best, flush=True)
    if args.bisect_mu:
        log = []
        best = bisect(lambda mu: S.comparison(mu), *args.bisect_mu, log)
        out['bisections']['comparison'] = {'bracket': args.bisect_mu, 'largest_passing_mu': best, 'trace': log}
        print('bisect mu ->', best, flush=True)
    out['source_sha256'] = source_hashes()
    out['seconds'] = time.monotonic() - start
    Path(args.output).write_text(json.dumps(out, indent=2) + '\n')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--step', type=int, choices=[1, 2], required=True)
    p.add_argument('--bits', type=int, default=2048)
    p.add_argument('--output', required=True)
    p.add_argument('--absolute', nargs='*', help='floors m for the absolute test')
    p.add_argument('--relative', nargs='*', help='theta or theta:m for the relative test')
    p.add_argument('--mu', nargs='*', help='thresholds for the comparison test')
    p.add_argument('--bisect-absolute', nargs=2, metavar=('LO', 'HI'))
    p.add_argument('--bisect-relative', nargs='*', metavar='THETA:LO:HI')
    p.add_argument('--bisect-mu', nargs=2, metavar=('LO', 'HI'))
    p.add_argument('--oracle-tail-floor', help='DIAGNOSTIC: replace the certified complement floor')
    p.add_argument('--record', help='step 2: build record to replay (default numerics/records/second-quarter-build.json)')
    p.add_argument('--continuation', help='step 2: continuation record (default numerics/records/second-quarter-continuation.json)')
    p.add_argument('--proposal-output', help='step 2: where to write the Galerkin continuation if the continuation record does not exist')
    run(p.parse_args())
