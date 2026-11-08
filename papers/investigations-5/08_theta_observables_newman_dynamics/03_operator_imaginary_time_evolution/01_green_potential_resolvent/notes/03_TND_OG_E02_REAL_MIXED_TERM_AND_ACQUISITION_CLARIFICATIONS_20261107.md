# E02: real mixed-term verification and acquisition clarifications

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Author-selected configuration: **Sol6.1 / ultra**. Three read-only analytical assessors were explicitly dispatched as **gpt-6.1-sol / ultra**; root backend/effort were not independently exposed. These are internal shared-premise checks, not independent specialist review.

**Status: bounded E02 correction and clarification; the residual-floor theorem and its constants are unchanged.** Read this addendum with [Note02](02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_20261107.md), especially §4. Its frozen bytes, requests and input manifests are preserved. The [claim-level assessment](../reviews/01_TND_OG_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md) owns the assessment disposition.

## 1. What needed correction

Note02 §4 describes the real mixed error as \(O((\log\log N)/\sqrt{\log N})\sqrt{E_N}\) and attributes this directly to Radziwiłł v3 Lemma 13. The estimate needed by the argument is correct, but that description is not a literal account of the printed source. Printed p.15 Lemma 13 and p.16 (23) display \(E_N\), without its square root. For complex coefficients, the cancellation in (22)–(23) also needs the real part already required by Lemma 11; the two complex terms need not cancel before taking it.

The following direct calculation verifies the needed real estimate. It also uses the exact prime sum in the second directed term instead of reading the source's truncated prime-power replacement as an exact equality. This is one elementary correction cycle within E02, with no change of coefficient class, primary theorem, interval, source, observable or mechanism.

## 2. Exact real mixed term

Use Note02's definitions
\[
w_\ell=\frac{\varphi(\ell)}{\ell^2},\quad
G_N=\sum_{\ell\le N}\frac{\mu(\ell)^2}{\varphi(\ell)},\quad
z_\ell=\frac{\mu(\ell)\ell}{G_N\varphi(\ell)},\quad
e_\ell=y_\ell-z_\ell,\quad E_N=\sum_{\ell\le N}w_\ell|e_\ell|^2.
\]

Möbius inversion and \(a_1=1\) give exactly
\[
\sum_{\ell\le N}\frac{\mu(\ell)e_\ell}{\ell}=0. \tag{C1}
\]
The mixed contribution to the real quadratic form is
\[
\mathcal C_N=
2\Re\sum_{p^k\ell\le N}\frac{\log p}{p^k}w_\ell
\{z_\ell\overline{e_{p^k\ell}}+z_{p^k\ell}e_\ell\}. \tag{C2}
\]
Here \(z_\ell\) is real. Write the two sums inside \(2\Re\) as \(U_N,V_N\).

Reindexing the first by \(m=p^k\ell\), the exact identity
\(\sum_{p^k\mid m}\mu(m/p^k)\log p=-\mu(m)\log m\) gives
\[
U_N=-\frac1{G_N}\sum_{m\le N}
\frac{\mu(m)\log m}{m}\overline{e_m}. \tag{C3}
\]
In the second, \(\mu(p^k\ell)\ne0\) requires \(k=1\) and \(p\nmid\ell\). Since \(\varphi(p\ell)=(p-1)\varphi(\ell)\),
\[
V_N=-\frac1{G_N}\sum_{\ell\le N}\frac{\mu(\ell)e_\ell}{\ell}
P_\ell(N/\ell),\quad
P_\ell(x)=\sum_{\substack{p\le x\\p\nmid\ell}}\frac{\log p}{p-1}. \tag{C4}
\]
The factor \(p-1\) is retained exactly.

The same classical prime-sum estimate used in the primary §7 gives, uniformly for \(1\le\ell\le N\),
\[
P_\ell(N/\ell)=\log(N/\ell)+r_\ell,\qquad
|r_\ell|\ll\log\log(3N). \tag{C5}
\]
To see the uniformity in \(\ell\), the unrestricted sum is \(\log x+O(1)\): replacing \(1/(p-1)\) by \(1/p\) costs a convergent sum. The excluded-prime sum is \(O(\log\log(3N))\). For instance split its primes at \(Y=\log(3N)\); those below \(Y\) cost \(O(\log Y)\), while those above \(Y\) cost at most \(2Y^{-1}\sum_{p\mid\ell}\log p\le2\log N/Y\). Small \(N\) is absorbed into the constant. This reuses the named primary prime-sum input; it is not a new primary theorem.

