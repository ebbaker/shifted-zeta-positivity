# Coupled signed tail proof, acquisition and comparator review

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded **gpt-6.1-sol (Codex), effort
ultra**. Root-agent review plus delegated same-model proof/error checks;
no independent specialist review or formal proof.

**Assessment: the one-sided bounds and finite strict moment-comparator
gains are supported. The stronger direct signed-tail comparison stops a
dominance claim for this pilot. No global signed theta estimate is supplied.**

## Reviewed versions

| Object | SHA-256 |
| --- | --- |
| [Note 02](../notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md) | `c2b3046f01fbc8c902e294533132e23f7908ffff57b29e5da21b8249bd82e26d` |
| [Script](../numerics/certify_coupled_signed_tail.py) | `6e89f290464d715bf46aea7759ef9d8caedf40cb73204d1ecfbbe2cf34ab6bd3` |
| [Receipt](../numerics/COUPLED_SIGNED_TAIL_CERTIFICATE_20261022.json) | `bd79817136369f96caf6f36a2d3faf831d84ff58fa91468ffc271654596dc9ac` |

Hashes identify reviewed versions; the arithmetic, not the hashes, decides
inequalities. The receipt embeds the script hash, actual precision,
parameters and library versions. A fresh-process replay passed all
assertions and matched every non-timing receipt field. The final integration
check verified the script/review hashes, 161 local Markdown links and the
under-1-MiB home file-size limit; no broken link was found.

## Checks

1. **Known-forced sign.** `F=(H_zzz)^2-H_zz H_zzzz` is the first Laguerre
   expression for `H_zz` in the declared LP regime. The note counts no new
   theta result from its sign, and does not infer it from positivity alone.
2. **One-equation proof.** Integrating `s(s-sin s)` proves the global
   remainder with constants `1/3,1/30`. Stationarity correction `-h1/x`
   and both strict endpoint gains are correct. The exact-data width factor
   `4/5` is against the displayed same-moment cosine interval.
3. **Both-equation proof.** Differentiating `g` twice yields its positive
   integral kernel and constants `1/90,1/1680`. The `8/x²` value correction
   and `-5h1/x` correction have correct signs. The positive integral for
   `P-a` proves strict containment and factor `3/7` against the displayed
   same-moment sixth-order cosine interval. No mixed term is discarded.
4. **Source and tails.** The implemented `exp(u)` factor gives the exact
   canonical `exp(9u)`/`exp(5u)` normalization. Negative source terms remain
   in every core. The complete omitted-mode geometric sum pays `n>=8`;
   retained exterior tangents pay `u>=1`, including polynomial weights.
   All slope prerequisites are checked. Bounds on sine/cosine moduli are
   used on real-source error integrations.
5. **Actual critical point.** `S1_x=C2`; the head, complete `M2` tail and
   full `M3` wall payment prove strict monotonicity throughout the bracket.
   Opposite endpoint signs prove existence and uniqueness. The quadratic
   full-value wall allowance is valid because `H_x=0` at the actual root.
   Head-value variation has its separate linear moment payment. No zero
   table or global RH assumption is used as proof.
6. **All interval errors.** Arb's constructor retains existing radii when
   adding errors. Every rational coefficient is enclosed on the nonzero
   critical bracket. Full moment, source, head, shared-value, wall and
   quadrature errors enter outward endpoints. The script asserts strict
   inclusion for complete intervals, not just ideal fractions.
7. **Endpoint costs.** The note retains the `k e_V` allowance when `k~1/t`.
   Fixed absolute truncation accuracy does not become an `O(t)` residual;
   neither singular square-trace subtraction is deleted.

## Actual result, comparator and controls

The 320-bit run encloses a regular critical point at `t=0`, `x≈31.17141718`,
with `V<0`. The best coupled amplitude width is about `1.90544e-29`, against
`4.44602e-29` for the same-moment sixth-order cosine interval. Complete
rounding allowances make the recorded ratio slightly larger than `3/7`;
the receipt preserves this distinction.

Ten shared scalar integrals acquire the required head, root, value and
moments. One additional direct signed-tail integral gives width about
`1.26549e-61`, with a conservative complete wall allowance. An equally
informed direct evaluator can reuse the coupling identities too. No
exclusive topological benefit, overall accuracy dominance or asymptotic
cost advantage is established.

The exact heat-weighted atomic control has `C0=S1=0`, `C2=-3/5`, `C4=3/5`,
`S3=0`, `F=-9/25`. Both estimators retain its ordinary-double collision.
The [cluster-12 families](../../../../result-summaries/12_collision_controls_and_screening.md)
are screened analytically by the universal kernel inequalities; their
published witnesses are not numerically recomputed here. The note names
the changed-source, reflection or arithmetic premise each fails for this
particular canonical receipt. Generic positivity and criticality supply
no new global exclusion premise.

The proofread correction to the strongest-direct table rounding,
`1.26549e-61`, is incorporated in the reviewed note.

## Decision

CHB-07 remains active; this finite coupled acquisition subtask is complete
in its scope. Stop refining these moment envelopes as a candidate for
beating the acquired direct signed integral at this point. Additional
arithmetic control of a complete conditional signed consumer remains open.
CHB-05's full phase/flux acquisition, CHB-06, home 02's new constraint task,
ICW and all inherited exclusion gates retain their prior states.
The [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md), especially
[joint cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [known-forced tests](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md),
govern that scope.
