# GNP-RS-B10 — a signed quadratic estimate by Mellin projection

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Registered chat0007, thread
`01a1d19b-462e-7722-a6be-3d1555a82423`, title “Find a signed joint
estimate”. Actual backend model and reasoning effort are unavailable in
the recorded source configurations. Checking is by the same assistant;
no independent or separate-agent review is claimed.

**Status: proved in-note from named published and inherited inputs;
same-assistant checking.** The signed quantity controlled is the real
quadratic correlation consumed by the tail norm, including all shifts.
This is not an absolute bound for every individual complex block in B09.
The resulting useful window exponent is **17/81**, improving B08's
17/72 by **17/648**. The unchanged logarithmic residual and Green rates
hold for windows with an arbitrary fixed positive power margin.
**No every-center estimate is proved.**

Under [avoid01][a01] this is an averaged quantitative milestone, not an
RH-equivalent criterion. Read the [result index][results] and
[avoid index][avoid], specifically [cluster11][r11], [premise02][a02],
[scope07][a07], [separate-bounds12][a12] and [imports16][a16]. Section 7
screens the [collision controls][controls]. No literature priority is
claimed for Mellin projection or zeta mean-square estimates.

## 1. Statement, parameters and exact signed consumer

Retain [B07][b07] and [B08][b08]'s complete theta field, c=1, physical
time fixed inside each spatial window, original strip/depth/radius, exact
convolution measure dσ, and block-constant prime cutoff. Their residual
definitions, full-field provider and internal-review qualifications remain.
Write L=log(U/(4π)), ℒ=1+log U, and

\[
 B=N_U=\lfloor\sqrt{U/(4\pi)}\rfloor,
 w_x=x^{-3/4}e^{(\log x)^2/(4L)},\qquad
 \tau(u)=u/2+\pi/(8L).
\]

Use the fixed χ from B07, with χ≥0, support [-2,3], integral four and
the same Fourier convention. For integers 0≤a<b≤B set

\[
 D_{a,b}(u)=\sum_{a<n\le b}w_ne^{i\tau(u)\log n},\quad
 \mathcal Q_{a,b}=\ell^{-1}\int\chi((u-U)/\ell)|D_{a,b}(u)|^2du,
\]
\[
 \mathcal S_{a,b}=\sum_{a<m<n\le b}w_mw_n
 e^{i\tau(U)\log(n/m)}
 \widehat\chi\bigl((\ell/2)\log(n/m)\bigr).
\]

The exact identity, before any estimate, is

\[
 \mathcal Q_{a,b}=4\sum_{a<n\le b}w_n^2+2\operatorname{Re}\mathcal S_{a,b}.
 \tag{B10.1}
\]

Thus an upper bound on this full signed real correlation suffices for
the norm consumer. We do not need |S_N| for each m-block, a sign for
each shift, or a nonresonance assumption. All integers, including B09's
lattice-gradient resonances, remain in (B10.1).

The explicit choices are

\[
 \theta=19/60,\quad Z=\lfloor U^{1/3}\rfloor,
 \quad M=U^{1/10},\quad Y=\lfloor U^{1/10}\rfloor,
 \quad\eta=1/8,\quad\beta=17/81.
 \tag{B10.2}
\]

**Theorem.** For each fixed 0<ρ≤47/162, all sufficiently large real U,
all integers 2≤P≤floor(L²), and U^(17/81+ρ)≤ell≤U,

\[
 \boxed{|\mathscr R(U,\ell;P)-\mu_P|
 \le C(\sqrt{\mu_P}/L+L^{-2})
       +O_\rho\bigl(U^{-\min(7/6480,\,9\rho/28)}\bigr).}
 \tag{B10.3}
\]

At P=floor(L²), the residual-mean error remains Oρ(L^(-3/2)), the
residual mean Oρ(L^(-1)), the Green mean Oρ(L^(-1/3)), and the
fixed-h>0 exceptional proportion O_(h,ρ)(L^(-1)). Constants/onsets are
finite analytical ones, not numerically evaluated or certified. This
proof does not optimize the exponent or the remainder cap.

