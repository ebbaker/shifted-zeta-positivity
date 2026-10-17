#!/usr/bin/env python3
"""Outward sharp-row pilot; no y transfer or complete Newman certificate.

Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Model gpt-6.1-sol (Codex), effort ultra. Standard-library Python only.

Imports hash-pinned scalar/table/error helpers from the canonical audit.
The new main sum uses W=max(|B-g A|,c|B+g A|), c=(1-g)/(1+g).
For fixed-point errors eB,eA,dG,dC, real |A|<=Ar, |B|+|A|<=Wr:
 eGA=eA+dG*Ar+ceil(dG*eA/U)+1;
 eV=eB+eGA;
 eW=max(eV,eV+dC*Wr+ceil(dC*eV/U)+1).
The max and absolute-value maps are 1-Lipschitz. Remaining sum/table
bounds are inherited, with W<=|B|+g|A|<=|B|+|A|.
"""
import argparse, hashlib, importlib.util, json, platform, resource, signal, sys, time
from decimal import Decimal as Dc, ROUND_CEILING, ROUND_HALF_EVEN
from pathlib import Path

HELPER = 'papers/investigations-2/newman_certificate_audit/numerics/check_finite_row_certified_replay.py'
HELPER_SHA = '37d525ed2e8b424462523710d0b70e7a1e23b5dd6d755f36d6c3b1e77152fc35'


def load_helper(repo):
    path = repo / HELPER
    if hashlib.sha256(path.read_bytes()).hexdigest() != HELPER_SHA:
        raise RuntimeError('Inherited helper hash mismatch; audit the change before replay')
    spec = importlib.util.spec_from_file_location('canonical_row_helpers', path)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    return h


def sharp_sum(h, N, P, sc, BT, AA, KS):
    U, K, CN = h.U, h.K, h.CN
    fix = lambda z: int(CN.multiply(z, h.UD).to_integral_value(rounding=ROUND_HALF_EVEN))
    LAM = {mask: sign * fix(mag.mid()) for mask, (sign, mag, _) in sc['lam'].items()}
    G0IV = {mask: h.iexp(-sc['sigma'] * h.iln(h.Iv(d)))
            for mask, (_, _, d) in sc['lam'].items()}
    G0S = {mask: fix(v.mid()) for mask, v in G0IV.items()}
    # This construction uses interval scalars, not the relative table bound.
    dG0_exact = max(int(h.CC.multiply(v.width(), h.UD).to_integral_value(
                       rounding=ROUND_CEILING)) + 1 for v in G0IV.values())
    val = {mask: d for mask, (_, _, d) in sc['lam'].items()}
    nmask = 1 << len(P)
    pairs = {}
    for G in range(nmask):
        pairs[G] = sorted((val[e], LAM[G & ~e]) for e in range(nmask) if e & G == e)
    supersets = [[(G, pairs[G], G0S[G]) for G in range(nmask) if G & mask == mask]
                 for mask in range(nmask)]
    pm = bytearray(N + 1)
    for i, p in enumerate(P):
        for k in range(p, N + 1, p):
            pm[k] |= 1 << i
    gfix = fix(sc['g'].mid())
    civ = (1 - sc['g']) / (1 + sc['g'])
    cfix = fix(civ.mid())
    assert 0 <= gfix <= U and 0 <= cfix <= U
    S = NSsum = NT = INC = 0
    for k in range(1, N + 1):
        emax, ksk = N // k, KS[k]
        for G, terms, g0s in supersets[pm[k]]:
            if k == 1 and G == 0:
                continue
            B2 = A2 = 0
            for e, lam in terms:
                if e > emax:
                    break
                m = e * k
                B2 += lam * BT[m]
                A2 += lam * AA[m]
                INC += 1
            b, a = B2 >> K, A2 >> K
            ga = (gfix * a) >> K
            w = max(abs(b - ga), (cfix * abs(b + ga)) >> K)
            ns = (g0s * ksk) >> K
            S += (w * ns) >> K
            NSsum += ns
            NT += 1
    ms = dict(S=S, NSsum=NSsum, NT=NT, INC=INC, LAM=LAM, G0S=G0S, Gfix=gfix, dG0_exact=dG0_exact)
    return ms, civ


