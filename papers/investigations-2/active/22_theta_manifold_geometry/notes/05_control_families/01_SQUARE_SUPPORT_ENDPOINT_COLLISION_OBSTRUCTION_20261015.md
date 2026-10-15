# Square-support constraints admit a collision even with the first source endpoint

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**; reasoning effort **ultra**. This is a bounded arithmetic applicability test for Investigation 22. It combines an analytic construction, a finite validated calculation, and independent replay. It is not a theta sign counterexample or an RH result.

## 1. Result and scope

The proposed square-lattice localizing hierarchy has a concrete limitation. There exist fixed strictly positive weights on the first three square nodes for which the corresponding complete finite source is positive on the physical half-line, obeys every square-support moment/localizing inequality at every order and every positive base parameter, and satisfies the first source reflection condition `Phi'(0)=0`, but its physical heat transform has a nondegenerate collision at

\[
T=\frac14,\qquad 44.1303<x_*<44.1304.
\]

A fixed positive rescaling additionally gives the exact primitive normalization

\[
\psi'(0)=\psi'''(0)=-\frac12,
\]

and therefore the same affine primitive reconstruction used for the actual theta source. The third odd source derivative is strictly negative, so the complete source reflection hierarchy is not retained. The construction can be perturbed analytically to give positive weights at every square node while preserving the collision and the displayed endpoint conditions; no explicit numerical perturbation radius is asserted.

Thus no certificate using only these support constraints, local Jacobi heat identities, period-two base symmetry, the first source endpoint, and the affine primitive normalization can establish the desired uniform chord sign or stationary collision-exclusion estimate for every member of that relaxed class. Additional coefficient coupling or the full modular/elliptic relation remains essential. This obstruction does not concern a certificate that already incorporates the complete reflection hierarchy or the actual equal theta weights.

## 2. Weighted square sources and their exact constraints

Set `lambda_n=pi*n²`, `q=e^(4u)`, and define the individual physical source modes

\[
\phi_n(u)=e^u(2\lambda_n^2q^2-3\lambda_nq)e^{-\lambda_nq},
\qquad
H_n(t,x)=\int_0^\infty e^{tu^2}\phi_n(u)\cos(xu)\,du.
\]

Every `phi_n` is strictly positive on `u>=0`, because `2 lambda_n q>3`. Every fixed derivative has double exponential decay there. For any fixed finite nonnegative weight sequence `a_n`, define

\[
\Phi_a=\sum_n a_n\phi_n,\qquad
H_a=\sum_n a_n H_n,\qquad
\psi_a=e^u\sum_n a_n e^{-\lambda_nq}.
\]

The transform is entire in `(t,x)`, is even in the spectral variable `x`, and satisfies `H_t=-H_xx`. Direct differentiation gives

\[
8\Phi_a=\psi_a''-\psi_a.
\]

Evenness of `H_a` in `x` is automatic from the cosine transform and must not be confused with evenness of the arithmetic source in `u`.

For any positive base parameter `q`, let

\[
M_k^a(q)=\sum_n a_n\lambda_n^k e^{-\lambda_nq}.
\]

If `P(lambda)>=0` at every square node and `V` is any real polynomial, then

\[
\sum_n a_n e^{-\lambda_nq}P(\lambda_n)V(\lambda_n)^2\ge0.
\]

This proves all ordinary moment-matrix inequalities, all adjacent-square localizing inequalities, and in fact every support-only nonnegative-polynomial constraint at every finite degree. In particular,

\[
\left[M^a_{r+s+2}-(\lambda_m+\lambda_{m+1})M^a_{r+s+1}
 +\lambda_m\lambda_{m+1}M^a_{r+s}\right]_{r,s=0}^d\succeq0
\]

for all `m>=1`, `d>=0`, and `q>0`. This is an exact analytic statement about the constructed measure, not a numerical eigenvalue test.

The weighted series

