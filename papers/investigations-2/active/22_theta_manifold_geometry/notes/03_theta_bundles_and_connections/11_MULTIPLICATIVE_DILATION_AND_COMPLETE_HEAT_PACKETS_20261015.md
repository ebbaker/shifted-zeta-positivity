# Multiplicative dilation and complete heat packets

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. This continues the arithmetic task in [coordination 11](../00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md). The compact-surface direction is parked at the user's request.

## Result and scope

The square source admits an exact prime sieve and Möbius inversion by translations in the source coordinate. This is a concrete arithmetic identity outside the finite neighboring polynomial-current ansatz. Its complete half-line heat transforms converge, and explicit moment bounds give uniform endpoint errors of the permitted form `epsilon sqrt(E)` after multiplication by the complete starting observation.

The lower intervals created by these translations are essential. At every fixed positive heat time, the separate Möbius series of complete transforms and of lower intervals fail even the term test. Their paired difference converges rapidly. Thus neither dropping the lower intervals nor moving the inversion to the whole real source line supplies the missing signed estimate. A nonempty finite prime sieve also removes the source's even reflection symmetry. These statements locate the cancellations explicitly; they do not exclude a coupled estimate that retains them.

The sieve and inversion themselves are classical multiplicative algebra: see [DLMF 27.5.2](https://dlmf.nist.gov/27.5.E2) and [27.5.7](https://dlmf.nist.gov/27.5.E7). No novelty claim is made for those identities. The present contribution is their complete bookkeeping and convergence test in this investigation's positive-time, stationary-endpoint problem.

## 1. Source dilation is multiplication of the square index

Retain the manuscript normalization

\[
 p_n(u)=e^u e^{-\pi n^2e^{4u}},\qquad
 \phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\]
\[
 \psi=\sum_{n\ge1}p_n,\qquad \Phi=\sum_{n\ge1}\phi_n,
 \qquad 8\phi_n=p_n''-p_n.
\]

For an integer `d>=1`, set `a_d=(log d)/2` and

\[
 (D_df)(u)=d^{-1/2}f(u+a_d).
\]

Direct substitution, including the factor `d^(-1/2)`, gives

\[
 D_dp_n=p_{dn},\qquad D_d\phi_n=\phi_{dn},\qquad
 D_dD_e=D_{de}.                                      \tag{1}
\]

Consequently

\[
 D_d\Phi=\sum_{d\mid n}\phi_n.                       \tag{2}
\]

These identities hold at every fixed real source coordinate. On `u>=0` all the modes are strictly positive because `2 pi n^2 e^(4u)>3`.

Let `P` be a finite set of primes and `Q_P=product_(p in P) p`. Inclusion-exclusion yields

\[
 \Phi_P:=\prod_{p\in P}(I-D_p)\Phi
   =\sum_{d\mid Q_P}\mu(d)D_d\Phi
   =\sum_{(n,Q_P)=1}\phi_n.                          \tag{3}
\]

In particular `Phi_P>0` on the positive source half-line. If `m` is the smallest prime outside `P`, then

\[
 0\le\Phi_P-\phi_1\le\sum_{n\ge m}\phi_n
 \quad(u\ge0).                                      \tag{4}
\]

The least integer greater than one coprime to `Q_P` is exactly `m`; no density or prime-number asymptotic is used.

Möbius inversion also gives

\[
 \sum_{d\ge1}\mu(d)D_d\Phi=\phi_1.                  \tag{5}
\]

For each fixed real `u`, the double series is absolutely convergent: its absolute value is majorized by `sum_n tau(n)|phi_n(u)|`, and Gaussian decay in `n` dominates the divisor count. Collecting divisors then gives `sum_(d|n) mu(d)=1_(n=1)`. Equation (5) is a valid source identity without an RH assumption.

## 2. An explicit, uniform positive-half-line remainder

Fix `T>=0`, a complex-frequency strip `|Im z|<=Y`, and a derivative order `j>=0`. For an integer `m>=2`, assume

\[
 \pi m^2\ge T/8,\qquad b_m=4\pi m^2-9-Y>0.
\]

Using `e^(4u)>=1+4u+8u^2`, for `n>=m`, `t<=T`, and `u>=0`,

\[
 u^je^{tu^2+Yu}\phi_n(u)
 \le2\pi^2n^4u^j e^{-\pi n^2}e^{-b_m u}.
\]

The ratio of successive `n^4 exp(-pi n^2)` terms is at most

\[
 r_m=(1+1/m)^4e^{-\pi(2m+1)}<1.
\]

Integrating the elementary exponential majorant therefore proves

\[
 \boxed{\sum_{n\ge m}\int_0^\infty
 u^je^{tu^2+Yu}\phi_n(u)\,du
 \le \varepsilon_j(m;T,Y):=
 \frac{2\pi^2m^4 j! e^{-\pi m^2}}
 {b_m^{j+1}(1-r_m)}.}                                \tag{6}
\]

The apparent lack of `T` in the displayed value is intentional: `T` enters the stated admissibility condition, after which the remaining quadratic exponent is nonpositive. For the physical range `0<=t<=1/2`, `Y=0`, every `m>=2` is admissible. This bound is uniform in the real part of `z`, not merely on bounded frequency intervals.

For a truncated Möbius sum through `d=K`, the error in (5) is supported on indices `n>K` and has coefficient magnitude at most `tau(n)<=n`. Thus a corresponding explicit bound is (6) with `m=K+1`, `m^4` replaced by `m^5`, and `r_m` by `(1+1/m)^5 exp(-pi(2m+1))`. This also proves absolute convergence of the *paired* transformed Möbius series and all its fixed-order endpoint derivatives, locally uniformly in complex frequency and bounded upper heat time. For a larger fixed `T`, discard finitely many initial indices before applying the estimate.

The finite sieve approximates the **sifted** source by the first mode. It does not assert that the complete theta transform is its first mode with an error tending to zero as more primes are sieved out. An endpoint approximation to the complete theta source instead retains the modes whose prime factors all belong to `P`. Its omitted modes also begin at `m`, so (6) bounds that approximation, but the retained prime-smooth head is infinite. No computational advantage over ordinary index cutoff is asserted.

## 3. Exact heat transform, with the lower interval retained

Use the complex half-line transform

\[
 F(t,z)=\int_0^\infty e^{tu^2+izu}\Phi(u)\,du,
 \qquad H(t,x)=\Re F(t,x)\quad(x\in\mathbb R).
\]

It is entire in `z` and has all needed derivatives. Define

\[
 L_d(t,z)=\int_0^{a_d}
 e^{tv^2+i(z+2ita_d)v}\Phi(v)\,dv,
\]
\[
 \boxed{\mathcal P_d(t,z)=d^{-1/2}e^{ta_d^2-iza_d}
 \bigl[F(t,z+2ita_d)-L_d(t,z)\bigr].}                \tag{7}
\]

A change of variable `v=u+a_d` gives the complete formula

\[
 \mathcal P_d(t,z)=\int_0^\infty e^{tu^2+izu}D_d\Phi(u)\,du
                 =\sum_{d\mid n}F_n(t,z),           \tag{8}
\]

where `F_n` is the transform of `phi_n`. Derivatives in `z` include derivatives of the prefactor and of the lower integral. Replacing the weight `(v-a_d)^j` by `v^j`, or keeping the shifted frequency but omitting the prefactor, would change the observation.

The exact arithmetic identities are consequently

\[
 \sum_{d\mid Q_P}\mu(d)\mathcal P_d=F_1+R_P,
 \qquad |\partial_z^j R_P|\le\varepsilon_j(m;T,Y),   \tag{9}
\]
\[
 \sum_{d\ge1}\mu(d)\mathcal P_d=F_1.               \tag{10}
\]

Every lower interval in (7) is part of (9) and (10).

For clarity, the unrestricted complete-transform pieces

\[
 (\mathcal T_d^t f)(z)=d^{-1/2}e^{ta_d^2-iza_d}f(z+2ita_d)
\]

satisfy the exact semigroup law `T_d^t T_e^t=T_(de)^t`. The extra lower terms are the boundary correction imposed by the half-line. In additive shift notation `D_a f=e^(-a)f(u+a)` and `T_a^t f(z)=e^(-a+ta^2-iza)f(z+2ita)`, write `C_a[f]` for the prefactor times its lower integral. Directly splitting `[0,a+b]` at `b` proves

\[
 C_{a+b}[f]=\mathcal T_a^t C_b[f]+C_a[D_bf].          \tag{11}
\]

The semigroup alone is not the transform of the half-line source action; (11) records exactly what is missing.

## 4. Why the separated positive-time inversion diverges

Fix `t>0` and a finite complex `z`. For `a` tending to infinity, endpoint Laplace asymptotics give

\[
 F(t,z+2ita)=\frac{\Phi(0)}{2ta-iz}+O(a^{-2}).       \tag{12}
\]

Here `Phi(0)>0`. To justify (12), write the integral as the Laplace transform at parameter `2ta-iz` of `e^(tv^2)Phi(v)`. This function is smooth at zero and decays faster than every exponential at infinity. Taylor expansion at zero with a split at a fixed positive endpoint gives (12); the contribution from the rest of the source line is negligible compared with `1/a`.

The same leading asymptotic holds for `L_d`, and their difference in (7) is small by (8). But the *separated* term has magnitude

\[
 \left|d^{-1/2}e^{ta_d^2-iza_d}F(t,z+2ita_d)\right|
 \sim\frac{\Phi(0)}{t\log d}
 \exp\!\left(\frac t4(\log d)^2\right)
 d^{-1/2+\Im z/2}.                                 \tag{13}
\]

It tends to infinity. Along the infinite prime subsequence `mu(d)=-1`, so the individual summands in the separated Möbius series do not even tend to zero. The lower-interval series has the same defect. Neither series is an ordinary convergent series; their rapidly convergent **difference term by term** is (10).

At `t=0`, separating out `F(0,z)` would instead introduce

\[
 \sum_{d\ge1}\mu(d)d^{-s},\qquad s=\tfrac12+\tfrac{i z}{2}.
\]

On real `z` this lies on `Re s=1/2`; the ordinary absolute-convergence Euler-product argument applies only in `Re s>1`. No critical-line convergence or beneficial sign is supplied by invoking formal Möbius inversion. The valid paired identity (10) needs no such assertion.

This is a concrete boundary obstruction, not a theorem against every nonpolynomial multiplier.

## 5. Whole-line reflection does not remove the cost

The complete source `Phi` is even by its theta transformation. For a finite prime set, reflection changes forward to backward shifts:

\[
 \Phi_P(-u)=\prod_{p\in P}(I-p^{-1/2}T_{-a_p})\Phi(u).
\]

It does not leave the sifted source fixed. In fact, as `u` tends to minus infinity the largest divisor `Q_P` dominates the finite sum in (3), and

\[
 \Phi_P(u)\sim\mu(Q_P)\,2\pi^2 Q_P^{-5}e^{-9u}
 \exp[-\pi e^{-4u}/Q_P^2].                          \tag{14}
\]

Thus an odd number of sieving primes gives a source that is positive for `u>=0` and negative sufficiently far on the opposite half-line. Positive-half-line sieve estimates cannot be treated as even-source estimates.

Pointwise full-line Möbius inversion (5) remains valid, but integration against the positive heat weight does not commute with it. With `H(t,z)=int_0^infinity e^(tu^2) Phi(u) cos(zu) du` denoting its entire extension, at real frequency zero,

\[
 d^{-1/2}\int_{\mathbb R}e^{tu^2}\Phi(u+a_d)\,du
 =2d^{-1/2}e^{ta_d^2}H(t,2ita_d)
 \ge2H(t,0)d^{-1/2}e^{ta_d^2}.                      \tag{15}
\]

The inequality uses evenness, positivity, and `cosh(2ta_d u)>=1`. For `t>0` the terms fail to tend to zero along squarefree indices. Consistently, the inverted first mode has the negative-tail asymptotic `phi_1(u)~-3 pi e^(5u)`, whose positive-time whole-line heat integral is not defined. There is no dominated limiting operation here.

The finite symmetric operator `product_p (I-c_p T_(-a_p))(I-c_p T_(a_p))`, with `c_p=p^(-1/2)`, is positive self-adjoint on unweighted full-line `L^2`, with multiplier `product_p(1+c_p^2-2c_p cos(xi a_p))>0`. That generic operator positivity is not a sign for a product of two different physical observations and does not overcome (13) or (15).

## 6. Primitive lower edges and the complete first factor

Set `beta_n=(4 pi n^2-1)exp(-pi n^2)`. Then `p_n'(0)=-beta_n` and `sum beta_n=1/2`. For a polynomial-growth mask `c_n` put `psi_c=sum c_n p_n` and `b_c=sum c_n beta_n`. Take a `C^2` weight with the displayed integrals convergent and upper bracket `psi_c' w-psi_c w'` tending to zero; the physical weights satisfy these hypotheses. The full integration-by-parts formula is

\[
 \int_0^\infty\!\Big(\sum_n c_n\phi_n\Big)w\,du
 =\frac{b_cw(0)+\psi_c(0)w'(0)}8
  +\frac18\int_0^\infty\psi_c(w''-w)\,du.           \tag{16}
\]

The upper endpoints vanish for the physical weights used here. In particular, for even physical weights `w'(0)=0`:

- The divisible-index packet `D_d Phi` has lower coefficient `b_[d]=sum_k beta_(dk)=-d^(-1/2)psi'(a_d)`.
- The sieve has `b_P=sum_((n,Q_P)=1) beta_n`, not `1/2`.
- Möbius inversion of the lower coefficients gives `sum_d mu(d)b_[d]=beta_1`.
- A prime-smooth endpoint approximation has its own coefficient `b_sm=sum_(n P-smooth) beta_n`.

For the endpoint reconstruction residual from note 09, with an endpoint mask `c_n` and complete starting terms, the source lower edge is exactly

\[
 B_{\rm src}=\frac{\mathbf1_{j=0}b_c-A/2}{8}.        \tag{17}
\]

The choice `A=2 b_c` on branch zero, `A=0` on branch one, cancels this edge without division by the physical jet. It does not cancel the remaining source or index trace. Alternatively the difference from the complete coefficient is a controlled absolute error; its sign after multiplication by `W` is not fixed.

For any endpoint approximation justified by (6), retain the **complete** `W=h_j(t,x)` and full stationarity `S=h_(j+1)(t,x)=0`. Then

\[
 |W(h_j(t,x+\delta)-h_{j,c}(t,x+\delta))|
 \le\varepsilon_j |W|\le\varepsilon_j\sqrt E.       \tag{18}
\]

This is precisely an admissible error. Sifting or cutting off the starting `W` would lose (18). The estimate does not sign the remaining complete cross term; making the error small and controlling that term are separate requirements.

## 7. Arithmetic discriminator and next acceptance test

For a weighted square source `Phi_a=sum a_n phi_n`, equation (1) still holds modewise but the exact prime-excision formula (2) becomes

\[
 \Phi_a-D_p\Phi_a
 =\sum_{p\nmid n}a_n\phi_n
  +\sum_{p\mid n}(a_n-a_{n/p})\phi_n.               \tag{19}
\]

The extra coefficients vanish exactly when `a_(pn)=a_n` for every `n`, using the same uniqueness of a Gaussian square expansion as the existing arithmetic notes. With `a_1=1`, imposing this for every prime forces `a_n=1`. Imposing it for finitely many primes allows arbitrary values on the remaining prime-free parts; it does not characterize theta. Positivity of the expression in (19) alone is weaker still and must not be substituted for exact excision.

The certified finite weighted-square collisions fail the full family of exact prime identities. The reflected quartic collision in Investigation 22 fails the square expansion itself. Investigation 21's positive-primitive collision shows that generic primitive positivity, reflection, and endpoint identities are insufficient; they do not supply the multiplicative source identities. Local asymmetric heat germs likewise do not carry this arithmetic data.

These distinctions make (7) a legitimate arithmetic candidate. They do **not** establish its scalar sign. Taking absolute values of the entire surviving main term supplies a fixed `C|W|`, which does not vanish with the sieve error and cannot substitute for `C W^2` through a collision. Replacing its coefficient by a quotient involving `W` merely restates the local boundedness problem.

The bounded conclusion is to retain (7), (9), (11), and (17) as the complete arithmetic formulation, and reject the separated Euler/Möbius route. Any further proposal should bound the combined lower intervals and shifted complete transforms in their signed stationary pairing, with an error tending to zero uniformly through a putative event. This remains an open estimate, not a promised consequence of the sieve. The accompanying [nonlocal audit](12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md) records three other explicit candidates and why their current forms do not supply it.
