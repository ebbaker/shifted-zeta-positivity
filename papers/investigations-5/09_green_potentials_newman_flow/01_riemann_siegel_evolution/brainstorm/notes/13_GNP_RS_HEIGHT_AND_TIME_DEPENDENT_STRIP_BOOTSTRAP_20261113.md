# Weighted boundary prediction and a height and time dependent bootstrap

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, continuing child chat0007.
Actual model and reasoning effort are unavailable in the recorded
configurations. Same-assistant analytical checking; no independent review.

**Status: explanatory brainstorm and a scoped polynomial diagnostic.**
The author's proposal is to improve a proved zero enclosure by moving its
boundary toward the real axis, with both heat-time and zeta-height
dependence. The observation offset can vary too. The formulas below
separate these choices and identify the quantitative input an improvement
would require. No canonical strip improvement or extension of B10 is proved.

Read the [result index][results], especially [heat-flow results][r11],
[collision controls][r12] and [local geometry][r13], and the
[avoid index][avoid], especially [classification][a01],
[control screening][a02], [scoped exclusions][a07],
[coupled estimates][a12], [circular hypotheses][a14] and
[checked imports][a16]. The limiting all-real assertion is a target
reformulation, not a milestone. A milestone here would be a proved,
explicitly quantified improvement to an enclosure on a stated domain.

## 1. The weighted boundary prediction

Write \(u_\lambda(z)=\log|H_\lambda(z)|\). In a fixed strip
\(0<\operatorname{Im}z<B\), evaluated at \(p=X+ib\), \(0<b<B\),
the harmonic prediction from the two boundary lines is

\[
 \mathcal P_{\lambda,B}^{(b)}(X)=
 \int_{\mathbb R} P_{0,B}^{(b)}(x-X)u_\lambda(x)\,dx+
 \int_{\mathbb R} P_{B,B}^{(b)}(x-X)u_\lambda(x+iB)\,dx,             \tag{1}
\]

\[
 P_{0,B}^{(b)}(v)=
 \frac{\sin(\pi b/B)}
 {2B\{\cosh(\pi v/B)-\cos(\pi b/B)\}},\qquad
 P_{B,B}^{(b)}(v)=
 \frac{\sin(\pi b/B)}
 {2B\{\cosh(\pi v/B)+\cos(\pi b/B)\}}.                            \tag{2}
\]

Their masses are \(1-b/B\) and \(b/B\). At the original \(B=8,b=4\),

\[
 \mathcal P_{\lambda,8}^{(4)}(X)=
 \int_{\mathbb R}
 \frac{\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|}
 {16\cosh(\pi(x-X)/8)}\,dx.                                     \tag{3}
\]

The observed defect is

\[
 J_{\lambda,B}^{(b)}(X)=
 \mathcal P_{\lambda,B}^{(b)}(X)-\log|H_\lambda(X+ib)|
 =\sum_{\zeta_j\ {\rm in\ strip}}m_jG_B(X+ib,\zeta_j),             \tag{4}
\]

with the positive Green function normalized by
\(-\Delta G=2\pi\delta\). Thus the prediction exceeds the observed log
modulus by the zero potential. In a zero-free strip the difference is zero.
The identity and growth control at \(B=8,b=4\) are in the
[parent proof][green]; the general kernels and offset calculations are
in [Note12][n12]. A boundary zero has no Green atom, and a zero at the
observation point gives an infinite defect.

## 2. Three distinct moving quantities

For positive \(X\), zeta height is \(T=X/2\). At time zero
\(H_0(X+ib)=\xi((1+b)/2-iX/2)/8\); for negative \(X\), use \(T=|X|/2\).
The transverse offset \(b\) measures distance from the real axis in the
Newman plane. At nonzero heat time this is the deformed field.

Use

\[
 \lambda,\qquad a_n(\lambda,X),\qquad b_n(\lambda,X)
\]

for heat time, the half-width of the allowed-zero band at iteration \(n\),
and the observation offset. The proposed enclosure is

\[
 H_\lambda(x+iy)=0\ \Longrightarrow\
 |y|\le a_n(\lambda,x),\qquad
 0\le a_{n+1}(\lambda,x)\le a_n(\lambda,x).                       \tag{5}
\]

The allowed band shrinks; the zero-free exterior expands toward the axis.
This permits real zeros. Both \(a_n\) and \(b_n\) may vary with zeta height.
A possible safe observation is \(b_n=a_n+\eta_n\) with a proved positive
buffer \(\eta_n\); the local enclosure proves nonvanishing there but does
not give a quantitative normalized-field lower bound.

