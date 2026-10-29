# Integration by parts from the theta primitive to feedback pairings

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0031**, *Continue CTF-B02 Astra assessment*.

**Status: analytical bridge and conceptual continuation.** Edward Baker
identified integration by parts as an original reason for the
three-dimensional realization. The book's primitive identity applies to
the current prepared densities through their test functions. The exact
transfer below retains the initial unit-sphere terms and all effects of
the evolving inner ball. It establishes no improved estimate or collision
exclusion. The scalar positive-time formula is already in Note12; it is
not a new result of this discussion.

## 1. What the book makes available

The [book, Sections 1–2][book] gives, for r=e^(2u),
\[
 A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
 \Theta=1+2A,\qquad
 \Phi(u)=\tfrac12r^{5/2}\Delta_3A(r).
\]
Dimension three matches the source coefficients and the Kelvin weight.
With V=1+r^(-1)-Theta, Green's identity transfers the Laplacian from
Theta to the power kernel. The resulting scalar identity is the classical
theta–Mellin representation, with its endpoint contributions combined.
[Note35][n35] identifies the normalization. Riemann's theta sum, reflection
and differentiated-source formulas appear together on printed p.3 of the
[Wilkins translation][riemann]; [DLMF 25.5.13–14][dlmf] gives the split
theta integral. Those passages were checked again for this discussion.

