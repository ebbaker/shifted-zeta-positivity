#!/usr/bin/env python3
"""Frozen HFCE-01 one-cell direct baseline; no source quadrature.

Prepared for Edward Baker, 20 October 2026, with substantial LLM
assistance. Model gpt-6-astra, actual effort ultra, verified by parent
execution metadata. Delegated same-model internal computation.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, platform, signal, sys, time
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode = True
from flint import arb, ctx
import flint

REL=Path("papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision")
ACR=Path("papers/investigations-3/11_arithmetic_collision_rigidity")
T0,T1,X0,X1=F(109999,10**6),F(110001,10**6),F(4005,4),F(2003,2)
TC,XC,S=F(21,200),F(1000),F(1,10**6)
def check(b,s):
    if not b: raise ArithmeticError(s)
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def A(q): return arb(q.numerator)/q.denominator if isinstance(q,F) else arb(q)
def box(a,b): return arb(A((a+b)/2),A((b-a)/2))
def poly(cs,x):
    r=cs[-1]
    for c in reversed(cs[:-1]):r=r*x+c
    return r
def square(v):
    lo=(v.abs_lower()**2).lower(); hi=(v.abs_upper()**2).upper()
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def dyadic(v):
    check(v.is_finite() and v.is_exact(),"exact finite dyadic required")
    m,e=v.man_exp()
    return {"mantissa":str(m),"exponent":int(e)}
def rec(v):
    check(v.is_finite(),"nonfinite interval")
    return {"display":v.str(50,more=True),"lower_dyadic":dyadic(v.lower()),"upper_dyadic":dyadic(v.upper())}
def bernstein_1d(cs,left,right):
    n=len(cs)-1; aa=A(left); ww=A(right-left)
    shifted=[ww**i*sum((cs[j]*math.comb(j,i)*aa**(j-i) for j in range(i,n+1)),arb(0)) for i in range(n+1)]
    return [sum((shifted[i]*math.comb(k,i)/math.comb(n,i) for i in range(k+1)),arb(0)) for k in range(n+1)]
def bernstein_2d(cs):
    nx,nt=len(cs),len(cs[0])
    cols=[bernstein_1d([cs[l][k] for l in range(nx)],X0-XC,X1-XC) for k in range(nt)]
    grid=[bernstein_1d([cols[k][l] for k in range(nt)],T0-TC,T1-TC) for l in range(nx)]
    lo=min(v.lower() for row in grid for v in row);hi=max(v.upper() for row in grid for v in row)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def polynomial_energy(c0,c1):
    out=[[arb(0) for k in range(25)] for l in range(49)]
    for cs,weight in [(c0,arb(1)),(c1,A(S))]:
        for l in range(25):
            for k in range(13):
                for p in range(25):
                    for q in range(13):
                        out[l+p][k+q]+=weight*cs[l][k]*cs[p][q]
    return out
def execute(module,setup,ext,bits):
    start=time.monotonic();ctx.prec=bits
    cache=setup["setup"]
    moments=[module.undyadic(r["midpoint_dyadic"]) for r in cache["midpoint_jets"]]
    radii=[module.undyadic(r["quadrature_radius_dyadic"]) for r in cache["midpoint_jets"]]
    check(len(moments)==51 and all(r>=0 for r in radii),"invalid complete cache")
    M=module.undyadic(cache["common_moment_dyadic"]);check(M>0,"invalid majorant")
    modes,sources,tail_record=ext.tail_bounds(bits)
    check(F(1,100)<=T0<=T1<=F(1,5) and F(999)<=XC<=X0<=X1<=1002,"unsupported full domain")
    R=A(X1-XC);Delta=A(max(abs(T0-TC),abs(T1-TC)))
    fact=[math.factorial(j) for j in range(53)]
    rem=(M*(R**25/fact[25]+R.exp()*Delta**13/fact[13])).upper()
    dt,dx=box(T0,T1)-A(TC),box(X0,X1)-A(XC)
    images=[];values=[];errors=[];coeffs=[];payments=[]
    for j in range(2):
        cs=[[(-1)**k*moments[j+l+2*k]/(fact[l]*fact[k]) for k in range(13)] for l in range(25)]
        image=poly([poly(row,dt) for row in cs],dx)
        quad=sum((R**l*Delta**k*radii[j+l+2*k]/(fact[l]*fact[k]) for l in range(25) for k in range(13)),arb(0)).upper()
        error=(rem+quad+modes[j]+sources[j]).upper()
        check(error<arb("1e-6"),"complete component error budget exceeded")
        coeffs.append(cs);images.append(image);errors.append(error);values.append(image+arb(0,error))
        payments.append({k:rec(v) for k,v in dict(quadrature=quad,taylor=rem,mode=modes[j],source=sources[j],total=error).items()})
    # Retain the original Horner result, then apply the strongest available
    # same-data component bounds on this unchanged parameter cell.
    horner_values=list(values)
    original_coordinate_F=square(values[0])+A(S)*square(values[1])
    original_coord_seconds=time.monotonic()-start
    component_Bernstein=[bernstein_2d(cs) for cs in coeffs]
    intersected_images=[images[j].intersection(component_Bernstein[j]) for j in (0,1)]
    values=[intersected_images[j]+arb(0,errors[j]) for j in (0,1)]
    product_maxima=[min(images[j].abs_upper(),component_Bernstein[j].abs_upper(),intersected_images[j].abs_upper()) for j in (0,1)]
    coordinate_F=square(values[0])+A(S)*square(values[1])
    coordinate_scalar_lower=(values[0].abs_lower()**2+A(S)*values[1].abs_lower()**2).lower()
    coord_seconds=time.monotonic()-start
    correlated_start=time.monotonic()
    epoly=polynomial_energy(*coeffs)
    eb=bernstein_2d(epoly)
    original_errF=(2*images[0].abs_upper()*errors[0]+errors[0]**2+
          A(S)*(2*images[1].abs_upper()*errors[1]+errors[1]**2)).upper()
    original_correlated_F=eb+arb(0,original_errF)
    errF=(2*product_maxima[0]*errors[0]+errors[0]**2+
          A(S)*(2*product_maxima[1]*errors[1]+errors[1]**2)).upper()
    correlated_F=eb+arb(0,errF)
    correlated_scalar_lower=(eb.lower()-errF).lower()
    # This exact-endpoint scalar bound avoids unnecessary loss from the
    # compact outward radius of a constructed symmetric interval.
    rounding_lower=max(arb(0),(eb.lower()-errF-correlated_F.lower()).upper())
    rounding_upper=max(arb(0),(correlated_F.upper()-eb.upper()-errF).upper())
    L=max(arb(0),coordinate_F.lower(),coordinate_scalar_lower,
          correlated_F.lower(),correlated_scalar_lower)
    margin=max(v.abs_lower() for v in values)
    check(margin>arb("1e-6") and L>arb("1e-12"),"strict baseline did not exclude")
    correlated_seconds=time.monotonic()-correlated_start
    control_start=time.monotonic()
    # Own exact polynomial event, no theta normalization or source errors.
    y=box(X0,X1)-A(F(8011,8));tau=box(T0,T1)-A(F(11,100))
    hc=square(y)-2*tau;hxc=2*y
    control_F=square(hc)+A(S)*square(hxc)
    check(hc.contains(0) and hxc.contains(0) and control_F.contains(0),"true event must remain possible")
    check(not bool(max(hc.abs_lower(),hxc.abs_lower())>arb("1e-6")),"false control exclusion")
    # The SAME correlated polynomial consumer must also refuse this genuine
    # interior event. Variables are dx=x-1000, dt=t-.105.
    cc0=[[arb(0) for _ in range(13)] for _ in range(25)]
    cc1=[[arb(0) for _ in range(13)] for _ in range(25)]
    cc0[0][0]=A(F(121,64)+F(1,100));cc0[1][0]=-A(F(11,4))
    cc0[2][0]=arb(1);cc0[0][1]=arb(-2)
    cc1[0][0]=-A(F(11,4));cc1[1][0]=arb(2)
    correlated_control_F=bernstein_2d(polynomial_energy(cc0,cc1))
    check(correlated_control_F.contains(0),"correlated consumer falsely excludes interior polynomial event")
    check(not bool(correlated_control_F.lower()>0),"strict correlated event exclusion must fail")
    # Updated component-Bernstein/intersection branch uses this same own
    # exact data, zero source error, and the true interior event.
    control_component_Bernstein=[bernstein_2d(cc0),bernstein_2d(cc1)]
    control_intersection=[hc.intersection(control_component_Bernstein[0]),
                          hxc.intersection(control_component_Bernstein[1])]
    control_scalar_lower=(control_intersection[0].abs_lower()**2+
                          A(S)*control_intersection[1].abs_lower()**2).lower()
    check(not bool(control_scalar_lower>0),"component-Bernstein branch falsely excludes event")
    return dict(bits=bits,source_acquisition_bits=setup["actual_precision_bits"],
        physical_H_over_Gstar=rec(values[0]),physical_Hx_over_Gstar=rec(values[1]),
        polynomial_images=[rec(v) for v in images],component_payments=payments,
        component_Bernstein_images=[rec(v) for v in component_Bernstein],
        intersected_component_images=[rec(v) for v in intersected_images],
        product_component_absolute_maxima=[rec(v) for v in product_maxima],
        original_Horner_physical_components=[rec(v) for v in horner_values],
        original_Horner_coordinate_F=rec(original_coordinate_F),
        original_Horner_energy_product_error=rec(original_errF),
        original_Horner_correlated_physical_F=rec(original_correlated_F),
        coordinate_square_F=rec(coordinate_F),coordinate_scalar_lower_F=rec(coordinate_scalar_lower),
        correlated_Bernstein_polynomial_F=rec(eb),
        correlated_energy_product_error=rec(errF),correlated_physical_F=rec(correlated_F),
        correlated_scalar_lower_F=rec(correlated_scalar_lower),
        additional_interval_rounding_allowance=dict(lower=rec(rounding_lower),upper=rec(rounding_upper),
            scope="Widening of the constructed correlated symmetric ball beyond polynomial endpoints plus product payment; scalar lower endpoint retained separately"),
        strongest_complete_lower_F=rec(L),strict_coordinate_margin=rec(margin),
        selected_F_consumer="correlated Bernstein scalar endpoint with component-Bernstein product bounds" if correlated_scalar_lower>=coordinate_scalar_lower else "component Bernstein coordinate squares",
        tail_admissibility=tail_record,
        control=dict(field="Hc=(x-1001.375)^2-2(t-.11)",H=rec(hc),Hx=rec(hxc),
                     F=rec(control_F),correlated_Bernstein_F=rec(correlated_control_F),
                     own_source_error=0,true_event_exclusion_refused=True,
                     same_correlated_consumer_event_exclusion_refused=True,
                     component_Bernstein_intersections=[rec(v) for v in control_intersection],
                     component_Bernstein_scalar_lower_F=rec(control_scalar_lower),
                     same_component_Bernstein_branch_event_exclusion_refused=True),
        original_Horner_coordinate_consumer_seconds=original_coord_seconds,
        coordinate_consumer_seconds=coord_seconds,correlated_consumer_seconds=correlated_seconds,
        own_control_seconds=time.monotonic()-control_start,
        total_seconds=time.monotonic()-start,new_source_quadratures=0,new_majorant_quadratures=0,status="pass")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--contract",type=Path,required=True)
    ap.add_argument("--output",type=Path,default=Path("/private/tmp/hfce_baseline_receipt.json"));args=ap.parse_args()
    started=time.monotonic()
    check(args.contract.is_file(),"frozen contract must precede execution")
    def stop(sig,frame):raise TimeoutError("300 second whole-run limit")
    signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,300)
    ep=args.repo/REL/"numerics/check_bounded_first_jet_extension.py"
    spec=importlib.util.spec_from_file_location("hfce_extension",ep);ext=importlib.util.module_from_spec(spec);spec.loader.exec_module(ext)
    module,setup,pins=ext.pin_sources(args.repo)
    cover=args.repo/ACR/"numerics/analytic_continuation/GLOBAL_ANALYTIC_CONTINUATION_LEDGER_20261018.json"
    earlier=args.repo/REL/"numerics/BOUNDED_THETA_EVENT_GATE_20261020.json"
    report=dict(date="2026-10-20",timezone="America/New_York",prepared_for="Edward Baker",
        llm_assistance="substantial; delegated same-model audit; parent verified actual model/effort",
        model="gpt-6-astra",reasoning_effort="ultra",
        python=platform.python_version(),python_executable=sys.executable,python_flint=flint.__version__,
        wrapper_sha256=digest(__file__),contract_sha256=digest(args.contract),
        source_pins=pins,extension_wrapper_sha256=digest(ep),
        coverage_input_pins=[dict(path=str(p.relative_to(args.repo)),sha256=digest(p)) for p in [cover,earlier]],
        domain=dict(time=[str(T0),str(T1)],space=[str(X0),str(X1)]),fixed_s=str(S),
        normalization="fixed Gstar=1000^(7/4)exp(-125*pi), never differentiated",
        historical_acquisition=dict(precision_bits=setup["actual_precision_bits"],seconds=setup["setup"]["seconds"],
                                    callbacks=setup["setup"]["callbacks"],charged_separately=True),
        source_acquisition_count=0,scan=False,adaptive_subdivision=False,
        inherited_current_outer_onset="exp(2000)",
        baseline_polynomial_method="Tensor Bernstein convex-hull enclosure of P0^2+sP1^2 on the exact same cell; component Bernstein/Horner intersections tighten coordinate bounds and product maxima; original Horner results retained; exact outward scalar endpoint retained alongside the constructed correlated interval",
        scope="All common-zero multiplicities excluded only on declared B; no later-event, negative winding or global claim")
    report["replays"]=[execute(module,setup,ext,bits) for bits in (192,256)]
    report["primary_attempt_decision"]="stop: existing complete source cache already yields strict direct baseline exclusion; any cap run is the separately predeclared cost comparison"
    report["status"]="pass"
    report["elapsed_seconds"]=time.monotonic()-started
    signal.setitimer(signal.ITIMER_REAL,0)
    args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["status","elapsed_seconds","historical_acquisition","primary_attempt_decision"]},indent=2))
    for r in report["replays"]:
        print(json.dumps({k:r[k] for k in ["bits","physical_H_over_Gstar","physical_Hx_over_Gstar","strongest_complete_lower_F","selected_F_consumer","total_seconds"]},indent=2))
if __name__=="__main__":main()
