# One-sided arithmetic investigation: density elimination and the remaining correlation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Internal analytical work and
same-model cross-review, not independent specialist refereeing. No new
global prime-variance exponent or mathematical priority is claimed.

## Outcome

The next target from the [signed covariance continuation](SIGNED_COVARIANCE_CONTINUATION_20261004.md)
has now been investigated: prove either one-sided power bound for the
complete centered arithmetic scalar. That inequality remains open.
There are three concrete deductions from the attempt:

1. The continuous prime-density term cancels the entire explicit
   continuum, with a proved power-small lattice remainder. An independent
   estimate for the reciprocal Möbius sum is unnecessary at this step.
2. Shell averaging gains a derivative, permitting a slightly larger
   balanced cutoff and therefore a narrower range of retained factors.
3. Actual smooth arithmetic coefficients defeat literal sign deletion,
   even after grouping equal products and retaining the exact continuum.
   Real-axis transform positivity and fixed positive kernel averaging
   also fail to supply the missing inequality.

The resulting target is one signed correlation with the normalized
prime-counting error. Known PNT input bounds it to every logarithmic
order, which is insufficient for any fixed positive exponent.

## 1. An unconditional elimination inside the complete scalar

Use the fixed probe, with A=e^(−1/4), B=e^(1/4), C=2B, q=7/3, and

\[
\ell(v)=\int_1^2y w(v/y)\,dy,\qquad
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),\qquad
M_1(U)=\sum_{d\le U}\frac{\mu(d)}d.
\]

The ordinary moment of ell is zero and its logarithmic moment is
q c_w, with the fixed nonzero c_w<0. For real U>=1 with U²<=AX, set

\[
J_0(X;U)=c_wM_1(U)+\frac1{qX}
\sum_{m>U}\sum_{p>U}A_U(m)(\log p)\ell(mp/X),
\qquad E(t)=\theta(t)-t.
\tag{1}
\]

Here p denotes a prime; all product caps come from the exact support.
The [centering derivation](PRIME_DISCREPANCY_CENTERING_20261004.md)
uses H(v)=int_v^infinity ell and f(v)=H(v)/v. Both are supported on
[A,C], and int f=q c_w. The full density contribution is

\[
\frac1q\sum_{m>U}\frac{A_U(m)}m H(mU/X)
=-c_wM_1(U)+O_w((U^2/X)^8).
\tag{2}
\]

This is a signed cancellation before any estimate of M_1. The two gained
derivatives, from shell averaging and integration, give a finite measure
D^8 f and the eighth-order lattice remainder. No infinite smoothness is
assumed for the fixed probe.

Stieltjes integration by parts must retain the boundary E(U), using its
right-continuous value when U itself is prime. Summing that boundary
costs O_w((U²/X)^7). With epsilon(t)=E(t)/t, define

\[
\mathcal I(X;U)=\sum_{U<m<CX/U}\frac{A_U(m)}m
\int_{mU/X}^{C}\varepsilon(Xv/m)\,v\ell'(v)\,dv.
\tag{3}
\]

The complete result is

\[
\boxed{J_0(X;U)=-\frac1q\mathcal I(X;U)
+O_w((U^2/X)^7+(U^2/X)^8).}
\tag{4}
\]

At U=X^(11/24), the density remainder is O(X^(−2/3)) and the
boundary is O(X^(−7/12)). The terminal intervals m>AX/U retain the
lower limit mU/X in (3). Dropping that limit changes the functional.

For every fixed 0<kappa<11/24, either inequality

\[
\mathcal I(X;X^{11/24})\ge-KX^{-\kappa/2}
\quad\hbox{or}\quad
\mathcal I(X;X^{11/24})\le KX^{-\kappa/2}
\tag{5}
\]

on all sufficiently large real X would separately imply the exact
variance estimate O(X^(3−kappa)). This uses the already-proved scalar
detector and the affordable inner-prime-power error; it does not prove
(5). The sign reverses in (4). Envelopes with subpower losses suffice
as in the earlier scalar criterion.

## 2. A sharper cutoff budget for this scalar

Because D^7 ell is a finite measure, direct scalar Vaughan comparison
has error

\[
O_w\!\left(X^{-7}\{U^7(1+\log X)+(UV)^7\}\right).
\tag{6}
\]

Thus fixed positive exponents U=X^u,V=X^v need only satisfy
u+v<=1−kappa/14 to preserve the target scalar scale. Balanced cutoffs
can be set to

\[
U=V=X^{1/2-\kappa/28}.
\tag{7}
\]

