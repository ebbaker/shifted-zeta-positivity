#!/usr/bin/env python3
"""Complete paid candidate atlas, with all genuine terms and closed coverage.

The independent Note 3 source is preserved and hash-checked before import.
Only standard-library outward Decimal arithmetic decides assertions. A
degree-63 signed coherent polynomial, with a 64th absolute moment, covers
the entire height interval. Adaptive closed strips certify every point.
"""
import argparse
import hashlib
import json
import platform
from decimal import Decimal
from pathlib import Path

SOURCE = Path(__file__).with_name('check_complete_current_rectangle.py')
EXPECTED_SOURCE_SHA256 = 'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'
if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED_SOURCE_SHA256:
    raise RuntimeError('Preserved Note 3 source hash mismatch; restore before replay.')
from check_complete_current_rectangle import (
    I, DOWN, UP, PRECISION, real_data, absmax, add, rotate, padded,
    pi_interval, reduced_trig, factorial, serialize_complex)

M, ORDER = 22066, 64


def absmin(z):
    if z.lo <= 0 <= z.hi:
        return Decimal(0)
    return min(z.lo.copy_abs(), z.hi.copy_abs())


def polynomial_shift(coefficients, center):
    """Exact polynomial identity P(center+z), evaluated outward."""
    out = [coefficients[-1]]
    for coefficient in reversed(coefficients[:-1]):
        out = [center*out[0]+coefficient] + [
            out[k-1]+center*out[k] for k in range(1, len(out))] + [out[-1]]
    return out


def polynomial_value(coefficients, offset):
    out = I(0)
    for coefficient in reversed(coefficients):
        out = out*offset+coefficient
    return out


def check_polynomial_identity():
    from fractions import Fraction
    for degree in range(7):
        coefficients = [I.rational(Fraction((-1)**k, k+1))
                        for k in range(degree+1)]
        for center in ('-4', '0', '3/2'):
            m = I.rational(center)
            shifted = polynomial_shift(coefficients, m)
            for offset in ('-1/8', '0', '1/8'):
                z = I.rational(offset)
                left = polynomial_value(coefficients, m+z)
                right = polynomial_value(shifted, z)
                assert left.lo <= right.hi and right.lo <= left.hi
    return 63


