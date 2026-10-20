# Finite evaluation and endpoint inverse costs

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
**gpt-6-astra (Codex), reasoning effort ultra**, verified turn metadata.
Separate same-model internal checks; no specialist review or novelty claim.

**Outcome.** A classical Riemann–Siegel formula plus a discrete Cauchy derivative lowers the sufficient leading summand exponent for both existing gap-certified extraction schemes to one-half. The earlier geometric-versus-single-width exponent advantage belongs to the specified Euler-sum method. A separate exact Möbius mollifier still has a large paid remainder and retains the multiple-zero residue when its contour crosses the line. Endpoint heat energy retains its compatible divergence. No original multiple zero is excluded.

This continuation follows the [result index](../../../../../../../result-summaries/README.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), particularly [scoped conclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md). These are bounded quantitative comparisons, not additional equivalent simplicity criteria.

The inputs and matched consumer are in [Note 09](09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md); [Note 08](08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md) supplies the checked reciprocal estimate. The [review](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) records the source and algebra checks. Section 3 is a bounded assessment of the inherited energy route, not a newly activated numerical campaign.

## 1. Square-root-length evaluation with the cutoff error retained

This section imports a classical evaluation algorithm, not a new zeta approximation. Its contribution here is the complete relative-error calculation for the existing consumer and its matched comparison. Write L=log(gamma), ell=log L. Keep Note 09's independent noncentral gap d=c/L, where c stays in a fixed positive compact set, fixed tolerance tau, widths a_j, coefficients c_j, and r=O(sqrt(ell)). Its smallest width satisfies

\[
 a_*=(c/L)\exp\{-\sqrt{\ell\log2}+O_\tau(1)\},\qquad
 |\zeta(1/2+a+i\gamma)|^{-1}\le e^{R_*}
       =\gamma^{1/2+o(1)}\quad(a_*\le a\le d/2).       \tag{R1}
\]

These are Note 09 (E10)–(E17), using Balazard–de Roton under RH; no simplicity is assumed. All arguments below take gamma sufficiently large for the displayed fixed strip.

### Classical value input

