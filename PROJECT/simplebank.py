# Project: Banking system illustration
# Author: Matthew Ajiri
# Date: 18/07/2026
# Description: It has an home module similar to an actual bank with varios functions that can be carried out by the bank
print("WELCOME TO MATTHEW BANK")
print("    ")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("Assuming balance is $100")

option = int(input("Select a number from the list: "))

if option == 1:
    balance = int(input(print("What amount should be deposited: ")))
    print(f"Your new balance is ${balance +100}")
elif option == 3:
    print("Your balance is $100")
elif option == 2:
    print("Withdrawal feature coming soon.")
else:
    print("")