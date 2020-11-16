import math


def leastCommonMultiple(a, b):
    return (a * b) / math.gcd(a, b)


# frac1 + frac2
def add_frac(frac1, frac2):
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter = frac1[0] * (denominator / frac1[1]) + frac2[0] * (denominator / frac2[1])
    return [counter, denominator]


# frac1 - frac2
def sub_frac(frac1, frac2):
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter = frac1[0] * (denominator / frac1[1]) - frac2[0] * (denominator / frac2[1])
    return [counter, denominator]


# frac1 * frac2
def mul_frac(frac1, frac2):
    counter = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(counter, denominator)
    return [counter / gcd, denominator / gcd]


# frac1 / frac2
def div_frac(frac1, frac2):
    return mul_frac(frac1, frac2[::-1])


# bool, czy dodatni
def is_positive(frac):
    return frac[0] * frac[1] > 0


# bool, typu [0, x]
def is_zero(frac):
    return frac[0] == 0


# -1 | 0 | +1
def cmp_frac(frac1, frac2):
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter1 = frac1[0] * (denominator / frac1[1])
    counter2 = frac2[0] * (denominator / frac2[1])

    if counter1 > counter2: return 1
    elif counter2 > counter1: return -1
    else: return 0


# konwersja do float
def frac2float(frac):
    return float(frac[0] / frac[1])
