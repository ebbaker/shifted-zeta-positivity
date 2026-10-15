# Review: proper source filters and theta correlations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Independent reviewing agent: **gpt-6-astra (Codex)**; reasoning effort **ultra**,
as recorded by the parent session. This review concerns
[Note 22](../notes/22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md)
and its two bounded numerical experiments. No manuscript change, new height
coverage, or resolution of the positive-time collision problem is certified.

**Assessment.** The prescribed direct-product criterion is valid. The
64-case compact-filter pilot and 14-case complete-source Gaussian pilot
replay successfully. The sharp-endpoint expansion, its obstruction on
genuine high-height stationary sets, and the impossibility of a finite
rational-coefficient jet closure for a nonzero compact source filter are
mathematically sound with the scopes stated below. The constructive Gaussian
identities are exact, but do not establish a uniform signed comparison.

## 1. Direct signed absorption and what it actually implies

Write \(C_j=G_j+R_j\), \(E=h_0^2+h_1^2\), and

\[
\mathcal L_j=\mu h_j^2+h_jC_j
\quad\text{on }h_{j+1}=0,\qquad \mu=a^2+b^2>0.
\]

For a prescribed \(0\le\lambda\le1\), the two estimates

\[
h_jG_j\ge-\alpha_jE,\qquad
h_j(R_j+\lambda G_j)\ge-\beta_jE
\]

give

\[
\mathcal L_j\ge-[(1-\lambda)\alpha_j+\beta_j]E.
\]

Here the displayed expression is simply expansion of

\[
h_jC_j=(1-\lambda)h_jG_j+h_j(R_j+\lambda G_j)
\]

and omission of the nonnegative term \(\mu h_j^2\). The loss remains
locally bounded if the prescribed nonnegative \(\alpha_j,\beta_j\) are
locally bounded. Both pilots prescribe \(\lambda=1/2\) and
\(\alpha_j=\beta_j=K_j=0\) before evaluating the fields. No loss is fitted
from an energy floor or a quotient of jets.

Unlike Note 21's residual-square sufficient condition, these product
conditions do not force \(R_j=0\) merely from \(h_j=0\) and \(E=0\): both
products then vanish irrespective of the residual. This removes that
particular algebraic obstruction, but proving the estimates uniformly
through a candidate collision remains the substantive obligation. The
criterion supplies the earlier stationary estimate if proved; the new
finite tests do not supply such a global proof.

## 2. Proper compact-filter pilot: all 64 classifications reproduced

The inspected and independently rerun driver is
[certify_predetermined_source_filter_pilot.py](../numerics/certify_predetermined_source_filter_pilot.py),
with record
[PREDETERMINED_SOURCE_FILTER_PILOT_20261014.json](../numerics/PREDETERMINED_SOURCE_FILTER_PILOT_20261014.json).
The declared family is \(N\in\{1,2\}\), \(U\in\{1,3/2\}\),

\[
G_j=e^{-ax}\Re\sum_{n\le N}\int_0^U
(u^2-b^2)[i(u+ia)]^j e^{t(u+ia)^2+ixu}\phi_n(u+ia)\,du,
\]

with fixed \(a=\pi/16\), \(b=1/4\). This is a split of the already valid
complete horizontal-contour identity. It does not independently shift an
individual raw theta term and discard its vertical segment.

The 64 cases comprise four filters, two stationary branches, and eight
closed time slabs covering \([0,1/2]\). The branches are genuine and unique:
opposite paid endpoint signs of \(h_1\), together with \(h_2<0\), establish
the branch in \(101<x<102\); opposite endpoint signs of \(h_2\), together
with \(h_3>0\), establish the branch in \(103<x<104\). All assertions hold
for every time in the stated closed slab, rather than at selected samples.

| Prescribed filter | Cases | \(h_jG_j\) | \(h_jR_j\) | \(h_j(R_j+G_j/2)\) |
|---|---:|---|---|---|
| \(N=1, U=1\) or \(3/2\) | 32 | positive | negative | negative |
| \(N=2, U=1\) or \(3/2\) | 32 | positive | negative | positive |

