# Final internal audit: phase concentration and large-time theta revision

20 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance. Model gpt-6-astra (Codex), actual effort
ultra, as verified by the parent. Separate delegated same-model
analytical review; no numerical execution, independent implementation,
cross-model review or specialist review.

**Final disposition: accepted as an internally reviewed analytical
manuscript and matched unexecuted research program, within their
explicit scope. No unresolved mathematical blocker was found.**
The assembled final TeX, program and progress register were read in full.
Their installed copies match the reviewed hashes. This review does not
independently claim successful compilation or specialist review.

The initial source reviewed was BW09
`brainstorm/01_CAP_AT_INFINITY_20261020.md`, SHA256
`37b788cf0d478589617169236ded84fbb3867f3863337961981fd5181c9346b5`.
The review also checks the existing manuscript's numerical dependencies.
The exact final reviewed artifacts are:

- [manuscript/main.tex](../manuscript/main.tex), SHA256
  `da74b16f54b8bdbe702f0b9faeb95e247237777f57b86c561c2cd1f7d62d98ad`;
- [Program 03](../research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md), SHA256
  `3f8f207b8726ab5b39b43bfbaf4370cad4bc8effb84e2a0b5c613dc2c7d383e2`;
- [PSC register](../research-progress/03_ANALYTICAL_PHASE_SURPLUS_PROGRESS_20261020.md), SHA256
  `10b7254b4b7a26767fce88d496852b1fd241c251883f7da8a6bb94f39b4a43f9`.

## Finite-bound correction: resolved in the assembled manuscript

The initial endpoint-strip estimate (18) wrote
`2 arcsin(E/(L cos b))` while assuming only L>=1 and E<1.
Those premises do not imply E<L cos b, so that real arcsine need not
be defined. At the inner cuts the exact model modulus is

    r_b = sqrt(sin^2(b) + L^2 cos^2(b)) >= 1.

Use `2 arcsin(E/r_b)` under the existing E<1 premise. The looser
`2 arcsin(E/(L cos b))` is available only if the additional
E<L cos b condition is imposed. This fixes a finite interface and
does not change the large-time conclusion. The final proposition
`asym:phase-budget` uses the exact r_beta denominator, explicitly gives
the additional condition for the looser denominator, and pays root/cut
placement with the complete C1 errors. The correction is therefore
resolved in the reviewed final TeX. The installed brainstorm was also
checked: equation (18) now uses the exact modulus and records the extra
condition for the looser form. Its corrected SHA256 is
`3daf4b73ddd81245bd7f5f89621f77070ccf54f14fed005bcba590b4bfd28bef`.

## Statements checked

The root-wall identities are consistent with the inherited orientation:
cap phase `-(N+1)pi`, truncated regularized degree `-N/2`, physical
degree `-1-N/2`. They require two finite simple continued walls,
regular caps, and paid initial-event accounting. Opposite endpoint
phases forbid treating a collapsed infinity endpoint as a continuous
constant-phase cap. For the nested family with isolated events, the
integer interior count can become larger only at a finite event.
No infinity argument supplies missing global wall continuation.

The quadratic phase density, continuous phase lift, endpoint weak
limit, and all finite estimates (4)--(6) are correct. In particular
the exact physical endpoint-window mass is
`atan(V+V^2/[2(r-V)])`, and the middle mass is bounded by `2/V`.
The relative endpoint strips shrink but their useful physical widths
need not. The simple-root estimate (7) follows from the stated
relative-curvature assumption KV<1. It bounds a net argument change;
it does not assume or prove nonnegative phase density.

The atomic control has a continuous nonzero limiting cap with phase
-pi. Its complete positive-source and actual-threshold properties
therefore do not eliminate the cap. The final manuscript identifies the missing unchanged-theta-source
premise. It omits the earlier ambiguous phrase “eventual simplicity at
the threshold.” The atomic family has infinitely many simultaneous
double events at its threshold; no theta global wall system is inferred
from this control.

The large-time source factorization and two-sided bounds on b(u) are
correct. The stationary equation has a small local-minimum root and
one large local-maximum root for sufficiently large t. The asymptotic

    4L = log t + log log t - log(8pi) + o(1)

has the correct constant. The exact increment identity and curvature
`kappa=16A-2t=8tL-2t+36` are correct.

The three-region localization proof supports both the Laplace
asymptotic and convergence of every fixed absolute centered scaled
moment. In a formal proof, make the following payments explicit:

