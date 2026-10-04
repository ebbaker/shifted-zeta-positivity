# Internal audit: complete response and signed prime pairs

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Root derivation and separate agents
using the inherited model configuration checked the arguments. This is
internal same-model research, not independent specialist refereeing.

Reviewed the [complete response note](../notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md),
the [program overview](../notes/selective-loss-program/overview.md), and
the [signed decomposition package](../numerics/selective_loss_signed_pairs_20261003/README.md).
The scope is an exact reduction with a controlled diagonal cost.
The signed off-diagonal global bound is still open.

## 1. Causal identity and complete window

For a=1/4 and ell=1/2, p(y)=sum Lambda(n)/sqrt(n) g(y-log n)
vanishes below log 2-a>a. With y=x+r/2, oddness of g gives
w=(p(y)-p(r-y))/sqrt2. At y<=r+a every required log n is
less than r+2a, so this is the complete source window.

Direct expansion proves N=J(r+a)-(p*p)(r). The two overhangs
give the nonnegative term int_r^(r+a)p^2, and the remaining
term is half int_0^r[p(y)-p(r-y)]^2. This proves the lower
shell bound without presuming the sign of the reflected cross.
Cauchy--Schwarz gives N<=2J(r+a).

The auxiliary r<=ell range is used only to express all-r weighted
integrals. It does not assert unit normalization of the overlapping
source. The disjoint-cap boundary formula is explicitly restricted
to r>ell.

The exact odd projection removes only sinh(x/2), with squared
norm sinh((r+ell)/2)-(r+ell)/2. The moment coefficient is
[exp(-r/4)J_+-exp(r/4)J_-]/sqrt2. Every full individual
packet has both zero exponential moments; only delays in (r,r+ell)
contribute to the moment integrals. No terminal packet is discarded.

## 2. Diagonal and one-sided aggregate loss

At a fixed Y all prime powers with log n<Y+a are included.
The kernel K_Y is the actual integral over [0,Y]. For arithmetic
arguments u,v>=log 2, at least one full packet suffices to replace
the overlap by phi(u-v); the top-top block needs the truncated
polynomial integral. This qualification corrects a too-general
initial wording about arbitrary small u,v.

The exact identity D(Y)=int g(v)^2 A_2(Y-v)dv has no lower
boundary correction because log n+v>0. The explicit elementary
bound D<=(Y+a)^2(1+Y+a) follows from Lambda<=log n and the
harmonic sum. Ordinary PNT and partial summation imply
D=Y^2/2+o(Y^2); the contribution of higher powers to A_2 is
bounded. This is an asymptotic statement without an explicit
certified PNT remainder.

For J=D+Theta>=0, the lower bound Theta>=-D is automatic.
The required upper bound is on the aggregate scalar Theta_+.
It is taken only after every signed pair is combined. The resulting
bound

    X <= (C_Gamma+sqrt(2D)+sqrt(2Theta_+))^2

and the allowance obtained by multiplying its square root by
sqrt(a_*) follow from the already established positive-A
construction. A certified positive upper x for X supplies
epsilon=sqrt(x/A[F_r]); no sign assumption on Q or arithmetic
complement is inserted. This is a source-family allowance, not
an operator-monotone negative-part claim.

Individual positive pairs cannot replace the aggregate: a narrow
complete interior prime block has phi bounded below by a positive
constant and squared coefficient sum of order exp(Y). Its
polynomial diagonal is negligible. Thus positive off-diagonal
mass is exponentially large even away from a boundary cutoff.

The complete continuum Gram integrates to a fixed cap norm after
signed cancellation. It is different from the quadratic smooth
diagonal model D_0 in the numerical record.

## 3. Prime insertion and higher-power reduction

At fixed Y, different powers of the same base prime have disjoint
g packet interiors. The exact self energy of adding that prime is
at most (log p)^2/(p-1), and its cumulative cost is polynomial.
The full old/new cross remains in the exact insertion identity.
Its direct iterative Cauchy majorant costs exponentially.
No first-order prime-place cancellation law is proved.

For the linear causal signal, prime squares have a zero continuous
main because int g=0; PNT makes their response o(1). Powers
k>=3 have total O((1+y)exp(-y/6)). Hence the full higher-power
response is bounded and o(1). The two comparisons
J<=2J_prime+O(Y) and its reverse are unconditional.
This reduction does not permit omitting powers from an exact
finite response without separately using their correction bound.

## 4. Weighted coercivity and transform limitations

Tonelli gives

    I_epsilon >= (exp(2epsilon a)-1)J_epsilon/(2epsilon)

