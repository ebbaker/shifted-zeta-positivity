# Weighted prime energy and the sharp cutoff boundary

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Internal research with same-model
checking, not independent specialist refereeing.

This continuation attempts the weighted square-integrability condition in
the [single-probe theorem](SINGLE_PROBE_GROWTH_THEOREM_20261003.md). It gives
an exact finite prime-pair formula and identifies a substantial truncation
error: sharply truncating the primes does not approximate the full smoothed
sum in the desired weighted L2 spaces. The defect is present unconditionally
and comes from the continuous prime main term at the cutoff. No global
growth estimate is proved here.

## Definitions and a finite prime-pair identity

Keep the exact normalized real polynomial probe g and its real even
autocorrelation phi, supported on [-ell,ell], ell=1/2. Write

    Phi(s)=integral exp(su)phi(u)du,
    M(r)=sum_(n>=2) Lambda(n)n^(-1/2)phi(log n-r),
    M_X(r)=sum_(2<=n<=X) Lambda(n)n^(-1/2)phi(log n-r).

The preparation gives Phi(1/2)=0, and the mean-zero condition gives
Phi(0)=0. For epsilon>0 define

    K_epsilon(d)=integral exp(2epsilon u)
                         phi(u+d/2)phi(u-d/2)du.

This kernel is real, even, continuous, supported on [-2ell,2ell], and is
the autocorrelation of u -> exp(epsilon u)phi(u). In particular it is
positive definite, but its individual values need not be nonnegative.
For every finite X, exact expansion and a change of variable give

    integral_0^infinity exp(-2epsilon r) M_X(r)^2 dr
      = sum_(2<=n,m<=X) Lambda(n)Lambda(m)
             (nm)^(-1/2-epsilon) K_epsilon(log(m/n)).      (1)

Indeed let c=(log n+log m)/2, d=log(m/n), and u=c-r in the integral of
one product. The exponential contributes exp(-2epsilon c)=(nm)^(-epsilon),
and the two correlation arguments become u-d/2 and u+d/2. Both profiles
are supported in positive r because ell<log2, so the lower endpoint causes
no correction. All interchanges here are finite.

The diagonal part of (1) is

    K_epsilon(0) sum_(2<=n<=X) Lambda(n)^2 n^(-1-2epsilon), (2)

and is bounded as X grows for every epsilon>0. The elementary majorant
Lambda(n)<=log n already proves this. This diagonal estimate does not
bound the full energy: the off-diagonal signed terms must also be handled.

## Absolute prime-pair bounds diverge at the relevant weights

The absolute double series obtained from (1) by replacing K_epsilon by
its absolute value diverges whenever 0<epsilon<=1/2.

To see this, K_epsilon(0)=integral exp(2epsilon u)phi(u)^2du>0. Choose
c>1 sufficiently close to one that K_epsilon(d)>=k>0 for
|d|<=log c. PNT and partial summation on n in [Y,cY] give

    sum_(Y<n<=cY) Lambda(n)n^(-1/2-epsilon)
       ~ integral_Y^(cY) x^(-1/2-epsilon)dx.

For epsilon<1/2 this has size Y^(1/2-epsilon); for epsilon=1/2 it
tends to log c. Therefore the block with both n,m in [Y,cY] contributes
at least a positive constant times Y^(1-2epsilon), or a positive constant
when epsilon=1/2. Taking disjoint growing multiplicative blocks proves
divergence. The diagonal subseries (2) remains convergent.

The same compact kernel retains the exact centered cancellation

    integral exp(bd)K_epsilon(d)dd
       =Phi(epsilon+b)Phi(epsilon-b),                    (3)

by the substitution x=u+d/2, y=u-d/2, whose Jacobian has absolute value
one. At b=1/2-epsilon, the right side vanishes by Phi(1/2)=0. Thus the
positive continuous main density cancels only after the signed kernel is
retained. Absolute pair estimates discard that cancellation.

