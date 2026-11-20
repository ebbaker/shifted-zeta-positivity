# AGC-E16 r1: fixed three-prime ellipse allowance obstruction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit execution-helper dispatch:
**gpt-6.1-sol, reasoning effort ultra**; independent serving-backend
attestation is unavailable. **Type E**, under B04's
[frozen r1 request](../research-progress/handoffs/AGC-E16-r1-request.md).
One analytical proof pass and one bounded correction pass. The only
mathematical execution is the eight fixed exact-rational checks recorded
in [Record08](../numerics/08_AGC_E16_RATIONAL_WITNESS_20261119.json);
there is no transcendental evaluation, phase sample or numerical campaign.

**Status: proved in-note; separate nonauthor assessment pending.** On

\[
\mathcal F_0:\quad t=\frac1{10},\quad y=\frac15,\quad
x_0=14000+\sqrt{24/25}\le x\le30000,
\]

the prescribed signed arithmetic lower function and its complete
allowance satisfy

\[
\boxed{\ell_E<-\frac1{400},\qquad m_E=\ell_E-v<-\frac1{400}.}
\tag{1}
\]

This is an upper bound on this **lower allowance**, not an upper bound
on the actual reference or field magnitude. The fixed three-prime
multiplier with individual paired-ellipse radii and separate
kappa/correction/source payments cannot certify the whole required
closed final strip. No theta zero, new coverage, Newman bound,
cost advantage, or universal arithmetic obstruction is established.

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns live status. Read the
[result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md),
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: a quantitative failure theorem for one specified
information reduction, judged by (1), not a reformulated positivity
criterion. The [r0 preflight](../research-progress/handoffs/AGC-E16-r0-preflight-return.md)
supplied the fixed rational witness before B04 froze this segment and
correlated estimating class.

