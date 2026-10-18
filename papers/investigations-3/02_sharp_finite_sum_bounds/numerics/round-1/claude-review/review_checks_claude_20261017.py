#!/usr/bin/env python3
"""Support computations for the round-one cross-model review of Project 02.

Prepared for Edward Baker with LLM assistance, 17 October 2026. Model:
Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. Standard library only. Nothing here alters the round's records.

Sections (labels in the record say which outputs are exact, interval,
floating or planning):

  A  SHA-256 digests of the reviewed files and of the inherited helpers.
  B  Independent float64 row values, with an enumeration order different
     from the round's pilot (gcd class outer, cofactor inner) and math.fsum:
     B1 sharp weight, t=157/1000, N=690988, against the certified pilot
        enclosure; B2 plain weight, t=129/800, N=690988, against the audit's
        certified plain row; B3 the audit's floating table (sharp at
        t=129/800; plain at t=157/1000 at the four leg starts);
     B4 the first-row boundary in t (sharp L < 0 at t=0.1569).
  C  The transfer-gate numerator (8) of Note 02, evaluated by the engine on
     point boxes, against a finite-difference derivative of the summand
     computed from the definitions (Decimal, 80 digits) at actual integer
     points of every pattern; also the absolute-sum numerator (9).
  D  Fault injection in the engine (source modified in memory only):
     D1 removing the n^-sigma decay term must produce strictly positive
        numerators at actual integer points;
     D2 (with --slack) halving the slope bound sigma' >= 1/2 to 1/4 as an
        interval slack probe on legs 3, 2 and 1;
     D3 (with --slack) a float64 scan of the required slope over actual
        integer terms (a sampled supremum, not a certificate).
  E  Exact rational checks of the seminorm properties of U_g used by the
     activation lemma of the review (Section 6 there), and of the closed form
     (1-g)U_g(1,a) = (1-g)(1+ga)/(1+g) for a >= 1, g^2 a <= 1.
  F  Activation-lemma planning in float64: greedy meshes per leg, with exact
     activation sums and with cap-lemma bounds, for the sharp lane at
     t=157/1000 and for the inherited plain lane at t=129/800.
     PLANNING ONLY: floating values, not a certificate.
  G  Contract arithmetic: the first window contains X+sqrt(1-y0^2) at the
     new time (Decimal, 60 digits); exact rational checks of the tail y-box,
     y1^2 = 1-2t, and the barrier containment numbers.

Exit status 1 if an exact check fails, a comparison leaves its tolerance,
or a negative control fails to fail.
"""
import argparse, hashlib, importlib.util, itertools, json, math, platform, sys, time, types
from decimal import Decimal as Dc, Context, ROUND_HALF_EVEN, localcontext
from fractions import Fraction as Fr
from pathlib import Path

PROJECT = Path('papers/investigations-3/02_sharp_finite_sum_bounds')
R1 = PROJECT / 'numerics/round-1'
ENGINE = R1 / 'check_sharp_y_transfer_gate.py'
ENGINE_SHA = 'aa6c73e0aa6672b5e6706f704b0a8dda42f1a572d9cd2a3766c91a61bebf6792'
PILOT_RECORD = R1 / 'SHARP_PILOT_RECORD_20261017.json'
DIGEST_FILES = [
    PROJECT / 'README.md', PROJECT / 'DRAFT_HISTORY.md',
    PROJECT / 'research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md',
    PROJECT / 'notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md',
    PROJECT / 'notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md',
    PROJECT / 'manuscript/sharp_finite_sum_bounds/main.tex',
    R1 / 'certify_sharp_pilot.py', R1 / 'check_sharp_y_transfer_gate.py',
    R1 / 'complete_sharp_y_transfer_gate.py', R1 / 'check_gate_arithmetic.py',
    R1 / 'check_t157_tail_budget.py', R1 / 'check_transfer_counterexample.py',
    R1 / 'SHARP_PILOT_RECORD_20261017.json', R1 / 'SHARP_Y_TRANSFER_GATE_RECORD_20261017.json',
    R1 / 'SHARP_Y_TRANSFER_COMPLETION_RECORD_20261017.json',
    R1 / 'TAIL_T157_M600000_RECORD.json', R1 / 'TAIL_T157_M153814_RECORD.json',
    Path('papers/investigations-2/newman_certificate_audit/numerics/check_finite_row_certified_replay.py'),
    Path('papers/investigations-2/newman_certificate_audit/numerics/check_tail_and_uniform_error_budget.py'),
]
LEGS = [((2, 3, 5, 7, 11), 690988, 728999), ((2, 3, 5, 7), 729000, 818999),
        ((2, 3, 5), 819000, 1027999), ((2, 3), 1028000, 3840000)]
