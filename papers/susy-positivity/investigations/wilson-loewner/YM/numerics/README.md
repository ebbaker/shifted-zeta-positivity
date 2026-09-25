# YM numerics and algebra controls

## Native electric recentering controls, 25 September 2026

The [new checker](check_current_recentering.py) and [small record](records/current-recentering-20260925.json) accompany the [recentring/positive-completion note](../notes/NATIVE_RECENTERING_AND_GAPPED_POSITIVE_COMPLETION_20260925.md). Prepared for Edward Baker with substantial GPT-6 (Codex) assistance; exact variant and reasoning effort unavailable.

Run from the YM directory with Python 3 and NumPy:

```sh
OPENBLAS_NUM_THREADS=1 python3 -B numerics/check_current_recentering.py --output /tmp/ym-current-recentering.json
```

Nineteen floating controls passed: sine quadrature refinement and Plancherel, local identity-packet recovery, mixed winding coefficients, and retained/escaped norms for windings 2, 3 and 5. Scales 16, 64, 256 and 1024 are recorded. The script also records the proved coercive lower bound at four prime cutoffs. Haar and a prescribed radial density are comparisons, not interacting four-dimensional current samples. Full-state convergence, closability, and divergence are analytical results; these controls do not prove them. Arrays remain in memory and only a small JSON record is saved.

## Electric-parity review rerun, 25 September 2026

The [review rerun record](records/electric-parity-review-20260925.json) records unchanged executions of the 57 character controls and 19 archimedean controls for the [critical review](../reviews/ELECTRIC_PARITY_RESPONSE_CRITICAL_REVIEW_20260925.md). All passed. It includes script and reviewed-file hashes, commands, environment, and compact summaries; the existing scripts above their respective records remain the reproduction sources. The new bounded-occurrence theorem is analytical and does not depend on these floating diagnostics. No original script or record was overwritten.

## Electric parity and archimedean response, 25 September 2026

The [new checker](check_archimedean_response.py) and [small record](records/archimedean-response-20260925.json) accompany the [response note](../notes/ELECTRIC_PARITY_ARCHIMEDEAN_RESPONSE_AND_PHASE_OBSTRUCTION_20260925.md) and [audit](../reviews/CHARACTER_CURRENT_AND_PRIME_DOMAIN_AUDIT_20260925.md). Prepared with substantial GPT-6 (Codex) assistance; exact deployed variant and reasoning effort unavailable.

Run from the YM directory with Python 3 and NumPy:

```sh
OPENBLAS_NUM_THREADS=1 python3 -B numerics/check_archimedean_response.py --output /tmp/ym-archimedean-response.json
```

Nineteen floating controls compare the finite log-angle matrix with an independent Fourier/digamma integral for both sine and cosine parity; verify the contact and difference kernel; check the logarithmic asymptotic, pi-current reversal, winding-two defect, nonidentity-phase divergence, and an explicit negative signed full-core response. A finite weighted pairing uses a prescribed nonconstant density, not an interacting Wilson sample. Coarse and refined errors are retained. All passed in the saved environment. The 57 earlier character controls were also rerun unchanged and passed. Neither set certifies limiting statements or positivity.

Only the script and small provenance/summary record are saved. All arrays remain in memory; no external datasets or large files are generated.

## Character channels and current controls, 25 September 2026

