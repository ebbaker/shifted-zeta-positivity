# AGC-E18 r1: actual-height dyadic-cost obstruction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Conceptual author explicitly dispatched
**gpt-6-astra / ultra**; independent serving-backend attestation is
unavailable. Parent **AGC-B06 r1**. **Type E; recommended gpt-6.1-sol /
ultra:** all formulas, proof route and quantitative targets are fixed.
Frozen request; no numerical diagnostic, scan or source change is issued.
The [sole register](../01_AGC_RESEARCH_PROGRESS_20261119.md) owns status.

Read root AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md,
the result/pattern indices, Cluster18, Controls12 and patterns01/02/07/11/12.
Reuse Notes14 and17–21, Review09 and manuscript Sections5/12. B06's
decision is Note22. This request is self-contained as a mathematical
contract; no work depends on an unfinished draft of that decision.

## Question and unchanged consumer

Can the actual-height dyadic cost, rather than its auxiliary full-circle
supremum, provide a positive complete allowance throughout F0? Prove the
following scoped negative answer by transferring a fixed-height phase
mean to a real phase revolution with a paid coefficient-variation error.

Keep t=1/10, y=1/5, x0=14000+sqrt(24/25), x0<=x<=30000, the literal theta
source, q=f-c, full v and D_kappa from Note20(3)–(8). Keep exactly
E=product_(p=2,3,5)(1-b_p p^(-s)), the full beta/a convolution through30N,
and all cutoff edges. Do not pay a different reference's source error.
Here s=s0+alpha(s0)/20=sigma+i*tau, s0=3/5-i*x/2,
g=|M_t(2/5+i*x/2)/M_t(s0)| and N=floor(sqrt(x/(4pi)+1/160)).

Use the actual u(x)=-tau(x)log2 and Note20's exact group radii

    R_r(x,u)=(1-g(x))*r^(-sigma(x))*||M_r(x,u)||_2,
    C_act(x)=sum_(r odd<=30N) R_r(x,u(x)),
    K_act=1-g-C_act,
    ell_act=K_act/|E|-D_kappa-|c|,  m_act=ell_act-v.

The independent core rotations eta_r are still relaxed in R_r; only the
common dyadic phase is physical. Thus ell_act<=|q|. Its complete strict
positivity threshold is exactly

    C_act < 1-g-|E|*(D_kappa+|c|+v).

No full-circle supremum is substituted for C_act in the conclusion.

## Target theorem

For **every closed interval [a,a+19] in one fixed natural-cutoff chart**
within F0, there is an actual height x* in that interval with

    C_act(x*)-(1-g(x*)) > 1/100,
    K_act(x*) < -1/100,
    ell_act(x*) < -1/800,  m_act(x*) < -1/800.

At a chart's excluded upper cutoff endpoint, interpret the old chart by
its continuous one-sided limit. Because the phase advances strictly more
than2pi in19 units, choose the first full revolution ending strictly
before a+19. Its witness then uses an actual natural reference, including
when a+19 is an excluded old-chart right endpoint.
There is no assertion that all heights in the interval fail, that x0
itself fails, or that any collection of independently maximizing core
phases occurs physically. The failure of this actual-u estimator on at
least one point of [x0,x0+19] already prevents its uniform use on F0.

## Fixed analytical route

1. Reprove the actual-u reverse-triangle lower allowance without taking
   a supremum over u. Preserve every correction/source payment and the
   exact positive divisor. Give the direct comparator the same data and
   prove m_E<=m_dyad<=m_act<=m_dir=|f-c|-v.

2. Retain only P*={7,11,13,17,19,23,29,31} in the cost for the obstruction:

       C_*(x,u)=sum_(p in P*)R_p(x,u)<=sum_r R_r(x,u).

   At frozen x=a, reuse the accepted finite Fourier-mean argument and
   eight-prime witness to show

       mean_u C_*(a,u) > (21/20)*(1-g(a)).

   This step alone remains an auxiliary-phase statement. The new input
   required below is quantitative transport of it along physical x.

3. Bound the actual smooth coefficients on fixed-N charts. With T=x/2,
   w=v+iT, 2/5<=v<=3/5, and L_t=L_0+alpha^2/40, derive

       |sigma'|<1/(39x), |tau'+1/2|<1/(39x), |g'|<1/(10x).

   Use alpha'=-1/(2w^2)-1/(w-1)^2+1/(2w),
   alpha''=1/w^3+2/(w-1)^3-1/(2w^2). On this horizontal segment
   |alpha|<6, |alpha'|<51/(100T), |alpha''|<1/T^2 suffice to give
   |L_t''|<3/(5T). The alpha' estimate for sigma/tau can be sharper:
   |alpha'|<=1/(2T)+3/(2T^2), hence |alpha'|/40<1/(39x).
   Since

       log g=Re[L_t(2/5+iT)-L_t(3/5+iT)],

   the horizontal integral and g<3/5 give
   |g'|<9/(125x)<1/(10x). Justify branches by the inherited carrier.
   Elementary e>8/3, e<68/25 and 25/8<pi<22/7 are available from the
   accepted proof; no transcendental numerical evaluation is needed.

4. For these eight prime cores only d=1,2 occurs in each convolution.
   The possible original n=p*2^k<=48 are exactly

       7,14,28; 11,22,44; 13,26; 17,34;
       19,38; 23,46; 29; 31.

   On each chart retain the appropriate n<=N subset. The convolution
   support for these cores is m<=2N<=96. From log n<4 and sigma>3/5,

       b_n*n^(-sigma)<n^(-1/2)<2/5,
       n^(1/5)*b_n*n^(-sigma)<n^(-3/10)<3/5,
       b_2*2^(-sigma)<3/4.

   Triangle only for the following variation budget (not the physical
   field) yields, summing over all harmonics in these eight cores,

       B_abs=sum |beta_m|m^(-sigma)<56/5,
       A_abs=sum |a_m|m^(-sigma)<84/5,  log m<5.

