#!/usr/bin/env python3
"""Outward actual-theta derivative autocorrelation sign calibration.

This checks a kernel value, not its Fourier sign or positive definiteness.
The whole theta source and a full positive-time interval are retained.
"""
import argparse
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path


HASHES = {
    'check_block_current.py': '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
    'check_complete_current_rectangle.py': 'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path)
    parser.add_argument('--cells', type=int, default=2048)
    parser.add_argument('--interval-source-dir', type=Path,
                        default=Path(__file__).resolve().parents[2]
                        / '13_microlocal_phase_space' / 'numerics')
    args = parser.parse_args()
    assert args.cells > 0
    for name, digest in HASHES.items():
        if hashlib.sha256((args.interval_source_dir / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError('Retained interval source mismatch: ' + name)
    sys.path.insert(0, str(args.interval_source_dir))
    from check_complete_current_rectangle import I, pi_interval, PRECISION

    pi = pi_interval()
    assert pi.lo > 3
    assert (16 * (-3 * pi).exp()).hi < Decimal('.5')
    time = I(0, '.05')
    s = I('.3')
    radius = I(1)
    width = radius / args.cells

    def phi(u):
        assert u.lo >= 0
        e4, e5, e9 = [(u * k).exp() for k in (4, 5, 9)]
        value = I(0)
        for n in (1, 2, 3):
            c = pi * n * n
            value += (2 * c**2 * e9 - 3 * c * e5) * (-c * e4).exp()
        # n^m <= 4^m(5/4)^(m(n-4)), n^2 >=16+9(n-4).
        def omitted(m):
            denominator = 1 - (I(5) / 4)**m * (-9 * pi * e4).exp()
            assert denominator.lo > 0
            return I(4)**m * (-16 * pi * e4).exp() / denominator
        tail = 2 * pi**2 * e9 * omitted(4) + 3 * pi * e5 * omitted(2)
        out = value + I(0, tail.hi)
        assert out.lo > 0
        return out

    def absolute_interval(v):
        if v.lo <= 0 <= v.hi:
            return I(0, max(v.lo.copy_abs(), v.hi.copy_abs()))
        return I(min(v.lo.copy_abs(), v.hi.copy_abs()),
                 max(v.lo.copy_abs(), v.hi.copy_abs()))

    negative_piece = I(0)
    positive_piece = I(0)
    crossing_piece = I(0)
    for j in range(args.cells):
        left = width * j
        right = width * (j + 1)
        r = I(left.lo, right.hi)
        factor = r**2 * (r**2 - s**2)
        density = (2 * time * (s**2 + r**2)).exp() * phi(s + r) * phi(absolute_interval(s - r))
        contribution = 2 * width * factor * density
        if r.hi <= s.lo:
            negative_piece += contribution
        elif r.lo >= s.hi:
            positive_piece += contribution
        else:
            crossing_piece += contribution

    # Phi(u)<=C exp(-8*pi*u^2), C=4*pi^2 exp(-pi), u>=0.
    # Drop each negative summand, use n^4<=16^(n-1),
    # n^2-1>=3(n-1), and the geometric ratio16exp(-3pi)<1/2.
    # Then exp(4u)>=1+4u+8u^2 and4pi>9 imply the envelope.
    # This is the full theta Gaussian envelope, with its negative linear
    # exponent omitted. m_t<=C exp(-a*u^2), a=8*pi-.05.
    # For r>=R=1>s, r^2(r^2-s^2)<=r^4. Integration by parts and
    # the Gaussian Mills bound give the printed outward tail payment.
    C = 4 * pi**2 * (-pi).exp()
    k = 2 * (8 * pi - I('.05'))
    tail = 2 * C**2 * (-k * (s**2 + radius**2)).exp() * (
        radius**3 / (2 * k) + 3 * radius / (4 * k**2) + 3 / (8 * k**3 * radius))
    complete = negative_piece + positive_piece + crossing_piece + I(0, tail.hi)
    assert complete.hi < 0
    record = {
        'status': 'PASS',
        'date': '2026-10-10',
        'prepared_for': 'Edward Baker',
        'model': 'GPT-6 (Codex)',
        'reasoning_effort': 'Not exposed in this session; not inferred',
        'acknowledgment': 'Substantial LLM assistance; internal outward replay, not independent validation.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'imported_sources': HASHES,
        'arithmetic': str(PRECISION) + '-digit outward Decimal with corrected integer powers; no binary floating sign tests',
        'time_interval': time.strings(),
        'kernel_argument_s': s.strings(),
        'kernel_definition': 'J1(s)=integral_R r^2(r^2-s^2)e^(2t(s^2+r^2))Phi_e(s+r)Phi_e(s-r) dr',
        'integration': {
            'positive_half_radius': radius.strings(),
            'interval_cells': args.cells,
            'theta_terms': [1, 2, 3],
            'omitted_theta_terms': 'Full pointwise positive geometric bounds for n>=4 included in every cell',
            'negative_region_contribution': negative_piece.strings(),
            'positive_region_contribution': positive_piece.strings(),
            'crossing_region_contribution': crossing_piece.strings(),
            'r_above_1_full_theta_tail_upper': str(tail.hi),
        },
        'full_kernel_enclosure': complete.strings(),
        'scope': 'Genuine theta J1(.3)<0 uniformly 0<=t<=.05. A negative kernel value does not refute positive definiteness or a Fourier sign. No stationary sign or collision exclusion is proved by this record.',
    }
    if args.record:
        args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': record['status'], 'J1': complete.strings(),
                      'time_interval': time.strings(), 'cells': args.cells}, indent=2))


if __name__ == '__main__':
    main()