T_NEW = 157 / 1000
T_OLD = 129 / 800
Y0SQ = Fr(87677, 2500000)
Y0 = math.sqrt(87677 / 2500000)
E_NEW = 3e-7                       # the round's declared allowance (E_max < 2.829444e-7)
E_OLD = 2.33494905212337849e-7     # the inherited E_max at t0 (audit note 4)
AUDIT_PLAIN_690988 = 7.9136674559413e-07   # audit note 3, certified lower end
FAILURES = []


def fail(msg):
    FAILURES.append(msg)


# ----------------------------------------------------------------------------
# B, F: float64 rows (independent code path)
# ----------------------------------------------------------------------------
def scalars(N, t, y):
    q = N * N - t / 16
    x = 4 * math.pi * q
    lq = math.log(q)
    g = math.exp(y / 50 - y / 2 * lq)
    inner = 1 - 3 * y + 4 * y * (1 + y) / (x * x)
    sig = (1 + y) / 2 + t / 4 * lq - t * max(inner, 0.0) / (2 * x * x)
    kap = t * y / (2 * (x - 6))
    return g, sig, kap


def row(N, P, t, y, weight, scal=None):
    """L_N for the sharp weight (1-g)U_g or the plain weight |B|+g|A|, float64.
    With scal=(g, sigma, kappa) the frozen scalars of another index are used (hybrid row)."""
    g, sig, kap = scal if scal is not None else scalars(N, t, y)
    t4 = t / 4
    log, exp = math.log, math.exp
    bt = [0.0] * (N + 1)
    ay = [0.0] * (N + 1)
    ks = [0.0] * (N + 1)
    for m in range(1, N + 1):
        l = log(m)
        b = exp(t4 * l * l)
        bt[m] = b
        ay[m] = b * exp(y * l)
        ks[m] = exp(-sig * l)
    n = len(P)
    full = (1 << n) - 1
    val = [math.prod(P[i] for i in range(n) if s >> i & 1) for s in range(1 << n)]
    bp = [exp(t4 * log(p) ** 2) for p in P]
    lam = [(-1) ** bin(s).count('1') * math.prod(bp[i] for i in range(n) if s >> i & 1)
           for s in range(1 << n)]
    M = math.fsum(abs(lam[s]) * val[s] ** (-sig) for s in range(1 << n))
    pm = bytearray(N + 1)
    for i, p in enumerate(P):
        for k in range(p, N + 1, p):
            pm[k] |= 1 << i
    g2 = g * g
    parts = []
    NT = 0
    for G in range(1 << n):
        comp = full & ~G
        pairs = []
        s = G
        while True:
            pairs.append((val[s], lam[G & ~s]))
            if s == 0:
                break
            s = (s - 1) & G
        pairs.sort()
        acc = []
        for k in range(1, N + 1):
            if pm[k] & comp or (k == 1 and G == 0):
                continue
            B = A = 0.0
            for e, l in pairs:
                m = e * k
                if m > N:
                    break
                B += l * bt[m]
                A += l * ay[m]
            if weight == 'sharp':
                acc.append((abs(B - g2 * A) + g * abs(A - B)) * ks[k])
            else:
                acc.append((abs(B) + g * abs(A)) * ks[k])
        NT += len(acc)
        Gs = val[G] ** (-sig)
        parts.append(Gs * math.fsum(acc) * ((1 - g) / (1 - g2) if weight == 'sharp' else 1.0))
    S = math.fsum(parts)        # unnormalized mass: (1-g)V (sharp) or plain mass
    C = math.fsum(bt[m] * math.expm1(kap * log(m)) * exp((y - sig) * log(m)) for m in range(2, N + 1))
    L = (1 - g - S) / M - g * C
    return dict(N=N, P=list(P), t=t, weight=weight, g=g, sigma=sig, kappa=kap, M=M, S=S, C=C, L=L, NT=NT)


def act_weight(g, a, weight):
    if weight == 'sharp':
        return (abs(1 - g * g * a) + g * abs(a - 1)) / (1 + g)      # (1-g) U_g(1,a)
    return 1 + g * a


