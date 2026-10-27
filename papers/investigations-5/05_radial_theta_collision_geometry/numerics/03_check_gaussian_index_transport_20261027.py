"""Exact rational checks for RTC-05 Note04.

Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), actual recorded effort max; 27 October 2026.

Checks polynomial/rational identities, not sampled approximate identities.
Convergence, degree theory and inequality domains are proved in Note04.
No theta values or unknown canonical collision locations are evaluated.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

N = 10
ZERO = (0,) * N
NAMES = ["t", "a", "rho", "T", "A", "u", "v", "gamma", "y", "c"]


def pc(v):
    return {ZERO: Q(v)} if v else {}


def padd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def pscale(a, b):
    return {k: v*b for k, v in a.items() if v*b}


def pmul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(i+j for i, j in zip(ka, kb))
            out[k] = out.get(k, Q(0)) + va*vb
    return {k: v for k, v in out.items() if v}


def pdiff(a, j):
    out = {}
    for k, v in a.items():
        if k[j]:
            kk = list(k)
            kk[j] -= 1
            out[tuple(kk)] = v*k[j]
    return out


class R:
    def __init__(self, n=0, d=None):
        self.n = n if isinstance(n, dict) else pc(n)
        self.d = pc(1) if d is None else d
        if not self.d:
            raise ZeroDivisionError
        if not self.n:
            self.d = pc(1)
        elif set(self.d) == {ZERO}:
            self.n = pscale(self.n, 1/self.d[ZERO])
            self.d = pc(1)

    @staticmethod
    def as_r(v):
        return v if isinstance(v, R) else R(v)

    def __add__(self, other):
        other = R.as_r(other)
        if self.d == other.d:
            return R(padd(self.n, other.n), self.d)
        return R(padd(pmul(self.n, other.d), pmul(other.n, self.d)), pmul(self.d, other.d))

    __radd__ = __add__

    def __neg__(self):
        return R(pscale(self.n, -1), self.d)

    def __sub__(self, other):
        return self + (-R.as_r(other))

    def __rsub__(self, other):
        return R.as_r(other) + (-self)

    def __mul__(self, other):
        other = R.as_r(other)
        return R(pmul(self.n, other.n), pmul(self.d, other.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = R.as_r(other)
        return R(pmul(self.n, other.d), pmul(self.d, other.n))

    def __rtruediv__(self, other):
        return R.as_r(other)/self

    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        out = R(1)
        for _ in range(k):
            out *= self
        return out

    def __eq__(self, other):
        other = R.as_r(other)
        return pmul(self.n, other.d) == pmul(other.n, self.d)

    def diff(self, j):
        return R(padd(pmul(pdiff(self.n, j), self.d),
                      pscale(pmul(self.n, pdiff(self.d, j)), -1)),
                 pmul(self.d, self.d))

    def is_zero(self):
        return not self.n


def variable(j):
    k = [0]*N
    k[j] = 1
    return R({tuple(k): Q(1)})


t, a, rho, T0, A0, u, v, gamma, y, c = [variable(j) for j in range(N)]
d = 1-rho**2
Delta = 1-d*t
T = rho**2*t/Delta
A = rho*a/Delta
k = rho/Delta
ell = -d*a/(2*Delta)
logW_t = d/(2*Delta)-d**2*a**2/(4*Delta**2)
logW_rho = -rho*t/Delta+rho*a**2/(2*Delta**2)

# Complete transformed physical heat equation, coefficient by coefficient.
assert T.diff(0) == k**2
assert A.diff(0)+2*ell*k == 0
assert logW_t+ell.diff(1)+ell**2 == 0
assert T.diff(0)*A.diff(1)-T.diff(1)*A.diff(0) == rho**3/Delta**3

# Auxiliary source evolution transferred through the complete observation.
p = 2*t*(t-1)
q = (2*t-1)*a
m = t-a**2/2
assert -rho*T.diff(2) == p*T.diff(0)+q*T.diff(1)
assert -rho*A.diff(2) == p*A.diff(0)+q*A.diff(1)
assert -rho*logW_rho == p*logW_t+q*ell+m

# The Gaussian kernel itself satisfies the source Fokker--Planck equation.
e = u-rho*v
log_kernel_s = -rho**2/d-2*e*rho*v/d+2*rho**2*e**2/d**2
log_kernel_u = -2*e/d
assert log_kernel_s == (log_kernel_u**2+log_kernel_u.diff(5))/2+1+u*log_kernel_u

# Full normal-form composition for operators in partial_t and partial_a.
def op_add(x, z):
    out = dict(x)
    for order, coefficient in z.items():
        out[order] = out.get(order, R(0))+coefficient
    return {o: f for o, f in out.items() if not f.is_zero()}


def op_scale(x, z):
    return {o: f*z for o, f in x.items() if not (f*z).is_zero()}


def repeat_diff(f, j, n):
    for _ in range(n):
        f = f.diff(j)
    return f


def compose(x, z):
    out = {}
    for (it, ia), f in x.items():
        for (jt, ja), g in z.items():
            for kt in range(it+1):
                for ka in range(ia+1):
                    dg = repeat_diff(repeat_diff(g, 0, kt), 1, ka)
                    order = (it-kt+jt, ia-ka+ja)
                    term = f*dg*comb(it, kt)*comb(ia, ka)
                    out[order] = out.get(order, R(0))+term
    return {o: f for o, f in out.items() if not f.is_zero()}


B = {(1, 0): R(1), (0, 2): R(1)}
X = {(1, 0): p, (0, 1): q, (0, 0): m}
commutator = op_add(compose(B, X), op_scale(compose(X, B), -1))
assert commutator == op_scale(B, 4*t-2)

# Exact inverse event map and all-multiplicity orbit geometry.
event_q = T0+(1-T0)*rho**2
event_t = T0/event_q
event_a = A0*rho/event_q
event_Delta = 1-d*event_t
assert rho**2*event_t/event_Delta == T0
assert rho*event_a/event_Delta == A0
assert -rho*event_t.diff(2) == 2*event_t*(1-event_t)
assert -rho*event_a.diff(2) == (1-2*event_t)*event_a
assert event_a**2*T0*(1-T0) == A0**2*event_t*(1-event_t)
assert A**2*t*(1-t) == a**2*T*(1-T)

rho_c_squared = T0*(1-c)/(c*(1-T0))
q_at_c = T0+(1-T0)*rho_c_squared
assert T0/q_at_c == c
assert A0**2*rho_c_squared/q_at_c**2 == A0**2*c*(1-c)/(T0*(1-T0))

# The control's full transform polynomial, and its heat equation.
P = y**2-12*gamma*y+R(Q(3, 2))*gamma**4+12*gamma**2
P_at_vertex = (6*gamma)**2-12*gamma*(6*gamma)+R(Q(3, 2))*gamma**4+12*gamma**2
assert P.diff(8) == 2*y-12*gamma
assert P_at_vertex == R(Q(3, 2))*gamma**2*(gamma**2-16)
assert (12*gamma)**2-4*(R(Q(3, 2))*gamma**4+12*gamma**2) == 6*gamma**2*(16-gamma**2)
polynomial_factor = 6+48/gamma**2-48*a**2/gamma**3+4*a**4/gamma**4
assert -polynomial_factor.diff(7)+polynomial_factor.diff(1).diff(1)-a/gamma*polynomial_factor.diff(1) == 0
assert 6+Q(48, 16)-Q(48, 64)*a**2+Q(4, 256)*a**4 == (a**2-24)**2/64

# Complete control wall and top-face calculations use rational endpoints.
gmin = Q(31, 8)
wall_polynomial = Q(28)**2-12*gmin*28+Q(3, 2)*gmin**4+12*gmin**2
wall_derivative = 6*gmin**3+24*gmin-336
assert wall_polynomial == Q(3203, 8192) > 0
assert wall_derivative == Q(27165, 256) > 0
assert Q(28)*Q(3, 8)*Q(5, 8)/(Q(1, 4)*Q(3, 4)) == 35 < 36
event_T, event_A2 = Q(1, 4), Q(24)
b0, c0, R0 = Q(1, 8), Q(3, 8), Q(6)
cross_rho2 = event_T*(1-c0)/(c0*(1-event_T))
cross_a2 = event_A2*c0*(1-c0)/(event_T*(1-event_T))
assert cross_rho2 == Q(5, 9)
assert cross_a2 == 30 < R0**2
rho_half2 = Q(1, 4)
event_t_half = event_T/(event_T+(1-event_T)*rho_half2)
mapped_top_half = rho_half2*c0/(1-(1-rho_half2)*c0)
assert event_t_half == Q(4, 7) > c0
assert mapped_top_half == Q(3, 23) < event_T
assert b0 < event_T < c0

record = {
    "date": "2026-10-27", "timezone": "America/New_York",
    "prepared_for": "Edward Baker", "llm_assistance": "substantial",
    "model": "gpt-6-astra", "effort": "max", "status": "passed",
    "scope": "Exact multivariate rational identities and analytic-control endpoint arithmetic; no theta sampling",
    "verified_identities": [
        "Transformed physical heat equation, all coefficient terms",
        "Positive coordinate-map Jacobian rho^3/Delta^3",
        "Source Gaussian kernel equation and complete auxiliary observation generator",
        "[partial_t+partial_a^2,X]=(4t-2)(partial_t+partial_a^2) as differential operators",
        "Exact inverse collision map and logistic/elliptical orbit identities",
        "Upper-time crossing parameter and height formula",
        "Gaussian-polynomial control heat equation and complete common-zero polynomial"
    ],
    "control": {
        "source": "(64u^4+6)exp(-17u^2/4)",
        "domain": {"time_lower": "1/8", "time_upper": "3/8", "frequency_lower": "0", "frequency_upper": "6"},
        "original_event": {"time": "1/4", "frequency_squared": "24", "multiplicity": 2},
        "top_crossing": {"rho_squared": "5/9", "time": "3/8", "frequency_squared": "30"},
        "wall_checks": {
            "P_gamma31over8_at_28": str(wall_polynomial),
            "gamma_derivative_lower": str(wall_derivative),
            "all_deformed_root_frequency_squared_upper": "35",
            "right_wall_squared": "36",
            "ordinary_right_wall_flux": 0,
            "lower_time_root_count": 0
        },
        "degree_rho1": -1,
        "degree_rho_half": 0,
        "degree_basis": "Inherited exact wall-flux theorem plus the polynomial root classification proved in Note04; not a sampled winding",
        "boundary_at_crossing": "joint zero; winding undefined",
        "event_time_rho_half": str(event_t_half),
        "mapped_top_time_rho_half": str(mapped_top_half)
    },
    "analytical_not_computational": [
        "Gaussian integration, source convergence, tail rate and limit are proved in Note04",
        "General local index and physical wall-flux theorem are inherited at stated scope",
        "Finite positive anchor uses unevaluated complete canonical moments",
        "No canonical event, zero-degree constraint, Newman bound or independent review is claimed"
    ],
    "review_scope": "same-assistant exact algebra and self-assessment"
}
out = Path(__file__).with_name("03_GAUSSIAN_INDEX_TRANSPORT_CHECKS_20261027.json")
out.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({"status": "passed", "record": str(out), "control_degree_change": [-1, 0], "theta_sampling": False}))
