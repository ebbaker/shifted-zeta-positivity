"""Build certificates at the logarithmic horizons log2..log6 (N=128, M=220, 1792 bits)
with the unmodified builder, then bisect the largest certifiable floor and certify an
upper bound via a ball Rayleigh quotient. Output: profile.json"""
import sys, subprocess, gzip, json, io, contextlib, time
from fractions import Fraction
import mpmath as mp
sys.path.insert(0, '.')  # run from numerics/
import certify_arb as c
from flint import arb as A, arb_mat as AM, ctx

def validate_quiet(data, m):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return c.validate(data, m)['status'] == 'PASS'

def twosided(data, bits, lo=-60.0, hi=0.0):
    ctx.prec = bits; N = data['N']
    a, b = lo, hi
    assert validate_quiet(data, f'1e{int(lo)}')
    for _ in range(12):
        mid = (a+b)/2
        if validate_quiet(data, mp.nstr(mp.mpf(10)**mid, 3)):
            a = mid
        else:
            b = mid
    lower = mp.nstr(mp.mpf(10)**a, 3)
    mp.mp.dps = 60
    out = {}
    for parity in (0, 1):
        ids = list(range(parity, N, 2))
        qmid = mp.matrix([[mp.mpf(int(data['matrices']['Q'][i][j][0][0]))*mp.mpf(2)**int(data['matrices']['Q'][i][j][0][1]) for j in ids] for i in ids])
        E, V = mp.eigsy(qmid)
        order = sorted(range(len(ids)), key=lambda i: E[i])
        k = order[0]
        v = [Fraction(str(mp.nstr(V[i, k], 40))) for i in range(len(ids))]
        Qball = AM([[c.unpack(data['matrices']['Q'][i][j]) for j in ids] for i in ids])
        vb = AM([[c.rat(x)] for x in v])
        ray = (vb.transpose()*Qball*vb)[0, 0]/(vb.transpose()*vb)[0, 0]
        L = A(data['log_horizon']).log() if data['log_horizon'] else c.rat(data['horizon'])
        eta = c.analytic(L, c.profile(data['M']), N, c.prime_powers(L, data['log_horizon']), data['log_horizon'])['profile_remainder']
        out[f'parity{parity}'] = {'head_eigs_lowest5': [mp.nstr(E[i], 6) for i in order[:5]],
                                  'upper_bound_ball': (ray+eta).upper().str(8)}
    out['largest_certified_floor'] = lower
    return out

results = {}
for n in (2, 3, 4, 5, 6):
    outdir = f'output/profile_log{n}'
    t0 = time.time()
    r = subprocess.run([sys.executable, 'certify_arb.py', '--N', '128', '--M', '220', '--bits', '1792',
                        '--log-horizon', str(n), '--floor', '1e-60', '--output', outdir], capture_output=True, text=True,
                       cwd='.')
    build_s = time.time()-t0
    with gzip.open(outdir+'/central_matrices.json.gz', 'rt') as fh:
        data = json.load(fh)
    cert = json.load(open(outdir+'/central_certificate.json'))
    res = {'build_status': cert['status'], 'build_seconds': round(build_s, 1), 'tail_floor': cert['bound_display']['tail_floor'][:20],
           'active': data['active_prime_powers'], 'overlaps': data['reflected_delay_overlaps']}
    res.update(twosided(data, 1792))
    results[f'log{n}'] = res
    print(f'log{n}', json.dumps(res), flush=True)
    json.dump(results, open('review_claude/profile.json', 'w'), indent=1)
print('PROFILE DONE')
