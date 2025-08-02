import random
number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > number_to_guess:
            print("Too high!!")
        elif guess< number_to_guess:
            print("Too low!!")
        else:
            print("Yay!!!! you found it!!")
            break
        
    except ValueError:
        print("Please enter a valid number---")