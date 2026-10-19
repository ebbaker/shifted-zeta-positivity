#!/usr/bin/env python3
"""Exact m=2 completed-current algebra and fresh source-specific controls.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6.1-sol (Codex), reasoning effort ultra. Internal checks.
Finite polynomial checks supplement the analytic proof, not infinite-source
convergence or an independently established theta sign inequality.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


# Sparse exact multivariate polynomial arithmetic. No symbolic package needed.
NAMES = ('H','H1','H2','H3','t','x')
ZERO = (0,)*len(NAMES)


def c(v):
    return {} if not v else {ZERO:F(v)}


def v(name):
    key=list(ZERO);key[NAMES.index(name)]=1
    return {tuple(key):F(1)}


def add(*ps):
    out={}
    for p in ps:
        for k,a in p.items():out[k]=out.get(k,F(0))+a
    return {k:a for k,a in out.items() if a}


def scale(p,a):
    return {k:F(a)*b for k,b in p.items() if a*b}


def mul(*ps):
    out=c(1)
    for p in ps:
        step={}
        for k,a in out.items():
            for l,b in p.items():
                kl=tuple(x+y for x,y in zip(k,l))
                step[kl]=step.get(kl,F(0))+a*b
        out={k:a for k,a in step.items() if a}
    return out


def sq(p):return mul(p,p)


def partial(p,name):
    j=NAMES.index(name);out={}
    for k,a in p.items():
        if k[j]:
            l=list(k);l[j]-=1;out[tuple(l)]=a*k[j]
    return out


def dx(p):
    out=partial(p,'x')
    for old,new in zip(NAMES[:3],NAMES[1:4]):
        out=add(out,mul(partial(p,old),v(new)))
    return out


def at(p,values):
    return sum((a*__import__('functools').reduce(lambda z,kv:z*F(values.get(kv[0],0))**kv[1],zip(NAMES,k),F(1)) for k,a in p.items()),F(0))


def text_poly(p):
    return [{'powers':{n:k[j] for j,n in enumerate(NAMES) if k[j]},'coefficient':str(a)} for k,a in sorted(p.items())]


# Univariate differential-operator polynomials.
def ua(*ps):
    out={}
    for p in ps:
        for k,a in p.items():out[k]=out.get(k,F(0))+a
    return {k:a for k,a in out.items() if a}


def us(p,a):return {k:F(a)*b for k,b in p.items() if a*b}


def um(*ps):
    out={0:F(1)}
    for p in ps:
        out=ua(*[{k+l:a*b} for k,a in out.items() for l,b in p.items()])
    return out


def ud(p):return {k-1:k*a for k,a in p.items() if k}


def uat(p,z):return sum((a*z**k for k,a in p.items()),F(0))


def apply(op,action,p):
    out={};term=p
    for k in range(max(op,default=-1)+1):
        out=ua(out,us(term,op.get(k,0)));term=action(term)
    return out


def delta(p):return ua(um({1:4},ud(p)),um({0:1,1:-4},p))


def divide_d2_minus1(p):
    rem=p.copy();q={}
    while rem and max(rem)>=2:
        k=max(rem);a=rem[k];q=ua(q,{k-2:a});rem=ua(rem,{k:-a,k-2:a})
    return q,rem


def up(poly):return {str(k):str(a) for k,a in sorted(poly.items())}


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def finite_algebra():
    checks=[]
    def check(label,lhs,rhs):
        if lhs!=rhs:raise ArithmeticError(label)
        checks.append(label)
    d={1:F(1)};one={0:F(1)};source={1:F(-3),2:F(2)}
    p2=um({1:1,0:-9},{1:1,0:-7},{1:1,0:-1},{1:1,0:-5})
    completed=ua(us(p2,F(1,128)),{1:F(15,4),0:F(-15,4)})
    q2={2:F(1,16),1:F(-22,16),0:F(165,16)}
    check('second-insertion mode coefficient, from direct n^4 weighting',apply(us(p2,F(1,128)),delta,one),um({2:1},source))
    check('m2 exact primitive completion and physical reduction',completed,us(um({2:1,0:-1},q2),F(1,8)))
    check('m2 P(D) coefficients',p2,{4:F(1),3:F(-22),2:F(164),1:F(-458),0:F(315)})
    check('m2 coefficient forced by negative-cusp exponential',uat(completed,F(-1)),F(0))
    check('uncompleted actual psi half-zero-mode cusp coefficient',uat(us(p2,F(1,256)),F(-1)),F(15,4))
    # Finite consistency checks for the general exact division argument.
    divisions=[]
    for m in range(13):
        pm=ua(um({1:1,0:-4*m},{1:1,0:-4*m}),{0:-1})
        for j in range(m):pm=um(pm,{1:1,0:-1-4*j})
        alpha=F((-1)**m,8*4**m);correction=alpha*uat(pm,F(-1))/2
        pp=ua(us(pm,alpha),{1:correction,0:-correction})
        qq,rem=divide_d2_minus1(pp)
        check('finite completed primitive division m='+str(m),rem,{})
        check('finite completed source mode m='+str(m),apply(us(pm,alpha),delta,one),um({m:1},source))
        divisions.append({'m':m,'correction':str(correction),'physical_operator_coefficients':up(us(qq,8))})
    # Four product terms kept at independent differential coordinates.
    raw=us(p2,F(1,128));cor={1:F(15,4),0:F(-15,4)}
    tensor=lambda a,b:{(i,j):ai*bj for i,ai in a.items() for j,bj in b.items()}
    terms={'raw_raw':tensor(raw,raw),'raw_correction':tensor(raw,cor),
           'correction_raw':tensor(cor,raw),'correction_correction':tensor(cor,cor)}
    def tadd(*ps):
        out={}
        for p in ps:
            for k,a in p.items():out[k]=out.get(k,F(0))+a
        return {k:a for k,a in out.items() if a}
    full=tadd(*terms.values())
    check('all four independent-variable source-product terms',full,tensor(completed,completed))
    for name in ('raw_correction','correction_raw'):
        check('dropping '+name+' changes the product',tadd(*(p for n,p in terms.items() if n!=name))==full,False)
    # Independently integrate the second-order Green identity on monomials;
    # retain both finite endpoints rather than assuming cusp cancellation.
    integ=lambda p:sum((a/F(k+1) for k,a in p.items()),F(0))
    op={2:1,1:-22,0:165};adj={2:1,1:22,0:165}
    for i in range(5):
        for j in range(5):
            phi={i:F(1)};f={j:F(1)}
            current=ua(um(ud(phi),f),us(um(phi,ud(f)),-1),us(um(phi,f),-22))
            check('finite-interval Green identity '+str((i,j)),integ(um(apply(op,ud,phi),f)),
                  uat(current,F(1))-uat(current,F(0))+integ(um(phi,apply(adj,ud,f))))
    h,h1,h2,h3,t,x=map(v,NAMES)
    real=scale(add(mul(add(c(165),scale(t,2),scale(sq(x),-1)),h),
                   scale(mul(t,x,h1),4),scale(mul(sq(t),h2),-4)),F(1,16))
    imag=scale(add(mul(x,h),scale(mul(t,h1),-2)),F(22,16))
    # Build f'/f and f''/f independently using the product rule for
    # f=exp(t*u^2+i*x*u), then apply the exact formal adjoint.
    # Coefficients are pairs (real,imaginary) of rational polynomials.
    def pair_add(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
    def pair_scale(a,z):return (scale(a[0],z),scale(a[1],z))
    def pair_mul(a,b):return (add(mul(a[0],b[0]),scale(mul(a[1],b[1]),-1)),
                              add(mul(a[0],b[1]),mul(a[1],b[0])))
    def heat_derivative(coeff):
        out={}
        for k,a in coeff.items():
            if k:out[k-1]=pair_add(out.get(k-1,({},{})),pair_scale(a,k))
            out[k+1]=pair_add(out.get(k+1,({},{})),pair_mul(a,(scale(t,2),{})))
            out[k]=pair_add(out.get(k,({},{})),pair_mul(a,({},x)))
        return out
    f0={0:(c(1),{})};f1=heat_derivative(f0);f2=heat_derivative(f1)
    adj_coeff={}
    for coeff,factor in ((f2,1),(f1,22),(f0,165)):
        for k,a in coeff.items():adj_coeff[k]=pair_add(adj_coeff.get(k,({},{})),pair_scale(a,factor))
    moment={0:(h,{}),1:({},scale(h1,-1)),2:(scale(h2,-1),{})}
    image=({}, {})
    for k,a in adj_coeff.items():image=pair_add(image,pair_mul(a,moment[k]))
    check('physical W map from heat-weight adjoint recurrence',pair_scale(image,F(1,16)),(real,imag))
    # Green lower current is -phi1*f0+phi0*f1+22*phi0*f0.
    # At zero f0=1 and f1=i*x, so no hidden heat endpoint survives.
    lower=pair_add(pair_mul(f0[0],(add(scale(h1,-1),scale(h,22)),{})),
                   pair_mul(f1[0],(h,{})))
    check('half-line lower endpoint from heat-weight recurrence',lower,
          (add(scale(h,22),scale(h1,-1)),mul(x,h)))
    J=add(mul(real,dx(imag)),scale(mul(imag,dx(real)),-1))
    L0=add(sq(h1),scale(mul(h,h2),-1))
    L1=add(sq(h2),scale(mul(h1,h3),-1));dL0=dx(L0)
    first=add(mul(add(c(165),scale(t,2),sq(x)),sq(h)),
              scale(mul(t,x,h,h1),-4),scale(mul(sq(t),sq(h1)),4))
    higher=add(scale(mul(t,add(c(165),scale(t,4),sq(x)),L0),2),
               scale(mul(sq(t),x,dL0),-4),scale(mul(t,t,t,L1),8))
    rhs=scale(add(first,higher),F(11,128))
    check('complete m2 physical signed-current polynomial identity',J,rhs)
    # Independent primitive reconstruction shift kappa=I0+1/2.
    # Here H,H1,... are placeholders for I0,I1,... in N=128*J/11.
    bulk=scale(J,F(128,11))
    def shift_H(poly,amount):
        out={}
        for key,a in poly.items():
            for power in range(key[0]+1):
                new=list(key);new[0]=power
                out=add(out,{tuple(new):a*comb(key[0],power)*amount**(key[0]-power)})
        return out
    edge=add(shift_H(bulk,F(1,2)),scale(bulk,-1))
    expected_edge=add(mul(add(c(165),scale(t,2),sq(x)),add(h,c(F(1,4)))),
                      scale(mul(t,x,h1),-2),scale(mul(t,add(c(165),scale(t,4),sq(x)),h2),-1),
                      scale(mul(sq(t),x,h3),2))
    check('complete primitive lower edges and one-quarter corner',edge,expected_edge)
    Jc=add(J,scale(first,F(-11,128)))
    check('centered current retains derivative-Laguerre cross term',Jc,scale(higher,F(11,128)))
    check('dL0 coefficient identity',dL0,add(mul(h1,h2),scale(mul(h,h3),-1)))
    event={'H':0,'H1':0,'H2':2,'H3':0,'t':F(1,4),'x':0}
    W=(at(real,event),at(imag,event));jj=at(J,event);jc=at(Jc,event)
    check('polynomial event nonzero completed W',W,(F(-1,32),F(0)))
    check('polynomial event positive centered current',jc,F(11,256))
    check('polynomial event uncentered current agrees',jj,jc)
    check('polynomial event energy zero',event['H']**2+event['H1']**2,0)
    # H=x²-2(t-1/4) satisfies backward heat exactly. At t=1/4,x=0
    # W!=0 and Jc>0, so no finite E-payment holds there.
    field=add(sq(x),scale(t,-2),c(F(1,2)))
    check('heat-polynomial exact backward-heat equation',add(partial(field,'t'),partial(partial(field,'x'),'x')),{})
    return {'exact_checks':checks,'completion_operator':up(q2),'completion_divisions_finite_only':divisions,
            'current_expanded_coefficients':text_poly(J),'centered_current_expanded_coefficients':text_poly(Jc),
            'product_term_coefficient_counts':{n:len(p) for n,p in terms.items()},
            'half_line_complex_lower_boundary':'[-Phi_prime(0)+(22+i*x)*Phi(0)]/16; cannot be discarded',
            'physical_full_line_map':'use complete even Phi and paired cosine/even, sine/odd integrals; no half-line complex doubling',
            'polynomial_witness':{'field':'x^2-2*(t-1/4)','t':'1/4','x':'0','H':'0','H1':'0','H2':'2','W_real':'-1/32','W_imag':'0','J2':'11/256','J2_centered':'11/256','E':'0',
                 'source_status':'local heat-polynomial jet model; no integrable positive source asserted'}}


def replay_controls(repo,folder,model,effort):
    import flint
    from flint import arb,ctx
    ctx.prec=192
    source=repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py'
    folder.mkdir(parents=True,exist_ok=True);output=folder/'SOURCE_SPECIFIC_CONTROLS.json'
    subprocess.run([sys.executable,str(source),'--repo',str(repo),'--receipts',str(folder/'receipts'),
          '--output',str(output),'--execution-model',model,'--execution-effort',effort],check=True,
          capture_output=True,text=True,timeout=90,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    controls=json.loads(output.read_text());events=controls['screen']['event_rejections']
    if len(events)!=5:raise ArithmeticError('five fresh events required')
    inherited=[]
    for event in events:
        if not (event['strict_first_jet_rejected'] and event['strict_signed_margin_rejected'] and not event['theta_error_constants_used']):
            raise ArithmeticError('source-specific rejection invariant')
        inherited.append({'control':event['control'],'domain':event['event_domain'],
            'theta_error_constants_used':False,'old_first_jet_and_Laguerre_gates_reject':True,
            'complete_H2_enclosure':event['event_jet_enclosures'][2]})
    # Exact-event specialization of the actual integrable reflected source.
    # Fresh own-source certificate includes full quartic and normalization tails.
    receipt=folder/'receipts/REFLECTED_CONTROL_REPLAY.json';reflected=json.loads(receipt.read_text())
    h2=arb(reflected['Hxx_at_collision']);T=arb(1)/4
    if not h2>0:raise ArithmeticError('reflected exact-event curvature not positive')
    w=-T*T*h2/4;current=11*T*T*T*h2*h2/16
    if not (w<0 and current>0):raise ArithmeticError('reflected completed observation/current false-positive missing')
    own_reflected={'source_definition':reflected['source_definition'],'exact_event':{'t':'1/4','x':'pi/4','H':'0','H1':'0'},
       'event_relation_basis':'analytic Fourier factorization H=cF(x)(1+cos(4x)); F(pi/4)>0; fresh complete own-source certificate encloses curvature',
       'H2':h2.str(40,more=True),'W_real':w.str(40,more=True),'W_imag':'0',
       'J2_and_J2c':current.str(40,more=True),'E':'0',
       'W_norm_squared_over_H2_squared_exact':'1/4096','J2c_over_H2_squared_exact':'11/1024',
       'current_positive_at_collision':True,'finite_E_payment_at_collision':False,
       'source_specific_receipt_sha256':digest(receipt),'theta_error_constants_used':False,
       'missing_theta_premise':'exact normalized integer-square theta expansion; source is positive, even and normalized with complete primitive endpoints'}
    euler=controls['screen']['euler_witness']
    if not euler['strict_signed_margin_rejected']:raise ArithmeticError('Euler negative-Laguerre witness not rejected')
    # Complete own-source weighted-square event certificates are replayed above;
    # this uses their exact event existence, not arbitrary theta tail constants.
    weighted=[]
    square_receipts=[json.loads((folder/'receipts/THREE_SQUARE_REPLAY.json').read_text()),
                     json.loads((folder/'receipts/FOUR_SQUARE_REPLAY.json').read_text())]
    curvatures=[square_receipts[0]['combined_second_x_derivative_enclosure'],
                square_receipts[1]['collision_certificate']['scaled_transform_second_x_derivative']]
    for event,Tq,rr in zip(events[:2],(F(1,4),F(1,100)),curvatures):
        h2=arb(rr['display'] if isinstance(rr,dict) else rr)
        if h2.contains(0):raise ArithmeticError('weighted event needs nonzero source-specific curvature')
        ta=arb(Tq.numerator)/Tq.denominator
        jj=11*ta**3*h2*h2/16
        if not jj>0:raise ArithmeticError('weighted event positive m2 current failed')
        weighted.append({'control':event['control'],'exact_event_time':str(Tq),
            'event_location':event['event_domain']['x'],'H_at_event':'0','H1_at_event':'0',
            'source_specific_H2_enclosure':h2.str(40,more=True),
            'W_real_at_event':(-ta*ta*h2/4).str(40,more=True),'J2_and_J2c_at_event':jj.str(40,more=True),
            'E_at_event':'0','theta_error_constants_used':False,
            'map_scope':'completed physical jet of the even source extension; endpoint Phi_prime(0)=0 allows the second-order full-line distributional map without a delta boundary source; no identity with the raw analytic theta p-extension is claimed',
            'curvature_provenance':'fresh exact-event certificate on its spatial root bracket, before the intentionally coarse time-halo enlargement used by the old rejection screen',
            'missing_theta_premise':'complete analytic source reflection and unchanged canonical theta coefficients'})
    return {'status':'fresh own-source replay passed','interface_precision_bits':192,'python_flint':flint.__version__,
       'imported_source_certificate_precision_bits':{'three_square':160,'four_square':160,'reflected':160,'Euler':128},
       'precision_scope':'fresh interface arithmetic at 192 bits; source certificates retain the explicit precisions above; no 256-bit physical evaluation is asserted',
       'replay_script_sha256':digest(source),'replay_receipt_sha256':digest(output),
       'receipt_identities':controls['screen']['receipt_identities'],'inherited_event_screens':inherited,
       'reflected_integrable_event':own_reflected,'weighted_square_event_jet_specializations':weighted,
       'Euler_negative_Laguerre_witness':euler,
       'Euler_m2_current_sign_claimed':False,
       'analytic_premise_screen':controls['screen']['analytic_premise_screen']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--replay-dir',type=Path,required=True)
    parser.add_argument('--execution-model',required=True);parser.add_argument('--execution-effort',required=True)
    parser.add_argument('--exact-only',action='store_true')
    args=parser.parse_args();start=time.monotonic();repo=args.repo.resolve()
    algebra=finite_algebra()
    controls=None if args.exact_only else replay_controls(repo,args.replay_dir,args.execution_model,args.execution_effort)
    base=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
    paths=[base/'symmetries/06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md',
      base/'symmetries/06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md',
      Path('papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md'),
      Path('papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md')]
    record={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
       'actual_model':args.execution_model,'actual_effort':args.execution_effort,
       'llm_assistance':'substantial; exact finite algebra and same-model source-control replay',
       'python':platform.python_version(),'status':'pass','script_sha256':digest(__file__),
       'source_sha256':{str(p):digest(repo/p) for p in paths},
       'arithmetic':'standard-library exact rational multivariate polynomials; Arb outward intervals for inherited own-source controls',
       'algebra':algebra,'controls':controls,
       'scope':'m=2 q-weighted completed base-p source, its full-line physical observation and current; event-containing generic-source E-payment/strict-positive-current criterion excluded',
       'not_established':['a theta-specific current sign','a theta-specific obstruction','universal transverse-source impossibility','new physical collision-free coverage','an all-m current theorem from finite m checks'],
       'seconds':time.monotonic()-start}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','exact_checks':len(algebra['exact_checks']),'own_source_controls':controls is not None,'output':str(args.output),'seconds':record['seconds']}))


if __name__=='__main__':main()
