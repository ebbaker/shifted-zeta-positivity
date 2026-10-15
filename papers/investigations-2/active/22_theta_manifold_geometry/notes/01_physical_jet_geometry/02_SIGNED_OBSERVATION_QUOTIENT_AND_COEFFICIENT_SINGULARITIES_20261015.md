# The exact signed observation quotient and allowable coefficient singularities

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. This note proves finite-dimensional algebraic statements and a conditional refinement of the signed boundary-trace criterion. It supplies no independent theta sign estimate and no collision exclusion for the complete theta field.

The starting point is [arithmetic boundary geometry Note 01](01_ARITHMETIC_BOUNDARY_TRACE_AND_SIGNED_OBSERVATION_20261015.md), especially its absolute quotient norm and its weaker signed target. The refinement here gives an exact quotient constant for the latter target and identifies precisely which singular reconstruction coefficients it permits.

## 1. The one-sided quotient theorem

Let \(V\) be a finite-dimensional real inner-product space, let
\(\mathsf J:V\to\mathbb R^2\) be a physical first-jet map, and let
\(\ell:V\to\mathbb R\) be an endpoint functional. Fix \(e\in\mathbb R^2\)
and write

\[
W(c)=e\cdot\mathsf Jc,\qquad E(c)=\|\mathsf Jc\|^2.
\]

**Signed quotient proposition.** If \(W\) is identically zero, the inequality

\[
W(c)\ell(c)\le C E(c)\qquad(c\in V)
\tag{1}
\]

holds with \(C=0\), without any restriction on \(\ell\). Otherwise, a finite nonnegative \(C\) exists if and only if

\[
\ker\mathsf J\subseteq\ker\ell.
\tag{2}
\]

Under (2), put \(L=\operatorname{im}\mathsf J\), let \(P_L\) be orthogonal projection onto \(L\), and set

\[
a=P_Le,\qquad b=\ell\mathsf J^\dagger\in L.
\]

Here rows and vectors are identified by the Euclidean metric. The least nonnegative constant in (1) is

\[
\boxed{C_{\rm sign}
=\frac{a\cdot b+\|a\|\|b\|}{2}.}
\tag{3}
\]

**Proof.** Choose \(c_*\) with \(W(c_*)\ne0\). For \(v\in\ker\mathsf J\), the complete starting jet, energy and \(W\) stay fixed on \(c_*+\lambda v\). If \(\ell(v)\ne0\), the left side of (1) is unbounded above for one sign of \(\lambda\). Thus (2) is necessary. Under (2), \(\ell\) descends uniquely to the covector \(b\) on \(L\), and (1) is

\[
(a\cdot z)(b\cdot z)\le C\|z\|^2\qquad(z\in L).
\]

Its least nonnegative constant is the positive part of the largest eigenvalue of \((ab^T+ba^T)/2\) on \(L\). If \(a,b\) span a plane, its two nonzero eigenvalues are
\((a\cdot b\pm\|a\|\|b\|)/2\). If they are collinear, the only possibly nonzero eigenvalue is \(a\cdot b\), whose positive part is again (3). The zero cases are immediate. This also proves sufficiency. \(\square\)

Thus a signed bound over an entire nontrivial homogeneous real-vector relaxation does not evade the endpoint kernel test. Its advantage appears in the size and parameter dependence of the descended covector, rather than in allowing uncontrolled kernel directions. This statement does not claim that theta coefficients vary over such a relaxation.

## 2. The two physical branches and an exact boundedness test

On branch zero, full stationarity is \(H_x=0\), so a nontrivial observed image lies on the \(H\)-axis. An endpoint reconstruction \(A H+B H_x\) contributes

\[
H(AH+BH_x)=AH^2\le A_+E,
\qquad C_{\rm sign,0}=A_+.
\tag{4}
\]

On branch one, full stationarity is \(H_{xx}=0\). It does not force either coordinate of \((H,H_x)\) to vanish. For the full two-dimensional observed image,

