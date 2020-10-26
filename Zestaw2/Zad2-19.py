L = [1, 198, 26, 166, 14, 3]

output = ""
for elem in L:
    output += str(elem).zfill(3) + " "

print(output.strip())