5. Put k(g)=(1-g)/(1+g) and Q_p=(1-g)*p^(-sigma)M_p so R_p=||Q_p||_2.
   Each harmonic of Q_p is

       m^(-sigma)*diag(k(g)*(beta_m+g*a_m),beta_m-g*a_m)*Rot(j*u).

   Here Rot(v)=[[cos v,-sin v],[sin v,cos v]]. At fixed auxiliary u,
   the g-derivative has norm <=m^(-sigma)*(2|beta_m|+|a_m|), using
   |k'|<=2 and |(k*g)'|<=1. The sigma-derivative has norm
   <=log(m)*m^(-sigma)*(|beta_m|+g|a_m|). Therefore

       |C_*(x,u)-C_*(a,u)| < 7*|x-a|/a     (a<=x<=a+19),

   uniformly in u; possible nonsmooth matrix norms use their Lipschitz
   inequality, not a differentiability assumption. A sufficient strict
   derivative majorant is

       [5*(532/25)/39 + (196/5)/10]/x = (6482/975)/x < 7/x.

6. Because log2>2/3 and the tau bound,

       19*inf u' > 19*(1/2-1/(39*14000))*(2/3) > 2pi.

   Thus u traverses a full circle in [a,b] for a unique b<a+19 with
   u(b)=u(a)+2pi. Choose a maximum of the frozen C_*(a,u), which is at
   least its mean, and use this first phase revolution to choose an
   actual x* in[a,b] attaining that phase modulo2pi. Pay both cost
   and anchor variation:

       C_*(x*,u(x*))-(1-g(x*))
       > (1-g(a))/20 - (71/10)*19/a
       > 1/50 - 1349/140000 > 1/100.

   Strictly, a maximum is at least its mean; the mean already exceeds
   the stated threshold, so no unjustified strict maximum/mean gap is
   required. The full cost is at least C_*. With 0<|E|<8 and all other
   payments nonnegative, conclude the target bounds. Do not claim an
   upper bound for |q| or |H/B|.

## Domain, seams, comparator and controls

Natural indices are N=33,...,48; seams are x_j=4pi*j^2-pi/40 for
j=34,...,48. Define closed chart endpoints

    l_33=x0, l_N=x_N for N>=34;
    r_N=x_(N+1) for N<=47, r_48=30000.

Each [l_N,r_N] has length>38. In particular the theorem covers the
first and last length19 interval in every chart, with new included
left and old limiting right data. No pointwise sign at a seam or x0 is
asserted. State this distinction expressly. Reuse Note14's signed jump
and whole payment if discussing a fixed-reference transfer; do not glue
unrelated charts or differentiate the floor.

This is new actual-height information about an estimating class. Direct
q evaluation can use it too. Its sign, positive coverage and measured
runtime are not acquired. Signed anchor/core aggregation, restrictions
coupling different eta_r, other products, and joint correction or source
payments are outside this theorem. The full two-dimensional finite
strip, effective tail onset/overlap, initial verification and whole
intermediate-time barrier remain separate unacquired inputs.

Run Controls12 against three distinct premises: complete literal source
enclosure; the acquired finite-coefficient/phase-velocity estimates; and
strict complete margin. A changed source may share the velocity estimate
or finite coefficients; do not assert that it fails every coarse estimate
merely because it fails the complete source identity. Preserve every
control's event/location and conditional qualifications. An honest
enclosure at an included zero always defeats the strict margin. Include
the exact quadratic check from Note20 without calling it theta arithmetic.

## Outputs, limits and stop rule

Write only notes/23_AGC_E18_ACTUAL_PHASE_RECURRENCE_20261119.md,
research-progress/handoffs/AGC-E18-r1-return.md and concise manuscript
sections/13_actual_phase_recurrence.tex. Root owns main.tex, shared
navigation, status, production records and history. Separate assessment
follows the proof; the author does not accept their own result on its
behalf. One analytical pass plus one correction pass. No numerical
samples, transcendental execution, interval campaign or rational-witness
replay is needed or authorized by this packet. Any later computation
requires its own frozen request before execution.

Acceptance is the actual-height existence theorem with all displayed
constants justified and scope retained, or a precise failed step and its
remaining numerical deficit. If the displayed variation budget fails,
one correction may sharpen its elementary constants without changing
P*, domain, width19 or estimating class. A new grouping, signed consumer,
phase scan or target change escalates to B; stop this local route.

## Pinned prerequisites

| Artifact | SHA-256 |
| --- | --- |
| Note17 | `23fee20746272c467a0563d6090605f85bbafcbf86921c0d86421d51bdeb00c0` |
| Note20 | `7b1de78efaf84e418e80fe9fc910a20c213b20cd1dddd8f0d206662c2e91608e` |
| Note21 | `46f2abae13f2d81648cccf2ea33e205b20e3a2f3d98ab78dd8eeba0432012a1b` |
| Review09 | `e06086e08cc502dd120a8cd06f68049670305ee20d9e9c5e2f6298adf6161390` |
| Section05 arithmetic source | `9c2be91c73a85408f15b9e3fd5755c9cbf766c896575a7d716ddb8c235dfcf8c` |
| B06 r1 request | `4d58fc2ca3887ce25d0b2e03d15c07eace0594e94af361352726fcaf8943cdb2` |

Hashes identify inputs, not mathematical validity. Record the actual
execution dispatch/available settings without inferring backend metadata.
