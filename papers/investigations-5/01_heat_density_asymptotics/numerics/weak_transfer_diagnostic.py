#!/usr/bin/env python3
"""HDA-17-AN01 r1 bounded floating diagnostic; no continuous enclosure.
Prepared for Edward Baker, 2026-10-24, gpt-6.1-sol effort ultra.
Requires numpy, mpmath; companion weak_coefficients.py and exact_controls.py.
Run with --repo /path/to/checkout --output /path/to/small.json.
"""
import argparse, hashlib, json, math, os, platform, sys, time, re, subprocess
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp
mp.mp.dps=80
US=1.5; ETA=.5; PI=math.pi
MESHES=[192,384,768]; TIMES=[64,96,128]; ORDERS=[16,32,64]
POINTS=[(0,0),(0,.5),(4,0),(4,.5)]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lse(a):return float(np.logaddexp.reduce(np.asarray(a).ravel()))
def phi(u,n=4):
    u=np.asarray(u); a=PI*np.arange(1,n+1)[:,None]**2*np.exp(4*u.reshape(-1))
    ans=(2*PI**(-.25)*np.arange(1,n+1)[:,None]**(-.5)*np.exp(2.25*np.log(a)-a)*(1-1.5/a)).sum(0)
    return ans.reshape(u.shape)
def phi_mp(u,n=4):
    return mp.fsum((2*mp.pi**2*k**4*mp.exp(9*u)-3*mp.pi*k*k*mp.exp(5*u))*mp.exp(-mp.pi*k*k*mp.exp(4*u)) for k in range(1,n+1))
C=float(phi_mp(mp.mpf(0),16)*mp.sqrt(mp.pi)/2)
def budget(m,t,n=4):
    u=np.linspace(0,US,m+1);a=u[:-1];b=u[1:];h=US/m
    terms=[]
    for k in range(1,9):
        lo=PI*k*k*np.exp(4*a); hi=PI*k*k*np.exp(4*b)
        for p,c in zip([1.25,2.25,3.25,4.25],[75,330,224,32]):
            v=np.clip(p,lo,hi); terms.append(-.25*math.log(PI)-.5*math.log(k)+math.log(c)+p*np.log(v)-v)
    lo=PI*81*np.exp(4*a); rat=(1+1/9)**8*np.exp(-PI*19*np.exp(4*a))
    for p,c in zip([1.25,2.25,3.25,4.25],[75,330,224,32]):
        terms.append(-.25*math.log(PI)-.5*math.log(9)+math.log(c)+p*np.log(lo)-lo-np.log1p(-rat))
    logbc=np.logaddexp.reduce(np.array(terms),axis=0)
    aa=PI*(n+1)**2*np.exp(4*u)
    ratio=(1+1/(n+1))**4*np.exp(-PI*(2*n+3)*np.exp(4*u))
    logmode=math.log(2*PI**2*(n+1)**4)+9*u-aa-np.log1p(-ratio)
    f=phi(u,n)
    with np.errstate(divide='ignore'):logsigma=np.logaddexp(math.log(1e-12)+np.log(f),math.log(1e-300))
    rows=[]
    for j in range(4):
        lw=j*np.log(b)+t*b*b+b
        li=lse(logbc+3*math.log(h)+lw-math.log(12))
        lm=lse(np.logaddexp(logmode[:-1],logmode[1:])+math.log(h/2)+lw)
        la=lse(np.logaddexp(logsigma[:-1],logsigma[1:])+math.log(h/2)+lw)
        U=mp.mpf('1.5');lam=4*mp.pi*mp.exp(4*U)-2*t*U-10-j/U
        assert lam>0 and 16*mp.pi*mp.exp(4*U)>=2*t
        lt=mp.log(2*mp.pi**2/(1-16*mp.exp(-3*mp.pi)))+j*mp.log(U)+t*U**2+10*U-mp.pi*mp.exp(4*U)-mp.log(lam)
        # Preserve analytic tail logarithm even when below IEEE representability.
        total=float(mp.exp(li)+mp.exp(lm)+mp.exp(la)+mp.exp(lt))
        rows.append(dict(j=j,interpolation=math.exp(li),omitted_modes=math.exp(lm),complete_tail_log10=float(lt/mp.log(10)),nodal_arithmetic_candidate=math.exp(la),total=total,log10_categories=[li/math.log(10),lm/math.log(10),float(lt/mp.log(10)),la/math.log(10)]))
    return rows

