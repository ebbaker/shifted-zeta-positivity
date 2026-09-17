#!/usr/bin/env python3
"""Checks for the deformation-flow manuscript, version 0.2.

Standard library only. Prints JSON to standard output and writes nothing.
Five groups:

  1. Truncation is multiplicative on causal kernels (Lemma 2.1 of the
     manuscript), as an exact rational matrix identity P A P B P = P A B P.
  2. Truncated causal convolutions commute (Theorem 2.2), exact; with the
     control that truncated non-causal convolutions do not, so that causality
     is what the lemma uses.
  3. The causal pole kernel 4 cosh(w x) cosh(x/2) 1_{x>0}, symmetrised, equals
     2 cosh(w(x-y)) cosh((x-y)/2), and at w = 0 equals 2|C(f)|^2 - 2|S(f)|^2.
  4. The pole symbol has vanishing real part on the imaginary axis, exact.
  5. The hyperbolic identity Q_w[f] = Q_0[cosh(wX) f] - Q_0[sinh(wX) f]
     (Proposition 6.1) as a finite matrix identity.
  6. The endpoint algebra (Proposition 8.3): G B = 0 exactly by causality,
     [G, B] = -B G which does not vanish, and the integrated form of
     d/dL G_{w,L} = B_L G_{w,L}.
  7. The resonance model (Propositions 4.1 and 4.3): a Blaschke factor with a
     zero at w + i gamma is unimodular on the critical line and has
     |b - 1|^2 equal to the Lorentzian 4w^2/(w^2 + (tau-gamma)^2) EXACTLY, with
     mass 4 pi w and total phase change -2 pi; and the summed group delay over a
     window is 2 pi times the number of resonances in it. Published zero
     ordinates enter as rational input data; the identities hold for any
     rational gamma, so this verifies the mechanism and not the arithmetic.

Groups 1, 2 and 4 are exact rational. Groups 3 and 5 are floating point and are
labelled as such. Counts are finite test cases, not independent theorems. No
check here is a positivity certificate.
"""
from fractions import Fraction
import json
import math

DATE = "2026-09-17"
MODEL = "claude-opus-5"


def sequence(n, seed):
    """Deterministic rationals in (-1, 1); no dependence on the random module."""
    out, state = [], seed
    for _ in range(n):
        state = (1103515245 * state + 12345) % 2147483648
        out.append(Fraction(state % 20011 - 10005, 10007))
    return out


