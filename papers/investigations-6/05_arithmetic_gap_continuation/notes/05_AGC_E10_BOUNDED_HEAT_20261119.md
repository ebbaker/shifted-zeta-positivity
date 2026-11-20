# AGC-E10 module B: the bounded horizontal heat problem

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit helper dispatch: **gpt-6.1-sol,
reasoning effort ultra**. Independent serving-backend model and effort
attestation are unavailable to this helper; dispatch is recorded separately
from actual backend metadata. Written analytical derivation, followed by
one correction pass; no numerical verification or independent review is
claimed.

**Status:** proved elementary conditional representation and bounds below.
The fixed canonical data, reference count, contour clearance and a useful
discriminant margin have not been acquired. This is a finite quantitative
comparison under [B01](../brainstorm/notes/02_AGC_B01_FIXED_CELL_COMPARISON_20261119.md),
not an RH-equivalent reformulation or a new coverage claim. The
[result index](../../../../result-summaries/README.md) and
[patterns index](../../../../avoid/README.md) route the inherited results
and cautions; particularly relevant are
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
[approximation/residual results](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Frozen physical field and the information used

Keep exactly the physical holomorphic reference of manuscript
[Section 5](../manuscript/sections/05_arithmetic_source.tex), with the same
theta field H and fixed cutoff N. Put

    x_- = X-A,  x_+ = X+A,  L = 2A,  I = (x_-,x_+),
    0 < U < t_* <= 1/2,  0 < h <= 1,  X-A >= 200,
    N² <= (X-A)/(4π)+(t_*-U)/16,
    (X+A)/(4π)+t_*/16 < (N+1)².

The natural cutoff is therefore N on the entire closed time-rectangle.
Write every physical field in backward time u=t_*-t and define

    E(u,z) = H_{t_*-u}(z)-P_N(t_*-u,z),
    R(u,z) = R_N(t_*-u,z),
    R_N = ∂_t P_N + ∂_z² P_N.

The exact equation from manuscript
[Section 6](../manuscript/sections/06_residual_transport.tex) is

    ∂_u E = ∂_z² E + R.                                      (1)

It has diffusion coefficient one. In particular, it is not the
coefficient-1/4 equation in the s variable. The full forcing is

    R_N(t,z) = Σ_{n=1}^N [R_n(t,s_+(z))+R_n(t,s_-(z))],
    s_±(z) = (1±iz)/2,
    R_n(t,s) = -(p_n(t,s)/4)
        [b + t a_n² b + (t/2)(b²+a_n c) + (t²/4)a_n² b²],     (2)
    a_n = α(s)-log n,  b=α'(s),  c=α''(s).

There is no replacement of (2) by zero, and no subtraction of an
unacquired correction from P_N. The initial error includes both the
individual term errors and the complete omitted Riemann--Siegel remainder.

For each fixed real height y in [-h,h], the complex-valued function
e_y(u,x)=E(u,x+iy) obeys e_{y,u}=e_{y,xx}+R(u,x+iy). Its complete data are

    f_y(ξ) = E(0,ξ+iy),
    g_-(v,y) = E(v,x_-+iy),   g_+(v,y) = E(v,x_++iy).           (3)

These are actual restrictions of E, not artificial zero boundary values.
The height is a parameter; the evolution acts only on real x. Formulae
below also depend holomorphically on a complex parameter η replacing y
whenever all translated segments x+iη lie in one common analytic domain
with the stated bounds. The frozen rectangle itself supplies the needed
data only for real y; no such extra parameter domain is assumed.
No additional boundary integral at y=±h is present in this horizontal
problem. Bounds there are relevant only to uniformity in the parameter
or a later Cauchy estimate.

For a simple classical version, assume E is continuous on
[0,U]×[x_-,x_+]×[-h,h], is C¹ in u and C² in x on a neighborhood of
that set, and is holomorphic in z on a neighborhood of the closed
rectangle, with these properties locally uniform in time. Assume R is
continuous there and (1) holds. Initial and boundary data then satisfy
the corner compatibilities g_±(0,y)=f_y(x_±). These stronger-than-necessary
assumptions suffice for every integration below. A continuous solution
classical in the interior gives the same formula by interior/time limits
provided the displayed integrals converge. In particular, uniform
integrable-in-time forcing majorants suffice for the estimates. No
boundedness or extension at any real x outside [x_-,x_+] is required.

## 2. Exact formula with two lateral terms

For τ>0 let G_τ(q)=(4πτ)^(-1/2) exp(-q²/(4τ)). The Dirichlet kernel is

    K(τ;x,ξ) = Σ_{k∈Z} [G_τ(x-ξ+2kL)
                            -G_τ(x+ξ-2x_-+2kL)]             (4)
              = (2/L) Σ_{n>=1} exp[-(nπ/L)²τ]
                    sin[nπ(x-x_-)/L] sin[nπ(ξ-x_-)/L].

Both series and their required derivatives converge uniformly when τ
is bounded away from zero. The image formula solves the heat equation,
vanishes at both endpoints and approaches the identity on interior
continuous data. Uniqueness for the scalar Dirichlet heat problem, applied
to real and imaginary parts, identifies it with the Dirichlet solution
kernel. The maximum principle gives K>=0. Define inward ξ derivatives

    k_-(τ;x) = ∂_ξ K(τ;x,ξ)|_{ξ=x_-},
    k_+(τ;x) = -∂_ξ K(τ;x,ξ)|_{ξ=x_+}.                        (5)

They are nonnegative: K is nonnegative in ξ, zero at its endpoints and
differentiable there. For u>0 and x in I the exact representation is

    E(u,x+iy)
      = ∫_I K(u;x,ξ) f_y(ξ) dξ
        + ∫_0^u ∫_I K(u-v;x,ξ) R(v,ξ+iy) dξ dv
        + ∫_0^u k_-(u-v;x) g_-(v,y) dv
        + ∫_0^u k_+(u-v;x) g_+(v,y) dv.                    (6)

This retains the complete signed complex integrals until a bound is
chosen. In particular, neither boundary integral may be dropped.

**Proof.** For v<u differentiate
J(v)=∫_I K(u-v;x,ξ)E(v,ξ+iy)dξ. By (1) and K_τ=K_{ξξ},

    J'(v) = [K E_ξ-K_ξ E]_{x_-}^{x_+} + ∫_I K R dξ
           = k_-(u-v;x)g_-(v,y)
             +k_+(u-v;x)g_+(v,y)+∫_I K R dξ.

Integrate first over 0<=v<=u-ε and then let ε↓0. The approximate-identity
limit is J(u-)=E(u,x+iy). For an interior x the boundary kernels are
integrable at zero; the stated regularity justifies the other limits.
This proves (6), including its signs and the two boundary payments.

The equivalent exact adjoint identity can be useful for a joint linear
consumer. Let ψ be a smooth complex terminal function with compact
support in I, and put

    φ(v,ξ)=∫_I K(u-v;x,ξ)ψ(x) dx,  0<=v<u.

Then φ_v+φ_{ξξ}=0, φ(v,x_±)=0 and φ(u,ξ)=ψ(ξ), and

    ∫_I ψ(x)E(u,x+iy)dx
      = ∫_I φ(0,ξ)f_y(ξ)dξ + ∫_0^u∫_I φ(v,ξ)R(v,ξ+iy)dξdv
        +∫_0^u [φ_ξ(v,x_-)g_-(v,y)
                         -φ_ξ(v,x_+)g_+(v,y)]dv.            (7)

This is a bilinear identity, with no complex conjugation. General complex
ψ need not produce nonnegative weights. A signed adjoint does not supply
a small allowance without a paid bound for all of its terms. A terminal
point mass gives (6) by a limiting argument.

## 3. Survival mass and a paid erfc boundary bound

Define nonnegative masses

    S(τ,x)=∫_I K(τ;x,ξ)dξ,
    Q_±(τ,x)=∫_0^τ k_±(s;x)ds.

Applying (6) to the constant solution 1, with zero forcing and data 1,
gives the exact mass identity

    S(τ,x)+Q_-(τ,x)+Q_+(τ,x)=1.                              (8)

Thus 0<=S<=1. S is the survival probability for the real diffusion with
generator ∂_x² killed at the endpoints, but (8) requires no probabilistic
input. An explicit version convenient for exact mass evaluation is

    S(τ,x)=(4/π) Σ_{j>=0} exp[-((2j+1)π/L)²τ]
                       sin[(2j+1)π(x-x_-)/L]/(2j+1).        (9)

Individual summands in (9) need not be nonnegative; positivity refers to
S and K themselves. The two Q functions are the zero-initial-data heat
solutions with boundary values (1,0) and (0,1), respectively. Comparing
the first with the half-line solution
erfc((x-x_-)/(2√τ)), which has boundary value 1 at x_- and a nonnegative
value at x_+, gives

    Q_-(τ,x) <= erfc((x-x_-)/(2√τ)),
    Q_+(τ,x) <= erfc((x_+-x)/(2√τ)).                          (10)

Here erfc(a)=(2/√π)∫_a^∞ exp(-s²)ds. The comparison follows from the
maximum principle, taking initial limits in the interior; the corner
jump can equivalently be handled by continuous monotone boundary
approximations. Direct differentiation verifies the half-line heat
equation and endpoint/initial limits. Consequently the total lateral
influence obeys

    1-S(τ,x) <= min{1, erfc((x-x_-)/(2√τ))
                            +erfc((x_+-x)/(2√τ))}.          (11)

This is a union bound on influence from both endpoints, not a whole-line
Gaussian tail multiplied by an unacquired outside bound.

For the fixed circle Γ:|z-X|=r, r<min(A,h), write z=x+iy. Then
x in [X-r,X+r], and for τ>0 a uniform bound is

    β_Γ(τ) = min{1, erfc((A-r)/(2√τ))
                         +erfc((A+r)/(2√τ))},
    sup_{z∈Γ}[1-S(τ,Re z)] <= β_Γ(τ)
                              <= min{1,2erfc((A-r)/(2√τ))}. (12)

Indeed, erfc(d/(2√τ)) is convex for d>0; the sum in (11) is an even
convex function of x-X, so its maximum on [-r,r] occurs at an endpoint.
Set β_Γ(0)=0. One may instead retain the exact mass (9) pointwise, or
use sup_{|x-X|<=r}(1-S(τ,x)); no erfc relaxation is compulsory.

## 4. Complete error envelopes and the fixed-information comparison

Suppose the acquired nonnegative functions majorize the *physical* data:

    |f_y(ξ)| <= F(ξ,y),      |R(v,ξ+iy)| <= ρ(v,ξ,y),
    |g_±(v,y)| <= B_±(v,y).

The positive-kernel allowance at each point is

    B_heat(u,x,y)
      = ∫_I K(u;x,ξ)F(ξ,y)dξ
        +∫_0^u∫_I K(u-v;x,ξ)ρ(v,ξ,y)dξdv
        +∫_0^u [k_-(u-v;x)B_-(v,y)
                              +k_+(u-v;x)B_+(v,y)]dv,       (13)
    |E(u,x+iy)| <= B_heat(u,x,y).

Thus all initial, full-forcing and lateral information is paid. Spatial
and time dependence may be retained; replacing it by independent
suprema is optional and can lose phase or data compatibility.
At u=0, define B_heat(0,x,y)=F(x,y) directly from the initial datum;
on interior x the mass conventions are S(0,x)=1 and Q_±(0,x)=0.

For instance, if F<=ε0, ρ(v,ξ,y)<=ρ0(v), and both B_±<=M_b on the
whole time-rectangle, (13) becomes

    |E(u,x+iy)| <= ε0 S(u,x)+M_b[1-S(u,x)]
                     +∫_0^u ρ0(v)S(u-v,x)dv.              (14)

The exact initial mass S matters: replacing the first term by ε0 and
then adding the entire M_b boundary payment overcounts by
ε0[1-S]. In particular, if M_b>=ε0, (12) yields

    sup_Γ |E(u,z)| <= ε0+(M_b-ε0)β_Γ(u)+∫_0^u ρ0(v)dv.     (15)

If M_b<ε0 the coefficient M_b-ε0 is negative, so substituting an
*upper* bound for 1-S would reverse the required inequality. Keep (14),
or use the safe coarser ε0+∫ρ0. If M_b=ε0 and ρ0=0, (14) is exactly
ε0, as the constant solution requires. This check pays both boundaries
and the surviving initial data without an artificial additive loss.

The raw direct source envelope in the frozen cell is precisely the
Section 5 omitted-correction budget, in physical normalization:

    V(u,z)=|B_{t_*-u}(z)|[e_A+e_B+e_{C,0}](t_*-u,z),
                  Re z>=200, 0<=Im z<=h,                    (16)

where B in (16) denotes the manuscript's nonvanishing normalizer
mathcal B, not boundary data. For negative Im z define V(u,z)=V(u,bar z)
by the conjugation symmetry of H and P_N. The frozen cutoff makes (16)
an envelope for this same E everywhere in the rectangle. Its complete
published formulas and their evaluation remain E11 obligations. They
may supply F=V(0,·), B_±=V(v,x_±+iy), and the independent endpoint
bound V(u,z); the forcing is still the full (2).

Define, on each slice,

    ε_heat(u)=sup_{z=x+iy∈Γ} B_heat(u,x,y),
    ε_raw(u)=sup_{z∈Γ} V(u,z).

At these fixed inputs, the explicit sufficient inequality

    ε_heat(u) < ε_raw(u)                                    (17)

is an improvement of the raw uniform physical value envelope. A
sufficient scalar form, when M_b>=ε0, is that the right side of (15)
is strictly below ε_raw(u). No such inequality is asserted for an
unacquired canonical cell. Failure of (17) does not prove that the
actual error is large or exclude signed/correlated estimates.

With the same acquired lower denominator m_Γ(u)<=inf_Γ|P_N|, the two
uniform relative-error allowances are ε_heat/m_Γ and ε_raw/m_Γ. A
value below one permits Rouché transfer if Count(P_N)=2 has separately
been acquired. The direct comparator is entitled to every input of
(13), and hence to min{V(u,z),B_heat(u,Re z,Im z)} pointwise, or any
sharper direct consequence of their joint signed data. The identity
therefore gives no superiority over an equally informed direct
consumer. It provides a possible improvement over using (16) alone.

For an entire continuation cell the contour count, denominator and the
chosen complete discriminant lower bound must hold on *every* slice.
An endpoint improvement alone is not path protection. The accepted
module-A contour consumer can consume these values without extracting
E_zz. If separate jets are needed, a radius d disk about z contained in
the paid analytic rectangle gives |E_zz(u,z)|<=2 d^(-2) sup_disk|E|;
the enlarged disk allowance must be acquired. This fallback supplies
no automatic gain for the joint numerator P E_zz-P_zz E.

## 5. Controls, scope and E11 handoff

The exact translated quadratic control H=P=(z-X)²-2(t-T) has E=R=0.
All terms of (6), including both boundaries, vanish. Yet its discriminant
is D_P(u)=2(t_*-T)-2u and reaches zero at u=t_*-T. A small fixed circle
has count two and a cleared boundary around the merger on a sufficiently
short time cell. The missing quantitative premise is a **strictly
positive complete discriminant margin**, not an approximation estimate.
Thus zero heat error does not protect a colliding reference.

The [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
screen below is analytical, not a new numerical replay. For a physical
control possessing an isolated double event, choosing P=H_control is
the same zero-error test of the generic heat representation. At that
event the strict positive discriminant margin fails. This choice is a
test of (6), not a claim that it equals the frozen canonical P_N. No
source-specific numerical envelope for P_N is assigned to a control.

| Cluster12 class | Failed canonical identification or equation premise; quantitative screen |
| --- | --- |
| Euler-factor translates | Complete normalized theta arithmetic is changed. Heat evolution and positivity still do not provide the missing strict discriminant margin at a collision. |
| Three/four weighted-square controls | Theta's complete coefficient/reflection identification fails. Selected square support and endpoints do not supply that margin. |
| Reflected super-Gaussian | Literal theta arithmetic and the manuscript's order-one product input fail; full reflection and Gram positivity do not supply the margin. The bounded heat formula itself needs no product hypothesis. |
| Smooth shape and positive-primitive controls | Complete theta square expansion is absent; even all listed primitive endpoint/asymptotic properties supply no pointwise margin. |
| Finite theta-tail / finite zero-tail source controls | The complete theta source is changed and no all-real heat time is available in the proved class; a finite event witness is not a global upper threshold. The bounded formula makes no all-real assertion. |
| Finite-prime orbit controls | Complete source reflection fails despite all prescribed finite-prime/measurement compatibilities. Their time-dependent, escaping event family supplies no fixed canonical compact margin. |
| BW-01 fixed-event atom and finite-profile threshold controls, including continuous compact extensions | Full theta profile and eventual simplicity at the threshold fail. Prescribed finite floors/profile coordinates and moment budgets do not supply the event's strict discriminant margin. |
| RH-conditional endpoint controls | Ordinary Dirichlet-series arithmetic is changed and construction is RH-conditional; escaping doubles do not refute a fixed-compact canonical estimate. A fixed positive approximation tolerance alone does not acquire the needed height-dependent margin. |
| Fixed amplitude / changed observation kernel controls | The full physical cosine/Newman equation fails. Equation (1) with the canonical forcing (2) cannot be assigned to them; zero raw amplitude mismatch does not pay their true prepared residual. |

For any actual use of the frozen theta P_N, literal source identification
only permits the published source formulas. It does not by itself prove
the useful inequality (17), count two, a denominator floor, or positive
complete D_H. These are separate quantitative acquisition gates.

The need for full-time boundaries is already visible in the entire
homogeneous-heat family

    E_K(u,z)=ε exp[K(z-x_+)+K²u],  K>0.

Its initial norm on the whole closed horizontal rectangle is at most ε,
whereas at any fixed interior real x and u>0 the modulus
ε exp[K(x-x_+)+K²u] is unbounded as K→∞. The right boundary data grow
and (6) pays them. This excludes initial-local-norm-only propagation in
this classical solution class; it makes no negative claim about the
canonical theta data or a comparison using acquired boundaries.

**E11 inputs.** Attach the complete formulas in (16) in physical units on
the initial segment and both lateral segments for every v in [0,U];
attach the exact finite defect (2) and a paid spatial/time bound or joint
integral; evaluate (13) or its chosen conservative reduction at Γ on
every slice; and acquire Count(P_N)=2, denominator clearance, reference
discriminant and any arithmetic/quadrature uncertainty. Compare the
complete module-A lower bound with the equally informed endpoint
consumer. Retaining signed terms in (6) or (7) remains available, but
their useful cancellation has not been acquired here.

**Bounded work record.** One analytical derivation and one self-correction
pass completed. The pass checked the boundary signs by Green's identity,
the diffusion coefficient against the physical time change, the kernel
mass against the constant solution, and the sign condition M_b>=ε0 in
(15). It clarified the u=0 mass convention and why there is no top/bottom
boundary integral. These are written analytical checks, not a numerical
verification or independent assessment. No register, history or
manuscript file is modified by this module.
