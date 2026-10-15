# Independent internal review of the favorable-curvature split and stationary pilot

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent configuration: **gpt-6-astra (Codex)**, reasoning effort
**ultra**, inherited by this independent reviewing subagent. This is an
internal mathematical and computational audit, not external peer review or
formal verification. The reviewer made no shared repository edits.

## Conclusion and scope

The exact sufficient identity and paired slack in
[Note 21](../notes/21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md) are correct. They permit
favorable signed curvature to pay for a remaining residual square. They
prove a conditional lemma, not a new all-height theta estimate. The direct
one-sided stationary inequality remains the leading target; the new slack
is an auxiliary sufficient condition that may be stronger than necessary.

The stationary pilot is also valid relative to its retained complete-source
certificate. An independent replay passed all eight closed time slabs and
was byte-identical to the producing agent's receipt. It certifies a genuine
stationary branch, a prescribed zero-loss signed estimate on that branch,
and failure of the stated small norm cones under a deliberately changed
centering. It tests the full favorable split `G=C, R=0, rho=0`, not a proper
finite block filter. No height extension or statement near an unknown
collision follows.

## 1. Exact identity and paired source obligation

With `h=h_j`, `s=h_(j+1)`, and the exact split `C=G+R`, direct expansion gives

\[
4\kappa\mathcal L_j+\rho^2E
=(R+2\kappa h)^2+
 \left(4\kappa hG+\rho^2E-R^2\right)
 +4\kappa(\mu-\kappa)h^2+4\kappa s(s+2ah).
\]

Consequently, `0<kappa<=mu` and nonnegative slack on the genuine
stationary set imply `L_j >= -rho^2 E/(4 kappa)`. Local boundedness of
`rho` and a positive local lower bound for `kappa` suffice to make this
loss regular. No division by `E`, `h_j`, or a derivative is involved.
Choosing `kappa=mu` with a fixed positive contour parameter provides the
required lower bound `mu>=a^2`.

For the paired formula, real-product polarization gives `h_j G_j` with
coefficient `1/4` and symmetrized multiplier `m(alpha)+m(beta)`. It gives
`R_j^2` with coefficient `1/2` and multiplier `r(alpha)r(beta)`. Combining
these with `E` gives exactly the coefficient

\[
2\kappa(m(\alpha)+m(\beta))-r(\alpha)r(\beta)
\]

inside the draft's common prefactor `exp(-2ax)/2`. Thus F6 has neither a
sign error nor a missing factor two. Polynomial growth of the prescribed
multipliers is covered by the earlier complete-source moment majorants.
Actual phases, both carrier coordinates, cross terms, and staircase
entries remain necessary. Integrability supplies no sign.

The integrated note correctly warns against the algebraically vacuous choice
`m=y^2-b^2+2 kappa`, for which `R=-2 kappa h`. With `kappa=mu`,
its slack on stationarity is exactly `4 mu L_j+rho^2 E`: the condition
then only restates the target and supplies no source estimate.

The split is meaningfully prescribed only when its source rule and loss
parameters are fixed without using an unknown energy denominator. The
statement that the slack is nonnegative is the new theta-specific proof
obligation. Treating it as automatic, or choosing `rho^2=R^2/E`, would
simply conceal the open problem.

## 2. Structural limitation of a proper block split

At a candidate first-pair zero, `h0=h1=0`, the proposed first slack obeys

\[
\Delta_0=-R_0^2.
\]

Therefore a valid slack certificate there forces **exactly** `R_0=0`.
The original pointwise stationary inequality at that point does not
impose this extra condition. A prescribed finite block filter need not
have this omitted-source cancellation merely because its tail is small.
A fixed absolute tail radius cannot prove the required vanishing.

The same issue applies to the second slack when a candidate zero also
lies on `h2=0`, as in the cubic control. This is a reason to retain the
direct adverse-product estimate as the primary route. Before treating a
proper finite filter as an all-height solution, one must either establish
a suitable source-derived relation such as

