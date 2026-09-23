# Internal audit of the deterministic SU(2)_2 Loewner pilot

22 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review status:** same-assistant mathematical and source audit with LLM
assistance; not an independent review. No sub-agents were used.

Reviewed: [research note](../notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md),
[checker](../numerics/check_wzw_loewner_pilot.py), and
[record](../numerics/records/wzw-loewner-pilot-20260922.json).

The pilot answers the five questions in the proposal. The analytic claims
are internally consistent with the chosen current-algebra normalization and
the standard unitary Cardy theory. The checks support implementation accuracy;
they do not independently establish the BCFT axioms or mathematical QFT.

## Scope-critical audit points

1. **Boundary conditions really select the initial solution.** The labels
   0, 1/2, 0, 1/2, 0 admit the four spin-1/2 fields. The first adjacent pair
   must propagate in H_00=V_0. Thus the vacuum Frobenius branch is selected,
   rather than an arbitrary two-vector chosen for favorable signs. Its
   second tensor component is nonzero. The two-dimensional conformal-block
   space must not be called the full boundary Hilbert space.

2. **The factor-of-two convention matters.** With t=sigma/sqrt(2), the
   Casimir is 3/2, h=3/16, and the vacuum KZ exponent is -3/8. The Pauli
   reduction is checked in the actual 16-dimensional tensor product. The
   three square/anticommutator identities are also checked with exact
   fractions after a rational change of basis.

3. **No singular tip derivative is evaluated.** The same prime-end local
   coordinate and cutoff are used for both endpoint factors in the ratio.
   The denominator cancels the tip factor; the infinity factor is fixed by
   hydrodynamic normalization. The scalar anomaly cancellation is a statement
   about this normalized ratio. It says nothing about an unnormalized slit
   partition function. A moving driver still contributes -nu dot(u) Q.

4. **The algebraic blocks are independently controlled.** Eliminating one
   KZ component gives the scalar equation displayed in the note. Its two
   algebraic solutions reproduce the prescribed Frobenius exponents and
   coefficients. Numerical controls compare the formulas with a series
   construction and with differential evolution, including both columns.
   This avoids checking only a single specially chosen state.

5. **The positive balance is stated in its actual pairing.** For real
   boundary positions Q is Hermitian in the constant spin-tensor metric,
   which proves the constant-driver balance analytically. The CS channel
   metric is instead diag(1,4/3) in the raw Frobenius normalization, or
   the identity after the explicit channel rescaling. Fusion preserves it.
   In evaluated coordinates it varies with the marked points and conformal
   factors. CS norm preservation and fixed-tensor norm decay are compatible;
   neither gives arithmetic contraction.

6. **The moving-driver counterexample uses the physical selected block.**
   For u=4t at x=1,y=2, its initial squared-norm derivative is positive,
   approximately 0.4363884954. This is stronger than a counterexample using
   an arbitrary channel superposition. The later numerical norm falls
   below its initial value by capacity 0.2; the note states this to avoid
   suggesting monotone growth. The completing-square normalization is
   identified as additional, not silently inserted into the observable.

7. **Raw smearing cannot supply the desired initial identity.** On a compact
   positive boundary interval away from the tip, the only diagonal divergence
   is at most |x-y|^(-3/8). Its square is integrable. Dominated convergence
   gives a Hilbert--Schmidt initial limit, so this particular kernel cannot
   have the identity initial condition on L2. This conclusion uses both
   compactness and convergence to the explicit compact initial operator;
   compact operators alone could otherwise converge strongly to identity
   in a different singular limiting regime.

## Source support and limitations

The source audit used the actual primary texts:

* [Alekseev--Bytsko--Izyurov](https://arxiv.org/html/1012.3113): normalized
  slit correlators, weight normalization, Ward/KZ equations, and the
  spin-1/2 algebra. Their stochastic martingale theorem is not imported as
  a deterministic contraction theorem.
* [Cardy](https://arxiv.org/html/hep-th/0411189) and
  [Behrend--Pearce--Petkova--Zuber](https://arxiv.org/html/hep-th/9908036):
  boundary sectors, current gluing, and fusion selection. These are the
  assumed established BCFT framework, not new constructions in this note.
* [Alekseev--Barmaz--Mnev](https://arxiv.org/html/1212.6256): Wilson endpoint
  state spaces as conformal blocks. This does not turn the slit into a bulk
  Wilson line or identify a boundary affine module with L2 of an interval.

The explicit level-2 algebraic blocks, fusion matrix in the stated gauge,
deterministic square reduction, and compactness argument are derived in the
note. No literature novelty claim is made for these consequences.

The next substantive uncertainty is the full boundary-state sewing operator
and its physical reflected pairing. The pilot does not compute that operator,
prove its boundedness, or construct arbitrary spatial boundary inputs. This
is the proposed next calculation, not an unfinished item hidden inside the
five finite pilot deliverables.

All 72 recorded checks passed: seven exact rational checks and 65 floating
controls. The largest floating equality residual was below 6.7e-14. Independent
specialist review should focus on the physical normalization/local-coordinate
choice and the passage from these primary amplitudes to full sewing.
