# A cofactor-inverse compensation block and its limitation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal research scout, not independent specialist validation.

This note gives an actual compensated block with arbitrarily small full
Schwartz-weighted energy. Its proof combines a finite Möbius inverse with
the already recorded zero-integral completion estimate. It holds for
complex physical twists, deletion zeros, and bounded row-dependent
coefficient selectors. The controlled block occupies a constant edge of
one truncated Möbius factor. It does not produce a new power estimate for
the full tail, and its algebra is equivalent to an asymmetric change of
factor cutoffs.

## 1. Setting and imported estimates

Keep the good ideal monoid, physical characters, and full nonnegative
Schwartz row weight of the organized short-family manuscript. Choose fixed
constants
\[
 0<c<C_0<C,\qquad \operatorname{supp}W\subset[c,C_0],
 \qquad \int_0^\infty W(t)\,dt=0.
\tag{1}
\]
The profile may be complex. The derivative profiles
\(W=(1+t\partial_t)V\) provide the detector class considered in the
manuscript. Let
\[
 z=\sqrt{CD},\qquad A_D=C_0D/z,\qquad
 Y_u=D^{1-\theta}/L_u,\qquad 0<\theta<1.
\tag{2}
\]
The full response uses completely multiplicative
\(\lambda_u(n)=\nu(n)\chi_n(u)\), including every deletion zero.
Write
\[
 S_u(X)=\sum_m\lambda_u(m)W(Nm/X).
\tag{3}
\]

The explicit imported completion and weighted-mass estimates are
\[
 |S_u(X)|\ll_{M,W}\tau(E_u)\sqrt{Q_u}(L_u/X)^M
 \quad(X>0,\ M\ge0),
\tag{4}
\]
\[
 \sum_{u\ne0}\Phi(Nu/H)
       \frac{\tau(E_u)^2Q_u}{L_u^2}\ll_\delta H^\delta
 \quad(H\ge1,\ \delta>0).
\tag{5}
\]
There is no principal term in (4), precisely because of (1).
Equations (4)--(5) retain the source status of the manuscript's native
primitive Poisson package and radical-weighted Euler-product deduction.
No conductor-uniform Möbius bound is assumed.

## 2. A pointwise cofactor inverse

Let \(\sigma_u(a)\) be any complex coefficient selector with
\[
 |\sigma_u(a)|\le1,\qquad
 \sigma_u(a)=0\ \text{unless}\ A_D\le Na\le z.
\tag{6}
\]
It may depend on \(u,D\), and may select prime ideals only. Define the full
selected-factor convolution
\[
 F_u^\sigma(D)=
 -\sum_{\substack{a,b\\Na,Nb\le z}}
  \sigma_u(a)\mu_K(a)\mu_K(b)
  \lambda_u(ab)S_u(D/Nab).
\tag{7}
\]

### Lemma 1. Exact full-convolution cancellation

For sufficiently large \(D\),
\[
 F_u^\sigma(D)=0
\tag{8}
\]
for every row \(u\).

**Proof.** Recombine \(k=bm\) in (7). Every supported cofactor satisfies
\[
 Nk\le C_0D/Na\le z,\qquad
 Nk\ge cD/Na\ge cD/z>1.
\tag{9}
\]
Consequently every divisor of \(k\) lies below the \(b\)-cutoff, and
\[
 \sum_{\substack{b\mid k\\Nb\le z}}\mu_K(b)
 =\sum_{b\mid k}\mu_K(b)=0.
\tag{10}
\]
Complete multiplicativity puts the common factor
\(\lambda_u(a)\lambda_u(k)W(Nak/D)\) outside this divisor sum.
This remains valid when it is complex or zero. The coefficient
\(\sigma_u(a)\) is fixed while \(k\) is summed. Thus every \(a\)-channel
vanishes, proving (8). In fact, for each supported total product \(n\),
the full coefficient is already zero:
\[
 \sum_{\substack{a\mid n\\A_D\le Na\le z}}
   \sigma_u(a)\mu_K(a)
   \sum_{\substack{b\mid n/a\\Nb\le z}}\mu_K(b)=0.
\]
Here \(1<N(n/a)\le z\) for every outer summand, so the inner inverse
vanishes separately. \(\square\)

The cancellation in (8) is finite divisor algebra. It uses no
prime-counting theorem, no unproved integer-to-ideal transfer, and no
Poisson estimate with an arithmetic row selector.

## 3. The actual adaptive-tail block

