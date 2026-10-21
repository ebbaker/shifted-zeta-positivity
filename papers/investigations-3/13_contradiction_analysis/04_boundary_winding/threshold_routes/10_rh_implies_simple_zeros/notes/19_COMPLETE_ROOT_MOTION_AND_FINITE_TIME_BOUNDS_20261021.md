# Complete root motion and finite time bounds

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this conversation's turn metadata.
Status: **proved in-note; same-assistant self-review only**. No specialist
review or simplicity exclusion.

This completes the quantitative HMC-01 work package: the entire distant
root contribution has a uniform explicit remainder, both velocity
summations are specified, and the moving deflation is retained. A finite
root-block estimate supplies the endpoint enclosure needed by the tail
theorem. These are quantitative estimates, not a reformulated collision
criterion. They also give a bounded-time width estimate for HMC-03.

Read with the [program][program], [progress register][progress],
[result index][results], [heat geometry][geometry], [control register][controls]
and [avoid index][avoid], particularly [target classification][a01],
[control premises][a02] and [scoped conclusions][a07].

## 1. Assumptions and normalization

Keep the complete theta source
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad 8H(0,z)=\xi(1/2+iz/2),
\]
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}.
\]
Assume RH for the real-root conclusions. At positive time the positive
roots are simple and have analytic fixed ranks
\(0<x_1(t)<x_2(t)<\cdots\), by [Note 01, Section 2][n01]. Fix
\(0<\epsilon<T<\infty\), an adjacent positive pair
\(a=x_k,b=x_{k+1}\), and \(g=b-a,c=(a+b)/2\).

