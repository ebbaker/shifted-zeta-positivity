"""Two-sided enclosure of lambda_min(Q_{0,L}) from the rebuilt archives.
 lower: bisect the largest floor m the package's own ball-LDL validate() certifies
 upper: rigorous Rayleigh quotient <v,Qv>/<v,v> in ball arithmetic, for a rational
        vector v approximating the head ground state (the head q = P Q_0 P is the
        exact form on polynomials up to the profile error eta ~ 1e-40)."""
import os as _os
ARCHIVE_1P8 = _os.environ.get('ARCHIVE_1P8', 'output/length_1p8_N128/central_matrices.json.gz')
ARCHIVE_LOG7 = _os.environ.get('ARCHIVE_LOG7', 'output/log7_N128/central_matrices.json.gz')
import sys, gzip, json, io, contextlib
from fractions import Fraction
import mpmath as mp
sys.path.insert(0, '.')  # run from numerics/
import certify_arb as c
from flint import arb as A, arb_mat as AM, ctx

def load(path):
    with gzip.open(path, 'rt') as fh:
        return json.load(fh)

def validate_quiet(data, m):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return c.validate(data, m)['status'] == 'PASS'

for tag, path, bits, lo, hi, eta_disp in [
        ('9/5',  ARCHIVE_1P8, 1536, -26.0, -22.0, '2.48e-40'),
        ('log7', ARCHIVE_LOG7, 1792, -34.0, -26.0, '9.35e-42')]:
    data = load(path); N = data['N']; ctx.prec = bits
    # --- lower bound bisection in log10(m)
    assert validate_quiet(data, f'1e{int(lo)}')
    a, b = lo, hi   # a passes, b fails (checked below)
    assert not validate_quiet(data, f'1e{int(b)}')
    for _ in range(9):
        mid = (a+b)/2
        m = mp.nstr(mp.mpf(10)**mid, 3)
        if validate_quiet(data, m):
            a = mid
        else:
            b = mid
    best = mp.nstr(mp.mpf(10)**a, 3)
    print(f"L={tag}: largest certified floor found by bisection: m = {best} (PASS), first failure above ~ {mp.nstr(mp.mpf(10)**b,3)}")
    # --- upper bound: ball Rayleigh quotient of the even-sector head ground state
    mp.mp.dps = 60
    ids = list(range(0, N, 2))
    qmid = mp.matrix([[mp.mpf(int(data['matrices']['Q'][i][j][0][0]))*mp.mpf(2)**int(data['matrices']['Q'][i][j][0][1]) for j in ids] for i in ids])
    E, V = mp.eigsy(qmid)
    k = min(range(len(ids)), key=lambda i: E[i])
    v = [Fraction(str(mp.nstr(V[i, k], 40))) for i in range(len(ids))]
    Qball = AM([[c.unpack(data['matrices']['Q'][i][j]) for j in ids] for i in ids])
    vb = AM([[c.rat(x)] for x in v])
    num = (vb.transpose()*Qball*vb)[0, 0]
    den = (vb.transpose()*vb)[0, 0]
    ray = num/den
    eta = c.analytic(A(data['log_horizon']).log() if data['log_horizon'] else c.rat(data['horizon']), c.profile(data['M']), N,
                     c.prime_powers(A(data['log_horizon']).log() if data['log_horizon'] else c.rat(data['horizon']), data['log_horizon']), data['log_horizon'])['profile_remainder']
    upper = (ray + eta).upper()   # exact head = model head + O(eta) in norm
    print(f"        even ground-state Rayleigh quotient (ball) = {ray.str(12)}; certified upper bound lambda_min <= {upper.str(6)}  (includes profile error eta < {eta_disp})")
    print(f"        => enclosure  {best} <= lambda_min(Q_(0,{tag})) <= {upper.str(4)}")
