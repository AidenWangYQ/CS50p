# has emoji.emojize module, set language to 'alias' to gain access to additional aliases
import emoji


def main():
    expression = input("Input: ")
    print(f"Output: {emoji.emojize(expression, language='alias')}")


main()