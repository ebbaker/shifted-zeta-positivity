#!/usr/bin/env python3
"""Bounded floating theta-density pilot; NumPy only.

Prepared for Edward Baker, 2026-10-24, with substantial LLM assistance.
Model gpt-6-astra (Codex), recorded effort max. Not interval certified.
"""
import argparse
import json
import math
import platform
import hashlib
from functools import lru_cache
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

leggauss = lru_cache(maxsize=16)(leggauss)


def source_jets(t, z, order=3, nquad=192, ntheta=8):
    t, z = np.broadcast_arrays(np.asarray(t, float), np.asarray(z, complex))
    shape = z.shape
    t, z = t.ravel(), z.ravel()
    out = np.empty((order + 1, z.size), complex)
    nodes, weights = leggauss(nquad)
    for value in np.unique(t):
        mask = t == value
        umax = min(2.0, 12.0 / math.sqrt(max(1.0, -value)))
        u = (nodes + 1) * umax / 2
        w = weights * umax / 2
        source = np.zeros_like(u)
        for n in range(1, ntheta + 1):
            source += (2 * math.pi**2 *
                       (n**4 - 3*n*n*np.exp(-4*u)/(2*math.pi)) *
                       np.exp(value*u*u + 9*u - math.pi*n*n*np.exp(4*u)))
        phase = z[mask, None] * u[None, :]
        cosine, sine = np.cos(phase), np.sin(phase)
        for k in range(order + 1):
            trig = cosine if k % 2 == 0 else sine
            sign = (-1)**((k + 1)//2)
            out[k, mask] = sign * (trig @ (w * source * u**k))
    return [row.reshape(shape) for row in out]


def fields(t, z, epsilon, nquad=192, ntheta=8):
    h, h1, h2, h3 = source_jets(t, z, nquad=nquad, ntheta=ntheta)
    return fields_from_jets(h, h1, h2, h3, epsilon)


def fields_from_jets(h, h1, h2, h3, epsilon):
    d = abs(h)**2 + epsilon**2
    dt = -2*np.real(h2*np.conj(h))
    b = h1*np.conj(h)/d
    c = h2*np.conj(h)/d - b*b
    bt = (-h3*np.conj(h)-h1*np.conj(h2))/d - b*dt/d
    rho = epsilon**2*abs(h1)**2/(math.pi*d*d)
    j = epsilon**2*h2*np.conj(h1)/(math.pi*d*d)
    rhox = 2*j.real-2*rho*(2*b.real)
    rhoy = -2*j.imag-2*rho*(-2*b.imag)
    rhot = -2*epsilon**2*np.real(h3*np.conj(h1))/(math.pi*d*d)-2*rho*dt/d
    rhozz = (epsilon**2/math.pi)*(h3*np.conj(h1)/d**2
             -6*h2*abs(h1)**2*np.conj(h)/d**3
             +6*abs(h1)**2*h1**2*np.conj(h)**2/d**4)
    return dict(S=np.log(d), rho=rho, sx=2*b.real, sy=-2*b.imag,
                sxx=2*c.real+2*math.pi*rho,
                syy=-2*c.real+2*math.pi*rho, sxy=-2*c.imag,
                st=dt/d, sxt=2*bt.real, syt=-2*bt.imag,
                jx=j.real, jy=j.imag, rhox=rhox, rhoy=rhoy, rhot=rhot,
                rhoxx_minus_rhoyy=4*rhozz.real)


def filter_axis(width, n):
    if width == 0:
        return np.array([0.0]), np.array([1.0])
    q, w = leggauss(n)
    w = w*(315/256)*(1-q*q)**4
    assert abs(w.sum()-1) < 1e-12
    return width*q, w


def average(center, epsilon, widths, nfilter=20, nquad=192, evaluator=None):
    t, x, y = center
    tau, lx, ly = widths
    shifts = [filter_axis(w, nfilter) for w in widths]
    dt, dx, dy = np.meshgrid(*(q[0] for q in shifts), indexing="ij")
    wt, wx, wy = np.meshgrid(*(q[1] for q in shifts), indexing="ij")
    w = (wt*wx*wy).ravel()
    evaluate = fields if evaluator is None else evaluator
    f = evaluate(t-dt.ravel(), x-dx.ravel()+1j*(y-dy.ravel()), epsilon, nquad)
    mean = {key:float(np.dot(w, value)) for key,value in f.items()}
    vx = float(np.dot(w,(f["sx"]-mean["sx"])**2))
    vy = float(np.dot(w,(f["sy"]-mean["sy"])**2))
    q = vx-vy
    variance = float(np.dot(w,(f["rho"]-mean["rho"])**2))
    sigt, sigx, sigy = [(v*v/11) for v in widths]
    qgrad = (sigt*(mean["sxt"]**2-mean["syt"]**2)
             +sigx*(mean["sxx"]**2-mean["sxy"]**2)
             +sigy*(mean["sxy"]**2-mean["syy"]**2))
    identity = mean["st"]+.5*(mean["sxx"]-mean["syy"]+
                              mean["sx"]**2-mean["sy"]**2+q)
    def cov(a,b):
        return float(np.dot(w,(f[a]-mean[a])*(f[b]-mean[b])))
    lapq = (2*(cov("sxx","sxx")-cov("syy","syy"))
            +8*math.pi*(cov("sx","rhox")-cov("sy","rhoy")))
    density_identity = (mean["rhot"]+.5*mean["rhoxx_minus_rhoyy"]
                        +(mean["sxx"]**2-mean["syy"]**2)/(4*math.pi)
                        +mean["sx"]*mean["rhox"]-mean["sy"]*mean["rhoy"]
                        +lapq/(8*math.pi))
    return dict(center=list(center), epsilon=epsilon, widths=list(widths),
                mean=mean, Txx=vx, Tyy=vy, Q=q, Q_gradient=qgrad,
                density_variance=variance,
                potential_identity_residual=identity,
                Laplacian_Q=lapq, density_identity_residual=density_identity,
                omitted_Q_potential_error=abs(q)/2,
                gradient_closure_potential_error=abs(q-qgrad)/2)


def derivative_diagnostics(center, epsilon, widths, nfilter=28, nquad=224,
                           evaluator=None):
    base = average(center,epsilon,widths,nfilter,nquad,evaluator)
    records=[]
    for step in (.02,.01,.005,.0025):
        around=[]
        for axis in (1,2):
            pair=[]
            for sign in (-1,1):
                other=list(center)
                other[axis]+=sign*step
                pair.append(average(other,epsilon,widths,nfilter,nquad,evaluator))
            around.append(pair)
        lap={key:sum(pair[0][key]-2*base[key]+pair[1][key] for pair in around)/step**2
             for key in ("Q","Q_gradient")}
        divj=((around[0][1]["mean"]["jx"]-around[0][0]["mean"]["jx"])
              +(around[1][1]["mean"]["jy"]-around[1][0]["mean"]["jy"]))/ (2*step)
        records.append(dict(step=step,laplacian_Q=lap["Q"],
                            laplacian_Q_gradient=lap["Q_gradient"],divergence_J=divj))
    extrapolations=[{key:(4*fine[key]-coarse[key])/3
                     for key in ("laplacian_Q","laplacian_Q_gradient","divergence_J")}
                    for coarse,fine in zip(records[:-1],records[1:])]
    extrap=extrapolations[-1]
    exact=base["Laplacian_Q"]
    base["derivatives"]=dict(
        finite_differences=records,richardson=extrap,
        richardson_history=extrapolations,
        Q_laplacian_check=abs(extrap["laplacian_Q"]-exact),
        current_identity_check=abs(base["mean"]["rhot"]+extrap["divergence_J"]),
        omitted_Q_density_error=abs(exact)/(8*math.pi),
        gradient_closure_density_error=abs(extrap["laplacian_Q_gradient"]-exact)/(8*math.pi),
        gradient_density_fd_change=abs(extrap["laplacian_Q_gradient"]-
                         extrapolations[-2]["laplacian_Q_gradient"])/(8*math.pi))
    return base


def run_pilot():
    cases=[]
    centers=[(0,28,.5),(.25,26,.25),(-.25,30,.5)]
    common=[(0,.25,.25),(0,1,1),(.25,0,0),(.25,.5,.5)]
    for i,center in enumerate(centers):
        widths=([(0,.125,.125),(0,.5,.5)] if i==0 else [])+common
        for width in widths:
            cases.append((f"center_{i+1}",center,1e-4,width))
    for width in [common[0],common[1],common[3]]:
        cases.append(("regulator_sensitivity",centers[0],5e-5,width))
    data=[]
    for label,center,epsilon,widths in cases:
        baseline=average(center,epsilon,widths,20,160)
        middle=average(center,epsilon,widths,28,224)
        source_only=average(center,epsilon,widths,20,224)
        refinement={key:abs(middle[key]-baseline[key])
                    for key in ("Q","Q_gradient","Laplacian_Q")}
        refinement.update({key:abs(middle["mean"][key]-baseline["mean"][key])
                           for key in ("rho","st","rhot","jx","jy")})
        nfilter=40 if max(refinement.values())>1e-7 else 28
        refined=derivative_diagnostics(center,epsilon,widths,nfilter=nfilter)
        extra={key:abs(refined[key]-middle[key])
               for key in ("Q","Q_gradient","Laplacian_Q")}
        extra["rho"]=abs(refined["mean"]["rho"]-middle["mean"]["rho"])
        source_ref={key:abs(source_only[key]-baseline[key])
                    for key in ("Q","Q_gradient","Laplacian_Q")}
        source_ref["rho"]=abs(source_only["mean"]["rho"]-baseline["mean"]["rho"])
        refined.update(label=label,refinement_20_160_to_28_224=refinement,
                       source_refinement_160_to_224=source_ref,
                       final_filter_order=nfilter,extra_filter_refinement=extra)
        data.append(refined)
        d=refined["derivatives"]
        print(label,widths,"eps",epsilon,"rho",refined["mean"]["rho"],
              "potential_ratio",refined["gradient_closure_potential_error"]/
                                 max(refined["omitted_Q_potential_error"],1e-30),
              "density_ratio",d["gradient_closure_density_error"]/
                               max(d["omitted_Q_density_error"],1e-30),flush=True)
    return data


def phi_zero():
    return sum((2*math.pi**2*n**4-3*math.pi*n*n)*math.exp(-math.pi*n*n)
               for n in range(1,9))


def negative_time_checks():
    rows=[]
    epsilon=1e-4
    for T in (1e8,4e8,1.6e9):
        value=average((-T,2,.5),epsilon,(0,.5,.5),24,192)
        leading=phi_zero()**2*(2**2+.5**2+2*.5**2/11)/(16*epsilon**2*T**3)
        resummed=leading/(1+math.pi*phi_zero()**2/(4*T*epsilon**2))**2
        def gaussian(t,z,eps,nquad):
            TT=-t
            hg=phi_zero()*math.sqrt(math.pi)/ (2*np.sqrt(TT))*np.exp(-z*z/(4*TT))
            return fields_from_jets(hg,-z*hg/(2*TT),
                     (z*z/(4*TT**2)-1/(2*TT))*hg,
                     (3*z/(4*TT**2)-z**3/(8*TT**3))*hg,eps)
        g=average((-T,2,.5),epsilon,(0,.5,.5),24,192,evaluator=gaussian)
        rows.append(dict(T=T,epsilon=epsilon,widths=[0,.5,.5],
                         rho=value["mean"]["rho"],fixed_region_leading=leading,
                         ratio=value["mean"]["rho"]/leading,
                         regulator_resummed_leading=resummed,
                         resummed_ratio=value["mean"]["rho"]/resummed,
                         gaussian_average=g["mean"]["rho"],
                         gaussian_ratio=value["mean"]["rho"]/g["mean"]["rho"]))
    return rows


def negative_covariance_checks():
    rows=[]
    epsilon=1.0
    halfwidth=.5
    variance=halfwidth**2/11
    fourth=3*halfwidth**4/143
    B=math.pi*phi_zero()**2/(4*epsilon**2)
    for T in (1e3,4e3,1.6e4):
        a=average((-T,2,.5),epsilon,(0,halfwidth,halfwidth),28,224)
        q=-2*B*B*(variance*(4+.25)+fourth-variance**2)/T**5
        lapq=-8*B*B*variance/T**5
        rows.append(dict(T=T,epsilon=epsilon,halfwidth=halfwidth,Q=a["Q"],
                         Q_leading=q,Q_ratio=a["Q"]/q,Laplacian_Q=a["Laplacian_Q"],
                         Laplacian_Q_leading=lapq,Laplacian_Q_ratio=a["Laplacian_Q"]/lapq,
                         Q_gradient=a["Q_gradient"]))
    return rows


def cosine_covariance_checks():
    rows=[]
    # This is a model calculation; L=1.3 and M=1 at the observed time.
    L=1.3
    for eta in (.1,.5,1,2):
        for Y in (0,.4,1):
            n=16384
            X=(np.arange(n)+.5)*math.pi/n
            z=(X+1j*Y)/L
            f=fields_from_jets(np.cos(L*z),-L*np.sin(L*z),
                              -L*L*np.cos(L*z),L**3*np.sin(L*z),eta)
            a=math.sinh(Y)**2+eta**2
            d=math.sqrt(a*(a+1))
            uy=L*math.sinh(2*Y)/d
            r=L*L*eta*eta/(2*math.pi)*(2*a*(a+1)+1-eta*eta*(2*a+1))/d**3
            q=4*math.pi*r+uy*uy-4*L*L+4*L*L*eta*eta/d
            actual_q=float(np.var(f["sx"])-np.var(f["sy"]))
            rows.append(dict(eta=eta,Y=Y,L=L,U=2*math.asinh(math.sqrt(a))-2*math.log(2),
                             rho=r,Q=q,numeric_Q=actual_q,
                             Q_error=abs(actual_q-q),
                             U_error=abs(float(np.mean(f["S"]))-
                                         (2*math.asinh(math.sqrt(a))-2*math.log(2))),
                             Ut_error=abs(float(np.mean(f["st"]))-2*L*L*(1-eta*eta/d))))
    return rows


def polynomial_control():
    def evaluate(t,z,epsilon,nquad):
        # Exact heat field with a double zero at (t,z)=(0,0).
        return fields_from_jets(z*z-2*t,2*z,2+0*z,0*z,epsilon)
    rows=[]
    for h in (.2,.1,.05):
        result=derivative_diagnostics((0,.2,.1),1,(h,h,h),evaluator=evaluate)
        rows.append(result)
    return rows


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--scout",action="store_true")
    args=p.parse_args()
    if args.scout:
        for t in (0, .25, 4, 16, 64):
            xs=np.array([0, 6, 12, 24, 28, 30])
            h,h1=source_jets(t,xs,order=1)
            print(t,[(int(x),float(a.real),float(b.real)) for x,a,b in zip(xs,h,h1)])
        return
    result=dict(title="Averaged unnormalized theta density: first bounded pilot",
                date="2026-10-24",author="Prepared for Edward Baker with LLM assistance",
                model="gpt-6-astra",effort="max",status="floating checks; not a certificate",
                python=platform.python_version(),numpy=np.__version__,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                kernel="315/256 (1-q^2)^4 on [-1,1]; product over active axes",
                variance_factor=1/11,phi_zero=phi_zero(),
                source_nterms=8,source_u_cutoff="min(2,12/sqrt(max(1,-t)))",
                samples=run_pilot(),negative_time=negative_time_checks(),
                negative_covariance=negative_covariance_checks(),
                cosine_covariance=cosine_covariance_checks(),
                collision_control=polynomial_control())
    if not args.output:
        raise SystemExit("Provide --output PATH for the small reproducibility record")
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print("saved",args.output)


if __name__=="__main__":
    main()