Inputs are Notes10–11 and13–16, Review07 and manuscript Sections5/10.
All four prerequisite hashes in the issued request were checked and
match. Selected primary passages in
[Polymath v2](https://arxiv.org/html/1904.12438v2) were reopened:
definitions(9)–(22), Corollary6.4/(68)–(73), Section8.5/Lemma8.5,
Proposition9.1 and Theorem1.2. The source's t=.2 numerical bounds are
not used at t=.1. The ellipse modulus proof below is supplied directly;
no distance-to-ray or argument-principle conclusion is imported. The
source's (79) is a heuristic, not a multiplicative identity. This is
selected-passage checking, not a full source audit or specialist review.

## 1. Exact normalized reference and complete physical source budget

All logarithms and carriers are those of manuscript Section5. Put

\[
s_0=\frac{1+y-ix}{2},\qquad s_1=\frac{1-y+ix}{2},\qquad
\alpha(w)=\frac1{2w}+\frac1{w-1}+\frac12\operatorname{Log}\frac w{2\pi},
\]

\[
\mathfrak M_t(w)=\mathfrak M_0(w)e^{t\alpha(w)^2/4},\qquad
\mathcal B=\mathfrak M_t(s_0),\qquad
s=s_0+\frac t2\alpha(s_0)=\sigma+i\tau,
\]

\[
\gamma=\frac{\mathfrak M_t(s_1)}{\mathfrak M_t(s_0)},\quad
g=|\gamma|,\quad
\kappa=\frac t2\{\alpha(s_1)-\overline{\alpha(s_0)}\},\quad
b_n=e^{\log^2n/40},\quad
N=\left\lfloor\sqrt{\frac{x}{4\pi}+\frac1{160}}\right\rfloor.
\tag{2}
\]

The manuscript's `s_-(z)` is `s0` here; the primary source uses a
different plus/minus naming convention. Both carriers are nonzero
because their arguments avoid the fixed logarithmic cut.

Expanding the square in each actual term

\[
p_n(t,w)=\mathfrak M_t(w)b_n n^{-w-(t/2)\alpha(w)}
\]

and observing

\[
s_1+\frac t2\alpha(s_1)=\overline s-y+\kappa
\]

give the **exact finite reference** identity

\[
f:=\frac{P_N}{\mathcal B}
=\sum_{n\le N}b_n n^{-s}
 +\gamma\sum_{n\le N}b_n n^{y-\overline s-\kappa}.
\tag{3}
\]

Keep Note14's real-profile correction, with

\[
W=x/2+\pi/80,\qquad
J_N=(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-\pi z/8-\pi^2/640},
\quad C_{\rm val,N}=J_N A_N(W),
\]

\[
c=\frac{C_{\rm val,N}}{\mathcal B},\qquad
q=\frac{Q_{\rm val,N}}{\mathcal B}=f-c.
\tag{4}
\]

Here `A_N` is exactly Note14(1)–(2); this is its value formula, with
no spatial differentiation. The whole retained physical budget is

\[
v=\frac{V_{\rm val,N}}{|\mathcal B|},\qquad
V_{\rm val,N}=\sum_{n=1}^N\sum_{\nu\in\{-,+\}}
 |p_n(t,w_\nu)|\epsilon_n(t,w_\nu)
 +L_N(\delta_{\sigma_-}+\delta_{\sigma_+}),
\tag{5}
\]

where `T0=x/2`, `sigma_±=(1±y)/2`, `w_±=sigma_±+iT0`,
`a_RS=sqrt(W/(2pi))`, and

\[
\epsilon_n(t,w)=\exp\left(
\frac{(t^2/8)|\alpha(w)-\log n|^2+t/4+1/6}{T_0-3.33}
\right)-1,
\]

\[
\delta_\sigma=\left(\frac{0.397\,9^\sigma}{a_{\rm RS}-0.865}
                   +\frac5{3(T_0-6)}\right)e^{3.49/(T_0-4)},\qquad
L_N=\frac{|J_N|}{2}\sqrt W\sqrt{W^2+1}.
\tag{6}
\]

Thus both complete finite-term replacement sums and both entire delta
payments remain. The accepted carrier-phase identity and retained
Corollary6.4 prove

\[
\left|\frac{H_t}{\mathcal B}-q\right|\le v.
\tag{7}
\]

No `+L_N` omitted-correction payment is added to (5), and no part of
the retained remainder is removed. `|c|` below is a separate arithmetic
triangle loss for the actual retained reference, not a switch back to
the old reference or its error budget. All quantities in (5) are
nonnegative and finite on the fixed segment; in fact `v>0`.

## 2. Kappa replacement, finite convolution and exact phase coupling

Define

\[
S=\sum_{n\le N}b_n n^{-s},\qquad
T=\sum_{n\le N}b_n n^{y-s},\qquad F=S+\gamma\overline T.
\]

The elementary exponential-series inequality

\[
|e^{-\kappa\log n}-1|\le e^{|\kappa|\log n}-1
\]

and (3) give the complete arithmetic replacement payment

\[
|f-F|\le D_\kappa,
\qquad
D_\kappa=g\sum_{n\le N}b_n n^{y-\sigma}
                       (e^{|\kappa|\log n}-1)\ge0.
\tag{8}
\]

This is distinct from the physical error (5). A source bound for
`|kappa|`, if used, only enlarges this nonnegative payment.

Fix exactly

\[
E=\prod_{p\in\{2,3,5\}}(1-b_p p^{-s})
 =\sum_{d\mid30}\lambda_d d^{-s},\qquad
\lambda_d=\prod_{p\mid d}(-b_p),\quad\lambda_1=1.
\]

For `1<=m<=30N` set the real coefficients

\[
\beta_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}
                  \lambda_d b_{m/d},\qquad
a_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}
                  \lambda_d(m/d)^y b_{m/d}.
\tag{9}
\]

Multiplicativity of the **phase and exponent** `(dn)^(-s)=d^(-s)n^(-s)`
proves the exact finite convolutions

\[
U=ES=\sum_{m\le30N}\beta_m m^{-s},\qquad
V=ET=\sum_{m\le30N}a_m m^{-s},\qquad\beta_1=a_1=1.
\tag{10}
\]

The indicator in (9) includes every edge term with `m>N` correctly.
Heat weights are not treated as multiplicative: generally
`b_(dn)!=b_d b_n`. The coefficients at `2,3,5` cancel in `U`,
whereas the corresponding `a_p` need not vanish.

Wherever `E!=0`, set

\[
\rho=\gamma\frac E{\overline E},\qquad |\rho|=g.
\]

Then the second branch retains its exact conjugate coupling:

\[
EF=U+\rho\overline V.
\tag{11}
\]

This equality uses `conjugate(V)=conjugate(E) conjugate(T)` and does
not replace the actual gamma phase by an independent physical phase.

