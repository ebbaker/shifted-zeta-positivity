# CTF-E07 R1: verified weighted residual closure

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0020**, **Verify CTF-E07 weighted residual**.

**Request:** [CTF-E07 R1][packet], executing the fixed design in
[Note39][n39]. **Return: accepted analytical execution within the inherited
prepared Schwartz/weighted solution class.** Note39 (12)–(16) hold with
its constants unchanged. No failed premise or algebraic correction was
found. This proves finite weighted-residual closure, its integrated
dissipation estimate and a positive local lifespan interval. It supplies
no bound through a collision deadline and no signed theta separator.
Parent CTF-B02 remains partial.

| Next task | Type and recommended model | Readiness and bounded output |
| --- | --- | --- |
| **CTF-E08 — default** | **E — Sol:** assess this fixed analytical return | Ready; one scoped assessment and proportionate integration under Overview05 |
| CTF-E03 | E — Sol | Gated; this analytical proof needs no numerical acquisition |
| CTF-B03 | B — Astra | Gated on an assessed substantive canonical gain; no extension is issued here |

[Progress05][progress] remains the sole live register. The
[model workflow][workflow], [result index][results] and [avoid index][avoid]
were read before execution. Under [avoid/01][a01], this is a bounded
energy estimate, not another noncollision reformulation. Its control
screen follows [result-summaries/12][controls] and [avoid/02][a02]; its
scope and cancellation accounting follow [avoid/07][a07] and
[avoid/12][a12]. The gain is the finite residual estimate specified in
R1, with the remaining transfer gap stated under [avoid/20][a20].

## 1. Coefficients, data and the preparation residual

Keep precisely the physical rectangle
\(\mathscr P=[0,1/2]\times[1,6]\), the complete theta source, the unit
Gaussian preparation and the fixed-mark propagator of [Note28][n28].
Use [Note31 (6)][n31] with its explicit smooth cutoff
\(\eta(r)=h(4r-2)\): zero for \(r\le1/2\), one for \(r\ge3/4\).
All integrations below are over \(\mathbb R^3\). Let
\[
\mathcal A_T=b\cdot\nabla+c_T,\quad b=\eta\log r\,X,
\quad c_T=-\eta r\log r\,\ell_T',\quad\ell_T=\log\rho_T,
\]
\[
J=\left.\partial_z^2j^p(s,T,z)\right|_{z=a},\quad
\Theta=(aV,V+aJ),\quad\mathcal R=\mathcal A_TW-\Theta,
\quad\omega=(1+r^2)^{-2},\quad Z=\omega\mathcal R.
\]
Write \(Y=\|Z\|_2^2\), \(Q=\|J\|_2^2\),
\(N=\|\Delta W\|_2^2\), and \(\mathcal F=G+Y+Q\).

