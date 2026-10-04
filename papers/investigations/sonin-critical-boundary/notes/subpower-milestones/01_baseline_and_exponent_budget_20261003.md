# Baseline transfer and the first exponent threshold

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate same-model agents checked the fixed-exponent consequence and
baseline transfer. These are internal checks, not specialist refereeing.

This note gives a precise starting point for the [subpower program](README.md).
It establishes the fixed-exponent equivalence and transfers a stronger
known PNT estimate to the complete variance. No global delta below one
is proved. The first unresolved step is one genuine fixed power saving.

## A fixed exponent is equivalent to a fixed zero strip

Use the existing g, w, p_g, V_g and complete physical caps. For each fixed
delta in [0,1], the following statements are equivalent:

1. \(\mathcal V_g(X)=O(X^{2+\delta})\) for all sufficiently large real X.
2. Every nontrivial zero satisfies \(\Re\rho\le1/2+\delta/2\).

For the forward implication, the exact shell inequalities are

\[
X^2\{J_g(\log(2X))-J_g(\log X)\}
\le\mathcal V_g(X)
\le4X^2\{J_g(\log(2X))-J_g(\log X)\}.
\]

For positive delta, shell summation gives
\(J_g(Y)=O(e^{\delta Y})\). At delta=0 it gives
\(J_g(Y)=O(1+Y)\), not bounded cumulative energy. In either case,
the physical weighted integral J_{g,epsilon} is finite for every
\(\varepsilon>\delta/2\). Its true Laplace transform is holomorphic
on Re s>epsilon and, initially on Re s>1/2, equals

\[
P_g(s)=-G(-s)\frac{\zeta'}{\zeta}(1/2+s),
\]

in the manuscript's plus-exponent convention. The probe's noncancellation
lemma leaves a pole at every zero right of 1/2+epsilon. Varying epsilon
excludes all zeros strictly right of 1/2+delta/2. This does not assert
weighted convergence at the boundary epsilon=delta/2.

Conversely, assume the zero-strip statement only for this direction.
The established pole-inclusive linear explicit formula has coefficients
\(-m_\rho G(1/2-\rho)\). Sixth-power transform decay, uniform across
the critical strip, and N(T)=O(T log T) make their absolute sum finite.
Every nontrivial term is bounded in magnitude by its coefficient times
exp(delta y/2). The trivial-zero contribution is bounded for y at least
one; the original finite arithmetic response controls the initial compact
interval. Thus

\[
|p_g(y)|\le C_g e^{\delta y/2},\qquad
|V_g(x)|\le C_g x^{(1+\delta)/2},\qquad
\mathcal V_g(X)=O_g(X^{2+\delta}).
\]

This allows zeros on the strip boundary. At delta=0 functional-equation
symmetry makes the statement RH. The optimal power frontier consequently
obeys

\[
\inf\{\delta>0:\mathcal V_g(X)=O(X^{2+\delta})\}
=2\sup_\rho(\Re\rho-1/2).
\]

This is an exact translation of the established zero-detection framework,
not new information about zero locations. It explains why even delta=0.99
would be a substantial all-height zero-free theorem. Existing
[height-dependent zero-free regions](https://arxiv.org/abs/2212.06867)
have boundaries approaching 1 as height grows; their direct use supplies
no constant strip of this kind. No exponent-descent rule is presently
established in this project.

## Exact transfer of a known Chebyshev-error envelope

Let A=e^(-1/4), B=e^(1/4), E(t)=psi(t)-t, and

\[
M_w=\int_A^B u|w'(u)|du.
\]

The complete-cap Stieltjes identity from note 09 reads

\[
V_g(x)=-\int_A^B E(xu)w'(u)du.
\]

If an unconditional bound gives \(|E(t)|\le t r(t)\) on the complete
band [AX,2BX], put \(R_X=\sup_{AX\le t\le2BX}r(t)\). Then
\(|V_g(x)|\le xM_wR_X\) on [X,2X], and exactly

\[
\boxed{\mathcal V_g(X)\le\frac73M_w^2X^3R_X^2.}
\]

No monotonicity of r is assumed, no endpoint is omitted, and the constant
7/3 comes from the integral of x squared over the whole shell.

[Johnston and Yang, Theorem 1.4](https://arxiv.org/pdf/2204.01980),
give the unconditional envelope, for t at least 23,

\[
r(t)=0.026(\log t)^{1.801}
\exp\!\left[-0.1853\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}\right].
\]

For every real X at least 23/A, the boxed transfer with this exact
supremum is therefore an unconditional explicit source-dependent bound.
No numerical enclosure of M_w or the supremum has been generated here.
To read its asymptotic strength, let
\(F(X)=(\log X)^{3/5}/(\log\log X)^{1/5}\).
For fixed c in the complete compact interval [A,2B],
F(cX)-F(X) tends to zero uniformly, by the mean value theorem in log X.
The logarithmic prefactor ratio also tends to one uniformly. It follows
that

\[
\boxed{\mathcal V_g(X)=O_g\!\left(
X^3(\log X)^{3.602}e^{-0.3706F(X)}\right).}
\]

This strengthens the square-root-logarithm asymptotic saving previously
used in the project. The envelope need not be tighter on the existing
finite computation range. It is an application of a known PNT theorem, not a
new number-theoretic saving. Its global power remains delta=1:
F(X)=o(log X), and the displayed comparison function is larger than
X^(3-kappa) for every fixed positive kappa at sufficiently large X.
The upper bound does not prove that the actual variance has that larger
growth; it simply supplies no fixed power improvement.

## The first candidate lemma and its exponent budget

Seek a genuinely unconditional estimate for the exact actual-prime
projection or combined signed remainder. A useful candidate has the form

\[
\mathcal V_g(X)\le C\{X^2L(X)+X^{3-\kappa}L(X)\},
\quad \kappa>0,\quad L(X)=X^{o(1)},
\]

for every sufficiently large real X, with all physical caps and any
exceptional-set costs included. Such an estimate proves every
\(\delta>\max(0,1-\kappa)\). It does not automatically give the endpoint
delta=1-kappa when L is unbounded. If kappa is at least one, it gives
all positive delta and therefore RH. This is an open candidate template,
not an estimate obtained here.

The next bounded investigation should choose one actual arithmetic input,
write its full projected estimate, and calculate kappa after every error
is accounted for. Stop that candidate route if it supplies only a
logarithmic or other subpower saving on X cubed, assumes an equivalent
fixed zero strip, or loses the cancellation under absolute summation.
Record useful baseline improvements separately. Further numerical work
should test a specific proposed mechanism; fixed-height verification or
a fitted finite-range slope does not establish a smaller global delta.