## 2. Published input and a uniform translated mean bound

[Bourgain–Watt v1, Theorem 4, printed page 1][bw] proves the cumulative
critical-line mean-square error bound E(V)=Oε(V^(1515/4816+ε)).
The newly inspected passage and unchanged external PDF identity are in
the [source-use addendum][source]. This is a different use of the paper
from B09's failed direct import of Theorem 2. Its shift hypotheses are
not hypotheses of Theorem 4. We use the published theorem as an input,
not a new verification of its complete proof.

Choose ε_src=151/144480. Since

\[
 19/60-1515/4816=151/72240>0,
\]

the published result gives |E(V)|≤C(1+V)^θ for θ=19/60 after enlarging
C on bounded V. Subtracting the cumulative formula at the two endpoints,
and using |ζ(1/2-it)|=|ζ(1/2+it)|, proves: for every real interval I
of length at most c ell contained in [-R,R], R≥2, ell≥1,

\[
 \int_I|\zeta(1/2+it)|^2dt
 \le C_c\{\ell\log(2+R)+R^\theta\}.
 \tag{B10.4}
\]

An interval crossing zero is split at zero; values in a bounded interval
are absorbed into C_c. This does **not** assert a short-interval
asymptotic below the published mean-square scale. Its cumulative error
R^θ is retained and will be multiplied by the actual small arm weight.

## 3. Exact sharp-cutoff Mellin projection, with both tails paid

For this section 1≤ell≤sqrt(U) and U is large enough that 2≤Z<B.
Put a(x)=sqrt(x)w_x=x^(-1/4)exp((log x)²/(4L)). Choose a fixed smooth
increasing q with q=0 on (-∞,0], q=1 on [1/2,∞), and 0≤q≤1.
Define

\[
 b(x)=a(x)q(x-Z-1/4)q(B+3/4-x),\qquad
 \widetilde b(z)=\int_0^\infty b(x)x^z\,dx/x.
 \tag{B10.5}
\]

For every positive integer n, b(n)=a(n)1_(Z<n≤B). These transitions
are entirely between integers: this is the exact sharp finite sum,
with no omitted endpoint coefficients. They introduce a kernel tail,
which is estimated below rather than discarded.

Let A=U^(-1/18) and g(y)=b(e^y). With constants depending only on q,

\[
 \|g\|_1\le CA\mathcal L,\qquad
 \|g'\|_1\le CA,\qquad
 \|g''\|_1\le CAB.
 \tag{B10.6}
\]

Here and below A is just this amplitude scale, not the complete arm A(u).
To verify (B10.6), on the support log x/log U lies between 1/3+o(1)
and 1/2+o(1), and

\[
 \log a(U^\alpha)
   =-\alpha(1-\alpha)\log U/4+O(1).
\]

The O(1) is uniform on this compact α-range, since L=log U-log(4π).
Thus sup a≤CA. Its logarithmic derivative is -1/4+(log x)/(2L),
so a decreases up to sqrt(U/(4π)) and increases only over the bounded
extra endpoint extension. Its total variation is O(A). The smooth
end transitions have logarithmic widths comparable to 1/Z and 1/B;
their first derivative L1 cost is O(A), second derivative cost O(AB).
Interior second derivatives cost at most O(Aℒ)≤O(AB). These observations
also give all higher derivative bounds needed for contour convergence.

With k(v)=tilde b(iv)/(2π), integration by parts gives

\[
 |k(v)|\le CA\min\{\mathcal L,|v|^{-1},B|v|^{-2}\},
 \tag{B10.7}
\]

where the terms with v in the denominator are used only for v≠0.
Consequently, because B≤sqrt U and 0<θ<1,

\[
 \begin{aligned}
 \int|k(v)|dv&\le CA\mathcal L,\\
 \int|k(v)|\log(2+U+|v|)dv&\le CA\mathcal L^2,\\
 \int|k(v)|(U+|v|)^\theta dv&\le CAU^\theta\mathcal L.
 \end{aligned}\tag{B10.8}
\]