Substitute (C5) into (C4) and use (C1). The remaining logarithmic main term of \(V_N\) is \(G_N^{-1}\sum\mu(\ell)\log\ell\,e_\ell/\ell\). Its sum with (C3) is purely imaginary. Therefore
\[
\mathcal C_N=-\frac2{G_N}\Re\sum_{\ell\le N}
\frac{\mu(\ell)r_\ell e_\ell}{\ell}, \tag{C6}
\]
\[
\begin{aligned}
|\mathcal C_N|
&\le\frac2{G_N}
\left(\sum_{\ell\le N}\frac{\mu(\ell)^2r_\ell^2}{\varphi(\ell)}\right)^{1/2}
E_N^{1/2}\\
&\ll\frac{\log\log(3N)}{\sqrt{G_N}}\sqrt{E_N}
\ll\frac{\log\log(3N)}{\sqrt{\log N}}\sqrt{E_N}.
\end{aligned}\tag{C7}
\]
The final asymptotic is for large \(N\), using the primary \(G_N\sim\log N\). This proves precisely the homogeneous bound needed for the **real** form. It does not assert the same small bound for the modulus of the unprojected complex mixed sum.

For any fixed \(\nu>0\), with \(S\) the primary height and \(N=\lfloor S^\theta\rfloor\),
\[
b_N\sqrt{E_N}\le\nu\log S\,E_N+
\frac{b_N^2}{4\nu\log S},\qquad
b_N\ll\frac{\log\log(3N)}{\sqrt{\log N}}. \tag{C8}
\]
The scalar remainder is \(o(1)\), uniformly in the coefficients. Together with Lemma 12's \((\log N+O(\log\log N))E_N\) and Lemma 11's \(O((\log\log N)^2)E_N\), this leaves a positive excess coefficient when \(1-\theta-\nu>0\). Thus the primary lower-bound route and Note02's arbitrary-family argument survive.

Proposition B remains the imported moment theorem. No uniform **additive** moment asymptotic for arbitrarily large forms is introduced. The inspected primary statement includes complex coefficients, coefficient growth, its relative asymptotic and its lower bound. The bad-sequence argument in Note02 §4 uses that lower bound for arbitrary admissible families with common constants. It does not identify a coefficient-independent additive error in the displayed full moment formula.

## 3. Two explicit domain conventions

For Note02 (25), choose **an integer \(M_c\ge2\)**. Then the absolute prime-power logarithm tail is bounded by
\[
\sum_{n>M_c}n^{-5/2}\le\int_{M_c}^{\infty}v^{-5/2}\,dv
=\frac23 M_c^{-3/2}.
\]
The existing acquisition prescription can always make this integer choice. Its constants, exact finite \(A(s_c)\) and denominator propagation are unchanged. This removes an implicit convention rather than claiming an integral-test bound for arbitrary noninteger cutoffs.

In Note01 §5, a distance combining the source distance and finitely many fixed-safe-line jet norms means a fixed sum, maximum or ordinary finite-dimensional norm of those seminorms, with weights independent of \(\eta\). For example
\[
D(f,g)=\left\|\frac{\Psi_f-\Psi_g}{\Psi_0}\right\|_\infty+
\sum_{r=1}^{m}c_r\sup_x
|\partial_z^{j_r}(R_f-R_g)(x+ib_r)|,\qquad c_r\ge0
\]
has \(D(f_\eta,f_0)\le C\eta\). The output remains at least \(c\sqrt\eta\), contradicting every nondecreasing modulus \(o(\sqrt t)\). Arbitrary nonlinear reparameterizations of the distance are not being covered.

## 4. Effect on the completed assessment

No conclusion or constant is weakened. Note02 (3) remains
\[
\liminf_{T\to\infty}\inf_A\frac1{|I_T|}
\int_{I_T}\epsilon_A^2\ge
\frac{1/(2\theta)-11/12}{\zeta(5/2)^4},
\]
in its frozen time-zero, fixed-\(\theta<1/2\), bounded-complex, one-polynomial, padded-interval class. Note01 §§1–5 retain their enlarged-source square-root conditioning conclusion. No lower bound on the canonical \(J_0^{\rm G}\), nonreal-zero existence, bad-center density or favorable canonical signed upper margin follows.

Classification and scope follow the [result index](../../../../../../result-summaries/README.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../avoid/README.md), especially [target01](../../../../../../avoid/01_restating_the_target.md), [controls02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [shared-premise05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md). The correction is passage-level attribution and elementary algebra; it is not a full audit of the primary mean-value theorem.
