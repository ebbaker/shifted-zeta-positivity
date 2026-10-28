#!/usr/bin/env python3
"""CTF-E01 R1: bounded central heat measurements, 28 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Actual recorded model gpt-6.1-sol, effort ultra, investigation05 chat0009.
Requires mpmath. All numerical results are floating diagnostics, not intervals.
Run once; the global budget includes both precisions and any refinement.
"""
import argparse
import datetime as dt
import hashlib
import json
import platform
import time
from pathlib import Path

import mpmath as mp

MODEL = {"model": "gpt-6.1-sol", "effort": "ultra"}
N, THETA_U, CONTROL_U = 6, 2, 6
PRECISIONS, S_VALUES = (30, 50), (1, 4, 16, 64, 256)
MAX_EVALS, MAX_SECONDS = 250000, 900
EXPECTED_NOTE25 = "321d557080ef06abb3e8a70f85872f1e10980881a91fc47806d54ab9b050e11b"


def decimal(x):
    return mp.nstr(x, 53)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class BudgetStop(Exception):
    pass


def tail_bounds(source, t, m, k):
    """Analytic upper-bound formulas; evaluated without directed rounding."""
    if source == "theta":
        q, b, U = mp.mpf(N + 1), 9 + 2 * m, mp.mpf(THETA_U)
        d = 4 * (mp.pi * q*q - t/8) - b
        ratio = (1 + 1/q)**4 * mp.exp(-mp.pi*(2*q+1))
        index = 2*mp.pi**2*q**4*mp.exp(-mp.pi*q*q)*mp.factorial(k)/(d**(k+1)*(1-ratio))
        E, alpha = mp.exp(4*U), mp.pi-t/8
        lam, D = 4*alpha*E-b, 1-16*mp.exp(-3*mp.pi*E)
        common = 2*mp.pi**2*mp.exp(-t/8+b*U-alpha*E)/D
        outer = common/lam if k == 0 else common*(U/lam+1/lam**2)
        assert d > 0 and lam > 0 and D > 0 and ratio < 1
        return index, outer
    U = mp.mpf(CONTROL_U)
    def lam(p):
        return 8*U-2*m-p/U
    assert lam(k+4) > 0
    outer = mp.exp(-4*U*U+2*m*U)*(64*U**(k+4)/lam(k+4)+6*U**k/lam(k))
    return mp.mpf(0), outer


def control_reference(kind, a, k, m=0, collision=False):
    def G(b):
        L = mp.sqrt(mp.pi)/4*mp.exp(b*b/16)*mp.erfc(-b/4)
        if k == 0:
            return (b**4/64+3*b*b/4+9)*L+b**3/64+5*b/8
        return (b**5/512+5*b**3/32+21*b/8)*L+b**4/512+9*b*b/64+mp.mpf(7)/4
    if kind == "H":
        if collision:
            return mp.mpf(0)
        q = a*a/4-6
        if k == 0:
            return mp.sqrt(mp.pi)/16*q*q*mp.exp(-a*a/16)
        return mp.sqrt(mp.pi)/16*mp.exp(-a*a/16)*a*q*(1-q/8)
    if kind == "C":
        return G(mp.mpf(2*m))
    z = G(4+mp.j*a)
    return mp.re(z) if k == 0 else -mp.im(z)


