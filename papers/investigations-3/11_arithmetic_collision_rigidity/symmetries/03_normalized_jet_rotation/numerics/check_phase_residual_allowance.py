#!/usr/bin/env python3
"""S03-T2: phase-aware analytic-only residual allowance on the fixed B box.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Internal verification.
No complete-source Taylor cache or residual coefficients are consumed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import flint
from flint import arb, acb, ctx

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE = INV / 'symmetries/03_normalized_jet_rotation'

def A(x): return arb(x.numerator) / x.denominator if isinstance(x, F) else arb(x)
def out(x): return x.str(38, more=True)
def check(ok, message):
    if not ok: raise ArithmeticError(message)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def box(a, b):
    a, b = A(a), A(b)
    return arb((a+b)/2, ((b-a)/2).upper())
def load(p, name):
    s = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m

def allowance(eta, radius, wlo, whi, wpmax, width, split=F(23, 50)):
    """Complete bound from real analytic disk data and a monotone real phase.

    Inputs are certified scalar bounds, not interval estimates of free values.
    The fixed split is in absolute phase distance, not physical distance.
    """
    check(eta >= 0 and radius > 0 and wlo > 0 and whi >= wlo and
          wpmax >= 0 and width >= 0, 'invalid analytic allowance inputs')
    split = A(split)
    check(split > 0 and split < arb.pi()/2, 'invalid phase split')
    K = max(A(1), (1/(radius*wlo)).upper())
    D = 1 + 2/(radius**2*wlo**2) + wpmax/(radius*wlo**3)
    independent = (2*eta*K).upper()
    phase_max = (whi*width).upper()
    near = (eta*D*min(split, phase_max)).upper()
    far = A(0)
    if phase_max > split:
        # Otherwise |cos(delta)| may return to 1; preserve the valid old bound.
        if phase_max < arb.pi()-split:
            far = (eta*(2*(1+K*K+(K*K-1)*split.cos())).sqrt()).upper()
        else:
            far = independent
    combined = min(independent, max(near, far))
    return {'K': K, 'D': D, 'split': split, 'phase_max': phase_max,
            'near': near, 'far': far, 'independent': independent,
            'combined': combined}

def mechanism_controls():
    """Actual helper, its class assumptions, and collision controls."""
    # A polynomial event has its OWN disk allowance, not theta's allowance.
    # On disks radius .5 at centers [-1,0], |z^2-2cos(z)| < 5.
    eta_event = A(5)
    check(A(F(3,2))**2 + 2*A(F(1,2)).cosh() < eta_event,
          'polynomial own disk allowance')
    event = allowance(eta_event, A(F(1,2)), A(1), A(1), A(0), A(1))
    # At t=t_c, H=x^2, f=2cos(x), A=1, theta=x; I_r(0) has modulus sqrt(5).
    ii = acb(0,1)
    Z = lambda x: (-ii*x).exp()*acb(x*x, -2*x)
    actual = abs(ii*(Z(A(0))-Z(A(-1))))
    check((actual-A(5).sqrt()).contains(0), 'polynomial endpoint identity')
    check((actual-abs(Z(A(-1)))).contains(0), 'polynomial exact anchor equality')
    check(event['combined'] > actual, 'polynomial error allowance underpays event')
    check(not (abs(Z(A(-1))).lower() > event['combined']),
          'strict helper propagation accepted the event')
    # Pure oscillators have zero complete increment; a bound need not be sharp.
    for q in (F(0), F(1,3), F(1)):
        x = A(q); osc = 2*x.cos(); oscxx = -osc
        check((osc+oscxx).contains(0), 'oscillator defect')
    # The phase-dependent ellipse bound must retain |cos(delta)| after pi/2.
    K=A(2); delta=arb.pi()*A(F(5,6))
    correct=(2*(1+K*K+(K*K-1)*abs(delta.cos()))).sqrt()
    wrong=(2*(1+K*K+(K*K-1)*delta.cos())).sqrt()
    # Two opposite points on the major axes of rotated equal ellipses.
    witness=2*K*(delta/2).sin()
    check(witness > wrong and correct >= witness,
          'missing absolute cosine mutation not detected')
    # Long intervals must fall back rather than extrapolate the short phase bound.
    long=allowance(A(1), A(F(1,2)), A(1), A(1), A(0), A(4))
    check(long['combined'] == long['independent'], 'long-phase fallback')
    invalid=0
    for args in ((-1,F(1,2),1,1,0,2),(1,0,1,1,0,2),
                 (1,F(1,2),0,1,0,2),(1,F(1,2),2,1,0,2),
                 (1,F(1,2),1,1,-1,2),(1,F(1,2),1,1,0,-1)):
        try: allowance(*(A(v) for v in args))
        except ArithmeticError: invalid+=1
    check(invalid==6, 'invalid input guards')
    zero=allowance(A(0),A(F(1,2)),A(1),A(1),A(0),A(1))
    check(zero['combined']==0, 'zero error')
    return {'polynomial_event': {'source':'H=x^2-2(t-t_c), f=2cos(x), A=1, theta=x',
            'anchor':-1,'event':0,'own_complete_disk_allowance':'5',
            'complete_increment_modulus':out(actual),
            'helper_allowance':out(event['combined']),
            'strict_anchor_preservation_fails_by_equality':True},
            'oscillator_identity_checks':3,'invalid_inputs_rejected':invalid,
            'missing_absolute_cosine_mutation_detected':True,
            'long_phase_falls_back':True,'zero_error_exact':True}

def run(repo, bits):
    ctx.prec=bits;ctx.cap=8
    path=repo/INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py'
    t2=load(path, 's03_t2_phase_'+str(bits));ev=t2.ClosedJetEvaluator(repo,bits)
    eta=ev.eta['full'];wlo=A(100);whi=A(0);wpmax=A(0)
    for it in range(32):
        t=box(F(1,100)+F(19,100)*it/32,F(1,100)+F(19,100)*(it+1)/32)
        for ix in range(128):
            x=box(F(999)+F(2)*ix/128,F(999)+F(2)*(ix+1)/128)
            _,w,wp,_,_,_=ev.phase(x,t)
            check(w<0, 'phase orientation')
            wlo=min(wlo,abs(w).lower());whi=max(whi,abs(w).upper())
            wpmax=max(wpmax,abs(wp).upper())
    a=allowance(eta,A(F(1,2)),wlo,whi,wpmax,A(2))
    check(a['combined'] < A('.8123'), 'fixed analytic-only allowance goal')
    check(a['combined'] < a['independent'], 'same-information strict gain')
    check(a['phase_max'] < arb.pi()-a['split'], 'far phase interval admissibility')
    c=A(F(1,5))
    check(c<eta and whi<arb.pi()/2, 'constant residual class witness')
    floor=(2*c*wlo.sin()).lower()
    check(floor>A('.355'), 'envelope-only class floor')
    return {'bits':bits,'closed_cover':{'t_cells':32,'x_cells':128},
            'full_complete_disk_eta_upper':out(eta),
            'phase_bounds':{'absolute_omega_lower':out(wlo),'absolute_omega_upper':out(whi),
                            'absolute_omega_x_upper':out(wpmax)},
            'allowance':{k:out(v) for k,v in a.items()},
            'allowance_ratio_upper':out((a['combined']/a['independent']).upper()),
            'allowance_decrease_lower':out((1-a['combined']/a['independent']).lower()),
            'envelope_class_floor':{'residual':'r(t,z)=1/5',
                'full_endpoint_increment_lower_uniform_in_t':out(floor),
                'scope':'Holomorphic real-symmetric uniform disk-envelope class only; not the exact theta source or prescribed heat forcing.'},
            'controls':mechanism_controls()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();repo=args.repo.resolve()
    paths=[INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py',
           INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py',
           INV/'symmetries/02_cutoff_reflection/numerics/compare_correction_representations.py',
           INV/'symmetries/02_cutoff_reflection/numerics/S02_MATCHED_CORRECTION_20261019.json',
           LANE/'notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md']
    result={'date':'2026-10-19','prepared_for':'Edward Baker',
            'actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'llm_assistance':'substantial; same-model derivation and separate internal audit',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'script_sha256':sha(__file__),'source_sha256':{str(v):sha(repo/v) for v in paths},
            'domain':'B=[1/100,1/5] x [999,1001], anchor x=999, full analytic cutoff N=8',
            'information_class':'Imported complete radius-1/2 Q-disk envelope and explicit phase only; no complete-source jets.',
            'status':'Complete analytic-only residual allowance; no new arithmetic cancellation estimate or coverage.',
            'error_ledger':'The imported complete eta pays all source/arithmetic residuals; no new source truncation or quadrature; closed-cell outward phase bounds and scalar rounding paid.',
            'retained_comparators':{'source_informed_independent_endpoints':'<0.002011747',
                                    'source_informed_correlated_prefix':'<0.000266448'},
            'runs':[run(repo,b) for b in args.bits]}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'bounds':[v['allowance']['combined'] for v in result['runs']]}))

if __name__=='__main__': main()