Each filter has 16 cases, split equally between even development slabs and
odd holdout slabs. Every case and failure is retained. The negative
absorption enclosure for \(N=1\) disproves that particular product condition
on a nonempty stationary branch; it does not imply a negative complete
Laguerre form. The \(N=2\) filters exhibit a favorable retained contribution
paying a strictly adverse complementary product, on both stationary sets.

The accounting checks are important:

* The normalization \(e^{\pi x_c/8}\) is constant throughout each cell.
  Physical \(x\) derivatives therefore remain the transported jets.
* Full center jets retain the original complete index and integration-tail
  payments. Filtered centers use fresh validated finite Acb integrals.
  Taking \(R=C-G\) retains every original omitted-source payment.
* The source masks for \(G\), \(R\), and \(R+G/2\) are respectively
  \(\chi_A\), \(1-\chi_A\), and \(1-\chi_A/2\), all of absolute value at
  most one. Each field's Taylor remainder is therefore dominated separately
  by the same complete-source centered moment majorant. Adding a second
  copy merely because \(R\) is represented as a difference is unnecessary.
* The centered payments are the original jet payments combined with
  positive coefficients \(1,2a,\mu\). This dominates the multiplier
  \(u^2-b^2=-q^2-2aq-\mu\) and its higher moments. The stored center-jet
  depth covers every term of the space-order 12, time-order 8 expansion.
* Intersections using \(C_j=-h_{j+2}-\mu h_j\) are taken only on the
  current true stationary set. Whole-cell enclosures and stationary
  restrictions are not confused.
* The filter is fixed in \(t,x\). It obeys the backward heat equation and
  has no moving-cutoff derivative. Its source endpoints remain present in
  integration-by-parts formulas, as discussed below.

The independent 192-bit run used Python 3.10.0 and python-flint 0.9.0 and
completed in about 14 seconds. Its entire parsed record equals the producing
record after removing only `elapsed_seconds`; this includes all interval
endpoints, full center arrays, payments, and branch certificates. The
temporary independent output is
`/private/tmp/inv21-review-proper-filter-pilot.json`; it is replay provenance,
not a required mathematical input or a separate repository artifact.

## 3. Endpoint expansion and obstruction on true stationary points

For fixed \(t>0,a,b,N,U\), let

\[
f_{N,j}(u)=(u^2-b^2)(-a+iu)^j e^{t(u+ia)^2}\Phi_N(u+ia).
\]

Two integrations by parts, for \(x>0\), give

\[
e^{ax}G_j(x)=x^{-1}\Im\{f_{N,j}(U)e^{ixU}-f_{N,j}(0)\}
 +\mathcal E_j(x),
\]

\[
|\mathcal E_j(x)|\le x^{-2}
\left(|f'_{N,j}(U)|+|f'_{N,j}(0)|+
\int_0^U|f''_{N,j}(u)|\,du\right).
\]

The signs and the complete remainder are correct. The lower endpoint is
not generally real for a finite raw-index sum. For the complete theta
source, evenness and reality give \(f_j(-u)=\overline{f_j(u)}\), which
cancels the real part of every lower-endpoint coefficient in the repeated
expansion. A common-\(v\) filter has frequencies \(V-d_n\) and retains each
entry; a zero-length interval contributes zero, not a lone boundary term.

The endpoint nonvanishing claim covering the pilot is proved, not assumed:
at \(a=\pi/16, U\ge1, U\ne b\), the \(n=1\) endpoint dominates the rest.
The bound

\[
\sum_{n\ge2}2n^4e^{-100(n^2-1)}
\le\frac{2e^{-297}}{1-e^{-495}}<\tfrac12
\]

is valid. Thus the endpoint sinusoid is nonconstant for both \(j=0,1\).

The genuine-stationary-sequence argument also checks out. At fixed positive
\(t\), Notes 17 and 19 give

\[
h_k=A\omega^k\{\cos(\varphi+k\pi/2)+O(1/\log x)\},
\quad \varphi'=\omega+O(1),\quad
\log A=-\pi x/8+O_t(\log^2x).
\]

Fixed-width phase windows around \(k\pi\), respectively
\(\pi/2+k\pi\), have opposite endpoint signs of \(h_1\), respectively
\(h_2\), and a strictly signed next derivative. Each window therefore
contains exactly one true stationary point. Adjacent stationary points
have alternating signs of \(h_j\), and their spacing tends to zero.
Every sufficiently late fixed-width sign interval of the endpoint sinusoid
contains points with both signs. On those intervals \(G_j\asymp e^{-ax}/x\),
whereas \(C_j\) is exponentially smaller. Consequently both signs of
\(h_jR_j\) occur on stationary sequences, with

