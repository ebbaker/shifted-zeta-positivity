---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG]
status: proved_source_shape_obstruction_theta_target_open
---

# Source concavity and a positive-time collision control

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This analytic control complements [Note 36](36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md), [Note 50](../04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md), and the open source target in [Note 49](../00_research_coordination/49_OCTONIONIC_SIGNED_BOUND_ANALYTIC_CONTINUATION_20261015.md). No numerical pilot or sampled sign evidence is used.

**Positive, even, decreasing, strongly log-concave sources can retain strict square-variable log-concavity and double-exponential decay while their backward-heat transforms undergo a positive-time collision.** Consequently, these source properties cannot by themselves prove a locally bounded energy-relative lower bound for the signed stationary observation. This is an applicability control for the investigation, not a claim of novelty in the literature or a counterexample for the actual theta source.

## 1. Statement and scope

For a positive even source \(\phi\), define
\[
H(t,z)=\int_0^\infty e^{tu^2}\phi(u)\cos(zu)\,du,
\qquad h_k=\partial_x^kH,
\]
\[
E=h_0^2+h_1^2,\qquad
\mathcal L_0=h_1^2-h_0h_2,\qquad S_0=\{h_1=0\}.
\]
The source constructed below is integrable with every polynomial weight and every real heat multiplier. Its transform is entire in \(z\) and satisfies \(H_t=-H_{xx}\). In a whole time neighborhood of a collision \((T,x_*)\), with \(0<T<1/2\) and \(x_*>0\), the heat-deformed source is positive, even, strictly decreasing on \(u>0\), and uniformly strongly log-concave. In addition,
\[
v\longmapsto\log\{e^{tv}\phi(\sqrt v)\}
\]
is strictly concave for every real \(t\). Nevertheless, on a full stationary predecessor curve,
\[
\boxed{\frac{\mathcal L_0(t,x(t))}{E(t,x(t))}
=-\frac1{T-t}+O(1)\quad(t\uparrow T).}
\tag{1}
\]
Thus no coefficient locally bounded through that event can give \(\mathcal L_0\ge-\kappa_0E\) on its predecessors.

Failure on this one branch suffices to rule out an argument deriving both branch bounds solely from the listed common source properties. It does not exclude stronger assumptions, including theta-specific modular identities, arithmetic coefficients, or a separately proved positive-definiteness property.

## 2. An exact Gaussian-polynomial collision

Set
\[
b=\frac15,\qquad c=\frac1{50},\qquad b^2=2c,
\qquad \phi_0(u)=e^{-u^2}(1+bu^2+cu^4).
\]
Initially restrict to \(a=1-t>0\). Differentiating the Gaussian cosine integral gives
\[
H_0(t,x)=\frac{\sqrt\pi}{2\sqrt a}e^{-x^2/(4a)}
\frac{P_a(x^2)}{16a^4},
\tag{2}
\]
where
\[
P_a(y)=cy^2-(4ba^2+12ca)y
+16a^4+8ba^3+12ca^2.
\tag{3}
\]
For example, the three polynomial factors before collecting denominators are
\[
1+b\left(\frac1{2a}-\frac{x^2}{4a^2}\right)
+c\left(\frac3{4a^2}-\frac{3x^2}{4a^3}
+\frac{x^4}{16a^4}\right),
\]
which verifies (2) directly.

The discriminant of (3), as a polynomial in \(y\), is
\[
\begin{aligned}
\Delta(a)
&=16a^2\{(b^2-4c)a^2+4bca+6c^2\}\\
&=32ca^2(-a^2+2ba+3c).
\end{aligned}
\tag{4}
\]
Its positive zero is
\[
a_c=b+\sqrt{b^2+3c}
=\frac{2+\sqrt{10}}{10},\qquad
T_0=1-a_c=\frac{8-\sqrt{10}}{10}\in(0,1/2).
\tag{5}
\]
The last inclusion follows from \(3<\sqrt{10}<8\). At this value,
\[
P_{a_c}(y)=c(y-y_c)^2,
\qquad y_c=\frac{2ba_c^2}{c}+6a_c
=4+\frac{7\sqrt{10}}5>0.
\tag{6}
\]
Put \(x_c=\sqrt{y_c}\). Equations (2) and (6) yield
\[
H_0(T_0,x_c)=h_1(T_0,x_c)=0,
\]
\[
d_0:=h_2(T_0,x_c)
=\frac{\sqrt\pi}{2\sqrt{a_c}}e^{-y_c/(4a_c)}
\frac{c\,y_c}{2a_c^4}>0.
\tag{7}
\]
This is a nondegenerate double zero. At this stage the source has Gaussian decay and its heat integral is only defined for \(t<1\). The next step removes both restrictions while retaining the collision.

