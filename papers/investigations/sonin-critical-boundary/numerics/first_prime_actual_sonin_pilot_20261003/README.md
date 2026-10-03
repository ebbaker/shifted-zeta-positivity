# Actual-Sonin trial pilot, 3 October 2026

Prepared for Edward Baker with substantial LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort are not exposed and are not inferred. Exploratory floating arithmetic only: no certified sign or trace lower bound has been produced.

The source is the existing exactly odd prepared bump F=A(x phi)/||A(x phi)||2, with phi supported in (-9/20,9/20). Its prior certified arithmetic upper value is Q<=1.047808594.

## Trial and metric

Let b_j be normalized physical indicators on a logarithmically graded partition of (1,R). Define exact q_j=Pi_infinity b_j, y_j=D_2 q_j. Thus y_j belong to the true first-prime Sonin space. The finite trial trace is tr(G^-1 H), G_ij=<y_i,y_j>, H_ij=<C_F y_i,C_F y_j>. Restricting the output integral in H preserves the lower-bound direction in exact arithmetic.

The pilot approximates the archimedean resolvent by I+E(R-I)E*: the full identity complement is retained. It never replaces this by E R E*. For t_j=E* T b_j, put z_j=T b_j+E(R-I)t_j and h_j=F_infinity z_j. The exact mathematical trial uses the exact resolvent; these formulas give its computational proxy. The band-projection part of h_j is a four-sine-integral corner formula; the finite correction is in transformed even Legendre polynomials (spherical Bessel functions). Substituting the proxy into the exact identities below also incurs the unpropagated inverse-model error.

All metric integrals are compact. Let N=<q,q> and S=<q,U_log2 q>. Then N=I-<b,h>, and G=1.5N-2^(-1/2)(S+S*). Expand S over x>2 into seed/seed, seed/h, h/seed, and h/h terms. The last term is exactly

    integral_0^(1/2) z_i(u) sqrt(2) z_j(2u) du
    - integral_0^2 h_i(x) 2^(-1/2) h_j(x/2) dx.

This is the unitary cosine-transform identity with dilation, with the lower interval subtracted. No spatial Gram tail is discarded. All other terms are compact seed integrals. Numerical Gaussian quadrature evaluates these formulas.

For H, logarithmic-coordinate convolution is integrated on a finite output interval using midpoint grids. Compact seed contributions use an antiderivative of F(t)e^(-t/2), avoiding sampling the indicator jumps. Smooth projection corrections use FFT convolution. The dyadic translation is exactly an integer grid shift. Source normalization and antiderivative are numerical.

## Results

At input physical endpoint exp(3.5)=33.11545, retained trial dimensions 80,160,320,640,1280 give finite-output traces approximately .6665153,.8783061,.9815153,1.0210491,1.0314268. These are all below Q's certified upper endpoint. There is no positive falsification signal from these trial lower approximations.

A bounded refinement of dimension640 changed rank24 to32, compact Gauss order240 to400, seed Gauss order20 to24, logarithmic resolution4096 to8192 cells per log2, and output endpoint4.5 to5. It gave1.02106592457960, an aggregate change1.6820e-5. Replacing the floating quadrature inverse with the midpoint of the independently certified rank32 prolate model gave1.02106592457739, a difference2.21e-12. These sensitivity comparisons are not error enclosures.

Expanding the physical seed endpoint to exp(4.5)=90.01713 at fixed dimension1280 gave1.03037457739. This has coarser local seed spacing than the endpoint33 run and therefore is not a nested comparison. It did not close the gap to Q. The smallest Gram eigenvalues fall toward1e-6; formal metric coercivity of D does not prevent projected seed columns from becoming nearly dependent.

## Status and next use

This implements the requested actual-Sonin lower-trace prototype and compact Gram reduction. It does not settle the original odd source's K sign. Before a certificate, enclose Gram integrals, finite-output overlaps, source normalization, sine-integral evaluation, and the propagated prolate and floating errors; prove the exact trial Gram positive. An omitted positive output contribution does not need an upper bound for a successful one-sided falsification, but that observation does not certify approximate quadrature.

