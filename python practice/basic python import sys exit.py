#number game
import random

secretnum = random.randint(1,20)
print("guess a number between 1 to 20")

for guesses in range(1,7):
    guess = int(input("take a guess : "))

    if guess < secretnum:
        print("your guess is too low ")
    elif guess > secretnum:
        print("your guess is too high")
    else:
        break
print("your guess is correct the number is : ", str(secretnum))