def rule(m,order):
    v,w=leggauss(order);nodes=np.linspace(0,US,m+1);h=US/m
    u=(nodes[:-1,None]+(v+1)*h/2).ravel();f=phi(nodes)
    vals=(f[:-1,None]*(1-v)/2+f[1:,None]*(1+v)/2).ravel()
    return u,np.tile(w*h/2,m)*vals

def jets(t,z,rule):
    u,w=rule;e=np.exp(t*u*u)*w;z=np.asarray(z).reshape(-1)
    out=np.zeros((len(z),4),complex)
    for k in range(0,len(z),96):
        zu=z[k:k+96,None]*u;co=np.cos(zu);si=np.sin(zu)
        out[k:k+96]=np.stack([co@e,-si@(e*u),-co@(e*u*u),si@(e*u**3)],axis=1)
    return out

def regulator(t,x):
    x=np.asarray(x);rb=2*math.log(ETA*C)-.5*math.log1p(t*t);rbt=-t/(1+t*t)
    if t<=64:a,at,b,bt=rb,rbt,0.,0.;L=kap=chi=chip=0.
    else:
        L=float(-mp.lambertw(-8*mp.pi/t*mp.exp(-18/mp.mpf(t)),-1)/4-mp.mpf(9)/(2*t))
        kap=8*t*L-2*t+36;Lp=2*L/kap;kp=8*L+8*t*Lp-2
        logM=math.log(2*PI**2)+t*L*L+9*L-PI*math.exp(4*L)+.5*math.log(2*PI/kap)
        ap=2*logM-2*math.log(kap);apt=2*L*L-3*kp/kap
        if t>=128:chi,chip=1.,0.
        else:
            v=(t-64)/64;chi=1/(1+math.exp(1/v-1/(1-v)));chip=chi*(1-chi)*(v**-2+(1-v)**-2)/64
        a=(1-chi)*rb+chi*ap;at=(1-chi)*rbt+chi*apt+chip*(ap-rb)
        b=chi/kap;bt=chip/kap-chi*kp/(kap*kap)
    r=a-b*x*x;rt=at-bt*x*x;rx=-2*b*x;rxx=np.full(x.shape,-2*b);rtx=-2*bt*x;rtxx=np.full(x.shape,-2*bt)
    return dict(q=np.exp(r),r=r,rt=rt,rx=rx,rxx=rxx,rtx=rtx,rtxx=rtxx),dict(a=a,at=at,beta=b,betat=bt,L=L,kappa=kap,chi=chi,chip=chip,saddle_residual=(4*PI*math.exp(4*L)-2*t*L-9) if t>64 else None)

def indices(n):return [(i,j) for k in range(n+1) for i in range(k+1) for j in [k-i]]
def target(name,al,L):
    if name=='DeltaQ':return .01
    if name=='Q':return .001 if al==(0,0) else .01*max(1,L)
    return .0001*max(1,L)
def key(n,al):return n+':'+str(al[0])+','+str(al[1])

