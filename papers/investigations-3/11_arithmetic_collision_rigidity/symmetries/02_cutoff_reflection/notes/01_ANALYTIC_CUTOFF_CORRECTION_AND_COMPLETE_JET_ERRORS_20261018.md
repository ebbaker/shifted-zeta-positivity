# S02 opening comparison: analytic cutoff correction and complete jet errors

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the parent turn metadata. Parallel same-model
algebra and budget audits; no independent specialist review.

**Result: the declared bounded complete-error gate passes.** On
`[1/100,1/5] x [999,1001]`, the current absolute-correction disk allowance
decreases from `0.887748` to `0.226300`; on the separate cutoff-crossing
test `[1/100,1/5] x [1017,1019]`, it decreases from `2.897966` to `0.431778`.
The strict comparisons cover the complete analytic residual and its
derivatives through order two, in the same normalization and radius.
These are error envelopes for exact analytic approximants, not complete
evaluated jet enclosures, pointwise comparisons of actual errors, or new
collision-exclusion regions. The error bounds are proved below using the
published approximation theorem and checked with outward interval arithmetic.

## Contract and reconciliation with prior work

The [program guide][guide] selects S02 as the first quantitative experiment.
The repository [result summaries][summaries] and [avoid index][avoid] were
read, especially [the existing corrected interface][heat-summary],
[collision controls][controls], [target reformulations][target],
[scoped conclusions][scope], [normalization][normalization-warning], and
[preserving signed cancellation][pairing]. A global first-jet nonvanishing
criterion is an RH-equivalent reformulation; this note instead measures
a bounded approximation error. No such global criterion is proved here.

The [earlier collision manuscript][earlier], `sc:vector`, retains amplitude
drift and signed cross terms; `prop:absmass` excludes a small absolute
terminal tail in its stated scaling regime; `sc:packet` excludes diagonal
coercivity for the specified adjacent packets; `lem:phase` is a conditional
error-paid consumer. None supplies a many-term signed lower bound here.

