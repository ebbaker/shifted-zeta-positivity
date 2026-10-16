"""Exact arithmetic examples and constants for the amplitude-profile lemma.
Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured effort are not exposed.
The imported analytic moment estimates are NOT verified by this script.
"""
from fractions import Fraction as F
import json

alpha=F(5,6)
eta=F(1,10000)
H0=F(1,5000)
dlo,dhi=F(9,25),F(21,50)
ratio=(alpha-dhi)/(alpha-dhi/3)
assert ratio==F(31,52)
assert ratio*H0-eta==F(1,52000)
assert 4*dlo*F(14,37)>alpha-dlo
assert H0/(alpha-dhi/3)<F(1,10)
# The upper cutoff bound uses b_delta <= (2/5)delta.
assert F(2,5)*dhi/(2*(alpha-dhi+F(2,5)*dhi))<F(3,20)
assert -36+96*F(49,100)-40*F(49,100)**2==F(359,250)>0
# The second strict inverse width margin after taking z=(1-r)/2.
assert 2*F(3,5)-1==F(1,5)
# Candidate geometry supplies the stronger refined capacity threshold.
ell=F(1,6)+F(1,5000)
h=(1+3*ell+F(1,8))/2
assert ell/(h+F(1,1600000))>F(1,5)

class Profile:
    def __init__(self, parts):
        self.parts=sorted(parts, key=lambda wg:wg[1], reverse=True)
        self.length=sum((w for w,g in self.parts),F(0))
        self.q=sum((w*g for w,g in self.parts),F(0))/self.length
        self.knots=[]
        z=F(0)
        for w,g in self.parts:
            z+=w
            self.knots.append(z)
    def G(self,z):
        assert z>=0
        val=F(0)
        for w,g in self.parts:
            used=min(w,z)
            val+=used*g
            z-=used
        return val
    def K(self,z):
        assert 0<=z<=self.length
        return self.G(z)-self.q*z

def parameters(delta,profile):
    x=profile.q/delta
    D=3-F(17,9)*x
    P=(2-F(8,9)*x)*(1-x)
    bdelta=delta*P/D
    t0=1+bdelta/(2*(alpha-delta+bdelta))
    return x,D,P,bdelta,t0

def short(delta,profile,t):
    A=lambda r:1-delta*r-2*profile.G((1-r)/2)
    S=lambda r:1-2*delta*(t-r)-2*profile.G(F(2,9)*(1-2*(t-r)))
    lo,hi=t-F(1,2),F(1)
    knots=sorted(set([lo,hi]+[r for z in profile.knots for r in [1-2*z,t-F(1,2)+F(9,4)*z] if lo<r<hi]))
    for left,right in zip(knots,knots[1:]):
        fl,fr=A(left)-S(left),A(right)-S(right)
        if fl>=0>=fr:
            r=left if fl==0 else left+(right-left)*fl/(fl-fr)
            assert A(r)==S(r)
            assert (4*t-1)/5<=r<=(14*t+2)/23
            return r,A(r)
    raise AssertionError('no crossing')

def record(delta,profile):
    x,D,P,bd,t0=parameters(delta,profile)
    r0=((2-F(8,9)*x)*t0-F(5,9)*x)/D
    R=1-delta+bd*(F(3,2)-t0)
    rg,fg=short(delta,profile,t0)
    H=R-fg
    km=profile.K((1-r0)/2)
    kp=profile.K(F(2,9)*(1-2*(t0-r0)))
    certified=F(28,23)*km+F(2,5)*kp
    assert H>=certified>=0
    if km>=kp: assert H>=(28*km+18*kp)/23
    else: assert H>=(8*km+2*kp)/5
    lower=min(H,H0)
    tau=min(t0-1,lower/(alpha-delta/3))
    _,new_short=short(delta,profile,t0-tau)
    new_long=1-delta+(alpha-delta)*(t0-tau-1)
    gain=R-max(new_short,new_long)
    assert gain>=(alpha-delta)*tau
    if H>=H0: assert gain>=ratio*H0>eta
    return {k:{'exact':str(v),'decimal':float(v)} for k,v in dict(q=profile.q,x=x,t0=t0,r0=r0,refined_r=rg,short_gain=H,profile_lower_bound=certified,retuned_count_gain=gain).items()}

length=F(5,24)
delta=F(2,5)
examples={
    'two_level_nearly_saturated':record(delta,Profile([(F(3,5)*length,F(1,5)),(F(2,5)*length,F(19,100))])),
    'fully_saturated_no_gain':record(delta,Profile([(length,F(1,5))])),
}
assert examples['fully_saturated_no_gain']['short_gain']['exact']=='0'
print(json.dumps({
    'status':'Exact arithmetic checks of the derived profile formulas; analytic source lemmas remain conditional.',
    'uniform_retuning_ratio':str(ratio),
    'profile_gain_threshold':str(H0),
    'certified_gain_at_threshold':str(ratio*H0),
    'spare_count_exponent_above_required_gain':str(ratio*H0-eta),
    'examples':examples,
},indent=2,sort_keys=True))
