# Primitive-conductor localization of the remaining mixed moment

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

Status: a further conditional reduction using the source's existing reflected
plain-polynomial estimate, together with an exact coefficient observation and
an obstruction to a proposed elementary argument. No new mixed moment or
zero-free boundary is established. The source's analytic inputs remain
assumptions; their deep proofs have not been independently validated here.

Source: the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
Lemmas 8.1, 8.2 and 17.1, Proposition 8.3, and Section 19.1. The consulted PDF
has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
See also [joint witness reduction](JOINT_WITNESS_REDUCTION_20261008.md) and
[amplitude-profile reduction](AMPLITUDE_PROFILE_REDUCTION_20261008.md).

## 1. Keep the actual primitive row conductor in the reflected bound

Fix the source's nonprincipal row presentation psi, at row scale U, and let
Q_psi be the conductor norm of the primitive character inducing it. Define

    theta = log(Q_psi)/log(U).

This is a conductor of a character indexed by the row. It is not the conductor
of the ratio of two column characters appearing when a moment is expanded.
The two conductor localizations are distinct and may be imposed together.

Write delta=2a-1 for the buffered zero bin. In the proof of Lemma 8.1, before
using Q_psi << U, the reflected bound is

    |L_orig(1-a-6e+it,psi)|
      << Q_psi^(a-1/2+6e) U^(O(e)+epsilon) (1+T_1)^A.

The estimate follows directly from the primitive functional equation, the
source's bound for the conjugate primitive L-value on the right-hand line,
and its deleted Euler-factor estimate. The norm of the deleted-prime radical
is polynomial in U, exactly as in the source. No deleted Euler factor is
replaced by an independently chosen mask.

On the present hard box 9/25 <= delta <= 21/50, the reflected line has real
part at least 29/100-6e. It is therefore bounded away from zero after e is
chosen small. The deleted Euler product has an arbitrarily small U-power
there. Retaining the weaker U^(O(e)+epsilon) bound already suffices. The
Gamma quotient and all allowed norm-twist heights have the same fixed
polynomial height cost as in Lemma 8.2.

Repeating its plain-polynomial Mellin shift, but retaining Q_psi, gives

    |S_m(psi)|^2
      << U^[delta(theta-m)+epsilon] (1+T_1)^A.                (1)

All preliminary e-losses have been absorbed into epsilon. This is uniform
for the fixed length ranges, fixed smooth-profile seminorms, and cumulative
height allocation used in the existing detector. Here Q_psi << U supplies a
bounded range for theta. Combining with the direct right-hand contour bound
also gives the sharpened version of Equation (8.2):

    |S_m(psi)|^2
      << U^[delta min(m,theta-m)+epsilon] (1+T_1)^A.         (2)

Formula (2) does not assume a smaller row range and does not change the row
character. In particular, one must not silently apply a moment theorem at
base U^theta to rows whose physical norms are still of size U.

## 2. A proved partial saving at the mixed-moment level

Let C be any subcollection of a fixed nonprincipal buffered bin, with fixed
presentation and physical amplitude profile. Let Q_I be the actual selected
product of disjoint physical prime slots, of total length z, and assume the
strict marked-inverse conditions

    r+2z <= 1-c_1,   2r+8z <= 3-c_2,

for positive fixed c_1,c_2. The inverse and every prime slot use the common
presentation required by Lemma 17.1; norm-power and height parameters have
its permitted uniform treatment.

For any fixed lambda>0 define

    C_low(lambda) = {u in C: theta(u) <= 2m-lambda}.

Applying (1) pointwise on this set and Lemma 17.1 to the marked inverse gives

    sum_{u in C_low(lambda)} |M_r S_m Q_I|^2
      << U^[1+delta m-delta lambda+epsilon] (1+T_1)^A.      (3)

This argument is valid even though membership in C_low is defined by the
moving conductor: after the pointwise bound, positivity permits enlarging the
remaining marked-inverse sum to the full row family. No Poisson estimate with
an arbitrary sharp conductor weight is being asserted.

For the target mixed saving eta_mix=1/5000, choose

    lambda=1/1000.

Uniformly on 9/25 <= delta <= 21/50,

    delta lambda >= 9/25000 = 1/5000 + 1/6250.

Thus all rows with theta <= 2m-1/1000 already have the required mixed saving,
with an additional exponent margin 1/6250 available for the prescribed
losses. This gain is conditional only on the already-imported source inputs;
it is not the missing new arithmetic theorem.

Consequently the new mixed estimate need only address

    theta > 2m-1/1000,                                    (4)

in addition to the previous hard box, amplitude-profile restriction, and
length ranges. On 9/25 <= m <= 1/2, condition (4) runs from theta>719/1000
at the left endpoint to theta>999/1000 at the right endpoint. It leaves the
ordinary large-conductor rows, so it does not by itself lower the final
exceptional-row envelope.

The fully selected detector witnesses are even more restricted. If their
plain lower bound is |S_m|^2 >= U^(delta m-epsilon_w), (1) forces

    theta >= 2m-(epsilon+epsilon_w)/delta
                 - A log(1+T_1)/(delta log U) - o(1).

After the usual preliminary-loss and height choices, this is

    theta >= 2m-o_loss(1).                                (5)

