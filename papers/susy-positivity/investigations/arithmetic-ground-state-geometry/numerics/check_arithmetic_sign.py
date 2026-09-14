#!/usr/bin/env python3
"""Small exact checks for note 20; no sampled arithmetic positivity test.

The Green kernel is checked against an independent hyperbolic expression.
Finite counterexamples are evaluated on explicit vectors. Analytic domain,
essential-norm and infinite-tail proofs are not certified by this program.
"""
import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path

from check_joint_response import (
    add, blocks, eye, inv, mat, mul, positive, rational_rows,
    require, scale, sub, tr, zeros,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []

    def checked(name, evidence):
        checks.append({'name': name, 'status': 'passed', 'evidence': evidence})

    cases = 0
    for a in (F(1, 2), F(5, 2), F(9, 2)):
        for r, ux, uy in ((F(1, 4), F(3, 4), F(1, 2)),
                          (F(1, 9), F(2, 3), F(1, 3)),
                          (F(1, 16), F(1, 2), F(1, 4))):
            # ux=e^{-ax}, uy=e^{-ay}, r=e^{-aL}, x<y.
            cx = (ux + 1/ux)/2
            cy_right = (r/uy + uy/r)/2
            sinh_l = (1/r-r)/2
            rn = cx*cy_right/(a*sinh_l)
            rf = uy/(2*a*ux)
            vx, vy = r/ux, r/uy
            boundary = (ux*uy+vx*vy+r*(ux*vy+vx*uy))/(1-r*r)
            require(2*a*(rn-rf) == boundary, 'Independent Green kernel')
            coeff = scale(1/(1-r*r), mat([[1, r], [r, 1]]))
            require(positive(coeff), 'Positive rank-two coefficient')
            # Derivatives in x at x=0 and x=L; free kernel is differentiated
            # on the appropriate side of y. Smooth boundary term has no jump.
            dleft = (-a*uy+a*r*vy+r*(-a*vy+a*r*uy))/(1-r*r)
            dright = (-a*r*uy+a*vy+r*(-a*r*vy+a*uy))/(1-r*r)
            require(uy/2+dleft/(2*a) == 0, 'Left Neumann derivative')
            require(-vy/2+dright/(2*a) == 0, 'Right Neumann derivative')
            cases += 1
    checked('neumann_free_boundary_kernel',
            f'{cases} rational exponential-coordinate cases compare the independent '
            'hyperbolic Green kernel, rank-two correction and both boundary derivatives.')

    cases = 0
    for sigma in (-1, 1):
        for tau in (-1, 1):
            a, r, wi2, wj2 = F(5, 2), F(1, 7), F(9), F(16)
            li, lj = a*(1-sigma*r)/(a*a+wi2), a*(1-tau*r)/(a*a+wj2)
            coeff = scale(1/(1-r*r), mat([[1, r], [r, 1]]))
            direct = mul(mul(mat([[li, sigma*li]]), coeff),
                         mat([[lj], [tau*lj]]))[0][0]
            expected = (2*a*a*(1-sigma*r)/((a*a+wi2)*(a*a+wj2))
                        if sigma == tau else F(0))
            require(direct == expected, 'Parity matrix coefficient')
            column = mul(coeff, mat([[lj], [tau*lj]]))
            require(column == scale(a/(a*a+wj2), mat([[1], [tau]])),
                    'Boundary column cancellation')
            cases += 1
    checked('parity_and_boundary_columns',
            f'{cases} parity pairs check the rank-two Gram against the integrated '
            'cosine-column formula; no numerical cosine integrals are substituted.')

    samples = []
    for ell in (0, 1, 2, 5, 12, 30):
        a = 1-F(1, 2**(ell+2))
        w = mat([[a, 1], [1, 1]])
        require(positive(add(w, eye(2))), 'Positive shifted reference')
        partial = sum((F(1, 2)**(j+1) for j in range(ell+1)), F(0))
        witness = mat([[1], [-1]])
        value = mul(mul(tr(witness), w), witness)[0][0]
        require(a-partial == -value == F(1, 2**(ell+2)),
                'Truncated positivity and exact negative witness')
        require(value < 0, 'Negative target witness')
        samples.append({'ell': ell, 'partial_schur': str(a-partial),
                        'full_negative_value': str(value)})
    checked('positive_truncated_schur_negative_target', samples)

    x = mat([[1, 0], [0, F(1, 4)]])
    y = mat([[1, 1], [1, 1]])
    jordan = add(mul(x, y), mul(y, x))
    determinant = jordan[0][0]*jordan[1][1]-jordan[0][1]**2
    witness = mat([[1], [-2]])
    require(determinant == F(-9, 16), 'Jordan determinant')
    require(mul(mul(tr(witness), jordan), witness)[0][0] == -1,
            'Mixed-word negative witness')
    require(mul(mul(x, y), x) == mul(mat([[1], [F(1, 4)]]),
                                                  mat([[1, F(1, 4)]])),
            'Grouped sandwich is a Gram')
    checked('noncommuting_word_sign_obstruction',
            {'jordan_matrix': rational_rows(jordan), 'determinant': str(determinant),
             'negative_value': '-1', 'grouped_sandwich': 'exact rank-one Gram'})

    h = mat([[4, 1], [1, 3]])
    lam = mat([[2, 0], [0, 2]])
    b = mat([[1, 2], [3, -1]])
    trial = mat([[F(1, 4), 0], [0, F(1, 4)]])
    require(positive(h) and positive(sub(h, lam)), 'Known positive comparison')
    residual = sub(b, mul(h, trial))
    u = sub(add(mul(tr(b), trial), mul(tr(trial), b)),
            mul(mul(tr(trial), h), trial))
    exact = mul(mul(tr(b), inv(h)), b)
    remainder = mul(mul(tr(residual), inv(h)), residual)
    upper = add(u, mul(mul(tr(residual), inv(lam)), residual))
    require(exact == add(u, remainder), 'Mixed residual identity')
    require(positive(sub(upper, exact)), 'Weighted residual upper bound')
    checked('mixed_response_residual_identity',
            {'exact_response': rational_rows(exact),
             'residual_upper_bound': rational_rows(upper),
             'comparison': 'H-Lambda positive; upper minus exact positive'})

    # Galerkin subspace is the first high coordinate. Its residual is supported
    # only on the second coordinate, permitting the sharper d_K tail bound.
    galerkin = mat([[F(1, 4), F(1, 2)], [0, 0]])
    rg = sub(b, mul(h, galerkin))
    require(rg[0] == [0, 0], 'Galerkin orthogonality')
    gvalue = mul(tr(b), galerkin)
    require(gvalue == mul(mul(tr(galerkin), h), galerkin),
            'Galerkin response energy')
    gupper = add(gvalue, scale(F(1, 2), mul(tr(rg), rg)))
    require(sub(gupper, exact) == scale(F(3, 22), mul(tr(rg), rg)),
            'Entire omitted-mode residual accounted for')
    checked('galerkin_residual_tail',
            {'residual': rational_rows(rg),
             'upper_minus_exact': '3/22 times the residual Gram; positive semidefinite'})

    # A nonconstant diagonal inverse makes the mode-tail inequality nontrivial.
    rows = mat([[1, 2], [2, -1], [1, 1]])
    dinv = mat([[F(1, 2), 0, 0], [0, F(1, 5), 0], [0, 0, F(1, 9)]])
    whole = mul(mul(tr(rows), dinv), rows)
    low = mul(tr(rows[:1]), rows[:1])
    gram = mul(tr(rows), rows)
    tail_upper = add(scale(F(1, 2), low), scale(F(1, 5), sub(gram, low)))
    last_gram = mul(tr(rows[2:]), rows[2:])
    require(sub(tail_upper, whole) == scale(F(4, 45), last_gram),
            'Full-Gram mode-tail estimate')
    checked('mode_tail_uses_full_residual_gram',
            'An exact three-row example retains the omitted Gram and gives '
            'upper minus exact = (4/45) times the final-row Gram.')

    low_block = mat([[F(1, 2), 0], [0, 1]])
    schur = sub(low_block, exact)
    shifts = []
    for alpha in (F(8), F(9), F(12)):
        v = inv(add(h, scale(alpha, eye(2))))
        m = add(low_block, scale(alpha, eye(2)))
        t = blocks(m, tr(b), b, add(h, scale(alpha, eye(2))))
        require(positive(t), 'Shifted full reference')
        g = sub(m, mul(mul(tr(b), v), b))
        defect = add(scale(alpha, eye(2)), mul(mul(tr(b), sub(inv(h), v)), b))
        require(positive(g) and positive(defect), 'Positive Gram and defect')
        require(sub(g, defect) == schur, 'Reference shift leaves sign unchanged')
        shifts.append(str(alpha))
    require(schur[0][0] < 0, 'Shift control has a negative target')
    checked('reference_shift_cancels_from_schur',
            {'shifts': shifts, 'unchanged_schur': rational_rows(schur)})

    # Laurent coefficients in z=e^{r/2}: poles 2(z+z^{-1}),
    # prime density -2z, lowest-gamma off-diagonal -z^{-1} on the full line
    # or -2z^{-1} in the positive-r correlation integral.
    poles = {1: F(2), -1: F(2)}
    density = {1: F(-2), -1: F(0)}
    lowest_gamma = {1: F(0), -1: F(-2)}
    require(all(poles[e]+density[e]+lowest_gamma[e] == 0 for e in (-1, 1)),
            'Exact density, pole and lowest-gamma cancellation')
    checked('density_pole_lowest_gamma_cancellation',
            'Both Laurent coefficients cancel exactly; the surviving scalar '
            'coefficient is 4+w_0 and all higher gamma masses remain.')

    exp_lower = sum((F(11, 10)**j/F(factorial(j)) for j in range(7)), F(0))
    h8 = sum((F(1, j) for j in range(1, 9)), F(0))
    require(exp_lower > 3 and h8-F(11, 5) == F(29, 56) > F(1, 2),
            'Euler constant lower bound via log 9')
    pi_lower = 4*sum((F((-1)**j, 2*j+1) for j in range(8)), F(0))
    require(pi_lower > 3, 'Pi lower alternating integral')
    # n! >= 2^(n-1) for n>=2; strict at n=3 implies e<3.
    require(factorial(3) > 2**2, 'Strict exponential-series upper comparison')
    a1 = F(5, 2)
    tower_upper = 2/a1**3+1/(2*a1**2)
    require(tower_upper == F(26, 125), 'Infinite gamma tail integral bound')
    bound = -1+tower_upper*F(22, 7)**2/4
    require(bound == F(-2979, 6125) < 0, 'Continuum negative witness bound')
    checked('rational_density_obstruction',
            {'gamma_lower': '29/56', 'higher_mass_derivative_bound': str(tower_upper),
             'length': '2', 'unit_witness': 'cos(pi*x/2) on (-1,1)',
             'strict_quadratic_upper_bound': str(bound),
             'scope': 'Smooth-density control, not the arithmetic Weil form.'})

    record = {'status': 'passed', 'arithmetic': 'exact fractions; Python standard library',
              'checks': checks,
              'limitation': 'Finite identities and rational inequalities only. '
                            'No analytic proof certification or arithmetic positivity claim.'}
    encoded = json.dumps(record, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x') as stream:
            stream.write(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
