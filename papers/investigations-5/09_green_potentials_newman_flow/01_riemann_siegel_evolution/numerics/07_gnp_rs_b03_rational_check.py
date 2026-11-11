#!/usr/bin/env python3
"""11 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
B03: dispatched gpt-6-astra/ultra; independent audit gpt-6.1-sol/ultra.
Root model/effort unavailable. Exact rational arithmetic only; no field samples.
Run from any directory. This checks constants, not the inherited analytic inputs.
"""
import json
from fractions import Fraction as F

def check():
    tail = F(80,79)**2 * (F(1,6250)+F(1,5625))
    prime_square = F(154,1000)**2 + F(51,1000)**2 + tail
    margin = F(1,1000)
    exponent = 4*(F(9,50)+margin) + 8*F(27,1000)
    exponential_upper = 1+exponent+exponent**2/(2*(1-exponent/3))
    assert 2**11 > F(20,3)**4 and 3**11 > 20**4 and 5**11 > 80**4
    assert F(7,50)+F(9,680) == F(521,3400) < F(77,500)
    assert F(49,1000)+F(1,760) == F(239,4750) < F(51,1000)
    assert tail == F(2432,7021125)
    assert prime_square == F(1497655573,56169000000)
    assert prime_square < F(27,1000)
    assert exponent == F(47,50)
    assert exponential_upper < F(13,5)
    independent_prime_square = F(31,200)**2+F(13,250)**2+F(1,2000)
    assert independent_prime_square < F(11,400)
    return {"status":"passed", "arithmetic":"exact fractions", "prime_tail_upper":str(tail),
            "prime_square_upper":str(prime_square), "allowance_margin":str(margin),
            "exponent_upper":str(exponent), "exponential_upper":str(exponential_upper),
            "gap_below_13_over_5":str(F(13,5)-exponential_upper),
            "independent_prime_square_upper":str(independent_prime_square),
            "scope":"Rational budgets only; not a theta-field or interval certificate."}

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
