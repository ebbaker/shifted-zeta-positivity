# Manuscript integration and cross-time continuation

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra**, reasoning effort **ultra**. The manuscript
retains the author field **Drafted for Edward Baker** and an explicit LLM
acknowledgment. This is an internal research handoff, not external peer
review or formal verification.

## 1. Current deliverable and provenance

The stable [manuscript source](../manuscript/quaternion_theta_geometry.tex)
and [PDF](../../../../../output/pdf/quaternion_theta_geometry.pdf) now
integrate Notes 19–22 into the main exposition. The title remains
**Uniform Laguerre signs and hypercomplex jets of the theta heat flow**.
The [build record](../manuscript/BUILD_RECORD.json) binds the final source,
PDF, page count, validation receipt, and review by hashes. The
[integration review](../reviews/17_MANUSCRIPT_CONTINUATION_INTEGRATION_REVIEW_20261014.md)
records the mathematical and visual audit.

This revision continues commit `560684890d84ab2287ae6ddcd69d763a21f8c0f2`.
The previous 24-page manuscript can be recovered from that commit.
The explicitly requested historical 35-page individual-file backups and
[backup receipt](../manuscript/BACKUP_RECORD_20261014.json) remain intact.
No new snapshot folder, commit, or tag was created for this integration.
The older notes' statements that their results had not yet been integrated
are historical; this note records the completed integration.

## 2. What is now in the manuscript

| Research record | Integrated mathematical content |
| --- | --- |
| [Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md) | Uniform threshold-three outer proof, maximal logarithmic-phase blocks, staircase entry terms, exact paired Laguerre/residual integrals, and complete omitted-pair payments. |
| [Note 20](20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md) | Separate threshold-five explicit height, all imported approximation errors, disc/amplitude comparison, four derivative budgets, and final strict sign margins. |
| [Note 21](21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md) | Favorable-curvature split, exact slack and stationary-ideal identities, collision limitation of the squared residual condition, controls, and the eight-slab full-theta example. |
| [Note 22](22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md) | Direct signed absorption criterion, prescribed proper source filters on both genuine stationary branches, sharp-endpoint and rational-jet closure obstructions, complete-source Gaussian comparison, finite certificate, and the remaining cross-time target. |

The introduction, main theorem, collision consequence, remaining-domain
statement, reproduction appendix, and acknowledgment were revised
consistently. The original collision reduction, quaternionic/octonionic
constructions, complete-source payments, and bounded certificate remain
part of the unified argument. Equations are given with their proofs and
hypotheses; the integration does not merely point to the notes.

### Outer signs and the separate explicit height

For every fixed epsilon > 0, the two full Laguerre forms are strictly
positive for sufficiently large |x|, uniformly on

\[
0<t\le\tfrac12,\qquad t\log\frac{|x|}{4\pi}\ge3+\varepsilon.
\]

The proof preserves the maximal exponential-sum estimate for every
shortened arithmetic block, splits the weighted sum at exp(L/3), controls
the growing-time factor uniformly, retains all three imported Polymath
errors, and differentiates only after passing to an analytic comparison
on shrinking discs. A common nonzero zeta amplitude controls all four
physical derivatives. A hypothetical sequence of positive-time collisions
with unbounded heights therefore has limsup t log(|x|/(4 pi)) <= 3.
There is no assertion at epsilon = 0 and no evaluated cutoff for this
sharper theorem.

The distinct explicit statement is

\[
|x|\ge X_{\rm exp}:=4\pi\exp(10^9),\quad
0<t\le\tfrac12,\quad t\log\frac{|x|}{4\pi}\ge5.
\]

Every normalized jet error is at most 108000000/L <= 0.108 < 1/8.
The normalized balanced first-jet norm is at least 1/2, and each normalized
Laguerre form is at least 31/64. The manuscript uses **X_exp**, rather
than Note 20's former X_1, to avoid confusing this threshold-five cutoff
with epsilon = 1 in the improved threshold-three theorem. This enormous
height supplies no practical bridge from 104.

### Exact source structure and signed estimates

The staircase recurrence includes every entering-index delta term. The
entry phases cancel in x, so these terms cannot be assigned an artificial
oscillatory gain. Paired identities retain independent arithmetic indices
and independent integration coordinates. Their Hermitian and bilinear
parts both contribute; square frequency factors alone do not imply a
positive product. The omitted-pair bound includes retained–omitted,
omitted–retained, and omitted–omitted pairs, using complete source tails.

For frozen a,b and mu = a²+b², the centered residual is

\[
C_j=-h_{j+2}-2ah_{j+1}-\mu h_j,\qquad j\ge0.
\]

