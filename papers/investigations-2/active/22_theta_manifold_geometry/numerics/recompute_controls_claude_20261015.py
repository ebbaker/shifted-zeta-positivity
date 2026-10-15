#!/usr/bin/env python3
"""Independent recomputation of selected Investigation 22 claims.

15 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Fable 5.1 (claude-fable-5-1), Claude Cowork; the session's
configured identifier is claude-opus-5-5 and the serving model may differ.

This is a cross-check with a different library (mpmath, tanh-sinh quadrature
at 40-45 digits, no interval arithmetic) of numbers that the investigation
certifies with python-flint/Arb.  It is not a validated certificate; its value
is independence of code and method.  Companion to
reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md.

Recomputed
  A. Three-square weighted control (manuscript Prop. "Validated weighted-square
     control"; numerics/certify_square_support_endpoint_collision.py):
     Wronskian root x_* in [44.1303, 44.1304] at T=1/4, mixing theta, raw weights,
     double zero, H_xx, source endpoints, primitive endpoint.
  B. Four-square two-endpoint control (notes/05_control_families/03;
     numerics/check_theta_two_endpoint_control.py): Wronskian root in
     [83.5323729, 83.5323730] at T=1/100, q_*, raw weights, double zero, G_xx,
     Phi'(0)=Phi'''(0)=0, Phi^(5)(0), psi'(0).
  C. Positive-tail inequality (notes/03_theta_bundles_and_connections/10):
     -H_{n,x}/beta_n > x/[40(4 pi n^2-1)^2] on a grid n in {2,3,4},
     t in {0,1/4,1/2}, x in {1/2,5,15,30}.
  D. Source tail bound |W - W_N| <= B_j(T*) exp(-pi (N+1)^2/4) at one point.
  E. Fixed-endpoint chord limit on the heat polynomial x^2+2s.

Dependency: mpmath (pip install mpmath).  Runtime about three minutes.
Usage: python3 recompute_controls_claude_20261015.py [--output FILE]
"""
import argparse, hashlib, json, sys, time
from mpmath import mp, mpf, quad, exp, cos, sin, pi, findroot, diff, nsum, inf

mp.dps = 45
lam = lambda n: pi*n*n
beta = lambda n: (4*pi*n*n - 1)*exp(-pi*n*n)


def phi_n(n, u):
    q = exp(4*u); l = lam(n)
    return exp(u)*(2*l*l*q*q - 3*l*q)*exp(-l*q)


def H_n(n, t, x, j=0):
    """j-th x-derivative of int_0^inf e^{t u^2} phi_n(u) cos(xu) du."""
    def f(u):
        c = [cos(x*u), -u*sin(x*u), -u*u*cos(x*u), u**3*sin(x*u)][j]
        return exp(t*u*u)*phi_n(n, u)*c
    return quad(f, [0, 0.25, 0.5, 0.75, 1, 1.5, 2.5])


def s(v):
    return mp.nstr(v, 30)


