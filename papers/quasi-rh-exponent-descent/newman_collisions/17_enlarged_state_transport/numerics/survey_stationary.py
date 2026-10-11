#!/usr/bin/env python3
"""Exploratory physical stationary jets; no numerical output is a certificate.

At fixed t,N the complete finite travelling sum has physical jets
K_j=(A F)^(j)/A. All normalizer, beta' and beta'' corrections are retained.
50-digit Decimal computes only the large base phase; sampled sums are doubles.
All sign-change brackets on the stated grid are kept. Even roots and root pairs
within one grid interval can be missed; this is not complete root isolation.
"""
import argparse, cmath, hashlib, json, math, platform, time
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np
PI='3.141592653589793238462643383279502884197169399375105820974944592307816406286'

def coeff(x,t):
    s=(1-1j*x)/2
    a=1/(2*s)+1/(s-1)+.5*cmath.log(s/(2*math.pi))
    ap=-1/(2*s*s)-1/(s-1)**2+1/(2*s)
    app=1/s**3+2/(s-1)**3-1/(2*s*s)
    appp=-3/s**4-6/(s-1)**4+1/s**3
    return a,ap,app,appp

class Model:
    def __init__(self,N,time_shift):
        self.N=N
        with localcontext() as ctx:
            ctx.prec=60
            pi=Decimal(PI); dn=Decimal(N); ln=dn.ln()
            xx=4*pi*dn*dn; tt=1/(2*ln)+Decimal(time_shift)
            self.x0=float(xx); self.t=float(tt); self.logN=float(ln)
            # alpha at x0. atan x=pi/2-atan(1/x), tiny series retained.
            y=1/xx; atanx=pi/2-(y-y**3/3+y**5/5)
            lc=(1+y*y).ln()
            ar=ln+lc/4-1/(1+xx*xx)
            ai=3*xx/(1+xx*xx)-atanx/2
            carrier=pi*(N%2)-pi+atanx/4-xx*lc/8+tt*ai*(ar-ln)/2
            T=(xx-tt*ai)/2
            delta=[]; phase=[]; ell=[]
            for n in range(1,N+1):
                en=Decimal(n).ln(); de=ln-en
                ph=(carrier-T*de)%(2*pi)
                ell.append(float(en)); delta.append(float(de)); phase.append(float(ph))
            self.base_meta={'x0':str(xx),'t':str(tt),'N':N,'time_shift':time_shift}
        self.ell=np.array(ell); self.delta=np.array(delta)
        self.a0=coeff(self.x0,self.t)[0]
        amp=np.exp(self.t*self.ell**2/4-(.5+self.t*self.a0.real/2)*self.ell)
        self.q0=amp*np.exp(1j*np.array(phase))
        self.b0,self.bp0,self.bpp0=self.betas(0.)

    def betas(self,h):
        a,ap,app,appp=coeff(self.x0+h,self.t)
        v=a-self.ell
        b=-.5j*v*(1+self.t*ap/2)
        bp=-.25*(ap*(1+self.t*ap/2)+v*self.t*app/2)
        bpp=.125j*(app*(1+1.5*self.t*ap)+v*self.t*appp/2)
        return b,bp,bpp

    def jets(self,h):
        x=self.x0+h; t=self.t
        a=coeff(x,t)[0]; a0=self.a0
        # Stable exact formula for change of theta+T log N.
        lc=math.log1p(1/x**2); lc0=math.log1p(1/self.x0**2)
        carr=h/4-x/4*math.log1p(h/self.x0) \
             +(math.atan(x)-math.atan(self.x0))/4-(x*lc-self.x0*lc0)/8 \
             +t/2*(a.imag*(a.real-self.logN)-a0.imag*(a0.real-self.logN))
        Td=(h-t*(a.imag-a0.imag))/2
        q=self.q0*np.exp(-t*(a.real-a0.real)*self.ell/2+1j*(carr-Td*self.delta))
        b,bp,bpp=self.betas(h)
        fac=(np.ones(self.N),b,b*b+bp,b*b*b+3*b*bp+bpp)
        return np.array([2*np.real(np.sum(q*v)) for v in fac])

    def errors(self,h):
        x=self.x0+h; t=self.t; L=math.log(x/(4*math.pi))
        a,ap,app,appp=coeff(x,t)
        lam=(-.5j*a*(1+t*ap/2)).real
        lam1=(-.25*(ap*(1+t*ap/2)+a*t*app/2)).real
        lam2=(.125j*(app*(1+1.5*t*ap)+a*t*appp/2)).real
        c2=lam*lam+lam1; c3=lam**3+3*lam*lam1+lam2
        eta=5*math.exp(-t*L*L/16-L/4)
        e=[eta,eta*L,eta*2*L*L,eta*6*L**3]
        eps=[e[0],e[1]+abs(lam)*e[0],e[2]+2*abs(lam)*e[1]+abs(c2)*e[0],
             e[3]+3*abs(lam)*e[2]+3*abs(c2)*e[1]+abs(c3)*e[0]]
        return np.array(eps),lam

    def grid(self,left,right,step):
        hs=np.linspace(left,right,int(round((right-left)/step))+1)
        # Grid is a frozen-frequency locator only; root refinement is physical.
        f=np.stack([self.q0*v for v in (self.b0,self.b0**2+self.bp0)])
        out=np.empty((len(hs),2))
        for start in range(0,len(hs),64):
            sub=hs[start:start+64]
            phase=np.exp(-.5j*sub[:,None]*self.delta[None,:])
            out[start:start+len(sub)]=2*np.real(phase@f.T)
        return hs,out

    def refine(self,j,l,r):
        fl=self.jets(l)[j]; fr=self.jets(r)[j]
        if fl*fr>0: return None
        h=(l+r)/2
        for _ in range(12):
            k=self.jets(h); f=k[j]
            if abs(f)<1e-10 or r-l<1e-10: break
            if fl*f<=0: r=h; fr=f
            else: l=h; fl=f
            eps,lam=self.errors(h)
            candidate=h-f/(k[j+1]-lam*f)
            h=candidate if l<candidate<r else (l+r)/2
        k=self.jets(h); eps,lam=self.errors(h)
        E=k[0]**2+k[1]**2
        dlo=np.maximum(np.abs(k[:2])-eps[:2],0)
        e_min=float(np.sum(dlo**2))
        e_max=float(np.sum((np.abs(k[:2])+eps[:2])**2))
        product=float(k[j-1]*k[j+1])
        # Root displacement estimate solely diagnostic, excludes source payment.
        slope=k[j+1]-lam*k[j]
        return {'stationary_order':j,'offset':float(h),'root_residual':float(k[j]),
          'K':k.tolist(),'E':float(E),'signed_stationary_product':product,
          'signed_product_over_E':float(product/E),'epsilon':eps.tolist(),
          'nominal_E_range_after_absolute_disk_payment':[e_min,e_max],
          'first_jet_detectability':float(np.sqrt(np.sum((k[:2]/eps[:2])**2))),
          'point_sign_survives_naive_disk_payment':bool((abs(k[j-1])>eps[j-1]) and (abs(k[j+1])>eps[j+1])),
          'nominal_stationary_displacement_from_error':float(eps[j]/abs(slope)),
          'last_refinement_bracket':[l,r]}

