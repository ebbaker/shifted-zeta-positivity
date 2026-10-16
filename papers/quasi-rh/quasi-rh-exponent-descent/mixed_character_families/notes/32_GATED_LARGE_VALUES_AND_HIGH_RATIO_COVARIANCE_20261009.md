# Gated large values and the remaining signed pair covariance

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: new conditional arithmetic sector reduction and an exact sufficient
pair-covariance criterion. The central count and gated inverse-mass saving
remain unproved. Same-model checks are internal validation, not independent
specialist review or formal verification.

**A large gated inverse mass forces a positive signed covariance between
different, well-separated primitive row characters.** At the desired count
threshold, equal-character pairs and all row-ratio conductors
\(Q_{uv}\le U^{8/15}\) are too small to supply that covariance. Their
removal has a uniform conditional reserve greater than \(0.004\), including
the universal physical-slot upper/lower gap and a stated real loss budget.
The remaining object is a two-row large-values covariance with the actual
gate, inverse energy and plain-response phases. It is sufficient to bound
this particular scalar; an arbitrary-coefficient operator bound or the
older three-row open chain is not required by this reduction.

The attempted estimate for the remaining covariance does **not** close.
The supplied entrywise kernel bound misses its necessary normalized scale
by at least \(91/500=0.182\) in the exponent. Even a hypothetical uniform
square-root entrywise bound misses by at least \(4/125=0.032\). These are
failures of the indicated absolute majorants, not lower bounds for the
native covariance. The new reduction does not improve the sharp positive
count envelope of Note 31.

## 1. Source scope and the precise positive target

The inputs inspected locally are the [mixed manuscript](../mixed_character_reductions.tex),
[Note 2](2_SELECTED_INVERSE_DISTRIBUTION_20261008.md),
[Note 3](3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md),
[Note 4](4_CONDUCTOR_NEIGHBOR_SECTORS_20261008.md),
[Note 19](19_SOURCE_SLOT_WITNESS_CERTIFICATE_20261009.md), and
[Notes 30](30_SURVIVING_BLOCK_AND_GATED_COUNT_CHECKPOINT_20261009.md)
and [31](31_GATED_INVERSE_MASS_AND_POSITIVE_MOMENT_LIMIT_20261009.md).
The parent [joint-witness note](../../../quasi-rh-character-amplification/notes/JOINT_WITNESS_REDUCTION_20261008.md)
fixes the common-character and common-height selection. No new external
theorem is used. In particular, this note does not reprove the underlying
family strip/growth estimate, native reciprocity, conductor identification,
masked Poisson formula, detector, or source moment/profile calculus.

Those analytic inputs remain the explicitly conditional source package
checked in the earlier notes against the September 30 source PDF, SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The kernel bound used below is exactly Note 4 (28), with its complete
canceled-ramification masks, rather than a bound inferred from an
unmasked primitive character.

Fix one permitted native presentation, orientation, original physical
slot system, amplitude bin, length pair \((r,m)\), and common separating
parameters. Write \(D=U^r\), \(N=U^m\), \(d=2a-1\), and
\(H=1+T_1\). Retain the actual polynomials

\[
 M_u=D^{-1/2}\sum_{\mathfrak d}\mu_F(\mathfrak d)
  \psi_u(\mathfrak d)A_0(N\mathfrak d/D),\quad
 S_u=N^{-1/2}\sum_{\mathfrak k}\psi_u(\mathfrak k)B(N\mathfrak k/N),
 \quad Z_u=M_uQ_I(u).
 \tag{1}
\]

Every \(Q_I\) is the original product of whole disjoint smooth
prime slots. Its fixed-ray coefficient expansions, physical zeros, norm
twists and selected derivative profiles remain part of (1). The plain
sum is the complete good annulus, including its nonsquarefree columns.
The inverse contains its original Möbius coefficient and truncated cutoff.

Let the actual gate be

\[
 \sigma=(c/C)U^{dm-\tau}H^{-b_M},\qquad
 \tau=\lambda_1+e_M,
 \quad \mathcal G=\{u\in\mathcal C:|S_u|^2\ge\sigma\},
 \quad w_u=1_{\mathcal G}(u)|Z_u|^2,
 \quad J=\sum_u w_u.
 \tag{2}
\]

