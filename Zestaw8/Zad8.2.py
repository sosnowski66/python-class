def calc_delta(a, b, c):
    return b ** 2 - (4 * a * c)


def solve2(a, b, c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    delta = calc_delta(a, b, c)

    if delta < 0 :
        print("Brak rozwiązań")

    elif delta == 0:
        print("x = {}".format(-b / (2 * a)))

    else:
        from math import sqrt
        delta_sqrt = sqrt(delta)
        print("x1 = {0}, x2 = {1}".format((-b - delta_sqrt) / (2 * a), (-b + delta_sqrt) / (2 * a)))


solve2(1, 6, 9)
solve2(1, 4, 3)