\[
\frac{|h_jR_j|}{E}=\exp\{(\pi/8-a)x+o(x)\}.
\]

For \(j=0\), \(E\asymp A^2\); for \(j=1\),
\(E\asymp A^2\omega^2\). These justify the displayed rate. Division by
\(E\) is only diagnostic here, on the already proved nonvanishing outer
region; it is not used to define a loss.

On the subsequence with \(h_jG_j>0\), every fixed \(\lambda<1\) gives

\[
h_j(R_j+\lambda G_j)=h_jC_j-(1-\lambda)h_jG_j<0
\]

with the same exponential rate relative to \(E\). Thus even the actual
direct-absorption criterion, with this fixed sharp filter, cannot hold at
all heights using a constant, polynomial, or other subexponential separate
budget. This is fully compatible with the certified finite success.

The obstruction does **not** exclude losses merely locally bounded at
each finite point: exponential growth in height is still locally bounded.
It does not address \(x\)-dependent filters, adaptive contours, or times
tending to zero within the unresolved cusp. It does not obstruct the
complete product \(h_jC_j\), where the artificial endpoints cancel exactly.

## 4. Rational finite-jet closure obstruction

For a nonzero fixed compact source filter, an identity

\[
R_j(x)=\sum_{k=0}^{m}r_k(x)h_k(t,x)
\]

with finitely many rational-in-\(x\) coefficients cannot hold even on a
nonempty pole-free open interval. The proof in the note is valid:

1. Clear denominators and use that \(G_j\) and all full jets are entire in
   \(x\), extending the resulting polynomial identity from the interval.
2. Multiply by \(e^{ax}\). The complete jet has Fourier density
   \(\tfrac12(-a+iu)^k e^{t(u+ia)^2}\Phi(u+ia)\), real analytic on all
   of \(\mathbb R\), with rapidly decaying derivatives at both ends.
   The negative-end assertion uses complete theta evenness and conjugation.
3. The compact-filter density is \(f_{N,j}(u)/2\) on \(0<u<U\), its
   Hermitian reflection on \(-U<u<0\), and zero elsewhere. Polynomial
   multiplication in \(x\) differentiates this compact distribution.
4. Fourier injectivity equates a compactly supported distribution with a
   real-analytic function. The latter vanishes on an exterior open interval,
   hence identically. Thus the polynomial times \(G_j\) vanishes, forcing
   \(G_j\equiv0\), a contradiction.

Nonzeroness of \(G_j\) follows from Fourier injectivity and the nonzero
analytic density on a subinterval; the finite theta sum cannot vanish
identically. For coefficients depending on \(t\), the same reasoning
applies with \(t\) frozen. General transcendental or merely locally bounded
coefficients are not ruled out, and quotients away from zeros are not
counterexamples to this specifically rational-coefficient statement.

The related warning about finite symmetrization is correct:
\(\Phi_N(-u)=-3\pi(\sum_{n\le N}n^2)e^{-5u}+O_N(e^{-9u})\).
Multiplication by \(e^{tu^2}\) destroys its integrability for \(t>0\).
Naive finite-index symmetrization therefore does not reproduce the complete
source's positive-time contour symmetry.

## 5. Complete-source Gaussian pilot and transport identities

The tested mask is \(e^{-\delta z^2}\), \(z=u+ia\), with fixed
\(\delta=1/16\). It is complex on the horizontal contour. The complete
even theta source nevertheless gives the exact physical identity

\[
G_j(t,x)=C_j(t-\delta,x),\qquad R_j=C_j(t,x)-G_j(t,x),
\]

with the same fixed \(a,b\). The real-multiplier paired formula in Note 21
cannot be reused unchanged for this complex mask; the physical-field
identity used in the pilot avoids that mistake.

The inspected and independently rerun driver is
[check_gaussian_source_filter_pilot.py](../numerics/check_gaussian_source_filter_pilot.py),
with record
[GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json](../numerics/GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json).
All 14 cases, comprising both current genuine stationary branches and
seven slabs covering \(1/16\le t\le1/2\), certify

