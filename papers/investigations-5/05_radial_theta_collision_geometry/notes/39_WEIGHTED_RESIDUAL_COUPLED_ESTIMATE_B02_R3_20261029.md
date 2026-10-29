# CTF-B02 R3: a weighted residual and second-jet estimate

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 chat0018, **Derive coupled CTF-B02 R3 estimate**.

**Return: one functional and a fixed analytical route for CTF-E07 R1.**
The formal energy calculation below absorbs the residual's second-order
forcing with the Laplacian dissipation already present in the gradient
balance. It suggests a finite estimate for three energies, with no third
spectral jet. Full coefficient, domain and integrated-estimate verification
is assigned to [E07 R1][packet]; this note does **not** report that lemma as
proved. Parent B02 remains partial. No signed theta separation or control
through the collision deadline has been obtained.

| Next task | Type | Recommended model | Readiness | Output |
| --- | --- | --- | --- | --- |
| **CTF-E07 R1 — default** | E | Sol: the functional, identities, constants and proof method are fixed | Ready from this note and the frozen packet | Prove the stated weighted estimate, or return one specific failed premise |
| CTF-E08 | E | Sol: assess one completed return | Gated on E07 | Bounded assessment; integrate only supported conclusions |
| CTF-E03 / CTF-B03 | E / B | Sol / Astra | Still gated | No numerical or coverage task is issued |

The [overview][overview] authorizes a bounded residual estimate as an
intermediate job. [Progress05][progress] owns live status; the
[model workflow][workflow] requires the routine proof work to pass to Sol
once this route is fixed. The [result index][results], [avoid index][avoid],
[control screen][controls], [target classification][a01],
[cancellation discipline][a12], [scoped-result rule][a07] and
[useful-gain rule][a20] govern the interpretation below.

## 1. Frozen choice and intended gain

The single functional was selected before this estimating argument on
the physical rectangle
\[
\mathscr P=[0,\tfrac12]\times[1,6],\qquad p=(T,a).
\tag{1}
\]
For each fixed mark use the whole-space smooth weighted solution from
[Note28][n28], for auxiliary time \(0\le s<S_{\max}(p)\). Keep the complete
theta source, K1 preparation, fixed unit jet weight, original feedback
and the explicit cutoff extension in [Note31, equation (6)][n31]:
\[
\mathcal A_T=b\cdot\nabla+c_T,\quad
b=\eta(r)\log r\,X,\quad
c_T=-\eta(r)r\log r\,\ell_T'(r),\quad \ell_T=\log\rho_T.
\tag{2}
\]
Here \(\rho_T=e^{Tu^2}\Phi(u)/(8\pi r^3)\), \(u=\log r/2\), on the
exterior; the complete reflection defines its positive continuation.
Use exactly Note31's cutoff, zero for r<=1/2 and one for r>=3/4.
The complete theta sum defines every coefficient; no truncated first
square mode replaces it.

Set \(J=J_2\), the actual second derivative in the running spectral
parameter with the mark fixed, and retain
\[
\Theta=(aV,V+aJ),\quad \mathcal R=\mathcal A_TW-\Theta,
\quad Z=\omega\mathcal R,\quad \omega=(1+r^2)^{-2},
\]
\[
Y=\|Z\|_2^2,\quad Q=\|J\|_2^2,\qquad
\boxed{\mathcal F=G+Y+Q.}
\tag{3}
\]
All three weights in the functional are fixed at one. The proposed gain
is a **finite differential estimate for a weighted residual**, using the
existing second spatial derivatives in G's dissipation. This is weaker
than unweighted residual control at infinity. It is stronger than leaving
the commutator as an unevaluated forcing requiring a higher derivative
hierarchy. No improvement in the previous bound for G alone is claimed.

The spatial weight is smooth and strictly positive everywhere. It has no
singularity at the origin or sphere. On every fixed ball of radius Rb,
\[
\|\mathcal R\|_{L^2(B_{R_b})}^2\le(1+R_b^2)^4Y.
\tag{4}
\]
Thus a bound for Y controls the actual residual on bounded spatial sets.
The energy G still includes the entire inner ball.

## 2. Full signed production before estimates

