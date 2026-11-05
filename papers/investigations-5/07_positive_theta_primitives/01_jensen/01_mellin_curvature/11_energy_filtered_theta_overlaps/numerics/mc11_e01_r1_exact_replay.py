#!/usr/bin/env python3
"""MC11-E01 r1: fixed saved-data replay; no quadrature or E02 calculation.

Prepared for Edward Baker, 2026-11-04, with substantial LLM assistance.
Actual recorded model gpt-6.1-sol, reasoning effort ultra.
"""
import argparse
import hashlib
import itertools
import json
import platform
import time
from fractions import Fraction as F
from pathlib import Path

PARENT = Path('papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature')
RGD = PARENT / '10_radial_green_determinants'
FROZEN = {
    str(PARENT / '08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md'): '96ffcc2943608870d5b8426fd217ce5ad515a05f06ff73f97c1d1295b71eec5a',
    str(RGD / 'manuscript/sections/01_green.tex'): '0822d1d731da513ff62c6c7fa4ec8dfcd794c7212847dc2e39256efcfc015a60',
    str(RGD / 'brainstorm/notes/02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md'): '7b1cfcf6bdc9edd3e09b8143e70491c795f8d1cf011a7acec104f8a416824a10',
    str(RGD / 'brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md'): '6a54482efcf3e586df878b097a450bb2584e75b5888a77c214105ec1f63ac928',
    str(RGD / 'numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json'): '9ddc5881df258c3dbdfe611bf0c620c74cbd1292e0628d0e00dbca30a4e06e9a',
}


def dyadic(pair):
    mantissa, exponent = int(pair[0]), int(pair[1])
    return F(mantissa) * F(2) ** exponent


def ball(mid, rad):
    m, r = dyadic(mid), dyadic(rad)
    assert r >= 0
    return m-r, m+r


def subtract(a, b):
    return a[0]-b[1], a[1]-b[0]


