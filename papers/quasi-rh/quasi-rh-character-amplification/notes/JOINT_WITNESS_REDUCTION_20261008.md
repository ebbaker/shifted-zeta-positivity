# Joint inverse/plain witnesses: exact reduction and the missing estimate

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort
are not exposed and are not inferred.

Status: exact coefficient identities and conditional exponent bookkeeping, plus
an obstruction to deducing a new power saving from the existing marginal
moments alone. No new arithmetic moment or zero-free theorem is proved here.
The external detector and moment statements are imported conditionally; this
note does not validate their deep proofs.

Source: the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
Proposition 8.3, Lemmas 17.1 and 18.1, and Proposition 19.2. PDF pages 59–60
contain the complete detector, and pages 182–185 fix the common character,
physical slots and moment capacities. The local research-directions note and
[bottleneck sensitivity record](../numerics/bottleneck_sensitivity.json) supply
the numerical diagnostic point below. The consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

## 1. A smaller mixed object is sufficient

Let the row scale be U, the inverse length D=U^r, and the plain length N=U^m.
After the source's fixed presentation and dyadic subdivision, write M_r and
S_m for the two witnesses. Proposition 8.3 supplies the same zero-extended
character and the same norm-twist height for both. In particular,

    |M_r S_m|^2 >= U^{delta(r+m)-epsilon}.

It is not necessary to square the plain witness again. The first object to
investigate should be

    sum_{u in C} |M_r(u) S_m(u) Q_I(u)|^2,

where C is a fixed buffered zero bin with a prescribed nearly saturated
physical-prime amplitude profile, and Q_I is one actual permitted product of
selected physical prime slots. C should not be defined by the simultaneous
witness lower bounds; those pick out the exceptional subset B of C to count.

At the diagnostic obstruction recorded in bottleneck_sensitivity.json,

    delta = 0.38668853097393885,
    r     = 0.7149876681965772,
    m     = 0.4083888933488997,
    t     = r+m = 1.123376561545477,
    R     = 0.6684169689733224.

Thus the column product for M_r S_m has log-length 1.12337656. For
M_r S_m^2 it is 1.53176545. The latter remains legitimate but asks for a
longer mixed polynomial and has no additional detector identity.

## 2. The exact coefficient and what common height does

Write the untwisted inverse and plain annular profiles as A and B, retaining
A(x)=W_1(x)V_<= (Dx/D_*) from the source. Fix all separating parameters first,
and let s_0=sigma+i omega be their common profile norm power. The product is
exactly

    M_r S_m
      = (DN)^{s_0-1/2}
        sum_n psi(n) (N n)^{-s_0} c_{D,N}(n),

    c_{D,N}(n)
      = sum_{d|n} mu_K(d) A(N d/D) B(N(n/d)/N).

Here N n denotes the ideal norm. The character includes all original row,
fixed-ray and excluded-prime zeros. Its complete multiplicativity makes this
factorization valid even when a divisor meets a zero support: both sides then
vanish. Common height makes the norm phase depend on the total ideal n; it does
not make the annular divisor weight constant.

For the unseparated detector block, retain in addition the product cap

    H_{D,N}(N n/(DN))
      = Omega(N n/(DN)) [1-V_<= (2 N n/D_*)]
        exp(-N n/Y_*) V_term(N n/U^21).

The source's Fourier separation of H gives the common additional frequency
nu. Selecting one Fourier frequency removes H from that selected product only
because its Fourier coefficient remains in the integral from which the witness
was selected. It is invalid to discard H from the complete detector or to
identify a selected rectangle with the full unweighted convolution.

Adding physical slots gives a coefficient sum over

    n = d k p_1 ... p_j,

with the same psi(n), the actual annular inverse/plain weights, and the original
fixed prime coefficients and disjoint prime-support conditions. The physical
prime heights need not equal omega. Their norm weights must stay in the
coefficient or be separated with the source's permitted smooth calculus. They
are not extra free coefficients. No new row-dependent prime coefficients are
introduced by this reduction.

## 3. Why mu_K * 1 does not give a power saving here

