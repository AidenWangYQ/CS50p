# create infinite loop which asks user for prompt
# user input is placed in a dict, sorted in alphabetical order(using sorted)
# use something to increase value of each key in dict
# clt-d to break loop and print out the keys and values(iterate over dictionary)
# take note of KeyError and EOFError(terminate&print)

def main():
    items = {}
    while True:
        try:
            item = input().strip().upper()
            if item not in items:
                items[item] = 1
            else:
                items[item] = items[item] + 1
        except EOFError:
            for item in sorted(items):
                print(items[item], item)
            break


main()