#!/usr/bin/env python3
"""UAR-06: matched physical margins and complete bounded cost ledger.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Internal LLM validation.
Requires python-flint 0.9.0. No source H data or retained contour quadrature.
"""
from __future__ import annotations
import time
START = time.perf_counter()
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
sys.dont_write_bytecode = True

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE = INV/'symmetries/03_normalized_jet_rotation'
SCRIPT = LANE/'numerics/check_matched_uniform_consumer.py'
NOTE = LANE/'notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md'
CONTROL = LANE/'numerics/UAR06_SOURCE_CONTROLS_20261019.json'
INPUT = LANE/'numerics/UAR05_PAID_ANCHOR_20261019.json'
ACCEPTANCE = LANE/'numerics/UAR06_ACCEPTANCE_INPUT_REVIEW_20261019.json'
U05_SCRIPT = LANE/'numerics/check_paid_uniform_anchor.py'
SCHEMA = 'uar06-matched-complete-consumer-v1'
u = None

def load(repo):
    global u
    spec = importlib.util.spec_from_file_location('uar05', repo/U05_SCRIPT)
    u = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(u)

def sources(repo):
    saved = json.loads((repo/INPUT).read_text())
    u.pins_valid(repo, saved['source_sha256'])
    return sorted(set(map(Path, saved['source_sha256'])) |
                  {SCRIPT, NOTE, CONTROL, INPUT, ACCEPTANCE})

def pins_valid(repo, pins):
    u.check(set(pins) == {str(p) for p in sources(repo)}, 'incomplete source manifest')
    for name, digest in pins.items():
        p = repo/name
        u.check(p.is_file() and not p.is_symlink(), 'missing or linked source')
        u.check(u.sha(p) == digest, 'stale source: '+name)

def evaluate_first(x,t):
    """Complete analytic finite first jet, dropping unconsumed anchor second jet.

    Use only at x=u, t=T when paired with inherited evaluate(xcell,T)
    for the whole-cell rotating derivative. This returns no derivative bound.
    """
    A=u.A;arb=u.arb;acb=u.acb;acb_series=u.acb_series
    pi=arb.pi();ii=acb(0,1);s=(1-ii*acb(x))/2
    aa=u.alpha(s);aap=u.ap(s);mm=u.mt(s,t)
    beta=aa*(1+t*aap/2)
    theta=mm.imag;omega=-beta.real/2;b=beta.imag/2
    u.check(omega<0 and omega.abs_lower()>A('4.999'),'phase orientation')
    cutoff=(x/(4*pi)+t/16).sqrt()
    u.check(cutoff.floor().unique_fmpz()==u.N,'natural cutoff is not frozen N')
    P=acb(0);Px=acb(0)
    for n in range(1,u.N+1):
        ell=A(n).log()
        q=(-s*ell+t*(ell*ell-2*aa*ell)/4).exp()
        lam=ii*ell/2*(1+t*aap/2)
        P+=q;Px+=lam*q
    ee=(ii*theta).exp()
    g=2*(ee*P).real;gx=2*(ee*(ii*omega*P+Px)).real
    zs=acb_series([acb(x),acb(1)],2);ss=(1-ii*zs)/2
    tau=zs/2+pi*t/8;a=(tau/(2*pi)).sqrt();p=2*u.N+1-2*a
    u.check((pi*p[0]).cos().abs_lower()>A('.97'),'profile denominator near removable point')
    phi=pi*(p*p/2+A('.375'));den=2*(pi*p).cos()
    D=phi.cos()/den;B=(phi.sin()-A(2).sqrt()*(pi*p/2).cos())/den
    bracket=tau.sqrt()*(tau*D-B)
    logA=(u.mt(ss,t)+u.mt(1-ss,t))/2
    cp=(-1)**(u.N+1)*pi.sqrt()/4*(-pi*zs/8-pi*pi*t/64-logA).exp()*bracket
    u.check(all(cp[j].imag.contains(0) for j in range(2)),'real symmetry of analytic correction')
    C=cp[0].real;Cx=cp[1].real
    f=g-C;fx=gx-Cx;W=acb(f,-fx/omega)
    Z=(-ii*theta).exp()*W
    u.check(all(v.is_finite() for v in (W,Z)),'nonfinite first jet')
    return {'f':f,'fx':fx,'W':W,'Z':Z,'theta':theta,
        'omega':omega,'b':b,'P':P,'Px':Px,'C':C,'Cx':Cx,
        'profile_p':p[0].real,'profile_cosine':(pi*p[0]).cos().real}



