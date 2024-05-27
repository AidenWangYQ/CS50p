def main():
    sentence = input()
    print(emoted(sentence))


def emoted(x):
    x = x.replace(":)","🙂").replace(":(","🙁")
    return x


main()