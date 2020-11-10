def fibonacci(n):
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1

        for i in range(2, n):
            c = a + b
            a = b
            b = c

        return b


print(fibonacci(9))