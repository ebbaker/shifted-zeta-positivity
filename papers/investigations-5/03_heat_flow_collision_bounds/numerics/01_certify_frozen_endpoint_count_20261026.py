#!/usr/bin/env python3
"""Fixed m=16 HCB endpoint/count pilot. Requires python-flint==0.9.0.

The protocol in notes/05_ENDPOINT_COUNT_PILOT_PROTOCOL_20261026.md is fixed
before execution. All field evaluations use the exact xi initial field.
Uniform positive-time endpoint claims are conditional on RH and the
real-zero-product/Gaussian theorem in the associated research note.
No F_N asymptotic constants or zero database are inputs.
"""
import argparse
import hashlib
import json
import platform
import signal
import time
from pathlib import Path

import flint
from flint import acb, acb_series, arb, ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec = 192
    L = arb(16)
    pi = arb.pi()
    X = 4*pi*L.exp()
    tau = 1/X.sqrt().sqrt()
    logpi = pi.log()
    logX = X.log()
    calls = 0
    stage = 'setup'
    record = {
        'date': '2026-10-26', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
        'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'thread_id': '01a17aca-de9a-7533-9bb8-8ee0e9bdb282',
        'turn_id': '01a17af6-9d42-7491-a5ce-b8709a6756e2',
        'environment': {'python': platform.python_version(),
                        'python_flint': flint.__version__, 'precision_bits': ctx.prec},
        'source': 'H(0,z)=xi((1+i*z)/2)/8; exact gamma and zeta factors',
        'normalization': 'A_X=pi^(1/4)*X^(7/4)*exp(-pi*X/8)/16',
        'fixed_case': {'m': 16, 'X': X.str(50), 'tau_X': tau.str(50),
                       'wall': '[-4,4]+i[-2,2] in u=16(z-X)'},
        'assumptions': ['RH for all-real canonical roots and positive-time endpoint transport'],
        'scope': 'One finite method comparison. No uniform-in-m, F_N, Poisson-excess or new RH conclusion.',
        'source_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol': 'notes/05_ENDPOINT_COUNT_PILOT_PROTOCOL_20261026.md',
        'limits': {'total_seconds': 180, 'integral_abs_tol': '1e-8',
                   'integral_rel_tol': '1e-8', 'eval_limit_per_edge': 4096,
                   'depth_limit': 12, 'deg_limit': 128},
        'checks': [], 'endpoints': {}, 'corners': {}, 'integrals': []
    }

    def check(name, condition):
        result = bool(condition)
        record['checks'].append({'name': name, 'passed': result})
        if not result:
            raise ArithmeticError(name)

    def ball(z):
        return {'real': z.real.str(50), 'imag': z.imag.str(50)}

    def core(u, order=2, with_value=False):
        nonlocal calls
        calls += 1
        z = X + u/L
        s = (1+acb(0, 1)*z)/2
        zs = acb_series([s, 1], order).zeta()
        B = 1/s+1/(s-1)-logpi/2+(s/2).digamma()/2+zs[1]/zs[0]
        D = acb(0, 1)*B/(2*L)
        result = {'D': D}
        if order >= 3:
            B2 = -1/s**2-1/(s-1)**2+(s/2).polygamma(1)/4
            B2 += 2*zs[2]/zs[0]-(zs[1]/zs[0])**2
            result['Q'] = B2/(4*L**2)
        if with_value:
            exponent = (s/2).lgamma()-s*logpi/2-logpi/4-7*logX/4+pi*X/8
            result['F'] = s*(s-1)*exponent.exp()*zs[0]
        return result

    def checkpoint():
        record['running_stage'] = stage
        record['seconds'] = time.monotonic()-started
        if args.output:
            args.output.write_text(json.dumps(record, indent=2)+'\n')

    def timeout(_signum, _frame):
        raise TimeoutError('180-second protocol cap')

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(180)
    try:
        check('pinned library version', flint.__version__ == '0.9.0')
        stage = 'real endpoint and uniform-time comparator'
        endpoint_floors = []
        for c in [-4, 4]:
            data = core(acb(c), 3, True)
            F, D, Q = data['F'], data['D'], data['Q']
            record['endpoints'][str(c)] = {'F': ball(F), 'A': ball(D), 'Q': ball(Q)}
            check('finite real endpoint '+str(c), all(z.is_finite() for z in [F, D, Q]))
            check('endpoint reality '+str(c), 0 in F.imag and 0 in D.imag and 0 in Q.imag)
            lower = F.real.abs_lower()
            check('initial endpoint nonzero '+str(c), lower > 0)
            Amax = D.real.abs_upper()
            Qmax = Q.real.abs_upper()
            check('Gaussian moment exists '+str(c), 2*tau*Qmax < 1)
            error = 1-(-tau*Amax**2).exp()+(1-2*tau*Qmax).rsqrt()-1
            check('uniform endpoint error below one half '+str(c), error < arb(1)/2)
            error_max = error.abs_upper()
            floor = (lower*(1-error_max)).lower()
            check('positive uniform endpoint lower bound '+str(c), floor > 0)
            record['endpoints'][str(c)].update({
                'A_abs_upper': Amax.str(50), 'Q_upper': Qmax.str(50),
                'relative_error_upper_ball': error.str(50),
                'relative_error_upper': error_max.str(50),
                'initial_abs_lower': lower.str(50),
                'uniform_abs_lower_ball': floor.str(50)})
            endpoint_floors.append(floor)
            checkpoint()
        stage = 'off-axis corner gateway'
        corner_D = {}
        gateway = True
        for c in [-4, 4]:
            data = core(acb(c, 2), 2, True)
            D = data['D']
            check('finite corner data '+str(c), D.is_finite() and data['F'].is_finite())
            P = -D.imag
            passed = bool(P <= arb(3)/8)
            gateway = gateway and passed
            corner_D[c] = D
            record['corners'][str(c)] = {'F': ball(data['F']), 'D': ball(D),
                                        'P': P.str(50), 'P_le_3_over_8': passed}
        record['gateway_passed'] = gateway
        checkpoint()
        stage = 'continuous contour count'
        corners = [acb(-4, -2), acb(4, -2), acb(4, 2), acb(-4, 2)]
        integrals = []
        for index in range(4):
            start, end = corners[index], corners[(index+1) % 4]
            delta = end-start
            before = time.monotonic()
            def integrand(v, analytic):
                # D is meromorphic; division returns nonfinite on a ball
                # which cannot exclude a denominator zero. Gamma and zeta
                # arguments stay in the positive-real-part, high-imaginary
                # region, away from their poles and lgamma branch cuts.
                return core(start+delta*v)['D']*delta
            value = acb.integral(integrand, 0, 1,
                                 abs_tol=arb('1e-8'), rel_tol=arb('1e-8'),
                                 eval_limit=4096, depth_limit=12, deg_limit=128)
            record['integrals'].append({'edge': index, 'value': ball(value),
                                        'seconds': time.monotonic()-before})
            check('finite continuous edge integral '+str(index), value.is_finite())
            check('edge integral radius below tolerance '+str(index),
                  value.real.rad() < arb('1e-8') and value.imag.rad() < arb('1e-8'))
            integrals.append(value)
            checkpoint()
        count = sum(integrals, acb(0))/acb(0, 2*pi)
        record['contour_count_ball'] = ball(count)
        integer = count.real.unique_fmpz()
        check('count ball isolates integer', integer is not None)
        check('count imaginary part contains zero', 0 in count.imag)
        check('count real radius below one quarter', count.real.rad() < arb(1)/4)
        record['count'] = int(integer)
        stage = 'fourth-order filter comparator'
        upper_ascending = -integrals[2]
        C2 = (-upper_ascending.imag + 2*(corner_D[4]-corner_D[-4]).real)/pi
        record['C2'] = C2.str(50)
        leakage = arb(2)/3-arb(3).sqrt()/(2*pi)
        record['C2_leakage_allowance'] = leakage.str(50)
        if gateway:
            check('C2 arithmetic radius below 1e-4', C2.rad() < arb('1e-4'))
            enlarged = C2+arb(0, leakage.abs_upper())
            record['C2_enlarged_count_ball'] = enlarged.str(50)
            filtered_integer = enlarged.unique_fmpz()
            check('C2 isolates same integer', filtered_integer is not None and int(filtered_integer) == int(integer))
            record['C2_count'] = int(filtered_integer)
        else:
            record['C2_status'] = 'diagnostic only; fixed corner gateway failed'
        check('total execution within protocol cap', time.monotonic()-started < 180)
        record['status'] = 'certified_finite_case_under_RH'
        record['uniform_time_count'] = int(integer)
        record['uniform_endpoint_floor'] = min(endpoint_floors).str(50)
    except Exception as exc:
        record['status'] = 'stopped'
        record['failed_stage'] = stage
        record['error'] = type(exc).__name__+': '+str(exc)
    finally:
        signal.alarm(0)
        record['evaluation_calls'] = calls
        record['seconds'] = time.monotonic()-started
        encoded = json.dumps(record, indent=2)+'\n'
        if args.output:
            args.output.write_text(encoded)
        print(encoded)
    return 0 if record['status'] == 'certified_finite_case_under_RH' else 1


if __name__ == '__main__':
    raise SystemExit(main())
