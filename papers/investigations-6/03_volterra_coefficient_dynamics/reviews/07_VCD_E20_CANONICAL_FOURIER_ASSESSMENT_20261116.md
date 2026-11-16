# VCD-E20 r1 assessment of the canonical Fourier estimates

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. Recorded assessor dispatch **gpt-6.1-sol / ultra**.
Separate backend attestation and the lead's actual model and effort are
unavailable. This separate internal assessor shares the E17–E19 dispatch
configuration and the inherited source premises. Specialist review remains
outstanding. [Shared-premise review scope][a05]

**Accepted in the stated scope.** All 11 direct [E20 pins][request] and all
15 prerequisite entries in the [E17][h17], [E18][h18] and [E19][h19]
requests matched before reconstruction. The prerequisite entries cover
seven distinct paths. This assessment used the proofs and the relevant
source passages. The work used no numerical campaign.
[Result index][results] [Coefficient cluster][cluster] [Avoid index][avoid]

| Assessed result | Disposition |
| --- | --- |
| [E17, Note16 §§1–5][n16] | Accepted. Complete canonical contour bound and exact asymptotic for the displayed optimized majorant. |
| [E18, Note17 §§1–4][n17], with [frozen addendum][r18] | Accepted. Exterior anchor scales, exact normalized identity, absolute summation boundary, and comparison of the verified E17 majorant with the pointwise margin. |
| [E19, Note18 §§1–5][n18] | Accepted. At time zero on each fixed interior line, the exact canonical source defeats the uniform reverse-triangle and fixed-affine-half-plane consumers. |
| [B05, Synthesis19 §§1–5][n19] | Accepted. The improved absolute \(B\) allowance and both comparisons have the stated scope. |

## E17. Source, contour and lattice

