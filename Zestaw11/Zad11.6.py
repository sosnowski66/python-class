from Zestaw11.Zad1 import *
from collections import deque


def partition(array, begin, end):
    pivot = array[end]
    pivot_index = begin
    for i in range(begin, end):
        if array[i] < pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1

    array[pivot_index], array[end] = array[end], array[pivot_index]
    return pivot_index


def q_sort(array):
    stack = deque()
    begin = 0
    end = len(array)
    stack.append((begin, end - 1))
    while stack:
        begin, end = stack.pop()
        pivot_index = partition(array, begin, end)
        if pivot_index - 1 > begin:
            stack.append((begin, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))


if __name__ == '__main__':
    a = generate_random_list(20)
    b = generate_almost_sorted_list(20)
    c = generate_almost_sorted_reversed_list(20)
    d = generate_gauss_random_list(20)
    e = generate_random_list_with_repetitions(20)

    print("Nie posortowane listy")
    print("a) ", a)
    print("b) ", b)
    print("c) ", c)
    print("d) ", d)
    print("e) ", e)

    q_sort(a)
    q_sort(b)
    q_sort(c)
    q_sort(d)
    q_sort(e)


    print("Po sortowaniu")
    print("a) ", a)
    print("b) ", b)
    print("c) ", c)
    print("d) ", d)
    print("e) ", e)



