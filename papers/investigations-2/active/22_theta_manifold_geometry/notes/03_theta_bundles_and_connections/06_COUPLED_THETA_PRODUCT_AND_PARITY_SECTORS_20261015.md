# Coupled theta products before source restriction: parity sectors and a Gram obstruction

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is a bounded continuation of the [elliptic-shift experiment](05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md), using a genuinely coupled two-source identity. The product identity, its full source insertion, coefficient discriminator and specified Gram obstruction are analytic results. No signed amplitude bound for theta is proved.

## 1. Independent source parameters give a mixed theta addition identity

Keep both source points independent:

\[
q=e^{4u},\quad r=e^{4v},\quad
\Theta(z,iq)=\sum_{n\in\mathbb Z}e^{-\pi qn^2+2\pi inz}.
\]

Before applying either physical source operator, make the invertible lattice change

\[
p=n+m,\quad k=n-m,\qquad
n=(p+k)/2,\quad m=(p-k)/2.
\]

Its image is the same-parity lattice `p≡k (mod 2)`. Writing `X=z+w`, `Y=z-w`, the complete product becomes

\[
\boxed{\Theta(z,iq)\Theta(w,ir)
=\sum_{p\equiv k\ (2)}
e^{-\pi Q_{q,r}(p,k)+\pi i(pX+kY)},}
\tag{1}
\]

where

\[
Q_{q,r}(p,k)
=\frac{q+r}{4}(p^2+k^2)+\frac{q-r}{2}pk.
\tag{2}
\]

The quadratic form has eigenvalues `q/2` and `r/2` and is positive definite. Its mixed term is present at all unequal source points.

Put `A=q+r`, `B=q-r`, and introduce the two standard parity series in the manuscript's period-one elliptic convention:

\[
\vartheta_\epsilon(Z,iA)
=\sum_{a\in\mathbb Z}
e^{-\pi A(a+\epsilon/2)^2+2\pi i(a+\epsilon/2)Z},
\qquad\epsilon=0,1.
\]

Writing `p=2a+epsilon`, `k=2b+epsilon` in (1) gives the exact mixed-heat form

\[
\boxed{\Theta(z,iq)\Theta(w,ir)
=\exp\!\left(\frac{B}{2\pi}\partial_X\partial_Y\right)
\sum_{\epsilon=0}^1
\vartheta_\epsilon(X,iA)\vartheta_\epsilon(Y,iA).}
\tag{3}
\]

The exponential operator has a precise convergent meaning here. On each Fourier mode its multiplier is `exp[-2πB(a+epsilon/2)(b+epsilon/2)]`. Expanding that multiplier and taking absolute values is dominated, locally in the elliptic arguments, by the Gaussian with coefficient

\[
A-|B|=2\min(q,r)>0.
\]

Thus the series, derivative expansion and every fixed source jet converge normally on compact parameter sets with `q,r>0`. This does not claim that the mixed-heat operator is a positivity-preserving semigroup on general functions: its generator has opposite-sign diffusion directions in `X+Y` and `X-Y`.

At `q=r`, (3) reduces to the ordinary separated parity addition formula with modulus `2iq`. In the physical two-source integral, however, `q=r` means `u=v`, a measure-zero diagonal. Its separated factorization cannot replace (3) off that diagonal.

## 2. Both complete physical fourth-jet operators

For the ordinary marked-frame coefficients the physical source operator is

\[
\mathscr S_q
=e^u\left(\frac{q^2}{16\pi^2}\partial_z^4
 +\frac{3q}{8\pi}\partial_z^2\right),
\]

evaluated at `z=0`. This equals the manuscript's full covariant operator `e^u(q²D_z⁴-3π²)/(16π²)` at that section, including all connection-coefficient derivatives. Use the analogous `S_r` in the second variable. Since `∂_z=∂_X+∂_Y`, `∂_w=∂_X-∂_Y`, their complete product is

\[
\boxed{\begin{aligned}
\mathscr S_q\mathscr S_r
=\frac{e^{u+v}qr}{256\pi^4}
(\partial_X^2-\partial_Y^2)^2
\big\{&qr(\partial_X^2-\partial_Y^2)^2\\
&+6\pi[(q+r)(\partial_X^2+\partial_Y^2)
 +2(q-r)\partial_X\partial_Y]+36\pi^2\big\}.
\end{aligned}}
\tag{4}
\]

Apply this to the complete right side of (3) and then put `X=Y=0`. All its coefficients are external parameters for these vertical derivatives. The result is exactly `Phi(u)Phi(v)`, not a squared Hermitian norm.

The source coefficient for a same-parity pair `(p,k)` is particularly explicit:

