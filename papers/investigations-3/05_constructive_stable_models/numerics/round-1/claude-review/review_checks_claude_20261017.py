#!/usr/bin/env python3
"""Independent checks for the round-one cross-model review of Project 05.

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, reasoning effort max,
17 October 2026. The serving model may differ from the configured identifier.
Support computations for
papers/investigations-3/05_constructive_stable_models/reviews/
01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md.

Nothing here is imported from the round's programs. The routes differ where
an alternative exists: H_0 through the Riemann-Siegel Z function rather than
zeta; moments by quadrature of Phi rather than a Decimal cell sum; cumulants
and convolution coefficients by mpmath quadrature and numerical Taylor
expansion; the Chebyshev discriminant and the binomial envelope in exact or
high-precision arithmetic.

Sections
  A  SHA-256 digests of the committed round artifacts (needs --committed-dir)
  B  H_0 at the bracket endpoints and on a 61-point grid of the tripled
     interval, via mpmath.siegelz; comparison with the committed Acb balls
  C  theta moments by quadrature; the inherited enclosure; inequality (7)
  D  the two source finite differences and the Taylor coefficients of
     -log Phi(sqrt x)
  E  the two-quartic seed (cumulant, potential coefficients, its own
     third difference) and the X+Y/4 convolution coefficients
  F  exact Fraction checks: T9+cT5 and its discriminant; binomial envelope;
     Bessel transform identity; the interacting-pair example
  G  theta field growth constant; exact crossover fields for one quartic site
  H  reverse control: the stable Bessel seed exp(-2 pi cosh 4u) against the
     odd-dilation and field-growth obstructions (Acb signs when python-flint
     is installed)
  I  sub-Gaussian bound E exp(hS) <= exp(h^2 Var S / 2) on the two-quartic seed

Status: floating diagnostics (mpmath, 30-50 digits) except F (exact rational)
and the optional Acb enclosures in H. Agreement with the round's records is
evidence about implementation, not an independent certificate.
"""
import argparse
import hashlib
import json
import platform
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

try:
    import flint
    from flint import acb, arb, ctx
except ImportError:  # pragma: no cover
    flint = None

ARTIFACTS = [
    'notes/round-1/01_INDEPENDENT_SPIN_HEAT_FAMILY_AND_ODD_DILATION_OBSTRUCTION_CODEX_20261017.md',
    'notes/round-1/02_INTERACTING_FERROMAGNETS_AND_OTHER_STABLE_SEEDS_CODEX_20261017.md',
    'notes/round-1/03_FIELD_GROWTH_AND_QUARTIC_NETWORK_OBSTRUCTIONS_CODEX_20261017.md',
    'notes/round-1/README.md',
    'manuscript/constructive_stable_models.tex',
    'manuscript/constructive_stable_models.pdf',
    'manuscript/BUILD_RECORD.json',
    'numerics/round-1/certify_harmonic_obstruction.py',
    'numerics/round-1/certify_source_alternative_obstructions.py',
    'numerics/round-1/certify_two_quartic_seed.py',
    'numerics/round-1/certify_unequal_quartic_convolution.py',
    'numerics/round-1/HARMONIC_SIGN_CERTIFICATE.json',
    'numerics/round-1/SOURCE_ALTERNATIVE_OBSTRUCTIONS.json',
    'numerics/round-1/TWO_QUARTIC_SEED_CERTIFICATE.json',
    'numerics/round-1/UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json',
]


def s(x, n=15):
    return mp.nstr(x, n)


def phi(u, nmax=30):
    u = mp.mpmathify(u)
    return mp.fsum((2*mp.pi**2*n**4*mp.e**(9*u) - 3*mp.pi*n**2*mp.e**(5*u))
                   * mp.e**(-mp.pi*n**2*mp.e**(4*u)) for n in range(1, nmax+1))


def xi(z):
    if z == 1:  # removable singularity: xi(1) = 1/2
        return mp.mpf(1)/2
    return z*(z-1)*mp.pi**(-z/2)*mp.gamma(z/2)*mp.zeta(z)/2


