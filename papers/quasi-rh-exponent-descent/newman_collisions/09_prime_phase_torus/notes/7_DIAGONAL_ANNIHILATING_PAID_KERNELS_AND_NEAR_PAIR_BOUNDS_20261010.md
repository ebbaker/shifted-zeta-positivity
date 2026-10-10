# Diagonal-annihilating paid kernels and macroscopic near-pair bounds

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an internal analytical
derivation, not independent mathematical validation. No numerical sweep
or sampled-height sign claim is used.

This continues the [centered collision reduction](2_CENTERED_COLLISION_JETS_AND_RATIO_PRODUCT_CORRELATIONS_20261010.md),
[paid ratio/product kernels](3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md),
and [common-factor smoothing and signed frontier](6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md).
It proves an exact candidate-paid extension whose four pair kernels vanish
on the diagonal, and a uniform absolute bound for a narrow macroscopic
pair band. The density-strengthened normalizer and its recomputed physical
payment are retained. Every other primitive, product, and mixed-block term
remains in the complete signed sum. A negative bound for that remaining
sum, collision exclusion, or RH is not proved.

The companion [product Poisson transform](8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md)
and [coupled Möbius frontier](9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md)
develop the next signed representations. The [central continuation](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md)
relates them to the prescribed stationary reflection.

## 1. Physical data, genuine candidates, and the threshold payment

Freeze the physical center, time, natural integer cutoff, centering, and
every coefficient below. Retain the complete sums on
\[
0<t\le1/20,\qquad 1\le\kappa\le3/2,\qquad
L=\kappa/t,\quad x=4\pi e^L,\quad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor.
\tag{1}
\]
Use the actual amplitude, phase, and frequency data of Notes 2 and 6:
\[
\begin{split}
w_n&=n^{-\sigma}e^{t\log^2 n/4},\qquad
\phi_n=\theta_t+T\log n,\qquad \rho_n=\log n-\mu,\\
\mu&=\Omega/c,\qquad \epsilon=d/c,\qquad A=-d\mu\in\mathbb R,\\
M_j&=\sum_{n\le N}w_n\rho_n^j e^{i\phi_n}=X_j+iY_j,
\qquad Z_1=Y_1+\epsilon X_1.
\end{split}
\tag{2}
\]
Here \(c\) is positive and uniformly bounded above and away from zero.
The two complete finite candidate equations obey
\[
X_0=F_N/2,\qquad e_1=F_N'/2=A X_0-cZ_1.
\tag{3}
\]
At an actual heat collision the approximation theorem gives the paid
constraints
\[
|X_0|\le a_0:=\eta_N/2,\qquad |e_1|\le L\eta_N/2,
\qquad
|Z_1|\le a_1:=\frac{(L+|A|)\eta_N}{2c}.
\tag{4}
\]
The \(\epsilon X_1\) term is retained; \(Y_1\) is not set to zero.

Throughout this note choose the density-strengthened coefficient of
Note 6, Section 10:
\[
\gamma_{\rm count}=\gamma+\frac{9\log x}{2D_0^2},\qquad
D_0=8\pi(4C_{\rm count}+1),\qquad
\Gamma=\Gamma_{\rm count}:=\gamma_{\rm count}/c^2.
\tag{5}
\]
The absolute imported counting constant \(C_{\rm count}\) is fixed.
Since \(\gamma=O(x^{-2})\), \(\Gamma=\Theta(L)\) as
\(t\downarrow0\), uniformly in the stated closed \(\kappa\)
interval. All algebra below holds for any real frozen \(\Gamma\);
the asymptotic comparisons use (5).

