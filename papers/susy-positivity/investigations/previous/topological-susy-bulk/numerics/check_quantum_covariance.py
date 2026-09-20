"""Exact moment checks and numerical controls for a coupled vacuum covariance.

This does not test or prove positivity of the full Weil form. Fraction arithmetic
certifies the displayed polynomial identities. Floating-point and Decimal checks
are diagnostics, not interval enclosures. No zero data or target square root.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from math import comb, lcm
from functools import reduce
import argparse
import hashlib
import json
import platform
import numpy as np


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*ps):
    out = [F(0)] * max(map(len, ps))
    for p in ps:
        for i, x in enumerate(p):
            out[i] += x
    return trim(out)


def scale(p, c):
    return trim([F(c) * x for x in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x * y
    return trim(out)


def power(p, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, p)
    return out


def shift_one(p):
    """Coefficients in r=q-1: p(1+r)."""
    return trim([sum(p[j] * comb(j, i) for j in range(i, len(p)))
                 for i in range(len(p))])


def evaluate(p, x):
    out = 0
    for coefficient in reversed(p):
        out = out*x + coefficient
    return out


def bernoulli_numbers(n):
    out = [F(1)]
    for j in range(1, n+1):
        out.append(-sum(F(comb(j+1, k))*out[k] for k in range(j))/(j+1))
    return out


BERN = bernoulli_numbers(80)


def gamma_coefficient(n):
    degree = 2*n
    polynomial = sum(F(comb(degree, k))*BERN[k]*F(1, 4)**(degree-k)
                     for k in range(degree+1))
    return (-1)**(n+1)*F(2**degree, degree)*polynomial


Q = [F(0), F(1)]
MOMENTS = [sum(2*a**(2*j-1) for a in [F(1, 2), F(5, 2)]) for j in range(6)]
GAMMA = [None] + [gamma_coefficient(j) for j in range(1, 6)]
TARGET = [[MOMENTS[0]]]
for j in range(1, 6):
    TARGET.append(add(scale(power(Q, j), MOMENTS[j]),
                      scale(sub(power(Q, j), [F(1)]), (-1)**(j+1)*GAMMA[j])))

MU = scale(TARGET[1], 1/MOMENTS[0])
V2 = scale(TARGET[2], 1/MOMENTS[0])
V3 = scale(TARGET[3], 1/MOMENTS[0])
BETA2 = sub(V2, power(MU, 2))
N = sub(sub(V3, power(MU, 3)), scale(mul(MU, BETA2), 2))
DETNUM = sub(mul(MU, N), power(BETA2, 2))
M4NUM = scale(add(mul(power(V2, 2), BETA2),
                 power(add(mul(MU, BETA2), N), 2)), MOMENTS[0])
D8NUM = sub(M4NUM, mul(TARGET[4], BETA2))
H1DET = add(mul(TARGET[1], sub(mul(TARGET[3], TARGET[5]), power(TARGET[4], 2))),
            scale(mul(TARGET[2], sub(mul(TARGET[2], TARGET[5]), mul(TARGET[3], TARGET[4]))), -1),
            mul(TARGET[3], sub(mul(TARGET[2], TARGET[4]), power(TARGET[3], 2))))


def exact_checks():
    require(GAMMA[1:] == [-F(1, 24), -F(7, 960), -F(31, 8064), -F(127, 30720), -F(511, 67584)],
            'Digamma coefficients differ')
    require(add(power(MU, 2), BETA2) == V2, 'Second moment differs')
    require(add(power(MU, 3), scale(mul(MU, BETA2), 2), N) == V3,
            'Third moment differs')
    for j in range(1, 4):
        coefficient = add(scale(sub(power(Q, j), [F(1)]), GAMMA[j]),
                          scale(sub(TARGET[j], scale(power(Q, j), MOMENTS[j])), (-1)**j))
        require(coefficient == [0], f'Residual inverse power {2*j} did not cancel')
    require(all(x > 0 for x in shift_one(MU)), 'mu positivity certificate failed')
    require(all(x > 0 for x in shift_one(BETA2)), 'beta squared positivity failed')
    require(all(x > 0 for x in shift_one(DETNUM)), 'Determinant positivity failed')
    r8 = shift_one(D8NUM)
    require(r8[0] == 0 and all(x < 0 for x in r8[1:]), 'Surviving coefficient sign failed')
    require(evaluate(MU, F(1)) == F(5, 4), 'Uncoupled mu differs')
    require(evaluate(BETA2, F(1)) == F(5), 'Uncoupled beta differs')
    require(evaluate(N, F(1))/evaluate(BETA2, F(1)) == F(21, 4), 'Uncoupled nu differs')
    # Exact no-loop response equality at arbitrary s, by polynomial cross product.
    denominator = [F(25, 16), F(13, 2), F(1)]
    numerator = [F(0), F(126, 5), F(24, 5)]
    require(numerator == scale(mul([F(0), F(1)], [F(21, 4), F(1)]), MOMENTS[0]),
            'No-loop response numerator differs')
    require(denominator == mul([F(1, 4), F(1)], [F(25, 4), F(1)]),
            'No-loop response denominator differs')
    denominator8 = reduce(lcm, (x.denominator for x in r8[1:]))
    certificate = [int(-x*denominator8) for x in r8[1:]]
    hankel = shift_one(H1DET)
    require(hankel[0] == 0 and all(x < 0 for x in hankel[1:]),
            'Shifted moment matrix obstruction sign failed')
    hankel_denominator = reduce(lcm, (x.denominator for x in hankel[1:]))
    hankel_certificate = [int(-x*hankel_denominator) for x in hankel[1:]]
    return dict(
        status='passed', arithmetic='fractions.Fraction',
        gamma_inverse_power_coefficients=[str(x) for x in GAMMA[1:]],
        original_two_channel_moments=[str(x) for x in MOMENTS],
        two_field_cancelled_inverse_powers=[2, 4, 6],
        three_field_cancelled_inverse_powers=[2, 4, 6, 8],
        mu_q_coefficients=[str(x) for x in MU],
        beta_squared_q_coefficients=[str(x) for x in BETA2],
        nu_numerator_q_coefficients=[str(x) for x in N],
        beta_squared_coefficients_in_q_minus_one=[str(x) for x in shift_one(BETA2)],
        determinant_numerator_coefficients_in_q_minus_one=[str(x) for x in shift_one(DETNUM)],
        residual_inverse8='-(q-1)*P5(q-1)/(denominator*beta_squared)',
        P5_ascending_integer_coefficients=certificate, denominator=denominator8,
        shifted_hankel_determinant='-(q-1)*P8(q-1)/hankel_denominator',
        P8_ascending_integer_coefficients=hankel_certificate, hankel_denominator=hankel_denominator,
        three_field_inverse10='H1DET/(c0**2*DETNUM)+q*d8 < 0 for q>1',
        scope='Positive mass matrices for q>=1. Two fields leave inverse8; three leave inverse10. Any positive mass realization replacing only these two channels cannot match the first five moments for q>1.')


def fpoly(p, x):
    return float(evaluate([float(c) for c in p], x))


def covariance_controls():
    psi0 = -np.euler_gamma - np.pi/2 - 3*np.log(2)
    w0 = psi0-np.log(np.pi)
    theta = np.linspace(0, 2*np.pi, 129)[:-1]
    r = 2**(-.5)
    v = (w0 - 2*np.log(2)*r*np.exp(-1j*theta)/(1-r*np.exp(-1j*theta))).real
    qs = np.exp(-2*v)
    require(float(qs.min()) > 1, 'One-prime sample not in proved q regime')
    max_covariance_error = 0.
    max_uncertainty_error = 0.
    min_scaled_eigenvalue = np.inf
    count = 0
    for q in [1., 2., 10., 1000., *qs.tolist()]:
        mu, beta2 = fpoly(MU, q), fpoly(BETA2, q)
        nu = fpoly(N, q)/beta2
        matrix = np.array([[mu, np.sqrt(beta2)], [np.sqrt(beta2), nu]])
        min_scaled_eigenvalue = min(min_scaled_eigenvalue, np.linalg.eigvalsh(matrix)[0]/q)
        det = fpoly(DETNUM, q)/beta2
        d8 = fpoly(D8NUM, q)/beta2
        gamma2 = max(0., -d8/(float(MOMENTS[0])*beta2))
        eta = q+gamma2*mu/det
        matrix3 = np.array([[mu,np.sqrt(beta2),0],
                            [np.sqrt(beta2),nu,np.sqrt(gamma2)],
                            [0,np.sqrt(gamma2),eta]])
        for dimension, mass in [(2,matrix),(3,matrix3)]:
            min_scaled_eigenvalue = min(min_scaled_eigenvalue,np.linalg.eigvalsh(mass)[0]/q)
            for ratio in [.001, .1, 1., 10., 1000.]:
                s = q*ratio
                h = mass+s*np.eye(dimension)
                frequencies, rotation = np.linalg.eigh(h)
                coordinate_covariance = (rotation*(1/(2*frequencies)))@rotation.T
                momentum_covariance = h/2
                direct = 2*float(MOMENTS[0])*s*coordinate_covariance[0, 0]
                if dimension == 2:
                    formula = float(MOMENTS[0])*s*(s+nu)/((s+mu)*(s+nu)-beta2)
                else:
                    tail = (s+nu)*(s+eta)-gamma2
                    formula = float(MOMENTS[0])*s*tail/((s+mu)*tail-beta2*(s+eta))
                max_covariance_error = max(max_covariance_error, abs(direct-formula)/max(1.,abs(formula)))
                max_uncertainty_error = max(max_uncertainty_error,
                                            float(np.max(abs(coordinate_covariance@momentum_covariance-.25*np.eye(dimension)))))
                count += 1
    require(max_covariance_error < 1e-12, 'Normal-mode covariance mismatch')
    require(max_uncertainty_error < 1e-12, 'Ground-state uncertainty control failed')
    require(min_scaled_eigenvalue > 0, 'Unexpected negative sampled frequency')
    return dict(status='passed', cases=count, largest_relative_covariance_error=max_covariance_error,
                largest_uncertainty_product_error=max_uncertainty_error,
                smallest_sampled_mass_eigenvalue_divided_by_q=min_scaled_eigenvalue,
                sampled_arithmetic_q_range=[float(qs.min()),float(qs.max())],
                interpretation='Floating-point checks of normal-mode quantization; positivity is proved by the exact polynomial certificate.')


def decimal_fraction(x):
    x = F(x)
    return D(x.numerator)/D(x.denominator)


def dpoly(p, x):
    return evaluate([decimal_fraction(c) for c in p], x)


def real_digamma(tau, shift=80, terms=32):
    """High precision recurrence plus asymptotics; diagnostic, not an enclosure."""
    x, y = D(shift)+D('0.25'), tau/2
    den = x*x+y*y
    invr, invi = x/den, -y/den
    step_r, step_i = invr*invr-invi*invi, 2*invr*invi
    pr, pi = step_r, step_i
    answer = den.ln()/2-invr/2
    for k in range(1, terms+1):
        answer -= decimal_fraction(BERN[2*k])*pr/D(2*k)
        pr, pi = pr*step_r-pi*step_i, pr*step_i+pi*step_r
    for j in range(shift):
        xj = D(j)+D('0.25')
        answer -= xj/(xj*xj+y*y)
    return answer


def exact_channel_change_decimal(s, q):
    mu, beta2 = dpoly(MU, q), dpoly(BETA2, q)
    nu = dpoly(N, q)/beta2
    det = dpoly(DETNUM, q)/beta2
    mu0, nu0, det0 = 5*q/4, 21*q/4, 25*q*q/16
    numerator = ((mu0-mu)*s*s+(det0-det+nu*mu0-nu0*mu)*s+(nu*det0-nu0*det))
    denominator = (s*s+(mu+nu)*s+det)*(s*s+(mu0+nu0)*s+det0)
    return decimal_fraction(MOMENTS[0])*s*numerator/denominator


def three_channel_change_decimal(s, q):
    c0 = decimal_fraction(MOMENTS[0])
    mu, beta2 = dpoly(MU,q), dpoly(BETA2,q)
    nu, det = dpoly(N,q)/beta2, dpoly(DETNUM,q)/beta2
    d8 = dpoly(D8NUM,q)/beta2
    gamma2 = -d8/(c0*beta2)
    eta = q+gamma2*mu/det
    tail = (s+nu)*(s+eta)-gamma2
    new = c0*s*tail/((s+mu)*tail-beta2*(s+eta))
    old = 4*s/(s+q/4)+D('0.8')*s/(s+25*q/4)
    return new-old


def high_frequency_controls():
    rows=[]
    with localcontext() as context:
        context.prec=80
        for q_int, carriers in [(2, [100, 1000, 10000]),
                                (10, [100, 1000, 10000]),
                                (1000000, [100000, 1000000, 10000000])]:
            q=D(q_int)
            d8=dpoly(D8NUM,q)/dpoly(BETA2,q)
            d10=dpoly(H1DET,q)/(decimal_fraction(MOMENTS[0])**2*dpoly(DETNUM,q))+q*d8
            require(d10 < 0, 'Unexpected inverse10 sign')
            previous_error={2:None,3:None}
            for tau_int in carriers:
                tau=D(tau_int); s=tau*tau
                for fields, order, coefficient, change in [(2,4,d8,exact_channel_change_decimal),
                                                           (3,5,d10,three_channel_change_decimal)]:
                    def residual(shift,terms):
                        old=real_digamma(tau/q.sqrt(),shift,terms)-real_digamma(tau,shift,terms)+q.ln()/2
                        return old+change(s,q)
                    residual1=residual(80,32)
                    residual2=residual(100,40)
                    ratio=residual2*s**order/coefficient
                    error=abs(ratio-1)
                    if previous_error[fields] is not None:
                        require(error < previous_error[fields]/50, 'Residual asymptotic convergence failed')
                    require(abs(residual1-residual2)*s**order/abs(coefficient) < D('1e-35'),
                            'Digamma diagnostic refinements disagree')
                    previous_error[fields]=error
                    rows.append(dict(q=q_int,tau=tau_int,fields=fields,leading_inverse_power=2*order,
                                     scaled_residual_divided_by_leading_coefficient=str(ratio),
                                     refinement_difference=str(abs(residual1-residual2))))
    return dict(status='passed', decimal_precision=80, rows=rows,
                interpretation='Direct digamma evaluation agrees with the derived eighth- and tenth-power tails; asymptotic truncations and rounding are not interval certified.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=dict(status='passed',date='2026-09-13',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                python=platform.python_version(),numpy=np.__version__,
                exact_algebra=exact_checks(),normal_mode_covariance=covariance_controls(),
                high_frequency=high_frequency_controls(),
                scope='Coupled Gaussian covariance models, q>=1. Two fields cancel three coefficients; three fields cancel four. A shifted moment determinant excludes cancellation of the first five in this positive mass class with only the first two original channels replaced. No full Weil positivity or RH claim.')
    encoded=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(encoded)
        print(json.dumps(dict(status='passed',output=str(args.output),
                              two_field_cancellations=[2,4,6],three_field_cancellations=[2,4,6,8],
                              surviving_inverse_powers=[8,10],fifth_moment_obstruction=True),indent=2))
    else:
        print(encoded,end='')


if __name__=='__main__':
    main()
