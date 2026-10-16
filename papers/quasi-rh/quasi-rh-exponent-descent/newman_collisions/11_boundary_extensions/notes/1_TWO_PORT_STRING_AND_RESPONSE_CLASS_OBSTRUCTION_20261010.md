# Two-port string and the response-class obstruction

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available in this session and are not inferred. The checks here are internal,
not independent mathematical review.

This scout implements program 11 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The initial results are an explicit two-port positive string, a sharp
distinction between Cauchy visibility and determinant derivatives, and a
pole obstruction to identifying an entire heat function with a nonzero
passive resolvent response. A product extension does match the genuine heat
function exactly, while showing why its two oscillatory flux observations
are not local boundary Cauchy data.

## 1. Independently specified positive bulk

Fix \(c>0\) and \(\ell>0\). The Dirichlet operator
\[
 K=-\partial_y^2+c,
 \qquad D(K)=H^2(0,\ell)\cap H_0^1(0,\ell)
\]
is selfadjoint positive on \(L^2(0,\ell)\). Its form domain is
\(H_0^1(0,\ell)\), with energy
\(\int(|v'|^2+c|v|^2)dy\). For the homogeneous boundary equation
\((K-\lambda)v=0\), set \(k^2=c-\lambda\). The full transfer matrix is
\[
 \binom{v(\ell)}{v'(\ell)}
 =T_\ell(\lambda)\binom{v(0)}{v'(0)},\quad
 T_\ell=\begin{pmatrix}
 \cosh(k\ell)&\sinh(k\ell)/k\\
 k\sinh(k\ell)&\cosh(k\ell)
 \end{pmatrix},\qquad\det T_\ell=1.
\tag{1}
\]
The entries extend analytically at \(k=0\) and are entire in \(\lambda\),
so no square-root branch is intrinsic to this matrix.

For endpoint values \(f=(v(0),v(\ell))^\top\), the outward fluxes are
\[
 \binom{-v'(0)}{v'(\ell)}=N(\lambda)f,
 \quad N(\lambda)=k\begin{pmatrix}
 \coth(k\ell)&-\operatorname{csch}(k\ell)\\
 -\operatorname{csch}(k\ell)&\coth(k\ell)
 \end{pmatrix}.
\tag{2}
\]
For real \(\lambda<c\), integration by parts gives the exact Green identity
\[
 f^*N(\lambda)f=
 \int_0^\ell (|v'|^2+(c-\lambda)|v|^2)dy>0\quad(f\ne0).
\tag{3}
\]
The two eigenvalues are \(k\tanh(k\ell/2)\) and
\(k\coth(k\ell/2)\), both positive. At \(k=0\), the first eigenvalue
vanishes and the second tends to \(2/\ell\). These limiting cases are
retained; positivity is stated for \(\lambda<c\).

For every compact \(\lambda\)-set, (1) also gives a finite Cauchy
visibility constant:
\[
 \|v\|_{H^1(0,\ell)}
 \le C\bigl(|v(0)|+|v'(0)|\bigr).
\tag{4}
\]
It follows directly by bounding the two fundamental solutions and their
derivatives on the compact set. In particular, vanishing local value and
local flux force the homogeneous state to vanish.

## 2. Why a determinant derivative is a different channel

For the Dirichlet characteristic function
\(d(\lambda)=\sinh(k\ell)/k\), the zeros are
\(\lambda_n=c+(n\pi/\ell)^2\), \(n\ge1\), and
\[
 d'(\lambda_n)=\frac{(-1)^n\ell}{2(n\pi/\ell)^2}\ne0.
\tag{5}
\]
This is a genuine simplicity result for this independently specified model.
It does not identify \(d,d'\) with \(v(0),v'(0)\): a Dirichlet eigenmode
has two zero endpoint values and a nonzero endpoint flux. Differentiation
of a determinant in the spectral parameter includes the variation of the
whole boundary solution. A visibility theorem for local Cauchy data cannot
be applied to determinant and parameter derivative without a separate map.

Identifying \(H_t(x)\) with \(d(x^2)\) would furthermore impose this
model's rigid quadratic spectrum and its entire normalization. Such an
identification has not been derived. Shifting \(c\) changes the spectrum
and the determinant; it is not a free positivity repair for a fixed target.

## 3. Passive response obstruction

For a nonzero \(g\in L^2(0,\ell)\), the scalar passive response is
\[
 r(s)=\langle g,(K+s)^{-1}g\rangle
      =\sum_{n\ge1}\frac{|g_n|^2}{\lambda_n+s}.
\tag{6}
\]
It is positive for real \(s>0\), has positive real part for \(\Re s>0\),
and has a pole at each \(-\lambda_n\) with \(g_n\ne0\). At least one
such pole exists. Thus \(r(x^2)\) is meromorphic with a nonremovable
pole at some \(x=\pm i\sqrt{\lambda_n}\), whereas the genuine \(H_t(x)\)
is entire. Equality on any real interval would extend analytically and
contradict that pole. A nonvanishing entire normalizer cannot cancel it.

The same obstruction applies to the full two-port resolvent response
matrix when any observed spectral residue survives: its pole residue is
positive semidefinite and cannot be cancelled by summing diagonal positive
channels. A cross response, a response numerator, a determinant, or an
observation with source-dependent cancellations has a different analytic
class. The obstruction above is deliberately restricted to (6), not to all
boundary or inverse-spectral constructions.

The [Kwaśnicki–Mucha extension paper](https://arxiv.org/abs/1707.02475)
realizes complete Bernstein functions of the Laplacian by an appropriate
extension. It does not place the theta heat response in that function class.
For the present scout the class audit precedes any inverse realization.

## 4. An exact genuine extension and its surviving observation kernel

Let \(w=K^{-1}1\), so
\[
 w(y)=\frac1c\left(1-
 \frac{\cosh(\sqrt c(y-\ell/2))}{\cosh(\sqrt c\ell/2)}\right),
 \quad \alpha=w'(0)=\frac{\tanh(\sqrt c\ell/2)}{\sqrt c}>0.
\]
Set
\[
 U_t(u,y)=m_t(u)w(y),\qquad
 KU_t=m_t(u),\qquad\partial_tU_t=u^2U_t,
\tag{7}
\]
where \(m_t=e^{tu^2}\Phi_e\) is the full genuine theta state. This is a
positive elliptic extension with an explicitly prepared source. It lies in
the tensor product of the polynomially weighted spectral \(L^2\) domains
and \(D(K)\); boundary fluxes are classical here. On the unrestricted
Hilbert space the positive-time evolution remains unbounded multiplication.

The normalized inward flux observation and its fixed-time derivative are
\[
 \mathcal PU_t(z)=\frac1{2\alpha}
    \int_{\mathbb R}e^{izu}\partial_yU_t(u,0)\,du=H_t(z),
\]
\[
 \partial_z\mathcal PU_t(z)=\frac1{2\alpha}
    \int iu\,e^{izu}\partial_yU_t(u,0)\,du=H_t'(z).
\tag{8}
\]
Thus \(\mathcal P(u^2U)=-\partial_z^2\mathcal PU\) on the stated
theta class, with the required backward sign. The two channels in (8) are
different oscillatory integrals of the same flux; they are not the local
value and flux of a homogeneous solution. The state already has zero
Dirichlet boundary values. Even if both integrals vanish, (4) cannot be
applied at each spectral \(u\).

The elliptic energy is still strictly positive:
\[
 \int_{\mathbb R}\int_0^\ell
 (|\partial_yU_t|^2+c|U_t|^2)dy\,du
 =\|m_t\|_2^2\int_0^\ell w(y)\,dy>0.
\tag{9}
\]
This follows by testing \(Kw=1\) against \(w\). It has no lower-bound
implication for the joint observation (8). The same product extension
applies to the manuscript's positive-kernel threshold control. The actual
adjacent packet and multiplicative-twist controls additionally rule out
generic diagonal or twist-uniform repairs; their scopes remain distinct.

## 5. Normalization, cutoff, and continuation

The genuine observed collision pair is
\[
 \left(\frac{\mathcal PU_t}{2A_t},
 \frac{2}{LA_t}\bigl(\partial_x\mathcal PU_t-b\mathcal PU_t\bigr)\right),
 \qquad b=\partial_x\log A_t.
\tag{10}
\]
Its normalized PDE includes the complete drift and potential
\(-2b\partial_x-(\partial_t\log A_t+b_x+b^2)\). Differentiating in
\(x\) fixes time, the spectral cutoff if present, and the central scale
\(L\). Each higher jet of (10) retains all derivatives of \(A_t^{-1}\).

Spectral truncation of (8) is paid by the explicit bound (6)–(7) of
[the kinetic scout](../../10_kinetic_stochastic/notes/1_FIVE_JET_MEMORY_AND_FINITE_CLOSURE_OBSTRUCTION_20261010.md),
which is derived from the same theta series. On a closed complex rectangle
that bound is multiplied by the corresponding normalizer derivative suprema.
The full finite arithmetic approximation and its \(j!L^j\eta_N\) errors
from Note 13 then apply to this exact genuine observation. This scout claims
no newly certified large-height matching computation; equations (7)–(8)
provide exact matching instead.

The passive resolvent route stops at its analytic-class mismatch. The
product extension stops at the surviving oscillatory observation kernel.
A useful next bounded task would specify an arithmetic boundary numerator
with an independently defined source and prove that its *actual* two
collision observations coincide with homogeneous Cauchy data, including the
source residual. Without that dictionary, inverse fitting or finite jet
agreement would not create a collision theorem. No new exclusion or RH
conclusion is obtained.
