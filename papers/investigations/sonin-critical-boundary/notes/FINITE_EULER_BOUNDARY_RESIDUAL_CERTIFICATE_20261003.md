# A posteriori certificates for the finite Euler boundary correction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Internal analytic derivation; not
independent specialist refereeing. No arithmetic positivity is assumed.

The [finite-product identity](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md)
defines the correction by an actual boundary resolvent. This note supplies
a way to enclose that correction using approximate solutions and **full
Hilbert-space residuals**, together with a quantitative trace-norm bound
for truncating the source crossing operator. It is different from refining
the already insufficient mass and first compressed moment in the
[earlier calculation](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_COMPACT_FIRST_MOMENT_20260929.md).
The general residual identity is elementary numerical functional analysis;
the application, source nuclear-tail bound, and connection to the actual
Sonin cutoff are the progress here, with no priority claim.

## 1. Exact target and a source truncation bound

Fix finite \(S\), \(\sigma>0\), and a compact smooth complex source \(F\).
Use the identity note's operators \(C,T,X=Pa_e(D)\chi\), and put
\[
A=I_\chi-C^2=TT^*\ge gI_\chi>0,\qquad c=\|C\|<1.
\]
Then
\[
K[F]=2\Re\operatorname{Tr}(CA^{-1}TX).
\tag{1}
\]
The operator \(C\) need not be Hilbert--Schmidt. All trace classes below
come from \(X\) or finite-column source factors, not from \(C\) alone.

Let \(X_N: \chi\mathcal H\to P\mathcal H\) be finite rank, with
\(\|X-X_N\|_1\le\tau_N\). Factor it as
\(X_N=VW^*\), with finite-column operators
\(V:\mathbb C^r\to P\mathcal H\) and
\(W:\mathbb C^r\to\chi\mathcal H\). The factors can be obtained by a
singular-value factorization of the finite source matrix; no positivity
of that matrix is required. Write
\[
K_N=2\Re\operatorname{Tr}(W^*CA^{-1}TV).
\]
Using \(TT^*=A\) and commutation of \(C\) with \(A\),
\[
\|CA^{-1}T\|^2=\|C^2A^{-1}\|
\le\frac{c^2}{g},\qquad
\boxed{|K-K_N|\le\frac{2c}{\sqrt g}\tau_N.}
\tag{2}
\]
Thus source truncation loses only one square root of the gap, rather than
the full inverse-gap factor from a naive separate bound for \(T\).
An upper bound for \(c\), such as \(\sqrt{1-g}\), suffices throughout.

## 2. A primal-dual residual identity

Set \(b=TV\), \(d=CW\). For arbitrary finite-column approximations
\(Y,Z:\mathbb C^r\to\chi\mathcal H\), define the full residuals
\[
r_b=b-AY,\qquad r_d=d-AZ,
\]
and the computable corrected scalar
\[
\widehat K_N=2\Re\left\{
\langle d,Y\rangle_{\mathrm{HS}}+
\langle Z,r_b\rangle_{\mathrm{HS}}\right\}.
\tag{3}
\]
The Hilbert--Schmidt inner product is antilinear in its first argument.
Direct subtraction, using \(A=A^*\), gives the exact identity
\[
\boxed{K_N-\widehat K_N
=2\Re\langle r_d,A^{-1}r_b\rangle_{\mathrm{HS}}.}
\tag{4}
\]
Indeed \(A^{-1}b-Y=A^{-1}r_b\), and
\(d-AZ=r_d\). This proof has only bounded operators acting on
Hilbert--Schmidt finite-column maps, so no infinite trace is cancelled.
Consequently
\[
|K_N-\widehat K_N|
\le 2\|A^{-1/2}r_d\|_{\mathrm{HS}}
         \|A^{-1/2}r_b\|_{\mathrm{HS}}
\le\frac{2}{g}\|r_d\|_{\mathrm{HS}}\|r_b\|_{\mathrm{HS}}.
\tag{5}
\]
Combining (2) and (5) gives
\[
\boxed{|K-\widehat K_N|
\le\frac{2c}{\sqrt g}\tau_N
+\frac{2}{g}\|r_d\|_{\mathrm{HS}}\|r_b\|_{\mathrm{HS}}.}
\tag{6}
\]
Add a separate outward error for evaluating (3). The residual norms must
include the full continuous half-line, not just the tested rows of a
matrix. Approximations to \(b,d,AY,AZ\) also need their own propagated
errors. Formula (6) does not certify a computation merely because a linear
solver has a small matrix residual.

If both solves use one exact Galerkin space, its orthogonality makes
\(\langle Z,r_b\rangle=0\). Keeping the correction in (3) accommodates
inexact solves or different trial spaces. The error is a product of the
two full residuals; solving the dual problem can therefore improve on a
one-sided residual estimate. This observation has no sign assumption.

