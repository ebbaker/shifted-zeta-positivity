# Conditional geometry theorem and analytic dependency ledger

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Parallel follow-up checks use the inherited model configuration and are
internal checks, not independent specialist validation.

The geometry candidate can be stated as one conditional theorem. Its
conclusion remains a family boundary of \(20999/24000\); it requires no
new mixed inverse/plain estimate. The continuation and height-selection
steps below have direct proofs, reducing the list of imported assertions.
The difficult dependencies are still the reflected energy estimate, the
canonical inverse recursion, and the centered fourth-moment induction.
Consolidation makes their audit concrete but does not validate them.

The reference is the [September 30 source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
PDF SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Its Proposition 2.1, Proposition 8.3, Lemmas 14.3, 17.1, 17.6, and 18.1,
and the order of choices in Section 20.6 were checked against the local
extracted source. The previous [geometry certificate](GEOMETRY_OPTIMIZATION_20261008.md)
and [low](../reviews/LOW_STRUCTURAL_AUDIT_20261008.md),
[moment](../reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md), and
[contour](../reviews/CONTOUR_TRANSFER_AUDIT_20261008.md) audits specify the
remaining transfer calculations.

## A single conditional family theorem

Let \(\beta_*\) be the supremum of real parts of nontrivial zeros over
primitive finite-order Hecke characters of \(F=\mathbb Q(\sqrt{-3})\).
Assume the source family bound \(\beta_*\le7/8\). Assume the following
structural assertions, with their full coefficient, zero-extension,
moving-modulus, and height uniformity, in the geometry displayed below.

1. The exact physical reflection and compensated finite probe of Sections
   6, 7, 12, and 16; the reflected energy estimate of Lemma 14.3; and the
   additive Gram estimate used in Section 15. The probe is defined by its
   completed sums before estimating or introducing its high integral.
2. The buffered zero bins, pointwise bounds, and simultaneous witnesses of
   Section 8, including Proposition 8.3 and its literal height ceiling.
3. Lemma 17.1 with fixed strict width decrements, and Lemma 17.6 on the
   sixth-power-free physical rows, uniformly across inverse length one.
4. Lemma 18.1 at fixed \(\kappa=3/4\), with a mesh independent of the
   later fixed slot count; its zero-slot case; and the native disjoint
   prime supports and finite ray-character coefficient class.
5. The complete correction and contour bounds of Sections 7, 10, 13,
   and 16, with the principal Euler domain enlarged to
   \(\Re s\ge87/100,\Re w\ge19/20,\Re z\ge33/200\), as verified
   in the contour audit. These include the positive prime normalizer,
   the common excluded set, and external decay orders that do not
   change previously fixed internal height orders.

**Conditional theorem.** Under these assumptions, every finite-order Hecke
\(L\)-function over \(F\) has no nontrivial zero with
\[
\Re s>\sigma_0=\frac{20999}{24000}
=\frac78-\frac1{24000}.
\]
In particular the same exclusion holds for zeta. The local fixed-probe
variance consequence is \(O(X^{32999/12000})\), under the profile
hypotheses of the existing variance equivalence.

The family baseline is essential here: a zeta-only seven-eighths
assumption does not satisfy the positive-slot hypothesis in item 4.
The theorem is an application of assumed analytic estimates, not an
independent proof of the source baseline or its moment machinery.

## Exact exponents and the family contradiction

Set
\[
\ell=\frac{1001}{6000},\quad b=\frac18,\quad
l_x=\frac{4249}{12000},\quad l_y=\frac{5749}{12000},\quad
h=\frac{3251}{4000}.
\]
Then \(l_x+l_y+\ell=1\), \(l_y-l_x=b\), and
\[
C(s)=s-\frac{11}{16},\qquad
L=\frac{l_x}{2}+\frac b{12}=C(\sigma_0).
\]
For every rescaled subset of length \(v\in[0,\ell]\), the complete
low contribution has excess
\[
-v+\frac{(5\ell-1+v)_+}{8}\le0.
\]
This pays the subset energy excess before taking its low bound.

Suppose \(\Delta_0=\beta_*-\sigma_0>0\). Then
\(0<\Delta_0\le1/24000\), and every live bin has
\(1/50<\delta=2a-1\le3/4\). Fixing \(\kappa=3/4\) is therefore
legal, and no negative version of the source's capacity penalty is used.
Writing \(x=q/\delta\), the retained count uses
\[
\alpha=5/6,\quad D_x=3-17x/9,\quad
P_x=(2-8x/9)(1-x),\quad
J=(\alpha-\delta)D_x+\delta P_x,
\]
\[
t=1+\frac{\delta P_x}{2J},\qquad
R^*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J}.
\]
This is obtained by repeating the inverse/plain comparison at the fixed
permitted parameter, rather than quoting Proposition 19.2 with a
negative \(\beta_*-7/8\). Whole-slot selection pays fixed rounding
and capacity costs, and every physical slot stays in the original probe.

