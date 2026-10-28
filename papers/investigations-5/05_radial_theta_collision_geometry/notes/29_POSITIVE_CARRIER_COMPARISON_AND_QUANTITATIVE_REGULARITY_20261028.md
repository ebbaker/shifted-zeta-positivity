# CTF-B02: positive-carrier comparison and quantitative regularity

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, Investigation05 chat0010, **Continue radial theta collision**.

**Status: first bounded B02 return; the estimates below are proved in-note, with same-assistant analytical checking.** The result is an explicit conversion of an independently known physical first-jet margin into bounds for the fixed [Note28][n28] flow. The positive-carrier dissipation itself supplies no such margin. Applying the conversion to the existing fourth-moment estimate gives regularity on its already covered bounded domain, with no enlarged collision-free region.

The quantitative additions are a sharp mass–energy–moment inequality, an explicit compression/gradient bound with its first-jet dependence exposed, and an explicit carrier-moment bound on amplitude growth at collision breakdown. No numerical evolution, new quadrature, interval certificate, or independent specialist review is reported. The broader canonical estimate remains open.

| Next task | Type | Recommended model | Readiness | Output |
| --- | --- | --- | --- | --- |
| CTF-B02, next bounded route | B — brainstorm | Astra: a propagated signed theta relation is missing | Ready; this carrier-only route has returned | Establish a source-specific estimate for the signed gradient production, or identify the precise failure of one proposed relation |
| CTF-E02 R1 | E — execution, optional | Sol | Existing fixed packet; not a prerequisite | Size/source of the already proved initializer-payment gap |
| CTF-E03 | E — execution | Sol | Gated on a new inequality requiring finite rigorous inputs | Only the quantities that inequality consumes |

[Progress04][progress] owns live status. [Continuation30][continuation] specifies the next bounded question. This return follows the [result index][results], [avoid index][avoid], [control screen][controls], [target-classification rule][a01], [shape-only warning][a02], and [scope rule][a07].

## 1. Fixed flow and the comparison being tested

Retain Note28's whole-space flow, preparatory smoothing time1, unit jet weight, and fixed mark p=(T,A):
\[
 W=(U,V),\qquad
 \partial_s W=\Delta W+\alpha(s)\operatorname{div}(vW),\qquad
 v=X+\frac{X}{1+|X|^2},
\]
\[
 E_0=\int|W|^2>0,\quad G=\int|\nabla W|^2,\quad
 D=\int(\operatorname{div}v)|W|^2,\quad
 \alpha=\frac{2G}{D},\quad B(s)=\int_0^s\alpha(q)\,dq.
 \tag{1}
\]
Here V is the actual spectral derivative of the common propagator family with the mark held fixed, exactly as in Note28. The carrier below is a comparison solution; it changes neither component nor the feedback coefficient. In this note A denotes the physical frequency, not the manuscript's squared coordinate lambda=a²/4.

The inherited bounds used are
\[
 3E_0\le D\le6E_0,\qquad
 \alpha\le\frac{2G}{3E_0},\qquad
 G(s)+3E_0\le(G(0)+3E_0)e^{10B(s)}.
 \tag{2}
\]
Note28 establishes local existence, complete mass preservation, the continuation criterion, and finite breakdown when both masses vanish. We use those results within their stated Schwartz/moment class.

The attempted improvement is specific: use the complete positive theta amplitude to dominate both signed components, then combine its moment equation and relative-density dissipation to control B and G. We test what information this comparison actually retains. Note28 has already classified global regularity as a pointwise noncollision reformulation; the calculation below quantifies its converse without proposing another criterion.

## 2. A positive carrier for the complete source and actual jet

