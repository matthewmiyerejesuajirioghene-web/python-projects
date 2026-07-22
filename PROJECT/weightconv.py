weight = int(input("Enter your weight: "))
unit = input("(L)bs or (k)g: ")

if unit.upper() == "L":
    print(f"Your weight is {weight *0.45}Kg")
    print(f"We converted your weight {weight}Lbs to Kg")
elif unit.upper() == "K":
    print(f"Your weight is {weight /0.45}Lbs")
    print(f"We converted your weight {weight}Kg to Lbs")
else:
    print("Please initiate process again")