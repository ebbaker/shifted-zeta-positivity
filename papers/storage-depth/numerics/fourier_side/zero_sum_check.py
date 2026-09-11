"""Fourier-side check of the first-step spatial head against the zero sum.

In the working normalization (Weil-depth v0.3, checked there on a smooth test
to relative 6e-10) the central form satisfies

    Q_{0,L}[f] = 2 * sum_{gamma > 0} |F(gamma)|^2,   F(tau) = \int f_c(x) e^{-i tau x} dx,

where f_c is the centered zero extension and gamma runs over the ordinates of
the nontrivial zeros. For the lowest eigenvector f_0 of the 288-mode spatial
head at L_q the left side is the head eigenvalue lambda_0 (about 3.28e-29).
This script computes the partial zero sums for f_0 with the first K zeros and
reports (i) how fast they converge to lambda_0, (ii) where |F_0| lives, and
(iii) for a hypothetical off-line pair 1/2 +- delta + i t the change

    Delta(delta, t) = 2 Re[ F_0(t + i delta) conj(F_0(t - i delta)) ]

that the pair would contribute, compared with lambda_0. Diagnostic only; uses
midpoints of the ball matrices and mpmath at 60 digits. Legendre transforms use
the closed form  \int_{-1}^{1} P_n(u) e^{-i w u} du = 2 (-i)^n j_n(w).
"""
import json, sys, time
from pathlib import Path
import mpmath as mp

mp.mp.dps = 60
head_path, zeros_cache, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
K = int(sys.argv[4]) if len(sys.argv) > 4 else 400
t0 = time.monotonic()
data = json.loads(Path(head_path).read_text())
no, nn = data['old_modes'], data['new_modes']
n = no + nn
H = mp.matrix([[mp.mpf(x) for x in row] for row in data['head_mid']])
H = (H + H.T) / 2
E, V = mp.eigsy(H)
order = sorted(range(n), key=lambda i: E[i])
lam0 = E[order[0]]
f0 = mp.matrix([V[i, order[0]] for i in range(n)])
print('lambda_0 =', mp.nstr(lam0, 12), ' next:', [mp.nstr(E[order[k]], 6) for k in (1, 2, 3)], ' eig s', round(time.monotonic() - t0), flush=True)

a = mp.log(7); h = (mp.log(8) - mp.log(7)) / 4; L = a + h
intervals = [(mp.mpf(0), a, no), (a, h, nn)]  # (start, length, modes)

def basis_transform(tau):
    """Vector of F_i(tau) for the 288 orthonormal piecewise-Legendre modes, complex tau allowed."""
    out = []
    for s, ell, modes in intervals:
        centre = s + ell / 2 - L / 2
        w = tau * ell / 2
        phase = mp.exp(-1j * tau * centre)
        if w == 0:
            vals = [mp.sqrt(ell) * phase] + [mp.mpc(0)] * (modes - 1)
        else:
            pref = mp.sqrt(mp.pi / (2 * w))
            vals = []
            for k in range(modes):
                jn = pref * mp.besselj(k + mp.mpf(1) / 2, w)
                vals.append(mp.sqrt((2 * k + 1) * ell) * (-1j) ** k * jn * phase)
        out.extend(vals)
    return out

def F0(tau):
    vec = basis_transform(tau)
    return sum(f0[i] * vec[i] for i in range(n))

# zeros (cached)
cache = Path(zeros_cache)
zeros = json.loads(cache.read_text()) if cache.exists() else []
mp.mp.dps = 40
while len(zeros) < K:
    zeros.append(mp.nstr(mp.im(mp.zetazero(len(zeros) + 1)), 35))
    if len(zeros) % 50 == 0:
        cache.write_text(json.dumps(zeros)); print('zeros', len(zeros), 'height', zeros[-1][:8], 's', round(time.monotonic() - t0), flush=True)
cache.write_text(json.dumps(zeros))
mp.mp.dps = 60
gammas = [mp.mpf(z) for z in zeros[:K]]

