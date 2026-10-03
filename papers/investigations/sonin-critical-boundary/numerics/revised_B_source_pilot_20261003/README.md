# Revised B comparison: finite smooth source-space pilot

3 October 2026. Prepared for Edward Baker. Model: GPT-6 (Codex); serving variant and configured effort are not exposed to this subagent. All numbers are exploratory floating approximations. No continuum sign or positive-part comparison is certified.

## What was computed

The source window has length at most1 (actual source diameter0.9). Let b=9/20, phi(x)=exp(-1/(1-(x/b)^2)) on |x|<b, and A=-d²/dx²+1/4. Two nested raw source families were used:

- Pole-neutral: F_n=A(phi P_n(x/b)), n=0,...,m-1.
- Pole-neutral and exactly mean-zero: F_n=A d/dx(phi P_n(x/b)), n=0,...,m-1.

The source functions are mathematically smooth and compact. Integration by parts gives both prescribed pole zeros; the second family's mean vanishes by derivative preparation, independent of numerical normalization. Numerical Cholesky orthonormalization was applied in L². Recorded defects are around1e-14 to3e-13. These are finite source spans, not a discretization proven to exhaust the full source space with a controlled error.

For each family, Q=Gamma-W_2 was computed by sampled-source Fourier quadrature for the gamma multiplier and direct correlation quadrature for the sole active prime delay log2. Eigenvalues, approximate moment residuals, runtime versions and parameters are retained in the small JSON files. Regenerable B/Q/K, positive-part, source-transform and Gram arrays are not committed; content hashes identify the derived arrays in each tested runtime.

The actual-Sonin trial construction inherited from the prior pilot supplies mathematical transported columns y_j=D_2 Pi_infinity b_j from normalized physical indicator seeds. It retains the full identity complement in the prolate resolvent approximation. All transported Gram integrals are compact by the cosine/dilation identity. For each source, convolution responses were integrated over a finite logarithmic output interval; this produces the finite source quadratic form B_d. The mathematical exact construction satisfies0<=B_d<=B. Floating values in these records have no error enclosure and therefore are not certified lower endpoints.

We then formed K_d=B_d-Q, the positive spectral part (K_d)_+, B_d-(K_d)_+, and the generalized spectrum of K_d relative to B_d. The summary also gives ||B_d^(-1/2)(K_d)_+B_d^(-1/2)||. In this finite model the revised comparison is equivalent to that last norm being at most1.

## Findings

| Source family | Source dimension | Trial columns | max eig K_d | min eig[B_d-(K_d)_+] | Relative positive-part norm |
|---|---:|---:|---:|---:|---:|
| Pole-neutral |8|320|0.0194985|0.0765226|0.173130|
| Pole-neutral |8|640|0.0233067|0.0751878|0.203861|
| Pole-neutral |12|320|0.0205309|0.0703677|0.191049|
| Pole-neutral, mean-zero |8|320|-0.0305293|0.340648|0|
| Pole-neutral, mean-zero |8|640|-0.0100773|0.347866|0|
| Pole-neutral, mean-zero |12|320|-0.0221159|0.289711|0|

The finite models contain no counterexample to the revised comparison. The pole-only models have a positive K_d direction and therefore exercise a nonzero positive-part calculation. In the tested mean-zero models, K_d remains negative definite, so their positive-part test is presently trivial. This does not contradict the separate localized two-packet construction; these low-degree broad smooth sources are a different finite family, and B_d omits positive trace contributions.

The full Q matrices are positive definite on all tested spans. For the pole family, the first two diagonal values reproduce the inherited even/odd arithmetic diagnostics1.43923795758 and1.04780858696. Doubling the source grid16384->32768 and Fourier padding16->32 changed the dimension8 Q entries by at most3.2e-14 (pole) and1.14e-13 (mean-zero). These are empirical sensitivity checks, not bounds on the quadrature or high-frequency tail.

Spatial trial refinement remains material: at source dimension8, the operator norm of B_640-B_320 is approximately0.149881 for the pole family and0.355795 for the mean-zero family. Their least difference eigenvalues are positive in floating arithmetic, consistent with nested exact trial spaces. These changes are much larger than the small positive K_d eigenvalues. Hence the full K matrix is not accurately enclosed by these runs.

