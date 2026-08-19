import math
user1 = input("Enter a value:(please enter 22)")
print("What is the result of mystery number plus 22?")
answer = print("""
    (a) 722
    (b) 40
    (c) 99
    (d) 111
""")
answer_select = int(input("What was your answer? "))
if answer_select == 722:
    print("You guessed correctly!!!")
print(int(user1) + 700)
#how to generate options for any value the user enters
print(math.ceil(2.9))