## 3. Direct modulus proof for the paired-ellipse lower bound

Assume `0<=g<1` and write `rho=g exp(i theta)`; the case `g=0`
allows any theta. Rotate (11) by `exp(-i theta/2)`. With
`phi_m=tau log(m)+theta/2`, its m-th pair is

\[
m^{-\sigma}\{\beta_m e^{-i\phi_m}+g a_m e^{i\phi_m}\}
=m^{-\sigma}\{(\beta_m+ga_m)\cos\phi_m
              -i(\beta_m-ga_m)\sin\phi_m\}.
\tag{12}
\]

Use the genuine norm

\[
\|w\|_g=\sqrt{\left(\frac{\Re w}{1+g}\right)^2
                  +\left(\frac{\Im w}{1-g}\right)^2}.
\]

It obeys `|w|>=(1-g)||w||_g`. Because `beta_1=a_1=1`, the
constant pair has norm exactly1 for every theta. Every other pair has
norm at most

\[
\frac{h_m}{1-g}\,m^{-\sigma},\qquad
h_m=\max\left(|\beta_m-ga_m|,
               \frac{1-g}{1+g}|\beta_m+ga_m|\right).
\tag{13}
\]

This follows by squaring (12), dividing its real and imaginary axes
by `1+g` and `1-g`, and using `cos²(phi)+sin²(phi)=1`.
The reverse triangle inequality in this norm gives

\[
|EF|\ge(1-g)\|e^{-i\theta/2}EF\|_g
\ge K,\qquad
K=(1-g)-\sum_{m=2}^{30N}h_m m^{-\sigma}.
\tag{14}
\]

Both inequalities remain true when `K<0`; no positivity assumption
was used. Equations(8) and (14), followed by the ordinary triangle
payment for (4), prove the requested signed lower function

\[
\boxed{\ell_E=\frac K{|E|}-D_\kappa-|c|\le |q|,
\qquad m_E=\ell_E-v\le|H_t/\mathcal B|.}
\tag{15}
\]

The denominator is the **actual positive** `|E|`. Replacing it by an
upper bound in this signed lower-bound definition when `K<0` would
reverse the intended inference and is not done.

The retained information consists of equal-frequency convolution,
actual multiplicative phase identities, and the common phase of each
paired branch at a fixed m. Taking individual radii in (13)–(14)
discards the cross-index constraints

\[
\phi_m-\phi_n=\tau\log(m/n),\qquad
\phi_{mn}=\phi_m+\phi_n-\theta/2
\]

where the indices occur, as well as the physical relation of theta
to gamma and E. The separate payments discard the correction's
orientation and its correlations with the sums, kappa and physical
remainder. No claim is made that all these individual worst phases can
occur simultaneously at any actual height.

## 4. Uniform analytic constants on the whole fixed segment

Throughout `F0`, `T0=x/2>7000` and

\[
\frac{x}{4\pi}>\frac{14000\cdot7}{88}>1000.
\]

Using `pi<22/7` gives

\[
\frac{x}{4\pi}+\frac1{160}>33^2,\qquad N\ge33.
\tag{16}
\]

Substitution of `s0=3/5-iT0` into (2) gives

\[
\begin{split}
\Re\alpha(s_0)-\frac12\log\frac{T_0}{2\pi}
={}&\frac{3/10}{T_0^2+9/25}-\frac{2/5}{T_0^2+4/25}
 +\frac14\log\left(1+\frac9{25T_0^2}\right)\\
\le{}&\frac{39/100}{T_0^2}-\frac{2/5}{T_0^2+4/25}<0.
\end{split}
\tag{17}
\]

The first inequality uses `log(1+u)<=u`; the last is equivalent to
`T0²>156/25`, which holds. Since `pi>3`, `x<=30000` and

\[
2500<(8/3)^8<e^8
\quad\left(2500\cdot6561=16402500<16777216=8^8\right),
\]

we have `x/(4pi)<e^8`. Therefore

\[
\sigma=\frac35+\frac1{20}\Re\alpha(s_0)
<\frac35+\frac1{40}\log\frac{x}{4\pi}<\frac45.
\tag{18}
\]

For the lower bound, the positive rational term and positive
logarithmic correction in the first line of (17) may be dropped:

\[
\Re\alpha(s_0)>
\frac12\log\frac{T_0}{2\pi}-\frac{2}{5T_0^2}>0,
\tag{19}
\]

