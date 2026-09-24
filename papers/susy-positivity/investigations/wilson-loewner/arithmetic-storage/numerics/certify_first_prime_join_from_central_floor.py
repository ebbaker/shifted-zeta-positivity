#!/usr/bin/env python3
"""The first-prime append (L, h, omega) = (11/20, 1/5, 1/1000) from a central floor.

Reduction (see notes/FIRST_PRIME_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md):
  Lemma A  kappa_0 <= kappa  <=>  [[kappa Q_L, -H*], [-H, kappa Q_h]] >= 0;
           in particular kappa_0 <= 1 <=> Q_{0,R} >= 0 on the joined window.
  Lemma B  Q_{0,R} >= m I and ||H_0|| <= beta  ==>  kappa_0 <= beta/(beta + m).
  Lemma C  Q_{s,R} >= 0 for 0 <= s <= omega  ==>  ||V_{omega,R}|| <= 1 (defect identity);
           weil-depth's continuation inequality gives the decay form used below.
This program
  1. rebuilds, with the unchanged weil-depth Arb builder, the N = 128 Legendre
     model at horizon R = 3/4 and replays its full Schur test at the floor m;
  2. encloses beta = pi/2 + sqrt((e^L - 1)(e^h - 1)) + log2/sqrt2 >= ||H_0||
     (Carleman corner, rank-one growing pole, partial-isometry prime translation);
  3. proves kappa_0 <= beta/(beta + m) with exact rationals;
  4. reads the first session's 40-digit record (hash-checked) for the local floors
     and the uniform shift perturbations, and proves the normalized cumulative
     coupling bound of that session's equation (4.4) with the new kappa_0;
  5. checks weil-depth's continuation inequality m - C w^2/3 >= d at the stated
     shift, giving ||V_{w,3/4}|| <= exp(-d w) directly, without any append.
Signs are decided only by python-flint balls and exact rationals.

Prepared for Edward Baker, 24 September 2026, by Claude (Anthropic); session
configured as claude-fable-5-1, runtime-reported serving model Claude Opus 5.5
(claude-opus-5-5); the serving model may differ.  Reasoning effort not exposed.
"""
import argparse, hashlib, importlib.util, json, platform, time
from fractions import Fraction as F
from pathlib import Path

if not __debug__:
    raise SystemExit('Do not disable certificate assertions with python -O.')

