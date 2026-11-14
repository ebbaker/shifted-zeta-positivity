# B02 decision: a uniform local cover with signed finite tails

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Lead actual model/effort are
unavailable in chat0002's recorded configurations; Astra/ultra is the
author-selected setting. The two analytical helpers were explicitly
tool-selected as **gpt-6.1-sol / ultra**. No independent human review.

**Status: conceptual selection and analytical feasibility; E02 must acquire
the complete canonical bound.** This closes B02's design pass, not the
broader line-reaching program. Read the [result index][results] and
[avoid index][avoid], especially [cluster11][r11], [controls12][r12],
[classification01][a01], [premises02][a02] and [scope07][a07].

## Decision and new quantitative target

Select a continuum of local rectangles at each real center X, with
lambda_X=1/log(X/(4pi)) **frozen within each rectangle**. Keep the exact
canonical H, C_minus and s_lambda from Note03. The next domain is

    |Re z-X| <= 1,       7/12 <= Im z <= 9/8.

The prescribed comparison remains F=H/(C_minus*zeta(s_lambda)).
E02 will prove a uniform error tending to zero, hence eventual
nonvanishing on this entire closed rectangle and |Im z|<7/12 for a
zero at Re z=X at this center's time. The target improves an asymptotic
allowed width near 1 to 7/12; it is not an RH-equivalent criterion.
All claims remain from the inherited internally assessed HDA provider.

## Geometry, observations and their coupling

[Note08](../../notes/08_GNP_BB_B02_GEOMETRY_AND_OBSERVATION_20261113.md)
compares disks, rectangles and strips at fixed observation and target,
then observation choices on fixed domains. Its complete Green and
Cauchy comparisons include vertical edges and full derivative disks.
Choosing the smallest independently supported exterior observation
buffer improves these generic margins; it supplies no arithmetic bound.
The scale-dependent centered-buffer rule keeps a positive Green margin
when all separations shrink proportionally to the allowed width.

Use this concrete all-height tail protocol for the present estimate:
Gamma_X is the boundary of the displayed rectangle and
p_X=X+i(sqrt(1-2/L_X)+1/32). For L_X>=64 it is strictly inside and
above the initial zero enclosure. Uniform estimates on all X>=X_* give
coverage of the entire continuum without a remote-end limit. This is
a family of bounded contours at their individual times, not one global
variable-time Green integral. Every rectangle still pays its four edges.

With a full uniform |F-1|<1, direct nonvanishing already excludes the
whole rectangle. Consequently geometry and observation optimization
cannot improve this particular arithmetic conclusion from the same
uniform error disk. This statement concerns that information class;
signed boundary estimates or nonuniform acquisition could behave
differently. The unbounded graph alternative retains its end estimates
and is not rejected as a universal method.

## The estimating change below 3/4

[Note07](../../notes/07_GNP_BB_B02_FINITE_ARM_COMPARISON_20261113.md)
records the comparison. Split the dominant finite arm at n~exp(L_x/8).
The low part pays heat-weight removal by a convergent logarithmic
moment. Treat the high part as a signed sum with its actual common
logarithmic phase; do not extend the heat-weighted series to infinity.
Use exponent pairs (1/126,20/21) on logarithmic scales [1/8,1/4]
and (1/30,13/15) on [1/4,1/2]. At y=7/12 and c=1, their power
envelopes are respectively

    1/126 - (7/72)v + v^2/4,
    1/30  - (5/24)v + v^2/4.

Their endpoint values are strictly negative. Convexity pays the whole
scale intervals, including their junction. The smallest displayed
margin is 5/16128. Retain time/height drift explicitly; the E02 packet
uses the weaker exponent 1/4096 and a small fixed drift gate. The
reflected arm has its own signed estimate; ordinary zeta tails, the
correction and the provider remainder are still required.

An initially suggested shortcut using a single increasingly deep
A-process pair all the way to the cutoff was rejected during this
design: its heat quadratic can turn positive at the far end. A finite
piecewise envelope, with verified overlap, replaces that unsupported
shortcut. No theorem of arbitrary contraction to y=1/2 follows.

## Iteration assessment and controls

This method supplies a new fixed-depth target, not a recurrence with
widths tending to zero. At c=1, ordinary absolute Euler nonvanishing
requires y>1/2 asymptotically; the selected finite-arm allowance imposes
additional restrictions above it. Moving observations or narrowing
contours does not remove either unpaid arithmetic cost. Any sharper
claim needs a new estimate, checked carrier, and onsets that permit its
claimed iteration. A sequence of separate asymptotic theorems with
onsets escaping to infinity is insufficient at fixed height.

The analytical control screen is Note03 §5, repeated for the changed
premise here. Euler-factor and normalized endpoint controls fail the
unchanged ordinary Dirichlet coefficients; weighted-square/finite-tail
controls fail the complete unit coefficients and completed theta
representation; reflected/smooth/positive-primitive controls fail the
same exact arithmetic; finite-prime controls fail full coefficient and
reflection agreement; atomic/finite-profile controls fail the complete
source/profile; variable-readout controls fail the actual cosine field.
The new exponent-pair payment additionally uses the single actual
logarithmic phase at the physical height, which free-phase relaxations
do not preserve. Generic geometry is not a discriminator. A collision
inside a tested domain would violate |F-1|<1 with a nonzero carrier;
no rejection is required on a disjoint zero-free box.

## Disposition

Issue [E02 r1](../../research-progress/handoffs/GNP-BB-E02-r1.md), type E,
recommended **GPT-6.1 Sol / ultra**, for the fixed complete proof. E01 r1
remains unchanged. The author already authorizes this follow-through.
The proof must return a paid theorem or the exact failed allowance;
changing its domain, clock or carrier requires a recorded B revision.
Compact-height coverage, a common-time global enclosure, a time-zero
passage and a line-reaching iteration remain open.

**Specified follow-through after the same design pass:**
[E03 r1](../../research-progress/handoffs/GNP-BB-E03-r1.md) verifies the
complete A-chain power envelope and transfers the E02 bookkeeping to
each fixed y0>2927/5152. It includes the explicit 4/7 milestone and
the sharply scoped allowance endpoint. This is a finite analytical
execution, recommended Sol/ultra, not an unbounded search for exponent
pairs. E04 supplies an additional-agent arithmetic proof review. No
canonical theorem is accepted merely by issuing either request.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[r11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
