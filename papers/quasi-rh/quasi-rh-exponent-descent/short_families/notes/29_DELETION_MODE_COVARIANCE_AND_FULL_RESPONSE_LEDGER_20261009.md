# Local deletion modes survive scalar coherent mean subtraction

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: a new actual-block covariance obstruction, an exact conditional
mean/covariance/complement ledger for the full squarefree response, and
finite exact checks. The analytic block asymptotic imports Note 24's
fixed-field prime ideal theorem. This is internal validation, not
independent specialist review or formal verification. No bound or lower
bound for the full signed response is established.

[Note 27](27_COHERENT_COVARIANCE_AND_FINITE_SPAN_BARRIER_20261009.md)
restricts its constant coherent block to rows coprime to the cofactor.
The broader inner sixth-power ball has another obligation: the physical
deletion zeros make that same actual block vary with the small primes
dividing the row. Subtracting its optimal scalar mean leaves energy
\(D^{16/15}\) up to logarithms. Thus a broader compensation argument must
match local deletion modes, not only a global coherent mean. The
conditional means below retain every other product shape and the adaptive
cutoff; their within-cell covariance and the full row complement have
separate, explicit payments.

## 1. Enlarge the actual coherent row set, without changing the block

Use Note 24's good ideal monoid, trivial permitted fixed twist \(\nu=1\),
physical deletion zeros, fixed nonzero complex mean-zero profile \(W\),
and \(H=D^{2/5}\), \(z=\sqrt{CD}\), \(Y_u=D^{9/20}/L_u\).
Fix a nonunit squarefree good ideal
\[
 P=\prod_{i=1}^Jp_i,\qquad q_i=Np_i.
\]
Here \(P,J\) are fixed. Distinct prime ideals of equal norm remain
different indices. Define
\[
 X=D^{1/15},\qquad
 \mathcal C(D)=\{u=v^6:0<Nv\le X\},\qquad
 w_u=D^{-1}\Phi(Nu/H),\qquad m=\sum_{u\in\mathcal C}w_u.
 \tag{1}
\]
Count each physical sixth-power image once. For a subset \(S\subseteq[J]\)
let \(\mathcal C_S\) be the rows for which precisely the primes indexed
by \(S\) divide \(v\); this is well defined on a sixth-power image.
Write \(m_S=\sum_{\mathcal C_S}w_u\), and let
\[
 \pi_S=\prod_{i\in S}q_i^{-1}
       \prod_{i\notin S}(1-q_i^{-1}).
\]
Elementary weighted Eisenstein lattice counting gives
\[
 m\asymp_\Phi D^{-14/15},\qquad
 \frac{m_S}{m}=\pi_S+O_{P,\Phi}(D^{-1/30}).                 \tag{2}
\]
To justify the weighted version, apply finite inclusion-exclusion to the
counts in the fixed principal ideal lattices and then partial summation
with \(g(t)=\Phi(t^6)\), \(0\le t\le1\). Each lattice has main term
proportional to \(X/Nd\) and error \(O_P(\sqrt X+1)\). Every nonzero
sixth-power image has six unit-related roots in this field; the radial
weight and all divisibility conditions are invariant under these units,
so this common multiplicity cancels in the ratios. This is the same
elementary lattice input as Note 24, not a growing-modulus equidistribution
theorem. In particular every cell has positive mass eventually.

Let \(\mathcal B_{u,P}\) be exactly Note 24's original projection onto
total ideals \(bqr\), \(b\mid P\), with the two distinct large prime
factors bounded by \(z\). On all rows (1), not only the coprime ones,
\[
 \boxed{\mathcal B_{u,P}=\mathcal P_{P_S,W}(D)
             \quad(u\in\mathcal C_S),\qquad
 P_S=\prod_{i\notin S}p_i.}                              \tag{3}
\]
Here \(\mathcal P_{M,W}\) is the exact ordered-prime-pair sum in Note 24.
Indeed, uniformly on (1), \(Y_{v^6}\gg D^{23/60}>NP\), while every
supported pair prime has norm \(\gg_P D^{1/2}>Y_{v^6}\) and \(>Nv\).
Thus \(t_{Y_{v^6}}(bqr)=2\mu_K(b)\), and the physical character equals
\(\mathbf1_{(b,v)=1}\). The cofactors meeting \(S\) are deleted; all
remaining cofactors occur with their actual signs. The exclusion of the
large pair primes from \(P\) is automatic on the support, even for the
smaller cofactor \(P_S\). Ordered pairs absorb the factor two. No
deletion zero has been replaced by one, and no coefficient is redesigned.

