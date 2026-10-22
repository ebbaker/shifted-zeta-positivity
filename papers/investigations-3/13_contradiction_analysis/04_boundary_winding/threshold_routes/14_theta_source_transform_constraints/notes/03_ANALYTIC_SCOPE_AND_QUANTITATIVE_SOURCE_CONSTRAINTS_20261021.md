# Analytic scope: what reflection exhausts and what source constraints can gain

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Analytic clarification requested by the user;
no numerical experiment. Proofs and assessment are by the authoring
assistant only, without independent specialist review or novelty claim.

## 1. The earlier stop is analytic and narrowly specified

[Note 02][n02] proves equality of the optimized odd-reflection adjoint
allowance and the best cosine allowance in a particular pointwise error
class. This is an analytic sharpness theorem, not a failed numerical
benchmark. More precision or a better search within that class cannot
produce a strict inequality. The complete transformed problem is not
restricted to that class, however: that relaxation remembers an envelope
and evenness, but forgets quantitative analytic and arithmetic coupling.

The [two-endpoint note][n01] also has an analytic comparison:
\(M-R_2>0\) follows from its positive series in equation (21).
Its numerical constants measure the difference. Its uniform theorem
for a larger coefficient family remains a useful robustness result
even though a bound for the one fully known theta sequence is smaller.

Thus “competitive” should identify the objective. A uniform analytic
theorem, a structural cancellation, or a stability result need not beat
point evaluation to be useful. A proposed stronger estimate for the
same object should still identify the inequality that improves. The
source identities alone do not imply a sign of their oscillatory image.

This continuation follows the [result index][results] and
[avoid index][avoid], especially [theta identities][arithmetic],
[control matching][controls], [scoped conclusions][scope],
[numerics before the question][numerics-first] and
[complete signed estimates][signed]. The new elementary estimates below
concern source-error classes; neither is an RH criterion or a theta
collision exclusion.

## 2. The abstract issue is which errors the constraints exclude

If \(r\) is a source residual, \(Lr=0\) is a known linear constraint
and \(k\) is the observation kernel, then, whenever the pairings exist,
\[
 \langle k,r\rangle=\langle k-L^*q,r\rangle.
 \tag{1}
\]
For a norm bound \(\|r\|_X\le1\), this gives
\[
 \sup_{\substack{Lr=0\\\|r\|_X\le1}}|\langle k,r\rangle|
 \le\inf_q\|k-L^*q\|_{X^*}.
 \tag{2}
\]
No equality or attainment is claimed here for arbitrary operators and
spaces. Formula (2) explains the role of the adjoint: it can remove a
part of the kernel that the admissible errors cannot detect. If an
approximation has a known nonzero defect \(Lr=b\), the identity instead
has the explicit extra term \(\langle q,b\rangle\). Ignoring that
term recreates the connector error of Note 02.

For reflection, \(L=I-R\) and its adjoint corrections are odd. The
cosine observation has already removed those directions. The sharpness
proof says this particular constraint is exhausted in this particular
norm. It says nothing comparable about a specified additional lattice
relation or a quantitatively bounded analytic class.

The practical analytic question is whether the relaxed class permits
errors whose signs track the observation kernel. If it does, the
triangle-inequality bound can be sharp. A useful extra constraint must
prevent that tracking in a quantitatively controlled way.

## 3. Qualitative analyticity alone can leave the bound sharp

Here is an explicit strengthening of that warning. Fix real \(t,x\)
and a real first-jet covector \(\ell=(\ell_0,\ell_1)\). Put
\[
 G(u)=\ell_0\cos(xu)-\ell_1u\sin(xu),\qquad
 w(u)=e^{tu^2}\Phi(u)>0\quad(u\ge0),
 \tag{3}
\]
where \(\Phi\) is the canonical source. Its pointwise-envelope allowance
in this direction is
\[
 B_0=\int_0^\infty w(u)|G(u)|du.
 \tag{4}
\]
Consider the source errors
\[
 r_M(u)=\Phi(u)m_M(u),\qquad
 m_M(u)=\operatorname{erf}(M G(u)),\quad M>0.
 \tag{5}
\]
The [error function][erf] is entire, real between -1 and 1 on the real
axis, and tends to the corresponding sign at real infinity. Since
\(G\) is even and entire, each \(r_M\) is even and holomorphic in
the theta strip, and \(|r_M(u)|\le\Phi(u)\) on the real axis.
Dominated convergence gives
\[
 \int_0^\infty e^{tu^2}r_M(u)G(u)du
 =\int_0^\infty w(u)G(u)\operatorname{erf}(MG(u))du
 \longrightarrow B_0.
 \tag{6}
\]
Zero values of G contribute zero; no assumption on their number is needed.

These examples also retain rapid decay on each closed horizontal
substrip, for each fixed M. Indeed the defining integral gives
\(|\operatorname{erf}z|\le(2/\sqrt\pi)|z|e^{|z|^2}\).
On \(|\Im u|\le d<\pi/8\), \(|G(u)|\le C_d(1+|\Re u|)\).
The multiplier therefore grows at most like
\(C_{M,d}(1+|\Re u|)\exp(C_{M,d}(1+|\Re u|)^2)\).
The complete theta source's double-exponential decay on both ends
dominates this bound and any bounded heat weight. Source derivatives
have the same property on smaller closed substrips, by Cauchy estimates.

It follows that the supremum B_0 is unchanged even if this error class
requires evenness, holomorphy in the fixed source strip and rapid
horizontal decay, **without uniform quantitative strip bounds**.
The constants in those bounds may grow with M. The discontinuous
pointwise extremizer from Note 02 need not itself be analytic for its
supremum to persist under analytic approximation.