The full-space V integral converges in its stated Mellin strip at t=0.
Multiplication by e^(tu²) for t>0 cannot simply be inserted into that
formula: V's algebraic tails, or the associated generator's exponential
tails, no longer suffice. The rapidly decaying half-line primitive avoids
that problem. Set
\[
 p(u)=e^uA(e^{2u}),\quad u\ge0.
\]
Then
\[
 p''-p=8\Phi,\qquad p(0)=A(1),\qquad p'(0)=-\tfrac12. \tag{1}
\]
The endpoint derivative follows from theta reflection. For a C² function
f whose growth and derivatives are dominated by the complete theta tail,
two integrations by parts give
\[
 \boxed{\int_0^\infty\Phi f\,du
 =\frac{f(0)}{16}+\frac{A(1)f'(0)}8
   +\frac18\int_0^\infty p(f''-f)\,du.} \tag{2}
\]
Indeed the integrated boundary is [p'f-pf'] from zero to infinity;
its lower endpoint supplies both displayed terms. Polynomial growth in
r=e^(2u), with any fixed Gaussian exponential in u, is admissible.

For f=e^(tu²)cos(au), (2) is precisely the scalar version of
[Note12, equations (14)–(16)][n12]:
\[
 H(t,a)=\frac1{16}+\frac18\int_0^\infty p(u)e^{tu^2}
 \left[(2t-1-a^2+4t^2u^2)\cos(au)-4tau\sin(au)\right]du. \tag{3}
\]
The constant, the mixed sine term and the t² term are essential. At t=0,
this reduces to the book's entire companion formula. The identities
extend in the physical parameters by the complete tail domination.

## 2. Transfer with a spatial test function

Let F_j^raw be the actual j-th frequency derivative of the current raw
density:
\[
 F_j^{\rm raw}(X)=\mathbf1_{r\ge1}
 \frac{e^{tu^2}\Phi(u)}{8\pi r^3}
 u^j\cos^{(j)}(au),\qquad u=\tfrac12\log r.
\]
For a smooth radial test chi, held fixed when differentiating in a, put
\[
 f_j(u)=e^{tu^2}u^j\cos^{(j)}(au)\chi(e^{2u}).
\]
The Euclidean Jacobian gives
\[
 \langle F_j^{\rm raw},\chi\rangle
 =\frac{f_j(0)}{16}+\frac{A(1)f_j'(0)}8
  +\frac18\int_0^\infty p(f_j''-f_j)\,du. \tag{4}
\]
For j=0 its boundary contribution is
\[
 \frac{\chi(1)}{16}+\frac{A(1)}4\chi_r(1). \tag{5}
\]
For j>=1 both boundary values vanish. In particular the first derivative
contains -u sin(au), whose value and first u-derivative vanish at zero.

There is a second, direct check of (4)–(5). For j=0 put
k(r)=r^(-1/2)e^(tu²)cos(au)chi(r). The radial Green identity is
\[
 \langle F_0^{\rm raw},\chi\rangle
 =\frac14\int_1^\infty A(r)\Delta_3k(r)r^2\,dr
  +\frac14\{-A'(1)k(1)+A(1)k'(1)\}. \tag{6}
\]
Using A'(1)=-A(1)/2-1/4 gives exactly (5). The two derivations
check the sign and normalization of the initial sphere contribution.

## 3. The unchanged conservative flow fits this identity

Fix an actual feedback path on a compact interval inside its lifespan.
Let P_(s,0) be the common propagator for the density and its frequency
derivatives, and K_1 the existing unit heat preparation. For an admissible
smooth radial terminal test eta,
\[
 J_j(s)=P_{s,0}K_1F_j^{\rm raw},\qquad
 \langle J_j(s),\eta\rangle
 =\langle F_j^{\rm raw},\chi_s\rangle,\qquad
 \chi_s=K_1P_{s,0}^*\eta. \tag{7}
\]
The spatial adjoint of Delta+alpha div(v·) is Delta-alpha v·grad.
Equation (7) follows from duality and self-adjointness of K_1; (4) then
applies whenever chi_s and its derivatives satisfy the stated growth
condition. Smooth compact terminal tests on a compact regular interval
are the intended starting class. Any wider or uniform test class requires
its own bounds.

This evaluates the whole-space pairing at time s. The appearance of
r>=1 in (4) refers only to the raw initial support; propagation through
the ball has already entered chi_s. No boundary condition is imposed on
the evolved sphere. No claim is made that A, V, or p themselves satisfy
the feedback equation, or that its source residual disappears. The common
path is frozen exactly as in the manuscript; differentiating a feedback
path separately would be a different operation.

The price is visible. Writing c=e^(tu²)cos(au) and
b(u)=chi_s(e^(2u)),
\[
 (cb)''-cb=(c''-c)b+2c'b'+cb''. \tag{8}
\]
Thus derivative costs move to the complete transported test, including
its first two derivatives and the trace in (5). Dropping those terms
would manufacture an advantage.

## 4. Comparison and collision controls

This is a faithful interface, not a proposed exclusion criterion. For
eta=1, conservation gives chi_s=1 and (7) returns only the scalar formula
(3). An equally informed direct method may use the same integration by
parts. No information advantage follows merely from introducing p.

The Green construction also supplies a precise control check. For any
positive source q on the half-line with the required exponential moments,
\[
 p_q(u)=8\int_u^\infty\sinh(v-u)q(v)\,dv>0,
 \quad p_q''-p_q=8q,\quad
 p_q'(0)=-8\int_0^\infty\cosh(v)q(v)\,dv. \tag{9}
\]
Take the book's Gaussian-polynomial colliding source, and rescale it by
a positive constant so that its last integral is 1/16. Then p_q'(0)=-1/2,
and (2) has the same constant term while the double zero persists.
Positivity of the primitive and the integration-by-parts structure alone
therefore do not exclude this control. It lacks the unchanged complete
theta primitive A. Likewise the fixed-A polynomial observation controls
still satisfy (2) for their own tests; they fail the literal cosine
equation used in (3). These are distinct failed premises, not one universal
control obstruction. The other families retain the scopes in the
[control register][controls].

## 5. Continuation and model handoff

The author's suggestion sharpens the next conceptual comparison: use
the undifferentiated complete theta primitive inside a specific evolving
pairing **before** applying separate absolute bounds. Select one term in
the current energy or residual production, specify the needed test class,
and compare the complete transfer with the strongest direct estimate
using the same source and test information. A useful return would improve
an unpaid bound or identify the precise derivative or boundary cost that
prevents improvement. No such bound is supplied by (4) alone.

Read this note alongside [Continuation72][n72]; it supplements that
handoff without replacing the accepted uniform-feedback theorem or
selecting a new flow. B02 remains partial; no E07/E08 proof packet or
numerical acquisition is issued. Both manuscript sources remain unchanged.
On a model change, preserve chat0031 and its existing history identity,
verify the newly recorded model/effort, and begin with (4)–(8), not a
rederivation of the classical scalar transform. These calculations have
same-assistant analytical checks only.

The [result index][results], particularly [geometric realizations][geometry],
and [pattern index][avoid], particularly [target restatement][a01] and
[separate bounds][a12], govern the scope. The exact identities organize
information; their quantitative benefit remains the question to test.

[book]: ../book/main.tex
[n12]: 12_FLAT_QUATERNION_DIRAC_AND_DYADIC_LATTICE_H_20261027.md
[n35]: 35_CLASSICAL_THETA_MELLIN_ATTRIBUTION_20261028.md
[n72]: 72_ANALYTICAL_MANUSCRIPT_AND_MODEL_CONTINUATION_20261029.md
[riemann]: https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf
[dlmf]: https://dlmf.nist.gov/25.5#E13
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
