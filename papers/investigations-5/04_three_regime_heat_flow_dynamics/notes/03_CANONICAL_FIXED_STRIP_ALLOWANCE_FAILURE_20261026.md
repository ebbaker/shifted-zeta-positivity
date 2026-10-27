# A canonical failure of the fixed-strip response allowance

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Status: proved in-note for the specified sufficient allowance; internal
same-model review only.** This answers the negative alternative in
[Note01 Section7][response]: an explicit growing-window implementation
fails an R11 payment. It does not exclude a canonical regime, bound an
actual multiplicity population, or acquire the true local root time caps.
The new quantities are the optimized cost (F6), its canonical exponential
lower bound (F7), and the independent source-majorant gate failure (F10).
Progress and review are in the [sole register][progress] and [Review02][review].

Read the [result index][results], [geometry cluster][geometry],
[collision controls][controls] and [avoid index][avoid]. Under
[avoid01][classify] this is a precise obstruction to a declared bound,
not an RH-equivalent criterion. [Scoped exclusions][scope],
[normalization][normalization] and [coupled accounting][coupled] govern
the claims below. The inherited response theorem remains valid.

## 1. An explicit window and the allowance being tested

Take fixed smooth functions with

\[
0\le\alpha,\beta\le1,\quad
\alpha\in C_c^\infty((1,2)),\quad
\alpha=1\text{ on }[5/4,7/4],
\]
\[
\beta\in C_c^\infty((-4,4)),\quad
\beta(y)=\beta(-y),\quad \beta=1\text{ on }[-3,3].
\]

For X>=1 set chi_X(x+iy)=alpha(x/X)beta(y),
psi_X=chi_X y^2, q_X=Delta psi_X and K_X=supp psi_X.
Work under either RH regime B or C, with the buffered local data required
by Note01. Choose its disjoint real-centered event disks with radii at most
1/4; this is possible for each fixed X, without asserting any uniform
distinct-zero gap. Grant all its root gates and remainder constants for
the purpose of testing the remaining payment.

Let A_X be any nonzero constant, independent of space and time within
this window. Put f_tau=H(-tau,.)/A_X. Let b_0>0 be any certified uniform
floor for |f_tau| on E_0=K_X minus the event disks, including time zero.
Let delta_H>0 be the declared uniform absolute error budget for the raw
field H; the normalized budget inserted in R10 is delta=delta_H/|A_X|.
Define

\[
b_H=|A_X|b_0,\qquad \eta_H=|A_X|\eta,\qquad
N_X=\sum_j\chi_X(a_j)m_j>0.
\tag{F1}
\]

All ratio claims concern N_X>0; when it is zero the R11 population ratio
is not defined. No zero locations or multiplicities are inferred from
the argument. The cutoff equals one at its central real interval.

Write E_X(tau,eta,delta) for the **right-hand side** of R11, using the
specific R8-R9 bias allowance, the R10 transfer allowance and any valid
nonnegative remainder C_X. This is a positive sufficient upper allowance
for the response error. A lower bound for E_X proves failure of this
bound to certify a limit; it is not a lower bound for the actual error.
In particular delta_H denotes the number supplied to the certificate,
not a claim that the actual field error attains that number.

## 2. A canonical floor ceiling and a source-defined count upper bound

The rectangle [5X/4,7X/4] times [-3,-2] belongs to E_0: every event disk
lies within |y|<=1/4. On the central rectangle
x in [5X/4,7X/4], |y|<=3 one has q_X=2. Thus

\[
 A_0=\operatorname{area}(E_0)\ge X/2,\quad
 \|q_X\|_\infty\ge2,\quad
 D_X=\|q_X\|_1/(4\pi)\ge X/(2\pi).
\tag{F2}
\]

The last inequality uses only the smaller plateau |y|<=1; all transition
collars are still included in the original norms.

At z_X=3X/2-3i, the canonical normalization gives

\[
 H(0,z_X)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad s=2+3iX/4.
\]

The absolutely convergent Dirichlet series gives |zeta(s)|<=zeta(2).
The exact gamma identity |Gamma(1+iv)|^2=pi v/sinh(pi v), v=3X/8,
then proves, for X>=1,

\[
 b_H\le |H(0,z_X)|\le L_X
 :=C_*X^{5/2}e^{-\kappa X},\qquad \kappa=3\pi/16,
\tag{F3}
\]
\[
 C_*:=\frac{77\pi}{1536}
 \left(\frac{3\pi}{4(1-e^{-3\pi/4})}\right)^{1/2}.
\]

