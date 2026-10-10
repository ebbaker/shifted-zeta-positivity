#!/usr/bin/env python3
"""Exact rational controls for candidate localization and degree-six support.

These check finite algebra and the support of a necessary first-jet body.
They do not certify arithmetic candidates, imported analytic inputs, or an RH sign.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def support(a, b):
    assert a >= 0 and b >= 0
    return a + b*b/(4*a) if a > 0 and b <= 2*a else b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = 0
    families = {}

    def check(condition, family):
        nonlocal checks
        if not condition:
            raise AssertionError(f'{family}: control {checks+1} failed')
        checks += 1
        families[family] = families.get(family, 0)+1

    # Shifted quadratic identity without any square-root evaluation.
    for k in range(1, 121):
        gamma = F(k+3, 37)
        x2, y3, x4, payment = F(k-61, 13), F(k % 17-8, 7), F(19-k, 23), F(k, 101)
        K = 2*y3*y3 + 3*x2*x4 - gamma*x2*x2
        shifted = 2*y3*y3 + payment + 9*x4*x4/(4*gamma) - gamma*(x2-3*x4/(2*gamma))**2
        check(K+payment == shifted, 'curvature complete square')
        a, b3, b4 = abs(x2), abs(y3), abs(x4)
        check(K+payment <= 2*b3*b3 + 3*a*b4 + payment - gamma*a*a,
              'curvature unsigned outer enclosure')

    # Degenerate branches and exact maximizing necessary-body coordinates.
    values = [F(0), F(1, 11), F(1, 3), F(1), F(2), F(3), F(11)]
    for a in values:
        for b in values:
            upper = support(a, b)
            s = b/(2*a) if a > 0 and b <= 2*a else F(1)
            r = 1-s*s
            check(s*s + abs(r) == 1 and a*r+b*s == upper, 'sharp support attainment')
            check(upper <= a+b, 'slab comparison')
            # Exactly equivalent to h >= (sqrt(5)-1)(a+b)/2.
            check((2*upper+a+b)**2 >= 5*(a+b)**2, 'golden ratio lower comparison')
            if a > 0 and b <= 2*a:
                check(4*a*a*((2*upper+a+b)**2-5*(a+b)**2) == (b*b+2*a*b-4*a*a)**2,
                      'golden ratio equality polynomial')
            for j in range(41):
                y = F(j, 40)
                check(a*(1-y*y)+b*y <= upper, 'rational body support controls')
            check(support(a+F(1, 17), b) >= upper and support(a, b+F(1, 19)) >= upper,
                  'interval upper endpoint monotonicity')

    # Both signs, physical drift, and complete finite moment identity.
    for k in range(1, 121):
        eta, L, c = F(k+1, 503), F(k+21, 3), F(k+9, 41)
        drift, eps, gamma = F(k-60, 89), F(k-70, 97), F(k-40, 13)
        x0, x1, y1 = F(k-61, 17), F(k % 11-5, 19), F(k % 13-6, 23)
        x2, y3, x4 = F(k-57, 13), F(k % 17-8, 7), F(19-k, 23)
        y5, x6, y6 = F(k-45, 29), F(k-33, 31), F(k % 19-9, 37)
        z1 = y1+eps*x1
        e1 = drift*x0-c*z1
        K = 2*y3*y3+3*x2*x4-gamma*x2*x2
        J = K+x0*(gamma*x4-3*x6+2*eps*y6)-2*z1*y5
        H = 3*x6-gamma*x4-2*eps*y6
        R = H+2*drift*y5/c
        check(K-J == R*x0-2*y5*e1/c, 'candidate null physical drift identity')
        a, b = 2*L*abs(y5)/c, abs(R)
        curved = eta*support(a, b)/2
        slab = eta*(a+b)/2
        box = eta*abs(H)/2+(L+abs(drift))*eta*abs(y5)/c
        check(curved <= slab <= box, 'candidate null payment comparisons')
        for j in range(-8, 9):
            s = F(j, 8)
            for sign in (-1, 1):
                r = sign*(1-s*s)
                body_x0, body_e1 = eta*s/2, L*eta*r/2
                value = R*body_x0-2*y5*body_e1/c
                check(abs(value) <= curved, 'candidate null paid body controls')
        # Choose the maximizing signs for the actual frozen coefficients.
        s_abs = b/(2*a) if a > 0 and b <= 2*a else F(1)
        s_sign = 1 if R >= 0 else -1
        r_sign = -1 if y5 >= 0 else 1
        body_x0 = eta*s_sign*s_abs/2
        body_e1 = L*eta*r_sign*(1-s_abs*s_abs)/2
        attained = R*body_x0-2*y5*body_e1/c
        check(attained == curved, 'candidate null sharpness on necessary body')

    record = {
        'date': '2026-10-10',
        'model': 'GPT-6 (Codex); exact serving variant and effort not exposed and not inferred',
        'status': 'PASS',
        'arithmetic': 'Python standard-library Fraction; exact rational controls',
        'source': Path(__file__).name,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'assertions_passed': checks,
        'families': families,
        'scope': 'Finite algebra and sharp necessary-body support controls; no genuine candidate or arithmetic sign certificate; internal LLM validation only.',
    }
    output = json.dumps(record, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
