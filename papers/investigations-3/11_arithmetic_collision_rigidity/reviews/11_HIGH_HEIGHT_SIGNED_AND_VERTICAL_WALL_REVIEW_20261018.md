# Review of the high height signed and vertical wall consumers

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual effort
ultra**, verified from the current turn metadata. This review is by the
contributing assistant with parallel same-model proof and implementation
checks. It is internal review, not independent specialist review.

**Disposition:** no blocking mathematical defect found in the scoped
Notes 12–13 proof chain or complete interval contracts. The earned result
is finite noncollision on [1/100,1/5] × [-1001,1001], from the signed
box plus a complete wall and named published inputs. The global bridge
and Newman bound remain unclosed.

## Signed consumer and error checks

The finite shifted cutoff integral solves the backward heat equation with
its mode list, contour and cutoff frozen. Degree 24 in space and degree 12
in time use midpoint orders through 50 and remainder derivatives through 52.
The positive integrand factor 1+(u+d)^52 bounds every intermediate order;
its common moment includes the spectral exponential at the left edge.
The normalizer G0(1000) is a fixed positive constant. The Taylor proof,
quadrature-radius propagation and outward polynomial image pay every
whole-cell and arithmetic contribution. Physical mode/source tails are
added at final derivative orders0–2 rather than incorrectly treated as
relative field errors.

The new nonstationary mode estimate is actually consumed, with the frozen
phase gap taken at x_right=1001 and the spectral magnitude at x_left=999.
Its conditions and every retained-source tangent/concavity condition pass
with intervals. The initial whole-time strip failure is retained; the
single time-slab repair changes geometry only. Exact rational checks cover
all 40 accepted cells, the four time slabs, both spatial endpoints and every
seam. The minimum signed excess is above 8.26087e-5 G0(1000)^2, with added
component error below 4.621e-12 G0(1000).

The matched real comparator uses 768 bits and the same useful physical
contour derivative bound, transferred to its finite real integral with
high-order real-source tails. It is not forced to use an exponentially
poor absolute real propagation bound. Finite but inaccurate initial
quadrature radii fail the actual error gate. The sole tolerance repair
sets relative tolerance to zero; all rejected work and shared preprocessing
are charged. Both methods certify the same cells and their jet enclosures
intersect. The total measured ratio is about1.480, below the declared
factor-two gate. The successful real kernel alone is also competitive;
there is no general shifted speed advantage claim.

## Wall and finite propagation proof

The wall covers the exact closed rectangle t∈[0,1/5], y∈[0,1] at Re z=1000.
Its complex majorant includes e^u, and the largest time distance from the
cached centre is21/200. All seven closed cells have a real or imaginary H
coordinate with absolute lower bound greater than0.00425 G0(1000); their
three coarse split choices are retained. Every final coordinate error is
below 1.533e-11 G0(1000). Conjugacy covers negative y, including all equality
endpoints. This is a complete complex wall, not real-axis sampling.

The finite propagation lemma uses a boundary-free height-two rectangle,
a constant argument-principle zero count, conjugation uniqueness for simple
zeros and the local Hermite expansion at arbitrary multiplicity. The
weighted heat Taylor identity justifies the generic analytic-family lemma;
forward real Hermite branches and nonreal predecessors give the correct
time orientation. Closedness and first-exit reasoning handle the whole
time interval; a positive-time repeated zero, including the final endpoint,
would contradict the nonreal predecessor. Initial simplicity and an
unproved zero-velocity bound are not used. Evenness and the overlapping
signed box then extend the real first-jet exclusion to 1001 on the slab.

The primary inputs were freshly checked: [Polymath §3](https://arxiv.org/html/1904.12438v2#S3)
for the zero-strip/local splitting facts, and [Platt–Trudgian Theorem 1](https://arxiv.org/html/2004.09765v1#S1)
for initial zero reality. The normalization maps real height 1000 to zeta
height 500. The published initial verification is an imported theorem; this
round does not rerun its producer computation or infer positive-time
coverage without the additional wall.

## Replay and failure controls

[REPLAY.json](../numerics/high_height_consumer/REPLAY.json) performs fresh 256-bit midpoint integration,
recalculates all 40 signed and seven wall margins, and checks exact closed
coverage. Independent 768-bit real-source midpoint data also replay both
consumers with their own real/complex tail payments. All enclosures
intersect their saved counterparts. Ten negative controls reject changed
source hashes, foreign frozen parameters/domains, incomplete caches,
negative radii, missing signed/wall cells, absent files, equality cases
and an exact polynomial heat event. That polynomial fails the finite
lemma's initial-reality premise; no theta truncation constant is used for it.

[CONTROLS.json](../numerics/high_height_consumer/CONTROLS.json) freshly replays the source-specific collision
catalogue and separate Euler witness. The theta source/reflection contract
absent from each control is named in Note 13. No implicit event location or
unverified damping parameter is supplied. Saved-cache consumers now guard
source hashes, exact domains, frozen parameters, precision and Taylor orders
before loading data. Hashes identify artifacts; the mathematical margins
are decided by the recomputed interval comparisons.

## Reviewed identities and remaining gap

| Source or claim ledger | SHA-256 |
| --- | --- |
| `notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md` | `23c4a06536a4f105e1684eab95fcef30cc55e4df78f09d5817527762332668cd` |
| `notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md` | `e28b714a52706120af26fce67070adb83529c4446a75cb1f9bb0c46abe756229` |
| `numerics/high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json` | `e2e821a83e65bec799be04748b153b4306d396f9aa8a5c4cec5a00eed083a696` |

The ledger binds every new script and numerical record. Every source hash
and record dependency was rechecked against current bytes; the manuscript's
eight TeX sources retain their earlier build pin. All new files are below
1 MiB and all local artifact links resolve. No manuscript snapshot, Git
commit or new global bound is part of this round.

For tau=1/100, finite coverage now reaches 1001. The inherited outer theorem
still begins at exp(6400), leaving the open bridge (1001,exp(6400)). A general
signed/exterior estimate or feasible complete consumer remains the next
required input. The quantitative finite result does not close Stage 4's
global gate or justify an uncontrolled height scan.