even before convergence is known. If J_epsilon is finite,
Cauchy--Schwarz makes P(2epsilon) absolutely convergent and
Fubini gives

    I_epsilon = exp(2epsilon a)J_epsilon/(2epsilon)
                -P(2epsilon)^2.

The subtraction is an ordinary square at a real Laplace argument.
The vertical line in the Plancherel formula instead has real part
epsilon. Both distinctions were checked.

The reverse coercivity is for unprojected N. A causal exponential
mode can be hidden by sinh-moment projection. The note supplies
an explicit generic counterexample and uses the actual arithmetic
transform, rather than geometry, for the projected RH implication.

With the minus-transform convention,
G(s)=s(1/4-s^2)H_h(s)/sqrt(nu) and
P(s)=-G(s)zeta'(1/2+s)/zeta(1/2+s) initially for Re s>1/2.
The pole at s=1/2 cancels. The probe theorem excludes cancellation
at any off-critical zero in the right half-plane.

The full linear explicit formula retains both nontrivial and trivial
zeros, their negative residue signs, and multiplicities. It includes
both imaginary signs with no extra factor two. Canonical constants
multiply g(y) and vanish for y>a; the pole term is zero by preparation.
Sixth distributional-derivative decay and the standard zero count
justify the smoothed sums. RH is invoked only for the converse,
where the nontrivial exponentials have modulus one.

Polynomial cumulative J and all-positive-weight finiteness
therefore have exactly RH strength. They have not been proved
unconditionally. Meromorphic continuation of the zeta expression
alone gives no small-weight energy bound. On a smaller-weight
Plancherel line, assuming only J_epsilon finite supplies L2
Fourier/Hardy boundary values; it need not supply an absolutely
convergent Laplace integral on that line.

Primary inputs were checked against the
[Euler and canonical products](https://dlmf.nist.gov/25.2),
[digamma series](https://dlmf.nist.gov/5.7.E6), and
[classical PNT statement](https://dlmf.nist.gov/25.16.E3).
The fixed-probe noncancellation and zero-count input were already
documented in the linked prior notes. No priority claim is made.

## 5. Complete boundary Gram

The signed-measure Gram is
K_r(u,v)=<f_u,f_v>-m(u)m(v)/d_r.
At each finite window its double integral is justified by finite
total variation. K_r is a positive-semidefinite Gram kernel,
but its individual values can have either sign.

If either delay is <=r, its packet is fully prepared, giving
phi(u-v)+phi(u+v-r). Only the upper-upper square requires
truncation and projection corrections. The explicit top moment

    [-2sinh(L/4)h''(a-t)+cosh(L/4)h'(a-t)]/sqrt(2nu)

was checked from the two exponential antiderivatives. It vanishes
at both layer endpoints. The top/interior cross near zero has
no prime atoms but does have continuum density; the latter
cannot be removed from the discrepancy Gram.

## 6. Numerical replay and practical limits

The root replayed the whole floating package with the existing
NumPy dependency and single-threaded numerical backend.
It evaluates r=2,...,10 with every active prime power and every
polynomial/cap breakpoint. At r=10 there are 3932 powers and
12931 pieces. Runtime was about 3.32 seconds in the root replay.
No large pair matrix or data cache is generated.

The 16-node rule integrates degree-30 pieces exactly in ideal
real arithmetic. Actual logarithms and floating operations
are not outward-enclosed. Order 24 comparisons and separate
moment orders 24/32 check numerical stability only.

- Maximum relative raw-order difference: about 7.64e-15.
- Maximum causal identity residual across both polynomial orders:
  below 1.8e-13.
- Root check of the explicit cap-moment formula against the independent
  Gauss32 evaluation: maximum absolute difference below 7.1e-15.
- All five r=2,...,6 projected norms match the earlier implementation
  within 2e-12.
- The saved source SHA-256 matches the record; the replay reproduces
  all numerical result rows, with only runtime metadata varying.

At r=10, D=51.0029784 and Theta=-37.1107177 give J=13.8922607.
The reflected convolution is positive there, 4.81461604, while it
is negative at the earlier sampled separations. The complete
projected response is about 9.07756966. These are bounded-range
arithmetic measurements, not a fitted global growth law.

Neither A inverse, Sonin B inverse, X, a safe complement, nor an
outward selective-loss certificate was computed. The outstanding
analytic obligation is a polynomial upper signed-pair estimate,
a local prime-signal energy bound, or the sharper dual bound.

Repository checks retain the requested note/numerics/review organization,
small files, and metadata. The manuscript and draft history are preserved;
no snapshot, commit, push, or synced-source edit is part of this work.
