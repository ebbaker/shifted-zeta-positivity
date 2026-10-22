# Endpoint-window, signed-response and many-root internal review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual root-turn configuration, verified from
session metadata: **gpt-6-astra (Codex), reasoning effort ultra**.
The three notes were developed by delegated agents of the same model
configuration. The root assistant checked all three; the signed-response
agent separately checked Note 07 and the exact-control script, and the
window-analysis agent separately checked Notes 08 and 09. These are
**same-model internal reviews**, not independent specialist validation.
No novelty or RH-conditional simplicity claim is made.

**Assessment: the stated local theorems and scoped counterexamples pass
this internal review. ECE-01 is complete in its parameterized exact-double
scope; the unchanged-theta signed estimate and endpoint exclusion remain
open.** This review concerns the working-tree additions based on repository
HEAD `5da7681`, not an immutable reviewed release. Earlier uncommitted
research files and unrelated changes were preserved.

## 1. Window geometry and height quantifiers

[Note 07][n07] pays the contract rather than defining an unproved wall
minimum. At an assumed exact double, q=|H_zz(0,a)|/2 is positive by
nondegeneracy, while H=H_z=0 at the center. It is not a joint-jet floor.
The complete moments B_2,B_3 bound derivatives on all required complex
segments. The rectangle corners cost sqrt(2)h, explicitly included in
the time restriction.

The spatial Taylor error is at most q s^2/6; the temporal error is at
most q r^2/4. Thus both circles have floor at least 7q s^2/12, with
the stronger 37qR^2/48 on the outer circle. Two separate Rouché counts
give exactly two roots inside each circle and exclude extra collar
roots. The derivative calculation gives
(5/2+sqrt(2)/128)qR<3qR. Substitution yields exactly 96/R^2, and
the phase product is at most 3/4<pi/2. All boundary extensions have
strict slack. No exterior roots are dropped.

The cap estimates have the correct signs. When Delta(0)=0, the complete
integrating-factor solution is negative before zero and positive after
zero, with the displayed nonzero exponential margins. The resulting
charge is one. Obtaining zero from these same hypotheses would be an
error. The off-event finite-jet test supplies a sufficient geometric
contract, without assuming an event or a positive gap.

The height statement is pointwise and universal over finite real a:
fixed complete B_j and the actual q(a)>0 produce a positive window at
every hypothetical exact double. Integration by parts gives
q(a)<=||(u^2 Phi)'||_1/(2|a|), so the selected radii and widths can
shrink. This is a bound on this conservative prescription, not a necessary
window scale or a proof that another construction cannot be uniform.
Neither compactness over finitely many zeros nor the displayed formula
proves an all-height source sign. The scalar event-time enclosure assumes
event existence; it is not allowed to manufacture an event from a cap
value alone.

Two wording issues found in the separate pass were corrected before
installation: roots are **inside** each circle, and the polynomial
control uses a positive third-derivative majorant instead of dividing
literally by zero in q/B_3.

## 2. Signed source response and its nonlinear payment

[Note 08][n08] uses log(1+E/F) only on a boundary annulus where the
strict ratio q<1 gives its single-valued series. Interior reference zeros
are allowed. Integration by parts gives delta S_1=-I[ell] and
delta S_2=-2I[(z-a)ell]. Expanding 2S_2-S_1^2 then yields
the exact term -4I[(z-c)ell] **minus** (I[ell])^2. This last term
cannot be discarded. Its linear part and the complete logarithmic tail
give exactly 4R(R+r)l_2(q)+R^2 l_1(q)^2, with no internal-gap
denominator. The smaller target collar is explicitly a separate payment.

The source-contour interchange is justified by the stated complete
residual majorant and wall floor. At a double, the residue is
-8E/F_zz. This is an oscillatory source measurement, not signed merely
by positivity of the source. The finite enclosure is useful only after
the complete signed integral and its errors have been established.

