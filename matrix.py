matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)

numbers = [5, 3, 1, 7, 9, 3, 7, 33]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
numbers.insert(0, 111)
print(uniques)
