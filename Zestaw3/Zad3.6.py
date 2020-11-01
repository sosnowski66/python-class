
def drawLine(elements, n):
    return elements[0] + elements[1] * n +"\n"




height, width = [int(x) for x in input("Podaj wysokość i szerokość: ").split()]
# height, width = input("Podaj wysokość i szerokość: ").split()

if height < 1 and width < 1:
    print("Minimalne wartości to 1")
    exit(1)


HORIZONTAL = ("+", "---+")
VERTICAL = ("|", "   |")

resultString = ""

for i in range(height):
    resultString += drawLine(HORIZONTAL, width)
    resultString += drawLine(VERTICAL, width)

resultString += drawLine(HORIZONTAL, width)

print(resultString)