def H0_rs(x):
    """H_0(x) = -(1/16)(x^2/4+1/4) pi^(-1/4) |Gamma(1/4+ix/4)| Z(x/2)."""
    x = mp.mpf(x)
    return -(x**2/4 + mp.mpf(1)/4)*mp.pi**(-mp.mpf(1)/4)*abs(mp.gamma(mp.mpf(1)/4 + 1j*x/4))*mp.siegelz(x/2)/16


def log_M_theta(h):
    h = mp.mpf(h)
    z = (1+h)/2
    return mp.log(xi(z)) - mp.log(xi(mp.mpf(1)/2))


def section_A(committed):
    if committed is None:
        return {'skipped': 'no --committed-dir'}
    root = Path(committed)
    out = {}
    for rel in ARTIFACTS:
        p = root/rel
        out[rel] = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else 'missing'
    rec = {}
    for name, key in [('HARMONIC_SIGN_CERTIFICATE.json', 'script_sha256'),
                      ('SOURCE_ALTERNATIVE_OBSTRUCTIONS.json', 'script_sha256'),
                      ('TWO_QUARTIC_SEED_CERTIFICATE.json', 'source_sha256'),
                      ('UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json', 'source_sha256')]:
        rec[name] = json.loads((root/'numerics/round-1'/name).read_text())[key]
    scripts = {'HARMONIC_SIGN_CERTIFICATE.json': 'certify_harmonic_obstruction.py',
               'SOURCE_ALTERNATIVE_OBSTRUCTIONS.json': 'certify_source_alternative_obstructions.py',
               'TWO_QUARTIC_SEED_CERTIFICATE.json': 'certify_two_quartic_seed.py',
               'UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json': 'certify_unequal_quartic_convolution.py'}
    out['record_script_hashes_match'] = {k: rec[k] == out['numerics/round-1/'+v] for k, v in scripts.items()}
    build = json.loads((root/'manuscript/BUILD_RECORD.json').read_text())
    out['build_record_hashes_match'] = {
        'tex': build['source_sha256'] == out['manuscript/constructive_stable_models.tex'],
        'pdf': build['pdf_sha256'] == out['manuscript/constructive_stable_models.pdf']}
    return out


def section_B(committed):
    mp.mp.dps = 40
    a, b = mp.mpf('28.26945'), mp.mpf('28.26946')
    grid = [3*a + k*(3*b - 3*a)/60 for k in range(61)]
    vals = [H0_rs(x) for x in grid]
    out = {'H0(a)': s(H0_rs(a), 20), 'H0(b)': s(H0_rs(b), 20),
           'H0_on_B_grid_min': s(min(vals), 20), 'H0_on_B_grid_max': s(max(vals), 20),
           'H0_prime_at_B_mid': s(mp.diff(H0_rs, (3*a+3*b)/2), 10),
           'width_B_times_H0_prime': s((3*b-3*a)*abs(mp.diff(H0_rs, (3*a+3*b)/2)), 6),
           'two_gamma_1': s(2*mp.zetazero(1).imag, 22),
           'H0(0)': s(H0_rs(0), 20),
           'delta_over_H0(0)': s(mp.mpf(36)/10**14/H0_rs(0), 6),
           'delta_over_min_abs_H0_on_B': s(mp.mpf(36)/10**14/abs(max(vals)), 6)}
    if committed is not None:
        rows = json.loads((Path(committed)/'numerics/round-1/HARMONIC_SIGN_CERTIFICATE.json').read_text())['rows']
        mids = [mp.mpf(r['real'].strip('[').split('+/-')[0]) for r in rows]
        out['relative_difference_to_committed_midpoints'] = [
            s(abs(H0_rs(a)/mids[0]-1), 3), s(abs(H0_rs(b)/mids[1]-1), 3),
            s(abs(H0_rs((3*a+3*b)/2)/mids[2]-1), 3)]
    return out


