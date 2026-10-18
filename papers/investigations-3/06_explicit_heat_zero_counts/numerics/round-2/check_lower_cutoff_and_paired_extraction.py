#!/usr/bin/env python3
"""Finite constants for the round-2 cutoff and paired extraction note.

Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Recorded model: gpt-6.1-sol (Codex), reasoning effort ultra.
Standard-library rational arithmetic. This checks finite allowances and
exact adversarial examples; the infinite-domain analytic proof is in the note.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys


def exp_bounds(x, n=40):
    """Positive Taylor sum with a geometric majorant for its remaining tail."""
    if not 0 <= x < n + 2:
        raise ValueError("unsupported exponential enclosure")
    term = total = Q(1)
    for k in range(1, n + 1):
        term *= x / k
        total += term
    following = term * x / (n + 1)
    return total, total + following / (1 - x / (n + 2))


def atan_bounds(x, n):
    total = sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(n)), Q(0))
    following = total + (-1)**n*x**(2*n+1)/(2*n+1)
    return min(total, following), max(total, following)


def log2_bounds(n=14):
    z = Q(1, 3)
    lower = 2*sum((z**(2*k+1)/(2*k+1) for k in range(n)), Q(0))
    return lower, lower + 2*z**(2*n+1)/((2*n+1)*(1-z*z))


def run(comparison_ceiling=Q(7, 10), kernel_floor=Q(7, 25),
        derivative_allowance=Q(5, 3)):
    checks = []
    def require(name, value):
        checks.append({"name": name, "passed": bool(value)})

    p5lo, p5hi = atan_bounds(Q(1, 5), 18)
    p239lo, p239hi = atan_bounds(Q(1, 239), 6)
    pi_lo, pi_hi = 16*p5lo-4*p239hi, 16*p5hi-4*p239lo
    log2lo, log2hi = log2_bounds()
    require("Machin enclosure meets rational pi cuts", Q(157, 50) < pi_lo < pi_hi < Q(22, 7))
    require("elementary exponential cuts", Q(8, 3) < exp_bounds(Q(1))[0] < exp_bounds(Q(1))[1] < 3)
    require("log2 moment lower cut", log2lo > Q(2, 3))
    require("log3 moment upper cut", exp_bounds(Q(11, 10))[0] > 3)
    require("square root pi and square root two cuts", pi_hi < Q(71, 40)**2 and pi_hi < 4 and Q(99, 70)**2 > 2)

    x0, T0, a0 = Q(100000), Q(50000), Q(89)
    D0 = T0-3
    h0 = 1-Q(1, 2)/D0
    require("a exceeds new endpoint", T0/(2*pi_hi) > a0*a0)
    require("log cutoff upper bound", exp_bounds(Q(12))[0] > x0)
    require("log cutoff lower bound", 3**8 < x0)
    require("ordinary denominator", x0/2-Q(333, 100) > x0/3)
    ordinary_exponent = (3*Q(12)**2/32+Q(7, 8))/x0
    require("ordinary exponential allowance", ordinary_exponent == Q(23, 160000) and ordinary_exponent < Q(1, 8) and Q(8, 7)*ordinary_exponent < Q(1, 6000))
    require("heat weight reserve with L greater than one", Q(1, 2)-pi_hi/(16*x0)-26/x0**2 > 0)
    require("alpha modulus error", Q(11, 2)/x0+Q(25, 4)/x0**2 < 6/x0)
    require("alpha phase reserve", pi_hi/4+Q(11, 4)/T0+Q(85, 16)/T0**2 < 1)
    require("carrier algebraic absorption", 85/x0 < Q(1, 100) and 6/x0 < Q(1, 100) and Q(101, 100)*3/2+Q(102, 100) < 3)
    require("carrier exponential below two", Q(12)/x0 < Q(1, 2) and exp_bounds(Q(12)/x0)[1] < 2)
    require("carrier heat exponent sign", 6*pi_hi/x0 < 1 and x0/13 > 3)
    require("finite cutoff power allowance", Q(33, 32)**2 < 2 and x0/13 > 1)

    require("Gaussian h reserve", h0 > Q(999, 1000))
    require("Gaussian quadratic reserve", Q(29, 4)/D0 < Q(1, 1000))
    require("Gaussian linear reserve", Q(5, 2)/D0 < Q(1, 1000))
    require("Gaussian logarithm reserve", Q(1, 2)/(2*D0*h0) < Q(1, 1000))
    moment_log = Q(2, 1000)+Q(1, 2)*Q(1101, 1000)**2*Q(1000, 999)
    require("tilted Gaussian moment below two", moment_log < Q(2, 3) and exp_bounds(moment_log)[1] < 2)
    require("zero Gaussian moment below four thirds", exp_bounds(14/(T0-6))[1] < Q(4, 3))

    require("positive coefficient cut", 1/(8*pi_lo) < Q(1, 5)**2)
    require("positive remainder coefficient cut", Q(11, 10)**2/7 < Q(173, 1000))
    require("negative coefficient prefactor", Q(99, 70)/(4*pi_lo*pi_lo) < Q(36, 1000))
    rho = Q(445, 1000)
    require("negative coefficient geometric rate", 1/((3-2*log2hi)*pi_lo) < rho*rho)
    require("negative even geometric sum", rho**2/(1-rho**2) < Q(247, 1000))
    require("negative odd geometric sum", rho**3/(1-rho**2)*Q(71, 80) < Q(98, 1000))
    require("negative baseline at smaller a", Q(36, 1000)*(rho*Q(71, 40)+Q(247, 1000)/a0+Q(98, 1000)/a0**2) < Q(29, 1000))
    require("fixed index log coefficient", exp_bounds(Q(1, 5), 2)[0] > Q(121, 100))
    stirling_error = 1/(12*(a0*a0-Q(33, 100)))
    require("fixed index real Stirling prefactor", Q(8, 3)*exp_bounds(stirling_error)[1] < 3)
    require("fixed index nu allowance", Q(1, 2)+1/(4*a0*a0) < 1)
    require("fixed index extra exponential absorbed", 3*a0*a0/10 > 2 and exp_bounds(Q(2))[0] > 5)
    require("fixed index Gaussian contribution", Q(4, 3)/(1+a0*a0/2) < 1)

    coefficient = Q(2, 5)*243+Q(58, 1000)*3
    require("Gaussian coefficient total", coefficient == Q(48687, 500))
    require("old compression is unavailable at new endpoint", coefficient/(a0-Q(173, 200)) > 98/a0)
    require("old compression threshold", 98*Q(173, 200)/(98-coefficient) == Q(42385, 313))
    f14 = Q(11, 10)**14*720*2**10*Q(3, 8)**100
    f15 = Q(11, 10)**15*Q(135135, 64)*2**11*Q(3, 8)**121
    require("tail base 14", f14 < Q(1, 10**30))
    require("tail base 15", f15 < Q(1, 10**30))
    require("tail recurrence below one", Q(121, 50)*14*Q(3, 8)**44 < 1)
    require("tail recurrence decreases", Q(15, 14)*Q(3, 8)**4 < 1)
    require("tail enlargement and Gaussian domination", 2*a0*a0 > 14 and 1/D0 < Q(1, 8))
    require("tail delta below one over a", Q(4, 10**30) < a0**13)
    bracket = Q(2, 3)+coefficient/(a0-Q(173, 200))+2/a0
    require("uncompressed full remainder bracket", bracket == Q(42215698, 23532045) and bracket < Q(9, 5) < 2)

    require("opposite sum allowance", 16*13/x0 < Q(23, 500)**2)
    require("ordinary normalized allowance", (Q(242, 147)+Q(23, 500))/6000 < Q(3, 10000))
    require("two normalized remainder allowance", 4*pi_hi < 13)
    budget = Q(95, 147)+Q(23, 500)+Q(3, 10000)+52/x0
    require("new comparison budget exact value", budget == Q(5094127, 7350000))
    require("new comparison below declared band", budget < Q(347, 500) < Q(7, 10))
    require("requested comparison ceiling fits sufficient budget", budget < comparison_ceiling)

    # Schwarz--Pick bound: clearing the positive denominator yields
    # 84s^2-70s+16 = 84(s-5/12)^2+17/12 > 0.
    require("Schwarz Pick quadratic completion", -2*84*Q(5, 12) == -70 and 84*Q(5, 12)**2+Q(17, 12) == 16)
    require("proved derivative allowance fits request", Q(5, 3) <= derivative_allowance)
    # An exact disk automorphism: a=-2/5, r=1/2, q=7/10.
    q, a, r = Q(7, 10), -Q(2, 5), Q(1, 2)
    witness = q*(1-a*a)/(r*(1+q*a))
    require("disk automorphism derivative witness", witness == Q(49, 30))
    require("requested derivative allowance survives exact witness", witness <= derivative_allowance)
    v = Q(7, 2)
    endpoint = v/(v*v+Q(1, 4))
    require("kernel convexity reserve on whole interval", Q(5, 2)**2-3*Q(1, 4) > 0)
    require("paired endpoint floor", endpoint == Q(7, 25))
    require("requested kernel floor survives real endpoint", kernel_floor <= endpoint)
    pair = (Q(5, 2)/(Q(5, 2)**2+Q(1, 4)) + Q(9, 2)/(Q(9, 2)**2+Q(1, 4)))/2
    require("nonreal conjugate pair retains multiplicity", pair > endpoint)
    require("double root contributes twice the endpoint", 2*endpoint == Q(14, 25) and 2*kernel_floor <= 2*endpoint)
    A, B = Q(25, 7)*Q(2003, 8000), Q(25, 7)*Q(5, 3)
    require("rounded new count constants", A == Q(2003, 2240) and A < Q(9, 10) and B == Q(125, 21) < 6)
    oldq = Q(96624791, 147000000)
    require("original budget enables smaller derivative", oldq < Q(48, 73) and Q(48, 73)**2+Q(55, 73)**2 == 1 and 4*Q(48, 73)/(1+Q(55, 73)) == Q(3, 2))
    require("high height additive allowance", Q(25, 7)*Q(3, 2) == Q(75, 14) < Q(11, 2))
    return {
        "status": "pass" if all(c["passed"] for c in checks) else "fail",
        "domain": {"x_min": 100000, "t": "0<t<=1/2", "y": "3<=y<=4"},
        "comparison_budget": str(budget), "remainder_bracket_endpoint": str(bracket),
        "count_bound": "K_t(X)<=9/10*log(X+2)+6 for X>=100000",
        "high_height_corollary": "K_t(X)<=9/10*log(X+2)+11/2 for X>=2000000",
        "requested_comparison_ceiling": str(comparison_ceiling),
        "requested_kernel_floor": str(kernel_floor),
        "requested_derivative_allowance": str(derivative_allowance),
        "exact_automorphism_derivative": str(witness),
        "checks": checks,
        "scope": "Exact finite arithmetic and adversarial functions; analytic domain proof and imports are not formally verified. No H_t zero sampling.",
    }


def write_record(path):
    script = Path(__file__).resolve()
    note = script.parents[2]/"notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md"
    injections = [
        ("comparison_budget", ["--comparison-ceiling", "69/100"]),
        ("kernel_endpoint", ["--kernel-floor", "3/10"]),
        ("derivative_automorphism", ["--derivative-allowance", "3/2"]),
    ]
    runs = []
    for label, flags in [("normal", [])] + injections:
        p = subprocess.run([sys.executable, str(script), *flags], capture_output=True, text=True)
        result = json.loads(p.stdout)
        expected = 0 if label == "normal" else 1
        if p.returncode != expected:
            raise RuntimeError(f"unexpected exit code {p.returncode} for {label}: {p.stderr}")
        runs.append({"name": label, "arguments": flags, "exit_code": p.returncode,
                     "failed_checks": [c["name"] for c in result["checks"] if not c["passed"]],
                     "result": result if label == "normal" else {k: result[k] for k in ("status", "requested_comparison_ceiling", "requested_kernel_floor", "requested_derivative_allowance")}})
    baseline_note = script.parents[2]/"notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md"
    current = baseline_note.read_bytes()
    repaired_link = b"../../01_dirichlet_newman_families/notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md"
    reviewed_link = repaired_link.replace(b"/round-1", b"")
    if current.count(repaired_link) != 1:
        raise RuntimeError("unexpected baseline Note 01 link provenance")
    restored = current.replace(repaired_link, reviewed_link, 1)
    reviewed_sha = "46266338f670fde0514ec51029ba85bc34b25a5075c149107abb146fa45e9196"
    if hashlib.sha256(restored).hexdigest() != reviewed_sha:
        raise RuntimeError("baseline Note 01 differs by more than the documented link repair")
    baseline_identity = {
        "note": "../../notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md",
        "reviewed_commit": "146b3f9", "link_repair_commit": "452eee4",
        "current_sha256": hashlib.sha256(current).hexdigest(),
        "reviewed_sha256": reviewed_sha,
        "reviewed_bytes_recovered_by_reversing_exactly_one_link_repair": True,
        "repaired_link": repaired_link.decode(), "reviewed_link": reviewed_link.decode(),
        "scope": "Pre-existing hyperlink-only change; no mathematical text changed. Original review/build digests remain historical.",
    }
    record = {
        "date_local": "2026-10-17", "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker", "model": "gpt-6.1-sol (Codex)", "reasoning_effort": "ultra",
        "llm_assistance": "Substantial; three same-model subagents assisted in analytic development.",
        "review_status": "Proved in-note from named imports; same-model checks only. New work not covered by Claude Review 02.",
        "question": "Does the retained full remainder budget close at x>=100000, and do paired extraction constants improve the count?",
        "resource_limit": "Four fixed standard-library executions; no zero survey or parameter sweep.",
        "environment": {"python": platform.python_version(), "implementation": platform.python_implementation(), "platform": platform.system()},
        "script": script.name, "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "note": "../../notes/round-2/"+note.name, "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "source": "https://arxiv.org/html/1904.12438v2", "baseline_note_01_identity": baseline_identity, "runs": runs,
        "limits": "Finite constants and exact class controls support the written proof. No specialist or cross-model review of the new result; no consumer gain or RH/Newman bound.",
    }
    path.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"record": str(path), "normal_exit": 0, "injection_exits": [1, 1, 1],
                      "comparison_budget": runs[0]["result"]["comparison_budget"],
                      "failed_injection_checks": {row["name"]: row["failed_checks"] for row in runs[1:]}}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison-ceiling", type=Q, default=Q(7, 10))
    parser.add_argument("--kernel-floor", type=Q, default=Q(7, 25))
    parser.add_argument("--derivative-allowance", type=Q, default=Q(5, 3))
    parser.add_argument("--write-record", type=Path)
    args = parser.parse_args()
    if args.write_record:
        write_record(args.write_record)
    else:
        result = run(args.comparison_ceiling, args.kernel_floor, args.derivative_allowance)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["status"] == "pass" else 1)
