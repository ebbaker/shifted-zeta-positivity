# First analytical round: finite walls and the arithmetic resolution gap

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from this chat's recorded turn metadata. Three separate agents of
the same model assisted the derivations; the [round review][review] is
internal LLM review, not specialist review. No priority is claimed.

**Status: finite root-wall continuation under RH proved below; exact
arithmetic control terms and scoped estimating obstructions derived.
No multiple theta zero is excluded, and RH ⇒ simplicity remains unproved.**
The [opening analysis][opening], [program][program] and [BW09 manuscript][bw09]
set the assumptions. This round follows the [result index][results],
[collision controls][controls], [local geometry][geometry], and
[avoid index][avoid], especially [reformulations][a01], [control premises][a02],
[scope][a07], [checked imports][a16], and [gain before expansion][a20].

The proposed implication is a substantial target; assuming RH supplies
useful structure but does not establish how difficult the remaining
arithmetic estimate is. The literature distinction in the opening remains
valid: [Bui–Heath-Brown](https://arxiv.org/abs/1302.5018) prove a proportion
of simple zeros under RH, while [Bui–Florea–Milinovich, §1](https://arxiv.org/html/2310.03949v1)
distinguish RH from simplicity. These are checked primary references,
not an exhaustive novelty search or a claim about the best proportion.

## 1. Contract and what this round changes

Keep the unchanged theta family and normalization
\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_t=-H_{zz},\qquad
 8H(0,z)=\xi(1/2+iz/2).
\]
Assume RH and a zero of exact order \(m\ge2\) at \((0,a)\), \(a>0\).
Put \(\gamma=a/2\). RH gives all-realness for \(t\ge0\), and local
backward splitting excludes every multiple zero at \(t>0\). These inputs
are checked against [Polymath, §1 and Proposition 3.1](https://arxiv.org/html/1904.12438v2).
Rodgers–Tao's lower threshold bound is not needed for this implication.

The primary contradiction still needs an independent cap surplus over
\((m-1)\pi\). The review found no error in BW09's orientation, ordinary
root-strip identity, or local index \(-\lfloor m/2\rfloor\). We can now
remove the finite wall-continuation obligation under assumed RH (§2).
The exact source/product calculation in §3 distinguishes the endpoint
Euler-factor control quantitatively, but does not give the missing
opposing estimate. Sections 4–5 identify precisely where two estimating
classes stop. These are partial analytical results, not completion of
RHS-02's positive acceptance gate.

## 2. Finite walls, and the phase they retain

### 2.1 Every fixed positive root label continues

The positive square expansion gives
\(0<\Phi(u)\le C e^{9u-\pi e^{4u}}\) for \(u\ge0\).
For \(|t|\le B\), absorb \(Bu^2+9u\) into
\((\pi/2)e^{4u}+C_B\). For \(r=|z|\ge4\),
\[
 |H(t,z)|\le C_B\int_0^\infty e^{ru-(\pi/2)e^{4u}}du
 \le\frac{C_B}{4}(2/\pi)^{r/4}\Gamma(r/4).
\]
Thus each entire slice has order at most one. Also \(H(t,0)>0\), and
Riemann–Lebesgue gives \(H(t,x)\to0\) as \(|x|\to\infty\).
There are infinitely many zeros: otherwise Hadamard factorization gives
an exponential times a polynomial; evenness makes the exponential
constant and the polynomial even, contradicting real-axis decay.

Under RH enumerate the simple positive-time zeros
\(0<x_1(t)<x_2(t)<\cdots\). Each fixed rank is locally analytic.
Indeed, near any \(t_0>0\), isolate the first finitely many roots in
small disjoint disks and choose a cutoff between successive roots.
Rouché's theorem and local uniform convergence retain one root in each
disk. The compact real complement from zero to the cutoff has positive
minimum modulus, so no new root appears there. All-realness makes these
roots real; \(H(t,0)>0\) prevents crossing zero. Thus the rank cannot
change locally. The pointwise \(j\)-th root is consequently one analytic
function on all of \((0,\infty)\), bounded and simple on each compact
\([\epsilon,R]\).

The \(m\) roots born from the event occupy consecutive finite ranks at
small \(\epsilon>0\). Their outer walls therefore continue to every
finite \(R\), enclosing exactly \(m-2\) roots. An adjacent subpair stays
adjacent. The positive-time physical jet is everywhere nonzero, so its
finite boundary regularity follows as well. This proves finite
continuation without a curvature floor, bounded event height, or a
presumed root chart. It gives no uniform speed or location estimate.

### 2.2 Product positivity pays exactly the baseline

At each fixed \(t\ge0\) the even paired product is
\[
 H(t,z)=H(t,0)\prod_{\lambda>0}(1-z^2/\lambda^2)^{m_\lambda},
 \qquad\sum_{\lambda>0}m_\lambda/\lambda^2<\infty.
\]
Evenness removes the remaining linear exponential. With \(f=H(t,\cdot)\)
and \(q=f'/f\), off the zeros,
\[
 q'=-\sum_{\lambda>0}m_\lambda
 \left((x-\lambda)^{-2}+(x+\lambda)^{-2}\right)<0,
 \qquad \rho:=\frac{f'^2-ff''}{f^2+f'^2}
             =\frac{-q'}{1+q^2}>0.                    \tag{1}
\]
At a positive-time simple root, \(\rho\) extends with value one.
For adjacent roots \(u<v\) and cuts \(u<c<d<v\),
\[
 M_{\rm mid}=\arctan q(c)-\arctan q(d),\qquad
 M_{\rm ends}=\pi-M_{\rm mid}.                         \tag{2}
\]
This follows by integrating \(-d(\arctan q)\), since \(q\) decreases
from \(+\infty\) to \(-\infty\) across the lobe. Thus the positive
middle phase is exactly the actual endpoint deficit. Summing \(m-1\)
lobes gives \(M_{\rm cap}=(m-1)\pi\) for the continued outer cluster.

This closes deductions from real-zero product positivity and correctly
paid endpoint/middle phases alone. It does not exclude an incompatible
estimate using additional exact arithmetic. The atomic and Euler controls
satisfy these same formulas and have multiple zero-time roots.

There is also a boundary caution. At an order-\(m\) zero,
\(q_0=m/(x-a)+O(1)\), so the formal density \(\rho_0\) has removable
limit \(1/m\), although the physical jet vanishes there. Locally,
\[
 \rho_t\,dx\ \rightharpoonup\
 \rho_0^{\rm reg}\,dx+(m-1)\pi\delta_a\quad(t\downarrow0). \tag{3}
\]
To prove this, use uniform convergence away from \(a\). Across a small
fixed interval containing only this cluster, the simple-root phase
formula adds \(m\pi\) to the arctangent endpoint difference. Integrating
the regular zero-time density on its two sides instead adds \(\pi\).
Their difference is \((m-1)\pi\); positivity proves the weak limit.
A removable density is therefore not a removal of the event's phase.

## 3. Exact arithmetic, with the control evaluated on its own data

### 3.1 A complete Poisson identity

Let \(\lambda\) run over distinct positive and negative zeta ordinates,
with multiplicities \(m_\lambda\). The paired product under RH gives
\[
 \boxed{B_\delta(\gamma):=\delta\Re\frac{\xi'}{\xi}
 (1/2+\delta+i\gamma)
 =\sum_\lambda m_\lambda
   \frac{\delta^2}{\delta^2+(\gamma-\lambda)^2}}.       \tag{4}
\]
The real-part series is absolutely convergent by the reciprocal-square
tail. Pairing about \(s=1/2\) shows there is no missing real constant.
RH is used to make all terms the stated nonnegative real kernels.
Consequently \(m(\gamma)\le B_\delta(\gamma)\).

Exact zeta arithmetic enters through the derivative of the
[completed function](https://dlmf.nist.gov/25.4.E4):
\[
 \frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
       +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s).
\]
For \(\sigma=1/2+\delta>1\), write
\[
 A(\sigma,\gamma)=\Re\left(\frac1s+\frac1{s-1}\right)
 -\tfrac12\log\pi+\tfrac12\Re\psi(s/2),\quad s=\sigma+i\gamma.
\]
Absolute convergence of the Euler product then gives the complete
**signed** identity
\[
 B_\delta(\gamma)=\delta\left[A(\sigma,\gamma)
 -\sum_{n\ge2}\Lambda(n)n^{-\sigma}\cos(\gamma\log n)\right]. \tag{5}
\]
A proved bound \(B_\delta(\gamma)<2\) excludes every multiplicity
\(m\ge2\) at that ordinate. No such all-height bound is obtained here.
Moreover \(B_\delta(\gamma)\to m(\gamma)\) as \(\delta\downarrow0\),
by isolation and dominated convergence of the other-zero terms.
Unquantified successful-scale existence at every zero is therefore
**equivalent to simplicity**, not a weaker milestone.

### Boundary maximum principle: no stronger one-point bound

20 October 2026 continuation, for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.

**Outcome.** This particular boundary maximum-principle attempt provides
no new event exclusion: its full one-point Julia inequality is exactly
Note 01's completed Poisson consumer. Positivity alone allows every
positive integer multiplicity.

Assume RH, fix an actual zero `rho=1/2+i gamma` of multiplicity `m`,
and, for `Re z>0`, define
\[
 P(z)=\frac{\xi'}{\xi}(\rho+z),\qquad
 H(z)=\frac1{P(z)}=\frac{\xi(\rho+z)}{\xi'(\rho+z)}.
 \tag{EP1}
\]
The paired product gives `Re P>0`; hence `P` has no zero and `H` is
holomorphic with `Re H>0`. Locally `xi(rho+z)=z^m a(z)`, `a(0)!=0`, so
\[
 H(z)=\frac zm+O(z^2),\qquad
 H(0)=0,\qquad \partial_x\Re H(0)=\frac1m>0.
 \tag{EP2}
\]
Thus Hopf's strictly positive inward derivative is compatible with a
double zero: the quotient has canceled the common factor of orders
`m` and `m-1`. It has a simple removable zero even when `xi` does not.
Applying Hopf directly to `log|xi|` would instead fail its finite boundary
value hypothesis, since that function is `m log|z|+O(1)`.

The stronger boundary comparison is equally explicit. Half-plane
Schwarz–Pick, applied to `H` at `z` and positive real `x`, says
\[
 \left|\frac{H(z)-H(x)}{H(z)+\overline{H(x)}}\right|^2
 \le\left|\frac{z-x}{z+x}\right|^2.
\]
Insert (EP2), expand both sides to first order in `x`, and let `x` decrease
to zero. This proves
\[
 \Re\frac1{H(z)}\ge m\Re\frac1z,
 \qquad
 m\le\delta\Re\frac{\xi'}{\xi}(\rho+\delta)
       =B_\delta(\gamma)\quad(\delta>0).
 \tag{EP3}
\]
This is exactly the already recorded bound, without an improved constant.
The left-side version `-xi(rho-z)/xi'(rho-z)` is its conjugate-reflection
and gives the same bound. The elementary maps `H(z)=z/m` attain the
general boundary inequality for arbitrary `m>0`; they are sharpness
examples for this complex-analytic comparison, not arithmetic models.

The original zeta and completed derivatives must remain distinct:
\[
 \frac{\xi'}{\xi}(s)=\frac{\zeta'}{\zeta}(s)
 +\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
 \tag{EP4}
\]
At a critical-line point where zeta is nonzero, reflection makes the left side
purely imaginary, so
\[
 \Re\frac{\zeta'}{\zeta}(1/2+it)
 =-\frac12\Re\psi(1/4+it/2)+\frac12\log\pi
 =-\frac12\log\frac{|t|}{2\pi}+O(t^{-2}).
 \tag{EP5}
\]
This excludes `zeta'=0` there at sufficiently large height, but the
quotient is undefined at a common zero. The actual order-`m` boundary
zero remains an order-`m-1` zero of `zeta'`.

The primary [Levinson–Montgomery paper, Theorem 1 and its corollary,
pp. 49 and 52](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6174-11511_2006_Article_BF02392141.pdf)
excludes derivative zeros in the **open** strip `0<Re s<1/2` under RH.
Its proof indents the critical-line zeros; it does not exclude common
zeros on that boundary. The completion in (EP4) and the
[digamma asymptotic](https://dlmf.nist.gov/5.11.E2) give (EP5) directly.

Finally, the positive coefficients of `-zeta'(s)` in `Re s>1` give
`|zeta'(sigma+it)|<=-zeta'(sigma)`, an upper bound, with no endpoint
nonvanishing consequence. Note 09 already supplies multiple-boundary-zero
controls with positive ordinary and logarithmic coefficients; their
failure of exact completion must be retained. Note 05's different
completed-source controls likewise retain their failed Dirichlet-series
premise. Neither control is being assigned unchanged zeta arithmetic.

**Scope:** the Hopf/Julia comparison and the named open-strip theorem
supply no additional opposing sign beyond `B_delta`. This assessment
does not rule out an independent signed arithmetic estimate for that
consumer or every use of derivative-zero geometry.

[Separate same-model continuation check](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).

### 3.2 The changed Euler factor contributes a mass greater than two

For the opening control let \(L=\log p\). Its completion is
\[
 \xi_p(s)=\xi(s)[1+\cosh(L(s-1/2))]
 =\tfrac12p^{s-1/2}\xi(s)(1+p^{1/2-s})^2.
\]
Its own product/arithmetic identity gives exactly
\[
 B_{\delta,p}-B_\delta
 =\delta L\frac{\sinh(\delta L)}
                  {\cosh(\delta L)+\cos(\gamma L)}>0.    \tag{6}
\]
At its added double zeros \(\gamma_k=(2k+1)\pi/L\),
\[
 \boxed{B_{\delta,p}(\gamma_k)-B_\delta(\gamma_k)
 =\delta L\coth(\delta L/2)>2},\qquad
 \lim_{\delta\downarrow0}(B_{\delta,p}-B_\delta)=2.        \tag{7}
\]
The inequality follows from \(x\coth x>1\). Coincident base zeros add
their multiplicities; no noncoincidence assumption is used.

The change in completed logarithmic derivative is
\(L-2Lq/(1+q)\), \(q=p^{1/2-s}\). At \(\gamma_k\) it equals
\(L+2L/(e^{\delta L}-1)\). The smooth conductor contribution
\(\delta L\) tends to zero; the changed Euler factor supplies the
limiting mass two. Naming conductor one alone misses the load-bearing
term. In \(-D_p'/D_p\), where \(D_p=\zeta(s)(1+\sqrt p\,p^{-s})^2\),
the coefficient at \(p^k\) is
\[
 L[1+2(-1)^{k-1}p^{k/2}].                               \tag{8}
\]
It is negative at \(p^2\), unlike zeta's von Mangoldt coefficients.
This is an exact arithmetic distinction. Its conversion to a strict
multiplicity, phase, or Gaussian estimate remains unproved.

## 4. Two precise arithmetic obstructions

### 4.1 The absolute-prime upper envelope fails uniformly

Declare the estimating class: keep \(A\) exactly, replace the signed
sum in (5) by its absolute sum
\(C(\sigma)=-\zeta'(\sigma)/\zeta(\sigma)>0\), and use
\[
 B_\delta\le U_\sigma:=(\sigma-1/2)[A+C].
\]
For \(\Re z>0\), first Euler–Maclaurin summation of the defining
reciprocal sum for the digamma function yields
\[
 \psi(z)=\log z-\frac1{2z}
       +\int_0^\infty\frac{\{u\}-1/2}{(z+u)^2}du.
\]
For \(z=x+iy\), \(x,y>0\), the integral has modulus at most
\(\pi/(4y)\), and \(\Re(1/(2z))\le1/(4y)\). Therefore
\[
 \Re\psi(\sigma/2+i\gamma/2)
 \ge\log(\gamma/2)-\frac{\pi+1}{2\gamma}.
\]
The rational real parts in \(A\) are positive for \(\sigma>1\).
For \(\gamma\ge2\pi e\), its resulting lower bound is positive, and
\[
 \boxed{\inf_{\sigma>1}U_\sigma(\gamma)
 \ge\frac14\log\frac\gamma{2\pi}
         -\frac{\pi+1}{8\gamma}\longrightarrow\infty.}  \tag{9}
\]
In particular this envelope is greater than two for every \(\sigma>1\)
when \(\gamma\ge2\pi e^9\). The explicit threshold is convenient,
not optimized. Nonnegative normalized averages of these envelopes
also fail there. Signed scale combinations, certified subtraction of
other zeros, and other test kernels are outside this assertion.

### 4.2 Even the exact fixed-width consumer fails at high height

Under RH, the classical local zero count is
\[
 N(\gamma+1/2)-N(\gamma-1/2)
 =\frac1{2\pi}\log\gamma
       +O(\log\gamma/\log\log\gamma).
\]
This is [Goldston–Gonek, equation (4)](https://arxiv.org/pdf/math/0511092),
with a fixed interval of length one. Endpoint conventions are covered
by the same error term. Each zero in the closed interval contributes
at least \(1/2\) to (4) whenever \(\delta\ge1/2\). Hence
\[
 \boxed{B_\delta(\gamma)
 \ge(1/(4\pi)+o(1))\log\gamma\longrightarrow\infty}
 \quad\text{uniformly for }\delta\ge1/2.                \tag{10}
\]
Thus the **un-deflated one-point condition** \(B_\delta<2\) cannot
hold at all high zeros in that resolution range, even with exact signed
arithmetic. It counts too many neighboring zeros. Every other fixed
lower resolution \(\delta\ge\delta_0>0\) has the analogous obstruction.
This is a restriction of this particular consumer, not a no-go theorem
for signed prime information or the wider simplicity program.

The displayed elementary definition of \(A(\sigma,\gamma)\) also applies
for \(\sigma>1/2\) at \(\gamma>0\); only its Euler series was restricted
to \(\sigma>1\). An illustrative shrinking rule is \(\delta=c/\log\gamma\), for which
\(\delta A=c/2+O(1/\log\gamma)\). It leaves the missing obligation
\[
 \delta\Re\frac{\zeta'}{\zeta}(1/2+\delta+i\gamma)
       <2-\delta A.                                    \tag{11}
\]
This specification is not an estimate. Formula (5)'s prime series does
not converge absolutely in this range; analytically continuing zeta
does not justify termwise continuation. A different justified explicit
formula must pay all its terms. The companion [finite-prime test][fejer]
examines one such next step without assuming its desired sign.

## 5. Gaussian comparison: RH strengthens the compatible sign

Write \(F=H(0,\cdot)\), \(h_j=F^{(j)}(a)\),
\(G_s(y)=(4\pi s)^{-1/2}e^{-y^2/(4s)}\), and
\(D_s=s\int G_s H_x(s,a+y)^2-\int G_s H(s,a+y)^2\).
The exact time-zero source kernel is
\[
 D_s=\frac12\iint\Phi(u)\Phi(v)
 \big[(suv-1)e^{2suv}\cos(a(u-v))
 -(suv+1)e^{-2suv}\cos(a(u+v))\big]du\,dv.             \tag{12}
\]
All interchanges converge absolutely because
\(e^{2suv}\le e^{s(u^2+v^2)}\) and the source decays doubly
exponentially. Expanding hyperbolic functions retains exactly the two
event cancellations:
\[
 D_s=-h_0^2-sh_1^2+R_s,\qquad
 R_s=\sum_{n\ge3}\frac{n-2}{2}\frac{(2s)^n}{n!}h_n^2\ge0. \tag{13}
\]
For clarity the even and odd residual kernels, with \(q=2suv\), are
\((q/2)\sinh q-\cosh q+1\) and
\((q/2)\cosh q-\sinh q+q/2\). Their positive power-series coefficients
integrate to squares; pointwise positivity of the oscillatory integrand
is not asserted. At an event, equality \(R_s=0\) would make \(F\) a
quadratic polynomial, impossible for the nonzero decaying theta slice.

For an exact double zero under RH, set
\(g(x)=F(x)/(x-a)^2\), \(L=g'(a)/g(a)\), and
\(S=-(\log|g|)''(a)\). Deflating the real-zero product gives
\[
 S=\sum_{r\ne a}\frac{m_r}{(a-r)^2}\ge\frac1{2a^2},
 \qquad h_3=3h_2L,\qquad h_4=6h_2(L^2-S).
\]
The floor comes from the double root at \(-a\). The first two terms
of (13) yield
\[
 \frac{D_s}{h_2^2}\ge6s^3L^2+24s^4(L^2-S)^2,
 \qquad
 \boxed{D_s\ge6s^4h_2^2/a^4\quad(0<s\le a^2/4).}     \tag{14}
\]
For the second inequality minimize over \(v=L^2\ge0\) and
\(S\ge b=1/(2a^2)\). On \(v\le b\), the minimum is at \(S=b,v=0\)
when \(8sb\le1\); on \(v\ge b\), the first term already suffices.
For exact multiplicity \(m\ge3\), (13) directly gives
\(D_s\ge[(m-2)/2](2s)^m h_m^2/m!>0\). All multiplicities are thus
covered by an event-compatible positive sign. No absolute floor for
\(h_m\) is available.

The Euler control satisfies these same bounds on its own data.
At \(a=(2k+1)\pi/b_p\), \(b_p=\tfrac12\log p\), with \(F(a)\ne0\),
\[
 c_2=b_p^2F(a),\quad c_3=3b_p^2F'(a),\quad
 c_4=6b_p^2F''(a)-b_p^4F(a),
\]
\[
 S_p=\sum_{\text{theta roots }r}\frac{m_r}{(a-r)^2}
                      +b_p^2/6>0.                       \tag{15}
\]
If \(F(a)\) has order \(r\ge1\), the control instead has order
\(r+2\), and the preceding higher-multiplicity bound applies.
The atomic control gives \(D_s=1+s\sinh(2s)-\cosh(2s)>0\);
the quadratic gives zero and \(P_4\) gives \(384s^4\).
These are exact algebraic checks, not theta sign samples.

Finally, if the same available data separately give
\(h_0^2+sh_1^2\ge\ell\ge0\) and \(0\le R_s\le B\), the Gaussian
margin is only \(\max(0,\ell-B)\le\ell\). This estimating class cannot
improve its own direct first-jet lower bound. A new correlated bound
on the signed kernel (12), or a different cost model, is outside that
comparison. This round supplies no reason to switch to a Gaussian
numerical campaign.

## 6. Coverage, controls, and decision

The finite-wall theorem covers every finite event height, every finite
multiplicity, and every finite positive cap time **under RH**. The phase
identities have the same coverage. The arithmetic identity/control
comparison covers every ordinate and \(\delta>0\); its prime series is
restricted to \(\sigma>1\). The explicit envelope failure has the stated
high-height range, while the exact fixed-width failure is asymptotic.
None is a simplicity exclusion for any new theta event class.

| Control | Screen result and missing premise |
| --- | --- |
| Quadratic, cubic, \(P_m\) | Local index/cap and Hermite identities retained; no unchanged theta source. The quadratic lacks the positive-height mirror-root premise of (14). |
| Positive atomic family | Actual all-real endpoint and later simplicity; exact cap \(\pi\) and positive deficit. Fails continuous theta square source. |
| Euler \(c=1\) | Shares all-realness, finite walls, and Gaussian signs. Its changed coefficient/completion data give exactly (6)–(8), (15). |
| Two-event quartic | Detects a genuine later event; its first event is not an all-real initial slice. |
| Weighted-square and finite-prime families | Local events screen their shared information; full reflection fails and no all-real endpoint is supplied. |
| Reflected and positive-primitive families | Lack the unchanged normalized theta square expansion; no unproved all-real endpoint is assigned to them. |

**Decision:** the first analytical round removes a real geometric
obligation and computes the exact arithmetic control response. It stops
the specified product-only phase inference, fixed-width un-deflated
Poisson consumer, absolute-prime envelope, and separately paid Gaussian
comparison. RHS-02 still needs an opposing complete arithmetic estimate;
RHS-03 has its finite-wall subtask complete, with surplus unproved;
RHS-04 has no new exclusion coverage. RHS-05 can review this scoped
outcome, not a theorem of RH ⇒ simplicity. The [progress register][progress]
records these distinctions. No numerical sign scan or manuscript was created. The frozen
[exact algebra contract](../numerics/EXACT_ALGEBRA_CONTRACT_20261020.md) and
[replay record](../numerics/EXACT_ALGEBRA_REPLAY_20261020.json) check finite
polynomial/Hermite constants and the finite control formula in Note 02.
They are not theta zero certificates or substitutes for these proofs.

[opening]: ../brainstorm/01_RH_IMPLIES_SIMPLICITY_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[review]: ../reviews/02_FIRST_ANALYTICAL_ROUND_REVIEW_20261020.md
[fejer]: 02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