def compact(result):
    rows=result['all_detected_roots']
    result['detected_root_columns']=['stationary_order','offset','K0','K1','K2','K3','E','signed_product_over_E']
    result['all_detected_roots']=[[c['stationary_order'],c['offset'],*c['K'],c['E'],c['signed_product_over_E']] for c in rows]
    result['disk_payment_ranges_at_detected_roots']=[[min(c['epsilon'][j] for c in rows),max(c['epsilon'][j] for c in rows)] for j in range(4)]
    result['root_diagnostics']={str(j):{'count':sum(c['stationary_order']==j for c in rows),
      'positive_products':sum(c['stationary_order']==j and c['signed_stationary_product']>0 for c in rows),
      'naive_point_product_sign_survives_absolute_payment':sum(c['stationary_order']==j and c['point_sign_survives_naive_disk_payment'] for c in rows)} for j in (1,2)}
    result['max_abs_root_residual']=max(abs(c['root_residual']) for c in rows)
    result['smallest_E_by_stationary_order']={str(j):min((c for c in rows if c['stationary_order']==j),key=lambda c:c['E']) for j in (1,2)}
    result.pop('smallest_E_roots',None)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--N',type=int,default=22066); p.add_argument('--time-shift',default='0')
    p.add_argument('--left',type=float,default=0); p.add_argument('--right',type=float,default=256)
    p.add_argument('--step',type=float,default=.0625); p.add_argument('--record',type=Path,required=True)
    args=p.parse_args(); started=time.perf_counter(); m=Model(args.N,args.time_shift)
    assert args.left < args.right and args.step > 0
    assert 0 < m.t <= .05
    cutoff=[(m.x0+h)/(4*math.pi)+m.t/16 for h in (args.left,args.right)]
    assert args.N**2 <= cutoff[0] and cutoff[1] < (args.N+1)**2
    kappas=[m.t*math.log((m.x0+h)/(4*math.pi)) for h in (args.left,args.right)]
    assert 1-1e-14 <= min(kappas) and max(kappas) <= 1.5
    hs,grid=m.grid(args.left,args.right,args.step)
    candidates=[]; dropped=[]
    for j in (1,2):
        for i in np.flatnonzero(grid[:-1,j-1]*grid[1:,j-1]<0):
            row=m.refine(j,float(hs[i]),float(hs[i+1]))
            if row is None: dropped.append([j,float(hs[i]),float(hs[i+1])])
            else: candidates.append(row)
    validation=[]
    for h in (0.35,87.41,(args.left+args.right)/2):
        step=1e-4
        k=m.jets(h); fd=(m.jets(h+step)-m.jets(h-step))/(2*step)
        eps,lam=m.errors(h)
        exact=k[1:]-lam*k[:3]
        error=np.max(np.abs(fd[:3]-exact)/(1+np.abs(exact)))
        assert error<2e-6,(h,error)
        validation.append({'offset':h,'max_scaled_differentiation_residual':float(error),'K':k.tolist()})
    assert max(abs(c['root_residual']) for c in candidates)<1e-5
    result={'status':'EXPLORATORY_NOT_CERTIFIED','date':'2026-10-10',
      'prepared_for':'Edward Baker','model_family':'GPT-6 (Codex)',
      'reasoning_effort':'not exposed to this worker; not inferred',
      'acknowledgment':'Prepared with substantial LLM assistance; internal diagnostic only.',
      'parameters':vars(args)|{'record':args.record.name},'base':m.base_meta,
      'formulas':{'beta':'(-i/2)(alpha-log n)(1+t alpha_s/2)',
       'beta_prime':'-1/4 [alpha_s(1+t alpha_s/2)+(alpha-log n)t alpha_ss/2]',
       'beta_second':'i/8 [alpha_ss(1+3t alpha_s/2)+(alpha-log n)t alpha_sss/2]',
       'K':'2 Re sum q_n [1,beta,beta^2+beta_prime,beta^3+3 beta beta_prime+beta_second]',
       'epsilon':'Complete imported disk |e|<=eta gives Cauchy j! L^j eta, conjugated by full normalizer A.'},
      'cutoff_squared_endpoints':cutoff,'kappa_endpoints':kappas,
      'grid_point_count':len(hs),'root_counts':{str(j):sum(c['stationary_order']==j for c in candidates) for j in (1,2)},
      'dropped_frozen_brackets':dropped,'all_detected_roots':candidates,
      'smallest_E_roots':[{'stationary_order':c['stationary_order'],'offset':c['offset'],'E':c['E'],
         'K':c['K'],'first_jet_detectability':c['first_jet_detectability']} for c in sorted(candidates,key=lambda c:c['E'])[:16]],
      'validation':validation,'limitations':[
       'Floating arithmetic is used for all sums and diagnostics; there are no certified intervals or sign claims.',
       'Every sign-changing grid root is retained, but even roots and multiple roots in a single grid gap may be missed.',
       'The disk error is imported conditionally, evaluated as scalar diagnostic only; no spatial-time enclosure is supplied.',
       'Nominal E ranges are pointwise arithmetic diagnostics; genuine stationary points can move under the disk error.',
       'The base follows N floor sqrt(x/(4pi)+t/16); the requested offset domain must stay inside its cutoff chamber.'],
      'runtime_seconds':time.perf_counter()-started,'python_version':platform.python_version(),'numpy_version':np.__version__,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result=compact(result)
    args.record.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({k:result[k] for k in ('root_counts','root_diagnostics','smallest_E_by_stationary_order','validation','runtime_seconds')},indent=2))
if __name__=='__main__': main()