\[
\boxed{\begin{aligned}
M_{p,k}(u,v)
={}&\frac{e^{u+v}\pi^2qr}{256}(p^2-k^2)^2
 [\pi q(p+k)^2-6][\pi r(p-k)^2-6]\\
&\hspace{18mm}\cdot e^{-\pi Q_{q,r}(p,k)}.
\end{aligned}}
\tag{5}
\]

Equivalently, with `φ_0=0` and the manuscript's positive physical modes,

\[
M_{p,k}(u,v)
=\tfrac14\phi_{|(p+k)/2|}(u)\phi_{|(p-k)/2|}(v),
\qquad
\Phi(u)\Phi(v)=\sum_{p\equiv k\ (2)}M_{p,k}(u,v).
\tag{6}
\]

Both zero-mode lines `p=k` and `p=-k` vanish exactly through the factor `(p²-k²)²`. Away from those lines, the parity lattice gives `|p+k|,|p-k|>=2`. Hence every coefficient in (5) is strictly positive for `q,r>=1`. This is source positivity before the oscillatory physical transform, not the desired signed amplitude estimate.

## 3. What is arithmetic-specific and what is merely reindexing

For arbitrary even weighted coefficients `(a_n)`, (1) still holds after inserting the weight

\[
a_{(p+k)/2}a_{(p-k)/2}.
\]

Thus the lattice change itself does not reject a weighted collision control. The canonical separated parity factors in (3) use unit coefficients and do not hold unchanged for an arbitrary weighted series. In the parity sector `p=2a`, `k=2b`, the pre-source coefficient array is

\[
C_0(a,b)=a_{a+b}a_{a-b}.
\tag{7}
\]

There is a precise intermediate discriminator. Suppose all coefficients are positive, even, of polynomial growth, and `a_0=1`. Rank one of the full array (7) is equivalent to

\[
\boxed{a_{a+b}a_{a-b}=a_a^2a_b^2\quad(a,b\in\mathbb Z).}
\tag{8}
\]

Indeed its zeroth row and column give the normalized outer product. Setting `b=1` in (8) and taking logarithms shows that the second difference of `log a_n` is the constant `2 log a_1`. The initial values at 0 and 1 therefore give

\[
a_n=c^{n^2},\qquad c=a_1>0.
\tag{9}
\]

Conversely these Gaussian weights satisfy (8). Polynomial growth forces `0<c<=1`. The primitive normalization then distinguishes theta: every term of

\[
\psi_a'(0)=\sum_{n\ge1}c^{n^2}(1-4\pi n^2)e^{-\pi n^2}
\]

is negative. For `c<1` the sum is strictly greater than the theta value `-1/2`; hence the prescribed endpoint `psi_a'(0)=-1/2` forces `c=1`.

The finite weighted collision controls fail (8) directly. If their highest nonzero coefficient is `a_M>0`, then the principal minor of (7) on indices `{0,M}` is

\[
\det\begin{pmatrix}1&a_M^2\\a_M^2&a_{2M}\end{pmatrix}
=-a_M^4<0.
\tag{10}
\]

This includes the three-square and four-square controls, independently of which finitely many source endpoints they retain.

This discriminator lives **before** applying the two source operators. In particular, (8) uses coefficients on the zero-mode lines that (4) annihilates. It cannot be inferred from the source-projected identity without separately restoring the missing information. Input rigidity under (8) and the endpoint is not a signed transform inequality.

## 4. The natural addition-basis Gram matrix is indefinite

There is an exact obstruction to treating (5) as a positive Gram kernel in the parity indices. For every physical pair `u,v>=0`, the matrix `M_(p,k)` is symmetric in p and k. All its diagonal entries vanish, because `m=(p-k)/2=0`. Its indicated off-diagonal entries are positive.

In the even sector, the principal block on `{0,2}` is

\[
\boxed{\begin{pmatrix}0&b_{\rm ev}\\b_{\rm ev}&0\end{pmatrix},
\qquad b_{\rm ev}=\tfrac14\phi_1(u)\phi_1(v)>0.}
\tag{11}
\]

Its determinant is `-b_ev²`, and the vector `(1,-1)` has value `-2b_ev`. In the odd sector, indices `{1,3}` give the same block with

\[
b_{\rm odd}=\tfrac14\phi_2(u)\phi_1(v)>0.
\tag{12}
\]

Both parity matrices therefore fail positive semidefiniteness at **every** physical source pair, including the diagonal `q=r`. This is a stronger, concrete statement than observing that a later cosine kernel changes sign. The pre-source unit coefficient array is rank one; after the mixed Gaussian and both complete source operators are inserted, the resulting matrix fails Gram positivity, with exact zero-mode annihilation forcing its zero diagonal.

The obstruction persists on the coefficient zero-sum subspace and has both signs there. For `n>=m>=1`, the explicit modes give