Set
\[
\mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2,
\quad g_2=-2c^2X_2,\quad g_3=2c^3Y_3,\quad g_4=2c^4X_4.
\tag{6}
\]
With the complete raw Bell residuals \(E_j\) of Note 2, retain
\(\widehat\delta_j=j!L^j\eta_N+E_j\), for \(j=2,3,4\), and
the recomputed measured physical payment
\[
\begin{split}
\widehat\Delta_{\rm count}={}&
4|g_3|\widehat\delta_3+2\widehat\delta_3^2\\
&+3\bigl(|g_2|\widehat\delta_4+|g_4|\widehat\delta_2
                    +\widehat\delta_2\widehat\delta_4\bigr)\\
&+|\gamma_{\rm count}|\bigl(2|g_2|\widehat\delta_2
                                    +\widehat\delta_2^2\bigr).
\end{split}
\tag{7}
\]
The old payment with \(\gamma\) cannot automatically be reused.
By Note 6, equations (38)–(39), this payment has the uniform admissible
upper-budget scale
\[
\widehat\Delta_{\rm count}
=O\left(L^4N^{-\kappa/4}+L^6N^{-(\kappa+4)/4}\right)=o(1).
\tag{8}
\]
An actual all-real threshold collision in the range of the imported
counting implication has its strengthened physical threshold quadratic
nonnegative. Therefore a sufficient arithmetic exclusion is still
\[
\mathcal K+\widehat\Delta_{\rm count}/(4c^6)<0.
\tag{9}
\]
This note supplies a paid representation for the left side; it does not
establish (9).

## 2. An exact candidate-null extension and its payment

Define the complete finite-moment expression
\[
\boxed{
\mathcal J^\dagger=
\mathcal K+X_0(\Gamma X_4-3X_6+2\epsilon Y_6)-2Z_1Y_5.
}
\tag{10}
\]
It agrees with \(\mathcal K\) when both exact finite candidates
\(X_0=Z_1=0\) hold. At a paid actual candidate, the exact difference
is
\[
\mathcal K-\mathcal J^\dagger
=X_0(3X_6-\Gamma X_4-2\epsilon Y_6)+2Z_1Y_5.
\tag{11}
\]
Thus a measured, complete candidate payment is
\[
\Pi^\dagger_{\rm box}
=a_0|3X_6-\Gamma X_4-2\epsilon Y_6|+2a_1|Y_5|,
\qquad
|\mathcal K-\mathcal J^\dagger|\le\Pi^\dagger_{\rm box}.
\tag{12}
\]
The correlated constraint (3) also gives the valid alternative
\[
\Pi^\dagger_{\rm slab}
=\frac{\eta_N}{2}
 \left|3X_6-\Gamma X_4-2\epsilon Y_6+\frac{2A}{c}Y_5\right|
 +\frac{L\eta_N}{c}|Y_5|.
\tag{13}
\]
Indeed substitute \(Z_1=(AX_0-e_1)/c\) in (11), then apply the
two bounds in (4). Either bound, or their minimum, is admissible; a signed
estimate must retain the chosen payment. Certified moment intervals can
replace the displayed absolute moment values by rigorous upper endpoints.

For completeness, let
\[
B_j=\sum_{n\le N}w_n|\rho_n|^j.
\tag{14}
\]
The complete centered moment bound of Note 6, equation (15) with common
factor \(u=1\), gives for every fixed \(j\), including \(j=5,6\),
\[
B_j\le C_jNw_N=O_j(e^{\mathfrak a/t}),\qquad
\mathfrak a=\kappa(4-\kappa)/16.
\tag{15}
\]
Consequently (12) is bounded by
\[
\Pi^\dagger_{\rm box}
\le\frac{\eta_N}{2}
       \{(3+2|\epsilon|)B_6+|\Gamma|B_4\}
       +\frac{(L+|A|)\eta_N}{c}B_5.
\tag{16}
\]
The physical estimates \(\epsilon=O(t/x)\),
\(A=-d\mu=O(x^{-1})\), and \(\Gamma=O(L)\) imply
\[
\Pi^\dagger_{\rm box}
=O\bigl(L\eta_N e^{\mathfrak a/t}\bigr)
=O\left(LN^{-\kappa/4}\right)=o(1).
\tag{17}
\]
For the second equality use the actual complete approximation bound
\(\eta_N=O(e^{-\mathfrak b/t})\),
\(\mathfrak b=\kappa(\kappa+4)/16\), and
\(\mathfrak a-\mathfrak b=-\kappa^2/8\), together with
\(\log N=\kappa/(2t)+o(1)\). It is an upper bound; the measured
payment is (12) or (13).

