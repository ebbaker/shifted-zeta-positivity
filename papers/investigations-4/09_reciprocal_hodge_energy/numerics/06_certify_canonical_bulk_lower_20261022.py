#!/usr/bin/env python3
"""One fixed actual canonical jet-bulk lower bound; see the fixed contract."""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import flint
from flint import arb, acb, ctx
import rhe_actual_theta_core as core_module
from rhe_actual_theta_core import ActualThetaCore


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def rec(x):
    require(x.is_finite(), 'nonfinite output')
    scale=10**40
    lower=(x.lower()*scale).floor().unique_fmpz()
    upper=(x.upper()*scale).ceil().unique_fmpz()
    require(lower is not None and upper is not None,'rational display endpoints unresolved')
    return {'ball':x.str(45),'lower_exact':str(lower)+'/'+str(scale),
            'upper_exact':str(upper)+'/'+str(scale)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--contract',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=192
    core=ActualThetaCore(bits=192,terms=65,center=35,radius=8,cauchy_radius=16)
    center=acb(0,2); radius=arb(1)
    require(abs(center)+radius<core.r,'source disk inclusion')
    # Exact coefficient translation, including all input coefficient balls.
    shifted=[sum((core.coeff[k]*math.comb(k,j)*center**(k-j)
                  for k in range(j,core.N)),acb(0)) for j in range(core.N)]
    jet=[shifted[k]+acb(0,1)*(k+1)*shifted[k+1]
         for k in range(core.N-1)]+[shifted[-1]]
    source_jet_error=core.tail0+core.tail1
    source_derivative_error=core.tail1+2*core.tail2half
    derivative=jet[1]
    err=source_derivative_error.abs_upper()
    derivative=acb(derivative.real+arb(0,err),derivative.imag+arb(0,err))
    derivative_lower=abs(derivative).lower()
    require(derivative_lower>0,'canonical jet derivative lower')
    disk_upper=(sum((abs(jet[k])*radius**k for k in range(core.N)),arb(0))
                +source_jet_error).upper()
    require(disk_upper>0,'positive finite disk upper')
    phi_floor=(arb(31)/32)**3*(arb(23)/32)**3
    bulk_lower=phi_floor*arb.pi()*radius**2*derivative_lower**2/disk_upper
    require(bulk_lower.lower()>0,'strict positive bulk mass')
    potential_source_error=arb('8.05e-19')
    require(bulk_lower>potential_source_error,'strict reduction beyond potential source error')
    require((arb(4)*arb(2).sqrt())>3,'disk inside cutoff rectangle')
    out={
      'schema':'rhe-canonical-bulk-lower-v1','date':'2026-10-22',
      'prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
      'LLM_assistance':'substantial','status':'fixed canonical lower bound interval-certified',
      'python':platform.python_version(),'python_flint':flint.__version__,'bits':192,
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'oracle_sha256':hashlib.sha256(Path(core_module.__file__).read_bytes()).hexdigest(),
      'contract_sha256':hashlib.sha256(args.contract.read_bytes()).hexdigest(),
      'geometry':{'time':'0','source_center':'35','source_radius':'8','outer_cauchy_radius':'16',
                  'terms':65,'jet_disk_center':'35+2i','jet_disk_radius':'1',
                  'cutoff_half_width_and_height':'4sqrt(2)'},
      'phi_floor':rec(phi_floor),'source_majorant':rec(core.M),
      'source_errors':{'H':rec(core.tail0),'Hprime':rec(core.tail1),
                       'Hsecond':rec(2*core.tail2half),'J':rec(source_jet_error),
                       'Jprime':rec(source_derivative_error)},
      'Jprime_center_real':rec(derivative.real),'Jprime_center_imag':rec(derivative.imag),
      'abs_Jprime_center_lower':rec(derivative_lower),
      'sup_disk_abs_J_upper':rec(disk_upper),'M_phi_lower':rec(bulk_lower),
      'ratio_lower_to_potential_source_error':rec(bulk_lower/potential_source_error),
      'conditions':{'source_disk_inclusion':True,'cutoff_disk_inclusion':True,
                    'all_source_and_coefficient_errors_retained':True,
                    'positive_mass_lower':True,'lower_exceeds_potential_source_error':True},
      'not_acquired':'No signed potential/trace value or sign, physical amplitude floor, RH, event, or simplicity exclusion.',
      'comparator':'The same complete canonical point/disk data and identity are available to direct evaluation.'}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'M_phi_lower':out['M_phi_lower'],
                     'ratio_lower_to_source_error':out['ratio_lower_to_potential_source_error']}))


if __name__=='__main__':
    main()
