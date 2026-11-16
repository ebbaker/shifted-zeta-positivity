# TN6-E03 r1 — Finite acquisition assessment

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The author selected
**gpt-6.1-sol / ultra** for this separate internal assessment, the same
dispatch settings as E02. Independent attestation of backend identity
and runtime effort is unavailable.

**Accepted as a finite certificate at the issued scope.** The exact
status in the [E02 return][return] is “Complete pass at 256 bits, certified
within the issued execution scope.” The [E03 manifest][e03m] authenticated
7 inputs and the pinned [E02 manifest][e02m] authenticated 22 by byte
count and SHA-256 at assessment time. The [assessment record][record]
binds the exact inputs and checks. This is a finite absolute
approximation milestone under the [result index][results],
[avoid index][avoid] and [avoid 01][a01].

## Source, indexing and error payments

- **Complete source and tails.** The [GNP chapter][source] gives
  \(W_*=e^{u^2/2}\Phi\), \(\lambda=1/2-\tau\), full even reflection
  and \(H_{1/2}(0)=Z_*/2\) for the full-line mass \(Z_*\).
  Every summand on \(u\ge0\) is positive because
  \(r_m=\pi m^2e^{4u}>3/2\). On \([0,U]\) the bounds
  \(2r_m^2-3r_m\le2r_m^2\) and \(e^{-r_m}\le e^{-\pi m^2}\),
  monotonicity of \(u^{2k}e^{u^2/2+9u}\), and the successive-ratio
  bound \((10/9)^4 e^{-19\pi}<1\) for \(m\ge9\) give the issued
  full-line omitted-mode allowance \(A_k\).
  The [ITP bound][itp] uses
  \(\sum_{m\ge1}m^4e^{-\pi(m^2-1)}<2\): the \(m=2\) term is
  at most \(16e^{-9}\) and the subsequent ratios are bounded by
  \((3/2)^4 e^{-15}<1/2\). This gives
  \(\Phi(u)<10e^u\rho^2e^{-\rho}\), \(\rho=\pi e^{4u}\).
  On \(u\ge2\) and \(k\le16\),
  \(2k\log u+u^2/2+u\le u^2/2+33u\le16u^3\le\rho/2\),
  using the cubic term of \(e^{4u}\) and \(\pi>3\).
  With \(du=d\rho/(4\rho)\), both half-lines give
  \(B=10(R+2)e^{-R/2}\), \(R=\pi e^8\).
  Thus the doubled retained moment pays \([0,A_k+B]\).
  The direct comparison stays on the half-line and pays the
  symmetric radius \((A_0+B)/2\) since the real multiplier has
  modulus at most one. The [generator][gen] evaluates these bounds
  outward and supplies Acb with entire callbacks on the four exact
  dyadic panels, following the [recorded API contract][api].
- **LDL and couplings.** The degree-\(i,j\) same-parity Gram entry
  is \(m_{i+j}\), stored at index \((i+j)/2\) in the even-moment
  list. Eliminating the earlier same-parity monomials yields the
  raw squared monic norm \(h_i\). The opposite-parity projections
  vanish. Divisions follow strict lower-endpoint pivot tests.
  Both scaled-block condition diagnostics use exact diagonal ones,
  a validated inverse and a product of outward row norm bounds.
  They are separate from the acceptance gates. The coupling between
  sites \(n-1,n\) is \(a_n=\sqrt{h_n/h_{n-1}}\). The finite
  nominal matrix uses the exact stored dyadic midpoints of edges
  \(1,\ldots,15\), symmetric with zero diagonal. Zero padding and
  the maximum adjacent-radius sum give the row norm bound \(\delta\)
  on the internal perturbation, hence also a spectral norm bound by
  symmetry. Edge 16 contributes via
  \(\prod_{n=1}^{16} a_n^2=h_{16}/h_0\) to the remainder.
