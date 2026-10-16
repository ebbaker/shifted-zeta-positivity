#!/usr/bin/env python3
"""Certified full gamma/contact scalar for the exact A17 sources and D_2 sources.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.

Arb FFT and digamma arithmetic; analytic bounds for source-sampling alias,
frequency trapezoid alias, and the omitted frequency tail. No numerical
agreement or sampled sign test is used as a rigorous error estimate.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import platform
import time

import flint
from flint import arb, acb, ctx


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rat(value):
    q = Fraction(value)
    return arb(q.numerator)/q.denominator


def inflate(value, error):
    return value+arb(0, error.abs_upper())


def enclosure(value):
    require(value.is_finite(), "Nonfinite output enclosure")
    return {"display": value.str(30),
            "lower": str(value.lower().fmpq()),
            "upper": str(value.upper().fmpq())}


def load_source(directory):
    path = directory/"source_norm_enclosures.py"
    spec = importlib.util.spec_from_file_location("certified_source_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    record_path = directory/"records"/"source_norm_enclosures.json"
    record = json.loads(record_path.read_text())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    require(record["script_sha256"] == digest, "Source script/record hash mismatch")
    return module, record, digest, hashlib.sha256(record_path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-directory", type=Path,
                        default=Path(__file__).resolve().parent)
    parser.add_argument("--fft-power", type=int, default=18)
    parser.add_argument("--period", type=int, default=48)
    parser.add_argument("--frequency-cutoff", type=int, default=5000)
    parser.add_argument("--precision-bits", type=int, default=128)
    parser.add_argument("--max-width", default="1e-6")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent/"records"/"gamma_scalar_certificate.json")
    args = parser.parse_args()
    source, source_record, source_hash, record_hash = load_source(args.source_directory)
    ctx.prec = args.precision_bits
    started = time.monotonic()
    count = 2**args.fft_power
    period = rat(args.period)
    step = Fraction(args.period, count)
    step_ball = rat(step)
    frequency_step = 2*arb.pi()/period
    sampling_frequency = 2*arb.pi()/step_ball
    candidate = (rat(args.frequency_cutoff)*period/(2*arb.pi())).floor().unique_fmpz()
    require(candidate is not None, "Frequency endpoint floor is not uniquely enclosed")
    max_n = int(candidate)
    cutoff = frequency_step*max_n
    require(cutoff <= args.frequency_cutoff, "Frequency endpoint rounded incorrectly")
    require(frequency_step*(max_n+1) > args.frequency_cutoff,
            "Frequency endpoint is not the intended floor")
    require(max_n < count//2 and cutoff > 1, "Invalid FFT/frequency configuration")
    require(sampling_frequency > 2*cutoff, "Source alias separation condition failed")
    half_support = Fraction(9,20)
    max_j_q = half_support/step
    max_j = max_j_q.numerator//max_j_q.denominator
    norms = [source.record_ball(row["normalizer"]) for row in source_record["sources"]]
    values = [acb(0)]*count
    for j in range(-max_j,max_j+1):
        x = rat(j*step)
        values[j % count] = acb(
            source.source_value(0,x,normalizer=norms[0]),
            source.source_value(1,x,normalizer=norms[1]))
    print(json.dumps({"stage":"sampled", "nonzero_grid_count":2*max_j+1,
                      "elapsed_seconds":time.monotonic()-started}),flush=True)
    transformed = acb.dft(values)
    del values
    print(json.dumps({"stage":"fft", "count":count,
                      "elapsed_seconds":time.monotonic()-started}),flush=True)

    derivative4_l1 = [source.record_ball(row["normalized_derivative_L1_cauchy_bounds"][4])
                      for row in source_record["sources"]]
    # 2*zeta(4)=pi^4/45; aliases are separated by sampling_frequency.
    source_alias = [a*arb.pi()**4/(45*(sampling_frequency-cutoff)**4)
                    for a in derivative4_l1]
    accum = [[arb(0),arb(0)] for _ in range(2)]
    raw = [[arb(0),arb(0)] for _ in range(2)]
    root2 = arb(2).sqrt()
    log2 = arb(2).log()
    logpi = arb.pi().log()
    for n in range(max_n+1):
        t = frequency_step*n
        positive = transformed[n]
        negative_conjugate = transformed[(-n) % count].conjugate()
        # For real input sequences, packing yields their two independent DFTs.
        f0 = (positive+negative_conjugate)/2
        f1 = (positive-negative_conjugate)/acb(0,2)
        require(f0.imag.contains(0), "Even source DFT lost its real symmetry")
        require(f1.real.contains(0), "Odd source DFT lost its imaginary symmetry")
        components = [step_ball*f0.real,step_ball*f1.imag]
        multiplier = acb(rat("1/4"),t/2).digamma().real-logpi
        transport = rat("3/2")-root2*(t*log2).cos()
        require(transport > 0, "Transport multiplier must be positive")
        factor = rat(1 if n==0 else 2)/period
        for j in range(2):
            h = components[j]
            wide = inflate(h,source_alias[j])
            bare = factor*multiplier*(h*h)
            enclosed = factor*multiplier*(wide*wide)
            raw[j][0] += bare
            raw[j][1] += transport*bare
            accum[j][0] += enclosed
            accum[j][1] += transport*enclosed
    del transformed
    print(json.dumps({"stage":"summed", "frequency_nodes":max_n+1,
                      "elapsed_seconds":time.monotonic()-started}),flush=True)

    u = 1+1/root2
    width_f = rat("9/10")
    width_h = width_f+log2
    rows=[]
    for j,row in enumerate(source_record["sources"]):
        l1_f=source.record_ball(row["normalized_L1"])
        for kind,scale,width in [(0,arb(1),width_f),(1,u,width_h)]:
            l1=scale*l1_f
            derivative_l1=scale*derivative4_l1[j]
            # Discrete tail <= the decreasing integral from cutoff to infinity.
            tail = derivative_l1**2/arb.pi()*cutoff**(-7)/7*(
                6+(rat("29/25")).log()/2+cutoff.log()+rat("1/7"))
            require(period > width, "Gamma alias bound needs period beyond support")
            trapezoid_alias = 2*l1**2*((width-period)/2).exp()/(
                (1-(-period/2).exp())*(1-(-2*(period-width)).exp()))
            value=inflate(accum[j][kind],tail+trapezoid_alias)
            require(2*value.rad() < rat(args.max_width), "Final gamma enclosure is too wide")
            rows.append({"source":j,"kernel":"F" if kind==0 else "D2F",
                         "gamma":enclosure(value),
                         "raw_finite_sum":enclosure(raw[j][kind]),
                         "finite_sum_with_sampling_alias":enclosure(accum[j][kind]),
                         "frequency_truncation_error_bound":enclosure(tail),
                         "frequency_trapezoid_alias_bound":enclosure(trapezoid_alias),
                         "source_sampling_alias_per_Fourier_value":enclosure(source_alias[j]),
                         "certified_width":enclosure(2*value.rad())})
    record={"status":"CERTIFIED","date":"2026-09-29",
            "model":"GPT-6 (Codex)","serving_variant":"not exposed","reasoning_effort":"not exposed",
            "definition":"Gamma[H]=integral (Re psi(1/4+it/2)-log pi)*abs(Hhat(t))^2 dt/(2pi)",
            "fourier_convention":"Hhat(t)=integral H(x)*exp(-itx) dx; U_a H(x)=H(x-a)",
            "transport":"D2=I-2^(-1/2) U_log(2)",
            "parameters":{"fft_count":count,"spatial_period_exact":args.period,
                          "spatial_step_exact":str(step),"max_frequency_index":max_n,
                          "frequency_cutoff":enclosure(cutoff),"precision_bits":args.precision_bits},
            "source_script_sha256":source_hash,"source_record_sha256":record_hash,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "runtime":{"python":platform.python_version(),"python_flint":flint.__version__,
                       "flint":flint.__FLINT_VERSION__},
            "results":rows,
            "scope":"Actual gamma/contact scalar only; no actual Sonin trace or residual sign claimed."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"CERTIFIED","results":[{"source":r["source"],
                      "kernel":r["kernel"],"gamma":r["gamma"]["display"],
                      "width":r["certified_width"]["display"]} for r in rows],
                      "elapsed_seconds":time.monotonic()-started,"output":str(args.output)},indent=2))


if __name__=="__main__":
    main()
