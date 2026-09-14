numbers = [9, 2, 3, 4, 4, 2, 9, 11, 23, 3]
numbers.sort(reverse=True)
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)