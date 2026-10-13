/*
 * Direct-summation evaluation of the Polymath finite sum
 *
 *   f_t(x+iy) = sum_{n<=N} b_n n^{-s_*} + gamma sum_{n<=N} b_n n^{-s_**},
 *   b_n = exp((t/4) log^2 n),  s = (1-y+ix)/2,
 *   s_*  = (1-s) + (t/2) alpha(1-s),   s_** = s + (t/2) alpha(s),
 *   gamma = M_t(s)/M_t(1-s),  M_t(z) = exp((t/4) alpha(z)^2) M_0(z),
 *   alpha(z) = 1/(2z) + 1/(z-1) + (1/2) Log(z/(2 pi)),
 *   M_0(z) = (1/8)(z(z-1)/2) pi^{-z/2} sqrt(2 pi) exp((z/2-1/2) Log(z/2) - z/2),
 *
 * (Polymath arXiv:1904.12438v2, (6)-(11), (14)-(19), and (92) for s_**), at
 * points read from stdin as lines "t re_s im_s" (decimal strings; s is the
 * point's s = (1-y+ix)/2 as used by the barrier program), N = 690988.
 * Output per line: "t re_s im_s re_f im_f rad_re rad_im" (midpoints to 30
 * digits and radii of the 256-bit enclosure).  About 5 s per point on one
 * x86-64 core.
 *
 * This is an independent implementation of the formula (no Taylor stored
 * sums, no shared code with the package); it uses FLINT/Arb ball
 * arithmetic, the same library as the package.  Exploration and
 * corroboration tool for note 5 of the Newman certificate audit; it is not
 * a check programme in the repository's standard-library sense.
 *
 * Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
 * claude-opus-5-5), 12 October 2026.
 *
 * Build: gcc -O2 direct_ft_arb.c -o direct_ft_arb -lflint -lmpfr -lgmp
 */
#include <flint/arb.h>
#include <flint/acb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NMAX 690988

static void
alpha(acb_t r, const acb_t z, slong prec)
{
    acb_t a, b;
    arb_t twopi;
    acb_init(a); acb_init(b); arb_init(twopi);
    acb_mul_2exp_si(a, z, 1); acb_inv(a, a, prec);          /* 1/(2z) */
    acb_sub_ui(b, z, 1, prec); acb_inv(b, b, prec);         /* 1/(z-1) */
    acb_add(r, a, b, prec);
    arb_const_pi(twopi, prec); arb_mul_2exp_si(twopi, twopi, 1);
    acb_div_arb(b, z, twopi, prec); acb_log(b, b, prec); acb_mul_2exp_si(b, b, -1);
    acb_add(r, r, b, prec);
    acb_clear(a); acb_clear(b); arb_clear(twopi);
}

/* log M_t(z) = (t/4) alpha(z)^2 + log M_0(z), principal branches as in (6)-(10) */
static void
logMt(acb_t r, const acb_t z, const arb_t t, slong prec)
{
    acb_t a, b, c, al;
    arb_t pi, tmp;
    acb_init(a); acb_init(b); acb_init(c); acb_init(al);
    arb_init(pi); arb_init(tmp);
    arb_const_pi(pi, prec);
    /* log(1/8) + log(z) + log(z-1) - log 2 - (z/2) log pi + log sqrt(2 pi) */
    acb_log(a, z, prec);
    acb_sub_ui(b, z, 1, prec); acb_log(b, b, prec); acb_add(a, a, b, prec);
    arb_set_ui(tmp, 16); arb_log(tmp, tmp, prec); acb_sub_arb(a, a, tmp, prec);   /* 1/8 * 1/2 */
    arb_log(tmp, pi, prec); acb_mul_arb(b, z, tmp, prec); acb_mul_2exp_si(b, b, -1); acb_sub(a, a, b, prec);
    arb_mul_2exp_si(tmp, pi, 1); arb_log(tmp, tmp, prec); arb_mul_2exp_si(tmp, tmp, -1); acb_add_arb(a, a, tmp, prec);
    /* (z/2 - 1/2) Log(z/2) - z/2 */
    acb_mul_2exp_si(b, z, -1); acb_log(c, b, prec);
    acb_sub_ui(b, z, 1, prec); acb_mul_2exp_si(b, b, -1); acb_mul(b, b, c, prec);
    acb_add(a, a, b, prec);
    acb_mul_2exp_si(b, z, -1); acb_sub(a, a, b, prec);
    /* (t/4) alpha^2 */
    alpha(al, z, prec); acb_sqr(b, al, prec); acb_mul_arb(b, b, t, prec); acb_mul_2exp_si(b, b, -2);
    acb_add(r, a, b, prec);
    acb_clear(a); acb_clear(b); acb_clear(c); acb_clear(al);
    arb_clear(pi); arb_clear(tmp);
}

