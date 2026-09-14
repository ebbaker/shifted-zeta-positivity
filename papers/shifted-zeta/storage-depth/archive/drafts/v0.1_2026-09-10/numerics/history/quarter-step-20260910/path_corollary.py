#!/usr/bin/env python3
"""Corollaries of the full reference certificate and the central row bound."""
import hashlib
import json
from pathlib import Path
from flint import arb as A,ctx
import central_residual as r

def run():
    ctx.prec=1024
    here=Path(__file__).resolve().parent
    record=json.loads((here/'reference_256.json').read_text())
    assert record['status']=='PASS' and record['horizon']=='99/50'
    for name,digest in record['source_sha256'].items():
        assert hashlib.sha256((r.ROOT/name).read_bytes()).hexdigest()==digest
    a=A(7).log();h=(A(8).log()-a)/4;L=a+h
    ceiling=r.c.rat('99/50')
    assert L<ceiling
    m=r.c.rat(record['central_coercivity'])
    wmax=r.c.rat('5e-17')
    active=r.c.prime_powers(ceiling)
    g=r.c.profile(record['M'])
    bounds=r.c.analytic(ceiling,g,record['N'],active,None)
    C=bounds['generator_change_constant']
    assert C*wmax*wmax<m/2
    defect_lower=-(-m*wmax).expm1()
    assert defect_lower>r.c.rat('4.99e-48')
    # Bound the central cross block, combining disjoint arithmetic windows.
    delays=[A(n).log() for n,_,_ in active]
    assert all(h<y-x for x,y in zip(delays,delays[1:]))
    arithmetic_norm=sum((A(p).log()**2/n for n,p,_ in active),A(0)).sqrt()
    b=A.pi()/2+bounds['smooth_variation']*(a*h).sqrt()/2+arithmetic_norm
    f0=r.row_floor(h,record['M'],g)
    penalty=b*b/f0
    assert penalty<8
    central_slack=m/(m+penalty)
    assert central_slack>r.c.rat('1e-32')
    # A simple additional arithmetic norm observation, not used by the
    # existing certificate or by its small-shift corollary.
    points=[A(0),ceiling]+delays+[ceiling-d for d in delays]
    points.sort(key=lambda x:float(x.mid()))
    row_bounds=[]
    for lo,hi in zip(points,points[1:]):
        assert lo<hi
        x=(lo+hi)/2;val=A(0)
        for n,p,_ in active:
            d=A(n).log();weight=A(p).log()/A(n).sqrt()
            if x>d:val+=weight
            else:assert x<d
            if x<ceiling-d:val+=weight
            else:assert x>ceiling-d
        row_bounds.append(val.upper())
    data={'scope':'Full-operator consequences in the working v0.3 normalization. The full-depth proof uses the existing reference method.',
          'quarter_depth':L.str(40),'rational_ceiling':'99/50',
          'central_coercivity':'1e-31','safe_shift_interval':'0 < omega <= 5e-17',
          'generator_change_constant_upper':C.upper().str(35),
          'shift_change_at_upper_endpoint_upper':(C*wmax*wmax).upper().str(35),
          'uniform_generator_floor':'5e-32',
          'transfer_norm_bound':'||V_{omega,L}|| <= exp(-5e-32*omega)',
          'cumulative_relative_coupling_squared_bound':'c_D(omega)^2 <= exp(-1e-31*omega)',
          'storage_floor_at_shift_5em17':defect_lower.lower().str(45),
          'central_cross_norm_upper':b.upper().str(35),
          'central_schur_penalty_norm_upper':penalty.upper().str(35),
          'full_central_relative_slack_lower':central_slack.lower().str(45),
          'rounded_full_central_relative_slack_lower':'1e-32',
          'joint_arithmetic_row_norm_upper':max(row_bounds).str(35),
          'separated_arithmetic_chain_bound':bounds['arithmetic_norm_bound'].str(35),
          'all_checks_pass':True,
          'reference_result_sha256':hashlib.sha256((here/'reference_256.json').read_bytes()).hexdigest(),
          'source_sha256':{str(p.relative_to(r.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(r.__file__),Path(r.c.__file__)]}}
    (here/'path_corollary.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__':run()
