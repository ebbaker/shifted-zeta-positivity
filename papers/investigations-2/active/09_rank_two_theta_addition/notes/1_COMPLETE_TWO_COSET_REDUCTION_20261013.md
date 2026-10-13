# Complete unequal-scale two-coset reduction for both paired kernels

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex); reasoning effort **ultra**, supplied from the
parent chat's verified current-turn configuration. The parallel analytic
and computational checks are internal LLM work, not independent validation.

This completes the first identity task in the [initial program](INITIAL_RESEARCH_PROGRAM_20261013.md)
and supplies the source decomposition for [direction 06](../../06_paired_kernel_factorization/README.md).
The result is an absolutely convergent, modular-folded two-coset identity
for **both** `J_0` and `J_1`, with the genuine differential insertions. The
two cosets are exactly same-parity and opposite-parity source products.
They do not supply a positive factorization of their Fourier observations.
The separate endpoint defects exposed below must cancel between sectors.

## 1. Source, normalization and the order of operations

Write
\[
 \Theta(a)=\sum_{n\in\mathbb Z}e^{-\pi a n^2},\qquad
 T(u)=e^u\Theta(e^{4u}),\qquad D_u=\partial_u.
\]
Jacobi inversion `Theta(a)=a^(-1/2)Theta(1/a)` makes `T` even. With the
project's normalization,
\[
 \Phi_e(u)=\frac{D_u^2-1}{16}T(u),\qquad
 m_t(u)=e^{tu^2}\Phi_e(u),\qquad
 H_t(x)=\tfrac12\int_{\mathbb R}e^{ixu}m_t(u)\,du.                 \tag{1}
\]
Indeed, for `z=pi n^2 e^(4u)`,
\[
 (D_u^2-1)e^{u-z}=e^{u-z}P(z),\qquad
 P(z)=16z^2-24z,                                                \tag{2}
\]
so for `p>=0`
\[
 \Phi(p)=\sum_{n\ge1}\phi_n(p),\quad
 \phi_n(p)=\big(2\pi^2n^4e^{9p}-3\pi n^2e^{5p}\big)
             e^{-\pi n^2e^{4p}}>0.                            \tag{3}
\]
The zero theta mode is annihilated in (2). For each compact interval of
`u`, theta convergence permits every fixed source derivative. The relevant
Jacobi modular formula is [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32);
the constants in (1)--(3) are calculated here rather than imported.

**Ordering:** first differentiate the complete smooth theta identity,
then use `Phi_e(u)=Phi(|u|)`, then interchange the positive-half-line
lattice sums and the physical integrals under the bounds in section 5.
For `t>0`, an individual raw full-line summand behaves as
`-3 pi n^2 exp(tu^2+5u)` when `u` tends to minus infinity. Its one-source
absolute integral diverges. Thus the raw unrestricted product Fourier
exchange cannot stand in for this folding argument. No such exchange is
used below.

## 2. Two cosets with the unequal scales retained

