# Large-prime overlap and the compulsory semiprime cancellation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Internal derivations, with
classical input identified below; no new global prime-variance exponent.

## Result

There is a useful actual-arithmetic refinement of the balanced Vaughan
response. For the first-saving budget, inner higher prime powers can be
removed at a proved cost. The remaining coefficient vanishes whenever its
cofactor contains a large prime and another factor. Consequently the exact
prime-inner response splits into a negative weighted semiprime sum and a
signed sum with a smooth cofactor.

This split proves a concrete obstruction to termwise estimates. The
semiprime sector alone has energy asymptotic to a nonzero constant times
\(X^3/(\log X)^2\). Even after the prescribed projection onto the
orthogonal complement of \(x\), its energy is asymptotic to a nonzero
constant times \(X^3/(\log X)^4\). Both exceed every fixed-saving budget.
Thus the smooth-cofactor/semiprime cross term is compulsory, including
after projection. This is an obstruction for the actual arithmetic
coefficients, not merely a generic balanced-coefficient countermodel.

Repeated inner primes, exact product collisions, and a thin product
diagonal can nevertheless be bounded below the cubic scale. The unresolved
estimate is located in distinct-prime, distinct-product signed covariance,
combined with the scalar mismatch.

## 1. Scope, notation and exact projection

Use the fixed probe, \(A,B,w,c_w\) and the [proved Vaughan reduction](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).
In particular \(\int w=0\) and \(c_w=\int w(t)\log t\,dt<0\).
Throughout

\[
u=11/24,\quad U=V=X^u,\quad N=2BX,\quad
K=N/U^2=2BX^{1/12},\qquad I_X=\mathbb Z\cap[AX,N].
\]

All statements concern every sufficiently large real \(X\), with \(U\)
held fixed throughout \(x\in[X,2X]\). In particular we require
\(N/U<U^2\), equivalently \(K<U\); this holds eventually since
\(u>1/3\). No assertion requires integral \(X\) or integral \(U\).
Every cutoff below is strict where displayed, including when \(U\) is an
integer. Every product is restricted to \(I_X\); zero endpoint values of
\(w\) cause no ambiguity.

Set

\[
\Omega(s,t)=\int_1^2w(s/y)w(t/y)\,dy,\qquad
\ell(s)=\int_1^2y w(s/y)\,dy,\qquad q_0=7/3,
\]
\[
H(s,t)=\Omega(s,t)-\ell(s)\ell(t)/q_0.
\]

For any real finitely supported coefficient \(b\), let
\(R_b(x)=\sum_{r\in I_X}b(r)w(r/x)\), and write \(P\) for
orthogonal projection off \(x\) in \(L^2(X,2X)\). Then, exactly,

\[
\|PR_b\|_2^2=X\sum_{r,s\in I_X}b(r)b(s)H(r/X,s/X),\qquad
\lambda_b=\frac{\langle R_b,x\rangle}{\|x\|_2^2}
=\frac1{q_0X}\sum_rb(r)\ell(r/X).                                      \tag{1}
\]

Hence \(\|R_b+cx\|_2^2=\|PR_b\|_2^2+q_0X^3(c+\lambda_b)^2\).
The kernel is positive as a quadratic form, not entrywise positive. It
includes every physical frequency. No low-frequency term is omitted.

## 2. Inner higher prime powers have a sufficient weak-target budget

Split the exact Vaughan response as

\[
B_{U,U}=B^{\rm pr}+B^{\rm pp},\qquad
B^{\rm pr}(x)=\sum_{p>U}(\log p)\sum_{m>U}A_U(m)w(mp/x),
\]
\[
B^{\rm pp}(x)=\sum_{\substack{n=p^j>U\\j\ge2}}
(\log p)\sum_{m>U}A_U(m)w(mn/x).
\]

