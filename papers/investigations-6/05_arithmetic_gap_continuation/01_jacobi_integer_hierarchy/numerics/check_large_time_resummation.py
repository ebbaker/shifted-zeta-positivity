"""Canonical zeros and their loop and phase expansions at T=1000.

20 November 2026. For Edward Baker, with OpenAI Codex assistance.
Desktop chat configuration gpt-6.2-astra, max effort. Run with python-flint.
"""

import json
from math import comb, factorial, prod

import flint
from flint import acb, arb, arb_series, ctx, fmpq, fmpq_series


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def check_residue_kernel():
    # After h=-it the universal residue, divided by i^(n-1), is rational.
    # Compare the defining Laurent coefficient with its product formula.
    ctx.cap = 11
    t = fmpq_series([0, 1])
    sinh_over_t = fmpq_series([
        fmpq(1, factorial(j + 1)) if j % 2 == 0 else 0 for j in range(ctx.cap)
    ])
    for n in range(1, 12):
        for y in (fmpq(0), fmpq(-1), fmpq(3, 2), fmpq(-7, 3)):
            coefficient = ((y * t).exp() / sinh_over_t**n)[n - 1]
            explicit = fmpq(prod(y + n - 2 * j for j in range(1, n)), factorial(n - 1))
            require(coefficient == explicit, "exact exponential residue kernel")


class ThetaAt1000:
    """Integrate the first square mode on [1,2] and enclose the full source."""

    def __init__(self):
        self.time = arb(1000)
        self.pi = arb.pi()
        t = self.time
        self.saddle = -(-8 * self.pi / t * (-18 / t).exp()).lambertw(-1) / 4 - 9 / (2 * t)
        self.curvature = 8 * t * self.saddle - 2 * t + 36
        self.peak = self.q(self.saddle)
        self.first_mode = 3 / (2 * self.pi)

        one, two = arb(1), arb(2)
        self.tail = self.omitted_integral_bound(one, two)
        self.mass = self.integral(lambda u: 1)
        require(self.mass > 0, "failed to normalize the complete source")

    def q(self, u):
        return self.time * u * u + 9 * u - self.pi * (4 * u).exp()

    def q_prime(self, u):
        return 2 * self.time * u + 9 - 4 * self.pi * (4 * u).exp()

    def omitted_integral_bound(self, one, two):
        # Every real test used below satisfies |g(u)| <= (u+2)^7 exp(16(u+2)).
        # The complete factor b in the note is less than 2. On [1,2] the
        # unused square modes contribute at most 32 exp(-3 pi exp(4)).
        require(1 < self.saddle and self.saddle < 2, "saddle outside the integration interval")
        require(self.q_prime(one) > 0 and self.q(one) > self.q(arb(0)), "left endpoint test")
        require(2 * self.time < 16 * self.pi * (4 * one).exp(), "concavity on [1,infinity)")
        require(16 * (-3 * self.pi).exp() < arb(1) / 2, "complete prefactor bound")
        require(16 * (-5 * self.pi * (4 * one).exp()).exp() < arb(1) / 2, "square tail ratio")
        left = 2 * 3**7 * (48 + self.q(one) - self.peak).exp()
        middle = 32 * 4**7 * (64 - 3 * self.pi * (4 * one).exp()).exp()
        decay = -self.q_prime(two) - 16 - arb(7) / 4
        require(decay > 0, "right tail derivative test")
        right = 2 * 4**7 * (64 + self.q(two) - self.peak).exp() / decay
        return (left + middle + right).upper()

    def integral(self, test):
        def integrand(u, analytic):
            # All central integrands are entire. The sole denominator here
            # is exp(4u), which never vanishes.
            exponential = (4 * u).exp()
            phase = self.time * u * u + 9 * u - self.pi * exponential - self.peak
            return phase.exp() * (1 - self.first_mode / exponential) * test(u)

        tol = arb("1e-53")
        value = acb.integral(integrand, 1, 2, abs_tol=tol, rel_tol=tol)
        require(value.is_finite() and value.imag.contains(0), "real finite integral failed")
        return value.real + arb(0, self.tail)

    def expect(self, test):
        return self.integral(test) / self.mass

    def cumulants(self):
        center = arb(4) / 3
        moments = [arb(1)]
        cumulants = [arb(0)]
        for n in range(1, 8):
            moments.append(self.expect(lambda u: (u - center)**n))
            cumulants.append(moments[n] - sum(
                comb(n - 1, j - 1) * cumulants[j] * moments[n - j] for j in range(1, n)
            ))
        cumulants[1] += center
        return cumulants

    def root(self, q, mean):
        # Newton gives a candidate only. Direct full-source signs at two
        # exact dyadics establish the bracket. Each caller checks its index.
        center = (q / mean).mid()
        for _ in range(4):
            value = self.expect(lambda u: (center * u).cos())
            slope = -self.expect(lambda u: u * (center * u).sin())
            require(not slope.contains(0), "Newton candidate slope")
            center = (center - value / slope).mid()
        width = arb("1e-43")
        lo, hi = (center - width).lower(), (center + width).upper()
        signs = [self.expect(lambda u: (x * u).cos()) for x in (lo, hi)]
        require(signs[0] * signs[1] < 0, "full field failed direct sign bracket")
        return lo.union(hi)

    def loop_displacements(self, q, sine):
        # h/sin(h)=1+h^2/6+O(h^4). Precision four suffices for four residues.
        jet = arb_series([
            self.expect(lambda u: (u / self.saddle)**j
                        * (q * u / self.saddle + j * self.pi / 2).cos()) / factorial(j)
            for j in range(4)
        ])
        h = arb_series([0, 1])
        raw = h + sine * jet * arb_series([1, 0, arb(1) / 6])
        # cos(q+h)=-sine*sin(h), so g=f-cos equals jet+sine*sin(h).
        arcsine = (sine * jet + h.sin()).asin()
        return [[(factor**n)[n - 1] / n for n in range(1, 5)]
                for factor in (raw, arcsine)]


