# Continuation: quasi-RH, character amplification, and exponent descent

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and cross-review are internal checks, not
independent specialist validation.

**Subsequent work:** the [third continuation results](THIRD_CONTINUATION_RESULTS_20261008.md),
[second continuation results](SECOND_CONTINUATION_RESULTS_20261008.md),
and [dependency ledger](RESEARCH_LEDGER_20261008.md) update the immediate
tasks below. In particular, one fixed short-family moment now suffices
for finite repeated extraction of its floor; the stronger scale supremum
is unnecessary for that conclusion. The new notes also refine the mixed
conductor residual, construct the complete integer-response lift, and
identify the finite theta-cutoff obstruction. The missing arithmetic
estimates remain open.

## 1. Purpose and present conclusion

Continue the investigation in papers/quasi-rh-exponent-descent/, using
both papers/prime-variance-exponents/ and
papers/quasi-rh-character-amplification/. The central question is whether
a fixed zero strip strictly narrower than the critical strip can lead to
RH through arithmetic exponent descent, direct exclusion of off-line
zeros, or a zeta-specific obstruction to positive Newman time.

**The character-amplification work is relevant, but does not already supply
the missing descent.** It contributes actual arithmetic families,
simultaneous inverse/plain witnesses, exact signed kernels, conductor
localization, and signal-preserving probe combinations. Its short-family
transfer suggests an explicit conditional iteration toward \(1/2\).
Its audits identify why the available moment estimates cannot simply be
inserted into that iteration or into the prime-variance recurrence.

This note deliberately covers more than improvement of one numerical
boundary. It separates several possible endpoints and gives each route
a first task, missing input, and test of whether it could reach RH.
It is not an exhaustive classification of possible RH proofs. The
recommended order should change when new evidence favors another route.

No new signed arithmetic estimate, zero-free region, or implication
quasi-RH ⇒ RH is proved here. New deductions below are conditional exponent
bookkeeping and refinements of existing reductions. The
[relevance review](../reviews/CHARACTER_AMPLIFICATION_RELEVANCE_REVIEW_20261008.md)
records the audit and its limits.

### Source status and the logical hypothesis

