# Squarefree cofactor parity and a growing signed zero sector

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model derivations, audits and finite checks are internal
validation, not independent specialist review or formal proof verification.

## Outcome and limits

At the actual squarefree-reduction cutoff \(\theta=11/20\), there is a
canonical complete signed cofactor decomposition. It cancels every
**saturated small-prime cofactor with an odd rough core**. The cancellation
includes nonempty adaptive tails, rather than only products excluded by
support. A concrete new sector consists of a squarefree cofactor of norm
at most \(D^{1/40}\) and three larger primes. Its actual response on
rows with \(L_u\ge D^{1/8+\delta}\) has arbitrarily rapid decay in full
Schwartz-weighted energy. This sector has growing cofactor width and is
at the same cutoff as note 17.

This is finite signed cancellation plus a Schwartz exterior-row bound.
It is **not** a new exponent for the full moment. Saturated even rough
cores and unsaturated small-prime cofactors remain. Their individual
generic bounds still have exponent \(16/15\), rather than the desired
\(4/5\). Balanced semiprimes survive on every significant conductor
range; balanced triples survive on coherent low-conductor rows. No
cross-total-product contraction has been proved.

## 1. Setting and exact squarefree coefficient

Use the good ideal monoid, fixed finite-order twist, physical zero-extended
characters, and analytic inputs of the [existing manuscript](../short_family_reductions.tex).
Put

\[
 z=\sqrt{CD},\qquad Y_u=D^{9/20}/L_u,\qquad
 \lambda_u(n)=\nu(n)\chi_n(u),\qquad H=D^{2/5}.
 \tag{1}
\]

For \(n\) on the fixed annulus \(cD\le Nn\le CD\), sufficiently
large \(D\) gives \(z<Nn\le z^2\) and \(Y_u<z\) for every row.
For squarefree \(n\), the exact coefficient of the actual tail is

\[
 t_Y(n)=-\sum_{\substack{d\mid n\\Nd>Y}}c_z(d)
       =\mu_K(n)+\sum_{\substack{d\mid n\\Nd\le Y}}
                                    (-2)^{\omega(d)}.
 \tag{2}
\]

The first equality retains both truncated factors and every free-factor
tuple; the second is the truncated inverse, using \(Y<z\). The unit
divisor is included exactly when \(Y\ge1\). All characters, including
deletion zeros, multiply the common coefficient at the total ideal.
No new coprimality condition is imposed on an unprojected sum: squarefree
total ideals already force squarefree pairwise-coprime factors.

The original small response and nonsquarefree response retain their
previously proved budgets, including \(19/24\) for the latter. We only
decompose \(T_{u,\mathrm{sf}}^{(11/20)}\) here.

## 2. Complete small-prime cofactor and rough-core decomposition

For \(Y\ge1\), define, uniquely,

\[
 b_Y(n)=\prod_{\substack{p\mid n\\Np\le Y}}p,
 \qquad r_Y(n)=n/b_Y(n),
 \qquad
 O_Y(b)=\sum_{\substack{d\mid b\\Nd>Y}}(-2)^{\omega(d)}.
 \tag{3}
\]

Thus \((b_Y,r_Y)=1\), both factors are squarefree, and every prime
of \(r_Y\) has norm strictly greater than \(Y\). Equal-norm distinct
prime ideals enter \(b_Y\) simultaneously. The factors may be units.
Every divisor counted by the prefix in (2) divides \(b_Y\), and

\[
 \sum_{d\mid b}(-2)^{\omega(d)}
       =\prod_{p\mid b}(1-2)=\mu_K(b).
 \tag{4}
\]

Consequently the complete coefficient identity is

\[
 \boxed{t_Y(n)=\mu_K(b_Y)\{1+\mu_K(r_Y)\}-O_Y(b_Y).}
 \tag{5}
\]

This includes the entire overflow \(O_Y\); it is not permissible to
replace its coefficients by arbitrary bounded values or absolute Möbius
envelopes in a claimed improved estimate.

Call the small-prime cofactor *saturated* when \(Nb_Y\le Y\).
On this sector every divisor of \(b_Y\) belongs to the prefix, so
\(O_Y(b_Y)=0\), and (5) gives