Only the two genuine lower-jet candidate tolerances are used in this
extension. \(X_6,Y_6,Y_5\) are exact finite logarithmic moments and
are bounded by (15); they are not identified with genuine fifth or sixth
raw spatial derivatives. No new approximation theorem or unpaid fifth-
or sixth-jet tolerance is introduced. Note 6's degree obstruction for the
older dual family applies to upper features of degree at most four.
Expression (10) extends that family by \(X_6,Y_6,Y_5\), so that
restriction does not apply here.

## 3. The four exact coupled pair kernels

For an ordered pair write
\[
a=\rho_n,\qquad b=\rho_m,\qquad h=a+b,\qquad \delta=a-b,
\]
\[
\Delta_{nm}=\phi_n-\phi_m=T\log(n/m),\qquad
\Sigma_{nm}=\phi_n+\phi_m=2\theta_t+T\log(nm).
\tag{18}
\]
All sums in this section run over ordered pairs \(1\le n,m\le N\).
Then exactly
\[
\begin{split}
\mathcal J^\dagger=\sum_{n,m\le N}w_nw_m\{&
D_c^\dagger(n,m)\cos\Delta_{nm}
 +D_s^\dagger(n,m)\sin\Delta_{nm}\\
&+P_c^\dagger(n,m)\cos\Sigma_{nm}
 +P_s^\dagger(n,m)\sin\Sigma_{nm}\},
\end{split}
\tag{19}
\]
where
\[
\boxed{
\begin{aligned}
D_c^\dagger&=\frac14h^2\delta^2(\Gamma-2h^2-\delta^2),\\
P_c^\dagger&=\frac14h^2\delta^2(\Gamma-h^2-2\delta^2),\\
D_s^\dagger&=\frac\epsilon2(a-b)(a^5+b^5),\\
P_s^\dagger&=\frac\epsilon2(a-b)(a^5-b^5).
\end{aligned}}
\tag{20}
\]

Here is a derivation that checks the ordered-pair normalization and the
difference-sine orientation. Symmetrize every cosine-cosine and
sine-sine term in the expansion of (10). Using invariance of the full
ordered sum under exchanging \(n,m\), its expansion is the ordered sum
of
\[
R_{nm}\cos\phi_n\cos\phi_m
 +S_{nm}\sin\phi_n\sin\phi_m
 +2C_{nm}\cos\phi_n\sin\phi_m.
\tag{21}
\]
The coefficients are
\[
\begin{split}
R_{nm}={}&-\Gamma a^2b^2
 +\frac32(a^2b^4+a^4b^2)
 +\frac\Gamma2(a^4+b^4)-\frac32(a^6+b^6),\\
S_{nm}={}&2a^3b^3-ab^5-a^5b,\\
C_{nm}={}&\epsilon(b^6-ab^5)=\epsilon b^5(b-a).
\end{split}
\tag{22}
\]
For example, \(2\epsilon X_0Y_6-2\epsilon X_1Y_5\)
is precisely the ordered sum of
\(2\epsilon(b^6-ab^5)\cos\phi_n\sin\phi_m\).
Equivalently its symmetric bilinear summand has cross part
\(C_{nm}\cos\phi_n\sin\phi_m+
C_{mn}\sin\phi_n\cos\phi_m\). Applying product-to-sum to this
symmetric summand gives
\[
D_c^\dagger=(R+S)/2,\quad P_c^\dagger=(R-S)/2,
\quad D_s^\dagger=(C_{mn}-C_{nm})/2,
\quad P_s^\dagger=(C_{nm}+C_{mn})/2.
\tag{23}
\]
The sign follows from
\(\sin(\phi_n-\phi_m)=\sin\phi_n\cos\phi_m
-\cos\phi_n\sin\phi_m\). In particular
\[
C_{mn}=\epsilon a^5(a-b),\quad
C_{mn}-C_{nm}=\epsilon(a-b)(a^5+b^5),\quad
C_{mn}+C_{nm}=\epsilon(a-b)(a^5-b^5).
\tag{24}
\]