\[
R_j=A_jh_0+B_jh_1
\]

with bounded coefficients through the candidate zero, or use an estimate
that directly absorbs the adverse product without requiring such residual
vanishing. This relation itself needs proof from the source; solving for
its coefficients using jet quotients would not help.

No matrix or sum-of-squares argument on arbitrary independent block
amplitudes can bypass theta-specific input. On `h1=0`, the form
`L0+K E=-h0 h2+K h0^2` is indefinite for every finite `K`; the analogous
second form is also indefinite. Multiples of the stationary derivative
vanish on that constraint and do not repair the obstruction.

## 3. Collision controls

The three model calculations were checked directly.

- For the closing real pair, `h0=-D`, `G0=-2`, `R0=mu D`, the slack is
  `8 kappa D+(rho^2-mu^2)D^2`. At `rho=0` it is nonnegative for
  `0<D<=8 kappa/mu^2`, although the magnitude of the whole centered
  residual relative to `sqrt(E)` diverges as `D` tends to zero.
- On the adverse side of a double collision, `h0=2s`, `G0=-2`, and
  `R0=-2mu s` give slack
  `-16 kappa s+4(rho^2-mu^2)s^2`. It is negative for sufficiently
  small positive `s` if `kappa` stays bounded below and `rho` bounded.
  Directly, `L0=-4s` and `E=4s^2`.
- For the cubic predecessor on `h2=0`, `h1=6s`, `G1=-6`, and
  `R1=-6mu s` give slack
  `-144 kappa s+36(rho^2-mu^2)s^2`, with `L1=-36s` and `E=36s^2`.

These controls verify the intended favorable-curvature behavior and
collision sensitivity. They are polynomial heat solutions, not evidence
that a particular theta block filter has the required sign.

## 4. Genuine stationary theta pilot

The reviewer inspected [stationary pilot driver](../numerics/check_stationary_favorable_curvature_pilot.py),
the generating source [input generating source](../numerics/certify_phase_centered_residual.py), and the
[retained complete-source record](../numerics/THETA_CENTERED_RESIDUAL_100_104_20261014.json). The endpoint reconstruction uses the
same heat/space Taylor expansion as the original certificate, now at
signed spatial displacement `-1/2` or `+1/2` and the full closed temporal
interval. It adds both stored spatial and temporal payments without
reducing them. The normalization is the constant
`exp(pi*101.5/8)`, so no derivative of a moving normalization is inserted.
The interval products use exact rational endpoints and can overestimate
but do not underpay the original enclosure.

The eight source cells cover `[101,102] x [0,1/2]`. Their endpoint signs
are strictly opposite, and `h2<0` throughout. Thus, for each time, there
is exactly one genuine zero of `h1` in `(101,102)`; the implicit function
theorem gives a smooth branch. This avoids a vacuous sign claim on an
empty stationary set.

For fixed `a=pi/16`, `b=1/4`, and `mu=a^2+1/16`, the signed stationary
identity uses `C0=-h2-mu h0`. With normalized quantities denoted here by
`Z_k` and `widehat C_j`, every slab certifies

\[
Z_0\widehat C_0>6000,\qquad
\widehat C_0-\mu Z_0>7/5,\qquad
\mu Z_0^2+Z_0\widehat C_0>9400.
\]

This proves the signed target with prescribed `K0=0`, directly from
signed products. The proof does not obtain a loss by dividing by the
record's energy floor. On the same branch, `E=h0^2` and
`widehat C0>mu Z0>0` imply strictly negative two-component cone slack
at `eta=mu` and hence for every `0<=eta<=mu`. The certified normalized
upper bound is below `-78`.

