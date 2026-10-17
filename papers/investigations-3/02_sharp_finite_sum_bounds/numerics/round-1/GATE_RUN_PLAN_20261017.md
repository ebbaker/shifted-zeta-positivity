# Bounded implementation of the active branch transfer gate

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model gpt-6.1-sol (Codex), reasoning effort ultra. Same-model internal work.

Scope before the interval run: exact t=157/1000; all four finite legs
N=690988..728999,729000..818999,819000..1027999,1028000..3840000 with
prime sets {2,3,5,7,11},{2,3,5,7},{2,3,5},{2,3}. Cover y from
sqrt(87677/2500000) through sqrt(343/500). Cover all 360 nonempty
(gcd pattern, active-divisor sector) types, embedding the actual integer
pairs in continuous boxes h=log N, v=log(n/N). Keep N dependence through
delta(h)=-log(1-(t/16)exp(-2h))/2; do not freeze ell at a leg endpoint.

Answer sought: does the sufficient active-branch gate (2) certify termwise
nonincrease of the normalized sharp mass on the stated domain? A passing
continuous cover implies the integer result. An unresolved interval or a
positive value at an unphysical continuous point is not a counterexample.
Use both active branches at ties and right absolute-value derivatives at
zeros. An equivalent absolute-sum derivative may certify a box without
branch masks; its identity is checked in exact rational arithmetic.

Analytic shortcuts: singleton-active-divisor sectors pass under the
proved bound log N < -2 ell; exact n=p prime terms pass under the direct
zero-coefficient argument. Only use the latter when the interval contains
that sole possible integral n. Integer emptiness pruning must overenclose
N,n and enforce gcd and exact strict-lower/inclusive-upper sectors.

Arithmetic: 40-digit directed Decimal operations; exp, ln, sqrt correctly
rounded in nearest mode and padded outward by 1e-38. No float signs are
accepted. Before full evaluation run interval endpoint checks, exact
rational derivative identities including ties/zeros, and small-integer
coverage checks. Baseline: the old generic transfer implication is false;
a separate bounded float scout found no sampled theta violation, which is
not a certificate and does not choose an acceptance threshold.

Fixed one-pass budget: process legs in order 3,2,1,0, at most 45 seconds
and 30000 evaluated boxes per leg, depth at most 36, total at most 180
seconds of interval evaluation (plus self-checks). Peak resident limit
512 MiB. A budget stop is recorded as incomplete with pending domains;
no precision increase, full row sweep or adaptive campaign is permitted
inside this pass. Accepted-leaf hashes are reproducibility diagnostics;
interval comparisons, not hashes or counts, decide signs. Keep only small
records and representative unresolved cells. Code/plan hashes bind the run.
