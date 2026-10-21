#!/usr/bin/env python3
"""Finite exact checks for BW10 Note 24, 21 October 2026.

Prepared for Edward Baker with substantial gpt-6-astra / max assistance.
Frozen checks: heat polynomials of degrees 2..10; both signs of time;
complex Gram normalization; pure endpoint radial flux; asymmetric
predecessor leading coefficients; and rational enclosures of the exact
quadratic disk-area formula. No theta quadrature, analytic-limit proof,
or endpoint exclusion is supplied by these checks.
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import platform

import check_hmc_exact_algebra as algebra
import check_hmc_endpoint_trace_algebra as endpoint
from check_hmc_exact_algebra import add, scale, derivative, trim


COUNTS = {}


def check(test, group):
    assert test, group
    COUNTS[group] = COUNTS.get(group, 0) + 1


def ca(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cs(a, x):
    return (a[0] * x, a[1] * x)


def cm(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def cc(a):
    return (a[0], -a[1])


def cn(a):
    return a[0]**2 + a[1]**2


def cp(a, n):
    out = (F(1), F(0))
    for _ in range(n):
        out = cm(out, a)
    return out


def cv(poly, z):
    out = (F(0), F(0))
    for v in reversed(poly):
        out = ca(cm(out, z), (v, F(0)))
    return out


def dx(poly, n):
    for _ in range(n):
        poly = derivative(poly)
    return poly


def heat(poly, t):
    out = [F(0)]
    for k in range((len(poly)-1)//2+1):
        out = add(out, scale(dx(poly, 2*k), (-t)**k/F(factorial(k))))
    return out


def gcd(p, q):
    while trim(q) != [0]:
        p, q = q, endpoint.divrem(p, q)[1]
    return scale(p, 1/p[-1])


def inner_coefficient(poly, eta, power):
    # e^(s d_z^2) poly evaluated at z=s*eta; coefficient of s^power.
    out = (F(0), F(0))
    for degree, coefficient in enumerate(poly):
        for k in range(degree//2+1):
            if degree-k == power:
                c = coefficient*F(factorial(degree),
                                  factorial(k)*factorial(degree-2*k))
                out = ca(out, cs(cp(eta, degree-2*k), c))
    return out


def sqrt_interval(x, digits=65):
    denominator = 10**digits
    a = isqrt((x.numerator*denominator**2)//x.denominator)
    lo, hi = F(a, denominator), F(a+1, denominator)
    check(lo*lo <= x < hi*hi, "rational_square_root")
    return lo, hi


def quadratic_area_over_pi(s, radius):
    q = radius**2
    a, b, c = q*q+4*q+4*s*s, 4*s*q, q*q-4*s*s
    delta = a*a-b*b
    check(delta-c*c == 8*q*(q*q+2*q+4*s*s),
          "quadratic_discriminant")
    check(delta > c*c, "quadratic_area_between_zero_and_two")
    aq, bq = 2*q+4, 4*s
    # Reduce the differentiated mean-log expression modulo d^2=delta.
    check(q*aq-a-c == 0, "quadratic_boundary_simplification")
    check(q*(a*aq-b*bq)-delta-a*c == 0,
          "quadratic_boundary_simplification")
    lo, hi = sqrt_interval(delta)
    endpoints = [1+c/lo, 1+c/hi]
    lower, upper = min(endpoints), max(endpoints)
    check(0 < lower <= upper < 2, "quadratic_area_enclosure")
    return lower, upper


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    z_points = [(F(0), F(0)), (F(1,3), F(2,5)),
                (F(-2,7), F(3,4)), (F(1), F(-1))]
    for m in range(2, 11):
        pure = [F(0)]*m+[F(1)]
        check(len(gcd(pure, derivative(pure)))-1 == m-1,
              "endpoint_common_factor")
        for t in [F(1,4), F(1,32), F(-1,4), F(-1,32)]:
            p = heat(pure, t)
            check(len(gcd(p, derivative(p))) == 1,
                  "split_polynomial_simple_zeros")
            pt = [F(0)]
            for k in range(1, m//2+1):
                pt = add(pt, scale(dx(pure, 2*k),
                         F((-1)**k, factorial(k-1))*t**(k-1)))
            check(add(pt, dx(p,2)) == [0], "heat_sign")
            for z in z_points:
                f, f1, f2 = [cv(dx(p,j),z) for j in range(3)]
                energy = cn(f)+cn(f1)
                v = ca(cm(f1,cc(f)), cm(f2,cc(f1)))
                determinant = ca(cm(f,f2),cs(cm(f1,f1),-1))
                check(energy > 0, "split_jet_nonvanishing_at_fixtures")
                check(energy*(cn(f1)+cn(f2))-cn(v) == cn(determinant),
                      "complex_gram_and_laplacian_normalization")
        for radius in [F(1,5), F(1), F(3)]:
            for u in [F(0), F(1,3), F(2)]:
                direction = ((1-u*u)/(1+u*u),2*u/(1+u*u))
                z = cs(direction, radius)
                f, f1, f2 = [cv(dx(pure,j),z) for j in range(3)]
                energy = cn(f)+cn(f1)
                v = ca(cm(f1,cc(f)),cm(f2,cc(f1)))
                radial = 2*cm(direction,v)[0]
                check(radius*radial/(2*energy)
                      == m-1+radius**2/(radius**2+m*m),
                      "pure_endpoint_boundary_flux")
                det = ca(cm(f,f2),cs(cm(f1,f1),-1))
                check(cn(det)/energy**2
                      == F(m*m)/(radius**2+m*m)**2,
                      "pure_reduced_gauss_density")

    for j in [0,1]:
        for r in range(1,6):
            m = 2*r+j
            for a,b in [(F(0),F(0)),(F(1,3),F(-2,7)),
                        (F(-2,5),F(1,4))]:
                germ = [F(0)]*m+[F(1),a,b]
                w = dx(germ,j)
                A = w[2*r]*factorial(2*r)
                B = (w[2*r+1] if len(w)>2*r+1 else F(0))*factorial(2*r+1)
                k, c1 = A/F(factorial(r)), -B/(r*A)
                for q in z_points:
                    eta = ca((c1,F(0)),cs(q,F(1,r)))
                    check(inner_coefficient(w,eta,r)==(k,F(0)),
                          "complex_inner_leading_coefficients")
                    check(inner_coefficient(dx(w,1),eta,r)==cs(q,k),
                          "complex_inner_leading_coefficients")
                    check(inner_coefficient(dx(w,2),eta,r-1)==(k*r,F(0)),
                          "complex_inner_leading_coefficients")
                    for d in range(r):
                        check(inner_coefficient(w,eta,d)==(0,0),
                              "inner_lower_coefficients_vanish")

    samples = []
    for C in [F(1,2),F(1),F(2)]:
        for s in [F(1,8),F(1,32),F(1,128)]:
            lo, hi = quadratic_area_over_pi(s,s*C)
            samples.append({"s":str(s),"R_over_s":str(C),
                "area_over_pi_interval":[str(lo),str(hi)],
                "area_over_pi_display":float((lo+hi)/2),
                "limiting_area_over_pi":str(C*C/(1+C*C))})
    for s in [F(1,7),F(1,100)]:
        for radius in [F(1,10),F(1),F(3)]:
            quadratic_area_over_pi(s,radius)
            q = radius**2
            for u in [F(0),F(1,3),F(2)]:
                v=((1-u*u)/(1+u*u),2*u/(1+u*u))
                z=cs(v,radius)
                f=ca(cm(z,z),(2*s,F(0)))
                e=cn(f)+4*cn(z)
                cos2=v[0]**2-v[1]**2
                check(e==q*q+4*q+4*s*s+4*s*q*cos2,
                      "quadratic_polar_energy")
                # Changing time sign equals rotating z by i, in the energy.
                iz=(-z[1],z[0])
                after=ca(cm(iz,iz),(-2*s,F(0)))
                check(cn(after)+4*cn(iz)==e,
                      "opposite_turning_equal_rotated_energy")

    paths=[Path(__file__),Path(algebra.__file__),Path(endpoint.__file__)]
    record={
        "status":"passed",
        "date":"2026-10-21",
        "prepared_for":"Edward Baker",
        "model":"gpt-6-astra",
        "effort":"max",
        "verification":"same-assistant finite exact checks; analytic results rely on the written proof",
        "python":platform.python_version(),
        "utc_execution_time":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "checks_by_group":COUNTS,
        "source_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        "quadratic_inner_area_samples":samples,
        "scope":"No theta sign, analytic-tail, arbitrary-multiplicity proof, or endpoint exclusion certificate."
    }
    if args.output:
        args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"passed","checks_by_group":COUNTS,
                      "quadratic_inner_area_samples":[
                          {k:v for k,v in row.items() if k!="area_over_pi_interval"}
                          for row in samples]},indent=2))


if __name__=="__main__":
    main()
