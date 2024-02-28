from random import randint
import re

# this is the main roll function
def roll_dice(num_dice=1, dice_sides=20):
    roll_list = []
    for _ in range(num_dice):
        roll = randint(1, dice_sides)
        roll_list.append(roll)
    return roll_list

# this parses the the input
def parse_roll(roll):
    # Regex for the roll forumula
    # TODO: validate xdy+z (ex: 1d20+5)
    match = re.match(r"(\d+)d(\d+)(?:\s*([tf])(\d+))?(?:\s+(.*))?", roll)
    outcome = ""
    outcome_text = ""

    try:
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))
        operator = match.group(3) if match.group(3) else ""
        target = int(match.group(4)) if match.group(4) else ""
        message = match.group(5) if match.group(5) else ""

        # the actual roll results and sum
        roll_results = roll_dice(num_dice, num_sides)
        roll_sum = sum(roll_results)

    # outcome statement
        if not target:
            outcome = "ROLL"
        else:
            if (roll_sum > target and operator == "f") or (roll_sum < target and operator == "t"):
                outcome = "FAILURE"
            elif (roll_sum < target and operator == "f") or (roll_sum > target and operator == "t"):
                outcome = "SUCCESS"
            elif roll_sum == target:
                outcome = "CRITICAL"

    except:
        print(f"ERROR: you typed it in like a dummy, try again.")



    return outcome, roll, roll_sum, message, target


# run the program!
while True:
    phrase = input(f"Type a roll phrase: (1d20 f10 Sword) (6d6): ")
    if phrase == "":
        print(f"Nothing input, try again.")
        continue
    elif phrase.lower() == "exit" or phrase.lower() == "quit":
        print(f"Thanks for playing.")
        break
    else:
        overall_results = parse_roll(phrase)
        print(overall_results)
