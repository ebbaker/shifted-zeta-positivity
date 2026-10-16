# Phase 1: retaining the inverse in the source fourth-moment proof

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. This is a same-model internal
proof-structure and source-scope audit, not independent verification of the
imported analytic lemmas.

Primary source: [30 September companion manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Inspected the printed pp. 152–180 in memory; no PDF was saved.
SHA-256: 8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.
This version has subsections 18.1–18.8; section 19 begins on p. 180,
so there is no subsection 18.9 in the inspected version.

## 1 Result and the exact first loss

The existing deduction of the selected inverse-weighted fourth moment is
\[
 F_J=\sum_{u\in\mathcal C_+}|M_u|^2|S_u|^4|Q_J(u)|^2
 \le \left(\sup_{u\in\mathcal C_+}|M_u|^2\right)
       \sum_{u\in\mathcal C_+}|S_u|^4|Q_J(u)|^2
 \ll U^{1+dr+\varepsilon}H^b. \tag{1}
\]
The replacement of the inverse response by its pointwise envelope is
where its correlation with the plain/prime response is discarded.
The missing \(1/540\) is not an identified loss already spent inside the
source fourth proof. That proof estimates a different coefficient class.

If the inverse is retained, its positive full product can be enlarged to
a complete source-compatible row family. This is a legitimate stronger
problem. Keeping the sharp selector and treating
\(\mathbf1_{\mathcal C_+}|M_u|^2\) as a row weight instead does not permit
the source's clean radial row-Poisson formula. Source p. 158 enlarges a
whole positive norm before applying Poisson; it does not transform an
arbitrary sharply selected response-weighted row sum.

These are distinct options. A theorem for the full positive mixed norm
would imply the selected bound, and then the note 14 remainder bound by
its controlled difference. A signed ratio- or gcd-filtered sum cannot
itself be enlarged by positivity.

## 2 Source statement and proof dependencies

On p. 153, Lemma 18.1 concerns two plain sums and original short whole
prime slots. Its physical rows are elements of norm \(O(Z^{m_{\rm row}})\);
the fixed-within-row-sum presentation is
\(\tau(n)\chi_n(k)\), and displayed moving support has length \(q\).
The effective width is \(M=m_{\rm row}+q\). For positive slots, the
primitive inducing character must lie outside the fixed finite ray group
\(\Theta\), and the length condition is
\[
 n_1+n_2+6\kappa z\le M,\qquad 3/4\le\kappa\le1. \tag{2}
\]
Positive-length slot coefficients are fixed finite combinations of
characters in \(\Theta\), with disjoint original underlying supports.
For \(\kappa<1\), the global family prerequisite is
\(\beta_*\le(1+\kappa)/2\). The mesh precedes the fixed slot count and its
profiles. With no live slots the two plain lengths have no restriction,
but that conclusion uses their specific reflection and centering proof.
It is not an arbitrary-coefficient operator statement.

The relevant proof steps are:

| Printed pages | Step | Requirement when inserting the inverse |
| --- | --- | --- |
| 154–156 | Extra-mask erasure; functional-equation reflection of plain sums | The reciprocal polynomial has no corresponding reflected plain-sum identity supplied by this proof. |
| 157–158 | Prime pointwise bounds; finite width induction; equal-product comparison; enlargement of a whole positive norm | Retaining a selected inverse weight blocks radial Poisson; enlarging the whole mixed norm is legal but loses the selected bin's buffered local input. |
| 159–163 | One common centered coefficient; first row Poisson; complete common-support extraction; separated Gauss norms | Arithmetic identities extend to a mixed convolution, but its Gauss norm is a new marked norm requiring an additional estimate. |
| 164–168 | One prime-pool amplification; second finite transform; exact common-prime correlations; strict smaller width | Any extension must allocate inverse prime powers as well as plain powers and preserve squarefreeness. |
| 169–173 | Full artificial coprimality allocation; coefficient lemma; independent children; clipping and greedy whole-slot removal | Extracting an artificial divisor prime from the inverse introduces its own puncture. Source child moments do not cover the resulting inverse-plus-two-plain class. |
| 174–178 | Exceptional child count; equal-product masked plain cancellation | Plain main-term cancellation can survive after freezing inverse labels, but the remaining signed inverse-label average is not supplied by the source lattice estimate. |
| 179–180 | Uniform aggregate errors and finite propagation of seminorm/height orders | Every new marked child estimate and its finite orders must be established before the later external tail order; no automatic propagation is available. |

## 3 What survives the first transform, and the precise missing norm

Take one fixed original inverse/plain profile and fixed permitted twists.
Write \(P_J=\prod_{j\in J}P_j\), and let
\[
 X_{\rm mix}=D N^2P_J=U^{A_{\rm mix}},\qquad
 A_{\rm mix}=r+2m+z_J .
\]
The whole mixed polynomial has the exact row-independent coefficient
\[
 B(n)=\sum_{d k_1 k_2\prod_jp_j=n}
   \mu_F(d)A_0(\mathrm Nd/D)
   B_0(\mathrm Nk_1/N)B_0(\mathrm Nk_2/N)
   \prod_j a_j(p_j)W_j(\mathrm Np_j/P_j), \tag{3}
\]
where all original supports and good exclusions remain. Its central
normalizer is \(X_{\rm mix}^{-1/2}\). This is a three-variable convolution,
with a Möbius inverse variable, rather than the two-plain coefficient of
source (18.18).

The first full-row Poisson calculation still has a harmless zero frequency:
the sextic mean forces a powerful full-product ideal, allocations are
divisor-bounded for the fixed number of factors, and central normalization
gives \(O(U^{1+\varepsilon})\). This is below the desired mixed target by
the positive \(dr-1/540\).

For nonzero frequencies the source arithmetic formula (18.21), printed
p. 161, remains valid for the allocated mixed convolution on its genuine
coprime locus. Use \(c_C,c_D\) for the logarithmic norms of the two complete
common-support factors, \(R\) for the active common radical length, \(E\)
for the complementary mask-divisor length, \(p\) for the common radical
length and \(s_0\) for the later coprimality divisor length. Put
\[
 e_q=q+R+E,\qquad
 B_C=\left(\frac{3c_C-5c_D-R}{6}\right)_+,
 \quad
 B_D=\left(\frac{3c_D-5c_C-R}{6}\right)_+ .
\]
The primitive Gauss scalar and every common physical mask stay present
until positive norms have formed.

After the source's whole-product Fourier separation, one side has the
new mixed Gauss norm
\[
 \mathcal N_C^{\rm mix}
 =\sum_{h\ne0}\omega_K(\mathrm Nh/U^K)
 \left|U^{-(A_{\rm mix}-c_C)/2}
       \sum_{s\mid a}A_C^{\rm mix}(a)\tau_C'(a)
                   (\mathrm Na)^{it}G(a,h)\right|^2. \tag{4}
\]
Here \(A_C^{\rm mix}\) retains the actual allocated Möbius inverse
coefficient, profiles, masks, live slot coefficients and, when present,
the full centered two-plain difference. It is not an arbitrary vector.

Set \(\Lambda=dr-1/540\). A concrete sufficient analytic bridge at this
step is the estimate
\[
 \boxed{\mathcal N_C^{\rm mix}
   \ll U^{A_{\rm mix}-c_C+e_q+B_C-s_0+\Lambda+\varepsilon}H^b,}
 \tag{5}
\]
and its \(D\)-side counterpart, uniformly in genuine frozen allocations,
divisor labels, allowed twists, masks and required derivative profiles.
This is the marked replacement of source (18.23), printed p. 163.
It is a sufficient norm bound, not a necessary characterization of the
original selected fourth target.

Indeed the unchanged first-transform ledger gives
\[
 (m_{\rm row}-A_{\rm mix}-R/2-E)+(p+s_0)
 +\frac12\!\left[
  2A_{\rm mix}-c_C-c_D+2e_q+B_C+B_D-2s_0+2\Lambda\right]
 =M+\Lambda+\frac12[B_C+B_D-(c_C+c_D-2p-R)] .
\]
The last bracket is nonpositive by source (18.24), whose proof uses only
local sextic multiplicities. Thus (5) would close the full positive mixed
bound at \(U^{M+\Lambda}\), in particular the physical application \(M=1\),
subject to the source's complete separation and uniformity obligations.
The source proof of (18.23) does not prove (5): its induction closes on
two plain factors and original prime slots.

There is an additional exponent obstruction to a plug-in induction.
The new full length satisfies \(A_{\rm mix}>1\), whereas the physical
parent width is \(M=1\). The second-transform diagonal ledger (18.31),
printed p. 166, has excess \(A_{\rm mix}-M\) before its terminal losses.
The exceptional-row optimization (18.50), printed p. 178, uses the same
\(A\le M\) requirement in its positive-slot branch. The allowed new
budget \(\Lambda\) does not absorb that excess:
\[
 A_{\rm mix}-1-\Lambda
 =(1-d)r+2m+z_J-1+\frac1{540}
 >\frac{103}{500}+\frac1{540}
 =0.2078518518\ldots \tag{5a}
\]
on the coarse working box \(r\ge7/10\), \(m>2/5\), \(d\le21/50\),
\(z_J\ge0\). This is a limitation of that separately positive diagonal
majorant, not a lower bound for the original mixed moment.

In particular (5) is only a precisely located sufficient new inequality.
The source's second-transform diagonal estimate cannot prove it by
unchanged power bookkeeping. A marked argument must improve its actual
coefficient estimate or preserve cancellation with other transformed
terms, or avoid this positive norm reduction. Reflection of just the two
plain variables also leaves the inverse length untouched, so the source
comparison's total-length calculation cannot be reused with
\(A_{\rm mix}\) substituted for its two-plain length.

## 4 Exact closure issue at the artificial divisor allocation

On p. 169, the source allocates each artificial coprimality prime among
the two plain variables and live slots. Selecting a plain variable permits
an unrestricted quotient and merely extracts a scalar and a norm power.
Selecting the new inverse variable instead requires the exact identity
\[
 \mu_F(pv)=-\mu_F(v)\mathbf1_{(v,p)=1}. \tag{6}
\]
The new indicator affects the inverse variable alone. It is not the old
common puncture shared by every remaining factor, and cannot be omitted.
The complete Möbius allocation must therefore be redone for the marked
coefficient class; the source common-coefficient lemma cannot be cited
unchanged.

Likewise source reflection acts on the two plain factors only.
For an exceptional child, freezing an inverse label can leave the two
plain sums' equal-product main terms equal, so their lattice cancellation
need not disappear. What is missing is a bound for summing those inverse
labels with their Möbius signs and masks afterwards. Taking their absolute
volume is a genuine additional power cost, not a proof of (5).

## 5 Selection, orientation and height audit

Permitted positive enlargements are: the full uncentered mixed square;
the full centered square if the comparison has separately been bounded;
and nonnegative child norms only after separation and exact allocation.
Forbidden substitutions are: Poisson on the unsmoothed detector indicator
without a new transform; positivity for a signed low-gcd or high-core
piece; and enlarging a signed exceptional/nonexceptional partition before
the source's positive or absolute-product step on p. 171.

All whole-slot coefficient restrictions remain. A divisor-completed
row-dependent profile from note 15 is not inserted into source Lemma 18.1
as a newly allowed profile. It can only be expanded into its original
divisor states before a new analytic estimate.

For the common opposite native orientation, conjugate the entire
polynomial and its fixed ray coefficient consistently; conjugation
preserves its norm and all zeros. A canceled sextic factor remains the
zero-extended principal character. The fixed group must contain the
needed finite ray phases; moving good-prime factors cannot be absorbed
into it.

The source fourth proof uses global family growth for its prime estimate,
whole-product Fourier separations with one norm power per side, and a
fixed polynomial in separated heights. The inverse's buffered estimate
is only available on the original selected bin and its assigned central
frequency domain. Transformed child rows need not lie in that bin.
Moving the inverse bound onto them would require either a justified
global input or a new marked child theorem. All internal derivative and
height orders must be fixed before the later external tail order, as
recorded on pp. 179–180. The present audit establishes none of these new
marked estimates.

This completes phase 1 only. The next bounded analytic test should choose
one marked norm or one selected near-coprime block and demonstrate its
actual exponent; further algebraic reindexing alone does not establish
the required \(1/540\) gain.