The identity mu_K*1=epsilon holds only after the complete divisor sum has been
retained. A chosen dyadic rectangle does not have that coefficient. For example,
choose distinct prime ideals p and q outside all masks, with norms near D and N
respectively. Since r>m>0 and all profile windows are fixed, for sufficiently
large U the only divisor of pq that can meet the inverse annulus near D is p.
On a subwindow where A and B are nonzero,

    c_{D,N}(pq) = - A(N p/D) B(N q/N),

which is nonzero. This is a coefficient obstruction to formal cancellation,
not a lower bound for the character-family moment. It holds without relying on
arbitrary coefficient choices.

The full truncated inverse has coefficient

    C_{D_*}(n) = sum_{d|n} mu_K(d) V_<= (N d/D_*).

For n != 1 it also has the exact boundary representation

    C_{D_*}(n)
      = - sum_{d|n} mu_K(d) [1-V_<= (N d/D_*)].

It vanishes for 1<N n<=D_*, but it does not vanish above the cutoff. Those
boundary coefficients are exactly what carry the zero detector. Removing them
by an appeal to complete convolution removes the mechanism producing the
large witness.

For the larger mixed object M_r S_m^2, the formal unrestricted convolution is

    mu_K * 1 * 1 = 1,

where the final 1 is the constant-one function on ideals, not convolution's
unit epsilon. Thus even the fully untruncated algebra has a surviving main
coefficient. In a dyadic example n=p q_1 q_2 with N p near D and distinct
N q_j near N, and with 2m>r, only d=p meets the inverse annulus; its coefficient
is the negative sum of the two ordered plain-factor weights. It again does
not cancel. This example applies at the current diagnostic point.

## 4. A precise, weaker-than-square-root missing estimate

Let all positive selected slots have total length z, measured at base U, and
let their actual gain be G_I=sum_i w_i g_i. Their squared product on B is at
least U^{2G_I-o(1)}. A mixed bound

    sum_{u in C} |M_r S_m Q_I|^2
      <= U^{K+epsilon} (1+T_1)^A

therefore implies

    #B <= U^{K-delta(r+m)-2G_I+epsilon}(1+T_1)^A.

All rowwise witness parameters require the same uniform Sobolev treatment and
height-order quantifiers as in the source; the displayed estimate is not a
license to choose unrelated coefficient arrays separately for each row.

At the flat endpoint g_i=delta/2 and q=delta/2, G_I=delta z/2. With no primes,
the exponent that just matches R is

    K_0 = R+delta(r+m) = 1.1028138012878974.

Thus a theorem with K<K_0 would already be useful; a generic U^{1+epsilon}
bound is much stronger than necessary. For comparison, the available marked
inverse moment and the plain pointwise bound yield only

    sum_C |M_r S_m|^2 <= U^{1+delta m+epsilon},
    1+delta m = 1.1579193012351587.

The especially natural selected length is

    z_M = (1-r)/2 = 0.1425061659017114,

with the source's fixed strict capacity decrement and whole-slot loss. Since
at the crossing R=1-delta(r+z_M), the existing estimate

    sum_C |M_r S_m Q_I|^2 <= U^{1+delta m+epsilon}

is exactly at the required threshold. Any uniform improvement

    sum_C |M_r S_m Q_I|^2
      <= U^{1+delta m-eta+epsilon}(1+T_1)^A,  eta>0,

on the localized parameter and amplitude class improves this short-branch
count by eta, apart from the explicitly reserved capacity/mesh losses.
This is a weighted correlation saving over the pointwise plain bound under
the marked inverse energy. It need not save all of delta m.

There is a dual target using the plain capacity

    z_P=2(1-2m)/9=0.040716047400489015.

The existing plain fourth moment and inverse pointwise bound give

    sum_C |M_r|^2 |S_m|^4 |Q_J|^2
      <= U^{1+delta r+epsilon}.

Replacing its exponent by 1+delta r-eta would likewise improve the count by
eta at the short crossing. The first target has the shorter product length
and is the preferred initial arithmetic calculation.

A gain only at the short crossing does not by itself lower the entire envelope
by eta. The competing long branch remains, so the detector cutoff must be
rebalanced and all nearby and outside bins controlled. No new global boundary
is asserted from this target alone.

## 5. Existing marginal moments cannot force the saving