Write \(L_s=\Delta+\alpha(v\cdot\nabla+d)\), \(d=\operatorname{div}v\).
There is no mark derivative of alpha in these equations:
\[
J_s=L_sJ,\qquad
\mathcal R_s=L_s\mathcal R+(\mathscr C_0+\alpha\mathscr C_1)W,
\tag{5}
\]
where the full operators, including cutoff derivatives, are
\[
\begin{split}
\mathscr C_0={}&-2(\partial_jb_i)\partial_{ij}
 -(\Delta b+2\nabla c_T)\cdot\nabla-\Delta c_T,\\
\mathscr C_1={}&(b\cdot\nabla v-v\cdot\nabla b)\cdot\nabla
 +b\cdot\nabla d-v\cdot\nabla c_T.
\end{split}
\tag{6}
\]
The last terms are multiplication operators. Put \(l=\log\omega\).
Conjugating (5) gives the proposed identity to verify in E07:
\[
Z_s=\Delta Z+(\alpha v-2\nabla l)\cdot\nabla Z
 +\{\alpha d+|\nabla l|^2-\Delta l-\alpha v\cdot\nabla l\}Z
 +\omega(\mathscr C_0+\alpha\mathscr C_1)W.
\tag{7}
\]
Let \(N=\|\Delta W\|_2^2\) and retain Note31's exact drift production
\[
\mathcal K=2\sum_{k=1}^2\int\nabla W_k^TDv\nabla W_k
 +\int d|\nabla W|^2-\int(\Delta d)|W|^2.
\]
The formal integration by parts then yields
\[
\begin{split}
\mathcal F'={}&-2N-2\|\nabla Z\|_2^2-2\|\nabla J\|_2^2
 +2\int|\nabla l|^2|Z|^2
 +2\langle Z,\omega\mathscr C_0W\rangle
 +\alpha\mathfrak P,\\
\mathfrak P={}&\mathcal K+\int h|Z|^2+\int d|J|^2
 +2\langle Z,\omega\mathscr C_1W\rangle,\qquad
h=d-2v\cdot\nabla l.
\end{split}
\tag{8}
\]
These are whole-space real inner products. In particular, no absolute
value has yet replaced the signed mixed source terms. For q=r²,
\[
2|\nabla l|^2=\frac{32q}{(1+q)^2}\le8,\qquad
h=11+\frac{q-5}{(1+q)^2}\le\frac{265}{24}.
\tag{9}
\]
The cancellation of the two Laplacians of l in the integrated identity
is essential to these coefficients. Equations (7)–(9) are formal algebra
checked during the design stage; E07 must justify their use in the stated
solution class and verify the constants.

## 3. The finite coefficient route and proposed bound

All suprema below are over X in R³ and, for coefficients depending on T,
over \(0\le T\le1/2\). Use the Frobenius matrix norm in A2:
\[
\begin{array}{ll}
A_2=2\sup\omega|Db|_{\rm F},&
A_1=\sup\omega|\Delta b+2\nabla c_T|,\\
A_0=\sup\omega|\Delta c_T|,&
B_1=\sup\omega|b\cdot\nabla v-v\cdot\nabla b|,\\
B_0=\sup\omega|b\cdot\nabla d-v\cdot\nabla c_T|.&
\end{array}
\tag{10}
\]
The reason these should be finite is specific and checkable. Note31's
complete-theta asymptotic, with differentiated remainder uniform in T,
gives \(c_T=O(r^2\log r)\),
\(\nabla c_T=O(r\log r)\), \(\Delta c_T=O(\log r)\) at infinity.
The other coefficients in (10) grow at most as \(r^2\log r\).
Multiplication by omega makes them bounded. The fixed cutoff and positive
reflected source handle the compact inner transition region. E07 must
check these differentiated and uniform bounds; a leading-term
substitution for the actual coefficients is not permitted.

