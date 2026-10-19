#!/usr/bin/env python3
"""Pay the complete independent coherent RS8 edge model error on the fixed pilot.

Prepared for Edward Baker, 19 October 2026, substantial LLM assistance.
Execution model and effort supplied by CLI. This bounds actual edge minus the
retained Gaussian/profile polynomial; it is not the complete H residual.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, platform
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
COHERENT=INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
HIERARCHY=INV/'symmetries/03_normalized_jet_rotation/numerics/check_rs_edge_hierarchy.py'

def interval(lo,hi):
    lo,hi=arb(lo),arb(hi)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def output(v):return v.str(45,more=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def trim(poly):
    poly=list(poly)
    while poly and not poly[-1]:poly.pop()
    return poly

def add(*ps):
    q=[F(0)]*max([len(p) for p in ps]+[0])
    for p in ps:
        for j,v in enumerate(p):q[j]+=v
    return trim(q)
def scale(p,c):return trim([v*c for v in p])
def times_linear(p,c0,c1):
    return add([c0*v for v in p],[F(0)]+[c1*v for v in p])
def coefficients(order):
    d={(0,0):[F(1)]};get=lambda n,k:d.get((n,k),[])
    for n in range(1,order+1):
        for k in range(3*n//2+1):
            m=3*n-2*k
            if m:
                d[n,k]=add(scale(get(n-1,k),F(1,4*m)),
                    times_linear(get(n-1,k-1),F(1,2*m),F(-1,m)),
                    scale(get(n-1,k-2),F(-m-1)))
            else:
                d[n,k]=add(*(scale(get(n,j),-(-1)**(k-j)*F(
                    math.factorial(2*k-2*j),math.factorial(k-j))) for j in range(k)))
    return d

def cr_component(repo,bits):
    # Guard bits are explicit: high-order point Taylor coefficients of the
    # removable profile exhibit cancellation that is irrelevant to parameters.
    pi=arb.pi();ii=acb(0,1);K=8;J=96
    X=interval(998,1002);t=interval('.01','.2');Y=arb(0,1)
    T=X/2+pi*t/8;Tlo=T.lower();Thi=T.upper()
    # Stable enclosure of principal sqrt((T+i eta)/(2pi)), |eta|<=1/2.
    amin=(Tlo/(2*pi)).sqrt()
    amax=(((Thi**2+arb(1)/4).sqrt()+Thi)/(4*pi)).sqrt()
    avec=acb(interval(amin,amax),arb(0,(1/(8*pi*amin)).upper()))
    p=17-2*avec
    center=acb(-arb(21)/25);R=arb(1)/4;h=p-center;q=h.abs_upper()/R
    if not q<arb('.09'):raise ArithmeticError('profile Taylor domain')
    def profile(w):
        return ((ii*pi*(w*w/2+arb(3)/8)).exp()
                -ii*arb(2).sqrt()*(pi*w/2).cos())/(2*(pi*w).cos())
    # On |p+21/25|<=1/4, Re p in[-1.09,-.59], |Im p|<=.25.
    # |cos(pi p)| >= sin(.09pi), numerator <=exp(1.09pi/4)+sqrt2 cosh(pi/8).
    M=((arb('1.09')*pi/4).exp()+arb(2).sqrt()*(pi/8).cosh())/(2*(arb('.09')*pi).sin())
    if not M<10:raise ArithmeticError('Cauchy profile maximum')
    pc=profile(acb_series([center,acb(1)],J+3*K+1))
    derivatives=[];tails=[]
    for k in range(3*K+2):
        total=sum((math.factorial(j+k)*pc[j+k]/math.factorial(j)*h**j
                    for j in range(J)),acb(0))
        ratio=q*(1+arb(k)/(J+1))
        tail=10*math.factorial(k)*R**(-k)*math.comb(J+k,k)*q**J/(1-ratio)
        total=acb(arb(total.real.mid(),(total.real.rad()+tail).upper()),
                  arb(total.imag.mid(),(total.imag.rad()+tail).upper()))
        derivatives.append(total);tails.append(tail)
    uabs=arb(1)+10*arb('.2').sqrt()
    u=acb(interval(-uabs+1,uabs)) # [1/2-sqrt(.2)10-1/2,1/2+sqrt(.2)10+1/2]
    d=coefficients(K)
    def peval(poly,z):
        val=acb(0)
        for v in reversed(poly):val=val*z+arb(v.numerator)/v.denominator
        return val
    C=[];Cp=[]
    for n in range(K+1):
        C.append(sum(((pi/(2*ii))**j*peval(d[n,j],u)*derivatives[3*n-2*j]
                     for j in range(3*n//2+1)),acb(0))/pi**(2*n))
        Cp.append(sum(((pi/(2*ii))**j*peval(d[n,j],u)*derivatives[3*n-2*j+1]
                     for j in range(3*n//2+1)),acb(0))/pi**(2*n))
    bracket=((Cp[K]/(2*pi)+(K-1+u)*C[K-1]/(4*pi))*avec**(-K-1)
                 +(K+u)*C[K]*avec**(-K-2)/(4*pi))
    B=bracket.abs_upper()
    # Independently paid exact gamma prefactor exp eta at every CR path point.
    # Segment has |Im s|>=Tlo, |Re s|<=uabs+1/2.
    argmax=pi/2+((uabs+arb(1)/2)/Tlo).atan()
    sec4=(1/(argmax/2).cos())**4
    if not sec4<arb('4.2'):raise ArithmeticError('Stirling sector')
    stirling=1/(6*Tlo)+arb('4.2')/(45*Tlo**3)
    ap=1/(2*Tlo)+arb(3)/(2*Tlo**2)
    eta=stirling+3*uabs/(2*Tlo)+ap*uabs**2/2
    # Symmetric A vertical modulus variation. b=(log A)_z.
    def alpha(s):return 1/(2*s)+1/(s-1)+(s/(2*pi)).log()/2
    def alphap(s):return -1/(2*s*s)-1/((s-1)*(s-1))+1/(2*s)
    z=acb(X,Y);s=(1-ii*z)/2
    def mtp(w):return alpha(w)*(1+t*alphap(w)/2)
    b=-ii*(mtp(s)-mtp(1-s))/4
    normalizer_cost=b.imag.abs_upper().exp()
    # W_real exactly equals sqrt(pi)/4 exp(-pi X/8-pi²t/64)/A(X,t).
    ar=(1+X*X).log()/4-(4*pi).log()/2-1/(1+X*X)
    ai=X.atan()/2-3*X/(1+X*X)
    W=8*pi**(arb(1)/4)*(1+X*X)**(-arb(7)/8)*(arb(1)/4
        -X*(1/X).atan()/4-t*(pi*pi/64+(ar*ar-ai*ai)/4)).exp()
    # Both reflected channels. Exact M0(i tau)U identity cancels the
    # enormous gamma exponential against A before interval evaluation.
    taumod=(Thi**2+arb(1)/4).sqrt()
    tauplusimod=(Thi**2+arb(9)/4).sqrt()
    physical_prefactor=(W.abs_upper()*taumod.sqrt()*tauplusimod*normalizer_cost)
    value_payment=physical_prefactor*eta.exp()*B/2
    # Whole-Gaussian polynomial majorant for a separate approximate-tail proof.
    major=arb(0)
    for n in range(K+1):
        for j in range(3*n//2+1):
            coeffsum=sum(abs(v) for v in d[n,j])
            coeffsum=arb(coeffsum.numerator)/coeffsum.denominator
            if len(d[n,j])-1>n:raise ArithmeticError('polynomial degree')
            major+=coeffsum*derivatives[3*n-2*j].abs_upper()*(pi/2)**j/(pi**(2*n)*amin**n)
    if not value_payment<arb('2e-8'):raise ArithmeticError('CR payment threshold')
    record={'requested_bits':bits,'working_bits':ctx.prec,'K':K,
       'physical_disk_radius':'1','gaussian_interval':['-10','10'],
       'tube':{'real_z':['998','1002'],'imag_z':['-1','1'],'t':['.01','.2']},
       'tau_real':output(T),'a_enclosure':output(avec),'profile_p':output(p),
       'profile_taylor':{'center':'-21/25','Cauchy_radius':'1/4',
           'Cauchy_maximum_bound':output(M),'used_maximum':'10','terms_per_derivative':J,
           'highest_derivative':3*K+1,'q':output(q),
           'largest_derivative_tail':output(max(tails))},
       'exact_coefficient_recurrence':'Fractions over Q[u], evaluated by Horner; degree d[n,k]<=n checked',
       'endpoint_bracket':output(B),'eta_absolute_bound':output(eta),
       'eta_exp_bound':output(eta.exp()),'normalizer_vertical_cost':output(normalizer_cost),
       'both_channel_physical_prefactor':output(physical_prefactor),
       'both_channel_normalized_CR_value_payment':output(value_payment),
       'approximate_tail_polynomial_majorant':{
           'formula':'|sum_(k=0)^8 Ck(p,u)/a^k| <= C*(1+|u|)^8',
           'C':output(major),'domain':'tau.real in pilot tube; |tau.imag|<=1/2; u real arbitrary'},
       'scope':'Only central finite CR mismatch, uniform on complex physical radius1 tube. Add real RS8 and exact Gaussian tails. Cauchy may be applied only to the combined holomorphic exact-minus-coherent error.'}

    return record,physical_prefactor,value_payment,normalizer_cost,major

MODEL=INV/'symmetries/03_normalized_jet_rotation/numerics/estimate_arithmetic_residual_increment.py'


def real_central_component():
    """Real-tau Proposition 6.2 remainder, with exact gamma factor paid."""
    pi=arb.pi();d=arb(496);tmax=arb(1)/5
    amin=(arb(499)/(2*pi)).sqrt()
    negative_margin=8-10*tmax.sqrt()-2
    if not negative_margin>0:raise ArithmeticError('negative-u RS order condition')
    def gaussian(c):
        den=1-tmax/d
        return ((2/d+c+tmax*(c+2/d)**2/(4*den)).exp()/den.sqrt())
    base=(arb(9)/2).gamma()*(arb(11)/10/amin)**9
    mean=gaussian(3*arb(2).log()/2)/7+gaussian(arb(0))/2
    central=base*mean
    if not central<arb('7.21e-8'):raise ArithmeticError('central real RS remainder')
    return {'K':8,'gaussian_interval':['-10','10'],
      'printed_sigma_range':['0','1'],'tau_safe_range':['499','502'],
      'negative_u_order_margin':output(negative_margin),
      'exact_prefactor_formula':'abs(M(u+i*tau)*a^(-u))/abs(M0(i*tau)) <= exp((u^2+1)/(tau-3))',
      'coefficient_base':output(base),'full_gaussian_mean_bound':output(mean),
      'one_channel_before_external_heat_shift_M0_units':output(central),
      'primary_input':'Polymath 2019 Proposition 6.2 (56)-(57); gamma prefactor independently derived from Lemma 5.1(v)'},central


def exact_tail_component(vertical_cost):
    """Actual fixed RS contour tails, paid against actual complex A(z,t)."""
    pi=arb.pi();cross=arb(17)/2;tmax=arb(1)/5
    Tlo=arb(499);Thi=arb(502)
    Lmax=Thi/cross-2*pi*cross
    C=(Lmax*Lmax/(4*pi)).upper()
    amin=(Tlo/(2*pi)).sqrt();amax=(Thi/(2*pi)).sqrt()
    log_ratio=max(abs((cross/amin).log()).upper(),abs((cross/amax).log()).upper())
    linear=log_ratio+arb(3)/(2*Tlo)
    quadratic=1/(pi*cross*cross)+1/(4*(Tlo-3))
    base=arb(2).sqrt()*(C+1/(6*(Tlo-arb('0.66')))).exp()
    if not (C<3 and log_ratio<arb('.051') and linear<arb('.055')
            and quadratic<arb('.005') and base<30):
        raise ArithmeticError('fixed contour exact tail constants')
    if not (arb('.055')*tmax.sqrt()<arb('.025')
            and 2*arb('.005')*tmax<arb('.003')):
        raise ArithmeticError('Gaussian tail exponent')
    V=arb(10);ga=arb('.997');be=arb('.025')
    tail=60*arb('.065').exp()/pi.sqrt()*(-ga*V*V+be*V).exp()/(2*ga*V-be)
    if not tail<arb('8e-43'):raise ArithmeticError('exact Gaussian tail')
    # At each actual real X, compare M0(i*tau) with A(X,t). The horizontal
    # and vertical offset to (1+iX)/2 is .5-i*pi*t/8. Then pay A(X)/A(X+iy).
    delta=(arb(1)/4+(pi*tmax/8)**2).sqrt()
    ratio=(arb('2.4')*delta).exp()
    if not ratio<4:raise ArithmeticError('real normalizer ratio')
    if not vertical_cost<arb('1.000522'):raise ArithmeticError('complex A variation')
    if not (tmax*pi*pi/64).exp()<arb('1.04'):raise ArithmeticError('heat shift scalar')
    payment=2*4*vertical_cost*arb('1.04')*tail
    if not payment<arb('1.4e-41'):raise ArithmeticError('two-channel exact tail payment')
    return {'contour_crossing':'17/2','gaussian_cutoff':'10',
      'phase_constant':output(C),'log_radius_ratio_constant':output(log_ratio),
      'combined_linear_sigma':output(linear),'combined_quadratic_sigma':output(quadratic),
      'combined_base':output(base),'per_channel_M0_units':output(tail),
      'M0_over_A_at_same_real_X':output(ratio),
      'actual_complex_A_vertical_cost':output(vertical_cost),
      'both_channel_actual_A_payment':output(payment),
      'proof':'Exact contour denominator >=2; quadratic phase and logarithmic radius bounds, followed by a Mills bound. No RS expansion or source H data on the tails.'},payment


def model_conversion_component(polynomial_majorant):
    """Pay Gaussian/profile polynomial conversion and retained tails."""
    from math import factorial,comb
    if not polynomial_majorant<arb(".473"):
        raise ArithmeticError("retained RS polynomial majorant")
    pi=arb.pi();U=arb('16.5');bmin=arb(499);zmin=bmin-U;R=arb(16);t=arb('.2');wmax=10*t.sqrt();K=8
    # Exact eta and its explicit log/J24, Stirling/S3 approximant on |w|<=16.
    q=U/bmin;q1=U/bmin
    logtail=((arb(503)+U+1)/2)*q**25/(25*(1-q))+q1**25/(25*(1-q1))
    argmax=pi/2+(arb(17)/zmin).atan()
    sec4=(1/(argmax/2).cos())**4;sec8=sec4*sec4
    assert sec8<20
    stirling_eta_tail=arb(8)/105*sec8/zmin**7
    eta_model_error=(logtail+stirling_eta_tail).upper()
    eta_bound=(1/(6*(zmin-arb('.66')))+arb(3)*U/(2*bmin)+(1/(2*zmin)+arb(3)/(2*zmin*zmin))*U*U/2).upper()
    assert eta_bound+eta_model_error<arb('.2')
    M=arb('1.3');assert (eta_bound+eta_model_error).exp()<M
    # Central mean error, using full Gaussian moment to dominate central integral.
    C=arb('.473');central_S=C*(1+arb('.5')+wmax)**8
    mom13=t**(arb(13)/2)*arb(7).gamma()/pi.sqrt()
    trunc=M*mom13/R**13/(1-wmax/R)
    eta_exp_error=eta_model_error*arb('.2').exp()
    central_error=(trunc+eta_exp_error)*central_S
    # True profile F versus degree120 Taylor polynomial, derivative tails through26.
    # Coherence agent independently proves M_F=10 on |p+21/25|<=1/4 and q_p<.09.
    qp=arb('.09');Rp=arb(1)/4;profiletails=[]
    for n in range(27):
        ratio=qp*arb(122)/(122-n)
        tail=10*factorial(n)*Rp**(-n)*comb(121,n)*qp**(121-n)/(1-ratio)
        profiletails.append(tail)
    D=max(profiletails)
    # Exact recurrence coefficient l1 sums with all profile derivatives replaced by1.
    def trim(p):
     while p and not p[-1]:p.pop()
     return p
    def add(*ps):
     a=[F(0)]*max([len(p)for p in ps]+[0])
     for p in ps:
      for j,v in enumerate(p):a[j]+=v
     return trim(a)
    def scale(p,c):return trim([v*c for v in p])
    def mul(p,q):
     a=[F(0)]*(len(p)+len(q))
     for j,c in enumerate(p):
      for k,d in enumerate(q):a[j+k]+=c*d
     return trim(a)
    d={(0,0):[F(1)]};get=lambda n,k:d.get((n,k),[])
    for n in range(1,9):
     for k in range(3*n//2+1):
      m=3*n-2*k
      if m:d[n,k]=add(scale(get(n-1,k),F(1,4*m)),mul([F(1,2*m),F(-1,m)],get(n-1,k-1)),scale(get(n-1,k-2),-m-1))
      else:d[n,k]=add(*(scale(get(n,j),-(-1)**(k-j)*F(factorial(2*k-2*j),factorial(k-j)))for j in range(k)))
    amin=(bmin/(2*pi)).sqrt();coeffmajor=arb(0)
    for n in range(9):
     for j in range(3*n//2+1):
      c=sum(abs(v)for v in d[n,j]);c=arb(c.numerator)/c.denominator
      coeffmajor+=c*(pi/2)**j/(pi**(2*n)*amin**n)
    # FullGaussian expectation of polynomial coefficient majorant P12*S8/profiletail.
    beta=t.sqrt();alpha=beta/R
    major_mean=arb(0)
    for j in range(13):
     for k in range(9):
      moment=arb(j+k+1)/2
      moment=moment.gamma()/pi.sqrt()
      major_mean+=M*alpha**j*comb(8,k)*arb('1.5')**(8-k)*beta**k*moment
    # The exact discrepancy subtracts F, while the model subtracts F_hat.
    # Pay that retained-Chat profile difference in addition to the integral.
    profile_error=D*coeffmajor*major_mean+profiletails[0]
    if not polynomial_majorant+D*coeffmajor<arb('.473'):
        raise ArithmeticError('retained profile polynomial tail majorant')
    # Entire polynomial Gaussian tail outside10; geometric coefficient bound gives
    # |P12|<=13M(1+alpha|v|)^12 and |S8|<=C(1.5+beta|v|)^8.
    V=arb(10)
    log_slope=(12*alpha/(1+alpha*V)+8*beta/(arb('1.5')+beta*V)-2*V).upper()
    assert log_slope< -19
    poly_tail=(2*13*M*C/pi.sqrt()*(1+alpha*V)**12*(arb('1.5')+beta*V)**8*(-V*V).exp()/19).upper()
    # Actual complex normalizer: bothchannel prefactor already includes heatshift.
    pref=arb('.667289')
    combined=(pref*(central_error+profile_error+poly_tail)).upper()
    assert combined<arb('1e-11')
    record={'precision_bits':ctx.prec,'eta_domain':'|u-.5|<=16; real tau in[499,502]; |Imtau|<=.5','eta_bound':str(eta_bound),'J24_log_tail':str(logtail),'S3_loggamma_tail':str(stirling_eta_tail),'eta_approximant_error':str(eta_model_error),'Cauchy_exp_maximum':'1.3','gaussian_absolute_13th_moment':str(mom13),'central_g_Taylor12_mean_error':str(trunc),'central_S8_majorant':str(central_S),'central_weighted_error_before_prefactor':str(central_error),'profile_degree120_max_derivative_error_0_to26':str(D),'profile_recurrence_coefficient_majorant':str(coeffmajor),'profile_fullGaussian_and_Chat_error':str(profile_error),'subtracted_Chat_profile_error':str(profiletails[0]),'full_polynomial_Gaussian_tail_outside10':str(poly_tail),'bothchannel_actual_complex_normalizer_prefactor':str(pref),'combined_Q_value_error':str(combined),'safe_Q_value_error':'1e-11','Q_Cauchy_derivative_errors':['1e-11','1e-11','2e-11'],'scope':'Approximation payment only: central coherent gamma replaced by J24/S3/P12, profile degree120, entire polynomial Gaussian tails. Add central real RS8, CR mismatch and exact edge Gaussian tails before Cauchy.'}
    return record,combined


def run(repo,bits):
    """Return the complete normalized edge model error and Cauchy jet caps."""
    ctx.prec=bits+512;ctx.cap=130
    cr,pref,cr_pay,vertical,major=cr_component(repo,bits)
    real,central=real_central_component()
    tail,tail_pay=exact_tail_component(vertical)
    model,model_pay=model_conversion_component(major)
    real_pay=pref*central
    complete=real_pay+cr_pay+tail_pay+model_pay
    if not (pref<arb('.667289') and cr_pay<arb('5.529e-9')):
        raise ArithmeticError('declared normalization/CR caps')
    if not complete<arb('6e-8'):raise ArithmeticError('complete normalized edge cap')
    return {'requested_bits':bits,'working_bits':ctx.prec,
      'physical_disk_radius':'1','pilot':{'t':['.01','.2'],'x':['999','1001'],'N':8},
      'central_real_component':real,'CR_component':cr,'exact_tail_component':tail,
      'both_channel_normalized_real_RS_payment':output(real_pay),
      'both_channel_normalized_CR_payment':output(cr_pay),
      'both_channel_normalized_exact_tail_payment':output(tail_pay),
      'model_conversion_component':model,
      'both_channel_normalized_retained_model_conversion_payment':output(model_pay),
      'both_channel_normalized_retained_model_conversion_cap':'1e-11',
      'model_conversion_cap_basis':'Computed analytic J24/S3/P12 Gaussian and degree120 profile conversion, including the retained full-polynomial Gaussian tails; see the complete-edge note and its same-model audit.',
      'both_channel_normalized_complete_edge_model_error':output(complete),
      'normalized_value_cap':'6e-8','normalized_first_x_cap':'6e-8',
      'normalized_second_x_cap':'1.2e-7',
      'derivative_payment':'Cauchy on the holomorphic exact-minus-polynomial normalized error, radius1 in physical x. First factor1, second factor2.',
      'scope':'Actual complete reflected RS heat edge minus the declared retained Gaussian/profile polynomial approximation, divided by actual A(z,t). This is not the full H residual: the retained signed finite-mode and edge corrections remain to be evaluated.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--bits',nargs='+',type=int,default=[192,256])
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    p.add_argument('--model-script',type=Path,
        help='Staging override; normal lookup is the repository-relative arithmetic estimator path.')
    a=p.parse_args();repo=a.repo.resolve()
    model_path=(a.model_script.resolve() if a.model_script else repo/MODEL)
    if not model_path.is_file():raise FileNotFoundError(f'Retained model script is absent: {model_path}')
    result={'date':'2026-10-19','prepared_for':'Edward Baker',
      'llm_assistance':'substantial; internal same-model derivation and review',
      'actual_model':a.execution_model,'actual_effort':a.execution_effort,
      'python':platform.python_version(),'python_flint':flint.__version__,
      'script_sha256':sha(__file__),
      'source_sha256':{str(v):sha(repo/v) for v in [COHERENT,HIERARCHY]},
      'retained_model':{'repository_relative_path':str(MODEL),
        'sha256':sha(model_path),'staging_override_used':bool(a.model_script)},
      'primary_sources':['https://arxiv.org/html/1904.12438v2#S6.SS2',
        'https://arxiv.org/html/2201.00342','https://dlmf.nist.gov/5.11#ii'],
      'source_theta_taylor_data_used':False,'source_H_values_used':False,
      'runs':[run(repo,b) for b in a.bits]}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),
      'complete_error_payments':[r['both_channel_normalized_complete_edge_model_error'] for r in result['runs']],
      'normalized_value_cap':'6e-8','normalized_first_x_cap':'6e-8','normalized_second_x_cap':'1.2e-7'}))

if __name__=='__main__':main()