def section_C():
    mp.mp.dps = 40
    I = [mp.quad(lambda u: u**(2*k)*phi(u, 12), [0, 0.25, 0.5, 1, 2]) for k in range(4)]
    m2, m4, m6 = I[1]/I[0], I[2]/I[0], I[3]/I[0]
    return {'I0': s(I[0], 20), 'm2': s(m2, 15), 'm2_via_xi_second_derivative': s(mp.diff(xi, mp.mpf(1)/2, 2)/xi(mp.mpf(1)/2)/4, 15),
            'm4_over_m2sq': s(m4/m2**2, 15), 'inherited_enclosure_m2': ['0.01155234249', '0.01155265063'],
            'inherited_enclosure_kurtosis': ['2.79098616', '2.79121956'],
            'spin_count_bound_2_over_(3-kurt)': s(2/(3 - m4/m2**2), 15),
            'inequality_7_left_side': s(m2*m6 + 9*m2**2*m4 - 6*m2**4 - 4*m4**2, 10),
            'kappa4': s(m4 - 3*m2**2, 10)}


def section_D():
    mp.mp.dps = 50
    W = lambda x: -mp.log(phi(mp.sqrt(x)))
    R = lambda x: phi(mp.sqrt(x))*mp.e**(2*mp.pi*mp.cosh(4*mp.sqrt(x)))
    h3, h4 = mp.mpf(1)/100, mp.mpf(1)/1000
    d3 = W(3*h3) - 3*W(2*h3) + 3*W(h3) - W(0)
    d4 = R(4*h4) - 4*R(3*h4) + 6*R(2*h4) - 4*R(h4) + R(0)
    mp.mp.dps = 60
    wc = mp.taylor(lambda x: -mp.log(phi(mp.sqrt(x))), 0, 6, method='quad', radius=mp.mpf('0.05'))
    mp.mp.dps = 50
    return {'delta3_W_h=1/100': s(d3, 15), 'committed_delta3': '-0.00043499819129152038...',
            'delta4_R_h=1/1000': s(d4, 15), 'committed_delta4': '-5.2311893135780041...e-7',
            'quantitative_reading_delta3_over_8': s(abs(d3)/8, 6),
            'taylor_coefficients_of_-log_Phi(sqrt x)_x^0..6': [s(c.real, 12) for c in wc]}


def section_E():
    mp.mp.dps = 40
    w = lambda v: mp.e**(-2*(v**2 - mp.mpf(3)/2)**2)
    br = [0, 1, mp.sqrt(mp.mpf(3)/2), 1.5, 4]
    Z0 = mp.quad(w, br)
    mom = [mp.quad(lambda v: v**(2*k)*w(v), br)/Z0 for k in range(4)]
    k2 = mom[2] - mom[1]**2
    k3 = mom[3] - 3*mom[2]*mom[1] + 2*mom[1]**3

    def rho_two(z):
        z = mp.mpmathify(z)
        return mp.e**(-z**4/8 + 2*z**2)*mp.quad(lambda v: mp.e**(-2*v**4 + 6*v**2 - 3*z**2*v**2), [-4, -1.5, -1, 0, 1, 1.5, 4])

    def rho_conv(z, d=mp.mpf(1)/4):
        z = mp.mpmathify(z)
        return mp.quad(lambda y: mp.e**(-(z - d*y)**4 - y**4), [-6, -2, 0, 2, 6])

    h = mp.mpf(1)/100
    d3 = lambda f: f(3*h) - 3*f(2*h) + 3*f(h) - f(0)
    Wt = lambda x: -mp.log(rho_two(mp.sqrt(x)))
    Wc = lambda x: -mp.log(rho_conv(mp.sqrt(x)))
    conv = mp.taylor(lambda z: -mp.log(rho_conv(z)), 0, 6)
    r4 = mp.mpf(1)/256
    A = 1 + r4
    v = mp.gamma(mp.mpf(3)/4)/mp.gamma(mp.mpf(1)/4)
    s4f = (1 - mp.mpf(11)/2*r4 + r4**2 + 18*r4*v**2)/A**3
    s6f = 8*(mp.mpf(1)/4)**2*v/A**(mp.mpf(9)/2)*(-(1 - r4)**2 + 9*r4*v**2)
    return {'two_quartic': {'kappa3_W': s(k3, 15), 'committed_kappa3': '-0.005059254091980581...',
                            's2_coefficient': s(-2 + 3*mom[1], 12), 's4_coefficient': s(mp.mpf(1)/8 - mp.mpf(9)/2*k2, 12),
                            's6_coefficient': s(mp.mpf(9)/2*k3, 15),
                            'delta3_marginal_potential_h=1/100': s(d3(Wt), 12)},
            'X_plus_Y_over_4': {'taylor_s2': s(conv[2], 12), 'taylor_s4': s(conv[4], 12), 'taylor_s6': s(conv[6], 12),
                                'closed_form_s4': s(s4f, 12), 'closed_form_s6': s(s6f, 12),
                                'delta3_h=1/100': s(d3(Wc), 12)}}


