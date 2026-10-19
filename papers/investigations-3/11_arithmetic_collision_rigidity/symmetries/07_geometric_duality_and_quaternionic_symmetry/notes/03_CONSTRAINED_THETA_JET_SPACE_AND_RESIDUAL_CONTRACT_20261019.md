# Constrained theta jets, automorphic residuals and the S07-T1 observation contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, verified from this turn's session metadata. Analytic
admissibility result and elementary norm estimates, with separate delegated
same-model mathematical and code review; no specialist human review.

## Outcome and boundary of the task

**S07-T1 is complete as an admissible-space and observation contract.**
The fourth covariant theta jets form a five-dimensional fiber space, with
an explicit orthogonal Gram matrix and evaluation kernel. The complete
source belongs to it but is not holomorphic. A smooth profile cutoff gives
a global automorphic approximation with a nonzero residual. That residual
generally leaves the five-dimensional space; its whole complement is
retained in a different, explicitly paid profile norm. This is not the
one-dimensional span of the already evaluated complete source.

The estimates below establish admissibility, not a useful paid physical
error constant. **S07-T2 is Ready** to evaluate this one selected residual
contract and compare its complete physical payment with a direct arithmetic
payment on the same domain. It must stop if the extra norms consume the
benefit. S07-T3 remains Waiting, S07-T4 Deferred, and no extension is
activated. No new physical sign, smaller complete error, cost advantage,
coverage or Newman bound is claimed.

Read the [result summaries][summaries] and [patterns to avoid][avoid],
particularly [collision controls][controls], [geometric results][geometry],
[target reformulations][a01], [shape-only arguments][a02], [scoped
exclusions][a07] and [separate-bound losses][a12]. This note proves a local
function-space result and identifies a genuine residual, rather than
proposing another global nonvanishing criterion. It continues [S07
Note 02][green] and the [T1 task contract][plan].

## Marked geometry, frames and the parent theta constraints

Keep exactly the existing tube and metric:

\[
 \Omega=[-1/4,1/4]_p\times[1,4]_q\times\mathbb T^2_{r,s},\qquad
 g=q(dp^2+dq^2)+q^{-1}(dr+p\,ds)^2+q\,ds^2.
\]

Put \(\tau=p+iq\), \(z=r+\tau s\), and use the marked holomorphic frame
\(e\), with \(h=\exp(2\pi p^2q-2\pi q s^2)\). The unitary frame is
\(e_U=h^{-1/2}e\); a section \(F e\) has unitary coefficient
\(h^{1/2}F\). Fiber integration is \(dr\,ds\), the fiber metric volume;
base integration in the ambient volume is \(q\,dp\,dq\). The physical
path is \(p=r=s=0\), with \(du=dq/(4q)\), not metric arclength.
No full modular descent or boundary condition is added.

The parent theta coefficient satisfies

\[
 \vartheta(z+1,\tau)=\vartheta(z,\tau),\quad
 \vartheta(z+\tau,\tau)=e^{-\pi i\tau-2\pi iz}\vartheta(z,\tau),
 \quad \partial_{\bar z}\vartheta=\partial_{\bar\tau}\vartheta=0,
 \quad(4\pi i\partial_\tau|_z-\partial_z^2)\vartheta=0. \tag{1}
\]

