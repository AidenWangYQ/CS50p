def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    calculate(x, y, z)


def calculate(x, y, z):
    if y == "+":
        result = round((x + z), 1)
        print(result)
    elif y == "-":
        result = round((x - z), 1)
        print(result)
    elif y == "*":
        result = round((x * z), 1)
        print(result)
    else:
        result = round((x / z), 1)
        print(result)


main()