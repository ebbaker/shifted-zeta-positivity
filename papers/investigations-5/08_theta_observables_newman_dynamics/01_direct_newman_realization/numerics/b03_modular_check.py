"""One local check for Note11, 10 November 2026, America/New_York.

Prepared for Edward Baker with OpenAI Codex LLM assistance, chat0008.
Actual model/effort unavailable in recorded source metadata.
Exact rational algebra plus three fixed-radius Decimal diagnostics;
not interval arithmetic, an A0 calculation, or a positivity certificate.
Uses only the Python standard library. Run from any directory.
"""

from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from math import factorial
import hashlib
import json
import platform


def pi_machin():
    # Guard digits, rounded to the caller's precision on return.
    with localcontext() as ctx:
        ctx.prec = 95

        def atan_inverse(n):
            z = D(1) / n
            term = z
            total = z
            for k in range(1, 300):
                term *= -z * z
                addition = term / (2 * k + 1)
                total += addition
                if abs(addition) < D('1e-100'):
                    break
            else:
                raise AssertionError('Fixed Machin-series bound exhausted')
            return total

        value = 16 * atan_inverse(5) - 4 * atan_inverse(239)
    return +value


def main():
    # Each inverted psi(u)du contributes J(x)x^(-3/2)dx/4.
    bulk = F(1, 64) * F(1, 4) ** 2
    face = F(1, 64) * F(1, 4)
    assert bulk == F(1, 1024) and face == F(1, 256)
    assert F(1, 2) - 2 == -F(3, 2)   # r=1/x, dr=-x^(-2)dx
    assert F(1, 8) - F(3, 2) * F(1, 16) == F(1, 32)

    # D_p and E_x have the same eigenvalue on r^n=x^(-n).
    for n in range(-4, 5):
        assert (2 * n) ** 2 - 1 == (2 * -n) ** 2 - 1

    # Exact formal expansion of AB-(A-E)(B-F).
    # Indeterminates are A, B, E, F; coefficients retained explicitly.
    left = {(1, 1, 0, 0): F(1)}
    retained = {(1, 1, 0, 0): F(1), (1, 0, 0, 1): F(-1),
                (0, 1, 1, 0): F(-1), (0, 0, 1, 1): F(1)}
    for key, value in retained.items():
        left[key] = left.get(key, F(0)) - value
    left = {key: value for key, value in left.items() if value}
    assert left == {(1, 0, 0, 1): F(1), (0, 1, 1, 0): F(1),
                    (0, 0, 1, 1): F(-1)}

    # Rational payments used with pi>3, not decimal approximations to a proof.
    assert sum(F(6 ** k, factorial(k)) for k in range(5)) > 101
    assert sum(F(9 ** k, factorial(k)) for k in range(8)) > 2000
    assert F(1) + 15 > 2

    rows = []
    with localcontext() as ctx:
        ctx.prec = 80
        pi = pi_machin()

        def term(n, r):
            return (-pi * D(n * n) * r * r).exp()

        def envelope(m, r):
            return term(m + 1, r) / (1 - (-pi * (2 * m + 3) * r * r).exp())

        for radius in (1, 2, 4):
            r = D(radius)
            s = 1 / r
            a = sum((term(n, r) for n in range(1, 65)), D(0))
            dual_full = sum((term(n, s) for n in range(1, 129)), D(0))
            dual_residual = ((1 + 2 * dual_full) / r - 1) / 2
            assert abs(a - dual_residual) < D('1e-70')
            assert envelope(64, r) / a < D('1e-100')
            assert envelope(128, s) / r / a < D('1e-100')
            for cutoff in sorted({radius, radius * radius}):
                c = ((1 + 2 * sum((term(n, s) for n in range(1, cutoff + 1)), D(0))) / r - 1) / 2
                e = sum((term(n, s) for n in range(cutoff + 1, 129)), D(0)) / r
                direct_tail = sum((term(n, r) for n in range(cutoff + 1, 65)), D(0))
                upper = envelope(cutoff, s) / r
                assert abs(a - c - e) < D('1e-70')
                assert e >= direct_tail
                assert upper >= envelope(cutoff, r)
                assert e <= upper * (1 + D('1e-70'))
                if cutoff == radius * radius:
                    assert e / a < D('0.01')
                rows.append({'r': radius, 'M': cutoff,
                             'dual_retained_sign': 1 if c > 0 else -1 if c < 0 else 0,
                             'dual_relative_error': format(e / a, '.18E'),
                             'direct_relative_error': format(direct_tail / a, '.18E'),
                             'dual_geometric_relative_envelope': format(upper / a, '.18E')})

    here = Path(__file__).resolve()
    note = here.parent.parent / 'notes/11_TND_D_B03_SIMULTANEOUS_MODULAR_COMPARISON_20261110.md'
    record = {
        'date_local': '2026-11-10',
        'recorded_at_local': datetime.now(ZoneInfo('America/New_York')).isoformat(),
        'prepared_for': 'Edward Baker', 'assistance': 'OpenAI Codex LLM',
        'actual_model': None, 'actual_reasoning_effort': None,
        'thread_id': '01a1c3dc-12e9-7023-a3e1-bc27d98d94d0',
        'turn_id': '01a1c3dc-b3f4-7bf3-8174-d2fa06b39e34',
        'task': 'TND-D-B03 single local check', 'status': 'passed',
        'python': platform.python_version(),
        'exact_checks': ['bulk coefficient 1/1024', 'face coefficient 1/256',
                         'inverse-radius weight x^(-3/2)',
                         'Euler derivative pullback on Laurent monomials',
                         'negative mixed product in the exact remainder',
                         'resolving beta minimum 1/32',
                         'coarse 1/100 dual and 1/1000 direct relative constants'],
        'floating_diagnostics': {
            'arithmetic': 'Python Decimal, 80 decimal digits; not interval arithmetic',
            'pi': 'Machin formula, 95 guard digits, bounded series',
            'radii': [1, 2, 4], 'original_reference_cutoff': 64,
            'dual_reference_cutoff': 128,
            'reference_tail_check': 'Geometric envelopes below 1e-100 relative, evaluated in Decimal; not certified rounding',
            'rows': rows},
        'scope': 'Checks constants and representative cancellation only. Universal statements are proved analytically in Note11. No A0 integration, collision scan, certificate, runtime comparison, or independent review.',
        'script_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
        'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest()}
    target = here.parent / '03_TND_D_B03_MODULAR_CHECK_20261110.json'
    target.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'record': str(target), 'diagnostics': rows}, indent=2))


if __name__ == '__main__':
    main()
