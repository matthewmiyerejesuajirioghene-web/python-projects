# Project: Drawing letter F with a for loop
# Author: Matthew Ajiri
# Date: 22/07/2026
# Description: The program draws letter 'F' as an output

numbers = [5, 2, 5, 2, 2,]

for no in numbers:
    output = ''
    for count in range(no):
        output += 'x'
    print(output)