Write
\[
 q_T(u)=e^{Tu^2}\Phi(u),\qquad
 \rho_T(X)=\mathbf1_{r\ge1}\frac{q_T(u)}{8\pi r^3},
 \quad r=|X|,\quad u=\tfrac12\log r.
\]
The spherical Jacobian gives \(\int\rho_T b(u)\,dX=\int_0^\infty q_T(u)b(u)\,du\). Set
\[
 W^{\rm raw}=\rho_T(\cos(Au),-u\sin(Au)),\qquad
 h^{\rm raw}=\rho_T(1+u^2),
\]
\[
 W_0=K_1*W^{\rm raw},\qquad h_0=K_1*h^{\rm raw}.
 \tag{3}
\]
The entire theta sum is present. No absolute value of H or H_a is substituted into the source. Since
\[
 \cos^2(Au)+u^2\sin^2(Au)\le1+u^2\le(1+u^2)^2,
\]
we have \(|W^{\rm raw}|\le h^{\rm raw}\) and hence \(|W_0|\le h_0\).

Along the existing W trajectory let h solve the same scalar linear equation:
\[
 \partial_s h=\Delta h+\alpha(s)\operatorname{div}(vh),\qquad h|_{s=0}=h_0.
 \tag{4}
\]
On every compact interval before the maximal lifespan, Note28's positive mass-preserving kernel gives
\[
 h>0,\qquad |W|\le h,\qquad
 M:=\int h=P_0(T)+P_2(T),
 \quad P_j(T)=\int_0^\infty u^j q_T(u)\,du.
 \tag{5}
\]
The vector mass is
\[
 m=\int W=(H(T,A),H_a(T,A)),\qquad \mu=|m|.
 \tag{6}
\]
All integrals include the unit ball after smoothing and evolution.

For the carrier second moment \(R(s)=\int |X|^2h_s\,dX\),
\[
 R_0=\int_0^\infty e^{4u}(1+u^2)q_T(u)\,du+6M,
\]
\[
 R'=6M-2\alpha\int X\cdot v(X)h\,dX
       \le6M-2\alpha R.
 \tag{7}
\]
The number6 is \(\Delta|X|^2\) in three dimensions; the preparatory K1 has second moment6. Theta's complete tails give all required moments on compact physical parameter sets. The same conclusion holds for the exact control on T<T_c+4.

## 3. Relative-density dissipation and the missing lower bound

Define
\[
 Z=W/h,\qquad
 \mathcal F(s)=\int h|Z|^2=\int\frac{|W|^2}{h},\qquad
 \mathcal I(s)=\int h|\nabla Z|^2.
\]
Direct subtraction of (1) and (4) gives
\[
 \partial_s Z=\Delta Z+(2\nabla\log h+\alpha v)\cdot\nabla Z,
\]
\[
 \partial_s(h|Z|^2)
 =\Delta(h|Z|^2)+\alpha\operatorname{div}(v h|Z|^2)
       -2h|\nabla Z|^2.
 \tag{8}
\]
Thus, in integrated form on every compact lifespan interval,
\[
 \boxed{\mathcal F(s)+2\int_0^s\mathcal I(q)\,dq=\mathcal F(0).}
 \tag{9}
\]
This is the classical quadratic general-relative-entropy identity; [reference12][ref12] records the checked lemma and its application here. It is derived above rather than imported as a nonlinear feedback theorem.

For completeness, use nonnegative radial cutoffs tending to1 in (8). Since \(|Z|\le1\), \(h|Z|^2\le h\). The Laplacian cutoff error is bounded by \(C R_{\rm cut}^{-2}\int h\), and the drift error by \(C\sup\alpha\int_{|X|\ge R_{\rm cut}}h\), because v has linear growth. These errors vanish, uniformly on compact lifespan intervals. Monotone cutoffs and the nonnegative dissipation give (9) by passage to the limit. The initial quotient is continuous under the smoothing; \(h_0>0\), and the same domination gives the initial limit. This accounts for complete spatial boundaries without assuming a uniform lower bound for h.

