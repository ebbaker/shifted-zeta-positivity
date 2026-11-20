# Recovering the marked roots and the counted cluster

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. AGC-ST-Z-E03 r1 execution dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. Conditional transfer and exact conditioning example, pending separate assessment. [Frozen request](../research-progress/handoffs/AGC_ST_Z_E03_REQUEST_R1_20261120.md) · [Position plan](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md) · [Second-order transport choice](../brainstorm/notes/06_AGC_ST_Z_B02_ODD_CUBIC_TRANSPORT_20261120.md)

Work in forward physical time \(H_t=-H_{zz}\) and in Newman height. On the fixed conjugation-invariant cleared contour \(\Gamma\), assume the count is two with multiplicities. The selected monic divisor is \(Q(z)=(z-c)^2-D\) with \(c,D\in\mathbb R\). A joint enclosure for \(c,D\) must concern the same counted pair and time. It can retain dependencies, or it can be contained in the product \(C\times [L,U]\), where \(C=[c_-,c_+]\). The products below give explicit bounds when only these two marginals are used. [Parent counted-pair law](../../manuscript/sections/02_pair_chain.tex)

## Separated positive discriminant

If \(L>0\), the roots are distinct and real, with labels \(a=c-\sqrt D<b=c+\sqrt D\). The product enclosure gives the explicit intervals
\[
 \begin{aligned}
 a&\in[c_- -\sqrt U,\ c_+ -\sqrt L],\\
 b&\in[c_- +\sqrt L,\ c_+ +\sqrt U].
 \end{aligned}
\]
Both widths are \(w(C)+\sqrt U-\sqrt L\), where \(w\) is interval width. They are the exact projections of the product enclosure. The ordering identifies the two simple continuations on a separated real chart anchored at \(t=0\). This local ordering requires separate information to attach a global ordinal.

For \(|c-\widehat c|\le e_c\), \(|D-\widehat D|\le e_D\) and \(\widehat D>e_D\), an equivalent error benchmark for either endpoint is
\[
 \big|(c\pm\sqrt D)-(\widehat c\pm\sqrt{\widehat D})\big|
 \le e_c+\frac{e_D}{\sqrt{\widehat D}+\sqrt{\widehat D-e_D}}.
\]
Indeed the exact gap-coordinate difference is \(|D-\widehat D|/(\sqrt D+\sqrt{\widehat D})\). The largest such difference over the stated discriminant interval occurs at its lower endpoint. A floor \(D,\widehat D\ge d>0\) gives the simpler Lipschitz constant \(1/(2\sqrt d)\). [Position plan benchmark](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md)

## Matching two occurrences across zero

For real \(d\) put \(\sigma(d)=\sqrt d\) if \(d\ge0\) and \(\sigma(d)=i\sqrt{-d}\) if \(d<0\). For two pairs with real centers \(c,\widehat c\), use the distance that minimizes the larger matching error over the two bijections of counted occurrences. This definition includes the two copies of a double root. Pairing corresponding signs in \(c\pm\sigma(D)\) and \(\widehat c\pm\sigma(\widehat D)\) attains the minimum. In fact if \(u=\sigma(D)-\sigma(\widehat D)\) and \(\delta c=c-\widehat c\), the maximum squared error for that pairing is
\[
 (\delta c)^2+|u|^2+2|\delta c\,\Re u|.
\]
For the transposition replace \(u\) by \(\sigma(D)+\sigma(\widehat D)\). When the discriminants have the same sign, both the modulus and the absolute real part of the difference are at most those of the sum. For opposite signs, these two magnitudes coincide under either pairing. This proves the optimal matching formula.

The exact centered part of the distance is
\[
 |\sigma(D)-\sigma(\widehat D)|=
 \begin{cases}
 \dfrac{|D-\widehat D|}{\sqrt{|D|}+\sqrt{|\widehat D|}},
   &D,\widehat D\ \text{of the same sign or one zero, with nonzero denominator},\\[5pt]
 \sqrt{|D-\widehat D|},&D\widehat D<0,\\
 0,&D=\widehat D=0 .
 \end{cases}
\]
In the first case it is at most \(\sqrt{|D-\widehat D|}\), since the squared difference of two nonnegative square roots is at most the difference of their squared magnitudes in absolute value. Thus the uniform matching bound for all real discriminants is \(e_c+\sqrt{e_D}\) for the same coefficient error allowances as above, now with \(e_D\ge0\) and arbitrary real \(\widehat D\). The square-root constant \(1\) is attained when the centers agree and the discriminants have opposite signs or one is zero.

If \(L\le0\le U\), the possible offsets from an allowed center range over \([-\sqrt U,\sqrt U]\) on the real axis or \(i[-\sqrt{-L},\sqrt{-L}]\) on the imaginary axis. The two offsets of a single pair must be opposite. The single-occurrence enclosure from the product is the union of
\[
 [c_- -\sqrt U,\ c_+ +\sqrt U]
 \quad\text{and}\quad C+i[-\sqrt{-L},\sqrt{-L}] .
\]
For example, the exact worst matching error over this product to the double \(\{\widehat c,\widehat c\}\) is \(\max(e_c+\sqrt U,\sqrt{e_c^2-L})\) with \(e_c=\max(|c_- -\widehat c|,|c_+-\widehat c|)\). Report the count-two cluster and the joint center and discriminant enclosure when the sign is unresolved. Positive \(D\) orders the real roots, negative \(D\) gives conjugate roots with an optional upper/lower half-plane convention, and \(D=0\) puts two occurrences at \(c\). When the enclosure permits a double, it gives no separate continuation for the two oriented real labels through the merger. [Pair coordinates through a double](../../manuscript/sections/02_pair_chain.tex)

### An exact heat double