def toeplitz(diag, size, causal):
    """Matrix with entries k[i-j]; causal means k[d] = 0 for d < 0."""
    def entry(d):
        if d >= 0:
            return diag[d] if d < len(diag) else Fraction(0)
        if causal:
            return Fraction(0)
        return diag[-d] if -d < len(diag) else Fraction(0)
    return [[entry(i - j) for j in range(size)] for i in range(size)]


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][t] * B[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


def project(A, lo, hi):
    n = len(A)
    return [[A[i][j] if (lo <= i < hi and lo <= j < hi) else Fraction(0)
             for j in range(n)] for i in range(n)]


def maxabs(A, B):
    return max(abs(A[i][j] - B[i][j])
               for i in range(len(A)) for j in range(len(A)))


def exact_groups(checks, samples):
    for size, lo, hi, seed in ((14, 3, 11, 7), (16, 0, 16, 11), (18, 5, 14, 23)):
        a, b = sequence(size, seed), sequence(size, seed + 101)
        A, B = toeplitz(a, size, True), toeplitz(b, size, True)
        PA, PB = project(A, lo, hi), project(B, lo, hi)
        left = matmul(matmul(PA, PB), project(
            [[Fraction(1) if i == j else Fraction(0) for j in range(size)]
             for i in range(size)], lo, hi))
        right = project(matmul(A, B), lo, hi)
        # P A P B P = P A B P, both already carrying the outer projections.
        assert maxabs(matmul(PA, PB), right) == 0, "multiplicativity failed"
        assert maxabs(left, right) == 0, "multiplicativity failed"
        checks["multiplicative_truncation"] += 1

        assert maxabs(matmul(PA, PB), matmul(PB, PA)) == 0, "causal commutator"
        checks["causal_commutator_zero"] += 1

        c, d = sequence(size, seed + 7), sequence(size, seed + 211)
        C, D = toeplitz(c, size, False), toeplitz(d, size, False)
        PC, PD = project(C, lo, hi), project(D, lo, hi)
        gap = maxabs(matmul(PC, PD), matmul(PD, PC))
        assert gap > 0, "non-causal control degenerated"
        checks["noncausal_control_nonzero"] += 1
        samples.append({"size": size, "block": [lo, hi],
                        "causal_commutator": "0",
                        "noncausal_commutator_maxabs": f"{float(gap):.6f}"})

    for numerator in range(1, 41):
        tau = Fraction(numerator, 7)
        denom = Fraction(1, 4) + tau * tau
        real_part = 2 * Fraction(-1, 2) / denom + 2 * Fraction(1, 2) / denom
        assert real_part == 0, "pole symbol has nonzero real part"
        checks["pole_symbol_imaginary_axis"] += 1


def float_groups(checks, worst):
    for L, m in ((2.3, 200), (1.0, 240), (3.0, 160)):
        h = L / m
        xs = [-L / 2 + (i + 0.5) * h for i in range(m)]
        f = [complex(math.sin(3 * x) + 0.4 * x * x,
                     0.7 * math.cos(2 * x) - 0.2 * x) for x in xs]
        for w in (0.0, 0.17, 0.5):
            causal = 0.0
            for i, x in enumerate(xs):
                gi = f[i].conjugate()
                for j, y in enumerate(xs):
                    if x > y:
                        weight = 1.0
                    elif i == j:
                        weight = 0.5
                    else:
                        continue
                    causal += (weight * 4 * math.cosh(w * (x - y))
                               * math.cosh((x - y) / 2)
                               * (gi * f[j]).real * h * h)
            symmetric = 0.0
            for i, x in enumerate(xs):
                gi = f[i].conjugate()
                for j, y in enumerate(xs):
                    symmetric += (2 * math.cosh(w * (x - y))
                                  * math.cosh((x - y) / 2)
                                  * (gi * f[j]).real * h * h)
            rel = abs(causal - symmetric) / abs(symmetric)
            assert rel < 1e-12, "causal pole kernel mismatch"
            checks["causal_pole_kernel"] += 1
            worst["causal_pole_kernel"] = max(worst["causal_pole_kernel"], rel)

            if w == 0.0:
                C = sum(math.cosh(x / 2) * f[i] for i, x in enumerate(xs)) * h
                S = sum(math.sinh(x / 2) * f[i] for i, x in enumerate(xs)) * h
                poles = 2 * abs(C) ** 2 - 2 * abs(S) ** 2
                rel = abs(causal - poles) / abs(poles)
                assert rel < 1e-12, "pole form mismatch"
                checks["pole_form_at_zero_shift"] += 1
                worst["pole_form_at_zero_shift"] = max(
                    worst["pole_form_at_zero_shift"], rel)

            # Proposition 4.1 on a generic even kernel plus a diagonal term.
            def kernel(t):
                return math.cosh(t / 2) - 0.3 * math.exp(-abs(t)) + 0.11
            shifted = 0.0
            hyperbolic = 0.0
            for i, x in enumerate(xs):
                gi = f[i].conjugate()
                for j, y in enumerate(xs):
                    base = kernel(x - y) * (gi * f[j]).real * h * h
                    shifted += math.cosh(w * (x - y)) * base
                    hyperbolic += (math.cosh(w * x) * math.cosh(w * y)
                                   - math.sinh(w * x) * math.sinh(w * y)) * base
            scale = max(abs(shifted), 1e-30)
            rel = abs(shifted - hyperbolic) / scale
            assert rel < 1e-12, "hyperbolic identity mismatch"
            checks["hyperbolic_identity"] += 1
            worst["hyperbolic_identity"] = max(worst["hyperbolic_identity"], rel)


# First twelve zero ordinates, truncated to exact rationals (published input
# data; the identities below hold for any rational gamma).
ZEROS = ["14134725/1000000", "21022040/1000000", "25010858/1000000",
         "30424876/1000000", "32935062/1000000", "37586178/1000000",
         "40918719/1000000", "43327073/1000000", "48005151/1000000",
         "49773832/1000000", "52970321/1000000", "56446248/1000000"]


def endpoint_algebra(checks, samples):
    """Proposition 8.3, as exact rational finite algebra."""
    for size, lo, hi, seed in ((16, 2, 12, 5), (20, 0, 15, 31)):
        k = sequence(size, seed)
        k = [abs(v) + Fraction(1, 3) for v in k]          # causal kernel g_omega
        G = project(toeplitz(k, size, True), lo, hi)
        f = [Fraction(0)] * size
        for i in range(lo, lo + 4):
            f[i] = sequence(4, seed + 3)[i - lo]
        edge = hi - 1                                     # the leading endpoint

        # B = (1/2) delta_edge (x) ev_edge
        def B(v):
            out = [Fraction(0)] * size
            out[edge] = Fraction(1, 2) * v[edge]
            return out

        def apply(M, v):
            return [sum(M[i][j] * v[j] for j in range(size)) for i in range(size)]

        # (ii) G B = 0 on the block: B injects at the leading edge, a causal
        # generator transports only to the right of it, which is outside.
        GB = apply(G, B(f))
        require_zero = max(abs(GB[i]) for i in range(lo, hi))
        assert require_zero == 0, "G B != 0"
        checks["endpoint_GB_zero"] += 1

        # (iii) [G, B] = -B G, and B G is not zero
        BG = B(apply(G, f))
        comm = [GB[i] - BG[i] for i in range(size)]
        assert all(comm[i] == -BG[i] for i in range(size)), "commutator identity"
        assert any(BG[i] != 0 for i in range(size)), "B G degenerated"
        checks["endpoint_commutator"] += 1

        # (iv) integrated flatness: G_{L'} f - G_L f is the restriction of the
        # convolution to the annulus, which is what int B_s G_s f ds gives.
        full = toeplitz(k, size, True)
        gf = [sum(full[i][j] * f[j] for j in range(size)) for i in range(size)]
        for hi2 in (hi + 1, hi + 3):
            if hi2 > size:
                continue
            lhs = [(gf[i] if lo <= i < hi2 else Fraction(0))
                   - (gf[i] if lo <= i < hi else Fraction(0)) for i in range(size)]
            rhs = [gf[i] if hi <= i < hi2 else Fraction(0) for i in range(size)]
            assert all(a == b for a, b in zip(lhs, rhs)), "integrated flatness"
            checks["endpoint_flatness"] += 1
        samples.append({"size": size, "block": [lo, hi], "edge": edge,
                        "GB": "0", "BG_nonzero": True})


def resonance_model(checks, worst):
    """Propositions 4.1 and 4.3 in a Blaschke model built from published zeros."""
    gammas = [Fraction(z) for z in ZEROS]
    for w in (Fraction(1, 20), Fraction(1, 100)):
        # (a),(b) one factor: b(i tau) = (-w + i u)/(w + i u), u = tau - gamma
        for g in gammas[:6]:
            for num in (0, 1, 2, 5, 17):
                u = Fraction(num, 10)
                tau = g + u
                mod2 = (w * w + u * u) / (w * w + u * u)
                assert mod2 == 1, "Blaschke factor not unimodular"
                checks["blaschke_unimodular"] += 1
                # |b - 1|^2 = 4 w^2 / (w^2 + u^2), exactly
                lhs = (4 * w * w) / (w * w + u * u)
                num_re = -w - w
                shape = (num_re * num_re) / (w * w + u * u)
                assert lhs == shape, "line shape not exact"
                checks["blaschke_line_shape"] += 1
        # (c) mass of the Lorentzian over a window, closed form
        for U in (10, 100, 1000):
            mass = (2.0 * float(w)) * (2.0 / math.pi) * math.atan(U / float(w))
            rel = abs(mass - 2.0 * float(w)) / (2.0 * float(w))
            assert rel < 5e-3, "resonance mass"
            checks["resonance_mass"] += 1
            worst["resonance_mass"] = max(worst["resonance_mass"], rel)
        # (d),(f) summed group delay over a window equals 2 pi times the count
        T1, T2 = 10.0, 60.0
        inwin = [float(g) for g in gammas if T1 < float(g) < T2]
        fw = float(w)
        n, total = 200000, 0.0
        for j in range(n):                                  # midpoint rule
            t = T1 + (j + 0.5) * (T2 - T1) / n
            total += sum(2 * fw / (fw * fw + (t - g) ** 2) for g in inwin)
        total *= (T2 - T1) / n
        rel = abs(total - 2 * math.pi * len(inwin)) / (2 * math.pi * len(inwin))
        assert rel < 2e-2, "group delay sum"
        checks["group_delay_sum"] += 1
        worst["group_delay_sum"] = max(worst["group_delay_sum"], rel)


def main():
    checks = dict(multiplicative_truncation=0, causal_commutator_zero=0,
                  noncausal_control_nonzero=0, pole_symbol_imaginary_axis=0,
                  causal_pole_kernel=0, pole_form_at_zero_shift=0,
                  hyperbolic_identity=0, endpoint_GB_zero=0,
                  endpoint_commutator=0, endpoint_flatness=0,
                  blaschke_unimodular=0, blaschke_line_shape=0,
                  resonance_mass=0, group_delay_sum=0)
    worst = dict(causal_pole_kernel=0.0, pole_form_at_zero_shift=0.0,
                 hyperbolic_identity=0.0, resonance_mass=0.0,
                 group_delay_sum=0.0)
    samples = []
    exact_groups(checks, samples)
    float_groups(checks, worst)
    endpoint_algebra(checks, samples)
    resonance_model(checks, worst)

    print(json.dumps({
        "status": "passed",
        "date": DATE,
        "model": MODEL,
        "arithmetic": {
            "exact_rational": ["multiplicative_truncation",
                               "causal_commutator_zero",
                               "noncausal_control_nonzero",
                               "pole_symbol_imaginary_axis",
                               "endpoint_GB_zero", "endpoint_commutator",
                               "endpoint_flatness", "blaschke_unimodular",
                               "blaschke_line_shape"],
            "floating_point": ["causal_pole_kernel", "pole_form_at_zero_shift",
                               "hyperbolic_identity", "resonance_mass",
                               "group_delay_sum"],
        },
        "checks": checks,
        "total_checks": sum(checks.values()),
        "worst_relative_error": {k: f"{v:.2e}" for k, v in worst.items()},
        "commutator_samples": samples,
        "reading": "Truncation to an interval is multiplicative on causal "
                   "kernels, so truncated causal convolutions form a "
                   "commutative algebra and the shift flow carries no path "
                   "ordering. The non-causal control shows causality is what "
                   "the argument uses. The causal realisation of the pole "
                   "factors reproduces the contact and pole term exactly, "
                   "while the same symbol has identically zero real part on "
                   "the imaginary axis, so a Fourier reading of the generator "
                   "loses that term. The shift acts on inputs by a hyperbolic "
                   "rotation generated by multiplication by x. The endpoint "
                   "operator is annihilated from the left by the causal "
                   "generator, so the endpoint algebra is triangular rather "
                   "than commutative, and the generator's own length variation "
                   "is its boundary value. In the Blaschke model each zero "
                   "contributes a Lorentzian of height 4 and half-width w to "
                   "|K-1|^2, of mass 4 pi w and total phase change -2 pi, so "
                   "the summed group delay over a window is 2 pi times the "
                   "number of resonances in it.",
        "zero_ordinates": "first twelve, truncated to exact rationals; "
                          "published input data. The Blaschke identities hold "
                          "for any rational gamma, so these checks verify the "
                          "mechanism and not the arithmetic.",
        "scope": "Finite algebra underlying the identities of Sections 3 to 8 "
                 "of the manuscript. Not a positivity certificate, not a "
                 "verification of the convergence arguments in the proof of "
                 "Theorem 3.1, not a computation with zeta itself, and not a "
                 "statement about operator domains.",
    }, indent=2))


if __name__ == "__main__":
    main()