In [Note16][n16] §1, \(r=\pi m^2 e^{4w}\) has \(r'=4r\), so differentiation
of \(e^w(2r^2-3r)e^{-r}\) yields \(e^w(-8r^3+30r^2-15r)e^{-r}\).
Multiplying the undifferentiated summand by
\(-8\pi\sinh(4w)=-4r/m^2+4\pi e^{-4w}\) gives the remaining terms in
(1). The net cubic is \(8(1-m^{-2})r^3\), exactly zero for \(m=1\).
The quadratic and linear terms of that mode remain. The real-axis
reflection is inherited from [manuscript §2][ms]. On compact sets of
\(|\Im w|<\pi/8\), the real part of \(r\) is uniformly bounded below by
a positive multiple of \(m^2\). The polynomial times Gaussian bounds
there justify the holomorphic sum and its derivatives. The identity
theorem gives evenness of \(\Phi\), hence oddness and holomorphy of
\(g=-\Phi'-8\pi\sinh(4w)\Phi\). Strict real-axis positivity defines
the score there, and continuation of \(g\) follows from its product
formula.

For §2, \(P_m(u)>0\) for real \(u\ge0\) and \(P_m\le C r_m^3\) since
\(r_m\ge\pi\) and \(e^{-4u}\le1\). With \(a=\pi e^{4u}\) and
\(\delta=\cos(4v)>0\), the majorant for the mode sum is
\(Ca^3 e^{-\delta a}\sum_{m\ge1}m^6 e^{-\pi\delta(m^2-1)}\).
Oddness controls the left side of the rectangle with the same bound.
On its ends the Fourier factor is bounded by \(e^{v|x|+YR}\) at
\(\Re w=\pm R\). The mode bound eliminates those ends and gives integrable
majorants on the two horizontal lines. The shift in the direction of
the sign of \(x\), with either sign at \(x=0\), extracts \(e^{-v|x|}\).
The remaining \(e^{-yu}\) is bounded
on each half-line by \(e^{Y|u|}\). This yields (5) and the positive
\(A_Y(\delta)\) in (4), finite at fixed \(\delta>0\) and any finite \(Y\ge0\).

In §3, write \(h=\sqrt{\delta a}\). For \(j=1,2,3\), the scaled sum
is \(a^{-1/2}h\sum_{m\ge1}(mh)^{2j}e^{-(mh)^2}\), bounded uniformly in
\(h\) by comparison to the descending Gaussian \(C_j e^{-t^2/2}\).
The right-endpoint quadrature error is bounded by \(h\) times the
\(L^1\) norm of the derivative, so for fixed \(u\) the sum converges
to \(a^{-1/2}\) times the corresponding Gaussian moment. With the
\(\delta^{7/2}\) scaling the lower powers vanish for fixed \(u\).
The cubic \(m^{-2}\) piece also vanishes since \(m^{-2}r_m^3=a r_m^2\).
For domination in \(u\), the original \(P_m\le C r_m^3\) bound gives
\(C e^{(1+Y)u}a^{-1/2}=C\pi^{-1/2}e^{-(1-Y)u}\).
The half-line sixth moment is \((5/2)(3/2)(1/2)(\sqrt{\pi}/2)
=15\sqrt{\pi}/16\). Including \(8\) from the cubic and \(2/Z\)
from (4) gives \(15/[Z(1-Y)]\). Fatou gives divergence of
\(\delta^{7/2}A_Y(\delta)\) for fixed \(Y\ge1\). The finite bound
\(A_Y(\delta)\le A_1(\delta)\) at fixed \(\delta>0\) rules out uniform
relative convergence to (7) as \(Y\uparrow1\).

For §4, set \(t=\pi/8-v\), \(p=7/2\) and \(K_Y=15/[Z(1-Y)]\).
The small-\(t\) allowance after extracting \(e^{-\pi X/8}\) is
asymptotic to \(K_Y4^{-p}e^{Xt}t^{-p}\). It has the model optimizer
\(t=p/X\) and value \(K_Y(eX/(4p))^p\). For the lower comparison,
on \(t<t_1\) the small-\(t\) asymptotic permits a multiplicative
\(1-\epsilon\) bound. On \(t\ge t_1\) monotonicity and positivity
give \(e^{Xt_1}A_Y(1)\), which eventually dominates every fixed power
of \(X\). Thus \(4p=14\) yields (8). The choice \(v=0\) gives a
finite upper bound at fixed \(X\) as \(Y\uparrow1\), confirming
nonuniformity of (8) there. The lower asymptotic is for the infimum
of the displayed termwise majorants alone. The Fourier magnitude
receives only an upper estimate by this argument.

## E18. Normalization, exterior scale and consumer

For [Note17][n17] §§1–2, \(H_0=\xi(s)/8\) is the half-line cosine
integral, so reflection gives \(F=2H_0/Z=\xi(s)/(4Z)\) with
\(s=(1-iz)/2\). The real endpoints vanish and the derivative term
is absolutely integrable by the source tails and E06 score bound.
Integration by parts gives \(-Z^{-1}\int\Phi' e^{izu}=izF\).
The factors \(e^{4u}\) and \(e^{-4u}\) shift \(z\) by \(-4i\) and
\(+4i\), respectively, so the signed relation is
\(4\pi(F_- -F_+)+B=izF\).

The completed-zeta arguments after reflection are \(s+2\) and \(3-s\),
with real parts \((5+y)/2\) and \((5-y)/2\) and imaginary parts of
magnitude \(x/2\). The product bound
\(\zeta(2\Re w)/\zeta(\Re w)\le|\zeta(w)|\le\zeta(\Re w)\)
gives both anchors' positive exterior zeta bounds, and the other
completion factors are regular and nonzero. In Stirling's formula the
gamma height is \(T=x/4\); its power is \(\Re w/2-1/2\).
The polynomial contributes \(4T^2(1+O(T^{-2}))\). Including the
normalizing \(1/(4Z)\) and the factor \(1/2\) in \(\xi\) gives the
prefactor \(\sqrt{2\pi}\pi^{-\Re w/2}/(2Z)\) in the \(T\) convention.
The exponential is \(e^{-\pi x/8}\) and the powers are \((11\pm y)/4\).
The quotient is \(O(x^{-y/2})\), tending to zero uniformly on compact
interior \(y\) intervals. The dominance argument has no uniform
onset down to \(y=0\), where evenness and reality give
\(|F_+|=|F_-|\) for real \(x\). The reverse triangle inequality yields
\(|z||F|\ge4\pi(|F_+|-|F_-|)-|B|\), a positive pointwise lower bound
on \(|F|\) when the displayed right side is positive.

In §3 the gamma recurrence gives
\(F/F_+=2\pi(s-1)Q/[(s+2)(s+1)]\), with
\(Q=\zeta(s)/\zeta(s+2)\). Since \(iz=1-2s\), solving the signed
relation gives \(B/(4\pi F_+)=1-R-DQ\) with \(R=F_-/F_+\) and the
stated \(D\). The local Euler factor expands to
\(1+(1-p^{-2})\sum_{k\ge1}p^{-ks}\) in the product's absolute
domain. The resulting coefficients are in \([1/\zeta(2),1]\), so
there is no absolute summation of this series for \(\Re s\le1\).
The continued quotient is regular in the comparison strip. The
conditional comparison in §4 is resolved by the [frozen E18 return
addendum][r18], which pins the completed E17 return. The exponent
of the optimized allowance divided by \(\Delta\) is
\(7/2-(11+y)/4=(3-y)/4\). The historical proof's conditional wording
is consistent with its dated record and the later addendum.

## E19. Summation, actual heights and transfer

In [Note18][n18] §1, the divisor formula gives
\(A(u)=\sum_{d\le u}\mu(d)d^{-2}\lfloor u/d\rfloor\).
The floor error costs at most \(\zeta(2)\). Replacing the truncated
coefficient of \(u\) by \(\sum_d\mu(d)d^{-3}=1/\zeta(3)\)
costs at most \(u/(2\lfloor u\rfloor^2)\le2\).
For a cutoff \(M\), the \(cu\) part of the partial-summation tail
contributes \(-cM^{1-s}+csM^{1-s}/(s-1)=cM^{1-s}/(s-1)\).
With \(C(u)=A(u)-cu\), the remaining
\(-C(M)M^{-s}+s\int_M^\infty C(u)u^{-s-1}\,du\)
is at most \((\zeta(2)+2)M^{-\Re s}(1+|s|/\Re s)\) in modulus.
Local domination gives holomorphy on \(\Re s>0\), and
\(\zeta(s+2)\) is nonzero there. Identity on the absolute domain
extends (1) to \(\Re s>0,\ s\ne1\).

For §2, the fixed cutoff \(M=\lfloor T^2\rfloor\) leaves signed
frequencies \(\log(q/n)\) in the mean against \(e^{it\log q}\).
Exactly the integer \(q=n\) term, when present, is constant.
The finitely many other \(n\le2q\) cost \(O_{q,\sigma}(T^{-1})\).
The remaining terms cost \(O_\sigma(M^{1-\sigma}/T)\) since
\(|\log(q/n)|\ge\log2\). The mean absolute pole allowance is
\(O_\sigma(M^{1-\sigma}\log T/T)\) by integrating
\(((1-\sigma)^2+t^2)^{-1/2}\). The averaged remainder is
\(O_\sigma(M^{-\sigma}(1+T))\). The total error is
\(O_{q,\sigma}(T^{1-2\sigma}\log T)\), tending to zero for every
fixed \(1/2<\sigma<1\). The separate pointwise choice
\(M=\lfloor t\rfloor\) at \(t\ge2\) gives \(O_\sigma(t^{1-\sigma})\)
for the finite sum and the remainder and \(O_\sigma(t^{-\sigma})\)
for the pole term. Conjugation extends the bound to negative heights.

In §3, the positive frequency of each \(1+\cos(t\log p-\alpha)\)
has coefficient \(e^{-i\alpha}/2\). Its negative frequency has
coefficient \(e^{i\alpha}/2\). Unique factorization leaves only the
all-zero frequency in the ordinary mean, and only squarefree integer
frequencies survive the \(Q\)-weighted mean. This gives the sign and
product in (5). For \(h_p=a_p/(2p^\sigma)\),
\(\sum h_p=\infty\) by \(a_p\ge 3/4\), \(p^{-\sigma}\ge p^{-1}\)
and the elementary product bound for the harmonic sums. Also
\(\sum h_p^2<\infty\) by \(2\sigma>1\). The log expansion has summable
quadratic errors, so the real log tends to \(+\infty\) and its
lifted argument tends to \(-\infty\), with each step negative and
tending to zero. Crossing successive target angles modulo \(2\pi\)
has vanishing overshoot. At the targets \(\phi\) and \(\phi+\pi\)
this forces arbitrarily large positive and negative
\(\Re(e^{-i\phi}L_P)\).

Positivity of \(W_P\) transfers the contradiction from the means to
actual heights. An eventual projection upper bound \(H\) would bound
the limit of its \(W_P\)-weighted mean by \(H\), for each fixed
prefix. The fixed initial interval is bounded and its contribution
after division by \(T\) vanishes, while the remaining weight has
mean one. Choosing a prefix whose limiting projection exceeds
\(H\) contradicts that bound. Apply the argument to the negative
projection for the other direction. The limits use fixed \(P\), then
\(T\to\infty\), with the prefix chosen separately for each contradiction.
The conclusion supplies actual arbitrarily large heights for each
fixed projection.

For §§4–5, \(s=\sigma-ix/2\) with \(\sigma=(1+y)/2\).
Conjugation exchanges the two height directions and reverses the
projection angle. Direct subtraction gives
\(D-1=-(9s+3)/(2(s+2)(s+1))=O_y(x^{-1})\), so
\((D-1)Q=O_y(x^{-\sigma})\). Together with the anchor ratio this
gives \(B/(4\pi F_+)=1-Q(\sigma-ix/2)+o_y(1)\). The minus sign
exchanges the two projection extremes and the additive terms
preserve their unboundedness. The same estimates give \(DQ=Q+o_y(1)\).
Since \(1-|R|\to1\), the reverse-triangle denominator is eventually
positive. The quotient of \(|B|\) by that margin has infinite limsup by unboundedness
of the normalized modulus. These are individual projection and
height-tail conclusions at time zero. Effective onset, density,
joint observation matching and zero existence remain outside their
scope.

## Synthesis19, sources and controls

For [Synthesis19][n19] §3, fixed \(0<y<1\) gives \(D=O_y(1)\),
\(R=O_y(x^{-y/2})\) and \(Q=O_y(x^{1-\sigma})\) with
\(1-\sigma=(1-y)/2>0\). Thus \(U=1-R-DQ=O_y(x^{1-\sigma})\).
Rescaling by \(4\pi|F_+|\) pays the correct exponent
\((11+y)/4+(1-y)/2=(13-y)/4\). This improves the \(7/2\) absolute
power by \((1+y)/4\). The resulting relative upper allowance has
power \((1-y)/2\), so it supplies no small relative payment.
Equation (6) depends on E18 and the coarse bound in E19. The
infinite-limsup conclusion depends on the actual arithmetic means
from E19. The E17 upper envelope by itself supplies neither
conclusion. The synthesis claims no optimality or priority.

I checked [Reference03][refs] against the online passages. The
Euler product operates in \(\Re s>1\) and the completed reflection
uses the normalization in DLMF (25.4.3)–(25.4.4). The recurrence and
nonvanishing apply at the stated gamma arguments. The complex
remainder estimate in §5.11(ii) bounds the first omitted term by a
fixed sector factor for \(|\arg w|\le\pi/2\), which pays the uniform
error used with (5.11.1) and (5.11.9).
[DLMF zeta series and product](https://dlmf.nist.gov/25.2)
[DLMF reflection and completion](https://dlmf.nist.gov/25.4)
[DLMF gamma definition](https://dlmf.nist.gov/5.2#i)
[DLMF recurrence](https://dlmf.nist.gov/5.5.E1)
[DLMF Stirling](https://dlmf.nist.gov/5.11)

Riemann's translated pp. 1–4 support the product, reflection and
Fourier conventions after conversion from his \(\xi(t)\) notation.
Rodgers–Tao v5 §1 (1)–(3) has the same half-line source and the
\(+iz/2\) argument, switched here by reflection. Its later theorems
are outside the proof. DLMF (25.2.8) is the ordinary zeta
partial-summation analogue. The quotient mean, prime-reciprocal
divergence and positive trigonometric weight are derived in E19.
No additional value-distribution theorem or local PDF copy is
needed for this assessment.
[Riemann, Wilkins translation](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf)
[Rodgers–Tao v5](https://arxiv.org/pdf/1801.05914v5)
[DLMF Euler summation](https://dlmf.nist.gov/25.2.E8)

The generic integration-by-parts identity can hold with a control's
own score. The E17 contour proof uses the exact canonical square sum
and full analytic reflection. Euler translates change the mode scales
and the completed Fourier multiplier. Weighted-square, finite-source
and finite-prime orbit controls change the coefficients and lose full
smooth reflection. Reflected super-Gaussian and smooth/primitive
controls lack the canonical square sum, with a polynomial-order score
on the reflected super-Gaussian. Finite atoms lack the required smooth
density, and compact triangular extensions lack strictly positive
full-line density. The RH-conditional endpoint controls change the
source and ordinary Dirichlet arithmetic. The varied-kernel control
changes the literal exponential observation, and the relaxed
finite-profile data supply no physical source and Fourier field.
[Collision catalog][catalog] [Premise comparisons][a02]

The E10/E12 compact multipliers have their own continuation test.
For \(\Psi=(1+h)\Phi\), the own-score product differs from \(g\)
by \(hg-h'\Phi\). If the correction vanished, \(h'=bh\) would force a
compactly supported solution to vanish everywhere. A nonzero correction
has compact support, hence fails analytic continuation by the identity
theorem. Finite canonical-symbol observations can still hold and
the zero locations for E10/E12 remain open. E07's inherited nonreal-zero
conclusion applies to its finite square-change class.
[E17 §5][n16] [Midpoint scope][mid] [Scoped exclusions][a07]

The E17 allowance comparison is an exclusion for the displayed
termwise absolute contour bound as a payment for the consumer.
E19 uses the complete canonical source as the witness against an
eventual uniform reverse-triangle bound and a fixed affine half-plane
on each fixed interior line. Both leave a height-dependent phase,
correlated estimates, and tests restricted to selected regions outside
the excluded class. At a zero, (4) in the synthesis would require
\(U=1-R\), equivalently \(DQ=0\) in the stated interior line domain.
Unbounded projections give no such value assertion. The estimates
are intermediate quantitative results and the reverse-triangle
condition is pointwise sufficient. The packet proves no new
RH equivalence, zero confinement, degree step or terminal condition.
[Classification][a01] [Separate bounds][a12]

## Disposition

All four claims above are accepted at their frozen versions. No
mathematical correction or correction-response check was needed.
A short quotation for the result summary comes from
[Synthesis19 §3][n19].

> The uniform-in-height reverse-triangle comparison fails for the exact canonical source itself.

[request]: ../research-progress/handoffs/VCD-E20-r1.md
[h17]: ../research-progress/handoffs/VCD-E17-r1.md
[h18]: ../research-progress/handoffs/VCD-E18-r1.md
[h19]: ../research-progress/handoffs/VCD-E19-r1.md
[r18]: ../research-progress/handoffs/VCD-E18-r1-return.md
[n16]: ../notes/16_VCD_E17_CANONICAL_REMAINDER_CONTOUR_BOUND_20261116.md
[n17]: ../notes/17_VCD_E18_EXTERIOR_ANCHOR_COMPARISON_20261116.md
[n18]: ../notes/18_VCD_E19_CANONICAL_CONSUMER_OBSTRUCTION_20261116.md
[n19]: ../notes/19_VCD_B05_CANONICAL_FOURIER_ESTIMATE_SYNTHESIS_20261116.md
[ms]: ../manuscript/main.tex
[mid]: ../notes/15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md#2-finite-canonical-score-and-midpoint-data-leave-local-freedom
[refs]: ../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
