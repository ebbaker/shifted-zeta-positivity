#!/usr/bin/env python3
"""BW-13: exact finite algebra plus non-certified contour diagnostics.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort max, 21 October 2026.
Uses only the Python standard library. No theta data are acquired.
"""
import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

def trim(p):
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p

def mul(p, q, degree=None):
    top = len(p) + len(q) - 2
    if degree is not None:
        top = min(top, degree)
    out = [F(0)] * (top + 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i + j <= top:
                out[i + j] += a * b
    return trim(out)

def deriv(p, n=1):
    if n >= len(p):
        return [F(0)]
    return [p[k] * F(math.factorial(k), math.factorial(k-n))
            for k in range(n, len(p))]

def scale(p, c):
    return [c*a for a in p]

def add(p, q):
    return trim([(p[k] if k < len(p) else F(0)) +
                 (q[k] if k < len(q) else F(0))
                 for k in range(max(len(p), len(q)))])

def binomial_series(g, exponent, degree):
    """g[0]=1; return (g**exponent) to the stated degree, exactly."""
    assert g[0] == 1
    u = g.copy()
    u[0] = F(0)
    power = [F(1)]
    out = [F(1)]
    coeff = F(1)
    for k in range(1, degree+1):
        power = mul(power, u, degree)
        coeff *= F(exponent-k+1, k)
        out = add(out, scale(power, coeff))
    return out + [F(0)] * max(0, degree+1-len(out))

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for first in range(1, n-k+2):
            for rest in compositions(n-first, k-1):
                yield (first,) + rest

def normalized_period_coefficient(h, n):
    """Coefficient of tau**n in P/(2*pi*i*sqrt(A)), via Laurent residue.

    A=1 in these exact controls. Formula expands sqrt(h + delta h)
    before taking the x**(-1) coefficient; it does not use the
    proposed closed expression for the quadratic time coefficient.
    """
    assert h[0] == h[1] == 0 and h[2] == 1
    g = h[2:]
    residue = F(0)
    choose = F(1)
    for p in range(1, n+1):
        choose *= F(F(1, 2)-p+1, p)
        top = 2*p-2
        gp = binomial_series(g, F(1, 2)-p, top)
        for parts in compositions(n, p):
            product = [F(1)]
            for k in parts:
                product = mul(product, scale(deriv(h, 2*k),
                                  F((-1)**k, math.factorial(k))), top)
            product = mul(product, gp, top)
            residue += choose * (product[top] if top < len(product) else 0)
    return -residue

def value(p, x):
    ans = 0j
    for a in reversed(p):
        ans = ans*x + float(a)
    return ans

def heat_coefficients(h, t):
    return [scale(deriv(h, 2*k), F((-1)**k, math.factorial(k)))
            for k in range((len(h)-1)//2+1)]

def heat_value(h, t, x):
    return sum((t**k)*value(c, x) for k, c in
               enumerate(heat_coefficients(h, t)))

def contour(h, t, radius, points):
    # w0=x sqrt(g), continued as w=w0 sqrt(H/h), with both auxiliary
    # square roots in their small disks about 1. The cut orientation is
    # the NEGATIVE of the counterclockwise outer boundary.
    g = h[2:]
    pp, qq, qqmax = [], [], 0.0
    for k in range(points):
        x = radius*cmath.exp(2j*math.pi*k/points)
        h0 = value(h, x)
        ht = heat_value(h, t, x)
        w0 = x*cmath.sqrt(value(g, x))
        ratio = ht/h0
        qqmax = max(qqmax, abs(ratio-1))
        w = w0*cmath.sqrt(ratio)
        pp.append(x*w)
        qq.append(x/w)
    avg = lambda arr: complex(math.fsum(z.real for z in arr),
                              math.fsum(z.imag for z in arr))/points
    # P/(2*pi*i) and Q/(-2*pi*i).
    return -avg(pp), avg(qq), qqmax

def polynomial_majorant(h, j, radius, time_radius):
    out = 0.0
    for k in range((len(h)-1)//2+1):
        c = scale(deriv(h, j+2*k), F(1, math.factorial(k)))
        out += time_radius**k * sum(float(abs(a))*radius**d
                                    for d, a in enumerate(c))
    return out

def polynomial_contract(h, r, s):
    eta = sum(float(abs(h[k]))*r**(k-2) for k in range(3, len(h)))
    M = {j:polynomial_majorant(h,j,r,s) for j in (2,3,4,6)}
    m0 = r*r*(1-eta)
    m = m0-s*M[2]
    assert m > 0 and s*M[2]/m0 < 0.5
    assert M[3]*r + M[4]*s < 1
    assert sum(float(abs(k*h[k]))*r**(k-1) for k in range(3,len(h))) \
            + s*M[3] < 2*r
    D = (M[6]/(2*math.sqrt(m)) +
         3*M[2]*M[4]/(4*m**1.5) +
         3*M[2]**3/(8*m**2.5))
    return r*D/6, m, eta

def run():
    examples = {
        "quadratic": [0,0,1],
        "cubic": [0,0,1,F(1,5)],
        "positive_quartic": [0,0,1,0,F(3,10)],
        "mixed_quartic": [0,0,1,F(1,5),F(3,10)],
        "all_real_quartic": [0,0,1,0,F(-1,9)],
        "even_mirrored_double": [0,0,1,1,F(1,4)],
        "higher_jet_change": [0,0,1,F(1,5),F(3,10),F(1,7),
                              F(-1,11),F(1,13),F(1,17)],
    }
    exact = []
    floating = []
    for name, raw in examples.items():
        h = [F(a) for a in raw]
        B = h[3] if len(h)>3 else F(0)
        C = h[4] if len(h)>4 else F(0)
        expected = F(15,16)*B*B-F(3,4)*C
        coeffs = [normalized_period_coefficient(h,n) for n in (1,2,3)]
        assert coeffs[0] == 1 and coeffs[1] == expected
        # Separate deflated-logarithmic-derivative identity.
        S = B*B-2*C
        assert expected == F(9,16)*B*B+F(3,8)*S
        exact.append({"case":name,"P_normalized_coefficients_1_to_3":
                      [str(x) for x in coeffs], "S":str(S)})
        r, s = 0.125, 0.001
        C3, m, eta = polynomial_contract(h,r,s)
        for t in (0.001,0.0005):
            p, q, qmax = contour(h,t,r,1024)
            p2,q2,_ = contour(h,t,r,2048)
            residual = abs(p-(t+float(expected)*t*t))
            expected_q = 1+(4.5*float(C)-2.625*float(B*B))*t
            assert qmax<0.5
            assert residual <= C3*t**3+2e-16
            assert abs(p-p2)<2e-14 and abs(q-q2)<2e-13
            assert abs((p-t)/t**2-float(expected))<0.003
            if name == "quadratic":
                assert abs(p-t)<1e-15 and abs(q-1)<1e-14
            floating.append({"case":name,"tau":t,"radius":r,
                  "normalized_P_real":p.real,
                  "normalized_P_imaginary_abs":abs(p.imag),
                  "K_estimate_real":((p-t)/t**2).real,
                  "K_exact":str(expected),"quadratic_residual_abs":residual,
                  "remainder_bound":C3*t**3,
                  "P_grid_change_abs":abs(p-p2),
                  "Q_first_order_residual_abs":abs(q-expected_q),
                  "boundary_relative_change_max":qmax})
    # An exact all-real polynomial control: x^2(1-x^2/9).
    # Its positive-time roots have squared coordinates v satisfying
    # v^2-(9+12t)v+18t+12t^2=0. For all t>0, the sum and product
    # are positive, and discriminant 81+144t+96t^2 is positive.
    # This proves four distinct real roots, not just the finite check.
    for t in (F(1,1000),F(1,10),F(1),F(10)):
        sm, prod = 9+12*t, 18*t+12*t*t
        disc = sm*sm-4*prod
        assert disc==81+144*t+96*t*t and disc>0 and prod>0 and sm>0
        # The even global control (z^2-1)^2, locally normalized at z=1.
        sm2, prod2 = 2+12*t, 1+4*t+12*t*t
        assert sm2*sm2-4*prod2 == 32*t+96*t*t
        assert sm2>0 and prod2>0 and sm2*sm2>4*prod2
    # b=2 cubic from the originating proposal. Exactly one physical
    # event; the other two occur at nonreal complex time.
    cubic = []
    for k in range(3):
        z = cmath.exp(2j*math.pi*k/3)
        t = (-4+3*z*z)/6
        H = z**3-(4+6*t)*z+2
        Hz = 3*z*z-(4+6*t)
        assert abs(H)<1e-13 and abs(Hz)<1e-13
        cubic.append({"z":[z.real,z.imag],"t":[t.real,t.imag]})
    assert abs(cubic[0]["t"][0]+1/6)<1e-14
    assert all(abs(row["t"][1])>0.4 for row in cubic[1:])
    return {
       "status":"exact finite algebra passed; floating diagnostics passed",
       "scope":"No theta quadrature, interval certificate, or global exclusion.",
       "prepared_for":"Edward Baker","date":"2026-10-21",
       "model":"gpt-6-astra","reasoning_effort":"max",
       "exact_controls":exact,"floating_contours":floating,
       "all_real_controls":[
           "h=x^2(1-x^2/9), K=1/12; real/simple for every tau>0",
           "global h=(z^2-1)^2; local K=3/4 at z=1; real/simple for every tau>0"],
       "cubic_spacetime_events_floating":cubic,
       "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    content=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
        print(json.dumps({"status":result["status"],
                          "exact_cases":len(result["exact_controls"]),
                          "floating_rows":len(result["floating_contours"]),
                          "output":str(args.output)}))
    else:
        print(content)

if __name__=="__main__":
    main()
