# Row-selector feasibility: the principal rows added by enlargement

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Status: exact positive decomposition, an elementary partial bound for
mean-zero plain profiles, and a conditional inverse-sum budget. The
complete-family route is not justified by the available estimates. This
does not disprove the restricted mixed-moment target. The current
conditional candidate remains **7/8 − 1/24000**; **7/8 − 1/20000** remains
conditional on the unproved uniform mixed saving.

This carries out the first gate in the [continuation plan](CONTINUATION_20261008.md).
Use the [manuscript](../manuscript.tex) definitions throughout, including
its actual profiles, fixed prime lists, fixed ray presentation, and zero
extensions. The source is the [September 30 companion preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
with the already recorded SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The source checks are in the [continuation input review](../reviews/CONTINUATION_INPUT_REVIEW_20261008.md).

## 1. The precise positive enlargement

Fix all separating parameters first. Choose a nonnegative smooth compactly
supported function Phi on an annulus in (0,infinity), with Phi >= 1 on
the physical norm interval of C. Define

    E_Phi = sum_{u in O, u != 0} Phi(Nu/U) |M_r(u) S_m(u) Q_I(u)|^2.

The coefficients and original column masks are unchanged. This family
includes elements that are not sixth-power-free and characters that are
principal. Positivity gives the exact sufficient route

    E_C <= E_Phi;    E_Phi << U^K H^A would suffice,
    K = 1 + delta*m - eta, eta = 1/5000, H = 1+T_1.       (1)

For an application, (1) must hold uniformly over the manuscript's box,
the actual disjoint prime lists and bounded prime coefficients, the
permitted truncated-inverse/plain profiles and their required derivative
profiles, either common orientation, and the finite permitted ray data.
Constants use fixed annuli, finitely many seminorms, slot cap, arithmetic
data, and strict capacities. Height orders must be fixed before choosing
the slowly growing height range. The test below at nu=1 and fixed heights
is necessary for a claim uniform over that presentation and profile class;
it does not identify the profiles selected by an actual detector row.

## 2. Exact sixth-power rows, with no unit overcount

The Eisenstein ring is a PID with six units. For each nonzero integral
ideal a, choose a generator alpha_a. The element alpha_a^6 is independent
of this choice, and the map a -> alpha_a^6 is a bijection onto the
nonzero sixth powers. Indeed equal sixth powers have generators differing
by a sixth root of unity, hence the same ideal. Therefore these rows are
counted once by ideals. Summing over all nonzero element roots instead
would require a factor 1/6. Do not also multiply the ideal sum by six.

In the principal-twist case nu=1 (with its fixed zero support still
excluded), either orientation gives

    chi_n(alpha_a^6) = 1_{(a,n)=1}.

All following sums are over the original good column supports. Set

    M^(a) = D^(-1/2) sum_d mu_F(d) A(Nd/D) 1_{(a,d)=1},
    S^(a) = N^(-1/2) sum_k B(Nk/N) 1_{(a,k)=1},
    Q_i^(a) = P_i^(-1/2) sum_{p in P_i}
                  a_i(p) W_i(Np/P_i) 1_{p not dividing a},
    Q^(a) = product_i Q_i^(a).

The exact extracted norm is

    E_6 = sum_{a integral, a != 0} Phi((Na)^6/U)
                         |M^(a)|^2 |S^(a) Q^(a)|^2.      (2)

There are O(U^(1/6)) such a on the support. Equation (2) is a positive
subsum of E_Phi, so E_Phi = E_6 + E_other with E_other >= 0. It is not a
subsum of E_C: its inducing row character has primitive conductor 1,
while C consists of nonprincipal rows and C_+ has growing primitive
conductor. The mask rad(a) does not become a primitive conductor.

More generally, write an element uniquely as u=b alpha_a^6 by choosing
one generator for each sixth-power-free ideal and putting the remaining
unit into b. If a fixed nu presentation induces the principal character,
b can have prime divisors only in the fixed excluded set S: at every
other prime an exponent 1,...,5 has a nontrivial sextic local character.
There are finitely many possible such seeds b, including their units.
For each principal seed, (2) has Phi(Nb*(Na)^6/U) and the original b
masks. Outside S its coefficients reduce to the same principal masked
sums. Thus the same budgets apply to the entire principal-inducing
part, up to a fixed finite sum. Unit seeds are not silently identified.

These row statements are unrelated to the ratio conductor f(n,n') of
two columns. The previously controlled principal *column pairs* can be
small even when principal *rows* impose a difficult budget on E_Phi.

## 3. Evaluate the actual plain and prime coefficients first

Write R_a=rad(a)*S as a union of prime supports, without repeated primes,
and define

    beta_B = integral_0^infinity B(y) dy,
    c(a) = Res_{s=1} zeta_F(s) product_{p|R_a}(1-(Np)^(-1)).

Smooth lattice counting, followed by inclusion-exclusion at R_a, gives

    S^(a) = N^(1/2) c(a) beta_B
                    + O_epsilon(N^(-1/2) U^epsilon H^J).       (3)

Here the integral is of the actual B, including its real and imaginary
norm powers. For example, if B(y)=B_0(y)y^(sigma+it), the integral is
integral B_0(y)y^(sigma+it)dy, not integral B_0. Nonnegative untwisted
nonzero B has positive beta_B; a general selected or derivative profile
can have beta_B=0. A fixed nonprincipal ray twist has zero lattice main
coefficient as well. No assertion of a nonzero main term is made for
the detector's unspecified fixed profiles.

For completeness, the uniform error in (3) has an elementary proof.
Divide the smooth radial element-lattice sum by six to count ideals;
Poisson summation gives its area term plus O(H^J) on every scale >=1.
After extracting e|R_a, the scale is N/Ne, and
Ne <= O(U^(1/6)) while m >= 9/25 > 1/6. Each residual scale therefore
exceeds one for large U. The divisor count of R_a is O_epsilon(U^epsilon).
This proves the stated unnormalized error O(U^epsilon H^J).
Equivalently this is the principal case of source Lemma 18.3. The proof
retains the fixed S restrictions and all a masks; it does not use a
sharp ideal-count remainder in place of smooth Poisson.

For every prime slot there is the exact, coefficient-sensitive formula

    Q_i^(a) = Q_i^(1) - P_i^(-1/2)
                 sum_{p in P_i, p|a} a_i(p) W_i(Np/P_i).       (4)

The deleted sum contains O(log U) primes. Its size is
O(P_i^(-1/2) log U) times the permitted profile bound. But neither
the original prime lists nor the bounded complex coefficients imply
that Q_i^(1) is nonzero or has size P_i^(1/2-o(1)). Cancellations,
empty supports, and vanishing profiles must all remain possible.
For fixed positive w_i, an independently established lower bound
|Q_i^(1)| >= P_i^(1/2) U^(-epsilon) makes the deletion negligible
after choosing epsilon small relative to w_i. For w_i=0 one must
evaluate the finite sum and its masks directly; such uniform neglect
would be false.

## 4. The exact budget and the diagnostic nonzero-mass budget

Define the nonnegative, actual profile weight

    G(a) = U^(-m-z) |S^(a) Q^(a)|^2.

No asymptotic is needed for the exact equivalence

    E_6 <= C U^(K+epsilon) H^A
    iff
    sum_a Phi((Na)^6/U) G(a)|M^(a)|^2
       <= C U^(1-(1-delta)m-z-eta+epsilon) H^A.             (5)

This is the missing weighted inverse estimate for these extra rows.
There is no claimed cancellation in the Möbius sum M^(a) from (3) or
(4). In particular the truncation in A has not been removed.

As a diagnostic, suppose beta_B is fixed nonzero and the actual prime
factors have the above principal mass on a specified subfamily A_0 of
roots. Equations (3)-(4) then give G(a) >= U^(-epsilon) on that
subfamily, after reallocating the small losses; c(a) has an inverse
bounded by an arbitrarily small U-power. A necessary consequence of
the enlarged target is the unweighted bound on that subfamily

    sum_{a in A_0} Phi((Na)^6/U)|M^(a)|^2
          << U^B6,     B6=1-(1-delta)m-z-eta,              (6)

with epsilon and the permitted height factors restored. If the mass
condition holds on every root, (6) concerns every root. If bounded
slots require coprimality with extra fixed primes, it concerns that
restricted root family only. Nonnegative prime-rich lists and
untwisted profiles motivate this diagnostic, but no such mass is
inferred for the application's actual lists. Equation (5), not (6),
is the statement for general profiles.

## 5. What the available estimates supply

Assume the imported seven-eighths theorem and its global reciprocal
control. Source Lemmas 4.9 and 4.10, followed by smooth Mellin inversion,
give, uniformly for the polynomial-size masks here,

    |M^(a)|^2 << D^(3/4+epsilon) U^epsilon H^A.

Indeed the masked Dirichlet series is

    1/zeta_F(s) product_{p|R_a}(1-(Np)^(-s))^(-1),

and the contour may be placed at Re s=7/8+v for any fixed v>0.
The reciprocal has a zero, not a pole, at s=1. The original smooth
inverse cutoff remains part of A. This imports the source theorem;
it is not an independent proof of that theorem or a sharper boundary.
Counting roots gives

    sum_a Phi((Na)^6/U)|M^(a)|^2
                   << U^(1/6+3r/4+epsilon) H^A.           (7)

Before using a full principal exponent, one can retain the actual
profile dependence in the sufficient upper bound

    E_6 << U^(1/6+3r/4+epsilon) H^A
           [N |beta_B|^2 + N^(-1) H^J]
           product_i (|Q_i^(1)| + C_i P_i^(-1/2) log U)^2,

where C_i bounds the relevant prime profile. This follows from
(3)-(4), c(a) << 1, and (7). It is useful even when some principal
prime sums vanish. No numerical values for these actual profile
integrals or prime sums are supplied by the fixed-bin specification.

At z=(1-r)/2-rho, the exponent of (7) exceeds B6 by

    Delta6 = (1-delta)m + r/4 - 1/3 + eta - rho.

Over the entire continuous box, monotonicity in delta, m and r gives

    19/375 - rho <= Delta6 <= 1289/7500 - rho.             (8)

Thus a small capacity decrement, including any rounding included in
rho, leaves a fixed gap. The same exponent follows as an upper bound
for E_6 using (7) and triangle bounds for the plain and prime factors:
1/6+3r/4+m+z. It is an inadequate upper bound, not a lower bound on
E_6. The root average might cancel much more strongly.

A pointwise substitute |M^(a)|^2 << D^(2sigma-1+epsilon) would need

    sigma <= sigma_req
      = 3/4 + [1/3-(1-delta)m-eta+rho]/(2r).              (9)

At rho=0 its extrema are 16847/22200 and 3523/4200 (about 0.759
and 0.839), below 7/8. An averaged estimate (5) could be weaker than
this pointwise demand; (9) is a sufficient budget calculation, not a
necessary new zero-free half-plane. Even the present conditional
candidate improves 7/8 by far too little to close (8) by this method.

The original marked inverse input also applies positively to these
rows, but combining it with the plain triangle bound gives only
E_6 << U^(1+m+epsilon)H^A. The buffered plain bound cannot be used
here: these added principal rows do not belong to its nonprincipal
zero bin. No available estimate checked here proves (5) in the
nonzero-mass regime. Removing principal rows by an indicator makes
a new restricted family; the unmodified complete smooth Poisson
formula then no longer applies without an additional decomposition.

## 6. A proved partial theorem when the actual plain mean vanishes

**Proposition.** In the nu=1 case, for fixed admissible smooth profiles
with beta_B=0 and all original masks and prime supports retained,

    E_6 << U^(1/6+r-m+z+epsilon) H^A
        << U^(K-6791/15000+epsilon) H^A.                 (10)

The same conclusion holds for a finite sum of principal seeds described
in Section 2, with beta_B=0 for each associated profile. It is uniform
for a family of profiles with controlled required seminorms that each
satisfy the displayed mean-zero condition.

**Proof.** Equation (3) gives |S^(a)|^2 << N^(-1) U^epsilon H^A.
Ideal counting gives |M^(a)|^2 << D H^A without cancellation, and
|Q^(a)|^2 << U^z H^A, including bounded or empty prime slots. Sum over
O(U^(1/6)) roots. Since z <= (1-r)/2, the margin below K is at least

    1/3-r/2+(1+delta)m-eta >= 6791/15000.

The minimum occurs at r=37/50, delta=m=9/25. This proves (10).

This elementary subcase controls the principal layer only. It neither
bounds E_other nor establishes the original restricted mixed saving.
Moreover beta_B=0 at one height need not imply that the height
derivatives of B have zero integral. The rowwise Sobolev application
requires the condition or another estimate for each derivative profile.

## 7. Decision and selector-preserving alternative

Do not start a complete-family induction as though (1) were now an
available estimate. For unspecified actual profiles the principal test
is profile-dependent; in its nonzero-mass regime it requires the new
weighted inverse estimate (5), and removing that regime still leaves
the other added rows. The formal divisor calculation can be studied
separately, with this gate explicit; see the [live-divisor note](LIVE_DIVISOR_TRANSFORM_20261008.md).

The justified route keeps w(u)=1_{C_+}(u). One precise positive input is

    sum_u w(u) |S_m(u)|^2 |M_r(u)Q_I(u)|^2
                       << U^(1+delta*m-eta+epsilon) H^A. (11)

Equivalently put g(u)=w(u) U^(-delta*m)|S_m(u)|^2 and ask for
sum_u g(u)|M_rQ_I|^2 << U^(1-eta+epsilon)H^A. The available
buffered bound and marked inverse moment give only U^(1+epsilon)H^A
for this last sum. The saving must exploit this particular g, including
its zero/profile-bin origin and its actual plain coefficients; it is
not asserted uniformly over arbitrary bounded nonnegative weights.

By the existing three-block reduction, (11) can instead be sought as
the one-sided bound on the complete signed T_large with its sharp row
selector, unequal plain ideals, ratio conductor and E-mask intact.
A future weighted transform must prove its estimates for that selector;
inserting it into a Schwartz profile is not a justification. The
remaining arithmetic estimate and the full application uniformity are
still open. No new two-rebalance payoff is activated by (10).

Exact exponent checks are reproducible with
`numerics/check_selector_feasibility.py`. They certify these budgets,
not Möbius cancellation or the main-mass hypotheses in Section 4.