def ceil_grid384(x):
    n = x * 2**384
    return F(-(-n.numerator // n.denominator), 2**384)


def determinant_polynomial(indices):
    """Collect exact monomials in c1,...,c5 by permutation expansion."""
    n = len(indices)
    out = {}
    for p in itertools.permutations(range(n)):
        parity = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        powers = [0]*5
        for i, j in enumerate(p):
            powers[indices[i][j]-1] += 1
        key = tuple(powers)
        out[key] = out.get(key, 0) + (-1)**parity
    return {k: v for k, v in out.items() if v}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an existing replay record')
    start = time.perf_counter()
    checks = []

    def check(name, condition):
        checks.append({'check': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    for path, expected in FROZEN.items():
        check('frozen input SHA-256: ' + path,
              hashlib.sha256((args.repo/path).read_bytes()).hexdigest() == expected)

    record_path = RGD / 'numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json'
    source = json.loads((args.repo/record_path).read_text())
    X = []
    for j, row in enumerate(source['compact_moment_dyadics']):
        check(f'compact input index {j}', row['j'] == j)
        X.append(ball(row['mid'], row['rad']))
        check(f'positive compact primitive moment {j}', X[-1][0] > 0)
    check('six saved primitive moments only', len(X) == 6)
    C = [subtract((F(1,16), F(1,16)), X[0])]
    C.extend(subtract(X[j-1], X[j]) for j in range(1,6))
    for j, row in enumerate(source['reference_boxes']):
        check(f'reconstruct reference box {j}', C[j] == (F(row['lower']),F(row['upper'])))
        check(f'positive reference coefficient {j}', C[j][0] > 0)
    check('C0 upper strictly below 1/16', C[0][1] < F(1,16))
    check('C1 lower strictly above 1/3000', C[1][0] > F(1,3000))

    eps = F(1,40000)
    T = []
    for j, row in enumerate(source['tail_allowances']):
        check(f'tail input index {j}', row['j'] == j)
        E = ball(row['E_mid'], row['E_rad'])
        B = ball(row['B_mid'], row['B_rad'])
        check(f'positive saved energy/spatial tails {j}', E[0] > 0 and B[0] > 0)
        t = ceil_grid384(E[1]+B[1])
        check(f'outward tail sum including nonzero spatial tail {j}', t >= E[1]+B[1])
        check(f'saved tail grid equality {j}', t == F(row['upper_grid384']))
        T.append(t)
    entry = []
    for j in range(1,6):
        allowance = (T[j-1]+T[j])/C[j][0]
        check(f'recompute recorded entry allowance {j}',
              allowance == F(source['entry_relative_upper_bounds'][j]['exact']))
        check(f'whole-path and h{j} allowance strictly below epsilon', allowance < eps)
        entry.append({'j': j, 'exact_upper': str(allowance)})

    boxes = {2: (F('.465'),F('.466')), 3: (F('.135'),F('.137')),
             4: (F('.028'),F('.029')), 5: (F('.004'),F('.005'))}
    for j, row in zip(range(2,6), source['normalized_ratios']):
        lo = C[0][0]**(j-1)*C[j][0]/C[1][1]**j
        hi = C[0][1]**(j-1)*C[j][1]/C[1][0]**j
        check(f'recompute normalized t{j} interval',
              row['j'] == j and (lo,hi) == (F(row['lower']),F(row['upper'])))
        check(f'normalized t{j} in frozen rational box', boxes[j][0] <= lo <= hi <= boxes[j][1])

    slope = 4*F(25,2)-9-F(12)/(2*F(25,2)-3)
    check('logarithmic slope at X=25/2 strictly above 40', slope > 40)
    ratio_floor = (1-eps)/(1+eps)*boxes[3][0]/boxes[2][1]*F(16,3000)
    check('whole-path c3/c2 floor > 1/700', ratio_floor > F(1,700))
    check('exchange margin 1/700 > 1/800', F(1,700) > F(1,800))
    check('two slope recursions give 2a2/a1 <= 1/800', 2*F(1,40)**2 == F(1,800))
    R = boxes[3][1]/boxes[2][0]**2
    check('compact R bound < 16/25', R < F(16,25))
    reference_floor = (1-eps)**2-(1+eps)**2*R
    check('D2(0)/C2^2 floor > 7/20', reference_floor > F(7,20))
    loss_upper = 2*eps*(1+eps)*R/F(7,20)
    coarse_loss = 2*eps*(1+eps)*F(16,25)/F(7,20)
    check('strict fractional loss upper < 1/10000', loss_upper < F(1,10000))
    check('coarse fractional loss upper < 1/10000', coarse_loss < F(1,10000))

    for q in (2,3):
        indices = [[q+j-i for j in range(q)] for i in range(q)]
        ones = [(i,j) for i in range(q) for j in range(q) if indices[i][j]==1]
        check(f'only index-one entry at bottom left q={q}', ones == [(q-1,0)])
        minor = [row[1:] for row in indices[:-1]]
        poly = {k: (-1)**(q-1)*v for k,v in determinant_polynomial(minor).items()}
        expected = ({(0,0,1,0,0):-1} if q==2 else
                    {(0,0,0,2,0):1,(0,0,1,0,1):-1})
        check(f'corner cofactor sign and polynomial q={q}', poly == expected)
    corner_floor = (1-eps)**2*boxes[4][0]**2-(1+eps)**2*boxes[3][1]*boxes[5][1]
    check('three-orbital corner floor strictly positive', corner_floor > 0)

    out = {
        'task':'MC11-E01','request_revision':'r1','date':'2026-11-04',
        'timezone':'America/New_York','prepared_for':'Edward Baker','llm_assistance':True,
        'actual_model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'thread_id':'01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab',
        'turn_id':'01a1a8e5-1f78-7db1-9405-1dfc9cf9d984',
        'input_sha256':FROZEN,
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),
        'arithmetic':'standard-library Fraction and integers only; no floating input',
        'trusted_inputs':'Saved primitive integral balls and analytical constant/tail balls; acquisition not rerun',
        'integrand_evaluations':0,'new_moments':0,'local_corrections':0,
        'checks':checks,'entry_relative_upper_bounds':entry,
        'rational_consequences':{
            'epsilon':str(eps),'slope_at_25_over_2':str(slope),
            'c3_over_c2_strict_lower':str(ratio_floor),
            'R_upper':str(R),'D2_reference_scaled_strict_lower':str(reference_floor),
            'fractional_loss_strict_upper':str(loss_upper),
            'coarse_fractional_loss_strict_upper':str(coarse_loss),
            'q3_corner_scaled_lower':str(corner_floor),
            'q3_corner_scale':'(c1*)^8/(c0*)^6 > 0',
        },
        'status':'passed all fixed E01 exact-rational checks',
        'scope':'Internal assessment inheriting accepted acquisition; no E02 spectral split or finite-energy cutoff',
        'execution_seconds':time.perf_counter()-start,
    }
    with args.output.open('x') as f:
        json.dump(out,f,indent=2); f.write('\n')
    print(json.dumps({'status':out['status'],'checks':len(checks),'seconds':out['execution_seconds'],
                      'rational_consequences':out['rational_consequences']}))


if __name__ == '__main__':
    main()