\[
 t_Y(n)=
 \begin{cases}
 0,&Nb_Y\le Y,\quad\omega(r_Y)\text{ odd},\\
 2\mu_K(b_Y),&Nb_Y\le Y,\quad\omega(r_Y)\text{ even}.
 \end{cases}
 \tag{6}
\]

Even includes \(r_Y=1\). On the annulus the latter cannot be saturated
since \(Nn>Y\), but it must remain in the general identity. When
\(Y<1\), (2) instead gives \(t_Y(n)=\mu_K(n)\); (5) is not used.

For an exact response decomposition define, for \(Y\ge1\),

\[
 g_Y(n)=2\mu_K(b_Y(n))
       \mathbf1_{Nb_Y(n)\le Y}\mathbf1_{\omega(r_Y(n))\ \mathrm{even}},
 \qquad h_Y(n)=t_Y(n)-g_Y(n).
 \tag{7}
\]

Here \(h_Y\) is precisely (2) on the unsaturated sector and zero on
the whole saturated sector. Set \(g_Y=0\), \(h_Y=\mu_K\) when
\(Y<1\). Then pointwise in every actual physical row,

\[
 T_{u,\mathrm{sf}}^{(11/20)}=G_u+R_u,
 \quad G_u=\sum_{n\ \mathrm{sf}}g_{Y_u}(n)\lambda_u(n)W(Nn/D),
 \quad R_u=\sum_{n\ \mathrm{sf}}h_{Y_u}(n)\lambda_u(n)W(Nn/D).
 \tag{8}
\]

In particular the exact remaining target is the energy of **\(G_u+R_u\)**,
with both terms retained inside the same absolute square. It is not an
additive energy identity. Saturated odd rough cores have zero response
on every row where they satisfy the displayed conditions, without any
restriction on the fixed complex twist.

## 3. A growing, nonempty signed sector at large conductor

Fix \(\kappa>0\) and \(0<\delta<11/40\). Let \(\mathcal Q(D)\)
be the row-independent set of squarefree ideals on the profile admitting
a representation

\[
 n=bq_1q_2q_3,\qquad Nb\le D^{1/40},\qquad
 Nq_j\ge\kappa D^{13/40}\quad(1\le j\le3),
 \tag{9}
\]

where the \(q_j\) are distinct good primes and \((b,q_1q_2q_3)=1\).
Each total ideal is counted once. For sufficiently large \(D\) the
three large primes cannot divide \(b\), and all other primes of \(n\)
belong to \(b\), so the representation is unique up to permutation.
Define the actual conductor-selected response

\[
 C_u(D)=\mathbf1_{L_u\ge D^{1/8+\delta}}
      \sum_{n\in\mathcal Q(D)}t_{Y_u}(n)\lambda_u(n)W(Nn/D).
 \tag{10}
\]

**Theorem.** For every \(N>0\),

\[
 \boxed{D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})|C_u(D)|^2
                =O_{N,\delta,\kappa,W,\Phi}(D^{-N}).}
 \tag{11}
\]

**Proof.** First restrict to \(Nu\le D^{33/80}\). The existing
comparison \(1\le L_u\ll_{\nu,S}Nu\), with its fixed constant retained,
gives

\[
 Y_u\gg D^{9/20-33/80}=D^{3/80}>D^{1/40}\ge Nb.
 \tag{12}
\]

On the conductor-selected rows,

\[
 Y_u\le D^{9/20-1/8-\delta}
       =D^{13/40-\delta}<\kappa D^{13/40}\le Nq_j.
 \tag{13}
\]

The positive margins absorb the fixed constants. Thus \(b=b_{Y_u}(n)\)
is saturated and \(r_{Y_u}(n)=q_1q_2q_3\) has odd parity. Equation (6)
makes every total-product coefficient zero. Rows failing the conductor
selector also have \(C_u=0\) by definition.

The exterior rows have not been discarded. Uniformly in every row and
cutoff, the divisor bound and ideal counting give

\[
 |C_u(D)|\ll_{\epsilon,W}D^{1+\epsilon},\qquad
 \sum_{Nu>D^{33/80}}\Phi(Nu/D^{2/5})
       \ll_{A,\Phi}D^{2/5-A/80}
 \tag{14}
\]

for every chosen \(A>0\), after adjusting the Schwartz decay order.
The normalized energy is at most
\(O(D^{7/5+2\epsilon-A/80})\). Choose \(A\) after \(N\) to prove
(11). No character estimate for growing conductors is being substituted
for the exact zero. \(\square\)