This is an algebraic insufficiency, not a counterexample in the arithmetic
family. Consider an abstract set with U^R rows. On every row set

    |M_r|^2=U^{delta r},   |S_m|^2=U^{delta m},
    |Q_I|^2=U^{delta z_I}.

At the diagnostic short crossing,

    R+delta(r+z_M)=1,
    R+delta(2m+z_P)=1.

Consequently this maximally correlated model obeys, and saturates, both of the
existing selected marginal moments. Smaller selected lengths only weaken
those constraints. It also obeys the displayed pointwise bounds. Applying
Holder, Cauchy–Schwarz, or interpolation to these same inequalities cannot
rule the model out, hence cannot prove a saving in R. The missing input must
use arithmetic information absent from the separate marginal estimates.

## 6. Two cutoffs at the same zero: an exact relation, not independence

Proposition 8.3 may use the same selected zero rho for every t. For a cutoff
D_*=U^t, keep the same Y_*=U^20 and terminal cutoff, and define

    J_D(rho)= (1/(2 pi i)) integral_{(2)}
              Y_*^z Gamma(z) L_orig(rho+z,psi) C_D(rho+z) dz,

where C_D(s) is the finite truncated inverse Dirichlet polynomial, as in the
source. Its contour proof gives J_D(rho)=o(1), uniformly for 1<=t<=3/2. Before
the terminal truncation, the tail detector is exactly

    T_D(rho)=J_D(rho)-exp(-1/Y_*).

The equality uses the vanishing coefficient for 1<N n<=D and the product cap
[1-V_<= (2 N n/D)]. The terminal truncation adds only o(1). Hence

    T_{D_1}(rho)=-1+o(1),
    T_{D_2}(rho)=-1+o(1),
    T_{D_1}(rho)-T_{D_2}(rho)=o(1).

Before the terminal truncation the difference is a single exact Dirichlet
coefficient sum with

    C_{D_1}(n)-C_{D_2}(n)
      = sum_{d|n} mu_K(d)
        [V_<= (N d/D_1)-V_<= (N d/D_2)].

Its unit term vanishes. It is supported on a divisor transition shell; one
must retain both original caps when expressing it in the two capped dyadic
expansions.

This supplies a useful signed compatibility equation. It does not give two
independent large events, and their probabilities cannot be multiplied. A
linear combination sum_j a_j T_{D_j} with sum_j a_j=1 retains the detector
signal; a contrast whose coefficients sum to zero kills it. Exploiting that
compatibility would require an actual mixed kernel estimate for these full
capped sums, preserving their phases.

There is also a parameter warning: the subsequent dyadic selection can produce
a different pair (D,N) and a different Fourier frequency nu for each cutoff.
The underlying zero height gamma is shared, but the selected witness height
gamma-nu need not be. Proposition 8.3 does not give a common selected nu or
common selected profiles across cutoffs. Cross-scale moment claims must retain
the two integrations or prove the needed joint selection lemma.

## 7. Next concrete arithmetic calculation

Take the shorter selected object M_r S_m Q_I, at z just below (1-r)/2, on the
nearly saturated buffered bin. Expand its exact squared coefficient before
any absolute value. This preserves the four variables from the inverse/plain
pair and the original prime labels. The source's marked inverse machinery
cannot be cited unchanged after appending S_m: the residual coefficient is a
truncated convolution, not its permitted Mobius coefficient class.

The practical target is the eta saving in Section 4. A derivation should locate
one explicit off-diagonal or transformed exceptional term whose contribution
is bounded by U^{1+delta m-eta}. The semiprime coefficient calculation shows
that a formal mu*1 cancellation is insufficient. The abstract saturation model
shows that recombining only the already-proved moments is also insufficient.
This narrows the task to a genuine, localized arithmetic correlation estimate.

## 8. Conditional uniform payoff on the proposed hard box

The following computes the payoff of the missing mixed estimate; it does not
prove that estimate. Suppose the preparation localizes the remaining problem
to

    9/25 <= delta <= 21/50,   49/100 <= x=q/delta <= 1/2,

and to the nearly saturated amplitude profiles specified by the parent
localization (in that notation, H_G<1/5000). Set

    B=2-8x/9, D=3-17x/9, P=B(1-x),
    a=5/6-delta, J=aD+delta P, c=B/D.

