# Source transport and zeros outside every horizontal strip

31 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, effort **xhigh**, Investigation05 chat0053.

**Status: proved in-note; same-assistant analytical self-check, no independent or specialist review.** For the precise raw exterior theta source, the pure divergence flow with \(v(X)=X+X/(1+|X|^2)\), and the fixed logarithmic cosine observation, every nonzero finite positive or negative auxiliary time gives zeros outside every bounded horizontal strip. There is consequently no finite-time all-real theorem for this family. The endpoint-recentered observation also has zeros outside every bounded horizontal strip. These statements concern the changed spectral family, not the zeros of the original theta transform.

This continues [the setup note](CHAT0053_ZERO_TIME_AUXILIARY_EVOLUTION_AND_REAL_ZEROS_20261031.md) and supersedes its open-status sentence for this specific transport. Read with the [result index](../../../../result-summaries/README.md), [theta cluster14](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control cluster12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [target reformulations](../../../../avoid/01_restating_the_target.md) and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md). Classification: a precise obstruction for a fully specified new family, not an RH-equivalent criterion or a theta collision exclusion.

The endpoint-versus-entire-growth method has a repository precedent in [Investigation3/07 round-two Note01, Section3](../../../investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md). That result concerns finite source changes, whose first uncancelled odd endpoint leaves finitely many real zeros. Here the moved nonzero endpoint leaves infinitely many, but only linearly many, real zeros; the extra bounded-strip Rouché argument and paired-product estimate handle this difference. No novelty claim for the general method is made.

## 1. Exact family and theorem

