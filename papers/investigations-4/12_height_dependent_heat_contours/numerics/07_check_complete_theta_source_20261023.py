#!/usr/bin/env python3
"""Independent complete-source quadrature checks of the HDC13 finite heat core.

Prepared for Edward Baker, 23 October 2026. Substantial LLM assistance:
gpt-6-astra (Codex), reasoning effort ultra. Stdout JSON unless --output.
These spot checks supplement, and do not replace, the uniform analytic proof.
"""
import argparse,hashlib,json,platform,time
from pathlib import Path
from math import factorial
import flint
from flint import arb,acb,ctx
from hdc13_theta_core import ActualHeatCore,canonical_h0,rec

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    args=ap.parse_args();started=time.monotonic();checks=[]
    def check(name,ok):
        if not ok:raise AssertionError(name)
        checks.append(name)
    core=ActualHeatCore();pi=arb.pi();T=core.T;N=4
    mode_ratio=4*(-pi*(2*N+3)).exp()
    beta_tail=4*pi*(N+1)**2*(-pi*(N+1)**2).exp()/(1-mode_ratio)
    mode_tail=T.exp()*arb(2).cosh()*beta_tail/8
    source_ratio=16*(-3*pi*arb(4).exp()).exp()
    source_den=4*pi*arb(4).exp()-11-2*T
    source_tail=2*pi*pi*(T+11-pi*arb(4).exp()).exp()/source_den/(1-source_ratio)
    check('source_geometric_ratios_less_than_one',mode_ratio<1 and source_ratio<1)
    check('source_tangent_decays',source_den>0 and 2*T<16*pi*arb(4).exp())
    check('target_time_square_inside_paid_source_disk',core.tau.abs_upper()<core.T)
    check('target_spatial_rectangle_inside_radius11',arb(104).sqrt()<11)
    check('source_errors_below_1e-25',all(e<arb('1e-25') for e in core.errors))
    cases=[(acb(26,2),acb(0)),(acb(46,-2),acb(arb(1)/10000)),
           (acb(36,2),acb(arb(1)/10000,arb(1)/10000)),
           (acb(28),acb(-arb(1)/10000,arb(1)/10000))]
    results=[]
    for number,(z,tau) in enumerate(cases):
        def integrand(u,analytic):
            q=(4*u).exp()
            phi=sum(((2*(pi*n*n)**2*q*q-3*pi*n*n*q)*(-pi*n*n*q).exp()
                for n in range(1,N+1)),acb(0))
            return (tau*u*u+u).exp()*phi*(z*u).cos()
        t=time.monotonic()
        integral=acb.integral(integrand,0,1,abs_tol=arb('1e-45'),
            rel_tol=arb('1e-40'),eval_limit=40000,depth_limit=25)
        check('finite_independent_quadrature_'+str(number),integral.is_finite())
        tail=(mode_tail+source_tail).abs_upper()
        full=acb(integral.real+arb(0,tail),integral.imag+arb(0,tail))
        cell=core.cell(z,tau=tau)
        check('complete_quad_overlaps_complete_heat_enclosure_'+str(number),full.overlaps(cell))
        # Point polynomial evaluated two independent algebraic routes.
        poly=core.evaluate_poly(z,tau)
        check('coefficient_horner_overlaps_heat_of_point_jets_'+str(number),
            poly.overlaps(core.point_jets(z,tau=tau)[0]))
        # Derivative coefficients independently versus direct factorial sum.
        for j in range(1,4):
            check('finite_derivative_routes_overlap_'+str(number)+'_'+str(j),
                core.evaluate_poly(z,tau,j).overlaps(core.point_jets(z,j,tau)[j]))
        difference=core.difference_cell(z,tau=tau)
        hzero=core.cell(z,tau=0)
        check('difference_oracle_overlaps_subtracted_source_balls_'+str(number),
            difference.overlaps(cell-hzero))
        if tau==0:
            check('xi_identity_overlaps_independent_full_source_quad',canonical_h0(z).overlaps(full))
        results.append({'z':rec(z),'tau':rec(tau),'independent_full_source':rec(full),
            'heat_oracle':rec(cell),'quadrature_seconds':time.monotonic()-t})
    # The source enclosure on a cell must contain separately enclosed centers
    # up to compatible ball overlap. Dyadic small cells exercise interval jets.
    for i,z in enumerate([acb(26,arb(1,arb(1)/32)),acb(arb(44,arb(1)/32),2),
                          acb(arb(28,arb(1)/32),-2)]):
        values=core.jets(z,3)
        mid=acb(z.real.mid(),z.imag.mid())
        points=core.jets(mid,3)
        for j in range(4):
            check('cell_contains_its_center_enclosure_'+str(i)+'_'+str(j),values[j].contains(points[j]))
    output={'date':'2026-10-23','prepared_for':'Edward Baker','model':'gpt-6-astra (Codex)',
        'reasoning_effort':'ultra','llm_assistance':'Substantial LLM assistance; Arb interval execution and independent analytic review.',
        'checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'core_sha256':hashlib.sha256(Path(__file__).with_name('hdc13_theta_core.py').read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'python_flint_version':flint.__version__,
        'core':core.metadata(),'independent_quadrature':{'modes':N,'u_cutoff':1,
            'omitted_mode_bound':rec(mode_tail),'large_u_bound':rec(source_tail),'cases':results},
        'status':'PASS','assertions_passed':len(checks),'checks':checks,
        'elapsed_seconds':time.monotonic()-started,
        'scope':'Independent complete-source spot checks supplement the uniform heat/Cauchy proof; no roots or zero-count premises are supplied.'}
    data=json.dumps(output,indent=2)+'\n'
    if args.output:args.output.write_text(data)
    else:print(data,end='')
if __name__=='__main__':main()
