# Applying the radial primitive to both source factors of A0

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, direct chat0007, thread
`01a1c389-3fe9-7930-8223-c935cc1920e1`, turn
`01a1c3c2-5721-7421-a134-8d0037d5413a`. Actual backend model and reasoning
effort are unavailable in accessible capture metadata.

**Author-requested B03 addendum; exact identities proved in-note with
same-assistant checks.** Applying the established three-dimensional
primitive transfer to both source factors does remove their polynomial
square-index prefactors. The answer is a complete double primitive
integral and one boundary integral. The primitive product is a rectangular
rank-two Gaussian lattice sum. This supplies a concrete formula for the
proposed arithmetic analysis, but no signed estimate or collision
exclusion yet.

The author's new proposed method authorizes this bounded addendum: one
candidate, one exact transfer/convergence derivation and one local check.
The completed r3 decision is preserved; its exhausted pass is not reset.
All new research notes remain in the requested brainstorm folder.
[Progress01][progress] owns the live task status. E09/E10 remain unissued.

Read the [result index][results], particularly [theta arithmetic14][theta]
and [controls12][controls], and the [avoid index][avoid], particularly
[classification01][a01], [control premises02][a02], [scoped claims07][a07]
and [joint estimates12][a12]. The present result is an exact representation,
not an independently established sign premise. The earlier negative-region
screen in [Note09][n09] concerned discarding quantitative positive
contributions; it did not exclude this primitive/lattice method.

## 1. The located three-dimensional identity

Investigation05 [Note01, Section 2][radial] and [Note73, Sections 1–2][ibp]
give, for u >= 0,
\[
 r=e^{2u},\qquad A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
 \psi(u)=e^u A(e^{2u}),
\]
\[
 \boxed{\Phi(u)=\tfrac12r^{5/2}\Delta_3 A(r),\qquad
 (\partial_u^2-1)\psi=8\Phi.}                         \tag{1}
\]
Here \(\Delta_3=\partial_r^2+2r^{-1}\partial_r\). Indeed
\(\Delta_3 e^{-cr^2}=(4c^2r^2-6c)e^{-cr^2}\), so (1) reproduces
the canonical \(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\) prefactor exactly.
The spatial dimension three is distinct from the rank-one index n.

