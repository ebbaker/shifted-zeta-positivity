# Target bounds for the heat-density program to prove RH implies simple zeros

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant mathematical checking; no independent specialist review.

**Purpose.** Specify bounds worth attempting in **01_heat_density_asymptotics**, together with the exact contradiction each would deliver. This is a new forward-looking note. [Note01][note1] remains the review of existing work and its limits.

The main candidates are:

| Target | Sufficient bound to seek | Why a multiple zero contradicts it |
| --- | --- | --- |
| **J: joint value/derivative margin** | For the completed finite arithmetic model, a normalized first-jet norm \(\ge cX^{-\beta}\), with \(\beta<3/4\). | The current through-zero approximation transfers this positive margin to \(H(0,\cdot)\), preventing \(H=H_z=0\). |
| **P: density second moment** | At a fully covered positive-time population, the Poisson density has \(2\pi\sqrt t\,\|p_{\sqrt t}\|_2^2-n<2/3\), including all errors. | A pair descended from one multiple endpoint forces excess at least \(2/3\). |
| **V: negative-time vertical moment** | A localized weak zero-density moment is \(o(s)\) at time \(-s\), uniformly enough to remove its regulator; a coefficient strictly below \(4\) also suffices. | An order-\(m\) endpoint contributes \(2m(m-1)s+o(s)\), at least \(4s+o(s)\). |
| **E: Rodgers–Tao energy** | \(E_I(t)\le A_I t^{\alpha-1}+e_I/t\), with \(\alpha>0\) and \(e_I<1/4\), down to zero. | Any multiple endpoint contributes at least \(1/(4t)+O(1)\). |

**These canonical bounds are unproved targets.** Their conditional implications and the constants below are derived explicitly. The research output here is a calibrated specification for the parent program, not a claim that formulating a criterion proves simplicity.

I would investigate **P as the closest density/energy application**, with **J as the most direct benchmark using the existing field theorem**. V is a separate opportunity for signed weak-density estimates on the negative crossover. E records the direct Rodgers–Tao requirement. The coefficient-transport machinery in Section 6 is an existing way to try to acquire these inputs.

The [result summaries][results], [control register][controls] and [patterns to avoid][avoid] apply. In particular [avoid/01][a01] requires distinguishing final-strength reformulations from intermediate estimates; it does not prohibit specifying aspirational bounds, which is the purpose of this investigation.

## 1. Common hypotheses, coverage and the existing approximation

Use the canonical heat coordinate throughout:
\[
 H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
 \tag{1.1}
\]
Assume RH. Then the endpoint zeros are real and all positive-time zeros are real and simple. Multiplicities at time zero are not assumed known or equal to one. The root dynamics and local heat splitting are classical; see [Polymath, Proposition 3.1][polymath] and the existing [BW10 root-motion note][bw19].

For a population-based target, every endpoint site in the target core must be included with **all** of its descendants and multiplicity. Its finite population size \(n\) is distinct from the arithmetic cutoff \(N\) below. An enclosing wall or a complete transport/count argument must establish membership and coverage. A favorable subset of roots does not cover an omitted multiple zero.

To prove simplicity of every zero, establish the selected target on a cover of every sufficiently high endpoint core, and certify the bounded-height remainder; evenness supplies the negative real heights. A bound averaged over many cores can leave sparse exceptional multiple zeros; it is not the same conclusion. Target J needs no zero labels: overlapping real charts suffice.

### Current Book input

The [Book crossover theorem][crossover] already supplies the completed model \(F_N\), \(N=\lfloor\sqrt{X/(4\pi)}\rfloor\), with
\[
 |\partial_z^j(H-F_N)|
 \le C_j\mathcal E_o X^{-3/4}e^{sL^2/16}(1+L)^j,
 \qquad j=0,1,2,3,
 \tag{1.2}
\]
on fixed buffered charts, where \(L=\log(X/(4\pi))\), \(s=\max(0,-t)\), and \(|t|L\le8\). On the positive side the exponential is one. The weaker \((1+\log X)^2X^{-3/4}\) allowance is needed on the longer positive band of [Ansatz Note26][ans26]; it is not necessary to use that weaker allowance exactly at zero.

