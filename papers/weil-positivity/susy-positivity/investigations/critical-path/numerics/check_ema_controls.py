#!/usr/bin/env python3
"""Finite EMA controls; no arithmetic contraction certificate.

Standard-library binary64 quadrature tests the identities in the continuation
note. No zeta zeros, finite transfer matrix, or fitted smoothing schedule is used.
"""
import cmath
import json
import math


def integrate(fun, a=0., b=1., tolerance=2e-13):
    def simpson(a, b, fa, fm, fb):
        return (b-a)*(fa+4*fm+fb)/6

    def refine(a, b, fa, fm, fb, old, eps, depth):
        mid = (a+b)/2
        left_mid, right_mid = (a+mid)/2, (mid+b)/2
        fl, fr = fun(left_mid), fun(right_mid)
        left = simpson(a, mid, fa, fl, fm)
        right = simpson(mid, b, fm, fr, fb)
        difference = left+right-old
        if abs(difference) <= 15*eps:
            return left+right+difference/15
        if depth == 0:
            raise ValueError("Quadrature did not meet its local tolerance")
        return (refine(a, mid, fa, fl, fm, left, eps/2, depth-1)
                + refine(mid, b, fm, fr, fb, right, eps/2, depth-1))

    if a == b:
        return 0.
    fa, fm, fb = fun(a), fun((a+b)/2), fun(b)
    return refine(a, b, fa, fm, fb, simpson(a, b, fa, fm, fb),
                  tolerance, 24)


def split_integral(fun, ell, endpoint=1.):
    points = sorted({0., endpoint, *[min(m*ell, endpoint)
                                    for m in (1, 4, 16, 40)]})
    return sum(integrate(fun, a, b) for a, b in zip(points, points[1:]))


def polynomial(x):
    return x*(1-x)


def poly_ema(x, ell, start=0.):
    particular = lambda y: polynomial(y)-ell*(1-2*y)-2*ell*ell
    if start == 0.:
        return polynomial(x)+2*ell*x+(ell+2*ell*ell)*math.expm1(-x/ell)
    return particular(x)-particular(start)*math.exp(-(x-start)/ell)


def poly_ema_derivative(x, ell):
    return (1+2*ell)*(-math.expm1(-x/ell))-2*x


def oscillation(x):
    return cmath.exp(3j*x)


def oscillatory_ema(x, ell, start=0.):
    return (oscillation(x)-oscillation(start)*math.exp(-(x-start)/ell))/(1+3j*ell)


def oscillatory_derivative(x, ell):
    return (3j*oscillation(x)+math.exp(-x/ell)/ell)/(1+3j*ell)


def digamma_positive(z):
    correction = 0.
    while z < 24:
        correction -= 1/z
        z += 1
    inv = 1/z
    return (correction+math.log(z)-inv/2-inv**2/12+inv**4/120
            -inv**6/252+inv**8/240-inv**10/132)


