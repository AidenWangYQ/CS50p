# catch exceptions
# calculate fuel percentage
# consider E and F cases
# set up infinite loop, capture errors, continue loop if conditionals not met
def main():
    while True:
        try:
            fuel = input("Fraction: ")
            while not validated(fuel):
                fuel = input("Fraction: ")
            x, y = fuel.split("/")
            x = float(x)
            y = float(y)
            if (x <= y):
                percentage = round((x/y) * 100)
                if 0 <= percentage <= 1:
                    print("E")
                elif 99 <= percentage:
                    print("F")
                else:
                    print(f"{percentage}%")
                break
        except (ValueError, ZeroDivisionError):
            pass
# double check that input given has "/" in it and x and y are both integers, or else returns False, which is looped for reprompt in main


def validated(string):
    if not "/" in string:
        return False
    x, y = string.split("/")
    return x.isnumeric() and y.isnumeric()


main()