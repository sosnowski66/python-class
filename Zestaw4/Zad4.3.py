def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1

    return result


print(factorial(5))