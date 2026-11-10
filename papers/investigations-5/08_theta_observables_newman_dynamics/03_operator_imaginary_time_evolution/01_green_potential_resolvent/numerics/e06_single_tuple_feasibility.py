"""Replay frozen TND-OG-E06 r1 with python-flint. No field evaluations.

2026-11-10. Prepared for Edward Baker with OpenAI Codex assistance.
Actual model and reasoning effort were unavailable in the capture metadata.
"""
import json
import platform
import signal
from time import monotonic

import flint
from flint import arb, ctx

TIERS = (128, 256, 512, 1024)
WORK_LIMIT = 300
PANEL_CAP = 10**6
X = 30


class Unresolved(Exception):
    """A directed comparison is undecided at the current tier."""

    def __init__(self, label, value):
        self.label = label
        self.value = enclosure(value)


def enclosure(value):
    def endpoint(x):
        mantissa, exponent = x.man_exp()
        return [str(mantissa), int(exponent)]

    return {
        "lower_dyadic": endpoint(value.lower()),
        "upper_dyadic": endpoint(value.upper()),
        "ball": value.str(22, more=True),
    }


def first_hit(label, grid, gap, record):
    """Find the first certified success, escalating on any ambiguous comparison."""
    rejected = []
    for candidate in grid:
        difference = gap(candidate)
        if difference <= 0:
            closest = min(rejected) if rejected else None
            record[label] = {
                "selected": candidate,
                "success_gap": enclosure(difference),
                "rejected": len(rejected),
                "closest_rejected": (
                    {"candidate": closest[1], "gap": enclosure(closest[2])}
                    if closest is not None else None
                ),
            }
            return candidate
        if not difference > 0:
            raise Unresolved(f"{label} at {candidate}: gap versus zero", difference)
        rejected.append((difference.lower(), candidate, difference))
    record[label] = {"selected": None, "rejected": len(rejected)}
    return None


