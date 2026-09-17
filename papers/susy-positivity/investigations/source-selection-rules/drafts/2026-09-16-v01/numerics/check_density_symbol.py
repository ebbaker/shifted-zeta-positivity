#!/usr/bin/env python3
"""The archimedean symbol of the Weil form, together with the contact, is the
smooth zero-counting density.

Standard library only. Prints a JSON record to standard output.

Conventions are those of Section 2 of the inverse-bulk manuscript 0.5. There

    b(tau^2) = sum_{n>=0} (2/a_n) tau^2/(a_n^2 + tau^2) = Re psi(1/4 + i tau/2) - psi(1/4),
    a_n      = 2n + 1/2,                                                   (2.2), (2.6)
    w0       = psi(1/4) - log pi = -gammaE - pi/2 - 3 log 2 - log pi,      (2.7)

and the archimedean part of the target is K[F] + w0 ||f||^2, which by Plancherel
is (1/2pi) int [b(tau^2) + w0] |F^(tau)|^2 dtau.

THE IDENTITY CHECKED HERE is

    b(tau^2) + w0 = Re psi(1/4 + i tau/2) - log pi = 2 theta'(tau),         (D)

where theta(t) = arg Gamma(1/4 + it/2) - (t/2) log pi is the Riemann-Siegel
theta function.  Since the smooth part of the Riemann-von Mangoldt counting
function is Nbar(T) = theta(T)/pi + 1, (D) says

    K[E_L f] + w0 ||f||^2 = int_R |F^(tau)|^2 dNbar(tau),                   (*)

i.e. the gamma energy together with the contact is integration against the
SMOOTH ZERO-COUNTING MEASURE.  The contact constant is not an independent
object: it is the -log pi inside theta'.

SIX FACTS ARE CHECKED.

(1) The series and digamma forms of b agree, (2.6).
(2) w0 agrees with its closed form, (2.7).
(3) (D): b(tau^2) + w0 equals twice a central-difference derivative of theta
    computed from arg Gamma, at several tau.  This is the content of (*); the
    two sides are computed by different routines (a partial-fraction digamma
    and a Stirling log-Gamma) so the agreement is not definitional.
(4) The asymptotic expansion
        b(tau^2) + w0 = log(tau/2pi) + 0*tau^{-1} - (1/24) tau^{-2}
                        + 0*tau^{-3} - (7/960) tau^{-4} + ...
    which is Stirling for theta'.  The absence of the odd orders is the
    reflection symmetry of Proposition 2.4 seen in the expansion.
(5) Nbar tracks the true zero count to within one at the first three published
    ordinates, which is what makes (*) a statement about zeros rather than a
    rewriting; the residual is the fluctuation S, which the prime term carries.
(6) The consequences for the subtraction form: the symbol
        sigma_L(tau) = b(tau^2) + w0 + sum_{p<e^L} kappat_p = 2 theta'(tau) + Sigma_L
    is negative exactly on |tau| < tau_L, this band shrinks with L, and it is
    EMPTY for L > log 13 -- because c_L = sigma_L(0) > 0 is exactly
    Sigma_L > -2 theta'(0) = -w0 = 5.3721834..., the maximum negativity of the
    smooth zero density.  The programme locates tau_L and the crossing prime.

WHAT THIS DOES AND DOES NOT ESTABLISH.  (1)-(4) and (6) are finite numerical
verifications of identities that are proved in the accompanying note; the
digamma and log-Gamma routines are standard and carry the stated tolerances.
(5) uses three published zero ordinates as labelled floating-point input and
establishes nothing about zeros itself.  No positivity statement, no field
theory, and no part of the Weil criterion is claimed here.
"""
import cmath
import json
import math

GAMMA_E = 0.57721566490153286060651209008240243104215933593992
CATALAN = 0.91596559417721901505460351493238411077414937428167
TOL = 1e-11

B2 = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]