For arbitrary `a,b>0`, set
\[
 Q(a,b)=\frac14\begin{pmatrix}a+b&a-b\\a-b&a+b\end{pmatrix},
 \quad \Lambda_0=(2\mathbb Z)^2,\quad
 \Lambda_1=(2\mathbb Z+1)^2.
\]
The map
\[
 k=n+m,\quad \ell=n-m,\qquad
 n=(k+\ell)/2,\quad m=(k-\ell)/2                            \tag{4}
\]
is a bijection from `Z^2` onto the disjoint union of these two cosets.
There is **no factor two** in this discrete reindexing. Its image satisfies
\[
 an^2+bm^2=(k,\ell)Q(a,b)(k,\ell)^T
 =\frac{(a+b)(k^2+\ell^2)+2(a-b)k\ell}{4}.                   \tag{5}
\]
The eigenvalues of `Q` are `a/2,b/2`; `det Q=ab/4`.
Define
\[
 E(a,b)=\sum_{\Lambda_0}e^{-\pi y^TQ(a,b)y},\qquad
 O(a,b)=\sum_{\Lambda_1}e^{-\pi y^TQ(a,b)y}.
\]
Then `Theta(a)Theta(b)=E+O`. At `a=b`, (5) reduces to the usual two-term
addition calibration, corresponding to [DLMF 20.7.14](https://dlmf.nist.gov/20.7.E14).
For physical unequal scales its mixed term remains.

For `p,q>=0`, use `a=e^(4p),b=e^(4q)` and
\[
 z_{k\ell}=\frac{\pi a(k+\ell)^2}{4},\qquad
 w_{k\ell}=\frac{\pi b(k-\ell)^2}{4}.
\]
The complete differentiated sector is
\[
 F_\varepsilon(p,q)=\frac{e^{p+q}}{256}
 \sum_{(k,\ell)\in\Lambda_\varepsilon}
 P(z_{k\ell})P(w_{k\ell})e^{-z_{k\ell}-w_{k\ell}},
 \qquad \varepsilon=0,1.                                     \tag{6}
\]
In particular,
\[
 \boxed{\Phi(p)\Phi(q)=F_0(p,q)+F_1(p,q).}                    \tag{7}
\]
Equation (6) is precisely `(D_p^2-1)(D_q^2-1)/256` applied to
`e^(p+q)E` or `e^(p+q)O`. Each derivative acts on the full exponential,
including its prefactor. This includes all lower terms of both source
insertions; replacing `P(z)` with just its leading monomial is invalid.

The lines `k=ell` and `k=-ell` are the original zero axes `m=0,n=0`.
They vanish individually because `P(0)=0`, including their common origin.
No subtraction of surviving axis terms is needed, and no diagonal
`n=m` or anti-diagonal `n=-m` is discarded. Every remaining term of (6)
is nonnegative on the folded region, since its nonzero `z,w` are at least
`pi`. This is a source fact, not the desired Fourier sign.

## 3. One modular generator, including its characteristic

The simultaneous inversion generator can be calculated directly by
Gaussian Poisson summation. Put `R=4Q(a,b)`, so `det R=4ab` and
`R^(-1)=Q(1/a,1/b)`. The even sector is a sum over `Z^2` with matrix `R`;
the odd sector is the same sum translated by `(1/2,1/2)`. Hence
\[
 E(a,b)=\frac1{2\sqrt{ab}}
   \sum_{y\in\mathbb Z^2}e^{-\pi y^TQ(1/a,1/b)y},
\]
\[
 O(a,b)=\frac1{2\sqrt{ab}}
   \sum_{y\in\mathbb Z^2}(-1)^{y_1+y_2}
                         e^{-\pi y^TQ(1/a,1/b)y}.              \tag{8}
\]
Their sum projects onto `y_1=y_2 mod 2`, giving
\[
 (E+O)(a,b)=\frac1{\sqrt{ab}}(E+O)(1/a,1/b).                   \tag{9}
\]
Thus the modular square-root factor is `1/(2 sqrt(ab))` in each individual
Poisson formula and `1/sqrt(ab)` after the parity projection. The signed
characteristic in (8) cannot be dropped. Individual cosets do not map to
individual positive copies of themselves. Formula (8) is the real Gaussian
specialization of the [inversion generator](https://dlmf.nist.gov/21.5.E8)
and [characteristic transformation](https://dlmf.nist.gov/21.5.E9).

On multiplying by `e^(p+q)`, the factor in (9) changes it to
`e^(-p-q)`. To make the transported differential insertions explicit, put
`z*=pi e^(-4p)(k+ell)^2/4` and `w*=pi e^(-4q)(k-ell)^2/4`.
Differentiating the full prefactors in (8) gives
\[
 F_\varepsilon(p,q)=\frac{e^{-p-q}}{512}
 \sum_{(k,\ell)\in\mathbb Z^2}(-1)^{\varepsilon(k+\ell)}
 P(z^*)P(w^*)e^{-z^*-w^*}.                                   \tag{9a}
\]
For example `(D_p^2-1)e^(-p-z*)=P(z*)e^(-p-z*)`, so no derivative
of the modular factor is lost. Unlike (6), individual terms of (9a)
need not be positive: `P(z*)` changes sign and the odd sector also has
its characteristic. The dual scales can become small; (9a) is an exact
locally convergent identity, while global integration below uses the
folded expansion (6) and its majorant, not an unpaid dual termwise exchange.

All derivatives in (1) commute with simultaneous reflection because their
orders are even. Independent one-source Jacobi inversions
also give `Phi_e(u)Phi_e(v)=Phi(|u|)Phi(|v|)`. These one-source inversions
are used for the four physical quadrants: simultaneous inversion alone
would not fold a mixed-sign quadrant. Characteristics mix during that
operation; it is only the complete source that is reflected before its
positive-half-line parity decomposition is defined.

## 4. The physical reduction and its exact 09-to-06 interface

Let `p=|s+r|,q=|s-r|`. Define the two complete folded sector kernels by
\[
 J_{j,t}^{\varepsilon}(s)=\int_{\mathbb R}
   r^2(r^2-s^2)^j e^{2t(s^2+r^2)}F_\varepsilon(p,q)\,dr,
 \qquad j=0,1.                                                \tag{10}
\]
Then
\[
 \boxed{J_{j,t}=J_{j,t}^0+J_{j,t}^1,\qquad
 (H_t^{(j+1)})^2-H_t^{(j)}H_t^{(j+2)}
       =\widehat J_{j,t}(2x).}                                \tag{11}
\]
The second identity has exactly the normalization of the
[complete-kernel note](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md).
The Jacobian `du dv=2 ds dr` is present; the lattice bijection (4) has
no continuous Jacobian. In particular the signed factor `r^2-s^2`
in `J_1` has not been replaced by its absolute value.

The rank-two identity can be simplified further without an approximation.
For `p>=0` define
\[
 A(p)=\sum_{n\ge1,\,2\mid n}\phi_n(p),\quad
 B(p)=\sum_{n\ge1,\,2\nmid n}\phi_n(p),\quad A+B=\Phi.
\]
In (4), the even-even `(k,ell)` coset means that `n,m` have the same
parity, and the odd-odd coset means opposite parity. Therefore
\[
 \boxed{F_0(p,q)=A(p)A(q)+B(p)B(q),\quad
 F_1(p,q)=A(p)B(q)+B(p)A(q).}                                  \tag{12}
\]
Set
\[
 a_t(u)=e^{tu^2}A(|u|),\quad b_t(u)=e^{tu^2}B(|u|),\quad
 h_A(x)=\tfrac12\widehat a_t(x),\quad h_B(x)=\tfrac12\widehat b_t(x).
\]
These are absolutely integrable, with all polynomial moments. Although
`a_t,b_t` need not be smooth at the origin, their Fourier transforms have
all frequency derivatives. Write
\[
 \mathscr L_j(f)=(f^{(j+1)})^2-f^{(j)}f^{(j+2)},
\]
\[
 \mathscr C_j(f,g)=2f^{(j+1)}g^{(j+1)}
                   -f^{(j)}g^{(j+2)}-g^{(j)}f^{(j+2)}.
\]
The bilinear version of the same Jacobian calculation gives
\[
 \widehat J_{j,t}^{0}(2x)=\mathscr L_j(h_A)+\mathscr L_j(h_B),
 \qquad
 \widehat J_{j,t}^{1}(2x)=\mathscr C_j(h_A,h_B).                 \tag{13}
\]
Since `H=h_A+h_B`, these sum to (11). Formula (13) is the exact
factorization interface for direction 06, with no missing diagonal or
cross term. It is an indefinite quadratic decomposition, not an
autocorrelation factorization.

The physical stationary equations are imposed only after summation:
`h_A'+h_B'=0` for `j=0`, and `h_A''+h_B''=0` for `j=1`.
Sectorwise stationarity would change the problem.

## 5. Domain, summation and a declared cutoff/tail ledger

For a first bounded diagnostic take `0<=t<=T=1/20`, `|s|<=S=1/2`,
and retain `|r|<=R=1`. Fourier evaluation on any specified finite
frequency window uses the same estimates; the bounds below are uniform
for every real frequency. The exact identities themselves hold for all
real `t,s,x`. For larger compact time intervals the double-exponential
envelope below supplies the domain even when the displayed Gaussian
bound is no longer useful.

The full-source estimates established in the complete-kernel note are
\[
 0<\Phi(p)\le C e^{-8\pi p^2},\quad C=4\pi^2e^{-\pi},
 \qquad
 \Phi(p)\le4\pi^2e^{9p-\pi e^{4p}},\quad p\ge0.               \tag{14}
\]
Since `0<=A,B<=Phi`, all absolute sector sums in (6) are bounded by
`Phi(p)Phi(q)`. With `kappa=2(8 pi-T)>0`,
\[
 e^{2t(s^2+r^2)}(F_0+F_1)(p,q)
 \le C^2e^{-\kappa(s^2+r^2)}.                                 \tag{15}
\]
This pays lattice summation, the `r` integral, the outer Fourier
integral, and every fixed polynomial moment in either order. The positive
theta series permits Tonelli for its absolute majorant. For `J_1`, apply
it with `r^2|r^2-s^2|<=r^2(r^2+s^2)`. On compact `p,q` sets,
the differentiated series is dominated by a convergent Gaussian in the
lattice indices; fixed additional derivatives merely raise its polynomial
degree. For arbitrary compact time sets the second inequality of (14)
absorbs every fixed Gaussian and polynomial factor. There is no
positive-heat raw negative-half-line summation step.

For an explicit `r`-tail payment define
\[
 I_d(R)=\int_R^\infty r^d e^{-\kappa r^2}\,dr.
\]
For either sector separately, and also for their sum,
\[
 |J_{0,t}(s)-J_{0,t}^{[R]}(s)|
 \le 2C^2e^{-\kappa s^2}I_2(R),
\]
\[
 |J_{1,t}(s)-J_{1,t}^{[R]}(s)|
 \le 2C^2e^{-\kappa s^2}\{I_4(R)+S^2I_2(R)\},\quad |s|\le S.  \tag{16}
\]
Use
\[
 I_0(R)\le\frac{e^{-\kappa R^2}}{2\kappa R},\qquad
 I_d(R)=\frac{R^{d-1}e^{-\kappa R^2}}{2\kappa}
                +\frac{d-1}{2\kappa}I_{d-2}(R).              \tag{17}
\]
If a Fourier integral is also truncated at `|s|<=S`, its outer tail is
bounded, respectively, by
\[
 2C^2M_2 I_0(S),\qquad
 2C^2\{M_4I_0(S)+M_2I_2(S)\},                                \tag{18}
\]
where `M_2=sqrt(pi)/(2 kappa^(3/2))` and
`M_4=3 sqrt(pi)/(4 kappa^(5/2))`. Add the integrated payment from (16)
for an actual rectangular `(s,r)` cutoff. No oscillatory cancellation
is assumed in these payments.

For a theta cutoff `1<=n<=N`, its omitted source satisfies
\[
 0\le\Phi(p)-\Phi_N(p)\le b_N(p):=
 \frac{2\pi^2e^{9p}(N+1)^4e^{-\pi(N+1)^2e^{4p}}}
 {1-\big((N+2)/(N+1)\big)^4e^{-\pi(2N+3)e^{4p}}},\quad p\ge0. \tag{19}
\]
The denominator is positive for `N>=1`. This follows by dropping the
negative source term and bounding consecutive ratios in the remaining
`n^4` series. Also `b_N(p)<=b_N(0)`. The omitted product is at most
`b_N(p)Phi(q)+Phi(p)b_N(q)`. This includes same- and opposite-parity
omissions. A rectangular cutoff `|n|,|m|<=N` is the **diamond**
`|k|+|ell|<=2N` in (4), with the parity restriction; a square in the
new coordinates is a different finite set and requires its own payment.

## 6. The gluing endpoints reveal an actual obstruction

The even-index density has a simple exact form. Put `h=(log 2)/2`.
Since `phi_(2n)(p)=2^(-1/2)phi_n(p+h)`,
\[
 A(p)=2^{-1/2}\Phi(p+h),\qquad B(p)=\Phi(p)-A(p),\quad p\ge0. \tag{20}
\]
Consequently
\[
 h_A(t,x)=2^{-1/2}e^{th^2}\operatorname{Re}\left[
 e^{-ihx}\int_h^\infty e^{tv^2+(ix-2th)v}\Phi(v)\,dv\right].   \tag{21}
\]
This is a complete shifted half-line transform, with the finite endpoint
`h` retained. It is not the full transform multiplied by a phase.

For completeness the endpoint derivative is strictly nonzero analytically.
For `z=pi n^2e^(4p)`,
\[
 \phi_n'(p)=e^pe^{-z}(-8z^3+30z^2-15z).
\]
When `p>=h`, `z>=4 pi`, and `8z^2-30z+15>0`; hence every term
is decreasing there. Thus `A'(0+)=2^(-1/2)Phi'(h)<0`. Full modular
evenness gives `Phi'(0)=0`, so `B'(0+)=-A'(0+)>0`. Folding creates
opposite derivative cusps:
\[
 [a_t']_{0^-}^{0^+}=2A'(0+),\qquad
 [b_t']_{0^-}^{0^+}=2B'(0+)=-2A'(0+).                         \tag{22}
\]
Their sum is smooth. This is why high-frequency sector observations can
have algebraic endpoint terms although the complete observation has
rapid decay. The [06 endpoint calculation](../../06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md)
uses this exact interface to determine the signs of those terms.

There is an earlier, distinct distributional endpoint if the theta
parent is folded **before** applying the source differential operator.
Define `T_A(p)=e^p Theta(4e^(4p))`, `T_B=T-T_A`. Then
\[
 \frac{D_u^2-1}{16}T_A(|u|)
 =A(|u|)+\frac{T_A'(0+)}8\delta_0,
\]
\[
 \frac{D_u^2-1}{16}T_B(|u|)
 =B(|u|)+\frac{T_B'(0+)}8\delta_0,
 \qquad T_A'(0+)+T_B'(0+)=0.                                \tag{23}
\]
Equations (6) and (10) differentiate first and therefore do not insert
these folding-induced delta terms. An integration-by-parts proof that instead
differentiates the folded parents must keep them, including their
two-source products, until the complete cancellation is taken. At the
pairing lines `r=+s` and `r=-s`, the full source has matched derivatives;
individual sectors do not. Merely noting that those lines have measure
zero does not justify deleting their integration-by-parts endpoints.

The scope of this obstruction matters. The unfurled parity subtotal
`2^(-1/2)Phi_e(u+h)` is a different, smooth whole-line function; its
complement in `Phi_e(u)` need not be nonnegative. The cusps in (22) belong
to the **positive modular-folded sectors** constructed here. They do not
show that every other possible characteristic or matrix representation
has the same defect.

## 7. What the reduction does and does not establish

The two-coset identity now retains the unequal-scale coupling, both
source differential operators, the modular characteristic, zero axes,
both physical kernels and all cutoff payments. It also identifies the
complete new comparison to test: the two quadratic expressions (13),
with their endpoint cancellation, under stationarity of their sum.

Nothing in positive definiteness of the lattice matrix `Q`, or in
nonnegativity of (6), proves nonnegativity of (13). An autocorrelation
factorization of `J_0,J_1` remains unproved. The simple plan of treating
the positive source cosets as independently positive Fourier channels
must pass the nonzero cusp test (22); direction 06 evaluates that test.
This note establishes no uniform stationary sign and no RH implication.

The [checker](../numerics/check_rank_two_to_paired.py) and
[small execution record](../numerics/RANK_TWO_TO_PAIRED_RECORD_20261013.json)
verify the source algebra and enclose negative same-parity coset Fourier
responses for both kernels: folded sources at `t=0,x=60`, and distinct
unfolded sources at `t=0,x=0`. Their different definitions and full tail
payments are stated in the [numerics guide](../numerics/README.md).
These falsify the proposed separate-coset positivity, not positivity of
the complete kernels. The finite coupled-lattice and modular calibrations
are explicitly diagnostic; the negative signs use outward arithmetic.
Analytic convergence and endpoint arguments above do not depend on finite
floating-point agreement. No large derived data or manuscript snapshot
is created.
