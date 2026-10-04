# Review of the global growth continuation and manuscript additions

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
were not exposed and are not inferred. Parent review and separate agent
cross-checks use the same model family and are not independent specialist
refereeing. Repository baseline: `5052fc961dc755718f2cf88516e78096eb9e8edf`.

## Mathematical assessment

The continuation establishes useful bounds but leaves the proposed global
subexponential estimate open. The manuscript statements and proof notes
distinguish the following conclusions.

- **One-sided criterion:** the positive-tail Laplace transform has no real
  singularity above the assumed growth exponent. Landau's boundary lemma
  therefore forces convergence there. This uses real-axis regularity of
  the meromorphic arithmetic transform, not an assumed zero-free half-plane.
- **Both-sign obstruction:** the eventual one-sided envelope supplies the
  needed half-plane of convergence before the boundary residue is used.
  Hence the quantitative lower bound on each signed excursion does not
  require a rightmost off-critical zero or a spectral gap.
- **Prime powers:** the square main term vanishes by Phi(0)=0, leaving o(1)
  by PNT. Higher powers are O((1+r)exp(-r/6)) using only a Chebyshev bound.
- **Zero formula:** polarization, conjugation symmetry, and the complete
  explicit formula give C=sum m Phi(rho-1/2)exp((rho-1/2)r), with distinct
  zeros and explicit multiplicities. There is no factor two. The identity
  M=-C+epsilon fixes the sign. The sixth distributional derivative includes
  both endpoint atoms; omitting them would invalidate the tail constant.
- **Verified low zeros:** nonnegative coefficients are used only for zeros
  below the published verification height. The identity S_T=q-R_T(0)
  controls their complete mass; unknown high zeros are bounded absolutely.
- **Global asymptotic bound:** twelfth-power transform decay and the zero
  count give the exponent 11 in exponential height blocks. The classical
  zero-free region then yields every c<2sqrt(11/5.558691), but leaves
  exponential rate one-half. This is not a proof of the target criterion.
- **Sharp cutoff obstruction:** the finite energy identity retains the
  signed kernel. PNT gives uniform convergence of the rescaled last-window
  profile and a strictly positive squared-error constant. Sharp prime
  cutoffs fail in the relevant weighted norms even under RH; the note
  gives the correct complete-window finite integral instead.

Two agents cross-checked the complementary derivations, and the parent read
both full proofs and the cutoff proof. Minor wording changes explicitly
allow Laplace abscissa minus infinity, name the meromorphic identity theorem,
and specify distinct-zero indexing. No substantive mathematical error was
found in these checks. This finding is not a priority assessment.

The scope limits are material: the bound 1.48 exceeds q; finite verified
height does not give arbitrarily large verified height; an approximate Gram
lower bound does not give positivity; and scalar certificate replay does
not reverify the published RH computation.

## Source verification

Primary sources were checked for the imported claims:

- Platt--Trudgian, Bull. London Math. Soc. 53 (2021), 792--797,
  [DOI 10.1112/blms.12460](https://doi.org/10.1112/blms.12460),
  [author preprint](https://arxiv.org/abs/2004.09765): RH through 3e12.
- Hasanalizade--Shen--Wong, J. Number Theory 235 (2022), 219--241,
  [DOI 10.1016/j.jnt.2021.06.032](https://doi.org/10.1016/j.jnt.2021.06.032),
  [author preprint](https://arxiv.org/abs/2107.06506), Corollary 1.2:
  inclusive positive-ordinate count, T>=e, constants .1038, .2573, 9.3675.
- Mossinghoff--Trudgian--Yang, Res. Number Theory 10 (2024), article 11,
  [DOI 10.1007/s40993-023-00498-y](https://doi.org/10.1007/s40993-023-00498-y),
  [author preprint](https://arxiv.org/abs/2212.06867), Theorems 1.3 and 1.1:
  classical constant 5.558691 and Vinogradov--Korobov constant 55.241.
- [NIST DLMF 27.12](https://dlmf.nist.gov/27.12): classical PNT input.

No third-party PDFs are saved in the repository. The current manuscript
retains the author field and acknowledgement of LLM assistance.

## Arithmetic validation

The parent reran the final scalar generator at 192 and 256 bits. Both
passed, reconstructing rational polynomial constants and the derivative
measure's endpoint contribution. The saved diagonal hash is
`643456713dbbb3001c03ab4e1b4978fedd34fd7233c9ba1a6a2a2057889bf49a`.
The separate rational-endpoint replay passes all four outward comparisons,
source bindings, invariant values, and cross-precision interval overlap.
The final upper endpoint is strictly below 1.47931505787654.
Runtime for each scalar run was under 0.01 seconds in the recorded
Python 3.10.0 / python-flint 0.9.0 / FLINT 3.6.0 environment.

This is a reproducible scalar certificate and record audit, not an
independent implementation of the published zero verification or a new
prime-sum computation. Source and record hashes are in
`numerics/global_growth_20261003/zero_tail_replay.json`.

## Manuscript validation

The existing manuscript was updated in place and the current editor was
kept open. The desktop built-in compiler returned **success** on the saved
source; no repair was needed and no separate PDF was generated.

Final manuscript SHA-256:
`7a23e9797bd3207e7c6fea3fb7510cac6a208ae28f841be4767963776dd1f2bf`.
The source has 185 unique labels, 207 resolved references, and 22 bibliography
items; all citation keys resolve. No unexpected control characters were
found. All 78 relative Markdown links checked across the installed package
resolve. The installed numerical package replay passes. `git diff --check`
also passes. The 15 installed or updated files are each below 1 MiB; the
largest is the 129,498-byte manuscript source.

README and draft-history entries point to the new outcome, proofs, and
review. There is no new manuscript snapshot, generated data archive, Git
commit, or remote push. The global subexponential bound remains explicitly
open in the abstract, theorem discussion, scope section, and outcome note.