On the genuine current stationary set h_(j+1) = 0,

\[
\mathcal L_j=\mu h_j^2+h_jC_j.
\]

The auxiliary favorable-curvature slack identity is sufficient, but its
squared-residual condition forces residual vanishing at a joint zero.
The more flexible objective therefore uses a prescribed split C_j = G_j+R_j
and retains the signs of

\[
h_jG_j\ge0,\qquad h_j(R_j+\lambda G_j)\ge-K_jE,
\quad 0\le\lambda\le1,\quad E=h_0^2+h_1^2.
\]

These inequalities imply L_j >= -K_j E without dividing by unknown E.
A loss must be locally bounded through each candidate positive-time
collision. An estimate valid only after defining K from an energy quotient
does not meet that requirement.

### What the finite pilots establish

All pilots lie within the already certified height-104 region. They test
mechanisms; they add no height coverage.

- The full-residual comparison uses eight closed time slabs on the unique
  h_1 = 0 branch in 101 < x < 102. It certifies zero-loss favorable
  curvature with a different centering where specified stricter residual
  cones fail. The previously successful natural cone is not contradicted.
- The proper sharp filters use N = 1 or 2, U = 1 or 3/2, a = pi/16,
  b = 1/4, lambda = 1/2, and K = 0. Eight closed time slabs cover
  0 <= t <= 1/2; even slabs are development cells and odd slabs are
  held out. Both current stationary branches are genuine, unique, and
  paid: h_1 = 0 in 101 < x < 102 and h_2 = 0 in 103 < x < 104.
  The N = 1 absorption test fails in all 32 cases, while N = 2 passes
  in all 32 cases despite an adverse complement. Failure of the N = 1
  split is not a negative full Laguerre form.
- The full-source complex Gaussian mask exp(-delta z²), with
  delta = 1/16, gives G_j = C_j(t-delta,x). On the two current
  stationary branches and the seven time slabs in delta <= t <= 1/2,
  all 14 cases have positive retained, complementary, and absorption
  products. Earlier-time stationarity is not assumed. This is not an
  all-height or small-time certificate.

The sharp-filter theorems explain why this finite success does not by
itself give a global mechanism. A nonzero fixed upper endpoint produces
algebraic Fourier decay; along suitable true stationary sequences at fixed
positive time its separate payment relative to the full physical energy
is exponentially adverse. This excludes uniform or subexponential
separate budgets for those fixed sharp filters. It does not exclude the
original locally bounded-loss objective: a loss may grow exponentially
with height and still be locally bounded at every finite point. The
obstruction is proved in an already favorable outer region, not as a new
cusp theorem.

A second theorem rules out exact finite rational-in-x jet closure of a
nonzero compact source filter, even if initially asserted only on a
pole-free interval. Clearing denominators and Fourier inversion would
make a real-analytic full-source density compactly supported. This does
not rule out general transcendental coefficients, moving filters, or
noncompact filters. Finite evenization also fails at positive time because
its wrong-end Gaussian-weighted density is not integrable.

## 3. Next objective: a theta-specific cross-time stationary comparison

The next analytic objective is to establish a usable signed comparison for
the complete-source Gaussian filter on both **current** stationary sets.
Choose the delay and lambda before inspecting signs. With a,b frozen,
set

\[
\begin{aligned}
P_j^\delta(t,x)&=h_j(t,x)C_j(t-\delta,x),\\
Q_j^\delta(t,x)&=h_j(t,x)
 [C_j(t,x)-(1-\lambda)C_j(t-\delta,x)].
\end{aligned}
\]

The target is P_j^delta >= 0 and Q_j^delta >= -K_j E when
h_(j+1)(t,x) = 0, for j = 0,1, with losses locally bounded through
candidate positive-time collisions. The exact complementary formula is

\[
R_j(t,x)=C_j(t,x)-C_j(t-\delta,x)
       =-\int_0^\delta C_{j+2}(t-s,x)\,ds.
\]

This identifies the missing cross-time product. The heat equation and
source symmetry do not determine its sign. In particular, stationarity
at (t,x) cannot be imposed at (t-s,x).

A productive next step is a declared delay rule that remains meaningful
as t decreases, followed by a signed integral decomposition of Q retaining
the full source and all cross terms. A rule such as delta = rho t,
0 < rho < 1, is a **candidate for investigation**, not an established
choice or a consequence of the fixed-delay pilot. Moving a,b,delta require
their derivative terms in any transport argument. Pointwise identities
with frozen parameters do not authorize dropping those derivatives.

