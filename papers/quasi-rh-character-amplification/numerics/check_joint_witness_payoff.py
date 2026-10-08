"""Independent exact audit of the CONDITIONAL joint-witness payoff.
Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
The new mixed arithmetic estimate is assumed, not proved or verified here.
"""
from fractions import Fraction as F
import json

def con(q): return {(0,0):F(q)} if q else {}
def add(*ps):
    result={}
    for p in ps:
        for powers,value in p.items(): result[powers]=result.get(powers,F(0))+value
    return {k:v for k,v in result.items() if v}
def scale(c,p): return {k:F(c)*v for k,v in p.items() if c*v}
def mul(*ps):
    result=con(1)
    for p in ps:
        new={}
        for (i,j),v in result.items():
            for (k,l),w in p.items(): new[i+k,j+l]=new.get((i+k,j+l),F(0))+v*w
        result={k:v for k,v in new.items() if v}
    return result

def diff(p,axis):
    out={}
    for powers,v in p.items():
        if powers[axis]:
            new=list(powers);new[axis]-=1
            out[tuple(new)]=v*powers[axis]
    return out

alpha=F(5,6)
delta,x={(1,0):F(1)},{(0,1):F(1)}
a=add(con(alpha),scale(-1,delta))
B=add(con(2),scale(-F(8,9),x))
D=add(con(3),scale(-F(17,9),x))
one_minus_x=add(con(1),scale(-1,x))
P=mul(B,one_minus_x)
J=add(mul(a,D),mul(delta,P))
num=mul(a,B)
# Exact derivative numerator identities for F=aB/J.
num_delta=add(mul(diff(num,0),J),scale(-1,mul(num,diff(J,0))))
num_x=add(mul(diff(num,1),J),scale(-1,mul(num,diff(J,1))))
assert num_delta==scale(-alpha,mul(B,B,one_minus_x))
assert num_x==mul(a,add(scale(F(10,9),a),mul(delta,B,B)))
# c=B/D increases, r_star(1)=(B-5x/9)/D decreases.
assert add(mul(diff(B,1),D),scale(-1,mul(B,diff(D,1))))==con(F(10,9))
r1num=add(B,scale(-F(5,9),x))
assert add(mul(diff(r1num,1),D),scale(-1,mul(r1num,diff(D,1))))==con(-F(5,9))

lo,hi=F(9,25),F(21,50)
xl,xh=F(49,100),F(1,2)
eta_mix,eta_final=F(1,5000),F(1,10000)
bb=lambda v:2-F(8,9)*v
dd=lambda v:3-F(17,9)*v
pp=lambda v:bb(v)*(1-v)
jj=lambda d,v:(alpha-d)*dd(v)+d*pp(v)
factor=lambda d,v:(alpha-d)*bb(v)/jj(d,v)
Fmin=factor(hi,xl)
assert Fmin==F(1091200,2012413)
assert Fmin>F(5422346208,10**10)
full_gain=Fmin*eta_mix
assert full_gain==F(1091200,10062065000)
assert full_gain>F(108446924,10**12)
spare=full_gain-eta_final
assert spare==F(169987,20124130000)>F(844,10**8)
assert spare>F(1,250000)

# B,D,P are positive and decreasing on the box (P'=-(26-16x)/9<0).
assert all(bb(v)>0 and dd(v)>0 and pp(v)>0 for v in [xl,xh])
assert bb(xl)>bb(xh) and dd(xl)>dd(xh) and pp(xl)>pp(xh)
Jlow=(alpha-hi)*dd(xh)+lo*pp(xh)
Jhigh=(alpha-lo)*dd(xl)+hi*pp(xl)
tlow=1+lo*pp(xh)/(2*Jhigh)-bb(xl)*eta_mix/Jlow
thigh=1+hi*pp(xl)/(2*Jlow)
assert tlow>F(553,500) # 1.106
assert thigh<F(1149,1000)
assert 1<tlow<thigh<F(3,2)
cc=lambda v:bb(v)/dd(v)
r1=lambda v:(bb(v)-F(5,9)*v)/dd(v)
rlow=cc(xl)*(tlow-1)+r1(xh)-eta_mix/(lo*dd(xh))
rhigh=cc(xh)*(thigh-1)+r1(xl) # drop the negative crossing shift
assert rlow>F(7013099,10**7)>F(701,1000)
assert rhigh<F(7351703,10**7)<F(92,125) # .736
mmin=tlow-F(37,50)
assert mmin>F(183,500)>F(9,25)
# Thus the inverse profile cutoff argument is O(U^-mmin), uniformly.
plain_outside_slack=lo*bb(xh)*(F(701,1000)-F(7,10))
inverse_outside_slack=lo*(1-xh)*(F(37,50)-F(92,125))-eta_mix
assert plain_outside_slack==F(7,12500)>F(1,2000)
assert inverse_outside_slack==F(13,25000)>F(1,2000)

# Independently check crossing/rebalance and mixed spike normalization at
# rational tensor nodes. The proofs are the displayed affine identities.
for d in [lo,F(2,5),hi]:
    for v in [xl,F(99,200),xh]:
        a0=alpha-d; B0=bb(v);D0=dd(v);P0=pp(v);J0=jj(d,v)
        t0=1+d*P0/(2*J0)
        tnew=t0-B0*eta_mix/J0
        rstar=lambda t:(B0*t-F(5,9)*v)/D0
        rn=rstar(tnew)-eta_mix/(d*D0)
        AI=lambda r:1-d*(v+(1-v)*r)
        ST=lambda r:1-d*(F(4,9)*v+B0*(tnew-r))
        long=lambda t:1-d+a0*(t-1)
        Rold=long(t0)
        assert AI(rn)-eta_mix==ST(rn)==long(tnew)
        assert Rold-long(tnew)==factor(d,v)*eta_mix>=full_gain
        assert tlow<=tnew<=thigh and rlow<=rn<=rhigh
        for rr in [F(7,10),rn,F(37,50)]:
            for mm in [F(9,25),F(2,5),F(1,2)]:
                z=(1-rr)/2
                mixed_bound=1+d*mm-eta_mix
                spike=d*(rr+mm)+2*d*v*z
                assert mixed_bound-spike==AI(rr)-eta_mix

entry=lambda v:{'exact':str(v),'decimal':float(v)}
print(json.dumps({
    'status':'Conditional payoff only: the required mixed arithmetic estimate remains UNPROVED.',
    'verified_symbolic_derivatives':['F_delta','F_x','(B/D)_x','r_star(1)_x'],
    'mixed_moment_gain':entry(eta_mix),
    'minimum_full_envelope_factor':entry(Fmin),
    'minimum_full_envelope_gain':entry(full_gain),
    'desired_final_row_gain':entry(eta_final),
    'spare_exponent_for_cumulative_losses':entry(spare),
    'safe_example_loss_budget':entry(F(1,250000)),
    'interval_bounds':{k:entry(v) for k,v in dict(Jlow=Jlow,Jhigh=Jhigh,tlow=tlow,thigh=thigh,rlow=rlow,rhigh=rhigh,mmin=mmin).items()},
    'outside_band_slack':{'plain_left':entry(plain_outside_slack),'inverse_right':entry(inverse_outside_slack)},
    'scope':'Derivative identities use exact sparse polynomial arithmetic; interval and slack bounds use rational arithmetic; tensor checks supplement the affine normalization proof.',
},indent=2,sort_keys=True))
