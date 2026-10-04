# Causal arithmetic Gram cancellation and the complete discrepancy

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and configured reasoning effort are not
exposed and are not inferred. Same-model analytic derivation and floating
pilot, not independent specialist refereeing. No uniform loss estimate,
outward enclosure, or arithmetic positivity claim.

## 1. Exact causal decomposition of the complete response

Keep the real odd normalized prepared probe g, support radius a=1/4,
source diameter ell=1/2, and phi(u)=int g(x)g(x+u)dx. Define the locally
finite causal response on the whole real axis by

    p(y)=sum_(n>=2) Lambda(n)/sqrt(n) g(y-log n).

It vanishes for y<=0 because log2>a. At outer separation r>ell, put
L=r+ell and Y=r+a. On the centered source interval I=(-L/2,L/2), the
complete arithmetic response is exactly

    w_r(x)=[p(x+r/2)-p(r/2-x)]/sqrt2.                (1.1)

This uses oddness of g. Every contributing prime power has log n<L;
there are no omitted outward packets. With y=x+r/2, the integration
interval becomes (-a,Y), which is invariant under y->r-y. Since p is
causal,

    J(Y)=int_0^Y p(y)^2dy,
    C(r)=int_0^r p(y)p(r-y)dy=(p*p)(r),
    N(r)=||w_r||_I^2=J(Y)-C(r).                    (1.2)

C may have either sign. Reflection and Cauchy--Schwarz give

    |C(r)|<=J(Y),   0<=N(r)<=2J(Y).               (1.3)

The odd prepared-source projection removes precisely s(x)=sinh(x/2).
If m(r)=int_I s(x)w_r(x)dx and d_s=sinh(L/2)-L/2, then

    R_ar(r)=N(r)-M(r),   M(r)=m(r)^2/d_s>=0.        (1.4)

M in this fragment is a moment subtraction, not the earlier scalar
prime covariance M_g. No source inverse is involved in (1.1)--(1.4).

## 2. Diagonal and signed off-diagonal Gram terms

For u_n=log n and c_n=Lambda(n)/sqrt(n), let

    Gamma_Y(u,v)=int_0^Y g(y-u)g(y-v)dy.

The exact finite causal Gram is

    J(Y)=sum_(n,m)c_n c_m Gamma_Y(u_n,u_m)
        =D(Y)+Theta(Y),
    D(Y)=sum_n c_n^2 Gamma_Y(u_n,u_n),
    Theta(Y)=sum_(n!=m)c_n c_m Gamma_Y(u_n,u_m).     (2.1)

All active prime powers occur in these sums. Theta retains signed pair
correlations. This is not a sum of absolute pair contributions.

Putting A2(t)=sum_(log n<=t) Lambda(n)^2/n, with A2(t)=0 for t<log2,
the lower endpoint never clips an individual profile. Changing variables
therefore gives the useful exact diagonal identity

    D(Y)=int_(-a)^a g(v)^2 A2(Y-v)dv.              (2.2)

Ordinary PNT yields A2(t)~t^2/2. Indeed the prime term is
int_2^(exp t) (log x)/x dtheta(x)~t^2/2 by partial summation;
the m>=2 prime-power square weights have a finite total sum.
Since ||g||=1 and v ranges over a fixed compact interval,

    D(Y)~Y^2/2.                                  (2.3)

There is also an elementary explicit polynomial majorant:

    D(Y)<=A2(Y+a)<=(Y+a)^2(1+Y+a),                (2.4)

using Lambda(n)<=log n and the harmonic-sum bound. This estimate is crude
but does not depend on a prime-counting error theorem.

The smooth diagonal model replaces A2(t) by t^2/2. Its exact value is

    D0(Y)=Y^2/2+mu2/2,
    mu2=int v^2 g(v)^2dv.                         (2.5)

Oddness of g makes g^2 even and removes the linear v term. This model
is a diagonal reference, not the squared norm of the complete continuum
response. Ordinary PNT alone is not being used to claim that the actual
D-D0 is bounded or has a particular secondary asymptotic.

## 3. Only an upper bound on the signed off-diagonal term is needed

Because J>=0, the lower bound Theta>=-D is automatic. A global bound

    Theta(Y)<=C(1+Y)^m                            (3.1)

