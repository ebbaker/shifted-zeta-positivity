#!/usr/bin/env python3
"""Exact rational-polynomial audit of the signed curvature split lemma.

This checks algebra and controls, not the unproved theta slack inequality.
No optional arithmetic packages are needed.
Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded model gpt-6-astra, reasoning effort ultra.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

NAMES = ('h', 's', 'G', 'R', 'mu', 'kap', 'rho', 'E', 'a', 'D', 'z')
NV = len(NAMES)
ZERO = (0,) * NV

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {k:F(v) for k,v in value.items() if v}
        else:
            self.terms = {ZERO:F(value)} if value else {}
    @staticmethod
    def var(name):
        e = [0]*NV
        e[NAMES.index(name)] = 1
        return P({tuple(e):F(1)})
    def __add__(self, other):
        out = dict(self.terms)
        for e,c in P(other).terms.items(): out[e] = out.get(e,F(0))+c
        return P(out)
    __radd__ = __add__
    def __neg__(self): return P({e:-c for e,c in self.terms.items()})
    def __sub__(self, other): return self+-P(other)
    def __rsub__(self, other): return P(other)+-self
    def __mul__(self, other):
        out = {}
        for e,c in self.terms.items():
            for f,d in P(other).terms.items():
                ef=tuple(x+y for x,y in zip(e,f))
                out[ef]=out.get(ef,F(0))+c*d
        return P(out)
    __rmul__=__mul__
    def __pow__(self, n):
        out=P(1)
        for _ in range(n): out=out*self
        return out
    def sub(self, **values):
        out=P(0)
        for e,c in self.terms.items():
            term=P(c)
            for name,power in zip(NAMES,e):
                if power: term=term*(P(values[name]) if name in values else P.var(name))**power
            out=out+term
        return out
    def scalar(self):
        assert not any(any(e) for e in self.terms)
        return self.terms.get(ZERO,F(0))
    def serial(self):
        return [{'powers':{name:k for name,k in zip(NAMES,e) if k},'coefficient':str(c)}
                for e,c in sorted(self.terms.items())]

h,s,G,R,mu,kap,rho,E,a,D,z=(P.var(n) for n in NAMES)
checks=[]

def equal(name, lhs, rhs):
    residual=lhs-rhs
    assert not residual.terms, (name,residual.serial())
    checks.append({'name':name,'passed':True,'residual_terms':0})

def truth(name, value):
    assert value, name
    checks.append({'name':name,'passed':True})

L = mu*h*h+h*(G+R)+s*(s+2*a*h)
slack = 4*kap*h*G+rho*rho*E-R*R
rhs=(R+2*kap*h)**2+slack+4*kap*(mu-kap)*h*h+4*kap*s*(s+2*a*h)
equal('F2_full_stationary_ideal_identity',4*kap*L+rho*rho*E,rhs)
equal('F2_true_stationarity', (4*kap*L+rho*rho*E).sub(s=0),rhs.sub(s=0))
equal('joint_zero_residual_obstruction',slack.sub(h=0,E=0),-R*R)
equal('vacuous_split_warning',slack.sub(G=G+R+2*kap*h,R=-2*kap*h),
      4*kap*h*(G+R)+4*kap*kap*h*h+rho*rho*E)

favorable=slack.sub(h=-D,G=-2,R=mu*D,E=D*D)
equal('favorable_double_slack',favorable,8*kap*D+(rho*rho-mu*mu)*D*D)
equal('favorable_double_L',L.sub(h=-D,G=-2,R=mu*D,E=D*D,s=0),2*D)
adverse=slack.sub(h=2*z,G=-2,R=-2*mu*z,E=4*z*z)
equal('adverse_double_slack',adverse,-16*kap*z+4*(rho*rho-mu*mu)*z*z)
equal('adverse_double_L',L.sub(h=2*z,G=-2,R=-2*mu*z,E=4*z*z,s=0),-4*z)
cubic=slack.sub(h=6*z,G=-6,R=-6*mu*z,E=36*z*z)
equal('adverse_cubic_slack',cubic,-144*kap*z+36*(rho*rho-mu*mu)*z*z)
equal('adverse_cubic_L',L.sub(h=6*z,G=-6,R=-6*mu*z,E=36*z*z,s=0),-36*z)

small=F(1,1000)
favval=favorable.sub(D=small,mu=1,kap=1,rho=0).scalar()
advval=adverse.sub(z=small,mu=1,kap=1,rho=0).scalar()
cubval=cubic.sub(z=small,mu=1,kap=1,rho=0).scalar()
truth('favorable_double_passes_rho_zero',favval>0)
truth('adverse_double_rejected',advval<0)
truth('adverse_cubic_rejected',cubval<0)
old_ratio=(F(-2)+small)**2/(small**2)
truth('whole_residual_ratio_large_in_favorable_control',old_ratio>1000000)

record={'schema':'inv21-signed-curvature-split-exact-v1',
        'date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial','model':'gpt-6-astra','effort':'ultra',
        'scope':'Exact polynomial identities and synthetic controls; no theta positivity or all-height claim.',
        'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'passed':len(checks),'failed':0,
        'exact_diagnostics':{'favorable_slack':str(favval),'adverse_double_slack':str(advval),
                             'adverse_cubic_slack':str(cubval),'whole_residual_square_ratio':str(old_ratio)},
        'symbolic_slacks':{'favorable_double':favorable.serial(),'adverse_double':adverse.serial(),
                           'adverse_cubic':cubic.serial()}}
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path)
args=parser.parse_args()
if args.output: args.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'failed':0,'output':str(args.output) if args.output else None}))
