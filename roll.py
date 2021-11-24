import random

# roll a "die" some number of times.

def main ():
    rollback = dice_roller()

def dice_roller():

    roll_dice = input("Do you want to roll the dice? Y/N")

    if roll_dice == "y":
        nums = [1,2,3,4,5,6]
        result1 = random.choice(nums)
        print(result1)

    turns = input("How many dice do you want to roll?")

    if roll_dice == "y" and turns == "2":
        nums = [1,2,3,4,5,6]
        result1 = random.choice(nums)
        result2 = random.choice(nums)
        print(result1)
        print(result2)

    roll_dice = input("Do you want to roll the dice? Y/N")
    turns = input("How many dice do you want to roll?")

    if roll_dice == "y" and turns == "3":
        nums = [1,2,3,4,5,6]
        result1 = random.choice(nums)
        result2 = random.choice(nums)
        result3 = random.choice(nums)
        print(result1)
        print(result2)
        print(result3)
    else:
        return ("INVALID")


dice_roller()









# roll - run it once and go into a loop

# roll 1 - produce a number 1-6 random and print it

# roll 2 - produce two numbers 1-6 and print them

# roll 3 - produce three numbers and print them.




