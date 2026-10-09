# The plain fourth proof with an actual annular inverse inserted

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model internal proof audit,
not independent specialist review or formal verification.

Scope: phase 1 only. Read the complete relevant pages 153–180 of the
[30 September primary manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
in memory. SHA-256:
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Visually checked page 161's first Poisson normalization and conjugations.
No source PDF or long source extraction is saved.

**Finding.** There is no inverse-weighted theorem hidden in Lemma 18.1.
The inverse can be inserted exactly, and it does not destroy the two-plain
rectangle cancellation merely because its coefficient is Möbius. The
obstruction is closing the Gauss-norm/child coefficient family while
retaining compensation between inverse labels. Freezing those labels
keeps the ordinary centered plain identity, but absolute aggregation
spends the inverse volume. Retaining the signed sum instead produces a
new bilinear Gauss-bridge norm that the cited proof does not estimate.

## 1 The source interfaces

The following short map identifies the interfaces used in this audit.
The deep source estimates remain imported; the audit does not replay
their global arithmetic or automorphic dependencies.

| Pages / equation | Interface |
| --- | --- |
| 153–157, 18.2–18.12 | Two plain factors, finite-ray prime slots; common masks, reflection and pointwise prime bounds. |
| 158–159, 18.17–18.18 | Equal-product rectangle difference; enlarge its nonnegative norm to smooth rows. |
| 160–163, 18.21–18.23 | First Poisson, complete common-support extraction, full coprimality inversion, Cauchy in frequency; allocated positive Gauss norms. |
| 163–165, 18.28–18.30 | One sixth-power row amplification; second Gauss transform. |
| 166–173, 18.32–18.40 | Whole-product separation and full Möbius allocation; smaller-width two-plain children, masks and whole-slot removal. |
| 174–178, 18.41–18.50 | Exceptional-character count and common masked rectangle cancellation. |
| 178–180, 18.52 | Finite width induction and fixed-order derivative/height propagation. |

With source width \(M\), total plain-plus-slot length \(A\), complete
support lengths \(c_L,c_R\), new moving support \(\widetilde q\), and
coprimality divisor length \(s_0\), its first-transform target is
\[
 \mathcal N_L\ll
 U^{A-c_L+\widetilde q+B_L-s_0+\varepsilon_G},
 \qquad
 B_L=\max\{0,(3c_L-5c_R-R)/6\}.
 \tag{1}
\]
The Gauss norm has the exact structure
\[
 \mathcal N_L=
 \sum_{h\ne0}\omega_K(Nh/U^K)
 \left|U^{-(A-c_L)/2}
   \sum_{s\mid n}\mathcal A_L(n)\tau_L'(n)(Nn)^{it}G(n,h)
 \right|^2.
 \tag{2}
\]
The allocated coefficient \(\mathcal A_L\) contains the whole rectangle
difference, all live slots and every fixed mask. The source does not
claim (1) for arbitrary divisor-bounded coefficients. Its proof derives
it by carrying exactly that coefficient class through the second transform.

In source notation the second transform has nominal child width
\(M'=M+J-g-g_2+t_2\le M-\sigma\) (18.32), with inner allowance
\(M'+\Delta_{\rm child}\),
\(\Delta_{\rm child}=b_2-p_2+w+B_L+\ell\) (18.33).
The eventual nonexceptional children have two plain factors and surviving
original slots. The proof's width decrease is not an estimate for an
additional inverse-weighted child.

## 2 Exact insertion before the first transform

Keep the actual source-compatible profiles, whole slots, characters and
the original selected physical row set. Put
\[
 X=U^A=X_1X_2\prod_{i\in J}P_i,
 \quad D=U^r,
 \quad a_D(d)=\mu_F(d)A_0(Nd/D).
\]
Let \(B(n)\) be the ordinary plain/slot convolution coefficient before
its common character is applied. Its full-product support is \(Nn\asymp X\).
Then the exact mixed polynomial is
\[
 M_uS_{1,u}S_{2,u}Q_J(u)
 =(DX)^{-1/2}\sum_{d,n}a_D(d)B(n)\psi_u(dn).
 \tag{3}
\]
Complete multiplicativity includes the original zero extensions. Thus
the first Poisson full-index scale is \(DX\), and the total column
length is \(A_\mu=A+r\), rather than \(A\). It is not the ratio radical
or the sixth-power-free representative norm. Every inverse and plain
annulus in (3) stays at its original scale.

If centering is used, replace \(B\) by the full common coefficient for
the equal-product rectangle difference. Multiplying this difference by
the same inverse is exact. However, the comparison term also retains
that inverse and needs its own mixed estimate. Bounding the comparison
by the existing plain fourth moment and the inverse envelope recovers
only \(U^{1+dr}\).

One may enlarge a nonnegative full norm of (3), or of the full mixed
rectangle difference, to a smooth complete row ball. This produces a
stronger sufficient arithmetic problem; it does not identify the signed
near-coprime remainder with a complete-row norm. Poisson cannot be
applied directly to that selected signed remainder by this positivity
argument. If retaining the selector exactly, its weighted row kernel
must remain inside every inverse-pair sum.

Freezing an inverse pair creates \(\psi_u(d)\overline{\psi_u(d')}\)
as an oscillatory character on the original row. This is not automatically
the source's common fixed column twist \(\tau(n)\). In particular,
changing \(q\) to \(\log_U Nf\) and quoting Lemma 18.1 is not a valid
substitution. Combining the full indices \(dn,d'n'\) as in (3) is the
safe insertion.

## 3 The first sign-loss fork

Suppress complete-support allocation labels temporarily. The inserted
Gauss polynomial has the exact form
\[
 \mathscr G_\mu(h)=D^{-1/2}
       \sum_d a_D(d)\mathscr G_d(h),
\]
\[
 \mathscr G_d(h)=X^{-1/2}\sum_n B(n)\tau'(dn)
          (Ndn)^{it}G(dn,h)\mathbf1_{s\mid dn},
 \tag{4}
\]
with all physical and fixed masks still present. After a complete-support
allocation, the same statement uses the exact shortened inverse and
plain scales, and the exact central extraction coefficients.
Its squared frequency norm is the native bilinear kernel
\[
 \mathcal Q_\mu
 =D^{-1}\sum_{d,d'}a_D(d)\overline{a_D(d')}
                         \mathscr K(d,d'),
\]
\[
 \mathscr K(d,d')=
 \sum_{h\ne0}\omega_K(Nh/U^K)
                         \mathscr G_d(h)\overline{\mathscr G_{d'}(h)}.
 \tag{5}
\]
The first source Cauchy step may be applied to the full combined
polynomial, preserving (5), but then its Gauss norm has this new
inverse-bearing coefficient. The source's bound (1) does not cover it.
Alternatively, freezing inverse labels and placing them in the absolute
outer-label measure discards \(\mu_F(d)\mu_F(d')\) compensation.
Minkowski then spends
\[
 \left(D^{-1/2}\sum_d|A_0(Nd/D)|\right)^2\asymp D
 \tag{6}
\]
for a nonzero fixed annular profile. Separate absolute inverse-pair
aggregation has the same volume. A bound for each fixed inverse label
therefore does not give the desired signed aggregate. The inherited
pointwise inverse envelope is better than this volume bound, but still
supplies no extra \(1/540\) gain.
Here the sums are on the squarefree inverse support. The displayed
volume is the raw annular coefficient mass after signs are discarded;
it is not a lower bound for the masked Gauss norm or actual selected
energy. Moving physical zeros must remain in \(\mathscr G_d\).

The external elementary bound that first loses the requested gain is
precisely \(F_J\le\sup_{u\in\mathcal C_+}|M_u|^2\sum_uV_u\).
That inequality is not a step of the source proof, which contains no
inverse factor in Lemma 18.1. Inside a replayed proof, the corresponding
fork occurs at the first Gauss-norm interface on pages 162–163.

## 4 A precise sufficient bridge lemma

For every genuine allocation from (3), form the inverse-bearing
coefficient and native Gauss norm exactly as in (2), with total length
\(A_\mu\). Require the same allowed profiles, source frequencies, whole
slots and masks, including variable-specific inverse deletion masks.
One sufficient bridge is
\[
 \boxed{\mathcal N_{L,\mu}
  \ll U^{A_\mu-c_L+\widetilde q+B_L-s_0+\alpha+\varepsilon_G},}
 \tag{7}
\]
and its right-side analogue, where at the original physical application
\(\alpha=dr-1/540-\sigma_1\) for a specified positive reserve
\(\sigma_1\). The source's first-transform exponent ledger then adds
\(\alpha\) to its final width bound because Cauchy averages the two side
allowances. Its local common-support inequality remains valid for the
actual full multiplicities. Proving the bridge uniformly over the
centered and comparison coefficients would give the stronger full
positive mixed estimate; its selected version gives the desired target.

This formulation is a genuinely new norm estimate, not an assertion that
the source induction already proves it. If attempted recursively, it must
track the residual inverse length, its exact coefficient and mask, and
the exponent allowance through the smaller-width children. In particular,
source 18.2's coefficient-closure lemma and the moment invocation on
pages 171–173 must be replaced by corresponding mixed statements.

At a final coprimality allocation, selecting a prime in an inverse variable
uses \(\mu_F(pe)=-\mu_F(e)\mathbf1_{(e,p)=1}\). That added puncture is
specific to the inverse quotient; it cannot be silently promoted to a
common puncture of both plains. The amplification valuations 1, 6 and 7
also need allocation to the inverse: squarefreeness eliminates impossible
inverse powers, but a permitted valuation one retains the extra inverse
mask and sign. These are concrete closure obligations for (7).

## 5 Exceptional rectangle cancellation is preserved

For a fixed inverse label on an exceptional child, its Möbius coefficient,
inverse profile and remaining character factors are common to both plain
rectangles. They multiply, rather than alter, their main-term cancellation.
The same observation holds after restoring the inverse sum whenever
the allocated inverse mask remains independent of the two plain labels.
Consequently there is no basis for declaring that Möbius coefficients
destroy source Lemma 18.3's two-plain lattice cancellation.

What fails is using that lemma as an inverse estimate. It evaluates plain
finite-ray sums, not \(\mu_F\)-weighted annular sums. After the plain
main terms cancel, the residual inverse amplitude must still be bounded
with its own source-compatible reciprocal estimate or signed correlation.
The local bin inverse estimate does not automatically apply to transformed
child rows; those may require the global family strip and its admissible
heights. Absolute aggregation of frozen inverse labels is again subject
to (6). These costs must be included in any mixed exceptional-child ledger.

## 6 Phase-1 disposition and a legitimate next native test

The bridge (7) is the exact new operator family exposed by this audit.
No inverse-weighted fourth estimate has been proved. The audit explains
both a valid positive enlargement and the obligation to retain the actual
selector on the original signed remainder, rather than conflating them.

After phase 1, the proposed \(g=1\) coprime Euler resummation is a serious
native test: it retains every signed inverse pair and the original two
Mellin profiles, with each selected row and its zeros fixed. Its collision
factor tests whether existing reciprocal contours suffice or whether a
new averaged correlation is needed. The present source central inverse
line is buffered to the right of the bin parameter a; reducing the total
Mellin real part by \((1/540)/r\) is a new contour obligation and can
encounter a selected witness zero. Thus that resummation should be used
to decide feasibility, without assuming the correction cancels such poles
or claiming a proof for the entire surviving gcd range. Phase 2 was not
executed in this audit.
