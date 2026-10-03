# A finite low-band certificate for local prepared Weil coercivity

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and inherited effort label are not
exposed to this agent and are not inferred. Status: the outward certificate passed at 192 and 256 bits. The proof below
includes every omitted source mode and the quadrature error. Internal
same-model audits checked the derivation and implementation; specialist
review remains outstanding. The floating matrix center is only a diagnostic.

## 1. Source class and target

Let I=(-1/2,1/2) and use Fourier transform Fhat(t)=integral F(x)e^{-itx}dx.
We work on the closed subspace E of L2(I) specified by

    integral F(x) dx = integral e^{x/2}F(x) dx
                     = integral e^{-x/2}F(x) dx = 0.

For smooth compact F this is precisely pole neutrality plus zero mean; the
preparation theorem supplies F=(-d²/dx²+1/4)h with the same support and
integral h=0. Both parity sectors and arbitrary complex sources are retained.

Only the prime-power delay a=log 2 lies inside the correlation support.
Consequently the complete arithmetic form is

    Q[F]=integral_R q(t)|Fhat(t)|² dt/(2 pi),
    q(t)=gamma(t)-c cos(a t),
    c=sqrt(2)log 2,
    gamma(t)=Re psi(1/4+it/2)-log pi.                       (1)

There is no sum over zeros in this calculation.

The certified lower bound is

    Q[F] >= (9/100)||F||².                                (2)

The following proof reduces (2) to explicit outward inequalities for one
finite matrix and a few scalar constants. It does not assume Sonin positivity.

## 2. Negative part of the multiplier

Set lambda=1, T=46 and w(t)=(1-q(t))_+. The digamma series gives

    gamma(t)=gamma(0)+sum_{n>=0} 2t²/[lambda_n(lambda_n²+t²)],
    lambda_n=2n+1/2,

so gamma is increasing for t>=0. This follows directly from the convergent
partial-fraction expansion [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6).
An outward check of gamma(46)>1+c therefore proves w=0 for |t|>=46.

Let P_E be the exact orthogonal projection onto E, and v_t=P_E e^{itx}
on I. Define the positive bounded source-space operator

    D = integral_{-T}^T w(t)|v_t><v_t| dt/(2 pi).

For F in E, (1) gives

    Q[F] >= ||F||² - <F,DF>.                              (3)

The operator D commutes with real conjugation and additive reflection. On
real Legendre coordinates its even and odd diagonal blocks equal the positive
half-band integrals with factor 1/pi; cross-parity entries vanish.

## 3. Dimension-independent midpoint bound

Put h=1/1000, N=46000, t_i=(i+1/2)h. The source-space midpoint operator is

    D_mid=(h/pi) sum_i w(t_i) Re(|v_{t_i}><v_{t_i}|).

Since ||v_t||<=1 and ||v'_t||<=||x||L2(I)=1/sqrt(12), the total variation
of the operator-valued integrand is bounded by

    TV(w Re|v><v|) <= V0 + W/sqrt(3),
    V0=gamma(T)-gamma(0)+c a T,
    W=integral_0^T w(t)dt.                                (4)

Indeed w is absolutely continuous, |w'|<=gamma'(t)+c a|sin(at)| almost
everywhere, and the derivative of a rank-one outer product has norm at most
2||v||||v'||. No differentiability of the positive-part function at its zeros
is required. Composite midpoint integration for an absolutely continuous
Banach-valued function gives

    ||D-D_mid|| <= h/(2 pi) [V0+W/sqrt(3)].                (5)

For the scalar midpoint sum W_mid=h sum_i w(t_i), the same variation argument
gives |W-W_mid|<=h V0/2. The certified outward scalar caps are

    V0<40,  W_mid<22.5, hence W<23.                       (6)

The certified W_mid is about 22.241312. Equations (5)--(6) bound
the midpoint error by less than 0.00849.

## 4. Explicit full moment projection in Legendre coordinates

Use l_n(x)=sqrt(2n+1)P_n(2x), n>=0, an orthonormal basis of L2(I).
Let M=40 and P_M project onto n=0,...,39. Define

    m=4 sinh(1/4),
    n_s=sinh(1/2)-1/2,
    n_c=sinh(1/2)+1/2-m².

The three orthonormal constraint functions are

    u0=1,
    us=sinh(x/2)/sqrt(n_s),
    uc=(cosh(x/2)-m)/sqrt(n_c).

Their nonzero Legendre coefficients are

    (us)_n=sqrt(2n+1) i_n(1/4)/sqrt(n_s), n odd,
    (uc)_n=sqrt(2n+1) i_n(1/4)/sqrt(n_c), n even>=2,

with (uc)_0=0; i_n denotes the modified spherical Bessel function.
Thus these coordinates describe the FULL moment projection, not a projection
onto approximate finite constraint vectors.

For t>0 write s(t)=sin(t/2)/(t/2) and

    b_s(t)=2[(1/2)cosh(1/4)sin(t/2)
                   -t sinh(1/4)cos(t/2)]/(1/4+t²),
    b_c(t)=2[(1/2)sinh(1/4)cos(t/2)
                   +t cosh(1/4)sin(t/2)]/(1/4+t²).

