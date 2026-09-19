#!/usr/bin/env python3
"""Independent finite checks for angular smearing and the Robin continuation.

Standard library only; prints deterministic JSON and writes nothing.
These checks do not establish interacting reflection positivity or RH.
"""
import cmath
import json
import math


GROUPS = []


def group(name, checks, method, tolerance):
    failures = [i for i, ok in enumerate(checks) if not ok]
    GROUPS.append(dict(name=name, cases=len(checks), method=method,
                       tolerance=tolerance, **{'pass': not failures}))
    if failures:
        raise AssertionError(name + ': ' + str(failures))


def gauss(n, left=-1., right=1.):
    """Gauss-Legendre nodes and weights by Newton iteration."""
    pairs = []
    for k in range(1, n+1):
        z = math.cos(math.pi*(k-.25)/(n+.5))
        for _ in range(32):
            p0, p1 = 1., z
            for j in range(2, n+1):
                p0, p1 = p1, ((2*j-1)*z*p1-(j-1)*p0)/j
            derivative = n*(z*p1-p0)/(z*z-1)
            dz = p1/derivative
            z -= dz
            if abs(dz) < 2e-16:
                break
        # Recompute the derivative at the final root.
        p0, p1 = 1., z
        for j in range(2, n+1):
            p0, p1 = p1, ((2*j-1)*z*p1-(j-1)*p0)/j
        derivative = n*(z*p1-p0)/(z*z-1)
        pairs.append(((left+right)/2+(right-left)*z/2,
                      (right-left)/((1-z*z)*derivative*derivative)))
    return sorted(pairs)


def legendre(l, mu):
    if l == 0:
        return 1.
    p0, p1 = 1., mu
    for j in range(2, l+1):
        p0, p1 = p1, ((2*j-1)*mu*p1-(j-1)*p0)/j
    return p1


def angular_density(rho, mu):
    # 2*pi times the antipodally averaged S^2 Poisson kernel.
    return (1-rho*rho)/4*((1-2*rho*mu+rho*rho)**-1.5
                            +(1+2*rho*mu+rho*rho)**-1.5)


def covariance(rho, u):
    return math.exp(-abs(u)/2)/(1-rho**4*math.exp(-2*abs(u)))


def tower(rho, tau=0., difference=False, n=2000):
    z = rho**4
    terms = []
    weight = 1.
    for k in range(n):
        a = 2*k+.5
        terms.append(weight*(2*tau*tau/(a*(a*a+tau*tau)) if difference
                             else 2*a/(a*a+tau*tau)))
        weight *= z
    return math.fsum(terms)


def simpson(fn, end, n=32768):
    h = end/n
    return h/3*math.fsum([fn(0.), fn(end)] +
                         [(4 if k % 2 else 2)*fn(k*h) for k in range(1, n)])


def gram_cholesky(kernel, points):
    size = len(points)
    lower = [[0.]*size for _ in points]
    pivots = []
    for i in range(size):
        for j in range(i+1):
            v = kernel(points[i], points[j])-sum(lower[i][k]*lower[j][k]
                                                for k in range(j))
            if i == j:
                pivots.append(v)
                if v <= 0:
                    return False
                lower[i][j] = math.sqrt(v)
            else:
                lower[i][j] = v/lower[j][j]
    return min(pivots) > 0


def psi(z):
    z = complex(z)
    value = 0j
    while z.real < 30:
        value -= 1/z
        z += 1
    value += cmath.log(z)-1/(2*z)
    for k, bn in enumerate((1/6, -1/30, 1/42, -1/30, 5/66, -691/2730), 1):
        value -= bn/(2*k*z**(2*k))
    return value


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(*terms):
    return [[sum(c*a[i][j] for c, a in terms)
             for j in range(len(terms[0][1][0]))]
            for i in range(len(terms[0][1]))]