would give a polynomial J through (2.4), hence a polynomial R_ar via
(1.3)--(1.4). The existing special-probe criterion then gives RH.
Only the upper signed aggregate needs control; no two-sided absolute
pair estimate is required. Conversely polynomial J implies an upper
polynomial Theta, since Theta<=J.

This identifies a genuine cancellation target. It does not prove (3.1),
and it does not assert that polynomial J is equivalent to polynomial
R_ar without another comparison: reflected and moment cancellations
could make R_ar smaller than J.

### Absolute off-diagonal pair bounds are exponentially large

This can be proved unconditionally. Since phi(0)=1, choose h>0 small
enough that phi(v)>=c>0 for |v|<=h. Fix b>a+h. Restrict primes to

    Y-b<=log p<=Y-b+h.

For large Y both profiles lie wholly in (0,Y), so Gamma_Y(u,v)=phi(u-v)
and every pair in this narrow band has Gamma_Y>=c. PNT and partial
summation give

    sum_(band primes) (log p)/sqrt p
       ~2 exp((Y-b)/2)(exp(h/2)-1).

Thus the absolute off-diagonal pair sum over this band alone is at least

    c[(sum_(band)c_p)^2-sum_(band)c_p^2]
       >=c' exp(Y)                               (3.2)

for sufficiently large Y; the diagonal being subtracted is only O(Y^2).
The lower bound concerns absolute pair mass, not the signed Theta.
Accordingly taking absolute values of individual correlations destroys
the desired polynomial scale before the reflected or moment terms can
help. The support choice places these profiles below the upper cap, so
this is not an artifact of the complete-window boundary.

## 4. The complete projected discrepancy Gram

On 0<=u<=L define the signed weighted discrepancy measure

    dmu(u)=sum_(log n<L) Lambda(n)/sqrt n delta_(log n)(du)
                                       -exp(u/2)du,

and the full odd packet

    b_(r,u)(x)=[g(x+r/2-u)+g(x-r/2+u)]/sqrt2.

Let alpha_r(u)=int_I sinh(x/2)b_(r,u)(x)dx. The exact prepared-projected
Gram kernel is

    K_r(u,v)=int_I b_(r,u)(x)b_(r,v)(x)dx
                              -alpha_r(u)alpha_r(v)/d_s.    (4.1)

This is a positive-semidefinite Gram kernel, but individual entries need
not be nonnegative. The full projected discrepancy energy is exactly

    ||P_H e_r||^2=int_0^L int_0^L K_r(u,v)dmu(u)dmu(v),
    e_r=w_r-w_(0,r).                              (4.2)

It includes all atomic, atomic-density, density-density, reflected, and
moment terms. Expanding the signed measure before any absolute estimate
is essential.

For the complete continuum caps established in note 03, let
c0=917180/580421327, m0=int_I sinh(x/2)w_(0,r)(x)dx, and
B0=int_I w_r(x)w_(0,r)(x)dx. Then (4.2) is equivalently

    ||P_H e_r||^2
      =D+Theta-C-2B0+c0-(m-m0)^2/d_s.             (4.3)

The continuum norm c0 is constant, even though the diagonal model D0
grows quadratically. These are distinct references. Equation (4.3)
does not replace the complete window by a sharp cutoff at r.

## 5. What the pilot actually measures

The companion script evaluates D, Theta, C, the full moment subtraction,
and (4.3) at r=2,...,10, using every polynomial support breakpoint and
every active prime power. It computes aggregate responses and diagonal
squares rather than storing a large pair Gram matrix.

At r=10 the floating values are

    D=51.0029784,   Theta=-37.1107177,
    J=13.8922607,   C=4.81461604,
    M=0.0000749876, R_ar=9.07756966.

The signed direct off-diagonal term cancels about 72.8% of the diagonal
there. The reflected cross C is negative at r=2,...,9 and positive at
r=10, so it cannot be replaced by a presumed favorable sign. Moment
projection removes little at these samples. Continuum centering changes
the projected norm only modestly in this bounded range, as its cap norm
is small. The records retain that term exactly in the floating calculation.

These are measurements of actual cancellation in a finite arithmetic
vector. They are not a fitted growth law, a uniform interval statement,
or a proof of (3.1). No compressed inverse or dual energy X is computed.
