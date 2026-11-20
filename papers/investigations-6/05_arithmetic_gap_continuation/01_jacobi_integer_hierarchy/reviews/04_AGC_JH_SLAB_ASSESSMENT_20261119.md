# E05 r3 — assessment of the matched physical-time slab

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded reviewer dispatch **gpt-6.2-sol /
ultra**. Independent serving metadata are unavailable. This separate
internal assessment shares the mathematical inputs and recorded model
dispatch of the E08 contributors.
[Assessment request](../research-progress/handoffs/AGC_JH_E05_REQUEST_R3_20261119.md),
[frozen acquisition](../research-progress/handoffs/AGC_JH_E08_REQUEST_R1_20261119.md),
[Note08](../notes/08_AGC_JH_PHYSICAL_TIME_SLAB_20261119.md).

**Disposition.** Accept the first-level interval certificate on the fixed
\(N=24\), center-36, radius-9 chart for every physical \(t\in[0,10^{-4}]\).
The signed estimate and the direct comparator each enclose a strictly
negative gap correction. The paid lower bound for \(D_F\) exceeds
\(47.43458098488\). Direct evaluation with matched inputs gives the
narrower correction enclosure. No blocking issue was found.
[Primary record](../numerics/06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json).

## Source acquisition

The normalized even measure has full-line density
\(\Phi(u)/(2H_0(0))\), and folding onto \(u\ge0\) gives
\(\Phi(u)/H_0(0)\). The complete identity is
\(H_0(z)=\xi((1+iz)/2)/8\). Thus the source and head use the same even
moments, and both all-mode tail bounds divide the half-line integral
by the same \(H_0(0)=\xi(1/2)/8\). The heat equation gives the factor
\((-T)^k(m+2k)!/(k!m!)\) when the time-zero spatial jet is indexed
by \(m+2k\). The denominator in the unnormalized heat field is
\(g(Ts)=\sum T^k\mu_{2k}s^k/k!\), with constant coefficient one.
The recurrence subtracts only \(g_jF_{k-j}\) with \(1\le j\le k\)
and gives the true normalized coefficients through the retained time
order. For the complex-time bound, the mass variation up to \(u=1\)
costs \(e^\rho-1\), and its absolute tail costs at most the full
tilted mass tail. In the numerator \(|\cos(zu)|\le\cosh(24u)\)
on \(|z-36|\le24\). Reflection supplies the untilted majorant
\(\xi(25/2)/\xi(1/2)\). The all-mode envelope and tangent bound
for \(e^{4u}\) give the recorded tail and a strict mass floor.
The time tail pays every spatial coefficient beyond time order \(K\)
using the time Cauchy majorant at each point of radius ten. The spatial
tail pays the omitted spatial coefficients in retained time orders using
both Cauchy radii. The ratios are \(1/500\) and \(10/24\).
[Source code](../numerics/e08_source.py),
[complete identity](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md).

## Moving head acquisition

Parity LDL yields the positive monic norms \(h_j\), so
\(\beta_j=h_j/h_{j-1}\). For the unnormalized even heat-tilted
measure, differentiating the monic norm gives
\(\partial_t\log h_j=\beta_{j+1}+\beta_j\), since the derivative of
the monic polynomial has lower degree and the norm of \(uP_j\)
comes from the two adjacent orthogonal degrees. The difference of
consecutive logarithmic derivatives gives the stated Volterra
equation. Its order-\(k\) recurrence in \(s=t/T\) takes the order
\(k-1\) coefficient of the product and multiplies by \(T/k\).
The triangular range \(j+k\le23+K\) retains all required
neighbors, ending at \(\beta_{23}\) in row \(K\). The highest
acquired moments have order \(2(23+K)\). Formal square roots start
from positive anchors and divide by twice that constant term.

