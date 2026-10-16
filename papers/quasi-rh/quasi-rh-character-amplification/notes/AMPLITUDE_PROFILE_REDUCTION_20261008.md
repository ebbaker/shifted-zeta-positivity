# Full amplitude profiles and reduction to the remaining saturated class

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

## Status and external dependencies

This is a conditional refinement of the row-count calculation in Section 19
of the September 30 companion paper, not an independent verification of its
moment or detector lemmas. Its inputs are precisely the inverse marked
moment (Lemma 17.1), the amplified inverse moment (Lemma 17.6), the plain
fourth moment (Lemma 18.1), and the common detector (Proposition 8.3), with
the coefficient, zero-extension, common-character, and height requirements
retained as in Proposition 19.2. Fix the permitted value `kappa=3/4` using
the already-assumed seven-eighths boundary. Thus there is no positive-Delta
plain-capacity penalty. Source:
<https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf>,
pages 181–186. The consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

The result below is an actual refinement obtainable from those existing
inputs. It improves nonflat amplitude classes, but gives exactly no gain on
a perfectly saturated profile. It therefore localizes a genuinely new
joint-witness estimate; it does not itself prove an improved global boundary.

## 1. Exact profile and whole-slot selection

Fix a dynamic/amplitude bin and its external physical Mellin parameters.
Write

\[
0<\delta\le3/4,\qquad c=\delta/2,\qquad
w_i=\ell_i/d>0,\quad L=\sum_iw_i=\ell/d,
\quad 0\le g_i\le c,\quad q=L^{-1}\sum_iw_ig_i.
\]

Include zero-amplitude slots, including the declared error slots, in this
weighted list. Arrange the slot amplitudes decreasingly, represent them as
a decreasing step function \(g^*:[0,L]\to[0,c]\), and put

\[
G(z)=\int_0^z g^*(v)\,dv,\qquad
K(z)=G(z)-qz,\qquad 0\le z\le L.
\]

Then \(G\) is nondecreasing, concave, and \(c\)-Lipschitz;
\(G(L)=qL\); and \(K\) is concave with \(K(0)=K(L)=0\), so
\(K\ge0\). This is the fractional knapsack optimum, not a replacement
coefficient class. Its selection consists only of the source's original
physical prime slots.

Let \(\mu=\max_iw_i\). Delete the one possibly fractional slot in the
optimal prefix. Zero-amplitude slots require no lower bound and are not
selected. The remaining whole positive slots have total length at most
\(z\), and their actual squared product satisfies

\[
\left|\prod_{i\in I}Q_i\right|^2
 \ge U^{2G(z)-\delta\mu}.
\]

To meet a strict moment condition first request \((z-\nu)_+\).
The combined loss relative to \(2G(z)\) is at most
\(\delta(\mu+\nu)\), unless no positive capacity is selected, when the
source's unweighted estimate supplies the relevant endpoint bound. These
losses can be made smaller than any prescribed fixed positive exponent by
choosing the finite slot mesh and decrement first. Neither clipping nor
fractional coefficients are inserted into the moment theorem.

## 2. Refined short-witness count

Fix the source detector cutoff \(1\le t\le3/2\). Write the actual inverse
length as \(r\), and use the source relation \(m\ge t-r-O(\epsilon)\)
for the plain length. The two useful capacities are

\[
z_M(r)=\frac{1-r}{2},\qquad
z_P(m)=\frac{2(1-2m)}9.
\]

For the comparison only, extend \(G(z)=G(L)\) when \(z>L\); this means selecting at most the available length and preserves concavity and all stated slope bounds. At the actual crossing and on the selected sides, the capacities below are strictly less than \(L\). In the positive-capacity range define

\[
A_G(r)=1-\delta r-2G((1-r)/2),
\]
\[
S_{G,t}(r)=1-2\delta(t-r)
 -2G\!\left(\frac{2(1-2(t-r))}{9}\right).
\]

These are the actual marked second-moment and plain fourth-moment count
exponents. The latter is decreasing in the actual \(m\), since its slope
lies between \(-2\delta\) and \(-14\delta/9\), so replacing \(m\) by
\(t-r\) is legitimate with the source's preliminary loss.

On \(t-1/2\le r\le1\), the inverse branch is strictly decreasing and
the plain branch strictly increasing. Their almost-everywhere slopes obey

\[
-\delta\le A_G'(r)\le-\delta/2,
\qquad 14\delta/9\le S_{G,t}'(r)\le2\delta.
\]

