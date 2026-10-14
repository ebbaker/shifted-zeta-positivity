#!/usr/bin/env python3
"""Validated higher-height stationary signs with correlated raw-source transport.

2026-10-14. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
Requires python-flint. Imports the reviewed retained integration, full Gaussian
transform, raw heat transport, and complete-index bound. It sums retained
raw center jets before applying common time and space
Taylor monomials, retaining theta-index cancellation in the aggregate.
The individual channel enclosures and every remainder payment are retained.
No sampled sign, tabulated zero, or approximate root decides any cell.
"""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from math import isqrt
import platform
import time

import flint
from flint import arb, ctx
import certify_compensated_stationary_theta as core


def compact(a):
    """Exact outward dyadic endpoints; no rounded decimal enters a decision."""
    core.require(a.is_finite(), 'Nonfinite enclosure')
    def endpoint(v):
        m, e = v.man_exp()
        return [str(m), int(e)]
    return [endpoint(a.lower()), endpoint(a.upper())]


def lower(a):
    return Fraction(int(a[0][0])) * Fraction(2)**a[0][1]


def upper(a):
    return Fraction(int(a[1][0])) * Fraction(2)**a[1][1]


def repack(value):
    """Compact the original certificate's exact enclosure serialization."""
    if isinstance(value, dict):
        if 'lower_dyadic' in value and 'upper_dyadic' in value:
            return [[value[k]['mantissa'], value[k]['exponent']]
                    for k in ('lower_dyadic', 'upper_dyadic')]
        return {k: repack(v) for k, v in value.items()}
    if isinstance(value, list):
        return [repack(v) for v in value]
    return value


class SlabSource(core.Source):
    """Original source machinery with exact arbitrary 0<=t_left<t_right<=1."""
    def __init__(self, n, bits, space_order, time_order, beta_order, tl, tr):
        core.require(0 <= tl < tr <= 1, 'Time slab lies in proved majorant range')
        self.n = n
        self.p = arb.pi()
        self.t0 = core.rat((tl + tr)/2)
        self.dt = core.rat((tr - tl)/2)
        self.tmax = core.rat(tr)
        self.lt = time_order
        self.lx = space_order
        self.lb = beta_order
        self.top = 3 + 2*(self.lt - 1) + self.lx - 1
        self.mtop = 3 + 2*(self.lt - 1) + self.lx
        self.tol = arb(2)**(-(bits - 48))
        self.endpoints = [core.endpoint_coefficients(nn) for nn in range(1, n + 1)]
        self.tail_norms, self.beta_norms = core.compensated_tail_norms(n)
        self.moments = []
        self.moment_quadrature_max_radius = arb(0)
        self.jet_quadrature_max_radius = arb(0)
        self.source_tail_max = arb(0)
        self.center_cache = {}
        for nn in range(1, n + 1):
            mm = []
            for k in range(self.mtop + 1):
                v, rad, tail = self.integrate(nn, self.tmax, arb(0), k, True)
                mm.append(v)
                self.moment_quadrature_max_radius = max(self.moment_quadrature_max_radius, rad)
                self.source_tail_max = max(self.source_tail_max, tail)
            self.moments.append(mm)
        core.require(all(m > 0 for mm in self.moments for m in mm),
                     'Positive complete retained channel moment enclosures')

    def center(self, x):
        m, e = x.man_exp()
        key = (int(m), int(e))
        if key not in self.center_cache:
            self.center_cache[key] = super().center(x)
        return self.center_cache[key]


    def enclosure(self, center_data, eta):
        """Enclose the same exact aggregate, correlating common monomials.

        Summation commutes with the finite Taylor polynomial. Positive per-
        channel remainder bounds add. This improves interval dependency only;
        it changes no source, index tail, half-line tail, or approximation.
        """
        aggregate, channels, rawpay, betapay = super().enclosure(center_data, eta)
        raw, betas = center_data
        summed_jets = [sum(row[k] for row in raw) for k in range(self.top + 1)]
        tau = core.symmetric(self.dt)
        rawsum = []
        for k in range(4):
            polynomial = sum(core.ipow(-tau, ell)/core.factorial(ell)
                * sum(core.ipow(eta, m)/core.factorial(m)*summed_jets[k+2*ell+m]
                      for m in range(self.lx)) for ell in range(self.lt))
            payment = sum(row[k] for row in rawpay)
            rawsum.append(polynomial + core.symmetric(payment))
        sb = sum(z[0] for z in self.endpoints)
        se = sum(z[1] for z in self.endpoints)
        tball = self.t0 + core.symmetric(self.dt)
        beta = [[self.beta_transport(betas[b], b, k, eta)[0]
                 for k in range(4)] for b in range(2)]
        aggregate = [rawsum[k]-sb*beta[0][k]-(se+6*tball*sb)*beta[1][k]
                     for k in range(4)]
        return aggregate, channels, rawpay, betapay