For complex \(t\), use the time-zero orthonormal basis through degree
23. Cauchy–Schwarz bounds the Gram perturbation over \(|u|\le1\)
by \(e^\rho-1\) in operator norm. Over \(|u|\ge1\) the squared
polynomials are bounded using the characteristic polynomials of the
leading real Jacobi compressions, the row-sum upper bound \(L\)
and the positive minimum pivot. The exponent
\(\rho u^2+(9+46)u-\pi e^{4u}\) is concave for \(u\ge1\)
under the checked curvature inequality. Its tangent and the
constant from \(u^{46}\le e^{46(u-1)}\) give the implemented
tail. The full Gram perturbation bound applies to each leading block.
For a pivot the diagonal change costs \(\epsilon\), and the cross
term at most \(\epsilon^2/(1-\epsilon)\). Thus the Schur deviation
bound is \(\sigma=\epsilon/(1-\epsilon)<1\). On the real axis
the rebased pivot is the moving unnormalized monic norm divided by
its time-zero norm. Its logarithm extends along the complex disk.
The two log terms for one link give the relative edge bound
\(\exp(-\log(1-\sigma))-1=\sigma/(1-\sigma)\). Because \(L\)
bounds the row sums of the positive anchor and the complex perturbation
has symmetric absolute entries, its operator norm is bounded by
\(L\sigma/(1-\sigma)\). Duhamel with the self-adjoint time-zero
anchor pays \(|\Im z|L+|z|L\sigma/(1-\sigma)\).

The sparse path recurrence accumulates \(J(s)^me_0/m!\),
with only even powers contributing at index zero. The binomial
shift from \(z\) to \(w=z-36\) is exact in the polynomial algebra.
The omitted spatial exponential is bounded on the larger time disk
before projecting its retained time coefficients. The projection costs
at most \(1/(1-T/\rho)\), while the true field's time remainder uses
its Duhamel majorant. This accounts for both truncations. For each
field, the radius-ten analytic remainder gives the same absolute
bound for its first derivative on radius nine by a radius-one Cauchy
circle. The coefficient radii remain in ordinary interval evaluation.
[Head code](../numerics/e08_head.py).

## Common chart, correction and controls

The HDC record and the xi zero strip at time zero bound the source
count on both collar curves by two. The two real source brackets
account for both zeros, strictly inside radius eight. The verified
source walls then transport that count over the entire slab. Rouché
on both collars transfers the counts to the head. Four strict
bracket sign changes, two per field, give simple real roots in
disjoint brackets on every slice. The count and signs use no
gap-correction assumption. The centered arc expansion bounds the
fourth-order remainder on the chord inside the circle. The lower
half is covered by conjugation for real time. The positive boundary
floors and ratio extend across the annulus using \(1/F\), \(1/Y\)
and \(B/Y\). Real refinements retain uniform opposite endpoint
signs and use the real mean-value enclosure for each Newton
intersection. They preserve all roots at once as \(s\) ranges in
\([0,1]\). [Chart code](../numerics/e08_chart.py),
[HDC certificate](../../../../investigations-4/12_height_dependent_heat_contours/numerics/07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json).

The driver subtracts the joint coefficient arrays before evaluating
time or space and adds both absolute remainder bounds. For head
roots \(y_i\) with half-gap \(h\), the two divisions by \(Y_z(y_i)\)
have nonzero denominators. The contour orientation gives
\(J=-h[(B/Y_z)(y_2)-(B/Y_z)(y_1)]\). With
\(K_0=-\log(1-\eta)\), integration by parts and the collar log
give the radius \(153(K_0-\eta)+81K_0^2/4\). Here \(153=9(18-1)\)
uses the common buffer and \(81K_0^2/4\) pays the square of the
center displacement. The direct calculation uses the same numerators,
with \(F_z\) evaluated on the convex hull of each source and head tube.
It therefore bounds all intervening mean-value points. At the head
root \(B(y_i)=F(y_i)\). This gives the exact displacement
\(d_i=-B(y_i)/F_z(\xi_i)\), including zero displacement when the two
roots coincide and the slope is cleared. Algebra gives
\(D_F-D_{24}=d(h+d/4)\) with \(d=d_2-d_1\).
[Remainder proof](../notes/04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md),
[driver](../numerics/certify_e08.py).

