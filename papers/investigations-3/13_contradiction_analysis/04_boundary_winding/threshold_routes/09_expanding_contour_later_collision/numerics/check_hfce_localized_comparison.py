#!/usr/bin/env python3
"""Frozen HFCE04 fixed-weight pointwise screen; no new quadratures."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, platform, signal, sys, time
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode=True
from flint import arb,ctx
import flint
REL=Path('papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision')
T0,T1=F(119999,10**6),F(120001,10**6)
X0,X1=F(20023,20),F(5008,5)
TC,XC=F(21,200),F(1000)
def check(b,s):
    if not b:raise ArithmeticError(s)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def box(a,b):return arb(A((a+b)/2),A((b-a)/2))
def dyadic(v):
    check(v.is_exact() and v.is_finite(),'exact dyadic endpoint required');m,e=v.man_exp();return dict(mantissa=str(m),exponent=int(e))
def rec(v):return dict(display=v.str(50,more=True),lower_dyadic=dyadic(v.lower()),upper_dyadic=dyadic(v.upper()))
def square(v):
    lo=(v.abs_lower()**2).lower();hi=(v.abs_upper()**2).upper();return arb((lo+hi)/2,((hi-lo)/2).upper())
def poly(cs,x):
    r=cs[-1]
    for c in reversed(cs[:-1]):r=r*x+c
    return r
def bernstein1(cs,left,right):
    n=len(cs)-1;a=A(left);w=A(right-left)
    sh=[w**i*sum((cs[j]*math.comb(j,i)*a**(j-i) for j in range(i,n+1)),arb(0)) for i in range(n+1)]
    return [sum((sh[i]*math.comb(k,i)/math.comb(n,i) for i in range(k+1)),arb(0)) for k in range(n+1)]
def bernstein2(cs):
    nx,nt=len(cs),len(cs[0]);cols=[bernstein1([cs[l][k] for l in range(nx)],X0-XC,X1-XC) for k in range(nt)]
    grid=[bernstein1([cols[k][l] for k in range(nt)],T0-TC,T1-TC) for l in range(nx)]
    lo=min(v.lower() for row in grid for v in row);hi=max(v.upper() for row in grid for v in row)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def intersect(a,b):
    lo=max(a.lower(),b.lower());hi=min(a.upper(),b.upper());check(lo<=hi,'inconsistent independent enclosures')
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def qpoly(cs):
    p0,p1,p2=cs;out=[[arb(0) for k in range(25)] for l in range(49)]
    for l in range(25):
        for k in range(13):
            for p in range(25):
                for q in range(13):out[l+p][k+q]+=p1[l][k]*p1[p][q]-p0[l][k]*p2[p][q]
    return out
def tails(bits):
    ctx.prec=bits;pi=arb.pi();d=pi/8-4*arb(1000).log()/1000;c=(4*d).cos();sig=(4*d).sin()
    m,U,Tmax=12,arb(2),arb(1)/5;N=arb(1000)**(arb(9)/4)*d.exp();B=4*c*pi*m*m-9;P=4*sig*pi*m*m-arb(1002)-2*Tmax*d
    ratio=(arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
    check(d>0 and d<pi/8 and c>0 and sig>0 and B>0 and P>0 and ratio<1 and 8*c*pi*m*m>=Tmax,'mode admissibility failed')
    S=(2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-ratio)
    modes=[];sources=[];Ds=[];Cs=[]
    for j in range(3):
        Q=sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/B**k for k in range(j+1)),arb(0));modes.append((N*2*S*Q/P).upper())
        s=arb(0)
        for n in range(1,m):
            lam=pi*n*n;D=4*c*lam*(4*U).exp()-9-2*Tmax*U-arb(j)/(U+d);C=16*c*lam*(4*U).exp()-2*Tmax
            check(D>0 and C>0,'source tangent failed');Ds.append(D.lower());Cs.append(C.lower())
            s+=(2*lam*lam+3*lam)*(U+d)**j*(Tmax*U*U+9*U-c*lam*(4*U).exp()).exp()/D
        sources.append((N*s).upper())
    return modes,sources,dict(physical_orders=[0,1,2],B=rec(B),phase_gap=rec(P),geometric_ratio=rec(ratio),minimum_D=rec(min(Ds)),minimum_concavity=rec(min(Cs)))
def deriv(p):return [i*p[i] for i in range(1,len(p))] or [F(0)]
def mult(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
def sub(p,q):return [(p[i] if i<len(p) else F(0))-(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))]
def integrate_bump(p,L):
    b=[F(35,32)/L,F(0),-3*F(35,32)/L**3,F(0),3*F(35,32)/L**5,F(0),-F(35,32)/L**7]
    q=mult(p,b);return sum((2*c*L**(i+1)/F(i+1) for i,c in enumerate(q) if i%2==0),F(0))
def controls():
    rows=[]
    for k,expect in [(0,F(1)),(2,F(1,9)),(4,F(1,33)),(6,F(5,429))]:
        got=integrate_bump([F(0)]*k+[F(1)],F(1));check(got==expect,'bump moment mismatch');rows.append(dict(kind='bump_moment',order=k,value=str(got)))
    for a,b in [(F(2),F(0)),(F(-2),F(0)),(F(2),F(3)),(F(-2),F(3)),(F(2),F(-3))]:
        t,L=F(3,4),F(1,10);h=[-a*t,-b*t,a/2,b/6];q=sub(mult(deriv(h),deriv(h)),mult(h,deriv(deriv(h))))
        got=integrate_bump(q,L);expect=a*a*(t+L*L/18)+b*b*(t*t+L**4/396)
        check(got==expect and got>0,'cubic control failed');rows.append(dict(kind='quadratic_or_cubic',h2=str(a),h3=str(b),tau=str(t),L=str(L),exact_average=str(got),own_source_error=0))
    t,L=F(3,4),F(1);h=[12*t*(t-1),F(0),6-12*t,F(0),F(1)];q=sub(mult(deriv(h),deriv(h)),mult(h,deriv(deriv(h))))
    got=integrate_bump(q,L);check(got==F(-7409,858),'quartic negative average failed');check(q[0]==F(-27,2),'quartic point failed')
    rows.append(dict(kind='two_event_quartic',exact_average=str(got),pointwise_at_center=str(q[0]),own_source_error=0,initial_event_not_actual_threshold=True))
    h=[12*t*t,F(0),-12*t,F(0),F(1)];q=sub(mult(deriv(h),deriv(h)),mult(h,deriv(deriv(h))))
    got=integrate_bump(q,L);expect=F(20,429)*L**6-F(8,11)*t*L**4+16*t*t*L*L+288*t**3
    check(got==expect and got>0,'multiplicity four failed');rows.append(dict(kind='multiplicity_four',exact_average=str(got),ordinary_h2_quotient_refused=True,own_source_error=0))
    return rows

def actual_correlated_control(bits):
    """Run the very same qpoly/Bernstein path on own exact quartic data."""
    ctx.prec=bits
    c,d=F(11,8),F(147,200)
    hp=[[F(0) for k in range(13)] for l in range(25)]
    for l in range(5):hp[l][0]+=F(math.comb(4,l))*(-c)**(4-l)
    for l in range(3):
        yc=F(math.comb(2,l))*(-c)**(2-l)
        hp[l][0]+=(6-12*d)*yc
        hp[l][1]+=-12*yc
    hp[0][0]+=12*d*d-12*d;hp[0][1]+=24*d-12;hp[0][2]+=12
    def derivative(cs):
        return [[(l+1)*cs[l+1][k] if l+1<len(cs) else F(0)
                 for k in range(13)] for l in range(25)]
    hp1=derivative(hp);hp2=derivative(hp1)
    cs=[[[A(v) for v in row] for row in component] for component in (hp,hp1,hp2)]
    enclosure=bernstein2(qpoly(cs))
    check(enclosure.upper()<0,'same-consumer quartic negative Q not detected')
    # This independent exact evaluation checks the coordinate translation.
    def rat_eval(component,dx,dt):
        return sum((v*dx**l*dt**k for l,row in enumerate(component) for k,v in enumerate(row)),F(0))
    cp=[rat_eval(component,c,F(3,4)-d) for component in (hp,hp1,hp2)]
    check(cp==[F(-9,4),F(0),F(-6)] and cp[1]**2-cp[0]*cp[2]==F(-27,2),
          'same-consumer control translation or derivatives failed')
    return dict(bits=bits,field='H=y^4+(6-12*tau)y^2+12*tau*(tau-1)',
                mapping=dict(y='(x-1000)-11/8',tau='(t-21/200)+147/200'),
                own_y_box=[str(X0-XC-c),str(X1-XC-c)],
                own_tau_box=[str(T0-TC+d),str(T1-TC+d)],
                correlated_Q=rec(enclosure),strict_negative_upper_certified=True,
                center_H_Hx_Hxx=[str(v) for v in cp],center_Q='-27/2',
                own_source_error=0,theta_normalization_applied=False,
                exact_rational_components_differentiated=True,
                same_qpoly_and_bernstein2_as_theta=True,
                initial_event_not_actual_threshold=True)

def execute(module,setup,bits):
    start=time.monotonic();ctx.prec=bits;cache=setup['setup'];mom=[module.undyadic(r['midpoint_dyadic']) for r in cache['midpoint_jets']];rad=[module.undyadic(r['quadrature_radius_dyadic']) for r in cache['midpoint_jets']]
    check(len(mom)==51 and all(r>=0 for r in rad),'incomplete cache');M=module.undyadic(cache['common_moment_dyadic']);check(M>0,'majorant invalid')
    check(F(1,100)<=T0<=T1<=F(1,5) and F(999)<=XC<=X0<=X1<=1002,'full path outside domain')
    check(2+24+2*12==50 and 2+24+2*13==52,'derivative order mismatch')
    modes,sources,admiss=tails(bits);R=A(X1-XC);Delta=A(max(abs(T0-TC),abs(T1-TC)));fact=[math.factorial(i) for i in range(53)]
    rem=(M*(R**25/fact[25]+R.exp()*Delta**13/fact[13])).upper();dt=box(T0,T1)-A(TC);dx=box(X0,X1)-A(XC)
    images=[];values=[];errors=[];coeffs=[];payments=[];component_seconds=[]
    for j in range(3):
        js=time.monotonic();cs=[[(-1)**k*mom[j+l+2*k]/(fact[l]*fact[k]) for k in range(13)] for l in range(25)]
        horner=poly([poly(row,dt) for row in cs],dx);bern=bernstein2(cs);image=intersect(horner,bern)
        quad=sum((R**l*Delta**k*rad[j+l+2*k]/(fact[l]*fact[k]) for l in range(25) for k in range(13)),arb(0)).upper();error=(rem+quad+modes[j]+sources[j]).upper()
        check(error<arb('1e-6'),'added component error cap failed');coeffs.append(cs);images.append(image);errors.append(error);values.append(image+arb(0,error));component_seconds.append(time.monotonic()-js)
        payments.append(dict(j=j,horner_polynomial=rec(horner),bernstein_polynomial=rec(bern),used_polynomial=rec(image),quadrature=rec(quad),taylor=rec(rem),mode=rec(modes[j]),source=rec(sources[j]),total=rec(error)))
    coord=square(values[1])-values[0]*values[2];corrstart=time.monotonic();qp=bernstein2(qpoly(coeffs));B=[p.abs_upper() for p in images];e=errors
    prod=(2*B[1]*e[1]+e[1]**2+B[0]*e[2]+B[2]*e[0]+e[0]*e[2]).upper();corr=qp+arb(0,prod)
    lower=max(coord.lower(),corr.lower());upper=min(coord.upper(),corr.upper());check(lower<=upper,'inconsistent Q ranges')
    competitor=(2*(2*B[1]*e[1]+e[1]**2)+42/(5*arb(5).sqrt()*A(F(1,10))**2)*(2*B[0]*e[0]+e[0]**2)).upper()
    return dict(bits=bits,source_acquisition_bits=setup['actual_precision_bits'],full_box=dict(time=[str(T0),str(T1)],space=[str(X0),str(X1)]),R=rec(R),Delta=rec(Delta),maximum_midpoint_order=50,maximum_remainder_order=52,source_majorant=rec(M),tail_admissibility=admiss,component_values_over_Gstar=[rec(v) for v in values],component_payments=payments,coordinate_Q_over_Gstar_squared=rec(coord),correlated_Q_polynomial=rec(qp),complete_Q_product_error=rec(prod),correlated_physical_Q=rec(corr),strongest_lower_Q=rec(lower),strongest_upper_Q=rec(upper),fixed_weight_A_lower_by_mass_one=rec(lower),H_Hx_only_competitor_product_allowance_not_executed=rec(competitor),component_consumer_seconds=component_seconds,Hxx_component_seconds=component_seconds[2],correlated_consumer_seconds=time.monotonic()-corrstart,total_seconds=time.monotonic()-start,new_source_quadratures=0,new_majorant_quadratures=0,weighted_integration_performed=False,status='uniform_positive_Q_selected_negative_average_impossible' if lower>0 else 'inconclusive_fixed_box_no_adaptation')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--contract',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();check(args.contract.is_file(),'preexisting frozen contract required')
    start=time.monotonic()
    def expired(sig,frame):raise TimeoutError('predeclared300s whole-run budget')
    signal.signal(signal.SIGALRM,expired);signal.setitimer(signal.ITIMER_REAL,300)
    extpath=args.repo/REL/'numerics/check_bounded_first_jet_extension.py';spec=importlib.util.spec_from_file_location('localized_pinned_ext',extpath);ext=importlib.util.module_from_spec(spec);spec.loader.exec_module(ext);module,setup,pins=ext.pin_sources(args.repo)
    report=dict(date='2026-10-20',prepared_for='Edward Baker',llm_assistance='substantial; same-model subagent; no independent specialist review',model='gpt-6-astra',reasoning_effort='ultra',model_metadata_provenance='verified by root agent from parent turn metadata',python_executable=sys.executable,python_version=platform.python_version(),python_flint=flint.__version__,wrapper_sha256=digest(__file__),contract_sha256=digest(args.contract),source_pins=pins,extension_wrapper_sha256=digest(extpath),normalization='fixed Gstar=1000^(7/4)exp(-125*pi)',contract_file=str(args.contract),initial_box_already_excluded=True,scope='One fixed localized cap comparator; no new initial event coverage, later-event assertion or universal localized-functional obstruction',scan=False,adaptive=False,new_quadratures=0,own_controls=controls())
    report['replays']=[execute(module,setup,b) for b in (192,256)];report['same_consumer_correlated_controls']=[actual_correlated_control(b) for b in (192,256)];report['elapsed_seconds']=time.monotonic()-start;report['status']='bounded_comparison_complete';signal.setitimer(signal.ITIMER_REAL,0);args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status=report['status'],elapsed_seconds=report['elapsed_seconds'],replays=[{k:r[k] for k in ['bits','strongest_lower_Q','complete_Q_product_error','Hxx_component_seconds','total_seconds','status']} for r in report['replays']]),indent=2))
if __name__=='__main__':main()
