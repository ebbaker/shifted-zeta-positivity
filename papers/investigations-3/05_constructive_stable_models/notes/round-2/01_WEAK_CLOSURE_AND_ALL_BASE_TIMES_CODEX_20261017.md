# Round 2: weak closure and independent-spin preparation at all base times

17 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**;
reasoning effort: **ultra**. Three same-model agents checked the arguments
and primary sources. These are authoring checks, not another cross-model
review or specialist human review.

**Status: proved in-note from the cited classical inputs; round-two review
pending.** This reconciles the mathematical extensions in the
[round-one review](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
Weak convergence suffices for the persistent-site obstruction. Moreover,
the independent-spin heat family cannot approximate theta at any fixed
nonnegative target time when prepared at any nonpositive base times,
including base times tending to minus infinity. The review's remaining
unbounded-base-time exception is therefore unnecessary for that family.
No theta approximation or RH conclusion is obtained.

The [result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md) govern this continuation;
especially [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[target classification](../../../../../avoid/01_restating_the_target.md),
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
These are exclusions of specified constructions. Stable approximation to
the complete time-zero theta transform remains an RH-strength objective.

## 1. Weak closure is an existing theorem

Use symmetric Lee–Yang laws: symmetric probability measures with
some finite Gaussian-square moment and an entire characteristic function
in the Laguerre–Pólya (LP) class. Newman–Wu's
[Definition 6, Theorem 7 and Proposition 13](https://arxiv.org/pdf/1708.08820#page=4)
give the relevant product and weak closure. The result proposed in review
§4.1 is correct, but is already in this primary source. Here is the short
proof, including the stronger convergence needed in this investigation.

Write
\[
f_n(z)=e^{-a_nz^2}\prod_k(1-z^2/r_{nk}^2),\qquad
a_n\ge0,\quad \sum_k r_{nk}^{-2}<\infty,\quad
v_n=2a_n+2\sum_k r_{nk}^{-2}=\operatorname{Var}\mu_n.
\tag{1}
\]
Suppose \(\mu_n\Rightarrow\mu\). Their characteristic functions converge
uniformly on bounded real intervals. Choose \(\delta>0\) with the limiting
characteristic function at least \(1/2\) on \([-\delta,\delta]\).
Eventually \(f_n\ge1/4\) there, so \(|r_{nk}|>\delta\). The product gives
\[
\frac14\le f_n(\delta)\le e^{-v_n\delta^2/2},\qquad
v_n\le\frac{2\log4}{\delta^2},\qquad
|f_n(z)|\le e^{v_n|z|^2/2}.
\tag{2}
\]
This improves the review's nonessential constant \(8\log4\) to
\(2\log4\). Normality and uniqueness on the real axis give convergence
on complex compact sets to an entire LP function \(F\).

For each original law its Gaussian-square moment permits evaluation at
imaginary arguments, so
\(M_n(h)=f_n(-ih)\le e^{Vh^2/2}\), with \(V=\sup_n v_n<\infty\).
The same bound at \(2h\) gives uniform integrability of \(e^{hX_n}\).
Weak convergence therefore gives
\[
M_n(h)\longrightarrow M_\mu(h)=F(-ih)\quad(h\in\mathbb R).
\tag{3}
\]
Cauchy's formula gives convergence of all moments. Gaussian integration
also gives the paid bound
\[
\sup_n\mathbb E e^{qX_n^2}\le(1-2qV)^{-1/2},\qquad
0\le q<(2V)^{-1}.
\tag{4}
\]
Thus weak convergence gives differentiated unnormalized heat-transform convergence on
compact sets with \(\Re t<(2v)^{-1}\) when the limiting variance is
\(v>0\): choose an eventual variance bound \(V>v\) and a larger
Gaussian-square exponent within (4). This does not guarantee convergence
at arbitrary heat times.

The Gaussian-square/LP hypothesis matters. An entire characteristic
function with only real zeros can have an additional zero-free factor of
infinite order. For example
\(\cos z\exp\{(\cos(nz)-1)/n\}\) corresponds to a Rademacher variable plus
independent rare compound-Poisson jumps \(\pm n\). Its laws converge
weakly to Rademacher, but their variances are \(1+n\), and their Laplace
transforms diverge at nonzero real fields. It is outside (1).

## 2. Consequence for interacting quartic networks

Finite zero-field ferromagnetic Ising readouts have entire characteristic
functions of order at most one. Finite quartic-network readouts have order
at most \(4/3\), by quartic domination of the finite-dimensional integral.
The Lee–Yang inputs already checked in
[round-one Notes 01–03](../round-1/README.md) give only real zeros.
Symmetry and Hadamard factorization give (1); each law also has every
Gaussian-square moment. Hence weak convergence implies the Laplace
convergence used in Note 03's persistent-site proof.

**Corrected hypothesis.** If the readout laws of those quartic networks
converge weakly to theta's normalized source, then for every \(A>0,B\ge0\)
eventually no site satisfies both
\[
\alpha_{nj}/b_{nj}^4\le A,\qquad \beta_{nj}/b_{nj}^2\le B.
\tag{5}
\]
In particular, the necessary condition (11a) there follows under weak
convergence too. The proof remains the normalized GKS comparison and
the contradiction between \(h^{4/3}\) site growth and theta's
\(O(h\log h)\) growth. The earlier limitation concerning weak convergence
is superseded. The same proof excludes the stable Bessel source
\(e^{-2\pi\cosh4u}\), so this is a family-expressiveness result.

## 3. Fixed rollback closes even unbounded preparation times

For a probability measure define
\[
T_a\rho(du)=\frac{e^{au^2}\rho(du)}{\int e^{au^2}\,d\rho},
\tag{6}
\]
whenever defined. If \(\rho_n\Rightarrow\rho\) and \(a_n\to a\ge0\),
then \(T_{-a_n}\rho_n\Rightarrow T_{-a}\rho\). On bounded intervals the
weights converge uniformly; tightness controls the complement, since
the weights lie in \([0,1]\). The limiting denominator is positive.
This proves the zero-limit case too, where global uniform convergence
of \(e^{-a_nu^2}\) to 1 would be false.

Let \(\mu_n\) be arbitrary finite independent Rademacher sums, with
arbitrary changing amplitudes and counts. Their forward heat laws
\(T_s\mu_n\) are Lee–Yang for every \(s\ge0\), by the finite Ising theorem
already verified in round one. Write
\(\mu_{\theta,t}(du)\propto e^{tu^2}\Phi(|u|)\,du\).

**Theorem.** For every fixed \(t_0\ge0\), no sequence \(\tau_n\ge0\)
can satisfy
\[
T_{t_0+\tau_n}\mu_n\Rightarrow\mu_{\theta,t_0}.
\tag{7}
\]
Thus independent preparation at base time \(-\tau_n\le0\) is excluded,
even when \(\tau_n\to\infty\).

**Proof.** If a subsequence has \(\tau_n\ge\delta>0\), roll back the
fixed amount \(t_0+\delta\). Equation (6) gives
\[
T_{\tau_n-\delta}\mu_n\Rightarrow\mu_{\theta,-\delta}.
\]
The left side consists of Lee–Yang laws because
\(\tau_n-\delta\ge0\). Weak closure makes \(H_{-\delta}\) real-rooted,
contradicting [Rodgers–Tao, Theorem 1](https://arxiv.org/pdf/1801.05914),
\(\Lambda\ge0\). No upper bound on \(\tau_n\) was used.

The only alternative is \(\tau_n\to0\). Roll back the full varying
amount \(t_0+\tau_n\) to get \(\mu_n\Rightarrow\mu_{\theta,0}\).
Lévy's theorem gives uniform convergence of the cosine products on the
bounded real set of Note 01's certified odd-dilation floor, a contradiction.
For normalized probability transforms the floor is divided by \(H_0(0)\).
This proves (7). \(\square\)

More generally, the same fixed rollback proves that any weakly
theta-approximating sequence with a Lee–Yang heat path underneath it
cannot retain a positive removable amount of heat. This conditional
statement about the construction does not assert such a path for an
arbitrary real-zero measure. Initially interacting families are not all
covered by (7).

## 4. Reconciliation and bounded disposition

Accept the review's round-one proof checks and reverse Bessel control.
The persistent-site weak extension is valid; the bounded-time extension
is valid and is strengthened by (7). The classical attribution is to
Newman–Wu for weak closure, and to Lee–Yang and Rodgers–Tao for rollback.
The review's de Bruijn attribution for fixed entire source multipliers
also stands. A finite diagnostic does not make these mechanisms new.

The [companion note](02_DIVERGING_HEAT_TILTS_AND_NEWMAN_CLASS_CODEX_20261017.md)
uses Newman's classical Gaussian-convolution argument to exclude the
stable Bessel control too in the diverging-time regime, even for general
LP seeds. It requires no additional numerical campaign.

The collision controls from summary 12 fail stable convergence at their
nonreal-zero slices: time zero for Euler-factor controls and a positive
pre-collision time for weighted-square, reflected and positive-primitive
controls. Hurwitz already forces these failures. They do not validate a
construction; the stable Bessel reverse control tests expressiveness.

Round one ran its nomination, compatibility and diagnostics before its
first cross-model review at the user's request. That review found no
mathematical error but did not endorse a manuscript milestone. Its
recommended dormant status is adopted for the completed opening search:
no larger fit or new manuscript is warranted. General interacting
infinitesimal-site constructions and fixed non-Gaussian Cardon multipliers
remain unresolved. Reopening needs a named construction with a proved
Bessel approximation and a theta-specific estimate; these are future
gates, not established convergence. Round-two proofs await cross-model
review.