def direct_consumer(anchor, variation, error):
    return u.paid_consumer(anchor, variation, error, u.A(0))

def guards():
    result = u.guards()
    A = u.A
    radius = A(5).sqrt()
    u.check(not (direct_consumer(radius, A(radius.upper()), A(0)) > 0),
            'direct polynomial event accepted')
    u.check(direct_consumer(A(1), A(0), A(0)) > 0, 'direct oscillator rejected')
    for k in range(3):
        row = [A(1), A(0), A(0)]
        row[k] = A(-1)
        u.reject(lambda row=row: direct_consumer(*row))
    u.reject(lambda: direct_consumer(A(1), A('nan'), A(0)))
    # Exact rational ledger: a=2, v=1/2, Eu=Ex=1/10, B=1/5.
    a, v, e, B = map(A, ['2', '.5', '.1', '.2'])
    d = direct_consumer(a, v, e)
    local = u.paid_consumer(a, v, e, 2*e)
    glob = u.paid_consumer(a, v, e, 2*B)
    u.check(d > local and local > glob, 'matched debit order')
    result.update({'direct_polynomial_own_event_rejected': True,
                   'direct_oscillator_accepted': True,
                   'direct_negative_and_nonfinite_inputs_rejected': True,
                   'matched_debit_order_fixture': True,
                   'no_crossing_in_frozen_box': True})
    return result

def acquire(bits):
    u.ctx.prec = bits
    u.ctx.cap = 8
    u.check(bits in (192, 256), 'unsupported precision')
    u.domain_guard(u.T0, u.T1, u.HALF)
    A = u.A
    x0 = 4*u.arb.pi()*A(20).exp()+1
    t = u.interval(A(u.T0), A(u.T1))
    h = A(u.HALF)
    x = u.arb(x0, h.upper())
    xmin, xmax = x0-h, x0+h
    u.check(xmin > 4*u.arb.pi()*(1/A(u.T0)).exp(), 'left sector boundary')
    u.check(xmax < 4*u.arb.pi()*(2/A(u.T1)).exp(), 'right sector boundary')
    L = (x/(4*u.arb.pi())).log()
    cutoffs = (u.arb(x0, (h+1/L).upper())/(4*u.arb.pi())+t/16).sqrt()
    u.check(cutoffs.floor().unique_fmpz() == u.N, 'extremal cutoff')
    before = time.perf_counter()
    anchor = evaluate_first(x0, t)
    anchor_seconds = time.perf_counter()-before
    before = time.perf_counter()
    cell = u.evaluate(x, t)
    cell_seconds = time.perf_counter()-before
    a = anchor['W'].abs_lower()
    variation = h*cell['Zprime'].abs_upper()
    factor = cell['omega'].abs_lower()/(
        1+cell['b'].abs_upper()**2+cell['omega'].abs_upper()**2).sqrt()
    shared = {'bits': bits, 'closed_box': {'t': [str(u.T0),str(u.T1)],
        'x0': '4*pi*exp(20)+1', 'offset': [str(-u.HALF),str(u.HALF)],
        'cutoff': u.N}, 'anchor': u.out(a), 'variation': u.out(variation),
        'return_factor': u.out(factor), 'anchor_f': u.out(anchor['f']),
        'anchor_fx': u.out(anchor['fx']), 'anchor_omega': u.out(anchor['omega']),
        'Zfprime': u.complex_out(cell['Zprime'])}
    # All bounds are computed at frozen exact T and X, not sampled centers.
    return shared, a, variation, factor, x0, xmin, {
        'anchor_first_jet_seconds': anchor_seconds,
        'closed_cell_signed_derivative_seconds': cell_seconds}

def work(bits, method):
    shared,a,v,factor,x0,xmin,timing = acquire(bits)
    start = time.perf_counter()
    margins = {}
    if method == 'direct':
        Ex,_ = u.endpoint_error(xmin,u.A(u.T0))
        margins['direct'] = direct_consumer(a,v,Ex)
        payments = {'endpoint': u.out(Ex)}
    else:
        Ea,_ = u.endpoint_error(x0,u.A(u.T0))
        if method == 'global_transport':
            B = u.A('3.246')*(-u.A(u.F(13,16))/u.A(u.T1)).exp()
            increment=2*B
        else:
            Ex,_ = u.endpoint_error(xmin,u.A(u.T0))
            increment=2*Ex
        margins[method] = u.paid_consumer(a,v,Ea,increment)
        payments = {'anchor':u.out(Ea),'increment':u.out(increment)}
    values = {}
    for name, margin in margins.items():
        physical = (factor*margin).lower()
        energy = (physical**2).lower()
        u.check(margin > u.A('.539') and physical > u.A('.522')
                and energy > u.A('.27'), 'complete physical margin failed')
        values[name] = {'rotating': u.out(margin),
                        'physical_norm_over_A': u.out(physical),
                        'physical_energy_over_A_squared': u.out(energy)}
    timing['complete_errors_and_physical_return_seconds'] = time.perf_counter()-start
    return {'shared': shared, 'payments': payments, 'margins': values}, timing

