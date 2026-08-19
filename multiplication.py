import math
import random

print("""
THIS IS A MULTIPLICATION QUIZ
Testing your multiplication ability..
""")

while True:
    number = int(input("Enter a number: "))

    if number == 1:
        print("Enter another number!~a!")
        continue
    
#make the program not to accept 1
    correct_answer = number * 16.813

    print(f"What is 16.813 x {number}")
    options = [
        correct_answer,
        correct_answer + 5,
        correct_answer - 9,
        correct_answer + 10,
        correct_answer - 4,
    ]

    print(f"(a) {options[0]}")
    print(f"(b) {options[1]}")
    print(f"(c) {options[2]}")
    print(f"(d) {options[3]}")
    print(f"(e) {options[4]}")

    answer = input("What's your answer? ").lower()

    if answer == "a":
        selected = options[0]
    elif answer == "b":
        selected = options[1]
    elif answer == "c":
        selected = options[2]
    elif answer == "d":
        selected = options[3]
    elif answer == "e":
        selected = options[4]
    else:
        not_correct = print("INVALID OPTION")
        
    if selected == correct_answer:
        print("CORRECT!!!")
    else:
        print("Wrong!!!")