For clarity, split at |v|=1/ℒ, B and U. The L1 integral between
1/ℒ and B costs A log(Bℒ). Beyond U the last integral is at most
CAB U^(θ-1)/(1-θ)≤CAU^θ; the logarithmic tail is at most
CAB(log U+1)/U. This explicitly pays heights outside the original
interval; no compact support in Mellin frequency is assumed.
These frequency shifts are in the auxiliary ζ identity; they do not
change the physical Newman time fixed inside a Green window.

For s=1/2-iτ, Mellin inversion first on Re z=1 and then shifting to
Re z=0 gives the exact identity

\[
 \sum_n b(n)n^{-s}
 =\widetilde b(1-s)+\int_{\mathbb R}k(v)\zeta(s+iv)dv.
 \tag{B10.9}
\]

The crossed pole is the simple pole of ζ at s+z=1, with residue one.
Compact smooth support gives arbitrary vertical decay for tilde b for
each fixed U. Polynomial vertical growth for ζ in this strip follows,
for example, from its one-step Euler summation formula on Re s>0;
thus the horizontal contour integrals tend to zero. There is no
truncated-Perron error. The constants in the estimates used to bound
the resulting integral are the uniform ones in (B10.6)–(B10.8).

The residue is also paid. For |τ| comparable to U,

\[
 |\widetilde b(1/2+i\tau)|
 \le C A B^{1/2}/|\tau|\le CAU^{-3/4}.
 \tag{B10.10}
\]

Indeed y↦e^(y/2)a(e^y) is increasing in the interior; the two cutoffs
make its total variation O(A sqrt B). One integration by parts proves
(B10.10). Throughout the χ-window τ(u) is comparable to U.

Apply Cauchy–Schwarz to the integral in (B10.9), using |k| as its
measure, then integrate against χ/ell. For each v, (B10.4) applies
with R=C(U+|v|) after the change t=v-τ(u); its Jacobian is exactly
1/2 and its interval length is 5ell/2. Equations (B10.8)–(B10.10)
therefore prove

\[
 \boxed{\mathcal Q_{Z,B}
 \le C\mathcal L^3\{U^{-1/9}+U^{37/180}/\ell\}.}
 \tag{B10.11}
\]

The residue-square cost O(A²U^(-3/2)) is smaller than the first term.
The coefficient diagonal is ≤CA²ℒ, since w_n²=a(n)²/n. Combining
this with nonnegativity of Q and (B10.1) gives an actual signed joint
estimate for all the high-arm shifts together:

\[
 \boxed{|\operatorname{Re}\mathcal S_{Z,B}|
 \le C\mathcal L^3\{U^{-1/9}+U^{37/180}/\ell\}.}
 \tag{B10.12}
\]

This preserves the joint canonical arithmetic before estimation. It
does not bound |S_N| or the imaginary part of each one-sided block.
At ell=U^(17/81+ρ), the growing term in (B10.12) is
O(ℒ³U^(-7/1620-ρ)), an explicit power gain on the actual consumed sum.

## 4. Lower modes: retain the sharper weights in the B08 estimate

The high-arm estimate alone would be too weak if started at Y. Split
the frozen tail exactly at Z:
D_(Y,B)=D_(Y,Z)+D_(Z,B). The inequality |x+y|²≤2|x|²+2|y|² pays
all cross terms between these two parts by a fixed factor. There are
no missing cross-block pairs in the resulting norm bound.

For Y<m<n≤Z use B08's proved phase-class estimate (B08.9), including
its N²/(Uh) remainder. Its amplitude argument improves, using the exact
decreasing coefficients instead of n^(-5/8), to

\[
 \sup|a_h|+\operatorname{TV}(a_h)
 \le C_A N^{-3/2}e^{(\log N)^2/(2L)}(1+\ell h/N)^{-A}.
 \tag{B10.13}
\]

This follows exactly as B07 (B07.15): weight derivatives are O(w/x),
and one extra Fourier power pays the derivative of its argument.
The interval endpoints and the n≤Z restriction remain included.
For 1≤h≤δ0N, summing the main phase bound over h gives

\[
 CU^{2/7}N^{-3/14}e^{(\log N)^2/(2L)}\ell^{-9/7}.
 \tag{B10.14}
\]

