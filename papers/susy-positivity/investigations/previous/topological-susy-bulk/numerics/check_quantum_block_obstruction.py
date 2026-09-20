"""Independent covariance audit and finite-block moment obstructions.

Standard-library Fraction calculations certify polynomial identities and signs.
NumPy normal-mode checks are diagnostics, not interval bounds. No zero data or
square root of the Weil operator is used. Historical inputs are read only.
Run from the investigation root with --output /tmp/quantum-block-check.json.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def scale(p, x):
    return trim([x * a for a in p])


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                if y:
                    r[i+j] += x*y
    return trim(r)


def evaluate(p, x):
    value = F(0)
    for a in reversed(p):
        value = value*x + a
    return value


def shift_one(p):
    return trim([sum(p[j]*comb(j, i) for j in range(i, len(p)))
                 for i in range(len(p))])


def determinant(matrix):
    """Leibniz determinant of small polynomial matrices, independent of old code."""
    n = len(matrix)
    result = [F(0)]
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i+1, n))
        term = [F(sign)]
        for i in range(n):
            term = mul(term, matrix[i][perm[i]])
        result = add(result, term)
    return result


def gamma_coefficients(max_j):
    """Expand x*j(x) = exp(-x/2)/((1-exp(-2*x))/x), then integrate cos.

    This does not use the historical Bernoulli-polynomial implementation.
    b_j = 2*(-1)**(j+1)*(2*j-1)! * [x**(2*j)](x*j(x)).
    """
    denominator = [F((-1)**k * 2**(k+1), factorial(k+1))
                   for k in range(2*max_j+1)]
    quotient = []
    for n in range(2*max_j+1):
        numerator = F(-1, 2)**n / factorial(n)
        quotient.append((numerator - sum(denominator[k]*quotient[n-k]
                                         for k in range(1, n+1))) / 2)
    return [None] + [2*(-1)**(j+1)*factorial(2*j-1)*quotient[2*j]
                     for j in range(1, max_j+1)]


B = gamma_coefficients(60)


def original_moment(n, j):
    return sum(2*F(4*k+1, 2)**(2*j-1) for k in range(n))


def target_polynomials(n, count):
    result = [[original_moment(n, 0)]]
    for j in range(1, count+1):
        correction = (-1)**(j+1)*B[j]
        result.append([-correction] + [F(0)]*(j-1)
                      + [original_moment(n, j)+correction])
    return result


def hankel_det(t, size, shift):
    return determinant([[t[i+j+shift] for j in range(size)]
                        for i in range(size)])


def replay_historical():
    historical = ROOT/'numerics/records/quantum-covariance-diagnostics.json'
    before = historical.read_bytes()
    with tempfile.TemporaryDirectory(prefix='quantum-block-replay-') as folder:
        output = Path(folder)/'replay.json'
        run = subprocess.run([sys.executable, str(ROOT/'numerics/check_quantum_covariance.py'),
                              '--output', str(output)], capture_output=True, text=True)
        require(run.returncode == 0, run.stdout + run.stderr)
        old, new = json.loads(before), json.loads(output.read_text())
    require(historical.read_bytes() == before, 'Historical record changed')
    # Exact scientific values in this environment; metadata may differ elsewhere.
    for key in ['exact_algebra', 'high_frequency']:
        require(old[key] == new[key], f'Historical {key} replay differs')
    for key in ['cases', 'status']:
        require(old['normal_mode_covariance'][key] == new['normal_mode_covariance'][key],
                'Historical covariance replay structure differs')
    for key in ['largest_relative_covariance_error', 'largest_uncertainty_product_error']:
        require(new['normal_mode_covariance'][key] < 1e-12, 'Covariance replay failed')
    return old, dict(status='passed', entire_json_equal=old == new,
                     historical_record_sha256=hashlib.sha256(before).hexdigest(),
                     exact_algebra_and_decimal_rows_equal=True,
                     normal_mode_diagnostics=new['normal_mode_covariance'])


def independent_pair_audit(old):
    exact = old['exact_algebra']
    require([str(x) for x in B[1:6]] == exact['gamma_inverse_power_coefficients'],
            'Independent kernel expansion disagrees with gamma coefficients')
    t = target_polynomials(2, 5)
    c0 = t[0][0]
    mu = scale(t[1], 1/c0)
    beta2 = scale(hankel_det(t, 2, 0), 1/c0**2)
    delta = scale(hankel_det(t, 2, 1), 1/c0**2)
    # Gram determinants give d8 without expanding the old two-field formula.
    d8_num = scale(hankel_det(t, 3, 0), -1/c0**2)
    h1 = hankel_det(t, 3, 1)
    comparisons = [
        (mu, exact['mu_q_coefficients']),
        (beta2, exact['beta_squared_q_coefficients']),
        (shift_one(delta), exact['determinant_numerator_coefficients_in_q_minus_one']),
        (shift_one(d8_num), ['0'] + [str(-F(x, exact['denominator']))
                                    for x in exact['P5_ascending_integer_coefficients']]),
        (shift_one(h1), ['0'] + [str(-F(x, exact['hankel_denominator']))
                                for x in exact['P8_ascending_integer_coefficients']]),
    ]
    for actual, expected in comparisons:
        require(actual == [F(x) for x in expected], 'Independent polynomial audit failed')
    rows = []
    for q in map(F, [1, 2, 10, 1000000]):
        v = [evaluate(p, q) for p in t]
        m = v[1]/c0
        b2 = v[2]/c0-m*m
        nu = (v[3]/c0-m**3-2*m*b2)/b2
        d = m*nu-b2
        m4 = c0*((m*m+b2)**2+b2*(m+nu)**2)
        d8 = m4-v[4]
        chi2 = -d8/(c0*b2)
        eta = q+chi2*m/d
        # Similar to symmetric M3 via diag(1,beta,beta*chi).
        monic = [[m, b2, F(0)], [F(1), nu, chi2], [F(0), F(1), eta]]
        vec = [F(1), F(0), F(0)]
        realized = [c0]
        for _ in range(5):
            vec = [sum(monic[i][j]*vec[j] for j in range(3)) for i in range(3)]
            realized.append(c0*vec[0])
        require(realized[:5] == v[:5], 'Three-field moments differ')
        d10 = v[5]-realized[5]
        formula = evaluate(h1, q)/(c0**2*evaluate(delta, q))+q*d8
        require(d10 == formula, 'Independent fifth-moment residual sign differs')
        require(d > 0 and eta-chi2*m/d == q, 'Positive Schur complement failed')
        require(q == 1 or (d8 < 0 and d10 < 0), 'Residual sign failed')
        rows.append(dict(q=str(q), d8=str(d8), d10=str(d10)))
    return dict(status='passed', method='Kernel Taylor division and independent Gram determinants',
                polynomial_certificates_match=True, exact_three_field_rows=rows)


def annihilator_witness(n, t):
    # p_q(x)=q**n*p_1(x/q); roots q*a_k**2 kill the original atoms.
    p = [F(1)]
    for k in range(n):
        p = mul(p, [-F(4*k+1, 2)**2, F(1)])
    actual, negative_sum = [F(0)], [F(0)]
    for i, vi in enumerate(p):
        for j, vj in enumerate(p):
            k = i+j+1
            actual = add(actual, [F(0)]*(2*n-i-j) + scale(t[k], vi*vj))
            coefficient = abs(vi*vj)*(-B[k])
            term = [F(0)]*(2*n+2)
            term[2*n+1-k] += coefficient
            term[2*n+1] -= coefficient
            negative_sum = add(negative_sum, term)
    require(trim(actual) == trim(negative_sum), 'Annihilator identity failed')
    shifted = shift_one(actual)
    require(shifted[0] == 0 and all(x < 0 for x in shifted[1:]),
            'Annihilator negative coefficient certificate failed')
    return dict(p_at_q_one_ascending=[str(x) for x in p],
                negative_quadratic_form_coefficients_in_q_minus_one=[str(x) for x in shifted])


def block_certificates(n):
    t = target_polynomials(n, 2*n+1)
    rows = []
    for shift in [0, 1]:
        for size in range(1, n+2):
            coefficients = shift_one(hankel_det(t, size, shift))
            if size == n+1:
                require(coefficients[0] == 0, 'No-loop block did not lose rank')
                wanted = 1 if shift == 0 else -1
                require(all(wanted*x > 0 for x in coefficients[1:]), 'Block sign failed')
            else:
                require(all(x > 0 for x in coefficients), 'Lower principal minor failed')
            rows.append(dict(shift=shift, size=size,
                             coefficients_in_q_minus_one=[str(x) for x in coefficients]))
    return dict(replaced_channels=n, feasible_matching_moments=2*n,
                impossible_matching_moments=2*n+1,
                target_moments_q_coefficients=[[str(x) for x in p] for p in t],
                leading_principal_minor_certificates=rows,
                annihilator=annihilator_witness(n, t))


def dot_polynomials(p, q, moments, shift=0):
    return sum(x*y*moments[i+j+shift] for i, x in enumerate(p)
               for j, y in enumerate(q))


def jacobi_data(n, q):
    # Work with mass/q to avoid enormous powers in the arithmetic phase range.
    t = [evaluate(p, q)/q**j for j, p in enumerate(target_polynomials(n, 2*n+1))]
    polynomials, norms = [], []
    for k in range(n+1):
        p = [F(0)]*k+[F(1)]
        for earlier, norm in zip(polynomials, norms):
            p = add(p, scale(earlier, -dot_polynomials(p, earlier, t)/norm))
        polynomials.append(p)
        norms.append(dot_polynomials(p, p, t))
    require(all(x > 0 for x in norms), 'Gram-Schmidt norm failed')
    alpha = [dot_polynomials(p, p, t, 1)/norms[k]
             for k, p in enumerate(polynomials[:-1])]
    beta2 = [norms[k]/norms[k-1] for k in range(1, n+1)]
    # Bottom-right entry of inverse upper Jacobi block: continued LDL elimination.
    pivot = alpha[0]
    for k in range(1, n):
        pivot = alpha[k]-beta2[k-1]/pivot
        require(pivot > 0, 'Upper Jacobi block not positive')
    alpha.append(1+beta2[-1]/pivot)  # Schur complement = 1 (unscaled = q).
    monic = [[F(0)]*(n+1) for _ in range(n+1)]
    for k in range(n+1):
        monic[k][k] = alpha[k]
        if k < n:
            monic[k][k+1] = beta2[k]
            monic[k+1][k] = F(1)
    vec = [F(1)]+[F(0)]*n
    realized = [t[0]]
    for _ in range(2*n+1):
        vec = [sum(monic[i][j]*vec[j] for j in range(n+1)) for i in range(n+1)]
        realized.append(t[0]*vec[0])
    require(realized[:2*n+1] == t[:2*n+1], 'Jacobi moment matching failed')
    require(t[-1]-realized[-1] < 0, 'First surviving odd residual not negative')
    return t, alpha, beta2, realized


def construction_controls():
    rows, largest_error = [], 0.0
    for n in [3, 4]:
        for q in map(F, [2, 10, 1000000]):
            t, alpha, beta2, realized = jacobi_data(n, q)
            mass = np.diag(list(map(float, alpha)))
            off = np.sqrt(list(map(float, beta2)))
            mass += np.diag(off, 1)+np.diag(off, -1)
            c0 = float(t[0])
            minimum = float(np.linalg.eigvalsh(mass)[0])
            require(minimum > 0, 'Sampled Jacobi mass not positive')
            for s in [.01, 1., 100.]:
                h = s*np.eye(n+1)+mass
                frequencies, rotation = np.linalg.eigh(h)
                vacuum = (rotation*(1/(2*frequencies)))@rotation.T
                quantum = 2*c0*s*vacuum[0, 0]
                # Schur complement and an independent minimization of the classical energy.
                e = np.eye(n+1)[:, 0]
                u = np.linalg.solve(np.eye(n+1)+s*np.linalg.inv(mass), e)
                classical = c0*((e-u)@(e-u)+s*u@np.linalg.solve(mass, u))
                # Entire rational covariance by the Jacobi continued fraction.
                denominator = s+float(alpha[-1])
                for k in reversed(range(n)):
                    denominator = s+float(alpha[k])-float(beta2[k])/denominator
                response = c0*s/denominator
                error = max(abs(quantum-response), abs(classical-response))/max(1., abs(response))
                largest_error = max(largest_error, error)
            rows.append(dict(replaced_channels=n, fields=n+1, q=str(q),
                             alpha_scaled=[str(x) for x in alpha],
                             beta_squared_scaled=[str(x) for x in beta2],
                             leading_inverse_power=4*n+2,
                             leading_residual_divided_by_q_power=str(t[-1]-realized[-1]),
                             smallest_sampled_mass_eigenvalue_divided_by_q=minimum))
    require(largest_error < 1e-11, 'Quantum/classical/continued-fraction response mismatch')
    return dict(status='passed', exact_rational_rows=rows,
                largest_floating_response_error=largest_error,
                scope='Exact finite moment arithmetic; sampled covariance controls are not enclosures.')


def diagonal_obstruction_certificates():
    rows = []
    for n in [1, 2, 3, 4]:
        j = next(j for j in range(1, len(B), 2)
                 if -B[j]*(1-F(2)**(-j)) > original_moment(n, j))
        margin = -B[j]*(1-F(2)**(-j))-original_moment(n, j)
        require(margin > 0, 'Uniform odd-moment obstruction failed')
        rows.append(dict(replaced_channels=n, odd_moment=j, q_lower_bound='2',
                         positive_margin=str(margin),
                         first_such_odd_moment_in_exact_search=True))
    return dict(status='passed', rows=rows,
                meaning='For q>=2, t_j/q**j <= -margin < 0. These conservative orders support the diagonal-jump theorem; they are not optimal cancellation counts.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    old, replay = replay_historical()
    report = dict(status='passed', date='2026-09-13',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python=platform.python_version(), numpy=np.__version__,
                  historical_replay=replay, independent_pair_audit=independent_pair_audit(old),
                  larger_blocks=[block_certificates(n) for n in [1, 2, 3, 4]],
                  larger_block_constructions=construction_controls(),
                  diagonal_obstruction=diagonal_obstruction_certificates(),
                  gamma_coefficients_from_kernel=[str(x) for x in B[1:]],
                  scope='Exact finite certificates and Gaussian controls. General finite-block and interval obstructions are proved in the accompanying note. No full Weil positivity or operator-norm estimate.')
    encoded = json.dumps(report, indent=2)+'\n'
    if args.output:
        output = args.output.resolve()
        require(output != (ROOT/'numerics/records/quantum-covariance-diagnostics.json').resolve(),
                'Refusing to overwrite historical quantum record')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded)
        print(json.dumps(dict(status='passed', output=str(output),
                              exact_blocks=[1, 2, 3, 4],
                              larger_block_cancellation_counts=[6, 8],
                              larger_block_first_surviving_inverse_powers=[14, 18],
                              uniform_diagonal_obstruction_moments=[r['odd_moment'] for r in report['diagonal_obstruction']['rows']]), indent=2))
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