For \(Y=w^2-1,\ F=w^2\), the collar quotient is \(1/(w^2-1)\).
The two residues of \(w/(w^2-1)\) sum to one, giving \(J=-1\)
and exact change \(-1\) while \(D_F=0\). The signed paid lower
gap is nonpositive. The target's distinct real brackets and slopes
needed for the direct method fail. The simple-head residue divisions
also lose their premise at a reference double. The exact contour and
integer trace formulation retain their counted-chart domain.
A coincident reference/target field has zero gap change and fails the
strict negative gate. For altered arithmetic controls the unchanged
ordinary xi source, reflection or exact square coefficients fail
according to the family. Shape, primitive and atomic-profile controls
lose canonical arithmetic. The altered observation loses the literal
cosine evolution, and relaxed profile measures lose the physical
integer divisor. The RH-conditional added double has altered
Dirichlet arithmetic and retains its RH hypothesis. This is a
premise screen for the fixed canonical estimate.
[Branch screen](02_AGC_JH_INTERFACE_AND_PARITY_ASSESSMENT_20261119.md#collision-premise-screen-and-comparator),
[collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[result index](../../../../../result-summaries/README.md),
[patterns index](../../../../../avoid/README.md),
[criterion classification](../../../../../avoid/01_restating_the_target.md),
[control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Reproduction and interval arithmetic

One replay to a temporary record accepted at the first frozen level,
\(K=10\), 768 bits, 144 source terms, 192 head terms and 512 sectors
per boundary circle. It matched every invariant record field,
including exact rational endpoints, all serialized constants, counts,
runtime versions and code and input hashes. The only differences were
timestamps and timings. The replay used CPython 3.10.0, python-flint
0.9.0, FLINT 3.6.0 and one thread. It reported 9.806 seconds. The
primary reported 10.193 seconds, of which about 9.53 seconds were
shared collar work. The paid signed and direct arithmetic followed
the same source/head model, chart, time root tubes and subtracted
numerators. Neither field required a separate count acquisition for
the direct comparator.
[Replay return and hashes](../research-progress/handoffs/AGC_JH_E05_RETURN_R3_20261119.md).

Both collar floors exceed \(1.43319\times10^{-5}\) and
\(\eta<1.715356\times10^{-7}\). The two analytic tail allowances
are below \(4.750\times10^{-29}\) for \(F\) and
\(8.876\times10^{-27}\) for \(Y\) on radius ten, including the same
absolute first-derivative allowances on radius nine. The numerical
Gram bound gives \(\epsilon<0.051272\), \(\sigma<0.054042\) and
\(L<0.662987\). At this level the last link is \(\beta_{33}\)
and the highest moment order is 66.

| Full-slab quantity | Outward-rounded interval | Width, approximately |
| --- | --- | ---: |
| \(J\) | \([-4.957996144,-4.957019371]\,10^{-8}\) | \(9.76772\,10^{-12}\) |
| Signed \(D_F-D_{24}\) | \([-4.958280826,-4.956734690]\,10^{-8}\) | \(1.54613\,10^{-11}\) |
| Direct \(D_F-D_{24}\) | \([-4.957996104,-4.957019318]\,10^{-8}\) | \(9.76786\,10^{-12}\) |
| Unsigned \(D_F-D_{24}\) | \([-2.624494235,2.624494235]\,10^{-5}\) | \(5.24899\,10^{-5}\) |
| \(D_F\) with signed allowance | \([47.43458098488,47.43550019748]\) | \(9.19213\,10^{-4}\) |

A separate exact-rational endpoint check used the first 48 terms
of the log series and an upper tail
\(\eta^{49}/[49(1-\eta)]\).
The resulting interval gives \(A\) approximately
\(2.8468154762680883\times10^{-12}\), with approximately
\(5.958451266227265\times10^{-13}\) for the center square.
The stored radii dominate these bounds. Exact endpoint arithmetic
reconstructed \(J\) from the signed quotients and the head half-gap,
checked the quotient boxes against the stored numerators and slopes,
and verified the strict sign of \(J+A\), signed enclosure, and
positive paid gap. The direct endpoint calculation independently
reconstructed the displacement quotients and final product from
the stored boxes. The direct enclosure lies inside the signed one,
and the unsigned enclosure straddles zero. The same arithmetic
checked the fixed endpoint results, the listed widths, and overlap
with the saved E07 correction, gap and root brackets.
[E07 anchor](../numerics/05_AGC_JH_E07_CERTIFICATE_20261119.json).

The direct correction's full-slab width is about
\(9.77\times10^{-12}\), compared with about \(2.70\times10^{-16}\)
at either fixed E08 endpoint. The comparison measures the extra
enclosure width when time is ranged and includes interval dependency.
Using the E07 time-zero reference, the direct change of the correction
at the right endpoint is in \([4.0556183,4.0558878]\,10^{-12}\).
Over the full slab, the difference from that reference lies in
\([-2.8561948,6.9116648]\,10^{-12}\). The strict endpoint difference
establishes a net increase in the correction between the two fixed times.
The full-slab interval gives neither its exact extrema nor its
monotonicity. The quantitative result is the local canonical Jacobi
correction on already covered geometry. Weighted forcing and degree
transfer require further inputs.
