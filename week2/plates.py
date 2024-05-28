def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # check if s is of correct length and if all its digits are alphanumeric
    if 2 <= len(s) <= 6 and s.isalnum():

        # for the case of all 6 characters of s being alphabetic
        if s.isalpha():
            return True

        # for the cases of the first 2 or 3 or 4 characters of s being alphabetic
        if s[:2].isalpha() or s[:3].isalpha() or s[:4].isalpha():
            # check if number starts with 0, by looping through every character in s
            for i in range(len(s)):
                if str(s[i]).isalpha() and str(s[i + 1]).isnumeric() and s[i + 1] == "0":
                    return False
            # check with there is a letter following a number, making sure that i is not big enough to exceed the range of s
            for i in range(len(s)):
                if (i <= len(s) - 2) and str(s[i]).isnumeric() and str(s[i + 1]).isalpha():
                    return False
            # if all conditions are right
            return True

        # for the case of the first 5 characters of s being alphabetic
        if s[:5].isalpha():
            # check if number starts with 0
            if s.startswith("0"):
                return False
            else:
                return True


main()

# is_valid should return True or False
# start with at least 2 letters
# max 6 characters (letters or number) min 2 characters
# cannot have letter after number
# first number cannot be 0
# no periods, spaces or punctuation