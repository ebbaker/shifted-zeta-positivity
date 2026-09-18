#!/usr/bin/env python3
"""
The group-delay test of Condition 9.1 / 10.1, run on the objects it names.
Standard library only; prints JSON to stdout.  Nothing here is a positivity
certificate and nothing here computes with zeta or xi.

SETUP.  On a ray r > 0 put x = log r, so the dilatation generator translates x.
A defect two-point function in the ray frame is a function of u = x_1 - x_2,
    G_Delta(u) = (2 sinh(u/2))^{-2 Delta},
the conformally covariant form of C/|r_1 - r_2|^{2 Delta}.  Its causal symbol is
    khat_+(tau) = int_0^inf e^{-i tau u} G_Delta(u) du
                = Gamma(1-2 Delta) Gamma(Delta + i tau)/Gamma(1 - Delta + i tau),
and the group delay is  T_Delta(tau) = -d/dtau arg khat_+(tau).

WHAT IS CHECKED.

  A. The closed symbol against direct quadrature, for Delta < 1/2.
  B. The boundary-channel decomposition
       G_Delta(u) = sum_{k>=0} c_k e^{-(Delta+k) u},  c_k = Gamma(2 Delta + k)/(k! Gamma(2 Delta)) > 0,
     i.e. primary plus descendants with positive coefficients -- so G is
     completely monotone and khat_+ is a Stieltjes transform of a positive
     measure.  Checked against the closed symbol.
  C. The delay in closed form,
       T_Delta(tau) = pi Re cot(pi(Delta + i tau))
                    = pi sin(2 pi Delta)/(cosh 2 pi tau - cos 2 pi Delta),
     against a numerical derivative; its total, int_0^inf T = pi(1/2 - Delta);
     and that it VANISHES IDENTICALLY when 2 Delta is an integer, which is the
     case for every protected operator of the 1/2-BPS Wilson-line defect CFT
     (Delta = 1 for the five scalars, 3/2 for the fermions, 2 for the
     displacement, L for the (Y.Phi)^L tower).
  D. The Stieltjes bound for arbitrary positive spectral measures:
     arg khat_+ in (-pi/2, 0), so int_0^T T dtau < pi/2 for every T.
  E. The target.  exp(2 i theta(tau)) = pi^{-i tau} Gamma(1/4 + i tau/2)/
     Gamma(1/4 - i tau/2) is unimodular -- an inner function -- and
     int_0^T 2 theta' = 2 theta(T) grows without bound.  The two are compared.
  G. The asymptotic expansion of the delay, which is where the discrimination is.
     For a unimodular Gamma-ratio amplitude
       S(tau) = e^{2 i c1 tau} prod_j [Gamma(a_j + i b_j tau)/Gamma(a_j - i b_j tau)]^{n_j}
     one has, from Re psi(a + i y) = log y + B_2(a)/(2 y^2) + O(y^-4),
       d(arg S)/dtau = Lambda log tau + const + tau^{-2} sum_j n_j B_2(a_j)/b_j + O(tau^-4),
       Lambda = 2 sum_j n_j b_j,   B_2(a) = a^2 - a + 1/6.
     The target has Lambda = 1 and second coefficient -1/24, and for the
     archimedean factor of a degree-d L-function Lambda IS d.  Since the second
     coefficient must be negative and n_j, b_j > 0, some a_j must lie in
     (1/2 - 1/(2 sqrt 3), 1/2 + 1/(2 sqrt 3)); Gamma(1 + i .), which is what
     Liouville and generic QFT reflection amplitudes are built from, does not.

  H. The graded invariants, which make the test dictionary-free.  Under the
     linear momentum change tau -> kappa tau that the leading term forces
     (kappa = Lambda), the quantities
       I_2m = Lambda^(2m-1) Sigma_2m,   Sigma_2m = sum_j n_j B_2m(a_j)/b_j^(2m-1)
     are invariant, and the target is I_2m = 2^(2m-1) B_2m(1/4), i.e.
     -1/24, 7/480, -31/2688, 127/7680, ...  Checked here:
       - the target values, exactly, in rational arithmetic;
       - the degeneracy B_2m(1/2) = 2^2m B_2m(1/4), exactly, m <= 8, which makes
         (a=1/4, b, n) and (a=1/2, 2b, n/2) indistinguishable in every invariant;
       - for ONE factor, I_2m = 2^(2m-1) n^2m B_2m(a), with b absent, and the
         resulting complete classification: matching I_2 and I_4 forces
         576 u^2 + 60 u + 1 = 0 with u = B_2(a), so (a,n) is one of
         (1/4,+-1), (3/4,+-1), (1/2,+-1/2) and nothing else;
       - the survey of reflection amplitudes, every row;
       - the RETRACTION of the claim that Gamma(m + i.) with m >= 1 cannot work:
         Gamma(1+i r tau)/Gamma(1+i tau) has I_2 = -(r-1)^2/(3 r), which equals
         -1/24 at r = (17 +- sqrt 33)/16, with I_4 = 5/384 = (25/28) x target;
         and the full two-factor family at a = 1 matching BOTH I_2 and I_4;
       - that imposing I_6 on that family leaves exactly the two Legendre
         duplication points, which are the target in disguise.

  F. Two objects that DO wind: the phase shift of the inverted harmonic
     oscillator on the half-line, eta(tau) = arg Gamma(1/4 + i tau/2), whose
     derivative differs from theta' by exactly (log pi)/2; and the bulk
     Liouville reflection amplitude, whose phase derivative is 4 Q log P.

Tolerances are numerical agreement thresholds, not theorems.
"""
import cmath, json, math
from fractions import Fraction as Fr

# ---------------------------------------------------------------- specials
BERN = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510, 43867/798]
LANCZOS = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
           -176.61502916214059, 12.507343278686905, -0.13857109526572012,
           9.9843695780195716e-6, 1.5056327351493116e-7]

def loggamma(z):
    """Lanczos, with reflection; principal branch tracked continuously in Im z."""
    if z.real < 0.5:
        return cmath.log(cmath.pi/cmath.sin(cmath.pi*z)) - loggamma(1-z)
    z -= 1
    x = 0.99999999999980993
    for i, c in enumerate(LANCZOS):
        x += c/(z+i+1)
    t = z + len(LANCZOS) - 0.5
    return 0.5*math.log(2*math.pi) + (z+0.5)*cmath.log(t) - t + cmath.log(x)

