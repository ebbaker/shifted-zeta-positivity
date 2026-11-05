#!/usr/bin/env python3
"""MC11-E02 r1: fixed common-path spectral split, no quadrature.

Prepared for Edward Baker, 2026-11-04, with substantial LLM assistance.
Actual model gpt-6.1-sol, effort ultra. One calculation and one regrouping.
"""
import argparse
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform
import time

PARENT=Path('papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature')
MC11=PARENT/'11_energy_filtered_theta_overlaps'
RGD=PARENT/'10_radial_green_determinants'


def add(*polys):
    out={}
    for p in polys:
        for e,a in p.items():out[e]=out.get(e,F(0))+a
    return {e:a for e,a in out.items() if a}


def scale(p,a):return {e:a*v for e,v in p.items() if a*v}


def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            key=tuple(x+y for x,y in zip(e,f));out[key]=out.get(key,F(0))+a*b
    return {e:a for e,a in out.items() if a}


def var(j,n):
    e=[0]*n;e[j]=1;return {tuple(e):F(1)}


def derivative(p,j):
    out={}
    for e,a in p.items():
        if e[j]:
            f=list(e);f[j]-=1;out[tuple(f)]=a*e[j]
    return out


def substitute(p,variables):
    n=len(next(iter(variables[0])))
    out={}
    for e,a in p.items():
        term={(0,)*n:a}
        for v,power in zip(variables,e):
            for _ in range(power):term=mul(term,v)
        out=add(out,term)
    return out


def iv_add(a,b):return a[0]+b[0],a[1]+b[1]


def iv_mul(a,b):
    ends=[x*y for x in a for y in b];return min(ends),max(ends)


def interval_value(p,box):
    out=(F(0),F(0))
    for e,a in p.items():
        term=(a,a)
        for iv,power in zip(box,e):
            for _ in range(power):term=iv_mul(term,iv)
        out=iv_add(out,term)
    return out


def dyadic(pair):return F(int(pair[0]))*F(2)**int(pair[1])


def ball(row):
    m,r=dyadic(row['mid']),dyadic(row['rad'])
    assert r>=0
    return m-r,m+r


