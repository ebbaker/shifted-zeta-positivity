#!/usr/bin/env python3
"""Planning table for the activation section of the working manuscript.

Prepared for Edward Baker with LLM assistance, 18 October 2026. Model:
Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max; the serving model may differ. Standard library only.

This program supports Section 7 of
manuscript/sharp_finite_sum_bounds/main.tex (the activation lemma, the
bound for the activation sums, the mesh criterion and Table 4). It does
two things.

1. Side conditions of the activation-sum lemma, in 50-digit Decimal
   arithmetic: on every leg, g_a^2 m^{y0} < 1/10 for N_a <= m in the leg
   (so the closed form of W_g(1, m^{y0}) applies), and
   sigma_a - y0 - (t/2) log N > 0.3 for N_a <= N in the leg (so the
   endpoint cap lemma applies to every subrange), together with the
   rounded constants quoted in the manuscript's proof.

2. Floating planning (float64, not a certificate). The mesh rows and their
   float64 floors L_{N_i}(y0) are read from the hash-pinned record of the
   round-one review checks (section F, cap-lemma mesh, mixed plan). For each
   span [N_i, E_i] the activation bound delta_i of the lemma is recomputed
   with a single cap (J = 1) and compared with the record; on the last span
   of leg 3, where one cap does not suffice, the lemma is applied on a
   partition into J geometric pieces. The table, the margins
   L - delta - 3e-7 and the tiling of every leg are checked.

The program exits with status 1 if any check fails. It reads only the
review record beside it and writes only --output.

Usage, from this folder:
  python3 -I activation_plan_claude_20261018.py --output /tmp/ACTIVATION_PLAN.json
"""
import argparse
import hashlib
import json
import math
import platform
import sys
import time
from decimal import Decimal, getcontext
from pathlib import Path

RECORD = 'REVIEW_CHECKS_CLAUDE_20261017.json'
RECORD_SHA = 'a89771dcb61ddbcf494de6ec3f157b3cf4f90aa6ac7b8439a97db53969f009a7'
LEGS = [((2, 3, 5, 7, 11), 690988, 728999), ((2, 3, 5, 7), 729000, 818999),
        ((2, 3, 5), 819000, 1027999), ((2, 3), 1028000, 3840000)]
ALLOWANCE = 3e-7
J_LAST = 16
J_SCAN = (1, 2, 4, 8, 16, 32, 64)
FAILURES = []


def check(ok, msg):
    if not ok:
        FAILURES.append(msg)
    return bool(ok)


# ----------------------------------------------------------------------------
# 1. Side conditions, 50-digit Decimal
# ----------------------------------------------------------------------------
def side_conditions():
    getcontext().prec = 50
    t = Decimal(157) / 1000
    y0 = (Decimal(87677) / Decimal(2500000)).sqrt()

    def q(n):
        return Decimal(n) * n - t / 16

    legs = []
    for P, a, b in LEGS:
        ratio = Decimal(b) / q(a)
        g2m = (y0 / 25 + y0 * ratio.ln()).exp()        # e^{y0/25} (b/q_a)^{y0}
        # sigma_a - y0 - (t/2) log N >= (1-y0)/2 - (t/2) log(N/N_a) - 1e-13 on the leg
        cap_gap = (1 - y0) / 2 - t / 2 * (Decimal(b) / a).ln() - Decimal('1e-13')
        legs.append(dict(leg=len(legs), primes=list(P), first=a, last=b,
                         last_over_q_first=f'{ratio:.6e}', g2_m_y0_max=f'{g2m:.6f}',
                         cap_validity_gap_min=f'{cap_gap:.6f}', last_over_first=f'{Decimal(b) / a:.6f}'))
        check(g2m < Decimal('0.1'), f'leg {a}: g^2 m^y0 bound {g2m} not below 0.1')
        check(cap_gap > Decimal('0.3'), f'leg {a}: cap validity gap {cap_gap} not above 0.3')
        check(ratio < Decimal('3.7e-6'), f'leg {a}: N_last/q(N_first) not below 3.7e-6')
        check(Decimal(b) / a < Decimal('3.74'), f'leg {a}: N_last/N_first not below 3.74')
    quoted = dict(
        y0=f'{y0:.12f}',
        y0_between_0187_and_01873=bool(Decimal('0.187') < y0 < Decimal('0.1873')),
        y0_over_25_below_00075=bool(y0 / 25 < Decimal('0.0075')),
        one_minus_y0_half=f'{(1 - y0) / 2:.6f}',
        t_half_log_374=f'{t / 2 * Decimal("3.74").ln():.6f}',
        e00075_times_37e6_pow_0187=f'{(Decimal("0.0075") + Decimal("0.187") * Decimal("3.7e-6").ln()).exp():.6f}',
    )
    check(quoted['y0_between_0187_and_01873'], 'y0 not in (0.187, 0.1873)')
    check(quoted['y0_over_25_below_00075'], 'y0/25 not below 0.0075')
    check(Decimal(quoted['one_minus_y0_half']) > Decimal('0.406'), '(1-y0)/2 not above 0.406')
    check(Decimal(quoted['t_half_log_374']) < Decimal('0.104'), '(t/2) log 3.74 not below 0.104')
    check(Decimal(quoted['e00075_times_37e6_pow_0187']) < Decimal('0.1'), 'e^0.0075 (3.7e-6)^0.187 not below 0.1')
    return dict(arithmetic='50-digit Decimal', legs=legs, quoted_constants=quoted)


