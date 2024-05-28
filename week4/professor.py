# prompt user for level(1,2,3)(n) or else reprompt
# creates 10 addition problems in X+Y format, where X&Y are positive integers with n digits
# ask question, if answer incorrect, display EEE up to 3 times, then display correct answer, record correct/wrong answer
# collate score and display
import random
import sys


def main():
    level = get_level()
    questions = {}
    score = 0
    while len(questions) < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        quiz = str(x) + " + " + str(y) + " = "
        solution = x + y
        questions[quiz] = solution
    for question in questions:
        answer = int(input(question))
        if answer == questions[question]:
            score += 1
        else:
            print("EEE")
            answer = int(input(question))
            if answer == questions[question]:
                score += 1
            else:
                print("EEE")
                answer == int(input(question))
                if answer == questions[question]:
                    score += 1
                else:
                    print("EEE")
                    answer = questions[question]
                    question = question.rstrip()
                    print(question, answer)
                    continue
    print(f"Score: {score}")
    sys.exit(0)


# prompts user for level, looping if wrong format, returns 1,2 or 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


# randomly generates positive integer with n digits, if n != 1, 2 , 3 , return ValueError(by raising in exception)
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2 or level == 3:
        smallest_value = 10 ** (level - 1)
        largest_value = (10 ** level) - 1
        return random.randint(smallest_value, largest_value)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
    