This is not a perturbation preserving canonical lattice coefficients,
the primitive normalization or a prescribed coefficient prefix. No
collision is asserted for (5). Even positivity of a perturbed source
alone is insufficient to remove these residuals: for \(0<\epsilon<1\),
\(\Phi+\epsilon r_M\) is positive and even on the real axis. Its
additional arithmetic and normalization data have not been fixed.

## 4. A quantitative regularity constraint produces a strict analytic gain

There is also a concrete positive statement. Keep (3)–(4), and write
an error as \(r=\Phi m\), with real \(|m(u)|\le1\). Suppose G
has a simple sign-changing zero at \(u_0>0\). Reversing G if needed,
choose \(\delta<u_0\), \(g>0\), \(w_0>0\) such that
\[
 G(u_0+v)\ge gv,\quad G(u_0-v)\le-gv,\quad
 w(u_0\pm v)\ge w_0\qquad(0\le v\le\delta).
 \tag{7}
\]
Such constants exist by the simple-zero hypothesis and positivity and
continuity of w. Assume the **common** local derivative bound
\(|m'|\le L\) on this interval. For any \(0<h\le\delta\)
with \(Lh\le1\),
\[
 \boxed{\left|\int_0^\infty w(u)m(u)G(u)du\right|
 \le B_0-w_0g\left(h^2-\frac{2Lh^3}{3}\right)
 \le B_0-\frac{w_0gh^2}{3}.}
 \tag{8}
\]
**Proof.** The integrand of
\(B_0-\int wmG\) is nonnegative everywhere. Pair points
\(u_0-v,u_0+v\) on the indicated interval. Their total is at least
\[
 w_0gv\{2-m(u_0+v)+m(u_0-v)\}
 \ge w_0gv(2-2Lv).
\]
Integration from 0 to h gives the first loss in (8). Applying the same
argument to -m gives the absolute-value statement. Finally \(Lh\le1\)
implies the second inequality.

For example, if m is holomorphic and bounded by a common B on all
closed complex discs of radius \(\eta>0\) centered in this real
interval, Cauchy's formula gives \(L\le B/\eta\). Thus a quantitative
analytic norm provides exactly the missing restriction. In contrast,
at a simple zero of G, the multipliers (5) have
\(m_M'(u_0)=2MG'(u_0)/\sqrt\pi\), so no fixed such derivative bound
contains the whole saturating sequence.

Equation (8) is an elementary strict improvement over the pointwise
allowance, with explicit symbolic dependence on the additional
constraint. It requires no numerical search. It does **not** establish
that the actual residual in a useful theta approximation has a favorable
L, or that the gain survives the cost of proving that bound, or that it
excludes a collision. A direct method using the same extra constraint
can of course use (8) too. This is a possible analytic mechanism, not
a competition against an omniscient evaluator.

## 5. What can already be gained, and what remains a research target

There are three distinct outcomes worth separating.

1. **Preserve an essential cancellation.** The inherited complete
   reflected contour changes the type of approximation error. At fixed
   admissible N,d, an ordinary finite-prefix error has a nonzero
   algebraic connector, whereas the shifted approximation has a complete
   error bounded by a constant times exp(-dx). This is an analytic
   asymptotic advantage already available in the project, not a new
   result of the reflection-only norm optimization.
2. **Extract a sharper uniform estimate.** The existing [S01 paired
   endpoint theorem][s01] already does this symbolically. For its two
   positive monomial magnitudes a,b,
   \(|C_n|\le\sqrt{a^2+b^2-2ab\cos(4d)}<a+b\).
   This produces a strict saving under the theorem's nonstationary
   hypotheses before any numerical evaluation. Equation (8) is another
   elementary example of the kind of additional quantitative constraint
   that can improve a relaxed bound. Neither example gives a sign for H.
3. **Prove a property of the complete transformed field on a regime.**
   A controlled sign, a quantitative lower bound for its relevant jet,
   or a useful inequality at a stationary event would be a stronger
   analytic output. It would require preserving the signed retained
   arithmetic core and paying all other terms. Source identification,
   an upper error estimate or a positive source norm alone is not that
   output. No such new theta statement is proved here.

The [collision controls][controls] remain decisive for the third goal.
Full reflection and analytic strip decay admit the exact reflected
double event in Note 02. A regularity-driven reduction of an upper
error allowance need not exclude that event, and may apply to controls
as well. A theta-specific exclusion must explain where canonical
arithmetic, a quantitatively stronger bound, or another genuinely
unshared premise enters. Finite-prime, Euler-factor, reflected and
primitive controls retain the separate preservation lists in Note 02;
none is claimed to satisfy unchanged full theta coefficients.

**Research direction after the user's clarification:** prioritize the
analytic admissible class and the signed observation, not numerical
competition. First determine a useful quantitative constraint on the
actual residual, and whether it prevents saturation in the observation
direction. Keep both cusps and all lattice coefficients coupled where
they matter. A statement uniform in a parameter regime or an asymptotic
family is a legitimate goal. Its explicit inequality and complete
payments should precede any numerical experiment.

The [self-review][review] records the scope of (6) and (8). The program's
arithmetic sign bound remains open; this note changes the analytic focus
and supplies two auxiliary error-class facts, not a simplicity result.

[n01]: 01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md
[n02]: 02_FULL_REFLECTION_ADJOINT_AND_CONNECTOR_AUDIT_20261021.md
[review]: ../reviews/03_ANALYTIC_SCOPE_SELF_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[numerics-first]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[signed]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[s01]: ../../../../../11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[erf]: https://dlmf.nist.gov/7.2
