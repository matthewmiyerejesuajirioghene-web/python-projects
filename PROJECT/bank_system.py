# Banking System Using OOP
# Parent class: User
# Holds details about a user
# Has a function to show user details

# Child class: Bank
# Stores details about the acount balance
# Stores details about the amount
# Allows for deposits, withdraw and view_balance

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        pass

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated:$ ", self.balance)

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insufficient Funds!!")
            print("Balance Available:$ ", self.balance)
        else:
            self.balance = self.balance - amount
            print("Account balance has beeen updated ")
            print("$", self.balance)

    def view_balance(self):
        print()
        print("=======ACCOUNT DETAILS========")
        self.show_details()
        print("$", self.balance)
        print("======================")

name = input("What is your name: ")
age = int(input("What's your age: "))
gender = input("What's your gender: ")

account = Bank(name, age, gender)

while True:

    print("Welcome to the bank")
    print("")
    print("""
    1. Deposit
    2. View Account Balance
    3. Withdraw
    4. View Account Details
    0. Exit
    """)

    print("Your current balance:", account.balance)
    selection = input("Choose an option: ")
    if selection == "1":
        print("Welcome to the deposit page")
        amount = float(input("How much are depositing today: "))
        account.deposit(amount)
    elif selection == "2":
        print("Welcome to the balance page")
        print("Your balance is", account.balance)
    elif selection == "3":
        print("Welcome to the withdrawal page")
        amount = float(input("How much are you withdrawing today? "))
        account.withdraw(amount)
    elif selection == "4":
        print("Welcome to your acoount details")
        account.view_balance()
    elif selection == "0":
        print("Thank you for banking with us.")
        print("Goodbye")
        break
    else:
        print("Invalid option. Please choose 0, 1, 2, 3 or 4.")