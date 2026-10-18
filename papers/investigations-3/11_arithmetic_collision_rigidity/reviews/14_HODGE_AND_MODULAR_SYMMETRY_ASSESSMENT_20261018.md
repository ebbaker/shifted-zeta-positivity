# Assessment of Hodge duality for the symmetry program

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort
**max**, verified from the reviewing turn metadata. Internal LLM assessment;
the companion derivation is self-checked, without independent specialist
review.

## Conclusion

Investigation 22 is useful for organizing the proposed symmetries, especially
its covariant theta jets and oriented first-jet geometry. A bare Hodge star
does not supply an additional constraint on the collision equations. The
most concrete simplification is to normalize the covariant jets so that
source differentiation has constant coefficients and modular reflection is
diagonal. The [companion note][note] derives this basis and the exact defect
of the proposed spectral jet rotation.

This supports a limited addition to the existing research program: use the
normalized basis for source algebra, and use the rotation defect as a
diagnostic for a signed cutoff calculation. It does not justify opening
another geometric positivity construction without a specified arithmetic
estimate. The cutoff-correction experiment remains the first quantitative
candidate; the rotation formulation needs comparison against its extra
second-derivative cost.

## Sources and checked claims

The exact source hashes are in the [execution record][record], including
the two requested brainstorm notes, Investigation 22's Hodge manuscript,
the ASD and signed-correlation notes, the coupled-product note, and the
current exterior contract. The repository [summaries][summaries] and
[avoidance guide][avoid] were read, especially [collision controls][controls],
[geometric realizations][geometry], [reformulations][reformulations],
[generic lifts][lifts], and [scoped exclusions][scope].

| Claim reviewed | Disposition |
| --- | --- |
| Applying star to the existing self-dual inputs yields a new equation | No: star fixes each input. The Laguerre polarization retains one negative eigenvalue. |
| ASD curvature contributes a favorable term after physical restriction | No for tangential differentiation on the stated path and natural external product: those pullbacks are flat. Transverse identities remain available. |
| Modular inversion simplifies the covariant jets | Yes: normalized even jets have reflection signs alternating with half their order; the derivative recurrence loses its variable coefficients. This synthesizes existing identities. |
| The normalized first jet rotates exactly | Only when its oscillator defect vanishes. The leading pair has zero defect; the complete arithmetic sum has a defect to estimate. |
| One rotation speed approximates all retained arithmetic modes | Unsupported: the existing frequency formulas put cutoff modes near zero relative speed. A signed combined estimate may still be useful. |
| Positive Hodge norms or parity sectors can replace the complete signed sum | Unsupported: the Hodge pairing is mixed, the parity matrices are indefinite, and the complete source needs cancellations before positive-time integration. |

The normalized-jet inversion is classical theta modularity in the
period-one convention, checked against [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32).
The fourth-jet case was already recognized in Investigation 22 Review 16.
The sign symmetry of the leading normalized cutoff correction is directly
visible in [Polymath equation (53) and Proposition 6.3](https://arxiv.org/html/1904.12438v2#S6.SS2).
Neither source proves the new arithmetic defect estimate proposed here.

## Collision controls and failed premises

Every holomorphic control admits the same generic self-dual form
construction. Every twice differentiable real control obeys the rotation
identity on an interval with a prescribed nonzero phase derivative. Thus
those identities alone distinguish none of the controls. If an interval
contains a collision, equation (9) of the companion note forces the complex
defect integral to cancel the initial normalized jet exactly at that event;
a strict bound smaller than the initial radius cannot hold there.

| Control class | What fails in a theta-specific application |
| --- | --- |
| Finite-prime orbit controls | Complete normalized analytic modular reflection; finite prime constraints alone survive. No effective event height is supplied by that theorem. |
| Three-square and four-square controls | Full reflection and the unchanged complete theta coefficient sequence. Their certified event boxes reject the existing strict tests. |
| Reflected super-Gaussian control | The normalized theta integer-square source expansion. Reflection survives; the enclosed event rejects the strict tests. |
| Smooth shape and positive-primitive controls | The same exact theta arithmetic source data. Their analytic events are not replaced by invented numerical boxes. |
| Euler-factor controls | The unchanged level-one theta coefficient data. The replayed negative-Laguerre witness contradicts a global positive signed margin, but is not a double-event enclosure. |
| Counter-kernels and polynomial heat events | The exact theta source. Generic heat evolution and jet geometry survive; the qTa and polynomial event boxes reject the strict tests. |
| Smooth-density and two-channel constructions | The complete evaluated arithmetic observation and its signed comparison. Auxiliary positivity alone is shared. |

Full modular reflection together with the normalized square expansion
already selects theta in the stated coefficient class. That rigidity is
not an extra lower bound for its transform. Different controls fail
different premises; there is no claim that all fail reflection.

## Verification and proposed next calculation

Fresh execution passed the existing ASD metric/path and complete signed
bridge checks. The source-specific control replay rejected five event boxes
and the separate Euler witness. The additional exact polynomial check
verified the normalized ladder through even order 20, the complete source
and its first two source derivatives, their zero-mode cancellations, and
the formal rotation-defect coefficients. The derivations in the note give
the analytic identities; these finite checks are not evidence for a
global theta inequality.

For a bounded next calculation, retain the signed Riemann–Siegel correction
with its full prefactor, combine it with cutoff-neighbor terms, and compare
the resulting complete jet error against the current fixed-cutoff contract
on the same domain and at the same precision. Freeze the cutoff on a
holomorphic disk and retain all transition terms. If using the rotation
defect, pay for the second derivative and measure the complete complex
integral before taking norms. Report a strict certified improvement or a
precise failure of this particular combination. The identities alone
provide no new collision exclusion, Newman bound, or demonstrated speedup.

[note]: ../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[record]: ../numerics/HODGE_MODULAR_ROTATION_REVIEW_CHECKS_20261018.json
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[reformulations]: ../../../../avoid/01_restating_the_target.md
[lifts]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
