#!/usr/bin/env python3
"""Exact algebra for the S06 geometric-symmetry coverage review.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra. These checks
verify finite algebra, not global analytic or cohomological theorems.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform


def plus(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def times(p, r):
    return plus(*[{tuple(a+b for a, b in zip(k, l)): v*w}
                  for k, v in p.items() for l, w in r.items()])


def diff(p, axis):
    out = {}
    for k, v in p.items():
        if k[axis]:
            l = list(k)
            l[axis] -= 1
            out[tuple(l)] = k[axis]*v
    return out


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def apply(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def wedge(p, r):
    out = {}
    for k, v in p.items():
        for l, w in r.items():
            seq = k+l
            if len(set(seq)) != len(seq):
                continue
            sign = (-1)**sum(a > b for n, a in enumerate(seq) for b in seq[n+1:])
            out = plus(out, {tuple(sorted(seq)): sign*v*w})
    return out


def tensor_pullback(form, a):
    out = {}
    for indices, value in form.items():
        term = {(): value}
        for k in indices:
            term = wedge(term, {(j,): a[k][j] for j in range(4) if a[k][j]})
        out = plus(out, term)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, got, expected):
        if got != expected:
            raise ArithmeticError(f'{name}: {got!r} != {expected!r}')
        checks.append(name)

    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    minus_identity = [[-x for x in row] for row in identity]
    ii = [[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]
    jj = [[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]]
    kk = matmul(ii, jj)
    wi = {(0,1):1,(2,3):1}
    wj = {(0,2):1,(1,3):-1}
    wk = {(0,3):1,(1,2):1}
    anti = {(0,1):1,(2,3):-1}
    for name, a in [('I',ii),('J',jj),('K',kk)]:
        check(name+' square',matmul(a,a),minus_identity)
        check(name+' orthogonal',matmul(transpose(a),a),identity)
    check('JI=-K',matmul(jj,ii),[[-x for x in row] for row in kk])
    for form, expected in [(wi,scale(wi,-1)),(wj,wj),(wk,scale(wk,-1)),(anti,anti)]:
        check('J form action '+str(form),tensor_pullback(form,jj),expected)
    for a in [wi,wj,wk,anti]:
        for b in [wi,wj,wk,anti]:
            check('J wedge pairing '+str((a,b)),
                  wedge(tensor_pullback(a,jj),tensor_pullback(b,jj)),wedge(a,b))
    dx, dy = {(0,):1}, {(1,):1}
    check('closed beta=x omegaJ-y omegaK',plus(wedge(dx,wj),scale(wedge(dy,wk),-1)),{})
    check('J beta not closed',plus(wedge(dx,wj),wedge(dy,wk)),{(0,1,3):-2})

    # Orthonormal tangent direction and curvature signs. After dividing
    # X by its positive factor 4q^(3/2), it is E2.
    e2 = (0,1,0,0)
    check('I E2',apply(ii,e2),(-1,0,0,0))
    check('J E2',apply(jj,e2),(0,0,0,-1))
    check('K E2',apply(kk,e2),(0,0,1,0))
    def pairing(form,v,w):
        return sum(c*(v[i]*w[j]-v[j]*w[i]) for (i,j),c in form.items())
    check('F(X,IX) normalized',pairing(anti,e2,apply(ii,e2)),1)
    check('F(X,JX) normalized',pairing(anti,e2,apply(jj,e2)),0)
    check('F(X,KX) normalized',pairing(anti,e2,apply(kk,e2)),0)
    check('F(JX,KX) normalized',pairing(anti,apply(jj,e2),apply(kk,e2)),-1)
    check('Chern fiber sign: i*(-2 pi i)/(2 pi)',Q(2)/2,Q(1))

    # Christoffel acceleration from g_qq=q, g_ss=q, g_rr=q^-1 at p=0.
    # These are Laurent polynomials in q, with one-component exponents.
    inv_gqq={( -1,):Q(1)}
    gss={(1,):Q(1)}
    grr={(-1,):Q(1)}
    gamma_ss=scale(times(inv_gqq,diff(gss,0)),Q(-1,2))
    gamma_rr=scale(times(inv_gqq,diff(grr,0)),Q(-1,2))
    accel_v=times({(-1,):Q(1)},gamma_ss)
    accel_w=times({(1,):Q(1)},gamma_rr)
    check('unit V Levi-Civita acceleration',accel_v,{(-2,):Q(-1,2)})
    check('unit W Levi-Civita acceleration',accel_w,{(-2,):Q(1,2)})
    # nabla_q S=Phi_prime/(4q); Hessian subtracts the acceleration.
    check('V Hessian source correction',scale(times(accel_v,{(-1,):Q(1,4)}),-1),{(-3,):Q(1,8)})
    check('W Hessian source correction',scale(times(accel_w,{(-1,):Q(1,4)}),-1),{(-3,):Q(-1,8)})

    # Laurent polynomials in (A, pi, q); normal ordering uses [B,A]=-pi/q.
    aa = {(1,0,0):Q(1)}
    cc = {(0,1,-1):Q(1)}
    rr = {(4,0,2):Q(1),(0,2,0):Q(-3)}
    for name, sign in [('W',-1),('V',1)]:
        first=plus(times(aa,rr),scale(times(cc,diff(rr,0)),sign))
        check(name+' first insertion has only odd jets',
              all(k[0] % 2 == 1 for k in first),True)
    base = times(times(aa,aa),rr)
    cross = times(cc,plus(rr,scale(times(aa,diff(rr,0)),2)))
    second = times(times(cc,cc),diff(diff(rr,0),0))
    wbracket = plus(base,scale(cross,-1),second)
    vbracket = plus(base,cross,second)
    check('W normal ordering',wbracket,
          {(6,0,2):Q(1),(4,1,1):Q(-9),(2,2,0):Q(9),(0,3,-1):Q(3)})
    check('V normal ordering',vbracket,
          {(6,0,2):Q(1),(4,1,1):Q(9),(2,2,0):Q(9),(0,3,-1):Q(-3)})
    def normalized(poly):
        out = {}
        for (a,p,q), value in times(poly,{(0,-2,1):Q(1)}).items():
            check('normalized pi/q weights '+str((a,p,q)),(p+a//2,q-a//2),(1,0))
            out[a//2] = value
        return out
    wn = normalized(wbracket)
    vn = scale(normalized(vbracket),-1)
    check('W normalized jets',wn,{3:Q(1),2:Q(-9),1:Q(9),0:Q(3)})
    check('V plus W relation',plus(vn,wn,{2:Q(18),0:Q(-6)}),{})

    # Univariate differential polynomials in D, represented with 1-tuples.
    one={(0,):Q(1)}
    dd={(1,):Q(1)}
    ladder=[one,dd]
    for m in range(1,3):
        ladder.append(plus(times(dd,ladder[m]),scale(ladder[m-1],2*m*(2*m-1))))
    p3=one
    for root in [1,3,5]:
        p3=times(p3,plus(dd,{(0,):Q(-root)}))
    wp=plus(*(scale(ladder[m],v) for m,v in wn.items()))
    vp=plus(*(scale(ladder[m],v) for m,v in vn.items()))
    check('W factorization',wp,p3)
    check('J raw e^u zero mode in units pi/16',sum(v for v in vp.values()),Q(-48))
    check('K raw e^u zero mode',sum(v for v in wp.values()),Q(0))
    fact=times(plus(dd,{(0,):Q(-9)}),{(2,):Q(1),(0,):Q(-1)})
    check('primitive compensation polynomial',plus(p3,scale(plus(dd,{(0,):Q(-1)}),-24)),fact)
    # S06: partial_p S=-i P3(D)psi/(32q); P=T0=e^u+2psi.
    check('K equals 4 pi i q partial_p S, scalar factor',Q(2,16),Q(4,32))
    check('completed K equals -4 pi C, scalar factor',Q(1),Q(-4)*Q(-1,4))

    repo=args.repo.resolve()
    base=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
    s06=base/'symmetries/06_hodge_and_transverse_geometry'
    theta=Path('papers/investigations-2/active/22_theta_manifold_geometry')
    paths=[base/'research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md',
           base/'reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md',
           s06/'notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md',
           s06/'notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md',
           s06/'reviews/01_TRANSVERSE_OBSERVATION_INTERNAL_REVIEW_20261018.md',
           s06/'reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md',
           theta/'manuscript/theta_manifold_geometry.tex',
           theta/'notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md',
           theta/'notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md',
           theta/'notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md']
    record={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
            'actual_model':'gpt-6.1-sol','actual_effort':'ultra',
            'llm_assistance':'substantial; same-model internal delegated review',
            'python':platform.python_version(),'status':'pass',
            'arithmetic':'exact rational finite matrices, exterior algebra and differential polynomials',
            'exact_checks':len(checks),'check_names':checks,
            'source_sha256':{str(p):hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in paths},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite algebra only. Analytic proofs and hypotheses are in Review 03.',
            'new_independent_physical_sign_estimate':False,
            'fresh_control_replay':False,'fresh_signed_certificate_replay':False}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','exact_checks':len(checks),'output':str(args.output)}))


if __name__=='__main__':
    main()