## 3. Explicit nuclear tails for the source crossing kernel

Assume \(\operatorname{diam}(\operatorname{supp}F)\le L\). Reflect the
negative coordinate and identify the nonzero part of \(X\) with the
operator on \(L^2(0,L)\) having kernel
\[
k(x,z)=\check a_e(x+z)=\Re\kappa_F(x+z),\qquad 0<x,z<L.
\tag{7}
\]
This kernel is smooth on the closed square and vanishes smoothly when
\(x+z\ge L\). There is no corner singularity from the half-line cutoff
inside this square.

Let \(\varphi_n(x)=\sqrt{(2n+1)/L}\,P_n(2x/L-1)\). These form an
orthonormal Legendre basis, with
\[
\mathcal L=-\partial_x\{x(L-x)\partial_x\},\qquad
\mathcal L\varphi_n=n(n+1)\varphi_n.
\]
Write \(k_{ij}=\langle\varphi_i,X\varphi_j\rangle\), and let
\(X_N\) retain \(0\le i,j\le N\), with zero extension to the full
half-lines. For an integer \(r\ge1\), define
\[
H_r=\|(I+\mathcal L_x)^r(I+\mathcal L_z)^r k\|_{L^2((0,L)^2)}.
\tag{8}
\]
Repeated integration by parts has no boundary terms because
\(x(L-x)=0\) at both endpoints, and all kernels being differentiated
are smooth. Parseval gives
\[
\sum_{i,j\ge0}(1+i(i+1))^{2r}(1+j(j+1))^{2r}|k_{ij}|^2=H_r^2.
\]
The trace norm of each normalized rank-one basis kernel is one.
Cauchy--Schwarz therefore yields, with
\(s_r=\sum_{n\ge0}(1+n(n+1))^{-2r}\) and
\(t_{r,N}=\sum_{n>N}(1+n(n+1))^{-2r}\),
\[
\|X-X_N\|_1
\le H_r\sqrt{2s_rt_{r,N}-t_{r,N}^2}.
\tag{9}
\]
This simultaneously proves absolute nuclear convergence of the expansion.
For \(N\ge1\), elementary integral bounds give
\(s_r\le2+(4r-1)^{-1}\) and
\(t_{r,N}\le N^{1-4r}/(4r-1)\). An entirely explicit version is
\[
\boxed{\text{one may take }\quad\tau_N
=H_r\sqrt{\frac{2(2+(4r-1)^{-1})}{4r-1}}
N^{(1-4r)/2}.}
\tag{10}
\]
For example the coefficient is \(\sqrt{14}/3\) at \(r=1\),
with rate \(N^{-3/2}\), and \(\sqrt{30}/7\) at \(r=2\),
with rate \(N^{-7/2}\). Higher orders are available for smooth sources;
the constants must be evaluated rather than presumed small.
The quantities in (8) involve only derivatives of the explicitly prepared
source correlation. Bounds such as
\(|\kappa_F^{(j)}(u)|\le\|F\|_2\|F^{(j)}\|_2\)
give simple, albeit possibly coarse, upper bounds. No Sonin spectral
approximation enters this source-tail step.

If an approximate coefficient matrix \(\widetilde X_N\) is used, add
\(\|X_N-\widetilde X_N\|_1\) to \(\tau_N\). Entrywise coefficient
errors bound this nuclear error by their absolute sum. SVD or factorization
roundoff must likewise be covered by the source-matrix error budget.

## 4. Application and remaining work

At prime \(2\), \(\sigma=1/2\), an admissible transport gap is
\[
g=(17-12\sqrt2)(1-\|C_\infty\|^2)>0.
\]
It can be made numerical with the already certified archimedean gap in
the earlier [prolate certificate](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md).
The bound is small; conditioning must be accounted for in (6), not hidden
by a successful finite-matrix solve.

The complementary [first-prime analysis](FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md)
develops a full-cutoff Gram calculation for controlling the part of these
residuals outside a finite trial space. It is essential to distinguish
\(E^*C^2E\) from \((E^*CE)^2\): their difference is the positive Gram
matrix of the omitted component of \(CE\). This is the next implementable
operator information beyond the previous first-moment summaries.

For a mean-zero prepared source, a rigorously positive lower endpoint for
\(K\) from (6) would refute the rank-one proposal at that support. A
negative interval would settle only that source. A finite-family result
cannot prove the all-source bound, and mean-zero negativity alone does
not settle mixed terms with the mean direction. The latter obligation
already appears in the [finite Mellin-defect lemma](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md),
which is reused here rather than rediscovered.

Equations (6) and (10) are analytic estimates. No numerical values of the
full residuals or a certified correction sign are claimed in this note.
The next certificate must supply those residual norms, source-tail
constants, finite arithmetic errors, and the actual cutoff gap together.