- **Uniform ideal function.** The [R2 proof][jch] uses Gaussian
  quadrature exact through degree 31 and the real Hermite
  interpolation remainder bounded by the square of the monic
  degree-16 polynomial. Its squared norm in the probability
  measure is \(h_{16}/h_0\). Averaging the cosine bound over
  \(s=x+\sqrt{2\tau}G\), \(G\) standard normal, gives
  \(S_{16}(\tau,x)=\sum_{k=0}^{16}\tau^k x^{32-2k}/[k!(32-2k)!]\).
  Nonnegative terms give its uniform maximum at \((1/2,\pm8)\).
  The rational validator reconstructed that corner and
  \(Q=\operatorname{upper}(h_{16}/h_0)S_{16}(1/2,8)\).
  For real symmetric \(A,B\), Duhamel gives
  \(\|e^{isA}-e^{isB}\|\le |s|\|A-B\|\).
  The same Gaussian average bounds the cosine readout perturbation
  by \((|x|+\sqrt{4\tau/\pi})\delta\le9\delta\), including
  \(\tau=0\). The matrix scalar magnitude is at most one, so
  replacing \(Z_*/2\) by the midpoint \(\widehat Z/2\) pays
  \(\eta_Z=\operatorname{rad}(Z_*)/\operatorname{lower}(Z_*)\)
  in base-mass units. The resulting exact nominal function satisfies
  \(Q+9\delta+\eta_Z<1.515\times10^{-25}\) across
  \(0\le\tau\le1/2,\ |x|\le8\). Complete moment errors have
  already entered the coefficients and mass through their enclosures.
- **Nine machine readouts.** The matrix exponential is formed with
  the square of the finite nominal matrix. Parity conjugation sends
  \(\widehat J\) to \(-\widehat J\) and fixes \(e_0\), making
  the \((0,0)\) entry of \(\exp(-\tau\widehat J^2+ix\widehat J)\)
  real. Each imaginary ball contains zero. The validator checks
  the real ball scaling by \(\widehat Z/2\), the rounding payment
  \(2r_j/\operatorname{lower}(Z_*)\), and physical enlargement by
  \((Q+9\delta+\eta_Z)\operatorname{upper}(Z_*)/2\).
  All nine totals including rounding are below \(1.515\times10^{-25}\)
  in base-mass units. The separate direct integrals enclose the
  same field and use their own tail payment. The validator checks
  their radius cap, overlap and both oriented difference intervals.
  The maximum normalized rounding and direct radii are respectively
  below \(1.740\times10^{-77}\) and \(3.812\times10^{-68}\).
  The absolute nominal-minus-direct bound is below
  \(7.771\times10^{-27}\) in physical units, largest at
  \((\tau,x)=(1/2,8)\). Overlap tests consistency after both
  independent error payments. The machine rounding result covers
  the nine frozen points.

## Replay, failed gate and costs

The one unchanged generator replay wrote to a new temporary path.
It exited 0 after 2.069 s under a 60-second outer process-group
watchdog. The inner numerical process took 1.874 s.
The [rational validator][validator] checked all 527 exact dyadic
midpoint/radius/endpoint triples per record, the ledger inequalities
and containments, sample and integration order, and cost and work
counts. The generator itself verifies that repacked balls contain
their original Arb values. After removing timings and timing sums,
the entire payload, including decisions and counts, is identical.
Its canonical SHA-256 is
**ea5ba6a8fa863c13bd3f8012c96e40dcc38e17b6109ae53063916769f40e2454**.
The final validator check took 0.061 s. The replay and all arithmetic
checks were within 120 seconds. The retained receipt carries the
identities and evidence. Later validator use requires the frozen
inputs, including the pre-update result-summary guide, verified
against both manifests at the validator's repository root.

At 128 bits all 17 pivots and 16 couplings are positive, and only
the acquisition gate fails. Its exact row radii give
\(9\delta\approx1.790589064\times10^{-7}>2\times10^{-9}\),
with the largest row sum at zero-based site 14. The valid enclosures
are retained. This width failure applies to the 128-bit algorithm
and issued tuple. It supplies no lower bound on actual field error.
The 68 integrations use 4,384 callbacks and 35,072 mode evaluations.
The gate runs before chain or direct readouts. At 256 bits, 104
integrations and nine exponentials use 15,636 callbacks and 125,088
mode evaluations. The successful gate ends the ladder at 256 bits.
The code requests the frozen 64/8,000/20 call parameters and
\(2^{-p+32}\) tolerances. Counts are below 400,000 per attempt and
800,000 total. Recorded times are below 0.006 s for individual
integrations and 0.0037 s for exponentials, within the 15 s and
30 s limits and the inner 900 s process limit. Watchdog and
counter branches were inspected. The successful replay exercises
neither forced timeout nor interrupted checkpoint recovery.

