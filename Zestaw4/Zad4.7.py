def flatten(sequence):
    result = []
    return flattenHelper(sequence, result)


def flattenHelper(sequence, result):
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flattenHelper(element, result)
        else:
            result.append(element)
    return result


sourceList = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Spłaszczona lista elementów: ", flatten(sourceList))
