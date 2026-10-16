#!/usr/bin/env python3
"""Full-theta physical Hx/Hxx/Hxxx stationary sign at bounded low height.

Outward interval integrals, not sampled sign tests. No holomorphic disk input.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys
import time

HASHES = {
 'check_block_current.py':'0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
 'check_complete_current_rectangle.py':'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path,
        help='Write a record only when this explicit path is supplied.')
    parser.add_argument('--interval-source-dir',type=Path,
        default=Path(__file__).resolve().parents[2]/'13_microlocal_phase_space'/'numerics')
    parser.add_argument('--u-cells',type=int,default=2048)
    parser.add_argument('--x-cells',type=int,default=80)
    parser.add_argument('--height-low',default='8')
    parser.add_argument('--height-high',default='12')
    args=parser.parse_args()
    assert args.u_cells>0 and args.x_cells>0
    for name,digest in HASHES.items():
        if hashlib.sha256((args.interval_source_dir/name).read_bytes()).hexdigest()!=digest:
            raise RuntimeError('Retained interval source mismatch: '+name)
    sys.path.insert(0,str(args.interval_source_dir))
    from check_complete_current_rectangle import I, UP, PRECISION, pi_interval, reduced_trig, absmax
    start=time.perf_counter()
    pi=pi_interval()
    timebox=I(0,'.05')
    xlo,xhi=I(args.height_low),I(args.height_high)
    assert 0<xlo.lo<xhi.lo
    radius=I(1)
    width=radius/args.u_cells

    def phi(u):
        e4,e5,e9=[(u*k).exp() for k in (4,5,9)]
        value=I(0)
        for n in (1,2,3):
            c=pi*n*n
            value+=(2*c**2*e9-3*c*e5)*(-c*e4).exp()
        def omitted(m):
            denominator=1-(I(5)/4)**m*(-9*pi*e4).exp()
            assert denominator.lo>0
            return I(4)**m*(-16*pi*e4).exp()/denominator
        tail=2*pi**2*e9*omitted(4)+3*pi*e5*omitted(2)
        result=value+I(0,tail.hi)
        assert result.lo>0
        return result

    # Full theta density and polynomial insertions are enclosed once.
    weights=[]
    for j in range(args.u_cells):
        left,right=width*j,width*(j+1)
        u=I(left.lo,right.hi)
        density=(timebox*u**2).exp()*phi(u)
        weights.append((u,[width*u**k*density for k in (1,2,3)]))

    # Phi<=C exp(-8*pi*u²), so e^(t*u²)Phi<=C exp(-a*u²).
    # Full n>=1 sum: n4<=16^(n-1), n²-1>=3(n-1), and
    # 16exp(-3pi)<1/2. e4u>=1+4u+8u², 4pi>9.
    assert (16*(-3*pi).exp()).hi<Decimal('.5') and (4*pi).lo>9
    C=4*pi**2*(-pi).exp()
    a=8*pi-I('.05')
    factor=C*(-a*radius**2).exp()
    tails=[factor/(2*a),
        factor*(radius/(2*a)+1/(4*a**2*radius)),
        factor*(radius**2/(2*a)+1/(2*a**2))]
    # The second formula uses Gaussian Mills: int_R∞ exp(-a u²)
    # <=exp(-a R²)/(2a R); the odd moment formulas are exact.

    def pad(z,e):
        return z+I(e.copy_negate(),e)

    def clip_trig(z):
        return I(max(Decimal(-1),z.lo),min(Decimal(1),z.hi))

    def integral(x):
        # Evaluate sin/cos at centre phases by rigorous interval rotation.
        # Every actual xu differs by at most phase_error; |sin'|,|cos'|<=1.
        centre=I(x.midpoint())
        sin_step,cos_step=reduced_trig(centre*width,pi)
        sin_phase,cos_phase=reduced_trig(centre*width/2,pi)
        values=[I(0),I(0),I(0)]
        for j,(u,w) in enumerate(weights):
            phase=centre*width*(I(j)+I('.5'))
            phase_error=absmax(x*u-phase)
            actual_sin=clip_trig(pad(sin_phase,phase_error))
            actual_cos=clip_trig(pad(cos_phase,phase_error))
            values[0]-=w[0]*actual_sin
            values[1]-=w[1]*actual_cos
            values[2]+=w[2]*actual_sin
            sin_phase,cos_phase=(sin_phase*cos_step+cos_phase*sin_step,
                                cos_phase*cos_step-sin_phase*sin_step)
        return [pad(values[j],tails[j].hi) for j in range(3)]

    subcells=[]
    alljets=[[] for _ in range(3)]
    candidates=[]
    xwidth=(xhi-xlo)/args.x_cells
    for k in range(args.x_cells):
        left,right=xlo+xwidth*k,xlo+xwidth*(k+1)
        xb=I(left.lo,right.hi)
        jets=integral(xb)
        for j in range(3):alljets[j].append(jets[j])
        candidate=jets[1].lo<=0<=jets[1].hi
        if candidate:candidates.append((xb,jets))
        assert jets[0].hi<0 and jets[2].lo>0
        assert (jets[0]*jets[2]).hi<0
        subcells.append({'physical_height':xb.strings(),
            'physical_H_jets_1_to_3':[v.strings() for v in jets],
            'Hxx_stationary_candidate':candidate,
            'Hx_Hxxx':(jets[0]*jets[2]).strings()})
    def hull(vals):
        return I(min(v.lo for v in vals),max(v.hi for v in vals))
    whole=[hull(v) for v in alljets]
    laguerre_one=whole[1]**2-whole[0]*whole[2]
    assert laguerre_one.lo>0
    endpoints=[integral(xlo),integral(xhi)]
    assert endpoints[0][1].hi<0<endpoints[1][1].lo
    assert candidates
    rootband=hull([v[0] for v in candidates])
    products=hull([v[1][0]*v[1][2] for v in candidates])
    assert products.hi<0
    record={
        'status':'PASS','date':'2026-10-10','prepared_for':'Edward Baker',
        'model':'GPT-6 (Codex)','reasoning_effort':'Not exposed to this session; not inferred',
        'acknowledgment':'Substantial LLM assistance; internal outward replay, not independent mathematical validation.',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'imported_sources':HASHES,
        'arithmetic':str(PRECISION)+'-digit outward Decimal, corrected integer powers, explicit trig Taylor bounds and interval rotation; no binary float sign tests',
        'source':'Genuine full half-line theta integral, n1..3 plus positive geometric n>=4 tails in every integration cell',
        'physical_jet_dictionary':[
            'Hx=-integral_0∞ u exp(tu²)Phi(u)sin(xu) du',
            'Hxx=-integral_0∞ u² exp(tu²)Phi(u)cos(xu) du',
            'Hxxx=integral_0∞ u³ exp(tu²)Phi(u)sin(xu) du'],
        'domain':{'time':timebox.strings(),'physical_height':[str(xlo.lo),str(xhi.hi)]},
        'integration':{'u_radius':radius.strings(),'u_cells':args.u_cells,'x_cells':args.x_cells,
            'full_theta_absolute_jet_tail_bounds':[str(v.hi) for v in tails],
            'trig_method':'Initial midpoint phase and one-step sin/cos from rigorous Taylor; subsequent centre phases by interval rotation; actual xu enclosed with derivative1 Lipschitz padding'},
        'whole_domain_H_jets_1_to_3':[v.strings() for v in whole],
        'whole_domain_L1_H_equals_J1_Fourier_at_2x':laguerre_one.strings(),
        'Hxx_endpoint_signs':{'left':endpoints[0][1].strings(),'right':endpoints[1][1].strings()},
        'stationary_set':{'one_unique_Hxx_zero_for_each_time':True,
            'stationary_height_band':rootband.strings(),'candidate_subcells':len(candidates),
            'Hx_Hxxx_on_candidate_band':products.strings(),
            'S1_strictly_nonvacuous':True},
        'subcells':subcells,'runtime_seconds':str(time.perf_counter()-start),
        'limitations':[
            'Bounded genuine theta S1 calibration only; no global stationary cover or RH implication.',
            'Timezero is included in the calibration, but no negative-time predecessor buffer is proved.',
            'Hx is strictly negative throughout, so S0 is vacuous on this rectangle.',
            'The full-source integration uses no finite arithmetic disk approximation.']}
    if args.record:args.record.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:record[k] for k in ('status','domain','whole_domain_H_jets_1_to_3','Hxx_endpoint_signs','stationary_set','runtime_seconds')},indent=2))


if __name__=='__main__':main()
