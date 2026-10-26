# Generalized transforms and the hierarchy of heat components

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0004, thread 01a1765a-5c4e-7dd1-9de8-d70dd1725e34.

**Status: explanatory synthesis and exact elementary identities.** This
organizes the existing results; it establishes no new asymptotic domain,
ADHM correspondence, inverse-scattering construction, or closure theorem.
No numerical, symbolic, interval, or sampling campaign was run.

The author's examples are ADHM/twistor transforms, quantum-chemical
approximation hierarchies, BBGKY, and inverse scattering for sine-Gordon
and KdV. Their shared lesson is to distinguish (a) a structured
representation, (b) evolution in that representation, and (c) the error
of finite reconstruction. A component need not be an ordinary frequency.

## 1. What the analogies contribute

ADHM encodes self-dual fields by constrained auxiliary data with a
reconstruction procedure. Ward explicitly relates ADHM to Fourier,
Radon, Penrose and inverse-scattering transforms. This corroborates the
author's terminology, without identifying the particular Atiyah passage
he recalls. No twistor or ADHM data have been constructed for this
investigation.

Inverse scattering reorganizes certain nonlinear evolution problems in
spectral data with simpler evolution and nonlinear reconstruction. Its
discrete and continuous sectors need not be ranked by smallness.
An integrable hierarchy of commuting flows is also distinct from a
hierarchy of approximation accuracy. The AKNS 1974 paper explicitly
frames inverse scattering as Fourier analysis for nonlinear problems.

Quantum chemistry separates such choices as orbital-basis resolution
and treatment of correlation. Excitation/correlation order is not a
frequency label. BBGKY organizes reduced distributions or density
matrices: evolution at one level depends on higher-order information,
so finite closure has its own error and compatibility requirements.
Neither ordering alone guarantees monotone or uniform improvement.
See the [source catalog](../references/README.md) for inspected scope.

## 2. Exact heat evolution, energies, and a literal moment hierarchy

Write h(T,z)=H(-T,z), so h_T=h_zz. With the canonical even spectral
density rho(u)=Phi(|u|)/2, the exact source formula is

\[
h(T,z)=\int_{\mathbb R}e^{-Tu^2+izu}\rho(u)\,du.
\tag{GT1}
\]

For T>=0 on compact complex z sets, canonical source decay permits
differentiation. Thus

\[
\mu_j(T,z)=\int_{\mathbb R}u^j e^{-Tu^2+izu}\rho(u)\,du,\qquad
\partial_T\mu_j=-\mu_{j+2},\quad
\partial_z\mu_j=i\mu_{j+1},\quad h=\mu_0.
\tag{GT2}
\]

GT2 is a simple moment hierarchy with the BBGKY-like feature that lower
levels require higher levels. It is not a many-body BBGKY system. A
finite list of these moments does not determine its own time evolution
without more source information or a controlled closure.

On the real line, the heat operator is exp(-T A), with A=-d_x^2 and
generalized Fourier eigenvalue u^2. This is the elementary imaginary-time
energy-filtering analogy. The arithmetic label n below is not an energy
index: its local slope is complex, and its oscillatory frequency decreases
toward the Riemann--Siegel cutoff.

## 3. A concrete family already present in Note05

Let X be a fixed large real center, d=z-X, and

\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\qquad
\alpha=M'/M,\qquad w_\epsilon(z)=\frac{1+\epsilon iz}{2},
\]
\[
h_{\epsilon n}(z)=M(w_\epsilon(z))n^{-w_\epsilon(z)},\qquad
\beta_{\epsilon n}(z)=\frac{\epsilon i}{2}
 [\alpha(w_\epsilon(z))-\log n],\qquad
\lambda_{\epsilon n}=\beta_{\epsilon n}(X).
\tag{GT3}
\]

Define the heat components

\[
\Psi_{\lambda,m}(T,d)=
\partial_\lambda^m e^{\lambda d+T\lambda^2}.
\tag{GT4}
\]

They satisfy (partial_T-partial_d^2)Psi=0 exactly. For fixed lambda,