class Run:
    def __init__(self):
        self.start = time.perf_counter()
        self.evals = 0
        self.cache = {}
        self.metrics = []
        self.raw = {}
        self.active = None
        self.attempts = []

    def check(self):
        if self.evals >= MAX_EVALS or time.perf_counter()-self.start >= MAX_SECONDS:
            raise BudgetStop("global integrand/time cap reached")

    def rho(self, source, t, u):
        key = (mp.mp.dps, source, str(t), u._mpf_)
        if key in self.cache:
            self.active["source_cache_hits"] += 1
            return self.cache[key]
        before = time.perf_counter()
        if source == "theta":
            E = mp.exp(4*u)
            v = mp.pi*mp.exp(t*u*u+5*u)*sum(
                n*n*(2*mp.pi*n*n*E-3)*mp.exp(-mp.pi*n*n*E)
                for n in range(1, N+1))
            self.active["theta_terms"] += N
        else:
            v = (64*u**4+6)*mp.exp(-4*u*u)
        self.active["source_seconds"] += time.perf_counter()-before
        self.active["source_cache_misses"] += 1
        self.cache[key] = v
        return v

    def integration(self, key, source, t, a, kind, k, m=0, s=None, refine=False):
        self.check()
        stage = {"H": "direct", "C": "positive_moments", "M": "signed_moments", "F": "heat"}[kind]
        metric = dict(key=key, dps=mp.mp.dps, stage=stage, refinement=refine,
                      evaluations=0, source_cache_hits=0, source_cache_misses=0,
                      source_seconds=0., theta_terms=0)
        self.active = metric
        before = time.perf_counter()
        def f(u):
            self.check()
            self.evals += 1
            metric["evaluations"] += 1
            v = self.rho(source, t, u)
            if kind == "C":
                return v*mp.exp(2*m*u)*u**k
            c = mp.cos(a*u) if k == 0 else -u*mp.sin(a*u)
            if kind == "M":
                return v*mp.exp(4*u)*c
            if kind == "F":
                return v*mp.exp(-mp.exp(4*u)/(4*s))*c
            return v*c
        panels = [mp.mpf(x) for x in (
            [0, .25, .5, 1, THETA_U] if source == "theta"
            else [0, .5, 1, 2, 3, 4, CONTROL_U])]
        if refine:
            panels = sorted(set(panels+[(x+y)/2 for x,y in zip(panels,panels[1:])]))
        try:
            value, error = mp.quad(f, panels, method="gauss-legendre", maxdegree=5, error=True)
        except BudgetStop:
            metric["seconds"] = time.perf_counter()-before
            metric["status"] = "interrupted"
            self.metrics.append(metric)
            raise
        metric["seconds"] = time.perf_counter()-before
        metric["status"] = "complete"
        self.metrics.append(metric)
        self.raw[(mp.mp.dps, key)] = (value, error)
        self.attempts.append(dict(key=key, dps=mp.mp.dps, value=decimal(value), error=decimal(error), refinement=refine))
        return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reprocess", type=Path, help="Rebuild reporting from saved raw values without quadrature")
    parser.add_argument("--investigation", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    inv = args.investigation.resolve()
    inputs = {str(p.relative_to(inv)): digest(p) for p in [
        inv/"notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md",
        inv/"notes/26_CONSERVATIVE_THETA_FLOW_CONTINUATION_20261028.md",
        inv/"research-progress/handoffs/CTF-E01_BASELINE_HEAT_MEASUREMENTS_REQUEST_R1_20261028.md"]}
    assert inputs["notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md"] == EXPECTED_NOTE25
    # The issued request is immutable through its link definitions; a later return
    # appendix does not change the request-contract hash.
    packet = inv/"research-progress/handoffs/CTF-E01_BASELINE_HEAT_MEASUREMENTS_REQUEST_R1_20261028.md"
    contract = packet.read_text().split("\n## Execution return", 1)[0]
    inputs["request_contract_sha256"] = hashlib.sha256(contract.encode()).hexdigest()
    run, specs, aliases = Run(), {}, {}
    profiles = [("theta_t0", "theta", "0"), ("theta_t025", "theta", "0.25"),
                ("control_tc", "control", "0.25")]
    if args.reprocess:
        mp.mp.dps = 60
        previous = json.loads(args.reprocess.read_text())
        run.evals = previous["evaluation_count"]
        run.metrics = previous["integration_metrics"]
        specs.update(previous.get("quantity_specs",{}))
        for key,q in previous["quantities"].items():
            specs[key] = {field:q[field] for field in ("profile","source","t","frequency","a","kind","k","m","s")}
            for dps in PRECISIONS:
                run.raw[(dps,key)] = (mp.mpf(q[f"value_{dps}"]),mp.mpf(q[f"quadrature_estimate_{dps}"]))
            if "reused_from" in q:
                aliases[key] = q["reused_from"]
        for sample in previous.get("raw_samples",[]):
            run.raw[(sample["dps"],sample["key"])] = (mp.mpf(sample["value"]),mp.mpf(sample["quadrature_estimate"]))
        run.attempts = previous.get("integration_attempts",[])
        if not run.attempts:
            for metric in run.metrics:
                q = previous["quantities"].get(metric["key"])
                if q and metric["status"] == "complete":
                    dps = metric["dps"]
                    run.attempts.append(dict(key=metric["key"],dps=dps,value=q[f"value_{dps}"],
                                             error=q[f"quadrature_estimate_{dps}"],refinement=metric["refinement"]))
        return finish(args,inv,previous["input_hashes"],run,specs,aliases,previous["status"],previous)
    try:
        for dps in PRECISIONS:
            mp.mp.dps = dps
            for profile, source, tstr in profiles:
                t = mp.mpf(tstr)
                frequencies = [("a0", mp.mpf(0)), ("astar", 2*mp.sqrt(6)),
                               ("a28", mp.mpf(28)), ("a30", mp.mpf(30))] if source == "theta" else [
                               ("aminus", 2*mp.sqrt(6)-mp.mpf(1)/4),
                               ("astar", 2*mp.sqrt(6)),
                               ("aplus", 2*mp.sqrt(6)+mp.mpf(1)/4)]
                def acquire(fid, a, kind, k, m=0, s=None):
                    key = f"{profile}/{fid}/{kind}{m if kind=='C' else ''}/k{k}" + (f"/s{s}" if s else "")
                    specs[key] = dict(profile=profile, source=source, t=tstr, frequency=fid,
                                      a=decimal(a), kind=kind, k=k, m=m, s=s)
                    if source == "theta" and fid == "a0" and k == 1 and kind != "C":
                        run.raw[(dps,key)] = (mp.mpf(0),mp.mpf(0))
                    elif kind == "C" and source == "theta" and m == k == 0:
                        other = f"{profile}/a0/H/k0"
                        run.raw[(dps,key)] = run.raw[(dps,other)]
                        aliases[key] = other
                    else:
                        run.integration(key,source,t,a,kind,k,m,s)
                # Same complete source, precision, cutoffs, rule and work cap for
                # direct and heat acquisition. Direct is measured first, cold.
                for fid,a in frequencies:
                    for k in (0,1):
                        acquire(fid,a,"H",k)
                for m in (0,2,4):
                    for k in (0,1):
                        acquire("positive",mp.mpf(0),"C",k,m=m)
                for fid,a in frequencies:
                    for k in (0,1):
                        acquire(fid,a,"M",k)
                        for s in S_VALUES:
                            acquire(fid,a,"F",k,s=s)
                print(json.dumps(dict(event="profile_complete", dps=dps, profile=profile,
                                      evaluations=run.evals, seconds=time.perf_counter()-run.start)), flush=True)
        # One midpoint subdivision refinement at the existing 50-digit precision
        # only if either estimated quadrature error or precision difference fails.
        mp.mp.dps = 50
        for key,spec in specs.items():
            if key in aliases:
                continue
            m = spec["m"] if spec["kind"] == "C" else (2 if spec["kind"] == "M" else 0)
            ck = f'{spec["profile"]}/positive/C{m}/k{spec["k"]}'
            scale = abs(run.raw[(50,ck)][0])
            v30,e30 = run.raw[(30,key)]
            v50,e50 = run.raw[(50,key)]
            if max(e30,e50,abs(v30-v50)) > mp.mpf("1e-12")*scale:
                a = mp.mpf(spec["a"])
                # Reconstruct algebraic frequencies at the current precision.
                if spec["frequency"] in ("astar","aminus","aplus"):
                    a = 2*mp.sqrt(6)+{"astar":0,"aminus":-mp.mpf(1)/4,"aplus":mp.mpf(1)/4}[spec["frequency"]]
                run.integration(key,spec["source"],mp.mpf(spec["t"]),a,spec["kind"],
                                spec["k"],spec["m"],spec["s"],refine=True)
        status = "complete"
    except BudgetStop as exc:
        status = "budget_limited"
        print(str(exc), flush=True)
    return finish(args,inv,inputs,run,specs,aliases,status)


def finish(args,inv,inputs,run,specs,aliases,status,previous=None):
    mp.mp.dps = 50
    quantities, cases = {}, []
    for key,spec in specs.items():
        if (30,key) not in run.raw or (50,key) not in run.raw:
            continue
        m = spec["m"] if spec["kind"] == "C" else (2 if spec["kind"] == "M" else 0)
        ck = f'{spec["profile"]}/positive/C{m}/k{spec["k"]}'
        if (50,ck) not in run.raw:
            continue
        v30,e30 = run.raw[(30,key)]
        v50,e50 = run.raw[(50,key)]
        index,outer = tail_bounds(spec["source"],mp.mpf(spec["t"]),m,spec["k"])
        # a=0,k=1 is identically zero and needs no quadrature or tail payment.
        if spec["frequency"] == "a0" and spec["k"] == 1:
            index = outer = mp.mpf(0)
        agreement = abs(v30-v50)
        diagnostic = index+outer+max(e30,e50)+agreement
        tolerance = mp.mpf("1e-12")*abs(run.raw[(50,ck)][0])
        accepted = diagnostic <= tolerance
        q = dict(**spec, value_30=decimal(v30),value_50=decimal(v50),
                 quadrature_estimate_30=decimal(e30),quadrature_estimate_50=decimal(e50),
                 precision_difference=decimal(agreement),theta_index_bound=decimal(index),
                 u_tail_bound=decimal(outer),diagnostic_absolute_allowance=decimal(diagnostic),
                 absolute_target=decimal(tolerance),accepted=bool(accepted))
        if key in aliases:
            q["reused_from"] = aliases[key]
        if spec["source"] == "control" and spec["kind"] in ("H","M","C"):
            a = 2*mp.sqrt(6)+{"astar":0,"aminus":-mp.mpf(1)/4,"aplus":mp.mpf(1)/4,"positive":0}[spec["frequency"]]
            ref = control_reference(spec["kind"],a,spec["k"],spec["m"],spec["frequency"]=="astar")
            q["analytic_reference"] = decimal(ref)
            q["reference_difference"] = decimal(abs(v50-ref))
            q["reference_check_pass"] = bool(abs(v50-ref) <= tolerance)
        quantities[key] = q
    for key,q in quantities.items():
        if q["kind"] != "F":
            continue
        prefix = f'{q["profile"]}/{q["frequency"]}'
        dependencies = [f'{prefix}/H/k{q["k"]}',f'{prefix}/M/k{q["k"]}',
                        f'{q["profile"]}/positive/C2/k{q["k"]}',f'{q["profile"]}/positive/C4/k{q["k"]}']
        if not all(dep in quantities for dep in dependencies):
            continue
        hq, mq = quantities[dependencies[0]],quantities[dependencies[1]]
        cp = f'{q["profile"]}/positive/'
        c2q, c4q = quantities[f'{cp}C2/k{q["k"]}'],quantities[f'{cp}C4/k{q["k"]}']
        F,M = mp.mpf(q["value_50"]),mp.mpf(mq["value_50"])
        collision = q["source"] == "control" and q["frequency"] == "astar"
        H = mp.mpf(hq["analytic_reference"] if q["source"] == "control" else hq["value_50"])
        C2 = mp.mpf(c2q["value_50"])+mp.mpf(c2q["diagnostic_absolute_allowance"])
        C4 = mp.mpf(c4q["value_50"])+mp.mpf(c4q["diagnostic_absolute_allowance"])
        s = q["s"]
        b0,b1 = C2/(4*s),C4/(32*s*s)
        eh,ef,em = [mp.mpf(x["diagnostic_absolute_allowance"]) for x in (hq,q,mq)]
        def ratio(bound, signal, uncertainty, resolved):
            return decimal(bound/abs(signal)) if resolved and abs(signal)>uncertainty else None
        resolved_H = hq["accepted"] and hq.get("reference_check_pass",True)
        rH = ratio(b0,H,eh,resolved_H)
        rF = ratio(b0,F,ef,q["accepted"])
        rM = ratio(b1,M/(4*s),em/(4*s),mq["accepted"])
        b1H = ratio(b1,H,eh,resolved_H)
        row = dict(profile=q["profile"],frequency=q["frequency"],k=q["k"],s=s,quantity=key,
                   exact_collision=collision,H_reference=decimal(H),F=decimal(F),
                   physical_density=decimal(F/(4*mp.pi*s)**mp.mpf("1.5")),
                   signed_second_moment=decimal(M),mass_residual=decimal(F-H),
                   corrected_residual=decimal(F-H+M/(4*s)),
                   mass_allowance=decimal(b0),corrected_allowance=decimal(b1),
                   mass_residual_error_diagnostic=decimal(ef+eh),
                   corrected_residual_error_diagnostic=decimal(ef+eh+em/(4*s)),
                   allowance_to_H=rH,allowance_to_F=rF,corrected_allowance_to_H=b1H,
                   corrected_allowance_to_next_moment=rM,
                   mass_informative_H=bool(rH is not None and mp.mpf(rH)<1),
                   mass_informative_F=bool(rF is not None and mp.mpf(rF)<1),
                   corrected_informative_H=bool(b1H is not None and mp.mpf(b1H)<1),
                   corrected_informative_next_moment=bool(rM is not None and mp.mpf(rM)<1),
                   bound_check=bool(abs(F-H)<=b0+ef+eh and abs(F-H+M/(4*s))<=b1+ef+eh+em/(4*s)))
        cases.append(row)
    summaries = []
    for dps in PRECISIONS:
        for stage in ("direct","positive_moments","signed_moments","heat"):
            subset = [x for x in run.metrics if x["dps"]==dps and x["stage"]==stage]
            summaries.append(dict(dps=dps,stage=stage,integrations=len(subset),
                **{field:sum(x[field] for x in subset) for field in (
                "evaluations","seconds","source_seconds","source_cache_hits","source_cache_misses","theta_terms")}))
    planned_keys = []
    for profile,source in [("theta_t0","theta"),("theta_t025","theta"),("control_tc","control")]:
        frequencies = ["a0","astar","a28","a30"] if source == "theta" else ["aminus","astar","aplus"]
        for fid in frequencies:
            for k in (0,1):
                planned_keys.extend([f"{profile}/{fid}/H/k{k}",f"{profile}/{fid}/M/k{k}"])
                planned_keys.extend(f"{profile}/{fid}/F/k{k}/s{s}" for s in S_VALUES)
        planned_keys.extend(f"{profile}/positive/C{m}/k{k}" for m in (0,2,4) for k in (0,1))
    missing_keys = sorted(set(planned_keys)-set(quantities))
    record = dict(task="CTF-E01",request_revision="R1",status=status,
        prepared_for="Edward Baker",llm_assistance="substantial",**MODEL,
        thread_id="01a180ca-245a-7151-a2fb-76636318c4c0",history_number=9,
        generated_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        software=dict(python=platform.python_version(),mpmath=mp.__version__,mpmath_backend=mp.libmp.BACKEND),
        script_sha256=digest(Path(__file__)),input_hashes=inputs,
        parameters=dict(epsilon=1,N=N,theta_U=THETA_U,control_U=CONTROL_U,
                        precisions=PRECISIONS,s_values=S_VALUES,max_evaluations=MAX_EVALS,max_seconds=MAX_SECONDS,
                        quadrature="mpmath Gauss-Legendre, maxdegree=5; one conditional midpoint refinement",
                        theta_panels=[0,.25,.5,1,2],control_panels=[0,.5,1,2,3,4,6]),
        evidence="Floating quadrature; analytic tail formulas evaluated without directed rounding. No certified numerical enclosure.",
        error_policy="Sum of theta-index and u-tail analytic bounds, max quadrature estimate across precisions, and precision difference. Heuristic quadrature/roundoff categories; no rigorous roundoff bound.",
        cost_policy="Counts are scalar integrand wrapper calls. Source and Gauss-Legendre rule caches shared. Direct first pays cold source and initial quadrature setup; additional stages are incremental, warm. Analytic control references are cheaper than the measured quadrature comparator.",
        evaluation_count=run.evals,total_seconds=(previous["total_seconds"] if previous else time.perf_counter()-run.start),
        scalar_F_count=len(cases),expected_quantities=len(planned_keys),missing_quantities=missing_keys,
        all_quantities_accepted=not missing_keys and all(q["accepted"] for q in quantities.values()),
        unresolved_quantities=missing_keys+[key for key,q in quantities.items() if not q["accepted"]],
        all_bound_checks_pass=len(cases)==110 and all(c["bound_check"] for c in cases),
        all_control_reference_checks_pass=not missing_keys and all(q.get("reference_check_pass",True) for q in quantities.values()),
        raw_samples=[dict(dps=dps,key=key,value=decimal(value),quadrature_estimate=decimal(error))
                     for (dps,key),(value,error) in run.raw.items()],integration_attempts=run.attempts,
        quadrature_refinements=sum(x["refinement"] for x in run.metrics),
        cost_summary=summaries,integration_metrics=run.metrics,quantity_specs=specs,quantities=quantities,cases=cases)
    if previous:
        record["executed_script_sha256"] = previous.get("executed_script_sha256",previous["script_sha256"])
        record["postrun_reporting_correction"] = "No quadrature repeated: include positive moment diagnostics, gate unresolved ratios, preserve partial samples and original attempt provenance; acquisition metrics retained."
        record["raw_acquisition_record_sha256"] = digest(args.reprocess)
        record["report_finalization_seconds"] = time.perf_counter()-run.start
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({k:record[k] for k in ("status","evaluation_count","total_seconds","scalar_F_count",
        "all_quantities_accepted","all_bound_checks_pass","all_control_reference_checks_pass","quadrature_refinements")}),flush=True)


if __name__ == "__main__":
    main()
