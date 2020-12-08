def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Równanie tożsamościowe")
            else:
                print("Rówanie sprzeczne")
        else:
            if c == 0:
                print("y = 0 \n x - dowolne")
            else:
                print("y = {}, x - dowolne".format(- c / b))
    else:
        if b == 0:
            if c == 0:
                print("x = 0, y - dowolne")
            else:
                print("x = {}, y - dowolne".format(- c / a))
        else:
            if c == 0:
                print("y = {}x".format(- a / b));
            else:
                print("y = {}x + ({})".format(- a / b, - c / b))


print("Równanie: 3x + 6y + 9 = 0")
solve1(3, 6, 9)
print("Równanie: 3x + 6y + 8 = 0")
solve1(3, 6, 8)
print("Równanie: 2x + 5y - 1 = 0")
solve1(2, 5, -1)
