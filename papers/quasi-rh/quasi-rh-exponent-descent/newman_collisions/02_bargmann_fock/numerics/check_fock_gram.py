"""Exact rational algebra checks; not a theta nonvanishing certificate."""
from fractions import Fraction as F

cases = 0
for a in (F(1, 2), F(1), F(3, 2)):
    for x in (F(0), F(2, 3), F(7)):
        g00, g01, g11 = F(1), x/a, 1/a + x*x/(a*a)
        det = g00*g11 - g01*g01
        assert det == 1/a
        inverse = ((1+x*x/a, -x), (-x, a))
        assert g00*inverse[0][0] + g01*inverse[1][0] == 1
        assert g00*inverse[0][1] + g01*inverse[1][1] == 0
        assert g01*inverse[0][0] + g11*inverse[1][0] == 0
        assert g01*inverse[0][1] + g11*inverse[1][1] == 1
        for value, slope in ((F(0), F(0)), (F(3, 5), F(-2, 7))):
            quadratic = (1+x*x/a)*value*value-2*x*value*slope+a*slope*slope
            assert quadratic == value*value+a*(slope-x*value/a)**2
        cases += 1
print(f"PASS: {cases} exact rational Gram/inverse/projection cases.")
