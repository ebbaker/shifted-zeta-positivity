# AGC-B03 r1: full-phase family and the complete pointwise consumer

19 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. B03 author explicitly dispatched **gpt-6-astra / ultra**; dispatch is recorded separately from unavailable independent serving-backend attestation. Root model/effort unavailable. One conceptual pass and one correction/comparator pass; no numerical campaign.

**Decision: one family and one consumer fixed; E14 analytical execution ready.** Extend the natural-cutoff correction over every phase on the positive slab below, and use precisely the final-strip input of Polymath Theorem1.2. The lift supplies a useful uniform analytic interface, but its separately paid vertical mismatch cannot improve the equally informed retained-value pointwise allowance. Retaining the value correction does uniformly improve the complete omitted-correction allowance by more than **3L/40**. This is an allowance comparison, not an acquired positive strip margin. The [frozen E14 request](../research-progress/handoffs/AGC-E14-r1-request.md) owns the subsequent proof and separate assessment.

| Next task | Type / model | Dependency | Expected output |
| --- | --- | --- | --- |
| **AGC-E14 r1, default** | E / Sol6.1 ultra | This frozen decision | Proved uniform constants, complete comparator and paid seams; separate assessment |
| Positive arithmetic strip-floor acquisition | B / Astra | E14 result and a specified independent lower-bound mechanism | Concrete arithmetic input or scoped failure; no open numerical scan |

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md) owns live status. Read the [result index](../../../../result-summaries/README.md), [pattern index](../../../../avoid/README.md), [Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and patterns [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md), [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Classification: a uniform source/interface and complete-allowance comparison with an explicit numerical constant; it is not an RH-equivalent criterion. The unacquired positivity condition is stated once in Section5, not supported by repetitions or surrogate checks.

Inputs are [B03 r1](../research-progress/handoffs/AGC-B03-r1-request.md), [Milestone12](12_AGC_CORRECTED_MILESTONE_AND_CONTINUATION_20261119.md), [Note10](10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md), [Note11](11_AGC_E12_R2_CORRECTED_COMPARISON_20261119.md), [Reviews05](../reviews/05_AGC_CORRECTED_REFERENCE_ASSESSMENT_20261119.md)–[06](../reviews/06_AGC_CORRECTED_COMPARISON_ASSESSMENT_20261119.md), and manuscript Sections5–9. Selected primary passages in [Polymath v2](https://arxiv.org/html/1904.12438v2), especially (53), (58), Corollary6.4 and Theorem1.2, were reopened. This is not a full audit of that imported theorem.

## 1. Exactly one family

Keep the literal theta source and physical equation H_t=−H_zz. Fix

    .09 <= t <= .1, x >= 14000, |y| <= 1,
    z=x+iy, k=pi/8, u=x/2+kt >=7000, w=u+iy/2,
    N=floor(sqrt(u/(2pi))), p_N(w)=2N+1−2sqrt(w/(2pi)).

Use the accepted fixed-index P_N and

    C(p)=[exp(i*pi*(p²/2+3/8))−i*sqrt(2)*cos(pi*p/2)]/[2cos(pi*p)],
    C^sharp(p)=conjugate(C(conjugate(p))),
    A_N(w)=sqrt(w)/2 [(w+i)C(p_N(w))+(w−i)C^sharp(p_N(w))],
    J_N=(-1)^(N+1) sqrt(pi)/4 exp(−kz−k²t),
    Cval_N=J_N A_N(u), Chol_N=J_N A_N(w),
    Qval_N=P_N−Cval_N, Qhol_N=P_N−Chol_N.

Principal roots stay in Re w>0. Natural real phases cover (−1,1], with −1 obtained as the one-sided endpoint before a cutoff change. No positive fraction of heights or phases is omitted. These are fixed-index analytic charts and a pointwise natural-cutoff selection, not a single globally holomorphic patchwork. Qval is used only as a value approximation.

The height 14000 retains the scale of the prior cell while opening every later natural phase. It is a proof threshold for the explicit bounds below, not an asserted threshold of zero exclusion. No new physical time range or time-zero passage is selected.

## 2. The phase issue is tractable, with explicit constants

At p=m+1/2, m an integer, the exponential in C's numerator equals

    i (-1)^(m(m+1)/2)=i sqrt(2) cos(pi*m/2+pi/4).

Thus every simple denominator zero cancels; C and C^sharp extend to entire even functions. The apparent poles at ±1/2 need no phase-window exclusions.

On the boundary of |Re p|<=5/4, |Im p|<=1/4, the denominator modulus is at least sqrt(2)>7/5. The numerator is bounded by

    exp(5pi/16)+sqrt(2)cosh(pi/8)<3+33/20=93/20.

The maximum principle gives |C|<4 in that rectangle; Cauchy disks of radius1/5 give |C'|<20 and |C''|<200 on |Re p|<=101/100, |Im p|<=1/100. The sharp function has the same bounds. For the chosen physical domain, the root formula shows the complex phase differs in real part from its real-axis value by less than 1/100, and has imaginary part less than 1/100. The whole vertical segment and both one-sided seam phases lie in that inner patch.

Write r=|w| and B=[(w+i)C+(w−i)C^sharp]/2, so A=sqrt(w)B. The proof route retains

    |B|<=4(r+1),
    |B'|<=4+20(r+1)/sqrt(2pi*r),
    |B''|<=40/sqrt(2pi*r)
             +10(r+1)/(sqrt(2pi)*r^(3/2))
             +200(r+1)/(2pi*r).

Together with u<=r<=u+1/2 and u>=7000, these imply the conservative targets

    |A_N|<5u^(3/2), |A_N'|<9u, |A_N''|<40sqrt(u).

E14 must supply the full rational checks and independently assess them before these uniform targets are promoted to accepted results. Fixed-index differentiation has the same exact cancellation as Note10:

    (partial_t+partial_z²)Chol_N=J_N A_N''/4,
    R_Q=R_P−J_N A_N''/4.

The complete defect is bounded by |R_P|+10sqrt(u)|J_N|. No cancellation with R_P has been acquired. The vertical mismatch is paid by

    M=(9/2)u|y||J_N|,
    L=|J_N|sqrt(u)sqrt(u²+1)/2,
    M/L <=9|y|/sqrt(u)<|y|/9  for y!=0,
    M=0 at y=0, and M/L<1/9 everywhere.

Here L is the old omitted leading-correction allowance. The strict comparison with |y|/9 is confined to y!=0. All rates are uniform over this one family; no sampled derivatives enter.

## 3. Complete comparison and the equally informed direct method

Let S_N be both full finite-term replacement sums, and retain the entire published delta remainder. Set

    V_ret=S_N+L(delta_-+delta_+),
    V_om=V_ret+L, V_hol=V_ret+M.

The source bounds are |H−Qval_N|<=V_ret and |H−Qhol_N|<=V_hol. Consequently V_om−V_hol>8L/9. This is a **source-only saving of the leading payment**. It is not an 8/9 improvement of the whole source error or of a zero margin.

The useful complete comparison uses the phase of the same correction. Source (58) gives |C(p)|<=1/2 for real p∈[−1,1]. Put q=|p|, a=q−1/2, b=(q+1/2)/2. Then

    Re C(p)=sin(pi*a*b)/(2sin(pi*a)),
    0<Re C(p)<=cos(pi/8)/2,

with the removable value at a=0. For u1=pi|a|, monotonicity of sin(bu1)/sin(u1) in u1∈[0,pi/2] follows because v cot(v) decreases; monotonicity in b∈[1/4,3/4] is immediate. Their endpoint value is cos(pi/8). Since |Im C|<=1/2 and A_N(u)=sqrt(u)[u Re C−Im C],

    |Cval_N|/L <=cos(pi/8)+1/u <37/40.

For example cos(pi/8)<231/250 follows by squaring its positive radical expression, and 231/250+1/7000<37/40. This avoids a numerical extremization. The lead supplied this strengthening during the single comparator pass; the B author checked its algebra and included it in E14.

Define the complete exact-reference lower allowances

    m_om=|P_N|−V_om,
    m_val=|Qval_N|−V_ret,
    m_hol=|Qhol_N|−V_ret−M.

Reverse triangle gives the quantitative target

    m_val > m_om+3L/40.                                  (1)

The comparison includes the changed reference value and all source contributions. It is stronger than subtracting an omitted remainder while retaining the old reference. It remains a comparison of possibly negative lower allowances.

For the identical data and any valid M>=|Qhol_N−Qval_N|, ordinary triangle gives

    m_hol <= m_val.                                      (2)

Thus the holomorphic lift with a separate vertical triangle payment has no advantage over exact direct retained-value evaluation for this **pointwise** consumer. The direct method receives Cval, the full source information and any lower-bound data available to the lift. This says nothing about implementation costs, differences between particular interval enclosures, coupled residual information, counted-pair discriminants or heat transport. The already accepted contour gain remains intact. Both (1) and (2) survive division by the same positive carrier modulus.

## 4. Cutoff changes are real reference changes

At u=2pi m² the natural index changes from m−1 to m along

    x_m(t)=4pi m²−pi t/4.

Let d_m=p_m(t,s_+)+p_m(t,s_-). Since J_{m−1}=−J_m, and evenness gives A_{m−1}(u)=A_m(u) at real phases −1 and +1,

    Delta Qval=d_m−2J_m A_m(u),
    Delta Qhol=d_m−J_m[A_m(w)+A_{m−1}(w)].                (3)

Off the real axis the two A's in the second formula are not identified. These jumps need not vanish. Their moduli are bounded by the sum of the two complete one-sided source allowances, since both reference errors are measured against the same continuous H. The old-index source inequality at its excluded endpoint follows by taking the limit from its natural cell; the new index owns the endpoint. Equivalently keep the exact finite jump (3) in a joint enclosure.

For a fixed-reference continuation across a seam, E_new=E_old−Delta Q and the error enclosure pays |Delta Q|. Crossing several seams requires the full successive transfers, or the exact difference between the frozen and natural references; the local phase constants cannot silently be assigned to an index far from its natural chart. A contour crossing a seam must use such a fixed analytic reference and pay the change. Differentiating the natural floor or using the discontinuous patchwork in the heat equation without distributions is disallowed.

The selected consumer is pointwise. It uses the half-open natural cells and their one-sided endpoints separately, so its proof takes no derivative of the floor and needs no fictitious global analytic gluing. This resolves the cutoff interface without assuming continuity of Q.

## 5. Exact final consumer and missing independent input

Choose only Polymath Theorem1.2(ii) with

    t0=1/10, y0=1/5, X=14000,
    x>=14000+sqrt(24/25), 1/5<=y<=sqrt(4/5).             (4)

The nonvanishing carrier is B_t(z)=M_t(s_−(z)). The required independent arithmetic input is a proved lower function ell(x,y)<=|Qval_N/B_t| such that

    ell(x,y)>V_ret/|B_t|  at every point of (4),          (5)

including every finite-height/tail join and natural-cutoff endpoint. It must come from independently bounded full arithmetic sums or another specified source-specific estimate. Defining ell by the desired nonvanishing claim does not acquire it. On this unbounded height region a positive uniform **unscaled** infimum is inappropriate because of carrier decay; a normalized positive floor or the displayed pointwise positive margins are the proper data.

No count, center or discriminant is imported from the old pair. Those are not inputs of the chosen consumer, and Notes10–11 do not supply (5). The finite interval 14000<=x<14000+sqrt(24/25) is outside criterion(ii); criterion(iii) requires its full barrier at every 0<=t<=.1, including times below this slab. Criterion(i) requires the initial zeta exclusion up to T=7000 in .6<=sigma<=1. Neither is acquired here. Only all three inputs would give Lambda<=.1+.2²/2=.12; that conditional arithmetic is not a new bound.

The target against the prior omitted-value allowance is exactly (1), not a positive margin claim. Against the equally informed retained-value method the exact conclusion is (2), not superiority. E14 may therefore finish with useful uniform analytic and complete-allowance theorems while recording (5) as missing.

## 6. Controls, correction pass and disposition

The [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md) screen applies before interpretation:

| Control class | Premise unavailable for this source theorem or final consumer |
| --- | --- |
| Euler-factor translates | Unchanged complete normalized theta arithmetic and its specific retained-error bound |
| Weighted-square, finite-source, finite-prime and finite-score changes | Full theta coefficients/reflection; finite preserved rows do not identify the source; the documented finite-source class also lacks an all-real time |
| Reflected super-Gaussian, smooth shape and positive-primitive sources | Exact theta arithmetic expansion; preserved shape, reflection or positive primitive does not supply it |
| Atomic fixed-event and finite-profile controls | Full theta profile and eventual simplicity; finitely selected profile data are insufficient |
| RH-conditional endpoint controls | Ordinary Dirichlet-series arithmetic; construction is RH-conditional and event heights escape, with no fixed-compact conclusion |
| Changed observation kernels, including polynomial/counter-kernel constructions | Literal cosine/Newman equation; the true prepared residual includes additional forcing |
| Fractional relaxed profiles and static divisor surgery | Integer physical divisor and common source heat path, respectively |

These are failures of source identification, not measured rejection by a new coarse inequality. Generic triangle comparisons remain valid for any control with its own honest data. At a zero in a proposed exclusion domain, any valid complete pointwise allowance is nonpositive. For H=Q=(z−X)²−2(t−T), zero approximation error still coexists with a merger and D_Q=0. That control prevents interpreting the present source saving as automatic gap protection; its event need not lie in (4), so no blanket rejection on unrelated collision-free domains is claimed. Reflection rigidity identifies theta only under its full stated conjunction; it does not add the missing quantitative margin.

The single correction pass changed the initially tempting comparison into the properly informed one: the direct value formula avoids the lift mismatch, while its real correction phase gives the nonzero complete allowance improvement (1). It retained separate fixed-index holomorphy, the off-axis seam sum, the normalized final floor and all finite/barrier interfaces. No family change, numerical sample or hidden gap assumption was added.

**Disposition:** B03's conceptual decision is complete and [E14 r1](../research-progress/handoffs/AGC-E14-r1-request.md) is frozen. The uniform constants, full allowance comparison and seams require its proof and separate assessment before acceptance. The missing arithmetic floor is neither assumed nor turned into a claimed universal obstruction. No further numerical packet is opened by this decision.