def compute(h, N, P, t, y2):
    sc = h.row_scalars(N, t=t, y2=y2, P=P)
    assert 0 < sc['g'].lo <= sc['g'].hi < 1
    rho = h.rho_bound(N, sc)
    assert rho <= h.RHO
    BT, AA, KS, CS = h.build_tables(N, sc)
    ms, civ = sharp_sum(h, N, P, sc, BT, AA, KS)
    _, ep = h.error_bound_S(N, P, sc, BT, AA, KS, ms, h.RHO)
    cdiv = lambda a, b: -(-a // b)
    ep['dG0'] = ms['dG0_exact']
    ep['eNS'] = ep['dKS'] + ep['dG0'] + cdiv(ep['dG0'] * ep['dKS'], h.U) + 1
    dC = int(h.CC.multiply(civ.width(), h.UD).to_integral_value(rounding=ROUND_CEILING)) + 1
    eGA = ep['eA'] + ep['dG'] * ep['Ar'] + cdiv(ep['dG'] * ep['eA'], h.U) + 1
    eV = ep['eB'] + eGA
    eW = max(eV, eV + dC * ep['Wr'] + cdiv(dC * eV, h.U) + 1)
    eNS, Wr, NT = ep['eNS'], ep['Wr'], ms['NT']
    E = NT * (Wr * eNS + cdiv(eW * eNS, h.U) + 1) + cdiv(eW * (ms['NSsum'] + NT * eNS), h.U)
    S = h.Iv(h.CF.divide(Dc(ms['S'] - E), h.UD), h.CC.divide(Dc(ms['S'] + E), h.UD))
    lnN = h.iln(h.Iv(N))
    # Inherited CS bound: relative table/accumulation error < 1e-35.
    CSi = h.Iv(h.CF.multiply(CS, 1 - Dc('1e-35')), h.CC.multiply(CS, 1 + Dc('1e-35')))
    kap = sc['kappa']
    C = h.Iv(h.CF.multiply(kap.lo, CSi.lo),
             h.CC.multiply(h.CC.multiply(kap.hi, h.iexp(kap * lnN).hi), CSi.hi))
    Q = 1 - sc['g'] - S
    L = Q / sc['M'] - sc['g'] * C
    enc = lambda v: [str(v.lo), str(v.hi)]
    return dict(N=N, primes=list(P), t=str(t), y_squared=str(y2),
                sigma=enc(sc['sigma']), g=enc(sc['g']), M=enc(sc['M']),
                S=enc(S), Q=enc(Q), kappa_correction=enc(sc['g'] * C),
                L=enc(L), fixed_point_error=str(h.CC.divide(Dc(E), h.UD)),
                number_of_n=NT, incidences=ms['INC'], rho_needed=str(rho),
                error_parts=dict(ep, dC=dC, eGA=eGA, eV=eV, sharp_eW=eW)), sc


def brute_sharp(h, N, P, sc):
    # Separate enumeration over every n and its divisors; no gcd partition.
    CN, D = h.CN, max(v[2] for v in sc['lam'].values())
    t4, y, sigma, g = sc['t'].mid() / 4, sc['y'].mid(), sc['sigma'].mid(), sc['g'].mid()
    c = (1 - g) / (1 + g)
    lam = {d: s * a.mid() for s, a, d in sc['lam'].values()}
    S = Dc(0)
    for n in range(2, D * N + 1):
        B = A = Dc(0)
        for d, ld in lam.items():
            if n % d == 0 and n // d <= N:
                m = n // d
                l = CN.ln(Dc(m))
                b = CN.exp(t4 * l * l)
                B += ld * b
                A += ld * b * CN.exp(y * l)
        S += max(abs(B - g * A), c * abs(B + g * A)) * CN.exp(-sigma * CN.ln(Dc(n)))
    return S


def selftest(h):
    checks = []
    for N, P, y2 in [(19,(2,3),'.0350708'), (23,(2,3,5),'.25'),
                     (29,(2,3,5,7),'.686'), (17,(2,3,5,7,11),'.0350708')]:
        r, sc = compute(h, N, P, Dc('.157'), Dc(y2))
        direct = brute_sharp(h, N, P, sc)
        assert Dc(r['S'][0]) <= direct <= Dc(r['S'][1]), (r, direct)
        checks.append(dict(N=N, primes=list(P), y_squared=y2, direct_S=str(direct),
                           enclosure=r['S'], passed=True))
    # Deterministic exact weight identity includes zeros and branch ties.
    from fractions import Fraction as F
    count = 0
    for b in map(F, range(-4,5)):
        for a in map(F, range(-4,5)):
            for g in (F(0), F(1,10), F(1,2), F(9,10)):
                w = max(abs(b-g*a), (1-g)/(1+g)*abs(b+g*a))
                rhs = (abs(b-g*g*a)+g*abs(a-b))/(1+g)
                assert w == rhs
                count += 1
    return dict(direct_enumerations=checks, exact_weight_identities=count)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path)
    ap.add_argument('--N', type=int, default=690988)
    ap.add_argument('--t', default='.157')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--selftest-only', action='store_true')
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    repo = a.repo or next(p for p in Path(__file__).resolve().parents if (p / HELPER).exists())
    h = load_helper(repo)
    start = time.monotonic()
    def timeout(signum, frame):
        raise TimeoutError('600 second wall budget exceeded')
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(600)
    rec = dict(date='2026-10-17', prepared_for='Edward Baker', model='gpt-6.1-sol',
               reasoning_effort='ultra', status='outward arithmetic pilot; no strip transfer or full bound',
               helper=HELPER, helper_sha256=HELPER_SHA,
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               python=platform.python_version(), fixed_point_bits=h.K)
    if a.selftest or a.selftest_only:
        rec['selftest'] = selftest(h)
    if not a.selftest_only:
        r, _ = compute(h, a.N, h.leg_primes(a.N), Dc(a.t), h.Y0SQ)
        rec['row'] = r
    rec['seconds'] = time.monotonic() - start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rec['peak_resident_bytes'] = rss if sys.platform == 'darwin' else rss * 1024
    rec['resource_gates'] = dict(wall_below_600_seconds=rec['seconds'] < 600,
        peak_below_512MiB=rec['peak_resident_bytes'] < 512 * 1024**2)
    assert all(rec['resource_gates'].values()), rec['resource_gates']
    signal.alarm(0)
    a.output.write_text(json.dumps(rec, indent=2) + '\n')
    print(json.dumps(dict(output=str(a.output), seconds=rec['seconds'],
                          L=rec.get('row',{}).get('L'), selftest='selftest' in rec)))

if __name__ == '__main__':
    main()