At the left endpoint the plain exponent is \(1-\delta\), no larger
than the inverse exponent; at the right endpoint the inverse exponent is
\(1-\delta\), no larger than the plain exponent. Hence they have one
crossing \(r_G(t)\), with the common value denoted \(F_G(t)\). For
\(t=3/2\) this is the common endpoint. The short-witness count is
\(U^{F_G(t)+\epsilon}\), because the smaller of these two monotone
branches has its maximum at the crossing.

The needed capacity supply is slightly stronger than in the scalar proof.
The elementary bounds \(0\le G(z)\le\delta z/2\) give

\[
\frac{4t-1}{5}\le r_G(t)\le\frac{14t+2}{23}.
\]

For example, the lower bound follows by comparing
\(A_G\ge1-\delta(1+r)/2\) with
\(S_{G,t}\le1-2\delta(t-r)\); the upper bound uses the opposite
bounds. Thus \(r_G\ge3/5\), \(t-r_G\ge7/23\), and

\[
z_M(r_G)\le1/5,\qquad z_P(t-r_G)\le2/23.
\]

It is enough that \(L>1/5\) by a fixed amount. This holds for the current
geometry and for \(\ell=1/6+1/5000\) at the relevant row scales. On the
inverse-selected side \(r\ge r_G\), the second width condition has a
fixed margin \(2r-1\ge1/5\); the first obtains its fixed margin by the
capacity decrement. This checks the strict hypotheses rather than simply
reusing the earlier \(7/37\) supply threshold. Zero-capacity neighborhoods
and \(m\ge1/2\) use the source's unweighted estimates.

The long inverse branch is unchanged:

\[
L_\delta(t)=1-\delta+(\alpha-\delta)(t-1),\qquad \alpha=5/6.
\]

Therefore the complete count obtained here is

\[
\#\mathcal B\ll U^{\max\{F_G(t),L_\delta(t)\}+\epsilon}
 (1+T_1)^{A},
\]

with the source's fixed finite subdivisions and height bookkeeping. The
power \(A\), thresholds, and constants may depend on the fixed mesh and
other permitted data. The requested exponent loss can be fixed first.

## 3. Quantitative profile gain at the scalar crossing

Set \(x=q/\delta\),

\[
D_x=3-17x/9,\quad
P_x=(2-8x/9)(1-x),\quad b_\delta=\delta P_x/D_x.
\]

For the flat comparison \(G_q(z)=qz\), its crossing and exponent are

\[
r_0(t)=\frac{(2-8x/9)t-5x/9}{D_x},\qquad
F_q(t)=1-\delta+b_\delta(3/2-t).
\]

At that crossing put

\[
k_M=K((1-r_0)/2),\qquad
k_P=K(2(1-2(t-r_0))/9),\qquad H_G(t)=F_q(t)-F_G(t).
\]

Both \(k_M,k_P\) are nonnegative. If \(k_M\ge k_P\), the refined
crossing moves left. The slope bounds above give

\[
H_G(t)\ge\frac{28k_M+18k_P}{23}.
\]

If \(k_P\ge k_M\), it moves right and

\[
H_G(t)\ge\frac{8k_M+2k_P}{5}.
\]

For a proof of the first inequality, let the leftward displacement be
\(v\ge0\). At the new crossing the inverse exponent is at most
\(F_q-2k_M+\delta v\), and the plain exponent is at most
\(F_q-2k_P-14\delta v/9\). Their weighted comparison eliminates \(v\).
The second inequality follows identically with slopes \(\delta/2\)
and \(2\delta\). In particular, the convenient unconditional bound is

\[
H_G(t)\ge\frac{28}{23}k_M+\frac25k_P
\ge\frac25(k_M+k_P).
\]

This gives an explicit check on a fixed profile without computing the
refined crossing. Computing the piecewise-linear crossing gives the exact
and potentially larger gain.

## 4. Retuning the cutoff is necessary

The scalar optimized cutoff is

\[
t_0=1+\frac{b_\delta}{2(\alpha-\delta+b_\delta)},
\]

where \(F_q(t_0)=L_\delta(t_0)=R^*\). Improving only \(F_q\) while
keeping \(t=t_0\) does not improve the full maximum: the long branch
still equals \(R^*\).

There is, however, an explicit valid retuning. Implicit differentiation
at the refined crossing, or a monotone finite-difference comparison, gives

\[
-\frac{2\delta}{3}\le F_G'(t)\le-\frac{14\delta}{37}
\]

