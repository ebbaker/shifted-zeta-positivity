#!/usr/bin/env python3
"""Closed UAR-05 paid anchor and bounded physical separation.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual execution provenance is required. Authoring gpt-6.1-sol, effort ultra.
The two finite sums enclose a whole closed box, not a point sample or H fit.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
sys.dont_write_bytecode=True
import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
SYM=INV/'symmetries'
LANE=SYM/'03_normalized_jet_rotation'
NOTE=LANE/'notes/11_PAID_ANCHOR_AND_BOUNDED_PHYSICAL_SEPARATION_20261019.md'
SCRIPT=LANE/'numerics/check_paid_uniform_anchor.py'
CONTROL=LANE/'numerics/UAR05_SOURCE_CONTROLS_20261019.json'
SOURCES=[NOTE,SCRIPT,CONTROL,
    SYM/'notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md',
    SYM/'numerics/UAR01_CONTRACT_CHECK_20261019.json',
    LANE/'notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md',
    LANE/'notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md',
    LANE/'notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md',
    LANE/'numerics/UAR04_UNIFORM_SIGNED_INCREMENT_20261019.json',
    LANE/'numerics/check_uniform_signed_increment.py',
    INV/'numerics/replay_nonstationary_controls.py',
    Path('result-summaries/12_collision_controls_and_screening.md')]
T0=F(1,20)-F(1,10**14)
T1=F(1,20)
HALF=F(1,100)
N=22026
SCHEMA='uar05-paid-anchor-bounded-physical-separation-v1'

def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v):return v.str(38,more=True)
def complex_out(v):return {'real':out(v.real),'imag':out(v.imag)}
def check(ok,msg):
    if not ok:raise ArithmeticError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def interval(lo,hi):return arb((lo+hi)/2,((hi-lo)/2).upper())
def reject(call):
    try:call()
    except ArithmeticError:return
    raise ArithmeticError('invalid fixture accepted')
def domain_guard(t0,t1,h):
    check(all(isinstance(v,F) for v in (t0,t1,h)),'exact rational domain required')
    check((t0,t1,h)==(T0,T1,HALF),'outside frozen closed feasibility contract')
def pins_valid(repo,pins):
    check(set(pins)=={str(p) for p in SOURCES},'missing or extra source pins')
    for name,digest in pins.items():
        p=repo/name
        check(p.is_file() and not p.is_symlink(),'missing or linked source: '+name)
        check(sha(p)==digest,'stale source: '+name)
def paid_consumer(anchor,variation,anchor_error,increment):
    """Source-neutral first-jet reverse triangle acceptance, all debits paid."""
    check(all(v.is_finite() for v in (anchor,variation,anchor_error,increment)),'nonfinite consumer input')
    check(all(v>=0 for v in (anchor,variation,anchor_error,increment)),'negative consumer debit')
    return (anchor.lower()-variation.upper()-anchor_error.upper()-increment.upper()).lower()
def guards():
    domain_guard(T0,T1,HALF)
    reject(lambda:domain_guard(T0,T1,F(1,10)))
    reject(lambda:domain_guard(F(0),T1,HALF))
    reject(lambda:domain_guard(T0,.05,HALF))
    # Actual polynomial q=x^2, theta=-x, omega=-1: at anchor -1,
    # |Z_q|=sqrt(5), and at its own event 0 both q and q' vanish.
    # The exact endpoint variation has precisely the anchor radius.
    radius=A(5).sqrt()
    paid=paid_consumer(radius,A(radius.upper()),A(0),A(0))
    omitted=paid_consumer(radius,A(0),A(0),A(0))
    check(not(paid>0),'polynomial own event must reject after variation')
    check(omitted>0,'omitted variation mutation should expose false acceptance')
    # q=cos(x), theta=-x, omega=-1 gives Z_q identically one. The
    # source-neutral consumer must retain this nonvanishing success case.
    oscillator=paid_consumer(A(1),A(0),A(0),A(0))
    check(oscillator>0,'nonzero oscillator should pass the paid consumer')
    reject(lambda:paid_consumer(A(1),A(-1),A(0),A(0)))
    d=A(F(1,8))
    check(not(paid_consumer(d,A(0),d,A(0))>0),'anchor uncertainty must be paid')
    check(not(paid_consumer(d,A(0),A(0),d)>0),'residual increment must be paid')
    check(paid_consumer(d,A(0),A(0),A(0))>0,'omitted-error mutations should expose false acceptance')
    reject(lambda:paid_consumer(A(-1),A(0),A(0),A(0)))
    reject(lambda:paid_consumer(A(1),A(0),A(-1),A(0)))
    reject(lambda:paid_consumer(A(1),A(0),A(0),A(-1)))
    reject(lambda:paid_consumer(A('nan'),A(0),A(0),A(0)))
    return {'frozen_closed_contract':True,'invalid_domain_fixtures_rejected':3,
        'polynomial_own_event_rejected':True,
        'nonzero_oscillator_accepted':True,
        'omitted_variation_mutation_false_acceptance_detected':True,
        'omitted_anchor_uncertainty_mutation_false_acceptance_detected':True,
        'omitted_residual_increment_mutation_false_acceptance_detected':True,
        'negative_debit_rejected':True,
        'all_four_negative_input_positions_rejected':True,
        'nonfinite_input_rejected':True,
        'ordinary_integral_rebase_factor':'2',
        'same_N_overlaps_by_identical_definition':True}

def m0(s):
    pi=arb.pi()
    return s.log()+(s-1).log()-s*pi.log()/2+(2*pi).log()/2-A(16).log()+(s/2-A('.5'))*(s/2).log()-s/2
def alpha(s):return 1/(2*s)+1/(s-1)+(s/(2*arb.pi())).log()/2
def ap(s):return -1/(2*s*s)-1/(s-1)**2+1/(2*s)
def app(s):return 1/s**3+2/(s-1)**3-1/(2*s*s)
def mt(s,t):return m0(s)+t*alpha(s)**2/4

def evaluate(x,t):
    """All N modes including near-cutoff heat weights, frozen t and N in x jets."""
    pi=arb.pi();ii=acb(0,1);s=(1-ii*acb(x))/2
    aa=alpha(s);aap=ap(s);aapp=app(s);mm=mt(s,t)
    beta=aa*(1+t*aap/2)
    theta=mm.imag;omega=-beta.real/2;b=beta.imag/2
    mpp=aap*(1+t*aap/2)+t*aa*aapp/2
    omega_x=-mpp.imag/4
    check(omega<0 and omega.abs_lower()>A('4.999'),'phase orientation')
    cutoff=(x/(4*pi)+t/16).sqrt()
    check(cutoff.floor().unique_fmpz()==N,'natural cutoff is not frozen N')
    P=acb(0);Px=acb(0);Pxx=acb(0)
    for n in range(1,N+1):
        ell=A(n).log()
        q=(-s*ell+t*(ell*ell-2*aa*ell)/4).exp()
        lam=ii*ell/2*(1+t*aap/2)
        P+=q;Px+=lam*q;Pxx+=(lam*lam+t*ell*aapp/8)*q
    ee=(ii*theta).exp();ee2=(-2*ii*theta).exp()
    g=2*(ee*P).real;gx=2*(ee*(ii*omega*P+Px)).real
    # Analytic C=Chat/A in one second-order power series; exact A derivatives
    # and the fixed-N removable profile continuation are retained. This box
    # avoids the removable points with a checked positive cosine reserve.
    zs=acb_series([acb(x),acb(1)],3);ss=(1-ii*zs)/2
    tau=zs/2+pi*t/8;a=(tau/(2*pi)).sqrt();p=2*N+1-2*a
    check((pi*p[0]).cos().abs_lower()>A('.97'),'profile denominator near removable point')
    phi=pi*(p*p/2+A('.375'));den=2*(pi*p).cos()
    D=phi.cos()/den;B=(phi.sin()-A(2).sqrt()*(pi*p/2).cos())/den
    bracket=tau.sqrt()*(tau*D-B)
    logA=(mt(ss,t)+mt(1-ss,t))/2
    cp=(-1)**(N+1)*pi.sqrt()/4*(-pi*zs/8-pi*pi*t/64-logA).exp()*bracket
    check(all(cp[j].imag.contains(0) for j in range(3)),'real symmetry of analytic correction')
    C=cp[0].real;Cx=cp[1].real;Cxx=2*cp[2].real
    f=g-C;fx=gx-Cx;W=acb(f,-fx/omega)
    Z=(-ii*theta).exp()*W
    # Preserve the signed finite relation before the final norm.
    Zg=2*P-ii/omega*(Px+ee2*Px.conjugate())
    Zc=(-ii*theta).exp()*acb(C,-Cx/omega)
    check((Z-(Zg-Zc)).contains(0),'equivalent rotating endpoint forms disagree')
    Zgp=2*Px-2*ee2*Px.conjugate()-ii/omega*(Pxx+ee2*Pxx.conjugate())+ii*omega_x/(omega*omega)*(Px+ee2*Px.conjugate())
    Zcp=(-ii*theta).exp()*(-ii*omega*C-ii*Cxx/omega+ii*omega_x*Cx/(omega*omega))
    Zfp=Zgp-Zcp
    check(all(v.is_finite() for v in (W,Z,Zfp)),'nonfinite first jet')
    return {'f':f,'fx':fx,'W':W,'Z':Z,'Zprime':Zfp,'theta':theta,
        'omega':omega,'omega_x':omega_x,'b':b,'P':P,'Px':Px,'Pxx':Pxx,
        'C':C,'Cx':Cx,'Cxx':Cxx,'profile_p':p[0].real,'profile_cosine':(pi*p[0]).cos().real}

def endpoint_error(x,t):
    L=(x/(4*arb.pi())).log()
    S=(-3*L/4-t*L*L/16).exp()
    delta=160*(L/4-t*L*L/16).exp()/x**2
    epsilon=1000*(-A('4.24')*L-t*L*L/16).exp()
    return A('1.53')*S+delta+9*epsilon,{'S':out(S),'Delta_AB':out(delta),'edge_rotating_error':out(9*epsilon)}

def run(bits):
    ctx.prec=bits;ctx.cap=8
    domain_guard(T0,T1,HALF)
    pi=arb.pi();base=4*pi*A(20).exp();x0=base+1
    t=interval(A(T0),A(T1));h=A(HALF);x=arb(x0,h.upper())
    xmin=x0-h;xmax=x0+h
    lower_boundary=4*pi*(1/A(T0)).exp()
    upper_boundary=4*pi*(2/A(T1)).exp()
    check(xmin>lower_boundary,'box leaves sector at lower height')
    check(xmax<upper_boundary,'box leaves sector at upper height')
    L=(x/(4*pi)).log();R=1/L
    all_cutoffs=((arb(x0,(h+R).upper()))/(4*pi)+t/16).sqrt()
    check(all_cutoffs.floor().unique_fmpz()==N,'extremal chart cutoffs disagree')
    a=evaluate(x0,t);v=evaluate(x,t)
    anchor=a['W'].abs_lower();D=v['Zprime'].abs_upper();debit=h*D
    Ea,ea_parts=endpoint_error(x0,A(T0))
    Ex,ex_parts=endpoint_error(xmin,A(T0))
    B=A('3.246')*(-A(F(13,16))/A(T1)).exp()
    # The theorem is applied only on the exact rational T and symbolic X;
    # outward parameter balls can extend beyond them by rounding slivers.
    anchor_Q=paid_consumer(anchor,A(0),Ea,A(0))
    calibrated=paid_consumer(anchor,debit,Ea,2*B)
    local=paid_consumer(anchor,debit,Ea,2*Ex)
    direct=paid_consumer(anchor,debit,Ex,A(0))
    # Physical map (Q,-Qx/omega) -> (H/A,Hx/A) has determinant -omega
    # and Frobenius norm sqrt(1+b^2+omega^2). Account for A_x/A=b.
    return_factor=v['omega'].abs_lower()/(1+v['b'].abs_upper()**2+v['omega'].abs_upper()**2).sqrt()
    physical=return_factor*calibrated
    flags={'anchor_first_jet_above_1_5441778':bool(anchor>A('1.5441778')),
        'Zf_derivative_below_100_51':bool(D<A('100.51')),
        'variation_below_1_0051':bool(debit<A('1.0051')),
        'paid_anchor_above_1_5441776':bool(anchor_Q>A('1.5441776')),
        'complete_calibrated_margin_above_0_539':bool(calibrated>A('.539')),
        'local_endpoint_margin_positive':bool(local>0),
        'same_information_direct_margin_stronger':bool(direct>calibrated),
        'same_information_direct_stronger_than_local_return':bool(direct>local),
        'anchor_error_below_1_341e_minus7':bool(Ea<A('1.341e-7')),
        'global_calibrated_error_below_7_031e_minus7':bool(Ea+2*B<A('7.031e-7')),
        'local_calibrated_error_below_4_023e_minus7':bool(Ea+2*Ex<A('4.023e-7')),
        'physical_det_over_frobenius_above_0_97':bool(return_factor>A('.97')),
        'physical_Euclidean_margin_above_0_522':bool(physical>A('.522')),
        'profile_denominator_reserve':bool(v['profile_cosine'].abs_lower()>A('.97')),
        'all_extremal_cutoffs_equal_22026':True,
        'all_errors_paid_before_strict_test':True}
    check(all(flags.values()),'paid inequality failed: '+str([k for k,v in flags.items() if not v]))
    return {'bits':bits,'all_checks_passed':True,'checks':flags,
        'closed_box':{'t':[str(T0),str(T1)],'x0':'4*pi*exp(20)+1',
            'x_offset':[str(-HALF),str(HALF)],'x0_enclosure':out(x0),
            'sector_lower_height_reserve':out(xmin-lower_boundary),
            'sector_upper_height_reserve':out(upper_boundary-xmax),
            'fixed_and_extremal_cutoffs':N,'profile_p':out(v['profile_p']),
            'profile_cosine':out(v['profile_cosine'])},
        'anchor':{'f':out(a['f']),'fx':out(a['fx']),'omega':out(a['omega']),
            'Zf':complex_out(a['Z']),'first_jet_radius_lower':out(anchor),
            'physical_Q_radius_lower':out(anchor_Q)},
        'closed_box_approximant':{'Zfprime':complex_out(v['Zprime']),
            'Zfprime_modulus_upper':out(D),'signed_variation_upper':out(debit),
            'omega':out(v['omega']),'omega_x':out(v['omega_x']),'A_log_derivative':out(v['b']),
            'correction':[out(v[k]) for k in ('C','Cx','Cxx')]},
        'complete_allowances':{'anchor_rotating_residual':out(Ea),
            'anchor_breakdown':ea_parts,'closed_box_rotating_residual':out(Ex),
            'box_breakdown':ex_parts,'primary_global_prefix':out(B),
            'primary_rebased_increment':out(2*B),'local_two_endpoint_increment':out(2*Ex),
            'calibrated_total_error':out(Ea+2*B),'same_information_direct_error':out(Ex)},
        'margins':{'calibrated_primary_rotating':out(calibrated),
            'calibrated_local_endpoint_rotating':out(local),
            'same_information_direct_rotating':out(direct),
            'physical_det_over_frobenius_lower':out(return_factor),
            'physical_Euclidean_over_A':out(physical)},
        'acquisition':{'H_values':0,'retained_contour_quadratures':0,
            'finite_sum_evaluations':2,'terms_per_sum':N,'total_mode_terms':2*N,
            'domain_cells':1,'time_parameter_is_a_closed_interval':True},
        'scope':'One frozen closed sector box; not all J_t or a coverage campaign.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--output',type=Path);g.add_argument('--verify',type=Path)
    p.add_argument('--bits',nargs='+',type=int,default=[192,256]);p.add_argument('--execution-model');p.add_argument('--execution-effort')
    args=p.parse_args();repo=args.repo.resolve();ctx.prec=192;exact=guards()
    if args.verify:
        saved=json.loads(args.verify.read_text());check(saved['schema']==SCHEMA,'wrong schema')
        pins_valid(repo,saved['source_sha256']);check(saved['exact_guards']==exact,'exact guards differ')
        fresh=[run(row['bits']) for row in saved['runs']]
        check(fresh==saved['runs'],'outward replay differs')
        print(json.dumps({'status':'verified','bits':[r['bits'] for r in fresh]}));return
    check(bool(args.execution_model) and bool(args.execution_effort),'actual execution provenance required')
    check(all(b in (192,256) for b in args.bits),'precision must be 192 or 256')
    pins={str(v):sha(repo/v) for v in SOURCES};pins_valid(repo,pins)
    reject(lambda:pins_valid(repo,{}));stale=dict(pins);stale[str(NOTE)]='0'*64
    reject(lambda:pins_valid(repo,stale));reject(lambda:pins_valid(repo/'absent_uar05_fixture',pins))
    start=time.monotonic();runs=[run(b) for b in args.bits];elapsed=time.monotonic()-start
    record={'schema':SCHEMA,'date':'2026-10-19','timezone':'America/New_York',
        'prepared_for':'Edward Baker','actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; separate same-model internal audit',
        'scope':'paid_anchor_and_strict_physical_first_jet_separation_on_one_closed_sector_box',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'rounding':'outward Arb/acb closed interval arithmetic and formal analytic series',
        'source_sha256':pins,'exact_guards':exact,
        'source_guards':{'missing_pins_rejected':True,'stale_pin_rejected':True,'missing_files_rejected':True},
        'runs':runs,'execution_observation':{'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':elapsed},
        'limitations':['The declared closed box only; not all heights, t=0, real bridge or complex exterior.',
            'No H calibration or inferred edge values; no total-cost advantage over direct certification.',
            'The same-information direct endpoint error is strictly smaller on this box.',
            'Same-model/checker replay is not independent specialist or implementation validation.']}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'written','output':str(args.output),'bits':args.bits}))
if __name__=='__main__':main()
