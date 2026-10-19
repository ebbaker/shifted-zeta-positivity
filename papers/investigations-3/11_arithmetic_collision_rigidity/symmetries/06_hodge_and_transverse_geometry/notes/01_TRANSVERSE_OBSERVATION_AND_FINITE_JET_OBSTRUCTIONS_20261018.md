# Transverse observations and finite theta jet obstructions

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from the turn metadata. Analytic derivations with exact
finite checks and same-model internal agent review; no specialist human review.

## Opening decision and contract

The first S06 attempt gives an exact observation map for a transverse base
derivative and scoped obstructions. A vertical derivative of the
complete source generally restores a nonzero exponential zero lattice mode. After
convergence and definite reflection parity are imposed, every finite
constant-coefficient combination of normalized vertical jets reduces to
ordinary physical derivatives. The coupled mixed-heat operator also fails
positivity preservation on a small explicit class of trigonometric
polynomials. These facts constrain the proposed transfers; they do not
exclude estimates using transverse or coupled information.

The primary objective is the program's **scoped obstruction** gate. The
physical comparison domain is
\(t\in[1/100,1/5], x\in[999,1001]\), but the analytic statements below
hold for every fixed real t and x where indicated. There is no spectral
cutoff, disk approximation, or new quadrature in this opening attempt.
Consequently no cutoff transition or approximation error is hidden in a
numerical comparison. The all-source convergence test is part of the gate.

| Contract item | Choice |
| --- | --- |
| Ambient data | Marked theta bundle, adapted metric of Investigation 22, arithmetic frame |
| New observation | Base p derivative of the complete source before p=0 restriction |
| Physical observation | Half-line cosine transform with its original heat weight |
| Derivatives | One base p derivative; general coefficient formula also stated |
| Boundary terms | Every integration-by-parts lower endpoint; upper current shown before its limit |
| Signed consumer | Original H, E=H²+H_x² and L0=H_x²−HH_xx; no auxiliary norm replaces them |
| Completed gate | Convergence obstruction for raw vertical insertions; finite-jet reduction and mixed-heat counterexample |
| Unpaid estimate | A cancellation-preserving comparison of the new observation and its boundary to the complete physical jet |

The [program guide][guide], [result summaries][summaries] and
[patterns to avoid][avoid] govern the interpretation. In particular consult
[collision controls][controls], [theta bookkeeping][theta-summary],
[geometric realizations][geometry-summary], [reformulations][a1],
[generic lifts][a3], [scoped exclusions][a7], and
[separate-bound losses][a12]. Global nonvanishing is the existing target;
rewriting it as a new observation is not an RH milestone.

## Complete source and the chosen transverse extension

Write D=partial_u, q=e^(4u), and use the period-one theta convention

\[
 \vartheta(z,\tau)=\sum_{n\in\mathbb Z}e^{\pi i n^2\tau+2\pi inz},
 \qquad \tau=p+iq.
\]

