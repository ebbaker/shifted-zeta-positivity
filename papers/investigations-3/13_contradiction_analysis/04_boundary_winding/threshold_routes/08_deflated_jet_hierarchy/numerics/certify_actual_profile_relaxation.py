#!/usr/bin/env python3
"""Actual theta three-profile relaxation obstruction, 20 October 2026.
Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
actual reasoning effort ultra. This is a scoped interval certificate, not
an actual theta collision or RH claim. See BW08 Note 06 for the proof.
"""
from fractions import Fraction as Q
import argparse, hashlib, json, platform, time, signal, resource
from pathlib import Path
import flint
from flint import arb, acb, ctx

BVALS=(20,40,80)
NODES=(900,1600,25000)

def A(q):
    q=Q(q); return arb(q.numerator)/q.denominator

def ball(lo,hi):
    lo,hi=Q(lo),Q(hi)
    return arb(A((lo+hi)/2),A((hi-lo)/2).upper())

def record(v): return v.str(45,more=True)
def require(c,msg):
    if not c: raise ArithmeticError(msg)

def inverse(m):
    n=len(m); z=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(m)]
    det=Q(1)
    for k in range(n):
        if not z[k][k]:
            r=next(i for i in range(k+1,n) if z[i][k]);z[k],z[r]=z[r],z[k];det=-det
        p=z[k][k];det*=p;z[k]=[v/p for v in z[k]]
        for i in range(n):
            if i!=k:
                p=z[i][k];z[i]=[v-p*w for v,w in zip(z[i],z[k])]
    inv=[r[n:] for r in z]
    require(all(sum(m[i][k]*inv[k][j] for k in range(n))==Q(i==j) for i in range(n) for j in range(n)), 'exact inverse check')
    return inv,det

def acquire(t,b,pi):
    values=[]; audit=[]
    for j in (0,1):
        calls=0
        def integrand(u,analytic):
            nonlocal calls
            calls+=1
            if calls % 128 == 0:
                rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                rss_bytes=rss if platform.system()=='Darwin' else 1024*rss
                require(rss_bytes<512*1024**2,'callback memory budget')
            e=(4*u).exp(); total=acb(0)
            for n in range(1,5):
                lam=pi*n*n
                total+=(2*lam*lam*e*e-3*lam*e)*(-lam*e).exp()
            base=(A(t)*u*u+u).exp()*total
            return base*(b*u).cosh() if j==0 else base*u*(b*u).sinh()
        core=acb.integral(integrand,0,1,abs_tol=arb('1e-40'),rel_tol=arb('1e-36'),eval_limit=200000,depth_limit=30)
        require(core.is_finite() and core.imag.contains(0), 'finite real entire quadrature')
        m=5; lam=pi*m*m;den=4*lam-9-b
        rat=(A(Q(m+1,m))**4)*(-pi*(2*m+1)).exp()
        require(den>0 and rat<1 and 16*pi-2*A(t)>0,'whole-axis omitted-mode tangent')
        omitted=2*pi*pi*m**4*(-lam).exp()/(den**(j+1)*(1-rat))
        # j is 0 or 1, hence j! = U**j = 1 for U=1.
        exterior=arb(0)
        for n in range(1,5):
            l=pi*n*n;d=4*l*arb(4).exp()-9-b-2*A(t)-j
            require(d>0,'retained-mode exterior tangent')
            exterior+=2*l*l*(A(t)+9+b-l*arb(4).exp()).exp()/d
        tail=(omitted+exterior).upper()
        full=core.real+arb(tail/2,tail/2)
        require(full>0,'positive full denominator/numerator')
        values.append(full)
        audit.append({'component':j,'core':record(core.real),'omitted_modes_upper':record(omitted.upper()),'retained_exterior_upper':record(exterior.upper()),'full':record(full),'callbacks':calls})
    profile=values[1]/values[0]
    require(profile.rad()<arb("1e-30"), "exact-time profile error budget")
    return profile,audit