This improves the scalar comparison only; it is not a strengthened
energy approximation. For these cutoffs the density error in (2) is
O(X^(−4 kappa/7)), the boundary error is O(X^(−kappa/2)), and the
inner-prime-power error O(U^(−1/2) log X) is smaller when
0<kappa<14/29. Either version of (5), with cutoff (7), therefore
remains a sufficient and equivalent first-saving target in that range.

For the concrete illustrative target kappa=0.01, take
U=X^(1399/2800). The retained factors range from U to C X/U, whose
ratio is C X^(1/1400). The outstanding one-sided bound is
I(X;U)>=−K X^(−1/200), or its opposite-sign counterpart. The lower-cutoff
boundary error is allowed at that same scale; no little-o estimate for
it is needed. The first global saving has not been obtained.

## 3. Routes tested and their failure points

The [arithmetic sign test](SIEVE_SIGN_TEST_20261004.md) constructs
actual smooth outer products m=q_1 q_2 with q_j of size X^(1/4),
paired with a unique retained inner prime p of size X^(1/2).
Their coefficient A_U(m)=1, and fixed-ratio prime boxes land inside
either lobe of ell. After grouping every representation of each
integer, the positive and negative scalar masses P_X,N_X each obey

\[
P_X,N_X\gg(\log X)^{-2},\qquad
J_0=c_wM_1(U)+P_X-N_X.
\tag{8}
\]

Outer products of three primes also exhibit the opposite arithmetic
sign. Classical PNT gives J_0=O_M((log X)^(−M)) for every fixed M.
Consequently the literal upper majorant c_wM_1+P_X is at least a
positive multiple of (log X)^(−2), and the corresponding lower
minorant c_wM_1−N_X is at most a negative multiple of that size.
Neither reaches a fixed power. This obstruction applies to the new
cutoff (7) as well. It excludes those specific sign-discarding methods,
not all sieve arguments or methods that preserve signed comparisons.

The [analytic sign tests](ONE_SIDED_SIGN_GATE_20261004.md) establish
that a hypothetical zero rho=beta+i gamma with beta>1/2 forces both
signs of the exact scalar at scale X^(beta−1), with lower amplitude
m_rho |D(rho)|>0. The proof needs no rightmost zero. A positive
transform on the real axis does not suppress those nonreal poles.
Fixed positive logarithmic averaging retains a sign-changing prepared
kernel; filters that cancel a forbidden pole lose that detector unless
another filter covers it. A strictly larger fixed pointwise kernel
majorant introduces positive prime-density mass and cannot yield a
decaying upper bound.

## 4. The remaining research target

The most direct next calculation is the correlation of E(t) with the
aggregated arithmetic kernel, before taking absolute values. Reversing
the finite sum and integral in (3) gives exactly

\[
\mathcal I(X;U)=\int_U^{CX/U} E(t)\,\mathcal K_{X,U}(t)\,dt,
\qquad
\mathcal K_{X,U}(t)=\frac1{X^2}
\sum_{m>U}m A_U(m)\ell'(mt/X).
\tag{9}
\]

The support of ell' enforces the full product cap in the inner sum.
At the illustrative cutoff (7), it is specifically one sign of this
complete correlation that needs a bound K X^(−1/200). A useful
dispersion or sieve decomposition must retain its cross terms, its
terminal intervals, and the signs in A_U. Bounding E or the Möbius
coefficients separately by stronger fixed-power hypotheses would merely
move the global zero-strip obligation into an input.

Applying the available PNT envelope and sum |A_U(m)|/m=O(log²X)
gives every fixed logarithmic saving for (3), but no fixed power.
There is currently no proved contraction of (9) at the required scale.
That is the precise unresolved step after this investigation.

## Verification

Separate same-model agents cross-reviewed the centering and analytic
sign arguments, and the coordinating agent checked the arithmetic box
construction and coefficient bookkeeping. The two new exact checkers
passed 81,429 comparisons: 81,043 finite arithmetic identities and 386
rational centering/endpoint comparisons. The endpoint checker detects
the deliberately omitted boundary in 28 of its 32 synthetic cases.
Its polynomial kernel and rational prime weights test identities, not
the fixed-probe derivative constants or an asymptotic bound.

See the [review record](../../../reviews/01_signed_arithmetic_covariance/ONE_SIDED_ATTEMPT_REVIEW_20261004.md)
and [reproduction package](../../../numerics/01_signed_arithmetic_covariance/README.md).
No manuscript source, outward certificate, or compilation record is
changed by this investigation.
