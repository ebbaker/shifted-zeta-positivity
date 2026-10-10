# Enlarged-state transport, chord dynamics, and theta gluing

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred. These derivations and parallel
cross-audits are internal LLM work, not independent mathematical validation.

This revisits the dimensional-reduction program of [Heat Note 14](14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
after the signed bottleneck in [Heat Notes 23](23_SIGNED_CANDIDATE_LOCALIZATION_AND_RESONANT_BOUNDARY_PROGRAM_20261010.md)
and [24](24_CURVATURE_CONES_SHARP_NULL_PAYMENTS_AND_LOCALIZED_POISSON_20261010.md).
The proposal is to work in the full states behind programs 09 and 13, solve
or organize their simpler bulk dynamics, and then study the loss of
visibility at reduction. Three exact structures are developed here:
anchored divisor transport, a transverse gradient-overlap equation, and a
theta angular differential-shift relation. None yet gives the missing
one-sided estimate. The most direct new proof target is an effective
source-to-value-and-slope visibility theorem; it can bypass the fourth-jet
payment and covers every multiplicity on its certified domain.

## 1. What the enlargement should accomplish

The existing ordinary-double threshold route requires a signed finite
quadratic
\[
\mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2
\]
to be incompatible with its full physical error payment on the candidate
region. Note 24 localizes the remaining curvature and improves the
candidate-null payment, but establishes no such contradiction. Its pilots
do not sample a surviving joint candidate and do not prove its exclusion.
The fourth Cauchy payment is still a material loss, and the imported
density coefficient remains symbolic in the strengthened test.

An enlarged-state approach may instead prove that a prescribed physical
source cannot become invisible simultaneously in the two readouts. It
must retain the actual preparation, exact reduction, endpoints, and
approximation error. There is no requirement that this theorem take the
form \(\mathcal K<0\). Programs 09 and 13 already have the paid interface
for a first-jet alternative.

On a fixed-cutoff physical neighborhood write
\[
S=\sum_{n\le N}q_n=u+iv,\qquad F=2u,
\qquad |Q-F|\le\eta,\quad |Q'-F'|\le L\eta.
\]
The real-symmetric holomorphic disk sharpens the necessary condition for
every genuine multiple zero to
\[
\boxed{\left(\frac F\eta\right)^2+
          \left|\frac{F'}{L\eta}\right|\le1.}
\tag{1}
\]
This is the complete state condition, including its normalizer and
physical derivative. It is not a condition on each block, each Gaussian
slice, or each shifted state separately.

For the complete coherent current
\(\mathcal J=-\Im(S'\overline S)=u'v-uv'\), (1) also implies
\[
|\mathcal J|\le\frac\eta2 h(L|v|,|v'|),
\quad
h(D,B)=
\begin{cases}D+B^2/(4D),&D>0,\ B\le2D,\\ B,&B\ge2D.\end{cases}
\tag{2}
\]
At \(D=0\), use \(h(0,B)=B\). A strict reverse estimate supplied by
the full state would exclude a multiple zero. Equation (2) itself is a
support-function consequence of (1), not extra pointwise information.
The new work must be a correlated estimate on the source/state, rather
than a reformulation of the same two scalar readouts.

## 2. Program 09: commuting bulk evolution and noncommuting arithmetic transport

Freeze the integer cutoff \(N\). Let
\(\mathsf H e_n=(\log n)e_n\) on \(\mathbb C^N\), and put
\(\zeta=\sigma-iT\), where \(\sigma,T,\theta\) are the actual physical
functions of \(t,x\) from [program 09 Note 1](../09_prime_phase_torus/notes/1_ACTUAL_ORBIT_JETS_AND_EXACT_FINITE_HEAT_RESIDUAL_20261010.md).
Then
\[
q=e^{i\theta}\exp\{t\mathsf H^2/4-\zeta\mathsf H\}\mathbf1_N,
\qquad q_n=e^{t\log^2n/4-\sigma\log n+i(\theta+T\log n)}.
\tag{3}
\]
Before the physical pullback, independent variables \(\tau,\zeta\)
give an exact finite spectral heat equation
\[
\partial_\tau\psi_N=\tfrac14\mathsf H^2\psi_N
                     =\tfrac14\partial_\zeta^2\psi_N.
\tag{4}
\]
Equivalently, on the complexified prime torus,
\[
P_\tau(W)=\sum_{n\le N}e^{\tau\log^2n/4}W^{\nu(n)},\quad
\mathcal D=\sum_{p\le N}\log p\,W_p\partial_{W_p},\quad
\partial_\tau P_\tau=\tfrac14\mathcal D^2P_\tau.
\]
Unique factorization is the spectral dictionary. The physical pullback
has the simple diagonal connection
\[
q_x=(i\theta_x-\zeta_x\mathsf H)q,
\qquad q_t=(i\theta_t+\mathsf H^2/4-\zeta_t\mathsf H)q.
\tag{5}
\]
It is flat. Its spatial multiplier is exactly
\(-i\Omega+(-d+ic)\log n\), retaining amplitude drift. This does not
make \(F\) an independent homogeneous Newman solution: the genuine
finite heat residual and moving physical coordinates remain present.

Every constant diagonal phase matrix commutes with this evolution. In
particular, a constant multiplicative twist \(\chi(n)\) obeys the same
connection. Thus diagonal evolution and flatness do not select the actual
source preparation. This identifies what must be retained in the lift.

For a prime \(p\), let \(\mathsf S_p e_n=e_{pn}\) if \(pn\le N\),
and zero otherwise. With \(a=\log p\),
\[
[\mathsf H,\mathsf S_p]=a\mathsf S_p,\qquad
[\mathsf H^2,\mathsf S_p]=2a\mathsf S_p\mathsf H+a^2\mathsf S_p.
\tag{6}
\]
Define exact edge transport on the divisor graph by
\[
r_{p,n}=e^{t(2a\log n+a^2)/4-\zeta a},\qquad
(B_pv)_n=v_{pn}-r_{p,n}v_n,
\quad n\le\lfloor N/p\rfloor.
\]
Then
\[
\boxed{B_pq=0,\qquad q_1=e^{i\theta}.}
\tag{7}
\]
All retained integers are connected to 1 by prime division, so these
fixed edge values and the source uniquely specify \(q\). For a
multiplicative twist,
\[
(B_pq^\chi)_n=\chi(n)(\chi(p)-1)q_{pn}.
\]
Nontrivial twists fail the same prescribed edges. Abstract flatness
around prime cycles still holds if the edges are changed with the twist;
it is fixed physical transport, not flatness alone, that selects the state.

Differentiating (7) supplies exact tangent/source identities
\[
(B_pq_x)_n=-\zeta_xa\,q_{pn},\qquad
(B_pq_t)_n=(a\log n/2+a^2/4-\zeta_ta)q_{pn}.
\tag{8}
\]
The carrier drops out of each edge difference. Dilation also couples
partial sums to a real shift of the spectral argument:
\[
\sum_{n\le N/p}q_{pn}
=e^{-\zeta a+ta^2/4}e^{i\theta}
 \sum_{n\le N/p}e^{t\log^2n/4-(\zeta-ta/2)\log n}.
\tag{9}
\]
The shifted state on the right has its literal smaller cutoff. It does
not inherit the complete candidate equations.

## 3. An anchored source response and a precise visibility certificate

Stack the edge operators into \(B\). The positive parent operator
\(B^*B\) has kernel \(\mathbb Cq\). Adding the source anchor gives
\[
\boxed{A_{\rm bulk}=B^*B+e_1e_1^*>0,\qquad
q=A_{\rm bulk}^{-1}e_1e^{i\theta}.}
\tag{10}
\]
Positivity follows because \(Bv=0\) and \(v_1=0\) force \(v=0\).
Every hidden principal block is therefore invertible independently of
any observation nonvanishing. This permits exact Schur elimination of
hidden coordinates with all boundary/source terms retained. At the
\(n=1\) source, the unanchored Schur complement is zero; anchoring changes
it to one. Source coercivity does not yet give observation coercivity.

The standard [Feshbach--Schur formulation](https://arxiv.org/html/2105.02058v1)
is useful methodological guidance: invertibility of the eliminated block
must be justified before using its effective operator. Equation (10)
provides that justification for coordinate blocks. It provides no imported
theorem about the zeta observation.

Indeed, at fixed \(t,\sigma\), with \(U_Te_n=e^{iT\log n}e_n\),
\(A_{\rm bulk}(t,\sigma,T)=U_TA_{\rm bulk}(t,\sigma,0)U_T^*\).
Its spectrum is independent of \(T\) at fixed \(t,\sigma\), while its
projected response can cancel. Along physical \(x\), \(\sigma\) also
changes. A gap-only
proof cannot read the oscillatory observation. The open target is the
source-to-observation map, including its tangent in (8).

Here is an explicit alternative to estimating the fourth-jet quadratic.
Realify the state as \(q_R\in\mathbb R^{2N}\), and let
\[
Cv_R=\left(\Re\sum v_n,
 \frac1L\Re\sum[-i\Omega+(-d+ic)\log n]v_n\right).
\tag{11}
\]
Thus \(Cq_R=(F/2,F'/(2L))\). Define source covectors
\[
b^Tv_R=\Re(e^{-i\theta}v_1),\qquad
a^Tv_R=\Im(e^{-i\theta}v_1).
\]
For the prescribed state, \(b^Tq_R=1\), \(a^Tq_R=0\).

**Adjoint-transport certificate.** Suppose real multipliers
\(y\in\mathbb R^2,\lambda,z\) and a residual covector \(r\) satisfy
\[
\boxed{b=C^Ty+B_R^T\lambda+za+r.}
\tag{12}
\]
Write \(r_n\) for its two-dimensional integer blocks, and put
\(\mathcal R=\sum_{n\le N}w_n\|r_n\|_2\), \(w_n=|q_n|\).
Pairing (12) with \(q_R\) gives
\(1=y\cdot Cq_R+r\cdot q_R\), hence
\[
\boxed{\|Cq_R\|_2\ge\frac{1-\mathcal R}{\|y\|_2}}
\quad(\mathcal R<1,\ y\ne0).
\tag{13}
\]
At every genuine multiple zero, (1) implies
\(\|Cq_R\|_2\le\eta/2\): if \(s^2+|v|\le1\), then
\(s^2+v^2\le1\). Therefore outward cell bounds
\(\mathcal R\le R_{\rm up}<1\), \(\|y\|_2\le Y_{\rm up}\),
\(\eta\le\eta_{\rm up}\) give a sufficient exclusion
\[
\boxed{\frac{1-R_{\rm up}}{Y_{\rm up}}>\frac{\eta_{\rm up}}2.}
\tag{14}
\]
The sharper directional sufficient condition is
\(R_{\rm up}+\tfrac12\eta_{\rm up}h(|y_2|,|y_1|)<1\),
using uniform outward bounds for the support factor if \(y\) varies.

Equations (12)--(14) prove a certificate lemma, not existence of useful
certificates. An arbitrary pseudoinverse that divides by the unknown
joint observation only restates the scalar problem. The proof task is an
explicit regular multiplier construction, organized by arithmetic
transport and cutoff matching, with controlled \(R_{\rm up},Y_{\rm up}\).
It must not divide by \(F,F'\), or their unknown common-zero determinant.
Using only the edges for \(p=2,3\) leaves disconnected source sectors;
these must be retained or explicitly paid rather than silently removed.

## 4. Program 13: a simple chord generator and a hidden gradient overlap

Use the genuine positive even density and its pure wavefunction,
\[
m_t(u)=e^{tu^2}\Phi_e(u),\qquad
\psi_t=\sqrt{m_t},\qquad \partial_t\psi_t=\tfrac12u^2\psi_t.
\]
Introduce the real two-variable Weyl overlap, or chord field,
\[
\mathcal A_t(k,\ell)=\int_{\mathbb R}e^{iku}
 \psi_t(u+\ell/2)\psi_t(u-\ell/2)\,du.
\tag{15}
\]
It is Schwartz on the real \((k,\ell)\) plane and entire in \(k\)
for each real \(\ell\); no global complex-\(\ell\) square-root branch
is asserted. The reduction and evolution are exactly
\[
\boxed{\mathcal A_t(k,0)=2H_t(k),\qquad
\partial_t\mathcal A_t=(-\partial_k^2+\ell^2/4)\mathcal A_t.}
\tag{16}
\]
The generator is simple, but the observed slice is autonomous. Transverse
jets \(C_{2r}=\partial_\ell^{2r}\mathcal A|_{\ell=0}\) satisfy
\[
\partial_tC_{2r}=-\partial_k^2C_{2r}
                    +\tfrac12r(2r-1)C_{2r-2}.
\]
This lower-triangular hierarchy supplies no automatic feedback into
\(H\). Extra restrictions must come from the prepared theta state.

Define the derivative-wavefunction overlap
\[
\mathcal B_t(k,\ell)=\int e^{iku}
 \psi_t'(u+\ell/2)\psi_t'(u-\ell/2)\,du.
\]
Differentiating the rank-one product and integrating by parts gives
\[
\boxed{(\partial_\ell^2+k^2/4)\mathcal A=-\mathcal B,}
\tag{17}
\]
\[
\boxed{\partial_t\mathcal B=(-\partial_k^2+\ell^2/4)\mathcal B
                  -(k\partial_k+\ell\partial_\ell+1)\mathcal A.}
\tag{18}
\]
The source follows from the exact operator commutator. In particular, for
\(C=\mathcal A_{\ell\ell}|_{\ell=0}\),
\[
C(k)=-k^2\mathcal A(k,0)/4-
         \widehat{|\psi_t'|^2}(k),\qquad
|\psi_t'|^2=m_t\left(tu+\frac{\Phi_e'}{2\Phi_e}\right)^2.
\tag{19}
\]
At a genuine collision, \(C=-\widehat{|\psi_t'|^2}\). A positive
gradient density has an oscillatory Fourier transform, so this is a new
signed observable, not a sign theorem. It identifies a full theta
gradient/score insertion that the scalar moment relaxation discarded.

For \(W=-\log m_t\), equivalently
\(C=-\tfrac14\widehat{m_tW''}\). A relation
\(C=P(\partial_k)\mathcal A(k,0)\) with a finite constant-coefficient
polynomial would force \(W''\) to be a polynomial in \(u\).
The genuine tail has \(W''\sim16\pi e^{4|u|}\), so this specific
finite local closure is impossible. Nonlocal or arithmetic gluing
relations are still available.

There is also an exact dictionary for the threshold route. Freeze a
positive score slope \(\beta\) under spatial differentiation, let
\[
E(k)=\widehat{m_t(W'-\beta u)^2}(k),\qquad D=4C+E.
\]
Then integration by parts gives
\[
D=-\beta^2\mathcal A_{kk}-2\beta k\mathcal A_k
                         -(k^2+2\beta)\mathcal A.
\tag{20}
\]
At \(\mathcal A=\mathcal A_k=0\), write \(D_j=\partial_k^jD\)
and \(\mathcal A_j=\partial_k^j\mathcal A\). Direct elimination yields
\[
\begin{split}
\beta^4(2\mathcal A_3^2-3\mathcal A_2\mathcal A_4-g\mathcal A_2^2)
={}&2D_1^2-3D_0D_2-\frac{2k}{\beta}D_0D_1\\
 &+\left(\frac{18}{\beta}-\frac{k^2}{\beta^2}-g\right)D_0^2.
\end{split}
\tag{21}
\]
The mirror-only raw coefficient is \(g=9/k^2\); the density-strengthened
raw test requires its complete justified extra coefficient. The apparent
negative \(k^2\) term cannot be separated from the compensating derivative
terms. At approximate candidates the omitted value/slope terms from (20)
and all normalizer payments must be restored. A new proof would estimate
\(D_0,D_1,D_2\) jointly using the genuine theta preparation, rather than
apply separate absolute Cauchy bounds and reproduce the existing loss.

## 5. A collision control that the full-state estimate must distinguish

Pure-state completion and positive phase-space norms alone cannot exclude
a positive threshold. A bounded-time control is
\[
t_*=1/40,\quad
\Phi_{\rm ctrl}(u)=(16u^4+24)e^{-(1+t_*)u^2},\quad
\alpha=1+t_*-t>0.
\]
Its even positive Schwartz wavefunction has all identities (15)--(20),
Weyl Gram positivity, and the exact rank-one purity relation. Gaussian
Fourier differentiation gives
\[
\mathcal A_t^{\rm ctrl}(k,0)=\sqrt\pi\alpha^{-9/2}
 e^{-k^2/(4\alpha)}
 [k^4-12\alpha k^2+12\alpha^2+24\alpha^4].
\tag{22}
\]
At \(t=t_*\), the polynomial is \((k^2-6)^2\). The discriminant in
\(k^2\) is \(96\alpha^2(1-\alpha^2)\); hence the four zeros are
nonreal for \(t<t_*\), and all real for \(t\ge t_*\) while
\(\alpha>0\). At the threshold there are ordinary doubles at
\(\pm\sqrt6\). This is a Gaussian-tail control on its stated time
interval, not a super-exponential all-time Newman family. It suffices to
test any claimed exclusion based only on the local lift and purity.

The analogy with quantum backflow is useful for recognizing signed
coherent current: even positive spectral support does not give pointwise
current positivity. See the primary article [Probability backflow for
correlated quantum states](https://doi.org/10.1103/PhysRevResearch.2.033206).
Its Schrödinger estimates do not transfer automatically to Newman
evolution or to the carrier-dependent finite arithmetic branch. Here the
useful task is a theta-specific signed source/gradient-overlap estimate.

## 6. A further angular channel preserves the actual theta preparation

To retain arithmetic preparation before a rotor trace, set
\[
\Theta(r,y)=\sum_{n\in\mathbb Z}e^{-\pi n^2r+2\pi iny},\qquad
k(u,y)=e^u[\Theta(e^{4u},y)-1],\quad u\ge0.
\]
The periodic angular channel satisfies
\[
\Theta_r=\Theta_{yy}/(4\pi),\qquad
k_u=k+e^{4u}k_{yy}/\pi,
\tag{23}
\]
and exact Jacobi gluing
\[
\Theta(r,y)=r^{-1/2}\sum_{m\in\mathbb Z}e^{-\pi(m-y)^2/r}.
\tag{24}
\]
This is the heat-kernel form of [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32).
Retain the whole field
\[
\mathcal T_t(z,y)=\int_0^\infty e^{tu^2+izu}k(u,y)\,du.
\]
Super-exponential decay justifies it locally uniformly for bounded complex
parameters. A single integration by parts gives the exact relation
\[
\boxed{\frac1\pi\mathcal T_{yy}(z-4i,y)
=-k(0,y)+2it\mathcal T_z(z,y)-(1+iz)\mathcal T(z,y).}
\tag{25}
\]
It also satisfies \(\partial_t\mathcal T=-\mathcal T_{zz}\).
The endpoint source \(k(0,y)\) is essential. At \(y=0\),
\(\Re\mathcal T_t(x,0)\) is the existing rotor auxiliary \(J_t\).
The identity \((\partial_u^2-1)k(u,0)/16=\Phi(u)\) gives the genuine
\(H_t\) as its cosine readout.
This recovers the existing affine Ward identity but retains the complete
angular field and its modular partner.

Periodicity and (23) allow arbitrary Fourier coefficients \(C_n\).
The genuine preparation has \(C_n=1\) and the full gluing (24). Thus a
new argument must actually use those data; the PDE alone is not an
arithmetic selection theorem. The positive scalar Green-kernel collision
controls do not automatically carry this full package.

The fixed complex shift \(z\mapsto z-4i\) is not contained in the
imported radius-\(1/L\) approximation disk at large height. Relating (25)
to the normalized finite observation requires its own growth and error
estimates. Entireness alone is not a quantitative payment bound.

## 7. Stationary reduction becomes reflection, with paired boundaries

There is a concrete geometric bridge to the signed Poisson work. On
\(L^2(\mathbb R_+,dv)\), define the linear unitary involution
\[
(\mathcal I_Pf)(v)=\frac{\sqrt P}{v}f(P/v).
\]
The log-coordinate unitary
\[
g(y)=P^{1/4}e^{y/2}f(\sqrt P\,e^y)
\]
sends it to \(g(y)\mapsto g(-y)\). Combining with complex conjugation
gives an antiunitary reflection, a different operator. Literal blocks
\([A,B]\) map exactly to \([P/B,P/A]\).

For a chirped input \(f(v)=a(v)e^{iT\log v}\) (including a fixed
carrier in \(a\)), the stationary phase is \(T\log v-2\pi kv\).
With \(P=T/(2\pi)\), its leading local stationary coefficient is
\(e^{-i(T+\pi/4)}\mathcal I_Pf\), evaluated at output frequency \(k\).
This is linear, not the antiunitary map; no uniform endpoint or global
remainder theorem is asserted here. Comparing with the ideal physical
chirp yields the familiar
anti-linear moment relation. At the ideal center
\(\mu=\tfrac12\log P\), \(\sigma=\tfrac12+t\log P/4\), the log
amplitude is even and proportional to \(e^{ty^2/4}\). Use compact
blocks or qualified weighted domains; it is not globally square integrable
at positive time.

The natural cutoff near \(N=\sqrt P\) is the reflecting boundary
\(y=0\). The block \([N/2,N]\) is paired with approximately
\([N,2N]\), not with itself. The natural language is therefore matched
interior/exterior channels with explicit boundary coupling. There is no
small-commutator approximation for that sharp cutoff. Leading reflection
fixes the existing quadratic \(\mathcal K\), so it cannot alone supply
the missing sign.

The proof opportunity is to compute the *complete* matched flux or source
response: exact finite Poisson integrals, endpoint half-weights, carrier
mismatch, and reflection defects together. This could furnish regular
adjoint multipliers for (12), or a direct current estimate in (2).
Untested scattering terminology is not a sign theorem; full coupling and
error must be exhibited. This is consistent with Note 24's rational-grid
local Fourier reduction and its improved ceiling, without discarding the
remaining signed frontier.

## 8. Proof-oriented order of work

1. **Try source visibility on a bounded shrinking-sector cell.** Choose a
   closed \(\kappa=tL\) interval and a fixed-cutoff cell. Construct (12)
   by arithmetic adjoint telescoping and matched cutoff channels, with
   effective bounds for every residual and multiplier. Aim at (14), or
   its directional support version. The first informative success is a
   cell where the existing separate value/slope tests are inconclusive,
   excluded by a regular transport certificate. A restricted-family
   failure should identify the precise residual or multiplier loss.

   A proof-oriented asymptotic target is \(R_{\rm up}\le1-\delta\)
   and \(Y_{\rm up}\le C N^\alpha\), uniformly on a closed shrinking
   subsector, with \(\delta>0\) and
   \(\alpha<\inf(\kappa+4)/8\). Indeed
   \(\log N=\kappa/(2t)+o(1)\) and the imported
   \(\eta\le5e^{-\kappa(\kappa+4)/(16t)}\) imply
   \(\eta Y_{\rm up}\to0\). On \(1\le\kappa\le3/2\), the
   conservative sufficient exponent is \(\alpha<5/8\). Such effective
   bounds would turn (14) into eventual exclusion on that whole subsector.
   They are targets, not bounds obtained in this note.

2. **Use the coherent lift to estimate a full signed overlap.** Derive a
   theta-specific gradient/score correlation using (17)--(20) and the full
   preparation, then test whether it controls the complete current or
   the joint expression (21). The first-jet current route has fewer
   approximation costs; the threshold route can use Note 24's curvature
   localization. In either case adjacent packets and all cross terms
   remain present. Test the proposed lemma on (22) before attempting
   genuine huge-height estimates; its hypothesis must visibly distinguish
   the theta preparation from this pure-state threshold control.

3. **Retain angular gluing if the boundary correlation remains missing.**
   Use (23)--(25), with exact theta coefficients and Jacobi gluing, to
   derive an angular flux/boundary identity which can feed steps 1 or 2.
   First determine the growth payment for its complex shift. Another
   scalar endpoint Ward identity or a positive angular norm is not yet
   the required new estimate.

A bounded theorem would establish the mechanism, not RH. Extending it
must still cover cutoff changes, remaining shrinking sectors, higher
multiplicities if only the ordinary-threshold route is used, complementary
parameter ranges, and the small-time endpoint. A visibility theorem using
(1) already covers all multiplicities on its stated domain. Generic parent
positivity, purity, or leading modular/stationary symmetry supplies no such
uniform theorem by itself.

## 9. Checks and scope

The companion [algebra replay](../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
and [small record](../13_microlocal_phase_space/numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json)
check the anchored source/Schur example, Gaussian Fourier polynomial,
chord commutator, and score-to-jet identity using exact rational arithmetic.
They are finite controls of printed algebra. They do not enclose the
genuine huge-height state, establish a theta sign or a useful multiplier
bound, or certify any new candidate region. The analytical proofs of the
edge relations, certificate lemma, angular identity, and reflection map
are given above and internally cross-read. See the accompanying
[internal review](../13_microlocal_phase_space/reviews/8_ENLARGED_STATE_TRANSPORT_AND_CHORD_INTERNAL_REVIEW_20261010.md).

The conclusion of this investigation is a revised proof program with
specific enlarged-state quantities and one proved conditional certificate
lemma. The signed arithmetic/visibility estimate remains open.