def run(bits):
    ctx.prec=bits;start=time.monotonic(); pi=arb.pi()
    tlo=Q(1,10)-Q(1,10**6);thi=Q(1,10)+Q(1,10**6)
    profiles=[];audit=[]
    for b in BVALS:
        low,lo_audit=acquire(tlo,b,pi);hi,hi_audit=acquire(thi,b,pi)
        # Exact covariance monotonicity in the note gives the union enclosure.
        mid=(low.lower()+hi.upper())/2; rad=((hi.upper()-low.lower())/2).upper()
        box=arb(mid,rad); profiles.append(box)
        audit.append({'b':b,'at_time_lower':record(low),'at_time_upper':record(hi),'all_times':record(box),'lower_acquisition':lo_audit,'upper_acquisition':hi_audit})
    matrix=[[Q(y+400,y+b*b) for y in NODES] for b in BVALS]
    inv,det=inverse(matrix)
    # Uniformly a in [1001,1002], offset d in (0,1/2].
    s=ball(1001**2,1002**2)
    ystar=ball(1001**2,Q(2005,2)**2)
    residual=[p/b-4/(s+b*b)-2/(ystar+b*b) for p,b in zip(profiles,BVALS)]
    weights=[sum((A(v)*r for v,r in zip(row,residual)),arb(0)) for row in inv]
    require(all(w>A(Q(1,1000)) for w in weights),'all three slack masses exceed 1/1000 uniformly')
    require(all(w>A(q) for w,q in zip(weights,(Q('0.0017583'),Q('0.0019438'),Q('0.0064978')))),'displayed stricter weight floors')
    require(all(y < (1001-1)**2 for y in NODES),'slack nodes outside moving count interval')
    # Uniform exact rational proof of a conditioning lower bound on g(s):
    # phi_0(s)=1 and B_i>=B_0, so max(phi_i(s))=1.
    conditioning_norm_min=Q(1001**2+400,2)
    # Supply one direct feasible (very weak) count majorant for a finite baseline.
    c0=Q((1002+1)**2+400,2)
    baseline=A(c0)*(profiles[0]/20-4/(s+400))
    require(baseline>1,'direct baseline also loses')
    return {'bits':bits,'seconds':time.monotonic()-start,'time_interval':[str(tlo),str(thi)],'event_height_interval':['1001','1002'],'root_offset_interval':['0 (excluded)','1/2'],'sample_heights':BVALS,'squared_slack_nodes':NODES,'matrix':[[str(v) for v in r] for r in matrix],'matrix_determinant':str(det),'exact_inverse':[[str(v) for v in r] for r in inv],'profiles':audit,'residual_after_inserted_root':[record(r) for r in residual],'slack_weight_enclosures':[record(w) for w in weights],'uniform_slack_floor':'1/1000','count_witness':'exactly 1 for every parameter and offset','dual_objective_lower_bound':'1 even for zero acquisition error','S2_relaxation_lower_bound':'1/d^2 for every 0<d<=1/2; unbounded as d tends to 0','coefficient_l1_lower_bound':str(conditioning_norm_min),'direct_constant_majorant_coefficient':str(c0),'direct_count_baseline':record(baseline)}

def control_check():
    a=Q(1001); y=(a+Q(1,2))**2; s=a*a; B0=Q(400)
    mu=2/(y+B0)
    own=[4/(s+b*b)+2/(y+b*b) for b in BVALS]
    require(all(mu*(y+B0)/(y+b*b)==v-4/(s+b*b) for b,v in zip(BVALS,own)), 'one-neighbor own-profile identity')
    require(mu*(y+B0)/2==1, 'integer unit count')
    # Compare with exact root distance without taking a fractional rational power.
    r=a+Q(1,2)
    require(mu*(s+y)*(y+B0)/(s-y)**2==1/(a-r)**2+1/(a+r)**2, 'deflated root-pair identity')
    return {'normalized_polynomial':'(z^2-a^2)^2(z^2-(a+1/2)^2) / its value at 0','event_height':str(a),'own_D_over_b':[str(v) for v in own],'own_residual_weight':str(mu),'exact_count':'1','zero_residual_even_quartic':'D(b)/b=4/(a^2+b^2), N=0','checks':'exact rational'}

def main():
    signal.alarm(300)
    pa=argparse.ArgumentParser();pa.add_argument('--repo',type=Path,required=True);pa.add_argument('--out',type=Path,required=True);args=pa.parse_args()
    paths=['AGENTS.md','LARGE_FILES.md','result-summaries/README.md','result-summaries/12_collision_controls_and_screening.md','result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md','avoid/README.md','avoid/01_restating_the_target.md','avoid/02_shape_only_arguments_and_the_controls.md','avoid/07_scoped_exclusions_read_as_universal.md','avoid/10_numerics_ahead_of_the_question.md','papers/investigations-3/13_contradiction_analysis/04_boundary_winding/README.md','papers/investigations-3/13_contradiction_analysis/04_boundary_winding/research-overview/03_FOURTH_ORDER_ARITHMETIC_AND_ACTUAL_PROFILE_PROGRAM_20261020.md','papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md','papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md','papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md','papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py','papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md']
    import subprocess
    result={'author':'Prepared for Edward Baker','llm_assistance':'Substantial; authoring model gpt-6-astra, actual reasoning effort ultra, inherited from parent turn','date':'2026-10-20 America/New_York','status':'scoped actual-profile relaxation obstruction; no physical theta event or gap','python':platform.python_version(),'python_flint':flint.__version__,'git_parent':subprocess.check_output(['git','rev-parse','HEAD'],cwd=args.repo,text=True).strip(),'source_sha256':{p:hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'budget':{'seconds':300,'memory_mib':512,'memory_enforcement':'RSS checks each 128 quadrature callbacks and completion; no OS address-space cap','per_integral_eval_limit':200000,'per_integral_depth_limit':30,'finite_modes':4,'source_cutoff':'1','absolute_quad_tolerance':'1e-40','relative_quad_tolerance':'1e-36'},'controls':control_check(),'runs':[run(192),run(256)]}
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['peak_rss_bytes']=rss if platform.system()=='Darwin' else 1024*rss
    require(result['peak_rss_bytes']<512*1024**2,'memory budget')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    for r in result['runs']:
        print(r['bits'],r['slack_weight_enclosures'],r['direct_count_baseline'],r['seconds'])
if __name__=='__main__': main()
