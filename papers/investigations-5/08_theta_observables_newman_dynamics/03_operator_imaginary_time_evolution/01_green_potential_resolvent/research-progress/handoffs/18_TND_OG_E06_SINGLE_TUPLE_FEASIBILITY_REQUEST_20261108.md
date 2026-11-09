# TND-OG-E06 r1 — one-tuple uniform-midpoint feasibility screen

8 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance; actual current runtime **gpt-6-astra**,
reasoning effort not exposed.

**Type E; recommend Sol6.1, at the author's selected effort. READY,
UNACTIVATED at issue.** This is the fixed execution successor selected
by B04. The [sole register](../01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns live status and [Inputs18](18_TND_OG_E06_INPUTS_20261108.json) binds
the immutable request/input versions. No field evaluator is requested.

## Question, tuple and outcomes

For **X=30, d=1/2, r=1**, can the explicit E03/E05 uniform-midpoint
certificate recipe meet a panel cap **N_cap=10^6**, with total acquisition
error at most h=m(d,r)/4? This is a calibration/cost question inside
established low-height verification, as recorded by B04 source-use09.
Do not count it as new exclusion coverage, evaluate U or set J(30)=0.

Return one of:

* **Recipe exceeds cap:** a directed lower bound proves that its specified
  required panel allowance exceeds N_cap, or a specified source/tail search
  cannot meet its allowance within its fixed cap. This stops this recipe;
  a later B05 decision must select any estimate/integration change.
* **Panel screen passes:** the displayed bounds fit N_cap and all preliminary
  source/tail searches succeed. This clears only this panel-count screen.
  A later implementation contract must still pay field construction,
  finite prime/G evaluation, arithmetic and measured runtime.
* **Inconclusive:** the fixed scalar precision/time limit cannot resolve
  a threshold. Report its exact interval and stop, without a wider run.

Do not infer that an upper-bound expression exceeding a cap proves an
actual quadrature error or the optimal algorithmic cost exceeds it.
The failure is explicitly about the specified certificate recipe.

## Fixed inputs and allowances

Use OG Note06 (6), (9), (11)–(16), (18), (20) and §8, and OG Note07
(A6)–(A7). Keep the literal finite reflected theta source and the exact
finite-source Fhat convention. HDA/RS substitution, deflation, adaptive
quadrature or a new local logarithm bound is outside this request.

Write h_a=h/2, eta_eval=h/2. The analytical allowances are
T<=h_a/6, beta<=h_a/6, E<=h_a/3. The remaining evaluation allowance
is an **interval width** eta_eval. Divide its symmetric radii into four
equal parts:
\[
e_{\rm quad}=e_{\rm node}=e_{\rm prime/G}=e_{\rm arith}
=\eta_{\rm eval}/8.
\tag{F1}
\]
Their radii sum to eta_eval/2. This is an error allocation; no evaluation
of the latter terms is performed by the cost screen.

1. Search integer **1<=R<=256** for a certified T(30,R)<=h_a/6. Use the
   first certified success; do not claim it is the minimal mathematical R
   if an earlier comparison was unresolved. If none is certified, distinguish
   a proved bound/cap failure from an unresolved interval comparison.
2. Choose integer **Q>=max(2,ceil((4/h_a)^(2/3)))**, conservatively using
   directed endpoints if necessary. Report Q and beta; do not enumerate
   primes or evaluate P_Q.
3. For v=30±(k+1/2), 0<=k<R, use the exact n_v and p_v of Note06.
   Certify the ceilings defining n_v; an unresolved ceiling at the
   arithmetic cap gives an inconclusive return. Put
   W_R=2 sum_{k=0}^{R-1}1/[16 cosh(ak)] and b=h_a/(3W_R). Set
   \[
   \delta_* = \min\{1,\min_v (M_v/2)(b/p_v)^{n_v}\}.
   \tag{F2}
   \]
   Work with logarithms. Choose a certified dyadic delta=2^(-j_delta)
   <=delta_*, using the ceiling of a directed upper bound for
   max(0,-log2 delta_*). Report that conservative choice and E(delta).
   No lower limit is imposed on delta, and no tiny number need underflow.
4. Use only the explicit source majorants from Note06 (15):
   C2bar(N)=t_N/(1-r_N), B0bar=5 C2bar(0), and
   \[
   Q_{\rm src}^{\rm bar}(V)=
   \frac{e^{-T_V}}{2\pi^{9/4}}
    (T_V^4+4T_V^3+12T_V^2+24T_V+24),
   \quad T_V=\pi e^{4V},
   \tag{F3}
   \]
   with Qsrcbar=Qsrcbar(0). Search **1<=N<=256** and **V=j/16,
   1<=j<=64** for certified
   \[
   5\mathcal B\,C2bar(N)Qsrcbar\le\delta/2,
   \qquad \mathcal B\,B0bar\,Qsrcbar(V)\le\delta/2.
   \tag{F4}
   \]
   These pay mathcal B delta_H<=delta/2 because delta_H has the factor
   1/2. Use the first certified values; distinguish nonminimal conservative
   choices. These computations use scalar majorants, not theta samples.

## Fixed integration cost expression

With W=30+R, use exactly the compact mathcal B of Note06 and the collar
bound mathcal B_c(W) in Note07 (A6). Define, using the above source
majorants,
\[
M_{\rm hat}=\mathcal B B0bar Qsrcbar/2,\qquad
L_{\rm hat}=(2\mathcal B_c+V\mathcal B)B0bar Qsrcbar/2,
\]
\[
H=\max\{|\log\delta|,|\log(M_{\rm hat}+\delta)|\},
\qquad L_g=aH/16+L_{\rm hat}/(16\delta).
\tag{F5}
\]
For N_pan uniform midpoint panels on [30−R,30+R], the stated conservative
error bound is 2R²L_g/N_pan. Thus this recipe prescribes
\[
N_{\rm req}=\left\lceil 2R^2L_g/e_{\rm quad}\right\rceil.
\tag{F6}
\]
Compute an enclosure of log2(2R²L_g/e_quad), compare it to log2(N_cap),
and only construct an actual integer panel count if it is within the cap.
Do not allocate panels or evaluate a field. Also report the sufficient
uniform node error and a resolution diagnostic
\[
e_F=8\delta e_{\rm node}/R,\qquad
b_F=\log_2(\max\{1,M_{\rm hat}\}/e_F).
\tag{F7}
\]
The positive midpoint weights sum to at most R/8, so F7 pays e_node.
b_F is a bound-based amplitude/error ratio, **not** a tested working
precision or a complete field-evaluation cost model.

Report j_delta and both terms of L_g separately. Combine them by a stable
base-two log-sum; the remaining count factor is
1+2 log2(R)−log2(e_quad). This identifies which bound a later B decision
would need to change. Do not infer a runtime from an unexecuted count.

## Finite execution and verification rules

Use directed interval/ball arithmetic, or explicit rational enclosures
for transcendental constants. Floating arithmetic alone is diagnostic
and cannot decide the certified cap comparison. Scalar arithmetic tiers
are **128, 256, 512, 1024 bits**, with no tier above 1024. Overall script
work limit **five minutes**, excluding environment setup; all searches
retain the fixed bounds above. Log-domain arithmetic is permitted and
expected. No parameter sweeps, root searches, sampling, panels or
manuscript work. No new Python package installation is implied if a
suitable local certified runtime already exists.

Before reporting, recheck the factors of 1/2 in F4, width/radius split in
F1, the 2R² midpoint coefficient, and node weights R/8. Demonstrate that
the returned directed inequalities really imply the selected outcome.
One bounded implementation or conservative-allocation correction is
allowed, recorded additively. A necessary changed local lemma, provider,
quadrature rule or numerical question stops that dependency and returns
to **TND-OG-B05** as a proposed B decision; do not execute it automatically.

Save the replayable script and small execution record in numerics, the
interpretation in notes, a proof/code-author check in reviews, the exact
return in handoffs, and update the sole register and continuation. Record
actual configuration and runtime when available, including inconclusive
or failed allowances. No favorable-value/RH claim, new known-region
certificate, provider comparison or all-center cost theorem follows.
Stop after the fixed screen and its honest outcome.
