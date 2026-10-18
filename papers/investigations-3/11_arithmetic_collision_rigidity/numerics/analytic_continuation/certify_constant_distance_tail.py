#!/usr/bin/env python3
"""Outward scalar check for the constant-distance contour-tail theorem.
Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
GPT-6.1 Sol; actual effort ultra inherited from the parent research run.
Only two predeclared parameter sets; no theta integrals or height scan.
"""
from __future__ import annotations
import argparse,hashlib,json,platform
from pathlib import Path
from flint import arb,ctx
import flint

def s(value):return value.str(45,more=True)
def check(condition,message):
 if not condition:raise ArithmeticError(message)

def evaluate(Aint):
 A=arb(Aint);X=arb(1000);b=arb(1)/8;T=arb(1)/2;Y=arb(1);pi=arb.pi()
 v=4*A/X;kappa=1-v*v/6;sigma=1-v*v/2
 M=1+1/(b*X).sqrt();qstar=4*pi*A*kappa*b;B=4*qstar-9-Y
 eta=4*pi*sigma-1/b-T*pi/(4*b*X)
 Q1=pi/8+1/B;Q2=(pi/8)**2+pi/(4*B)+2/(B*B)
 check(v>0 and v<pi/2 and kappa>0,'positive near-boundary shift')
 check(qstar>=1 and 8*qstar>=T and B>0 and eta>0,'uniform nonstationary/Gaussian admissibility')
 check(Q1<1 and Q2<1,'common Qj<=1 for j0,1,2')
 bracket=(4*pi*pi*M*M*b/X.sqrt()+pi*M*b.sqrt()/(2*A*kappa)
          +1/(16*A*A*kappa*kappa*b.sqrt())+6*pi/(X*X.sqrt())
          +3/(4*A*kappa*b.sqrt()*X))
 C=(A-qstar).exp()*bracket/eta
 onset=C/X**(arb(1)/4)
 target=arb('1.1e-9')if Aint==28 else arb('7e-11')
 check(onset<target,'predeclared uniform onset allowance')
 return {'A':Aint,'b_star':'1/8','X':1000,'T':'1/2','Y':1,'orders':[0,1,2],
 'v':s(v),'kappa':s(kappa),'sigma':s(sigma),'ceil_factor_M':s(M),
 'q_star':s(qstar),'B_star':s(B),'eta':s(eta),'Q1_upper':s(Q1.upper()),'Q2_upper':s(Q2.upper()),
 'C_X':s(C),'uniform_bound_at_X':s(onset),'rounded_uniform_allowance':s(target),
 'statement':'For all real x>=1000 and all0<=t<=1/2,|Imz|<=1, physical derivative orders0..2: error/G0(x)<=C_X*x^(-1/4), holding d,m fixed when differentiating.',
 'status':'pass'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('CONSTANT_DISTANCE_CHECK.json'))
 p.add_argument('--bits',type=int,default=256);p.add_argument('--execution-model',default='gpt-6.1-sol');p.add_argument('--execution-effort',default='ultra');a=p.parse_args();ctx.prec=a.bits
 records=[evaluate(28),evaluate(33)]
 pi=arb.pi();L=arb(2000);b=arb(1)/8
 lower_N=((b*L.exp()).sqrt()-1).lower();log10N=(lower_N.log()/arb(10).log()).lower()
 check(log10N>433,'outer-onset explicit-mode lower bound')
 Uconstant=(L/4+(arb(9)/(16*pi*33)).log()/4).lower()
 Ulog=(L/4+(arb(9)/(64*pi*L)).log()/4).lower()
 report={'date':'2026-10-18','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,
 'llm_assistance':'substantial; same-model internal scalar replay','python':platform.python_version(),'python_flint':flint.__version__,'bits':a.bits,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'predeclared_sets':[{'A':28,'b_star':'1/8','X':1000},{'A':33,'b_star':'1/8','X':1000}],
 'records':records,'outer_example':{'log_x':2000,'retained_count_lower_decimal_log10':s(log10N),
 'constant_A33_source_tangent_necessary_U_lower':s(Uconstant),'log_shift_a4_source_tangent_necessary_U_lower':s(Ulog),
 'scope':'explicit mode enumeration and stated monotone-tangent source payment only; no universal complexity lower bound'},'status':'pass'}
 a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
