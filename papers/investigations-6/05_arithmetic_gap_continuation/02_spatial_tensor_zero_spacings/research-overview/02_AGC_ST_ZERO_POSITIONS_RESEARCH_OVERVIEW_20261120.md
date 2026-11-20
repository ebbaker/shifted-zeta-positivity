# The equations of a spatial tensor tree for zeros

20 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. The opening position overview has no recorded lead configuration. The position milestone records gpt-6.2-astra/ultra coordination. The recorded chat settings for this program revision are gpt-6.2-astra, reasoning effort max.

**What must a block of zeros tell its neighbors for the whole tree to evolve, and can those equations simplify the gap chain and its moments?** This is the primary research question. The individual zero positions are the preferred prediction when the zeros are separated and anchored. Their differences give every adjacent gap, while their common displacement also records motion of the whole block. The gap and its exterior moments are the quantities to keep when asking *why* a spacing changes. Both outputs belong to one evolving state. [Comparison of the two outputs](../reviews/06_AGC_ST_GAP_AND_POSITION_COMPARISON_20261120.md) · [Parent gap chain](../../manuscript/sections/02_pair_chain.tex) · [Parent moment hierarchy](../../manuscript/sections/03_hierarchy.tex)

## What fixes the network at one time?

Before choosing a field, write \(u_I=C_I(u_L\otimes u_R)\) for a proposed contraction of two child messages. In a differentiable choice of coordinates it must satisfy
\[
 \dot u_I=\dot C_I(u_L\otimes u_R)
          +C_I(\dot u_L\otimes u_R+u_L\otimes\dot u_R).
\]
This identity constrains any dynamics assigned to the tensors. The field law must still determine the messages and their velocities. Require the exact observable to agree under the two groupings of three children, allowing for a change of basis on an internal index. Ask which part of the contraction is fixed by that consistency and which depends on how space is partitioned.

Start with a scalar field \(F(t,z)\) holomorphic in \(z\) and differentiable in \(t\), with \(F_t\) also holomorphic and differentiation valid on the contours below. A finite spatial partition has an outer boundary and cuts that stay clear of zeros on the time interval under study. Each node \(I\) contains a finite count of zeros with multiplicity. In a fixed spatial coordinate set
\[
 P_I(z)=\prod_{\rho\in I}(z-\rho),\qquad A_I=F/P_I,\qquad R_I=\frac{\partial_z A_I}{A_I}.
\]
The monic polynomial \(P_I\) represents the interior. Its coefficients, equivalently the count and the required power sums, stay defined through an internal merger. The nonvanishing factor \(A_I\) supplies the influence from outside. Its logarithmic derivative \(R_I\) includes any zero-free factor of the field. The outermost node needs that exterior information as boundary data. [Counted polynomials, Newton identities and exterior data](../notes/02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md)

For children \(L,R\) of \(I\), factorization forces
\[
 P_I=P_LP_R,\qquad
 R_L=R_I+\frac{\partial_z P_R}{P_R},\qquad
 R_R=R_I+\frac{\partial_z P_L}{P_L}.
\]
The two downward identities are read near the receiving child's zeros, where its sibling polynomial is nonzero. In coefficient coordinates the upward tensor is convolution, \((P_I)_k=\sum_{i+j=k}(P_L)_i(P_R)_j\), after translating to a common origin. The downward pass supplies each child with the sibling's field and the parent's exterior. Reassociating exact products gives the same divisor and exterior at a leaf. These laws constrain the tensors for any admissible grouping. The choice of cuts, basis and retained coefficients becomes consequential when one seeks a simpler evolution. At a zero crossing an internal cut, the enclosing parent still carries the full count. Continuing with smaller cells requires a cleared split and a count or verified overlap. [Spatial split and change of coordinates](../notes/02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md)

## Which time law is compatible with that split?