def validation(repo):
    """Fresh reusable validation, charged equally to each cold consumer."""
    before = time.perf_counter()
    replay = subprocess.run([sys.executable, str(repo/U05_SCRIPT), '--repo',str(repo),
        '--verify',str(repo/INPUT)],check=True,capture_output=True,text=True)
    old_status = json.loads(replay.stdout)
    u.check(old_status == {'status':'verified','bits':[192,256]}, 'UAR05 replay failed')
    with tempfile.TemporaryDirectory(prefix='uar06-controls-') as folder:
        output = Path(folder)/'controls.json'
        subprocess.run([sys.executable,str(repo/INV/'numerics/replay_nonstationary_controls.py'),
            '--repo',str(repo),'--receipts',str(Path(folder)/'receipts'),'--output',str(output),
            '--execution-model','gpt-6.1-sol','--execution-effort','ultra'],
            check=True,capture_output=True,text=True)
        fresh = json.loads(output.read_text())
    saved = json.loads((repo/CONTROL).read_text())
    # Child three/four-square records include a fresh creation timestamp.
    # Compare their full mathematical screen and source hashes, while retaining
    # the new stored-byte identities separately rather than requiring old bytes.
    def mathematical_screen(record):
        screen=json.loads(json.dumps(record['screen']))
        for identity in screen['receipt_identities'].values():
            identity.pop('sha256')
        return screen
    u.check(mathematical_screen(fresh) == mathematical_screen(saved),
            'own-source control mathematics or source identity differs')
    u.check(all(fresh[k] == saved[k] for k in ['script_sha256','checker_sha256',
            'interface_precision_bits','rounding']), 'control producer or precision changed')
    return {'uar05_fresh_replay':old_status,'own_source_event_rejections':5,
            'separate_euler_witness_rejected':True,
            'own_source_screen_reproduced':True,
            'fresh_child_receipt_identities':fresh['screen']['receipt_identities'],
            'child_identity_scope':'Stored-byte hashes of timestamped replays may differ; mathematical screen and producer source hashes must reproduce exactly.',
            'elapsed_seconds':time.perf_counter()-before,
            'reuse':'Validation records and source identities only; no acquired finite sums reused.'}

def compare(direct,glob,local):
    u.check(direct['shared'] == glob['shared'] == local['shared'], 'unmatched acquired data')
    d = direct['margins']['direct']
    for name,method in [('global_transport',glob),('local_transport',local)]:
        for metric in d:
            u.check(u.A(d[metric]) > u.A(method['margins'][name][metric]),
                    'direct dominance not enclosed')
    return {'direct_stronger_than_both_transports_in_all_three_metrics':True,
            'identical_domain_precision_source_and_acquisition':True,
            'new_coverage_relative_to_UAR05_or_direct':False,
            'transport_factor_two_cost_advantage':False,
            'gate':'complete scoped comparison loss; stop this consumer configuration'}