The old affine inverse and plain counts are

    A_I(r)=1-delta[x+(1-x)r],
    S_t(r)=1-delta[4x/9+B(t-r)].

A mixed-moment saving eta_mix in Section 4 improves A_I to A_I-eta_mix;
it does not independently improve S_t. Their new crossing is therefore

    r_new(t)=r_*(t)-eta_mix/(delta D),
    r_*(t)=(Bt-5x/9)/D.

The short envelope drops by c eta_mix, rather than eta_mix. Rebalancing it
against the unchanged long branch gives

    t_new=t_0-B eta_mix/J,
    t_0=1+delta P/(2J),
    R_new=R_* - F eta_mix,
    F=(5/6-delta) B / J.

Both rebalances matter. Over this hard box, F decreases with delta and
increases with x. Indeed its derivative in delta is

    -(5/6) B^2(1-x)/J^2 < 0,

and its derivative in x is

    a[(10/9)a+delta B^2]/J^2 > 0.

Thus the exact uniform factor is

    F >= F(21/50,49/100) = 1091200/2012413
      > 0.5422346208.

Taking eta_mix=1/5000 gives a full-envelope gain at least

    1091200/10062065000 > 0.000108446924.

This leaves more than 0.00000844 for cumulative capacity, mesh, witness,
height and other losses if the desired final row gain is 1/10000. A saving
eta_mix=1/10000 would not suffice for that final target by this route.

A rectangular mixed-input domain suffices: it is enough to prove the stated
moment saving uniformly for

    7/10 <= r <= 37/50,   9/25 <= m <= 1/2,

with the actual selected prime product of requested length z_M=(1-r)/2
minus its fixed capacity decrement, and with the source's actual common
character and profiles. The inverse base cutoff V_<= (Dx/D_*) is identically
one on these annuli for all sufficiently large U: t_new-r is bounded below
by more than 0.36. Thus the necessary inverse base profiles here are simply
the fixed dyadic partition profiles, with the selected real and imaginary
norm powers. Uniformity for arbitrary coefficient arrays is not requested.

Here is an elementary bound proving coverage of the entire short-witness
range, rather than only the numerical crossing. Let lower/upper subscripts
indicate the endpoints of the hard box. Define

    J_low = (5/6-delta_high)D(x_high)+delta_low P(x_high),
    J_high= (5/6-delta_low) D(x_low) +delta_high P(x_low).

Positive interval arithmetic gives

    t_low=1+delta_low P(x_high)/(2J_high)
            -B(x_low)eta_mix/J_low > 1.106,
    t_high=1+delta_high P(x_low)/(2J_low) < 1.149.

The functions B/D and (B-5x/9)/D are respectively increasing and decreasing
in x. Substitution of these bounds into r_new gives

    0.701 < r_new < 0.736.

More accurate diagnostic bounds from the same coarse arithmetic are
0.7013099<r_new<0.7351703. No assumption about where inside the hard box the
minimum occurs is needed. If r is in [0.70,0.74], the detector support bound
m>=t_new-r-o(1) gives m>0.366-o(1), so the requested m>=0.36 covers every
potentially relevant witness there. Cases m>=1/2 are already bounded by the
source's unmarked plain fourth moment.

For r<=0.70, the old plain line is below the improved short envelope by at
least

    delta_low B(x_high) (0.701-0.70) > 0.0005.

For r>=0.74 and r<1, the old inverse line is below it by at least

    delta_low (1-x_high)(0.74-0.736)-eta_mix > 0.0005.

Hence outside the requested inverse-length band the old marginal estimates
have ample fixed slack. This supplies an actual covering argument for all
short witnesses. Long inverse witnesses continue to use the original long
estimate at t_new. The numerical inequalities in this paragraph have large
rational safety margins, and the source's small support and moment losses can
be reserved below those margins.

This payoff is conditional on a uniform mixed estimate over the entire stated
bin/profile/length domain. Establishing it only at the diagnostic point, for
one prime slot selection, or for one row-independent norm-twist height would
not close the argument.

See the [localized payoff](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md),
[exact payoff record](../numerics/joint_witness_payoff_check.json), and
[scoped review](../reviews/LOCALIZED_TARGET_PROFILE_REVIEW_20261008.md).
