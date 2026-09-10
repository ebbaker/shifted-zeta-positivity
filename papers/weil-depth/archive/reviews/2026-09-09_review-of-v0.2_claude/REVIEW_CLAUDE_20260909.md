# Review of `papers/weil-depth` — *Finite-horizon Weil coercivity and shifted-zeta contraction* (v0.2, 9 September 2026)

Reviewer: Claude (Anthropic), working from the v0.2 manuscript, `REVIEW_20260909.md`, `STATUS.md`, `CONTINUATION_WEIL_DEPTH_20260909.md`, the `numerics/` supplement and the `background/` reports, on 9 September 2026. This is a machine-assisted review with independent recomputation. It is not a human referee report and does not replace one; where I say a proof is correct I mean that I followed every step and found nothing wrong, and where I say a number is confirmed I mean I recomputed it by a route that does not share code or formulas with the package. Everything I ran is in `numerics/review_claude/` (see the appendix) so it can be replayed.

## 1. Summary of the claims

Let $Q_{0,L}$ be the Weil quadratic form on complex test functions supported in an interval of total length $L$, in the normalization of eq. (2.6) (`eq:weil`), and let $V_{\omega,L}$ be the causal finite-horizon transfer of Suzuki's shifted ratio $\xi(\tfrac12+p-\omega)/\xi(\tfrac12+p+\omega)$. The paper proves, by a computer-assisted argument that never uses zeta zeros,

* $Q_{0,L}\succeq 10^{-26}I$ for $0<L\le 9/5$ and $Q_{0,L}\succeq 10^{-34}I$ for $0<L\le\log 7$ (Theorems 1.1, 1.2, via the certified matrix inequalities of Theorems 6.1 and 6.2);
* the consequent small-shift contraction $\|V_{\omega,L}\|\le e^{-5\cdot10^{-27}\omega}$ for $0<\omega\le3\cdot10^{-14}$ (and the analogous statement at $\log 7$), with reflection-positivity and cumulative-storage corollaries;
* an exact storage factorization and a nested Schur identity as bookkeeping for a hoped-for induction in arithmetic depth, plus the (correct) remark that a sequence $L_j\to\infty$, $\omega_j\downarrow 0$ with $\|V_{\omega_j,L_j}\|\le 1$ would imply RH.

The paper is explicit that it establishes a finite-depth statement and nothing about RH or zero-free regions. I agree with that framing.

## 2. The analytic argument

I checked every displayed formula and every proof by hand. The chain is: (i) identify $Q_{0,L}$ with the central Weil form and $Q_{\omega,L}$ with the symmetric logarithmic generator of $V_{\omega,L}$ (§2–3); (ii) bound $\|Q_{\omega,L}-Q_{0,L}\|\le C_L\omega^2$ and integrate an energy identity to get contraction from coercivity (Lemma 3.2, Prop. 3.3); (iii) a lower bound for $Q_{0,L}$ on the infinite Legendre tail by fractional integration (Lemma 4.1, Prop. 4.2), with an analytic remainder for the truncated smooth profile (Lemma 4.3); (iv) an exact parity-resolved leakage identity (Lemma 5.1) feeding a Schur-complement test on two $64\times64$ matrices (Prop. 5.2). All four components are correct. Specific points:

**Normalization (eq. 2.6, Prop. 3.1).** The Dirichlet coefficients $b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega})$ are exactly those of $\zeta(\tfrac12+p-\omega)/\zeta(\tfrac12+p+\omega)$ in the Laplace variable $p$, so $B_{\omega,L}=\sum b_\omega(n)T_{\log n}$ is the correct arithmetic factor and $V_{\omega,L}=B_{\omega,L}V^\gamma_{\omega,L}$ is the compression of the full causal transfer by causality. Differentiating the finite Euler product at $\omega=0$ gives $\partial_\omega b_\omega(n)|_0=2\Lambda(n)/\sqrt n$, so the arithmetic part of $Q_0$ is $-\sum\Lambda(n)n^{-1/2}(T_{\log n}+T_{\log n}^*)$ with the right sign. For the gamma factor I rederived $2\ell'(p)$, checked that the real parts of the two pole terms cancel on the imaginary axis (leaving the multiplier $\Re\psi(\tfrac14+\tfrac{i\tau}2)-\log\pi$) while their causal kernel $4\cosh(t/2)$ yields $2|C|^2-2|S|^2$, and that the regular kernel of $-a_0^\gamma(p)-\log(2\pi/p)$ is $w(t)=(G_0(t)-1)/t$ with $G_0$ as in (4.4) and $(g_0,g_1,g_2)=(1,-7/2,-1/24)$. So (2.6) is the Weil form in the normalization $\sum_\rho|\hat f_c(\gamma_\rho)|^2$ under RH — and I confirmed this numerically against actual zeta zeros (§3 below). This was the item the package listed as its top review priority; it is right.

