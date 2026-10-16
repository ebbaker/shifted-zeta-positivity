# Structural audit of the marked moments and endpoint count

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

## Scope and conclusion

This is a focused audit of the parameter extension in
`papers/quasi-rh-character-amplification/notes/PARAMETER_EXTENSION_20261008.md`
against the September 30 source PDF, SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Source: <https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf>.

The audit inspected the actual statements and relevant proof steps in
Sections 8, 17.7, 18.1--18.2, 18.9, 19, and 20. It checked the moment
hypotheses, selected-slot coefficient classes, row exclusions, witness
widths, supply, and parameter quantifiers. It did not reproduce the full
canonical inverse recursion or two-transform fourth-moment induction,
verify the source's global theorem independently, or replay Lean.

**Finding:** there is no newly identified moment-domain obstruction to
using the source estimates at fixed `kappa=3/4` after assuming its
`beta_*<=7/8` theorem. The cited part of the argument does not require
`beta_*>7/8`. This is an extension of the *application* of the source's
stated lemmas, conditional on their validity. It is not independent
verification of those analytic lemmas.

The general geometry has no moment-side requirement that `ell=1/6` or
`b=1/8`. Its relevant supply requirement is
`ell/(h+zeta)>7/37`, with a fixed positive margin. A sharper exact endpoint
certificate is also available. It supports the selected geometry
`ell=1001/6000`, `b=1/8`, with candidate boundary
`sigma=20999/24000=7/8-1/24000`, subject to the separate low-side and
contour audits.

## 1. The fixed fourth-moment parameter is permitted

Lemma 18.1, source pp. 153--154, explicitly permits

    3/4 <= kappa <= 1.

For positive total selected prime length `z`, its condition is

    n1+n2+6*kappa*z <= M,

and when `kappa<1` its zero-free assumption is

    beta_* <= (1+kappa)/2.

Thus `kappa=3/4` is legal under the imported `beta_*<=7/8` theorem, including
at equality. One must not instead choose `kappa=2*beta_*-1` below `3/4`.
The original extension note makes this distinction correctly.

The proof confirms that the lower-bound contradiction in Part II is not
silently needed here. In Section 18.2, pp. 156--157, the prime estimate
uses `s_kappa=(1+kappa)/2 >= beta_*` and moves to `s_kappa+e`, with fixed
`e>0`. Equality at the boundary is harmless because the contour is
strictly to its right. Equations (18.12)--(18.16) use only the stated
compact interval for `kappa`; at its lower endpoint the inequalities
`6*kappa-1>=7/2` and `z<=2*M/9` remain valid. The final induction choices
in (18.52), p. 179, are explicitly uniform on `[3/4,1]`.

For zero selected slots, the lemma does not require a zero-free
hypothesis or a restriction on bounded plain lengths. This is important
near zero capacity and when a plain witness reaches length `1/2`.

## 2. Witness and row hypotheses survive the new contradiction

Section 8 assumes only `beta_*>51/100` (p. 55). Under a proposed boundary
near `7/8`, the contradiction `beta_*>sigma_new` meets this requirement.
The bin construction proves exactly

    a <= beta_*,   delta=2*a-1 <= 2*beta_*-1.

It does not need the supremum to be attained. Therefore the imported
`beta_*<=7/8` gives `delta<=3/4`. The actual witnessed bins have
`delta>1/50`; the floor bin `a=51/100` must continue to use the trivial
row count and must not be assigned an artificial witness.

Proposition 8.3 applies for every fixed `t` in `[1,3/2]`. Its inverse and
plain witnesses have one common row-character presentation, common
height, and a selected dyadic pair. The presentation and pair can vary
with the row; subdivision into finitely many presentations and
logarithmically many pairs is required before a moment is applied.
Separate rowwise smooth parameters are then allowed by the stated
Sobolev argument, with a fixed polynomial height cost.

