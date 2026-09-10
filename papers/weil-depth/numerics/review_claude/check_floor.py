"""High-precision head spectrum and maximal certifiable floor with the same matrices."""
import os as _os
ARCHIVE_1P8 = _os.environ.get('ARCHIVE_1P8', 'output/length_1p8_N128/central_matrices.json.gz')
ARCHIVE_LOG7 = _os.environ.get('ARCHIVE_LOG7', 'output/log7_N128/central_matrices.json.gz')
import sys, gzip, json, io, contextlib
import mpmath as mp
sys.path.insert(0, '.')  # run from numerics/
import certify_arb as c
from flint import ctx

def load(path):
    with gzip.open(path, 'rt') as fh:
        return json.load(fh)

def midmat(data, name, ids):
    return mp.matrix([[mp.mpf(int(data['matrices'][name][i][j][0][0]))*mp.mpf(2)**int(data['matrices'][name][i][j][0][1]) for j in ids] for i in ids])

for tag, path, bits in [('9/5', ARCHIVE_1P8, 1536),
                        ('log7', ARCHIVE_LOG7, 1792)]:
    data = load(path); N = data['N']
    mp.mp.dps = 80
    print(f"=== L = {tag}: head spectrum (mpmath eigsy on Arb midpoints, 80 digits)")
    for parity in (0, 1):
        ids = list(range(parity, N, 2))
        q = midmat(data, 'Q', ids); e = midmat(data, 'E_central', ids)
        ev = mp.eigsy(q, eigvals_only=True)
        ev = sorted(ev)
        print(f"  parity {parity}: eig(q): min {mp.nstr(ev[0],6)}, 2nd {mp.nstr(ev[1],6)}, 3rd {mp.nstr(ev[2],6)}, 4th {mp.nstr(ev[3],6)}, 5th {mp.nstr(ev[4],6)}, 8th {mp.nstr(ev[7],6)}, max {mp.nstr(ev[-1],6)}")
        eve = sorted(mp.eigsy((e+e.T)/2, eigvals_only=True))
        print(f"             eig(E): min {mp.nstr(eve[0],4)} (PSD check), max {mp.nstr(eve[-1],6)}")
        # required tail floor diagnostic: lambda_max(q^{-1/2} E q^{-1/2}) via generalized eig of (E, q)
        Lq = mp.cholesky(q)
        Li = mp.inverse(Lq)
        rel = sorted(mp.eigsy(Li*e*Li.T, eigvals_only=True))
        print(f"             required tail floor lambda_max(q^-1/2 E q^-1/2) = {mp.nstr(rel[-1], 10)}")
    ctx.prec = bits
    print(f"  --- certifiable floor sweep with the package's validate() (ball LDL), same matrices")
    for m in ['1e-34','1e-30','1e-26','1e-22','1e-20','1e-19','1e-18','3e-18','1e-17','3e-17','1e-16','1e-15','1e-14']:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            res = c.validate(data, m)
        summary = []
        for ch in res['checks']:
            if ch['positive']:
                summary.append('PASS')
            else:
                summary.append(f"FAIL@{ch['failed_pivot']}")
        print(f"     m={m:>6s}: {res['status']:14s} {summary}")
        if res['status'] != 'PASS' and m not in ('1e-34',):
            pass
