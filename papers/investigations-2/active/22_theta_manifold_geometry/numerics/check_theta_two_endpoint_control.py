#!/usr/bin/env python3
"""Bounded two-endpoint weighted-square control search and certified checks.
15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra; reasoning effort ultra. Requires python-flint.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, platform, time
from pathlib import Path
import flint
from flint import arb, acb, ctx

def poly(k):
    p={2:2,1:-3}
    for _ in range(k):
        q={}
        for d,c in p.items():
            q[d]=q.get(d,0)+(1+4*d)*c
            q[d+1]=q.get(d+1,0)-4*c
        p={d:c for d,c in q.items() if c}
    return p
def peval(p,a): return sum((c*a**d for d,c in p.items()),arb(0))
def brec(x): return x.str(35,more=True)
def main():
    pa=argparse.ArgumentParser();pa.add_argument('--output',type=Path)
    pa.add_argument('--bits',type=int,default=160);pa.add_argument('--search',action='store_true')
    args=pa.parse_args();ctx.prec=args.bits;start=time.monotonic();checks=[]
    def check(label,p):
        if not p: raise AssertionError(label)
        checks.append(label)
    pi=arb.pi(); aa={n:pi*n*n for n in range(1,7)}
    d={n:peval(poly(1),a) for n,a in aa.items()}
    r={n:peval(poly(3),a)/d[n] for n,a in aa.items()}
    c={n:-d[1]/d[n] for n in range(2,7)}
    eta={n:(r[1]-r[2])/(r[n]-r[2]) for n in range(3,7)}
    # Exact integer-polynomial verification P3=(16a²-120a+49)P1+360a.
    rhs={}
    for i,ci in {2:16,1:-120,0:49}.items():
        for j,cj in poly(1).items():rhs[i+j]=rhs.get(i+j,0)+ci*cj
    rhs[1]=rhs.get(1,0)+360
    check('rational_ratio_identity_exact',rhs==poly(3))
    check('r1_exceeds_r2',r[1]>r[2]);check('r3_exceeds_r1',r[3]>r[1])
    check('first_P1_positive',d[1]>0)
    check('P1_negative_n2_through6',all(d[n]<0 for n in range(2,7)))
    check('ratio_derivative_positive_for_a_at_least_4pi_32a_minus120',32*4*pi-120>0)
    check('ratio_derivative_positive_for_a_at_least_4pi_16a_minus30',16*4*pi-30>0)
    check('ratio_denominator_positive_for_a_at_least_4pi',8*(4*pi)**2-30*4*pi+15>0)
    check('uniform_high_mode_mass_below_0p000002093',eta[3]<arb('0.000002093'))
    check('uniform_high_mode_mass_above_0p000002092',eta[3]>arb('0.000002092'))
    check('tail_envelope_for_t_at_most_half_k_at_most6',(-arb(2)).exp()/2+15*(-arb(3)).exp()<pi/2)
    tails={n:aa[n]*(aa[n]-4-(aa[n]/2)*arb(4).exp()).exp() for n in aa}
    evaluations=0
    def integral(n,k,T,x):
        nonlocal evaluations
        a=aa[n]
        def f(u,analytic):
            q=(4*u).exp();z=(T*u*u+u-a*(q-1)).exp()*(2*a*a*q*q-3*a*q)*u**k
            if x is None:return z
            phase=x*u
            return z*(phase.cos(),-phase.sin(),-phase.cos(),phase.sin())[k%4]
        z=acb.integral(f,0,1,rel_tol=arb('1e-32'),abs_tol=arb('1e-36'),eval_limit=200000,depth_limit=30)
        if not z.is_finite() or not z.imag.contains(0):raise ArithmeticError('integral failure')
        evaluations+=1
        return z.real+arb(0,tails[n])
    def vertices(T,x,orders=(0,1)):
        jets={n:{k:integral(n,k,T,x) for k in orders} for n in aa}
        ff={n:{k:jets[1][k]+c[2]*jets[2][k]+eta[n]*(c[n]*jets[n][k]-c[2]*jets[2][k]) for k in orders} for n in range(3,7)}
        return ff,jets
    search={'performed':bool(args.search),'status':'not performed'}
    if args.search:
        times=['0.01','0.05','0.1','0.25','0.5']; pairs=list(itertools.combinations(range(3,7),2));changes=[];candidates=[]
        for ts in times:
            T=arb(ts);previous=None
            for xint in range(20,301):
                x=arb(xint);ff,_=vertices(T,x)
                determinants={pair:ff[pair[0]][1]*ff[pair[1]][0]-ff[pair[0]][0]*ff[pair[1]][1] for pair in pairs}
                if previous:
                    for pair in pairs:
                        old=previous[1][pair];new=determinants[pair]
                        if (old>0 and new<0) or (old<0 and new>0):
                            changes.append({'T':ts,'pair':pair,'x_interval':[xint-1,xint]})
                previous=(xint,determinants)
            print('completed T',ts,'sign changes',len(changes),flush=True)
        for change in changes:
            T=arb(change['T']);n,m=change['pair'];left,right=map(arb,change['x_interval'])
            ff,_=vertices(T,left);dl=ff[n][1]*ff[m][0]-ff[n][0]*ff[m][1]
            for _ in range(35):
                mid=(left+right)/2;ff,_=vertices(T,mid);dm=ff[n][1]*ff[m][0]-ff[n][0]*ff[m][1]
                if not (dm>0 or dm<0):break
                if (dl>0 and dm>0) or (dl<0 and dm<0):left=mid;dl=dm
                else:right=mid
            mid=(left+right)/2;ff,_=vertices(T,mid,orders=(0,1,2))
            denom=ff[n][0]-ff[m][0]
            if denom.contains(0):continue
            q=-ff[m][0]/denom
            if q>0 and q<1:
                curvature=q*ff[n][2]+(1-q)*ff[m][2]
                item={**change,'refined_x_interval':[brec(left),brec(right)],'q_at_midpoint':brec(q),'curvature_at_midpoint':brec(curvature)}
                candidates.append(item);print('candidate',item,flush=True)
                break
        search={'performed':True,'status':'exploratory scan; refined pair candidates are not yet existence certificates','times':times,'x_grid':{'start':20,'end':300,'step':1},'support_nodes':[1,2,3,4,5,6],'determinant_sign_changes':changes,'candidates':candidates,'complete_integral_evaluations':evaluations}
    # Independent fixed-bracket certificate for the first robust candidate.
    T=arb(1)/100;left=arb('83.5323729');right=arb('83.5323730');mid=(left+right)/2;rho=(right-left)/2
    def combine(jets):
        return {n:{k:jets[1][k]+c[2]*jets[2][k]+eta[n]*(c[n]*jets[n][k]-c[2]*jets[2][k]) for k in jets[1]} for n in (3,4)}
    wronskians={}
    for name,x in [('left',left),('right',right)]:
        ff,_=vertices(T,x)
        wronskians[name]=ff[3][1]*ff[4][0]-ff[3][0]*ff[4][1]
    check('Wronskian_negative_at_left',wronskians['left']<0)
    check('Wronskian_positive_at_right',wronskians['right']>0)
    jets={n:{k:integral(n,k,T,mid) for k in range(4)} for n in range(1,5)}
    fc=combine(jets)
    moments={n:integral(n,4,T,None) for n in range(1,5)}
    M={n:moments[1]+c[2]*(1-eta[n])*moments[2]+c[n]*eta[n]*moments[n] for n in (3,4)}
    boxes={}
    for n in (3,4):
        # Taylor bounds combine the signed jets before using a positive fourth moment.
        b2=rho*fc[n][3].abs_upper()+rho**2*M[n].abs_upper()/2
        b1=rho*fc[n][2].abs_upper()+rho**2*fc[n][3].abs_upper()/2+rho**3*M[n].abs_upper()/6
        b0=rho*fc[n][1].abs_upper()+rho**2*fc[n][2].abs_upper()/2+rho**3*fc[n][3].abs_upper()/6+rho**4*M[n].abs_upper()/24
        boxes[n]={0:fc[n][0]+arb(0,b0),1:fc[n][1]+arb(0,b1),2:fc[n][2]+arb(0,b2)}
    diff=boxes[3][0]-boxes[4][0]
    check('vertex_value_difference_nonzero_on_bracket',not diff.contains(0))
    q=-boxes[4][0]/diff
    check('mixture_q_positive',q>0);check('mixture_q_less_than_one',q<1)
    curvature=q*boxes[3][2]+(1-q)*boxes[4][2]
    check('collision_second_derivative_positive_on_bracket',curvature>0)
    dp=boxes[3][2]*boxes[4][0]-boxes[3][0]*boxes[4][2]
    check('Wronskian_derivative_positive_on_bracket',dp>0)
    v={1:arb(1),2:c[2]*(1-q*eta[3]-(1-q)*eta[4]),3:c[3]*q*eta[3],4:c[4]*(1-q)*eta[4]}
    check('all_four_scaled_mode_weights_positive',all(z>0 for z in v.values()))
    raw={n:v[n]*((n*n-1)*pi).exp() for n in v}
    endpoint1=(-pi).exp()*sum((v[n]*d[n] for n in v),arb(0))
    endpoint3=(-pi).exp()*sum((v[n]*peval(poly(3),aa[n]) for n in v),arb(0))
    endpoint5=(-pi).exp()*sum((v[n]*peval(poly(5),aa[n]) for n in v),arb(0))
    check('first_endpoint_ball_contains_exact_algebraic_zero',endpoint1.contains(0))
    check('third_endpoint_ball_contains_exact_algebraic_zero',endpoint3.contains(0))
    check('fifth_endpoint_nonzero',not endpoint5.contains(0))
    primitive=(-pi).exp()*sum((v[n]*(1-4*aa[n]) for n in v),arb(0))
    check('primitive_derivative_negative',primitive<0)
    scale=-1/(2*primitive);check('primitive_normalization_positive',scale>0)
    detend=d[2]*d[3]*(r[3]-r[2]);check('endpoint_elimination_minor_nonzero',not detend.contains(0))
    tangent=-diff/(c[4]*eta[4]);jac=tangent*curvature
    check('infinite_tail_reduced_Jacobian_nonzero',not jac.contains(0))
    certificate={'status':'validated unique Wronskian root and nondegenerate positive-weight collision','T_exact':'1/100','x_bracket_exact_decimal':['83.5323729','83.5323730'],'definition':'F_n=G1+c2*G2+eta_n*(c_n*G_n-c2*G2), G_n=exp(pi*n^2)H_n, c_n=-P1(pi)/P1(pi*n^2), eta_n=(r1-r2)/(rn-r2). F=qF3+(1-q)F4, q=-F4/(F3-F4) at unique Wronskian root. Fixed raw weights a_n=v_n exp((n^2-1)pi), then positive primitive normalization.','Wronskian_at_left':brec(wronskians['left']),'Wronskian_at_right':brec(wronskians['right']),'Wronskian_derivative_on_bracket':brec(dp),'q_enclosure':brec(q),'F3_minus_F4_on_bracket':brec(diff),'scaled_transform_second_x_derivative':brec(curvature),'raw_weights':{str(n):brec(raw[n]) for n in raw},'scaled_mode_weights_v':{str(n):brec(v[n]) for n in v},'source_first_and_third_endpoint':'exactly zero by vertex construction; ball consistency checked','raw_source_fifth_endpoint':brec(endpoint5),'primitive_first_endpoint_before_final_scale':brec(primitive),'positive_final_normalization':brec(scale),'normalized_source_fifth_endpoint':brec(scale*endpoint5),'endpoint_minor':brec(detend),'reduced_continuation_jacobian':brec(jac),'tail_bound_per_G_n_jet_order_0_through6':{str(n):brec(tails[n]) for n in range(1,5)},'vertex_boxes':{str(n):{str(k):brec(z) for k,z in boxes[n].items()} for n in boxes},'fourth_absolute_moment_bounds':{str(n):brec(M[n]) for n in M},'complete_integral_evaluations_in_this_run':evaluations,'infinite_tail_continuation':'Qualitative only: positive fixed weights on every node persist after adding a sufficiently small positive unweighted tail and solving the two endpoints plus H=Hx=0 using the nonzero reduced Jacobian. No explicit epsilon radius.'}
    history={'description':'Exploratory discovery run completed the declared five time grids before candidate refinement was interrupted after robust candidates were found. The fixed-bracket certificate is separate and replayed by this checker. No absence claim is inferred from the grid.','times':['0.01','0.05','0.1','0.25','0.5'],'x_grid_start':20,'x_grid_end':300,'x_grid_step':1,'support_nodes':[1,2,3,4,5,6],'pair_determinant_sign_changes_total_reported':468,'first_selected_pair':[3,4],'first_selected_candidate_x':'83.53237296145','scope':'No completeness claim for candidate refinements; no assertion that each determinant crossing gives an admissible collision.'}
    rec={'date':'2026-10-15','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra','llm_assistance':'Substantial LLM assistance','checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':args.bits,'python_version':platform.python_version(),'python_flint_version':flint.__version__,'P1':poly(1),'P3':poly(3),'P5':poly(5),'r_values':{str(n):brec(r[n]) for n in r},'eta_values':{str(n):brec(eta[n]) for n in eta},'uniform_mass_bound':brec(eta[3]),'checks':checks,'assertions_passed':len(checks),'search':search,'discovery_history':history,'collision_certificate':certificate,'elapsed_seconds':time.monotonic()-start}
    serialized = json.dumps(rec, indent=2)+'\n'
    if args.output:
        args.output.write_text(serialized)
    print(serialized, flush=True)
if __name__=='__main__':main()