because `T0/(2pi)>1000>e`, so its logarithm is greater than1.
Thus `3/5<sigma<4/5`.

The source's exact bound(20), applied at `y=1/5`, gives

\[
0<g\le e^{1/250}\left(\frac{x}{4\pi}\right)^{-1/10}.
\]

For `0<u<1`, the positive series gives `e^u<=1/(1-u)`. Hence

\[
e^{1/250}\le\frac{250}{249}<\frac{21}{20}.
\]

Also `(7/4)^5=16807/1024<17`, whose square is below1000, so
`1000^(1/10)>7/4`. Consequently

\[
\boxed{0<g<\frac{21}{20}\frac47=\frac35.}
\tag{20}
\]

The strict positivity follows from the two nonvanishing carriers.
For `p=2,3,5`, `log p<2`, since `e>8/3` implies `e²>5`. By (19),

\[
0<b_p p^{-\sigma}=p^{\log p/40-\sigma}<1.
\]

Each factor of E is nonzero and has modulus less than2. Therefore

\[
\boxed{0<|E|<8.}
\tag{21}
\]

All endpoint inequalities in (16)–(21) are strict on the closed
segment, using only exact rational comparisons and the source bound
for g; no sampled carrier or alpha value enters.

## 5. Exact eight-prime witness and the negative complete allowance

For each

\[
p\in\mathcal P_*:=\{7,11,13,17,19,23,29,31\},
\]

we have `p<=N` and `gcd(p,30)=1`. Thus (9) gives

\[
\beta_p=b_p>0,\qquad a_p=p^{1/5}b_p\ge b_p,
\qquad h_p\ge\frac{1-g}{1+g}(b_p+g p^{1/5}b_p)
             \ge(1-g)b_p.
\tag{22}
\]

There are no other d-terms at these primes. To bound their mass
without computing logarithms or exponentials, let
`P_j(u)=sum_(h=0)^j u^h/h!` and use these fixed rational rows:

| p | r | v | k | j |
| --- | --- | --- | --- | --- |
| 7 | 19/10 | 47/100 | 228 | 1 |
| 11 | 23/10 | 59/100 | 163 | 2 |
| 13 | 5/2 | 13/20 | 147 | 2 |
| 17 | 14/5 | 3/4 | 124 | 1 |
| 19 | 29/10 | 79/100 | 115 | 1 |
| 23 | 31/10 | 43/50 | 102 | 3 |
| 29 | 33/10 | 93/100 | 87 | 2 |
| 31 | 17/5 | 193/200 | 84 | 2 |

First `P6(1)=1957/720`. The remaining series is strictly below
`(1/7!)/(1-1/8)=1/4410`, since its later term ratios are strictly
below1/8. Hence

\[
e<\frac{1957}{720}+\frac1{4410}<\frac{68}{25}.
\tag{23}
\]

For each row set `a=ceil(r)`. Direct rational substitution verifies

\[
\frac{(68/25)^a}{P_j(a-r)}<p,\qquad
\frac r5+\frac{r^2}{40}>v,\qquad
\frac{P_4(v)}p>\frac{k}{1000}.
\tag{24}
\]

For example, the first upper fraction is `46240/6875<7`; the
other seven are respectively

\[
\frac{2515456}{243125}<11,\quad
\frac{2515456}{203125}<13,\quad
\frac{1572160}{93750}<17,\quad
\frac{3144320}{171875}<19,\quad
\frac{42762752000}{1895703125}<23,\quad
\frac{4276275200}{151953125}<29,\quad
\frac{1069068800}{34765625}<31.
\tag{25}
\]

Equivalently one can use (24) directly. Record08 preserves each
positive exact gap in (24), expressed as a rational fraction, and
checks the fixed auxiliary rational inequalities used above. It
does not evaluate any transcendental function or import.

From (23) and `e^(a-r)>=P_j(a-r)`, (24) gives
`e^r<(68/25)^a/P_j(a-r)<p`, so `log p>r`. Therefore

\[
\begin{split}
b_p p^{-4/5}
&=\frac1p\exp\left(\frac{\log p}{5}+\frac{\log^2p}{40}\right)
 >\frac1p P_4(v)>\frac{k}{1000}.
\end{split}
\]

Adding the eight strict inequalities yields exactly