For a fixed domain \(0<y<B\), simply substitute
\(b=b_n(\lambda,X)\) into (1)–(2). Each evaluation uses the same two
horizontal boundary lines. No derivative of \(b_n\) belongs in this
pointwise formula. Along a differentiable sampling path \(\lambda=\lambda(X)\),
however, the chain rule includes

\[
 \frac{dJ}{dX}=
 \partial_XJ+\lambda'(X)\partial_\lambda J+
 \{\,\partial_X b_n+\lambda'(X)\partial_\lambda b_n\,\}\partial_bJ.
                                                                    \tag{6}
\]

This holds where the derivatives exist and the observation is nonzero.
An average theorem at fixed \(b=4\) does not automatically apply to (6).

## 3. A curved boundary changes the boundary measure

If the contour itself follows \(y=a_n(\lambda,x)\), it bounds a curved
domain. Replacing \(B\) or a lower endpoint in (2) by its value at \(X\)
does not produce that domain's exact Poisson kernel.

At a fixed time, take a bounded regular domain \(D\), with observation
\(p\in D\), and no zeros on its boundary. The general formula is

\[
 \mathcal P_{\lambda,D}(p)=
 \int_{\partial D}u_\lambda(\zeta)\,d\omega_D^p(\zeta),\qquad
 \mathcal P_{\lambda,D}(p)-u_\lambda(p)=
 \sum_{\zeta_j\in D}m_jG_D(p,\zeta_j).                            \tag{7}
\]

Here \(\omega_D^p\) is harmonic measure, the geometry-dependent positive
boundary weighting of total mass one. The bounded formulation retains
both vertical sides. An unbounded-domain version must pay the side limit
and growth/tail conditions. A finite rectangle approximation must retain
the side integrals and any boundary-shape approximation error.

In particular, for \(D\) lying above an already proved graph \(a_n\), the
right side of (7) vanishes. That interpolation identity does not by itself
establish nonvanishing in the new layer below \(a_n\).

## 4. What one improvement would have to pay

At a fixed time, the new layer is
\(a_{n+1}(\lambda,x)<y\le a_n(\lambda,x)\).
There is an elementary local extension step worth comparing with the
Green and contour-count alternatives.

Choose a nonzero analytic carrier and write \(F_\lambda=H_\lambda/C_\lambda\).
At \(p_0=x+ib_0\), suppose \(|F_\lambda(p_0)|\ge m>0\) and
\(|F_\lambda'(x+iy)|\le M\), \(M>0\), throughout a proposed inward
vertical segment of length \(h\). Integration along that segment gives

\[
 |F_\lambda(x+i(b_0-s))|\ge m-Ms>0
 \quad(0\le s\le h),\qquad h<m/M.
\]

In particular \(h=m/(2M)\) retains a floor \(m/2\), provided the derivative
bound has been established over that full length. If
\(b_0=a_n+\eta\), this improves the known enclosure only when \(h>\eta\):
the new bound is \(a_{n+1}=b_0-h<a_n\), while \(b_0-h\ge0\).
For an approximate normalized field \(A\), one may use
\(m=|A(p_0)|-E_0>0\) and
\(M=\sup_{\rm segment}|A'|+E_1\), with certified value and derivative
errors \(E_0,E_1\). These are errors for the full normalized field,
including both RS arms and the derivative of its carrier.

Apply this simultaneously over the stated height and time domain to get
a curved enclosure. The segment estimate uses the analytic field itself,
so it does not assume a logarithm exists in the extension being proved.
It is a generic local lemma; repeated positive step sizes can still
shrink to zero with the limiting boundary above the axis. The additional
research input is quantitative control of that iteration, not local
continuity or nonvanishing alone.

For a Green comparison, put a compact target \(K\) strictly inside a
regular domain \(D\), with \(p\notin K\), and set

\[
 g_K=\inf_{\zeta\in K}G_D(p,\zeta)>0.
\]

If a complete approximation gives \(J_D(p)\le\widehat J_D(p)+E\), then

\[
 \widehat J_D(p)+E<g_K                                           \tag{8}
\]

excludes a zero in \(K\). The error \(E\) includes boundary, observation,
tail, quadrature and domain-approximation errors wherever present.
The lower contour must sit below the part of the target one intends to
exclude: a zero on the contour itself has zero Green weight. Exhausting
an open layer by compact targets is valid only when (8) is proved for
every required target; its positive margin need not stay uniform.

Alternatively, for an analytic approximant \(A\) with certified zero
count zero in \(D\), the complete-boundary inequality

\[
 \sup_{\partial D}|H_\lambda-A|
 <\inf_{\partial D}|A|                                          \tag{9}
\]

gives the same zero count by Rouché. The new lower boundary and both
vertical sides are part of (9). Knowing only the old outer contour
is nonzero does not establish this inequality.

If a nonzero analytic normalization gives \(F=H_\lambda/C_\lambda\),
\(|F-A|\le\varepsilon\), and \(|A|\ge\mu>\varepsilon\), its logarithmic
error is at most \(\varepsilon/(\mu-\varepsilon)\). Any harmonic-carrier
cancellation must hold on the complete domain. This is where a shrinking
offset can improve the Green margin while also making the arithmetic
error harder to control. Formula (8) is a diagnostic interface, not an
acquired estimate.

## 5. Known heat contraction and a numerical measure of improvement

In the present normalization \(\partial_\lambda H=-H_{zz}\),
de Bruijn's global strip theorem gives

\[
 |\operatorname{Im}\zeta_j(\lambda_0)|\le A
 \quad\Longrightarrow\quad
 |\operatorname{Im}\zeta_j(\lambda_0+\tau)|
 \le\sqrt{\max(A^2-2\tau,0)},\qquad \tau>0.                       \tag{10}
\]

It implies \(\Lambda\le\lambda_0+A^2/2\).
The primary-source check is Polymath,
[arXiv:1904.12438v2, Theorem 3.2][poly3].
Its [Theorem 1.2 and Proposition 3.3][poly1] combine initial finite-height
information, final large-height information and a connecting space-time
barrier. This is an existing precedent for the author's proposal.

For constant global widths define \(Q=\lambda+A^2/2\). Before the
zero-width endpoint, (10) leaves \(Q\) unchanged. Iterating the same
contraction only divides up the same physical time. A further proved
squared-width gain \(\delta>0\),

\[
 A_{\rm new}^2\le A_{\rm old}^2-2\tau-\delta,\qquad
 A_{\rm old}^2-2\tau-\delta\ge0,
\]

would instead give \(Q_{\rm new}\le Q_{\rm old}-\delta/2\).
This is bookkeeping for a possible improvement, not a proof of one.
The positive-part endpoint must be treated separately.

For a height-dependent enclosure one can take
\(A=\sup_x a_n(\lambda,x)\) if this supremum is finite and the enclosure
is global. Replacing \(A\) by the value at each \(x\) in (10) is not valid.
Likewise, proving a smaller width at one positive time does not propagate
that improvement backward to time zero.

## 6. The extra term in a height-dependent time barrier

At a simple zero \(z_j(\lambda)=x_j(\lambda)+iy_j(\lambda)\),
differentiation of \(H_\lambda(z_j(\lambda))=0\) gives

\[
 z_j'=\frac{H_{zz}}{H_z}(z_j),\qquad
 \frac d{d\lambda}\{y_j-a(\lambda,x_j)\}
 =y_j'-a_\lambda-a_xx_j'.                                     \tag{11}
\]

For a proposed upper enclosure, a sufficient strict inward condition
at every possible simple first contact is

\[
 \operatorname{Im}\frac{H_{zz}}{H_z}
 -a_x\operatorname{Re}\frac{H_{zz}}{H_z}-a_\lambda<0.             \tag{12}
\]

The term \(a_xx_j'\) pays for changing zeta height. The quotient requires
simplicity; a complete argument must address multiple contacts through
cluster analysis or contour zero counts, initial containment, side entry,
and possible entry from infinity. Local continuity alone supplies none
of these uniform estimates. Polymath's Section 3 handles these issues
for its particular barrier, not for an arbitrary graph.

## 7. Exact diagnostic against pointwise use of the strip theorem

This example screens only the attempted substitution
\(A\mapsto a_0(x)\) in (10).
Let \(F_0\) be the monic polynomial with roots

\[
 \{\ \pm10\pm\tfrac12i,\quad
       \pm\tfrac{101}{10}\pm\tfrac35i\ \},
 \qquad
 F_\lambda=\sum_{k=0}^{4}
 \frac{(-\lambda)^k}{k!}\partial_z^{2k}F_0.                      \tag{13}
\]

It is real and even and satisfies \(\partial_\lambda F=-F_{zz}\).
All its initial roots obey the smooth even enclosure

\[
 a_0(x)=\tfrac12+\tfrac1{10}\sin^2(5\pi x).
\]

At the simple zero \(z_*=10+i/2\),

\[
 z_*'=2\sum_{\zeta\ne z_*}\frac1{z_*-\zeta},\qquad
 \operatorname{Im}z_*'
 =8-\frac{110}{61}-\frac2{401}
   +\frac{10}{20201}-\frac{110}{20261}
 =6.1867996557\ldots>6.                                       \tag{14}
\]

Thus this lower zero initially moves outward while its outermost zeros
initially move inward: the transverse velocity at \(101/10+3i/5\)
is less than \(-5/3\), also checked exactly in Numerics21.
This is compatible with a contracting global band. For the naive candidate
\(a(\lambda,x)=\sqrt{a_0(x)^2-2\lambda}\), at \((0,10)\)
one has \(a_x=0\), \(a_\lambda=-2\). Hence

\[
 \left.\frac d{d\lambda}(y_*-a(\lambda,x_*))\right|_{\lambda=0}
 >8,
\]

so this proposed height-dependent enclosure fails immediately. A smooth
nonconstant envelope does not inherit (10) pointwise. This does not
exclude a different variable-boundary theorem with additional hypotheses.
The exact rational record is [Numerics21][check]; it checks the root
formula against \(F_0''/F_0'\) at \(z_*\). It is an algebraic diagnostic,
not evidence concerning RH. This polynomial has no canonical theta
source or canonical arithmetic coefficients.

## 8. Collision-control screen

The following is an analytical premise screen against [cluster12][r12],
not a rerun of its archived numerical certificates.

| Control class | Premise it lacks, and implication for this proposal |
| --- | --- |
| Euler-factor controls | Fail the exact undeformed theta arithmetic/completion; nevertheless retain positivity, symmetry and finite positive collision thresholds. Those generic properties cannot force iteration to zero at time zero. |
| Weighted-square controls | Fail unit theta coefficients and full source reflection. Their finite endpoint matches do not establish the missing arithmetic boundary margin; they also lack an all-real heat time. |
| Reflected super-Gaussian control | Fails the full integer-square theta expansion. Full reflection and positive Gram forms do not supply (8) or (12). |
| Smooth shape and positive-primitive controls | Fail the complete theta arithmetic source despite the listed positivity, decay and primitive matches. These properties do not establish a boundary-improvement rate. |
| Finite-prime orbit controls | Fail full source reflection and complete canonical arithmetic agreement. Selected prime identities alone do not establish a uniform margin on all heights. |
| The polynomial (13) | Fails the theta source and arithmetic hypotheses; it directly refutes only pointwise localization of the global strip law. |

The Green identities themselves do not distinguish these fields where
their domain/growth assumptions hold. Any canonical improvement must
identify the extra quantitative input it uses; this note has not obtained it.

## 9. Continuation and model change

The next bounded comparison should freeze one height block
\([U,U+\ell]\), one heat interval, and a known enclosure. Choose an
explicit smaller candidate envelope and an observation buffer. First
compare the elementary \(m/(2M)\) inward extension with a Green or
contour-count implementation, including the sides and the error from
approximating any curve. Attempt one strictly positive gain that exceeds
the initial observation buffer, or a gain in (8), (9), or an applicable
first-contact bound. Record the gained width and its full error budget.

If using B10, retain its \(c=1\), \(b=4\), fixed strip thickness eight,
block-constant cutoff and stated interval range until a replacement
transfer is actually proved. Its averaged signed estimate does not yet
give the complete-boundary margins for this bootstrap.

An iteration also needs common domain coverage, admissible errors at
every step and a convergence argument. Height onsets escaping with the
iteration cannot exclude a fixed finite-height zero. A boundary
approaching zero only as \(X\to\infty\) still permits nonreal zeros at
finite heights. These are quantifier requirements, not a prohibition
on height-dependent estimates.

**Suggested continuation model: GPT-6 Astra**, retaining the existing
[continuation recommendation][n11]. The [official model page][model],
checked 13 November 2026, identifies complex reasoning and research as
uses; the selection here is a task-fit judgment. Actual backend and effort
remain unrecorded. No model setting is changed and no delegation occurred.

The registered chat refresh still fails the source creation-time identity
check. The verified record is preserved; completed public text uses the
explicitly unregistered supplemental workflow, followed by the bounded
exact-turn capture. This does not repair the registry discrepancy.

[results]: ../../../../../../result-summaries/README.md
[r11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[r13]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[a16]: ../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[green]: ../../../manuscript/sections/05_green.tex
[n11]: 11_GNP_RS_PERSISTENCE_CONTINUATION_20261113.md
[n12]: 12_GNP_RS_LOWER_TRANSVERSE_OFFSET_AND_LOG_OBSERVATION_20261113.md
[check]: ../../numerics/21_GNP_RS_VARIABLE_STRIP_DIAGNOSTIC_20261113.json
[poly3]: https://arxiv.org/html/1904.12438v2#S3
[poly1]: https://arxiv.org/html/1904.12438v2#S1
[model]: https://developers.openai.com/api/docs/models/gpt-6-astra
