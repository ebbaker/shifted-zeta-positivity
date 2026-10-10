# External review of program 12 (radial Bessel geometry)

10 October 2026. Prepared for Edward Baker. Reviewer model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, running in Claude Cowork. This is a
cross-model review of material prepared with GPT-6 (Codex); it includes
independent replays written from scratch rather than reruns of the folder's
own scripts alone. Location:
`papers/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/reviews/`.

Reviewed artifacts: `README.md`, Notes 1 and 2, internal reviews 1 and 2,
`numerics/check_radial.py`, `numerics/check_radial_center_obstructions.py`,
both JSON records, and the program-12 sections of Heat Notes 14, 15 and 16.
Source state: commit `eddf25c` (10 October 2026).

## 1. Summary verdict

Everything in the folder that I checked is correct. Almost none of it is
load-bearing. The folder proves (a) that the genuine theta state has a
positive three-dimensional radial lift, (b) that the lift evolves by an
exact nonlocal generator, (c) a change-of-variables identity for the
fourth-jet threshold test, and (d) two "shape obstructions" (no positive
Gaussian mixture; no positive radial realization in dimension 11 or above).
Items (a)–(c) are representation results. Items (d) follow in one line
from the existence of a single zero of ξ (section 4 below), so the
certificates, while exact, certify something already known. The one
clarifying piece is Note 1's counterexample (10), which shows the radial
positivity mechanism cannot exclude a double zero even in principle. The
notes say as much themselves, candidly.

My recommendation is to close program 12 with a short closure note rather
than pursue the proposed next task. Reasons follow.

## 2. What was verified

Analytic checks, by hand:

- The summand identity `phi_n = e^r (2a_n^2 - 3a_n) e^{-a_n}`,
  `a_n = pi n^2 e^{4r}`, agrees with the standard de Bruijn–Newman `Phi`.
- Criterion (5) of Note 1, `R_t > 0 iff -Phi'/Phi > 2tr`, is exact.
- The three-dimensional marginal relation (2), the inverse (1), the
  generator (4) `dR/dt = r^2 R - 2 int_r^infty R(s) s ds`, and the closed
  form `R_t = e^{tr^2}(R_0 - t Phi_e/pi)` are all correct.
- The small-radius argument: `q(a)` negative with negative derivative on
  `[3.14, 3.28]`, the tail bound (7), `Phi(0) < 1`, hence `Phi'' < -20`
  near zero. The `r >= 1/100` argument via the increasing log-decay
  `lambda(a) = (8a^2-30a+15)/(2a-3)`, `lambda(3.2656) > 3/5`, and
  `lambda(a) >= 2a` for `a >= 8`. All steps hold.
- Counterexample (10): the axis characteristic function of `sigma*sigma*B`
  is `(sin x/x)^2 B^(x)`, `B^(pi) > 0`, and
  `m_t = e^{(t-T)u^2} m_*` has nonnegative inverse for `t <= T`. Correct.
- Note 2 identity (6): expanding `H = 2 pi S/x` at `S = S' = 0` gives
  `H_2 = 2 pi S_2/x`, `H_3 = (2 pi/x)(S_3 - 3S_2/x)`,
  `H_4 = (2 pi/x)(S_4 - 4S_3/x + 12S_2/x^2)`; the cross terms cancel and
  the mirror coefficient `9 + 18 = 27` is right. The product-rule identity
  `A^2 L = 2H_3^2 - 3H_2H_4 - 9H_2^2/x^2` at a collision also checks.
- The Gaussian-mixture determinant: `f(0) = Phi(0)`, `f'(0) = Phi''(0)/2`,
  `f''(0) = Phi''''(0)/12`, and time-independence of `f f'' - f'^2` under
  `f -> e^{tv} f`. Correct.
- Center formula (18): `(r^{-1} d/dr)^k r^{2k} = 2^k k!`, giving
  `(2k-1)!!` in the denominator. Correct. The coefficients 90, 2520, 25200,
  75600, 30240 in (19) are `C(10,2j) (2j)!/j!`. Correct.

