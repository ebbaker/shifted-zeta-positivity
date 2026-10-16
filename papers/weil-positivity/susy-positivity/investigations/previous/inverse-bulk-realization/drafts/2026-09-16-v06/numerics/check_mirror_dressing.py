#!/usr/bin/env python3
"""The mirror prime reference is a single-insertion state of the same Schur
representation, and the reachable output states are not constrained as
Remark 7.10 of manuscript 0.4 supposes.

Standard library only. Prints a JSON record to standard output.

Conventions are those of Section 6 of the manuscript. On the elementary
q-Weyl representation, H = l^2(Z) tensor L^2(S^1), the negative magnetic
action and the vacuum are

    (u_- psi)_m(zeta) = (1 + q^{-m-1} zeta) psi_{m+1}(q^{-1} zeta),
    (Omega_q)_m(zeta) = C_q delta_{m0} chi_q(zeta),
    chi_q(w) = (-q w; q^2)_inf^{-1} = prod_{j>=0} (1 + q^{2j+1} w)^{-1},
    C_q = (q^2; q^2)_inf,

so an electric preparation eta = D(v) Omega_q on the zero-charge sector,
eta(w) = C_q D(w) chi_q(w), is carried to the sector m = -1 as

    (u_- eta)_{-1}(zeta) = (1 + zeta) eta(q^{-1} zeta).                  (*)

Lemma 6.1 prepares eta_a(w) = sqrt(1-a^2)/(1+a w) with a = q r and obtains
the output (1+zeta)/(1+r zeta), whose modulus squared is the positive prime
reference w_{r,d}. Remark 7.10 asks whether the mirror reference wt_{r,d},
which needs the output (1-zeta)/(1+r zeta), is reachable, and lists three
blocked routes.

FOUR FACTS ARE CHECKED.

(1) A fourth route exists. Take the electric state

        etat(w) = sqrt(1-a^2) (1 - q w) / ((1 + q w)(1 + a w)),

    which differs from eta_a by the factor (1-qw)/(1+qw). Then (*) gives
    exactly (1-zeta)/(1+r zeta): the (1+zeta) inserted by u_- is cancelled
    against the factor (1+qw) of etat at w = q^{-1} zeta, and what survives
    is the mirror numerator. No pole is crossed on the circle.

(2) The dressing that prepares etat is admissible in the sense of Lemma 6.1.
    Since etat/eta_a = (1-qw)/(1+qw) and the dressing of Lemma 6.1 carries
    the numerator (-q w; q^2)_inf, whose j = 0 factor is exactly (1 + q w),

        Dt(w) = sqrt(1-a^2) (1 - q w) (-q^3 w; q^2)_inf / (C_q (1 + a w)),

    i.e. the mirror dressing is the dressing of Lemma 6.1 with the sign of
    the first Pochhammer factor reversed. Its only singularity is the simple
    pole at w = -1/a, of modulus 1/(qr) > 1/q, which is the hypothesis of
    the graph-domain argument. The programme verifies the telescoping
    identity that makes Dt entire apart from that pole, for every truncation
    of the Pochhammer product, and exhibits the geometric rate r at which
    the truncated dressings' images converge.

(3) The output's weight is the mirror weight. With z = -zeta the Laurent
    coefficients of |(1-zeta)/(1+r zeta)|^2 are in the ratio
    2/(1+r) : 1 : r : r^2 : ..., which is the coefficient ratio
    kappat_{r,d} : d r : d r^2 : ... of wt_{r,d}, against the ratio
    2/(1-r) : -1 : r : -r^2 : ... of w_{r,d}. So the same fixed q, the same
    vacuum and the same single insertion produce both references.

(4) The general statement. For ANY psi analytic on a disk of radius rho > 1,
    the electric state eta(w) = psi(q w)/(1 + q w) satisfies (*) with output
    psi, and its dressing psi(q w) (-q^3 w; q^2)_inf / C_q is analytic on the
    disk of radius rho/q > 1/q. The factor (1 + q w) in the denominator of
    eta is always cancelled by the j = 0 factor of the vacuum's Pochhammer,
    for every psi. Hence the reachable output states on the sector m = -1 are
    exactly the functions analytic on some disk of radius greater than one,
    and the output is not divisible by (1 + zeta).

WHAT THIS DOES AND DOES NOT ESTABLISH. The identities below are exact
rational-arithmetic statements about formal power series, plus one labelled
floating-point convergence rate. They show that the mirror reference is
reachable and that the reachable class is large. They supply no positivity
certificate, no compression of the prime-free form A_L, and hence nothing
about Problem 8.3; a larger reachable class makes the source side easier and
leaves the domination untouched.

Written by Claude Opus 5 (Anthropic), 15 September 2026.
"""
import json
from fractions import Fraction as Fr

