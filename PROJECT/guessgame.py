# Project: Guessing Game
# Author: Matthew Ajiri
# Date: 17/07/2026
# Description: A number guessing game where the user has 3 attempts to guess the secret number
# program also hints if guess is too high or too low

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess:(It should be a number): "))
    guess_count += 1
    if guess > secret_number:
        print("Too high!!!")
    elif guess < secret_number:
        print("Too low")
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failedf') 