def kron(a, b):
    return [[a[i][j]*b[k][l] for j in range(len(a)) for l in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


def norm(a):
    return max(abs(v) for row in a for v in row)


def main():
    nodes = gauss(96)
    checks = []
    for rho in (0., .3, .6, .8):
        for l in range(9):
            value = math.fsum(w*angular_density(rho, mu)*legendre(l, mu)
                              for mu, w in nodes)
            target = rho**l if l % 2 == 0 else 0.
            checks.append(abs(value-target) < 2e-10)
    group('A. normalized angular profiles and spherical harmonic moments', checks,
          'Gauss-Legendre integration of the explicit Poisson density', 2e-10)

    checks = []
    # Genuine double angular integration, not substitution into the tower sum.
    sphere_nodes = gauss(64)
    cosines = [math.cos(2*math.pi*k/64) for k in range(64)]
    for rho, u in ((.2, .7), (.5, .7), (.7, 1.), (.8, 2.)):
        rows = [(mu, w*angular_density(rho, mu), math.sqrt(1-mu*mu))
                for mu, w in sphere_nodes]
        terms = []
        for mu, wm, sm in rows:
            for nu, wn, sn in rows:
                average = math.fsum(1/math.sqrt(2*(math.cosh(u)-mu*nu-sm*sn*c))
                                    for c in cosines)/len(cosines)
                terms.append(wm*wn*average)
        checks.append(abs(math.fsum(terms)-covariance(rho, u)) < 2e-9)
    for rho in (0., .4, .8, .98):
        for u in (0., .1, 1., 3.):
            direct = math.fsum(rho**(4*n)*math.exp(-(2*n+.5)*u)
                               for n in range(2000))
            checks.append(abs(direct-covariance(rho, u)) < 1e-11)
        checks.append(gram_cholesky(lambda x, y: covariance(rho, x-y),
                                    (-1.7, -.5, 0., .2, 1.1)))
    group('B. smeared free covariance and finite Gram matrices', checks,
          'Double sphere quadrature, independent tower sum, Cholesky pivots', 2e-9)

    checks = []
    for rho in (.2, .6, .85):
        for tau in (.3, 1., 3.):
            direct = simpson(lambda u: 4*math.sin(tau*u/2)**2*covariance(rho, u), 64.)
            value = tower(rho, tau, difference=True)
            checks += [abs(value-direct) < 2e-8,
                       abs(tower(rho, 0)-tower(rho, tau)-value) < 1e-12,
                       value > 0]
    for tau in (.3, 1., 3., 10.):
        seq = [tower(rho, tau, difference=True) for rho in (.5, .8, .95, .99)]
        exact = (psi(.25+1j*tau/2)-psi(.25)).real
        checks += [all(x < y for x, y in zip(seq, seq[1:])), seq[-1] < exact]
        total = math.fsum(2*tau*tau/((2*n+.5)*((2*n+.5)**2+tau*tau))
                          for n in range(20000))
        a = 40000.5
        bound = 2*tau*tau*(a**-3+1/(4*a*a))
        checks.append(-1e-12 < exact-total < bound+1e-12)
    # Independent real-space Dirichlet energy for f(x)=exp(-x^2/2).
    # Its autocorrelation is sqrt(pi)*exp(-u^2/4).
    for rho in (.3, .8):
        position = 2*math.sqrt(math.pi)*simpson(
            lambda u: -math.expm1(-u*u/4)*covariance(rho, u), 64.)
        # |fhat|^2/(2*pi)=exp(-tau^2).
        frequency = 2*math.fsum(w*math.exp(-t*t)*tower(rho, t, True)
                                for t, w in gauss(160, 0., 10.))
        checks.append(abs(position-frequency) < 2e-8)
    group('C. finite covariance subtraction and positive difference form', checks,
          'Real-space quadrature versus Fourier tower, monotonicity and explicit tail bound', 2e-8)

    checks = []
    constant = -0.5772156649015328606-psi(.25).real
    errors = []
    for z in (.9, .99, .999):
        rho = z**.25
        mass = tower(rho, n=40000)
        errors.append(abs(mass+math.log1p(-z)-constant))
    checks += [errors[2] < errors[1] < errors[0], errors[2] < .01]
    for c in (0., 2., 5.):
        tau = math.exp(c+2)
        b = (psi(.25+1j*tau/2)-psi(.25)).real
        checks.append(c-b < 0)
    group('D. logarithmic contact divergence and failed finite contact repair', checks,
          'Abel tower asymptotic and high-frequency sign controls', .01)

    eye2 = [[1, 0], [0, 1]]
    sx, sy, sz = [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]
    tangents = [kron(sx, eye2), kron(sy, eye2), kron(sz, sx)]
    normal, internal = kron(sz, sy), kron(sz, sz)
    eye4 = kron(eye2, eye2)
    jmat = add((1j, mm(internal, normal)))
    projector = add((.5, eye4), (-.5, jmat))
    checks = []
    gammas = tangents+[normal, internal]
    for i, a in enumerate(gammas):
        for j, b in enumerate(gammas):
            anti = add((1, mm(a, b)), (1, mm(b, a)), (-2*(i == j), eye4))
            checks.append(norm(anti) < 1e-12)
    for direction in ((1,0,0), (0,1,0), (0,0,1), (1,2,3), (-2,1,-1)):
        length = math.sqrt(sum(v*v for v in direction))
        gn = add(*[(v/length, gamma) for v, gamma in zip(direction, tangents)])
        for radius in (.7, 2.):
            for theta in (.2, 1., 2.7):
                x = add((radius/2*(1+math.cos(theta)), gn),
                        (radius/2*math.sin(theta), normal))
                condition = add((-1j*math.sin(theta), gn),
                                (1j*math.cos(theta), normal), (1, internal))
                checks.append(norm(mm(mm(condition, x), projector)) < 1e-12)
    group('E. common bulk condition for arbitrary defect directions', checks,
          'Five-dimensional Clifford algebra in a 4x4 representation and rotated arcs', 1e-12)

    checks = []
    for a in (.5, 2.5, 6.5):
        for p in (-.2, .8, 2.):
            # On-shell half-cylinder action for phi(t)=exp(-a*t), boundary value 1.
            bulk = .5*simpson(lambda s: 2*a*math.exp(-2*s), 24.)
            checks.append(abs(bulk+p/2-(a+p)/2) < 1e-11)
            # Complex Gaussian integral with d^2z/pi = 2r dr and b=(a+p)/2.
            b = (a+p)/2
            integral = simpson(lambda r: 2*r*math.exp(-b*r*r), 12/math.sqrt(b))
            checks.append(abs(integral-1/b) < 1e-11)
    for p, p0, omega in ((.8, 1.4, .2), (.3, .9, .4), (2., .7, .45)):
        def logratio(x):
            return math.lgamma(.25+(x-omega)/2)-math.lgamma(.25+(x+omega)/2)
        exact = logratio(p)-logratio(p0)
        nmax = 20000
        finite = math.fsum(math.log1p(2*omega/(2*n+.5+p-omega))
                           -math.log1p(2*omega/(2*n+.5+p0-omega))
                           for n in range(nmax))
        amin = 2*nmax+.5+min(p, p0)-omega
        bound = 2*omega*abs(p-p0)*(amin**-2+1/(2*amin))
        checks.append(abs(finite-exact) < bound+1e-12)
        def heat(u):
            if u == 0:
                return omega*(p0-p)
            return ((math.exp(-p*u)-math.exp(-p0*u))*2*math.sinh(omega*u)/u
                    *math.exp(-u/2)/(-math.expm1(-2*u)))
        checks.append(abs(simpson(heat, 120., 65536)-exact) < 2e-8)
    group('F. free Robin boundary Gaussian and normalized gamma ratio', checks,
          'On-shell action, complex Gaussian quadrature, finite product with tail bound and heat integral', 2e-8)

    print(json.dumps(dict(schema=1, date='2026-09-19', model='OpenAI GPT-6 (Codex)',
                          groups=GROUPS, total_checks=sum(g['cases'] for g in GROUPS),
                          **{'pass': all(g['pass'] for g in GROUPS)},
                          scope='Finite checks of free angular smearing, the difference form and a projected Robin model; no interacting gauge-theory or arithmetic realization.'), indent=2))


if __name__ == '__main__':
    main()