Split (7) into its small-product and tail parts:
\[
 I_u^\sigma(D)=
 -\sum_{\substack{Na,Nb\le z\\Nab\le Y_u}}
  \sigma_u(a)\mu_K(a)\mu_K(b)
  \lambda_u(ab)S_u(D/Nab),
\tag{11}
\]
\[
 T_u^\sigma(D)=
 -\sum_{\substack{Na,Nb\le z\\Nab>Y_u}}
  \sigma_u(a)\mu_K(a)\mu_K(b)
  \lambda_u(ab)S_u(D/Nab).
\tag{12}
\]
The tail in (12) is an actual tuple block of the original adaptive tail.
Lemma 1 gives the pointwise relation
\[
 T_u^\sigma(D)=-I_u^\sigma(D).
\tag{13}
\]
At a fixed balanced prime product \(pq\), its tail coefficient can remain
nonzero. Equation (13), followed by completion below, is what permits
cancellation across different total products in this block.

### Theorem 2. Arbitrarily small full weighted energy

For \(1\le H\le D\), every requested \(N>0\), and any selectors (6),
\[
 \boxed{\frac1D\sum_{u\ne0}\Phi(Nu/H)|T_u^\sigma(D)|^2
                  =O_{N,W,\Phi,\theta}(D^{-N}).}
\tag{14}
\]
The constants are uniform in \(\sigma\).

**Proof.** When \(Y_u<1\), the small sum is empty, and (13) gives
\(T_u^\sigma=0\) exactly. When \(Y_u\ge1\), ideal counting yields
\[
 \sum_{\substack{Na,Nb\le z\\Nab\le Y_u}}
       |\sigma_u(a)\mu_K(a)\mu_K(b)|
 \ll Y_u\log(2Y_u).
\tag{15}
\]
For each of these products,
\[
 \frac{L_uNab}{D}\le D^{-\theta}.
\tag{16}
\]
Apply (4) to the original free-factor sum, before summing the coefficients.
Using \(Y_u=D^{1-\theta}/L_u\) gives
\[
 |I_u^\sigma(D)|
 \ll_{M,W}
 D^{1-\theta-M\theta}\log(2D)
       \frac{\tau(E_u)\sqrt{Q_u}}{L_u}.
\tag{17}
\]
Square, divide by \(D\), and use (5):
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|I_u^\sigma(D)|^2
 \ll_{M,\delta,W,\Phi}
 D^{1-2\theta-2M\theta}\log^2(2D)H^\delta.
\tag{18}
\]
Choose \(M\) sufficiently large after \(N,\theta,\delta\), and use
\(H\le D\). Equations (13) and (18) prove (14). \(\square\)

Even a row-dependent selector is legal here: it enters only a finite
coefficient sum bounded by (15). The completion in (4) is still applied
separately to the same original \(S_u\) for each fixed row. No selector is
inserted into a previously completed row kernel.

For a general profile with nonzero integral, the principal correction
must be retained:
\[
 I_u^\sigma=
 -\kappa_uD\!\left(\int W\right)
  \sum_{\substack{Na,Nb\le z\\Nab\le Y_u}}
     \frac{\sigma_u(a)\mu_K(a)\mu_K(b)\lambda_u(ab)}{Nab}
   +\text{small completion error}.
\tag{19}
\]
Thus (14) cannot be claimed for arbitrary profiles by dropping that term.

## 4. Why this is real compensation but a limited advance

For this branch-size illustration, specialize to the trivial fixed twist
\(\nu=1\) and the proposed parameters
\[
 h=a=2/5,\qquad H=D^{2/5},\qquad \theta=1/40.
\tag{20}
\]
Choose \(t\in(c,C_0)\) with \(W(t)\ne0\), and then choose
\[
 \alpha\in(C_0/C,1),\qquad
 \beta=t/(\alpha C)\in(0,1),\qquad \alpha\ne\beta.
\tag{21}
\]
The last condition excludes at most one choice of \(\alpha\).
Choose sufficiently narrow, disjoint fixed-ratio prime windows
\[
 Np\asymp\alpha z,\qquad Nq\asymp\beta z.
\tag{22}
\]
Their centers satisfy \(Np>A_D\), \(Np,Nq<z\), and \(NpNq=tD\).
Shrinking the windows preserves the strict inequalities and ensures
\[
 \Re(e^{-i\arg W(t)}W(NpNq/D))\ge\gamma_W>0.
\tag{23}
\]
Let \(\sigma_u(a)\) select the good prime ideals in the first window,
independently of \(u\). Within its actual tail, select \(a=p,b=q,m=1\)
with the two windows (22). The coefficient is the original
\(-\mu_K(p)\mu_K(q)=-1\).

The fixed-field prime ideal theorem supplies
\(\asymp D/\log^2D\) pairs. On every coherent inner row \(u=r^6\),
the supported prime norms are \(\gg\sqrt D\), while \(Nr\le D^{1/15}\).
Both deletion masks are therefore one. Every supported pair is in the
tail, since \(NpNq\ge cD>Y_u\). Equation (23) gives a subpiece amplitude
of modulus \(\gg_W D/\log^2D\) on each such row.
Counting the \(\asymp H^{1/6}\) distinct coherent rows gives the
selected primepiece energy
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)
       |\text{selected primepiece}_u|^2
 \gg_{W,\Phi}\frac{DH^{1/6}}{\log^4D}
 =\frac{D^{16/15}}{\log^4D}.