def run_screen(record):
    pi = arb.pi()
    a = pi / 8
    log2 = arb(2).log()
    h = a.sin() / (8 * a.cosh())  # sin(a)*d/(4*cosh(a*r))
    h_a = eta_eval = h / 2
    radius = eta_eval / 8
    c0 = 3 * arb(5).zeta() / (5 * (arb(5) / 2).zeta())
    kappa = (arb(27) / 26).log()
    disk_B = arb(26) / 3
    n0 = 2 + (26 / c0).log() / kappa
    c_log = arb(26).log() + 2 * disk_B * (51 * kappa).exp() * n0**2
    q = (-a).exp()

    def tail(R):
        return c_log / 4 * (-a * R).exp() * (1 + arb(X + R + 2).log())**2 * (
            (1 + q) / (1 - q)**3
        )

    R = first_hit("R_search", range(1, 257), lambda R: tail(R) - h_a / 6, record)
    if R is None:
        return "recipe exceeds cap"

    cutoff = (4 / h_a) ** (arb(2) / 3)
    Q = max(2, int(cutoff.upper().ceil().unique_fmpz()))
    beta = 2 / (3 * arb(Q) * arb(Q).sqrt())
    record.update({
        "R": R, "Q": Q, "Q_cutoff": enclosure(cutoff),
        "h": enclosure(h), "h_a": enclosure(h_a),
        "eta_eval": enclosure(eta_eval), "each_radius": enclosure(radius),
        "tail_and_prime_budget": enclosure(h_a / 6),
        "T": enclosure(tail(R)), "beta": enclosure(beta),
    })
    if not beta <= h_a / 6:
        raise Unresolved("prime budget gap", beta - h_a / 6)

    weights = [1 / (16 * (a * k).cosh()) for k in range(R)]
    weight_sum = 2 * sum(weights)
    b = h_a / (3 * weight_sum)
    log_b = b.log()
    required_bits = arb(0)
    centers = []
    for k, weight in enumerate(weights):
        for sign in (-1, 1):
            twice_v = 2 * X + sign * (2 * k + 1)
            M_v = abs(twice_v) + 26
            A_v = (M_v / c0).log()
            quotient = A_v / kappa
            n = quotient.ceil().unique_fmpz()
            if n is None:
                raise Unresolved(f"Jensen ceiling at twice_v={twice_v}", quotient)
            n = max(2, int(n))
            log_p = (2 * disk_B * n**3 / (n - 1)).log() + 51 * A_v / n
            log_M_over_2 = (arb(M_v) / 2).log()
            bits_v = (n * (log_p - log_b) - log_M_over_2) / log2
            required_bits = required_bits.max(bits_v)
            centers.append((twice_v, weight, n, log_p, log_M_over_2, bits_v))
    j_delta = int(required_bits.upper().ceil().unique_fmpz())
    log_delta = -j_delta * log2
    E = sum(
        w * (log_p + (log_delta - log_M_over_2) / n).exp()
        for _, w, n, log_p, log_M_over_2, _ in centers
    )
    record.update({
        "W_R": enclosure(weight_sum), "b": enclosure(b),
        "minus_log2_delta_star": enclosure(required_bits),
        "j_delta": j_delta, "delta": {"mantissa": 1, "exponent2": -j_delta},
        "E": enclosure(E), "E_budget": enclosure(h_a / 3),
        "center_requirements": [
            {"twice_v": v, "n_v": n, "minus_log2_delta_v": enclosure(bits)}
            for v, _, n, _, _, bits in centers
        ],
    })
    if not E <= h_a / 3:
        raise Unresolved("compact-log budget gap", E - h_a / 3)

    W = X + R
    log_pi = pi.log()
    log_B = arb(16).log() + 9 * log_pi / 4 + arb(9) / 4 + pi**2 * (81 + W**2) / 192
    log_Bc = arb(32).log() + 3 * log_pi / 8 + arb(3) / 8 + pi**2 * (
        arb(9) / 4 + (W + arb(1) / 2)**2
    ) / 192

    def log_c2(N):
        ratio = (arb(N + 2) / (N + 1))**4 * (-pi * (2 * N + 3)).exp()
        return 4 * arb(N + 1).log() - pi * ((N + 1)**2 - 1) - (-ratio).log1p()

    def log_source_tail(V):
        T = pi * (4 * V).exp()
        poly = (((T + 4) * T + 12) * T + 24) * T + 24
        return -T - log2 - 9 * log_pi / 4 + poly.log()

    log_B0 = arb(5).log() + log_c2(0)
    log_Q0 = log_source_tail(arb(0))
    log_half_delta = log_delta - log2
    record["source_log2_budget"] = enclosure(log_half_delta / log2)

    def arithmetic_log2(N):
        return (arb(5).log() + log_B + log_c2(N) + log_Q0) / log2

    def radial_log2(j):
        return (log_B + log_B0 + log_source_tail(arb(j) / 16)) / log2

    N = first_hit(
        "N_src_search", range(1, 257),
        lambda N: arithmetic_log2(N) - log_half_delta / log2, record,
    )
    j = first_hit(
        "V_search", range(1, 65),
        lambda j: radial_log2(j) - log_half_delta / log2, record,
    )
    if N is None or j is None:
        return "recipe exceeds cap"

    V = arb(j) / 16
    # Stable two-term log-sum in base two. The difference is nonpositive.
    def logadd2(x, y):
        hi = x.max(y)
        return hi + ((x.min(y) - hi) * log2).exp().log1p() / log2

    log2_Mhat = (log_B + log_B0 + log_Q0) / log2 - 1
    log2_Lhat = logadd2(log_Bc / log2 + 1, (V.log() + log_B) / log2)
    log2_Lhat += (log_B0 + log_Q0) / log2 - 1
    H = abs(log_delta).max(abs(log2 * logadd2(log2_Mhat, arb(-j_delta))))
    log2_kernel_term = (a * H / 16).log() / log2
    log2_derivative_term = log2_Lhat + j_delta - 4
    log2_radius = radius.log() / log2
    log2_R = arb(R).log() / log2
    count_factor = 1 + 2 * log2_R - log2_radius
    log2_count_argument = logadd2(log2_kernel_term, log2_derivative_term) + count_factor
    log2_cap = arb(PANEL_CAP).log() / log2
    log2_eF = 3 - j_delta + log2_radius - log2_R
    record.update({
        "N_src": N, "V": f"{j}/16", "V_grid_numerator": j,
        "arithmetic_source_log2_bound": enclosure(arithmetic_log2(N)),
        "radial_source_log2_bound": enclosure(radial_log2(j)),
        "log2_Mhat": enclosure(log2_Mhat), "log2_Lhat": enclosure(log2_Lhat),
        "H": enclosure(H),
        "L_g_kernel_term": enclosure(a * H / 16),
        "L_g_derivative_term": enclosure((log2_derivative_term * log2).exp()),
        "log2_L_g_kernel_term": enclosure(log2_kernel_term),
        "log2_L_g_derivative_term": enclosure(log2_derivative_term),
        "log2_count_factor": enclosure(count_factor),
        "log2_panel_count_argument": enclosure(log2_count_argument),
        "log2_panel_cap": enclosure(log2_cap),
        "log2_excess_over_cap": enclosure(log2_count_argument - log2_cap),
        "e_F": enclosure((log2_eF * log2).exp()),
        "log2_e_F": enclosure(log2_eF),
        "b_F": enclosure(log2_Mhat.max(0) - log2_eF),
        "N_req": None,
    })
    if log2_count_argument > log2_cap:
        return "recipe exceeds cap"
    if not log2_count_argument <= log2_cap:
        raise Unresolved("panel cap log2 gap", log2_count_argument - log2_cap)
    count = (log2_count_argument * log2).exp()
    n_req = count.ceil().unique_fmpz()
    if n_req is None or int(n_req) > PANEL_CAP:
        raise Unresolved("panel-count ceiling", count)
    record["N_req"] = int(n_req)
    return "panel screen passes"


def main():
    def time_limit(_signum, _frame):
        raise TimeoutError("300-second scalar work cap")

    start = monotonic()
    record = {}
    attempts = []
    signal.signal(signal.SIGALRM, time_limit)
    signal.setitimer(signal.ITIMER_REAL, WORK_LIMIT)
    outcome = "inconclusive"
    try:
        for bits in TIERS:
            ctx.prec = bits
            record = {"precision_bits": bits}
            try:
                outcome = run_screen(record)
            except Unresolved as exc:
                attempts.append({
                    "precision_bits": bits, "unresolved": exc.label, "interval": exc.value,
                })
            else:
                attempts.append({"precision_bits": bits, "outcome": outcome})
                break
    except TimeoutError as exc:
        attempts.append({"precision_bits": ctx.prec, "stopped": str(exc)})
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    result = {
        "task": "TND-OG-E06 r1",
        "tuple": {"X": X, "d": "1/2", "r": 1},
        "panel_cap": PANEL_CAP, "precision_tiers": TIERS,
        "work_limit_seconds": WORK_LIMIT,
        "scalar_elapsed_seconds": monotonic() - start,
        "runtime": {
            "python": platform.python_version(), "python_flint": flint.__version__,
            "FLINT": flint.__FLINT_VERSION__,
        },
        "endpoint_encoding": "[integer mantissa, exponent] means mantissa * 2**exponent",
        "search_gap_definition": "tested bound minus budget in the stated scale",
        "outcome": outcome, "attempts": attempts, "calculations": record,
        "field_evaluations": 0, "panels_executed": 0, "primes_enumerated": 0,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
