#!/usr/bin/env python3
"""Complete genuine current and a paid rectangle of unique simple heat zeros.

This imports, but never changes, the old 60-digit interval arithmetic source.
All transported phases, spatial drift, time drift and holomorphic remainder
payments are included. No ordinary binary floating point enters a sign test.
"""
import argparse
import hashlib
import json
import platform
from decimal import Decimal
from pathlib import Path

INTERVAL_SOURCE = Path(__file__).with_name('check_block_current.py')
EXPECTED_INTERVAL_SHA256 = '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2'
if hashlib.sha256(INTERVAL_SOURCE.read_bytes()).hexdigest() != EXPECTED_INTERVAL_SHA256:
    raise RuntimeError('Imported Note 2 interval source hash mismatch; restore its retained source before replay.')

from check_block_current import (I, DOWN, UP, PRECISION, atan_small, pi_interval,
                                 reduced_trig, product_real, product_imag,
                                 factorial)


def integer_power(value, power):
    """Enclose integer powers using only guaranteed directed multiplication.

    Decimal's C Context.power is not guaranteed correctly rounded in every
    case. Keep the imported source intact, and override its integer powers
    for this certificate. Repeated multiplication also handles directed
    underflow at the tiny adjacent endpoints of ln(1).
    """
    assert isinstance(power, int) and power >= 0
    if power == 0:
        return I(1)

    def endpoint_bounds(endpoint):
        magnitude = endpoint.copy_abs()
        low, high = Decimal(1), Decimal(1)
        for _ in range(power):
            low = DOWN.multiply(low, magnitude)
            high = UP.multiply(high, magnitude)
        if endpoint < 0 and power % 2:
            return high.copy_negate(), low.copy_negate()
        return low, high

    left, right = endpoint_bounds(value.lo), endpoint_bounds(value.hi)
    upper = max(left[1], right[1])
    if power % 2 == 0 and value.lo <= 0 <= value.hi:
        return I(0, upper)
    return I(min(left[0], right[0]), upper)


I.__pow__ = integer_power


def absmax(value):
    return max(value.lo.copy_abs(), value.hi.copy_abs())


def add(a, b):
    return [a[0]+b[0], a[1]+b[1]]


def rotate(z, sine, cosine, weight=I(1)):
    return [weight*(cosine*z[0]-sine*z[1]),
            weight*(cosine*z[1]+sine*z[0])]


def multiply(a, b):
    return [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]]


def padded(z, bound):
    return [v+I(bound.copy_negate(), bound) for v in z]


def overlap(a, b):
    return a.lo <= b.hi and b.lo <= a.hi


def real_data(x, t, pi):
    x2 = x*x
    atanx = pi/2-atan_small(1/x, 6)
    log_correction = (1+1/x2).ln()
    ar = (x/(4*pi)).ln()/2+log_correction/4-1/(1+x2)
    ai = 3*x/(1+x2)-atanx/2
    U = (7*x2-5)/((1+x2)**2)
    V = x*(x2+5)/((1+x2)**2)
    c = (1+t*U/2)/2
    Omega = (ar*(1+t*U/2)-ai*t*V/2)/2
    return ar, ai, U, V, c, Omega, atanx, log_correction


def vector_data(S, D, L):
    W = [-4*D[1]/L, 4*D[0]/L]  # W=4i S'/L.
    return W, S[0]**2+W[1]**2, -product_imag(D, S)


def serialize_complex(z):
    return {'real': z[0].strings(), 'imaginary': z[1].strings()}


