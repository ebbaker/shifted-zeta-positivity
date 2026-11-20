# AGC-E14 r1: full-phase correction, complete strip allowances and cutoff interfaces

19 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Contract author explicitly dispatched **gpt-6-astra / ultra**; this records dispatch, not independent serving-backend attestation. Lead configuration unavailable. Parent: **AGC-B03 r1**. This request is frozen on issue; the [sole progress register](../01_AGC_RESEARCH_PROGRESS_20261119.md) owns live status.

**Type E / Sol 6.1 ultra.** The family, functions, proof route, consumer and comparison are fixed below. One analytical derivation and one correction pass, followed by separate nonauthor assessment. No numerical campaign, source change, new height choice, optimization search or acquisition of a positive strip floor is authorized by this packet.

## Inputs and single family

Read root instructions, model workflow, result/pattern indexes, Controls12 and patterns01/02/07/11/12; AGC Notes10–12, Reviews05–06, B03 r1 request/decision, and manuscript Sections5–9. The accepted source is Polymath [arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), specifically (53), (58), (59), (68), Corollary6.4 and Theorem1.2. Recheck selected imports; no full-paper audit is required or claimed.

Use only the literal theta H with H_t=−H_zz and

    9/100 <= t <= 1/10, x >= 14000, |y| <= 1,
    z=x+iy, k=pi/8, w0=x/2+kt, w=w0+iy/2,
    N=floor(sqrt(w0/(2pi))), p_N(w)=2N+1−2sqrt(w/(2pi)).

Principal square roots stay in Re w>0. Keep Note10's C, C^sharp, A_N, J_N and fixed-index P_N, defining

    Cval_N=J_N A_N(w0), Chol_N=J_N A_N(w),
    Qval_N=P_N−Cval_N, Qhol_N=P_N−Chol_N.

Only fixed-index Qhol_N is a holomorphic reference. Qval_N is a pointwise value approximation. The natural-index patchwork Qhol_{N(t,x)} is not asserted holomorphic or a global heat solution.

## Fixed proof targets

1. **Full phase and removable poles.** Prove cancellation of C's numerator at each half-integer; C and C^sharp extend to entire even functions. On |Re p|<=5/4, |Im p|<=1/4 prove |C|,|C^sharp|<4 by a boundary denominator bound and the maximum principle. Cauchy disks of radius1/5 then give |C'|<20 and |C''|<200 on |Re p|<=101/100, |Im p|<=1/100. Show every natural phase, its vertical segment and one-sided seam phase lies in this inner patch; p(w0) ranges over (−1,1], with −1 supplied by one-sided limits. No omitted phase windows.

2. **Uniform derivatives and exact defect.** With w0>=7000 prove on the vertical segment

       |A_N(w)|<5 w0^(3/2), |A_N'(w)|<9 w0,
       |A_N''(w)|<40 sqrt(w0).

   Retain all chain/product terms. For a fixed index establish

       R_Q=R_P−J_N A_N''/4,
       |R_Q|<=|R_P|+10 sqrt(w0)|J_N|.

   The vertical mismatch may be paid by

       M_N=(9/2) w0 |y| |J_N|,
       M_N/L <=9|y|/sqrt(w0)<|y|/9 <=1/9,
       L=|J_N| sqrt(w0) sqrt(w0^2+1)/2.

   No favorable signed defect cancellation is assumed. If a displayed constant fails, return the exact failed inequality; no silent family/threshold change.

3. **Complete physical source budget.** Retain both term-error sums S_N and the entire delta remainder from Note10:

       R_N^val=S_N+L(delta_-+delta_+),
       V_om=R_N^val+L, V_val=R_N^val, V_hol=R_N^val+M_N.

   Use a different symbol from the heat defect to avoid conflating the two R's. Prove |H−Qval_N|<=V_val and |H−Qhol_N|<=V_hol. The source-only saving V_om−V_hol>8L/9 is not a final margin or percentage improvement of the whole budget.