Let A(s) be the finite part of the Riemann–Siegel expansion in [O'Sullivan, Theorem 1.3, equation (1.8)](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/Riemann-Siegel-2nd-revision.pdf), with its expansion parameter N=6. This N is the number of retained correction indices, not a Dirichlet cutoff. The formula has two sums through floor(sqrt(t/(2pi))) and six explicitly recursive correction terms. Uniformly for 1/2<=Re(s)<=3/4 and t=Im(s)>2pi, that theorem gives

\[
 |A(s)-\zeta(s)|\ll t^{-1-\Re(s)/2}\le t^{-5/4}.        \tag{R2}
\]

The theorem includes every fractional part of sqrt(t/(2pi)), including cutoff transitions. A(s) is evaluated separately at each point. No holomorphic dependence of this pointwise truncation is assumed, and no derivative of its remainder is taken. The cited asymptotic constants are not numerically instantiated here. The primary formula is an unconditional value approximation.

### Discrete Cauchy derivative with an explicit alias payment

For s_a=1/2+a+i gamma put r_a=a/2, J=ceil(3 log_2 gamma), omega=exp(2pi i/J), and define the finite quantity

\[
 D_{a,J}={1\over J r_a}\sum_{j=0}^{J-1}
       A(s_a+r_a\omega^j)\omega^{-j}.                  \tag{R3}
\]

The zeta function is holomorphic on the closed disc |s-s_a|<=a; its pole at one is far from this high ordinate. A coarse elementary sum, or the approximate functional equation, bounds its supremum on that disc by M<<gamma^(1/2), uniformly in the selected a. This disc lies in the fixed strip of (R2). If zeta(s_a+z)=sum b_k z^k, Cauchy's coefficient bound gives |b_k|<=M/a^k. For J>=2 the root-of-unity sum with exact zeta values equals

\[
 \zeta'(s_a)+\sum_{q\ge1}b_{1+qJ}r_a^{qJ}.
\]

Consequently the normalized alias error is at most

\[
 a\left|{1\over Jr_a}\sum_j\zeta(s_a+r_a\omega^j)
       \omega^{-j}-\zeta'(s_a)\right|
 \le {M 2^{-J}\over1-2^{-J}}\ll\gamma^{-5/2}.          \tag{R4}
\]

Each value error in (R2), after multiplication by a/(Jr_a), contributes at most 2/J times its bound. Thus the complete value-plus-alias estimate is

\[
 |A(s_a)-\zeta(s_a)|+a|D_{a,J}-\zeta'(s_a)|
       \ll\gamma^{-5/4}.                              \tag{R5}
\]

Using different floors at different sample points is harmless: (R4) uses analyticity of zeta alone and (R5) pays the pointwise errors directly. This also avoids differentiating a scalar big-O statement.

### Division and the actual multiplicity consumer

As in Note 09 (E13), the analytic logarithm in a strictly right-half-plane disc under RH gives

\[
 a|\zeta'/\zeta(s_a)|\ll 1+L+R_* .                    \tag{R6}
\]

For sufficiently large gamma, (R1) and (R5) imply |A(s_a)|>=|zeta(s_a)|/2. Exact division, before taking real parts, therefore yields

\[
 a\left|{D_{a,J}\over A(s_a)}-{\zeta'\over\zeta}(s_a)\right|
 \ll(1+L+R_*)e^{R_*}\gamma^{-5/4}
   =\gamma^{-3/4+o(1)}.                              \tag{R7}
\]

For clarity, this follows by bounding (D-zeta')/A and (zeta'/zeta)(zeta-A)/A separately; neither denominator is replaced by a fixed nonzero constant. Add the exact completion logarithmic derivative

\[
 D_{\rm comp}(s)=1/s+1/(s-1)-\tfrac12\log\pi
                         +\tfrac12\psi(s/2).
\]

Then a Re[D_comp(s_a)+D_{a,J}/A(s_a)] approximates B_a=a Re(xi'/xi)(s_a) with the same error. Since Note 09 proves sum_j|c_j|<2, the combined extraction M_r inherits error gamma^(-3/4+o(1)), uniformly over all its widths. Its previously paid zero-side leakage, independent-gap premise and optional center-uncertainty bound remain unchanged.

There are O(r log gamma) value evaluations, each using two sums of O(sqrt(gamma)) terms and a fixed number of correction terms. Thus the total number of Dirichlet summands is

\[
 O\bigl(\sqrt\gamma\log\gamma\sqrt{\log\log\gamma}\bigr)
       =\gamma^{1/2+o(1)}.                            \tag{R8}
\]

This is an asymptotic summand count in exact arithmetic, not a bit-complexity theorem, optimal algorithm, implemented interval certificate, or finite-height onset. Special-function evaluation and finite-precision roundoff would need their own rigorous payments in an implementation. Increasing the fixed expansion order and J supplies any fixed polynomial absolute accuracy without changing the exponent in (R8).

### The same algorithm changes the matched comparison

Note 09's one-width comparator selects a~L^(-3/2). Substituting that width into the same checked reciprocal estimate gives

\[
 |\zeta(1/2+a+i\gamma)|^{-1}\le\gamma^{3/4+o(1)}.       \tag{R9}
\]

Equations (R3)–(R6) apply without change. Its normalized logarithmic-derivative error is now gamma^(-1/2+o(1)), still vanishing; it uses O(sqrt(gamma) log gamma) summands. Thus **both** the geometrically spaced extraction and its matched coarse one-width comparator have sufficient leading summand exponent 1/2 with this value algorithm. Note 09's comparison of exponents 1 and 3/2 remains correct for its declared elementary Euler-sum payment, but is not an algorithm-independent advantage. The geometric method still has its proved leakage cancellation and coefficient stability; this calculation establishes no advantage over a direct first-jet certificate on matched complete data.

At a hypothetical double zero the exact extracted mass remains two plus nonnegative leakage. Smaller arithmetic error identifies that value more accurately and supplies no opposing upper bound below two. The endpoint control's zero-side behavior is therefore retained; Note 05's failure of ordinary Dirichlet-series arithmetic does not convert (R7) into a strict inequality for the original theta source.


## 2. Exact finite Möbius mollification and the crossed zero term

**Outcome.** No opposing event-conditioned sign was obtained. For the explicit Riesz mollifier below, the existing RH reciprocal bound gives a proved absolute remainder, but a polynomial length does not make its declared allowance small. An attempt to obtain a dual short sum by the functional equation must retain reciprocal-zeta zero residues; the exact double-zero term is displayed. This is a scoped assessment of this contour payment, not a lower bound on all possible mollifier lengths.

Let L=log γ, ell=log L, a=c/L with fixed c>0, s=1/2+a+iγ, and fix an integer k≥2. Define the finite polynomial with the actual Möbius coefficients

    M_{Y,k}(s)=Σ_{n≤Y} μ(n)n^{−s}(1−n/Y)^k,
    K_k(w)=k!/[w(w+1)…(w+k)].

Mellin inversion of the beta integral gives, initially on Re w=1,

    M_{Y,k}(s)=(1/(2πi))∫ K_k(w)Y^w/ζ(s+w) dw.

Under RH, put h=a/ell and b=a−h. Moving the line to Re w=−b crosses only the kernel pole at w=0: the reciprocal zeta factor is holomorphic when Re(s+w)>1/2. Thus the exact remainder is

    M_{Y,k}(s)−1/ζ(s)
      =(1/(2πi))∫_{Re w=−b} K_k(w)Y^w/ζ(s+w) dw.          (M1)

No zero simplicity or derivative moment is used.

The uniform [Balazard–de Roton bound](https://arxiv.org/pdf/0810.3587), Propositions 1 and 18, already checked in Note 08, gives

    |1/ζ(1/2+h+i(γ+v))|
       ≤(γ+|v|+3)^{1/2+O_c(log ell/ell)}                   (M2)

for sufficiently large γ, uniformly in real v. Here is the additional uniformity check. Write u=log(|γ+v|+3), q=log u. Fix θ∈(0,1]. For sufficiently large |γ+v|, Proposition 18 permits V=u[1/(2q)+(log q)/q²], and Proposition 1 bounds the reciprocal logarithm by V[log(V/(hu))+2(1+θ)log log V+O_θ(1)] when h≤V/u. Conjugation treats negative heights. Thus in this small-shift regime its exponent is at most

    [u/(2q)] * (1+2 log q/q)
      [ell+log ell+(1+2θ)log q+O_{c,θ}(1)].

For u≥L this is at most u[1/2+O(log ell/ell)], since the bracket divided by q, and 1+2log q/q, decrease for q≥ell once γ is large. For L/ell²≤u≤L the same expression is at most L[1/2+O(log ell/ell)]. For fixed-large u≤L/ell² it is O(L/ell)=o(L). The remaining compact heights have only finitely many boundary poles of finite orders, so their reciprocal bound is a fixed power of 1/h=O(L ell), also exp(o(L)). In the larger-shift regime h≥V/u, one has q≥1/(2h), and the bound O_θ(V) has exponent/u=O_θ(1/q)=O_θ(h), smaller than the required exponent for large γ. No all-zero derivative lower bound is imported in this compact-height step.

For b<1/2,

    |K_k(−b+iv)|≲_k [(b²+v²)^{1/2}(1+|v|)^k]^{−1}.

Its integral against (M2) is γ^{1/2+O_c(log ell/ell)}: near v=0 the extra factor is only log(1/b), and the tails converge for fixed k≥2. For the horizontal contour segments, the same bound holds uniformly throughout the traversed strip: the horizontal shift from 1/2 ranges from h to 1+a<3/2, within Proposition 1’s range σ≤2. Its small-shift bound decreases as the shift increases, and its larger-shift bound is O_θ(V). Together with K_k(w)=O_k(|Im w|^{−k−1}), this makes the horizontal integrals vanish. Therefore (M1) proves

    |M_{Y,k}(s)−1/ζ(s)|
       ≤γ^{1/2+O_{c,k}(log ell/ell)}
          Y^{−(c/L)(1−1/ell)}.                            (M3)

This is an absolute approximation. If Y=γ^A with fixed A, the damping is e^{−Ac+o(1)}; the resulting allowance in (M3) remains γ^{1/2+o(1)}, so it does not certify o(1). If

    log Y=K L²,    K>1/(2c),

then (M3) gives a vanishing absolute error γ^{1/2−Kc+o(1)}. This is a sufficient payment, not a necessity statement about the actual remainder. It is also not a computational improvement over Note 08's finite-zeta ratio, whose different exact coefficients already give polynomial-cutoff precision. A relative approximation requires its additional denominator/value payment.

**The functional-equation crossing retains the event.** To move the reciprocal-zeta contour into Re(s+w)<1/2, even when using the exact functional equation there, one crosses all reciprocal poles at w=ρ′−s. Suppose specifically that ρ=1/2+iγ is an exact double zero. Its Laurent coefficients are

    1/ζ(ρ+z)= [2/ζ″(ρ)]z^{−2}
              −[2ζ‴(ρ)/(3ζ″(ρ)²)]z^{−1}+O(1).

The pole at w=−a therefore contributes exactly

    Y^{−a} { [2/ζ″(ρ)] [K_k′(−a)+K_k(−a)log Y]
              −[2ζ‴(ρ)/(3ζ″(ρ)²)]K_k(−a) }.              (M4)

Other zeros contribute their own residues and the displaced contour remains to be paid. The [exact functional equation](https://dlmf.nist.gov/25.4) does not remove (M4); reciprocal completion is meromorphic at the original zeros. Neither the coefficient 1/ζ″(ρ) nor the required regular-factor control follows from the event condition. Omitting these terms would be precisely the unsupported step in a pole-free two-sum approximate functional equation for the inverse.

Multiplying ζ by a finite mollifier likewise preserves its zero order when the mollifier is nonzero there, and increases it if the mollifier vanishes. Pairing it with its reflected factor preserves reflection but does not cancel this local event. Thus (M1)–(M4) identify the remaining signed/residue payment rather than excluding a double zero. No weak-Mertens assertion, negative derivative moment, or simplicity premise has been used.


## 3. Endpoint heat energy: the remaining inverse-gap bound

**Assessment.** No opposing estimate from unchanged theta arithmetic was obtained. The calculation below pays the finite cluster's exterior forcing and identifies exactly what endpoint renormalization removes. It extends the double-gap coefficient already recorded in Note 03 §8 and Note 04 §3 to the associated all-multiplicity energies; it is a bounded assessment, not a new simplicity criterion or a reason to activate BW09's deferred energy campaign.

Assume RH and an exact order-`m>=2` zero of `F(x)=H(0,x)` at `a>0`. Put

\[
g(x)=F(x)/(x-a)^m,\quad L=(\log|g|)'(a),\quad
S=-(\log|g|)''(a)=\sum_{r\ne a}\frac{m_r}{(a-r)^2}>0,
\quad M=\frac{m(m-1)}2.
\tag{H1}
\]

The full exterior sum converges. In particular `S>=m/(4a^2)` from the mirror zero. Isolate this cluster in a fixed disk. Weierstrass preparation gives `H(t,x)=p(t,x)G(t,x)` there, with `p` the monic cluster polynomial and `G` a nonvanishing analytic function. At its positive-time simple roots,

\[
\dot x_i=2\sum_{j\ne i,\ j\text{ in cluster}}\frac1{x_i-x_j}
 +b(t,x_i),\qquad b=2G_x/G.
\tag{H2}
\]

This follows directly from `dot x_i=H_xx/H_x`; all exterior roots are retained by `G`, without a moving spatial cutoff. At the event, `b(0,a)=2L` and `b_x(0,a)=-2S`.

Let `lambda_i` be the roots of the monic probabilists' Hermite polynomial `He_m`, put `tau=sqrt(2t)`, and let `D_m=prod_(i<j)(lambda_i-lambda_j)^2`. The local heat expansion, with its analytic remainder, gives

\[
\frac{H(t,a+\tau z)}{g(a)\tau^m}
=\operatorname{He}_m(z)+L\tau\operatorname{He}_{m+1}(z)
 +\frac{L^2-S}{2}\tau^2\operatorname{He}_{m+2}(z)+O(\tau^3),
\]

uniformly on compact complex `z`-sets. Expanding at each simple Hermite root yields

\[
x_i=a+\tau\lambda_i+L\tau^2-\frac S2\lambda_i\tau^3+O(\tau^4).
\tag{H3}
\]

Indeed, at such a root, `He_(m+1)=-He_m'`, `He_(m+1)'=0`, `He_m''=lambda_i He_m'`, and `He_(m+2)=-lambda_i He_m'`. The uniform expansion follows from the jointly analytic heat series; the simple-root implicit function theorem applies after scaling. Symmetric rational cluster quantities are meromorphic in `t`, not merely in `tau`; for the logarithmic energy, `U+(M/2)log(2t)` is analytic near zero. These assertions follow from the analytic coefficients of `p` and its discriminant. Their remainders below therefore have integer powers.

For the unordered log-gap and inverse-square energies,

\[
U=-\sum_{i<j}\log(x_j-x_i),\qquad
E=\sum_{i<j}(x_j-x_i)^{-2},
\]

one obtains

\[
\boxed{U=-\frac M2\log(2t)-\frac12\log D_m+MS\,t+O(t^2),
\qquad E=\frac M{8t}+\frac{MS}4+O(t).}
\tag{H4}
\]

Here `sum_(i<j)(lambda_i-lambda_j)^(-2)=M/4`, from the Hermite root identity `sum_(j!=i)1/(lambda_i-lambda_j)=lambda_i/2` and the cancellation of triple cross terms. The exact cluster Hamiltonian identity is

\[
\boxed{U'=-4E-\sum_{i<j}
 \frac{b(t,x_j)-b(t,x_i)}{x_j-x_i}.}
\tag{H5}
\]

The last sum tends to `-2MS`; discarding it would give the wrong finite part. For completeness, the kinetic cost is

\[
\sum_i\dot x_i^2=\frac Mt+4mL^2-6MS+O(t).
\tag{H6}
\]

Thus the inverse-gap integral from `epsilon` to any fixed sufficiently small positive time has cost `(M/8)log(1/epsilon)+O(1)`, and the kinetic integral has cost `M log(1/epsilon)+O(1)`. Subtraction against fixed distinct reference positions leaves these divergences. Subtracting the universal heat-collision term instead makes the energies regular, but leaves the compatible positive values `U_ren'(0)=MS` and `E_ren(0)=MS/4`. No residual negative sign or finite renormalized contradiction is produced.

The attempted arithmetic bound stops at a definite denominator. With `h_j=F^(j)(a)`,

\[
L=\frac{h_{m+1}}{(m+1)h_m},\qquad
S=\frac{h_{m+1}^2}{(m+1)^2h_m^2}
 -\frac{2h_{m+2}}{(m+1)(m+2)h_m}.
\tag{H7}
\]

The exact theta source supplies finite moment upper bounds for each `|h_j|`, but no all-event lower bound for `|h_m|`, nor an upper bound for this exterior inverse-square sum. Moreover, even finite `S` leaves the `M/(8t)` term in (H4). Controlling the ordinary heat solution in source or finite-jet norms does not control this reciprocal-gap energy: Note 05 §4's normalized positive-source controls approach theta in every stated finite heat-jet seminorm, retain exact endpoint doubles, and have this same nonintegrable energy. Their failed premise remains the unchanged ordinary-Dirichlet arithmetic; they do not refute an estimate using that exact information.

[Rodgers–Tao, §§6–8](https://arxiv.org/html/1801.05914v2) obtain their integrated-energy and final time-zero estimates under the contradiction assumption `Lambda<0`, using an all-real evolution interval strictly before zero. Their finite-cluster identities retain exterior terms (Lemma 4.2). RH alone supplies the forward interval beginning at zero, so their pre-zero regularizing interval is unavailable here. Replacing it with an asserted finite integral down to the endpoint would assume the missing input.

**Decision.** Retain BW09 HFCE-07 as deferred. The next needed result is an independently proved exact-theta bound that contradicts the displayed endpoint energy cost; none follows from the checked source moments, complete exterior bookkeeping, or compatible positive finite parts. No new numerical campaign, exclusion class, or standalone research milestone is justified by this calculation.


## 4. Endpoint phase energy and derivative-scale comparison

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Actual model **gpt-6-astra**, reasoning effort **ultra**; derivation against
HEAD `fa80fa9`. Separate same-model internal checks by the phase and Gaussian
agents; no specialist review or novelty claim. This is an addition to the existing endpoint assessment.

The [result index](../../../../../../../result-summaries/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../../../../avoid/README.md), and
[gain-before-expansion rule](../../../../../../../avoid/20_volume_without_a_gain.md)
apply. This is an exact comparison of two energies for the **same event**.
It supplies no opposing estimate from unchanged theta arithmetic.

Keep §3's order-`m>=2` event, `g`, `L=g'(a)/g(a)`, and
`tau=sqrt(2t)`. Write `P_m=He_m` and let `nu_1<...<nu_(m-1)` be the
roots of `He_(m-1)`. For the physical jet define

\[
 J=H+iH_x,\qquad
 \rho_t(x)=-\operatorname{Im}\frac{J_x}{J}
 =\frac{H_x^2-HH_{xx}}{H^2+H_x^2}.
 \tag{H8}
\]

Under RH the positive-time zeros are simple and real, and this phase
density is positive. The following local asymptotics retain the complete
analytic contribution of the exterior zeros and source.

### Actual peak centers and the retained exterior term

Put `F(tau,z)=H(t,a+tau z)/(g(a)tau^m)`. The heat expansion in §3 gives
`F=P_m+L tau P_(m+1)+O(tau^2)`, with derivatives uniformly on compact
complex sets. The actual real critical points `c_j(t)`, where `H_x=0`,
and the nearby complex zeros `z_j(t)=alpha_j(t)-i beta_j(t)` of `J` obey

\[
\begin{aligned}
 c_j(t)&=a+\tau\nu_j+\frac{m+1}{m}L\tau^2+O(\tau^3),\\
 z_j(t)&=a+\tau\nu_j+
       \left(\frac{m+1}{m}L-\frac{i}{m}\right)\tau^2+O(\tau^3).
\end{aligned}
\tag{H9}
\]

Indeed, the scaled physical jet is `tau F+i F_z`. At `nu_j`,
`P_m'=0`, `P_m''=-m P_m`, and `P_(m+1)'=(m+1)P_m`; the simple-root
implicit function theorem gives (H9). In particular
`beta_j=2t/m+O(t^(3/2))>0`, `alpha_j-c_j=O(t^(3/2))`, and distinct
centers are separated by a nonzero constant times `sqrt(t)`.

At time zero `J` has exact order `m-1` at `a`. Choose a fixed complex
disk containing no other zero of `J(0,.)`. Weierstrass preparation gives
`J(t,z)=A(t,z) product_j(z-z_j(t))`, with `A` nonvanishing and
`A_x/A` uniformly bounded on a smaller fixed interval `I` about `a`.
Consequently the following is an exact identity on `I`:

\[
 \rho_t(x)=R_t(x)+\sum_{j=1}^{m-1}
 \frac{\beta_j(t)}{(x-\alpha_j(t))^2+\beta_j(t)^2},
 \qquad R_t=-\operatorname{Im}(A_x/A),\quad |R_t|\le C.
 \tag{H10}
\]

The bounded term `R_t` is retained, not assigned a favorable sign or
deleted. Formula (H10) proves the uniform local limit, for bounded real `y`,

\[
 \frac{2t}{m}\rho_t\!\left(c_j(t)+\frac{2t}{m}y\right)
 \longrightarrow\frac1{1+y^2}.
 \tag{H11}
\]

Each peak has asymptotic phase area `pi`; the peak width is `2t/m`,
smaller than the `sqrt(t)` root-separation scale.

### Full physical energy and the scale comparison

For a Lorentzian `L_j(x)=beta_j/((x-alpha_j)^2+beta_j^2)`,

\[
 \int_{\mathbb R}L_j^2\,dx=\frac{\pi}{2\beta_j},\qquad
 \int_{\mathbb R}L_iL_j\,dx=
 \frac{\pi(\beta_i+\beta_j)}
      {(\alpha_i-\alpha_j)^2+(\beta_i+\beta_j)^2}=O(1)
 \quad(i\ne j).
\]

The bounded unit contributes `O(1)` to the cross and squared integrals.
Restricting a squared peak to `I` loses `O(t^2)`. The same leading
answer holds on the actual outer-root cap
`[x_1(t),x_m(t)]`: each peak is a distance comparable to `tau` from
its endpoints, so its omitted squared tails are `O(tau)`.
Thus, for either of these two integration intervals `I_t`,

\[
 \int_{I_t}\rho_t(x)^2\,dx
 =\frac{\pi m(m-1)}{4t}+O(t^{-1/2}),\qquad
 \int_\epsilon^{t_0}\int_{I_t}\rho_t^2\,dx\,dt
 =\frac{\pi m(m-1)}4\log\frac{t_0}{\epsilon}+O(1).
 \tag{H12}
\]

Constants may depend on the fixed event and interval. The coefficient
is exactly `4 pi` times §3's leading unordered inverse-gap coefficient.
This is compatible with every finite multiplicity.

Now apply precisely the derivative rescaling discussed in
[BW09, “Concentration, energy and invariant information”](../../09_expanding_contour_later_collision/manuscript/main.tex).
For each positive-time cap set `beta(t)=tau` and

\[
 J_\beta=H+i\beta H_x,\qquad
 \rho_{\beta,t}=\frac{\beta(H_x^2-HH_{xx})}{H^2+\beta^2H_x^2}.
 \tag{H13}
\]

Exactly under `x=a+tau z`,
`rho_(beta,t)=tau^(-1)(F_z^2-F F_zz)/(F^2+F_z^2)`.
The polynomials `P_m` and `P_m'` have no common real zero, so their
squared denominator stays positive on a fixed compact interval
containing the actual cap. Uniformly there,

\[
 \rho_{\beta,t}(a+\tau z)=\tau^{-1}{\cal R}_m(z)+O(1),
 \qquad {\cal R}_m=
 \frac{(P_m')^2-P_mP_m''}{P_m^2+(P_m')^2}.
 \tag{H14}
\]

The scaled cap endpoints are `lambda_1+O(tau)` and
`lambda_m+O(tau)`. Their displacement therefore contributes only `O(1)`
to the following energy, including all endpoint pieces:

\[
 \int_{x_1(t)}^{x_m(t)}\rho_{\beta,t}^2\,dx
 =\frac{C_m}{\sqrt{2t}}+O(1),\qquad
 C_m=\int_{\lambda_1}^{\lambda_m}{\cal R}_m(z)^2\,dz>0.
 \tag{H15}
\]

In particular `P_2=z^2-1`, `R_2=2/(1+z^2)`, and `C_2=pi+2`.
The time integral from zero is finite, with value
`C_m sqrt(2t_0)+O(t_0)` as `t_0` decreases to zero.
Nevertheless, for every sufficiently small positive `t`, **both jets
have exactly the same cap phase decrease `(m-1)pi`**, one `pi` for each
adjacent root interval. The total cap count has not decreased.

This is a cap-energy comparison, not permission to discard a term from
a spacetime contour. With time-dependent `beta` the complete one-form is

\[
 d\arg J_\beta=
 \frac{\beta Q_x+\beta' HH_x}{H^2+\beta^2H_x^2}\,dt
 -\frac{\beta Q}{H^2+\beta^2H_x^2}\,dx,
 \qquad Q=H_x^2-HH_{xx}.
 \tag{H16}
\]

Positive scaling preserves degree on each nonzero finite contour;
`beta(0)=0` supplies no nonzero extension through the event.

### What this bounded attempt establishes

The physical phase energy diverges, but its divergence is not invariant
under the derivative-scale change already allowed by BW09. Conversely,
finite energy for the rescaled cap is compatible with the same endpoint
event and the same cap phase. Neither statement supplies a strict winding
surplus. The scaled finite energy therefore does not exclude this event.

Complete theta moment bounds control finite jets, not the reciprocal
denominator in (H8). Global counting retains multiplicities and does not
bound inverse gaps at a fixed event. The primary
[Rodgers–Tao argument, introduction and §§6–8](https://arxiv.org/html/1801.05914v2)
obtains its integrated and time-zero energy estimates under `Lambda<0`,
with an all-real interval strictly before zero. RH supplies no such
interval; the cited theorem cannot replace the missing endpoint bound.

Note 05's normalized positive-source doubles satisfy these same local
heat laws and approximate theta in the stated finite heat-jet norms.
Their failed premise is unchanged ordinary-Dirichlet arithmetic, so this
comparison is not a counterexample to an estimate using the full original
source. No exact-theta opposing bound was obtained. Keep the energy
campaign deferred and retain this calculation only as the quantitative
scale clarification of the existing endpoint assessment.
[Separate same-model continuation review](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).


## 5. Prescribed logarithmic Möbius taper: a quantitative obstruction

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. This section uses the original Möbius
coefficients and the complete norm. Its obstruction concerns one prescribed
approximant, and gives no RH-only upper bound. The logarithmic taper here
differs from the physical Riesz taper in §2.

### 5.1 The lower constant counts distinct zeros with squared multiplicity

Put
\[
 \mathcal E(A)=\frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\zeta(\tfrac12+it)A(\tfrac12+it)|^2}{\tfrac14+t^2}\,dt,
 \qquad d_N^2=\inf_{A(s)=\sum_{n\le N}a_nn^{-s}}\mathcal E(A).
 \tag{NB1}
\]
[Burnol, Theorem1.3](https://arxiv.org/pdf/math/0103058) proves the corresponding lower bound for the continuous-dilation distance \(D(\lambda)\). Since the discrete span is contained in that continuous span, \(d_N\ge D(1/N)\). Therefore, under RH,
\[
 \liminf_{N\to\infty}d_N^2\log N
 \ge \sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}
 =Z+\sum_{\rho\ {\rm distinct}}\frac{m_\rho(m_\rho-1)}{|\rho|^2},
 \quad Z=2+\gamma_E-\log(4\pi).
 \tag{NB2}
\]
Both signs of the ordinate occur. An exact double conjugate pair contributes an excess \(4/(\gamma^2+1/4)\). This is an asymptotic liminf, not a uniform finite-\(N\) inequality. A positive error allowance in the leading constant would not exclude arbitrarily high exceptional pairs.

### 5.2 The sharp constructive theorem assumes simplicity

Let
\[
 V_N(s)=\sum_{n\le N}\mu(n)\left(1-\frac{\log n}{\log N}\right)n^{-s},
 \qquad E_N=\mathcal E(V_N).
 \tag{NB3}
\]
[Bettin–Conrey–Farmer, Theorem1](https://arxiv.org/pdf/1211.5191) obtains \(E_N\sim Z/\log N\) under RH and
\[
 \sum_{|\Im\rho|\le T}|\zeta'(\rho)|^{-2}\ll T^{3/2-\delta}
 \quad(\delta>0).
 \tag{NB4}
\]
They expressly state that this hypothesis assumes all zeros simple. It is unavailable for the present investigation. Their unconditional Lemma2 retains
\[
 R_N(\rho,s)=\operatorname*{Res}_{z=\rho}
 \frac{N^{z-s}}{\zeta(z)(z-s)^2}
 \tag{NB5}
\]
with the complete higher-order residue; Lemma3's bound for the residue sum assumes simplicity and (NB4). Replacing (NB5) by a simple-zero residue before proving simplicity loses precisely the event under investigation.

### 5.3 What RH alone constructively supplies

[Balazard–de Roton, Propositions1–3](https://arxiv.org/pdf/0812.1689) instead use
\[
 A_N(s)=\sum_{n\le N}\mu(n)n^{-\varepsilon_N-s},\qquad
 \varepsilon_N=26\frac{(\log\log N)^{5/2+\eta}}{\sqrt{\log N}}
 \quad(\eta>0).
 \tag{NB6}
\]
Their RH-only estimates give, for sufficiently large \(N\),
\[
 d_N^2\le\mathcal E(A_N)
 \ll_\eta\varepsilon_N+N^{-\varepsilon_N/2}
 \ll_\eta\frac{(\log\log N)^{5/2+\eta}}{\sqrt{\log N}}.
 \tag{NB7}
\]
This upper allowance divided by \(1/\log N\) grows without bound. These coefficients differ from (NB3), so (NB7) supplies neither its convergence nor its sharp constant. The distinction is about these checked theorems; no current-best literature claim is made.

### 5.4 Even convergence for this fixed polynomial already forces simplicity

[Wei–Wu, Proposition1.9 and its proof](https://bimsa.net/doc/publication/1424.pdf) establish that \(E_N\to0\) implies RH and simplicity. Their Theorem1.10 proves RH-equivalence only after moving the norm to every fixed line \(\Re s>1/2\).

Here is a quantitative extraction from that proof. Let M(x)=sum_{n<=x} mu(n), take N>=2, and fix a critical-line zero rho=1/2+i gamma. With
\[
 F(x)=\int_1^x\frac{M(u)}u\,du,\quad
 c_N=F(N)/\log N,\quad
 A=\limsup_{x\to\infty}\frac{|F(x)|}{\sqrt x\log x},
 \tag{NB8}
\]
Mellin Plancherel and the unitary multiplier
\(s\zeta(1-s)/((1-s)\zeta(s))\) give
\[
 \sqrt{E_N}\ge |c_N|/\sqrt N-o(1),\qquad
 \limsup_N\sqrt{E_N}\ge A.
 \tag{NB9}
\]
Indeed it maps \(\{1/(nt)\}\) to \(\{nt\}/(nt)\); on \((0,1/N)\) the transformed sum equals \(c_N\). The transformed indicator has vanishing norm there. Integer and real limsups agree since \(|F(x)-F(\lfloor x\rfloor)|\le1\).

If \(A<\infty\), integration by parts yields
\[
 \frac1{\zeta(s)}=s^2\int_1^\infty F(x)x^{-s-1}\,dx,
 \qquad
 \limsup_{\alpha\downarrow0}\alpha^2|\zeta(\rho+\alpha)^{-1}|
 \le |\rho|^2A.
 \tag{NB10}
\]
Consequently an exact double zero forces
\[
 \boxed{\limsup_NE_N\ge\frac4{|\rho|^4|\zeta''(\rho)|^2}>0},
 \tag{NB11}
\]
whereas multiplicity at least three forces \(\limsup_NE_N=\infty\). This is a coefficient-sensitive obstruction for (NB3), not an upper bound or a new simplicity criterion.

#### Verification details for the quantitative extraction

The multiplier in (NB9) has modulus one almost everywhere on the critical line; its values at the discrete zero set do not matter. Mellin transformation gives exactly
\(E_N=\|\sum_{n\le N}\mu(n)(1-\log n/\log N)\{1/(nt)\}+\mathbf1_{(0,1]}\|_{L^2(dt)}^2\).
Thus no limiting residue sum is assumed. For (NB10), first prove the integral identity in \(\Re s>1\), then continue using the bound defining finite \(A\). For every \(\epsilon>0\), the compact initial interval contributes \(o(1)\) after multiplication by \(\alpha^2\), while the tail contributes at most \(|\rho+\alpha|^2(A+\epsilon)\), since \(\int_1^\infty x^{-1-\alpha}\log x\,dx=\alpha^{-2}\). Taking \(\epsilon\downarrow0\) proves (NB10). If \(A=\infty\), (NB9) already gives unbounded limsup. These facts retain the original Möbius coefficients and allow arbitrary other multiplicities.


### 5.5 The local residue profile and its retained remainder

The complete-norm result (NB11) is separate from the following local calculation.

Let \(L=\log N\), and for an integer \(k\ge1\) set
\[
V_{N,k}(s)=\sum_{n\le N}\mu(n)n^{-s}
                 (1-\log n/L)^k.
\]
For \(0<\Re s<1\), the exact Perron representation is
\[
V_{N,k}(s)=\frac{k!}{L^k}\frac1{2\pi i}
       \int_{\Re w=2}\frac{N^w}{\zeta(s+w)w^{k+1}}\,dw .
\tag{ME1}
\]
Absolute convergence on this line justifies interchanging the Dirichlet series and the integral. For \(k=1\), [Bettin–Conrey–Farmer, Lemma2, PDF p.6](https://arxiv.org/pdf/1211.5191) records the corresponding full residue formula, retaining all distinct zero locations with their actual pole orders. Its later residue bound assumes simple zeros and a negative derivative moment.

Assume RH and fix an exact order-\(m\) zero \(\rho=1/2+i\gamma\). Write
\(\zeta(\rho+u)=c u^m g(u)\), \(c\ne0\), \(g(0)=1\), with \(g\) analytic and nonzero near zero. The coefficients are fixed as \(N\to\infty\); no uniformity in moving \(\rho\) is asserted.

One can shift a **finite** rectangular contour from \(\Re w=2\) to \(\Re w=-b\), with fixed \(0<b<1/2\), and horizontal sides avoiding poles. Retain the tails of the original line, both horizontal sides, the new vertical side, and every crossed reciprocal-zeta residue. Denote by \(G_{N,k}(s)\) only the sum of the kernel-pole contribution at \(w=0\) and the target-zero contribution at \(w=\rho-s\), including the factor \(k!/L^k\). The exact identity is then
\[
V_{N,k}(s)=G_{N,k}(s)+\mathcal R_{N,k}(s).
\tag{ME2}
\]
Here \(\mathcal R\) contains all the remaining terms just listed. It is not discarded or assumed small. A finite contour avoids assuming convergence of an infinite sum over inverse derivatives. At \(s=\rho\), the two selected poles merge and are interpreted by their combined contour.

Set \(s=\rho+z/L\). For a fixed compact \(K\subset\mathbb C\), enclose \(v=0,-z\) by \(|v|=R>\sup_K|z|\). Scaling \(w=v/L\) gives exactly
\[
\begin{split}
\zeta(\rho+z/L)G_{N,k}(\rho+z/L)
 &=\frac{k!}{2\pi i}\int_{|v|=R}
 \frac{e^v z^m}{v^{k+1}(v+z)^m}
 \frac{g(z/L)}{g((z+v)/L)}\,dv\\
 &=\frac{z^m}{(m-1)!}\int_0^1
       u^{m-1}(1-u)^k e^{-zu}\,du
       +O_{K,\rho,k}(|z|^m/L).
\end{split}
\tag{ME3}
\]
The second equality follows either by residues or convolution of the inverse Laplace transforms of \(v^{-k-1}\) and \((v+z)^{-m}\). The regular-factor ratio is \(1+O(1/L)\) uniformly on the contour. In particular the unknown leading coefficient \(c\) cancels. The remainder has its displayed factor \(z^m\), including at \(z=0\).

Define the entire model error
\[
E_{m,k}(z)=1-\frac{z^m}{(m-1)!}
                 \int_0^1u^{m-1}(1-u)^k e^{-zu}\,du.
\]
Then the **actual** error is
\[
1-\zeta(\rho+z/L)V_{N,k}(\rho+z/L)
 =E_{m,k}(z)-\zeta(\rho+z/L)\mathcal R_{N,k}(\rho+z/L)
       +O_{K,\rho,k}(|z|^m/L).
\tag{ME4}
\]
This is the transfer condition that must be paid. Squaring the error retains the signed cross term with \(\mathcal R\); the selected local residues are not a separately nonnegative contribution to the full norm.

For the requested linear taper,
\[
E_{1,1}(z)=\frac{1-e^{-z}}z,\qquad
E_{2,1}(z)=\frac{2(1-e^{-z})}z-e^{-z}.
\tag{ME5}
\]
Both have value one at zero; the double profile has derivative zero there, as required by \(1-\zeta V=1+O((s-\rho)^2)\). In particular a surviving endpoint term cannot be omitted. With \(\operatorname{Si}(Y)=\int_0^Y\sin y/y\,dy\),
\[
\begin{split}
\int_{-Y}^Y|E_{1,1}(iy)|^2dy
 &=4\operatorname{Si}(Y)-4(1-\cos Y)/Y \longrightarrow2\pi,\\
\int_{-Y}^Y|E_{2,1}(iy)|^2dy
 &=2Y+8\operatorname{Si}(Y)-16(1-\cos Y)/Y\\
 &=2Y+4\pi+O(Y^{-1}).
\end{split}
\tag{ME6}
\]
Thus the simple profile is square integrable; the double profile is not. In Fourier language \(E_{2,1}\) is the transform of \(2\mathbf1_{[0,1]}-\delta_1\).

For a fixed \(Y\), the model contribution on \(|t-\gamma|\le Y/L\), with the Nyman–Beurling weight \(dt/(2\pi(1/4+t^2))\), is
\[
\frac1{2\pi|\rho|^2L}
       \int_{-Y}^Y|E_{m,k}(iy)|^2dy+O_{\rho,Y,k}(L^{-2}).
\tag{ME7}
\]
Equation(ME7) becomes the leading **actual** local norm only if the scaled remainder term in(ME4) is \(o(1)\) in this fixed-window \(L^2(dy)\) norm. No such estimate is obtained here. In particular(ME6) alone does not prove actual nonconvergence.

The taper comparison has a complete model answer. For integers \(k\ge m\), put \(w=u^{m-1}(1-u)^k/(m-1)!\). Integration by parts \(m\) times yields
\[
E_{m,k}(z)=\int_0^1p_{m,k}(u)e^{-zu}\,du,\qquad p_{m,k}=-w^{(m)}.
\tag{ME8}
\]
The endpoint data give \(\int_0^1u^jp_{m,k}(u)\,du=\delta_{j0}\) for \(j<m\). Among all \(L^2(0,1)\) functions with those moments the minimum squared norm is \(m^2\): the minimizer is the endpoint reproducing kernel for polynomials of degree below \(m\). For \(k=m\), \(p_{m,m}\) has degree \(m-1\) and is exactly that kernel. Thus
\[
\frac1{2\pi}\int_{\mathbb R}|E_{m,m}(iy)|^2dy=m^2;
\qquad p_{2,2}(u)=4-6u.
\tag{ME9}
\]
This explains the classical multiplicity-squared constant; it is not a new arithmetic lower-bound theorem. [Burnol, Theorem1.3](https://arxiv.org/pdf/math/0103058) supplies the legitimate global Nyman–Beurling lower bound. The internal continuation review checks its one-sided support and weighted-jet normalization. Support length alone is insufficient: on the centered interval [-1/2,1/2], the constant one satisfies the two double-zero model moments with squared norm one. The full \(\zeta V\) is not bandlimited merely because \(V\) is finite.


[Separate same-model continuation review, §6](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
