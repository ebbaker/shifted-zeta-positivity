# Signed covariance continuation: one scalar target and compulsory cross cancellation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Three parallel research
contributions and coordinating cross-checks are internal same-model work,
not independent specialist refereeing. No new fixed global exponent or
mathematical priority is claimed.

## Outcome

This continuation makes three substantive advances to the previous plan.

1. **The complete scalar mismatch alone suffices globally.** For the
   actual fixed arithmetic response, even an eventual bound on one sign
   of that scalar is equivalent to the desired variance exponent. A
   second independent projected-Gram estimate is unnecessary once the
   all-real-shell scalar bound is proved.
2. **A concrete actual-arithmetic obstruction rules out sectorwise bounds.**
   The prime-inner Vaughan response splits exactly into semiprimes and
   a signed smooth-cofactor sector. The semiprime sector has raw energy
   of order X³/log²X and projected energy of order X³/log⁴X. Both exceed
   every fixed-saving budget. Their cancellation with the other sector
   is compulsory, not merely a desirable numerical feature.
3. **Cutoffs can be adapted to the intended saving.** Exact cutoff-annulus
   identities permit UV<=X^(1−kappa/12); the corresponding cofactor and
   outer Mellin powers are kappa/12. Averaging admissible cutoffs preserves
   the same unresolved response and provides no contraction by itself.

The first item sharpens the next target. The second rejects a tempting
way of estimating it. The third supplies more flexible coordinates.
None establishes the missing arithmetic inequality.

## 1. The revised minimal arithmetic target

Set q=7/3, U=V=X^(11/24), and retain every cap in

\[
\ell(u)=\int_1^2y w(u/y)\,dy,\qquad
J(X)=c_wM_1(U)+\frac1{qX}
\sum_{m>U,n>U}A_U(m)\Lambda(n)\ell(mn/X).
\tag{1}
\]

Here A_U(m)=sum_{d|m,d>U}mu(d), M_1(U)=sum_{d<=U}mu(d)/d,
and ell is supported on [A,2B]. The continuum c_w M_1(U) is part of
the signed expression. Cutoffs remain fixed as the shell variable varies.

The [scalar-detector proof](SCALAR_DETECTOR_20261004.md) establishes that,
for every fixed 0<=kappa<=1, each of the following **separately** is
equivalent to the exact variance bound O(X^(3−kappa)):

\[
|J(X)|\ll X^{-\kappa/2},\qquad
J(X)\le C X^{-\kappa/2},\qquad
J(X)\ge-C X^{-\kappa/2}.
\tag{2}
\]

Each estimate must hold for every sufficiently large real X with one
fixed exponent. Either one-sided condition with a subpower loss also
suffices, through an intersection of closed strips and the inherited
endpoint theorem. Neither one-sided inequality has been proved here.

The reason is arithmetic, not a generic projection bound. With
lambda_V=<V_g,x>/(qX³) and S(X)=X lambda_V(X), the full Mellin transform
is