\[
\boxed{C_{\rm sign,1}(A,B)
=\frac{B+\sqrt{A^2+B^2}}2.}
\tag{5}
\]

Formula (5) is always a valid bound for actual first jets; it is the optimal bound over a specified homogeneous relaxation when its observed image is all of \(\mathbb R^2\). A smaller image can have a smaller optimal constant, computed by (3).

For a prescribed finite \(M\ge0\), (5) obeys \(C_{\rm sign,1}\le M\) if and only if

\[
\boxed{B\le M,\qquad A^2\le4M(M-B).}
\tag{6}
\]

Indeed the bound is equivalent to positive semidefiniteness of

\[
\begin{pmatrix}M&-A/2\\-A/2&M-B\end{pmatrix},
\]

whose principal-minor conditions are exactly (6), including \(M=0\).

Consequently a coefficient \(B\to-\infty\) can be allowed if the transverse coefficient satisfies \(A^2=O(-B)\). An unbounded positive \(B\) cannot be allowed. These are statements about a fixed reconstruction rule; manufacturing that rule by division by an unknown physical observation still supplies no independent bound.

## 3. Analytic degeneration with a bounded signed constant

Consider the analytic maps, for real \(\tau\),

\[
\mathsf J(\tau)=\operatorname{diag}(\tau^2,\tau^4),
\qquad \ell(\tau)=(\tau,-\tau^2),
\qquad e=(0,1).
\tag{7}
\]

Endpoint descent holds for every \(\tau\): the map is invertible when \(\tau\ne0\), and \(\ell(0)=0\). For \(\tau\ne0\), the descended covector is

\[
b(\tau)=(\tau^{-1},-\tau^{-2}).
\]

The optimal absolute quotient constant diverges:

\[
C_{\rm abs}(\tau)=\|b(\tau)\|
=\sqrt{\tau^{-2}+\tau^{-4}}\asymp |\tau|^{-2}.
\]

The optimal signed constant, however, is

\[
C_{\rm sign}(\tau)
=\frac{\sqrt{1+\tau^2}-1}{2\tau^2}
=\frac1{2(\sqrt{1+\tau^2}+1)}\le\frac14.
\tag{8}
\]

At \(\tau=0\) the optimal constant is zero. The optimal constant need not be continuous at this rank drop, but it has the uniform bound \(1/4\). That bound also has the polynomial certificate, for \(c=(c_0,c_1)\),

\[
\frac14\|\mathsf J(\tau)c\|^2
-\{e\cdot\mathsf J(\tau)c\}\ell(\tau)c
=\left(\frac{\tau^2c_0}{2}-\tau^3c_1\right)^2
 +\frac{\tau^8c_1^2}{4}\ge0.
\tag{9}
\]

This is an analytic matrix relaxation, not a theta field and not a backward-heat solution. It proves that the extra flexibility of a signed estimate can survive analytic degeneration and pointwise endpoint descent; it is not merely a favorable sign at a single fixed parameter.

## 4. A sharper conditional boundary-trace criterion

Suppose a source-prescribed complete identity gives

\[
V=A H+B H_x+C h_{j+1}+B_{\partial}+R,
\qquad |R|\le\varepsilon,
\]

and on the full stationary starts with \(\rho=\sqrt E>0\),

\[
\frac{h_j}{\rho}B_{\partial}\le C_0\rho+\varepsilon_0,
\qquad C_0,\varepsilon_0\ge0.
\tag{10}
\]

Define \(q_0=A_+\) and \(q_1=(B+\sqrt{A^2+B^2})/2\). Then

\[
\boxed{h_jV\le(q_j+C_0)E
 +(\varepsilon+\varepsilon_0)\sqrt E.}
\tag{11}
\]

**Proof.** The stationarity multiplier vanishes. Apply (4) or (5) to the reconstruction term, multiply (10) by \(\rho\), and use \(|h_jR|\le\varepsilon\rho\). \(\square\)

For fixed \(\delta>0\), (11) implies the exponential chord estimate