Write a dot for differentiation at fixed \(z\). Differentiating \(F=P_IA_I\) gives the starting equations for a supplied field velocity \(F_t\).
\[
 \dot P_I=\operatorname{rem}_{P_I}(F_t/A_I),\qquad
 W_I=\frac{F_t/A_I-\dot P_I}{P_I}=\frac{\dot A_I}{A_I},\qquad
 \dot R_I=\partial_z W_I.
\]
The remainder matches the Taylor coefficients at each zero through one less than its multiplicity. Monicity fixes \(\dot P_I\) to degree below the count, and the quotient defining \(W_I\) extends across the zeros. An empty cell has \(P_I=1\) and \(\dot P_I=0\). The generator of the field supplies \(F_t\). Consistency of the network requires
\[
 \dot P_I=\dot P_LP_R+P_L\dot P_R,\qquad W_L=W_I+\dot P_R/P_R
\]
and the exchanged equation for \(W_R\). Thus evolving the two children and then contracting must agree with evolving their parent. A time-dependent basis or origin contributes its own derivative to this comparison. A direct check uses \(B=F_z/F\) and \(B_t=\partial_z(F_t/F)\). On a closed, cleared contour the derivative of the moment with weight \(w(t,z)\) is the integral of \(w_t B-w_z F_t/F\) with measure \(dz/(2\pi i)\). The two sides of an internal wall cancel when they carry the same full traces. [Product and contour derivations for heat flow](../notes/02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md#independent-contour-balance)

The first differential law of interest is the **class** \(F_t=-F_{zz}\), with the initial field still free. It gives
\[
 \dot P_I=-\operatorname{rem}_{P_I}(P_{I,zz}+2R_I P_{I,z}),\qquad
 B_t=-\partial_z(B_z+B^2).
\]
The existing split calculation already identifies the distinction the research must resolve. One value of \(R_I\) per distinct root determines the instantaneous coefficient velocity. For a singleton \(P_I=z-x\), the next step requires
\(\frac{d}{dt}R_I(t,x(t))=-2R_{I,zz}(t,x(t))\).
Which exterior quantities, or which controlled remainders, let such data propagate on a time interval and serve multiple neighboring blocks? The full exterior field and the direct contour equations supply the exact benchmark. [Generator and exterior time law](../notes/02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md#samples-at-repeated-roots) · [Internal assessment](../reviews/02_AGC_ST_LOCAL_GENERATOR_ASSESSMENT_20261120.md)

## What would simplify the arithmetic gap chain?

On a separated real edge \(x_n=a<b=x_{n+1}\), write \(c_n=(a+b)/2\), \(g_n=b-a\), \(D_n=g_n^2/4\), and \(R_n\) for the exterior of that pair. Its positions are \(c_n\pm\sqrt{D_n}\). The oriented sum \(c_n'=R_n(a)+R_n(b)\) recovers the common motion. The divided difference gives \(M_n=-[R_n(b)-R_n(a)]/g_n\). At a double, the monic quadratic \((z-c_n)^2-D_n\) carries the unordered pair with multiplicity. An absolute forecast needs an initial position anchor and a label on each separated chart. [Counted pair equations](../../manuscript/sections/02_pair_chain.tex) · [Recovery through a merger](../notes/10_AGC_ST_Z_E03_ROOT_RECOVERY_20261120.md)

Under the parent's complete-product and count hypotheses, let \(w_\rho=\rho-c_n\), \(Q_\rho=w_\rho^2-D_n\), \(S_{n,k}=\sum_{\rm ext}Q_\rho^{-k}\) for \(k\ge1\), and \(T_{n,k}=\sum_{\rm ext}w_\rho Q_\rho^{-k}\) for \(k\ge2\). Each sum includes the entire exterior with multiplicity, including nonreal zeros. In forward physical time the first rows read
\[
 M_n=S_{n,1},\qquad D_n'=2-4D_nM_n,\qquad
 g_n'=4/g_n-2g_nM_n,\qquad
 M_n'=2M_n^2-\big(12S_{n,2}+16D_nS_{n,3}\big).
\]
On an entirely real simple chain the exterior distances are cumulative sums of adjacent gaps. On a finite real block the other occurrences still contribute. Adjacent rows share a root and exterior data. When \(M_n=M_L+M_R\) is split across two exterior blocks, \(2M_n^2\) contains \(4M_LM_R\). The next even row also contains \(4T_{n,2}^2\). A reduced state must account for these mixed contributions and the moving centers of the moments. [Chain and block telescope](../../manuscript/sections/02_pair_chain.tex) · [Moment recurrences and overlap identity](../../manuscript/sections/03_hierarchy.tex) · [Terms across a spatial split](../notes/03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md#products-across-the-exterior-split)

The first opportunity is to use one exterior response at a shared endpoint for both adjacent rows and combine the signed terms before bounding them. The parent already cancels internal velocities in the sum of the gaps across a block. The open question is what survives **on an individual edge or moment row** after that cancellation. A result could identify fewer independently evolving exterior quantities, or give a bound for the omitted contribution that can be integrated in time. Its direct comparator receives the same data and correlations. [Parent continuation estimates](../../manuscript/sections/04_continuation.tex) · [Scope of the existing block cancellation](../reviews/02_AGC_ST_LOCAL_GENERATOR_ASSESSMENT_20261120.md#neighboring-edges-and-the-scope-of-the-aggregate)

## What the completed comparisons establish

- **Absolute motion.** For the first positive Newman pair near heights 28 and 42, anchored positions and velocities, a fixed exterior observation and sign and count data predicted both positions at \(t=10^{-4}\) to widths below \(1.574\times10^{-10}\) and \(8.466\times10^{-11}\). Both moved toward smaller heights. Direct endpoint bisection gave width \(2^{-54}\) per zero. Two finite even polynomial heat flows also show that the initial marked positions and gap velocity can agree while the center velocities have opposite signs. [Position milestone](../notes/13_AGC_ST_Z_POSITION_MILESTONE_AND_CONTINUATION_20261120.md) · [Scope of the polynomial control](../notes/08_AGC_ST_Z_E01_ORIENTED_TRACE_20261120.md#the-inherited-gap-drift-check)
- **Relative motion.** On the same interval the gap shrinks at a decreasing rate. One exterior zero near 50 and nonnegative remaining contributions certify \(g''>1/180\). Subtracting the two separate fixed-probe acceleration intervals leaves both signs possible. At high labels on fixed intervals \(0<t_0\le t\le t_*\le 1/2\), pairing opposite marks also improves a deterministic term in the forcing estimate. The equally informed direct sum shares that gain and the source localization error dominates it. Speed, uniform rank and control of a chain at new heights remain open. [Readout comparison](../reviews/06_AGC_ST_GAP_AND_POSITION_COMPARISON_20261120.md) · [High-label assessment](../reviews/03_AGC_ST_SPATIAL_FORCING_ASSESSMENT_20261120.md)

The split and time identities are structural identities. A reduction is judged by the independent quantities it eliminates or the signed error it bounds, with the class and the observable specified. The collision controls illustrate the distinction. A cleared cell can contain a true double, where a separated gap fails. An Euler factor can preserve the initial real zero list while changing the exterior trace. Weighted-square and finite-source controls change the coefficients, finite-prime controls lose full reflection, and reflected or positive-primitive sources lack the theta square expansion. Fixed-event and finite-profile controls change the full profile, the normalized endpoint control changes ordinary Dirichlet arithmetic, and a changed observation kernel can change the evolution law. Fractional-mass relaxations lose the integer divisor. These distinctions enter when a particular estimate uses the corresponding premise. [Results index](../../../../../result-summaries/README.md) · [Tensor and gap results](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Premise screen](../reviews/02_AGC_ST_LOCAL_GENERATOR_ASSESSMENT_20261120.md#collision-premise-screen) · [Patterns index](../../../../../avoid/README.md) · [Representation versus gain](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)

**Next decision.** AGC-ST-Z-B06 is ready for conceptual work (B, Astra/ultra). Specify the state on one split and its reassociation, the exterior information at the outer boundary, and the equations a reduced state would have to satisfy under time evolution. The plan and register specify the proof that follows and when a particular field or test becomes relevant. [Research plan](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md) · [Current progress and continuation](../research-progress/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PROGRESS_20261120.md)