All prime symbols denote primes, and product caps are implicit only through
the explicitly specified \(I_X\). The elementary bound
\(|A_U(m)|\le\tau(m)\) and \(\sum_{m\le Y}\tau(m)\ll Y\log(2Y)\)
give

\[
|B^{\rm pp}(x)|\ll_w X\log X
\sum_{\substack{U<n\le N/U\\n=p^j,\ j\ge2}}\frac{\Lambda(n)}n.
\]

Chebyshev's bound gives
\(\Theta_{\rm pp}(z)=\sum_{p^j\le z,j\ge2}\log p\ll\sqrt z\):
the square term is \(O(\sqrt z)\), and the other powers total
\(O(z^{1/3}\log(2z))=O(\sqrt z)\). Partial summation therefore bounds
the displayed reciprocal tail by \(O(U^{-1/2})\). Thus

\[
\boxed{\quad
\|B^{\rm pp}\|_2\ll_w X^{3/2}U^{-1/2}\log X
=X^{61/48}O_w(\log X),\qquad
\|B^{\rm pp}\|_2^2\ll_w X^{61/24}(\log X)^2.
\quad}                                                               \tag{2}
\]

This is weaker than a quadratic-energy error, but adequate for every fixed
\(0<\kappa<11/24\), including the planning budget \(\kappa=0.01\).
For those exponents the centered prime-inner response
\(B^{\rm pr}+c_wM_1(U)x\) and the original response have the same
\(O(X^{3-\kappa})\) target by the triangle inequality and the parent
\(O(X)\) norm error. At \(\kappa=11/24\), (2) retains a logarithm;
the subpower formulation is still valid. No estimate for prime powers in
the original prime response has been substituted for this convolution
estimate. Projection and scalar-slope errors also obey
\(\|PB^{\rm pp}\|\le\|B^{\rm pp}\|\) and
\(|\lambda_{\rm pp}|\ll X^{-11/48}\log X\).

## 3. An exact large-prime vanishing identity

Suppose \(U<m\le N/U\) and a prime \(q>U\) divides \(m\). Write
\(m=qg\). Then \(g\le N/U^2=K<U<q\). A divisor of \(g\) is
at most \(U\), whereas every divisor \(qe\), \(e\mid g\), exceeds
\(U\). Since \(q\nmid g\),

\[
\boxed{\quad A_U(qg)=\sum_{e\mid g}\mu(qe)
=-\sum_{e\mid g}\mu(e)=-\mathbf1_{g=1}.\quad}                  \tag{3}
\]

This uses the full divisor identity and its actual signs. It remains true
with repeated prime factors in \(g\). Consequently

\[
B^{\rm pr}=S_X+F_X,
\]
\[
S_X(x)=-\sum_{p,q>U}(\log p)w(pq/x),\qquad
F_X(x)=\sum_{\substack{m>U\\P^+(m)\le U}}A_U(m)
\sum_{p>U}(\log p)w(mp/x).                                      \tag{4}
\]

The \((p,q)\) sum is ordered. Its coefficient at distinct-prime
\(r=pq\) is \(-\log r\), and at \(r=p^2\) is \(-\log p\).
All products with two primes above \(U\) and a further nontrivial
cofactor have zero prime-inner coefficient by (3). In the smooth sector
there is at most one prime above \(U\) in each product.

The remaining coefficient still has the exact small-cofactor form

\[
A_U(m)=\sum_{\substack{k\mid m\\k<m/U}}\mu(m/k),\qquad m/U\le K.
                                                                    \tag{5}
\]

For squarefree \(m\), this equals
\(\mu(m)\sum_{k\mid m,k<m/U}\mu(k)\). Formula (5) does not give a
sign to the smooth sector. Removing its cutoff or replacing it by a
positive divisor norm would discard the relation being investigated.

## 4. Full signed covariance and exact collisions

Expanding the coefficient, the prime-inner projected energy is exactly

