# imports
from timer import timer # allows us to call timer() from timer.py
from rng import rng


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
    if "random" and "number"in user_input:
        return "rng"    #word rng, in main function when calling it will call rng


def main():
    user_input = input("What is your request?: ")
    # turn user input into the requested app
    user_input = parse_request(user_input)

    if user_input == "timer":  # start timer method if timer requested
        timer()
    elif user_input == "rng": # user would likely say "give me a random number from _ to _ "
        rng()
    elif user_input == "quit": # end program if user asks to quit
        quit
    elif user_input == "quit":  # end program if user asks to quit
        exit()
    else:  # try again if error
        main()


if __name__ == "__main__":
    main()
