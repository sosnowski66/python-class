def odwracanie_iter(L, left, right):
    counter = 0
    for i in range(left, right + 1):
        if counter >= (right - left + 1) / 2:
            break

        L[i], L[right - counter] = L[right - counter], L[i]
        counter += 1

    return L


def odwracanie_rek(L, left, right):
    if left == right:
        return L

    L[left], L[right] = L[right], L[left]

    return odwracanie_rek(L, left + 1, right - 1)



L1 = [x**2 for x in range(10)]
L2 = [x**2 for x in range(10)]
print(odwracanie_iter(L1, 3, 7))
print(odwracanie_rek(L2, 3, 7))

