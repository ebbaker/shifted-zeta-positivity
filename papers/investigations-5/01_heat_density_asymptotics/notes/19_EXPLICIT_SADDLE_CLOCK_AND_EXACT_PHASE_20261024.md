# An explicit saddle clock with an exact finite phase correction

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this session's metadata.

**Status: estimates proved in-note, conditional on the explicit eventual
source/collar gates of Notes 12 and 16; same-assistant assessment only.**
Exact rational controls and floating theta observations are separate
evidence. No interval-certified finite onset or all-time theorem is claimed.

This executes the explicit-formula part of [Note 18][handoff]. It replaces
the complete source mean and drift in the moving clock by the explicit
saddle, without losing Note 16's differentiated growing-window rate.
It also replaces an infinite Fourier series or a variable-length lattice
sum by **five periodic-polynomial terms** for density and six for current.
The density error becomes O(kappa^-1/2), removing the old O(L^-3) phase
allowance. The finite-time connection is treated separately in [Note 20][bridge].

This is a quantitative approximation milestone under [avoid/01][a01],
not an RH reformulation. Read the [result index][results], especially
[heat geometry][geometry] and [collision controls][controls], and the
[avoid index][avoid], especially [status][a06] and [scope][a07].

## 1. Contract and the candidate

Keep the canonical H, H_t=-H_zz, and the **positive algebraic density**
rho=q|H_z|^2/[pi(|H|^2+q)^2]. Use fixed compact spatial averaging
K=k_ell k_h, with k(s)=(315/256)(1-s^2)^4 on [-1,1], zero outside.
There is no time average in this theorem. The regulator is exactly

\[
\epsilon_+(t,x)=M_0(t)\kappa^{-1}e^{-x^2/(2\kappa)},\qquad
M_0=2\pi^2e^{tL^2+9L-\pi e^{4L}}\sqrt{2\pi/\kappa},
\tag{SC1}
\]
\[
4\pi e^{4L}=2tL+9,\quad \kappa=8tL-2t+36,
\quad L'=2L/\kappa,\quad p=\pi/L.
\]

The large positive saddle is the Lambert-W expression in Note 12 (2).
On the buffered X~kappa^(1/3) rectangle of Note 16 define

\[
\boxed{R_L(t,x,y)=k_h(y)P(p,x),\qquad
J_L(t,x,y)=-\frac2\kappa k_h(y)\{xP(p,x)-D(p,x)\}.}
\tag{SC2}
\]

Here P and D are the finite formulas in Section 3. They use L and kappa,
fixed kernel widths, and fractional parts. **No theta zeros, complete
source moments, fitted coefficients or unevaluated theta integral enter
SC2.** The error bounds use explicit complete-source majorants. J_L is a
real horizontal current, with vertical component zero.

The conclusions, in the sup norm on the buffered observation window, are

\[
\|K*\rho-R_L\|_\infty=O(\kappa^{-1/2}),
\tag{SC3}
\]
\[
\|K*\mathbf j-(J_L,0)\|_\infty+
\|\partial_t(K*\rho)-\partial_tR_L\|_\infty
=O(L\kappa^{-7/6})=o(L/\kappa).
\tag{SC4}
\]

The constant depends on the fixed widths/transverse buffer. These are
absolute errors for the unnormalized density. SC2 is nonnegative in its
density component and obeys R_L,t+partial_x J_L=0 exactly. The actual
adaptive density has Note 14's current source; its signed allowance is
already paid by Note 16. This does **not** supply an actual-theta
potential/covariance closure for SC2.

## 2. A complete-source score estimate pays the saddle substitution

Use the notation of Note 12:

\[
dP_t=M^{-1}e^{tu^2}\Phi(u)du,\quad M=H(t,0),\quad
\mu=E u,\quad v=\operatorname{Var}u,\quad \alpha=\mu'/\mu,
\]
\[
e^{tu^2}\Phi(u)=2\pi^2e^{q_t(u)}b(u),\quad
q_t(u)=tu^2+9u-\pi e^{4u}.
\]

All A_j(Y), Z_- and M_- below are the explicit complete-source
allowances of Note 12 (3)--(5), with
M_-=2pi^2 exp(q_t(L)) Z_-/sqrt(kappa). Retain that note's finite gates.
Its weighted proof applies at Y=4 as well as at the physical transverse
width; this use of 4 is a source weight, not an enlarged observation strip.

Put c=3/(2pi). On u>=0, b>=1-c>1/2 and

