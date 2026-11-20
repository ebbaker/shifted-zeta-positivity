# The oriented trace determines the initial velocity

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. AGC-ST-Z-E01 r1 execution dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. Exact derivation and polynomial obstruction, pending separate assessment. [Frozen request](../research-progress/handoffs/AGC_ST_Z_E01_REQUEST_R1_20261120.md) · [B01 decision](../brainstorm/notes/05_AGC_ST_Z_B01_ORIENTED_ANCHOR_20261120.md) · [Position overview](../research-overview/02_AGC_ST_ZERO_POSITIONS_RESEARCH_OVERVIEW_20261120.md)

## Readout on the counted chart

Use forward physical Newman time, a fixed physical origin and \(H_t=-H_{zz}\). The conjugation-invariant contour \(\Gamma\) stays cleared and counts two occurrences. An independent anchor at \(t=0\) locates the two real positive roots and fixes the labels by increasing height. The count describes this local pair. An ordinal in the full divisor requires a separate count or calibration. The formulas continue with the same counted occurrences on a cleared chart. Write
\[
 \mathcal I f=\frac{1}{2\pi i}\oint_\Gamma f(z)\,dz,\qquad
 B=H_z/H,\qquad Q=(z-c)^2-D,\qquad H=QA,\qquad R=A_z/A .
\]
The moments \(J_k=\mathcal I(z^kB)\) give \(J_0=2\), \(c=J_1/2\), and \(D=J_2/2-c^2\). Their complete physical time law is
\[
 J_k'=\mathcal I\big((z^k)_z B^2-(z^k)_{zz} B\big).
\]
This follows from \(B_t=-\partial_z(B_z+B^2)\) and integration by parts on the cleared contour. The same formula holds for deformations within a cleared collar by the cancellation of endpoint terms on the closed contour. [Parent pair law](../../manuscript/sections/02_pair_chain.tex) · [Local spatial generator](02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md)

