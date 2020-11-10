def sum_seq(sequence):
    sum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum += sum_seq(element)
        else:
            sum += element
    return sum


sourceList = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Suma elementów: ", sum_seq(sourceList))
