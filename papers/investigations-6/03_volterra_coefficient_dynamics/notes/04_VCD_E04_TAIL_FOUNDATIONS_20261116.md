# VCD-E04 r1 — Tail dynamics and analytic domains

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Tool dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, checked in-note.** This is a foundation audit of the five
groups in [plan §5](../research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md#5-vcd-e04--audit-exact-tail-dynamics-and-analytic-domains).
All eight hashes in the [frozen manifest](../numerics/04_VCD_INDUCTION_SESSION_INPUTS_20261116.json)
match. The proofs use [brainstorm Note03 §§1, 3–4 and 7](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md),
[manuscript §§2–5](../manuscript/main.tex), the
[E01 envelope](01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md), and the
[checked quadrature and Rouché passages](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md).
These foundations leave the source-sensitive closure and its zero implication open.

Retain the full even source \(W_\lambda=e^{\lambda u^2}\Phi\) on
\(0\le\lambda\le1/2\). Write \(Z_\lambda=\int W_\lambda\),
\(d\mu_\lambda=W_\lambda\,du/Z_\lambda\),
\(H_\lambda(z)=\tfrac12\int W_\lambda e^{izu}\,du\), and
\(F_\lambda(z)=2H_\lambda(z)/Z_\lambda\).
In the \(\mu_\lambda\)-orthonormal polynomial basis, the full self-adjoint
operator \(J=J(\lambda)\) is multiplication by \(u\), with zero diagonal
and edge \(a_j=\sqrt{\beta_j}>0\) between sites \(j-1,j\) for \(j\ge1\).
Use inner products linear in the second slot. Fix \(\lambda\) for the
operator identities. The projection \(\Pi_N\) retains \(0,\ldots,N-1\),
\(J_N\) denotes that finite block, and \(J^{[n]}\) denotes the tail
starting at \(n\), with \(J^{[0]}=J\).

## 1. Projection and finite evolution

Since \(\Pi_N e_0=e_0\), the projected full propagator has first matrix
element \(F_\lambda(x)\) for every real \(x\) and every \(N\ge1\).
The corresponding finite propagator has first matrix element
\(F_{\lambda,N}(x)=\langle e_0,e^{ixJ_N}e_0\rangle\).
To compare the matrices, the second derivatives at \(x=0\) of the
projected and finite propagators differ by
\[
 -\Pi_NJ^2\Pi_N\big|_{\operatorname{ran}\Pi_N}+J_N^2
 =-\beta_N|e_{N-1}\rangle\langle e_{N-1}|.
\]
All finite sequences lie in the domain of every power of \(J\), so
these projected derivatives exist. In the \(e_0,e_0\) entry, every
removed walk has length at least \(2N\). At length \(2N\) the unique
removed walk goes monotonically to \(N\) and returns. Hence all scalar
derivatives agree through order \(2N-1\) and
\[
 F_\lambda^{(2N)}(0)-F_{\lambda,N}^{(2N)}(0)
      =(-1)^N\prod_{j=1}^N\beta_j .
\]
This is a comparison of the fixed-\(\lambda\) readouts.

## 2. Real-height elimination

For \(N\ge1\), cut the bounded self-adjoint edge
\(B+B^*\), where \(B=a_N|e_{N-1}\rangle\langle e_N|\).
The resulting operator is self-adjoint on the domain of \(J\).
The domain splits into its prefix and tail parts since the finite prefix
lies in the domain. The cut operator acts diagonally in that splitting
and hence is \(J_N\oplus J^{[N]}\), with a self-adjoint tail. Cutting the
next edge of a tail gives the same realization of the next tail,
by restriction of the same domain to the narrower tail subspace.

The logarithmic growth also makes finite sequences a core on every
tail. Indeed, if their image under \(J^{[n]}-i\) had a nonzero
orthogonal vector \(f\), basis testing would give the formal Jacobi
equation \(J^{[n]}f=-if\). Sum its product with \(\overline f_j\)
over \(n\le j\le L\) and take imaginary parts. All internal edges
cancel in the imaginary part and
\[
 \sum_{j=n}^{L}|f_j|^2\le a_{L+1}|f_L f_{L+1}|.
\]
For nonzero \(f\) this would imply \(\sum_L |f_L f_{L+1}|=\infty\),
since \(\sum_L 1/a_{L+1}=\infty\) by the growth bound, contradicting
\(f\in\ell^2\). Hence the image is dense. The norm
\(\|(J^{[n]}-i)g\|\) equals the graph norm for self-adjoint \(J^{[n]}\),
so the finite sequences are graph dense. This also proves uniqueness
of the self-adjoint realization of the given tail recurrence.

Set \(\psi(x)=e^{ixJ}e_0=(y(x),v(x))\). This is a strong differentiable
orbit on the domain of \(J\), and \(v(x)\) belongs to the domain of
\(D=J^{[N]}\). With \(y(0)=e_0\), \(v(0)=0\) the block equations are
\[
 y'=iJ_Ny+iBv,\qquad v'=iDv+iB^*y.
\]
Differentiating \(e^{-ixD}v(x)\) on the real axis and integrating yields
\(v(x)=i\int_0^x e^{i(x-t)D}B^*y(t)\,dt\).
For \(k_N(x)=\langle e_N,e^{ixD}e_N\rangle\), substitution gives
\[
 y'(x)=iJ_Ny(x)-\beta_Ne_{N-1}
           \int_0^x k_N(x-t)y_{N-1}(t)\,dt,
 \qquad y_{N-1}(t)=\langle e_{N-1},y(t)\rangle .
\]
The two factors of \(i\) give the minus sign and the two boundary
crossings square the coupling. The real integral is oriented for
\(x<0\). The initial tail vanishes, so there is no independent
initial-data forcing.

## 3. Tail recursion and transforms

Apply §2 to the first site of \(J^{[n]}\), with initial vector \(e_n\).
The retained block is zero and its outgoing edge is \(a_{n+1}\), so
\[
 k_n'(x)=-\beta_{n+1}\int_0^x k_{n+1}(x-t)k_n(t)\,dt,
 \qquad k_n(0)=1.
\]
The moment walks give \(k_n''(0)=-\beta_{n+1}\) and
\(k_n^{(4)}(0)=\beta_{n+1}(\beta_{n+1}+\beta_{n+2})\).
Unitarity gives \(|k_n(x)|\le1\) on the real axis. For
\(\Re s>0\) put \(\widehat{k}_n(s)=\int_0^\infty e^{-sx}k_n(x)\,dx\).
Integration by parts and Fubini are justified by the real-axis bound
and \(|(k_{n+1}*k_n)(x)|\le x\) for \(x\ge0\).
The transformed equation is
\[
 [s+\beta_{n+1}\widehat{k}_{n+1}(s)]\widehat{k}_n(s)=1,\qquad
 \widehat{k}_n(s)=\frac{1}{s+\beta_{n+1}\widehat{k}_{n+1}(s)} .
\]

For \(\Im\zeta\ne0\) let
\(m_n(\zeta)=\langle e_n,(\zeta-J^{[n]})^{-1}e_n\rangle\).
Solve \((\zeta-J^{[n]})v=e_n\) by using the deeper-tail resolvent
for its tail component. This component is
\(a_{n+1}v_n(\zeta-J^{[n+1]})^{-1}e_{n+1}\), and the first-site
equation gives
\[
 m_n(\zeta)=\frac{1}{\zeta-\beta_{n+1}m_{n+1}(\zeta)} .
\]
With \(\sigma_n\) the probability spectral measure of \(e_n\), one has
\[
 \widehat{k}_n(s)=\int\frac{d\sigma_n(u)}{s-iu}
    =-i\,m_n(-is),\qquad \Re s>0 .
\]
The first equality uses absolute integrability in \((x,u)\).
The sign follows from \(s-iu=i(-is-u)\). This maps the right Laplace
half-plane to the lower resolvent half-plane. Alternating site signs
conjugate \(J^{[n]}\) to \(-J^{[n]}\) and preserve the basis-vector
spectral measures, so the equivalent upper-half-plane expression is
\(\widehat{k}_n(s)=i\,m_n(is)\).
The diagonal sign symmetry holds for the full multiplication operator
by reflection and passes to each cut. The resolvent sign follows from
\(\Im m_n(\zeta)=-(\Im\zeta)\int|\zeta-u|^{-2}\,d\sigma_n(u)\).
The two recursions recover the response at a shallower site from the
one at a deeper site.

## 4. Entire continuation on fixed vectors

The inherited envelope gives \(a_l\le C\log(l+2)\) for \(l\ge1\),
with \(C\) independent of \(\lambda\) in its band. For \(n\le j\)
and \(p\ge1\), finite propagation of the tridiagonal powers gives
\[
 \bigl\|(J^{[n]})^p e_j\bigr\|
         \le [2C\log(j+p+2)]^p .
\]
Indeed, the support after \(r\le p\) steps is within
\([\max(n,j-r),j+r]\). All \(p\) successive applications can use a
finite compression to \([\max(n,j-p),j+p]\), whose norm is at most
twice the largest edge bound there. The same estimate holds for
a right-truncated chain containing \(j\).

The vector series \(\sum_{p\ge0}(iz)^p(J^{[n]})^p e_j/p!\) therefore
converges normally on compact \(z\)-sets, uniformly in the allowed
\(\lambda\) at each fixed \(j\). It is the spectral exponential on
that vector for all \(z\in\mathbb C\). To check its domain, the
probability spectral measure \(\sigma_{n,j}\) of \(e_j\) satisfies
\[
 \int \cosh(2R u)\,d\sigma_{n,j}(u)
 =\sum_{p\ge0}\frac{(2R)^{2p}}{(2p)!}
                  \bigl\|(J^{[n]})^p e_j\bigr\|^2<\infty .
\]
Monotone convergence gives the equality, and the root test and the
displayed power bound give finiteness. Since
\(e^{2R|u|}\le2\cosh(2Ru)\), the spectral Taylor series converges in
\(L^2(\sigma_{n,j})\) to \(e^{izu}\) on \(|z|\le R\) by dominated
convergence. The same argument covers finite linear combinations of
fixed basis vectors by linearity on the spectral exponential domain.

For fixed \(N\) this yields entire \(k_N\), \(y\), and \(F_\lambda\).
In the scalar-boundary memory equation and the tail recursion one can
use the entire convolution
\[
 (k*f)(z)=z\int_0^1 k((1-t)z)f(tz)\,dt .
\]
The integrand is uniformly bounded on compacts for fixed entire \(k,f\),
and its holomorphic derivatives are locally bounded there as well.
The real-axis identities in §§2–3 thus extend by the identity theorem.
This continuation uses fixed-vector domains and finite entries.
For \(\Im z\ne0\), the spectral exponential of the full \(J\) is
unbounded since its multiplier has unbounded modulus on one end of
the full-line source.

There is also a moving-site obstruction for the actual theta source.
For every fixed \(\lambda\) and real \(b\ne0\), symmetry gives
\[
 k_N(ib)=\int\cosh(bu)\,d\sigma_N(u)
             \ge 1+\tfrac12 b^2\beta_{N+1}.
\]
The coefficients \(a_j\) are unbounded at each fixed \(\lambda\).
Otherwise \(A=\sup_j a_j<\infty\) would give
\(\int u^{2p}\,d\mu_\lambda=\|J^p e_0\|^2\le(2A)^{2p}\) for all \(p\).
Any positive \(\mu_\lambda\)-mass on \(|u|\ge L>2A\) contradicts this
as \(p\to\infty\), and the full-line weight supplies such mass.
It follows that \(\sup_{N\ge1} k_N(ib)=\infty\) for each \(b\ne0\).
In particular, absolute bounds on these unscaled moving kernels on a
fixed complex neighborhood of zero require a restriction or a different
quantity. The real-axis bound still holds for all sites.

## 5. Bare quadrature and shrinking strips

For each \(N\), the spectral measure of \(J_N\) at \(e_0\) is a
probability measure on the roots of \(P_N\). The characteristic
polynomial obeys the monic recurrence. Strictly positive internal
edges make evaluation at site \(0\) injective on each eigenspace by
the row recurrence, so the eigenvalues are simple and all spectral
weights are positive. Alternating site signs give evenness. The
moment agreement in §1 makes this Gaussian quadrature for
\(\mu_\lambda\), as in [manuscript §5](../manuscript/main.tex).
For \(m_{2p}=\int u^{2p}\,d\mu_\lambda\) and finite moments \(m_{2p,N}\),
the same walks are nonnegative products of edges, with only a subset
retained by \(J_N\). Thus \(0\le m_{2p,N}\le m_{2p}\) for all \(p\)
and equality holds for \(p<N\). Odd moments vanish. For fixed \(R\),
expansion of the Fourier transforms gives
\[
 \sup_{|z|\le R}|F_\lambda(z)-F_{\lambda,N}(z)|
      \le \sum_{p\ge N}\frac{R^{2p}m_{2p}}{(2p)!}\ \longrightarrow\ 0 .
\]
The majorant is the tail of the series for
\(\int\cosh(Ru)\,d\mu_\lambda<\infty\).
In fact \(d\mu_\lambda\le (W_{1/2}/Z_0)\,du\), so dominated
convergence of the integrated series tail is uniform in the given
\(\lambda\)-band on each fixed disk. The earlier real-window estimate
applies on its stated real-height domain.

For any specified entire \(G_N\to F_0\) locally uniformly in
\(\mathbb C\), consider the existence of positive \(R_N\to\infty\) and
\(\delta_N\to0\) such that
\[
 G_N(z)=0,\quad |z|<R_N
       \quad\Longrightarrow\quad |\Im z|\le\delta_N.
\]
Since \(F_0(0)=1\), around any hypothetical nonreal zero choose a
closed disk with zero-free boundary and positive distance from the
real axis. Rouché on that boundary supplies an approximant zero
inside for all sufficiently large \(N\), contradicting the
window and strip. The argument counts zeros with multiplicity.
It works for arbitrary entire approximants with the stated convergence,
including ones without finite-stage reality or conjugation symmetry.

Conversely, under RH the equality \(H_0(z)=\xi((1-iz)/2)/8\) makes
\(F_0\) nonvanishing on the compact sets
\(K_j=\{|z|\le j,\ |\Im z|\ge1/j\}\) for integers \(j\ge1\).
On \(K_j\), its positive minimum modulus and uniform convergence
make \(G_N\) nonvanishing for \(N\ge N_j\). Choose \(N_j\) strictly
increasing and put \(R_N=j,\ \delta_N=1/j\) when
\(N_j\le N<N_{j+1}\). Any earlier terms can use \(R_N=\delta_N=1\).
This gives the unspecified windows and widths. Thus their existence
is RH-equivalent once convergence is given, in particular for the
bare sequence at \(\lambda=0\). The equivalence makes no claim about
prescribed rates or a prescribed \(R_N,\delta_N\).

## Classification and controls

The exact equations are operator identities. The convergence estimate
is for approximation. The unspecified strips are a target reformulation
under [avoid 01](../../../../avoid/01_restating_the_target.md).
For provenance use the [result index](../../../../result-summaries/README.md),
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and the [avoid index](../../../../avoid/README.md), especially
[control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[exact representations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Apply the [collision catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
through the [inherited family-by-family screen](02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md#actual-control-screen)
and [Note03 §§6–7](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md#6-analytical-collision-control-screen).
The weighted-square controls satisfy both the envelope and the exact
approximation foundations at their validated positive-time collisions.
Their complete equal coefficients and full canonical reflection are
absent. The finite-prime square controls likewise lack full canonical
reflection. Euler translates, reflected super-Gaussian, and smooth
shape or primitive controls retain the generic memory and compact
approximation premises when their source has all exponential moments.
The translates change the summand score, with envelope failure proved
only for the inherited specified example. The super-Gaussian fails
the exponential confinement premise, and the smooth controls lack the
canonical summand formula. An individual coefficient-envelope comparison
for the latter controls remains untested. Finite atomic controls
terminate the recurrence and lack a positive full-line density.
Compact triangular extensions also lack global strict positivity.
The RH-conditional endpoint controls lack ordinary Dirichlet arithmetic
and the canonical summand formula. The varied-observation controls fail
the literal Fourier/Newman readout. The actual-profile relaxation
does not provide the same full-line source and readout. These
comparisons limit inferences from the shared foundations without
excluding a closure using additional canonical information. No collision
certificate or numerical campaign was rerun.
