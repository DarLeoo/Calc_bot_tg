import div, mult, diff, sum
from fractions import Fraction
from my_ui import write_line


def calc_fraction(act, a, b, c, d):
    if act == "+":
        return str(sum.sum(Fraction(a, b), Fraction(c, d)))
    elif act == "-":
        return str(diff.diff(Fraction(a, b), Fraction(c, d)))
    elif act == "*":
        return str(mult.mult(Fraction(a, b), Fraction(c, d)))
    elif act == "/":
        return str(div.div(Fraction(a, b), Fraction(c, d)))

