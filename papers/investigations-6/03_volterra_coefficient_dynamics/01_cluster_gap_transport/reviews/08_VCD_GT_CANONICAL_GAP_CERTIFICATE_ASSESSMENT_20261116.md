# VCD-GT-E05 r6 — Assessment of the fixed canonical gap certificate

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Reviewer dispatch selected
**gpt-6.1-sol / ultra**. Lead actual recorded settings and separate backend
attestation are unavailable. The reviewer did not contribute to the E09
proof or numerical implementation and also assessed the E08 oracle in r5.
This is an internal proof/code assessment and replay with shared premises
and model selection. [Assessment07][r5] ·
[Shared-premise review limits](../../../../../avoid/05_same_model_reviews_and_shared_premises.md)

**Accepted within scope after two wording clarifications.** Note14 remains
**proved in-note within the stated enclosure premises**. The completed
enclosure for the one fixed canonical Lehmer tube passes the proof,
provenance, geometry, signed-cost and quadratic-control checks. The
same-source direct endpoint lower bound is stronger and uses only the
endpoint source row given the shared certified collar and angular bounds.
The result concerns one finite signed-versus-absolute comparison.
[Enclosure][certnote] · [Synthesis][synthesis] ·
[Result index](../../../../../result-summaries/README.md) ·
[Avoid index](../../../../../avoid/README.md)

## Frozen inputs and replay

All eleven frozen file hashes matched at entry. The [request][request]
SHA-256 is `e9aeff19bbaabb934aa9dc96a210eb46bb8f54f7c89749b6cb92201a44d08f5d`.
The lead clarified only the shared-geometry cost premise in [Note16][synthesis]
and the direct-xi time-zero row in [ARCHIVES][archives]. Both replacements
were reread against the code and independently rehashed.

| Artifact | Frozen SHA-256 | Clarified SHA-256 |
| --- | --- | --- |
| Note16 | `00a40160d579bed10ebccb9e50b393aa27624a05a42e8e3096090169763d8895` | `f8076b5544687a851a86e319eb2bc2d36ef32ea772cade10fdacb4428cd81a4a` |
| ARCHIVES.md | `cece934a7049a36b31513bbdad005a373fd5c4a70b44f4397ba955fe42239a61` | `109f59ccd08e62ee1aeeefca4f759f5d9ac83d1bc8156686bd540872e9d96421` |

The source and consumer code hashes match the pinned records. The fine
archive's 192,793 stored bytes hash to
`033f83cb4a8d6bd411e4861380a78e054ab70f7c60079b98a75bd159644a078a`.
Its decompressed, canonical compact JSON hashes to
`508d0feec6655524f1927d5b2877b1171c92a5a553053b7ef428fc680eb6f816`.
The decoded grid has 33 time rows of 128 complex samples, with two
integer midpoint/radius/exponent triples per sample and all radii
nonnegative. [Source record][r1record] · [Archive guide][archives]

The replay used the specified interpreter and cache, with Python 3.10.0,
python-flint 0.9.0, FLINT 3.6.0 and 224-bit working precision. It finished
in about 0.84 seconds with zero xi calls. Every non-timing record field
matched, including the exact gate decisions and ball outputs. The
external replay record has SHA-256
`032a353aa3b98d41db5e0f946dc6c57fa673549709b4ddc6b3301e708629bf47`
and was written at `/private/tmp/vcd-gt-lehmer/E05-r6-replay.json`.
An empty temporary cache and a separate one-byte-modified copy both exited
with status 1 and a failed gate before certificate arithmetic. The
original archive's hash still matched after the tests. The loader checks
the stored hash before decompression and the payload hash before decoding.
This replay checks the arithmetic from bound inputs. It relies on the
analytical majorants and source generating code checked separately below.
[Consumer][code] · [Pinned certificate record][record]

## Source and approximation

- The source script evaluates \(s=(1+i(z+2i\sqrt t\,r))/2\) with the
  fixed gauge in the same exponential as the logarithmic gamma.
  Its factor \(s(s-1)\zeta(s)/16\) is the product of the \(1/8\)
  field normalization and the \(1/2\) completion factor. The
  positive-time lattice uses \(h/\sqrt\pi\) and \(e^{-r^2}\) through
  \(|r|=12\). The \(r=0\) values are reused from time zero, where
  direct xi carries no lattice error. At real nodes the two opposite
  shifts are conjugates. Reflection across the real axis gives the
  lower semicircle after the symmetric lattice is summed.
  [Source code][source] · [E08 oracle proof][oracle]