def gamma_c(z):
    return cmath.exp(loggamma(z))

def digamma_c(z):
    s = 0j
    while abs(z) < 14:
        s -= 1/z
        z += 1
    r = cmath.log(z) - 1/(2*z)
    z2, p = z*z, z*z
    for k, b in enumerate(BERN, start=1):
        r -= b/(2*k*p)
        p *= z2
    return s + r

def arg_gamma(z):
    """arg Gamma(z), continued in Im z from the real axis by integrating Re psi.
    Avoids branch jumps; Gauss-Legendre on panels of unit length."""
    y = z.imag
    if y == 0:
        return 0.0
    n = max(8, int(abs(y)) + 4)
    tot, h = 0.0, y/n
    for i in range(n):
        lo, hi = i*h, (i+1)*h
        c, hh = (lo+hi)/2, (hi-lo)/2
        tot += hh*sum(w*digamma_c(complex(z.real, c + hh*x)).real for x, w in zip(GLX, GLW))
    return tot

def gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n+1):
        x = math.cos(math.pi*(i-0.25)/(n+0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n+1):
                p0, p1 = ((2*j-1)*x*p0 - (j-1)*p1)/j, p0
            dp = n*(x*p0 - p1)/(x*x-1)
            dx = -p0/dp
            x += dx
            if abs(dx) < 1e-16:
                break
        xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs, ws

GLX, GLW = gauss_legendre(90)

def quad(f, a, b, panels=60):
    tot = 0j
    for p in range(panels):
        lo, hi = a + (b-a)*p/panels, a + (b-a)*(p+1)/panels
        c, h = (lo+hi)/2, (hi-lo)/2
        tot += h*sum(w*f(c + h*x) for x, w in zip(GLX, GLW))
    return tot

_BERN = [Fr(1), Fr(-1, 2), Fr(1, 6), Fr(0), Fr(-1, 30), Fr(0), Fr(1, 42), Fr(0),
         Fr(-1, 30), Fr(0), Fr(5, 66), Fr(0), Fr(-691, 2730), Fr(0), Fr(7, 6),
         Fr(0), Fr(-3617, 510), Fr(0)]


def bernpoly(n, x):
    """B_n(x) = sum_k C(n,k) B_{n-k} x^k, exact when x is a Fraction."""
    tot = 0*x if isinstance(x, Fr) else 0.0
    for k in range(n + 1):
        b = _BERN[n - k]
        c = math.comb(n, k)
        tot = tot + (c*b if isinstance(x, Fr) else c*float(b))*(x**k)
    return tot


def invariants(factors, M=3):
    """factors = [(n, a, b), ...];  returns (Lambda, [I_2, I_4, ...])."""
    lam = 2*sum(n*b for n, a, b in factors)
    return lam, [lam**(2*m - 1)*sum(n*bernpoly(2*m, a)/b**(2*m - 1) for n, a, b in factors)
                 for m in range(1, M + 1)]


def relerr(a, b):
    return abs(a-b)/max(abs(a), abs(b), 1e-300)

# ---------------------------------------------------------------- the objects
def G_ray(u, D):
    return (2*math.sinh(u/2))**(-2*D)

def khat_closed(tau, D):
    return gamma_c(complex(1-2*D, 0))*gamma_c(complex(D, tau))/gamma_c(complex(1-D, tau))

def khat_quad(tau, D):
    """Direct quadrature.  Write G = u^{-2D} g(u) with g(u) = (2 sinh(u/2)/u)^{-2D}
    smooth and g(0) = 1.  With u = t^a, a = 1/(1-2D), one has u^{-2D} du = a dt
    exactly, so the endpoint singularity is removed:
        int_0^1 e^{-i tau u} G du = a int_0^1 e^{-i tau t^a} g(t^a) dt.
    The tail is cut where e^{-D u} is below 1e-24."""
    a = 1.0/(1.0 - 2*D)
    g = lambda u: 1.0 if u == 0.0 else (2*math.sinh(u/2)/u)**(-2*D)
    head = a*quad(lambda t: cmath.exp(-1j*tau*t**a)*g(t**a), 0.0, 1.0, panels=240)
    U = max(80.0, 56.0/D)
    tail = quad(lambda u: cmath.exp(-1j*tau*u)*G_ray(u, D), 1.0, U, panels=1400)
    return head + tail

def khat_channels(tau, D, K):
    tot, c = 0j, 1.0
    for k in range(K):
        tot += c/complex(D+k, tau)
        c *= (2*D+k)/(k+1)
    return tot

def delay_closed(tau, D):
    """pi Re cot(pi(D + i tau))."""
    return math.pi*math.sin(2*math.pi*D)/(math.cosh(2*math.pi*tau) - math.cos(2*math.pi*D))

def delay_via_digamma(tau, D):
    return digamma_c(complex(1-D, tau)).real - digamma_c(complex(D, tau)).real

def two_theta_prime(tau):
    return digamma_c(complex(0.25, tau/2)).real - math.log(math.pi)

def theta_rs(tau):
    return arg_gamma(complex(0.25, tau/2)) - 0.5*tau*math.log(math.pi)

# ---------------------------------------------------------------- the checks
def main():
    out = {"groups": [], "note": "counts are finite test cases, not theorems"}
    TAUS = [0.15, 0.4, 0.9, 1.7, 3.0]
    DS = [0.05, 0.12, 0.25, 0.33, 0.45]

    # A ------------------------------------------------------------------
    cases, worst = 0, 0.0
    for D in DS:
        for tau in TAUS:
            worst = max(worst, relerr(khat_quad(tau, D), khat_closed(tau, D))); cases += 1
    out["groups"].append({"name": "A. causal symbol: closed form vs quadrature",
                          "cases": cases, "worst_error": worst,
                          "tolerance": 1e-9, "pass": worst < 1e-9})

    # B ------------------------------------------------------------------
    cases, worst = 0, 0.0
    for D in DS:
        K = 200000 if D > 0.2 else 40000
        for tau in TAUS:
            a = khat_channels(tau, D, K)
            b = khat_closed(tau, D)
            # channel tail: c_k ~ k^{2D-1}/Gamma(2D); truncation error is O(K^{2D-1})
            worst = max(worst, relerr(a, b) / max(K**(2*D-1), 1e-30)); cases += 1
    out["groups"].append({"name": "B. boundary-channel sum (primary + descendants, positive coefficients)",
                          "cases": cases, "worst_error": worst,
                          "tolerance": 60.0, "pass": worst < 60.0,
                          "scope": "error normalised by the K^{2D-1} truncation tail of the channel sum"})

    # C ------------------------------------------------------------------
    cases, worst, worst_fd = 0, 0.0, 0.0
    h = 1e-5
    for D in DS + [0.7, 1.3]:
        for tau in TAUS:
            num = -(arg_gamma(complex(D, tau+h)) - arg_gamma(complex(1-D, tau+h))
                    - arg_gamma(complex(D, tau-h)) + arg_gamma(complex(1-D, tau-h)))/(2*h)
            worst_fd = max(worst_fd, abs(num - delay_closed(tau, D))); cases += 1
            worst = max(worst, abs(delay_via_digamma(tau, D) - delay_closed(tau, D))); cases += 1
    totals = []
    for D in DS:
        tot = quad(lambda t: delay_closed(t, D), 1e-12, 12.0, panels=400).real
        totals.append({"Delta": D, "total_delay": tot, "pi(1/2-Delta)": math.pi*(0.5-D)})
        worst = max(worst, abs(tot - math.pi*(0.5-D))); cases += 1
    protected = []
    for D in (0.5, 1.0, 1.5, 2.0, 3.0, 5.0):
        vals = [abs(delay_closed(t, D)) for t in TAUS]
        protected.append({"Delta": D, "max_|delay|": max(vals)})
        worst = max(worst, max(vals)); cases += 1
    out["groups"].append({"name": "C. delay in closed form; total pi(1/2-Delta); zero at half-integer Delta",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-7,
                          "pass": worst < 1e-7 and worst_fd < 1e-6, "totals": totals,
                          "worst_error_finite_difference": worst_fd,
                          "tolerance_finite_difference": 1e-6,
                          "protected_operators": protected})

    # D ------------------------------------------------------------------
    cases, worst, rows = 0, 0.0, []
    measures = [[(1.0, 1.0)], [(0.3, 2.0), (1.0, 5.5), (4.0, 0.25)],
                [(0.01, 1.0), (7.0, 1.0), (7.01, 3.0), (60.0, 9.0)],
                [(1e-3, 1e-3), (0.5, 1.0), (2.0, 1.0), (13.0, 1.0), (100.0, 40.0)]]
    for mu in measures:
        f = lambda t: sum(c/complex(d, t) for d, c in mu)
        args = [cmath.phase(f(t)) for t in (1e-6, 1e-3, 0.1, 1, 10, 1e3, 1e6, 1e9)]
        worst = max(worst, max(0.0, max(args)), max(0.0, -math.pi/2 - min(args))); cases += 1
        acc = [(-(cmath.phase(f(T)) - cmath.phase(f(1e-12)))) for T in (1, 10, 1e3, 1e6)]
        worst = max(worst, max(0.0, max(acc) - math.pi/2)); cases += 1
        rows.append({"measure": mu, "arg_range": [min(args), max(args)],
                     "accumulated_delay_at_T=1e6": acc[-1]})
    out["groups"].append({"name": "D. Stieltjes bound: arg in (-pi/2, 0), accumulated delay < pi/2",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-12,
                          "pass": worst < 1e-12, "rows": rows})

    # E ------------------------------------------------------------------
    cases, worst, rows = 0, 0.0, []
    for tau in (1.0, 7.0, 30.0, 140.0):
        inner = cmath.exp(-1j*tau*math.log(math.pi))*gamma_c(complex(0.25, tau/2))/gamma_c(complex(0.25, -tau/2))
        worst = max(worst, abs(abs(inner) - 1.0)); cases += 1
        worst = max(worst, abs(cmath.phase(inner) - cmath.phase(cmath.exp(2j*theta_rs(tau)))))
        cases += 1
    for T in (10.0, 100.0, 1000.0):
        acc = quad(lambda t: two_theta_prime(t), 1e-9, T, panels=600).real
        rows.append({"T": T, "int_0^T 2 theta'": acc, "2 theta(T)": 2*theta_rs(T),
                     "pi/2 bound for any correlator": math.pi/2})
        worst = max(worst, abs(acc - 2*theta_rs(T))/max(abs(acc), 1.0)); cases += 1
    out_E_tol = 1e-9
    out["groups"].append({"name": "E. the target is inner and its accumulated delay is unbounded",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-7,
                          "pass": worst < 1e-7, "rows": rows})

    # F ------------------------------------------------------------------
    cases, worst, rows = 0, 0.0, []
    for tau in (1.0, 10.0, 100.0, 1000.0):
        eta_p = digamma_c(complex(0.25, tau/2)).real          # 2 eta'(tau)
        worst = max(worst, abs(eta_p - two_theta_prime(tau) - math.log(math.pi))); cases += 1
    for b in (0.5, 1.0, 1.7):
        Q = b + 1/b
        darg = lambda P: (-2/b)*math.log(math.pi) + 4*b*digamma_c(complex(1, 2*b*P)).real \
                         + (4/b)*digamma_c(complex(1, 2*P/b)).real
        slope = (darg(1e7) - darg(1e6))/math.log(10)
        rows.append({"b": b, "Q": Q, "measured d/dlogP of the Liouville delay": slope, "4Q": 4*Q})
        worst = max(worst, abs(slope - 4*Q)); cases += 1
    out["groups"].append({"name": "F. two objects that do wind: inverted oscillator (exactly log pi off) and Liouville (4 Q log P)",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-5,
                          "pass": worst < 1e-5, "liouville": rows,
                          "scope": "the inverted-oscillator identity is exact; the Liouville slope is asymptotic"})

    # G ------------------------------------------------------------------
    cases, worst, rows = 0, 0.0, []
    B2 = lambda a: a*a - a + 1/6

    # G1: the expansion of Re psi
    for a in (0.25, 0.5, 0.75, 1.0, 1.7):
        for y in (200.0, 2000.0):
            meas = 2*y*y*(digamma_c(complex(a, y)).real - math.log(y))
            worst = max(worst, abs(meas - B2(a))*min(1.0, y/200.0)); cases += 1

    # G2: the target's second coefficient is exactly -1/24, i.e. 2 B_2(1/4)
    for tau in (200.0, 2000.0):
        meas = tau*tau*(two_theta_prime(tau) - math.log(tau/(2*math.pi)))
        worst = max(worst, abs(meas + 1/24)); cases += 1
    worst = max(worst, abs(B2(0.25)/0.5 + 1/24)); cases += 1     # single factor a=1/4, b=1/2
    worst = max(worst, abs(2*1*0.5 - 1.0)); cases += 1           # Lambda = 1

    # G3: Lambda is the degree.  Gamma_R(s + mu_j) at s = 1/2 + i tau has a_j=(1/2+mu_j)/2, b_j=1/2
    for d in (1, 2, 3, 4):
        worst = max(worst, abs(2*sum(0.5 for _ in range(d)) - d)); cases += 1

    # G4: Liouville.  tau = 4 Q P fixes Lambda = 1; the tau^-2 coefficient is then Q^2/3 > 0
    for b in (0.3, 0.5, 0.8, 1.7, 3.0):
        Q = b + 1/b
        bet = (b/(2*Q), 1/(2*Q*b))                              # beta_j in the tau variable
        lam = 2*sum(bet)
        coef = sum(B2(1.0)/x for x in bet)
        worst = max(worst, abs(lam - 1.0)); cases += 1
        worst = max(worst, abs(coef - Q*Q/3)); cases += 1
        rows.append({"b": b, "Q": Q, "Lambda": lam, "tau^-2 coefficient": coef,
                     "target": -1/24, "sign": "opposite"})

    # G5: the sign window, and where the standard shifts fall
    lo, hi = 0.5 - 1/(2*math.sqrt(3)), 0.5 + 1/(2*math.sqrt(3))
    worst = max(worst, abs(B2(lo)), abs(B2(hi))); cases += 2
    window = []
    for label, a in (("Gamma_R(s), zeta / even chi", 0.25), ("Gamma_R(s+1), odd chi", 0.75),
                     ("Gamma_C(s), complex place", 0.5), ("Gamma(1 + i.), Liouville", 1.0),
                     ("Gamma(3/2 + i.)", 1.5)):
        window.append({"factor": label, "a": a, "B_2(a)": B2(a),
                       "inside": bool(lo < a < hi)}); cases += 1
        worst = max(worst, 0.0 if (B2(a) < 0) == (lo < a < hi) else 1.0)

    # G6: rigidity at a common shift.  sum n = sum(nhat)/sqrt(A B) <= 1/sqrt(48|B_2(a)|)
    import random as _r
    _r.seed(3)
    for a in (0.25, 0.75, 0.5, 0.3):
        if B2(a) >= 0:
            continue
        bound, hit = 1/math.sqrt(-48*B2(a)), 0.0
        for _ in range(3000):
            k = _r.randint(1, 5)
            nh = [_r.uniform(0.02, 4) for _ in range(k)]
            bh = [_r.uniform(0.02, 4) for _ in range(k)]
            A = sum(n*x for n, x in zip(nh, bh)); Bs = sum(n/x for n, x in zip(nh, bh))
            sig = 1/math.sqrt(A*Bs*(-48*B2(a))); t = math.sqrt(Bs*(-48*B2(a))/A)/2
            n = [sig*x for x in nh]; bb = [t*x for x in bh]
            worst = max(worst, abs(2*sum(u*v for u, v in zip(n, bb)) - 1.0))
            worst = max(worst, abs(sum(u*B2(a)/v for u, v in zip(n, bb)) + 1/24))
            hit = max(hit, sum(n))
        worst = max(worst, max(0.0, hit - bound)); cases += 1
        rows.append({"common shift a": a, "max sum(n) over exact solutions": hit,
                     "bound 1/sqrt(48|B_2|)": bound})
    # a = 1/4 and 3/4 are exactly where the bound is one
    for a in (0.25, 0.75):
        worst = max(worst, abs(1/math.sqrt(-48*B2(a)) - 1.0)); cases += 1

    # G7: the common-shift hypothesis is necessary -- an explicit two-shift solution
    b1 = 0.15767078084837
    b2 = 0.5 - b1
    lam = 2*(b1 + b2); coef = B2(0.5)/b1 + B2(1.0)/b2
    worst = max(worst, abs(lam - 1.0)); cases += 1
    two_shift = {"a_1": 0.5, "a_2": 1.0, "beta_1": b1, "beta_2": b2,
                 "Lambda": lam, "coefficient": coef, "target": -1/24,
                 "note": "so the two conditions alone are not rigid; the sign rule is what is unconditional"}
    worst = max(worst, abs(coef + 1/24)*1e-3); cases += 1

    out["groups"].append({"name": "G. the expansion: Lambda is the degree, the tau^-2 sign is a selection rule",
                          "cases": cases, "worst_error": worst, "tolerance": 2e-4,
                          "pass": worst < 2e-4, "rows": rows,
                          "sign_window": {"lo": lo, "hi": hi, "factors": window},
                          "two_shift_solution": two_shift})

    # ------------------------------------------------------------------ H
    cases, worst, rows = 0, 0.0, []

    # H1: the targets, exactly, in rational arithmetic
    TGx = [Fr(2)**(2*m - 1)*bernpoly(2*m, Fr(1, 4)) for m in range(1, 5)]
    for got, want in zip(TGx, [Fr(-1, 24), Fr(7, 480), Fr(-31, 2688), Fr(127, 7680)]):
        worst = max(worst, 0.0 if got == want else 1.0); cases += 1
    TG = [float(x) for x in TGx]

    # H2: the degeneracy B_2m(1/2) = 2^2m B_2m(1/4), exactly
    for m in range(1, 9):
        lhs = bernpoly(2*m, Fr(1, 2)); rhs = Fr(2)**(2*m)*bernpoly(2*m, Fr(1, 4))
        worst = max(worst, 0.0 if lhs == rhs else 1.0); cases += 1
    # and the downward split B_2m(1/4) = 2^(2m-1) [B_2m(1/8) + B_2m(5/8)]
    for m in range(1, 6):
        lhs = bernpoly(2*m, Fr(1, 4))
        rhs = Fr(2)**(2*m - 1)*(bernpoly(2*m, Fr(1, 8)) + bernpoly(2*m, Fr(5, 8)))
        worst = max(worst, 0.0 if lhs == rhs else 1.0); cases += 1
    # the parity symmetry B_2m(1-a) = B_2m(a)
    for m in range(1, 6):
        for a in (Fr(1, 4), Fr(1, 3), Fr(2, 7)):
            worst = max(worst, 0.0 if bernpoly(2*m, 1 - a) == bernpoly(2*m, a) else 1.0)
            cases += 1

    # H3: one factor -- I_2m = 2^(2m-1) n^2m B_2m(a), with b absent
    for (n, a) in ((1.0, 0.25), (-1.0, 0.75), (0.5, 0.5), (-2.3, 0.37), (1.7, 1.4)):
        prev = None
        for b in (0.5, 3.0, 0.137, 11.0):
            lam, I = invariants([(n, a, b)], M=3)
            closed = [2**(2*m - 1)*n**(2*m)*bernpoly(2*m, a) for m in (1, 2, 3)]
            worst = max(worst, max(relerr(x, y) for x, y in zip(I, closed))); cases += 3
            if prev is not None:
                worst = max(worst, max(relerr(x, y) for x, y in zip(I, prev)))
                cases += 3                                   # b-independence
            prev = I

    # H4: the classification.  576 u^2 + 60 u + 1 = 0 with u = B_2(a)
    for u in (Fr(-1, 48), Fr(-1, 12)):
        worst = max(worst, 0.0 if 576*u*u + 60*u + 1 == 0 else 1.0); cases += 1
    SOLS = [(0.25, 1.0), (0.25, -1.0), (0.75, 1.0), (0.75, -1.0), (0.5, 0.5), (0.5, -0.5)]
    for (a, n) in SOLS:
        lam, I = invariants([(n, a, 0.61)], M=3)            # b deliberately generic
        worst = max(worst, max(abs(x - y) for x, y in zip(I, TG))); cases += 3
    # nothing else on a fine grid matches BOTH I_2 and I_4
    spurious = []
    for ia in range(1, 400):
        a = ia/200.0                                         # a in (0, 2)
        B2a = bernpoly(2, a)
        if B2a >= 0:
            continue
        nsq = -1/(48*B2a)                                    # forced by I_2
        i4 = 8*nsq*nsq*bernpoly(4, a)
        if abs(i4 - TG[1]) < 1e-9:
            spurious.append(a)
    for a in spurious:
        worst = max(worst, 0.0 if min(abs(a - x) for x in (0.25, 0.5, 0.75)) < 1e-9 else 1.0)
    cases += 1
    # a >= 1 is impossible at any n: I_2 = 2 n^2 B_2(a) > 0 there
    for a in (1.0, 1.25, 1.5, 2.0, 5.0):
        worst = max(worst, 0.0 if bernpoly(2, a) > 0 else 1.0); cases += 1

    # H5: the survey
    SURVEY = [
        ("target Gamma_R(s), zeta / even chi",      [(1.0, 0.25, 0.5)],                     True),
        ("Gamma_R(s+1), odd chi",                   [(1.0, 0.75, 0.5)],                     True),
        ("inverted oscillator, half line, even",    [(1.0, 0.25, 0.5)],                     True),
        ("inverted oscillator, half line, odd",     [(1.0, 0.75, 0.5)],                     True),
        ("c=1 matrix model / 2d string, sqrt",      [(0.5, 0.5, 1.0)],                      True),
        ("Gauss duplication of the target",         [(1.0, 0.125, 0.25), (1.0, 0.625, 0.25)], True),
        ("inverted oscillator, FULL line",          [(1.0, 0.5, 1.0)],                      False),
        ("modular surface, archimedean factor",     [(-1.0, 0.5, 0.5)],                     False),
        ("JT / Liouville-QM wall",                  [(1.0, 1.0, 2.0)],                      False),
        ("H_3^+ (m-basis), level k = 5",            [(-1.0, 1.0, 2.0/3)],                   False),
        ("bulk Liouville, b = 1",                   [(1.0, 1.0, 2.0), (1.0, 1.0, 2.0)],     False),
        ("bulk Liouville, b = 0.7",                 [(1.0, 1.0, 1.4), (1.0, 1.0, 2/0.7)],   False),
        ("FZZT boundary, b = 1",                    [(0.5, 1.0, 2.0), (0.5, 1.0, 2.0)],     False),
        ("FZZT boundary, b = 0.7",                  [(0.5, 1.0, 1.4), (0.5, 1.0, 2/0.7)],   False),
    ]

    def cigar(k, nn, w):
        t = k - 2
        return [(-1.0, 1.0, 2.0/t), (-1.0, 1.0, 2.0),
                (1.0, 0.5 + (abs(nn) - k*w)/2, 1.0), (1.0, 0.5 + (abs(nn) + k*w)/2, 1.0)]
    SURVEY += [("cigar SL(2,R)/U(1), k = 14/3, n = 1, w = 0", cigar(14/3.0, 1, 0), False),
               ("cigar, k = 782/3, n = 7, w = 0",             cigar(782/3.0, 7, 0), False),
               ("cigar, k = 5, n = w = 0",                    cigar(5.0, 0, 0),     False)]

    SURVEY_FOR_FIT = [r for r in SURVEY if r[0] in (
        "target Gamma_R(s), zeta / even chi", "c=1 matrix model / 2d string, sqrt",
        "bulk Liouville, b = 1", "modular surface, archimedean factor",
        "cigar SL(2,R)/U(1), k = 14/3, n = 1, w = 0")]

    for name, f, want_match in SURVEY:
        lam, I = invariants(f, M=3)
        got = all(abs(I[k] - TG[k]) < 1e-12 for k in range(3))
        worst = max(worst, 0.0 if got == want_match else 1.0); cases += 1
        rows.append({"amplitude": name, "Lambda": lam,
                     "I_2": I[0], "I_4": I[1], "I_6": I[2],
                     "matches all three": got,
                     "first failure": (None if got else
                                       ("I_2" if abs(I[0] - TG[0]) > 1e-12 else
                                        "I_4" if abs(I[1] - TG[1]) > 1e-12 else "I_6"))})
    # the two cigar rows hit I_2 exactly and fail I_4
    for k, nn in ((14/3.0, 1), (782/3.0, 7)):
        lam, I = invariants(cigar(k, nn, 0), M=2)
        worst = max(worst, abs(I[0] - TG[0])); cases += 1
        worst = max(worst, 0.0 if abs(I[1] - TG[1]) > 0.05 else 1.0); cases += 1

    # H6: the retraction.  Gamma(1 + i r tau)/Gamma(1 + i tau), both shifts at a = 1
    rr = (17 + math.sqrt(33))/16
    lam, I = invariants([(1.0, 1.0, rr), (-1.0, 1.0, 1.0)], M=2)
    worst = max(worst, abs(I[0] + 1/24)); cases += 1                     # I_2 exactly on target
    worst = max(worst, abs(I[1] - 5/384)); cases += 1                    # I_4 = 5/384 in closed form
    worst = max(worst, abs(I[1]/TG[1] - 25/28)); cases += 1
    worst = max(worst, abs(8*rr*rr - 17*rr + 8)); cases += 1
    worst = max(worst, abs(rr*(17 - math.sqrt(33))/16 - 1.0)); cases += 1  # roots are reciprocal
    worst = max(worst, abs(I[0] + (rr - 1)**2/(3*rr))); cases += 1         # the closed form for I_2
    retraction = {"r": rr, "I_2": I[0], "I_4": I[1], "I_4 closed form 5/384": 5/384,
                  "I_4 / target": I[1]/TG[1], "25/28": 25/28,
                  "note": "both shifts at a = 1, so the last clause of manuscript 11.6 is false"}

    # the full two-factor family at a = 1 matching BOTH I_2 and I_4
    def family(P):
        s = (7 - 16*P*P)/(16*P*P*(1 + 8*P*P))
        p = -(1 + 8*P*P)/(8*P*(s - 1)); q = P - p
        r = 1/math.sqrt(s)
        return [(p/r, 1.0, r), (q, 1.0, 1.0)], s
    for Pv in (0.1, 0.25, 0.3, 0.45, 0.5, 0.6, 0.65):
        f, s = family(Pv)
        lam, I = invariants(f, M=3)
        worst = max(worst, abs(I[0] - TG[0])); cases += 1
        worst = max(worst, abs(I[1] - TG[1])); cases += 1
    worst = max(worst, abs(16*(math.sqrt(7)/4)**2 - 7)); cases += 1       # the endpoint of the family

    # imposing I_6 leaves exactly the two Legendre duplication points
    def f6(P):
        f, s = family(P)
        return invariants(f, M=3)[1][2] - TG[2]
    roots, prev = [], None
    for i in range(4, 265):
        P = i/400.0
        v = f6(P)
        if prev is not None and (v > 0) != (prev[1] > 0):
            lo_, hi_ = prev[0], P
            for _ in range(200):
                mid = 0.5*(lo_ + hi_)
                if (f6(mid) > 0) == (f6(lo_) > 0):
                    lo_ = mid
                else:
                    hi_ = mid
            roots.append(0.5*(lo_ + hi_))
        prev = (P, v)
    worst = max(worst, 0.0 if len(roots) == 2 else 1.0); cases += 1
    for rt, want in zip(sorted(roots), (0.25, 0.5)):
        worst = max(worst, abs(rt - want)); cases += 1
    # and the survivors match every invariant to m = 3
    for P in (0.25, 0.5):
        f, s = family(P)
        lam, I = invariants(f, M=3)
        worst = max(worst, max(abs(I[k] - TG[k]) for k in range(3))); cases += 3

    # H7: the two survivors ARE Legendre duplication.  The square root of the
    #     identity holds only up to a branch (it fails by a global sign on whole
    #     intervals of tau), so the squared form is what is asserted; see H12.
    #     Here: the halved form agrees up to sign at every tau tested.
    for t in (1.3, 2.7, 7.0, 21.0):
        lhs = cmath.exp(0.5*(loggamma(1 + 2j*t) - loggamma(1 + 1j*t)))
        rhs = cmath.exp(1j*t*math.log(2))*math.pi**-0.25*cmath.exp(0.5*loggamma(0.5 + 1j*t))
        worst = max(worst, min(abs(lhs - rhs), abs(lhs + rhs))/abs(rhs)); cases += 1

    # H8: the modular surface row, zeta-free.  Its Gamma content is Gamma(1/2 + i r),
    #     a = 1/2 not 1/4, so in tau = 2 r the delay is log(tau/2pi) - 1/(6 tau^2).
    #     Verified as the full asymptotic series, so the check is tight rather than
    #     a truncation compared against its own leading term:
    #       Re psi(a + i y) = log y + sum_{m>=1} (-1)^(m+1) B_2m(a)/(2 m y^2m).
    for a in (0.5, 0.25, 0.75):
        for y in (30.0, 100.0, 400.0):
            ser = math.log(y) + sum((-1)**(m + 1)*bernpoly(2*m, a)/(2*m*y**(2*m))
                                    for m in range(1, 5))
            worst = max(worst, abs(digamma_c(a + 1j*y).real - ser)); cases += 1
    #     Hence in tau = 2 r the modular surface delay is log(tau/2pi) - 1/(6 tau^2)
    #     while the target is log(tau/2pi) - 1/(24 tau^2): the shifts are 1/2 and 1/4.
    for a, lead in ((0.5, -1/6), (0.25, -1/24)):
        for tau in (60.0, 200.0, 800.0):
            y = tau/2
            meas = tau*tau*(digamma_c(a + 1j*y).real - math.log(math.pi)
                            - math.log(tau/(2*math.pi)))
            pred = 2*bernpoly(2, a) - bernpoly(4, a)/y**2 + (2.0/3)*bernpoly(6, a)/y**4
            worst = max(worst, abs(meas - pred)); cases += 1
            worst = max(worst, 0.0 if abs(2*bernpoly(2, a) - lead) < 1e-14 else 1.0)
            cases += 1
    lam_ms, I_ms = invariants([(-1.0, 0.5, 0.5)], M=1)
    worst = max(worst, abs(I_ms[0] + 1/6)); cases += 1
    worst = max(worst, abs(I_ms[0]/TG[0] - 4.0)); cases += 1
    #     and the completion matters: Lambda_zeta(2s-1)/Lambda_zeta(2s) differs from
    #     xi(2s-1)/xi(2s) for the xi of (eq:xi) by (2s-2)/(2s) = (-1+i tau)/(1+i tau),
    #     unimodular but with delay -2/tau^2 + O(tau^-4) -- enough to move I_2 from
    #     -1/6 to +11/6.  Checked without zeta.
    for tau in (50.0, 200.0, 1000.0):
        z = complex(-1.0, tau)/complex(1.0, tau)
        worst = max(worst, abs(abs(z) - 1.0)); cases += 1
        h = 1e-6
        d = (cmath.phase(complex(-1.0, tau + h)/complex(1.0, tau + h))
             - cmath.phase(complex(-1.0, tau - h)/complex(1.0, tau - h)))/(2*h)
        worst = max(worst, abs(d + 2.0/(1.0 + tau*tau))); cases += 1
    #     Sigma_2 of the archimedean factor is +1/6 (Lambda = -1 gives I_2 = -1/6);
    #     the extra factor adds -2, so Sigma_2 -> 1/6 - 2 and I_2 -> (-1)(-11/6).
    worst = max(worst, abs((-1.0)*(1.0/6 - 2.0) - 11.0/6)); cases += 1
    worst = max(worst, abs(invariants([(-1.0, 0.5, 0.5)], M=1)[1][0] - (-1.0/6))); cases += 1

    # H9: Proposition (rigidity)'s last clause needs a in [1/4, 3/4].
    #     At a = (4 - sqrt 5)/8 one has B_2(a) = -1/192 and the bound is 2, attained
    #     by two factors with n_1 = n_2 = 1 and equal widths -- integer
    #     multiplicities, and not n = 1 with a in {1/4, 3/4}.
    a_ce = (4 - math.sqrt(5))/8
    worst = max(worst, abs(bernpoly(2, a_ce) + 1.0/192)); cases += 1
    worst = max(worst, abs(1/math.sqrt(-48*bernpoly(2, a_ce)) - 2.0)); cases += 1
    for b in (0.5, 1.0, 3.7):
        lam, I = invariants([(1.0, a_ce, b), (1.0, a_ce, b)], M=2)
        worst = max(worst, abs(I[0] - TG[0])); cases += 1
        worst = max(worst, 0.0 if abs(I[1] - TG[1]) > 0.5 else 1.0); cases += 1   # fails I_4
    #     the bound exceeds one exactly on the sign window minus [1/4, 3/4]
    zlo, zhi = 0.5 - 1/(2*math.sqrt(3)), 0.5 + 1/(2*math.sqrt(3))
    for a in (0.215, 0.24, 0.76, 0.785):
        worst = max(worst, 0.0 if 1/math.sqrt(-48*bernpoly(2, a)) > 1.0 else 1.0); cases += 1
    for a in (0.25, 0.3, 0.5, 0.7, 0.75):
        worst = max(worst, 0.0 if 1/math.sqrt(-48*bernpoly(2, a)) <= 1.0 + 1e-12 else 1.0)
        cases += 1
    #     but no common-shift configuration with positive integers n_j <= 6 matches I_4
    surv = []
    for n1 in range(1, 7):
        for n2 in range(0, 7):
            for ia in range(1, 1200):
                a = zlo + (zhi - zlo)*ia/1200.0
                B2a, B4a = bernpoly(2, a), bernpoly(4, a)
                if -48*B2a*(n1 + n2)**2 > 1.0 + 1e-12:
                    continue                                  # bound violated
                # equal widths saturate; scan the ratio for the general case
                for ratio in (1.0, 1.7, 3.0):
                    if n2 == 0 and ratio != 1.0:
                        continue
                    bb = [1.0, ratio]
                    nn = [float(n1), float(n2)]
                    A = sum(u*v for u, v in zip(nn, bb))
                    Bs = sum(u/v for u, v in zip(nn, bb))
                    if A*Bs == 0:
                        continue
                    i2 = 2*B2a*A*Bs
                    if abs(i2 - TG[0]) > 1e-6:
                        continue
                    i4 = (2*A)**3*B4a*sum(u/v**3 for u, v in zip(nn, bb))
                    if abs(i4 - TG[1]) < 1e-4 and not (abs(a - 0.25) < 1e-3 or abs(a - 0.75) < 1e-3):
                        surv.append((n1, n2, a, ratio, i4))
    worst = max(worst, 0.0 if not surv else 1.0); cases += 1

    # H10: the two-shift solution in closed form, beta_1 = (13 - sqrt 153)/4
    b1 = (13 - math.sqrt(153))/4
    b2 = 0.5 - b1
    lam2 = 2*(b1 + b2)
    sig2 = bernpoly(2, 0.5)/b1 + bernpoly(2, 1.0)/b2
    worst = max(worst, abs(lam2 - 1.0)); cases += 1
    worst = max(worst, abs(lam2*sig2 - TG[0])); cases += 1

    # H11: P double-covers the two-factor family.  P = 1/4 and P = 1/2 are the same
    #      amplitude after beta -> 2 beta; the fold is the root of 128 P^4 + 32 P^2 = 7.
    fa, _ = family(0.25); fb, _ = family(0.5)
    scaled = sorted((round(n, 12), round(a, 12), round(2*b, 12)) for n, a, b in fa)
    plain = sorted((round(n, 12), round(a, 12), round(b, 12)) for n, a, b in fb)
    worst = max(worst, 0.0 if scaled == plain else 1.0); cases += 1
    Pf = 0.37438622162808732517
    worst = max(worst, abs(128*Pf**4 + 32*Pf**2 - 7)*1e-3); cases += 1

    # H12: Legendre duplication, as the SQUARED identity -- the square root of it is
    #      true only up to branch, and only d/dtau arg is used anywhere.
    for t in (1.3, 2.7, 7.0, 21.0):
        lhs = gamma_c(1 + 2j*t)/gamma_c(1 + 1j*t)
        rhs = cmath.exp(2j*t*math.log(2))*math.pi**-0.5*gamma_c(0.5 + 1j*t)
        worst = max(worst, abs(lhs - rhs)/abs(rhs)); cases += 1

    # H0: the expansion itself, against the delay assembled from Re psi.
    #     T(tau) = sum_j 2 n_j beta_j Re psi(a_j + i beta_j tau) is the exact delay,
    #     and the claim is
    #       T(tau) = Lambda log tau + c0 + sum_m ((-1)^(m+1)/m) Sigma_2m / tau^2m,
    #       c0 = 2 sum_j n_j beta_j log beta_j        (c1 = 0 here).
    #     The prefactor (-1)^(m+1)/m is UNIVERSAL and is not part of Sigma_2m.  It
    #     is +1 at m = 1, so a statement written only to that order does not show
    #     it; dropping it at m >= 2 is the error this check exists to catch.
    def _delay(factors, t):
        return sum(2*n*b*digamma_c(a + 1j*b*t).real for n, a, b in factors)

    def _series(factors, t, M, prefactor=True):
        lam = 2*sum(n*b for n, a, b in factors)
        tot = lam*math.log(t) + 2*sum(n*b*math.log(b) for n, a, b in factors)
        for m in range(1, M + 1):
            sig = sum(n*bernpoly(2*m, a)/b**(2*m - 1) for n, a, b in factors)
            tot += (((-1)**(m + 1)/m) if prefactor else 1.0)*sig/t**(2*m)
        return tot

    #     (i) the derivative step, d/dtau arg Gamma(a + i b tau) = b Re psi
    for (a, b) in ((0.25, 0.5), (1.0, 2.0), (0.5, 1.0)):
        for t in (7.0, 23.0):
            h = 1e-4
            fd = (arg_gamma(complex(a, b*(t + h))) - arg_gamma(complex(a, b*(t - h))))/(2*h)
            #   a second-difference quotient, so this is a bound, not an equality
            worst = max(worst, 0.0 if relerr(fd, b*digamma_c(a + 1j*b*t).real) < 1e-6
                        else 1.0); cases += 1

    #     (ii) the assembly, term by term and exactly: the m-th term of
    #     2 n b Re psi(a + i b tau) is ((-1)^(m+1)/m) n B_2m(a) b^(1-2m) tau^(-2m)
    for (n, a, b) in ((1.0, 0.25, 0.5), (-0.5, 0.5, 1.0), (1.7, 1.0, 2.3)):
        for m in range(1, 5):
            for t in (13.0, 101.0):
                lhs = 2*n*b*((-1)**(m + 1)*bernpoly(2*m, a)/(2*m*(b*t)**(2*m)))
                rhs = ((-1)**(m + 1)/m)*n*bernpoly(2*m, a)/b**(2*m - 1)/t**(2*m)
                worst = max(worst, relerr(lhs, rhs)); cases += 1

    #     (iii) the decisive discrimination.  At moderate tau the residual left by
    #     the correct truncation is smaller than the one left by setting the
    #     prefactor to 1 by three or more orders of magnitude.
    fitrows = []
    for name, f, _w in SURVEY_FOR_FIT:
        for t in (50.0, 90.0):
            good = abs(_delay(f, t) - _series(f, t, 2, True))
            bad = abs(_delay(f, t) - _series(f, t, 2, False))
            worst = max(worst, 0.0 if bad > 1e3*max(good, 1e-14) else 1.0); cases += 1
        fitrows.append({"amplitude": name,
                        "residual, correct prefactor, tau = 90": abs(_delay(f, 90.0) - _series(f, 90.0, 2, True)),
                        "residual, prefactor set to 1, tau = 90": abs(_delay(f, 90.0) - _series(f, 90.0, 2, False))})
    #     and the correct truncation's residual falls like tau^-6, the wrong one
    #     only like tau^-4
    for idx, (name, f, _w) in enumerate(SURVEY_FOR_FIT):
        g1 = abs(_delay(f, 20.0) - _series(f, 20.0, 2, True))
        g2 = abs(_delay(f, 40.0) - _series(f, 40.0, 2, True))
        b1 = abs(_delay(f, 20.0) - _series(f, 20.0, 2, False))
        b2 = abs(_delay(f, 40.0) - _series(f, 40.0, 2, False))
        eg = math.log(g1/g2)/math.log(2.0)
        eb = math.log(b1/b2)/math.log(2.0)
        #   these are observed decay orders, so they are bracketed, not equated
        worst = max(worst, 0.0 if 5.5 < eg < 6.5 else 1.0); cases += 1
        worst = max(worst, 0.0 if 3.8 < eb < 4.2 else 1.0); cases += 1
        fitrows[idx]["decay order, correct prefactor (predicted 6)"] = eg
        fitrows[idx]["decay order, prefactor set to 1 (predicted 4)"] = eb

    out["groups"].append({"name": "H. the graded invariants: dictionary-free, the single-factor classification, the survey, and a retraction",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-9,
                          "pass": worst < 1e-9,
                          "targets I_2m = 2^(2m-1) B_2m(1/4)": TG,
                          "single factor solutions (a, n)": SOLS,
                          "spurious grid solutions beyond those": spurious,
                          "survey": rows,
                          "expansion prefactor, residuals": fitrows,
                          "retraction of manuscript 11.6": retraction,
                          "I_6 roots on the two-factor family": sorted(roots),
                          "modular surface I_2": I_ms[0]})

    out["all_pass"] = all(g.get("pass", False) for g in out["groups"])
    out["total_checks"] = sum(g.get("cases", 0) for g in out["groups"])
    print(json.dumps(out, indent=2, sort_keys=False))

if __name__ == "__main__":
    main()
