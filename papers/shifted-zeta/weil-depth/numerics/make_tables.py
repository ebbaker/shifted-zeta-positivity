#!/usr/bin/env python3
"""Generate the LaTeX tables of the manuscript from the JSON records in output/.
Writes manuscript/tables_main.tex and manuscript/tables_certificate.tex (input by
finite_horizon_weil.tex) and output/paper_numbers.json.

Rounding policy (v0.4).  Every enclosed quantity is stored as an Arb ball string
'[mid +/- rad]'.  A displayed lower value is the LOWER endpoint mid-rad rounded DOWN,
so the true quantity is at least the printed number; a displayed upper value is the
UPPER endpoint mid+rad rounded UP, so the true quantity is at most the printed number.
Exact rationals (floors, shifts, decays) are printed exactly, and the script asserts
this.  Only floating-point diagnostics (head eigenvalues, relative coupling) are rounded
to nearest, and their captions say so.  The radius is never discarded before rounding.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN

getcontext().prec = 120          # well above the 35-40 digits of the printed balls

root = Path(__file__).resolve().parent
folders = ['log2_N128', 'log3_N128', 'log4_N128', 'log5_N128', 'log6_N128', 'length_1p8_N128', 'log7_N128']
labels = {'log2': r'$\log2$', 'log3': r'$\log3$', 'log4': r'$\log4$', 'log5': r'$\log5$', 'log6': r'$\log6$',
          '9/5': r'$9/5$', 'log7': r'$\log7$'}


def ball(s):
    """Arb ball string '[mid +/- rad]' (or '[+/- rad]', or a plain decimal) -> (lower, upper) as exact Decimals."""
    if not isinstance(s, str):
        s = repr(s)
    s = s.strip()
    if s.startswith('['):
        body = s[1:-1].strip()
        if '+/-' in body:
            mid, rad = body.split('+/-')
            mid = Decimal(mid.strip() or '0')
            rad = Decimal(rad.strip())
        else:
            mid, rad = Decimal(body), Decimal(0)
        assert rad >= 0
        return mid - rad, mid + rad
    x = Decimal(s)
    return x, x


def _endpoint(s, mode):
    lo, hi = ball(s)
    if mode == 'lower':
        return lo, ROUND_FLOOR
    if mode == 'upper':
        return hi, ROUND_CEILING
    if mode == 'nearest':                       # diagnostics only
        return (lo + hi) / 2, ROUND_HALF_EVEN
    if mode == 'exact':
        assert lo == hi, f'{s!r} is not an exact value'
        return lo, ROUND_FLOOR
    raise ValueError(mode)


def sci(s, mode, sig=3):
    """Directed rounding of an enclosure endpoint to `sig` significant figures, as LaTeX a\\times10^{b}.

    mode='lower': lower endpoint rounded down (true value >= printed);
    mode='upper': upper endpoint rounded up (true value <= printed);
    mode='exact': the value must be an exact decimal with at most `sig` significant figures;
    mode='nearest': midpoint rounded to nearest (floating-point diagnostics only)."""
    x, rnd = _endpoint(s, mode)
    assert x > 0, f'non-positive value {s!r}'
    e = x.adjusted()
    q = x.scaleb(-e)                           # 1 <= q < 10, exact
    q = q.quantize(Decimal(1).scaleb(-(sig - 1)), rounding=rnd)
    if q >= 10:
        q = q.scaleb(-1); e += 1
    if mode == 'exact':
        assert q.scaleb(e) == x, f'{s!r} is not exact to {sig} significant figures'
    m = format(q, 'f').rstrip('0').rstrip('.')
    if e == 0:
        return m
    return f'{m}\\times10^{{{e}}}'


def plain(s, mode, dec=4):
    """Directed rounding of an enclosure endpoint to `dec` decimal places (same modes as sci)."""
    x, rnd = _endpoint(s, mode)
    return format(x.quantize(Decimal(1).scaleb(-dec), rounding=rnd), 'f')


rows = []
for f in folders:
    e = json.loads((root/'output'/f/'enclosure.json').read_text())
    c = json.loads((root/'output'/f/'central_certificate.json').read_text())
    a = json.loads((root/'output'/f/'analysis.json').read_text())
    assert c['status'] == 'PASS' and a['continuation']['status'] == 'PASS'
    assert F(c['central_coercivity']) == F(e['central_floor_rational'])
    assert F(a['continuation']['shift_maximum']) == F(e['continuation']['shift_rational'])
    assert F(a['continuation']['decay_coefficient']) == F(e['continuation']['decay_rational'])
    assert F(e['central_floor']) == F(e['central_floor_rational'])
    for sec in ('even', 'odd'):
        assert F(e['sectors'][sec]['certified_floor']) == F(e['sectors'][sec]['certified_floor_rational'])
    rows.append((e, c, a))

out = []
# ---- Table: main theorem
out.append(r'''\begin{table}[ht]
\centering
\caption{Certified two-sided bounds and continuation constants (Theorem~\ref{thm:main}). $m_j$ is an exact rational passing the full-operator test in both reflection sectors; $\mu_j$ is a certified upper bound (upper endpoint of the ball evaluation, rounded up). $C_j$ is an integer exceeding the generator constant $C_{L_j}$ of \eqref{eq:CL}, and $h_j$, $d_j$ are exact decimals satisfying $m_j-C_jh_j^2/3\ge d_j$.}
\label{tab:main}
\small\setlength{\tabcolsep}{4pt}\begin{tabular}{@{}lclllrll@{}}
\toprule
$L_j$ & value & delays & floor $m_j$ & upper $\mu_j$ & $C_j$ & shift $h_j$ & decay $d_j$\\
\midrule''')
for e, c, a in rows:
    act = ', '.join(str(n) for n, p, k in e['active_prime_powers']) or 'none'
    out.append(f"{labels[e['horizon_label']]} & {plain(e['horizon_value'],'nearest',3)} & {act} & ${sci(e['central_floor'],'exact')}$ & ${sci(e['sectors']['even']['certified_upper_bound'],'upper')}$ & {e['continuation']['generator_bound']} & ${sci(e['continuation']['shift_maximum'],'exact',sig=1)}$ & ${sci(e['continuation']['decay'],'exact',sig=1)}$\\\\")
out.append(r'''\bottomrule
\end{tabular}
\end{table}''')

# ---- Table: sectors
out.append(r'''\begin{table}[ht]
\centering
\caption{Sector-wise enclosures. Floors are exact rationals passing the sector test; upper bounds are ball Rayleigh quotients plus the profile error, upper endpoints rounded up. In every row the even upper bound lies below the odd floor, so the bottom of the spectrum lies in the even sector.}
\label{tab:sectors}
\begin{tabular}{@{}lllll@{}}
\toprule
Horizon & even floor & even upper bound & odd floor & odd upper bound\\
\midrule''')
for e, c, a in rows:
    s = e['sectors']
    out.append(f"{labels[e['horizon_label']]} & ${sci(s['even']['certified_floor'],'exact')}$ & ${sci(s['even']['certified_upper_bound'],'upper')}$ & ${sci(s['odd']['certified_floor'],'exact')}$ & ${sci(s['odd']['certified_upper_bound'],'upper')}$\\\\")
    # certified statement: even upper bound (upper endpoint of its ball) < odd floor (exact rational)
    assert F(ball(s['even']['certified_upper_bound'])[1]) < F(s['odd']['certified_floor_rational'])
    # and the tabulated (rounded-up) even upper bound is at least the floor of its own sector
    assert F(ball(s['even']['certified_upper_bound'])[1]) >= F(s['even']['certified_floor_rational'])
out.append(r'''\bottomrule
\end{tabular}
\end{table}''')

# ---- Table: certificate data
out.append(r'''\begin{table}[ht]
\centering
\caption{Certificate data at $N=128$. The tail floor $a_{128,L}$ is an outward lower value of \eqref{eq:tailformula} (lower endpoint, rounded down); $\epsilon$ is the outward upper value of \eqref{eq:eps} subtracted before each sign test (upper endpoint, rounded up); pivots are lower values of the smallest LDL pivots at the floor $m_j$ (rounded down; summaries, not spectral bounds); the radius is the largest ball radius among the four saved matrices (upper endpoint, rounded up). ``Required'' is the floating-point diagnostic $\lambda_{\max}(q_r^{-1/2}E_rq_r^{-1/2})$, the tail floor the model test would need at level zero, rounded to nearest. The certified endpoints themselves are in the JSON records.}
\label{tab:certificate}
\footnotesize\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{@{}lrrllllll@{}}
\toprule
$L$ & $M$ & bits & $a_{128,L}$ & $\epsilon$ & pivot (even) & pivot (odd) & radius & required\\
\midrule''')
for e, c, a in rows:
    piv = [ch['minimum_pivot_lower'] for ch in c['checks']]
    assert [ch['parity'] for ch in c['checks']] == [0, 1], 'checks must be ordered even (parity 0), odd (parity 1)'
    req = ' / '.join(f"{r['maximum']:.3f}" for r in a['relative_coupling'])
    out.append(f"{labels[e['horizon_label']]} & {c['M']} & {c['precision_bits']} & {plain(e['tail_floor_lower'],'lower',4)} & ${sci(c['model_error'],'upper')}$ & ${sci(piv[0],'lower')}$ & ${sci(piv[1],'lower')}$ & ${sci(c['maximum_matrix_radius'],'upper',sig=2)}$ & {req}\\\\")
out.append(r'''\bottomrule
\end{tabular}
\end{table}''')

# ---- Table: head spectra (diagnostic) at 9/5 and log7
def eigs(e, sector, k=5):
    return ',\ '.join('$'+sci(v,'nearest')+'$' for v in e['sectors'][sector]['head_eigenvalues_lowest_diagnostic'][:k])
e15 = rows[5][0]; e7 = rows[6][0]
assert e15['horizon_label'] == '9/5' and e7['horizon_label'] == 'log7'
out.append(r'''\begin{table}[ht]
\centering
\caption{Lowest five eigenvalues of the $64\times64$ head $q_r$ in each sector (floating-point diagnostics from the ball midpoints, rounded to nearest; not certified). The certified statements are the enclosures of Tables~\ref{tab:main} and~\ref{tab:sectors}.}
\label{tab:spectra}
\small
\begin{tabular}{@{}lll@{}}
\toprule
Horizon & sector & lowest five head eigenvalues\\
\midrule''')
out.append(f"$9/5$ & even & {eigs(e15,'even')}\\\\")
out.append(f"$9/5$ & odd & {eigs(e15,'odd')}\\\\")
out.append(f"$\\log7$ & even & {eigs(e7,'even')}\\\\")
out.append(f"$\\log7$ & odd & {eigs(e7,'odd')}\\\\")
out.append(r'''\bottomrule
\end{tabular}
\end{table}''')

split = next(i for i, x in enumerate(out) if 'label{tab:certificate}' in x)
(root.parent/'manuscript'/'tables_main.tex').write_text('\n'.join(out[:split])+'\n')
(root.parent/'manuscript'/'tables_certificate.tex').write_text('\n'.join(out[split:])+'\n')

# machine-readable summary for the text: certified endpoints (not midpoints) as decimal strings
def lo(s): return str(ball(s)[0].normalize())
def hi(s): return str(ball(s)[1].normalize())
summ = {e['horizon_label']: {
        'm': e['central_floor'],
        'mu_even_upper': hi(e['sectors']['even']['certified_upper_bound']),
        'm_odd': e['sectors']['odd']['certified_floor'],
        'mu_odd_upper': hi(e['sectors']['odd']['certified_upper_bound']),
        'C': e['continuation']['generator_bound'], 'h': e['continuation']['shift_maximum'], 'd': e['continuation']['decay'],
        'margin': e['continuation']['exact_margin'],
        'a_lower': lo(e['tail_floor_lower']),
        'CL_upper': hi(e['generator_change_constant']),
        'eps_upper': hi(c['model_error']),
        'radius_upper': hi(c['maximum_matrix_radius']),
        'req': [r['maximum'] for r in a['relative_coupling']],
        'note': 'endpoints of the saved enclosures (lower endpoint for lower values, upper endpoint for upper values); the tables round these outward'}
        for e, c, a in rows}
(root/'output'/'paper_numbers.json').write_text(json.dumps(summ, indent=1)+'\n')
print('tables written')
