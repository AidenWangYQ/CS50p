# program can count number of lines of code in a python file
# done by opening file, reading file and appending to a list, counting length of list

import sys


def main():
    check_input()
    lines = []
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not (line.strip() == "" or line.strip().startswith("#")):
                    lines.append(line)
        print(len(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")


# exit if sys.argv[1] does not end with .py or exist or there is more than 1 command-line argument
def check_input():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


main()


# when using open(file), if file is sys.argv[], do not use ""
# tuple must add (), .startswith() only accepts 1 argument, but can take a tuple of prefixes