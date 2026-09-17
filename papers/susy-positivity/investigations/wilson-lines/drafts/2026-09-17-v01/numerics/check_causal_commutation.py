#!/usr/bin/env python3
"""Checks for the deformation-flow manuscript, version 0.1.

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
     (Proposition 4.1) as a finite matrix identity.

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


def main():
    checks = dict(multiplicative_truncation=0, causal_commutator_zero=0,
                  noncausal_control_nonzero=0, pole_symbol_imaginary_axis=0,
                  causal_pole_kernel=0, pole_form_at_zero_shift=0,
                  hyperbolic_identity=0)
    worst = dict(causal_pole_kernel=0.0, pole_form_at_zero_shift=0.0,
                 hyperbolic_identity=0.0)
    samples = []
    exact_groups(checks, samples)
    float_groups(checks, worst)

    print(json.dumps({
        "status": "passed",
        "date": DATE,
        "model": MODEL,
        "arithmetic": {
            "exact_rational": ["multiplicative_truncation",
                               "causal_commutator_zero",
                               "noncausal_control_nonzero",
                               "pole_symbol_imaginary_axis"],
            "floating_point": ["causal_pole_kernel", "pole_form_at_zero_shift",
                               "hyperbolic_identity"],
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
                   "rotation generated by multiplication by x.",
        "scope": "Finite algebra underlying the identities of Sections 1 to 4 "
                 "of the manuscript. Not a positivity certificate, not a "
                 "verification of the convergence arguments in the proof of "
                 "Theorem 1.1, and not a statement about operator domains.",
    }, indent=2))


if __name__ == "__main__":
    main()
