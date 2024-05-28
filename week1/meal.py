def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    if time.find("a.m.") != -1:
        time = time.removesuffix("a.m.")
        hours, minutes = time.split(":")
        minutes = round((float(minutes) / 60), 2)
        return float(hours) + minutes
    elif time.find("p.m.") != -1:
        time = time.removesuffix("p.m.")
        hours, minutes = time.split(":")
        minutes = round((float(minutes) / 60), 2)
        hours = float(hours) + 12
        return hours + minutes
    else:
        hours, minutes = time.split(":")
        minutes = round((float(minutes) / 60), 2)
        return float(hours) + minutes


if __name__ == "__main__":
    main()