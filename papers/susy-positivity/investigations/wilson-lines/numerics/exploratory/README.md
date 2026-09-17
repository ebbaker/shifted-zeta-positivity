# Exploratory computations

Programmes here are **not registered check programmes**. They use libraries the
repository's conventions exclude (`mpmath` throughout), they are not listed in
the `CHECKS` dictionary of [`validation/drafts.py`](../../validation/drafts.py),
and `drafts.py check --replay` does not run them. They exist so that numbers
quoted in the notes are reproducible.

| Programme | Supports |
|---|---|
| [verify_inner_function.py](verify_inner_function.py) | Propositions 1 and 3 and Section 4 of the [inner-function note](../../notes/INNER_FUNCTION_AND_RESONANCE_20260917.md): unimodularity of the transfer symbol, the Lorentzian line shape at each zero and its mass, and the group-delay identity. |
| [weil_sine_basis.py](weil_sine_basis.py) | The module the rest import. Assembles $Q_{0,L}$ on $L^2(-L/2,L/2)$ in the orthonormal sine basis, every element in closed form from the explicit formula in its real-space (jump-measure) presentation, so that $\lambda_{\min}$ can be taken to arbitrary precision. Its closed forms are what the registered [check programme](../check_sampling_forms.py) verifies. |
| [frame_bound_scan.py](frame_bound_scan.py) | The converged table of $\lambda_{\min}(Q_{0,L})$, Section 6 of the [frame-bound note](../../notes/FRAME_BOUND_AND_THE_DENSITY_20260917.md), and the calibration of Section 1.2. |
| [bandwidth_profile.py](bandwidth_profile.py) | Section 4.1: the universal profile of $\log\lambda^{(W)}/\log\lambda_{\min}$ in $W/\tau_c$. |
| [deficit_construction.py](deficit_construction.py) | Section 4.2: the literal deficit construction --- band plus exact vanishing at the sub-critical zeros --- and its failure. Uses published zero ordinates to define the constraint subspace only; any subspace gives a valid upper bound. |
| [comb_homotopy.py](comb_homotopy.py) | Section 5.1: $\lambda_{\min}$ with the prime comb deleted (indefinite for $L\gtrsim0.85$) and along the coupling homotopy $Q_s$. |
| [gram_point_cache.py](gram_point_cache.py) | Gram points $\theta(g_n)=n\pi$ to a requested height and precision, two-stage: `mp.grampoint` at 30 digits, then Newton with the analytic $\theta'$. Run before the two controls. |
| [density_control_gram.py](density_control_gram.py) | Section 5.2: $\lambda_{\min}$ for the Gram points, an arithmetic-free set with the same counting function. |
| [density_control_jitter.py](density_control_jitter.py) | Section 5.2: the same with jitter applied in the unfolded variable $\theta/\pi$, so the counting function is preserved. |
| [decay_laws.py](decay_laws.py) | Section 6: the one-parameter model comparison and the two published laws. |
| [crosscheck_against_repo_assembler.py](crosscheck_against_repo_assembler.py) | Section 1.2: $Q[f]$ from the closed-form matrix against `weil_functional` of the finite-response investigation's `chk1_explicit_formula.py`, a pre-existing and independently written quadrature assembler in Suzuki's normalisation. Relative agreement $6\times10^{-25}$ at 25 digits. Also requires `sympy`. |

Every number these produce is a trial-space Rayleigh quotient, hence an **upper**
bound on the corresponding infimum; the notes state which direction each value
certifies. Basis size must reach about $2.8$ times the Nyquist count $2Le^{L}$ or
the value saturates --- see Section 4.1 of the note, which measures this.

Anything that earns a place in the manuscript should be ported to a registered
programme under the investigation's conventions --- standard library only, JSON
to standard output, a preserved record under [`../records/`](../records) ---
using hard-coded published zero ordinates where $\xi$ itself would otherwise be
needed, as `check_sampling_forms.py` now does.

See the [checks index](../README.md).
