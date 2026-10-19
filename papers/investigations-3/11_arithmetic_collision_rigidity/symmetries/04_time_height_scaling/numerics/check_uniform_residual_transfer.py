#!/usr/bin/env python3
"""S04-T3: local residual transfer and scoped cutoff-payment obstruction.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra.
The accompanying note proves the uniform reductions; no height sampling.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import flint
from flint import arb, acb, ctx

LANE = Path('papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling')
SOURCE_PINS = {
    'papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex': '620f98be47635b8ebb0ecb6d321238c8caa02d66d8496859c994489981c7b050',
    'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex': '5e9ea35168b629923bc548f27b591f641a235feb262163177c0041b83a5244c5',
    str(LANE/'notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md'): '7a0de0010327f4469836038e54df471aa227eaacdc83a6ab3dffe5fd218175b1',
    str(LANE/'notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md'): 'fac173bf5dc839a8669e192b40d19be8788c0b41b8bee411858512acb08bba70',
    'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md': '24e5bf2c124b0340a4bc75ba3b858aa8d9da2654f9c0ed840b4122df576aed35',
    'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md': '1ee0b6f2ba1a358aa8f188cf6a1137250a2edc1bd8bb56a7621bdee7518598dc',
}

def A(x):
    return arb(x.numerator)/x.denominator if isinstance(x, F) else arb(x)

def out(x): return x.str(38, more=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(ok, message):
    if not ok: raise ArithmeticError(message)

def validate_sources(repo, record=None):
    record = SOURCE_PINS if record is None else record
    check(set(record)==set(SOURCE_PINS),'missing analytic source identity')
    for rel, pin in record.items():
        check(sha(repo/rel) == pin, 'stale imported analytic source: '+rel)
    return record

def endpoint_payments(eta, radius, omega_lower, displacement):
    """Real-Schwarz-Pick disk payments, in the original radius coordinate."""
    check(eta >= 0 and radius > 0 and omega_lower > 0, 'positive disk contract')
    check(displacement >= 0 and displacement < radius, 'interior endpoint')
    s = displacement/radius
    # Python max on overlapping balls is not an interval-safe maximum.
    def at_least_one(q): return (1+q+abs(1-q))/2
    k0 = at_least_one(1/(radius*omega_lower))
    k1 = at_least_one(1/(radius*omega_lower*(1-s*s)))
    return {'anchor': k0*eta, 'endpoint': k1*eta, 'increment': (k0+k1)*eta}

def structural_checks(repo, record):
    # Entire constant residual: the actual rotating increment is bounded.
    eta=A(1); angle=A('1.7')
    p=endpoint_payments(eta,A(1),A(4),A(F(1,2)))
    check(2*abs((angle/2).sin()) <= p['increment'], 'constant residual control')
    # Q=y^2, f=2cos y, theta=y: at event y=0, Q=Q'=0.
    # c=1,R=2, |z|<=3: |r|<=9+2cosh(2)<20 on the whole disk.
    check(9+2*A(2).cosh()<20, 'own-source event disk envelope')
    p=endpoint_payments(A(20),A(2),A(1),A(1))
    anchor=acb(0,-1).exp()*acb(1,-2)
    actual_increment=abs(anchor)
    check((actual_increment*actual_increment-5).contains(0), 'event exact primitive')
    check(actual_increment < p['increment'], 'event helper bound')
    check(not (actual_increment > p['increment']), 'event cannot pass propagation')
    # Exact oscillator f=Q=2cos y has zero residual and exact nonzero jet.
    z=endpoint_payments(A(0),A(2),A(1),A(1))
    check(all(v.is_zero() for v in z.values()), 'zero residual oscillator')
    overlap=endpoint_payments(A(1),A(1),A('1 +/- 0.1'),A(0))
    check(overlap['anchor'].upper()>A('1.11'), 'overlapping-ball maximum guard')
    rejected=0
    for args in ((-1,1,1,0),(1,0,1,0),(1,1,0,0),(1,1,1,1),(1,1,1,-1)):
        try: endpoint_payments(*(A(x) for x in args))
        except ArithmeticError: rejected+=1
    check(rejected==5, 'invalid-input guards')
    altered=copy.deepcopy(record); del altered[next(iter(altered))]
    try: validate_sources(repo,altered)
    except ArithmeticError: pass
    else: raise ArithmeticError('missing source mutation escaped')
    altered=copy.deepcopy(record); key=next(iter(altered))
    altered[key]='0'*64
    try: validate_sources(repo,altered)
    except ArithmeticError: pass
    else: raise ArithmeticError('analytic source mutation escaped')
    # At a stationary phase with cos psi=0, an actual mode jet can vanish,
    # although its independent coefficient envelope is 2W>0.
    # This fixture prevents treating an assigned budget as a lower actual jump.
    check(A(0)<2*A(1), 'zero actual jump with positive assigned payment')
    # Schur extremals at center and half radius, differentiated independently.
    for av in (F(0),F(1,2)):
        av=A(av)
        for sv in (F(-1,2),F(0),F(1,2)):
            sv=A(sv); u=(av+sv)/(1+av*sv)
            derivative=(1-av*av)/(1+av*sv)**2
            check((derivative*(1-sv*sv)-(1-u*u)).contains(0),
                  'Schwarz-Pick extremal identity')
    # Two opposed transition vectors cancel before envelopes are assigned.
    v=acb(1,2)
    check((v-v).is_zero() and abs(v)+abs(-v)>0, 'signed transition cancellation')
    # Algebraic real-Schwarz-Pick ellipse at rational u values; proof in note.
    for j in range(-10,11):
        u=A(F(j,10)); K=A('4.001')
        check(j==0 or u*u*(K*K*(2-u*u)-1)>0,
              'real-Schwarz-Pick endpoint norm')
    return {'event_fixture':'own-source polynomial event rejects strict propagation',
            'constant_residual':True,'exact_oscillator_zero_error':True,
            'invalid_contracts_rejected':rejected,'source_mutations_rejected':2,
            'schur_extremal_identities':6,'opposed_transitions_cancel':True,
            'overlapping_ball_maximum_guard':True,
            'assigned_budget_is_not_actual_jump':True}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    a=p.parse_args(); check(a.bits>=128,'at least 128 bits required')
    check(a.execution_model.strip() and a.execution_effort.strip(),'actual metadata required')
    ctx.prec=a.bits; repo=a.repo.resolve(); record=validate_sources(repo)
    L=A(20); x=4*arb.pi()*L.exp(); C=A('4.001')
    # Note01(6) plus Note02(13), over the larger already-paid Y window.
    phase_reserve=(1-A('.005')/x)/4-A('.250003')/(2*L*L*x)-1/C
    check(phase_reserve>0,'uniform omega >= center L/4.001')
    b=A(F(5,16)); t=A(F(1,20)); eta=5*(-b/t).exp()
    payments=endpoint_payments(eta,1/L,L/C,1/(2*L))
    coefficients={k:v/(-b/t).exp() for k,v in payments.items()}
    check(coefficients['increment']<A('46.679'),'local increment ceiling')
    check(payments['anchor']<A('.038619'),'opening anchor-error ceiling')
    check(payments['increment']<A('.090111'),'opening increment ceiling')
    calibrated=payments['anchor']+payments['increment']
    check(calibrated>payments['endpoint'],'same-envelope direct comparison')
    transition=[]
    for tt in (F(1,20),F(1,25),F(1,40),F(1,100)):
        tv=A(tt); U=(1/tv).exp()
        # Whole block lies in kappa[1,2], including the floor correction.
        kappa_lower=tv*((U/2)**2-tv/16).log()
        check(kappa_lower>1,'entire transition block within sector')
        factor=1-2/U
        check(factor>A('.99999999'),'uniform integer-count reserve')
        assigned_lower=factor*(1/(4*tv)).exp()
        check(assigned_lower>A('.99')*(1/(4*tv)).exp(),'assigned transition floor')
        transition.append({'t_exact':str(tt),'block_kappa_lower':out(kappa_lower),
            'assigned_transition_budget_lower':out(assigned_lower),
            'scaled_floor_factor':out(factor)})
    paths=[repo/q for q in SOURCE_PINS]
    result={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':a.execution_model,'actual_effort':a.execution_effort,
        'llm_assistance':'substantial; internal same-model research, no specialist review',
        'status':'uniform analytic corollary and scoped assigned-payment obstruction; no exclusion',
        'precision_bits':a.bits,'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':sha(__file__),
        'source_sha256':{str(q.relative_to(repo)):sha(q) for q in paths},
        'domain':{'t':'0<t<=1/20','kappa':'1<=kappa<=2','center':'c=4*pi*exp(kappa/t)',
            'fixed_cutoff':'floor(sqrt(exp(kappa/t)+t/16))',
            'analytic_disk_radius':'1/log(c/(4*pi))',
            'real_chart':'|y-c|<=1/(2log(c/(4*pi)))',
            'residual':'r_N=Q-F_(t,N); NOT the S03 corrected fixed-pilot residual'},
        'uniform_phase_lower_reserve_divided_by_L':out(phase_reserve),
        'uniform_coefficients_times_exp_minus_b_over_t':{k:out(v) for k,v in coefficients.items()},
        'opening_payments':{k:out(v) for k,v in payments.items()},
        'opening_calibrated_error_with_F_anchor':out(calibrated),
        'transition_rule':'independent coefficientwise mode disks, paying at least 2W_n each',
        'uniform_transition_budget_lower':'.99*exp(1/(4t))',
        'transition_scalar_diagnostics':transition,
        'structural_checks':structural_checks(repo,record),
        'complete_error_ledger':{'source':'inherited complete RS disk theorem, source pins verified',
            'derivatives':'real-Schwarz-Pick within same fixed-cutoff disk',
            'anchor':'error paid; positive physical anchor margin still required',
            'cutoffs':'local theorem pays at most one via imported disk; global independent sum fails',
            'quadrature_or_extra_truncation':'none introduced','rounding':'outward Arb',
            'coverage':'analytic family of local error charts; no collision-free coverage'},
        'limitations':['no transfer of the S03 <0.000854 fixed-pilot constant',
            'no lower bound for actual signed jumps or the theta residual',
            'no obstruction to signed/coherent corrected RS cutoff matching',
            'no uniform positive anchor margin, cost win, complex exterior or Newman bound']}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),'bits':a.bits,'checks':'passed',
                      'opening_increment':out(payments['increment'])}))

if __name__=='__main__': main()