| Measured operation scope | Original | Replay |
| --- | ---: | ---: |
| Attempt wall, 128 and 256 bits | 0.322 / 1.521 s | 0.310 / 1.420 s |
| Inner process wall | 1.986 s | 1.874 s |
| Acquisition phase across attempts | 1.136 s | 1.076 s |
| Nine readout phase | 0.152 s | 0.142 s |
| Chain setup plus nine, with failure charged | 1.288 s | 1.218 s |
| Direct nine-point phase | 0.535 s | 0.493 s |
| Amortized chain / direct over nine | 0.143 / 0.059 s | 0.135 / 0.055 s |
| Successful acquisition phase plus first exponential | 0.818 s | 0.769 s |
| First direct point's four integral calls | 0.0104 s | 0.00949 s |

Phase timings include checkpoint and loop overhead. First-use operation
sums cover the specified different scopes. The chain took longer across
nine points in both runs. Achieved radii differ and the Gaussian rule
with the same Jacobi coefficients has identical scalar values. The
measured comparison is local to these executions. [Avoid 20][a20]

## Collision screen and disposition

The actual [B02 screen][b02] uses [controls 12][controls] and names
the failed premises under [avoid 02][a02] and [avoid 07][a07].
For the three-atom witness at \(T=1/4,x=\pi\) the output and its
first derivative vanish and the second derivative equals two. The
exact terminating chain has zero approximation error there. The
strict Gram positivity through degree 16 fails by finite rank,
also for atomic finite-profile witnesses with insufficient support.
The continuous extensions fail the literal theta input. Euler-factor
translates fail the unshifted source identity. Weighted-square,
finite-theta changes and finite-prime orbit examples fail the
unchanged arithmetic coefficients and can fail full reflection.
The reflected quartic, smooth shape and positive-primitive examples
fail the integer-square expansion and its tail payments. The
quartic event at \(T=1/4,x=\pi/4\) is in the box and permits generic
moment approximation. The other event locations and small-damping
qualifications retain their source scopes. RH-conditional controls
fail ordinary Dirichlet arithmetic and retain their conditional
status. The altered-kernel example fails the full cosine/Newman
observation with the same acquired amplitude. The actual-profile
relaxation concerns a positive measure representing relaxed zero
data, outside the canonical Fourier source premise. These analytical
checks admit absolute approximation at a control collision. Signed
margins, zero exclusion and growing-height conclusions remain open
beyond the task.

No E02 implementation correction occurred and no E03 response check
was needed. The assessment shares the pinned GNP source, R2 assumptions,
Acb semantics and generator implementation. The separate arithmetic
checks the saved endpoints and their use. This same-model internal
review and reproduction within the same numerical environment do
not supply independent specialist review. Ownership transfers to
the coordinator. [Avoid 05][a05] [Avoid 17][a17] [Frozen E03 request][e03]

[e03]: ../research-progress/handoffs/TN6-E03-r1.md
[e03m]: ../numerics/10_TN6_E03_R1_INPUT_MANIFEST_20261114.json
[e02m]: ../numerics/08_TN6_E02_R1_INPUT_MANIFEST_20261114.json
[return]: ../research-progress/handoffs/TN6-E02-r1-return.md
[record]: ../numerics/11_TN6_E03_R1_ASSESSMENT_RECORD_20261114.json
[validator]: ../numerics/assess_tn6_e03_r1.py
[gen]: ../numerics/execute_tn6_e02_r1.py
[api]: ../references/01_BALL_INTEGRATION_SOURCES_20261114.md
[source]: ../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex
[itp]: ../04_exact_infinite_tensor_products/notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md
[jch]: ../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md
[b02]: ../brainstorm/notes/02_TN6_B02_FINITE_COEFFICIENT_ACQUISITION_DECISION_20261114.md#actual-collision-control-screen
[results]: ../../../result-summaries/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a17]: ../../../avoid/17_parallel_writers_and_broken_registries.md
[a20]: ../../../avoid/20_volume_without_a_gain.md