\[
\frac{\phi_n(u)}{\phi_m(u)}
=\frac{n^2(2\pi n^2q-3)}{m^2(2\pi m^2q-3)}
 e^{-\pi(n^2-m^2)q}
\le 2(n/m)^4e^{-3(n^2-m^2)},\qquad q\ge1.
\tag{12a}
\]

Indeed `2πm²q-3>=πm²q` because `πm²q>3`, while `2πn²q-3<=2πn²q`; then `πq>3` gives the displayed bound.

For the even block on `{0,2,4}`, put

\[
a=M_{0,2}=\tfrac14\phi_1(u)\phi_1(v),\quad
b=M_{0,4}=\tfrac14\phi_2(u)\phi_2(v),\quad
c=M_{2,4}=\tfrac14\phi_3(u)\phi_1(v).
\]

Its quadratic form is `2a v_0v_1+2b v_0v_2+2c v_1v_2`. Both vectors `v_-=(1,-1,0)` and `v_+=(1,1,-2)` have coefficient sum zero. Their values are `-2a<0` and `2a-4b-4c`, respectively. By (12a),

\[
\frac{b+c}{a}
\le1024e^{-18}+162e^{-24}
<\frac{1024}{2^{18}}+\frac{162}{2^{24}}<\tfrac12,
\]

so the latter value is strictly positive. For the odd block on `{1,3,5}`, the same vectors work with

\[
a=\tfrac14\phi_2(u)\phi_1(v),\quad
b=\tfrac14\phi_3(u)\phi_2(v),\quad
c=\tfrac14\phi_4(u)\phi_1(v),
\]

because

\[
\frac{b+c}{a}
\le324e^{-24}+32e^{-36}
<\frac{324}{2^{24}}+\frac{32}{2^{36}}<\tfrac12.
\]

Thus each parity matrix is indefinite even after restricting to zero-sum coefficient vectors. Adding any scalar constant rank-one term `lambda 11^T` leaves these two witnesses unchanged and cannot make either block positive or negative semidefinite. This rules out repair by that particular scalar normalization. The coefficient zero-sum constraint is **not** the complete physical stationarity constraint; no equivalence between them is asserted.

There is no contradiction with the positive scalar sum in (6): entrywise positive off-diagonal matrices can be indefinite, and the sum tests only a particular vector. The obstruction applies to this actual addition-basis matrix and the stated scalar correction. It does not exclude an alternative lifted kernel, other constrained representations, or a genuinely new arithmetic inequality.

## 5. Physical heat transform and indispensable parity cancellation

Let `c_j(x,u)=u^j cos(xu+jπ/2)`, and use the exponential-average kernel from [Note 04](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md):

\[
U_{j,\delta}(x;u,v)
=c_j(x,u)c_j(x,v)
-\frac{e^{-\delta}}2[c_j(x,u)c_j(x+\delta,v)
 +c_j(x,v)c_j(x+\delta,u)].
\]

The complete coupled formula is

\[
\boxed{\mathcal A_{j,\delta}
=\int_0^\infty\!\int_0^\infty
e^{t(u^2+v^2)}U_{j,\delta}(x;u,v)
\sum_{p\equiv k\ (2)}M_{p,k}(u,v)\,du\,dv.}
\tag{13}
\]

All heat multipliers and spectral phases remain. Complete-source decay justifies the series/integral exchanges locally uniformly in the physical parameters. Source positivity in (6) provides no sign for (13).

The lattice parity has a direct physical interpretation. Even p,k mean that n,m have the same parity; odd p,k mean opposite parity. Let `W_e,W_o` be the even- and odd-index parts of the complete starting `h_j(t,x)`, and let `V_e,V_o` be the corresponding endpoint values, either complete or cut off only at that endpoint. Put `alpha=e^(-delta)`, `W_+=W_e+W_o`, `W_-=W_e-W_o`, and similarly `V_±`. The two parity contributions to the amplitude observation are exactly

\[
\begin{aligned}
\mathcal A_{\rm same}
 &=W_e^2+W_o^2-\alpha(W_eV_e+W_oV_o),\\
\mathcal A_{\rm cross}
 &=2W_eW_o-\alpha(W_eV_o+W_oV_e),
\end{aligned}
\]

and therefore

\[
\boxed{\mathcal A_{\rm same}=\tfrac12(\mathcal A+\mathcal B),
\quad \mathcal A_{\rm cross}=\tfrac12(\mathcal A-\mathcal B),}
\quad
\mathcal B=W_-^2-\alpha W_-V_-.
\tag{14}
\]

