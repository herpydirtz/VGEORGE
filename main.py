# imports
from timer import timer # allows us to call timer() from timer.py
from rng import rng

# classes

# methods
def parseRequest(user_input): # takes user_input and turns it into the valid app
    try:
        user_input = user_input.split()
    except:
        print("invalid input")
        return "error"

    if "timer" in user_input:
        return "timer"
    if "countdown" in user_input:
        return "timer"
    if "random" in user_input:
        return "rng"

# main loop
def main():
    user_input = input("What is your request?: ")
    user_input = parseRequest(user_input) # turn user input into the requested app
    
    if user_input == "timer": # start timer method if timer requested
        timer()
    elif user_input == "random": # user would likely say "give me a random number from _ to _ "
        rng()
    elif user_input == "quit": # end program if user asks to quit
        quit
    else: # try again if error
        main()

if __name__ == "__main__":
    main()