For Schwartz fields, the whole-space identity
\(\|D^2W\|_2^2=\|\Delta W\|_2^2\) would give
\[
\|\omega\mathscr C_0W\|_2\le A_2\sqrt N+A_1\sqrt G+A_0\sqrt{E_0},
\quad
\|\omega\mathscr C_1W\|_2\le B_1\sqrt G+B_0\sqrt{E_0}.
\tag{11}
\]
In particular \(2A_2\sqrt{YN}\le N+A_2^2Y\) spends only half of the
negative diffusion in (8). Applying Young's inequality to the other
mixed terms, and the inherited \(\mathcal K\le10G+30E_0\), gives the
following **E07 target**, with every coefficient displayed:
\[
\begin{split}
\mathcal F'+N+2\|\nabla Z\|_2^2+2\|\nabla J\|_2^2
\le{}&[A_1+\alpha(10+B_1)]G\\
 &+[8+A_2^2+A_1+A_0+\alpha(265/24+B_1+B_0)]Y\\
 &+6\alpha Q+[A_0+\alpha(30+B_0)]E_0.
\end{split}
\tag{12}
\]
Equivalently, the weaker convenient target is
\[
\boxed{\mathcal F'+N+2\|\nabla Z\|_2^2+2\|\nabla J\|_2^2
 \le(\kappa_0+\kappa_1\alpha)(\mathcal F+E_0),}
\tag{13}
\]
where
\[
\kappa_0=8+A_2^2+A_1+A_0,\qquad
\kappa_1=\max\{10+B_1,265/24+B_1+B_0,6,30+B_0\}.
\tag{14}
\]
These are explicitly defined source/coefficient constants, **not
numerically paid constants**. They must not depend on the solution's
unknown gradient, compression or lifespan. No derivative of R is taken
in its forcing estimate, and J solves its own homogeneous equation.
This is the reason a third spectral jet or a differentiated residual
equation should not be needed.

## 4. Consequences to verify, and the boundary accounting

If (13) is established, let \(B(s)=\int_0^s\alpha\). It implies
\[
\mathcal F(s)+E_0\le(\mathcal F(0)+E_0)
 e^{\kappa_0s+\kappa_1B(s)}.
\tag{15}
\]
It also closes locally without assuming an independent bound for B:
\(\alpha\le2G/(3E_0)\le2\mathcal F/(3E_0)\). With
\(x=1+\mathcal F/E_0\), \(x_0=x(0)\), and
\(C=\kappa_0+2\kappa_1/3\), the proposed consequence is
\[
x'\le Cx^2,\qquad
x(s)\le\frac{x_0}{1-Cx_0s}\quad(0\le s<(Cx_0)^{-1}).
\tag{16}
\]
Combine this with Note28's continuation criterion to obtain the stated
open lower lifespan interval. Finiteness, positivity of E0 and continuous
parameter dependence should give \(\sup_{p\in\mathscr P}x_0(p)<\infty\),
without any assumed lower bound for \(|(H,H_a)|\). E07 must verify that
compactness step rather than silently inserting a first-jet margin.

The actual preparation residual remains
\(\mathcal R_0=([\mathcal A_T,K_1*]F_0,
[\mathcal A_T,K_1*]F_1)\), with F0,F1 as in Note31. On r<=1/2 the
cutoff makes \(\mathcal R_{U,0}=-aV_0\). A useful check for E07 is that
V0 cannot vanish on that entire open ball: its Gaussian smoothing is
real analytic, heat convolution is injective, and the raw
\(-u\rho_T\sin(au)\) is nonzero for every a>0. This would prove
\(Y(0)>0\) throughout (1). It does **not** assert a nonzero sphere trace
at every frequency; Note31's exceptional-frequency qualification stays.

At r=1 retain exactly
\(\mathcal R=-\Theta\). If reconstructing the exterior gradient, the
only admissible expression is
\[
\partial_rW=\ell_T'W+\frac{\Theta+\mathcal R}{r\log r}.
\tag{17}
\]
The present functional never estimates the two singular quotients
separately and never replaces their sum by Theta. Its integrations are
over the whole space, without an artificial boundary at r=1. Equation
(17) and the full inner-ball part of G must remain in E07's domain audit.
No bound for either separate quotient is claimed by (4).

## 5. Canonical input, control screen and matched information

The fixed complete source enters (6) and the signed mixed terms in (8)
through its actual logarithmic derivative. Positivity, full reflection
and differentiated theta tails are the inputs to finiteness of (10).
The estimate (12) then discards their signs by Young's inequality.
**It uses no proved arithmetic sign that separates theta from colliding
controls.** This is a deliberate limit of this intermediate contract,
not a claim that such a sign is unavailable by other estimates.

The controls are screened analytically against the proposed lemma; no
prior witness or numerical certificate was recomputed:

