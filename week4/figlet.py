# import Figlet and sys modules
# check validity of input. must be 0 or 2 arguments, if 2 arguments, 1st must be either -f or --font, 2nd is font name
# if 2 arguments provided is not in correct fomrat, sys.exit()
# using Figlet, we can get list of fonts, set list of fonts and print list of fonts

from pyfiglet import Figlet
from random import choice
import sys


figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(text))
    elif len(sys.argv) == 3:
        if not validity(sys.argv[1], sys.argv[2]):
            sys.exit("Invalid usage")
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")


def validity(format, font):
    if len(sys.argv) == 1:
        return True
    elif (len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts()):
        return True
    else:
        return False


main()