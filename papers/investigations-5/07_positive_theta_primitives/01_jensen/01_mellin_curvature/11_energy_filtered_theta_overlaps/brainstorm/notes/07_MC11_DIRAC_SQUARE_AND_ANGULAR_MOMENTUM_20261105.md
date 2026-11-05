# Dirac square and angular momentum on the two sphere

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra (Codex), reasoning effort xhigh**. MC11 history0002, thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`.

Routine analytic clarification of the existing model: the author asks whether the squared angular Dirac operator has eigenvalues j(j+1). This does not activate AR-E01 or change the frozen Note06 input, geometry or research target. The distinction is a constant shift and the half-integer range of the total angular momentum label.

In units with hbar=1, let J=L+sigma/2 denote the total angular momentum on spinor spherical harmonics. On a round sphere of radius R, the intrinsic self-adjoint Dirac operator can be represented, up to the conventional unitary identification and overall sign, by
\[
D_R=\frac{\boldsymbol\sigma\cdot\mathbf L+1}{R}.
\]
Using the angular momentum commutators and Pauli identities,
\[
(\boldsymbol\sigma\cdot\mathbf L)^2
=\mathbf L^2-\boldsymbol\sigma\cdot\mathbf L,
\qquad
\mathbf J^2=\mathbf L^2+\boldsymbol\sigma\cdot\mathbf L+\frac34.
\]
Consequently
\[
R^2D_R^2=\mathbf J^2+\frac14,
\]
so its eigenvalues are
\[
\lambda_j(D_R^2)=\frac{j(j+1)+1/4}{R^2}
=\frac{(j+1/2)^2}{R^2},
\qquad j=\frac12,\frac32,\frac52,\ldots.
\]
With n=j+1/2 this is n^2/R^2, n=1,2,3,... . The signed Dirac eigenvalues are ±n/R. Each sign has 2j+1=2n states; the square has 4n states when both signs are retained. Thus the existing n^2 notation and multiplicity are consistent with the angular momentum labeling.

The scalar angular Laplacian has eigenvalues ell(ell+1)/R^2 with integer ell>=0. On spinors, J^2 still has j(j+1), but D_R^2 includes the additional 1/(4R^2). The spinor connection Laplacian and scalar Laplacian are different operators. The Lichnerowicz formula D_R^2=\nabla^*\nabla+Scal/4, with Scal=2/R^2, is consistent: the spinor connection Laplacian has eigenvalues [j(j+1)-1/4]/R^2. The net shift from J^2 is therefore +1/4, not the +1/2 curvature term alone.

The spectrum and per-sign degeneracy were rechecked in [Camporesi and Higuchi, section 3.1 and equation (3.54)](https://arxiv.org/html/gr-qc/9505009), using the self-adjoint convention in [Note06](06_MC11_ANGULAR_WEIGHT_DIRAC_SQUARE_AND_RADIAL_GREEN_20261104.md). The version and reading-copy provenance are already in the [reference catalog](../../references/README.md). The displayed angular momentum algebra is the direct explanatory check; no new spectral theorem or determinant estimate is claimed.

This clarification preserves the distinction between an exact representation and an all-order sign estimate in the [theta results](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [result index](../../../../../../../../result-summaries/README.md), [patterns index](../../../../../../../../avoid/README.md) and [re-realization caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md). The [current register](../../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) and its default next task, [E] MC11-AR-E01 — Sol, remain unchanged.
