# Correlated source transport for the higher-height certificate

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
This numerical subtask inherited that verified parent configuration.

`certify_correlated_source_height_extension.py` imports the unchanged
`certify_compensated_stationary_theta.py` quadrature, Gaussian transform,
complete omitted-index bound, genuine stationary payment, and exact controls.
The new driver keeps every channel and every error payment. It improves the
aggregate enclosure by commuting finite theta summation with the common
finite space/time Taylor polynomial before interval evaluation.

For retained center jets J_(n,k), write S_k=sum_(n=1)^N J_(n,k). The
aggregate raw polynomial is evaluated as

    sum_(ell=0)^(Lt-1) sum_(m=0)^(Lx-1)
        (-tau)^ell eta^m S_(k+2ell+m)/(ell! m!).

The raw remainder is the sum of the original positive channel payments.
The driver then subtracts the same summed affine endpoint compensation.
Finite summation commutes with this polynomial exactly. This change keeps
cancellation in the common Taylor coefficients; all theta indices beyond
N, both infinite integration half-lines, quadrature radii, time/space Taylor
remainders, Gaussian Taylor remainders, and arithmetic rounding are paid by
the same complete bounds as the original certificate. The individual D and
X enclosures can be broad; their exact correlated aggregate, evaluated from
the summed jets, decides the stationary sign.

The old separate channel transport loses this coefficient cancellation at
larger heights: an N=4 probe on [79,80], with the orders below, returned an
aggregate H interval of width about 2.18e-7 despite a first raw Taylor
payment below 2e-28. Correlated transport certifies the same whole time band
there with a positive norm floor greater than 2.97e-12. This diagnostic is
an explanation of interval dependency; the stored full-band records below
carry the deciding exact dyadic endpoints.

All three runs use t in [0,1/2], eight initial closed slabs of width 1/16,
N=4, K=2, 256-bit Arb/Acb arithmetic, source cutoff U=1, space Taylor order
16, time Taylor order 8, and Gaussian Taylor order 32. Cells whose stationary signs or direct norm floor remain unresolved
may be bisected spatially twice; no time bisection is used in these runs.
All files remain below one MiB. No external numerical archive is needed.

With python-flint available, run from this directory:

```sh
python3 certify_correlated_source_height_extension.py --output /tmp/inv21-height-40-60.json --x-left 40 --x-right 60 --max-time-depth 0 --max-space-depth 2
python3 certify_correlated_source_height_extension.py --output /tmp/inv21-height-60-80.json --x-left 60 --x-right 80 --max-time-depth 0 --max-space-depth 2
python3 certify_correlated_source_height_extension.py --output /tmp/inv21-height-80-100.json --x-left 80 --x-right 100 --max-time-depth 0 --max-space-depth 2
```

The retained execution records are `CORRELATED_SOURCE_HEIGHT_40_60_20261014.json`,
`CORRELATED_SOURCE_HEIGHT_60_80_20261014.json`, and
`CORRELATED_SOURCE_HEIGHT_80_100_20261014.json`. Each binds the generating
and imported sources by SHA-256, records exact coverage and all errors,
checks strict stationary surpluses, audits merged regular branch windows,
and extracts a rational direct norm floor without a quotient. Rounded
printed decimals describe these exact recorded results; they decide no sign.

All three runs pass, with no unresolved sign cells, direct norm cells, or
regular branch windows:

| Positive-height band | Closed cells | Record bytes | Direct norm floor (rounded) |
|---|---:|---:|---:|
| [40,60] | 160 | 646,967 | 2.3585055433547174e-9 |
| [60,80] | 170 | 775,834 | 2.6771402990640046e-12 |
| [80,100] | 180 | 812,441 | 2.61803107837403e-16 |

Thus 510 closed cells cover [0,1/2] x [40,100]. Exact rational
comparisons of the stored minima establish, throughout this rectangle,

    H_x=0   implies L_0>1/10^30,
    H_xx=0  implies L_1>2/10^32,
    sqrt(H^2+H_x^2)>1/10^16.

For the final norm floor the exact directed rational is

    q=22271745300542300149807/85070591730234615865843651857942052864.

Its minimizing cell is [1/16,1/8] x [96,97]. The computation separately
checks q^2 against the exact minimum of cellwise squared norm floors.
The minimal signed surpluses occur in the final band, approximately
1.8018473510451535e-30 and 2.151418941997313e-32. Together with the
previous height-41 strip and evenness, these results give the physical
norm floor 1/10^16 on 0<=t<=1/2 and |x|<=100.

These remain finite-height certificates. Increasing the theta cutoff and
Taylor orders, or preserving common coefficients, does not by itself provide
an all-height relative estimate or an RH conclusion.
