# Internal review: complete theta stationary signs and paired kernels

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable to the session
and not inferred. This combines root verification and separate-agent
audits. All are internal LLM checks, not independent mathematical validation.

## Verdict and scope

The written and arithmetic checks pass within their stated scope:

- A conditional high-cell physical Hx stationary set has strict S0,
  with HHxx/normalizer² < -90.3133241620. Its S1 stationary set is empty.
- A direct full-theta low-height Hxx stationary set has strict S1,
  with HxHxxx < -3.78300454912e-7. Its S0 stationary set is empty.
- The complete source identity is \(\mathscr L_j(H;x)=\widehat J_{j,t}(2x)\),
  with \(\mathscr L_j(A;x)=4\widehat J_{j,t}(2x)\) when A=2H.
- Every analytic exact triple has a punctured local neighborhood with
  L0(H)>0; the first Laguerre sign alone cannot detect it locally.
- Genuine J1,t(0.3) is negative for all 0≤t≤0.05. This does not refute
  positive definiteness. The same theta source has strictly positive
  J1 Fourier response on physical heights 8–12 throughout that time range.
- The genuine theta kernel tail asymptotics in Note 7 are non-effective;
  their constants and compact-time domination were checked separately.

Neither stationary calibration adds collision coverage: the first jets
already exclude joint zeros on their rectangles. The high calculation
assumes the imported complete holomorphic disk. No predecessor buffer at
the lower time boundaries, uniform sign, complete parameter cover or RH
conclusion is claimed.

## Physical jet and high-cell audit

The root and two separate agents checked the physical triangular normalizer
dictionary through order three. Physical stationarity is imposed on
Hx/normalizer=Q'+λQ, not Q'. The full λx and λxx channels, finite Bell
coefficients, mixed time derivatives γt, γxt, γxxt, complete spatial
transport and degree-eleven Taylor remainder are retained.

The checker regenerates the retained complete regular-cell moments from
hash-checked source. The imported Cauchy cost is carried into physical jets:
the third-jet upper cost remains 472.218960911. None of this cost is
removed by subdivision. Paid Hxx<0 and opposing endpoint slope signs give
one physical critical point per time. Its complete candidate band contains
three of eighty subcells, and interval product arithmetic gives the stated
strict S0 bound. No defect was found. Separate-agent replay reproduced the
same physical stationary band, curvature hull and product upper endpoint.

## Direct theta and kernel audits

The low-height integral uses the physical half-line H derivatives without
an extra factor two. Independent agents checked the full n≥4 geometric
source payment, Gaussian envelope and the three u>1 integral moments.
Interval rotations enclose the exact center phases; derivative-one phase
padding covers every physical x/u point in the cell. This is a complete
range integral with no quadrature remainder assumed. Endpoint Hxx signs
and uniform Hxxx>0 give exactly one genuine inflection per time.
The candidate band and strict S1 product were reproduced by a separate
outward replay.

The final checker also records the outward whole-domain expression
Hxx²-HxHxxx, whose lower endpoint is
2.43219610004493616457418814125377865295063814358534555232644e-7.
This extension uses the same paid hulls and a corrected interval square.

The kernel audit checks the absolute Jacobian two and the symmetrized
multiplier, yielding the full/half normalization above. It distinguishes
derivative-level Lj from generalized Laguerre coefficients. The negative
J1 point calculation includes the full paired theta source, its crossing
intervals and positive r>1 tail. Root and separate-agent replays passed.
Negative pointwise kernel values are not interpreted as negative Fourier
responses or failure of positive definiteness.

## Analytic limitations and literature

A separate-agent analytic audit recalculated the triple Taylor orders and
the leading term c²(3y⁴+36s²), bounded below by 3c²w⁴/8. The remainder
is O(w⁵); the stated small radius lies within the original analytic
neighborhood. The local positivity statement is therefore valid and has
no claimed uniform radius. The descending Duhamel formula subtracts
2 times the second source; its orientation does not furnish automatic
positivity propagation.

The theta saddle constants π³/32 and 3π²/1024 and ratio
3 exp(-4s)/(32π) were recalculated. Compact-time inner Gaussian domination
and negligible double-exponential outer tail support the non-effective
asymptotics. An optional clarity improvement was incorporated: Note 7 now
prints the sharper intermediate theta envelope used for the outer region.

The primary [Csordas PDF](https://arxiv.org/pdf/1309.0055v2), printed
Theorem 3.7 and Open Problems 4.7 and 4.11, was checked. The canonical
autocorrelation approach is credited as classical. Its hypotheses are not
silently imported, and its historical questions are not presented as a
verified current literature status or a low-order sign theorem.

## Root replay and source identity

Final-source root replays pass. After the stationary checkers were made
explicit-record-only, the complete arithmetic endpoints and subcells
matched their previous audited records. Runtime and source hashes changed;
the low checker additionally records the same-hull L1 bound above.

| Checker | SHA-256 | Result |
| --- | --- | --- |
| check_theta_stationary_cell.py | e721cbd7d4a212fd18c460a057c6cf5c4d3cfb306667c7152d6b99e5d755e6b3 | PASS; eighty high-cell subcells |
| check_theta_stationary_low_height.py | 18058e4994ae1c93f7796b87a12537a519340ea56228b5eac20a8db3ca1fa704 | PASS; 2,048 integration and eighty height cells |
| check_theta_laguerre_kernel.py | 91f0fa818a9e1b18211e2f177c990b6ab090ec67b6e584f4e293716155ae7d2c | PASS; complete signed source at 0.3 |
| check_laguerre_kernel_algebra.py | e3287e09e16700401b120c4541ec91cb99672ef462fbc6779c0a6b43709447e8 | PASS; 167 exact assertions |

Hashes establish source identity in the checked environment. They do not
replace outward sign decisions or provide independent proof. Finite exact
assertions do not verify analytic remainder or uniform theta signs.

Native manuscript compilation: PASS on the saved existing source,
`enlarged_state_transport_and_heat_flow.tex`, using the desktop editor
compiler. An initially missing script-font package was added; the next
compile succeeded. The current editor stayed open and no replacement
source or separate PDF was produced.

A separate-agent review of the final integration text and Note 6 also
passed, including every printed outward shortening, unique stationary
branch argument, product cost and boundary limitation. Its suggested
clarification was incorporated: the high-cell real normalizer A_t is
explicitly distinguished from the chord readout A=2H.

## Research disposition

The next analytic obligation is a uniform conditional Fourier sign for
J0 on Hx=0 and J1 on Hxx=0, with a predecessor neighborhood. Positive
definiteness of the complete kernels is a stronger sufficient route.
A theta-specific identity modulo the stationary constraints would also
be useful if its channels and residual payments were independently proved;
none has been constructed. Intermediate work can improve direct rigorous
quadrature or attempt a nonvacuous high-height S1 cell with full third-jet
costs. Pointwise source positivity, passive coordinates and the first
Laguerre hierarchy alone do not discharge the target.

Evidence: [paid stationary signs](../notes/6_PAID_GENUINE_THETA_STATIONARY_SIGNS_20261010.md),
[complete kernels and triple limit](../notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md),
and their four checker/record pairs in [numerics](../numerics/README.md).
