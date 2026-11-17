# B09: complete-source transverse second-moment input

17 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance, chat0006. Actual root model/effort unavailable;
conceptual dispatch gpt-6-astra/ultra, execution gpt-6.1-sol/ultra.

The primary reference is Kenneth Maples and Brad Rodgers, *Bootstrapped
zero density estimates and a central limit theorem for the zeros of the
zeta function*, [arXiv:1404.3080v2](https://arxiv.org/html/1404.3080v2),
4 June 2016; [DOI 10.1142/S1793042115500918](https://doi.org/10.1142/S1793042115500918).
Reuse the [canonical annotation][catalog], [BibTeX][bib] and
[PDF receipt][receipt]; this is a dated use addendum, not another catalog.

Fresh selected primary HTML inspection on 17 November checked Theorem2.4,
Corollary2.3 and §4 equation(18). Theorem2.4 fixes a density exponent in
(0,1), with a constant depending on that exponent. Equation(18) is uniform
for height at least two and scaled transverse threshold. It is an
unconditioned aggregate count. No conditional distribution of zeros near
a chosen pair or every-center bound is imported. Fixed-order moment
constants and equation(19)'s test class are not used here.

The heat-time extension is the repository's **proved in-note**
[TND-O Note21][moment], equations(7)–(8), internally accepted in
[Assessment07 §5][review]. It uses canonical time-zero density, the
complete count/resolvent input, convex broad-window heat transport and
collision assembly. In the H-coordinate x=2*ordinate and
y=-2*(real part−1/2), for fixed 0<b<1/2 it gives

    sum_{T<=Re rho<=2T} (Im rho)^2 <= (2 B_b/b^2) T/log T,
    T>=8, 0<=t<=1/2,

with multiplicities and constants uniform in t,T. B09 reuses that theorem;
it does not claim to reprove the entire inherited chain. Its proposed new
step integrates the truncated inverse-fourth kernel against centers and
uses this second moment. The equally averaged count-only comparison must
also integrate its kernel; comparing a mean to a pointwise allowance
would exaggerate the gain. The source gain is in the exclusion-radius
dependence, not a selected-pair positivity conclusion.

The existing authorized PDF reading copy was re-hashed, not downloaded:
`/Users/Shared/szp-archive/operator-newman-collision-geometry/references/1404.3080v2.pdf`,
194362 bytes, SHA-256
`3122ff5fcc95844cf010aa66b124ecf3ed3b69776840831fe2dec130e9006c56`.
It matches the 6 November receipt. Today's passage inspection used HTML;
this hash is file identity, not mathematical verification. No full-paper
or specialist review, new article, changed source or literature-priority
claim is made. The [branch reference guide](README.md) and
[predecessor audit](../reviews/16_VCD_GT_B09_PREDECESSOR_RATE_AUDIT_20261117.md)
retain the separate signed-consumer limitations.

[catalog]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/08_TND_O_B03_LOCALIZED_STATISTICS_SOURCE_USE_20261106.md
[bib]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/localized_statistics_sources.bib
[receipt]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/LOCALIZED_STATISTICS_PDF_RECEIPTS_20261106.json
[moment]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[review]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
