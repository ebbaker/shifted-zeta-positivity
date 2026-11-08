# BGST import: version-pinned source check

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Actual backend model and reasoning
effort are unavailable: this chat's registered model-configuration list is
empty. Thread `01a1bbc3-acff-7b90-93d7-02a41152fda4`, chat0004.

**Disposition: the parent manuscript's cumulative equation `eq:BGST`
survives unchanged.** It is exactly the normalization of the **first line
of (3.5)** in [arXiv:2501.14545v3, §3](https://arxiv.org/html/2501.14545v3#S3),
printed p.8. The correction notice does not require weakening that
equation. Cite the corrected proof, distinguish it from the dyadic
statement (3.2), and do not import the erroneous multiplicative remainder
reproduced on p.7.

This is a bounded internal LLM source/import assessment, not an independent
proof of every arithmetic input, a B04 route comparison, or the pending
E03 assessment. It supplies no new canonical estimate or RH gain.
The [result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md) govern this check,
particularly [source use16](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md),
[normalization08](../../../../../../avoid/08_normalization_and_constant_slips.md),
[classification01](../../../../../../avoid/01_restating_the_target.md) and
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Sources actually compared

- **Correcting source:** Siegfred Alan C. Baluyot, Daniel Alan Goldston,
  Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, *Pair Correlation
  of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and
  Critical Zeros*, [arXiv:2501.14545v3](https://arxiv.org/abs/2501.14545v3),
  submitted 1 September 2026; PDF dated 8 June 2026. Checked §3, pp.7–10,
  including the correction, (3.1)–(3.8), both lines of (3.5), and the
  cross-interval error in the dyadic proof. HTML and retained PDF agree
  on the relevant formulas. Pages7–9 were rendered and visually checked.
- **Earlier pinned source:** the same authors, *An unconditional Montgomery
  Theorem for Pair Correlation of Zeros of the Riemann Zeta Function*,
  [arXiv:2306.04799v1](https://arxiv.org/abs/2306.04799v1), submitted
  7 June 2023; PDF dated 9 June 2023. Checked Theorem1/(1.2)–(1.4), p.1,
  and Lemmas2–3/(2.4)–(2.6), p.3. Page1 was visually checked. Theorem1
  literally prints the additive formula used in the manuscript.
- **Local consumer:** [11_complex_statistics.tex](../../manuscript/sections/11_complex_statistics.tex),
  `thm:BGST`/`eq:BGST`, and its direct dependencies below. The later
  paper's description of the erroneous earlier formula is not a literal
  reproduction of pinned v1's (1.4). The 2024 journal text was **not**
  inspected in this check; no claim is made about exactly when that
  difference entered the publication history.

Existing reading copies were reused and their recorded SHA-256 hashes
matched. The [execution receipt](../numerics/BGST_IMPORT_SOURCE_CHECK_20261108.json)
records identities, inspected pages, local input hashes and checks.
Hashes identify bytes, not mathematical validity. Canonical article
annotations remain in [source-use04](../references/04_TND_OC_PAIR_MARGINAL_LITERATURE_SOURCE_USE_20261108.md)
and [parent source-use07](../../references/07_TND_O_B03_COMPLEX_ZERO_STATISTICS_SOURCE_USE_20261106.md).

## 2. Exact import and normalization

Put \(\ell=\log T\), \(B_T=T\ell/(2\pi)\), and let
\[
 \mathcal F_I(x)=\sum_{\rho,\rho':\,\gamma,\gamma'\in I}
 x^{\rho-\rho'}\frac4{4-(\rho-\rho')^2}.
\]
These are ordered sums over all nontrivial zeta zeros in the specified
interval, counting multiplicity in **both** indices and including self
pairs. No RH, simplicity or narrow-box assumption is used in §3.

The first line of v3 (3.5), for \(I=(0,T]\), states uniformly for
\(1\le x\le T\), as \(T\to\infty\),
\[
 \mathcal F_{(0,T]}(x)
 =\frac{T}{2\pi x^2}(\ell^2+O(\ell))
  +\frac{T}{2\pi}\log x+O(T\sqrt\ell).                 \tag{C}
\]
Substitute \(x=T^\alpha\) and divide every term by \(B_T\). This
gives, uniformly on the **closed** interval \(0\le\alpha\le1\),
\[
 F_{\rm c}(\alpha,T)
 =T^{-2\alpha}(\ell+O(1))+\alpha+O(\ell^{-1/2}).       \tag{N}
\]
This is the existing parent equation exactly. In particular, the
\(O(1)\) stays inside the \(T^{-2\alpha}\) factor, whereas the final
\(O(\ell^{-1/2})\) is an **absolute additive** error. Realness,
evenness and nonnegativity are preserved; the finite reflection/Gram
proof in the manuscript does not depend on the disputed error estimate.

For \(I=(T,2T]\), v3's stated theorem (3.2) instead gives the convenient
weaker normalized form
\[
 \frac{\mathcal F_{(T,2T]}(T^\alpha)}{B_T}
 =T^{-2\alpha}\ell+\alpha
  +O\bigl(T^{-2\alpha}\sqrt\ell+\ell^{-1/2}\bigr).      \tag{D}
\]
The second line of (3.5) deliberately weakens (C) to the same error
format. At \(\alpha=0\), (N) has error \(O(1)\), while (D) permits
\(O(\sqrt\ell)\). These are different printed bounds for different
interval conventions; (3.2) alone does not justify the sharper first
error in the cumulative manuscript statement. Equation (3.5) does.

## 3. What the correction changes

The formula identified as erroneous on v3 p.7 is
\[
 \left(\frac{T\ell^2}{2\pi x^2}
       +\frac{T}{2\pi}\log x\right)(1+O(\ell^{-1/2})). \tag{M}
\]
After normalization its error would be
\(O(T^{-2\alpha}\sqrt\ell+\alpha\ell^{-1/2})\), not the
additive error in (N). These are not interchangeable uniformly down
to \(\alpha=0\).

For the diagnostic scale \(x=c\ell\), with fixed \(c>0\), (M)
would leave an unnormalized error
\(O_c(T\log\ell/\sqrt\ell)=o(T)\). It would therefore determine a
lower-order term of size \(T\), which the authors identify as
incorrect. The corrected \(O(T\sqrt\ell)\) allowance does not
determine that term. Our normalization check explains why (N) also
does **not** determine it: its \(O(\ell^{-1/2})\) allowance exceeds
the main term's order \(\log\ell/\ell\) at this scale.

Thus the source warning was appropriate pending inspection, but it must
not be upgraded into a finding that the manuscript's displayed formula
is false. The authors' p.7 footnote preserves their earlier applications;
that statement is not a substitute for the local dependency check here.

## 4. Check of the repaired proof's error bookkeeping

The proof on p.8 supplies
\[
 M_1=Tx^{-2}(\ell^2+O(\ell)),\quad
 M_2=T\log x+O(T\sqrt\ell),\quad
 M_3\ll Tx^{-2}+x.
\]
The nontrivial prime mean-square estimate for \(M_2\) and the explicit
formula underlying (3.4) remain external arithmetic inputs. They were
not independently re-proved or traced through every cited older paper.

Here is an independent check of the elementary passage from these inputs
to (C). Since \(M_1\ll T\ell^2/x^2\), \(M_2\ll T\ell\), and
\(1\le x\le T\),
\[
 \sqrt{M_1M_3}\ll T\ell/x^2+T\sqrt\ell,\qquad
 \sqrt{M_2M_3}+M_3\ll T\sqrt\ell.
\]
For the \(A_1\)-\(A_2\) cross term, integration by parts gives
\(\int_0^T n^{it}\log(t+2)\,dt\ll\ell/\log n\).
Even the elementary bound \(\Lambda(n)/\log n\le1\), followed by
splitting the sum at \(n=x\), yields
\[
 \left|\int_0^T A_1\overline{A_2}\,dt\right|
 \ll\frac\ell x\sum_{n\ge2}n^{-1/2}
           \min(n/x,x/n)
 \ll\ell/\sqrt x\ll\ell.
\]
This suffices; the extra logarithmic saving printed in the source is
unnecessary for (C). Finally, the \(O(\sqrt T+x)\) in (3.4) is
absorbed by \(O(T\sqrt\ell)\). There is no forced degradation of
\(O(T\ell/x^2)\) in this cumulative calculation.

For the dyadic theorem, the source subtracts cumulative sums and pays
cross-interval pairs. Its bound is
\(E_1\ll x^{2\Theta(2T)-1}\ell^3\), followed by the stated zero-free
region to obtain \(E_1\ll\sqrt T+x\). It does not simply identify
the dyadic double sum with a difference of cumulative double sums.
This part retains the source's zero-free-region input and yields (D).

## 5. Dependency findings and usable limits

The dependency search covered the parent operator subtree's manuscript,
notes, references and handoffs, excluding chat transcripts and generated
build products. It is not a repository-wide theorem audit.

| Consumer | Finding within this audit |
| --- | --- |
| `11_complex_statistics.tex`, `thm:BGST`/`eq:BGST` | Formula, multiplicities, normalization and frequency range accepted against v3 (3.5), first line. Add corrected-proof provenance. |
| `prop:complex-Gram` and positivity discussion | Exact finite reflection argument; no use of the asymptotic remainder. |
| `prop:horizontal` and ordinate PCC discussion | Elementary coincidence argument and a separately conditional GLSS input. The manuscript already says the density-one conclusion does not follow from BGST. |
| `prop:finite-defects` | Direct kernel/count estimate, independent of BGST's arithmetic proof. Its \(O(T^{-\eta}/\log T)\) perturbation is \(o((\log T)^{-1/2})\) for fixed \(\eta>0\), so its stated finite-change limitation survives. |
| `13_localized_statistics.tex`, `thm:BGST` reference | Correctly denies that the bulk theorem supplies expanded frequencies or a moving-window ordinate statistic. The finite weighted-Gram identities and their background payments do not use (M). |
| TND-OC B04 | May consume (C)/(N), or the dyadic (D), with their exact objects and errors. This audit does not evaluate or select B04's two candidate routes. |
| TND-OC E02/B02/E03 | No reassessment or status promotion; the frozen E03 input files are outside the edits. |

For a factorial sum, remove only the same **copy** in each self pair:
subtract \(N_I\) from \(\mathcal F_I\), or \(N_I/B_T\) from its
normalization. Do not remove all equal-position or equal-ordinate pairs.
Since \(N_I/B_T=1+O(1/\ell)\) for either interval, an asymptotic
replacement of this diagonal has its own error payment. A normalization
by the exact \(N_I\), rather than \(B_T\), also needs conversion.

In Newman coordinates \(z=2\gamma+i(1-2\beta)\),
\(\rho-\rho'=i(z-z')/2\). Consequently the kernel becomes
\(16/(16+(z-z')^2)\), and the exponential becomes
\(\exp(i\alpha\ell(z-z')/2)\). The dyadic ordinate band is
\(2T<\Re z\le4T\). This still controls one analytic difference
projection, not arbitrary separate transverse marks or a common-center
window. §3 supplies no short-window theorem, Newman-time uniformity,
derivative bound for its remainder, or numerical finite-height constant.

## 6. Control screen and disposition

Classification: repair of an existing literature import, not a proposed
RH-equivalent criterion or new exclusion mechanism. No zero simulations
are evidence for this source check. Applying the inherited
[collision screen12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [pattern02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md):
Euler-factor modifications fail the unchanged zeta arithmetic input;
weighted-square and finite-prime-orbit controls fail complete normalized
reflection; reflected super-Gaussian, smooth-shape and positive-primitive
controls lack the canonical theta arithmetic expansion. Other fixed
atomic/profile controls in that cluster also fail the unchanged complete
zeta/theta source. Their generic Gram positivity does not establish the
arithmetic asymptotic or a useful one-defect comparison. No universal
statistical obstruction is claimed.

**Source reconciliation is complete at the stated bounded scope.** The
canonical reference annotations now link this check. The manuscript's
mathematical statement requires no replacement; a future manuscript
integration should add the precise provenance: “For the cumulative sum,
the corrected proof in BGST, arXiv:2501.14545v3, §3, equation (3.5), first
line, gives the stated formula after normalization.” Use the existing
`BGST2026PairI` bibliography record. No manuscript source, reading PDF,
build record, B04 note, progress register, or historical continuation was
rewritten by this audit.
