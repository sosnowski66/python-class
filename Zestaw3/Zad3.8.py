import random

# s = random.getstate()

firstSequence = [random.randint(1, 10) for i in range(5)]
secondSequence = [random.randint(1, 10) for j in range(5)]

print('Pierwsza lista: ', firstSequence)
print('Druga lista: ', secondSequence)

sameElements = set()

for i in firstSequence:
    if i in secondSequence:
        sameElements.add(i)

print('Wspólne elementy', sameElements)

allElements = set(firstSequence).union(secondSequence)
print('Wszystkie elementy: ', allElements)
