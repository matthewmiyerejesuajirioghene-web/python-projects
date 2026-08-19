while True:
    name = input("What is your name? ")

    if len(name) > 6:
        print("Name cannot be more than 15 characters" + "Try again!!!")
    else:
        print(f"Welcome, {name}")
        break
colour = input("What is your favourite colour? ")
print(name + " likes " + colour)