The Jacobi heat equation in this convention is
\(\partial_\tau\vartheta=(4\pi i)^{-1}\partial_z^2\vartheta\).
This follows term by term from the normally convergent series and agrees
with [DLMF 20.13.1](https://dlmf.nist.gov/20.13.E1) after replacing its
elliptic argument by pi*z. It is distinct from physical H_t=−H_xx.

Choose the extension dictated by the existing covariant fourth source
operator, keeping its q coefficients fixed under p differentiation:

\[
 \psi(u,p)=q^{1/4}\sum_{n\ge1}e^{-\pi n^2(q-ip)},\qquad
 \mathcal S(u,p)=\frac18(D^2-1)\psi(u,p).
 \tag{1}
\]

Indeed with \(J_k(p,q)=(\mathcal D^k\vartheta)(0,p+iq)\),

\[
 \mathcal S(u,p)=\frac{q^{1/4}}{16\pi^2}
 (q^2J_4-3\pi^2J_0).
 \tag{2}
\]

Both sides have n>=1 coefficients
\((2v_n^2-3v_n)e^u e^{-v_n+i\pi n^2p}\),
\(v_n=\pi n^2q\). The constant theta mode cancels for every p.
At p=0, \(\mathcal S=\Phi\) and \(\psi(u,0)=\psi(u)\).
This is a specified coefficient extension; substituting q−ip into all
prefactors would define a different extension.

For u>=0 and complex |p|<=1/4, \(q+\operatorname{Im}p\ge3q/4\).
Every fixed number of p and u derivatives is therefore dominated by a
polynomial in q and n times \(e^{-3\pi n^2q/4}\). The series is normally
convergent there and all these complete derivatives decay doubly
exponentially at the cusp. Multiplication by e^(tu²), a fixed polynomial,
or a fixed complex spectral exponential preserves integrability locally
uniformly in (t,x). This justifies the interchanges used below.

## A convergent base derivative with its exact endpoint

Directly from (1),

\[
 \partial_p\psi\big|_0=-\frac{i}{4q}(D-1)\psi,
 \qquad
 \partial_p\mathcal S\big|_0
 =-\frac{i}{32q}(D-1)(D-3)(D-5)\psi.
 \tag{3}
\]

The shift comes from D q^(−1)=q^(−1)(D−4), as an operator identity.
More generally, for m>=0, with an empty product at m=0,

\[
 \partial_p^m\mathcal S\big|_0
 =\frac{(-i/4)^m}{8}q^{-m}
 \{(D-4m)^2-1\}
 \prod_{j=0}^{m-1}(D-1-4j)\psi.
 \tag{4}
\]

These are coefficient derivatives, not uncorrected higher covariant jets.
For the first observation define

\[
 G_1(t,x)=\int_0^\infty e^{tu^2}
       (\partial_p\mathcal S)(u,0)\cos(xu)\,du,
 \quad f(u)=e^{tu^2-4u}\cos(xu),
 \quad P(D)=D^3-9D^2+23D-15.
\]

The finite upper-end current is

\[
 C(\psi,f)=\psi''f-\psi'f'+\psi f''
                   -9\psi'f+9\psi f'+23\psi f.
\]

Green's identity gives
\(\int_0^U(P(D)\psi)f=[C]_0^U+
\int_0^U\psi P(-D)f\). The complete source decay makes C(U) vanish.
At the lower end \(f(0)=1\), \(f'(0)=-4\),
\(f''(0)=2t+16-x^2\). Thus the exact physical bridge is

\[
 \boxed{G_1=-\frac i{32}
 \left[B_1(t,x)+\int_0^\infty
       \psi\{-D^3-9D^2-23D-15\}f\,du\right],}
 \tag{5}
\]
\[
 B_1=-\psi''(0)+5\psi'(0)+(x^2-2t-3)\psi(0)
     =-8\Phi(0)-\frac52+(x^2-2t-4)\psi(0).
 \tag{6}
\]

The second form uses the canonical theta endpoint \(\psi'(0)=-1/2\).
For a different square-series source, the first form remains valid with
that source's own endpoint data. The boundary is part of the signed
observation at its original scale.

This bridge can be evaluated using derivatives through order three of
the **one-sided** primitive transform

\[
 F_\psi(t,z)=\int_0^\infty e^{tu^2}\psi(u)e^{izu}\,du,
 \qquad z_\pm=\pm x+4i.
 \tag{7}
\]

For either exponential, put a=2tu+iz. Its adjoint integrand is
\(-[a^3+6ta]-9[a^2+2t]-23a-15\), multiplied by
e^(tu²+izu); replace each power u^j by i^(−j)partial_z^j after expanding,
with the z coefficients kept on the left. Average the z_+ and z_- values.
They are two damped half-line frequencies. Their sum is not
H(t,x+4i), whose cosine has a different second exponential. The map has
therefore identified a convergent signed estimating problem, not a local
formula in a few same-point derivatives of H.

## Metric and observation covector

Use [Investigation 22's adapted metric][metric]
\(\widetilde h=e^{2\pi p^2q}h\). On the zero section its connection is

\[
 \widetilde A=(2\pi pq-\pi ip^2)(dp+i\,dq).
\]

At p=0 both A_p and A_u vanish, so the first coefficient derivative in
(3) equals the first covariant derivative of the source section in this
frame. However,

\[
 \nabla_p^2 S\big|_0=\partial_p^2 S\big|_0+2\pi q S\big|_0,
 \qquad [\nabla_p,\nabla_u]S\big|_0=8\pi iq^2S\big|_0.
 \tag{8}
\]

The dual observation covector carries the opposite terms. The connection
and curvature contributions cancel in the complete paired scalar when
both factors are differentiated. A second covariant insertion with a
frozen coefficient test defines a different observation unless this
correction is retained. A bundle isometry likewise requires transporting
both source and dual test. Equations (3)–(7) stay in the fixed arithmetic
coefficient frame, so no unobserved positive metric norm enters them.

## Raw vertical insertions restore the zero mode

Let
\(T_k=\pi^{-k/2}q^{k/2+1/4}J_k(0,q)\). The already established ladder is
\(DT_k=T_{k+2}-k(k-1)T_{k-2}\), and
\(16\Phi=T_4-3T_0\). Specify the ambient extension
\(S(p,q,z)=q^{1/4}(q^2\mathcal D^4-3\pi^2)
\vartheta(z,p+iq)/(16\pi^2)\), whose zero-section restriction is (2).
Applying the vertical covariant derivative to this section before setting z=0 gives

\[
 V_m:=\left(\frac q\pi\right)^m\mathcal D^{2m}S\big|_0
       =\frac{T_{2m+4}-3T_{2m}}{16}.
 \tag{9}
\]

Its zero lattice mode is \(c_m e^u\), where

\[
 c_m=\frac{(2m+3)!!-3(2m-1)!!}{16}>0\quad(m\ge1).
 \tag{10}
\]

The remaining modes decay doubly exponentially. Consequently
e^(tu²)V_m fails the half-line heat-integrability test for every t>0.
The unnormalized insertion has zero mode
\(\pi^m c_m e^{(1-4m)u}\), which still fails it. Even a decaying ordinary
exponential cannot compensate positive quadratic heat growth. For a real
fixed x, the corresponding oscillatory cosine improper integral also
fails to converge: intervals with cosine bounded away from zero give
unbounded tails. At t=0 this latter conclusion does not apply to the
unnormalized insertion.

Already m=1 gives

\[
 V_1=\Phi'+\tfrac34T_2,\qquad
 T_2=e^u+2\psi',\qquad
 V_1-\tfrac34e^u=\Phi'+\tfrac32\psi'.
 \tag{11}
\]

Removing this zero mode makes a convergent coefficient expression, but
the subtraction is an additional operation. It is not permission to split
the original complete source into separately divergent transforms.

## Finite normalized jets with fixed parity reduce to physical derivatives

This gives a stronger scoped statement. Write A_m for the polynomial with
T_(2m)=A_m(D)T_0. The ladder gives

\[
 A_0=1,\quad A_1=D,\quad
 A_{m+1}=D A_m+2m(2m-1)A_{m-1}.
\]

Thus every finite constant-coefficient linear combination of normalized
even-order jets is Q(D)T_0, with Q a polynomial. Suppose Q has definite
reflection parity, \(Q(-D)=\epsilon Q(D)\), epsilon=±1, and suppose its
positive-time heat transform is required to converge as an ordinary
improper integral (without principal values or regularization). Since
\(T_0=e^u+2\psi\), convergence at +infinity forces Q(1)=0. Parity then
forces Q(−1)=0. Polynomial division gives

\[
 Q(D)=(D^2-1)R(D),\qquad
 \boxed{Q(D)T_0=16R(D)\Phi.}
 \tag{12}
\]

This proof uses the genuine theta reflection for T_0. All derivatives of
Phi decay at both ends, so integration by parts in the full-line Fourier
transform has no boundary. With the normalization
\(\mathcal F_t f=\frac12\int_{\mathbb R}e^{tu^2}f(u)e^{ixu}du\),

\[
 \mathcal F_t(Df)=-i(x-2t\partial_x)\mathcal F_t(f),\qquad
 \mathcal F_t(Q(D)T_0)
 =16R\!\left(-i(x-2t\partial_x)\right)H.
 \tag{13}
\]

Powers in (13) are operator compositions, retaining the noncommutation of
x and partial_x. For odd parity the full-line transform uses the sine
channel; it must not be identified with an odd source's half-line cosine
transform in (5). The statement covers finite constant-coefficient
normalized jets of definite parity. Variable coefficients, nonlocal
constraints, inequalities, and coupled sources lie outside this class.
Even within the class, estimating the resulting physical derivatives may
still be useful. The reduction supplies no independent favorable sign.

## The coupled mixed operator does not preserve positivity

For the existing addition identity put X=z+w, Y=z−w, A=q+r, B=q−r and
\(L=(2\pi)^{-1}\partial_X\partial_Y\). For B>0 the nonnegative
same-parity trigonometric polynomial

\[
 f(X,Y)=1+\cos(2\pi(X-Y))
\]

satisfies

\[
 e^{BL}f=1+e^{2\pi B}\cos(2\pi(X-Y)),
\]

which is negative at X−Y=1/2. For B<0 use
1+cos(2pi(X+Y)). This proves failure of positivity preservation on these
finite polynomials for every nonzero B. It does not challenge the
convergent action on the special theta Gaussian seed. The second-order
coefficient matrix has signature (1,1); a real nonsingular coordinate
change or scalar gauge conjugation cannot turn it into an elliptic
positive-diffusion operator.

A diagonal interpolation also transports the entire physical problem.
For interpolation parameter lambda in [0,1], define
\(q_\lambda=(A+\lambda B)/2\),
\(r_\lambda=(A-\lambda B)/2\),
\(u_\lambda=\log q_\lambda/4\),
\(v_\lambda=\log r_\lambda/4\).
The mixed theta identity becomes the product with these two parameters.
Applying the consistent complete source operators at q_lambda,r_lambda
gives \(R_\lambda=\Phi(u_\lambda)\Phi(v_\lambda)\) and

\[
 R'_\lambda=\frac B8
 \left\{\frac{\Phi'(u_\lambda)\Phi(v_\lambda)}{q_\lambda}
       -\frac{\Phi(u_\lambda)\Phi'(v_\lambda)}{r_\lambda}\right\}.
 \tag{14}
\]

For lambda>0, writing Q=q_lambda,R=r_lambda, U=logQ/4,V=logR/4,
the image of q,r>=1 is
\(Q+R\ge2, |Q-R|\le\lambda(Q+R-2)\), and

\[
 du\,dv=\frac{QR}{\lambda qr}\,dU\,dV.
 \tag{15}
\]

The map loses rank at lambda=0. The heat factors, spectral phases,
original source operators, domain and Jacobian cannot be frozen while
replacing the physical two-source integral by its diagonal. In particular
the primitive branch-0 edge and energy corner from the [complete signed
bridge][bridge] and the infinite cutoff strip from the [parity note][parity]
remain payable. Both parity sectors must be retained. Separate absolute
bounds require an independently paid comparison to complete physical
energy; polynomial-height payments of the stated kind fail in the parity
note's fixed-time unbounded regime.

## Controls and the next decision

| Control | Status for this attempt |
| --- | --- |
| Three- and four-square sources | The local Jacobi, p-transfer and covariant-jet algebra survive with their weights and endpoints. Their colliding event boxes prevent treating these identities as a strict test. They fail full theta reflection and canonical coefficients. |
| Finite-prime orbit sources | Finite measurements survive. Complete normalized reflection or another evaluated complete theta estimate remains missing; no effective event height is supplied. |
| Reflected super-Gaussian source | Reflection survives, exact theta square coefficients fail. Its event is rejected by the existing strict interface. |
| Smooth shape and positive-primitive sources | Their positivity and endpoint data do not supply the exact square-series premise. Analytic events are not replaced by fabricated boxes. |
| Euler controls | Unchanged level-one coefficients fail. The negative-Laguerre witness is distinct from a double-event box. |
| Polynomial and qTa events | Generic heat/Hodge algebra survives; exact theta source fails. Their known events reject strict first-jet tests. |
| Auxiliary smooth-density/two-channel constructions | A complete signed physical observation comparison is still missing. |

The [execution record][record] includes fresh rejection of five inherited
event boxes and the separate Euler witness. Those tests validate the
existing interface, not a new p-derivative inequality. The new exact checks
cover the transfer algebra, all Green boundary signs, zero-mode coefficients,
finite-jet reduction and the coupled counterexample's Fourier multipliers.
The analytic arguments above establish convergence and the stated scoped
obstructions; finite tests alone do not establish them.

The declared scoped-obstruction gate is met. No complete spectral error,
evaluation cost, signed domain or exterior onset improves. The real bridge
\(1001<|x|<e^{2000}\) on the original time slab remains open, as does the
complex exterior required by the conditional Newman route.

Do not launch a larger geometric construction or scan from these identities
alone. The next S06 contract must add a specific cancellation-preserving
inequality for (5) or the recombined two-source expression, with its boundary
paid at physical energy scale. The exact p map is now available for that
purpose; finite local jets or a positive-heat interpretation of L are
insufficient additions. The [internal review][review] records this decision.

[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta-summary]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry-summary]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a3]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[bridge]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[metric]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[parity]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md
[record]: ../numerics/TRANSVERSE_OBSERVATION_CHECKS_20261018.json
[review]: ../reviews/01_TRANSVERSE_OBSERVATION_INTERNAL_REVIEW_20261018.md