For the cosine factors use
\[
\begin{split}
R_{nm}&=(a^2-b^2)^2
 \left\{\frac\Gamma2-\frac32(a^2+b^2)\right\},\\
S_{nm}&=-ab(a^2-b^2)^2.
\end{split}
\tag{25}
\]
Since \(a^2-b^2=h\delta\),
\(a^2+b^2=(h^2+\delta^2)/2\), and
\(ab=(h^2-\delta^2)/4\), equations (23) and (25) give the
first two rows of (20), with no remaining multiplicative factor.

Both cosine kernels and the product sine kernel are symmetric in
\((n,m)\); the difference sine kernel is antisymmetric. Its phase
\(\sin\Delta_{nm}\) is also antisymmetric, so its ordered sum
does not cancel under exchanging the indices. On \(n=m\),
\(\delta=0\), and all four kernels in (20) vanish individually.
The diagonal is therefore removed exactly in both channels.

The prescribed pair weight remains
\[
w_nw_m=(nm)^{-\sigma}
 \exp\{t\log^2(nm)/8+t\log^2(n/m)/8\}.
\tag{26}
\]
Equation (19) retains one actual common \(T\) and carrier
\(\theta_t\). Grouping the difference coefficients by
\(n=ja,m=jb\), \((a,b)=1\), and the product coefficients by
\(nm=k\), is exact as in Notes 2–3. The ratio diagonal
\((a,b)=(1,1)\) is now zero. For a product square, only its actual
diagonal divisor pair is zero; off-diagonal divisors of the same square
remain. Neither product channel is discarded.

## 4. Absolute near-pair theorem on a macroscopic interval

Fix \(\lambda\in(0,1)\), and let \(1\le H\le N\).
For sufficiently small \(t>0\), uniformly in
\(\kappa\in[1,3/2]\), consider any subset of ordered pairs
\[
\mathcal E_{\lambda,H}
 \subseteq\{(n,m):\lambda N\le n,m\le N,
                            \ |n-m|\le H\}.
\tag{27}
\]
Define the absolute cosine and sine envelopes of this subset by
\[
\begin{split}
\mathsf B_c&=\sum_{(n,m)\in\mathcal E_{\lambda,H}}
   w_nw_m(|D_c^\dagger|+|P_c^\dagger|),\\
\mathsf B_s&=\sum_{(n,m)\in\mathcal E_{\lambda,H}}
   w_nw_m(|D_s^\dagger|+|P_s^\dagger|).
\end{split}
\tag{28}
\]
These envelopes bound the absolute value of the corresponding signed
near-pair contributions in (19). There are constants depending only on
the fixed \(\lambda\) and the uniform physical reserves such that
\[
\boxed{
\begin{aligned}
\mathsf B_c&\le C_\lambda(1+|\Gamma|)w_N^2\frac{H^3}{N}
 =C_\lambda(1+|\Gamma|)(Nw_N)^2(H/N)^3,\\
\mathsf B_s&\le C_\lambda|\epsilon|w_N^2H^2.
\end{aligned}}
\tag{29}
\]
More precisely the product sine portion alone is at most
\(C_\lambda|\epsilon|w_N^2H^3/N\).

