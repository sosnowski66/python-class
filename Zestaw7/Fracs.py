from math import gcd


def least_common_multiple(a, b):
    return (a * b) // gcd(a, b)


def to_common_denominator(frac1, frac2):
    y = least_common_multiple(frac1.y, frac2.y)
    x1 = frac1.x * (y / frac1.y)
    x2 = frac2.x * (y / frac2.y)
    return Frac(x1, y), Frac(x2, y)


class Frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Nie może być zera w mianowniku")

        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x == frac2.x

    def __ne__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return not frac1 == frac2

    def __lt__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x < frac2.x

    def __le__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x <= frac2.x

    def __gt__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x > frac2.x

    def __ge__(self, other):
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x >= frac2.x

    def __add__(self, other):
        if isinstance(other, Frac):
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) + other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(other, int):
            """frac1 + int"""
            x = self.x + other * self.y
            y = self.y
            return Frac(x, y)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            """frac1 - frac2"""
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) - other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, int):
            """frac1 - int"""
            x = self.x - other * self.y
            y = self.y
            return Frac(x, y)

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            x = self.x * other.x
            y = self.y * other.y
            _gcd = gcd(x, y)
            return Frac(x // _gcd, y // _gcd)
        elif isinstance(self, Frac) and isinstance(other, int):
            x = self.x * other
            y = self.y
            _gcd = gcd(x, y)
            return Frac(x // _gcd, y // _gcd)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            return self * ~other
        elif isinstance(self, Frac) and isinstance(other, int):
            return self * Frac(1, other)
        else:
            return Frac()

    def __rtruediv__(self, other):
        return other * ~self

    def __pos__(self):
        return self

    def __neg__(self):
        return -1 * self

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return float(self.x / self.y)
