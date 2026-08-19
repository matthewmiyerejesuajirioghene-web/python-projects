user_weight = input("Enter your weight?(in pounds)")
user_age = input("Enter your date of birth: ")
new_weight = 20 * int(user_weight)
new_age = 2026 - int(user_age)
print("Your weight is " + str(new_weight))
print(f"Your age now is {new_age}")

if new_age < 18:
    print("You can't use this service")
else:
    print("You are eligible")