The separate real horizontal mask exp(-delta u²) has the exact identity

\[
G_j=e^{a^2\delta}C_j(t-\delta,x+2a\delta),
\]

and complement

\[
R_j=-\int_0^\delta e^{a^2s}
 (C_{j+2}+2aC_{j+1}+a^2C_j)(t-s,x+2as)\,ds.
\]

It is not the mask used in the 14-case certificate. The real-multiplier
paired slack identity applies to this real mask, whereas the tested
complex mask requires the physical-field identity or polarization with
the correct conjugation. A comparison between the two rules should keep
that distinction explicit.

A concrete next deliverable should contain: one predetermined delay rule;
an exact signed cross-time representation on both current stationary
sets; all source, contour, and parameter payments; and either a
locally bounded loss theorem on a declared new domain or a precise
obstruction/counterexample to that rule. A bounded pilot can guide that
choice, but a new finite success should be labeled with its actual domain.
The paired arithmetic blocks from Note 19 can support this work by
preserving correlation and paying tails. Absolute component bounds alone
do not decide the missing product.

The independent quantitative route remains useful: improve the explicit
outer height or close part of the finite strip above 104. Neither task
substitutes for controlling the moving small-time region.

## 4. Validation and reproduction

The [new compact audit](../numerics/MANUSCRIPT_CONTINUATION_CHECKS_20261014.json)
records 100 fresh exact checks: 34 paired/staircase/block algebra checks,
52 explicit constant inequalities, and 14 signed-split/control checks.
Each fresh record is byte-identical to its saved counterpart. The current
8-slab, 64-case, and 14-case records are hash-identical to their earlier
independently replayed versions. This integration did not repeat the
interval quadrature or extend the certificates. Reviews
[14](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md),
[15](../reviews/15_ONE_SIDED_STATIONARY_ESTIMATES_REVIEW_20261014.md), and
[16](../reviews/16_SOURCE_FILTERS_AND_THETA_CORRELATIONS_REVIEW_20261014.md)
retain the earlier proof and replay details.

From this investigation's `numerics/` directory, the exact checks are:

```sh
python3 check_signed_carrier_pair_identities.py --output /tmp/inv21-pairs.json
python3 check_explicit_outer_constants.py --output /tmp/inv21-constants.json
python3 check_signed_curvature_split.py --output /tmp/inv21-split.json
```

The two source-filter replays, with python-flint 0.9.0 for the first, are:

```sh
python3 certify_predetermined_source_filter_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --original-driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-proper-filter-replay.json
python3 check_gaussian_source_filter_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --original-driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-gaussian-filter-replay.json
```

The saved source is checked with the desktop LaTeX compiler. The canonical
PDF is exported with pdfTeX, with build auxiliaries outside the repository.
Final page count, compilation diagnostics, visual inspection, and exact
hashes are in the build record and Review 17. All newly saved permanent
files remain below the repository's 1 MiB limit.

## 5. Chat-history identity and closeout

This conversation remains uniquely registered as **number 9** in the
formal replay lane, following the author's explicit standing instruction:

- Thread: `01a13cd2-1633-7f50-a8bb-d62373ca4e24`.
- Archive: [0009_2026-10-14T23-49-23Z_continue-quaternion-theta-rewrite.json](../../../formal_replay_crosswalk/chat-histories/0009_2026-10-14T23-49-23Z_continue-quaternion-theta-rewrite.json).
- Registry: [index.json](../../../formal_replay_crosswalk/chat-histories/index.json).
- Current integration turn: `01a13cf8-422c-7f43-8ffe-9807f534ebf6`.
- Point-in-time verification: [history verification receipt](../reviews/CHAT_HISTORY_INTEGRATION_VERIFICATION_20261014.json).

The start-of-turn check confirmed the preceding final reply was captured.
Closeout refreshes and compares all completed public messages with the
source transcript and checks archive bytes, canonical-content hash, and
unique registration through the repository helper. This preserves the
existing number, filename, original creation time, first-capture provenance,
and earlier messages. Public commentary is included; tool traffic,
subagent correspondence, and private reasoning are excluded by policy.
Research files are saved in the repository and linked from this public
record; they are not embedded wholesale in the chat archive.

A normal in-turn verification cannot contain an unsent closing reply.
The required final action therefore starts the bounded worker for this
exact turn, which captures the actual final text after completion. The
receipt explicitly identifies its earlier verification snapshot, so later
legitimate refreshes may change the archive's count and hash. Native-hook
activation has not been verified; the explicit refresh and exact-turn
follow-up workflow remains in use. On the next turn, check that worker's
result and refresh before beginning new research.