An explicit check of the unspecialized high identity is useful. At
\(d=h\), let \(z_0=17/50\) and \(a=(1+\delta)/2\). The error-free
exponent relative to \(C(\sigma_0)\) is
\[
E_{\sigma_0}(h)
=a-\sigma_0+h(z_0-1/6)-a l_y-\ell/2+q\ell
 +h(R^*+\delta/2-z_0)
\]
\[
=h(R^*+1/2+\delta)-1-b(7/12+\delta/2)
 +\ell(q-1-\delta/2).
\]
The existing exact polynomial certificate gives
\[
E_{\sigma_0}(h)\le-\frac{12977}{4408214400}
<-m_0,\qquad m_0=\frac1{400000}.
\]
The exponent relative to the hypothetical family edge is consequently
\[
E_{\beta_*}(h)=E_{\sigma_0}(h)-\Delta_0
\le-m_0-\Delta_0.
\]
This subtraction must remain explicit. The complete floor, middle, small,
and principal margins exceed \(m_0\); a frequency extension
\(\zeta=1/6400000\) costs at most \(2\zeta=m_0/8\). The absolute
large-row contour is chosen sufficiently far right after this fixed
extension. The strict supply condition remains
\(\ell/(h+\zeta)>1/5>7/37\).

## The normalizer changes the final margin

The geometric margin \(m_0\) is not the final common theorem margin.
Choose the moment losses first and obtain the source mesh. Choose a fixed
even \(K\) large enough for that mesh, the strict widths, and rounding;
take \(\ell_i=\ell/K\) and the disjoint windows of the source
construction. No numerical upper bound for this \(K\) follows from the
stated qualitative mesh theorem.

The prime-normalizer approximation must then receive its own positive
saving. One permitted conservative choice is
\[
m_P=\frac{87}{200}\frac{\ell}{K}
=\frac{87087}{1200000K}
<\frac{87}{100}\min_i\ell_i.
\]
The other principal margins are
\(m_w=l_y/20\) and \(m_z=h/600\). Reserve a total moderate-range
cost below \(m_0/2\), including the extension, moment and witness
losses, dyadic multiplicity, and subpower normalization. After \(K\)
is fixed, choose the additional principal powers small enough to retain
at least half of \(m_w,m_z,m_P\). A safe common retained saving is
\[
m=\frac18\min\{m_0,m_w,m_z,m_P\}>0.
\]
At \(K>29029\), this choice of \(m_P\) is smaller than \(m_0\).
This is a limit of this conservative ledger, not an obstruction to the
candidate boundary: the fixed slot count leaves a positive saving.
It prevents treating the rational endpoint margin as a numerical bound
for every part of the final analytic theorem.

All these real choices are common to the family. Low losses can be taken
below \(\Delta_0/2\), giving \(\omega=\Delta_0/2\). The final set
of excluded primes, physical probe, principal correction, normalizer,
and Mellin signal use identical arithmetic data for each fixed target.
The two functions below do not depend on the auxiliary height cutoff.

## Direct height absorption