\tag{24}
\]
This is above the \(D^{4/5+\varepsilon}\) target.

On these coherent rows \(Y_u\gg D^{109/120}>z\).
At a fixed total product \(pq\), the other cofactor-divisor choice
\(b=1,m=q\) has \(Nab=Np\le z<Y_u\) and is absent from the tail.
Thus its tail coefficient cannot cancel within that same prime product.
Theorem 2 nevertheless makes the **complete selected-\(a\) tail block**
arbitrarily small in weighted norm. Its other total products must
compensate (24) in the aggregate.

The fixed-field prime ideal theorem is needed only for the branch-size
illustration (24), not for Lemma 1 or Theorem 2. The lower bound is for a
selected sum of squares. No lower bound for the full selected-\(a\) block,
or the full adaptive tail, follows from it.

The geometric limitation is explicit:
\[
 A_D/z=C_0/C.
\tag{25}
\]
For fixed profile constants, the controlled interval is a constant
fraction of the upper edge. It supplies no new power-width sector of
the two-factor geometry. If \(z\) is chosen arbitrarily close to the
smallest symmetric cutoff covering the profile, this interval becomes
arbitrarily narrow.

There is also an exact explanation in terms of asymmetric cutoffs.
Let \(m_A=\mu_K\mathbf1_{Nn\le A}\) and
\(r_A=\delta-\mathbf1*m_A\). Finite convolution algebra gives
\[
 \mu_K=m_A+m_B-m_A*m_B*\mathbf1+\mu_K*r_A*r_B.
\tag{26}
\]
Its remainder is supported strictly beyond \(AB\).
If \(AB\ge C_0D\) and \(A,B<cD\), then on the profile
\[
 \mu_K(n)=-(m_A*m_B*\mathbf1)(n).
\tag{27}
\]
Choosing \(A=A_D,\ B=z\) gives \(AB=C_0D\).
Thus the selected upper-edge cancellation is the mechanism behind
replacing the symmetric factorization by this asymmetric one.

More generally \(A\asymp D^\alpha,\ B\asymp D^{1-\alpha}\), with fixed
\(0<\alpha<1\), is allowed,
with the constant in \(AB\) covering the full annulus.
This changes the bilinear support but supplies no arithmetic estimate
for its remaining Möbius factors. The generic grouped-column sieve
still retains \(DH^{1/6}\). Primepair obstructions move to asymmetric
prime windows rather than disappearing.

Theorem 2 is therefore a concrete compensated block, valid on every
physical row and for complex twists. It does not control the complete
adaptive tail, establish a stronger zero-free boundary, or bypass
the cross-product obstruction in the unresolved remainder.

## 5. Relation to other repository tools

The proof uses the same ordering principle as the signed cofactor
representation in the prime-variance signed Mellin continuation:
sum a complete signed cofactor channel before applying an absolute
envelope. Here the complete cofactor sum is exactly a Möbius inverse,
so it can be used without transferring an integer Mertens estimate.

The source inputs are the organized manuscript's all-scale masked
completion, radical-weighted row mass, and elementary ideal counting.
The finite algebra in (10) and (26) is new only as this particular
application; it requires no deeper analytic source.

No empirical asymptotic bound or large derived data is used.
The full signed tail estimate remains open.

## 6. Finite verification

The companion checker, check_short_family_cofactor_compensation.py, prints
deterministic JSON and writes no files. Its small saved record,
short_family_cofactor_compensation_record_20261008.json, reports 18,442
passed assertions.

The checks use a free multiplicative divisor model with integer norms.
They verify the complete cofactor inverse, bounded row-dependent
selectors, the adaptive small/tail split, integer and noninteger strict
cutoff boundaries, the asymmetric inverse and its remainder support,
and the rational support and power-gap exponents. Complex phases and
deletion zeros use an exact quartic character modulo five with
Gaussian-integer values. This model is a finite test of the convolution
algebra; it is not a transfer of an integer analytic estimate to ideals.

No finite check validates physical Eisenstein reciprocity, the native
conductor comparison, Poisson completion, the radical-weighted row mass,
the prime ideal theorem, or an unbounded signed moment. Those inputs and
the analytic deduction remain as stated in the proof.

See the [organized manuscript](../short_family_reductions.tex),
[adaptive completion input](11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md),
[checker](../../numerics/check_short_family_cofactor_compensation.py),
[record](../../numerics/short_family_cofactor_compensation_record_20261008.json),
and [scoped review](../../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md).
