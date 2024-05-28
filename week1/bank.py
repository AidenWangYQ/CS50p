def main():
    greeting = input("Greeting: ").lower().strip()
    print(calculate(greeting))


def calculate(x):
    # if starts with hello
    if x.startswith("hello"):
        return "$0"
    # else if starts with h
    elif x.startswith("h"):
        return "$20"
    # else
    else:
        return "$100"


main()