Only `W_+` is the complete physical starting observation. There is no established bound paying the extra `B` by its small starting energy. Even the algebraic assignment `W_e=1,W_o=-1,V_e=V_o=0` gives total `A=0` and parity sectors `+2,-2`. This is a cancellation witness, not a claimed theta stationary point. Thus bounding the sectors separately would require a new comparison, not supplied by the addition identity.

The equal-coefficient source does give an exact relation for its even-index part. With `a=log(2)/2`,

\[
\Phi_e(u)=e^{-a}\Phi(u+a),
\]

and hence

\[
h_{j,e}(t,x)=e^{-a}\int_a^\infty
e^{t(v-a)^2}\Phi(v)(v-a)^j
\cos[x(v-a)+j\pi/2]\,dv.
\tag{15}
\]

Its shifted lower endpoint, heat tilt and spectral phase are part of the relation. Dropping them would falsely identify this parity observation with a scaled copy of the original physical field. The companion [cutoff and parity note](07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md) examines the corresponding actual-theta cancellation and the correct endpoint-only cutoff domain. In the `(p,k)` lattice, that cutoff is the diagonal strip `|p-k|<=2N`; a rectangular box also truncates the starting factor.

## 6. Complete primitive axes, edges and corner

The primitive product can also be written in the addition variables, but first subtract both zero-mode axes:

\[
\boxed{\psi(u)\psi(v)
=\frac{e^{u+v}}4
\{\Theta(0,iq)\Theta(0,ir)-\Theta(0,iq)-\Theta(0,ir)+1\}
=\frac{e^{u+v}}4\sum_{\substack{p\equiv k\ (2)\\p\ne k,\ p\ne-k}}
e^{-\pi Q_{q,r}(p,k)}.}
\tag{16}
\]

This converges with double exponential decay in each half-line variable. The unsubtracted product contains growing zero-axis terms and cannot be used as a convergent positive-time primitive transform merely because the differential source operator eventually annihilates them.

Let `L_u=∂_u²-1`, and let `Q=e^{t(u²+v²)}U_(j,delta)`. Then `64 Phi(u)Phi(v)=L_u L_v[psi(u)psi(v)]`. Both test factors are even in their individual source variables. Applying the exact one-variable endpoint identity in each variable gives

\[
\begin{aligned}
64\mathcal A_{j,\delta}
={}&\iint\psi(u)\psi(v)L_uL_v Q\,du\,dv\\
&+\tfrac12\int\psi(v)L_vQ(0,v)\,dv
 +\tfrac12\int\psi(u)L_uQ(u,0)\,du
 +\tfrac14Q(0,0).
\end{aligned}
\tag{17}
\]

All first-derivative lower-edge terms vanish by evenness; all upper endpoints vanish by decay. With `d=δ_(j0)`, `alpha=e^(-delta)`, `I_x=I_j(t,x)` and `I_y=I_j(t,x+delta)`, the edges and corner in (17) are

\[
d\{(1-\alpha/2)I_x-(\alpha/2)I_y\}
 +\frac d4(1-\alpha).
\tag{18}
\]

Together with the interior `I_x²-alpha I_x I_y`, this reproduces

\[
64\mathcal A_{j,\delta}
=(I_x+d/2)^2-\alpha(I_x+d/2)(I_y+d/2).
\]

Thus neither the lattice addition nor the double source differentiation removes a primitive edge or corner. The physical energy remains `E(t,x)=H²+H_x²` at the complete stationary starting point on both branches.

## 7. Outcome and verification

This experiment supplies a genuine coupled identity with an explicit mixed derivative, rather than a boundary reindexing of a single source. It also supplies a meaningful arithmetic coefficient discriminator. Its most natural positive-Gram interpretation, however, is false: both source parity blocks have explicit negative principal minors and both signs on the coefficient zero-sum subspace, even after any scalar constant-kernel correction. Separately estimating the physical parity channels also introduces a second observation whose cancellation is necessary to recover the small complete starting scale.

The next useful step would have to exploit a different constraint or kernel while retaining both source variables, the mixed operator, parity recombination and the endpoint-only cutoff. Increasing the number of parity modes or applying source positivity to (13) does not address the demonstrated obstruction. This note proves no lower bound `A>=-K_NE` and no collision exclusion for theta.

The accompanying [exact checker](../../numerics/check_coupled_theta_product.py) verifies the formal operator and mode polynomials, finite lattice/sector correspondence, Gaussian coefficient controls, negative minors, the zero-sum witnesses and exact rational sign bounds, parity-channel algebra and primitive edges. Its [receipt](../../numerics/COUPLED_THETA_PRODUCT_ALGEBRA_20261015.json) records finite assertion groups and the source hash. The infinite convergence, rigidity and full-domain statements have the analytic proofs above; they are not inferred from finite enumeration. The checker does not evaluate a theta stationary point or assert an RH consequence.
