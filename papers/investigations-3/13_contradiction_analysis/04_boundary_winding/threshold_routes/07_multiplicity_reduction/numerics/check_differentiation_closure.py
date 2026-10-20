#!/usr/bin/env python3
"""Exact own-source controls for BW-07; not numerical theta evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import subprocess


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def scale(p, c):
    return trim([c*x for x in p])


def deriv(p, n=1):
    for _ in range(n):
        p = trim([i*p[i] for i in range(1, len(p))] or [0])
    return p


def at(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out


def heat(p, s):
    out = [F(0)]
    for j in range((len(p)-1)//2+1):
        out = add(out, scale(deriv(p, 2*j), (-s)**j/F(factorial(j))))
    return out


def mul_truncated(p, q, order=2):
    out = [F(0)]*(order+1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            if i+j <= order:
                out[i+j] += x*y
    return out


def subst_series(p, xseries, order=2):
    out = [F(0)]*(order+1)
    power = [F(1)]+[F(0)]*order
    for c in p:
        out = [u+c*v for u,v in zip(out, power)]
        power = mul_truncated(power, xseries, order)
    return out


def critical_heat_series(g, a):
    # Independent substitution into sum_j (-s)^j/j! g^(2j)(x(s)).
    g2, g3 = at(deriv(g, 2), a), at(deriv(g, 3), a)
    xseries = [a, g3/g2, F(0)]
    out = [F(0)]*3
    for j in range(3):
        part = subst_series(deriv(g, 2*j), xseries)
        for degree in range(3-j):
            out[degree+j] += F((-1)**j, factorial(j))*part[degree]
    return out


def imag_amplitude(p, epsilon):
    out = [F(0)]*len(p)
    for j, c in enumerate(p):
        if c:
            assert j % 2 == epsilon
            out[j] = (-1)**((j-epsilon)//2)*c
    return trim(out)


def polynomial_control(m, a):
    k = m-2
    epsilon = k % 2
    p = [F(0)]*(2*m+1)
    for j in range(m+1):
        p[2*j] = F((-1)**j*comb(m,j), a**(2*j))
    sign = (-1)**(k//2 if epsilon == 0 else (k+1)//2)
    g = scale(deriv(p,k),sign)
    assert at(g,a) == at(deriv(g),a) == 0
    gj = {j:at(deriv(g,j),a) for j in range(2,7)}
    assert gj[2] != 0
    assert all(at(deriv(p,j),a) == 0 for j in range(m))
    assert at(deriv(p,m),a) != 0
    if epsilon:
        assert g[0] == 0 and g[1] != 0
    else:
        assert g[0] != 0
    amp = imag_amplitude(g,epsilon)
    assert at(amp,a) > 0
    d = at(deriv(amp),a)/at(amp,a)
    s = gj[3]**2/(9*gj[2]**2)-gj[4]/(6*gj[2])
    comparison_gap = s-d/a+F(3,2*a*a)
    assert comparison_gap >= 0
    assert s >= F(1,2*a*a)+F(epsilon,a*a)
    for delta in [F(-1,256),F(1,256),F(1,16)]:
        assert scale(deriv(heat(p,delta),k),sign) == heat(g,delta)
    curve = critical_heat_series(g,F(a))
    vsecond = 2*curve[2]/gj[2]
    assert curve[0] == 0 and curve[1] == -gj[2]
    assert vsecond == gj[4]/gj[2]-(gj[3]/gj[2])**2
    assert vsecond == -F(1,3)*(gj[3]/gj[2])**2-6*s
    # Flexible-b comparison is independent of the imaginary-axis source floor.
    b = max(a,40)
    db = at(deriv(amp),b)/at(amp,b)
    flexible_gap = s-F(1,2*a*a)-db/b+F(4,a*a+b*b)
    assert flexible_gap >= 0
    return dict(m=m,k=k,a=a,parity="odd" if epsilon else "even",
                deflated_S=str(s),D_at_a=str(d),comparison_gap=str(comparison_gap),
                flexible_b=b,flexible_comparison_gap=str(flexible_gap),
                critical_value_second_derivative=str(vsecond),
                physical_index=-(m//2),derivative_index=-1,
                scope="exact polynomial identities; no theta floor imposed")


def positive_atom_controls():
    # b=log(2), u=1,2; t=0 or log(2): all hyperbolic and time weights rational.
    records=[]
    for k in range(7):
        ds=[]
        for time_power in [0,1]:
            den=num=F(0)
            base_den=base_num=F(0)
            for u, mass in [(1,F(1)),(2,F(3))]:
                ex=F(2)**u
                co=(ex+1/ex)/2
                si=(ex-1/ex)/2
                time=F(2)**(time_power*u*u)
                den += mass*time*u**k*(si if k%2 else co)
                num += mass*time*u**(k+1)*(co if k%2 else si)
                base_den += mass*time*co
                base_num += mass*time*u*si
            d=num/den
            dbase=base_num/base_den
            assert d>=dbase
            if k:
                assert d>dbase
            ds.append(d)
            records.append(dict(k=k,time="0" if time_power == 0 else "log(2)",
                                b="log(2)",D=str(d),base_D=str(dbase)))
        assert ds[1]>ds[0]
    return records


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo-root",type=Path,required=True)
    parser.add_argument("--note",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    repo=args.repo_root.resolve()
    own=Path(__file__).resolve()
    note=args.note or own.parent.parent/"notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md"
    output=args.output or own.parent/"DIFFERENTIATION_CLOSURE_CONTROLS_20261020.json"
    base=repo/"papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes"
    sources={
        "checker":own,
        "note":note,
        "BW01_contract":base/"01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md",
        "BW01_result":base/"01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md",
        "BW08_result":base/"08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md",
    }
    records=[polynomial_control(m,a) for m in range(2,9) for a in [1,20]]
    atom_records=positive_atom_controls()
    record={
        "date":"2026-10-20",
        "prepared_for":"Edward Baker",
        "model":"gpt-6-astra (Codex)","reasoning_effort":"ultra",
        "method":"Python standard-library Fraction arithmetic",
        "status":"exact controls passed; no theta event or theta certificate",
        "source_parent":subprocess.check_output(["git","rev-parse","HEAD"],cwd=repo,text=True).strip(),
        "source_sha256":{key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in sources.items()},
        "polynomial_controls":records,
        "two_atom_positive_source_controls":atom_records,
        "negative_controls_and_limits":[
            "For m=4 the physical index is -2 while derivative index is -1; degree preservation rejected.",
            "Odd transforms have a simple origin and use coth, not the even-source tanh statistic.",
            "No theta imaginary-axis floor assigned to polynomial controls.",
            "No numerical threshold assigned to an existence-only control.",
            "Finite checks do not establish all-m closure; the note supplies its proof."
        ]
    }
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"polynomial_cases":len(records),
                      "positive_atom_cases":len(atom_records),"record":str(output)}))


if __name__ == "__main__":
    main()
