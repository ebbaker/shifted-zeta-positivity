# CNV determinant transfer and theta differential closure

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

**Status: detailed explanatory continuation, with elementary derivations.** The suggested connection is a research question about transferring source-side signs. No new spectral positivity theorem, collision bound, or RH criterion is established. The recent concavity theorem is a preprint claim; its interval certificates have not been rerun here. The algebra below explains the mechanism and its relationship to our normalization; it is not an independent audit of that theorem.

This follows [Note01](01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md) and the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md). Read with the [result index](../../../../result-summaries/README.md), particularly [theta identities and scoped nonclosure](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly [target reformulations](../../../../avoid/01_restating_the_target.md), [separate bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). [Source inspection records](../references/03_DIFFERENTIAL_CLOSURE_SOURCES_20261101.md) preserve reading scope and external PDF receipts.

## 1. The precise reference and the proposed connection

The reference was specifically **Section 5 of Planat–Solé, Second-Level Concavity of the Riemann Xi Kernel, arXiv:2608.19160v1, 19 August 2026**. Its autonomous Jacobi system is equation (5.10), and its kernel factorization is (5.12). The differential closure is in a logarithmic **source coordinate**. It is neither an ODE for Xi as a function of frequency nor the auxiliary spatial evolution of Investigation05. The reference was not to Sra's Wronskian/finite sign-regularity work.

The suggested combination has two logically separate steps:

\[
\boxed{\text{exact theta differential relations}}
\ \longrightarrow\
\boxed{\text{a source-side signed inequality}}
\ \xrightarrow{\text{proved transfer identity}}\
\boxed{\text{an integrated inequality}}.
\]

CNV supplies a successful transfer for normalized moments. The Jacobi system supplies relations among derivatives of the actual theta source. Our unanswered question is whether an appropriately chosen relation survives the integration required by a primitive pairing or a correlation. Putting the two papers beside one another does not supply that transfer.

## 2. Separate the variables and objects

Write
\[
\theta_3(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r},\qquad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Our half-line and completed primitives are
\[
p(u)=\tfrac12e^u[\theta_3(e^{4u})-1],\quad u\ge0,
\qquad
G(u)=\cosh u-\tfrac12e^u\theta_3(e^{4u}).
\]
They satisfy \(p''-p=8\Phi\) and \(p'(0)=-1/2\). CNV instead uses
\[
S(x)=\Phi(\sqrt{x}),\qquad K(x)=\int_x^\infty S(v)\,dv.
\]
Thus \(K\) is not \(p\) or \(G\). Below \(L=\log r=4u\), while \(x=u^2=L^2/16\). Heat time is denoted \(\tau\), and frequency \(z\):
\[
H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du.
\]
The variable \(a\) in the following ODE is the paper's theta state, not our usual spectral frequency.

## 3. What closes, and why

Jacobi's classical nonlinear third-order equation, reproduced in [Romik, Section 6, equation (28)](https://arxiv.org/html/1807.06130v2), is
\[
(Y^2Y'''-15YY'Y''+30(Y')^3)^2
+32(YY''-3(Y')^2)^3
=\pi^2Y^{10}(YY''-3(Y')^2)^2,
\]
where \(Y(r)=\theta_3(r)\) and these derivatives are with respect to \(r\). This is a restrictive identity relating derivatives, not merely positivity or concavity of a function.

Now set
\[
A(L)=\pi e^L\theta_3(e^L)^4,\quad a=A'/A,
\quad U=2a'+1-a^2,
\quad V=a''+a^3-3aa'-a.
\]
From here primes mean \(L\)-derivatives. The theta identity
\[
U=\pi^2e^{2L}\theta_2(e^L)^4\theta_4(e^L)^4>0
\]
justifies defining \(\chi=V/U\). In this notation Jacobi's equation reduces to
\[
4(V^2+U^3)=A^2U^2,\qquad A^2=4(U+\chi^2),
\]
and the differential equations become
\[
\boxed{a'=\tfrac12(U+a^2-1),\qquad U'=2U(a+\chi),\qquad\chi'=a\chi-U.}
\tag{1}
\]
These are [Planat–Solé (5.5)–(5.10)](https://arxiv.org/html/2608.19160v1#S5.SS1). The distinguished initial data are
\[
a(0)=\chi(0)=0,\qquad U(0)=\frac{\Gamma(1/4)^8}{64\pi^4}.
\tag{2}
\]

The first equation follows from the definition of \(U\). For the second, direct differentiation gives \(U'=2V+2aU\). Differentiating \(A^2=4(U+\chi^2)\), using \(A'=aA\), gives the third away from zeros of \(\chi\); the actual analytic theta solution extends it through those zeros. Modular reflection makes \(A,U\) even and \(a,\chi\) odd, selecting the data at zero.

The meaning of **closure** is precise: once the three state values are known, their next derivatives are determined by those same values. Differentiation of any polynomial or rational expression in the state stays in the same differential algebra. The expressions become more complicated, but no independent new theta derivative needs to be introduced at each step. Arbitrary initial data do not describe the canonical theta function.

To connect this directly to our source, put
\[
B(L)=e^{L/4}\theta_3(e^L)=(A/\pi)^{1/4},\qquad
Q=U+\tfrac32(a^2-1).
\]
Then
\[
\boxed{\Phi(L/4)=\tfrac18 B(L)Q.}
\tag{3}
\]
Indeed \(B'/B=a/4\), and
\[
p(u)=\tfrac12[B(4u)-e^u],\qquad
p''-p=\tfrac12B(4u)(4a'+a^2-1)=B(4u)Q.
\]
The same state gives \(G(u)=\cosh u-B(4u)/2\).

There is an explicit derivative recurrence. Define the vector field
\[
\mathcal D=\tfrac12(U+a^2-1)\partial_a
+2U(a+\chi)\partial_U+(a\chi-U)\partial_\chi,
\]
and let
\[
Q_0=Q,\qquad Q_{j+1}=\mathcal DQ_j+\tfrac a4Q_j.
\]
Then
\[
\Phi^{(j)}(u)=\frac{4^jB(4u)}8Q_j(a(4u),U(4u),\chi(4u)).
\tag{4}
\]
For example,
\[
Q_1=\tfrac{15}4aU+2U\chi+\tfrac{15}8(a^3-a).
\]
This is the practical content of the closure. A complete differential expression in \(\Phi\) can be rewritten before estimating its pieces. Formula (3) also cautions against assuming a numerical gain: at large \(L\), its factors contain severe cancellation. The positive tail of \(p\) is similarly recovered by subtracting the leading exponential in its formula.

The repository's exclusion of a finite homogeneous **linear rational-coefficient frequency ODE for H** does not exclude (1). The variables, nonlinearity and object are different; see [result summary14](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md).

## 4. How a derivative identity can become a sign proof

Define the differential Laguerre operation
\[
\mathcal L[f]=(f')^2-ff''=-f^2(\log f)''
\]
for positive \(f\). Classical first-level concavity is \(\mathcal L[S]>0\). The recent preprint reports
\[
(\log\mathcal L[S])''<0,
\quad\text{equivalently}\quad\mathcal L[\mathcal L[S]]>0.
\tag{5}
\]
These derivatives are in \(x\), not frequency. Also distinguish iterating \(\mathcal L\) from the generalized spectral Laguerre hierarchy; [Craven–Csordas (2002), Introduction and Theorem2.2](https://math.hawaii.edu/~tom/mathfiles/iteratedLT.pdf) explicitly separates these constructions.

Here is the chain-rule calculation exposing the complete signed expression. Let
\[
g(L)=\log\Phi(L/4),\quad P=g',\quad P_j=g^{(j+1)},\quad W=P/L-P_1.
\]
Since \(d/dx=(8/L)d/dL\),
\[
(\log S)''=-\frac{64}{L^2}W,\qquad
\mathcal L[S]=\frac{64}{L^2}S^2W.
\]
In particular \(W>0\) is first-level concavity. Using \(W'=-W/L-P_2\) gives
\[
\boxed{(\log\mathcal L[S])''
=\frac{64}{L^2}\left[\frac6{L^2}-2W-\frac{P_3}{W}-\frac{P_2^2}{W^2}\right].}
\tag{6}
\]
All the \(P_j\) can be generated from (1), (3) and (4). The explicit \(1/L\) comes from changing to \(x=L^2/16\); it must not be dropped. The source is regular at zero, but these normalized coordinates are singular there.

For comparison with the paper, normalize
\[
C=-P^2/P_1,\quad\alpha=PP_2/P_1^2,\quad
\beta=P^2P_3/P_1^3,\quad\delta=W/(-P_1).
\]
On the canonical trajectory \(P,P_1<0\), \(0<\delta<1\). Multiplying the bracket in (6) by the positive factor \(P^2\delta^2/P_1^2\) yields
\[
\mathcal F=6\delta^2(1-\delta)^2-2C\delta^3+\beta\delta-\alpha^2.
\tag{7}
\]
The shear \(\widetilde\beta=\beta+6\delta-(12+2C)\delta^2+6\delta^3\) writes this as \(\mathcal F=\delta\widetilde\beta-\alpha^2\). Thus the boundary is a quadratic cone in moving coordinates. This is an algebraic equality surface for source curvature, not a physical collision surface.

The useful general barrier principle is elementary. Start in \(\mathcal F<0\); prove that the derivative of \(\mathcal F\) is strictly negative at every possible first boundary contact. A first exit would instead require a nonnegative derivative there, giving a contradiction. This keeps the signed expression intact. Merely bounding each derivative separately or plotting the trajectory would not establish the barrier.

[Planat–Solé Sections5.4–5.7](https://arxiv.org/html/2608.19160v1#S5.SS4) implement this with a local modular certificate, a compact first-contact argument and a subsequent monotonicity estimate. Theta-term/tail bounds still enter the coefficient enclosures. The argument is therefore not supplied by the autonomous ODE alone. Selected algebra and proof architecture were read; certificates and the complete theorem remain unaudited here.

## 5. What CNV actually transfers

For ordered \(x_1<x_2\), \(y_1<y_2\), strict log-concavity of \(K\) gives
\[
\det[K(x_i+y_j)]_{i,j=1}^2<0.
\tag{8}
\]
The negative sign matters: this is reverse order-two regularity of a sum kernel, not positivity of a Gram matrix.

Define
\[
f_s(u)=\frac{u^{s-1/2}}{\Gamma(s+1/2)},\quad s>-1/2,
\qquad M(q)=\frac1{\Gamma(q+1)}\int_0^\infty w^qK(w)\,dw.
\]
The beta integral gives
\[
\int_0^w f_s(u)f_t(w-u)\,du
=\frac{w^{s+t}}{\Gamma(s+t+1)},
\]
so
\[
M(s+t)=\int_0^\infty\!\int_0^\infty
f_s(u)K(u+v)f_t(v)\,du\,dv.
\tag{9}
\]
Ordered minors of the power kernel \(f_s(u)\) are positive. The continuous determinant-composition identity applied twice therefore preserves the negative order-two sign from (8), proving strict log-concavity of \(M\). This is the mechanism of [CNV, Lemmas2.2–2.3 and Proposition2.4](https://www.math.kent.edu/~varga/pub/paper_157.pdf).

The normalization can be checked directly in our notation. With
\[
b_m=\int_0^\infty u^{2m}\Phi(u)\,du,\qquad
\gamma_m=\frac{m!}{(2m)!}b_m,
\]
the substitution \(x=u^2\) and one integration by parts give
\[
b_m=\frac{2m-1}{4}\int_0^\infty x^{m-3/2}K(x)\,dx,
\qquad
\gamma_m=\frac{\sqrt\pi}{2\,4^m}M(m-3/2),\quad m\ge1.
\tag{10}
\]
Thus log-concavity of \(M\) proves \(\gamma_m^2>\gamma_{m-1}\gamma_{m+1}\) for \(m\ge2\). The first index is handled separately in CNV; (10) must not be used at \(m=0\). Unnormalized moments are log-convex by Cauchy–Schwarz. The gamma normalization and the kernel in (9) do essential work.

## 6. A closer bridge already exists in the 1988 follow-up

[Csordas–Varga, Moment Inequalities and the Riemann Hypothesis](https://www.math.kent.edu/~varga/pub/paper_161.pdf), Theorem2.1, proves strict log-concavity of \(S\). Proposition2.2 gives a particularly relevant signed double-integral identity; Theorem2.4 includes all-real-heat-parameter Turán inequalities. Printed pp.175,177–178,180–181 were inspected visually in this continuation.

For the pure heat-weighted source \(\Psi_\tau(u)=e^{\tau u^2}\Phi(u)\), put
\[
b_m(\tau)=\int_0^\infty u^{2m}\Psi_\tau(u)\,du,
\qquad q_\tau(u)=-\frac{\Psi_\tau'(u)}{u\Psi_\tau(u)}.
\]
Then \(q_\tau'(u)>0\), since
\[
q_\tau(u)=-2\tau-2(\log S)'(u^2),\qquad
q_\tau'(u)=-4u(\log S)''(u^2).
\]
For \(m\ge1\), integration by parts and symmetrization give
\[
\begin{aligned}
&2(2m+1)\left[b_m(\tau)^2-\frac{2m-1}{2m+1}b_{m-1}(\tau)b_{m+1}(\tau)\right]\\
&=\int_0^\infty\!\int_0^\infty
u^{2m}v^{2m}\Psi_\tau(u)\Psi_\tau(v)
(v^2-u^2)[q_\tau(v)-q_\tau(u)]\,du\,dv>0.
\end{aligned}
\tag{11}
\]
Both differences have the same sign. One can verify the identity by expanding: its two diagonal terms are each \((2m+1)b_m^2\), and its two cross terms are each \(-(2m-1)b_{m-1}b_{m+1}\). The boundary terms vanish for this source. This is an existing successful example of retaining the complete signed interaction through integration.

It also supplies a useful limitation on the proposed direction. If \(S_\tau(x)=e^{\tau x}S(x)\), then
\[
(\log S_\tau)''=(\log S)'',\qquad
\mathcal L[e^{\tau x}f]=e^{2\tau x}\mathcal L[f].
\tag{12}
\]
Consequently second-level source concavity, if true at zero, is unchanged by every real heat parameter. More generally \(\mathcal L^{\circ k}[S_\tau]=e^{2^k\tau x}\mathcal L^{\circ k}[S]\). This is an elementary covariance identity, not an assertion that all such iterates are positive. It shows why these source-shape conclusions alone cannot locate the physical heat threshold. The full canonical theta state contains more information than the concavity inequality extracted from it.

There is also a simple link back to CNV's tail. For decreasing strictly log-concave \(S\), let \(h=-S'/S>0\). The tangent-line bound gives \(K(x)<S(x)/h(x)\), whence
\[
(K')^2-KK''=S^2-hSK>0.
\]
This recovers a known tail property. It is a worked example of sign transfer, not new progress beyond the classical theorems.

## 7. What remains missing for our spectral or primitive questions

Our first spectral Laguerre expression has the exact correlation form
\[
H_z(0,z)^2-H(0,z)H_{zz}(0,z)
=\int_{\mathbb R}\mathcal K_1(v)\cos(2zv)\,dv,
\quad
\mathcal K_1(v)=\int_{\mathbb R}u^2\Phi(u+v)\Phi(u-v)\,du.
\tag{13}
\]
The source correlation is positive pointwise. What would sign its Fourier transform is positive definiteness, for example a justified autocorrelation/Gram representation with the needed convergence. Neither positivity nor source concavity implies this. The all-order associated-kernel characterization is an RH-equivalent reformulation, as recorded in the opening note; it is not a new criterion being proposed here.

Two concrete obstacles prevent an automatic combination of (1) and (9).

First, the cosine kernel lacks the fixed ordered determinant sign used by CNV. At frequencies \(0,1\), the source points \(0,\pi\) give determinant \(-2\), whereas \(\pi,2\pi\) give \(+2\). This blocks that direct determinant-composition argument for the raw cosine kernel; it does not exclude a transformed representation or a signed cancellation identity.

Second, local nonlinear differential closure need not survive integration. Equation (13) contains two shifted copies of the state. Their derivatives close pointwise in a doubled state, but integration introduces mixed products, and generally \(\int UV\ne(\int U)(\int V)\). Differentiating the correlation may therefore generate new mixed integrals rather than a finite autonomous system. A separate exact identity, factorization, or inequality is required to control them.

Investigation05 already supplies the precise primitive transfer
\[
\int_0^\infty\Phi(u)f(u)\,du
=\frac{f(0)}{16}+\frac{p(0)f'(0)}8
+\frac18\int_0^\infty p(u)[f''(u)-f(u)]\,du.
\tag{14}
\]
[Note73](../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md) retains both endpoints. [Note75](../../05_radial_theta_collision_geometry/notes/75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md) pays the transported-test derivative and trace costs in its prepared class. The unresolved issue is a favorable complete signed comparison, not the mere existence of those derivatives. Positivity of \(p\) cannot sign an arbitrary \(f''-f\).

The possible benefit of (1) is to constrain the interacting derivative terms before replacing them by independent upper bounds. Whether those constraints help the actual test in (14) is unproved. The source coordinate \(L\) must remain distinct from the auxiliary spatial time in Investigation05; conserved flows and the cone in (7) do not establish physical noncollision by analogy.

## 8. A bounded continuation question

The next useful derivation would select one complete correlation or primitive pairing and ask whether the Jacobi relations produce an **integrable signed identity** analogous to (11), with every endpoint retained. Success would mean a new factorization or inequality on a declared domain, beyond the already known coefficient inequalities. Rewriting the same unknown sign in theta coordinates would only change its description.

This note adopts no new estimate and performs no new control or numerical campaign. Before promoting any resulting estimate, test its precise premises against the [registered controls](../../../../result-summaries/12_collision_controls_and_screening.md). Canonical initial data can identify theta by ODE uniqueness, but source identification is not the missing quantitative sign proof. Conversely, a weakened positivity or concavity consequence may still admit colliding controls. The discriminating premise must be exhibited, not inferred from the presence of theta notation.

The methodological suggestion is therefore specific: **use theta differential identities to retain correlations among derivatives, and require a separate sign-preserving integral identity before claiming an integrated consequence.** CNV and its 1988 follow-up show what a successful transfer looks like. The recent Jacobi reduction offers an additional way to organize the source information. The corresponding transfer for our spectral or feedback expression is still an open derivation task.
