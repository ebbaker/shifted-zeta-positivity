#!/usr/bin/env python3
"""Frozen adaptive-radius/IBP comparison, FCG-E01 R2 plus A1.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual execution model gpt-6.1-sol, effort ultra, existing chat0047.
Uses installed python-flint/Arb and frozen R1 arithmetic helpers.
Never writes manuscript files. Real interval panels are not Acb quadrature.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
import math
from pathlib import Path
import platform
import re
import signal
import sys
import time
import flint
from flint import arb, acb, ctx

BASE="papers/investigations-5/05_radial_theta_collision_geometry"
PACKET=BASE+"/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_ADAPTIVE_RADIUS_IBP_COMPARISON_20261030.md"
AMEND=BASE+"/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_A1_RADIUS_RULE_20261030.md"
PACKET_SHA="ded48f912d2fd4cd84fee44c009a1f3e69478050a4ffc8ba8ff351a98d6777dd"
AMEND_SHA="e687386c62824bc9db51ac4328364547c79ec2c4bcc4e5eac57453b78306bc22"
TAU=F(1,4);CENTER=F(64);R=F(1,32)
RADII=(F(1,64),F(1,128),F(1,256));DEGREES=(1,2,4,8)
PHI_COMPONENT=(2,2,9)
PRIME_COMPONENTS=((30,2,9),(15,1,5),(8,3,13))


def A(x):
    return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)


def check(condition,message):
    if not condition:raise ArithmeticError(message)


def rec(x):
    check(x.is_finite(),"nonfinite recorded interval")
    return x.str(65,more=True)


def binary(x):
    m,e=x.man_exp();return [str(m),int(e)]


def enc(x):
    return {"ball":rec(x),"mid_binary":binary(x.mid()),"rad_binary":binary(x.rad())}


def bounds(lo,hi,nonnegative=False):
    check(lo<=hi,"reversed interval")
    value=arb((lo+hi)/2,((hi-lo)/2).upper())
    return value.nonnegative_part() if nonnegative else value


def interval_min(values):
    return bounds(min(x.lower() for x in values),min(x.upper() for x in values),True)


def status(x):
    return "positive" if x>0 else ("nonpositive" if x<=0 else "unresolved")


def digest(path):return sha256(path.read_bytes()).hexdigest()


class Run:
    def __init__(self,root,output):
        self.root,self.output=root,output;self.started=time.monotonic();self.deadline=self.started+1200
        self.data={"task":"FCG-E01 R2","amendment":"A1","date":"2026-10-30",
            "prepared_for":"Edward Baker","llm_assistance":"Substantial; internal execution",
            "model":"gpt-6.1-sol","effort":"ultra","chat":"0047",
            "thread_id":"01a18d3a-0de3-7781-b7e1-79a42cf0a6fd",
            "manuscript_writes":False,
            "fixed":{"tau":"1/4","a":"64","R":"1/32","radii":[str(x) for x in RADII],
                     "degrees":list(DEGREES),"modes":8,"analytic_cutoff":1,
                     "U3":"41*pi/128","U4":"21*pi/64"},
            "limits":{"seconds":1200,"eval_limit":200000,"depth_limit":30,
                      "panel_counts":[1024,2048],"precisions":[256,384]},
            "runtime":{"python":sys.version,"executable":sys.executable,
                       "python_flint":flint.__version__,"flint":getattr(flint,"__FLINT_VERSION__","unavailable"),
                       "platform":platform.platform()},
            "script_sha256":digest(Path(__file__)),"inputs":[],"stages":[],
            "terminal_status":"in_progress","refinement":None}
        for path,expected,count in ((PACKET,PACKET_SHA,13),(AMEND,AMEND_SHA,3)):
            p=root/path;check(digest(p)==expected,"issued packet/amendment hash")
            self.data["inputs"].append({"path":path,"sha256":expected})
            rows=re.findall(r"\| \x60([^\x60]+)\x60 \| \x60([0-9a-f]{64})\x60 \|",p.read_text())
            check(len(rows)==count,"frozen hash-table count")
            for relative,h in rows:
                check(digest(root/relative)==h,"frozen input changed: "+relative)
                if not any(x["path"]==relative for x in self.data["inputs"]):
                    self.data["inputs"].append({"path":relative,"sha256":h})
        helper=root/BASE/"numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r1.py"
        spec=importlib.util.spec_from_file_location("frozen_r1",helper)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        self.absolute,self.square,self.positive_part=mod.absolute,mod.square,mod.positive_part
        self.old=mod
        ctx.prec=256
        self.data["algebra_checks"]=mod.algebra_checks()
        # New exact tail/phase/root algebra, without source evaluation.
        for n in DEGREES:
            q=F(1,2);t=q**(n+1)*((n+2)-(n+1)*q)/(1-q)**2
            check(t==F(n+3,2**n),"general Cauchy sum at 1/2")
        check(F(64)*F(41,128)+F(3,2)==22,"phase U3")
        check(F(64)*F(21,64)+2==23,"phase U4")
        # Clearing r^2: stable root implies L*r+8M*r^2/R^2=D/2.
        self.data["algebra_checks"].update({"general_tail_half":True,"phase_centers":True,
            "primitive_lower_endpoint":"analytic O(u^4) cancellation checked before acquisition",
            "sharp_radius_root":"D/(L0+sqrt(L0^2+16MD/R^2)); both-zero case treated separately"})
        self.stages=[];self.save()

    def cap(self):
        if time.monotonic()>=self.deadline:raise TimeoutError("20-minute acquisition cap")

    def save(self):
        self.data["elapsed_seconds"]=time.monotonic()-self.started
        allints=[i for s in self.data["stages"] for i in s["integrals"]]
        keys={(i["kind"],i["j"],i["T"],i["Y"]) for i in allints}
        panels=[p for s in self.data["stages"] for p in s["panel_acquisitions"]]
        self.data["cost"]={"distinct_analytic_integrands":len(keys),"analytic_calls":len(allints),
            "analytic_callbacks":sum(i["callbacks"] for i in allints),
            "analytic_seconds":sum(i["seconds"] for i in allints),
            "panel_acquisitions":len(panels),"panel_range_evaluations":sum(p["count"] for p in panels),
            "incremental_ibp_panel_seconds":sum(p["seconds"] for p in panels)}
        self.output.write_text(json.dumps(self.data,indent=2)+"\n")

    def component_tail(self,component,k,T,Y,U):
        C,p,q0=component;pi=arb.pi();m=9;T=A(T);Y=A(Y)
        beta=4*pi*m*m-q0-Y
        ratio=(arb(m+1)/m)**(2*p)*(-pi*(2*m+1)).exp()
        tg=8*pi*m*m-T
        check(beta>0 and ratio<1 and tg>=0,"generalized mode-tail guard")
        mode=C*pi**p*m**(2*p)*(-pi*m*m).exp()/(1-ratio)*math.factorial(k)/beta**(k+1)
        source=arb(0);denoms=[];concaves=[]
        for n in range(1,9):
            lam=pi*n*n;den=4*lam*(4*U).exp()-(q0+Y)-2*T*U-k/U
            conc=16*lam*(4*U).exp()-2*T
            check(den>0 and conc>0,"generalized source-tail guard")
            source+=C*lam**p*U**k*(T*U*U+(q0+Y)*U-lam*(4*U).exp()).exp()/den
            denoms.append(rec(den));concaves.append(conc.lower())
        detail={"component":[C,p,q0],"k":k,"T":rec(T),"Y":rec(Y),"U":rec(U),
                "mode_upper":rec(mode.upper()),"retained_exterior_upper":rec(source.upper()),
                "beta":rec(beta),"ratio":rec(ratio),"time_guard":rec(tg),
                "source_denominators":denoms,"minimum_concavity":rec(min(concaves)),"guards_pass":True}
        return mode.upper(),source.upper(),detail

    def B_tails(self,j,U):
        pieces=[(F(j),PHI_COMPONENT,j-1),(2*(TAU+R),PHI_COMPONENT,j+1)]
        pieces += [(F(1),c,j) for c in PRIME_COMPONENTS]
        mode=arb(0);source=arb(0);details=[]
        for multiplier,c,k in pieces:
            m,s,d=self.component_tail(c,k,TAU+R,R,U)
            mode+=A(multiplier)*m;source+=A(multiplier)*s
            d["multiplier"]=str(multiplier);details.append(d)
        return mode.upper(),source.upper(),details

    def finite_source(self,u,complex_value=False):
        q=(4*u).exp();total=acb(0) if complex_value else arb(0)
        prime=acb(0) if complex_value else arb(0);pi=arb.pi()
        for n in range(1,9):
            lam=pi*n*n;exp=(-lam*q).exp()
            total+=(2*lam*lam*q*q-3*lam*q)*exp
            prime+=(30*lam*lam*q*q-15*lam*q-8*lam**3*q*q*q)*exp
        eu=u.exp()
        return eu*total,eu*prime

    def integral(self,s,j,T,Y=F(0),signed=False):
        self.cap();start=time.monotonic();calls=0
        def integrand(u,analytic):
            nonlocal calls
            calls+=1;self.cap()
            # Entire expressions only; absolute-value cores use real panels below.
            q=(4*u).exp();total=acb(0);pi=arb.pi()
            for n in range(1,9):
                lam=pi*n*n
                total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
            value=(A(T)*u*u+(1+A(Y))*u).exp()*u**j*total
            if signed:
                phase=64*u
                trig=(phase.cos,phase.sin,phase.cos,phase.sin)[j%4]()
                if j%4 in (1,2):trig=-trig
                value*=trig
            return value
        v=acb.integral(integrand,0,1,abs_tol=s["abs"],rel_tol=s["rel"],
                       eval_limit=200000,depth_limit=30)
        check(v.is_finite() and v.imag.contains(0),"nonfinite/nonreal analytic source integral")
        mode,source,tail=self.component_tail(PHI_COMPONENT,j,T,Y,arb(1))
        err=(mode+source).upper()
        complete=v.real+arb(0,err) if signed else v.real+bounds(arb(0),err,True)
        check(complete.is_finite(),"nonfinite complete analytic integral")
        if not signed:check(complete>0,"positive moment not signed positively")
        item={"kind":"jet" if signed else "moment","j":j,"T":str(T),"Y":str(Y),
              "finite":enc(v.real),"quad_radius_upper":rec(v.real.rad().upper()),
              "mode_upper":rec(mode),"source_upper":rec(source),"complete":enc(complete),
              "tail":tail,"callbacks":calls,"seconds":time.monotonic()-start}
        s["record"]["integrals"].append(item);self.save()
        print("integral",s["bits"],item["kind"],j,str(T),str(Y),flush=True)
        return complete

    def new_stage(self,bits):
        ctx.prec=bits;at,rt=(180,140) if bits==256 else (280,240)
        record={"bits":bits,"abs_tolerance":"2^-"+str(at),"rel_tolerance":"2^-"+str(rt),
                "integrals":[],"panel_acquisitions":[],"passes":[]}
        self.data["stages"].append(record)
        s={"bits":bits,"abs":arb(2)**(-at),"rel":arb(2)**(-rt),"record":record,
           "h":[],"moments":{},"envelopes":{},"cases":{}}
        self.stages.append(s)
        for rho in (F(1,32),F(1,64),F(1,128)):
            s["moments"][rho]=[self.integral(s,j,TAU+rho,rho) for j in (3,4)]
        s["h"]=[self.integral(s,j,TAU,signed=True) for j in range(18)]
        return s

    def panels(self,s,j,count):
        self.cap();ctx.prec=s["bits"];start=time.monotonic()
        U=arb.pi()*(F(41,128).numerator)/F(41,128).denominator if j==3 else arb.pi()*21/64
        whole=arb(0);phase=arb(0);fingerprint=sha256();crossings=0
        for i in range(count):
            self.cap()
            v=arb(arb(2*i+1)/(2*count),arb(1)/(2*count)).nonnegative_part()
            u=U*v
            phi,prime=self.finite_source(u)
            phi=phi.nonnegative_part()
            inside=j*u**(j-1)*phi+2*A(TAU)*u**(j+1)*phi+u**j*prime
            if inside.contains(0):crossings+=1
            B=((A(TAU)+A(R))*u*u).exp()*(self.absolute(inside)+2*A(R)*u**(j+1)*phi)
            angle=64*u+arb.pi()*j/2
            S=self.absolute(angle.sin())*(A(R)*u).cosh()+self.absolute(angle.cos())*(A(R)*u).sinh()
            w1=(B*(A(R)*u).exp()*U/count).nonnegative_part()
            w2=(B*S*U/count).nonnegative_part()
            whole+=w1;phase+=w2
            fingerprint.update((rec(w1)+"|"+rec(w2)+"\n").encode())
        whole=whole.nonnegative_part();phase=phase.nonnegative_part()
        bm,bs,bd=self.B_tails(j,U)
        # Full mode upper is paid once symmetrically for the core and once
        # nonnegatively for the exterior. The intentional duplicate is recorded.
        whole_core=(whole+arb(0,bm)).nonnegative_part()
        I=(whole_core+bounds(arb(0),(bs+bm).upper(),True))/(64-A(R))
        pm,ps,pd=self.component_tail(PHI_COMPONENT,j,TAU+R,R,U)
        # Complete phase-aligned boundary, including omitted endpoint modes.
        finite_phi,_=self.finite_source(U)
        finite_phi=finite_phi.nonnegative_part()
        first=2*arb.pi()**2*9**4*(9*U-arb.pi()*81*(4*U).exp()).exp()
        ratio=(arb(10)/9)**4*(-arb.pi()*19*(4*U).exp()).exp()
        check(ratio<1,"endpoint omitted-mode ratio")
        endpoint_mode=(first/(1-ratio)).upper()
        endpoint_phi=finite_phi+bounds(arb(0),endpoint_mode,True)
        boundary=U**j*((A(TAU)+A(R))*U*U).exp()*endpoint_phi*(A(R)*U).sinh()
        phase_core=(phase+arb(0,bm)).nonnegative_part()
        W=(boundary+phase_core)/(64-A(R))+bounds(arb(0),(ps+pm).upper(),True)
        M=s["moments"][R][j-3]
        selected=interval_min([M,I,W])
        check(all(v.is_finite() for v in (I,W,selected)) and selected>0,"nonfinite/unsigned IBP envelope")
        strict=[name for name,x in (("I",I),("W",W)) if x.upper()<M.lower()]
        definitive=[name for name,x,others in (("M",M,[I,W]),("I",I,[M,W]),("W",W,[M,I]))
                    if all(x.upper()<y.lower() for y in others)]
        item={"j":j,"count":count,"U":rec(U),"finite_core_whole":enc(whole),
            "finite_core_phase":enc(phase),"core_mode_symmetric_upper":rec(bm),
            "whole_retained_exterior_upper":rec(bs),"whole_additional_mode_upper":rec(bm),
            "phase_retained_exterior_upper":rec(ps),"phase_exterior_mode_upper":rec(pm),
            "boundary":enc(boundary),"endpoint_mode_upper":rec(endpoint_mode),
            "endpoint_ratio":rec(ratio),"B_tail_components":bd,"phase_exterior_tail":pd,
            "I":enc(I),"W":enc(W),"M":enc(M),"selected_min":enc(selected),
            "strictly_below_moment":strict,"definitive_minimum":definitive,
            "inside_zero_crossing_panels":crossings,"panel_contribution_sha256":fingerprint.hexdigest(),
            "seconds":time.monotonic()-start,
            "overpayment":"I core +/-whole B mode bound and exterior +whole B mode bound; W core whole B mode and original-form exterior whole phi mode each over full half-line; endpoint paid separately."}
        s["record"]["panel_acquisitions"].append(item)
        s["envelopes"][j]={"M":M,"I":I,"W":W,"U":selected,"panels":count}
        self.save();print("panels",s["bits"],j,count,"strict",strict,"seconds",round(item["seconds"],3),flush=True)

    def MG(self,h,rho,envelopes):
        b,h1=h[2],h[1];u3,u4=envelopes;z=A(rho)
        e0=(z**3/6+z*z)*u3+z*z*u4/2
        e1=(z+z*z/2)*u3
        return 2*self.absolute(b)*e0+(self.absolute(h1)+z*self.absolute(b))*e1

    def tail_factor(self,r,N,outer):
        q=A(r)/A(outer)
        return q**(N+1)*((N+2)-(N+1)*q)/(1-q)**2

    def case(self,s,r,N,rule,outer,U):
        h=s["h"];b,h1=h[2],h[1];rr=A(r)
        def q(m,n):
            if (m,n) in {(0,0),(0,1),(0,2),(1,0)}:return arb(0)
            return (-1)**m*h[2*m+n]/(math.factorial(m)*math.factorial(n))
        finite=arb(0)
        for k in range(1,N+1):
            for m in range(k+1):
                n=k-m
                g=b*(n-2)*q(m,n)+h1*(n+1)*q(m,n+1)
                finite+=self.absolute(g)*rr**k
        D=self.absolute(self.square(h1)-2*b*h[0]);payment=2*self.square(b)*rr
        mg=self.MG(h,outer,U);factor=self.tail_factor(r,N,outer);tail=mg*factor
        gamma=finite+tail;d=D-payment-gamma
        normalizer=1+self.square(h[0])+self.square(h1)+self.square(b);c=d/normalizer
        K=(4*self.square(b)+self.square(self.absolute(h1)+rr*self.absolute(b))).sqrt()
        mu=d/K if d>0 else arb(0)
        e0=(rr**3/6+rr*rr)*U[0]+rr*rr*U[1]/2
        e1=(rr+rr*rr/2)*U[0]
        scalarH=self.absolute(h[0])-rr*self.absolute(h1)-self.absolute(b)*(rr+rr*rr/2)-e0
        scalarHA=self.absolute(h1)-rr*self.absolute(b)-e1
        values={"D":D,"time":payment,"finite_sum":finite,"M_G":mg,"tail_factor":factor,
                "tail":tail,"Gamma":gamma,"d":d,"c":c,"K":K,"mu":mu,
                "scalar_H_floor":scalarH,"scalar_HA_floor":scalarHA}
        saved={"r":str(r),"N":N,"rule":rule,"outer":str(outer),
               **{k:rec(v) for k,v in values.items()},"status":status(d)}
        return saved,values

    def compare(self,s,label):
        ctx.prec=s["bits"];allrows=[];s["cases"]={}
        Uc=[s["envelopes"][j]["U"] for j in (3,4)]
        for r in RADII:
            for N in DEGREES:
                for rule,outer,U in (("A",2*r,s["moments"][2*r]),("B",R,s["moments"][R]),("C",R,Uc)):
                    row,values=self.case(s,r,N,rule,outer,U)
                    allrows.append(row);s["cases"][r,N,rule]=values
        h=s["h"];b,h1=h[2],h[1];z=A(R)
        alpha3=2*self.absolute(b)*(z**3/6+z*z)+(self.absolute(h1)+z*self.absolute(b))*(z+z*z/2)
        alpha4=self.absolute(b)*z*z
        gaps=[(s["moments"][R][i]-Uc[i]).nonnegative_part() for i in (0,1)]
        mg_gap=alpha3*gaps[0]+alpha4*gaps[1]
        differences=[{"r":str(r),"N":N,"Gamma_B_minus_C":rec(mg_gap*self.tail_factor(r,N,R)),
                      "strict":mg_gap*self.tail_factor(r,N,R)>0,"exact_nonworsening_by_definition":True}
                     for r in RADII for N in DEGREES]
        minima=[]
        for r in RADII:
            row={"r":str(r)}
            for rule in ("A","B","C"):
                passing=[N for N in DEGREES if s["cases"][r,N,rule]["d"]>0]
                first=min(passing) if passing else None
                row[rule]={"minimum_certified":first,
                    "lower_degrees_unresolved":[N for N in DEGREES if (first is None or N<first) and status(s["cases"][r,N,rule]["d"])=="unresolved"]}
            minima.append(row)
        s["record"]["passes"].append({"label":label,"rows":allrows,"differences":differences,"minimum_degrees":minima})
        s["final_rows"]=allrows;self.save()
        print("comparison",s["bits"],label,[(x["r"],x["C"]["minimum_certified"]) for x in minima],flush=True)

    def refinement_needed(self,s):
        affected=set()
        for j,e in s["envelopes"].items():
            M,I,W=e["M"],e["I"],e["W"]
            decided=(I.upper()<M.lower() or W.upper()<M.lower() or
                     (I.lower()>=M.upper() and W.lower()>=M.upper()))
            if not decided:affected.add(j)
        if any(status(s["cases"][r,N,"C"]["d"])=="unresolved" for r in RADII for N in DEGREES):
            affected.update(j for j,e in s["envelopes"].items() if min(e["I"].lower(),e["W"].lower())<e["M"].upper())
        return affected

    def sharp_radius(self,s,U):
        h=s["h"];D=self.absolute(self.square(h[1])-2*h[2]*h[0])
        if not D>0:return None
        L0=2*self.square(h[2])+self.absolute(h[1]*h[3]);M=self.MG(h,R,U)
        if M==0 and L0==0:return A(min(R/2,TAU/2))
        denominator=L0+(self.square(L0)+16*M*D/A(R)**2).sqrt()
        check(denominator>0,"sharp radius denominator")
        return interval_min([A(R/2),A(TAU/2),D/denominator])

    def confirm(self):
        a,b=self.stages
        shared=[]
        for rho in a["moments"]:
            shared+=list(zip(a["moments"][rho],b["moments"][rho]))
        shared+=list(zip(a["h"],b["h"]))
        for x,y in shared:check(x.overlaps(y),"disjoint analytic input precisions")
        for j in (3,4):
            for key in ("M","I","W","U"):
                check(a["envelopes"][j][key].overlaps(b["envelopes"][j][key]),"disjoint envelope precisions")
        for key in a["cases"]:
            for item in ("d","c","Gamma"):
                check(a["cases"][key][item].overlaps(b["cases"][key][item]),"disjoint case precisions")
        self.data["confirmation"]="all shared analytic inputs, selected envelopes and 36 case margins overlap"

    def derived(self):
        out=[]
        for s in self.stages:
            ctx.prec=s["bits"];Ub=s["moments"][R];Uc=[s["envelopes"][j]["U"] for j in (3,4)]
            rb,rc=self.sharp_radius(s,Ub),self.sharp_radius(s,Uc)
            s["radii"]=(rb,rc)
            out.append({"bits":s["bits"],"B":enc(rb) if rb is not None else None,
                        "C":enc(rc) if rc is not None else None,
                        "strict_C_greater_B":rc.lower()>rb.upper() if rb is not None and rc is not None else False})
        a,b=self.stages
        for i in (0,1):
            if a["radii"][i] is not None:
                check(a["radii"][i].overlaps(b["radii"][i]),"disjoint sharp-radius precisions")
        self.data["sharp_radius"]=out
        s=b;ctx.prec=384
        if s["radii"][1] is None:return
        lower=s["radii"][1].lower()
        check(lower>0,"derived radius lower not positive")
        mant,exponent=lower.man_exp()
        k=int(mant).bit_length()-1+int(exponent)
        rr=F(2**k) if k>=0 else F(1,2**(-k))
        check(A(rr)<=lower,"dyadic downward rounding")
        row,values=self.case(s,rr,1,"C-derived",R,[s["envelopes"][j]["U"] for j in (3,4)])
        check(values["d"]>0,"derived degree-one margin unresolved")
        guarantee=values["d"]-values["D"]/2
        check(guarantee>=0,"derived d1>=D/2 not verified by outward algebra")
        self.data["derived_ball"]={"radius":str(rr),"power_of_two":k,
            "rounding":"largest power-of-two radius no greater than C's confirmed positive lower endpoint; the endpoint itself is also retained above",
            "case":row,"d_minus_D_over_2":rec(guarantee)}
        self.derived_values=(rr,values)

    def representative(self):
        s=self.stages[1];ctx.prec=384;choice=None
        for r in RADII:
            passing=[N for N in DEGREES if s["cases"][r,N,"C"]["d"]>0]
            if passing:choice=(r,min(passing),s["cases"][r,min(passing),"C"]);break
        if choice is None and hasattr(self,"derived_values"):
            r,v=self.derived_values;choice=(r,1,v)
        if choice is None:
            self.data["representative"]=None;return
        r,N,v=choice
        # Require a matching positive first-stage fixed case, or two-stage
        # radius confirmation for the single formula-derived case.
        if r in RADII:check(self.stages[0]["cases"][r,N,"C"]["d"]>0,"representative lost first-stage positivity")
        c,mu=v["c"],v["mu"];cl,ml=c.lower(),mu.lower()
        check(cl>0 and ml>0,"representative positive coefficient/floor")
        Uc=[s["envelopes"][j]["U"] for j in (3,4)]
        B2=self.absolute(s["h"][2])+A(r)*(Uc[0]+Uc[1])
        C=(1+B2.upper()/ml).upper();Cint=int(C.ceil().fmpz())
        L=sum((self.integral(s,j,F(17,64)) for j in (0,1)),arb(0))
        R2=sum((self.integral(s,j,F(17,64),F(4)) for j in (0,1)),arb(0))
        Nbar=max((R2.upper()+6*L.upper()).upper(),(3*L.upper()/cl).upper())
        ratio=ml/(2*Nbar);delta=3*ml*ml/(16*arb.pi())*ratio*ratio.sqrt()
        check(delta>0,"representative energy floor")
        self.data["representative"]={"r":str(r),"N":N,"exact_defined_coefficient":True,
            "c":enc(c),"mu":enc(mu),"B2":enc(B2),"C01_upper":rec(C),"C01_integer":Cint,
            "C01_start":"eventual only; accepted compact-uniform derivative convergence at spatial c=1",
            "L":enc(L),"R2":enc(R2),"Nbar_upper":rec(Nbar),"delta_lower":rec(delta.lower()),
            "all_time_start":0,"direct_floor_same_information":rec(ml)}

    def run(self):
        for bits in (256,384):
            s=self.new_stage(bits)
            for j in (3,4):self.panels(s,j,1024)
            self.compare(s,"1024 panels")
        affected=set().union(*(self.refinement_needed(s) for s in self.stages))
        if affected:
            self.data["refinement"]={"affected_j":sorted(affected),"reason":"unresolved IBP-versus-moment comparison or C margin at 1024 panels","one_refinement_only":True}
            for s in self.stages:
                ctx.prec=s["bits"]
                for j in sorted(affected):self.panels(s,j,2048)
                self.compare(s,"permitted 2048-panel refinement")
        self.confirm();self.derived();self.representative()
        self.data["terminal_status"]="completed_fixed_comparison"
        self.save()


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True);args=parser.parse_args()
    check(not args.output.exists(),"preserve old execution evidence")
    run=None
    def timeout(signum,frame):raise TimeoutError("20-minute acquisition cap")
    try:
        run=Run(args.repo.resolve(),args.output)
        signal.signal(signal.SIGALRM,timeout)
        signal.setitimer(signal.ITIMER_REAL,max(0.001,run.deadline-time.monotonic()))
        run.run()
    except Exception as exc:
        if run is None:raise
        run.data["terminal_status"]="resource_cap" if isinstance(exc,TimeoutError) else "implementation_or_integrity_stop"
        run.data["error"]={"type":type(exc).__name__,"message":str(exc)};run.save()
        raise
    finally:signal.setitimer(signal.ITIMER_REAL,0)
    print("TERMINAL",run.data["terminal_status"],run.data["cost"],flush=True)


if __name__=="__main__":main()
