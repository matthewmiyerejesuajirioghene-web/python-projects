import random

name = input("What is your name? ")
class_sch = input("What class are you in now? ")
print("""
THIS IS A MULTIPLICATION QUIZ
""")
question = input("Are you ready(YES/NO)? ").upper

if question == "No":
    print("YOU WILL STILL ANSWER MY QUIZ^a^a")

number = random.randint(1, 28)

correct_answer = number * 16.634

wrong1 = correct_answer - 1
wrong2 = correct_answer * 5
wrong3 = correct_answer - 8
wrong4 = correct_answer + 5

options = [
    correct_answer,
    wrong1,
    wrong2,
    wrong3,
    wrong4
]
random.shuffle(options)

print(f"What is 16.634 x {number}? ")

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

if selected == correct_answer:
    print("HURRAY. YOU JUST WON A MILLION NAIRA!!")
else:
    print("Nope, wrong. TRY AGAIN LATER...")