def main():
    cases, samples = [], []

    def check(name, value, threshold, comparison="<="):
        passed = value <= threshold if comparison == "<=" else value >= threshold
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison=comparison,
                          passed=math.isfinite(value) and passed))

    families = (("polynomial", polynomial, poly_ema, poly_ema_derivative),
                ("complex oscillation", oscillation, oscillatory_ema,
                 oscillatory_derivative))
    for name, f, ema, derivative in families:
        for ell in (.03, .2, .8):
            input_norm = integrate(lambda x: abs(f(x))**2)
            output_norm = split_integral(lambda x: abs(ema(x, ell))**2, ell)
            derivative_norm = split_integral(
                lambda x: abs(derivative(x, ell))**2, ell)
            storage = ell*ell*derivative_norm+ell*abs(ema(1., ell))**2
            check(f"EMA energy identity {name} ell={ell}",
                  abs(input_norm-output_norm-storage), 3e-11)
            allpass_norm = split_integral(
                lambda x: abs(f(x)-2*ema(x, ell))**2, ell)
            check(f"all-pass EMA boundary storage {name} ell={ell}",
                  abs(input_norm-allpass_norm-2*ell*abs(ema(1., ell))**2),
                  3e-11)
            for x in (.23, .71):
                # Integrate in the scaled delay to resolve the narrow kernel.
                cap = min(x/ell, 45.)
                direct = integrate(lambda v: math.exp(-v)*f(x-ell*v), 0., cap)
                check(f"convolution versus ODE {name} ell={ell} x={x}",
                      abs(direct-ema(x, ell)), 3e-11)
            cut, endpoint = .4, .7
            carry = math.exp(-(endpoint-cut)/ell)*ema(cut, ell)
            new = ema(endpoint, ell, cut)
            check(f"memory across interval join {name} ell={ell}",
                  abs(ema(endpoint, ell)-carry-new), 2e-13)
        norms = [split_integral(lambda x: abs(ema(x, ell))**2, ell)
                 for ell in (.05, .2, .8)]
        for i in (0, 1):
            check(f"increasing length decreases output norm {name} pair={i}",
                  norms[i]-norms[i+1], 0., ">=")

    euler = .5772156649015328606
    w0 = -euler-math.pi/2-3*math.log(2)-math.log(math.pi)
    count = 20000
    for p in (1.3, 2., 5.):
        finite = w0+4+2/(p-.5)
        finite += math.fsum(2*p/((2*n+.5)*(2*n+.5+p))
                            for n in range(1, count+1))
        target = digamma_positive((p+2.5)/2)-math.log(math.pi)+2/(p-.5)
        check(f"EMA tower versus full prime-free generator p={p}",
              abs(target-finite), p/(2*count+.5)+2e-12)

    growth, endpoint = .6, .7
    for rate in (.4, .6, .8):
        ema = integrate(lambda y: rate*math.exp(-rate*(endpoint-y))
                        * math.exp(growth*y), 0., endpoint)
        expected = ((growth-rate)*math.exp(growth*endpoint)
                    + 2*rate*math.exp(-rate*endpoint))/(growth+rate)
        check(f"fixed arithmetic EMA cancels growing mode rate={rate}",
              abs(math.exp(growth*endpoint)-2*ema-expected), 3e-12)

    for omega in (.1, .01, .001, .0001):
        # V_toy = exp(omega) I; ell = 2 sqrt(omega), L=1.
        upper_squared = math.exp(2*omega)/(1+8*omega)
        check(f"toy all-input filtered contraction bound omega={omega}",
              upper_squared, 1.)
        check(f"toy original transfer expands omega={omega}",
              math.expm1(2*omega), 0., ">=")

    for omega in (1e-4, 1e-6, 1e-8):
        for label, ell, limit, tolerance in (
                ("contaminating", 2*math.sqrt(omega), 19/30, 8*math.sqrt(omega)),
                ("vanishing", omega**.75, -1/30, math.sqrt(omega))):
            loss = (ell*ell*split_integral(
                lambda x: poly_ema_derivative(x, ell)**2, ell)
                + ell*poly_ema(1., ell)**2)
            quotient = (-math.expm1(2*omega)/30+math.exp(2*omega)*loss)/(2*omega)
            check(f"toy fixed-test limit {label} omega={omega}",
                  abs(quotient-limit), tolerance)
            samples.append(dict(schedule=label, omega=omega, ell=ell,
                                quotient=quotient, expected_limit=limit))

    for c in (.5, 1., 2.):
        omega = 1e-4
        # Exact series for the path EMA with tau(omega)=c*omega,
        # driven by exp(omega), initialized by continuity at one.
        slope = math.fsum(omega**(n-1)/(math.factorial(n)*(1+c*n))
                         for n in range(1, 15))
        check(f"path EMA rescaled first derivative c={c}",
              abs(slope-1/(1+c)), 6e-5)

    result = dict(schema_version=1, description=__doc__.strip(),
                  parameters=dict(precision="Python binary64; not interval arithmetic",
                                  quadrature_local_tolerance=2e-13,
                                  gamma_modes=count, window_length=1.,
                                  source_functions=["x(1-x)", "exp(3 i x)"],
                                  toy_transfer="exp(omega) I"),
                  cases=cases, case_count=len(cases),
                  all_pass=all(c["passed"] for c in cases), samples=samples)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result["all_pass"])


if __name__ == "__main__":
    main()
