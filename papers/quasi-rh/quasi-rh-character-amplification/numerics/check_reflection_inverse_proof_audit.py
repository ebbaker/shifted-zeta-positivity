#!/usr/bin/env python3
"""Scoped exact algebra checks for the September30 reflection/inverse proofs.

No sampled character sum establishes a sieve or an analytic induction here.
Affine coefficient identities are checked identically. Finite local tests use
zero-extended sixth-root exponents and exact valuation/divisor arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import json

class A:
    def __init__(self,d=None):self.d={k:F(v) for k,v in (d or {}).items() if v}
    @staticmethod
    def var(k):return A({k:1})
    @staticmethod
    def coerce(x):return x if isinstance(x,A) else A({'1':F(x)})
    def __add__(self,x):
        x=A.coerce(x);d=dict(self.d)
        for k,v in x.d.items():d[k]=d.get(k,F(0))+v
        return A(d)
    __radd__=__add__
    def __neg__(self):return A({k:-v for k,v in self.d.items()})
    def __sub__(self,x):return self+-A.coerce(x)
    def __rsub__(self,x):return A.coerce(x)+-self
    def __mul__(self,x):return A({k:v*F(x) for k,v in self.d.items()})
    __rmul__=__mul__
    def __truediv__(self,x):return self*(1/F(x))
    def same(self,x):assert self.d==A.coerce(x).d,(self.d,A.coerce(x).d)
    def eval(self,d):return sum(v*(1 if k=='1' else d[k]) for k,v in self.d.items())


def affine_identities():
    vs={x:A.var(x) for x in 'M r ell V A B t g theta v j delta R m z G'.split()}
    M,r,ell,V,Ai,B,t,g,theta,v,j,delta,R,m,z,G=(vs[x] for x in 'M r ell V A B t g theta v j delta R m z G'.split())
    parent=r+3*ell+V
    si=r-Ai-B-t
    Hc=2*r-2*B-M+4*ell+2*V+delta-j
    Nc=r-Ai-B-t-g-v;Vc=B+theta+v+j;Fc=Nc+Vc
    Mc=2*(si-g)-Hc+delta+2*theta
    Dc=ell+Ai+t+g-theta+V
    kappa=M-2*r-2*ell-V-delta+Ai+B-R/2
    lam=Hc-theta-(si-g)
    count=ell+R/2-j+t+g-theta
    identities=[
        (Mc,M-4*ell-2*Ai-2*t-2*g+2*theta-2*V+j),
        (Fc,parent-Dc-2*ell+j),
        (Mc,M-2*Dc-2*ell+j),
        (Fc-Mc,parent-M+Dc),
        (4*Fc-3*Mc,4*parent-3*M+2*(Ai+t+g-theta+V)+j),
        (kappa+Hc+si+B+t+ell+R/2,parent-B-j),
        (kappa+lam+count+2*Fc,parent),
    ]
    D=r+z-2*G;z0=z-G;P1=B-theta
    Fi=D-P1;Mi=2*D-m-2*P1;ki=m-2*D+P1
    identities.extend([
        (Fi-Mi-(P1+G)-z0,m-r-2*z+2*G),
        (4*Fi-3*Mi-6*z0,3*m-2*r-8*z+10*G+2*P1),
        (ki+P1+2*Fi,m),
    ])
    for x,y in identities:x.same(y)
    # Support-loss ledgers are exact sums, rather than a residual epsilon.
    assert 1+1+2+2+2+1+1+2==12
    assert F(9,2)+18+F(11,2)+2*6==40
    assert F(9,2)+12+4+1+1+F(7,2)==26
    assert 3+2+2*3==11
    assert 6+3==9 and 3*6+4==22
    return {'affine_identities':len(identities),'support_loss_ledgers':6}


def mulroot(x,y):return None if x is None or y is None else (x+y)%6
def powroot(x,n):return None if x is None else (x*n)%6

def local_checks():
    n=0
    # Each local pair table has common exponent0 or4 on both Cauchy sides.
    for parity,a1,a2 in product(range(2),repeat=3):
        tp=(a1-a2+3*parity)%6;active=int(tp!=0)
        e1=(4*a1+active*(1+tp)+parity*(a1+a2))%6
        e2=(4*a2+active*(1-tp)+parity*(a1+a2))%6
        expected=4 if parity or (a1 and a2) else 0
        assert e1==e2==expected;n+=1
        # Exact valuation identities underlying J, q0, the row cap, and fibre.
        for total in range(1,13):
            if total%2!=parity:continue
            j2=int(not parity and a1==a2==1)
            q0=total//2-j2
            assert q0>=0
            s=parity;J=s+j2;R=active;E=parity*(a1+a2)
            assert 2*q0+2*j2+s==total
            assert R-a1-a2+E==s-2*j2
            assert 4*F(total,2)-2*s+j2==4*q0+5*j2
            # B/R1 primes are in J2 or rad(q0), proving17.59.
            if not active:assert J or q0>0
            n+=1
    # Reflection14.17: each frozen-prime coefficient fits actual row/f/rho
    # valuation, including repeated row primes and all j4 assignments.
    for rowval,fbit,rhobit in product(range(13),range(2),range(2)):
        if rowval==fbit==rhobit==0:continue
        residual=rowval==1 and not fbit and not rhobit
        rhs=2*rowval-(rowval if rowval>=2 else 0)+fbit+rhobit
        jexp=(rowval+4*fbit)%6
        coefficients=([2] if residual else ([2] if jexp in (1,2,3,5) else [0,1] if jexp==0 else [1,1,-2]))
        for coef in coefficients:assert coef<=rhs;n+=1
    # No prime label is cancelled through a zero. None denotes a local zero.
    roots=[None]+list(range(6))
    for x,y in product(roots,repeat=2):
        assert powroot(mulroot(x,powroot(y,3)),3)==powroot(mulroot(x,y),3);n+=1
        lhs=powroot(mulroot(x,powroot(y,3)),-2)
        rhs=powroot(x,-2) if y is not None else None
        assert lhs==rhs;n+=1
    for x in roots:
        assert powroot(x,-1)==mulroot(x,powroot(x,4));n+=1
    # Whole-index marking and exact priority masks, including repeated factors.
    for h in range(1,6):
        for bits in product(range(2),repeat=h+1):
            rhs=sum(bits[j]*int(not any(bits[:j])) for j in range(h))+bits[h]*int(not any(bits[:h]))
            assert int(any(bits))==rhs;n+=1
    # A full moving coprimality mask is represented by its complete Moebius sum.
    for row,mark in product(range(16),repeat=2):
        inter=row&mark
        subs=[d for d in range(16) if d&inter==d]
        assert sum((-1)**d.bit_count() for d in subs)==int(inter==0);n+=1
    return n


def finite_ray_phase_checks():
    # Model mu3 times the stated square-class group: G=chi(4)*Gamma,
    # Gamma(-1)^e lambda^f = i^(f(1+2e)), and R is the source bicharacter.
    group=list(product(range(3),range(2),range(2)))
    def add(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%2,(a[2]+b[2])%2)
    def inv(a):return ((-a[0])%3,a[1],a[2])
    def G(a):return (4*a[0]+3*a[2]*(1+2*a[1]))%12
    def R(a,b):return 6*((a[1]*b[2]+a[2]*b[1]+a[2]*b[2])%2)
    n=0
    for a,b in product(group,repeat=2):
        assert G(add(a,b))==(G(a)+G(b)+R(a,b))%12;n+=1
        # Exact quotient phase in133; conjugation of G(a) is indispensable.
        assert (6*a[2]-G(a)+G(b)+R(a,b))%12==G(add(b,inv(a)));n+=1
        for w in group:
            assert G(add(add(w,b),inv(add(w,a))))==G(add(b,inv(a)));n+=1
    return n


def amplification_checks():
    n=0
    image={}
    for u,a in product(product(range(6),repeat=2),product(range(4),repeat=2)):
        value=tuple(u[i]+6*a[i] for i in range(2))
        assert value not in image
        image[value]=(u,a)
        assert tuple(v%6 for v in value)==u
        assert tuple(v//6 for v in value)==a;n+=1
    # Coefficients of17.90, with two independent finite prime supports.
    # n decomposes uniquely into d=n intersect rad(a), and m prime to a.
    for u,a,ncol in product(range(16),repeat=3):
        d=ncol&a;m=ncol^d
        assert not (m&a) and not (m&d)
        lhs=0 if u&ncol else (-1)**ncol.bit_count()
        rhs=0 if (u&d) or ((u|a)&m) else (-1)**(d.bit_count()+m.bit_count())
        assert lhs==rhs;n+=1
    # Fix c before r: the Lem17.1 short-scale strict width never shrinks at1.
    eps=F(1,1000);rmax=F(3,2);c=eps/(20*max(1,rmax))
    c1=c/(2*(1+c));c2=F(1,2)
    for r in (F(0),F(999,1000),F(1),F(1001,1000),rmax):
        base=max(F(1),r*(1+c));short_r=r/base
        assert 1-short_r>=2*c1
        assert 3-2*short_r>=c2
        actual=max(F(1),(1+5*r*(1+c))/6)
        ideal=max(F(1),(1+5*r)/6)
        assert actual-ideal<=5*rmax*c/6<eps/20;n+=1
    return n,{'epsilon':str(eps),'fixed_c':str(c),'first_strict_margin':str(c1),'second_strict_margin':str(c2)}


def terminal_checks():
    n=0
    eta=F(1,1000);tau=eta
    for H,O,v,l,S,B,za in product((F(0),F(1,4),F(1,2)),repeat=7):
      for e in (-eta,F(0),F(1,4)):
       for excess in (-tau,F(0),F(1,2)):
        Td=v+3*l+e+excess
        assert v+3*l+e<=Td+tau
        u=min(v,za,(v+za)/3)
        E=O/2+max(H,v+l)-S-B+za-u-l-2*e/3-max(F(0),Td-v-3*l-e)/2
        if H>=v+l:
            assert E<=O/2+H+za+2*eta/3;n+=1
        if H<=v+l:
            if u==za:
                assert E<=O/2+(Td-S-B)+5*eta/3+tau;n+=1
            else:
                assert u>=v/2
                assert E<=O/2+(Td-S-B)/2+za+7*eta/6+tau/2;n+=1
    return n


def loss_choice_checks():
    n=0
    for cs,Mmax,eps in product((F(1,100),F(1,20000)),(F(1),F(3)),(F(1,1000),F(1,10000))):
        d=cs/200
        depth=(Mmax+2)//d+2
        eta=min(d/16,cs/(14*depth),eps/(160*depth),cs/1000,F(1,100))
        tau=min(eps/(4*depth),cs/1000,F(1,100))
        pi=eps/(4*depth)
        assert cs-7*depth*eta>=cs/2
        assert Mmax-depth*d<0
        assert depth*(40*eta+tau+pi)<=3*eps/4<eps
        assert 2*d-8*eta>=F(3,2)*d
        n+=1
    return n


def main():
    amp,choices=amplification_checks()
    out={
      'status':'all exact scoped checks passed',
      'scope':'Finite/local algebra and affine identities only; no reflection theorem, large sieve, Poisson analytic tail, source family theorem, or complete inverse induction is independently validated.',
      'source_pdf_sha256':'8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7',
      'identities':affine_identities(),
      'local_zero_valuation_mask_assertions':local_checks(),
      'finite_ray_phase_assertions':finite_ray_phase_checks(),
      'amplification_assertions':amp,
      'uniform_length_one_example':choices,
      'terminal_branch_assertions':terminal_checks(),
      'finite_depth_loss_allocations':loss_choice_checks(),
      'pdf_notation_check':'Visual inspection of133/134 verified the conjugations suppressed by extracted text, including bar(chi_n(d2))=chi_n(d2)*chi_n(d2)^4 and chi_a(-1)*bar(G(a))*G(b)*R(a,b)=G(b*a^-1).'
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
