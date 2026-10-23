# Complete boundary subtraction and a scoped comparison

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model internal checks; no specialist review.

**Status: HDC-02 complete at the exact-expression level, conditional on the explicitly listed boundary inputs.** Generic identities and the scoped control/comparison statements below are **proved in-note**. No theta lower interval is acquired. The additional findings are a polynomial counterexample to dropping the complete relative energy, and a comparison confined to shared holomorphic residual models and uniform pathwise error payments. Neither is a universal obstruction to heat deformation.

Use [Note 02](02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md) for the fixed geometry, unchanged source, all-root population, complete chart-free estimator and source input list. This follows the [result index](../../../../result-summaries/README.md), [local geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [coupled-estimation rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The finite expression is an estimating interface, not a new sign theorem.

## 1. Assemble a physical chain before estimating

Let \(\mathcal B\) be the forward left cap minus all other outward faces of W_-, excluding the time-zero cap. Thus \(B_\epsilon=\int_{\mathcal B}\mathcal C\). Equations (4)–(5) of Note 02 are an unconditional algebraic expression for this chain wherever E>0. Cancel common cell interfaces exactly. If approximate functions are used, they must be restrictions of the same approximant on the shared interface; two independently rounded values are not an exact cancellation.

For the optional phase reduction, extract the certified equal-radius root disks over

\[
 \gamma:\ -iY\to-\epsilon-iY\to-\epsilon+iY\to iY.
\]

The orientations are the bottom face traversed backwards, the left cap upwards, and the top face forwards. Put

\[
 a_\rho=\frac{k_\rho}{2\pi},\qquad k_\rho=\frac{\rho^2}{1+\rho^2},\qquad
 \mathscr D(\tau)=\prod_{j=1}^NH_z(\tau,z_j(\tau)),\quad K=\mathscr D'/\mathscr D.
\]

The fixed wall gives a symmetric all-root product; root labels are only needed locally for its factorization. Boundary regularity and the actual inverse charts imply nonvanishing on a neighborhood of gamma. Interior events are permitted. Define the **signed physical complement**, not an unspecified small error,

\[
 J:=\int_{\mathcal B-\mathcal T_\gamma}\mathcal C,
\]

where \(\mathcal T_\gamma\) is the root-disk three-chain. It includes left-cap complements, complements on both imaginary faces with their negative-outward signs, all four spatial faces with those signs, and any exposed transitions. Note 02's f,p,r,s compute it. Matched joins cancel; unmatched ones remain. Then the inherited disk reduction proves

\[
 \boxed{B_\epsilon=a_\rho\operatorname{Im}\int_\gamma K(\tau)\,d\tau+J.}
 \tag{1}
\]

This uses inverse charts along the broken boundary path only. A globally regular tube over the time rectangle would be a stronger, event-excluding hypothesis, and is not used in (1).

There is a useful exact check on the complement when both gamma and the direct vertical edge v have certified disks. The symmetric product extends holomorphically through interior collisions: it is the discriminant of the monic root polynomial times the nonvanishing symmetric product of U at the roots, up to sign. The local heat multiplicity theorem makes its zero count, with multiplicity, equal to Q_-. The positively oriented rectangle is v followed by reversed gamma. The argument principle therefore gives

\[
 a_\rho\Im\left(\int_vK\,d\tau-\int_\gamma K\,d\tau\right)=k_\rho Q_-,
 \qquad J_0-J=(1-k_\rho)Q_-.
 \tag{1a}
\]

Here J0 is the full direct-cap complement. Thus the root disks alone collect only the fraction k_rho of the integer event charge; their complements carry the rest. At the proposed rho=1/100, k_rho=1/10001. Shrinking these disks does not shrink the complete event contribution. Equation (1a) is bookkeeping, not an independent enclosure for J in terms of an already known Q_-.

## 2. Complete finite reference subtraction

Freeze a reference spacing independently of unknown gaps:

\[
 d_*=\frac\pi{\ell(36)},\quad \ell(36)=\tfrac14\log\frac{36}{4\pi}>0,
 \qquad r_{jk}=d_*(k-j),\quad j<k.
\]

After the population is acquired, label its simple roots at \(\tau=-\epsilon\) lexicographically by (real part, imaginary part), and continue along the open path. Roots need not be real. The reference is constant in time; it makes no assertion of close spacing. Write \(d_{jk}=z_k-z_j\) and

\[
 R=8\sum_{j<k}r_{jk}^{-2},\qquad
 L_1=-16\sum_{j<k}\frac{d_{jk}-r_{jk}}{r_{jk}^3},\qquad
 E_{\rm rel}=8\sum_{j<k}\frac{\widehat V(d_{jk}/r_{jk})}{r_{jk}^2},
\]
\[
 \widehat V(u)=u^{-2}-1+2(u-1).
\]

For \(H=U\prod_j(z-z_j)\), let \(a=\partial_z\log U\) and

\[
 \mathcal B_U=2\sum_{j<k}\frac{a(\tau,z_k)-a(\tau,z_j)}{z_k-z_j}
 +\sum_j\bigl(a(\tau,z_j)^2-3a_z(\tau,z_j)\bigr).
\]

The inherited material derivative and finite triple cancellation give

\[
 K=R+F,\quad F=L_1+E_{\rm rel}+\mathcal B_U
 =\sum_j\left[\left(\frac{H_2}{H_1}\right)^2-\frac{H_3}{H_1}\right]_{z=z_j}-R.
 \tag{2}
\]

For completeness, the root velocity is H2/H1 and differentiating log H1 along it gives the last sum. With \(S_{r,j}=\sum_{k\ne j}(z_j-z_k)^{-r}\), its summand is
\(S_{1,j}^2+3S_{2,j}+2a_jS_{1,j}+a_j^2-3a'_j\).
The distinct-triple terms in \(\sum S_{1,j}^2\) vanish, leaving \(\sum S_{2,j}\); pairing the remaining sums gives \(8\sum d_{jk}^{-2}+\mathcal B_U\). Finally, insert the exact identity
\(d^{-2}=r^{-2}-2(d-r)r^{-3}+r^{-2}\widehat V(d/r)\).

Thus the first coupled estimating target is precisely

\[
 \boxed{B_\epsilon=2a_\rho YR+
 \underbrace{a_\rho\operatorname{Im}\int_\gamma
 (L_1+E_{\rm rel}+\mathcal B_U)\,d\tau+J}_{\mathcal R_{\rm complete}}.}
 \tag{3}
\]

The full root-jet expression in (2) is often a better way to enclose F than separate pair and unit bounds: it retains their correlation automatically. Its signed dependence on common source coefficients must remain intact through the sum and integration. The unit contains exterior zeros and normalization; no exterior sum was discarded. All roots in the wall are included, so there is no artificial internal cutoff. Radius and reference derivatives are zero by this contract, not omitted as small. If either moves, (3) needs its corresponding extra terms. Individual reference pieces depend on labeling, but their total F=K−R does not.

The subtraction is the finite algebraic mechanism used as motivation by [Rodgers–Tao, Sections 7–8](https://arxiv.org/html/1801.05914). Their global negative-time real-zero and relaxation estimates are under a contradiction hypothesis and are not imported. The close-pair squared-gap scale in [Csordas–Odlyzko–Smith–Varga, equation (2.19)](https://etna.ricam.oeaw.ac.at/vol.1.1993/pp104-111.dir/pp104-111.pdf) is consistent with the inherited two-root comparator, not a theta boundary certificate. [Polymath, Theorem 1.5](https://arxiv.org/html/1904.12438) does not certify the microscopic positive face chosen here.

## 3. A usable enclosure interface, including transverse errors

Suppose jointly derived source information gives \(F=F_*+e\) on gamma with \(|e(\tau)|\le\eta(\tau)\), a rigorously evaluated nominal line integral, and \(J\ge J_*-E_J\). Including the nominal quadrature error in \(E_{\rm quad}\) gives

\[
 L_{\rm deform}=2a_\rho YR+a_\rho\Im\int_\gamma F_*d\tau+J_*
 -a_\rho\int_\gamma\eta\,|d\tau|-E_J-E_{\rm quad}
 \le B_\epsilon\le I_0.
 \tag{4}
\]

This last triangle inequality is a fallback, not a requirement to discard known correlations. A single shared coefficient uncertainty set may instead be propagated through the full signed functional, including J. HDC-03 must supply either a paid interval for \(\mathcal R_{\rm complete}\), or the sufficient inputs to (4). A bound only for E_rel, one cap, or one face does not meet it.

No transverse approximation appears in (1)–(4); all complex-time values are actually included. If instead reducing a vertical cap to real time, assume the all-root product is holomorphic and nonzero on that vertical neighborhood and is of real type. Conjugation-invariance of the complete population suffices; individual roots need not be real. Then

\[
 I_t^{\rm disks}=\frac{k_\rho}{\pi}\int_0^Y\Re K(t+i\sigma)\,d\sigma,
\quad
 \left|I_t^{\rm disks}-\frac{k_\rho Y}{\pi}K(t)\right|
 \le\frac{k_\rho Y^3}{6\pi}\sup|K''(t+i\sigma)|.
 \tag{5}
\]

The linear Taylor term has zero real part; the integral second-order remainder proves the constant. In this alternative, (5)'s error, both horizontal faces and J all stay in (3). Real positivity of E_rel can be used at a real slice only when its gaps are positive real, and only with those transverse and face costs retained.

## 4. A heat control forbids dropping the complete relative energy

Consider the event-free neighborhood of zero for

\[
 H(\tau,z)=z^2-\tfrac14-2\tau,\qquad
 d(\tau)=\sqrt{1+8\tau},\quad r=1.
\]

Its only joint event is \(\tau=-1/8,z=0\); take \(0<\epsilon<1/8\) and a sufficiently small Y. For real t in this slab the roots are real and \(E_{\rm rel}(t)=8V(d(t))\ge0\). Nevertheless,

\[
 E_{\rm rel}(\tau)=8[(1+8\tau)^{-1}-3+2\sqrt{1+8\tau}]
 =384\tau^2-3584\tau^3+30208\tau^4+O(\tau^5),
\]
\[
 \int_0^Y\Re E_{\rm rel}(i\sigma)\,d\sigma
 =-128Y^3+O(Y^5)<0.
 \tag{6}
\]

This is not just a formal small-Y sign. For even n≥4, the coefficient c_n satisfies \(0<c_n<8\cdot8^n\), by the binomial series. Hence the absolute remainder after −128Y³ is at most

\[
 \frac{8Y(8Y)^4}{5(1-64Y^2)},\qquad 0<Y<1/8.
\]

It is smaller than 128Y³ for \(0<Y\le1/100\), including the contract's Y. Cauchy's theorem gives \(\Im\int_\gamma E_{\rm rel}d\tau=2\int_0^Y\Re E_{\rm rel}(i\sigma)d\sigma<0\). Thus **even an event-free polynomial heat flow with positive real gaps can have a negative complete relative-energy contribution**. Translating z centers this control in the specified spatial band. A proof that simply drops E_rel from (3) has the wrong inequality direction on this example. This does not invalidate dropping its real value inside the fully paid alternative (5).

Other required controls retain their expected behavior. A negative-time quadratic event contributes one full unit to I0−B; a time-zero event invalidates the regular cap; a later shifted event prevents automatic extension. For \(H=e^{\ell^2\tau}\sin(\ell z)/\ell\), H2=0 and H3=−ell²H1 at each root, so \(K=N\ell^2\). Its pair gaps are constant: the omitted-unit shortcut would miss the necessary contribution of \(\mathcal B_U\). The published source families pass the generic identities and fail the canonical premises listed in Note 02. No new exclusion inequality is claimed to reject those families.

## 5. What an equally informed direct method already receives

If the direct vertical root charts are paid, then

\[
 I_0=a_\rho\Im\int_vK\,d\tau+J_0,
 \quad v:[-iY,iY],
\]

with its full cap complement J0. Otherwise the direct method uses the nonsingular density in Note 02. Comparing the line contribution alone while withholding J or J0 does not compare the chosen observable.

**Shared analytic coefficients.** Let a nominal F_* and a finite family of residual basis functions \(\psi_m\) be holomorphic on a neighborhood of the closed negative time rectangle. For any common coefficient uncertainty set C,

\[
 \int_\gamma\psi_m\,d\tau=\int_v\psi_m\,d\tau,
 \qquad
 \inf_{c\in C}\Im\sum_mc_m\int_\gamma\psi_m\,d\tau
 =\inf_{c\in C}\Im\sum_mc_m\int_v\psi_m\,d\tau.
 \tag{7}
\]

The proof is Cauchy's theorem on gamma followed by the reversed direct edge, and equality of the linear functionals on the same coefficient set. Thus transport gives **exactly the same payment for these shared holomorphic coefficients**, including signed correlations. This statement does not assume actual K is holomorphic: any poles of actual K must remain in the residual not covered by (7). They cannot be hidden in a purported holomorphic model with an unpaid remainder.

**Uniform residual disk, regular-tube subclass.** Suppose additionally the whole root tube is regular on the rectangle, F and F_* are holomorphic there, \(|F-F_*|\le\eta\) uniformly, and the same independently paid lower bound is available for the complete complement. Exact transport gives equal nominal centers and equal exact disk contributions. The triangle-rule allowance along gamma is

\[
 a_\rho(2Y+2\epsilon)\eta,
\]

while direct vertical integration pays \(2a_\rho Y\eta\). The broken-path **triangle estimator** is therefore no stronger under these explicitly matched assumptions. At epsilon=Y its scalar residual allowance is twice the direct allowance. A direct method using the shared analytic structure may also implement the cancellation first, yielding equality rather than paying the extra length. No claim is made that the triangle rule is optimal over holomorphic functions, or that the complete fixed-box theta comparison has been performed.

The special regular-tube hypothesis is used only for this comparison, not for (1)–(4). Interior events, different source error profiles, different complement enclosures, and measured acquisition cost are outside that domination statement. A two-root wall/discriminant survival test remains the fair comparison only if survival becomes the target; it is unnecessary for the lower-bound transfer.

## 6. The next acquisition must test a specific advantage

HDC-03 now has an explicit target: certify the fixed physical boundary and enclose (3) jointly, while obtaining a direct enclosure of the same fixed-box I0 from identical source information. Preserve negative-time smoothing and source correlations in both. Record the complement and its error separately in the output, even when estimated jointly. A potential gain could come from smaller source errors on the broken boundary, cheaper full-boundary evaluation, or a genuinely better coupled bound including J. It cannot come merely from relabeling the shared analytic coefficients in (7).

The claimed gain must survive the total error comparison, including quadrature, both source tails, geometry verification, and complementary faces. In the fallback regime it must overcome the extra horizontal-path allowance rather than report only a smaller negative cap. Failure of the fixed trial parameters or this residual class is to be recorded with that scope. The program is not closed: HDC-03 inputs and HDC-04's actual theta comparison remain open.
