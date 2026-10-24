#!/usr/bin/env python3
"""Finite coarse theta observations, with no root finding or peak quadrature.

2026-10-24. Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), actual recorded effort max. FLOATING, NOT CERTIFIED.
Analytic bounds have complete-source premises; their numerical inputs here
are finite quadratures and are not outward-rounded enclosures.
"""
import argparse
import hashlib
import json
import math
import platform
from functools import lru_cache
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

C = 315/256
LX, HY, YBUFFER, NCELL = 10., .75, 1.25, 6
EPS = 1e-4
leggauss = lru_cache(None)(leggauss)


def kernel(q):
    q = np.asarray(q)
    return C*np.maximum(0., 1-q*q)**4


def fourth_norm():
    roots = [0., math.sqrt((15-2*math.sqrt(30))/35),
             math.sqrt((15+2*math.sqrt(30))/35), 1.]
    primitive = lambda q: C*(144*q-480*q**3+336*q**5)
    return 2*sum(abs(primitive(b)-primitive(a)) for a,b in zip(roots[:-1],roots[1:]))


class Source:
    def __init__(self,t,order=32,umax=3.,ntheta=8):
        self.t = float(t)
        q,w = leggauss(order)
        edges = np.linspace(0,umax,round(umax/.125)+1)
        u = ((edges[:-1,None]+edges[1:,None])/2+
             (edges[1:,None]-edges[:-1,None])*q/2).ravel()
        weights = (np.diff(edges)[:,None]*w/2).ravel()
        terms = [math.log(2*math.pi**2)+4*math.log(n)+9*u
                 -math.pi*n*n*np.exp(4*u)
                 +np.log1p(-3*np.exp(-4*u)/(2*math.pi*n*n))
                 for n in range(1,ntheta+1)]
        exponent = t*u*u+np.logaddexp.reduce(terms,axis=0)
        top = float(exponent.max())
        raw = weights*np.exp(exponent-top)
        self.logM = top+math.log(raw.sum())
        self.u, self.p = u, raw/raw.sum()
        self.mu = float(self.p@u)
        self.d = u-self.mu
        self.var = float(self.p@(self.d**2))
        self.third = float(self.p@(self.d**3))
        self.muprime = 2*self.mu*self.var+self.third
        self.varprime = (2*self.mu*self.third+float(self.p@(self.d**4))
                         -self.var**2)

    def moment(self,k,y):
        return float(self.p@(abs(self.d)**k*np.exp(y*abs(self.d))))

    def jets(self,z):
        z = np.asarray(z,complex)
        phase = z.ravel()[:,None]*self.u
        cos, sin = np.cos(phase), np.sin(phase)
        return [(cos@self.p).reshape(z.shape),
                (-sin@(self.p*self.u)).reshape(z.shape),
                (-cos@(self.p*self.u**2)).reshape(z.shape)]

    def transfer(self):
        x = NCELL*math.pi/self.mu
        z2 = x*x+YBUFFER**2
        amin = 1-self.var*z2/2
        simple = z2*math.exp(self.mu*YBUFFER)*self.moment(2,YBUFFER)/2
        delta = (z2**1.5*math.exp(self.mu*YBUFFER)*self.moment(3,YBUFFER)
                 /(6*amin)) if amin>0 else None
        if not (amin>0 and delta is not None and 2*delta<1):
            return dict(passed=False,X=x,a_min=amin,delta_unadjusted=simple,
                        delta_adjusted=delta)
        radius = math.asin(2*delta)/self.mu
        passed = radius<min(YBUFFER,math.pi/(2*self.mu)) and x-radius>LX+2
        b = amin*(math.sin(self.mu*radius)-delta)
        c = b/(2*radius)
        kprime = 8*C/math.sqrt(7)*(6/7)**3/LX**2
        phase_bound = (math.pi/self.mu)**3*fourth_norm()/(720*LX**4)
        intensity_bound = 2*NCELL*radius*kprime+phase_bound
        logeta = math.log(EPS)-self.logM
        # I_1 <= pi*(eta/c)^2 * (1+log(1+(2r*c/eta)^2)).
        loga = logeta-math.log(c)
        soft = float(np.logaddexp(0,2*(math.log(2*radius)-loga)))
        logdisk = math.log(math.pi)+2*loga+math.log1p(soft)
        logoutside = math.log(4*x*YBUFFER)+2*logeta-2*math.log(b)
        log_integral = float(np.logaddexp(logoutside,math.log(2*NCELL)+logdisk))
        lapK = 8*C*C*(1/(LX**3*HY)+1/(LX*HY**3))
        logbias = math.log(lapK/(4*math.pi))+log_integral
        return dict(passed=bool(passed),X=x,a_min=amin,
                    delta_unadjusted=simple,delta_adjusted=delta,radius=radius,
                    outside_floor_f=b,quotient_floor_f=c,
                    log_eta=logeta,phase_intensity_bound=phase_bound,
                    intensity_transfer_bound=intensity_bound,
                    density_transfer_bound_at_y0=intensity_bound*C/HY,
                    log10_density_regulator_bound=logbias/math.log(10),
                    number_of_carrier_disks=2*NCELL)