## 2. A scalar mean subtraction leaves a positive covariance

Let \(k_0\ge1\) be the first nonzero profile moment from Note 24, put
\(B=\log z\), and define its nonzero common leading amplitude
\[
 A_D=\frac{D\alpha_{k_0}M_{k_0}(W)}{B^{k_0+1}},\qquad
 \alpha_k=\sum_{j=1}^k2^{-(k-j)}/j.
\]
The fixed-cofactor asymptotic, applied to every cell of (3), is
\[
 \mathcal B_{u,P}=A_D f_P(S)+O_{P,W}(|A_D|/B),\qquad
 f_P(S)=\prod_{i\notin S}(1-q_i^{-1}).                  \tag{4}
\]
Its PNT and removed-diagonal errors are smaller than this displayed
logarithmic error. The profile may be complex: \(A_D\) is complex and
the factors \(f_P(S)\) are positive real numbers.

Under the independent model measure \(\pi\), the indicator
\(Z_i=\mathbf1_{i\in S}\) has mean \(\rho_i=1/q_i\). Set
\[
 a_i=1-\frac1{q_i}+\frac1{q_i^2},\qquad
 s_i=\frac{\sqrt{q_i-1}}{q_i^2}.
\]
The mean and variance of \(f_P=\prod_i(1-1/q_i+Z_i/q_i)\) are
\[
 E_\pi f_P=\prod_i a_i,\qquad
 v_P=\prod_i(a_i^2+s_i^2)-\prod_i a_i^2>0.              \tag{5}
\]
The last inequality follows because every \(s_i>0\) and \(J\ge1\).
Combining (2)--(5) and the exact least-squares identity gives
\[
 \boxed{\inf_{c\in\mathbb C}\sum_{u\in\mathcal C}w_u
       |\mathcal B_{u,P}-c|^2
       =m|A_D|^2\{v_P+O_{P,W,\Phi}(B^{-1})
                         +O_{P,\Phi}(D^{-1/30})\}
       \asymp_{P,W,\Phi}\frac{D^{16/15}}{(\log D)^{2k_0+2}}.}
                                                               \tag{6}
\]
The minimizing scalar is the *actual* weighted mean, so (6) rules out
even an exactly computed scalar mean as a repair of this block. This
does not rule out an arithmetic correction that depends on the row and
comes from other total products.

For one good prime \(p\), \(q=Np\), the conclusion is especially direct.
Let \(\rho_D=m_{\{p\}}/m\). The block is \(\mathcal P_{p,W}\) on
\(p\)-free rows and \(\mathcal P_{1,W}\) on \(p\)-divisible rows. Hence
\[
 \inf_c\sum_{\mathcal C}w_u|\mathcal B_{u,p}-c|^2
 =m\rho_D(1-\rho_D)|\mathcal P_{1,W}-\mathcal P_{p,W}|^2,
 \quad
 \mathcal P_{1,W}-\mathcal P_{p,W}
     =A_D/q+O_{p,W}(|A_D|/B).                          \tag{7}
\]
The variance coefficient is exactly \((q-1)/q^4\) at leading order.
Unlike the constant coprime-row obstruction, this is a physical
deletion-induced covariance across the enlarged actual row set.

## 3. The full arithmetic compensation must match every deletion mode