Do not spend further unbounded effort increasing the box dimension on this source. A higher-order or source-adapted seed basis could be more efficient, but no margin currently exists for certifying B_d>Q. The alternative localized two-packet analytic construction being investigated separately may be a better route.

The accompanying SUMMARY.json and small pilot records contain parameters, numbers, and hashes. No grid arrays or large derived matrices are persisted. Only hashes and metadata for the derived 32-by-32 prolate midpoint input are retained; regenerate the matrix with the recipe below. Despite the prototype filename, the seed space is a logarithmically graded indicator space, followed by source-response eigenanalysis; it is not an optimized source-specific seed construction. The source function is currently hard-coded to this odd bump; the prototype is not an all-source theorem or a general source optimizer.

The subsequent [analytic two-packet obstruction](../../notes/FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md) refutes the all-source mean-only candidate independently of this numerical pilot. It does not supply a sign for this original broad bump.

## Reproduction and inherited input checks

The retained pilot runs used Python 3.12.14, NumPy 2.5.3 and SciPy 1.17.1 on macOS 14.5 arm64. From this folder, representative commands are:

```sh
OPENBLAS_NUM_THREADS=1 python3 -B source_adapted_galerkin.py --cells 160 --logmax 3.5 --nper 2048 --tout 4.5 --output /tmp/sonin-pilot160.json
OPENBLAS_NUM_THREADS=1 python3 -B source_adapted_galerkin.py --cells 1280 --logmax 3.5 --nper 4096 --tout 4.5 --output /tmp/sonin-pilot1280.json
OPENBLAS_NUM_THREADS=1 python3 -B source_adapted_galerkin.py --cells 640 --logmax 3.5 --rank 32 --quad 400 --seedquad 24 --nper 8192 --tout 5 --prolate-json /tmp/prolate_resolvent_midpoint32.json --output /tmp/sonin-pilot640-midpoint.json
```

All other retained parameters appear in the small JSON records. Changing the output path does not change the mathematical input. The midpoint run records its original temporary input path as provenance; regenerate the matrix and pass its local path explicitly when replaying.

`inherited_input_check.json` verifies the arithmetic/source/gamma generator bindings and the rounded arithmetic threshold. `arithmetic_prime_replay.json` was regenerated from the ancestor `arithmetic_prime_diagnostic.py` at 192 bits. This replays its Arb/Acb prime correlation integration while retaining its independently recorded source and gamma inputs. `prolate_replay_check.json` records a fresh successful rank-32, 256-bit certificate rebuild, with the same dyadic inverse hash and exactly matching floating midpoint input. These checks used Python 3.10.0, python-flint 0.9.0 and FLINT 3.6.0. None certifies the pilot's unbounded error terms.

From the repository root, the following Python snippet rebuilds the midpoint input needed by the third command in an environment with python-flint. The final conversion to floating values is deliberately labeled unenclosed:

```python
import hashlib, json, sys
from pathlib import Path

numerics = Path("papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics").resolve()
sys.path.insert(0, str(numerics))
import prolate_certificate
record, _, inverse = prolate_certificate.certify(rank=32, precision_bits=256)
output = {
    "rank": 32,
    "status": "FLOAT_CONVERSION_OF_CERTIFIED_MODEL",
    "exact_model_inverse_error_cap": "9.2e-32",
    "float_rounding_not_enclosed": True,
    "generator_sha256": hashlib.sha256((numerics / "prolate_certificate.py").read_bytes()).hexdigest(),
    "exact_dyadic_inverse_sha256": record["dyadic_inverse_sha256"],
    "R": [[float(inverse[i, j]) for j in range(32)] for i in range(32)],
}
Path("/tmp/prolate_resolvent_midpoint32.json").write_text(json.dumps(output, indent=2) + "\n")
```