For positive slots the fourth moment excludes inducing characters in
the finite fixed group `Theta`. Every sufficiently large retained
physical row has a prime outside the fixed set `S` with valuation from
1 through 5. At that prime the local character has order
`6/gcd(6,v_p(u))>1`. A fixed character supported on `S` cannot cancel it.
Thus these rows induce outside `Theta`. The finitely many rows supported
on `S`, including unit rows, belong to the outer-row treatment, not this
moment count. The same explanation is stated at the end of Section 18
and in Section 19.2.

## 3. The sixth-power amplification is uniform near inverse length one

Lemma 17.1 requires fixed strict margins

    r+2*z <= m-c1,
    2*r+8*z <= 3*m-c2.

It contains no global zero-free assumption. Searching its proof found
no use of `beta_*` or the Part II contradiction; its other occurrences
of beta and kappa are unrelated coefficient or length labels.

Lemma 17.6 gives the unmarked exponent on sixth-power-free rows

    e(r)=max(1,(1+5*r)/6).

The exact identity (17.90) retains every zero extension, and injectivity
of `(u,a) -> u*a^6` follows from sixth-power-free valuations of `(u)`.
These statements apply even when `u` and `a` share primes. No extra
coprimality condition should be inserted or omitted in using this
identity.

The proof of (19.3), p. 184, selects the preliminary amplification
parameter `c` and epsilon once for a bounded interval of `r`. It does
not let the strict margin in the marked estimate tend to zero as
`r -> 1`. Consequently the no-slot count

    #B << U^(e(r)-delta*r+epsilon)*(1+T1)^A

is uniform near `r=1`. For `r>=1` this becomes
`1-alpha+(alpha-delta)*r`, with `alpha=5/6`. Since here
`delta<=3/4<alpha`, the upper bound by the cutoff `t` is legitimate.

Remark 19.3, rather than a Proposition 19.3, is the source's explicit
statement that (19.3) can be used beyond the original bin ceiling when
the shared detector hypotheses hold. The present application needs
only the smaller ceiling `3/4`.

## 4. Reconstructing the selected count at kappa=3/4

The published Proposition 19.2 is situated under the original Part II
contradiction and includes a `Delta/4` loss. It cannot be quoted with
negative `Delta=beta_*-7/8`. Its proof must instead be repeated at the
permitted fixed parameter. This is what the extension note proposes.

At row width one the capacities are now exactly

    z_M(r)=(1-r)/2,
    z_P(m)=2*(1-2*m)/9.

Let `q` be mean prime amplitude, `x=q/delta`, and

    D_x = 3-17*x/9,
    P_x = (2-8*x/9)*(1-x),
    alpha = 5/6.

The comparison lines are

    A_I(r)=1-delta*(x+(1-x)*r),
    S_t(r)=1-delta*(4*x/9+(2-8*x/9)*(t-r)).

Their crossing is

    r_*(t)=((2-8*x/9)*t-5*x/9)/D_x.

For `0<=x<=1/2`, `1<=t<=3/2`, source pp. 184--185 gives

    23/37 <= r_*(t) <= 1,
    1/3 <= t-r_*(t) <= 1/2.

On the inverse side decrease the requested capacity by a fixed `nu0>0`.
Then `1-r-2*z>=2*nu0` and

    3-2*r-8*z = 4*(1-r-2*z)+(2*r-1).

The second width condition has margin at least `9/37` even before the
positive first term. The first margin is supplied by `nu0`.
The greatest requested inverse capacity is `7/37`; the plain capacity
is at most `2/27+O(epsilon)`.

No capacity-replacement penalty occurs at fixed `kappa=3/4`. Thus

    R_short(t)=1-delta+(delta*P_x/D_x)*(3/2-t),
    L(t)=1-delta+(alpha-delta)*(t-1),
    #B << U^(max(R_short(t),L(t))+epsilon)*(1+T1)^A.

At very small capacities the unweighted moments give `1-delta+O(nu0)`.
They replace the marked estimates; a shrinking strict margin is never
used. The selected coefficients are exactly the finite combinations
of fixed characters obtained after conjugating the entire product when
necessary. Their prime profiles include the physical Mellin twist.
There are no arbitrary row-dependent prime coefficients.

