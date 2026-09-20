#!/usr/bin/env python3
"""Rational checks for a floor-backed cumulative-energy HS obstruction.

This certifies scalar inequalities in the accompanying analytic reduction.
It does NOT certify ||C|| < 1 or prove ||C|| >= 1. In particular the lower
bound for an HS norm is not a lower bound for the operator norm.
No matrices, quadratures, or floating-point sign decisions are used.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform


def load_anchor(path):
    spec = importlib.util.spec_from_file_location('energy_anchor_intervals', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def record(q):
    return {'exact_rational': str(q), 'decimal_display_only': float(q)}


def calculate(anchor, digits):
    I = anchor.I
    I.scale = 10**digits
    pi = 16*anchor.atan_reciprocal(5)-4*anchor.atan_reciprocal(239)
    harmonic = I(sum((F(1, j) for j in range(1, 1001)), F(0)))
    hn = harmonic-anchor.log_interval(1000)
    gamma = I.raw((hn-F(1, 2000)).lo, (hn-F(1, 2002)).hi)
    w0 = -gamma-pi/2-3*anchor.log_interval(2)-anchor.log_interval(pi)
    c32 = w0+sum((F(4, 4*n+1) for n in range(32)), F(0))
    assert pi.lower() > F(157, 50) and pi.upper() < F(22, 7)
    assert c32.upper() < F(1157, 500)
    # ln(10000)<10 verifies eta^(2w)>=1-20w without rounded logs.
    assert anchor.log_interval(10000).upper() < 10
    assert anchor.exp_interval(2).lower() > 7
    ell_values = (F(1, 2), F(1, 20))
    tau = (F(83, 25), F(483, 200))
    computed_tau = []
    for ell, upper in zip(ell_values, tau):
        exp = anchor.exp_interval(ell/2)
        actual = c32+ell+exp-1/exp  # c32 + 2||cosh((x-ell/2)/2)||^2
        assert actual.upper() < upper
        computed_tau.append(actual.record())

    w, delta, eta = F(1, 1000), F(24999, 500000000), F(1, 10000)
    a_upper = w/((1-w)*(1-2*w))
    y_upper = a_upper*(F(22, 7)+F(80, 29)*F(4, 25))
    kernel_bracket = 1-F(5, 2)*eta-2*eta/(1-eta/2)
    hs_lower_sq = w/2*kernel_bracket**2*(1-20*w)
    # Rectangular cross-section <=u; R^(2w)<=1.
    r, constant = F(11, 20), F(80, 29)
    hs_upper_sq = a_upper**2*(1/(2*w)+2*constant*r/(1+2*w)
                            +constant**2*r*r/(2+2*w))
    b_old, b_new = (2*w*t for t in tau)
    assert delta < min(b_old, b_new)
    total_head_rank = 32  # 16 old and 16 new; any energy-orthogonal heads.
    residual = hs_lower_sq-total_head_rank*y_upper**2
    lower_normalized_hs_sq = residual/(b_old*b_new)
    assert residual > 0
    assert lower_normalized_hs_sq > F(3, 2)**2
    # All four OPERATOR blocks have the valid common upper bound y_upper/a.
    theta = F(1, 2)
    a_floor = theta*delta
    blocks_upper = y_upper/a_floor
    assert blocks_upper < 144
    # For this theta a sharper HS obstruction uses the actual metric caps.
    caps_half = [theta*delta+(1-theta)*b for b in (b_old, b_new)]
    half_lower_sq = residual/(caps_half[0]*caps_half[1])
    assert half_lower_sq > 9
    half_hs_upper_sq = hs_upper_sq/a_floor**2
    assert half_hs_upper_sq < 903**2
    # Rank threshold: this elementary lower bound still excludes HS<1
    # at any total head rank <=35. It is inconclusive at rank 36.
    threshold = (hs_lower_sq-b_old*b_new)/(y_upper**2)
    assert 35 < threshold < 36

    # Cutoff E=I-V*V construction: a norm error eps <=delta/10 keeps
    # I-A*A-(2eps+eps^2)I >=delta/2 I, with all cross blocks retained.
    eps = delta/10
    defect_error = 2*eps+eps*eps
    assert delta-2*defect_error > delta/2
    # For rho<=eta, ||V-V_rho|| >= .99 rho^w on either window.
    assert (1-eta/F(1,20))*kernel_bracket > F(99,100)
    p_required = 1000*anchor.log_interval(F(99,100)/eps)/anchor.log_interval(10)
    assert p_required.lower() > 5200
    # Direct rational check that rho=10^-5200 cannot meet eps:
    # 10^(1/5)<5/3, hence 10^-5.2> (3/5)10^-5.
    assert F(5,3)**5 > 10
    assert F(99,100)*F(3,5)*F(1,100000) > eps

    # Elementary counter-control: large HS norm alone need not mean norm>1.
    # 16 orthogonal channels of amplitude 1/2: HS=2, operator norm=1/2.
    assert 16*F(1,2)**2 > 1 and F(1,2) < 1
    return {
        'schema': 1, 'date': '2026-09-20',
        'model': 'OpenAI GPT-6 (Codex; developer-provided identity)',
        'reasoning_effort': 'Not exposed in this session; not inferred',
        'status': 'Exact rational scalar checks with outward interval constants; analytic operator reduction requires specialist review',
        'digits': digits, 'python': platform.python_version(),
        'parameters': {'L': '1/2', 'h': '1/20', 'omega': str(w), 'M': 32,
                       'delta': str(delta), 'corner_triangle_eta': str(eta),
                       'head_ranks': [16,16], 'log_shell_width': 4},
        'tower_constant_c32': c32.record(),
        'tower_upper_constants_intervals': computed_tau,
        'tower_upper_constants_used': list(map(str,tau)),
        'cumulative_metric_upper_constants': list(map(str,(b_old,b_new))),
        'theta_half_necessary_true_to_proxy_metric_comparison_factor': record(2/delta),
        'kernel_bracket_lower': record(kernel_bracket),
        'Y_operator_norm_upper': record(y_upper),
        'Y_HS_squared_lower': record(hs_lower_sq),
        'Y_HS_squared_upper': record(hs_upper_sq),
        'rank32_residual_HS_squared_lower': record(residual),
        'all_convex_weights_CC_HS_squared_lower': record(lower_normalized_hs_sq),
        'all_convex_weights_CC_HS_lower': '3/2',
        'theta_half': {'each_operator_block_upper': record(blocks_upper),
                       'CC_HS_squared_lower': record(half_lower_sq),
                       'CC_HS_lower': '3', 'CC_HS_upper': '903'},
        'rank_obstruction_threshold_display': record(threshold),
        'cutoff': {'target_transfer_error': str(eps),
                   'defect_metric_error': str(defect_error),
                   'necessary_decimal_exponent_lower_interval': p_required.record(),
                   'certified_necessary_decimal_exponent': '>5200'},
        'certificate_pass': True,
        'not_claimed': ['An upper bound below one for the true normalized coupling',
                        'A lower operator-norm bound above one',
                        'Failure of spectral-norm estimates with these same metrics',
                        'A lower complexity bound for arbitrary finite-rank approximations',
                        'Independent specialist validation'],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--digits', type=int, default=40)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert args.digits >= 24
    repository = args.repository or Path(__file__).resolve().parents[5]
    anchor_path = repository/'papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py'
    if not anchor_path.is_file():
        raise SystemExit('Anchor interval source absent; supply --repository with the local checkout.')
    out = calculate(load_anchor(anchor_path), args.digits)
    out['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['inherited_interval_source_sha256'] = hashlib.sha256(anchor_path.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    keys = ('certificate_pass','all_convex_weights_CC_HS_squared_lower','theta_half','cutoff')
    print(json.dumps({key:out[key] for key in keys}, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Do not disable certificate assertions with python -O.')
    main()
