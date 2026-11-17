# VCD-GT-E03 r6 — Two literal Fourier-grouping screens

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The proof helper inherits the
session; actual model and effort are unavailable. This is a proof-author
return under [E03 r6][request], pending separate internal assessment, not
specialist review.

**Proved in-note for the two stated groupings.** The unchanged natural
difference-frequency matrix is indefinite when the spectral support has
two distinct positive radii. The constant-mode minus absolute-remainder
allowance is negative for the complete continuous source. Neither result
asserts negativity of the canonical numerator or excludes other Fourier
groupings. [Decision08][decision] selects the exterior route; this note
acquires no source values, divisor counts or canonical magnitude bound.

Read the [result index][results], [controls12][controls], and
[avoid index][avoid], especially [01][class], [02][screen], [07][scope]
and [12][joint]. These are scoped analytical feasibility results with
explicit failure tests, not an RH-equivalent criterion. The exact target
and earlier controls are in [Note24][input]; [Note21 §6][strip] supplies
the order/strip premise screen used below.

## 1. Natural matrix and a negative principal determinant

On a fixed slice let

\[
 F(z)=\sum_j\omega_j e^{izx_j},\qquad
 \omega_j>0,\quad \sum_j\omega_j=1,
\]

with distinct real nodes and an even measure: the node \(-x_j\) has
weight \(\omega_j\). Put

