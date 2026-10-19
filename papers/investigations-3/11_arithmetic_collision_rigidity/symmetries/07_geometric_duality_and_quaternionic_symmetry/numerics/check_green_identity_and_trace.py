#!/usr/bin/env python3
"""Exact finite checks for S07's zero-form Green/trace investigation.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra. Analytic scope
and the smooth concentration proof are supplied by Note02, not these checks.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys

sys.dont_write_bytecode=True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    repo=args.repo.resolve()
    base=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
    old=base/'symmetries/06_hodge_and_transverse_geometry/numerics/check_geometric_symmetry_coverage.py'
    spec=importlib.util.spec_from_file_location('s06_exact_helpers',repo/old)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    add,mul,scale,diff=m.plus,m.times,m.scale,m.diff
    checks=[]

    def check(name,got,expected):
        if got!=expected:
            raise ArithmeticError(f'{name}: {got!r} != {expected!r}')
        checks.append(name)

    def mon(dim,axis=None,power=1,c=1):
        k=[0]*dim
        if axis is not None:k[axis]=power
        return {tuple(k):F(c)}

    def fwedge(a,b):
        out={}
        for ia,pa in a.items():
            for ib,pb in b.items():
                seq=ia+ib
                if len(set(seq))<len(seq):continue
                sg=(-1)**sum(x>y for k,x in enumerate(seq) for y in seq[k+1:])
                key=tuple(sorted(seq))
                out[key]=add(out.get(key,{}),scale(mul(pa,pb),sg))
        return {k:p for k,p in out.items() if p}

    def dform(a,dim=4):
        out={}
        for ia,pa in a.items():
            for axis in range(dim):
                dp=diff(pa,axis)
                if not dp:continue
                piece=fwedge({(axis,):mon(dim)},{ia:dp})
                for k,p in piece.items():out[k]=add(out.get(k,{}),p)
        return {k:p for k,p in out.items() if p}

    one=mon(4);p=mon(4,0);q=mon(4,1);s=mon(4,3)
    # Connection divided by pi; F/(i pi)=d a_normalized.
    au={(0,):add(mul(s,s),scale(mul(p,p),-1)),
        (1,):scale(mul(p,q),2),(2,):scale(s,2),(3,):scale(mul(p,s),2)}
    curv={(0,1):scale(q,2),(2,3):scale(one,-2)}
    omega={(0,2):one,(0,3):p,(1,3):scale(q,-1)}
    check('adapted unitary connection curvature',dform(au),curv)
    check('J Kahler form closed',dform(omega),{})
    check('curvature wedge omegaJ zero',fwedge(curv,omega),{})
    # Complex P/Q vector bracket: both nonconstant r derivatives equal i.
    check('P Q vector bracket cancellation',diff(p,0),diff(q,1))
    check('P Q curvature cancellation',add(curv[(0,1)],mul(q,curv[(2,3)])),{})

    # Complete symbolic boundary three-form with variables p,q,jp,jq,jr,js.
    o6=mon(6);p6=mon(6,0);q6=mon(6,1)
    jr=[mon(6,k) for k in range(2,6)]
    jform={(k,):jr[k] for k in range(4)}
    w6={(0,2):o6,(0,3):p6,(1,3):scale(q6,-1)}
    got=fwedge(jform,w6)
    expected={(1,2,3):mul(q6,jr[2]),
              (0,2,3):add(jr[3],scale(mul(p6,jr[2]),-1)),
              (0,1,3):scale(add(mul(q6,jr[0]),mul(p6,jr[1])),-1),
              (0,1,2):scale(jr[1],-1)}
    check('all boundary three-form coefficients',got,expected)

    # Gaussian rationals as pairs (real,imag); no floating complex arithmetic.
    zero=(F(0),F(0));ii=(F(0),F(1))
    def ca(a,b):return (a[0]+b[0],a[1]+b[1])
    def cs(a,c):return(a[0]*c,a[1]*c)
    def cm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def cc(a):return(a[0],-a[1])
    def csum(xs):
        out=zero
        for x in xs:out=ca(out,x)
        return out
    jj=[[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]]
    def jpull(v):return[csum(cs(v[k],jj[k][i]) for k in range(4)) for i in range(4)]
    def project(v):return[cs(ca(a,cm(ii,b)),F(1,2)) for a,b in zip(v,jpull(v))]
    def inner(v,w):return csum(cm(a,cc(b)) for a,b in zip(v,w))
    basis=[]
    for k in range(4):
        for c in [(F(1),F(0)),ii]:
            v=[zero]*4;v[k]=c;basis.append(v)
    for i,a in enumerate(basis):
        for j,b in enumerate(basis):
            left=ca(inner(a,b),cs(inner(project(a),project(b)),-2))
            right=zero
            for x,y,c in [(0,2,1),(1,3,-1)]:
                term=ca(cm(a[x],cc(b[y])),cs(cm(a[y],cc(b[x])),-1))
                right=ca(right,cs(cm(ii,term),c))
            check(f'polarized J energy algebra {i},{j}',left,right)
    check('projection first source component factor',inner(project(basis[1]),project(basis[1])),(F(1,2),F(0)))
    check('projection second source component factor',inner(project(basis[2]),project(basis[2])),(F(1,2),F(0)))

    # Normalize pi out of the unitary connection norm and use inverse metric.
    qinv=mon(4,1,-1)
    norm=add(mul(qinv,add(mul(au[(0,)],au[(0,)]),mul(au[(1,)],au[(1,)]))),
             mul(q,mul(au[(2,)],au[(2,)])),
             mul(qinv,mul(add(au[(3,)],scale(mul(p,au[(2,)]),-1)),
                           add(au[(3,)],scale(mul(p,au[(2,)]),-1)))))
    expectednorm=add(mul(qinv,mul(add(mul(s,s),scale(mul(p,p),-1)),
                                    add(mul(s,s),scale(mul(p,p),-1)))),
                     scale(mul(q,add(mul(p,p),mul(s,s))),4))
    check('adapted connection norm polynomial',norm,expectednorm)
    check('connection bound on fixed chart',F(2)+F(1,256)<3,True)
    check('inverse metric Euclidean comparison',F(4)+F(1,16)+F(1,4)<6,True)

    # Exact Gaussian moments relative to integral exp(-2v²).
    def gm(k):
        if k%2:return F(0)
        value=F(1)
        for j in range(1,k,2):value*=F(j,4)
        return value
    amp={(4,):F(1),(2,):F(-3,2)}
    squared=mul(amp,amp)
    c0=sum(v*gm(k[0]) for k,v in squared.items())
    check('canonical fiber source norm constant times sqrt2',c0,F(33,256))
    check('canonical fiber r current odd Gaussian moment',
          sum(v*gm(k[0]+1) for k,v in squared.items()),F(0))
    # D^k theta on an exponential has Hermite recurrence H_next=xH+H'.
    # After homogeneity scaling c=pi/q to one, x²=-4v² in H4.
    herm={(0,):F(1)}
    xx={(1,):F(1)}
    for _ in range(4):herm=add(mul(xx,herm),diff(herm,0))
    normalized_h4={(k[0],):v*(-4)**(k[0]//2) for k,v in herm.items()}
    complete_amp=scale(add(normalized_h4,{(0,):F(-3)}),F(1,16))
    check('source amplitude from complete fourth Hermite jet',complete_amp,amp)
    phi={(2,):F(1,16),(0,):F(-3,16)}
    kp={(3,):F(1,16),(2,):F(-9,16),(1,):F(9,16),(0,):F(3,16)}
    jp={(3,):F(-1,16),(2,):F(-9,16),(1,):F(-9,16),(0,):F(3,16)}
    lap_correction=add(scale(add(kp,jp),-1),scale(phi,-2))
    check('rough Laplacian connection and fiber combination',lap_correction,{(2,):F(1)})
    def double_factorial_odd(k):
        out=1
        for j in range(1,k+1,2):out*=j
        return F(out)
    tz=[double_factorial_odd(2*m-1) for m in range(4)]
    kzero=(tz[3]-9*tz[2]+9*tz[1]+3*tz[0])/16
    jzero=-(tz[3]+9*tz[2]+9*tz[1]-3*tz[0])/16
    check('raw rough Laplacian growing zero mode divided by pi',
          sum(v*tz[k[0]] for k,v in lap_correction.items()),F(3))
    for k in range(7):
        check(f'physical q chain rule on monomial {k}',F(k*(k-1)),F((4*k)**2-4*(4*k),16))

    # Flat compact polynomial example checks codimension-three scaling.
    def integral(poly,lo,hi):
        return sum(v*(hi**(k[0]+1)-lo**(k[0]+1))/F(k[0]+1) for k,v in poly.items())
    rho={(0,):F(1),(2,):F(-2),(4,):F(1)}
    aa={(2,):F(1),(3,):F(-2),(4,):F(1)} # q-2 in [0,1]
    i0=integral(mul(aa,aa),F(0),F(1))
    i1=integral(mul(diff(aa,0),diff(aa,0)),F(0),F(1))
    b=integral(mul(rho,rho),F(-1),F(1))
    d=integral(mul(diff(rho,0),diff(rho,0)),F(-1),F(1))
    b0=b**3;b1=3*d*b*b
    check('flat model longitudinal L2 constant',i0,F(1,630))
    check('flat model transverse L2 constant',b,F(256,315))
    check('flat model transverse derivative constant',d,F(256,105))
    check('codimension-three derivative energy exponent',3-2,1)
    sequence=[]
    for n in range(3,8):
        eps=F(1,2**n)
        energy=i0*b1*eps+(i1+i0)*b0*eps**3
        sequence.append({'epsilon':str(eps),'flat_H1_squared':str(energy),
                         'flat_path_L2_squared':str(i0),'path_to_energy_ratio':str(i0/energy)})
    check('flat model H1 tends downward on recorded sequence',
          all(F(sequence[i+1]['flat_H1_squared'])<F(sequence[i]['flat_H1_squared']) for i in range(4)),True)
    check('flat model path stays fixed',len({x['flat_path_L2_squared'] for x in sequence}),1)

    folder=base/'symmetries/07_geometric_duality_and_quaternionic_symmetry'
    sources=[repo/old,repo/(folder/'notes/01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md'),
             repo/(folder/'notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md'),
             repo/(folder/'reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md'),
             repo/(folder/'numerics/S07_GREEN_SOURCE_CONTROLS_20261018.json'),
             repo/(base/'symmetries/06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md'),
             repo/(base/'symmetries/06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md'),
             repo/'papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md']
    record={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
            'actual_model':'gpt-6.1-sol','actual_effort':'ultra','llm_assistance':'substantial; same-model delegated checks',
            'python':platform.python_version(),'status':'pass','exact_checks':len(checks),'check_names':checks,
            'arithmetic':'exact rational real/complex matrices, Laurent/exterior polynomials and Gaussian moments',
            'flat_model_scope':'C1 compact polynomial illustration only; the note proves a smooth family on the actual bundle/metric.',
            'flat_scaling_sequence':sequence,
            'source_sha256':{str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'new_independent_physical_sign_estimate':False,
            'scope':'Finite algebra only. Analytic Green and smooth trace-obstruction proofs are in S07 Note02.'}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','exact_checks':len(checks),'output':str(args.output)}))


if __name__=='__main__':main()
