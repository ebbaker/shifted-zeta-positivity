#!/usr/bin/env python3
"""L=1/2 EMA pilot. NumPy only; imports the parent arithmetic assembler.

Full output functions are integrated, never projected before forming a norm.
All floating results are diagnostics, not interval certificates. See the dated
research note for exact analytical bounds and the unresolved input complement.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
PARENT = HERE.parents[1] / 'loewner/numerics/check_contraction_margin.py'
spec = importlib.util.spec_from_file_location('parent_transfer', PARENT)
parent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parent)
L = 0.5
SHIFTS = (0.1, 0.03, 0.01, 0.003, 0.001)
SCHEDULES = {'w^0.75': 0.75, 'w': 1.0, 'w^1.25': 1.25, 'sqrt(w)_contaminating': 0.5}
CACHE = {}


def gj(omega, n):
    """Parent Golub-Welsch recurrence, NumPy eigensolver, removable factors cancelled."""
    key = (float(omega), int(n))
    if key not in CACHE:
        be = omega - 1.0
        diag = [(omega - 1.0) / (omega + 1.0)]
        sub = []
        for k in range(1, n):
            d = 2.0 * k + be
            diag.append(be * be / (d * (d + 2)))
            v = (4 * omega / ((1 + omega)**2 * (2 + omega)) if k == 1 else
                 4*k*k*(k+be)**2/(d*d*(d+1)*(d-1)))
            sub.append(math.sqrt(v))
        mat = np.diag(diag) + np.diag(sub, 1) + np.diag(sub, -1)
        x, U = np.linalg.eigh(mat)
        CACHE[key] = ((x + 1)/2, U[0]**2/omega)
    return CACHE[key]


# Kernel and all local/pole factors stay in the imported machinery. Only its
# quadrature eigensolver and array evaluation are accelerated here.
parent.gauss_jacobi_unit = gj


def gh_array(ker, t):
    """Vectorized parent Kernel.Ghat; both rational pole corrections retained."""
    def G(t):
        r = 2*np.sinh(t)/t
        return ker.pref * r**(ker.omega-1) * np.exp(t/2)
    t = np.asarray(t)
    u = t[..., None]*np.asarray(ker.xv)
    gg = G(u)
    delta = t[..., None]-u
    j1 = np.sum(np.exp(-ker.b*delta)*gg*ker.wv, axis=-1)
    j2 = np.sum(np.exp(ker.a*delta)*gg*ker.wv, axis=-1)
    return G(t)-4*ker.omega*t*(ker.b*j1+ker.a*j2)


def xrule(order):
    z, w = np.polynomial.legendre.leggauss(order)
    edges = L*np.array([0, 0.0001, 0.001, 0.01, 0.1, 1.0])
    x = np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges[:-1], edges[1:])])
    wx = np.concatenate([(b-a)*w/2 for a,b in zip(edges[:-1], edges[1:])])
    return np.r_[x,L], np.r_[wx,0.0]


def basis(x, n, ell=0.0, derivative=False):
    x = np.asarray(x)[..., None]
    k = np.arange(1,n+1)*math.pi/L
    sn, cs = np.sin(x*k), np.cos(x*k)
    if not ell:
        return math.sqrt(2/L)*(k*cs if derivative else sn)
    a = ell*k
    if derivative:
        y = (k*cs+ell*k*k*sn-k*np.exp(-x/ell))/(1+a*a)
    else:
        y = (sn-a*cs+a*np.exp(-x/ell))/(1+a*a)
    return math.sqrt(2/L)*y


class Response:
    def __init__(self, omega, x, delay_order, inner_order):
        self.omega, self.x = omega, x
        self.ker = parent.Kernel(omega, inner_order)
        v,w = gj(omega,delay_order)
        t = x[:,None]*v
        self.y = x[:,None]*(1-v)
        self.weights = x[:,None]**omega*w*gh_array(self.ker,t)

    def apply(self,n,ell=0.0,derivative=False):
        return np.einsum('ij,ijk->ik',self.weights,basis(self.y,n,ell,derivative))


def gram(F, wx, G=None):
    return F.T @ (wx[:,None]*(F if G is None else G))


def largest(A):
    return float(np.linalg.eigvalsh((A+A.T)/2)[-1])


def smallest(A):
    return float(np.linalg.eigvalsh((A+A.T)/2)[0])


def generalized_min(D,B):
    ev,U = np.linalg.eigh(B)
    R = U @ np.diag(1/np.sqrt(ev)) @ U.T
    return smallest(R@D@R)


def quadratic(A,v):
    return float(v@A@v)


def qmatrix(n):
    W=parent.WeilForm(L,n)
    Q=np.zeros((n,n))
    for parity in (0,1):
        block,idx=W.matrix(parent.prime_comb(L),parity)
        ix=np.array(idx)-1
        Q[np.ix_(ix,ix)]=block
    return Q


def explicit_bounds(omega,ell,n):
    # h(t) <= (2 pi)^omega / Gamma(omega) t^(omega-1), 0<omega<=1.
    mh=(2*math.pi*L)**omega/math.gamma(1+omega)
    a=0.5-omega
    C=mh*(1+2*omega*L*math.exp(a*L))
    snorm=1/math.sqrt(1+2*ell*ell/L**2)
    # W=S V; |W* f(0)|<=C/sqrt(2 ell), ||(W*)' f||<=2C/ell.
    tail=C*(math.sqrt(L/(n*ell))/math.pi+2*L/(math.pi*(n+1)*ell))
    tail=min(tail,C*snorm)
    return {'kernel_L1_upper_formula':C,'smoother_norm_upper_formula':snorm,
            'input_complement_upper_formula':tail}


def pilot(n,order,delay_order,inner_order,path_order):
    start=time.perf_counter()
    x,wx=xrule(order)
    F=basis(x,n)
    I=np.eye(n)
    Q=qmatrix(n)
    qev,qvec=np.linalg.eigh(Q)
    weak=qvec[:,0]
    rows=[]
    checks={'input_orthogonality':float(np.max(np.abs(gram(F,wx)-I)))}
    # Importer's scalar implementation is a separate evaluation path.
    scalar_error=0.0
    reduced_error=0.0
    for omega in SHIFTS:
        R=Response(omega,x,delay_order,inner_order)
        G=R.apply(n)
        Gp=R.apply(n,derivative=True)
        T=gram(G,wx)
        D=I-T
        ev,U=np.linalg.eigh(D)
        wdir=U[:,0]
        projected=gram(F,wx,G)
        omitted=T-projected.T@projected
        unit=np.eye(n)
        dirs={'e1':unit[0],'e8':unit[min(7,n-1)],'eN':unit[-1],
              'central_weak':weak,'original_weak':wdir}
        row={'omega':omega,'original':{'restricted_norm':math.sqrt(largest(T)),
             'min_defect_over_2w':float(ev[0]/(2*omega)),
             'output_projection_loss_norm':largest(omitted),
             'output_projection_loss_weak_over_2w':quadratic(omitted,wdir)/(2*omega),
             'tests':{k:{'defect_over_2w':quadratic(D,v)/(2*omega),'Q':quadratic(Q,v)} for k,v in dirs.items()}},
             'schedules':{},'path_averages':{}}
        # Parent kernel versus absorbed S10 kernel, including remaining pole.
        ts=np.array([0.001,0.03,0.15,0.3,0.5])
        gh=gh_array(R.ker,ts)
        scalar_error=max(scalar_error,max(abs(gh[j]-R.ker.Ghat(float(t))) for j,t in enumerate(ts)))
        vj,wj=gj(omega,inner_order)
        def hhat(t):
            return (2*math.pi)**omega/math.gamma(omega)*(np.sinh(t)/t)**(omega-1)*np.exp(-1.5*t)
        red=hhat(ts)-2*omega*ts*np.sum(wj*np.exp((0.5-omega)*ts[:,None]*(1-vj))*hhat(ts[:,None]*vj),axis=1)
        reduced_error=max(reduced_error,float(np.max(np.abs(red-gh))))
        # The parent transfer_matrix is only a check of projected entries.
        if omega==0.01:
            _,nodes=parent.kernel_nodes(omega,L,delay_order,inner_order)
            pm=np.array(parent.transfer_matrix(L,n,nodes))
            checks['parent_projected_entries']=float(np.max(np.abs(pm-projected)))
        for name,power in SCHEDULES.items():
            ell=omega**power
            SF=basis(x,n,ell)
            H=R.apply(n,ell)
            Hp=R.apply(n,ell,derivative=True)
            B=gram(SF,wx)
            HT=gram(H,wx)
            Dout=I-HT
            Eintegral=ell**2*gram(Hp,wx)+ell*np.outer(H[-1],H[-1])
            E=T-HT
            Din=B-HT
            residual=float(np.max(np.abs(E-Eintegral)))
            bounds=explicit_bounds(omega,ell,n)
            a2=largest(HT)
            bounds['all_input_norm_upper_with_diagnostic_finite_block']=math.sqrt(a2+bounds['input_complement_upper_formula']**2)
            # Exact analytic loss bound for any unit sine-space vector uses
            # ||f'||<=k_N; |g(L)|<=||f'||_infinity times the first kernel moment.
            mh=(2*math.pi*L)**omega/math.gamma(1+omega)
            kval=np.arange(1,n+1)*math.pi/L
            infder=math.sqrt(2/L)*np.linalg.norm(kval)
            trace_bound=omega*infder*mh*(L/(1+omega)+2*L*L*math.exp((0.5-omega)*L))
            loss_bound=2*ell**2*bounds['kernel_L1_upper_formula']**2*kval[-1]**2+2*ell*trace_bound**2
            row['schedules'][name]={'ell':ell,'ell2_over_w':ell*ell/omega,
                'output_restricted_norm':math.sqrt(a2),'output_min_defect_over_2w':smallest(Dout)/(2*omega),
                'filter_loss_norm_over_2w':largest(E)/(2*omega),
                'filter_energy_identity_residual':residual,
                'loss_subtracted_min_over_2w':smallest(Dout-Eintegral)/(2*omega),
                'input_congruence_min_over_2w':smallest(Din)/(2*omega),
                'input_relative_min_over_2w':generalized_min(Din,B)/(2*omega),
                'smoothed_input_gram_condition':float(np.linalg.cond(B)),
                'analytic_uniform_sine_space_loss_upper_over_2w':loss_bound/(2*omega),
                'bounds':bounds,
                'tests':{k:{'output_over_2w':quadratic(Dout,v)/(2*omega),
                    'filter_loss_over_2w':quadratic(Eintegral,v)/(2*omega),
                    'input_relative_over_2w':quadratic(Din,v)/quadratic(B,v)/(2*omega)} for k,v in dirs.items()}}
        for c in (0.5,1.0,2.0):
            u,weights=gj(1/c,path_order)
            weights=weights/c
            mean=omega/(1+c)
            avg=np.zeros_like(G)
            avgT=np.zeros_like(T)
            for s,p in zip(omega*u,weights):
                GS=Response(s,x,delay_order,inner_order).apply(n)
                avg+=p*GS
                avgT+=p*gram(GS,wx)
            BT=gram(avg,wx)
            variance=avgT-BT
            original_mean=Response(mean,x,delay_order,inner_order).apply(n)
            Dmean=I-gram(original_mean,wx)
            row['path_averages'][str(c)]={'m':mean,'min_defect_over_2m':smallest(I-BT)/(2*mean),
                'averaged_defect_min_over_2m':smallest(I-avgT)/(2*mean),
                'variance_norm_over_2m':largest(variance)/(2*mean),
                'variance_min':smallest(variance),'original_at_m_min_over_2m':smallest(Dmean)/(2*mean),
                'tests':{k:{'average_transfer_over_2m':quadratic(I-BT,v)/(2*mean),
                    'average_defect_over_2m':quadratic(I-avgT,v)/(2*mean),
                    'variance_over_2m':quadratic(variance,v)/(2*mean),
                    'original_at_m_over_2m':quadratic(Dmean,v)/(2*mean)} for k,v in dirs.items()}}
        rows.append(row)
        print(f'n={n} omega={omega:g} complete',file=sys.stderr,flush=True)
    checks['vectorized_parent_kernel']=float(scalar_error)
    checks['absorbed_complete_kernel']=float(reduced_error)
    checks['filter_energy_identity']=max(v['filter_energy_identity_residual'] for row in rows for v in row['schedules'].values())
    checks['variance_negative_part']=max(0.0,-min(v['variance_min'] for row in rows for v in row['path_averages'].values()))
    # Expanding all-input control; L=.5 means 2L sqrt(omega)=sqrt(omega).
    toy=[]
    for omega in SHIFTS+(0.0001,0.00001):
        for name,power in SCHEDULES.items():
            ell=omega**power
            S=basis(x,n,ell)
            B=gram(S,wx)
            normloss=I-B
            orig=-math.expm1(2*omega)/(2*omega)
            out=(I-math.exp(2*omega)*B)/(2*omega)
            toy.append({'omega':omega,'schedule':name,'ell2_over_w':ell*ell/omega,
                'original':orig,'e1_output':float(out[0,0]),
                'e1_loss_subtracted':float(out[0,0]-math.exp(2*omega)*normloss[0,0]/(2*omega)),
                'input_relative':orig,
                'filtered_all_input_squared_norm_upper':math.exp(2*omega)/(1+2*ell*ell/L**2),
                'path_uniform_over_2m':(1-(math.expm1(omega)/omega)**2)/omega})
    return {'parameters':{'L':L,'N':n,'x_order_per_panel':order,'x_panels':5,
              'delay_order':delay_order,'inner_order':inner_order,'path_order':path_order},
        'central_Q_min':float(qev[0]),'central_Q_diagonal':[float(Q[i,i]) for i in (0,min(7,n-1),n-1)],
        'central_weak_coefficients':weak.tolist(),'checks':checks,'rows':rows,'toy':toy,
        'elapsed_seconds':time.perf_counter()-start}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=HERE/'records/adaptive-ema-pilot-20260920.json')
    args=ap.parse_args()
    runs=[pilot(24,48,64,24,8),pilot(24,72,96,32,12),pilot(40,96,128,32,12)]
    # Errors below are empirical refinement differences, not enclosures.
    r0,r1=runs[:2]
    differences=[]
    for a,b in zip(r0['rows'],r1['rows']):
        differences.append(abs(a['original']['min_defect_over_2w']-b['original']['min_defect_over_2w']))
        for s in SCHEDULES:
            for key in ('output_min_defect_over_2w','loss_subtracted_min_over_2w','input_relative_min_over_2w'):
                differences.append(abs(a['schedules'][s][key]-b['schedules'][s][key]))
        for c in ('0.5','1.0','2.0'):
            differences.append(abs(a['path_averages'][c]['min_defect_over_2m']-b['path_averages'][c]['min_defect_over_2m']))
    out={'schema':1,'date':'2026-09-20','model':'GPT-6 (Codex; system identity; deployment ID not exposed)',
         'reasoning_effort':'Extra High (user-confirmed in this task)',
         'scope':'Full-output finite-input diagnostics; analytical bound formulas evaluated in binary64, no interval certification.',
         'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'parent_source':str(PARENT.relative_to(HERE.parents[1])),
         'parent_sha256':hashlib.sha256(PARENT.read_bytes()).hexdigest(),
         'runs':runs,'max_N24_refinement_difference_normalized':max(differences)}
    out['checks_pass']=all(max(r['checks'].values())<2e-8 for r in runs) and max(differences)<2e-5
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(args.output),'checks_pass':out['checks_pass'],
                      'max_refinement_difference':max(differences)},indent=2))
    if not out['checks_pass']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