Opposite-parity B_d entries need not vanish after restricting the output integration. They range up to about7.2e-4 in the saved runs; source reflection symmetry holds for the full-output form. This is another reason not to treat the output-truncated floating matrix as the full B.

## Interpretation limits

1. Even in exact arithmetic, B_d<=B only gives K_d<=K. It does not give an upper estimate of K or of its positive part sufficient for the proposed comparison.
2. The positive part of a finite source compression is generally different from compressing the full operator's positive part. Increasing source dimension8->12 already changes the compressed positive part by about0.00128 in the pole-family model.
3. Q>=0 implies the generalized K_d/B_d eigenvalues are at most1 in each exact model, but this alone does not imply B_d>=(K_d)_+ when the matrices do not commute. The separate positive-part test was therefore computed explicitly.
4. The matrices do not generally commute: the recorded Frobenius commutator norms are nonzero. No abstract monotonicity or scalar reduction has been inferred.
5. A useful next certificate needs an upper control of the omitted positive trace form on a selected source span, plus source-space complement/positive-part control if the proposed conclusion concerns the full source operator. Certifying only a Galerkin lower B_d does not meet that requirement.

## Reproduction

Dependencies are Python3.12.14, NumPy2.5.3, SciPy1.17.1 and python-flint0.9.0 in the retained runs; platform macOS14.5 arm64. No matrices or sampled grids are persisted. Regenerable arrays are hashed as compact UTF-8 JSON with standard Python float formatting, as stated in each record. Hashes identify the computed arrays; they do not certify mathematical accuracy or cross-platform reproducibility. With dependencies available, from this directory after integration into the repository (the inherited prolate generator is located by walking repository ancestors):

```sh
OPENBLAS_NUM_THREADS=1 python3 -B source_space_pilot.py --dim 8 --cells 640 --nper 2048 --output pole8_c640.json
OPENBLAS_NUM_THREADS=1 python3 -B source_space_pilot.py --dim 8 --cells 640 --nper 2048 --mean-zero --output mean8_c640.json
OPENBLAS_NUM_THREADS=1 python3 -B source_space_pilot.py --dim 12 --cells 320 --nper 2048 --output pole12_c320.json
OPENBLAS_NUM_THREADS=1 python3 -B source_space_pilot.py --dim 12 --cells 320 --nper 2048 --mean-zero --output mean12_c320.json
python3 -B summarize.py
```

`trial_geometry.py` retains the preceding actual-Sonin compact Gram construction. It regenerates the rank32 prolate model directly by calling the inherited `arithmetic-storage/numerics/prolate_certificate.py` function `certify(rank=32, precision_bits=256)` and converts its dyadic midpoint to floating entries. The generator and exact dyadic inverse hashes are stored in every record. No derived prolate matrix is committed. If run outside the repository, supply `--ancestor-numerics /path/to/arithmetic-storage/numerics`; no author-specific path is baked into the scripts.

For all eight retained cases, run `(dim,cells,nper)` equal to `(6,160,1024)`, `(8,320,2048)`, `(8,640,2048)`, `(12,320,2048)`, once with and once without `--mean-zero`. Other parameters are the defaults: seed log endpoint3.5, finite output endpoint4.5, source grid16384, Fourier padding16, prolate rank32, compact Gauss order400, seed Gauss order24. Then run `summarize.py`.

The inherited certificate establishes the exact polynomial resolvent's error. Floating conversion, compact quadrature and propagation in this pilot remain unenclosed. The scripts reject nonfinite derived arrays, but a finite result is not a successful rigorous quadrature certificate: no outward quadrature failure/success test is implemented. Approximate pole-moment residuals and mean residuals are retained as diagnostics; the exact mathematical constraints follow from preparation, not from those small sampled numbers.

The numerical source families include complex linear combinations of the real basis through their Hermitian form extensions. The published positive-part spectra concern the chosen numerically orthonormal L² basis. They do not define or verify a full infinite-dimensional positive-part operator. The preceding pilot's formulas were independently audited within this session; this is not independent specialist refereeing.
