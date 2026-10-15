#!/usr/bin/env python3
"""Extract a genuine stationary-branch pilot from the paid 100--104 record.

Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded inherited model gpt-6-astra, reasoning effort ultra.
Exact rational arithmetic only; no quadrature rerun or finite gap division.
The source certificate and its imported analytic tail lemmas remain inputs.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def dyadic(pair):
    m,e=pair
    require(isinstance(e,int) and abs(e)<100000,'valid dyadic exponent')
    return Q(int(m))*Q(2)**e


def iv(encoded):
    lo,hi=map(dyadic,encoded)
    require(lo<=hi,'ordered interval')
    return lo,hi


def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b]
    return min(p),max(p)
def scale(a,q): return mul(a,(Q(q),Q(q)))
def power(a,n):
    ans=(Q(1),Q(1))
    for _ in range(n): ans=mul(ans,a)
    return ans

def encode_interval(a): return [str(a[0]),str(a[1])]
def display(a): return [float(a[0]),float(a[1])]


def endpoint_transport(row, side, lx, lt, component=1):
    xl,xr=map(Q,row['x']);tl,tr=map(Q,row['t'])
    dx=(xr-xl)/2*(1 if side=='right' else -1)
    dt=(tr-tl)/2
    eta=(dx,dx);delta=(-dt,dt)
    centers=list(map(iv,row['center_jets']))
    val=(Q(0),Q(0))
    for ell in range(lt):
        spatial=(Q(0),Q(0))
        for m in range(lx):
            term=scale(mul(power(eta,m),centers[component+2*ell+m]),Q(1,factorial(m)))
            spatial=add(spatial,term)
        val=add(val,scale(mul(power(neg(delta),ell),spatial),Q(1,factorial(ell))))
    rem=iv(row['jet_space_payments'][component])[1]+iv(row['jet_time_payments'][component])[1]
    return add(val,(-rem,rem))


def main(args):
    r=json.loads(args.record.read_text())
    require(r['status']=='PASS' and r['failed_cells']==[], 'input certificate passes')
    require(r['schema']=='inv21_phase_centered_complete_source_pilot_v1','input schema')
    require(r['domain']=={'x':['100','104'],'t':['0','1/2']},'input domain')
    require(r['space_order']==12 and r['time_order']==8,'expansion orders')
    require(digest(args.driver)==r['script_sha256'],'input driver hash')
    require(digest(args.contour_source)==r['imported_source_sha256'],'input contour source hash')
    rows=[row for row in r['cells'] if row['x']==['101','102']]
    require(len(rows)==8 and [row['t'] for row in rows]==[[str(Q(j,16)),str(Q(j+1,16))] for j in range(8)],'complete eight-slab closed cover')
    a=iv(r['a']);mu=add(power(a,2),(Q(1,16),Q(1,16)))
    require(a[0]>0 and mu[0]>0,'positive prescribed parameters')
    out=[]
    for i,row in enumerate(rows):
        jets=list(map(iv,row['whole_cell_jets']))
        h0,h1,h2,h3=jets
        left=endpoint_transport(row,'left',12,8)
        right=endpoint_transport(row,'right',12,8)
        require(left[0]>0 and right[1]<0,f'opposite genuine h1 endpoint signs slab {i}')
        require(h0[0]>0 and h2[1]<0,f'h0 positive and h1 strictly decreasing slab {i}')
        # On h1=0 only: C0=-h2-mu*h0. All terms are full physical jets
        # in the source record's constant positive normalization.
        C0=sub(neg(h2),mul(mu,h0))
        require(C0[0]>0,f'favorable signed residual slab {i}')
        favorable=mul(h0,C0)
        signed=add(mul(mu,power(h0,2)),favorable)
        direct=neg(mul(h0,h2))
        require(signed[0]>0 and direct[0]>0,f'fixed K0=0 signed estimate slab {i}')
        strong_margin=C0[0]-mu[1]*h0[1]
        require(strong_margin>0,f'all eta<=mu strong cones fail slab {i}')
        # E=h0^2 at genuine h1=0, and discarding C1^2 gives an upper
        # bound for the strong-cone slack. No division by E is used.
        cone_slack_upper=mu[1]**2*h0[1]**2-C0[0]**2
        require(cone_slack_upper<0,f'strong-cone eta=mu negative slack slab {i}')
        require(left[0]>37 and right[1]<-20 and favorable[0]>6000 and signed[0]>9400
                and strong_margin>Q(7,5) and cone_slack_upper<-78,
                f'advertised conservative rational margins slab {i}')
        out.append({'x':row['x'],'t':row['t'],
                    'normalization':row['normalization'],
                    'h1_left_endpoint_all_times':encode_interval(left),
                    'h1_right_endpoint_all_times':encode_interval(right),
                    'h0_whole_cell':encode_interval(h0),'h2_whole_cell':encode_interval(h2),
                    'C0_on_stationary_set':encode_interval(C0),
                    'h0_C0_on_stationary_set':encode_interval(favorable),
                    'signed_curvature_lower':str(signed[0]),
                    'direct_curvature_lower':str(direct[0]),
                    'C0_minus_mu_h0_lower':str(strong_margin),
                    'cone_slack_eta_mu_upper':str(cone_slack_upper),
                    'K0':0,'passed':True,
                    'display_only':{'h1_left':display(left),'h1_right':display(right),
                                    'h0':display(h0),'h2':display(h2),'C0_stationary':display(C0),
                                    'favorable_residual_lower':float(favorable[0]),
                                    'signed_curvature_lower':float(signed[0]),
                                    'C0_minus_mu_h0_lower':float(strong_margin),
                                    'cone_slack_eta_mu_upper':float(cone_slack_upper)}})
    result={'schema':'inv21_genuine_stationary_favorable_curvature_pilot_v1',
            'date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial',
            'recorded_model':'gpt-6-astra','recorded_effort':'ultra','status':'PASS',
            'script_sha256':digest(Path(__file__)),
            'input_record_name':args.record.name,'input_record_sha256':digest(args.record),
            'input_driver_name':args.driver.name,'input_driver_sha256':digest(args.driver),
            'input_contour_name':args.contour_source.name,'input_contour_sha256':digest(args.contour_source),
            'parameters':{'a':encode_interval(a),'b':'1/4','mu':encode_interval(mu),'comparison_eta':'mu'},
            'domain':{'x':['101','102'],'t':['0','1/2']},
            'stationarity_existence':'For every t in [0,1/2], h1(t,101)>0>h1(t,102) and h2<0 throughout: exactly one h1=0 point in (101,102).',
            'result':'Along that genuine branch, h0*C0>0 and L0=mu*h0^2+h0*C0>0, so the one-sided target holds with prescribed K0=0; every strong residual cone with eta<=mu fails.',
            'identity':'At h1=0, C0=-h2-mu*h0, E=h0^2; C0>mu*h0 implies C0^2+C1^2>mu^2 E.',
            'proof_scope':'Exact-rational re-use of validated full-source whole-cell jets and paid endpoint Taylor transport; no new quadrature or tail approximation.',
            'limitations':['b=1/4 is a deliberately prescribed alternative centering, not the natural saddle-based centering of the input record.',
                           'This does not show failure of the existing natural-centering eta=1/3 cone, which passes throughout 100--104.',
                           'The rejected cones are eta<=mu, sufficient for nonnegative first stationary curvature; a larger cone budget may still hold.',
                           'This finite branch is already covered by the input certificate; there is no height extension, unknown collision, all-height result or RH conclusion.',
                           'The imported quadrature record and analytic complete-source tail lemmas are assumed valid; their original numerical verification is not rerun here.',
                           'The K0=0 proof uses signed products directly and never defines a loss by dividing by a certified energy floor.'],
            'slab_count':len(out),'slabs':out,
            'uniform_display_only':{'h1_left_lower':float(min(ivv['display_only']['h1_left'][0] for ivv in out)),
                                    'h1_right_upper':float(max(ivv['display_only']['h1_right'][1] for ivv in out)),
                                    'favorable_residual_lower':float(min(Q(ivv['h0_C0_on_stationary_set'][0]) for ivv in out)),
                                    'C0_minus_mu_h0_lower':float(min(Q(ivv['C0_minus_mu_h0_lower']) for ivv in out)),
                                    'signed_curvature_lower':float(min(Q(ivv['signed_curvature_lower']) for ivv in out))}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'slabs':len(out),'uniform_display_only':result['uniform_display_only'],'output':str(args.output)},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',required=True,type=Path)
    p.add_argument('--driver',required=True,type=Path)
    p.add_argument('--contour-source',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    main(p.parse_args())