\[
 P_F=2(F''')^2-3F''F'''',\qquad m_r=\sum_j\omega_jx_j^r.
\]

Differentiating the finite sum and symmetrizing the product gives

\[
 P_F(z)=\frac12\sum_{j,k}\omega_j\omega_kx_j^2x_k^2
 (3x_j^2-4x_jx_k+3x_k^2)e^{iz(x_j+x_k)}.                 \tag{1}
\]

Replace the second node by its negative. For real \(x\), this is the
literal difference-frequency representation

\[
 P_F(x)=v(x)^*Mv(x),\quad v_j(x)=e^{-ixx_j},\quad
 M_{jk}=\frac{\omega_j\omega_kx_j^2x_k^2}{2}
 (3x_j^2+4x_jx_k+3x_k^2).                              \tag{2}
\]

For two distinct positive nodes \(p,q\), the diagonal entries are
\(5\omega_p^2p^6\) and \(5\omega_q^2q^6\). The determinant of this
principal submatrix factors as

\[
\begin{aligned}
 \det M_{\{p,q\}}
 &=\frac{\omega_p^2\omega_q^2p^4q^4}{4}
       \{100p^2q^2-(3p^2+4pq+3q^2)^2\}\\
 &=-\frac34\omega_p^2\omega_q^2p^4q^4
       (p-q)^2(3p^2+14pq+3q^2)<0.                     \tag{3}
\end{aligned}
\]

Thus the unchanged matrix \(M\) is not positive semidefinite and cannot
be written as \(T^*T\). Equivalently, with
\(u_j=\omega_jx_j^4\), \(w_j=\omega_jx_j^2\), and
\(r_j=\omega_jx_j^3\), it is
\(M=\tfrac32(uw^T+wu^T)+2rr^T\).

This rejects a Gram factorization of **this matrix**. It does not prove
\(P_F(x)<0\) anywhere: the vectors \(v(x)\) form a restricted curve,
not all complex vectors. Coincident difference frequencies can permit a
different coefficient matrix for the same function. Regrouping,
redistributing those coefficients, adding other frequencies with exact
cancellation, and local correlated-phase estimates are outside (3).
The representation as a Hermitian quadratic form in (2) uses real \(x\);
no complex-segment positivity is inferred from it.

## 2. Exact constant-mode/absolute-remainder allowance

Combine equal sum frequencies in (1). Its coefficients are nonnegative
because
\(3u^2-4uv+3v^2=u^2+v^2+2(u-v)^2\). Evenness gives, on the real line,

\[
 P_F(x)=C_0+2\sum_{\nu>0}C_\nu\cos(\nu x),\qquad C_\nu\ge0.
\]

The zero frequency consists exactly of opposite nodes. Consequently

\[
 C_0=5\sum_j\omega_j^2x_j^6,
 \qquad P_F(0)=3m_2m_4=C_0+2\sum_{\nu>0}C_\nu.        \tag{4}
\]

The value of the allowance obtained by retaining \(C_0\) and replacing
each remaining cosine by its separate lower bound \(-1\) is therefore

\[
 \boxed{\quad P_F(x)\ge L_{\rm abs}
       :=10\sum_j\omega_j^2x_j^6-3m_2m_4.\quad}        \tag{5}
\]

This is an exact formula for that lower allowance, not necessarily the
infimum of \(P_F\). The phases need not attain their separate extrema
simultaneously. If \(m_2m_4>0\), then \(m_6>0\). Writing
\(\omega_{\max}=\max_j\omega_j\), positivity gives

\[
 L_{\rm abs}\le10\omega_{\max}m_6-3m_2m_4.
\]

In particular the finite, sufficient failure test is

\[
 \boxed{\quad \omega_{\max}<\frac{3m_2m_4}{10m_6}
       \quad\Longrightarrow\quad L_{\rm abs}<0.\quad} \tag{6}
\]

For an \(N\)-node Gaussian quadrature with \(N\ge4\), exactness through
degree \(2N-1\) makes the moments in (6) those of its source. More
generally only exactness through degree six is needed for that statement.
No particular quadrature degree is acquired here, and no assertion about
\(\omega_{\max}\) tending to zero is needed or made. Failure of (6) to
hold is not success of the desired curvature bound.

For the complete normalized theta measure on a fixed slice, use its even
absolutely continuous density and finite sixth moment. The same product
formula is the Fourier transform of the finite positive measure obtained
by pushing

\[
 \tfrac12u^2v^2(3u^2-4uv+3v^2)\,d\mu(u)d\mu(v)
\]

forward under \((u,v)\mapsto u+v\). Its total mass is \(3m_2m_4>0\),
by evenness and the same evaluation at zero as in (4). The line
\(u+v=0\) has product-measure zero, including with this integrable
weight. Thus its zero-frequency atom is zero. The **same** strategy,
retaining only that atom and paying the rest by its absolute total mass,
has allowance

\[
 \boxed{\qquad L_{\rm abs}^{\rm continuous}=-3m_2m_4<0.\qquad} \tag{7}
\]

This applies to every slice of the fixed canonical slab after positive
normalization; the heat weight preserves evenness, absolute continuity
and the required moments. It also applies to other nondegenerate even
continuous positive sources with these moments. It does not rule out
retaining a neighborhood of the anti-diagonal as a phase-controlled
block, or grouping a signed remainder jointly. Those are different
allowances and require their own estimate.

## 3. Relation to the actual two-point target

For a counted pair put \(Q=(z-c)^2-D\), \(A=F/Q\), and
\(\mathcal L[A]=A'^2-AA''\). The regular divided difference gives

\[
 -K=\int_0^1\frac{\mathcal L[A]}{A^2}
       (z_2+s(z_1-z_2))\,ds.                         \tag{8}
\]

At a stipulated real nondegenerate double,
\(-K=P_F(c)/(18F''(c)^2)\). Hence the useful local target is
\(P_F(c)\ge18(59/100)F''(c)^2\), with strictly positive right side.
The negative allowance (7), or (5) when (6) holds, cannot pay it.
An indefinite matrix alone supplies no lower bound on that quotient.

At a conjugate pair \(c\pm ib\), the correct full target is

\[
 -K=\frac1{2b}\int_{-b}^b
       \Re\frac{\mathcal L[A](c+iy)}{A(c+iy)^2}\,dy.    \tag{9}
\]

A successful numerator estimate at a double still requires a two-point
extension and uniform time payment on \([0,1/10]\). A finite Jacobi
readout additionally requires the complete error, collar and derivative
payments, model-coordinate substitution, and its physical heat defect
from [Notes04][transfer] and [05][defect]. None is acquired in this note.

## 4. Collision controls and the scope of the decision

The calculations (1)–(7) are identities or failure tests, not collision
exclusion claims. The following screen prevents promoting them into a
positive-source sign theorem. Each untested geometric or quantitative
premise remains untested; failure of literal theta equality alone is not
evidence of failure of a derived inequality.

| Control family | Relevant shared, failed or untested premise |
| --- | --- |
| Five-atom readout of Note24 | Has positive even masses, two positive radii and a real double, but \(P_F(\pi)=-5/12\). It defeats automatic numerator positivity from these premises; its extra zeros have height \(\operatorname{arcosh}2>1\), failing the width-one strip. |
| Four-atom readout of Note24 | Has positive even masses and two positive radii, so (3) applies. Its strictly positive first undeflated Laguerre expression coexists with nonreal zeros. That expression is not (8); no full-slab deflated magnitude is supplied. |
| Exact even quartic | Shares the order, strip, local geometry and negative \(K\) of Note21, but is unbounded on the real axis and is not a Fourier transform of a finite positive measure. Its only exterior mass is the insufficient mirror group. |
| Nonzero Gaussian-factor heat controls | Fail order at most one. Their local analytic curvature examples are not thereby examples of the finite even positive spectral model used in (1); positive-source representation would need checking separately. |
| Euler-factor translates | Share positive even continuous source and the physical equation, hence (7). Order one is shared. Width one fails when the added initial height exceeds one, and is inherited by contraction otherwise; the specified local tube and useful lower mass remain untested. |
| Weighted-square, finite-source and finite canonical-score changes | Share applicable positive continuous Fourier and moment algebra, including (7), and order one. Their nonzero odd source endpoint makes zeros escape every fixed horizontal strip, as proved for these specified classes in Note21. |
| Finite-prime orbit controls | Share their positive continuous source, finite matched data and order one. The stated bounded-coefficient, endpoint-defective classes fail the fixed global strip. Their high-gap events do not locate this tube. |
| Reflected super-Gaussian | Shares positive even continuous source and the physical equation, so (7); fails order at most one through its super-Gaussian component. |
| Smooth shape and positive primitive | The damped positive continuous constructions share (7) and the order bound. Their common strip, this tube and useful exterior mass are untested. The Gaussian precursor's order-two failure is a separate fact. |
| Reflection rigidity / four-family comparison | The complete reflection-plus-normalized-endpoint conjunction forces theta weights only in its stated polynomial square-comb class. It supplies no missing estimate in (8); the separate families retain the individual failures above. |
| BW-01 and finite-profile threshold controls | Positive finite atoms share (1)–(6) when even; the matrix failure additionally requires two positive radii. Compact continuous extensions satisfy (7). Their threshold information supplies neither this earlier slab nor this tube's full two-point magnitude. |
| RH-conditional normalized endpoint merger | Keeps its RH premise. Its positive continuous source shares (7), order one and, under RH, the strip. Remote added doubles do not pay the present tube or lower-mass budget. |
| Changed observation kernels | Do not supply the literal cosine readout or physical Newman equation; their raw compatibility does not justify (1), (8) or physical transport for the altered observation. |
| Actual-theta three-profile relaxation | Fractional relaxed masses do not realize the multiplicity-counted divisor of an actual analytic heat field; (8) and integer exterior counts cannot be assigned to them from the relaxed measurements. |

The direct comparator receives all shared source values, geometry, strip
and any future exterior counts. Its existing positive endpoint is already
the interval minimum. This proof pass supplies no stronger gap enclosure
or evaluation-cost advantage. The specific unchanged-matrix Gram proposal
and continuous constant-mode/absolute-remainder proposal fail their stated
tests. A different phase grouping is outside these failures and would
require a new B decision with explicit blocks, signed remainder,
normalization and full-domain payment. E04 r4 and E06 remain unissued.

[request]: ../research-progress/handoffs/VCD-GT-E03-r6.md
[decision]: ../brainstorm/notes/08_VCD_GT_B06_SHARP_MASS_FEASIBILITY_DECISION_20261116.md
[input]: 24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[strip]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[transfer]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[defect]: 05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[class]: ../../../../../avoid/01_restating_the_target.md
[screen]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
