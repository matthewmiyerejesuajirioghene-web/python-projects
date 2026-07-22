temperature = float(input("What is the temperature? "))
temperature
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = input("Enter your name? ")

if len(name) <= 3:
    print("Name must be at least 3 characters long")
    input("Enter a longer name? ")
elif len(name) >= 10:
    print("Name is just too long")
    input("Enter a shorter name? ")
    print("Name looks good")
else:
    print("Name looks good")