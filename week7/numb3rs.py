import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    range = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    if matches := re.search(rf"^{range}\.{range}\.{range}\.{range}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

# in regexes, it is incorrect to write [0-255] to find range between 0-255, as re finds the specific pattern of numbers instead of the number itself
# in rf string, \. is interpreted as literally a period, \\. is used to mean literal backslash and a random character
# in r string, in the context of regexes, \ is an escape character, in a normal context without regexes, \ means literally backslash