**Uniform complete-source bounds.** Put \(\beta=3/(2\pi)\). The full
theta series gives, exactly for \(r\ge1\),
\[
\rho_T(r)=\frac\pi4 r^{3/2}
 e^{-\pi r^2+(T/4)(\log r)^2}P(r),\qquad
P(r)=1-\beta r^{-2}+\tau(r),
\]
\[
\tau(r)=\sum_{n\ge2}(n^4-\beta n^2r^{-2})
                  e^{-\pi(n^2-1)r^2}.
\tag{1}
\]
Every summand of \(\tau\) is positive and \(P\ge1-\beta>0\).
Termwise differentiation through order three is justified uniformly on
\(r\ge1\). Indeed, after extracting \(e^{-3\pi r^2}\), the derivatives
are bounded by \(C_k r^k\) times convergent sums of polynomials in \(n\)
against \(e^{-\pi(n^2-4)}\). Thus
\[
\tau^{(k)}=O_k(r^k e^{-3\pi r^2}),\qquad 0\le k\le3.
\tag{2}
\]
This remainder is independent of T; its differentiated estimates are
for the complete tail, not a replacement by its first square mode.
It follows, uniformly for \(0\le T\le1/2\), that
\[
\ell_T'=-2\pi r+\frac{3}{2r}+\frac{T\log r}{2r}+O(r^{-3}),
\]
\[
c_T=2\pi r^2\log r-\frac32\log r
       -\frac T2(\log r)^2+e(r),\qquad
e^{(k)}(r)=O(r^{-2-k}\log r)\quad(0\le k\le2).
\tag{3}
\]
In particular \(c_T=O(r^2\log r)\),
\(\nabla c_T=O(r\log r)\), \(\Delta c_T=O(\log r)\).
Here and below asymptotic growth estimates are at infinity.
Also \(Db=O(\log r)\), \(\Delta b=3X/r^2=O(r^{-1})\).
Writing \(v=\lambda(r)X\),
\[
b\cdot\nabla v-v\cdot\nabla b
 =(r\lambda'\log r-\lambda)X=O(r),
\]
while \(b\cdot\nabla d=O(r^{-2}\log r)\) and
\(v\cdot\nabla c_T=O(r^2\log r)\).
Multiplication by \(\omega=O(r^{-4})\) therefore bounds every
coefficient in Note39 (10).

On \([1/2,1]\), the full reflection
\(\rho_T(r)=r^{-6}\rho_T(1/r)\) supplies a smooth strictly positive
source, uniformly on the compact T interval. Positivity and compactness
bound the required logarithmic derivatives. All cutoff derivatives
remain in the coefficients; near the origin both b and c vanish.
Consequently the following are finite, with the exact definitions in R1:
\[
\begin{array}{ll}
A_2=2\sup\omega|Db|_{\rm F},&
A_1=\sup\omega|\Delta b+2\nabla c_T|,\\
A_0=\sup\omega|\Delta c_T|,&
B_1=\sup\omega|b\cdot\nabla v-v\cdot\nabla b|,\\
B_0=\sup\omega|b\cdot\nabla d-v\cdot\nabla c_T|.&
\end{array}
\tag{4}
\]
The suprema are over all space and, where relevant, \(0\le T\le1/2\).
They depend only on the fixed source, cutoff and drift, never on the
unknown solution, \(\sup G\), \(\sup\alpha\), B or lifespan.

**Prepared data and compactness.** For the raw \(F_0,F_1,F_2\) in
Note31 (2), every weighted \(L^1\) moment is finite uniformly on
\(\mathscr P\), as are the moments of their needed parameter derivatives.
The factor \(e^{-\pi r^2+(T/4)\log^2r}\) decays faster than every
inverse power of r, even after multiplication by powers of log r. Gaussian convolution maps these data continuously into Schwartz
space: for each weighted derivative use
\[
(1+|X|)^M\le(1+|X-Y|)^M(1+|Y|)^M
\]
inside the differentiated convolution, and then the weighted Gaussian
bound and a weighted \(L^1\) bound for the raw data. Dominated convergence
gives continuity in \((T,a)\). The polynomial/logarithmic coefficient
bounds above give the same continuity for \(\mathcal A_TW_0\), \(Z_0\)
and their required norms. Hence \(\mathcal F(0)<\infty\) and both
\(\mathcal F(0)\) and \(E_0\) are continuous on \(\mathscr P\).

For each mark \(F_0\) is nonzero on a short exterior interval near u=0.
Heat convolution is injective: its Fourier multiplier
\(e^{-|\xi|^2}\) never vanishes. Thus \(U_0\ne0\), so \(E_0>0\).
Compactness now gives
\[
\min_{\mathscr P}E_0>0,\qquad
X_0:=\max_{\mathscr P}\left(1+\frac{\mathcal F(0)}{E_0}\right)<\infty.
\tag{5}
\]
This is a prepared spatial-energy bound; no lower bound for the physical
mass vector \((H,H_a)\) is assumed or obtained.

The exact preparation residual is retained:
\[
\mathcal R_0=([\mathcal A_T,K_1*]F_0,
              [\mathcal A_T,K_1*]F_1).
\tag{6}
\]
The raw identities used here hold distributionally across r=1: the
normal coefficient \(r\log r\) kills the surface delta of \(F_0\).
The heat commutator includes the **plus** \(\operatorname{div}b(Y)\)
term in Note31 (7), so (6) does not discard that term.
On the open cutoff ball \(\mathcal R_{U,0}=-aV_0\). For every a in
[1,6], \(F_1=-u\rho_T\sin(au)\) is nonzero on a short interval u>0.
Its Gaussian convolution extends analytically to complex spatial
variables, with domination on every compact complex set. If V0 vanished
on the whole ball, real analytic continuation would make it vanish
everywhere, contradicting heat injectivity. Therefore
\[
Y(0)>0\quad\hbox{throughout }\mathscr P.
\tag{7}
\]
This ball argument does not assert nonzero residual trace at every sphere
frequency. Note31's possible exceptional frequencies remain qualified.

## 2. Full signed production and whole-space boundaries

Put \(L_s=\Delta+\alpha(v\cdot\nabla+d)\). With the mark fixed, J
and both components of \(\Theta\) solve the same homogeneous equation.
Direct differentiation therefore gives
\[
J_s=L_sJ,\qquad
\mathcal R_s=L_s\mathcal R+(\mathscr C_0+\alpha\mathscr C_1)W,
\]
\[
\begin{split}
\mathscr C_0={}&-2(\partial_jb_i)\partial_{ij}
 -(\Delta b+2\nabla c_T)\cdot\nabla-\Delta c_T,\\
\mathscr C_1={}&(b\cdot\nabla v-v\cdot\nabla b)\cdot\nabla
 +b\cdot\nabla d-v\cdot\nabla c_T.
\end{split}
\tag{8}
\]
These are the full commutators. In particular, \(-\Delta c_T\),
\(b\cdot\nabla d\) and \(-v\cdot\nabla c_T\) are multiplication
terms with the displayed signs. All derivatives of eta are present.
There is no mark derivative of alpha in this spatial commutator or in
the running spectral derivatives.

For \(l=\log\omega\), substitution of \(\mathcal R=e^{-l}Z\) gives
\[
Z_s=\Delta Z+(\alpha v-2\nabla l)\cdot\nabla Z
 +(\alpha d+|\nabla l|^2-\Delta l-\alpha v\cdot\nabla l)Z
 +\omega(\mathscr C_0+\alpha\mathscr C_1)W.
\tag{9}
\]
In the derivative of Y, integration of the advection contributes
\(-\int(\alpha d-2\Delta l)|Z|^2\). Twice the multiplication
coefficient in (9) cancels this \(2\Delta l\) exactly. Consequently,
with
\[
\mathcal K=2\sum_{k=1}^2\int\nabla W_k^TDv\nabla W_k
 +\int d|\nabla W|^2-\int(\Delta d)|W|^2,
\quad h=d-2v\cdot\nabla l,
\]
the **signed identity before any absolute estimate** is
\[
\begin{split}
\mathcal F'={}&-2N-2\|\nabla Z\|_2^2-2\|\nabla J\|_2^2
 +2\int|\nabla l|^2|Z|^2
 +2\langle Z,\omega\mathscr C_0W\rangle\\
&+\alpha\left\{\mathcal K+\int h|Z|^2+\int d|J|^2
 +2\langle Z,\omega\mathscr C_1W\rangle\right\}.
\end{split}
\tag{10}
\]
Here \(G'=-2N+\alpha\mathcal K\) and
\(Q'=-2\|\nabla J\|_2^2+\alpha\int d|J|^2\).

The two weight constants are exact. For q=r²,
\[
2|\nabla l|^2=\frac{32q}{(1+q)^2}\le8,
\qquad h=11+\frac{q-5}{(1+q)^2}\le\frac{265}{24}.
\tag{11}
\]
The first maximum occurs at q=1. The derivative of the fraction in h is
\((11-q)/(1+q)^3\), so its maximum is \(1/24\) at q=11.

These manipulations are valid also at s=0 after preparation. On each
compact interval inside the inherited lifespan, the weighted smoothness
and Schwartz decay of W and J, together with the polynomial/logarithmic
coefficients, give the required decay for R and Z and their derivatives.
One may first integrate with a smooth large-radius cutoff and pass to
the limit; every cutoff error vanishes by these bounds. The origin is
smooth because the operator is zero near it. There is no boundary at
r=1 in a whole-space integral.

At that sphere \(b=c_T=0\), hence exactly
\(\mathcal R=-\Theta\) at every smooth time. If the exterior gradient
is reconstructed, the valid formula is
\[
\partial_rW=\ell_T'W+\frac{\Theta+\mathcal R}{r\log r},\qquad r>1.
\tag{12}
\]
Smoothness and \((\Theta+\mathcal R)(1)=0\) preserve its cancellation.
Neither singular quotient is estimated separately. The entire inner
ball remains included in G; no flux or energy is removed at its sphere.

## 3. Fixed Young payments and integrated consequences

For Schwartz fields, two integrations by parts, component by component,
give
\[
\sum_{i,j,k}\|\partial_{ij}W_k\|_2^2
 =\sum_{i,j,k}\int\partial_{ii}W_k\,\partial_{jj}W_k
 =\|\Delta W\|_2^2=N.
\]
Pointwise Frobenius Cauchy–Schwarz in the second-order term of (8),
then the triangle inequality, proves Note39 (11):
\[
\|\omega\mathscr C_0W\|_2
 \le A_2\sqrt N+A_1\sqrt G+A_0\sqrt{E_0},\qquad
\|\omega\mathscr C_1W\|_2
 \le B_1\sqrt G+B_0\sqrt{E_0}.
\tag{13}
\]
Use exactly
\[
\begin{gathered}
2A_2\sqrt{YN}\le N+A_2^2Y,\\
2A_1\sqrt{YG}\le A_1(Y+G),\qquad
2A_0\sqrt{YE_0}\le A_0(Y+E_0),\\
2B_1\sqrt{YG}\le B_1(Y+G),\qquad
2B_0\sqrt{YE_0}\le B_0(Y+E_0).
\end{gathered}
\tag{14}
\]
There is no derivative of R to estimate in (13). The first payment uses
only one of the two units of N in (10). Note28's
\(Dv\le2I\), \(d\le6\), \(|\Delta d|\le30\) give
\(\mathcal K\le10G+30E_0\). Since \(\alpha\ge0\), (10)–(14) yield
the requested bound with every coefficient unchanged:
\[
\begin{split}
\mathcal F'+N+2\|\nabla Z\|_2^2+2\|\nabla J\|_2^2
\le{}&[A_1+\alpha(10+B_1)]G\\
 &+[8+A_2^2+A_1+A_0+\alpha(265/24+B_1+B_0)]Y\\
 &+6\alpha Q+[A_0+\alpha(30+B_0)]E_0.
\end{split}
\tag{15}
\]
Define exactly as in Note39 (14)
\[
\kappa_0=8+A_2^2+A_1+A_0,\quad
\kappa_1=\max\{10+B_1,265/24+B_1+B_0,6,30+B_0\}.
\]
Each coefficient in (15) is dominated by
\(\kappa_0+\kappa_1\alpha\), so, writing
\(\mathscr D=N+2\|\nabla Z\|_2^2+2\|\nabla J\|_2^2\),
\[
\boxed{\mathcal F'+\mathscr D
 \le(\kappa_0+\kappa_1\alpha)(\mathcal F+E_0).}
\tag{16}
\]

**Integrated estimate.** For s strictly below Smax put
\(B(s)=\int_0^s\alpha(q)\,dq\) and
\(M(s)=\kappa_0s+\kappa_1B(s)\). Multiplication by \(e^{-M}\) and
integration give
\[
\boxed{e^{-M(s)}(\mathcal F(s)+E_0)
 +\int_0^se^{-M(q)}\mathscr D(q)\,dq
 \le\mathcal F(0)+E_0.}
\tag{17}
\]
In particular
\[
\mathcal F(s)+E_0\le(\mathcal F(0)+E_0)e^{M(s)}.
\tag{18}
\]
Because M is nondecreasing, (17) also implies
\(\mathcal F(s)+E_0+\int_0^s\mathscr D(q)dq
\le(\mathcal F(0)+E_0)e^{M(s)}\). No finite bound for B beyond the
solution's existing compact lifespan intervals is presumed.

**Local comparison and continuation.** Since
\(\alpha\le2G/(3E_0)\le2\mathcal F/(3E_0)\), set
\(x=1+\mathcal F/E_0\), \(x_0=x(0)\) and
\(C=\kappa_0+2\kappa_1/3\). Then
\[
x'\le[\kappa_0+(2\kappa_1/3)(x-1)]x\le Cx^2,
\qquad x(s)\le\frac{x_0}{1-Cx_0s}.
\tag{19}
\]
Initially this is proved only for
\(s<\min\{S_{\max},(Cx_0)^{-1}\}\), by integrating the inequality
for \(1/x\). If \(S_{\max}<(Cx_0)^{-1}\), its right side keeps G
bounded up to that finite endpoint. This contradicts Note28's
continuation criterion. Hence
\[
S_{\max}(p)\ge\frac1{Cx_0(p)},\qquad
S_{\max}(p)\ge\frac1{CX_0}\quad(p\in\mathscr P).
\tag{20}
\]
Existence is guaranteed on the respective **open** intervals; equality
at their endpoints is permitted. This uses continuation after the
pre-lifespan estimate, never an assumed extension. The constants X0 and
C are finite but have not been acquired numerically.

Finally, \(\omega^{-2}\le(1+R_b^2)^4\) on a fixed ball gives
\[
\|\mathcal R(s)\|_{L^2(B_{R_b})}^2
 \le(1+R_b^2)^4Y(s),
\tag{21}
\]
which is Note39 (4). Finite closure here concerns precisely
\(G+\|\omega\mathcal R\|_2^2+\|J\|_2^2\) and its stated integrated
dissipation. It asserts neither pointwise bounds for every derivative nor
a whole-space unweighted residual bound from this energy alone.

## 4. Control screen, matched information and disposition

The exact Gaussian-polynomial control in Notes28 and31 has
\[
\Phi_*(u)=(64u^4+6)e^{-(17/4)u^2},\qquad
H_*(1/4,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16}.
\]
All its spatial moments and finite spectral jets exist for T<17/4:
a spatial moment contributes only a factor exponential in u, dominated
by \(e^{-(17/4-T)u^2}\). Its prepared fields are Schwartz, so the same
theta operator and the same coefficient budgets admit it throughout
\(\mathscr P\). At \((T,a)=(1/4,2\sqrt6)\), both masses vanish, while
its prepared data have \(E_{*,0},P_{*,0}>0\). Note28's theorem still gives
\[
S_{\max,*}\le\frac{60}{7(5\pi^2)^{2/5}}
 \frac{P_{*,0}^{4/5}}{E_{*,0}^{2/5}}<\infty.
\tag{22}
\]
This imported exact control identity was not recomputed as a numerical
witness. The local interval (20) is compatible with (22); it is not a
payment through that deadline.

In this same-operator comparison, both initial residual terms are
essential. On the exterior let
\[
M_T^*(r)=r\log r\{(\log\rho_{*,T})'-\ell_T'\}.
\]
Then the distributional raw mismatch is
\(\mathcal A_TW_*^{\rm raw}-\Theta_*^{\rm raw}
=M_T^*W_*^{\rm raw}\), and
\[
\mathcal R_{*,0}=[\mathcal A_T,K_1*]W_*^{\rm raw}
 +K_1*(\mathcal A_TW_*^{\rm raw}-\Theta_*^{\rm raw}).
\tag{23}
\]
The boundary delta again has zero multiplier \(r\log r\) at r=1.
The second summand vanishes for theta, not for this control. Dropping it
would falsely assign the control theta's raw relation. No claim about
its nonzero sphere trace at the event is needed.

The other rows of Note39 were checked against the [registered screen][controls]
without recomputing witnesses:

| Control | Premise/domain distinction retained |
| --- | --- |
| Weighted-square | Complete unit coefficients and full reflection fail; the registered events near 44.1303 and 83.5324 are outside this frequency rectangle |
| Finite-prime orbit | Selected-prime constraints do not supply full reflection; high-gap witnesses have no fixed compact location |
| Fully reflected super-Gaussian | Full reflection survives, complete square arithmetic fails; its event at frequency pi/4 is below the rectangle |
| Smooth shape / positive primitive | Their named shape and primitive properties do not identify the complete source; no event location in this rectangle is imported |
| Euler-factor | Modified arithmetic/conductor fail the literal theta source; negative Laguerre witnesses are not automatically double events in this box |
| RH-conditional endpoint | Their RH hypothesis, failure of ordinary Dirichlet-series arithmetic and escaping double heights are retained |
| Atomic finite-profile / continuous compact | Atoms remain outside the imported source-function statement; a continuous prepared control may use the fixed theta operator without a logarithmic derivative of its own at source zeros |

Thus literal theta-source premises distinguish these sources as recorded,
but the intermediate energy estimate does not use those distinctions to
reject a colliding control. Its complete-source input is the actual
\(\ell_T'\), full reflection and differentiated tail in (1)–(4), and the
actual prepared data in (5)–(7). The signed mixed terms remain visible in
(10); Young's payments in (14) discard their signs and correlations.
No arithmetic sign separating theta from these controls is proved.

For matched information, F(0), E0 and the coefficient budgets use the
same complete source, preparation and spectral derivatives as a direct
analysis. These data also define H and Ha directly. The new output is
the explicit finite weighted-residual estimate (15)–(21). There is no
acquired physical first-jet floor, new exclusion box, measured cost saving
or improved allowance for G. In particular \(\kappa_1\ge30\), whereas
Note28 already bounds \(G+3E_0\) with exponent 10B; the new coupled bound
is not a sharper gradient estimate.

**All four R1 items are complete.** The frozen functional, source,
operator, domain, constants and proof method were unchanged. No
simulation, quadrature, scan, optimization, interval certificate,
external literature acquisition or numerical E03 request was used.
The unresolved premises for collision exclusion are a source-specific
signed or otherwise sharper estimate and enough independent control to
reach a paid deadline. Neither is supplied by (17) in an unknown B nor
by the local Riccati interval. These are remaining research obligations,
not failures of this weighted lemma.

The proof and checks here are internal LLM work. The executing assistant
checked the derivation and used three read-only delegated checks for
coefficients/data, energy/continuation, and controls/domain. All are the
same model, gpt-6.1-sol, with inherited ultra effort. The R3 design was by
gpt-6-astra; this execution is a different-model check of that design,
but neither relationship constitutes independent specialist review.
Note28's continuation theorem and collision deadline and Note31's full
reflection/source identities are imported within their stated hypotheses,
not re-established in every detail here.

**Next: [E] CTF-E08 — Sol**, assess this one return and integrate only
supported conclusions. No E08 assessment or manuscript integration is
claimed in this execution return; B02 remains partial and E03/B03 remain
gated. Preserve the issued R1 packet and Note39 as the frozen design.

## Input versions and provenance

The six frozen input hashes in R1 all matched at execution. The table
below records the exact bytes used; hashes establish identity only.
Progress05 is live and its listed hash is before this return's update.

| Input | SHA-256 |
| --- | --- |
| Overview05 | `b60765aa8cb1214e0ab7bd4c2fb334809549c2085df4039ae5d17e62deb33f82` |
| Note28 | `519dda1bdb4418b0cc7cea0f0fa2c403e3542196c7de1ade29cfda169649879c` |
| Note29 | `8f4a9b0f615afa4a50aebcd1144763620d2601d9f468669d5f1bb7f9d6c9a297` |
| Note31 | `9d2a9832f3a128d3bb2c3fc37eb7ab83547f2f9d35c16c82847ef7994795b8ec` |
| Continuation32 | `8516649f574e4b818a2dc371834e23b112410fab6f226cab2c36ccd623e6ea6e` |
| Note39 | `36cb00f7d07a8740c1e429b3eaa3870ef87ce95e38279610e179d6ce5dea0594` |
| E07 R1 | `618911e546f098e976202a00b6b8b4233937867fc0574cf44bbf7dcd96ba099b` |
| GPT workflow | `fa6ba38f1d8b0ee4c58d1341101fa7af53178a790d20d391d73752b7ee552a8a` |
| Progress05 at execution input | `46b7bac5cc4cbece7e4fa86b227068ae6143236e9977c29e7f605e40a6cbdc40` |
| Control register | `56dd6a40264a755df74bb6186fda68c054e86a8a63b7bff0272b9cdcb18e2af6` |

Executing thread: `01a187d2-e789-7180-bf38-a969c909c55f`;
turn: `01a187d3-7a08-7a62-8e55-879ad0a33181`.
The actual model and effort were read from this turn's recorded session
context. [The unique public archive][history] retains chat0020's identity;
current capture metadata belong to its registry. Research and chat
capture establish no external validation.

[packet]: ../research-progress/handoffs/CTF-E07_WEIGHTED_RESIDUAL_CLOSURE_REQUEST_R1_20261029.md
[n39]: 39_WEIGHTED_RESIDUAL_COUPLED_ESTIMATE_B02_R3_20261029.md
[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
[history]: ../chat-histories/0020_2026-10-29T13-21-48Z_verify-ctf-e07-weighted-residual.json
