def main():
    sentence = input()
    print(slowed(sentence))


def slowed(x):
    x = x.replace(" ", "...")
    return x


main()