def values(g,reg,k):
    # Weak identities evaluate the actual finite-field observables, E=0.
    wts=k['signed_weights'];cv=lambda al,f: np.sum(wts[al]*f)
    q=reg['q'];rt=reg['rt'];rx=reg['rx'];rxx=reg['rxx'];rtx=reg['rtx'];rtxx=reg['rtxx']
    D=abs(g[:,0])**2+q;S=np.log(D);w=q/D;c=w*(1-w)
    V=g[:,2]*np.conj(g[:,0])/D;V1=w*V;V2=w*w*V
    st=-2*V.real+rt*w;wt=rt*c+2*V1.real;ct=rt*c*(1-2*w)+2*(V1-2*V2).real
    cc=rxx+rx*rx;b=rt+cc/2
    def add(a,i,j):return a[0]+i,a[1]+j
    U={a:cv(a,S) for a in indices(4)}
    J={a:(cv(add(a,1,0),V)+1j*cv(add(a,0,1),V)+cv(a,rx*V1))/(2*PI) for a in indices(3)}
    out={}
    for a in indices(4):out[key('U',a)]=U[a];out[key('W',a)]=cv(a,w)
    for a in indices(2):
        ax=add(a,1,0);axx=add(a,2,0);ayy=add(a,0,2)
        cur=(2*cv(ax,w*rx)-cv(a,w*rxx+c*rx*rx))/(4*PI)
        curt=(2*cv(ax,wt*rx+w*rtx)-cv(a,wt*rxx+w*rtxx+ct*rx*rx+2*c*rx*rtx))/(4*PI)
        rtval=(cv(axx,st)+cv(ayy,st))/(4*PI)-curt
        prod=0.
        for i,sign in [((1,0),1),((0,1),-1)]:
            for be in indices(sum(a)):
                if be[0]<=a[0] and be[1]<=a[1]:
                    ga=(a[0]-be[0],a[1]-be[1]);comb=math.comb(a[0],be[0])*math.comb(a[1],be[1])
                    prod+=sign*comb*U[(be[0]+i[0],be[1]+i[1])]*U[(ga[0]+i[0],ga[1]+i[1])]
        Q=4*cv(a,V.real)-cv(axx,S)+cv(ayy,S)+cv(a,cc*w)-prod
        row=dict(R=(U[axx]+U[ayy])/(4*PI)-cur,C=cur,J=J[a],Q=Q,Ut=cv(a,st),Wt=cv(a,wt),Rt=rtval,Ct=curt,B=cv(a,b*w),source=rtval+J[ax].real+J[add(a,0,1)].imag)
        for n,v in row.items():out[key(n,a)]=v
    out['DeltaQ']=out[key('Q',(2,0))]+out[key('Q',(0,2))]
    return out

def cleanval(v):
    v=complex(v);return [v.real,v.imag] if abs(v.imag)>0 else v.real

def local_t64(g,ds,k,rt,q):
    # LC7--11, all overlapping derivatives, same field and errors.
    wts=k['signed_weights'];cv=lambda a,f:float(np.sum(abs(wts[a])*f));e=np.sqrt(q)
    P=abs(g)+np.array(ds);m=np.maximum(abs(g[:,0])-ds[0],0);M=abs(g[:,0])+ds[0]
    cl=lambda x:np.clip(x,m,M)
    av=cl(e/math.sqrt(5));bv=cl(e);wv=cl(e/math.sqrt(3))
    A=q/(PI*(q+m*m)**2);A1=4*q*av/(PI*(q+av*av)**3);a=bv/(q+bv*bv);bb=1/(q+m*m);ww=2*q*wv/(q+wv*wv)**2
    R=2*A*P[:,1]*ds[1]+A1*P[:,1]**2*ds[0]
    J=A*(P[:,1]*ds[2]+P[:,2]*ds[1])+A1*P[:,1]*P[:,2]*ds[0]
    E13=A*(P[:,1]*ds[3]+P[:,3]*ds[1])+A1*P[:,1]*P[:,3]*ds[0]
    W=ww*ds[0];rho=A*P[:,1]**2;src=abs(rt)*(R+2*rho*W)
    Rt=2*E13+src+4*(P[:,2]*a*R+rho*(a*ds[2]+P[:,2]*bb*ds[0]))
    d=2*a*ds[1]+2*P[:,1]*bb*ds[0];G=2*P[:,1]*a
    env=dict(R=R,J=J,Rt=Rt,U=2*a*ds[0],Ut=2*(a*ds[2]+P[:,2]*bb*ds[0])+abs(rt)*W,W=W,B=abs(rt)*W,source=src,C=np.zeros(len(g)))
    out={}
    for name,f in env.items():
        for al in indices(4 if name in ('U','W') else 2):out[key(name,al)]=cv(al,f)
    for al in indices(2):
        # Product derivative comparison, constant component sum over x/y.
        E=2*cv(al,G*d)
        for be in indices(sum(al)):
            if be[0]<=al[0] and be[1]<=al[1]:
                ga=(al[0]-be[0],al[1]-be[1]);cc=math.comb(al[0],be[0])*math.comb(al[1],be[1])
                E+=cc*(cv(be,d)*cv(ga,G)+cv(be,G)*cv(ga,d))
        out[key('Q',al)]=2*E
    # LC10 direct |Delta K| rather than triangle pure derivatives.
    dk=abs(wts[(2,0)]+wts[(0,2)]);convD=lambda f:float(np.sum(dk*f));zero=(0,0)
    out['DeltaQ']=2*(2*convD(G*d)+2*cv(zero,d)*convD(G)+2*cv(zero,G)*convD(d)+4*sum(cv(al,G)*cv(al,d) for al in [(1,0),(0,1)]))
    return out