Use real source coordinate \(u\), complex spectral coordinate \(z\), auxiliary time \(s\in\mathbb R\), and physical time zero. The full source is
\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad u\ge0.
\]
It is strictly positive, has \(\Phi(0)>0\), and extends evenly and smoothly across zero, so \(\Phi'(0)=0\). For every fixed derivative order \(j\),
\[
|\Phi^{(j)}(u)|\le C_j e^{(9+4j)u-\pi e^{4u}}\quad(u\ge0).
\tag{1}
\]
One may obtain finite \(C_j\) by factoring \(e^{-\pi e^{4u}}\) from the differentiated series and using the summability of polynomial powers of \(n\) times \(e^{-\pi(n^2-1)}\). In particular,
\[
(2\pi^2-3\pi)e^{9u-\pi e^{4u}}
\le\Phi(u)\le C_0e^{9u-\pi e^{4u}}.
\tag{2}
\]
The lower bound uses just the first positive mode and \(e^{5u}\le e^{9u}\).

Start with the raw density in three dimensions,
\[
\rho_0(X)=\mathbf1_{\{|X|\ge1\}}
\frac{\Phi(\log|X|/2)}{8\pi |X|^3}.
\]
No Gaussian preparation is included. Evolve
\[
\partial_s\rho_s=\operatorname{div}(v\rho_s),
\qquad v(X)=X+\frac{X}{1+|X|^2}.
\tag{3}
\]
The velocity of a characteristic is \(-v\), not \(v\). Its radius satisfies
\[
r_s(r_0)^2=\sqrt{1+e^{-4s}r_0^2(r_0^2+2)}-1.
\tag{4}
\]
Define
\[
\chi_s(u)=\tfrac12\log r_s(e^{2u}),\qquad
F_s(z)=\int_{\mathbb R^3}\rho_s(X)\cos(z\log|X|/2)\,dX
      =\int_0^\infty\Phi(u)\cos(z\chi_s(u))\,du.
\tag{5}
\]
The pushforward and the initial radial Jacobian give the last equality. This is source-only transport followed by a fixed observation. Transporting the complete cosine-weighted density instead would leave the original transform invariant.

**Theorem.** For every fixed real \(s\ne0\):

1. \(F_s\) is even and real entire, of order one and infinite exponential type.
2. In each fixed strip \(|\operatorname{Im}z|\le D\), all zeros with sufficiently large \(|\operatorname{Re}z|\) are real and simple. Its sufficiently large positive real zeros, indexed by the lattice below, satisfy
   \[
   \lambda_n=\frac{n\pi}{|a_s|}+O_s(n^{-1}),\qquad
   a_s=\frac14\log\!\left(\sqrt{1+3e^{-4s}}-1\right).
   \tag{6}
   \]
3. There are infinitely many nonreal zeros, and their imaginary parts are unbounded in absolute value.

All thresholds and constants here are for fixed \(s\); the strip-asymptotic constants also depend on \(D\). No uniform claim as \(s\to0\) is made.

## 2. The moved endpoint

The logarithmic characteristic solves
\[
\partial_s\chi_s(u)=-b(\chi_s(u)),\quad
b(x)=\frac12\left(1+\frac1{1+e^{4x}}\right)
=\frac34-\frac14\tanh(2x).
\tag{7}
\]
Since \(1/2<b<1\), this is a complete increasing flow on \(\mathbb R\), with
\[
|\chi_s(u)-u|\le |s|,\qquad
\chi'_s(u)=\frac{b(\chi_s(u))}{b(u)}>0.
\tag{8}
\]
For fixed \(s\), its derivatives and those of its inverse are bounded; this also follows directly from the smooth bounded derivatives of \(b\) and its positive lower bound.

The image of the initial endpoint is \(a_s=\chi_s(0)\). Formula(4) gives (6); \(a_s<0\) for \(s>0\), \(a_s>0\) for \(s<0\), and \(a_s=0\) only for \(s=0\). Change variables \(x=\chi_s(u)\):
\[
F_s(z)=\int_{a_s}^\infty q_s(x)\cos(zx)\,dx,\qquad
q_s(x)=\Phi(\chi_{-s}(x))\chi'_{-s}(x).
\tag{9}
\]
The density is smooth and positive up to its one-sided endpoint, and
\[
q_s(a_s)=\frac{\Phi(0)}{\chi'_s(0)}
=\frac{\Phi(0)b(0)}{b(a_s)}>0.
\tag{10}
\]
Equations(1) and(8) imply, for each fixed \(s,D\) and derivative order \(j\),
\[
\int_{a_s}^\infty |q_s^{(j)}(x)|e^{D|x|}\,dx<\infty,
\tag{11}
\]
and the endpoint terms at infinity vanish in the integrations below.

Two integrations by parts give, for \(z\ne0\),
\[
F_s(z)=-q_s(a_s)\frac{\sin(a_sz)}z
-\frac{q'_s(a_s)\cos(a_sz)}{z^2}
-\frac1{z^2}\int_{a_s}^\infty q''_s(x)\cos(zx)\,dx.
\tag{12}
\]
Consequently, uniformly in every fixed horizontal strip,
\[
zF_s(z)=-q_s(a_s)\sin(a_sz)+O_{s,D}(|z|^{-1}),
\qquad |\operatorname{Re}z|\to\infty.
\tag{13}
\]
The estimate concerns the complete source. There is no truncated theta series and no numerical cancellation allowance.

## 3. All sufficiently distant zeros inside a fixed strip are real

Fix \(D>0\) and \(s\ne0\), and abbreviate \(a=a_s\). The zeros of \(\sin(az)\) are the real points
\[
x_n=n\pi/|a|,\qquad n\in\mathbb Z.
\]
Choose a fixed radius \(0<\delta<\min(D,\pi/(4|a|))\). On each circle \(|z-x_n|=\delta\), the modulus of \(\sin(az)\) has the same positive lower bound, independent of \(n\). For all sufficiently large \(|n|\), (13) and Rouché therefore put exactly one zero, counted with multiplicity, of \(zF_s(z)\) in that disk. These disks avoid zero, so this is exactly one zero of \(F_s\).

The disk is invariant under conjugation and \(F_s(\bar z)=\overline{F_s(z)}\). A nonreal zero would require its distinct conjugate in the same disk. Thus the unique zero is real and simple.

Outside these disks, \(|\sin(az)|\) is bounded below by a positive constant throughout the strip: use
\[
|\sin(a(x+iy))|^2=\sin^2(ax)+\sinh^2(ay)
\]
and periodicity in \(x\). Equation(13) excludes any further zeros at large \(|x|\). At the unique zero in a disk, (13) also gives \(|\sin(a\lambda_n)|=O_s(1/|n|)\); the simple sine zero gives (6).

In particular, counting multiplicity,
\[
N_+(R):=\#\{\lambda\in(0,R]:F_s(\lambda)=0\}
=\frac{|a_s|}{\pi}R+O_s(1).
\tag{14}
\]
Every fixed horizontal strip contains only finitely many nonreal zeros.

## 4. The tail forces more zeros than the real sequence can supply

From (2), (5), and (8), for \(R\) large,
\[
M_s(R):=\max_{|z|=R}|F_s(z)|
\le C_0e^{|s|R}\int_0^\infty e^{(R+9)u-\pi e^{4u}}\,du
\le \frac{C_0}{4}e^{|s|R}
\pi^{-(R+9)/4}\Gamma((R+9)/4).
\]
Stirling's formula gives
\[
\log M_s(R)\le \tfrac R4\log R+O_s(R).
\tag{15}
\]
This also supplies compact domination for the entire extension.

There are two useful lower-growth arguments. Positivity and the unbounded support of \(q_s\) give, for any fixed \(L>\max(0,a_s)\),
\[
F_s(iy)=\int_{a_s}^\infty q_s(x)\cosh(yx)\,dx
\ge \tfrac12e^{Ly}\int_L^{L+1}q_s(x)\,dx.
\tag{16}
\]
Thus \(\log F_s(iy)/y\to+\infty\). More precisely, insert the lower bound in(2), use \(\chi_s(u)\ge u-|s|\), and integrate over
\[
[u_y-1,u_y],\qquad u_y=\tfrac14\log(y/(4\pi)),
\]
which lies in the positive half-line for large \(y\). This gives
\[
\log F_s(iy)\ge\tfrac y4\log y-O_s(y).
\]
Together with(15),
\[
\log F_s(iy)=\tfrac y4\log y+O_s(y).
\tag{17}
\]
Hence \(F_s\) has order exactly one and infinite exponential type.

Suppose, for contradiction, that it has only finitely many nonreal zeros. By Hadamard factorization, pairing each zero with its negative, evenness gives
\[
F_s(z)=C P(z)\prod_{\lambda>0:F_s(\lambda)=0}
\left(1-\frac{z^2}{\lambda^2}\right),
\tag{18}
\]
where \(P\) is a finite even polynomial accounting for the nonreal zeros, with multiplicity. There is no zero at zero because \(F_s(0)=\int\Phi>0\). The possible exponential factor for an order-one function is \(e^{Az+B}\); since the paired product and \(P\) are even, evenness forces \(A=0\). The product converges locally uniformly because \(\sum\lambda^{-2}<\infty\). See the [checked Hadamard reference](../references/20_HADAMARD_FACTORIZATION_AND_TRANSPORT_SCOPE_20261031.md), printed page4; the application is derived here.

Equation(14) implies \(N_+(t)\le K_s t\) for all \(t>0\), after increasing \(K_s\) to cover the finitely many small zeros. Stieltjes integration by parts yields
\[
\begin{aligned}
\sum_{\lambda>0}\log(1+y^2/\lambda^2)
&=2y^2\int_0^\infty\frac{N_+(t)}{t(t^2+y^2)}\,dt\\
&\le \pi K_s y.
\end{aligned}
\tag{19}
\]
The finite polynomial contributes only \(O(\log y)\), so(18) gives \(\log F_s(iy)=O_s(y)\), contradicting(17). There are infinitely many nonreal zeros.

Section3 puts only finitely many nonreal zeros in any prescribed horizontal strip. Their imaginary parts must therefore be unbounded. This proves all parts of the theorem.

## 5. Merely recentering the observation does not cure the defect

Consider the obvious altered observation
\[
\widetilde F_s(z)=\int_0^\infty
\Phi(u)\cos(z(\chi_s(u)-a_s))\,du
=\int_0^\infty q_s(a_s+x)\cos(zx)\,dx.
\tag{20}
\]
Now the endpoint is zero, so the sine boundary term vanishes. Its first odd endpoint derivative, however, is nonzero. Put \(c_s=\chi'_s(0)>0\). Differentiating(8) gives
\[
\chi''_s(0)=\frac{c_s}{b(0)}\{b'(a_s)-b'(0)\}.
\]
Using \(\Phi'(0)=0\),
\[
q'_s(a_s)
=-\frac{\Phi(0)}{b(0)c_s^2}\{b'(a_s)-b'(0)\}
=-\frac{\Phi(0)}{2b(0)c_s^2}\tanh^2(2a_s)<0
\quad(s\ne0).
\tag{21}
\]
Here \(b'(x)=-\tfrac12\operatorname{sech}^2(2x)\).

Three integrations by parts give, uniformly in every fixed strip,
\[
\widetilde F_s(z)=-\frac{q'_s(a_s)}{z^2}+O_{s,D}(|z|^{-3}),
\qquad |\operatorname{Re}z|\to\infty.
\tag{22}
\]
Thus each fixed strip contains only finitely many zeros of \(\widetilde F_s\), including real zeros. The bounded shift in(20) leaves the order-one, infinite-type growth argument unchanged. If the total number of zeros were finite, Hadamard factorization would make \(\widetilde F_s\) a polynomial times \(e^{Az+B}\), of finite exponential type, a contradiction. It has infinitely many zeros, and their imaginary parts are unbounded.

This is the same first-uncancelled-odd-endpoint mechanism already present in the finite-source precedent, now with the exact derivative(21).

## 6. Interpretation, controls, and surviving directions

At \(s=0\), \(a_0=0\), and theta's reflection gives all odd endpoint derivatives zero. The algebraic boundary terms disappear. At \(s\ne0\), the fixed-observation family has a nonzero moving endpoint; the recentered family has a nonzero odd derivative. Both destroy the reflection compatibility needed to avoid these terms.

The theorem is independent of RH and makes no claim about reality of \(F_0=H(0,\cdot)\). The initial function has its classical bounded strip, while the evolved functions lose every bounded-strip property at arbitrarily small nonzero times. Nevertheless \(F_s\to F_0\) locally uniformly as \(s\to0\). The large-frequency thresholds in the proof are not uniform near zero; the additional nonreal zeros need not appear in any fixed compact set. No particular zero trajectory from \(s=0\) is asserted.

**Control screening.** This is a negative theorem for the transported family, not a proposed theta-only noncollision principle. No arithmetic premise is used in Sections2–4 beyond the checked source regularity, positive endpoint, unbounded positive tail, and order-one growth. The finite positive weighted-square controls pass those premises and obey the same obstruction under this transport. Positive Euler-factor shifts of theta likewise preserve a positive endpoint, derivative tails, and order-one growth, so they also pass; their shifted heat collisions are irrelevant to this fixed-time transport statement. Smooth double-exponential controls are covered when their derivatives satisfy(11); a shape label alone is not used to infer that hypothesis.

The reflected super-Gaussian control is not included in the stated order-one theorem; its super-Gaussian growth requires a separate order check or a more general formulation. Gaussian-polynomial variants also lie outside the order-one premise. Atomic fixed-profile controls fail the smooth endpoint-density premise. Compact-source controls fail the unbounded positive-tail premise (and may also fail endpoint smoothness); their transforms can have finite exponential type. Finite-prime and conditional endpoint controls are not asserted covered merely from their finite measurement lists: their full derivative tails, endpoint value, and entire order must be checked. The polynomial variants in the comparison table are outside this density formulation. No control is being excluded by a supposed theta-specific positivity advantage.

A viable different source flow would need to preserve the reflection compatibility, not merely mass or positivity. One concrete modification, offered only as a new candidate, is the odd logarithmic velocity
\[
\partial_s\psi_s(u)=\tfrac14\tanh(2\psi_s(u)),\qquad
\psi_s(u)=\tfrac12\operatorname{arsinh}(e^{s/2}\sinh(2u)).
\tag{23}
\]
It results from subtracting the constant \(3/4\) from \(b\) in the generator, rather than translating the already evolved endpoint. It fixes zero, is odd, and transporting the full even log source by it preserves evenness. Its half-line density therefore has all odd endpoint derivatives zero. The obstruction proved here does not apply to it. No strip contraction, eventual reality, or advantage over Newman evolution has been proved for(23).

The conclusion is restricted to(3)–(5) and the explicitly recentered variant(20). It excludes neither all source transports nor source weighting, smoothing, different vector fields, different initial representations, or other observations. It is not a statement about the energy-normalized conservative feedback or its physical nonvanishing problem. R11's separate assessment status and global physical coverage remain unchanged.
