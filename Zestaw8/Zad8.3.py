import random
from math import sqrt


def get_distance(x, y):
    return sqrt(x * x + y * y)


def calc_pi(n=100):
    circle_counter = 0
    random.getstate()

    for i in range(n):
        x = random.random()
        y = random.random()

        distance = get_distance(x, y)

        if distance <= 1:
            circle_counter += 1

    return 4 * (circle_counter / n)


print(calc_pi(50))
print(calc_pi())
print(calc_pi(200))
