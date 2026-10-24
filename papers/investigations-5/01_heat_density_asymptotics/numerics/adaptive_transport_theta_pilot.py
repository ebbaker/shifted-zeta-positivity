#!/usr/bin/env python3
"""Floating weak-current/time-derivative checks for Note 16, no root fitting.

Prepared for Edward Baker, 2026-10-24, with substantial LLM assistance.
gpt-6-astra (Codex), actual effort max. Not interval certificates.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss
from two_time_limits_round3 import positive_source

C=315/256


def observe(t, center, source_order, cut, contour_order, height=.6):
    L,kap,u,v,p,logM=positive_source(t,source_order,cut)
    mean_v=float(p@v); mu=L+mean_v
    centered=v-mean_v
    variance=float(p@(centered**2))
    third=float(p@(centered**3))
    mup=2*mu*variance+third
    alpha=mup/mu
    ell=10.
    q,w=leggauss(contour_order)
    corners=[center-ell-1j*height,center+ell-1j*height,
             center+ell+1j*height,center-ell+1j*height]
    integral=np.zeros(3,dtype=complex)
    minf=math.inf
    for a,b in zip(corners,corners[1:]+corners[:1]):
        z=(a+b)/2+(b-a)*q/2; dz=(b-a)*w/2
        phase=z[:,None]*u
        cos,sin=np.cos(phase),np.sin(phase)
        f=cos@p
        f1=-sin@(p*u)
        # f_zz/f = -E(u^2) - f_t/f. The omitted constant has
        # zero integral against either analytic polynomial weight.
        # Retain source covariance before integration to avoid cancellation.
        centered_u2=2*mu*centered+centered**2-variance
        transport_numerator=-cos@(p*centered_u2)
        qz=(z-center)/ell
        P=C/ell*(1-qz*qz)**4
        Pprime=-8*C/ell**2*qz*(1-qz*qz)**3
        integral[0]+=np.sum(P*f1/f*dz)/(2j*math.pi)
        integral[1]+=np.sum(P*transport_numerator/f*dz)/(2j*math.pi)
        integral[2]+=np.sum(Pprime*transport_numerator/f*dz)/(2j*math.pi)
        minf=min(minf,float(abs(f).min()))
    lo=math.floor((center-ell)*mu/math.pi-.5)-1
    hi=math.ceil((center+ell)*mu/math.pi-.5)+1
    roots=(np.arange(lo,hi+1)+.5)*math.pi/mu
    arg=(center-roots)/ell
    inside=abs(arg)<1
    arg=arg[inside]; roots=roots[inside]
    k=C/ell*(1-arg*arg)**4
    kprime=-8*C/ell**2*arg*(1-arg*arg)**3
    clock=np.array([sum(k),-alpha*sum(roots*k),alpha*sum(roots*kprime)])
    continuum=np.array([mu/math.pi,-mup*center/math.pi,mup/math.pi])
    return dict(t=t,x=center,L=L,kappa=kap,mu=mu,muprime=mup,
       source_order=source_order,source_cut=cut,source_theta_modes=8,
       contour_order=contour_order,contour_height=height,
       zero_measure_observables=integral.real.tolist(),
       moving_clock=clock.tolist(),continuum=continuum.tolist(),
       absolute_clock_errors=abs(integral.real-clock).tolist(),
       absolute_continuum_errors=abs(integral.real-continuum).tolist(),
       derivative_clock_error_over_mean=abs(float(integral[2].real-clock[2]))/(mup/math.pi),
       derivative_continuum_error_over_mean=abs(float(integral[2].real-continuum[2]))/(mup/math.pi),
       max_imaginary_residue=float(max(abs(integral.imag))),
       sampled_contour_min_f=minf)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    rows=[]
    for t in [1e6,1e9]:
        L,kap,u,v,p,_=positive_source(t,48,14)
        mu=L+float(p@v)
        X=math.floor(mu*kap**(1/3)/math.pi)*math.pi/mu
        for center in [0.,.8*(X-10),.91*(X-10)]:
            base=observe(t,center,32,12,224)
            source=observe(t,center,48,14,224)
            final=observe(t,center,48,14,320)
            height=observe(t,center,48,14,320,.8)
            def change(a,b):return abs(np.array(a['zero_measure_observables'])-np.array(b['zero_measure_observables'])).tolist()
            final.update(X=X,source_refinement=change(base,source),
                         contour_refinement=change(source,final),
                         contour_height_change=change(final,height))
            rows.append(final)
    record={'date':'2026-10-24','prepared_for':'Edward Baker',
       'model':'gpt-6-astra','reasoning_effort':'max',
       'status':'Floating actual-theta weak observations; same-assistant implementation.',
       'python':platform.python_version(),'numpy':np.__version__,
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'source_dependency_sha256':hashlib.sha256(Path(__file__).with_name('two_time_limits_round3.py').read_bytes()).hexdigest(),
       'parameters':{'ell':10,'observable_order':['zero_intensity','zero_current','zero_intensity_time_derivative'],
                     'transverse_factor':'Multiply each observable by k_h(y); observations are zero-measure coefficients.'},
       'rows':rows,
       'limitations':['No interval source, quadrature or contour-floor enclosure.',
          'Finite Gaussian cutoff and eight theta modes; refinement is diagnostic only.',
          'No actual root finding or finite-epsilon peak quadrature.',
          'Finite-epsilon transfer is analytic in Note 16, not numerically observed.',
          'No independent implementation, closure or trajectory solve.']}
    args.output.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'observations':len(rows),'rows':[{
       k:r[k] for k in ['t','x','derivative_clock_error_over_mean',
                        'derivative_continuum_error_over_mean','contour_refinement']} for r in rows]}))


if __name__=='__main__':main()