\[
\boxed{\sum_{p\in\mathcal P_*}b_p p^{-4/5}
 >\frac{228+163+147+124+115+102+87+84}{1000}
 =\frac{21}{20}.}
\tag{26}
\]

Since `sigma<4/5`, (22) and (26) imply

\[
\sum_{m=2}^{30N}h_m m^{-\sigma}
\ge\sum_{p\in\mathcal P_*}h_p p^{-\sigma}
>(1-g)\frac{21}{20},
\]

\[
\boxed{K<-\frac{1-g}{20}<-\frac1{50}.}
\tag{27}
\]

All unlisted coefficients have nonnegative radius costs, so omitting
them here only weakens this upper bound on K. This is not a
lower bound obtained by discarding a contribution to the physical
sum. In particular the witness is present at the actual included
endpoint, rather than at a surrogate or freely selected phase.

Keep the exact denominator in (15). From (21) and (27), **upper
bounding this already defined negative allowance** gives

\[
\frac K{|E|}<-\frac1{50|E|}<-\frac1{400},\qquad
\ell_E=\frac K{|E|}-D_\kappa-|c|<-\frac1{400},
\qquad m_E=\ell_E-v<-\frac1{400}.
\tag{28}
\]

The sign and exact normalization are preserved. The nonnegative
version `max(0,ell_E)` is identically0 on `F0` and cannot exceed
the nonnegative complete error strictly. The quantities `|q|` and
`|H_t/B|` themselves remain nonnegative and are not bounded above
by (28).

## 6. Equally informed direct comparator

Give direct retained-value evaluation the identical coefficients,
actual height phases, gamma, kappa, finite multiplier, c and full v.
Its complete exact-reference allowance is

\[
m_{\rm dir}=|f-c|-v=|q|-v.
\]

Equation(15) proves

\[
\boxed{m_{\rm dir}\ge m_E.}
\tag{29}
\]

Direct evaluation can itself use (9)–(15). This comparison does not
assert `m_dir<=0`, a runtime ordering or domination over every
interval/grouped implementation. A stronger joint phase estimate,
or a joint correction/remainder estimate, can preserve information
discarded by this estimator. Neither is evaluated or excluded here.

## 7. Cutoff seams, finite/tail coverage and separate criterion inputs

Every natural chart in `F0` has `N>=33`. At

\[
x_j=4\pi j^2-\pi/40,
\]

the new index j owns the endpoint and the old index is `j-1`.
An old one-sided endpoint in this segment also has index at least33.
Formulas(9)–(15) apply independently to both fixed finite sums,
including all edge terms. The eight primes remain present on both
sides, so (26)–(28) hold with either one-sided convention. The old
complete source budget at its excluded endpoint is the continuous
limit from its natural cell, as established in Note14. There is no
floor differentiation or globally holomorphic patchwork assumption.

For a fixed-reference transfer, keep Note14's exact signed jump

\[
\Delta Q_{\rm val}=d_j-2J_j A_j(W),\qquad
d_j=p_j(t,s_+(z))+p_j(t,s_-(z)),
\tag{30}
\]

and the error identity
`E_src,new=E_src,old-Delta Q_val`. Its full triangle payment is
`|Delta Q_val|<=V_val,old+V_val,new`; retaining the exact jump jointly
is also allowed. Crossing several seams requires the successive full
transfers. This pointwise proof uses natural charts directly and
does not invoke an unpaid transfer.

A future successful final-strip proof must cover

\[
x\ge x_0,\qquad\frac15\le y\le\sqrt{4/5},\qquad t=\frac1{10},
\]

by a finite-height region and an infinite tail with an effective
`X_tail` and a paid overlap or common included endpoint. Its finite
proof must cover every y in that interval. An explicit usable
`X_tail` and the required complete error comparison at the join are
**unacquired** here. Classical eventual two-carrier coverage from
Proposition9.1/Theorem1.5 is pre-existing and is not counted as new.
No separate tail calculation or finite scan is performed.

Changing only the join label cannot change the negative value of
this allowance at `x=x0,y=1/5`. Assigning that point to a different
successful estimate would require that additional proved estimate;
it would not repair the tested formula. This does not exclude a
hybrid proof using other information on the failing segment.

