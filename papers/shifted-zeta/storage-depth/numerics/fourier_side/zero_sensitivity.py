"""Sensitivity of the first-step near-null vector to displacing a low zero.

For the lowest eigenvector f_0 of the 288-mode head at L_q, and for each of
the first K zeros gamma_k, evaluate the exact pair term

    Delta(delta, gamma_k) = 2 Re[ F_0(gamma_k + i delta) conj(F_0(gamma_k - i delta)) ]

that the explicit formula would assign to a zero displaced to 1/2 +- delta +
i gamma_k (with its conjugates), in place of the on-line term 2|F_0(gamma_k)|^2.
Near a zero where F_0 is small, Delta ~ 2(|F_0|^2 - delta^2 |F_0'|^2) turns
negative, and the displacement delta_k* at which Delta = -lambda_0 measures the
sensitivity of the finite-horizon floor to that zero. Diagnostic only.
"""
import json, sys, time
from pathlib import Path
import mpmath as mp

mp.mp.dps = 60
rayleigh_path, zeros_cache, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
K = int(sys.argv[4]) if len(sys.argv) > 4 else 20
t0 = time.monotonic()
# the rounded lowest eigenvector and its ball Rayleigh quotient from rayleigh_upper.py (record R16)
ray = json.loads(Path(rayleigh_path).read_text())
no, nn = 256, 32; n = no + nn
vec = [mp.mpf(x) for x in ray['vector']]; assert len(vec) == n
nrm = mp.sqrt(sum(x * x for x in vec)); f0 = mp.matrix([x / nrm for x in vec])
lam0 = mp.mpf(ray['rayleigh_quotient'].split('+/-')[0].strip(' []'))
a = mp.log(7); h = (mp.log(8) - mp.log(7)) / 4; L = a + h
intervals = [(mp.mpf(0), a, no), (a, h, nn)]

def F0(tau):
    total = mp.mpc(0); off = 0
    for s, ell, modes in intervals:
        centre = s + ell / 2 - L / 2; w = tau * ell / 2
        phase = mp.exp(-1j * tau * centre); pref = mp.sqrt(mp.pi / (2 * w))
        for k in range(modes):
            total += f0[off + k] * mp.sqrt((2 * k + 1) * ell) * (-1j) ** k * pref * mp.besselj(k + mp.mpf(1) / 2, w) * phase
        off += modes
    return total

zeros = [mp.mpf(z) for z in json.loads(Path(zeros_cache).read_text())[:K]]
rows = []
for k, g in enumerate(zeros, 1):
    F = F0(g)
    dF = (F0(g + mp.mpf('1e-12')) - F0(g - mp.mpf('1e-12'))) / mp.mpf('2e-12')
    row = {'k': k, 'gamma': mp.nstr(g, 12), 'abs_F0': mp.nstr(abs(F), 6), 'abs_dF0': mp.nstr(abs(dF), 6),
           'on_line_term': mp.nstr(2 * abs(F) ** 2, 6)}
    for d in ('1e-9', '1e-6', '1e-3', '1e-1'):
        dd = mp.mpf(d)
        Delta = 2 * mp.re(F0(g + 1j * dd) * mp.conj(F0(g - 1j * dd)))
        row[f'Delta_{d}'] = mp.nstr(Delta, 6)
    # leading-order displacement at which the pair term equals -lambda_0
    if abs(dF) > 0:
        row['delta_star_leading_order'] = mp.nstr(mp.sqrt((lam0 + 2 * abs(F) ** 2) / (2 * abs(dF) ** 2)), 6)
    rows.append(row); print(row, flush=True)
out = {'scope': 'Sensitivity of Q_{0,L_q}[f_0] to displacing individual low zeros; explicit-formula pair terms; diagnostic.',
       'lambda_0': mp.nstr(lam0, 15), 'rows': rows, 'seconds': time.monotonic() - t0}
Path(out_path).write_text(json.dumps(out, indent=2) + '\n')
print('done', round(time.monotonic() - t0))