\[
\vartheta_a(z,\tau)=1+\sum_{n\ge1}a_n e^{\pi i n^2\tau}
 (e^{2\pi i nz}+e^{-2\pi i nz})
\]

also obeys `z -> z+1` periodicity, `tau -> tau+2` periodicity, and the Jacobi heat equation. Hence the local differential source identities and local covariant-jet recurrence also hold. The full elliptic multiplier under `z -> z+tau` is not retained when the coefficients differ. The counterexample is not a section of the original theta line bundle on its lattice quotient.

## 3. Impose the first source endpoint before searching for a collision

For a single mode, repeated source differentiation has the form

\[
\partial_u^k\phi_n(u)=e^u e^{-\lambda_nq}P_k(\lambda_nq),
\qquad
P_{k+1}(a)=(1-4a)P_k(a)+4aP_k'(a),
\]

starting with `P_0(a)=2a²-3a`. In particular,

\[
P_1(a)=-8a^3+30a^2-15a,
\]
\[
P_3(a)=-128a^5+1440a^4-4232a^3+3270a^2-375a.
\]

Write `d_n=P_1(lambda_n)`. One has `d_1>0`, `d_2<0`, and `d_3<0`. Put

\[
G_n=e^{\lambda_n}H_n,\qquad
b_2=-\frac{d_1}{d_2}>0,\qquad b_3=-\frac{d_1}{d_3}>0.
\]

For `0<theta<1`, consider the fixed-source family

\[
G_\theta=G_1+\theta b_2G_2+(1-\theta)b_3G_3.
\]

Its normalized source first derivative at zero vanishes **identically in theta**:

\[
d_1+\theta b_2d_2+(1-\theta)b_3d_3
=d_1-\theta d_1-(1-\theta)d_1=0.
\]

The equivalent raw square weights for `H_a=e^(-pi)G_theta` are

\[
a_1=1,\qquad a_2=\theta b_2e^{3\pi},\qquad
 a_3=(1-\theta)b_3e^{8\pi}.
\]

These are positive whenever `0<theta<1`.

At the fixed construction time `T=1/4`, put

\[
A(x)=G_1(T,x)+b_3G_3(T,x),\qquad
B(x)=b_2G_2(T,x)-b_3G_3(T,x),
\]
\[
D(x)=A'(x)B(x)-A(x)B'(x).
\]

At any zero `x_*` of `D` where `A<0<B`, the choice

\[
\theta_*=-A(x_*)/B(x_*)
\]

gives `G_theta_*(T,x_*)=partial_x G_theta_*(T,x_*)=0`. This defines the source once and for all. Neither `theta_*` nor any subsequent normalization varies with heat time or with the spatial observation point.

## 4. Certified narrow-bracket calculation

The accompanying checker proves the following enclosures using Arb ball arithmetic. The rounded intervals here are deliberately wider than those in its JSON receipt:

| Quantity | Certified enclosure |
| --- | --- |
| `D(44.1303)` | `(5.0206e-14, 5.0208e-14)` |
| `D(44.1304)` | `(-6.4752e-14, -6.4750e-14)` |
| `D'(x)` throughout the bracket | `(-1.178e-9, -1.121e-9)` |
| `theta_*` | `(0.87916, 0.87919)` |
| `partial_x² G_theta_*(T,x_*)` | `(-5.95e-6, -5.65e-6)` |
| Raw `a_2` | `(0.87916, 0.87919)` |
| Raw `a_3` | `(57740, 57745)` |
| Raw `Phi_a'''(0)` | `(-40.00, -39.98)` |

It also certifies `A<0<B` throughout the bracket. Continuity, the endpoint signs, and `D'<0` prove that there is exactly one root of `D` in the bracket. Its corresponding `theta_*` is strictly between zero and one. The second spectral derivative is nonzero, so this is a nondegenerate double zero, not merely an undecided small value or a fitted near-collision.