def analyze(source, tl, tr, xl, xr, td, xd):
    cell = repack(core.analyze_cell(source, core.rat(xl), core.rat(xr), xd))
    # Store all genuine jets to permit separate exact branch-cover auditing.
    eps = [v/core.rat(xl)**4 for v in source.tail_norms]
    data = source.center(core.rat((xl+xr)/2))
    aggregate = source.enclosure(data, core.symmetric(core.rat((xr-xl)/2)))[0]
    genuine = [aggregate[k]+core.symmetric(eps[k]) for k in range(4)]
    return {'t': [str(tl), str(tr)], 'x': [str(xl), str(xr)],
            'time_bisection_depth': td, 'space_bisection_depth': xd,
            'genuine_four_jets': [compact(v) for v in genuine],
            'compensated_aggregate_jets': cell['compensated_aggregate_jets'],
            'complete_compensated_four_jet_errors': cell['complete_compensated_four_jet_errors'],
            'raw_source_parameter_Taylor_payments': cell['raw_source_parameter_Taylor_payments'],
            'complete_Gaussian_transform_Taylor_payments': cell['complete_Gaussian_transform_Taylor_payments'],
            'observations': cell['observations']}


def interval_overlap(a, b):
    return max(a[0], b[0]) < min(a[1], b[1])


def exact_cover(cells, tl, tr, xl, xr):
    """At each elementary closed time slab check the exact full spatial cover.

    Cells are closed. Their interiors partition every elementary time slab;
    inspecting its midpoint selects exactly the cells spanning that slab.
    Closedness then covers all slab boundaries as well.
    """
    times = sorted({Fraction(v) for c in cells for v in c['t']})
    core.require(times[0] == tl and times[-1] == tr, 'Exact time endpoints')
    for left, right in zip(times, times[1:]):
        middle = (left+right)/2
        spans = sorted((Fraction(c['x'][0]), Fraction(c['x'][1]))
                       for c in cells if Fraction(c['t'][0]) < middle < Fraction(c['t'][1]))
        core.require(spans and spans[0][0] == xl and spans[-1][1] == xr,
                     'Spatial endpoints on every exact elementary time slab')
        core.require(all(a < b for a,b in spans)
                     and all(spans[k][1] == spans[k+1][0] for k in range(len(spans)-1)),
                     'Gap-free nonoverlapping spatial partition on every time slab')
    for c in cells:
        core.require(tl <= Fraction(c['t'][0]) < Fraction(c['t'][1]) <= tr
                     and xl <= Fraction(c['x'][0]) < Fraction(c['x'][1]) <= xr,
                     'No cell outside requested closed rectangle')
        core.require(all(Fraction(v).denominator & (Fraction(v).denominator-1) == 0
                         for v in c['t']+c['x']), 'All parameter endpoints exact dyadics')
    return times


