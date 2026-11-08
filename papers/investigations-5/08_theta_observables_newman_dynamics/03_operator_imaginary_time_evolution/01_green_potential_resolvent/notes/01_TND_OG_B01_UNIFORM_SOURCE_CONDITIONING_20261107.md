# B01: uniform-source conditioning of the Green/resolvent interface

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual recorded model/effort: **gpt-6-astra / max**, branch chat0001.

**Evidence:** §§1–5 are an analytical derivation from the inherited complete Green identity, checked by the same assistant only. They prove a scoped square-root stability obstruction for a fixed translated-source family. Section 6 is a selected proof route, **not an executed canonical residual theorem**. No favorable canonical Green bound, zero exclusion, numerical experiment or novelty claim is made.

The [B01 decision](../brainstorm/notes/01_TND_OG_B01_RESOLVENT_CONDITIONING_DECISION_20261107.md) owns mechanism selection; [the live register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md) owns status. The [source-use receipt](../references/01_TND_OG_B01_SOURCE_USE_20261107.md) records exactly what was inspected.

## 1. The question that this calculation answers

Parent [Decision17 §6](../../brainstorm/notes/17_TND_O_B04_R5_SIGNED_ACQUISITION_DECISION_20261107.md) lets a prime grow: its safe-line data converge while the added Green potential diverges, but source/count constants are not uniform. The focused clarification here asks whether **common quantitative source bounds** alone remove the problem for a first-order resolvent comparison.

They do not give a Lipschitz comparison. Fix the prime **2** throughout. A positive, even, exactly normalized complete-source perturbation of relative size η has all fixed safe-line resolvent jets of size O(η), but changes the Green statistic by **Θ(√η), uniformly at all real centers**. This is a continuity/conditioning obstruction, unlike the earlier discontinuity across a nonuniform class. It does not rule out a square-root modulus, collision-resolving accuracy, signed arithmetic information or an estimate restricted to the unchanged theta source.

Let H=H₀ and Φ be the exact canonical source from the parent [source section](../../manuscript/sections/02_source.tex). Retain a=π/8, K(t)=1/(16 cosh(at)), and

\[
G(t,y)=\operatorname{atanh}\frac{\sin(ay)}{\cosh(at)}.
\]

For a function f for which the integrals exist, write

\[
\mathcal J[f](X)=\int_{\mathbb R}K(x-X)
 [\log|f(x)|+\log|f(x+8i)|],dx-\log|f(X+4i)|.
\tag{1}
\]

For canonical H this is the inherited J₀ᴳ. Parent [Note25 §§1–4](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) supplies its complete zero sum, logarithmic integrability, scalar cancellation and defect margin. No all-real assumption on H is used below.

## 2. A fixed-prime family with common complete-source bounds

Set

\[
\alpha=\tfrac12\log2,\qquad
S_\alpha(u)=\tfrac12[\Phi(u+\alpha)+\Phi(u-\alpha)],
\]
\[
\Psi_\eta(u)=\frac{(1+\eta)\Phi(u)+(1-\eta)S_\alpha(u)}2,
\qquad 0\le\eta\le\eta_0:=\tanh^2(\alpha/4).
\tag{2}
\]

Thus d(η)=(2/α)atanh√η lies in [0,1/2]. These are strictly positive, smooth even sources. Their transforms are exactly

\[
f_\eta(z)=\tfrac12\int\Psi_\eta(u)e^{izu}du
=H(z)M_\eta(z),
\quad M_\eta(z)=\cos^2(\alpha z/2)+\eta\sin^2(\alpha z/2).
\tag{3}
\]

The half-Fourier normalization is retained. All fη(0)=H(0), because translations preserve the integral and Mη(0)=1. Equivalently Mη=(1+cη cos(αz))/(1+cη), cη=(1−η)/(1+η)=sech(αd). This is the existing Euler control's scalar normalization, with prime fixed and amplitude varied.

The full source difference is particularly simple:

\[
\Psi_\eta-\Psi_0=\frac\eta2(\Phi-S_\alpha),\qquad
|\Psi_\eta-\Psi_0|\le\eta\Psi_0.
\tag{4}
\]

In fact the supremum relative distance equals η. For u→+∞, the first theta term gives
Φ(u−α)/Φ(u)∼exp(−9α+π(1−e^(−4α))e^(4u))→∞;
hence Sα/Φ→∞ and |Φ−Sα|/(Φ+Sα)→1. Only the upper bound in (4) is needed for the obstruction.

For any fixed L,b≥0 and nonnegative integers j,q,

\[
\int |u|^j e^{Lu^2+b|u|}|\Psi_\eta^{(q)}-\Psi_0^{(q)}|,du
\le\frac\eta2\int |u|^j e^{Lu^2+b|u|}
(|\Phi^{(q)}|+|S_\alpha^{(q)}|),du<\infty.
\tag{5}
\]

