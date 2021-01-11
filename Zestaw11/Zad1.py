import random


def generate_random_list(n):
    resultArray = [x for x in range(n)]
    random.shuffle(resultArray)
    return resultArray


def generate_almost_sorted_list(n):
    arr = [x for x in range(n)]

    for i in range(n-1):
        random_index = random.randint(i, i+1)
        if random_index != i:
            arr[i], arr[random_index] = arr[random_index], arr[i]
    return arr


def generate_almost_sorted_reversed_list(n):
    array = generate_almost_sorted_list(n)
    array.reverse()
    return array


def generate_gauss_random_list(n):
    return [random.gauss(0, 1) for x in range(n)]


def generate_random_list_with_repetitions(n):
    from math import sqrt
    from math import floor
    k = floor(sqrt(n))
    return [random.randint(0, k) for x in range(n)]


if __name__ == '__main__':
    print(generate_random_list(10))
    print(generate_almost_sorted_list(10))
    print(generate_almost_sorted_reversed_list(10))
    print(generate_gauss_random_list(10))
    print(generate_random_list_with_repetitions(10))
