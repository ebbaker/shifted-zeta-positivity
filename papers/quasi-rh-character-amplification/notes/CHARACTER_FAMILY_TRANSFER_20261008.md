# Character family amplification transfer targets and obstructions

2026-10-08. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning effort are not exposed and are not inferred.
Same-model parallel analysis is an internal check, not independent specialist refereeing.

## Scope and source inputs

This note derives conditional exponent transfers and tests a direct connection to the repository's signed covariance. It proves no new arithmetic mean-square estimate or zero-free region. The [parameter extension](PARAMETER_EXTENSION_20261008.md) records a separate, small conditional improvement using the published structural lemmas; the short-family hypotheses below are a different, unproved research direction.

Sources are OpenAI's [October 5 paper, the 11/12 half-plane](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf), especially Proposition 3.1 and equations (3.1)–(3.3), and its [September 30 companion, the 7/8 half-plane](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), especially Lemmas 17.1, 17.2, 17.6 and 18.1. Their analytic lemmas are treated as source inputs, not independently verified here.

Write, over Eisenstein ideals outside the fixed excluded set,

\[
A_u(D)=\sum_{\mathfrak n}\mu_K(\mathfrak n)\nu(\mathfrak n)
 \chi_{\mathfrak n}(u)W(N\mathfrak n/D),
\]

with fixed finite-order character \(\nu\) and fixed smooth annular \(W\). The October paper establishes

\[
\sum_{0<N(u)\le H}|A_u(D)|^2\ll D^{1+\varepsilon}H,
\qquad H=D^{1+\vartheta},\quad 0<\vartheta\le1/10.
\tag{1}
\]

The longer paper's unmarked equations (17.87)–(17.89) likewise require \(H\ge D^{1+c}\), with fixed \(c>0\). Neither statement supplies square-root average cancellation for \(H<D\).

## Existing covariance feedback does not improve the baseline

The external seven-eighths zero strip would give our fixed-response variance
\(\mathcal V_g(X)=O(X^{11/4})\) and prepared scalar
\(\lambda_V(X)=O(X^{-1/8})\). The [mixed-discrepancy identity](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/MIXED_DISCREPANCY_FEEDBACK_20261004.md)
retains the exact caps in

\[
J_0(X;U)-R=\frac1{q_0X^2}\iint_{s,t>U}
M_U(s)E_U(t)\mathscr F(st/X)\,ds\,dt,\qquad q_0=7/3.
\]

Here \(R=O((U^2/X)^8)\), and the prepared kernel has bounded upper support
and \(\mathscr F(v)=O(v^3)\) at zero. Even granting compatible separate
bounds \(|M_U(s)|\ll s^\beta\), \(|E_U(t)|\ll t^\beta\), taking absolute
values and setting \(v=st/X\) gives only

\[
|J_0-R|\ll X^{\beta-1}
\int_{U^2/X}^C v^\beta|\mathscr F(v)|\log(Xv/U^2)\,dv
\ll X^{\beta-1}\log(X/U^2).
\]

