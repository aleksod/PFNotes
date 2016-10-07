import random

def roll_die():
   '''
   Input:  None
   Output: Int - Between 1 and 6

   Using random.randint(), perform a die roll and return the number that "comes up".
   '''
   return random.randint(1,6)

def roll_combo(n_times):
    return [roll_die() for _ in range(n_times)]

def die_sum(die_combo):
    temp_sum = 0
    for i in die_combo:
        temp_sum += i
    return temp_sum

def who_won(total1, total2):
    if total1 > total2:
        return "Player 1 wins!"
    elif total1 < total2:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

def model_dice_rolls(p1, p2):
    p1_roll = roll_combo(p1)
    p2_roll = roll_combo(p2)

    p1_total = die_sum(p1_roll)
    p2_total = die_sum(p2_roll)

    print who_won(p1_total, p2_total)
    return (p1_total, p2_total)

var1 = model_dice_rolls(6,7)
print var1