The amplification project imports deep statements from the September 30
2026 [seven-eighths paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
and the distinct October 5
[eleven-twelfths paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf).
The former PDF is identified locally by SHA-256
8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.
The [published formalization scope](https://raw.githubusercontent.com/openai/math/main/lean/docs/003.md)
states a \(7/8\) boundary for zeta, Dirichlet functions, and finite-order
Hecke functions over \(\mathbb Q(\sqrt{-3})\). Reading that scope is not
a proof replay. This session did not validate the deep analytic machinery
or replay Lean. The local extension remains conditional on imported inputs.

Keep three hypotheses distinct:

1. **Zeta-only quasi-RH:** every nontrivial zeta zero satisfies
   \(\Re\rho\le B<1\), for one fixed \(B\).
2. **A family strip:** a corresponding bound for the relevant Hecke
   functions, with the growth controls and quantifiers required by the
   particular family argument.
3. **A new short-family or mixed-moment estimate:** stronger arithmetic
   information that might imply RH when combined with a strip.

Zeta-only quasi-RH does not grant 2 or 3. A proof from stronger hypotheses
must be labeled accordingly. A direct proof using independently established
family estimates would still be valuable even if it is not a proof of
the logical implication from hypothesis 1 alone.

## 2. Repository reading order

Start with the [descent overview](../README.md),
[initial review](../reviews/INITIAL_REVIEW_20261008.md),
[amplification overview](../../quasi-rh-character-amplification/README.md),
[current amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex),
and [prime-variance overview](../../prime-variance-exponents/notes/PROJECT_OVERVIEW_20261004.md).

For the nearest mixed-moment task, read the **latest** records:

- [Plain-ratio and total-ratio conductor reduction](../../quasi-rh-character-amplification/notes/SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md).
- [Proved mixed subcases](../../quasi-rh-character-amplification/notes/SELECTOR_PRESERVING_SUBCASES_20261008.md).
- [Energy localization and buffered application triangle](../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md).
- [Selector-preserving review](../../quasi-rh-character-amplification/reviews/SELECTOR_PRESERVING_REVIEW_20261008.md).

For scalable alternatives, read:

- [Character-family transfer](../../quasi-rh-character-amplification/notes/CHARACTER_FAMILY_TRANSFER_20261008.md).
- [Joint witnesses](../../quasi-rh-character-amplification/notes/JOINT_WITNESS_REDUCTION_20261008.md)
  and [amplitude profiles](../../quasi-rh-character-amplification/notes/AMPLITUDE_PROFILE_REDUCTION_20261008.md).
- [Common-signal probes](../../quasi-rh-character-amplification/notes/COMMON_SIGNAL_PROBE_SCOUT_20261008.md).
- [Geometry optimization](../../quasi-rh-character-amplification/notes/GEOMETRY_OPTIMIZATION_20261008.md),
  [off-balance geometry](../../quasi-rh-character-amplification/notes/OFF_BALANCE_GEOMETRY_SCOUT_20261008.md),
  and the low, moment, and contour audits linked there.
- [Selector feasibility](../../quasi-rh-character-amplification/notes/SELECTOR_FEASIBILITY_20261008.md),
  [live divisor transform](../../quasi-rh-character-amplification/notes/LIVE_DIVISOR_TRANSFORM_20261008.md),
  and [marked transfer audit](../../quasi-rh-character-amplification/reviews/MARKED_MIXED_TRANSFER_AUDIT_20261008.md).

The older amplification continuation is useful history, but its first
selector and live-divisor investigations have already been done. Likewise,
the earlier residual \(T_{\rm large}\), with total-ratio cutoff \(U^{4/5}\),
has been sharpened to \(T_{\rm joint}\). Do not restart at diagonal removal.

## 3. Notation and possible endpoints

| Symbol here | Meaning |
| --- | --- |
| \(B_\zeta\) | Supremum of real parts of nontrivial zeta zeros |
| \(B_{\rm fam}\) | Supremum of \(1/2\) and real parts of zeros of all primitive finite-order Hecke functions over \(\mathbb Q(\sqrt{-3})\) |
| \(\delta\) | Prime-variance exponent; optimally \(\delta_*=2B_\zeta-1\) |
| \(d\) | Amplification zero-bin parameter \(2a_{\rm bin}-1\), called delta in that project |
| \(x\) | Amplification amplitude ratio \(q_{\rm bin}/d\), near \(1/2\) in the hard class |
| \(X\) | Real-prime shell scale in the variance problem |
| \(U,D,N\) | Character row scale, inverse length \(D=U^r\), plain length \(N=U^m\) |
| \(Z,T\) | Amplification outer physical scale and height; neither is automatically \(X\) |
| \(h\) | Short-family exponent in \(H=D^h\), in Route B only |
| \(\kappa\) | Source fourth-moment parameter, audited in \([3/4,1]\) |
| \(\Lambda_{\rm DN}\) | de Bruijn–Newman constant, distinct from von Mangoldt \(\Lambda(n)\) |

The inherited fixed-probe theorem is

\[
\mathcal V_g(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
|\Re\rho-1/2|\le\delta/2
\quad\text{for every nontrivial zeta zero}.                 \tag{1}
\]

Its least admissible exponent is attained as a variance bound. This does
**not** imply that some zero attains the spectral supremum. Quasi-RH means
\(\delta_*<1\); RH means \(\delta_*=0\).

Rodgers–Tao gives \(\Lambda_{\rm DN}\ge0\) unconditionally; RH is equivalent
to \(\Lambda_{\rm DN}\le0\), hence to equality. The sign correction is
settled. With \(H_0(z)=\xi(1/2+iz/2)/8\), the strip theorem gives
\(0\le\Lambda_{\rm DN}\le\delta_*^2/2\), not its vanishing. See the
[bridge note](../../prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md)
and [Rodgers–Tao](https://arxiv.org/abs/1801.05914).

Several endpoints would suffice:

- Strict improvement at every positive optimal \(\delta_*<1\).
- An iterable boundary map whose iterates tend to \(1/2\), with all its
  analytic hypotheses preserved at every stage.
- Direct exclusion of every zero to the right of \(1/2\), with complete
  height coverage and rigorous arithmetic bounds.
- Exclusion of positive Newman time by a zeta-specific property.

For a general map, pointwise \(F(B)<B\) alone is not a convergence proof.
Sufficient controls include continuity and strictness on \((1/2,B_0]\),
or a positive lower bound on improvement on each compact interval away
from \(1/2\). Constants may depend on the iteration: each fixed stage must
be valid, but one estimate uniform in the iteration number is not
automatically necessary. Within a stage all target/profile quantifiers matter.

## 4. Route A: the nearest explicit mixed character sum

### A1. The remaining object

Let \(\mathcal C\) be the full fixed buffered zero/profile bin, defined
before selecting the witnesses under consideration. The normalized factors
are \(M_r\), the actual ideal Möbius inverse polynomial of length \(D=U^r\);
\(S_m\), the plain polynomial of length \(N=U^m\); and \(Q_I\), a product
of whole prime slots of total length \(U^z\). All use the same character
\(\psi_u(\mathfrak n)=\nu(\mathfrak n)\chi_{\mathfrak n}(u)^{s_\chi}\),
with a common orientation \(s_\chi=\pm1\) and all zero extensions retained.
The inverse profile retains its cutoff. The prime slots are the original
physical smooth annuli, bounded in number and with disjoint supports.

The hard box is

\[
9/25\le d\le21/50,\quad49/100\le x\le1/2,\quad
7/10\le r\le37/50,\quad9/25\le m\le1/2,                   \tag{2}
\]

with nearly saturated amplitude profiles and prime length just below
\((1-r)/2\). The inverse capacities \(r+2z<1\), \(2r+8z<3\) require
positive margins. The new target is

\[
\mathcal E_{\mathcal C}:=\sum_{u\in\mathcal C}|M_rS_mQ_I|^2
\ll U^{1+dm-\eta+\varepsilon}(1+T_1)^A,\qquad\eta=1/5000. \tag{3}
\]

Set \(\gamma=1/6250\), \(K=1+dm-\eta\), and

\[
\mathcal C_+=\{u\in\mathcal C:Q_{\psi_u}>U^{2m-1/1000}\},
\quad v_{\rm pl}=2dm-2(\eta+\gamma),
\]
\[
R_0=9/8-23d/20,\qquad
\tau_0=2(1+dm-\eta-\gamma-R_0).                            \tag{4}
\]

The latest reduction proves

\[
\mathcal E_{\mathcal C}=\Re T_{\rm joint}
+O_\varepsilon(U^{K-\gamma+\varepsilon}(1+T_1)^A).        \tag{5}
\]

For a tuple \(\mathbf t=(\mathfrak d,\mathfrak k,(\mathfrak p_i))\), put
\(n(\mathbf t)=\mathfrak d\mathfrak k\prod_i\mathfrak p_i\),
\(X_{\rm col}=DN\prod_iP_i\), and

\[
b(\mathbf t)=\mu_K(\mathfrak d)\nu(n(\mathbf t))
A(N\mathfrak d/D)B(N\mathfrak k/N)
\prod_i a_i(\mathfrak p_i)W_i(N\mathfrak p_i/P_i).
\]

The exact remaining sum is

\[
T_{\rm joint}=X_{\rm col}^{-1}
\sum_{\substack{\mathbf t,\mathbf t'\\
Nf(n,n')>U^{\tau_0}\\
Nf_{\rm pl}(\mathfrak k,\mathfrak k')>U^{v_{\rm pl}}}}
b(\mathbf t)\overline{b(\mathbf t')}
\sum_{u\in\mathcal C_+}\chi_{c(n,n')}(u)^{s_\chi}
\mathbf1_{(u,E(n,n'))=1}.                                \tag{6}
\]

The local exponents of \(c\) are valuation differences modulo six, in
\(\{0,\ldots,5\}\); \(f=\operatorname{rad}c\). The extra mask \(E\)
contains primes dividing \(nn'\) whose phase difference is zero modulo
six. For example \(n=p^6,n'=1\) gives \(\mathbf1_{p\nmid u}\), not one.
The intermediate plain-ratio expansion has its own \(c_{\rm pl}\),
\(f_{\rm pl}\), and \(E_{\rm pl}\). There is no general divisibility
relation between \(f_{\rm pl}\) and \(f\). The primitive row conductor
\(Q_{\psi_u}\) is a third distinct quantity.

The proof first removes low row conductors; then expands only the plain
factor against the positive weight
\(\mathbf1_{\mathcal C_+}|M_rQ_I|^2\); then expands the remaining factors.
The pair bound
\(\#\{n,n':Nn,Nn'\ll Y,\ Nf(n,n')\le V\}\ll_\varepsilon
YV^{1/2+\varepsilon}\) pays for the two small-ratio blocks.
Changing the order can destroy the positive factorization.

Conjugate symmetry makes the whole residual real, but not every piece
positive. An upper bound for its real part, or a bound for its whole
modulus, suffices. Summing moduli term by term is stronger and discards
the cancellation this route seeks.

### A2. The actual application is narrower

The existing physical-profile subcase \(m\ge21/50\) and count-sensitive
strip \(7/10\le r\le701/1000\) miss the remaining application triangle.
Use them rather than reprove them as the main task.

Put

\[
\alpha=5/6,\ a=\alpha-d,\ B_x=2-8x/9,\ D_x=3-17x/9,\quad
P_x=B_x(1-x),\ J=aD_x+dP_x,
\]
\[
t_0=1+dP_x/(2J),\quad R^*=1-d+adP_x/(2J),\quad F=aB_x/J,
\]
\[
t_{\rm new}=t_0-B_x\eta/J,\quad
r_{\rm new}=(B_xt_{\rm new}-5x/9)/D_x-\eta/(dD_x),\quad
m_{\rm new}=t_{\rm new}-r_{\rm new}.                      \tag{7}
\]

The ideal remaining triangle is

\[
0<r-r_{\rm new}<\frac{\eta}{d(1-x)},\qquad
0<m_{\rm new}-m\le r-r_{\rm new}.                         \tag{8}
\]

Its side is between \(1/1071\) and \(1/900\), within roughly
\(.7057<r<.7296\), \(.4039<m<.4124\). Thinness in length-exponent space
does not make the physical sums short or supply a saving. The sufficient
saving can taper to

\[
s(r)=\eta-d(1-x)(r-r_{\rm new})>0.                        \tag{9}
\]

Actual witness, slot, and detector losses require the buffered region in
the energy note. If \(\ell_{\rm loss}\) bounds its specified losses, the
outer region includes

\[
r-r_{\rm new}<\frac{\eta+\ell_{\rm loss}}{d(1-x)},\quad
m_{\rm new}-m>-\frac{\ell_{\rm loss}}{dB_x},\quad
m_{\rm new}-m\le r-r_{\rm new}+\ell_{\rm loss}.            \tag{10}
\]

A theorem only on the ideal zero-loss triangle is insufficient. It must
also cover the permitted derivative profiles before the positive-norm
Sobolev step selects rowwise heights.

More precisely, set \(R_{\rm new}=R^*-F\eta\). If the actual selected
prime product has squared amplitude lower exponent \(2G_I\), its required
saving is \(s_{\rm actual}=1-R_{\rm new}-dr-2G_I\), plus witness losses.
A prime-slot length loss \(\rho_{\rm slot}\) can cost another
\(2q_{\rm bin}\rho_{\rm slot}\). The ideal taper (9) cannot replace
this actual-profile budget without checking those losses.

### A3. A refinement available before seeking cancellation

The sharper full-bin count \(R^*\le R_0\) permits the larger total cutoff

\[
\tau_*=2(1+dm-\eta-\gamma-R^*)
=\tau_0+2(R_0-R^*)\ge\tau_0.                             \tag{11}
\]

The error is unchanged, since \(R^*+\tau_*/2=K-\gamma\).
For \(0<s\le\eta\), use

\[
v_{\rm pl}(s)=2dm-2(s+\gamma),\qquad
\tau_*(s)=2(1+dm-s-\gamma-R^*).                           \tag{12}
\]

The low-row reserve remains valid because \(d/1000-s\ge\gamma\).
If operational losses require \(s>\eta\), first require \(s<d/1000\),
then choose \(0<\gamma'<d/1000-s\) and recheck the budget.
If this fails, the low-row deletion needs a stronger input.
These formulas are elementary
deductions from the existing reduction, not bounds for the complement.
First quantify their benefit on the buffered triangle.

**Next analytic tasks:** seek a selector-preserving weighted transform,
conductor reciprocity estimate, spectral inequality, or dispersion bound
for (6), with its actual coefficients. A sparse cofactor/prime
decomposition of the plain factor is another possibility, but every
recombination cost must be paid; the tested all-cofactor version fails.

**Payoff:** a full \(\eta\) saving and both witness rebalances give row
gain at least \(1091200\eta/2012413>1/10000\), with the documented small
loss reserve. The proposed boundary \(7/8-1/20000\) remains conditional;
the current candidate is \(7/8-1/24000\). Their variance exponents are
\(3/4-1/10000\) and \(3/4-1/12000\), a gain of \(1/60000\).
This would be a fixed improvement, not an RH iteration theorem.

## 5. Route B: short character families and a conditional iteration

This route has a clear algebraic path to repeated improvement, although
its missing estimate becomes substantially stronger near the endpoint.
For fixed allowed \(\nu,W\), consider the actual ideal Möbius family

\[
A_u(D)=\sum_{\mathfrak n}\mu_K(\mathfrak n)\nu(\mathfrak n)
\chi_{\mathfrak n}(u)W(N\mathfrak n/D).
\]

Suppose a new theorem supplies

\[
\sum_{0<Nu\le D^h}|A_u(D)|^2
\ll_\varepsilon D^{1+a+h+\varepsilon},\qquad a\ge0.       \tag{13}
\]

The source estimates recorded locally require \(h>1\). Restricting their
left side to fewer rows retains the old upper bound; it does not prove
(13) for \(h<1\).

Rows \(u=p^6\) replicate \(A_1\) except for columns divisible by \(p\).
With \(Np\asymp D^{h/6}\), there are \(D^{h/6+o(1)}\) repetitions.
A prior bound for the same character and profile,
\(|A_1(L)|\ll_\varepsilon L^{\theta+\varepsilon}\), gives

\[
A_1(D)-A_{p^6}(D)
=-\sum_{j\ge1}\nu(p)^jA_1(D/(Np)^j)
\ll_\varepsilon(D/Np)^{\theta+\varepsilon}.               \tag{14}
\]

Thus the conditional new exponent is

\[
B_{\rm out}=\max\left\{\frac{1+a}{2}+\frac{5h}{12},
\theta(1-h/6)\right\}.                                  \tag{15}
\]

When \(a<2\theta-1\), balancing gives

\[
h_*(\theta,a)=\frac{6(2\theta-1-a)}{5+2\theta},\qquad
T_a(\theta)=\frac{\theta(6+a)}{5+2\theta}.                 \tag{16}
\]

For \(a=0\), writing \(e=\theta-1/2>0\),

\[
T_0(\theta)-1/2=\frac{5e}{6+2e}<\frac56e.                 \tag{17}
\]

Starting at \(7/8\), the first balanced step would require \(h_*=2/3\)
and give \(7/9\). The exponents tend to \(1/2\), while the required
\(h_*\) tends to zero. Even the first short-family input is unproved;
one theorem at one fixed \(h\) does not complete the chain.

More generally, if
\(0\le a(\theta)\le\lambda(2\theta-1)\), \(0\le\lambda<1\), then

\[
T_{a(\theta)}(\theta)-1/2
\le\frac{5+\lambda}{6}(\theta-1/2).                       \tag{18}
\]

Indeed its exact excess is \([5e+a(e+1/2)]/(6+2e)\).
A fixed positive loss \(a\) stalls at \((1+a)/2\).
An estimate whose loss decreases with the current gap is therefore a
precise research target.

**A clean conditional proposition.** Fix one finite-order Hecke character
\(\nu\), excluded primes, and a class of fixed smooth annular profiles
with no common Mellin zero in \(\Re s>1/2\): for each such \(s\), some
permitted \(W\) has \(\widehat W(s)\ne0\). Fix \(0\le\lambda<1\).
Let \(P_\nu(\theta)\) mean the
bound \(A_1(D;\nu,W)\ll_{\nu,W,\theta,\varepsilon}
D^{\theta+\varepsilon}\) for every such \(W\), every \(\varepsilon>0\),
and all sufficiently large \(D\). Assume \(P_\nu(\theta_0)\) for
\(\theta_0>1/2\).
At every reached \(\theta>1/2\), suppose (13) holds for every permitted
profile and epsilon at \(h=h_*(\theta,a)\), with
\(0\le a\le\lambda(2\theta-1)\). Then
\(P_\nu(T_a(\theta))\) follows, and iteration reaches exponents arbitrarily
close to \(1/2\). The Mellin identity
\(\widehat W(s)/L_K^S(s,\nu)\), using a profile nonzero at each putative
zero, excludes zeros in \(\Re s>1/2\).

The “for every epsilon” property absorbs logarithms and finite constants
at each stage. Arbitrarily large stage-dependent thresholds are harmless:
for a fixed \(\sigma>1/2\), choose one finite stage with
\(\theta_j<\sigma\). If tracking explicit epsilon losses instead, decrease
them with the contraction margin. A single fixed epsilon creates a floor.

A stronger alternative is the scale-uniform short-family hypothesis

\[
\sum_{0<Nu\le H}\sup_{0<L\le D}|L^{-1/2}A_u(L)|^2
\ll_\varepsilon H D^{a+\varepsilon},\qquad H=D^h.         \tag{19}
\]

The existing exact sixth-power completion identity removes the omitted
prime term and gives \(B_{\rm out}=(1+a)/2+5h/12\).
Arbitrarily small positive \(h\) with loss tending to zero would reach
the endpoint directly. This is a stronger unproved input, not a source theorem.

**First bounded task:** formulate the weakest actual-coefficient theorem
needed for one step of (16), then inspect the source induction's reason
for \(h>1\). Test whether restricted families, extra bilinear structure,
or a new transform can improve that range. Arbitrary divisor-bounded
weights are not permitted: they could simply remove the Möbius signs.
Also compare other character orders or denser repeated-row sets, if a
valid family theorem and exact completion identity exist for them.
The replication gain must be balanced against their new masks and errors.

**Logical transfer to zeta:** the initial ideal Möbius bound concerns the
same Hecke function. Deriving it from a strip also needs appropriate
vertical growth of its reciprocal and a justified smooth contour shift.
For the trivial character,
\(\zeta_K(s)=\zeta(s)L(s,\chi_{-3})\). Zeta-only quasi-RH supplies no
matching control on the companion factor. Conversely, a zero-free
\(\zeta_K\) in \(\Re s>1/2\) implies RH for zeta, since the companion
does not have poles there. An all-character theorem requires the
appropriate inputs for each character, with precisely the uniformity
the proof uses.

Trivial ideal counting already gives \(P_\nu(1)\). If the new family
estimates were available along the whole chain from \(1\), the argument
would prove the endpoint without an initial quasi-RH hypothesis. This
emphasizes the strength of the missing input.

A direct integer-family version could avoid the companion-function issue,
but must be constructed. In particular \(N((d))=d^2\), and at a split
rational prime \(\mu_K((p))=+1\), whereas \(\mu(p)=-1\).
Relabeling ideal coefficients does not transfer the integer covariance.

## 6. Route C: a boundary-dependent amplification theory

Rebuild a full input-boundary/output-boundary theorem instead of repeating
the small geometry adjustment. The source uses \(B_{\rm fam}\), not
\(B_\zeta\). Its fourth moment is audited only for
\(3/4\le\kappa\le1\), with prerequisite
\(B_{\rm fam}\le(1+\kappa)/2\). An improved boundary below \(7/8\)
keeps \(\kappa=3/4\) legal; it does not authorize
\(\kappa=2B_{\rm fam}-1<3/4\).

Two specific limitations matter:

1. At fixed \(b=1/8\), the high-side obstruction is an interior bin
   \(d\approx0.386688531\), or \(a_{\rm bin}\approx0.6933442655\).
   Slightly lowering the ceiling \(d\le2B_{\rm fam}-1\) near \(3/4\)
   does not remove it. The current estimate stalls near \(0.8749572006154\).
2. The balanced low certificate is
   \(\Sigma_{\rm low}(\ell)=11/12-\ell/4+(5\ell-1)_+/8\).
   Its algebraic minimum is \(13/15\), at \(\ell=1/5\).
   Even ideal high-row counts cannot take this certificate to \(1/2\).
   This limits an upper-bound method, not the actual arithmetic sum.

The displayed signed-imbalance envelopes combine algebraically as

\[
\Sigma(\ell,\tau)=11/12-\ell/4+\tau/12+\tau_+/2
+(5\ell-1-2\tau)_+/8,\qquad\tau=M+\ell-1.                 \tag{20}
\]

Its infimum is also \(13/15\): minimize in \(\tau\) at
\((5\ell-1)/2\) for \(\ell\le1/5\), and at zero for \(\ell\ge1/5\).
The full analytic transfer on a large signed-imbalance domain has not
been audited. This is an algebraic synthesis, not a new parameter theorem.
The existing contour audit reaches only \(\Re s\ge.87\), so it does not
license using even the algebraic \(13/15\) endpoint unchanged.

A formal target for an extended fourth-moment theorem is

\[
z_P(m;\kappa)=\frac{1-2m}{6\kappa},\quad
B_\kappa=2-\frac{2x}{3\kappa},\quad
D_\kappa=3-x-\frac{2x}{3\kappa},\quad
P_\kappa=B_\kappa(1-x),
\]
\[
R_\kappa=1-d+
\frac{(\alpha-d)dP_\kappa}
{2((\alpha-d)D_\kappa+dP_\kappa)}.                        \tag{21}
\]

These specialize to current balancing formulas at \(\kappa=3/4\),
assuming admissible crossings, capacities, and prime supply. They are
not proved in a new range. At \(x=1/2\), \(B_\kappa\) vanishes at
\(\kappa=1/6\); this geometry cannot be continued unchanged to zero.
The low-side limitation remains independently present.

**First tasks:** make a ledger of every use of the family boundary, moment
range, low estimate, detector floor, contour line, Euler domain, and
prime-supply inequality. Determine the interval on which current proofs
could feed back. Then pursue an actual extension: improved low cancellation,
a larger residual coefficient induction, a different physical operation
or residue geometry, or a fourth moment below \(3/4\).
Joint optimization of \(b,\ell\) is an inexpensive diagnostic, but a tiny
certified gain should not consume the whole search for a scalable mechanism.

## 7. Route D: signed arithmetic feedback at fixed multiplicative scales

The [arithmetic note](../fixed_scale_descent/notes/ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
keeps the full von Mangoldt function and gives, at \(U=X^{11/24}\),

\[
\lambda(X)=\mathcal Q(X)+O(X^{-7/12}),\qquad
\mathcal Q(X)=\frac1{q_0X^2}
\iint_{s,t>U}M_U(s)E_U(t)\mathscr F(st/X)\,ds\,dt,
\quad q_0=7/3.                                         \tag{22}
\]

The definitions include product caps and the continuum in \(E_U\).
After multiplication by \(X^{1-\beta}\), the error is
\(O(X^{-(\beta-5/12)})\), leaving at least \(1/12\) of decay when
\(\beta\ge1/2\). Thus the comparison error permits a small gain;
the complete signed functional is the missing estimate.

Separate absolute bounds \(M_U(s)\ll s^\beta\), \(E_U(t)\ll t^\beta\)
give the old power with a logarithm. The moving-cutoff transform of the
actual functional preserves the forbidden-zero residues: it is
\(-D(z)\zeta'(z)/\zeta(z)\) plus a holomorphic error in the relevant
region. The fixed-cutoff factor
\(1-\zeta(z)\sum_{d\le U}\mu(d)d^{-z}\) equals one at a zero.
These identities expose the missing cancellation; self-substitution does
not supply it.

For \(E_\delta(X)=X^{-2-\delta}\mathcal V_g(X)\), a sufficient target is

\[
E_\delta(X)\le qE_\delta(X/b)+CX^{-\eta},
\qquad b>1,\quad0<q<1,\quad\eta>0.                       \tag{23}
\]

The [fixed-scale criterion](../fixed_scale_descent/notes/FIXED_SCALE_DESCENT_CRITERION_20261008.md)
proves every saving
\(\sigma<\min\{\delta,\eta,\log(1/q)/\log b\}\).
The recurrence must hold for all sufficiently large real \(X\).
For shell profiles \(F_X(u)=X^{-(1+\delta)/2}V_g(Xu)\), \(1\le u\le2\),
and \(\Delta_X=F_X-F_{X/b}\), the exact identity is

\[
E_\delta(X)-E_\delta(X/b)
=2\Re\langle\Delta_X,F_{X/b}\rangle+\|\Delta_X\|^2.        \tag{24}
\]

A strict decrease needs signed information about the cross term;
Cauchy alone cannot provide it. A scalar version uses
\(\lambda(X)-r c^{\beta-1}\lambda(X/c)\), whose Mellin multiplier is
\(D(z)(1-r c^{\beta-z})\). For \(0<r<1\), \(c>1\), it is nonzero in
\(\Re z>\beta+\log r/\log c\), apart from the known zeros of \(D\).
The relevant forbidden-zero residues of the prepared detector survive.
A bound must preserve that detecting power.

**First task:** expand one complete fixed-delay defect with the arithmetic
identity at both scales. Keep both moving cutoffs, continua, terminal
bands, and prime powers. Identify a bilinear or multilinear signed form
that could actually be estimated, and test it on coherent zero modes
before importing a mean square.

This route benefits from the amplification project's treatment of
selectors and signed kernels. But a family moment at row scale \(U\)
is not yet a bound for (24) at prime scale \(X\). It needs an exact bridge.

## 8. Route E: direct family bridges and common signals

### E1. Replicate the complete integer prime response

An elementary Hilbert-space criterion states the needed bridge precisely.
If \(R_X\) distinct rows satisfy \(T_u(X)=F_X+e_u(X)\), then

\[
\|F_X\|\le
\left(R_X^{-1}\sum_u\|T_u(X)\|^2\right)^{1/2}
+\left(R_X^{-1}\sum_u\|e_u(X)\|^2\right)^{1/2}.           \tag{25}
\]

Apply this to a complete prime profile or scalar delay defect only after
deriving a genuine row identity. To gain \(X^{-\eta}\), it suffices
that both averaged energies are \(O(X^{-2\eta})\) in the chosen normalization.
Count distinct repetitions and every omission. Ideal/integer Möbius
differences, continua, caps, and prime powers are part of the identity.

**First task:** attempt one explicit family lift and calculate its error
before seeking a general moment theorem. If it fails, record the precise
obstacle and compare with the indirect Hecke-to-zeta route. No reviewed
note currently supplies this complete integer-response lift.

### E2. Common-signal probes and an actual mixed energy estimate

The common-signal scout constructs \(J_j=f+E_j\) with the same **full**
signal after actual finite-prime normalization. Bounded coefficients
\(\sum_jc_j=1\) preserve it. Use the following unweighted Gram convention
so that the energy of \(\sum_jc_jR_j\) is \(c^*Gc\), even for complex
coefficients:

\[
G_{jk}=\sum_{u\in\mathcal B}\overline{R_j(u)}R_k(u).        \tag{26}
\]

The scout gives a signed prime-pair kernel for these entries.
If \(\#\mathcal B\ll U^{R+\varepsilon}\), and \(B_Z\) is the old row-size
envelope, then \(c^*Gc\ll U^{R-2\eta+\varepsilon}B_Z^2\) supplies an
\(L^1\) gain \(U^{-\eta}\). The doubled energy saving matters.
A weighted version uses nonnegative \(\lambda_u\), replaces the count
by \(\sum_u\lambda_u\), and concludes a weighted \(L^1\) estimate.
Arbitrary weights that vanish on some rows do not control the unweighted sum.

**First task:** choose a concrete admissible pair of physical profiles and
estimate a cross entry or a justified projected residual. A Schur
complement of unknown entries only renames the missing bound. Handle
singular contrast matrices by projection or justified regularization.
Keep the excluded primes, Euler correction, Gaussian, masks, full
normalizers, and differing principal remainders.

A common coherent component survives all signal-preserving combinations.
Finitely many bounded fixed filters cannot cancel a continuum of possible
modes while retaining the signal. This leaves open concentration of the
actual arithmetic modes, a growing probe family with controlled cost,
or a proved frame/observability inequality. Coefficients cannot be tuned
separately to unknown rows or zeros without paying for that choice.

A constant improvement at one scale is not a power gain. It might become
useful inside a proved recurrence across \(O(\log X)\) multiplicative steps.
This distinction connects common-signal work with Route D without claiming
that the current Gram calculation already provides such a recurrence.

### E3. Multiple cutoffs before witness selection

Use detector cutoffs \(D_{*,j}=U^{t_j}\), with fixed \(1\le t_j\le3/2\),
the same zero and presentation, and the common smoothing
\(Y_*=U^{20}\) and terminal cutoff from the joint-witness note.
These are not the selected inverse lengths \(D=U^r\).
Each complete capped detector obeys
\(T_{D_{*,j}}(\rho)=-1+o(1)\), \(j=1,2\), so their difference is \(o(1)\).
Before terminal truncation its divisor-transition coefficient is exactly
\(\sum_{\mathfrak d\mid\mathfrak n}\mu_K(\mathfrak d)
[V_\le(N\mathfrak d/D_{*,1})-V_\le(N\mathfrak d/D_{*,2})]\).
With terminal truncation retain the common terminal weight; in the two
capped dyadic expansions retain both original product caps.
This supplies compatibility, not independence.
Selected dyadic rectangles and Fourier heights may differ with the cutoff.

**First task:** derive a mixed capped kernel before selection, retaining
both height integrations, or prove a compatible selection lemma with
explicit losses. Test for a covariance identity, rigidity of nearly
saturated profiles, or amplification of an individual forbidden zero.
Multiplying marginal probabilities for two witnesses of the same zero
is unjustified. Changing a cutoff exponent is not automatically the
fixed multiplicative scale change of (23).

## 9. Route F: height-adapted detection and unbounded heights

The [spectral-edge note](../fixed_scale_descent/notes/SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md)
shows why a vanishing normalized leading term need not improve the power.
At a positive admissible exponent, little-o excludes boundary zeros but
may leave zeros approaching the boundary at unbounded height.
An abstract symmetric spectrum even admits every logarithmic saving
while retaining a positive optimal exponent. That model is not an
actual-prime, Euler-product, or full zeta-zero-density model.

Use the existing
[height-adapted project](../../prime-variance-exponents/notes/height_adapted_zero_detection/README.md)
and its newer
[Gaussian continuation](../../prime-variance-exponents/notes/height_adapted_zero_detection/gaussian_localization/README.md).
They already address clustered zeros with a finite-window detector;
do not restart by assuming an isolated or exposed zero.

The saved coefficient lower bounds cover \(\beta\in[3/4,1]\) at large
carrier height, not the whole range down to \(1/2\).
Carrier modulation changes derivative norms, normalizations, and the
continuum. A coefficient lower bound is not a response lower bound in
the presence of interfering zeros.

The Gaussian branch supplies explicit physical-window and tail budgets,
a finite signed Möbius reduction, and an improved removable small-divisor
range. Its latest
[cofactor-aware criterion](../../prime-variance-exponents/notes/height_adapted_zero_detection/gaussian_localization/COFACTOR_AWARE_SIGNED_CRITERION_20261004.md)
weakens a sufficient twisted-Möbius block input from exponent \(3/5\)
to \(13/20\), with its stated normalization and all-sample quantifiers.
That input is unproved. The
[carrier-centered reduction](../../prime-variance-exponents/notes/height_adapted_zero_detection/arithmetic_centered_at_carrier/README.md)
retains another complete Möbius/von Mangoldt spectrum.

**First tasks:** compare the actual finite coefficient classes, factor
lengths, and height costs with the character-family theorems. Derive a
legitimate transfer or state the missing moment. Alternatively prove one
complete signed block estimate directly, including terminal partial blocks
and every required carrier. Then extend the beta range and establish
height coverage for the desired boundary.

Another possibility is arithmetic compactness: force a positive spectral
supremum to be realized in a controllable height range, then combine
this with strict edge exclusion. This would be a new strong theorem;
ordinary zero density does not give it. A single exceptional zero can
invalidate RH. A large-values route must turn one forbidden zero into
enough actual weighted witnesses to contradict a count, in the correct
length/conductor/height range.

## 10. Route G: positive Newman time and collision exclusion

The [Newman scout](../newman_collisions/notes/NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md) reduces
a positive threshold to a finite real multiple zero, using the
positive-time high-real-part cutoff and zero dynamics in
[Polymath's heat-flow paper](https://arxiv.org/html/1904.12438).
Near a positive threshold, nonreal zeros remain in a compact region and
must meet the real axis at a multiple zero.

One route is therefore to rule out \(H_t(x)=H_t'(x)=0\) for real \(x\)
and \(t>0\), using arithmetic information absent from general Fourier
kernels. Another is a zeta-specific quantitative strip improvement that
cannot stall at positive time. Either would require a major new theorem.

The current analytic reductions do not suffice. Reapplying the basic
strip bound preserves the same absolute endpoint. Near a generic double
collision at \(T>0\),
\(y(t)^2=2(T-t)+O((T-t)^2)\); strict instantaneous improvement need not
force \(T=0\). The saved scout gives a positive, even, decreasing,
rapidly decaying kernel with arbitrarily narrow initial nonreal strip
and positive Newman threshold. Those properties alone are insufficient.

**First tasks:** express a collision-sensitive Wronskian, logarithmic
derivative, or local discriminant using a rigorous finite or smoothed
zeta arithmetic representation. Test whether character amplification,
theta modularity, total positivity, or a signed prime correlation
constrains its sign or vanishing. Identify the additional property
that fails in the general-kernel counterexample.

Do not treat \(H_t\), \(t>0\), as an ordinary Euler-product \(L\)-function
or apply Hecke-family bounds without a representation theorem.
Unjustified termwise heat evolution of an infinite Dirichlet series is
not such a theorem. Use effective heat-flow approximations and pay their
errors. Finite collision searches need coverage and tails for the range
they are intended to prove.

## 11. Further routes to retain in the portfolio

These are informed by existing prime-variance reductions. Read the linked
records before proposing a new version. Failure of Route A would not
eliminate these possibilities.

| Route | Concrete task and missing input | Main check |
| --- | --- | --- |
| [Signed prime-pair dispersion](../../prime-variance-exponents/notes/programs/03_signed_prime_pair_dispersion/README.md) | Estimate the complete weighted pair correlation with signs and continuum cancellation, in the detector's actual averaging range. | Include proportional shifts, caps, exceptional shifts, and the full kernel. Marginal prime bounds do not control the needed covariance. |
| [Higher multilinear identities](../../prime-variance-exponents/notes/programs/05_higher_multilinear_identities/README.md) | Use the exact higher divisor identity to expose a tractable new signed form; compare its entire error budget with the bilinear form. | More factors alone do not improve an exponent. Apply a real arithmetic estimate after the identity. |
| [Short-interval multiscale covariance](../../prime-variance-exponents/notes/programs/04_short_interval_multiscale/README.md) | Estimate a cross-scale or cross-interval covariance not supplied by individual variance bounds. | Higher-order reconstruction retains arbitrary common modes unless a new estimate controls them. |
| [Selective Sonin loss](../../prime-variance-exponents/notes/programs/02_selective_sonin_loss/README.md) | Construct an arithmetic-selective growing head with controlled mixed tail and the true inverse metric. | Fixed-rank repair and unrestricted ambient absorption have existing obstructions. Pay the growing rank and tail cost. |
| [Arithmetic approximation](../../prime-variance-exponents/notes/programs/06_arithmetic_approximation/README.md) | Build Dirichlet-polynomial or Beurling-type approximants converging in the criterion's norm, possibly using amplified cancellation. | Membership or density heuristics do not give convergence. Logarithmic norm convergence can suffice here, unlike a logarithmic variance-exponent improvement. |
| [Shifted Hermite–Biehler](../../prime-variance-exponents/notes/programs/07_shifted_hermite_biehler/README.md) | Continue the full strict kernel/ratio inequality for \(E_b(z)=\xi(b-iz)\) toward \(b=1/2\), with arithmetic control of dangerous frequencies. | Scalar positivity is weaker than the whole-frequency condition. Handle common factors and endpoint symmetry. |
| [Generalized Li positivity](../../prime-variance-exponents/notes/programs/08_generalized_li_positivity/README.md) | Control the signed prime term uniformly in all orders while moving toward the RH parameter. | Finite-order positivity does not imply all-order positivity. Retain the continuous-prime cancellation against the elementary term. |
| [Large-values detection](../../prime-variance-exponents/notes/programs/09_large_values_zero_detection/README.md) | Amplify one forbidden zero into many actual witnesses and use a moment in the correct length/height range. | Density is not exclusion. Do not transplant an estimate outside its \(N,T\) regime. |
| [Finite certificates](../../prime-variance-exponents/notes/programs/10_finite_certificates_support/README.md) | Certify compact parameter inequalities, spectral tails, or finite detector boxes supporting an analytic theorem. | Sampling is reconnaissance; finite checks do not replace the all-height or asymptotic arithmetic input. |

Another lane is independent audit of claimed implications or imported
machinery. The earlier bridge note records a claimed quasi-RH-to-RH
preprint; that check did not establish its claim. Examine exact hypotheses,
quantifiers, limiting operations, and decisive lemmas. A flawed auxiliary
lemma does not settle an entire argument if a valid replacement might
exist. Conversely, a scope statement is not independent verification of
a formal proof's dependency graph.

## 12. Failure checks shared by all routes

1. **An optimum is not a zero.** The variance optimum is attained;
   the spectral or family supremum need not be. Cover sequences at
   unbounded height and, for families, varying conductor.
2. **A real power gain.** Constant contraction under \(X\mapsto X^a\)
   may produce only logarithms. Use a valid multiplicative recurrence,
   strict boundary theorem, or complete detector exclusion.
3. **Selectors survive transforms.** A sharp exceptional indicator
   cannot be silently inserted into smooth complete-row Poisson.
   Whole positive-norm enlargement requires paying for added rows.
   Added principal sixth-power rows differ from the already controlled
   principal column-ratio contribution.
4. **Residual coefficients matter.** The inverse/plain transform contains
   \(h(tfn)\), depending on the averaged label and residual divisor.
   The imported inverse lemma excludes this additional coefficient.
   Divisor bounds do not justify signed cancellation.
5. **Actual lengths matter.** Appending the plain factor adds \(2m\) to
   the dual-row width. Near \(z=(1-r)/2-\nu\), the formal margins become
   \(2\nu-m\) and \(2r-1-2m+8\nu\), macroscopically negative in the
   target box. Cauchy may restore a coefficient class and still leave
   inadmissible widths and endpoint costs.
6. **Masks and profiles survive.** Keep zero extensions after phase
   cancellation, physical prime annuli, whole slots, fixed coefficients,
   and derivative-profile uniformity. Arbitrary prime deletion is not
   covered by a theorem for the original physical profiles.
7. **Full signed expressions survive.** An annular truncated convolution
   is not the complete identity \(\mu_K*1=\varepsilon\). Reality is not
   positivity. Separate absolute estimates may erase the useful cancellation.
8. **The signal survives.** Preserve the full normalized signal and
   forbidden-pole detector. Smallness achieved by annihilating the target
   is not a zero-free proof.
9. **Source ranges survive.** Check the field, character order, lengths,
   \(\kappa\), conductors, height seminorms, Euler domains, and contours.
   A similar formal shape is not a transfer theorem.
10. **The gain can continue.** State the map, valid interval, loss reserves,
    and limit. One fixed improvement, profile subcase, or constant Gram
    gain is not automatically iterable.

These checks diagnose particular proposals; they do not forbid new
arithmetic structures that overcome an existing limitation.

## 13. Suggested next Codex session

Begin with a dependency ledger separating inherited theorem, source
assumption, new deduction, unproved estimate, and conclusion. Check the
current repository state so concurrent work is preserved. These records
may no longer be the newest notes when the next session starts.

Run bounded lanes in parallel where useful:

1. **Concrete cancellation:** refine (6) by (11)–(12), then attempt one
   selector-preserving estimate on the buffered triangle. Deliver a
   proof, genuine subcase, or explicit residual obstruction.
2. **Scalable descent:** formulate the weakest short-family estimate for
   one step of (16), then investigate access to progressively smaller
   \(h\). Keep zeta-only and family hypotheses separate.
3. **Arithmetic bridge:** derive a complete fixed-delay or common-signal
   mixed kernel, or test one family replication of the integer response.
   Establish the identity and error budget before importing a theorem.
4. **Alternative endpoint:** pursue a height-adapted signed input or a
   zeta-specific collision quantity, so the whole program does not become
   optimization of the present \(7/8\) architecture.

A geometry or source-audit lane can replace a lane when evidence favors
it. Reassess concrete progress: a new arithmetic inequality, a weaker
sufficient input, an expanded legal range, or a rigorous obstruction that
changes the next task. Rewriting the same unresolved identity is not
itself progress toward its bound.

Use exact rational identities and continuous certificates for finite
parameter claims; floating scans find candidates. Include coherent-mode
and mask counterchecks. Reuse existing calculations rather than produce
large redundant data. Decisive external proofs or certificates need
specialist or formal validation beyond same-model review.

Save research in the relevant investigation's `<project>/notes/` folder,
using the [notes index](README.md) to select the project. Keep shared plans
and dependency records in `notes/`, calculations and small records in
`numerics/`, and reviews in `reviews/`. Link to the original projects
rather than silently revising their claims. Include model/effort metadata
honestly. Follow [LARGE_FILES.md](../../../LARGE_FILES.md).
Use the concise [DRAFT_HISTOR.md](../DRAFT_HISTOR.md) for milestones;
do not create manuscript snapshot folders. Write a manuscript only when
there is a coherent result, with authorship and LLM acknowledgement.

### Ready-to-use continuation request

> Continue the research in papers/quasi-rh-exponent-descent/ from
> notes/CODEX_CONTINUATION_20261008.md. Read the current character-amplification
> manuscript and latest selector-preserving reductions, and the relevant
> prime-variance arithmetic and height-adapted notes. Investigate broadly
> whether these mechanisms can produce exponent descent toward RH,
> an all-height detector exclusion, or exclusion of positive Newman
> collisions. Keep a localized mixed-moment lane and at least one route
> capable in principle of approaching \(1/2\), especially the conditional
> short-family map. Preserve the stated verification status of imported
> results; distinguish zeta-only quasi-RH from family hypotheses and new
> moment assumptions. Do not assume fixed improvements iterate.
> Make each transform preserve its selector, coefficients, masks, lengths,
> full signal, and error budget. Produce concrete notes with proofs or
> sharply specified missing estimates, meaningful finite checks where
> useful, and separate scoped reviews. Reassess routes as evidence changes;
> do not confine the search to a fixed-scale recurrence or the present
> \(7/8\) geometry. Preserve existing work and follow the repository's
> project notes, shared numerics/reviews, and draft-history conventions.