**Lemma 3.2 / Prop. 3.3 (shift perturbation and continuation).** The kernel $(\cosh\omega|x-y|-1)\,r(|x-y|)$ with $r(t)=e^{t/2}-e^{-5t/2}/(1-e^{-2t})$ is correct; I verified the identity $2\cosh(t/2)-e^{-t/2}/(1-e^{-2t})=r(t)$ and the inequality $e^{-5t/2}/(1-e^{-2t})\le 1/(2t)$. The displayed $C_L$ is a valid bound; it carries a spare factor of 2 in the gamma term (the Schur-test row integral of an increasing radial kernel on an interval is at most $\int_0^L$, not $2\int_0^L$, and $\cosh x-1\le\tfrac{x^2}{2}\cosh x$), so $C_{9/5}$ could be reduced from 10.30 to about 6.3 if anyone cares; it does not matter for the theorem. The Gronwall step from $\frac{d}{ds}\|V_sf\|^2=-2Q_s[V_sf]$ is fine. The regularity justification (far-right Laplace line, $|K_s(\eta+i\tau)|\le C(2+|\tau|)^{-s}$, Strichartz for the indicator on $H^r$, $r<1/2$) is a correct sketch, but it is a sketch: the sentence "The same estimates with a logarithmic factor justify the causal generator action and extension of its symmetric form identity from smooth data" is doing real work and should be expanded into a lemma with the two estimates written out. This is the one place a careful human referee will push.

**Lemma 2.2 (polynomial core).** Correct; the dilation-then-mollification argument is the standard way to get $C_c^\infty(0,L)$ as a core for a log-Sobolev form on an interval, and the $C^1\to$ form-domain continuity bounds are right. Fine as written, though a reference for the weighted-norm dilation continuity would help.

**Lemma 4.1 (fractional tail).** This is the technical heart and it is clean. I verified $I_\nu P_n(2x/L-1)=\frac{n!}{\Gamma(n+1+\nu)}x^\nu P_n^{(-\nu,\nu)}(2x/L-1)$ at $n=0,1$ by hand, the Jacobi weight $x^\nu(L-x)^{-\nu}$ (the $2^{\pm\nu}$ factors cancel), the norm $L\,\Gamma(n+1-\nu)\Gamma(n+1+\nu)/((2n+1)(n!)^2)$, and the monotonicity of $\Gamma(n+1-\nu)/\Gamma(n+1+\nu)$. Differentiating $\|(2\pi)^\nu I_\nu f\|^2\le(\pi L)^{2\nu}\frac{\Gamma(N+1-\nu)}{\Gamma(N+1+\nu)}\|f\|^2$ at $\nu=0$ gives exactly $-\Re\langle f,J_Lf\rangle\ge(\psi(N+1)-\log\pi L)\|f\|^2=(H_N-\gamma-\log\pi L)\|f\|^2$. A useful sanity check the paper could mention: the Weber–Schafheitlin integral gives the exact diagonal value $\frac1{2\pi}\int\log\frac{|\tau|}{2\pi}|\hat\phi_n|^2\,d\tau=\log2+\tfrac12(\psi(n+\tfrac12)+\psi(n+\tfrac32))-\log(\pi L)$, so the tail floor is sharp to within about $\log 2$ on single modes.

**Lemma 4.3 (profile remainder).** $G_0$ is analytic on $|z|\le 3$ (poles of $t/\sinh t$ at $\pm i\pi$), $|z/\sinh z|\le 3/\sin 3<24$ on $|z|=3$ follows from the product for $\sinh$, and $|G_0|<180<256$ there. Numerically $\sup_{|z|=3}|G_0|\approx 28.3$ and $\max_j|g_j|3^j\approx15.2$, so the majorant 256 is loose by an order of magnitude; harmless.

