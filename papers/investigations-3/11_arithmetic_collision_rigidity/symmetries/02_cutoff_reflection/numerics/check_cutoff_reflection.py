#!/usr/bin/env python3
"""Bounded S02 complete disk-error comparison; no noncollision claim.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring configuration: gpt-6.1-sol, actual effort ultra.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time
import flint
from flint import arb, acb, acb_series, ctx

def A(x):
    return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def interval(lo,hi):
    lo,hi=A(lo),A(hi)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def out(x): return x.str(38,more=True)
def check(ok,message):
    if not ok: raise ArithmeticError(message)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cap(*xs): return max(x.abs_upper() for x in xs)
def m0(s):
    return s.log()+(s-1).log()-s*arb.pi().log()/2+(2*arb.pi()).sqrt().log()-A(16).log()+(s/2-A(F(1,2)))*(s/2).log()-s/2
def alpha(s): return 1/(2*s)+1/(s-1)+(s/(2*arb.pi())).log()/2
def alphap(s): return -1/(2*s*s)-1/((s-1)*(s-1))+1/(2*s)
def alphapp(s): return 1/s**3+2/(s-1)**3-1/(2*s*s)
def mt(s,t): return m0(s)+t*alpha(s)**2/4
def normalizer(z,t):
    s=(1-acb(0,1)*z)/2
    return ((mt(s,t)+mt(1-s,t))/2).exp()
def mode(z,t,n):
    s=(1-acb(0,1)*z)/2; l=A(n).log()
    return sum(((mt(v,t)+t*l*l/4-(v+t*alpha(v)/2)*l).exp() for v in (s,1-s)),acb(0))
def profile(p):
    pi=arb.pi(); phi=pi*(p*p/2+A(F(3,8))); c=(pi*p).cos()
    D=phi.cos()/(2*c)
    E=(phi.sin()-A(2).sqrt()*(pi*p/2).cos())/(2*c)
    Dp=(-pi*p*phi.sin()+2*pi*(pi*p).sin()*D)/(2*c)
    Ep=(pi*p*phi.cos()+A(2).sqrt()*pi/2*(pi*p/2).sin()+2*pi*(pi*p).sin()*E)/(2*c)
    return D,E,Dp,Ep
def J(z,t,N):
    v=z/2+arb.pi()*t/8; a=(v/(2*arb.pi())).sqrt(); p=2*N+1-2*a
    D,E,Dp,Ep=profile(p)
    f=v.sqrt()*(v*D-E)
    fp=3*v.sqrt()*D/4-E/(4*v.sqrt())-(v*Dp-Ep)/(2*(2*arb.pi()).sqrt())
    return f,fp
def correction(z,t,N):
    f,_=J(z,t,N)
    return (-1)**(N+1)*arb.pi().sqrt()/4*(-arb.pi()*z/8-arb.pi()**2*t/64).exp()*f
def corrected(z,t,N):
    return (sum((mode(z,t,n) for n in range(1,N+1)),acb(0))-correction(z,t,N))/normalizer(z,t)
def W_real(x,t):
    ar=(1+x*x).log()/4-(4*arb.pi()).log()/2-1/(1+x*x)
    ai=x.atan()/2-3*x/(1+x*x)
    return 8*arb.pi()**A(F(1,4))*(1+x*x)**(-A(F(7,8)))*(A(F(1,4))-x*(1/x).atan()/4-t*(arb.pi()**2/64+(ar*ar-ai*ai)/4)).exp()
def transition(z,t,N):
    v=z/2+arb.pi()*t/8; a=(v/(2*arb.pi())).sqrt()
    p=2*N+1-2*a; psi=arb.pi()*((p+1)**2/2-A(F(1,8)))
    shift=(-1)**(N+2)*arb.pi().sqrt()/4*(-arb.pi()*z/8-arb.pi()**2*t/64).exp()*v.sqrt()*(v*psi.cos()-psi.sin())
    return (mode(z,t,N+1)-shift)/normalizer(z,t)

def disk_budget(xlo,xhi,N,nt,nx,ny,transition_needed):
    """Union of radius-1/2 disks at every real X in [xlo,xhi]."""
    pi=arb.pi(); R=A(F(1,2)); eps=A(F(1,100)); tau=A(F(1,5))
    xm=A(xlo)-R; xp=A(xhi)+R; qlo=xm/(4*pi); qhi=xp/(4*pi)
    V=xm/2; S=(xp*xp+(1+R)**2).sqrt()/2
    al=qlo.log()/2-1/(V*V)
    ast=3/(2*V)+( (S/(2*pi)).log()**2+pi*pi/4).sqrt()/2
    dst=3/(2*V*V)+1/(2*V); lst=ast*(1+tau*dst/2); K=(R*lst/2).exp()
    omega=(al-tau*ast*dst/2)/2
    mlo=int((qlo+eps/16).sqrt().floor().unique_fmpz()); mhi=int((qhi+tau/16).sqrt().floor().unique_fmpz())
    check(mlo==8 and mhi==(9 if transition_needed else 8),'cutoff range')
    eab=[]; ec0=[]; jumps=[]
    for m in range(mlo,mhi+1):
        ab=A(0); jump=A(0)
        for n in range(1,m+1):
            l=A(n).log(); d=l*l/4-al*l/2
            vn=A(n)**(-A(F(1,2)))*max((eps*d).upper(),(tau*d).upper()).exp()
            ell=max(abs((qlo/(n*n)).log()).upper(),abs((qhi/(n*n)).log()).upper())
            un=((tau*tau*ell*ell/16+A('.626'))/(xm-A('6.66'))).exp()-1
            ab+=(1+A(m)**(tau*R/(2*(xm-6)))*A(n)**R)*vn*un
            if n>N: jump+=2*A(n)**(R/2)*vn
        c0=qlo**(-A(F(1,4)))*(-eps*qlo.log()**2/16+A('1.24')*(3**R+3**(-R))/(m-A('.125'))+(3*(qhi.log()**2+pi*pi/4).sqrt()+A('10.44'))/(xm-12)).exp()
        eab.append(ab); ec0.append(c0); jumps.append(jump)
    old=K*max((eab[i]+ec0[i]+jumps[i]).upper() for i in range(len(eab)))
    # Bound the slowly varying prefactor on the real enclosing interval;
    # A(x)/A(x+iy) costs K, from the same logarithmic-derivative bound.
    W=W_real(interval(xm,xp),interval(eps,tau)).upper()
    vr=interval(xm/2+pi*eps/8,xp/2+pi*tau/8)
    pref=(K*W/2*vr.sqrt()*(vr*vr+1).sqrt()).upper()
    tilde=((A('.397')*(9**((1+R)/2)+9**((1-R)/2))/((qlo+eps/16).sqrt()-A('.865'))+A(10)/(3*(xm/2-6)))*(A('3.49')/(xm/2-4)).exp()).upper()
    # Closed rational cell cover of upper enclosing rectangle and time slab.
    # No floor-defined function is differentiated. Natural m may be either
    # endpoint on any cell; both continuations are bounded below.
    maxfp=A(0); maxtransition=A(0); count=0; started=time.monotonic()
    for it in range(nt):
        t=interval(F(1,100)+F(19,100)*it/nt,F(1,100)+F(19,100)*(it+1)/nt)
        for ix in range(nx):
            x=interval(F(xlo)-F(1,2)+(F(xhi-xlo)+1)*ix/nx,F(xlo)-F(1,2)+(F(xhi-xlo)+1)*(ix+1)/nx)
            for iy in range(ny):
                y=interval(F(iy,2*ny),F(iy+1,2*ny)); z=acb(x,y)
                for m in range(mlo,mhi+1):
                    _,fp=J(z,t,m); check(fp.is_finite(),'profile derivative finite')
                    maxfp=max(maxfp,abs(fp).upper())
                if transition_needed:
                    dd=transition(z,t,N); check(dd.is_finite(),'transition finite')
                    maxtransition=max(maxtransition,abs(dd).upper())
                count+=1
    mismatch=K*W*R*maxfp
    shared=K*max(v.upper() for v in eab)
    ec=pref*tilde
    candidate=shared+ec+mismatch+maxtransition
    # A second matched baseline uses precisely the same pre-relaxation
    # amplitude and eps bounds, paying the leading correction absolutely.
    jumpmax=max(v.upper() for v in jumps)
    matched=shared+pref*(1+tilde)+K*jumpmax
    check(candidate<old,'strict improvement versus current complete eta')
    check(candidate<matched,'strict improvement versus matched absolute correction')
    check(omega>0,'nonzero phase derivative')
    appr=3/V**3+1/(2*V*V)
    logA1=lst/2; logA2=(dst*(1+tau*dst/2)+tau*ast*appr/2)/4
    factors=[A(1),1/R+logA1,2/R**2+2*logA1/R+logA1**2+logA2]
    result={
      'real_domain':{'t':['1/100','1/5'],'x':[str(xlo),str(xhi)]},
      'disk_radius':'1/2','enclosing_real_interval':[str(F(xlo)-F(1,2)),str(F(xhi)+F(1,2))],
      'fixed_cutoff':N,'possible_natural_cutoffs':list(range(mlo,mhi+1)),
      'retained_neighbors': 'all n<=8; cutoff-neighbor 9 enters exact signed transition' if transition_needed else 'all n<=8, including cutoff neighbors 7 and 8',
      'closed_rectangle_cells':count,'grid':[nt,nx,ny],'seconds':time.monotonic()-started,
      'constants':{k:out(v) for k,v in {'alpha_lower':al,'Astar':ast,'Dstar':dst,'Lstar':lst,'Kstar':K,'omega_lower':omega,'W_real_upper':W,'correction_amplitude_over_A_upper':pref,'tilde_epsilon_sum_upper':tilde,'slow_profile_z_derivative_upper':maxfp}.items()},
      'error_parts':{k:out(v) for k,v in {'AB_shared':shared,'signed_C_remainder':ec,'holomorphic_continuation_mismatch':mismatch,'signed_cutoff_transition':maxtransition,'baseline_absolute_cutoff_transition':K*jumpmax}.items()},
      'eta_current_absolute':out(old),'eta_matched_absolute':out(matched),'eta_candidate':out(candidate),
      'candidate_over_current':out(candidate/old),'candidate_over_matched':out(candidate/matched),
      'Q_derivative_errors':{'current':[out(math.factorial(j)*old/R**j) for j in range(3)],'candidate':[out(math.factorial(j)*candidate/R**j) for j in range(3)]},
      'phase_scaled_first_jet_error':{'current':out(old*(1+1/(R*omega)**2).sqrt()),'candidate':out(candidate*(1+1/(R*omega)**2).sqrt())},
      'physical_errors_divided_by_A_at_real_x':{'current':[out(f*old) for f in factors],'candidate':[out(f*candidate) for f in factors]},
      'strict_improvement':True,'noncollision_claim':False,
    }
    return result

def algebra_checks():
    # These balls verify analytic identities at chosen points; the note
    # proves them exactly. They are not used as a proof of the identities.
    rows=[]
    for p in (acb(A(F(-4,5)),A(F(1,100))),acb(A(F(1,5)),A(F(-1,100)))):
        d,e,_,_=profile(p); d2,e2,_,_=profile(p+2)
        phase=arb.pi()*((p+1)**2/2-A(F(1,8)))
        defect=d+acb(0,1)*e+d2+acb(0,1)*e2-(acb(0,1)*phase).exp()
        check(defect.contains(0),'profile shift identity check')
        rows.append({'p':str(p),'shift_defect':str(defect)})
    # Removable values and first derivatives by formal Taylor division.
    # Both numerator/denominator constant terms are exactly zero by the
    # trigonometric identities at p=1/2, so remove them before division.
    ctx.cap=6; p=acb_series([acb(A(F(1,2))),acb(1)])
    phi=arb.pi()*(p*p/2+A(F(3,8)))
    num=(acb(0,1)*phi).exp()-acb(0,1)*A(2).sqrt()*(arb.pi()*p/2).cos()
    den=2*(arb.pi()*p).cos()
    quotient=acb_series([num[i] for i in range(1,6)])/acb_series([den[i] for i in range(1,6)])
    check(quotient[0].contains(acb(A(F(1,4)),-A(F(1,4)))),'removable value')
    check(quotient[1].contains(acb(A(F(1,4)))),'removable derivative')
    z=acb(1000); t=A(F(21,200)); v=z/2+arb.pi()*t/8
    Wdirect=arb.pi().sqrt()/4*(-arb.pi()*z/8-arb.pi()**2*t/64).exp()/normalizer(z,t)
    check((Wdirect-W_real(z.real,t)).contains(0),'exact W normalization cross-check')
    U=(-acb(0,1)*(v/2*(v/(2*arb.pi())).log()-v/2-arb.pi()/8)).exp()
    mult=(m0(acb(0,1)*v)).exp()*U*(acb(0,1)*arb.pi()/8).exp()
    simple=-arb.pi().sqrt()/8*v.sqrt()*(v+acb(0,1))*(-arb.pi()*v/4).exp()
    check((mult-simple).contains(0),'full multiplier simplification')
    zz=acb(A('1017.8'),A('.2'))
    jump_direct=(mode(zz,t,9)-correction(zz,t,9)+correction(zz,t,8))/normalizer(zz,t)
    check((transition(zz,t,8)-jump_direct).contains(0),'signed transition identity')
    zs=acb_series([z,acb(1)],3)
    check((J(z,t,8)[1]-J(zs,t,8)[0][1]).contains(0),'profile derivative cross-check')
    return {'shift_checks':rows,'removable_C0_plus_half':str(quotient[0]),'removable_C0prime_plus_half':str(quotient[1]),'minus_half':'same value and opposite first derivative by evenness; exact analytic proof in note','normalization_direct_vs_simplified':True,'full_multiplier_identity':True,'signed_transition_identity':True,'profile_derivative_identity':True}

def series_approximation(z,t,retain_correction):
    zz=acb_series([z,acb(1)],3); ss=(1-acb(0,1)*zz)/2
    aser=((mt(ss,t)+mt(1-ss,t))/2).exp()
    def one(n):
        l=A(n).log()
        return sum(((mt(v,t)+t*l*l/4-(v+t*alpha(v)/2)*l).exp() for v in (ss,1-ss)),acb_series([0]))
    fs=sum((one(n) for n in range(1,9)),acb_series([0]))/aser
    if not retain_correction:return fs
    vv=zz/2+arb.pi()*t/8; pp=17-2*(vv/(2*arb.pi())).sqrt(); DD,EE,_,_=profile(pp)
    cc=-arb.pi().sqrt()/4*(-arb.pi()*zz/8-arb.pi()**2*t/64).exp()*vv.sqrt()*(vv*DD-EE)
    return fs-cc/aser

def point_reference(repo,path):
    sys.path.insert(0,str(repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer'))
    from high_height_consumer import validate_setup
    d=json.loads(path.read_text()); validate_setup(d,repo)
    t=A(F(21,200)); z=acb(1000)
    norm=(arb.pi()*1000/8).exp()/A(1000)**A(F(7,4))
    aa=normalizer(z,t).real
    rows=d['setup']['midpoint_jets']; vals=[]
    for j in range(3):
        r=rows[j]; mid=r['midpoint_dyadic']; rad=r['quadrature_radius_dyadic']
        midpoint=A(mid['mantissa'])*A(2)**mid['exponent']; radius=A(rad['mantissa'])*A(2)**rad['exponent']
        # Add the reference source/mode tail bounds printed in its setup.
        mode_tail=d['setup']['uniform_mode_tail_dyadics'][j]
        source_tail=d['setup']['uniform_source_tail_dyadics'][j]
        tails=A(mode_tail['mantissa'])*A(2)**mode_tail['exponent']+A(source_tail['mantissa'])*A(2)**source_tail['exponent']
        vals.append(arb(midpoint,(radius+tails).upper())/(norm*aa))
    s=(1-acb(0,1)*z)/2
    mp=lambda v: alpha(v)*(1+t*alphap(v)/2)
    b=(-acb(0,1)*(mp(s)-mp(1-s))/4).real
    mpp=lambda v: alphap(v)*(1+t*alphap(v)/2)+t*alpha(v)*alphapp(v)/2
    bp=(-(mpp(s)+mpp(1-s))/8).real
    Q=vals[0]; Qp=vals[1]-b*Q; Qpp=vals[2]-2*b*vals[1]+(b*b-bp)*Q
    f=sum((mode(z,t,n) for n in range(1,9)),acb(0))/aa
    fc=corrected(z,t,8)
    fs=series_approximation(z,t,False);fcs=series_approximation(z,t,True)
    check(abs(Q-fc)<A('.23'),'complete reference value inside new bound')
    check(abs(Qp-fcs[1])<A('.46'),'complete reference derivative inside new bound')
    check(abs(Qpp-2*fcs[2])<A('1.82'),'complete reference second derivative inside new bound')
    return {'status':'fresh complete-evaluator consistency check; source/cache pins validated',
      'reference_path':str(path),'reference_sha256':sha(path),'reference_precision_bits':d['bits'],
      'source_pins':d['source_pins'],
      'x':'1000','t':'21/200','Q':out(Q),'Qprime':out(Qp),'Qsecond':out(Qpp),
      'baseline_value_residual':str(Q-f),'candidate_value_residual':str(Q-fc),
      'baseline_first_derivative_residual':str(Qp-fs[1]),'candidate_first_derivative_residual':str(Qp-fcs[1]),
      'baseline_second_derivative_residual':str(Qpp-2*fs[2]),'candidate_second_derivative_residual':str(Qpp-2*fcs[2])}

def evaluation_cost():
    z=acb(1000);t=A(F(21,200));count=256;rows={}
    for keep in (False,True):
        started=time.monotonic()
        for _ in range(count):value=series_approximation(z,t,keep)
        rows['candidate' if keep else 'baseline']={'seconds':time.monotonic()-started,'evaluations':count,'max_real_rounding_radius_orders_0_2':out(max(value[j].real.rad().upper()*math.factorial(j) for j in range(3)))}
    rows['scope']='fixed center only; complete analytic value/first/second derivatives; identical precision, N=8, no caching; no speed milestone'
    return rows

def main():
    p=argparse.ArgumentParser(); p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    p.add_argument('--reference-setup',type=Path)
    a=p.parse_args();ctx.prec=a.bits;started=time.monotonic()
    # Fixed, declared cover; no precision/grid search or post-hoc stopping.
    reference=disk_budget(999,1001,8,4,24,8,False)
    cross=disk_budget(1017,1019,8,8,64,16,True)
    crossing=4*arb.pi()*(81-interval(F(1,100),F(1,5))/16)
    check(crossing>1017 and crossing<1019,'entire a=9 curve inside transition test')
    report={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,
      'llm_assistance':'substantial; parallel same-model derivation and internal checks','precision_bits':a.bits,'python':platform.python_version(),'python_flint':flint.__version__,
      'primary_objective':'strict decrease of uniform complete normalized value/first/second derivative error; no speed or coverage milestone',
      'primary_source':'https://arxiv.org/html/1904.12438v2#S6.SS3','reference_box':reference,'transition_box':cross,'a9_crossing_x':out(crossing),
      'algebra_and_removable_checks':algebra_checks(),'reference_point':point_reference(a.repo,a.reference_setup) if a.reference_setup else None,
      'evaluation_cost':evaluation_cost(),
      'source_sha256':{s:sha(a.repo/s) for s in [
       'papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex',
       'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex',
       'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md',
       'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md',
       'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py']},
      'script_sha256':sha(__file__),'seconds':time.monotonic()-started,
      'limitations':['imported Polymath error theorem is assumed, not re-proved','no collision exclusion or new finite region','no effective improvement to unbounded exterior','no performance gate claimed','error envelope for exact analytic approximants, not whole-cell evaluated jet enclosures'],
      'status':'PASS: outward complete-disk-error comparison, with analytic proof obligations stated in companion note'}
    a.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'reference_eta':reference['eta_candidate'],'reference_ratio':reference['candidate_over_current'],'transition_eta':cross['eta_candidate'],'transition_ratio':cross['candidate_over_current'],'seconds':report['seconds']}))

if __name__=='__main__':main()
