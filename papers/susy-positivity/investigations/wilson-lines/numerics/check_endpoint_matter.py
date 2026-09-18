#!/usr/bin/env python3
"""Finite checks for the endpoint-matter continuation; standard library only.

Prints deterministic JSON and writes nothing. Analytic proofs are in the notes.
No test establishes endpoint protection, physical supercharges, positivity of a
gauge-theory kernel, or the arithmetic transfer. Model: OpenAI GPT-6 (Codex).
"""
import cmath
from fractions import Fraction as F
import json
import math


def psi(z):
    z = complex(z)
    result = 0j
    while z.real < 24:
        result -= 1 / z
        z += 1
    result += cmath.log(z) - 1 / (2*z)
    for n, bn in enumerate((F(1, 6), F(-1, 30), F(1, 42),
                            F(-1, 30), F(5, 66), F(-691, 2730)), 1):
        result -= float(bn) / (2*n*z**(2*n))
    return result


def simpson(fn, end=64., n=32768):
    step = end / n
    # fsum handles real and imaginary components independently.
    terms = [complex(fn(0)), complex(fn(end))]
    terms.extend((4 if k % 2 else 2)*fn(k*step) for k in range(1, n))
    return step/3 * complex(math.fsum(x.real for x in terms),
                            math.fsum(x.imag for x in terms))


def kernel(u):
    return math.exp(-u/2)/(-math.expm1(-2*u))


GROUPS = []


def group(name, checks, method, tolerance=None):
    passed = all(checks)
    row = {"name": name, "cases": len(checks), "method": method, "pass": passed}
    if tolerance is not None:
        row["tolerance"] = tolerance
    GROUPS.append(row)
    if not passed:
        raise AssertionError(name + ': failed cases ' + str(
            [i for i, ok in enumerate(checks) if not ok]))


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def norm(a):
    return max(abs(x) for row in a for x in row)