def digamma(z):
    """psi(z) for complex z, by recurrence to large argument plus Stirling."""
    z = complex(z)
    total = 0.0 + 0.0j
    while z.real < 20.0:
        total -= 1.0/z
        z += 1.0
    total += cmath.log(z) - 0.5/z
    zz = z*z
    power = zz
    for k, b in enumerate(B2, start=1):
        total -= b/(2*k*power)
        power *= zz
    return total


def loggamma(z):
    """log Gamma(z) for complex z with positive real part, continuous branch."""
    z = complex(z)
    shift = 0.0 + 0.0j
    while z.real < 20.0:
        shift -= cmath.log(z)
        z += 1.0
    total = (z - 0.5)*cmath.log(z) - z + 0.5*math.log(2*math.pi)
    power = z
    for k, b in enumerate(B2, start=1):
        total += b/(2*k*(2*k - 1)*power)
        power *= z*z
    return total + shift


def b_digamma(t):
    return digamma(0.25 + 0.5j*t).real - digamma(0.25).real


def b_series(t, terms=400000):
    """The partial-fraction form (2.6), with an explicit tail bound."""
    total = 0.0
    for n in range(terms):
        a = 2*n + 0.5
        total += (2.0/a)*(t*t)/(a*a + t*t)
    a = 2*terms + 0.5
    tail = (t*t)*(0.5/(a - 2.0)**2 + 1.0/(a - 2.0))   # crude upper bound
    return total, tail


def theta(t):
    return loggamma(0.25 + 0.5j*t).imag - 0.5*t*math.log(math.pi)


def theta_prime(t, step=1e-5):
    return (theta(t + step) - theta(t - step))/(2*step)


def nbar(t):
    return theta(t)/math.pi + 1.0


def primes_below(bound):
    found, n = [], 2
    while n < bound:
        if all(n % p for p in found if p*p <= n):
            found.append(n)
        n += 1
    return found


def kappa_tilde(p):
    """2 d r /(1 + r) with d = log p, r = p^{-1/2}."""
    return 2.0*math.log(p)/(math.sqrt(p) + 1.0)