Now restore the *complete* squarefree response from Notes 21--22:
\[
 T_u=T_{u,\mathrm{sf}}
  =\sum_{n\ \mathrm{sf}}t_{Y_u}(n)\lambda_u(n)W(Nn/D),\qquad
 t_Y(n)=\mu_K(n)+\sum_{\substack{d\mid n\\Nd\le Y}}(-2)^{\omega(d)}.
                                                               \tag{8}
\]
The coefficient formula applies on this annulus with \(Y_u<z\).
Write \(R_u=T_u-\mathcal B_{u,P}\). For every cell define actual means
\[
 r_S=m_S^{-1}\sum_{\mathcal C_S}w_uR_u,
 \qquad c_S=\mathcal P_{P_S,W}+r_S,
 \qquad V_S=\sum_{\mathcal C_S}w_u|R_u-r_S|^2.
\]
Because the block is *exactly* constant in each cell, the exact complete
row partition is
\[
 \boxed{\sum_{u\ne0}w_u|T_u|^2
       =\sum_Sm_S|c_S|^2+\sum_SV_S+E_{\rm out},\qquad
 E_{\rm out}=\sum_{u\notin\mathcal C}w_u|T_u|^2.}       \tag{9}
\]
In particular no other product shape is estimated separately, and its
cross terms with the block remain in \(c_S\) and \(V_S\). The outer
energy is the actual squarefree energy on all other physical rows,
including other principal rows and exterior sixth-power rows.

All conditional means are literal arithmetic expressions. On coherent
rows put
\[
 b_u(n)=t_{Y_u}(n)\mathbf1_{(v,n)=1},\qquad
 \beta_S(n)=m_S^{-1}\sum_{\mathcal C_S}w_ub_u(n).
\]
Then \(c_S=\sum_n\beta_S(n)W(Nn/D)\). The cutoff depends on the
actual \(L_u\) and is retained inside \(\beta_S\); no fictitious fixed
cutoff is substituted. Equivalently,
\[
 V_S=\sum_{n,n'}W(Nn/D)\overline{W(Nn'/D)}\,
 \sum_{u\in\mathcal C_S}w_u
       (b_u(n)-\beta_S(n))(b_u(n')-\beta_S(n')).          \tag{10}
\]
For the explicitly fixed twist \(\nu=1\), both \(b_u(n)\) and
\(\beta_S(n)\) are real on these coherent rows, so the second factor
in (10) requires no additional complex conjugate. This whole quadratic
form is positive semidefinite. It contains all
cross-product-shape covariances, including unsaturated and balanced
triple products; diagonal or separately positive shape bounds cannot
replace it in a claimed contraction.

A convenient explicit mode interface uses the orthonormal product basis
\[
 e_I(S)=\prod_{i\in I}\frac{Z_i-\rho_i}
                              {\sqrt{\rho_i(1-\rho_i)}},\qquad
 \widehat c_I=\sum_S\pi_Sc_Se_I(S),\qquad
 \widehat r_I=\sum_S\pi_Sr_Se_I(S).
\]
Let \(\delta_D=\max_S|m_S/(m\pi_S)-1|=O_{P,\Phi}(D^{-1/30})\).
Parseval is exact for \(\pi\), so
\[
 (1-\delta_D)m\sum_I|\widehat c_I|^2
 \le\sum_Sm_S|c_S|^2
 \le(1+\delta_D)m\sum_I|\widehat c_I|^2.                \tag{11}
\]
These are transforms of the *actual* conditional means; only the measure
comparison uses a lattice asymptotic. The exact packet mode to cancel is
\[
 B_I(D)=\sum_S\pi_S\mathcal P_{P_S,W}(D)e_I(S),\qquad
 \widehat c_I=B_I(D)+\widehat r_I,
\]
with the informative leading asymptotic
\[
 B_I(D)=A_D\left(\prod_{i\in I}s_i\right)
                   \left(\prod_{i\notin I}a_i\right)
               +O_{P,W}(|A_D|/B).                     \tag{12}
\]
Every fixed-prime mode is nonzero eventually, including nonempty \(I\).

If the desired full squarefree energy is
\(Q_D=C_\varepsilon D^{4/5+\varepsilon}\), (9)--(11) force
\[
 \sum_I|B_I(D)+\widehat r_I|^2
        \le\frac{Q_D}{(1-\delta_D)m},\qquad
 \sum_SV_S+E_{\rm out}\le Q_D.                         \tag{13}
\]
Thus each fixed mode must be matched to absolute accuracy
\(O_{P,\Phi,\varepsilon}(D^{13/15+\varepsilon/2})\), or relative
accuracy
\(O(D^{-2/15+\varepsilon/2}(\log D)^{k_0+1})\).
Matching only \(I=\varnothing\) leaves all the deletion modes unpaid.
Condition (13) is necessary; allocating total bounds to the three
nonnegative terms in (9) with sum at most \(Q_D\) is sufficient.

