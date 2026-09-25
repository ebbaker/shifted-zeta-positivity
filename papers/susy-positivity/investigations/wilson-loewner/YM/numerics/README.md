# YM hierarchy numerics

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
