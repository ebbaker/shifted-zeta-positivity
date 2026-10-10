# The complete fixed-delay difference and a covariance obstruction

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Internal
same-model investigation, not independent specialist validation.

**The proposed bounded checkpoint is now an exact arithmetic object, but
it has no proved negative energy margin.** The delay difference below retains
both moving lower cutoffs, both product ceilings, every centering correction,
and the full scalar remainder. A new spectral calculation shows that a
negative cross-scale covariance can occur on a persistent boundary mode while
its squared difference cancels the entire apparent gain. Consequently the
covariance alone is an inadequate success condition. This strengthens the
reason to keep fixed-scale descent a narrow exploratory lane.

## 1. Inputs and an exact remainder ledger

Use [Note 3](3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md), including
its inherited scalar detector, von Mangoldt coefficient identity, and smooth
lattice comparisons. Put

\[
a=11/24,\quad q=7/3,\quad C=2e^{1/4},\qquad
G(v)=(v\ell'(v))',\qquad \mathscr F(v)=\sum_{k\ge1}kG(kv).
\]

The kernel is zero for \(v\ge C\) and is \(O_w(v^3)\) at zero. Write
\(E(t)=\psi(t)-t\), \(M(s)=\sum_{n\le s}\mu(n)\), and
\(M_L(s)=M(s)-M(L)\), \(E_L(t)=E(t)-E(L)\). All cutoff values are
right-continuous. The complete comparison is

\[
\lambda(Z)=\frac1{qZ^2}
 \iint_{s,t>Z^a\atop st<CZ}M_{Z^a}(s)E_{Z^a}(t)
             \mathscr F(st/Z)\,ds\,dt+R(Z),
\qquad R(Z)=O_w(Z^{-7/12}).                 \tag{1}
\]

The remainder here has an exact, rather than only big-O, definition. For
\(L=Z^a\), \(N=Z/L\), set

\[
\begin{aligned}
T(Z;L)&=\frac1{qZ}\sum_n\Lambda(n)\ell(n/Z)
 -c_w\sum_{d\le L}\frac{\mu(d)}d
 -\frac1{qZ}\sum_{m,n>L}A_L(m)\Lambda(n)\ell(mn/Z),\\
R_d(Z;L)&=-\frac1{qN}\sum_{d\le L}\mu(d)r_f(N/d),\\
f(v)&=v^{-1}\int_v^\infty\ell(s)\,ds,\qquad
r_f(y)=\sum_{k\ge1}f(k/y)-y\int_0^\infty f(v)\,dv,\\
A_L(m)&=\sum_{d\mid m,\ d>L}\mu(d).
\end{aligned}                                                    \tag{2}
\]

Then \(R=T+R_d\) exactly. These sums are finite: the zero ordinary
moment of \(\ell\) also makes \(f\) compactly supported away from zero.
The estimates imported from Note 3 are
\(T=O_w(Z^{-7/12})\), \(R_d=O_w(Z^{-2/3})\). In particular the
continuum \(c_w\sum_{d\le L}\mu(d)/d\) is retained in (2); it has not
been discarded as an independently small term.

## 2. One common domain, with all three corrections

Fix \(c>1\), \(0<r\le1\), \(\beta\in[1/2,1]\), and large real
\(X\). Set

\[
Y=X/c,\quad U=X^a,\quad V=Y^a,\quad k=r c^{1+\beta},\quad
m=M(U)-M(V),\quad e=E(U)-E(V).
\]

Take \(X\) sufficiently large that \(U^2<CY\) and both copies of
(1) apply. Define

\[
\begin{aligned}
\Omega&=\{s,t>U:\ st<CY\},\\
\mathcal T&=\{s,t>U:\ CY\le st<CX\},\\
\mathcal L&=\{s,t>V:\ st<CY,\ \min(s,t)\le U\},\\
K_X(s,t)&=\mathscr F(st/X),\qquad K_Y(s,t)=\mathscr F(st/Y).
\end{aligned}                                                     \tag{3}
\]

The lower correction can be split disjointly into
\(V<s\le U,t>V,st<CY\) and
\(s>U,V<t\le U,st<CY\). The first part includes the corner where both
variables are at most \(U\); it must not be counted twice.

For \(f_\beta(Z)=Z^{1-\beta}\lambda(Z)\), direct subtraction gives

\[
\boxed{\quad
f_\beta(X)-r f_\beta(Y)
=\frac{\mathcal B_r+\mathcal C+\mathcal T_X+\mathcal L_r}
       {qX^{1+\beta}}+\mathcal R_{\beta,c,r}(X),\quad}       \tag{4}
\]

where every integral below uses ordinary Lebesgue measure \(ds\,dt\):

\[
\begin{aligned}
\mathcal B_r&=\iint_\Omega M_V(s)E_V(t)(K_X-kK_Y),\\
\mathcal C&=\iint_\Omega[-mE_V(t)-eM_V(s)+me]K_X,\\
\mathcal T_X&=\iint_{\mathcal T}M_U(s)E_U(t)K_X,\\
\mathcal L_r&=-k\iint_{\mathcal L}M_V(s)E_V(t)K_Y,\\
\mathcal R_{\beta,c,r}(X)
 &=X^{1-\beta}R(X)-rY^{1-\beta}R(Y)
 =O_{w,\beta,c,r}(X^{-(\beta-5/12)}).
\end{aligned}                                                     \tag{5}
\]

**Proof.** Partition the \(X\)-domain into \(\Omega\cup\mathcal T\)
and the \(Y\)-domain into \(\Omega\cup\mathcal L\). On the common
domain substitute \(M_U=M_V-m\), \(E_U=E_V-e\). The normalized
smaller-scale coefficient is
\(rY^{-1-\beta}=kX^{-1-\beta}\); expanding the product proves (4).
The exact remainder formula (2) and its bounds prove the last line of (5).
Product boundaries are measure-zero, and the uppermost kernel endpoint is
zero. No boundary atom in the original Stieltjes identity is reinstated.
\(\square\)

Equation (4) is the requested complete fixed-delay arithmetic difference.
In particular the terminal ceiling shifts by a factor \(c\), while each
factor cutoff shifts by \(c^a\). They are different changes. Replacing
all cutoffs by \(U\), or using only the bulk kernel difference, loses
terms in (5). No separate affordable bound for \(\mathcal C\),
\(\mathcal T_X\), or \(\mathcal L_r\) is claimed.

For completeness, the finite-coefficient version retains the delayed
continuum with the exact coefficient

\[
c_w X^{1-\beta}
\left(\sum_{d\le U}\frac{\mu(d)}d
-r c^{\beta-1}\sum_{d\le V}\frac{\mu(d)}d\right).       \tag{6}
\]

In (4) its density cancellation is encoded by \(R_d\) at both scales.
One cannot keep the mixed sums from (2) while omitting (6).

## 3. The actual signed estimate that would suffice

Let \(B_\beta(Z)=Z^{1-\beta}\mathcal Q(Z)\), with \(\mathcal Q\)
the complete integral in (1), and define

\[
\mathcal E_\beta(X)=\int_1^2|B_\beta(Xu)|^2du,\qquad
D_X(u)=B_\beta(Xu)-B_\beta(Xu/c).
\]

The delay \(D_X(u)\) is precisely the four integrals in (4)–(5), with
\(r=1\), evaluated at \(Xu\); each scale therefore has its own cutoff.
The following is a specific remaining covariance obligation:

\[
2\Re\int_1^2 D_X(u)\overline{B_\beta(Xu/c)}\,du
 +\int_1^2|D_X(u)|^2du
\le-\kappa\mathcal E_\beta(X/c)+CX^{-\eta},
\quad0<\kappa<1,\ \eta>0.                         \tag{7}
\]

This is bilinear in the two complete arithmetic response functionals.
Expanding it in \(M\) and \(\psi-t\) gives quartic correlations, with
all bulk, centering, lower, terminal, and pair-cross terms. Thus an isolated
bilinear \(M\)–\(\psi-t\) bound is not automatically (7).
A convenient sufficient pair is
\(2\Re\langle D_X,B_Y\rangle\le-(\kappa+\nu)\|B_Y\|^2+CX^{-\eta}\)
and \(\|D_X\|^2\le\nu\|B_Y\|^2+CX^{-\eta}\).
**Both** inequalities matter.

If (7) held at an admissible \(\beta>1/2\), the exact square identity
and Note 1's fixed-scale iteration give
\(\mathcal E_\beta(X)=O(X^{-\sigma})\) for every
\(0<\sigma<\min\{\eta,\log(1/(1-\kappa))/\log c\}\).
The scalar remainder in (5) permits a positive power saving for the
corresponding energy built from \(f_\beta\) as well. A dyadic-shell
Cauchy–Schwarz argument then extends the holomorphic Mellin domain of
\(\int\lambda(X)X^{-z}dX\) strictly to the left, and the detector's nonzero zero residues give a smaller strip.
This is a proved conditional implication, not a proof of (7).

A stronger but simpler alternative is a complete signed estimate

\[
|\mathcal B_r+\mathcal C+\mathcal T_X+\mathcal L_r|
\ll X^{1+\beta-\eta},\qquad0<r<1.                  \tag{8}
\]

Then (4) gives \(f_\beta(X)=rf_\beta(X/c)+O(X^{-\eta'})\), where
\(\eta'=\min\{\eta,\beta-5/12\}>0\), and fixed-scale iteration
gives scalar power decay. Estimates (7) and (8) identify complete targets;
no estimate for them is established here.

## 4. New obstruction: a negative covariance can pay no net energy

Here is a scoped analytic theorem using the fixed-probe explicit formula
already invoked in Notes 1–2. In log coordinates \(y=\log X\), assume
an admissible strip \(\Re\rho\le\beta\), \(\beta>1/2\). The scalar
formula and its summable coefficient majorant give

\[
f_\beta(e^y)=\sum_{\Re\rho=\beta}b_\rho e^{i\gamma_\rho y}+o(1),
\qquad b_\rho=-m_\rho D(\rho),\qquad\sum_\rho|b_\rho|<\infty.
                                                               \tag{9}
\]

The formula follows by integrating the complete linear formula for
\(V_g\) against \(y\,dy/q\) on \([1,2]\); this is also the source
of the scalar factor \(D\). Multiplicity is already in \(b_\rho\).
Replacing \(f_\beta\) by \(B_\beta\) changes (9) by a decaying
power and hence does not alter any following mean.

Let \(h=\log c\), \(A_\beta=\sum_{\Re\rho=\beta}|b_\rho|^2\),
and take Cesàro means in \(y\). Then

\[
\begin{aligned}
\operatorname{Mean}\mathcal E_\beta(e^y)&=A_\beta,\\
\operatorname{Mean}\left[2\Re\langle D_{e^y},B_{e^y/c}\rangle\right]
 &=2\sum_{\Re\rho=\beta}|b_\rho|^2(\cos(\gamma_\rho h)-1),\\
\operatorname{Mean}\|D_{e^y}\|^2
 &=2\sum_{\Re\rho=\beta}|b_\rho|^2(1-\cos(\gamma_\rho h)).
\end{aligned}                                                    \tag{10}
\]

**Proof.** First use a finite edge sum. Distinct frequencies have zero
mean cross product. The fixed \(u\)-integration introduces phases
\(u^{i\gamma}\) of modulus one and interval length one, so each
same-frequency contribution is unchanged. For each frequency the delayed
factor is \(e^{-i\gamma h}\), giving the two displayed real expressions.
Absolute summability extends the calculation to the full edge sum; the
uniform \(o(1)\) term has zero mean contribution. \(\square\)

Thus the last two means cancel **exactly**. For a resonant edge mode
\(\gamma h\in2\pi\mathbb Z\), both vanish. Otherwise the covariance
is negative, possibly very negative, but the squared delay defect removes
all the apparent benefit. In particular if \(A_\beta>0\), (7) is
impossible: its left side has mean zero and its right side has negative
mean \(-\kappa A_\beta\).

This theorem is conditional on a boundary zero being present; it is not an
Euler-product counterexample. If the optimal real-part supremum is
unattained, \(A_\beta=0\), and (10) alone says nothing quantitative
about descent. The spectral-edge problem in Note 2 remains. The advance
is a precise rejection criterion: **reporting a negative covariance
without paying the squared defect is not progress toward contraction.**

## 5. Checks and next priority

The new [checker](../../numerics/check_fixed_heat_checkpoint.py) verifies
55,296 exact rational mesh-point partitions of (4), with all three
correction groups nonzero in every tested case, and five exact finite-mode
covariance identities, including resonance. The
[record](../../numerics/fixed_heat_checkpoint_record_20261009.json) identifies
this limited scope. The synthetic meshes verify bookkeeping; they do not
estimate the actual arithmetic integral or prove its asymptotic sign.

The comparative review's priority continues to hold. The next useful fixed-
scale task is a proved signed estimate for **one complete** combination in
(7) or (8), with its complements paid. More lattice-remainder sharpening,
cutoff averaging, or an attractive covariance sign by itself does not address
the missing margin. Until such a mechanism appears, this branch supplies a
clean independence benchmark for the family methods and a bounded arithmetic
scout, rather than a demonstrated descent route.