The short and long counts balance at

    J=(alpha-delta)*D_x+delta*P_x,
    t=1+delta*P_x/(2*J),
    R*=1-delta+(alpha-delta)*delta*P_x/(2*J).

For `0<=delta<=3/4`, `J>0` and `1<=t<3/2`; the live witnessed range has
strict inequality `t>1`. These are the exact usable exponents.

## 5. General slot lengths and target quantifiers

Nothing in the preceding moment argument fixes total physical length
`ell`. The weighted amplitude mean is

    q = sum(ell_i*g_i)/ell.

Greedy selection and rounding use this mean at row base `U=Z^d`, where
the slot lengths are `ell_i/d`. In the selected range `d>=1/2`, a mesh
with `2*ell_i` sufficiently small works uniformly. Fixed coefficients,
disjoint underlying windows, and every mask must remain as in the
physical expression.

The necessary supply margin is

    ell/(h+zeta) > 7/37.

The source's stronger comparison with `1/5` is a convenient numerical
choice, not an additional hypothesis of a moment lemma. For geometry

    lx=(1-ell-b)/2, ly=(1-ell+b)/2,
    h=(1+3*ell+b)/2,

positive supply at `d=h` is equivalent to `53*ell>7*(1+b)`. A sufficiently
small fixed positive `zeta` then preserves it.

The fourth-moment mesh is chosen before the fixed number of physical
slots; its independence of that number is part of Lemma 18.1 and its
explicit order of choices (18.52). Increasing the fixed slot count
changes eventual constants, thresholds, seminorms, and height orders,
not the pretarget real exponent mesh. Internal amplifier prime pools
remain separated from the physical windows by the strict mesh condition
in source pp. 195--196.

All real losses, capacity decrements, the slot system, bin width, and
extension `zeta` must be fixed before the target. Target-dependent
finite character sets, arithmetic exclusions, constants, thresholds,
and internal height orders are allowed. Only after those orders are
known is `T1=Z^(tau_eta)` chosen; the external tail order follows that
choice and may not change an internal height order. Source p. 186 and
Lemma 11.1 explicitly allow this arrangement. The proposed fixed-kappa
application preserves it. Claiming uniform implied constants over all
target conductors would be a stronger and unverified statement.

## 6. Selected geometry and exact endpoint certificate

The selected improvement uses

    ell=1001/6000, b=1/8,
    lx=4249/12000, ly=5749/12000, h=3251/4000,
    sigma=20999/24000=7/8-1/24000.

The exact identities `h=1-lx+ell`, `ly-lx=b`, and
`lx+ly+ell=1` hold. The signal remains `C(s)=s-11/16`; its value at the
new boundary is `4499/24000`, matching the proposed low exponent
`lx/2+b/12`. The change of `ell` is `e=1/6000`.

Set `y=1/2-x`, `0<=y<=1/2`, and

    D=(37+34*y)/18,
    P=(7+18*y+8*y^2)/9,
    J=(5/6-delta)*D+delta*P,
    T=(5/6-delta)*delta*P/J.

Then `R*=1-delta+T/2`. Direct substitution in source (10.15), using
`d=h`, `q=x*delta`, gives the general endpoint

    E = -1/4+5*ell/4+b/6
        -delta*(b/2+ell*y)+(1+3*ell+b)*T/4.

This was independently reconstructed from the original high exponent,
not assumed from the optimization script. Multiplication by `10368*J`
gives

    10368*J*(-E)=A(y)*delta^2+B(y)*delta+C(y),

where, in ascending powers of `y`,

    A=[306126/125, 786048/125, 564168/125, 192192/125],
    B=[-47352/25, -75386/25, -5204/25],
    C=[3663/10, 1683/5].

The coefficients of `D_poly(y)=4*A(y)*C(y)-B(y)^2` are

    [467172/625, 680072136/625, 3248881292/625,
     884272016/125, 1266754928/625].

