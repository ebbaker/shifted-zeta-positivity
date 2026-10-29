# CTF-B02 R8: diffusion variance pays the previous local endpoint

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0028**, **Continue CTF-B02 with Astra**.

**Status: proved in-note; same-assistant analytical checks only.** One
retained diffusion term gives a finite, initial-data bound for compression
on the **closed** interval ending at Note42's former Riccati singularity.
The new guaranteed open lifespan extends strictly beyond that endpoint.
This is a generic finite-horizon improvement, with explicit costs; it
supplies neither a theta-specific separator nor collision-deadline coverage.
[Progress05][progress] records the candidate before testing and owns status.
[Self-assessment31][review] and [the E08 R8 packet][packet] distinguish the
completed self-check from the next, unexecuted assessment.

The sole selected mechanism is the strictly positive diffusion remainder
\(N-G^2/E_0\). No positive physical first-jet margin is used. The complete
source, literal cosine, unit preparation, original feedback and actual
fixed-mark jets remain those of [Notes28][n28], [40][n40], [47][n47] and
[55][n55]. [Continuation58][n58] supplies the acceptance boundary.

## 1. Consumer, horizon and full costs

Freeze the application at \(p=(T,A)=(1/4,2)\), on all of \(\mathbb R^3\).
Write \(W=(U,V)\), \(E_0=\|W_s\|_2^2>0\),
\(G=\|\nabla W\|_2^2\), \(N=\|\Delta W\|_2^2\), and keep
\[
 W_s=\Delta W+\alpha\operatorname{div}(vW),\quad
 v=X+\frac{X}{1+|X|^2},\quad d=\operatorname{div}v,\quad
 D=\int d|W|^2,\quad \alpha=2G/D,\quad B(s)=\int_0^s\alpha.
\]
Thus \(3E_0\le D\le6E_0\). For ordered derivative tensors set
\[
 H_j=\|\nabla^jW\|_2^2\quad(0\le j\le3),\qquad
 g=G/E_0,\quad n=N/E_0,\quad \nu=n-g^2.
\]
Here \(H_0=E_0,H_1=G,H_2=N\); derivatives are **spatial**, not physical
frequency derivatives. Let
\[
 a=14/3,\quad b=7/2,\quad
 \delta(s)=1-\frac{4g_0}{3}(e^{bs}-1),\quad
 y(s)=\frac{g_0e^{bs}}{\delta(s)},\quad
 L(x)=\frac27\log\left(1+\frac{3}{4x}\right).
 \tag{1}
\]
The predeclared target is \(S_{\rm tar}=L(g_0)\). Note42 controls g and B
for \(s<S_{\rm tar}\), but its allowance diverges at this endpoint.
We will pay that endpoint without an unknown exponential in B.

Here is the complete data-dependent budget, with positivity and all
constants proved below:
\[
 C_3=11038,\quad S_3=\frac{H_0(0)+H_1(0)+H_2(0)+H_3(0)}{E_0},
 \quad K=2S_3\ge2,
\]
\[
 h_0=\frac27\log\left[1+\frac{3}{4g_0}
                         (1-2^{-7/C_3})\right],\qquad
 M=2K+264K^2+\frac{40}{3}K^3,
\]
\[
 \boxed{h=\min\left\{h_0,\frac{\nu_0}{2M},
                              \frac{g_0}{2\nu_0}\right\}>0,\quad
 \varepsilon=\nu_0h,\quad y_h=y(h),\quad
 g_1=y_h-\varepsilon,\quad \eta=\varepsilon/y_h.}
 \tag{2}
\]
All are determined at preparation time. In particular \(\nu_0>0\),
\(g_1\ge g_0/2>0\), and \(0<\eta\le1/2\). The result is
\[
 \boxed{S_{\max}\ge L_{\rm new}:=h+L(g_1)>S_{\rm tar},\qquad
 B(S_{\rm tar})\le B_*:=\frac17\log\frac1{\delta(h)\eta}<\infty.}
 \tag{3}
\]
B is nondecreasing, so the same B bound holds on the full closed target
interval. Explicit bounds for G, alpha and accumulated G follow below.
Existence at \(L_{\rm new}\) itself is not asserted.

