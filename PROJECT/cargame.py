#--------------------------
# Project: Car Game
# Date: 21/07/2026
# Author: Matthew Ajiri
# Description: It is a simple command-line car simulation written in python
# Commands:
# start: Starts the car
# stop: stops the car
# help: Displays available commands
# quit: exits the program
#
#---------------------------

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, i don't understand that")