def enclose():
    polynomial_identity_checks = check_polynomial_identity()
    pi, logM = pi_interval(), I(M).ln()
    L0, t0 = 2*logM, 1/(2*logM)
    x0, hbox, middle = 4*pi*M*M, I(0, 8), I(4)
    tbox = I(t0.lo, '0.05')
    dt = I(0, UP.subtract(Decimal('0.05'), t0.lo))
    xbox = x0+hbox
    Lbox = (xbox/(4*pi)).ln()
    kappa_upper = (tbox*Lbox).hi
    # Exact identities t0*L0=1 and x0/(4*pi)=M^2, and h>=0,
    # prove kappa>=1 without treating dependent intervals as independent.
    assert tbox.lo > 0 and t0.hi < Decimal('0.05')
    assert kappa_upper < 2
    cutoff_squared = xbox/(4*pi)+tbox/16
    assert cutoff_squared.lo > M*M
    assert cutoff_squared.hi < (M+1)*(M+1)

    ar, ai, U, V, c, Omega, atanx, lc = real_data(x0, t0, pi)
    aN = I('0.5')+t0*ar/2-t0*logM/2
    T = (x0-t0*ai)/2
    wN = (t0*logM*logM/4-(I('0.5')+t0*ar/2)*logM).exp()
    carrier = pi*(M % 2)-pi+atanx/4-x0*lc/8+t0*ai*(ar-logM)/2
    csine, ccosine = reduced_trig(carrier, pi)
    sar, sai, sU, sV, sc, sOmega, _, _ = real_data(xbox, t0, pi)
    bar, bai, bU, bV, bc, bOmega, _, _ = real_data(xbox, tbox, pi)
    moments = [[I(0), I(0)] for _ in range(ORDER)]
    absolute_moment = I(0)
    spatial_error0, spatial_error1 = I(0), I(0)
    time_budget0, time_budget1 = I(0), I(0)
    max_spatial_residual = Decimal(0)

    for n in range(1, M+1):
        delta = (I(M)/n).ln()
        ell, omega = logM-delta, delta/2
        amp = (aN*delta+t0*delta*delta/4).exp()
        w0 = wN*amp
        sine, cosine = reduced_trig(-T*delta-middle*omega, pi)
        q = [amp*cosine, amp*sine]
        power = I(1)
        for k in range(ORDER):
            moments[k] = add(moments[k], [power*q[0], power*q[1]])
            power *= omega
        absolute_moment += w0*power

        # Exact physical spatial gamma and centered residual gamma+i*omega.
        residual_imag = sOmega-sc*logM+(sc-I('0.5'))*delta
        residual = I(absmax(t0*sV*ell/4))+I(absmax(residual_imag))
        max_spatial_residual = max(max_spatial_residual, residual.hi)
        growth = (8*residual).exp()
        exp_error = I(0, UP.subtract(growth.hi, Decimal(1)))
        spatial_error0 += w0*exp_error
        spatial_error1 += w0*(omega*exp_error+residual*growth)

        # Fixed physical x and N: q_t=chi*q; q_xt=(gamma_t+gamma*chi)*q.
        wb = (tbox*ell*ell/4-(I('0.5')+tbox*bar/2)*ell).exp()
        chi = I(absmax(ell*ell/4-bar*ell/2))+I(absmax(bai*(bar-ell)/2))
        gamma = I(absmax(tbox*bV*ell/4))+I(absmax(bOmega-bc*ell))
        gamma_t = I(absmax(bV*ell/4))+I(absmax((bU*(bar-ell)-bai*bV)/4))
        time_budget0 += wb*chi
        time_budget1 += wb*(gamma_t+gamma*chi)

    jets = []
    for k, moment in enumerate(moments):
        jet = rotate(moment, csine, ccosine, wN)
        for _ in range(k % 4):
            jet = [jet[1], -jet[0]]
        jets.append(jet)
    remainder0 = (absolute_moment*I(4)**ORDER/factorial(ORDER)).hi
    remainder1 = (absolute_moment*I(4)**(ORDER-1)/factorial(ORDER-1)).hi
    error0 = (I(remainder0)+spatial_error0+dt*time_budget0).hi
    error1 = (I(remainder1)+spatial_error1+dt*time_budget1).hi
    coefficients = [[jet[k]/factorial(j) for j, jet in enumerate(jets)]
                    for k in range(2)]
    eta = 5*(-tbox*Lbox*Lbox/16-Lbox/4).exp()
    derivative_payment = Lbox*eta
    epsilon = (eta/2).hi
    derivative_epsilon = (derivative_payment/2).hi

    def observed(lo, hi):
        center = (I(lo)+I(hi))/2
        radius = (I(hi)-I(lo))/2
        shifted = [polynomial_shift(a, center-middle) for a in coefficients]
        z = I(radius.hi.copy_negate(), radius.hi)
        value = [polynomial_value(a, z) for a in shifted]
        derivative = [polynomial_value([k*a[k] for k in range(1, len(a))], z)
                      for a in shifted]
        return padded(value, error0), padded(derivative, error1)

    leaves = []
    max_depth = 12

    def certify(lo, hi, depth=0):
        S, D = observed(lo, hi)
        umin, dmin = absmin(S[0]), absmin(D[0])
        value_gap = DOWN.subtract(umin, epsilon)
        derivative_gap = DOWN.subtract(dmin, derivative_epsilon)
        current = D[0]*S[1]-S[0]*D[1]
        current_tolerance = eta/2*(Lbox*I(absmax(S[1]))+I(absmax(D[1])))
        current_gap = DOWN.subtract(absmin(current), current_tolerance.hi)
        # Both necessary rectangular candidate tolerances are retained.
        # The correlated Schwarz-Pick candidate bound is reported as an
        # additional audit quantity; coverage does not depend on it.
        correlated_candidate = (2*I(umin)/I(eta.hi))**2 \
            +2*I(dmin)/I(derivative_payment.hi)
        if value_gap > 0:
            kind = 'value_pruned'
            joint_lower = DOWN.subtract(DOWN.multiply(Decimal(2), umin), eta.hi)
        elif derivative_gap > 0 and current_gap > 0:
            kind = 'paid_candidate_current_and_derivative'
            joint_lower = DOWN.subtract(DOWN.divide(DOWN.multiply(Decimal(2), dmin), Lbox.hi), eta.hi)
        else:
            assert depth < max_depth, ('unresolved closed cell', str(lo), str(hi))
            mid = (I(lo)+I(hi))/2
            assert mid.lo == mid.hi
            certify(lo, mid.lo, depth+1)
            certify(mid.hi, hi, depth+1)
            return
        assert joint_lower > 0
        leaves.append({
            'height_offset': [str(lo), str(hi)], 'depth': depth, 'kind': kind,
            'complete_S': serialize_complex(S), 'physical_Sprime': serialize_complex(D),
            'value_candidate_gap': str(value_gap),
            'derivative_candidate_gap': str(derivative_gap),
            'complete_current': current.strings(),
            'rectangular_current_tolerance': current_tolerance.strings(),
            'paid_current_gap': str(current_gap),
            'correlated_candidate_lower': str(correlated_candidate.lo),
            'normalized_joint_vector_lower': str(joint_lower),
        })

    certify(Decimal(0), Decimal(8))
    assert leaves[0]['height_offset'][0] == '0'
    assert leaves[-1]['height_offset'][1] == '8'
    for left, right in zip(leaves, leaves[1:]):
        assert Decimal(left['height_offset'][1]) == Decimal(right['height_offset'][0])
    assert sum((Decimal(c['height_offset'][1])-Decimal(c['height_offset'][0])
                for c in leaves), Decimal(0)) == 8
    candidate = [c for c in leaves if c['kind'] != 'value_pruned']
    assert candidate
    groups = []
    for cell in candidate:
        if groups and groups[-1][-1]['height_offset'][1] == cell['height_offset'][0]:
            groups[-1].append(cell)
        else:
            groups.append([cell])

    zero_bands = []
    for group in groups:
        lo, hi = Decimal(group[0]['height_offset'][0]), Decimal(group[-1]['height_offset'][1])
        leftS, _ = observed(lo, lo)
        rightS, _ = observed(hi, hi)
        Qleft = 2*leftS[0]+I(eta.hi.copy_negate(), eta.hi)
        Qright = 2*rightS[0]+I(eta.hi.copy_negate(), eta.hi)
        dintervals = [I(*c['physical_Sprime']['real']) for c in group]
        Qprime = 2*I(min(d.lo for d in dintervals), max(d.hi for d in dintervals)) \
            +I(derivative_payment.hi.copy_negate(), derivative_payment.hi)
        assert (Qleft.hi < 0 < Qright.lo and Qprime.lo > 0) \
            or (Qright.hi < 0 < Qleft.lo and Qprime.hi < 0)
        zero_bands.append({'height_offset': [str(lo), str(hi)],
                           'Q_left_all_times': Qleft.strings(),
                           'Q_right_all_times': Qright.strings(),
                           'Qprime_entire_band_all_times': Qprime.strings(),
                           'unique_simple_H_zero_per_time': True})
    assert len(zero_bands) == 13
    minimum_joint = min(Decimal(c['normalized_joint_vector_lower']) for c in leaves)
    minimum_current_gap = min(Decimal(c['paid_current_gap']) for c in candidate)
    candidate_width = sum((Decimal(c['height_offset'][1])-Decimal(c['height_offset'][0])
                           for c in candidate), Decimal(0))
    assert len(leaves) == 46 and len(candidate) == 17 and candidate_width == Decimal('2.25')
    assert minimum_joint > Decimal('0.03728')
    assert minimum_current_gap > Decimal('0.11934')
    assert eta.hi < Decimal('0.009642') and derivative_payment.hi < Decimal('0.192864')
    assert remainder0 < Decimal('0.000001480') and remainder1 < Decimal('0.000023678')
    assert error0 < Decimal('0.019732') and error1 < Decimal('0.019684')
    return {
        'status': 'PASS',
        'scope': 'closed finite height/time rectangle; complete paid candidate exclusion; exactly thirteen simple genuine heat zeros at every time; no sectorwide theorem',
        'M': M, 'N': M, 'number_of_genuine_terms': M,
        'decimal_precision': PRECISION, 'Taylor_order': ORDER,
        'polynomial_shift_identity_checks': polynomial_identity_checks,
        'rectangle': {
            'center_height': x0.strings(), 'base_time': t0.strings(),
            'height_offset': hbox.strings(), 'outer_time_enclosure': tbox.strings(),
            'exact_time_domain': ['1/(2*log(22066))', '1/20'],
            'exact_height_domain': ['4*pi*22066^2', '4*pi*22066^2+8'],
            'domain_vs_hull': 'sector theorem is asserted on the exact domain; Decimal outer hulls only bound transport and payments',
            'exact_upper_time': '1/20', 'time_increment_upper': str(dt.hi),
            'L': Lbox.strings(), 'kappa': ['1', str(kappa_upper)],
            'kappa_lower_proof': 'exact t0*L0=1; h>=0 and t>=t0; monotonicity',
            'natural_cutoff_squared': cutoff_squared.strings(),
            'constant_natural_cutoff': True,
        },
        'coherent_model': {
            'midpoint_offset': '4', 'maximum_real_Taylor_radius': '4',
            'signed_midpoint_jets': [serialize_complex(j) for j in jets],
            '64th_absolute_frequency_moment': absolute_moment.strings(),
            'value_Taylor_remainder_upper': str(remainder0),
            'derivative_Taylor_remainder_upper': str(remainder1),
            'maximum_physical_spatial_residual': str(max_spatial_residual),
            'physical_spatial_value_error_upper': str(spatial_error0.hi),
            'physical_spatial_derivative_error_upper': str(spatial_error1.hi),
            'physical_time_value_budget_upper': str(time_budget0.hi),
            'physical_time_derivative_budget_upper': str(time_budget1.hi),
            'total_value_transport_and_Taylor_error': str(error0),
            'total_derivative_transport_and_Taylor_error': str(error1),
        },
        'full_holomorphic_payment': {
            'eta': eta.strings(), 'L_eta': derivative_payment.strings(),
            'value_candidate_tolerance': str(epsilon),
            'derivative_candidate_tolerance': str(derivative_epsilon),
            'source': 'Heat Notes 8 and 13 full symmetric/reflected/cutoff-change disk interface',
            'analytic_input_reproved_here': False,
        },
        'coverage': {
            'number_of_closed_leaves': len(leaves),
            'value_pruned_leaves': len(leaves)-len(candidate),
            'candidate_current_and_derivative_leaves': len(candidate),
            'exact_adjacency_and_total_width_checked': True,
            'all_leaves_cover_entire_exact_closed_time_domain': True,
            'joint_H_Hprime_nonvanishing': True,
            'minimum_normalized_joint_vector_lower': str(minimum_joint),
            'minimum_candidate_current_gap': str(minimum_current_gap),
            'candidate_height_width': str(candidate_width),
            'number_of_unique_simple_zeros_per_time': len(zero_bands),
            'zero_isolating_bands': zero_bands,
        },
        'closed_leaves': leaves,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'preserved_note3_source_sha256': EXPECTED_SOURCE_SHA256,
        'preserved_note2_interval_source_sha256': '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
        'source_hashes_checked_before_import': True,
        'python_version': platform.python_version(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = enclose()
    serialized = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(serialized)
        print(json.dumps({'status': result['status'],
                          'closed_leaves': result['coverage']['number_of_closed_leaves'],
                          'candidate_leaves': result['coverage']['candidate_current_and_derivative_leaves'],
                          'zeros_per_time': result['coverage']['number_of_unique_simple_zeros_per_time'],
                          'minimum_joint_lower': result['coverage']['minimum_normalized_joint_vector_lower'],
                          'minimum_candidate_current_gap': result['coverage']['minimum_candidate_current_gap'],
                          'certificate': str(args.output)}, indent=2))
    else:
        print(serialized, end='')
