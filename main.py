from apps import filer, rng, timer


def parse_request(user_input):  # takes user_input and turns it into the valid app
    user_input = user_input.lower().split()

    if "timer" in user_input or "countdown" in user_input: # TODO: give the ability to use short phrase like "mins" and allow for the time to be inserted before the word timer ie "create a 5 minute timer"
        timer.timer(user_input)
    elif "random" in user_input and "number" in user_input:   
        rng.rng(user_input)
    elif "flip" in user_input and ("coin" in user_input or "coins" in user_input):
        rng.coin(user_input)
    elif "roll" in user_input:
        rng.dice(user_input)

    elif "open" in user_input and "filer" in user_input:
        filer.filer(user_input)

    elif "quit" in user_input:
        exit()
    else:
        main()

def main():
    parse_request(input("What is your request?: "))


if __name__ == "__main__":
    main()