Write \(\Theta(r)=1+2A(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r^2}\).
The modular identity \(\Theta(r)=r^{-1}\Theta(1/r)\), the z=0,
tau=i r² specialization of [DLMF 20.7.32][dlmf], gives
\[
 A'(1)=-\tfrac12A(1)-\tfrac14,
 \qquad \psi(0)=A(1),\qquad \psi'(0)=-\tfrac12.       \tag{2}
\]
For an admissible test f, the complete transfer is therefore
\[
 \int_0^\infty\Phi(u)f(u)\,du
 =\frac{f(0)}{16}+\frac{A(1)f'(0)}8
  +\frac18\int_0^\infty\psi(u)(f''-f)(u)\,du.        \tag{3}
\]
The sign follows from \([\psi'f-\psi f']_0^\infty\). In radial variables,
with \(h(r)=r^{-1/2}f(\log r/2)\), the same formula reads
\[
 \frac14\int_1^\infty A(r)\Delta_3h(r)r^2\,dr
 +\frac14\{-A'(1)h(1)+A(1)h'(1)\}.                 \tag{4}
\]
Thus the u=0 term is exactly the initial unit-sphere contribution. The
time weight belongs to f; replacing the primitive by a positive-time
full-space potential would require different tail and boundary payments.

## 2. The complete two-source transfer

Keep \(F_\lambda(u)=e^{\lambda u^2}\Phi(u)\), with no normalization.
For real lambda, X and v>0, the exact source formula from [Note09][n09] is
\[
 A_0=\frac18\iint_{\mathbb R^2}(p-q)^2F_\lambda(p)F_\lambda(q)
       e^{-v(p+q)^2/2}\cos(X(p+q))\,dp\,dq.
\]
Fold using the complete even source and define
\[
 g(s)=e^{-vs^2/2}\cos(Xs),\quad
 K(p,q)=\tfrac14\{(p-q)^2g(p+q)+(p+q)^2g(p-q)\},
\]
\[
 T(p,q)=e^{\lambda(p^2+q^2)}K(p,q),\qquad
 D_p=\partial_p^2-1,\quad D_q=\partial_q^2-1.         \tag{5}
\]
Then \(A_0=\iint_{[0,\infty)^2}\Phi(p)\Phi(q)T(p,q)\,dp\,dq\).
The test T is symmetric in p,q and even in each variable separately.
Applying (3) in each variable gives
\[
\begin{split}
64 A_0={}&\iint\psi(p)\psi(q)D_pD_qT(p,q)\,dp\,dq\\
 &+\tfrac12\int\psi(q)D_qT(0,q)\,dq
  +\tfrac12\int\psi(p)D_pT(p,0)\,dp+\tfrac14T(0,0).
\end{split}                                                     \tag{6}
\]
All integrals in (6) are on the nonnegative half-line. Evenness makes
the A(1)-weighted first-derivative traces zero, including after the other
D operator acts. Also \(T(0,0)=0\), the two faces agree, and
\[
 f(u):=T(0,u)=\tfrac12u^2e^{(\lambda-v/2)u^2}\cos(Xu).
\]
Consequently the usable formula is
\[
 \boxed{A_0=\frac1{64}\left[
 \iint\psi(p)\psi(q)D_pD_qT(p,q)\,dp\,dq
 +\int\psi(u)(f''-f)(u)\,du\right].}                \tag{7}
\]
The second integral survives. Neither h_* nor Gaussian moment replacement
enters this calculation. This is exact integration by parts in the source
variables, distinct from integration by parts in the observation k.

There is also a useful closed expression for that boundary contribution.
Since f(0)=f'(0)=0, (3) gives
\[
 \frac1{64}\int\psi(f''-f)
 =-\frac1{16}H_{\lambda-v/2}''(X).                   \tag{7a}
\]
Thus it is a known curvature observation at a shifted time. It should not
be assumed small: as a resolving test approaches a hypothetical double
event with curvature a != 0, this term tends to -a/16, whereas A0 tends
to zero. The bulk term must retain its corresponding cancellation.

The transferred test can be kept compact. For a=p+q, b=p-q,
\[
 T=\tfrac14\{h(b)j(a)+h(a)j(b)\},\quad
 h(s)=s^2e^{\lambda s^2/2},\quad
 j(s)=e^{(\lambda-v)s^2/2}\cos(Xs),
\]
\[
 D_pD_q=\partial_a^4+\partial_b^4-2\partial_a^2\partial_b^2
       -2\partial_a^2-2\partial_b^2+1.               \tag{8}
\]
This gives all derivatives explicitly without differentiating the theta
sum again. The transformed quadrant is a >= |b|, with dp dq = da db / 2;
the factorization of the test does not make the integration domain a
product in a,b.

## 3. The lattice sum and what its rank means

The source weight in the double integral is now
\[
 \boxed{\psi(p)\psi(q)=e^{p+q}
 \sum_{m,n\ge1}\exp[-\pi(m^2e^{4p}+n^2e^{4q})].}     \tag{9}
\]
There are no remaining m², m⁴, n² or n⁴ polynomial factors in this
weight. The cost is the explicit fourth-order operator (8) on the
test and the single primitive boundary integral in (7).

For r=e^(2p), s=e^(2q), the arithmetic product is
\[
 A(r)A(s)=\sum_{m,n\ge1}e^{-\pi(m^2r^2+n^2s^2)}
 =\tfrac14\{\Theta(r)\Theta(s)-\Theta(r)-\Theta(s)+1\}.\tag{10}
\]
This is the positive-quadrant part of a Gaussian sum on Z² with diagonal
quadratic form diag(r²,s²). The two spatial radial Laplacians can be viewed
on R³ x R³, but that does not turn the arithmetic into a rank-six lattice.
Replacing either A by a full Z³ heat trace would change the source.

For an entirely radial version, put
\(\widehat T(r,s)=T(\log r/2,\log s/2)\),
\(\mathscr D_r=(2r\partial_r)^2-1\),
\(\widehat f(r)=f(\log r/2)\). Equation (7) becomes
\[
 A_0=\frac1{256}\int_1^\infty\!\int_1^\infty
 \frac{A(r)A(s)}{\sqrt{rs}}\mathscr D_r\mathscr D_s\widehat T(r,s)
 \,dr\,ds
 +\frac1{128}\int_1^\infty\frac{A(r)}{\sqrt r}
       \mathscr D_r\widehat f(r)\,dr.                \tag{11}
\]
The lattice reformulation is therefore literal, with explicit constants.

Poisson/modular transformation gives
\(\Theta(r)\Theta(s)=(rs)^{-1}\Theta(1/r)\Theta(1/s)\).
It is a candidate identity to use inside the complete signed expression,
not yet a sign theorem. The four terms in the braces of (10) must remain
combined for integration: their separate large-radius contributions need
not converge against this growing test. The log-radius time weight and
coupled cosine also remain. A standard Gaussian lattice identity alone
does not integrate that test away. These are specific costs of (7)–(11),
not an exclusion of a further useful lattice reorganization.

## 4. Convergence and complete tails

For r >= 1,
\[
 0<A(r)\le\frac{e^{-\pi r^2}}{1-e^{-3\pi r^2}},\qquad
 0<\psi(u)\le\frac{e^{u-\pi e^{4u}}}{1-e^{-3\pi}}.    \tag{12}
\]
The first bound uses n²-1 >= 3(n-1) for n >= 1. On compact real parameter
sets with v >= 0, every derivative of T used in the two integrations by
parts is bounded by
\(C(1+p+q)^6e^{L(p^2+q^2)}\), with finite C and
\(L=\max(0,\sup\lambda)\). Derivatives of psi have the same
double-exponential decay with extra fixed exponential/polynomial factors.
Thus all far-end boundary terms vanish, the integrals converge absolutely,
and the double sum can pass through the integral. This also justifies the
v downarrow 0 limiting check below. No finite theta prefix was substituted.

If a later calculation truncates (10), it can use
\[
 R_N(r):=\sum_{n>N}e^{-\pi n^2r^2}
 \le\frac{e^{-\pi(N+1)^2r^2}}{1-e^{-\pi(2N+3)r^2}}.   \tag{13}
\]
Writing A_N=A-R_N, the omitted product is bounded by
\(R_N(r)A(s)+A(r)R_N(s)\). Integrate this bound times the absolute
bulk test in (11), with coefficient 1/256; add the face bound with R_N
and coefficient 1/128. That pays the complete omitted terms. Such an
approximation evaluates the already-transferred canonical formula,
retaining its exact endpoint coefficient; A_N does not itself satisfy
the canonical reflection endpoint identity. No cutoff or numerical margin
is selected here.

## 5. Checks and the actual remaining sign question

As a normalization check, take lambda=X=0 and v downarrow 0. Then
\(T=(p^2+q^2)/2\), \(D_pD_qT=(p^2+q^2)/2-2\), and
\(f''-f=1-u^2/2\). With \(J_j=\int_0^\infty u^j\psi(u)\,du\),
equation (7) gives
\[
 A_0=\{J_0J_2-2J_0^2+J_0-J_2/2\}/64
 =\{(1/2-J_0)/8\}\{(2J_0-J_2)/8\}.
\]
These last factors are exactly \(\int\Phi\) and \(\int u^2\Phi\)
from (3), agreeing with \(H'(0)^2-H(0)H''(0)\).
The [small algebra check][check] additionally verifies the operator (8)
and the corner/face coefficients on separately even polynomial tests with
an elementary exponential primitive. [Execution record][record] is exact
rational algebra, not a theta numerical certificate or separate review.

The control screen concerns the premise actually used:

| Control family | What survives this transfer; what fails the canonical arithmetic input |
| --- | --- |
| Reflected smooth and positive-primitive controls | Positive Green primitives and the same normalized endpoint transfer can survive. Their primitive is not the complete unit-coefficient A in (10). |
| Euler-factor controls | Positive even source and an admissible Green transfer survive; the literal source/conductor and rank-one theta primitive change. |
| Weighted-square controls | An exponential square sum and its own IBP formula survive. Complete unit coefficients and full reflection fail; use their own boundary traces. |
| Finite-prime orbit controls | Square support and selected arithmetic identities can survive. Full canonical coefficients/reflection fail. |
| Atomic or compact finite-profile controls | Their own distributional or sufficiently regular transfer can be considered. They lack the full canonical source and theta profile; do not assume the same smooth primitive domains. |
| Normalized endpoint perturbations | Some shape/completion data survive; ordinary Dirichlet arithmetic and the unchanged full theta primitive fail. |
| Fixed amplitude with variable kernel | Even the literal primitive can survive, but the cosine/Newman test (5) changes. |
| Fractional-profile relaxation | It is not an integer physical zero divisor or the literal two-source integral (5). |

These are analytical premise checks against [controls12][controls], not
new numerical control replays. Failure of the exact arithmetic identity
does not by itself show failure of any future inequality. For example,
for any suitable positive source q,
\(\psi_q(u)=8\int_u^\infty\sinh(s-u)q(s)\,ds\) gives a positive
primitive; a positive rescaling can set \(\psi_q'(0)=-1/2\).
Thus primitive positivity plus boundary normalization alone cannot supply
the desired sign, as already explained in [Note73][ibp].

The gain established here is removal of square-index polynomial factors
from the source product. A useful subsequent estimate must control the
**sum of the bulk and face terms**, preserving arithmetic and oscillatory
cancellation. The earlier double-event diagnostic remains
\(A_0(\lambda_*-\epsilon,k_*,\epsilon)
=-\tfrac12|H''_{\lambda_*}(k_*)|^2\epsilon+E\), with the complete
curvature-dependent remainder from [Note09][n09]. No estimate in this
addendum contradicts that hypothetical signal. No comparison saving over
direct scalar analysis has been measured or proved; the direct baseline
may use exactly the same primitive identity.

## 6. Continuation and model changes

**Next conceptual question within B03:** can a joint theta-product or
modular identity simplify the complete pairing (7), including its face,
into a source-specific estimate with a useful signed remainder? Begin
with the explicit separated test and operator (8), rather than deriving
the scalar primitive again. Keep one specified joint lattice
reorganization in a subsequent bounded pass. Select a concrete domain
and signed consequence before numerical evaluation or an E09 contract.
If the transformation gives only another exact formula, record that
scope without inferring either a sign gain or a universal obstruction.

This addendum supplies the new input requested by the older
[Continuation10][continuation]; its completed r3 stop remains historical.
The suggested continuation model is **GPT-6 Astra**, following the
project's existing B03 conceptual routing (plan r3 recommends Astra/ultra).
The [official model description][model] identifies demanding reasoning
and research as uses; the recommendation here is the project's task
classification, not a measured model comparison. A later fixed proof or
calculation and assessment route to GPT-6.1 Sol under the existing plan.
No model setting is inferred, selected or changed by this note.

On a model change, retain the actual chat0007 capture and these source
links, record the new session's actual model/effort only when available,
read the [result index][results] and [avoid index][avoid] with their
specific arithmetic/control/joint-estimate entries above, and resume from
(7)–(13). This pass ends at exact representation and convergence scope;
E09/E10 are unissued, and no manuscript milestone or investigation closure
is asserted.

[radial]: ../../../../05_radial_theta_collision_geometry/notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[ibp]: ../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md
[n09]: ../../notes/09_TND_D_B03_GAUSSIAN_INTERFACE_AND_SIGNED_KERNEL_SCREEN_20261109.md
[continuation]: ../../notes/10_TND_D_AFTER_B03_CONTINUATION_AND_MODEL_CHANGE_20261109.md
[progress]: ../../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[check]: ../../numerics/b03_primitive_ibp_check.py
[record]: ../../numerics/02_TND_D_B03_PRIMITIVE_IBP_CHECK_20261109.json
[results]: ../../../../../../result-summaries/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[dlmf]: https://dlmf.nist.gov/20.7#E32
[model]: https://developers.openai.com/api/docs/models/gpt-6-astra
