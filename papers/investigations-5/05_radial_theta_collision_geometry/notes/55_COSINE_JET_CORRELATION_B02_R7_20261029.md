# CTF-B02 R7: a quantitative cosine first/second-jet correlation

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0026**, **Continue radial theta collision research**.

**Status: proved in-note with same-assistant analytical checks.** At the
single frozen mark \(p=(T,A)=(1/4,2)\), the literal theta/cosine data give
\[
\boxed{\|2J_{2,0}-V_0\|_2\le\frac{12}{13}\|J_{2,0}\|_2.}
\tag{1}
\]
This meets the predeclared target with a strict constant below one. It
improves a supporting second-jet energy allowance at the same actual
compression \(B\); it does not independently bound B, improve a collision
deadline, or enlarge a collision-free domain. No specialist, separate-model
or formal verification has occurred. [Self-assessment29][review] records
the checks; [Progress05][progress] owns live status.

| Next task | Type and recommended model | Dependency and bounded output |
| --- | --- | --- |
| **CTF-E08 R7 — default** | **E — Sol:** proof, constants and comparison are fixed | Ready; assess the [frozen packet][packet], return one supported verdict |
| CTF-B02 | B — Astra: independent compression control is still conceptual | Parent partial; no second candidate selected in R7 |
| CTF-E03 / CTF-B03 | E — Sol / B — Astra | Still gated; no numerical acquisition or coverage request |

## 1. Frozen question, class and comparison

The R7 intake in Progress05 was saved before testing. It fixes the mark
(1/4,2), the complete source, unit preparation, unchanged feedback, and
the target \(\|C_0\|_2\le\|J_{2,0}\|_2\), where \(C=AJ_2-V\).
C is only a supporting linear combination of the existing actual jets;
it changes neither the feedback nor the existing functional
\(\mathcal F=G+\|\omega\mathcal R\|_2^2+\|J_2\|_2^2\).

Use [Notes28][n28], [31][n31], [40][n40] and [47][n47]. Write
\[
q(u)=e^{u^2/4}\Phi(u),\quad M_j=\int_0^\infty u^j q(u)\,du,
\quad \rho(X)=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},\quad
u=\tfrac12\log r.
\]
Thus \(4\pi r^2\rho\,dr=q\,du\). Let \(S=K_1*\),
\(K_t(X)=(4\pi t)^{-3/2}e^{-|X|^2/(4t)}\), and
\[
F_0=\rho\cos(2u),\quad F_1=-\rho u\sin(2u),\quad
F_2=-\rho u^2\cos(2u),\quad (U_0,V_0,J_{2,0})=S(F_0,F_1,F_2).
\tag{2}
\]
All multipliers in (2) act on raw exterior data before smoothing.
Subsequent propagation is by the common fixed-mark path \(\mathcal P_s^p\).
In particular \(J_{2,s}=-\mathcal P_s^p S(u^2F_0)\), not \(-u(X)^2U_s\).

The equations and quantities retained are
\[
L_s=\Delta+\alpha(s)\operatorname{div}(v\,\cdot),\quad
v=X+\frac{X}{1+r^2},\quad d=\operatorname{div}v\le6,
\]
\[
W=(U,V),\quad E_0=\|W_s\|_2^2>0,\quad
G=\|\nabla W_s\|_2^2,\quad \alpha=\frac{2G}{\int d|W_s|^2},
\quad B(s)=\int_0^s\alpha,\quad Q(s)=\|J_{2,s}\|_2^2.
\tag{3}
\]
The comparison is with \(Q(s)\le Q_0e^{6B(s)}\), obtained from the
same homogeneous jet equation and d<=6. The intended gain is a smaller
upper allowance on an explicitly stated B range, not a smaller growth
exponent or an assertion about the actual asymptotic behavior of Q.
This is a numerical-constant milestone under [avoid01][a01], not another
regularity reformulation. The [result index][results], [control cluster][controls],
[spatial-flow cluster][theta-results], [avoid index][avoid] and
[scope rule][a07] govern its interpretation.

## 2. A complete-source fourth/second-moment bound