Numerical replays (independent code, mpmath at 40 digits, direct
differentiation of the series; not the folder's Decimal certificates):

| Quantity | Folder enclosure | Independent value |
| --- | --- | --- |
| `Phi(0)` | 0.4466969004671234 | 0.446696900467123 |
| `Phi''(0)` | -33.46100154940651 | -33.4610015494065 |
| `Phi''''(0)` | 6497.302667643394 | 6497.30266764339 |
| `Phi^(10)(0)` | 3.358201988404e11 | 3.358201988404e11 |
| determinant (16) | [-38.050, -38.048] | -38.0492425862565 |
| `R_11(0)`, t=0 | (-36403, -36287) | -36289.055 |
| `R_11(0)`, t=0.05 | (-36403, -36287) | -36401.442 |

Both folder scripts rerun with status PASS under Python 3 (standard
library only, deterministic, JSON output, SHA-256 of the checker recorded).
Repository conventions are followed: model attribution, notes/numerics/
reviews layout, `LARGE_FILES.md` referenced, nothing large committed.

## 3. Two facts the folder does not state

**The positivity window is enormous.** Note 1 proves 3D positivity for
`0 <= t <= 1/20` and calls its bounds "deliberately loose". The exact
threshold is `t_* = inf_{r>0} (-Phi'(r))/(2r Phi(r))`. Numerically the
infimum is attained as `r -> 0`, where it equals `-Phi''(0)/(2 Phi(0))`:

    t_* ~ 37.45

(sampled minimum over `r` in `(0, 2]` is 37.4586 at `r = 0.005`, limit
37.4538). So the three-dimensional lift is a positive density for every
Newman time up to about 37, which is two orders of magnitude beyond the
de Bruijn–Newman range `Lambda <= 0.2`. Any property that persists
unchanged across `t in [0, 37]` cannot detect a transition at
`t = Lambda in [0, 0.2]`. This is the quantitative form of the point the
counterexample (10) makes qualitatively: radial positivity is not sensitive
to the collision scale.

**The lift is just positive definiteness of `H_t` on `R^d`.** A radial
density `R_d >= 0` on `R^d` with axis marginal `m_t` exists exactly when
`z -> H_t(|z|)` is a positive-definite function on `R^d` (Bochner; the
inverse is Schwartz so the measure has a density). So:

- dimension 1: `m_t >= 0`, i.e. `H_t` is PD on `R` (classical);
- dimension 3 (Note 1): `H_t(|z|)` is PD on `R^3` for `t < 37.45`, which
  at `t = 0` is just `Phi' < 0` on `(0, infinity)`, a classical fact
  (Csordas–Norfolk–Varga, 1986);
- dimension 11 (Note 2): `H_t(|z|)` is not PD on `R^11`.

Positive-definite functions vanish to even order wherever they like
(`|g^|^2` for any `g`), which is why (10) exists and why no amount of
radial positivity, in any dimension, bears on double zeros.

## 4. Sections 3–4 of Note 2 are one-line consequences of Hardy's theorem

If `m_t(u) = int e^{-a u^2} d nu(a)` with `nu >= 0` (necessarily supported
on `a > t` for convergence), then

    H_t(z) = int (1/2) sqrt(pi/(a-t)) e^{-z^2/(4(a-t))} d nu(a) > 0

for all real `z`. But `H_0 = xi/8` has real zeros (Hardy), and `H_t` has
real zeros for every `t`. So the genuine density is not a positive
Gaussian mixture, for every `t`, with no computation. The determinant
certificate (16) is a correct but roundabout proof of this.

Likewise, Schoenberg's theorem (1938) says a radial function is positive
definite on `R^d` for every `d` exactly when it is a Gaussian mixture. So
"no positive rotation-invariant realization in unlimited dimension" is the
same one-liner. What Note 2 adds is the finite cutoff: dimension 11 fails.
That is a new number, but the folder identifies no use for it.

For completeness, I scanned the odd-dimensional inverses (18) on
`r in (0, 4)` at `t in {0, 0.05, 0.2, 1}` with sympy/mpmath (exploratory,
not certified): dimensions 3, 5, 7 and 9 are positive throughout; dimension
11 is negative at the center. So the "unclassified dimensions 5, 7, 9"
task in the README would most likely return "positive", and the maximal
positive radial dimension is 9. The sign at the center is governed by
`(-1)^k Phi^(2k)(0)`, and the alternation of `Phi^(2k)(0)` breaks between
`k = 4` and `k = 5` (`Phi^(8)(0)` and `Phi^(10)(0)` are both positive).
A curiosity, not a lever.

## 5. On the proposed next task

The README's next bounded task is to control the signed sine moments
`S_2, S_3, S_4` in dimension three with Volterra and cutoff terms paid.
Identity (6) is exact, but it is a change of variables: `S_j` are the
same oscillatory integrals as `H_j` reweighted by `r`, and the sign of
`2S_3^2 - 3S_2S_4 - 27S_2^2/x^2` is the original fourth-jet problem with
the constant 9 replaced by 27. Note 2 states this plainly ("an exact
representation of the signed problem, rather than a new coercivity
theorem"). No theta-specific structure has been introduced that could
supply the sign; the radial geometry contributes nothing the one-dimensional
formulation did not already have, and section 3 shows the geometry cannot
distinguish the collision scale.

The internal reviews are same-model and restate the notes; neither asks
whether the obstructions are trivial, which is the question an external
reviewer would ask first.

## 6. Recommendation

Close program 12. A closure note should record: the PD-on-`R^d`
reframing; the exact threshold `t_* ~ 37.45` and its consequence; the
Hardy/Schoenberg one-liners for Note 2 sections 3–4; the exploratory
positivity in dimensions 5–9 and failure at 11; and the counterexample
(10) as the standing reason the mechanism cannot work. By the
repository's own closure criterion (a branch closes when its findings are
absorbed or superseded, not only when progress stalls), the findings here
are absorbed by the generic positive-kernel obstruction already in the
heat manuscript.

Effort is better spent on the projects that produce new, checkable
content about the genuine object (the rectangle certificates of 13, the
paid dual kernels of 09) or on the single missing input every project in
the portfolio names: a signed constraint incompatible with both collision
equations. A representation-by-lift cannot supply that input unless the
lifted system carries a structure that is destroyed by the generic
controls, and this one does not.

No collision exclusion, threshold result, or RH conclusion is claimed or
refuted here.

## 7. Replay

Independent checks were run with Python 3, mpmath and sympy (not standard
library only; exploratory, not a certificate). The folder's own
`check_radial.py` and `check_radial_center_obstructions.py` both returned
`"status": "PASS"` on rerun from the repository root.
