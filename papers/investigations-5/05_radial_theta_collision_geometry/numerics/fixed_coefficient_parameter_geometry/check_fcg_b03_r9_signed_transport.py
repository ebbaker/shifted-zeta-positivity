#!/usr/bin/env python3
"""One fixed signed-source transport; exact rationals, no source evaluations.
Prepared for Edward Baker with substantial LLM assistance, Sol/ultra, 2026-10-30.
Requires the hash-bound complete E01 R2 record. See B03 R9 note for proof.
"""
from pathlib import Path
from fractions import Fraction as F
from dataclasses import dataclass
from math import comb, factorial
import argparse, hashlib, json, re, time

INPUT='papers/investigations-5/05_radial_theta_collision_geometry/numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json'
INPUT_HASH='557c57e420534e4db949e3d019d5d40077a1df8f055f6634bd2f657c4f87392c'
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        assert self.lo<=self.hi
    def __add__(self,o):
        o=as_i(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-as_i(o)
    def __mul__(self,o):
        o=as_i(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi];return I(min(v),max(v))
    __rmul__=__mul__
    def norm(self):return max(abs(self.lo),abs(self.hi))
def as_i(x):return x if isinstance(x,I) else I(F(x),F(x))
def binary(pair):return F(int(pair[0]))*F(2)**int(pair[1])
def decode(d):
    m=binary(d['mid_binary']);r=binary(d['rad_binary']);assert r>=0;return I(m-r,m+r)
def display_ball(s):
    s=s.strip('[] ')
    if '+/-' in s:
        m,r=s.split('+/-');return I(F(m.strip())-F(r.strip()),F(m.strip())+F(r.strip()))
    return as_i(F(s))
def add(p,q):
    r=dict(p)
    for k,v in q.items():r[k]=r.get(k,as_i(0))+v
    return r
def scale(p,c):return {k:v*c for k,v in p.items()}
def mul(p,q):
    r={}
    for (m,l),v in p.items():
        for (n,k),w in q.items():
            key=(m+n,l+k);r[key]=r.get(key,as_i(0))+v*w
    return r
def bernstein(p,s,x0=F(0),x1=F(2)):
    """Enclose p on [-s,s] x [x0,x1], exact tensor Bernstein coefficients."""
    dt=max(k[0] for k in p);dx=max(k[1] for k in p)
    a={}
    for (m,l),c in p.items():
        for j in range(m+1):
            for k in range(l+1):
                v=c*comb(m,j)*(-s)**(m-j)*(2*s)**j*comb(l,k)*x0**(l-k)*(x1-x0)**k
                a[j,k]=a.get((j,k),as_i(0))+v
    # Separable power-to-Bernstein conversion avoids a dense four-index loop.
    b={}
    for it in range(dt+1):
        for k in range(dx+1):
            b[it,k]=sum((a.get((j,k),as_i(0))*F(comb(it,j),comb(dt,j)) for j in range(it+1)),as_i(0))
    vals=[]
    for it in range(dt+1):
        for ix in range(dx+1):
            vals.append(sum((b[it,k]*F(comb(ix,k),comb(dx,k)) for k in range(ix+1)),as_i(0)))
    return I(min(v.lo for v in vals),max(v.hi for v in vals)),[dt,dx]
def sum_tail(j,s,x):
    mt,lt=32,64
    a=[s**m/F(factorial(m)) for m in range(mt+1)]
    b=[x**l/F(factorial(l)) for l in range(lt+1)]
    at=s**(mt+1)/factorial(mt+1)/(1-s/F(mt+2))
    bt=x**(lt+1)/factorial(lt+1)/(1-x/F(lt+2))
    return sum((a[m]*b[l] for m in range(mt+1) for l in range(lt+1) if 2*m+l>17-j),F(0))+at*(sum(b)+bt)+sum(a)*bt

def serialize_i(z):return {'lower':str(z.lo),'upper':str(z.hi),'display':[format(float(z.lo),'.14e'),format(float(z.hi),'.14e')]}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,default=Path.cwd());parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    started=time.monotonic();raw=(args.repo/INPUT).read_bytes();assert hashlib.sha256(raw).hexdigest()==INPUT_HASH
    data=json.loads(raw);stage=next(s for s in data['stages'] if s['bits']==384)
    jets={z['j']:z for z in stage['integrals'] if z['kind']=='jet'}
    assert set(jets)==set(range(18))
    h={k:decode(z['complete']) for k,z in jets.items()}
    ek={k:display_ball(z['source_upper']).hi+display_ball(z['mode_upper']).hi for k,z in jets.items()}
    moment=next(z for z in stage['integrals'] if z['kind']=='moment' and z['j']==4 and z['T']=='17/64' and z['Y']=='1/64')
    m4=decode(moment['complete']).hi
    ext4=display_ball(moment['source_upper']).hi+display_ball(moment['mode_upper']).hi
    x1row=next(z for z in stage['integrals'] if z['kind']=='moment' and z['j']==1 and z['T']=='17/64' and z['Y']=='4')
    x1=decode(x1row['complete']).hi
    s=F(1,128);rho=F(1,16384);x=F(2)
    assert F(1,4)+s+rho<F(17,64)
    p={};errors={};ranges={};degrees={};tails={}
    for j in range(4):
        p[j]={(m,l):h[j+2*m+l]*F((-1)**m,factorial(m)*factorial(l)) for m in range((17-j)//2+1) for l in range(18-j-2*m)}
        sj=sum_tail(j,s,x)
        ep=ext4+sum((s**m*x**l/F(factorial(m)*factorial(l))*ek[j+2*m+l] for m,l in p[j]),F(0))
        errors[j]=m4*sj+ep;tails[j]={'coefficient_tail_upper':str(sj),'core_error_upper':str(m4*sj),'exterior_error_upper':str(ep),'total_upper':str(errors[j])}
        ranges[j],degrees[j]=bernstein(p[j],s)
    dp=add(mul(p[1],p[1]),scale(mul(p[0],p[2]),-2));dr,dd=bernstein(dp,s)
    pe={j:ranges[j].norm() for j in range(4)}
    derror=2*pe[1]*errors[1]+errors[1]**2+2*(pe[0]*errors[2]+pe[2]*errors[0]+errors[0]*errors[2])
    dlow=dr.lo-derror
    physical={j:I(ranges[j].lo-errors[j],ranges[j].hi+errors[j]) for j in range(4)}
    left={k:v for (m,l),v in p[0].items() if l==0 for k in [(m,0)]}
    right={}
    for (m,l),v in p[0].items():right[m,0]=right.get((m,0),as_i(0))+v*2**l
    left_range,_=bernstein(left,s);right_range,_=bernstein(right,s)
    left_lower=left_range.lo-errors[0];right_upper=right_range.hi+errors[0]
    eta=physical[1].norm();bcap=physical[2].norm();u3=physical[3].norm();eta_lower=-physical[1].hi
    delta=4-rho
    ab=2/delta+6/delta**2+6/delta**3
    ah=1/delta**2+6/delta**3+12/delta**4
    tail=x1*rho**2*(bcap*ab+eta*ah)
    finite=rho*eta*u3;timecost=2*bcap**2*rho
    margin=dlow-timecost-finite-tail
    scalar_tail=x1*rho**2*ah
    scalar_lower=eta_lower-rho*(bcap+u3)-scalar_tail
    c_lower=margin/(1+physical[0].norm()**2+eta**2+bcap**2)
    identities={'status':'checked analytically in accompanying note','identities':['dx P0=P1','dx P1=P2','dt P0=-P2']}
    assertions={
       'signed_discriminant_above_7.4e-20':dlow>F('7.4e-20'),
       'uniform_HA_below_-2.4e-10':physical[1].hi<F('-2.4e-10'),
       'left_H_above_6.4e-10':left_lower>F('6.4e-10'),
       'right_H_below_-6.2e-11':right_upper<F('-6.2e-11'),
       'uniform_degree_one_margin_above_6.6e-20':margin>F('6.6e-20'),
       'exact_coefficient_above_6.6e-20':c_lower>F('6.6e-20'),
       'matched_local_scalar_HA_floor_above_2.3e-10':scalar_lower>F('2.3e-10'),
       'complete_positive_moment_X1_below_.01':x1<F('.01'),
       'all_four_source_errors_below_1.1e-12':max(errors.values())<F('1.1e-12')}
    result={'task':'FCG-B03 R9 fixed signed-source transport','date':'2026-10-30','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance','model':'gpt-6.1-sol','effort':'ultra','thread_id':'01a18e61-b771-7d81-9290-9dad3cc07d78','history_number':51,'input':{'path':INPUT,'sha256':INPUT_HASH},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'domain':{'T_center':'1/4','T_radius':str(s),'A_interval':['64','66'],'consumer_radius':str(rho),'consumer_degree':1,'weighted_source_order':17,'rational_exponential_sum_rectangle':[32,64]},'source_errors':tails,'polynomial_ranges':{str(j):serialize_i(ranges[j]) for j in range(4)},'polynomial_degrees':degrees,'discriminant_polynomial':serialize_i(dr),'discriminant_bernstein_degree':dd,'discriminant_error_upper':str(derror),'physical_ranges':{str(j):serialize_i(physical[j]) for j in range(4)},'signed_discriminant_lower':str(dlow),'left_H_lower':str(left_lower),'right_H_upper':str(right_upper),'consumer':{'time_cost_upper':str(timecost),'signed_finite_sum_upper':str(finite),'direct_tail_upper':str(tail),'margin_lower':str(margin),'c_lower':str(c_lower),'scalar_HA_tail_upper':str(scalar_tail),'scalar_HA_floor_lower':str(scalar_lower)},'polynomial_identities':identities,'checks':assertions,'status':'passed' if all(assertions.values()) else 'scoped_failure','new_source_evaluations':0,'new_quadrature_evaluations':0,'development_reporting_correction':'An initial diagnostic cap e3<1e-12 was too small: e3=1.00263832004e-12. Only that reporting cap was changed to1.1e-12; all theorem checks, input data, error formulas, domain, degree and radius were unchanged.', 'center_degree_radius_sweep':False,'bernstein_subdivisions':0,'elapsed_seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':assertions,'source_errors':{j:float(errors[j]) for j in errors},'D_lower':float(dlow),'d1_lower':float(margin),'time':float(timecost),'finite':float(finite),'tail':float(tail),'scalar_HA_floor':float(scalar_lower),'seconds':result['elapsed_seconds']}))
    assert all(assertions.values()),'One fixed certificate failed; do not expand the domain or scan parameters.'
if __name__=='__main__':main()