Cauchy–Schwarz inside the preparatory convolution and then mass preservation give
\[
 \mathcal F(0)
 \le\int_0^\infty q_T(u)
       \frac{\cos^2(Au)+u^2\sin^2(Au)}{1+u^2}\,du
 \le P_0(T).
 \tag{10}
\]
At every time there is the exact orthogonal decomposition
\[
 \boxed{\mathcal F(s)=\frac{\mu^2}{M}
            +\int h_s\left|Z_s-\frac mM\right|^2.}
 \tag{11}
\]
In particular, the nondecaying constant part supplied by this decomposition is exactly \(\mu^2/M\). Theta positivity supplies M>0 and the upper bound (10); neither is a positive lower bound on \(\mu\). The dissipative term is nonnegative and is subtracted in (9), so a positive initial value of \(\mathcal F\) cannot be carried forward as a positive uniform floor merely by monotonicity.

Equation(11) does not exclude additional lower bounds from further source information. The scoped issue is whether the displayed positive-carrier data and dissipation alone supply the missing floor. Section6 gives an actual colliding trajectory on which they do not.

## 4. A sharp mass–energy–moment bound

For any vector field W in L1 intersect L2, with \(E=\|W\|_2^2>0\), and any nonnegative carrier \(h\ge|W|\) with finite \(R=\int |X|^2h\), one has
\[
 \boxed{R\ge c_3\frac{\|W\|_1^{7/3}}{E^{2/3}}
            \ge c_3\frac{|\int W|^{7/3}}{E^{2/3}},
 \qquad
 c_3=\frac37\left(\frac{15}{14\pi}\right)^{2/3}.}
 \tag{12}
\]
This elementary inequality is proved here; no literature-priority claim is made.

For any L>0, write the L1 mass using \(1-|X|^2/L^2\), discard its negative part, and apply Cauchy–Schwarz:
\[
 \|W\|_1\le
 E^{1/2}\left(\int(1-|X|^2/L^2)_+^2\,dX\right)^{1/2}
             +R/L^2
 =a_3E^{1/2}L^{3/2}+R/L^2,
\]
where \(a_3^2=32\pi/105\). Maximizing
\(\|W\|_1L^2-a_3E^{1/2}L^{7/2}\) gives
\(L^{3/2}=4\|W\|_1/(7a_3E^{1/2})\), and hence (12).

The constant is sharp in this general inequality: take
\(W=e\,C(1-|X|^2/L^2)_+\), h=|W|, with a constant unit vector e. Direct integration gives
\[
 \|W\|_1=\frac{8\pi}{15}CL^3,\quad
 E=\frac{32\pi}{105}C^2L^3,\quad
 R=\frac{8\pi}{35}CL^5.
\]
These saturate (12). This extremizer is not asserted to be a theta trajectory or a strictly positive Schwartz carrier. Sharpness here concerns the general comparison inequality.

## 5. Quantitative regularity when a direct margin is available

Suppose an independently established \(\mu>0\) is available. With E=E0 fixed, set
\[
 r_\mu=c_3\mu^{7/3}E_0^{-2/3}>0.
\]
Equations(7),(12) give \(R(s)\ge r_\mu\) throughout the lifespan and
\[
 (\log R)'\le6M/r_\mu-2\alpha.
\]
Consequently
\[
 \boxed{B(s)\le\frac12\log\frac{R_0}{r_\mu}
                      +\frac{3Ms}{r_\mu},}
 \tag{13}
\]
\[
 \boxed{G(s)+3E_0\le
 (G(0)+3E_0)\left(\frac{R_0}{r_\mu}\right)^5
             \exp\!\left(\frac{30Ms}{r_\mu}\right).}
 \tag{14}
\]
Here \(R_0/r_\mu\ge1\). The bounds first hold before the maximal lifespan. Their finiteness on every finite interval, combined with Note28's continuation theorem, proves global existence and extends them to every s>=0. The response obeys \(\alpha\le2G/(3E_0)\).

This exposes the price hidden in the qualitative converse: for fixed remaining budgets, the exponential rate in this estimate deteriorates as \(\mu^{-7/3}\). It is a sufficient upper bound, not a sharp asymptotic for the actual trajectory. No inverse first jet has been inserted into the PDE; the first-jet dependence occurs explicitly in the comparison.

