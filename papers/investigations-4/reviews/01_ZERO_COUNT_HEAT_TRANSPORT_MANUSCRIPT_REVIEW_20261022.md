# Zero-count, heat-transport and Hodge manuscript: analytic review

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Disposition: the self-contained manuscript passes the internal analytic
checks below, subject to its stated hypotheses.** This is parent integration
plus separate delegated readings by the same model, not independent
specialist, human, or cross-model validation. No priority assessment is
claimed. The main results do not depend on a numerical computation.

Reviewed source: [maintained manuscript](../manuscript/zero_count_heat_transport/main.tex)
and its ten included section files. The [README](../manuscript/zero_count_heat_transport/README.md)
maps results to earlier notes. The [extensions note](../notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md)
distinguishes additions from consolidation.

## 1. Exact localized energy and normalized covers

The boundary floor b>0 gives constant valence N for every target |w|<b
by the homotopy f−sw. The nonnegative holomorphic area formula then gives

\[
\int_{|f|<\varepsilon}|f'|^2|f|^{p-2}\,dA
=N\,2\pi\int_0^\varepsilon r^{p-1}\,dr
=\frac{2\pi}{p}\varepsilon^pN.
\]

The factor 4π in W_<ε follows from its additional factor two at p=1.
Near an order-m zero the radial integrability exponent is mp−1; p>0 is
exactly sufficient for this argument. The constant nonzero case has N=0
and empty low-value region. The full-energy bound W≥4πbN follows by
letting ε increase to b; az^m on a disk checks sharpness.

For w^q=f, each of the q sheets contributes
|f′|²|f|^(2/q−2) to the energy of q dw. The total is therefore
πq²ε^(2/q)N, not a q or q³ prefactor. At a multiplicity-m root the
normalization has d=gcd(q,m) charts, with z−a=ξ^(q/d),
w=ξ^(m/d)v(ξ). Thus dw is holomorphic on each chart. The proof permits
disconnected covers and normalizes over a neighborhood before restriction
to the bordered surface.

## 2. Regularized divisor, field error and local bias

The compact potential and its first radial derivative match at ε.
It is C¹,¹ near the target cutoff; composition remains so even when f′
vanishes there. Hence there is no interface measure at a critical cutoff
level. At an m-fold zero its small-circle flux is O(r^(mp)), so there is
no atom for fixed ε. The exact mass and weak divisor limit then follow
from the area identity and concentration on disjoint root disks.

A separate reader identified a genuine class-definition issue in the
first draft: the p=1 potential is Lipschitz but not C¹ on the complex
plane at zero. The final optimality statement uses globally Lipschitz
radial potentials, C¹ for positive radius, with logarithmic exterior.
Within that class the exterior derivative at ε forces Lipschitz constant
at least 1/ε, and every p≥1 profile attains it. For p>1 it is also C¹
at zero. No field-error theorem needed differentiability at zero.

Pairing potentials with Δψ gives η‖Δψ‖₁/(2πε) for p≥1 and
η^p‖Δψ‖₁/(2πpε^p) for p<1. The cubic cutoff has
‖Δψ‖₁=32π/9, hence allowance 16η/(9ε). Its support is compactly
contained in the domain; it is not silently treated as a plateau.

The root-disk floor |f|≥c_j|z−a_j|^(m_j) confines each component of
the low-value measure to radius (ε/c_j)^(1/m_j), with exact mass m_j.
This proves the stated Lipschitz-test bias. The complement is explicitly
compact. The zero-free case is separated before defining M=max m_j.
Balancing the errors with fixed local data gives the stated upper
exponents 1/(M+1) and p/(pM+1); no minimax assertion follows.

For the smooth kernel (1/2)log(|f|²+ε²), direct differentiation gives
density ε²|f′|²/[π(|f|²+ε²)²]. Green's identity gives the boundary
multiplier |f|²/(|f|²+ε²). Taking total variation yields the explicit
absolute bias ε²V_boundary/(b²+ε²), without assuming a bias sign.
The maximal radial derivative is 1/(2ε), and the energy comparison
constant is 9/(32√3πε). Both constants were checked directly.
The time derivative is the Laplacian of
Re(conj(f)f_t)/(|f|²+ε²); backward heat supplies no automatic sign.

## 3. Real births, complex residues and complete boundary conventions

Joint analyticity justifies the actual bivariate Taylor expansion, not
a formal ill-posed heat series. With s=ε² and w=εy, the normalized
field converges to the heat polynomial. Gaussian orthogonality proves
the required Hermite roots real and simple. Implicit branches and a
separate spatial Rouché argument exhaust the local cluster.

For negative real s, every nonzero Hermite branch has a nonzero
imaginary leading displacement. The odd central branch is even in ε:
w_0(−ε)/ε=−y_0(−ε) is in the same unique normalized zero neighborhood.
It is consequently holomorphic in s and remains real. Thus the real
count changes from m mod 2 to m, while complex multiplicity stays m.