\[
h_jG_j>0,\qquad h_jR_j>0,\qquad h_j(R_j+G_j/2)>0.
\]

This test uses the existing complete-source record with exact rational
interval arithmetic; it performs no new quadrature. Prior and current
time cells have the same spatial center, the same constant normalization,
and exactly matched Taylor displacements. Their centered differences are
formed before transport. Remainder payments are current plus prior for
\(R\), and current plus one half of prior for \(R+G/2\). Endpoint and
monotonicity checks establish current stationarity. No stationary
condition is imposed at the earlier time. The independent output
`/private/tmp/inv21-review-gaussian-filter-pilot.json` is byte-identical to
the producing record.

The additional untested real mask \(e^{-\delta u^2}\) has the distinct
exact identity

\[
G_{\delta,j}(t,x)=e^{a^2\delta}C_j(t-\delta,x+2a\delta),
\]

\[
R_{\delta,j}=-\int_0^\delta e^{a^2s}
(C_{j+2}+2aC_{j+1}+a^2C_j)(t-s,x+2as)\,ds.
\]

These follow directly from the exponent identity and the backward heat
equation with fixed \(a,b\). They preserve complete-source boundary
symmetry and are compatible with Note 21's real-multiplier pairing.
Neither identity proves a favorable cross-time sign. Fixed-time carrier
phase separation also cautions against extrapolating the bounded Gaussian
pilot into a uniform all-height result. No numerical certificate for this
second, real-mask variant is claimed.

For the tested complex mask, the integrated note's additional formula
\[
R_j(t,x)=-\int_0^\delta C_{j+2}(t-s,x)\,ds
\]
has the correct sign: \(\partial_s C_j(t-s,x)=C_{j+2}(t-s,x)\).
The definitions of \(C_k\) extend to every needed order. The integrated
conditions (S1)–(S4) agree with the reviewed source identities and impose
stationarity only at the current time.

## 6. Replay identity and remaining trust boundary

Reviewed artifact hashes, SHA-256:

| Artifact | Hash |
|---|---|
| Final integrated Note 22 | f1ee2c3703d584b89f6a4d500a067e72b97cdbcd79182f1b058097c3ada65f9c |
| Proper-filter driver | `8adb74737c9a3f6ff7a76db72753c87fd415dab4e033c3a22890a8fc7afc1c8d` |
| Proper-filter producing record | `18bf6465e1fc04e5ed590a578976594d693e9d49ba732595e1b4123665a9c13e` |
| Proper-filter independent record | `3790637bbff0c2a2598d0240b7ce7ac20adfce8c46ef406f671bf5a17b52e353` |
| Gaussian driver | `1eec7358608a6ee687f2bdfd0b85920c24d10a12a3045c15c42645dfe213358d` |
| Gaussian producing and independent record | `e00a6e40c76395b711dc2ec7510e4db52296945affaf482e5fcd0fa8cf7367e0` |
| Complete input record | `aee1f000150a90e1269faa9a8cfafa6251d581ec0f586f0b09d554ef8822741d` |
| Complete input driver | `6da9b9c05b465a0067809f9e11bb7d7414f51330afe91c2c38e7cb02fc939afb` |
| Imported contour source | `b6f0114e1a4de2e1848f20ab0ab2f1022d9b55015184a879ae0c0536a62d6ad6` |

The final integration was reread, including (S1)–(S4), both pilot tables,
and the references between the compact and Gaussian sections. A further
234 exact rational comparisons verify every advertised conservative
endpoint and product margin in the integrated tables against the stored
receipts. The installed drivers and records match the reviewed hashes.
The opening summary was narrowed to distinguish the sharp-rectangular
endpoint theorem from the more general compact-filter rational-closure
obstruction. No substantive regression or outstanding correction remains.

Hash agreement establishes the reviewed and replayed objects, not the truth
of a theorem. The original complete-source quadrature, contour and tail
lemmas, and the numerical libraries remain trusted inputs; this review is
an independent mathematical and implementation audit, not formal proof
verification. The new finite computations retain all signed integrated
cross terms and pay all inherited errors. Their structural value is to
distinguish a successful signed mechanism from a nearby failing one, while
the analytic obstructions identify why fixed compact filters cannot simply
be promoted to a global argument.