This changes a complete local bound, not merely a prefactor at an
uncontrolled B. It is not a claim that the new horizon reaches Note28's
\(S_*\). Its size can be very small: small initial variance or a large
higher-derivative budget shrinks h and the lifespan gain. There is no
uniform lower gain or numerical value for the theta horizon in this return.
The [result index][results], [spatial-flow cluster][spatial], [avoid index][avoid],
[target classification][a01], [control screen][controls], [scope rule][a07]
and [quantitative utility rule][a20] govern these distinctions.

## 2. The initial gap is a strictly positive spatial datum

Let \(q(u)=e^{u^2/4}\Phi(u)\), with the complete theta sum, and
\[
 \rho(X)=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},\quad
 u=\tfrac12\log r,\quad
 W_0=K_1*\{\rho(\cos(2u),-u\sin(2u))\}.
 \tag{4}
\]
The full tail and unit preparation give nonzero radial Schwartz data,
as proved in Note40. Hence every H_j(0) here is finite, E0>0 and g0>0.
No inverse value of \(H(T,A)\) or \(H_a(T,A)\) enters (2).

With unnormalized Fourier transform, define the probability measure
\[
 d\mu_0(\xi)=\frac{|\widehat W_0(\xi)|^2}{(2\pi)^3 E_0}\,d\xi.
\]
Plancherel gives the exact positive integral
\[
 \nu_0=\int |\xi|^4d\mu_0-
              \left(\int |\xi|^2d\mu_0\right)^2
 =\frac12\iint(|\xi|^2-|\zeta|^2)^2d\mu_0(\xi)d\mu_0(\zeta)>0.
 \tag{5}
\]
If it were zero, the absolutely continuous probability measure would be
supported on one sphere, a Lebesgue null set. This is impossible.
Equivalently, equality in \(G^2\le E_0N\) would require a nonzero L2
Laplacian eigenfunction on the whole Euclidean space. The proof applies
to every nonzero H2 field, including signed zero-mass fields.

The cost S3 is also an independently available source integral. For
\(M_j=\int_0^\infty u^j q(u)\,du\), let \(\mathfrak m=M_0+M_2\) and
\(c_K^2=(8\pi)^{-3/2}\). Since the vector raw L1 norm is at most
\(\mathfrak m\), tensor-valued Young's inequality gives
\[
 H_j(0)\le c_K^2\mathfrak m^2 c_j,\quad
 (c_0,c_1,c_2,c_3)=(1,3/4,15/16,105/64),
\]
\[
 S_3\le\frac{277}{64}\frac{c_K^2\mathfrak m^2}{E_0}.
 \tag{6}
\]
The Gaussian constants follow by integrating \(|\xi|^{2j}e^{-2|\xi|^2}\)
in three dimensions. Either exact S3 or the upper budget (6) may be used
in (2), replacing K consistently. Equation (5) is a complete positive
source-data integral, not a measured scalar in this return. If rigorous
numerical budgets are used later, any \(0<\underline\nu\le\nu_0\)
may replace \(\nu_0\) throughout (2) and the proof. A mere assertion of
positivity without its value does not give a numerical horizon gain.

## 3. Pay gap persistence using spatial derivatives through order three

