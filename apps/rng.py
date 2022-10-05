import random


def coin(user_input):
    num_of_coins = 1
    if "coins" in user_input:
        try:
            num_of_coins = int(user_input[user_input.index("coins") - 1])
        except ValueError:
            num_of_coins = 1
    for _ in range(num_of_coins):
        print("Heads" if random.randint(0, 1) == 0 else "Tails")


def dice(user_input):
    num_of_dice = 1
    multiplier = 1
    for word in user_input:
        if parse_dice_string(word) == None:
            continue
        else:
            num_of_dice, multiplier = parse_dice_string(word)
            if num_of_dice <= 1:
                try:
                    num_of_dice = int(user_input[user_input.index(word) - 1])
                except ValueError:
                    num_of_dice = 1
            break
    for _ in range(num_of_dice):
        print(random.randint(1, multiplier))


def parse_dice_string(dice_string):
    if dice_string == "dice":
        return 1, 6
    else:
        dice_string = dice_string.split('d')
        if len(dice_string) == 2:
            try:
                return 1 if dice_string[0] == '' else int(dice_string[0]), int(dice_string[1])
            except ValueError:
                return None
        else:
            return None


def rng(user_input):  # TODO: add flip coin and roll dice
    num_range = []

    for word in user_input:
        try:
            num = int(word)
            num_range.append(num)
        except ValueError:
            continue

    if len(num_range) >= 2:
        print(random.randint(num_range[0], num_range[1]))
    else:
        print("Couldn't compute range.")
