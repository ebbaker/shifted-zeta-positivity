# VCD-GT-E21 r1 — Exact interaction evolution and the Riccati bound

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded executor dispatch
**gpt-6.1-sol / ultra**. Independent serving-model and actual effort
metadata were unavailable.

**Proved in-note on the independently paid tube, pending separate
internal assessment.** The occupation-to-snapshot comparison uses
the separate bound proved in [E20 Note40 (13)][e20], whose internal
assessment is also pending. These are quantitative
intermediate estimates and a scoped failure of the combined allowance
to exclude one exception at fixed collar. [Frozen E21 r1][request] ·
[Audit18][audit] · [Result index][results] · [Cluster18][cluster] ·
[Controls12][controls] · [Avoid index][avoid] · [Classification01][a01] ·
[Premises02][a02] · [Scope07][a07] · [Joint estimates12][a12] ·
[Sibling reuse15][a15]

## 1. Pair contour and the complete deflated PDE

Let \(H(t,z)\) be the unchanged complete canonical theta field in
physical time \(0\le t\le1/2\), with \(\partial_t H=-H_{zz}\).
Let \(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\), \(d\ge0\) and
\(\max(2,4\sqrt d)\le a\le L\). On a separately paid count-two tube
\(I=[t_0,t_1]\), the continued conjugation-invariant pair consists of
the two occurrences of \(Q=(z-c(t))^2-D(t)\), where \(c\in[T,2T]\),
\(D\in\mathbb R\), \(|D|\le d\ell^2\). Every exterior occurrence
\(\rho_j\) has \(|\rho_j-c|\ge r_0:=a\ell\), while the targets have
distance at most \(r_0/4\). All sums include multiplicities. Define
\[
 w_j=\rho_j-c,\qquad m_j=(w_j^2-D)^{-1},\qquad
 S_p=\sum_j m_j^p,\qquad M=S_1.
\]
The source strip \(|\Im\rho|\le1\) and the uniform complete unit
count on the closed time slab are the accepted inputs of
[TND-O Note21 (1)–(2)][o21] and [its internal assessment][o07].
Write \(C_{\rm u}\ge1\) for a common upper bound on its unit-count
and safe-line constants, so
\(\#\{\rho:v\le\Re\rho\le v+1\}\le C_{\rm u}\log(2+|v|)\) for each
real \(v\).

The source envelope used in [GT Note21 §1][gt21] bounds the absolute
cosine integrand on \(u\ge0\) by a constant times
\(\exp(9u+\Re(t)u^2+|\Im z|u-\pi e^{4u})\). It gives joint
holomorphy in \(t,z\) by domination on compact sets, also with the
polynomial factors introduced by differentiation. For
\(t\in[0,1/2]\), absorb \(9u+u^2/2\) into a constant plus
\((\pi/2)e^{4u}\), reserve \(\exp(-(\pi/4)e^{4u})\) for integration
and maximize \(ru-(\pi/4)e^{4u}\) for \(r=|z|\). The resulting
bound \(\log\max_{|z|=r}|H(t,z)|=O(1+r\log(2+r))\) gives order at
most one. The positive canonical source gives \(H(t,0)>0\) at
every real time in the slab.

Fix any \(t_*\in I\) and use the positively oriented circle
\(\Gamma=\{|z-c(t_*)|=r_0/2\}\). It encloses the chosen two
occurrences and has a strict margin to all zeros at \(t_*\).
Rouché's theorem gives the same count for nearby times, including
complex time in a sufficiently small neighborhood. For a holomorphic
field \(F(t,z)\) with this count put
\[
 J_k(t)=\frac1{2\pi i}\oint_\Gamma z^k\frac{F_z}{F}\,dz
 \quad(k=1,2),\qquad
 c=J_1/2,\qquad D=J_2/2-c^2,\qquad Q=(z-c)^2-D .
 \tag{1}
\]
The expressions give the counted symmetric coordinates through a
double, so \(c,D\) are analytic locally. On the real paid interval
the contour follows the same pair. The quotient \(A=F/Q\) is
jointly analytic and zero-free inside \(\Gamma\) near \(t_*\).
All its \(z\)-poles are removable by the counted multiplicities,
and the Cauchy integral of its jointly analytic boundary values
provides the joint extension. Put \(g=A_z/A\).

For \(\partial_t F=-F_{zz}\), insertion of the factorization gives
\[
 \frac{A_t}{A}=-(g_z+g^2)
  +\frac{2u c'+D'-2-4u g(c+u)}{u^2-D},\qquad u=z-c .
 \tag{2}
\]
The undivided identity makes the numerator of the quotient vanish
to the multiplicities of the roots of \(Q\). Write \(\zeta^2=D\),
\(z_\pm=c\pm\zeta\), \(h_0(u)=u g(c+u)\), and let
\(I_h(u)=\beta_0+\beta_1 u\) interpolate \(h_0\) at
\(\pm\zeta\), with value and derivative at zero when \(\zeta=0\).
Then \(2u c'+D'-2=4I_h(u)\), since both sides are linear and
their interpolation data agree. Here
\(\beta_1=(g(z_-)+g(z_+))/2\) and
\(\beta_0=D g[z_-,z_+]\), with the confluent convention. Thus
\[
 c'=g(z_-)+g(z_+),\qquad D'=2+4D g[z_-,z_+],\qquad
 \frac{A_t}{A}=-(g_z+g^2)-4 h_0[-\zeta,\zeta,u].
 \tag{3}
\]
The divided differences use analytic values also on the vertical
segment for \(D<0\). At a double, \(g[z_-,z_+]=g_z(c)\) and
\(D'=2\). This establishes the moving-coordinate part of
[Decision19 (12)][decision] through a collision.

For the canonical field, strip and unit count give
\(\sum_\rho|\rho|^{-2}<\infty\) by summing the two horizontal
tails in unit intervals, with the bounded part finite and no zero
at the origin. Order at most one gives the Hadamard product with
genus-one factors and prefactor \(e^{b_0+b_1z}\). Opposite
pairs multiply to \(1-z^2/\rho^2\). The grouped product converges
on compact sets by the inverse-square sum. It is even, so evenness
of \(H\) forces \(e^{2b_1z}=1\) off the zeros and thus \(b_1=0\).
The constant prefactor is \(H(t,0)\). This uses the same canonical
product as [GT Note21 §1][gt21]. Finite polynomials use the same
logarithmic-derivative argument below via their finite factorizations.

At any fixed time the deflated log derivative is the complete
log derivative minus \(Q_z/Q\). The divided difference
\(g[z_-,z_+]\) is the integral of \(g/Q\) on \(\Gamma\),
divided by \(2\pi i\), by residues. An additive constant
integrates to zero against \(1/Q\). For an exterior pole \(\rho\),
the analogous integral of \(1/((z-\rho)Q(z))\) equals
\(-1/Q(\rho)\), by the zero residue at infinity and the residue
at the exterior pole \(\rho\). This also computes the interior
residue at a confluent pair. The genus-one log derivative series
converges uniformly on the contour by the inverse-square bound,
and the resulting exterior reciprocal sum is absolute. Finally
\(Q_z/Q^2=-(1/Q)_z\) has zero integral. Consequently
\[
 M=-g[z_-,z_+]=-\frac1{2\pi i}\oint_\Gamma\frac{F_z/F}{Q}\,dz,
 \qquad D'=2-4DM .
 \tag{4}
\]
Conjugation of the exterior divisor makes \(M,S_2,S_3\) real,
with no sign bound on their complex summands.

## 2. Exact physical-time interaction law

Let \(F(t,z)\) first be a finite polynomial solving the same heat
equation, evaluated at a time when all roots are simple. For each
root \(\rho\), implicit differentiation and factoring out its
linear factor give \(\frac{d\rho}{dt}=F_{zz}(\rho)/F_z(\rho)
=2\sum_{\eta\ne\rho}(\rho-\eta)^{-1}\), with the sum over the
other roots of the polynomial. In this paragraph the indices
\(j,k\) exclude both target occurrences. Put
\(P=\sum_j w_jm_j\) and \(V=\sum_j w_jm_j^2\).
By (3), \(c'=-2P\), since the target sum \(g(z_-)+g(z_+)\)
gives \(-2w_jm_j\) for each exterior pole. The target
contribution to an exterior velocity is \(4w_jm_j\). Thus
\[
 w_j'=4w_jm_j+2P+2\sum_{k\ne j}(w_j-w_k)^{-1}.
\]
A common constant \(\lambda\) in the regular part of the log
derivative would add \(2\lambda\) to every root velocity and
to \(c'\). The shifts cancel in \(w_j'\) and in the equation
for \(D'\). Differentiating \(m_j\), inserting (4) and pairing
the \((j,k)\) and \((k,j)\) terms gives
\[
 M'=(2-4DM)S_2-8(S_2+DS_3)-4PV
     -4\sum_{j<k}\frac{w_jm_j^2-w_km_k^2}{w_j-w_k}.
 \tag{5}
\]
Indeed \(w_j^2m_j=1+Dm_j\). The symmetric quotient satisfies
\[
 \frac{w_jm_j^2-w_km_k^2}{w_j-w_k}
 =-m_jm_k-(D+w_jw_k)(m_j^2m_k+m_jm_k^2).
\]
This follows by first taking the difference of \(w_jm_j\) and
\(w_km_k\), then multiplying by \(m_j+m_k\) and subtracting
\((w_j-w_k)m_jm_k\). The sums over \(j<k\) of the expressions
\(m_jm_k\), \(D(m_j^2m_k+m_jm_k^2)\), and
\(w_jw_k(m_j^2m_k+m_jm_k^2)\) are \((M^2-S_2)/2\),
\(D(MS_2-S_3)\), and \(PV-S_2-DS_3\), respectively. For the
last equality the removed diagonal is \(\sum_j w_j^2m_j^3
=S_2+DS_3\). Substitution cancels the \(DMS_2\) and \(PV\)
terms and yields
\[
 \boxed{M'=2M^2-12S_2-16DS_3.} \tag{11}
\]
At a double this is \(2M^2-12\sum_j w_j^{-4}\). One exterior
occurrence gives \(-10M^2-16DM^3\).

To extend the finite identity through arbitrary multiple roots,
at the time in question perturb the finitely many root factors
to simple distinct locations, maintaining the degree and the
counts on either side of \(\Gamma\). Each perturbed polynomial
has its own polynomial heat evolution with the prescribed
time slice. At the reference time (1), (4), and their derivatives
are continuous in these polynomial data. In detail,
\[
 \partial_t(F_z/F)=-F_{zzz}/F+F_zF_{zz}/F^2,\qquad
 M'=-\frac1{2\pi i}\oint_\Gamma
       \left(\frac{\partial_t(F_z/F)}Q-\frac{(F_z/F)Q_t}{Q^2}\right)dz,
 \qquad Q_t=-2(z-c)c'-D'.
 \tag{6}
\]
The lower bounds for \(|F|,|Q|\) on the fixed circle persist for
small perturbations. Formula (1) gives \(c',D'\) using the same
\(\partial_t(F_z/F)\). Every exterior rational summand in
\(S_2,S_3\) converges with its displaced root occurrence, since
the denominators stay away from zero. This proves (11) for
the unperturbed polynomial, including multiple exterior roots
and a double target, by continuity of the derivative of a
symmetric observable at the multiple time.

For the canonical limit, at \(t_*\) truncate the complete product
of §1 by increasing radii, retaining every opposite group and
its conjugates and every occurrence at a repeated location.
For large enough radius the target factors are all present.
Let \(F_N\) take this truncated polynomial as time slice at
\(t_*\) and solve its polynomial heat equation
\(F_N(t,z)=e^{-(t-t_*)\partial_z^2}F_N(t_*,z)\). The operator
sum terminates on a polynomial. At \(t_*\) the products and
all spatial derivatives converge locally uniformly to those
of \(H\) by compact product convergence and Cauchy's integral
formula. Hence on \(\Gamma\) the time derivatives of the log
derivatives converge by (6). The analytic moments (1) give
convergence of \(c,D,c',D'\), and (4), (6) give convergence of
\(M,M'\). The exterior sums \(S_2,S_3\) are absolute: the
collar bounds the finite nearby terms and \(m_j=O(|\rho_j|^{-2})\)
as \(|\rho_j|\to\infty\). At \(t_*\) the terms for each retained
occurrence use exactly the canonical \(c,D\), since the
selected factors already agree. Passing (11) to the limit
proves the canonical identity at this time. Varying \(t_*\)
gives the result on the tube, with inward derivatives at its
ends. The local polynomial time neighborhoods may depend on
\(N,t_*\). All convergence was used at the single frozen time,
through derivatives of the contour observable.

## 3. Complete shell bounds and normalization

Use \(\sigma=(t-t_0)/\ell^2\), \(m=\ell^2M\),
\(\mu_j=\ell^2m_j\), and \(\delta=D/\ell^2\).
The scale \(\ell\) is fixed, so \(\partial_\sigma m=\ell^4 M'\).
Equation (11) yields
\[
 \partial_\sigma m=2m^2-12\sum_j\mu_j^2-16\delta\sum_j\mu_j^3.
 \tag{13}
\]
The collar gives \(|D|\le |w_j|^2/16\) and
\(|\mu_j|\le (16/15)L^{-2}|w_j|^{-2}\). Write \(q_0=16/15\).
For the near band \(|\Re\rho-c|<1\), the two closed unit
intervals starting at \(c-1,c\) give a count at most
\(4C_{\rm u}L\), since \(2+c\le3T\le T^2\). On each horizontal
shell \(n\le|\Re\rho-c|<n+1\), \(n\ge1\), use the two closed
unit intervals starting at \(c-n-1,c+n\). For either start \(v\),
\(2+|v|\le2T+n+3\le3T(n+1)\); therefore the shell count is at
most \(2C_{\rm u}(2L+\log(n+1))\). Shared endpoints can only
increase the bound. Every shell term has
\(|\mu_j|\le q_0 L^{-2}n^{-2}\). For \(p=1,2,3\),
\(\sum_{n\ge1}n^{-2p}\le2\) and
\(\sum_{n\ge1}n^{-2p}\log(n+1)\le3\). The latter follows from
\(\log(n+1)\le\sqrt n\) for \(n\ge1\) and the integral bound
on \(\sum n^{-3/2}\). The former follows from the integral
bound on \(\sum n^{-2}\). Since \(L\ge3\), the far sum is
bounded by
\[
 2C_{\rm u}q_0^p L^{-2p}(4L+3)
 \le 10C_{\rm u}q_0^p L^{1-2p}.
\]
The near sum is at most \(4C_{\rm u}q_0^p a^{-2p}L\).
Because \(a\le L\), the total is at most \(B_p L\), where
\[
 B_p=\frac{14 C_{\rm u} q_0^p}{a^{2p}},\qquad
 B=B_1,\qquad K=12B_2+16dB_3 .
\]
It follows that
\[
 |m|\le BL,\qquad
 \left|12\sum_j\mu_j^2+16\delta\sum_j\mu_j^3\right|\le KL,
 \qquad \partial_\sigma m\ge 2m^2-KL.                     \tag{14}
\]
This forcing bound depends on the signed identity followed by an
absolute estimate of its square and cube sums. Its near allowances
carry \(L/a^4\) and \(dL/a^6\), respectively.

The same shells verify the local deflated-field bound in
Decision19 §3. The accepted safe line of [TND-O Note21 (2)][o21]
gives \(|H_z/H(c+4i)|\le2C_{\rm u}L\), and the two targets
contribute less than one there. For \(|z-c|\le r_0/2\),
subtract \(g(c+4i)\) using the absolutely convergent differences
\((z-\rho)^{-1}-(c+4i-\rho)^{-1}\) over exterior roots.
Each near difference is bounded by \(2/r_0+1/3\).
On shell \(n\ge1\), the two denominator factors are at least
\(n/2,n\), with numerator at most \(9/2\), so the difference
is at most \(9/n^2\). The displayed shell sums give
\(|g(z)|\le 8C_{\rm u}L^2/a+95C_{\rm u}L\).
For every spatial derivative of order at least one the
exterior reciprocal-power sums converge absolutely and
locally uniformly by the same estimates.

## 4. Scalar comparison and transport cost

Let \(h=\sqrt{KL/2}\), \(k=\max(BL/h,2)\), and
\(u_0=\operatorname{arccoth}k>0\). The function
\(v(\sigma)=-h\coth(2h\sigma+u_0)\) solves
\(v'=2v^2-KL\) and satisfies \(v(0)=-hk\le -BL\le m(0)\).
The difference satisfies
\((m-v)'-2(m+v)(m-v)\ge0\). Multiplying by the positive
integrating factor and integrating gives \(m\ge v\) on
the paid tube. Since \(\coth x\) decreases for positive
\(x\), the bound independent of the finite initial value is
\[
 \boxed{m(\sigma)\ge -h\coth(2h\sigma)\quad(\sigma>0).}     \tag{15}
\]
For any fixed positive lower buffer in scaled time, this gives
a lower allowance of order \(-\sqrt L\) in place of the
count-scale \(-BL\). The bound is one-sided and its lower
barrier still permits any fixed negative normalized margin
for large \(T\). The elapsed buffer requires a tube paid for
at least that long.

For \(s\ge0\) inside the paid tube, \(m\ge v\) gives
\[
 \int_0^s(-m)_+\,d\sigma
 \le\frac12\log\frac{\sinh(2hs+u_0)}{\sinh u_0}
 \le hs+\frac12\log\frac{k+1}{2}.                        \tag{16}
\]
Indeed the quotient of hyperbolic sines is at most
\(e^{2hs} e^{u_0}/(2\sinh u_0)=e^{2hs}(k+1)/2\).
Since \(-m\le (-m)_+\) and
\(\int_{t_0}^{t_0+\ell^2s}M\,dt=\int_0^s m\,d\sigma\),
\[
 \exp\!\left(-4\int_{t_0}^{t_0+\ell^2s} M\,dt\right)
 \le e^{4hs}\left(\frac{k+1}{2}\right)^2
 =O_{a,d,C_{\rm u}}(L)\exp(O_{a,d,C_{\rm u}}(s\sqrt L)).
 \tag{17}
\]
Directly integrating only \(m\ge -BL\) gives \(e^{4BLs}\).
For fixed \(s>0\) the improved upper allowance still grows.
Solving (4) for \(D\) over a tube still needs its independent
incoming value \(D(t_0)\). The initial bound used here is on \(M\).

## 5. Persistence and the occupation comparison

With \(K_1=2B^2+K\), (13)–(14) imply
\[
 \left|\frac d{dt}(\ell^2M)\right|
 \le L^2(2B^2L^2+KL)\le K_1 L^4 .                       \tag{18}
\]
If \(\ell^2M(t_*)\le-\epsilon\) for \(\epsilon>0\), then
\(\ell^2M\le-\epsilon/2\) on either side of \(t_*\) for length
\(\Delta=\epsilon/(2K_1 L^4)\) when the entire chosen interval
lies in the paid tube. With strict negativity alone, the
length guaranteed by this modulus can tend to zero with the
margin. Tube and collar acquisition are separate premises.

For several such pairs at one snapshot, require a common
one-sided interval on which each tube is paid. The continued
pairs remain distinct. At a time of coincidence, the local
contour around their common pair determines the unique
continuation near that time, by (1). Coincidence would
therefore be open as well as closed in the common interval,
contradicting distinctness at the snapshot. Thus if
\(n_\epsilon\) such pairs are counted at \(t_*\), their combined
negative occupation is at least \(\Delta n_\epsilon\).
By [Note38 (8)][gt38], full negative interactions are a subset
of those with \(S_R<0\) for \(3\le R\le T/4\), on every slice
of this same pair class.

Use the separate occupation bound [E20 Note40 (13)][e20], which
pays the fixed target in [Decision19 (8)][decision]. Put
\(C_{a,b}=B_b(93/b^2+279/(ab^3))\) and \(C_\chi=32D_\chi/3\).
Dividing that target by \(\Delta\) gives the snapshot allowance
\[
 n_\epsilon\le C_{a,b}\frac{T}{L\Delta}
                  +C_\chi\left(\frac12+\frac L{3a}\right)L^3 .
 \tag{19}
\]
At the modulus-guaranteed \(\Delta\) this is
\(O(TL^3/\epsilon+L^4)=O(TL^3/\epsilon)\) for fixed \(a,b,d\)
and fixed source constants. The absorption holds even for
variable \(\epsilon\) in the nonempty case \(\epsilon\le BL\),
since \(L^2\le T\) for \(T\ge64\). At fixed \(\epsilon>0\)
the first term of (19) exceeds the order of the old
\(C_b' TL e^{-2ba/3}\) snapshot allowance by two powers of \(L\).
Even if a paid tube came with independently guaranteed
negative visibility of length \(\Delta\asymp\ell^2\), (19)
would only give \(O(TL)\). The tube length by itself supplies
no such sign guarantee. For any possible \(\Delta\le1/2\),
the first term on the right of (19) is at least \(2C_{a,b}T/L\).
For fixed \(a,b\), the displayed bound therefore cannot meet
the upper-allowance test \(<1\) as \(T\) grows. Intersecting
it with the old slice and packing allowances leaves the same
failure of that exclusion test. These comparisons concern
upper allowances on this fixed-collar class. They give no
lower bound on actual exception counts, occupation or lifetime.

## 6. Premise controls and equally informed comparison

Documentary and algebraic replay of [Controls12][controls],
[Decision19 §4][decision], and [Synthesis39 §4][gt39].
The law (11) is structural. The control checks distinguish
its heat and divisor premises from the canonical count and
occupation inputs.

| Control | Premise tested and consequence |
| --- | --- |
| Quadratic and even quartic physical heat controls | They may share a local collar through a double and satisfy (11) by the finite proof. Their finite divisor fails the canonical growing population law, though a coarse logarithmic upper count can still hold. The Riccati estimate permits these collisions. |
| Euler-factor translates | Their positive even sources can retain the heat law. The modified field changes the full theta source and fails the canonical endpoint count discrepancy in the documented class. The coarse upper count alone would not detect a linear discrepancy. Canonical uniform transverse density for the E20 comparison is untested for these modifications. |
| Weighted-square, finite-source, finite-score and finite-prime controls | Full reflected unit-weight theta equality fails. The documented endpoint-defective classes also fail the uniform strip. Finite scores or endpoints supply no complete count, safe-line or transverse-density payment. |
| Reflected super-Gaussian | It preserves reflection and physical heat evolution, and the documented control fails order at most one, used for the canonical opposite-paired product passage. Canonical count and moment transfer are unassigned. |
| Smooth shape and positive-primitive controls | These change the theta arithmetic. The canonical strip, unit-count and transverse inputs remain untested for their flows. |
| Fixed-event atoms and finite/compact-profile controls | Their sources differ from theta. The documented finite-type population has no canonical \(T\log T\) growth. Local heat identities and a coarse unit upper count may still hold. |
| RH-conditional normalized endpoint mergers | Their preservation list keeps the RH assumption and changes ordinary Dirichlet-series arithmetic. Uniform canonical count and moment transfer remain untested. The local law itself admits \(D=0\). |
| Varied observation kernel and fractional-profile relaxation | The former lacks the physical cosine/Newman readout. The latter lacks the full integer zero divisor used by (1), (4) and the occupation count. |
| Note34 opposite-sign equal-count slices | The supplied slices pass the stated strip, count, moment and transverse-density upper bounds with enlarged constants. They change the theta source and supply no common paid physical heat tube for the evolving identity and occupation estimates. |

An equally informed direct calculation has the same complete field,
heat law, integer divisor, paid tube, collar, symmetric coordinates,
full signed interaction, source moments, occupation input and incoming
\(D\) value. It has (11)–(18) and (19) with the same constants and
visibility requirements. The fixed-collar gain is in the conditional
interior and transport allowances. The combined occupation and
visibility inference stops at the allowance comparison above.

[request]: ../research-progress/handoffs/VCD-GT-E21-r1.md
[decision]: ../brainstorm/notes/19_VCD_GT_B11_FIXED_COLLAR_DECISION_20261117.md
[audit]: ../reviews/18_VCD_GT_B11_DYNAMIC_INPUT_AUDIT_20261117.md
[e20]: 40_VCD_GT_E20_FIXED_COLLAR_TIME_OCCUPATION_20261117.md
[gt21]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[gt38]: 38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
[gt39]: 39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md
[o21]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[o07]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a15]: ../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