def greedy_span_exact(Na, Nend, t, y, weight, budget):
    """Largest Nb <= Nend with Delta(Na,Nb) < budget, Delta from the exact activation sum."""
    g, sig, kap = scalars(Na, t, y)
    t4 = t / 4
    tot = 0.0
    m = Na
    while m < Nend:
        mm = m + 1
        l = math.log(mm)
        b = math.exp(t4 * l * l - sig * l)
        a = math.exp(y * l)
        inc = b * act_weight(g, a, weight) + g * b * math.expm1(kap * l) * a
        if tot + inc >= budget:
            break
        tot += inc
        m = mm
    return m, tot


def cap(a, N, s, t):
    """Polymath Lemma 8.2 on (a, N]: sum b_t(n) n^-s <= log(N/a) max_{u in {a,N}} exp((1-s)log u + (t/4)log^2 u)."""
    if N <= a:
        return 0.0
    assert s > t / 2 * math.log(N)
    f = lambda u: math.exp((1 - s) * math.log(u) + t / 4 * math.log(u) ** 2)
    return math.log(N / a) * max(f(a), f(N))


def delta_cap(Na, Nb, t, y, weight):
    """Upper bound for Delta(Na,Nb) by the cap lemma (float; planning only)."""
    g, sig, kap = scalars(Na, t, y)
    if weight == 'sharp':
        # (1-g)U_g(1,a) = (1-g)(1+g a)/(1+g) for a>=1, g^2 a<=1 (checked in E)
        assert g * g * Nb ** y <= 1
        c0, c1 = (1 - g) / (1 + g), g * (1 - g) / (1 + g)
    else:
        c0, c1 = 1.0, g
    kk = kap * math.log(Nb) * Nb ** kap        # m^k - 1 <= k log m m^k <= this
    return c0 * cap(Na, Nb, sig, t) + (c1 + g * kk) * cap(Na, Nb, sig - y, t)


def greedy_span_cap(Na, Nend, t, y, weight, budget):
    lo, hi = Na, Nend
    if delta_cap(Na, Nend, t, y, weight) < budget:
        return Nend
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if delta_cap(Na, mid, t, y, weight) < budget:
            lo = mid
        else:
            hi = mid
    return lo


def mesh(t, y, E, weight, mode, legs, max_rows=400):
    out = []
    for li in legs:
        P, a, b = LEGS[li]
        Na = a
        pts = []
        while Na <= b:
            r = row(Na, P, t, y, weight)
            L = r['L']
            if L <= E:
                pts.append(dict(Na=Na, L=L, Nb=None))
                fail(f'F: {weight} t={t} leg {li} mesh row {Na} has L={L} <= allowance')
                break
            if mode == 'exact':
                Nb, d = greedy_span_exact(Na, b, t, y, weight, L - E)
            else:
                Nb = greedy_span_cap(Na, b, t, y, weight, L - E)
                d = delta_cap(Na, Nb, t, y, weight)
            pts.append(dict(Na=Na, L=L, Nb=Nb, delta=d))
            if Nb >= b or len(pts) > max_rows:
                break
            Na = Nb + 1
        out.append(dict(leg=li, primes=list(P), N=[a, b], rows=len(pts), mesh=pts,
                        covered=bool(pts and pts[-1]['Nb'] is not None and pts[-1]['Nb'] >= b)))
    return out


# ----------------------------------------------------------------------------
# C, D: engine
# ----------------------------------------------------------------------------
def load_engine(repo, src_override=None):
    path = repo / ENGINE
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != ENGINE_SHA:
        raise RuntimeError('transfer-gate engine hash mismatch')
    m = types.ModuleType('gate_engine_readonly')
    m.__file__ = str(path)
    src = raw.decode() if src_override is None else src_override(raw.decode())
    exec(compile(src, 'gate_engine_readonly', 'exec'), m.__dict__)
    return m


HC = Context(prec=80, rounding=ROUND_HALF_EVEN)
TD = Dc('0.157')


