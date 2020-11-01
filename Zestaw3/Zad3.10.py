def isValidRomanNumber(number):
    validChars = ('I', 'V', 'X', 'L', "C", "D", 'M')

    for i in number:
        if i not in validChars:
            return False;

    counter = 1

    for index, value in enumerate(validChars):
        if (index + 1) < len(number) and value == number[i] and value in ('I', 'X', 'C', 'M'):
            ++counter
        else:
            counter = 1

        if counter > 3:
            return False

        if (index + 1) < len(number) and value in ('V', 'L', 'D') and number[i] in ('V', 'L', 'D'):
            return False

        return True


def roman2int(roman):
    romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultValue = 0
    for i in range(len(roman)):
        if i > 0 and romanValues[roman[i]] > romanValues[roman[i - 1]]:
            resultValue += romanValues[roman[i]] - 2 * romanValues[roman[i - 1]]
        else:
            resultValue += romanValues[roman[i]]
    return resultValue


romanInputNumber = input('Podaj liczbę w systemie rzymskim: ')

print(roman2int(romanInputNumber))