The initial pilot draft used `R_j` for the normalized whole
centered residual; the reviewer requested the notation `widehat C_j`
to avoid confusing it with the new split remainder. The integrated note makes that correction. This pilot corresponds to taking the full multiplier
`m=y^2-b^2`, hence `G=C`, `R=0`, and `rho=0`. It does not test favorable
curvature paying a nonzero proper-filter remainder.

The choice `b=1/4` is a deliberate alternative centering. The pilot does
not disprove the original saddle-centered `eta=1/3` cone, which passed,
and does not reject all larger cone budgets. It stays inside the already
certified domain and does not test regularity at a hypothetical collision.
A bounded loss exists trivially on any compact gap-certified cell; the
useful extra content here is the prescribed zero loss and the directly
certified signed mechanism, not existence of some finite constant.

## 5. Independent replay and identities

The independent command was run against the existing repository inputs,
writing `/private/tmp/inv21-review-stationary-favorable-pilot.json`.
All **eight** slabs passed. The result was byte-identical to
[saved pilot receipt](../numerics/STATIONARY_FAVORABLE_CURVATURE_PILOT_20261014.json).

- Pilot driver SHA-256:
  `f3468f116de57b1f06fb31621f3da3f643f526ffd629f3d4d0f9c2bdb6bc42f9`.
- Input complete-source record SHA-256:
  `aee1f000150a90e1269faa9a8cfafa6251d581ec0f586f0b09d554ef8822741d`.
- Input generating driver SHA-256:
  `6da9b9c05b465a0067809f9e11bb7d7414f51330afe91c2c38e7cb02fc939afb`.
- Input contour source SHA-256:
  `b6f0114e1a4de2e1848f20ab0ab2f1022d9b55015184a879ae0c0536a62d6ad6`.
- Independent replay receipt SHA-256:
  `0518a4b321985d57fe6fb0e08ac81cac3cfa35e98e9f913a889f9b687089f5ff`.

The pilot checks the input generating-driver and contour-source hashes
against those stored in the source certificate, and records the input
certificate hash. The replay inherits the validity of that certificate's
quadrature and analytic tail bounds; it does not rerun their numerical
integration or formally verify those analytic lemmas.

The reviewer also inspected and independently replayed
[split driver](../numerics/check_signed_curvature_split.py): all **14** exact polynomial and model
checks passed, including the joint-zero obstruction and vacuous-split
warning. The result is `/private/tmp/inv21-review-signed-split-checks.json`;
the driver SHA-256 is `91f41e221addb1f7804770ebf049ea7f2373293831c56aea43bd5e2344be9bd7`.
The replay agrees with the [saved split receipt](../numerics/SIGNED_CURVATURE_SPLIT_IDENTITY_CHECKS_20261014.json).
These finite checks do not establish the theta-specific slack inequality.

## Recommended first deliverable

The rigorous deliverable now available is the conditional signed-split
lemma together with the genuine-branch comparison, accompanied by its
residual-vanishing limitation. The next test should select one proper
source filter in advance and report a complete lower enclosure of its
slack on a declared stationary cell, including every tail and cross term.
A failure is informative and should not be repaired by fitting a loss to
the energy floor. To make the step relevant near collisions, develop a
source relation controlling its remainder in the bounded jet ideal, or
return to direct adverse-product absorption.

This route addresses the exact local obstruction left by the collision
criterion. Improving an outer threshold removes more distant cases but
still leaves a shrinking small-time region. The signed route therefore
has greater structural relevance, while its theta-specific all-height
estimate remains unproved.

## Final integration check

The reviewer read the integrated Note 21 and found no substantive regression.
The direct product estimates in Section 8 and the sufficient bound from a
bounded-coefficient jet-ideal source identity are correct. Two clarifications
were reported for integration: the second residual-vanishing statement applies
when the candidate joint zero also has `h2=0`; the separate product-loss
coefficients must remain locally bounded through the candidate collision.
The note clearly separates the proved auxiliary lemma, the existing-domain
full-residual pilot, and the unproved proper-filter/all-height obligation.
