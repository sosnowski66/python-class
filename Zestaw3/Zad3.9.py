import random

def init_list():
    resultList = []
    for i in range(10):
        resultList.append([random.randint(1, 10) for i in range(random.randint(0, 10))])

    return resultList

sourceList = init_list()

resultList = [len(sourceList[i]) for i in range(len(sourceList))]

print("Lista wejsciowa: ", sourceList)
print("Liczba elementow w poszczegolnych listach: ", resultList)