This controls the whole selected response in (10), not its branches
separately. The cofactor range has growing power width. For example,
choosing \(b\) a prime of norm comparable to \(D^{1/40}\) and the
three other primes comparable to \(D^{13/40}\), with fixed constants
placing their product in any open part of the annulus, gives examples
by the already imported fixed-field prime ideal theorem. That theorem
is only needed for this asymptotic nonemptiness statement, not (11).
More precisely, choose disjoint narrow prime windows with centers
\(\alpha D^{1/40},\beta_1D^{13/40},\beta_2D^{13/40},\beta_3D^{13/40}\),
where \(0<\alpha<1\), \(\beta_j>\kappa\), and
\(\alpha\beta_1\beta_2\beta_3\) lies in the interior of the annulus.
For any fixed \(\kappa\), choose the \(\beta_j\) first and then take
\(\alpha\) sufficiently small. The same imported theorem supplies
\(\asymp D/\log^4D\) distinct total ideals in these windows. Thus the
controlled column sector has full power cardinality; the limitation is
its conductor range, not a sparse-column gain.

The cancellation is not an empty-tail phenomenon. Already when \(b=1\)
and \(q_j\asymp D^{1/3}\), all three singletons are below \(z\), all
three pair products exceed \(z\), and \(Y_u<\min Nq_j\). The actual
truncated convolution has

\[
 c_z(q_j)=-2,\qquad c_z(q_iq_j)=2,\qquad c_z(q_1q_2q_3)=0.
 \tag{15}
\]

Its singleton tail terms sum to \(+6\) and its pair tail terms to
\(-6\). Both are nonzero before recombination. A finite nonunit-cofactor
instance is included in the checker. This differs from note 18's change
of asymmetric factor cutoffs and from note 15's larger-buffer packet.
It is nevertheless another productwise cancellation; it does not address
the surviving cross-total-product moment.

## 4. Every conductor range and the surviving coherent rows

For balanced triples \(Nq_j\asymp D^{1/3}\), the transition occurs
near \(L_u=D^{7/60}\), since \(9/20-1/3=7/60\). The following
statements concern their selected product response, not the full tail.

| Combined modulus range | Balanced triple coefficient or treatment |
| --- | --- |
| \(L_u\le D^{7/60-\gamma}\), fixed \(\gamma>0\) | Every singleton is below \(Y_u\), every pair is above it; coefficient \(-6\) |
| Between the two buffered powers | Keep each prime threshold; coefficients \(-6,-4,-2,0\) according to the number of included singletons |
| \(D^{7/60+\gamma}\le L_u\le D^{9/20}\) | \(1\le Y_u<\min Nq_j\); coefficient zero |
| \(L_u>D^{9/20}\) | \(Y_u<1\), coefficient \(-1\); full weighted energy is negligible by Schwartz decay |

Here the bounds hold for sufficiently large \(D\), absorbing the fixed
prime-window constants. At an exact prime threshold equality belongs to
the prefix: the coefficient changes at \(Y_u=Nq_j\), not after it.
The transition band carries no improved bound in this note.

Coherent inner rows \(u=r^6\), \(Nu\le D^{2/5}\), satisfy
\(L_u\ll Nr\le D^{1/15}\). Hence
\(Y_u\gg D^{23/60}\), and balanced triples retain coefficient \(-6\).
These rows have not been eliminated by the large-conductor theorem.
Balanced semiprimes have coefficient \(+2\) whenever \(Y_u\ge1\),
since both primes have norm comparable to \(D^{1/2}>Y_u\). They have
even rough parity and survive throughout the significant family.
No assertion that either complete selected amplitude is positive, or a
lower bound for the full tail, follows from these coefficient tables.

The single-large-prime special case deserves a separate caution. If
\(n=bq\), \(Nb\le Y_u\), \(Nq>Y_u\), its coefficient is also zero.
In the uniform range \(Nb\le D^{1/20-\delta}\), however, the annulus
forces \(Nq>z\). Neither truncated factor can contain \(q\), and every
possible convolution divisor is already below \(Y_u\). That case is
support exclusion, not cancellation of nonzero tail branches. It is not
the milestone claimed in (11).

## 5. Quantified retained budget without an extra power saving

