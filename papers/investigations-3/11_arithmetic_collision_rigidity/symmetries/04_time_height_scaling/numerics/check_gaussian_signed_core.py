#!/usr/bin/env python3
"""Outward scalar audit of the uniform real Gaussian-window RS payment.

19 October 2026; prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra.
The proof's monotonic endpoint reductions, rather than a parameter scan,
are the hypotheses checked here. See the accompanying Note 02. The finite transforms are diagnostics only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import flint
from flint import arb, acb, ctx
from fractions import Fraction

SOURCE_PINS={'papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex': '620f98be47635b8ebb0ecb6d321238c8caa02d66d8496859c994489981c7b050', 'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md': '7a0de0010327f4469836038e54df471aa227eaacdc83a6ab3dffe5fd218175b1', 'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex': '5e9ea35168b629923bc548f27b591f641a235feb262163177c0041b83a5244c5'}


def out(v): return v.str(40, more=True)
def require(c, s):
    if not c: raise ArithmeticError(s)

def finite_diagnostic(kappa,tfrac):
    """Finite transform diagnostic, not physical Q quadrature or uniform proof."""
    a=arb; pi=a.pi(); i=acb(0,1)
    t=a(tfrac.numerator)/tfrac.denominator
    k=a(kappa.numerator)/kappa.denominator
    L=k/t; x=4*pi*L.exp(); s=(1-i*x)/2
    alpha=1/(2*s)+1/(s-1)+(s/(2*pi)).log()/2
    ap=-1/(2*s*s)-1/(s-1)**2+1/(2*s)
    mt=s.log()+(s-1).log()-s*pi.log()/2+(acb(2*pi).sqrt()/16).log()+(s/2-a('.5'))*(s/2).log()-s/2+t*alpha**2/4
    theta=mt.imag; omega=(alpha*(1+t*ap/2)).real/2
    N=int((L.exp()+t/16).sqrt().floor().unique_fmpz())
    K=N-int((a(N)**(a(3)/4)).floor().unique_fmpz())
    sums={key:{'positive':acb(0),'reflected':acb(0),'mass':a(0)} for key in ('low','intermediate','terminal')}
    frequency_gap=2*omega-a(N).log()/2
    require(frequency_gap>=L/4,'finite actual reflected frequency gap')
    T=(x+t*pi/4)/2
    for n in range(1,N+1):
        ell=a(n).log(); W=(t*ell**2/4-(a('.5')+t*L/4)*ell).exp()
        pos=W*(-4*ell**2).exp()*(i*T*ell).exp()
        neg=W*(-16*(2*omega-ell/2)**2).exp()*(-i*(2*theta+T*ell)).exp()
        key='low' if n<=16 else ('intermediate' if n<=K else 'terminal')
        sums[key]['positive']+=pos; sums[key]['reflected']+=neg; sums[key]['mass']+=W
    total=sum((v['positive']+v['reflected'] for v in sums.values()),acb(0))
    require(abs(total-1)<a('.1'),'finite frozen complete average')
    require(abs(sums['intermediate']['positive'])<a('3.387e-15'),'finite signed intermediate positive channel')
    require(sum((v['mass'] for v in sums.values()),a(0))<5*(k*(4-k)/(16*t)).exp(),'finite complete mass bound')
    return {'t_exact':str(tfrac),'kappa_exact':str(kappa),'L':out(L),'N':N,'K_value_edge':K,
      'heat_phase_retained':True,'theta_exact_model_phase':True,
      'minimum_reflected_frequency':out(frequency_gap),
      'ranges':{key:{item:out(v) for item,v in row.items()} for key,row in sums.items()},
      'frozen_full_line_transform':out(total),'distance_to_one':out(abs(total-1)),
      'scope':'finite frozen explicit model only; physical window and movement are paid by analytic bounds'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    args=p.parse_args()
    require(args.bits>=128,'precision must be at least 128 bits')
    require(args.execution_model.strip() and args.execution_effort.strip(),'actual runtime metadata required')
    ctx.prec=args.bits
    source_hashes={}
    for name,expected in SOURCE_PINS.items():
        path=args.repo/name
        require(path.is_file(),f'missing analytic source: {name}')
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual==expected,f'stale analytic source: {name}')
        source_hashes[name]=actual
    a=arb; pi=a.pi(); L=a(20); t=a('0.05')
    x=4*pi*L.exp(); Y=8*L.sqrt(); xm=x-Y
    xi=Y/x; rho=-(1-xi).log()
    da=rho/2+4/xm**2
    width=Y/(4*pi*(xm/(4*pi)).sqrt())
    require(width<a('.00013'),'continuous cutoff interval width < .00013')
    # Every endpoint floor and the fixed center floor differ by at most one.
    # For a corrected index, |log j-L/2|<1e-4 follows from the center N.
    r=(-(L/2)).exp()
    dlo=-(1-r).log()
    dhi=(1+r+t*(-L).exp()/32).log()
    require(dlo<a('.0001') and dhi<a('.0001'),'jump index log displacement')
    delta=a('.0001')
    jump_log=delta/2+t*delta**2/4+da*(a('0.5')+t*delta/2)
    jump_weight=jump_log.exp()
    require(jump_weight<a('1.001'),'individual jump weight ratio')
    # sum V <= [5 + jump_weight exp(-L/2)] exp((.5+tiny) da) exp(a*/t)
    mass=(5+jump_weight*r)*(a('.500001')*da).exp()
    require(mass<a('5.1'),'complete common AB mass reserve')
    numerator=(2+t*rho)**2/16+a('.626')
    z=numerator/(xm-a('6.66'))
    # exp(z)-1 <= z exp(z), avoiding a subtractive ball cancellation.
    scaled_u=xm*z*z.exp()
    require(scaled_u<a('.9'),'U_n < .9/xminus')
    abratio=2*mass*a('.9')/(4*pi)*(1/(1-xi))*r
    require(abratio<a('.001'),'AB error ratio to exp(-b*/t)')
    # sqrt(L^2+c) <= L+sqrt(c), after which (3L+C)e^-L decreases.
    cextra=(3*(L+rho+pi/2)+a('10.44'))/(xm-12)
    clog=rho/2+a('2.48')/(22000-a('.125'))+cextra
    cratio=clog.exp()
    require(cratio<a('1.001'),'C error ratio to exp(-b*/t)')
    etaratio=abratio+cratio+2*jump_weight
    require(etaratio<a('3.1'),'complete eta ratio')
    # exp(a*/t)/x is maximized at kappa=1,t=1/20.
    mass_over_x=(a('3.75')).exp()/xm
    replacement=a('17.6')*mass_over_x
    require(replacement<a('.000000123'),'exact-to-leading scalar replacement')
    amplitude_rate=a('.250001')/xm
    first_abs_moment=8/pi.sqrt(); second_moment=a(32)
    movement=5*a('3.75').exp()*(2*(amplitude_rate*Y).exp()*amplitude_rate*first_abs_moment+amplitude_rate*second_moment)
    require(movement<a('.000000359'),'full two-channel movement')
    tails=10*(-a('16.25')).exp()/(pi*L).sqrt()
    require(tails<a('.000000111'),'frozen two-channel Gaussian tail')
    rs=a('3.1')*(-a('6.25')).exp()
    # Independent exact Gaussian-transform payments. These extend only the
    # frozen finite polynomial, never the physical Q outside its window.
    reserve=a('1.000001'); power=a(5)/8
    low=sum((a(n)**(-power)*(-4*a(n).log()**2).exp() for n in range(2,17)),a(0))
    log17=a(17).log()
    core=a(17)**(-power)*(-4*log17**2).exp()+(a(9)/1024).exp()*pi.sqrt()/4*(2*log17-a(3)/32).erfc()
    floor_reserve=(t*t*L/(128*L.exp())).exp()
    require(floor_reserve<reserve,'coefficient envelope floor reserve')
    leakage=reserve*(low+core)
    require(leakage<a('.099125'),'nonleading positive-channel leakage')
    require(reserve*core<a('3.387e-15'),'intermediate positive-channel leakage')
    # Note proves the exact frequency gap nu_n>=L/4. A weaker gap is
    # checked as well, so no machine sign at a floor endpoint is needed.
    reflected=5*(3*L/16).exp()*(-16*(L/4-a('1e-9'))**2).exp()
    require(reflected<a('4.1e-172'),'all reflected frozen modes')
    exacttail=10*(3*L/16).exp()*L.sqrt().erfc()
    require(exacttail<a('1.08e-7'),'sharper exact Gaussian tail')
    coarse_movement=5*(3*L/16).exp()/x*(first_abs_moment+second_moment)
    require(coarse_movement<a('1.274e-6'),'coarse complete two-channel movement')
    mid=reserve*core+reflected+exacttail+coarse_movement
    complete=leakage+reflected+exacttail+coarse_movement+replacement+rs
    require(mid<a('1.5e-6'),'uniform moving intermediate signed average')
    require(complete<a('.11'),'complete physical averaged value radius')
    energy=(1-a('.11'))**2/4
    require(energy>a('.198'),'weighted Q/2 energy floor')
    # Minimal finite diagnostics, fixed before computation. Retain all
    # phases and every n through N, separating low/core/terminal channels.
    diagnostics=[finite_diagnostic(Fraction(1),Fraction(1,20)),
                 finite_diagnostic(Fraction(1),Fraction(1,21)),
                 finite_diagnostic(Fraction(21,20),Fraction(1,20))]
    record={
      'schema':'S04_T2_GAUSSIAN_CORE_V1',
      'date':'2026-10-19','prepared_for':'Edward Baker',
      'authoring_model':'gpt-6.1-sol','authoring_effort':'ultra',
      'actual_model':args.execution_model,'actual_effort':args.execution_effort,
      'llm_assistance':'substantial; same-model analytic derivation and check',
      'status':'outward scalar audit of in-note uniform monotonic reductions; no scan and no pointwise exclusion',
      'python':platform.python_version(),'python_flint':flint.__version__,
      'precision_bits':args.bits,'source_sha256':source_hashes,
      'finite_frozen_transform_diagnostics':diagnostics,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'domain':{'kappa':['1','2'],'t':['0 excluded','1/20'],'L':'kappa/t >= 20','x':'4*pi*exp(L)','h':'8','Y':'8*sqrt(L)','fixed_cutoff':'floor(sqrt(exp(L)+t/16))'},
      'monotonic_reductions':[
        'sqrt(L)*exp(-L) decreases for L>=20',
        'exp(-L/2) decreases for L>=20',
        '(3L+C)*exp(-L) decreases for L>=20 and C>0',
        'b*/t=L*(kappa+4)/16 >= 6.25',
        'd*/t=L*(kappa+12)/16 >=16.25',
        'a*/t-L=-d*/t',
        't<=1/20, kappa<=2 independently bound small coefficient corrections'],
      'bounds':{k:out(v) for k,v in {
        'x_min':x,'Y_at_min':Y,'Y_over_x_max':xi,'log_q_shift_max':rho,
        'alpha_min_deficit_max':da,'continuous_cutoff_width':width,
        'jump_log_weight_excess':jump_log,'jump_weight_ratio':jump_weight,
        'mass_ratio_to_exp_a':mass,'scaled_U':scaled_u,
        'AB_ratio_to_exp_minus_b':abratio,'C_ratio_to_exp_minus_b':cratio,
        'complete_eta_ratio_to_exp_minus_b':etaratio,
        'eta_chosen_uniform_max':rs,'model_replacement_max':replacement,
        'full_two_channel_movement_max':movement,
        'frozen_two_channel_gaussian_tail_max':tails,
        'combined_nonleakage_error':rs+replacement+movement+tails,
        'low_positive_envelope':low,'intermediate_positive_envelope':core,
        'floor_coefficient_reserve':floor_reserve,
        'complete_nonleading_positive_payment':leakage,
        'reflected_frozen_payment':reflected,'exact_two_channel_tail':exacttail,
        'coarse_moving_model_payment':coarse_movement,
        'moving_intermediate_radius':mid,'complete_physical_radius':complete,
        'reported_complete_radius':a('.11'),'weighted_Q_over_2_energy_floor':energy,
        'absolute_model_payment_at_opening':10*(a('3.75')).exp()}.items()},
      'disclosures':{
        'source':'complete published Polymath RS real-axis majorants with local normalization/reflection convention',
        'cutoff':'one explicitly paid possible natural-to-center jump on the whole physical window',
        'source_quadrature':'none; exact frozen Gaussian transforms used for diagnostics',
        'holomorphic_extension':'none claimed; no Cauchy or spatial derivative needed',
        'window':'finite actual-source window; only the frozen explicit finite sum has a Gaussian tail',
        'neighboring_kappa':'old domain theorem not invoked at neighboring points; raw real-axis majorants are bounded directly'}}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'bits':args.bits,'mid_radius':out(mid),'complete_radius':out(complete)}))
if __name__=='__main__':main()