almost everywhere. Indeed, if the absolute inverse slope is
\(a\in[\delta/2,\delta]\) and the plain slope is
\(b\in[14\delta/9,2\delta]\), the absolute derivative is \(ab/(a+b)\).
All branches are continuous and piecewise linear, so the same bounds
integrate across a kink.

Given \(H=H_G(t_0)\), choose

\[
\tau=\min\left\{t_0-1,\frac{H}{\alpha-\delta/3}\right\},\qquad t=t_0-\tau.
\]

Then

\[
\max\{F_G(t),L_\delta(t)\}
\le R^*-(\alpha-\delta)\tau.
\]

The same conclusion holds with any certified lower bound on \(H\) in
place of \(H\). This is a power saving in the complete exceptional-row
count, not just in the short branch.

## 5. A concrete residual class for the next target

For the candidate geometry \(\ell=1/6+1/5000\), \(b=1/8\), the
separate endpoint-localization calculation concerns

\[
9/25\le\delta\le21/50,\qquad
0\le y:=1/2-q/\delta\le1/100.
\]

On this box,

\[
\frac{\alpha-\delta}{\alpha-\delta/3}\ge\frac{31}{52}.
\]

Also \(t_0-1>1/10\). To see this, use

\[
\frac{P_x}{D_x}-\frac{14}{37}
 =\frac{4(1-2x)(72-37x)}{37(27-17x)}\ge0
\]

and \(4(9/25)(14/37)>\alpha-9/25\). For an upper bound,
\(P_x/D_x\le2/5\) on \(49/100\le x\le1/2\), giving
\(t_0-1<3/20\). These inequalities are strict with fixed margins.

If a profile has

\[
H_G(t_0)\ge1/5000,
\]

use the fixed lower bound \(1/5000\) in the retuning. Its decrement is
less than \(1/10\), so no endpoint is reached, and the full count improves
by at least

\[
\frac{31}{260000}=\frac1{10000}+\frac1{52000}.
\]

Thus a proposed new arithmetic input with target gain \(1/10000\) is
needed only for the residual profile class

\[
\boxed{\quad 9/25\le\delta\le21/50,\quad
0\le y\le1/100,\quad H_G(t_0)<1/5000.\quad}
\]

For example, choose all the count-level mesh, decrement, and preliminary
moment/detector losses to sum to less than \(1/104000\). The preceding
profile elimination then retains gain greater than \(1/10000\), with
positive margin left for the larger argument. The full argument may choose
an even smaller loss. This works uniformly because the real ranges, box,
and supply margins are fixed; all slot selections are whole slots and all
cutoffs are fixed on each finite amplitude subdivision.

A readily checked sufficient condition for exclusion from this residual
class is

\[
\frac{28}{23}K(z_M(r_0(t_0)))
+\frac25K(z_P(t_0-r_0(t_0)))\ge1/5000.
\]

The residual class is nearly saturated in a precise weighted sense. Its
mean deficit is

\[
\frac1L\sum_iw_i(c-g_i)=c-q=\delta y\le21/5000.
\]

Consequently, for every \(\lambda>0\),

\[
\frac1L\sum_{c-g_i\ge\lambda}w_i
 \le\frac{\delta y}{\lambda}.
\]

In particular, at most one fifth of its physical slot length has amplitude
below \(0.9c=0.45\delta\). The total zero-amplitude length is at most
\(2y\le1/50\) of the physical length. At \(y=0\), every positive-length
slot has \(g_i=c\), hence \(G(z)=qz\), \(K=0\), and \(H_G=0\).
The dangerous fully saturated class survives exactly; it must not be
represented as removed by rearrangement.

## 6. What this establishes and what remains

The existing moments do give a refined count, a correct cutoff retuning,
and a quantitative reduction to a nearly saturated profile class. They do
not control the remaining simultaneous inverse/plain witness event beyond
the old envelope. A new mixed or cross-scale argument can now target this
smaller class. Any endpoint extension using such an argument must state
its additional estimate as a hypothesis until that estimate is proved.
The full-amplitude refinement also changes the supply threshold from
`7/37` to `1/5`; this is available in the present geometries and was checked
explicitly rather than silently assumed.

Related records: [localized payoff](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md),
[exact arithmetic examples](../numerics/amplitude_profile_check.json), and
[scoped review](../reviews/LOCALIZED_TARGET_PROFILE_REVIEW_20261008.md).
