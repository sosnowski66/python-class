
def getNumberInterval(number):
    result = " " * (5 - len(str(number)))
    return result + str(number)



INTERVAL = "....|"

resultString = "|"

n = int(input("Podaj długość miarki: "))
if n < 0:
    print("Długość nie może być ujemna")
    exit(1)

resultString += INTERVAL * n + "\n"

resultString += "0"
for i in range(n):
    resultString += getNumberInterval( i +1)

print(resultString)
