from timer import timer  # allows us to call timer() from timer.py


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


def main():
    user_input = input("What is your request?: ")
    # turn user input into the requested app
    user_input = parse_request(user_input)

    if user_input == "timer":  # start timer method if timer requested
        timer()
    elif user_input == "quit":  # end program if user asks to quit
        exit()
    else:  # try again if error
        main()


if __name__ == "__main__":
    main()