The event Jacobian in (t,z) has determinant -H_zz^2. Differentiating
with the backward heat sign gives tau'=E/H_zz and
b'=(H_zzz tau'-E_z)/H_zz. The second derivative simplifies to
(H_zzzz/H_zz)(tau')^2-2(E_zz/H_zz)tau'-(b')^2.
The negative last term is valid because the branch is real.

The additional whole-homotopy payment is sound: uniform proper two-root
geometry, phase, and opposite cap signs give a unique real ordinary
event for every homotopy parameter. Uniform strict boundaries prevent
escape, so local implicit branches patch over the closed parameter
interval. Also U=H/P is zero-free; the maximum-modulus theorem applied
to 1/U transfers |U|>=delta/(R+r)^2 from the spatial wall to the
interior. Therefore the event curvature has the paid floor
2delta/(R+r)^2. This does not assume a nonzero joint jet at the event.
Complete source-jet majorants pay the remaining terms, but no concrete
theta homotopy or negative event-time margin is supplied.

The quadratic affine control has Delta=8t+s^2 b^2-4sc and
tau=sc/2-s^2b^2/8. It checks both the nonlinear centroid correction
and the event acceleration. The displayed boundary-paid control in
Section 3.1 locates one perturbation strictly below zero and correctly
does not locate the opposite perturbation there.

## 3. Exact finite-envelope-moment obstruction

The reflected super-Gaussian base source has the asserted half-line
transform F(z)(1+cos 4z). At pi/4 its second derivative is positive:
integration by parts gives M_4=M_0/4, Cauchy-Schwarz gives
M_2<=M_0/2, and cos x>=1-x^2/2 gives the stated positive F value.
The compact perturbation is the weighted projection residual of
cos(bu) against a finite span of the displayed envelope kernels.
Its moments vanish exactly; its cosine pairing is a strictly positive
squared norm.

Nonmembership in that span follows from grouping real quadratic and
linear exponentials by their growth at positive infinity. After all
growing terms vanish, a constant plus decaying terms cannot equal a
nonconstant cosine. Positivity of the base source on the compact support
allows perturbations of either sign, preserving the specified moments
and moving the ordinary event in opposite directions.

The qualification is essential: this is the constructed control's
moment vector, **not theta's measured vector**. The perturbation need
not preserve source analyticity, strong shape, primitive identities,
arithmetic, or positive-time global real-rootedness. No exclusion of
theta-specific moment values, additional RH consequences, or signed
oscillatory measurements follows. The separate close normalized
endpoint controls retain their own distinct preservation list.

## 4. Many-root dynamics and the failed cap extension

[Note 09][n09] retains every root of the cluster. Logarithmic
differentiation, with the exact triple cancellation, gives
D'=8T+B D. The polynomial definition of T is valid at collisions.
The contour coefficient has factor two; replacing q=U_z/U by H_z/H
adds the rational integrand P_z P_zz/P^2, whose total residue is zero
because it decays cubically at infinity. The wall bound uses
|P_zz/P|<=m(m-1)/(R-r)^2, preserving the collar power two.
The optional scalar subtraction also integrates to zero.

The general-m theta geometry (G1)-(G3) pays both counts and walls
conditional on the full birth. Its coefficient bound is exactly
16m(m-1)B_1/(q_m R^(m+1)). All complete source moments remain present.
It supplies no time-boundary discriminant sign or exclusion.

The inherited Hermite splitting fixes order N=m(m-1)/2, with
D=d_m(t-t_0)^N+O((t-t_0)^(N+1)) and d_m>0. The forcing vanishes
to order N-1 at a full birth, which explains why the two-root
positive-derivative univalence argument no longer applies.

For a cubic, T=9p^2 after depressing the polynomial, so the real
integrating-factor discriminant is strictly increasing unless constant
and nonzero. There is at most one real event time; a separately located
negative event would exclude an endpoint real event. This does not
exclude nonreal events or supply actual theta event-location evidence.

The exact cubic has three interior event times, at 1/2 and
-1/4±i sqrt(3)/4; all are ordinary doubles, B=0 and total charge is
three. Its real cap signs would give one under the invalid extension.
The quartic birth has D=1769472 t^6, B=0, equal positive cap signs
and charge six. Its forcing changes sign on real time. Both examples
have strictly paid spatial and time boundaries. They refute the
specified extension, not the original two-root theorem or arbitrary
theta-specific many-root methods. The centered variance example also
correctly shows that its zero set is not the discriminant zero set.

## 5. Canonical-tail continuation of the signed estimator

The added Appendix A of [Note 08][n08] was derived by the window-analysis
agent, checked by the root and separately reviewed by the signed-response
agent. It uses the actual complete tail law in BW14 Note 04 and preserves
the unshifted reference required by that law; BW14 Note 05's corrected
reference would need a different residual.

Fubini with the same source measure across the contour gives the exact
response A J_K+(E_m-A) integral C_K d sigma. Its min/max bounds retain
every source mode. Combining them with the same nonlinear logarithmic
allowance gives the displayed discriminant interval. At distinct roots,
the residue factors (z_i-c)/P'(z_i)=1/2 give exactly the two cosine
terms divided by U(z_i); at a double they have the stated continuous
limit. No inverse internal gap occurs.

With reference roots in the right half-plane, the real kernel has both
signs arbitrarily far out. For positive real frequencies its primitive
is bounded and its limiting mean square is positive, ruling out an
eventual single sign. For conjugate roots the leading exponential has a
nonzero sinusoidal factor. Selected opposite-sign intervals then prove
the strict gains at both endpoints against the **same** pointwise source
floor/envelope. The identical wall-ratio and nonlinear allowance keep
the comparison fair. This does not establish that the narrower interval
omits zero or beats a stronger arithmetic evaluator.

The local applicability statement uses complete uniform tail convergence
on a fixed window. Rouché transfers its two root counts to the sufficiently
long unshifted head, and E_m/A remains bounded, so the envelope wall ratio
also tends to zero. There is no common cutoff across all heights.
Finite-prime controls with the same prefix/constants satisfy this bound
on a fixed admissible reference window, but their high-gap event is not
assumed to lie there. The construction preserves the distinction between
actual theta data, a shared estimate and an unproved strict signed margin.

## 6. Exact algebra checks, status, and continuation

The [standard-library script][script] and [small receipt][receipt]
provide exact rational checks: Hermite discriminants for m=2 through
8 at five nonzero rational times; five finite clusters with nonzero
exterior forcing; cubic T identities; and quadratic signed-response
controls, including rational payments for the whole-homotopy example. The script was inspected and run in a separate same-model
pass. All assertions passed. The printed Hermite T coefficients follow
from N d_m/8; they are not an independent computation of the roots
at negative times. The checks are algebraic controls, not an all-degree
proof, interval theta certificate, or new source acquisition.

The review supports these status changes only:

- ECE-01: parameterized hypothetical-double geometry complete.
- ECE-02: concrete signed consumer, error and homotopy payments supplied;
  the canonical-tail interval strictly improves its matched pointwise
  comparator. A positive unchanged-theta margin is still open.
- ECE-04: all-finite-height geometric existence paid; all-height signed
  exclusion and assembly remain open.
- ECE-05: finite many-root structure and specified failed-extension screen
  proved; source-estimate transfer and exclusion remain open.
- ECE-07: this round's internal review complete; the final chain is still
  gated by open ECE-02--06. Specialist review remains unmet.

ECE-03 and ECE-06 are not promoted. The next substantive input must be
a paid signed source margin or strictly negative event location for the
unchanged theta family, with its parameter range and complete errors.
Another absolute phase bound or another separated low-pair certificate
would not supply that input. This follows the repository's
[result index][results] and [avoid index][avoid], particularly
[coupled estimates][a12] and [scope][a07].

[n07]: ../notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md
[n08]: ../notes/08_SIGNED_DISCRIMINANT_RESPONSE_AND_EVENT_DISPLACEMENT_20261021.md
[n09]: ../notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md
[script]: ../numerics/ece_exact_controls.py
[receipt]: ../numerics/ECE_EXACT_CONTROLS_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
