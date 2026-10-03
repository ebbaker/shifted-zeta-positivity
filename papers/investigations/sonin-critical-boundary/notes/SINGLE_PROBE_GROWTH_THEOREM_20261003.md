# One prepared probe detects the full all-window obstruction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.
Internal research, not independent specialist refereeing. No literature
priority claim is made for the Laplace-transform argument or the resulting
Riemann-hypothesis criterion.

## 1. Result and scope

The polynomial probe already used in the
[translated-probe experiment](ALL_WINDOW_TRANSLATED_PROBE_CRITERION_20261003.md)
has an additional useful property: its transform cannot vanish at a
hypothetical zero of zeta off the critical line. Consequently, for this
**one fixed probe**, a global bound on the signed prime covariance is
equivalent to the full all-window positivity target. Even a subexponential
growth bound, or an appropriately weighted integral bound, suffices.

This strengthens the reduction from a complete family of probes and every
finite Gram matrix to one explicit scalar function. It does not prove the
required scalar bound. In particular, it identifies the exact strength of
the missing signed arithmetic estimate; it supplies no new unconditional
zero-free strip or all-window sign.

The pairwise conclusion below uses the special zeta transform of this
probe. It does not contradict the general fact that positive two-by-two
principal blocks do not imply positivity of arbitrary larger matrices.

## 2. The existing probe and its entire transform

Keep exactly the probe used in the outward experiment:

    h(x)=(1-16x^2)^8 for |x|<1/4, and h(x)=0 otherwise;
    g0=(-D^2+1/4)D h;    g=g0/||g0||_2;    ell=1/2.

Here D=d/dx. The zero extension of h is C^7, g0 is C^4,
and all derivatives used above agree with their distributional meanings.
The compact source lies in the logarithmic form domain. Its three
moments vanish by integration by parts. For example, the factor
(-D^2+1/4) kills the two exponential moments, and the derivative kills
the ordinary integral. Smooth exactly prepared approximations are
obtained by convolving h with compact smooth approximate identities
before applying (-D^2+1/4)D. Their supports remain in one fixed slightly
larger window and they converge in the form norm.

Write

    H(z)=integral h(x)e^(zx)dx,
    G(z)=integral g(x)e^(zx)dx,
    phi(u)=integral g(x)g(x+u)dx,
    Phi(z)=integral phi(u)e^(zu)du=G(z)G(-z).

Integration by parts gives the exact formula

    G(z)=z(z^2-1/4)H(z)/||g0||_2.                         (1)

Expanding the exponential, and integrating the even monomials against
(1-16x^2)^8, gives

    H(z)/H(0) = sum_(k>=0) (z^2/64)^k/[(19/2)_k k!]
              = 0F1(19/2;z^2/64).                        (2)

The series is entire and H(0)>0. Its zero-location property can be proved
directly, without assuming a special-function product representation.

**Lemma.** Every zero of H is purely imaginary and nonzero.