With \(w=z-c\), \(s^2=D\), \(a=c-s\) and \(b=c+s\), the remainder of \(R\) modulo \(Q\) is \(r_0+r_1w\), where
\[
 r_0=\frac{R(a)+R(b)}2,\qquad r_1=\frac{R(b)-R(a)}{b-a}.
\]
The state retained at the anchor is \((Q,r_0,r_1)\), with the orientation fixed by the labels. At fixed \(z\) the generator gives
\[
 -2c'w-D'=Q_t=-\operatorname{rem}_{Q}(2+4wR)
               =-4r_0w-2-4Dr_1 .
\]
Thus \(c'=2r_0\), \(D'=2+4Dr_1=2-4DM\) with \(M=-r_1\), and on the separated real chart
\[
 a'=-1/s+2R(a),\qquad b'=1/s+2R(b).
\]
Indeed, the singleton exterior germs at \(a,b\) are \(R+1/(z-b)\) and \(R+1/(z-a)\), respectively. The law \(x'=2R_{\{x\}}(x)=H_{zz}(x)/H_z(x)\) restores the other target in each singleton. The two singleton contour integrals of \(H_{zz}/H\) give these velocities by residues. On their common larger contour,
\[
 c'=\tfrac12\mathcal I(H_{zz}/H),\qquad
 D'=\mathcal I(wH_{zz}/H),\qquad
 r_0=\mathcal I(wB/Q),\qquad r_1=\mathcal I(B/Q).
\]
For the velocity formulas use \(H_{zz}/H=-Q_t/Q-A_t/A\), with \(A_t/A\) holomorphic in the cell. The identities \(\mathcal I(w/Q)=1\) and \(\mathcal I(w^2/Q)=\mathcal I(1/Q)=0\) then give both velocities. In the trace formulas the target term \(B-R=Q_z/Q\), multiplied by either weight, has total residue zero. The remaining residues use \(R\) and give its symmetric mean and divided difference. This direct calculation and the assembled tree use the same field and the same cleared pair. [Pair and moment readouts](03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md) · [Direct contour readout](../../manuscript/sections/06_residual_transport.tex)

At a double the two trace values are \(R(c)\) and \(R_z(c)\), the Hermite coefficients modulo \(w^2\). The contour formulas show their analytic continuation in time, including from \(D>0\) to \(D<0\). The term \(4Dr_1\) vanishes at the double, so \(c'=2R(c)\) and \(D'=2\) there. The ordered singleton velocity formulas require separation. The polynomial gives the two occurrences through coalescence, with the time-zero labels used only on the separated real branch.

## Complete exterior and moment equations

Use the parent's even product, with every zero occurrence counted and the logarithmic derivative grouped by opposite pairs \(\{\rho,-\rho\}\). On the positive pair chart, where the two partners \(-a,-b\) are exterior, remove the two target poles from \(B\) and keep the partners. Explicitly,
\[
 R(z)=\frac1{z+a}+\frac1{z+b}+
 \sum_{\{\rho,-\rho\}\,\text{untouched}}
       \left(\frac1{z-\rho}+\frac1{z+\rho}\right).
\]
The general rule is to remove only the selected occurrences from their groups. A group containing both targets then disappears, and a partner left exterior is kept with its multiplicity. This rule also gives the two exterior occurrences at \(-c\) when a positive pair coalesces at \(c\).

Accordingly, the two exterior target partners contribute
\[
 \frac1{2a}+\frac2{a+b}+\frac1{2b}
\]
to \(c'\) on the separated positive chart. Each untouched opposite group contributes
\[
 \frac{2a}{a^2-\rho^2}+\frac{2b}{b^2-\rho^2}.
\]
This signed group has an \(O(|\rho|^{-2})\) tail per group uniformly on a fixed compact chart. With the inherited zero count the grouped series converges absolutely with tail \(O(\log(2+N)/N)\) beyond radius \(N\). The real conjugation symmetry makes the combined value real, with nonreal occurrences included. The individual first-power poles are used only in the prescribed grouping or a finite part. In contrast, for the divided difference each exterior occurrence contributes an absolutely summable term
\[
 M=\sum_{\rho\text{ exterior}}\frac1{(\rho-a)(\rho-b)}.
\]
This sum applies also at \(a=b\), with its Hermite value \(M=-R_z(c)\). The tree adds the complete sibling logarithmic derivatives to the parent exterior, so the same partner terms and tail appear in either calculation. [Complete product and count](../../manuscript/sections/02_pair_chain.tex) · [Sibling response](02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md#product-and-sibling-response)

For \(q_\rho=(\rho-c)^2-D\), keep \(S_n=\sum_{\rm ext}q_\rho^{-n}\) for \(n\ge1\) and \(T_n=\sum_{\rm ext}(\rho-c)q_\rho^{-n}\) for \(n\ge2\). The contour readout is \(-\mathcal I(kB)\) with \(k=Q^{-n}\) and \(k=wQ^{-n}\), respectively. For such a weight its time derivative is
\[
 \frac{d}{dt}[-\mathcal I(kB)]
     =-\mathcal I\big((k_t-k_{zz})B+k_z B^2\big).
\]
The inherited symmetric rows, with complete products, are
\[
 \begin{aligned}
 S_n'&=2n\sum_{j=1}^{n}S_j S_{n+1-j}
     +2n\sum_{j=2}^{n}(T_jT_{n+2-j}+DS_jS_{n+2-j})
     -4n(n+2)S_{n+1}-4n(n+3)DS_{n+2}, &&n\ge1,\\
 T_n'&=2(2n-1)\sum_{j=2}^{n}T_j S_{n+1-j}
     +4nD\sum_{j=2}^{n}T_j S_{n+2-j}
     -4(n^2+n-1)T_{n+1}-4n(n+3)DT_{n+2}, &&n\ge2 .
 \end{aligned}
\]
On the separated chart the parent mixed and axis equations use the same trace derivative with \(k=(z-b)^{-p}(z-a)^{-q}\), \(p,q\ge0,\ p+q\ge2\). The time-dependent weight retains the motion of both targets. The mixed products between exterior blocks enter the complete rows, including \(4M_LM_R\) in \(M'=2M^2-12S_2-16DS_3\) for an exterior split \(M=M_L+M_R\). The inherited first time-jet passage uses convergence of spatial jets of the opposite-paired products on the fixed contour at one slice and \(B_t=-B_{zz}-2BB_z\). It applies at fixed moment order. The oriented initial state gives the two coefficient velocities, while these rows continue to use the full trace. [Parent hierarchy and fixed-order passage](../../manuscript/sections/03_hierarchy.tex) · [Mixed block products](03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md#products-across-the-exterior-split)

## The inherited gap-drift check

In Baker's anchored comparison, use the initial polynomial \((z^2-1)(z^2-4)(z^2-u)\), with \(u=1/4,6\) and the adjacent marked roots \(1,2\). Both cases have \(D=1/4\). The exterior \(-1,-2\) contributes \(1/4\) to \(M\) and \(17/12\) to \(c'\). Evaluating the poles of \(\pm\sqrt u\) gives the remaining contributions \(2(u+2)/[(u-1)(u-4)]\) and \(2/(1-u)+4/(4-u)\), respectively. The first is \(8/5\) in each case. This gives the common \(M=37/20\) and \(D'=3/20\), with center velocities \(103/20\) and \(-59/60\) in that order. The independently anchored initial positions, gap and gap drift therefore leave the center velocity undetermined within this finite even polynomial heat class. [Original anchored control](../../../brainstorm/notes/06_SPATIAL_TTN_ZERO_SPACING_20261119.md#20-november-2026-discussion-of-absolute-zero-positions)

## A common oriented state with different displacement

Now set \(P(z)=(z^2-1)(z^2-4)\), \(\lambda=\pm1/32\), and \(F_\lambda(z)=P(z)+\lambda P(z)^4\). The exact solutions are
\[
 H_\lambda(t,z)=\sum_{j=0}^{8}\frac{(-t)^j}{j!}F_\lambda^{(2j)}(z).
\]
On \([1,2]\), \(P(z)=(z^2-5/2)^2-9/4\), so \(|P(z)|\le9/4\) and \(|\lambda P(z)^3|\le729/2048<1\). By continuity the strict bound also holds on a common sufficiently thin closed rectangle containing \([1,2]\) in its interior and excluding \(-1,-2\). Thus the two \(F_\lambda=P(1+\lambda P^3)\) have just the same two simple zeros \(1,2\) in that rectangle and its boundary is zero-free. Uniform continuity on the boundary and the argument principle preserve the count for a common short time interval. The simple roots continue by the implicit function theorem and are real by uniqueness and conjugation, with increasing positive labels for sufficiently small real time.

At the anchor the deflated factor is \((z+1)(z+2)(1+\lambda P^3)\). The logarithmic derivative of the last factor vanishes at each endpoint, so for both signs
\[
 Q(0,z)=(z-1)(z-2),\quad c(0)=\tfrac32,\quad D(0)=\tfrac14,
 \qquad R(1)=\tfrac56,\quad R(2)=\tfrac7{12},\quad
 r_0=\tfrac{17}{24},\quad r_1=-\tfrac14 .
\]
The two branch velocities are \(a'=-1/3\) and \(b'=19/6\) in both fields, giving \(c'=17/12\) and \(D'=7/4\). The spatial derivatives \(F_j=\partial_z^j H_\lambda(0,x)\) at either root \(x=1,2\) agree for \(0\le j\le3\), since \(P^4\) vanishes to fourth order.

For a simple root \(x(t)\), twice differentiating \(H_\lambda(t,x(t))=0\) and using the heat law gives at \(t=0\)
\[
 v=x'=\frac{F_2}{F_1},\qquad
 x''=\frac{-F_4+2vF_3-v^2F_2}{F_1}.
\]
Use \(\Delta\) for the value at \(\lambda=+1/32\) minus that at \(\lambda=-1/32\). Only \(F_4\) changes in the formula for \(x''\), with
\[
 \Delta F_4=\frac{24}{16}P'(x)^4,\qquad
 \Delta x''=-\frac32 P'(x)^3 .
\]
Because \(P'(1)=-6\) and \(P'(2)=12\),
\[
 \Delta a''=324,\qquad \Delta b''=-2592,\qquad
 \Delta c''=-1134,\qquad \Delta D''=-1458 .
\]
Here \(D=(b-a)^2/4\) gives the last difference using the common initial gap and gap drift. The initial coordinates and first derivatives agree, and the continuations are analytic. In particular,
\[
 c_{+1/32}(t)-c_{-1/32}(t)=-567t^2+O(t^3)
\]
as \(t\downarrow0\), so their signed center displacements differ at every sufficiently small positive time. For any common prediction \(p_c(t)\) of the center displacement from the retained initial state and the time \(t\), the two-input triangle inequality gives
\[
 \liminf_{t\downarrow0}\frac{1}{t^2}
 \max_{\lambda=\pm1/32}
      \big|p_c(t)-(c_\lambda(t)-c_\lambda(0))\big|
 \ \ge\ \frac{567}{2}.
\]
The same data also leave both individual trajectories undetermined, by the nonzero endpoint acceleration differences. This is a finite-time information obstruction in the stated class of even polynomial heat evolutions with a locally counted positive pair, even when the initial coefficient velocity accompanies the anchor. The full exterior germs differ. The two time-zero fields lack the complete theta source.

## Source screen and the input for a time bound

For an Euler-factor control \(H^{\eta,p}(0,z)=f(z)H(0,z)\) with \(f(z)=1+\eta\cos(\tfrac12\log(p)\,z)\), \(0<\eta<1\), the entire real zero list with multiplicities agrees at time zero because \(f>0\) on the real axis. The analytic field acquires the nonconstant factor, with additional nonreal occurrences, and on a common local chart where \(f\) is nonvanishing the exterior trace acquires \(f_z/f\). At a shared simple root \(x\) the physical velocity consequently acquires \(2f_z(x)/f(x)\), which can vanish at an individual root. The changed source and complete exterior distinguish this control even when the real anchors agree. [Euler-factor control, structure and heat flow](../../../../../papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex)

The catalogue's weighted-square and finite-source controls have changed complete coefficients. Finite-prime orbit controls also fail full reflection. The reflected super-Gaussian and smooth positive-primitive controls lack the theta square expansion. Reflection rigidity identifies the source in its normalized square-comb class, while the motion estimate still needs quantitative trace data. The fixed-event atoms and finite-profile threshold controls lack the full theta profile and eventual simplicity at their events. The RH-conditional endpoint control fails ordinary Dirichlet-series arithmetic. The fixed-amplitude variable-kernel control fails the full cosine/Newman law. A cleared chart containing a genuine double keeps both occurrences and the Hermite formula. Applying the exact identities in collision-free boxes of these controls is compatible with the differences in their source premises. [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Branch premise screen](../research-overview/01_AGC_ST_RESEARCH_OVERVIEW_20261119.md#tests-and-ownership) · [Control premise rule](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)

To enclose the displacement from \(0\) to \(t>0\), supply a bound for the signed complete center drift or for the time remainder after subtracting the anchor drift. For example, the latter correction is \(\int_0^t(t-u)c''(u)\,du\). Acquiring the trace from source values requires clearance, a denominator floor and derivative and integration error bounds on the declared chart. For either endpoint, add the correlated relative term \(\pm(\sqrt{D(t)}-\sqrt{D(0)})\) on the separated real chart. A uniform positive lower bound on \(D\) controls conversion of a \(D\)-error to a square-root error, and absolute positioning also pays the uncertainty of the initial anchor. Give the direct calculation the same source information and chart. [Position plan and direct error comparison](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md)

The readout is a local representation identity. The common-state control is a quantified local information obstruction for the specified polynomial class. B02 owns the choice of a complete time remainder from independently acquired source information. [Results index](../../../../../result-summaries/README.md) · [Tensor results](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md) · [Scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