The normalization and the local velocity/Hermite laws agree with
[Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3).
[Rodgers–Tao, Theorem 4.16](https://arxiv.org/html/1801.05914#S4)
states its dynamical theorem on \(\Lambda<t\le0\); its time range is
not silently extended here. The positive-time argument below uses the
paired product directly. The new work is the uniform remainder and its
consumers, not the classical root equation.

## 2. Explicit complete zero count and inverse square tail

Define constants depending only on the declared upper heat time:
\[
C_b^*=\frac1{1-16e^{-3\pi}},\qquad C_\Phi=2\pi^2C_b^*,\qquad
h_* =\frac{\pi(2\pi-3)}4e^{-\pi e},
\]
\[
B_T=\frac{T}{e^2}+\frac9{2e},\quad D_T=\frac{B_T^2}{2\pi},\quad
A_T=\log\frac{C_\Phi}{2h_*}+D_T,\quad
C_T=\frac{A_T+1}{2\log2}.
\tag{RM1}
\]
These constants are deliberately crude. For \(0\le t\le T\),
\[
H(t,0)\ge h_*,\qquad
|H(t,z)|\le\frac{C_\Phi e^{D_T}}4
 (2/\pi)^{r/4}\Gamma(r/4),\quad |z|\le r,\ r\ge4.
\tag{RM2}
\]
Indeed, \(n\le2^{n-1}\) and \(n^2-1\ge3(n-1)\) give
\(\sum n^4e^{-\pi(n^2-1)}\le C_b^*\). Dropping the negative
source terms therefore gives
\(\Phi(u)\le C_\Phi e^{9u-\pi e^{4u}}\). Retaining the first
positive term on \(0\le u\le1/4\) gives the lower bound in RM2.
Also \(u^2\le e^{2u}/e^2\), \(u\le e^{2u}/(2e)\), and
\(B_Te^{2u}-(\pi/2)e^{4u}\le D_T\). Substitute
\(v=(\pi/2)e^{4u}\) in the remaining integral to obtain RM2.
No theta index or source tail has been omitted.

Let \(N_t(R)\) count all complex zeros in \(|z|\le R\), with
multiplicity. Jensen's formula on radius \(2R\) gives, for \(R\ge2\),
\[
N_t(R)\log2\le A_T+\frac R2\log R,
\qquad N_t(R)\le C_T R\log(eR).
\tag{RM3}
\]
For completeness, the elementary bound
\(\Gamma(q)\le2(2q)^q\), \(q\ge1\), follows by splitting
\(e^{-v}=e^{-v/2}e^{-v/2}\) and maximizing
\(v^{q-1}e^{-v/2}\). Since \(2/\pi<1\), applying this at
\(q=R/2\) proves the first inequality from RM2. Radius limits handle
a zero on the outer circle. The count itself does not require RH.

Under RH all roots are real. Stieltjes integration, retaining both signs,
now proves the uniform bound
\[
\sum_{|r|>R}\frac1{r^2}\le
2\int_R^\infty\frac{N_t(v)}{v^3}\,dv
\le \mathcal B_T(R):=\frac{2C_T(\log R+2)}R,
\quad R\ge2.
\tag{RM4}
\]
The omitted integration-by-parts boundary term is nonpositive. RM4 is
uniform on \([0,T]\), including repeated time-zero roots with their
multiplicities. It implies normal convergence of the paired products
and their spatial logarithmic derivatives on compact sets off the roots.

## 3. Both velocity conventions and their finite remainders

Evenness and order at most one give
\[
H(t,z)=H(t,0)\prod_{j\ge1}(1-z^2/x_j(t)^2).
\]
There is no linear exponential factor. At a positive simple root,
\[
x_i'=\frac{H_{zz}}{H_z}(t,x_i)
=\frac1{x_i}+4x_i\sum_{j\ne i}\frac1{x_i^2-x_j^2}
=2\operatorname{PV}_{\pm}\sum_{r\ne x_i}\frac1{x_i-r}.
\tag{RM5}
\]
The last convention pairs \(x_j,-x_j\); the single mirror \(-x_i\)
is retained separately. Absolute convergence holds for paired summands,
not for an arbitrarily ordered sum of individual reciprocal distances.
No differentiation of an infinite product with respect to time is needed:
implicit differentiation gives the first equality and spatial
differentiation of the product gives the rest.

Suppose \(|a|,|b|\le A\), and use a symmetric physical cutoff
\(R\ge2\), \(R>2A\). Define
\[
S_R=\sum_{\substack{|r|\le R\\r\ne a,b}}
 \frac1{(b-r)(a-r)},\qquad
C_R=\sum_{\substack{|r|\le R\\r\ne a,b}}
 \left(\frac1{a-r}+\frac1{b-r}\right).
\]
Then the complete gap and center equations satisfy
\[
g'=4/g-2gS_{\rm ext},\qquad c'=C_R+E_c,
\tag{RM6}
\]
\[
0\le S_{\rm ext}-S_R\le4\mathcal B_T(R),\qquad
\left|g'-(4/g-2gS_R)\right|\le8g\mathcal B_T(R),
\tag{RM7}
\]
\[
|E_c|\le\frac83 A\mathcal B_T(R).
\tag{RM8}
\]
Every term in \(S_{\rm ext}\) is positive by adjacency, and this sum
is absolutely convergent without pairing. For the center, the tail of
one root velocity is exactly
\[
E_x=4x\sum_{x_j>R}\frac1{x^2-x_j^2},\qquad
|E_x|\le\frac{2|x|}{1-A^2/R^2}\mathcal B_T(R).
\]
Taking \(E_c=(E_a+E_b)/2\) proves RM8. Both errors are nonpositive
for the selected positive pair: the gap tail subtracts compression,
and the center tail has \(E_c\le0\). The weaker absolute forms above
also expose their constants. The finite cutoff may change membership
as a root crosses \(R\); the formulas are pointwise, and do not
differentiate a discontinuous cutoff sum.

Thus both remainders have the requested
\(O_{T,A}((1+\log R)/R)\) rate, uniformly on \([\epsilon,T]\).
No lower bound on nearby gaps or on \(H_z\) enters this tail estimate.
Nearby roots still have to be retained or independently enclosed.

## 4. A root-label enclosure and an intermediate width bound

There is a quantitative way to supply \(A\). For a fixed positive rank
\(K\), put \(Q_K=\sum_{i=1}^Kx_i^2\). Summing RM5 and cancelling
the finite internal pairs gives
\[
Q_K'=2K(2K-1)
-8\sum_{i\le K}\sum_{j>K}\frac{x_i^2}{x_j^2-x_i^2}
\le2K(2K-1).
\tag{RM9}
\]
The exterior terms are positive and converge by RM4. Consequently
\[
x_K(t)^2\le Q_K(\epsilon)+2K(2K-1)(T-\epsilon)=:A^2
\quad(\epsilon\le t\le T).
\tag{RM10}
\]
A complete-function enclosure of the first \(K\) roots at one time
supplies the initial sum. Under a hypothetical event at \((0,a_0)\),
choose \(K=k+1\) for the selected pair's upper rank. Continuity of
the finite birth cluster gives \(Q_K(0)\le Ka_0^2\), hence the fully
declared event-dependent choice
\[
A^2=Ka_0^2+2K(2K-1)T.
\tag{RM11}
\]
This is not a height-independent or label-independent enclosure.
Taking \(\epsilon\downarrow0\) in the integrated inequality is
legitimate even if \(K\) cuts through a larger birth cluster.

For the positive pair, its two mirror roots alone contribute
\[
\frac1{2a(a+b)}+\frac1{2b(a+b)}=\frac1{2ab}
\quad\hbox{to }S_{\rm ext}.
\]
With \(h=g^2\) and any enclosure \(a,b\le A\) on the interval,
\[
h'\le8-2h/A^2,
\quad h(t)\le4A^2+(h(s)-4A^2)e^{-2(t-s)/A^2}.
\tag{RM12}
\]
For a born pair, use RM11 and \(s\downarrow0\):
\[
0<g(t)^2\le4A^2(1-e^{-2t/A^2})<8t,
\qquad 0<t\le T.
\tag{RM13}
\]
This is a strict quantitative improvement over the double-birth upper
bound on a declared finite time interval. It uses generic mirror-root
compression, not a sign distinguishing theta from endpoint controls.
It gives neither a turning-time enclosure nor a collision.

## 5. Moving deflation and the time-zero distinction

Let \(P=(z-a)(z-b)=(z-c)^2-g^2/4\), and denote the deflated entire
function by \(D=H/P\) to avoid confusing it with the cutoff \(R\).
The exact equation is
\[
P(D_t+D_{zz})+4(z-c)D_z+
\left[-2c'(z-c)+g^2S_{\rm ext}\right]D=0.
\tag{RM14}
\]
Before using RM6 its last coefficient is \(P_t+2\); in particular
\(D_t=-D_{zz}\) is false. Write \(\ell=D_z/D\) near the cap.
Removability at both endpoints gives
\[
a'=-2/g+2\ell(a),\quad b'=2/g+2\ell(b),\quad
c'=\ell(a)+\ell(b),\quad
S_{\rm ext}=\frac{\ell(a)-\ell(b)}g.
\tag{RM15}
\]
The equivalent divided equation has apparent poles at \(a,b\);
RM15 cancels them. RM14 is the safer identity at the endpoints.

For an **exact double** at \((0,a_0)\), Weierstrass preparation for
the isolated two-root cluster makes \(c(t)\), \(h(t)=g(t)^2\) and
the local deflated factor analytic at zero, with \(D(0,a_0)\ne0\).
Thus
\[
S_0=-(\log D(0,\cdot))''(a_0)
=\sum_{r\ne a_0}\frac{m_r}{(a_0-r)^2}<\infty,
\]
\[
c'(0)=2\frac{D_z(0,a_0)}{D(0,a_0)},\qquad
g(t)^2=8t-16S_0t^2+O_{H,a_0}(t^3).
\tag{RM16}
\]
Here the sum deletes the two copies at \(a_0\) and retains all other
multiplicities. In particular the mirror double contributes
\(1/(2a_0^2)\). These local remainders depend on the isolated event;
no uniform isolation radius is asserted.

For a pair within an \(m>2\) cluster, with adjacent probabilists'
Hermite roots \(\lambda_i,\lambda_{i+1}\), the other cluster members
instead contribute
\[
S_{\rm ext}(t)=\frac1{2t}
\sum_{j\ne i,i+1}
\frac1{(\lambda_{i+1}-\lambda_j)(\lambda_i-\lambda_j)}
+O_{H,a_0}(t^{-1/2}).
\tag{RM17}
\]
The coefficient is positive. The Hermite root equations give its sum
as \(2/(\lambda_{i+1}-\lambda_i)^2-1/2\), consistently with RM6.
RM16's nonvanishing deflation and bounded \(S_0\) do not apply to
such a two-root deflation. RM7–RM13 remain valid at positive time.

## 6. Controls and verification scope

| Control | Response and failed premise |
| --- | --- |
| Quadratic and Hermite heat polynomials | Recover RM5, RM6, RM9 and RM14 by finite algebra. The quadratic has gap squared \(8t\); it lacks the positive-height mirror pair used in RM13. Even degree \(2K\) Hermite flow attains equality in RM9 with no exterior roots. These polynomials lack the theta source. |
| \(1+e^t\cos x\) | With \(\alpha=\arccos(e^{-t})\), the pair is \(\pi\pm\alpha\), \(g'=2\cot\alpha\), \(c'=0\), and \(S_{\rm ext}=1/(2\alpha^2)-\cot\alpha/(2\alpha)\). Its limit is \(1/6\), giving \(g^2=8t-(8/3)t^2+O(t^3)\). Its atomic source fails RM1–RM2's theta constants. |
| Euler factor with \(c=1\), under RH | The paired dynamics and root-block inequality survive its multiple endpoint. Its shifted source changes the particular growth constants; no rejection by RM6 or RM9 is claimed. |
| Weighted-square and finite-prime controls | They fail full reflection and do not supply an all-real heat slice. RM5–RM13 as all-real-root statements are not assigned to them. |
| Reflected and positive-primitive controls | They retain local heat/deflation identities but lack the unchanged integer-square expansion. No unproved all-real global root system is assigned to them. |
| Note 05's close endpoint controls | Under RH their later all-real simple roots satisfy the generic dynamical estimates, with constants for their own sources. Their ordinary Dirichlet arithmetic fails. Thus these bounds cannot exclude the multiple endpoints they retain. |

The [finite replay][replay] checks rational polynomial identities and
the algebraic constants only. The complete zero count, infinite tails
and uniformity are established by the proofs above, not by that replay.
The [self-review][review] records the mathematical and provenance limits.
The next source-time step is [Note 20][n20].

[program]: ../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[progress]: ../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[n01]: 01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md
[n20]: 20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[review]: ../reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md
[replay]: ../numerics/HMC_EXACT_ALGEBRA_REPLAY_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
