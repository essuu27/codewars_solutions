# Given two integers a and b, return the sum of the numerator and the
#  denominator of the reduced fraction a/b.

from fractions import Fraction

def fraction(a,b):
    (i, j) = Fraction(a / b).limit_denominator().as_integer_ratio()
    return(i + j)