The right-hand constant is independent of η and of the horizontal observation height. Finiteness follows from the complete source majorant and fixed translations. All members therefore have common bounds in every fixed weighted source seminorm. They each admit the exact heat orbit (1/2)∫e^(λu²)Ψη(u)e^(izu)du, with ∂λf=−∂z²f. **η is a source parameter, not Newman time**; (3) is the λ=0 identity, not an asserted product formula at other times.

No finite arithmetic prefix has replaced Φ. If one later approximates it, the positive reflected prefixes Φ_N≤Φ and fixed translates admit a common majorant; mode and radial cutoffs tend to the complete field uniformly in η for each fixed weighted norm. Resolve an O(η) input difference by choosing those errors o(η), after η is specified. This is a permissible sequence of finite acquisitions, not a fixed cutoff for all η or a useful cost theorem. No such acquisition was run.

## 3. Complete Green difference and its uniform scale

Put ℓ=2π/α and x_k=(2k+1)π/α, k∈ℤ. At η=0, M₀ has double real zeros x_k. For η>0, its zeros are exactly the simple multiplier zeros

\[
x_k\pm i d(\eta),\qquad d(\eta)=\frac2\alpha\operatorname{atanh}\sqrt\eta.
\tag{6}
\]

If an H zero coincides with one, multiplicities add; simplicity of the full product is not claimed. The added lattice has a common unit-count bound because α is fixed. Together with the canonical count this gives common full-count constants for the entire family.

Apply the strip Green formula to the periodic multiplier. Its horizontal log-modulus is bounded above, its isolated boundary logarithms are integrable, and it has no zeros at heights 4 or 8. On the periodic cylinder, the difference between the Green-corrected log and its harmonic extension has zero boundary values and is bounded; the maximum principle makes it zero. Equivalently sum the exponentially decaying strip kernels over the lattice. At η=0 the real boundary doubles have **zero** interior Green contribution. Consequently

\[
\Delta_\eta(X):=\mathcal J[f_\eta](X)-\mathcal J[f_0](X)
=\sum_{k\in\mathbb Z}G(X-x_k,d),\qquad
\mathcal J[f_0]=\mathcal J[H].
\tag{7}
\]

This is the complete multiplier contribution, with no omitted residue or outer term. It is independent of any unproved value of the canonical J₀ᴳ. The series is absolutely convergent, uniformly in X modulo its period and d≤1/2.

Using the nearest lattice point and the inherited bound
G(t,d)≤K_G d e^(−a|t|), K_G=2a/cos²a, gives

\[
\boxed{\quad
\frac{\sin a}{\cosh(a\ell/2)},d
\le\Delta_\eta(X)
\le K_G\coth(a\ell/2),d,
\quad X\in\mathbb R.
\quad}
\tag{8}
\]

Indeed the nearest point is at distance at most ℓ/2. For the upper bound, the periodized exponential has maximum (1+e^(−aℓ))/(1−e^(−aℓ)), attained at a lattice point. The same geometric series bounds the omitted lattice tail by Cα d e^(−aR), uniformly in X. There is no hidden growing-height factor in this **difference**; do not replace the canonical full-boundary tail from Note25 by this smaller multiplier tail.

Since

\[
\frac2\alpha\sqrt\eta\le d(\eta)
\le\frac{2}{\alpha(1-\eta_0)}\sqrt\eta,
\tag{9}
\]

(8) is a uniform two-sided √η comparison. At X=x_k even the single nearest zero gives Δ≥sin(a)d. It is an actual defect signal, not a numerical near-zero diagnostic.

## 4. Full resolvent change on fixed safe lines

Let Rη=fη′/fη, R*=f₀′/f₀ and Bη=(1+η)/(1−η)=cosh(αd). Subtraction cancels the common canonical logarithmic derivative **exactly**:

\[
R_\eta-R_*=
\frac{\alpha(B_\eta-1)\sin(\alpha z)}
 {(B_\eta+\cos(\alpha z))(1+\cos(\alpha z))}.
\tag{10}
\]

There is no holomorphic ambiguity to fix: these are literal derivatives of the known quotient. The poles removed from R have not disappeared from (7).

For y>d₀=1/2 and 1≤B≤cosh(αd₀), elementary ellipse geometry gives

\[
|B+\cos(\alpha(x+iy))|\ge\cosh(\alpha y)-B,
\qquad |\sin(\alpha(x+iy))|\le\cosh(\alpha y).
\]

For example the squared first modulus, as a function of t=cos(αx), is
t²+2B cosh(αy)t+B²+sinh²(αy); its minimum on [−1,1] is at t=−1.

Fix b>1 and 0<ρ<b−1. Define

\[
C_{b,\rho}=
\frac{2\alpha\cosh(\alpha(b+\rho))}
 {(1-\eta_0)[\cosh(\alpha(b-\rho))-\cosh(\alpha/2)]
 [\cosh(\alpha(b-\rho))-1]}.
\tag{11}
\]

Equation (10) is at most C_(b,ρ)η throughout the radius-ρ disks about x+ib, uniformly in x. The canonical strip |Im z|≤1 guarantees that the actual resolvents are defined there. Cauchy's derivative estimate therefore gives