def enclose(M):
    assert M == 22066, 'The retained finite theorem is specifically M=22066.'
    pi = pi_interval()
    logM = I(M).ln()
    L, t0 = 2*logM, 1/(2*logM)
    x0 = 4*pi*M*M
    hbox, middle, radius = I('0.3', '0.4'), I('0.35'), I('0.05')
    dt = I('0.000008')
    tbox = t0+I(0, dt.hi)
    xbox = x0+hbox
    assert 0 < tbox.lo and tbox.hi < Decimal('0.05')
    Lbox = (xbox/(4*pi)).ln()
    kappabox = tbox*Lbox
    assert kappabox.lo >= 1 and kappabox.hi <= 2
    cutoff_squared = xbox/(4*pi)+tbox/16
    assert cutoff_squared.lo >= M*M
    assert cutoff_squared.hi < (M+1)*(M+1)

    ar, ai, U, V, c, Omega, atanx, lc = real_data(x0, t0, pi)
    lamN, aprime = Omega-c*logM, t0*V/4
    aN = I('0.5')+t0*ar/2-t0*logM/2
    T = (x0-t0*ai)/2
    wN = (t0*logM*logM/4-(I('0.5')+t0*ar/2)*logM).exp()
    carrier = pi*(M % 2)-pi+atanx/4-x0*lc/8 \
        +t0*ai*(ar-logM)/2
    csine, ccosine = reduced_trig(carrier, pi)

    # Spatial residual controls the complete hull 0<=h<=0.4 at fixed t0.
    xhull = x0+I(0, '0.4')
    sar, sai, sU, sV, sc, sOmega, _, _ = real_data(xhull, t0, pi)
    bar, bai, bU, bV, bc, bOmega, _, _ = real_data(xbox, tbox, pi)
    centered = {name: [[I(0), I(0)], [I(0), I(0)]]
                for name in ('B', 'C')}
    midpoint_moments = [[I(0), I(0)] for _ in range(6)]
    moment6, spatial_error0, spatial_error1 = I(0), I(0), I(0)
    time_budget0, time_budget1 = I(0), I(0)
    max_spatial_residual = Decimal(0)

    for n in range(1, M+1):
        delta = (I(M)/n).ln()
        ell = logM-delta
        amp = (aN*delta+t0*delta*delta/4).exp()
        w0 = wN*amp
        sine, cosine = reduced_trig(-T*delta, pi)
        q = [amp*cosine, amp*sine]
        name = 'B' if n > M//2 else 'C'
        centered[name][0] = add(centered[name][0], q)
        centered[name][1] = add(centered[name][1],
                                [delta*q[0], delta*q[1]])

        # These are exact moments of the frozen-frequency model at h=.35.
        msine, mcosine = reduced_trig(-T*delta-middle*delta/2, pi)
        mq = [amp*mcosine, amp*msine]
        power = I(1)
        for k in range(6):
            midpoint_moments[k] = add(midpoint_moments[k],
                                      [power*mq[0], power*mq[1]])
            power *= delta/2
        moment6 += w0*power

        # Full physical gamma=-tV ell/4-i(Omega-c ell).
        # r=gamma+i delta/2, with its drift retained, controls exp(int r).
        residual_imag = sOmega-sc*logM+(sc-I('0.5'))*delta
        residual = I(absmax(t0*sV*ell/4))+I(absmax(residual_imag))
        max_spatial_residual = max(max_spatial_residual, residual.hi)
        growth = (I('0.4')*residual).exp()
        exp_error = I(0, UP.subtract(growth.hi, Decimal(1)))
        spatial_error0 += w0*exp_error
        spatial_error1 += w0*((delta/2)*exp_error+residual*growth)

        # Fixed-x physical time derivative q_t=chi*q, not a scaling-curve
        # derivative. The mixed derivative is q_xt=(gamma_t+gamma*chi)*q.
        wb = (tbox*ell*ell/4-(I('0.5')+tbox*bar/2)*ell).exp()
        chi = I(absmax(ell*ell/4-bar*ell/2)) \
            +I(absmax(bai*(bar-ell)/2))
        gamma = I(absmax(tbox*bV*ell/4)) \
            +I(absmax(bOmega-bc*ell))
        gamma_t = I(absmax(bV*ell/4)) \
            +I(absmax((bU*(bar-ell)-bai*bV)/4))
        time_budget0 += wb*chi
        time_budget1 += wb*(gamma_t+gamma*chi)

    sums, derivatives, energies, currents, W = {}, {}, {}, {}, {}
    gammaN = [-aprime*logM, -lamN]
    g = [aprime, -c]
    for name, (z0, z1) in centered.items():
        sums[name] = rotate(z0, csine, ccosine, wN)
        dc = add(multiply(gammaN, z0), multiply(g, z1))
        derivatives[name] = rotate(dc, csine, ccosine, wN)
        W[name], energies[name], currents[name] = vector_data(
            sums[name], derivatives[name], L)
    S, D = add(sums['B'], sums['C']), add(derivatives['B'], derivatives['C'])
    Wfull, energy, current = vector_data(S, D, L)
    current_cross = -product_imag(derivatives['B'], sums['C']) \
        -product_imag(derivatives['C'], sums['B'])
    difference_cross = product_real(sums['B'], sums['C']) \
        +product_real(W['B'], W['C'])
    sum_cross = sums['B'][0]*sums['C'][0]-sums['B'][1]*sums['C'][1] \
        -W['B'][0]*W['C'][0]+W['B'][1]*W['C'][1]
    assert overlap(current, currents['B']+currents['C']+current_cross)
    assert overlap(energy, energies['B']+energies['C']+difference_cross+sum_cross)
    assert currents['B'].hi < 0 and currents['C'].lo > 0 and current.lo > 0
    eta0 = 5*(-I(5)/(16*t0)).exp()
    current_tolerance0 = eta0/2*(L*I(absmax(S[1]))+I(absmax(D[1])))
    current_gap0 = current-current_tolerance0
    assert current_gap0.lo > 0
    joint_tolerance0 = I.rational('17/4')*eta0*eta0
    assert energy.lo > joint_tolerance0.hi

    # G^(j)(.35)=(-i)^j * sum (delta/2)^j q_n(x0)e^{-i delta*.35/2}.
    jets = []
    for k, moment in enumerate(midpoint_moments):
        rotated = rotate(moment, csine, ccosine, wN)
        for _ in range(k % 4):
            rotated = [rotated[1], -rotated[0]]
        jets.append(rotated)
    remainder0 = (moment6*radius**6/factorial(6)).hi
    remainder1 = (moment6*radius**5/factorial(5)).hi
    total_error0 = (spatial_error0+dt*time_budget0).hi
    total_error1 = (spatial_error1+dt*time_budget1).hi

    def transported(offset):
        value, derivative = [I(0), I(0)], [I(0), I(0)]
        for k in range(6):
            factor = offset**k/factorial(k)
            value = add(value, [factor*jets[k][0], factor*jets[k][1]])
            if k < 5:
                derivative = add(derivative,
                                 [factor*jets[k+1][0], factor*jets[k+1][1]])
        return (padded(value, (I(remainder0)+I(total_error0)).hi),
                padded(derivative, (I(remainder1)+I(total_error1)).hi))

    Sbox, Dbox = transported(I('-0.05', '0.05'))
    leftS, _ = transported(I('-0.05'))
    rightS, _ = transported(I('0.05'))
    # Full complex-disk approximation and its Cauchy spatial payment.
    eta_box = 5*(-tbox*Lbox*Lbox/16-Lbox/4).exp()
    derivative_payment = Lbox*eta_box
    Qleft = 2*leftS[0]+I(eta_box.hi.copy_negate(), eta_box.hi)
    Qright = 2*rightS[0]+I(eta_box.hi.copy_negate(), eta_box.hi)
    Qprimebox = 2*Dbox[0]+I(derivative_payment.hi.copy_negate(),
                           derivative_payment.hi)
    assert Qleft.hi < 0 and Qright.lo > 0 and Qprimebox.lo > 0
    current_box = -product_imag(Dbox, Sbox)
    current_tolerance_box = eta_box/2*(Lbox*I(absmax(Sbox[1]))
                                      +I(absmax(Dbox[1])))
    current_gap_box = current_box-current_tolerance_box
    assert current_gap_box.lo > 0
    # Regression assertions match the deliberately coarse bounds in Note 3.
    assert Decimal('12.10675') < current.lo <= current.hi < Decimal('12.10677')
    assert Decimal('-0.000673643') < currents['B'].lo <= currents['B'].hi < Decimal('-0.000673642')
    assert Decimal('12.32324') < currents['C'].lo <= currents['C'].hi < Decimal('12.32325')
    assert Decimal('-0.215813') < current_cross.lo <= current_cross.hi < Decimal('-0.215811')
    assert Decimal('3.13574') < energy.lo <= energy.hi < Decimal('3.13575')
    assert current_tolerance0.hi < Decimal('0.061241')
    assert current_gap0.lo > Decimal('12.0455')
    assert Decimal('-0.337') < Qleft.lo <= Qleft.hi < Decimal('-0.246')
    assert Decimal('0.851') < Qright.lo <= Qright.hi < Decimal('0.941')
    assert Decimal('10.20') < Qprimebox.lo <= Qprimebox.hi < Decimal('13.46')
    assert Decimal('5.07') < current_box.lo <= current_box.hi < Decimal('11.10')
    assert current_gap_box.lo > Decimal('4.92')
    assert spatial_error0.hi < Decimal('1.3e-9')
    assert spatial_error1.hi < Decimal('4.5e-9')
    assert time_budget0.hi < 2203 and time_budget1.hi < 2195
    assert remainder0 < Decimal('9.39e-7') and remainder1 < Decimal('0.000113')
    assert eta_box.hi < Decimal('0.009642')
    assert derivative_payment.hi < Decimal('0.193')

    return {
        'status': 'PASS',
        'scope': 'finite complete-cutoff theorem: one unique simple genuine H_t zero per time in a positive-area rectangle; no collision there; no sectorwide sign theorem',
        'M': M, 'N': M, 'number_of_terms': M,
        'decimal_precision': PRECISION, 'pi_atan_terms': 100, 'trig_terms': 30,
        'integer_powers': 'local override: repeated outward multiplication; no Context.power',
        'center': {
            'time': t0.strings(), 'height': x0.strings(), 'L': L.strings(),
            'eta_upper_enclosure': eta0.strings(),
            'block_S': serialize_complex(sums['B']),
            'block_Sprime': serialize_complex(derivatives['B']),
            'complement_S': serialize_complex(sums['C']),
            'complement_Sprime': serialize_complex(derivatives['C']),
            'complete_S': serialize_complex(S),
            'complete_Sprime': serialize_complex(D),
            'block_current': currents['B'].strings(),
            'complement_current': currents['C'].strings(),
            'cross_current': current_cross.strings(),
            'complete_current': current.strings(),
            'current_collision_tolerance': current_tolerance0.strings(),
            'paid_current_gap': current_gap0.strings(),
            'block_real_pair_energy': energies['B'].strings(),
            'complement_real_pair_energy': energies['C'].strings(),
            'cross_difference_phase_energy': difference_cross.strings(),
            'cross_sum_phase_energy': sum_cross.strings(),
            'complete_real_pair_energy': energy.strings(),
            'joint_collision_tolerance': joint_tolerance0.strings(),
            'current_and_energy_recombination_overlap': True,
        },
        'rectangle': {
            'height_offset': hbox.strings(), 'time_increment': ['0', str(dt.hi)],
            'time': tbox.strings(), 'height': xbox.strings(),
            'kappa': kappabox.strings(), 'L': Lbox.strings(),
            'natural_cutoff_squared': cutoff_squared.strings(),
            'midpoint_offset': middle.strings(), 'Taylor_radius': radius.strings(),
            'frozen_midpoint_jets': [serialize_complex(j) for j in jets],
            'sixth_absolute_frequency_moment': moment6.strings(),
            'value_Taylor_remainder_upper': str(remainder0),
            'derivative_Taylor_remainder_upper': str(remainder1),
            'physical_spatial_residual_upper': str(max_spatial_residual),
            'spatial_value_transport_error_upper': str(spatial_error0.hi),
            'spatial_derivative_transport_error_upper': str(spatial_error1.hi),
            'physical_time_value_budget_upper': str(time_budget0.hi),
            'physical_time_derivative_budget_upper': str(time_budget1.hi),
            'total_value_transport_error_upper': str(total_error0),
            'total_derivative_transport_error_upper': str(total_error1),
            'complete_S_enclosure': serialize_complex(Sbox),
            'complete_Sprime_enclosure': serialize_complex(Dbox),
            'eta_upper_enclosure': eta_box.strings(),
            'Cauchy_derivative_payment': derivative_payment.strings(),
            'Q_left_endpoint_enclosure_for_all_times': Qleft.strings(),
            'Q_right_endpoint_enclosure_for_all_times': Qright.strings(),
            'Qprime_enclosure_for_entire_rectangle': Qprimebox.strings(),
            'complete_current_enclosure': current_box.strings(),
            'current_collision_tolerance': current_tolerance_box.strings(),
            'paid_current_gap': current_gap_box.strings(),
            'endpoint_signs_and_monotonicity': True,
            'one_unique_simple_H_zero_per_time': True,
            'joint_H_Hprime_nonvanishing': True,
        },
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'imported_interval_source_sha256': EXPECTED_INTERVAL_SHA256,
        'imported_source_hash_checked_before_import': True,
        'python_version': platform.python_version(),
        'sources': ['https://docs.python.org/3/library/decimal.html'],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--M', type=int, default=22066)
    args = parser.parse_args()
    print(json.dumps(enclose(args.M), indent=2))
