def main():
    word = input("Input: ")
    print(shorten(word))


# expect str and returns str without vowels
def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # loops through vowels, changing every vowel to "" and assigning them to a new string 'word'
    # old string remains, but will not longer be assigned to 'word' and become garbage values
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()

# key learning point: string are immutable, to 'change' a string, need to create a new string and add the desired characters to the new string

# Alternative method: loop through all characters in word, identify the vowels, replace them and assign to new string 'word'
'''
    for character in word:
        if character in vowels:
            word = word.replace(character, "")
    return word
'''
# Alternative method: Manually create new string, loop through word, apend new string, while retaining 'word' as old string
'''
    shortened_word = ""
    for i in range(len(word)):
        if word[i] in vowels:
            shortened_word += ""
        else:
            shortened_word += word[i]
    return shortened_word
'''
# Alternative method: replace_all just prints all everything, returning nothing to main
'''
def main():
    sentence = input("Input: ")
    replace_all(sentence)
    print()


def replace_all(sentence):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for character in sentence:
        if character in vowels:
            character = str(character).replace(character, "")
        print(character, end="")


main()
'''