- On -delta<=v<=0, the desired domination follows once
  `t(1-exp(-4delta)) <= exp(-4delta)*kappa/4`.
- The far-left weighted j-th moment, after normalization, is bounded
  by a constant times
  `(L sqrt(kappa))^(j+1) exp(-c_delta*kappa*delta^2)`,
  which tends to zero for each fixed j.
- The right-hand Gaussian bound is global, and the local left bound
  supplies uniform integrable domination in the scaled variable.
  The bounded b(u) factor tends to one in the saddle window.

These are explicit proof details, not extra unproved hypotheses.
No explicit finite onset time or numerical uniform constant has been
certified.

The resulting Cj convergence to cos(z) on fixed real compact sets is
valid for every fixed derivative order. Uniform C0 and C1 convergence
give exactly one simple root near each of the first finitely many
cosine zeros and exclude extra roots between them. Thus fixed-index
positive-root asymptotics are justified without assuming reality of
every complex zero. This is neither a high-index-uniform theorem nor
an eventual-monotonicity theorem.

The physical jet is `F+iL F'`, not `F+iF'`. Its model is
`cos z-iL sin z`, and its interior layer at `z=kpi+w/L`
converges to `(-1)^k(1-iw)`. If convergence of the actual phase
**density** is stated, explicitly invoke the available C2 convergence:
the derivative in w of the physical jet is `F'/L+iF''`.
Jet convergence alone should not be presented as automatic derivative
convergence. The source proof does provide the needed C2 input.

The finite error bounds (14)--(17), model central phase formula, and
monotonicity condition are correct. The root/cut conditions must apply
on the lobe enlarged by both root neighborhoods. The denominator
correction above completes (18). Endpoint strips here are bounded by
cuts at the corresponding **model** root plus/minus b and the actual
root endpoints; avoid describing them as windows of exact width b
measured from the shifted actual roots.

The signed-surplus budget is correctly scoped. Endpoint decrease
at least pi-eta plus strict middle decrease greater than eta implies
a total strictly greater than pi; the even interior-root count then
forces at least 3pi. No 3pi lower bound must be produced by a crude
integral. This remains a conditional accounting rule, not a new theta
estimate. The quadratic exactly saturates its deficit budget, and
theta's fixed-label asymptotic puts the ordinary pi predominantly
in the middle rather than producing surplus.

