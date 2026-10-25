#!/usr/bin/env python3
"""Six bounded exact-rational local controls for Note 42 GS8--GS12.

Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
reasoning effort ultra, inherited parent session configuration. These are
local algebra checks, not a theta, finite-source, or convolution certificate.
The existing exact_controls.py rational Taylor-jet helper is reused unchanged.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, importlib.util, json, platform, sys, time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--investigation-root',type=Path,default=Path(__file__).resolve().parent.parent)
args=parser.parse_args()
SOURCE=args.investigation_root/'numerics'/'exact_controls.py'
NOTE=args.investigation_root/'notes'/'42_GAP_LOCALIZED_SPATIAL_DEFECTS_20261024.md'
spec=importlib.util.spec_from_file_location('rational_jet_source',SOURCE)
m=importlib.util.module_from_spec(spec)
sys.dont_write_bytecode=True
spec.loader.exec_module(m)
J=m.J; lap=m.lap; box=m.box; cmul=m.cmul; conj=m.conj
cscale=m.cscale; cd=m.cd; add=m.add; bd=m.bar_d; re=m.creal; abs2=m.cabs2
def zd(a):
    return ((a[0].d(1)+a[1].d(2))/2,(a[1].d(1)-a[0].d(2))/2)
def sub(a,b): return add(a,cscale(b,-1))
def divc(a,d): return cscale(a,1/d)
def realmul(a,b): return re(cmul(a,b))

def run_case(name,point,variable_q=True):
    t0,x0,y0=map(Q,point)
    t=J({m.ZERO:t0,(1,0,0):1})
    x=J({m.ZERO:x0,(0,1,0):1})
    y=J({m.ZERO:y0,(0,0,1):1})
    z=(x,y)
    z2=cmul(z,z)
    if name=='B=0 heat polynomial': F=(z2[0]-2*t,z2[1])
    elif name=='conjugate(z)': F=conj(z)
    elif name=='x': F=(x,J(0))
    elif name=='local cutoff-polynomial join':
        G=(z2[0]-2*t,z2[1])
        D0=add((J(1),J(0)),add(cscale(z,Q(1,3)),cscale(z2,t/7)))
        lam=Q(1,2)+x/4-x**3/12
        F=add(G,cscale(D0,lam))
    elif name=='nonzero E_z holomorphic field': F=add(cmul(z2,z),cscale(z,t))
    elif name=='generic mixed field':
        F=((1+t)*x*x-y*y+x*y/3+t*t*x,2*x*y+t*y+x**3/5)
    else: raise ValueError(name)
    q=2+t*t+x*x if variable_q else J(2)
    r=q.log_derivatives(); rx=r.d(1); rt=r.d(0); rxx=r.d(1,2)
    a=zd(F); c=zd(a); B=bd(F); Bz=zd(B); Bb=bd(B); Bzz=zd(Bz)
    E=add(cd(F,0),c); Ez=zd(E)
    D=abs2(F)+q; S=D.log_derivatives(); w=q/D
    rho=q*abs2(a)/D**2  # pi*rho
    j=cscale(cmul(c,conj(a)),q/D**2)  # pi*j
    V0=divc(cmul(c,conj(F)),D); V1=cscale(V0,w)
    Z=divc(cmul(E,conj(F)),D)
    Creg=(2*w.d(1)*rx+w*rxx-w*(1-w)*rx*rx)/4  # pi*Creg
    TC=q*abs2(B)/D**2+2*re(sub(divc(cmul(Bz,conj(F)),D),divc(cmul(cmul(a,B),cmul(conj(F),conj(F))),D**2)))  # pi*T_C
    Ctot=Creg+TC
    Xi=8*realmul(a,conj(B))/D+4*realmul(F,conj(Bb))/D
    TJ=sub(cscale(divc(cmul(Bzz,conj(F)),D),-1),cscale(divc(cmul(cmul(c,B),cmul(conj(F),conj(F))),D**2),-1))
    TU=Xi/2+2*re(Z)
    b=rt+(rxx+rx*rx)/2; mathcalB=b*w
    stress=S.d(1)**2-S.d(2)**2
    signedsource=(1-2*w)*(rt*rho+rx*j[0])
    DE=2*q*realmul(Ez,conj(a))/D**2-4*rho*re(Z)
    DB=2*q*realmul(c,conj(Bz))/D**2-4*q*re(cmul(cmul(F,conj(B)),cmul(c,conj(a))))/D**3
    checks={}
    def check(label,diff):
        value=diff.value()
        checks[label]={'residual':str(value),'passed':value==0}
        if value!=0: raise AssertionError((name,label,str(value)))
    try:
        check('GS9_Laplacian',lap(S)-4*(rho+Ctot))
        jc=add(add(bd(V0),cscale(V1,rx/2)),TJ)
        check('GS9_current_real',j[0]-jc[0])
        check('GS9_current_imag',j[1]-jc[1])
        check('GS9_signed_gradient_stress',stress-(4*re(V0)-box(S)+(rxx+rx*rx)*w+Xi))
        check('GS9_time_potential',S.d(0)-(-2*re(V0)+rt*w+2*re(Z)))
        check('GS11_full_nonholomorphic_potential',S.d(0)-(-box(S)/2-stress/2+mathcalB+TU))
        # S derivatives and every Ctot derivative are taken directly, retaining
        # both curvature rows and full Xi/2 + 2 Re Z in TU.
        density_rhs=-box(rho)/2-lap(stress)/8+lap(mathcalB)/4-Ctot.d(0)-box(Ctot)/2+lap(TU)/4
        check('GS11_full_nonholomorphic_density',rho.d(0)-density_rhs)
        check('GS12_full_current_balance',rho.d(0)+j[0].d(1)+j[1].d(2)-signedsource-DE-DB)
        # Exact product differentiation underlying GS14; no differentiated
        # bound is used. The q_t contribution is retained.
        Ft=cd(F,0); at=cd(a,0); Bt=cd(B,0); Bzt=cd(Bz,0); Dt=D.d(0)
        TCt=q.d(0)*abs2(B)/D**2+2*q*realmul(Bt,conj(B))/D**2-2*q*abs2(B)*Dt/D**3
        positive=add(add(divc(cmul(Bzt,conj(F)),D),divc(cmul(Bz,conj(Ft)),D)),cscale(divc(cmul(Bz,conj(F)),D**2),-Dt))
        Fc2=cmul(conj(F),conj(F))
        negative=add(add(divc(cmul(cmul(at,B),Fc2),D**2),divc(cmul(cmul(a,Bt),Fc2),D**2)),cscale(divc(cmul(cmul(a,B),cmul(conj(F),conj(Ft))),D**2),2))
        negative=add(negative,cscale(divc(cmul(cmul(a,B),Fc2),D**3),-2*Dt))
        TCt=TCt+2*re(sub(positive,negative))
        check('GS14_exact_TC_time_product_derivative',TC.d(0)-TCt)
        if name=='local cutoff-polynomial join':
            D0z=zd(D0); D0zz=zd(D0z)
            P=add(G,D0); EP=add(cd(P,0),zd(zd(P)))
            compatibility={
                'B':sub(B,cscale(D0,lam.d(1)/2)),
                'B_z':sub(Bz,add(cscale(D0,lam.d(1,2)/4),cscale(D0z,lam.d(1)/2))),
                'B_bar_z':sub(Bb,cscale(D0,lam.d(1,2)/4)),
                'B_zz':sub(Bzz,add(add(cscale(D0,lam.d(1,3)/8),cscale(D0z,lam.d(1,2)/2)),cscale(D0zz,lam.d(1)/2))),
                'E':sub(E,add(add(cscale(EP,lam),cscale(D0z,lam.d(1))),cscale(D0,lam.d(1,2)/4))),
            }
            for label,difference in compatibility.items():
                check('GS5_join_'+label+'_real',difference[0])
                check('GS5_join_'+label+'_imag',difference[1])
        if name=='B=0 heat polynomial':
            check('B0_TC',TC); check('B0_Xi',Xi)
            check('B0_TJ_real',TJ[0]); check('B0_TJ_imag',TJ[1]); check('B0_DB',DB)
        if name=='conjugate(z)':
            check('conjugate_z_rho',rho); check('conjugate_z_j_real',j[0]); check('conjugate_z_j_imag',j[1])
            check('conjugate_z_TC_exact',TC-q/D**2)
        if name=='x': check('x_Xi_exact',Xi-2/D)
        status='passed'
    except AssertionError as error:
        status='failed'; failure=str(error)
    row={'field':name,'point':list(map(str,point)),'q':str(q.value()),'F':[str(F[0].value()),str(F[1].value())],'B':[str(B[0].value()),str(B[1].value())],'E':[str(E[0].value()),str(E[1].value())],'E_z':[str(Ez[0].value()),str(Ez[1].value())],'gradient_S':[str(S.d(1).value()),str(S.d(2).value())],'signed_gradient_stress':str(stress.value()),'status':status,'checks':checks}
    if status=='failed': row['failure']=failure
    return row

def main():
    began=time.perf_counter()
    definitions=[
        ('B=0 heat polynomial',(Q(1,3),Q(2,5),Q(1,7)),True),
        ('conjugate(z)',(Q(1,3),Q(2,5),Q(1,7)),False),
        ('x',(Q(1,3),Q(2,5),Q(1,7)),False),
        ('local cutoff-polynomial join',(Q(1,3),Q(2,5),Q(1,7)),True),
        ('nonzero E_z holomorphic field',(Q(1,3),Q(2,5),Q(1,7)),True),
        ('generic mixed field',(Q(1,3),Q(2,5),Q(1,7)),True),
    ]
    rows=[]
    for name,point,variable_q in definitions:
        rows.append(run_case(name,point,variable_q))
        if rows[-1]['status']=='failed': break
        if time.perf_counter()-began>=590: break
    # A normalized finite average verifies only universal mean-product algebra.
    # These six different fields are not samples of one convolved field.
    gradients=[list(map(Q,row['gradient_S'])) for row in rows]
    count=len(gradients); mx=sum(g[0] for g in gradients)/count; my=sum(g[1] for g in gradients)/count
    mean_stress=sum(Q(row['signed_gradient_stress']) for row in rows)/count
    covariance=mean_stress-(mx*mx-my*my)
    centered=sum((g[0]-mx)**2-(g[1]-my)**2 for g in gradients)/count
    # Rescale reversed gradients as an arbitrary second signed-stress array.
    g2=gradients[::-1]; hx=sum(g[0]/(count*(i+1)) for i,g in enumerate(g2)); hy=sum(g[1]/(count*(i+1)) for i,g in enumerate(g2))
    g2=[(g[0]/(i+1),g[1]/(i+1)) for i,g in enumerate(g2)]
    stress2=sum(g[0]**2-g[1]**2 for g in g2)/count
    covariance2=stress2-(hx*hx-hy*hy)
    diff_residual=(covariance-covariance2)-((mean_stress-stress2)-((mx-hx)*(mx+hx)-(my-hy)*(my+hy)))
    covariance_algebra={'scope':'Normalized finite average of arbitrary rational gradient pairs only; no convolution approximation or support theorem is claimed.','centered_vs_actual_definition_residual':str(covariance-centered),'comparison_mean_product_residual':str(diff_residual),'passed':covariance==centered and diff_residual==0}
    elapsed=time.perf_counter()-began
    result={'status':'passed' if len(rows)==6 and all(r['status']=='passed' for r in rows) and covariance_algebra['passed'] else 'stopped','prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra','case_count':len(rows),'checks_count':sum(len(r['checks']) for r in rows)+2,'total_execution_seconds':elapsed,'arithmetic':'Exact Python fractions.Fraction, Taylor jets total order 4','environment':{'python':sys.version,'platform':platform.platform()},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_source':str(SOURCE),'helper_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'note42_source':str(NOTE),'note42_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),'scope':'Local rational identities GS8--GS12 and exact derivative underlying GS14. No theta, actual filter, finite source, partition bound, or theorem certificate. Cutoff case is a local polynomial cutoff proxy, not a globally flat smooth cutoff. Actual covariance is defined by filtered signed stress minus mean products; the check does not substitute averaged component covariance or an equation-defined covariance.','covariance_mean_algebra':covariance_algebra,'cases':rows}
    output=Path(__file__).with_name('EXACT_GS8_GS12_20261024.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','case_count','checks_count','total_execution_seconds','script_sha256']},indent=2))
    return 0 if result['status']=='passed' else 1
if __name__=='__main__': raise SystemExit(main())