Put α=(log N)/(log U). For Y/2≤N≤Z, α lies in
[1/10+O(1/log U),1/3]. The logarithm of the N-dependent factor,
divided by log U, is

\[
 p(\alpha)=-3\alpha/14+\alpha^2/2+O(1/\log U).
\]

This quadratic is convex, so its maximum is at an endpoint. The exact
endpoint check, including the outer 2/7, is

\[
 2/7+p(1/3)=17/63,\quad
 2/7+p(1/10)=377/1400,\quad
 17/63-377/1400=1/1800>0,
 \tag{B10.15}
\]

where p in this display means its exact quadratic part. The O(1)
in the logarithm gives a fixed multiplicative constant. Counting
O(ℒ) dyadic blocks gives CU^(17/63)ell^(-9/7)ℒ.
The original B08 weight envelope still pays the extra phase term by
CU^(-5/8)ℒ, a conservative bound here. The full population with
h>δ0N and the noncomparable pairs costs CU^(3/8)ell^(-4), as before.
No per-shift phase approximation or Fourier tail has been dropped.
The diagonal costs at most 16Y^(-1/4). Hence

\[
 \mathcal Q_{Y,Z}\le C\{Y^{-1/4}
 +\mathcal L U^{17/63}\ell^{-9/7}
 +U^{3/8}\ell^{-4}+U^{-5/8}\mathcal L\}.
 \tag{B10.16}
\]

Combine (B10.11), (B10.16) and the unchanged complete-cutoff freezing
cost O(U^(-5/8)) from B07 (B07.10). For the actual unfrozen arm,

\[
 \int|A-A_Y|^2d\sigma\le A_1=C_{10}(Y^{-1/4}+\mathcal E_{10}),
 \tag{B10.17}
\]
\[
 \mathcal E_{10}=
 \mathcal L U^{17/63}\ell^{-9/7}
 +\mathcal L^3(U^{-1/9}+U^{37/180}/\ell)
 +U^{3/8}\ell^{-4}+U^{-5/8}\mathcal L.
 \tag{B10.18}
\]

The same Q/diagonal argument gives |Re S_(Y,B)| bounded by the
right side of (B10.17) for the frozen tail as well.
For the finite head, the diagonal is bounded and absolute Fourier
decay gives off-diagonal cost O(Y^(11/4)/ell²): every distinct pair
has |log(n/m)|≥1/Y, and (sum_(n≤Y)w_n)²=O(Y^(3/4)). This cost
decays at the parameters (B10.2). Freezing and |A|²≤2|A_Y|²+2|A-A_Y|²
then give, on increasing C10,

\[
 \int|A|^2d\sigma,\ \int|A_Y|^2d\sigma
 \le A_0=C_{10}(1+\mathcal E_{10}).
 \tag{B10.19}
\]

This also verifies the head norm used by the residual ledger; a bound
only for a high block has not been substituted for a complete-arm bound.

## 5. Complete residual ledger and explicit error checks

Use B08 (B08.14) literally, with A0,A1 from (B10.17)–(B10.19):

\[
\begin{split}
 |\mathscr R-\mu_P|\le{}&D_0+s_0+c_0/2
 +8H^2\sqrt{A_0A_1}+4T_M\sqrt{A_0b_0}
 +2T_M^2A_0+2HT_Mb_0\\
 &+C_{\rm clk}H^2(U^{-1/32}+r_*U^{-9/16})
 +(4/\pi)\mu_PU^{-4}.
\end{split}\tag{B10.20}
\]

Here H is the Euler-product bound, not an arithmetic shift size;
T_M≤M^(-1/8)exp(C P^(3/8)), and

\[
\begin{gathered}
 L_0=L_{U-r_*},\quad K_0=\lfloor M\rfloor Y,\quad
 a_0=C_2/(4L_0)+C_0Y^{-1/8}+C_0M^{-1/8},\\
 D_0=2\sqrt{\mu_P}a_0+a_0^2,\quad
 s_0=150000K_0(1+\log K_0)/\ell,\\
 b_0=(\sqrt{\mu_P}+a_0)^2+s_0,\quad
 c_0=8000H^4Y^{3/4}/(\ell L_0),\quad
 H\le\exp(CP^{1/4}).
\end{gathered}
\]

