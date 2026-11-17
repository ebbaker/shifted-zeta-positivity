# VCD-GT-E09 — Tensor evaluation bounds for the fixed signed-cost certificate

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. E09 helper dispatch
**gpt-6.1-sol / ultra**. Lead actual settings and separate backend
attestation are unavailable. Proof-author checks are internal.

**Proved in-note within the stated enclosure premises.**
[Decision05](../brainstorm/notes/05_VCD_GT_B05_UNIFORM_SIGNED_CERTIFICATION_20261116.md)
sets a single fixed local quantitative application and its direct
endpoint comparator. The continuous-domain certificate below uses the
existing complete-field sample grid. It has finite geometry, denominator
and numerical success tests. See the
[frozen E09 r1 request](../research-progress/handoffs/VCD-GT-E09-r1.md),
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Auxiliary radius-five bound

Use \(a=140101/10,\ w=z-a,\ q=\sqrt t,\ t\in[0,1/10]\), and
\(G_t=e^{\pi a/8}H_t\). On \(|w|\le5\) and for real \(r\), set
\(s_0=(1+i(z+2iqr))/2\), reflect \(s_0\) if necessary to \(s\)
with \(\Re s\ge1/2\), and put \(\omega=s/2=X+iY\). Then
\[
 \tfrac14\le X\le\tfrac32+\tfrac4{25}|r|,\qquad
 \left||Y|-\tfrac a4\right|\le\tfrac54,\qquad
 3501<|Y|<3504.
\]
Indeed \(X=1/4+|\Im z/4+qr/2|\) and
\(|Y|=|\Re z|/4\). Hence
\[
 1<|\omega|\le3506+\tfrac4{25}|r|,\qquad
 |s-1|\le|s|\le7012+\tfrac8{25}|r|.
\]
Use the proven Binet and Euler bounds in
[Note12 §2](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#2-a-uniform-strip-majorant)
with \(X\ge1/4,\ |\Im s|>7002\). These preserve the height exponential:
\[
 |\Gamma(\omega)|e^{\pi|Y|/2}
 \le\sqrt{2\pi}\,|\omega|^{X-1/2}e^{1/(12X)},\qquad
 |\zeta(s)|\le3|s|.
\]
Now \(e^{\pi a/8-\pi|Y|/2}\le e^{5\pi/8}<8\), since
\(5\pi/8<2\) and \((e^{1/3})^6<(7/5)^6<8\).
Thus the normalization \(H_0=\xi(s_0)/8=\xi(s)/8\) yields
\[
 |e^{-r^2}e^{\pi a/8}H_0(z+2iqr)|
 \le \frac{8\cdot3\cdot(3/2)\cdot3}{16}
 (7012+\tfrac8{25}|r|)^3
 (3506+\tfrac4{25}|r|)^{1+(4/25)|r|} e^{-r^2}.
\]
The prefactor at \(r=0\) is below \(10^{16}\).
Using \(\log(1+x)\le x\), its additional log-linear and log-quadratic
coefficients are bounded by
\[
 \tfrac4{25}\log(3506)+\frac{4/25}{3506}+\frac{3(8/25)}{7012}
 <\tfrac{131}{100},
 \qquad \frac{(4/25)^2}{3506}<\tfrac1{10000}.
\]
The rational check for \(\log(3506)<409/50\) is
\(\sum_{j=0}^{24}(409/50)^j/j!>3506\).
With \(\alpha=9999/10000,\ \beta=131/100,\ C_5=10^{16}\),
this gives the real-line integrand majorant
\(C_5\exp(-\alpha r^2+\beta|r|)\). Integrating it in the exact
Gaussian formula of [Note12 §1](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#1-complete-source-and-normalization)
and completing the square proves
\[
 \boxed{\quad |G_t(a+w)|\le M_5
 =\frac{2C_5}{\sqrt\alpha}\exp(\beta^2/(4\alpha)),
 \qquad |w|\le5,\quad 0\le t\le1/10. \quad}
 \tag{1}
\]
The radius five is for analytic bounds on the true field. The sample
oracle uses exactly the frozen radius-\(9/10\) data and its existing
error formula.

## 2. Fixed tensor polynomial

Let \(\rho=9/10\) be the spatial sample radius, \(R=21/20\) the
radius of the disk to enclose, and \(S=5\) the auxiliary Cauchy
radius. Let \(N=128,\ d=32,\ n=32\). Use
\[
 \omega_j=e^{2\pi i j/N},\quad
 x_l=\cos(\pi l/n),\quad t_l=(1+x_l)/20 .
\]
Here \(j=0,\ldots,N-1,\ l=0,\ldots,n\). An equivalent reversed
ordering of the time grid uses the same interpolant if its indexing
is consistent. Let \(\widehat F_{lj}\) be the chosen recorded sample
values with
\[
 \bigl|G_{t_l}(a+\rho\omega_j)-\widehat F_{lj}\bigr|\le\varepsilon_s
 \tag{2}
\]
for every \(l,j\). The uniform disk allowance \(\varepsilon_s\) covers
Note12's exact \(E_{1/4}\), arithmetic, and archive reconstruction of
the samples as applicable. The exact polynomial from the recorded
values is defined by
\[
 \widehat b_{l,k}=\frac1N\sum_{j=0}^{N-1}
                   \widehat F_{lj}\omega_j^{-k},\qquad
 P_l(w)=\sum_{k=0}^{d}\widehat b_{l,k}(w/\rho)^k,\qquad
 P(t,w)=I_n[P_l(w)](20t-1),
 \tag{3}
\]
where \(I_n\) interpolates the \(n+1\) values at \(x_l\).
Enclosing the coefficient arrays and evaluating them with outward
rounding encloses this exact mathematical \(P\). If evaluation uses
rounded coefficients as values, their discrepancy requires a separate
uniform allowance. For example, if the rounding disks of the coefficients
in \(\sum_{m,k}P_{m,k}T_m(20t-1)(w/\rho)^k\) have radii \(b_{m,k}\),
the additional uniform allowance on this domain is
\(\sum_{m,k} b_{m,k}(R/\rho)^k\).

At a fixed time \(t_l\) expand
\(G_{t_l}(a+w)=\sum_{k\ge0} a_{l,k} w^k\). Equation (1) and
Cauchy give \(|a_{l,k}|\le M_5/S^k\). The DFT of the exact field
samples satisfies
\[
 b_{l,k}=\sum_{m\ge0}a_{l,k+mN}\rho^{k+mN},\qquad 0\le k\le d.
\]
Absolute convergence justifies interchange with the finite root-of-unity
sum, and \(k<N\). The discrete coefficient error from (2) is at most
\(\varepsilon_s\). On \(|w|\le R\), the resulting three distinct errors
at every time node are bounded by
\[
 \begin{aligned}
 E_{\rm sample}&=\varepsilon_s\sum_{k=0}^d (R/\rho)^k ,\\
 E_{\rm alias}&=
 M_5\frac{(\rho/S)^N}{1-(\rho/S)^N}\sum_{k=0}^d (R/S)^k ,\\
 E_{\rm tail}&=M_5\frac{(R/S)^{d+1}}{1-R/S}.
 \end{aligned}
 \tag{4}
\]

The Lobatto interpolation operator has sup norm at most \(65\)
from arbitrary complex node values to the real interval \([-1,1]\).
To see this, let \(\sum{}'\) assign half weight at the two endpoints
and ordinary weight elsewhere. The cosine vectors
\(\cos(m\pi l/n)\) for \(0\le m\le n\) are orthogonal for the
primed sum over \(l=0,\ldots,n\), with squared norm \(n/2\) at the
interior mode numbers and \(n\) at \(m=0,n\). The cosine product identity
reduces the verification to the primed cosine sums, equal to half the
real full \(2n\)-root sum. Thus
\[
 I_n[f_l](x)=\sum_{m=0}^n{}'\gamma_m T_m(x),
 \qquad
 \gamma_m=\frac2n\sum_{l=0}^n{}' f_l\cos(m\pi l/n).
\]
The bound \(|\gamma_m|\le2\max_l|f_l|\) and \(|T_m(x)|\le1\)
actually give \(2n=64\), hence the convenient allowance \(65\).

For the separate true-field time remainder at any fixed \(|w|\le R\),
the exact PDE under the complete Fourier integral gives
\(\partial_t^{33}G_t=(-1)^{33}\partial_z^{66}G_t\).
Spatial Cauchy on the disk of radius \(S-R\) about \(a+w\) yields
\(\big|\partial_t^{33}G_t(a+w)\big|\le66! M_5/(S-R)^{66}\).
The monic Lobatto node product in \(x\) is
\[
 \prod_{l=0}^n(x-x_l)=2^{1-n}(x^2-1)U_{n-1}(x).
\]
The zeros give the product and the leading Chebyshev coefficient gives
the factor. For \(x=\cos\theta\),
\(\big|(x^2-1)U_{n-1}(x)\big|
=|\sin\theta\sin(n\theta)|\le1\), with continuity at the endpoints.
Thus the product in \(t\) has absolute value at most
\(2^{1-n}(1/20)^{n+1}\). Apply the real interpolation remainder to
the real projection of the function in the direction of its complex
error at the evaluation point. This gives the same absolute remainder
with the full derivative modulus, including for complex \(w\); at a
node the error is zero.

Combining (4), the interpolation norm and the true-field remainder gives
the uniform bound
\[
 \boxed{\quad
 |G_t(a+w)-P(t,w)|\le E
 =65(E_{\rm sample}+E_{\rm alias}+E_{\rm tail})+
 \frac{M_5\,66!}{33!\,(S-R)^{66}}\,2^{-31}(1/20)^{33},
 \quad |w|\le R,\ t\in[0,1/10].\quad}
 \tag{5}
\]
Add the stated rounding allowance for rounded coefficient values, if
used. The last term employs the PDE of \(G_t\) alone.
The use of \(M_5\) for the spatial coefficient decay pays the
degree-32 truncation at \(R=21/20\), in addition to the time remainder.
For scale, (1) is about \(3.07\cdot10^{16}\); (4)'s degree tail
is about \(1.67\cdot10^{-6}\) before amplification, and the time
remainder in (5) is about \(4.40\cdot10^{-20}\).
A sample allowance close to \(E_{1/4}\) gives total \(E\) of about
\(0.03124\). These decimals describe the exact formulas' scale.
The certificate uses outward-rounded bounds.

## 3. Count, collar and centered log

Use \(r_-=3/4,\ r_+=21/20\). For a common
\(\sigma\in\{+1,-1\}\), certify for every \(t\) and every boundary
point \(w\) with \(|w|=r_\pm\) that the ratio
\(V_t(w)=\sigma G_t(a+w)/w^2\) satisfies
\[
 \Re V_t(w)\ge m_\pm>0,\qquad |V_t(w)|\le M_\pm .
 \tag{6}
\]
For example, enclose \(\sigma P(t,w)/w^2\) on time-cell and angular-arc
products that cover these boundaries. Subtract \(E/r_\pm^2\) from
the lower real bound and add it to the upper absolute bound.
All interval arithmetic for \(P\), the arc values and the ratio
needs outward enclosures.

On each boundary the loop \(V_t\) has winding zero about zero since it
lies in the open right half-plane. The winding of \(G_t(a+w)\)
therefore equals two on each circle, by the factor \(w^2\).
The argument principle for the entire \(G_t\) gives count two in
the inner disk and count two in the outer disk. The annulus is
zero-free. The harmonic minimum principle gives
\(\Re V_t\ge\min(m_-,m_+)>0\) throughout the closed annulus.
The ratio is holomorphic off \(w=0\), so strictness on the compact
annulus also gives an open collar of it with positive real part. A
uniform extension follows on a compact time interval from the same
strict bounds and continuity. The branch
\[
 L(t,w)=\operatorname{Log}V_t(w)-\lambda
 \tag{7}
\]
with the principal log and fixed real \(\lambda\) is analytic and
single-valued there. Multiplication by \(\sigma\) and the real
centering preserve the derivative used in
[Note12 §4](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#4-contour-log-and-coordinate-errors).
They keep \(L\) conjugation symmetric.

On each boundary, (6) gives \(\Re\operatorname{Log}V_t\)
between \(\log m_\pm\) and \(\log M_\pm\) and the absolute imaginary
part at most \(\pi/2\). A conservative upper bound on the centered
log modulus is
\[
 B_\pm=\sqrt{\max\bigl(
       |\log m_\pm-\lambda|,\ |\log M_\pm-\lambda|
       \bigr)^2+(\pi/2)^2}.
 \tag{8}
\]
A single global real centering is sufficient. If directional bounds
are pooled across both boundaries, an example is the midpoint of
\([\log\min(m_-,m_+),\log\max(M_-,M_+)]\).
At a target-circle node the log in (7) can be enclosed from the
polynomial ratio enlarged by the disk of radius \(E/\rho^2\), using
the same branch and centering. The known positive real-part lower
bound can be intersected with that enclosure.

## 4. Angular tails and interval coordinates

For \(F\) analytic on a neighborhood of the closed annulus
\(r_-\le|w|\le r_+\), suppose \(\sup_{|w|=r_\pm}|F(w)|\le A_\pm\).
Let \(\langle F\rangle\) be its angular mean on \(|w|=\rho\) and
\(\langle F\rangle_N=N^{-1}\sum_{j=0}^{N-1}F(\rho\omega_j)\).
Expand in a Laurent series and apply Cauchy on the respective two
boundary circles. The positive powers \(k>0\) are bounded in
modulus at \(\rho\) by \(A_+(\rho/r_+)^k\) and the negative powers
\(-k\) by \(A_-(r_-/\rho)^k\). Both tails converge absolutely. Only
powers divisible by \(N\) contribute to the discrete mean, giving
\[
 \boxed{\quad|\langle F\rangle_N-\langle F\rangle|
 \le T_N(A_-,A_+)
 =A_-\frac{(r_-/\rho)^N}{1-(r_-/\rho)^N}
  +A_+\frac{(\rho/r_+)^N}{1-(\rho/r_+)^N}.\quad}
 \tag{9}
\]

Use \(p_k=\langle -k w^k L\rangle\) for \(k=1,2\), with
\(A_\pm=k r_\pm^k B_\pm\). On each paid interval of time, evaluate
the \(N=128\) node terms with the certified node log enclosures
and include (9) as an additive disk error. Taking the real part is
valid because \(G_t\) respects conjugation and the unordered pair
is conjugation invariant. From the resulting real moment intervals
propagate
\[
 \gamma=c-a=p_1/2,\qquad D=p_2/2-\gamma^2 .
 \tag{10}
\]
Use the same moment calculation at the two endpoint times for
the incoming and direct comparator intervals. These times are already
source sample times, so the node log enclosures there may use the
archive sample bounds (2) directly. The same collar and angular tails
still apply.

The actual \(Q=(w-\gamma)^2-D\) has both roots strictly inside
the inner circle by (6). In each time cell let
\(C_*\ge\sup|\gamma|\), \(D_*\ge\sup|D|\) from (10). A simple
usable denominator test on each radius \(r\) is
\[
 C_*<r,\qquad
 |Q|\ge q_r=(r-C_*)^2-D_*>0 .
 \tag{11}
\]
If this test is too weak, a verified lower bound from interval
evaluation of \(|(w-\gamma)^2-D|\) on the same radius using the
actual coordinate enclosures serves the same role. This is a sufficient
numeric denominator test. The analytic pole exclusion comes from
the counted inner disk. For example, a verified inner test of the
form (11) also supplies positive denominators on the larger radii
through the increasing lower bound.

Enclose
\[
 K(t)=\left\langle
         \frac{2w(w-\gamma)L(t,w)}{((w-\gamma)^2-D)^2}
       \right\rangle
 \tag{12}
\]
at each time cell by evaluating every node kernel with the interval
\(\gamma,D\) from (10). Use the same log enclosures as for the
moments and include (9) with
\[
 A_\pm=\frac{2r_\pm(r_\pm+C_*)B_\pm}{q_{r_\pm}^2}.
 \tag{13}
\]
The node evaluations also need nonzero denominators. They can use
a positive (11) at \(\rho\), a sharper bound using that interval,
or complex interval evaluation directly when the resulting domain
excludes zero. If an enclosing box for \(Q\) includes zero despite a
positive modulus floor, a validated reciprocal enclosure can use
\(\overline Q/|Q|^2\), with the squared floor as lower bound on the
denominator. The true kernel is analytic on the annulus used in (9),
since \(Q\)'s roots are strictly inside the inner circle. Its drift
is real by conjugation symmetry, so take the real part of the
resulting disk. All steps use enclosing intervals for the actual
coordinates, including when \(D\) contains zero. Using point
coordinates instead would require a separate coordinate transfer
allowance of the type proved in Note12 §4.

## 5. Certificate outputs and exact control

For the fixed \(u=0,\ v=1/10\), a certificate under Decision05 has
the following paid steps.

1. Check the input provenance and source/arithmetic sample errors.
   Build the prescribed tensor polynomial or coefficient enclosures
   and round (5) outwards on the disk and full time interval.
2. Verify (6) on both entire boundary circles across all geometry
   time cells with one common sign. Record the lower real-part floors,
   absolute ceilings and log centering. This supplies count two and
   a zero-free collar at every time.
3. Cover every time by the fixed permitted K interval mesh. For each
   interval, enclose the moments, actual coordinates and denominators,
   and use (9), (12) and (13) to enclose \(K\). A common upper endpoint
   \(k_U<0\) is certified only if every cell passes. An upper endpoint
   weaker than the target can be tested against the same exact cost
   inequality. Keep any failed gate and its stated mesh and domain.
4. Enclose the actual \(D(v)\) and \(D(u)\) by the same certified
   moment procedure using the same oracle information. Give the direct
   endpoint comparator its full interval and its lower endpoint, with
   its finite evaluation costs.

Let \(L_v\le D(v)\) be the incoming lower bound. For any real \(k\) put
\[
 B(k)=2\int_u^v e^{4k(v-t)}\,dt
 =\begin{cases}
 (e^{4k(v-u)}-1)/(2k), & k\ne0,\\
 2(v-u), & k=0 .
 \end{cases}
\]
This function is increasing. If step 3 pays \(K\le k_U<0\) then
\[
 \mathcal B\le B(k_U),\qquad
 W(u)\le e^{4k_U(v-u)},\qquad
 e^{4\int_u^v K}D(u)=D(v)-\mathcal B ,
 \tag{14}
\]
by the physical gap law and [Note12 §5](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#5-signed-primitive-time-cost-and-exact-control).
For a rigorously positive \(L_v-B(k_U)\), the same positive margin
holds against the whole tail cost at each \(t\in[u,v]\). It gives
the unweighted left-endpoint lower bound
\((L_v-B(k_U))/e^{4k_U(v-u)}\). Evaluate the cost and the weight upper
bounds outwards; use the lower numerator and upper positive denominator
in this endpoint comparison. If a lower drift bound \(k_L\) is also
certified, \(B(k_L)\le\mathcal B\). The absolute-cost comparator always
has \(\mathcal B_{\rm abs}\ge2(v-u)=1/5\). An upper \(D(v)<1/5\)
rules out strict success for that comparator on this tube. The
constant bound route requires only these exact cost evaluations,
without a time quadrature of \(K\).

For \(G_t(a+w)=w^2-2(t-1/20)\), put \(D_q=2(t-1/20)\).
Exact sample arithmetic gives tensor reproduction since the data
have spatial degree two and time degree one, and the spatial alias
identities used in (4) are exact finite identities. The field ratio
with \(\sigma=+1\) satisfies \(\Re V_t\ge1-|D_q|/r_\pm^2>0\).
The counted inner disk contains the double event.
The centered expansion
\[
 L(t,w)=-\lambda-\sum_{m\ge1}\frac{D_q^m}{m w^{2m}}
\]
gives \(p_1=0,\ p_2=2D_q\). The \(K\) kernel times this log has
strictly negative Laurent powers only, even with the constant
centering, hence \(K=0\). Equations (10)–(14) give
\(D(v)=1/10,\ D(0)=-1/10,\ W(0)=1,\ \mathcal B=1/5\).
The strict survival margin fails by \(1/10\) on the full interval
and is saturated starting at the double time. A finite interval
replay must enclose these exact values. For a paid negative sign of
the full control margin, the check is the upper \(D(v)\) minus
the lower cost \(B(k_L)\) being negative.

## 6. Control premises and scope

The exact quadratic passes count, collar and holomorphic-log gates,
and fails the strict incoming-cost test. The earlier quartic control
also has a local double event despite its favorable force sign and
small gap. Neither polynomial has the complete xi source. The
Euler-factor controls change the canonical arithmetic and completion.
Weighted-square controls fail the conjunction of full reflection and
unit coefficients; finite-tail and finite-score perturbations change
the canonical source even when retained data agree. Finite-prime
orbits fail full arithmetic/reflection. Reflected, smooth-shape and
positive-primitive controls lack unchanged theta square arithmetic.
Atomic and continuous finite-profile controls lack the full theta
profile and coefficients, with the recorded eventual-simplicity
failures. The RH-conditional endpoint control changes ordinary
Dirichlet arithmetic and retains its conditional premise. The varied
observation kernel changes the real cosine/Newman equation, and the
actual-profile relaxation lacks the complete integer zero divisor of
a specified analytic field. These verdicts use the established scoped
controls and the analytic screen of [Note12 §6](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#6-scope-and-control-screen).

The method can accept a particular collision-free contour tube of
another field when all its inputs are paid. Any qualifying tube
starting at a collision uses the full incoming gap in the exact
cost, by (14). The known-pair Lehmer success condition is the local
inequality \(L_v>B(k_U)\) with the stated continuous-domain payments.
The root count, denominator, numerical and cost outcomes of that
test belong to the fixed acquisition packet.