Positive derivative-channel scaling preserves finite-contour winding
and root-endpoint phase increments through a nonvanishing homotopy.
Localization is scale-dependent. For spatially variable beta the
signed density is

    -d arg(f+i beta f')
      = [beta Q - beta' f f']/(f^2+beta^2 f'^2) dx.

Thus the displayed constant-beta density must not silently be applied
to an x-dependent scaling. Positive time-dependent scaling is harmless
for the finite homotopy, without supplying a uniform infinite limit.

## Scope and circularity safeguards for the revision

Retain the distinction among:

1. an unconditional large-positive-time source asymptotic;
2. conditional identification of the two originally selected walls with
   fixed positive indices, requiring their global finite continuation;
3. an unproved signed surplus incompatible with the ordinary half-turn.

The cosine profile is fully compatible with adjacent walls and cannot
serve as the distinguishing RH premise. No later theta event, effective
large-time onset, high-index estimate, global wall system, negative
excess winding, or threshold improvement follows from this work.
An all-real-threshold hypothesis does not by itself replace an explicit
proof that the particular walls continue finitely for every finite time.

## Removing the dyadic appendix and numerical replay dependencies

Replacing BW09 `manuscript/main.tex` and omitting its 51-row dyadic
appendix **does not break the existing numerical scripts**:

- `check_bounded_first_jet_extension.py` loads the actual 51 jets from
  ACR `numerics/high_height_consumer/SETUP.json`, checks its exact hash,
  and imports `high_height_consumer.py`.
- The cached manuscript manifest is ACR's
  `manuscript/positive_arithmetic_packets/`, verified at commit
  `ad4783b067548a10b8bfa65de8b4a0a47b1aa924`. It is not the BW09
  manuscript being rewritten.
- HFCE baseline, cap, and localized scripts use that same source-pinning
  wrapper and cache. None parses the BW09 TeX table.
- The exact polynomial contour checker is independent of the TeX table.

The canonical cache SHA256 is
`c5598f9dfcc9ba0601b85989703a1e945db54beaf91396258e9758a8a9f3604f`.
Preserve that cache, its original pins, the wrapper, and all original
receipts. Do not edit old manifests merely to make their historical
claims look current.

The pre-revision BW09 source was clean and tracked. Its last affecting
commit is `c9f2ece6a5f496b5f853724252c99ca0fca3d00a`; its SHA256 is
`ed5b8901bc35480fa83ab510ffa96987d49f0f36060301403f037af1fad5be2f`.
A concise DRAFT_HISTORY entry can point to that commit for the old
self-contained numerical consolidation. The user additionally requested
preserving the old draft for this significant revision. That explicit
request overrides the default no-snapshot convention: retain the single
exact old source at `drafts/20261020_before_phase_concentration.tex`,
with the old SHA256 above, and do not infer a recurring snapshot policy.
The assembled manuscript explicitly links that authorized preserved
source. The revised manuscript should cite the canonical cache,
source-proof notes and numerical records when mentioning bounded
certificates. Without the table it must not claim that all exact
numerical inputs remain inside the standalone manuscript.

Update the manuscript's current scope/provenance descriptions and the
current README/history links while preserving historical execution
receipts. Retiring an appendix does not retract the bounded numerical
results; it makes them accompanying results with external exact inputs.

## Final assembled-manuscript checks

The complete source normalization is correct:
`Phi=(psi''-psi)/8=(P''-P)/16`, `psi'(0)=-1/2`, and the split Mellin
identity gives `8H(0,x)=xi((1+ix)/2)`. The heat sign is consistently
`H_t=-H_xx`. The physical winding form, root-wall cancellation and
upper-cap orientation are consistent with `dt wedge dx`.

The local-index appendix was checked separately. Its heat polynomial
satisfies the stated Rodrigues formula and has m simple real roots on
the positive-time face, versus m mod 2 simple real roots on the
negative-time face. The b=2m wall bound is valid, and the arctangent
jumps give degree `-floor(m/2)`. The scaled Taylor tail exponents for
both H and Hx are correct. The target normalization has positive
determinant even when the leading coefficient is negative, so the index
sign is preserved. The scaled-boundary argument proves local isolation,
and compactness plus boundary nonvanishing gives the finite event count.
The complex scaled expansion and Rouche argument justify a nonreal pair
immediately before every multiplicity m>=2; that is the needed local
input for simplicity strictly above an all-real threshold.

The final saddle proof explicitly pays the normalized far-left moments,
and the extension from real to complex compact sets is justified by the
additional factor `exp(ZU/L)`, absorbed by the right-hand Gaussian bound.
It therefore supports locally uniform complex convergence and every
fixed derivative, while keeping growing-index uniformity unclaimed.
The physical phase-density limit explicitly invokes C2. No unproved
wall identification is inserted into the fixed-index root corollary.

The scalar opposite-lobe criterion, signed-surplus quantization,
derivative-scale distinction, denominator-loss example and control
premises are consistent. The root-endpoint interior count N and the
level-arc count N_level remain distinct. Ancillary Gaussian and localized
results retain their original targets and failed-estimator scope.
The old exact dyadic inputs are routed to preserved source and numerical
artifacts rather than falsely claimed to remain in the revised document.

The program and register agree: PSC-00 is documentation complete,
PSC-01--05 are unexecuted or gated, and PSC-06 awaits actual program
results. The first explicit saddle split is delta=1/8, but no finite
constants or onset are claimed from merely fixing that split. Fixed-index
cosine homotopy is explicitly recognized as ordinary-phase behavior,
not a way to obtain an extra half-turn. Numerical scans and uncontracted
parameter changes are not implied by the new plan.

The final documents retain the author/LLM acknowledgments and all
substantive limitations listed above. Final mathematical/content review
is complete for the exact hashes recorded here. The installed manuscript,
program and progress register match those hashes. The preserved source
at `drafts/20261020_before_phase_concentration.tex` has the exact
pre-revision hash recorded above. The parent reports successful built-in
compilation; this separate analytical review did not invoke or audit the
compiler. Final link and repository/history checks remain the parent's
delivery responsibility.

## Delivery verification by the parent

The installed manuscript has the reviewed hash above and compiled successfully
with the desktop editor's compiler. The exact previous TeX is preserved with
its original SHA256 in the user-requested drafts location. The saved brainstorm
uses the corrected endpoint-strip modulus, and the three program registers
retain distinct scopes. See the [delivery and chat integrity record](PHASE_REVISION_VERIFICATION_20261020.json)
for installed-file hashes, link checks and the verified archive snapshot.
The current reply's unsent final text cannot yet be in that snapshot; the
bounded exact-turn follow-up is arranged immediately before sending it.