def mp_check(t,z,m,order=10):
    checks=[]
    for dps in (80,120):
        mp.mp.dps=dps;x,w=mp.gauss_quadrature(order,'legendre');hh=mp.mpf('1.5')/m;out=[mp.mpc(0) for _ in range(4)]
        zz=mp.mpc(float(z.real),float(z.imag));fixed_nodes=phi(np.linspace(0,US,m+1))
        for i in range(m):
            a=i*hh;fa=mp.mpf(float(fixed_nodes[i]));fb=mp.mpf(float(fixed_nodes[i+1]))
            for v,ww in zip(x,w):
                u=a+(v+1)*hh/2;f=fa*(1-v)/2+fb*(1+v)/2;ee=mp.exp(t*u*u)*f*ww*hh/2
                co=mp.cos(zz*u);si=mp.sin(zz*u)
                for j,val in enumerate([co,-u*si,-u*u*co,u**3*si]):out[j]+=ee*val
        checks.append(out)
    mp.mp.dps=80
    double=jets(t,[z],rule(m,order))[0]
    return dict(coefficient_scope='identical binary64 nodal coefficients promoted exactly; isolates later evaluator and source-node geometry rounding from nodal coefficients',t=t,z=[z.real,z.imag],cells=m,dps=[80,120],precision_change=[str(abs(a-b)) for a,b in zip(*checks)],double_abs_error=[float(abs(mp.mpc(complex(v))-r)) for v,r in zip(double,checks[-1])],physical_jet_abs=[float(abs(v)) for v in checks[-1]])

def write_record_bundle(record,output):
    """Partition small diagnostic records by time, each below 1 MiB.

    This is lossless JSON packaging, not another numerical computation.
    """
    record=dict(record);observations=record.pop('observations');parts=[]
    for t in TIMES:
        path=output.with_name(output.stem+f'_T{t}.json')
        part=dict(status=record['status'],request=record['request'],t=t,row_columns=record['row_columns'],observations=[o for o in observations if o['t']==t])
        path.write_text(json.dumps(part,separators=(',',':'),allow_nan=False)+'\n')
        assert path.stat().st_size<1048576
        parts.append(dict(file=path.name,sha256=sha(path),bytes=path.stat().st_size,t=t))
    record['observation_records']=parts
    output.write_text(json.dumps(record,indent=1,allow_nan=False)+'\n')
    assert output.stat().st_size<1048576

