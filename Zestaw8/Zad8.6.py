import time

class DynamicP:
    def __init__(self):
        self.values = {(0, 0): 0.5, (0, 1): 1, (1, 0): 0}

    def calc_p(self, i, j):
        if (i, j) in self.values.keys():
            return self.values.get((i, j))
        elif i == 0:
            return 1
        elif j == 0:
            return 0
        else:
            self.values[(i, j)] = 0.5 * (self.calc_p(i - 1, j) + self.calc_p(i, j - 1))
            return self.values.get((i, j))


def calc_p_rec(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (calc_p_rec(i - 1, j) + calc_p_rec(i, j - 1))



dynamic = DynamicP()

dynamic_start = time.time()
print("Dynamiczna = {}".format(dynamic.calc_p(15, 11)))
dynamic_end = time.time()
recursive_start = time.time()
print("Rekurencyjna = {}".format(calc_p_rec(15, 11)))
recursive_end = time.time()

print("Dynamiczna wersja: {} s".format(dynamic_end - dynamic_start))
print("Rekurencyjna wersja: {} s".format(recursive_end - recursive_start))