For the single-prime case there is an entirely exact two-mode form.
Write \(r_0,r_1\) for the \(p\)-free and \(p\)-divisible means and
\(\bar r=(1-\rho_D)r_0+\rho_Dr_1\). Then
\[
 \begin{split}
 \sum_{u\ne0}w_u|T_u|^2={}&m\left|
   (1-\rho_D)\mathcal P_{p,W}+\rho_D\mathcal P_{1,W}+\bar r
                           \right|^2\\
 &+m\rho_D(1-\rho_D)
       |\mathcal P_{1,W}-\mathcal P_{p,W}+r_1-r_0|^2
       +V_0+V_1+E_{\rm out}.                          \tag{14}
 \end{split}
\]
The new required signed estimate is specifically a conditional-mean
contrast \(r_1-r_0\approx-(\mathcal P_{1,W}-\mathcal P_{p,W})\),
in addition to the global mean cancellation. This contrast can receive
compensation from any of the original product shapes. It is not supplied
by deleting the row-dependent cutoff or replacing the character mask.

There is a direct complete arithmetic form of the full contrast. Since
\(\beta_1(n)=0\) for \(p\mid n\), it is exactly
\[
 c_1-c_0
 =\sum_{p\nmid n}W(Nn/D)\{\beta_1(n)-\beta_0(n)\}
  -\sum_{p\mid n}W(Nn/D)\beta_0(n).                    \tag{15}
\]
Both sums range over all squarefree total ideals on the profile. The
first term retains the conditional cutoff distribution and deletion by
every other prime; the second retains all product shapes removed by
\(p\). Thus the contrast cannot be replaced by a small-prime density
factor without also controlling the adaptive-cutoff and other-mask term.

## 4. What is paid, and what remains unproved

The row partition (9) and the Fourier interface include the whole inner
sixth-power ball. There is no omitted coherent divisibility stratum and
no projection norm charged twice. Existing Notes 17 and 20 already pay
the original small response with rapid decay and the nonsquarefree
response with exponent \(19/24<4/5\) (gap \(1/120\)); combining those
with a proved squarefree bound would finish that reduction. They do
*not* pay \(E_{\rm out}\), which is another part of the squarefree
response. Its required \(D^{4/5+\varepsilon}\) bound remains an explicit
obligation, alongside the conditional centered form (10).

The fixed-field PNT is enough to prove the leading block covariance (6).
Its absolute error \(De^{-c\sqrt{\log D}}\) is not a bound of order
\(D^{13/15+\varepsilon/2}\) when \(\varepsilon<4/15\). Likewise the
finite logarithmic approximation (12) is far too coarse to certify
(13). An arithmetic compensation proof must match the *exact* modes
\(B_I(D)\), or prove a signed combined error at the required power. An
asymptotic cancellation of their leading coefficients is insufficient.

This is progress from scalar coherent means to conditional arithmetic
means and a concrete deletion covariance. It is still a necessary
interface and a method obstruction. Neither (6) nor (7) proves that the
full \(T_u\) has large energy: the original remainder may cancel both
the scalar mode and every deletion mode. No positive lower bound for
the whole quadratic form is inferred from a selected block.

The next useful checkpoint is a native signed estimate for at least the
single-prime contrast in (14), together with its actual within-cell
variance and a complementary-row payment. Another scalar mean
subtraction or another finite cofactor difference would not provide it.

## 5. Verification

The [checker](../../numerics/check_deletion_mode_covariance.py) and
[record](../../numerics/deletion_mode_covariance_record_20261009.json)
verify exact rational tensor expansions, product-measure Parseval,
deletion-mask coefficients for genuine finite saturated pair packets,
least-squares and full-response decompositions with complex vectors,
measure-comparison inequalities, and the rational exponent ledger.
Equal-norm distinct prime symbols are included. The finite packets are
algebraic checks of the actual coefficient identity, not a numerical
model of its unbounded prime-ideal asymptotic. The checker does not
certify the PNT, the unbounded lattice asymptotic, or any estimate for
(10), (13), or \(E_{\rm out}\).

Two fresh runs passed 6,799 exact assertions and reproduced the small
record byte for byte. A separate same-model read-through by the parent
agent checked the block deletion identity, variance coefficient, fixed
prime lattice weights, exact-versus-leading mode distinction and the
unpaid complement. This remains internal validation.
