import os

def filer(user_input):
    answer = input("What would you like to file?")
    try:
        with open(answer) as file:
            print(file.read())
    except FileNotFoundError:
        print("File could not be found")