The even polynomial \(H(t,z)=z^2-2t\) satisfies \(H_t=-H_{zz}\). For \(|z|=r\) and \(2|t|<r^2\) it has two counted occurrences and a boundary floor \(r^2-2|t|\). At \(t=0\) both occurrences are at zero; at \(t>0\) they are the simple real pair \(\pm\sqrt{2t}\); at \(t<0\) they are the conjugates \(\pm i\sqrt{-2t}\). The matching distance from \(t=0\) is exactly \(\sqrt{2|t|}=\sqrt{|D(t)-D(0)|}\). Matching across \(t=0\) from \(-h\) to \(h\) gives distance \(2\sqrt h=\sqrt{|D(h)-D(-h)|}\). These exact distances show the sharp constant and preclude a Lipschitz discriminant-to-root bound near zero in this polynomial class. The double fails the uniform singleton slope assumption and the polynomial lacks the complete theta source.

Meanwhile the complete contour of \(B=2z/(z^2-2t)\) gives \(J_0=2,\ J_1=0,\ J_2=4t\) and hence \(c=0,\ D=2t\) throughout the chart. The velocity contour gives \(c'=0,\ D'=2\) at the double itself. The contour has regular coefficient readouts even though the root map is only square-root conditioned. For a canonical application those coefficients and their error budgets are conditional on independent clearance, a count of two and an enclosure of the complete trace on the contour. A boundary denominator floor and the field and derivative errors there are inputs to that trace enclosure. The singleton transport from E02 supplies separated real data. A near-double application instead needs a joint coefficient enclosure, for example from these contour moments, without using a singleton slope at the merger. [E01 contour and Hermite readout](08_AGC_ST_Z_E01_ORIENTED_TRACE_20261120.md#readout-on-the-counted-chart) · [Parent contour error comparison](../../manuscript/sections/06_residual_transport.tex)

## First-exit transport with shared variables

In the separated regime, let \(i\in\{a,b\}\) denote the anchored simple roots. Use the E02 first-exit data on a prescribed \([0,h]\). Each \(X_i\) encloses the initial position. A cleared count-two chart, real path boxes separated from each other, a uniform nonzero \(H_z\) floor on the boxes, and a bound \(U_i\) for \(|H_{zz}/H_z|\) with \(X_i+[-hU_i,hU_i]\) strictly inside its box ensure the continued simple branch stays there. The velocity enclosure \(V_i\) is taken at the initial anchor. The acceleration enclosure \(A_i\) uses the complete source on its first-exit tube. Both depend on the applicable source and derivative errors. [E02 proof](09_AGC_ST_Z_E02_CENTER_ACCELERATION_20261120.md)

Use the same variables \(x_i^0\in X_i,\ v_i^0\in V_i,\ u_i\in A_i\) in both outputs, with
\[
 u_i=\frac{2}{h^2}\int_0^h(h-t)x_i''(t)\,dt,\qquad
 y_i=x_i^0+hv_i^0+\tfrac12 h^2u_i,\qquad
 (c,s)=\left(\frac{y_a+y_b}{2},\frac{y_b-y_a}{2}\right).
\]
Here \(s>0\) on the separated chart and \(D=s^2\). The center and half-gap can be propagated jointly with these shared inputs. The inverse \(c-s=y_a,\ c+s=y_b\) is exactly the direct singleton affine projection. Under interval addition the endpoint enclosures are \(Y_i=X_i+hV_i+\tfrac12h^2 A_i\) with widths
\[
 w_i=w(X_i)+h\,w(V_i)+\tfrac12 h^2 w(A_i).
\]
For a signed endpoint displacement the corresponding width omits the initial position term, since \(y_i-x_i^0=hv_i^0+\tfrac12h^2u_i\) uses the same anchor. The center displacement is the mean of these two displacement expressions. Sign is determined when the resulting displacement interval is strictly on one side of zero. The widths from separate input intervals are valid even if the underlying source constrains those variables further.

For the projected marginal boxes from \(Y_a,Y_b\), both \(C=(Y_a+Y_b)/2\) and \(S=(Y_b-Y_a)/2\) have width \((w_a+w_b)/2\). If \(S\) lies on the positive half-line, replacing the joint enclosure by the independent product \(C\times S^2\), then taking the square root of \(S^2\), gives each endpoint width \(w_a+w_b\). The extra width relative to the shared projection is \(w_b\) for \(a\) and \(w_a\) for \(b\). If the projected \(S\) extends to zero or below, a certified positive lower bound from the path boxes can restrict it before using this separated calculation. The stated width loss is for the unclipped positive projection. Its reduction by other source constraints requires keeping those constraints in the comparison.

Before a source test, the three justified claims are the conditional formulas for the widths, the exact tie between shared affine recovery and the equally informed direct singleton projection, and the exact loss from discarding the specified correlation. A precise E04 comparison is to fix the anchor data, \(h\), chart and source precision before any terminal root solve, report \(w_a,w_b\) from the written predictor, and compare each with the width of a separately certified direct terminal bracket from the same source information in Newman height. This is a width comparison at matched source inputs, with the terminal brackets used for comparison after the predictor is fixed. Its numerical outcome and displacement signs depend on the acquired data. [Position plan and benchmark](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md)

The transfer is a finite conditional enclosure under the target classification. At a counted collision the singleton denominator fails, while the cleared joint coefficient readout continues. The change of arithmetic source or other failed input for each registered control is as in E01, including the Euler-factor preservation of real anchors with a changed analytic exterior. This transfer uses the actual coefficients of the chosen field and allows either sign of \(D\). [E01 control screen](08_AGC_ST_Z_E01_ORIENTED_TRACE_20261120.md#source-screen-and-the-input-for-a-time-bound) · [Results index](../../../../../result-summaries/README.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md) · [Scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
