# Green geometry and the Riemann–Siegel argument at the Newman threshold

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The actual backend model and
reasoning effort are not exposed in this chat's recorded configuration.

**Status: explanatory clarification and a standard compactness consequence
of a named published theorem; same-assistant analytical check.** No new
arithmetic inequality or exclusion of a positive Newman threshold is proved.

The author clarifies the intended direction: assume \(\Lambda>0\), work
at the all-real threshold slice, and use the complete symmetric
Riemann–Siegel representation there. This is different from B01's chosen
Green consumer at \(\lambda=c/\log(X/(4\pi))\), \(1/2\le c\le1\).
E01–E07 retain their existing scope and status. Their averaged conclusions
and scoped obstructions do not settle the threshold-collision argument.

This clarification follows the [result summaries](../../../../../result-summaries/README.md),
especially [Newman reductions](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md), specifically
[target reformulations](../../../../../avoid/01_restating_the_target.md),
[shared-premise controls](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. What the Green variables mean

Keep the complete field and clock of manuscript §2:
\[
 H_0(z)=\tfrac18\xi(\tfrac12-\tfrac{i z}{2}),\qquad
 \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]
The real \(z\)-axis corresponds to the zeta critical line at time zero.
For \(z=x+iy\), the corresponding zeta coordinate is
\(s=(1+y)/2-ix/2\). In particular, positive \(x\) corresponds to
absolute zeta height \(x/2\). At nonzero time, the zeros belong to the
deformed field, not directly to the original zeta function.

In manuscript §5, \(X\) is any chosen real observation coordinate, not a
time and not necessarily a zero. The auxiliary strip is \(0<\Im z<8\);
the observation point is its midpoint \(X+4i\). Its boundary consists of
the lines \(y=0\) and \(y=8\). With
\[
 K(u)=\frac{1}{16\cosh(\pi u/8)},
\]
each boundary has harmonic-measure density \(K(x-X)\), of mass \(1/2\).
Writing out the definition below manuscript (5.1) gives
\[
 J_\lambda(X)=
 \int_{\mathbb R}K(x-X)
 \bigl(\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|\bigr)\,dx
 -\log|H_\lambda(X+4i)|.                         \tag{1}
\]
Thus \(J\) is the harmonic boundary prediction of the logarithm minus
its actual interior value. For a zero-free analytic field with the stated
growth, the logarithm is harmonic and this difference vanishes. Interior
zeros give positive defects through the Poisson–Jensen identity.

For an upper zero \(z_j=x_j+iy_j\), its individual contribution is
\[
 G(X-x_j,y_j),\qquad
 G(u,y)=\operatorname{atanh}\frac{\sin(\pi y/8)}{\cosh(\pi u/8)}.
                                                               \tag{2}
\]
The first argument called \(t\) in manuscript (5.1) is a spatial
displacement, not heat time. The complete identity proved in §5 is
\[
 J_\lambda(X)=\sum_{y_j>0}G(X-x_j,y_j),\qquad 0\le\lambda\le1/2,
                                                               \tag{3}
\]
with multiplicities. \(G\) is the contribution of one zero; \(J\) is the
total. The canonical zeros have \(|y_j|\le1\), so the observation point
at height four is safely above them. The strip heights eight and four
are auxiliary choices, not zeta ordinates or Newman times. Real boundary
zeros, including multiple real zeros, contribute zero. Their logarithmic
singularities are integrable in (1).

## 2. A positive threshold entails a finite multiple real zero

Assume \(\Lambda>0\). By the defining threshold property, all zeros of
\(H_\Lambda\) are real, whereas every \(0<\lambda<\Lambda\) has a
nonreal zero. The passage from that statement to an attained finite event
needs uniform control at infinity; continuity alone would not suffice.

Use [Polymath, arXiv:1904.12438v2, Theorem 1.5(i)](https://arxiv.org/html/1904.12438v2#S1):
there is an absolute \(C\) such that, for \(0<\lambda\le1/2\), every
zero with \(\Re z\ge\exp(C/\lambda)\) is real. Evenness supplies the
same conclusion at negative real part. Choose \(\lambda_n\uparrow\Lambda\)
with \(\lambda_n\ge\Lambda/2\), and a nonreal zero \(z_n\) at each time.
By conjugation and evenness choose \(\Re z_n\ge0\), \(\Im z_n>0\).
The cited theorem and the canonical strip bound give
\[
 0\le\Re z_n<e^{2C/\Lambda},\qquad 0<\Im z_n\le1.
\]
A subsequence converges. Local uniform continuity of the complete field
gives \(H_\Lambda(z_*)=0\), hence \(z_*=x_*\) is real. Positivity of
\(H_\Lambda(0)\) implies \(x_*>0\).

If this zero were simple, the implicit-function theorem would give a
unique nearby zero for every sufficiently close real time. Schwarz
reflection would force that unique zero to be real. This contradicts the
nearby nonreal \(z_n\). Therefore
\[
                    H_\Lambda(x_*)=H_\Lambda'(x_*)=0.           \tag{4}
\]
This proves the stated conditional finite-attainment consequence of the
published uniform theorem. It does not assert that the multiplicity is
exactly two or that \(\Lambda>0\) actually occurs. The threshold statement
is imported in the same normalization as the manuscript. This argument
does not extend to \(\Lambda=0\): its compact bound deteriorates there.

At this entire all-real slice,
\[
                         J_\Lambda(X)=0\quad\text{for every }X. \tag{5}
\]
Equation (5) is compatible with (4), so the value of \(J\) at the
threshold cannot by itself exclude a multiple real zero. For an ordinary
double event, the local backward-heat expansion is
\[
 H_{\Lambda+s}(x_*+y)=\tfrac a2(y^2-2s)
        +\text{terms of higher parabolic weight},\qquad a\ne0.
\]
Just below the event the upper zero has height
\(\sqrt{2(\Lambda-\lambda)}+O(\Lambda-\lambda)\). Its Green contribution
tends to zero on that square-root scale, by (2). This is the local
behavior already described in manuscript §§4–5, with the clock sign
converted from \(\tau=-\lambda\).

## 3. The symmetric Riemann–Siegel representation at that slice

Manuscript §10 gives the exact Gaussian evolution and the complete
Riemann–Siegel split. An explicit real-axis version follows directly from
[Polymath §4, (39)](https://arxiv.org/html/1904.12438v2#S4).
For real \(x\ne0\), \(\lambda>0\), and any fixed nonnegative integer \(N\),
define, in that paper's notation,
\[
 A_{\lambda,N}(x)=
 \sum_{n=1}^{N}r_{\lambda,n}\bigl((1+ix)/2\bigr)
       +R_{\lambda,N}\bigl((1+ix)/2\bigr).
\]
The remainder is part of this definition. The reflected identity is
\[
 H_\lambda(x)=A_{\lambda,N}(x)+\overline{A_{\lambda,N}(x)}
             =2\Re A_{\lambda,N}(x).                            \tag{6}
\]
Fix \(N\) on a neighborhood when differentiating. The complete terms
are analytic there, and (4) becomes
\[
 \Re A_{\Lambda,N}(x_*)=0,\qquad
 \Re A_{\Lambda,N}'(x_*)=0.                                    \tag{7}
\]
These are exact simultaneous cancellation conditions, not conditions on
only the leading saddle. They hold for higher multiplicities as well.

Where the complete arm is nonzero, write \(A=\rho e^{i\psi}\). Then
\(H=2\rho\cos\psi\), and at a real zero
\[
 H'=-2\rho\psi'\sin\psi.
\]
Thus a multiple zero with \(A\ne0\) forces \(\psi'=0\). A useful proof
would have to control the complete arm's nonvanishing and phase derivative,
or exclude (7) directly. No such quantitative estimate is supplied here.
If a truncated arm is used instead, both the value and derivative of its
remainder must be paid. The amplitude-zero case cannot be discarded.

Conjugate symmetry is available on the real axis for every real time;
it does not require all zeros of the field to be real. The threshold
assumption adds the all-real zero configuration and the event (4).
At positive time one uses the evolved completed formula, not the
unchanged classical cosine sum for \(H_0\).

## 4. Difference from the completed transition-scale branch

Sections 11–13 used the heat-evolved arithmetic arms to estimate the
boundary logarithm in (1), on \(\lambda=c/L_X\), \(1/2\le c\le1\).
They did not impose (4) or work at an unknown threshold time. At a
putative threshold event with \(x_*>4\pi\), the corresponding product is
\(c_*=\Lambda\log(x_*/(4\pi))\); nothing here puts it in that chosen
band, let alone sets it equal to one. The original finite-height coverage
obligation also remains.

The next conceptual question matching the author's intent is whether
the **complete** symmetric formula has an arithmetic estimate incompatible
with (7), throughout the possible positive-threshold event domain. Merely
expressing this incompatibility as a criterion is a target reformulation
under avoid01. The earlier quadratic, fixed-reference and tangent
obstructions retain their original classes; none excludes this entire
critical-time approach. No new frozen execution task or model change is
issued by this explanatory note.

## 5. Control and source checks

Symmetry, an all-real slice and the backward heat equation alone permit
collisions. For example, at any chosen \(\lambda_*\), with \(s=\lambda-\lambda_*\),
\[
 F_\lambda(x)=(x^2-r^2)^2-s(12x^2-4r^2)+12s^2,\qquad r>0,
\]
satisfies \(\partial_\lambda F=-F_{xx}\). At \(s=0\) it has double
zeros at \(\pm r\); just above this time its four zeros are real, and
just below it they are nonreal. Its equation for \(x^2\) has discriminant
\(32r^2s+96s^2\). This local polynomial check does not have the canonical
theta source and makes no claim about the full theta threshold.

The repository controls impose the same scope discipline:

- Euler-factor and translated controls change the full canonical arithmetic
  coefficients. Their surviving reflection and heat evolution cannot
  themselves distinguish the desired argument.
- Weighted-square, finite-tail and finite-prime-orbit controls fail full
  canonical reflection and/or the unchanged coefficient sequence. Many
  have no finite all-real threshold, so their local events cannot silently
  be relabeled global thresholds.
- Reflected super-Gaussian, smooth-shape and positive-primitive controls
  lack the canonical theta square-series arithmetic.
- Atomic, finite-profile and their continuous extensions fail the full
  theta profile and its eventual simple-zero behavior at positive time.
- RH-conditional endpoint controls retain their conditional premise;
  they are not unconditional theta counterexamples.
- Fixed-amplitude variable-readout controls fail the literal cosine
  readout and its physical heat equation. Relaxed Green profiles omit the
  complete canonical boundary field and exact zero multiset.

No proposed arithmetic sign bound has been screened successfully here:
none has yet been derived. These premise checks prevent a symmetry-only
claim and do not exclude estimates using the complete theta arithmetic.

Primary inspection on 11 November 2026: Polymath,
*Effective approximation of heat flow evolution of the Riemann ξ function,
and a new upper bound for the de Bruijn–Newman constant*,
arXiv:1904.12438v2 (4 August 2019), Theorem 1.5(i), §4 (35)–(39), and the
local splitting statement in Proposition 3.1. These are selected checked
passages, not a new full-paper audit. The canonical bibliography remains
in the [HDA catalog](../../../01_heat_density_asymptotics/references/references.bib).

Same-assistant check: the Green boundary masses, coordinate conversion,
compactness/implicit-function argument, clock sign, differentiated full
arm and polynomial heat equation were checked algebraically. No numerical
evidence, specialist review or new quantitative zero exclusion is claimed.

Chat-capture status: the recorder refused this turn's refresh because the
source creation timestamp disagrees with the registered capture. The prior
verified archive is preserved; its JSON was not hand-edited and no guard
was bypassed. This research note is not a substitute transcript capture.
