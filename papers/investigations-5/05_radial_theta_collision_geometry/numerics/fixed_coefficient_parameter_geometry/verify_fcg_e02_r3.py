#!/usr/bin/env python3
"""Source-free exact-rational replay for the frozen FCG-E02 R3 assessment.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual model gpt-6.1-sol, effort ultra, Investigation05 chat0047.
Standard library only. No theta quadrature, parameter scan or new source data.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import argparse
import json
import re

PACKET_REL="papers/investigations-5/05_radial_theta_collision_geometry/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R3_JOINT_JET_COEFFICIENT_ASSESSMENT_20261030.md"
PACKET_SHA="558627511b346b854a2145c9f27ebfd0dd7031dfb91ef0b046b9c3fe53c805d0"
RECORD_REL="papers/investigations-5/05_radial_theta_collision_geometry/numerics/fixed_coefficient_parameter_geometry/fcg_e01_r1_joint_jet_coefficient_20261030.json"


class I:
    def __init__(self,lo,hi=None):
        if isinstance(lo,I):
            self.lo,self.hi=lo.lo,lo.hi
        else:
            self.lo,self.hi=F(lo),F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,y):
        y=I(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-I(y)
    def __rsub__(self,y):return I(y)+-self
    def __mul__(self,y):
        y=I(y);p=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=I(y);assert not y.lo<=0<=y.hi
        return self*I(1/y.hi,1/y.lo)
    def __rtruediv__(self,y):return I(y)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0:return self.square()**(n//2) if n>2 else self.square()
        return self*(self**(n-1))
    def absolute(self):
        return I(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),
                 max(abs(self.lo),abs(self.hi)))
    def square(self):
        a=self.absolute();return I(a.lo*a.lo,a.hi*a.hi)
    def sqrt(self):
        assert self.lo>=0
        scale=2**512
        def down(x):return F(isqrt((x.numerator*scale*scale)//x.denominator),scale)
        lo=down(self.lo);upper=down(self.hi)
        if upper*upper<self.hi:upper+=F(1,scale)
        return I(lo,upper)
    def contains(self,x):
        x=I(x);return self.lo<=x.lo and self.hi>=x.hi
    def overlaps(self,x):return self.lo<=x.hi and x.lo<=self.hi
    def record(self):return {"lower_exact":str(self.lo),"upper_exact":str(self.hi)}


def pow2(p):
    m,e=int(p[0]),int(p[1])
    return F(m*2**e) if e>=0 else F(m,2**(-e))


def binary(obj):
    mid,rad=pow2(obj["mid_binary"]),pow2(obj["rad_binary"])
    assert rad>=0
    return I(mid-rad,mid+rad)


def decimal(text):
    text=text.strip()
    if text.startswith("["):
        mid,rad=text[1:-1].split("+/-")
        mid,rad=F(mid.strip()),F(rad.strip())
        return I(mid-rad,mid+rad)
    return I(F(text))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists(),"preserve prior replay record"
    root=args.repo.resolve();packet=root/PACKET_REL
    assert sha256(packet.read_bytes()).hexdigest()==PACKET_SHA
    rows=re.findall(r"\| \x60([^\x60]+)\x60 \| \x60([0-9a-f]{64})\x60 \|",packet.read_text())
    assert len(rows)==15
    hashes=[]
    for name,expected in rows:
        actual=sha256((root/name).read_bytes()).hexdigest()
        assert actual==expected,name
        hashes.append({"path":name,"sha256":actual,"matches":True})
    source=json.loads((root/RECORD_REL).read_text())
    assert source["terminal_status"]=="confirmed_positive_complete"
    assert source["selected_degree"]==8
    assert source["fixed_parameters"]=={
        "tau":"1/4","a":"882607/20000","r":"1/64","R":"1/32",
        "modes":8,"cutoff":1,"degrees":[8,16,32]}
    assert source["runtime"]["python_flint"]=="0.9.0"
    assert source["limits"]=={"acquisition_seconds":1200,"eval_limit":200000,"depth_limit":30}
    stages=[];stage_inputs=[];all_integrals=[];assertions=0
    def verify(condition,label):
        nonlocal assertions
        assert condition,label
        assertions+=1
    def stored_contains(obj,value,label):
        verify(binary(obj).contains(value),label)
    for stage in source["stages"]:
        bits=stage["bits"]
        verify(bits in (256,384),"fixed precision")
        at,rt=(160,128) if bits==256 else (224,192)
        verify(stage["absolute_tolerance"]=="2^-"+str(at),"absolute tolerance")
        verify(stage["relative_tolerance"]=="2^-"+str(rt),"relative tolerance")
        integrals=stage["integrals"];all_integrals+=integrals
        expected=20 if bits==256 else 24
        verify(len(integrals)==expected,"stage integral count")
        for item in integrals:
            finite=binary(item["finite_integral"]);complete=binary(item["complete"])
            mode=decimal(item["omitted_mode_error_upper"]).hi
            exterior=decimal(item["retained_source_error_upper"]).hi
            verify(mode>=0 and exterior>=0,"tail positivity")
            error=mode+exterior
            extra=I(-error,error) if item["kind"]=="center_jet" else I(0,error)
            verify(complete.contains(finite+extra),"finite integral plus both full tails")
            verify(decimal(item["quadrature_radius_upper"]).hi>=pow2(item["finite_integral"]["rad_binary"]),
                   "recorded quadrature radius")
            guard=item["guards"]
            verify(guard["all_passed"],"actual guard flag")
            verify(decimal(guard["beta"]).lo>0,"mode beta")
            verify(decimal(guard["ratio"]).hi<1,"mode ratio")
            verify(decimal(guard["time_guard"]).lo>=0,"mode time guard")
            verify(len(guard["source_denominators"])==8,"eight source guards")
            verify(all(decimal(v).lo>0 for v in guard["source_denominators"]),"source tangent denominators")
            verify(all(decimal(v).lo>0 for v in guard["source_concavity_guards"]),"source concavity")
            verify(item["callbacks"]<=200000,"callback cap")
        verify([x["kind"] for x in integrals[:2]]==["positive_moment"]*2,"moments first")
        verify([x["order"] for x in integrals[:2]]==[3,4],"moment orders")
        verify(all((x["T"],x["Y"])==("9/32","1/32") for x in integrals[:2]),"moment parameters")
        jets=integrals[2:20]
        verify([x["order"] for x in jets]==list(range(18)),"complete h0 through h17")
        verify(all(x["kind"]=="center_jet" and x["T"]=="1/4" and x["Y"]=="0" for x in jets),"jet parameters")
        h=[binary(x["complete"]) for x in jets]
        M3,M4=[binary(x["complete"]) for x in integrals[:2]]
        stage_inputs.append([M3,M4]+h)
        r,R=F(1,64),F(1,32);b,h1=h[2],h[1]
        def e0(z):return (z**3/6+z*z)*M3+z*z*M4/2
        def e1(z):return (z+z*z/2)*M3
        def q(m,n):
            if (m,n) in {(0,0),(0,1),(0,2),(1,0)}:return I(0)
            return (-1)**m*h[2*m+n]/(factorial(m)*factorial(n))
        expected_g={}
        for k in range(1,9):
            for m in range(k+1):
                n=k-m
                expected_g[m,n]=b*(n-2)*q(m,n)+h1*(n+1)*q(m,n+1)
        finite=sum((g.absolute()*r**sum(ij) for ij,g in expected_g.items()),I(0))
        MG=2*b.absolute()*e0(R)+(h1.absolute()+R*b.absolute())*e1(R)
        cauchy=MG*F(11,256)
        gamma=finite+cauchy
        D=h1.square()-2*b*h[0];time=2*b.square()*r
        d=D.absolute()-time-gamma
        normalizer=1+h[0].square()+h1.square()+b.square()
        c=d/normalizer
        K=(4*b.square()+(h1.absolute()+r*b.absolute()).square()).sqrt()
        mu=d/K
        sep=2*b.absolute()*e0(r)+(h1.absolute()+r*b.absolute())*e1(r)
        sep_d=D.absolute()-time-sep
        values={"D0":D,"time_allowance":time,"finite_coefficient_sum":finite,
                "M_G":MG,"cauchy_tail":cauchy,"Gamma_N":gamma,"d":d,
                "normalizer":normalizer,"c":c,"K_B":K,
                "direct_uniform_floor":mu,"Gamma_sep":sep,"separate_margin":sep_d}
        verify(len(stage["degrees"])==1 and stage["degrees"][0]["N"]==8,"first-degree stop")
        saved=stage["degrees"][0]
        for key,value in values.items():stored_contains(saved[key],value,key)
        verify(len(saved["coefficients"])==44,"coefficient coverage count")
        for row in saved["coefficients"]:
            ij=row["m"],row["n"];g=expected_g.pop(ij)
            verify(decimal(row["g"]).contains(g),"signed coefficient enclosure")
            verify(decimal(row["weighted_absolute"]).contains(g.absolute()*r**sum(ij)),
                   "weighted coefficient enclosure")
        verify(not expected_g,"all coefficient indices covered once")
        verify(d.lo>F("5.07e-13") and c.lo>F("5.07e-13"),"positive d and c rational floors")
        verify(mu.lo>F("1.01e-6"),"positive jet floor")
        verify(sep_d.lo>F("4.35e-13"),"independent allowance also passes")
        # Supplemental same-information component comparison; keeps the joint theorem.
        H_floor=h[0].lo-h1.absolute().hi*r-b.absolute().hi*(r+r*r/2)-e0(r).hi
        verify(H_floor>F("9.9e-7"),"same-input scalar H-positive comparison")
        stages.append({"bits":bits,"all_derived_saved_balls_contain_exact_reconstruction":True,
                       "H_scalar_floor":str(H_floor),
                       "d_lower_exact":str(d.lo),"c_lower_exact":str(c.lo),
                       "mu_lower_exact":str(mu.lo)})
    verify(len(stage_inputs)==2,"two precision stages")
    for a,b in zip(*stage_inputs):verify(a.overlaps(b),"complete input cross-precision overlap")
    for key in ("D0","Gamma_N","d","c","K_B","direct_uniform_floor","separate_margin"):
        verify(binary(source["stages"][0]["degrees"][0][key]).overlaps(
               binary(source["stages"][1]["degrees"][0][key])),"derived cross-precision overlap")
    carrier=source["stages"][1]["integrals"][20:]
    verify([(x["order"],x["T"],x["Y"]) for x in carrier]==
           [(0,"17/64","0"),(1,"17/64","0"),(0,"17/64","4"),(1,"17/64","4")],
           "four post-confirmation carrier inputs")
    L=binary(carrier[0]["complete"])+binary(carrier[1]["complete"])
    R2=binary(carrier[2]["complete"])+binary(carrier[3]["complete"])
    pc=source["positive_consequence"]
    stored_contains(pc["L"],L,"complete carrier L")
    stored_contains(pc["R2"],R2,"complete carrier R2")
    saved=source["stages"][1]["degrees"][0]
    cl=binary(saved["c"]).lo;ml=binary(saved["direct_uniform_floor"]).lo
    # Use the published L/R2 balls' upper endpoints, as the executed code does.
    Lhi,Rhi=binary(pc["L"]).hi,binary(pc["R2"]).hi
    Nhi=max(Rhi+6*Lhi,3*Lhi/cl)
    verify(Lhi<F("0.068") and Rhi<F("0.101"),"carrier reporting bounds")
    verify(Nhi<F("4.01e11"),"second-moment ceiling")
    h=[binary(x["complete"]) for x in source["stages"][1]["integrals"][2:20]]
    M3,M4=stage_inputs[1][:2]
    B2=h[2].absolute()+F(1,64)*(M3+M4)
    stored_contains(pc["B2"],B2,"B2")
    verify(1+B2.hi/ml<F("3.496")<4,"C01 comparison coefficient 4")
    mus,Ns=F("1.01e-6"),F("4.01e11")
    energy_squared=9*mus**7/(2048*F(22,7)**2*Ns**3)
    verify(energy_squared>F("8.6e-41")**2,"exact squared energy floor with pi<22/7")
    rr=F(1,64)
    widened_H_floor=(F("1.03403761e-6")-rr*F("2.96993926e-8")
        -F("2.50273821e-7")*(rr+rr*rr/2)
        -(rr**3/6+rr*rr)*F("1.21893827e-4")
        -rr*rr*F("2.36386624e-5")/2)
    verify(widened_H_floor==F(980002569105109,983040000000000000000)
           and widened_H_floor>F("9.9e-7"),"widened same-information scalar comparison")
    cost=source["cost_summary"]
    keys={(x["kind"],x["order"],x["T"],x["Y"]) for x in all_integrals}
    verify(len(all_integrals)==44 and len(keys)==24,"acquisition counts")
    verify(sum(x["callbacks"] for x in all_integrals)==21716,"callback sum")
    verify(cost["distinct_source_integrands"]==24 and cost["precision_stage_quadrature_calls"]==44,"cost semantics")
    verify(source["elapsed_acquisition_seconds"]<1200,"acquisition time cap")
    result={"task":"FCG-E02 R3","date":"2026-10-30","prepared_for":"Edward Baker",
            "llm_assistance":"Substantial; same-assistant internal assessment",
            "model":"gpt-6.1-sol","effort":"ultra","chat":"0047",
            "packet":{"path":PACKET_REL,"sha256":PACKET_SHA},
            "inputs":hashes,"script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
            "method":"Exact Fraction interval reconstruction; no source quadrature or new numerical acquisition",
            "checks_passed":assertions,"stages":stages,
            "rational_reporting_bounds":{"d_gt":"5.07e-13","c_gt":"5.07e-13",
                "mu_gt":"1.01e-6","Nbar_lt":"4.01e11","delta_gt":"8.6e-41",
                "C01_coefficient":4,"supplemental_H_gt":"9.9e-7"},
            "energy_squared_lower":str(energy_squared),
            "widened_same_information_H_floor":str(widened_H_floor),"all_passed":True,
            "limitations":"Hashes and rational replay verify identity and internal arithmetic; analytic remainder, Arb quadrature validity, controls and propagation require the written assessment. No specialist or formal independence."}
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"{assertions} exact-rational consistency checks passed; 15 frozen hashes matched.")
    print("Both original precision stages and all stated floors retained; same-input H>9.9e-7.")
    print(args.output)


if __name__=="__main__":main()
