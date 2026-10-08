# A normalized heat collision criterion with reflected errors and a fixed cutoff

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed to this agent and are not inferred.
Same-model cross-review is an internal check, not independent validation.

Status: a derivation from an imported effective approximation theorem. The
complex-neighborhood, derivative, reflection, and cutoff corrections are proved
below. No new bound near time zero, full-flow Wronskian sign, or RH conclusion
is claimed. The crude explicit height bound is a rederivation of known
positive-time eventual simplicity, not a claimed improvement or priority result.

The [previous arithmetic note](ZETA_COLLISION_ARITHMETIC_20261008.md) left a
specific task: turn an effective normalized scalar heat approximation into an
analytic-neighborhood approximation, pay its moving integer cutoff, and obtain
an actual derivative error. This note completes that reduction. It also yields
an explicit, deliberately enormous sufficient high-height cutoff:

\[
 0<\varepsilon\le\tfrac12,\quad
 \varepsilon\le t\le\tfrac12,\quad
 |x|\ge\exp(64/\varepsilon)
 \quad\Longrightarrow\quad
 (H_t(x),H'_t(x))\ne(0,0).
 \tag{A}
\]

The remaining finite interval grows without bound as \(\varepsilon\downarrow0\).
There is no certificate for that interval in this note.

## 1. Imported theorem and an analytic rewriting

Use \(H_0(z)=\xi(1/2+iz/2)/8\). The only substantial analytic input here is
[Polymath, Theorem 1.3 and equations (6)–(24)](https://arxiv.org/html/1904.12438#S1.Thmtheorem3).
Its proved approximation applies for real parameters
\(0<t\le1/2\), \(x\ge200\), \(0\le y\le1\). The original proof is not
replayed. In particular, it is not being extrapolated to negative heat time,
a larger imaginary strip, or a derivative statement without further argument.

Let \(s=(1-iz)/2\), and use the principal logarithms in

\[
 \begin{aligned}
 m_0(s)={}&\operatorname{Log}s+\operatorname{Log}(s-1)
 -\frac{s}{2}\log\pi+\log\frac{\sqrt{2\pi}}{16}\\
 &+\left(\frac{s}{2}-\frac12\right)\operatorname{Log}\frac{s}{2}
 -\frac{s}{2},\\
 \alpha(s)={}&\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi},\\
 m_t(s)={}&m_0(s)+\frac t4\alpha(s)^2,\qquad M_t(s)=e^{m_t(s)}.
 \end{aligned}
 \tag{1}
\]

These branches are holomorphic for \(s\notin(-\infty,1]\), with
\(m_t(\bar s)=\overline{m_t(s)}\) for real \(t\). For positive real part
of \(z\), both \(s\) and \(1-s\) stay off that cut.

For a **fixed** integer \(N\ge1\), define

\[
 \begin{aligned}
 p_{t,n}(s)&=\exp\left(\frac t4\log^2n
                      -(s+\tfrac t2\alpha(s))\log n\right),\\
 P_{t,N}(s)&=\sum_{n=1}^N p_{t,n}(s),\\
 G_{t,N}(z)&=M_t(s)P_{t,N}(s)+M_t(1-s)P_{t,N}(1-s).
 \end{aligned}
 \tag{2}
\]

For the natural cutoff

\[
 n(t,x)=\left\lfloor\sqrt{\frac{x}{4\pi}+\frac t{16}}\right\rfloor,
 \tag{3}
\]

this is exactly the unnormalized finite approximation in the imported theorem.
To check the seemingly conjugated second sum there, observe that
\(\bar s-y=1-s\) and
\(\overline{\alpha(s)}=\alpha(\bar s)\). The source's correction
\(\kappa=\tfrac t2(\alpha(1-s)-\alpha(\bar s))\) then turns
\(n^y n^{-\overline{s_*}-\kappa}\) into
\(n^{-(1-s)-t\alpha(1-s)/2}\). No conjugate variable remains in (2).

Consequently \(G_{t,N}\) is holomorphic in \(z\) when \(N\) is fixed and
satisfies

\[
 G_{t,N}(\bar z)=\overline{G_{t,N}(z)}.
 \tag{4}
\]

This symmetry is what permits reflection of the error below the real axis.
Differentiating a formula with the natural moving cutoff (3) would not be
valid at its jumps; no such differentiation is used.

## 2. A symmetric nonzero normalizer

Define the analytic functions

\[
 \begin{aligned}
 A_t(z)&=\exp\left(\frac{m_t(s)+m_t(1-s)}2\right),\\
 \theta_t(z)&=\frac{m_t(s)-m_t(1-s)}{2i},\\
 Q_t(z)&=H_t(z)/A_t(z),\qquad F_{t,N}(z)=G_{t,N}(z)/A_t(z).
 \end{aligned}
 \tag{5}
\]

On the real axis, \(A_t(x)=|M_t((1-ix)/2)|>0\), and \(\theta_t(x)\),
\(Q_t(x)\), and \(F_{t,N}(x)\) are real. All these quotients are
holomorphic in a neighborhood of every closed disk used below. In
particular the normalizer has no hidden zeros inside a Cauchy contour.
The normalized approximation is

\[
 F_{t,N}=e^{i\theta_t}P_{t,N}(s)+e^{-i\theta_t}P_{t,N}(1-s).
 \tag{6}
\]

It has real symmetry, as does the remainder \(Q_t-F_{t,N}\). Thus an upper
half-disk bound for this remainder also bounds the lower half-disk.

Common zeros are invariant under this normalization:

\[
 H_t(x)=H'_t(x)=0\quad\Longleftrightarrow\quad
 Q_t(x)=Q'_t(x)=0.
 \tag{7}
\]

Unlike raw theta quadrature, (6) never needs the exponentially small common
factor \(\exp(-\pi x/8+o(x))\) to be represented numerically. It still has
oscillatory finite sums and possible cancellation. No relative lower bound
on the collision vector is asserted by normalization alone.

For explicit derivative evaluation, put

\[
 \lambda_{t,n}(s)=(\alpha(s)-\log n)(1+\tfrac t2\alpha'(s)),
 \qquad a_{t,n}(s)=M_t(s)p_{t,n}(s).
\]

Then

\[
 \begin{aligned}
 G'_{t,N}(z)&=\frac i2\sum_{n\le N}
 \bigl(\lambda_{t,n}(1-s)a_{t,n}(1-s)
       -\lambda_{t,n}(s)a_{t,n}(s)\bigr),\\
 b_t(z):=A'_t/A_t&=-\frac i4\bigl(m'_t(s)-m'_t(1-s)\bigr),\\
 F'_{t,N}&=G'_{t,N}/A_t-b_tF_{t,N},\qquad
 m'_t=\alpha(1+\tfrac t2\alpha').
 \end{aligned}
 \tag{8}
\]

The normalized terms \(a_{t,n}/A_t\) should be evaluated directly by
subtracting their logarithms before exponentiating, rather than dividing
underflowed unnormalized values.

## 3. A fully explicit uniform disk error

Fix

\[
 0<\varepsilon\le\tau\le\tfrac12,\qquad
 0<R\le1,\qquad X-R\ge200,
\]

and use every disk \(|z-X|\le R\), at every real time
\(t\in[\varepsilon,\tau]\). The following bounds use the enclosing upper
rectangle \(x\in[X-R,X+R]\), \(0\le y\le R\); all points remain in the
source theorem's stated domain.

Write

\[
 x_-=X-R,\quad x_+=X+R,\quad q_\pm=x_\pm/(4\pi),\quad V=x_-/2,
 \quad S=\tfrac12\sqrt{x_+^2+(1+R)^2},
\]
\[
 \begin{aligned}
 \alpha_-&=\tfrac12\log q_- -V^{-2}>0,\\
 A_*&=\frac{3}{2V}+rac12
       \sqrt{\log^2(S/(2\pi))+\pi^2/4},\\
 D_*&=\frac{3}{2V^2}+\frac1{2V},\\
 L_*&=A_*(1+\tfrac\tau2D_*),\qquad K_*=e^{RL_*/2}.
 \end{aligned}
 \tag{9}
\]

On the whole rectangle, both arguments \(s,1-s\) have real parts in
\([0,1]\), imaginary parts of magnitude at least \(V\), and modulus at
most \(S\). Directly from (1),

\[
 \operatorname{Re}\alpha(s),\operatorname{Re}\alpha(1-s)\ge\alpha_-;
 \quad |\alpha|\le A_*;\quad |\alpha'|\le D_*;\quad |m'_t|\le L_*.
 \tag{10}
\]

For the real-part lower bound use
\(\operatorname{Re}(1/(2s))\ge0\),
\(\operatorname{Re}(1/(s-1))\ge-V^{-2}\), and
\(|s|\ge V\). The modulus bounds use \(|\arg s|\le\pi/2\).
Integrating the vertical derivative of
\((m_t(s)-m_t(1-s))/2\), whose real part vanishes at \(y=0\), gives

\[
 |M_t(s)/A_t|,\ |M_t(1-s)/A_t|\le K_*.
 \tag{11}
\]

The natural cutoff lies among the explicitly known integers

\[
 m_-:=\left\lfloor\sqrt{q_-+\varepsilon/16}\right\rfloor,
 \qquad
 m_+:=\left\lfloor\sqrt{q_++\tau/16}\right\rfloor.
 \tag{12}
\]

Here \(m_-\ge3\), and \(m_+-m_-\le1\). Indeed the range of the quantity
inside the square root has length at most
\(1/(2\pi)+1/32<1\), and the square root itself varies by less than one.
Choose any fixed \(N\ge1\); using \(N=m_-\) means that a crossing costs
at most one additional summand.

For \(n\ge1\), define the elementary positive bounds

\[
 \begin{aligned}
 d_n&=\tfrac14\log^2n-\tfrac12\alpha_-\log n,\\
 V_n&=n^{-1/2}\exp(\max\{\varepsilon d_n,\tau d_n\}),
 \qquad P_n=n^{R/2}V_n,\\
 \ell_n&=\max\{|\log(q_-/n^2)|,|\log(q_+/n^2)|\},\\
 k_*&=\frac{\tau R}{2(x_--6)},\\
 U_n&=\exp\left(\frac{\tau^2\ell_n^2/16+0.626}{x_--6.66}\right)-1.
 \end{aligned}
 \tag{13}
\]

The maximum over time endpoints is legitimate because the logarithm of the
heat weight is affine in \(t\). It preserves the negative heat exponent
when \(d_n<0\); replacing its positive and negative pieces separately by
worst times would needlessly lose the high-height decay.

For each \(m\in\{m_-,\ldots,m_+\}\), put

\[
 \begin{aligned}
 E_m^{AB}&=\sum_{n=1}^m(1+m^{k_*}n^R)V_nU_n,\\
 E_m^C&=q_-^{-1/4}\exp\left(
 -\frac\varepsilon{16}\log^2q_-
 +\frac{1.24(3^R+3^{-R})}{m-0.125}
 +\frac{3\sqrt{\log^2q_++\pi^2/4}+10.44}{x_--12}
 \right),\\
 \eta_N&=K_*\max_{m_-\le m\le m_+}
 \left(E_m^{AB}+E_m^C
       +2\sum_{n=\min(m,N)+1}^{\max(m,N)}P_n\right).
 \end{aligned}
 \tag{14}
\]

An empty correction sum is zero. All constants in (14) are explicit; decimal
constants retain exactly their meanings in the imported inequalities.

### Proposition 1: normalized error with reflection and cutoff payment

For every \(t\in[\varepsilon,\tau]\) and \(|z-X|\le R\),

\[
 |Q_t(z)-F_{t,N}(z)|\le\eta_N.
 \tag{15}
\]

**Proof.** On the upper rectangle use the source theorem with its actual
cutoff \(m=n(t,x)\). Its estimates (23)–(24) are majorized by
\(E_m^{AB}+E_m^C\): the source's \(|\gamma|\le1\),
\(m^{|\kappa|}\le m^{k_*}\), \(n^y\le n^R\), and the first sum's
\(|p_{t,n}(s)|\le V_n\) follow from (10) and \(\operatorname{Re}s\ge1/2\).
For \(|\gamma|\le1\), the source's bound
\(e^{0.02y}(x/(4\pi))^{-y/2}\le1\) uses \(x\ge200\).
The remaining elementary terms are bounded monotonically as displayed.
Changing normalization from \(M_t(s)\) to \(A_t\) costs at most \(K_*\).

With a different fixed cutoff \(N\), the exact difference between the two
finite sums consists of the missing or added terms. Each of its two reflected
summands, divided by \(A_t\), is at most \(K_*P_n\), since both real parts
\(\operatorname{Re}s,\operatorname{Re}(1-s)\) are at least
\((1-R)/2\). This proves (15) on the upper rectangle. The real symmetry of
\(Q_t-F_{t,N}\) proves the same bound on the lower half-disk. \(\square\)

The factor \(K_*\) is essential. Reflection of an unnormalized error does
not preserve its bound after division by a nonsymmetric normalizer.

## 4. Derivative error and a compact collision criterion

Fix \(0\le a<R\). By Cauchy's formula applied to the **holomorphic**
remainder in (15), for real \(|x-X|\le a\) and
\(t\in[\varepsilon,\tau]\),

\[
 |Q_t(x)-F_{t,N}(x)|\le\eta_N,
 \qquad
 |Q'_t(x)-F'_{t,N}(x)|\le\frac{\eta_N}{R-a}.
 \tag{16}
\]

Thus either of the verified inequalities

\[
 \inf_{\substack{t\in[\varepsilon,\tau]\\|x-X|\le a}}
 |F_{t,N}(x)|>\eta_N,
 \qquad\text{or}\qquad
 \inf_{\substack{t\in[\varepsilon,\tau]\\|x-X|\le a}}
 |F'_{t,N}(x)|>\frac{\eta_N}{R-a}
 \tag{17}
\]

certifies no real collision on the full rectangle. A finite cover may use a
different successful alternative in each cell. The infima can be enclosed
by interval evaluation of the finite formulas (6), (8) on real parameter
cells, or by derivative-controlled subdivision. Merely checking center
values does not establish (17).

No interval arithmetic implementation or compact-rectangle certificate is
claimed here. The substantive advance over the previous note is that the
complete complex-neighborhood and derivative error are now explicit, including
reflection and every possible cutoff jump. It is no longer necessary to assume
an unspecified analytic-neighborhood extension of the source theorem.

## 5. A phase-independent leading-pair test

A fixed cutoff \(N=1\) is also allowed in (14), if the whole finite tail is
paid. In this case

\[
 F_{t,1}(x)=2\cos\theta_t(x),\qquad
 F'_{t,1}(x)=-2\theta'_t(x)\sin\theta_t(x),
 \tag{18}
\]
\[
 \theta'_t(x)=-\tfrac12\operatorname{Re}m'_t((1-ix)/2).
\]

Equations (9)–(10) give throughout the inner interval

\[
 |\theta'_t(x)|\ge
 \omega_*:=\tfrac12(\alpha_- -\tfrac\tau2A_*D_*),
 \quad\text{provided }\omega_*>0.
 \tag{19}
\]

If a collision occurred, (16) would force
\(|\cos\theta_t|\le\eta_1/2\) and
\(|\sin\theta_t|\le\eta_1/(2(R-a)\omega_*)\). Consequently the explicit
condition

\[
 \omega_*>0,\qquad
 \left(\frac{\eta_1}{2}\right)^2
 +\left(\frac{\eta_1}{2(R-a)\omega_*}\right)^2<1
 \tag{20}
\]

excludes collisions on the whole inner rectangle, without needing to locate
individual zeros or numerically enclose their oscillatory phase.

The next corollary uses deliberately wasteful estimates to make the height
cutoff completely explicit. The cost is its enormous size.

### Corollary 2: explicit high-height collision exclusion

Statement (A) holds.

**Proof.** It suffices to consider \(x=X>0\); evenness handles the other
sign. Take \(\tau=1/2\),

\[
 X\ge e^{64/\varepsilon},\qquad L=\log(X/(4\pi)),
 \qquad R=1/L,\qquad a=0,
 \tag{21}
\]

and use the disk quantities above. The following deliberately relaxed
bounds follow from \(X\ge e^{128}\), \(\log(4\pi)<2.6\), and (9)–(13):

\[
 \begin{gathered}
 L>125,\quad \log q_->125,\quad \varepsilon\log q_->62,
 \quad R<1/125,\\
 \alpha_-\ge\tfrac12\log q_- -0.001,\qquad
 \log m_+\le\tfrac12\log q_-+0.01,\\
 A_*\le0.51L,\quad D_*<0.001,\quad
 K_*<1.3,\quad R\omega_*>0.24.
 \end{gathered}
 \tag{22}
\]

For clarity, the logarithms of \(q_\pm\) differ from \(L\) by at most
\(2R/X\), and the logarithm of \(m_+\) is at most
\(\tfrac12\log(q_++1/32)\). These give the middle estimates.
The bounds for \(A_*,D_*\) follow directly from their definitions;
\(L_*/L<0.52\) gives \(K_*<e^{0.26}<1.3\).
Finally \(\alpha_-/L>0.499\) and
\(\tfrac\tau2 A_*D_*/L<0.000128\), which give the last estimate.

In particular \(\log m_+<2\alpha_-\), so \(d_n\le0\) for all
\(n\le m_+\). Put

\[
 p=\frac{1-R}{2}+\frac\varepsilon2\alpha_-
                         -\frac\varepsilon4\log m_+.
\]

By (22),
\(p>0.496+62/8-0.0015>8\). Thus
\(P_n\le n^{-p}\le n^{-8}\) and

\[
 \sum_{n=2}^{m_+}P_n
 \le2^{-8}+\int_2^\infty v^{-8}dv
 =\frac1{256}+\frac1{896}.
 \tag{23}
\]

The other terms in (14) are far smaller. For \(n\le m_+\),
\(\ell_n\le\log X\). Hence, since \((\log X)^2/X\) decreases for
\(X\ge e^{128}\),

\[
 U_n\le\exp\left(\frac{(\log X)^2/64+0.626}{X-R-6.66}\right)-1
 <10^{-40}.
\]

Also \(m_+^{k_*}<2\), and \(p-R>7\). Bounding both resulting power sums
by \(1+1/6\) yields

\[
 E_m^{AB}<4\times10^{-40}.
 \tag{24}
\]

In \(E_m^C\), the negative heat exponent is at most
\(-62\cdot125/16<-484\). The two positive exponent terms together are
less than \(3\) (use \(m\ge3\), \(R\le1\), and \(X\ge e^{128}\)).
Since its leading power factor is at most one,

\[
 E_m^C<e^{-481}<10^{-100}.
 \tag{25}
\]

Combining (14), (23)–(25), uniformly in every permitted cutoff and time,

\[
 \eta_1<1.3\left(4\times10^{-40}+10^{-100}
             +2\left(\frac1{256}+\frac1{896}\right)\right)<0.014.
 \tag{26}
\]

Equations (22), (26) imply the left side of (20), with \(a=0\), is at most

\[
 (0.014/2)^2+(0.014/0.48)^2<0.001<1.
\]

The collision is excluded at the arbitrary point \(X\), proving (A).
All finite sums in the proof have been bounded analytically; no floating-point
sample or finite-height RH verification enters this corollary. \(\square\)

## 6. What remains and what the criterion changes

For a hypothetical collision at time \(t\ge\varepsilon>0\), (A) gives an
explicit finite search interval \(|x|<e^{64/\varepsilon}\). On its portion
\(|x|\ge200\), (14)–(17) provide a finite normalized certificate target;
the earlier theta certificate handles lower heights. This is conceptually
complete coverage for a **specified** positive time floor, but may be utterly
impractical at this crude cutoff. Sharper errors, a correction term, and larger
finite cutoffs can materially reduce its computational size.

The leading-pair argument is a high-height simplification. It does not imply
that keeping only the first theta summand is permissible: (2) is an effective
Riemann–Siegel approximation with all its finite and analytic remainders paid,
not the fixed positive-half-line theta truncation ruled out previously.
There is no assertion that \(H_t\) has an Euler product.

A next computational step can now implement (14), (8), and interval coverage
in a normalized arithmetic backend, explicitly testing cells that straddle
(3). A next analytic step would need a lower bound for the genuine normalized
collision vector in the remaining middle-height range, with its constants
as \(\varepsilon\downarrow0\). Neither interval arithmetic nor the explicit
positive-time cutoff supplies that missing estimate. The union over all
positive time floors still requires infinitely many shrinking-time regimes;
no fixed finite certificate proves RH.

The small standard-library script
[check_normalized_heat_constants.py](../numerics/check_normalized_heat_constants.py)
checks the final rational implications in (22)–(26), including the explicit
cosine/sine contradiction. Its saved
[record](../numerics/normalized_heat_constant_record_20261008.json) reports only
those exact arithmetic checks. The analytic disk estimates and the imported
approximation theorem remain proof inputs; the script does not certify them
by sampling. All deliverables are small source/record files under the
repository's large-file convention.
