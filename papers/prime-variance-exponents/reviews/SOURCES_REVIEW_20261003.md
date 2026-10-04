# Primary-source and bibliography review

3 October 2026. Internal source review prepared for Edward Baker with substantial
LLM assistance. Model: GPT-6 (Codex), inherited configuration; the exact serving
variant and configured reasoning effort are not exposed and are not inferred.
This is an internal LLM review, not specialist refereeing or independent
regeneration of the numerical certificates.

The specified primary texts support the arithmetic inputs in the
[continuation note](../notes/MANUSCRIPT_CONTINUATION_20261003.md), with the scope
qualifiers below. The four arXiv/publisher PDFs and the publisher or author
bibliographic records were consulted during this review. Some publisher direct
fetches returned access errors, but their indexed records and the primary author
preprints were available. No third-party PDF was added to the repository.

## PNT envelope

Daniel R. Johnston and Andrew Yang, *Some explicit estimates for the error term
in the prime number theorem*, **Journal of Mathematical Analysis and
Applications 527** (2023), no. 2, Article 127460.
[Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0022247X23004638),
[DOI](https://doi.org/10.1016/j.jmaa.2023.127460),
[author preprint, arXiv:2204.01980v2](https://arxiv.org/pdf/2204.01980v2).

Theorem 1.4, printed page 2 of the preprint, gives for every real \(t\ge23\)

\[
 |\psi(t)-t|\le0.026t(\log t)^{1.801}
 \exp\{-0.1853(\log t)^{3/5}(\log\log t)^{-1/5}\}.
\]

This is the stated **psi** bound, with all three constants as used by the
continuation note. The manuscript's complete-band supremum therefore applies
for \(X\ge23/A\). Squaring doubles 1.801 and 0.1853 to 3.602 and 0.3706.
That transfer remains at global exponent 3; no fixed power saving follows.
Use the published citation plus the versioned preprint for theorem numbering.

## Verified height

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
\(3\cdot10^{12}\)*, **Bulletin of the London Mathematical Society 53** (2021),
no. 3, 792–797.
[Publisher record and DOI](https://doi.org/10.1112/blms.12460),
[author preprint, arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1).

Theorem 1, printed page 2 of the preprint, actually verifies the height
3,000,175,332,800 and the lowest 12,363,153,437,138 nontrivial zeros.
Consequently the manuscript's \(H=3\cdot10^{12}\) is conservative. This is a
rigorous finite-height calculation using interval arithmetic and completeness
checking. It licenses critical-line location only within that height; it
does not replace the unconditional estimate of the remaining zero tail.
Conjugation supplies negative ordinates. No assumption of a database containing
all high-precision ordinates to \(H\) should be attached to the theorem.

## Zero count

Elchin Hasanalizade, Quanli Shen, and Peng-Jie Wong, *Counting zeros of the
Riemann zeta function*, **Journal of Number Theory 235** (2022), 219–241.
[Publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X2100233X),
[DOI](https://doi.org/10.1016/j.jnt.2021.06.032),
[author preprint, arXiv:2107.06506v1](https://arxiv.org/pdf/2107.06506v1).

Corollary 1.2, printed page 2 of the preprint, states for every \(T\ge e\)

\[
 \left|N(T)-\frac{T}{2\pi}\log\frac{T}{2\pi e}\right|
 \le0.1038\log T+0.2573\log\log T+9.3675.
\]

Here \(N(T)\) counts nontrivial zeros with \(0<\Im\rho\le T\), with
multiplicity (as also follows from their argument-principle definition in
Section 2). The corollary has no \(7/8\) added to its displayed main term.
It immediately gives \(N(T)=O(T\log T)\). A sum over both signs of ordinates
requires the factor two used in the linear-tail certificate. Endpoint
conventions must agree with the certificate's Stieltjes integration.

## Short intervals and the theta/psi distinction

Bahman Saffari and R. C. Vaughan, *On the fractional parts of \(x/n\) and
related sequences. II*, **Annales de l'Institut Fourier 27** (1977), no. 2,
1–30.
[Publisher record](https://aif.centre-mersenne.org/articles/10.5802/aif.649/),
[DOI](https://doi.org/10.5802/aif.649),
[publisher PDF](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf).

Section 6, Lemmas 5–6, uses the prime-only function \(\vartheta\) in its
statements. Its density hypothesis (6.2) is

\[
 N(\sigma,T)\ll T^{C(1-\sigma)}(\log T)^B,\qquad C\ge2,
\]

and (6.19), printed page 24, gives the additive mean square

\[
 \int_U^{2U}|\vartheta(u+h)-\vartheta(u)-h|^2du
 \ll Uh^2\exp[-c(\log U/\log\log U)^{1/3}]
\]

for \(U\ge3\), \(U^{1-2/C+\varepsilon}<h\le U\).
The proof establishes the relative **psi** estimate first, in (6.12)–(6.18)
and the paragraph immediately before Section 6.2. Applying its additive
averaging identity (6.21) to psi gives the version needed here. Page 28 invokes
Huxley's unconditional \(C=12/5\). The existing
[arithmetic note](../../investigations/sonin-critical-boundary/notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md)
spells out this transfer and the complete support-band covering.
At \(h=X^{3/4}\) the range is ample, but the saving is subpower. A brief
manuscript statement should cite the **proof**, not claim Lemma 6 itself is a
psi lemma. RH alternatives (6.4), (6.20) are separate conditional estimates.

## Classical zeta inputs already cited by the parent paper

Terence Tao, *254A, Notes 2: Complex-analytic multiplicative number theory*,
9 December 2014, [author's lecture notes](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
Proposition 16 gives a local zero count with multiplicity;
Proposition 19 gives the local logarithmic-derivative expansion;
Corollary 20 and the proof of Theorem 21 furnish admissible contour heights.
Exercise 22 gives a smoothed but truncated explicit formula. It is useful
background for the contour method, not a statement of the new manuscript's
complete formula including every trivial zero.

Noam D. Elkies, *Math 259: Introduction to Analytic Number Theory*,
notes on the Riemann zeta function,
[author's lecture notes](https://people.math.harvard.edu/~elkies/M259.02/zeta2.pdf).
Printed pages 2–3 prove the Riemann–von Mangoldt estimate

\[
 N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T),
\]

and equation (6) gives a local logarithmic-derivative expansion on
\(-1\le\Re s\le2\). These are direct, accessible sources for the standard
contour bounds. The new paper can cite the exact HSW count instead if it
wishes to minimize its bibliography.

The parent also cites the NIST *Digital Library of Mathematical Functions*,
[Section 25.4](https://dlmf.nist.gov/25.4) for the functional equation and
[equation 27.4.12](https://dlmf.nist.gov/27.4.E12) for the logarithmic-derivative
Dirichlet series. Those references need no operator material from the parent.

For self-containment the new manuscript should write its Mellin/Laplace
integrand and residues explicitly, justify contour shifts from the sixth-power
decay and local logarithmic-derivative bounds, and account for the left contour
using \(y>a\). Merely citing Exercise 22 would leave the complete linear formula
and the \(C^4\) regularity extension insufficiently justified. If using smooth
approximation, uniform control of the sixth derivative as a finite measure
supplies the domination needed to pass to the fixed polynomial probe.

## Software reference and scope

The [FLINT acb_dirichlet documentation](https://flintlib.org/doc/acb_dirichlet.html)
documents zero isolation and zero counting based on Turing's method; the indexed
official documentation remains accessible although a direct page fetch returned
403. The current documentation version is not evidence of the historical
certificate's runtime version. Preserve the version and exact input hashes
reported by the existing certificate package. A rational replay establishes its
transfer arithmetic, not an independent recomputation of the original outward
zero enclosures.

No correction to the continuation note's cited constants or claimed scopes
was found. The published Johnston–Yang bibliography should replace a preprint-only
entry, and the theta/psi and complete-formula qualifications above should remain
visible in the draft.

## Resolution against the written manuscript — 4 October 2026

Reviewed the actual [manuscript](../manuscript.tex), with SHA-256
abaec83e19a7d775fb879ecfb5202c210b7f558d07e379e9e1311004d0560925
at this pass. No manuscript edits were made by this source reviewer.

- **Tao URL and date pass.** The exact /2014/12/09/ URL in the
  bibliography opens the intended primary page; its header says
  9 December 2014. There is no date or URL correction to make.
  Propositions 16 and 19 are correctly cited for the local count and
  logarithmic derivative; the manuscript now derives its complete
  formula by an explicit contour shift, including all residues and the
  far-left integral. This resolves the earlier self-containment caution.
- **HSW count passes.** The appendix reproduces Corollary 1.2 exactly,
  including its \(T\ge e\) range and all three constants. The subsequent
  majorant \(N(T)\le T\log T\) for \(T\ge100\) follows from the stated
  elementary comparison. The linear tail includes both ordinate signs
  and keeps the correct boundary convention.
- **SV range calculation passes.** The relative source range is
  \(U^{\varepsilon-2/C}<\vartheta<1\), \(U\ge4\), for a fixed positive
  margin \(\varepsilon\). At \(C=12/5\), \(\varepsilon=1/12\), this is
  \(U^{-3/4}<\vartheta<1\), as asserted in the manuscript. The full
  integration band has lower endpoint comparable to \(X^{-1/4}\) and is
  eventually admissible at both \(U\) and \(2U\). For added precision,
  replace “uniformly in the range used below” after the relative estimate
  by “uniformly for \(U\ge4\) and
  \(U^{\varepsilon-5/6}<\vartheta<1\), for each fixed
  \(\varepsilon>0\); below take \(\varepsilon=1/12\).”
  This is an expository strengthening, not a correction of the calculation.
- **Bibliography and links pass.** The JY, PT, HSW, and SV entries match
  the primary records; the DLMF sections cited contain the stated
  continuation, functional-equation, and zero-location inputs. Every
  citation key has a bibliography entry, every entry is cited, and both
  local certificate README links resolve from the manuscript directory.
  Optional precision edits are to give PT's issue number 3 and to use the
  versioned arXiv links 2204.01980v2, 2004.09765v1, and 2107.06506v1
  for the theorem numbers actually checked.

No substantive source-attribution, numerical-constant, or theorem-scope
defect was found in this written draft. This pass checked citations and
their use; it does not replace the separate full proof review or numerical
certificate replay.
