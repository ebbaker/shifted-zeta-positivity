# Hodge duality and arithmetic symmetries of the theta jets

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort
**max**, verified from this turn's metadata. Analytic derivations and an
internal self-check; no independent specialist review.

The manifold methods in Investigation 22 provide useful coordinates for
the symmetry questions in [brainstorm 01][b1] and [continuation 02][b2].
Their most direct simplification is a normalized covariant-jet basis in
which modular inversion is diagonal and source differentiation has constant
coefficients. Hodge duality itself adds no independent equation to the
existing self-dual forms. On the spectral side, the proposed first-jet
rotation has an explicit oscillator defect that an arithmetic estimate
would have to control.

These are identities and diagnostics, not a new signed estimate. The
repository [result summaries][summaries] and [patterns to avoid][avoid]
apply, especially [geometric realizations][s16], [theta identities][s14],
[collision controls][s12], [reformulations][a1], [generic lifts][a3], and
[scoped exclusions][a7]. A quantitative milestone would be a smaller
proved error, a larger certified region, or measured cost savings at the
same accuracy. None is claimed here.

## Three distinct meanings of duality

| Operation | What it acts on | What it preserves here |
| --- | --- | --- |
| Four-dimensional Hodge star | Two-forms at a fixed point, for a chosen metric and orientation | The self-dual input sector; the ASD curvature changes sign |
| Modular inversion | The theta section and lattice parameter, with its automorphy factor | The complete source under u to minus u |
| Quarter turn of the normalized first jet | A two-dimensional real value/derivative plane | Its Euclidean radius algebraically; physical evolution preserves it only in the exact oscillator model |

The familiar quarter turn on one-forms in an oriented Euclidean plane has
star squared equal to minus one. The four-dimensional star on two-forms
has star squared equal to one. Neither operation should be identified with
modular inversion without a separate intertwining identity.

## What the existing Hodge construction already decides

At fixed heat time, Investigation 22 constructs

\[
 \alpha_f=\frac1{\sqrt2}\operatorname{Re}(f(z)\,dz\wedge dw),
 \qquad *\alpha_f=\alpha_f,
 \qquad \alpha_f\wedge\alpha_g=\operatorname{Re}(f\bar g)\,dV.
\]

For the physical jets its signed pairing is

\[
 \alpha_{H_x}\wedge\alpha_{H_x}-\alpha_H\wedge\alpha_{H_{xx}}
 =(H_x^2-HH_{xx})\,dV
\]

on the real spectral slice, as an evaluated coefficient. Applying star to
any input leaves it unchanged. All inputs are self-dual, but the quadratic
form in the three real jet coefficients has eigenvalues
\(1,1/2,-1/2\). Self-duality therefore does not turn this mixed expression
into a positive squared norm. For example \(f(z)=1+z^2\) gives value
\(-2\) at zero while all its input forms satisfy the same self-duality.
This example is also a time slice of the polynomial backward heat control.
See [the manuscript, Hodge pairing subsection][manifold].

The arithmetic connection is a different construction. Its curvature is

\[
 F=2\pi i(q\,dp\wedge dq-dr\wedge ds),\qquad *F=-F.
\]

On \(\gamma(u)=(\tau=ie^{4u},z=0)\), the adapted connection is zero
and its curvature pulls back to zero. The natural external tensor product
on \(\gamma\times\gamma\) is flat too. Consequently a new curvature
term cannot be generated solely by differentiating tangentially along
these physical source paths. This is the scoped result of [metric freedom
and physical restriction][metric], not an exclusion of all geometric
methods. Transverse jets still satisfy

\[
 [\nabla_X,\mathcal D^k]\big|_{z=0}
 =-k(k-1)\frac\pi q\mathcal D^{k-2}\big|_{z=0}.
\]

Those lower-jet terms must be retained. The marked semi-flat metric also
does not descend through the full modular action as written; its ASD
equation does not automatically furnish a modularly invariant norm for
the physical observation.

## A normalized basis that simplifies the source equations

Use the period-one convention
\(\vartheta(z,iq)=\sum_{n\in\mathbb Z}e^{-\pi qn^2+2\pi inz}\).
Set \(q=e^{4u}\) and

\[
 J_k(q)=(\mathcal D^k\vartheta)(0,iq),\qquad
 T_k(u)=\pi^{-k/2}q^{k/2+1/4}J_k(q).
\tag{1}
\]

Only even k are needed; the odd jets vanish. Investigation 22 gives the
generating identity and recurrence