## 3. Double-exponential damping and persistence

For \(\delta>0\), define
\[
\boxed{\phi_\delta(u)=
 e^{-u^2-\delta\cosh(4u)}(1+bu^2+cu^4).}
\tag{8}
\]
For every fixed \(\delta>0\), every real heat time is allowed. The factor \(e^{-\delta\cosh(4u)}\) dominates any Gaussian, polynomial, or fixed exponential multiplier. Hence
\[
H_\delta(t,z)=\int_0^\infty e^{tu^2}\phi_\delta(u)\cos(zu)\,du
\tag{9}
\]
and all required derivatives converge locally uniformly in real \(t\) and complex \(z\). More explicitly, on a compact parameter set, the absolute value of a differentiated integrand with \(p\) heat derivatives and \(q\) spectral derivatives is bounded by
\[
C(1+u^{2p+q+4})
\exp\{A u^2+B u-\delta\cosh(4u)\},
\]
for finite constants \(A,B,C\). This is integrable. The same domination applies to complex heat time on compact sets, so the transform is in fact jointly entire in the heat and spectral parameters for fixed positive damping. Differentiation under the integral verifies the backward heat equation directly; no continuation of a divergent integral is involved. In particular, \(H_\delta\) is entire in \(z\) and \(H_{\delta,t}=-H_{\delta,xx}\).

Consider \(\delta\downarrow0\) with \(t\) in a compact neighborhood of \(T_0<1/2\). The factor \(e^{-\delta\cosh(4u)}\le1\) permits domination by a fixed polynomial times \(e^{-a_*u^2}\), with \(a_*>0\). The same applies to any fixed finite collection of \(t,x\) derivatives on compact sets. Thus these derivatives converge locally uniformly to those of (2).

Use the parameter implicit function theorem for
\[
\mathscr F_\delta(t,x)=
(H_\delta(t,x),\partial_xH_\delta(t,x)).
\]
The derivative with respect to \((t,x)\) at \((\delta,t,x)=(0,T_0,x_c)\) is
\[
D_{t,x}\mathscr F_0=
\begin{pmatrix}-d_0&0\\-h_3(T_0,x_c)&d_0\end{pmatrix},
\qquad \det D_{t,x}\mathscr F_0=-d_0^2<0.
\tag{10}
\]
The continuous-parameter version, with continuous first derivatives in \((t,x)\), therefore gives collision points
\[
(T_\delta,x_\delta)\longrightarrow(T_0,x_c),\qquad
H_\delta(T_\delta,x_\delta)=h_1(T_\delta,x_\delta)=0,
\]
\[
d_\delta:=h_2(T_\delta,x_\delta)>0
\tag{11}
\]
for every sufficiently small positive \(\delta\). By shrinking that range, \(0<T_\delta<1/2\) and \(x_\delta>0\). This is an existence statement for sufficiently small damping, not a numerically certified choice of damping size.

Only a one-sided parameter is required. One can alternatively use an ordinary \(C^1\) implicit function theorem: the one-sided \(\delta\) derivative exists and is continuous by Gaussian domination, now with an additional factor \(\cosh(4u)\). Extend \(\mathscr F\) to negative parameters by \(2\mathscr F_0-\mathscr F_{-\delta}\). This is a \(C^1\) extension at zero; it does not assert convergence of the original integral with negative damping.

## 4. Verification of the source-shape properties