\[
\begin{aligned}
\Psi_{\lambda,0}&=e^{\lambda d+T\lambda^2},\\
\Psi_{\lambda,1}&=(d+2T\lambda)\Psi_{\lambda,0},\\
\Psi_{\lambda,2}&=((d+2T\lambda)^2+2T)\Psi_{\lambda,0}.
\end{aligned}
\tag{GT5}
\]

Their polynomial factors are Gaussian-moment polynomials, equivalent
under complex rescaling to Hermite polynomials (DLMF18.12.15).
They are local analytic components, not an asserted orthonormal global
Fourier basis. At fixed lambda the derivative action is triangular:

\[
\partial_d^2\Psi_{\lambda,m}
=\lambda^2\Psi_{\lambda,m}
 +2m\lambda\Psi_{\lambda,m-1}
 +m(m-1)\Psi_{\lambda,m-2},
\tag{GT6}
\]

with negative indices zero. Finite exponential-polynomial spaces are
therefore invariant under heat evolution. This is a precise sense in
which the components are adapted to the equation.

Factor each initial mode exactly near X:

\[
h_{\epsilon n}(X+q)
=h_{\epsilon n}(X)e^{\lambda_{\epsilon n}q}A_\epsilon(q),
\qquad
A_\epsilon(q)=
\frac{M(w_\epsilon(X)+\epsilon iq/2)}{M(w_\epsilon(X))}
e^{-\epsilon i\alpha(w_\epsilon(X))q/2}.
\tag{GT7}
\]

The crucial simplification is that A_epsilon is independent of n.
Put a_epsilon,m=A_epsilon^(m)(0)/m!. The existing finite representation is

\[
F_{X;J,K}(-T,z)=
\sum_{\epsilon=\pm1}\sum_{n=1}^{N}h_{\epsilon n}(X)
\sum_{m=0}^{J}a_{\epsilon,m}\Psi_{\lambda_{\epsilon n},m}(T,z-X)
+\mathcal I_{X,K}(T,z),
\tag{GT8}
\]
\[
\mathcal I_{X,K}(T,z)=
\frac1{\sqrt{4\pi T}}\int_{X-V}^{X+V}
e^{-(z-u)^2/(4T)}Q_{X,K}(u)\,du,\qquad
N=\left\lfloor\sqrt{X/(4\pi)}\right\rfloor.
\tag{GT9}
\]

Q retains the real RS coefficients C0,...,CK and exact adjacent-cutoff
transfer. This integral is part of the representation, not an unknown
remainder. With X,V,J,K fixed, both terms solve the heat equation
exactly. The reconstruction error still includes initial RS truncation,
local Taylor truncation, and localization/tail errors.

