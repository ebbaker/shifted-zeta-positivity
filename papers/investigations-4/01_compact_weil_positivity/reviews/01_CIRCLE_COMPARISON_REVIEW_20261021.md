# Circle comparison: mathematical and computational review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **ultra**.

**Disposition: scoped analytic pass after the corrections below; internal
same-model review only.** The [note][note] states its results as proved
in-note. This is not external specialist review or formal verification.
The primary assistant integrated separate agent audits; the Weil/CCM agent
also contributed the diagonal-repair proof, so its review of that argument
is a contributing-author check. A separate transport agent checked the
image comparison and diagonal-repair argument. No novelty claim was assessed.

## Mathematical checks and corrections

The complete-form normalization agrees with the authoritative manuscript’s
label eq:weil. An unverified rendered equation number was removed. The
review checked the antilinear-first inner product, pole factors, zero-extension
map, logarithmic form domain, and the fact that hyperbolic cell weights are
bounded functionals but not smooth periodic sections.

The archimedean image sign and factor two follow from periodized
autocorrelation. The image series and both exponential bounds are correct
for complex tests. The cutoff contract excludes every wrapped prime
correlation, including its equality endpoint; no arithmetic tail is omitted.
The kernel is pointwise positive but has negative odd quadratic values.

The odd sine witness, gamma bound and finite-moment obstruction check out.
The negative-index statement now explicitly requires a common domain on
the finite Fourier block and defines positive rank through the positive
spectral subspace. Its fixed-cutoff scope is retained. The positive jump
completion has the exact nonvanishing diagonal/pole defect; pole-null tests
still pay the diagonal defect.

**Material wording correction:** diagonal-symbol clipping alone does not
make the full form positive. It leaves the negative sinh pole moment on
the odd witness. Section 6 now quantifies over successful nonnegative
Fourier-diagonal repairs, and does not claim that clipping supplies one.
The rank-one exception argument, shrinking frequency band, Fourier
normalization and elementary binomial/Chebyshev lower bound were checked.
The conclusion is restricted to X tending to infinity with log X=o(P).
The final decision explicitly retains each exclusion’s cutoff hypotheses.

## Computational evidence and its limits

The [checker][checker] and [receipt][receipt] record exact rational/integer
checks and independent floating comparisons of the real-line gamma form,
Fourier sum and image series. These support factor/sign debugging. The
analytic proof does not depend on the floating signs or tolerances.
The full receipt records Python/NumPy versions, parameters and script hash;
there are no large generated arrays or external data dependencies.
A separate code audit found that optimized Python could bypass assertions;
the checker now rejects optimized execution and records the optimization
state. The normal run was repeated after that fix and the rejection was
checked without producing a receipt.

The compact even and odd profiles are H^1 controls, not theta sources.
The global odd witness is a circle test, not a fixed localized test.
The computations are not interval certificates and do not prove a new
finite-horizon positivity result. Arithmetic collision families are screened
by their distinct failed canonical-source premises; no theta acquisition,
new collision data or paid source floor is asserted.

## Decision

I4-W01 is complete for the stated bounded candidate analysis, with a failed
positivity/comparison gate. Equations (10)–(12) remain useful approximation
identities. I4-W02 remains gated. Actual CCM and other non-diagonal maps or
cutoff schedules are outside these exclusions. Follow the [result index][results]
and [avoid index][avoid], especially [full-target identification][full] and
[scoped conclusions][scope].

[note]: ../notes/01_CIRCLE_COMPARISON_AND_POSITIVE_COMPLETION_OBSTRUCTIONS_20261021.md
[checker]: ../numerics/check_circle_comparison.py
[receipt]: ../numerics/CIRCLE_COMPARISON_CHECK_20261021.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[full]: ../../../../avoid/13_a_factor_is_not_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