def rectangle(x0,halfwidth,height,order):
    q,w = leggauss(order)
    corners = [x0-halfwidth-1j*height,x0+halfwidth-1j*height,
               x0+halfwidth+1j*height,x0-halfwidth+1j*height]
    z,dz = [],[]
    for a,b in zip(corners,corners[1:]+corners[:1]):
        z.extend((a+b)/2+(b-a)*q/2)
        dz.extend((b-a)*w/2)
    return np.array(z),np.array(dz)


def observables(source,x0,order=128,height=.75):
    z,dz = rectangle(x0,LX,height,order)
    f,f1,f2 = source.jets(z)
    q = (z-x0)/LX
    p = C/LX*(1-q*q)**4
    dp = -8*C/LX**2*q*(1-q*q)**3
    values = [np.dot(dz,p*f1/f)/(2j*math.pi),
              np.dot(dz,p*f2/f)/(2j*math.pi),
              np.dot(dz,dp*f2/f)/(2j*math.pi)]
    nodes = (np.arange(-NCELL,NCELL)+.5)*math.pi/source.mu
    lattice = float(np.sum(kernel((nodes-x0)/LX))/LX)
    return dict(x=x0,intensity=float(values[0].real),
                current_coefficient=float(values[1].real),
                intensity_time_derivative=float(values[2].real),
                model_intensity=source.mu/math.pi,
                model_current=-source.muprime*x0/math.pi,
                model_time_derivative=source.muprime/math.pi,
                lattice_intensity=lattice,
                max_imaginary_residue=float(max(abs(v.imag) for v in values)),
                sampled_contour_min_abs_f=float(abs(f).min()))


def compare(a,b):
    keys = ('intensity','current_coefficient','intensity_time_derivative')
    return {key:abs(a[key]-b[key]) for key in keys}


def row_errors(row):
    row['intensity_relative_error'] = abs(row['intensity']-row['model_intensity'])/row['model_intensity']
    row['time_derivative_relative_error'] = abs(row['intensity_time_derivative']-row['model_time_derivative'])/row['model_time_derivative']
    row['current_relative_error'] = (abs(row['current_coefficient']-row['model_current'])/abs(row['model_current']) if row['x'] else None)
    return row


def slice_case(t):
    source = Source(t)
    refined = Source(t,48,3.25,12)
    rows = []
    for x0 in (0.,1.,2.):
        a = observables(source,x0,96)
        b = observables(source,x0,160)
        source_check = observables(refined,x0,160)
        final = observables(refined,x0,224)
        displaced = observables(refined,x0,192,height=1.)
        final['contour_refinement_96_to_160'] = compare(a,b)
        final['source_refinement'] = compare(b,source_check)
        final['contour_refinement_160_to_224'] = compare(source_check,final)
        final['contour_height_check'] = compare(final,displaced)
        # Derivative checks compare separate time slices, not the same formula.
        fd=[]
        for step in (.5,.25):
            minus=observables(Source(t-step,48),x0,224)['intensity']
            plus=observables(Source(t+step,48),x0,224)['intensity']
            fd.append((plus-minus)/(2*step))
        final['time_derivative_fd_steps'] = [.5,.25]
        final['time_derivative_fd'] = fd
        final['time_derivative_richardson_error'] = abs((4*fd[1]-fd[0])/3-final['intensity_time_derivative'])
        rows.append(row_errors(final))
    # Count on auxiliary carrier-maxima walls; independent of filter endpoints.
    transfer=refined.transfer()
    z,dz=rectangle(0,transfer['X'],YBUFFER,160)
    f,f1,f2=refined.jets(z)
    count=np.dot(dz,f1/f)/(2j*math.pi)
    xx,yy=np.meshgrid(np.linspace(-transfer['X'],transfer['X'],33),
                      np.linspace(-YBUFFER,YBUFFER,17))
    grid=xx+1j*yy
    fg=refined.jets(grid)[0]
    sampled_carrier_error=float(np.max(abs(fg/(1-refined.var*grid*grid/2)
                                           -np.cos(refined.mu*grid))))
    return dict(t=t,logM=refined.logM,mu=refined.mu,variance=refined.var,
                third_centered_moment=refined.third,muprime=refined.muprime,
                variance_time_derivative=refined.varprime,
                sampled_adjusted_carrier_error=sampled_carrier_error,
                source_moment_refinement=dict(mu=abs(source.mu-refined.mu),
                    variance=abs(source.var-refined.var),logM=abs(source.logM-refined.logM)),
                transfer=transfer,outer_contour_count_real=float(count.real),
                outer_contour_count_imag=float(count.imag),observations=rows)