These are [Note05 FN20--26](05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
in reorganized notation. They are not a newly proposed ansatz.

## 4. How the AN03 curvature correction fits

At a target z suppress the arm and arithmetic labels. Let
beta=(log h)', gamma=beta', eta=beta'', zeta=beta'''.
The local Taylor organization is

\[
h(z+q)=h(z)e^{\beta q}
\left[1+\frac{\gamma q^2}{2}+\frac{\eta q^3}{6}
 +\left(\frac{\zeta}{24}+\frac{\gamma^2}{8}\right)q^4+\cdots\right].
\tag{GT10}
\]

The exact full-Gaussian identity

\[
\frac1{\sqrt{4\pi T}}\int_{\mathbb R}
e^{-q^2/(4T)}e^{\beta q}q^m\,dq
=\partial_\beta^m e^{T\beta^2}
\tag{GT11}
\]

explains the first correction:

\[
\frac{\gamma}{2}\partial_\beta^2e^{T\beta^2}
=e^{T\beta^2}\gamma(T+2T^2\beta^2).
\tag{GT12}
\]

Thus the existing evaluated component is

\[
h_{\epsilon n}(z)e^{T\beta_{\epsilon n}(z)^2}
[1+\gamma_\epsilon(z)(T+2T^2\beta_{\epsilon n}(z)^2)],
\quad \gamma_\epsilon=-\alpha'(w_\epsilon)/4.
\tag{GT13}
\]

The compact first-correction ansatz sums GT13 over both arms and all
n<=N and adds the K=1 bounded integral, with
V=8 sqrt(max(1,B)) log(X/(4pi)). Its proved compact family is
0<tau<=T<=B<infinity, after the declared onsets.

GT11 alone is not a canonical-field error proof: the local expansion
must still be localized and its remainder controlled. That work is
already in [Note10](10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md)
and [Note12](12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md).

The frozen-X form GT8 has zero residual. The compact formula GT13 uses
z-dependent beta and gamma; their spatial derivatives give a nonzero,
estimated residual. These are two related constructions with different
accuracy/cost statements, not identical formulas.

Polynomial degree also differs from asymptotic order:
gamma=O(X^-1), eta=O(X^-2), zeta=O(X^-3), so the next formal
X^-2 level includes both eta times the cubic moment and gamma^2 times
the quartic moment. Logarithmic factors, time factors and the full
arithmetic population must be included before assigning an error rate.
No new higher-order remainder estimate is asserted here.

## 5. What a useful hierarchy must measure

There are at least three distinct indices:

| Index | Information retained |
| --- | --- |
| n, epsilon | Arithmetic carriers and the two exact-gamma arms. |
| m<=J | Curvature/moment detail within each carrier. |
| k<=K | Canonical Riemann--Siegel completion and cutoff transfer. |

The current models retain every n<=N. Increasing m does not license
discarding arithmetic modes or the RS sector. In Note10 the first
arithmetic evolution correction has O(|G|X^-7/4) field allowance, whereas
the retained K=1 source comparison leaves O(|G|X^-5/4). Improving just
the curvature sector therefore does not improve that total bound.

For a fixed compact negative-time interval, the assessed first-correction
result has field and spatial j<=3 errors O(|G|X^-5/4), first-time error
of that order, and residual plus its spatial derivative O(|G|X^-7/4).
The relative allowance

\[
X^{-5/4}\exp(TL^2/16-\pi^2T/64),\qquad L=\log(X/(4\pi)),
\tag{GT14}
\]

grows at fixed T>0. It is an upper allowance that fails to prove outer
smallness, not proof that the actual error grows.

The separate growing-order result already chooses J=ceil(3L),
K=ceil(L). Notes05--06 prove the stricter E_o exp(-L^2/4) field,
spatial j<=3 and first-time comparison on 4/L<=T<=2 with their paid
buffers/onsets. Its bounded correction integral and growing component
counts remain. This domain is not automatically extended to every B
by Note12's compact fixed-order theorem.

A useful next use of this perspective is an error table indexed by
(regime, J, K), with each source of error measured in the intended
field/jet norm. A transform earns an analytical improvement when its
reconstruction estimate retains useful cancellations or lowers a proved
error or cost. Relabeling terms alone does not do that.

## 6. Scope controls and next owner

This is an explanatory representation, not an RH-equivalent criterion
or a new quantitative milestone. See the [result index][results],
[heat-flow cluster][r11], [collision controls][r12], [avoid index][avoid],
[reformulations][a01], [shared-shape controls][a02], and
[scoped conclusions][a07].

The heat/moment identities and finite invariant families apply to
noncanonical sources as well. The Euler-factor, weighted-square,
reflected super-Gaussian and smooth-shape collision controls therefore
are not excluded by these identities. They fail the premise of the
unchanged canonical gamma-zeta initial field/full theta source. Exact
canonical reconstruction remains essential; there is no new zero-sign,
collision-exclusion or physical-transfer conclusion.

Next owner remains **Analysis — Sol**, existing
[HDA-A08-AN01 r1](../research-progress/handoffs/HDA-A08-AN01.md):
one buffered positive-time comparison on [1/2,1]. The present hierarchy
is organizational guidance, not an execution or revision of that packet.
Positive original time has Fourier multiplier exp(+t u^2), so a
negative-time damping argument cannot substitute for its source/contour
estimates. A02 remains Partial; all parent statuses are unchanged.

[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
