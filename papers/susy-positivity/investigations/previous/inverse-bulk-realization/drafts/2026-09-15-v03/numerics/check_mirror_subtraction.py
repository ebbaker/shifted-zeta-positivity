#!/usr/bin/env python3
"""The mirror prime reference and the subtraction form of the localized Weil form.

Standard library only. Prints a JSON record to standard output.

Two facts are checked.

(1) Exact algebra. Alongside the positive prime reference with multiplier
    w_{r,d}(z) = kappa (z^0) - d r^{|n|} (z^n), kappa = 2dr/(1-r),
there is a mirror reference
    wt_{r,d}(z) = d r (1-r)/(1+r) * |1+z|^2 / |1-rz|^2
                = kappat (z^0) + d r^{|n|} (z^n),  kappat = 2dr/(1+r),
nonnegative on the circle, carrying the SAME prime atoms with the opposite
sign and a strictly smaller contact. kappat is the least contact compatible
with those atoms, as kappa is for the other sign, and w + wt = 4dr/(1-r^2).

(2) The subtraction form. Because the mirror atoms carry the opposite sign,
    Q_L = A_L - sum_p Bt_{r_p,d_p},
    A_L = K[E_L f] + (w0 + sum_p kappat_p) ||f||^2 + P_L[f],
and A_L contains NO prime translations: all arithmetic sits in the subtracted
term, which is a sum of positive references. Weil positivity on I_L is then
exactly the domination sum_p Bt_p <= A_L.

The programme verifies (1) exactly in rational arithmetic and (2) as an
identity of quadratic forms on explicit step-function inputs, and reports
Rayleigh quotients in a step-function subspace. Those quotients are one
sided: a subspace value ABOVE 1 certifies that domination fails, a value
below 1 certifies nothing. No Weil positivity certificate and no
field-theoretic construction is claimed.
"""
import json
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_channel_bound import Step, W0, kappa, primes_below, active_shifts  # noqa: E402


def kappa_tilde(p):
    r = p ** -0.5
    return 2 * math.log(p) * r / (1 + r)


def poisson_coeffs(r, nmax):
    """Laurent coefficients of (1-r^2)/|1-rz|^2 on |z|=1, exactly: r^{|n|}."""
    return [r ** abs(n) for n in range(-nmax, nmax + 1)]


def mirror_coeffs(r, d, nmax):
    """Coefficients of d r (1-r)/(1+r) * (2+z+1/z) * (1/(1-r^2)) * sum r^{|n|} z^n."""
    pois = poisson_coeffs(r, nmax + 1)
    out = []
    for n in range(0, nmax + 1):
        i = n + nmax + 1
        raw = (2 * pois[i] + pois[i - 1] + pois[i + 1]) / (1 - r * r)
        out.append(d * r * (1 - r) / (1 + r) * raw)
    return out


