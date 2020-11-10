# ZAD 3.5
def getNumberInterval(number):
    result = " " * (5 - len(str(number)))
    return result + str(number)


def getRuller(n):
    result = "|" + INTERVAL * n + "\n";

    result += "0"
    for i in range(n):
        result += getNumberInterval(i + 1)

    return result


INTERVAL = "....|"

# n = int(input("Podaj długość miarki: "))
# if n < 0:
#     print("Długość nie może być ujemna")
#     exit(1)

# print(getRuller(n))



# ZAD 3.6

def drawLine(elements, n):
    return elements[0] + elements[1] * n +"\n"

def drawRectangle(width, height):
    tmp = (drawLine(HORIZONTAL, width) * (height + 1)).splitlines()
    verticalLines = [x + "\n" for x in tmp];

    return drawLine(VERTICAL, width).join(verticalLines)


HORIZONTAL = ("+", "---+")
VERTICAL = ("|", "   |")

height, width = [int(x) for x in input("Podaj wysokość i szerokość: ").split()]

if height < 1 and width < 1:
    print("Minimalne wartości to 1")
    exit(1)

print(drawRectangle(width, height))

