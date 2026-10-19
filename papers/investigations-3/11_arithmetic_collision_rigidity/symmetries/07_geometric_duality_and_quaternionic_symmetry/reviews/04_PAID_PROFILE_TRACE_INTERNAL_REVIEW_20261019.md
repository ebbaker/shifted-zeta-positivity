# Internal review: paid profile trace and direct source-tail comparison

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6.1-sol (Codex)**,
actual reasoning effort **ultra**, in a separate delegated same-model
reading. This is an internal mathematical and code review, not independent
specialist human review. No repository files or history were written by
the reviewer; the author owns installation and status updates.

## Disposition

**Pass after two wording corrections incorporated before installation.**
The corrections are recorded below. The written
upper estimate is finite and applies to the actual selected residual.
A separate lower bound on the exact norm used by the selected rule proves
that refining its evaluation cannot beat the available direct arithmetic
allowance. This supports **S07-T2 Complete**, **S07-T3 Waiting**, T4
Deferred, and stopping this selected route without acquiring a numerical
consumer. It does not exclude other theta-geometric estimates.

The reviewer read S07 Note 03 and the complete Note 04 draft, checked the
continuous derivations separately, inspected the full new checker, and
executed a fresh **192-bit** replay, including a second run after the final
portable-checkout guards and displayed-decimal checks were added. Every
required check passed. The
reviewer record is
[S07_T2_REVIEW_REPLAY_192_20261019.json](../numerics/S07_T2_REVIEW_REPLAY_192_20261019.json).
The replay identifies the source files it actually read; the author must
produce the primary records against the installed final sources. File
hashes preserve identity, not mathematical validity.

## Cutoff, derivatives and complete norm upper bound

The logistic form of the actual smooth cutoff gives

\[
 |\rho'|=\frac{2(1+d^2)}{(1-d^2)^2\cosh^2z},
 \quad z=2d/(1-d^2),\quad |d|<1.
\]

Since cosh-squared z is at least 1+z-squared and
(1-d-squared)-squared+4d-squared=(1+d-squared)-squared, the claimed
bound 2 is valid, including smooth endpoint limits. It implies exactly
the displayed 9a-squared+2a_y-squared bound; no annular derivative is
dropped. The source derivative is correctly
q^(1/4)(-2 pi^3 q^3 y^5+7 pi^2 q^2 y^3-3 pi q y) exp(-pi q y^2).
Its leading-term magnitude dominates for |y|>=2, q>=1.

Both relevant squared polynomial-Gaussian terms decrease with q>=1.
The Gaussian tail estimate for M0 and the positive even-moment recurrence
therefore give a valid upper bound. The p integration retains the factor
exp(pi q/8)(2+pi-squared q-squared/24), with integral p-squared dp=1/96.
Taking its maximum at q=4 and then integrating dq/(4q) gives the written
X upper bound. The replay gives X_+ approximately 0.02648367416.

The derivatives g_p=2 pi p q g and g_py=2 pi p q g_y are both retained.
The argument uses no Green identity, no boundary flux deletion, no
Jacobi residual and no higher cutoff derivatives. Those are appropriately
outside its paid operator contract.

## Lower floor and its interpretation

On q in [1,17/16], |y| in [9/4,5/2], the cutoff lower bound is
rho>=1/(1+exp(8/3)). Direct differentiation shows a_q decreases in q
and |y| there; its minimum is the claimed corner value. Both y intervals,
the full p interval, the minimum weight 97/16, and dq/(4q) give exactly
the coefficient (97/64)log(17/16) in X_- squared. Dropping nonnegative
derivative terms is legitimate for this lower bound. The replay gives
X_->7.02927250e-9.

The sine/cosine norm floors follow from their exact elementary integrals.
In particular the first-derivative floor retains all three possible
endpoint payments, U-squared/(4x), U/(4x-squared), and 1/(8x-cubed).
The resulting assigned-payment floors exceed 1.30765836e-8 and
2.61274726e-9 throughout B.

These are floors for sqrt(20)X(g)C_j, **not** floors for the actual
approximation error or signed residual. The draft makes this distinction
explicitly. The noninteger annulus identifies a specific loss in this
norm: it contains positive profile mass absent from the integer physical
sampling. No conclusion about a differently adapted observation rule
follows from this floor.

## Direct bound, outside source and complete comparison

The inequalities (log q)^2<=q, u<= (q-1)/4, and q^(5/4)<=q-squared hold
on the entire q>=1 half-line. Together with the two lattice signs and
physical measure dq/(4q), they give the coefficients pi-squared/2 and
pi-squared/8 in the direct integrands. In particular the improved
first-derivative factor q-squared(q-1) has the right factor of four.

The consecutive-mode ratios at q>=1 and q>=4 are respectively bounded
by (4/3)^4 exp(-7pi) and (4/3)^4 exp(-28pi). The positive J_Delta
antiderivative is algebraically correct. Its q-squared(q-1) integrand
and both inside/outside source payments have been retained. The fresh
192-bit replay gives direct inside allowances below 8.07803e-12 and
7.65021e-14, and outside allowances below 1.84725e-47 and 1.40207e-47.
The geometric-floor/direct-total ratios exceed 1618 and 34152.

The global retained approximant includes n=1,2 for all u>=0. Thus paying
only n>=3 beyond q=4 is correct: the n=1,2 outside integrals are part of
the shared retained function, not omitted source. The same unspecified
nonnegative acquisition payments can be added to both routes, and strict
componentwise ordering remains. An acquired oscillatory approximant is
unnecessary to decide this analytic no-gain gate. The draft appropriately
does not claim a completed numerical consumer, acquired anchor, cost
benchmark or signed margin.

Fixed positive physical normalization rescales both routes equally.
The optional Q=H/A conversion retains b=(log A)_x and division by the
nonzero phase slope; its stated positive component map preserves the
ordering. Neither the raw direct N=2 bound nor its normalized value is
described as the strongest existing consumer.

## Wording corrections and controls

Two narrow wording corrections were communicated and verified in the
revised draft before installation:

1. Replace the statement about tightening only the rule's "constants or
   quadrature" with tightening its **norm enclosures or quadrature**.
   The floor fixes the sqrt(20) observation rule; it does not itself rule
   out replacing that rule with a new sharper observation theorem.
2. Describe the source/error identity and cutoff derivative bound as
   **proved in the note**, with the new code checking supporting finite
   algebra, outward interval constants and positivity conditions. The
   checker does not by itself establish every continuous source identity.

The supplied control discussion is correctly scoped to inherited
regression screening and analytic premise failures. The new estimate is
an upper-error rule, not a strict physical acceptance interface. The
reviewer did not rerun the separately author-owned source-control replay
and does not count its regression outcome as validation of the analytic
proof. The result-summary, collision-control and avoidance references
are consistent with the scoped claim.

The useful output is a fully paid, explicitly losing observation rule and
a reproducible stopping argument. It supplies no physical sign, new
coverage, Newman bound or universal geometric obstruction.
