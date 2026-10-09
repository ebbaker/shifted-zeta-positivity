# Exact joint second transform before Cauchy

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. This is same-model internal
research and source checking, not independent specialist review or formal
verification.

The primary source is the
[30 September companion manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Printed pp. 88–91 and 160–167 were read in memory. Pages 89, 161 and 162
were also rendered temporarily to verify conjugations that text extraction
omits. The PDF SHA-256 matches
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The PDF, long extracts and temporary rendered images are not retained.

The main new exact facts are these:

* The direct joint transform has the signed kernel
  \(Q_j(a,b)=R(a,b)\overline{\chi_b(-1)}F(a,b;j)\), rather than the
  positive Gauss norm created by Cauchy.
* Its \(j=0\) kernel, after the full coprimality Möbius sum, vanishes
  except for a possible unit/unit residual column. An active common
  primitive character makes it vanish even there.
* For nonzero \(j\), an individual coprimality label contributes only
  when \(s\mid j\). The restored outer sum is thus over divisors of the
  physical new frequency, with the full correlation kernel retained.
* Keeping the primitive common Gauss factor gives raw new row length
  \(m-E+(K_0-K)\), and its surviving column twist has support \(q+E\).
  The total width is \(M+(K_0-K)\). There is no automatic width descent.
* Exact sixth-power averaging kills every two-sided \(p\)-extraction
  branch after coprimality is restored, but the retained row lattice mask
  prevents the source's positive-norm enlargement from giving a free
  signed width saving.

## 1 The source's exact pre-Cauchy expression

Use \(q_v=\mathrm Nv\), multiplicative primary generators outside the
original excluded set, and the self-dual lattice normalization of the
source. Let \(X=Z^A\), \(H=Z^m\), and fix a genuine complete-common-support
allocation \(Ca,Db\). The physical residual locus is
\[
 (a,b)=1,\qquad (ab,CD)=1.
\]
Let \(r\) be the common primes with nonzero net character exponent,
let \(\xi_r\) be their primitive zero-extended character, and let \(e\)
be the selected squarefree divisor in the complementary common row mask.
Thus \(r,e\) are disjoint, and both puncture the residual columns.
The source uses
\[
 \tau_C(a)=\tau(a)\chi_a(er)\xi_r(a),\qquad
 \tau_D(b)=\tau(b)\chi_b(er)\overline{\xi_r(b)}.
\]
The conjugation in the second definition is essential.

With an outer scalar \(\kappa\) containing the frozen-label phases,
including the sign from the \(e\)-mask expansion, source (18.21) is
\[
 \mathcal I=
 \kappa\frac{H}{Xq_e\sqrt{q_r}}
 \sum_{h\ne0}G_{\xi_r}(r,h)
 \sum_{(a,b)=1}
 \frac{A_C(a)\overline{A_D(b)}}{\sqrt{q_aq_b}}\,
 \tau_C(a)\overline{\tau_D(b)}R(a,b)
 G(a,h)\overline{G(b,-h)}
 \widehat\Phi_1\!\left(\frac{Hq_h}{q_eq_rq_aq_b}\right).
 \tag{1}
\]
The coefficients retain the original profiles, all live slot sums, every
old zero mask, and the entire allocated centered difference if present.
For an actual marked mixed coefficient they also retain its inverse
Möbius coefficient and inverse annulus. Nothing in the following finite
algebra assumes the coefficients are plain or nonnegative.

The primitive and residual Gauss sums use
\[
 G_\xi(r,h)=q_r^{-1/2}\sum_{z\bmod r}\xi(z)e(hz/r),\qquad
 G(a,h)=q_a^{-1/2}\sum_{x\bmod a}\chi_a(x)e(hx/a).
\]
For \(r=1\), the primitive factor is one.

Fix one of the source's retained whole frequency dyads of length \(T=Z^K\).
Put
\[
 W_{a,b}(v)
 =\omega(q_v/T)\widehat\Phi_1\!\left(
              \frac{Hq_v}{q_eq_rq_aq_b}\right)
 =w_{\lambda_{a,b}}(q_v/T),\qquad
 \lambda_{a,b}=\frac{HT}{q_eq_rq_aq_b}.
 \tag{2}
\]
The dyad vanishes at \(v=0\). The whole product kernel remains attached
to the actual \(a,b\); neither its inverse roots nor its norms are
changed separately for a Möbius divisor label.

Define the source's artificial all-pairs extension of (1) using these
same Gauss sums, the fixed sign bicharacter \(R\), and the old masks.
Before estimating anything, insert
\[
 1_{(a,b)=1}=\sum_{s\mid a,\ s\mid b}\mu_F(s).
 \tag{3}
\]
This is a finite exact identity on each physical column shell. The \(s\)
in (3) is a coprimality label, distinct from the inverse variable inside
\(A_C,A_D\).

## 2 The correct finite Fourier coefficient

Lemma 13.3 defines
\[
 F(a,b;j)=\sum_{\substack{x\bmod a,\ y\bmod b\\
                         bx-ay\equiv j\;(\bmod ab)}}
                         \chi_a(x)\overline{\chi_b(y)}.
 \tag{4}
\]
It corresponds to \(G(a,h)\overline{G(b,h)}\). The source bridge instead
has \(\overline{G(b,-h)}\). Define its plus-congruence kernel
\[
 F^+(a,b;j)=
 \sum_{\substack{x\bmod a,\ y\bmod b\\
                 bx+ay\equiv j\;(\bmod ab)}}
                         \chi_a(x)\overline{\chi_b(y)}.
\]
Changing \(y\) to \(-y\) gives the exact all-pairs identity
\[
 F^+(a,b;j)=\overline{\chi_b(-1)}F(a,b;j).
 \tag{5}
\]
All values, including zeros and principal character powers, are retained.

Keeping the primitive common factor gives a triple kernel, with formal
modulus \(rab\):
\[
 F_r^+(a,b;j)=
 \sum_{\substack{z\bmod r,\ x\bmod a,\ y\bmod b\\
   ab z+rb x+ra y\equiv j\;(\bmod rab)}}
   \xi_r(z)\chi_a(x)\overline{\chi_b(y)}.
 \tag{6}
\]
This definition and finite Fourier expansion are valid even for
artificial noncoprime \(a,b\), provided \((ab,r)=1\). Direct expansion
of all three Gauss sums gives
\[
 \frac1{q_rq_aq_b}\sum_{h\bmod rab}
  G_{\xi_r}(r,h)G(a,h)\overline{G(b,-h)}
  e(-jh/(rab))
 =\frac{F_r^+(a,b;j)}{\sqrt{q_rq_aq_b}}.
 \tag{7}
\]
The factor on the left is the finite average; no character quotient
at a nonunit has been introduced.

Reduction of (6) modulo \(r\), followed by the unit changes
\(x\mapsto r^{-1}x,\ y\mapsto r^{-1}y\) on the other two moduli, gives
for every artificial pair
\[
 F_r^+(a,b;j)
 =\xi_r(j)\overline{\xi_r(ab)}
   \overline{\chi_a(r)}\chi_b(r)F^+(a,b;j).
 \tag{8}
\]
For \(r=1\) the \(\xi_1\)-factors are interpreted as one, even at \(j=0\).

The source's fixed bicharacter is symmetric and sign-valued, hence
\(R(a,b)^2=1\), including on artificial pairs. Combining (8) with the
displayed \(\tau_C,\tau_D\) in (1) yields the exact cancellation
\[
 \tau_C(a)\overline{\tau_D(b)}R(a,b)F_r^+(a,b;j)
 =\tau(a)\overline{\tau(b)}
   \chi_a(e)\overline{\chi_b(e)}\xi_r(j)Q_j(a,b),
 \tag{9}
\]
where
\[
 \boxed{Q_j(a,b)=R(a,b)\overline{\chi_b(-1)}F(a,b;j).}
 \tag{10}
\]
Thus the full common \(r\)-twist disappears from the columns and remains
as the native row factor \(\xi_r(j)\). Equation (9) holds before
coprimality is restored; it does not invoke CRT at a newly added pair.

On the genuine locus \((a,b)=1\), the congruence in (4) uniquely determines
both residues. Sextic reciprocity and \(\chi_b(-1)^2=1\) give
\[
 Q_j(a,b)=\chi_a(j)\overline{\chi_b(j)}.
 \tag{11}
\]
This genuine formula must not be substituted into an individual
noncoprime \(s>1\) term in (3).

## 3 The direct joint second Poisson formula

For the radial function \(w_{\lambda}\), write
\(\widehat w_{\lambda}\) for its self-dual radial Fourier transform.
Poisson applied to (7) gives
\[
 \sum_h W_{a,b}(h)G_{\xi_r}(r,h)
                  G(a,h)\overline{G(b,-h)}
 =\frac{T}{\sqrt{q_rq_aq_b}}
    \sum_j F_r^+(a,b;j)
       \widehat w_{\lambda_{a,b}}
          \!\left(\frac{Tq_j}{q_rq_aq_b}\right).
 \tag{12}
\]
The dyad already excludes \(h=0\); no Gauss row zero is added here.
Its transform includes \(j=0\), which is a different operation.

Consequently the retained dyad of (1) is exactly
\[
 \boxed{\begin{aligned}
 \mathcal I_T={}&
 \kappa\frac{HT}{Xq_eq_r}
 \sum_j \xi_r(j)\sum_s\mu_F(s)
 \sum_{\substack{s\mid a,\ s\mid b}}
 \frac{A_C(a)\overline{A_D(b)}}{q_aq_b}\,
 \tau(a)\overline{\tau(b)}
 \chi_a(e)\overline{\chi_b(e)}Q_j(a,b)\\
 &\hspace{18mm}\cdot
 \widehat w_{\lambda_{a,b}}
          \!\left(\frac{Tq_j}{q_rq_aq_b}\right).
 \end{aligned}}\tag{13}
\]
Every summand uses the original individually permitted column masks.
The sum in \(s\) is complete. For finite physical column shells,
interchanging it with the Schwartz frequency sum is justified by
absolute convergence. This is the exact joint transform before
Cauchy, with no positive row norm or row enlargement.

If the full Möbius sum is collapsed first, (11) turns (13) into
\[
 \kappa\frac{HT}{Xq_eq_r}
 \sum_j\xi_r(j)\!
 \sum_{(a,b)=1}
 \frac{A_C(a)\overline{A_D(b)}}{q_aq_b}
 \tau(a)\overline{\tau(b)}
 \chi_a(ej)\overline{\chi_b(ej)}
 \widehat w_{\lambda_{a,b}}
       \!\left(\frac{Tq_j}{q_rq_aq_b}\right).
 \tag{14}
\]
The physical zeros at primes dividing \(ej\) are explicit in this formula.

## 4 What vanishes, and what survives, at the new zero frequency

Lemma 13.3 gives
\(F(a,b;0)=1_{a=b}\varphi(a)\). The source also proves
\(\chi_a(-1)=R(a,a)\). Therefore (10) has the all-pairs diagonal
\[
 Q_0(a,b)=1_{a=b}\varphi(a).
 \tag{15}
\]
This is an exact finite-kernel statement, not a projection of a
separately estimated positive norm.

If \(r>1\), its primitive nonprincipal character satisfies
\(\xi_r(0)=0\), so the \(j=0\) term of (13) is zero even before
the \(s\)-sum. If \(r=1\), its diagonal coefficient contains
\[
 \sum_{s\mid a}\mu_F(s)=1_{a=1}.
 \tag{16}
\]
Hence the complete coprimality sum kills every nonunit diagonal.
Only \(a=b=1\) can remain, with its actual allocated coefficient,
old masks and Fourier weight. A physical residual shell bounded away
from the unit ideal excludes this possibility. Some complete-common-
support allocations can leave unit residual columns, so it cannot be
discarded without that support check or a separate outer-label estimate.

This cancellation does not apply to the source's later positive
\(\mathcal N_C\), which is formed after Cauchy, may be enlarged and
amplified, and no longer contains the full signed projector (3).
It does not cancel the source's original first-Poisson \(h=0\) term,
which was already handled separately through powerful products.
The annular prime-product diagonal of the earlier positive-norm
diagnostic is an artificial noncoprime pair in this zero-common-support
joint kernel and is killed by (16).

## 5 A nonzero-frequency arithmetic refinement

For \(g=(a,b)\), source Lemma 13.3 gives
\[
 F(a,b;j)=0\quad\hbox{unless }g\mid j,\qquad
 |F(a,b;j)|\le q_g.
 \tag{17}
\]
These are properties of the actual congruence kernel for all full
moduli, not the artificial factorized extension of Lemma 13.4.
Thus \(Q_j\) satisfies the same two assertions.

For \(j\ne0\), a term of (13) with \(s\mid a,b\) vanishes unless
\(s\mid j\). The complete restored sum can therefore be written exactly
as
\[
 \sum_{\substack{s\mid j\\s\ {\rm squarefree}}}\mu_F(s)
 \sum_{s\mid a,b}[\text{the unchanged summand of (13)}].
 \tag{18}
\]
There are only divisor-boundedly many labels for each fixed \(j\).
This removes the unrestricted artificial-label volume at this stage;
in a retained second-frequency range it also implies \(q_s\le q_j\).
The correlation itself can still be as large as \(q_{(a,b)}\).
Taking absolute values in (18) without controlling those local
correlations does not prove the desired saving. Nor does (18) permit
using (11) on an individual \(s>1\) term.

A legitimate next bilinear lemma would estimate the signed aggregate
in (13), or (18), with the actual marked coefficients and common smooth
kernel. Its coefficient class must retain inverse squarefreeness,
original inverse and plain annuli, all physical zeros and allocated
slots. A bound only for unrestricted positive coefficient norms misses
the cancellation (16).

## 6 Exact width ledger and the involution check

Write \(c=\log_Zq_C\), \(d_C=\log_Zq_D\),
\(R=\log_Zq_r\), \(E=\log_Zq_e\). The residual product lengths are
\(A-c\) and \(A-d_C\). Source (18.21) has nominal first frequency
\[
 K_0=2A-c-d_C+R+E-m.
\]
The triple second transform in (12) uses period \(rab\), so its raw
new frequency length is
\[
 m_{\rm joint}=2A-c-d_C+R-K
              =m-E+(K_0-K).
 \tag{19}
\]
After (9), the additional moving column support is only that of \(e\).
The original support \(q\) remains, while \(r\) is a native row scalar.
Consequently
\[
 M_{\rm joint}=m_{\rm joint}+q+E=M+(K_0-K).
 \tag{20}
\]
The factor \(\xi_r(j)\) is still present and can have moving conductor.
This is an exact column-support and row-length ledger, not a claim that
the joint signed expression belongs to every source recursive coefficient
class. Its row character may not be relabeled as fixed arithmetic data
or silently discarded in a signed bound.
At the nominal upper frequency \(K=K_0\) the width is exactly \(M\);
lower dyads have larger nominal total width. A retained endpoint with
\(K>K_0\) by the source's small frequency allowance gives only that
already allocated perturbation, not a fixed new descent.

The same conclusion is visible without a dyad. If the full first
Fourier kernel is transformed back, set
\(B=q_eq_rq_aq_b/H\). Its second radial transform is
\(B\Phi_1(Bq_j/(q_rq_aq_b))=B\Phi_1(q_eq_j/H)\).
All normalization factors cancel, recovering
\[
 \frac{\kappa}{X}\sum_{(a,b)=1}
 A_C(a)\overline{A_D(b)}\tau(a)\overline{\tau(b)}
 \sum_j \xi_r(j)\chi_a(ej)\overline{\chi_b(ej)}
                         \Phi_1(q_eq_j/H),
 \tag{21}
\]
with the corresponding first \(h=0\) term subtracted if only \(h\ne0\)
was retained. The frozen scalar includes the original \(\xi_r(e)\)
and Möbius-mask factors when present. Restoring the full \(e\)-sum
restores the original common row mask. This is an exact Poisson
involution, consistent with (19)–(20).

## 7 Sixth-power row replacement before Cauchy

Let \(p\) be an eligible pool prime, disjoint from \(h\), \(r,e\), all
frozen supports and every live slot window. Put \(P=q_p\). The source
local identity changes only full column valuations \(i=1,6,7\).
On a \(p\)-free column,
\[
 G(a,hp^6)=G(a,h),
\]
and the primitive common factor is also unchanged, since \(\xi_r\)
has order dividing six and \(p\) is a unit modulo \(r\).

On the genuine residual locus, at most one of \(a,b\) can contain \(p\).
Equivalently the full projector (3) annihilates every artificial branch
where both columns contain \(p\). Thus, if both Gauss polynomials are
expanded through their exact \(h\mapsto hp^6\) local identities, the
two-sided extraction error vanishes after (3). The surviving errors
are one-sided valuations \(1,6,7\), with linear central coefficient
moduli
\[
 P^{-1/2},\qquad 1-P^{-1},\qquad P^{-1/2}.
 \tag{22}
\]
These are not the squared \(P^{-1},(1-P^{-1})^2,P^{-1}\) costs of
the source's positive norm.

In the marked mixed coefficient the allocations also include possible
ownership by its inverse variable. That ownership is at most one
power, and extraction uses
\[
 \mu_F(pd)=-\mu_F(d)1_{(p,d)=1}.
 \tag{23}
\]
It shortens the actual inverse annulus from \(D_{\rm inv}\) to
\(D_{\rm inv}/P\), retains its rescaled profile, and adds the \(p\)-puncture
to every residual factor. The remaining \(i-1\) powers, if any, are
allocated to the plain variables. All two-rectangle comparison
coefficients must use the same allocations. Replacing this by an
unmarked plain child would lose the original coefficient.

The apparent enlarged row length alone does not give signed descent.
For \(p\)-free residual columns set
\(\mathcal P(h)=G_\xi(r,h)G(a,h)\overline{G(b,-h)}\), with period
\(L=rab\). Since \(\mathcal P(p^6h)=\mathcal P(h)\),
\[
 \sum_h w(q_h/T)\mathcal P(h)
 =\sum_{\substack{h'\\p^6\mid h'}}
     w(q_{h'}/(TP^6))\mathcal P(h').
 \tag{24}
\]
The right side has a larger ball but a retained sublattice mask.
Its formal period is \(p^6L\). The finite average of its masked
periodic factor is \(P^{-6}\) times the old finite coefficient, while
its row scale is \(TP^6\); the factors cancel. The Fourier argument is
\[
 \frac{TP^6q_j}{P^6q_L}=\frac{Tq_j}{q_L},
\]
so the new frequency scale is unchanged. If eligibility \(p\nmid h\)
is retained, the right side has \(v_p(h')=6\); its extra unit mask
likewise remains present on both sides and does not alter this
equivalence.

The actual pool average has a row-dependent eligible set and its exact
normalization. Dropping eligibility, replacing the retained sublattice
by a smooth full ball, or treating its signed weight by a positive
majorant needs a new inequality. The source obtains that enlargement
only after positivity from Cauchy/Jensen. Applying it unchanged here
would abandon the projector cancellation that removed (15).
The one-sided branches (22) are concrete objects for a new signed
operator estimate, but no such estimate or fixed width saving follows
from the replacement identity alone.

## 8 Required masks and the bounded analytic conclusion

Equations (13)–(18) require:

1. Complete, genuine common-support extraction before extension:
   \(a,b\) individually avoid \(CD\), hence \(e,r\).
2. Every old moving zero and every extracted puncture on every residual
   factor. A forced-zero allocation is discarded before any scalar
   Gauss bound.
3. Identical physical profiles and column-pair Fourier kernels in all
   divisor terms. No \(s\)-dependent truncation or live-label frequency
   cutoff may replace the common whole-dyad selection.
4. The full squarefree coprimality sum. Its terms are not independent
   estimates to be absolutized before (13) or (16).
5. Original marked inverse coefficients and all live slots, including
   inverse ownership in (23); fixed ray factors remain whole-product
   characters.
6. Actual column norms in both inverse roots and Fourier kernels.
   Smooth separation, if later needed, uses a common measure for the
   entire signed combination.

This kernel derivation applies to the source's fixed smooth row-envelope
problem. The original positive selected moment F may be bounded by the
stronger full mixed moment under a smooth majorizer of its physical row
ball, with the actual coefficient and all masks retained. That monotonicity
does not authorize replacing the physical selected signed near-coprime
remainder by an enlarged row sum. A selected signed result still needs
an applicable signed bilinear estimate or another justified transfer from
a sufficient positive full mixed-moment estimate.

The arithmetic advance is the exact removal of the artificial second
diagonal and the frequency-divisor support (18). The remaining problem
is to bound the nonzero-frequency signed aggregate without restoring
a damaging positive coefficient diagonal. Unamplified double Poisson
returns the original width. Exact sixth-power replacement simplifies
the branches but also returns that width unless a new signed operator
bound supplies a quantitative gain.