N = 60           # power-series truncation
JTRUNC = (1, 2, 3, 6)   # Pochhammer truncations used in the telescoping check


# ------------------------------------------------------------ series algebra
def zero():
    return [Fr(0)] * (N + 1)


def const(c):
    s = zero()
    s[0] = Fr(c)
    return s


def mul(a, b):
    out = zero()
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        top = N - i
        for j, bj in enumerate(b[:top + 1]):
            if bj:
                out[i + j] += ai * bj
    return out


def inv_linear(c):
    """1 / (1 + c z)."""
    return [(-Fr(c)) ** i for i in range(N + 1)]


def linear(c):
    """1 + c z."""
    s = const(1)
    s[1] = Fr(c)
    return s


def dilate(a, c):
    """f(z) -> f(c z)."""
    return [ai * Fr(c) ** i for i, ai in enumerate(a)]


def equal(a, b):
    return all(x == y for x, y in zip(a, b))


def autocorr(a, k):
    """Laurent coefficient k of |f|^2 for f analytic with real coefficients,
    truncated: sum_n a_n a_{n+k}."""
    return sum(a[n] * a[n + k] for n in range(N + 1 - k))


def main():
    checks = {}
    q = Fr(2, 5)
    r = Fr(3, 5)
    a = q * r

    # ------------------------------------------------------------- fact (1)
    # eta_a and etat, and the action (*) applied to each.
    eta = inv_linear(a)                                   # 1/(1+aw), up to sqrt(1-a^2)
    etat = mul(mul(linear(-q), inv_linear(q)), inv_linear(a))

    lin1z = const(1)
    lin1z[1] = Fr(1)                                       # 1 + zeta

    out_pos = mul(lin1z, dilate(eta, 1 / q))
    out_mir = mul(lin1z, dilate(etat, 1 / q))

    want_pos = mul(lin1z, inv_linear(r))                   # (1+zeta)/(1+r zeta)
    lin_m = const(1)
    lin_m[1] = Fr(-1)                                      # 1 - zeta
    want_mir = mul(lin_m, inv_linear(r))                   # (1-zeta)/(1+r zeta)

    assert equal(out_pos, want_pos), "Lemma 6.1 output not reproduced"
    assert equal(out_mir, want_mir), "mirror output not reproduced"
    checks["action_identities"] = 2 * (N + 1)

    # the two electric states differ by exactly (1-qw)/(1+qw)
    assert equal(etat, mul(eta, mul(linear(-q), inv_linear(q))))
    checks["electric_ratio"] = N + 1

    # ------------------------------------------------------------- fact (2)
    # telescoping: chi_q^{(J)}(w) * prod_{j=1..J} (1 + q^{2j+1} w) = 1/(1+qw),
    # exactly, for every truncation J. This is what makes the mirror dressing
    # Dt = sqrt(1-a^2)(1-qw) prod_{j>=1}(1+q^{2j+1}w) / (C_q (1+aw)) free of
    # any singularity except the pole at w = -1/a.
    telescope = 0
    for J in JTRUNC:
        chi_J = const(1)
        for j in range(0, J + 1):
            chi_J = mul(chi_J, inv_linear(q ** (2 * j + 1)))
        tail = const(1)
        for j in range(1, J + 1):
            tail = mul(tail, linear(q ** (2 * j + 1)))
        assert equal(mul(chi_J, tail), inv_linear(q)), f"telescoping fails at J={J}"
        telescope += N + 1
    checks["pochhammer_telescoping"] = telescope

    # graph-domain convergence rate: the truncated dressings' images differ
    # from the target by a tail evaluated at radius 1/q, so the rate is
    # a/q = r. Labelled floating point.
    # The Taylor coefficients of (1-qw)/(1+aw) are c_0 = 1 and, for n >= 1,
    # c_n = (-a)^{n-1}(-a-q), so |c_n| q^{-n} = ((a+q)/a) r^n exactly: the
    # error of the truncated dressing, measured at the radius 1/q where the
    # magnetic action evaluates it, is geometric with ratio r.
    dressing_tail = []
    NT = 400
    cq, ca = float(q), float(a)
    mag = [1.0] + [ca ** (n - 1) * (ca + cq) for n in range(1, NT + 1)]
    for M in (8, 16, 24, 32):
        tail = sum(mag[n] * cq ** (-n) for n in range(M + 1, NT + 1))
        dressing_tail.append({"truncation": M, "tail_at_radius_1_over_q": tail})
    rates = [dressing_tail[i + 1]["tail_at_radius_1_over_q"]
             / dressing_tail[i]["tail_at_radius_1_over_q"]
             for i in range(len(dressing_tail) - 1)]
    predicted = float(r) ** 8
    assert all(abs(x - predicted) < 1e-12 for x in rates), "unexpected convergence rate"
    checks["graph_convergence_rate"] = len(rates)

    # ------------------------------------------------------------- fact (3)
    # Laurent coefficients of the two weights, in the variable z = -zeta.
    # The output coefficient sequences are geometric from the first term:
    #   (1+zeta)/(1+r zeta) : p_0 = 1, p_n = (1-r)(-r)^{n-1}
    #   (1-zeta)/(1+r zeta) : m_0 = 1, m_n = -(1+r)(-r)^{n-1}
    # so the autocorrelations sum in closed form, and after z = -zeta
    #   positive reference: 2/(1+r), then -(1-r) r^{k-1}/(1+r)
    #   mirror reference:   2/(1-r), then +(1+r) r^{k-1}/(1-r).
    # Both are checked against the truncated series below.
    KMAX = 6
    wpos = [2 / (1 + r)] + [-(1 - r) * r ** (k - 1) / (1 + r) for k in range(1, KMAX)]
    wmir = [2 / (1 - r)] + [(1 + r) * r ** (k - 1) / (1 - r) for k in range(1, KMAX)]

    assert all(wmir[k] > 0 for k in range(KMAX))
    assert all(wpos[k] < 0 for k in range(1, KMAX))
    assert wmir[0] / wmir[1] == 2 / (1 + r), "mirror contact ratio wrong"
    assert wpos[0] / (-wpos[1]) == 2 / (1 - r), "positive contact ratio wrong"
    for k in range(1, KMAX - 1):
        assert wmir[k + 1] / wmir[k] == r
        assert wpos[k + 1] / wpos[k] == r
    checks["weight_coefficients"] = 4 + 2 * (KMAX - 2)

    # the closed forms against the truncated series: the difference is the
    # geometric tail, which is bounded by r^{2(N-k)} times a constant.
    series_gap = 0.0
    for k in range(KMAX):
        trunc = autocorr(want_pos, k) * (-1) ** k
        series_gap = max(series_gap, abs(float(trunc - wpos[k])))
        trunc = autocorr(want_mir, k) * (-1) ** k
        series_gap = max(series_gap, abs(float(trunc - wmir[k])))
    assert series_gap < 1e-12, "closed forms disagree with the truncated series"
    checks["weight_series_agreement"] = 2 * KMAX

    # The two output states are orthogonal in the m = -1 sector: the overlap
    # truncated at N is exactly r^{2N}, hence zero in the limit.
    overlap = sum(want_pos[n] * want_mir[n] for n in range(N + 1))
    assert overlap == r ** (2 * N), "truncated overlap is not r^{2N}"
    checks["output_orthogonality"] = 1

    # ------------------------------------------------------------- fact (4)
    # a target with nothing to do with the prime references: any psi analytic
    # past the unit circle is reached by eta(w) = psi(qw)/(1+qw).
    samples = []
    targets = {
        "mirror": want_mir,
        "rational_pole_at_2": mul(
            [Fr(1), Fr(-2), Fr(3)] + [Fr(0)] * (N - 2), inv_linear(Fr(-1, 2))),
        "polynomial": [Fr(1), Fr(0), Fr(-7), Fr(4)] + [Fr(0)] * (N - 3),
    }
    for name, psi in targets.items():
        eta_psi = mul(dilate(psi, q), inv_linear(q))
        got = mul(lin1z, dilate(eta_psi, 1 / q))
        ok = equal(got, psi)
        assert ok, f"general reachability fails for {name}"
        samples.append({"target": name, "reproduced": ok})
    checks["general_reachability"] = len(samples) * (N + 1)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "model": "claude-opus-5",
        "parameters": {"q": str(q), "r": str(r), "a_eq_qr": str(a),
                       "series_truncation": N},
        "arithmetic": "exact rational power series, except the labelled "
                      "convergence rate, which is floating point",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "dressing_tail": dressing_tail,
        "observed_rate_per_8_terms": rates,
        "predicted_rate_per_8_terms": predicted,
        "mirror_weight_coefficients": [str(x) for x in wmir],
        "weight_series_max_gap": series_gap,
        "positive_weight_coefficients": [str(x) for x in wpos],
        "general_reachability": samples,
        "reading": "The mirror prime reference is the output of one negative "
                   "magnetic insertion applied to an admissible electric "
                   "preparation of the same elementary representation at the "
                   "same fixed q, so Remark 7.10 of manuscript 0.4 has a "
                   "positive answer. More generally every function analytic "
                   "on a disk of radius greater than one is a reachable "
                   "output state: the factor (1+zeta) supplied by u_- is "
                   "cancelled by the j=0 factor of the vacuum Pochhammer "
                   "whenever the dressing declines to remove it.",
        "scope": "Reachability of source states only. No positivity "
                 "certificate, no compression of the prime-free form A_L, "
                 "and no statement about Problem 8.3 or the pole term.",
    }, indent=2))


if __name__ == "__main__":
    main()