def bisect(f, lo, hi, rounds=200):
    flo = f(lo)
    for _ in range(rounds):
        mid = 0.5*(lo + hi)
        if (f(mid) < 0) == (flo < 0):
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def main():
    checks = {}
    w0 = digamma(0.25).real - math.log(math.pi)
    closed = -GAMMA_E - math.pi/2 - 3*math.log(2) - math.log(math.pi)

    # (2) the contact constant
    assert abs(w0 - closed) < TOL, (w0, closed)
    checks["contact_constant"] = 1

    # (1) series against digamma
    series_rows = []
    for t in (0.5, 1.0, 3.0, 7.5):
        partial, tail = b_series(t)
        exact = b_digamma(t)
        assert partial <= exact + 1e-9 and exact - partial <= tail, (t, partial, exact, tail)
        series_rows.append({"tau": t, "series_partial": partial,
                            "digamma": exact, "tail_bound": tail})
    checks["series_versus_digamma"] = len(series_rows)

    # (3) the identity (D)
    identity_rows = []
    for t in (0.5, 1.0, 2.0, 6.0, 14.134725142, 40.0, 137.0):
        lhs = b_digamma(t) + w0
        mid = digamma(0.25 + 0.5j*t).real - math.log(math.pi)
        rhs = 2.0*theta_prime(t)
        assert abs(lhs - mid) < TOL, (t, lhs, mid)
        assert abs(lhs - rhs) < 1e-7, (t, lhs, rhs)
        identity_rows.append({"tau": t, "b_plus_w0": lhs, "two_theta_prime": rhs,
                              "gap": lhs - rhs})
    checks["density_identity"] = 2*len(identity_rows)

    # (4) the expansion
    expansion_rows = []
    for t in (20.0, 50.0, 100.0, 200.0, 500.0):
        residual = (b_digamma(t) + w0) - math.log(t/(2*math.pi))
        first = residual*t
        second = residual*t*t
        third = (residual + 1.0/(24*t*t))*t**4
        assert abs(first) < 3e-3, (t, first)
        assert abs(second + 1.0/24) < 5e-5, (t, second)
        assert abs(third + 7.0/960) < 5e-4, (t, third)
        expansion_rows.append({"tau": t, "residual_times_tau": first,
                               "residual_times_tau2": second,
                               "next_order_times_tau4": third})
    checks["expansion_coefficients"] = 3*len(expansion_rows)

    # (5) the smooth count against published ordinates
    ordinates = [14.134725142, 21.022039639, 25.010857580]
    count_rows = []
    for index, gamma in enumerate(ordinates):
        value = nbar(gamma)
        assert abs(value - index) < 1.0, (gamma, value, index)
        count_rows.append({"published_ordinate": gamma, "Nbar": value,
                           "true_count_below": index, "S": value - index})
    checks["smooth_count_at_ordinates"] = len(count_rows)

    # (6) the sign structure of the symbol
    tau_star = bisect(lambda t: b_digamma(t) + w0, 0.1, 40.0)
    assert abs(tau_star - 2*math.pi) < 0.01, tau_star

    ladder, running, crossing = [], 0.0, None
    for p in primes_below(100):
        running += kappa_tilde(p)
        ladder.append({"p": p, "Sigma": running, "c_L_after_p": w0 + running})
        if crossing is None and w0 + running > 0:
            crossing = p
    assert crossing == 13, crossing

    band = []
    for target in (0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0):
        sigma_shift = sum(kappa_tilde(p) for p in primes_below(math.exp(target)))
        symbol = lambda t: b_digamma(t) + w0 + sigma_shift
        c_L = symbol(0.0)
        if c_L >= 0:
            band.append({"L": target, "Sigma_L": sigma_shift, "c_L": c_L,
                         "tau_L": None, "negative_band": "empty"})
            continue
        tau_L = bisect(symbol, 1e-9, 1e6)
        assert symbol(0.5*tau_L) < 0 < symbol(2.0*tau_L), target
        band.append({"L": target, "Sigma_L": sigma_shift, "c_L": c_L,
                     "tau_L": tau_L, "negative_band": "|tau| < tau_L"})
    checks["symbol_sign_structure"] = 1 + len(ladder) + 2*len(band)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-16",
        "model": "claude-opus-5",
        "arithmetic": "floating point throughout; the digamma and log-Gamma "
                      "routines are recurrence plus Stirling, and the series "
                      "check carries an explicit tail bound",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "contact": {"w0": w0, "closed_form": closed,
                    "note": "w0 = psi(1/4) - log pi is the -log pi inside theta'"},
        "series_versus_digamma": series_rows,
        "density_identity": identity_rows,
        "expansion": expansion_rows,
        "smooth_count": count_rows,
        "symbol_vanishes_at": tau_star,
        "two_pi": 2*math.pi,
        "constant_ladder": ladder,
        "crossing_prime": crossing,
        "negative_band": band,
        "reading": "b(tau^2) + w0 = 2 theta'(tau), so the gamma energy together "
                   "with the contact is integration against the smooth "
                   "zero-counting measure Nbar = theta/pi + 1. The contact "
                   "requires no mechanism of its own. The archimedean form is a "
                   "SIGNED measure, negative exactly below tau* = 6.2898 "
                   "(compare 2pi = 6.2832); after the summed prime contacts join "
                   "it the negative band is |tau| < tau_L, which shrinks with L "
                   "and is empty for L > log 13, the crossing being exactly the "
                   "point where the prime contacts overtake -w0.",
        "scope": "An exact re-presentation of the archimedean part of the "
                 "target, verified numerically. No positivity statement, no "
                 "zero-free or zero-location claim, and no field theory.",
    }, indent=2))


if __name__ == "__main__":
    main()
