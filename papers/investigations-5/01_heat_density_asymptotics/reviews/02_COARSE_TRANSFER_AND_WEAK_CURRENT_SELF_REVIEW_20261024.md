# Coarse transfer and weak current: same-assistant assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Scope:** Notes 08–09 and the round-two code/record. This is the same
assistant's audit, not an independent, cross-model or specialist review.

## Analytic audit

1. The complete-source probability measure is used only for moment
   evaluation. M is restored through eta=epsilon/M. Epsilon=1e-4 stays
   fixed in original units, and neither density nor zero counts are
   divided by total mass. The plane's total mass remains infinite.
2. The centered Taylor expansion retains the variance term in an analytic
   factor A=1-vz^2/2. The third absolute exponential moment controls its
   remainder on the complex rectangle. The division by A requires the
   explicit positive a_*; a moment bound alone without that gate would
   not justify the comparison.
3. The sine lower bound holds on the carrier circles and their whole
   complement, using nearest real carrier nodes. X=N pi/mu places the
   vertical walls between nodes; r<min(Y,pi/(2mu)) makes the circles
   disjoint and contained. Rouche gives exactly one zero with multiplicity
   per disk. Reality follows from conjugation and uniqueness. These are
   finite-domain conclusions, not global simplicity or RH statements.
4. The minimum-modulus step is applied to f/(z-a), whose sole zero has
   already been removed. Its boundary denominator is <=2r, hence the
   correct lower constant is b/(2r). Enlarging each disk to radius 2r
   around a only increases the logarithmic integral. The complement's
   area bound can overcount disk area harmlessly. No actual a is computed.
5. The compact kernel is C3, its first three boundary derivatives vanish,
   and its fourth derivative is integrable. This justifies all four
   Fourier integrations by parts and the p^3/720 lattice bound. The
   kernel-derivative constants and zero-extended Lipschitz comparison
   retain roots that can cross the edge of the kernel's support.
6. Contour orientation is positive. H_zz/H has residue H_zz(a)/H_z(a),
   the zero velocity for H_t=-H_zz. P' differentiates the integration
   coordinate, producing the correct sign in the weak time derivative.
   The interpretation of the polynomial contour weights as real spatial
   kernel weights uses the previously stated real-zero premise; it is
   not valid for arbitrary off-axis zeros.
7. The model current is tested against a different observable, not just
   against its own continuity identity. The source moments give mu'
   exactly in the analytic setting. No finite-epsilon current error is
   obtained by differentiating an undifferentiated density-bias bound.
8. The potential/covariance ansatz in Note 09 keeps the transverse variance
   from Note 05 and the additional temporal variance. Its kinematic Q
   satisfies its defining equation by construction. It is not a measured
   theta covariance, and has not been promoted to an accurate closure.
   Its harmonic/additive data and the derivative errors remain material.

## Numerical audit

The initial 96-to-160 contour refinement failed the mass-change target
at several points: the largest change was 1.775e-7 versus 1e-8 allowed.
The record retains this failure. The 160-to-224 comparison changed mass
by at most 1.436e-11, current by 1.303e-14 and time derivative by 1.447e-15.
These meet the contract's diagnostic tolerances.

Changing source order 32 to 48, cutoff 3 to 3.25 and theta terms 8 to 12
changed mass by <=2.78e-16 and the other two observables by <=2.0e-17.
Moving the refined contour height from .75 to 1 changed mass by
<=1.53e-14 and the derivative/current by <=2.12e-16. These comparisons
test implementation stability; they are not independent evaluation or
tail enclosures. The exploratory whole-interval source quadrature used
before the contract was not used for the reported values.

Separate time differences at steps .5/.25, Richardson extrapolated,
agree with the contour time derivative within 2.01e-15. The weighted
cosine contour control has mass error <3.77e-12 and current <1.75e-17.
Outer contour counts differ from 12 by <5.2e-11. The final imaginary
remainders in the real observables are <9.2e-17. Refining the temporal
quadrature from 12 to 20 nodes changes mass by <6.2e-16 and current/time
derivative by <1.1e-17. The source gates pass numerically at all 20 nodes,
without certifying intervening times or full contour boundary floors.

The largest observed density, nonzero-current and time-derivative
relative errors, including the time average, are approximately 0.02984%,
0.08560% and 0.35888%. All pass the exploratory 1%/10% usefulness targets.
The model's finite cosine-lattice comparator is still closer in mass.
Transverse samples multiply the same coefficients and must not be
counted as independent tests. Exact identities, counts, precision and
refinement totals are not proofs of source accuracy.

**A minute regulator-bias formula does not bound source or total error.**
The log10 values -328.85, -649.45 and -1028.87 are floating substitutions
into a proved conditional expression. They do not certify errors at
those scales. Complete-source moment enclosures, quadrature error and
roundoff remain unpaid; zero floating differences do not pay them.
The code stores log bounds so underflow cannot become a false exact zero.

The script hash, versions, parameters and per-case checks are stored in
the small JSON record. No large arrays or PDFs are added. No source
manuscript or earlier chat archive is edited.

## Controls, status and next work

The positive atomic heat control has a double event at t=1/4 and
a_*=-177.434... on this contract, so the proposed concentration gate
correctly fails there. It does not fail positivity itself. The existing
Euler-factor, weighted-square, reflected and positive-primitive families
are screened at the premise level in Note 09, not numerically replayed.
Each can satisfy generic identities away from an event, and source
arithmetic alone is not claimed to distinguish these finite estimates.

Assessment: record a completed **bounded research round**, while retaining
HDA-02, HDA-04 and HDA-06 as partial. The new evidence is a conditional
coarse-transfer/regulator estimate and finite floating weak-transport
accuracy. A certified slab, actual differentiated covariance, negative-time
remainder constants, compatible boundary traces and a stability theorem
remain open. HDA-07–09 are still gated. No approximate evolution has
been independently solved and compared over a trajectory.

- [Contract](../notes/08_SECOND_BOUNDED_COARSE_AVERAGING_CONTRACT_20261024.md)
- [Derivation and results](../notes/09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md)
- [Execution record](../numerics/COARSE_THETA_ROUND2_20261024.json)
- [Progress ledger](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
