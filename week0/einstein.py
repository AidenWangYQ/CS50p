def main():
    mass = int(input("m: "))
    print(f"e: {formulated(mass)}")


def formulated(m):
    c = 300000000
    e = m * (c**2)
    return e


main()