The finite model retains both arithmetic arms, the complete finite mode sum and its Riemann–Siegel completion. Its heat residual is generally nonzero. The current physical construction instead uses its prescribed regulator and fixed averaging widths. Changing those for a new consumer is an additional theorem specification, not an inherited conclusion.

This distinction gives two different tasks: **estimate a favorable arithmetic quantity of the model**, and **transfer that quantity to the canonical field in the norm the consumer needs**. Target J already has a particularly simple transfer. Targets P and V need new nonlinear or weak transfer at their stated scales.

## 2. Target J: a quantitative joint first-jet bound

This is the cleanest target for the present retained-arithmetic formula.

On a microscopic real chart put
\[
 z=X+u/L,\quad |u|\le2,\qquad
 A_X=\mathcal E_o(0,X)>0,
\]
\[
 h_X(u)=H(0,X+u/L)/A_X,\qquad
 f_X(u)=F_N(0,X+u/L)/A_X.
 \tag{2.1}
\]
The frame \(A_X\), \(N\), \(X\) and \(L\) are frozen when differentiating in \(u\). Comparability of the envelope on this chart and (1.2) give
\[
 \sup_{|u|\le2}
 \left\|(h_X,h_X')-(f_X,f_X')\right\|_2
 \le \varepsilon_X,\qquad
 \varepsilon_X=C X^{-3/4}.
 \tag{2.2}
\]
One may use a larger explicitly acquired allowance; the exponent is the relevant current budget.

### J1: direct finite-arithmetic margin