int
main(int argc, char **argv)
{
    slong prec = 256;
    char line[4096], ts[512], rs[512], is[512];
    arb_t t, logn, b, tmp;
    acb_t s, onems, al, sstar, sss, gam, l1, l2, term, sum1, sum2, f, e;
    (void) argc; (void) argv;
    arb_init(t); arb_init(logn); arb_init(b); arb_init(tmp);
    acb_init(s); acb_init(onems); acb_init(al); acb_init(sstar); acb_init(sss);
    acb_init(gam); acb_init(l1); acb_init(l2); acb_init(term); acb_init(sum1); acb_init(sum2);
    acb_init(f); acb_init(e);

    while (fgets(line, sizeof line, stdin))
    {
        if (sscanf(line, "%511s %511s %511s", ts, rs, is) != 3)
            continue;
        arb_set_str(t, ts, prec);
        arb_set_str(acb_realref(s), rs, prec);
        arb_set_str(acb_imagref(s), is, prec);
        acb_neg(onems, s); acb_add_ui(onems, onems, 1, prec);
        /* s_* = (1-s) + (t/2) alpha(1-s);  s_** = s + (t/2) alpha(s) */
        alpha(al, onems, prec); acb_mul_arb(al, al, t, prec); acb_mul_2exp_si(al, al, -1);
        acb_add(sstar, onems, al, prec);
        alpha(al, s, prec); acb_mul_arb(al, al, t, prec); acb_mul_2exp_si(al, al, -1);
        acb_add(sss, s, al, prec);
        /* gamma = M_t(s)/M_t(1-s) */
        logMt(l1, s, t, prec); logMt(l2, onems, t, prec); acb_sub(l1, l1, l2, prec); acb_exp(gam, l1, prec);
        acb_zero(sum1); acb_zero(sum2);
        for (slong n = 1; n <= NMAX; n++)
        {
            arb_set_ui(logn, (ulong) n); arb_log(logn, logn, prec);
            arb_sqr(b, logn, prec); arb_mul(b, b, t, prec); arb_mul_2exp_si(b, b, -2);   /* (t/4) log^2 n */
            /* b_n n^{-s_*} = exp((t/4) log^2 n - s_* log n) */
            acb_mul_arb(e, sstar, logn, prec); acb_neg(e, e); acb_add_arb(e, e, b, prec);
            acb_exp(term, e, prec); acb_add(sum1, sum1, term, prec);
            acb_mul_arb(e, sss, logn, prec); acb_neg(e, e); acb_add_arb(e, e, b, prec);
            acb_exp(term, e, prec); acb_add(sum2, sum2, term, prec);
        }
        acb_mul(f, gam, sum2, prec); acb_add(f, f, sum1, prec);
        printf("%s %s %s ", ts, rs, is);
        arf_printd(arb_midref(acb_realref(f)), 30); printf(" ");
        arf_printd(arb_midref(acb_imagref(f)), 30); printf(" ");
        mag_printd(arb_radref(acb_realref(f)), 5); printf(" ");
        mag_printd(arb_radref(acb_imagref(f)), 5); printf("\n");
        fflush(stdout);
    }
    flint_cleanup();
    return 0;
}