The constants C0≤25, C2≤81(32/e)² and C_clk retain their inherited
meaning. Exact boundary mass and variation, complete field, physical
clock, reflected frequencies and multiplier tails are unchanged.
At ell≥U^(β+ρ), β=17/81, the powers before logarithms and product
factors are as follows.

| Payment | Power bound |
| --- | --- |
| Lower-mode shifted norm square | U^(-9ρ/7) |
| High-mode joint norm square | U^(-7/1620-ρ), plus U^(-1/9) |
| Head tail norm square | U^(-1/40) |
| Their square-root comparisons | U^(-9ρ/14), U^(-7/3240-ρ/2), U^(-1/80) |
| Coefficient head and multiplier tails | U^(-1/80) |
| Same-arm finite head s0 | U^(-4/405-ρ) |
| Reflected finite head c0 before H⁴/L0 | U^(-437/3240-ρ) |
| Large shifts/noncomparable norm square | U^(-301/648-4ρ) |
| Phase remainder and complete-cutoff freezing | O(U^(-5/8)ℒ) |
| Auxiliary head-norm off-diagonal | U^(11/40-2β-2ρ) with 11/40-2β=-469/3240 |
| Clock payment | O(U^(-1/32)+ℒU^(-9/16)) |

In particular 37/180-17/81=-7/1620 and
17/63-(9/7)(17/81)=0. All costs decay for fixed ρ>0. A0 and b0
are bounded after a finite gate. With fixed constants C,C′ enlarged
to cover all these terms, (B10.20) implies