The [character checker](check_character_channels.py) and [small record](records/character-channels-20260925.json) accompany the [character-channel note](../notes/CHARACTER_CHANNEL_LIMITS_AND_PRIME_MIXED_PAIRINGS_20260925.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; reasoning effort not exposed or inferred.

Run from the YM directory with Python 3 and NumPy: `python3 -B numerics/check_character_channels.py --output /tmp/ym-character-channels.json`.

The 57 controls cover the actual weighted-adjoint formula using prescribed densities, exact root branching, mixed packet limits including common-divisor weights, phase orthogonality, positive prime-type differences, two-dimensional gluing multipliers, electric energy growth, the electric–Wilson current approximation, and its growth on winding-created components. All passed in the recorded environment. Finite exact controls had maximum absolute discrepancy below 2.2e-14; final asymptotic comparisons were below 8.6e-6, against tolerance 2e-5.

Phase refinement runs through representation scale 8192, and the current comparison through scale 2048. Intermediate errors are retained, including coarse comparisons exceeding the final tolerance. The Haar and positive central test densities are algebra controls, not interacting YM samples. No infinite limit is certified by this floating calculation; those claims have analytical arguments in the note. The small record includes parameters, environment and checker provenance. No large arrays or external datasets are stored.

## Winding-source mixed-pairing controls, 25 September 2026

The [winding checker](check_winding_electric_pairing.py) and [small record](records/winding-electric-pairing-20260925.json) accompany the [native source and electric pairing note](../notes/NATIVE_WINDING_MELLIN_SOURCES_AND_ELECTRIC_PAIRING_20260925.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; reasoning effort not exposed or inferred.

Run from `wilson-loewner/YM` with Python 3 and NumPy:

```sh
python3 -B numerics/check_winding_electric_pairing.py --output /tmp/ym-winding-electric-pairing.json
```

The 64 controls compare finite Laurent norm and electric mixed Gram formulas against direct angular quadrature, including negative windings and complex pairs. They also check the Haar finite-difference identity and normalization. All passed in the recorded environment; maximum scaled discrepancy was below 1.6e-15. Haar and a prescribed positive central density are algebra controls, not samples of the interacting state. The source's infinite-winding limit and exclusion theorem are analytical and are not certified by this floating calculation. The script and small provenance record are the complete reproducible material; no large data are generated.

## Earlier hierarchy controls

The [checker](check_positive_hierarchy.py) and [record](records/positive-hierarchy-preliminary-20260924.json) accompany the [preliminary analysis](../notes/YM_POSITIVE_HIERARCHY_PRELIMINARY_ANALYSIS_20260924.md). Prepared for Edward Baker with GPT-6 (Codex) assistance; reasoning effort not exposed or inferred.

Run from `wilson-loewner/YM` with Python 3 and NumPy:

```sh
python3 -B numerics/check_positive_hierarchy.py --output /tmp/ym-positive-hierarchy.json
```

The program runs 64 controls:

- exact finite OS null-space controls and examples of returning storage and nonunitary scalar transport;
- generic SU(3) residual identities, including the cubic moment;
- moving Gram-metric conservation and the effect of omitting its connection;
- a nonautonomous four-state memory reconstruction and positive Gram kernel;
- actual Loewner tip geometry, noncommuting SU(2) prefix/chord transport, the two-observable approximation and evaluated residual error bounds, including step refinement.

The field configurations and positive weights are chosen explicitly. They are not draws from the YM measure. The geometry uses the square root of capacity as the integration variable to regularize the tip; all displayed capacities are its square. It integrates the prefix transport directly and computes the reduced model separately from chord curvature moments.

The record includes code provenance and summarizes outputs. Only sources and the small record are retained. No large matrices, ensembles or third-party papers are stored.

The diagnostic inequalities include numerical tolerances. The residual theorem is analytical under its stated assumptions, but its floating quadrature in this program is not an interval enclosure. Passing these controls establishes neither an interacting vacuum bound nor a continuum limit. It also does not establish arbitrary-input passivity or an arithmetic realization.


## First interacting finite-slab experiment

The [sampler](sample_finite_slab.cpp), [driver and analysis](check_finite_slab.py), and [small record](records/finite-slab-20260924.json) accompany the [reflection derivation](../notes/FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md) and [interacting test](../notes/FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md). This session samples the actual pure SU(2) Wilson measure on a spatial 6³ torus with five open time slices, at beta 1.6. It is separate from the prescribed-background controls above.

Run from `wilson-loewner/YM`, with Python 3, NumPy and a C++17 `clang++` compiler:

```sh
python3 -B numerics/check_finite_slab.py --work-dir /tmp/ym-finite-slab-20260924 --record /tmp/ym-finite-slab-20260924.json
```

This compiles into the scratch directory and runs four seeded chains concurrently. It writes raw per-configuration averages, sampler diagnostic logs, path words, and a hash manifest there. The program then computes correlated batch-bootstrap uncertainties, forward projections, all three output bounds, and held-out-chain comparisons. Reanalysis checks the raw-file and sampler-source hashes:

```sh
python3 -B numerics/check_finite_slab.py --work-dir /tmp/ym-finite-slab-20260924 --record /tmp/ym-finite-slab-20260924.json --analyze-only
```

The committed material consists of sources and the small summary record. Raw chains and executables are regenerable scratch material kept outside Git; they are not deposited as a permanent data archive. The record contains both stored-file and canonical numerical-content hashes, parameters, seeds, provenance, checks and per-chain summaries. Matching hashes establishes data identity in the tested environment, not portability across compilers, standard-library random-number implementations or floating-point environments. No proof depends on reproducing a hash. Regeneration needs no external dataset.

The geometry is fixed before sampling: driver u(t)=t, capacities 0, 1, 2.8, 6, specified nearest-vertex trace and straight-chord rasterization. A finer geometry mesh gives the same words, and an independent implicit tip equation is checked. The 216 translated loops in each configuration are averaged before statistical analysis; they are not treated as 216 independent samples.

Controls include full-action versus staple differences, gauge transformations of all measured moments, site-reflection action splitting, explicit-matrix quaternion multiplication, Haar moments, and 30 independent complex-unitary moving-projection systems. Positivity of empirical Gram matrices and passing residual inequalities are algebraic controls, not proofs of mixing or certified true-ensemble bounds.

The result is unfavorable for the tested local curvature family: large state residuals and loose output bounds remain, and a larger family can worsen a later scalar readout. The notes retain that negative result and specify the next local-sector comparison. The continuous norm-preserving system from the first checker and the discrete contractive projection from this experiment must not be conflated.
