# Set up infinite loop, which reprompts for name, terminated with clt-d (EOFError)
# When terminated, print desired message
# Set up a list which adds names to it. Upon termination, iterate over list, adding ','&' ' before and after every name except for last. (slice list?)
# did not use inflect in this code, but upon review could have used inflect.engine.join(names) to simplify the joining of names instead of considering multiple cases

def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names += [name]
        except EOFError:
            print("\n", end="")
            break
    print(f"Adieu, adieu, to {names[0]}", end="")
    if len(names) == 2:
        print(f" and {names[1]}")
    elif len(names) == 3:
        print(f", {names[-2]}, and {names[-1]}")
    elif len(names) >= 4:
        for name in names[1:-2]:
            name_1 = ", " + name
            print(name_1, end="")
        print(f", {names[-2]}, and {names[-1]}")
    else:
        exit(0)


main()