Thus beta=7/8 recovers the same power. The exact
[zero-mode calculation](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
also transmits the original detector residue with coefficient one; this
is a deterministic finite-mode diagnostic, not a zero expansion of the
actual arithmetic errors.

To target beta=7/8-eta by the local scalar route, a complete signed
estimate must save another \(X^{-\eta}\). The existing comparison budget
permits \(U=V=X^{55/112-\eta/14}\) and
\(H=X/U^2=X^{1/56+\eta/7}\). Then the lower-boundary cost is exactly
\(H^{-7}=X^{-1/8-\eta}\), density costs \(H^{-8}\), and prime-power
removal fits for \(0<\eta<27/232\). These are valid cutoff choices,
not the missing cancellation estimate.

## Replicated-row transfer

Suppose instead that, for fixed \(h>0\) and loss \(a\ge0\),

\[
\sum_{0<N(u)\le D^h}|A_u(D)|^2
 \ll D^{1+a+h+\varepsilon}.
\tag{2}
\]

This is a hypothesis when its parameters leave the source's range. For characters of order dividing \(m\), rows \(u=p^m\), with \(Np\asymp D^{h/m}\), reproduce \(A_1\) except for columns divisible by \(p\). There are \(D^{h/m+o(1)}\) such rows. Ideal counting bounds each omitted contribution by \(O(D^{1-h/m})\), whenever this range is relevant. Averaging their squared values gives

\[
|A_1(D)|\ll D^{B+\varepsilon},\qquad
B=\max\left\{\frac{1+a}{2}+\frac{m-1}{2m}h,
                       1-\frac hm\right\}.
\tag{3}
\]

For sextic characters and \(a=0\), this beats \(7/8\) precisely for

\[
\frac34<h<\frac9{10}.
\]

Balancing the two terms gives \(h=6/7\), \(B=6/7\). More generally, the interval is \(3/4<h<9/10-6a/5\), nonempty when \(a<1/8\). The actual source range \(h=1+\vartheta\) gives \(11/12+5\vartheta/12\), as expected. Merely selecting a smaller subfamily from (1) retains its larger upper bound and does not prove (2).

## Paying for the omitted primes more efficiently

Assume explicitly, for the same fixed \(\nu,W\), that

\[
|A_1(L)|\ll L^{\theta+\varepsilon}\quad(L\ge1),\qquad\theta>0.
\tag{4}
\]

Take \(q=Np\) and \(B_p(L)=A_{p^6}(L)\). Squarefree multiplicativity gives

\[
A_1(L)=B_p(L)-\nu(p)B_p(L/q),
\quad
B_p(L)=\sum_{j\ge0}\nu(p)^jA_1(L/q^j).
\]

The sum terminates by annular support. Consequently

\[
A_1(D)-A_{p^6}(D)
=-\sum_{j\ge1}\nu(p)^jA_1(D/q^j)
\ll(D/q)^{\theta+\varepsilon}.
\tag{5}
\]

For the growing prime range used above, the geometric-series constant is uniform. This is an estimate for one fixed character; removing a prime does not introduce a new conductor.

Equations (2), (4), and (5) imply

\[
B=\max\{(1+a)/2+5h/12,\;\theta(1-h/6)\}.
\tag{6}
\]

When the balanced value is positive, it is

\[
h=\frac{6(2\theta-1-a)}{5+2\theta},\qquad
B=\frac{\theta(6+a)}{5+2\theta}.
\]

Thus \(\theta=7/8,a=0\) leads conditionally to \(h=2/3\), \(B=7/9\). Equation (4) is kept explicit: deriving it from a zero-free half-plane also requires the appropriate reciprocal-growth and Mellin-contour argument. Even granting (4), the short-family hypothesis (2) remains unavailable.

There is an exact alternative. The companion's equation (17.90), with \(M_u(L)=L^{-1/2}A_u(L)\), gives

\[
M_1(D)=\sum_{d\mid\operatorname{rad}(b)}
 \mu_K(d)\nu(d)N(d)^{-1/2}M_{b^6}(D/Nd).
\tag{7}
\]

If one hypothesizes the stronger scale-uniform bound

\[
\sum_{0<N(u)\le H}\sup_{0<L\le D}|M_u(L)|^2
\ll H D^{a+\varepsilon},\qquad H=D^h,
\tag{8}
\]

averaging (7) over primary ideals \(Nb\le H^{1/6}\), using the divisor bound and distinct sixth-power rows, yields

\[
|A_1(D)|\ll D^{(1+a)/2+5h/12+\varepsilon}.
\tag{9}
\]

There is no omitted-prime error here. Therefore \(6/7\) is only the optimum of the crude extraction (3), not an intrinsic barrier. The source proves the necessary scale control only for \(H>D\).

## Why the local covariance does not immediately transfer

Our [signed covariance continuation](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/SIGNED_COVARIANCE_CONTINUATION_20261004.md) retains truncated divisor coefficients, product caps, prime factors, and a continuum subtraction. Its cancellation cannot be replaced by separate absolute bounds on the semiprime and smooth-cofactor sectors. Three further obstacles matter.

First, integer and ideal Möbius functions differ. Sending an integer \(d\) to \((d)\) changes its norm to \(d^2\); at a split rational prime, \(\mu_K((p))=+1\) while \(\mu(p)=-1\). The source's consequence for Dirichlet functions descends through factorization of Hecke \(L\)-functions, not coefficientwise substitution.

Second, the marked coefficient class is restricted. Lemma 17.1 permits one inverse polynomial times disjoint prime slots, all sharing one character and orientation, with prime coefficients independent of the row. Lemma 17.2 expressly excludes an arbitrary additional residual coefficient, even row-independent. A direct transfer therefore needs an exact decomposition of our cofactor and cutoff weights into this class, with controlled total cost. Smooth norm-test separation alone does not justify arbitrary arithmetic weights.

Third, the marked ranges defeat the naive balanced block. With inverse length \(Z^r\), total prime-slot length \(Z^z\), and row length \(Z^m\), Lemma 17.1 requires

\[
r+2z<m,\qquad 2r+8z<3m.
\]

The illustrative balanced choice \(r=z=1/2\) forces \(m>5/3\). Even granting favorable replication and ignoring extra errors, the extracted unnormalized product bound has exponent

\[
(r+z)/2+5m/12>43/36,
\]

worse than its trivial exponent one. Splitting prime factors into more slots does not lower total \(z\). This diagnoses a naive model, not the complete covariance.

An unrestricted coefficient extension is impossible: choose an allowed nonnegative nonzero annular W and a bounded residual weight \(b(\mathfrak n)=\mu_K(\mathfrak n)\overline{\nu(\mathfrak n)}\) on squarefree support. This cancels the Möbius signs. Prime sixth-power rows then contribute energy \(\gg D^2H^{1/6}/\log H\), forcing \(h\ge6/5\) for a uniform \(O(DH D^\varepsilon)\) theorem. Random bounded coefficients also give expected diagonal-size energy, ruling out uniform power gains below \(DH\), up to logarithms. These are coefficient-class obstructions, not lower bounds for actual Möbius sums.

The precise open target is short-family control for the actual Möbius coefficients, preferably (8) with \(h<9/10\), together with any decomposition needed to reach our signed kernel. The announced results suggest its structure but do not establish this target.
