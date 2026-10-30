#!/usr/bin/env python3
"""Frozen FCG-E01 R1 complete-source correlated-jet acquisition.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual recorded execution model gpt-6.1-sol, effort ultra, chat0047.
Requires the already installed python-flint/Arb stack; no package changes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import math
from pathlib import Path
import platform
import re
import signal
import sys
import time

import flint
from flint import acb, arb, ctx

PACKET_REL = "papers/investigations-5/05_radial_theta_collision_geometry/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R1_CORRELATED_JET_COEFFICIENT_20261030.md"
PACKET_SHA = "72fe0d54ade96e5c10defc3028f4f7ce816f849d7942116307f5ac27fd849b91"
TAU, CENTER, RADIUS, BIG_RADIUS = F(1,4), F(882607,20000), F(1,64), F(1,32)


def A(x):
    return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rec(x):
    check(x.is_finite(), "nonfinite serialization")
    return x.str(65, more=True)


def binary(x):
    m,e = x.man_exp()
    return [str(m),int(e)]


def enclosed(x):
    return {"ball":rec(x), "lower":rec(x.lower()), "upper":rec(x.upper()),
            "mid_binary":binary(x.mid()), "rad_binary":binary(x.rad())}


def zero_to_upper(upper):
    """Nonnegative representable ball enclosing [0,upper], with power-two radius."""
    upper = upper.upper()
    check(upper >= 0, "negative nonnegative-range upper")
    if upper == 0:
        return arb(0)
    mant, exp = upper.man_exp()
    mant, exp = int(mant), int(exp)
    k = mant.bit_length() + exp
    if mant & (mant-1) == 0:
        k -= 1
    half = arb(2) ** (k-1)
    # python-flint adds a radius rounding unit even for dyadic inputs.
    # Clamp the known nonnegative interval with Arb's outward operation.
    result = arb(half, half).nonnegative_part()
    check(result.lower() == 0 and result.upper() >= upper,
          "nonnegative ball construction")
    return result


def absolute(x):
    if x >= 0:
        return x
    if x <= 0:
        return -x
    return zero_to_upper(x.abs_upper())


def square(x):
    check(x.is_finite(), "nonfinite square")
    if x >= 0:
        return x*x
    if x <= 0:
        return (-x)*(-x)
    return zero_to_upper(x.abs_upper()*x.abs_upper())


def positive_part(x):
    if x >= 0:
        return x
    if x <= 0:
        return arb(0)
    return zero_to_upper(x.upper())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def algebra_checks():
    """Exact rational polynomial identities, independent of acquired jets."""
    def add(p,q):
        out=dict(p)
        for ij,v in q.items():
            out[ij]=out.get(ij,F(0))+v
        return {ij:v for ij,v in out.items() if v}
    def mul(p,q):
        out={}
        for (m,n),v in p.items():
            for (k,l),w in q.items():
                ij=(m+k,n+l);out[ij]=out.get(ij,F(0))+v*w
        return {ij:v for ij,v in out.items() if v}
    def scale(p,c):
        return {ij:c*v for ij,v in p.items() if c*v}
    # Exact polynomial cancellation for arbitrary symbolic h0,h1,b reduces
    # to the shown coefficient products; use monomials in those variables.
    # A tiny five-variable ring (t,x,h0,h1,b) makes that identity symbolic.
    def smul(p,q):
        out={}
        for i,v in p.items():
            for j,w in q.items():
                ij=tuple(a+b for a,b in zip(i,j))
                out[ij]=out.get(ij,F(0))+v*w
        return {ij:v for ij,v in out.items() if v}
    one={(0,0,0,0,0):F(1)}
    t={(1,0,0,0,0):F(1)};x={(0,1,0,0,0):F(1)}
    h0={(0,0,1,0,0):F(1)};h1={(0,0,0,1,0):F(1)};b={(0,0,0,0,1):F(1)}
    P=add(add(h0,smul(h1,x)),smul(b,add(scale(smul(x,x),F(1,2)),scale(t,-1))))
    PA=add(h1,smul(b,x))
    lhs=add(smul(PA,PA),scale(smul(b,P),-2))
    rhs=add(add(smul(h1,h1),scale(smul(b,h0),-2)),scale(smul(smul(b,b),t),2))
    check(lhs==rhs,"polynomial identity (8)")
    # Coefficient rule checked against multiplication/differentiation of
    # an arbitrary finite polynomial R, with integer rational coefficients.
    rem={(m,n):F(3*m-2*n+7,math.factorial(m)*math.factorial(n))
         for m in range(5) for n in range(5)}
    rx={(m,n-1):n*v for (m,n),v in rem.items() if n}
    bb,hh=F(7,3),F(-5,2)
    direct=add(scale(rem,-2*bb),add(scale(rx,hh),mul({(0,1):bb},rx)))
    for m in range(4):
        for n in range(4):
            expected=bb*(n-2)*rem.get((m,n),0)+hh*(n+1)*rem.get((m,n+1),0)
            check(direct.get((m,n),0)==expected,"coefficient identity (16)")
    # Symbolic h_j products for the six low-order cases.
    def term(i,j,c=F(1)):
        return {tuple(sorted((i,j))):c} if c else {}
    def qfactor(m,n):
        if (m,n) in {(0,0),(0,1),(0,2),(1,0)}:return None
        return 2*m+n,F((-1)**m,math.factorial(m)*math.factorial(n))
    def low(m,n):
        out={}
        first=qfactor(m,n);second=qfactor(m,n+1)
        if first:out=add(out,term(2,first[0],F(n-2)*first[1]))
        if second:out=add(out,term(1,second[0],F(n+1)*second[1]))
        return out
    expected={(0,0):{},(0,1):{},(1,0):term(1,3,-1),(0,2):term(1,3,F(1,2)),
              (1,1):add(term(2,3),term(1,4,-1)),
              (2,0):add(term(2,4,-1),term(1,5,F(1,2))),
              (0,3):add(term(2,3,F(1,6)),term(1,4,F(1,6)))}
    for ij,p in expected.items():check(low(*ij)==p,"low-order identity (17)")
    for N in (8,16,32):
        q=F(1,2)
        tail=q**(N+1)*((N+2)/(1-q)+q/(1-q)**2)
        check(tail==F(N+3,2**N),"geometric identity (19)")
    for z in (arb(0),arb(0,A(F(1,8))),arb(A(F(1,8)),A(F(1,8))),arb(-2),arb(3)):
        zz=square(z);check(zz.is_finite() and zz.lower()>=0,"square nonnegativity")
        check(zz.contains(z.mid()*z.mid()),"square contains midpoint square")
    return {"polynomial_identity_8":True,"coefficient_rule_16":True,
            "low_orders_17":True,"geometric_tail_19":True,
            "four_q_zeros_exact":True,"nonnegative_square_guards":True}


class Acquisition:
    def __init__(self, output, repo):
        self.output,self.repo=output,repo
        self.start=time.monotonic()
        self.deadline=self.start+1200
        self.data={"task":"FCG-E01 R1","date":"2026-10-30","prepared_for":"Edward Baker",
                   "llm_assistance":"Substantial; same-assistant numerical execution/self-check",
                   "model":"gpt-6.1-sol","effort":"ultra","chat":"0047",
                   "thread_id":"01a18d3a-0de3-7781-b7e1-79a42cf0a6fd",
                   "fixed_parameters":{"tau":"1/4","a":"882607/20000","r":"1/64","R":"1/32",
                                       "modes":8,"cutoff":1,"degrees":[8,16,32]},
                   "limits":{"acquisition_seconds":1200,"eval_limit":200000,"depth_limit":30},
                   "runtime":{"python":sys.version,"executable":sys.executable,
                              "python_flint":flint.__version__,
                              "flint":getattr(flint,"__FLINT_VERSION__","unavailable"),
                              "platform":platform.platform()},
                   "script_sha256":digest(Path(__file__)),
                   "packet":{"path":PACKET_REL,"sha256":PACKET_SHA},
                   "stages":[],"terminal_status":"in_progress","distinct_source_integrals":0}
        self.stages=[]
        packet=repo/PACKET_REL
        check(digest(packet)==PACKET_SHA,"frozen packet changed")
        inputs=re.findall(r"\| (papers/[^ |]+|result-summaries/[^ |]+) \| ([0-9a-f]{64}) \|",packet.read_text())
        check(len(inputs)==9,"frozen input count")
        self.data["inputs"]=[]
        for name,expected in inputs:
            actual=digest(repo/name);check(actual==expected,"frozen source changed: "+name)
            self.data["inputs"].append({"path":name,"sha256":actual,"matches":True})
        ctx.prec=256
        self.data["algebra_checks"]=algebra_checks()
        self.save()

    def cap(self):
        if time.monotonic()>=self.deadline:
            raise TimeoutError("20-minute acquisition cap")

    def save(self):
        self.data["elapsed_acquisition_seconds"]=time.monotonic()-self.start
        self.output.write_text(json.dumps(self.data,indent=2)+"\n")

    def tail(self,j,T,Y):
        pi=arb.pi();m=9;U=arb(1);T=A(T);Y=A(Y)
        beta=4*pi*m*m-9-Y
        ratio=(arb(m+1)/m)**4*(-pi*(2*m+1)).exp()
        time_guard=8*pi*m*m-T
        check(beta>0 and ratio<1 and time_guard>=0,"mode-tail guards A2/A3")
        mode=2*pi*pi*m**4*(-pi*m*m).exp()/(1-ratio)*math.factorial(j)/beta**(j+1)
        source=[];denoms=[];concavity=[]
        for n in range(1,9):
            lam=pi*n*n;denom=4*lam*(4*U).exp()-(9+Y)-2*T*U-j/U
            concave=16*lam*(4*U).exp()-2*T
            check(denom>0 and concave>0,"source-tail guards A4")
            value=2*lam*lam*U**j*(T*U*U+(9+Y)*U-lam*(4*U).exp()).exp()/denom
            source.append(value.upper());denoms.append(rec(denom));concavity.append(rec(concave))
        return mode.upper(),sum(source,arb(0)).upper(),{
            "beta":rec(beta),"ratio":rec(ratio),"time_guard":rec(time_guard),
            "source_denominators":denoms,"source_concavity_guards":concavity,
            "retained_mode_source_tail_uppers":[rec(z) for z in source],"all_passed":True}

    def integral(self,stage,j,T,Y=F(0),signed=False):
        self.cap();start=time.monotonic();calls=0
        pi=arb.pi();aa=A(CENTER)
        def integrand(u,analytic):
            nonlocal calls
            calls+=1;self.cap()
            q=(4*u).exp();total=acb(0)
            for n in range(1,9):
                lam=pi*n*n
                total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
            result=(A(T)*u*u+(1+A(Y))*u).exp()*total*u**j
            if signed:
                phase=aa*u
                trig=(phase.cos,phase.sin,phase.cos,phase.sin)[j%4]()
                if j%4 in (1,2):trig=-trig
                result*=trig
            return result
        value=acb.integral(integrand,0,1,abs_tol=stage["abs_tol"],rel_tol=stage["rel_tol"],
                           eval_limit=200000,depth_limit=30)
        check(value.is_finite(),"nonfinite quadrature")
        check(value.imag.contains(0),"real integral has nonreal enclosure")
        finite=value.real
        mode,source,guards=self.tail(j,T,Y)
        error=(mode+source).upper()
        complete=finite+arb(0,error) if signed else finite+zero_to_upper(error)
        check(complete.is_finite(),"nonfinite complete source integral")
        if not signed:check(complete>0,"positive moment not enclosed positively")
        item={"kind":"center_jet" if signed else "positive_moment","order":j,
              "T":str(T),"Y":str(Y),"finite_integral":enclosed(finite),
              "quadrature_radius_upper":rec(finite.rad().upper()),
              "omitted_mode_error_upper":rec(mode),"retained_source_error_upper":rec(source),
              "complete":enclosed(complete),"guards":guards,"callbacks":calls,
              "elapsed_seconds":time.monotonic()-start}
        stage["record"]["integrals"].append(item)
        self.data["distinct_source_integrals"]+=1
        self.save()
        print("integral",stage["bits"],"jet" if signed else "moment",j,str(T),str(Y),
              "callbacks",calls,"seconds",round(item["elapsed_seconds"],3),flush=True)
        return complete

    def stage(self,bits):
        ctx.prec=bits
        at,rt=(160,128) if bits==256 else (224,192)
        record={"bits":bits,"absolute_tolerance":"2^-"+str(at),
                "relative_tolerance":"2^-"+str(rt),"integrals":[],"degrees":[]}
        stage={"bits":bits,"abs_tol":arb(2)**(-at),"rel_tol":arb(2)**(-rt),
               "jets":[],"moments":[],"record":record,"results":{}}
        self.data["stages"].append(record);self.stages.append(stage)
        for j in (3,4):
            stage["moments"].append(self.integral(stage,j,F(9,32),F(1,32)))
        return stage

    def jets_to(self,stage,maximum):
        while len(stage["jets"])<=maximum:
            stage["jets"].append(self.integral(stage,len(stage["jets"]),TAU,signed=True))

    def degree(self,stage,N):
        self.cap();h=stage["jets"];b=h[2];h1=h[1];r=A(RADIUS);R=A(BIG_RADIUS)
        M3,M4=stage["moments"]
        def e0(z):return (z**3/6+z*z)*M3+z*z*M4/2
        def e1(z):return (z+z*z/2)*M3
        D0=square(h1)-2*b*h[0]
        paidtime=2*square(b)*r
        MG=2*absolute(b)*e0(R)+(absolute(h1)+R*absolute(b))*e1(R)
        def q(m,n):
            if (m,n) in {(0,0),(0,1),(0,2),(1,0)}:return arb(0)
            return (-1)**m*h[2*m+n]/(math.factorial(m)*math.factorial(n))
        finite=arb(0);coeff=[]
        for k in range(1,N+1):
            for m in range(k+1):
                n=k-m
                g=b*(n-2)*q(m,n)+h1*(n+1)*q(m,n+1)
                weighted=absolute(g)*r**k
                finite+=weighted
                coeff.append({"m":m,"n":n,"g":rec(g),"weighted_absolute":rec(weighted)})
        tail=MG*F(N+3,2**N).numerator/F(N+3,2**N).denominator
        gamma=finite+tail;d=absolute(D0)-paidtime-gamma
        normalizer=1+square(h[0])+square(h1)+square(b);c=d/normalizer
        K=(4*square(b)+square(absolute(h1)+r*absolute(b))).sqrt()
        sep=2*absolute(b)*e0(r)+(absolute(h1)+r*absolute(b))*e1(r)
        sep_d=absolute(D0)-paidtime-sep
        sign="positive" if d>0 else ("nonpositive" if d<=0 else "unresolved")
        mu=d/K if d>0 else arb(0)
        wcenter=(4*square(b)+square(h1)).sqrt()
        centerstrip=positive_part(absolute(D0)-gamma)/wcenter if wcenter>0 else arb(0)
        result={"N":N,"D0":enclosed(D0),"time_allowance":enclosed(paidtime),
                "finite_coefficient_sum":enclosed(finite),"M_G":enclosed(MG),
                "cauchy_tail":enclosed(tail),"Gamma_N":enclosed(gamma),
                "d":enclosed(d),"normalizer":enclosed(normalizer),"c":enclosed(c),
                "Gamma_sep":enclosed(sep),"separate_margin":enclosed(sep_d),
                "K_B":enclosed(K),"direct_uniform_floor":enclosed(mu),
                "direct_center_strip_distance":enclosed(centerstrip),
                "direct_formula":"(|D0+2*b^2*t|-Gamma_N)_+/sqrt(4*b^2+(h1+b*x)^2), w!=0; 0 if w=0",
                "coefficients":coeff,"sign":sign}
        stage["record"]["degrees"].append(result)
        stage["results"][N]={"d":d,"c":c,"mu":mu,"K":K,"gamma":gamma}
        self.save()
        print("DEGREE",stage["bits"],N,sign,"d",rec(d),"Gamma",rec(gamma),flush=True)
        return result

    def consistent(self,first,second,degree):
        for i in range(2):check(first["moments"][i].overlaps(second["moments"][i]),"disjoint positive moments")
        for j in range(2*degree+2):
            check(first["jets"][j].overlaps(second["jets"][j]),"disjoint complete jet "+str(j))
        for N in set(first["results"]) & set(second["results"]):
            for key in ("d","c","gamma"):
                check(first["results"][N][key].overlaps(second["results"][N][key]),
                      "disjoint derived enclosures "+str(N)+" "+key)
        self.data["precision_consistency"]="all shared complete inputs and degree margins overlap"

    def positive_constants(self,stage,N):
        T=F(17,64)
        L=sum((self.integral(stage,j,T) for j in (0,1)),arb(0))
        R2=sum((self.integral(stage,j,T,F(4)) for j in (0,1)),arb(0))
        data=stage["results"][N];c,mu=data["c"],data["mu"]
        cl,ml=c.lower(),mu.lower()
        check(cl>0 and ml>0,"confirmed lower c/mu not positive")
        first=R2.upper()+6*L.upper();second=3*L.upper()/cl
        Nupper=max(first.upper(),second.upper())
        ratio=ml/(2*Nupper)
        delta=3*ml*ml/(16*arb.pi())*ratio*ratio.sqrt()
        M3,M4=stage["moments"];B2=absolute(stage["jets"][2])+A(RADIUS)*(M3+M4)
        C=(1+B2.upper()/ml).upper()
        check(delta>0,"positive spatial energy lower bound")
        self.data["positive_consequence"]={
            "N":N,"uses_exact_source_defined_c":True,"c":enclosed(c),
            "c_lower":rec(cl),"mu":enclosed(mu),"mu_lower":rec(ml),
            "L":enclosed(L),"R2":enclosed(R2),"L_upper":rec(L.upper()),
            "R2_upper":rec(R2.upper()),"Nbar_upper":rec(Nupper),
            "delta_lower":rec(delta.lower()),"B2":enclosed(B2),
            "C01_coefficient_upper":rec(C),"C01_integer_coefficient":str(C.ceil()),
            "all_time_start":0,
            "C01_start":"eventual only, from accepted compact-uniform derivative convergence",
            "same_information_direct_uniform_floor":rec(ml)}
        self.save()

    def run(self):
        first=self.stage(256);selected=None
        for N in (8,16,32):
            self.jets_to(first,2*N+1)
            if self.degree(first,N)["sign"]=="positive":
                selected=N;break
        second=self.stage(384)
        if selected is not None:
            self.jets_to(second,2*selected+1)
            result=self.degree(second,selected)
            self.consistent(first,second,selected)
            check(result["sign"]=="positive","positive confirmation lost")
        else:
            self.jets_to(second,65)
            for N in (8,16,32):
                result=self.degree(second,N)
                if result["sign"]=="positive":
                    selected=N;break
            self.consistent(first,second,32)
        if selected is not None:
            self.data["coefficient_sign_status"]="confirmed_positive"
            self.positive_constants(second,selected)
            self.data["terminal_status"]="confirmed_positive_complete"
            self.data["selected_degree"]=selected
        else:
            signs=[r["sign"] for r in second["record"]["degrees"]]
            self.data["terminal_status"]="all_exact_candidates_nonpositive" if all(x=="nonpositive" for x in signs) else "final_enclosures_unresolved"
        self.save()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,default=Path(__file__).resolve().parents[5])
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise FileExistsError("preserve prior execution evidence; choose an unused output")
    task=None
    def alarm(signum,frame):
        raise TimeoutError("20-minute acquisition cap")
    try:
        task=Acquisition(args.output,args.repo.resolve())
        signal.signal(signal.SIGALRM,alarm)
        signal.setitimer(signal.ITIMER_REAL,max(0.001,task.deadline-time.monotonic()))
        task.run()
    except Exception as exc:
        if task is None:
            raise
        task.data["terminal_status"]="resource_cap" if isinstance(exc,TimeoutError) else "implementation_or_integrity_stop"
        task.data["error"]={"type":type(exc).__name__,"message":str(exc)}
        task.save()
        print("STOP",task.data["terminal_status"],str(exc),flush=True)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
    print("TERMINAL",task.data["terminal_status"],"integrals",task.data["distinct_source_integrals"],
          "seconds",round(task.data["elapsed_acquisition_seconds"],3),flush=True)


if __name__=="__main__":
    main()