def run(repo,output):
    from weak_coefficients import kernel_data,weak_coefficients
    started=time.perf_counter();record=dict(status='floating diagnostic; all continuous and rounding gates unpaid',request='HDA-17-AN01 r1',model='gpt-6.1-sol',effort='ultra',date='2026-10-24 America/New_York',thread_id='01a170a3-5f6e-7aa2-9e33-bcae4835c782',environment=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__,platform=platform.platform(),blas_threads=os.environ.get('OPENBLAS_NUM_THREADS')),source_orders=[0,2],source_quadrature_orders=[6,10],filter_orders=ORDERS,source=[],observations=[])
    budgets={(m,t):budget(m,t) for m in MESHES for t in TIMES};sources={m:rule(m,6) for m in MESHES};kernels={o:kernel_data(o) for o in ORDERS}
    for (m,t),bs in budgets.items():record['source'].append(dict(cells=m,t=t,jets=bs))
    allrows=[];filterratios=[];worstnodes=[];alternate=None
    for t in TIMES:
        # Continuous scalar Pj majorant from source positive moments + error.
        caps=[budgets[(192,t)][j]['total'] for j in range(4)]
        ur,wr=sources[192];P=np.array([sum(wr*np.exp(t*ur*ur+ur)*ur**j)+3*caps[j] for j in range(4)])
        reg10,params=regulator(t,np.array([-10.,0.,10.]))
        for x,y in POINTS:
            obs=dict(t=t,x=x,y=y,regulator=params,meshes=[])
            for m in MESHES:
                ds=[z['total'] for z in budgets[(m,t)]];byorder={};allowBy={};localBy={}
                for order in ORDERS:
                    k=kernels[order];z=x+1j*y-k['x']-1j*k['y'];g=jets(t,z,sources[m]);reg,_=regulator(t,z.real)
                    vals=values(g,reg,k);byorder[order]=vals
                    # Fixed caps from baseline; all refinements checked <= these.
                    result=weak_coefficients(g,**{n:reg[n] for n in ('q','rt','rx','rxx','rtx','rtxx')},bar0=caps[0],bar2=caps[2],kernel=k)
                    # Scalar full D+ domain caps; endpoint regulator formula exact in x².
                    scalarresult=weak_coefficients(g,**{n:reg[n] for n in ('q','rt','rx','rxx','rtx','rtxx')},bar0=caps[0],bar2=caps[2],kernel=k,scalar=True,field_caps=dict(P0=P[0],P2=P[2]),reg_caps=dict(q_min=float(min(reg10['q'])),q_max=float(max(reg10['q'])),a0=float(max(abs(reg10['rt']))),R1=float(max(abs(reg10['rx']))),R2=float(max(abs(reg10['rxx']))),T1=float(max(abs(reg10['rtx']))),T2=float(max(abs(reg10['rtxx']))),Th=float(max(abs(2*reg10['rx']*reg10['rtx']))),b0=float(max(abs(reg10['rt']+(reg10['rxx']+reg10['rx']**2)/2))),c0=float(max(abs(reg10['rxx']+reg10['rx']**2)))))
                    rows=result['rows'];meta=result['metadata'];sc=scalarresult['rows'];scmeta=scalarresult['metadata'];allowBy[order]=rows
                    if t==64:localBy[order]=local_t64(g,ds,k,reg['rt'],reg['q'])
                    if order==64:
                        # Float source-rule refinement, including all actual rows.
                        refined=values(jets(t,z,rule(m,10)),reg,k)
                        refine={n:float(abs(refined[n]-vals[n])) for n in vals}
                        if (t,x,y,m)==(64,4,.5,768):
                            tight=weak_coefficients(g,**{n:reg[n] for n in ('q','rt','rx','rxx','rtx','rtxx')},bar0=ds[0],bar2=ds[2],kernel=k)['rows']
                            alternate={n:dict(ABC=co.tolist(),source_allowance=float(co[0]*ds[0]+co[1]*ds[2])) for n,co in tight.items() if not (n.startswith('J:') and sum(map(int,n.split(':')[1].split(',')))==3)}
                        amp=abs(g[:,0])/np.sqrt(reg['q']);ii=int(np.argmin(amp));worstnodes.append((float(amp[ii]),t,complex(z[ii]),m))
                last=allowBy[64];lr=localBy.get(64,{});data=[]
                for n,co in last.items():
                    if n.startswith('J:') and sum(map(int,n.split(':')[1].split(',')))==3:continue
                    if n=='DeltaQ':name,al='DeltaQ',(0,0);ln=0
                    else:name,idx=n.split(':');al=tuple(map(int,idx.split(',')));ln=kernels[64]['L'][al]
                    th=target(name,al,ln);co=np.array(co);scalar=np.array(sc[n]);anal=float(co[0]*ds[0]+co[1]*ds[2]);scval=float(scalar[0]*ds[0]+scalar[1]*ds[2])
                    fd=float(abs(byorder[64][n]-byorder[32][n]));fdold=float(abs(byorder[32][n]-byorder[16][n]));pfdold=float(abs(np.dot(allowBy[32][n]-allowBy[16][n],np.array([ds[0],ds[2],0.]))));pfd=float(abs(np.dot(last[n]-allowBy[32][n],np.array([ds[0],ds[2],0.]))))
                    sourcecats=[co[0]*budgets[(m,t)][0][cat]+co[1]*budgets[(m,t)][2][cat] for cat in ('interpolation','omitted_modes','nodal_arithmetic_candidate')]
                    tailterms=[math.log(v)/math.log(10)+budgets[(m,t)][j]['complete_tail_log10'] for v,j in ((co[0],0),(co[1],2)) if v>0]
                    taillog=float(np.logaddexp.reduce(np.array(tailterms)*math.log(10))/math.log(10)) if tailterms else None
                    row=dict(positive_filter_change_16_32=pfdold,local_positive_filter_change_32_64=abs(lr[n]-localBy[32][n]) if n in lr else None,positive_filter_change_32_64=pfd,positive_filter_ratio=pfd/(.1*th),source_categories=sourcecats,source_tail_log10=taillog,row=n,target=th,ABC=co.tolist(),source_allowance=anal,source_ratio=anal/(.8*th),scalar_allowance=scval,scalar_ratio=scval/(.8*th),filter_change_32_64=fd,filter_ratio=fd/(.1*th),filter_change_16_32=fdold,evaluator_change_6_10=refine[n],evaluator_ratio=refine[n]/(.1*th),value64=cleanval(byorder[64][n]),evaluation_rounding='unpaid',filter_enclosure='unpaid')
                    if n in lr:row.update(local_allowance=lr[n],local_ratio=lr[n]/(.8*th))
                    data.append(row);allrows.append(dict(t=t,x=x,y=y,cells=m,**row))
                # Preserve six physical values for most informative rows, all coefficient rows retained.
                req0=min([caps[0]]+[.4*r['target']/r['ABC'][0] for r in data if r['ABC'][0]>0])
                req2=min([caps[2]]+[.4*r['target']/r['ABC'][1] for r in data if r['ABC'][1]>0])
                obs['meshes'].append(dict(CJ21_requirements=dict(d0=req0,d2=req2,status='diagnostic coefficient table; quadrature and arithmetic unpaid'),cells=m,caps=caps,rows=data,cap_meta=meta,scalar_meta=scmeta))
            record['observations'].append(obs)
            print('completed',t,x,y,'elapsed',round(time.perf_counter()-started,2),flush=True)
    record['maxima']={}
    for metric in ('source_ratio','scalar_ratio','filter_ratio','evaluator_ratio','positive_filter_ratio','local_ratio'):
        candidates=[v for v in allrows if metric in v];record['maxima'][metric]=max(candidates,key=lambda v:v[metric])
    record['mesh_maxima']={str(m):{metric:max((v for v in allrows if v['cells']==m and metric in v),key=lambda v:v[metric]) for metric in ('source_ratio','scalar_ratio','filter_ratio','evaluator_ratio')} for m in MESHES}
    # At most two worst pointwise amplitude cases; one 120-digit check each.
    worstnodes.sort();chosen=[]
    for amp,t,z,m in worstnodes:
        if not any(t==v[1] and m==v[3] for v in chosen):chosen.append((amp,t,z,m))
        if len(chosen)==2:break
    record['alternate_frozen_768_caps_t64_x4_yhalf']=alternate
    record['high_precision_checks']=[mp_check(t,z,m) for amp,t,z,m in chosen]
    # Source candidate is only a candidate; all float node comparisons include underflowed nodes.
    maxratio=0.;nodetime=time.perf_counter()
    for m in MESHES:
        for i,f in enumerate(phi(np.linspace(0,US,m+1))):
            true=phi_mp(mp.mpf('1.5')*i/m);err=abs(mp.mpf(float(f))-true);sig=mp.mpf('1e-12')*abs(mp.mpf(float(f)))+mp.mpf('1e-300');maxratio=max(maxratio,float(err/sig))
    record['nodal_candidate']=dict(formula='1e-12 Phi_N(binary64 node)+1e-300; tested against exact rational i*1.5/m',sample_max_error_ratio=maxratio,status='candidate only; no continuous rounding proof',runtime_seconds=time.perf_counter()-nodetime)
    record['join']=dict(status='unpaid',reason='source/filter/evaluation gates not paid; endpoint h_i,0 and residual bounds not instantiated',formal_remaining_tolerance='min_rows max(0,theta-A*d0-B*d2-eval-filter-C*component_residual)/(c_theta*C); no positive value accepted')
    record['runtime_seconds']=time.perf_counter()-started
    record['numerical_budget']=dict(cap_seconds=1800,retained_run_seconds=record['runtime_seconds'],discarded_runs_and_misc_conservative_debit_seconds=240,aggregate_conservative_upper_seconds=record['runtime_seconds']+240,reason='three interrupted implementation runs plus small checks charged conservatively; only final run retained as evidence')
    record['hashes']={p.name:sha(p) for p in [Path(__file__),Path(__file__).with_name('weak_coefficients.py'),Path(__file__).with_name('exact_controls.py')]}
    record['controls']=json.loads(Path(__file__).with_name('EXACT_CONTROLS_20261024.json').read_text())
    packet=repo/'papers/investigations-5/01_heat_density_asymptotics/research-progress/handoffs/HDA-17-AN01.md'
    frozen=re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',packet.read_text())
    record['inputs']={p:dict(expected=h,actual=sha(repo/p),match=sha(repo/p)==h) for p,h in frozen}
    record['implementation_corrections']=[dict(issue='scalar cap audit required +3 rather than +2 baseline errors to ensure Pj>=sup|Fm,j|+bar_j for all meshes',effect='diagnostic rerun before retention',correction='moment(F192)+3*baseline caps'),dict(issue='initial implementation used -2*pi/t rather than -8*pi/t in Lambert-W argument',effect='wrong regulator at t96/128; initial run interrupted and discarded before any acceptance',correction='solve 4*pi*exp(4L)=2tL+9 using W_-1(-8*pi/t*exp(-18/t)) and record saddle residual')]
    record['git_head']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
    record['kernel_L']={f'{i},{j}':v for (i,j),v in kernels[64]['L'].items()}
    columns=list(record['observations'][0]['meshes'][0]['rows'][0])
    for optional in ('local_allowance','local_ratio'):
        if optional not in columns:columns.append(optional)
    record['row_columns']=columns
    for ob in record['observations']:
        for mm in ob['meshes']:mm['rows']=[[rr.get(c) for c in columns] for rr in mm['rows']]
    write_record_bundle(record,output)
    print('DONE',record['runtime_seconds'],output.stat().st_size,flush=True)
    print(json.dumps({k:{n:v.get(n) for n in ('t','x','y','cells','row',k)} for k,v in record['maxima'].items()}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.repo,args.output)
