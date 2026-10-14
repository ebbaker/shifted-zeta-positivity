# Correlated transport and a certificate through height 100

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**,
verified from this turn's local metadata. Parallel numerical development,
analytic derivation, and internal review assisted this continuation.
These are internal checks, not formal verification or specialist review.

The completed higher-height cover proves on

\[
0\le t\le1/2,\qquad40\le|x|\le100
\]

that both genuine stationary observations have strict margins:

\[
h_1=0\Longrightarrow\mathscr L_0>10^{-30},\qquad
h_2=0\Longrightarrow\mathscr L_1>2\,10^{-32}.
\tag{1}
\]

A separate direct norm enclosure gives |F|>10^(-16). Combining with
[Note 9](9_FULL_THRESHOLD_TIME_COVER_AND_HEIGHT_41_GAP_20261014.md)
and the central theorem yields

\[
\boxed{|F(t,x)|>10^{-16}\quad
       (0\le t\le1/2,\ |x|\le100).}
\tag{2}
\]

Every possible positive threshold collision therefore has |a|>100.
The arbitrary-height obligation remains open. The accompanying analytic
advance, [Note 12](12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md),
removes the fixed algebraic error ceiling by shifting the complete-source
contour. [Note 13](13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md)
locates the remaining normalized signed target in a moving small-time
region; neither note claims the missing sign has been proved.

## 1. The interval cancellation that limited the old transport

Raw retained channels are not separately Schwartz. Their endpoint tails
cancel across theta indices. Even after endpoint compensation, evaluating
each raw channel's Taylor polynomial on the same parameter intervals and
then summing loses much of this common dependence. On the probe [79,80],
the old evaluation order produced an aggregate width of order 10^(-7),
despite paid Taylor/index errors below 10^(-27) and a physical norm
of order 10^(-12). Increasing precision alone would not remove that
interval dependency.

For channel-center jets J_(n,k), use the exact identity

\[
\sum_{n=1}^N\sum_{\ell<L}\sum_{m<M}
\frac{(-\tau)^\ell\eta^m}{\ell!m!}J_{n,k+2\ell+m}
=
\sum_{\ell<L}\sum_{m<M}
\frac{(-\tau)^\ell\eta^m}{\ell!m!}
\sum_{n=1}^N J_{n,k+2\ell+m}.
\tag{3}
\]

The new [driver](../numerics/certify_correlated_source_height_extension.py)
performs the inner theta sum before evaluating each common Taylor
monomial. All center-jet ball radii and all positive per-channel
remainder bounds are retained and added. The endpoint compensation is
then subtracted with its summed coefficients and its full affine time
dependence. This changes only the interval evaluation order, not the
exact source or its physical observation.

The individual compensated channels and every diagonal/cross term are
still enclosed separately. The aggregate and the paired expression are
the same exact quadratic form. The N=4 identity follows by collecting
all ordered pairs, for any finite N; it does not assume channel signs
or discard an off-diagonal term. Every source-integration, Gaussian,
complete-index, rounding and Taylor payment from the reviewed machinery
remains present.

## 2. Three closed band records

The new run uses Python 3.12.14, python-flint 0.9.0, 256-bit arithmetic,
K=2, N=4, retained-source cutoff U=1, spatial Taylor order16, time
Taylor order8, and Gaussian order32. Eight exact dyadic time slabs
[i/16,(i+1)/16], i=0,...,7, cover [0,1/2]. Initial spatial cells have
unit width. Unresolved signs or a direct norm interval meeting zero
trigger spatial subdivision, with maximum depth2. There was no time
subdivision. All complete-index bounds remain in their proved time
range [0,1].

| Height band | Final cells | Record bytes | Direct norm lower bound, approximately |
|---|---:|---:|---:|
| [40,60] | 160 | 646967 | 2.35850e-9 |
| [60,80] | 170 | 775834 | 2.67714e-12 |
| [80,100] | 180 | 812441 | 2.61803e-16 |

The records are
[40--60](../numerics/CORRELATED_SOURCE_HEIGHT_40_60_20261014.json),
[60--80](../numerics/CORRELATED_SOURCE_HEIGHT_60_80_20261014.json), and
[80--100](../numerics/CORRELATED_SOURCE_HEIGHT_80_100_20261014.json).
Each binds the new driver and imported original source by SHA-256.
Every record stays below one MiB. They contain outward dyadic enclosures,
shared error-payment references, exact cover checks and all unresolved
lists. All three lists for signs, direct norms, and branch windows are
empty in every record.

The total is 510 new closed cells. Both spatial bands and time slabs
include their common and outer boundaries. Exact rational cover checks
verify the full spatial partition on each elementary time slab, even
where spatial subdivision differs between slabs. Merged adjacent signed
cells retain uniform next-derivative separation and strict opposite
outer endpoint signs, so roots crossing a cell boundary do not become
unreported branches.

The smallest exact recorded stationary surpluses exceed approximately
1.80184735e-30 at level0 and 2.15141894e-32 at level1. Exact Fraction
comparisons, rather than these decimal displays, prove the rounded
margins in (1). Direct derivative exclusions and strict monotone-endpoint
exclusions concern the genuine complete-source jets.

## 3. The direct norm lower bound

On every cell let I_0,I_1 be the paid genuine H,H_x enclosures. The
lower energy bound dist(0,I_0)^2+dist(0,I_1)^2 is calculated using exact
outward endpoints. The directed square-root method of Note 9 gives
an overall rational floor

\[
q=\frac{22271745300542300149807}
        {85070591730234615865843651857942052864}>10^{-16}.
\tag{4}
\]

Its square is bounded by the exact minimum cellwise energy floor.
The minimizing cell is [1/16,1/8] x [96,97]. A strictly positive first
stationary margin would already exclude a joint zero, but (4) supplies
a direct quantitative statement throughout the rectangle as well. No
quotient by an unproved norm is used. Evenness and the overlap [40,41]
with the previous certificate prove (2).

## 4. Reproduction and assessment

The [numerical guide](../numerics/CORRELATED_SOURCE_HEIGHT_README_20261014.md)
gives the exact three replay commands and the correlation proof. The
[internal review](../reviews/9_HIGHER_HEIGHT_CERTIFICATES_INTERNAL_REVIEW_20261014.md)
independently reads the source, replays the three bands, and audits
cover, every stationary/norm decision, source bindings, and the general
retained-pair identity. The retained [semantic auditor](../numerics/audit_correlated_source_height_records.py)
and its [small record](../numerics/HIGHER_HEIGHT_RECORD_AUDIT_20261014.json)
reproduce all 6682 exact checks using only the Python standard library,
with explicit source and certificate bindings. As always, the hashes identify the inputs;
complete estimates and validated arithmetic decide the mathematics.

The finite result closes no universal height limit. Its role is to
establish a larger verified region and test a cancellation-preserving
implementation. The new all-height absolute contour payments and the
remaining signed target are separate results in Notes12--13. A finite
sequence of successful bands is not a proof of a global covering family.