With orientation dt∧dx, the angular current −darg(H+iH_x)/(2π) has
positive event charge floor(m/2). The complete balance is
N_b−N_a+Q_left−Q_right=2Σ floor(m/2).
The sign-change definition includes nontransverse wall contacts; a
transverse lower crossing removes a root and an upper crossing adds one.
A single cap retains its endpoint arctangents. Boundary events are not
included by applying a regular-cap formula at a singular endpoint.

Contour power sums and Newton identities construct the entire cluster
polynomial. A Cauchy integral of the quotient supplies a jointly
holomorphic, nonzero unit near the closed product. Each squared local
root difference contributes one power of s, giving discriminant order
binom(m,2). Simultaneous spatial events add, with nonvanishing
cross-cluster factors. Complex event times need not be real.

The separate transport audit checked the nonzero-unit matrix homotopy
and the regular-target resultant proof of degree agreement. A target
smaller than the boundary jet floor keeps the whole target homotopy
nonvanishing. Each regular complex inverse image contributes +1.
The resultant's constant Vandermonde sign changes no winding.

A scalar indentation contributes qΔθ/(2π); a clockwise semicircle
contributes −q/2. This is not a universal real-current half-charge.
Exact controls give discriminants 8t for z²−2t and 864t³ for
z³−6tz: both real birth charges are one, whereas complex charges
are one and three.

## 4. Cover topology and differential choice

A lifted triangulation gives χ(X_q)=q−Σ(q−gcd(q,m_j)) over a disk.
At q=2 this is 2−B_odd, so the normalized singular-fiber excess over
a regular fiber of complex count N is 2Σ floor(m_j/2).
It is not a permanent topological difference between two regular fibers.

For dz/w, even multiplicity 2r gives poles of order r on two components;
odd multiplicity 2r+1 gives order 2r on one normalized component.
The energy 2∫1/|f| is finite at a simple zero, logarithmically divergent
at a double zero and power divergent at higher multiplicity.
Its coefficient and period scaling retain the analytic amplitude.
The exact differential 2 dw has a different contract.

## 5. Pair matrices and dynamics

The clock perturbation estimate uses gap error at most 2δ.
The inverse-square derivative gives entry error
4δ/(d−2δ)³; summing both sides and the Laplacian diagonal gives
operator allowance 16δΣ(d−2δ)^(-3). The Loewner factors are
(1±2δ)^(-2). Complete-graph comparison gives the stated spectral floor.

The full selected-root law is x_i′=2S_i+2b_i, with b_i=U_z/U.
For E=−logΔ, the identities ∇E=−2S, Hess E=2L and
‖S‖²=2Σ_(i<j)gap^(-2) give the complete forced energy law.
The exterior term is retained. Normalized weights include their
rescaling derivative; the physical and unfolded formulas are distinct.

The centered contraction uses mixed weights
1/[(y_i−y_j)(c_i−c_j)], not the Hessian at a single configuration.
The center equation and full residual are stated. Its convolution bound
assumes a continuous nonnegative error allowance; this is an estimation
interface, not a paid theta dissipation result.

For a whole polynomial population, u=x/√(2t) and s=log t give a
gradient flow with Hessian at least I/2. The norm and potential-gap
rates are (t_0/t)^(1/2) and t_0/t respectively. This is deterministic
Hermite relaxation, not convergence in distribution to GUE.

## 6. Statistics and physical cap normalization

Ordered pairs omit the label diagonal only. Repeated locations still
give a zero-gap atom. The inverse-square targets are π²/3 for a clock
and 2π²/3 for the sine kernel, derived explicitly. The sparse-modification
proof keeps vague pair convergence while adding a duplicate or an
arbitrarily near pair. Density-one simplicity is compatible with such
sparse exceptions. Singular-moment transfer retains both near-zero
uniform integrability and far-tail control.

The tent-test upper is π²δ³/18. With acquired error e_m(δ), a total
strictly below 2/m excludes a duplicate; below 1/m excludes gaps ≤δ/2.
These are conditional finite tests, not acquired canonical estimates.

At (1,0) on S³, the outward-oriented tangent basis is
(∂y_1,∂x_2,∂y_2), and α∧dα evaluates to +2.
Unitary invariance gives integral 4π². Pullback by G/|G| is exactly the
physical connection; the real normalization derivative adds no phase.
This establishes the sign and factor of the total boundary degree.

In projective coordinates G=h(q,1), the common phase of h remains.
The cap is k_ε/(2π) times its central imaginary-time phase increment.
The fixed-radius projective side vanishes, but the two imaginary faces
close the balance; in the real-type case their signed contributions
agree. The final source explicitly distinguishes full-boundary equality
from any unproved equality of individual discriminant edges and
physical caps.