FIRST_SESSION_RECORD = 'first-prime-inputs-40digits-20260924.json'
FIRST_SESSION_SHA256 = '3caf68b768d4c32584d1425eef8436522c86de8f7deaadd816dcc147b1bddf38'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--floor', default='123/250000')
    ap.add_argument('--N', type=int, default=128)
    ap.add_argument('--M', type=int, default=180)
    ap.add_argument('--bits', type=int, default=1536)
    ap.add_argument('--shift-max', default='1/50')
    ap.add_argument('--decay', default='1/5000')
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.repository or Path(__file__).resolve().parents[6]
    here = Path(__file__).resolve().parent
    builder = root/'papers/shifted-zeta/weil-depth/numerics/certify_arb.py'
    spec = importlib.util.spec_from_file_location('weil_depth_certify_arb', builder)
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
    from flint import arb as A, ctx
    ctx.prec = args.bits
    t0 = time.time()
    L, h, R = F(11, 20), F(1, 5), F(3, 4)
    m = F(args.floor)
    # 1. central floor on the joined window
    data = c.build(argparse.Namespace(N=args.N, M=args.M, horizon='3/4', log_horizon=None))
    assert [list(v) for v in data['active_prime_powers']] == [[2, 2, 1]]
    replay = c.validate(data, args.floor)
    assert replay['status'] == 'PASS'
    # 2. operator-norm bound for the complete mixed block H_0
    beta = A.pi()/2 + ((c.rat(L).exp() - 1)*(c.rat(h).exp() - 1)).sqrt() + A(2).log()/A(2).sqrt()
    beta_up = F(2464, 1000)
    assert beta < c.rat(beta_up)
    # 3. Lemma B with exact rationals
    kappa_up = beta_up/(beta_up + m)
    # 4. transfer to the normalized cumulative coupling at w = 1/1000
    rec_path = here/'records'/FIRST_SESSION_RECORD
    assert hashlib.sha256(rec_path.read_bytes()).hexdigest() == FIRST_SESSION_SHA256
    rec = json.loads(rec_path.read_text())
    assert rec['certificate_pass'] and rec['parameters']['omega'] == '1/1000'
    ck = rec['checks']
    mL, mh = F(ck['old']['all_input_floor']), F(ck['new']['all_input_floor'])
    dL = F(ck['old']['uniform_shift_perturbation_upper']['upper'])
    dh = F(ck['new']['uniform_shift_perturbation_upper']['upper'])
    dmix = F(ck['complete_mixed_shift_perturbation_upper']['upper'])
    assert (mL, mh) == (F(3, 200), F(11, 25))
    root_lower = F(812, 10000)
    assert root_lower**2 < mL*mh
    loss = dL/mL + dh/mh
    assert loss < 1
    normalized_up = (kappa_up + dmix/root_lower)/(1 - loss)
    assert normalized_up < 1
    # 5. direct continuation on the joined window (weil-depth inequality)
    bounds = c.analytic(c.rat(R), c.profile(args.M), args.N, c.prime_powers(c.rat(R)), None)
    change = bounds['generator_change_constant']
    C = F(1)
    while not change < c.rat(C):
        C += 1
    w_max, d = F(args.shift_max), F(args.decay)
    margin = m - C*w_max**2/3 - d
    assert 0 < d < m and margin >= 0
    out = {'date': '2026-09-24',
           'model': 'Claude (Anthropic); session configured claude-fable-5-1; runtime-reported serving model Claude Opus 5.5 (claude-opus-5-5); serving model may differ',
           'reasoning_effort': 'not exposed',
           'joined_window': {'R': '3/4', 'N': args.N, 'M': args.M, 'precision_bits': args.bits,
                             'central_floor': str(m), 'weil_depth_schur_test': replay['status'],
                             'matrices_content_sha256': c.content_sha256(data),
                             'minimum_pivot_lower': [x['minimum_pivot_lower'] for x in replay['checks']]},
           'mixed_block_norm_upper': str(beta_up), 'mixed_block_norm_ball': c.show(beta),
           'kappa0_upper': str(kappa_up), 'kappa0_upper_decimal': float(kappa_up),
           'first_session_inputs': {'record': FIRST_SESSION_RECORD, 'sha256': FIRST_SESSION_SHA256,
                                    'local_floors': [str(mL), str(mh)], 'mixed_shift_perturbation_upper': str(dmix),
                                    'relative_local_loss_upper': str(loss)},
           'normalized_coupling_upper': str(normalized_up), 'normalized_coupling_upper_decimal': float(normalized_up),
           'direct_continuation': {'generator_change_constant': c.show(change), 'rounded_constant': str(C),
                                   'shift_maximum': str(w_max), 'decay': str(d), 'exact_margin': str(margin),
                                   'statement': '||V_(w,3/4)|| <= exp(-d w) for 0 < w <= shift_maximum'},
           'builder_source_sha256': hashlib.sha256(builder.read_bytes()).hexdigest(),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'runtime': {'python': platform.python_version()},
           'elapsed_seconds': time.time() - t0,
           'scope': 'Internal computer-assisted closure of the first-prime append via the joined-window central floor. '
                    'Relies on the weil-depth builder/Schur test and the first session\'s local constants; specialist review outstanding.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('kappa0_upper_decimal', 'normalized_coupling_upper_decimal', 'direct_continuation')}, indent=1))


if __name__ == '__main__':
    main()