**Proof.** Let F(z)=H(z)/H(0), suppose F(z0)=0, and set y(t)=F(z0 t)
for 0<=t<=1. Termwise differentiation of (2) gives

    (t^18 y'(t))'=(z0^2/16)t^18 y(t),
    y(0)=1,    y'(0)=0,    y(1)=0.

Multiply by conjugate(y), integrate, and integrate by parts. The boundary
term at t=1 vanishes because y(1)=0; the one at t=0 vanishes by regularity
and the factor t^18. Thus

    -integral_0^1 t^18 |y'(t)|^2 dt
       = (z0^2/16) integral_0^1 t^18 |y(t)|^2 dt.          (3)

The integral on the right is strictly positive. The integral on the left
has strictly negative sign, since y cannot be constant with y(0)=1 and
y(1)=0. Hence z0^2 is strictly negative real, proving the lemma.

It follows from (1) that

    Phi(z) != 0 whenever Re z>0 and z != 1/2.             (4)

At z=1/2, Phi has a zero of order two: H(1/2)>0 and the corresponding
zeros of G(z) and G(-z) are simple. The same preparation gives double
zeros of Phi at z=-1/2 and z=0. No zero-location assumption about zeta
has entered the argument.

## 3. Exact Laplace identity for the signed arithmetic quantity

For r>=0 define, as in the existing note,

    M(r)=sum_(n>=2) Lambda(n)/sqrt(n) phi(log n-r).        (5)

The sum is locally finite because phi is supported on [-ell,ell].
It defines a continuous function, and the elementary bound
Lambda(n)<=log n gives M(r)=O((1+r)e^(r/2)). This estimate is only a
convergence bound; it does not have the strength required below.

The support choice ell=1/2<log 2 ensures that, for every n>=2, the whole
support of r -> phi(log n-r) lies in r>0. Therefore no finite-endpoint
correction appears in the exact identity

    integral_0^infinity e^(-sr)M(r)dr
       = -Phi(s) zeta'(1/2+s)/zeta(1/2+s),    Re s>1/2.  (6)

Indeed, change variables u=log n-r in each integral. Its value becomes
n^(-s)Phi(s). Summing uses the absolutely convergent logarithmic
derivative Dirichlet series. Absolute convergence justifies the exchange:
the same integral with |phi| is bounded by a fixed profile integral times
sum Lambda(n)n^(-1/2-Re s).

For the classical analytic input, see the
[logarithmic-derivative identity](https://dlmf.nist.gov/27.4.E12),
obtained by differentiating the absolutely convergent Euler product.
The meromorphic continuation and
[functional equation](https://dlmf.nist.gov/25.4) give the usual reflection
symmetry of the [nontrivial zeros](https://dlmf.nist.gov/25.10).

## 4. The single-probe equivalence theorem

Let Q be the arithmetic Weil form on the original three-moment source
space, and put C(r)=Q(g,tau_r g), q=Q[g]. The following are equivalent:

1. Q is nonnegative on every compactly supported original source.
2. The Riemann hypothesis holds.
3. q>=0 and |C(r)|<=q for every real r (all two-source translate Grams).
4. M is bounded on [0,infinity).
5. For every epsilon>0 there is a finite C_epsilon such that
   |M(r)|<=C_epsilon e^(epsilon r) for every r>=0.
6. For every epsilon>0,
   integral_0^infinity e^(-epsilon r)|M(r)|dr<infinity.
7. For every epsilon>0,
   integral_0^infinity e^(-2epsilon r)|M(r)|^2dr<infinity.

**Proof.** Under RH the established explicit formula expresses Q as a
sum of nonnegative zero samples, counting multiplicities; consequently
2 implies 1. This is the existing explicit-formula implication, not an
unconditional use of a positive zero-sampling measure. The form closure
described in section 2 extends the conclusion to g and each of its finite
translate combinations. Cauchy-Schwarz for a nonnegative sesquilinear
form then gives 1 implies 3.

For r>ell, the exact off-diagonal formula in the translated-probe note is

    C(r)=-M(r)+epsilon_g(r),
    |epsilon_g(r)| <= ell e^(-5(r-ell)/2)
                           /(1-e^(-2(r-ell))).           (7)

In particular the correction is bounded on r>=ell+1 and tends to zero.
Condition 3 therefore bounds M there; continuity handles the remaining
compact interval. This proves 3 implies 4. Boundedness immediately gives
5, 6, and 7. Condition 5 implies 6 by choosing a growth exponent smaller
than the desired integration exponent. Condition 7 implies 6 by
Cauchy-Schwarz, for example

    integral e^(-delta r)|M(r)|dr
      <= (integral e^(-delta r)|M(r)|^2dr)^(1/2)
         (integral e^(-delta r)dr)^(1/2).

It remains to prove 6 implies 2. Condition 6 makes the left side of (6)
holomorphic on Re s>0: on a compact subset, use a smaller positive
exponential weight to dominate every differentiated integrand. The
meromorphic right side must coincide there with this holomorphic
extension. The zeta pole at 1 is harmless, since the double zero of Phi
at s=1/2 cancels the simple logarithmic-derivative pole.

If zeta had a zero rho of multiplicity m_rho with Re rho>1/2, put
s_rho=rho-1/2. By (4), Phi(s_rho)!=0, since rho is not the pole at 1.
The right side of (6) would have a genuine simple pole at s_rho with
residue

    -m_rho Phi(s_rho) != 0.                              (8)

This contradicts holomorphy. Thus no nontrivial zero lies to the right
of the critical line; reflection symmetry excludes those to its left.
This is RH. The argument requires neither simple zeros nor isolation of
a rightmost zero, and it does not assume any positivity of zero samples
before RH has been deduced. End of proof.

## 5. Quantitative growth consequences

The same proof gives a useful partial statement with one exponent. If

    integral_0^infinity e^(-a r)|M(r)|dr<infinity,

for some a>=0, then zeta has no zero with Re rho>1/2+a. More generally,
a bound |M(r)|<=C(1+r)^k e^(a r) gives the same conclusion by convergence
of the transform in Re s>a. When a=0 this already implies RH.

Conversely, every hypothetical zero rho with beta=Re rho>1/2 forces

    limsup_(r->infinity) log(1+|M(r)|)/r >= beta-1/2.      (9)

Otherwise an intermediate exponential rate would yield a holomorphic
Laplace transform at s=rho-1/2, contradicting (8). In particular, for
every 0<epsilon<beta-1/2, the weighted absolute integral in condition 6
diverges. An off-line zero cannot be hidden by cancellations among other
zeros in this transform: its local residue is nonzero, even if other
zeros approach farther-right vertical lines.

Equation (9) supplies no effective first violating separation, and no
lower bound valid at every large separation. Five certified values at
r=4,6,8,10,12 therefore remain exactly five finite tests.

## 6. What this changes in the proposed theorem

For general probes, the full family of translate Gram inequalities is
still the direct positivity criterion. For this specific polynomial probe,
the exact arithmetic structure makes global pairwise bounds sufficient:
they imply RH by (6), and then positivity of every original source by
the explicit formula. Arbitrary abstract covariance functions have no
corresponding implication.

The next arithmetic target can consequently be weakened to proving just
one of conditions 5--7 for the already tested M(r). Such a result would
settle the original all-window problem. The essential unresolved step is
still a global signed estimate; (6) shows precisely why ordinary positive
majorants of size e^(r/2) cannot provide it. Neither the transform identity
nor the zero-location lemma proves any of conditions 3--7 unconditionally.

The [continuation review](../reviews/ALL_WINDOW_OUTCOME_REVIEW_AND_CONTINUATION_20261003.md)
records separate same-model analytic checks. The [seven-source package](../numerics/single_probe_joint_20261003/README.md)
certifies one joint translate Gram with the same probe and original prime
cutoff. Neither finite numerical result is an input to the equivalence
proof above.
