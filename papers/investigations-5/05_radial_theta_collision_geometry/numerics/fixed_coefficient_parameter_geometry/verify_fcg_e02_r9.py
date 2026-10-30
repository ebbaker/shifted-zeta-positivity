#!/usr/bin/env python3
"""R9 assessment: independent rational reconstruction of fixed saved inputs.
Prepared for Edward Baker with LLM assistance, gpt-6-astra/max, 2026-10-30.
No source evaluation, parameter scan, quadrature or root finding.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import argparse, hashlib, json, re, time

ZERO=(F(0),F(0))
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def times(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)
def scaled(a,q): return times(a,(F(q),F(q)))
def absolute(a): return max(abs(a[0]),abs(a[1]))
def decoded(z):
    m=F(int(z['mid_binary'][0]))*F(2)**int(z['mid_binary'][1])
    r=F(int(z['rad_binary'][0]))*F(2)**int(z['rad_binary'][1])
    assert r>=0
    return m-r,m+r
def displayed(z):
    z=z.strip('[] ')
    if '+/-' not in z: return F(z),F(z)
    m,r=(F(x.strip()) for x in z.split('+/-'))
    assert r>=0
    return m-r,m+r
def multiply(p,q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            key=i+k,j+l
            out[key]=plus(out.get(key,ZERO),times(a,b))
    return out
def tensor_bounds(p,s,xwidth=F(2)):
    """Direct monomial-to-Bernstein weights; signed weights combined first.
    This differs from the original intermediate affine-interval expansion.
    """
    d=max(i for i,j in p);e=max(j for i,j in p)
    wt={(i,m):s**m*sum((F(comb(m,k)*comb(i,k)*(-1)**(m-k)*2**k,comb(d,k)) for k in range(min(i,m)+1)),F(0)) for i in range(d+1) for m in range(d+1)}
    wx={(j,l):F(comb(j,l),comb(e,l))*xwidth**l for j in range(e+1) for l in range(j+1)}
    first={}
    for i in range(d+1):
        for l in range(e+1):
            v=ZERO
            for m in range(d+1):
                if (m,l) in p: v=plus(v,scaled(p[m,l],wt[i,m]))
            first[i,l]=v
    out=[]
    for i in range(d+1):
        for j in range(e+1):
            v=ZERO
            for l in range(j+1): v=plus(v,scaled(first[i,l],wx[j,l]))
            out.append(v)
    return (min(v[0] for v in out),max(v[1] for v in out)),(d,e)
def bound_record(v): return {'lower':str(v[0]),'upper':str(v[1])}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--replay',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args(); start=time.monotonic(); repo=args.repo.resolve()
    base=repo/'papers/investigations-5/05_radial_theta_collision_geometry'
    packet=base/'research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R9_SIGNED_TRANSPORT_ASSESSMENT_20261030.md'
    hashes=re.findall(r'\| `([^`]+)` \| `([a-f0-9]{64})` \|',packet.read_text())
    for p,h in hashes: assert hashlib.sha256((repo/p).read_bytes()).hexdigest()==h,p
    checks=[]
    def check(name,c):
        assert c,name
        checks.append(name)
    raw=base/'numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json'
    data=json.loads(raw.read_text()); stage=next(x for x in data['stages'] if x['bits']==384)
    rows={x['j']:x for x in stage['integrals'] if x['kind']=='jet'}
    check('complete signed jet indices 0 through 17',set(rows)==set(range(18)))
    h={k:decoded(v['complete']) for k,v in rows.items()}
    ek={k:displayed(v['source_upper'])[1]+displayed(v['mode_upper'])[1] for k,v in rows.items()}
    def moment(j,y): return next(x for x in stage['integrals'] if x['kind']=='moment' and x['j']==j and x['T']=='17/64' and x['Y']==y)
    m4row=moment(4,'1/64');m4=decoded(m4row['complete'])[1]
    exterior=displayed(m4row['source_upper'])[1]+displayed(m4row['mode_upper'])[1]
    x1=decoded(moment(1,'4')['complete'])[1]
    s=F(1,128);rho=F(1,16384)
    check('all local times below complete carrier moment time',F(1,4)+s+rho<F(17,64))
    a=[s**m/F(factorial(m)) for m in range(33)]
    b=[F(2)**l/F(factorial(l)) for l in range(65)]
    at=s**33/F(factorial(33))/(1-s/34)
    bt=F(2)**65/F(factorial(65))/(1-F(2,66))
    p={};err={};ranges={};degrees={};symbolic={}
    for j in range(4):
        symbolic[j]={(m,l):(j+2*m+l,F((-1)**m,factorial(m)*factorial(l))) for m in range(9) for l in range(18) if 2*m+l<=17-j}
        p[j]={k:scaled(h[index],factor) for k,(index,factor) in symbolic[j].items()}
        st=sum((a[m]*b[l] for m in range(33) for l in range(65) if 2*m+l>17-j),F(0))+(sum(a)+at)*(sum(b)+bt)-sum(a)*sum(b)
        # The complementary rectangle formula here is algebraically different.
        err[j]=m4*st+exterior+sum((s**m*F(2)**l/F(factorial(m)*factorial(l))*ek[j+2*m+l] for m,l in p[j]),F(0))
        ranges[j],degrees[j]=tensor_bounds(p[j],s)
    def diff(poly,var):
        out={}
        for (m,l),(j,c) in poly.items():
            k=(m,l)[var]
            if k: out[m-(var==0),l-(var==1)]=(j,c*k)
        return out
    check('symbolic dx P0 equals P1',diff(symbolic[0],1)==symbolic[1])
    check('symbolic dx P1 equals P2',diff(symbolic[1],1)==symbolic[2])
    check('symbolic dt P0 equals minus P2',diff(symbolic[0],0)=={k:(j,-c) for k,(j,c) in symbolic[2].items()})
    dp=multiply(p[1],p[1])
    for key,v in multiply(p[0],p[2]).items(): dp[key]=plus(dp.get(key,ZERO),scaled(v,-2))
    dr,dd=tensor_bounds(dp,s)
    check('fixed discriminant tensor degree',(16,32)==dd)
    ce={j:absolute(ranges[j]) for j in range(4)}
    de=2*ce[1]*err[1]+err[1]**2+2*(ce[0]*err[2]+ce[2]*err[0]+err[0]*err[2])
    dlow=dr[0]-de
    physical={j:(ranges[j][0]-err[j],ranges[j][1]+err[j]) for j in range(4)}
    ends=[]
    for endpoint in [F(0),F(2)]:
        poly={}
        for (m,l),v in p[0].items(): poly[m,0]=plus(poly.get((m,0),ZERO),scaled(v,endpoint**l))
        er,_=tensor_bounds(poly,s)
        ends.append((er[0]-err[0],er[1]+err[0]))
    eta=absolute(physical[1]);B=absolute(physical[2]);h3=absolute(physical[3]);delta=4-rho
    ab=2/delta+6/delta**2+6/delta**3
    ah=1/delta**2+6/delta**3+12/delta**4
    finite=rho*eta*h3;tc=2*rho*B**2;tail=x1*rho**2*(B*ab+eta*ah)
    margin=dlow-finite-tc-tail
    cn=margin/(1+absolute(physical[0])**2+eta**2+B**2)
    scalar=-physical[1][1]-rho*(B+h3)-x1*rho**2*ah
    check('independent physical discriminant bound',dlow>F('7.4e-20'))
    check('independent derivative sign',physical[1][1]<F('-2.4e-10'))
    check('independent left endpoint sign',ends[0][0]>F('6.4e-10'))
    check('independent right endpoint sign',ends[1][1]<F('-6.2e-11'))
    check('independent C04 degree-one margin',margin>F('6.6e-20'))
    check('independent exact c lower bound',cn>F('6.6e-20'))
    check('independent local scalar derivative floor',scalar>F('2.3e-10'))
    check('reporting correction necessary and sufficient',F('1e-12')<err[3]<F('1.1e-12'))
    saved_path=base/'numerics/fixed_coefficient_parameter_geometry/fcg_b03_r9_signed_transport_20261030.json'
    saved=json.loads(saved_path.read_text()); replay=json.loads(args.replay.read_text())
    check('original checker replay identical except runtime',all(saved.get(k)==replay.get(k) for k in saved.keys()|replay.keys() if k!='elapsed_seconds'))
    for j in range(4):
        check(f'complete independent transport error j{j}',err[j]==F(saved['source_errors'][str(j)]['total_upper']))
        old=saved['polynomial_ranges'][str(j)]
        check(f'independent range contained in original j{j}',ranges[j][0]>=F(old['lower']) and ranges[j][1]<=F(old['upper']))
    check('independent discriminant lower bound at least original',dlow>=F(saved['signed_discriminant_lower']))
    check('assessment runtime under 60 seconds',time.monotonic()-start<60)
    result={
        'task':'FCG-E02 R9 fixed assessment', 'date':'2026-10-30', 'prepared_for':'Edward Baker',
        'llm_assistance':'Substantial LLM assistance', 'model':'gpt-6-astra','effort':'max',
        'thread_id':'01a18e52-fa91-7b61-b31b-b311eee675f8','history_number':50,
        'provenance':'Different-model internal assessment of Sol-authored R9; separately written exact affine/Bernstein reconstruction, common source data and inherited analytic premises; no specialist, formal or independent source validation.',
        'inputs':[{'path':p,'sha256':h} for p,h in hashes]+[{'path':str(packet.relative_to(repo)),'sha256':hashlib.sha256(packet.read_bytes()).hexdigest()}],
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'replay_sha256':hashlib.sha256(args.replay.read_bytes()).hexdigest(),
        'replay_runtime_seconds':replay['elapsed_seconds'],
        'checks':checks,'transport_errors':{str(j):str(v) for j,v in err.items()},
        'independent_polynomial_ranges':{str(j):bound_record(v) for j,v in ranges.items()},
        'independent_discriminant_polynomial':bound_record(dr),
        'independent_discriminant_error':str(de),'independent_D_lower':str(dlow),
        'independent_physical_ranges':{str(j):bound_record(v) for j,v in physical.items()},
        'independent_endpoint_ranges':[bound_record(v) for v in ends],
        'consumer':{k:str(v) for k,v in {'time':tc,'finite':finite,'tail':tail,'d_lower':margin,'c_lower':cn,'scalar_derivative_floor':scalar}.items()},
        'new_source_evaluations':0,'new_quadrature_evaluations':0,'parameter_sweep':False,
        'dispositions':{str(j):'accept without mathematical correction' for j in range(1,8)},
        'status':'all_seven_obligations_accepted', 'runtime_seconds':time.monotonic()-start,
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':len(checks),'seconds':result['runtime_seconds'],'D_lower':float(dlow),'d_lower':float(margin),'scalar_floor':float(scalar)}))

if __name__=='__main__':main()