If only \(\mu\ge\underline\mu>0\), \(E_0\le\overline E\), \(M\le\overline M\), \(R_0\le\overline R\), and \(G(0)\le\overline G\) are known, use
\[
 r_* = c_3\underline\mu^{7/3}\overline E^{-2/3}
\]
and replace the constants in (13),(14) by those upper budgets, dropping \(-3E_0\) in the resulting upper bound for G. Also (12) at time0 gives the uniform lower energy
\[
 E_0\ge\underline E
 :=c_3^{3/2}\underline\mu^{7/2}\overline R^{-3/2},
 \tag{15}
\]
so \(\alpha\le2G/(3\underline E)\) is uniformly paid as well.

These estimates give actual finite-time control if a first-jet margin has been acquired. They do not acquire that margin. Passing from \(\mu>0\) to (14) and then citing regularity as evidence for \(\mu>0\) would reverse the dependency.

## 6. What happens to the carrier at a collision

At any finite maximal endpoint, Note28 gives \(B(s)\to\infty\). Integrating (7),
\[
 R(s)\le e^{-2B(s)}R_0
       +6M\int_0^s e^{-2(B(s)-B(q))}\,dq\longrightarrow0.
 \tag{16}
\]
For the limit, extend the integrand by zero to the fixed finite endpoint interval; it is bounded by1 and tends to0 for each earlier q. No blow-up rate is assumed.

The stronger first inequality in (12) then gives
\[
 \|W_s\|_1\le c_3^{-3/7}E_0^{2/7}R(s)^{3/7},
\]
\[
 \boxed{\mathcal F(s)\le\|W_s\|_1
       \le c_3^{-3/7}E_0^{2/7}R(s)^{3/7}\longrightarrow0,}
 \tag{17}
\]
and
\[
 \boxed{\|W_s\|_\infty
       \ge c_3^{3/7}E_0^{5/7}R(s)^{-3/7}\longrightarrow\infty.}
 \tag{18}
\]
The first inequality in (17) uses \(|W|\le h\). The amplitude bound follows from \(E_0\le\|W\|_\infty\|W\|_1\). These are quantitative bounds in terms of the carrier moment; they do not specify a power of the remaining auxiliary time or a blow-up profile.

For Note28's exact control
\[
 \Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\quad T_c=\tfrac14,\quad A_*=2\sqrt6,
\]
\[
 H_*(T_c,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16},
\]
so \(\mu=0\), while
\[
 P_0=\frac{9\sqrt\pi}{4},\quad P_2=\frac{21\sqrt\pi}{32},
 \quad M=\frac{93\sqrt\pi}{32}>0.
\]
The smoothed pair is nonzero, so \(\mathcal F(0)>0\). All identities(3)–(12) hold and Note28 supplies its finite deadline. Nevertheless \(\mathcal F(s)\to0\) by (17). Thus positivity of the carrier, its initial relative energy, finite moments, and this dissipation identity do not furnish a positive uniform relative-energy floor through the collision deadline.

This control fails canonical square arithmetic and the literal theta tail, but no step in the tested carrier comparison uses either as a separating premise. This is a failure of this comparison, not of every bound using the complete theta source.

## 7. Actual theta specialization and matched direct information

The comparison can be fully paid on a domain already covered by [Note16][n16]. This is a useful consistency check of the analytical interface, not a numerical test.

Fix finite \(T_+\ge0\), \(A_+\ge0\) satisfying
\[
 \vartheta:=\frac{A_+^4P_4(T_+)}{24P_0(T_+)}<1.
\]
For \(0\le T\le T_+\), \(0\le A\le A_+\), Note16's direct inequality and monotonicity of P4/P0 give
\[
 H(T,A)-\frac A2H_a(T,A)
 \ge P_0(0)(1-\vartheta),
\]
and hence
\[
 \underline\mu
 =\frac{P_0(0)(1-\vartheta)}{\sqrt{1+A_+^2/4}}>0.
 \tag{19}
\]
For A>0 the source inequality is strict; at A=0 the displayed weak bound is immediate. The strict interior condition \(\vartheta<1\) is required for this explicit uniform margin. We do not extend (19) to the boundary \(\vartheta=1\).