**Lemma 5.1 / Prop. 5.2 (parity leakage and Schur test).** $U^*=R_LUR_L$ for real causal kernels; for $R_Lf=rf$, $\|\widetilde Qf\|^2=\tfrac12\langle f,(F_r+rC_r)f\rangle$; subtracting $\|q_rf\|^2$ leaves the Gram of $(I-P)\widetilde QP_r$. The Schur argument (minimize over the tail component with $Q_0\ge a$ there) and the error budget $(|a-m|+4K)\eta+2\eta^2$ are correct, including the use of $\mathrm{tr}\,F<10^7\Rightarrow\|\widetilde UP\|<10^4$. Remark 5.3 (the sharper $\epsilon_r$) is also correct.

**Section 7.** Corollary 7.1, Prop. 7.2, the factorization (7.2) and the nested Schur identities (7.3) are all elementary and correct. The $2\times2$ counterexample is right.

**Verdict on the mathematics.** I found no error. The theorems are proved modulo two functional-analytic passages (Prop. 3.3 and the last sentence of Lemma 2.2's use in Prop. 4.2) that are stated at sketch level and should be written out in full before circulation.

## 3. Independent numerical verification

Environment: Python 3.11.15, python-flint 0.9.0, FLINT 3.6.0, mpmath 1.4.1 (the package records Python 3.12.14 / 3.10.0). Source SHA-256 hashes match `REVIEW_BUILD_RECORD.json`.

| Check | Method | Result |
|---|---|---|
| Analytic constants $a_{N,L},K_L,\eta_M,\epsilon,C_L$, chain norms, both horizons | mpmath, 60 digits, from the printed formulas, $g_j$ by Taylor expansion of $G_0$ | All agree with the manuscript and with `bounds` in the archives to every displayed digit (e.g. $a_{128,9/5}=0.69124708426711\ldots$, $C_{\log7}=13.541168\ldots$) |
| Normalization of $Q_{0,L}$ | Evaluate (2.6) for $f_c=\cos^6(\pi x/L)$, $L=9/5$, from its Fourier/kernel definition; compare with $2\sum_{\gamma>0}|\hat f_c(\gamma)|^2$ over the first 100 zeta zeros (mpmath `zetazero`) | $6.056077406\times10^{-8}$ vs $6.056077403\times10^{-8}$, relative discrepancy $6\times10^{-10}$ (my quadrature error). The form is the Weil form, exactly. |
| Head matrix $q=P\widetilde QP$ | $Q_{0,L}[\phi_n]$ from the Fourier side: exact log-part via Weber–Schafheitlin, remainder multiplier $\Re\psi(\tfrac14+\tfrac{i\tau}2)-\log\tfrac{|\tau|}{2}$ by quadrature, pole and delay terms by quadrature; no use of $U^\gamma$, $G_0$ or moment tables | Diagonal entries $n=0,1,2,3,6,10,20$ agree with the Arb head to $\le 8\times10^{-11}$ (quadrature-limited); off-parity entries enclose 0 |
| Full-output Grams $F$, $C$ | Direct quadrature of $\langle\widetilde U\phi_i,\widetilde U\phi_j\rangle$ and $\langle\widetilde U\phi_i,R\widetilde U\phi_j\rangle$ with breakpoints at $\delta_k$, $1-\delta_k$ | Entries $(0,0),(1,1),(2,2),(0,2),(1,3),(3,5),(2,8),(5,5)$ agree to at least 20 significant digits (differences $\le10^{-21}$ at 25-digit quadrature precision) |
| Full rebuild, both horizons | `certify_arb.py` from source in my container | PASS; every displayed pivot digit, bound, model error and maximum radius identical to the archived certificates (62 s and 80 s) |
| Independent implementation, both horizons | `independent_arb.py` from source | PASS; identical pivots |
| Analyzer, cross-check, review checks | `analyze_certificate.py` with the paper's shift/decay inputs; `compare_implementations.py`; `review_checks.py` | Continuation PASS with the stated rational margins; 16384/16384 entries overlap per matrix; 45 moment quadratures and 51 Euler-derivative identities PASS; all failure controls behave |
| $E_r\succeq 0$ | 80-digit eigendecomposition of the archived $E_r$ | Smallest eigenvalue $\sim-5\times10^{-82}$ (rounding), so PSD as it must be |
| Ball-LDL logic | Read `ldl()` in both implementations | Sound: strictly positive ball pivots enclose the true pivots of every symmetric matrix in the ball matrix; symmetric consistency is asserted before use |

I also confirmed the two "required tail floor" diagnostics ($0.4905447626$ / $0.4795714956$ at $9/5$; $0.5947911826$ / $0.5899173486$ at $\log7$) from the archived matrices.

**Verdict on the computation.** Reproducible bit-for-bit in a third environment, and the matrices it uses are confirmed by two routes (Fourier-side Weil form for the head; direct quadrature of the outputs for the Grams) that do not share code with the package. The residual risk is the one the package itself names: both implementations and my checks all rely on the same analytic reduction, which is why §2 matters.

## 4. What the certified numbers actually are

The floors $10^{-26}$ and $10^{-34}$ are round targets, not measurements, and the paper says nothing about how small $\lambda_{\min}(Q_{0,L})$ really is. With the same archived matrices and the package's own `validate()`, one can do much better, and one can also certify *upper* bounds: the head $q$ is the exact form on polynomials up to the profile error $\eta$, so a ball Rayleigh quotient of a rational approximation to its ground state is a rigorous upper bound. Doing both:

| Total horizon $L$ | Largest floor `validate()` certifies (bisection) | Certified upper bound (even ground state) | Paper's floor |
|---|---|---|---|
| $9/5$ | $3.34\times10^{-23}$ | $4.136\times10^{-23}$ | $10^{-26}$ |
| $\log 7$ | $1.33\times10^{-28}$ | $6.802\times10^{-28}$ | $10^{-34}$ |

So $3.3\times10^{-23}\le\lambda_{\min}(Q_{0,9/5})\le4.14\times10^{-23}$ (gap ×1.24) and $1.3\times10^{-28}\le\lambda_{\min}(Q_{0,\log7})\le6.8\times10^{-28}$ (gap ×5), and the certified shift intervals become $\omega\le2\times10^{-12}$ and $\omega\le3.7\times10^{-15}$ respectively (using $m-C_Lh^2/3\ge m/2$). The lowest head eigenvalues (80-digit diagnostics, not certified) form a strikingly regular ladder:

| Sector | $L=9/5$ | $L=\log 7$ |
|---|---|---|
| even | $4.14\times10^{-23},\ 7.2\times10^{-17},\ 1.5\times10^{-11},\ 4.0\times10^{-7},\ 2.8\times10^{-3}$ | $6.80\times10^{-28},\ 1.7\times10^{-21},\ 8.2\times10^{-16},\ 6.0\times10^{-11},\ 1.2\times10^{-6}$ |
| odd | $7.2\times10^{-20},\ 4.2\times10^{-14},\ 3.3\times10^{-9},\ 3.7\times10^{-5},\ 6.9\times10^{-2}$ | $1.6\times10^{-24},\ 1.3\times10^{-18},\ 3.2\times10^{-13},\ 8.1\times10^{-9},\ 1.1\times10^{-4}$ |

The ground state is even and simple at both horizons, with a ratio of about $10^{5.5}$–$10^{6}$ between consecutive eigenvalues, and it drops by a factor $\approx6\times10^{4}$ between $L=1.8$ and $L=\log7$. This is the Landau–Widom-type collapse that Zhu's preprint (arXiv:2608.24827) names in its title; Zhu's own certified enclosure at total length 1.6 is $8.9\times10^{-18}\le\lambda_{\min}\le2.27\times10^{-17}$. Running the unmodified builder at the intermediate logarithmic horizons (N=128, M=220, 1792 bits, about 30–80 s each) gives a certified profile:

| $L$ | active generator delays | scalar tail floor $a_{128,L}$ | certified lower bound for $\lambda_{\min}$ | certified upper bound (even ground state) | odd-sector ground state (upper bound) |
|---|---|---|---|---|---|
| $\log2=0.693$ | none | 4.067 | $1.3\times10^{-3}$ | $1.3293\times10^{-3}$ | $7.31\times10^{-2}$ |
| $\log3=1.099$ | 2 | 3.109 | $5.42\times10^{-8}$ | $5.537\times10^{-8}$ | $1.49\times10^{-5}$ |
| $\log4=1.386$ | 2, 3 | 2.235 | $7.43\times10^{-13}$ | $7.566\times10^{-13}$ | $4.77\times10^{-10}$ |
| $\log5=1.609$ | 2, 3, 4 | 1.530 | $8.9\times10^{-18}$ | $9.293\times10^{-18}$ | $9.69\times10^{-15}$ |
| $\log6=1.792$ | 2, 3, 4, 5 | 0.696 | $5.8\times10^{-23}$ | $7.328\times10^{-23}$ | $1.35\times10^{-19}$ |
| $9/5=1.8$ | 2, 3, 4, 5 | 0.691 | $3.34\times10^{-23}$ | $4.136\times10^{-23}$ | $7.22\times10^{-20}$ |
| $\log7=1.946$ | 2, 3, 4, 5 | 0.607 | $1.33\times10^{-28}$ | $6.802\times10^{-28}$ | $1.57\times10^{-24}$ |

(Lower bounds are the largest $m$ passing the package's ball-LDL test to three significant figures; upper bounds are ball Rayleigh quotients including the profile error; the earlier background certificates $5\times10^{-13}$ at $\log4$ and $10^{-18}$ at $\log5$ are superseded.) Two cross-checks fall out. The $\log 5$ row has the same active primes as Zhu's window of total length 1.6, and since $\lambda_{\min}$ is nonincreasing in $L$, it implies $\lambda_{\min}(1.6)\ge 8.9\times10^{-18}$ — the same lower bound Zhu certifies by a completely different reduction, and consistent with his upper bound $2.27\times10^{-17}$. And the slope $-\log_{10}\lambda_{\min}$ per unit $L$ steepens from about 11 (between $\log2$ and $\log3$) to about 33 (between $9/5$ and $\log7$), i.e. the decay is super-exponential, as the Landau–Widom picture predicts; Zhu's asymptotic law $-\ln\lambda_{\min}\sim2\pi^2N(T_*)/\ln N(T_*)$ with $T_*=2\pi e^{L}$ overshoots these small-$L$ values by 13–26 in the exponent, which is unsurprising for an asymptotic statement with $N(T_*)\le 8$.

Two remarks follow. First, the certified floors in the paper are within four to seven orders of magnitude of the truth, so they are not a symptom of a lossy method; the smallness is real. Second, this is why the shift intervals are what they are: $h\approx\sqrt{3m/2C_L}$ is fixed by the spectrum, and no refinement of the continuation lemma will make $3\times10^{-14}$ into something physically meaningful.

## 5. How interesting is this?

Being direct: this is a competent, carefully documented computer-assisted certificate in a small niche, not a conceptual advance, and the paper mostly knows that.

What is genuinely good. The fractional-integration tail bound (Lemma 4.1) is an elegant, quotable tool: a one-line lower bound for the log-Sobolev part of the Weil form on the orthogonal complement of the first $N$ Legendre polynomials, sharp to within $\log 2$. The exact parity-resolved leakage (Lemma 5.1) is a sensible reduction that a naive full-Gram approach would miss. The certificate extends the rigorously certified window from total length 1.6 (Zhu, August 2026, with primes 2, 3, 4 active) to $\log 7\approx1.946$, which is the first certificate that includes the prime 5 and the first mixed composition $6=2\cdot3$ in the transfer. The engineering is unusually clean for this genre: exact rationals for every coefficient, Arb throughout, outward serialization, replay, hash binding, a second implementation, negative controls. If I were refereeing for a computational journal I would be satisfied on reproducibility.

What limits the interest. Weil positivity on a window of total length $L$ is a finite statement, and under RH it holds with a constant that decays like the ground energy of a time–frequency limiting problem — Zhu's abstract states that under RH $\lambda_{\min}\le\exp(-\ell e^{\ell})$ for large half-width $\ell=L/2$. Zhu also argues, and the paper's own tail floor shows the same thing, that any "one-stroke" certificate must resolve doubly-exponentially many frequencies. Concretely, the scalar tail floor (4.6) is $\approx\log N-\log(\pi L)-\Sigma_L$ with $\Sigma_L=\sum_{\log n<L}\Lambda(n)n^{-1/2}\|T_{\log n}+T^*_{\log n}\|$ growing like $ce^{L/2}$, so keeping the floor at the currently required $\approx0.6$ needs roughly $N\approx310$ at $\log8$, $950$ at $\log 11$, $1900$ at $\log 13$, $4400$ at $\log16$, and $27{,}000$ as $L\to3$ (where Lemma 4.3's radius also runs out), while the certified margin itself shrinks by about $10^{-34}$ per unit of $L$. So the method as it stands has a practical ceiling around $L\approx2.6$–$2.8$, and no ceiling-lifting idea in §7 is yet a theorem. The storage/nested-Schur material is correct linear algebra but it does not point at a mechanism; the paper is honest that "the missing theorem is an arithmetic bound", and I would go further: nothing in the finite data gives evidence for or against such an induction, and the $2\times2$ counterexample is an argument against the simplest version of it.

Who would care. The Connes–Consani–Moscovici–van Suijlekom circle (the observation that the window ground state is even and simple at every certified horizon is directly relevant to the spectral hypothesis Zhu mentions, and the paper could say so with certified sector-wise enclosures); people doing certified computation in analytic number theory; and the Lean/formalization community, for whom the structure "one analytic lemma + one exact identity + a ball-LDL replay" is an attractive target — the tail lemma is a few pages of classical special-function identities, and a verified LDL checker over the archived dyadic balls is a realistic project. For number theorists at large the result will read as "expected, now certified a bit further out".

Net: worth finishing and depositing as a well-verified certificate paper, with the two-sided enclosures and the profile added, and with the ambition in §7 trimmed to what has been shown. As a route to RH it is not one, and the paper should keep saying so as plainly as it does now.

## 6. Suggested changes to the manuscript

1. **Report what was actually certified.** Replace the round floors by the largest certifiable ones ($3.3\times10^{-23}$ at $9/5$, $1.3\times10^{-28}$ at $\log7$) and add the certified upper bounds, giving two-sided enclosures as Zhu does. The code change is a bisection loop around `validate()` plus a ball Rayleigh quotient; both are in `numerics/review_claude/check_twosided.py`. Update the shift intervals accordingly.
2. **Add the profile table** of certified enclosures at $L=\log2,\log3,\log4,\log5,\log6,9/5,\log7$ (§4 above; each run is about a minute). A profile is far more informative than two isolated floors, it supersedes the earlier `log4`/`log5` certificates from the background reports, and it lets the paper make its own empirical statement about the decay law rather than only citing Zhu's.
3. **Rewrite "Relation to earlier work".** State that positivity through total length $\log2$ is classical (Yoshida 1992; Connes–Consani 2021 — Zhu's abstract says exactly this, so the citation trail is easy), that Zhu's certificate at 1.6 comes with a matching upper bound, and that Zhu's doubly-exponential resolution threshold is the same phenomenon as the growth of $\Sigma_L$ in (4.6). Right now the section reads as if the only comparison point were Zhu's window length.
4. **Consolidate the two main theorems** into one statement with a table (horizon, floor, upper bound, shift interval, decay). The $9/5$ horizon has no independent interest once $\log7$ is certified except as a profile point; the abstract should lead with $\log7$.
5. **Write out Prop. 3.3 in full.** Give the two Laplace-line estimates as a lemma, state precisely in what sense $\partial_sV_{s,L}=-A_{s,L}V_{s,L}$ holds for $s>0$, and show $V_{s,L}f\in\mathcal D_{\log,L}$ with the form identity, rather than "the same estimates with a logarithmic factor justify…". Same for the closure step at the end of Prop. 4.2.
6. **Trim §7.** Keep Corollary 7.1 and Prop. 7.2 (short), move the storage factorization, counterexample and nested Schur to a half-page outlook or an appendix, and drop the language of "recursion strategies" from the abstract's "Exact storage and nested Schur identities specify what an induction would need to retain" — they specify bookkeeping, not what would need to be proved.
7. **Add the sector-wise statement.** Certify per-sector lower bounds (bisect $m$ separately per parity) and per-sector Rayleigh upper bounds, and state that the ground state is even and simple at every certified horizon. This is cheap and is the one observation with an audience beyond certification.
8. **Small corrections.** "an independently assembled certificates" (§1.1) → "independently assembled certificates". "second slab", "first-slab numerical archive" (§7.4, App. B) are project-internal terms undefined in this paper; define them or remove them. Harmonize the recorded environment (App. B says Python 3.12.14 / NumPy 2.3.5; `numerics/README.md` and `requirements.txt` say 3.10.0 / 2.2.6; I reproduced with 3.11.15). The spare factor 2 in $C_L$ can be removed or left with a remark. Mention that the Cauchy majorant 256 is an order of magnitude loose so nobody wastes time tightening it.
9. **Table 2** ("What the larger head resolved") is useful; add a column with the ground-state eigenvalue of the head so the reader sees that the floors are near the spectrum bottom.
10. **Disclosure.** The acknowledgment names OpenAI models; the repository-level disclosure for the program mentions more than one assistant. Make the per-paper statements consistent with the repository's.

## 7. Suggested next steps

In order of value per hour, as I see it.

Cheap and clearly worthwhile: items 1, 2 and 7 above (two-sided enclosures, the profile, sector-wise statements) — an afternoon of compute, and they change the paper from "two floors" to "a certified spectral profile of the finite-window Weil form through $\log 7$".

The $\log 8$ run. The tail floor at $N=128$ is $-0.20$ (negative), $0.52$ at $N=256$ and $1.22$ at $N=512$; the coupling requirement will rise with the new prime, so plan on $N=512$, $M\approx300$ (the target floor will be around $10^{-32}$–$10^{-34}$, so $\eta_M$ must be well below that; $M=300$ gives $\eta\approx10^{-47}$ at $L=\log8$), and about 2000–2500 bits. Matrix assembly scales like $N(N+M)^2$, so expect tens of minutes, not seconds. Use Remark 5.3's sharper $\epsilon_r$ only if it is needed — at these parameters it is not.

Beyond $\log 8$. The estimates in §5 say the current scalar-tail method reaches perhaps $\log 13$–$\log 16$ with effort and stops there. The one idea in the paper that could change the scaling is a *structured* tail bound that keeps the prime–gamma cancellation instead of paying $\Sigma_L$ in full: for instance, bounding the tail form on frequency bands (Legendre tails are spread in frequency, but Slepian/prolate or band-limited tail bases are not), where the multiplier $\log(|\tau|/2\pi)-\sum\Lambda(n)n^{-1/2}\cdot2\cos(\tau\log n)$ is what actually has to be shown positive on high bands. Whether that is easier than the original problem is exactly the question; it is at least a well-posed experiment.

The Lean angle. If the goal is engagement from the formalization community, this paper is the best entry point in the repository: state Lemma 4.1 and Prop. 5.2 as standalone theorems, publish the archived dyadic ball matrices with a specification of the LDL replay, and invite a verified checker. The analytic normalization (§2) is the part a formalizer will least enjoy, so the fully written-out versions of Lemma 2.2 and Prop. 3.3 (item 5) are prerequisites.

What not to invest in yet: the storage induction. Until there is a candidate arithmetic inequality to test, more algebra around $\mathcal C=(I-ZZ^*)^{-1/2}Y(I-X^*X)^{-1/2}$ will not produce one, and the certified data (a ground state that collapses by five orders of magnitude per 0.15 in $L$) suggests any inductive margin would have to be carried at ever-increasing precision.

## Appendix: files added

`numerics/review_claude/` contains the scripts used here, all runnable from `numerics/`:

* `check_constants.py` — analytic constants and the $\log 8$ tail-floor projections (mpmath).
* `check_fourier_side.py`, `check_head_exact.py` — Weil-form normalization against zeta zeros; head diagonal via Weber–Schafheitlin (needs a rebuilt or archived `central_matrices.json.gz`).
* `check_grams_and_floor.py` — direct quadrature of $F$, $C$ entries; note the unit-coordinate convention (the archives store the unitary-coordinate Grams, so do not multiply by $L$).
* `check_floor.py`, `check_twosided.py` — head spectra, floor bisection, certified upper bounds.
* `profile_runs.py` — builds and encloses $\lambda_{\min}$ at $\log2,\ldots,\log6$; output in `profile.json`.

Nothing in the package was modified; all runs used the unmodified `certify_arb.py` and `independent_arb.py`.
