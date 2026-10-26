# R02: every fixed fluctuation order with matched RS completion

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from rollout turn_context. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Return: HDA-R02-AN01 r1. Proved in-note from the named inputs;
same-model internal assessment only.** This round began after
[R01 Note02][r1], [Review01][review1] and its packet disposition were saved.
For every **fixed integer p>=1**, the unchanged canonical frozen model,
with `K(p)=2p` and `V=8 sqrt(2)L`, satisfies
\[
 \boxed{\|h-F^{[p,2p]}\|^{(3,1)}_{X;1,2}
       \le C_{p,r,b}X^{-(p+3/4)}}.
\tag{R2.1}
\]
The proposed exponent and RS matching are proved, without log loss.
The quantifiers are fixed p, then sufficiently large X. The integral and
all N modes remain. No order-growing or infinite-series theorem follows.
[Actual inputs][inputs] and [internal assessment][review] pin this return.
No numerical/symbolic campaign, manuscript integration or evaluated cost.

## 1. Finite coefficients and the recurrence

Keep all definitions and full buffers from R1 Sections1--3. In particular
`c_r=kappa_(r+1)/(r+1)!`, `Q_T=d+2T partial_d`, and
`|c_r|<=A D^(r-1)X^-r` simultaneously for all r>=1, proved analytically
in R1.5. Define
\[
 a_j(q)=\sum_{\substack{k_1,\ldots,k_j\ge0\\\sum r k_r=j}}
            \prod_{r=1}^j\frac{(c_rq^{r+1})^{k_r}}{k_r!},
 \quad a_0=1,\qquad P_p(q)=\sum_{j=0}^p a_j(q).
\tag{R2.2}
\]
This is a finite partition formula, with degree j+1 through 2j for j>=1.
Differentiate the **local convergent** generating function
`exp(sum_r c_r q^(r+1)s^r)` near s=0 and compare coefficients. It gives
`j a_j=sum_{r=1}^j r c_r q^(r+1)a_(j-r)`. Gaussian evolution replaces q
by Q_T; its powers commute, so this is exactly Note16's recurrence for
U_j. This justification does not assert whole-line convergence of an
infinite operator sum.

For initial coefficient bounds, grouping partitions by
`k=sum k_r` uses the finite identity
\[
 \sum_{\substack{\sum r k_r=j\\\sum k_r=k}}\frac1{\prod k_r!}
                       =\frac1{k!}{j-1\choose k-1}.
\tag{R2.3}
\]
One proof expands `(t+t^2+...)^k/k!`: the coefficient counts ordered
compositions, then divides by k!. Consequently
\[
 |a_j(q)|\le X^{-j} C_j(|q|),\quad
 C_j(x)=\sum_{k=1}^j\frac{A^kD^{j-k}}{k!}{j-1\choose k-1}x^{j+k}.
\tag{R2.4}
\]
The whole-line polynomial used by the model is finite at each p. At X>=1,
`|P_p(q)|<=H_p(|q|)`, where `H_p(x)=1+sum_{j=1}^p C_j(x)`.

## 2. Weighted Taylor remainder, with order dependence retained

Put m=p+1. For `x=|q|<=V` and `0<=s<=1`, R1.5--6 give, for every
integer r>=1,
\[
 |f^{(r)}(s)|/r!\le
  A D^{r-1}X^{-r}x^{r+1}(1-Dsx/X)^{-r-1}
 \le 2^{r+1}A D^{r-1}X^{-r}x^{r+1},
\quad |f(s)|\le1,
\tag{R2.5}
\]
where `f(s)=sum_{r>=1}c_r q^(r+1)s^r`. The analytic disk, geometric
majorant and the gates justify termwise differentiation in this local
statement. Expanding the m-th derivative of exp f by finite partitions
and using R2.3 proves
\[
 \frac{|(e^{f})^{(m)}(s)|}{m!}
   \le e X^{-m} B_m(x),\qquad
 B_m(x)=\sum_{k=1}^m
 \frac{2^{m+k}A^kD^{m-k}}{k!}{m-1\choose k-1}x^{m+k}.
\tag{R2.6}
\]
Taylor's integral remainder multiplies the supremum in R2.6 by one:
`m int_0^1(1-s)^(m-1)ds=1`. Hence
\[
 \boxed{|A(q)-P_p(q)|\le e X^{-(p+1)} B_{p+1}(|q|)}.
\tag{R2.7}
\]
This is an explicit order-dependent polynomial, not an undefined new
coefficient or formal power count. It has degrees p+2 through 2p+2.
At p=2 it reproduces R1.7. No q-power is replaced by V before integration.
The local gates `DV/X<=1/2`, `2AV^2/X<=1` are unchanged with p; the
moment constants, retained-degree tails and RS constants are not.