\[
 G_q(w):=e^{\pi w^2/(2q)}\vartheta(w,iq)
       =\sum_{k\ge0}J_k(q)\frac{w^k}{k!},
\]
\[
 \partial_uJ_k=\frac q\pi J_{k+2}-(2k+1)J_k
                   -k(k-1)\frac\pi qJ_{k-2}.
\tag{2}
\]

These are [existing transverse-jet identities][bridge]. Differentiating
the normalization in (1) adds \((2k+1)J_k\), exactly cancelling the
diagonal term of (2). The remaining powers of q and pi cancel, giving

\[
 \boxed{\partial_uT_k=T_{k+2}-k(k-1)T_{k-2}.}
\tag{3}
\]

Terms with zero coefficient are omitted. This is an infinite ladder,
not a closed finite system.

Modular inversion supplies the complementary simplification. In this
theta convention, the classical transformation [DLMF 20.7.32][dlmf] gives

\[
 G_q(w)=q^{-1/2}G_{1/q}(-iw/q).
\]

The sign of the argument is immaterial because the theta section is even.
Comparing even derivatives gives

\[
 J_{2m}(1/q)=(-1)^m q^{2m+1/2}J_{2m}(q),
 \qquad
 \boxed{T_{2m}(-u)=(-1)^mT_{2m}(u).}
\tag{4}
\]

Thus the orders divisible by four form the even sector, and the orders
congruent to two modulo four form the odd sector. Differentiation (3)
exchanges the sectors, as it should. The modularity of the Hermite jets,
including the fourth-jet inversion, was already identified in
[Investigation 22 Review 16, Section 5][prior-review]. Equations (3)–(4)
are a convenient normalized synthesis of that law and (2), with no claim
of a new underlying symmetry.

The complete source and its first two source derivatives become

\[
 \boxed{16\Phi=T_4-3T_0,\qquad
 16\Phi'=T_6-15T_2,\qquad
 16\Phi''=T_8-45T_4+30T_0.}
\tag{5}
\]

These follow directly from the [complete covariant source][connection]
and (3). For example differentiating \(T_4-3T_0\) gives
\(T_6-12T_2-3T_2\), and differentiating again gives the last expression.
This basis removes scale-dependent coefficients and makes reflection
parity visible before estimating anything.

The cancellation in (5) must occur before the physical transform. The
zero lattice mode of \(T_{2m}\) is \((2m-1)!!e^u\), with
\((-1)!!=1\). These growing terms cancel in all three combinations.
Their separate positive-time half-line transforms do not converge.
Multiplication by \(e^{tu^2}\) preserves (4), but changes (3) to

\[
 \partial_u(e^{tu^2}T_k)
 =e^{tu^2}\{T_{k+2}-k(k-1)T_{k-2}+2tuT_k\}.
\tag{6}
\]

It does not yield a finite closed spectral system. Reflection still gives
the known evenness of the complete source and H; it is not a relation
between H and its first derivative at a fixed positive height.

## The exact defect of first-jet rotation

Fix t and a real interval where the existing normalization satisfies
\(\mathcal A_t>0\) and \(\omega=\partial_x\vartheta_t\ne0\).
Use \(Q=H/\mathcal A_t\) and \(\theta=\vartheta_t(x)\), so
\(D_\theta=\omega^{-1}\partial_x\). Define

\[
 W=Q-iD_\theta Q,\qquad
 \mathscr R=(D_\theta^2+1)Q
 =Q+\frac{Q_{xx}}{\omega^2}-\frac{\omega_xQ_x}{\omega^3}.
\tag{7}
\]

These quantities remain defined at a common zero of Q and Q_x. Direct
differentiation proves

\[
 \boxed{D_\theta W=iW-i\mathscr R,\qquad
 D_\theta(e^{-i\theta}W)=-ie^{-i\theta}\mathscr R.}
\tag{8}
\]

For \(Q=2\cos\theta\), the defect vanishes and \(W=2e^{i\theta}\).
The algebraic quarter turn of the jet \((Q,-Q_\theta)\) is
\((Q_\theta,Q)\). To be the jet of the scalar function Q_theta it would
need \(-Q_{\theta\theta}=Q\). Thus (7) is exactly the compatibility
obstruction to treating a quarter turn as a symmetry of the scalar jet.

The integrated identity is

\[
 e^{-i\theta}W(\theta)=e^{-i\theta_0}W(\theta_0)
       -i\int_{\theta_0}^{\theta}e^{-is}\mathscr R(s)\,ds.
\tag{9}
\]

A separately established bound on the modulus of the **complete complex
integral**, strictly smaller than \(|W(\theta_0)|\) throughout a phase
interval, would propagate nonvanishing. Estimating it by
\(\int|\mathscr R|\) can lose the cancellation that made the change of
variables useful. Formula (9) is an elementary variation-of-constants
identity, not an independently established arithmetic bound. It refines
the question posed in brainstorm 01 and should not be counted as another
exclusion milestone. The [earlier amplitude–phase criterion][earlier],
label `lem:phase`, already identifies the related missing estimates.