Cross-section normalization also checks:
tr L(y)=‖A(y)‖_F²=mQ_m, so the physical positive pair term is
4mρ²Q_m. No pair-order or unfolding factor is missing.

## 7. Complete-source theta proof

A separate reader checked the entire proof, including every tail:
b_-=1−3/(2π), b_+=(1−16e^(-3π))^(-1), c=1/(4e),
κ=16πe^(4L)−2t, and t=(4πe^(4L)−9)/(2L), L≥2.
The near/right quadratic bound, the far-left maximum argument, and the
denominator interval of width κ^(-1/2) yield the explicit first-moment
allowance. Every mode is covered by the global b bounds.

Real Fourier values and derivatives are bounded using only this first
moment. Strict comparisons with sin β and cos β prove existence,
uniqueness, order and simplicity of the first K positive real roots.
The rate O_K((L√κ)^(-1)) passes directly to the normalized matrix;
the physical error is O_K(L/√κ) against a leading matrix of size L².

Only locations are needed for logΔ=−m(m−1)log L+C_m+o(1).
Integrating the exact forced law proves cumulative exterior cancellation.
It does not differentiate the o(1) term or import the earlier complex-time
saddle-jet theorem. The physical energy diverges, precluding a
nonincreasing tail, without a pointwise derivative-sign claim.

## 8. Controls, source provenance and limits

The manuscript's polynomial, cosine and same-root/different-phase controls
are proved analytically. They pass the universal identities. In the wider
[control register](../../../result-summaries/12_collision_controls_and_screening.md),
Euler-factor controls change the canonical source; weighted-square
controls change its coefficients and fail full reflection; reflected
and smooth primitive-compatible controls fail its canonical square
expansion; finite-prime controls fail full reflection; normalized endpoint
controls fail ordinary Dirichlet-series arithmetic. Thus no such family
is being excluded by a qualitative property it shares with theta.

The complete-source theorem uses the unchanged displayed series, but its
late clock conclusion is not an event exclusion. The displayed asymptotics
fix rank; the explicit finite tests also permit sufficiently slow growing
rank, as clarified in the continuation review below. No global minimum
gap, GUE relaxation, RH, endpoint simplicity, or new opposing
canonical signed estimate is claimed. RHE's already positive fixed-window
trace and its stopping decision remain unchanged.

The primary Rodgers–Tao, Montgomery and Joyner–Smilansky sources were
consulted for normalization and context. The main calculations are proved
in the manuscript. The existing RHE04 certificate appears only in the
appendix and was not rerun; it is not a premise of any main theorem.

## 9. Build and presentation verification

The final source compiled successfully with the desktop editor compiler
and with latexmk/pdfTeX (TeX Live 2023). The final log has no undefined
references/citations, multiply defined labels, overfull or underfull boxes,
or other warnings. The PDF has **41 pages**. Text extraction found no
unresolved reference marks. Every final page was rasterized and visually
inspected in contact sheets; formula-heavy pages were also viewed
individually. No clipping, overlapping formulas, missing glyphs or broken
equation numbering was observed.

The final PDF is 578,745 bytes, below the approximate 1 MB repository
limit. Build intermediates and page images remain in temporary storage.
The maintained project has an auxiliary-file ignore list. No new
manuscript snapshots, Git commits or Investigations 5 folder were created.

The completed milestone includes the base overview, progress register,
extensions note, manuscript source crosswalk and history routing.
History remains uniquely registered in home 11 / archive 0001.
Final local-link and whitespace validation is recorded below.



### Final file validation receipt

Final integration checked 113 local link targets across the seven new Markdown records; all resolve. No trailing whitespace was found in those files, and the scoped repository diff check passed. The 214 LaTeX labels are unique and every reference resolves. The PDF and all eleven TeX source hashes match the [build record](../manuscript/zero_count_heat_transport/BUILD_RECORD.json). The largest new deliverable is the 578,745-byte PDF. The build record establishes source/output identity and document checks, not mathematical validity.


### Continuation review and scope clarification — 22 October 2026

Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra, ultra**. The [continuation note](../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md) separates proposed C² stability estimates from the growing-window consequence already available from explicit finite tests. The manuscript paragraph following Theorem 9.3 now permits growing K when K M_1/L tends to zero, while retaining the separate temporal and exterior-force requirements. No theorem statement was changed.

Both compilers succeeded again with no warnings. Text comparison shows that only PDF page 37 changed; that page was re-rendered and visually checked. The PDF remains 41 pages and is 578,745 bytes. The build record now contains the revised PDF and all eleven source hashes. The initial all-page presentation check remains applicable to the unchanged pages. This clarification does not establish a growing-population dynamical law.