## 3. Arithmetic Gaussian moments and full population

The exact completed moment is
\[
 \Psi_{\lambda,m}(T,d)=e^{\lambda d+T\lambda^2}
 m!\sum_{l=0}^{\lfloor m/2\rfloor}
    \frac{T^l(d+2T\lambda)^{m-2l}}{l!(m-2l)!}.
\tag{R2.8}
\]
It follows by taking coefficients in
`exp(s(d+2T lambda)+Ts^2)`. Its shifted argument must not be declared
bounded uniformly in n before summation.

For completeness, here is a separate full **evolved** population bound
on this slab. Write `a_X=sqrt(X/(4pi))`, `v_n=log(a_X/n)`, `a0=pi/8`;
sectorial calibration gives
`lambda=-a0+epsilon i v_n/2+delta`, `|delta|<=D0/X`. At a sufficient
slope gate
\[
 2\{(D_0/X)(2a0+L/2)+D_0^2/X^2\}\le1,\quad D_0/X\le1,
\tag{R2.9}
\]
`|e^(T lambda^2)|<=exp(2a0^2+1)exp(-v_n^2/4)`. Also
`|e^(lambda d)|<=exp(R+Y)exp(Y v_n/2)` and
`(1+|lambda|)^d<=4^d(1+v_n)^d`. A shell `j<=v_n<j+1` has at most
`2a_Xe^-j` integers. With `c=(Y-1)/2`, define the explicit finite envelope
\[
 W_d=2^d+\frac{3^d}2\sum_{k=0}^d{d\choose k}
                        8^{(k+1)/2}\Gamma((k+1)/2),
\]
\[
 \Pi_d=4(4\pi)^{-1/4}4^d
 e^{R+Y+2a0^2+1+(Y+1)/2+2c_+^2}W_d.
\tag{R2.10}
\]
The shell sum is bounded by `exp(2c_+^2)W_d`, by
`cj-j^2/4<=2c_+^2-j^2/8` and comparison to Gaussian integrals over
`[j-1,j]`. Thus, with both arms included,
\[
 \sum_{\epsilon,n\le N}|b_{\epsilon n}e^{\lambda d+T\lambda^2}|
                    (1+|\lambda|)^d\le\Pi_d G(X)X^{1/4}.
\tag{R2.11}
\]
For `Z_m=m! sum_l 2^l(W+4)^(m-2l)/(l!(m-2l)!)`, R2.8 gives a summed
moment bound `Z_m Pi_m G(X)X^1/4`. Combining it with R2.4 yields the
explicit level bound
\[
 \sum_\epsilon|U_{\epsilon,j}|\le G(X)X^{1/4-j}
  \sum_{k=1}^j\frac{A^kD^{j-k}}{k!}{j-1\choose k-1}
                              Z_{j+k}\Pi_{j+k}.
\tag{R2.12}
\]
These are absolute upper bounds; no positivity, monotone error reduction
or domination of the signed field is inferred. The proof of **solution
error** uses the sharper-for-this-purpose real initial bound R1.11 and
Gaussian integration of B_m, so no logarithmic loss from shifted moments
enters R2.1. Both arguments retain the entire population.

## 4. Matching the canonical completion and complete error ledger

For arbitrary positive integer K, R1.12 and `u>=X/2` give the integrated
source error with constant
\[
 C_K=C_\Gamma\frac{2^{7/4}}7\Gamma((K+1)/2)1.1^{K+1}
                         (8\pi)^{K/2+3/4},
\tag{R2.13}
\]
and power `X^-(K/2+3/4)`. Set **K=2p**, so that the source matches the
local `X^-(p+1) X^1/4=X^-(p+3/4)` allowance. This is the smallest integer
K paying this rate by the displayed RS remainder estimate; it is not a
necessary lower bound on the actual source error. `K=2p-1` leaves that
bound at X^-(p+1/4). `Gamma(p+1/2)1.1^(2p+1)(8pi)^(p+3/4)` is retained.

Retain all real RS terms through 2p and the exact adjacent-cutoff transfer
inside the same bounded integral. At `2p<=a_min^2`, Note05's coefficient
ratio bound controls its size by `C G(u)X^-1/4`. Real partitions stay
fixed. No derivative of a coefficient, floor, partition or endpoint occurs.

Use R1.8 and R1.14 at tau=1,B=2, with polynomial evaluation notation.
For `s_p=p+3/4`, the complete normalized error table is

| Payment | Field | Direct first T |
| --- | --- | --- |
| Initial RS mismatch, K=2p | C_(2p) M_0 X^-s_p | C_(2p) M_0^t X^-s_p |
| Local weighted remainder and all modes | C_pop e B_(p+1)[M] X^-s_p | C_pop e B_(p+1)[M^t] X^-s_p |
| True moderate tail | A_mod X^(P-7/4)e^-L² | A_mod includes D_0^t |
| Artificial completed polynomial tail | A_art,p X^1/4 e^-L² | A_art,p includes D_m^t through degree 2p |
| True remote tail | A_far X^-7/4 exp(pi X/8-X²/256) | A_far includes J_0^t |