To prove the uniform estimates, first
\(\mu=\log N+O(N^{-1})\) gives
\[
|\rho_n|,|\rho_m|\le R_\lambda:=1+\log(1/\lambda),\qquad
|\delta|=|\log(n/m)|\le\frac{|n-m|}{\lambda N}.
\tag{30}
\]
The last inequality is the mean value theorem for the real logarithm.
For \(y=\log(N/n)\in[0,\log(1/\lambda)]\), the exact physical
weight ratio is
\[
w_n/w_N=\exp\{c_\sigma y+t y^2/4\},\qquad
c_\sigma=\sigma-(t/2)\log N=1/2+o(1).
\tag{31}
\]
Hence \(w_n,w_m\le C_\lambda w_N\), uniformly. Equations
(20) and (30) give the pointwise bounds, with \(k=|n-m|\),
\[
|D_c^\dagger|+|P_c^\dagger|
 \le C_\lambda(1+|\Gamma|)k^2/N^2,
\quad
|D_s^\dagger|\le C_\lambda|\epsilon|k/N.
\tag{32}
\]
Also \(a^5-b^5=(a-b)\sum_{j=0}^4a^{4-j}b^j\), so
\[
|P_s^\dagger|\le C_\lambda|\epsilon|k^2/N^2.
\tag{33}
\]
For each positive integer gap \(k\), at most \(2N\) ordered
pairs have \(|n-m|=k\). The gap-zero terms vanish. Therefore
\[
\sum_{\mathcal E_{\lambda,H}}\frac{|n-m|^2}{N^2}
 \le\frac2N\sum_{k=1}^{\lfloor H\rfloor}k^2
 \le C H^3/N,
\quad
\sum_{\mathcal E_{\lambda,H}}\frac{|n-m|}{N}
 \le2\sum_{k=1}^{\lfloor H\rfloor}k\le C H^2.
\tag{34}
\]
Combine (31)–(34). Finally \(H^3/N\le H^2\) for
\(H\le N\), proving (29). This proof is an absolute bound for
the stated band; it invokes no cancellation or independent phase choice.

Taking \(\lambda=1/2\) covers the requested macroscopic block
\([N/2,N]\). Taking \(\lambda=1/4\) gives the same theorem
with a different fixed constant and covers the near pairs crossing the
physical boundary between
\(\mathcal B=\{\lfloor N/2\rfloor+1,\ldots,N\}\) and
\(\mathcal C=\{1,\ldots,\lfloor N/2\rfloor\}\).
For \(H=\lceil N^{1/2}\rceil\) and sufficiently large \(N\),
every such crossing pair has minimum index at least \(N/4\).
Pairs with minimum index below \(N/4\) are outside this bound and
remain exact in the complementary signed expression.

## 5. Payment scale and the remaining coupled signed criterion

For the genuine physical coefficients, Note 6 gives
\[
(Nw_N)^2\asymp N^{1-\kappa/4},\qquad
x\asymp N^2,\qquad \epsilon=O(t/N^2).
\tag{35}
\]
At \(H=\lceil N^{1/2}\rceil\), equations (5), (29), and
(35) yield
\[
\mathsf B_c=O\left(LN^{-1/2-\kappa/4}\right),\qquad
\mathsf B_s=O\left(tN^{-2-\kappa/4}\right).
\tag{36}
\]
The separate product sine bound is
\(O(tN^{-5/2-\kappa/4})\). Both envelopes are uniformly
\(o(N^{-\kappa/4})\); in particular they are below the displayed
physical upper-budget scale \(L^4N^{-\kappa/4}\). The full
candidate payment (17) is also smaller than that displayed scale by a
factor \(O(L^{-3})\). These are comparisons with admissible upper
scales, not claims that any measured physical payment has a positive
lower bound.

Let \(\mathcal J^\dagger_{\rm near}\) denote exactly the portion
of (19) with
\(\min(n,m)\ge N/4\) and \(|n-m|\le H\), and define
\(\mathcal J^\dagger_{\rm rem}
=\mathcal J^\dagger-\mathcal J^\dagger_{\rm near}\).
The four kernels, both actual phases, and the true pair weight remain
together in this difference. If an actual-phase analytical bound proves
\(\mathcal J^\dagger_{\rm rem}\le U_{\rm rem}\), then
\[
\mathcal K\le U_{\rm rem}+\mathsf B_c+\mathsf B_s+\Pi^\dagger,
\tag{37}
\]
where \(\Pi^\dagger\) is (12), (13), or their minimum. The resulting
sufficient threshold exclusion is the fully paid inequality
\[
\boxed{
U_{\rm rem}+\mathsf B_c+\mathsf B_s+\Pi^\dagger
 +\widehat\Delta_{\rm count}/(4c^6)<0.
}
\tag{38}
\]
If a subsequent Poisson, Möbius, or other signed transformation estimates
\(U_{\rm rem}\), its proved error must be added to (38). A complete
alternative representation of the same sum is not a disjoint new term.