We give explicit, deliberately loose drift constants, rather than
assuming an unpriced higher-regularity bound. Frobenius tensor norms obey
\[
\begin{array}{c|rrrr}
 m&1&2&3&4\\ \hline
 \|\nabla^m v\|_\infty\text{ upper bound}&6&20&168&1824
\end{array}
\qquad
 (\|\nabla d\|_\infty,\|\nabla^2d\|_\infty,
  \|\nabla^3d\|_\infty)\le(40,336,3648).
 \tag{7}
\]
To verify every entry, put f=(1+r²)^(-1). The chain rule partition into
singletons and pairs, with \(\|\nabla(r^2)\|=2r\) and
\(\|\nabla^2(r^2)\|=2\sqrt3\le4\), gives
\[
 \|\nabla^k f\|\le F_k(1+r^2)^{-1-k/2},\quad
 F_k=\sum_{a+2c=k}\frac{k!}{a!c!2^c}(a+c)!2^a4^c.
\]
For k=0,...,4 these are \(1,2,12,96,1056\). The product Xf then gives
\(F_m+2mF_{m-1}\), with an extra2 for the linear X term when m=1.
Tracing one tensor pair to obtain \(\nabla^m d\) costs at most
\(\sqrt3\le2\). This proves (7) on the entire space.

Write its v and d bounds as V_m and D_m. Commuting ordered spatial
derivatives of order k with \(v\cdot\nabla+d\) produces a remainder
whose L2 norm is bounded by
\[
 \sum_{m=1}^k\binom{k}{m}
 \{V_m\sqrt{H_{k-m+1}}+D_m\sqrt{H_{k-m}}\}.
 \tag{8}
\]
This is the full Leibniz expansion; no derivative of alpha appears
because alpha is spatially constant. Set \(\mathcal H=\sum_{j=0}^3H_j\).
Integrating the leading transport term contributes
\(\alpha\int d|\nabla^kW|^2\le6\alpha H_k\); diffusion is nonpositive.
Since all derivative orders on the right of (8) are at most3,
\[
 \mathcal H'\le C_3\alpha\mathcal H,\qquad
 C_3=6+2\sum_{m=1}^3\binom4{m+1}(V_m+D_m)=11038.
 \tag{9}
\]
All integrations are justified on compact lifespan intervals by the
inherited prepared smooth weighted class; diffusion in this identity
uses order four, but its nonnegative dissipation is discarded, so no
initial order-four budget is needed. Preparation supplies regularity at0.

The already proved Note42 bounds apply on \([0,h_0]\), because
\(h_0<S_{\rm tar}\). By construction
\(\delta(h_0)=2^{-7/C_3}\), hence \(B(h_0)\le\log2/C_3\).
Integrating (9) therefore gives the independent bootstrap budget
\[
 \mathcal H(s)/E_0\le2S_3=K\quad(0\le s\le h_0).
 \tag{10}
\]
There is no assumption that B is controlled beyond the old interval.
Only its established interior bound pays (10).

