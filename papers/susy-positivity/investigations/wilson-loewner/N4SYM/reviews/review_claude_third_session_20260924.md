# Same-assistant audit of the third N4SYM session (24 September 2026)

**Model:** Claude Fable 5.1 (Anthropic), session configuration `claude-fable-5-1`; the serving model can differ and no model identifier was exposed by the runtime. Reasoning effort not exposed.  
**Kind:** an internal audit, with two separate adversarial referee contexts of the same model. This is **not** an independent specialist review.  
**Scope:** [finite-mass memory and quartic response](../notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md); [`check_finite_mass_response.py`](../numerics/check_finite_mass_response.py); [`check_quartic_input.py`](../numerics/check_quartic_input.py); the draft [manuscript](../manuscript.tex).

## First referee pass (finite-mass endpoint dynamics)

The referee re-derived twelve items with its own sympy/mpmath code, without access to the author's program.

**Confirmed:** m = √λ/(2πz_m); the quadratic action, bulk equation and the sign of the boundary condition (a positive force makes the string trail); the retarded branch and the exclusion of the horizon-emerging branch; F = mŸ, X = Y + z_mẎ, mẌ = F + z_mḞ exactly; the nonrelativistic limits of the transcribed CGG equations (28) and (35); the causal exponential kernel, the pole at −i/z_m and the expansion of χ_m; the energy identity and the string-energy identity, verified to 30 digits on a Gaussian; the flux at the endpoint equal to FẊ; the light-cone support of the retarded Δ = 4 propagator with the identity Im(s + iε)⁻⁴ = (π/6)δ‴(s).

**Corrections and qualifications, applied in the note:**
1. The remainder in the point limit is O(√λ z_m) = O(z_m) at fixed λ, not O(z_m²).
2. "One simple pole" applies to X → F and X → Ÿ; F → Ÿ has no pole and F → X has a double pole at the origin.
3. Rationality needs T = 0, the strict planar limit (rigid flavour brane, O(1/N) back-reaction), strict λ → ∞ and linear order; a black-brane background gives a quasinormal tower.
4. Assumptions to state: string initially static (Ẏ(−∞) = 0); the horizon boundary term vanishes by retardation, not by the variational principle; integer Δ for the sharp support.

## Second referee pass (boundary field and quartic structure)

**Confirmed:** the retarded propagator's sign and constants, additionally by matching its Laplace transform to the Euclidean Fourier transform to 13 digits; the linear-response formula and the static dipole check (ratio 4); g₄; the antiderivative G(z) by symbolic differentiation and the closed form P₄, against direct quadrature to 12 digits; the vanishing of G at depth; the static closed form; the memory statement that N is not divisible by (1 − iωz); the operator content of the quartic tilt response; the vanishing of the GFF cubic response; the scale-free statement; both crossing matrices (brute-force index sums, R² = 1); the GFF OPE coefficients and the block decomposition; the validity of the transcribed Δ = 1 functions under both crossings; the small-χ structure of G_S^{(1)} with b = −43/30.

**Corrections and additions, applied in the note:**
1. Sign in the massless limit: Y(t − r) + rẎ(t − r), not Y − rẎ; this equals x(t, z = r).
2. The quartic tilt response needs ⟨Φ₆⟩ in a cutoff scheme to be finite at tree level; at weak coupling ⟨Φ₆Φ₆⟩ is the leading quartic term; GRT's unit normalization must be multiplied by (2B)²; a retarded kernel needs all Wightman orderings.
3. Literature: the exact localization has precedents for the energy density (Athanasiou–Chesler–Liu–Nickel–Rajagopal; Hatta–Iancu–Mueller–Triantafyllopoulos; Hubeny's shock-wave picture). The referee also reports that Callan–Güijosa (1999) computed the dilaton observable and concluded broadening, with an intermediate kernel that agrees with the exact one only at ω = 0 and a final formula inconsistent with their own intermediate one. **This reading was made through a text extractor and must be confirmed by eye.**
4. Extracted patterns from the transcribed functions: γ_S(n) = −(2n² + 3n + 5), γ_T(n) = −(2n² + 3n), γ_A(n) = −(2n² + 5n + 4), to be compared with GRT eqs. 4.34–4.36.

## Program audit

- `check_finite_mass_response.py`: 107 cases in seven groups, all passing, byte-identical on repeated runs, 2–3 s. An earlier version of group G expected a continuum of delays in the time domain and failed; the failure led to the discovery that the depth integrand is a total derivative, after which the group was rewritten around the closed form. Two tolerance adjustments were made after inspection (a trapezoid identity at relative 10⁻⁵; a finite-difference check of g₄ at 3×10⁻⁵).
- `check_quartic_input.py`: 93 cases, all passing, deterministic, well under a second. The transcribed Δ = 2 functions fail 16 of 18 crossing relations and the OPE constraint; this is recorded as a passing case ("transcription inconsistent"), and those functions are not used anywhere.

## Residual concerns for a specialist

- **The CGG equation numbers and formulas** were read through a fetch summary of arXiv:0906.1592. The nonrelativistic limits agree with the independent derivation, which is strong evidence, but the transcription should be compared with the paper by eye.
- **Callan–Güijosa.** The claimed discrepancy is the most consequential literature statement in the note and rests on a single text-extractor reading.
- **Nonlinear localization** of the dilaton response is conjectured from the energy-density precedent, not shown.
- **The Lorentzian cubic kernel** was not computed; Proposition 7 is a discontinuity-structure argument.
- **The manuscript** was drafted in the same session and inspected page by page by the same assistant only.

## Repository hygiene

Nothing from the three N4SYM sessions is committed. `validation/check_package.py` was not run. A zero-byte `.git/index.lock` may be present and should be removed by the author before committing.