# ----------------------------------------------------------------------------
# 2. Floating planning
# ----------------------------------------------------------------------------
T = 157 / 1000
Y0 = math.sqrt(87677 / 2500000)


def scalars(N):
    q = N * N - T / 16
    x = 4 * math.pi * q
    lq = math.log(q)
    g = math.exp(Y0 / 50 - Y0 / 2 * lq)
    inner = 1 - 3 * Y0 + 4 * Y0 * (1 + Y0) / (x * x)
    sig = (1 + Y0) / 2 + T / 4 * lq - T * max(inner, 0.0) / (2 * x * x)
    kap = T * Y0 / (2 * (x - 6))
    return g, sig, kap


def cap(a, b, s):
    """Endpoint cap on (a, b]: log(b/a) max_{u in {a, b}} exp((1-s) log u + (t/4) log^2 u)."""
    assert b > a and s > T / 2 * math.log(b)
    f = lambda u: math.exp((1 - s) * math.log(u) + T / 4 * math.log(u) ** 2)
    return math.log(b / a) * max(f(a), f(b))


def delta_bound(Na, Nb, J):
    """c_a S(sigma_a) + g_a (c_a + eps_a) S(sigma_a - y0), each S bounded by caps on J geometric pieces."""
    g, sig, kap = scalars(Na)
    assert g * g * Nb ** Y0 <= 0.1
    c = (1 - g) / (1 + g)
    eps = kap * math.log(Nb) * Nb ** kap
    pts = sorted({Na, Nb} | {int(round(Na * (Nb / Na) ** (j / J))) for j in range(1, J)})
    S1 = math.fsum(cap(u, v, sig) for u, v in zip(pts, pts[1:]))
    S2 = math.fsum(cap(u, v, sig - Y0) for u, v in zip(pts, pts[1:]))
    return c * S1 + g * (c + eps) * S2, len(pts) - 1


