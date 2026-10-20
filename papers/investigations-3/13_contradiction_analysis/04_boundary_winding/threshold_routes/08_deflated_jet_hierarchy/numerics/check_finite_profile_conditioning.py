#!/usr/bin/env python3
"""Exact rational replay of BW2-03 finite-profile pencils.

Prepared for Edward Baker, 20 October 2026, with substantial LLM assistance.
Authoring model gpt-6-astra; effort ultra, verified by parent turn metadata.
Only Python's standard library is used. No floating value decides a sign.
This is a control replay, not a theta computation or a threshold certificate
independent of the written proof.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json
import hashlib
import argparse
import subprocess


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        r[i] += v
    for i, v in enumerate(q):
        r[i] += v
    return trim(r)


def scale(p, c):
    return trim([v*c for v in p])


def mul(p, q):
    r = [Q(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def prod(polys):
    p = [Q(1)]
    for q in polys:
        p = mul(p, q)
    return p


def deriv(p, n=1):
    for _ in range(n):
        p = [Q(i)*p[i] for i in range(1, len(p))] or [Q(0)]
    return trim(p)


def value(p, x):
    out = Q(0)
    for c in reversed(p):
        out = out*x+c
    return out


def solve(matrix, rhs):
    n = len(rhs)
    aug = [list(row)+[v] for row, v in zip(matrix, rhs)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        d = aug[j][j]
        aug[j] = [v/d for v in aug[j]]
        for i in range(n):
            if i != j:
                c = aug[i][j]
                aug[i] = [v-c*w for v,w in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]


def pencil(xs, nodes, radius):
    # Enforce derivative(V/R0)(node)=0 with first residue exactly one.
    matrix = [[1/(t-x)**2 for x in xs[1:]] for t in nodes]
    rhs = [-1/(t-xs[0])**2 for t in nodes]
    residues = [Q(1)]+solve(matrix, rhs)
    factors = [[-x, Q(1)] for x in xs]
    r0 = prod(factors)
    v = [Q(0)]
    for j, c in enumerate(residues):
        v = add(v, scale(prod(factors[:j]+factors[j+1:]), c))
    for t in nodes:
        assert value(deriv(v),t)*value(r0,t) == value(v,t)*value(deriv(r0),t)
    C = max(abs(c) for c in residues)
    Ms = [sum((abs(residues[l])/(abs(xs[j]-xs[l])-radius)
               for l in range(len(xs)) if l != j), Q(0))
          for j in range(len(xs))]
    M = max(Ms)
    eps0 = min(radius/(4*C), 1/(4*M)) if M else radius/(4*C)
    return r0, v, residues, Ms, eps0


def check_intervals(xs, residues, radius, eps):
    for j, x in enumerate(xs):
        def f(d):
            return d+eps*residues[j]+eps*d*sum(
                (residues[l]/(x+d-xs[l]) for l in range(len(xs)) if l != j),
                Q(0))
        assert f(radius) >= radius/2
        assert f(-radius) <= -radius/2


def record_rational(x):
    return {"exact": str(x), "display": float(x)}


def polynomial_replay():
    a, A = Q(20), Q(400)
    bs = [Q(20), Q(40)]
    nodes = [-b*b for b in bs]
    xs = [A, Q(900), Q(2100)]  # c=500
    # Keep fixed roots separated from compensation-root intervals.
    fixed = [Q(1100), Q(1200), Q(1300), Q(1400), Q(1500)]
    radius = Q(50)
    r0,v,residues,Ms,eps0 = pencil(xs,nodes,radius)
    W = prod([[-x,Q(1)] for x in fixed])
    event_factor = mul([-A,Q(1)],[-A,Q(1)])
    baseline = mul(mul(event_factor,r0),W)
    target = [-2*b*value(deriv(baseline),-b*b)/value(baseline,-b*b) for b in bs]
    assert target[0] > Q(3,20)
    assert target[1] > Q(297,1000)
    rows = []
    for divisor in [2,4,8,16]:
        eps=eps0/divisor
        check_intervals(xs,residues,radius,eps)
        R=add(r0,scale(v,eps))
        G=mul(mul(event_factor,R),W)
        G=scale(G,1/value(G,Q(0)))
        F=[Q(0)]*(2*len(G)-1)
        for j,c in enumerate(G):
            F[2*j]=c
        h=[value(deriv(F,j),a) for j in range(5)]
        assert h[0] == h[1] == 0 and h[2] != 0 and value(F,Q(0))==1
        observed=[-2*b*value(deriv(G),-b*b)/value(G,-b*b) for b in bs]
        assert observed == target
        S=h[3]**2/(9*h[2]**2)-h[4]/(6*h[2])
        L=Q(1,200)
        QL=2*h[3]**2-3*h[2]*h[4]-18*L*h[2]**2
        assert QL == 18*h[2]**2*(S-L) and QL > 0
        # Weaker rational version of the analytic lower bound (17):
        # a+sqrt(A-radius)>a, hence S>1/(2a²)+a²/(4eps²).
        assert S > 1/(2*A)+A/(4*eps**2)
        # Explicit time coefficients of the polynomial heat expansion.
        heat=[scale(deriv(F,2*n), Q((-1)**n,factorial(n)))
              for n in range((len(F)-1)//2+1)]
        for n in range(len(heat)-1):
            assert add(scale(heat[n+1],n+1),deriv(heat[n],2)) == [0]
        assert deriv(heat[-1],2) == [0]
        rows.append({"epsilon":str(eps),"h2":record_rational(h[2]),
                     "S2":record_rational(S),"Q_1_over_200":record_rational(QL)})
    return {"a":str(a),"b":[str(b) for b in bs],"c":"500",
            "fixed_root_squares":[str(x) for x in fixed],
            "radius":str(radius),"residues":[str(x) for x in residues],
            "M":[str(x) for x in Ms],"epsilon_cap":str(eps0),
            "fixed_profile":[record_rational(x) for x in target],"rows":rows}


def chebyshev(n):
    if n==0:
        return [Q(1)]
    if n==1:
        return [Q(0),Q(1)]
    a,b=[Q(1)],[Q(0),Q(1)]
    for _ in range(2,n+1):
        a,b=b,add(mul([Q(0),Q(2)],b),scale(a,Q(-1)))
    return b


def cosine_coefficients(P):
    w=[Q(0)]*len(P)
    for m,c in enumerate(P):
        for j in range(m+1):
            w[abs(m-2*j)]+=c*Q(comb(m,j),2**m)
    return w


def trig_replay():
    qs=[Q(1,2),Q(1,4),Q(3,4)]
    xs=[-q for q in qs]
    nodes=[Q(2),Q(3)]
    radius=Q(1,16)
    r0,v,residues,Ms,eps0=pencil(xs,nodes,radius)
    q0=qs[0]
    fixed=mul([q0,Q(1)],[q0,Q(1)])
    baseline=mul(fixed,r0)
    target=[value(deriv(baseline),t)/value(baseline,t) for t in nodes]
    rows=[]
    for divisor in [2,4,8,16]:
        eps=eps0/divisor
        check_intervals(xs,residues,radius,eps)
        R=add(r0,scale(v,eps))
        P=mul(fixed,R)
        P=scale(P,1/value(P,Q(1)))
        assert all(c>0 for c in P)
        observed=[value(deriv(P),t)/value(P,t) for t in nodes]
        assert observed==target
        assert value(P,-q0)==value(deriv(P),-q0)==0
        w=cosine_coefficients(P)
        assert len(w)==6 and all(c>0 for c in w) and sum(w)==1
        reconstructed=[Q(0)]
        for n,c in enumerate(w):
            reconstructed=add(reconstructed,scale(chebyshev(n),c))
        assert reconstructed==P
        # Spatial operator in dimensionless angle: D²=(1-y²)d²-y d.
        Lpoly=add(mul([Q(1),Q(0),Q(-1)],deriv(P,2)),
                  mul([Q(0),Q(-1)],deriv(P)))
        diag=[Q(0)]
        for n,c in enumerate(w):
            diag=add(diag,scale(chebyshev(n),-n*n*c))
        assert Lpoly==diag
        P2,P3,P4=[value(deriv(P,j),-q0) for j in [2,3,4]]
        s2=1-q0*q0
        J2=s2*P2
        J3sq=s2*(s2*P3+3*q0*P2)**2
        J4=s2*s2*P4+6*s2*q0*P3+(3*q0*q0-4*s2)*P2
        assert J2 != 0
        Sscaled=J3sq/(9*J2*J2)-J4/(6*J2)
        lower=(1-(q0+radius)**2)/(4*eps*eps)
        assert Sscaled >= lower
        # a=20: lambda²=pi²/900>1/100; hence L/lambda²<1/2 for L=1/200.
        qlower=2*J3sq-3*J2*J4-9*J2*J2
        assert qlower > 0
        rows.append({"epsilon":str(eps),"h2_over_lambda2":record_rational(J2),
                     "S2_over_lambda2":record_rational(Sscaled),
                     "proved_lower_S2_over_lambda2":record_rational(lower),
                     "lower_Q_over_lambda6_for_L_1_over_200":record_rational(qlower),
                     "positive_cosine_weights":[str(x) for x in w]})
    return {"q":[str(q) for q in qs],"cosh_lambda_b":[str(t) for t in nodes],
            "radius":str(radius),"residues":[str(x) for x in residues],
            "M":[str(x) for x in Ms],"epsilon_cap":str(eps0),
            "fixed_D_divided_by_lambda_sinh":[str(x) for x in target],
            "rows":rows}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name(
        "FINITE_PROFILE_CONDITIONING_CONTROLS_20261020.json"))
    parser.add_argument("--repo-root",type=Path,default=None)
    args=parser.parse_args()
    result={"status":"exact-rational-control-replay-passed",
            "date":"2026-10-20","author":"Prepared for Edward Baker with LLM assistance",
            "model":"gpt-6-astra","effort":"ultra",
            "scope":"Own-source controls; no theta event or new theta exclusion",
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "polynomial":polynomial_replay(),"positive_six_atom":trig_replay()}
    repo=args.repo_root
    if repo is None:
        repo=next((p for p in Path(__file__).resolve().parents
                   if (p/"LARGE_FILES.md").is_file() and (p/".git").exists()),None)
    if repo is not None:
        relbase="papers/investigations-3/13_contradiction_analysis/04_boundary_winding/"
        inputs=["result-summaries/README.md","result-summaries/12_collision_controls_and_screening.md",
                "avoid/README.md",
                relbase+"research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md",
                relbase+"threshold_routes/README.md",
                relbase+"threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md",
                relbase+"threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md",
                relbase+"threshold_routes/08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md"]
        result["input_sha256"]={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in inputs}
        result["repository_parent"]=subprocess.check_output(
            ["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("Exact rational polynomial and positive six-atom replays passed.")
    print("Record:",args.output)
    print("Polynomial epsilon cap:",result["polynomial"]["epsilon_cap"])
    print("Six-atom epsilon cap:",result["positive_six_atom"]["epsilon_cap"])
    print("Six-atom fixed normalized profiles:",
          result["positive_six_atom"]["fixed_D_divided_by_lambda_sinh"])


if __name__=="__main__":
    main()
