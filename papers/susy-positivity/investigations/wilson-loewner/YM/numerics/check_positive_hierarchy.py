#!/usr/bin/env python3
"""Finite controls for the YM positive-hierarchy preliminary analysis.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-24.
Reasoning effort: not exposed; not inferred.
Requires NumPy. Uses finite prescribed backgrounds, NOT a Yang--Mills ensemble.
Floating diagnostics do not constitute interval certificates or continuum proofs.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np

I2 = np.eye(2, dtype=complex)
T = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
              [[1, 0], [0, -1]]], dtype=complex) / 2
WEIGHTS = np.array([0.2, 0.3, 0.5])
FIELDS = [([1., 0., 0.], [0., 1., 0.]),
          ([1.6, 0.2, 0.], [0., 0.7, 0.4]),
          ([0.7, 0., 0.3], [0.2, 1.4, 0.])]
NODES, QUAD_WEIGHTS = np.polynomial.legendre.leggauss(18)
NODES = (NODES + 1) / 2
QUAD_WEIGHTS = QUAD_WEIGHTS / 2
CASES = []


def check(name, value, limit, kind='floating'):
    value = float(value)
    CASES.append({'name': name, 'value': value, 'upper_bound': float(limit),
                  'pass': bool(value <= limit), 'kind': kind})


def mat(v):
    return np.einsum('i,ijk->jk', v, T)


def exp_su2(v):
    length = np.linalg.norm(v)
    if length < 1e-15:
        return I2 + 1j * mat(v)
    return math.cos(length/2)*I2 + 2j*math.sin(length/2)*mat(v)/length


def inner(x, y):
    return np.einsum('c,cij,cij->', WEIGHTS, x.conj(), y)/2


def hnorm(x):
    return math.sqrt(max(0., inner(x, x).real))


def radial_j(q):
    out = []
    for av, bv in FIELDS:
        av, bv = np.array(av), np.array(bv)
        direction = q.real*av + q.imag*bv
        radius = np.linalg.norm(direction)
        f = np.cross(av, bv)
        if radius < 1e-14:
            out.append(mat(f/2))
            continue
        axis = direction/radius
        angles = NODES*radius
        # R^* (f dot sigma) R rotates f by +angle about axis.
        rotated = (np.cos(angles)[:, None]*f
                   + np.sin(angles)[:, None]*np.cross(axis, f)
                   + (1-np.cos(angles))[:, None]*axis*np.dot(axis, f))
        out.append(mat(np.sum((QUAD_WEIGHTS*NODES)[:, None]*rotated, axis=0)))
    return np.array(out)


def local_moments(q, dq, k):
    j = radial_j(q)
    eps = 2e-4 / max(1., abs(dq))
    dj = (radial_j(q-2*eps*dq)-8*radial_j(q-eps*dq)
          +8*radial_j(q+eps*dq)-radial_j(q+2*eps*dq))/(12*eps)
    g = inner(j, j).real
    gp = 2*inner(j, dj).real
    j2 = j@j
    mu3 = inner(j, j2).real
    mu4 = inner(j2, j2).real
    derivative_residual = inner(dj, dj).real-gp*gp/(4*g)
    curvature_residual = mu4-g*g-mu3*mu3/g
    h = derivative_residual+k*k*curvature_residual
    return j, dj, g, gp, mu3, mu4, h


def step(fun, t, y, h):
    a = fun(t, y)
    b = fun(t+h/2, y+h*a/2)
    c = fun(t+h/2, y+h*b/2)
    d = fun(t+h, y+h*c)
    return y+h*(a+2*b+2*c+d)/6


def geometry_control(a, s_end, steps):
    """Direct prefix transports vs the moving two-observable Galerkin model.

    Uses s=sqrt(capacity). Geometry follows q_s=2s(a-2/q).
    Direct transport uses A dot dq; the reduced model uses transported curvature.
    """
    s0 = 1e-5
    q0 = 2j*s0+(2*a/3)*s0*s0-1j*a*a*s0**3/18
    transports = np.array([exp_su2(q0.real*np.array(av)+q0.imag*np.array(bv))
                           for av, bv in FIELDS])
    # q; three prefix transports; theta; residual integral; |k|sqrt(g) integral;
    # residual-integral times |k|sqrt(g), the sharper observable bound.
    state = np.r_[q0, transports.reshape(-1), 0j, 0j, 0j, 0j]

    def fun(s, y):
        q = y[0]
        dq = 2*s*(a-2/q)
        k = (q.conjugate()*dq).imag
        j, dj, g, gp, mu3, mu4, h2 = local_moments(q, dq, k)
        us = y[1:13].reshape(3, 2, 2)
        dus = np.array([1j*mat(dq.real*np.array(av)+dq.imag*np.array(bv))@u
                        for (av, bv), u in zip(FIELDS, us)])
        theta = y[13].real
        residual = abs(math.sin(theta))*math.sqrt(max(0., h2/g))
        speed = abs(k)*math.sqrt(g)
        return np.r_[dq, dus.reshape(-1), k*math.sqrt(g), residual, speed,
                     speed*y[14].real]

    ds = (s_end-s0)/steps
    for n in range(steps):
        state = step(fun, s0+n*ds, state, ds)
    q = state[0]
    loops = np.array([exp_su2(q.real*np.array(av)+q.imag*np.array(bv)).conj().T@u
                      for (av, bv), u in zip(FIELDS, state[1:13].reshape(3,2,2))])
    e = np.repeat(I2[None,:,:], 3, axis=0)
    w = inner(e, loops)
    theta = state[13].real
    x, y = math.cos(theta), 1j*math.sin(theta)
    j = radial_j(q)
    g = inner(j, j).real
    approx = x*e+y*j/math.sqrt(g)
    result = {'a':a, 'capacity':s_end*s_end, 'steps':steps,
              'W':w.real, 'W_imag':w.imag, 'W_two_mode':x,
              'observable_error':abs(w-x), 'state_error':hnorm(loops-approx),
              'state_error_bound':state[14].real,
              'observable_error_bound':min(state[14].real,state[16].real),
              'norm_error':abs(inner(loops,loops)-1),
              'storage_identity_error':abs(abs(w)**2+hnorm(loops-w*e)**2-1)}
    return result


def algebra_controls():
    # OS positivity does not make half-space multiplication descend to its quotient.
    # Independent +/-1 variables on the two halves: ||f||_OS^2=|E f|^2.
    f = np.array([-1.,1.])
    u = 1j*f  # e^(i*pi*f/2)
    check('OS null input',abs(np.mean(f))**2,0.,'exact finite arithmetic')
    check('OS unitary multiplier gives non-null output',abs(abs(np.mean(u*f))**2-1),0.,'exact finite arithmetic')
    check('configuration multiplier is unitary',np.max(abs(abs(u)**2-1)),0.,'exact finite arithmetic')
    # Positive storage can return to the observed amplitude; it is not monotone.
    check('two-state storage returns to zero',abs(math.sin(math.pi)**2),1e-28)
    check('two-state storage initially reaches one',abs(math.sin(math.pi/2)**2-1),1e-15)
    # The scalar-coupled analogue is not unitary even on one configuration.
    check('Hermitian scalar transport has norm above one',1-math.cosh(1.),-0.1)

    # Generic SU(3) controls test the mu3 term absent identically for SU(2).
    rng = np.random.default_rng(20260924)
    for n in range(4):
        raw = rng.normal(size=(3,3,3))+1j*rng.normal(size=(3,3,3))
        j = (raw+raw.conj().transpose(0,2,1))/2
        j -= np.trace(j,axis1=1,axis2=2)[:,None,None]*np.eye(3)/3
        raw = rng.normal(size=(3,3,3))+1j*rng.normal(size=(3,3,3))
        dj = (raw+raw.conj().transpose(0,2,1))/2
        dj -= np.trace(dj,axis1=1,axis2=2)[:,None,None]*np.eye(3)/3
        inn = lambda x,y: np.einsum('c,cij,cij->',WEIGHTS,x.conj(),y)/3
        e = np.repeat(np.eye(3)[None,:,:],3,axis=0)
        g, gp = inn(j,j).real, 2*inn(j,dj).real
        mu3, mu4 = inn(j,j@j).real, inn(j@j,j@j).real
        k=0.7
        ares = dj-gp*j/(2*g)
        bres = j@j-g*e-(mu3/g)*j
        direct = inn(ares-1j*k*bres,ares-1j*k*bres).real
        formula = inn(dj,dj).real-gp*gp/(4*g)+k*k*(mu4-g*g-mu3*mu3/g)
        check(f'SU3 residual formula {n}',abs(direct-formula),2e-13)
        check(f'SU3 residual orthogonal to identity {n}',abs(inn(e,ares-1j*k*bres)),2e-14)
        check(f'SU3 residual orthogonal to J {n}',abs(inn(j,ares-1j*k*bres)),2e-14)
        check(f'SU3 derivative residual nonnegative {n}',-inn(ares,ares).real,1e-14)
        check(f'SU3 curvature residual nonnegative {n}',-inn(bres,bres).real,1e-14)

    # Moving Gram connection: b0=e0, b1=(1+t)e1 with fixed skew generator.
    t=0.4
    basis=np.diag([1.,1+t]).astype(complex)
    db=np.diag([0.,1.]).astype(complex)
    gen=1j*np.array([[0.,0.8],[0.8,0.]])
    gram=basis.conj().T@basis
    conn=basis.conj().T@db
    amat=basis.conj().T@gen@basis
    c=np.array([1.,1j])/math.sqrt(2)
    dc=np.linalg.solve(gram,(amat-conn)@c)
    gdot=db.conj().T@basis+basis.conj().T@db
    check('moving Gram connection conserves norm',abs(np.vdot(c,gdot@c)+2*np.vdot(c,gram@dc).real),1e-14)
    bad=np.linalg.solve(gram,amat@c)
    bad_rate=(np.vdot(c,gdot@c)+2*np.vdot(c,gram@bad).real).real
    check('omitting connection changes norm',-abs(bad_rate),-0.5)


def memory_control(steps=1000):
    """Independent nonautonomous four-state control of the exact memory formula."""
    h0=np.array([[0.,.7,.2,0.],[.7,.3,.4,0.],[.2,.4,-.2,.3],[0.,0.,.3,.5]])
    h1=np.array([[0.,0.,.3,.2],[0.,-.1,.2,.1],[.3,.2,.4,0.],[.2,.1,0.,-.3]])
    e=np.array([1.,0.,0.,0.],complex)
    q=np.eye(4)-np.outer(e,e.conj())
    gen=lambda t: 1j*(h0+math.sin(t)*h1)
    def rhs(t,y):
        a=gen(t)
        return np.r_[a@y[:4],(q@a@q@y[4:].reshape(4,4)).reshape(-1)]
    end=1.2
    dt=end/steps
    state=np.r_[e,np.eye(4,dtype=complex).reshape(-1)]
    vectors=[]; ws=[]; states=[]
    for n in range(steps+1):
        t=n*dt
        r=state[4:].reshape(4,4)
        vectors.append(r.conj().T@gen(t)@e)
        ws.append(state[0]); states.append(state[:4].copy())
        if n<steps: state=step(rhs,t,state,dt)
    vectors=np.array(vectors); ws=np.array(ws)
    sample=vectors[::100]
    kernel=sample.conj()@sample.T
    check('two-time memory Gram is positive',-np.linalg.eigvalsh(kernel).min(),1e-12)
    check('complement propagation is unitary',np.linalg.norm(r.conj().T@r-np.eye(4)),1e-11)
    integ=np.trapz((vectors[-1].conj()@vectors.T)*ws,dx=dt)
    derivative=(gen(end)@state[:4])[0]
    check('Volterra memory reproduces amplitude derivative',abs(derivative+integ),8e-7)
    z_reconstructed=r@np.trapz(vectors*ws[:,None],dx=dt,axis=0)
    check('memory reconstructs retained state',np.linalg.norm(q@state[:4]-z_reconstructed),8e-7)
    check('full-state storage identity',abs(np.linalg.norm(q@state[:4])**2+abs(state[0])**2-1),1e-11)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    algebra_controls()
    memory_control()
    e=np.repeat(I2[None,:,:],3,axis=0)
    for n,q in enumerate([0.1+0.5j,0.3+1.0j,0.6+1.5j]):
        dq=0.4+0.9j
        k=(q.conjugate()*dq).imag
        j,dj,g,gp,mu3,mu4,h=local_moments(q,dq,k)
        res=dj-(gp/(2*g))*j-1j*k*(j@j-g*e-(mu3/g)*j)
        check(f'YM chord residual formula {n}',abs(h-inner(res,res).real),2e-13)
        check(f'YM chord generator is Hermitian {n}',hnorm(j-j.conj().transpose(0,2,1)),1e-14)
        check(f'SU2 cubic moment vanishes {n}',abs(mu3),1e-14)
        # Independent matrix integration checks the vector rotation convention.
        jm=[]
        for av,bv in FIELDS:
            av,bv=np.array(av),np.array(bv)
            f=mat(np.cross(av,bv))
            total=np.zeros((2,2),complex)
            for r,w in zip(NODES,QUAD_WEIGHTS):
                u=exp_su2(r*(q.real*av+q.imag*bv))
                total+=w*r*(u.conj().T@f@u)
            jm.append(total)
        check(f'rotation and direct matrix J agree {n}',hnorm(j-np.array(jm)),1e-14)
    runs=[]
    for a,s in [(0.,.65),(.8,.45),(.8,.65),(-.8,.65)]:
        result=geometry_control(a,s,400)
        runs.append(result)
        tag=f'a={a},s={s}'
        check('direct-loop unitarity '+tag,result['norm_error'],1e-9)
        check('Wilson storage identity '+tag,result['storage_identity_error'],1e-9)
        check('state residual bounds direct error '+tag,result['state_error']-result['state_error_bound'],2e-9)
        check('sharper residual bounds Wilson error '+tag,result['observable_error']-result['observable_error_bound'],2e-9)
    refined=geometry_control(.8,.65,800)
    coarse=runs[2]
    check('direct W step refinement',abs(refined['W']-coarse['W']),2e-10)
    check('residual bound step refinement',abs(refined['observable_error_bound']-coarse['observable_error_bound']),2e-10)
    check('finite noncommuting ensemble has nonzero residual',-coarse['state_error_bound'],-1e-7)
    out={'date':'2026-09-24','prepared_for':'Edward Baker',
         'model':'GPT-6 (Codex; developer-provided identity)',
         'reasoning_effort':'Not exposed; not inferred',
         'program':Path(__file__).name,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'runtime':{'python':platform.python_version(),'numpy':np.__version__},
         'scope':'Finite matrix and prescribed positive-background diagnostics; no YM measure sampling, interval certification, continuum construction, or arithmetic realization.',
         'case_count':len(CASES),'all_pass':all(c['pass'] for c in CASES),
         'failed':[c for c in CASES if not c['pass']], 'cases':CASES,
         'geometry_runs':runs,'refined_run':refined,
         'backgrounds':FIELDS,'weights':WEIGHTS.tolist(),
         'limits':['Residual quadratures and field derivatives are floating evaluations, not certified bounds.',
                   'The analytic error theorem is proved in the companion note under its hypotheses.',
                   'Finite prescribed fields are not draws from the interacting YM vacuum.']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('case_count','all_pass','failed','geometry_runs')},indent=2))
    if not out['all_pass']: raise SystemExit(1)


if __name__=='__main__':
    main()