Write
\[
Q(v)=1+bv+cv^2,\quad C(v)=\cosh(4\sqrt v),
\]
\[
\eta_{\delta,t}(v)=\log\{e^{tv}\phi_\delta(\sqrt v)\}
=-(1-t)v-\delta C(v)+\log Q(v).
\tag{12}
\]
The expression \(C\) is smooth at zero, as follows from its entire power series
\[
C(v)=\sum_{k=0}^\infty\frac{16^kv^k}{(2k)!}.
\]
Consequently \(C'(v)\ge8\) and \(C''(v)>0\) for \(v\ge0\). Also,
\[
(\log Q)''(v)
=\frac{2c-b^2-2bcv-2c^2v^2}{Q(v)^2}
=-\frac{2bcv+2c^2v^2}{Q(v)^2}.
\tag{13}
\]
For every \(\delta>0\), every real \(t\), and every \(v\ge0\), equations (12)–(13) prove
\[
\boxed{\eta_{\delta,t}''(v)<0.}
\tag{14}
\]
Since \((\log Q)'\) is nonincreasing and equals \(b\) at zero,
\[
\eta_{\delta,t}'(v)\le-(1-t)+b-8\delta.
\]
Choose any \(\tau\) with \(1/2<\tau<4/5\). For \(t\le\tau\),
\[
\begin{aligned}
\partial_u^2\log(e^{tu^2}\phi_\delta(u))
&=2\eta_{\delta,t}'(u^2)+4u^2\eta_{\delta,t}''(u^2)\\
&\le-2(1-\tau-b)<0.
\end{aligned}
\tag{15}
\]
This gives a uniform strong-concavity constant on an interval containing the collision and its predecessors. The first derivative is \(2u\eta'\), so the source decreases strictly for \(u>0\). Positivity and evenness follow immediately from (8).

For each fixed \(\delta>0\), differentiation in \(u\) introduces polynomial factors and finite products of \(\sinh(4u)\), \(\cosh(4u)\). On compact heat-time intervals, all such derivatives still have double-exponential decay. In particular, they satisfy the super-Gaussian derivative-decay condition used in the admissible-kernel literature. Monotonicity and strong log-concavity are asserted in the stated time range; integrability and (14) hold for all real times.

## 5. Full stationary predecessors and the adverse pole

Fix one sufficiently small \(\delta>0\). By (11), the equation \(h_1(t,x)=0\) defines a smooth full stationary curve \(x=x_\delta(t)\) through \((T_\delta,x_\delta)\). This is stationarity for the complete transform (9), with no retained-source substitution. Set \(f(t)=H_\delta(t,x_\delta(t))\). The heat equation gives exactly
\[
f'(t)=H_{\delta,t}+H_{\delta,x}x_\delta'(t)
=-h_2(t,x_\delta(t)).
\]
Therefore, for \(\varepsilon=T_\delta-t\downarrow0\),
\[
h_0=d_\delta\varepsilon+O(\varepsilon^2),\quad h_1=0,
\quad h_2=d_\delta+O(\varepsilon).
\]
It follows that
\[
E=d_\delta^2\varepsilon^2+O(\varepsilon^3),\qquad
\mathcal L_0=-d_\delta^2\varepsilon+O(\varepsilon^2),
\]
which proves (1). The division is used only to display the failure on predecessors where \(E>0\); the collision itself is handled by the expansions. No unknown physical quotient defines any proposed coefficient.

## 6. Consequences for the correlation and form approaches

[Csordas, Theorem 3.5](https://arxiv.org/pdf/1309.0055) shows that a strictly log-concave admissible source has admissible associated kernels. His Theorem 4.2(b) records square-variable log-concavity for the actual theta source; Remark 2.1 explains the resulting normalized-moment Turán inequalities. These statements do not assert Fourier positivity. Example 3.12 already illustrates the distinction for a different Gaussian-polynomial source.

For (8), all those source hypotheses hold near the collision. Nevertheless, the complete correlation identity from Note 36 gives
\[
\int_{\mathbb R}K_1(t,s)\cos(2xs)\,ds=\mathcal L_0(t,x)<0
\]
on the stationary predecessors just constructed. Thus a positive, decreasing admissible \(K_1\) need not be positive definite. The exact closed self-dual lift of Note 50 likewise applies to every entire jet of (9), without changing this sign.

It is useful to distinguish the two roles of the small parameter. The value \(\delta=0\) supplies an exactly computable collision whose nondegeneracy is visible in (7) and (10). The counterexample to a source-shape implication uses a fixed, strictly positive \(\delta\), chosen from the existence interval proved by the implicit function theorem. Once that choice is made, the full infinite source is retained everywhere. The limit \(\delta\downarrow0\) is not an approximation used in the signed stationary estimate, and the adverse limit in (1) varies time at fixed source. Thus there is no unpaid tail, changing cutoff, or drifting source in the final collision argument.

Likewise, moment control and stationary control test different quantities. Positive source moments integrate a fixed-sign weight against \(e^{tu^2}\phi_\delta\); their associated inequalities do not see the phase cancellations at a physical stationary point. The physical first-jet energy tends quadratically to zero along the predecessor curve, while its adverse signed loss tends only linearly. A fixed absolute moment bound therefore cannot be converted into a bounded multiple of that energy. Smoothness of every source derivative, convergence of every source moment, and the complete correlation representation all coexist with this mismatch.

For the form construction the distinction is equally explicit. Entirety of the spectral jets makes the forms of Note 50 closed and self-dual throughout this example. The polarized pairing still has its indefinite coefficient matrix and still produces the scalar \(\mathcal L_0\). Closedness, a positive form norm, or a positive reproducing formula for each separate input does not change its negative stationary value. Consequently, any proposed argument using the old quaternion-form kernels should identify the extra source hypothesis at the exact step where it would exclude this control.

The obstruction concerns only deductions from these common analytic shapes. It neither reproduces the theta arithmetic nor closes the source-prescribed signed-current target. A useful continuation must identify additional complete-theta information and show that it controls the signed physical observation at energy scale. The manuscript's proved domains and open pointwise status remain unchanged.
