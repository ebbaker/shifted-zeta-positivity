# E04 additional-agent review of the E01–E03 arithmetic proofs

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol / ultra** by explicit
tool selection. The reviewer is distinct from the arithmetic proof authors,
shares their source inputs and model selection, and previously wrote
[B02's geometry comparison][geometry]. This is an internal additional-agent
review. The inherited HDA theorem retains its original same-model
assessment level. No specialist assessment or fresh field computation
was carried out. [Result index][results], [avoid index][avoid].

## E01 outer comparison

Checked [frozen E01 r1][e01packet] directly against [Note06][e01] and
verified all 17 manifest entries by byte length and SHA-256. The arithmetic
check concerns the saved proofs and consumption of their cited inputs.
The [exact replay record][checks] contains the finite algebra checks.

In [HDA Note04][hda], CS4–6 give the cosine, correction and two-carrier
remainder on fixed charts, with \(x^{-3/4}\) at nonnegative time and
\(0\le\lambda L_x\le8\). Note06 pays the fixed (1,9) chart onsets,
CS18's window, enlarged zero-time charts, Gaussian exterior and cutoff
joins. It evaluates the chart recentered at each real coordinate \(x\)
with its designated integer cutoff \(N_x\), at the time fixed by the
center \(X\). Cauchy's formula uses the exact analytic quotient
independently of those chart cutoffs. The sign reversal relative to
the HDA source's time-zero argument is covered by the functional
equation of the completed \(\xi\). [HDA formulation][hda03],
[HDA assessment][hreview], [parent formula][parent].

The cosine splits with the \(C_-\) arm multiplying
\(e^{i\nu\log n}\). It gives the exact argument
\(s_\lambda=(1-iz)/2+\lambda L(z)/4-i\pi\lambda/8\).
On the full closed rectangle, \(\Re s_\lambda\ge37/32>9/8\)
and the ordinary Euler product gives \(|1/\zeta(s_\lambda)|\le9\).
The finite heat-removal majorant \(n^{-33/32}(\log n)^2\)
is summable. The ordinary tail costs \(O(x^{-1/16})\).
The complete reflected sum has powers
\(\alpha=(y-1)/2-c_x/8\in[-13/64,-3/64]\) and, after the
carrier, exponent \((1-y)/4-c_x/16\le-3/128\).
The correction factor is bounded at every fractional cutoff after
removing the simple denominator zeros of \(\mathcal C\). It costs
\(O(x^{-(1+y)/4})\) together with the normalized carrier. The
remainder includes both carrier moduli and the inherited full source
tails. Note06's two explicit final gates each pay at most \(1/288\)
before the factor nine. [Ordinary zeta series and Euler product][zeta].

The radius-\(1/32\) derivative disks are inside the region of the
value estimate. The resulting \(M=2\), \(m=1/2\), and \(h=1/8\)
cover the closed target with an observation buffer \(1/16\).
The full Green bound has all four edges and exact harmonic
normalization. Its strict margin is at least \(\log(285/272)\).
Direct nonvanishing with the same uniform field bound covers the
entire rectangle. Polymath Theorem 3.2 at initial width 1 supplies
the exterior of the old enclosure at each \(\lambda_X\). This proves
the frozen E01 comparison and one-step gain from the cited inputs.
[Polymath §3][poly].

## Exponent-pair source for E02 and E03

Checked Montgomery–Vaughan, author-hosted Chapter 16, Definitions
16.1–16.2, equations (16.55)–(16.58), Theorems 16.23 and 16.25, and
Table 16.1. With derivative parameter \(\theta=1\), their comparison
phase is a positive multiple of \(\log u\). Our exact positive phase is
\(\tau\log u/(2\pi)\) in the \(e(f)=e^{2\pi i f}\) convention.
It satisfies every derivative tolerance with zero difference. The
negative sign follows by conjugation. Their scale \(M\) may be real,
so clipped blocks and their partial sums on arbitrary subintervals
of \([M,2M]\) give \(O(x^kM^{l-k}+M/x)\) for \(\tau\asymp x\),
including the inverse derivative term. Half-open endpoints can be
represented by a closed interval with the same integer set.
The A/B rules start with \(AB(0,1)=(1/6,2/3)\). They give
\(k_j=1/(2^{j+3}-2)\), \(l_j=1-(j+2)k_j\) after \(j\) more A steps.
The constants depend on the fixed pair and the fixed derivative
parameter. [Montgomery–Vaughan, Chapter 16][mv].

## E02 signed finite tails

Checked [frozen E02 r1][e02packet] against [Note09][e02].
Expansion of the two cosine arms gives frequencies
\[
 \tau_D=x/2+\pi\lambda/8-\lambda\arg z/4,\qquad
 \tau_R=x/2+\pi\lambda/8+\lambda\arg z/4.
\]
These are the frequencies in the saved proof. The real logarithmic
drift \(\Re L(z)-L_x\ge0\) enters the two weights with the same
helpful sign and is also kept in the exact zeta argument. Both
frequencies are comparable to \(x\). The proof independently pays
\(\Re s\ge124997/120000>33/32\) and reciprocal floor factor 33.

The finite prefix uses \(K=\lfloor\exp(L_x/8)\rfloor\), the
summable heat-removal majorant \(n^{-129/128}(\log n)^2\),
and the ordinary tail after \(K\). The tail partitions at exact
real scales and uses left-open, right-closed clipped dyads.
An integer at a junction is counted once, the terminal integer
is included, and \(N_x\) remains the actual provider cutoff.
Singletons and the included \(n=1\) of the reflected arm are paid.
Direct log differentiation gives the uniform amplitude bound
\(|ua'(u)/a(u)|\le4\), yielding the saved Abel variation constant.
There are \(O(1+L_x)\) blocks.

The rational endpoint replay confirms all four primary dominant
powers stay below \(-1/4096\) at the worst allowed real-clock drift.
The reflected primary cutoff power is
\(1/6-y/4-c_x/16\); at \((y,c_x)=(7/12,1)\) it equals \(-1/24\).
The other endpoint is \(1/6-y/2\). Convexity pays the full reflected
population with primary exponent at most \(-1/32\).
The inverse terms of both arms cost \(O(x^{-1/2})\) per block.
The correction and two-carrier remainder pay faster fixed powers
by the same HDA bounds as E01, with all inherited onsets retained.
This gives the specified uniform bound with finite constants plus
the exact logarithmic block count. The final onset gates yield
\(|F-1|\le1/64\). With the initial strip and conjugation, direct
nonvanishing gives \(|y|<7/12\) for zeros of \(H_{\lambda_X}\) at
\(\Re z=X\), for every real \(X\) beyond the fixed onset. No
mathematical correction requested.

## E03 envelope and canonical transfer

Checked [frozen E03 r1][e03packet] against [Note10][e03].
The adjacent crossings of \(k_j-d_j v\) have the stated order.
Chaining the adjacent inequalities identifies the minimizing pairs
at \(v_*=32/161\) as \(j=3,4\), where the envelope is
\(q_*=351/10304\). For \(v\le1/8\), the limit as \(j\to\infty\)
bounds the envelope above by \(v/4\le1/32<q_*\). On the remaining
interval, the six convex functions used in the proof have both
endpoints at or below \(q_*\); the [exact replay][checks] checks
each comparison. Thus the full envelope maximum equals \(q_*\).

The canonical proof uses only the six finite pairs. The exact phases,
dyadic endpoints, and Abel and secondary costs are covered by the
same logarithmic-sum estimate as E02. For \(\rho=y_0-\gamma>0\),
the dominant primary power is at most \(-\rho/16\) at \(c_x=1\),
and the clock gate loses at most \(\rho/256\). The power
\(\min(\rho/32,1/4096)\) is strictly paid. The Euler-product floor
and finite-head majorant survive the full \(10^{-4}\) drift.
The reflected primary powers still satisfy the same \(-1/32\)
bound, with the whole cutoff population handled and inverse term
\(O(x^{-1/2})\) per block. The ordinary tail, correction and complete
provider remainder retain their faster powers. The constants can
be fixed on the full closed parameter range starting at \(\gamma\);
the power and its finite onset for nonvanishing depend on the
strictly positive \(\rho\). In particular \(y_0=4/7\) has
\(\rho=17/5152\) and allowed power \(17/164864\).
The resulting strict width \(y_0\) holds for every sufficiently
large real \(X\) at the prescribed \(\lambda_X\).
No mathematical correction requested.

At \(x=X\), \(c_x=1\) exactly. At \(y_0\le\gamma\) with
\(y_0>1/2\), the summable head bound ends below \(v_*=32/161\).
The minimum displayed dominant primary power at \(v_*\) is
nonnegative. Moving the start of its clipped dyad by
\(O(1/L_X)\) in scale changes the envelope by at most
\(O(1/L_X)\), by a uniform derivative bound over the chain.
The additional real-log correction there is
\(e^{-\lambda(\Re L(z)-L_X)\log M/4}=e^{O(X^{-2})}\) and does
not give a fixed power. This verifies the stop for this
particular summable-head and separate A-chain strict-power
allowance. Other pairs, logarithmic or cross-block savings and
actual endpoint nonvanishing remain unassessed.

## Disposition and quantifiers

Accept the three saved proofs within their respective fixed contracts
and inherited input level. The collision screens identify unchanged
ordinary coefficients for Euler-factor and endpoint controls, complete
square coefficients with reflection for weighted-square, finite-tail
and finite-prime controls, canonical arithmetic for reflected and
primitive-compatible controls, the full source/profile for atomic and
finite-profile controls, and the actual cosine equation for
variable-readout controls. Arbitrary phases fail the common physical
logarithmic phase. A control with a zero in the comparison domain
would fail the uniform error test with a nonzero carrier; a disjoint
domain may pass. [Collision controls12][controls], [scope07][scope].

The comparison bounds are uniform over every real high center in
their stated range with one frozen time per comparison. E01–E03
establish statements on the curve \(\lambda_X=1/L_X\). They leave
compact heights, a common-time tail, a time-zero passage, and
line-reaching iteration for separate results. The E03 endpoint
obstruction is an optimization of upper allowances. The exact
rational replay checks the finite algebra within the proofs.

[e01packet]: ../research-progress/handoffs/GNP-BB-E01-r1.md
[e02packet]: ../research-progress/handoffs/GNP-BB-E02-r1.md
[e03packet]: ../research-progress/handoffs/GNP-BB-E03-r1.md
[e01]: ../notes/06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[e02]: ../notes/09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e03]: ../notes/10_GNP_BB_E03_ENVELOPE_ENDPOINT_AND_WIDTH_20261113.md
[geometry]: ../notes/08_GNP_BB_B02_GEOMETRY_AND_OBSERVATION_20261113.md
[hda03]: ../../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[parent]: ../../manuscript/sections/10a_transition_green.tex
[checks]: ../numerics/06_GNP_BB_REVIEW_CHECKS_20261113.json
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[zeta]: https://dlmf.nist.gov/25.2
[poly]: https://arxiv.org/html/1904.12438v2#S3