def summand(N, n, P, y):
    """U_{g_N(y)}(B,A(y)) n^-sigma with sigma' = 1/2 exactly (the kink term, below 1e-26, omitted),
    from the definitions; also returns b_t(n) n^-sigma, g and the two normalized branches."""
    with localcontext(HC):
        q = Dc(N) * N - TD / 16
        lq = HC.ln(q)
        g = HC.exp(y / 50 - (y / 2) * lq)
        sig = (1 + y) / 2 + (TD / 4) * lq
        B = Dc(0)
        A = Dc(0)
        for mask in range(1 << len(P)):
            d = 1
            lam = Dc(1)
            for i, p in enumerate(P):
                if mask >> i & 1:
                    d *= p
                    lam *= -HC.exp((TD / 4) * HC.ln(Dc(p)) ** 2)
            if n % d == 0 and n // d <= N:
                lm = HC.ln(Dc(n // d))
                b = HC.exp((TD / 4) * lm * lm)
                B += lam * b
                A += lam * b * HC.exp(y * lm)
        um = abs(B - g * A) / (1 - g)
        up = abs(B + g * A) / (1 + g)
        ln_n = HC.ln(Dc(n))
        w = HC.exp(-sig * ln_n)
        bn = HC.exp((TD / 4) * ln_n * ln_n)
        return max(um, up) * w, bn * w, g


def section_C(repo, rng_seed=20261017):
    import random
    m = load_engine(repo)
    rnd = random.Random(rng_seed)
    h = Dc('1e-30')
    stats = dict(points=0, kinds={}, accepted_with_positive_fd=0, active_single_branch_compared=0,
                 absolute_sum_compared=0, enclosure_misses=0, max_relative_mismatch='0', examples=[])
    worst = Dc(0)
    for idx in range(4):
        leg = m.Leg(idx)
        for p in leg.patterns:
            N = rnd.randint(leg.nlo, leg.nhi)
            lower = 2 if p.previous == 0 else p.previous * N + 1
            upper = p.top * N
            kl, kh = max(1, -(-max(lower, p.nmin) // p.G)), upper // p.G
            k = None
            for _ in range(400):
                cand = rnd.randint(kl, kh)
                if math.gcd(cand, leg.D // p.G) == 1:
                    k = cand
                    break
            if k is None:
                continue
            n = p.G * k
            if not (lower <= n <= upper and math.gcd(n, leg.D) == p.G and n >= 2):
                continue
            for y in (Dc('0.18728'), Dc('0.4'), Dc('0.8282')):
                v0, wn, g = summand(N, n, leg.P, y)
                v1, _, _ = summand(N, n, leg.P, y + h)
                fd = (v1 - v0) / h
                kind, detail = m.evaluate(leg, p, m.ln(m.I(N)), m.ln(m.I(n) / N), m.I(y))
                stats['points'] += 1
                stats['kinds'][kind] = stats['kinds'].get(kind, 0) + 1
                rec = dict(leg=idx, G=p.G, sector=[p.previous, p.top], N=N, n=n, y=str(y), kind=kind)
                if kind in ('active', 'absolute_sum', 'singleton', 'prime_zero') and fd > 0:
                    stats['accepted_with_positive_fd'] += 1
                    stats['examples'].append(dict(rec, problem='accepted but finite difference positive'))
                with localcontext(HC):
                    if kind == 'active' and len(detail['branches']) == 1:
                        e = detail['branches'][0]
                        target = fd * (1 + e * g) ** 2 / wn
                        lo, hi = (Dc(s) for s in detail['bounds'][str(e)])
                        stats['active_single_branch_compared'] += 1
                    elif kind == 'absolute_sum':
                        target = fd * (1 - g * g) / wn
                        lo, hi = (Dc(s) for s in detail['bound'])
                        stats['absolute_sum_compared'] += 1
                    else:
                        continue
                    tol = Dc('1e-24') * (abs(lo) + abs(hi) + 1)
                    if not (lo - tol <= target <= hi + tol):
                        stats['enclosure_misses'] += 1
                        stats['examples'].append(dict(rec, problem='numerator does not enclose scaled FD derivative',
                                                      target=str(target), bounds=[str(lo), str(hi)]))
                    rel = abs(target - (lo + hi) / 2) / max(abs(target), Dc('1e-40'))
                    if rel > worst:
                        worst = rel
    stats['max_relative_mismatch'] = str(worst)
    if stats['accepted_with_positive_fd'] or stats['enclosure_misses']:
        fail('C: engine numerator disagrees with the definition-based derivative')
    if stats['points'] < 900:
        fail('C: too few sample points')
    return stats


def rep_once(s, a, b):
    if s.count(a) != 1:
        raise RuntimeError('engine splice not unique: ' + a)
    return s.replace(a, b)


def variant_drop_decay(src):
    src = rep_once(src, "gate=d*dint(z,e*Tv)-((L/2)*d+e*ell*g)*z.abs()",
                   "gate=d*dint(z,e*Tv)-(e*ell*g)*z.abs()")
    return rep_once(src, "alt=dint(R,Rp)+dint(S,Sp)-(L/2-2*gg*ell/(1-gg))*(R.abs()+S.abs())",
                    "alt=dint(R,Rp)+dint(S,Sp)-(-2*gg*ell/(1-gg))*(R.abs()+S.abs())")


def variant_slope(sv):
    def f(src):
        src = rep_once(src, "gate=d*dint(z,e*Tv)-((L/2)*d+e*ell*g)*z.abs()",
                       f"gate=d*dint(z,e*Tv)-((L*I('{sv}'))*d+e*ell*g)*z.abs()")
        src = rep_once(src, "alt=dint(R,Rp)+dint(S,Sp)-(L/2-2*gg*ell/(1-gg))*(R.abs()+S.abs())",
                       f"alt=dint(R,Rp)+dint(S,Sp)-(L*I('{sv}')-2*gg*ell/(1-gg))*(R.abs()+S.abs())")
        # the analytic shortcuts assume the slope 1/2; route those cells through the interval test
        src = rep_once(src, "    if len(p.active)==1:return 'singleton',None\n", "")
        return rep_once(src, "    if p.previous==0 and p.G in leg.P and candidates==[p.G]:return 'prime_zero',None\n", "")
    return f


def summarize_leg(r):
    keep = ('leg', 'evaluated', 'accepted', 'unresolved_leaf_count', 'stop_reason', 'passed')
    out = {k: r[k] for k in keep}
    if r['unresolved_examples']:
        ex = r['unresolved_examples'][0]
        out['first_unresolved'] = dict(pattern=ex['pattern'], box=ex['box'], detail=ex['detail'])
    return out


def section_D(repo, slack, rng_seed=4):
    import random
    res = {}
    m = load_engine(repo, variant_drop_decay)
    rnd = random.Random(rng_seed)
    definite = 0
    seen = 0
    example = None
    for idx in (3, 0):
        leg = m.Leg(idx)
        for p in leg.patterns:
            N = rnd.randint(leg.nlo, leg.nhi)
            lower = 2 if p.previous == 0 else p.previous * N + 1
            kl, kh = max(1, -(-max(lower, p.nmin) // p.G)), (p.top * N) // p.G
            ks = [k for k in (rnd.randint(kl, kh) for _ in range(50)) if math.gcd(k, leg.D // p.G) == 1]
            if not ks:
                continue
            n = p.G * ks[0]
            for y in (Dc('0.18728'), Dc('0.8282')):
                kind, detail = m.evaluate(leg, p, m.ln(m.I(N)), m.ln(m.I(n) / N), m.I(y))
                seen += 1
                if kind == 'unresolved' and all(Dc(b[0]) > 0 for b in detail['bounds'].values()) \
                        and Dc(detail['absolute_sum'][0]) > 0:
                    definite += 1
                    if example is None:
                        example = dict(leg=idx, G=p.G, sector=[p.previous, p.top], N=N, n=n, y=str(y),
                                       bounds=detail['bounds'], absolute_sum=detail['absolute_sum'])
    res['D1_drop_decay_point_rejections'] = dict(points=seen, strictly_positive_numerators=definite,
                                                 first_example=example)
    if definite == 0:
        fail('D1: no actual point was rejected after removing the decay term (negative control did not fail)')
    if slack:
        m2 = load_engine(repo, variant_slope('0.25'))
        res['D2_slope_quarter'] = [summarize_leg(m2.certify_leg(i, 10 ** 6, 30000, 36)) for i in (3, 2, 1)]
        res['D3_required_slope_scan_FLOAT'] = slope_scan()
    return res


def slope_scan(ny=31, nk=40, edge=10):
    """Float64 diagnostic: sampled supremum over actual integer terms of the required slope
    s* = (d/dy log U)/log n, where U = U_{g_N(y)}(B,A(y)); the gate (2) needs s* <= 1/2.
    Samples: three indices per leg (first, middle, last), every pattern, the first and last
    `edge` admissible cofactors of each sector and `nk` log-spaced ones, `ny` values of y.
    A sampled supremum is a lower bound for the true supremum, not a certificate."""
    T, y0, y1 = 0.157, Y0, math.sqrt(0.686)
    ys = [y0 + (y1 - y0) * i / (ny - 1) for i in range(ny)]
    out = []
    for li, (P, a, b) in enumerate(LEGS):
        D = math.prod(P)
        bp = {p: math.exp(T / 4 * math.log(p) ** 2) for p in P}
        lamd = {}
        for r in range(len(P) + 1):
            for c in itertools.combinations(P, r):
                lamd[math.prod(c)] = (-1) ** r * math.prod(bp[p] for p in c)
        best = (-1e9, None)
        samples = 0
        for N in (a, (a + b) // 2, b):
            ell = 0.02 - 0.5 * math.log(N * N - T / 16)
            for G in sorted(lamd):
                divs = sorted(d for d in lamd if G % d == 0)
                for j, top in enumerate(divs):
                    prev = divs[j - 1] if j else 0
                    lo = 2 if prev == 0 else prev * N + 1
                    hi = top * N
                    kl, kh = max(1, -(-lo // G)), hi // G
                    if kl > kh:
                        continue
                    ok = lambda k: math.gcd(k, D // G) == 1 and G * k >= 2
                    ks = set()
                    k = kl
                    while k <= kh and len(ks) < edge:
                        if ok(k):
                            ks.add(k)
                        k += 1
                    k = kh
                    cnt = 0
                    while k >= kl and cnt < edge:
                        if ok(k):
                            ks.add(k)
                            cnt += 1
                        k -= 1
                    for i in range(nk):
                        kk = int(round(math.exp(math.log(kl) + (math.log(kh) - math.log(kl)) * i / (nk - 1))))
                        for k2 in (kk, kk + 1):
                            if kl <= k2 <= kh and ok(k2):
                                ks.add(k2)
                                break
                    for k in ks:
                        n = G * k
                        act = [(math.log(n // d), lamd[d]) for d in divs if n // d <= N]
                        if not act:
                            continue
                        terms = [(lm, l * math.exp(T / 4 * lm * lm)) for lm, l in act]
                        B = sum(c for _, c in terms)
                        ln_n = math.log(n)
                        for y in ys:
                            A = Ap = 0.0
                            for lm, c in terms:
                                e = c * math.exp(y * lm)
                                A += e
                                Ap += e * lm
                            g = math.exp(y * ell)
                            gp = ell * g
                            R = B - g * g * A
                            S = g * (A - B)
                            Rp = -(2 * g * gp * A + g * g * Ap)
                            Sp = gp * (A - B) + g * Ap
                            dR = (Rp if R > 0 else -Rp) if R != 0 else abs(Rp)
                            dS = (Sp if S > 0 else -Sp) if S != 0 else abs(Sp)
                            den = abs(R) + abs(S)
                            if den == 0:
                                continue
                            s = ((dR + dS) / den + 2 * g * gp / (1 - g * g)) / ln_n
                            samples += 1
                            if s > best[0]:
                                best = (s, dict(N=N, G=G, sector=[prev, top], n=n, n_over_N=n / N, y=y,
                                                active=[d for d in divs if n // d <= N]))
        out.append(dict(leg=li, primes=list(P), sampled_sup_required_slope=best[0], at=best[1], samples=samples))
    return out


# ----------------------------------------------------------------------------
# E: exact rational checks
# ----------------------------------------------------------------------------
def U(g, B, A):
    return (abs(B - g * g * A) + g * abs(A - B)) / (1 - g * g)


def section_E():
    import random
    rnd = random.Random(17)
    n_sub = n_hom = n_mono = n_closed = 0
    for _ in range(4000):
        g = Fr(rnd.randint(0, 99), 100)
        B1, A1, B2, A2 = (Fr(rnd.randint(-50, 50), rnd.randint(1, 9)) for _ in range(4))
        c = Fr(rnd.randint(-30, 30), rnd.randint(1, 7))
        if not U(g, B1 + B2, A1 + A2) <= U(g, B1, A1) + U(g, B2, A2):
            fail('E: subadditivity')
        n_sub += 1
        if U(g, c * B1, c * A1) != abs(c) * U(g, B1, A1):
            fail('E: homogeneity')
        n_hom += 1
        g2 = g + Fr(rnd.randint(0, 99 - int(g * 100)), 100)
        if g2 < 1 and not U(g, B1, A1) <= U(g2, B1, A1):
            fail('E: monotonicity in g')
        n_mono += 1
        a = 1 + Fr(rnd.randint(0, 500), 100)
        if g * g * a <= 1:
            if (1 - g) * U(g, 1, a) != (1 - g) * (1 + g * a) / (1 + g):
                fail('E: closed form of (1-g)U_g(1,a)')
            n_closed += 1
    return dict(subadditivity=n_sub, homogeneity=n_hom, monotonicity_in_g=n_mono, closed_form=n_closed)


# ----------------------------------------------------------------------------
# G: contract arithmetic
# ----------------------------------------------------------------------------
def section_G():
    out = {}
    X = 6000000185827
    with localcontext(Context(prec=60)):
        pi = Dc('3.14159265358979323846264338327950288419716939937510582097494')
        t = Dc(157) / 1000
        xs = X + (1 - Dc(87677) / 2500000).sqrt()
        x = lambda N: 4 * pi * (Dc(N) * N - t / 16)
        lo, hi = xs - x(690988), x(690989) - xs
        out['x_star_minus_x_690988'] = str(lo.quantize(Dc('0.01')))
        out['x_690989_minus_x_star'] = str(hi.quantize(Dc('0.01')))
        if not (lo > 0 and hi > 0):
            fail('G: first window does not contain x_*')
        dt = (Dc(129) / 800 - t) / 16 * 4 * pi
        out['edge_shift_from_t0'] = str(dt)
    ylo, yhi = Fr(1872719, 10 ** 7), Fr(23409, 125000)
    ext = Fr(8282512, 10 ** 7)
    checks = {
        'ybox_contains_y0': ylo ** 2 < Y0SQ < yhi ** 2,
        'y1_squared_is_1_minus_2t': Fr(343, 500) == 1 - 2 * Fr(157, 1000),
        'ext_top_covers_y1': ext ** 2 >= Fr(343, 500),
        'target_value': Fr(157, 1000) + Y0SQ / 2 == Fr(872677, 5000000),
        'barrier_y0_above_0.1809': Fr(1809, 10000) ** 2 < Y0SQ,
        'barrier_t_inside': Fr(157, 1000) < Fr(129, 800),
        'barrier_width_below_one': Y0SQ > 0,
    }
    out.update(checks)
    for k, v in checks.items():
        if not v:
            fail('G: ' + k)
    return out


# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--repo-root', type=Path)
    ap.add_argument('--sections', default='ABCDEFG')
    ap.add_argument('--legs', default='0,1,2,3', help='legs for section F')
    ap.add_argument('--slack', action='store_true', help='also run the D2 interval slack probe and the D3 float slope scan')
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    here = Path(__file__).resolve()
    repo = a.repo_root or next(p for p in here.parents if (p / ENGINE).exists())
    legs = [int(v) for v in a.legs.split(',')]
    rec = dict(date='2026-10-17', prepared_for='Edward Baker',
               model='Claude Opus 5.5 (configured identifier claude-opus-5-5); serving model may differ',
               reasoning_effort='max', interface='Claude Cowork',
               scope='cross-model review support computations; floating and planning sections are not certificates',
               python=platform.python_version(), platform=platform.platform(),
               script_sha256=hashlib.sha256(here.read_bytes()).hexdigest(), sections=a.sections)
    start = time.monotonic()
    if 'A' in a.sections:
        rec['A_digests'] = {str(p): hashlib.sha256((repo / p).read_bytes()).hexdigest() for p in DIGEST_FILES}
    if 'B' in a.sections:
        pilot = json.loads((repo / PILOT_RECORD).read_text())['row']
        lo, hi = (float(v) for v in pilot['L'])
        b1 = row(690988, LEGS[0][0], T_NEW, Y0, 'sharp')
        b1['pilot_enclosure'] = pilot['L']
        b1['abs_difference_to_enclosure_midpoint'] = abs(b1['L'] - (lo + hi) / 2)
        if b1['abs_difference_to_enclosure_midpoint'] > 1e-13 or b1['NT'] != pilot['number_of_n']:
            fail('B1: float sharp row disagrees with the certified pilot')
        b2 = row(690988, LEGS[0][0], T_OLD, Y0, 'plain')
        b2['audit_certified_lower'] = AUDIT_PLAIN_690988
        b2['abs_difference'] = abs(b2['L'] - AUDIT_PLAIN_690988)
        if b2['abs_difference'] > 1e-13:
            fail('B2: float plain row disagrees with the audit certificate')
        b3 = dict(sharp_t0_690988=row(690988, LEGS[0][0], T_OLD, Y0, 'sharp')['L'],
                  audit_float_sharp_t0='+0.0770',
                  plain_t157_leg_starts={str(N): row(N, P, T_NEW, Y0, 'plain')['L'] for P, N, _ in LEGS},
                  audit_float_plain_t157=['-0.0870', '-0.0876', '-0.0892', '-0.0916'])
        if abs(b3['sharp_t0_690988'] - 0.0770) > 5e-5:
            fail('B3: sharp t0 value')
        for (P, N, _), ref in zip(LEGS, (-0.0870, -0.0876, -0.0892, -0.0916)):
            if abs(b3['plain_t157_leg_starts'][str(N)] - ref) > 5e-5:
                fail('B3: plain leg-start value')
        b4 = {str(t): row(690988, LEGS[0][0], t, Y0, 'sharp')['L'] for t in (0.1569, 0.15695)}
        if not (b4['0.1569'] < 0 < b4['0.15695']):
            fail('B4: first-row boundary control')
        rec['B_rows'] = dict(B1_sharp_new=b1, B2_plain_old=b2, B3=b3, B4_first_row_boundary=b4)
    if 'C' in a.sections:
        rec['C_gate_numerator_vs_definition'] = section_C(repo)
    if 'D' in a.sections:
        rec['D_fault_injection'] = section_D(repo, a.slack)
    if 'E' in a.sections:
        rec['E_exact_seminorm_checks'] = section_E()
    if 'F' in a.sections:
        f = {}
        # F0: bookkeeping of the activation lemma on two spans (float):
        #     L_N(own scalars) >= L_hyb(N) >= L_Na - Delta(Na, N)
        f0 = []
        for li, Na, N in ((0, 690988, 691988), (3, 1028000, 1030000)):
            P = LEGS[li][0]
            La = row(Na, P, T_NEW, Y0, 'sharp')['L']
            Lh = row(N, P, T_NEW, Y0, 'sharp', scal=scalars(Na, T_NEW, Y0))['L']
            Ln = row(N, P, T_NEW, Y0, 'sharp')['L']
            _, dlt = greedy_span_exact(Na, N, T_NEW, Y0, 'sharp', float('inf'))
            ok = Ln >= Lh - 1e-13 and Lh >= La - dlt - 1e-13
            f0.append(dict(leg=li, Na=Na, N=N, L_Na=La, L_hybrid_N=Lh, L_N=Ln, Delta=dlt,
                           hybrid_minus_bound=Lh - (La - dlt), ok=ok))
            if not ok:
                fail(f'F0: activation-lemma bookkeeping fails on span {Na}..{N}')
        f['F0_lemma_bookkeeping'] = f0
        f['sharp_t157_exact_activation'] = mesh(T_NEW, Y0, E_NEW, 'sharp', 'exact', legs)
        f['sharp_t157_cap_activation'] = mesh(T_NEW, Y0, E_NEW, 'sharp', 'cap', legs)
        f['plain_t0_exact_activation'] = mesh(T_OLD, Y0, E_OLD, 'plain', 'exact', legs)
        # Mixed plan: cap-lemma bounds on every span except the last of each leg, which uses the
        # exact (in a certificate: outward direct) activation sum from the earliest cap-mesh row
        # whose exact span reaches the end of the leg.
        mixed = []
        for leg in f['sharp_t157_cap_activation']:
            leg_end = LEGS[leg['leg']][2]
            for i, p in enumerate(leg['mesh']):
                Nb, d = greedy_span_exact(p['Na'], leg_end, T_NEW, Y0, 'sharp', p['L'] - E_NEW)
                if Nb >= leg_end:
                    mixed.append(dict(leg=leg['leg'], rows=i + 1, last_row=p['Na'], last_row_L=p['L'],
                                      last_span_exact_delta=d, rows_list=[q['Na'] for q in leg['mesh'][:i + 1]]))
                    break
        f['sharp_t157_cap_then_direct_last_span'] = mixed
        f['summary'] = {k: [v['rows'] for v in f[k]] for k in list(f)
                        if k.endswith('activation') or k.endswith('last_span')}
        f['largest_row'] = {k: max((p['Na'] for v in f[k] for p in v['mesh']), default=None)
                            for k in list(f) if k.endswith('activation')}
        f['largest_row']['sharp_t157_cap_then_direct_last_span'] = max(v['last_row'] for v in mixed) if mixed else None
        rec['F_activation_planning_FLOAT'] = f
    if 'G' in a.sections:
        rec['G_contract_arithmetic'] = section_G()
    rec['seconds'] = time.monotonic() - start
    rec['failures'] = FAILURES
    rec['passed'] = not FAILURES
    a.output.write_text(json.dumps(rec, indent=1, default=str) + '\n')
    print(json.dumps(dict(output=str(a.output), passed=rec['passed'], failures=FAILURES,
                          seconds=round(rec['seconds'], 1),
                          F=rec.get('F_activation_planning_FLOAT', {}).get('summary'))))
    return 0 if rec['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
