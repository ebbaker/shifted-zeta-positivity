#!/usr/bin/env python3
"""Two-sided enclosure of the bottom of the central spectrum from a saved archive.

For each reflection sector r = +1 (even) and r = -1 (odd), this script

  * bisects the largest floor m_r for which the certified finite test
        (a - m)(q_r - m I) - E_r - epsilon(m) I  >= 0
    passes in ball arithmetic (the same test as certify_arb.validate, with the
    analytic tail floor a, the exact parity leakage E_r and the profile error
    epsilon recomputed from the archive), rounds it DOWN to a fixed number of
    significant figures and re-tests that exact rational;
  * certifies an upper bound: the head q_r is the exact form on the retained
    polynomials up to the profile error eta, so for any rational vector v in the
    sector, <v, q_r v>/<v, v> + eta (evaluated with balls) is an upper bound for
    the bottom of the sector spectrum.  v approximates the ground state of q_r.

The overall floor m_L = min(m_+, m_-) is re-tested in both sectors.  A sufficient
shift interval and decay for the transfer bound are then derived exactly:
    m_L - C h^2 / 3 >= d,  C an integer above the generator constant C_L.
Only python-flint and the standard library decide anything; mpmath is used to
find the candidate ground-state vector (a diagnostic), never for a bound.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, gzip, hashlib, json, math, platform, sys
import flint
from flint import arb as A, arb_mat as AM, ctx
import certify_arb as c

if not __debug__:
    raise RuntimeError('Enclosure checks require assertions; do not use Python -O or -OO')


def load(folder):
    archive = c.locate(folder/'central_matrices.json.gz')
    with gzip.open(archive, 'rt') as f:
        data = json.load(f)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    cert_path = folder/'central_certificate.json'
    if cert_path.exists():
        cert = json.loads(cert_path.read_text())
        if cert.get('matrix_archive_sha256') not in (None, digest):
            raise ValueError('central_certificate.json does not match the archive hash')
    return data, digest


def horizon(data):
    if data['log_horizon'] is not None:
        return A(data['log_horizon']).log(), 'log%d' % data['log_horizon']
    return c.rat(data['horizon']), data['horizon']


class Sector:
    """Finite test for one parity, built exactly as in certify_arb.validate."""

    def __init__(self, data, parity, bounds, mats, a_lower, eta_upper):
        N = data['N']
        self.ids = list(range(parity, N, 2))
        self.n = len(self.ids)
        self.head = c.block(mats['Q'], self.ids)
        leakage = (c.block(mats['Gram_causal'], self.ids)
                   + (-1)**parity*c.block(mats['ReflectedGram_causal'], self.ids))/2 - self.head*self.head
        assert leakage.overlaps(c.block(mats['E_central'], self.ids))
        self.leakage = c.sym(leakage)
        self.a, self.eta = a_lower, eta_upper
        self.I = c.ident(self.n)

    def passes(self, m):
        m = c.rat(m)
        if not self.a > m or not m > 0:
            return False
        err = ((self.a - m).abs_upper() + 40000)*self.eta + 2*self.eta**2
        test = (self.head - self.I*m)*(self.a - m) - self.leakage - self.I*err.upper()
        return c.ldl(test)['positive']

    def upper_bound(self, digits=40):
        """Ball Rayleigh quotient of a rational approximation to the head ground state."""
        import mpmath as mp
        mp.mp.dps = 60
        q = mp.matrix([[mp.mpf(int(self.head[i, j].mid().man_exp()[0]))*mp.mpf(2)**int(self.head[i, j].mid().man_exp()[1])
                        for j in range(self.n)] for i in range(self.n)])
        E, V = mp.eigsy(q)
        order = sorted(range(self.n), key=lambda i: E[i])
        k = order[0]
        v = AM([[c.rat(F(mp.nstr(V[i, k], digits)))] for i in range(self.n)])
        ray = (v.transpose()*self.head*v)[0, 0]/(v.transpose()*v)[0, 0]
        upper = (ray + self.eta).upper()
        lowest = [mp.nstr(E[i], 8) for i in order[:6]]
        return upper, ray, lowest


def round_down_sig(x, sig):
    """Largest decimal with `sig` significant figures not exceeding the positive float x."""
    e = math.floor(math.log10(x))
    scale = F(10)**(e - sig + 1)
    return F(math.floor(F(x)/scale))*scale


def fmt(fr):
    """Compact decimal string of a Fraction such as 334/10^25 -> '3.34e-23'."""
    s = format(float(fr), '.3e')
    m, e = s.split('e')
    m = m.rstrip('0').rstrip('.')
    return f'{m}e{int(e)}'


def bisect_floor(sector, upper_bound_float, sig, steps=20):
    """Largest floor passing the sector test, rounded down to `sig` significant figures
    and re-tested as an exact rational."""
    hi = math.log10(upper_bound_float)      # no floor can pass above the head bottom
    lo = float(math.floor(hi - 12.0))
    assert sector.passes(F(10)**int(lo)), 'no passing floor found in the search window'
    for _ in range(steps):
        mid = (lo + hi)/2
        if sector.passes(F(format(10**mid, '.6e'))):
            lo = mid
        else:
            hi = mid
    cand = round_down_sig(10**lo, sig)
    assert sector.passes(cand)
    return cand


def continuation(m, change):
    """Integer generator bound C > C_L, then 1-significant-figure decay d <= m/2 and
    the largest 1-significant-figure shift h with m - C h^2/3 >= d (exact rationals)."""
    C = F(1)
    while not change < c.rat(C):
        C += 1
    d = round_down_sig(float(m)/2, 1)
    # largest h = k*10^e (k in 1..9) with m - C h^2/3 >= d
    hmax = math.sqrt(3*float(m - d)/float(C))
    h = round_down_sig(hmax, 1)
    while m - C*h*h/3 < d:
        h = round_down_sig(float(h)*0.999, 1)
    assert m - C*h*h/3 >= d and 0 < h <= F(1, 2)
    return C, h, d, m - C*h*h/3 - d


def enclose(folder, sig, bits):
    data, digest = load(folder)
    ctx.prec = max(bits or 0, data['precision_bits'])
    N = data['N']
    mats = {k: AM([[c.unpack(x) for x in row] for row in mat]) for k, mat in data['matrices'].items()}
    for mat in mats.values():
        assert mat.nrows() == N and mat.ncols() == N
        c.sym(mat)
    L, label = horizon(data)
    active = c.prime_powers(L, data['log_horizon'])
    assert [list(v) for v in active] == [list(v) for v in data['active_prime_powers']]
    bounds = c.analytic(L, c.profile(data['M']), N, active, data['log_horizon'])
    for key, value in bounds.items():
        assert value.overlaps(c.unpack(data['bounds'][key]))
    assert sum((mats['Gram_causal'][i, i] for i in range(N)), A(0)) < 10**7
    a_lower, eta_upper = bounds['tail_floor'].lower(), bounds['profile_remainder'].upper()
    out = {'horizon_label': label, 'horizon_value': c.show(L), 'N': N, 'M': data['M'],
           'precision_bits': ctx.prec, 'matrix_archive_sha256': digest,
           'matrices_content_sha256': c.content_sha256(data),
           'active_prime_powers': active, 'tail_floor_lower': c.show(a_lower),
           'profile_remainder_upper': c.show(eta_upper), 'sectors': {}}
    floors = []
    for parity, name in ((0, 'even'), (1, 'odd')):
        sec = Sector(data, parity, bounds, mats, a_lower, eta_upper)
        upper, ray, lowest = sec.upper_bound()
        m_r = bisect_floor(sec, float(upper.mid()), sig)
        assert c.rat(m_r) <= upper  # lower bound cannot exceed the certified upper bound
        floors.append(m_r)
        out['sectors'][name] = {
            'certified_floor': fmt(m_r), 'certified_floor_rational': f'{m_r.numerator}/{m_r.denominator}',
            'certified_upper_bound': upper.str(8),
            'rayleigh_quotient_ball': ray.str(15),
            'head_eigenvalues_lowest_diagnostic': lowest,
            'ground_state_simple_diagnostic': float(lowest[1]) > 1000*float(lowest[0])}
        print(name, 'floor', fmt(m_r), 'upper', upper.str(6), 'head eigs', lowest[:3], flush=True)
    m_L = min(floors)
    both = [Sector(data, p, bounds, mats, a_lower, eta_upper).passes(m_L) for p in (0, 1)]
    assert all(both)
    C, h, d, margin = continuation(m_L, bounds['generator_change_constant'])
    out['central_floor'] = fmt(m_L)
    out['central_floor_rational'] = f'{m_L.numerator}/{m_L.denominator}'
    out['central_floor_passes_both_sectors'] = True
    out['generator_change_constant'] = c.show(bounds['generator_change_constant'])
    out['continuation'] = {'generator_bound': str(C), 'shift_maximum': fmt(h), 'decay': fmt(d),
                           'shift_rational': f'{h.numerator}/{h.denominator}', 'decay_rational': f'{d.numerator}/{d.denominator}',
                           'exact_margin': f'{margin.numerator}/{margin.denominator}',
                           'norm_bound': f'||V_(omega,L)|| <= exp(-{fmt(d)} omega) for 0 < omega <= {fmt(h)}'}
    out['runtime'] = {'python': platform.python_version(), 'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__}
    out['scope'] = ('Lower bounds: exact rationals passing the certified full-operator Schur test in each sector. '
                    'Upper bounds: ball Rayleigh quotients of rational retained vectors plus the profile error. '
                    'Head eigenvalue lists are floating-point diagnostics.')
    (folder/'enclosure.json').write_text(json.dumps(out, indent=2)+'\n')
    return out


def summary(folders, outdir):
    rows = []
    for folder in folders:
        e = json.loads((folder/'enclosure.json').read_text())
        rows.append(e)
    rows.sort(key=lambda e: float(e['horizon_value'].strip('[]').split(' ')[0]))
    (outdir/'enclosure_summary.json').write_text(json.dumps(rows, indent=1)+'\n')
    lines = []
    for e in rows:
        act = ', '.join(str(n) for n, p, k in e['active_prime_powers']) or '---'
        lines.append(f"{e['horizon_label']} & {act} & {e['sectors']['even']['certified_floor']} & {e['sectors']['odd']['certified_floor']} & "
                     f"{e['sectors']['even']['certified_upper_bound'].split(' ')[0].strip('[')} & {e['sectors']['odd']['certified_upper_bound'].split(' ')[0].strip('[')} & "
                     f"{e['continuation']['generator_bound']} & {e['continuation']['shift_maximum']} & {e['continuation']['decay']} \\\\")
    (outdir/'enclosure_table.tex').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('folders', nargs='+')
    ap.add_argument('--sig', type=int, default=3, help='significant figures for the reported floor')
    ap.add_argument('--bits', type=int, default=0)
    ap.add_argument('--summary', help='directory for enclosure_summary.json / enclosure_table.tex')
    args = ap.parse_args()
    folders = [Path(f) for f in args.folders]
    for folder in folders:
        print('==', folder, flush=True)
        enclose(folder, args.sig, args.bits)
    if args.summary:
        summary(folders, Path(args.summary))
    return 0


if __name__ == '__main__':
    sys.exit(main())