def main():
    checks = {}

    # (1) exact rational algebra for the mirror weight
    exact = 0
    for r in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(7, 10)):
        d = Fraction(3, 2)
        co = mirror_coeffs(r, d, 6)
        assert co[0] == 2 * d * r / (1 + r), (r, co[0])
        exact += 1
        for n in range(1, 7):
            assert co[n] == d * r ** n, (r, n, co[n], d * r ** n)
            exact += 1
        # sum rule with the original reference
        assert 2 * d * r / (1 - r) + 2 * d * r / (1 + r) == 4 * d * r / (1 - r * r)
        exact += 1
        # least contact for the mirror sign: the multiplier at z = -1 is
        # C + 2d*sum (-r)^n = C - 2dr/(1+r); nonnegative forces C >= 2dr/(1+r)
        alt = sum(2 * d * (-r) ** n for n in range(1, 400))
        assert abs(alt + 2 * d * r / (1 + r)) < Fraction(1, 10 ** 30)
        exact += 1
    checks["mirror_weight_exact_coefficients"] = exact

    # the mirror weight is nonnegative on the circle (it is a modulus squared)
    pos = 0
    for p in (2, 3, 5, 7):
        r, d = p ** -0.5, math.log(p)
        lo = min(d * r * (1 - r) / (1 + r) * abs(1 + z) ** 2 / abs(1 - r * z) ** 2
                 for z in (complex(math.cos(t), math.sin(t))
                           for t in (2 * math.pi * k / 2048 for k in range(2048))))
        assert lo >= 0.0
        pos += 1
    checks["mirror_weight_nonnegative_samples"] = pos

    # (2) the subtraction identity, as quadratic forms on step inputs
    def pieces(L, fv):
        s = Step(L, fv)
        K, _ = s.gamma_energy()
        n2 = s.norm2()
        ps = primes_below(math.exp(L))
        ktsum = sum(kappa_tilde(p) for p in ps)
        mirror = ktsum * n2
        for dd, coef in active_shifts(L):
            mirror += coef * s.corr(dd)        # PLUS: the mirror atoms
        A = K + (W0 + ktsum) * n2 + s.poles()
        Q = K + W0 * n2 + s.poles() + s.prime_term(L)
        return dict(norm2=n2, K=K, A_sub=A, mirror=mirror, Q=Q,
                    kappa_tilde_sum=ktsum, kappa_sum=sum(kappa(p) for p in ps),
                    primes=ps, identity_error=abs(A - mirror - Q))

    ident, samples = 0, []
    inputs = [[1.0], [1, -1], [1, 1, 0, -1, -1, 0, 1, 1], [1, 2, -1, 3, 0, -2, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 1]]
    for L in (0.8, 1.0, 1.25, 1.5, 2.0, 3.0):
        for fv in inputs:
            r = pieces(L, fv)
            assert r["identity_error"] < 1e-9, (L, fv, r["identity_error"])
            assert r["Q"] > 0
            ident += 1
        samples.append({k: v for k, v in pieces(L, [1.0]).items() if k != "primes"} |
                       {"L": L, "primes": pieces(L, [1.0])["primes"]})
    checks["subtraction_identity_on_step_inputs"] = ident

    # (3) one-sided Rayleigh quotients in a step subspace
    def quotient(L, cells, which):
        """max over the step subspace of  (mirror form)/(reference form)."""
        h = L / cells
        basis = []
        for i in range(cells):
            v = [0.0] * cells
            v[i] = 1.0
            basis.append(v)

        def form(fv, kind):
            s = Step(L, fv)
            K, _ = s.gamma_energy()
            n2 = s.norm2()
            ps = primes_below(math.exp(L))
            if kind == "mirror":
                val = sum(kappa_tilde(p) for p in ps) * n2
                for dd, coef in active_shifts(L):
                    val += coef * s.corr(dd)
                return val
            if kind == "prime":
                val = sum(kappa(p) for p in ps) * n2
                for dd, coef in active_shifts(L):
                    val -= coef * s.corr(dd)
                return val
            if kind == "A_sub":
                return K + (W0 + sum(kappa_tilde(p) for p in ps)) * n2 + s.poles()
            return K

        def matrix(kind):
            n = cells
            diag = [form(b, kind) for b in basis]
            M = [[0.0] * n for _ in range(n)]
            for i in range(n):
                M[i][i] = diag[i]
            for i in range(n):
                for j in range(i + 1, n):
                    v = [basis[i][k] + basis[j][k] for k in range(n)]
                    M[i][j] = M[j][i] = 0.5 * (form(v, kind) - diag[i] - diag[j])
            return M

        num = matrix("mirror" if which == "new" else "prime")
        den = matrix("A_sub" if which == "new" else "K")
        # power iteration on den^{-1} num via Cholesky of den
        n = cells
        Lc = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                t = den[i][j] - sum(Lc[i][k] * Lc[j][k] for k in range(j))
                if i == j:
                    if t <= 0:
                        return None          # reference form not positive here
                    Lc[i][i] = math.sqrt(t)
                else:
                    Lc[i][j] = t / Lc[j][j]

        def solve(b):
            y = [0.0] * n
            for i in range(n):
                y[i] = (b[i] - sum(Lc[i][k] * y[k] for k in range(i))) / Lc[i][i]
            x = [0.0] * n
            for i in reversed(range(n)):
                x[i] = (y[i] - sum(Lc[k][i] * x[k] for k in range(i + 1, n))) / Lc[i][i]
            return x

        x = [1.0 / (i + 1) for i in range(n)]
        lam = 0.0
        for _ in range(4000):
            y = solve([sum(num[i][k] * x[k] for k in range(n)) for i in range(n)])
            nrm = math.sqrt(sum(t * t for t in y))
            if nrm == 0:
                return 0.0
            x = [t / nrm for t in y]
            num_x = [sum(num[i][k] * x[k] for k in range(n)) for i in range(n)]
            den_x = [sum(den[i][k] * x[k] for k in range(n)) for i in range(n)]
            lam = sum(x[i] * num_x[i] for i in range(n)) / sum(x[i] * den_x[i] for i in range(n))
        return lam

    quotients = []
    for L in (1.0, 1.25, 1.5, 2.0, 3.0):
        new = quotient(L, 24, "new")
        old = quotient(L, 24, "old")
        quotients.append({"L": L, "mirror_over_A_sub": new, "prime_over_gamma": old,
                          "old_architecture_fails": old is not None and old > 1})
    assert all(q["old_architecture_fails"] for q in quotients if q["L"] >= 1.25)
    checks["rayleigh_quotients"] = len(quotients)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "arithmetic": "exact rational for the mirror weight; floating point elsewhere",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "indicator_samples": samples,
        "rayleigh_quotients": quotients,
        "reading": "prime_over_gamma is the largest value of (sum_p B_p)/K on the "
                   "step subspace; a value above 1 certifies that the gamma energy "
                   "cannot dominate the prime references, which is the quantitative "
                   "form of the two-channel exclusion. mirror_over_A_sub is the "
                   "corresponding quotient for the subtraction form; a subspace "
                   "value below 1 is a lower bound only and certifies nothing.",
        "scope": "Exact algebra for the mirror reference and the subtraction identity. "
                 "No Weil positivity certificate, no operator-domain statement, and "
                 "no field-theoretic realization of either term.",
    }, indent=2))


if __name__ == "__main__":
    main()