def branch_cover(cells, times):
    """Join contiguous possible-stationarity cells into uniform branch windows.

    The sum of cell derivative enclosures is not used. Every next derivative
    has the same strict sign on every member cell; strict opposite outer
    endpoint enclosures prove one and only one zero at every slab time.
    """
    records = []
    for tl, tr in zip(times, times[1:]):
        midpoint = (tl+tr)/2
        slab = sorted((c for c in cells if Fraction(c['t'][0]) < midpoint < Fraction(c['t'][1])),
                      key=lambda c: Fraction(c['x'][0]))
        for j in (0,1):
            groups, group = [], []
            for c in slab:
                o = c['observations'][j]
                if o['classification'].startswith('stationary_signed'):
                    group.append(c)
                elif group:
                    groups.append(group)
                    group = []
            if group:
                groups.append(group)
            for group in groups:
                derivs = [c['genuine_four_jets'][j+2] for c in group]
                ls = group[0]['observations'][j]['left_stationary_derivative']
                rs = group[-1]['observations'][j]['right_stationary_derivative']
                positive = all(lower(v) > 0 for v in derivs)
                negative = all(upper(v) < 0 for v in derivs)
                unique = ((positive and upper(ls) < 0 and lower(rs) > 0)
                          or (negative and lower(ls) > 0 and upper(rs) < 0))
                records.append({'t': [str(tl), str(tr)], 'j': j,
                                'x_window': [group[0]['x'][0], group[-1]['x'][1]],
                                'member_cell_count': len(group),
                                'next_derivative_sign': (1 if positive else -1 if negative else 0),
                                'left_stationary_derivative': ls, 'right_stationary_derivative': rs,
                                'uniform_unique_regular_branch': bool(unique)})
    return records


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', required=True, type=Path)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--theta-terms', type=int, default=4)
    ap.add_argument('--space-order', type=int, default=16)
    ap.add_argument('--time-order', type=int, default=8)
    ap.add_argument('--beta-order', type=int, default=32)
    ap.add_argument('--t-left', type=Fraction, default=Fraction(0))
    ap.add_argument('--t-right', type=Fraction, default=Fraction(1,2))
    ap.add_argument('--time-slabs', type=int, default=8)
    ap.add_argument('--x-left', type=int, default=40)
    ap.add_argument('--x-right', type=int, default=60)
    ap.add_argument('--max-time-depth', type=int, default=2)
    ap.add_argument('--max-space-depth', type=int, default=6)
    args = ap.parse_args()
    core.require(args.precision >= 192 and args.theta_terms >= 3 and args.space_order >= 8
                 and args.time_order >= 4 and args.beta_order >= 20,
                 'Minimum reviewed arithmetic and approximation parameters')
    core.require(0 <= args.t_left < args.t_right <= 1 and args.x_left >= 7
                 and args.x_right > args.x_left and args.time_slabs > 0
                 and args.max_time_depth >= 0 and args.max_space_depth >= 0, 'Domain and subdivision parameters')
    # Exact dyadic parameter balls avoid hidden endpoint inflation.
    for endpoint in (args.t_left, args.t_right, (args.t_right-args.t_left)/args.time_slabs):
        core.require(endpoint.denominator & (endpoint.denominator-1) == 0,
                     'Initial time cover must have exact dyadic endpoints')
    ctx.prec = args.precision
    started = time.monotonic()
    checks, controls = core.exact_controls()
    sources = {}
    def source(tl,tr):
        key = (tl,tr)
        if key not in sources:
            sources[key] = SlabSource(args.theta_terms, args.precision, args.space_order,
                                      args.time_order, args.beta_order, tl, tr)
        return sources[key]
    dt = (args.t_right-args.t_left)/args.time_slabs
    stack = [(args.t_left+i*dt, args.t_left+(i+1)*dt, Fraction(x), Fraction(x+1), 0, 0)
             for i in range(args.time_slabs) for x in range(args.x_left,args.x_right)]
    cells = []
    while stack:
        tl,tr,xl,xr,td,xd = stack.pop()
        cell = analyze(source(tl,tr), tl,tr,xl,xr,td,xd)
        unresolved = any(o['classification'] == 'unresolved' for o in cell['observations'])
        norm_unresolved = all(lower(v) <= 0 <= upper(v)
                              for v in cell['genuine_four_jets'][:2])
        needs_refinement = unresolved or norm_unresolved
        if needs_refinement and td < args.max_time_depth:
            middle = (tl+tr)/2
            stack.extend([(tl,middle,xl,xr,td+1,xd), (middle,tr,xl,xr,td+1,xd)])
        elif needs_refinement and xd < args.max_space_depth:
            middle = (xl+xr)/2
            stack.extend([(tl,tr,xl,middle,td,xd+1), (tl,tr,middle,xr,td,xd+1)])
        else:
            cells.append(cell)
    cells.sort(key=lambda c: (Fraction(c['t'][0]), Fraction(c['t'][1]), Fraction(c['x'][0])))
    times = exact_cover(cells,args.t_left,args.t_right,Fraction(args.x_left),Fraction(args.x_right))
    branches = branch_cover(cells,times)
    totals = {str(j): dict(Counter(c['observations'][j]['classification'] for c in cells)) for j in (0,1)}
    unresolved = [{'t':c['t'],'x':c['x'],'j':o['j']} for c in cells for o in c['observations']
                  if o['classification'] == 'unresolved']
    margins = {str(j): [o['correlated_cross_term_surplus_L_P_minus_payment']
                       for c in cells for o in c['observations']
                       if o['j']==j and o['classification'].startswith('stationary_signed')] for j in (0,1)}
    minima = {j:min(lower(v) for v in vv) if vv else None for j,vv in margins.items()}
    first_source = next(iter(sources.values()))
    source_records = []
    for (tl,tr),s in sorted(sources.items()):
        source_records.append({'t':[str(tl),str(tr)], 'time_center':str((tl+tr)/2),
                               'time_radius':str((tr-tl)/2), 'moment_majorant_time':str(tr),
                               'max_returned_jet_quadrature_radius':compact(s.jet_quadrature_max_radius),
                               'max_returned_moment_quadrature_radius':compact(s.moment_quadrature_max_radius),
                               'max_complete_retained_source_integration_tail':compact(s.source_tail_max),
                               'channel_absolute_moments_at_tmax':[[compact(v) for v in mm] for mm in s.moments]})
    # Shared payments are mathematically identical for a fixed slab/radius
    # (Taylor) or fixed left height (all-index error). Store them once.
    parameter_payments, parameter_index = [], {}
    index_payments, index_index = [], {}
    packed_cells = []
    gap_candidates = []
    for c in cells:
        radius = (Fraction(c['x'][1])-Fraction(c['x'][0]))/2
        key = tuple(c['t'])+(str(radius),)
        payments = {'raw_source_parameter_Taylor_payments':c['raw_source_parameter_Taylor_payments'],
                    'complete_Gaussian_transform_Taylor_payments':c['complete_Gaussian_transform_Taylor_payments']}
        if key not in parameter_index:
            parameter_index[key] = len(parameter_payments)
            parameter_payments.append({'t':c['t'],'space_radius':str(radius),**payments})
        else:
            core.require(all(parameter_payments[parameter_index[key]][k] == v for k,v in payments.items()),
                         'Identical shared parameter payments')
        error_key = c['x'][0]
        if error_key not in index_index:
            index_index[error_key] = len(index_payments)
            index_payments.append({'x_left':error_key,'complete_compensated_four_jet_errors':c['complete_compensated_four_jet_errors']})
        else:
            core.require(index_payments[index_index[error_key]]['complete_compensated_four_jet_errors']
                         == c['complete_compensated_four_jet_errors'], 'Identical shared complete-index errors')
        pc = {k:v for k,v in c.items() if k not in ('raw_source_parameter_Taylor_payments',
              'complete_Gaussian_transform_Taylor_payments','complete_compensated_four_jet_errors',
              'compensated_aggregate_jets')}
        pc['parameter_Taylor_payment_reference'] = parameter_index[key]
        pc['complete_index_payment_reference'] = index_index[error_key]
        if any(o['classification'] != 'stationarity_excluded' for o in c['observations']):
            pc['compensated_aggregate_jets'] = c['compensated_aggregate_jets']
        packed_cells.append(pc)
        def distance(ball):
            return max(Fraction(0),lower(ball),-upper(ball))
        gap_candidates.append((sum(distance(v)**2 for v in c['genuine_four_jets'][:2]), c['t'], c['x']))
    gap_squared,gap_t,gap_x = min(gap_candidates,key=lambda v:v[0])
    # Directed rational square root with denominator 2^128; no norm division.
    gap_scale = 1 << 128
    gap_lower = Fraction(isqrt(gap_squared.numerator*gap_scale**2//gap_squared.denominator),gap_scale)
    core.require(gap_lower**2 <= gap_squared, 'Exact rational genuine norm lower bound')
    dep = Path(core.__file__)
    unresolved_norm = [{'t':c['t'],'x':c['x']} for c in cells
                       if all(lower(v) <= 0 <= upper(v)
                              for v in c['genuine_four_jets'][:2])]
    status = 'PASS' if not unresolved and gap_lower > 0 else 'PARTIAL_UNRESOLVED'
    record = {'schema':'inv21-correlated-source-height-extension-v1', 'date':'2026-10-14',
              'provenance':{'prepared_for':'Edward Baker','llm_assistance':'substantial',
                            'recorded_model':'gpt-6.1-sol (Codex)','reasoning_effort':'ultra'},
              'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,
                         'seconds':round(time.monotonic()-started,3)},
              'checker':{'file':Path(__file__).name,'sha256':sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_reviewed_source':{'file':dep.name,'sha256':sha256(dep.read_bytes()).hexdigest()},
              'precision_bits':args.precision,
              'enclosure_encoding':'[[lower_mantissa,lower_exponent],[upper_mantissa,upper_exponent]]; endpoint=mantissa*2^exponent',
              'domain':{'t':[str(args.t_left),str(args.t_right)],'x':[str(args.x_left),str(args.x_right)]},
              'parameters':{'K':2,'N':args.theta_terms,'source_cutoff':'1',
                            'initial_time_slabs':args.time_slabs,'initial_x_width':'1',
                            'space_Taylor_order':args.space_order,'time_Taylor_order':args.time_order,
                            'Gaussian_Taylor_order':args.beta_order,'max_time_bisection_depth':args.max_time_depth,
                            'max_space_bisection_depth':args.max_space_depth,
                            'subdivision_priority':'time before space; subdivide cells with unresolved stationary signs or direct norm floor'},
              'complete_index_tail':{'valid_time_domain':['0','1'], 'formula':'manuscript (14.3)-(14.4), K=2; epsilon_j=C_j/x_left^4',
                                     'norm_constants_C_j':[compact(v) for v in first_source.tail_norms],
                                     'beta_L1_majorants_B_jk':[[compact(v) for v in row] for row in first_source.beta_norms]},
              'quadrature':{'method':'Acb validated integral of entire retained source on [0,1], plus full concavity tail',
                            'requested_tolerance_bits':args.precision-48,'eval_limit':100000,'depth_limit':30},
              'source_time_slabs':source_records,'exact_checks':checks,'shifted_heat_collision_controls':controls,
              'exact_cover_checks':{'all_endpoints_exact_dyadic':True,'elementary_closed_time_slabs':len(times)-1,
                                    'gap_free_spatial_partition_on_every_time_slab':True,
                                    'full_requested_closed_rectangle_covered':True},
              'cell_count':len(cells),'observation_totals':totals,'unresolved_sign_cells':unresolved,
              'unresolved_direct_norm_cells':unresolved_norm,
              'minimum_stationary_surplus_exact_rational':{j:str(v) for j,v in minima.items()},
              'strict_stationary_surplus_checks':{j:v is None or v>0 for j,v in minima.items()},
              'regular_stationary_branch_windows':branches,
              'unresolved_branch_windows':[b for b in branches if not b['uniform_unique_regular_branch']],
              'shared_parameter_Taylor_payments':parameter_payments,
              'shared_complete_index_payments':index_payments,
              'uniform_genuine_norm_gap':{'definition':'sqrt(H^2+H_x^2)',
                   'method':'Minimum over every closed cover cell of sqrt(dist(genuine_h0_ball,0)^2+dist(genuine_h1_ball,0)^2). No division.',
                   'minimum_cellwise_squared_lower_bound':str(gap_squared),
                   'rational_norm_lower_bound':str(gap_lower),
                   'strict_positive':bool(gap_lower>0),'minimizing_cell':{'t':gap_t,'x':gap_x}},
              'cells':packed_cells,'status':status,
              'established_claim':('Every point of the full requested closed rectangle satisfies h_(j+1)=0 => L_j(H)>0 for j=0,1.'
                                   if status=='PASS' else 'Only individually reported resolved cells are certified; no claim across unresolved cells.'),
              'error_payments':['complete omitted theta indices for all physical jets k=0..3',
                                'validated returned retained-source quadrature radii and all rounding',
                                'complete retained-source integration tail beyond u=1',
                                'raw heat time Taylor remainder from positive moments at slab maximum time',
                                'space Taylor remainder for each retained time term',
                                'entire Gaussian compensation transforms and full Gaussian moment Taylor remainder',
                                'explicit affine time-dependent endpoint compensation retaining finite-channel heat residual',
                                'exact D+X aggregate identity and complete genuine-stationary remainder payment',
                                'retained raw jets summed before shared Taylor monomials; per-channel remainders still added'],
              'limitations':['Bounded height domain; no all-height relative estimate or global RH conclusion.',
                             'Only complete H obeys heat; compensated finite channels carry the explicit residual.',
                             'D and X can be separately negative; the exact correlated sum decides signs.']}
    payload = json.dumps(record,sort_keys=True,separators=(',',':'))+'\n'
    core.require(len(payload.encode()) < 1048576, 'Small certificate must stay below one MiB')
    args.output.write_text(payload)
    print(json.dumps({'status':status,'cell_count':len(cells),'source_time_slabs':len(sources),
                      'observation_totals':totals,'unresolved_sign_cells':len(unresolved),
                      'unresolved_direct_norm_cells':len(unresolved_norm),
                      'unresolved_branch_windows':len(record['unresolved_branch_windows']),
                      'minima_decimal':{j:float(v) if v else None for j,v in minima.items()},
                      'uniform_genuine_norm_lower_bound_decimal':float(gap_lower),
                      'strict_stationary_surplus_checks':record['strict_stationary_surplus_checks'],
                      'seconds':record['runtime']['seconds'],'record_bytes':len(payload.encode())},indent=2))
    if unresolved or gap_lower <= 0:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
