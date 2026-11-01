#!/usr/bin/env python3
"""Fixed E02 R10 saved-input reconstruction; prepared for Edward Baker.
Substantial LLM assistance, actual gpt-6.1-sol/ultra, 30 October 2026.
This exact arithmetic supplements the analytical assessment; no source calls.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import argparse,hashlib,json,re

BASE=Path('papers/investigations-5/05_radial_theta_collision_geometry')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def endpoints(z):
    def number(pair):
        a,e=int(pair[0]),int(pair[1])
        return Q(a*2**e) if e>=0 else Q(a,2**(-e))
    center=number(z['mid_binary']);radius=number(z['rad_binary'])
    assert radius>=0
    return center-radius,center+radius
def bounds(z):return {'lower':str(z[0]),'upper':str(z[1])}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--replay',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();root=a.repo.resolve();base=root/BASE
    packet=base/'research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R10_COMMON_FLOW_AND_TRANSPORT_ASSESSMENT_20261030.md'
    pairs=re.findall(r'\| `(papers/[^`]+)` \| `([a-f0-9]{64})` \|',packet.read_text());assert len(pairs)==11
    inputs=[]
    for rel,want in pairs:
        actual=sha(root/rel);assert actual==want,rel
        inputs.append({'path':rel,'sha256':actual})
    record=json.loads((base/'numerics/fixed_coefficient_parameter_geometry/fcg_b03_r10_fixed_flow_and_transport_limit_20261030.json').read_text())
    replay=json.loads(a.replay.read_text());old=dict(record);fresh=dict(replay)
    old.pop('runtime_seconds');fresh.pop('runtime_seconds');assert old==fresh
    source=json.loads((base/'numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json').read_text())
    stage=[s for s in source['stages'] if s['bits']==384];assert len(stage)==1;stage=stage[0]
    def moment(j,y):
        rows=[z for z in stage['integrals'] if z['kind']=='moment' and z['j']==j and z['T']=='17/64' and z['Y']==y];assert len(rows)==1
        return endpoints(rows[0]['complete'])
    l0,l1=moment(0,'0'),moment(1,'0');r0,r1=moment(0,'4'),moment(1,'4');m4=moment(4,'1/64')
    L=(l0[0]+l1[0],l0[1]+l1[1]);R2=(r0[0]+r1[0],r0[1]+r1[1]);Nmax=max(R2[1]+6*L[1],3*L[1])
    mu=Q(23,10**11);nbar=Q(127,250);rootlower=Q(3,200000);ratio=mu*Q(125,127)
    energy=Q(21,352)*mu**2*ratio*rootlower
    assert L[1]<Q('.067746') and R2[1]<Q('.100970') and Nmax<nbar
    assert rootlower**2<ratio and energy>Q('1.07166e-35')>Q('1e-35')
    tmax=Q(4225,16384);slack=Q(17,64)-tmax;assert slack==Q(127,16384)>0
    r9=json.loads((base/'numerics/fixed_coefficient_parameter_geometry/fcg_b03_r9_signed_transport_20261030.json').read_text())
    assert Q(r9['consumer']['scalar_HA_floor_lower'])>mu
    h={z['j']:endpoints(z['complete']) for z in stage['integrals'] if z['kind']=='jet'}
    # Sign-aware endpoint reconstruction, without the author's interval helpers.
    assert h[1][1]<0 and h[0][0]>0 and h[2][1]<0
    square_h1=(h[1][1]**2,h[1][0]**2)
    positive_cross=(-2*h[0][0]*h[2][1],-2*h[0][1]*h[2][0])
    D=(square_h1[0]+positive_cross[0],square_h1[1]+positive_cross[1])
    omitted=m4[0]*Q(4)**17/factorial(17);squared=omitted**2;deficit=D[1]-squared;cost=squared/D[1]
    assert m4[0]>Q('2.3540e-5') and D[1]<Q('1.905844e-19')
    assert omitted>Q('1.13700e-9') and deficit<Q('-1.10e-18') and cost>Q('6.78')
    expected={'complete_L':bounds(L),'complete_R2':bounds(R2),'complete_M4':bounds(m4),'anchor_D':bounds(D)}
    for key,value in expected.items():assert record[key]==value,key
    assert Q(record['energy']['lower_bound'])==energy
    tr=record['transport_limit']
    for key,value in [('first_omitted_error_lower',omitted),('squared_error_lower',squared),('anchor_D_upper',D[1]),('paid_D_upper_at_X4',deficit),('cost_to_anchor_D_ratio_lower',cost)]:assert Q(tr[key])==value,key
    result={'task':'FCG-E02 R10 common-flow and fixed-transport assessment','date':'2026-10-30','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance','model':'gpt-6.1-sol','effort':'ultra','thread_id':'01a18e61-b771-7d81-9290-9dad3cc07d78','history_number':51,'packet_sha256':sha(packet),'frozen_inputs':inputs,'replay_matches_except_runtime':True,'independent_reconstruction':expected,'carrier':{'mu':str(mu),'tube_time_max':str(tmax),'carrier_time_slack':str(slack),'moment_upper':str(Nmax),'Nbar':str(nbar),'root_lower_squared':str(rootlower**2),'ratio':str(ratio),'energy_lower':str(energy)},'fixed_width4':{'omitted_budget_lower':str(omitted),'squared_budget_lower':str(squared),'cost_ratio':str(cost),'paid_D_upper':str(deficit),'threshold_power34':str(factorial(17)**2*D[1]/m4[0]**2)},'obligations':{str(k):'accepted without mathematical correction' for k in range(1,6)},'script_sha256':sha(Path(__file__)),'new_source_evaluations':0,'new_quadrature_evaluations':0,'parameter_scan':False,'provenance':'Different-model internal assessment of Astra R10 proof; parent plus two read-only same-Sol contributions. Independently arranged rational reconstruction shares source enclosures, Fraction arithmetic and analytic premises; no specialist, formal or independent source validation.'}
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'five_obligations_accepted','frozen_hashes':len(inputs),'replay':'matches except runtime','energy_lower':float(energy),'paid_D_upper_X4':float(deficit),'cost_ratio':float(cost)}))
if __name__=='__main__':main()
