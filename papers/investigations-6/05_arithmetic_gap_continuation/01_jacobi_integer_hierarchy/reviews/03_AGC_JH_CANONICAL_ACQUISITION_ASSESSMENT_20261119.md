# E05 r2 — assessment of the canonical signed contour acquisition

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded review dispatch **gpt-6.2-sol /
ultra**. Independent serving-model and effort metadata are unavailable.
The reviewer is a separate contributor from the three E07 implementers,
whose recorded dispatch is also gpt-6.2-sol / ultra. This internal
assessment shares the inherited source and remainder premises.
[E05 request](../research-progress/handoffs/AGC_JH_E05_REQUEST_R2_20261119.md),
[E07 request](../research-progress/handoffs/AGC_JH_E07_REQUEST_R1_20261119.md),
[Note07](../notes/07_AGC_JH_CANONICAL_SIGNED_CONTOUR_20261119.md).

**Disposition.** Accept the certified negative first variation for the
single time-zero cell at center 36 and degree 24. The complete signed
allowance resolves a negative gap change and gives a positive lower
bound for the target gap. Direct evaluation of the complete field with
the same source and count data gives substantially narrower intervals.

## Source, count and collar

The documented normalization is \(F(z)=\xi((1+iz)/2)/\xi(1/2)\).
The factor \(1/8\) cancels from \(H_0/H_0(0)\), and the corresponding
full-line \(Z_0\) is \(\xi(1/2)/4\). The jets use the affine argument
with slope \(i/2\). Taylor coefficient \(2k\) is multiplied by
\((-1)^k(2k)!\) to obtain the even moment. For parities \(p=0,1\),
the moment Gram entry in row \(i\), column \(j\) is
\(\mu_{2(i+j+p)}\); the positive LDL pivots in interleaved degree
order are the monic norms. Their consecutive ratios give the
\(N-1\) links, with moments through order \(2N-2\). Both jets
enclose real coefficients by symmetry.
[Complete-source identity](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md),
[field code](../numerics/e07_fields.py).

The centered degree-143 source polynomial has a radius-10 remainder
paid by the positive cosine-source bound \(F(24i)\) on radius 24.
The xi reflection evaluates this value at \(s=25/2\).
The validated matrix exponential at the real center and the successive
Taylor coefficients enclose the head. The true center exponential is
unitary and the real symmetric Jacobi matrix has operator norm at most
its maximum row sum \(L\), giving the remainder
\(e^{10L}(10L)^{144}/144!\). Unit-radius Cauchy disks pay the same
absolute first-derivative errors through radius 9. Coefficient and
arithmetic rounding stay inside the ball evaluations. The separate
coefficient-radius totals describe the cost of using coefficient
midpoints and are already included in those evaluations.

The saved HDC certificate and its replay agree on the count, wall,
anchor sums and source hashes. The \(\xi\) strip puts every possible
source zero in the outer collar disk inside the HDC rectangle.
The two strict real sign brackets then account for both zeros inside
radius 8. The chart bounds both collar circles by Taylor expansion about
each arc midpoint with a fourth-derivative bound on the chord and
reflection across the real line. Subtracting the coefficient sequences
before taking magnitudes retains the numerator cancellation, with
both tails paid. Each tested circle satisfies \(|F-Y|<|Y|\), so
Rouché transfers the count on both. The two real head brackets give
count two strictly inside radius 8 and simplicity by multiplicity.
Thus the closed collar is zero-free for both fields. The maximum
modulus principle applied to \(1/F,1/Y,(F-Y)/Y\) extends the
boundary floors and ratio to the full collar. These checks use no
gap-correction sign. The verified floors exceed \(1.43319\times10^{-5}\)
for both fields and \(\eta<1.71533\times10^{-7}\).
[HDC Note13](../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md),
[chart code](../numerics/e07_chart.py).

## Signed and direct gaps