There is a legal generic bound for each *canonical* term of (8):

\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/H)(|G_u|^2+|R_u|^2)
          \ll_{\epsilon,W,\Phi}D^\epsilon B(D,H),
 \tag{16}
\]
\[
 B(D,H)=H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}.
\]

Here is why their row dependence is legal. For a fixed squarefree column
\(n\), extend \(t_y(n)\) to all \(y\ge0\) by its original truncated
tail \(-\sum_{d\mid n,\,Nd>y}c_z(d)\). This agrees with (2) at every
actual threshold \(Y_u<z\); the untruncated low-prefix formula is not
asserted beyond \(z\). This auxiliary \(t_y\) has jumps at divisor
norms, total variation at most
\(\sum_{d\mid n}2^{\omega(d)}=3^{\omega(n)}\ll_\epsilon(Nn)^\epsilon\).
The coefficient \(g_y(n)\) only changes when \(y\) crosses a prime norm
or the norm of the current initial prime product \(b_y\). These are also
divisor norms. Its number of changes and variation are \(O(1+\omega(n))\),
since its values are \(0,2,-2\). At equal norm thresholds one uses the
combined jump. Thus \(h_y=t_y-g_y\), including the jump at \(y=1\),
also has total variation \(O_\epsilon((Nn)^\epsilon)\).

Represent either coefficient by its value at \(y=0\) and its jumps on
the common integer threshold list \(1,\ldots,\lfloor CD\rfloor\).
Every prefix is a union of \(O(\log D)\) fixed binary-tree intervals.
For one fixed partition level, if \(a_{\mathcal J}(n)\) is the sum of
jumps in interval \(\mathcal J\),

\[
 \sum_{\mathcal J\ \mathrm{at\ that\ level}}
          |a_{\mathcal J}(n)|^2
       \le\left(\sum_j|\Delta a_j(n)|\right)^2
       \ll_\epsilon D^\epsilon.
 \tag{17}
\]

For each interval, multiply this fixed vector by
\(\nu(n)W(Nn/D)\) and apply the manuscript's imported physical operator
on squarefree columns of length \(CD\). Sum (17) over the
\(O(D)\) columns and \(O(\log D)\) levels, and pay the prefix Cauchy
factor. Dividing by \(D\) proves (16), with logarithms absorbed into
epsilon. The initial constant vector is handled by the same operator.
This does not insert a row-dependent product mask into a completed
kernel, and does not license arbitrary row-dependent selectors.

At \(H=D^{2/5}\), the four generic powers are respectively
\(2/5,16/15,2/3,29/30\). Consequently (16) leaves the same
\(D^{16/15+\epsilon}\) bound. The deficit to \(4/5\) remains
\(4/15\). The nonsquarefree difference vector still costs
\(D^{19/24+\epsilon}\), and the exterior/unit rows cost arbitrary
negative powers, as before. There is no unbudgeted conductor range
claimed to be small.

## 6. What the next estimate must do

The exact decomposition provides a new signed zero sector of nonempty
tails at the intended buffer. It localizes the open response to saturated
even rough cores and unsaturated cofactors, with the latter's full overflow
retained. Proving separate target-sized bounds for convenient prime
components is still incompatible with the coherent semiprime examples.
The next useful advance would control a nonzero signed combination of
these remaining terms across different total products. The
[squarefree discrepancy bridge](22_SHORT_FAMILY_SQUAREFREE_DISCREPANCY_20261008.md)
records an exact interface and the extra modulus cost; it supplies no
such contraction.

The [checker](../../numerics/check_short_family_rough_parity.py) and its
[small record](../../numerics/short_family_rough_parity_record_20261008.json)
report 32,815 passing assertions over 177 inverse-profile cases and
3,173 cutoffs, including 420 nonempty canceled tails. Two fresh runs
reproduced the record byte-for-byte. These verify finite truncated convolution,
the prefix and overflow identities,
endpoint conventions, nonempty signed examples, phases/deletion zeros
and rational exponent budgets. They do not verify physical reciprocity,
conductor comparison, Poisson, the infinite weighted mass estimate, ideal
prime asymptotics, the imported sieve, or an unbounded signed moment.
See the [scoped audit](../../reviews/SHORT_FAMILY_ROUGH_PARITY_REVIEW_20261008.md).
