# Initial derivation check

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Scope: same-agent check of the [continuation note](../notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md). This is not an independent referee review.

The boundary representative is well-defined because the simple even ground vector has nonzero boundary functional. The inverse derivative maps the odd space onto the even functions with zero endpoint value. It is not treated as an isometry: the induced mass matrix is retained explicitly.

The two mechanical forms are strictly positive under the stated finite assumptions. Weighted self-adjointness gives the generalized eigenvalue equation, and their dimensions agree with the quotient after removal of the inserted ground mode. The auxiliary stiffness identity follows from the odd-even block equation. The energy shift remains visible as an unresolved sign issue for the original Weil form.

The finite characteristic polynomial and the full normalized spectral function are distinguished. The latter includes the untouched Fourier tail. The Gaussian limit follows from the reciprocal-square tail and a vanishing fourth-power remainder, and is compatible with the original staged cutoff limit.

The normal-family criterion has explicit hypotheses: a uniform inverse-square trace bound plus local identification of the limit, or convergence of every inverse moment. The computations do not establish those hypotheses. Full algebra representations and continuum domain questions also remain open.

Numerical validation reconstructs the rank-one matrix and the mechanical pencil separately from the same Weil input. Selected entries are additionally checked through direct correlation integrals. The 120- and 160-digit runs agree on all 21 retained observables for the largest case, and record source hashes match the saved program. These checks are multiprecision evidence, not interval enclosures.

The third finite frequency is not necessarily the third full spectral value: the free tail can intervene. The continuation and numerical README state this distinction explicitly.
