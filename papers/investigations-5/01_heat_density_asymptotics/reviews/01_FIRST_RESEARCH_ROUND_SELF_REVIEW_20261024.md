# First research round: same-assistant assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.


**Review scope:** Notes 03–06, the first-round numerical script and record,
and their status in the progress ledger. This was written by the same
assistant that developed the calculations. There has been no independent,
cross-model or specialist review, and no interval certification.

## What was checked

1. **Target and normalization.** The target stays
   \(R=\mathcal F[\epsilon^2|H_z|^2/(\pi(|H|^2+\epsilon^2)^2)]\).
   It is never normalized to total mass or replaced by a squared averaged
   amplitude. Numerical cases measure window averages, not root locations
   or fitted peaks. Centered time averaging is explicitly offline.
2. **Closure derivation.** The covariance Taylor expansion retains the
   nonprojective nature of convolution. The stated C2 remainder uses a
   sufficient C7 assumption and fixed regulator. The isotropic identity
   \(Q_\nabla=4\pi vR(U_{xx}-U_{yy})\) follows from the Poisson identity.
   No time-causal or well-posed evolution theorem is inferred.
3. **Differentiated covariance.** Expanding the Laplacian of the two
   gradient variances gives Note 04 (5). Cross Hessian squares cancel,
   while gradient/density correlations remain. The source-jet density
   identity and a finite-difference current identity were both checked.
4. **Numerical scope.** All 17 source-field samples improve both measured
   defects over omitting Q. An initial filter refinement failed for the
   half-regulator wide window; the final 40-node refinement is recorded.
   Spatial finite-difference steps were also refined. The final records
   meet the declared diagnostic targets. Those targets are not rigorous
   truncation or floating-error enclosures.
5. **Negative-time coefficients.** Re-expanding the source integral through
   T^-2 inside H gives the stated potential through T^-3. Equal spatial
   variances cancel the T^-4 covariance; the independent fourth-moment
   calculation yields Q at T^-5 and its Laplacian at T^-5. The difference
   from the gradient model at this order is spatially constant, so it
   disappears in the density equation. Unequal variances and time-only
   filters are explicitly distinguished. Fixed-epsilon background on a
   zero-free compact set is not interpreted as actual zero-count mass.
6. **Whole-period model.** Differentiating its averaged logarithmic
   potential verifies the density. Continuing a slice by fixed-frequency
   heat flow gives its covariance. The law of total covariance explains
   the additional term after time or transverse smoothing. The distributional
   limits use concentration plus locally dominated bounded remainder
   terms, not pointwise convergence on the real line. No variable-frequency
   cosine is declared an exact heat solution.
7. **Regulator bridge.** Distributional integration by parts transfers two
   derivatives to the compact C2 kernel. Direct radial integration gives
   the simple-zero logarithmic bound; splitting the multiple-zero integral
   at its regulator scale gives the stated finite constant. Theta lower
   bounds and temporal uniformity are visibly missing inputs.

## Control screen

The colliding heat polynomial was checked numerically with a positive
regulator, including a window containing its double event. It correctly
satisfies the generic identities. The cosh control continues to refute
only a variance-only correction forced to vanish when density variance
vanishes. The repository's [Euler-factor, weighted-square, reflected and
primitive-compatible controls][controls] are screened at the premise
level: they alter the unchanged theta coefficients/reflection/arithmetic
inputs used for an actual-source application. They may still satisfy
the generic smoothing identities and any applicable local expansion.
No collision exclusion is claimed, and old certificates were not replayed.
The even-source negative-time expansion specifically needs even endpoint
data, which a non-reflected finite weighted source need not possess.

## Material limitations and next gates

- The broad average shape is still not approximated by a solved theta
  evolution. This round supplies local consistency evidence and exact
  asymptotic/model coefficients, not a uniformly accurate solution.
- The largest gain factors do not measure error in the density itself.
  No residual-to-solution stability estimate or boundary solve exists.
- The local Taylor remainder constants deteriorate as the regulator
  shrinks. Its success in modest windows does not establish accuracy
  across many zeros or oscillations.
- Negative-time numerical remainder constants and growing-domain bounds
  are unpaid. Positive-time theta transfer, source-tail bounds and
  moving-period effects are also unpaid.
- The regulator-bias estimate is conditional on lower-bound data that
  have not been computed for the theta pilot. No actual zero-count
  approximation tolerance has been attained.
- Source quadrature, tail truncation and cancellation remain floating
  diagnostics; there is no independent evaluator. External filtering
  literature was cataloged at its stated partial inspection depth, not
  imported as a theta theorem or a novelty comparison.

**Assessment:** the first bounded round is reproducible and appropriately
scoped as partial research progress. HDA-01 can be marked complete for its
specified contract; HDA-02–06 remain partial. HDA-07–09 must not be marked
complete. The [continuation note][continuation] directs the next bounded
step toward missing quantitative source and coarse-average information.

[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[continuation]: ../notes/07_CONTINUATION_FOR_NEW_CHAT_20261024.md
