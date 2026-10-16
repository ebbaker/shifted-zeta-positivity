# Continue the endpoint-matter investigation

Prepared 18 September 2026 by OpenAI GPT-6 (Codex).

**For the Claude handoff, read [CONTINUATION_20260918_CLAUDE.md](CONTINUATION_20260918_CLAUDE.md) first.** It includes the repository state, review qualifications, and next calculation.

Work in `papers/susy-positivity/investigations/wilson-lines`. Read
`ENDPOINT_MATTER_CONTINUATION_20260918.md` and
`ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md` first, then the 17 September review
and Loewner Section 4.1. The manuscript stays at 0.8; a fresh baseline snapshot
is `drafts/2026-09-18-v08-endpoint-baseline`. Do not edit historical snapshots.

Established: the even image average of the free dimension-one-half endpoint
kernel equals `n_gamma`; its difference energy gives the central archimedean
multiplier; a regularized determinant on the fixed tower `2n+1/2` gives the
whole shifted Gamma ratio. These are exact identities, not a gauge-theory
realization of the arithmetic target.

The first physical ansatz has been tested: pairwise semicircle operators are
gauge invariant, but their fixed-coupling bulk BPS equations have a common
solution only for circles sharing an endpoint. A fixed row is allowed by the
bulk equation, while the full two-variable family has no one common bulk
supercharge. Defect endpoint constraints have not been solved for the fixed
row. Pairwise semicircle transports also do not automatically factor into a
positive Gram construction.

Next: choose a common-reference or reflected-state gluing, write the actual
operator pairing, and test its leading kernel. If using supersymmetry, solve
bulk and endpoint conditions together. Alternatively vary the scalar coupling
with the contour while retaining a fixed supercharge, then check whether the
endpoint polarizations still give the required equal even weights. Do not
infer common supersymmetry from the individual BPS nature of semicircles.

Resolve the interaction correction in a common local renormalization scheme.
The logarithmic endpoint self-energy cannot be removed at every momentum by
normalizing at one scale. Do not infer an anomalous dimension from a gauge-
dependent propagator alone; the full observable might cancel the logarithm.
The continuation gives the exact effect of a weight shift if one survives.

Do not identify a divergent protected correlator transform with its naive
analytic continuation. The old zero-delay claim needs a subtraction scheme.
Do not change spatial dimension just to realize the Gamma shift: the fixed
spectral tower already does that. The conductor normalization, prime atoms,
pole/contact terms, physical determinant and contraction remain unproved.

Validation:

```sh
python3 validation/drafts.py check
python3 validation/endpoint_matter.py check --replay
```

The new 154 cases replay identically. The 1067 legacy cases pass their own
thresholds, but strict replay differs in five small floating-point error
metrics; see `numerics/records/endpoint-baseline-replay-audit.json`. Preserve
legacy records rather than replacing them. New research checks use the
separate continuation registry until manuscript integration.
