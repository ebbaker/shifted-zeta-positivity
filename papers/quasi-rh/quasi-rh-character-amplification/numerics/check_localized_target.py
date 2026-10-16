"""Exact localized exponent certificate, conditional on a NEW row-count input.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured effort are not exposed.
The proposed exceptional-row improvement is not proved by this script.
"""
from fractions import Fraction as F
from math import comb
import json

def const(c):
    return {(0,0): F(c)} if c else {}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(c,p):
    return {k:F(c)*v for k,v in p.items() if c*v}
def mul(*ps):
    out=const(1)
    for p in ps:
        new={}
        for (i,j),v in out.items():
            for (k,l),w in p.items():
                new[i+k,j+l]=new.get((i+k,j+l),F(0))+v*w
        out={k:v for k,v in new.items() if v}
    return out

delta,y={(1,0):F(1)},{(0,1):F(1)}
e,ell,b=F(1,5000),F(1,6)+F(1,5000),F(1,8)
lx,ly=(1-ell-b)/2,(1-ell+b)/2
h=(1+3*ell+b)/2
sigma=F(11,12)-ell/4
assert sigma==F(17499,20000)
eta,margin=F(1,10000),F(1,100000)
py=add(const(7),scale(18,y),scale(8,mul(y,y)))
jy=add(const(185),scale(170,y),
       mul(delta,add(const(-138),scale(12,y),scale(96,mul(y,y)))))
J=scale(F(1,108),jy)
Eplain=add(const(-F(1,4)+5*ell/4+b/6),
           scale(-1,mul(delta,add(const(b/2),scale(ell,y)))))
N=add(scale(-96,mul(jy,Eplain)),
      scale(-576*h,mul(add(const(F(5,6)),scale(-1,delta)),delta,py)))
# N=10368 J(-E). Certify E<=-margin outside the designated box.
ordinary=add(N,scale(-10368*margin,J))
# Inside the box this certificate assumes R is replaced by R-eta.
improved=add(N,scale(10368*(h*eta-margin),J))

def bernstein(p,box):
    a,b0,c,d0=box
    q={}
    for (i,j),v in p.items():
        for k in range(i+1):
            for l in range(j+1):
                q[k,l]=q.get((k,l),F(0))+v*comb(i,k)*a**(i-k)*(b0-a)**k*comb(j,l)*c**(j-l)*(d0-c)**l
    n=max(i for i,j in p); m=max(j for i,j in p)
    return [sum((v*F(comb(k,i),comb(n,i))*F(comb(l,j),comb(m,j))
                 for (i,j),v in q.items() if i<=k and j<=l),F(0))
            for k in range(n+1) for l in range(m+1)]

def certify(p,box,depth=0):
    bs=bernstein(p,box)
    if min(bs)>0:
        return [(box,min(bs),depth)]
    if depth>=16: raise AssertionError(('unresolved exact box',box,min(bs)))
    a,b0,c,d0=box
    # Alternate normalized coordinates; every split exactly partitions its box.
    if depth%2==0:
        mid=(a+b0)/2
        boxes=[(a,mid,c,d0),(mid,b0,c,d0)]
    else:
        mid=(c+d0)/2
        boxes=[(a,b0,c,mid),(a,b0,mid,d0)]
    return sum((certify(p,q,depth+1) for q in boxes),[])

boxes={
    'delta_below':(F(1,50),F(9,25),F(0),F(1,2)),
    'delta_above':(F(21,50),F(3,4),F(0),F(1,2)),
    'amplitude_below':(F(9,25),F(21,50),F(1,100),F(1,2)),
    'hard_box_with_NEW_count_input':(F(9,25),F(21,50),F(0),F(1,100)),
}
certificates={}
for name,box in boxes.items():
    leaves=certify(improved if name.startswith('hard') else ordinary,box)
    certificates[name]={
        'box':[str(v) for v in box],
        'leaves':len(leaves),
        'maximum_depth':max(z for _,_,z in leaves),
        'minimum_positive_Bernstein_coefficient':str(min(z for _,z,_ in leaves)),
    }

# Residual high ranges, low geometry, and a bounded frequency extension.
low=lx/2+b/12
assert sigma-F(11,16)==low
assert lx+ly+ell==1 and ell<F(1,5)
f=lambda d:-d+max(F(0),5*ell-1+d)/8
assert max(f(d) for d in [F(0),1-5*ell,ell])==0
assert ly-ell-F(11,6)*b>0
floor=F(7,1200)-F(32,25)*e
middle=F(241,9600)-F(329,400)*e
small=F(63,800)-F(51,100)*e
assert min(floor,middle,small,ly/20,h/600)>margin
zeta=margin/16
assert ell/(h+zeta)>F(1,5)>F(7,37)
assert 2*zeta<margin/4 and sigma>F(87,100)

# Profile retuning on the hard box; widths are row-base quantities.
alpha=F(5,6)
ratio=(alpha-F(21,50))/(alpha-F(21,50)/3)
assert ratio==F(31,52)
Hthreshold=F(1,5000)
profile_gain=ratio*Hthreshold
assert profile_gain>eta
# P/D>=14/37: in x coordinates, 9(37P-14D)
# equals (1/2-x)(576-296x), nonnegative on [0,1/2].
assert (F(1,2)*576,-576-F(1,2)*296,296)==(288,-724,296)
delta_min=F(9,25)
t_minus_one_min=delta_min*F(14,37)/(2*(alpha-delta_min+delta_min*F(14,37)))
assert t_minus_one_min>F(1,10)
assert Hthreshold/(alpha-F(21,50)/3)<F(1,10)

def entry(v): return {'exact':str(v),'decimal':float(v)}
print(json.dumps({
    'status':'Conditional implication only: a new restricted exceptional-row bound is REQUIRED and is not proved here.',
    'geometry':{k:entry(v) for k,v in dict(ell=ell,b=b,lx=lx,ly=ly,h=h,sigma=sigma,low=low).items()},
    'variance_exponent':entry(1+2*sigma),
    'required_row_gain':entry(eta),'uniform_high_margin_before_losses':entry(margin),
    'exact_Bernstein_certificates':certificates,
    'other_margins':{k:entry(v) for k,v in dict(floor=floor,middle=middle,small=small,principal_w=ly/20,principal_z=h/600,zeta=zeta).items()},
    'profile_retuning':{'short_count_gain_threshold':entry(Hthreshold),'minimum_ratio':entry(ratio),'implied_row_gain_before_losses':entry(profile_gain)},
    'method':'Exact rational tensor Bernstein coefficients after exact rectangular subdivision; no floating grid is used.',
},indent=2,sort_keys=True))