Indeed |s(s-1)|<=(11X/4)(7X/4), and
sinh(pi v)>=(1-e^{-3pi/4})e^{pi v}/2. This is an exact inequality,
not a critical-strip estimate or fitted gamma envelope. The primary
identities and their checked scope are recorded in [Reference02][reference].
The pointwise upper bound itself does not require RH.

A coarse count sufficient here also follows from the complete source,
without importing a local gap or an exact zero count. Set

\[
 h_*=H(0,0)>0,\qquad S(v)=\int_0^\infty\Phi(u)e^{vu}\,du.
\]

The source representation implies max_{|z|<=r}|H(0,z)|<=S(r).
Jensen's formula therefore gives

\[
 N_X\le n_0(2X)\le
 \frac{\log(S(4X)/h_*)}{\log2}
 \le C_N X\log(2+X),
\tag{F4}
\]

where n_0 counts all endpoint zeros with multiplicity and C_N is one
fixed canonical constant. For completeness, discard the negative source
summands to obtain

\[
 \Phi(u)\le C_\Phi e^{9u-\pi e^{4u}},\quad
 C_\Phi=2\pi^2\sum_{n\ge1}n^4e^{-\pi(n^2-1)}<\infty.
\]

Changing variable e^{4u}=v yields
S(r)<=(C_Phi/4)pi^{-(r+9)/4}Gamma((r+9)/4). The usual real gamma
growth gives log S(r)=O(r log(2+r)), proving the final bound in F4.
This acquires an upper count, not individual multiplicities or an exact
contour count. The RH premise only identifies the real sites used by R11.

## 3. Optimize the regulator before testing the budget

The zero-free-remainder term of R9 and the transfer term of R10 alone
give, on putting s_eta=eta_H/b_H and r_delta=delta_H/b_H,

\[
 E_X\ge\frac{X}{8\pi\tau N_X}
 \left(s_\eta^2+\frac{2r_\delta}{s_\eta}\right).
\tag{F5}
\]

For s,r>0 the minimum of s^2+2r/s is 3r^{2/3}, attained at s=r^{1/3}.
Consequently every regulator, even one chosen after all data are known,
satisfies

\[
 \inf_{\eta>0}E_X\ge
 \frac{3X}{8\pi\tau N_X}
       \left(\frac{\delta_H}{b_H}\right)^{2/3}
 \ge\frac{3}{8\pi C_N\tau\log(2+X)}
       \left(\frac{\delta_H}{b_H}\right)^{2/3}.
\tag{F6}
\]

Every factor of |A_X| has canceled. A small constant normalization can
rescale eta and delta, but cannot improve this matched payment. The
other nonnegative R8-R11 payments can only make this particular allowance
larger. Their omission here is legitimate for a lower bound on it.

For the explicit declared raw budget delta_H=X^{-p}, any fixed p>0,
F3-F6 yield

\[
 \inf_{\eta>0}E_X\ge
 \frac{3}{8\pi C_N C_*^{2/3}}
 \frac{e^{\pi X/8}}
 {\tau X^{(2p+5)/3}\log(2+X)}\longrightarrow\infty
 \quad(X\to\infty,\ 0<\tau\le1).
\tag{F7}
\]

Thus this polynomial raw-error budget fails the specified R11 payment
for every growing height schedule with N_X>0, irrespective of eta or
constant normalization. This remains true if the root gates and remainder
are supplied for free. A provider with a much smaller actual or certified
error must insert that sharper budget instead; F7 does not say its error
is polynomially large.

A necessary condition for this allowance to tend to zero is

\[
 \frac{\delta_H}{b_H}
 =o\!\left((\tau\log(2+X))^{3/2}\right),
\quad\text{hence}\quad
 \delta_H=o\!\left(
 L_X(\tau\log(2+X))^{3/2}\right).
\tag{F8}
\]

Neither condition is sufficient: the actual b_H may be smaller than L_X,
and all the cluster terms, analytic gates and remainder still have to be
paid. In particular a Book envelope error must first be converted to its
raw absolute budget; an exponentially small raw envelope is not rejected
by the polynomial-budget conclusion.

## 4. The separate source-majorant time gate already loses fast windows

Consider specifically the elementary remainder-floor certification
proposed in Note01 Section1. Let b_init,H be a certified positive
time-zero raw floor on E_0 and use the fixed strip majorant

