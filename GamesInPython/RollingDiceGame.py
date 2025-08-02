#take input from user
#ask them if they want to roll the dice
#if they say yes:
#   print random numbers of the both dices
#if they say no:
#   Break the loop and thank the user for playing the game
import random
while True:
    number = input("Want to roll the dice? (yes/no)").lower()
    if number == "yes":
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"{dice_1},{dice_2}")
    elif number == "no":
        print("Thank you for Playing... Have a nice day!!")
        break
    else:
        print("Invalid Character")