#!/usr/bin/env python3
"""Canonical two-root RT-03/RT-04 r2 acquisition and exterior-force budget.

Prepared for Edward Baker, 26 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol (Codex), recorded effort ultra.
Requires python-flint==0.9.0 and the hash-bound HDC13 canonical source core.
See Rodgers--Tao Note03 for the analytical proof and precise scope.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path
import platform
import sys
import time

sys.dont_write_bytecode = True
import flint
from flint import arb, acb, ctx

CORE_REL = 'papers/investigations-4/12_height_dependent_heat_contours/numerics/hdc13_theta_core.py'
CORE_SHA = 'd340a3cc8400a94b72fa4ca23e254a962cdb4563aacf01789fad7c354ae66edb'
STEPS = 32


def a(value):
    q = Q(value)
    return arb(q.numerator) / q.denominator


def rec(value):
    return value.str(40, more=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def point(p):
    return acb(a(p[0]), a(p[1]))


def cell(p, q):
    return acb(arb(a((p[0]+q[0])/2), a(abs(p[0]-q[0])/2)),
               arb(a((p[1]+q[1])/2), a(abs(p[1]-q[1])/2)))


def run(root, extra_wall_error=Q(0)):
    started = time.perf_counter()
    source_path = root / CORE_REL
    if digest(source_path) != CORE_SHA:
        raise ArithmeticError('Source-core version mismatch; inspect/update the analytical input first')
    spec = importlib.util.spec_from_file_location('rt_r2_canonical_source', source_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    core = module.ActualHeatCore(bits=192)
    checks = []

    def require(ok, name):
        if not ok:
            raise ArithmeticError(name)
        checks.append(name)

    u, v = Q(1, 20000), Q(1, 10000)
    dt = a(v-u)
    tau = arb(a((u+v)/2), a((v-u)/2))
    require(acb(tau).abs_upper() < core.time_radius, 'full time interval lies in source disk')
    d0, d1 = [e.upper() for e in core.errors[:2]]
    require(d0 < arb('6e-27') and d1 < arb('6e-27'), 'complete source errors below fixed budgets')
    # Optional adversarial uncertainty is used only for a recorded
    # nonzero-exit margin-rejection check, never for the PASS certificate.
    require(extra_wall_error>=0,'injected uncertainty nonnegative')
    d0=(d0+a(extra_wall_error)).upper()

    # Fixed 16-segment cover: both horizontal edges use the inherited
    # rational partition; the two vertical edges are whole segments.
    xs = [Q(26), Q(57,2), Q(31), Q(36), Q(77,2), Q(41), Q(87,2), Q(46)]
    vertices = [(x,Q(-2)) for x in xs]
    vertices += [(Q(46),Q(2))]
    vertices += [(x,Q(2)) for x in reversed(xs[:-1])]
    vertices += [(Q(26),Q(-2))]
    require(len(vertices) == 17, '16 exact closed wall segments')
    wall = []
    for p, q in zip(vertices, vertices[1:]):
        # Check exact requested cells, rather than rounded Arb supersets.
        require(max(abs(p[1]),abs(q[1])) <= 2, 'entire exact cell satisfies transverse source domain')
        require(max((p[0]-36)**2+p[1]**2,(q[0]-36)**2+q[1]**2) < 121,
                'entire exact cell satisfies physical disk domain')
        z = cell(p,q)
        h0, h1 = core.jets(z, 1, tau=tau)
        mh = h0.abs_lower().lower()
        mf = (mh-d0).lower()
        mf1 = (h1.abs_upper()+d1).upper()
        require(mf > 0, 'complete canonical and model wall floors positive')
        length = a(abs(q[0]-p[0])+abs(q[1]-p[1]))
        require(mf>d0, 'model floor exceeds complete error')
        q1 = ((d1+mf1*d0/mf)/(mf-d0)).upper()
        nu = (-(1-d0/mf).log()).upper()
        wall.append({'p':p,'q':q,'length':length,'mh':mh,'mf':mf,
                     'mf1':mf1,'q1':q1,'nu':nu})
    require(sum((r['length'] for r in wall),arb(0)) == 48, 'exact contour length 48')
    mh = min(r['mh'] for r in wall)
    mf = min(r['mf'] for r in wall)
    require(mh>arb('4.94e-7') and mf>arb('4.94e-7'), 'fixed declared canonical and model margins pass')

    # The finite-polynomial quotient is the analytic integrand. Physical
    # range oracles and the complete-source error are never callbacks.
    corners = [(Q(26),Q(-2)),(Q(46),Q(-2)),(Q(46),Q(2)),
               (Q(26),Q(2)),(Q(26),Q(-2))]
    integral = acb(0)
    for p,q in zip(corners,corners[1:]):
        pp = point(p)
        direction = point(q)-pp
        def integrand(s, analytic):
            z = pp+direction*s
            return direction*core.evaluate_poly(z,a(u),1)/core.evaluate_poly(z,a(u),0)
        val = acb.integral(integrand,0,1,abs_tol=arb('1e-13'),rel_tol=arb('1e-13'),
                           eval_limit=20000,depth_limit=16)
        require(val.is_finite(), 'finite validated analytic count integral')
        integral += val
    correction = (sum((r['length']*r['q1'] for r in wall),arb(0))/(2*arb.pi())).upper()
    count = integral/acb(0,2*arb.pi())
    count = acb(count.real+arb(0,correction),count.imag+arb(0,correction))
    require(count.real>arb(3)/2 and count.real<arb(5)/2 and count.imag.contains(0),
            'complete initial argument-principle count equals two')
    # Uniform nonvanishing on Gamma continues this count over the real slab.

    def sign_at(x,t):
        value = core.cell(acb(a(x)),tau=acb(t))
        require(value.imag.contains(0), 'real-type canonical field at real data')
        if value.real>0:
            return 1,value.real
        if value.real<0:
            return -1,value.real
        return 0,value.real

    broad = [(Q(28),Q(29)),(Q(42),Q(43))]
    for lo,hi in broad:
        sl,_ = sign_at(lo,tau)
        sr,_ = sign_at(hi,tau)
        require(sl*sr==-1,'uniform sign-changing real root interval')

    def bisect(bracket,t):
        lo,hi = bracket
        sl,_ = sign_at(lo,a(t))
        sh,_ = sign_at(hi,a(t))
        require(sl*sh==-1,'endpoint root bisection initial signs')
        for _ in range(STEPS):
            mid=(lo+hi)/2
            sm,_=sign_at(mid,a(t))
            require(sm!=0,'certified bisection sign excludes zero')
            if sm==sl:
                lo=mid
            else:
                hi=mid
        return lo,hi

    initial = [bisect(b,u) for b in broad]
    terminal = [bisect(b,v) for b in broad]
    # Freeze rational whole-slab brackets centered at the certified initial
    # root boxes. The radius is a declared 1e-4, not fitted root uncertainty.
    uniform = []
    uniform_signs=[]
    for lo,hi in initial:
        center=(lo+hi)/2
        interval=(center-Q(1,10000),center+Q(1,10000))
        sl,vl=sign_at(interval[0],tau)
        sr,vr=sign_at(interval[1],tau)
        require(sl*sr==-1,'narrow whole-slab root bracket certified')
        uniform.append(interval)
        uniform_signs.append([rec(vl),rec(vr)])
    gap_lo = a(uniform[1][0]-uniform[0][1])
    gap_hi = a(uniform[1][1]-uniform[0][0])
    require(gap_lo>13 and gap_hi<14,'fixed block gap range')
    emax=(2/gap_lo**2).upper()
    emin=(2/gap_hi**2).lower()
    initial_gap_lo=a(initial[1][0]-initial[0][1])
    initial_gap_hi=a(initial[1][1]-initial[0][0])
    e0lo=(2/initial_gap_hi**2).lower()
    e0hi=(2/initial_gap_lo**2).upper()
    final_gap_lo=a(terminal[1][0]-terminal[0][1])
    final_gap_hi=a(terminal[1][1]-terminal[0][0])
    e1lo=(2/final_gap_hi**2).lower()
    e1hi=(2/final_gap_lo**2).upper()
    # Both real intervals lie in J=[28,43], so the common contour buffer is2.
    require(all(lo>=28 and hi<=43 for lo,hi in uniform),'whole population in fixed real core J')
    b=arb(2)
    af=(sum((r['length']*r['mf1']/r['mf'] for r in wall),arb(0))/(arb.pi()*b*b)).upper()
    kj=(sum((r['length']*r['q1'] for r in wall),arb(0))/(arb.pi()*b*b)).upper()
    kl=(2*sum((r['length']*r['nu'] for r in wall),arb(0))/(arb.pi()*b**3)).upper()
    a0j=(sum((r['length']*r['q1'] for r in wall),arb(0))/(arb.pi()*b)).upper()
    a0l=(sum((r['length']*r['nu'] for r in wall),arb(0))/(arb.pi()*b*b)).upper()
    kappa=min(kj,kl)
    a0=min(a0j,a0l)
    i_upper=(dt*emax).upper()
    model_budget=(2*af*i_upper).upper()
    coupled_budget=(2*kappa*i_upper).upper()
    separate_budget=(8*a0*dt/gap_lo**3).upper()
    transfer_budget=min(coupled_budget,separate_budget)
    full_contour_budget=(model_budget+transfer_budget).upper()
    require(af<arb('10.47'),'model curvature below declared 10.47 bound')
    require(kappa<arb('5e-20'),'complete drift variation error below declared budget')

    # Equally informed direct comparator: actual complete H_z,H_zz on
    # the already acquired whole-slab root brackets. No model zero is
    # substituted for a true root in these quotients.
    velocities=[]
    slope_floors=[]
    direct_jets=[]
    for lo,hi in uniform:
        z=acb(arb(a((lo+hi)/2),a((hi-lo)/2)))
        jets=core.jets(z,2,tau=tau)
        require(all(h.imag.contains(0) for h in jets),'real root-cell jets respect real symmetry')
        floor=abs(jets[1].real).lower()
        require(floor>0,'independent root slope floor on entire root cell')
        velocities.append(jets[2].real/jets[1].real)
        slope_floors.append(floor)
        direct_jets.append([rec(h.real) for h in jets])
    # Build the interval directly from exact rational endpoints to avoid
    # treating displayed floating bounds as exact mathematical data.
    gl=uniform[1][0]-uniform[0][1]
    gh=uniform[1][1]-uniform[0][0]
    gap=arb(a((gl+gh)/2),a((gh-gl)/2))
    b_direct=-4*(velocities[1]-velocities[0])/gap**3+16/gap**4
    direct_budget=(b_direct.upper()*dt).upper()
    direct_integral=arb((b_direct*dt).mid(),(b_direct*dt).rad())
    require(b_direct>0,'direct exterior contribution positive over whole slab')
    require(direct_budget<full_contour_budget,'direct same-source force payment sharper than contour bound')
    dissipation=4*arb((emin+emax)/2,(emax-emin)/2)**2*dt
    balance=direct_integral-dissipation
    energy_increment=arb((e1lo+e1hi-e0lo-e0hi)/2,
                         (e1hi-e1lo+e0hi-e0lo)/2)
    require(balance.overlaps(energy_increment),'complete energy balance and endpoint root data consistent')
    require(energy_increment>0,'endpoint energy increment positive')

    wall_serial=[]
    for r in wall:
        wall_serial.append({'from':[str(x) for x in r['p']], 'to':[str(x) for x in r['q']],
                            'length':rec(r['length']),'canonical_H_floor':rec(r['mh']),
                            'model_F_floor':rec(r['mf']),'model_Fprime_upper':rec(r['mf1']),
                            'quotient_error_upper':rec(r['q1']),'log_ratio_error_upper':rec(r['nu'])})
    def intervals(rows):
        return [[str(x) for x in pair] for pair in rows]
    out={'schema':'rt03-rt04-r2-canonical-two-root-v1','status':'PASS',
         'date_local':'2026-10-26','prepared_for':'Edward Baker',
         'model':'gpt-6.1-sol','reasoning_effort':'ultra','LLM_assistance':'substantial',
         'review_independence':'same-model internal review only',
         'injected_extra_wall_error':str(extra_wall_error),
         'script_sha256':digest(Path(__file__)),'core_path':CORE_REL,'core_sha256':CORE_SHA,
         'python':platform.python_version(),'python_flint':flint.__version__,
         'domain':{'time':[str(u),str(v)],'delta_time':str(v-u),
                   'rectangle_x':['26','46'],'rectangle_y':['-2','2'],
                   'real_core_J':['28','43'],'contour_length':48,'buffer':2},
         'finite_model':'F_t=sum_{k=0}^5(-t)^k P95^(2k)/k!, canonical H0 Taylor at36; exact coefficients enclosed by Arb',
         'source_oracle':core.metadata(),
         'contour':{'segments':len(wall),'H_floor_lower':rec(mh),'F_floor_lower':rec(mf),
                    'cells':wall_serial},
         'initial_complete_zero_count':{'enclosure':rec(count),'count':2,
                                        'complete_quotient_correction':rec(correction),
                                        'uniform_continuation':'fixed Gamma nonzero over connected real slab'},
         'roots':{'bisection_steps':STEPS,'initial':intervals(initial),'terminal':intervals(terminal),
                  'uniform':intervals(uniform),'uniform_sign_enclosures':uniform_signs,
                  'gap_lower':rec(gap_lo),'gap_upper':rec(gap_hi),
                  'initial_E_lower':rec(e0lo),'initial_E_upper':rec(e0hi),
                  'uniform_E_lower':rec(emin),'uniform_E_upper':rec(emax),
                  'terminal_E_lower':rec(e1lo),'terminal_E_upper':rec(e1hi),
                  'energy_increment':rec(energy_increment)},
         'contour_force':{'model_derivative_A_F_upper':rec(af),
                          'transfer_kappa_jet_upper':rec(kj),'transfer_kappa_log_upper':rec(kl),
                          'transfer_kappa_selected_upper':rec(kappa),
                          'separate_drift_A0_jet_upper':rec(a0j),'separate_drift_A0_log_upper':rec(a0l),
                          'separate_drift_A0_selected_upper':rec(a0),
                          'integral_E_upper':rec(i_upper),'model_force_integral_upper':rec(model_budget),
                          'coupled_transfer_integral_upper':rec(coupled_budget),
                          'separate_transfer_integral_upper':rec(separate_budget),
                          'selected_transfer_integral_upper':rec(transfer_budget),
                          'complete_force_integral_upper':rec(full_contour_budget),
                          'coupled_over_separate_budget_ratio':rec(coupled_budget/separate_budget)},
         'direct_force':{'root_slope_floors':[rec(x) for x in slope_floors],
                         'root_cell_H_Hz_Hzz':direct_jets,
                         'root_velocity_intervals':[rec(x) for x in velocities],
                         'B_H_interval':rec(b_direct),'B_H_integral_interval':rec(direct_integral),
                         'integral_upper':rec(direct_budget),
                         'contour_over_direct_upper_budget_ratio':rec(full_contour_budget/direct_budget),
                         'internal_dissipation_integral':rec(dissipation),
                         'complete_balance_increment_interval':rec(balance),
                         'method':'B_H=-4(v2-v1)/g^3+16/g^4, vi=Hzz(ai)/Hz(ai), same actual root cells'},
         'checks':checks,'cost':{'validated_count_integrals':4,'wall_cells':len(wall),
                                'root_bisection_steps_per_endpoint_root':STEPS,
                                'direct_extra_root_jet_cells':2,
                                'elapsed_seconds':time.perf_counter()-started},
         'scope':'Known-covered compact source-acquisition and named exterior-term pilot; no new Newman bound, high-height uniformity, endpoint exclusion or RT dyadic assembly.'}
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--inject-wall-error',type=Q,default=Q(0))
    args=parser.parse_args()
    out=run(args.repo_root.resolve(),args.inject_wall_error)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','contour_force','direct_force','cost')},indent=2))


if __name__=='__main__':
    main()