\[
 V_4=\int_0^\infty u^2\Phi(u)e^{4u}\,du>0.
\]

For real negative time and |y|<=4, differentiation of the unchanged
source gives |H(-sigma,z)-H(0,z)|<=sigma V_4. The sufficient condition
tau V_4<=b_init,H/2 supplies the uniform remainder floor b_init,H/2.
Since the initial floor also obeys b_init,H<=L_X, this implementation
can pass only if

\[
 \tau\le\frac{C_*}{2V_4}X^{5/2}e^{-\kappa X},
 \quad\text{equivalently}\quad
 \kappa X\le\log(1/\tau)+\tfrac52\log X
                    +\log(C_*/(2V_4)).
\tag{F9}
\]

It therefore fails eventually for

\[
 X(\tau)/\log(1/\tau)\to\infty,
 \quad\text{including } X(\tau)=\tau^{-a}\ (a>0),
\tag{F10}
\]

and for X=c log(1/tau) with c>16/(3pi). At or below the last coefficient
no successful gate is asserted. Division by a constant A_X scales the
floor and V_4 equally and leaves F9 unchanged.

This proves failure of the declared **separate global source-majorant
gate**, even before the individual-site root gates are considered. It
does not upper-bound the actual permissible time interval of the zeros.
A local bound for field change can decay with height and can avoid this
specific loss. The initial floor b_init,H and the time-uniform b_H of R9
are distinct quantities, although F3 bounds each from above.

As an exponential-order bookkeeping consequence only, write
tau=e^{-lambda X+o(X)} and delta_H=e^{-mu X+o(X)}. Passing F9 requires
lambda>=kappa. F3-F6 require mu>=kappa+3lambda/2, hence mu>=15pi/32
when both implementations are used. Equality requires the subexponential
terms, including the displayed polynomial factors, to be paid; these
necessary inequalities do not provide a sufficient schedule.

## 5. Controls, scope and the next bounded question

| Control class from the existing screen | What this result does and which canonical premise is absent |
| --- | --- |
| Hermite and close-pair heat polynomials | They retain the local response and its gap-scale restriction; they lack the unchanged xi/gamma identity used in F3. They remain the calibration for an unpaid distinct-site gate. |
| Positive atomic q and q_{T,a}, smooth-density and two-channel controls | Their shared positivity and heat equation do not provide the exact canonical completion in F3; local collision behavior is not rejected by F5-F6. |
| Euler-factor controls | Their arithmetic/completion data differ from the unchanged theta source. A similar exponential gamma envelope may still satisfy the derived bound; no failure of that envelope is claimed. |
| Weighted-square, finite-tail, reflected, primitive-compatible, finite-prime and finite-profile controls | They lack the unchanged complete canonical source/completion identity; their other preservation lists differ. The algebraic optimization itself is generic and may hold for them. |
| Theta-close multiple endpoints and the all-multiple coarse-count control | They can share the response mechanism or coarse count/floor behavior. Neither the new count upper bound nor a cost obstruction gives the missing multiplicity-sensitive canonical inequality. |

This is an analytical screen using [existing control records][controls],
not a new control computation. The specific source identity justifies the
canonical calculation; it does not make a compatible derived estimate a
collision discriminator. No regime is excluded, and no statement is made
about the signed U/R/J/Q system or a lower bound for nonreal-zero escape.

The completed bounded decision is to stop the polynomial raw-budget
implementation of R11 on these fixed-strip windows and the separate
V_4 gate at the fast schedules in F10. The next work should test a single
localized replacement: a height-decaying field-change bound and an
integrated bias/transfer estimate on the **same** window, with the actual
envelope conversion paid. Before a growing-population conclusion, it
must also acquire individual-site gates, or explicitly retain a measured
distinct-zero clearance. Merely decreasing eta, changing A_X or citing
the coarse count F4 cannot supply these inputs.

**Verification:** direct analytical derivation, separate read-only
same-model checks, and primary-source identity inspection. No research
numerics, numerical certificate, fitted law, manuscript snapshot, commit
or new scheduled work is part of this return.

[response]: 01_BUFFERED_RESPONSE_AND_RESOLUTION_20261026.md
[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[review]: ../reviews/02_CANONICAL_ALLOWANCE_FAILURE_REVIEW_20261026.md
[reference]: ../references/02_DLMF_GAMMA_AND_ZETA_IDENTITIES_20261026.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[normalization]: ../../../../avoid/08_normalization_and_constant_slips.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