Define the complete-source budgets
\[
 \overline M=P_0(T_+)+P_2(T_+),\qquad
 \overline E=(8\pi)^{-3/2}\overline M^2,\qquad
 \overline G=\tfrac34(8\pi)^{-3/2}\overline M^2,
\]
\[
 \overline R=\int_0^\infty e^{4u}(1+u^2)q_{T_+}(u)\,du+6\overline M.
 \tag{20}
\]
They are finite. Positive time weights give M<=Mbar and R0<=Rbar. Young's inequality with K1 and its gradient gives the energy and gradient budgets. Note16's complete Gaussian-tail bounds can bound these integrals analytically; no new numerical values are needed for this theorem.

With \(r_*=c_3\underline\mu^{7/3}\overline E^{-2/3}\), the explicit uniform conclusion is
\[
 B(s)\le\tfrac12\log(\overline R/r_*)+3\overline M s/r_*,
\]
\[
 G(s)\le(\overline G+3\overline E)(\overline R/r_*)^5
                       e^{30\overline M s/r_*},\qquad s\ge0,
 \tag{21}
\]
and (15) gives the corresponding alpha bound.

Every point in this domain was already separated by (19) before evolving the field. The new flow bound uses the identical source moments and direct linear combination. It gives no larger domain, no cheaper acquisition, and no independent collision exclusion. The exact control has \(A_*^4P_4/P_0=123>24\), so it fails this direct margin condition at its event, as it must.

## 8. Control screen and disposition

| Control class | Application of this comparison | Premise missing from the canonical source; what the bound actually uses |
| --- | --- | --- |
| Exact Gaussian-polynomial | All carrier identities hold on T<T_c+4; relative energy tends to0 at its collision | It lacks complete theta arithmetic/tails. The quantitative regularity estimate fails there because its required direct margin is zero |
| Euler-factor | Smooth source/finite-moment cases use the same carrier algebra | Modified Euler factor/conductor; this comparison does not use their canonical values |
| Weighted-square and finite-prime | Positive half-line sources pass on their moment domains | Unchanged full coefficients/reflection fail; support or selected arithmetic alone is unused as a separator |
| Reflected super-Gaussian, smooth shape, positive primitive | Same relative-density and moment identities apply on their stated domains | Full canonical square source fails; positivity, reflection, or auxiliary positivity do not supply (19) at an event |
| Atomic / RH-conditional endpoint controls | Not newly extended or instantiated here | Atomic inputs are outside Note28's source-function statement; conditional controls retain their original hypothesis |

The [control register][controls] supplies the original family statuses. No earlier certificate or witness is recomputed. At any admitted actual collision, the premise \(\mu>0\) fails by definition; that is direct observation information, not a newly discovered arithmetic discriminator.

**Bounded result:** the carrier construction, sharp inequality(12), explicit regularity payment(13)–(15), endpoint bounds(17)–(18), and uniform theta specialization(19)–(21) are established by the displayed arguments. The classical relative-entropy step is attributed. All checking is by the same assistant; [assessment17][review] records its scope.

**Scoped failure:** inferring a positive uniform relative-energy floor from its positive initial value and monotone dissipation is false for this source class. The explicit moment-based regularity bound derived here requires an independently supplied direct margin. The exact control shows why that missing input cannot be omitted from this argument. This return does not rule out different quantitative combinations of canonical moments or other theta-specific relations.

**B02 remains partial.** Do not issue E03 merely to evaluate (20) on the already separated domain, and do not run a PDE to retest the exact control's known divergence. A further analytical attempt must retain additional signed canonical information and prove its propagation. The next bounded question and stop rule are in [Continuation30][continuation]. No manuscript source or previous note was rewritten.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n16]: 16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[progress]: ../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[continuation]: 30_CONSERVATIVE_CARRIER_COMPARISON_CONTINUATION_20261028.md
[ref12]: ../references/12_GENERAL_RELATIVE_ENTROPY_CARRIER_COMPARISON_20261028.md
[review]: ../reviews/17_POSITIVE_CARRIER_AND_REGULARITY_B02_ASSESSMENT_20261028.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