All coefficients of `A` and `D_poly` are positive. More strongly, the
coefficient list of `A(0)*D_poly(y)-D_poly(0)*A(y)` is

    [0,
     41564108617776/15625,
     994303470901896/78125,
     1353403489129056/78125,
     387786619088928/78125].

It is coefficientwise nonnegative. Completing the square therefore
gives, for every real `delta` and every `y>=0`,

    A*delta^2+B*delta+C
      = ((2*A*delta+B)^2+D_poly)/(4*A)
      >= D_poly(0)/(4*A(0))
      =12977/170070.

On the application rectangle, `0<P<=D<=3` and `delta<=5/6` imply
`J<=5/2`. Consequently

    -E >= 12977/4408214400 > 1/400000.

This is a positive *uniform* margin established by exact rational
arithmetic and polynomial positivity, not by sampled values. The
coefficient construction and every displayed rational were independently
checked with a separate standard-library calculation.

A global monotonicity shortcut in `y` is not valid for every `delta`:
the endpoint derivative in `y` can be positive at small `delta`. The
full polynomial certificate avoids that issue.

## 7. Other high ranges and a quantified supply margin

Let `z0=17/50`. The general relative high exponent checked here is

    E(d)=a-sigma+h*(z0-1/6)-a*ly-ell/2+q*ell
         +d*(R+delta/2-z0),  a=(1+delta)/2.

Its direct evaluation gives these savings before adjustable losses:

| Range | Choice | Positive saving |
| --- | --- | --- |
| Floor | `delta=1/50`, `q=1/100`, `R=1`, `d=h` | `281/50000` |
| Intermediate | `delta<=3/4`, `q<=delta/2`, `R=76/75-2*delta/3`, `d<=1/2` | `59921/2400000` |
| Small rows | source outer-row estimate with conservative `2*d_min`, `d_min=1/100` | `15733/200000` |
| Principal w remainder | `ly/20` | `5749/240000` |
| Principal z remainder | `h/600` | `3251/2400000` |

For the intermediate row formula the exponent increases with `delta`,
so `delta=3/4` gives its maximum. Its frequency slope is
`101/150-delta/6`, at least `329/600`. For the adaptive range,
`R*>=1-delta` gives frequency slope at least `57/200`; the floor slope
is positive as well. Thus the endpoint in each row-length range really
bounds the entire range.

The slopes are less than two. Choose, for example,

    zeta=1/6400000.

Then extension from `h` to `h+zeta` costs at most `2*zeta`, less than
one quarter of the clean adaptive margin `1/400000`. The prime supply
satisfies exactly

    ell/(h+zeta)-1/5 =411197/78024015>0,
    1/5-7/37=2/185>0.

Hence this actual choice retains more than the required supply. A fixed
fine enough mesh meets both moment and whole-slot rounding conditions.
The large-row contour can then be chosen sufficiently far right exactly
as in source Lemma 10.6; its real choice precedes the target.

The new boundary exceeds `87/100`, so it lies in the expanded Euler
region already proposed in the first extension note. Verifying that
expanded region and the full low estimate belongs to the companion
structural audit. This note only checks compatibility of their supplied
geometry with the moment and high-exponent machinery.

For a contradiction `beta_*>sigma`, compare the high estimates with
`C(beta_*)` by subtracting the additional positive difference
`beta_*-sigma`. The exact certificate already gives a strict high
margin at `C(sigma)`, so this comparison improves it. The low estimate
requires its arbitrarily small exponent loss to be less than
`beta_*-sigma`. These choices depend on the global contradiction, not
on the target character, and therefore retain the continuation
principle's quantifiers.

## Remaining limitations

The audit supports the logical reuse of the stated moment estimates
and the exact arithmetic after that reuse. It does not validate the
source's canonical inverse recursion, centered fourth-moment induction,
reflection identity, automorphic inputs, or global seven-eighths theorem
from first principles. Those remain substantial imported dependencies.
The proposed lower boundary also requires the separate low-side and
Euler/contour-domain checks; this note does not replace them.