The notation means a loss made arbitrarily small by the source's fixed
parameter choices; it is not a new uniform zero-error asymptotic. Formula
(5) sharpens the description of the rows carrying an actual detector spike.
For a moment over the larger profile class C, (3)-(4), rather than an assumed
witness condition on every row of C, are the valid reduction.

## 3. Why exponent saturation gives no elementary phase rigidity

For a physical slot at prime scale P, saturation means a normalized prime
sum of size approximately P^(delta/2). Even for nonnegative untwisted
profiles, its absolute-sum bound is of order at most P^(1/2+o(1)). The ratio
between these scales is

    P^[-(1-delta)/2+o(1)],

which tends to zero throughout the hard box. Thus saturation relative to the
zero-bin upper exponent is very far from equality in the triangle
inequality. For the plain polynomial the analogous ratio is

    N^[-(1-delta)/2+o(1)].

A majority of summands need not have aligned phases. No inference that the
character is approximately +1 on the plain interval, or approximately -1 on
prime factors of the inverse interval, follows from the amplitudes alone.
The fact that both polynomials use a common height correctly gives one
multiplicative norm phase in their product; it does not supply such an
alignment assertion. Any argument using more precise phase information must
prove it arithmetically.

A positive majorant made solely by inserting unused physical slots also has
a precise limitation. Applying the current marked-inverse theorem to a
whole-slot product permits total length at most (1-r)/2, less a strict
margin. Splitting that allowed length into 'witness marks' and 'majorant
marks' does not enlarge it. At a flat saturated profile, every unit of
length supplies exactly delta units of squared lower-bound exponent, so
redistributing the marks cannot exceed delta(1-r)/2. Reusing the same slot
with higher powers does not satisfy the theorem's disjoint prime-support
coefficient class. This explains, at the coefficient level, why the reserve
of physical prime slots is not by itself a new saving.

## 4. A small exact part of the expanded moment is already harmless

Fix the common separating parameters first, as required before a kernel
expansion. Let D=U^r, N=U^m, and let the selected prime lengths multiply to
U^z. Apart from their fixed smooth norm weights, the exact product has the
form

    M_r S_m Q_I = U^[-(r+m+z)/2] sum_n c(n) psi_u(n),

where n=d k product_i p_i and c(n) retains mu(d), the actual inverse/plain
annular profiles, and all original slot coefficients and supports. No
arbitrary residual coefficient is introduced. For X=U^(r+m+z), its support
lies in a fixed norm interval of size X. Because there are finitely many
slots and all coefficients are bounded by fixed smooth seminorms, ideal
divisor bounds give

    |c(n)| <<_epsilon X^epsilon.

The exact n=n' diagonal of the squared moment is therefore at most

    #C * X^(-1) sum_n |c(n)|^2 << #C * U^epsilon.

Since #C << U^(1+epsilon), this is << U^(1+epsilon), well below the desired
U^(1+delta m-1/5000+epsilon) on the entire hard length box. The smallest
delta m is (9/25)^2=81/625, which is much larger than 1/5000.

Even the universal sixth-power coincidences n=a b^6, n'=a c^6 have this
same harmless order after absolute values. Every ideal has a unique
sixth-power-free kernel a, and the number of pairs of ideals of norm at most
C X with the same kernel is

    << sum_{N(a)<=CX} (X/N(a))^(1/3) << X.

The last estimate uses elementary ideal counting. Divisor-bounded
coefficients add only X^epsilon. Fixed ray factors and zero-extension masks
can only reduce this absolute estimate. This covers a universal principal
part; it does not classify every principal or low-conductor term produced
by row stratification or Poisson transformation.

The remaining arithmetic object is the signed off-diagonal

    X^(-1) sum_{n,n' outside the discarded coincidences}
      c(n) conjugate(c(n'))
      sum_{u in C, theta(u)>2m-1/1000}
        psi_u(n) conjugate(psi_u(n')).                    (6)

Its coefficient retains the Mobius signs and the complete inverse/plain
convolution. The physical profile restriction and the actual row masks stay
inside the row sum. An upper bound of order
U^(1+delta m-1/5000+epsilon), uniformly in the required separating parameters,
would close this localized mixed-moment input. An absolute-value bound for
the modulus of (6) is sufficient but stronger than necessary; an upper bound
for its real part suffices because the complete moment is real and
nonnegative.

The rowwise detector parameters must still be handled by the source's fixed
Sobolev/profile calculus. The displayed kernel identity is first made at
fixed parameters; it is not valid to hide separately chosen row heights in
one coefficient c(n). Derivatives introduce only the permitted seminorm and
height costs, and any proposed estimate for (6) must retain that uniformity.

## 5. Result and next arithmetic input

The source already supplies a mixed saving stronger than the requested
1/5000 on rows of primitive conductor Q_psi <= U^(2m-1/1000). Actual
simultaneous detector witnesses force Q_psi essentially at least U^(2m).
The exact and universal sixth-power diagonals are also harmless at the
requested scale. The unresolved estimate is therefore an off-diagonal
correlation on nearly saturated, large-conductor rows. Neither elementary
phase rigidity nor reinserting unused slots proves it.

This reduction is compatible with a separate restriction on the primitive
conductor of a column-pair ratio, but that conductor must be defined and
estimated independently. The strongest next formulation should impose both
restrictions while retaining the signed convolution coefficient in (6).

See the [combined mixed-moment reduction](MIXED_MOMENT_REDUCTION_20261008.md)
for the complete decomposition and current remaining signed estimate.
