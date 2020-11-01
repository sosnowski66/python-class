while True:
    try:
        x = input("Podaj liczbe: ")
        x_number = float(x)
        print("x = ", x_number, ", x^3 = ", x_number**3)
    except ValueError:
        if x == "stop": break
        print("To nie jest liczba")
