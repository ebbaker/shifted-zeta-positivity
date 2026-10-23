#!/usr/bin/env python3
"""Fixed canonical direct trace reference; see adjacent predeclared contract."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json,math,platform
from pathlib import Path
from time import perf_counter
import flint
from flint import arb,ctx
import rhe_actual_theta_core as core_module
from rhe_actual_theta_core import ActualThetaCore


def require(c,label):
    if not c:raise ArithmeticError(label)


def rec(x):
    require(x.is_finite(),'nonfinite output')
    scale=10**40
    lo=(x.lower()*scale).floor().unique_fmpz()
    hi=(x.upper()*scale).ceil().unique_fmpz()
    require(lo is not None and hi is not None,'exact endpoints unresolved')
    return {'ball':x.str(50),'lower_exact':str(lo)+'/'+str(scale),'upper_exact':str(hi)+'/'+str(scale)}


def horner(c,x):
    p=arb(c[-1])
    for b in c[-2::-1]:p=p*x+b
    return p


def antiderivative(s):return s-s**3+arb(3)*s**5/5-s**7/7


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    contract=args.contract
    ctx.prec=192
    start=perf_counter()
    core=ActualThetaCore(bits=192)
    coeff=[core.coeff]
    for j in range(1,6):
        coeff.append([(k+1)*coeff[j-1][k+1] for k in range(len(coeff[j-1])-1)])
    tails=[core.tail0,core.tail1,2*core.tail2half]
    remainders=[sum((abs(a)*core.r**k for k,a in enumerate(coeff[j+3])),arb(0)) for j in range(3)]
    L=4*arb(2).sqrt();n=1024
    require(L<core.r,'real interval inside complete source disk')
    setup=perf_counter()-start
    out=arb(0);minE=None;minQ=None
    maxrad=arb(0);start=perf_counter()
    for k in range(n):
        smid=-arb(1)+(2*arb(k)+1)/n
        xmid=L*smid;rx=L/n;delta=arb(0,rx.abs_upper())
        vals=[]
        for j in range(3):
            p0=horner(coeff[j],xmid);p1=horner(coeff[j+1],xmid);p2=horner(coeff[j+2],xmid)
            err=(remainders[j]*rx**3/6+tails[j]).abs_upper()
            v=p0+delta*(p1+delta*p2/2)+arb(0,err)
            require(v.is_finite(),'field range nonfinite at cell '+str(k));vals.append(v)
        h,d1,d2=vals;E=h**2+d1**2;Q=d1**2-h*d2
        require(E>0,'E floor unresolved at cell '+str(k))
        value=Q/E.sqrt()
        slo=-arb(1)+arb(2)*k/n;shi=-arb(1)+arb(2)*(k+1)/n
        weight=L*(antiderivative(shi)-antiderivative(slo))
        require(weight>0,'positive exact cutoff weight unresolved')
        out+=weight*value
        ef=E.lower();qf=Q.lower()
        minE=ef if minE is None or ef<minE else minE
        minQ=qf if minQ is None or qf<minQ else minQ
    elapsed=perf_counter()-start
    require(out.is_finite(),'trace enclosure nonfinite')
    result={'schema':'rhe-direct-signed-trace-reference-v1','date':'2026-10-22','prepared_for':'Edward Baker',
      'model':'gpt-6.1-sol','reasoning_effort':'ultra','LLM_assistance':'substantial',
      'status':'single fixed 1024-cell outward-ball direct trace reference',
      'python':platform.python_version(),'python_flint':flint.__version__,'bits':192,
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'oracle_sha256':hashlib.sha256(Path(core_module.__file__).read_bytes()).hexdigest(),
      'contract_sha256':hashlib.sha256(contract.read_bytes()).hexdigest(),
      'time':'0','source':'H0(z)=xi((1+iz)/2)/8; unchanged complete canonical field',
      'geometry':{'center':'35','half_width':'4sqrt(2)','cutoff':'(1-s^2)^3','s_interval':'[-1,1]','cells':1024},
      'terms':65,'source_radius':'8','outer_cauchy_radius':'16',
      'source_tails':{'H':rec(tails[0]),'Hprime':rec(tails[1]),'Hsecond':rec(tails[2])},
      'polynomial_third_derivative_majorants_for_H_Hprime_Hsecond':[rec(v) for v in remainders],
      'T_psi':rec(out),'relative_width':rec(2*out.rad()/abs(out.mid())),
      'E_cell_floor_lower':rec(minE),'Q_cell_floor_lower':rec(minQ),
      'setup_seconds':setup,'consumer_seconds':elapsed,
      'conditions':{'source_disk_inclusion':True,'all_cells_finite':True,'all_E_cell_floors_positive':True,
                    'all_source_coefficient_and_quadrature_errors_retained':True,'positive_cutoff_cell_weights':True},
      'RH_assumption':False,'not_claimed':'No global sign, RH, simplicity, cap root count, or method-cost dominance.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'T_psi':result['T_psi'],'E_cell_floor_lower':result['E_cell_floor_lower'],
       'Q_cell_floor_lower':result['Q_cell_floor_lower'],'relative_width':result['relative_width'],
       'setup_seconds':setup,'consumer_seconds':elapsed}))

if __name__=='__main__':main()
