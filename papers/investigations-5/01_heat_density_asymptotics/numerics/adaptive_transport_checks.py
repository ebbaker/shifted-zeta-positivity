#!/usr/bin/env python3
"""Note 16: exact controls and floating evaluations of analytic allowances.

Prepared for Edward Baker, 24 October 2026, with substantial LLM assistance.
Model gpt-6-astra (Codex), actual effort max. Same-assistant implementation.
No theta quadrature, root fitting, interval enclosure or onset certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

from variable_epsilon_identity_checks import Poly, VARIABLES

PI = math.pi
CB = 1/(1-16*math.exp(-3*PI))


def exact_controls():
    t, x, y = VARIABLES
    a, b = x*x-y*y-2*t, 2*x*y
    f = a*a+b*b
    reports = {}
    for label, q in [('constant', Poly(1)), ('time', 1+t*t),
                     ('height_time', 1+t*t+x*x),
                     ('space_time', 1+t*t+x*x+2*y*y)]:
        D, N = f+q, f*(f+q)
        # h*w=(H_zz/H)*w=(A+iB)/N; j is in Note 14's orientation.
        A, B = 2*q*a, -2*q*b
        dxA = A.diff(1)*N-A*N.diff(1)
        dyB = B.diff(2)*N-B*N.diff(2)
        dxB = B.diff(1)*N-B*N.diff(1)
        dyA = A.diff(2)*N-A*N.diff(2)
        correction_re = a*q.diff(1)+b*q.diff(2)
        correction_im = a*q.diff(2)-b*q.diff(1)
        current_re = 4*q*x*f*f - correction_re*f*f + (dxA-dyB)*F(1,2)
        current_im = -4*q*y*f*f - correction_im*f*f + (dxB+dyA)*F(1,2)
        # L_q,t = w (r_t+2 Re h), cleared by f D.
        log_time = D.diff(0)*f-f.diff(0)*D-q.diff(0)*f-4*q*a
        # w_t = w(1-w) (r_t+2 Re h), cleared by D^2.
        w_time = q.diff(0)*D-q*D.diff(0)-q.diff(0)*f-4*q*a
        residuals = {'current_real': current_re, 'current_imag': current_im,
                     'log_time': log_time, 'w_time': w_time}
        reports[label] = {k: p.is_zero() for k,p in residuals.items()}
        assert all(reports[label].values())

    moment_reports = []
    for nodes, weights in [([0,1,3], [1,2,1]),
                           ([1,2,5,7], [2,3,1,4]),
                           ([0,2], [1,1])]:
        total = sum(weights)
        ps = [F(w,total) for w in weights]
        mu = sum(p*u for p,u in zip(ps,nodes))
        eu2 = sum(p*u*u for p,u in zip(ps,nodes))
        pdt = [p*(u*u-eu2) for p,u in zip(ps,nodes)]
        mup = sum(d*u for d,u in zip(pdt,nodes))
        m = {j:sum(p*(u-mu)**j for p,u in zip(ps,nodes)) for j in range(2,6)}
        vp = sum(d*(u-mu)**2 for d,u in zip(pdt,nodes))
        m3p = sum(d*(u-mu)**3 for d,u in zip(pdt,nodes))-3*mup*m[2]
        checks = [mup == 2*mu*m[2]+m[3],
                  vp == 2*mu*m[3]+m[4]-m[2]**2,
                  m3p == 2*mu*(m[4]-3*m[2]**2)+m[5]-4*m[2]*m[3]]
        assert all(checks)
        moment_reports.append({'nodes':nodes,'weights':weights,
                               'three_identities_exact':all(checks)})

    # s=radius^2/q. d[-s/(1+s)^2]/ds=(s-1)/(s+1)^3.
    primitive_num = -x
    primitive_den = (1+x)**2
    derivative_check = primitive_num.diff(1)*primitive_den-primitive_num*primitive_den.diff(1)
    derivative_check -= (x-1)*(x+1)
    assert derivative_check.is_zero()
    primitive_at_one = -F(1,4)
    signed_total = F(0)
    absolute_total = -2*primitive_at_one
    assert signed_total == 0 and absolute_total == F(1,2)
    return {'polynomial_identities': reports, 'polynomial_count':16,
            'moment_controls':moment_reports,'moment_identity_count':9,
            'linear_zero_source':{'signed_total':'0','absolute_total':'1/2',
                'meaning':'Integrals of (1-2w)rho for H=z and spatially constant q; multiply by r_t for the source.',
                'finite_disk_primitive':'-s/(1+s)^2',
                'primitive_derivative_exact':True,
                'scope':'Exact radial integral, not theta data.'}}


def saddle(t):
    fun=lambda u:4*PI*math.exp(4*u)-2*t*u-9
    lo=math.log(t/(8*PI))/4
    hi=max(2., math.log(t+10))
    assert fun(lo)<0
    while fun(hi)<=0: hi*=1.5
    for _ in range(100):
        mid=(lo+hi)/2
        if fun(mid)>0: hi=mid
        else: lo=mid
    L=(lo+hi)/2
    return L,8*t*L-2*t+36


def gauss_tail(p,c,lam,h):
    vals=[math.sqrt(PI)/(2*math.sqrt(c))*math.exp(lam*lam/(4*c))
          *math.erfc(math.sqrt(c)*h-lam/(2*math.sqrt(c)))]
    boundary=math.exp(-c*h*h+lam*h)
    if p: vals.append((boundary+lam*vals[0])/(2*c))
    for m in range(1,p):
        vals.append((h**m*boundary+m*vals[m-1]+lam*vals[m])/(2*c))
    return vals[p]


def finite_allowances(t, ell=10., hy=.75, Y=1., beta=.25):
    L, kap=saddle(t)
    c=1/(4*math.e); d=.25; hh=kap**(1/12)
    qt=lambda u:t*u*u+9*u-PI*math.exp(4*u)
    source_gates=L>=d and kap>=32 and t/kap<=c and qt(L-d)>=qt(0)
    QL=16*math.exp(-3*PI*math.exp(4*(L-d)))
    dL=3/(2*PI)*math.exp(-4*(L-d))+QL/(1-QL)
    ec=math.expm1(4*math.e/3*kap**(-.25))
    ec+=(ec+1)*dL
    def G(p,y): return 2*gauss_tail(p,.5,y/math.sqrt(kap),0)
    def D(p,y):
        logleft=math.log(CB)+(p+1)*math.log(L*math.sqrt(kap))+y*L-c*kap*d*d
        return ec*G(p,y)+2*(CB*gauss_tail(p,c,y/math.sqrt(kap),hh)
                    +gauss_tail(p,.5,y/math.sqrt(kap),hh))+math.exp(logleft)
    zm=math.sqrt(2*PI)-D(0,0)
    row={'t':t,'L':L,'kappa':kap,'source_gates':source_gates,'Z_lower':zm}
    if not source_gates or zm<=0:return row
    def A(p,y):return kap**(-p/2)*(G(p,y)+D(p,y))/zm
    emu=kap**(-.5)*D(1,0)/zm
    ml,mu=L-emu,L+emu
    if ml<=0:return row
    def B(p,y=0):
        if p==0:return math.exp(y*emu)*A(0,y)
        return 2**(p-1)*math.exp(y*emu)*(A(p,y)+emu**p*A(0,y))
    v=A(2,0)
    nu=(D(2,0)+D(0,0))/zm+kap*emu*emu
    fourth=kap**(-2)*(D(4,0)+3*D(0,0))/zm
    fourth+=4*emu*A(3,0)+6*emu**2*A(2,0)+3*emu**4
    fourth+=3*(v+1/kap)*nu/kap
    X=kap**(1/3); Z=math.hypot(X,Y)
    amin=1-v*Z*Z/2
    delta=Z**3*B(3,Y)/(6*amin) if amin>0 else math.inf
    s=4*delta
    R=beta/ml
    gate=amin>0 and s<beta/2 and 2*R<Y-hy and X>ell+2*R
    row.update(mu_lower=ml,mu_upper=mu,mean_error=emu,variance_upper=v,
               variance_scaled_error=nu,fourth_cumulant_upper=fourth,
               X_upper=X,a_min=amin,delta_upper=delta,collar_gates=gate)
    if not gate:return row
    alpha=2*v+B(3)/ml
    vp=2*mu*B(3)+B(4)+v*v
    m3p=2*mu*fourth+B(5)+4*v*B(3)
    E1=X*X*B(3)/2+X**3*(mu*B(3)+B(4))/6
    Rt4=X**4*(2*mu*B(5)+B(6)+v*B(4))/24
    dfloor=ml*amin*math.cos(s)-v*X*math.sin(s)-E1
    row['derivative_floor']=dfloor
    if dfloor<=0:return row
    Ev=(m3p*X**3/6+(alpha*v+vp/2)*X*X*math.sin(s)+Rt4+alpha*X*E1)/dfloor
    V=alpha*X+Ev
    b=amin*(math.exp(-beta)*math.sin(beta)-delta)
    slope=b/(2*R)
    eta=math.sqrt(2*PI)/zm/kap
    aa=eta/slope
    count=2*mu*(ell+R)/PI+2
    W=4*ell*hy*eta*eta/(b*b)+count*PI*aa*aa*math.log1p((2*R/aa)**2)
    logmass=W+count*PI*aa*aa
    Q2=mu*mu*B(0,Y)+2*mu*B(1,Y)+B(2,Y)
    Greg=Q2/b+V*mu/(beta-s)
    I=Greg*W+count*PI*PI*V*aa
    kp=8*L+16*t*L/kap-2
    b1=2*X/kap; b2=2/kap
    b1t=2*X*abs(kp)/kap**2; b2t=2*abs(kp)/kap**2
    rt=2*L*L+3*abs(kp)/kap+X*X*abs(kp)/kap**2
    C=315/256
    psi=C*C/(ell*hy)
    d1=8*C*(6/7)**3/math.sqrt(7)
    grad=math.hypot(d1*C/(ell**2*hy),C*d1/(ell*hy**2))
    lap=8*C*C*(ell**(-3)/hy+ell**(-1)*hy**(-3))
    Kr=lap+2*b1*grad+(b2+b1*b1)*psi
    Krt=2*b1t*grad+(b2t+2*b1*b1t)*psi
    density_bias=Kr*logmass/(4*PI)
    Jbias=(grad+b1*psi)*I/(2*PI)
    time_bias=(Kr*(rt*W+2*I)+Krt*W)/(4*PI)
    div_bias=(lap+b1*grad)*I/(2*PI)
    source=time_bias+div_bias
    forcing=(rt+(b2+b1*b1)/2)*psi*W
    rad=s/ml
    # Component/derivative comparisons against the exact moving mu-clock.
    Jclock=count*C/hy*(Ev*C/ell+alpha*rad*(C/ell+X*d1/ell**2))
    Tclock=count*C/hy*(Ev*d1/ell**2+alpha*rad*(d1/ell**2+X*8*C/ell**3))
    scale=L/kap
    row.update(passed_all_gates=True,alpha_upper=alpha,velocity_remainder=Ev,
        root_speed_upper=V,collar_radius_upper=R,collar_floor=b,
        local_population_upper=count,eta_upper=eta,W_upper=W,logmass_upper=logmass,
        I_upper=I,regulator_density_bias=density_bias,regulator_current_bias=Jbias,
        regulator_time_derivative_bias=time_bias,averaged_source_allowance=source,
        averaged_potential_forcing_allowance=forcing,
        moving_clock_current_error=Jclock+Jbias,
        moving_clock_time_derivative_error=Tclock+time_bias,
        drift_scale_L_over_kappa=scale,
        source_to_drift=source/scale,
        current_error_to_drift=(Jclock+Jbias)/scale,
        time_error_to_drift=(Tclock+time_bias)/scale)
    return row


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    controls=exact_controls()
    rows=[finite_allowances(t) for t in [1e4,1e6,1e9,1e12,1e18,1e24]]
    record={'date':'2026-10-24','prepared_for':'Edward Baker',
       'model':'gpt-6-astra','reasoning_effort':'max',
       'status':'Exact algebraic controls and floating analytic-allowance evaluations; same-assistant checks.',
       'python':platform.python_version(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'dependency_sha256':hashlib.sha256(Path(__file__).with_name('variable_epsilon_identity_checks.py').read_bytes()).hexdigest(),
       'controls':controls,'parameters':{'ell':10,'h':.75,'Y':1,'beta':.25,'regulator_p':1},
       'finite_allowances':rows,
       'limitations':['No interval arithmetic or certified finite onset.',
          'Exponential underflow in negligible tail formulas is ordinary floating evaluation, not exact zero.',
          'No theta source quadrature, acquired roots or trajectory solve.',
          'Moment reference uses complete mu and mu-prime; not an autonomous reduced PDE.',
          'No independent implementation or mathematical review.']}
    args.output.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'polynomial_identities':16,'moment_identities':9,
       'all_exact_controls_pass':True,'finite_rows':[{
       k:r.get(k) for k in ['t','passed_all_gates','source_to_drift',
                             'time_error_to_drift']} for r in rows]}))


if __name__=='__main__':main()
