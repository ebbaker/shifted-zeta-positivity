# Internal review of the correlated higher-height certificates

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified its actual current configuration. The reviewing
subtask inherited it and did not author or modify the numerical driver.
This is an internal implementation and mathematical review, not an external
referee report or a formal verification.

**Result:** the three final records pass independent replay and inspection.
They certify both genuine stationary signs and a direct positive physical
norm floor on the complete closed rectangle
[0,1/2] x [40,100]. There are no unresolved sign cells, norm cells, or
merged regular-branch windows. Together with the existing overlapping
height-41 result and evenness, this extends the bounded exclusion to
0<=t<=1/2, |x|<=100. The all-height sign remains open.

## Reviewed artifacts and exact replay

The driver is
[certify_correlated_source_height_extension.py](../numerics/certify_correlated_source_height_extension.py),
importing the unchanged
[certify_compensated_stationary_theta.py](../numerics/certify_compensated_stationary_theta.py).
Their SHA-256 values at review were, respectively,

```text
bd7c756815babc23b3f884e6c15c86800e7d0b9b86071360b109ec557145382e
a91a02b3605b9a2163cf5a9498f5391f181f9633bada9ec74080240f73da9fab
```

The reviewed records were regenerated independently into temporary files
using 256-bit Arb/Acb with python-flint 0.9.0, N=4, K=2, source cutoff
U=1, spatial Taylor order 16, time order 8, Gaussian order 32, eight
initial time slabs, no time bisection, and at most two spatial bisections.
All three replays returned PASS. After removing only the measured
`runtime.seconds` field, the complete parsed regenerated records were
exactly equal to the retained records. All deciding dyadic endpoints,
payments, classifications, source hashes, branches, and rational norm
floors therefore matched exactly in this environment.

Replay from the numerics directory, with python-flint available:

```sh
python3 certify_correlated_source_height_extension.py --theta-terms 4 --space-order 16 --time-order 8 --beta-order 32 --time-slabs 8 --max-time-depth 0 --max-space-depth 2 --x-left 40 --x-right 60 --output /tmp/inv21-review-height-40-60.json
python3 certify_correlated_source_height_extension.py --theta-terms 4 --space-order 16 --time-order 8 --beta-order 32 --time-slabs 8 --max-time-depth 0 --max-space-depth 2 --x-left 60 --x-right 80 --output /tmp/inv21-review-height-60-80.json
python3 certify_correlated_source_height_extension.py --theta-terms 4 --space-order 16 --time-order 8 --beta-order 32 --time-slabs 8 --max-time-depth 0 --max-space-depth 2 --x-left 80 --x-right 100 --output /tmp/inv21-review-height-80-100.json
```

The local replay used the bundled Python executable with
`PYTHONPATH=/private/tmp/shifted-zeta-research-python`; this temporary package
location is a local runtime detail, not a repository dependency path.
The records specify Python and python-flint versions for ordinary replay.

Retained-record byte hashes:

| Band | SHA-256 |
|---|---|
| [40,60] | `7e32b3f4c0ec7e26157bccb5a7248f5f7693f9dee11cfff40527f5a7e308ad66` |
| [60,80] | `c69ee97e476e44f54b75e320be4665132ab2a6aaa00ad454887bdb2155dad020` |
| [80,100] | `3d2c63e5b669843417f2324d26c4ba88de219b636c0bfe81d203c2ac25c5b6f3` |

The independent regenerated runs took approximately 44.5, 51.4, and
60.1 seconds while running concurrently. Agreement here establishes the
recorded arithmetic's replay in this environment; it is not a claim of
bit-for-bit portability across different arithmetic versions.

The independent semantic inspection is retained as
[audit_correlated_source_height_records.py](../numerics/audit_correlated_source_height_records.py),
with its [small execution record](../numerics/HIGHER_HEIGHT_RECORD_AUDIT_20261014.json).
It passes **6,682 exact-rational checks** using the Python standard library,
including the formal N=4 identity, coverage, classification, serialized
payment compatibility, branch windows, and physical norm extraction.
It binds the exact bytes of all three certificates before reading their
source bindings, checks those generating-source and imported-core hashes,
and records its own hash. An input or source mismatch fails before any
output is written. These identity checks preserve provenance; the proof
still uses the analytic bounds and the validated arithmetic replay.
Two focused negative tests, using temporary copies, confirmed that a
changed imported source and a changed certificate are both rejected while
an existing output record is preserved.

```sh
python3 audit_correlated_source_height_records.py --output /tmp/inv21-height-record-audit.json
```

## The correlated transport is legitimate

At a slab center let J_(n,k) be the validated raw-source center jets.
The new aggregate polynomial uses S_k=sum_(n=1)^N J_(n,k) in

\[
\sum_{\ell=0}^{L_t-1}\sum_{m=0}^{L_x-1}
\frac{(-\delta t)^\ell\delta x^m}{\ell!m!}
S_{k+2\ell+m}.
\]

This is exactly the finite sum of the original channel polynomials.
The reordering retains cancellation before interval multiplication by the
same parameter monomials. Every channel's positive space/time remainder
payment is still added; no payment is canceled or omitted. Center
quadrature radii remain inside the summed ball coefficients. The driver
then subtracts the same summed endpoint coefficients and complete Gaussian
observations as the original construction.

The raw source obeys heat, so the time Taylor coefficients have the correct
factor (-delta t)^ell and use derivatives k+2ell. Absolute retained-source
moments at the slab maximum time bound every remainder, because the raw
source is positive on the real integration half-line and exp(tu^2) is
monotone in t. The original integration routines still pay the entire
source tail beyond U=1. Gaussian Taylor remainders use complete half-line
moments. The affine coefficient e_n+6tb_n is evaluated on the whole time
slab after raw heat transport. Thus no homogeneous heat equation is applied
to an individual compensated channel.