\[
\int_0^\infty S(X)X^{-z-1}dX
=-\frac{G(1/2-z)}q\frac{2^{z+2}-1}{z+2}
\frac{\zeta'}{\zeta}(z),\qquad \Re z>1.
\tag{3}
\]

The averaging factor has zeros only on Re z=−2. It cannot hide any
forbidden zero. Preparation cancels the pole at one, and a zero of any
multiplicity leaves a simple nonzero residue. A true one-sided transform
has an explicitly retained entire initial cap from n=2. The Landau
nonnegative-tail argument turns either hypothetical sign bound into
holomorphy in the required half-plane, without assuming a rightmost zero.

The parent Vaughan norm error gives |J−lambda_V|=O(X^−1/2), so the
criterion transfers to (1), including the kappa=1 endpoint. It does not
apply to arbitrary responses: x sin(x²) has scalar O(X^−2) and cubic
energy. It also does not turn a finite collection of sampled scalars into
a global bound.

This corrects the logical role of the earlier two-piece requirement.
The projected/scalar identity is still exact on each shell, but its two
global bounds are not independent for this actual arithmetic response.

## 2. An exact arithmetic reduction inside the target

The [overlap investigation](ARITHMETIC_OVERLAP_20261004.md) proves

\[
\|B^{\rm pp}\|_2^2\ll X^{61/24}(\log X)^2,
\tag{4}
\]

where B-pp contains inner higher prime powers in the Vaughan convolution.
This is a new estimate for that convolution sector, not an application of
the easier original-response prime-power estimate. It permits removal of
inner higher prime powers for every fixed 0<kappa<11/24. In that range,
(2) remains equivalent with

\[
J_0(X)=c_wM_1(U)+\frac1{qX}
\sum_{p>U}(\log p)\sum_{m>U}A_U(m)\ell(mp/X).
\tag{5}
\]

Indeed |J_0−lambda_V|=O(X^−1/2)+O(X^−11/48 log X), which is
o(X^−kappa/2). This gives a simpler exact prime-inner target for the
illustrative saving kappa=0.01, retaining the whole signed sum.

The arithmetic support is sharper than a generic divisor-bound class.
If a retained outer factor m=qg contains a prime q>U, then the balanced
caps give g<U<q. Therefore

\[
A_U(qg)=-\sum_{d\mid g}\mu(d)=-\mathbf1_{g=1}.
\tag{6}
\]

As a result the prime-inner response is exactly S_X+F_X, where

\[
S_X(x)=-\sum_{p,q>U}(\log p)w(pq/x),
\]
\[
F_X(x)=\sum_{\substack{m>U\\P^+(m)\le U}}A_U(m)
\sum_{p>U}(\log p)w(mp/x).
\tag{7}
\]

The semiprime sum is ordered, including prime squares with their correct
weight. The other outer factors are U-smooth; their A_U coefficients
retain their signs and strict divisor cutoff. Equation (5) is precisely
J_0=c_wM_1(U)+lambda(S_X)+lambda(F_X).

## 3. What the overlap calculation eliminates, and what survives

In the full projected covariance, distinct inner primes with identical
products obey pm=qn. Equation (6) kills every nontrivial common cofactor,
leaving only the explicit semiprime collisions. Those collisions cost
O(X^(2+o(1))). Repeated inner-prime channels cost
O(X^(61/24)log³X). An absolute product band |r−s|<=X^(1−kappa)
costs O(X^(3−kappa+o(1))). All statements preserve the full product caps
and the rank-one projection subtraction. They bound portions of a signed
quadratic form, not independent response vectors that can be deleted.

These are genuine affordable arithmetic sectors. The unresolved covariance
lies in separated products and distinct inner primes, with their actual
Möbius signs. The scalar criterion allows this covariance to be treated
as a possible mechanism for a one-sign bound, instead of demanding a
second global theorem about the Gram matrix.

The semiprime obstruction makes the needed cancellation particularly clear.
Let L=log X, d=13/24, c_1=c_w, and c_2=int w(t)(log t)²dt. Classical
quantitative PNT, with both lower cutoff boundaries retained, gives

\[
S_X(x)=-\frac{c_1x}{dL}
+\frac{x}{d^2L^2}\left(c_1\log(x/X)+\frac{c_2}{2}\right)
+O_w(X/L^3),\quad X\le x\le2X.
\tag{8}
\]

Thus ||S_X||² is asymptotic to a positive constant times X³/L².
Projection off x removes the first term but leaves a nonconstant
x log(x/X) component; its energy is asymptotic to a positive constant
times X³/L⁴. These calculations use the ordinary logarithmic-quality
PNT supplied by the [primary source](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/),
not a power-saving prime estimate.

Consequently neither separate raw-sector bounds nor separate projected
sector bounds can meet a fixed power target. Keeping a finite number of
terms of (8) does not fix this: any remaining fixed logarithmic power
still exceeds the target. Even the complete continuous semiprime model
has a PNT replacement error that has not been bounded at fixed power.
The exact discrete semiprime sum in (7) must remain in the current target.

The cancellation is also known unconditionally at logarithmic resolution.
For every fixed M, classical PNT and the proved discarded-sector bounds give
F_X+c_wM_1(U)x=−S_X+O_M(X/log^M X), uniformly on the shell. Consequently
the two-sector Gram matrix, divided by ||S_X||², tends to
\(\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\).
The same holds after projection, with denominator ||PS_X||². This is an
actual arithmetic anticorrelation law. Its subpower remainder does not
yield a fixed kappa, and the known PNT input already explains it.

## 4. Cutoff transport: useful flexibility, no averaging shortcut

The [cutoff-transport proof](CUTOFF_TRANSPORT_20261004.md) derives exact
U-annulus, V-annulus and mixed-rectangle identities. The U transport
cancels its explicit log-density term against c_w x Delta M_1(U).
The V transport includes a prime-response annulus that vanishes only
under the stated support condition V<AX.

For fixed positive u,v with u+v<=1−kappa/12, cutoffs U=X^u,V=X^v
give norm error O(X^((3−kappa)/2)). Hence one can study the same scalar
criterion using balanced cutoffs

\[
U=V=X^{1/2-\kappa/24}.
\tag{9}
\]

For kappa=0.01, both factors then lie between powers 1199/2400 and
1201/2400, up to the fixed upper support constant. Cofactor and outer
Mellin powers can likewise be reduced to 1/1200, with logarithmic
adjustments keeping the discarded error inside the exact target budget.
All fixed nonzero frequencies eventually remain.

These narrower coordinates do not themselves improve an arithmetic
estimate. If T_j=V_g+e_j with ||e_j||<=E, convex cutoff averaging obeys

\[
\sum_jp_j\|T_j\|^2-\left\|\sum_jp_jT_j\right\|^2
=\sum_jp_j\|e_j\|^2-\left\|\sum_jp_je_j\right\|^2\le E^2.
\tag{10}
\]

At the original quadratic-error cutoffs, such averaging removes at most
O(X²) from a possibly larger common energy. Sum-zero combinations remove
the target itself. Moving to an empty Type II range exits the affordable
cutoff region. A new estimate for an average could help, but the transport
identity does not supply one.

## 5. Numerical checks and decision

The [numerical package](../../../numerics/01_signed_arithmetic_covariance/README.md)
contains an exact cutoff checker and a small sector diagnostic. The checker
passed 57,600 integer prime-log coefficient comparisons and 50 rational
centering checks. Four sector runs at X=10000.5 and 100000.25, with
128/256 quadrature nodes, verified the full capped decomposition and
orthogonal energy split. The maximum listed normalized-energy refinement
change was below 3.51e-8. These floating runs are not interval certificates.

The sampled semiprime scalars have the opposite sign to their eventual
positive leading term in (8). Finite fluctuations still dominate the
small logarithmic moment of this probe. The runs therefore provide no
empirical verification of the asymptotic cancellation, and no fitted
exponent or larger sweep is justified by them.

The preferred next analytic target is **one sign of the complete J_0 in
(5)**, keeping both sectors in (7) and the continuum together. With the
illustrative budget kappa=0.01, it is enough to prove

\[
J_0(X)\le C_\varepsilon X^{-0.005+\varepsilon}
\quad\text{for every }\varepsilon>0
\text{ and all sufficiently large real }X,
\tag{11}
\]

or the corresponding lower bound. Its strength is exactly the requested
fixed-strip strength; it is open. The next useful mechanism must control
this signed scalar beyond the known logarithmic cancellations. Separate
sector bounds and cutoff averaging, now explicitly tested, should be
retired as standalone mechanisms. The [internal review](../../../reviews/01_signed_arithmetic_covariance/CONTINUATION_REVIEW_20261004.md)
records checks and limitations.
