<<<<<<< HEAD
# imports
from timer import timer # allows us to call timer() from timer.py
from rng import rng
=======
from timer import timer  # allows us to call timer() from timer.py
>>>>>>> 6db690b65101dd4998bf2c4dd76d612c4603e4c8


def parse_request(user_input):  # takes user_input and turns it into the valid app
    try:
        user_input = user_input.split()
    except TypeError:
        print("invalid input")
        return "error"

    if "timer" in user_input:
        return "timer"
    if "countdown" in user_input:
        return "timer"
    if "random" in user_input:
        return "rng"


def main():
    user_input = input("What is your request?: ")
    # turn user input into the requested app
    user_input = parse_request(user_input)

    if user_input == "timer":  # start timer method if timer requested
        timer()
<<<<<<< HEAD
    elif user_input == "random": # user would likely say "give me a random number from _ to _ "
        rng()
    elif user_input == "quit": # end program if user asks to quit
        quit
    else: # try again if error
=======
    elif user_input == "quit":  # end program if user asks to quit
        exit()
    else:  # try again if error
>>>>>>> 6db690b65101dd4998bf2c4dd76d612c4603e4c8
        main()


if __name__ == "__main__":
    main()