def three_square():
    P1 = lambda a: -8*a**3 + 30*a**2 - 15*a
    d1, d2, d3 = P1(lam(1)), P1(lam(2)), P1(lam(3))
    b2, b3 = -d1/d2, -d1/d3
    T = mpf(1)/4
    G = lambda n, x, j=0: exp(lam(n))*H_n(n, T, x, j)
    A = lambda x, j=0: G(1, x, j) + b3*G(3, x, j)
    B = lambda x, j=0: b2*G(2, x, j) - b3*G(3, x, j)
    D = lambda x: A(x, 1)*B(x) - A(x)*B(x, 1)
    xl, xr = mpf('44.1303'), mpf('44.1304')
    Dl, Dr = D(xl), D(xr)
    xs = findroot(D, (xl, xr), solver='bisect', tol=mpf(10)**-36)
    theta = -A(xs)/B(xs)
    Gth = lambda x, j=0: G(1, x, j) + theta*b2*G(2, x, j) + (1-theta)*b3*G(3, x, j)
    raw = [mpf(1), theta*b2*exp(3*pi), (1-theta)*b3*exp(8*pi)]
    Phi = lambda u: sum(w*phi_n(n+1, u) for n, w in enumerate(raw))
    psi = lambda u: exp(u)*sum(w*exp(-lam(n+1)*exp(4*u)) for n, w in enumerate(raw))
    dpsi0 = diff(psi, 0)
    return dict(
        time='1/4', bracket=['44.1303', '44.1304'], D_left=s(Dl), D_right=s(Dr),
        sign_change=bool(Dl*Dr < 0), x_star=s(xs), theta=s(theta),
        raw_weights=[s(w) for w in raw], H_at_root=s(Gth(xs)), Hx_at_root=s(Gth(xs, 1)),
        Hxx_at_root=s(Gth(xs, 2)), source_derivative_at_0=s(diff(Phi, 0)),
        source_third_derivative_at_0=s(diff(Phi, 0, 3)), primitive_endpoint_raw=s(dpsi0),
        normalization_c=s(-1/(2*dpsi0)),
        source_positive_on_grid=all(Phi(mpf(k)/10) > 0 for k in range(0, 20)),
        manuscript_enclosures=dict(theta='(0.87916,0.87919)', Hxx='(-5.95,-5.65)e-6',
                                   third_derivative='(-40.00,-39.98)'),
    )


def four_square():
    P1 = lambda z: -8*z**3 + 30*z**2 - 15*z
    P3 = lambda z: -128*z**5 + 1440*z**4 - 4232*z**3 + 3270*z**2 - 375*z
    r = lambda n: P3(lam(n))/P1(lam(n))
    c = lambda n: -P1(lam(1))/P1(lam(n))
    eta = lambda n: (r(1) - r(2))/(r(n) - r(2))
    T = mpf(1)/100
    G = lambda n, x, j=0: exp(lam(n))*H_n(n, T, x, j)
    F = lambda n, x, j=0: G(1, x, j) + c(2)*(1 - eta(n))*G(2, x, j) + c(n)*eta(n)*G(n, x, j)
    D = lambda x: F(3, x, 1)*F(4, x) - F(3, x)*F(4, x, 1)
    xl, xr = mpf('83.5323729'), mpf('83.5323730')
    Dl, Dr = D(xl), D(xr)
    xs = findroot(D, (xl, xr), solver='bisect', tol=mpf(10)**-40)
    q = -F(4, xs)/(F(3, xs) - F(4, xs))
    Gm = lambda x, j=0: q*F(3, x, j) + (1 - q)*F(4, x, j)
    v = [mpf(1), c(2)*(1 - q*eta(3) - (1-q)*eta(4)), c(3)*q*eta(3), c(4)*(1-q)*eta(4)]
    a = [v[n]*exp(((n+1)**2 - 1)*pi) for n in range(4)]
    Phi = lambda u: sum(a[n]*phi_n(n+1, u) for n in range(4))
    psi = lambda u: exp(u)*sum(a[n]*exp(-lam(n+1)*exp(4*u)) for n in range(4))
    return dict(
        time='1/100', bracket=['83.5323729', '83.5323730'], D_left=s(Dl), D_right=s(Dr),
        sign_change=bool(Dl*Dr < 0), x_star=s(xs), q_star=s(q),
        r_values=[s(r(n)) for n in (1, 2, 3, 4)], eta_values=[s(eta(n)) for n in (3, 4)],
        raw_weights=[s(w) for w in a], G=s(Gm(xs)), Gx=s(Gm(xs, 1)), Gxx=s(Gm(xs, 2)),
        Phi1_0=s(diff(Phi, 0, 1)), Phi3_0=s(diff(Phi, 0, 3)), Phi5_0=s(diff(Phi, 0, 5)),
        psi1_0=s(diff(psi, 0, 1)),
        source_positive_on_grid=all(Phi(mpf(k)/8) > 0 for k in range(0, 24)),
        note_enclosures=dict(q_star='(0.8377475051,0.8377475108)', Gxx='(6.1408328,6.1408349)e-12',
                             Phi5_0='-2.65684411198 +/- 8e-8', psi1_0='-0.500000000034843223'),
    )