def main():
    # Rational t=exp(-u/2): independent image and tower expressions.
    checks = []
    for k in range(1, 20):
        t = F(k, 20)
        same, opposite = t/(1-t*t), t/(1+t*t)
        checks += [(same+opposite)/2 == t/(1-t**4),
                   (same-opposite)/2 == t**3/(1-t**4)]
    group('A. even and odd image kernels', checks, 'exact rational identities')

    checks = []
    for tau in (.3, 1., 3., 5.):
        value = simpson(lambda u: 0. if u == 0 else
                        4*math.sin(tau*u/2)**2*kernel(u))
        exact = (psi(.25+1j*tau/2)-psi(.25)).real
        checks.append(abs(value-exact) < 2e-8)
        count = 20000
        total = 2*math.fsum(tau*tau/((2*n+.5)*((2*n+.5)**2+tau*tau))
                           for n in range(count))
        a = 2*count+.5
        tail_bound = 2*tau*tau*(1/a**3+1/(4*a*a))
        checks += [total <= exact+1e-12,
                   abs(exact-total) <= tail_bound+1e-12]
    group('B. difference energy', checks,
          'quadrature and positive finite tower versus digamma; explicit sum-tail bound', 2e-8)

    checks = []
    for p, q in ((.1+.4j, .7), (1+1j, .2), (2+3j, 1.)):
        value = simpson(lambda u: q-p if u == 0 else
                        (cmath.exp(-p*u)-cmath.exp(-q*u))/(2*math.sinh(u/2)))
        checks.append(abs(value-(psi(q+.5)-psi(p+.5))) < 2e-8)
    # A fixed real subtraction does not force a constant phase.
    r1, r2 = (1+psi(.5)-psi(.5+1j*t) for t in (1., 2.))
    checks.append(abs(cmath.phase(r1)-cmath.phase(r2)) > .05)
    group('C. subtracted endpoint transform', checks,
          'convergent complex quadrature and fixed-subtraction phase control', 2e-8)

    checks = []
    for delta in (.2, .5, .8):
        for u in (.5, 1., 2.):
            direct = ((2*math.sinh(u/2))**(-2*delta)
                      +(2*math.cosh(u/2))**(-2*delta))/2
            c, total = 1., 1.
            for k in range(1, 241):
                c *= (2*delta+k-1)/k
                if k % 2 == 0:
                    total += c*math.exp(-k*u)
            checks.append(abs(math.exp(-delta*u)*total/direct-1) < 1e-12)
    for n in range(1, 12):
        def coefficient(delta):
            return math.prod((2*delta+k)/(k+1) for k in range(2*n))
        h = 1e-5
        derivative = (coefficient(.5+h)-coefficient(.5-h))/(2*h)
        checks.append(abs(derivative-2*sum(1/k for k in range(1, 2*n+1))) < 2e-8)
    group('D. general weight and first variation', checks,
          'binomial series and centered derivative versus harmonic-number formula', 2e-8)

    # Clifford identities, not a count of physical defect supercharges.
    eye = [[1, 0], [0, 1]]
    g1 = [[0, 1], [1, 0]]
    g3 = [[0, -1j], [1j, 0]]
    gi = [[1, 0], [0, -1]]
    jmat = scale(1j, mul(gi, g3))
    checks = [mul(jmat, jmat) == eye, mul(jmat, g1) == mul(g1, jmat)]
    for c, radius in ((0, 1), (2, 1), (3, 2), (1, 3)):
        m = scale(-1, add(scale(c, g1), scale(radius, mul(jmat, g1))))
        for co, si in ((1., 0.), (0., 1.), (-1., 0.), (.6, .8), (-.6, .8)):
            tangent = add(scale(-si, g1), scale(co, g3))
            point = add(scale(c+radius*co, g1), scale(radius*si, g3))
            checks.append(norm(mul(add(scale(1j, tangent), gi), add(m, point))) < 1e-12)
    plus = scale(.5, add(eye, jmat))
    for r1, r2 in ((3, 1), (5, 2), (7, 3)):
        # Delta c=r2, Delta R=-r2 for the two shared-right-endpoint circles.
        checks.append(norm(mul(add(scale(r2, eye), scale(-r2, jmat)), plus)) == 0)
        for left in (r2, -r2):
            c, radius = (r1+left)/2, (r1-left)/2
            diff = add(scale(c-r1, g1), scale(radius, mul(jmat, g1)))
            checks.append(norm(mul(diff, plus)) == 0)
    for dc, dr in ((2, 1), (3, 1), (1, 2), (1, 0)):
        product = mul(add(scale(dc, eye), scale(dr, jmat)),
                      add(scale(dc, eye), scale(-dr, jmat)))
        checks += [product == scale(dc*dc-dr*dr, eye), dc*dc != dr*dr]
    group('E. fixed-coupling semicircle bulk condition', checks,
          'finite Clifford identities and shared-endpoint/invertibility controls', 1e-12)

    def logk(p, w):
        return w*math.log(math.pi)+math.lgamma(.25+(p-w)/2)-math.lgamma(.25+(p+w)/2)
    checks = []
    p0 = 1.
    for p in (.2, .7, 2., 4.):
        for w in (.1, .3, .5):
            want = logk(p, w)-logk(p0, w)
            integral = simpson(lambda u: w*(p0-p) if u == 0 else
                               (math.exp(-p*u)-math.exp(-p0*u))
                               *2*math.sinh(w*u)*kernel(u)/u, end=160., n=65536)
            checks.append(abs(integral-want) < 3e-8)
            count = 3000
            logprod = math.fsum(math.log1p(2*w/(2*n+.5+p-w))
                               -math.log1p(2*w/(2*n+.5+p0-w)) for n in range(count))
            low = 2*count+.5+min(p, p0)-w
            bound = 2*w*abs(p-p0)*(1/low**2+1/(2*low))
            checks.append(abs(logprod-want) <= bound+1e-12)
            h = 1e-5
            derivative = -(logk(p, w+h)-logk(p, w-h))/(2*h)
            gen = -math.log(math.pi)+.5*(psi(.25+(p-w)/2)+psi(.25+(p+w)/2)).real
            checks.append(abs(derivative-gen) < 2e-8)
    group('F. shifted determinant, heat integral and generator', checks,
          'Gamma ratio versus convergent product, quadrature and shift derivative', 3e-8)

    checks = []
    # Substitute q=p(1+t) above the integrable log singularity and integrate
    # each side with quadratic coordinates; neither endpoint log is sampled.
    def direct_j(p, cutoff):
        def left(t):
            if t == 0: return 0.
            q = p*(1-t*t)
            return 2*p*t*math.log(((q+p)/(p-q))**2)
        def right(t):
            if t == 0: return 0.
            q = p+(cutoff-p)*t*t
            return 2*(cutoff-p)*t*math.log(((q+p)/(q-p))**2)
        return (simpson(left, 1., 16384)+simpson(right, 1., 16384)).real
    for p, ratio in ((.5, 3.), (1., 5.), (2., 10.)):
        exact = 2*p*((ratio+1)*math.log(ratio+1)-(ratio-1)*math.log(ratio-1))
        checks.append(abs(direct_j(p, p*ratio)-exact) < 2e-6)
    for ratio in (100., 1000.):
        normalized = .5*((ratio+1)*math.log(ratio+1)-(ratio-1)*math.log(ratio-1))
        checks.append(abs(normalized-math.log(ratio)-1) < 1/ratio**2)
    group('G. cutoff logarithm and retained momentum scale', checks,
          'split quadrature of integrable singularity and ultraviolet asymptotic', 2e-6)

    print(json.dumps({"schema": 1, "date": "2026-09-18", "model": "OpenAI GPT-6 (Codex)",
                      "groups": GROUPS, "total_checks": sum(g['cases'] for g in GROUPS),
                      "pass": all(g['pass'] for g in GROUPS),
                      "scope": "Finite identity checks; no physical realization or positivity certificate."}, indent=2))


if __name__ == '__main__':
    main()