The complete omitted-index norm routine accepts N=4: its required
alpha_(N+1)>=25 is satisfied. Its complete K=2 four-jet estimate is uniform
on 0<=t<=1, so all eight slabs in [0,1/2] are in its proved range. Each
cell uses epsilon_k=C_k/x_left^4, with its actual positive left endpoint.
The new aggregation changes interval dependence, not the complete source,
the tail bound, or the physical jet being enclosed.

## D/X identity and genuine stationary payments

The imported exact-control helper explicitly checks three formal channels.
Its retained-cell implementation is already general in `source.n`. For
this N=4 extension the review independently expanded the formal jet
polynomials for N=3,4,5 and both levels j=0,1. In each case it verified
coefficient by coefficient

\[
\left(\sum_n a_{n,j+1}\right)^2
-\left(\sum_n a_{n,j}\right)\left(\sum_n a_{n,j+2}\right)
=D_j+X_j.
\]

Every stored signed observation contains four diagonal terms and all six
unordered cross-index pairs. A narrow aggregate interval need not equal
the arithmetic sum of broad D and X intervals. They enclose expressions
that agree for the underlying exact channels; the aggregate evaluates
that exact expression with its common coefficients retained.

At a **genuine** stationary point h_(j+1)=0, the deciding subtraction is

\[
\epsilon_{j+1}^2+|p_j|\epsilon_{j+2}
+|p_{j+2}|\epsilon_j+\epsilon_j\epsilon_{j+2}.
\]

The epsilon_(j+1)^2 term is present. The driver does not substitute a zero
of the finite approximation for the actual stationary condition, and does
not infer a physical sign from an individual D or X sign. Every retained
stationary surplus has a strictly positive exact dyadic lower endpoint.

## Complete cover and branch decisions

Independent exact-rational inspection reconstructed the elementary time
partition and spatial cover from all 510 cells. Each of the eight closed
time slabs has a gap-free spatial partition; every parameter endpoint is
dyadic and within the requested rectangle. Closed cells cover all shared
edges, including t=0 and t=1/2. The adjacent spatial bands share their
endpoints 60 and 80, and [40,60] overlaps the previous height-41 strip.

For each excluded observation, either its genuine stationary derivative
interval excludes zero, or a strict next-derivative sign and equal strict
endpoint signs exclude a zero by monotonicity. The latter is an interval
argument uniform in time, not a sampled endpoint sign test.

Adjacent signed cells sometimes share a stationary branch. The review
independently reconstructed every maximal contiguous signed group in each
elementary time slab. Every member has the same strict next-derivative
sign, and the two outer endpoint derivative enclosures have opposite
strict signs. Therefore each merged window contains exactly one regular
stationary point at every time in its closed slab. All 128 stored windows
match this reconstruction. These are time-slab windows, not 128 asserted
distinct global branches. A `stationary_signed_cell` classification is
resolved by such a merged window; it is not an unresolved sign.

| Band | Cells | j=0 excluded / signed | j=1 excluded / signed | Regular time-slab windows |
|---|---:|---:|---:|---:|
| [40,60] | 160 | 143 / 17 | 144 / 16 | 32 |
| [60,80] | 170 | 146 / 24 | 145 / 25 | 48 |
| [80,100] | 180 | 154 / 26 | 154 / 26 | 48 |

Thus 886 of the 1,020 stationary observations exclude stationarity and
134 carry strict signed payments. None is unresolved.

## Direct physical norm floor and resulting bounded claim

For each cell the review independently computed, using the stored exact
outward dyadic genuine jets,

\[
d_{\rm cell}^2=
\operatorname{dist}(h_0\text{ interval},0)^2+
\operatorname{dist}(h_1\text{ interval},0)^2.
\]

Their minimum agrees exactly with the stored rational squared floor.
The recorded norm floor is the downward rational square root with
denominator 2^128; its square is checked against that minimum. This
uses neither a division by the norm nor an unproved lower bound.
The final driver refines a cell whenever both genuine h_0 and h_1 balls
contain zero, even if its stationary signs are already resolved. All
final cells have a positive direct norm floor.

| Band | Minimum stationary surplus j=0, rounded | Minimum stationary surplus j=1, rounded | Direct norm floor, rounded |
|---|---:|---:|---:|
| [40,60] | 6.567419687291166e-16 | 3.130676045712124e-17 | 2.3585055433547174e-9 |
| [60,80] | 9.08924753734521e-25 | 3.0504940997576843e-25 | 2.6771402990640046e-12 |
| [80,100] | 1.8018473510451535e-30 | 2.151418941997313e-32 | 2.618031078374030e-16 |

These decimals describe the record; all decisions use exact endpoints.
The final exact rational norm floor is

\[
q=\frac{22271745300542300149807}
{85070591730234615865843651857942052864}
>\frac1{4\cdot10^{15}}.
\]

The minimizing cell is [1/16,1/8] x [96,97]. Combining the three bands
with Note 9's stronger norm gap and applying evenness yields the valid
convenient consequence

\[
\boxed{|F(t,x)|>\frac1{4\cdot10^{15}}
\quad(0\le t\le1/2,\ |x|\le100).}
\]

The exact stationary minima also exceed 10^(-30) at level 0 and
2*10^(-32) at level 1 on the new bands. Both strict stationary signs
hold on the complete combined strip. Any positive-threshold collision
must therefore have |x|>100. This is a bounded conclusion: the new
contour payments of Note 12 still need a uniform theta-specific signed
surplus, or a complete moving-domain coverage theorem, before they can
exclude all heights.
