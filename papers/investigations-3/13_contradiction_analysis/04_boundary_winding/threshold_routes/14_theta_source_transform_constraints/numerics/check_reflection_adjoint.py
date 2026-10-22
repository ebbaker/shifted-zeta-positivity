#!/usr/bin/env python3
"""Bounded reflection/connector audit, 21 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6-astra (Codex), recorded reasoning effort max.
Requires python-flint 0.9.0. See BW14 Note 02 for the analytic proof.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import flint
from flint import arb, acb, ctx


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def show(v):
    return v.str(40, more=True)


def enlarge(v, error):
    e=error.upper()
    return v+acb(arb(0,e),arb(0,e))


def integral(fn, start, end):
    calls=0
    def callback(u, analytic):
        # All callback expressions are entire. No conjugation or branches.
        nonlocal calls
        calls+=1
        return fn(u)
    v=acb.integral(callback,start,end,abs_tol=arb('1e-32'),
                   rel_tol=arb('1e-29'),eval_limit=200000,depth_limit=35)
    require(v.is_finite(),'finite quadrature ball')
    require(v.real.rad()<arb('1e-26') and v.imag.rad()<arb('1e-26'),
            'quadrature radius budget')
    return v,calls


def run(bits):
    ctx.prec=bits
    pi=arb.pi()
    d=pi/16
    c=(4*d).cos()
    i=acb(0,1)
    T,Y=arb(1)/2,arb(1)
    U=arb(1)

    def phi(v,N):
        q=(4*v).exp()
        return sum(((2*(pi*n*n)**2*q*q-3*pi*n*n*q)
                    *(v-pi*n*n*q).exp() for n in range(1,N+1)),acb(0))

    def exterior(N,j,x,shifted):
        total=arb(0)
        for n in range(1,N+1):
            lam=pi*n*n
            if shifted:
                D=4*c*lam*(4*U).exp()-2*T*U-9-Y-j/(U+d)
                require(D>0 and 16*c*lam*(4*U).exp()>2*T,
                        'shifted exterior tangent')
                total+=(2*lam*lam+3*lam)*(U+d)**j * (
                    T*(U*U+d*d)+(9+Y)*U-c*lam*(4*U).exp()-d*x
                    ).exp()/D
            else:
                D=4*lam*(4*U).exp()-2*T*U-9-Y-j/U
                require(D>0 and 16*lam*(4*U).exp()>2*T,
                        'real exterior tangent')
                total+=2*lam*lam*U**j*(T*U*U+(9+Y)*U
                    -lam*(4*U).exp()).exp()/D
        return total.upper()

    cases=[]
    for name,N,t,z in [
        ('one_mode_real',1,acb(arb(1)/10),acb(30)),
        ('two_modes_complex',2,acb(arb(1)/10,arb(1)/20),
                              acb(30,arb(1)/2))]:
        require(abs(t)<T and abs(z.imag)<Y,'case within tail domain')
        row={'name':name,'N':N,'t':show(t),'z':show(z),'jets':[]}
        for j in (0,1):
            def real_core(u):
                trig=(z*u).cos() if j==0 else -u*(z*u).sin()
                return (t*u*u).exp()*phi(u,N)*trig
            def paired_core(u):
                vp,vm=u+i*d,u-i*d
                return ((i*vp)**j*(t*vp*vp+i*z*vp).exp()*phi(vp,N)
                       +(-i*vm)**j*(t*vm*vm-i*z*vm).exp()*phi(vm,N))/2
            def connector_core(s):
                return i/2*(-s)**j*(-t*s*s-z*s).exp()*(phi(i*s,N)-phi(-i*s,N))
            h,hcalls=integral(real_core,0,U)
            p,pcalls=integral(paired_core,0,U)
            edge,ecalls=integral(connector_core,0,d)
            eh,ep=exterior(N,j,z.real,False),exterior(N,j,z.real,True)
            h,p=enlarge(h,eh),enlarge(p,ep)
            residual=h-p-edge
            require(residual.contains(0),'H_N=P_N+C_N identity')
            require(edge.abs_lower()>0,'finite connector is nonzero')
            require(not (h-p).contains(0),'omitting connector changes the jet')
            require(residual.abs_upper()<arb('1e-25'),'identity resolution')
            row['jets'].append({'j':j,'H_N':show(h),'P_N':show(p),
                'C_N':show(edge),'identity_residual':show(residual),
                'real_exterior_upper':show(eh),'paired_exterior_upper':show(ep),
                'quadrature_callbacks':{'real':hcalls,'paired':pcalls,'connector':ecalls}})
        cases.append(row)

    # Entire, positive, reflected super-Gaussian control from Inv. 22.
    # Set its positive normalization factor c=1; zero multiplicity is unchanged.
    # At T*=1/4 the heat weight cancels, leaving g and transform F(1+cos(4x)).
    x=pi/4
    V=arb(8)
    require(6*d*d/(V-4)**2 < arb(1)/2,'quartic strip-tail condition')
    def g(v):
        return (-v**4).exp()+((-(v-4)**4).exp()+(-(v+4)**4).exp())/2
    control=[]
    for j in (0,1,2):
        def paired_control(u):
            vp,vm=u+i*d,u-i*d
            return ((i*vp)**j*(i*x*vp).exp()*g(vp)
                   +(-i*vm)**j*(-i*x*vm).exp()*g(vm))/2
        v,calls=integral(paired_control,0,V)
        D=2*(V-4)**3-j/(V+d)
        require(D>0,'quartic tail slope')
        tail=(2*(V+d)**j*(-d*x-(V-4)**4/2).exp()/D).upper()
        v=enlarge(v,tail)
        require(v.imag.contains(0),'control real symmetry')
        if j<2:
            require(v.contains(0),'reflected collision jet')
            require(v.abs_upper()<arb('1e-25'),'collision jet resolution')
        else:
            require(v.real>0,'nondegenerate reflected collision')
        control.append({'j':j,'paired_jet':show(v),'exterior_upper':show(tail),
                        'quadrature_callbacks':calls})

    # Complete theta shifted-mode bound, extended to |t|<=T by exp(T*d^2).
    m=5
    lam=pi*m*m
    b=4*c*lam-9-Y
    r=(arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
    require(b>0 and 8*c*lam>=T and r<1,'complete shifted-tail conditions')
    S=(2*lam*lam+3*lam)*(-c*lam).exp()/(1-r)
    K0=(T*d*d).exp()*S/b
    K1=(T*d*d).exp()*S*(d/b+1/(b*b))
    return {'status':'passed','date':'2026-10-21','prepared_for':'Edward Baker',
        'model':'gpt-6-astra','reasoning_effort':'max','precision_bits':bits,
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'frozen_contract':{'shift':'pi/16','finite_theta_U':1,
            'theta_tail_domain':'|t|<=1/2, Re(z)>=0, |Im(z)|<=1',
            'finite_theta_cases':'N=1 real (1/10,30); N=2 complex (1/10+i/20,30+i/2)',
            'control_time':'1/4','control_x':'pi/4','control_U':8,
            'purpose':'boundary-term and matching-control regression, not a theta sign pilot'},
        'finite_theta_connector_checks':cases,
        'reflected_collision_control':{'normalization_factor':1,'jets':control},
        'complete_theta_shifted_mode_constants':{
            'first_omitted_mode':m,'b':show(b),'ratio':show(r),
            'K0_complex_time':show(K0),'K1_complex_time':show(K1),
            'note':'multiply by exp(-d*Re(z)); all n>=5 included; no retained quadrature allowance included'},
        'review':'authoring assistant only; no independent specialist review',
        'scope':'Checks exact connector and existing reflected collision; no new theta exclusion or global claim.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run(args.bits)
    payload=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    print(payload)
