#!/usr/bin/env python3
"""Enclose prime-2 correlations for exact existing A17 sources.

Prepared for Edward Baker with GPT-6 (Codex); serving variant and effort
not exposed. Uses Arb/Acb arithmetic and analytic endpoint tail bounds.
No repository file is modified. New results are source-specific diagnostics.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from flint import arb, acb, ctx


def require(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pack(x):
    require(x.is_finite(), 'Non-finite result')
    return {'display': x.str(24), 'rational_lower': str(x.lower().fmpq()),
            'rational_upper': str(x.upper().fmpq())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerics', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bits', type=int, default=192)
    args = parser.parse_args()
    p = args.numerics
    spec = importlib.util.spec_from_file_location('a17_source', p/'source_norm_enclosures.py')
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    ctx.prec = args.bits
    normpath = p/'records/source_norm_enclosures.json'
    gammapath = p/'records/gamma_scalar_certificate.json'
    summarypath = p/'records/sonin_scalar_summary.json'
    norms = json.loads(normpath.read_text())
    gamma = json.loads(gammapath.read_text())
    summary = json.loads(summarypath.read_text())
    require(norms['script_sha256'] == digest(p/'source_norm_enclosures.py'), 'Source script mismatch')
    require(gamma['script_sha256'] == digest(p/'gamma_scalar_certificate.py'), 'Gamma generator mismatch')
    require(gamma['source_record_sha256'] == digest(normpath), 'Gamma source mismatch')
    require(summary['script_sha256'] == digest(p/'sonin_scalar_summary.py'), 'Summary generator mismatch')
    for name, sha in summary['input_sha256'].items():
        require(sha == digest(p/'records'/name), 'Summary input mismatch: '+name)
    a = arb(2).log()
    b = src.ball(src.B)
    d = b-a/2
    require(d > 0 and a-b > 0, 'Overlap coordinates invalid')
    # At u=255/256, a/2+d*u > b*(255/256), so the existing source
    # endpoint-tail enclosure covers all omitted overlap points.
    yend = src.ball(src.Y_END)
    require(a/2+d*yend > b*yend, 'Endpoint-tail coverage invalid')
    rows = []
    for sid in range(2):
        row = norms['sources'][sid]
        normalizer = src.record_ball(row['normalizer'])
        parity, polynomial = src.initial_polynomial(sid)
        def value(x):
            y = x/b
            den = 1-y*y
            if den.contains(0):
                return acb('nan')
            v = 1/den
            out = (-v).exp()*src.polyval(polynomial, v)/normalizer
            return out*y if parity else out
        def integrand(u, analytic):
            return value(a/2-d*u)*value(a/2+d*u)
        breaks = [src.Q(0), src.Q(1,2), src.Q(3,4), src.Q(7,8),
                  src.Q(15,16), src.Q(31,32), src.Q(63,64),
                  src.Q(127,128), src.Y_END]
        total = acb(0)
        for lo, hi in zip(breaks, breaks[1:]):
            z = acb.integral(integrand, acb(src.ball(lo)), acb(src.ball(hi)),
                             rel_tol=arb(2)**-100, abs_tol=arb(2)**-100,
                             deg_limit=128, eval_limit=100000, depth_limit=40)
            require(z.is_finite() and z.imag.contains(0), 'Correlation integration failure')
            total += z
        core = 2*((-1)**sid)*d*total.real
        n1 = src.record_ball(row['normalized_derivative_norm_squares'][1])
        # ||F||_infinity^2 <= ||F||_2 ||F'||_2; ||F||_2=1 exactly.
        supnorm = n1.sqrt().sqrt()
        raw_tail = src.record_ball(row['raw_L1_endpoint_tail_bound'])
        # A conservative factor 2 uses the both-endpoint L1 bound directly.
        omitted = 2*supnorm*raw_tail/normalizer
        kappa = core + arb(0, omitted.abs_upper())
        prime = arb(2).sqrt()*a*kappa
        gr = next(q for q in gamma['results'] if q['source']==sid and q['kernel']=='F')
        gdata = gr['gamma']
        if 'rational_lower' not in gdata:
            gdata = {'rational_lower':gdata['lower'], 'rational_upper':gdata['upper']}
        gamma_f = src.record_ball(gdata)
        q1 = gamma_f-prime
        prior = summary['sources'][sid]
        b2 = src.record_ball(prior['B2_coercivity_and_residual_enclosure'])
        residual = q1-b2
        require(q1 > 0, 'Direct source positivity unresolved')
        rows.append({'source':sid, 'correlation_kappa_log2':pack(kappa),
                     'analytic_correlation_endpoint_error':pack(omitted),
                     'prime_2_form_a2':pack(prime), 'Gamma_F':pack(gamma_f),
                     'direct_Q1':pack(q1), 'prior_B2':pack(b2),
                     'complete_residual_coarse_enclosure':pack(residual),
                     'coarse_residual_contains_zero':bool(residual.contains(0))})
    result = {'date':'2026-09-29', 'model':'GPT-6 (Codex)',
              'serving_variant':'not exposed', 'reasoning_effort':'not exposed',
              'status':'CERTIFIED_WITH_INHERITED_SOURCE_AND_GAMMA_RECORDS',
              'scope':'Direct arithmetic diagnostic for exact f0,f1. No independent finite-place trace, residual sign, or all-support theorem.',
              'precision_bits':args.bits, 'script_sha256':digest(Path(__file__)),
              'input_sha256':{x.name:digest(x) for x in [normpath,gammapath,summarypath]},
              'sources':rows}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    for row in rows:
        print(json.dumps({'source':row['source'], **{k:row[k]['display'] for k in
              ('correlation_kappa_log2','prime_2_form_a2','direct_Q1','complete_residual_coarse_enclosure')}}))


if __name__ == '__main__':
    main()