For each target \(\eta\), the structural estimates give finite orders
\(A_\eta\ge0,B_\eta\in\mathbb R\) and a positive permitted height ceiling
\(\tau_{0,\eta}\), all fixed before the external order \(N\):
\[
|J_\eta(Z)-f_\eta(Z)|
\ll_{\eta,N}Z^{C(\beta_*)-m}(1+T)^{A_\eta}
 +Z^{B_\eta}T^{-N}.
\]
Choose
\[
0<\tau_\eta\le
\min\{\tau_{0,\eta}/2,m/[4(A_\eta+1)]\},\qquad T=Z^{\tau_\eta}.
\]
The first term is \(O_\eta(Z^{C(\beta_*)-3m/4})\). Choose an integer
\[
N_\eta>\max\{0,(B_\eta-C(\beta_*)+m/2)/\tau_\eta\}.
\]
The second term is \(O_\eta(Z^{C(\beta_*)-m/2})\). Thus the common
high saving is \(\sigma=m/2\), even though the height exponent and
threshold vary with the target. This proves the needed instance of the
height-selection lemma directly. It requires the structural assertion
that increasing \(N\) leaves \(A_\eta,B_\eta\) unchanged.

## Direct Mellin continuation

For the fixed target let \(H_\eta\) be holomorphic on
\(\Re s>\sigma_0\), and let
\[
f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds,
\qquad \sup_{\Re s>\sigma_0}|H_\eta(s)-1|\le\frac12.
\]
The low estimate and the absorbed high estimate imply, with
\(\epsilon_* =\min\{\Delta_0/2,m/2\}>0\),
\[
f_\eta(Z)=O_\eta(Z^{C(\beta_*)-\epsilon_*})\quad(Z\to\infty).
\]
At zero, the line can be moved to any fixed \(\Re s=B>2\): the
Gaussian decays on horizontal joins, the Euler reciprocal is bounded
there, and \(H_\eta\) is bounded. Hence
\(f_\eta(Z)=O_{\eta,B}(Z^{B-11/16})\) as \(Z\downarrow0\).
Its Mellin transform
\[
F_\eta(s)=\int_0^\infty f_\eta(Z)Z^{-C(s)}\frac{dZ}{Z}
\]
is holomorphic for \(\Re s>\beta_*-\epsilon_*\). Fourier inversion
on the original line, followed by the identity theorem, gives
\[
F_\eta(s)=e^{(s-5/6)^2}H_\eta(s)/L_F^S(s,\eta)
\quad(\Re s>1).
\]
Since \(|H_\eta|\ge1/2\) on the relevant half-plane, this continues
the reciprocal holomorphically to \(\Re s>\beta_*-\epsilon_*\).
Deleting finitely many Euler factors neither creates nor removes zeros
in this half-plane. The same \(\epsilon_*\) works for every target,
contradicting the definition of \(\beta_*\). The supremum need not be
attained. This proves the continuation step without importing
Proposition 2.1 as an additional assumption.

## Dependencies to audit next

| Imported assertion | Exact role | Decisive audit question |
| --- | --- | --- |
| Original family boundary \(\beta_*\le7/8\) | Legality of fixed \(\kappa=3/4\) | Is the global family theorem valid with the same definition of \(\beta_*\)? |
| Reflection and Lemma 14.3 | Low energy and base estimates in the inverse recursion | Are the frozen base, active slots, residual-row annulus, and collision masks retained simultaneously? |
| Lemmas 17.1 and 17.6 | Marked short inverse count and uniform long inverse count | Does the canonical recursion close with all principal children, tails, punctures, and fixed loss choices? |
| Lemma 18.1 | Plain fourth count with prime capacity \(2(1-2m)/9\) | Does centered cancellation handle every transformed \(\Theta\)-row, with the claimed coefficient class and a mesh independent of \(K\)? |
| Section 8 detector and buffered bounds | Simultaneous witness rows and inverse denominators on retained contours | Are the rowwise presentation, shared height, preliminary losses, and all literal height ceilings compatible? |
| Full correction and principal normalizer | Exact high identity and nonvanishing common signal | Are every subset and mask retained before moving contours, and are normalizer errors paid after the fixed slots are chosen? |

The first three substantial proofs should receive expert or formal audit
before the conditional candidate is promoted to an established theorem.
The direct Mellin and height arguments above are useful reductions in the
ledger, but they do not substitute for those arithmetic proofs. Further
optimization of the fixed-\(b\) envelope remains a low priority.

The [new checker](../numerics/check_geometry_dependency_ledger.py) verifies
the unspecialized high identity, the normalizer threshold, and the
quantified height and contradiction arithmetic. Its finite cases check
algebra and allocation logic; the analytic proofs are the arguments
above and the explicitly assumed source estimates.