def planning(record):
    F = record['F_activation_planning_FLOAT']
    capmesh = F['sharp_t157_cap_activation']
    mixed = F['sharp_t157_cap_then_direct_last_span']
    spans = []
    last_span_scan = None
    for leg, mx in zip(capmesh, mixed):
        li = leg['leg']
        P, first, last = LEGS[li]
        check(leg['N'] == [first, last], f'leg {li} range differs from the manuscript table')
        keep = [p for p in leg['mesh'] if p['Na'] in mx['rows_list']]
        check([p['Na'] for p in keep] == mx['rows_list'], f'leg {li}: mixed rows are not a prefix of the cap mesh')
        for i, p in enumerate(keep):
            Na, L = p['Na'], p['L']
            Eb = keep[i + 1]['Na'] - 1 if i + 1 < len(keep) else last
            d1, _ = delta_bound(Na, Eb, 1)
            row = dict(leg=li, N=Na, E=Eb, L_float=L, delta_single_cap=d1)
            if Eb == p['Nb']:
                check(abs(d1 - p['delta']) <= 1e-12 * p['delta'],
                      f'span {Na}: single-cap bound {d1} differs from the review record {p["delta"]}')
                row.update(delta=d1, method='cap, J=1', review_record_delta=p['delta'])
            else:
                scan = {J: delta_bound(Na, Eb, J)[0] for J in J_SCAN}
                dJ, pieces = delta_bound(Na, Eb, J_LAST)
                row.update(delta=dJ, method=f'cap, J={pieces} geometric pieces',
                           review_record_direct_sum=mx['last_span_exact_delta'])
                last_span_scan = dict(leg=li, N=Na, E=Eb, L_float=L,
                                      delta_by_J={str(J): v for J, v in scan.items()},
                                      margin_by_J={str(J): L - v - ALLOWANCE for J, v in scan.items()},
                                      review_record_direct_sum=mx['last_span_exact_delta'])
                check(dJ >= mx['last_span_exact_delta'], 'partitioned cap below the direct sum')
            row['margin'] = L - row['delta'] - ALLOWANCE
            check(row['margin'] > 0, f'span {Na}..{Eb}: nonpositive floating margin')
            spans.append(row)
        legspans = [s for s in spans if s['leg'] == li]
        check(legspans[0]['N'] == first and legspans[-1]['E'] == last, f'leg {li}: spans do not reach the leg ends')
        check(all(v['N'] == u['E'] + 1 for u, v in zip(legspans, legspans[1:])), f'leg {li}: spans do not tile')
    counts = [sum(1 for s in spans if s['leg'] == li) for li in range(4)]
    ratios = [spans[i + 1]['L_float'] / spans[i]['L_float'] for i in range(len(spans) - 1)
              if spans[i + 1]['leg'] == spans[i]['leg']]
    return dict(spans=spans, rows_per_leg=counts, total_rows=sum(counts),
                largest_row=max(s['N'] for s in spans),
                min_margin=min(s['margin'] for s in spans),
                floor_ratio_range=[min(ratios), max(ratios)],
                first_span_length=spans[0]['E'] - spans[0]['N'] + 1,
                last_span_partition_scan=last_span_scan)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    t0 = time.perf_counter()
    here = Path(__file__).resolve().parent
    raw = (here / RECORD).read_bytes()
    if hashlib.sha256(raw).hexdigest() != RECORD_SHA:
        raise SystemExit('review record hash mismatch')
    rec = dict(
        date='2026-10-18', prepared_for='Edward Baker',
        model='Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork, reasoning effort max; '
              'serving model may differ',
        scope=('Side conditions of the activation-sum lemma (Decimal) and the floating planning table of the '
               "manuscript's Section 7. The planning values are float64 and are not a certificate: no row other "
               'than N=690988 is certified and no activation bound is evaluated outwardly.'),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input={RECORD: RECORD_SHA},
        python=platform.python_version(), platform=platform.platform(),
        allowance=ALLOWANCE, partition_pieces_last_span=J_LAST,
    )
    rec['side_conditions'] = side_conditions()
    rec['planning_FLOAT'] = planning(json.loads(raw))
    rec['failures'] = FAILURES
    rec['passed'] = not FAILURES
    rec['seconds'] = time.perf_counter() - t0
    a.output.write_text(json.dumps(rec, indent=1) + '\n')
    p = rec['planning_FLOAT']
    print(json.dumps(dict(passed=rec['passed'], rows_per_leg=p['rows_per_leg'], largest_row=p['largest_row'],
                          min_margin=p['min_margin'], failures=FAILURES)))
    return 0 if rec['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