Every theta summand is positive on u>=0. Set
\[
q_n(u)=\pi n^2 e^{5u}(x-3)e^{-x/2+u^2/4},\qquad
x=2\pi n^2e^{4u},\qquad q=\sum_{n\ge1}q_n.
\]
For \(\ell_n=\log q_n\), direct differentiation gives
\[
\ell_n'=9+\frac{12}{x-3}-2x+\frac u2,\qquad
\ell_n''=\frac12-8x-\frac{48x}{(x-3)^2}.
\tag{4}
\]
For x>=6 and y=x-6,
\[
\left(8x+\frac{48x}{(x-3)^2}-75\right)(x-3)^2
=8y^3+21(y-1)^2+24\ge0.
\tag{5}
\]
Thus \(\ell_n''\le-149/2<-74\). The elementary bound
\(\pi>25/8\), and monotonicity of \(9+12/(x-3)-2x\), give
\[
\ell_n'(0)\le9+\frac{48}{13}-\frac{25}{2}
=\frac5{26}<\frac15.
\]
Consequently \(q_n'\le(1/5-74u)q_n\) for every n, and summing gives
\[
q'(u)\le(1/5-74u)q(u).
\tag{6}
\]
We sum this first-derivative inequality; we do not infer log concavity
of a sum from log concavity of its summands. All source terms remain.
Termwise differentiation is justified locally by the Gaussian square
tail; polynomially weighted derivatives are integrable at infinity by
the full double-exponential decay, as in Note40. Hence all moments below
are finite, and \(u^3q\) vanishes at both endpoints.

Integrating \((u^3q)'\), then using (6) and Cauchy--Schwarz, yields
\[
74M_4\le3M_2+\tfrac15 M_3
\le3M_2+\tfrac15\sqrt{M_2M_4}.
\tag{7}
\]
For \(z=M_4/M_2>0\), the function \(74z-\sqrt z/5\) is increasing
on z>=1/24. At z=1/24 its value exceeds
\(37/12-1/20=91/30>3\). Equation (7) therefore proves
\[
\boxed{M_4<\frac1{24}M_2.}
\tag{8}
\]
No numerical quadrature, finite-square replacement or fitted moment
ratio is involved. For an elementary check of the only pi lower bound,
\(\pi/4=\arctan(1/2)+\arctan(1/3)\); integrating
\(1/(1+t^2)\ge1-t^2+t^4-t^6\) at those two endpoints gives a sum
greater than 25/32. This supplies \(\pi>25/8\) independently of a
decimal approximation.

## 3. The oscillator remainder survives the true preparation

For real x,
\[
\sin x-x\cos x=\int_0^x t\sin t\,dt,\qquad
|\sin x-x\cos x|\le |x|^3/3.
\tag{9}
\]
The actual raw difference at A=2 is
\[
2F_2-F_1=\rho u\{\sin(2u)-2u\cos(2u)\},
\quad |2F_2-F_1|\le\tfrac83\rho u^4.
\]
Let \(c_K=\|K_1\|_2=(8\pi)^{-3/4}\). Young's inequality and (8) give
\[
\|C_0\|_2=\|S(2F_2-F_1)\|_2
\le c_K\tfrac83M_4\le c_K\tfrac19M_2.
\tag{10}
\]
For a lower bound on the *prepared* J2, use precisely the fixed Gaussian
test K1, rather than a raw L2 norm. Self-adjointness and K1*K1=K2 give
\[
\langle J_{2,0},K_1\rangle=-(8\pi)^{-3/2}I,
\quad I=\int_0^\infty u^2q(u)e^{-e^{4u}/8}\cos(2u)\,du.
\tag{11}
\]
Put \(w(u)=e^{-e^{4u}/8}\cos(2u)\). The following three bounds pay
for the entire oscillatory tail:

- For 0<=u<=1/2, \(\cos(2u)\ge1/2\), \(e^{4u}\le e^2<8\) and
  \(e^{-1}>1/3\), so w>=1/6.
- For 1/2<=u<=3/4, \(2u\le3/2<\pi/2\), so w>=0.
- For u>=3/4, \(e^{4u}\ge e^3>16\), so w>=-e^{-2}>-1/4.

The elementary bounds \(8/3<e<11/4\) follow from its exponential
series and imply all the e bounds just used. With no sign restriction
on the last interval, Markov's moment bounds now yield
\[
\begin{split}
I&\ge\tfrac16\left(M_2-\int_{1/2}^\infty u^2q\right)
       -\tfrac14\int_{3/4}^\infty u^2q\\
 &\ge\tfrac16M_2-\left(\tfrac46+\tfrac4{9}\right)M_4
 \ge\frac{13}{108}M_2>0.
\end{split}
\tag{12}
\]
These are scalar input-variable partitions, not spatial boundaries or
changes to the PDE. Cauchy--Schwarz in (11) gives
\[
\|J_{2,0}\|_2\ge c_K I\ge c_K\frac{13}{108}M_2.
\tag{13}
\]
Dividing (10) by (13) proves (1); in particular Q0>0. Both sides refer
to exactly one unit of preparation, over the whole of R3.

## 4. Same-path energy gain and its explicit range

With the mark and its alpha path fixed, both V and J2 solve the same
homogeneous equation. Hence \(C_s=L_sC\), with no mark derivative of
alpha and no new feedback. On every compact lifespan interval,
\[
\frac d{ds}\|C\|_2^2=-2\|\nabla C\|_2^2+
\alpha\int d|C|^2\le6\alpha\|C\|_2^2.
\tag{14}
\]
Prepared Schwartz regularity and the inherited weighted decay justify
the whole-space integrations. The same calculation applies to J2.
Write \(X(s)=Q_0e^{6B(s)}>0\). The identity 2J2=V+C and E=E0 give
\[
\boxed{Q(s)\le\min\{X(s),\,\mathcal U_{\rm corr}(s)\},\quad
\mathcal U_{\rm corr}(s)=
\left(\frac{\sqrt{E_0}}2+\frac6{13}\sqrt{X(s)}\right)^2.}
\tag{15}
\]
The weaker Young form selected at intake is also valid:
\[
Q(s)\le\frac{E_0}{2}+\frac{72}{169}X(s)
\le\frac{E_0+X(s)}2.
\tag{16}
\]
For the stronger comparison (15),
\[
\frac{\mathcal U_{\rm corr}}{X}
=\left(\tfrac12\sqrt{E_0/Q_0}\,e^{-3B}+\tfrac6{13}\right)^2<1
\quad\Longleftrightarrow\quad
B>B_c:=\frac16\log\frac{169E_0}{196Q_0}.
\tag{17}
\]
The threshold is finite and strictly positive. Indeed (1) implies
\(\|V_0\|_2\ge(14/13)\|J_{2,0}\|_2\), and U0 is nonzero by
Gaussian injectivity, so \(E_0>(196/169)Q_0\). No early-time improvement
is asserted. The minimum in (15) keeps the old bound before the crossing.
As an algebraic function of B, the ratio in (17) tends to 36/169 as
B tends to infinity. This is a ratio of upper allowances, not the
ratio of actual energies or a claim that the trajectory reaches Bc.
For example, whenever X>=4E0, (17) is at most \((37/52)^2=1369/2704<1\).

There is a consumer in the existing source/residual estimate. At A=2,
\(\Theta=(2V,V+2J_2)=(2V,2V+C)\), so define
\[
\mathcal T_{\rm gen}=4E_0+(\sqrt{E_0}+2\sqrt X)^2,\qquad
\mathcal T_{\rm corr}=4E_0+(2\sqrt{E_0}+\tfrac{12}{13}\sqrt X)^2.
\]
Then
\[
\boxed{\|\Theta_s\|_2^2\le
\min\{\mathcal T_{\rm gen},\mathcal T_{\rm corr}\},\qquad
\mathcal T_{\rm corr}<\mathcal T_{\rm gen}\iff B>B_c.}
\tag{18}
\]
The baseline Tgen already uses the sharper triangle bound, rather than
only Note47's coarser Young payment \(6E_0+8X\) at this mark. Thus the
gain is not produced by an avoidable loss in the comparison.

Specifically, Note47's retained exterior term
\((12/625)\alpha\|\Theta\|_{L^2(r\ge2)}^2\) can be bounded by
\((12/625)\alpha\min(\mathcal T_{\rm gen},\mathcal T_{\rm corr})\).
Relative to that same whole-space Tgen payment, the explicit saving is
\((12/625)\alpha(\mathcal T_{\rm gen}-\mathcal T_{\rm corr})_+\).
No improvement of the already compacted R5 coefficient
\(274/25+B_1+B_0\) is claimed: its inner-region maximum still has to be
paid, and substituting a whole-space jet bound does not preserve every
advantage of a localized bound. The supported outputs are (15) and this
optional jet-forcing payment, not a new global allowance for F or G.

## 5. Residual and direct-information accounting

No residual is set to zero. The exact initial residual remains
\(\mathcal R_0=[\mathcal A_T,S](F_0,F_1)\), nonzero as proved in
Note40. Its full evolution and commutator remain those of Notes31/40/47:
\[
\mathcal R_s=L_s\mathcal R+[\mathcal A_T,L_s]W.
\]
This proof neither re-estimates nor drops any of those terms, including
the second-order part, cutoff derivatives and source multiplication.
On r=1, \(\mathcal R=-\Theta\), so the original combined numerator
\(\Theta+\mathcal R\) retains its cancellation. No singular quotient is
split, and all inner-ball energies remain. C is a relation between true
propagated jets, not an assertion of zero source-operator residual.

The same source information also supports a direct physical comparison.
For x>=0, \(\sin x\ge x-x^3/6\), by integrating
\(\cos x\ge1-x^2/2\). Thus at this same mark,
\[
-H_a(1/4,2)=\int_0^\infty uq(u)\sin(2u)\,du
\ge2M_2-\tfrac43M_4\ge\frac{35}{18}M_2>0.
\tag{19}
\]
This is a direct consequence of the same analytical moment budget,
available before auxiliary evolution. The low-frequency location is
already within the direct-information program in Notes16/29; R7 provides
no new collision-free region, acquisition advantage or independent
theta separator. An equally informed direct analysis may use the same
correlation (1). Its new utility here is the explicit supporting-energy
bound (15), compared to separate propagation at the same B.

Most importantly, both allowances in (15) still grow like exp(6B).
If B diverges at a finite endpoint, the improved bound is compatible
with that divergence. It supplies no independent control of G, alpha
or B through Note28's deadline. A direct-margin conversion from Note29
would still use direct information, as (19) makes explicit.

## 6. Controls, scope and stopping boundary

The proof's sufficient input class is broader than literal theta:
positive sources with the required spatial moments, literal cosine,
and \(M_4/M_2\le1/24\), at the same A=2 and unit preparation. The
complete theta sum proves that moment input; it is not characterized by
it. In fact the per-summand argument also works for admissible positive
weighted-square combinations. A failed canonical-source premise alone
does not imply failure of the final norm inequality.

| Registered comparison | What is retained or fails for this R7 proof |
| --- | --- |
| R6 fixed-amplitude polynomial kernels | The theta moment bound holds, but the literal sine/cosine remainder (9) fails. Finite cosine prefixes alone do not justify (10). No assertion that every such kernel violates (1) is made. |
| Exact Gaussian-polynomial cosine source | Literal cosine holds. At T=1/4 its M2=21 sqrt(pi)/32 and M4=123 sqrt(pi)/256 give M4/M2=41/56>1/24: the quantitative moment premise fails. Its event A=2 sqrt(6) is also outside the single R7 mark. |
| Weighted-square | Full unit coefficients/reflection fail, but positive weighted square terms can satisfy the very moment input proved here. The registered events near 44.13 and 83.53 are outside A=2; no contradiction or control exclusion follows. |
| Finite-prime orbit | Selected arithmetic does not fix the canonical source/reflection. No moment failure is claimed; its high-gap event locations are not this fixed mark. |
| Reflected super-Gaussian | Canonical amplitude fails; its registered event pi/4 is outside this mark. Its R7 moment ratio has not been acquired. |
| Smooth shape / positive primitive | Literal source fails; their shape/primitive data do not assert the quantitative ratio (8). No ratio failure or event at this mark is invented. |
| Euler-factor | The shifted source/conductor differs; no R7 moment evaluation. Negative Laguerre witnesses are not automatically double events here. |
| Atomic/profile / continuous compact | Atomic inputs are outside the imported source-function theorem. For admitted continuous prepared sources, the same sufficient moment test can apply; no unverified failure is assigned. |
| RH-conditional endpoint | Retain RH conditionality, altered arithmetic and escaping double heights. Neither a moment computation nor a witness at this mark is supplied. |

These are premise checks against the [registered controls][controls],
not a new numerical replay of their witnesses. In particular, this
one-point moment estimate cannot be sold as a discriminator for the
all-height collision problem.

**Stop R7 here:** one supporting-energy gain is proved with complete
costs and its explicit comparison range. Parent B02 remains partial.
The next task is the fixed [E08 R7 assessment][packet] by Sol, with
[Continuation56][next] for a model change. No second candidate, larger
domain, new PDE, numerical stage or manuscript version was produced.

## 7. Provenance and sources

Actual recorded thread 01a18911-d6d6-7650-ba07-adcf6916da3a, turn
01a18912-2ca1-7653-8da0-2ed5c70e49b7; **gpt-6-astra / max**.
The [unique public history][history] is chat0026. No subagents were used.
Review29 is same-assistant checking and does not constitute E08.

The elementary trigonometric normalization was rechecked in the already
cataloged [DLMF 4.19.1--2](https://dlmf.nist.gov/4.19), and the square
theta normalization in [DLMF 20.2.3](https://dlmf.nist.gov/20.2.E3),
29 October 2026. These selected formulas are classical references;
the new inequalities and constants are derived above, not attributed
to DLMF. No novelty search or new external theorem is claimed.
The packet records frozen input hashes as identity evidence only.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n47]: 47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[review]: ../reviews/29_COSINE_JET_CORRELATION_B02_R7_SELF_ASSESSMENT_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_COSINE_JET_CORRELATION_ASSESSMENT_REQUEST_R7_20261029.md
[next]: 56_COSINE_JET_CORRELATION_AND_MODEL_CONTINUATION_20261029.md
[history]: ../chat-histories/0026_2026-10-29T19-10-10Z_continue-radial-theta-collision-research.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta-results]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
