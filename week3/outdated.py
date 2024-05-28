# goal: change format of date
# request for date, in specific format, or else reprompt
# split valid date into their respective year, month and day
# print out new formatted date, with leading 0 for month and day if necessary
import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ").strip()
        if not validate(date):
            continue
        else:
            format(date)
            break


# date must be in x/x/xxxx or month x, xxxx format, where x is an integer from 0-9
def validate(string):
    if "/" in string:
        a, b, c = string.split("/")
        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            return False
        if 1 <= int(a) <= 12 and 1 <= int(b) <= 31 and 1 <= int(c) <= 9999:
            return True
    else:
        if "," in string:
            parts = string.split(",")
            a, b = parts[0].split(" ")
            c = parts[1].strip()
            a = a.title()
            if a in months and 1 <= int(b) <= 31 and 1 <= int(c) <= 9999:
                return True
            else:
                return False


# a is months, b is days, c is years
# x is months, y is days, z is years


def format(string):
    if "/" in string:
        a, b, c = string.split("/")
        a, b, c = int(a), int(b), int(c)
        if 1 <= b <= 9 and 1 <= a <= 9:
            print(f"{c}-{a:02}-{b:02}")
        elif 1 <= b <= 9:
            print(f"{c}-{a}-{b:02}")
        elif 1 <= a <= 9:
            print(f"{c}-{a:02}-{b}")
        else:
            print(f"{c}-{a}-{b}")
    else:
        parts = string.split(",")
        x, y = parts[0].split(" ")
        z = parts[1]
        x = x.title()
        if x in months:
            x = int(months.index(x)) + 1
        y, z = int(y), int(z)
        if 1 <= x <= 9 and 1 <= y <= 9:
            print(f"{z}-{x:02}-{y:02}")
        elif 1 <= x <= 9:
            print(f"{z}-{x:02}-{y}")
        elif 1 <= y <= 9:
            print(f"{z}-{x}-{y:02}")

        else:
            print(f"{z}-{x}-{y}")