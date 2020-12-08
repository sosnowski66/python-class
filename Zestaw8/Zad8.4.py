from math import sqrt


def heron(a, b, c):
    if not is_triangle(a, b, c):
        raise ValueError("Nie spelniony warunek trojkata")

    p = (a + b + c) / 2
    multiplying = p * (p - a) * (p - b) * (p - c)

    return sqrt(multiplying)




def is_triangle(a, b, c):
    sides = [a, b, c]
    longest_side = max(sides)
    sides.remove(longest_side)

    return longest_side < sum(sides)


print(heron(3, 4, 5))
try:
    print(heron(3, 5, 8))
except ValueError as e:
    print(str(e))