\[
\left|\frac{b'}b\right|\le5. \tag{SC5}
\]

For completeness, b_1'=4c exp(-4u). For n>=2 put A=exp(4u)>=1;
termwise differentiation bounds |b_n'| by
[4c n^2+4pi(n^2-1)n^4 A]exp[-pi(n^2-1)A]. Since A exp(-aA)
decreases for a>1, the supremum is at A=1. Using 3<pi<4 bounds the
tail by sum_(n>=2)(2n^2+16n^6)exp[-3(n^2-1)]. The first term is
1032 exp(-9); each subsequent ratio is less than 1/100000, using
e^3>20. Thus this tail is less than .13, |b'|<2.13, and SC5 follows.
Uniform convergence justifies the differentiated complete series.

Write zeta=u-L (a real source coordinate), d=E zeta, beta=b'/b,
and p_0=Phi(0)/M. The logarithmic derivative of the normalized source is

\[
\partial_u\log(dP_t/du)=-\kappa\zeta+E_q(\zeta)+\beta(u),
\quad |E_q(\zeta)|\le2(\kappa+2t)\zeta^2e^{4|\zeta|}.
\tag{SC6}
\]

Indeed q_t'(L+zeta)=-kappa zeta+E_q(zeta), where exactly

\[
E_q(\zeta)=-\frac{\kappa+2t}{4}
\{e^{4\zeta}-1-4\zeta\}.
\]

Taylor's exponential remainder proves SC6.

Integrating the source derivative, and then zeta times that derivative,
retains the nonzero half-line endpoint:

\[
\kappa d=E E_q+E\beta+p_0,\qquad
\kappa E\zeta^2=1-Lp_0+E(\zeta E_q)+E(\zeta\beta).
\tag{SC7}
\]

The endpoint signs follow from integral p'=-p(0) and
integral (u-L)p'=Lp(0)-1. At infinity the boundary terms vanish.
Use the explicit upper bound

\[
\overline p_0=\frac{2\pi^2 C_b e^{-\pi}}{M_-},\quad
a=1+2t/\kappa,\quad
e_s=2aA_2(4)+(5+\overline p_0)/\kappa,
\quad e=\min\{e_\mu,e_s\},
\tag{SC8}
\]
\[
E_v^s=2aA_3(4)+5A_1(0)/\kappa+L\overline p_0/\kappa+e^2,
\quad B_3^s=4\{A_3(0)+e^3A_0(0)\},
\]
\[
E_\alpha=2E_v^s+\frac{B_3^s}{L-e},\qquad L>e.
\tag{SC9}
\]

SC7, v=E zeta^2-d^2 and mu'=2mu v+m_3 give

\[
\boxed{|\mu-L|\le e=O(\kappa^{-1}),\quad
|v-\kappa^{-1}|\le E_v^s=O(\kappa^{-3/2}),\quad
|\alpha-2/\kappa|\le E_\alpha=O(\kappa^{-3/2}).}
\tag{SC10}
\]

The boundary term is smaller than any fixed inverse power of kappa.
These rates use A_j(4)=O(kappa^-j/2) and the inherited source gates.
They are sharper than the earlier sufficient O(kappa^-3/4) mean and
O(kappa^-5/4) drift allowances. No asymptotic remainder is differentiated.
This supplies the missing estimate behind Note 16's warning about
replacing alpha by 2/kappa; it does not retroactively justify the earlier
replacement without SC7--SC10.

## 3. Exact finite formula for the lattice phase

Write mathcal B_m(v)=B_m({v}), with B_m the Bernoulli polynomial and
{v} the fractional part. The standard convention is B_1(x)=x-1/2.
Set theta_-=(x-ell)/p+1/2 and theta_+=(x+ell)/p+1/2, and

\[
a_j=k_\ell^{(j)}(\ell)
=\frac{315}{256\ell^{j+1}}\sigma_j,\qquad
(\sigma_4,\sigma_5,\sigma_6,\sigma_7,\sigma_8)=(384,3840,17280,40320,40320).
\]

Other a_j used below are zero. Then

\[
\boxed{P(p,x)=\frac1p+
\sum_{j=4}^8\frac{p^j a_j}{(j+1)!}
\{\mathcal B_{j+1}(\theta_-)-(-1)^j\mathcal B_{j+1}(\theta_+)\}.}
\tag{SC11}
\]
\[
b_j=\ell a_j+j a_{j-1},\qquad
\boxed{D(p,x)=\sum_{j=4}^9\frac{p^j b_j}{(j+1)!}
\{\mathcal B_{j+1}(\theta_-)-(-1)^{j+1}\mathcal B_{j+1}(\theta_+)\}.}
\tag{SC12}
\]

These are exact identities

\[
P=\sum_{j\in\mathbb Z}k_\ell(x-d_j),\quad
D=\sum_{j\in\mathbb Z}(x-d_j)k_\ell(x-d_j),
\quad d_j=(j+1/2)p.
\tag{SC13}
\]

Every sum in SC13 is locally finite.

**Derivation.** For a polynomial f of degree d on [-ell,ell] with its
first four endpoint jets zero, repeated integration by parts gives
hat f(omega)=-sum_(j=4)^d
[f^(j)(ell)e^(-i omega ell)-f^(j)(-ell)e^(i omega ell)]/(i omega)^(j+1).
The Fourier coefficients of its p-periodization with half-step shift are
p^-1(-1)^n hat f(2pi n/p). Substitute the Bernoulli Fourier identity
[DLMF 24.8.3](https://dlmf.nist.gov/24.8.E3). The n=0 terms are 1/p for
f=k_ell and zero for f=s k_ell. Even/odd parity gives SC11--SC12.
All used series are absolutely convergent, including the endpoint
arguments, since their degrees are at least five. The formula is derived
here from a standard identity; no novelty claim is made.

P is C3 across kernel-edge crossings. Differentiation there does not
produce delta terms. Since p'=-2p/kappa,

\[
\partial_tR_L=-\frac{2p}\kappa k_h(y)P_p,
\qquad \partial_x(xP-D)=-pP_p,
\tag{SC14}
\]
which proves the exact continuity equation. There is **zero phase
truncation error**, including in this derivative. A fixed Fourier cutoff
would have needed a separate height-dependent derivative allowance.

## 4. Complete finite error ledger

Retain Note 16's root radius r_0, collar radius R_c, static regulator
error E_R(K), current error E_J(K), time-bias error E_T(K), and its
AT26 complete mean-clock errors A_J,A_T. Here A_J,A_T include root
velocity/location transfer and the respective regulator error.
All are explicit in that note; their source moments can be replaced by
the majorants in Notes 12/16. This is a ledger of inherited and new costs,
not a claim that the finite gates have been certified.

On a carrier rectangle with halfwidth X set

\[
\delta_c=Xe/L,\quad X_*=X+\delta_c,\quad
n_*=2\mu(\ell+R_c+\delta_c)/\pi+2,
\quad k_i=\|k_\ell^{(i)}\|_\infty,\ h_0=\|k_h\|_\infty.
\tag{SC15}
\]

For a completely explicit upper count replace mu by L+e_mu.
Require |x|+ell+2R_c+delta_c<X and |y|+h+2R_c<Y; the original
strict collar and derivative gates remain. These buffers cover all
actual roots and both clock labels that can enter the observation.
The matched mean-clock root c_j=(j+1/2)pi/mu and saddle-clock root
d_j satisfy |c_j-d_j|<=delta_c whenever |c_j|<=X.

The resulting bounds are

\[
\boxed{\mathcal E_R=E_R(K)+h_0 n_* k_1(r_0+\delta_c),}
\tag{SC16}
\]
\[
\boxed{\mathcal E_J=A_J+h_0n_*
\{E_\alpha X k_0+(2/\kappa)\delta_c(k_0+X_*k_1)\},}
\tag{SC17}
\]
\[
\boxed{\mathcal E_T=A_T+h_0n_*
\{E_\alpha X k_1+(2/\kappa)\delta_c(k_1+X_*k_2)\}.}
\tag{SC18}
\]

For SC16, match actual zeros to c_j and then to d_j; each kernel value
costs k_1 times its displacement. For SC17--SC18 compare
alpha c k(x-c) with (2/kappa)d k(x-d), and likewise with k'.
The drift difference costs E_alpha X k_i. The position difference costs
(2/kappa)delta_c(k_i+X_*k_(i+1)). Only n_* labels are relevant.
This also proves the bounds at kernel-edge crossings by zero extension.

At X~kappa^(1/3), the costs separate as follows:

| Cost | Density | Current or density time derivative |
| --- | --- | --- |
| Actual roots to mean clock | O(kappa^-1/2) | O(L kappa^-7/6), Note 16 |
| Mean to explicit saddle positions | O(kappa^-2/3) | O(kappa^-4/3) |
| Mean drift to 2/kappa | Not needed | O(L kappa^-7/6) |
| Adaptive regulator transfer | O(kappa^-2) | O(kappa^-5/3+L^2 kappa^-2) |
| Finite phase representation | Exactly zero | Exactly zero |

This proves SC3--SC4. The old leading mean L k_h/pi still omits a
phase term; it has not acquired the differentiated accuracy of SC2.
Potential harmonic data, actual covariance and its derivatives for the
clock remain additional obligations, not terms hidden in this ledger.

## 5. Reproducible checks and what their numbers mean

The [script][script] and [record][record] give 72 exact rational equalities
in 24 phase/width cases: SC11, SC12 and SC14 against direct finite
polynomial sums. Cases include negative centers and a root on a kernel
edge. These check constants and signs, not theta asymptotics.

Six existing Note 16 observations are reused without a numerical rerun.
Four new observations use t=3e6,3e8 and centers .37 and .83 times
(X-11), with ell=10. No parameter is fitted. The existing actual-theta
contour evaluator is refined from source order/cutoff 32/12 and contour
224 to 48/14 and contour 320, then the contour height changes .6 to .8.
Eight theta modes are retained. These new source/contour refinements are
combined; they are not separate enclosures or an independent implementation.

Across the ten observations, the largest density discrepancy divided by
L/pi is 2.702e-8. The largest derivative discrepancy divided by
2L/(pi kappa) is 3.708e-7. Omitting phase gives up to 0.003143 in the
same derivative units. Some upper-time discrepancies are only a few
times the observed refinement change. These are **floating zero-measure
observations**, not finite-epsilon peak measurements, interval errors,
uniform empirical laws or a solved trajectory.

The finite analytic time-error allowances SC18 divided by L/kappa are:

| t | Total allowance | Inherited mean-clock allowance |
| ---: | ---: | ---: |
| 1e6 | 109.78 | 106.31 |
| 1e9 | 1.975 | 1.870 |
| 1e12 | 0.03826 | 0.01768 |
| 1e18 | 0.003241 | 0.001407 |

At 1e4 the inherited collar gate fails, so no final clock error is
reported. Early passing gates do not make the error small. The new bound
is larger than the mean-clock bound because it pays for eliminating its
complete-source inputs. The gain is the explicit formula and its phase
error/rate, not an assertion that every finite constant improved.
All allowance evaluations are floating; tiny exponential tails can
underflow, and the boundary log bound is retained. No finite onset is certified.

## 6. Controls and the remaining finite-time problem

The score identity is a generic integration-by-parts fact for smooth
sources with the stated endpoints. The particular q_t, b and majorants
use the complete theta source. The required screen is:

| Control | Premise it lacks, or statement it still passes |
| --- | --- |
| Stationary sine/cosine and positive finite atoms | SC11--SC14 apply to their own clocks; the smooth canonical score and moving saddle do not apply. They must not acquire artificial motion. |
| H=z^2-2t and Hermite heat polynomials | Generic regulated equations hold through a double event; the positive theta source and eventual collar hypotheses are absent. |
| Euler-factor controls | Change the source and score; canonical b and SC8 constants cannot be assigned to them. |
| Weighted-square and finite-prime controls | Change canonical weights/full reflection; no unchanged complete-source majorants are established here. |
| Reflected, smooth-shape and positive-primitive controls | Lack the canonical square expansion; generic field stability remains valid. |
| Nearby smooth sources with the same leading tail | Can share late-time saddle/clock behavior while colliding earlier. SC3--SC4 are not an arithmetic collision discriminator. |

No existing control certificate is rerun or upgraded. A local simple-root
gate may legitimately pass a collision-free box of a control; at a
covered collision its simple-root premise fails.

The improvement advances HDA-04 and the explicit-formula part of the
all-time program. [Note 20][bridge] specifies a global regulator and a
finite-source connection with paid jet/covariance errors on compact time
slabs. Neither note proves informative overlap across the full transition,
an outer-height positive profile, or the full all-time boundary solution.
The [assessment][review] is by this same assistant. The maintained
manuscript is unchanged.

[handoff]: 18_CONTINUATION_TOWARD_EXPLICIT_ALL_TIME_APPROXIMATION_20261024.md
[bridge]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[script]: ../numerics/explicit_saddle_clock.py
[record]: ../numerics/EXPLICIT_SADDLE_CLOCK_20261024.json
[review]: ../reviews/06_EXPLICIT_CLOCK_AND_FINITE_BRIDGE_SELF_REVIEW_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