For completeness, the Lipschitz cost of the gap is as follows. Note28's
exact production gives \(G'=-2N+\alpha\mathcal K\), with
\(|\mathcal K|\le10G+30E_0\). Since \(\alpha\le2g/3\), (10) gives
\[
 |g'|\le22K+\frac{20}{3}K^2.
 \tag{11}
\]
Writing P=H3, the full Laplacian commutator gives exactly
\[
\begin{split}
 N'={}&-2P+\alpha\int d|\Delta W|^2
 +4\alpha\langle\Delta W,Dv:\nabla^2W\rangle\\
 &+2\alpha\langle\Delta W,(\Delta v+2\nabla d)\cdot\nabla W\rangle
 +2\alpha\langle\Delta W,(\Delta d)W\rangle.
\end{split}
 \tag{12}
\]
Use \(\|Dv\|_\infty\le6\), \(\|\Delta v\|_\infty\le40\),
\(\|\nabla d\|_\infty\le40\), \(|\Delta d|\le30\), and d<=6.
The equality \(\|\nabla^2W\|_2^2=N\) is whole-space Plancherel.
Consequently
\[
 |n'|\le2P/E_0+\alpha\{30n+240\sqrt{ng}+60\sqrt n\}
       \le2K+220K^2.
\]
Together with (11) and g<=K this gives
\[
 |\nu'|\le |n'|+2g|g'|
 \le2K+264K^2+\frac{40}{3}K^3=M.
 \tag{13}
\]
Thus \(\nu(s)\ge\nu_0/2\) on the fully paid interval \([0,h]\).
Neither its sign nor its size is extrapolated beyond that interval.

## 4. Strict restart and the closed-horizon compression bound

Retain the exact [Note42][n42] radial remainder:
\[
 G'=-2N+\alpha\{10G+(21/4)E_0-\mathscr H_{\rm rad}\},\qquad
 \mathscr H_{\rm rad}\ge0.
\]
Using \(N/E_0=g^2+\nu\) and \(\alpha\le2g/3\) yields
\[
 \boxed{g'\le ag^2+bg-2\nu.}
 \tag{14}
\]
This is the one diffusion mechanism selected at intake. On [0,h], it
improves to \(g'\le ag^2+bg-\nu_0\). The old solution y obeys
\(y'=ay^2+by\). Standard scalar comparison first gives y>=g; subtracting
then gives
\[
 (y-g)'\ge\{a(y+g)+b\}(y-g)+\nu_0\ge\nu_0.
\]
Therefore \(g(h)\le y_h-\nu_0h=g_1\). The last restriction in (2)
ensures \(g_1\ge g_0/2\); the saving is strictly positive.

Restart only the old scalar comparison at h, now from g1. For
\(0\le t<L(g_1)\), put
\[
 \delta_1(t)=1-\frac{4g_1}{3}(e^{bt}-1).
\]
Initially before any possible maximal endpoint,
\[
 g(h+t)\le\frac{g_1e^{bt}}{\delta_1(t)},\qquad
 B(h+t)\le-\frac17\log\{\delta(h)\delta_1(t)\}.
 \tag{15}
\]
If the maximal lifespan ended before h+L(g1), the first bound would
keep G bounded, contradicting Note28's continuation criterion. Thus
\(S_{\max}\ge h+L(g_1)\). Since L is strictly decreasing and
\(h+L(y_h)=L(g_0)\), this new bound is strictly larger than the old one.
The exact gain is
\[
 L_{\rm new}-S_{\rm tar}=L(g_1)-L(y_h)
 =\int_{g_1}^{y_h}\frac{du}{au^2+bu}>0.
 \tag{16}
\]
At the target endpoint, elementary algebra gives
\[
 \delta_1(S_{\rm tar}-h)=1-g_1/y_h=\eta>0,
\]
which proves (3). Uniformly on the closed target interval one may use
\[
 \bar g=\max\left\{y_h,
          \frac{g_1e^{b(S_{\rm tar}-h)}}{\eta}\right\},\qquad
 G\le E_0\bar g,\quad\alpha\le\frac23\bar g,
\]
\[
 \boxed{\int_0^{S_{\rm tar}}G(s)\,ds\le3E_0B_*.}
 \tag{17}
\]
The last bound uses \(\alpha\ge G/(3E_0)\). All right sides are finite
initial-data expressions. None contains an uncontrolled B.

## 5. Source residual, true jets, boundaries and downstream costs

Keep the exact residual of Notes31/40,
\(\mathcal R=\mathcal A_TW-\Theta\), with
\(\Theta=(AV,V+AJ_2)\), \(Z=\omega\mathcal R\),
\(\omega=(1+r^2)^{-2}\), \(Y=\|Z\|_2^2\), \(Q=\|J_2\|_2^2\),
and \(\mathcal F=G+Y+Q\). In particular
\(J_{2,s}=-\mathcal P_s^pK_1*(u^2F_0)\): multiplication precedes
preparation, and the mark and its feedback path are held fixed.

The source operator remains \(\mathcal A_T=b_T\cdot\nabla+c_T\),
\(b_T=\eta_{\rm cut}(r)\log r\,X\),
\(c_T=-\eta_{\rm cut}r\log r\,\ell_T'\), with the original cutoff.
The initial residual \([\mathcal A_T,K_1*](F_0,F_1)\) is genuinely
nonzero. Its evolution uses the complete commutators
\[
 \mathscr C_0=-2(\partial_j b_{T,i})\partial_{ij}
 -(\Delta b_T+2\nabla c_T)\cdot\nabla-\Delta c_T,
\]
\[
 \mathscr C_1=(b_T\cdot\nabla v-v\cdot\nabla b_T)\cdot\nabla
                  +b_T\cdot\nabla d-v\cdot\nabla c_T.
\]
Every cutoff derivative is retained. At r=1 the combined numerator
\(\Theta+\mathcal R\) vanishes; no separate singular quotient is used.
All energies and derivative estimates above include the whole inner ball.
The large-radius cutoff errors vanish by the inherited weighted decay.
No spatial partition or new interface is introduced.

There is a complete downstream consumer, using Note47's unchanged
source/cutoff budgets \(\kappa_0=8+A_2^2+A_1+A_0\),
\(\kappa_{1,\rm src}=274/25+B_1+B_0\), whose definitions and full-tail
finiteness are proved in Notes40/47. Put \(\zeta=\delta(h)\eta\in(0,1)\).
For every \(0\le s\le S_{\rm tar}\), its estimate now becomes
\[
 \boxed{\mathcal F(s)+E_0\le
 (\mathcal F(0)+E_0)e^{\kappa_0S_{\rm tar}}
                     \zeta^{-\kappa_{1,\rm src}/7}.}
 \tag{18}
\]
The right side also bounds \(\mathcal F(s)+E_0+\int_0^s
(\mathscr D+\alpha\mathscr H_{\rm rad})\), by Note47 (21) and
monotonicity of its integrating exponent; \(\mathscr D=N+2\|\nabla Z\|_2^2
+2\|\nabla J_2\|_2^2\). On any fixed spatial ball, multiply the
resulting Y allowance by \((1+R_b^2)^4\) for the residual norm.
Also \(Q(s)\le Q_0\zeta^{-6/7}\), and the accepted R7 minimum may
be used with this value of X. The earlier second-order commutator,
actual-jet and interior payments remain in (18).

The g estimate and the weighted estimate are separate valid inequalities
on the same trajectory. We substitute the independent B bound into the
latter; we do not add their dissipation terms or spend diffusion twice
in one energy identity.

## 6. Matched comparison, controls and limits

Against Note42 with the same E0,G0 and diffusion, the former allowance
is singular at S_tar; (3), (17), (18) are finite there. The strict gain
(16) costs the initial spatial variance and a paid H3 budget. An equally
informed direct energy argument can use exactly this diffusion remainder;
no acquisition advantage or theorem of optimality is asserted.

At this particular theta mark, the same complete-source information
already yields \(-H_a\ge35M_2/18>0\) in Note55. Combining that margin
with [Note29][n29] supplies bounds on every finite auxiliary horizon.
That is the stronger equally informed direct-information alternative.
The present proof does not consume that margin and therefore gives a
separate, generic finite-horizon estimate; it creates no new physical
collision-free region and does not replace the source-specific objective.

| Registered comparison | Premise audit for this diffusion mechanism |
| --- | --- |
| Gaussian-polynomial cosine control | Its nonzero prepared radial Schwartz pair has positive variance and finite H3, including at its exact event (1/4,2 sqrt(6)). It shares every sufficient premise of the generic lemma. Theta arithmetic fails, but is unused as a separator here. Its own L_new remains compatible with Smax<=S*; no deadline payment follows. |
| R6 fixed-amplitude polynomial kernels | Full cosine/Newman compatibility fails, but their admitted prepared nonzero radial fields still share this diffusion lemma. Literal cosine is kept for the theta application and is not used to exclude these controls. |
| Weighted-square | Unit coefficients/full reflection fail; positive prepared finite-moment fields share the lemma. Registered event heights near44.13 and83.53 remain outside the frozen application mark. No variance failure is claimed. |
| Finite-prime orbit | Full reflection/canonical source fail; admitted smooth finite-moment fields share the lemma. High-gap events keep their original location qualifications. |
| Reflected super-Gaussian | Full square arithmetic fails; smooth preparation shares the diffusion premises. Its pi/4 event is elsewhere. |
| Smooth shape / positive primitive | Their shape and primitive data do not fix theta. On the inherited finite-spatial-moment domains the diffusion premises are shared; no event is newly placed at this mark. |
| Euler-factor | Modified source/conductor fail the canonical identity. Admitted prepared data share the lemma; a Laguerre witness is not automatically a double event here. |
| Atomic/profile and continuous compact | Atomic inputs remain outside the imported source-function theorem. An admitted continuous prepared comparison shares the lemma with its own data; no extension to atoms is needed. |
| RH-conditional endpoint | Retain the RH condition, altered arithmetic and escaping heights. Where the inherited preparation class applies, this lemma gives no additional failed premise. |

For any admitted zero-mass control, Note28 still forces finite breakdown.
The proved lower horizon must therefore satisfy \(L_{\rm new}\le S_*\)
for that control. This is a consistency consequence of two theorems,
not a newly measured comparison. With the theta operator its genuine
initial residual still includes the preparation commutator **and** its
raw mismatch, as in Note40 (23).

**A strict local restart is not a global continuation estimate.** Repeated
restarts would require new bounds preventing the gaps and time increments
from collapsing. No positive sum of restart intervals or uniform variance
floor is proved. This is the precise remaining limitation, not a universal
obstruction to other diffusion or signed-production methods.

## 7. Disposition and provenance

Stop this single R8 candidate with (3). **B02 R8 is complete in-note;
parent B02 remains partial.** The next task is **[E] CTF-E08 R8 — Sol**,
a fixed proof/cost/scope assessment under [the packet][packet] and
[Continuation60][next]. No E07 execution is needed because the selected
bounded proof is supplied. E03/B03 remain gated; no numerical source
acquisition, PDE evolution, second candidate or manuscript expansion was
performed. A small [exact arithmetic check][check] verifies the displayed
combinatorial constants and illustrative rational endpoint identities;
it is not a source certificate or substitute for the proof.

Actual thread `01a18952-7213-7501-9ef1-a7aeddd83e80`, turn
`01a18953-1229-7ed3-8afb-407cc03308a3`, **gpt-6-astra / max**.
[Public chat0028][history] has its own registration; no subagents were used.
The current session includes an interrupted Sol/ultra opening; no research
result from that opening is attributed to Sol. Model change does not
provide specialist independence. Review31 is by this same assistant.

The only classical reference rechecked here is Plancherel in
[Hunter, Theorem5.71, printed p.171](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
29 October 2026, already cataloged in [reference11][ref11]. Hunter uses
forward normalization (2pi)^(-3); (5) uses the equivalent unnormalized
forward convention. The derivative budgets, variance persistence and
restart bounds are derived here. No priority claim or new literature
theorem is imported. Input hashes in the E08 packet identify the frozen
sources and both unchanged TeX files; hashes do not validate mathematics.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n47]: 47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[n55]: 55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[n58]: 58_COMPRESSION_CONTROL_AND_MODEL_CONTINUATION_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[review]: ../reviews/31_DIFFUSION_VARIANCE_B02_R8_SELF_ASSESSMENT_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_DIFFUSION_VARIANCE_ASSESSMENT_REQUEST_R8_20261029.md
[next]: 60_DIFFUSION_VARIANCE_AND_MODEL_CONTINUATION_20261029.md
[check]: ../numerics/25_DIFFUSION_VARIANCE_CONSTANT_CHECKS_20261029.json
[history]: ../chat-histories/0028_2026-10-29T20-20-44Z_continue-ctf-b02-with-astra.json
[ref11]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
