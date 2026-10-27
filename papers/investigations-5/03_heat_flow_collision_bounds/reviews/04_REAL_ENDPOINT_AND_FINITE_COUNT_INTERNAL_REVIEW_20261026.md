# Internal review: real endpoints and finite complete count

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. HCB chat0001. A separate same-model agent reviewed the analytical
arguments, fixed source script and retained-data verifier. The primary
agent integrated clarifications and records. No specialist validation or
independent revalidation of primary literature proofs is claimed.

**Assessment:** [Note06][note] passes at its explicit scope: generic
real-zero transport/count estimates and a finite, interval-arithmetic
witness **under RH**, for m=16 only. HCB-02 remains Partial. One finite
case does not acquire the frozen sequence. The retained F_N source
conversion, coefficient errors and favorable Poisson moment remain open.

## Mathematical audit

The global product remainder is correct for all real imaginary shifts:
|log(1+it)−it|≤t²/2. Summing its absolute remainders keeps every real
zero and gives the exact Gaussian remainder (1−2τQ)^(-1/2)−1.
The error from one includes **both** 1−exp(−τA²) and that remainder.
Its monotonicity justifies uniform endpoint floors from initial data.
There is no discarded Gaussian tail or source/model residual.

The Poisson corner product inequality gives the amplitude, clearance
and inverse-square bound. Its slope allowance at P≤3/8 is 3 sqrt(3)/8.
No uniform canonical corner inequality follows from the generic lemma.
The strip source error is an upper allowance, written ν≤X^(-1/4+o(1)),
and the bounded analytic log exists on the entire upper strip before
using its endpoint difference in the optional count filter.

For interior r∈[-4,4], the two-corner contribution minus 1/5 is exactly
r²(44−r²)/[5(r⁴−24r²+400)]≥0. Exterior contributions are positive.
The retained sum is below 2/5, so the complete count is at most one
under RH. Opposite endpoint signs supply one real root by the
intermediate value theorem. Thus the count is exactly one, including
multiplicity. Positive endpoint floors and forward reality preserve it
throughout the frozen time interval.

The full-wall lemma retains the exterior unit: after deflating every
interior root, log|G| is concave on the real interval, and all-real
order-one product structure makes its modulus increase with imaginary
height. This gives E/4^n on the horizontal sides and E on the vertical
sides. For n=1, E=0.2789 gives 0.069725, so the stated 0.0697 is safe.
No internal gap or root-slope premise is used.

The optional fourth-order filter and its leakage constant are correct;
its upper integral must run left to right, opposite the counterclockwise
top-edge orientation. That filter/integral did not complete in the pilot
and is not a numerical premise of the retained-data count.

## Implementation and failure audit

The [fixed protocol][protocol] was saved before source values ran. The
only source case is m=16, using python-flint 0.9.0 at 192 bits, exact xi
gamma/zeta factors, and fixed precision/tolerances/resource caps. The
normalized source formula and both logarithmic derivatives were checked,
including the factor 2 on the quadratic zeta-series coefficient. Outward
upper A/Q values and lower endpoint floors are conservative. The script
includes an elapsed-time check and an external watchdog was used.

The [original run][raw] remains **stopped** at the first nonfinite
continuous contour integral. No precision increase, source rerun or new
height was used. Its running_stage field is the last completed checkpoint;
failed_stage correctly identifies the later contour count. Both fields
and the original bytes are preserved.

The [separate verifier][verifier] makes no zeta, gamma or new source calls.
It checks the raw-record and source-script hashes, keeps stopped-run
provenance, recomputes the endpoint inequalities from outward serialized
balls and checks the two-corner population threshold and endpoint signs.
The successful [witness record][witness] supports (2)–(3). Its count is a
post hoc analytical consequence of completed data; it does not turn the
failed integration protocol into a successful one.

Conservative supported bounds are 0.8144 (left endpoint),0.2789 (right),
and 0.0697 (full canonical wall), over the entire selected time interval
under RH. The initial contour integration itself supplied no count.
The result is not an unconditional certificate, an F_N floor, a new RH
or Newman bound, or a uniform-in-m acquisition.

## Controls and next task

The generic lemmas permit all-real colliding controls; a multiple root
counts with its multiplicity, and a boundary zero defeats the endpoint
premise. This checks the mechanisms rather than rejecting named controls
without a failed premise. Altered controls do not supply the unchanged
canonical numerical source. No control certificate was rerun.

Next: prove a source-derived endpoint/corner bound for the frozen sequence,
or specify another bounded finite protocol before new source evaluations.
Keep the finite success, the stopped integral and the unproved uniform
input distinct. Source/link/size checks and archive capture are production
checks, not additional mathematical evidence.

[note]: ../notes/06_REAL_ENDPOINT_TRANSPORT_AND_FINITE_COUNT_20261026.md
[protocol]: ../notes/05_ENDPOINT_COUNT_PILOT_PROTOCOL_20261026.md
[raw]: ../numerics/FROZEN_ENDPOINT_COUNT_RECORD_20261026.json
[verifier]: ../numerics/02_verify_retained_endpoint_count_20261026.py
[witness]: ../numerics/RETAINED_ENDPOINT_COUNT_WITNESS_20261026.json