Here `A_mod,A_far` are exactly R1.15,17, and
\[
 A_{{\rm art},p}=C_{\rm pop}\max\{H_p[D],H_p[D^t]\}.
\tag{R2.14}
\]
All order dependence is a finite sum of powers, factorials, binomials and
Gamma functions. Direct local time uses moments through degree 2p+4.

Use the classical, chart, cutoff, tilt and local gates of R1.18, replace
`4<=a_min^2` by `2p<=a_min^2`, add R2.9, and replace tail absorption by
\[
 L^2\ge(P+p-1)\log X+\log^+A_{\rm mod},\quad
 L^2\ge(p+1)\log X+\log^+A_{{\rm art},p},
\]
\[
 X^2/256\ge\pi X/8+(p-1)\log X+\log^+ A_{\rm far}.
\tag{R2.15}
\]
Each tail is then <=X^-s_p for field and direct time. These are eventual
for every fixed p,r,b. Define
\[
 A_{f,p}=C_{2p}M_0+C_{\rm pop}e B_{p+1}[M]+3,\quad
 A_{t,p}=C_{2p}M_0^t+C_{\rm pop}e B_{p+1}[M^t]+3.
\tag{R2.16}
\]
A sufficient explicit majorant in R2.1 is
`C_(p,r,b)=C_chi(48 A_f,p+A_t,p)`, with C_chi from R1 Section5.
Radius-1/2 Cauchy on the full enlarged chart pays spatial derivatives
through three. Direct time comes from the differentiated kernel, and
not from differentiating R2.1. All finite U_j and the fixed Q integral
solve heat exactly, giving
\[
 (\partial_T-\partial_z^2)F^{[p,2p]}=0,\qquad
 \partial_z(\partial_T-\partial_z^2)F^{[p,2p]}=0.
\tag{R2.17}
\]
The reconstruction proof precedes the cross-check `E_T=E_zz`.

## 5. Low orders, limits, and disposition

| Comparison | Arithmetic local allowance | RS allowance | Total supported rate |
| --- | --- | --- | --- |
| Frozen p=1,K=2 | X^-7/4 | X^-7/4 | X^-7/4 |
| Frozen p=2,K=4 (R01) | X^-11/4 | X^-11/4 | X^-11/4 |
| Frozen p>=1,K=2p | X^-(p+3/4) | Same | X^-(p+3/4) |
| Older target-centered first correction, K=1 | X^-7/4 | X^-5/4 | Original X^-5/4 |

The older theorem's residual is nonzero; frozen R2.17 is exactly zero.
At the chart center its p=1 arithmetic values agree, while spatial
coefficient differentiation differs. Changing K alone explains why the
older total rate is weaker than the matched p=1 rate; no old theorem is
silently upgraded.

Preserve these failed extensions: fixed-r coefficient big-O alone would
not justify the all-order log expansion; coefficient weight alone misses
population and moments; insufficient K leaves a source floor; replacing
q by V loses unnecessary logs. Most significantly, no fixed p pays the
outer-relative allowance `X^-s_p exp(TL^2/16-pi²T/64)` at fixed T>0.
This remains an upper-bound limitation, not an actual-error lower bound.

The explicit constants and onset inequalities are not yet a theorem for
`p=p(X)`, `p->infinity`, tau->0, growing B, or convergence of an infinite
whole-line series. No cost bound for coefficient providers, quadrature,
working precision or useful evaluation follows from the finite formulas.

The [result index][results], [controls12][controls] and [avoid index][avoid]
apply as screened in R1 Section6: the canonical arithmetic/completion
premises distinguish the source, whereas heat identities also hold for
controls. This approximation theorem supplies no RH or physical-transfer
claim. The proposed rate is now established only at the stated fixed-p
scope; [avoid01][a01] and [scope07][a07] prevent promoting its quantifiers.

**Disposition — Analysis, Sol:** accept R2.1--17 with [Review02][review].
R02-AN01 r1 CLOSED; the requested fixed-order theorem Complete. Activate
R03 after saving this return, assessment and packet disposition. R03 may
consume every fixed p, with K=2p, rather than the p=2 fallback. Parent
HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

[r1]: 02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md
[review1]: ../reviews/01_FIRST_FINITE_FLUCTUATION_ASSESSMENT_20261026.md
[inputs]: ../numerics/R02_ANALYTICAL_INPUTS_20261026.json
[review]: ../reviews/02_FIXED_ORDER_HIERARCHY_ASSESSMENT_20261026.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
