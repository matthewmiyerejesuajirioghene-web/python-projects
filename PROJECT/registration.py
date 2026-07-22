# Project: Student registration system
# Author: Matthew Ajiri
# Date: 19/07/2026
# Description: A simple system to register into a school

full_name = input("What is your full name: ")
age = int(input("Enter your age: "))
mat_number = input("What's your matric number: ")
university = input("What university do you attend: ")
department = input("What's your department(IN SCHOOL):")
level = input("What level are you: ")
language = input("What's your favorite programming language: ")

print("             ")
print("WELCOME TO EDO UNIVERITY")
print("                         ")
print("Registration Succesful")
print("                ")
print("Student Details")
print("------------------------")
print(f"Name: {full_name.upper()}")
print(f"Age: {age}")
print(f"Matric No: {mat_number}")
print(f"Department: {department}")
print(f"Level: {level}")
print(f"Programming Language: {language}")