The raw real parity coordinates of e^{itx} are

    p_n(t)=(-1)^{n/2}sqrt(2n+1)j_n(t/2), n even,
    p_n(t)=(-1)^{(n-1)/2}sqrt(2n+1)j_n(t/2), n odd.

Odd coordinates have a common factor i, which cancels within their Hermitian
outer products. The projected real coordinates are

    v_n(t)=p_n(t) -(us)_n b_s(t)/sqrt(n_s)
                     -(uc)_n [b_c(t)-m s(t)]/sqrt(n_c),
    v_0(t)=0.                                             (7)

The finite midpoint matrix D_M is therefore two real symmetric parity blocks,
with entries (h/pi) sum_i w(t_i)v_j(t_i)v_k(t_i) within each parity and zero
across parities. Formula (7) avoids errors from ill-conditioned finite Gram
inversions of the three nearly polynomial constraint functions.

## 5. All omitted source modes

Rodrigues' integral for Legendre polynomials, or the spherical-Bessel integral
[DLMF 10.54](https://dlmf.nist.gov/10.54), gives for real z

    |j_n(z)| <= |z|^n/(2n+1)!!.

For z>=0 the same integral gives

    |i_n(z)| <= e^z z^n/(2n+1)!!.

If z²<(2M+1)(2M+3), put

    tau_M(z)² = [(2M+1)z^{2M}/((2M+1)!!)²]
                  /[1-z²/((2M+1)(2M+3))].                (8)

The ratio of successive squared tail majorants is
z²/[(2n+1)(2n+3)], so (8) bounds the entire Legendre tail of the plane wave.
Since |<us,e_t>| and |<uc,e_t>| are at most one,

    ||(I-P_M)v_t|| <= tau_M(t/2)
       +e^{1/4}tau_M(1/4)[n_s^{-1/2}+n_c^{-1/2}]
       =: delta_M(t).                                     (9)

For M=40 and t<=46, an outward evaluation of (8)--(9) establishes

    delta_M(t)<5*10^{-6}.                                 (10)

The plane-wave term at t=46 is about 4.273503447*10^{-6}; the moment-vector
tails are much smaller. These estimates retain all omitted source modes.

Because both v_t and P_Mv_t have norm at most one, the rank-one difference
has norm at most 2 delta_M(t). Apply this directly to the midpoint sum:

    ||D_mid-D_M|| <= (2 delta_M/pi) W_mid <0.000072.        (11)

Alternatively one may truncate the exact integral first, obtaining the bound
2 delta_M W/pi<0.000074 and then applying (5) to its compression. Either
order gives, with the same finite matrix,

    ||D-D_M||<0.009.                                      (12)

## 6. Completed outward certificate and implication

The [certificate generator](../numerics/local_weil_gap_20261003/certify_local_weil_gap.py) and
[192-bit record](../numerics/local_weil_gap_20261003/certificate_192.json) establish

    D_M < (9/10) I.                                      (13)

The check uses outward LDL pivots of the two parity blocks of
(9/10)I-D_M. It does not infer a matrix sign from floating eigenvalues.
The largest floating eigenvalue, about 0.897046848491, is only a diagnostic.
The record also encloses the frequency cutoff and all scalar remainders:

- gamma(46)-1-c is greater than 0.01048;
- V0 is less than 38.619;
- W_mid is less than 22.242 and W is less than 22.262;
- the midpoint operator error is less than 0.008192;
- the omitted-mode error is less than 0.000061;
- the total operator error is less than 0.008253.

These rounded bounds follow from the rational endpoints in the record.
The generator tests the more conservative total budget of 0.01, so
(3) and (13) give Q[F] >= (9/100)||F|| squared on the entire specified
source space. The stronger recorded total error also verifies (12).
A [256-bit replay](../numerics/local_weil_gap_20261003/certificate_256.json)
passed the same strict inequalities. See the
[replay check](../numerics/local_weil_gap_20261003/replay_check.json) and
[internal review](../reviews/REVISED_B_CERTIFICATE_REVIEW_20261003.md).

The constraint set and support remain essential. This argument does not
prove the same constant without zero mean, at larger supports, or through
growing prime sets. Section 7 combines this result with an independent source-form bound for K.
It does not establish B >= the positive spectral part of the correction
merely by definition.


## 7. Consequence for the revised Sonin main term

The separate [source-form analysis](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md)
proves |K[F]|<=772||F|| squared using the inherited certified boundary gap.
Combining this with (2) yields

    Q[F] >= (9/77209) B[F] >= B[F]/9000,
    K[F] <= (77200/77209) B[F] <= (8999/9000) B[F].

Thus B_new=B/9000 is manifestly nonnegative and

    Q = B_new + [(8999/9000)B-K]

has a nonnegative remainder on this entire source class. This completes a
local relative comparison. It does not establish B>=K_plus for the unweighted
source correction operator, and it obtains the comparison using an independent
arithmetic lower bound rather than deriving that bound from Sonin geometry.