The construction uses only this narrow bracket; no unbounded search or theta sign sweep is asserted. Ordinary floating-point quadrature was used only to locate the bracket and is not part of the proof.

### How the integration and x-interval bounds are paid

The normalized mode integrand for its kth spectral derivative is

\[
e^{\lambda_n}e^{Tu^2}\phi_n(u)u^k
\cos(xu+k\pi/2).
\]

Validated Acb integration encloses the complete integral on `[0,1]`. The integrand is entire in the integration variable, so no branch-cut assumption is hidden in the integrator's analytic flag.

For `u>=1`, `k<=3`, `T=1/4`, and `lambda>=pi`,

\[
k\log u+Tu^2+9u\le\tfrac14u^2+12u
\le\tfrac14e^{2u}+12e^u\le\tfrac\lambda2 e^{4u}.
\]

The last inequality follows by monotonicity of `e^(-2u)/4+12e^(-3u)` and the strictly verified scalar inequality at `u=1`. Since `phi_n(u)<2lambda_n²e^(9u-lambda_n e^(4u))`, this gives the complete tail allowance

\[
\boxed{\int_1^\infty u^k e^{Tu^2}e^{\lambda_n}\phi_n(u)\,du
\le \lambda_n\exp\{\lambda_n-4-(\lambda_n/2)e^4\}.}
\]

For the first mode it is below `7.554e-38`; the other mode tails are much smaller. The same bound applies to the absolute oscillatory tail. Every displayed integral includes this allowance.

To cover every x in the bracket, the checker computes jets through order two at its center and positive absolute moments through order three. The inequalities

\[
|G_n^{(k+1)}(T,x)|\le\mu_{n,k+1}
\]

first bound the variation of the centered derivatives. The resulting local derivative bound then bounds the variation of `G_n` itself. This avoids replacing a small oscillatory derivative by a coarse absolute norm unnecessarily. The positive moments pay all of these interval extensions. In particular, the root and nondegeneracy statements do not rely on samples between the bracket endpoints.

## 5. Restore the primitive boundary constant and identify the failed relation

For the raw weights above,

\[
\psi_a'(0)=\sum_{n=1}^3a_n(1-4\lambda_n)e^{-\lambda_n}<0.
\]

Define the fixed positive scalar

