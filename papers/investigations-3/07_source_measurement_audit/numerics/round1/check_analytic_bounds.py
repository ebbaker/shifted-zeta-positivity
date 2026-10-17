#!/usr/bin/env python3
"""Finite interval checks for the analytic bound and physical normalization.

17 October 2026; prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, reasoning effort ultra. The contour shift,
infinite-sum majorants and endpoint lemmas are analytic arguments in Note 02.
"""
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb,acb,acb_series,ctx

def bs(v):return v.str(65,more=True)

def main(evaluation,output):
    ctx.prec=448;ctx.cap=2
    pi=arb.pi(); y=pi/16;T=arb(1)/4;c=arb(1)/arb(2).sqrt()
    kappa=8*c*pi-T;ell9=4*c*pi-9;ell5=4*c*pi-5
    assert kappa>0 and ell9<0 and ell5>0
    J09=(pi/kappa).sqrt()*(ell9**2/(4*kappa)).exp()
    J19=(1-ell9*J09)/(2*kappa)
    J05=(pi/kappa).sqrt()/2;J15=1/(2*kappa)
    a2=4*pi
    qa=arb(9)/4*(-5*c*pi).exp();q0=(-5*c*pi).exp()
    assert qa<1 and q0<1 and 2*c*a2>9
    Sa=a2*(-c*a2).exp()/(1-qa);S0=(-c*a2).exp()/(1-q0)
    KHtail=Sa/c+3*S0/(2*c)
    KXtail=(1/(2*c*c)+3/(4*c*c*a2))*S0+y*KHtail
    KH=(-c*pi).exp()*(2*pi*pi*J09+3*pi*J05)+KHtail
    KX=(-c*pi).exp()*(2*pi*pi*(J19+y*J09)+3*pi*(J15+y*J05))+KXtail
    K=(KH*KH+KX*KX).sqrt()
    assert K<arb(6)/5
    raw=json.loads(evaluation.read_text());checks=[]
    for case in raw['cases']:
        t=arb(case['t']);x=arb(case['x']);ss=acb(arb(1)/2,x/2)
        alpha=1/(2*ss)+1/(ss-1)+(ss/(2*pi)).log()/2
        M0=ss*(ss-1)/16*(-ss*pi.log()/2).exp()*(2*pi).sqrt()*((ss/2-acb(1)/2)*(ss/2).log()-ss/2).exp()
        Mt=(t*alpha*alpha/4).exp()*M0
        A=(1+x*x).log()/4-(4*pi).log()/2-1/(1+x*x)
        B=x.atan()/2-3*x/(1+x*x)
        gamma=pi**(arb(1)/4)/(32*(arb(1)/4).exp())*(1+x*x)**(arb(7)/8)*(-x*x.atan()/4+t*(A*A-B*B)/4).exp()
        assert abs(Mt).overlaps(gamma)
        rec={'id':case['id'],'published_carrier_abs':bs(gamma),
             'closed_carrier_formula_overlaps_complex_definition':True}
        if case['t']=='0':
            s=acb_series([ss,acb(0,arb(1)/2)],2)
            xi=s*(s-1)/16*(-s*pi.log()/2).exp()*(s/2).gamma()*s.zeta()
            assert all(xi[j].imag.contains(0) and arb(case['h'][j]).overlaps(xi[j].real) for j in (0,1))
            rec['time_zero_xi_and_derivative_overlap']=True
            rec['xi_jet']=[bs(xi[j].real) for j in (0,1)]
        checks.append(rec)
    out={'schema':'source_measurement_analytic_checks_v1','date':'2026-10-17',
         'prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
         'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'evaluation_sha256':hashlib.sha256(evaluation.read_bytes()).hexdigest(),
         'uniform_domain':'0<=t<=1/4, x>=0',
         'analytic_bound':'||(H,Hx)||_2 <= (6/5) exp(-pi*x/16)',
         'KH_upper_expression':bs(KH),'KX_upper_expression':bs(KX),
         'Kjet_upper_expression':bs(K),'Kjet_less_than_six_fifths':True,
         'checks':checks,
         'scope':'Finite interval checks of displayed constants and normalization; analytic contour and infinite tail arguments are in Note 02.'}
    output.write_text(json.dumps(out,indent=2)+'\n')
    print('KH',KH.str(12),'KX',KX.str(12),'Kjet',K.str(12),'all five physical xi jets checked')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--evaluation',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();main(a.evaluation,a.output)
