#!/usr/bin/env python3
"""Paid dual identities, exact norm controls, and an actual-height rank witness.

This does not certify a negative candidate threshold or a theta collision.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import importlib.util
import json
import math


class P:
    size = 0
    def __init__(self, value=0):
        if isinstance(value, P):
            self.a = dict(value.a)
        elif isinstance(value, dict):
            self.a = {k: F(v) for k, v in value.items() if v}
        else:
            self.a = {} if not value else {(0,)*self.size: F(value)}
    @classmethod
    def var(cls, i):
        key = [0]*cls.size
        key[i] = 1
        return cls({tuple(key): F(1)})
    def __add__(self, other):
        out = dict(self.a)
        for key, value in P(other).a.items():
            out[key] = out.get(key, F(0))+value
        return P(out)
    __radd__ = __add__
    def __neg__(self):
        return P({key: -value for key, value in self.a.items()})
    def __sub__(self, other):
        return self+-P(other)
    def __rsub__(self, other):
        return P(other)+-self
    def __mul__(self, other):
        out = {}
        for key, value in self.a.items():
            for second, coefficient in P(other).a.items():
                combined = tuple(a+b for a, b in zip(key, second))
                out[combined] = out.get(combined, F(0))+value*coefficient
        return P(out)
    __rmul__ = __mul__
    def __truediv__(self, other):
        return self*F(1, other)
    def __pow__(self, power):
        result = P(1)
        for _ in range(power):
            result *= self
        return result
    def __eq__(self, other):
        return self.a == P(other).a


checks = 0
families = []
def check(condition):
    global checks
    assert condition, f'Exact assertion {checks+1} failed'
    checks += 1

def variables(n):
    P.size = n
    return [P.var(i) for i in range(n)]

def quad(a, q, b):
    return sum((a[i]*q[i][j]*b[j]
                for i in range(len(a)) for j in range(len(b))), 0)

def transpose(a):
    return list(map(list, zip(*a)))

def mmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def inverse(a):
    n = len(a)
    work = [list(row)+[F(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if work[i][col])
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        work[col] = [entry/value for entry in work[col]]
        for row in range(n):
            if row != col:
                factor = work[row][col]
                work[row] = [a-factor*b for a, b
                             in zip(work[row], work[col])]
    return [row[n:] for row in work]

def determinant(a):
    n = len(a)
    result = 0
    for perm in permutations(range(n)):
        term = (-1)**sum(perm[i] > perm[j] for i in range(n)
                         for j in range(i+1, n))
        for i in range(n):
            term *= a[i][perm[i]]
        result += term
    return result

def qmatrix(gamma, lam, b):
    return [[lam[0], lam[1], *b[0]], [lam[1], lam[2], *b[1]],
            [b[0][0], b[1][0], -gamma, 0, F(3, 2)],
            [b[0][1], b[1][1], 0, 2, 0],
            [b[0][2], b[1][2], F(3, 2), 0, 0]]

def feature(rho, eps):
    return [1, eps*rho, rho**2, 0, rho**4], [0, rho, 0, rho**3, 0]

# Symbolic candidate-null identity and all four trigonometric signs.
rn, rm, eps, gam, l00, l01, l11, *tail = variables(17)
b = [tail[:3], tail[3:6]]
cn, sn, cm, sm = tail[6:]
q = qmatrix(gam, [l00, l01, l11], b)
r, s = feature(rn, eps)
rr, ss = feature(rm, eps)
R, S = quad(r, q, rr), quad(s, q, ss)
C, Ct = quad(r, q, ss), quad(s, q, rr)
direct = quad([r[i]*cn+s[i]*sn for i in range(5)], q,
              [rr[i]*cm+ss[i]*sm for i in range(5)])
channels = ((R+S)*(cn*cm+sn*sm)+(R-S)*(cn*cm-sn*sm)
            +(Ct-C)*(sn*cm-cn*sm)+(C+Ct)*(sn*cm+cn*sm))/2
check(direct == channels)
e0, e1, x2, y3, x4, gam, l00, l01, l11, *tail = variables(15)
b = [tail[:3], tail[3:]]
q = qmatrix(gam, [l00, l01, l11], b)
e, u = [e0, e1], [x2, y3, x4]
check(quad(e+u, q, e+u) == 2*y3*y3+3*x2*x4-gam*x2*x2
      +l00*e0*e0+2*l01*e0*e1+l11*e1*e1
      +2*sum((e[i]*b[i][j]*u[j] for i in range(2) for j in range(3)), 0))
W, scale, x2, y3, x4, gam = variables(6)
check(2*(W*scale**3*y3)**2+3*(W*scale**2*x2)*(W*scale**4*x4)
      -gam*(W*scale**2*x2)**2
      == W*W*scale**4*(scale*scale*(2*y3*y3+3*x2*x4)-gam*x2*x2))
families.append('Exact dual identity, normalized threshold, and four pair-channel signs')

# Every dual tolerance is paid on rational controls, including mixed terms.
for seed in range(1, 41):
    lam = [F(seed-19, 7), F(11-seed, 9), F(seed-23, 13)]
    b = [[F(seed*(i+1)-(j+1)*13, 17+j) for j in range(3)] for i in range(2)]
    u = [F(seed-17, 5), F(2*seed-31, 7), F(9-seed, 11)]
    bounds = [F(seed, 47), F(seed+3, 61)]
    for sig in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        e = [sig[i]*bounds[i] for i in range(2)]
        remainder = (lam[0]*e[0]**2+2*lam[1]*e[0]*e[1]+lam[2]*e[1]**2
                     +2*sum(e[i]*b[i][j]*u[j] for i in range(2) for j in range(3)))
        paid = (abs(lam[0])*bounds[0]**2+2*abs(lam[1])*bounds[0]*bounds[1]
                +abs(lam[2])*bounds[1]**2
                +2*sum((bounds[0]*abs(b[0][j])+bounds[1]*abs(b[1][j]))*abs(u[j])
                       for j in range(3)))
        check(abs(remainder) <= paid)
families.append('Both lower-coordinate tolerances and all quadratic/cross dual payments')

# Exact common-frequency controls: n=2^k, one rational unit-complex generator.
def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def cpow(z, k):
    out = (F(1), F(0))
    for _ in range(k):
        out = cmul(out, z)
    return out

for count in range(2, 9):
    indices = [2**k for k in range(count)]
    logs = {n: F(k, 3) for k, n in enumerate(indices)}
    phases = {n: cmul((F(5, 13), F(12, 13)), cpow((F(3, 5), F(4, 5)), k))
              for k, n in enumerate(indices)}
    weights = {n: F(1, k+2) for k, n in enumerate(indices)}
    eps, mu, gam = F(1, 7), F(4, 3), F(1, 11)
    q = qmatrix(gam, [F(-2), F(1, 5), F(3)],
                [[F(1), F(-2, 3), F(1, 7)], [F(-3, 5), F(2), F(-1)]])
    moment = [F(0)]*5
    ratios, products = {}, {}
    paired = F(0)
    for n in indices:
        r, s = feature(logs[n]-mu, eps)
        cn, sn = phases[n]
        for i in range(5):
            moment[i] += weights[n]*(r[i]*cn+s[i]*sn)
        for m in indices:
            rr, ss = feature(logs[m]-mu, eps)
            cm, sm = phases[m]
            R, S = quad(r, q, rr), quad(s, q, ss)
            C, Ct = quad(r, q, ss), quad(s, q, rr)
            diff = ((R+S)*(cn*cm+sn*sm)+(Ct-C)*(sn*cm-cn*sm))/2
            prod = ((R-S)*(cn*cm-sn*sm)+(C+Ct)*(sn*cm+cn*sm))/2
            term = weights[n]*weights[m]*(diff+prod)
            check(term == weights[n]*weights[m]*quad(
                [r[i]*cn+s[i]*sn for i in range(5)], q,
                [rr[i]*cm+ss[i]*sm for i in range(5)]))
            g = math.gcd(n, m)
            key = (n//g, m//g)
            ratios[key] = ratios.get(key, F(0))+weights[n]*weights[m]*diff
            products[n*m] = products.get(n*m, F(0))+weights[n]*weights[m]*prod
            paired += term
    check(paired == quad(moment, q, moment))
    check(sum(ratios.values())+sum(products.values()) == paired)
families.append('Complete ordered pairs and reduced-ratio/product regrouping on one-frequency powers')

# Symbolic actual-frequency three-term control, arbitrary carrier and centering.
h, mu, co, si, gam, eps = variables(6)
mom = [sum((F(w)*(-1)**k*(k*h-mu)**j for k, w in enumerate((1, 2, 1))), P(0))
       for j in range(5)]
check(mom[0] == 0)
check(mom[1] == 0)
check(mom[2] == 2*h*h)
check(mom[3] == 6*h*h*(h-mu))
check(mom[4] == 2*h*h*(6*(h-mu)**2+h*h))
check(mom[1]*si+eps*mom[1]*co == 0)
control = 2*(mom[3]*si)**2+3*(mom[2]*co)*(mom[4]*co)-gam*(mom[2]*co)**2
check(control == 4*h**4*(18*(h-mu)**2*si*si
                          +(18*(h-mu)**2+3*h*h-gam)*co*co))
check(co*((2*h-mu)*(si+eps*co))-co*((-mu)*(si+eps*co))
      == 2*h*co*(si+eps*co))
for k in range(1, 21):
    hh, center, gamma = F(k, 7), F(k+3, 5), F(-k, 11)
    for cosine, sine in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)),
                         (F(0), F(1)), (F(1), F(0))):
        value = 4*hh**4*(18*(hh-center)**2*sine*sine
                         +(18*(hh-center)**2+3*hh*hh-gamma)*cosine*cosine)
        check(value >= 4*hh**4*min(18*(hh-center)**2,
                                  18*(hh-center)**2+3*hh*hh-gamma) > 0)
families.append('Three-term positive coefficient control, both candidates, and uniform positive threshold')

# Exact Gram/Schur projection and feasible conditioned states of both signs.
rows = []
for k in range(5):
    rho, sign = F(k-2), (-1)**k
    co, si, eps = sign*F(3, 5), sign*F(4, 5), F(1, 7)
    rows.append([co, rho*(si+eps*co), rho*rho*co, rho**3*si, rho**4*co])
gram = [[sum((row[i]*row[j]/5 for row in rows), F(0))
         for j in range(5)] for i in range(5)]
G = [row[:2] for row in gram[:2]]
C = [row[2:] for row in gram[:2]]
J = [row[2:] for row in gram[2:]]
coef = mmul(inverse(G), C)
adjustment = mmul(transpose(C), coef)
H = [[J[i][j]-adjustment[i][j] for j in range(3)] for i in range(3)]
residuals = [[row[j+2]-sum(row[k]*coef[k][j] for k in range(2))
              for j in range(3)] for row in rows]
for i in range(3):
    for j in range(3):
        check(H[i][j] == sum((r[i]*r[j]/5 for r in residuals), F(0)))
    check(determinant([row[:i+1] for row in H[:i+1]]) > 0)
for residual in transpose(residuals):
    for col in range(2):
        check(sum((rows[k][col]*residual[k]/5 for k in range(5)), F(0)) == 0)
witnesses = []
for target in ([F(0), F(1), F(0)], [F(1), F(0), F(-2)]):
    coefficients = mmul(inverse(H), [[v] for v in target])
    state = [sum(r[j]*coefficients[j][0] for j in range(3)) for r in residuals]
    norm = sum((v*v/5 for v in state), F(0))
    scaling = 1/(1+norm)
    state = [v*scaling for v in state]
    measured = [sum((state[k]*rows[k][j]/5 for k in range(5)), F(0))
                for j in range(5)]
    check(measured[:2] == [0, 0])
    check(measured[2:] == [v*scaling for v in target])
    check(sum((v*v/5 for v in state), F(0)) <= 1)
    threshold = 2*measured[3]**2+3*measured[2]*measured[4]-measured[2]**2
    check((threshold > 0) if target[1] else (threshold < 0))
    witnesses.append({'moments': list(map(str, measured)),
                      'relaxed_threshold': str(threshold)})
check(determinant([[F(-1), F(3, 2)], [F(3, 2), F(0)]]) == F(-9, 4))
families.append('Exact Schur residual Gram, positive definiteness, and both-sign norm-ball witnesses')

# Genuine common-height interval rank witness; hash-bound source, local powers.
source = Path(__file__).resolve()
dependency = source.parents[2]/'13_microlocal_phase_space/numerics/check_block_current.py'
dependency_hash = hashlib.sha256(dependency.read_bytes()).hexdigest()
expected_hash = '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2'
assert dependency_hash == expected_hash, 'Imported interval source changed; review and rebind before replay'
spec = importlib.util.spec_from_file_location('phase_current_intervals', dependency)
arith = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arith)
I = arith.I
integer_power_calls = 0
def exact_integer_power(interval, exponent):
    """Exact rational endpoint powers followed by directed division.

    Does not rely on the C Decimal Context.power rounding guarantee.
    The imported source remains unchanged on disk.
    """
    global integer_power_calls
    assert isinstance(exponent, int) and exponent >= 0
    integer_power_calls += 1
    if exponent == 0:
        return I(1)
    endpoint_powers = [F(interval.lo)**exponent, F(interval.hi)**exponent]
    if exponent % 2 == 0 and interval.lo <= 0 <= interval.hi:
        endpoint_powers.append(F(0))
    lower, upper = min(endpoint_powers), max(endpoint_powers)
    return I(arith.DOWN.divide(arith.Decimal(lower.numerator), arith.Decimal(lower.denominator)),
             arith.UP.divide(arith.Decimal(upper.numerator), arith.Decimal(upper.denominator)))
I.__pow__ = exact_integer_power
pi = arith.pi_interval()
M = 22066
logM = I(M).ln()
t, x = 1/(2*logM), 4*pi*M*M
x2 = x*x
atanx = pi/2-arith.atan_small(1/x, 6)
correction = (1+1/x2).ln()
ar = logM+correction/4-1/(1+x2)
ai = 3*x/(1+x2)-atanx/2
U, V = (7*x2-5)/((1+x2)**2), x*(x2+5)/((1+x2)**2)
c, d = (1+t*U/2)/2, t*V/4
Omega = (ar*(1+t*U/2)-ai*t*V/2)/2
mu, eps = Omega/c, d/c
T = (x-t*ai)/2
carrier = pi*(M % 2)-pi+atanx/4-x*correction/8+t*ai*(ar-logM)/2
nodes = [1, 2, 8, 128, 11033]
node_rows = []
for n in nodes:
    logn = I(n).ln()
    rho = logn-mu
    sine, cosine = arith.reduced_trig(carrier-T*(logM-logn), pi)
    node_rows.append([cosine, rho*(sine+eps*cosine), rho**2*cosine,
                      rho**3*sine, rho**4*cosine])
interval_det = determinant(node_rows)
assert interval_det.lo > 155000000
assert interval_det.hi < 156000000
assert interval_det.width() < arith.Decimal('1e-30')
assert t.hi < arith.Decimal('0.05')
assert c.lo > arith.Decimal('0.49')
families.append('Outward interval positive rank witness at genuine N=22066 physical height')
record = {
    'date': '2026-10-10', 'checker': source.name,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'assertions_passed': checks, 'families': families,
    'exact_arithmetic': 'Python standard-library Fraction sparse polynomials and matrices',
    'relaxation_inertia_if_residual_Gram_positive_definite': [2, 1, 0],
    'exact_common_frequency_relaxation_witnesses': witnesses,
    'actual_height_rank_witness': {
        'N': M, 'kappa': '1', 'time_definition': '1/(2*log(22066))',
        'height_definition': '4*pi*22066^2', 'time_interval': t.strings(),
        'height_interval': x.strings(), 'mu_interval': mu.strings(),
        'selected_nodes': nodes,
        'feature_columns': ['cos(phi)', 'rho*(sin(phi)+(d/c)*cos(phi))',
                            'rho^2*cos(phi)', 'rho^3*sin(phi)', 'rho^4*cos(phi)'],
        'node_determinant_interval': interval_det.strings(),
        'determinant_width': str(interval_det.width()),
        'decimal_precision': arith.PRECISION,
        'integer_power_method': 'Exact Fraction(endpoint)^integer with directed Decimal division; local override of imported I.__pow__, source unchanged.',
        'exact_integer_power_calls': integer_power_calls,
        'imported_interval_source': '../../13_microlocal_phase_space/numerics/check_block_current.py',
        'imported_interval_source_sha256': dependency_hash,
        'consequence': 'All prescribed weights are positive, so complete five-feature Gram and its residual Schur complement are positive definite at this genuine noncandidate state.',
    },
    'scope': 'Paid dual identities and precise norm-relaxation loss. Genuine-height rank only, not a candidate, negative threshold certificate, heat collision, or independent validation.',
}
target = source.with_name('paid_dual_kernel_record_20261010.json')
target.write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
print(json.dumps({'record': target.name, 'exact_assertions': checks,
                  'actual_node_determinant': interval_det.strings()}, sort_keys=True))
