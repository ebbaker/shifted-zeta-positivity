#!/usr/bin/env python3
"""Bounded complete physical jet and coherent disk residual validation.
Prepared for Edward Baker, 20 October 2026; substantial LLM assistance.
Authoring model gpt-6-astra, actual reasoning effort ultra (parent metadata).
No new coverage or threshold exclusion is claimed. Python-flint 0.9.0.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from fractions import Fraction as F
import hashlib, importlib.util, itertools, json, math, platform, resource, signal, sys, time
from pathlib import Path
import flint
from flint import arb, acb, ctx

PINS = [
'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py',
'papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md',
'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md',
'papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex',
]
EXPECTED_SHA256 = {'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py': '45c2e9adc347f91076b1ff16b171b71f450b504e391044811bf9bc847fe3c4ff', 'papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md': '933d9ae00689232017b7ee1d641acf04b4f245230366a1d18842bf03213cd23a', 'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md': 'b2ce09a21bc5f08eb94b53d2deb4ea1d142d981aac516234ef9337c672ead3df', 'papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex': '38a819cb4afa4008dc376b8a8892d020722fe9b9eb9a6afd44a46e538f9074c7'}

DSTAR = (F(99999,10**6), F(100001,10**6), F(29999999,10**6), F(30000001,10**6), F(0), F(0))
R = F(1,2)

@contextmanager
def deadline(seconds):
    def exhausted(*args): raise TimeoutError('declared setup resource cap exceeded')
    old=signal.signal(signal.SIGALRM, exhausted)
    signal.alarm(seconds)
    try: yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)

def mul(a,b,n):
    return [sum((a[k]*b[j-k] for k in range(j+1)), F(0)) for j in range(n+1)]

def inverse(a,n):
    assert a[0]
    out=[1/a[0]]
    for j in range(1,n+1):out.append(-sum((a[k]*out[j-k] for k in range(1,j+1)),F(0))/a[0])
    return out

def schur_coefficients(parameters):
    """Exact coefficients through n=len(parameters)-1 of a real Schur function.
    g_n = p_n; g_k=(p_k+w*g_{k+1})/(1+p_k*w*g_{k+1}).
    Every real disk-bounded jet of order n admits these parameters in [-1,1].
    """
    n=len(parameters)-1
    g=[parameters[-1]]+[F(0)]*n
    for p in reversed(parameters[:-1]):
        wg=[F(0)]+g[:-1]
        numerator=[p]+wg[1:]
        denominator=[F(1)]+[p*v for v in wg[1:]]
        g=mul(numerator,inverse(denominator,n),n)
    return g

def exact_fixtures():
    fixture_rows=[]
    for p in [tuple(F(v) for v in vs) for vs in itertools.product((-1,0,1),repeat=5)]+[(F(1,3),F(-2,5),F(3,7),F(-1,4),F(2,9))]:
        c=schur_coefficients(p)
        a,b,g=p[:3]
        assert c[0]==a and c[1]==(1-a*a)*b
        assert c[2]==(1-a*a)*((1-b*b)*g-a*b*b)
        if abs(a)==1:assert c[1:]==[0]*4
        # Forward Schur extraction independently reconstructs each nondegenerate layer.
        now=c[:]
        for k in range(4):
            a=now[0]
            assert a==p[k]
            if abs(a)==1:break
            m=len(now)-1
            denominator=[1-a*a]+[-a*v for v in now[1:]]
            quotient=mul([F(0)]+now[1:],inverse(denominator,m),m)
            now=quotient[1:]
        if p==(F(1,3),F(-2,5),F(3,7),F(-1,4),F(2,9)):
            fixture_rows.append({'parameters':list(map(str,p)), 'coefficients':list(map(str,c)), 'physical_derivatives_R_half':[str(math.factorial(j)*2**j*c[j]) for j in range(5)]})
    # Polynomial heat event H(t,x)=x^2-2(t-T) at x=0,t=T remains accepted.
    h=[F(0),F(0),F(2),F(0),F(0),F(0),F(0)]
    L=F(1,100)
    q=2*h[3]**2-3*h[2]*h[4]-18*L*h[2]**2
    assert q==-72*L
    # Exact exponential-normalizer return; all derivatives retained through 6.
    normalizers=[]
    for alpha,beta in [(F(2,3),F(-1,5)),(F(-7,4),F(3,8)),(F(0),F(0))]:
        aj=[F(1),alpha]; invj=[F(1),-alpha]
        for n in range(1,6):
            aj.append(alpha*aj[-1]+n*beta*aj[-2])
            invj.append(-alpha*invj[-1]-n*beta*invj[-2])
        f=[F(0),F(0),F(3,7),F(-5,11),F(13,17),F(1,19),F(-2,23)]
        physical=[sum((math.comb(j,k)*aj[j-k]*f[k] for k in range(j+1)),F(0)) for j in range(7)]
        returned=[sum((math.comb(j,k)*invj[j-k]*physical[k] for k in range(j+1)),F(0)) for j in range(7)]
        assert returned==f
        raw=2*physical[3]**2-3*physical[2]*physical[4]-18*L*physical[2]**2
        normalized=2*f[3]**2-3*f[2]*f[4]-18*(L+beta)*f[2]**2
        assert raw==normalized
        normalizers.append({'alpha':str(alpha),'alpha_x':str(beta),'Q_over_A_squared':str(normalized),'all_returns_exact':True})
    return {'schur_exact_cases':3**5+1,'nontrivial_schur_fixture':fixture_rows,'normalizer_return_cases':normalizers,
            'genuine_polynomial_heat_event':{'jets':list(map(str,h)),'L':str(L),'Q_L':str(q),'strict_first_jet_exclusion':'checked by actual helper in main'}}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--bits',type=int,nargs='+',default=[192,256])
    args=ap.parse_args(); start=time.monotonic()
    # RLIMIT_AS is enforced when the platform supports it; failure is explicit.
    memory_cap=1024**3
    memory_hard_limit=False; memory_limit_error=None
    try:
        resource.setrlimit(resource.RLIMIT_AS,(memory_cap,memory_cap))
        memory_hard_limit=True
    except (OSError,ValueError) as exc: memory_limit_error=str(exc)
    assert flint.__version__=='0.9.0'
    hash_before={p:hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in PINS}
    if hash_before != EXPECTED_SHA256: raise RuntimeError('Pinned source bytes changed; review before replay')
    source=args.repo/PINS[0]
    spec=importlib.util.spec_from_file_location('pinned_theta_evaluator',source)
    base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    fixtures=exact_fixtures()
    polynomial_first_jet=[arb(0),arb(0)]
    assert base.coordinate_separator(polynomial_first_jet) is None
    fixtures['genuine_polynomial_heat_event']['strict_first_jet_exclusion']=False
    def event_excluded(p0,p1,eta,radius):
        if eta==0:
            return base.coordinate_separator([p0,p1]) is not None
        assert eta>0 and radius>0
        return base.square(p0)+eta*radius*p1.abs_lower()-eta*eta>0
    assert not event_excluded(arb(0),arb(0),arb(0),arb(1)/2)
    assert event_excluded(arb(1),arb(0),arb(0),arb(1)/2)
    assert not event_excluded(arb(0),arb(0),arb(1),arb(1)/2)
    fixtures['zero_residual_boundary_handled_without_division']=True
    cells=[(F(1,100),F(1,100),F(25),F(25),F(0),F(0)),
           (F(21,200),F(21,200),F(35),F(35),F(0),F(0)),
           (F(1,5),F(1,5),F(45),F(45),F(0),F(0)),
           (F(1,10),F(11,100),F(28),F(29),F(0),F(0)),
           (F(1,100),F(1,5),F(34),F(341,10),F(0),F(0)),
           (F(1,10),F(11,100),F(34),F(341,10),F(2,5),F(3,5))]
    for t in [F(1,100),F(1,5)]:
        for x,y in [(F(25),F(1)),(F(35),F(1,2)),(F(45),F(1))]:cells.append((t,t,x,x,y,y))
    cells.append(DSTAR)
    disk=(DSTAR[0],DSTAR[1],DSTAR[2]-R,DSTAR[3]+R,-R,R)
    runs=[]; previous=None
    for bits in args.bits:
        results={}; evaluators={}
        for method in ('real','shifted'):
            with deadline(90):evaluators[method]=base.Evaluator(method,bits=bits,max_component=6)
            assert evaluators[method].maximum_midpoint_order==80
            assert evaluators[method].maximum_remainder_order==82
        rec=base.rec; A=base.A
        matched=[]; actual={}; diskrows={}; envelopes=[]
        for index,cell in enumerate(cells):
            values={m:e.enclose(*cell) for m,e in evaluators.items()}
            for j in range(7):
                assert values['real'][0][j].overlaps(values['shifted'][0][j]),(index,j)
                for method in evaluators:
                    b=values[method][1][j]
                    assert b['total_added_error']<arb('1e-10')
                    for key in ('mode','source','quadrature_with_internal_rounding'):assert b[key]<arb('1e-12')
                    assert b['taylor_propagation']<arb('1e-11')
            matched.append({'exact_cell':list(map(str,cell)), 'all_seven_overlap':True,
                            'methods':{m:{'jets':[rec(v) for v in pair[0]],'budgets':[{k:rec(v) for k,v in b.items()} for b in pair[1]]} for m,pair in values.items()}})
            if cell==DSTAR:
                for method,(v,bs) in values.items():
                    selected=base.coordinate_separator(v)
                    assert selected
                    actual[method]={'physical_jets':[rec(q) for q in v],
                       'separate_component_polynomial_images':[rec(b['polynomial_enclosure']) for b in bs],
                       'first_jet_separator':{'component':selected[1],'sign':selected[2],'margin_lower':rec(selected[0])},
                       'time_derivative_of_h4_equals_minus_h6':[rec(-v[6])],
                       'h4_time_Lipschitz_upper':rec(v[6].abs_upper())}
        for method,e in evaluators.items():
            _,budgets=e.enclose(*disk)
            b=budgets[0]; eta=b['total_added_error']
            assert eta<arb('1e-10')
            dt=base.box(DSTAR[0],DSTAR[1])-A(e.tc)
            dx=base.box(DSTAR[2],DSTAR[3])-A(e.xc)
            coherent=[]; discrepancies=[]
            for j in range(7):
                # These are genuine derivatives of one degree-50 P0; P_j has degree50.
                ck=[base.poly([e.midpoints[l+j+2*k]/math.factorial(l)
                               for l in range(e.L-j+1)],dx)/math.factorial(k)
                    for k in range(e.K+1)]
                fj=base.poly(ck,-dt)
                coherent.append(fj)
                high=[]
                for k in range(e.K+1):
                    tail=sum((e.midpoints[l+j+2*k]*dx**l/math.factorial(l)
                              for l in range(e.L-j+1,e.L+1)),arb(0))
                    high.append(tail/math.factorial(k))
                defect=base.poly(high,-dt)
                discrepancies.append(defect.abs_upper())
                allowance=eta*math.factorial(j)/A(R)**j
                physical=arb(actual[method]['physical_jets'][j])
                assert (fj+arb(0,allowance)).overlaps(physical)
            gate=base.square(coherent[0])+eta*A(R)*coherent[1].abs_lower()-eta*eta
            assert gate>0 and event_excluded(coherent[0],coherent[1],eta,A(R))
            actual[method]['coherent_P0_derivative_images']=[rec(v) for v in coherent]
            actual[method]['component_Pj_minus_derivative_P0_abs_upper']=[rec(v) for v in discrepancies]
            actual[method]['event_Schwarz_Pick_gate_lower']=rec(gate.lower())
            diskrows[method]={'disk_radius':str(R),'containing_rectangle':list(map(str,disk)),
                            'eta_absolute_complex_residual_upper':rec(eta),
                            'residual_payments':{k:rec(v) for k,v in b.items() if k!='polynomial_enclosure'},
                            'cauchy_derivative_allowances':[rec(eta*math.factorial(j)/A(R)**j) for j in range(7)],
                            'normalizer':'A=1; alpha_x=0; physical H normalization',
                            'polynomial':'P(t,z)=sum_{ell=0}^{50} sum_{k=0}^{12} (-1)^k m[ell+2k] (z-35)^ell (t-21/200)^k/(ell! k!), m exact midpoint dyadics; polynomial coefficients exact rationals',
                            'eta_includes_parameter_variation':False,
                            'eta_bounds_error_uniformly_over_parameters':True}
            # Independent finite-integral mixed time derivative check at center, j=4.
            def mixed(u,analytic):
                v=u+acb(0,e.d) if method=='shifted' else u
                q=(4*v).exp(); total=acb(0)
                for n in range(1,5):
                    lam=e.pi*n*n
                    total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
                if method=='shifted':
                    return (A(e.tc)*v*v+v+acb(0,A(e.xc))*v).exp()*total*(acb(0,1)*v)**4*v*v
                return (A(e.tc)*u*u+u).exp()*total*u**6*(A(e.xc)*u).cos()
            value=acb.integral(mixed,0,1,abs_tol=arb('1e-35'),rel_tol=arb('1e-28'),eval_limit=200000,depth_limit=30)
            assert value.is_finite()
            midpoint6=arb(e.midpoints[6],e.quad_radii[6])
            assert value.real.overlaps(-midpoint6)
            envelopes.append({'method':method,'direct_integral_dt_dx4':rec(value.real),'negative_midpoint_h6':rec(-midpoint6),'overlap':True})
        # Fresh precisions must agree on physical images; this is diagnostic only.
        if previous:
            for method in evaluators:
                for a,b in zip(previous[method]['physical_jets'],actual[method]['physical_jets']):assert arb(a).overlaps(arb(b))
        previous=actual
        manifests={}
        for method,e in evaluators.items():
            manifest=e.manifest()
            exact=[]
            for midpoint in e.midpoints:
                mantissa,exponent=midpoint.man_exp()
                mantissa,exponent=int(mantissa),int(exponent)
                assert arb(mantissa)*arb(2)**exponent==midpoint
                exact.append({'mantissa':str(mantissa),'binary_exponent':exponent})
            manifest['midpoint_exact_dyadics']=exact
            manifest['exact_dyadic_encoding']='mantissa * 2 ** binary_exponent; all entries round-trip exactly at run precision'
            manifests[method]=manifest
        runs.append({'bits':bits,'evaluators':manifests,'matched_cases':matched,
                    'actual_D_star':actual,'shared_disk_residual':diskrows,'separately_integrated_heat_diagnostic':envelopes})
        assert time.monotonic()-start<300
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)<memory_cap
    assert hash_before=={p:hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in PINS}
    output={'date':'2026-10-20','prepared_for':'Edward Baker','model':'gpt-6-astra','effort':'ultra',
       'provenance':'Root verified actual parent turn metadata; substantial LLM assistance; internal same-model computation.',
       'source_sha256':hash_before,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'python':platform.python_version(),'python_flint':flint.__version__,'frozen_D_star':list(map(str,DSTAR)),
       'exact_fixtures':fixtures,'declared_total_added_allowance':'1e-10','runs':runs,
       'all_checks_passed':True,'elapsed_seconds':time.monotonic()-start,'resource_caps':{'setup_seconds':90,'run_seconds':300,'address_space_bytes':memory_cap,'RLIMIT_AS_set_succeeded':memory_hard_limit,'RLIMIT_AS_error':memory_limit_error,'memory_contract':'Fixed problem dimensions and measured peak below cap; unsupported OS hard cap is not claimed enforced','peak_resident_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)},
       'scope':'Complete physical h0-h6 and coherent disk residual on declared bounded domain; empty event set at Dstar; no sign gain or new coverage. No UAR high-sector derivative theorem.'}
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'passed':True,'seconds':output['elapsed_seconds'],'D_star':runs[-1]['actual_D_star'],
                       'disk_eta':{m:q['eta_absolute_complex_residual_upper'] for m,q in runs[-1]['shared_disk_residual'].items()}},indent=2))
if __name__=='__main__':main()
