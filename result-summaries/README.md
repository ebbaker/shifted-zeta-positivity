# Result summaries

15 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max.

## Purpose

This folder is the short way into what the repository has actually
established. Each file summarizes one cluster of results in a few hundred
words, states their status in the words the source files use, lists the
caveats a reader must carry, and routes to the manuscripts, notes,
certificates and reviews that hold the full statements. The files are
pointers, not sources: nothing here is proved, certified or reviewed by
being written here, and when a summary and its source disagree the source
wins.

What counts as a result for this folder is a statement that the repository
records as established within explicitly stated hypotheses: a theorem
proved in a manuscript or note, a certificate with a replayable record, an
exact identity with a check programme, or a scoped obstruction with a
proof. Negative results are included on the same footing as positive ones,
because in this project they have been at least as useful. Conjectures,
targets, "sufficient criteria" and research plans are not results and are
not listed, except where a file explains that a criterion turned out to be
equivalent to the conclusion it was meant to approach.

No result in this repository has had independent specialist human review
(the top-level [README](../README.md) says so); every review cited below is
an internal LLM review, and the summaries say whether it was by the same
model that produced the work or by a different one.

## Status vocabulary

The summaries keep the source's own status words and never upgrade them:

- *proved* (or *proved in-paper*): a written proof in the cited file, with
  the imported classical inputs named there;
- *certified*: an interval-arithmetic or exact-rational certificate with a
  record in the tree (Arb, python-flint, or the standard library) and
  outward rounding; *validated* is used by some folders for the same thing;
- *conditional*: proved from a named unproved hypothesis, which the summary
  repeats;
- *numerical* or *floating*: a computation without a certificate; it
  supports a statement and does not prove it;
- *release-stage*: the first-slab preprint only (v1.0, no DOI yet).

A summary also says what each result is reusable for, since that is why a
reader would look it up.

## Structure

One file per cluster, numbered for reading order, each with the sections
*Summary*, *Status*, *Caveats*, *Reusable for* and *Where*. Links are
relative to this folder. Cluster files:

| File | Cluster | Programs |
| --- | --- | --- |
| [01](01_first_slab_positivity.md) | First-slab positivity: Theorems A–C, the bounded shift difference, the Arb certificate | shifted-zeta |
| [02](02_finite_horizon_certificates.md) | Finite-horizon Weil certificates to \(\log 7\) and beyond; continuation algebra; certified anchors | shifted-zeta, critical-path |
| [03](03_shifted_zeta_criteria_and_strings.md) | The \(\Psi_\omega\) margin and critical-shift dichotomy, the \(\omega\)-string, defect depth | shifted-zeta |
| [04](04_positive_constructions_and_scoped_obstructions.md) | Positive gamma constructions, odd factor, Schur localization, two-channel exclusion, smooth-density obstruction | susy-positivity (earlier packages) |
| [05](05_transfer_loewner_and_fractional_dimension.md) | All-pass transfer and the no-critical-path dichotomy, even-tower splits, Loewner decomposition, far-field delay, fractional dimension | susy-positivity |
| [06](06_physical_channels_wzw_ym_and_collar.md) | SU(2)\(_2\) pilot identities, the collar theorem, YM obstructions, what the through-defect network does and does not give | susy-positivity (Wilson–Loewner) |
| [07](07_sonin_critical_boundary.md) | Sonin critical limit, return defect, finite Euler identity, single-probe equivalence, finite certificates | investigations |
| [08](08_character_channels_ccm_and_detector.md) | Character channels as the Dirichlet family, CCM finite realizations and the threshold-energy obstruction, the RH detector and the Newman pencil | investigations, misc |
| [09](09_prime_variance_exponents.md) | Fixed variance exponent \(\iff\) closed zero strip; finite quadratic bounds; descent obstructions | prime-variance-exponents |
| [10](10_quasi_rh_audits_and_amplification.md) | What the quasi-RH preprints proved versus claimed; the internal audit and Lean replay; conditional extractions; amplification superseded | quasi-rh-*, investigations-2 |
| [11](11_newman_heat_flow_reductions_and_certificates.md) | Heat-flow reductions, counter-kernels, finite Newman certificates, the corrected Riemann–Siegel interface, the Gomila audit | quasi-rh-exponent-descent, investigations-2 |
| [12](12_collision_controls_and_screening.md) | The Euler-factor controls, the weighted-square and reflected controls, reflection rigidity, and the screening they impose | investigations-2 (19, 22) |
| [13](13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) | Local heat-flow geometry at a collision, spacetime index and winding, and the proof that the observation criteria are RH-equivalent | investigations-2 (21, 22) |
| [14](14_theta_identities_and_arithmetic_bookkeeping.md) | Exact theta identities: covariant source formula, dilation and sieve algebra, two-coset reduction, Volterra recovery, path corrections | investigations-2 |
| [15](15_verification_infrastructure.md) | The reusable machinery: blueprint and ledger, check-programme conventions, certificate formats, chat recorders, hygiene checks | repository-wide |

## Maintenance

Add an entry when a result has a written proof or a replayable certificate
and at least one review in the tree; put it in the cluster it belongs to,
or open a new numbered file and a row above. Keep the source's status
words. When a result is corrected or withdrawn, edit the entry to say so
and link the erratum; do not delete it, since the record of what was
believed is part of what the folder is for. Keep every file short enough to
read in a few minutes; detail belongs in the sources. Record the model that
wrote or revised an entry, as the repository asks for notes and reviews.
The companion folder [`avoid/`](../avoid/README.md) holds the patterns these
results were won against.
