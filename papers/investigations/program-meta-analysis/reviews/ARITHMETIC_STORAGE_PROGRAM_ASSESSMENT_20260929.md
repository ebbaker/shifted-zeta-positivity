# Arithmetic-storage in the broader positivity program

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. Three parallel same-model readings supported this assessment; they are not independent human refereeing.

This review concerns the current local working tree at HEAD `305806625d1659466f2ba7ff3fed9d496c1a1bc2`, including the uncommitted September 29 arithmetic-storage notes and records. That commit alone does not identify the reviewed state. The meta-analysis folder was read before the arithmetic-storage overview; selected derivations, reviews, code/record provenance, and the primary Sonin papers were then checked. This is a strategic mathematical assessment, not a complete proof audit or a replay of the substantial interval calculations. Existing research files were preserved.

## Assessment

**Arithmetic-storage is moving the broader program forward. The evidence supports continued, focused investigation; it does not yet justify describing the program as a very promising route to proving RH.** Its strongest advance is that a previously proposed comparison can now be stated on the right domains, computed using the actual infinite-dimensional objects, and tested with controlled errors. Its central limitation is that the new machinery has not produced the arithmetic sign estimate that motivated it.

The distinction matters. The [original meta-analysis](PROGRAM_META_ANALYSIS_20260926.md), especially Sections 2, 7, and 10, asked for an exact Sonin comparison and a place-addition rule, rather than more finite Weil certificates. Arithmetic-storage has delivered those preparatory structural milestones. It has not yet delivered an inequality with useful support dependence or a positive approximation converging to the full arithmetic form.

I would therefore increase confidence in this branch as a well-posed research project, while leaving confidence in its eventual RH mechanism substantially unchanged. Within the currently active program, it remains one of the most defensible directions to pursue. That is a comparative research judgment, not an estimated probability of success.

## What has genuinely advanced

| Meta-analysis requirement | Present result | Mathematical significance and limit |
|---|---|---|
| Recover and audit the comparison | The smooth-core identity `Q_L = B_S + R_(S,L)` now has explicit Fourier/Mellin conventions, full contact and poles, every active prime power, the actual Sonin projection, and the inverse compressed metric | Removes real domain and normalization uncertainties. It makes the residual a defined object, but does not control its sign. |
| Explain what adding a place does | Exact signed covariance and complete/partial residual laws, including the changing metric | Provides a concrete object on which an arithmetic inequality could act. The algebra by itself permits either sign. |
| Approximate the actual positive form with all tails retained | Certified prolate resolvent, smooth source norms, actual projected vectors, and an exact Galerkin error identity | Makes a bounded experiment meaningful. The positive approximants converge to `B_S`, not to `Q_L`. |
| Test a proposed method and stop it if it fails | The specified degree-20/24 trial space provably misses most of the relevant trace | Eliminates an ineffective approximation choice while preserving useful tools. It is not a negative Weil direction. |
| Develop a comparison beyond finite support | No signed all-source estimate or arithmetic fixed-test limit yet | This remains the decisive unmet requirement. |

The [canonical audit](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md) is particularly important. Its positive form is independently constructed; it is not defined by taking the square root of the unknown Weil form. The compressed trace-class factorization also avoids an invalid inference from Hilbert–Schmidt regularity to a stronger trace-class statement. The stronger smooth statement is treated separately.