def radius_tests(source, mean, largest_q):
    r = arb(1) / 2
    L = source.saddle
    weighted = source.expect(lambda u: 2 * (u - L)**2 * (r * (u - L) / L).cosh())
    B = largest_q + r
    eta = r.exp() / r.sin() * (B * abs(mean - L) / L + B**2 * weighted / (2 * L**2))
    require(eta < 1, "cosine comparisons failed")

    R = arb(16)
    require(1 < mean and mean < 2 and R / mean < 16, "weighted envelope for phase test")
    weighted = source.expect(lambda u: 2 * (u - mean)**2 * (R * (u - mean) / mean).cosh())
    delta = R**2 * weighted / (2 * mean**2)
    require(delta < 1, "centered logarithm disk failed")
    Q = R / 2 + (1 - delta).log() / 6
    require(Q > largest_q, "inverse series radius failed")
    return eta, delta, Q


def phase_errors(q, mean, c, root):
    h = -c[1]
    cube = 2 / (3 * h).sqrt() * (((3 * (3 * h).sqrt() * q / 2).asinh()) / 3).sinh()
    inv5 = q + c[1] * q**3 + (3 * c[1]**2 + c[2]) * q**5
    inv7 = inv5 + (12 * c[1]**3 + 8 * c[1] * c[2] + c[3]) * q**7
    return {
        "mean_lattice_minus_root": (q / mean - root).str(14),
        "resummed_cubic_minus_root": (cube / mean - root).str(14),
        "odd_inverse_degree_5_minus_root": (inv5 / mean - root).str(14),
        "odd_inverse_degree_7_minus_root": (inv7 / mean - root).str(14),
    }


def main():
    ctx.prec = 224
    check_residue_kernel()
    ctx.cap = 4
    source = ThetaAt1000()
    cumulant = source.cumulants()
    a, c = cumulant[1], [arb(0)]
    for j in range(1, 4):
        p = 2 * j + 1
        c.append((-1)**(j + 1) * cumulant[p] / (factorial(p) * a**p))
    require(c[1] < 0, "cubic sign")
    eta, delta, Q = radius_tests(source, a, 3 * source.pi / 2)
    root_balls, examples = [], []
    for k in (1, 2):
        q = (2 * k - 1) * source.pi / 2
        root = source.root(q, a)
        require(abs(source.saddle * root - q) < arb(1) / 2, "bracket outside its counted disk")
        root_balls.append(root)
        series_errors = []
        for terms in source.loop_displacements(q, (-1)**(k - 1)):
            partial = q
            errors = []
            for term in terms:
                partial += term
                errors.append((partial / source.saddle - root).str(14))
            series_errors.append(errors)

        examples.append({
            "k": k, "root_bracket_ball": root.str(45),
            "loop_partial_minus_root_orders_1_to_4": series_errors[0],
            "arcsine_partial_minus_root_orders_1_to_4": series_errors[1],
            **phase_errors(q, a, c, root),
        })
    ratio_defect = 1 - root_balls[1] / (3 * root_balls[0])
    require(ratio_defect > 0, "canonical sign of the two-root ratio")
    L, curvature = source.saddle, source.curvature
    scaled = L**3 * curvature**3 / (curvature + 2 * source.time) * ratio_defect

    k = 40
    q = (2 * k - 1) * source.pi / 2
    cap = (q + arb(1) / 2) / a
    # On [0,cap] the centered transform has positive real part, and the
    # phase is strictly increasing. Its distance from a*x is below pi/2.
    real_part_lower = 1 - cap**2 * cumulant[2] / 2
    require(real_part_lower > 0, "centered real-part test at index 40")
    phase_slope_lower = a - cumulant[2].sqrt() / real_part_lower
    require(phase_slope_lower > 0, "phase monotonicity at index 40")
    root = source.root(q, a)
    require(0 < root and root < cap and abs(a * root - q) < arb(1) / 2,
            "phase index test at index 40")
    higher_index = {
        "k": k, "q_over_mean_sqrt_curvature": (q / (a * curvature.sqrt())).str(16),
        "root_bracket_ball": root.str(45), "physical_interval_upper": cap.str(16),
        "centered_real_part_lower_bound": real_part_lower.str(16),
        "phase_slope_lower_bound": phase_slope_lower.str(16),
        **phase_errors(q, a, c, root),
    }
    return {
        "date": "2026-11-20", "prepared_for": "Edward Baker",
        "assistance": "OpenAI Codex; desktop chat setting gpt-6.2-astra, max effort; no separate per-turn configuration",
        "scope": "Outward Arb intervals at one positive time. All three root brackets use direct signs with the same complete source.",
        "T": 1000, "precision_bits": ctx.prec, "python_flint": flint.__version__,
        "residue_kernel_check": "exact rational Laurent coefficients through n=11 at y=0,-1,3/2,-7/3",
        "source_tail_upper": source.tail.str(10), "mean": a.str(24),
        "third_cumulant": cumulant[3].str(24), "contour_ratio_upper_bound": eta.str(15),
        "phase_disk_delta_upper_bound": delta.str(15), "inverse_radius_lower_bound": Q.str(15),
        "examples": examples, "one_minus_x2_over_3x1": ratio_defect.str(22),
        "scaled_by_L3_curvature3_over_curvature_plus_2T": scaled.str(18),
        "limiting_constant_4pi2_over_3": (4 * source.pi**2 / 3).str(18),
        "growing_window_example": higher_index,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
