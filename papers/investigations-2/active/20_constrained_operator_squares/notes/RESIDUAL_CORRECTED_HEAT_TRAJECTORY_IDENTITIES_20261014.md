# Residual corrected heat trajectory identities

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: gpt-6-astra (Codex), reasoning effort **ultra**.

The February 2018 Heat Quantum notes obtain energy and normalization
from two positive diagonal integrals along exact imaginary-time evolution.
They correctly observe that replacing this evolution by approximate
dynamics can lose the variational bound. The identities below retain the
evolution error and the finite-time endpoint explicitly. They provide an
elementary first theorem and a precise benchmark target; no literature
novelty or computational saving is claimed.

## Exact infinite-time identities

Let A=A* >= alpha I with alpha>0. For u(t)=exp(-tA)rho and
Psi=integral_0^infinity u(t)dt=A^{-1}rho, spectral calculus gives

\[
 E:=\langle\Psi,A\Psi\rangle
 =2\int_0^\infty\|u(t)\|^2dt,\qquad
 N:=\|\Psi\|^2
 =4\int_0^\infty t\|u(t)\|^2dt .
\]

The coefficients follow from integrating exp(-2t lambda) and
t exp(-2t lambda) for each spectral value lambda>0. A positive spectral
gap supplies convergence and inverse domains for arbitrary rho in the
Hilbert space. Weaker assumptions require corresponding integrability.

## Finite-time theorem with an arbitrary path

First take A to be a finite-dimensional Hermitian matrix and
u:[0,T] -> C^n continuously differentiable. Define

\[
 r(t)=u'(t)+Au(t),\quad
 U(t)=\int_t^T u(s)\,ds,\quad
 d(t)=\int_t^T r(s)\,ds-u(T),\quad
 \Psi=U(0).
\]

Then AU=u+d, and exactly

\[
 \boxed{E=\langle\Psi,A\Psi\rangle
 =2\int_0^T\|u\|^2dt
 +2\operatorname{Re}\int_0^T\langle u,d\rangle dt,}
 \tag{1}
\]

\[
 \boxed{N=\|\Psi\|^2
 =4\int_0^Tt\|u\|^2dt
 +4\operatorname{Re}\int_0^Tt\langle u,d\rangle dt
 -2\operatorname{Re}\int_0^T\langle U,d\rangle dt.}
 \tag{2}
\]

**Proof.** Integrating r=u'+Au gives AU=u+d.
Put F(t)=<U(t),AU(t)>, which is real. Since U'=-u and A=A*,

\[
 F'(t)=-2\operatorname{Re}\langle u,AU\rangle
      =-2\|u\|^2-2\operatorname{Re}\langle u,d\rangle .
\]

As F(T)=0, integrating gives (1).
Also d||U||^2/dt=-2 Re<U,u>, hence

\[
 N=2\operatorname{Re}\int_0^T\langle U,u\rangle dt
  =2\int_0^TF(t)dt
    -2\operatorname{Re}\int_0^T\langle U,d\rangle dt.
\]

Integration by parts yields integral F=-integral t F', proving (2).

The same proof holds for unbounded selfadjoint A if u is continuously
differentiable in the Hilbert norm, takes values in Dom(A), and is
continuous in the graph norm on [0,T]. These sufficient assumptions
justify integration in Dom(A) and the displayed derivatives.

## The variational consequence and the missing endpoint

For Psi != 0, E/N is the exact Rayleigh quotient of the integrated
trial state. Thus E/N >= inf spectrum(A), regardless of the quality
of the approximate evolution. For A=H+E_s I, subtract E_s to obtain
the original Hamiltonian's energy.

Even if r=0, the finite-time defect is d=-u(T). Omitting the endpoint
does not reproduce the finite-time trial state's energy and norm.
On an infinite interval the formulas reduce to the original identities
only when the residual vanishes and all weighted boundary and integral
limits are justified.

The correction can be bounded without replacing it by a sign assumption.
With Q_0=integral||u||^2, Q_1=integral t||u||^2,
D_0=integral||d||^2, D_1=integral t||d||^2 and
V_0=integral||U||^2, Cauchy--Schwarz gives

\[
 |E-2Q_0|\le2\sqrt{Q_0D_0}=:\delta_E,\qquad
 |N-4Q_1|\le4\sqrt{Q_1D_1}+2\sqrt{V_0D_0}=:\delta_N.
 \tag{3}
\]

If A>=0 and 4Q_1>delta_N, then

\[
 \inf\sigma(A)\le \frac EN
 \le\frac{2Q_0+\delta_E}{4Q_1-\delta_N}.
 \tag{4}
\]

This is a certified upper bound only when the quantities on the right
are themselves bounded rigorously. The practical task is to make those
bounds useful and inexpensive for a chosen approximation. The estimates
can be conservative; no improvement over direct variational methods
follows merely from (3).

## A decisive simple check

For A=aI, a>0, and an approximate infinite-time path
u(t)=exp(-bt)v, b>0, the uncorrected diagonal quotient is b.
It lies below the ground energy if b<a. The actual integrated state is
Psi=v/b, whose Rayleigh quotient is a. Here r=(a-b)u; retaining its
correction recovers the actual quotient.

The [exact checker](../numerics/check_seed_identities.py) also tests
(1)--(2) for a non-eigenvector polynomial path with a positive,
non-diagonal rational matrix and a nonzero terminal value.
That finite example checks algebra and endpoints. The proof above
establishes the stated identity; neither is a many-body approximation
result.