def positive_tail():
    worst = None; viol = []
    for n in (2, 3, 4):
        for t in (mpf(0), mpf('0.25'), mpf('0.5')):
            for x in (mpf('0.5'), mpf(5), mpf(15), mpf(30)):
                lhs = -H_n(n, t, x, 1)/beta(n)
                rhs = x/(40*(4*pi*n*n - 1)**2)
                if lhs <= rhs:
                    viol.append(dict(n=n, t=s(t), x=s(x), lhs=s(lhs), rhs=s(rhs)))
                ratio = lhs/rhs
                if worst is None or ratio < worst[0]:
                    worst = (ratio, n, t, x, lhs, rhs)
    return dict(grid='n in {2,3,4}; t in {0,1/4,1/2}; x in {1/2,5,15,30}',
                min_ratio_lhs_over_rhs=s(worst[0]), at=dict(n=worst[1], t=s(worst[2]), x=s(worst[3])),
                violations=viol)


def tail_bound():
    mp.dps = 30
    def Phi(u, N=None):
        tot = mpf(0); n = 1
        while True:
            if N is not None and n > N:
                break
            term = phi_n(n, u); tot += term
            if N is None and n > 3 and abs(term) < mpf(10)**(-mp.dps):
                break
            n += 1
        return tot
    Tstar, N, t, x = mpf('0.5'), 1, mpf('0.5'), mpf(3)
    B0 = 2*pi**2*nsum(lambda n: n**4*exp(-pi*n*n/4), [1, inf])*quad(
        lambda u: exp(Tstar*u*u + 9*u - (pi/2)*exp(4*u)), [0, 1, 3])
    W = quad(lambda u: exp(t*u*u)*Phi(u)*cos(x*u), [0, 1, 2.5])
    WN = quad(lambda u: exp(t*u*u)*Phi(u, N)*cos(x*u), [0, 1, 2.5])
    out = dict(N=N, t=s(t), x=s(x), actual_difference=s(abs(W - WN)),
               bound=s(B0*exp(-pi*(N+1)**2/4)), B0=s(B0), holds=bool(abs(W-WN) <= B0*exp(-pi*(N+1)**2/4)))
    mp.dps = 45
    return out


def chord_limit():
    res = []
    d = mpf('0.3')
    for sv in (mpf('0.1'), mpf('0.01'), mpf('0.001')):
        W0, Wd, Wxd = 2*sv, d*d + 2*sv, 2*d
        res.append(dict(s=s(sv), C0_over_sqrtE=s(W0*(Wd - Wxd)/(2*sv)), limit=s(-(2*d - d*d))))
    return dict(field='W(T-s,x)=x^2+2s, predecessor x=0, delta=0.3', values=res)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output')
    args = ap.parse_args()
    t0 = time.time()
    rec = dict(
        date='2026-10-15', prepared_for='Edward Baker',
        model='Claude Fable 5.1 (claude-fable-5-1); configured identifier claude-opus-5-5',
        library='mpmath', mp_dps=45,
        script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
        three_square_control=three_square(),
        four_square_control=four_square(),
        positive_tail_inequality=positive_tail(),
        source_tail_bound=tail_bound(),
        chord_limit=chord_limit(),
    )
    rec['elapsed_seconds'] = round(time.time() - t0, 1)
    rec['scope'] = ('Floating-point cross-check of certified numbers by an independent method; '
                    'agreement to the displayed digits supports the certificates but does not '
                    'replace them. Nothing here concerns the actual theta sign estimate.')
    text = json.dumps(rec, indent=1)
    if args.output:
        open(args.output, 'w').write(text + '\n')
    print(text)


if __name__ == '__main__':
    main()