4. **Quantitative complete pointwise comparison.** Source (58) supplies |C(p)|<=1/2 for real p∈[−1,1]. Prove the additional elementary real-part bound

       0<Re C(p)<=cos(pi/8)/2.

   Suggested proof: q=|p|, a=q−1/2, b=(q+1/2)/2; Re C=sin(pi*a*b)/(2sin(pi*a)), continuously at a=0. For u=pi|a|, sin(bu)/sin(u) increases in u∈[0,pi/2] and b∈[1/4,3/4], by monotonicity of v cot v. Thus

       |Cval_N|/L <=cos(pi/8)+1/w0 <37/40.

   Define complete exact-reference lower allowances

       m_om=|P_N|−V_om,
       m_val=|Qval_N|−V_val,
       m_hol=|Qhol_N|−V_hol.

   Prove uniformly

       m_val > m_om+3L/40,    m_hol <= m_val.

   The first is a complete allowance improvement from retaining correction information. The second scopes the limitation: the holomorphic lift with a separate valid vertical triangle payment cannot improve the equally informed exact pointwise retained-value allowance. It does not compare finite implementation costs, arbitrary interval enclosures, signed correlated residuals, counted-pair readouts or heat transport. Both statements survive division by the same positive carrier modulus. They do not assert m_val>0.

5. **Pay every cutoff interface.** For d_m=p_m(t,s_+)+p_m(t,s_-), at the seam w0=2pi m^2 (x=4pi m^2−pi t/4), old index m−1 and new index m have J_{m−1}=−J_m. Give exact signed jumps

       Delta Qval=d_m−2J_m A_m(w0),
       Delta Qhol=d_m−J_m[A_m(w)+A_{m−1}(w)].

   For Qval use evenness at p=±1; do not assume the two A's coincide off the real axis. Bound jumps by the sum of the complete two one-sided source allowances (or retain the exact finite jump). Source inequalities at the old seam endpoint follow by continuity from its natural cell. For fixed-reference continuation transfer E_new=E_old−Delta Q and pay |Delta Q|; no uncharged patching. The pointwise consumer covers half-open natural cells and their one-sided endpoints separately and takes no derivative of the floor. No global piecewise heat equation without seam distributions is claimed.

6. **Complete named consumer and independent missing input.** Select only Theorem1.2(ii) at

       t0=1/10, y0=1/5, X=14000,
       x>=14000+sqrt(24/25), 1/5<=y<=sqrt(4/5).

   With B_t(z)=M_t(s_−(z)) nonvanishing, the unresolved arithmetic input is an independently acquired lower function ell(t0,x,y)<=|Qval_N/B_t| exceeding V_val/|B_t| at every point, with finite-height/tail and natural-cutoff coverage paid. A positive unscaled infimum over unbounded x is not requested. Do not replace that acquisition by defining ell to be the desired margin. State finite [14000,14000+sqrt(24/25)) coverage and the time0/barrier interfaces separately: the slab does not cover the barrier 0<=t<=.1. Inputs(i) and(iii) remain unacquired here. The arithmetic output .12 is conditional on all three inputs, not a claimed Newman bound.

## Completion, controls and outputs

An accepted theorem comprising the uniform analytic bounds, complete allowance comparison and seam payments is the completion test. It is a bounded source/interface and comparator result with an explicit missing final positivity input, not a criterion proposed as proof of RH or new coverage. The equally informed direct method gets the exact correction, all source information and the same lower-bound information; do not withhold Qval from it.

Screen all Controls12 families by named failed premises; retain the exact quadratic collision as a generic check that perfect approximation does not protect a colliding reference. Scope every limitation to the class above. No new numerical control runs are requested.

Write `notes/14_AGC_E14_UNIFORM_CORRECTION_AND_STRIP_COMPARISON_20261119.md` and `research-progress/handoffs/AGC-E14-r1-return.md`; do not edit manuscript, indexes, history or sole register. Separate assessor writes Review07 and its review return. One proof pass plus one correction, no numerical computation or new conceptual route. Return failures to B03 with their exact scope; preserve all accepted local results and old scientific files. Record actual dispatch separately from unavailable serving-backend attestation.
