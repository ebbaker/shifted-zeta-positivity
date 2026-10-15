#!/usr/bin/env python3
"""Finite exact algebra audit; not a proof of uniform analytic estimates.

Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded parent model: gpt-6.1-sol; reasoning effort: ultra.
Uses only the Python standard library.  Laurent polynomial differentiation
and clearing the B=1+t*ell, J=1+x*x denominators are implemented independently
of the proposed formulas. The only output is the requested audit receipt.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


NAMES = ('t', 'x', 'ell', 'B', 'J', 'v', 'h', 'z', 'c0', 'c1', 'c2') + tuple('g%d' % k for k in range(5)) + ('y', 'q')
POS = {s: i for i, s in enumerate(NAMES)}
ZERO = (0,) * len(NAMES)


class P:
    """Sparse exact Laurent polynomial; only B,J may have negative powers."""
    def __init__(self, d=None):
        if isinstance(d, P):
            self.d = d.d.copy()
        elif isinstance(d, (int, F)):
            self.d = {ZERO: F(d)} if d else {}
        else:
            self.d = {k: F(v) for k, v in (d or {}).items() if v}

    def __add__(self, other):
        other = P(other)
        z = defaultdict(F, self.d)
        for k, v in other.d.items():
            z[k] += v
        return P(z)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        other = P(other)
        z = defaultdict(F)
        for a, av in self.d.items():
            for b, bv in other.d.items():
                z[tuple(x+y for x, y in zip(a, b))] += av * bv
        return P(z)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            if len(self.d) != 1:
                raise ValueError('negative power needs a monomial')
            (a, v), = self.d.items()
            return P({tuple(n*k for k in a): v**n})
        out = P(1)
        for _ in range(n):
            out = out * self
        return out

    def partial(self, name):
        i = POS[name]
        z = {}
        for a, v in self.d.items():
            if a[i]:
                b = list(a)
                b[i] -= 1
                z[tuple(b)] = v*a[i]
        return P(z)

    def subst(self, name, value):
        i = POS[name]
        out = P()
        for a, v in self.d.items():
            n = a[i]
            b = list(a)
            b[i] = 0
            out += P({tuple(b): v}) * (P(value)**n)
        return out


def var(name):
    a = list(ZERO)
    a[POS[name]] = 1
    return P({tuple(a): F(1)})


globals().update({s: var(s) for s in NAMES})


def normal(p):
    """Clear denominators, then impose the two defining relations exactly."""
    p = P(p)
    for name in ('B', 'J'):
        minimum = min((a[POS[name]] for a in p.d), default=0)
        if minimum < 0:
            p *= var(name)**(-minimum)
    return p.subst('B', 1+t*ell).subst('J', 1+x*x)


def Dt(p):
    # ell and J are independent of t; dB/dt=ell.
    return p.partial('t') + ell*p.partial('B')


def Dx(p):
    # d ell/dx=2x/J, dB/dx=t*d ell/dx, dJ/dx=2x.
    ep = 2*x*J**-1
    return (p.partial('x') + ep*p.partial('ell')
            + t*ep*p.partial('B') + 2*x*p.partial('J'))


checks = []


def identity(name, left, right):
    residual = normal(P(left)-right)
    assert not residual.d, (name, residual.d)
    checks.append({'name': name, 'kind': 'exact_cleared_polynomial_identity', 'pass': True})


def positive(name, polynomial, strict=True):
    """A nonnegative-coefficient polynomial is nonnegative on y,q>=0."""
    p = normal(polynomial)
    assert p.d and all(v >= 0 for v in p.d.values()), (name, p.d)
    if strict:
        assert p.d.get(ZERO, F(0)) > 0, (name, p.d)
    checks.append({'name': name, 'kind': 'exact_nonnegative_coefficient_certificate', 'pass': True})


delta = t*B**-1 * F(1, 2)
ep = 2*x*J**-1
epp = 2*(1-x*x)*J**-2
dt = B**-2 * F(1, 2)
dx = -t*t*ep*B**-2 * F(1, 2)
dtt = -ell*B**-3
dtx = -t*ep*B**-3
dxx = -t*t*epp*B**-2 * F(1, 2) + t**3*ep**2*B**-3

identity('delta_t', Dt(delta), dt)
identity('delta_x', Dx(delta), dx)
identity('delta_tt', Dt(Dt(delta)), dtt)
identity('delta_tx_both_orders', Dt(Dx(delta)), dtx)
identity('delta_xt', Dx(Dt(delta)), dtx)
identity('delta_xx', Dx(Dx(delta)), dxx)


def jet_t(p):
    out = Dt(p)
    for k in range(3):
        out += p.partial('g%d' % k) * (-(1-dt)*var('g%d' % (k+2)))
    return out


def jet_x(p):
    out = Dx(p)
    for k in range(3):
        out += p.partial('g%d' % k) * (var('g%d' % (k+1)) + dx*var('g%d' % (k+2)))
    return out


identity('observation_x_chain', jet_x(g0), g1+dx*g2)
identity('observation_t_chain', jet_t(g0), -(1-dt)*g2)
identity('observation_tt_chain', jet_t(jet_t(g0)), dtt*g2+(1-dt)**2*g4)
identity('observation_tx_chain', jet_x(jet_t(g0)), dtx*g2-(1-dt)*(g3+dx*g4))
identity('observation_mixed_derivatives_commute', jet_x(jet_t(g0)), jet_t(jet_x(g0)))
identity('observation_xx_chain', jet_x(jet_x(g0)), (1+dxx)*g2+2*dx*g3+dx**2*g4)
identity('complete_heat_defect', jet_t(g0)+jet_x(jet_x(g0)), (dt+dxx)*g2+2*dx*g3+dx**2*g4)


def branch(p):
    # Independent total derivative from tau=t-delta(t,xi(t)), xi'=v,
    # current h'=-z and current C'=-c2+v*c1.
    out = Dt(p)+v*Dx(p)
    out += p.partial('h')*(-z)
    out += p.partial('c0')*(-c2+v*c1)
    for k in range(3):
        out += p.partial('g%d' % k)*(
            v*var('g%d' % (k+1))-(1-(Dt(delta)+v*Dx(delta)))*var('g%d' % (k+2)))
    return out


ddot = dt+v*dx
identity('moving_branch_G', branch(g0), v*g1-(1-ddot)*g2)
identity('moving_branch_P', branch(h*g0), -z*g0+h*(v*g1-(1-ddot)*g2))
identity('moving_branch_Q', branch(h*(c0-g0*F(1,2))),
         -z*(c0-g0*F(1,2))+h*(-c2+v*c1-v*g1*F(1,2)+(1-ddot)*g2*F(1,2)))

# f(theta)>=91/30 after multiplying by the positive 2+4theta and
# substituting theta=13/4+y, y>=0.
theta = F(13,4)+y
positive('rational_outer_time_margin_91_over_30',
         theta*(2+4*theta)-theta-F(91,30)*(2+4*theta), strict=False)

# In Q(sqrt(217)), theta_*=(11+sqrt(217))/8 is the positive root.
# Pair representation a+b sqrt(217) avoids a numerical square root.
def quadmul(a, b):
    return (a[0]*b[0]+217*a[1]*b[1], a[0]*b[1]+a[1]*b[0])

root = (F(11,8), F(1,8))
square = quadmul(root, root)
assert (4*square[0]-11*root[0]-6, 4*square[1]-11*root[1]) == (0, 0)
assert 13**2 < 217 < 15**2
checks.append({'name': 'threshold_root_polynomial_and_3_to_13_over_4_bracket',
               'kind': 'exact_quadratic_field_identity_and_integer_inequality', 'pass': True})

# On R=ell/L<=21/10 and theta>=13/4, multiply d>=1/5 by
# 10(1+R theta)>0. Substitute R=21/10-q, theta=13/4+y.
R = F(21,10)-q
positive('amplitude_delay_d_ge_one_fifth', 5*theta-2-2*R*theta)

phase_upper = F(18,16)+F(22,7*64)
assert phase_upper < F(5,4)
assert 1-F(5,4)**2/F(2) == F(7,32)
checks.append({'name': 'paid_full_phase_and_cosine_margin',
               'kind': 'exact_rational_inequalities_given_pi_lt_22_over_7',
               'phase_upper_using_pi_bound': str(phase_upper),
               'remaining_phase_margin': str(F(5,4)-phase_upper),
               'cosine_lower': '7/32', 'pass': True})

# Analytic uniformity makes these finite positive budgets available
# eventually; this audit checks the resulting algebra only.
assert F(7,32)-F(3,32) == F(1,8)
assert 1+F(3,32) < 2
assert F(3,4)-F(1,2)*F(1,4)*2 == F(1,2)
checks.append({'name': 'P_and_Q_normalized_positive_error_budgets',
               'kind': 'exact_rational_margin_budget',
               'P_error_budget': '3/32', 'P_lower': '1/8',
               'current_product_lower': '3/4', 'r_upper': '1/4',
               'delayed_product_absolute_upper': '2', 'Q_lower': '1/2',
               'pass': True})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    receipt = {
        'investigation': '21_quaternion_theta_geometry',
        'date_America_New_York': '2026-10-14',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial; finite algebra audit generated by an analytic subagent.',
        'recorded_parent_model': 'gpt-6.1-sol',
        'recorded_parent_reasoning_effort': 'ultra',
        'configuration_provenance': 'Supplied by the parent agent from its session metadata.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Finite exact symbolic and rational checks only. Does not establish infinite-sum convergence, four-jet asymptotics, uniformity, an evaluated height cutoff, or cusp signs.',
        'checks_count': len(checks),
        'checks': checks,
        'all_passed': True,
    }
    Path(args.output).write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'all_passed': True, 'checks_count': len(checks), 'output': args.output}))


if __name__ == '__main__':
    main()