The complement in (37) includes every separated pair and every retained
low-index near pair, and thus all remaining
\(\mathcal B\times\mathcal B\),
\(\mathcal B\times\mathcal C\),
\(\mathcal C\times\mathcal B\), and
\(\mathcal C\times\mathcal C\) terms. No sign for
\(U_{\rm rem}\) is obtained here. The factor \(\delta^2\)
permits a narrow band to be paid; it does not make the complete primitive
or product frontier an absolutely small tail.

## 6. Reflection parity and the actual drift

Consider the algebraic antilinear reflection
\[
\mathcal R:M_j\longmapsto(-1)^j\overline{M_j}.
\tag{39}
\]
Its real-coordinate action is
\[
X_j\longmapsto(-1)^jX_j,\qquad
Y_j\longmapsto(-1)^{j+1}Y_j.
\tag{40}
\]
Thus even cosine moments and odd sine moments are fixed, while odd
cosine moments and even sine moments change sign. In particular
\(X_0,X_2,X_4,X_6,Y_1,Y_3,Y_5\) are fixed, and
\(X_1,Y_6\) change sign. The base expression \(\mathcal K\)
is invariant for the same frozen \(\Gamma\).

With the physical \(\epsilon\) held fixed,
\[
Z_1\longmapsto Y_1-\epsilon X_1=Z_1-2\epsilon X_1,
\]
and the complete correction transforms exactly as
\[
\mathcal J^\dagger(\mathcal R M;\epsilon)
=\mathcal J^\dagger(M;\epsilon)
 -4\epsilon X_0Y_6+4\epsilon X_1Y_5
=\mathcal J^\dagger(M;-\epsilon).
\tag{41}
\]
This follows directly by writing its drift-containing part as
\(2\epsilon(X_0Y_6-X_1Y_5)\). Equivalently, if the algebraic
reflection also reverses the drift parameter \(\epsilon\), then
\(Z_1\) and \(\mathcal J^\dagger\) are covariant invariants.
An actual physical center does not supply an arbitrary sign change of
its drift; the fixed-\(\epsilon\) discrepancy in (41) must instead
be retained or paid. The complete moment envelope gives the uniform
absolute payment
\[
4|\epsilon|\bigl(|X_0Y_6|+|X_1Y_5|\bigr)
\le4|\epsilon|(B_0B_6+B_1B_5)
=O\left(tN^{-1-\kappa/4}\right).
\tag{42}
\]

The [central stationary-reflection note](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md)
derives when the prescribed leading stationary coefficients approximate
(39), with their own mismatch and endpoint obligations. This parity
calculation alone does not identify a reflected finite cutoff with the
original finite sum, and it does not change the sign of the base threshold
quadratic.

## 7. Review scope and next proof obligation

The new proved statements are the exact extension and measured payment
(10)–(17), the complete four-kernel identity and diagonal cancellation
(19)–(25), the macroscopic near-pair theorem (29), its physical payment
scale (36), and the reflection/drift identities (40)–(42).

The next signed theorem must control the retained primitive/product
contribution and its boundary terms strongly enough for (38). It must
use the actual prescribed heat weights and one common height, preserve
both channels and all mixed terms, and use the genuine complete candidate
constraints. No separate candidate equation is imposed on a block or
sublattice. The counting threshold's hypotheses, higher multiplicities,
small-curvature candidates, complementary parameters, and the small-time
endpoint remain obligations of the eventual uniform collision argument.

Cross-audit should check the ordered-pair factors and especially (24),
the finite-moment status of the fifth/sixth-degree features, the literal
macroscopic range in (27), the gap count (34), recomputation of the
physical normalizer payment in (7), and the fixed-drift action (41).
