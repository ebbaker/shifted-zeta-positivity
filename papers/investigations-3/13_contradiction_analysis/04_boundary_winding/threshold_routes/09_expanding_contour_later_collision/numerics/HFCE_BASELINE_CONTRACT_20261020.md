# HFCE-01 frozen baseline and optional cap comparison contract

20 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance. This delegated audit inherits the parent
execution; model and effort are to be taken from its actual metadata,
not inferred from earlier source documents.

This contract is saved before any numerical evaluation of the selected
window. It is a bounded test, with no scan, source acquisition, adaptive
subdivision, changed window or changed scale.

## Fixed question and coverage

Test the closed rational rectangle

    B=[109999/1000000,110001/1000000] × [4005/4,2003/2].

The current inherited coverage ledger is
`papers/investigations-3/11_arithmetic_collision_rigidity/numerics/analytic_continuation/GLOBAL_ANALYTIC_CONTINUATION_LEDGER_20261018.json`.
Its finite cover ends at a=1001 on this time slab; the BW09 value
certificate covers time [99999/1000000,100001/1000000] and therefore does
not cover B. The updated exterior begins at exp(2000), not exp(6400).
No event or nonempty event set is asserted on B.

Freeze s=1/1000000 and Gstar=1000^(7/4)exp(-125*pi). The direct question
is a strictly positive uniform lower bound on

    F=(H(T,a)^2+s*Hx(T,a)^2)/Gstar^2.

First evaluate complete H,Hx enclosures on the single closed cell B,
using the exact cached finite-source dyadic midpoint derivatives,
not new source integration. Keep both coordinate-square bounds and
the available correlated bivariate polynomial bound for F; take their
maximum. All errors are paid before claiming a physical lower bound.

If these existing complete data exclude B, stop the primary new-exclusion
attempt and record that it was stopped by the direct baseline. It is
not a Gaussian gain or a later-event result.

## Frozen source and numerical contract

Use the source-pinning function in BW09
`numerics/check_bounded_first_jet_extension.py`, which binds the historical
manuscript to commit ad4783b067548a10b8bfa65de8b4a0a47b1aa924 and checks:

- ACR `high_height_consumer.py` SHA256
  e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f;
- ACR `SETUP.json` SHA256
  c5598f9dfcc9ba0601b85989703a1e945db54beaf91396258e9758a8a9f3604f;
- Note 11 source and every historical manuscript input.

The source acquisition was at 160 bits. Arithmetic replays are fixed at
192 and 256 bits and are not independent source acquisitions.
The midpoint is (21/200,1000); d=pi/8-4log(1000)/1000, retained modes
1–11, source cutoff U=2, spatial degree 24, time degree 12.
Use cached orders through 49 and the complete finite-integral derivative
majorant through 52. The majorant extends to x>=999 by its factor e^(-dx).
All temporal Taylor segments are inside [1/100,1/5].

Use the existing BW09 recomputed whole-domain physical mode/source tails
for x in [999,1002], t in [0,1/5], physical derivative orders 0 and 1.
Pay propagated quadrature radii, Taylor truncation, physical omitted
modes and retained-source tails separately. Polynomial arithmetic and
whole-parameter variation remain in the outward polynomial image.
Maximum complete added component error: 1e-6/Gstar-normalized.
The strict coordinate margin gate is 1e-6; strict F gate is 1e-12.
No new midpoint or majorant quadrature callbacks are allowed.
Whole-run budget: 300 seconds, one cell per arithmetic precision.

## Separately predeclared optional cap comparison

After the direct baseline stops or completes, a separately labeled
same-cache cost comparison may evaluate the same B at the same fixed
s, with finite Gaussian cap |y|<=L=1/10. This does not revive the
primary new-exclusion objective.

The cap has x in [1001.15,1001.6], t in [.110000,.110002]. It therefore
uses the same majorant and physical-tail domain, with no new source
acquisition. A complete cap enclosure may use one whole-cap cell
per precision, exact Gaussian mass erf(50), separate product error
payments, and the global spatial-tail payment. If interval dependency
prevents a useful answer, stop; do not subdivide or change scale.

For t<=1/5 and u>=0, positivity and e^(4u)>=1+4u+8u^2 imply

    e^(t u^2) Phi(u)
       <=20 sum_{n>=1} n^4 exp(-3 n^2) exp(-3u)
       < exp(-3u).

Indeed consecutive terms in the series have ratio at most 16 exp(-9),
and 20 exp(-3)/(1-16 exp(-9))<1. Thus global complete source moments
M0<1/3, M1<1/9. Conservative M0,M1<=1 give the normalized omitted
spatial tail

    (1+s)*Gstar^(-2)*erfc(50) < 2 exp(-1714) < 10^(-700).

The final comparison must report the actual normalized deficit interval,
the direct baseline, inherited acquisition cost, incremental costs,
all complete error payments and scope. A negative cap deficit does not
add coverage if the direct baseline already excludes B.

## Outcome and own-data refusals

The numerical wrapper must reject malformed/missing cache inputs,
source pin changes, unsupported domains, excessive errors, and a true
common zero under the strict first-jet gate. Use the exact heat polynomial
Hc=(x-1001.375)^2-2(t-.11), with its event in B, and its own zero
source errors. Do not assign theta normalization/tails to this control.
Additional Gaussian control checks belong to any later cap consumer.

No repository files or chat registrations are changed by this delegated
run; temporary records are returned to the parent for integration.
