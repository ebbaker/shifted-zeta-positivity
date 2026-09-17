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
  F. Two objects that DO wind: the phase shift of the inverted harmonic
     oscillator on the half-line, eta(tau) = arg Gamma(1/4 + i tau/2), whose
     derivative differs from theta' by exactly (log pi)/2; and the bulk
     Liouville reflection amplitude, whose phase derivative is 4 Q log P.

Tolerances are numerical agreement thresholds, not theorems.
"""
import cmath, json, math

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

    out["all_pass"] = all(g.get("pass", False) for g in out["groups"])
    out["total_checks"] = sum(g.get("cases", 0) for g in out["groups"])
    print(json.dumps(out, indent=2, sort_keys=False))

if __name__ == "__main__":
    main()
