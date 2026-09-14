#!/usr/bin/env python3
"""Exact checks for notes 18–19; no full Weil positivity computation.

Uses rational arithmetic only. The finite matrices are deliberately
non-arithmetic controls, including a target with a negative direction.
"""
import argparse
from fractions import Fraction as F
import json
from math import comb, factorial
from pathlib import Path


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def zeros(n, m):
    return mat([[0] * m for _ in range(n)])


def tr(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inv(a):
    n = len(a)
    z = [row[:] + erow for row, erow in zip(a, eye(n))]
    for i in range(n):
        pivot = next((j for j in range(i, n) if z[j][i]), None)
        require(pivot is not None, "Singular exact matrix")
        z[i], z[pivot] = z[pivot], z[i]
        d = z[i][i]
        z[i] = [x / d for x in z[i]]
        for j in range(n):
            if j != i:
                d = z[j][i]
                z[j] = [x - d * y for x, y in zip(z[j], z[i])]
    return [row[n:] for row in z]


def positive(a):
    """Exact positive-definiteness check by scalar Schur elimination."""
    require(a == tr(a), "Expected symmetric matrix")
    a = [row[:] for row in a]
    while a:
        d = a[0][0]
        if d <= 0:
            return False
        a = [[a[i][j] - a[i][0] * a[0][j] / d
              for j in range(1, len(a))] for i in range(1, len(a))]
    return True


def blocks(a, b, c, d):
    return [x + y for x, y in zip(a, b)] + [x + y for x, y in zip(c, d)]


def conv(a, b, n):
    return [sum((a[j] * b[k-j] for j in range(k+1)
                 if j < len(a) and k-j < len(b)), F(0))
            for k in range(n+1)]


def rational_rows(a):
    return [[str(x) for x in row] for row in a]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []

    def checked(name, evidence):
        checks.append({"name": name, "status": "passed", "evidence": evidence})

    # Independent coefficient formula, recurrence and squared formal series.
    degree = 24
    coeff = [F(0)] + [F(comb(2*j, j), 4**j * (2*j-1))
                      for j in range(1, degree+2)]
    require(coeff[1] == F(1, 2), "Initial response coefficient")
    for j in range(1, degree+1):
        require(coeff[j+1] == coeff[j] * F(2*j-1, 2*j+2),
                "Response recurrence")
    root = [F(1)] + [-coeff[j] for j in range(1, degree+1)]
    require(conv(root, root, degree) ==
            [F(1), F(-1)] + [F(0)] * (degree-1), "Squared response series")
    checked("binomial_response_coefficients",
            "Closed coefficient formula and recurrence; square is 1-z through degree 24.")

    cases = 0
    for r in [F(1, 5), F(3, 5), F(4, 5)]:
        z = 1-r*r
        lam = 1/z
        for n in range(1, 13):
            rn = 1-sum((coeff[j]*z**j for j in range(1, n+1)), F(0))
            error = lam*(rn*rn-r*r)
            bound = 2*coeff[n+1]*z**n/(1-z)
            require(r <= rn <= 1 and 0 <= error <= bound,
                    "Finite response error bound")
            cases += 1
    checked("finite_response_positive_errors",
            f"{cases} exact rational cases with a rational square-root value; "
            "checks the residual and its stated bound, not convergence as an analytic theorem.")

    # A positive four-dimensional Gram with a genuinely coupled low/high split.
    # Low inputs are first; high output coordinates are first.
    hroot = mat([[F(3, 4), 0], [0, F(4, 3)]])
    troot = mat([[F(5, 4), 0], [0, F(5, 3)]])
    th = mul(troot, troot)
    h = mul(hroot, hroot)
    v = inv(th)
    hinv = inv(h)
    b = mat([[1, 2], [3, 1]])
    zcap = mat([[2, 1], [0, 1]])
    a = blocks(mul(inv(troot), b), troot, zcap, zeros(2, 2))
    t = mul(tr(a), a)
    require(positive(t) and th == add(h, eye(2)), "Positive reference and gap")
    w = sub(t, eye(4))
    tfb = sub(eye(4), scale(F(1, 2), inv(t)))
    afb = mul(a, tfb)
    require(mul(tr(afb), afb) == add(w, scale(F(1, 4), inv(t))),
            "Joint one-pass feedback")
    checked("joint_one_pass_feedback",
            "Full matrix feedback Gram equals T-I+(1/4)T^{-1}, with T strictly positive.")

    # Noncommuting resolvent word order, including the exact truncation remainder.
    t0 = mat([[3, 0], [0, 5]])
    kh = mat([[2, 1], [1, 2]])
    require(mul(t0, kh) != mul(kh, t0), "Control must not commute")
    v0 = inv(add(t0, scale(F(4), eye(2))))
    j = mul(v0, sub(scale(F(4), eye(2)), kh))
    vjoint = inv(add(t0, kh))
    partial, power = zeros(2, 2), eye(2)
    for _ in range(7):
        partial = add(partial, mul(power, v0))
        power = mul(power, j)
    require(sub(vjoint, partial) == mul(power, vjoint),
            "Noncommuting resolvent remainder")
    require(positive(kh) and positive(sub(scale(F(4), eye(2)), kh)),
            "Positive resolvent comparison")
    checked("ordered_mixed_response_words",
            "Noncommuting two-channel example verifies all words through order six "
            "and the exact ordered remainder.")

    ap = [row[:2] for row in a]
    ah = [row[2:] for row in a]
    pi_h = mul(mul(ah, v), tr(ah))
    zz = mul(sub(eye(4), pi_h), ap)
    g = mul(tr(zz), zz)
    m = mul(tr(ap), ap)
    require(mul(pi_h, pi_h) == pi_h and pi_h == tr(pi_h), "Range projection")
    require(mul(tr(ah), ap) == b, "Exact low/high coupling")
    require(mul(tr(ah), zz) == zeros(2, 2), "Unused output orthogonality")
    require(ap == add(mul(mul(ah, v), b), zz), "All low outputs retained")
    require(g == sub(m, mul(mul(tr(b), v), b)) and positive(g), "Positive low Gram")
    checked("orthogonal_low_output_retained",
            "Range projection, coupling, exact reconstruction and unused output Gram "
            "are checked before the new readout.")

    rr = mul(inv(troot), hroot)
    phi = blocks(mul(inv(hroot), b), hroot, zcap, zeros(2, 2))
    phi_formula = add(
        mul(mul(ah, rr), [row + erow for row, erow in zip(mul(hinv, b), eye(2))]),
        [row + [F(0), F(0)] for row in zz])
    dn = add(eye(2), mul(mul(tr(b), sub(hinv, v)), b))
    require(dn == add(eye(2), mul(mul(mul(tr(b), v), hinv), b)),
            "Inverse-difference defect")
    require(phi == phi_formula, "Actual source formula")
    require(mul(tr(phi), phi) == add(w, blocks(dn, zeros(2, 2),
                                             zeros(2, 2), zeros(2, 2))),
            "Full polarized finite-rank Gram identity")
    require(positive(dn), "Finite-rank defect positive")
    checked("finite_rank_completion",
            "Exact four-by-four polarized Gram identity, positive rank-two error, "
            "and all mixed entries preserved.")

    source_change = blocks(
        mul(mul(troot, sub(mul(rr, hinv), v)), b),
        mul(troot, sub(rr, eye(2))), zeros(2, 2), zeros(2, 2))
    require(sub(phi, a) == source_change, "Source correction formula")
    checked("source_difference_formula",
            "Checks both terms in formula (28), including the finite low/high correction.")

    sn = sub(g, dn)
    require(sn == sub(sub(m, eye(2)), mul(mul(tr(b), hinv), b)),
            "Remaining Schur matrix")
    p = mat([[0], [1]])
    witness = p + scale(-1, mul(mul(hinv, b), p))
    negative = mul(mul(tr(witness), w), witness)[0][0]
    require(negative == sn[1][1] < 0, "Deliberately negative target control")
    checked("completion_does_not_prove_positivity",
            {"non_arithmetic_control": True,
             "remaining_matrix": rational_rows(sn),
             "negative_quadratic_value": str(negative),
             "witness": rational_rows(witness),
             "positive_defect": rational_rows(dn)})

    # Elementary rational bounds used for the L=1 high-sector cutoff.
    log2_lower = 2*sum((F(1, 3**(2*j+1)*(2*j+1)) for j in range(4)), F(0))
    log2_upper = log2_lower + 2*F(1, 3**9*9)/(1-F(1, 9))
    require(log2_lower > F(6931, 10000) and log2_upper < F(7, 10),
            "Logarithm bounds")
    h256 = sum((F(1, k) for k in range(1, 257)), F(0))
    require(h256-8*F(6931, 10000) < F(58, 100), "Euler constant upper comparison")
    pi_lower = 4*sum((F((-1)**j, 2*j+1) for j in range(8)), F(0))
    require(pi_lower > 3, "Pi lower integral sum")
    # q(x)(1+x^2)-4=x^4(1-x)^4; integrate q to obtain 22/7.
    quotient = [F(4), F(0), F(-4), F(0), F(5), F(-4), F(1)]
    product = conv(quotient, [F(1), F(0), F(1)], 8)
    product[0] -= 4
    require(product == [F(0)]*4 + [F(1), F(-4), F(6), F(-4), F(1)],
            "Pi upper integral polynomial")
    require(sum((x/F(i+1) for i, x in enumerate(quotient)), F(0)) == F(22, 7),
            "Pi upper integral constant")
    exp_lower = sum((F(23, 20)**j/F(factorial(j)) for j in range(11)), F(0))
    require(exp_lower > F(22, 7), "Log pi upper comparison")
    sinh_sum = 2*sum((F(1, 2)**(2*j+1)/F(factorial(2*j+1))
                      for j in range(5)), F(0))
    sinh_next = 2*F(1, 2)**11/F(factorial(11))
    require(sinh_sum+sinh_next/(1-F(1, 624))-1 < F(43, 1000),
            "Pole negative eigenvalue bound")
    require(F(7, 5)**2 < 2 and F(7, 10)/F(7, 5) == F(1, 2),
            "Prime two bound")
    # log 3 > 1 proves that no other prime is active at L=1.
    log3_lower = 2*sum((F(1, 2)**(2*j+1)/F(2*j+1) for j in range(2)), F(0))
    require(log3_lower > 1, "Prime set at L=1")
    checked("elementary_constant_bounds",
            "Rational log, Euler-constant comparison, pi integral, exponential, "
            "sinh-tail and prime-two bounds justify beta_1.")

    beta_upper = (F(58, 100)+F(11, 7)+F(21, 10)+F(23, 20)
                  +F(43, 1000)+F(1, 2))
    b64 = sum((F(2)/(2*k+F(1, 2))*F(144)/((2*k+F(1, 2))**2+144)
               for k in range(64)), F(0))
    require(b64 > F(3007, 500), "Gamma partial-sum lower comparison")
    require(F(3007, 500)-beta_upper > F(1, 16), "High-sector gap")
    checked("rational_length_one_cutoff",
            {"L": "1", "N": 4, "delta": "1/16",
             "gamma_partial_sum_terms": 64, "frequency_squared_lower": "144",
             "gamma_partial_sum_lower": "3007/500",
             "beta_upper": str(beta_upper),
             "scope": "Coercivity on the cosine complement only; full Q_1 sign is not checked."})

    record = {
        "status": "passed",
        "arithmetic": "exact fractions; Python standard library",
        "checks": checks,
        "limitation": "Finite algebra, rational inequalities and a deliberately non-arithmetic "
                      "control. Not analytical proof certification, a physical normalization "
                      "law, full Weil positivity, or an RH result."
    }
    encoded = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as out:
            out.write(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
