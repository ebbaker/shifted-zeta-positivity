# TND-A-E05: analytical manuscript and production review

6 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, verified in local turn metadata. Existing auxiliary chat0003,
thread `01a1af80-4c0e-76c3-b030-c92591d2edba`. Root authored and checked
the manuscript; no supporting agents were used. **E — fixed analytical
synthesis**, Sol recommended; the author requested it in this Astra chat.

**Disposition: complete at analytical synthesis and local production
scope.** This manuscript consolidates the internally assessed conditional
response; it does not establish a new collision estimate. This review is
an editorial, mathematical-consistency and rendering check, not a new
independent assessment of the original proofs.

## Scope and evidence

The [manuscript](../manuscript/main.tex) uses the
[parent manuscript](../../manuscript/main.tex) as background and develops
one auxiliary chain: cylinder spectrum, Green weight, canonical theta
source, prepared amplitude, heat evolution, calibrated response and
consequences. It ends with the outstanding tasks. The user explicitly
required analytical results to lead and reinforced the repository's
working-PDF rule; no numerical experiment enters the proof or was run.

[Branch E01](../notes/01_TND_A_E01_R1_COMPLETE_SPECTRUM_RESPONSE_20261106.md)
and [E02](01_TND_A_E02_REALIZATION_ASSESSMENT_20261106.md) retain their
conditional supplied-apparatus scope and internal same-model/proof-author
chat provenance. Shared parent geometry/source inputs retain their
existing assessment. The new writing supplies no specialist or formal
independence. The [E03 request](../research-progress/handoffs/07_TND_A_E03_R1_FROZEN_REQUEST_20261106.md)
is still issued and unactivated; E04 is pending. The first-jet map is
included as a direct differentiation of the accepted response, while
sharp norm/error bounds are identified as unfinished work.

## Mathematical and expository checks

| Manuscript passage | Check and disposition |
| --- | --- |
| §2, geometry and spectrum | Unit-sphere eigenvalues ±n have 2n multiplicity each; radius 1/2 produces ±2n and the complete squared dispersion k²+4n². Chirality cancels cross terms. Curvature 8 supplies the already included Lichnerowicz term 2; no second shift is added. Both radial directions and signed blocks are retained. |
| §2, realizations/core | Maximal multiplier domains carry weights omega and omega^(2p). The adjoint test uses compact spectral supports; complete shells commute with the signed block. Cutoffs and mollification yield the integer-power cores. Monotone dispersions on radial half-lines and null threshold preimages justify absolute continuity. No plane-wave or threshold L² eigenstate is asserted. |
| §2.3–§3.1, Green/source | The kernel derivative jump is −1, and the full dk/(2π) resolvent integral gives 1/(4n), not the zero-momentum value. Multiplicity 4n cancels exactly. Differentiating the scan twice and subtracting p yields 8 times the stated source. Complete theta inversion gives p(u)−p(−u)=−sinh(u), hence a smooth even processed source. The scan/imprint remain supplied. |
| §3.2, estimates | The polynomial recurrence, degree j+2, coefficient-sum bound and Gaussian source tail keep the sum of absolute values. The radial substitution gives the prefactor 2/4^(r+1), log-square coefficient M/16 and x^(d−1). The finite Leibniz constant, weighted L¹ estimate, L²/Schwartz bounds and Fourier integration-by-parts tail are consistent. Reflected finite prefixes are used only for values/moments, not as smooth graph cores. |
| §3.3, normalization | Full-line evenness pays the factor 1/2. With s=(1+iz)/2 and t=e^(4v), the transformed integral has prefactor 1/8. In Re s>1, absolute termwise integrals are O(m^(−Re s)); the gamma combination equals s(s−1)Gamma(s/2)/2, giving xi(s)/8 after the prefactor. Entire continuation then gives the full identity. The derivative insertion v² and (−iv)² give the negative Newman heat sign. |
| §4, amplification and graph identity | R has trace one, B=R^(1/2)J has HS norm one, and each shell contributes exp(−πn²)/Q. Expanding (k²+4n²)^(2p) yields binomial(2p,j)4^(2p−j)mu_(2p−j) times the squared (h+j)th radial derivative norm. No right energy or extra physical multiplicity appears. |
| §5, evolution | The semigroup norm is exp(−4τ), and its strong uniqueness follows from L≥4I. Prepared graph norms control actual zero-time derivatives, not arbitrary-data smoothing. The radial Gaussian variance is 2τ; exponential tilting shifts the mean by ±2bT and gives exp(b²T). The weighted convolution and finite heat-derivative sums are consistent. Translation continuity plus compact parameter families proves weighted limits; integration down to zero converts limits into actual derivatives. |
| §6, calibration/response | HS products are trace class; the Bochner Fourier readout is justified on the weighted prepared family. The metric factors 2×2 cancel 1/4. The known complex gain includes phase. There is one left angular heat factor, giving π+4τ. The Fourier and readout constants cancel exactly. The complete trace produces q, and entire continuation follows from the weighted bounds. |
| §6.3, derivatives | The integral derivative prefactor is 1/2. The weighted majorant uses r=d. Angular q derivatives have bound 4^s mu_s, while HS field derivatives use square roots of mu_(2s); these distinct moments are kept separate. The finite U recursion, product-rule indices and exp(Tb²) complex-window bound agree with the exact response. No uniform-in-order or negative-time assertion is made. |
| §7, consequences | The factor is nowhere zero, so multiplicities and collisions are preserved. Squaring ∂z+2τz retains the 2τ term. Proper time and Newman time obey different equations. Real inverse amplification is unbounded at nonzero τ, with a finite scalar bound on each compact window. The triangular first-jet map and transformed error-set identities do not constitute the pending sharp theorem. |
| §7.4–§8, scope/tasks | All four control families retain their precise failed canonical/domain premises. Positivity of the source, bank and Hamiltonian is not identified with a sign of the oscillatory amplitude. Outstanding tasks separate E03/E04, source-specific estimates, intrinsic apparatus work and independent review. |