def poly_mul(p, q):
    r = [0]*(len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def chebyshev(n):
    t0, t1 = [1], [0, 1]
    if n == 0:
        return t0
    for _ in range(n-1):
        t2 = [0]*(len(t1)+1)
        for i, c in enumerate(t1):
            t2[i+1] += 2*c
        for i, c in enumerate(t0):
            t2[i] -= c
        t0, t1 = t1, t2
    return t1


def quartic_disc(a, b, c, d, e):
    return (256*a**3*e**3 - 192*a**2*b*d*e**2 - 128*a**2*c**2*e**2 + 144*a**2*c*d**2*e
            - 27*a**2*d**4 + 144*a*b**2*c*e**2 - 6*a*b**2*d**2*e - 80*a*b*c**2*d*e
            + 18*a*b*c*d**3 + 16*a*c**4*e - 4*a*c**3*d**2 - 27*b**4*e**2 + 18*b**3*c*d*e
            - 4*b**3*d**3 - 4*b**2*c**3*e + b**2*c**2*d**2)


def section_F():
    out = {}
    T9, T5 = chebyshev(9), chebyshev(5)
    # (T9 + c T5)/x with y = x^2: coefficients in y for c-free and c parts
    base = [T9[2*k+1] for k in range(5)]
    cpart = [T5[2*k+1] if 2*k+1 < len(T5) else 0 for k in range(5)]
    claimed_base = [9, -120, 432, -576, 256]
    claimed_c = [5, -20, 16, 0, 0]
    out['p_c_matches_(T9+cT5)/x'] = base == claimed_base and cpart == claimed_c
    D = lambda sv: -575 - 1004*sv - 736*sv**2 - 472*sv**3 - 136*sv**4 - 20*sv**5
    agree = []
    for cval in [Fr(k, 3) for k in range(0, 25)]:
        coeffs = [Fr(base[k]) + cval*Fr(cpart[k]) for k in range(5)]  # y^0..y^4
        disc = quartic_disc(coeffs[4], coeffs[3], coeffs[2], coeffs[1], coeffs[0])
        agree.append(disc == 2**24*D(cval - 2))
    out['discriminant_equals_2^24_D(c)_at_25_rational_points'] = all(agree)
    # D(2+s)<0 for s>=0: all coefficients negative
    out['D(2+s)_coefficients_all_negative'] = True
    # binomial envelope
    mp.mp.dps = 40
    worst = mp.mpf('-inf')
    for N in range(2, 402, 2):
        lc = mp.log(mp.binomial(N, N//2))
        for r in range(0, N//2 + 1):
            M = 2*r
            lr = mp.log(mp.binomial(N, (N+M)//2)) - lc
            bound = -mp.mpf(M**2)/(2*(N+1)) - mp.mpf(M**2*(M**2-2))/(12*mp.mpf(N+1)**3)
            worst = max(worst, lr - bound)
    out['binomial_envelope_max_(lhs-rhs)_N<=400'] = s(worst, 6)
    bes = {}
    for z in [0, 3, 10]:
        lhs = mp.quad(lambda u: mp.e**(-2*mp.pi*mp.cosh(4*u))*mp.cos(z*u), [0, 0.5, 1, 2])
        rhs = mp.besselk(1j*mp.mpf(z)/4, 2*mp.pi).real/4
        bes[str(z)] = s(lhs/rhs - 1, 3)
    out['bessel_identity_relative_error'] = bes
    J = mp.log(3)/2
    z = mp.mpf('0.7')
    out['pair_example_identity_residual'] = s((2*mp.e**J*mp.cos(2*z) + 2*mp.e**(-J))/(2*mp.e**J + 2*mp.e**(-J)) - (mp.cos(2*z) + mp.mpf(1)/3)/(mp.mpf(4)/3), 3)
    out['cos(3 theta) at cos theta=-1/3'] = str(Fr(4)*Fr(-1, 3)**3 - 3*Fr(-1, 3))
    return out


def section_G():
    mp.mp.dps = 30
    asym = lambda h: (h/4)*mp.log(h) - (h/4)*(1 + mp.log(4*mp.pi)) + mp.mpf(7)/4*mp.log(h)
    growth = {str(h): s(log_M_theta(h) - asym(mp.mpf(h)), 10) for h in [10, 100, 1000, 10**4, 10**5]}
    den4 = mp.quad(lambda y: mp.e**(-y**4), [-mp.inf, 0, mp.inf])

    def logm(x):
        x = mp.mpf(x)
        if x == 0:
            return mp.mpf(0)
        p = (x/4)**(mp.mpf(1)/3)
        wdt = max(mp.mpf(1), 3/mp.sqrt(12*p**2))
        num = mp.quad(lambda y: mp.e**(-y**4 + x*y - (x*p - p**4)), [-mp.inf, p-6*wdt, p-wdt, p, p+wdt, p+6*wdt, mp.inf])
        return mp.log(num) + (x*p - p**4) - mp.log(den4)

    v1 = mp.gamma(mp.mpf(3)/4)/mp.gamma(mp.mpf(1)/4)
    m2 = mp.diff(xi, mp.mpf(1)/2, 2)/xi(mp.mpf(1)/2)/4
    cross = {}
    for ell in ['0.5', '0.25', '0.2', '0.18', '0.15', '0.1', '0.05']:
        e = mp.mpf(ell)
        if e**2*v1 > m2:
            cross[ell] = {'site_variance': s(e**2*v1, 6), 'crossover_field': '0+ (variance comparison)'}
            continue
        g = lambda h: logm(e*h) - log_M_theta(h)
        lo_h = None
        for k in range(-4, 44):
            h = mp.mpf(10)**(mp.mpf(k)/4)
            if g(h) > 0:
                hi_h = h
                break
            lo_h = h
        for _ in range(40):
            mid = (lo_h + hi_h)/2
            if g(mid) > 0:
                hi_h = mid
            else:
                lo_h = mid
        cross[ell] = {'site_variance': s(e**2*v1, 6), 'crossover_field': s(hi_h, 6)}
    return {'log_M_theta_minus_asymptotic': growth, 'unit_quartic_variance_v': s(v1, 12), 'theta_m2': s(m2, 12),
            'variance_threshold_readout_sqrt(m2/v)': s(mp.sqrt(m2/v1), 8), 'exact_crossover_fields': cross}


def section_H():
    mp.mp.dps = 40
    f = lambda z: mp.besselk(1j*mp.mpf(z)/4, 2*mp.pi).real
    zeros = []
    z, prev = mp.mpf('0.1'), f(mp.mpf('0.1'))
    while z < 125:
        z2 = z + mp.mpf(1)/20
        cur = f(z2)
        if prev*cur < 0:
            zeros.append(mp.findroot(f, (z, z2), solver='anderson'))
        z, prev = z2, cur
    rB = zeros[0]
    out = {'bessel_seed_real_zeros_below_125': [s(x, 12) for x in zeros], 'r_B': s(rB, 20),
           'value_at_3r_B': s(f(3*rB), 12), 'value_at_0': s(f(0), 12)}
    if flint is not None:
        ctx.prec = 160
        lo, hi = mp.nstr(rB - mp.mpf('1e-6'), 25), mp.nstr(rB + mp.mpf('1e-6'), 25)
        kb = lambda ball: acb(2*arb.pi()).bessel_k(acb(0, ball/4))
        ka, kb_, kt = kb(arb(lo)), kb(arb(hi)), kb(arb(mp.nstr(3*rB, 25), '3.1e-6'))
        sign = lambda x: 1 if x.real > 0 else (-1 if x.real < 0 else 0)
        out['acb_160_bits'] = {'K(r_B-1e-6)': ka.real.str(12, radius=True), 'K(r_B+1e-6)': kb_.real.str(12, radius=True),
                               'K(3(r_B +/- 1e-6)) ball': kt.real.str(12, radius=True),
                               'strict_signs': [sign(ka), sign(kb_), sign(kt)]}
    else:
        out['acb_160_bits'] = 'python-flint not installed; skipped'

    def logMB(h):
        h = mp.mpf(h)
        pk = mp.log(h/(8*mp.pi))/4 if h > 8*mp.pi else mp.mpf(0)
        num = mp.quad(lambda u: mp.e**(-2*mp.pi*mp.cosh(4*u))*mp.cosh(h*u), [0, max(pk-1, 0), pk, pk+0.5, pk+3])
        den = mp.quad(lambda u: mp.e**(-2*mp.pi*mp.cosh(4*u)), [0, 1, 3])
        return mp.log(num/den)
    out['bessel_seed_log_laplace'] = {str(h): {'logM_B': s(logMB(h), 10), 'h^(4/3)': s(mp.mpf(h)**(mp.mpf(4)/3), 8)}
                                      for h in [10, 100, 1000, 10000]}
    Bm = [mp.quad(lambda u: u**(2*k)*mp.e**(-2*mp.pi*mp.cosh(4*u)), [0, 0.5, 1, 2]) for k in range(3)]
    out['bessel_seed_m2'] = s(Bm[1]/Bm[0], 12)
    out['bessel_seed_kurtosis'] = s(Bm[2]*Bm[0]/Bm[1]**2, 12)
    return out


def section_I():
    mp.mp.dps = 20

    def rho(z):
        return mp.e**(-z**4/8 + 2*z**2)*mp.quad(lambda v: mp.e**(-2*v**4 + 6*v**2 - 3*z**2*v**2), [-4, -1.5, 0, 1.5, 4])
    nodes = [-6, -3, -2, 0, 2, 3, 6]
    Z = mp.quad(rho, nodes)
    var = mp.quad(lambda z: z**2*rho(z), nodes)/Z
    out = {'Var_S': s(var, 10)}
    for h in [0.5, 1, 2, 4]:
        lm = mp.log(mp.quad(lambda z: rho(z)*mp.e**(h*z), nodes)/Z)
        out[f'h={h}'] = {'log_E_exp_hS': s(lm, 10), 'Var*h^2/2': s(var*h**2/2, 10)}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--committed-dir', help='path to papers/investigations-3/05_constructive_stable_models')
    ap.add_argument('--sections', default='ABCDEFGHI')
    args = ap.parse_args()
    started = time.monotonic()
    rec = {'schema': 'project05_round1_claude_review_checks_v1', 'date': '2026-10-17',
           'prepared_for': 'Edward Baker', 'model': 'Claude Opus 5.5 (configured identifier claude-opus-5-5)',
           'reasoning_effort': 'max', 'status': 'floating diagnostics except section F (exact) and optional Acb signs in H',
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'python': platform.python_version(), 'mpmath': mp.__version__,
           'python_flint': getattr(flint, '__version__', None) if flint else None}
    table = {'A': lambda: section_A(args.committed_dir), 'B': lambda: section_B(args.committed_dir),
             'C': section_C, 'D': section_D, 'E': section_E, 'F': section_F, 'G': section_G,
             'H': section_H, 'I': section_I}
    for key in args.sections:
        rec[key] = table[key]()
    rec['runtime_seconds_not_part_of_content'] = round(time.monotonic() - started, 1)
    text = json.dumps(rec, indent=1, default=str) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        sys.stdout.write(text)


if __name__ == '__main__':
    main()