There is a genuine mathematical foundation for investigating this comparison. Connes–Consani establish the archimedean Sonin trace identity and a short-support dominance theorem with additional transform vanishings. Their theorem does not establish dominance for the present length-1 family. CCM establish finite-place stability of Sonin spaces, while explicitly retaining dependence of the inner product on the places. Neither result supplies the missing general arithmetic inequality. See [Connes–Consani, Theorems 1 and 7 and Appendix C](https://arxiv.org/html/2006.13771v1), and [CCM, Theorem 4.6 and Section 4.8](https://arxiv.org/html/2310.18423v2#S4.SS7).

## What the latest numbers do and do not tell us

The [project summary](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/PROJECT_SUMMARY.md) is appropriately cautious. Its latest accomplishment is accurate scalar archimedean smoothing, including the transformed input needed by the Galerkin error identity:

| Quantity | Even source | Odd source |
|---|---:|---:|
| `B_infinity[F]`, approximately | 1.13835 | 1.19636 |
| `h0 = B_infinity[D2 F]`, approximately | 1.97553 | 1.45705 |
| Current outward enclosure for `B2` | [0.68124, 22.89784] | [0.50392, 16.71659] |
| Upper bound on captured `B2` fraction for the selected space | 1.090% | 2.422% |

The four scalar intervals have widths below `10^-5`. The complete finite-place trace remains very broadly enclosed because `h0` does not include the inverse compressed metric. No complete arithmetic residual has yet been evaluated. The negative epsilon scalars do not decide that residual's sign.

The important lesson from the trace-capture failure is that accurate projection onto the correct space does not ensure that the chosen vectors capture the source response. Higher numerical precision cannot repair this fixed trial space. The full trace scale now makes a better trial choice assessable. See the [scalar calculation](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_SCALAR_TRACE_CALCULATION_20260929.md), Section 5, and its [review](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/reviews/SONIN_SCALAR_TRACE_REVIEW_20260929.md).

These two sources are calibration probes, not established weak directions of the constrained Weil form. A successful comparison on them would remain finite-dimensional. For this real even/odd pair, symmetry can eliminate the mixed entry; for broader families, mixed entries or an exact symmetry argument must be controlled. None of this supplies an all-source theorem. The earlier unrestricted weak vectors also cannot simply be relabeled as pole-neutral sources.

## Where the real difficulty now sits

For the complete residual, adding a place at fixed support changes `B_S` and `R_(S,L)` by opposite amounts while leaving `Q_L` fixed. That identity is useful bookkeeping, but cannot create positivity. The partial residual law is more informative for a possible induction: it compares a signed, source-dependent translation covariance against the new prime's full prime-power contribution. Its sign remains unproved.

The [place-addition note](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md), equations (A5), (A9), (A10), and (A14), makes the distinction precise. Its two-dimensional control allows both signs under the generic operator hypotheses. A successful next inequality must therefore use something specific to Sonin geometry and the arithmetic source, beyond positive local factors, commuting convolutions, and a positive compressed metric.

There are also two separate extension problems:

1. Adding places for a fixed source and fixed support.
2. Admitting new sources on larger supports, with new correlations and powers of already included primes.

A favorable theorem for the first does not automatically solve the second. A proposed induction needs a valid starting comparison on its source class, a support-extension rule or a direct treatment at each support, and quantified accumulated losses. The published prime-free starting theorem cannot simply be used as a base at arbitrary support.

The [CCM obstruction update](../notes/CCM_THRESHOLD_OBSTRUCTION_UPDATE_20260928.md) remains a useful warning about the estimate to seek. It excludes a particular absolute endpoint-energy comparison, not all one-sided inequalities. Arithmetic-storage should preserve joint arithmetic cancellations and avoid demanding a uniform positive gap. It also cannot infer that its own alternative succeeds merely because it uses a different topology.

## A bounded next calculation with a mathematical purpose

The immediate task should be to evaluate `B2` accurately enough to discriminate a stated comparison, using the existing two sources first for calibration. The tolerance should follow from the proposed inequality, not from an inherited arbitrary digit target. There are two reasonable approaches.

**Response-adapted approximation.** Construct actual Sonin vectors from the smoothed response and measure captured trace before investing in high precision. Capture of `h0` is an initial quality check; the full Galerkin residual is still required because the inverse metric couples captured and omitted directions. A source-adapted or Krylov construction needs certified infinite tails and a bound on the actual residual, not just a finite matrix that looks stable.

There is a concrete way to combine capture and inverse resolution. With `W` and `[m,M]` as below, choose a finite orthogonal projection `E` on the ambient Hilbert space and certify `epsilon=||W(I-E)||_HS^2`. Use the Sonin trial space spanned by `A^j W(Ran E)` for `0<=j<=k`. A polynomial approximate inverse with residual bound `rho_k` gives a Galerkin missed-trace bound at most `m^(-1)[epsilon+rho_k^2(h0-epsilon)]`. This follows from the orthogonal input columns and the variational error identity; for the prime-2 interval, Chebyshev polynomials give `rho_k<=2(1/sqrt(2))^(k+1)`. This elementary deduction suggests a measurable design criterion, but the required entries and full-tail capture certificate are not yet implemented.

**Positive spectral moments of the compressed metric.** This is an additional elementary possibility suggested by this review, not an implemented result. Write

\[
A=\Pi D_2^*D_2\Pi|_{\mathcal K},\qquad
W=(C_FD_2\Pi)^*,\qquad H=WW^*\ge0.
\]

With `E_A` the spectral resolution of `A`, define the positive finite measure

\[
\nu_F(E)=\operatorname{Tr}(E_A(E)H),\quad
\nu_F(\mathbb R)=h_0,\quad
B_2[F]=\int\lambda^{-1}\,d\nu_F(\lambda).
\]

Its support lies in `[m,M]`, where `m=(1-1/sqrt(2))^2` and `M=(1+1/sqrt(2))^2`. The current mass-only bounds are `h0/M <= B2 <= h0/m`. Certifying the first actual moment `m1=Tr(AH)` would already give the Jensen/secant bounds

\[
\frac{h_0^2}{m_1}\le B_2[F]
\le\frac{(m+M)h_0-m_1}{mM}.
\]

They follow from Cauchy–Schwarz and the chord bound for the convex function `1/lambda`. Further moments permit polynomial lower and upper bounds on the same interval. Positivity here comes from the independently constructed source measure, not from assumed Weil positivity. This may avoid some cancellation in signed-return evaluation, but the moments still require genuine Sonin projection and tail estimates. The first bounds could remain too broad; no numerical advantage is claimed in advance.

Either approach should independently determine the finite-place correction, retain the prime correlation, and cross-check the complete result against the direct Weil form. Merely defining the correction to make that answer agree would provide no mechanism test.

## Structural questions worth pursuing alongside that calculation

**1. A Sonin-specific covariance bound.** Use the actual kernel or compressed double commutator to estimate the signed integral in (A10), keeping its relation to the prime-power correlation. The first meaningful theorem could cover all sources in one enlarged window, or a nontrivial class with a proved extension argument. Such a result would be a stronger advance than extremely accurate values on two fixed sources. Rewriting `R >= -B` is not a new bound.

**2. A comparison with a controlled finite-dimensional defect.** The published archimedean result suggests investigating a bound of the form

\[
Q_L[f]\ge P_{S,L}[f]-\sum_{j=1}^k c_j|\mathcal M_j(f)|^2,
\qquad P_{S,L}\ge0,
\]

where the functionals are fixed Mellin evaluations at points known not to be nontrivial zeta zeros. On their common kernel, the published restricted Weil criterion could remove the defect. Optional zero mean is the simplest existing example. This is a proposed search direction, not a derived semilocal theorem. An arbitrary negative eigenspace is not automatically removable this way; support-dependent or proliferating constraints require a new sufficiency argument. The essential question is whether the actual semilocal correction has this special structure.

For a particularly bounded test, consider `R_(S,L)[f] >= -c_(S,L)|integral f|^2` on pole-neutral sources. The current odd source is already mean-zero, so an accurately negative residual on it would refute this stronger proposal at that window. A positive result on that source would only pass this one test.

**3. Fixed-test arithmetic convergence.** If place-by-place monotonicity is too strong, seek independently positive forms `P_j` with `P_j[f] -> Q[f]` for every fixed admissible compact smooth source, or `Q[f] >= P_j[f]-epsilon_j(f)` with `epsilon_j(f)->0`. The existing Galerkin convergence to `B_S` is only an inner approximation step. Increasing the place set needs a separate convergence theorem and arithmetic identification. A useful preliminary diagnostic is the change induced by inactive places on a fixed source: the bare arithmetic sum is then unchanged, while transport can still change the trace. Even summability of those changes would prove a limit, not identify it with `Q`.

**4. Tests aimed at the proposed theorem.** After the evaluator is working, use constrained low-energy pole-neutral sources and mixed combinations, rather than only the two current probes. Test the first genuinely new place and a power of an old one: crossing `log 3` and subsequently `log 4` separates these obligations. Compute only enough to test the candidate estimate and its error scale. Perturbed prime weights and the generic two-dimensional control can reveal whether the proposed explanation actually uses the correct arithmetic; their failure should be interpreted within the precise tested class.

## Decision criteria and outlook

I would continue with one bounded computational task and one structural lemma pursued together. The calculation should inform or reject the lemma; it should not become a prerequisite for an indefinite sequence of ever larger computations.

| Next milestone | What would improve the assessment |
|---|---|
| Accurate `B2` and complete residual on calibration sources | Establishes that the actual semilocal comparison is computationally accessible; still a diagnostic milestone |
| A rigorous estimate using Sonin geometry, applying beyond a finite source family | First direct evidence that the reformulation makes a formerly inaccessible sign easier to prove |
| A support/place extension with controlled losses, or identified positive fixed-test limit | A substantial advance toward the global program |
| Continued high-precision traces without a stable signed pattern or theorem | Reason to narrow or pause that numerical line |

A negative residual would disprove the strong proposal `R>=0` on that test, not positivity of `Q=B+R`. A rigorously established `R<-B` would instead be a negative Weil direction and could not be dismissed as an approximation-choice failure. This distinction must remain explicit in interpreting tests.

The encouraging feature is the improved quality of the research loop: a precise object, an honest error budget, a falsified approximation choice, and a sharper next question. The limiting feature is that the decisive sign still has no arithmetic explanation. I would describe the current program as **mathematically substantive, increasingly focused, and worth a disciplined next stage; its global RH route remains speculative**. Stronger optimism should follow the first new arithmetic comparison theorem, not the number of certified digits or the volume of internal review.

Before building heavily on that theorem, obtain specialist review of the normalization/domain bridge and the sign-bearing argument. The present calculations and reviews are internally checked machine-assisted work. For this assessment, the numerical reviewer checked the current scalar-summary generator and dependency hashes and the stored rational interval widths; the expensive underlying Arb calculations were not rerun. Primary-source checks confirmed the cited trace, restricted-test, and semilocal-stability scopes. No new numerical certificate, manuscript snapshot, commit, or push accompanies this review.
