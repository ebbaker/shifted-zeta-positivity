"""Check finite rational identities in GNP-BB-E03 r1 (13 November 2026).

Prepared for Edward Baker with substantial OpenAI Codex assistance.
Subagent dispatch: gpt-6.1-sol / ultra. Backend metadata unavailable.
"""

import json
from fractions import Fraction


def a_process(k, ell):
    denominator = 2 * k + 2
    return k / denominator, (k + ell + 1) / denominator


def closed_form(j):
    k = Fraction(1, 2 ** (j + 3) - 2)
    return k, 1 - (j + 2) * k


def crossing(j):
    q = 2 ** (j + 2)
    return Fraction(q, (j + 1) * q + 2)


def allowance(j, v):
    k, ell = closed_form(j)
    return k / v - (1 + k - ell) + v / 4


def main():
    pairs = [(Fraction(1, 6), Fraction(2, 3))]
    for _ in range(5):
        pairs.append(a_process(*pairs[-1]))
    assert pairs == [closed_form(j) for j in range(6)]

    q_star = Fraction(351, 10304)
    gamma = Fraction(1, 2) + 2 * q_star
    assert gamma == Fraction(2927, 5152)
    assert crossing(4) == Fraction(32, 161)
    assert 4 * q_star < crossing(4)
    assert Fraction(1, 8) < 4 * q_star

    cuts = [Fraction(1, 8), *(crossing(j) for j in range(5, 0, -1))]
    cuts.append(Fraction(1, 2))
    rows = []
    for j, left, right in zip(range(5, -1, -1), cuts, cuts[1:]):
        left_value, right_value = allowance(j, left), allowance(j, right)
        assert left < right
        assert max(left_value, right_value) <= q_star
        if j:
            assert right_value == allowance(j - 1, right)
        rows.append(
            {
                "pair_index": j,
                "left": str(left),
                "right": str(right),
                "g_at_left": str(left_value),
                "g_at_right": str(right_value),
            }
        )
    for j in range(1, 6):
        assert allowance(j, crossing(j)) == crossing(j) / 4 - Fraction(
            1, 2 ** (j + 2)
        )
    assert allowance(4, crossing(4)) == q_star

    # Finite base cases for the pen-and-paper monotonicity argument.
    q4 = 2**6
    assert q4 - 1 > 2 * (5 + Fraction(2, q4)) * (6 + Fraction(1, q4))
    assert 2**7 - 1 >= 2 * 7 * 8

    drift = Fraction(1, 10000)
    sigma_slack = q_star - drift / 4
    head_slack = q_star - Fraction(1, 32) - 7 * drift / 32
    assert sigma_slack > Fraction(1, 32)
    assert head_slack > Fraction(1, 512)
    assert Fraction(1, 16) - Fraction(1, 256) > Fraction(1, 32)
    assert Fraction(1, 6) - Fraction(9, 32) < -Fraction(1, 32)
    assert Fraction(1, 6) - Fraction(9, 64) - (1 - drift) / 16 < -Fraction(
        1, 32
    )
    assert -1 - Fraction(9, 32) + Fraction(17, 32) < -Fraction(1, 2)

    rho = Fraction(4, 7) - gamma
    power = min(rho / 32, Fraction(1, 4096))
    allowed_drift = min(drift, rho / 16)
    assert 0 < rho < Fraction(7, 12) - gamma
    assert rho / 16 - allowed_drift / 16 > power
    print(
        json.dumps(
            {
                "q_star": str(q_star),
                "gamma": str(gamma),
                "finite_endpoint_rows": rows,
                "head_slack": str(head_slack),
                "sigma_slack": str(sigma_slack),
                "milestone_y0": "4/7",
                "milestone_rho": str(rho),
                "milestone_power": str(power),
                "milestone_clock_tolerance": str(allowed_drift),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