Thus \(J\) is precisely Note 30's gated inverse mass, not an enlarged
ungated mixed moment. Under Note 31's literal localization budget, every
row in \(\mathcal G\) has
\(\log_U Q_{\psi_u}>2m-1/720000\). This individual-conductor fact
neither bounds nor identifies the conductor of a quotient of two rows.

Write \(R_t=R_{\rm new}\). On a simultaneous witness row the source
product lower bound and plain upper envelope give

\[
 |Z_u|^2\ge c_ZU^{dr+2G_I-L_{\rm wit}},
 \qquad L_{\rm wit}=\lambda_1+\lambda_2+e_S
                      +b_S\log_U H.
 \tag{3}
\]

Fixed constants enter the eventual threshold. The desired mass exponent
for this fixed subdivision is

\[
 j_t=R_t+dr+2G_I-L_{\rm wit}.
 \tag{4}
\]

A bound \(J\ll U^{j_t-\delta}\), with subsequent covering and
height costs below \(\delta\), gives the desired witness count. The
literal costs in (3) cannot be restored after proving a loss-free mass
exponent. We use \(J\ge U^{j_t}\) as the contradiction regime below.
This is a threshold test, not an assertion that actual rows reach it.

## 2. An exact gate-specific large-values identity

Let \(\mathcal K_N\) be the original finite plain column support,
including fixed zero columns if convenient, and let \(L_N=\#\mathcal K_N\).
The original fixed annular support gives \(L_N\ll_{\mathcal P}N\).
Set

\[
 T_{u,k}=N^{-1/2}\psi_u(k)B(Nk/N),\quad T\mathbf1=S,
 \quad K(u,v)=\sum_kT_{u,k}\overline{T_{v,k}}.
 \tag{5}
\]

On the positive gate define \(\epsilon_u=S_u/|S_u|\). Rows with
\(w_u=0\) can be omitted; no value of a character at a nonunit is
divided out. In particular \(\epsilon_u\) divides a nonzero **plain
response**, not an individual character value. The scalar

\[
 \mathcal B=\sum_{u,v}w_uw_v\overline{\epsilon_u}\epsilon_vK(u,v)
 =\sum_k\left|\sum_u w_u\overline{\epsilon_u}T_{u,k}\right|^2\ge0
 \tag{6}
\]

has all gate and bin predicates outside the complete smooth column sum.
Column Cauchy gives

\[
 \left(\sum_u w_u|S_u|\right)^2\le L_N\mathcal B,
 \qquad
 \boxed{\mathcal B\ge\sigma J^2/L_N.}
 \tag{7}
\]

The identity and lower bound need no statistical independence, large
sieve, smoothness of the row gate, or Poisson on a selected row family.
They retain the row phases which an absolute Schur estimate discards.
For \(L_N=0\) the gate is empty, so that degenerate case causes no issue.

There is an exact polynomial-endpoint companion without phase division.
Define \(E_G=\sum_u w_u|S_u|^2\) and

\[
 \mathcal B^{\rm amp}=
 \sum_{u,v}w_uw_v\overline{S_u}S_vK(u,v).
 \tag{8}
\]

Then
\(\mathcal B^{\rm amp}=\sum_k|\sum_uw_u\overline{S_u}T_{u,k}|^2\)
and
\[
 E_G^2\le L_N\mathcal B^{\rm amp},\qquad
 \mathcal B^{\rm amp}\ge\sigma^2J^2/L_N.
 \tag{9}
\]

This is the second positive spectral moment of the actual probe,
whereas Note 3 uses a third moment with three rows and two kernels.
Neither criterion is automatically easier to estimate. Equation (6)
has the advantage that the endpoints have modulus one; (8) has the
advantage that its endpoints are actual polynomial values. All future
signed estimates must state which object they bound.

## 3. Actual primitive fibers and low ratio conductors cannot supply a large tail

The physical rows are sixth-power-free. The source local character formula
therefore gives bounded primitive-character fibers, and Note 4's exact
valuation enumeration gives

\[
 \#\{v:Q_{uv}\le V\}\ll_{\varepsilon,S}V^{1+\varepsilon},
 \qquad
 \sum_{v:Q_{uv}\le V}w_v\ll U^\varepsilon W V,
 \quad W=\max_u w_u.
 \tag{10}
\]

The selector and gate can only reduce these physical counts. Equal
primitive characters are bounded in number, even when their imprimitive
zero masks differ. The conditional kernel inputs are

\[
 |K(u,v)|\ll U^\varepsilon H^{b_K}
 \min\{N^{-1/8},\sqrt{Q_{uv}}/N\}\quad(c(u)\ne c(v)),
 \qquad |K(u,v)|\ll H^{b_0}\quad\hbox{always}.
 \tag{11}
\]

The fixed-ray part and complete deleted Euler factors are retained in
(11). Applying order-zero masked Poisson to the smooth columns in (5)
is legal here; the sharp gate is an outer weight. The primitive conductor
is \(Q_{uv}\), and the extra mask includes every equal positive row
valuation whose character phase cancels.

Partition (6) exactly into equal primitive characters, unequal characters
with \(Q_{uv}\le V\), and unequal characters with \(Q_{uv}>V\).
Call the last part \(\mathcal B_>(V)\). Reversal of a pair gives its
complex conjugate, so all three grouped sums are real. Positivity is
claimed only for their full sum. Equations (10)–(11) imply

\[
 |\mathcal B_{=}|\ll WJ H^{b_0},\qquad
 |\mathcal B_{\le V,\ne}|\ll U^\varepsilon H^{b_K}
                    WJ V^{3/2}/N.
 \tag{12}
\]

This is a genuine native arithmetic count-plus-Poisson deduction. It does
not treat the gated family as a smaller smooth row ball. No changes to
the inverse coefficients or whole prime slots are made.

Use the source universal envelope and the positive-prefix lower gain,

\[
 W\ll U^{dr+dz_I+e_W}H^{b_W},\qquad
 G_I\ge dxz_I,\quad z_I\le(1-r)/2<3/20.
 \tag{13}
\]

Here \(e_W\) includes the actual fixed amplitude-width and inverse
upper costs; the convention \(dz_I\) is not used to erase them. Thus
the universal upper/lower slot gap is at most

\[
 dz_I-2G_I\le d(1-2x)z_I\le\frac{63}{50000}.
 \tag{14}
\]

This works for the original nonflat permitted profile as well as for the
flat limitation profile. A better source bin-specific upper envelope can
improve (14), but is unnecessary for the following removal.

Put \(t_G=\tau+b_M\log_U H\). Collect all real costs in (12)–(13)
relative to (7), including allocated small powers and heights, into

\[
 L_{\rm LV}=L_{\rm wit}+e_W+t_G+\varepsilon_K
                         +(b_W+b_K')\log_UH,
 \tag{15}
\]

where \(b_K'\) is a fixed height power large enough for both branches
of (12); a tiny eventual constant allowance is separate. We assume
\(L_{\rm LV}\le\ell=10^{-6}\). This is a conditional literal
allocation, not a recorded evaluated detector manifest. In the regime
\(J\ge U^{j_t}\), the ratios of (12) to (7)'s lower bound are at most

\[
 U^{(1-d)m-R_t+63/50000+L_{\rm LV}},\qquad
 U^{(3/2)v-R_t-dm+63/50000+L_{\rm LV}},\quad V=U^v,
 \tag{16}
\]

up to fixed constants. This is the important change from a full-chain
sector test: the mass threshold itself pays for the neighbor count.

## 4. A uniform paid cutoff \(V=U^{8/15}\)

The two-rebalance formula is

\[
 a=5/6-d,\quad B_x=2-8x/9,\quad D_x=3-17x/9,\quad
 P_x=B_x(1-x),\quad J_x=aD_x+dP_x,
 \quad F_x=aB_x/J_x,
 \quad R_t=1-d+\frac{adP_x}{2J_x}-F_x\eta,
 \quad\eta=1/5000.
 \tag{17}
\]

On \(9/25\le d\le21/50\), \(49/100\le x\le1/2\), both
\(R_t\) and \(R_t+(2/5)d\) decrease with \(d,x\). Here is a
continuous proof rather than an inference from a grid. Set
\(h=P_x/D_x\), \(H_0=a+dh\), so the positive term in (17) is
\(adh/(2H_0)\). Then

\[
 \partial_d\frac{adh}{2H_0}
 =\frac{h(a^2-d^2h)}{2H_0^2}\le h/2,
 \quad
 \partial_x h=\frac{(10/9)(1-x)-B_xD_x}{D_x^2}<0,
 \quad
 \partial_x\frac{adh}{2H_0}=\frac{a^2d}{2H_0^2}\partial_xh<0.
 \tag{18}
\]

Note 31's differentiated \(F_x\) has \(\partial_xF_x>0\) and
\(|\partial_dF_x|=(5/6)B_x^2(1-x)/J_x^2\). With
\(a\ge31/75\), \(B_x\le352/225\), \(D_x\ge37/18\), and
\(1-x\le51/100\), the upper bound

\[
 -1+\frac12\frac{(352/225)(51/100)}{37/18}
 +\eta\frac{(5/6)(352/225)^2(51/100)}{[(31/75)(37/18)]^2}
 +\frac25<0
 \tag{19}
\]

proves both \(d\)-monotonicities. The \(x\)-monotonicities follow
from (18). Since \(m>2/5\), exact endpoint evaluation gives

\[
 R_t\ge\frac{158126}{248125},\qquad
 R_t+dm>\frac{199811}{248125}.
 \tag{20}
\]

Consequently at \(v=8/15\), before (15)'s costs, the low-pair ratio
in (16) has reserve

\[
 \kappa_{\rm low}=\frac{199811}{248125}-\frac45-\frac{63}{50000}
 =\frac{79869}{19850000}=0.004023627204\ldots.
 \tag{21}
\]

The equal-character reserve is even larger. Using the conservative
\((1-d)m\le(16/25)(207/500)\) gives

\[
 \kappa_=\frac{158126}{248125}
 -(16/25)(207/500)-\frac{63}{50000}
 =\frac{7365613}{19850000}=0.371063627204\ldots.
 \tag{22}
\]

Under \(L_{\rm LV}\le\ell\), the low-pair reserve is
\(1596983/397000000>1/250\). Fix later small powers and heights
strictly within the unused room. At the eventual threshold, (7) and
(12) therefore force the necessary inequality

\[
 \boxed{\Re\mathcal B_>(U^{8/15})
       \ge\frac{\sigma J^2}{2L_N}\qquad(J\ge U^{j_t}).}
 \tag{23}
\]

All pairs in (23) have different inducing primitive characters, primitive
ratio conductor greater than \(U^{8/15}\), and individual conductors
in Note 31's forced gate domain. The stronger individual localization
does not itself give an upper bound for (23).

The reserves (21)–(22) pay this sector removal. They are **not** new
count savings and cannot be spent on unrelated detector coverage or
global boundary losses. In particular they do not remove the central
scalar deficit \(F_x\eta+\ell\) from Note 31.

## 5. The remaining quantitative criterion and the attempted bound

Equation (23) makes the remaining task concrete. A sufficient new estimate,
uniform in the retained bin, parameters and permitted profile families,
is for some fixed \(\delta>0\)

\[
 \boxed{\Re\mathcal B_>(U^{8/15})
 \ll U^{2j_t+(d-1)m-t_G-\delta}H^{b_*}.}
 \tag{24}
\]

The positive mass reserve can be stated explicitly. From (7) and (12),
for an upper bound \(C_B\ge\Re\mathcal B_>(V)\) with \(C_B\ge0\),
solve the resulting quadratic inequality to obtain

\[
 J\ll (L_N C_B/\sigma)^{1/2}
       +U^{\varepsilon_K}H^{b_K'}W(N+V^{3/2})/\sigma.
 \tag{24a}
\]

The elementary implication used here is
\(\alpha J^2\le C_B+\beta J\Rightarrow
J\le\beta/\alpha+\sqrt{C_B/\alpha}\), for \(\alpha>0\).
Under (24), at \(V=U^{8/15}\), (24a) gives the genuine mass saving

\[
 J\ll U^{j_t-\zeta+\varepsilon}H^{b'},\qquad
 0<\zeta<\min\{\delta/2,\kappa_{\rm low}-L_{\rm LV}\},
 \tag{24b}
\]

after allocating the remaining height/small-power costs. One may fix
\(\zeta=\min\{\delta/4,(\kappa_{\rm low}-L_{\rm LV})/4\}\)
to leave strict room. Equivalently, rerun (23)'s contradiction for
\(J\ge U^{j_t-\zeta}\): the low-sector reserve worsens by
\(\zeta\), and the high-covariance exponent margin worsens by
\(2\zeta\). All later covering, smoothing and height costs must fit
the resulting count reserve in (24b). They cannot be paid merely by
the contradiction at \(j_t\). The actual endpoints in (6) are fixed
by \(S_u\); (24) is not requested for arbitrary row phases or arbitrary
coefficient vectors. The one-sided real upper bound is sufficient.

The exact signed form to estimate is

\[
 \sum_{\substack{u,v\in\mathcal C\cap\mathcal G\,,\ c(u)\ne c(v)\\
                   Q_{uv}>U^{8/15}}}
 |M_uQ_I(u)|^2|M_vQ_I(v)|^2
 \frac{\overline{S_u}S_v}{|S_u||S_v|}
 \frac1N\sum_k|B(Nk/N)|^2\psi_u(k)\overline{\psi_v(k)}.
 \tag{25}
\]

All sharp row predicates are displayed, and the full good annulus is
retained in the inner kernel. Apply the criterion in either retained
orientation with its actual coefficient profiles. Simultaneous conjugation
of the characters and all coefficient profiles conjugates the whole
expression and preserves its real part; changing the character orientation
alone need not do so for complex profiles. Individual primitive
character phases canceled in a quotient are still zero extended through
the physical masks. No prime is removed from a slot to simplify (25).

Expanding \(M Q_I\) remains legitimate: it has the exact coefficient
\(X_I^{-1/2}\sum_c A_I(c)\psi_u(c)\), with
\(X_I=D\prod_{i\in I}P_i\), and
\(A_I(c)\) is the full ownership sum over
\(c=\mathfrak d\prod_i\mathfrak p_i\), containing \(\mu_F(\mathfrak d)\),
the inverse annulus, all original slot profiles, and fixed presentation
coefficients. Complete multiplicativity, including zero extension, makes
this exact. It gives four original signed inverse/slot coefficient labels
in (25). It does not turn the gated \(\overline{S_u}/|S_u|\) into
a row-independent coefficient, or justify a sieve theorem for a newly
selected smooth row family.

The straightforward attempt applies (11) after taking absolute values.
It gives only

\[
 |\mathcal B_>|\ll U^\varepsilon H^{b_K}N^{-1/8}J^2.
 \tag{26}
\]

Against the scale \(\sigma J^2/N\) forced by (23), this loses

\[
 (7/8-d)m+t_G\ge(7/8-21/50)(2/5)=91/500.
 \tag{27}
\]

Replacing (11) optimistically by a generic uniform \(N^{-1/2}\)
entry bound still loses
\((1/2-d)m+t_G\ge4/125\). The low-ratio count cannot improve
(26) on the remaining high-ratio domain: a cap only gives an upper bound
for the number of close neighbors, not cancellation among the distant
ones. Cauchy over the original inverse ownership labels likewise forgets
the signs and returns an unrelated positive coefficient norm. No useful
bound for the aggregate (25) was found in these attempts.

For the polynomial companion (8), the sufficient exponent is
\(2j_t+(2d-1)m-2t_G-\delta\); its absolute bound is
\(N^{d-1/8}J^2\) up to the plain upper-envelope cost. It has the
same basic gap (27), with an additional gate/upper cost. This provides
a version without divided response phases, but not an estimate.

Thus the next arithmetic question is sharper than improving a single
Gauss norm: bound the *aggregate* (25), or its polynomial companion,
using the actual common inverse/slot coefficient and response-phase
relations. The prior full-mask Fourier covariance and annular surviving
block remain compatible with this gap. A formal scalar marginal table
does not contain (25)'s native kernel information; conversely, the
existence of (25) does not invalidate that table without a new bound.

## 6. A gate-compatible interface for common parameter and height selection

A bound for (24) at one fixed parameter tuple does not establish the
source's rowwise selection. In particular it is invalid to differentiate
the sharp indicator in (2) or silently invoke Sobolev on (25).
The following elementary smoothing interface shows a legitimate route,
and makes its extra loss explicit.

Choose a fixed smooth \(\eta\) with \(0\le\eta\le1\),
\(\eta(x)=0\) for \(x\le1/2\), and \(\eta(x)=1\) for \(x\ge1\).
Set
\[
 F_u(\lambda)=|Z_u(\lambda)|^2
       \eta(|S_u(\lambda)|^2/\sigma).
 \tag{28}
\]

It dominates the original gated weight and is supported on the gate
\(|S_u|^2>\sigma/2\). That changes only a fixed constant in (2),
not its power width or conductor frontier. Equations (6)–(23) also
hold for these nonnegative smoothly gated weights. The phases remain
well defined on their support.

On a compact parameter box of dimension \(p\), repeated one-dimensional
fundamental theorem of calculus gives
\(\sup F\ll_p\sum_{\alpha\in\{0,1\}^p}\int|\partial^\alpha F|\).
For an internal derivative order \(k\), suppose the existing permitted
plain derivative envelopes are
\(|\partial^\beta S|^2\ll U^{dm+e_{\rm der}}H^{b_{\rm der}}\)
for every \(|\beta|\le k\). Product and chain rules give

\[
 |\partial^\alpha F_u|
 \ll U^{k(\tau+e_{\rm der})+\varepsilon}H^{B_k}
  \sum_{\beta,\mathfrak t}|Z_{\beta,\mathfrak t}(u)|^2
                 1_{|S_u|^2>\sigma/2}.
 \tag{29}
\]

Here \(\mathfrak t\) runs through a fixed finite derivative allocation
among the inverse and the **same whole original slots**. The Leibniz
terms \(Z_{\beta,\mathfrak t}\) are actual products with permitted
derivative profiles; Cauchy only separates their finite cross terms.
Every derivative of the cutoff costs at most one factor with exponent
\(\tau+e_{\rm der}\), because of its \(\sigma^{-1}\) and the
plain derivative envelope. Derivatives of a parameter-dependent
normalization add only prescribed logarithmic/fixed smooth factors on
each fixed dyadic subdivision. All physical zeros remain in (29).

Consequently a new gated estimate for the finite family in (29), uniform
before selection, can support the positive Sobolev procedure. It must
apply to a gate formed from the original \(S\), with derivative inverse
and slot products as weights; a statement only for one unmodified
\(M Q_I\) does not suffice. The smoothing costs
\(k(\tau+e_{\rm der})\) and its fixed height power have to fit the
*count* reserve after (24), separately from the sector reserve (21).
Fix the new theorem's finite internal orders first, then choose the
source real buffers and later height ceiling as in Note 19. This is a
conditional interface, not a proof that the remaining arithmetic theorem
has that derivative scope or a numerical loss manifest.

## 7. Verification and the research decision

The [checker](../../numerics/check_gated_large_values_covariance.py) and
[record](../../numerics/gated_large_values_covariance_record_20261009.json)
give 703,417 assertions. Exact arithmetic in \(\mathbb Z[\zeta_6]\)
checks 216 sixth-power-free valuation vectors at the split rational prime
norms 7, 13, 19; primitive ratio conductor multiplicities; every canceled
positive-valuation zero on the tested columns; and a complete marked
Möbius/plain/two-slot coefficient convolution. Rational arithmetic checks
the gated amplitude covariance identity, its positivity and Cauchy
inequality, the continuous monotonicity bounds, (20)–(22), and both
entrywise deficits. The phase-normalized covariance uses floating square
roots; its maximum observed identity error is \(2.74\cdot10^{-20}\),
below the declared \(2\cdot10^{-10}\) tolerance.

This finite model is a product of genuine finite sextic residue
characters over integer residue fields. Its annular lists and two prime
labels test the coefficient/zero algebra. They are **not** an Eisenstein
ideal detector bin, an original equal-width source slot instantiation,
or a native reciprocity/conductor theorem. No native row population or
asymptotic covariance is synthesized or certified. All files are small,
regenerable sources/records under the repository's `LARGE_FILES.md`
policy; no large derived dataset is retained.

The advance is the threshold-dependent low-ratio removal and the exact
remaining two-row covariance. The attempted aggregate bound fails at
the explicit gaps above. This warrants investigating native signed
covariance/large-values input on (25), with (29)'s selection interface,
but not another interpolation of Note 31's positive constraints.
The full central gated saving, direct witness count, selected mixed
moment, new family boundary, and descent to RH remain unproved.