On the positively oriented circle the minus sign of the linear
functional gives \(J=-h_Y(q_2-q_1)\), where \(h_Y=(x_2-x_1)/2\)
and \(q_i=(F-Y)(x_i)/Y'(x_i)\). Both derivative enclosures exclude
zero. The correlated Taylor numerator contains the exact \(F(x_i)\)
on each bracket since \(Y(x_i)=0\) at the root. With
\(K=-\log(1-\eta)\) and exact analytic input \(q_0=q\), the
complete signed radius is \(A=153(K-\eta)+81K^2/4\), of which
about \(5.95821\times10^{-13}\) pays the center square. The unsigned
radius is \(153K+81K^2/4\). The direct calculation forms each squared
half-gap from its complete roots and evaluates the difference as the
product of the sum and difference of the half-gaps. Both source and
reference use 120 bisections per root with the same source and head
data. [Note04](../notes/04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md),
[driver](../numerics/certify_e07.py),
[certificate](../numerics/05_AGC_JH_E07_CERTIFICATE_20261119.json).

| Quantity | Rounded value |
| --- | ---: |
| \(D_Y\) | \(47.4351010306712\) |
| \(J\) | \(-4.95771053563\times10^{-8}\) |
| \(A\) | \(2.84669940075\times10^{-12}\) |
| Direct \(D_F-D_Y\) | \(-4.95771048450\times10^{-8}\) |
| Full enclosing widths for \(D_F\), signed / unsigned / direct | \(5.69340\times10^{-12}\) / \(5.24888\times10^{-5}\) / \(1.03629\times10^{-35}\) |
| Full enclosing widths for \(D_F-D_Y\), signed / unsigned / direct | \(5.69340\times10^{-12}\) / \(5.24888\times10^{-5}\) / \(2.07258\times10^{-35}\) |

The widths are the differences of the serialized interval endpoints,
including rounding. The direct enclosures lie inside the signed ones.
The paid signed lower endpoint for \(D_F\) exceeds
\(47.43510098109\), and \(|J|>A\). A separate exact-rational check of
the same record enclosed \(D_F-D_Y-J\) between
\(5.11302218413354810658\times10^{-16}\) and
\(5.11302218413354810680\times10^{-16}\).
The signed calculation resolves the correction that the displayed
unsigned interval leaves open. Both use information available to
the direct method, whose measured widths are smaller.

Separate interval division by \(Y'(x_i)\) requires the derivative
floors and can lose conditioning near a reference merger. The exact
factor cancels the internal gap since writing
\(Y=(z-x_1)(z-x_2)U\) gives
\((x_i-c_Y)/Y'(x_i)=1/(2U(x_i))\). At a reference double the
contour residue is \(-F(c_Y)/U(c_Y)\), while the implemented
simple-root divisions lose their premise. For an included target
double the complete remainder forces \(D_Y+J-A\le0\) on any
valid chart. The family-by-family tests in Review02 still apply.
Modified arithmetic loses the literal complete xi source or its
reflection premises, changed observation loses the cosine kernel,
and the profile relaxations lose the physical integer divisor or
common heat path. The RH-conditional example retains its hypothesis.
[Review02 screen](02_AGC_JH_INTERFACE_AND_PARITY_ASSESSMENT_20261119.md#collision-premise-screen-and-comparator),
[collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md).

The replay reproduced every invariant field with the frozen first
level. The acquired result concerns one degree, circle and time, with
\(W(0,0)=1\). The inherited count and endpoint signs already prove
reality for this pair. The new information is its finite canonical
Jacobi correction. Any time or degree transfer needs its own inputs.
[Replay return](../research-progress/handoffs/AGC_JH_E05_RETURN_R2_20261119.md),
[result index](../../../../../result-summaries/README.md),
[patterns index](../../../../../avoid/README.md),
[criterion classification](../../../../../avoid/01_restating_the_target.md),
[control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