def floor_grid(x,bits):
    x=x*2**bits;return F(x.numerator//x.denominator,2**bits)


def ceil_grid(x,bits):return -floor_grid(-x,bits)


def exp_minus_interval(x):
    """Exact Taylor enclosure at both endpoints, then outward 192-bit grid.

    exp(y) lies between S_128(y) and S_128(y)+next/(1-y/130).
    No library transcendental evaluation or integral is used.
    """
    assert 0<x[0]<=x[1]<130
    def bounds(y):
        term=F(1);total=term
        for k in range(1,129):term=term*y/k;total+=term
        next_term=term*y/129
        return total,total+next_term/(1-y/130)
    left,right=bounds(x[0]),bounds(x[1])
    return floor_grid(1/right[1],192),ceil_grid(1/left[0],192)


def out_interval(iv):
    def reading(x,direction):
        with localcontext() as ctx:
            ctx.prec=14;ctx.rounding=direction
            return format(Decimal(x.numerator)/Decimal(x.denominator),'.12E')
    return {'lower':str(iv[0]),'upper':str(iv[1]),
            'lower_reading':reading(iv[0],ROUND_FLOOR),'upper_reading':reading(iv[1],ROUND_CEILING)}


def terms(p):return [{'powers':list(e),'coefficient':str(a)} for e,a in sorted(p.items())]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite existing result')
    start=time.perf_counter();checks=[];inputs={}
    def check(name,condition):
        checks.append({'check':name,'passed':bool(condition)})
        if not condition:raise AssertionError(name)
    def read(path,expected=None):
        data=(args.repo/path).read_bytes();h=hashlib.sha256(data).hexdigest()
        if expected:check('frozen hash '+str(path),h==expected)
        inputs[str(path)]=h;return json.loads(data)
    e01=read(MC11/'numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json')
    for path,h in e01['input_sha256'].items():
        actual=hashlib.sha256((args.repo/path).read_bytes()).hexdigest()
        check('E01 frozen input '+path,actual==h);inputs[path]=actual
    old=read(RGD/'numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json')
    acquisition=read(RGD/'numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json',
                     old['input_sha256']['numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json'])
    for rel in ['reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md',
                'research-progress/handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md']:
        path=MC11/rel;inputs[str(path)]=hashlib.sha256((args.repo/path).read_bytes()).hexdigest()
    check('accepted acquisition single complete pass',len(acquisition['passes'])==1 and acquisition['passes'][0]['complete'])
    pi_saved=ball(acquisition['passes'][0]['constants']['pi'])
    pi=(floor_grid(pi_saved[0],128),ceil_grid(pi_saved[1],128))
    check('pi coarse sanity',3<pi[0]<pi[1]<F(22,7))
    exp4=exp_minus_interval((4*pi[0],4*pi[1]))
    exp7=exp_minus_interval((7*pi[0],7*pi[1]))
    exp9=exp_minus_interval((9*pi[0],9*pi[1]))
    check('positive exponential boxes',all(0<v[0]<=v[1]<1 for v in [exp4,exp7,exp9]))
    lam2=16*pi[0]-1;lam3=36*pi[0]-1
    def slope(E):return 4*E-9-F(12)/(2*E-3)
    kap2=slope(4*pi[0]);kap3=slope(9*pi[0])
    check('excited slope lower bounds',kap2>40 and kap3>100)
    # Complete infinite group majorants, source moment <= previous primitive moment.
    U=[exp4[1]/(8*lam2**(2*j-1)) for j in range(1,6)]
    V=[exp9[1]/(8*(1-exp7[1])*lam3**(2*j-1)) for j in range(1,6)]
    H=[(F(0),u+v) for u,v in zip(U,V)]
    C=[(F(row['lower']),F(row['upper'])) for row in old['reference_boxes']]
    B=[]
    for row in old['tail_allowances']:
        iv=ball({'mid':row['B_mid'],'rad':row['B_rad']})
        check('nonzero spatial tail '+str(row['j']),iv[0]>0)
        B.append(ceil_grid(iv[1],384))
    b=[(C[j][0]-B[j],C[j][1]+B[j-1]) for j in range(1,6)]
    check('positive full-half-line ground boxes',all(v[0]>0 for v in b))
    cpath=[(bi[0],bi[1]+hi[1]) for bi,hi in zip(b,H)]

    cv=[var(j,5) for j in range(5)];D={}
    for perm in itertools.permutations(range(3)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        term={(0,)*5:F(sign)}
        for i,j in enumerate(perm):term=mul(term,cv[3+j-i-1])
        D=add(D,term)
    display=add(mul(mul(cv[2],cv[2]),cv[2]),scale(mul(mul(cv[1],cv[2]),cv[3]),-2),
                mul(cv[0],mul(cv[3],cv[3])),mul(mul(cv[1],cv[1]),cv[4]),
                scale(mul(mul(cv[0],cv[2]),cv[4]),-1))
    check('collected D3 equals permutation determinant',D==display)
    G=[derivative(D,j) for j in range(5)]
    bv=[var(j,10) for j in range(5)];hv=[var(j+5,10) for j in range(5)]
    along=[add(x,y) for x,y in zip(bv,hv)]
    K=[]
    for j,g in enumerate(G):
        path=substitute(g,along)
        check('quadratic or lower path degree '+str(j+1),all(sum(e[5:])<=2 for e in path))
        K.append({e:a/F(sum(e[5:])+1) for e,a in path.items()})
    response=add(*(mul(h,k) for h,k in zip(hv,K)))
    endpoint=add(substitute(D,along),scale(substitute(D,bv),-1))
    check('exact sum h_j K_j equals cubic endpoint difference',response==endpoint)
    # A sign error in the collected exchange term must fail the same identity.
    wrong=add(response,scale(mul(hv[1],K[1]),-2))
    check('flipped exchange sign breaks endpoint identity',wrong!=endpoint)
    ki=[interval_value(k,b+H) for k in K]
    gi=[interval_value(g,cpath) for g in G]
    signs=[1,-1,1,-1,1]
    check('integrated coefficient signs + - + - +',all(x[0]>0 if s>0 else x[1]<0 for s,x in zip(signs,ki)))
    check('whole-path coefficient signs + - + - +',all(x[0]>0 if s>0 else x[1]<0 for s,x in zip(signs,gi)))
    d0=interval_value(D,b)
    check('positive D3(0) full-half-line lower bound',d0[0]>0)

    def independent(bounds):
        return (sum(min(F(0),x[0])*u for x,u in zip(ki,bounds)),
                sum(max(F(0),x[1])*u for x,u in zip(ki,bounds)))
    direct2=independent(U);direct3=independent(V)
    # The single permitted regrouping uses the common lowest moment and slope ratios.
    # Exact expression: L=A1 sum K_j r_j, r1=1, 0<rj<=kappa^(-2j+2).
    def regroup(weights,kappa):
        lo=weights[0][0];hi=weights[0][1]
        for j,iv in enumerate(weights[1:],1):
            r=kappa**(-2*j)
            lo+=min(F(0),iv[0])*r;hi+=max(F(0),iv[1])*r
        return lo,hi
    norm2=regroup(ki,kap2);norm3=regroup(ki,kap3)
    point3=regroup(gi,kap3)
    check('higher group integrated response strictly positive',norm3[0]>0)
    check('every level n>=3 positive over full path',point3[0]>0)
    split2=(min(F(0),norm2[0])*U[0],max(F(0),norm2[1])*U[0])
    split3=(F(0),norm3[1]*V[0])
    total=iv_add(split2,split3)
    # Also retain valid independent bounds: intersect them without a second regrouping.
    split2=(max(split2[0],direct2[0]),min(split2[1],direct2[1]))
    split3=(F(0),min(split3[1],direct3[1]))
    total=iv_add(split2,split3)
    fractional=(total[0]/d0[0],total[1]/d0[0])

    # Fixed E03 gate: target absolute half-widths, no acquisition or feasibility integration.
    radii=[u/F(10**6) for u in U]
    moment_radius=sum(max(abs(x[0]),abs(x[1]))*r for x,r in zip(ki,radii))
    mids=[(x[0]+x[1])/2 for x in ki]
    krads=[(x[1]-x[0])/2 for x in ki]
    cofactor_radius=sum(u*r for u,r in zip(U,krads))
    gate_radius=moment_radius+cofactor_radius+split3[1]
    # Two uncertainty-set witnesses: not asserted to be realizable source moments.
    pos=[U[0]/2*(1/(100*kap2**2))**j for j in range(5)]
    neg=[U[0]/2]
    neg.append(neg[0]*F(99,100)/kap2**2)
    for _ in range(3):neg.append(neg[-1]/(100*kap2**2))
    witness=[]
    for name,values,expected in [('positive',pos,1),('negative',neg,-1)]:
        check(name+' witness in retained positive boxes',all(0<a<u for a,u in zip(values,U)))
        check(name+' witness respects slope recursion',all(values[j+1]<=values[j]/kap2**2 for j in range(4)))
        box=[(max(F(0),v-r),min(u,v+r)) for v,r,u in zip(values,radii,U)]
        val=(sum(min(a*x for a in ai for x in k) for ai,k in zip(box,ki)),
             sum(max(a*x for a in ai for x in k) for ai,k in zip(box,ki)))
        net=(val[0],val[1]+split3[1])
        check(name+' narrow n2 witness decides net sign',net[0]>0 if expected>0 else net[1]<0)
        witness.append({'name':name,'center':[str(v) for v in values],
                        'net_interval':out_interval(net),
                        'scope':'Retained bound-set witness only, not actual or realizable source moments'})
    out={
        'task':'MC11-E02','request_revision':'r1','date':'2026-11-04','timezone':'America/New_York',
        'prepared_for':'Edward Baker','llm_assistance':True,'actual_model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'thread_id':'01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab','turn_id':'01a1a8f3-323b-7ca1-aa36-acb844ed67ff',
        'input_sha256':inputs,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'arithmetic':'Fraction only; outward constant grids; Decimal display only',
        'limits_used':{'calculations':1,'regroupings':1,'integrand_evaluations':0,'new_moments':0},
        'constants':{'pi':out_interval(pi),'exp_minus_4pi':out_interval(exp4),
                     'exp_minus_7pi':out_interval(exp7),'exp_minus_9pi':out_interval(exp9),
                     'primitive_slopes_lower':[str(lam2),str(lam3)],'source_slopes_lower':[str(kap2),str(kap3)],
                     'exp_method':'128-term positive Taylor sum, geometric remainder, inversion, 192-bit outward grid'},
        'D3_polynomial':terms(D),'G_polynomials':[terms(g) for g in G],
        'K_polynomials_in_b1_to_b5_h1_to_h5':[terms(k) for k in K],
        'ground_coefficient_boxes':[out_interval(x) for x in b],
        'moment_upper_n2':[str(x) for x in U],'moment_upper_n_ge3':[str(x) for x in V],
        'integrated_K_boxes':[out_interval(x) for x in ki],
        'whole_path_G_boxes':[out_interval(x) for x in gi],
        'independent_split_bounds':{'L2':out_interval(direct2),'Lge3':out_interval(direct3)},
        'regrouped_normalized_responses':{'L2_over_a1':out_interval(norm2),
                                         'Lge3_over_H1':out_interval(norm3),
                                         'pointwise_n_ge3_over_a1':out_interval(point3)},
        'final_bounds':{'L2':out_interval(split2),'Lge3':out_interval(split3),
                        'Delta3':out_interval(total),'D3_ground':out_interval(d0),
                        'Delta3_over_D3_ground':out_interval(fractional)},
        'strict_signs':{'L2':'undetermined','Lge3':'strictly positive; zero lower endpoint is open',
                        'Delta3':'undetermined','D3_ground':'strictly positive',
                        'each_n_ge3_every_s':'strictly positive'},
        'E03_gate':{'needed_half_widths':[str(x) for x in radii],
                    'moment_sensitivity_radius':str(moment_radius),'cofactor_uncertainty_radius':str(cofactor_radius),
                    'sufficient_absolute_midpoint_margin_for_net_sign':str(gate_radius),
                    'uncertainty_set_witnesses':witness,
                    'interpretation':'N2 moment widths alone prevent the retained bounds deciding net sign; no actual sign forecast'},
        'checks':checks,'status':'complete bounded E02 return; n2 and net intervals inconclusive; E03 gate demonstrated',
        'execution_seconds':time.perf_counter()-start,
    }
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':out['status'],'checks':len(checks),'seconds':out['execution_seconds'],
                      'bounds':{k:{z:v for z,v in x.items() if 'reading' in z} for k,x in out['final_bounds'].items()},
                      'norm2':{k:v for k,v in out_interval(norm2).items() if 'reading' in k},
                      'E03_moment_radii':[out_interval((x,x))['upper_reading'] for x in radii],
                      'E03_midpoint_margin':out_interval((gate_radius,gate_radius))['upper_reading']}))


if __name__=='__main__':main()