The PNT input is the classical asymptotic for the von Mangoldt measure;
see [DLMF 27.12](https://dlmf.nist.gov/27.12). No unproved prime-pair
correlation estimate is invoked in this divergence argument.

## A stronger obstruction from the artificial last smoothing window

Define the continuous partial profile

    F(a)=integral_(-ell)^a exp(u/2)phi(u)du,  -ell<=a<=ell,

extended by zero for a<=-ell and a>=ell. This extension is consistent
at the upper endpoint because F(ell)=Phi(1/2)=0. The function F is not
identically zero, since F'(a)=exp(a/2)phi(a) and phi(0)=1.

**Proposition.** Uniformly for -ell<=v<=ell, as X tends to infinity,

    M_X(log X+v)/sqrt(X) -> exp(v/2)F(-v),
    M(log X+v)/sqrt(X)   -> 0.                            (4)

Consequently, for every fixed epsilon>0,

    X^(2epsilon-1) integral_(log X-ell)^(log X+ell)
       exp(-2epsilon r)|M_X(r)-M(r)|^2 dr
        -> c_epsilon
         := integral_(-ell)^ell exp((1-2epsilon)v)|F(-v)|^2dv
         >0.                                             (5)

**Proof.** PNT means the rescaled von Mangoldt measures X^(-1)dpsi(Xy)
converge to dy on every compact interval in y>0. At r=log X+v, the
rescaled truncated sum is the integral against this measure of

    y^(-1/2)phi(log y-v) 1_(y<=1).

For |v|<=ell all these tests are supported in one compact interval
bounded away from zero. Partial summation gives uniform convergence in
v: their smooth pieces and derivatives are uniformly bounded, and the
single jump at y=1 is controlled by the same uniform PNT remainder.
Endpoint atoms have size at most log X/X and tend to zero. The limiting
integral is

    integral_0^1 y^(-1/2)phi(log y-v)dy
      =exp(v/2) integral_(-ell)^(-v) exp(u/2)phi(u)du.

For the full sum remove the restriction y<=1. The same calculation gives
exp(v/2)Phi(1/2)=0, again uniformly. This proves (4). Put r=log X+v
in (5); uniform convergence on a compact interval proves the stated limit.
Its constant is strictly positive because F is not identically zero.
End of proof.

For 0<epsilon<1/2, the boundary contribution to the weighted squared
error therefore grows like c_epsilon X^(1-2epsilon). At epsilon=1/2
it tends to the nonzero constant c_(1/2). In particular sharp prime
cutoffs fail to converge to M in weighted L2 for every one of these
weights. The same leading asymptotic holds with |M_X|^2 in place of
|M_X-M|^2 on this last window.

This remains true if RH is assumed and M is bounded. Thus a proposed
proof seeking a uniform bound on the whole left side of (1), as X grows,
would be attempting a false assertion when epsilon<1/2. This is stronger
than merely observing that a particular absolute majorant is inefficient.

## Correct finite energy approximations

There is a direct way to avoid the spurious boundary. To compute

    E_epsilon(R)=integral_0^R exp(-2epsilon r)|M(r)|^2dr,

include every prime power n<=exp(R+ell) but integrate only over 0<=r<=R.
The sum is then exactly complete throughout the integration range.
The nonnegative quantities E_epsilon(R) increase to the desired weighted
energy as R tends to infinity. A uniform bound on these quantities would
prove the weighted criterion; no such uniform bound is presently available.

One may also subtract the explicit partial main term

    M_X(r)-exp(r/2)F(log X-r).

This agrees with M for r<=log X-ell and vanishes for r>=log X+ell.
It cancels the leading cutoff contribution in (4), but PNT only makes
the remaining transition error o(sqrt(X)). That is not sufficient to
control its weighted L2 norm for 0<epsilon<1/2. Further signed error
control is still required.

No numerical prime-pair sweep was launched. Equations (1)--(5) show why
the unrestricted finite prime-pair energy would answer the wrong question,
and give the correct finite integral for a future attempt. They do not
prove the global growth bound or RH.