\[
h_j^2-e^{-\delta}h_jV
\ge-e^{-\delta}(q_j+C_0)E
 -e^{-\delta}(\varepsilon+\varepsilon_0)\sqrt E.
\tag{12}
\]

Thus it is sufficient that \(q_j\) and \(C_0\) stay locally bounded through the candidate event. The individual coefficients \(A,B\) need not stay bounded. This strictly enlarges the sufficient coefficient class in the earlier boundary-trace proposition. It does not produce any such identity or signed trace bound for theta. All cutoff errors, both lower boundaries, the complete starting factor, the full stationary conditions on both branches, and the fixed-length/cutoff/event order of limits remain required. The source prescription must establish the bound on \(q_j\) independently; (5) evaluated after an unknown collision has been excluded is not a certificate.

Allowing singular \(A,B\) does not automatically preserve a previous uniform source or cutoff remainder bound. Such a bound often depends on \(|A|+|B|\), and it must be proved again using any claimed cancellation. In particular, a joint killed-current construction's residual source norm can diverge even when \(q_j\) stays bounded. Formula (11) applies only after the stated error bounds have independently been established on the required event neighborhood.

## 5. Affine normalization is a separate issue

For an affine coefficient set \(c_*+D\), the same varying-kernel argument forces \(\ell(v)=0\) for directions \(v\in D\cap\ker\mathsf J\), provided some admissible starting value \(W\) is nonzero. It does not remove the affine endpoint offset. After descent along directions, the endpoint can have the form \(b\cdot z+d\), and the extra term \(d(e\cdot z)\) must be retained.

For example, \(W=z\), \(E=z^2\), and endpoint \(1\) have no uncontrolled direction in the endpoint's linear part, but \(z\le Cz^2\) fails for every finite \(C\) near \(z=0\). Formula (3) alone is therefore not an affine normalization criterion. If the affine observed set contains the origin and has a direction on which \(W\ne0\), an estimate on both signs near the origin forces the endpoint value at that origin to vanish.

## 6. A finite-jet diagnostic along the complete predecessor

At a spatial multiplicity \(2r+j\) event, the manuscript's complete stationary predecessor satisfies

\[
\rho(s)=c s^r(1+O(s)),\qquad
\frac{h_j(s)}{\rho(s)}=\sigma(1+O(s^2)),
\qquad c>0,\quad\sigma\in\{-1,1\};
\]

on branch zero the normalized factor is exactly \(\sigma\). Suppose a proposed complete boundary trace is analytic on this curve and has first nonzero term
\(B_{\partial}(s)=b_qs^q+O(s^{q+1})\). The exact, zero-error signed trace bound \((h_j/\rho)B_{\partial}\le C_0\rho\) can hold with a locally bounded nonnegative \(C_0\) on this predecessor if and only if either

\[
\sigma b_q<0\quad\hbox{or}\quad q\ge r.
\tag{13}
\]

An identically zero trace also passes. To prove this, the factor \(h_j/\rho\) has the fixed sign \(\sigma\); when \(\sigma b_q>0\), its positive pairing divided by \(\rho\) is asymptotic to \((\sigma b_q/c)s^{q-r}\). This is bounded exactly when \(q\ge r\). A favorable leading sign makes the bound hold with zero for sufficiently small positive \(s\).

This is a test of a proposed trace on one necessary event predecessor, not full local event coverage. A nonzero fixed mixed-error allowance changes the comparison and must not be silently set to zero. For a family of cutoffs, the appropriate error is first made small at fixed spatial length and fixed cutoff, before approaching the event. The diagnostic supplies no arithmetic premise forcing the favorable sign or vanishing order.

## Verification record

The [exact checker](../../numerics/check_joint_source_current.py) passes **3,803 overlapping rational assertions**, recorded in its [receipt](../../numerics/JOINT_SOURCE_CURRENT_CHECKS_20261015.json). The [review](../../reviews/10_JOINT_SOURCE_CURRENT_AND_SIGNED_QUOTIENT_REVIEW_20261015.md) distinguishes those finite algebra checks from the analytic proofs and the unresolved theta sign.
