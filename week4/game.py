# prompt user for a level(n), reprompt if invalid format(postive integer only)
# use random module to randomly generate number from 1 to n
# ask for guesses, keep reprompting until guess is right

import random
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
            if validate(level):
                break
        except ValueError:
            pass
    random_number = random.randint(1, level)
    while True:
        try:
            answer = int(input("Guess: "))
            if answer > random_number:
                print("Too large!")
            elif answer < random_number:
                print("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


def validate(input):
    if str(input).isdigit() and input != 0:
        return True
    else:
        return False


main()