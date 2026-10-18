# Round-one review: effective outer remainders

17 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: **gpt-6-astra (Codex), reasoning effort ultra**, as recorded in this session. Three same-model review agents assisted with analytic, numerical and imported-source checks. This is a cross-model internal LLM review of work attributed to Claude Opus 5.5; the assisting reviewers are not independent model families. It is not specialist human review.

**Disposition: the corrected manuscript's transport identity, explicit remainder and Cauchy derivative bound pass this review on their stated domains. No blocking mathematical error was found in that analytic core. The no-loss conductor/height claims remain numerical, and the 0.18891 conclusion remains conditional on the imported analytic estimates.** The concrete corrections below are narrow; none overturns the transport theorem. This review does not declare a release or an accepted manuscript milestone.

## 1. Material and scope

Reviewed the [working manuscript](../manuscript/height_p_transport.tex), [Note 01](../notes/round-1/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md), [Note 02](../notes/round-1/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md), their [recorded errata](../notes/round-1/README.md#errata-found-while-drafting-the-manuscript), all three [programmes and records](../numerics/round-1/README.md), and the initial proposal. The checkout was clean at the start, at commit `7b4e8579677c8bb65a0fd5f9764c38e7056a1e78`. Source line references below refer to these unchanged files.

The manuscript corrects several errors in the historical notes. I treated the notes **together with** the round README's explicit errata, rather than presenting already acknowledged repairs as new findings. The source and PDF hashes agree with [BUILD_RECORD.json](../manuscript/BUILD_RECORD.json). This was a mathematical/source review, not a fresh PDF layout audit or a fresh typesetting build.

The review follows the [result-summary index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [outer-budget summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [control inventory 12](../../../../result-summaries/12_collision_controls_and_screening.md), and the specific cautions about [status](../../../../avoid/06_status_stronger_than_the_evidence.md), [normalization](../../../../avoid/08_normalization_and_constant_slips.md), [imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md), and [sibling results](../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## 2. Corrections and limits that matter

### 2.1 Qualify the real saddle's uniqueness

**Minor mathematical wording correction.** Manuscript lines 403–404 call \(\sigma^{(0)}\) the “unique real solution” of

\[
\sigma=\sigma_0+\tau^2\alpha(\sigma).
\]

The proof establishes uniqueness in **\([\sigma_0,\infty)\)**, which is the domain actually used. It does not establish uniqueness among all real solutions, and that unrestricted assertion is false. In the family case, put

\[
f(\sigma)=\sigma-\sigma_0-\tau^2\alpha(\sigma).
\]

For \(t>0\), \(\ell_0>0\), and parity \(\mathfrak a\), one has \(f(\sigma_0)=-\tau^2\ell_0/2<0\), whereas \(f(\sigma)\to+\infty\) as \(\sigma\downarrow-\mathfrak a\), because the digamma term tends to \(-\infty\). Continuity therefore gives another real solution in \((-\mathfrak a,\sigma_0)\), besides the intended one above \(\sigma_0\). Add “in \([\sigma_0,\infty)\)” to the statement. The fixed-point construction and every subsequent estimate already select the correct branch, so the theorem's conclusions survive unchanged.

### 2.2 State the sampled quantifiers accurately in the summaries

**Presentation correction; a real certification boundary.** The abstract (lines 44–48), introduction (143–150), and some sentences in Sections 6.2–6.4 say the floor persists “for every” conductor or height after describing a floating evaluation on a time grid. Section 6's caveats are unusually explicit and should be retained, but a time grid is not the only missing quantifier:

- monotonicity in \(\ell_*\) was sampled at twelve settings and only over a finite range;
- some parameter settings used in the tables were not among those samples;
- numerical integration, interpolation and discarded integration tails are not enclosed;
- the intervals between sampled times and the small-time remainder are not controlled.

Consequently, even **at a fixed grid time**, the current records do not establish a uniform statement for all real \(x\), all larger \(q\), or the whole circle used in the derivative estimate. They provide numerical evidence for that extrapolation. Prefer “the sampled evaluations support the conjectured uniform floor at these thresholds,” with the monotonicity assumption next to the threshold. This is not a newly discovered hidden analytic gap: manuscript lines 829–840, 889–894 and 820–824 already disclose it. The revision makes the headline match those disclosures.

In particular, the next round must not regard Lemma \(A_p\) with zero loss as proved merely because Proposition 4.5 has a proof. That proposition bounds a specific point by exact integrals; the implementation's finite evaluations require their own uniform error analysis.

### 2.3 Refresh the consumer dependency and its source paths

**Research-routing correction.** Manuscript lines 358–360 and 1376–1404, the main README, and both notes still route the family comparison through H12 as the standing next obstacle. The neighboring investigation now contains [Project 01's round-three sine-tail comparison](../../01_dirichlet_newman_families/notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md), explicitly **proved in-note, internal same-model checks only**, which bypasses H12 for its own height-three comparison. H12 itself is still open. This review has not audited that new proof.

Update the dependency map to distinguish the old route from this newer one. Do not infer that the new approximation argument automatically transports Project 03's stronger positive-time arithmetic floor or its derivative input: its approximants preserve an initial floor, and need not preserve the primitive-character Euler-product majorants. A written transfer for the stronger kernel remains necessary before the planning values become conclusions.

The bibliography's Project 01 path at manuscript line 1603 and Note 01's link at line 15 are also stale. The contract now lives in [notes/round-1](../../01_dirichlet_newman_families/notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md). Repair active pointers while preserving the historical notes' identity.

## 3. Analytic checks

### 3.1 Normalization, saddle and contour shift

The factors are consistent: imaginary Gaussian translation in \(z\) has variance \(2t\), so the corresponding real translation in \(s=(1+iz)/2\) has variance \(\tau^2=t/2\). The Hermitian functional equation gives

\[
S(x,p,t)=\frac12\Re\frac{\mathcal G'}{\mathcal G}(w),
\qquad w=\frac{1+p}{2}+\frac{ix}{2}.
\]

It also handles complex characters without assuming that their individual flows are even in \(x\). Conjugation pairing in the zero sum is sufficient. [Dobner’s Theorem 3](https://arxiv.org/html/2005.05142) explicitly permits complex Hermitian kernels in the strip-contraction theorem, so the family use does not silently impose positivity or evenness. The real-zero weight \(1/2\), the conjugate zero's contribution \(-1/h\), and the resulting \(+8Q/(p^2-Q)\) term agree.

For the family, the half-plane contraction has constant at most \(\pi^2/32<1\). The real saddle is a lower bound for the real part of the complex saddle on the intended branch. For zeta, the manuscript's restrictions \(x\ge40\), \(1<p\le x\), and its invariant rectangle pay for both existence and the height bound. Note 01 omitted \(p\le x\); its erroneous general statement is already identified in the errata and repaired in manuscript lines 406–439.

Completing the square after moving the entire-function contour to \(s_*+\mathbb R\) yields the claimed tilted Gaussian representation. Order-one growth makes both vertical end segments and the integration-by-parts boundaries vanish. The saddle is fixed while differentiating the Gaussian convolution; no derivative of the moving saddle has been incorrectly inserted in Lemma 3.3.

### 3.2 Majorants and the complete remainder

I checked the signs of the Euler-product Taylor majorants, the digamma derivative bounds, and the partial-summation tail. The character tail uses cancellation over a complete period to bound an arbitrary consecutive partial sum by \(q/2\); the zeta tail includes its pole term. The Stirling lemma follows from [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13) and the in-paper bound \(0\le\beta'\le1/12\). The proof's coefficient argument supplies that last bound, rather than relying on a plot.

The \(\mathcal Q_*\) substitution is used only where its real-part range permits it. On the far reflected tail the definition switches to the Euler-product bound when the reflected real part exceeds \(\sigma_*\); it does not extrapolate the height proxy outside its proved domain. Reflection retains the factor \(\exp(\ell_*(1-2\sigma)/2)\).

A useful independent check of Proposition 4.5 is its exact algebra. Writing \(a=\tau^2\Delta_1\), \(B=\varphi_\tau(V)\Theta(-V)\), \(R=\int_{-V}^\infty\rho\Theta\varphi_\tau\), and using the paper's complex integrals \(\mathcal N,\mathcal D,\mathcal N_L,\mathcal D_L\), integration by parts gives

\[
\mathcal N-\frac{a c_1}{1-a}\mathcal D
=\frac{B+R-a c_1\mathcal D_L+(1-a)\mathcal N_L}{1-a}.
\]

Taking moduli produces exactly the four terms in the second numerator of \(E\), including the boundary payment \(B_V\), the denominator-tail payment and the factor \(1+\tau^2k_*\) on \(N_L\). The lower bound \(|\mathcal D|\ge d_0\) correctly compares with the **complex** pure tilt \(e^{\tau^2c_1^2/2}\). Thus neither a positive-real-weight assumption nor a missing denominator error is concealed here. The conditions \(d_0>0\) and \(\tau^2k_*<1\) are essential.

### 3.3 Derivative bound

On the corrected disk domain, the contraction selects a holomorphic saddle and

\[
s_*'(w)=\frac1{1-\tau^2\alpha'(s_*)}.
\]

For the holomorphic remainder \(\varepsilon\), Cauchy's estimate gives \(|\varepsilon'(w)|\le\sup_{|w'-w|=r}E(w')/r\). Combining the factor \(1/2\) in \(S\) with \(\partial_pw=1/2\) gives the stated factor \(1/4\), and the main derivative contributes at most \((K_2+a_*)/[4(1-\tau^2a_*)]\). This checks Corollary 5.1 as an analytic statement. Replacing the circle supremum by a leftmost-point evaluation still needs the monotonicity/enclosure work identified above.

## 4. Imported comparison and the conditional table

The source check used [Hakimoglu-Brown, arXiv:2610.12803v1](https://arxiv.org/html/2610.12803v1), including Lemmas 2, 3, 10, Proposition 11 and Theorem 12. The latter permits \(M(0)\le Q_0<B\); the half-plane assumption is not needed after setting \(Q_0=1\). The local imports and their constants match the source. The last partial step lies inside the scalar certificate's full interval. No hypothesis mismatch was found in this application. Lemma 3's global remainder and derivative estimates have **not** been independently recertified here; reproducing the scalar expressions in Proposition 11 does not prove them. Retain the conclusion's conditional status.

For compact first contact, [Polymath's primary text](https://arxiv.org/html/1904.12438v2) supplies positive-time confinement and backward Hermite splitting. There is no missing uniform confinement at time zero in this particular argument: the perturbed barrier starts strictly above the known strip, so the explicit classical strip bound excludes an initial time interval; positive-time confinement then suffices. At contact, strip monotonicity puts the height inside the polynomial certificate's range. The published finite boundary computation is an imported input, not a computation replayed by this review. Its region above \(y=1/5\) must not be described as proving all zeros in the finite box are real.

The strengthened kernel can also be checked directly. If \(A=h^2\), \(r=v^2\le A\) and \(D=d^2\), then

\[
\frac{K_h(d,v)}h\ge\frac2{D+A+3r}\ge\frac2{D+A_2+3r}
\quad(A\le A_2),
\]

since the numerator left after clearing the first inequality is \(4r(A-r)\ge0\). The polynomial condition is precisely the upper bound needed on the combination of \(K_p\) and \(\partial_pK_p\). This independently supports the kernel conversion, without numerical sampling of an unbounded domain.

The finite certificate is meaningful: it checks its compactified polynomial over the full domain using rational Bernstein coefficients and uses a lower Taylor polynomial for the positive exponential in every comparison gate. Directed-rounding scalar bounds, rather than the floating table-construction routine, supply the floors used in the conditional conclusion.

## 5. Numerical replay and certificate audit

The [small replay record](../numerics/REVIEW_REPLAY_CODEX_20261017.json) records commands, environment, source and output hashes, and all differing sections. The three programmes were copied to temporary storage and run with `python3 -I -B` on macOS arm64, Python 3.10.0. All exited successfully. They use only the standard library and local companion code; no external dataset was fetched. All six original programme/record hashes match the numerical README.

| Programme | Result against the stored record |
| --- | --- |
| Height transport | Sections E–H are identical. There are 45 floating-value differences in A–D: one near-zero self-check, three Gaussian-identity residuals, and 41 transport/deviation quantities. Identity residual differences are at most \(8.61\cdot10^{-16}\); C/D relative differences are below \(4\cdot10^{-11}\). All recorded pass/fail outcomes are unchanged. |
| Hakimoglu-Brown comparison | Sections B–E are identical. Two diagnostic values in A differ at rounding level; the actual unscaled table difference changes by about \(4.03\cdot10^{-15}\). |
| Exact/directed strip table | **Byte-for-byte identical**, including both the 34-row classical-strip table and the 24-row published-preprint control. All checks pass. |

The certificate code was also inspected, rather than accepted solely because it replayed. Its compactification is \(D=B U/(1-U)\), \(r=A_2V\), with eight subdivisions and all degree-\((4,4)\) Bernstein coefficients tested. The positive exponential gates use exact rational lower Taylor sums. Decimal operations have consistent outward directions for the supplied parameters, including logarithms, negative exponential arguments, products, the denominator \(1-\varepsilon_0\), the downward floor \(C\), and the upward bound \(G\). The exact scalar record reproduces:

| Check for \(Q_0=1\) | Replayed value (display rounded) |
| --- | ---: |
| Least Bernstein coefficient | \(0.00141545404061\) |
| Least exponential-gate margin | \(1.07944528271\cdot10^{-5}\) |
| Least certified \(C^*-C_i\) | \(2.05110420075\cdot10^{-6}\) |
| Least certified \(G_i-G^*\) | \(2.02217660923\cdot10^{-6}\) |
| Largest \(\varepsilon_0\) | \(0.019088169794\) |
| Final time and height | \(t_n=16891/100000\), \(Q_n=1/25\) |

Thus the arithmetic really yields \(t_n+Q_n/2=18891/100000\) under the stated analytic imports. The word “unconditional” in the historical programme/record filename describes its **starting strip**, not an independently validated unconditional bound for \(\Lambda\).

The floating majorant evaluations are reproducible on this additional platform but are still not interval certificates. No substantive arithmetic implementation error was found in the present exact/directed table. These runs do not reproduce the earlier same-model randomized checks, supply missing interpolation bounds, or verify every external analytic constant.

## 6. What this establishes and what to do next

The change of consumer is justified. The old four-jet budget's positive costs already exceed its sign margin at practical heights; that is an obstruction to that **budget**, not to the true sign or to every possible remainder method. The new result is a quantitative sufficient input with an exact identity and an explicit complete error expression. It is not another RH-equivalent reformulation. Its potential gain is useful, but the quoted factors of 1.7–4.4 compare a floating estimate with the explicit estimate of the imported preprint and remain prospective until certification.

The collision controls do not contradict the theorem. For example, the Euler-factor control with \(c=1/2\) inserts \(1+4\sqrt{\mathfrak p}\,\mathfrak p^{-s}+\mathfrak p^{1-2s}\), so its logarithmic Euler coefficient at \(\mathfrak p\) exceeds the zeta majorant used in Lemma 4.1. The weighted-square, reflected super-Gaussian and primitive-compatible controls do not possess the specified primitive-character Euler product and its coefficient/partial-sum bounds. Their positivity or reflection alone cannot substitute for those arithmetic premises. The generic Gaussian identity can remain true for a control while the arithmetic estimate is inapplicable. This is a premise-level screen against the [documented controls](../../../../result-summaries/12_collision_controls_and_screening.md), not a new collision computation.

Recommended next gate:

1. Correct the saddle uniqueness qualifier and the summary quantifiers; update the current consumer links and dependency map.
2. Certify **one named useful parameter regime** of Proposition 4.5, including interpolation, all integration tails, the unbounded height/conductor range, between-grid times and the small-time remainder. Certify the whole Cauchy circle if the strengthened kernel is the consumer. More floating samples alone do not close these obligations.
3. Keep the zeta table's arithmetic acceptance separate from the remaining independent audit of the imported global analytic estimates. No unconditional 0.18891 bound is endorsed here.
4. Reconcile the family transfer with Project 01's newer comparison before expanding the planning tables. A sharper remainder and a comparison theorem must meet through an explicit common hypothesis set.

## 7. Version identity

These full SHA-256 values identify the reviewed source; they certify identity, not mathematics. The replay record supplies the numerical programme and record identities.

| Artifact | SHA-256 |
| --- | --- |
| Manuscript TeX | `b9d3b09231d5d21e7337c75d1c84340e2af3946832d6977224657efc7b7f661a` |
| Retained manuscript PDF | `a9ef9251a9b7e418cf63d062e1d432630dd7982d4e1eedc6d70168e3c40c6439` |
| Note 01 | `f591b9e7d03c9d32ac2167fcb90d72b5b2f99dc69faa746fbeb15cbba25185a2` |
| Note 02 | `3a95a8d34d8210acb9fd3efdf9ea95fcfef9e652149c2962797b00d8762877d5` |

No manuscript, historical note, programme, original numerical record or synced project source was modified for this review.
