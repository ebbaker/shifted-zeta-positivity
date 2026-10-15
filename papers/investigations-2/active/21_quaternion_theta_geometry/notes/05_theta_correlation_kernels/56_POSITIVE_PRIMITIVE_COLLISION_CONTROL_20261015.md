---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG, PR02]
status: proved_positive_primitive_collision_control_theta_signed_target_open
---

# Positive primitive reconstruction can coexist with a positive time collision

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the coordinating session's metadata. This is an analytic applicability control, with an exact-arithmetic algebra check, not a numerical sign pilot or a claim of literature novelty.

The positive primitive in [Note 52](52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md) is more general than the theta source. A smooth source can have a strictly positive heat-first primitive throughout the entire physical interval, the same exact reconstruction with boundary constant \(1/2\), an even completed primitive, and **every algebraic spectral asymptotic coefficient of the theta primitive**, while its physical transform has a collision at a time strictly between zero and \(1/2\). This strengthens the source-shape control of [Note 53](53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md). The complete signed theta estimate remains open.

## 1. A universal primitive with prescribed endpoint normalization

Let \(\phi\) be positive, even, smooth, and decay with its derivatives faster than every Gaussian. Assume its weighted moments below exist, as they do for the source constructed in Section 3. Normalize
\[
\int_0^\infty \cosh(v)\phi(v)\,dv=\frac1{16}.
\tag{1}
\]
Define, for \(u\ge0\),
\[
\psi(u)=8\int_u^\infty\sinh(v-u)\phi(v)\,dv.
\tag{2}
\]
Differentiation and the upper-end decay give
\[
\psi>0,\qquad
\psi'=-8\int_u^\infty\cosh(v-u)\phi(v)\,dv<0,
\]
\[
\boxed{\psi''-\psi=8\phi,\qquad \psi'(0)=-\tfrac12.}
\tag{3}
\]
In particular \(\psi''>0\). This is the unique super-Gaussian decaying solution of the inhomogeneous equation on the half-line: the difference of two such solutions is a linear combination of \(e^u\) and \(e^{-u}\), neither of which has that decay unless its coefficient vanishes.

If \(\phi\) is even and entire, the solution of (3) extends to an entire function. Its odd endpoint derivatives satisfy
\[
\psi^{(2k+1)}(0)=-\tfrac12\quad(k\ge0),
\tag{4}
\]
because the odd derivatives of \(\phi\) vanish at zero and differentiation of (3) gives the recurrence. Equivalently,
\[
\psi(-u)-\psi(u)=\sinh u,
\qquad P(u):=e^u+2\psi(u)\ \text{is even}.
\tag{5}
\]
These facts do not impose the arithmetic theta expansion on \(P\).

For
\[
H(t,x)=\int_0^\infty e^{tu^2}\phi(u)\cos(xu)\,du,
\qquad
J(t,x)=\int_0^\infty e^{tu^2}\psi(u)\cos(xu)\,du,
\tag{6}
\]
two integrations by parts using (3) give exactly
\[
\boxed{8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.}
\tag{7}
\]
Thus the reconstruction of Note 52 is a general endpoint-normalized Green identity. In the theta case its source \(\psi\) agrees with (2) by the differential equation and uniqueness. The theta-specific input lies in the actual source, not in the formal identity (7).

## 2. A sufficient condition for heat-first primitive positivity

Suppose in addition that, for \(v\ge0\),
\[
\phi'(v)\le-4v\phi(v).
\tag{8}
\]
Write \(K(u)=\int_u^\infty\cosh(v-u)\phi(v)\,dv\), so \(\psi'=-8K\). Integrating the right side of (8) against \(\cosh(v-u)\) yields
\[
\begin{aligned}
uK(u)
&\le\int_u^\infty v\cosh(v-u)\phi(v)\,dv\\
&\le\tfrac14\int_u^\infty\cosh(v-u)(-\phi'(v))\,dv\\
&=\frac{\phi(u)}4+\frac{\psi(u)}{32}.
\end{aligned}
\tag{9}
\]
No boundary term is omitted: the lower endpoint gives \(\phi(u)/4\) and the upper endpoint is zero. With \(f_t=e^{tu^2}\psi\), equations (3) and (9) imply, for \(t\ge0\),
\[
\begin{aligned}
e^{-tu^2}f_t''
&=8\phi+(1+2t+4t^2u^2)\psi+4tu\psi'\\
&\ge8(1-t)\phi+(1+t+4t^2u^2)\psi.
\end{aligned}
\tag{10}
\]
The right side is strictly positive for \(0\le t\le1\), hence throughout \([0,1/2]\).

For the constructed source, \(f_t\) and its derivatives vanish at infinity and \(f_t'(0)=-1/2\). Therefore
\[
\boxed{J(t,x)=\frac1{x^2}\int_0^\infty f_t''(u)(1-\cos(xu))\,du>0}
\tag{11}
\]
for \(x\ne0\) and \(0\le t\le1/2\). At zero the defining integral is positive. This is the same strict convexity mechanism used for the original theta primitive, with the heat multiplier applied to a fixed primitive before transformation.

## 3. An explicit source family retaining a collision

For \(\delta>0\), let
\[
g_\delta(u)=e^{-3u^2-\delta\cosh(4u)}
                 (1+u^2+\tfrac12u^4),
\]
\[
C_\delta=\left(16\int_0^\infty\cosh(v)g_\delta(v)\,dv\right)^{-1},
\qquad \phi_\delta=C_\delta g_\delta.
\tag{12}
\]
All constants are finite and strictly positive. This normalization changes no zero or stationary location. The source is positive, even, entire in \(u\), and has double-exponential decay on the real line, with all derivatives. It permits every finite real heat time and every complex spectral argument.

Set \(Q(v)=1+v+v^2/2\). Since
\[
(\log Q)'(v)=\frac{1+v}{Q(v)}\le1\quad(v\ge0),
\]
we have
\[
\frac{\phi_\delta'(u)}{\phi_\delta(u)}
=-6u-4\delta\sinh(4u)
 +2u(\log Q)'(u^2)\le-4u.
\tag{13}
\]
Consequently (8) holds, and the associated \(J_\delta\) is strictly positive for all real \(x\) and all \(0\le t\le1/2\).

For completeness, all integrations and endpoint expansions used above have the required decay. For \(u\ge1\), (13) gives
\(\phi_\delta(u+s)\le\phi_\delta(u)e^{-4us}\). Hence
\[
0<\psi_\delta(u)\le\frac{8\phi_\delta(u)}{16u^2-1},
\qquad
0<-\psi_\delta'(u)\le\frac{32u\phi_\delta(u)}{16u^2-1}.
\tag{14}
\]
The differential equation then controls all higher derivatives by \(\psi_\delta\), \(\psi_\delta'\), and finitely many source derivatives. The resulting decay survives each fixed heat multiplier, locally uniformly in heat time. Thus \(H_\delta\) and \(J_\delta\) are entire in the spectral variable and their stated differentiations are legitimate.

The source also retains the shape properties of Note 53. For
\[
\eta_{\delta,t}(v)=\log(e^{tv}\phi_\delta(\sqrt v)),
\]
\[
\eta_{\delta,t}''(v)
=-\delta\,\frac{d^2}{dv^2}\cosh(4\sqrt v)
-\frac{v+v^2/2}{Q(v)^2}<0\quad(v\ge0).
\tag{15}
\]
The first term is strictly negative also at zero, as its power series shows. Moreover \(\eta'_{\delta,t}\le-3+t+1=-2+t\). For \(0\le t\le1/2\),
\[
\partial_u^2\log(e^{tu^2}\phi_\delta(u))
=2\eta'_{\delta,t}(u^2)+4u^2\eta''_{\delta,t}(u^2)\le-3.
\tag{16}
\]
Thus the deformed source is strictly decreasing on \(u>0\) and uniformly strongly log-concave throughout the physical interval.

At \(\delta=0\), ignore the positive normalization temporarily and put \(a=3-t\). Direct Gaussian differentiation gives
\[
\widetilde H_0(t,x)
=\frac{\sqrt\pi}{2\sqrt a}e^{-x^2/(4a)}
 \frac{P_a(x^2)}{16a^4},
\tag{17}
\]
\[
P_a(y)=\tfrac12y^2-(4a^2+6a)y
       +16a^4+8a^3+6a^2.
\tag{18}
\]
Its discriminant is
\[
\Delta(a)=16a^2(-a^2+2a+\tfrac32).
\tag{19}
\]
The positive discriminant root and collision time are
\[
a_c=1+\sqrt{5/2}=\frac{2+\sqrt{10}}2,
\qquad T_0=3-a_c=\frac{4-\sqrt{10}}2\in(0,1/2).
\tag{20}
\]
At this point,
\[
y_c=4a_c^2+6a_c=20+7\sqrt{10}>0,
\qquad P_{a_c}(y)=\tfrac12(y-y_c)^2.
\tag{21}
\]
With \(x_c=\sqrt{y_c}\), this gives
\[
\widetilde H_0(T_0,x_c)
=\partial_x\widetilde H_0(T_0,x_c)=0,
\]
\[
d_0:=\partial_x^2\widetilde H_0(T_0,x_c)
=\frac{\sqrt\pi}{2\sqrt{a_c}}e^{-y_c/(4a_c)}
  \frac{y_c}{4a_c^4}>0.
\tag{22}
\]
The heat equation holds, and the derivative of
\((\widetilde H_0,\partial_x\widetilde H_0)\) with respect to \((t,x)\) at the collision is
\[
\begin{pmatrix}-d_0&0\\-\partial_x^3\widetilde H_0&d_0\end{pmatrix},
\qquad\det=-d_0^2<0.
\tag{23}
\]
On compact neighborhoods of \((T_0,x_c)\), the transforms of \(g_\delta\), and every fixed collection of their \(t,x\) derivatives, converge uniformly to (17) as \(\delta\downarrow0\). Gaussian domination applies since \(t\) stays below \(3\), and \(e^{-\delta\cosh(4u)}\le1\). The continuous-parameter implicit function theorem therefore gives, for every sufficiently small fixed \(\delta>0\), a nondegenerate collision
\[
(T_\delta,x_\delta)\longrightarrow(T_0,x_c),
\quad 0<T_\delta<1/2,\quad x_\delta>0,
\]
\[
H_\delta=h_{\delta,1}=0,
\qquad d_\delta:=h_{\delta,2}>0
\quad\text{at }(T_\delta,x_\delta).
\tag{24}
\]
The positive normalization in (12) preserves these statements. As in Note 53, this is a rigorous existence interval for sufficiently small damping; no numerical damping cutoff is asserted. An ordinary \(C^1\) parameter version is also available by including one factor \(\cosh(4u)\) in the Gaussian dominator and extending the parameter map differentiably through zero. No negative-damping integral is used.

## 4. The complete algebraic asymptotic series is universal

Equation (4) implies that the odd part of the endpoint germ of \(\psi_\delta\) is \(-\tfrac12\sinh u\). Hence for every \(k\ge0\),
\[
\left.\partial_u^{2k+1}(e^{tu^2}\psi_\delta(u))\right|_{u=0}
=-\frac{(2k+1)!}{2}
 \sum_{j=0}^k\frac{t^j}{j!(2k+1-2j)!}.
\tag{25}
\]
These are exactly the odd endpoint derivatives of the theta primitive. Repeated integration by parts gives, for every fixed \(N\ge1\), uniformly in \(0\le t\le1/2\),
\[
J_\delta(t,x)
=\frac12\sum_{k=0}^{N-1}
 \frac{(-1)^k(2k+1)!}{x^{2k+2}}
 \sum_{j=0}^k\frac{t^j}{j!(2k+1-2j)!}
 +O_{N,\delta}(x^{-2N-2}).
\tag{26}
\]
In particular the leading terms are \(1/(2x^2)-(1+6t)/(2x^4)\), as in Note 52. More strongly, the control and theta primitives differ by a quantity smaller than every fixed inverse power of \(|x|\), uniformly on the compact heat interval. The constants need not be uniform as \(\delta\downarrow0\).

This is an all-orders asymptotic statement, not a claim that the displayed formal series converges or determines the exponentially small physical cancellation. The source-dependent information remains in that cancellation.

## 5. Failure of a bounded stationary energy payment

Fix one of the sufficiently small positive damping parameters from (24). The equation \(h_{\delta,1}=0\) defines the full stationary curve \(x=x_\delta(t)\) through the collision. On this curve,
\[
\frac d{dt}H_\delta(t,x_\delta(t))=-h_{\delta,2}(t,x_\delta(t)).
\]
For \(\varepsilon=T_\delta-t\downarrow0\),
\[
h_{\delta,0}=d_\delta\varepsilon+O(\varepsilon^2),
\quad h_{\delta,1}=0,
\quad h_{\delta,2}=d_\delta+O(\varepsilon).
\]
Consequently, with \(E=h_{\delta,0}^2+h_{\delta,1}^2\) and
\(\mathcal L_0=h_{\delta,1}^2-h_{\delta,0}h_{\delta,2}\),
\[
\boxed{\frac{\mathcal L_0}{E}
=-\frac1{T_\delta-t}+O(1).}
\tag{27}
\]
No coefficient locally bounded through this event can give \(\mathcal L_0\ge-\kappa E\) on its full predecessors.

Nevertheless, for this same fixed source and heat interval:

- the physical source is positive, even, entire, decreasing, strongly log-concave, strictly log-concave in the squared coordinate, and double-exponentially decaying;
- the original heat-first primitive \(J_\delta\) is strictly positive for every real spectral argument;
- the full exact differential reconstruction (7), with the same boundary constant \(1/2\), holds;
- \(P_\delta=e^u+2\psi_\delta\) is even, and the primitive has every theta endpoint odd derivative and every theta algebraic spectral asymptotic coefficient.

These properties together therefore do not supply the signed energy-relative estimate. Failure on the \(j=0\) branch already precludes deducing the required pair of branch bounds from them alone. No claim is made that \(\phi_\delta\) is a theta series, has its arithmetic coefficients, or satisfies additional theta differential identities.

The discriminating next task is consequently sharper than “retain the full primitive operator.” Any successful signed reconstruction proof must use additional complete-theta information at the step that excludes this explicit primitive-compatible control. This note does not prove the theta estimate, enlarge a theta sign domain, evaluate an arithmetic endpoint, or change the manuscript's pointwise status.

## 6. Rational finite-jet nonclosure does not distinguish the control

For each fixed \(\delta>0\), write \(w_t=e^{tu^2}\phi_\delta\). Direct differentiation gives, for every fixed nonnegative integer \(k\),
\[
\frac{w_t^{(k)}(u)}{w_t(u)}
=(-2\delta)^k e^{4ku}\{1+o(1)\}\quad(u\to+\infty).
\tag{28}
\]
The leading contribution differentiates \(e^{-(\delta/2)e^{4u}}\) at each step. The Gaussian, polynomial, and \(e^{-(\delta/2)e^{-4u}}\) factors contribute lower orders. If a nonzero polynomial-coefficient differential operator annihilated \(w_t\), dividing by its highest-derivative coefficient, \(w_t\), and the largest exponential factor would leave a nonzero constant from that derivative while every lower-order term tends to zero. Thus no such operator exists.

Fourier conjugation, followed by clearing rational denominators and entire continuation, gives precisely the finite rational-coefficient jet nonclosure statement of Note 52 for the control transform as well. Consequently that structural exclusion, even combined with all the primitive properties above, still does not imply the signed stationary bound. This is a direct use of the existing nonclosure proof, not a new closure theorem.

## Verification record

The [companion standard-library checker](../../numerics/check_positive_primitive_collision_control.py), with its [exact-arithmetic receipt](../../numerics/POSITIVE_PRIMITIVE_COLLISION_CONTROL_CHECKS_20261015.json), verifies the Gaussian discriminant, factorization and double-zero coefficient symbolically in \(\mathbb Q(\sqrt{10})\), the formal reconstruction coefficients, the first several universal endpoint polynomials, and the rational constants in the convexity bound. It performs no sampled theta sign test. The analytic facts about decay, the implicit function theorem, strict positivity, and the stationary pole are established by the arguments above; an algebra receipt does not replace them.