The detailed inherited six-obligation proof is re-exposed with its domains
and complete limits rather than replaced by the formal multiplier alone.
The Mellin normalization paragraph is a local expository derivation of an
inherited identity. The editorial pass removed an overloaded A from the
first-jet discussion, standardized slash notation, and simplified one
introductory sentence; no inherited mathematical source or request was
corrected or rewritten.

An invertible response factor preserves collisions; it does not exclude
them. This is a limitation of the specified response, not an exclusion of
other physical models or source-specific auxiliary estimates. See the
[result index](../../../../../result-summaries/README.md),
[theta cluster](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[patterns index](../../../../../avoid/README.md), and
[re-realization pattern](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md).

## Production and file checks

- Final pdfLaTeX/BibTeX/latexmk build: **17 pages**, 452,502 bytes.
- Final TeX log: no warnings, overfull/underfull boxes, unresolved
  references/citations or missing-character reports. No duplicate source
  labels or undefined source reference targets were found.
- All 17 pages were rendered at 110 dpi and inspected individually.
  After the final notation/wording edits, all pages were rendered again:
  pages 2, 3 and 15 changed and were inspected again; the other 14 were
  pixel-identical to the already inspected pages. No clipping, overlap,
  missing glyph, broken table, numbering or section-transition defect was
  observed.
- PDF extraction: all 17 pages contain text, author/title metadata match,
  no replacement characters, and no character bounding boxes lie outside
  the page. These structural checks supplement the visual inspection.
- The PDF exists **only** in repository-root ignored `output/pdf/`.
  `git check-ignore -v` resolves it to root `.gitignore:39:/output/`.
  There is no PDF or TeX build product in the manuscript directory.
- All new editable sources and small records are under 1 MiB. No snapshot
  folder, third-party PDF, commit or tag was created.
- [BUILD_RECORD.json](../manuscript/BUILD_RECORD.json) records editable
  input identities separately from the untracked derived reading copy and
  log. The hash identifies this build; portable byte-for-byte output is
  not asserted.

The [input record](../research-progress/handoffs/08_TND_A_E05_MANUSCRIPT_INPUT_VERSIONS_20261106.json)
contained 38 items. The pre-closeout check found 37 byte-identical; the
sole changed item was the progress register modified by E05's recorded
activation. All mathematical premises, parent manuscript files and
pending E03 request/manifest matched. Closeout documentation changes are
recorded separately in the return record.

**Next scientific task remains [E] TND-A-E03 r1 — Sol**, at the
[existing request](../research-progress/handoffs/07_TND_A_E03_R1_FROZEN_REQUEST_20261106.md).
This manuscript return does not activate it or any other successor.