\[
X\!\sum_{\substack{d,e>U;\ k,l\ge1;\ p,q>U\\
dkp,elq\in I_X}}
\mu(d)\mu(e)(\log p)(\log q)
H(dkp/X,elq/X).                                                 \tag{6}
\]

Here \(k,l\le K\), but their terminal bands are retained through the
two product conditions. The scalar in (1) uses the identical signed
coefficient and must be combined with \(c_wM_1(U)\).

One can expose common divisor overlap by writing
\(d=ha,e=hb,(a,b)=1\). Only squarefree pairwise-coprime \(h,a,b\)
survive, and
\(\mu(d)\mu(e)=\mu(h)^2\mu(a)\mu(b)\). The complete conditions
are \(ha>U,hb>U,hakp,hblq\in I_X\). The positive factor
\(\mu(h)^2\) does not make this a positive-entry sum: both
\(\mu(a)\mu(b)\) and \(H\) retain signs.

There is stronger rigidity on the exact product diagonal. For distinct
inner primes \(p\ne q\), the equation \(pm=qn\) forces
\(m=qg,n=pg\), with \(g\le K<U\). Identity (3) kills every
\(g>1\). Therefore the entire distinct-prime coincident-product part
of (6) is

\[
X\sum_{\substack{p\ne q>U\\pq\in I_X}}
(\log p)(\log q)H(pq/X,pq/X).                                  \tag{7}
\]

It is nonnegative because diagonal values of a Gram kernel are
nonnegative. Its absolute size is \(O(X^{2+o(1)})\), using the
elementary divisor bound for the number/weight of factorizations. This
identifies an actual arithmetic cancellation, but on a sector already
affordable at the target scale.

Two other affordable sectors help locate the remaining obligation:

* **Repeated inner prime.** Let
  \(R_p=(\log p)\sum_{m>U}A_U(m)w(mp/x)\). Then
  \(\|PR_p\|\le\|R_p\|\ll X^{3/2}(\log X)(\log p)/p\).
  Chebyshev and partial summation give
  \(\sum_{p>U}(\log p)^2/p^2\ll (\log U)/U\), whence
  \[
  \sum_{p>U}\|PR_p\|_2^2\ll X^3U^{-1}(\log X)^3
  =X^{61/24}O((\log X)^3).                                    \tag{8}
  \]
  Every off-product interaction within a fixed prime channel is included.
* **Near products.** Write
  \(b(r)=\sum_{pm=r,p>U,m>U}A_U(m)\log p\). Uniformly on
  \(I_X\), \(|b(r)|\le d_3(r)\log r=X^{o(1)}\). Since \(H\)
  is bounded, the absolute sum of the terms with \(|r-s|\le h\)
  in (1) is \(O(X^{2+o(1)}(h+1))\). Thus
  \(h=X^{1-\kappa}\) is affordable at the subpower target. The same
  estimate holds before signed divisor cancellation by using the product
  coefficient with \(|\mu|\).

These statements bound specified contributions to a quadratic form.
They do not delete a response vector, and the complement need not be
positive. In particular they do not authorize applying separate positive
matrix bounds to the remaining cross terms. The rank-one subtraction in
\(H\) is present even where physical \(\Omega\) vanishes.

## 5. The actual semiprime sector defeats termwise power bounds

The classical quantitative PNT suffices for the following calculation;
no power-saving PNT is used. The input is
\(\theta(t)=t+O_M(t/(\log t)^M)\) and
\(\pi(t)=\operatorname{li}(t)+O_M(t/(\log t)^M)\) for every fixed
\(M\). These follow from [Tao, Notes 2, Corollary 39 and Exercise 40](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/),
whose stated classical exponential error is stronger. Only this
unconditional classical input is imported; the calculation below is a
new internal derivation.

