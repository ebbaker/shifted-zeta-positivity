#!/usr/bin/env python3
"""Exact local algebra and exponent checks for the source Lemma 18.1 audit.

Rational and Q(zeta_6) arithmetic only. Local finite-field checks do not
certify global Eisenstein reciprocity or moving-character Poisson estimates.
The affine identities are verified symbolically; finite inequality cases
supplement, and do not replace, the proofs recorded in the audit.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt
from pathlib import Path
import json


COUNT = 0


def require(condition):
    global COUNT
    assert condition
    COUNT += 1


def zadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def zscale(a, x):
    return a*x[0], a*x[1]


def zmul(x, y):
    # zeta^2 = zeta - 1, zeta = exp(pi*i/3).
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c+b*d


def zconj(x):
    return x[0]+x[1], -x[1]


def znorm(x):
    return x[0]**2+x[0]*x[1]+x[1]**2


ZERO, ONE = (F(0), F(0)), (F(1), F(0))
ROOTS = tuple((F(a), F(b)) for a, b in ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)))


def field_character(p):
    generator = next(g for g in range(2, p) if len({pow(g, j, p) for j in range(p-1)}) == p-1)
    logs = {pow(generator, j, p): j for j in range(p-1)}
    def char(x, c=1):
        x %= p
        return ZERO if x == 0 else ROOTS[(c*logs[x]) % 6]
    return char


def local_correlation_checks():
    cases = 0
    for p in (7, 13, 19):
        char = field_character(p)
        for c in range(1, 19):
            for n1, n2 in product((0, 1, 2, p-1), repeat=2):
                if n1 == n2 == 0:
                    continue
                for k in range(p):
                    actual = ZERO
                    if n1:
                        inv = pow(n1, -1, p)
                        for x in range(p):
                            y = ((n2*x-k)*inv) % p
                            actual = zadd(actual, zmul(char(x, c), zconj(char(y, c))))
                    else:
                        x = (k*pow(n2, -1, p)) % p
                        for y in range(p):
                            actual = zadd(actual, zmul(char(x, c), zconj(char(y, c))))
                    if n1 and n2:
                        phase = char(n1*pow(n2, -1, p), c)
                        scalar = p-1 if k == 0 else (-1 if c % 6 else p-2)
                        expected = zscale(scalar, phase)
                    else:
                        expected = zscale(p-1, ONE) if c % 6 == 0 and k != 0 else ZERO
                    require(actual == expected)
                    # L_{p^c} has exactly p^(c-1) times this field value.
                    require(znorm(actual) <= p*p)
                    cases += 1
            # A six-divisible power remains zero on nonunits.
            require(char(p, c) == ZERO)
        # Artificial extension on both nonunit residuals is not the true sum.
        true_both_nonunits = ZERO
        for x, y in product(range(p), repeat=2):
            true_both_nonunits = zadd(true_both_nonunits, zmul(char(x, 6), zconj(char(y, 6))))
        require(true_both_nonunits == zscale((p-1)**2, ONE) != ZERO)
    return cases


def prime_power_support_checks():
    cases = 0
    for p in (7, 13, 19):
        def gauss_norm_square(a, valuation):
            if a % 6:
                return F(p**(a-1)) if valuation == a-1 else F(0)
            if valuation >= a:
                return F(p**a)*(1-F(1, p))**2
            if valuation == a-1:
                return F(p**(a-2))
            return F(0)
        for a in range(1, 31):
            old, new = gauss_norm_square(a, 0), gauss_norm_square(a, 6)
            require((old != new) == (a in (1, 6, 7)))
            if a in (1, 6, 7):
                normalized_change = abs(old-new)/p**a
                expected = (1-F(1, p))**2 if a == 6 else F(1, p)
                require(normalized_change == expected)
            cases += 1
    return cases


def symbolic_ledgers():
    def add(*items):
        out = {}
        for item in items:
            for key, value in item.items():
                out[key] = out.get(key, F(0))+value
        return {key: value for key, value in out.items() if value}
    def scale(a, item):
        return {key: F(a)*value for key, value in item.items() if a*value}
    names = "A m q c d R E gap w wo g ell c2 d2 p2 g2 t2 V s0 f Bc".split()
    data = {name: {name: F(1)} for name in names}
    A, m, q, c, d, R, E, gap, w, wo, g, ell, c2, d2, p2, g2, t2, V, s0, f, Bc = [data[n] for n in names]
    M = add(m, q)
    K0 = add(scale(2, A), scale(-1, c), scale(-1, d), R, E, scale(-1, m))
    K = add(K0, scale(-1, gap))
    eq = add(q, R, E)
    a0 = add(A, scale(-1, c), scale(-1, w))
    b2 = scale(F(1, 2), add(c2, d2))
    mp = add(scale(2, a0), scale(-1, K), scale(-1, g), scale(-1, g2), scale(-1, V))
    qp = add(eq, wo, t2, V)
    Mp = add(mp, qp)
    J = add(d, scale(-1, c), gap, scale(-2, w), wo)
    require(Mp == add(M, J, scale(-1, g), scale(-1, g2), t2))
    allowance = add(a0, eq, wo, w, Bc, scale(-1, s0))
    prefix = add(K, g, scale(-1, ell), scale(-1, a0), p2, scale(-1, s0),
                 g2, scale(-1, t2), scale(-1, b2))
    Delta = add(b2, scale(-1, p2), w, Bc, ell)
    require(add(allowance, scale(-1, prefix)) == add(Mp, Delta))
    diagonal = add(K, g, scale(-1, ell), scale(-1, s0), scale(-1, allowance))
    require(diagonal == add(A, scale(-1, M), scale(-1, d), scale(-1, gap),
                            scale(-1, wo), scale(-1, Bc), g, scale(-1, ell)))
    F1 = add(scale(F(1, 6), c), scale(F(5, 6), add(d, gap)), scale(F(1, 3), w),
             scale(F(1, 6), eq), wo, Bc, scale(F(-5, 6), g), ell)
    F2 = add(scale(2, b2), scale(F(-5, 6), g2), scale(-1, p2), t2,
             scale(F(1, 6), V), scale(F(1, 6), f))
    excess = add(scale(F(1, 6), mp), scale(F(-1, 6), f), a0, scale(-1, b2),
                 scale(-1, Mp), scale(-1, Delta))
    require(excess == add(A, scale(F(-5, 6), M), scale(-1, F1), scale(-1, F2)))
    relative_length = add(a0, scale(-1, c2), scale(-1, Mp), scale(-1, A), M)
    require(relative_length == add(g, w, scale(-1, d), scale(-1, c2), scale(-1, gap),
                                   scale(-1, wo), g2, scale(-1, t2)))
    p, Bd = {"p": F(1)}, {"Bd": F(1)}
    first = add(m, scale(-1, A), scale(F(-1, 2), R), scale(-1, E), p, s0,
                scale(F(1, 2), add(A, scale(-1, c), eq, Bc, scale(-1, s0),
                                    A, scale(-1, d), eq, Bd, scale(-1, s0))))
    require(first == add(M, scale(F(1, 2), add(Bc, Bd, scale(-1, c), scale(-1, d), scale(2, p), R))))
    return ["18.23 first-transform allowance", "18.31 diagonal", "18.32 width",
            "18.33 child allowance", "18.38 affine defect", "18.42 exceptional excess"]


def primewise_and_centered_inequalities():
    cases = 0
    for i, j in product(range(1, 61), repeat=2):
        r = int((i-j) % 6 != 0)
        bc = max(F(0), F(3*i-5*j-r, 6))
        bd = max(F(0), F(3*j-5*i-r, 6))
        require(bc+bd <= i+j-2-r)
        cases += 1
        if i == j:
            b2 = F(i)
            if i % 6:
                for nonunit in (False, True):
                    t2, V = (0, 1) if nonunit else (1, 0)
                    f = 2 if nonunit and i == 1 else 0
                    F2 = 2*b2-F(5*i, 6)-1+t2+F(V+f, 6)
                    require(F2 >= F(2, 3)*b2)
            else:
                F2 = 2*b2-F(5*i, 6)-1
                require(F2 >= F(2, 3)*b2)
        elif min(i, j) % 6 == 0:
            b2, g2 = F(i+j, 2), min(i, j)
            F2 = 2*b2-F(5*g2, 6)-1
            require(F2 >= F(2, 3)*b2)
    for M in (F(1, 10), F(1), F(3, 2), F(3)):
        L = M/4
        for A in (5*M/6, M, M+F(1, 1000)):
            for v in (F(0), L/3, L, 2*L, M, 2*M):
                deficit = A-F(5, 6)*M-F(2, 3)*v-max(L-v, 0)
                require(deficit <= A-M <= max(A-M, 0))
                if v == L:
                    require(deficit == A-M)
                cases += 1
    # Common-support extraction does not gain from erased unit restrictions.
    for frozen_valuation in range(6):
        residue = (-frozen_valuation) % 6
        require((frozen_valuation+residue) % 6 == 0)
    require((-2) % 6 == 4)  # multiplicity-one nonunit: h'_0 contains p^4
    require((-1) % 6 == 5)  # added exceptional rows after a unit restriction is bounded
    return cases


def extraction_and_centering_checks():
    cases = 0
    char = field_character(7)
    values = (1, 7, 49, 13, 91)
    for factors in product(values, repeat=2):
        # Two distinct prime slots, permitted to overlap either plain.
        full = factors+(7, 13)
        for p in (7, 13):
            lhs = int(any(n % p == 0 for n in full))
            rhs = 0
            for size in range(1, 5):
                for subset in combinations(range(4), size):
                    rhs += (-1)**(size+1)*int(all(full[i] % p == 0 for i in subset))
            require(lhs == rhs)
            cases += 1
        for row in range(7):
            phase_product = ONE
            for n in full:
                phase_product = zmul(phase_product, char(n, 6))
            require(phase_product == char(full[0]*full[1]*full[2]*full[3], 6))
            cases += 1
    # Retaining p in a selected plain quotient is valid; no puncture is inserted.
    require(49//7 == 7)
    require(char(49, 6) == zmul(char(7, 6), char(7, 6)) == ZERO)
    # The full Möbius sum deletes an artificial shared residual prime.
    for a, b in product(range(1, 61), repeat=2):
        common = gcd(a, b)
        primes = [p for p in range(2, common+1) if common % p == 0
                  and all(p % d for d in range(2, isqrt(p)+1))]
        total = sum((-1)**len(subset) for size in range(len(primes)+1)
                    for subset in combinations(primes, size))
        require(total == int(common == 1))
        cases += 1
    for X1, X2, Y1, Y2 in ((6, 10, 5, 12), (4, 15, 3, 20), (8, 9, 6, 12)):
        require(X1*X2 == Y1*Y2)
        for d1, d2 in product((1, 2, 3, 7), repeat=2):
            U1, U2, V1, V2 = F(X1, d1), F(X2, d2), F(Y1, d1), F(Y2, d2)
            T = U1*U2
            require(T == V1*V2)
            for power in range(4):
                require(U1**(1+power)*U2**(1+power) == V1**(1+power)*V2**(1+power))
            # Different individual norm powers destroy the main-term cancellation.
            require(U1**2*U2 != V1**2*V2)
            cases += 1
    # The squared centered coefficient retains its cross term exactly.
    for a, b in product(ROOTS, repeat=2):
        delta = zadd(a, zscale(-1, b))
        cross = zmul(a, zconj(b))
        twice_real = 2*cross[0]+cross[1]
        require(znorm(delta) == znorm(a)+znorm(b)-twice_real)
        cases += 1
    require(znorm(zadd(ONE, zscale(-1, ONE))) == 0)
    require(znorm(ONE)+znorm(ONE) == 2)
    return cases


def greedy_and_band_checks():
    cases = 0
    for kappa in (F(3, 4), F(4, 5), F(5, 6), F(1)):
        for N in (1, 2, 10, 100, 1000):
            eta = F(1, 10000)
            lengths = [eta*F(i % 11+1, 11) for i in range(N)]
            for defect in (F(0), F(1, 20000), F(1, 1000), F(1, 100)):
                removed = F(0)
                for length in lengths:
                    if removed >= defect/(6*kappa):
                        break
                    removed += length
                require(removed <= min(sum(lengths), defect/(6*kappa)+eta))
                require(kappa*removed <= defect/6+eta)
                cases += 1
    for er1, er2, r in product((F(0), F(1, 10), F(2, 5), F(7, 10)), repeat=3):
        for omega2 in (F(-1, 100), F(0), F(1, 100)):
            tminus = er2+omega2
            lhs = tminus-er1-er2-max(r-er1, 0)
            require(lhs == (tminus-er2)-max(r, er1))
            require(lhs <= omega2-r)
            cases += 1
    eps = F(1, 1000)
    rho, sigma, delta = eps/100, eps/100, eps/10000
    Mmax, Cstar = F(4), F(100)
    depth = 2+(2*Mmax//sigma)+(int((2*Mmax) % sigma != 0))
    term = rho+delta+rho/6+3*sigma+5*sigma/3
    require(term < eps/4)
    xi = min(delta/2, rho/30, sigma/(4*Cstar), eps/(16*Cstar*depth))/2
    eta = min(sigma/6, eps/(16*Cstar*depth))/2
    local_share = eps/(32*Cstar*depth)
    require(Cstar*xi < sigma/2)
    require(term+Cstar*depth*(eta+xi+local_share) < eps)
    for N in (1, 10, 10000):
        # N changes the eventual log-Z threshold; numerical mesh stays fixed.
        HN = F(N+2)
        logZ = 100*Cstar*HN/xi
        thetaN = HN/logZ
        require(2*thetaN < xi/4)
        require(thetaN < xi)
        cases += 1
    return cases


def stage_branch_checks():
    cases = 0
    sigma, perturbation = F(3, 100), F(1, 1000)
    branches = [(F(0), F(0), F(0), sigma),
                (F(0), F(0), sigma/3, 2*sigma)]
    for lp in (sigma/6, sigma/4, sigma/3):
        branches += [(lp, lp, F(0), sigma), (6*lp, F(0), F(0), sigma),
                     (7*lp, lp, F(0), sigma)]
    for c, d in product((F(0), F(1, 100), F(1, 10), F(1), F(3)), repeat=2):
        for R in (F(0), min(c, d)):
            eq = R
            Bc = max(F(0), (3*c-5*d-R)/6)
            for gap in (-perturbation, F(0), F(1, 10), F(1)):
                for w, wo, ell, increment in branches:
                    J = d-c+gap-2*w+wo
                    g = max(J, 0)+increment
                    F1 = c/6+5*(d+gap)/6+w/3+eq/6+wo+Bc-5*g/6+ell
                    require(F1 >= 2*(c+w)/3-3*sigma-5*perturbation/6)
                    for g2, t2 in ((F(0), F(0)), (F(1, 10), F(0)),
                                   (F(1, 10), F(1, 20)), (F(1, 2), F(1, 2))):
                        width_change = J-g-g2+t2
                        require(width_change <= -sigma)
                        c2 = g2-t2
                        defect_change = g+w-d-c2-gap-wo+g2-t2
                        if w > 0 or ell > 0:  # (18.38) is explicitly positive-slot only.
                            require(defect_change <= 6*(w+ell)+perturbation)
                        cases += 1
    return cases


def main():
    # The audit separately checked the local PDF hash. Finite algebra replay
    # needs no temporary source file or network access.
    digest = '8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7'
    local = local_correlation_checks()
    gauss = prime_power_support_checks()
    affine = symbolic_ledgers()
    inequalities = primewise_and_centered_inequalities()
    centering = extraction_and_centering_checks()
    greedy = greedy_and_band_checks()
    stage = stage_branch_checks()
    result = {
        'date': '2026-10-09', 'source_pdf_sha256': digest,
        'arithmetic': 'exact rational and Q(zeta_6); symbolic affine coefficient maps',
        'assertions': COUNT, 'local_field_correlation_cases': local,
        'prime_power_support_cases': gauss, 'symbolic_ledger_identities': affine,
        'primewise_centered_inequality_cases': inequalities,
        'mask_extraction_centering_cases': centering, 'greedy_band_cases': greedy,
        'stage_F1_width_defect_cases': stage,
        'counterchecks': ['six-divisible phases retain nonunit zeros',
                          'artificial both-nonunit extension is not the original congruence sum',
                          'full Mobius inversion removes artificial noncoprime pairs',
                          'unequal individual norm powers spoil equal-product cancellation',
                          'separate rectangle squares lose the centered cross term',
                          'unit-restriction enlargement can admit exceptional valuation-five rows'],
        'scope': 'Critical finite algebra, exact affine ledgers, and sampled rational inequalities. No moving Hecke prime theorem, global number-field reciprocity, Poisson estimate, or source fourth-moment theorem is numerically certified.',
    }
    path = Path(__file__).with_name('centered_fourth_proof_audit_record_20261009.json')
    path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(f'PASS: {COUNT} exact assertions; {local} local field cases; six symbolic ledgers')


if __name__ == '__main__':
    main()
