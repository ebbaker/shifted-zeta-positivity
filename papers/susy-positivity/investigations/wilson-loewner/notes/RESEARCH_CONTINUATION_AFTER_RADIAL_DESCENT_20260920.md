# Continuation after the spatial radial-descent test

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; identity supplied by the session instructions).
Effort setting: not exposed in this session; not inferred.

## Read first

1. [Spatial radial evolution does not descend to the fixed Higgs hemisphere
   sector](SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md), especially
   the centered conformal frame and the explicit non-closure calculation.
2. `numerics/check_spatial_radial_descent.py`, its small check record and
   provenance under `numerics/records/`.
3. The preserved
   [predictive hemisphere note](PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md)
   and [preceding handoff](RESEARCH_CONTINUATION_AFTER_LOCALIZATION_TEST_20260920.md).
4. Current version 0.4 sources: `sections/03_free_kernel.tex`,
   `sections/07_endpoints.tex`, `sections/s_fixed_window.tex`,
   `sections/s_localization.tex`. The manuscript pair and all four dated
   snapshots remain unchanged.

The user requested one bounded test: whether the free spatial radial
generator descends to the already specified localized hemisphere
representation, before making a spectral-parameter fit. The deliverable
is a negative result with explicit scope, plus the actual free bilocal
state. No new Codex task or sub-agent was launched.

## What this session derived

The ordinary scalar cylinder Hamiltonian has one-particle rates
`sqrt(ell(ell+1)+1/4)=ell+1/2`, with spatial multiplicity `2ell+1`.
The spatial radial generator is conformal dilation `D`.

The protected Higgs scalar in an adapted flat frame is
`O(t)=q_1(t)+t q_2(t)/(2r)`. Write `chi(t)=mathcal Q q_2(t)`, a
nonzero free fermion combination. Then

```
mathcal Q O(t) = 0
[D,O(t)] = (t partial_t + 1/2) O(t) - t q_2(t)/(2r)
mathcal Q [D,O(t)] = -t chi(t)/(2r) != 0   (t != 0).
```

This proves failure on closed representatives, rather than just citing
`[D,mathcal Q] != 0`. It also affects the exact difference
`O(t)-O(0)` and neutral separated bilocals. The vacuum is invariant,
so an interior insertion supplies a boundary-state counterexample.

The hemisphere-center issue was handled explicitly. In the literature
the cut is at `varphi=0,pi`, and the usual stereographic origin lies at
one endpoint. For concentric-sphere evolution use instead
`t=2r tan((varphi-pi/2)/2)`, with the hemisphere mapping to the ball
`rho<2r`. In the original H basis its flat polarization is
`(1-t/(2r),1+t/(2r))/sqrt(2)`. A constant change of basis gives the
formula above. The old boundary polarization is not replaced by a
Dirichlet condition on the newly named first component.

The compensation `D-R_*` preserves the protected local family and is
the exact twisted dilation. Its local-cohomology action is trivial.
The elementary 3d contraction with the moving polarization is a
constant times an ordering sign: the twist cancels the spatial
distance. This does not retain the original stationary free kernel.

Transporting the supercharge with dilation instead gives a family,
`exp(aD) mathcal Q_r exp(-aD)=exp(a/2) mathcal Q_(exp(a)r)`, in a
standard flat frame. That is not evolution inside the fixed complex.
Overall scaling of the sphere and the boundary field is consistent
with the curvature boundary conditions and keeps `x=4pi r |Y|^2`
invariant. Curvature by itself was **not** used as a blanket no-go.

The boundary-field Mellin operation remains well-defined independently:
its real contour is `s=1/2-i sigma`, its measure is `d sigma`, and
`N=-x partial_x` obeys `N^dagger=1-N` in `L^2(dx)`. The centered
operator `N-1/2` generates unitary dilation of the **field magnitude**.
No equality with spatial `D` was derived; (10) in the note obstructs
the direct fixed-sector descent.

At the fixed hemisphere, the simplest free conformal arc with
separated `Q` and `tilde Q` endpoints has identity transport and state