Ask the parent program to prove, uniformly on target cores \(|u|\le1\),
\[
 \boxed{\quad
 \sqrt{|f_X(u)|^2+|f_X'(u)|^2}
       \ge cX^{-\beta},\qquad 0\le\beta<3/4,
 \quad}
 \tag{J1}
\]
for all sufficiently large charts, with \(c>0\) independent of the chart.

Then the corresponding norm for \(h_X\) is at least
\(cX^{-\beta}-CX^{-3/4}>0\). A multiple real zero would make both entries zero. RH turns exclusion of such real multiple zeros into simplicity of all nontrivial zeros, after bounded-height coverage.

A concrete target with room in the present error budget is
\[
 \boxed{|f_X|^2+|f_X'|^2\ge cX^{-1}.}
 \tag{J1a}
\]
Its norm margin is \(\sqrt c\,X^{-1/2}\). Once the approximation constants are instantiated, \(X>(C/\sqrt c)^4\), together with the theorem's own onset, suffices for the transfer.

**What HDA would need to prove.** A lower estimate for the *joint* complete finite arithmetic sum and its derivative. This is not a request for additional upper envelope terms. In a squared expansion, mixed arithmetic terms must be retained; the positive diagonal by itself is not a lower bound for the whole expression. Improvement of the model error would enlarge the permitted margin range, but J1a already fits the present accuracy.

**Classification.** J1 is a stronger quantitative arithmetic statement than qualitative simplicity. Its polynomial margin is not known to follow from simplicity alone. Nonvanishing of the exact first jet without a quantitative bound would merely restate the target. No evidence for J1 is claimed from a finite set of known-simple zeros.

### J2: an averaged bound that would produce J1's required margin

A possible parent-facing alternative is an integral of a smooth regularized finite-model quantity. Put
\[
 V_X=(f_X,f_X'),\qquad
 M_X\ge\max\{1,\sup_{|u|\le2}\|V_X'(u)\|_2\},
\]
\[
 I_X(r)=\int_{-2}^{2}
       \frac{du}{\sqrt{r^2+\|V_X(u)\|_2^2}},\qquad r>0.
 \tag{2.3}
\]
Only model jets through order two enter \(M_X\).

Suppose \(I_X(r)\le B_X\). At any \(u_0\in[-1,1]\), write \(v_0=\|V_X(u_0)\|_2\). On its unit neighborhood,
\[
 \sqrt{r^2+\|V_X(u)\|_2^2}
 \le r+v_0+M_X|u-u_0|.
\]
Integration and inversion yield the explicit lower bound
\[
 \boxed{\quad
 \|V_X(u_0)\|_2
 \ge \frac{M_X}{e^{M_XB_X/2}-1}-r.
 \quad}
 \tag{2.4}
\]
Thus choose \(r=\varepsilon_X\) and seek the complete bound
\[
 \boxed{\quad
 M_XB_X<
 2\log\left(1+\frac{M_X}{2\varepsilon_X}\right).
 \quad}
 \tag{J2}
\]
It forces \(\|V_X\|>\varepsilon_X\), sufficient for (2.2).

For example, any fixed \(0<\sigma<3/2\) and a uniform estimate
\[
 M_XB_X\le(3/2-\sigma)\log X
 \tag{2.5}
\]
would suffice eventually. This comparison uses \(M_X\ge1\) and (2.2); it does not assume \(M_X=O(1)\). A crude large derivative allowance can make (2.5) hard to meet, so the **product** \(M_XB_X\), not the integral alone, is the quantity to improve.

J2 is an optional way to obtain a lower margin from an averaged arithmetic estimate. Its regularizer applies to the joint jet, which is a new observable rather than the Book's existing field-only regulator. It is still a final-strength quantitative input when combined with its stated constants. The generic implication (2.4) is elementary; the canonical integral bound is the research problem.

## 3. Target P: a density second moment below one collision

This target expresses a regularized inverse-gap energy directly as a density second moment. It develops the same second-moment idea as [BW10 Note06][bw06], now with a Poisson kernel tied to heat time. The earlier note already established that absolute error below one event, not merely a relative asymptotic, is needed.

Let \(a_1(t),\ldots,a_n(t)\) be a complete covered finite real population at a positive time. For a spatial resolution \(y>0\) define
\[
 k_y(x)=\frac1\pi\frac{y}{x^2+y^2},\qquad
 p_{t,y}(x)=\sum_{i=1}^{n}k_y(x-a_i(t)).
 \tag{3.1}
\]
The integral of \(p_{t,y}\) is exactly \(n\). Define the self-subtracted second moment
\[
 \mathscr D_I(t,y)=2\pi y\int_{\mathbb R}p_{t,y}(x)^2\,dx-n.
 \tag{3.2}
\]

### Exact identity and the threshold

The elementary Poisson convolution integral is
\[
 \int_{\mathbb R}k_y(x-a)k_y(x-b)\,dx
 =\frac{2y}{\pi((a-b)^2+4y^2)}.
\]
Consequently
\[
 \boxed{\quad
 \mathscr D_I(t,y)
 =\sum_{i\ne j}\frac{4y^2}{(a_i-a_j)^2+4y^2}\ge0.
 \quad}
 \tag{3.3}
\]
The subtraction \(n\) removes the known self term of every **label**. It does not subtract unknown endpoint multiplicity as though every site were simple.

If the population contains a multiple endpoint, select two globally adjacent descendants from that site. The full real-root law gives
\[
 g'(t)=4/g(t)-2g(t)S_{\rm ext}(t),\qquad S_{\rm ext}\ge0,
 \quad g(0)=0,
\]
so \(g(t)^2\le8t\). This uses all exterior roots. For \(y^2=\kappa t\), the two ordered terms of this pair therefore imply
\[
 \boxed{\quad
 \mathscr D_I(t,\sqrt{\kappa t})
 \ge\frac{2\kappa}{2+\kappa}.
 \quad}
 \tag{3.4}
\]
No assumption of multiplicity exactly two is needed. At \(\kappa=1\), the exclusion target is
\[
 \boxed{\quad
 2\pi\sqrt t\,\|p_{t,\sqrt t}\|_2^2<n+\frac23.
 \quad}
 \tag{P1}
\]
The free heat double attains the threshold. A multiple site anywhere in the covered population contradicts P1 at **any** allowed positive time.

### P2: an aspirational asymptotic theorem

A useful form for HDA to attempt is
\[
 \boxed{\quad
 \mathscr D_{I_X}(t,\sqrt t)
 \le A_X(tL_X^2)^\alpha+e_X,
 \quad 0<t\le t_0(X),\quad \alpha>0,\quad e_X\to0,
 \quad}
 \tag{P2}
\]
with complete coverage, independently derived \(A_X<\infty\), and all source/localization errors included in \(e_X\). A quantitative version could bound
\(A_X\le C(n_X+1)^pX^B(1+\log X)^q\), with fixed declared exponents. Any proved such rate is useful; the exponents need not be optimized to imply simplicity.

For sufficiently large \(X\), take \(e_X<1/3\) and choose a source-prescribed time satisfying
\[
 0<t_X\le t_0(X),\qquad
 A_X(t_XL_X^2)^\alpha<1/3.
 \tag{3.5}
\]
Then P1 holds. Equivalently, the parent could prove P1 directly at one declared time \(t_X\), without a theorem for every smaller time.

The fixed-population statement \(\mathscr D_I(t,\sqrt t)\to0\) is equivalent to simple endpoints under the existing heat splitting. P2 with an explicitly controlled height/rate is the stronger quantitative target. It must be proved from canonical arithmetic; it is not an automatic nonlinear consequence of (1.2).

### The spatial scale and close simple pairs

Even distinct, well-spaced roots have a positive off-diagonal background. For an equally spaced reference with spacing \(d\),
\[
 \mathscr D_I(t,y)
 =8y^2\sum_{k=1}^{n-1}
       \frac{n-k}{k^2d^2+4y^2}
 \le\frac{4\pi^2}{3}n(y/d)^2.
 \tag{3.6}
\]
Thus a single-event target naturally asks for \(ntL_X^2\) small when \(d\asymp L_X^{-1}\). This is a scale calibration for that reference, not a spacing theorem for theta.

Close **simple** endpoint pairs also matter: for
\(H(t,z)=z^2-a^2-2t\), \(a>0\),
\[
 \mathscr D(t,\sqrt t)=\frac{2t}{a^2+3t}.
 \tag{3.7}
\]
It approaches \(2/3\) when \(a^2\ll t\), even though the endpoints are simple. Accordingly a convenient fixed clock cannot be justified just from simplicity or average spacing. A canonical bound for \(A_X\), or a different proved source-based choice of \(t_X\), is part of P2. This is why the target is not assigned an unsupported universal polylogarithmic time.

### What must be estimated in the Book variables

For the complete prepared polynomial \(P=\prod_i(z-a_i)\),
\[
 p_{t,y}(x)=-\frac1\pi\Im\frac{P_z}{P}(t,x+iy)
 =-\frac1\pi\Im\left(\frac{H_z}{H}-\frac{U_z}{U}\right)(t,x+iy).
 \tag{3.8}
\]
The entire exterior unit \(U\) remains. The recent RT contour interface and the existing HDC coefficient methods are relevant ways to acquire it.

The HDA producer request is therefore:

> Bound the **complete correlated second moment** of the deflated canonical logarithmic derivative at transverse distance \(y=\sqrt t\), with the label diagonal subtracted exactly, and an absolute excess budget below \(2/3\).

This is a new density/energy consumer of the Book's field and weak-potential machinery. The Book's fixed-width density \(R\) or its covariance \(Q\) is not identified with (3.2). A bridge, a shrinking spatial resolution, and any width-dependent errors must be proved.

### A finite transfer budget

Suppose the population lies in \([A,B]\), and only
\(J=[A-R,B+R]\) is integrated. Its exact exterior tail satisfies
\[
 2\pi y\int_{\mathbb R\setminus J}p_{t,y}^2
 \le T_{\rm tail}:=\frac{4n^2y^3}{3\pi R^3}.
 \tag{3.9}
\]
This follows from \(p\le ny/(\pi r^2)\) beyond either endpoint.

Let \(p_*\) be an acquired reference on \(J\), with
\(\|p-p_*\|_{L^2(J)}\le\epsilon_p\). Then a sufficient finite certificate is
\[
 \boxed{\quad
 2\pi y\|p_*\|_{L^2(J)}^2-n
 +2\pi y\{2\|p_*\|_{L^2(J)}\epsilon_p+\epsilon_p^2\}
 +T_{\rm tail}<\frac23,\quad y^2=t.
 \quad}
 \tag{P3}
\]
Quadrature/enclosure errors are additional terms if not already included. The count \(n\) and membership must be exact, or have their own rigorously signed allowances.

When the reference main term is of size \(n\), the cross-error has size
\(O(\sqrt{ny}\,\epsilon_p)\). Thus a merely small relative density error is insufficient at large \(n\): this comparison needs
\(\epsilon_p=o((ny)^{-1/2})\) for an \(o(1)\) absolute excess error. Coupled evaluation of the self-subtracted expression may improve the practical budget, but cannot remove the one-event scale.

This finite inequality is an actionable acquisition goal even before an all-height theorem. A genuinely smaller complete error or a new covered core would be an intermediate result.

## 4. Target V: a negative-time weak density moment

This candidate fits the signed crossover and the Book's weak density identity. It tests a different observable from P.

Fix a compact spatial chart \(D\) and a smooth nonnegative cutoff \(\chi\) supported inside it, equal to one on the target core. Put
\(\psi(x,y)=\chi(x,y)y^2\). Choose one fixed nonzero carrier \(A_X\), and write \(\mathcal H=H/A_X\); this constant division does not change zeros.

Introduce an **auxiliary constant regulator** \(\eta>0\):
\[
 \rho_\eta(t,z)=\frac1{4\pi}
       \Delta\log(|\mathcal H(t,z)|^2+\eta^2)
 =\frac{\eta^2|\mathcal H_z|^2}
        {\pi(|\mathcal H|^2+\eta^2)^2},
\]
\[
 Y_X(s,\eta)=\int_D\psi(z)\rho_\eta(-s,z)\,dA(z),
 \qquad s>0.
 \tag{4.1}
\]
This is an additional test family, not a silent replacement of the Book's prescribed physical regulator.

For fixed \(s\), as \(\eta\downarrow0\), the density converges distributionally to the zero-counting measure, with multiplicity. Hence
\[
 Y_X(s):=\lim_{\eta\downarrow0}Y_X(s,\eta)
 =\sum_{H(-s,z)=0}\chi(z)(\Im z)^2.
 \tag{4.2}
\]
Only zeros in the compact support contribute.

### Why the threshold is four

An order-\(m\) real endpoint \(a\) in the core has negative-time descendants
\[
 z_i(-s)=a+i\sqrt{2s}\lambda_i+O(s),
\]
where \(\lambda_i\) are the roots of \(\operatorname{He}_m\). Since
\(\sum_i\lambda_i^2=m(m-1)\), its contribution is
\[
 \sum_i(\Im z_i(-s))^2
       =2m(m-1)s+o(s).
 \tag{4.3}
\]
All other contributions to (4.2) are nonnegative. Thus a sufficient target is
\[
 \boxed{\quad
 \limsup_{s\downarrow0}
       \frac{\lim_{\eta\downarrow0}Y_X(s,\eta)}s<4
 \quad}
 \tag{V1}
\]
for every covered core. It excludes all \(m\ge2\), including odd multiplicities with one real descendant.

A concrete producer theorem sufficient for V1 would be
\[
 \boxed{\quad
 0\le Y_X(s,\eta)
 \le A_X^{\rm v}s^{1+\alpha}
          +C_X^{\rm v}\eta^\beta s^{-\gamma},
 \quad \alpha,\beta>0,\quad\gamma\ge0,
 \quad}
 \tag{V2}
\]
through all sufficiently small \(s,\eta>0\). The constants may depend on the fixed chart but must be acquired without assuming simple endpoint zeros. Taking \(\eta\downarrow0\) first and then \(s\downarrow0\) gives zero in V1. A bound with a leading \(c_Xs\), \(c_X<4\), and smaller remainder would also suffice.

V1 is a final-strength endpoint test; V2 is an unproved quantitative weak-density target. Bounds uniform only for one fixed regulator do not meet this contract.

### A precise weak-potential input and transfer cost

The Book's constant-regulator identity gives
\[
 Y_X(s,\eta)=\frac1{4\pi}
 \int_D\log(|\mathcal H(-s,z)|^2+\eta^2)\,\Delta\psi(z)\,dA.
 \tag{4.4}
\]
Thus HDA can attempt a **signed logarithmic-potential estimate** with the test \(\Delta(\chi y^2)\), keeping all cutoff terms. No sharply peaked density needs to be sampled.

If a holomorphic approximation \(\mathcal F\) on this chart satisfies
\(\sup_D|\mathcal H-\mathcal F|\le\delta_X(s)\), then
\[
 \boxed{\quad
 |Y_{\mathcal H}(s,\eta)-Y_{\mathcal F}(s,\eta)|
 \le \frac{\|\Delta\psi\|_{L^1}}{4\pi}
                   \frac{\delta_X(s)}{\eta}.
 \quad}
 \tag{4.5}
\]
Indeed the gradient of \(w\mapsto\log(|w|^2+\eta^2)\), as a function of two real variables, has norm at most \(1/\eta\). Apply the mean-value estimate inside (4.4).

For a one-event \(o(s)\) transfer, the sufficient demand is
\[
 \|\Delta\psi\|_1\,\delta_X(s)/\eta=o(s).
 \tag{4.6}
\]
On a chart scaled by \(L_X^{-1}\), the cutoff
\(\psi=y^2\chi(L_X(x-X),L_Xy)\) has
\(\|\Delta\psi\|_1=O(L_X^{-2})\). The condition becomes
\[
 \delta_X(s)/\eta=o(sL_X^2).
 \tag{4.7}
\]
This is a specific accuracy-versus-regulator requirement for the parent program.

If instead one uses a single joint regulator schedule to resolve a hypothetical order-\(m\) heat birth, one sufficient local resolution demand is
\(\eta=o(b(sL_X^2)^{m/2})\), where \(b\) is the nonzero normalized leading coefficient in that local chart. Combining this with (4.7) asks for
\[
 \delta_X(s)=o\!\left(b(sL_X^2)^{m/2+1}\right).
 \tag{4.8}
\]
A uniform proof must pay its multiplicity and unit-coefficient dependence; an iterated-limit theorem such as V2 is an alternative formulation. This explains exactly what stronger negative/crossover accuracy or direct weak cancellation would be useful for.

The signed integral in (4.4), rather than a separate absolute bound on each large term, is the relevant arithmetic target. The fixed positive-time physical estimates and the strong negative hierarchy away from zero are inputs to investigate, not substitutes for V2.

## 5. Target E: the direct Rodgers–Tao requirement

For a complete fixed endpoint population use the ordered raw energy
\[
 E_I(t)=\sum_{i\ne j}(a_i(t)-a_j(t))^{-2}.
\]
The already established Hermite expansion gives
\[
 tE_I(t)\longrightarrow
 \sum_{\text{endpoint sites }a}\frac{m_a(m_a-1)}8.
 \tag{5.1}
\]
The smallest nonzero contribution is \(1/4\).

Accordingly the parent-facing target is a canonical bound
\[
 \boxed{\quad
 E_{I_X}(t)\le A_X^{\rm E}t^{\alpha-1}+\frac{e_X}{t},
 \qquad \alpha>0,\quad e_X<1/4,
 \quad 0<t\le t_0(X).
 \quad}
 \tag{E1}
\]
For an all-height asymptotic version it is sufficient that \(e_X\to0\), with complete cores and a separately covered low-height region. The constant \(A_X^{\rm E}\) may grow with height; taking \(t\downarrow0\) at fixed \(X\) still gives the contradiction.

An integrated alternative is
\[
 \boxed{\quad
 \int_\epsilon^{T_X}E_{I_X}(t)\,dt
 \le B_X+c_X\log(T_X/\epsilon),
 \qquad c_X<1/4,\quad B_X<\infty,
 \quad}
 \tag{E2}
\]
uniformly as \(\epsilon\downarrow0\). Here \(B_X\) must be independent of \(\epsilon\). This is the precise logarithmic budget an adapted integrated-energy argument would need.

E1/E2 at final strength are endpoint simplicity reformulations under RH. An acquired arithmetic rate, constant or finite-domain improvement would be the intermediate achievement. Their value here is to state the theorem to request, with the critical coefficient fixed.

Target E also pays P: from (3.3),
\[
 \mathscr D_I(t,\sqrt t)\le4tE_I(t).
 \tag{5.2}
\]
The raw-energy route sees the exact endpoint coefficient, whereas the bounded density test can be easier to approximate. The inequality (5.2) alone would require \(tE<1/6\) to pass P1; use E1's own \(1/4\) threshold when it is available rather than losing that constant.

A stronger universal internal-dissipation coefficient is not the right producer request. For a two-root cluster the sharp internal dissipation is an identity, so it cannot be improved by a more accurate exterior approximation. The extra input must be a canonical arithmetic bound on the complete energy or its source/weighted-Hamiltonian representation, with all boundary and reference terms retained. [Rodgers–Tao][rt] and the local [RT Note02][rt2] motivate that type of calculation; their negative-threshold theorem does not already give E1/E2 under RH.

## 6. Existing machinery and a concrete order of work

The earlier [HDC forest-polynomial theorem][forest] and [complete coefficient transport][transport] should be reused. On a complete fixed wall, the latter gives a bound of the form
\[
 \|P_H(t)-P_*(t)\|
 \le \widehat B(t,T)\|P_H(T)-P_*(T)\|
       +\int_t^T\widehat B(t,s)\,\varepsilon_{\rm joint}(s)\,ds,
 \tag{6.1}
\]
where the full source quotient, exterior unit and actual model defect determine the joint residual. Internal gap divisions are absent from this coefficient theorem. Its coefficient uncertainty can feed the existing bounded spectral filter \(q(t)\), with the already established all-simple threshold \(q<1/2\), or a carefully derived P3 logarithmic-derivative enclosure.

That is an **acquisition tool**, not another independent target. The result becomes useful when the complete right side of (6.1), propagated through the actual consumer, fits its strict margin. A late simple anchor without this quantitative payment is insufficient.

I propose the following bounded first attempts in the parent investigation.

1. **J work package: finite arithmetic near-zero first jet.** Keep the current \(F_N\), its completion and its \(X^{-3/4}\) comparison. Seek J1a, or an analytic bound on the finite integral \(M_XI_X(\varepsilon_X)\) strong enough for J2. A weaker but explicit bound on this product or a new complete finite first-jet margin would be a measurable intermediate result. Compare against the direct joint-jet norm on the same data.

2. **P work package: small-positive-time density correlation.** Derive the deflated logarithmic-derivative/Poisson second moment from the unchanged source, retain its signed arithmetic cross terms, and compute the full P3 budget. Seek either a bound of form P2 with an acquired \(A_X\), or a strict P1 bound at a proved source-prescribed clock. Report the absolute excess, population, time, wall/coverage and error. A leading formula \(n+o(n)\) is useful density information but does not meet the one-event target.

3. **V work package: weak negative-time transverse moment.** Apply the signed crossover to (4.4), with an explicit family of cutoffs and auxiliary regulators. Seek V2 or a coefficient \(<4\), using (4.5) to determine the approximation order needed. First proving a uniform weak-transfer estimate at a stated joint scale is an intermediate result even before obtaining the favorable arithmetic coefficient.

4. **E comparison.** Any successful correlated density or coefficient estimate should be tested against E1/E2 and the existing direct first-jet comparator. Further generic energy identities are not the requested input; the target is a smaller complete canonical bound.

These are proposed mathematical tasks, not newly assigned tasks in another chat. No claim is made that one particular bound is already attainable. The cleanest current fit is J's transfer; P is the closest new density consumer; V requires the most explicit new regulator-uniform theorem.

## 7. Controls, status and what would count as progress

The controls are screened analytically, using their existing records rather than new numerical tests.

- A Hermite heat birth makes J's true joint jet zero, forces P's positive excess, contributes \(2m(m-1)\) to V's limiting coefficient and \(m(m-1)/8\) to E's. It therefore fails the desired strict bounds. It lacks the canonical theta source, so these targets must use that arithmetic.
- The RH-conditional theta-close controls in [BW10 Note05][bw05] meet the real-root and positive-source hypotheses while retaining endpoint doubles. They fail ordinary Dirichlet-series arithmetic. They show why a proof cannot depend only on generic source closeness or the heat equation.
- Euler-factor controls alter the canonical coefficients and conductor; at the \(c=1\) endpoint they also test multiple-zero detection. The \(0<c<1\) examples do not have the same endpoint all-real premise.
- Weighted-square/finite-tail controls fail the complete all-real premise of the positive-time argument. Reflected, shape and positive-primitive controls do not supply the full unchanged theta arithmetic. Local collision evidence is not silently upgraded into an all-real interval.
- The close **simple** pair (3.7) separately screens any proposed universal time schedule or uniform margin. It is not a counterexample to simplicity; it tests the additional quantitative strength of a target.

The parent need not prove a final-strength estimate in its first attempt. Useful intermediate outputs include an explicit first-jet lower margin, a smaller fully paid density-excess error, a new joint regulator/time transfer rate, or a coupled source residual that improves an existing complete certificate. Merely listing J/P/V/E, or checking their known collision costs, is not such an estimate.

The earlier [simplicity targets and hybrid consumer][old-targets], [Hermite domination][hermite] and [Note01][note1] remain the background. This note changes the emphasis to **what bounds to try to prove** in the heat-density investigation. It does not change their established mathematical statuses.

See the [assessment][assessment] and [source snapshot][inputs] for the derivation checks and inspection scope.

[a01]: ../../../../../avoid/01_restating_the_target.md
[ans26]: ../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md
[assessment]: ../reviews/02_TARGET_BOUNDS_ASSESSMENT_20261026.md
[avoid]: ../../../../../avoid/README.md
[bw05]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[bw06]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[bw19]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[crossover]: ../../../01_heat_density_asymptotics/book/sections/03_crossover.tex
[forest]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md
[hermite]: ../../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md
[inputs]: 02_TARGET_BOUNDS_INPUTS_20261026.json
[note1]: 01_RODGERS_TAO_REVIEW_AND_RH_SIMPLICITY_20261026.md
[old-targets]: ../../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/10_SIMPLICITY_THEOREM_TARGETS_AND_HYBRID_CONSUMER_20261023.md
[polymath]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../../result-summaries/README.md
[rt]: https://arxiv.org/html/1801.05914v5
[rt2]: ../../rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md
[transport]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
