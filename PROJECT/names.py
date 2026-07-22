while True:
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty.")
    elif not name.replace(" ", "").isalpha():
        print("Name should contain only letters.")

    elif len(name) < 3:
        print("Name must at least be 3 characters long")
    elif len(name) > 10:
        print("Name must be a maximum of 10 charcters")
    else:
        print(f"{name} looks good")
        break