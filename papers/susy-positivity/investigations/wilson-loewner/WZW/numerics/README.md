# WZW continuation diagnostics

## Thermal boundary coupling and front rigidity

The [structural diagnostic](check_thermal_boundary_structure.py) accompanies the [research note](../notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md) and [audit](../reviews/review_codex_thermal_boundary_structure_20260923.md). Its [record](records/thermal-boundary-structure-20260923.json) has 203 passing floating controls for native occupation-changing Kubo response, oscillator storage, the full modular boundary connection, finite-spectral-mass bounds, and the failed front and shift tangent.

From the parent Wilson–Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_thermal_boundary_structure.py --output /tmp/thermal-boundary-structure-replay.json
```

The recorded run uses mpmath 1.3.0 at 60 decimal digits, with occupation sums through 400 and tail controls. It uses no sibling program or external dataset. These are checks of the stated linear-response model and analytical exclusion, not a microscopic finite-coupling quantum simulation or interval certificate. Earlier suites remain unchanged.

## Finite-place thermal radiation interface

The [interface diagnostic](check_finite_place_interface.py) accompanies the [research note](../notes/FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md) and [audit](../reviews/review_codex_finite_place_interface_20260923.md). Its [record](records/finite-place-interface-20260923.json) has 144 passing floating controls. They solve the actual unitary loop boundary conditions, trace the native Gibbs state, integrate coherent and fluctuating pulse output plus loop storage, and verify the predicted coefficient failures and the finite-Euler completion pole. Passing checks confirm these scoped exclusions; a completed arithmetic physical realization is not claimed.

From the parent Wilson–Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_finite_place_interface.py --output /tmp/finite-place-interface-replay.json
```

The recorded run uses mpmath 1.3.0 at 60 decimal digits. Pulse overlaps are integrated from their exact interval lengths; thermal shell sums use occupation cutoff 360 with an explicit tail bound. There is no time grid, external dataset, sibling-program import or interval certificate. Earlier suites are unchanged.

## Arithmetic orbit weights and the Bost–Connes thermal source

The [orbit-weight diagnostic](check_arithmetic_orbit_weights.py) accompanies the [research note](../notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md) and [audit](../reviews/review_codex_arithmetic_orbit_weights_20260923.md). Its [record](records/arithmetic-orbit-weights-20260923.json) has 87 passing controls: 17 exact integer and 70 floating. They verify primitive coefficients, finite-place thermal laws, the prime-source derivative, local norm formulas and two specified norm limitations. They do not establish the missing causal scattering interface.

From the parent Wilson--Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_arithmetic_orbit_weights.py --output /tmp/arithmetic-orbit-weights-replay.json
```

The recorded run uses mpmath 1.3.0 at 50 decimal digits. Exact primitive-count and projector controls, a full Dirichlet-series comparison with an elementary tail bound, shell calculations and a piecewise pulse-energy integral are included. No external data, zero table, interval certificate or sibling-program import is used. Earlier suites are unchanged.

## Continuous exponent and fractional cusp field

The [fractional cusp diagnostic](check_fractional_cusp.py) accompanies the [research note](../notes/CONTINUOUS_EXPONENT_AND_FRACTIONAL_CUSP_TEST_20260923.md) and [audit](../reviews/review_codex_fractional_cusp_20260923.md). Its [record](records/fractional-cusp-20260923.json) contains 80 passing floating controls. These reproduce the positive memory law and leading front match, then verify the predicted arithmetic exclusions. There is no arithmetic realization or RH result.

From the parent Wilson--Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_fractional_cusp.py --output /tmp/fractional-cusp-replay.json
```

The recorded run uses mpmath 1.3.0 at 50 decimal digits, with 65 for one first-prime integral refinement. Independent Bessel, positive relaxation, energy and stable-density calculations are included. No external data, numerical zero table, interval certificates or sibling program imports are used. All earlier diagnostics and records are unchanged.

## Modular Hodge scattering and cusp coupling

The [modular diagnostic](check_modular_scattering.py) accompanies the [research note](../notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) and [audit](../reviews/review_codex_modular_scattering_20260923.md). Its [record](records/modular-scattering-20260923.json) has 65 passing controls: 5 exact rational and 60 floating. They check the half-shift gradient channel, norm, native arithmetic kernel, specified real cusp load, tangent exclusion, and corrected prior kernels. Passing controls do not establish a variable-shift physical realization or RH.

From the parent Wilson--Loewner directory, with Python 3, mpmath and NumPy installed:

```sh
python3 -B WZW/numerics/check_modular_scattering.py --output /tmp/modular-scattering-replay.json
```

The program imports both sibling continuation programs for independent incomplete-beta regression checks. The recorded run uses mpmath 1.3.0 at 50 decimal digits (65 for the energy refinement) and NumPy 1.25.1. Pole samples are solved locally; no zero table or interval certificate is used. The record stores the program and sibling hashes.

**Correction:** both earlier continuation programs had an exponential factor fixed at its half-shift value in the general-shift kernel quadrature. The corrected 60-case bounded and 51-case Brownian suites were fully replayed successfully. Their notes and audits document the changed sample values and unchanged analytical exclusions. The parent 22 September programs and records are unaffected.

## Brownian bridge readout

The [Brownian diagnostic](check_brownian_readout.py) accompanies the [readout test](../notes/BROWNIAN_BRIDGE_READOUT_TEST_20260923.md) and [same-assistant audit](../reviews/review_codex_brownian_readout_20260923.md). Its [record](records/brownian-readout-20260923.json) contains 51 passing floating controls for the density, Mellin moments, first-passage transfer, exact norm balance, first-delay mismatch, and logarithmic readout phase. Passing controls confirm the reported formulas and exclusions; they do not establish a causal arithmetic realization or RH.

From the parent Wilson--Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_brownian_readout.py --output /tmp/brownian-readout-replay.json
```

The recorded run uses mpmath 1.3.0, 45 decimal digits, 15 extra digits for oscillatory phase integrals and a complex-moment refinement, and 12 terms in the stable theta-density branch. There is no Monte Carlo simulation or xi-zero table. These are floating diagnostics, not interval certificates.

## Bounded WZW collar readout

The [bounded arithmetic-readout diagnostic](check_boundary_readout.py) accompanies the [23 September research note](../notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md) and [same-assistant audit](../reviews/review_codex_bounded_readout_20260923.md).

Its [record](records/boundary-readout-20260923.json) contains 60 passing controls: 13 exact rational and 47 floating. These check the specified collar and primary spectral response, the full first-window arithmetic benchmark and the first delay. Passing controls reproduce the reported mismatches; they do not establish an arithmetic realization, general WZW sewing, interval certification, or RH.

From the parent Wilson--Loewner directory, with Python 3 and NumPy installed:

```sh
python3 -B WZW/numerics/check_boundary_readout.py --output /tmp/wzw-boundary-readout-replay.json
```

The earlier pilot and arithmetic-source programs remain in the parent `numerics` directory. Their records are unchanged and their case counts are separate from this continuation suite. The new program uses no external data or xi-zero table.

Prepared with GPT-6 (Codex; developer-provided identity), reasoning effort not exposed and not inferred, for Edward Baker.
