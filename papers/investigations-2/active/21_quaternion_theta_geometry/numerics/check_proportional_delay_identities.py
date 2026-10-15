#!/usr/bin/env python3
"""Exact finite-algebra controls for a complete-source polarization.

Prepared for Edward Baker with LLM assistance, 14 October 2026.
Recorded parent model: gpt-6.1-sol; reasoning effort: ultra.
These checks validate identities and negative controls, not theta signs.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


class P:
    """Sparse polynomials over Q with arbitrary named variables."""
    def __init__(self, value=0):
        self.d = value.d.copy() if isinstance(value, P) else ({(): F(value)} if value else {})

    @staticmethod
    def var(name):
        p = P()
        p.d = {((name, 1),): F(1)}
        return p

    def __add__(self, other):
        p = P(self)
        for m, c in P(other).d.items():
            p.d[m] = p.d.get(m, F(0)) + c
            if not p.d[m]:
                del p.d[m]
        return p

    __radd__ = __add__

    def __neg__(self):
        p = P()
        p.d = {m: -c for m, c in self.d.items()}
        return p

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        if isinstance(other, Z):
            return NotImplemented
        p = P()
        for m, c in self.d.items():
            for n, d in P(other).d.items():
                powers = dict(m)
                for key, power in n:
                    powers[key] = powers.get(key, 0) + power
                key = tuple(sorted(powers.items()))
                p.d[key] = p.d.get(key, F(0)) + c*d
                if not p.d[key]:
                    del p.d[key]
        return p

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = P(1)
        for _ in range(exponent):
            result = result*self
        return result

    def __eq__(self, other):
        return self.d == P(other).d


class Z:
    def __init__(self, real=0, imag=0):
        if isinstance(real, Z):
            self.r, self.i = P(real.r), P(real.i)
        else:
            self.r, self.i = P(real), P(imag)

    def __add__(self, other):
        other = Z(other)
        return Z(self.r+other.r, self.i+other.i)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-Z(other))

    def __rsub__(self, other):
        return Z(other)-self

    def __mul__(self, other):
        other = Z(other)
        return Z(self.r*other.r-self.i*other.i, self.r*other.i+self.i*other.r)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = Z(1)
        for _ in range(exponent):
            result = result*self
        return result

    def bar(self):
        return Z(self.r, -self.i)


checks = []


def check(name, equality):
    if not equality:
        raise AssertionError(name)
    checks.append({"name": name, "passed": True})


a,b,u,v = map(P.var, ("a","b","u","v"))
W = [Z(P.var("A"), P.var("B")), Z(P.var("C"), P.var("D"))]
q = [Z(-a,u), Z(-a,v)]
d = [u*u-b*b, v*v-b*b]
m = [Z(P.var("R"),P.var("S")),Z(P.var("T"),P.var("U"))]
mu = a*a+b*b

for k in range(2):
    residual = -(q[k]*q[k]+2*a*q[k]+mu)
    check(f"physical_residual_multiplier_atom_{k}", residual.r == d[k] and residual.i == 0)


def pair(j, weights, wrong_conjugation=False):
    total = Z()
    for r in range(2):
        for s in range(2):
            coefficient = weights[r]+(weights[s] if wrong_conjugation else weights[s].bar())
            total += coefficient*W[r]*W[s].bar()*(q[r]*q[s].bar())**j
            total += (weights[r]+weights[s])*W[r]*W[s]*(q[r]*q[s])**j
    return F(1,4)*total.r


for j in (0,1):
    current = sum((W[r]*q[r]**j).r for r in range(2))
    for label, weights in (
        ("retained", [d[r]*m[r] for r in range(2)]),
        ("absorption", [d[r]*(1-F(1,2)*m[r]) for r in range(2)]),
    ):
        filtered = sum((W[r]*q[r]**j*weights[r]).r for r in range(2))
        check(f"complex_{label}_polarization_j{j}", current*filtered == pair(j, weights))
        check(f"missing_Hermitian_conjugation_detected_{label}_j{j}", current*filtered != pair(j, weights, True))
    full_residual = sum((W[r]*q[r]**j*d[r]).r for r in range(2))
    retained = sum((W[r]*q[r]**j*d[r]*m[r]).r for r in range(2))
    absorption = sum((W[r]*q[r]**j*d[r]*(1-F(1,2)*m[r])).r for r in range(2))
    check(f"signed_split_recombination_j{j}", full_residual == absorption+F(1,2)*retained)

h = [P.var(f"h{k}") for k in range(6)]
for j in (0,1):
    C = -h[j+2]-2*a*h[j+1]-mu*h[j]
    L = h[j+1]**2-h[j]*h[j+2]
    check(f"stationary_ideal_identity_j{j}", L-mu*h[j]**2-h[j]*C == h[j+1]*(h[j+1]+2*a*h[j]))

# Treat lower and delayed jets as independent variables; no delayed stationarity.
speed=P.var("speed")
for j in (0,1):
    cur2,cur1,old2,old1=map(P.var,(f"C{j+2}",f"C{j+1}",f"D{j+2}",f"D{j+1}"))
    Gdot=-F(1,2)*old2+speed*old1
    Bdot=-cur2+speed*cur1-F(1,2)*Gdot
    check(f"half_time_absorption_transport_j{j}", Bdot == -cur2+speed*cur1+F(1,4)*old2-F(1,2)*speed*old1)

ra,ta,rb,tb=map(P.var,("ra","ta","rb","tb"))
check("complete_omitted_pair_sectors", (ra+ta)*(rb+tb)-ra*rb == ra*tb+ta*rb+ta*tb)

# alpha = L/2+i*pi/4 gives the exact dominant gamma phase and amplitude.
L,pi,t,rho=map(P.var,("L","pi","t","rho"))
alpha=Z(F(1,2)*L,F(1,4)*pi)
exponent=-F(1,4)*rho*t*(alpha*alpha)
check("proportional_delay_gamma_phase", exponent.i == -F(1,16)*rho*t*pi*L)
check("proportional_delay_gamma_amplitude", exponent.r == -F(1,16)*rho*t*L*L+F(1,64)*rho*t*pi*pi)

# A simple double/cubic collision predecessor forces incompatible linear signs.
A,g=map(P.var,("collision_A","delayed_g"))
retained_linear=A*g
absorption_linear=-A*A-F(1,2)*A*g
check("collision_linear_split_obstruction", absorption_linear+F(1,2)*retained_linear == -A*A)

record={"description":"Exact algebra checks; no theta-sign certification or new height coverage.","model":"gpt-6.1-sol","reasoning_effort":"ultra","check_count":len(checks),"checks":checks,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
output=json.dumps(record,indent=2)+"\n"
if len(sys.argv)>1:
    Path(sys.argv[1]).write_text(output)
else:
    print(output,end="")