partial = mp.mpf(0); checkpoints = {}; terms = []
for k, g in enumerate(gammas, 1):
    v = abs(F0(g)) ** 2
    terms.append(v)
    partial += 2 * v
    if k in (1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 400, 600, 800, 1000, 1500, 2000) or k == K:
        checkpoints[k] = {'height': mp.nstr(g, 10), 'partial_sum': mp.nstr(partial, 12), 'ratio_to_lambda0': mp.nstr(partial / lam0, 10)}
        print('K', k, checkpoints[k], 's', round(time.monotonic() - t0), flush=True)
largest = sorted(range(len(terms)), key=lambda i: -terms[i])[:8]

# values of f_0 at the endpoints and on both sides of the join (orthonormal Legendre: P_k(-1)=(-1)^k, P_k(1)=1)
def f0_at(interval, side):
    s_, ell, modes = intervals[interval]; off = 0 if interval == 0 else no
    return sum(f0[off + k] * mp.sqrt((2 * k + 1) / ell) * ((-1) ** k if side == 'left' else 1) for k in range(modes))
f0_values = {'x=0': mp.nstr(f0_at(0, 'left'), 6), 'x=a-': mp.nstr(f0_at(0, 'right'), 6), 'x=a+': mp.nstr(f0_at(1, 'left'), 6), 'x=L_q': mp.nstr(f0_at(1, 'right'), 6),
             'norm_check': mp.nstr(sum(f0[i] ** 2 for i in range(n)), 12)}
print('f0 values', f0_values, flush=True)

# envelope of |F_0| at low frequency and between zeros
grid = [mp.mpf(x) / 2 for x in range(0, 61)] + [mp.mpf(x) for x in (35, 40, 50, 60, 80, 100, 150, 200, 300, 500, 700)]
envelope = [(mp.nstr(t, 6), mp.nstr(abs(F0(t)), 6)) for t in grid]
print('envelope |F_0| at tau=0..30:', [e for e in envelope if mp.mpf(e[0]) <= 30][::4], flush=True)

# hypothetical off-line pair
deltas = [mp.mpf(d) for d in ('0.02', '0.05', '0.1', '0.2', '0.3', '0.45')]
heights = [(gammas[i] + gammas[i + 1]) / 2 for i in range(min(len(gammas) - 1, 12))] + [mp.mpf(x) for x in (100, 200, 500)]
pair = []
for t in heights:
    row = {'t': mp.nstr(t, 8), 'on_line_term_2F2': mp.nstr(2 * abs(F0(t)) ** 2, 6)}
    for d in deltas:
        Fp, Fm = F0(t + 1j * d), F0(t - 1j * d)
        Delta = 2 * mp.re(Fp * mp.conj(Fm))
        row[f'delta_{mp.nstr(d,3)}'] = mp.nstr(Delta, 6)
    pair.append(row)
    print('pair', row, flush=True)

out = {'scope': 'Fourier-side diagnostic: zero sums for the lowest eigenvector of the first-step spatial head; midpoints and mpmath only.',
       'head_source': {k: data[k] for k in ('archive', 'matrix_archive_sha256', 'matrices_content_sha256', 'max_radius')},
       'digits': 60, 'zeros_used': K, 'highest_zero': mp.nstr(gammas[-1], 12),
       'lambda_0': mp.nstr(lam0, 20), 'next_eigenvalues': [mp.nstr(E[order[k]], 12) for k in (1, 2, 3, 4)],
       'f0_values': f0_values,
       'partial_sums': checkpoints, 'largest_terms': [{'index': i + 1, 'height': mp.nstr(gammas[i], 10), 'term_2F2': mp.nstr(2 * terms[i], 8)} for i in largest],
       'envelope_abs_F0': envelope, 'hypothetical_pair': pair,
       'seconds': time.monotonic() - t0}
Path(out_path).write_text(json.dumps(out, indent=2) + '\n')
print('done', round(time.monotonic() - t0), 's')
