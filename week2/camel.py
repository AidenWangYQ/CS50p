# request for camelname
# iterate through name, break upon seeing uppercase
# print _ when after break, case uppercase into lowercase
# continue loop

def main():
    name = input("camelCase: ")
    snake(name)


def snake(name):
    for character in name:
        if character.isupper():
            character = character.lower()
            print("_", end="")
        print(character, end="")
    print()


main()