```
Psi_pair = Y barY Psi_0 = epsilon x Psi_0
M Psi_pair = epsilon Gamma(s+1)/sqrt(2pi),   B=0
epsilon = 1/(4pi r).
```

The gluing expectation is `epsilon/2`, agreeing with the action's
one-dimensional propagator in that ordering. Reverse collision
ordering gives `epsilon(x-1)Psi_0`; a symmetric local composite gives
`epsilon(x-1/2)Psi_0`. Neither is an extra term forced into the
separated bilocal. Its real-coordinate squared norm is `epsilon^2/4`.
The fixed action and identity transport force no extra current term.

## What was not established

- No spatial affine map `p -> s`, no spatial image of the Mellin
  contour or measure, no physical arithmetic shift, and no source-to-
  response operator were obtained.
- The complete target remains
  `F_ar(p)=pi^(-p/2)(p-1/2)Gamma(p/2+5/4)`, with
  `K^<_omega=F_ar(p-omega)/F_ar(p+omega)`. It was not compared to the
  bilocal by an invented parameter identification.
- The previous degree-two obstruction remains conditional on its
  previous trial dictionary. This session does not strengthen it into
  a universal obstruction, and does not choose `N(2N-1)`.
- The negative result concerns fixed-charge cohomological descent.
  It does not exclude an unprotected calculation, a family of
  complexes with intertwiners, a different protected sector, a chosen
  grading of chiral primaries inserted at the center, or a genuine
  four-dimensional Wilson/defect construction.
- A grading after projecting to selected representatives does not by
  itself implement the original radial evolution on equivalent
  representatives. A deformation of `epsilon` also changes the
  protected algebra and needs its own physical definition.
- No arithmetic contraction, cumulative norm, additional horizon,
  smoothing benefit, or averaging benefit follows from this control.

## Reproduce and verify

From `papers/susy-positivity/investigations/wilson-loewner`:

```sh
python3 numerics/check_spatial_radial_descent.py \
  --output /tmp/spatial-radial-descent-replay.json
python3 numerics/check_spatial_radial_descent.py --order 40 \
  --output /tmp/spatial-radial-descent-order40.json
python3 validation/drafts.py check
python3 validation/check_package.py check
```

The new checker passes 83 cases at both orders: 57 exact rational
checks and 26 floating-point checks. It imports the standard-library
quadrature helper from the preceding hemisphere checker. Both source
hashes are included in its output. The saved primary run uses order
24; the order-40 output is disposable. These tests audit the written
calculation, not the external supersymmetry input or quantum positivity.

The live package inventory is updated separately from the frozen
version-0.4 build records. The new checker has its own research record;
the manuscript's historical 299 diagnostic cases are not relabeled
as including it. The five pre-existing untracked localization files
were preserved. No third-party papers or large generated data were
added. No commit was made by this session.

## Next bounded decision

The first useful audit is to challenge the **fixed-sector non-closure
argument**, especially the centered conformal frame and its use for
boundary states. A counterproposal must say which generator acts,
which representatives it acts on, and why exact-equivalent states
remain equivalent. A gamma divisor or polynomial fit is not an answer
to this test.

If that obstruction is accepted, do not enlarge the determinant
calculation in the same fixed free sector. To retain ordinary spatial
evolution, the next localization project needs an explicit interface
or connection relating the scale-dependent supercharges and boundary
polarizations, or it must retain the discarded unprotected states.
The required check is an intertwining identity, including the ordinary
adjoint and the fate of the rates `ell+1/2`; the compensating R current
alone removes those dynamics in the tested local cohomology.

The separate cumulative-defect program can instead resume from
`../../critical-path/notes/RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md`
and its subsequent local records, without importing any new positivity
claim from localization. Inspect the current critical-path index before
choosing a numerical experiment there; this session did not advance it.

Any continuation should preserve historical material, follow
`LARGE_FILES.md`, and record the model and only an actually exposed
effort setting. Specialist review remains outstanding.