Two particularly relevant prior sources are [transport Note 20][old20]
and [transport Note 22][old22]. **They already derive the full multiplier
simplification, the nonholomorphy warning, a paid holomorphic exponential
surrogate, and the exact cutoff-jump identity.** Note 22 also proves a
uniform complex matching bound for an entering term. Those are prior
results, not discoveries of this round. [Polymath Corollary 6.4](https://arxiv.org/html/1904.12438v2#S6.SS3)
already supplies the improved value approximation. This execution implements a different
holomorphic choice, the full analytic continuation of the real correction,
and evaluates a complete, uniform time-slab error ledger at the guide's
height-1000 pilot and a specified crossing. It does not claim to outperform
the best implementation of Notes 20–22, whose frozen exponential and
correlated physical-error representation remain available for comparison.

The primary objective is a strict decrease of the uniform complete error
for `Q`, `Q_x`, and `Q_xx` against the current [exterior contract][outer].
The secondary matched baseline uses the same unreduced multiplier bound
as the candidate, so a saving caused only by sharpening an old multiplier
is separately visible. No timing, new coverage, or exterior-onset objective
was selected. All eight modes are retained, including neighbors 7 and 8;
mode 9 is handled as one signed transition on the crossing box.

## Fixed-cutoff analytic formula

Use exactly the principal-logarithm definitions of `m_0`, `alpha`, `m_t`,
`M_t`, `w_{t,n}`, `G_{t,N}`, and `A_t` in [the exterior section][outer].
In particular, `s=(1-iz)/2`,

\[
G_N=M_t(s)\sum_{n\le N}w_{t,n}(s)
    +M_t(1-s)\sum_{n\le N}w_{t,n}(1-s),\qquad
\mathcal A_t=\exp\{(m_t(s)+m_t(1-s))/2\}.
\]

This is the symmetric normalizer, not the positive arithmetic carrier or
the reference evaluator's fixed `G0(1000)`. The published upper and lower
channels correspond to `1-s` and `s`; their apparent conjugations rewrite
to these holomorphic terms. All coefficients are the unchanged theta data.

Put, for real t and complex z near either test box,

\[
v=z/2+\pi t/8,\quad a=\sqrt{v/(2\pi)},\quad p_N=2N+1-2a,
\quad \phi(p)=\pi(p^2/2+3/8),
\]
\[
D(p)=\frac{\cos\phi(p)}{2\cos\pi p},\qquad
I(p)=\frac{\sin\phi(p)-\sqrt2\cos(\pi p/2)}{2\cos\pi p}.
\]

On real p, `C_0(p)=D(p)+i I(p)`. Both functions are even. At the local
removable points their values are `D=1/4`, `I=-1/4`; at `p=1/2`,
`D'=1/4`, `I'=0`, with opposite derivatives at `p=-1/2`. This follows by
dividing the numerator and denominator Taylor series after their common
simple zero. The checker repeats that division with balls. No test-domain
cell contains a denominator zero; the local check does not purport to
certify a whole removable-point neighborhood by floating subtraction.

Substitution into the prescribed Stirling factor gives the exact prior
identity

\[
M_0(iv)U(v)e^{\pi i/8}
=-\frac{\sqrt\pi}{8}\sqrt v(v+i)e^{-\pi v/4}.
\]

Consequently define

\[
J_N(t,z)=\sqrt v\{vD(p_N)-I(p_N)\},\qquad
\widehat C_N=(-1)^{N+1}\frac{\sqrt\pi}{4}
e^{-\pi z/8-\pi^2t/64}J_N(t,z),\qquad
\widehat F_N=\frac{G_N-\widehat C_N}{\mathcal A_t}.
\tag{1}
\]

All square roots have positive real part on the enclosing rectangles.
The finite sums, (1), and their normalized residual are holomorphic on a
neighborhood of every disk and have real symmetry. `H` is the entire
complete source transform; no finite source is asserted to have theta
reflection. This also justifies all differentiations of the fixed formula.

## Paying the complex continuation

Corollary 6.4's displayed correction is
`C_pub,m(t,x+iy)=exp(-pi i y/8) C_m(t,x)`, where m is the natural real
cutoff. It is generally nonholomorphic. Its real slow profile is evaluated
at x, whereas (1) evaluates that profile at z. We pay the difference before
applying Cauchy; no extension of the published theorem beyond its stated
`0<=y<=1`, `x>=200` domain is needed.

The exact slow derivative is

\[
J_N'=\frac34\sqrt vD-\frac{I}{4\sqrt v}
-\frac{vD'-I'}{2\sqrt{2\pi}}.
\tag{2}
\]

If `M_J` bounds (2) on the enclosing upper rectangle, integration along
the vertical segment gives

\[
\frac{|\widehat C_m-C^{\rm pub}_m|}{|\mathcal A_t(z)|}
\le K_* W_* R M_J.
\tag{3}
\]

Here `K_*` is the exterior contract's normalizer ratio bound and `W_*`
bounds the following **exact** real-axis ratio:

\[
W(t,x):=\frac{(\sqrt\pi/4)e^{-\pi x/8-\pi^2t/64}}{\mathcal A_t(x)}
=8\pi^{1/4}(1+x^2)^{-7/8}
\exp\!\left\{\frac14-\frac{x}{4}\arctan(1/x)
-t\left[\frac{\pi^2}{64}+\frac{\alpha_r^2-\alpha_i^2}{4}\right]\right\},
\tag{4}
\]
\[
\alpha_r=\tfrac14\log(1+x^2)-\tfrac12\log(4\pi)-(1+x^2)^{-1},
\quad \alpha_i=\tfrac12\arctan x-3x/(1+x^2).
\]

The sign of `alpha_i` is irrelevant to its square; the code otherwise
keeps the original lower-half-plane `alpha(s)`. The factor `pi^(1/4)` in
(4) is essential. An opening internal calculation omitted it; both retained
records were regenerated after correction. A direct interval comparison
with `A_t` checks (4), independently of its simplified evaluation.

Let `x_-`, `x_+` be the enclosing real endpoints, `q_-=x_-/(4pi)`,
`epsilon=1/100`, `tau=1/5`, and let `v_+ = x_+/2+pi tau/8`. The uniform
published correction amplitude and relative error are bounded by

\[
P_* =\frac{K_*W_*}{2}\sqrt{v_+}\sqrt{v_+^2+1},
\]
\[
T_* =\left\{
\frac{0.397[9^{(1+R)/2}+9^{(1-R)/2}]}
 {\sqrt{q_-+\epsilon/16}-0.865}
+\frac{10}{3(x_-/2-6)}\right\}
e^{3.49/(x_-/2-4)}.
\tag{5}
\]

The sum in (5) retains both reflected sigma values; it is maximized at
`|y|=R`. Corollary 6.4 pays `P_* T_*` instead of `P_*(1+T_*)`.
Its complete two-sum error remains the same `K_* max_m E_m^{AB}` as the
current exterior contract. These imported errors include the discarded
arithmetic/contour contributions; this implementation introduces no new
source truncation or quadrature. Interval rounding is included in every
scalar/profile/transition enclosure. No residual component is discarded.

## Signed cutoff transition

The prior exact identity from [Note 22][old22] is

\[
C_0(p)+C_0(p+2)=e^{i\pi((p+1)^2/2-1/8)}.
\]

By analytic continuation it gives

\[
\widehat C_{N+1}-\widehat C_N
=(-1)^N\frac{\sqrt\pi}{4}e^{-\pi z/8-\pi^2t/64}\sqrt v
\{v\cos\psi-\sin\psi\},\quad
\psi=\pi((p_N+1)^2/2-1/8).
\tag{6}
\]

Write `g_9=G_9-G_8`. For frozen `N=8`, natural `m=9`, the exact residual
decomposition is

\[
Q-\widehat F_8=r^{\rm pub}_9
+\frac{\widehat C_9-C^{\rm pub}_9}{\mathcal A_t}
+\frac{g_9-(\widehat C_9-\widehat C_8)}{\mathcal A_t}.
\tag{7}
\]

The last expression is enclosed as one signed analytic difference using
(6); its two magnitudes are never added separately. For natural `m=8`
this term is absent. On the crossing test `psi=2pi(a-9)^2-pi/8`.
This implementation uses direct interval evaluation of the difference,
not Note 22's sharper analytic edge estimate. Its `0.206301` transition
payment is substantially wider than the actual edge defect; improving it
is a separate, bounded follow-up, not a reason to expand this scan.

## Closed coverage and numerical ledger

Every real center X in each of the two boxes is assigned radius `R=1/2`.
The union of its upper disks is contained in the listed closed rectangle.
Closed rational subdivisions cover the entire rectangle and time slab:

| Real centers | Enclosing x range | Natural cutoffs | t/x/y grid | Cells |
| --- | --- | --- | --- | --- |
| `[999,1001]` | `[1997/2,2003/2]` | 8 | 4 / 24 / 8 | 768 |
| `[1017,1019]` | `[2033/2,2039/2]` | 8, 9 | 8 / 64 / 16 | 8192 |

Both use `0<=y<=1/2`. Endpoint evaluation proves the cutoff lists. The
entire crossing curve `x=4pi(81-t/16)` lies inside `(1017,1019)` for the
whole time slab (approximately `1017.7189`–`1017.8682`). Integer cutoff
8 stays fixed in the analytic candidate. Natural-cutoff membership only
selects which valid pointwise source bound enters (7).

The [192-bit record][r192] and [256-bit record][r256] have the same source
hash. Both use python-flint 0.9.0 and outward Arb/Acb arithmetic. Maxima
are taken on outward upper endpoints; no selection among overlapping
balls is treated as an enclosure of their maximum. Neither grid nor
precision was enlarged to obtain a pass.

| Uniform disk error contribution | Height-1000 test | Crossing test |
| --- | ---: | ---: |
| Common two-sum error | 0.014171 | 0.015416 |
| Corrected published residual | 0.209083 | 0.206434 |
| Holomorphic-continuation mismatch | 0.003046 | 0.003628 |
| Signed cutoff transfer | 0 | 0.206301 |
| Candidate total eta | **<0.226300** | **<0.431778** |
| Current absolute baseline eta | >0.887747 | >2.897965 |
| Matched absolute baseline eta | >0.819028 | >2.862537 |

The displayed component decimals are descriptive; the records supply
their outward enclosures. The candidate/current ratios are below
`0.254915` and `0.148995`; the matched ratios are also strictly below one.

Because `Q-Fhat_8` is holomorphic with real symmetry, the rectangle bounds
reflect to every full disk. Cauchy at its real center proves

\[
|\partial_x^j(Q-\widehat F_8)|\le j!2^j\eta\qquad(j=0,1,2).
\tag{8}
\]

Thus the new error triples are respectively below
`(0.226300,0.452600,1.810400)` and
`(0.431778,0.863556,3.454224)`, uniformly on the real boxes. The
phase-scaled first-jet errors and the physical return factors are also
recorded, using the same nonzero lower bound for `|theta_x|` in both methods.

For the physical approximation `Hhat=G_8-Chat_8`, with
`b=partial_x log A`, `|b|<=B=L_*/2`, and `|b_x|<=B_1`, (8) yields

\[
\frac{|H-Hhat|}{A}\le\eta,\quad
\frac{|H_x-Hhat_x|}{A}\le(2+B)\eta,\quad
\frac{|H_{xx}-Hhat_{xx}|}{A}\le(8+4B+B^2+B_1)\eta,
\]
\[
B_1=\tfrac14\{D_*(1+\tau D_*/2)+\tfrac\tau2 A_*
 [3/V^3+1/(2V^2)]\}.
\]

These factors are common to the two methods. No comparison silently
identifies normalized derivatives with physical derivatives.

## Reference evaluation, cost, and controls

A fresh run of the existing complete-source evaluator regenerated its
midpoint quadratures at 192 bits and passed its prior 40-cell signed
pilot and 7-cell complex wall. Its setup code and twelve-file manuscript
source pins were validated before consuming its exact dyadic midpoint and
tail cache. The bulky reference setup stays external; regeneration
commands and its hash are retained in the small record. This is validation
of the existing coverage, not coverage attributable to the new approximation.

At `t=21/200`, `x=1000`, conversion from the fixed `G0(1000)` normalization
gives `Q` about `-1.11924655`, `Q_x` about `2.46523052`. The candidate's
actual enclosed residuals at that point are about `-0.00080221`,
`-0.00014342`, `0.00095734` at orders 0–2. They lie well inside (8).
Point agreement does not prove whole-box accuracy; (3)–(8) do that.

The records include matched 256-evaluation timings for exact analytic
jets through order two at this single center, identical precision and
cutoff, without caching. At 192 bits the two totals were approximately
0.24 and 0.26 seconds in the first measured run. Timings are descriptive
and vary; the candidate adds work. The complete error-envelope construction
uses 8,960 interval cells and about a second of profile/transition work.
The fresh reference setup took about 8.8 seconds and is disclosed
separately. No factor-two performance claim is made, and the correction
is not competitive with the reference evaluator's much tighter errors
on accuracy alone.

The [fresh control replay][control-record] rejects all five supplied
event boxes with source-specific first-jet and signed-margin errors, and
rejects the separate Euler negative-Laguerre witness. Those are unchanged
consumer-interface checks, not tests of the new theta error theorem.
This checker does not accept an arbitrary source or assign theta error
constants to a control. The substantive missing premises are:

- Finite-prime orbit and finite square controls: the full normalized
  theta reflection/coefficient data; finite-prime event heights are not effective.
- Reflected super-Gaussian, smooth shape and positive-primitive controls:
  the unchanged normalized integer-square theta series. Their reflection
  and auxiliary positivity alone do not supply Corollary 6.4's constants.
- Euler-factor controls: the unchanged level-one coefficient data; their
  negative-Laguerre witness is not a double-event box.
- Counter-kernels and polynomial events: the exact theta source and its
  evaluated signed approximation. Generic heat and jet identities survive.
- Smooth-density/two-channel realizations: a comparison with the complete
  signed physical theta observation.

This follows [the control summary][controls]. No event is placed on either
test box by assumption, and no artificial rejection there is demanded.

## Decision and handoff

The primary gate passes against both declared absolute baselines, including
the full complex continuation, cutoff, normalization and derivative costs.
The result is an internally checked bounded implementation of known
correction machinery with a full analytic continuation. It does not show
that evenness by itself improves a signed bound, or improve on the best
prior rank-one/correlated implementation. Preserve that distinction.

S03 may consume (1), its exact analytic derivatives, and (8) on the stated
boxes; any rotation-defect or Laguerre claim must additionally evaluate
the signed finite expressions and pay its own propagation. The next useful
bounded decision is a matched comparison with Notes 20–22's frozen
exponential and analytic edge bound, before increasing height or scanning
more cells. The original real bridge `(1001,exp(2000))` and missing global
complex exterior remain open. The manuscript is unchanged.

[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[outer]: ../../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[old20]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md
[old22]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[heat-summary]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[normalization-warning]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[pairing]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[r192]: ../numerics/S02_CUTOFF_REFLECTION_192_20261018.json
[r256]: ../numerics/S02_CUTOFF_REFLECTION_256_20261018.json
[control-record]: ../numerics/S02_CONTROLS_20261018.json