Replace first the weighted prime measure in
\(-\sum_{q>U}\int_{(U,\infty)}w(tq/x)\,d\theta(t)\), and then
the remaining prime measure, by their PNT densities. Partial summation
retains the lower endpoint at \(U\). All sampled variables lie between
\(U\) and \(N/U\), so their logarithms are comparable to \(\log X\).
The derivative total variation of each fixed smooth weight, together with
the elementary harmonic bounds, shows that for every fixed \(M\),
uniformly for \(x\in[X,2X]\),

\[
S_X(x)=-\int_{q>U}\frac{dq}{\log q}\int_{p>U}w(pq/x)\,dp
 +O_{M,w}(X/(\log X)^M).                                       \tag{9}
\]

For clarity, the first replacement has error
\(O_M((X/q)(\log X)^{-M})\) for each \(q\); summing contributes
at most one logarithm, absorbed by choosing the input exponent larger.
For the second replacement, the weight is
\(f(q)=(x/q)\int_{Uq/x}^{\infty}w(t)\,dt\), with
\(|f(q)|\ll X/q\) and \(|f'(q)|\ll X/q^2\). Integration
against the PNT error is again \(O_M(X(\log X)^{-M})\) after
increasing the input exponent. These arguments include jumps at the
strict lower cutoffs and the final partial product bands. No prime-square
diagonal is removed from the ordered sum.
Indeed \(\int w=0\) makes \(f(q)=0\) when \(q\le Ax/U\), so
the second density replacement is supported entirely in
\([Ax/U,Bx/U]\), a fixed-ratio polynomial-size band.

For large \(X\), \(AX>U^2\). Change variables \(r=pq\) in (9):

\[
\boxed{\quad
S_X(x)=-x\int_A^B w(t)
\log\left(\frac{\log(xt/U)}{\log U}\right)dt
 +O_{M,w}(X/(\log X)^M).\quad}                                \tag{10}
\]

Let \(L=\log X,d=1-u=13/24,y=x/X\), and
\(c_j=\int_A^B w(t)(\log t)^jdt\), so \(c_1=c_w\ne0\).
Uniform Taylor expansion of
\(\log[(dL+\log y+\log t)/(uL)]\) and \(\int w=0\) gives

\[
S_X(x)=-\frac{c_1x}{dL}
 +\frac{x}{d^2L^2}\left(c_1\log y+\frac{c_2}{2}\right)
 +O_w(X/L^3).                                                   \tag{11}
\]

In particular the response is eventually positive uniformly on the
shell, since \(c_1<0\), and

\[
\|S_X\|_2^2\sim\frac{q_0c_1^2}{d^2}\frac{X^3}{L^2}.           \tag{12}
\]

Projection does remove the first term, but the next term has nonconstant
shape. Put

\[
\bar a=\frac1{q_0}\int_1^2y^2\log y\,dy,\qquad
\sigma_a^2=\int_1^2y^2(\log y-\bar a)^2\,dy>0.
\]

Explicitly \(\bar a=8\log2/7-1/3\) and
\(\sigma_a^2=7/27-8(\log2)^2/21\).

Then

\[
PS_X(x)=\frac{c_1}{d^2L^2}\,x(\log(x/X)-\bar a)
 +O_{L^2}(X^{3/2}/L^3),
\]
\[
\boxed{\quad
\|PS_X\|_2^2\sim\frac{c_1^2\sigma_a^2}{d^4}\frac{X^3}{L^4}.
\quad}                                                          \tag{13}
\]

Here \(O_{L^2}\) denotes a norm bound. Strict positivity of
\(\sigma_a^2\) follows because \(\log y\) is not constant on
\([1,2]\). Thus even an independently bounded projected semiprime
sector cannot meet \(X^{3-\kappa+o(1)}\) for any fixed
\(\kappa>0\). Removing the linear continuum before estimating
sectors does not fix this failure.

## 6. The precise remaining cancellation

The exact shell decomposition gives the following paired target for
\(0<\kappa<11/24\):

\[
\|PF_X\|_2^2+2\langle PF_X,PS_X\rangle+\|PS_X\|_2^2
\ll X^{3-\kappa+o(1)},
\]
\[
\big|c_wM_1(U)+\lambda_{F_X}+\lambda_{S_X}\big|
\ll X^{-\kappa/2+o(1)}.                                         \tag{14}
\]

The concurrent [scalar-detector derivation](SCALAR_DETECTOR_20261004.md)
proves that, for the actual arithmetic response and estimates on **all
sufficiently large real \(X\)**, the scalar condition in (14) alone
already implies the full variance target. Even either one-sided scalar
envelope suffices. Equation (2) transfers that result to the prime-inner
version for the stated \(\kappa\) range. Thus the two equations in (14)
are a valid exact decomposition, but they are no longer two logically
independent global obligations. The signed scalar is the preferred
minimal next target; covariance reveals the arithmetic cancellation that
its proof must respect. This distinction has no shell-local analogue for
generic coefficients.

The signs in (14) are physical; \(S_X\) already includes its minus
sign from (4). Formula (13) proves that treating the three quadratic
terms separately by absolute values cannot succeed. The smooth sector
must reproduce the opposite semiprime shape to all fixed logarithmic
orders, and the scalar must simultaneously match the continuum.

There is already an unconditional, but insufficient, signed cancellation
law. Quantitative PNT and \(\int w=0\) give
\(V_g(x)=O_{M,w}(X/L^M)\), uniformly on the shell, for every fixed
\(M\). Combining the exact Vaughan identity, its pointwise
\(O(X^{1/2})\) error, and (2), whose pointwise proof is available,
gives

\[
F_X(x)+c_wM_1(U)x=-S_X(x)+O_{M,w}(X/L^M)                       \tag{15}
\]

for every fixed \(M\). The two-channel raw Gram matrix of
\((S_X,F_X+c_wM_1(U)x)\), divided by \(\|S_X\|_2^2\), therefore
converges to
\(\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\).
The projected Gram matrix of \((PS_X,PF_X)\), divided by
\(\|PS_X\|_2^2\), has the same limit. Equations (12) and (13)
make the denominators nonzero eventually; taking \(M>2\) and
\(M>3\), respectively, proves the two conclusions. This confirms
genuine signed cross cancellation for the actual coefficients, but its
remainder inherits the classical subpower PNT quality. It establishes no
fixed \(\kappa>0\).

One may center \(S_X\) by the entire explicit integral in (10), not
just its first two Taylor terms. This improves bookkeeping but the
classical PNT replacement error is still only subpower small relative
to \(X\), and therefore does not meet a fixed-power norm budget by
itself. A finite logarithmic expansion cannot be discarded at the
target scale either. This is why the exact discrete \(S_X\) remains
in (14).

The large-prime identity has passed an arithmetic-structure test: it kills
all nontrivial cofactors on distinct-prime exact collisions and exposes
the compulsory compensating sectors. It has not passed the fixed-saving
gate. The next useful estimate should retain the signed sum of the
smooth-cofactor response, exact semiprime response, and continuum, and
prove one side of the scalar envelope in (14). The distinct-prime,
separated-product covariance remains a possible mechanism and a useful
check on any proposed sector estimate. A new separated power bound for
\(M_1(U)\), or a semiprime absolute majorant, would not supply this
estimate within the present rules.

## 7. Finite-check scope

The accompanying [sector pilot](../../../numerics/01_signed_arithmetic_covariance/centered_sector_pilot.py)
checks (3), coefficient-level decomposition (4), and the complete centered
energy bookkeeping; its [small record](../../../numerics/01_signed_arithmetic_covariance/centered_sector_record_20261004.json)
contains the parameters and floating diagnostics. It does not certify the
PNT asymptotics. On its modest shells the semiprime slopes are negative,
whereas (11) is eventually positive; the nonzero \(c_w\) is small and
there is no effective asymptotic threshold in this note. Finite covariance
signs are consequently not used as evidence for (12), (13), or (15).