\[
c=-\frac1{2\psi_a'(0)},\qquad
\widetilde\Phi=c\Phi_a,\quad\widetilde\psi=c\psi_a,
\quad\widetilde H=cH_a.
\]

The certificate encloses `c` near `1.0000347152`. Scaling changes neither the collision nor any square-support inequality. It gives exactly

\[
\widetilde\psi'(0)=-\frac12,\qquad
\widetilde\Phi'(0)=0,\qquad
\widetilde\psi'''(0)=\widetilde\psi'(0)+8\widetilde\Phi'(0)=-\frac12.
\]

Thus this control has the exact affine primitive reconstruction

\[
8\widetilde H=\frac12+(2t-x^2-1)\widetilde J
 +4tx\widetilde J_x-4t^2\widetilde J_{xx},
\qquad
\widetilde J=\int_0^\infty e^{tu^2}\widetilde\psi(u)\cos(xu)\,du.
\]

In contrast, the certified negative third source derivative gives

\[
\widetilde\Phi'''(0)\ne0,
\qquad
\widetilde\psi^{(5)}(0)
=\widetilde\psi'''(0)+8\widetilde\Phi'''(0)\ne-\frac12.
\]

The actual analytic weighted source is not even in u. Its even extension from the half-line is only C² at the origin, because the third derivative fails to match. No smooth even source, full modular reflection, or complete odd endpoint hierarchy is claimed. This is the exact missing relation that limits the scope of the obstruction.

## 6. Consequences for the full stationary and chord targets

Fix the constructed weights and the positive normalization. Let
`d=partial_x² H_tilde(T,x_*)`, which is nonzero. The implicit function theorem gives the full stationary predecessor `x=chi(t)` with `H_tilde_x(t,chi(t))=0`. Writing `s=T-t`, the heat equation yields

\[
\widetilde H(T-s,\chi(T-s))=ds+O(s^2),\qquad
\widetilde H_{xx}(T-s,\chi(T-s))=d+O(s).
\]

Therefore the actual first-jet energy and first Laguerre observation satisfy

\[
E=d^2s^2+O(s^3),\qquad
\mathcal L_0=-d^2s+O(s^2),\qquad
\mathcal L_0/E=-1/s+O(1).
\]

This rules out any locally bounded stationary energy payment for this control, and also any all-cutoff family whose Gaussian tail and allowed cutoff cost yield a subpower relative loss.

For the proposed pi/4 chord, use the W-zero-free interval from the full stationary start to `chi(T-s)+2s`. Uniform Taylor expansion on this interval gives

\[
\mathcal C_0(T-s;\chi(T-s),\chi(T-s)+2s)
=-d^2s^2+O(s^3)<0
\]

for sufficiently small positive s. The interval is W-zero-free because `W=ds+O(s²)` uniformly there. Thus the exact chord sign fails on arbitrarily short admissible intervals. A failure on branch zero already prevents deriving the required pair of branch statements from the relaxed hypotheses.

These deductions use the fixed constructed source; no weight or cutoff is varied along the predecessor.

## 7. Positive weights on every square node

The restriction to three nonzero weights is inessential to the support-only obstruction. Add `epsilon>0` times the raw complete tail `sum_(n>=4) phi_n`, whose endpoint derivatives and transforms converge absolutely. Use the first endpoint equation to solve for the third weight in terms of the second weight and epsilon. The derivative of that equation with respect to the third weight is `phi_3'(0)!=0`.

After this elimination, the Jacobian of `(H,H_x)` with respect to the remaining weight parameter and x has determinant equal to a nonzero constant multiple of `B(x_*)*H_xx(T,x_*)`. Both factors are nonzero by the certificate. The implicit function theorem therefore preserves the double collision and `Phi'(0)=0` for all sufficiently small epsilon. The original first three weights remain positive; all later weights equal epsilon. A positive fixed normalization again enforces `psi'(0)=-1/2`.

This produces a bounded positive sequence with full square support and the same obstruction. Every finite ordinary moment matrix and every finite adjacent-square localizing matrix is then strictly positive definite: a nonzero test polynomial has only finitely many zeros, while the positive measure has infinitely many square nodes. Merely demanding strict rather than weak positivity does not remove the obstruction. It is an analytic existence statement for a small interval of epsilon; the calculation does not supply a numerical epsilon threshold. The nonzero third source endpoint persists by continuity.

## 8. Verification and research consequence

The [replay file](../../numerics/certify_square_support_endpoint_collision.py) passed **50 assertions** at 160-bit precision, using python-flint 0.9.0. Its [JSON receipt](../../numerics/SQUARE_SUPPORT_ENDPOINT_COLLISION_CHECKS_20261015.json) records the source SHA-256, runtime version, all integral enclosures and tail allowances, root signs, nondegeneracy bounds, endpoint classification, and scope. An independent task replayed the frozen script and obtained exactly the same mathematical enclosure strings. The affine first-endpoint cancellation and all-orders localizing inequalities are analytic identities proved above; they are not inferred from finite interval checks.

The useful negative conclusion is specific: increasing the degree of support-only moment or square-gap matrices will not cure the missing coefficient information, even after adding the first source reflection endpoint and the exact primitive boundary constant. A next arithmetic certificate must encode an additional relation that rejects this fixed control, such as the full coefficient recurrence or the full modular reflection. This note does not assert that any such stronger certificate is impossible, and it proves no sign statement for the original theta source.

The [reflection-rigidity note](02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) proves that full source reflection plus the normalized endpoint forces the actual equal weights in the polynomial-growth class. The present control therefore identifies a relaxation failure without contradicting that rigidity.
