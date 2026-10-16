#!/usr/bin/env python3
"""Exact algebra for the gauge-transfer tests; no Weil positivity claim."""

from fractions import Fraction as F
import json
import math


def chebyshev_first(n, x):
    values = [F(1), x]
    for j in range(2, n + 1):
        values.append(2 * x * values[-1] - values[-2])
    return values[n]


def character(n, x):
    values = [F(1), 2 * x]
    for j in range(2, n + 1):
        values.append(2 * x * values[-1] - values[-2])
    return values[n]


def main():
    counts = {}
    count = 0
    for x in (F(-3, 5), F(0), F(1, 5), F(7, 8), F(1)):
        for m in range(2, 10):
            assert character(m, x) - character(m - 2, x) == (
                2 * chebyshev_first(m, x)
            )
            count += 1
    counts["su2_winding_character_identity"] = count

    count = 0
    for y in (F(1, 5), F(1, 3), F(2, 3), F(9, 10)):
        difference = 3 * y**4 - 2 * y**3 - 1
        assert difference == (y - 1) * (3 * y**3 + y**2 + y + 1)
        assert difference < 0
        count += 1
    counts["second_winding_exact_obstruction"] = count

    count = 0
    for q_t in (F(1, 3), F(2, 3), F(4, 5)):
        for q_u in (F(1, 2), F(3, 4)):
            c_t = (1 + 2 * q_t**2) / 3
            c_u = (1 + 2 * q_u**2) / 3
            c_tu = (1 + 2 * (q_t * q_u)**2) / 3
            defect = F(2, 9) * (1 - q_t**2) * (1 - q_u**2)
            assert c_tu - c_t * c_u == defect
            assert defect > 0
            count += 1
    counts["central_semigroup_obstruction"] = count

    count = 0
    for n in range(12):
        a = 2 * n + F(1, 2)
        assert a > 0
        for r in (F(1, 4), F(1, 2), F(3, 4)):
            # r = exp(-t/2), hence exp(-t a_n) = r**(4n+1).
            eigen_transfer = r**(4 * n + 1)
            assert eigen_transfer == r * (r**4)**n
            count += 1
    counts["disk_spectrum_and_transfer_exponents"] = count

    count = 0
    for a in (F(1, 2), F(3, 2)):
        for d in (F(1, 3), F(2, 3)):
            theta = a * d / 2
            assert 0 <= theta <= 1
            for q in (F(1, 2), F(2, 3)):
                for s in (F(0), F(1, 4), F(2), F(11)):
                    gamma = (2 / a) * s / (a**2 + s)
                    for cosine in (F(-1), F(0), F(3, 5), F(1)):
                        delay_norm = 1 + q**2 - 2 * q * cosine
                        lhs = (1 - theta) * gamma + theta * gamma * delay_norm
                        difference = q**2 - 2 * q * cosine
                        rhs = gamma + d * difference - (
                            d * a**2 * difference / (a**2 + s)
                        )
                        assert lhs == rhs
                        assert lhs >= 0
                        count += 1
    counts["complete_branching_multiplier"] = count

    count = 0
    for a in (F(1, 2), F(3, 2)):
        for d in (F(1, 3), F(2, 3)):
            c = a * d / 2
            for q in (F(1, 2), F(2, 3), F(3, 4)):
                # Algebraic exponent variables: q=exp(-ad), X=exp(ar).
                x_inside = (1 + 1 / q) / 2
                raw_inside = -c * (
                    q**2 / x_inside
                    - q * (q * x_inside + q / x_inside)
                )
                assert raw_inside == c * q**2 * x_inside
                x_outside = 2 / q
                raw_outside = -c * (
                    q**2 / x_outside
                    - q * (1 / (q * x_outside) + q / x_outside)
                )
                assert raw_outside == c / x_outside
                at_boundary = 1 / q
                assert c * q**2 * at_boundary == c / at_boundary
                jump = -c * a * q - c * a * q
                assert jump == -d * a**2 * q
                assert jump < 0
                count += 4
    counts["piecewise_kernel_and_nonzero_cusp"] = count

    count = 0
    for tau in (F(0), F(1, 3), F(1), F(7, 2)):
        denominator = F(1, 4) + tau**2
        gamma_first_real = 2 * tau**2 / denominator
        gamma_second_imag = tau / denominator
        gamma_norm = gamma_first_real**2 + gamma_second_imag**2
        assert gamma_norm == 4 * tau**2 / denominator
        for u in (F(1, 3), F(2, 5)):
            for v in (F(-1), -2 * u):
                dq = -2 * u * v
                assert dq > 0
                contact = v**2 + 4 * u**2
                assert contact - 2 * dq == (v + 2 * u)**2
                for cosine, sine in (
                    (F(1), F(0)), (F(0), F(1)),
                    (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
                ):
                    z_first_imag = 2 * u * sine
                    z_second_real = v + 2 * u * cosine
                    total = (
                        gamma_first_real**2 + z_first_imag**2
                        + z_second_real**2 + gamma_second_imag**2
                    )
                    assert total == gamma_norm + contact - 2 * dq * cosine
                    count += 1
    counts["coherent_cusp_cancellation_and_contact"] = count

    q2 = 2**(-0.5)
    result = {
        "status": "passed",
        "date": "2026-09-14",
        "arithmetic": "exact rational except the labelled illustration",
        "checks": counts,
        "total_checks": sum(counts.values()),
        "prime_2_illustration_only": {
            "first_return": q2,
            "second_winding": (3 * q2**(8 / 3) - 1) / 2,
            "required_second_return": 0.5,
            "branch_weight": math.log(2) / 4,
            "cusp_derivative_jump": -math.log(2) * q2 / 4,
        },
        "scope": (
            "Finite algebra checks for the written comparison proofs. "
            "No full Yang-Mills construction, no matched Weil pairing, "
            "and no positivity certificate for the Weil form."
        ),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