\[
 |\mathscr R-\mu_P|
 \le C(\sqrt{\mu_P}/L+L^{-2})
 +G(P)\mathcal L^{C'}
   \{U^{-7/3240}+U^{-9\rho/14}\},\qquad
 G(P)=C\exp(C(P^{1/4}+P^{3/8})).
 \tag{B10.21}
\]

Use the single finite subpower gate

\[
 \log(G(L^2)\mathcal L^{C'})
 \le\tfrac12\min(7/3240,9\rho/14)\log U.
 \tag{B10.22}
\]

This proves (B10.3) for ell≤sqrt U. For sqrt U≤ell≤U, B08 with
its fixed parameter ρ8=19/72 supplies its stronger power cap 1/144.
The same block-constant P is used on both ranges.

For the exact acceptance test in Note28 take δ=1/144 and
ell=U^(11/48)=U^(17/72-δ). This is covered with ρ=25/1296.
B08's leading allowance grows as U^(1/112); the new lower-mode and
high-mode terms instead decay, before logarithms, as U^(-25/1008)
and U^(-17/720). Thus this pass meets the stipulated strict
0<δ<1/72 test, in addition to giving the wider range (B10.3).

Retain every B07/B08 field and chart onset, together with L0≥16,
r*≤ell, U-2sqrt U≥U/2, 2≤Y<Z<B, Y≤N_(U-2sqrt U),
1/4≤ν′≤1/2 and T1(P)≤L². The reflected gates remain

\[
 2\log Y+3\log M\le(7/8)L_0,
\]
\[
 \frac\pi{8(U-r_*)^2}(L_0^{-2}+2L_0^{-3})
       (2\log Y+3\log M)\le1/(12U).
\]

Their frequency exponent is now 1/2<7/8. The new source ε_src,
θ, q and the inherited exponent-pair Q, ε, δ0 are fixed. Add the
finite source onset, the support/derivative gates in Section 3 and
the boundedness gates for E10,A0,b0 before (B10.22). Monotonicity in
P allows replacement by L² in all product gates. None of this supplies
a numerical value for the common onset.

Finally μ_P≤2P^(-1/2) and the unchanged E06 transfer
J≤δ/4+R_P/(2δ²)+C/L, with δ=L^(-1/3), give the asserted Green
mean. A fixed small δ and Markov give the exceptional proportion.
No new sign assertion or threshold-zero exclusion enters this step.

## 6. Why the omitted direct-theorem case was not needed

The source lead in Note28 has an earlier restriction than its printed
shift gates. In the unmodified Bourgain–Watt Section 7 setup, denote
the internal subdivision parameter by N_BW to avoid our coefficient N.
Equations (7.3), (7.5) imply

\[
 N_{\rm BW}R^2\ll M_{\rm BW}^3/T,\qquad
 H/N_{\rm BW}\le B_1,\qquad H/R^2\le B_1,
\]
\[
 \frac{TH^2}{M_{\rm BW}^3}\ll1.
 \tag{B10.23}
\]

For the dominant arithmetic scale M_BW≈sqrt T and H≈M_BW/ell,
the left side is comparable to U^(1/2)/ell². At the old B08 endpoint
it grows as U^(1/36), and below that endpoint it grows faster. Thus
relaxing only the later upper-shift restrictions, or adding the omitted
second-spacing case while retaining (7.3), (7.5), cannot cover this
population. This is a scoped failure of that unchanged internal setup,
not an obstruction to other implementations of the method.

The Mellin argument avoids this restriction by importing the completed
cumulative theorem and proving the actual cutoff-arm transfer separately.
In particular it does not cite a remark as a theorem, freely recenter a
shift, or pretend that a positive Hessian determinant prevents resonance.

## 7. Collision controls, retained limitations and continuation

The generic Mellin/mean-square inequality is not claimed to distinguish
theta from every control. Its canonical application needs the exact
unchanged arm coefficients and their Dirichlet identification. The
[control catalog][controls] has the following premise failures here.

| Control class | Premise not retained in this application |
| --- | --- |
| Euler-factor/translated sources and earlier heat counter-kernels | Unchanged theta source, completion and the exact ζ coefficient/arm identity in (B10.9). |
| Weighted finite-square, finite-tail and finite-prime-orbit controls | Complete unchanged coefficients and full reflection beyond retained finite data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical integer-square/Dirichlet arithmetic identifying this arm with ζ. |
| Atomic, exact finite-profile and compact continuous controls | Full theta profile/coefficients, rather than finitely many matched observations. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic of unmodified theta. |
| Fixed-amplitude variable-kernel controls | Actual cosine oscillator and Newman operator. |
| Relaxed positive-measure profiles | Actual integer zero configuration identified with the physical field. |
| RSCT calibrated multiplicative models | Actual common height trajectory and complete Green-window law. |

The four-family comparison and reflection rigidity retain their
conjunction/domain qualifications. A modified field might satisfy an
analogous averaged inequality; this is not claimed to exclude its
collision. No control witness is moved into this shrinking-time band.
The physical controls were screened analytically against the premises;
they were not rerun numerically. B09's quadratic screen fails the
canonical log-ratio/ζ identification, and its actual resonance examples
are allowed by the present proof.

The tail estimate and its consumer give a shorter averaged range, not
small Green value at every center. The permitted total Green mass
O(ell L^(-1/3)) still grows. No sufficient maximal estimate or
moving-time persistence-versus-mass inequality has been proved.
The c=1, fixed geometry, block-constant cutoff, unevaluated onset and
untreated bounded-height restrictions remain. Full-c, varying-cutoff,
shrinking-depth, time-zero and positive-threshold claims remain open.

[Review15][review] is same-assistant checking of this derivation, the
kernel tail, source scope and consumer ledger. The [small exact record][record]
checks rational bookkeeping and documents; it is not a numerical proof
of the analytic estimates. [Note30][return] provides model-change and
continuation guidance. No manuscript snapshot or height campaign was made.

[b07]: 23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md
[b08]: 25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md
[bw]: https://arxiv.org/pdf/1505.04161v1
[source]: ../references/02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md
[review]: ../reviews/15_GNP_RS_B10_SAME_ASSISTANT_ASSESSMENT_20261112.md
[record]: ../numerics/17_GNP_RS_B10_INPUTS_AND_CHECKS_20261112.json
[return]: 30_GNP_RS_B10_RETURN_AND_MODEL_CHANGE_20261112.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