def cost_ledger():
    return {'each_production_method': {'closed_domain_cells':1,
        'anchor_first_jet_images':1,'closed_cell_signed_derivative_images':1,
        'finite_mode_evaluations':2*u.N,'log_and_complex_exp_pairs':2*u.N,
        'finite_moment_accumulations':5*u.N,
        'analytic_profile_series_lengths':[2,3],
        'H_source_values':0,'retained_contour_quadratures':0,
        'interior_cutoff_changes':0,'time_interpolation_steps':0,
        'physical_normalizer_return':1},
        'direct_extra_payments':'One complete endpoint residual Ex.',
        'transport_extra_payments':{'global':'One complete endpoint Ea plus rebased 2B.','local':'Both complete endpoints Ea and Ex, local increment 2Ex.'},
        'cold':'Fresh interpreter, imports, pin/guard checks, two images, all debits/return; add fresh common validation preparation.',
        'reusable_preparation':'Only source identities and completed control/acceptance validation; separately timed. Mathematical proofs not assigned invented stopwatch costs.',
        'dominance':'The two acquisition graphs are identical. Direct pays one endpoint envelope of the same formula as Ea, omitting the global B evaluation or the local extra endpoint; any faithful optimization of that shared graph is available to both.',
        'timing_scope':'Finite fresh-process observations; OS/library caches not flushed; no universal implementation optimum or speed law.'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--output',type=Path)
    g.add_argument('--verify',type=Path)
    g.add_argument('--worker',choices=['direct','global_transport','local_transport'])
    p.add_argument('--bits',type=int,choices=[192,256],default=192)
    p.add_argument('--execution-model')
    p.add_argument('--execution-effort')
    args = p.parse_args()
    repo = args.repo.resolve()
    load(repo)
    u.ctx.prec = 192
    exact = guards()
    pins = {str(s):u.sha(repo/s) for s in sources(repo)}
    pins_valid(repo,pins)
    u.reject(lambda:pins_valid(repo,{}))
    stale = dict(pins); stale[str(SCRIPT)]='0'*64
    u.reject(lambda:pins_valid(repo,stale))
    if args.worker:
        data,timing = work(args.bits,args.worker)
        timing['worker_including_imports_pins_guards_seconds']=time.perf_counter()-START
        print(json.dumps({'data':data,'timing':timing}));return
    if args.verify:
        saved = json.loads(args.verify.read_text())
        u.check(saved['schema'] == SCHEMA,'wrong schema')
        u.check([row['bits'] for row in saved['runs']] == [192,256], 'incomplete precision validation')
        u.check(saved['cost_ledger'] == cost_ledger(), 'cost ledger changed')
        pins_valid(repo,saved['source_sha256'])
        u.check(saved['exact_guards'] == exact,'guards changed')
        for row in saved['runs']:
            d,_ = work(row['bits'],'direct')
            g,_ = work(row['bits'],'global_transport')
            l,_ = work(row['bits'],'local_transport')
            u.check(d==row['direct'] and g==row['global_transport'] and l==row['local_transport'],'fresh physical replay differs')
            u.check(compare(d,g,l)==row['comparison'],'gate changed')
        result = validation(repo)
        print(json.dumps({'status':'verified','bits':[r['bits'] for r in saved['runs']],
            'fresh_source_controls':result['own_source_screen_reproduced']}));return
    u.check(bool(args.execution_model) and bool(args.execution_effort),'actual provenance required')
    preparation = validation(repo)
    rows=[]
    for bits, order in ((192,['direct','global_transport','local_transport']),(256,['local_transport','global_transport','direct'])):
        acquired={};observed={}
        for method in order:
            before=time.perf_counter()
            child=subprocess.run([sys.executable,str(repo/SCRIPT),'--repo',str(repo),
                '--worker',method,'--bits',str(bits)],check=True,capture_output=True,text=True)
            elapsed=time.perf_counter()-before
            result=json.loads(child.stdout)
            acquired[method]=result['data']
            observed[method]={**result['timing'],
                'fresh_process_wall_seconds':elapsed,
                'cold_with_validation_preparation_seconds':elapsed+preparation['elapsed_seconds']}
        comparison=compare(acquired['direct'],acquired['global_transport'],acquired['local_transport'])
        rows.append({'bits':bits,**acquired,'comparison':comparison,'execution_order':order,
                     'observed_costs':observed})
    record={'schema':SCHEMA,'date':'2026-10-19','timezone':'America/New_York',
        'prepared_for':'Edward Baker','actual_model':args.execution_model,
        'actual_effort':args.execution_effort,'llm_assistance':'substantial; delegated internal reviews',
        'python':platform.python_version(),'python_flint':u.flint.__version__,
        'rounding':'outward Arb/acb; exact rational closed box; full cutoff',
        'source_sha256':pins,'exact_guards':exact,
        'missing_and_stale_source_guards_passed':True,'validation_preparation':preparation,
        'cost_ledger':cost_ledger(),'runs':rows,
        'utc':datetime.now(timezone.utc).isoformat(),
        'limits':['Exact UAR05 box only; no sector exhaustion, real bridge, complex exterior or Newman bound.',
            'Fresh same-producer replay and delegated internal review are not specialist or full implementation-independent validation.',
            'Direct is optimized within the shared acquisition graph; no global optimality claim.',
            'Both precisions validate; one production precision is charged per row.'],
        'outcome':'UAR06 complete scoped consumer loss; UAR-E1/G1 remain conditional.'}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'written','output':str(args.output),'bits':[192,256],
                      'gate':'complete scoped comparison loss'}))

if __name__=='__main__':
    main()
