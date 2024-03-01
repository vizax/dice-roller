from random import randint
import re


# this is the main roll function
def roll_dice(num_dice=1, dice_sides=20):
    roll_list = []
    for _ in range(num_dice):
        roll = randint(1, dice_sides)
        roll_list.append(roll)
    return roll_list


# this parses the the input text
def parse_roll(roll):
    # Regex for the roll forumula
    match = re.match(r"(\d+)d(\d+)(?:([\*])(\d+))?(?:\s*([tf])(\d+))?(?:\s+(.*))?", roll)
    outcome = ""

    try:
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))
        multiplier_used = match.group(3) if match.group(3) else ""
        multiplier = int(match.group(4)) if match.group(4) else ""
        operator = match.group(5) if match.group(5) else ""
        target = int(match.group(6)) if match.group(6) else ""
        message = match.group(7) if match.group(7) else ""
        over20 = None

        # the actual roll results          
        roll_results = roll_dice(num_dice, num_sides)

        # sum results and check for stats over 20 to adjust the roll_sum
        if target != "" and target > 20:
            over20 = target - 20
            roll_sum = sum(roll_results) + over20
        else:
            roll_sum = sum(roll_results)
        
        # test for multiplier 
        if multiplier_used != "":
            roll_sum = roll_sum * multiplier

        # outcome statement
        if not target:
            outcome = "ROLL"
        else:
            if (operator == "f" and target < 20 and roll_sum == 20):
                outcome = "CRITICAL FAILURE"
            elif (roll_sum == target) or (target >= 20 and roll_sum >= 20):
                outcome = "CRITICAL"
            elif (roll_sum > target and operator == "f") or (roll_sum < target and operator == "t"):
                outcome = "FAILURE"
            elif (roll_sum < target and operator == "f") or (roll_sum > target and operator == "t"):
                outcome = "SUCCESS"
            
    except:
        print(f"ERROR: you typed it in like a dummy, try again.")

    # rebuild die roll for output purposes
    dice_input = f"{num_dice}d{num_sides}"

    return outcome, dice_input, over20, multiplier_used, multiplier, roll_results, roll_sum, message, target


# run the program!
while True:
    phrase = input(f"Type a roll phrase: (1d20 f10 Sword) (6d6) (quit/exit): ")
    if phrase == "":
        print(f"Nothing input, try again.")
        continue
    elif phrase.lower() == "exit" or phrase.lower() == "quit":
        print(f"Thanks for playing.")
        break
    else:
        overall_results = parse_roll(phrase)
        
        # tweak the output to hide unused bits
        if overall_results[2] != None:
            # used for the bonus if the skill is over 20
            sentence_bonus = f"+{overall_results[2]}"
        else:
            sentence_bonus = ""
            
        if overall_results[8] != "":
            # used if ther is no target provided
            sentence_target = f"({overall_results[8]})"
        else:
            sentence_target = ""
        
        if overall_results[3] != "":
            multiplier_bonus = f"*{overall_results[4]}"
        else:
            multiplier_bonus = ""
            
        output_sentence = f"{overall_results[0]}: {overall_results[1]}{sentence_bonus}{multiplier_bonus} = {overall_results[5]}{multiplier_bonus} = {overall_results[6]} {overall_results[7]}{sentence_target}"
        print(output_sentence)