| Control | Actual premise/domain distinction | Outcome for this intermediate estimate |
| --- | --- | --- |
| Gaussian-polynomial, \(T_c=1/4,a_*=2\sqrt6\) | Its event lies inside (1); its log-radius Gaussian tail differs from the literal theta coefficient. Its smooth moment class is admitted for T<17/4 | Must remain compatible with finite breakdown. No deadline exclusion is obtained |
| Weighted-square, events near 44.1303 and 83.5324 | Square support remains, full unit coefficients/reflection fail; these witnesses lie outside (1) | Prepared finite-moment data satisfy the generic energy route; no claim of rejection in this box |
| Finite-prime orbit | Selected-prime identities may hold, full reflection fails; witnesses escape to high gaps with no fixed compact location | No separating use of all-prime arithmetic is made here |
| Fully reflected super-Gaussian, event \((1/4,\pi/4)\) | Reflection survives, complete integer-square source fails; witness frequency is below (1) | Same generic route on admitted moment domains; reflection alone is no separator |
| Smooth shape and positive-primitive controls | Shape/primitive identities survive while canonical square arithmetic does not; no event in (1) is asserted | No sign from those properties has been used |
| Euler-factor | Shifted source, modified Euler factor/conductor; its registered negative Laguerre witnesses are not automatically double events in this box | Generic energy calculus is compatible with its obstruction |
| RH-conditional endpoint controls | Retain their RH hypothesis, fail ordinary Dirichlet-series arithmetic, and added doubles escape to infinity | No witness is imported into (1), and no conditional premise is treated as unconditional |
| Atomic finite-profile / continuous compact controls | Atoms remain outside the imported source-function statement; the continuous extension is not a strictly positive complete theta amplitude | No new atomic theorem is claimed; the continuous prepared class can be tested without assigning it a logarithmic derivative at its zeros |

More precisely, even a smooth control can be measured with the **same
fixed theta operator**. Its initial residual then includes both the heat
commutator and the propagated raw mismatch:
\[
\mathcal R_{*,0}=[\mathcal A_T,K_1*]W_*^{\rm raw}
 +K_1*(\mathcal A_TW_*^{\rm raw}-\Theta_*^{\rm raw}).
\tag{18}
\]
Only the second summand vanishes for the actual theta source. The
proposed estimate accepts either initial residual; dropping the mismatch
for a control would be an invalid comparison. Alternatively its own
source operator needs its own coefficient bounds and extension. Neither
comparison turns the raw logarithmic-source identity into separation.

The direct-information comparison uses the same complete qT, Gaussian
preparation and actual spectral derivatives to form F(0), E0 and the
coefficient budgets. These data also define H and Ha directly. There
is no acquired physical first-jet floor, enlarged exclusion region,
measured cost saving or sharper G bound. Indeed (14) has kappa1>=30,
whereas Note28 already controls G+3E0 with exponent 10B. The potential
addition is the explicit finite weighted-residual estimate and its
local spatial consequence (4), not a superior gradient allowance.

## 6. Disposition and stop rule

**R3 completes its conceptual contract with an E07 route; the analytical
lemma remains unverified.** The signed form (8) is retained in the
record, but (12) pays it by absolute inequalities. Whether one can use
the actual theta correlations in those mixed terms to survive the
collision deadline remains unresolved. Gronwall in the unknown B does
not settle it, and the local Riccati interval is not claimed to reach
that deadline. No new RH-equivalent criterion is offered.

The proof strategy is now fixed: verify (6)–(11), use the displayed
Young payments for (12)–(13), then prove the integrated comparisons and
domain claims. This is routine analytical execution, so stop B02 R3 at
this boundary under the model workflow. E07 must not choose another
weight, functional, PDE or signed hypothesis. A failed premise returns
the precise defect to a recorded B02 revision. E03 remains gated; decimal
evaluation of these constants has no current separating consumer.

**Next: [E] CTF-E07 R1 — Sol**, prove this one weighted closure or record
its precise failure. [The packet][packet] fixes the finite checklist,
source versions, permitted edits and acceptance conditions. No E07
execution, E08 assessment, manuscript expansion, numerical run, new
snapshot or independent specialist review is reported in this return.

[packet]: ../research-progress/handoffs/CTF-E07_WEIGHTED_RESIDUAL_CLOSURE_REQUEST_R1_20261029.md
[overview]: ../research-overview/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_OVERVIEW_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
