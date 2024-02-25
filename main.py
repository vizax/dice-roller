from random import randint
import re
from termcolor import colored


def roll_dice(num_dice=1, dice_sides=20):
    roll_list = []
    for _ in range(num_dice):
        roll = randint(1, dice_sides)
        roll_list.append(roll)
    return roll_list


def parse_roll(roll):
    # Regex for the roll forumula
    match = re.match(r"(\d+)d(\d+)(?:\s*([tf])(\d+))?(?:\s+(.*))?", roll)

    # number of dicde check
    if not match.group(1).isdigit() or int(match.group(1)) <= 0:
        print(
            colored(
                "Number must be a positive integer", "red", attrs=["bold", "underline"]
            )
        )
        pass
    else:
        num_dice = int(match.group(1))

    # dice sides check
    if not match.group(2).isdigit() or int(match.group(2)) <= 0:
        print(
            colored(
                "Number must be a positive integer", "red", attrs=["bold", "underline"]
            )
        )
        pass
    else:
        num_sides = int(match.group(2))

    # the actual roll
    roll_results = roll_dice(num_dice, num_sides)
    roll_sum = sum(roll_results)

    # "f" or "t" for play style or level style
    operator = match.group(3) if match.group(3) else ""

    # target number
    if not match.group(4):
        target = None
        pass
    elif not match.group(4).isdigit() or int(match.group(4)) <= 0:
        print(
            colored(
                "Number must be a positive integer", "red", attrs=["bold", "underline"]
            )
        )
        pass
    else:
        target = int(match.group(4))

    # skill or roll message
    message = match.group(5) if match.group(5) else ""

    # outcome statement
    if not target:
        outcome = colored(
            f"ROLL: {num_dice}d{num_sides}: {roll_results} = {roll_sum}", "white",
        )
    else:
        if roll_sum > target:
            if operator == "f":
                outcome = colored(
                    f"FAILURE: {num_dice}d{num_sides}: {roll_results}={roll_sum} which is greater than the {message}({target}",
                    "red",
                )
            if operator == "t":
                outcome = colored(
                    f"SUCCESS: {num_dice}d{num_sides}: {roll_results}={roll_sum} which is less than the {message}({target})",
                    "green",
                )
        elif roll_sum < target:
            if operator == "t":
                outcome = colored(
                    f"FAILURE: {num_dice}d{num_sides}: {roll_results}={roll_sum} which is greater than the {message}({target})",
                    "red",
                )
            if operator == "f":
                outcome = colored(
                    f"SUCCESS: {num_dice}d{num_sides}: {roll_results}={roll_sum} which is less than the {message}({target})",
                    "green",
                )
        elif roll_sum == target:
            outcome = colored(
                f"CRITICAL: {num_dice}d{num_sides}: {roll_results}={roll_sum} which is exactly {message}({target})",
                "yellow",
                attrs=["blink", "bold"],
            )

    return outcome


# run the program!
while True:
    phrase = input(
        colored("type roll phrase: (1d20 f10 Sword)", attrs=["bold", "underline"])
    )
    if phrase == "":
        print(colored(f"Nothing input, try again.", "red"))
        continue
    elif phrase.lower() == "exit" or phrase.lower() == "quit":
        print(colored(f"Thanks for playing.", "green"))
        break
    else:
        print(parse_roll(phrase))
