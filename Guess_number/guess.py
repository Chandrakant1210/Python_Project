import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)



inp=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def easy():
    print("you have 10 chances to guess the number")
    num = random.randint(1, 100)
    for i in range(10):
        guess = int(input("Guess the number"))
        if guess == num:
            print("You guessed the number")
            return
        elif guess > num:
            print("Too high")
        else:
            print("Too low")
    print("you have ran out of guesses")



def Diff():
    print("you have 5 chances to guess the number")
    num = random.randint(1, 100)
    for i in range(5):
        guess = int(input("Guess the number"))
        if guess == num:
            print("You guessed the number")
            return
        elif guess > num:
            print("Too high")
        else:
            print("Too low")
    print("you have ran out of guesses")


if inp=="easy":
    easy()
else:
    Diff()