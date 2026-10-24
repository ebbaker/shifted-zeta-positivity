# Analytical manuscript integration: same-assistant review

24 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), actual effort max**, verified from
session metadata. This is review by the assistant that wrote the revision;
it is not independent mathematical or specialist review.

**Disposition: the requested analytical manuscript integration is complete
at its stated scope. The full all-time approximation remains open.**
See [Note 21](../notes/21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md),
[the maintained source](../manuscript/main.tex), and
[the build record](../manuscript/BUILD_RECORD_20261024.json).

## Mathematical audit

The proof chain was checked against Notes 14, 16, 19 and 20 and the earlier
fixed-regulator manuscript. The rewritten framework distinguishes the
positive algebraic density from potential curvature, keeps both curvature
correction derivatives, and retains the actual gradient covariance. Fixed
kernels avoid silently importing moving-filter commutators. Constant-
regulator covariance identities are explicitly restricted to that setting.

The score proof retains both half-line endpoint terms and the complete
prefactor derivative bound. Weighted source moments are extended through
order six. The differentiated carrier uses the fourth-cumulant cancellation
and a positive derivative floor, rather than differentiation of a static
error. The wider collar, moving-pole residue, weak current and time-bias
allowances retain the regulator terms and signed source cancellation.

The Bernoulli endpoint coefficients, half-step phase and current sign were
matched to Note 19. The exact continuity formula uses p'=-2p/kappa. The
final theorem pays mean-to-saddle position and drift separately, with full
buffers and a local label count. Its density is positive; no actual-theta
clock potential or covariance is asserted. The generic geometric unfolding
scale is renamed gamma to distinguish it from the source drift alpha.

The growing-block determinant proof now uses the score mean error. Its
mean contribution improves to O(L kappa^-1/3); the unchanged
O(L log(kappa) kappa^-1/6) location contribution still dominates. This
small deduction is recorded in Note 21, and no earlier note is silently
rewritten. The squared-Vandermonde factor and exterior force are retained.

The finite-source proof retains interpolation, theta-mode and source-tail
errors separately. Nonlinear stability uses the same regulator for both
fields and does not divide by H or H_z. The actual density time derivative
is compared through third field jets. For the covariance Laplacian, moving
derivatives onto the filter gives 4 L_1^2+6 L_2; it is not obtained by
differentiating the static covariance allowance. The finite field's heat
residual is exactly zero, but its source error is still paid explicitly.

The smooth switch is a regulator definition, not a certified theorem onset.
Finite-slab approximability is not informative full-transition overlap.
The fixed compact-source failure is restricted to that class and regulator.
The collision-control discussion names the missing canonical source or
simple-root premises and allows generic identities to pass colliding
controls. No RH, earlier simplicity, novelty or autonomous-closure claim
has been added.

## Production checks

- Desktop LaTeX compilation succeeded, and the reproducible export build
  produced a 25-page PDF with no final LaTeX/package or box warnings.
- All 25 pages were rendered and visually inspected. The final notation
  refinement affected page 16 only, which was re-rendered and inspected.
  No clipping, overlapping equations, illegible glyphs or broken tables
  were observed.
- All 26 local PDF link targets exist. The external Bernoulli reference
  points to NIST DLMF 24.8.3. No unresolved citation/reference markers remain.
- The author, title and substantial LLM acknowledgment match the source.
  The PDF stays in the ignored repository output tree; small source and
  build records remain in the investigation.
- Numerical support is three short paragraphs in Appendix C. The recorded
  exact phase checks and floating theta/primitive diagnostics were not
  rerun or upgraded to certificates in this revision.

The build record binds the final source and PDF by hash; those hashes and
successful compilation identify the artifact and do not certify its
mathematics. No new snapshot directory or commit was created.

## Remaining work

The construction proves approximability on each compact slab. Choosing a
finite transition representation with useful complete budgets and endpoint
overlap is still the next bounded research task. Clock covariance,
positive outer heights, certified finite onset and independent review
remain open. The progress register retains those gates.