Theorem1.2's initial zeta verification and its complete intermediate
barrier for `0<=t<=1/10` remain separate unacquired inputs. The earlier
finite-circle pair certificate and all four pinned prerequisites are
unchanged. No formal `.12` parameter implication is promoted to a
Newman bound.

## 8. Collision controls and the precise excluded class

Separate three premises: the complete literal theta reference/source
enclosure; the stated finite convolution and phase identities; and
a strict complete floor. The following screen uses Controls12 and
Note16's existing routing, preserving the original controls' scopes.

| Control | Source/convolution premise not supplied; strict-floor test |
| --- | --- |
| Euler-factor translates | Changed ordinary coefficients and source error do not inherit the literal theta enclosure. Their own included zero defeats a strict floor with their own honest budget. |
| Weighted-square and finite-source controls | All theta weights and full normalized reflection are absent. The documented finite-source class has no all-real heat anchor; its certified events are not finite Newman thresholds. |
| Finite-prime orbit and finite-score controls | Fixed selected-prime identities or finite rows can survive, including some algebra used in convolution, but do not supply the complete theta coefficients/reflection/remainder. Keep each construction's own event and location qualifiers; no common fixed event location is assigned to the class. |
| Reflected super-Gaussian; smooth shape and positive-primitive controls | Reflection, source/Gram positivity or positive primitive data fail to supply the exact theta arithmetic sums and complete source enclosure. Any included zero still defeats the strict floor. |
| Atomic fixed-event and finite-profile threshold controls | Finitely preserved profile data do not give full theta arithmetic/profile growth or eventual simplicity at their threshold. No rejection on every unrelated collision-free box is asserted. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic fails. Preserve the RH hypothesis and escaping-height scope; a time-zero real double is not this final-strip event. |
| Fixed theta amplitude with changed observation kernel | Literal cosine/Newman readout fails if its prepared forcing is omitted. Such observations are not physical theta collision examples. |
| Fractional relaxed profiles; static divisor surgery | Integer physical multiplicity and a common physical heat path, respectively, fail; neither supplies a physical zero of theta. |
| Reflection rigidity | The full normalized conjunction identifies theta within its stated class; it gives no new quantitative floor. |

Failure of a literal source premise is not a claim that every derived
coarse inequality fails for that control. Quantitatively, with any
honest complete enclosure and nonzero normalizer,

\[
H_*(z_*)=0,\quad |H_*-Q_*|\le V_*,\quad
\ell_*\le |Q_*/B_*|
\quad\Longrightarrow\quad
\ell_*-V_*/|B_*|\le0.
\tag{31}
\]

This holds even for zero source error. For the exact local heat control

\[
H_*=Q_*=(z-x_c)^2-2(t-1/4),\qquad B_*=1,\qquad V_*=0,
\]

at `t=1/10`, the point `z=x_c+i sqrt(3/10)` is an actual zero.
Since `1/25<3/10<4/5`, it lies inside the actual final-strip vertical
range for every `x_c>=x0`. The control obeys `H_t=-H_zz` and has its
double merger at `t=1/4`. Its strict complete floor fails at this
included zero. It does not satisfy the theta arithmetic or claim the
finite-multiplier premises.

**Exact scope:** fixed `{2,3,5}`, anchor coefficient1, individual
paired-ellipse radii, and separately paid kappa, retained correction
and complete source errors, on the specified segment. Larger or
adaptive products, signed coefficient groups, actual-height phase
constraints, correlated correction/remainder estimates, contour
arguments and all arithmetic methods are outside this exclusion.

## 9. Correction pass and disposition

The bounded self-check rederived (11)–(15) directly as a modulus
inequality, including a negative K, rather than assuming the source's
distance-to-ray formulation. It checked the t=.1 correction exponent,
all cutoff indicators, both term-error sums, both complete deltas,
the gamma convention, the exact denominator and the one-sided seam
indices. Record08 verifies the eight frozen rational rows and all
fixed auxiliary rational checks used there. No target, source,
mechanism, prime set, domain or completion threshold changed.

**Disposition:** all six E16 r1 proof targets are proved in-note;
acceptance and manuscript-integration assessment belong to the
separate nonauthor reviewer. The failure completes this E task and
opens no numerical campaign. B04's declared next B05 decision remains
a conceptual dependency requiring a distinct quantitative phase input,
not a mechanism selected by this execution. Shared indexes, manuscript,
progress register and public chat recording remain with the root.