def time_average(order):
    q,w=leggauss(order)
    ww=w*kernel(q)
    sources=[Source(768+64*s,48) for s in q]
    sums=[]
    for x0 in (0.,1.,2.):
        records=[]
        for source in sources:
            records.append(observables(source,x0,224))
        keys=('intensity','current_coefficient','intensity_time_derivative',
              'model_intensity','model_current','model_time_derivative','lattice_intensity')
        row={key:float(ww@np.array([r[key] for r in records])) for key in keys}
        row['x']=x0
        row['minimum_sampled_contour_modulus']=min(r['sampled_contour_min_abs_f'] for r in records)
        sums.append(row_errors(row))
    mean_mu=float(ww@np.array([s.mu for s in sources]))
    mean_v=float(ww@np.array([s.var for s in sources]))
    variances=dict(mu=float(ww@np.array([(s.mu-mean_mu)**2 for s in sources])),
                   variance_parameter=float(ww@np.array([(s.var-mean_v)**2 for s in sources])),
                   covariance=float(ww@np.array([(s.mu-mean_mu)*(s.var-mean_v) for s in sources])))
    gates=[dict(t=s.t,**s.transfer()) for s in sources]
    return dict(center=768,halfwidth=64,order=order,observations=sums,
                source_parameter_covariances=variances,transfer_at_quadrature_nodes=gates)


def cosine_control():
    # Fixed-frequency genuine heat field; direct contour weight sums are known.
    mu, x0=.9,1.
    z,dz=rectangle(x0,LX,.75,160)
    q=(z-x0)/LX
    p=C/LX*(1-q*q)**4
    f=np.cos(mu*z);f1=-mu*np.sin(mu*z);f2=-mu*mu*f
    mass=np.dot(dz,p*f1/f)/(2j*math.pi)
    current=np.dot(dz,p*f2/f)/(2j*math.pi)
    nodes=(np.arange(-12,12)+.5)*math.pi/mu
    exact=float(np.sum(kernel((nodes-x0)/LX))/LX)
    return dict(intensity_error=float(abs(mass-exact)),current_error=float(abs(current)))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args()
    records=[]
    for t in (512.,768.,1024.):
        row=slice_case(t);records.append(row)
        print(t,'delta',row['transfer']['delta_adjusted'],
              'log10 regulator bound',row['transfer']['log10_density_regulator_bound'],
              'density relative errors',[r['intensity_relative_error'] for r in row['observations']],flush=True)
    avg12=time_average(12);avg20=time_average(20)
    for a,b in zip(avg12['observations'],avg20['observations']):
        b['time_quadrature_refinement_12_to_20']=compare(a,b)
    control=cosine_control()
    result=dict(status='floating diagnostics; no interval enclosures or independent implementation',
                prepared_for='Edward Baker',date='2026-10-24',model='gpt-6-astra',effort='max',
                python=platform.python_version(),numpy=np.__version__,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                parameters=dict(epsilon=EPS,lx=LX,hy=HY,y_buffer=YBUFFER,
                    time_range=[512,1024],slice_times=[512,768,1024],
                    x_centers=[0,1,2],y_centers=[0,.25,.5],
                    source_panel_width=.125,source_order=48,source_umax=3.25,ntheta=12,
                    contour_order=224,contour_halfheight=.75,
                    interpretation='Density, current and time derivative equal coefficients times k(y/h)/h in the zero-measure limit, under the stated local real-zero premises.'),
                kernel_fourth_derivative_L1=fourth_norm(),
                slices=records,time_average=avg20,cosine_control=control,
                collision_control=dict(field='(1+exp(4*(t-1/4))*cos(2*z))/2',
                    event_t=.25,event_x=math.pi/2,source_mean_at_event=1.,
                    source_variance_at_event=1.,
                    a_min_on_contract=1-((6*math.pi)**2+YBUFFER**2)/2,
                    outcome='carrier nonvanishing gate fails at the double event'))
    Path(args.output).write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
