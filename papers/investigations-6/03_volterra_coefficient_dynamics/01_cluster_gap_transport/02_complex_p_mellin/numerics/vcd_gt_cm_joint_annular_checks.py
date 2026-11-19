#!/usr/bin/env python3
"""E43 exact-rational premise checks; deliberately no new D enclosure.

18 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Assessor settings inherited; actual serving model and effort unavailable.
Prior E41/E42 reviewer overlap and shared source premises are retained.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
CM = HERE.parent
REPO = next(p for p in HERE.parents if (p / "LARGE_FILES.md").is_file())
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E43-inputs-r1.json"
OUTPUT = HERE / "29_VCD_GT_CM_JOINT_ANNULAR_CHECKS_20261118.json"


def identity(path):
    data = path.read_bytes()
    return {"path":str(path.relative_to(REPO)),"bytes":len(data),
            "sha256":hashlib.sha256(data).hexdigest()}


def verify_inputs():
    rows=[]
    for expected in json.loads(MANIFEST.read_text())["inputs"]:
        actual=identity(REPO/expected["path"])
        if actual!=expected:
            raise ValueError("Frozen input differs: "+expected["path"])
        rows.append({**actual,"matches":True})
    return rows


def ball(text):
    if not isinstance(text,str):
        raise TypeError("Expected textual rational or midpoint-radius enclosure")
    if not text.startswith("["):
        value=F(text)
        return value,value
    match=re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]",text)
    if match is None:
        raise ValueError("Unsupported enclosure: "+text)
    midpoint,radius=map(F,match.groups())
    if radius<0:
        raise ValueError("Negative radius")
    return midpoint-radius,midpoint+radius


def add(*polys):
    result={}
    for poly in polys:
        for key,value in poly.items():
            result[key]=result.get(key,F(0))+value
    return {k:v for k,v in result.items() if v}


def mul(left,right):
    result={}
    for x,a in left.items():
        for y,b in right.items():
            key=tuple(u+v for u,v in zip(x,y))
            result[key]=result.get(key,F(0))+a*b
    return {k:v for k,v in result.items() if v}


def main():
    verified=verify_inputs()
    data=json.loads((HERE/"22_VCD_GT_CM_CARDINAL_SOURCE_REFINEMENT_20261118.json").read_text())
    can=data["canonical"]
    control=data["quadratic_control"]
    checks=[]

    def check(name,condition,**values):
        if not condition:
            raise AssertionError(name)
        checks.append({"name":name,"passes":True,
                       "exact_values":{k:str(v) for k,v in values.items()}})

    check("fixed_record_parameters", data["time_interval"]==["-3/10000","1/10"]
          and data["bits"]==224 and data["contour_nodes"]==128
          and data["time_cells"]==512
          and data["spatial_degree"]==data["time_degree"]==32)
    check("inherited_success_and_monotonicity", data["success"] and can["all_gates"]
          and can["count_on_each_boundary"]==2
          and can["whole_time_monotonicity"]["all_gates"]
          and F(can["whole_time_monotonicity"]["derivative_lower_strict"])==F(942,625))
    rminus,rho,rplus=F(3,4),F(9,10),F(21,20)
    N=data["contour_nodes"]
    qm,qp=(rminus/rho)**N,(rho/rplus)**N
    check("annular_ratios_and_N", N>2 and 0<qm<1 and 0<qp<1
          and rminus/rho==F(5,6) and rho/rplus==F(6,7))
    h=F(can["reference_h_exact"])
    check("exact_h_import", F(63,1000)<h<F(8,125))
    for name,radius in [("inner",rminus),("outer",rplus)]:
        x=abs(h)/radius
        check("h_ratio_"+name,F(3,50)<x<1,x=x)
    check("integer_five_percent_gate",400*2509<361*2809,
          positive_integer_margin=361*2809-400*2509)
    for name,q in [("inner",qm),("outer",qp)]:
        check("geometric_ratio_"+name,(1-q)**2<1-q*q)

    e1lo,e1hi=ball(can["epsilon1"])
    e2lo,e2hi=ball(can["epsilon2"])
    check("positive_serialized_allowances",0<e1lo<=e1hi and 0<e2lo<=e2hi)
    Alo=e2lo/2+abs(h)*e1lo
    lowerlo,lowerhi=ball(can["centered_direct"]["lower"])
    upperlo,upperhi=ball(can["centered_direct"]["upper"])
    old_width_outer=upperhi-lowerlo
    check("annular_width_premise",2*Alo>F(111,10**10),twice_Alo=2*Alo)
    check("old_full_width_premise",0<old_width_outer<F(23,10**9),old_parsed_width=old_width_outer)
    saving_floor=F(111,10**10)/20
    target_ceiling=F(24,1000)*F(23,10**9)
    check("coarse_total_width_gain",saving_floor-target_ceiling==F(3,10**12)>0,
          saving_lower=saving_floor,target_2_4_percent_upper=target_ceiling,
          coarse_margin=saving_floor-target_ceiling)
    check("future_primary_gate_is_weaker",F(2,100)<F(24,1000))

    hlo,hhi=ball(control["centered_direct"]["h"])
    control_h_abs=max(abs(hlo),abs(hhi))
    check("quadratic_factor_guard_fails",control_h_abs/rminus<F(3,50)
          and control_h_abs/rplus<F(3,50))
    clo,chi=ball(control["centered_direct"]["lower"]),ball(control["centered_direct"]["upper"])
    check("inherited_quadratic_contains_collision",clo[0]<0<chi[1]
          and F(control["exact_D"])==0 and control["retains_collision"]
          and control["strict_path_gates_fail"] and control["success"])

    # Exact numerator of K_aff+K_res-K_dir after multiplying by Z^2 Q;
    # polynomial variables are Z and D, Q=Z^2-D.
    flux=add(mul({(0,1):F(4)},{(2,0):F(1),(0,1):F(-1)}),
             {(0,2):F(4)},{(2,1):F(-4)})
    check("joint_affine_flux_identity",not flux)
    # At a double root b: p1=2b, p2=2b^2, and J_h=(b-h)^2.
    # Polynomial variables are b and h; this checks the complete square.
    J={(2,0):F(1),(1,1):F(-2),(0,2):F(1)}
    square=mul({(1,0):F(1),(0,1):F(-1)},
               {(1,0):F(1),(0,1):F(-1)})
    check("quadratic_full_square_identity",J==square)

    if verify_inputs()!=verified:
        raise ValueError("Inputs changed during checks")
    result={
        "task":"VCD-GT-CM-E43 r1","date":"2026-11-18","timezone":"America/New_York",
        "prepared_for":"Edward Baker","assistance":"OpenAI Codex LLM assistance; nonauthor internal shared-premise assessment",
        "actual_serving_model":None,"actual_serving_effort":None,
        "reviewer_overlap":"prior E41/E42 assessor; not Note52 author",
        "status":"exact-rational frozen-premise checks passed",
        "script":identity(Path(__file__).resolve()),"input_manifest":identity(MANIFEST),
        "verified_inputs":verified,"arithmetic":"Python standard-library fractions.Fraction; exact serialization parsing",
        "python_version":sys.version.split()[0],"checks":checks,"all_passed":True,
        "proof_pass_checks_not_inferred_from_sampling":[
            "single analytic annular logarithm from strict positive real part on both boundaries",
            "Laurent alias normalization and disjoint coefficient ladders for N>2",
            "Parseval and Cauchy-Schwarz yield the joint annular bound",
            "upward chosen tail weights and moment errors imply A_raw<=A",
            "moving already outward old endpoints by no more than A/20 retains their rounding slack",
            "epsilon1 and the full Gamma square remain unchanged"
        ],
        "scope":{
            "new_D_enclosure_computed":False,"new_source_calls":0,"new_zero_calls":0,
            "numerical_integration":False,"source_or_geometry_replay":False,
            "precision_change":False,"numerical_campaign":False,
            "specialist_or_attested_cross_model_independence":False,
            "meaning":"checks Note52 premises and guard; future E44 owns the new finite interval"
        }
    }
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"passed","checks":len(checks),"inputs":len(verified),
                      "new_D_enclosure":False,"output":str(OUTPUT.relative_to(REPO))}))


if __name__=="__main__":
    main()
