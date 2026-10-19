#!/usr/bin/env python3
"""Signed endpoint estimate and exactly completed transverse current.

Prepared for Edward Baker with substantial LLM assistance, 18 October 2026.
Actual authoring model gpt-6.1-sol, effort ultra. Internal verification.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import comb, factorial
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import flint
from flint import arb, ctx


def A(v):
    return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)


def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}


def scale(p,c,shift=0):
    return {k+shift:c*v for k,v in p.items() if c*v}


def deriv(p): return {k-1:k*v for k,v in p.items() if k}


def poly(p,x):
    return sum((A(v)*x**k for k,v in p.items()),arb(0))


def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def s(v): return v.str(40,more=True)


def endpoint_and_moments(bits):
    ctx.prec=bits
    T=F(1,5);pi=arb.pi();m=9
    pp=[{1:-3,2:2}]
    heat=[{0:F(1)}]
    for r in range(6):
        pp.append(add(scale(deriv(pp[-1]),4,1),pp[-1],scale(pp[-1],-4,1)))
        heat.append(add(deriv(heat[-1]),scale(heat[-1],2*T,1)))
    ends=[];tail_ends=[]
    for p in pp:
        finite=sum((pi*n*n*poly(p,pi*n*n)*(-pi*n*n).exp() for n in range(1,m)),arb(0))
        tail=arb(0)
        for ell,coefficient in p.items():
            ratio=(arb(m+1)/m)**(2*ell+2)*(-pi*(2*m+1)).exp()
            assert ratio<1
            tail+=pi*abs(coefficient)*(pi*m*m)**ell*m*m*(-pi*m*m).exp()/(1-ratio)
        ends.append(finite+arb(0,tail.upper()));tail_ends.append(tail.upper())

    # Gaussian envelope for n=1, linear envelope for n>=2.
    def gaussian_moments(a,b,J):
        i0=pi.sqrt()/(2*b.sqrt())*(a*a/(4*b)).exp()*(1+(a/(2*b.sqrt())).erf())
        values=[i0]
        if J: values.append((1+a*i0)/(2*b))
        for j in range(1,J): values.append((j*values[j-1]+a*values[j])/(2*b))
        assert all(v>0 for v in values)
        return values

    norms={};tail_norms={}
    for order in (4,6):
        total=arb(0);tail_total=arb(0)
        for k in range(order+1):
            for j,hc in heat[order-k].items():
                for ell,pc in pp[k].items():
                    coefficient=comb(order,k)*A(hc)*abs(pc)*pi
                    for n in range(1,m):
                        lam=pi*n*n
                        assert 8*lam>A(T)
                        if n==1:
                            moment=gaussian_moments(4*ell+1-4*lam,8*lam-A(T),j)[j]
                        else:
                            B=4*lam-4*ell-1
                            assert B>0
                            moment=arb(factorial(j))/B**(j+1)
                        total+=coefficient*n*n*lam**ell*(-lam).exp()*moment
                    ratio=(arb(m+1)/m)**(2*ell+2)*(-pi*(2*m+1)).exp()
                    B=4*pi*m*m-4*ell-1
                    assert ratio<1 and B>0 and 8*pi*m*m>A(T)
                    tail=coefficient*m*m*(pi*m*m)**ell*(-pi*m*m).exp()/(1-ratio)*factorial(j)/B**(j+1)
                    total+=tail;tail_total+=tail
        norms[order]=total.upper();tail_norms[order]=tail_total.upper()
    time_box=arb(A(F(21,200)),A(F(19,200)))
    f3=ends[3]+6*time_box*ends[1]
    f5=ends[5]+20*time_box*ends[3]+60*time_box*time_box*ends[1]
    c=-ends[1]
    error4=(f3.abs_upper()+norms[4])/999**2
    error6=f3.abs_upper()/999**2+(f5.abs_upper()+norms[6])/999**4
    scaled4=c+arb(0,error4.upper())
    scaled6=c+arb(0,error6.upper())
    return {'ends':ends,'tail_ends':tail_ends,'norms':norms,'tail_norms':tail_norms,
            'f3':f3,'f5':f5,'error4':error4,'error6':error6,
            'scaled4':scaled4,'scaled6':scaled6,'polynomials':pp,'heat':heat}


def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--probe-only',action='store_true')
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    p.add_argument('--replay-dir',type=Path,required=True)
    a=p.parse_args();started=time.monotonic();r=endpoint_and_moments(a.bits)
    print(json.dumps({'bits':a.bits,'g1':s(r['ends'][1]),'g3':s(r['ends'][3]),
          'M4':s(r['norms'][4]),'M6':s(r['norms'][6]),
          'scaled4':s(r['scaled4']),'scaled6':s(r['scaled6'])}))
    if a.probe_only:return
    assert r['scaled6']>A(F(37,100)) and r['scaled6']<A(F(3,8))
    # Preserve the failed fourth-derivative bound and its single repair.
    assert not r['scaled4']>0
    source=a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py'
    spec=importlib.util.spec_from_file_location('s06_physical_reference',source)
    reference=importlib.util.module_from_spec(spec);spec.loader.exec_module(reference)
    ev=reference.WholeCellEvaluator(a.bits)
    values,budgets=ev.enclose(F(1,100),F(1,5),F(999),F(1001))
    physical_norm=arb(1000)**F(7,4)*(-125*arb.pi()).exp()
    en=(reference.square(values[0])+reference.square(values[1])).upper()
    physical_E_upper=(physical_norm**2*en).upper()
    raw_lower=A(F(37,100))/1001**2
    ratio_lower=(raw_lower**2/physical_E_upper).lower()
    assert raw_lower**2>arb('1e310')*physical_E_upper

    # Fresh physical premise on a fixed 4-by-16 cover, used explicitly as
    # the inherited input to the completed transverse-current estimate.
    rows=[];minimum=None
    time_cuts=[F(1,100)+F(19,400)*k for k in range(5)]
    space_cuts=[F(999)+F(k,8) for k in range(17)]
    for ta,tb in zip(time_cuts,time_cuts[1:]):
        for xa,xb in zip(space_cuts,space_cuts[1:]):
            jet,errors=ev.enclose(ta,tb,xa,xb)
            energy=reference.square(jet[0])+reference.square(jet[1])
            L=reference.square(jet[1])-jet[0]*jet[2]
            excess=L-energy/100
            assert excess>0
            # Recombine the signed current symbolically before bounding:
            # J - 9 H^2/16 - 9 t E/800 = 9 t (L-E/100)/8.
            lower=(A(F(9,8))*A(ta)*excess).lower()
            assert lower>0
            minimum=lower if minimum is None else min(minimum,lower)
            rows.append({'t':[str(ta),str(tb)],'x':[str(xa),str(xb)],
                         'physical_excess_lower_norm2':s(excess.lower()),
                         'centered_current_excess_lower_norm2':s(lower)})
    assert len(rows)==64
    m=F(81,40083286400);M=F(12526027,200);c=F(9,80000)
    angle=F(9,5010410800)
    assert c/M==angle and angle>F(179,10**11)

    # Independent exact coefficient identity for source completion.
    P={3:1,2:-9,1:23,0:-15}
    right=add(scale({2:1,0:-1},9),scale({2:1,0:-1},-1,1),{1:-24,0:24})
    assert scale(P,-1)==right
    # Exact rational current expansion at nonzero jets, zeros, and events.
    for h,hx,hxx,t,x in ((F(2),F(3),F(-5),F(1,100),F(999)),
                           (F(0),F(7),F(2),F(1,5),F(1001)),
                           (F(0),F(0),F(2),F(1,4),F(0)),
                           (F(1,2),F(0),F(2),F(1,4),F(0))):
        re,im=9*h,x*h-2*t*hx
        rex,imx=9*hx,h+x*hx-2*t*hxx
        current=(re*imx-im*rex)/16
        assert current==F(9,16)*h*h+F(9,8)*t*(hx*hx-h*hxx)
    negative_current=F(9,16)*F(1,2)**2+F(9,8)*F(1,4)*(-1)
    assert negative_current==F(-9,64)

    a.replay_dir.mkdir(parents=True,exist_ok=True)
    controls_source=a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py'
    controls_output=a.replay_dir/'CONTROLS.json'
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    subprocess.run([sys.executable,str(controls_source),'--repo',str(a.repo),
            '--receipts',str(a.replay_dir/'receipts'),'--output',str(controls_output),
            '--execution-model',a.execution_model,'--execution-effort',a.execution_effort],
            check=True,capture_output=True,text=True,timeout=60,env=env)
    controls=json.loads(controls_output.read_text())
    assert len(controls['screen']['event_rejections'])==5
    assert all(v['strict_first_jet_rejected'] and v['strict_signed_margin_rejected']
               for v in controls['screen']['event_rejections'])
    assert controls['screen']['euler_witness']['strict_signed_margin_rejected']
    record={
      'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
      'actual_model':a.execution_model,'actual_effort':a.execution_effort,
      'llm_assistance':'substantial; same-model internal review',
      'python':platform.python_version(),'python_flint':flint.__version__,
      'precision_bits':a.bits,'rounding':'outward Arb; integer polynomial recurrences exact',
      'status':'pass','script_sha256':digest(__file__),
      'mathematical_source_sha256':{
         str(p.relative_to(a.repo)):digest(p) for p in [
           a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md',
           a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md',
           a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md']},
      'domain':{'t':['1/100','1/5'],'x':['999','1001']},
      'source_estimate':{
         'retained_modes':[1,8],'first_omitted_mode':9,
         'g_endpoint_derivatives':[s(v) for v in r['ends']],
         'endpoint_tail_allowances':[s(v) for v in r['tail_ends']],
         'f3_uniform':s(r['f3']),'f5_uniform':s(r['f5']),
         'L1_derivative_majorants':{str(k):s(v) for k,v in r['norms'].items()},
         'L1_mode_tail_allowances':{str(k):s(v) for k,v in r['tail_norms'].items()},
         'first_attempt':{'order':4,'signed_gate':'failed','scaled_enclosure':s(r['scaled4'])},
         'one_repair':{'order':6,'signed_gate':'passed','scaled_enclosure':s(r['scaled6']),
                       'scaled_error_allowance':s(r['error6'])},
         'certified_signed_rounding':'37/100 < x^2*(-i*G1) < 3/8',
         'raw_observation_lower':s(raw_lower)},
      'physical_comparison':{
         'normalization':'fixed G0=1000^(7/4)*exp(-125*pi); E scales by G0^2',
         'G0':s(physical_norm),'whole_box_E_upper_norm2':s(en),
         'whole_box_E_upper_physical':s(physical_E_upper),
         'raw_magnitude_squared_over_E_lower':s(ratio_lower),
         'certified_mismatch':'|-i*G1|^2 > 10^310 E throughout the pilot',
         'reference_code_sha256':digest(source),'reference_source_pins':reference.source_pins(a.repo),
         'fresh_setup_seconds':ev.setup_seconds,
         'whole_box_added_errors_norm':[s(v['total']) for v in budgets]},
      'completed_signed_current':{
         'source':'C=q*g+3/4*(D-1)*psi=(9-D)*Phi/4',
         'observation_convention':'one half of full-line integral exp(t*u^2)*C(u)*exp(i*x*u); combine C before integration',
         'transform':'Z=(9*H+i*(x*H-2*t*Hx))/4',
         'centered_current':'Im(conj(Z)*Zx)-9*H^2/16=9*t*L0/8',
         'inherited_physical_premise':'L0 > E/100, rechecked fresh on fixed 4-by-16 cover',
         'norm_comparison_lower':str(m),'norm_comparison_upper':str(M),
         'current_E_lower':str(c),'argument_speed_lower':str(angle),
         'minimum_centered_excess_lower_norm2':s(minimum),'fixed_cover':rows,
         'independent_new_physical_sign_bound':False},
      'controls':{'source_sha256':digest(controls_source),'receipt_sha256':digest(controls_output),
                  'event_rejections':5,'euler_signed_witness_rejected':True,
                  'interface':'centered current strict test is exactly positive 9t/8 times inherited signed test; raw-current positivity alone is not this test',
                  'negative_current_polynomial_witness':{'field':'x^2-2*(t-1/2)','t':'1/4','x':'0','J':'-9/64'},
                  'analytic_premise_screen':controls['screen']['analytic_premise_screen']},
      'not_established':['a smaller complete physical approximation error','new noncollision coverage',
            'independent theta current positivity','global signed estimate','all-order compensation obstruction'],
      'seconds':time.monotonic()-started}
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','bits':a.bits,'pilot_signed_raw':True,
          'raw_vs_energy_lower':s(ratio_lower),'fresh_current_cells':len(rows),
          'minimum_current_excess_norm2':s(minimum),'seconds':record['seconds']}))


if __name__=='__main__':main()