- The stored triples enclose the original Arb component balls. Their
  exact rational midpoints define the sample inputs to the polynomial.
  The consumer encloses their decimal reconstructions with Arb and adds
  the Euclidean norm of the recorded radii to the source error. An
  exact rational check of all 4,224 samples confirmed both reconstructed
  midpoint boxes and the upper disk radii. The maximum archived disk
  radius is less than \(1.127\cdot 10^{-54}\). The pinned source
  diagnostic's displayed binary64 midpoints and radii are separate from
  these triple data. Recomputing its fine-grid consumer from the archive
  reproduced all 33 stored \(D,K\) sample midpoints without new xi
  evaluations. Its angular and time quadrature remain diagnostic.
  [Serialization API](https://python-flint.readthedocs.io/en/latest/arb.html#flint.arb.mid_rad_10exp) ·
  [Diagnostic note][diagnostic]
- On \(|w|\le5\) and real \(r\), the reflected gamma coordinate has
  \(X\le3/2+(4/25)|r|\) and \(\big||Y|-a/4\big|\le5/4\).
  The height gauge leaves at most \(e^{5\pi/8}<8\). The Binet/Euler
  factor at \(r=0\) is at most \((27/4)7012^3\cdot3506<10^{16}\).
  Rational checks verify the finite exponential-sum lower bound for
  \(\log(3506)<409/50\) and the two strict extra exponent bounds.
  Integrating the majorant gives the stated \(M_5\), about
  \(3.072\cdot 10^{16}\). Binet's half-plane and Euler's height hypotheses
  continue to hold. The radius-five bound is for the true field.
  [Note14 §1][bounds]
- The spatial DFT's negative-angle phases and division by \(128\rho^k\)
  give coefficients in \(w^k\). Its exact-data aliases are the
  coefficients at indices \(k+128j\), \(j\ge1\). The Cauchy bound
  pays those aliases and the discarded terms \(k\ge33\). Sample
  error grows by \(\sum_{k=0}^{32}(R/\rho)^k\) with
  \(R=21/20\). The archive orders \(x_l\) increasingly, so the cosine
  block uses \(\cos((32-l)k\pi/32)\). The two half weights in the
  DCT-I, for time nodes and boundary time modes, agree with the
  primed sums in the proof. The interpolation norm is at most 64
  by the coefficient bound, and the code uses 65.
- At any fixed \(|w|\le R\), the exact field has
  \(\partial_t^{33}G=-\partial_z^{66}G\), so Cauchy pays
  \(66! M_5/(5-R)^{66}\). The monic Lobatto product in \(x\) has
  the factor \(2^{-31}\) and absolute bound \(2^{-31}\), with
  the additional \((1/20)^{33}\) in \(t\). For a complex
  interpolation error a real projection in its own direction
  verifies the usual \(33!\) divisor. The code uses all those
  factors and propagates the coefficient balls through evaluation.
  Its computed field allowance is less than \(0.03124\) on the
  whole disk and real time interval. The finite tensor polynomial
  does not use the physical heat equation.
  [Note14 §2][bounds] · [Consumer][code]

## Continuous geometry and drift

- In \(x=20t-1\), the equal time cells have half-width \(1/m\)
  at count \(m\). For the polynomial ratio \(P/w^2\) the angular
  derivative sum weights terms by \(|n-2|\) at spatial degree \(n\).
  The time derivative at a fixed node uses \(|T_k'(x)|\le k^2\),
  from \(T_k'=kU_{k-1}\) and \(|\sin(k\theta)|\le k|\sin\theta|\).
  Moving from a midpoint and angular node first in time and then
  in angle gives the sum of derivative paddings. The angular
  half-width is \(\pi/\text{arcs}\), so the cells at angle zero
  and \(\pi\) also cover their half-arcs. The field error adds
  \(E/r^2\). Conjugation of the exact field covers the reflected
  half even if the analytic interpolant were asymmetric.
- The first geometry grid, 16 time cells and 64 arcs per boundary,
  gives normalized real-part floors exceeding \(1{,}060{,}683\)
  and \(1{,}160{,}688\) on radii \(3/4\) and \(21/20\) with
  \(\sigma=+1\). The winding of \(G_t\) is two on each boundary.
  The harmonic minimum principle gives the same positive-real-part
  branch throughout the annulus, continuously on the time interval.
  Boundary modulus ceilings and this branch pay the centered log
  bounds, both smaller than \(1.737\). At the 128-node integration
  radius \(9/10\) the respective true-field ratio enclosures exclude
  the nonpositive half-plane and support interval principal logs.
- The two annular Laurent tails use \(r_-/\rho\) for negative
  powers and \(\rho/r_+\) for positive powers, both raised to
  multiples of 128. The node sums use both endpoints with weight
  one and the other upper-half nodes with weight two, valid for
  the real part by exact conjugation. Taking the real component
  of each interval sum and adding the angular tail encloses the
  true moments. The actual \(\gamma=c-a\) and
  \(D=p_2/2-\gamma^2\) intervals enter both radial bounds and the
  node denominator arithmetic. The centered log is used in the
  integrand and its tails together. The \(Q\) lower bounds use
  \((r-C_*)^2-D_*\) after verifying \(C_*<r\). Count two inside
  \(3/4\) excludes poles of the true kernel throughout the annulus;
  the separate code check excludes zero in the target-node
  denominator boxes.
- All 512 closed time cells passed. The outward tests verified
  \(|Q|>0.29708118\) and \(|Q|>0.80112371\) on the two boundaries,
  the two moment tails below \(5.014\cdot10^{-9}\) and
  \(1.048\cdot10^{-8}\), and the \(K\) tail below \(1.877\cdot10^{-8}\).
  The common true drift enclosure lies inside
  \([-0.615518848,-0.599329616]\). None of these steps requires
  ordering individual zeros or assuming they are simple or real.
  [Note14 §§3–4][bounds] · [Pinned certificate record][record]

## Exact cost and scope

The independently evaluated incoming \(D(v)\) uses the positive-time
endpoint row with lattice padding. The direct \(D(0)\) uses the time-zero
row, with archive arithmetic but no lattice padding. Both use the shared
true-field collar and annular moment tails. The direct interval
\([0.00142117117778,0.00142118228384]\) has a stronger lower endpoint
than the transported \(0.0007405546993009\). The 65 distinct time-zero
xi evaluations count the endpoint row given the shared collar and angular
bounds. The complete fine source acquisition used 196,673 calls for
33 rows. This comparison does not price an independent reacquisition
of that shared geometry. [Enclosure][certnote] · [Clarified synthesis][synthesis]

For \(k_U=-59/100\), the replay evaluates the exact constant-drift
upper cost \(\big(e^{4k_U/10}-1\big)/(2k_U)\), with negative numerator
and denominator. Its upper bound is \(0.178151971243388\).
The independently enclosed \(D(v)\) has lower endpoint above
\(0.17873684703288\). The resulting paid signed margin is above
\(0.0005848757894980\), and \(W(0)<0.789780673932803\) validates
division of the positive lower numerator by the positive upper
weight. For every later time the remaining actual cost is smaller
since its integrand is positive. The exact physical relation
\(W(t)D(t)=D(v)-2\int_t^v W(s)\,ds\) therefore gives strict
positivity throughout the interval. The pair is real and simple by
conjugation and \(D(t)>0\). The absolute cost is at least \(1/5\),
giving an upper margin less than \(-0.02126314189772\). These are
the signed and absolute margins for the same incoming gap and complete
source. Parsed ball comparisons confirmed the stated outward decimals
in both the execution note and synthesis. [Bounded execution][certnote]

The exact quadratic's ratio stays in the specified half-plane and its
pair remains counted through \(t=1/20\). Its centered-log Laurent
series gives \(K=0,\ D=2(t-1/20)\). The interval control encloses zero
at the double time, zero drift, and cost \(1/5\), with an upper signed
margin below \(-0.09993\). Its exact margin is \(-1/10\) on the whole
interval and zero when starting at the double time. The numerical
control inserts the exact degree-two spatial, degree-one time
polynomial into the geometry/contour/cost consumer. The tensor
reproduction statement is analytic and the control does not independently
retest the archived xi generation.

The control screen preserves the arithmetic, geometric and literal
evolution limits in Notes12/14. In particular positive-source controls
can share the Gaussian and local heat calculus. Their changed source
does not supply the canonical field samples used here. The sibling
OA bound on an exterior inverse-square sum still has the stated
wrong direction for survival in its class. This local certificate
uses neither that inequality nor an all-real slice. It gives no
general canonical gap inequality, new Newman bound, height-uniform
cost or global zero coverage. [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) ·
[Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) ·
[OA decision08][oa]

[request]: ../research-progress/handoffs/VCD-GT-E05-r6.md
[r5]: 07_VCD_GT_XI_ORACLE_ASSESSMENT_20261116.md
[oracle]: ../notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[diagnostic]: ../notes/13_VCD_GT_E04_LEHMER_DIAGNOSTIC_20261116.md
[bounds]: ../notes/14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md
[certnote]: ../notes/15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md
[synthesis]: ../notes/16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md
[archives]: ../ARCHIVES.md
[source]: ../numerics/vcd_gt_lehmer_diagnostic.py
[r1record]: ../numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json
[code]: ../numerics/vcd_gt_lehmer_certificate.py
[record]: ../numerics/05_VCD_GT_LEHMER_CERTIFICATE_20261116.json
[oa]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md
