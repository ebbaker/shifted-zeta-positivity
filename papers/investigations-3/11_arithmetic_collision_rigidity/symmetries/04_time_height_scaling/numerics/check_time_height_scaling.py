#!/usr/bin/env python3
"""Complete signed S04 leading-data jet; outward Arb checks, no global exclusion.

18 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual reasoning effort ultra.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import time
import flint
from flint import arb, acb, acb_series, ctx

def A(v):
    return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v): return v.str(36,more=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(c,m):
    if not c: raise ArithmeticError(m)
def floor(v): return int(v.floor().unique_fmpz())
def norm(v): return (v[0]**2+v[1]**2).sqrt()
def uppernorm(v): return (abs(v[0]).upper()**2+abs(v[1]).upper()**2).sqrt().upper()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def disk_budget(x,t,R,N,logs):
    """Current fixed-cutoff disk contract, point time; pays both possible m."""
    pi=arb.pi(); xm=x-R; xp=x+R; qm=xm/(4*pi); qp=xp/(4*pi)
    V=xm/2; S=(xp*xp+(1+R)**2).sqrt()/2
    al=qm.log()/2-1/(V*V)
    ast=3/(2*V)+((S/(2*pi)).log()**2+pi*pi/4).sqrt()/2
    dst=3/(2*V*V)+1/(2*V); lst=ast*(1+t*dst/2); K=(R*lst/2).exp()
    mlo=floor((qm+t/16).sqrt()); mhi=floor((qp+t/16).sqrt())
    check(mlo>=3 and 0<=mhi-mlo<=1,'permitted cutoff range')
    def term(n):
        ell=logs[n] if n<len(logs) else A(n).log()
        vn=(-ell/2+t*(ell*ell/4-al*ell/2)).exp()
        un=((t*t*max(abs((qm/(n*n)).log()).upper(),abs((qp/(n*n)).log()).upper())**2/16+A('.626'))/(xm-A('6.66'))).exp()-1
        return (1+(R*ell+t*R*A(mhi).log()/(2*(xm-6))).exp())*vn*un, (R*ell/2).exp()*vn
    # Using mhi in the AB multiplier majorizes every permitted m.
    partial=A(0); ab={}
    for n in range(1,mhi+1):
        vv,_=term(n); partial+=vv
        if n>=mlo: ab[n]=partial
    rows=[]
    for m in range(mlo,mhi+1):
        ec=qm**(-A(F(1,4)))*(-t*qm.log()**2/16+A('1.24')*(3**R+3**(-R))/(m-A('.125'))+(3*(qp.log()**2+pi*pi/4).sqrt()+A('10.44'))/(xm-12)).exp()
        jump=2*sum((term(n)[1] for n in range(min(m,N)+1,max(m,N)+1)),A(0))
        rows.append({'m':m,'AB':ab[m],'C':ec,'jump':jump,'eta':K*(ab[m]+ec+jump)})
    eta=max(v['eta'].upper() for v in rows)
    return eta,{'radius':out(R),'fixed_cutoff':N,'possible_natural_cutoffs':list(range(mlo,mhi+1)),
        'K':out(K),'parts':[{'m':v['m'],**{k:out(v[k]) for k in ('AB','C','jump','eta')}} for v in rows]}

def evaluate(old,x,t,kappa,label,Nfixed=None,expected_m=None,known_natural=None):
    check(isinstance(t,F) and 0<t<=F(1,20),'exact rational time regime')
    exact_t=t; t=A(t)
    if isinstance(kappa,F):
        check(1<=kappa<=2,'exact rational kappa regime'); exact_kappa=str(kappa); kappa=A(kappa)
    else:
        check(kappa>1 and kappa<2,'interior crossing kappa regime'); exact_kappa='t*log(22027^2-t/16)'
    started=time.monotonic(); pi=arb.pi(); ii=acb(0,1); L=(x/(4*pi)).log(); R=1/L
    root=(x/(4*pi)+t/16).sqrt()
    if known_natural is None:Nnat=floor(root)
    else:
        check(root.contains(known_natural),'symbolically exact crossing root')
        Nnat=known_natural
    N=Nnat if Nfixed is None else Nfixed
    check(N<=Nnat,'fixed cutoff is a prefix of natural center cutoff')
    s=(1-ii*x)/2; alpha=old.alpha(s); ap=old.alphap(s)
    th=old.mt(s,t).imag; mp=alpha*(1+t*ap/2); Omega=mp.real/2; a=mp.imag/2
    U=ap.real; V=ap.imag; T0=(x+t*pi/4)/2
    # These finite sums have no mode truncation beyond the inherited RS tail.
    exact=[A(0),A(0)]; model=[A(0),A(0)]; difference=[A(0),A(0)]
    ranges={q:{'exact':[A(0),A(0)],'model':[A(0),A(0)],'mass':A(0)} for q in ('low','intermediate','terminal')}
    H=floor(A(N)**A(F(3,4))); Kedge=N-H; logs=[A(0)]; mass=A(0); removed_heat_phase=[A(0),A(0)]
    edge_term=None
    for n in range(1,N+1):
        ell=A(n).log(); logs.append(ell)
        W=(t*ell*ell/4-(A(F(1,2))+t*L/4)*ell).exp(); mass+=W
        psi=th+T0*ell; base=W*acb(psi.cos(),psi.sin())
        delta=-t*ell/2*(alpha-acb(L/2,-pi/4)); ed=delta.exp(); whole=base*ed
        r=4*Omega/L-2*(1+t*U/2)*ell/L; c=t*V*ell/L; z=acb(r,-c)
        rt=4*Omega/L-2*ell/L; ct=t*ell/(L*x); zt=acb(rt,-ct)
        ex=[whole.real,(whole*z).imag]; mo=[base.real,(base*zt).imag]
        dd=[(base*(ed-1)).real,(base*((ed-1)*z+(z-zt))).imag]
        bucket='low' if n<=16 else ('intermediate' if n<=Kedge else 'terminal')
        ranges[bucket]['mass']+=W
        for j in range(2):
            exact[j]+=ex[j]; model[j]+=mo[j]; difference[j]+=dd[j]
            ranges[bucket]['exact'][j]+=ex[j]; ranges[bucket]['model'][j]+=mo[j]
        if n==N: edge_term={'value':out(2*mo[0]),'dx':out(L*mo[1]/2),'heat_phase_shift':out(t*pi*ell/8),'amplitude_drift_log':out(t*ell*ell/4)}
    eta,ledger=disk_budget(x,t,R,N,logs)
    if expected_m is not None: check(ledger['possible_natural_cutoffs']==expected_m,'crossing cutoff enclosure')
    aa=kappa*(4-kappa)/16; bb=kappa*(kappa+4)/16; dd=kappa*(kappa+12)/16
    model_bound=(-dd/t).exp(); analytic_eta=5*(-bb/t).exp()
    check(mass<5*(aa/t).exp(),'uniform complete mass bound')
    check(eta<analytic_eta,'fresh eta within inherited conservative payment')
    for j in range(2):
        check((exact[j]-model[j]-difference[j]).contains(0),'stable difference identity')
        check(abs(difference[j])<A('.7')*model_bound,'uniform coordinate replacement bound')
    check(uppernorm(difference)<model_bound,'uniform Euclidean replacement bound')
    # Q,Qx refer to the complete source, not merely the arithmetic sum.
    # Their outward error is the imported analytic disk contract.
    physical=[2*model[0],L*model[1]/2+2*a*model[0]]
    value_error=eta+A('1.4')*model_bound
    dx_error=(L+abs(a).upper())*eta+(A('.35')*L+A('1.4')*abs(a).upper())*model_bound
    physical_error=[value_error,dx_error]
    total_vector_error=A(17).sqrt()/2*eta+model_bound
    lower=(norm(model).lower()-total_vector_error).lower()
    physlower=(norm(physical).lower()-uppernorm(physical_error)).lower()
    return {'label':label,'t_exact':str(exact_t),'kappa_exact':exact_kappa,'t':out(t),'kappa':out(kappa),'x':out(x),'L':out(L),'natural_center_cutoff':Nnat,'fixed_cutoff':N,
        'fixed_time_derivative':True,'ranges':{'low':'1..16','intermediate':f'17..{Kedge}','terminal':f'{Kedge+1}..{N}','edge_length':H},
        'range_signed_sums':{k:{q:[out(vv) for vv in v] if isinstance(v,list) else out(v) for q,v in row.items()} for k,row in ranges.items()},
        'exact_finite_vector':[out(v) for v in exact],'model_vector':[out(v) for v in model],
        'exact_minus_model':[out(v) for v in difference],'exact_minus_model_norm_upper':out(uppernorm(difference)),
        'model_vector_norm':out(norm(model)),'sum_model_magnitudes':out(mass),
        'uniform_model_vector_error':out(model_bound),'uniform_model_coordinate_error':out(A('.7')*model_bound),
        'model_error_over_uniform_RS_bound':out(model_bound/analytic_eta),
        'current_RS_disk':ledger,'current_RS_eta':out(eta),'inherited_uniform_RS_eta':out(analytic_eta),
        'complete_scaled_jet_error':out(total_vector_error),'complete_scaled_jet_norm_lower':out(lower),
        'physical_jet_divided_by_A_model':[out(v) for v in physical],
        'physical_jet_divided_by_A_errors':[out(v) for v in physical_error],
        'complete_physical_jet_divided_by_A_norm_lower':out(physlower),'log_A':out((old.mt(s,t)+old.mt(1-s,t)).real/2),
        'last_model_mode_added_identity':edge_term,
        'error_disclosure':{'RS_mode_tail_and_correction':'AB+C above; no further source or mode cutoff',
          'cutoff_transition':'exact all added/removed modes in jump above',
          'source_quadrature':'none introduced; established RS theorem imported',
          'rounding_and_phase':'outward Arb/Acb in every finite expression',
          'derivative':'same scalar differentiated at fixed t,N; Cauchy eta/R',
          'whole_cell_propagation':'none; these are point jets, disk residual uniform in z only'},
        'seconds':time.monotonic()-started}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--repo',type=Path,required=True); p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192); p.add_argument('--execution-model',required=True); p.add_argument('--execution-effort',required=True); args=p.parse_args()
    started=time.monotonic(); ctx.prec=args.bits; ctx.cap=32; repo=args.repo.resolve()
    base=repo/'papers/investigations-3/11_arithmetic_collision_rigidity'
    oldpath=base/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
    oldrecord=oldpath.with_name('S02_CUTOFF_REFLECTION_192_20261018.json'); prior=json.loads(oldrecord.read_text())
    check(prior['script_sha256']==sha(oldpath),'S02 script hash')
    for rel,pin in prior['source_sha256'].items():check(sha(repo/rel)==pin,'S02 analytic source '+rel)
    old=load('s04_old_s02',oldpath)
    rows=[]
    for k,t in ((F(1),F(1,20)),(F(1),F(1,21)),(F(21,20),F(1,20))):
        kap=A(k); tt=A(t); xx=4*arb.pi()*(kap/tt).exp()
        rows.append(evaluate(old,xx,t,k,f'kappa={k},t={t}'))
    # A single fixed scalar on a disk crossing m=22027, not a differentiated floor.
    tt=A(F(1,20)); crossing=22027; xx=4*arb.pi()*(crossing**2-tt/16); kap=tt*(xx/(4*arb.pi())).log()
    row=evaluate(old,xx,F(1,20),kap,'cutoff_crossing_22027',Nfixed=crossing-1,expected_m=[crossing-1,crossing],known_natural=crossing)
    ell=A(crossing).log(); s=(1-acb(0,1)*xx)/2; th=old.mt(s,tt).imag; al=old.alpha(s); ap=old.alphap(s)
    om=(al*(1+tt*ap/2)).real/2; LL=(xx/(4*arb.pi())).log()
    WW=(tt*ell**2/4-(A(F(1,2))+tt*LL/4)*ell).exp(); ps=th+(xx+tt*arb.pi()/4)*ell/2
    added=[2*WW*ps.cos(),WW*(2*(om-ell/2)*ps.sin()-tt*ell/(2*xx)*ps.cos())]
    # Independent series differentiation of the same analytic single mode.
    zs=acb_series([acb(xx),acb(1)],2); ss=(1-acb(0,1)*zs)/2
    theta=(old.mt(ss,tt)-old.mt(1-ss,tt))/(2*acb(0,1))
    lser=(zs/(4*arb.pi())).log(); wser=(tt*ell**2/4-(A(F(1,2))+tt*lser/4)*ell).exp()
    mode_ser=2*wser*(theta+(zs+tt*arb.pi()/4)*ell/2).cos()
    for j in range(2):
        check(mode_ser[j].imag.contains(0),'real analytic model transition')
        check((mode_ser[j].real-added[j]).contains(0),'frozen-time transition derivative')
    row['crossing_exact_domain']={'t':'1/20','center':'4*pi*(22027^2-t/16)','disk_radius':'1/log(x/(4*pi))','fixed_cutoff':crossing-1}
    row['model_added_mode_22027_value_dx']=[out(v) for v in added]
    row['independent_transition_series_check']=True
    rows.append(row)
    sourcepaths=[oldpath,oldrecord,base/'research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md',
        base/'manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex',
        repo/'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex']
    record={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
      'actual_model':args.execution_model,'actual_effort':args.execution_effort,'llm_assistance':'substantial; same-model analytic checks and review',
      'status':'outward finite point-jet comparisons; analytic uniform replacement proved in companion note; no global exclusion',
      'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':args.bits,
      'script_sha256':sha(__file__),'source_sha256':{str(v.relative_to(repo)):sha(v) for v in sourcepaths},
      'declared_domain':{'kappa':['1','2'],'t':['0 (excluded)','1/20'],'x':'4*pi*exp(kappa/t)'},
      'primary_gate':'uniform full signed scalar and frozen-time derivative replacement, paid at exp(-kappa*(kappa+12)/(16*t)); no frozen-amplitude claim',
      'matched_kappa_rows':[0,1],'same_height_different_time_rows':[1,2],'rows':rows,'seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'rows':len(rows),'seconds':record['seconds'],
      'model_errors':[v['exact_minus_model_norm_upper'] for v in rows],
      'complete_jet_lower_bounds':[v['complete_scaled_jet_norm_lower'] for v in rows]}))

if __name__=='__main__':main()
