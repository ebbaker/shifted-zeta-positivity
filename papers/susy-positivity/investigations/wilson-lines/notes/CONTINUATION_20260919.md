# Continuation after the angular-regulator calculation

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

Start with [Angular smearing and the Robin model](ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md)
and the [18 September review](../reviews/review_codex_2026-09-18.md), then Claude's
[reflection-network note](REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md).
This replaces the previous handoff's next-calculation ordering. Work remains
in the Wilson-lines investigation; manuscript 0.8 and its nine snapshots remain
unchanged.

## Repository and review state

The session began at `0889d3b`, with a clean checkout. A fast-forward-only pull
reported it was current, and Edward confirmed that this was the latest Claude
work. There was no additional unseen Claude revision. The new work in this
session is an uncommitted continuation, not a manuscript integration.

The review identifies three corrections to the reflection note: its unsmeared
continuum Gram norm is divergent; the backtracking junction has a leading spike
divergence missing from its logarithmic estimate; being a norm does not establish
supersymmetric protection. The bulk common-reference geometry and free
off-diagonal identity survive. Correction notices now link the review and the
new result without silently rewriting Claude's historical derivations.

## What is now established

1. A normalized antipodally even Poisson profile on the defect's angular S2
   defines actual free smeared endpoint fields. Their exact covariance is
   `C_rho(u)=exp(-|u|/2)/(1-rho^4 exp(-2|u|))`, finite and positive for rho<1.
   It tends to n_gamma away from the diagonal. Common-reference Wilson
   transports can be assigned to all the smearing directions; at free order
   they reduce to these fields.
2. The common bulk condition `epsilon_s=0`, `J epsilon_c=-epsilon_c` survives
   every direction on S2, not just the two original rays. This remains bulk
   Clifford algebra; full endpoint supersymmetry is not established.
3. For convolution T_rho and `M_rho=integral C_rho`, the positive operators
   `A_rho=M_rho I-T_rho` converge in strong resolvent sense to
   `b(-d_x^2)`, with `b(tau^2)=Re psi(1/4+i tau/2)-psi(1/4)`. The closed form
   domain is the corresponding logarithmically weighted Fourier L2 space.
4. The covariance's contact-subtracted limit is **minus** that energy, so it
   is not a positive covariance. No finite delta adjustment repairs it at
   arbitrarily high frequency. Normalizing T_rho by M_rho instead gives the
   identity, a white-noise limit. Neither operation supplies the full Weil form.
5. The tower `2n+1/2` is the spectrum of `sqrt(-Delta_S2+1/4)` on the even
   axial modes `Y_(2n,0)`. A single complex free half-cylinder scalar in this
   sector, with Robin boundary mass p, has boundary Gaussian determinant
   `det_zeta((H+p)/2)^(-1)`. Opposite boundary shifts give the gamma ratio;
   a reference-normalized ratio has an ordinary convergent product.

The last result is an explicit auxiliary free boundary model. A local mass on
the **full** sphere retains multiplicity 2ell+1 and does not produce the same
single gamma factor. Smearing an observable does not remove other modes from
the partition function. The sector projection, the meaning of p as a dynamical
Laplace variable, the conductor normalization, and the arithmetic remain open.

## Next work, in order

1. Solve the defect endpoint supersymmetry variations for the angular family
   `Psi_rho` using Baker, arXiv:1102.4948, Appendix C, together with the defect
   projection and spinor reality/chirality conditions. Check one common
   physical supercharge and one endpoint R-symmetry polarization for all
   directions. Do not infer this from the bulk Clifford calculation.
2. Identify the physical antilinear adjoint/reflection. A discrete odd-scalar
   symmetry is not automatically OS positive. Begin with the Gaussian scalar
   sector and permissible observable algebra before attempting the interacting
   fermion/auxiliary audit. Include the internal scalar-sign junction.
3. Test whether any physical boundary or supersymmetric reduction selects the
   even axial one-copy sector and the Robin deformation. Keep the full angular
   determinant as a control. This is the concrete missing step between the
   auxiliary determinant and a gauge-theory derivation.
4. If these prerequisites hold, calculate the regulated gauge-invariant
   network at first interaction order in one local scheme. Include arc
   self-exchange, cross-arc exchange, endpoints, and the defect piercing point.
   The positive difference-form argument additionally needs pointwise
   nonnegative kernel weights; ordinary covariance positivity alone does not
   ensure it survives interactions.

The spike correction is recorded in the review but has not been developed into
a new full junction calculation. No prime weights, contact/pole matching,
scattering passivity, or RH result has been obtained. Keep these as explicit
missing requirements, not factors to insert by hand.

## Verification and preservation

`numerics/check_angular_regulator.py` adds 185 finite cases, with a deterministic
JSON record. It independently integrates the angular profiles and the double
sphere covariance, compares position/Fourier energies, checks cutoff behavior
and rotated bulk equations, and verifies the Robin Gaussian and normalized
gamma ratio. It does not numerically certify a continuum or interacting proof.

The continuation registry now includes Claude's 1,196 reflection cases and the
new 185, alongside the previous 154: **1,535 cases total**. It binds the new
notes, the review and the current handoff as well as the check programs and
their records. Model attribution records both contributors. The original
manuscript build record and numerical records are preserved.

From the investigation directory:

```sh
python3 validation/endpoint_matter.py check --replay
python3 validation/drafts.py check
```

The older full manuscript strict replay still has the previously documented
cross-runtime floating-point diagnostic issue; its records were not refreshed.