These relations follow directly from its complete integer-lattice series.
They describe original-I holomorphy; J-holomorphy is not imposed.
A fiber-holomorphic section with these degree-one multipliers is a scalar
multiple of theta: periodic Fourier expansion and the second multiplier
give \(c_{n+1}=e^{\pi i(2n+1)\tau}c_n\), hence
\(c_n=c_0e^{\pi in^2\tau}\). Joint I-holomorphy permits
\(c_0=c_0(\tau)\) holomorphic, and the last equation in (1) then forces
\(c'_0=0\). Thus imposing every homogeneous parent equation gives only
the constant theta line. This rigid parent class cannot accommodate a
nontrivial cutoff error. We retain (1) for the generator, and use its
covariant image plus explicitly paid defects for approximation residuals.

## Exact finite fiber space and its Gram matrix

At fixed base point write

\[
 A=\partial_z+2\pi i s,\quad B=\partial_{\bar z},\quad c=\pi/q,
 \qquad [B,A]=-c.
\]

These are the vertical Chern operators in the holomorphic frame; their
coefficients have the correct theta transitions. Integration over a full
fiber gives \(A^*=-B\). This also follows from the Gaussian calculation
below, without any boundary theorem. Set

\[
 V_4(p,q)=\operatorname{span}\{A^j\vartheta e:0\le j\le4\}.
\]

Let \(P_0(v)=1\), \(P_{j+1}=2vP_j-P'_j/2\), and \(v=\sqrt{\pi q}\,y\).
Define the isometric profile transform, in the unitary frame, by

\[
 Z_p[f](r,s)=\sum_{n\in\mathbb Z}f(n+s)
 e^{\pi ip n^2+2\pi in(r+ps)}. \tag{2}
\]

Then

\[
 (A^j\vartheta e)_U=e^{\pi p^2q}i^j(\pi/q)^{j/2}
 Z_p[P_j(\sqrt{\pi q}\,y)e^{-\pi qy^2}],
\]
\[
 \int_{T^2}Z_p[f]\overline{Z_p[g]}\,dr\,ds
   =\int_{\mathbb R}f(y)\overline{g(y)}\,dy. \tag{3}
\]

Indeed r integration removes unequal integer indices and the intervals
\(n+[0,1]\) partition the real line. Gaussian integration by parts gives

\[
 \int e^{-2v^2}P_j(v)P_k(v)\,dv
   =\sqrt{\pi/2}\,j!\,\delta_{jk}.
\]

Consequently the Gram matrix in the displayed jet basis is diagonal:

\[
 G_{jk}=\delta_{jk}\,
 \frac{e^{2\pi p^2q}}{\sqrt{2q}}j!(\pi/q)^j. \tag{4}
\]

All five diagonal entries are positive. In fact \(V_4=\ker B^5\) on
smooth automorphic sections: \(BA^j\vartheta=-jcA^{j-1}\vartheta\),
\(\ker B\) is the theta line just proved, and induction subtracts the
highest jet from any element of \(\ker B^5\). This is a fixed-fiber
statement, not closure under base derivatives.

An orthonormal unitary basis is \(E_j=Z_p[b_j]\), where

\[
 b_j(y;q)=\frac{2^{1/4}q^{1/4}}{\sqrt{j!}}
 P_j(\sqrt{\pi q}\,y)e^{-\pi qy^2}. \tag{5}
\]

The source and its fiber norm are therefore exactly

\[
 S=\frac{e^{\pi p^2q}}{16\,2^{1/4}}
       (\sqrt{24}\,E_4-3E_0),\qquad
 \|S\|_{T^2,h}^2=e^{2\pi p^2q}\frac{33}{256\sqrt2}. \tag{6}
\]

Here and in (6) the right side is expressed in the unitary basis.
The even source belongs to the three-dimensional even subspace
\(\operatorname{span}(E_0,E_2,E_4)\), and actually uses only levels 0 and 4.
It is not holomorphic:

\[
 BS=-\frac{q^{5/4}}{4\pi}A^3\vartheta e\ne0. \tag{7}
\]

## Reproducing kernel and the remaining base trace

For \(a=\sum_{j=0}^4d_j(p,q)E_j\), finite-dimensional duality gives

\[
 |a(p,q,r,s)|_h^2\le K_4(p,q,r,s)\sum_{j=0}^4|d_j(p,q)|^2,
 \quad K_4=\sum_{j=0}^4|Z_p[b_j](r,s)|^2. \tag{8}
\]

Equivalently \(K_4=\ell G^{-1}\ell^*\) with compatible Hermitian
evaluation. In particular the artificial base metric factor cancels.
At \(r=s=0\), odd levels vanish and

\[
 K_4(p,q,0,0)=\sqrt{2q}\sum_{j=0,2,4}\frac1{j!}
 \left|\sum_nP_j(\sqrt{\pi q}\,n)e^{-\pi q n^2+\pi ipn^2}\right|^2.
 \tag{9}
\]

This kernel uses the canonical theta jets and the elementary Gram matrix,
not the unknown physical value of S as a one-dimensional representer.
Gaussian majorants prove a finite uniform supremum on the compact base.
A rigorously evaluated useful supremum, its tail and its cost are T2 work;
no sampled maximum is substituted here.

Fiber control alone does not remove concentration in p. For any
Hilbert-valued \(d(p)\), the fundamental theorem of calculus and Cauchy
on the interval of length 1/2 give the safe bound

\[
 |d(0)|^2\le4\int_{-1/4}^{1/4}|d|^2dp
                  +\int_{-1/4}^{1/4}|\partial_pd|^2dp. \tag{10}
\]

The derivative in (10) is of the coefficients in (5), not silently the
covariant derivative of the whole section. In profile coordinates the
exact conversion is

\[
 \nabla_pZ_p[f]=Z_p[\partial_pf+i\pi(y^2-p^2)f],\quad
 \nabla_rZ_p[f]=Z_p[2\pi iyf],\quad
 (\nabla_s-p\nabla_r)Z_p[f]=Z_p[f_y]. \tag{11}
\]

Multiplication by \(y^2\) raises oscillator levels by two. Thus
\(\nabla_pV_4\) has components through level 6. A putative V4-closed
base connection would omit a real payment. T2 must either pay the
coefficient derivatives directly or retain this connection and the
additional moments/levels. Ambient volume and physical base measure
must also be converted explicitly.

## A genuine automorphic approximation and its residual

Let \(\eta(v)=0\) for \(v\le0\), \(\eta(v)=e^{-1/v}\) for \(v>0\),
and put
\(\chi_N(y)=\eta(N+1-|y|)/[\eta(N+1-|y|)+\eta(|y|-N)]\), for integer
\(N\ge1\). It is an even C-infinity cutoff, identically one for
\(|y|\le N\), zero for \(|y|\ge N+1\). The apparent absolute-value
corner is in a constant plateau. All annular derivatives must be paid
when used; they are not declared small.

Define

\[
 a_q(y)=q^{1/4}\{\pi^2q^2y^4-\tfrac32\pi qy^2\}e^{-\pi qy^2},
 \quad f_S=e^{\pi p^2q}a_q,\quad
 \widehat S_N=Z_p[f_S\chi_N],\quad R_N=Z_p[f_S(1-\chi_N)]. \tag{12}
\]

Both terms in (12) are global sections, and \(S=\widehat S_N+R_N\)
exactly. Indeed (2) has transitions

\[
 Z_p[f](r+1,s)=Z_p[f](r,s),\quad
 Z_p[f](r,s+1)=e^{-\pi ip-2\pi i(r+ps)}Z_p[f](r,s), \tag{13}
\]

by index shift. The index in the cutoff is \(n+s\), not n.
On the physical path \(\widehat S_N\) is exactly the ordinary source sum
with \(|n|\le N\); at each other fiber point it is also a finite sum.
In contrast an n-only cutoff fails (13), leaving an unaccounted seam.
We select N=2 as the first bounded T2 contract; this note does not optimize
N or claim that it gives a useful physical error.

The residual is nonzero and lies outside V4. Its profile vanishes on an
open interval and is nonzero on the Gaussian tail, whereas every profile
in V4 is a polynomial of degree at most four times that Gaussian. Its level-zero coefficient is strictly positive: on the nonzero tail,
\(a_q>0\), \(1-\chi_N\ge0\) and \(b_0>0\), since
\(\pi qy^2>3/2\). Thus the actual residual also has a low component.
In particular

\[
 R_N=\Pi_4R_N+(1-\Pi_4)R_N,\qquad
 \Pi_4Z_p[f]=\sum_{j=0}^4\langle f,b_j\rangle E_j. \tag{14}
\]

Neither term is discarded. One cannot identify the whole cutoff error
with its high-level projection, or estimate an arbitrary local S02/S03
spectral approximant by assigning it to V4. No ambient lift of those
spectral residuals is asserted by (12).

## Admissible source/error class and explicit complement payment

Use the Gaussian-profile class of smooth profiles f(p,q,y) with

\[
 |\partial_p^a\partial_y^bf(p,q,y)|
  \le M_{ab}(1+|y|)^6e^{-\pi qy^2},\qquad a,b\in\{0,1\}, \tag{15}
\]

for finite constants on the base rectangle. All V4 coefficient fields
with smooth bounded base coefficients, S, \(\widehat S_2\), \(R_2\),
and both projections in (14) belong to this class. Coefficient H1
extensions may be taken in the trace norm below; Gaussian-envelope
constants must still be provided for any later arithmetic estimate.
This is an admissible estimating class, not a claim that arbitrary
members obey the canonical source's inhomogeneous differential equations.

Set the stronger profile norm and its paid base trace norm to be

\[
 Y(f)=\int_{\mathbb R}(1+y^2)(|f|^2+|f_y|^2)dy,\qquad
 X(f)^2=\int_1^4\frac{dq}{4q}\int_{-1/4}^{1/4}
                    \{4Y(f)+Y(\partial_pf)\}dp. \tag{16}
\]

The full profile, or the complementary profile after (14), is measured
in this norm. It includes \(yf_y\) and \(f_{py}\), additional mixed/profile
regularity absent from the first-order bulk energy in Note 02. It is a
different norm: domination of that covariant bulk norm is not asserted.
A direct sampling proof gives the explicit safe admissibility inequality

\[
 \int_1^4|Z_0[f(0,q)](0,0)|^2\frac{dq}{4q}\le20 X(f)^2. \tag{17}
\]

For completeness, on \(I_n=[n-1/2,n+1/2]\),
\(|f(n)|^2\le2\int_{I_n}(|f|^2+|f_y|^2)\).
Also \(1+n^2\le2(1+y^2)\) there, and
\(\sum_n(1+n^2)^{-1}\le5\), by the integral test.
Weighted Cauchy therefore gives \(|\sum_nf(n)|^2\le20Y(f)\).
Apply (10) to the Hilbert space defining Y, and integrate in the actual
physical measure to obtain (17). This proves bounded observation on the
stated class; it does not evaluate its norm on a physical comparison box.

For the concrete residual put \(g=f_S(1-\chi_2)\). Its paid derivatives
are explicit:

\[
 g_y=e^{\pi p^2q}\{(a_q)_y(1-\chi_2)-a_q\chi'_2\},\quad
 g_p=2\pi pq\,g,\quad g_{py}=2\pi pq\,g_y. \tag{18}
\]

Thus X(g) is bounded by finite polynomial-Gaussian integrals on
\(|y|\ge2\), retaining the cutoff-derivative annulus \(2<|y|<3\),
the base metric factor and its derivative. These are independently
specified quantities; no full-source point evaluation occurs in the
norm. A future evaluation must bound the actual derivatives of the
chosen cutoff or explicitly replace it and reprice the contract.

The same sampling inequality can be used directly on g, or (8)/(10)
on \(\Pi_4g\) plus (17) on \((1-\Pi_4)g\). The latter also pays base
derivatives of the projection. Taking both payments without comparison
is not claimed to improve anything. Signed recombination remains an
option, not a consequence of these absolute norm bounds.

## Jacobi defects and exclusion of the old concentrating family

For clarity use the nonisometric profile \(a=e^{-\pi p^2q}f\) in the
holomorphic coefficient \(F=e^{\pi q s^2}Z_p[a]\). The parent vertical and Jacobi operators
have profile expressions

\[
 B:\quad \frac{i}{2q}(\partial_y+2\pi qy)a,
\]
\[
 \mathcal J a=2\pi(i a_p+a_q)+\frac{a_{yy}}{4q^2}
 -\frac{\pi y}{q}a_y+\left(\frac{\pi}{2q}-\pi^2y^2\right)a,
 \quad\mathcal J=4\pi i\partial_\tau|_z-\partial_z^2. \tag{19}
\]

The Gaussian parent is annihilated. The fourth covariant source has its
actual inhomogeneities, including (7); it is not declared a homogeneous
Jacobi solution. The exact cutoff commutators include

\[
 B(a\chi)-\chi Ba=\frac{i}{2q}a\chi',\quad
 \mathcal J(a\chi)-\chi\mathcal Ja
 =\frac{a\chi''+2a_y\chi'}{4q^2}-\frac{\pi y}{q}a\chi'. \tag{20}
\]

Any method using (19), B5 or further derivatives must retain their
annular derivatives and all additional base derivatives. Equations
(16)-(18) pay only the derivatives needed for the stated observation
bound; they do not pay every possible Green or PDE residual in advance.

The exact compactly supported concentrating sections of Note 02 are
outside V4 and outside (15). For fixed p,q,s, (15) gives Gaussian-decaying
Fourier coefficients in r, hence a real-analytic r function. A nonzero
compact r bump cannot have this property. However membership alone,
with unrestricted M, is not a uniform quantitative anti-concentration
estimate: finite Fourier approximations can belong with large constants.
The actual protection in (17) is the paid profile/base norm. In its larger
normed completion, compact smooth controls may be admitted, but their
old vanishing H1 energies do not imply small X. Base concentration alone
also incurs (10). No contradiction with the earlier obstruction arises.

Furthermore V4 with arbitrary base coefficients can lift many other
physical sources. Its membership alone is no discriminator for collision
controls. Canonical coefficients in (6), their equations and paid error
information would have to supply any future theta advantage.

## Physical observation contract and controls

For j=0,1 define on the bounded tube

\[
 \mathcal O_j[R](t,x)=\int_0^{\log4/4}
 e^{tu^2}R|_\gamma\,\partial_x^j\cos(xu)\,du. \tag{21}
\]

Equation (17) gives only the admissibility estimate
\(|\mathcal O_j[R]|\le\sqrt{20}X(f_R)
 \|e^{tu^2}\partial_x^j\cos(xu)\|_{L^2(du)}\).
A complete first-jet comparison must add the source beyond q=4, cutoff
and projection costs, arithmetic rounding, quadrature, base propagation,
normalizer conversion and any approximant/anchor error. If Green's
identity is used, all four p/q boundary faces and any new cutoff terms
remain. (17) itself uses no boundary identity and drops no flux.
Do not infer a lower bound from this upper estimate.

The [fresh source-control replay][control-record] exercises the unchanged
strict physical tests with their own sources and errors: five event boxes
are rejected and the Euler negative-Laguerre witness fails its signed
test. It does not validate (17), whose proof is above, or create a new
acceptance interface. The applicable premise screen is:

| Control | Premise absent from a canonical theta application |
| --- | --- |
| Polynomial/qTa heat events and counter-kernels | Complete canonical theta source/coefficients; local heat geometry alone is shared |
| Finite three-/four-square and finite-prime controls | Complete degree-one theta multipliers and unchanged canonical coefficients; selected arithmetic or square support is insufficient |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical integer-square theta source; reflection/shape alone is shared |
| Euler-factor controls | Unchanged conductor-one source; its signed witness is distinct from a double event |
| Smooth-density/two-channel constructions | Complete signed physical source/test comparison |
| Note 02 compact concentrating sections | Finite theta-jet/analytic Fourier constraints; if admitted in a larger norm, the extra profile/base regularity must be paid |

No effective event box is invented for the analytic finite-prime or
positive-primitive existence constructions. Generic Gaussian-profile
membership can admit alternative-source lifts, as just explained; the
upper estimate need not reject an event. Every eventual strict physical
acceptance test must fail on an event-containing control domain using
that control's own complete errors.

## Verification and next bounded step

The [exact checker][checker] and [execution record][record] verify Gaussian
Gram/ladder algebra, source inclusion/nonholomorphy, transition and
connection formulas, and targeted false truncation/closure fixtures.
These finite checks support the displayed derivations; they do not turn
a sampled norm into a uniform estimate. The [separate same-model
review][review] checks the source/error class, complement and scope.

For S07-T2 retain this tube and N=2; choose the complete bounded first-jet
error from (21) as the primary metric. Evaluate a uniform kernel or the
whole-profile bound, its actual residual norm and the q>4 payment, then
compare with the direct source-tail estimate on the same B pilot and
physical normalization. Both methods must pay the same retained source,
quadrature and outside-tube contribution. A true but losing estimate
completes that bounded feasibility attempt without activating T3. A new
mixed-adjoint construction, form degree or larger tube requires a new
explicit choice; none is launched here.

[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[green]: 02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md
[plan]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[checker]: ../numerics/check_theta_section_space.py
[record]: ../numerics/S07_T1_SECTION_SPACE_20261019.json
[control-record]: ../numerics/S07_T1_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/03_CONSTRAINED_THETA_SPACE_INTERNAL_REVIEW_20261019.md