\[
\sup_{x\in\mathbb R}|\partial_z^j(R_\eta-R_*)(x+ib)|
\le j!\rho^{-j}C_{b,\rho}\eta,
\qquad j=0,1,\ldots .
\tag{12}
\]

Thus even the **whole safe line**, with any fixed finite jet collection, changes at order η. The explicit factorial cost is retained if j grows; the statement is not a uniform growing-order theorem. Moving contours toward the double zeros is outside the fixed-safe-line class and must pay their degenerating margins.

## 5. Exact implication and control screen

No nondecreasing stability modulus ω(t)=o(√t) can bound |𝒥[f]−𝒥[g]| by ω of the full-source relative distance on a class containing (2), with common constants. Equations (4), (8) and (9) contradict it. The same conclusion holds for an observation distance combining that source distance and finitely many fixed-safe-line jet norms, since each is O(η). In particular a uniform Lipschitz modulus is impossible in this class.

This is **not** a discontinuity theorem: Δ→0. It supplies no universal upper Hölder theorem for arbitrary multiplicities. It does not forbid resolving η at order d², using shrinking contours, retaining signed directional information, or exploiting the literal normalized theta arithmetic. Even exact source values distinguish every member; analytic continuation is still unique.

| Control/information class | What survives | Premise missing from a canonical exclusion |
| --- | --- | --- |
| Fixed-prime family (2) | Positive smooth even complete source; fixed normalization; common weighted bounds and counts; a genuine heat orbit for each source; full safe-line jet stability | Ψη is a translated-source mixture, not Φ. It fails unchanged integer-square theta coefficients/xi identity; fixing p keeps the altered conductor fixed, not equal to conductor one. Baseline Ψ₀ is not theta. |
| Parent growing-prime Euler controls | Named finite safe-line/prefix observations | Literal source, conductor/residue/local roots and uniform source/count bounds; this earlier scope is not changed |
| Weighted-square/prefix controls | Their square support and specified finite endpoints/moments | Complete normalized infinite coefficients and full reflection conjunction |
| Reflected super-Gaussian and smooth/primitive controls | Their recorded positivity, reflection, decay and endpoint data | Exact theta square expansion and unchanged xi/zeta identity |

The last three rows apply the inherited [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md) analytically; no new numerical replay is claimed. A bound below the true one-defect margin must fail on a control box containing its zero. No claim is made about a box missing that zero. This follows [target classification](../../../../../../avoid/01_restating_the_target.md), [premise screening](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The quantitative gain is the removal of drifting source/count constants from the **square-root lower conditioning bound**. It is not a small canonical Green upper bound. No universally all-real conclusion is drawn from generic resolvent/Burgers identities.

## 6. Second mechanism: a frozen short-mollifier transfer, still to prove

The optional coefficient mechanism need not begin with optimization. The newly checked [Radziwiłł v3 Proposition B](../references/01_TND_OG_B01_SOURCE_USE_20261107.md) supplies a stronger diagnostic for short polynomials than the Euler-specific argument. The B01 choice is to test its transfer to the actual normalized residual first.

The [E01 request](../research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md) visibly narrows the exponent to fixed **0<θ<1/2**, permits complex coefficients a₁=1, |a_n|≤1, N≤(T/2)^θ, and fixes one polynomial on the padded center interval I_T=[T−L_T,2T+L_T], L_T=(8/π)log T. It targets

\[
\liminf_{T\to\infty}\inf_{A_T}
\frac1{|I_T|}\int_{I_T}\epsilon_{A_T}(X)^2dX
\ \ge\ \frac1{12\zeta(5/2)^4}>0.
\tag{13, target}
\]

This is **not yet asserted as a proved branch theorem**. The proposed proof combines the primary lower bound, an elementary first-moment contour shift, a uniform safe-line Dirichlet mean, and the nonnegative variance V=|c|²ε². The conservative diagonal allowance is
Στ(n)²n^(−5)≤1+4Σ_(n≥2)n^(−4)≤17/12;
the lower boundary would contribute at least (1+1/θ)/2>3/2. Their difference is the positive 1/12 allowance. The source has the required sharp-cutoff primary statement, avoiding an unproved conversion from a smooth BCR weight.

E01 must still prove the uniformity, first-moment and safe-line estimates, complex conjugation, x=2t scale, enlarged-center convolution, multiplier-zero contribution and normalization. The center-dependent c(X) cannot be replaced by one. An averaged lower bound on ε² would only obstruct uniform smallness of this **sufficient quadratic certificate**, especially as d↓0. It would give no lower bound on J₀ᴳ and no failure theorem for signed logarithmic, adaptive-center, longer-polynomial or θ≥1/2 methods.

Same-assistant checks of §§1–5 covered the source normalization, exact η parameter, all multiplier zeros and multiplicities, complete lattice tails, both constants in (8), the sign of (10), and Cauchy's fixed-order cost. A separate assessor has not checked this note. Primary checking and the proof contract in §6 are preparation, not E01 execution. No manuscript or numerical campaign was opened.
