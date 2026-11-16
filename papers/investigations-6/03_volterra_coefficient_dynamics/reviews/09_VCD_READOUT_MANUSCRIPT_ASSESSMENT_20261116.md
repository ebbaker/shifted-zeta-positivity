# Analytical readout manuscript: same-assistant assessment

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0004. Actual model and
reasoning effort are unavailable in the recorded configuration.
The drafting assistant performed this check. There was no separate
reviewer, specialist review or independent numerical verification.

**Status: same-assistant analytical and document check completed within
the stated scope.** This assessment covers the 16 November expansion of
[main.tex](../manuscript/main.tex) and its seven included analytical
sections, identified by [build record11](../numerics/11_VCD_READOUT_MANUSCRIPT_BUILD_20261116.json).
It does not upgrade E04/E08/E13/E15/E21/E22/E24 beyond their recorded
source and internal-review statuses.

## Analytical checks

1. **Normalization and variables.** Probability normalization is
   F=2H/Z, with q_n=P_n/sqrt(h_n/Z), q_0=1 and h_n/Z=product beta_j.
   The Jacobi edges are sqrt(beta_j). Heat time, source coordinate,
   polynomial degree and Fourier observation height are distinct.
   Complex propagation is justified on the particular input vector,
   not as a bounded whole-space operator.
2. **Finite readouts and convergence.** The determinant recurrence gives
   the nodes; the eigenvector recurrence gives simple eigenvalues and
   positive first-coordinate weights. Return paths prove exactness
   through degree 2N−1 and the first discrepancy h_N*. Nonnegative
   path products give the compact-complex convergence majorant.
   The Gaussian three-site nonreal-zero example is derived exactly.
3. **Polynomial phase.** The recurrence telescopes to Christoffel–Darboux.
   The coincident-point limit and phase derivative have consistent
   signs for arg(q_{N−1}+i q_N). The positive numerator differentiates
   in the source variable. No Fourier-readout Wronskian sign is imported.
4. **Memory and midpoint.** Cutting one bounded edge preserves
   self-adjointness. Real-time elimination gives minus beta_N and two
   boundary crossings. The midpoint pairing is bilinear, while its
   Hermitian norm is F(i Im z); the finite midpoint construction is
   exactly G_N.
5. **Complete error law.** The simplex dimension is 2N, its coordinate
   volume is 1/(2N)!, and its uniform probability is normalized
   accordingly. Doubled nodes implement first-derivative interpolation.
   The exponential remainder uses a convergent divided-difference
   expansion, not a real mean-value theorem for a complex function.
   Source exponential moments justify all fixed-degree interchanges.
6. **Error moments and phase.** The second/fourth moment formulas follow
   from finite coefficient extraction before averaging the unbounded
   source point. The N=1 factors agree with its beta density.
   The bounded-node reciprocal series is used only inside its radius;
   the unbounded source is handled by its cosh moment. The explicit
   ell_N<N bound keeps every strip denominator positive, including the
   separately stated N=1 case. The Taylor/Cauchy–Schwarz estimate has
   the stated uniform O(|z|² log²(N+1)/N) rate.
7. **Directed geometry and cost.** The unknown amplitude has a positive
   upper bound from the available coefficient head. The closed convex
   enclosure includes zero for the count homotopy. The pointwise
   half-plane test instead uses the strict positivity of the actual
   amplitude. These are different hypotheses. The next-head comparison
   uses the same extra known coefficient as the monomial correction;
   its actual-error ordering is proved only near zero at fixed N.
8. **Local zero motion and counts.** The local lemma explicitly assumes
   a positive disk radius, nonnegative error/curvature constants and
   a strict boundary inequality. Taylor plus Rouché gives one zero,
   conjugation gives reality, and the multiplicity count gives
   simplicity. The displacement denominator is strictly positive.
   The velocity formula follows from the simple-root identity.
   Other regions and complex pairs are not accounted for by this lemma.
9. **Source characterization and controls.** Products q_n q_{n−1}
   span the odd polynomials. The all-degree Stein identities extend
   to Fourier tests under the stated weighted exponential hypothesis,
   then to nu'=-V'nu as distributions. Normalization identifies theta.
   This is all-degree source rigidity, not finite predictive closure.
   The [integration note's control table](../notes/25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md)
   separates failed premises from untested inequalities and preserves
   E10's absence of a zero-location result.

No mathematical correction to the inherited E21/E22/E24 results was
identified in this check. The added local lemma and polynomial phase
derivation were checked directly above; this is not independent validation.
The qualitative global zero-strip objective remains explicitly classified
as an RH-equivalent reformulation, rather than a numerical milestone.

## Document and reference checks

- Built with latexmk/pdfLaTeX; the final log has no warnings, unresolved
  references, undefined commands, or overfull/underfull boxes.
- All 22 pages were rendered and visually inspected. After the final
  wording and normalization-background changes, the ten changed pages
  were re-inspected; the other rendered pages were byte-identical.
  Equations, theorem numbering, table of contents, margins and bibliography
  are readable, without clipping or overlap.
- Corrected an undefined script-font command during authoring and moved
  the long simplex vector to a display. The compact-convergence proof
  was simplified to use the already established nonnegative path products.
- Re-inspected de Boor's simplex formula and Topping's argument principle
  and Rouché statements. The manuscript preserves the checked Teschl
  spectral-variable scope and Romanov §3.2 analogy. It claims no faithful
  canonical-system representation of G_N.
- Numerical quantities are not premises in the proofs. Existing collision
  certificates appear only as supporting evidence for the scope discussion;
  none was rerun.
- The finished PDF is in the ignored root output folder. All intermediates
  and page images are outside the repository. Editable sources and small
  records are retained; no new manuscript snapshot folder was made.

## Remaining mathematical work

The complete signed error has a proved phase allowance. A canonical
readout separation estimate, useful lower slope or controlled companion
phase remains unproved. No successful exhaustive contour family, complete
finite-model zero count or degree-propagated zero confinement is supplied.
The local perturbation lemma does not impose global simplicity on the
research program. B07 remains ready but unactivated; E25 remains unissued.