The normalized radius is not the physical energy. With
\(a=\partial_x\log\mathcal A_t\) and \(J=(Q,-D_\theta Q)\),

\[
 E=\mathcal A_t^2\{J_1^2+(aJ_1-\omega J_2)^2\}.
\tag{10}
\]

This invertible change of coordinates preserves the collision set when
omega is nonzero. Uniform energy comparisons require bounds on the
displayed matrix. Choosing theta from the unknown actual jet angle would
instead make a circular definition and would be singular at a collision.

## Where a quantitative use could succeed or fail

On a fixed-cutoff interval the retained approximation is a sum of
\(f_n=2b_n\cos\phi_n\). With
\(\rho_n=D_\theta\phi_n\), the defect of one term is exactly

\[
 (D_\theta^2+1)f_n
 =2\{[D_\theta^2b_n+(1-\rho_n^2)b_n]\cos\phi_n
    -[2\rho_nD_\theta b_n+b_nD_\theta\rho_n]\sin\phi_n\}.
\tag{11}
\]

The [earlier exact joint-vector calculation][earlier], labels `sc:vector`
and `sc:coordinateasymptotics`, gives the leading frequency ratio
\(\rho_n\sim1-2\log n/\log(x/(4\pi))\) in its stated high-height
regime. Low fixed modes approach the leading rotation; near the natural
cutoff the ratio approaches zero. Consequently the frozen-amplitude
coefficient \(1-\rho_n^2\) in (11) is not uniformly small over the
whole retained sum. This observation is not a lower bound for its signed
sum. It explains why a common approximate rotation cannot simply be
assumed for every mode.

The worthwhile bounded experiment remains the signed cutoff correction
from brainstorm 01: retain the published nonzero multiplier times
\(C_0(p)\), exploit its evenness in p, and combine it with the neighboring
retained terms before estimating. That evenness follows from [Polymath
equation (53)][polymath]; it is not a symmetry of the full H. The normalized
jet and (8) give a way to measure whether the combination improves a
complete first-jet error or an integrated rotation defect.

This experiment has an additional cost: (7) uses two derivatives. If a
holomorphic remainder r is bounded by eta on a disk of radius d around a
real point, Cauchy's inequalities give

\[
 |(D_\theta^2+1)r|
 \le\eta\left(1+\frac{2}{d^2|\omega|^2}
                  +\frac{|\omega_x|}{d|\omega|^3}\right).
\tag{12}
\]

The [existing fixed-cutoff contract][outer] supplies the appropriate kind
of disk representation. The published real value estimate alone does not
pay for (12); the revised signed correction needs its own holomorphic
remainder bound. At cutoff crossings retain a fixed cutoff and its exact
transition terms. A useful outcome must beat the simpler direct first-jet
contract after paying these costs. The known adjacent-packet obstruction
and growing terminal-block absolute mass (`sc:packet`, `prop:absmass` in
the earlier manuscript) remain applicable to their stated methods.

For two-source experiments, Investigation 22's [coupled addition
formula][coupled] already retains the mixed derivative and both parity
sectors. Its natural post-source parity matrices are indefinite. A Hodge
norm or separate-sector bound cannot be substituted for that signed
recombination without a new comparison.

## Verification and control scope

The [companion assessment][review] maps the controls to their missing
theta premises. Fresh replays reject all five existing event boxes and
the distinct Euler negative-Laguerre witness. They check the existing
rejection interface, not a new symmetry-based estimate. The ASD path and
complete signed-bridge checkers also pass. The [small record][record]
preserves current source hashes, exact algebra checks, and execution
scope; its [checker][checker] tests the normalized mode ladder, source
cancellations, and the formal rotation-defect coefficients. Universal
identities (3)–(9) follow from the displayed derivations, not finite tests.

[b1]: ../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[b2]: ../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[s16]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a1]: ../../../../avoid/01_restating_the_target.md
[a3]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a7]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[manifold]: ../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[metric]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[bridge]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[connection]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md
[prior-review]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md
[coupled]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md
[earlier]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[outer]: ../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[dlmf]: https://dlmf.nist.gov/20.7.E32
[polymath]: https://arxiv.org/html/1904.12438v2#S6.SS2
[review]: ../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[record]: ../numerics/HODGE_MODULAR_ROTATION_REVIEW_CHECKS_20261018.json
[checker]: ../numerics/check_hodge_modular_rotation.py
