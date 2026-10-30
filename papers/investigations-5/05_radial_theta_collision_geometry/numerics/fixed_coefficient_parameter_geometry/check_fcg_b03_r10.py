#!/usr/bin/env python3
"""Fixed R10 corollary constants and one analytical transport-limit witness.
Prepared for Edward Baker with LLM assistance, gpt-6-astra/max, 2026-10-30.
No source, quadrature, root finding, new jets or parameter sweep.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import argparse,hashlib,json,time

def dec(z):
    m=F(int(z['mid_binary'][0]))*F(2)**int(z['mid_binary'][1])
    r=F(int(z['rad_binary'][0]))*F(2)**int(z['rad_binary'][1])
    assert r>=0
    return m-r,m+r
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z),max(z)
def scale(a,x):return mul(a,(x,x))
def ir(a):return {'lower':str(a[0]),'upper':str(a[1])}
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    start=time.monotonic();repo=args.repo.resolve();base=repo/'papers/investigations-5/05_radial_theta_collision_geometry'
    inp=base/'numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json'
    assert hashlib.sha256(inp.read_bytes()).hexdigest()=='557c57e420534e4db949e3d019d5d40077a1df8f055f6634bd2f657c4f87392c'
    data=json.loads(inp.read_text());stage=next(z for z in data['stages'] if z['bits']==384)
    def mom(j,y):return dec(next(z for z in stage['integrals'] if z['kind']=='moment' and z['j']==j and z['T']=='17/64' and z['Y']==y)['complete'])
    jets={z['j']:dec(z['complete']) for z in stage['integrals'] if z['kind']=='jet'}
    L=add(mom(0,'0'),mom(1,'0'));R2=add(mom(0,'4'),mom(1,'4'));M4=mom(4,'1/64')
    r9p=base/'numerics/fixed_coefficient_parameter_geometry/fcg_b03_r9_signed_transport_20261030.json'
    r9=json.loads(r9p.read_text())
    checks=[]
    def ck(name,condition):
        assert condition,name
        checks.append(name)
    mu=F('2.3e-10');Nbar=F('.508');c=F(1);rho=F(1,16384);pi_upper=F(22,7);sqrt_lower=F(3,200000)
    ck('accepted local derivative floor exceeds selected mu',F(r9['consumer']['scalar_HA_floor_lower'])>mu)
    ck('complete L cap',L[1]<F('.067746'))
    ck('complete R2 cap',R2[1]<F('.100970'))
    ck('uniform tube time below carrier time',F(1,4)+F(1,128)+rho<F(17,64))
    ck('common c=1 moment bound',max(R2[1]+6*L[1],3*L[1]/c)<Nbar)
    ratio=mu/(2*Nbar)
    ck('rational lower square root',sqrt_lower**2<ratio)
    energy=3*mu**2/(16*pi_upper)*ratio*sqrt_lower
    ck('common all-time energy exceeds 1e-35',energy>F('1e-35'))
    ck('outward energy display bound',energy>F('1.07166e-35'))
    Danchor=add(mul(jets[1],jets[1]),scale(mul(jets[0],jets[2]),F(-2)))
    ck('positive complete moment M4 lower endpoint',M4[0]>0)
    ck('positive anchor discriminant upper endpoint',Danchor[1]>0)
    X=F(4)
    omitted=M4[0]*X**17/F(factorial(17))
    deficit=Danchor[1]-omitted**2
    # Exactly one predeclared width witness; no adjustment if it fails.
    witness=deficit<0
    ck('single X=4 witness rejects the unchanged payment',witness)
    ck('outward complete M4 display',M4[0]>F('2.3540e-5'))
    ck('outward anchor discriminant display',Danchor[1]<F('1.905844e-19'))
    ck('outward omitted error display',omitted>F('1.13700e-9'))
    ck('outward paid discriminant failure display',deficit<F('-1.10e-18'))
    ck('outward cost ratio display',omitted**2/Danchor[1]>F('6.78'))
    evidence=[inp,r9p,base/'reviews/fixed_coefficient_parameter_geometry/E02_R9_SIGNED_TRANSPORT_ASSESSMENT_20261030.md',base/'notes/fixed_coefficient_parameter_geometry/12_REGIONAL_MOMENT_COEFFICIENT_AND_COMMON_FLOW_LIMITS_B03_R2_20261030.md']
    result={
      'task':'FCG-B03 R10 finite physical consequence and fixed-input transport limit',
      'date':'2026-10-30','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance',
      'model':'gpt-6-astra','effort':'max','thread_id':'01a18e52-fa91-7b61-b31b-b311eee675f8','history_number':50,
      'provenance':'Proof-author exact arithmetic from accepted R9 and inherited carrier; no independent R10 assessment or independent source validation.',
      'inputs':[{'path':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in evidence],
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'fixed':{'center_time':'1/4','center_A':64,'time_halfwidth':'1/128','R9_A_interval':[64,66],'tube_radius':str(rho),'spatial_c':str(c),'mu':str(mu),'Nbar_upper':str(Nbar),'width_witness':str(X),'source_order':17},
      'complete_L':ir(L),'complete_R2':ir(R2),'complete_M4':ir(M4),'anchor_D':ir(Danchor),
      'energy':{'pi_upper':str(pi_upper),'square_root_lower':str(sqrt_lower),'ratio':str(ratio),'lower_bound':str(energy),'claimed_floor':'1e-35'},
      'transport_limit':{'first_omitted_error_lower':str(omitted),'squared_error_lower':str(omitted**2),'anchor_D_upper':str(Danchor[1]),'paid_D_upper_at_X4':str(deficit),'cost_to_anchor_D_ratio_lower':str(omitted**2/Danchor[1]),'scope':'R9 same order17, anchor/time interval and absolute complete-M4 core payment on widening [64,64+X]. Not a statement about the true discriminant, higher orders, new centers, other tails, or theta collisions.'},
      'checks':checks,'status':'both_fixed_questions_decided','new_source_evaluations':0,'new_quadrature_evaluations':0,'parameter_sweep':False,'runtime_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'energy_lower':float(energy),'M4_lower':float(M4[0]),'anchor_D_upper':float(Danchor[1]),'X4_error_lower':float(omitted),'paid_D_upper_X4':float(deficit),'cost_ratio':float(omitted**2/Danchor[1]),'seconds':result['runtime_seconds']}))
if __name__=='__main__':main()
